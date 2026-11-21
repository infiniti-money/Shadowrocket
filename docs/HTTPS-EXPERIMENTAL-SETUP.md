# Infiniti Extended HTTPS Experimental — import troubleshooting

The screenshot of `Infiniti-All-In-One-Extended.sgmodule` showing **Quy tắc: 3; Giải mã HTTPS: 0; Kịch bản: 0** is expected. The Extended Safe module deliberately contains only three `RULE-SET` entries; all 39 script URLs are commented references, not executable entries.

## New opt-in file

```text
https://raw.githubusercontent.com/infiniti-money/Shadowrocket/main/modules/opt-in/Infiniti-Extended-HTTPS-Experimental.sgmodule
```

This is a **separate** module with:
- `[Rule]`: Advertising, Privacy and Vietnam threat protection (3 rulesets).
- `[Header Rewrite]`: 1 Spotify cache-related header rule.
- `[Url Rewrite]`: 3 YouTube endpoint reject rules.
- `[Script]`: 4 external JS script declarations (Spotify ×2, Locket ×2).
- `[MITM]`: 5 hostname patterns scoped to Spotify, YouTube and **shared** RevenueCat API.

This file does not enable all 39 archival JavaScript references, and does not grant authentic Spotify, YouTube, Locket or other Premium subscriptions.

## How to verify import on iPhone

1. Back up the active Shadowrocket configuration.
2. Disable (but don't delete) `Infiniti-All-In-One-Extended`, the standard All-in-One, and any overlapping standalone Spotify/Locket/YouTube modules. Don't enable two different all-in-one modules simultaneously.
3. Import the **new file** through the RAW URL above. The displayed module title should include **Extended HTTPS - Experimental**, not **Extended - Safe**.
4. View module details. If parsed, you should see nonzero Script and HTTPS Decryption counts in the module. **These numbers only indicate parsed declarations, not successful TLS decryption or working scripts.**
5. HTTPS Decryption/CA trust cannot be activated by publishing a GitHub file: it must be configured explicitly in Shadowrocket/iOS. Use this only in an authorized test environment. Do not trust unknown certificates or expose primary accounts.
6. Test one app at a time. Check Shadowrocket event logs for inability to download JS, pattern mismatches, timeout, TLS trust failures, certificate pinning or rewrite failures.
7. If network connections break, disable the experimental module and HTTPS Decryption, and restore the backed-up configuration.

## Critical risks

- MITM `api.revenuecat.com` is **shared across unrelated apps**. Its presence can impact far more than Locket.
- Scripts from third-party mutable `main`/`master` branches have not been fully audited and may change.
- Paid features may be enforced by app backend and cannot be legitimately restored by forging entitlement flags. Use official Restore Purchases for subscriptions already purchased.
- Device import and actual iOS behavior **have not been tested** by this repository's CI.

The main module remains MITM-free at:
`modules/Infiniti-All-In-One-Extended.sgmodule`.
