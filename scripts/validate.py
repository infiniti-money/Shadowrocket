#!/usr/bin/env python3
"""Static checks for domain-only Shadowrocket modules."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FILES = [ROOT / "modules/AdBlock-Lite.sgmodule", ROOT / "modules/AdBlock-Lite.module"]
RULE = "RULE-SET,https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Shadowrocket/AdvertisingLite/AdvertisingLite.list,REJECT"
FORBIDDEN = ("[mitm]", "[script]", "[header rewrite]", "[url rewrite]", "[map local]", "script-path=", "hostname =")
for path in FILES:
    assert path.is_file(), f"Missing {path}"
    contents = path.read_text(encoding="utf-8")
    lowered = contents.lower()
    assert not any(term in lowered for term in FORBIDDEN), f"Unexpected active MITM/rewrite in {path}"
    assert "[Rule]" in contents, f"Missing [Rule] in {path}"
    rules = [line.strip() for line in contents.splitlines() if line.strip() and not line.lstrip().startswith("#") and not line.startswith("[")]
    assert rules == [RULE], f"Unexpected rules: {path}: {rules}"
print("PASS: expected domain-only rules; no MITM or scripts")
