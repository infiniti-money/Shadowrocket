# Infiniti All-in-One Ultimate v3.3 — ALL 39 SCRIPT URLS ENABLED (HIGH RISK)

The user's original Extended module URL has been updated **in place**:

```text
https://raw.githubusercontent.com/infiniti-money/Shadowrocket/main/modules/Infiniti-All-In-One-Extended.sgmodule
```

This is an experimental Shadowrocket **module**, not a complete VPN/proxy server profile.

## Active module sections

| Section | Active entries |
|---|---:|
| `[Rule]` | 5 |
| `[Header Rewrite]` | 2 |
| `[Url Rewrite]` | 5 |
| `[Map Local]` | 1 |
| `[Script]` | **39 unique source URLs** |
| `[MITM]` | 1 directive with **26 host patterns** |

Scripts are individually named `SRC_01_...` through `SRC_39_...` to avoid duplicate declaration names. Their original source URLs are retained. The first matching original declaration per URL was reused, with minor normalization such as whitespace and dropping unresolved script arguments. This prevents duplicate URL declarations, but does NOT prevent overlap of request/response patterns or API handlers.

## Important caveats

- **20 of 39 URLs** in the existing repository inventory previously returned HTTP 404. These have now been **enabled** at the user's explicit request; Shadowrocket may fail to download and execute them.
- Competing Spotify, Locket, RevenueCat and YouTube scripts can process the same endpoints and conflict. Multiple Locket/RevenueCat scripts may modify subscription data of unrelated apps.
- This release is **not tested on iPhone** and does not guarantee Premium access, ad blocking inside every application, or smooth network connectivity.
- MITM host patterns do not cause iOS to trust a CA. Install and manage any authorized test CA **locally**. No `ca-p12` private key or `ca-passphrase` is stored on GitHub.
- Do not enable alongside other all-in-one or per-app experimental modules. Back up your active configuration, use a test device/account, and disable this module if you encounter TLS/login/network errors.

## Validation

```bash
python3 scripts/validate_extended.py
python3 scripts/check_script_sources.py --online
```

CI verifies the number of declarations, URL uniqueness, static sections and secret absence. It cannot verify JS code safety, runtime behavior or a valid subscription.

To return to a safe ad/privacy filter without MITM, use:
`https://raw.githubusercontent.com/infiniti-money/Shadowrocket/main/modules/Infiniti-All-In-One.sgmodule`
