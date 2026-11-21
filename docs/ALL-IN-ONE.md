# Infiniti Shadowrocket All-in-One — v1.0

**Module chính:** [Infiniti-All-In-One.sgmodule](../modules/Infiniti-All-In-One.sgmodule)

RAW URL:
```text
https://raw.githubusercontent.com/infiniti-money/Shadowrocket/main/modules/Infiniti-All-In-One.sgmodule
```

## Tính năng đã tích hợp
- **Advertising:** danh sách chặn quảng cáo blackmatrix7 (bản đầy đủ, không phải Lite).
- **Privacy:** danh sách hạn chế các domain theo dõi do blackmatrix7 phát hành.
- **Safari / Website / Game / TikTok / App khác:** lọc yêu cầu mạng khi trùng khớp tên miền trong hai danh sách trên.
- **YouTube / YouTube Music:** chặn một số domain, **không bảo đảm** loại bỏ quảng cáo trong video.
- **Không có** các script Premium Unlock, giả mạo mua hàng, API RevenueCat, `verifyReceipt`, MITM, VPN proxy server hoặc script tự chạy theo lịch.

Nguồn trực tiếp được kiểm tra có thể truy cập ngày 21/11/2026:
- https://github.com/blackmatrix7/ios_rule_script/tree/master/rule/Shadowrocket/Advertising
- https://github.com/blackmatrix7/ios_rule_script/tree/master/rule/Shadowrocket/Privacy

## Cài đặt
1. Sao lưu cấu hình đang dùng trong Shadowrocket.
2. Nhập URL RAW của module vào phần Modules (nếu phiên bản Shadowrocket của bạn hỗ trợ).
3. **Tắt các module AdBlock Lite / Gaucuto Safe / DuyVinh Safe** trước khi bật All-in-One để tránh chồng chéo.
4. Không cần cài CA, bật MITM hay HTTPS Decryption.
5. Thử từng ứng dụng. Nếu có lỗi đăng nhập, xem log REJECT và loại trừ các domain bị chặn nhầm, hoặc tắt module.
6. Nếu Shadowrocket không nhận module rời, có thể thêm hai dòng `RULE-SET` của file vào phần `[Rule]` của cấu hình đang dùng, phía trước quy tắc `FINAL`.

## Vì sao không nhúng hostsVN trực tiếp?
`bigdargon/hostsVN` phát hành file hosts `0.0.0.0 domain`, khác với kiểu dòng `DOMAIN/DOMAIN-SUFFIX` của `RULE-SET` Shadowrocket. Không đưa URL hosts vào RULE-SET khi chưa chuyển đổi. Để có bộ lọc Việt Nam nên kiểm tra nguồn rule chuyển đổi, giấy phép và tính tương thích riêng.

## Giới hạn và bảo mật
- `Advertising` và `Privacy` được dùng qua nhánh `master`; nội dung có thể thay đổi, cần kiểm tra lại nếu phát sinh lỗi.
- Cả hai nguồn có thể có mục trùng nhau; engine quyết định cách xử lý. Bản này không tự tuyên bố hiệu quả cao hơn dựa trên số quy tắc.
- Không có bằng chứng tương thích iOS thực tế cho mọi ứng dụng. GitHub Actions chỉ kiểm tra file, cấu trúc và khả năng truy cập URL.
- Các bản 10in1 của Gaucuto, duyvinh09 được lưu nguyên trong `modules/experimental/` để nghiên cứu, không nhập vào bản chính.
- Nếu người dùng có thuê bao hợp lệ nhưng chưa mở khóa, dùng Restore Purchases của ứng dụng.

## Cấu trúc dự án
- `modules/Infiniti-All-In-One.sgmodule`: file chính.
- `modules/AdBlock-Lite.sgmodule`: bản nhẹ, ít chặn nhầm hơn.
- `modules/reviewed/`: bản quy tắc an toàn gắn với nguồn nghiên cứu.
- `modules/experimental/`: bản gốc chưa kiểm toán; tránh bật trên điện thoại chính.
- `research/`: báo cáo về script và rủi ro Premium.
