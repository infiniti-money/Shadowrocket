#!/usr/bin/env python3
"""Validate consolidated Extended v3: structure, source index and no embedded CA secrets."""
from pathlib import Path
import json
import re

root = Path(__file__).resolve().parents[1]
path = root / "modules/Infiniti-All-In-One-Extended.sgmodule"
content = path.read_text(encoding="utf-8")
lines = content.splitlines()
inv = json.loads((root / "research/all-script-inventory.json").read_text(encoding="utf-8"))
expected = {v["url"] for v in inv["scripts"]}
actual_lines = [line.removeprefix("# Source: ").strip() for line in lines if line.startswith("# Source: ")]
assert len(expected) == len(inv["scripts"]) == len(actual_lines) == 39
assert set(actual_lines) == expected, "Script source inventory mismatch"
assert not re.search(r"(?im)^\s*(?:ca-p12|ca-passphrase)\s*=", content), "Private CA fields must never be committed"
sections = re.findall(r"(?m)^\[([^\]]+)\]\s*$", content)
assert sections == ["Rule","Header Rewrite","Url Rewrite","Map Local","Script","MITM"], sections
def active(section):
    text = content.split("[" + section + "]\n", 1)[1].split("\n[", 1)[0]
    return [line.strip() for line in text.splitlines() if line.strip() and not line.strip().startswith("#")]
expected_counts = {"Rule":5,"Header Rewrite":2,"Url Rewrite":8,"Map Local":1,"Script":22,"MITM":1}
for section,count in expected_counts.items():
    assert len(active(section)) == count, (section,len(active(section)),count)
for line in active("Script"):
    assert "script-path=https://" in line and "type=" in line, line
mitm = active("MITM")[0]
assert mitm.startswith("hostname = %APPEND% ") and mitm.count("%APPEND%")==1
hosts=[v.strip() for v in mitm.split("=",1)[1].replace("%APPEND%","",1).split(",")]
assert len(hosts)==len(set(hosts))==22
print("PASS: Extended v3 merged 22 JS declarations and 22 MITM host patterns")
print("PASS: 39 source references and no embedded private CA")
print("WARNING: 404 URLs, script correctness and iOS TLS trust are NOT tested")
