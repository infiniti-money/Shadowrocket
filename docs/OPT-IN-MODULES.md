# Bật module theo từng ứng dụng — thử nghiệm, không bật mặc định

Ngày kiểm tra: 21/11/2026. Đây là tính năng **opt-in**: bạn phải tự nhập và bật module trong ứng dụng Shadowrocket. Việc GitHub lưu file không bật module trên iPhone.

## Module đã bổ sung

| Module | URL trên GitHub | Kỹ thuật | Rủi ro |
|---|---|---|---|
| Spotify Experimental | [Spotify-Experimental.sgmodule](../modules/opt-in/Spotify-Experimental.sgmodule) | HTTP request & response scripts từ app2smile; MITM domain Spotify | Cao |
| Locket Experimental | [Locket-Experimental.sgmodule](../modules/opt-in/Locket-Experimental.sgmodule) | RevenueCat response/header scripts HuuTriet; MITM API chung | Rất cao |
| YouTube Rewrite Experimental | [YouTube-Rewrite-Experimental.sgmodule](../modules/opt-in/YouTube-Rewrite-Experimental.sgmodule) | Chặn một số endpoint quảng cáo/telemetry; MITM host YouTube | Cao |

### Quan trọng

- **Không phải bản mở khóa Premium hợp lệ.** Những script nhắm tới trạng thái thuê bao có thể không hoạt động khi ứng dụng xác minh quyền với máy chủ, và có thể vi phạm điều khoản sử dụng.
- Để xác nhận gói thuê bao đã trả tiền, sử dụng tính năng **Restore Purchases** của ứng dụng và kiểm tra tài khoản.
- Không bật bản Gaucuto 10in1, duyvinh09 All In One hay các module RevenueCat khác đồng thời với các bản thử nghiệm này.
- Không bật giải mã HTTPS cho tài khoản nhạy cảm trên iPhone chính chỉ để thử một module cộng đồng.
- Những module này sử dụng nguồn JavaScript bên ngoài từ nhánh main/master chưa ghim commit, có thể đổi nội dung sau này. URL truy cập được không có nghĩa script đã được kiểm toán.

## Thử nghiệm

1. Sao lưu cấu hình Shadowrocket trước khi thao tác.
2. Chọn **một** module thử nghiệm. Mở file trên GitHub để xem hostnames, script-path và cảnh báo.
3. Nếu vẫn quyết định thử, thực hiện trong môi trường thử nghiệm và chỉ cho phép hostname cần thiết; xem lưu lượng và log.
4. Khi có lỗi kết nối/đăng nhập, tắt module và HTTPS Decryption, xóa các CA tin cậy không còn dùng nếu bạn đã cài riêng.
5. Đừng coi giao diện hiển thị chữ “Premium” là bằng chứng có quyền mua hợp lệ.

## Tình trạng kiểm tra

- GitHub đã xác nhận file module và các URL script đích truy cập được vào ngày trên.
- Spotify: 2 script mục tiêu truy cập được; module dựa theo app2smile.
- Locket: 2 script truy cập được, nhưng scope MITM `api.revenuecat.com` có thể đụng chạm nhiều ứng dụng.
- YouTube: chỉ cài lại các rewrite thông thường và **không** đưa script JavaScript chưa kiểm toán vào. Không có PiP, background play hay Premium được xác nhận.
- Không có thử nghiệm thực tế trên iPhone, không có chứng nhận module tương thích.
