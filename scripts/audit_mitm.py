#!/usr/bin/env python3
"""Report potentially sensitive MITM configuration in archived/opt-in modules.

Read-only static reporting. Doesn't modify files, import modules, enable MITM,
or evaluate remote scripts. Exit zero so archives can be studied safely.
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
TARGETS = ["modules/opt-in", "modules/experimental"]
SENSITIVE = ("revenuecat.com", "itunes.apple.com", "accounts.", "login.", "bank", "paypal")

for folder in TARGETS:
    for path in sorted((ROOT / folder).glob("*.sgmodule")):
        data = path.read_text(encoding="utf-8")
        parts = re.split(r"(?m)^\[MITM\]\s*$", data, maxsplit=1, flags=re.I)
        if len(parts) < 2:
            print(f"{path.relative_to(ROOT)}: no MITM section")
            continue
        mitm = parts[1].split("\n[", 1)[0]
        hostline = next((line for line in mitm.splitlines()
                         if line.strip().lower().startswith("hostname")), "")
        hosts = [s.strip() for s in hostline.partition("=")[2].split(",")
                 if s.strip() and s.strip() != "%APPEND%"]
        risk = [h for h in hosts if any(term in h.lower() for term in SENSITIVE)]
        script_count = len(re.findall(r"(?m)^\s*[^#\n].*script-path=", data))
        print(f"{path.relative_to(ROOT)}: hosts={len(hosts)}, scripts={script_count}, "
              f"sensitive_scopes={risk or 'none identified'}")
print("Report only: no module or device settings were changed.")
