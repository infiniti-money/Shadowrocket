# Shadowrocket Safe Kit 🇻🇳

## HTTPS Experimental — bản có Script và Giải mã HTTPS (bật riêng)

Nếu Shadowrocket hiển thị **Giải mã HTTPS: 0 / Kịch bản: 0** cho bản Extended Safe thì đó là đúng thiết kế (39 URL script chỉ là chú thích). Đã tạo bản thay thế **[Infiniti-Extended-HTTPS-Experimental.sgmodule](modules/opt-in/Infiniti-Extended-HTTPS-Experimental.sgmodule)** có **3 RULE-SET, 4 khai báo script, 1 mục MITM gồm 5 hostname/pattern**, cùng các mục rewrite YouTube/Spotify.

**RAW:** `https://raw.githubusercontent.com/infiniti-money/Shadowrocket/main/modules/opt-in/Infiniti-Extended-HTTPS-Experimental.sgmodule`

Bản mới **không tự bật trên iPhone**, không nhập cùng bản Extended Safe, không bảo đảm mở khóa Premium và có rủi ro giải mã HTTPS qua API RevenueCat dùng chung. [Hướng dẫn nhập, kiểm tra số lượng và quay về bản an toàn](docs/HTTPS-EXPERIMENTAL-SETUP.md).


## All-in-One Extended v2.0 — tích hợp sâu 39 nguồn JS

**[Infiniti-All-In-One-Extended.sgmodule](modules/Infiniti-All-In-One-Extended.sgmodule)** là bản cài đặt hợp nhất **Advertising + Privacy + hostsVN threat protection**, kèm danh mục **39 script URL** theo từng nhóm ứng dụng (YouTube, Spotify, Locket/RevenueCat, Sub-Store, ứng dụng khác).

**RAW:** `https://raw.githubusercontent.com/infiniti-money/Shadowrocket/main/modules/Infiniti-All-In-One-Extended.sgmodule`

**Phân biệt rõ:** 39 URL script được liệt kê dưới dạng comment để tra cứu, **không chạy**; bản Extended không có MITM. Nếu muốn thử các script trước đây đã thêm, chúng vẫn ở `modules/opt-in/` riêng, chưa kiểm toán/không bảo đảm Premium hoạt động. **Chỉ bật một trong hai bản All-in-One thông thường và Extended** để tránh chồng bộ lọc.

Đã thêm [bộ kiểm tra toàn bộ 39 URL](scripts/validate_extended.py) và [hướng dẫn](docs/ALL-IN-ONE-EXTENDED.md). Đừng coi việc liệt kê đủ source là đã kích hoạt mọi tính năng Premium.


## 🚀 Nâng cấp v1.1 — giám sát nguồn tự động

- [Hướng dẫn nâng cấp](docs/UPGRADE-1.1.md): quy trình cài đặt, kiểm tra và khắc phục lỗi.
- [Danh mục upstream](rules/upstreams.json): quản lý nguồn rule chính thức, tránh URL ngoài dự kiến.
- [Trình kiểm tra upstream](scripts/check_upstreams.py): kiểm tra trạng thái tải, UTF-8 và cú pháp các dòng quy tắc.
- [GitHub Actions](.github/workflows/validate.yml): kiểm tra khi push/PR và mỗi ngày lúc 09:17 giờ Việt Nam.
- **URL cài đặt All-in-One không thay đổi.** Các module Premium còn ở chế độ nghiên cứu, không có quyền MITM trong module chính.


## 🌟 Bản đầy đủ chính chủ — Infiniti All-in-One

**Khuyên dùng nếu muốn một file tổng hợp**: [Infiniti-All-In-One.sgmodule](modules/Infiniti-All-In-One.sgmodule)

RAW:
`https://raw.githubusercontent.com/infiniti-money/Shadowrocket/main/modules/Infiniti-All-In-One.sgmodule`

Gồm **Advertising (full) + Privacy**, kiểm tra nguồn bằng GitHub Actions, không yêu cầu MITM. Áp dụng lọc tên miền cho Safari, game, TikTok và ứng dụng khác, có giới hạn đối với quảng cáo video YouTube / YouTube Music. **Không chứa Premium Unlock hoặc sửa trạng thái thuê bao.**

[Hướng dẫn sử dụng và giới hạn](docs/ALL-IN-ONE.md). **Chỉ bật một trong** Infiniti All-in-One, AdBlock Lite hoặc các bản reviewed, tránh quy tắc trùng. Các bản Premium 10in1 gốc vẫn được lưu ở `modules/experimental/` nhưng chưa kiểm toán và không tự bật.


[![Validate Shadowrocket modules](https://github.com/infiniti-money/Shadowrocket/actions/workflows/validate.yml/badge.svg)](https://github.com/infiniti-money/Shadowrocket/actions/workflows/validate.yml)

Bộ cấu hình Shadowrocket do **infiniti-money** quản lý, ưu tiên **chặn quảng cáo theo domain mà không cần HTTPS MITM**. Bộ mã này có tài liệu về YouTube, YouTube Music, TikTok, Safari, game iOS và đánh giá rủi ro của các module Premium.

> Đây là dự án độc lập. Không phải bản sao, bản fork hay bản mở khóa Premium của `Gaucuto/Gauapple/10in1_Vip_ProMax`.

## Cài đặt trên iOS

1. Sao lưu cấu hình Shadowrocket hiện tại.
2. Sao chép URL module: https://raw.githubusercontent.com/infiniti-money/Shadowrocket/main/modules/AdBlock-Lite.sgmodule
3. Nhập URL vào phần **Modules** nếu phiên bản Shadowrocket hỗ trợ module này; bật duy nhất một bản AdBlock Lite.
4. Không bật HTTPS Decryption/MITM cho bộ lọc domain.
5. Thử các ứng dụng và xem log REJECT nếu có sự cố mạng.

Nếu bản Shadowrocket không nhận `.sgmodule`, thử [AdBlock-Lite.module](modules/AdBlock-Lite.module) hoặc sao chép dòng RULE-SET trong [rules/AdvertisingLite-rule.txt](rules/AdvertisingLite-rule.txt) vào mục `[Rule]` của cấu hình đang dùng, trước quy tắc `FINAL`. **Đừng thay thế toàn bộ cấu hình proxy bằng module rời này.**

## Phạm vi và giới hạn

| Ứng dụng | Khả năng dự kiến | Giới hạn |
|---|---|---|
| Safari, website | Chặn một phần domain quảng cáo và tracker | Cần Safari content blocker riêng để ẩn phần tử HTML |
| Game iOS | Chặn một số SDK quảng cáo | Quảng cáo nhận thưởng có thể không hoạt động |
| TikTok | Lọc một phần request quảng cáo | Quảng cáo trong luồng nội dung có thể vẫn xuất hiện |
| YouTube / YouTube Music | Lọc những yêu cầu khớp bộ danh sách | Không bảo đảm bỏ quảng cáo của ứng dụng |
| Ứng dụng khác | Lọc domain có trong AdvertisingLite | Có nguy cơ chặn nhầm; cần xem log |

## Cấu trúc

- [modules/AdBlock-Lite.sgmodule](modules/AdBlock-Lite.sgmodule): Module Shadowrocket không MITM.
- [modules/AdBlock-Lite.module](modules/AdBlock-Lite.module): Biến thể đuôi file.
- [rules/AdvertisingLite-rule.txt](rules/AdvertisingLite-rule.txt): Quy tắc để nhập vào cấu hình hiện có.
- [research/RISK-AUDIT.md](research/RISK-AUDIT.md): Phân loại rủi ro MITM, JavaScript, Premium.
- [scripts/validate.py](scripts/validate.py): Kiểm tra tĩnh các module.
- [.github/workflows/validate.yml](.github/workflows/validate.yml): CI kiểm tra nội dung module và URL nguồn.

## Nguồn tham khảo và ghi nhận

- [blackmatrix7/ios_rule_script](https://github.com/blackmatrix7/ios_rule_script) — AdvertisingLite, nguồn rule đang dùng.
- [bigdargon/hostsVN](https://github.com/bigdargon/hostsVN) — quy tắc quảng cáo Việt Nam.
- [Johnshall/Shadowrocket-ADBlock-Rules-Forever](https://github.com/Johnshall/Shadowrocket-ADBlock-Rules-Forever) — cấu hình tổng hợp.
- [ithtelab/sr-adblock](https://github.com/ithtelab/sr-adblock) — lọc quảng cáo nhiều nguồn.
- [Gaucuto/Gauapple](https://github.com/Gaucuto/Gauapple) — nguồn nghiên cứu 10in1, **không** nhập script.
- [app2smile/rules](https://github.com/app2smile/rules) — tham khảo cơ chế rewrite, **không** nhập script.

Các danh sách upstream tuân theo giấy phép của tác giả tương ứng. Giấy phép MIT trong repository chỉ áp dụng cho mã và tài liệu do dự án này tự tạo.

## Bảo mật và kiểm tra

Chạy `python3 scripts/validate.py` để kiểm tra rằng hai module chính chỉ chứa RULE-SET hợp lệ theo kỳ vọng và không chứa `[MITM]`, `[Script]` hay Rewrite. GitHub Actions chạy kiểm tra khi push / pull request và kiểm tra khả năng truy cập URL quy tắc upstream.

Bộ kiểm tra tĩnh **không chứng nhận module tương thích mọi phiên bản Shadowrocket**, không kiểm thử iPhone và không bảo đảm hiệu quả chặn quảng cáo. Upstream có thể thay đổi theo thời gian.

## License

[MIT](LICENSE) cho mã và tài liệu gốc của repository.

## Module thử nghiệm bên thứ ba — không bật mặc định

Đã lưu bản tham khảo của Gaucuto tại [modules/experimental/10in1_Vip_ProMax.sgmodule](modules/experimental/10in1_Vip_ProMax.sgmodule) với dòng `#!url` ghi rõ [nguồn gốc](https://raw.githubusercontent.com/Gaucuto/Gauapple/refs/heads/main/10in1_Vip_ProMax). Nội dung upstream được giữ nguyên bên dưới các dòng cảnh báo.

**Quan trọng:** File này có MITM, Header Rewrite, JavaScript chỉnh sửa trạng thái thuê bao từ những nguồn bên ngoài và một số URL từng trả về 404. Đưa file vào GitHub không đồng nghĩa đã kiểm toán hoặc xác nhận tương thích. **Không được tự động nhập vào AdBlock Lite, không khuyến nghị bật trên iPhone chính.** Công cụ kiểm tra an toàn tại `scripts/validate.py` chỉ xác minh các module Lite, **không** phê duyệt module experimental.


### Lưu trữ bản All In One của duyvinh09

- [All_In_One_duyvinh09.sgmodule](modules/experimental/All_In_One_duyvinh09.sgmodule) — bản **người dùng cung cấp**, lưu nguyên cấu hình để kiểm tra và nghiên cứu, không thuộc AdBlock Lite.
- [Nguồn tác giả đã ghi trong file](https://raw.githubusercontent.com/duyvinh09/Module_IOS/refs/heads/main/All_In_One.sgmodule) — trả về **HTTP 404** khi kiểm tra ngày 21/11/2026; không xác minh được nội dung gốc trực tuyến.
- Cấu hình chứa 25 dòng tham chiếu `script-path`, MITM phạm vi rộng, can thiệp thông tin thuê bao và những dấu hiệu cú pháp cần kiểm tra như `engine={{{script}}}`, dòng VSCO thiếu dấu phân cách và dấu phẩy rỗng trong danh sách hostname. Không nhập vào iPhone chính.
- GitHub Actions hiện chỉ xác minh các module AdBlock Lite, **không** kiểm thử bản All In One này.


## Bản sửa sau khi nghiên cứu (21/11/2026)

**Không sử dụng các file trong `experimental/` trực tiếp trên iPhone chính.** Đã có hai phiên bản kiểm tra an toàn, tách biệt:

- [Gaucuto_10in1_Safe.sgmodule](modules/reviewed/Gaucuto_10in1_Safe.sgmodule): phiên bản lọc quảng cáo domain, bỏ MITM, sửa phản hồi thuê bao và script JavaScript không xác minh.
- [DuyVinh_All_In_One_Safe.sgmodule](modules/reviewed/DuyVinh_All_In_One_Safe.sgmodule): phiên bản lọc quảng cáo domain, không phụ thuộc các script 404 hoặc bản khai báo cú pháp bất thường.
- [MODULE-REPAIR-REPORT.md](research/MODULE-REPAIR-REPORT.md): bảng lỗi, giải thích những phần vô hiệu hóa và cách kiểm tra.

**Lưu ý:** Hai bản reviewed cố ý chỉ chặn domain theo AdvertisingLite, nên không khôi phục tính năng Pro/Premium, không bảo đảm bỏ quảng cáo trong ứng dụng YouTube. Hai file reviewed là hai biến thể độc lập; **chỉ bật một**, không cần bật cùng lúc hoặc chồng với AdBlock Lite.

**Tự kiểm tra:** `python3 scripts/validate.py` và [GitHub Actions](https://github.com/infiniti-money/Shadowrocket/actions). Bộ kiểm tra không chứng nhận tương thích thực tế trên iPhone.

## Tình trạng khôi phục tính năng Premium

Xem [PREMIUM-RECOVERY-STATUS.md](research/PREMIUM-RECOVERY-STATUS.md) để biết những nguồn còn truy cập được, chức năng nào cần kiểm thử, và giới hạn xác minh quyền thuê bao. **Chưa có module mở khóa Premium nào được khôi phục hoặc kích hoạt.** Các module AdBlock Lite và Reviewed Safe vẫn không MITM.

## Nguồn GitHub mới được tích hợp (21/11/2026)

Các nguồn đã được rà soát và phân loại trong [UPSTREAM-SOURCE-MATRIX.md](research/UPSTREAM-SOURCE-MATRIX.md). Tôi không gộp các bộ lọc chồng chéo hoặc script Premium vào module mặc định.

**Module tùy chọn:**
- [Vietnam-Threat-Protection.sgmodule](modules/optional/Vietnam-Threat-Protection.sgmodule): tên miền nguy cơ từ `bigdargon/hostsVN`, không cần MITM. Có thể thử cùng bản All-in-One, nhưng có nguy cơ chặn nhầm.
- [Privacy-Only.sgmodule](modules/optional/Privacy-Only.sgmodule): Privacy của `blackmatrix7` cho người chỉ cần quy tắc riêng. **Không bật chung với All-in-One**, vì đã bao gồm danh sách này.

Các nguồn `ithtelab`, `GMOogway`, `poohyeban`, `hongkongkiwi` được nghiên cứu về kiến trúc, tính tương thích và chuyển đổi quy tắc, chưa đưa thành quy tắc bật mặc định. Không ghép trực tiếp định dạng `hosts` vào `RULE-SET`. Bộ kiểm tra tĩnh cũng không tương đương với thử nghiệm trên iPhone.

## 📚 Bộ sưu tập script Premium iOS (nghiên cứu)

Đã nghiên cứu và xác minh 7 URL RAW module liên quan Spotify, Locket và YouTube. Xem [PREMIUM-SCRIPT-CATALOG.md](research/PREMIUM-SCRIPT-CATALOG.md) và [premium-sources.json](research/premium-sources.json) để kiểm tra danh mục, nguồn tác giả, rủi ro MITM và những điểm cần kiểm toán. Những URL này có thể thay đổi theo thời gian.

**Không tự kích hoạt bất kỳ script nào từ danh mục**: nhiều module can thiệp quyền thuê bao qua RevenueCat hoặc yêu cầu HTTPS MITM. Dự án chính Infiniti All-in-One tiếp tục chỉ chứa các quy tắc chặn quảng cáo và quyền riêng tư không cần giải mã HTTPS. Không tuyên bố rằng script Premium đã được khôi phục hoặc đang hoạt động.

## ⚠️ Module thử nghiệm bật riêng (opt-in)

Các bản thử nghiệm mới có file riêng trong [modules/opt-in](modules/opt-in), gồm **Spotify** (2 script từ app2smile), **Locket** (2 script liên quan RevenueCat từ HuuTriet) và **YouTube** (URL Rewrite giới hạn, không nhúng script Premium chưa kiểm toán). Xem [hướng dẫn, rủi ro và cách thử](docs/OPT-IN-MODULES.md).

**Mặc định KHÔNG bật** trong Infiniti All-in-One, vì cần HTTPS MITM, có thể xung đột với ứng dụng hoặc can thiệp xác thực thuê bao. Chỉ lưu file trên GitHub không kích hoạt module trên iPhone. Các chức năng trả phí không được xác nhận là đã khôi phục hoặc có thuê bao hợp lệ. GitHub Actions mặc định chỉ chứng nhận bộ lọc domain an toàn, **không kiểm toán script opt-in**.

## Bản tổng hợp ứng dụng (bật riêng, rủi ro cao)

Đã tạo [All-Apps-Experimental.sgmodule](modules/opt-in/All-Apps-Experimental.sgmodule) để gom các quy tắc **Spotify, Locket và YouTube**, cộng với Advertising + Privacy. File này có MITM và JavaScript can thiệp phản hồi thuê bao; **không bật mặc định**, không xác nhận gói Premium hợp lệ và chưa kiểm thử trên iPhone.

Không bật đồng thời bản tổng hợp với các module lẻ hay các gói 10in1 cũ. [Đọc hướng dẫn và cách quay lại cấu hình cũ](docs/ALL-APPS-EXPERIMENTAL.md). GitHub CI mặc định **không chứng nhận** an toàn của các script này. Bản chính `Infiniti-All-In-One.sgmodule` vẫn không MITM.

## 🔍 Nghiên cứu giải mã HTTPS trên iOS

Đã bổ sung [bảng nghiên cứu mitmproxy, HTTP Toolkit, Proxyman và tài liệu Shadowrocket](research/IOS-HTTPS-INSPECTION.md). Các phần mới gồm [mẫu HTTPS debug chỉ dành cho ứng dụng của chính bạn](modules/templates/HTTPS-Debug-Own-App.sgmodule.example) (tất cả dòng MITM đều bị comment, **không hoạt động**) và [trình kiểm toán tĩnh scope MITM](scripts/audit_mitm.py), được chạy trong GitHub Actions.

**Không tự động bật giải mã HTTPS:** Các module Premium/opt-in hiện có vẫn ở trạng thái thử nghiệm, không được tự động nhập vào bản All-in-One an toàn. Chỉ dùng chứng chỉ CA và MITM với app/domain bạn có quyền kiểm tra; không giải mã lưu lượng tài khoản nhạy cảm hoặc chia sẻ khóa CA trong repository.

## 📦 Toàn bộ nguồn script iOS để tự xác minh

Đã lập [danh mục 39 script-path URL](research/all-script-inventory.json) từ hai bản 10in1 và các module cộng đồng Spotify, Locket, YouTube, SoundCloud, Truecaller cùng nhiều ứng dụng khác. Xem [hướng dẫn xác minh](docs/SCRIPT-VERIFICATION-WORKSPACE.md). Chạy `python3 scripts/check_script_sources.py --online` để kiểm tra liên kết, **không thực thi JavaScript**.

Danh mục chứa liên kết nguồn và tên script, **không sao chép toàn bộ mã JS của tác giả bên ngoài hoặc tự kích hoạt tất cả**. Một số URL duyvinh09 trước đây trả về 404. Bản All-in-One chính vẫn không MITM; các bản Premium có sẵn trong `modules/opt-in/` và `modules/experimental/` chỉ dùng cho nghiên cứu có kiểm soát.
