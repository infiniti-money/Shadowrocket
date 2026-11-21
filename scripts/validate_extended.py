#!/usr/bin/env python3
"""Static structural check of Extended v2.1; does NOT approve JS or HTTPS decryption."""
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
module = ROOT / "modules/Infiniti-All-In-One-Extended.sgmodule"
data = module.read_text(encoding="utf-8")
lines = data.splitlines()
inventory = json.loads((ROOT / "research/all-script-inventory.json").read_text(encoding="utf-8"))
expected_sources = {row["url"] for row in inventory["scripts"]}
source_lines = [line for line in lines if line.startswith("# Source: ")]
actual_sources = {line.partition("# Source: ")[2].strip() for line in source_lines}
assert len(expected_sources) == len(inventory["scripts"]) == 39, "Unexpected script inventory size"
assert len(source_lines) == 39 and actual_sources == expected_sources, "Missing/duplicate archived script URL"
assert len([line for line in lines if line.startswith("# JS-")]) == 39, "Missing JS labels"

sections = re.findall(r"(?m)^\[([^\]]+)\]\s*$", data)
assert sections == ["Rule", "Header Rewrite", "Url Rewrite", "Script", "MITM"], sections

def active_in(section):
    content = data.split(f"[{section}]\n", 1)[1].split("\n[", 1)[0]
    return [line.strip() for line in content.splitlines() if line.strip() and not line.lstrip().startswith("#")]

rule = active_in("Rule")
# Index lines are all comments; only 3 rule sets may be active.
expected_rules = [
    "RULE-SET,https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Shadowrocket/Advertising/Advertising.list,REJECT",
    "RULE-SET,https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Shadowrocket/Privacy/Privacy.list,REJECT",
    "RULE-SET,https://raw.githubusercontent.com/bigdargon/hostsVN/master/extensions/threat/surge-rule.conf,REJECT",
]
assert rule == expected_rules, f"Unexpected rules: {rule}"
assert len(active_in("Header Rewrite")) == 1, "Unexpected header rewrite count"
assert len(active_in("Url Rewrite")) == 3, "Unexpected URL rewrite count"
script = active_in("Script")
assert len(script) == 4, "Expected exactly four experimental scripts"
assert all("script-path=https://" in line for line in script), "Invalid script path"
mitm = active_in("MITM")
assert len(mitm) == 1 and mitm[0].startswith("hostname = %APPEND% "), "Invalid MITM directive"
assert mitm[0].count("%APPEND%") == 1, "Duplicate MITM append marker"
hosts = [h.strip() for h in mitm[0].split("=", 1)[1].replace("%APPEND%", "", 1).split(",")]
assert len(hosts) == len(set(hosts)) == 5 and all(hosts), "Invalid/duplicated hostnames"

print("PASS: Extended v2.1 has 39 indexed sources and 4 active script declarations")
print("WARNING: Active MITM/third-party JS exists; no safety, runtime or Premium guarantees")
