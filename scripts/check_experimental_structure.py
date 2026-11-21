#!/usr/bin/env python3
"""Check structure of combined experimental module, not script safety or success."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "modules/opt-in/All-Apps-Experimental.sgmodule"
text = PATH.read_text(encoding="utf-8")
sections = re.findall(r"(?m)^\[([^\]]+)\]\s*$", text)
expected = ["Rule", "Header Rewrite", "Url Rewrite", "Script", "MITM"]
assert sections == expected, f"Unexpected sections: {sections}"

block = text.split("[MITM]", 1)[1]
active = [row.strip() for row in block.splitlines()
          if row.strip() and not row.lstrip().startswith("#")]
assert len(active) == 1 and active[0].startswith("hostname ="), "Invalid MITM section"
hostnames = active[0].split("=", 1)[1].split(",")
assert hostnames[0].strip().startswith("%APPEND% "), "Missing single initial %APPEND%"
assert active[0].count("%APPEND%") == 1, "Duplicate %APPEND% found"
names = [host.strip().replace("%APPEND% ", "", 1) for host in hostnames]
assert len(names) == len(set(names)), "Duplicate hostnames found"
assert "" not in names, "Empty hostname found"

script_block = text.split("[Script]", 1)[1].split("[MITM]", 1)[0]
script_lines = [row.strip() for row in script_block.splitlines()
                if row.strip() and not row.lstrip().startswith("#")]
assert len(script_lines) == 4, f"Expected 4 scripts, found {len(script_lines)}"
assert all("script-path=https://" in row for row in script_lines), "Missing script URL"
print("PASS: experimental combined module has consistent sections and one MITM append marker")
print("NOTE: Scripts are unreviewed and premium functionality is not verified")
