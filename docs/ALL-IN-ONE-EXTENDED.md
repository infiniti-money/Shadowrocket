# Infiniti All-in-One Extended v3.0 — Ultimate Experimental

**URL được giữ nguyên** để người dùng có thể cập nhật trong Shadowrocket:

```text
https://raw.githubusercontent.com/infiniti-money/Shadowrocket/main/modules/Infiniti-All-In-One-Extended.sgmodule
```

## Phạm vi tích hợp

- 5 dòng `[Rule]` (AdBlock, Privacy, hostsVN và hai YouTube UDP blocks).
- 2 dòng `[Header Rewrite]`, 8 dòng `[Url Rewrite]`, 1 dòng `[Map Local]`.
- 22 khai báo `[Script]`, 22 hostname/pattern MITM.
- Giữ 39 nguồn JS bên ngoài trong mục chú thích để tra cứu.
- Giữ các module độc lập và hai bản .conf đã **loại thông tin CA** trong repository.

**Cảnh báo:** Đây là phép gộp tĩnh, **không phải cấu hình được chứng minh hoạt động trơn tru** trên iOS. Các nguồn `duyvinh09/Module_IOS` từng trả về 404; các khai báo phụ thuộc vào URL đó có thể không tải được. GitHub Actions chỉ kiểm tra cấu trúc, không thực thi JS, không thử trên iPhone và không bảo đảm Premium.

## Giới hạn bắt buộc để an toàn

**Không đưa `ca-p12` hoặc `ca-passphrase` vào repository.** PKCS#12 bao gồm khóa riêng CA và mật khẩu, có thể cho phép giả mạo TLS. Module Shadowrocket trên GitHub cũng không thể tự tạo hoặc cấp quyền tin cậy chứng chỉ trên iPhone. Bạn phải tạo CA trên thiết bị của mình, chỉ tin cậy CA do chính bạn quản lý, trong môi trường có quyền kiểm thử.

Các quy tắc can thiệp `api.revenuecat.com` vẫn có thể ảnh hưởng nhiều ứng dụng; ưu tiên thử trên thiết bị/tài khoản phụ. Bản gộp đã bỏ một số hook RevenueCat/iTunes trùng và Apple location MITM không liên quan, nhưng còn nhiều mã nguồn bên thứ ba chưa kiểm toán.

## Cách thử

1. Sao lưu profile và tắt toàn bộ các module All-in-One, Spotify, Locket, YouTube trùng chức năng.
2. Bấm cập nhật module Extended hiện có; kiểm tra tên **Ultimate - Experimental**.
3. Nếu Shadowrocket báo lỗi tải script từ GitHub, vô hiệu hóa script nguồn bị 404; đừng tin rằng các chức năng Premium đã hoạt động.
4. Chỉ bật HTTPS Decryption sau khi tự cấu hình CA trên iPhone và hiểu rõ hostname được giải mã.
5. Nếu login, ứng dụng ngân hàng hoặc các trang web lỗi TLS, tắt module/MITM và quay lại bản [All-in-One không MITM](../modules/Infiniti-All-In-One.sgmodule).

## Kiểm tra repository

```bash
python3 scripts/validate_extended.py
python3 scripts/check_script_sources.py --online
```

Lượt CI này chỉ là kiểm tra cấu hình; nó không thể bảo đảm an toàn hoặc tính tương thích của 22 script. Xem [báo cáo hai tệp người dùng](USER-CONFIG-MERGE.md) và [danh mục nguồn](../research/all-script-inventory.json).
