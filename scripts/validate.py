#!/usr/bin/env python3
"""Static safety and syntax audit for Shadowrocket modules (no iOS runtime claims)."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
RULE = "RULE-SET,https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Shadowrocket/AdvertisingLite/AdvertisingLite.list,REJECT"
SAFE_MODULES = [
    "modules/Infiniti-All-In-One.sgmodule",
    "modules/AdBlock-Lite.sgmodule",
    "modules/AdBlock-Lite.module",
    "modules/reviewed/Gaucuto_10in1_Safe.sgmodule",
    "modules/reviewed/DuyVinh_All_In_One_Safe.sgmodule",
]
ORIGINAL_MODULES = [
    "modules/experimental/10in1_Vip_ProMax.sgmodule",
    "modules/experimental/All_In_One_duyvinh09.sgmodule",
]
FULL_RULES = [
    "RULE-SET,https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Shadowrocket/Advertising/Advertising.list,REJECT",
    "RULE-SET,https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Shadowrocket/Privacy/Privacy.list,REJECT",
]
FORBIDDEN_SECTIONS = {"[mitm]", "[script]", "[header rewrite]", "[url rewrite]", "[map local]"}
failures = []

for name in SAFE_MODULES:
    path = ROOT / name
    if not path.is_file():
        failures.append(f"{name}: missing safe module")
        continue
    lines = [line.strip() for line in path.read_text(encoding="utf-8").splitlines()]
    active = [line for line in lines if line and not line.startswith("#")]
    if any(line.lower() in FORBIDDEN_SECTIONS for line in active):
        failures.append(f"{name}: contains a forbidden active section")
    if any("script-path=" in line.lower() or "hostname =" in line.lower() for line in active):
        failures.append(f"{name}: contains active script or MITM hostname")
    if "[Rule]" not in active:
        failures.append(f"{name}: missing [Rule]")
    rules = [line for line in active if not line.startswith("[")]
    expected = FULL_RULES if name.endswith("/Infiniti-All-In-One.sgmodule") else [RULE]
    if rules != expected:
        failures.append(f"{name}: unexpected active rules: {rules}")

print("=== Experimental originals (audit only; NOT approved for installation) ===")
for name in ORIGINAL_MODULES:
    path = ROOT / name
    if not path.is_file():
        failures.append(f"{name}: archive missing")
        continue
    content = path.read_text(encoding="utf-8")
    lines = content.splitlines()
    urls = set(re.findall(r"script-path=(https?://[^,\s]+)", content))
    unavailable_refs = sorted(url for url in urls if "duyvinh09/Module_IOS/" in url)
    report = [
        f"{name}: script paths={len(urls)}, duyvinh09 dependency paths={len(unavailable_refs)}, "
        f"MITM={'[MITM]' in content}",
    ]
    for line in lines:
        s = line.strip()
        if s.startswith("#"):
            continue
        if "engine={{{script}}}" in s:
            report.append("  WARNING: unresolved script engine placeholder")
        if s.startswith("VSCO = ") and "pattern=" not in s:
            report.append("  WARNING: VSCO rule missing pattern= and separators")
        if s.startswith("hostname =") and re.search(r",\s*,", s):
            report.append("  WARNING: empty MITM hostname")
        if s.startswith("Camscanner =") and "pattern= " in s:
            report.append("  WARNING: space after pattern= may affect match")
    print("\n".join(report))

if failures:
    raise SystemExit("FAILED:\n" + "\n".join(failures))
print("PASS: safe/reviewed/all-in-one modules are domain-only; experimental originals reported, not validated as safe")
