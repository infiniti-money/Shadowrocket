# Infiniti All-in-One Recovery v3.4 — cấu hình khôi phục

**URL không đổi:**

```text
https://raw.githubusercontent.com/infiniti-money/Shadowrocket/main/modules/Infiniti-All-In-One-Extended.sgmodule
```

## Lý do sửa

Bản Ultimate v3.3 khai báo bật 39 URL script một lúc. Danh mục repository ghi nhận 20 URL từng lỗi HTTP 404; thử lại một URL SoundCloud duyvinh09 cũng trả 404. Những bộ Spotify/YouTube/Locket có thể dùng cùng endpoint, gây tranh chấp. CI kiểm tra cú pháp tĩnh đã từng thành công, nhưng không chứng minh iOS chạy được.

Theo phản hồi **"Không hoạt động"**, bản Extended cùng URL được khôi phục để giảm lỗi tải script, thay vì tiếp tục kích hoạt mọi đường dẫn.

## Bản v3.4 gồm những gì?

| Mục | Số lượng |
|---|---:|
| `[Rule]` | 3 (Advertising, Privacy, hostsVN threat) |
| `[Header Rewrite]` | 1 (Spotify) |
| `[Url Rewrite]` | 3 (YouTube) |
| `[Script]` | 2 (Spotify từ app2smile) |
| `[MITM]` | 4 hostname/pattern liên quan Spotify và YouTube |
| Thư viện tham khảo | 37 URL còn lại, chú thích, không thực thi |

**Tổng cộng vẫn lưu đủ 39 đường dẫn JS, không trùng nhau.** File `research/all-script-inventory.json` và `modules/opt-in/Full-Source-Merge-Experimental.sgmodule` vẫn giữ thông tin và quy tắc nguồn để nghiên cứu, không cần bật khi dùng v3.4.

Đã bỏ can thiệp vào RevenueCat và Apple iTunes trong bản đang bật, bởi chúng có thể ảnh hưởng mua hàng/đăng nhập của ứng dụng khác. Bản này **không hứa mở khóa Premium, không bảo đảm chặn tất cả quảng cáo YouTube/TikTok**.

## Cập nhật Shadowrocket

1. Sao lưu cấu hình Shadowrocket hiện tại.
2. Tắt những module 10in1, Spotify, Locket, YouTube và All-in-One khác có quy tắc chồng nhau.
3. Cập nhật lại URL Extended cũ; xác nhận tên **Infiniti All-in-One Recovery v3.4**.
4. Kiểm tra thấy quy tắc, script và HTTPS Decryption trong chi tiết module. Khai báo HTTPS không tự cài hoặc tin cậy CA trên iOS; chỉ dùng CA do bạn quản lý trong môi trường được phép.
5. Nếu vẫn lỗi, tắt HTTPS Decryption và module đang thử, sử dụng bản `modules/Infiniti-All-In-One.sgmodule` **không MITM**, rồi kiểm tra log để khoanh vùng.

Nếu mục tiêu là chặn quảng cáo ổn định thay vì thử script, lựa chọn hợp lý nhất vẫn là module không MITM.

## Xác minh repository

```bash
python3 scripts/validate_extended.py
python3 scripts/check_script_sources.py --online
```

CI chỉ xác minh các mục và danh mục URL. Nó không xác minh tải script, hợp lệ TLS trên thiết bị hay Premium.
