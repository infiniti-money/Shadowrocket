# Shadowrocket module repair and safety review

Review date: 2026-11-21. Source materials: user-provided archive and upstream GitHub URLs.

## Summary
**No original Premium/Unlock functions have been validated or restored.** The goal was to make safe importable domain-only alternatives, preserve historical references, and document reasons for disabling unsafe or unavailable behavior.

| Original | Preserved | Reviewed module |
|---|---|---|
| Gaucuto `10in1_Vip_ProMax` | `modules/experimental/10in1_Vip_ProMax.sgmodule` | `modules/reviewed/Gaucuto_10in1_Safe.sgmodule` |
| duyvinh09 `All_In_One.sgmodule` | `modules/experimental/All_In_One_duyvinh09.sgmodule` | `modules/reviewed/DuyVinh_All_In_One_Safe.sgmodule` |

## Confirmed findings

1. **Source availability:** `duyvinh09/Module_IOS` and sampled JavaScript paths returned GitHub API 404 on 2026-11-21. This can mean deletion, rename, privacy or access restrictions; don't relabel as definitely deleted. The user provided the full All In One configuration, but its original RAW file could not be independently retrieved.
2. **Invalid/unresolved placeholder in duyvinh09:** `engine={{{script}}}` is an unresolved template marker unless an external substitution mechanism fills it. `engine=jsc` is found elsewhere, but it would be unsafe to re-enable the unavailable YouTube JavaScript by guessing its runtime.
3. **Malformed VSCO script definition:** `VSCO = type=http-request ^https://... script-path=...` lacks `pattern=` and commas between parameters. If ever restored with an audited, available script, its *syntax* would need `type=http-request,pattern=...,script-path=...`, not the original spaces.
4. **Empty MITM entry:** `photos.adobe.io, , ap*.intsig.net` contains an empty hostname entry. A syntactic cleanup would collapse the duplicated comma, but these reviewed modules omit MITM entirely instead.
5. **Ambiguous CamScanner pattern:** `pattern= https:\/\/` includes an unnecessary space after the equals sign; trim it if attempting a future syntactic repair.
6. **RevenueCat duplication and scope:** multiple scripts target overlapping `api.revenuecat.com` subscriber/receipts paths. Such rules may conflict, and broad TLS interception affects unrelated apps.
7. **YouTube request/response:** both refer to `youtube.response.js`; a script can sometimes handle both event types, so don't call this an unconditional parsing error. Source cannot currently be audited.
8. **Gaucuto:** upstream uses `duyvinh09` scripts and `app2smile` scripts. The latter Spotify JS URLs were retrievable on review; availability is not a security endorsement.
9. **Sub-Store:** release names existed in GitHub releases; direct asset download compatibility was not fully tested. Scheduling and rewrite rules are excluded to avoid unrelated background activity.
10. **UDP REJECT for googlevideo/youtubei:** could force transport fallbacks or cause playback problems. Disabled in reviewed variants.

## Changes applied

- The two archived originals remain unchanged; they are **not automatically enabled** by the safe modules.
- The reviewed modules contain exactly one `AdvertisingLite` RULE-SET and no active `[MITM]`, `[Script]`, HTTP rewrites, or `Map Local`.
- Validator checks active entries in all safe modules and reports red flags in both original archives.
- No JavaScript or certificate is installed; no source from a different author was silently substituted.
- The AdvertisingLite upstream list is dynamic; review a pinned revision for reproducibility.

## How to test

1. Run `python3 scripts/validate.py`.
2. Check GitHub Actions workflow `Validate Shadowrocket modules`.
3. Back up Shadowrocket configuration, then import **one** `modules/reviewed/*Safe.sgmodule`.
4. Do not enable HTTPS decryption for these reviewed modules.
5. Check connectivity and REJECT log in Safari, YouTube, TikTok, and games. If issues occur, disable the new module or whitelist the specific false-positive domain.
6. Do not assume Premium, YouTube in-app ads, or App Store purchases are unlocked; the reviewed variants intentionally omit that behavior.

Static checks and GitHub CI are not a substitute for an actual Shadowrocket iOS parser/import test. No phone testing was performed.

## Sources
- https://github.com/Gaucuto/Gauapple/blob/main/10in1_Vip_ProMax
- https://raw.githubusercontent.com/duyvinh09/Module_IOS/refs/heads/main/All_In_One.sgmodule (404 during review)
- https://github.com/app2smile/rules
- https://github.com/sub-store-org/Sub-Store
- https://github.com/blackmatrix7/ios_rule_script
