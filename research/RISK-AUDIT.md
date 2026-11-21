# Shadowrocket security research

This document is for defensive analysis. No premium-unlock scripts or subscription-response modifications are shipped or enabled.

## Risk classification
| Technique | Typical risk | Notes |
|---|---|---|
| Domain / RULE-SET reject | Low to moderate | False positives can break app network requests; no TLS decryption required. |
| URL rewrite | Moderate to high | Can alter application behavior; review matches and precedence. |
| HTTPS MITM / response scripts | High | May expose account tokens and other sensitive response data. |
| RevenueCat / subscription response modification | High | Alters entitlement information; may violate terms and fail server validation. |
| Large all-in-one bundles | High | Broad hostname scope, dependencies and conflicts make auditing harder. |

## Sources reviewed
- https://github.com/blackmatrix7/ios_rule_script
- https://github.com/bigdargon/hostsVN
- https://github.com/Johnshall/Shadowrocket-ADBlock-Rules-Forever
- https://github.com/ithtelab/sr-adblock
- https://github.com/Gaucuto/Gauapple
- https://github.com/app2smile/rules

## Gaucuto/Gauapple 10in1_Vip_ProMax
The original file refers to external JavaScript from duyvinh09/Module_IOS, app2smile/rules and Sub-Store. On 2026-11-21 the duyvinh09/Module_IOS repository and selected scripts returned 404 via GitHub API; this may be deletion, rename, privacy or access limitations. The app2smile Spotify scripts could be retrieved. Sub-Store release assets were listed, but direct download was not exhaustively verified. The configuration also included broad [MITM] hostname patterns and subscription-related header/rewrite rules.

This repository deliberately excludes these scripts. Do not import the original 10in1 wholesale into a personal phone, and do not enable unfamiliar MITM CAs. The upstream AdvertisingLite list can change; pin a reviewed revision if reproducibility is needed.

## Compatibility
- Safari: domain filtering blocks some ad hosts; a Safari content blocker is better for cosmetic HTML hiding.
- YouTube / YouTube Music: network-domain blocking alone cannot guarantee ad removal.
- TikTok: inline/sponsored feed content often uses first-party infrastructure.
- Games: rewarded ads may stop yielding rewards; whitelist a false-positive domain instead of disabling all app security.
- Premium labels do not constitute proof of legitimate subscriptions or working capabilities.

## Review checklist
1. Read every [Script], [MITM], [Header Rewrite], [URL Rewrite] section before installing.
2. Verify each script-path and avoid unreviewed moving branches.
3. Confirm MITM hostname scope, avoid financial or login endpoints.
4. Test one module at a time and inspect Shadowrocket REJECT logs.
5. Restore the previous config on network failure.
