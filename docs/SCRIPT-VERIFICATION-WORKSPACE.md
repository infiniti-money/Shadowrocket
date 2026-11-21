# All iOS Script Sources — Verification Workspace

This repository inventories **39 distinct external script-path URLs** collected from the provided Gaucuto and duyvinh09 configurations, the existing opt-in All-Apps module, and public third-party source modules (Spotify, Locket, YouTube, SoundCloud, Truecaller and additional iOS apps). Source-specific counts and availability can change.

## What was added
- [all-script-inventory.json](../research/all-script-inventory.json) — 39 script-path URL references, original naming, source file and preliminary availability note.
- [check_script_sources.py](../scripts/check_script_sources.py) — optional HEAD/partial GET status check, **no JavaScript execution and no JS files downloaded or copied into this repository**.
- Existing original modules in `modules/experimental/` preserve their script declarations; their content may be broken or unsafe to import.
- `modules/opt-in/` contains independently installed *experimental* configs, not a working combined Premium unlock for every app.

## Verification commands

```bash
python3 scripts/check_script_sources.py
python3 scripts/check_script_sources.py --online
python3 scripts/check_script_sources.py --online --json
```

Offline mode reports previous status notes. Online mode checks that links currently respond over HTTP; some hosts reject HEAD and fall back to a partial GET. Online checks may take time or be rate-limited. The tool **does not evaluate** the scripts.

## App groups

- **YouTube:** multiple request/response engines; some use minified or compiled JS and require special arguments.
- **Spotify:** different JSON/protobuf scripts from app2smile, duyvinh09 and KhunTam; do not activate mutually conflicting versions simultaneously.
- **Locket / RevenueCat:** several script versions; `api.revenuecat.com` serves many apps, so host-only interception is not restricted to Locket.
- **SoundCloud, Alight Motion, PicsArt, Wink, Truecaller, KineMaster, CamScanner, BeautyPlus, VSCO, Lightroom, Snow, Meitu and iTunes:** archived references for independent evaluation.
- **Sub-Store:** release artifacts from its own project, including a cron task. Not a Premium entitlement script.

## Validation status

- A **previous GitHub API check** returned 404 for `duyvinh09/Module_IOS` dependencies. A 404 can reflect deletion, rename, privacy or access limitations.
- `app2smile` Spotify scripts and `HuuTriet` Locket scripts were individually retrievable in previous checks.
- Third-party references in this inventory were extracted from publicly retrieved modules; **not all 39 were individually checked or audited**.
- No script was claimed to work on current iOS or to represent an authentic Premium subscription.
- The normal `Infiniti-All-In-One.sgmodule` **has not been changed** and remains free of MITM and JS.

## Evaluating scripts safely

Inspect authorship, licensing, script-path trust, response alteration, app version, URL matching and MITM hostname scope before importing. Do not commit private CA keys, captured tokens, user credentials or response bodies. Validate one source in an environment you control; avoid financial, purchase or login endpoints. To recover already purchased Premium access, use the app's official Restore Purchases workflow.

**Important:** The files are indexed, not automatically enabled. Avoid importing all archival modules at once: duplicate RevenueCat rules, overlapping hostname scopes and broken dependencies are likely to cause errors.
