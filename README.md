# Shadowrocket Safe Kit 🇻🇳

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

