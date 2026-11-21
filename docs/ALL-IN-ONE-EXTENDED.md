# Infiniti All-in-One Extended v2.1 — HTTPS Experimental

**Thông báo thay đổi 21/11/2026:** URL Extended cũ đã được người dùng yêu cầu nâng cấp tại chỗ. Kể từ v2.1, module này **KHÔNG CÒN LÀ BẢN SAFE**: có JavaScript bên thứ ba và các quy tắc MITM/Rewrite đang hoạt động.

## URL cũ, nội dung đã cập nhật

```text
https://raw.githubusercontent.com/infiniti-money/Shadowrocket/main/modules/Infiniti-All-In-One-Extended.sgmodule
```

Trong Shadowrocket, dùng tính năng cập nhật lại module với URL trên. Kiểm tra nội dung và bản sao lưu trước khi bật; nếu ứng dụng còn cache, có thể cần tải lại module.

### Nội dung đang bật

- 3 `RULE-SET`: Advertising (blackmatrix7), Privacy (blackmatrix7), threat domains (hostsVN).
- 1 Spotify Header Rewrite.
- 3 YouTube URL Rewrite.
- 4 script JS từ app2smile (Spotify ×2) và HuuTriet (Locket ×2).
- 1 mục `[MITM]`, khai báo 5 hostname/pattern: Spotify, YouTube và API RevenueCat dùng chung.
- 39 URL script cũ **chỉ ghi chú** để đối chiếu, không thực thi.

**Không có** 39 script chạy đồng thời, không có bảo đảm PiP/phát nền/Spotify Premium/Locket Gold và không có quyền mua gói hợp lệ.

### Rủi ro và kiểm thử

1. Sao lưu cấu hình trước khi cập nhật.
2. Tắt tất cả module Spotify/Locket/YouTube và các bộ All-in-One khác trước khi bật Extended; tránh trùng script và MITM.
3. Chỉ thử trên thiết bị và tài khoản có quyền kiểm thử, vì giải mã HTTPS có thể ảnh hưởng thông tin nhạy cảm.
4. `api.revenuecat.com` dùng chung nhiều ứng dụng, nên Locket script có thể can thiệp cả phản hồi của các ứng dụng khác.
5. Việc file có mục `[MITM]` không có nghĩa Shadowrocket đã cài và tin cậy chứng chỉ CA trên iOS.
6. Nếu lỗi mạng, đăng nhập, TLS hoặc ứng dụng, tắt module và HTTPS Decryption, rồi quay về `modules/Infiniti-All-In-One.sgmodule` (không MITM).
7. Script-path trên nhánh `main/master` có thể thay đổi; chưa được kiểm toán đầy đủ, đặc biệt các response modifier thuê bao.

## Kiểm tra

```bash
python3 scripts/validate_extended.py
python3 scripts/check_script_sources.py --online
```

Trình kiểm tra xác nhận cấu trúc và kiểm kê nguồn, **không xác nhận khả năng hoạt động trên iPhone hay mở khóa Premium**.

Nếu bạn không muốn dùng HTTPS MITM, thay bằng bản không giải mã:
`https://raw.githubusercontent.com/infiniti-money/Shadowrocket/main/modules/Infiniti-All-In-One.sgmodule`
