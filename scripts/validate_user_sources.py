#!/usr/bin/env python3
"""Check uploaded Shadowrocket source archives and experimental merge.

Security boundary: CA PKCS#12 keys and passphrases must never be stored in Git.
This only checks static structure, NOT safety/functionality of scripts.
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
FILES = [
    ROOT / "sources/user-uploads/10in1_Vip_ProMax.sanitized.conf.txt",
    ROOT / "sources/user-uploads/All_In_One.sanitized.conf.txt",
    ROOT / "modules/opt-in/Full-Source-Merge-Experimental.sgmodule",
]
for path in FILES:
    assert path.exists(), f"Missing {path}"
    s = path.read_text(encoding="utf-8")
    assert not re.search(r"(?im)^\s*(?:ca-p12|ca-passphrase)\s*=", s), (
        f"Private certificate material may be present: {path}"
    )
    assert "[Script]" in s and "[MITM]" in s, f"Missing expected sections: {path}"
    print(f"PASS: no embedded CA fields in {path.relative_to(ROOT)}")

merged = FILES[-1].read_text(encoding="utf-8")
sections = re.findall(r"(?m)^\[([^\]]+)\]\s*$", merged)
assert sections == ["Rule", "URL Rewrite", "Header Rewrite", "Map Local", "Script", "MITM"], sections

def active_section(section):
    value = merged.split("[" + section + "]", 1)[1].split("\n[", 1)[0]
    return [
        line.strip() for line in value.splitlines()
        if line.strip() and not line.strip().startswith("#")
    ]

expected = {"Rule": 5, "URL Rewrite": 5, "Header Rewrite": 2,
            "Map Local": 1, "Script": 24, "MITM": 1}
for section, size in expected.items():
    lines = active_section(section)
    assert len(lines) == size, f"{section}: expected {size}, got {len(lines)}"
assert all("script-path=https://" in line for line in active_section("Script"))
hostname = active_section("MITM")[0]
assert hostname.startswith("hostname = %APPEND% "), hostname
assert hostname.count("%APPEND%") == 1, hostname
hosts = [x.strip() for x in hostname.split("=", 1)[1].replace("%APPEND%", "", 1).split(",")]
assert hosts and all(hosts) and len(hosts) == len(set(hosts))
print(f"PASS: experimental full merge has 24 scripts and {len(hosts)} MITM patterns")
print("WARNING: many remote scripts may return 404; no runtime/Premium validation performed")
