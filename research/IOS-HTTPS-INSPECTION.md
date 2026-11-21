# Nghiên cứu HTTPS inspection trên iOS — 2026-11-21

> Phục vụ debugging, QA và nghiên cứu **lưu lượng của ứng dụng/hạ tầng mà bạn có quyền kiểm tra**. Các mục bên dưới không tự động giải mã HTTPS trên iPhone và không cấp quyền Premium. Không bật MITM toàn cục hay giải mã tài khoản/ngân hàng/ứng dụng người khác.

## Nguồn GitHub và khả năng áp dụng

| Dự án | Repository | iOS | Vai trò trong Shadowrocket |
|---|---|---|---|
| mitmproxy | https://github.com/mitmproxy/mitmproxy | iPhone/iPad kết nối qua HTTP proxy, CA tin cậy | Trình xem request/response độc lập, không phải file `.sgmodule` |
| HTTP Toolkit | https://github.com/httptoolkit/httptoolkit | Hướng dẫn kết nối proxy trên iOS | Debug và kiểm tra lưu lượng do người dùng sở hữu |
| Proxyman | https://github.com/ProxymanApp/Proxyman | Mac/iOS, có SSL proxying | Công cụ debug desktop/iPhone |
| Proxyman Docs | https://github.com/ProxymanApp/docs | Chứng chỉ và hướng dẫn kết nối iPhone | Tham khảo vòng đời CA, phạm vi hostname |
| Shadowrocket config examples | https://github.com/haritos90/shadowrocket-config-files | Cú pháp `[MITM]` của Shadowrocket | Tham khảo cú pháp; không sao chép cấu hình proxy/chứng chỉ |
| Shadowrocket Handbook | https://github.com/jamespeter20110915/Shadowrockt-Handbook | Chương MITM, scope & verification | Tham khảo cấu hình và rủi ro CA |
| HTTP Toolkit pinning demo | https://github.com/httptoolkit/ios-ssl-pinning-demo | Demo app cố ý có pinning | Chỉ để hiểu trường hợp MITM thất bại |

Nguồn tham khảo chính thức:
- https://docs.mitmproxy.org/stable/concepts/certificates/
- https://httptoolkit.com/docs/guides/ios/
- https://proxyman.com/docs/debug-devices/ios-device
- https://proxyman.com/docs/proxyman-ios/vpn-and-proxyman-certificate

## HTTPS interception hoạt động ra sao?

1. Ứng dụng tạo kết nối TLS tới một hostname.
2. Proxy/Shadowrocket chỉ giải mã được nội dung khi ứng dụng chấp nhận chuỗi chứng chỉ do CA kiểm thử cấp và kết nối được định tuyến qua proxy.
3. Kiểm tra hostname trong `[MITM]` giới hạn tên miền mục tiêu, **không giới hạn quyền ký của chứng chỉ CA được hệ thống tin cậy**.
4. Certificate pinning, kiểm tra chứng chỉ riêng hoặc một số giao thức có thể khiến ứng dụng từ chối kết nối. **Không dùng kỹ thuật bypass pinning trên ứng dụng mà bạn không kiểm soát**.
5. Nếu MITM thất bại, tắt module/chứng chỉ và chuyển về cấu hình không giải mã.

## Kiến trúc đã tích hợp

- `modules/Infiniti-All-In-One.sgmodule`: vẫn là bộ chặn quảng cáo/Privacy thông thường, **không MITM**.
- `modules/templates/HTTPS-Debug-Own-App.sgmodule.example`: mẫu **vô hiệu hóa hoàn toàn**, dành cho app và domain do bạn quản lý. Thay hostname rồi tự chuyển thành module sau khi đánh giá.
- `scripts/audit_mitm.py`: liệt kê các hostnames và script liên quan MITM trong `modules/opt-in/` và `modules/experimental/`; không sửa hay bật các module.

## Quy trình thử nghiệm tối thiểu

1. Chỉ dùng app thử nghiệm hoặc dịch vụ do bạn sở hữu/được cấp quyền, ưu tiên máy/test account riêng.
2. Sao lưu cấu hình Shadowrocket trước khi cài.
3. Tạo CA thử nghiệm bằng công cụ bạn chọn; cài và tin cậy CA **chỉ khi cần**. Không lưu khóa riêng CA trong GitHub.
4. Giới hạn `hostname` vào **một domain cụ thể** do bạn quản lý. Tránh wildcard `*`, RevenueCat dùng chung, `buy.itunes.apple.com`, dịch vụ ngân hàng và đăng nhập.
5. Bắt đầu bằng kiểm tra metadata; không ghi headers `Authorization`, `Cookie`, body chứa dữ liệu cá nhân hay token.
6. Thử endpoint giả lập trong môi trường sandbox trước; theo dõi lỗi TLS/đăng nhập và chỉ chuyển đổi response nếu bạn có quyền.
7. Kết thúc phiên kiểm tra, **tắt HTTPS Decryption, bỏ cấu hình proxy và gỡ CA** nếu không còn sử dụng. Kiểm tra lại truy cập HTTPS bình thường.

## Những điều không được hiểu nhầm

- HTTP 200 hoặc GitHub Actions xanh **không** có nghĩa MITM hoạt động trên mọi ứng dụng.
- Giải mã phản hồi dịch vụ thanh toán không tạo ra quyền thuê bao hợp lệ.
- File module của Shadowrocket **không thể tự bật** thiết lập iOS/ứng dụng hay cài CA từ GitHub.
- Script `Premium` trong `modules/opt-in/` là các bản thử nghiệm chưa kiểm toán; không được hợp nhất vào mặc định.
