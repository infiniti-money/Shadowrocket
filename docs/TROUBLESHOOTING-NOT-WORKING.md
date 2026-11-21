# Vì sao module GitHub không hoạt động giống module nguồn?

Ngày kiểm tra: 21/11/2026. Dành cho người dùng đã nhập module vào Shadowrocket nhưng tính năng mong đợi không hoạt động.

## Phân biệt hai URL

### 1. Module chính (không bao gồm Premium)
```
https://raw.githubusercontent.com/infiniti-money/Shadowrocket/main/modules/Infiniti-All-In-One.sgmodule
```
Đây là bộ lọc **Advertising + Privacy**. Nó không có `[Script]`, `[MITM]` hay `[Url Rewrite]`. Vì thế nó **không thể** hoạt động giống Gaucuto/duyvinh09 đối với Spotify, Locket, YouTube PiP hoặc bất kỳ chức năng Premium nào.

### 2. Module tổng hợp thử nghiệm (chưa được xác nhận hoạt động)
```
https://raw.githubusercontent.com/infiniti-money/Shadowrocket/main/modules/opt-in/All-Apps-Experimental.sgmodule
```
Có 4 script bên ngoài và các mục MITM. **Ngày 21/11/2026 đã sửa lỗi ghép `hostname = %APPEND% %APPEND% ...`** thành chỉ một `%APPEND%` duy nhất. Tuy nhiên, sự thay đổi này mới sửa cú pháp cấu hình, không chứng minh sửa được tính năng Premium.

## Checklist chẩn đoán theo thứ tự

1. **Đúng URL chưa?** Kiểm tra tên module thực tế trong Shadowrocket; nếu là `Infiniti Shadowrocket All-in-One`, đó là module lọc domain không có Premium.
2. **Đã cập nhật file chưa?** URL RAW trỏ tới nhánh `main`, nhưng bản đã cài có thể đang dùng cache. Cập nhật hoặc xóa và nhập lại module thử nghiệm.
3. **Chỉ bật một phiên bản?** Không bật cùng lúc bản opt-in tổng hợp với các file Spotify/Locket/YouTube lẻ hay các bộ 10in1 nguồn vì có rewrite/script trùng nhau.
4. **Chế độ MITM được cho phép trong môi trường kiểm thử?** Nếu HTTPS Decryption không chạy, HTTP response scripts sẽ không nhận body TLS. Chỉ kiểm tra trên thiết bị/tài khoản được phép; không cài CA không rõ nguồn.
5. **Script có tải được không?** Mở log để tìm lỗi download, JavaScript runtime, regex `pattern`, binary body, timeout. HTTP 200 trên GitHub không chứng minh JavaScript tương thích ứng dụng hiện tại.
6. **App có đổi API?** Các pattern Spotify, Locket, YouTube bám URL cụ thể; app hoặc server thay endpoint thì script không bắt được sự kiện.
7. **Ứng dụng có kiểm tra server-side không?** Việc chỉnh giao diện hoặc body phản hồi không tạo quyền thuê bao hợp lệ và có thể không đem lại chức năng trả phí.

## Các giới hạn theo ứng dụng

| Ứng dụng | Kết quả được kỳ vọng thực tế |
|---|---|
| Spotify | Script bên ngoài có thể thay đổi một số request/response nhưng chưa được kiểm toán; không thể bảo đảm nhạc không quảng cáo hoặc quyền Premium |
| Locket | `api.revenuecat.com` là API dùng chung nhiều ứng dụng; có nguy cơ tác động ngoài Locket; chưa có bằng chứng quyền Gold hợp lệ |
| YouTube | Module hiện chỉ chứa ba quy tắc URL Rewrite, **không** chứa YouTube JavaScript của nguồn nên không thể đảm bảo PiP/phát nền hay bỏ quảng cáo video |
| Nhiều ứng dụng khác | Chưa có trong bản `All-Apps-Experimental` (khác với danh sách 10in1 nguồn) |

## Cách thu thập thông tin để tiếp tục sửa

Nếu vẫn không chạy, cung cấp **tên module đang bật, ứng dụng và tính năng không hoạt động, phiên bản app/iOS, và dòng lỗi Shadowrocket đã ẩn URL có token, Cookie và Authorization**. Không gửi chứng chỉ CA private key, dữ liệu tài khoản hay thông tin mua hàng nhạy cảm.

## Các việc đã sửa trên GitHub

- Sửa lỗi lặp `%APPEND%` trong `modules/opt-in/All-Apps-Experimental.sgmodule`.
- Thêm `scripts/check_experimental_structure.py` để CI phát hiện lỗi mục và hostname lặp.
- Giữ nguyên `Infiniti-All-In-One.sgmodule` an toàn không MITM.
