# Infiniti All-Apps Experimental — cách dùng và giới hạn

Đây là bản thử nghiệm **có các quy tắc Rewrite/MITM thực sự**, nhưng **không** phải một gói thuê bao hợp lệ và chưa được thử nghiệm trên iPhone.

## Gói đã ghép

- Advertising + Privacy từ blackmatrix7 (2 RULE-SET).
- Spotify: 1 Header Rewrite, 2 script JS app2smile.
- Locket: 2 script JS HuuTriet, nhắm tới `api.revenuecat.com`.
- YouTube: 3 quy tắc URL Rewrite. Không bật JS video/YouTube Premium chưa được kiểm toán.
- 5 hostname/pattern MITM: Spotify, RevenueCat, YouTube.

## Lý do phải tách bản thử nghiệm

- `api.revenuecat.com` có thể được nhiều ứng dụng dùng chung; script Locket có thể sửa thông tin phản hồi cho ứng dụng khác.
- Script tải động qua nhánh `master`/`main`, chưa được ghim vào commit và kiểm toán toàn bộ mã nguồn.
- MITM yêu cầu giải mã HTTPS. Quy tắc chỉ được thực thi trên thiết bị sau khi bạn cài, bật module và cấu hình HTTPS Decryption phù hợp.
- Quy tắc YouTube chỉ lọc vài endpoint, không xác nhận PiP/phát nền hoặc bỏ quảng cáo video.
- Không xác nhận quyền lợi Spotify/Locket Premium thật, không can thiệp mua hàng của Apple.

## Kích hoạt trên thiết bị (chỉ khi bạn chấp nhận rủi ro)

1. Sao lưu cấu hình Shadowrocket và thiết lập cách quay lại cấu hình cũ.
2. Tắt ba module lẻ Spotify, Locket, YouTube, các All-in-One Premium gốc và bất kỳ module nào sửa cùng domain.
3. Mở [file tổng hợp](../modules/opt-in/All-Apps-Experimental.sgmodule), kiểm tra `[Script]` và `[MITM]`.
4. Nhập RAW URL vào phần Modules, bật **duy nhất bản thử nghiệm mới**.
5. Không bật MITM diện rộng trên điện thoại chính hay tài khoản nhạy cảm. Nếu muốn kiểm thử, dùng môi trường tách biệt và quyền hợp lệ.
6. Thử từng ứng dụng, kiểm tra kết nối và log; khi lỗi thì tắt ngay module thử nghiệm.

URL:
```text
https://raw.githubusercontent.com/infiniti-money/Shadowrocket/main/modules/opt-in/All-Apps-Experimental.sgmodule
```

## Không nên làm

- Không bật song song bộ thử nghiệm này với ba module lẻ hoặc 10in1 cũ, vì tạo trùng script.
- Không hiểu "CI xanh" là bằng chứng script an toàn. Bộ kiểm tra mặc định chỉ áp dụng cho các module lọc domain.
- Không cài CA/HTTPS decryption không rõ nguồn gốc trên điện thoại chứa ngân hàng, tài khoản mật khẩu, dữ liệu cá nhân.

## Trạng thái xác minh

- Đã kiểm tra các nguồn module và file JavaScript liên quan còn truy cập được.
- Đã ghép cấu hình theo từng mục `[Rule]`, `[Header Rewrite]`, `[Url Rewrite]`, `[Script]` và `[MITM]`.
- Chưa chạy Shadowrocket thực tế trên iPhone.
- Bản chính `modules/Infiniti-All-In-One.sgmodule` vẫn giữ cấu hình không MITM.
