# Infiniti All-in-One Ultimate v3.2 — bản tổng hợp duy nhất

**URL cập nhật bản Extended hiện có:**

```text
https://raw.githubusercontent.com/infiniti-money/Shadowrocket/main/modules/Infiniti-All-In-One-Extended.sgmodule
```

Đây là một **module Shadowrocket**, không phải một profile VPN có máy chủ proxy được cấu hình sẵn. Không cần nhập URL mới nếu bạn đang dùng Extended: cập nhật lại module đã đăng ký.

## Tất cả phần đã tích hợp

| Mục trong file | Thành phần |
|---|---|
| `[Rule]` | 5 quy tắc: AdBlock, Privacy, hostsVN threat và 2 chặn YouTube UDP |
| `[Header Rewrite]` | 2 khai báo |
| `[Url Rewrite]` | 5 khai báo |
| `[Map Local]` | 1 khai báo |
| `[Script]` | 7 khai báo đang bật |
| `[MITM]` | Một dòng cấu hình 21 hostname/pattern giải mã HTTPS |
| Danh mục JS | **39 URL riêng biệt**: 7 đang bật, 32 chỉ ghi chú |

Dự án vẫn lưu các nguồn Gaucuto/duyvinh09 và các module từng ứng dụng; **chỉ bật một bản tổng hợp trên iPhone để tránh ghi đè và xung đột**.

## Vì sao không bật đủ 39 script?

- 20 URL trong danh mục từng được báo lỗi HTTP 404, nên được giữ để tự kiểm tra nhưng **không được chạy mặc định**.
- Các script từ nguồn khác có thể xử lý cùng endpoint và ghi đè lẫn nhau.
- Một số script sửa phản hồi cấp quyền thuê bao hoặc API RevenueCat dùng chung, có thể làm ảnh hưởng ứng dụng khác.
- Đủ `[MITM]` và `[Script]` chỉ cho biết cấu hình khai báo các chức năng. Nó không xác nhận script được tải, TLS giải mã thành công, hoặc có quyền Premium hợp lệ.

Không đưa `ca-p12` hoặc `ca-passphrase` từ hai file người dùng tải lên vào GitHub. Đó là vật liệu khóa riêng và mật khẩu của CA. Nếu cần kiểm thử HTTPS Decryption, thiết lập chứng chỉ do bạn quản lý cục bộ trên iPhone; không chia sẻ chứng chỉ có khóa riêng.

## Kiểm tra sau cập nhật

1. Sao lưu cấu hình và tắt các module All-in-One, Spotify, Locket và YouTube khác.
2. Cập nhật module từ URL cũ; xác nhận thấy **Ultimate v3.2**.
3. Kiểm tra chi tiết Shadowrocket: `[Rule]`, Rewrite, Map Local, Script và HTTPS Decryption.
4. Phần giải mã chỉ hoạt động sau khi bạn cấu hình tin cậy CA trên thiết bị và ứng dụng cho phép; một số ứng dụng có certificate pinning.
5. Nếu proxy, đăng nhập, ứng dụng ngân hàng, video hoặc mạng gặp lỗi, tắt module thử nghiệm và quay về bản [không MITM](../modules/Infiniti-All-In-One.sgmodule).

## Kiểm tra trên GitHub

```bash
python3 scripts/validate_extended.py
python3 scripts/check_script_sources.py --online
```

CI xác minh cấu trúc, không có khóa riêng CA và URL được lập danh mục không trùng. CI **không chứng nhận cấu hình chạy trơn tru trên iPhone**.

**Lưu ý về các nguồn lỗi:** Khi bạn muốn thử một JS từng 404, kiểm tra lại URL đó còn tải được và code hợp lệ trước khi tự bỏ dấu `#`. Chỉ bật một handler cho mỗi endpoint nếu không chắc về thứ tự chạy.
