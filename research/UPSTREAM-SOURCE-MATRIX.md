# Shadowrocket upstream review — 2026-11-21

The purpose of this matrix is to distinguish *verified format and availability* from *safety*, *efficacy* and *iOS compatibility*. Access to a source is not a full security audit.

| Project | What we checked | Decision |
|---|---|---|
| [blackmatrix7/ios_rule_script](https://github.com/blackmatrix7/ios_rule_script) | `Advertising.list`, `AdvertisingLite.list`, `Privacy.list` accessible and in Shadowrocket list syntax | Used as main and lite rule sources |
| [bigdargon/hostsVN](https://github.com/bigdargon/hostsVN) | `extensions/threat/surge-rule.conf` accessible; observed ~4,900 lines; all noncomment lines started with `DOMAIN` or `DOMAIN-SUFFIX`/similar; `option/domain.txt` is plain hostname format | Added **opt-in threat-only module**; did not copy raw hosts/domain.txt into RULE-SET |
| [ithtelab/sr-adblock](https://github.com/ithtelab/sr-adblock) | Repository describes multi-source filtering, deduplication and modules; selected raw lists too large for current fetch | Reference only; not combined with existing Advertising to avoid overlap |
| [GMOogway/shadowrocket-rules](https://github.com/GMOogway/shadowrocket-rules) | Repo documents routing-specific modules and automatic rules | Architecture reference only; no user-defined proxy policy available |
| [poohyeban/shadowrocket-rules](https://github.com/poohyeban/shadowrocket-rules) | Conversion/normalization methodology documented | Syntax-validation design reference |
| [hongkongkiwi/shadowrocket-vpn-configs](https://github.com/hongkongkiwi/shadowrocket-vpn-configs) | Documentation includes separation of module boundaries and source pins | Architecture reference |
| [Gaucuto/Gauapple](https://github.com/Gaucuto/Gauapple) | Upstream 10in1 read; references JavaScript and broad MITM | Preserved only in `experimental/`, not auto-enabled |
| [duyvinh09/Module_IOS](https://github.com/duyvinh09/Module_IOS) | User-provided module; repository and multiple script paths returned GitHub 404 | Preserved for audit only; do not load missing scripts |

## Current architecture

- **One recommended main module:** `modules/Infiniti-All-In-One.sgmodule` — Advertising + Privacy, no scripts.
- **One Lite alternative:** `modules/AdBlock-Lite.sgmodule`.
- **Optional:** `modules/optional/Vietnam-Threat-Protection.sgmodule` — extra threat domains; can be tested alongside main.
- **Privacy-only alternative:** `modules/optional/Privacy-Only.sgmodule` — do *not* enable alongside main, which already includes Privacy.
- **Experimental archives:** Historical scripts, potentially unsafe; excluded from CI allowlist approval.

## Important limits

- Do not treat threat lists as a comprehensive security product; false positives and false negatives happen.
- No iPhone/Shadowrocket parser integration test completed.
- Safari cosmetic ads are better handled by a Safari content blocker.
- TikTok and YouTube video advertisements commonly cannot be removed reliably by domain blocking.
- Premium entitlement bypass is not part of this project. Legitimate subscription restoration belongs to official app mechanisms.
- Respect upstream licenses; this repository links external sources rather than redistributing whole lists.
