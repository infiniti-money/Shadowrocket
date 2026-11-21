#!/usr/bin/env python3
"""Verify the extended module inventories every external script without activating it."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
path = ROOT / "modules" / "Infiniti-All-In-One-Extended.sgmodule"
data = path.read_text(encoding="utf-8")
inventory = json.loads((ROOT / "research/all-script-inventory.json").read_text(encoding="utf-8"))
expected = {item["url"] for item in inventory["scripts"]}
lines = data.splitlines()

active = [line.strip() for line in lines if line.strip() and not line.lstrip().startswith("#")]
expected_rules = [
    "RULE-SET,https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Shadowrocket/Advertising/Advertising.list,REJECT",
    "RULE-SET,https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Shadowrocket/Privacy/Privacy.list,REJECT",
    "RULE-SET,https://raw.githubusercontent.com/bigdargon/hostsVN/master/extensions/threat/surge-rule.conf,REJECT",
]
assert active == ["[Rule]", *expected_rules], f"Unexpected active directives: {active}"
assert len(expected) == len(inventory["scripts"]), "Inventory contains duplicated URLs"
assert len(expected) == 39, "Verify changes to expected source count and update release notes"

source_lines = [line for line in lines if line.startswith("# Source: ")]
actual = {line.partition("# Source: ")[2].strip() for line in source_lines}
assert actual == expected, f"Missing/unknown JS source references: {expected ^ actual}"
assert len(source_lines) == len(actual), "Duplicate JS URL references in module"
assert data.count("# JS-") == len(expected), "Incorrect number of JS index entries"

print(f"PASS: All-in-One Extended has {len(expected)} indexed JS links, all inactive")
print("PASS: only Advertising, Privacy and hostsVN threat-domain rules are enabled")
