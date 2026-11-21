# Premium and enhanced-feature recovery assessment

Review date: 2026-11-21. This is a technical recovery inventory, **not** an active Premium unlock module.

## Current result

The archived Gaucuto and duyvinh09 scripts cannot be safely re-enabled wholesale. The GitHub API returned 404 for `duyvinh09/Module_IOS` and several script URLs in the original configurations when tested. GitHub search engines can still index historical copies; a search snippet is not proof that a raw file is currently available.

A script that changes a client-side Premium flag cannot create a valid purchase or guarantee server-side entitlements. Do not use an iPhone's primary account or payment-related apps to test broad MITM or `verifyReceipt` manipulation.

## Apps and candidate sources

| App | Sources for review | What is technically feasible | Risk |
|---|---|---|---|
| YouTube / YouTube Music | https://github.com/Maasea/sgmodule ; https://github.com/YanbingJiang/Shadowrocket_diy_rules | Investigate ad and playback-response handling, PiP/background behavior; actual compatibility unverified | High if HTTPS MITM needed |
| Spotify | https://github.com/app2smile/rules | Original `spotify-json.js` and `spotify-proto.js` were retrievable on 2026-11-21; any modified playback or plan features remain unverified | High for HTTPS response interception |
| SoundCloud | https://github.com/llygad/Shadowrocket-modules | Community references exist; no audited drop-in replacement verified | High |
| Locket, PicsArt, VSCO, Wink, Alight Motion, etc. | User-provided archived configs in this repository | No trustworthy, verified working replacement was established | High |
| RevenueCat and App Store purchase status | Official app purchase receipt and entitlement APIs | Only restore legitimate purchases through the app/service's normal mechanisms | Very high for response tampering |

## Findings requiring repairs before any use

1. `duyvinh09` script dependencies must resolve to files with readable source. An HTTP 404 is a hard blocker; never silently point an unrelated script at a missing path.
2. `engine={{{script}}}` is unresolved in the archived All In One; the original module may have required a preprocessor. Do not replace it blindly.
3. VSCO rule is missing separators and `pattern=`. CamScanner pattern has suspicious space after `pattern=`.
4. `[MITM]` in duyvinh09 includes an empty hostname and broad purchase/entitlement domains; audited copies should minimize hostnames or omit MITM.
5. Multiple overlapping `api.revenuecat.com` scripts can race, and `buy.itunes.apple.com` receipt interception is unsafe on primary accounts.
6. YouTube DNS/domain blocking alone cannot reliably remove in-stream ads.
7. A source script accessible on GitHub does **not** prove that its runtime matches Shadowrocket, that it is safe, or that it unlocks legitimate Premium.

## Supported recovery paths

- **Ad blocking:** Use `modules/AdBlock-Lite.sgmodule` or one of `modules/reviewed/*Safe.sgmodule` for domain-only blocking, no MITM.
- **Legitimate Premium subscriptions:** If an app's paid features are missing despite an active subscription, verify Apple ID, sign into the right app account and use the application's **Restore Purchases** option. Contact vendor support when server-side entitlements fail.
- **Development or QA:** For an app that you own or are authorized to test, use a test environment or App Store sandbox and server-side entitlement checks rather than hardcoding Premium flags.
- **Other enhanced behaviors:** Evaluate a purpose-specific, reviewed source independently, pin to a commit, restrict hostname scope and test on a non-primary device before contemplating deployment.

## Status

No Premium-unlock module was installed, enabled or published as working. The original modules in `modules/experimental/` remain untouched; the reviewed safe modules remain domain-only.
