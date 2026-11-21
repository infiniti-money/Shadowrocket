# Bộ sưu tập script Premium iOS — danh mục nghiên cứu

> Kiểm tra nguồn: 21/11/2026. Đây là **danh mục liên kết tham khảo**, không phải module tự động kích hoạt các script. Kết quả **truy cập được** chỉ có nghĩa là file RAW được GitHub trả về tại thời điểm kiểm tra, không xác nhận tính an toàn, tính hợp pháp, hay chức năng mở khóa.

## Danh sách đã kiểm tra RAW

| Ứng dụng | Nguồn | RAW đã kiểm tra | Rủi ro | Ghi chú |
|---|---|---|---|---|
| Spotify | [app2smile/rules](https://github.com/app2smile/rules) | [spotify.module](https://raw.githubusercontent.com/app2smile/rules/master/module/spotify.module) | Cao | Header Rewrite, JavaScript và MITM; mô tả mở một phần chức năng, không phải quyền thuê bao hợp lệ |
| Spotify | [KhunTam/Shadowrocket](https://github.com/KhunTam/Shadowrocket) | [spotify.sgmodule](https://raw.githubusercontent.com/KhunTam/Shadowrocket/main/spotify.sgmodule) | Cao | Bản dẫn xuất, vẫn sử dụng script bên ngoài; không bật cùng app2smile |
| Locket | [HuuTriet/ios-scripts-collection](https://github.com/HuuTriet/ios-scripts-collection) | [LocketTriet.sgmodule](https://raw.githubusercontent.com/HuuTriet/ios-scripts-collection/main/LocketTriet.sgmodule) | Rất cao | Script HTTP response nhắm tới RevenueCat |
| Locket | [TTSan1208/scripts](https://github.com/TTSan1208/scripts) | [locket.sgmodule](https://raw.githubusercontent.com/TTSan1208/scripts/main/locket.sgmodule) | Rất cao | MITM, điều chỉnh request/response thuê bao, User-Agent giả định |
| Locket | [Trung-Han/LocketIOS15-26](https://github.com/Trung-Han/LocketIOS15-26) | [LocketPTP](https://raw.githubusercontent.com/Trung-Han/LocketIOS15-26/main/LocketPTP) | Rất cao | Trỏ tới JavaScript bên thứ ba; chưa kiểm toán phụ thuộc |
| YouTube | [dhungx/modules-shadowrocket](https://github.com/dhungx/modules-shadowrocket) | [youtube.module](https://raw.githubusercontent.com/dhungx/modules-shadowrocket/main/youtube.module) | Cao | Có quy tắc chặn UDP và xử lý video; bản ghi ngày 23/09/2024 nên cần kiểm thử tương thích |
| Hỗn hợp (Spotify, SoundCloud, Locket, YouTube) | [llygad/Shadowrocket-modules](https://github.com/llygad/Shadowrocket-modules) | [All.sgmodule](https://raw.githubusercontent.com/llygad/Shadowrocket-modules/main/All.sgmodule) | Rất cao | Nhiều script và hostname MITM; dễ xung đột |

## Các nguồn cần xem thêm, chưa đồng nghĩa đã kiểm toán

- [K4Z3X0R/NguyenNgocAnhTu](https://github.com/K4Z3X0R/NguyenNgocAnhTu): repository mô tả nhiều thay đổi liên quan Premium, RevenueCat và cấu hình.
- [nqkhaii/ShadowRocket](https://github.com/nqkhaii/ShadowRocket): bộ cấu hình tổng hợp, mô tả Spotify, Locket, YouTube.
- [Maasea/sgmodule](https://github.com/Maasea/sgmodule): nguồn module về xử lý quảng cáo YouTube và các khả năng liên quan phát video; cần kiểm tra Shadowrocket support.
- [RevenueCat/purchases-ios](https://github.com/RevenueCat/purchases-ios): SDK chính thức để hiểu quy trình quyền thuê bao thực và môi trường thử nghiệm.

## Vì sao không tự động ghép thành All-in-One Premium?

1. Nhiều module dùng cùng `api.revenuecat.com`, cùng endpoint subscriber/receipts. Kết quả phụ thuộc vào thứ tự và có thể làm hỏng những ứng dụng khác.
2. Một số module đòi hỏi `[MITM]` với hostnames liên quan tài khoản/đăng ký, có nguy cơ tiếp xúc nội dung HTTPS nhạy cảm.
3. Các `script-path` dẫn đến nhánh `main`/`master` có thể thay đổi mà không thông báo. Cần kiểm toán script và ghim commit trước khi chạy.
4. Dự án này không có bằng chứng thử nghiệm các script bằng Shadowrocket trên iPhone; không được công bố là hoạt động ổn định.
5. Sửa nội dung response gắn nhãn Premium không tạo giao dịch mua hợp lệ, có thể vi phạm điều khoản dịch vụ và không vượt qua kiểm tra quyền phía server.

## Quy trình đánh giá nếu muốn phát triển module riêng

- Đọc toàn bộ mã nguồn JavaScript và phụ thuộc được tải động; tìm lệnh gọi ra ngoài, dữ liệu tài khoản, logic thay đổi request.
- Đánh giá endpoint nào thực sự cần MITM và loại mọi hostname không liên quan.
- Không dùng chung các bộ response-rewrite cho RevenueCat hoặc iTunes.
- Chỉ kiểm thử trên thiết bị/tài khoản thử nghiệm với ứng dụng bạn sở hữu hoặc được phép kiểm thử.
- Đối với quyền Premium đã mua, ưu tiên chức năng Restore Purchases và xác minh entitlement từ server.

**Các module tham khảo ở đây không được nhập tự động vào `modules/Infiniti-All-In-One.sgmodule`.**
