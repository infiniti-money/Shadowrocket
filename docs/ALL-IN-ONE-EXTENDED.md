# Infiniti All-in-One Extended v2.0

This is a **single, installable Shadowrocket module** that combines actively loaded ad, privacy, and Vietnam threat-domain lists and indexes all **39** script-path references from the reviewed iOS ecosystem in an **inactive comments-only registry**.

**RAW URL**
```text
https://raw.githubusercontent.com/infiniti-money/Shadowrocket/main/modules/Infiniti-All-In-One-Extended.sgmodule
```

## Currently enabled

- Advertising (blackmatrix7)
- Privacy (blackmatrix7)
- Threat-domain extension (bigdargon/hostsVN)

All three are loaded as `RULE-SET,...,REJECT` under `[Rule]`. Depending on your apps, stricter blocking may break websites; disable and review REJECT logs if needed.

## Complete script catalog, not active interception

The module includes 39 external JavaScript source URLs as `# Source:` comment lines. Grouped into YouTube, Spotify, Locket/RevenueCat, Sub-Store and other iOS apps. These are **references**, not working or imported scripts. External original files and opt-in experimental modules are preserved.

Why not activate all 39? Some original URLs previously returned 404; others require different parameter conventions, may target the same API responses, can alter subscription entitlements, or require broad MITM. Running everything together would likely conflict. GitHub can also only publish your module, not change Shadowrocket settings on your iPhone.

## Comparing installation options

| File | Advertising | Privacy | Vietnam threat domains | JS script catalog | Active external JS/MITM |
|---|---|---|---|---|---|
| `Infiniti-All-In-One.sgmodule` | Yes | Yes | No | No | No |
| `Infiniti-All-In-One-Extended.sgmodule` | Yes | Yes | Yes | 39 commented refs | No |
| `opt-in/All-Apps-Experimental.sgmodule` | Yes | Yes | No | 4 active scripts | Yes (unverified, high risk) |

**Do not enable the main and extended All-in-One simultaneously.** Extended is a replacement for the main domain-filtering module, not an add-on.

## Verify source inventory

```bash
python3 scripts/validate_extended.py
python3 scripts/check_script_sources.py --online
```

The first command ensures every indexed URL is listed exactly once and only three domain rule lists are enabled. The second checks network reachability but does not execute remote scripts. Both are static/network checks, **not** proof of iOS compatibility or working Premium entitlements.

See [all-script-inventory.json](../research/all-script-inventory.json) and [SCRIPT-VERIFICATION-WORKSPACE.md](SCRIPT-VERIFICATION-WORKSPACE.md) for source metadata, and [ALL-APPS-EXPERIMENTAL.md](ALL-APPS-EXPERIMENTAL.md) for the separate opt-in experimental rewrite module.

## Licensing and safety

Script sources belong to their respective authors; this repository stores URLs rather than claiming ownership or duplicating JavaScript. Never publish private MITM CA keys or captured traffic with secrets. For legitimate Premium access, use the app's official purchase restoration mechanism.
