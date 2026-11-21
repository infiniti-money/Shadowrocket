# Tích hợp hai file cấu hình Shadowrocket do người dùng cung cấp

Ngày thực hiện: 21/11/2026.

## Files

- [10in1_Vip_ProMax.sanitized.conf.txt](../sources/user-uploads/10in1_Vip_ProMax.sanitized.conf.txt): bản xuất Gaucuto người dùng tải lên, giữ lại quy tắc và 17 khai báo script.
- [All_In_One.sanitized.conf.txt](../sources/user-uploads/All_In_One.sanitized.conf.txt): bản xuất duyvinh09 người dùng tải lên, giữ lại quy tắc và 24 khai báo script.
- [Full-Source-Merge-Experimental.sgmodule](../modules/opt-in/Full-Source-Merge-Experimental.sgmodule): bản tích hợp thử nghiệm từ hai nguồn, không phải cấu hình mặc định.

**Cả hai tệp nguồn được công khai đã loại bỏ hoàn toàn `ca-p12` và `ca-passphrase`**. Các tệp gốc do người dùng tải lên có chứa chứng chỉ PKCS#12 riêng tư và mật khẩu, không được đưa lên GitHub. Không sao chép chúng vào repository, Issue hay log. Nếu chứng chỉ đó từng được chia sẻ ở nơi công khai hoặc bạn không còn kiểm soát khóa riêng, hãy ngừng tin cậy CA đó và tạo CA thử nghiệm mới trong ứng dụng của bạn.

## Cấu trúc thử nghiệm tổng hợp

| Section | Active directives |
|---|---:|
| `[Rule]` | 5 (Advertising, Privacy, hostsVN Threats, 2 YouTube UDP rejects) |
| `[URL Rewrite]` | 5 |
| `[Header Rewrite]` | 2 |
| `[Map Local]` | 1 |
| `[Script]` | 24 |
| `[MITM]` | 1 danh sách, 28 hostname/pattern |

24 khai báo script gồm Sub-Store (3), YouTube (2), Spotify (2), SoundCloud, VSCO, Alight Motion, PicsArt (2), Wink, Truecaller, Lightroom, KineMaster, CamScanner, BeautyPlus, Locket/RevenueCat (3), iTunes, Snow, Meitu. Bản gốc Gaucuto có 17 khai báo; các tên trùng giữa hai nguồn đã được gom lại.

### Những thay đổi biên tập trong module tổng hợp

- Các quy tắc trùng được loại bỏ.
- Spotify JSON/Proto ưu tiên đường dẫn app2smile từ bản Gaucuto, thay vì các URL duyvinh09 từng trả về 404.
- Dòng VSCO thiếu `pattern=` và dấu phẩy được sửa thành khai báo dễ phân tích hơn.
- Dòng CamScanner được bỏ dấu cách sau `pattern=`.
- Dòng YouTube response bỏ `engine={{{script}}}` chưa được thay thế và khối `argument` JSON không đáng tin; dùng `engine=jsc` trong cấu hình thử nghiệm. Điều này **không chứng minh** script JavaScript đích hoạt động.
- Danh sách hostname MITM của hai tệp được hợp nhất, bỏ mục rỗng và `%APPEND%` trùng. Không thêm CA, không thay chứng chỉ hay buộc iOS tin cậy CA.
- Không thêm script từ những file nguồn khác không có trong hai tệp bạn cung cấp vào nhóm khai báo đang bật.

## Các hạn chế quan trọng

**24 khai báo không có nghĩa 24 script hoạt động.** Phần lớn URL `duyvinh09/Module_IOS` đã từng trả về 404. Một số script nhắm vào endpoints thuê bao dùng chung RevenueCat, thay đổi thông tin mua hàng và có thể gây hỏng kết nối những ứng dụng khác. Sub-Store Sync là tác vụ theo lịch, không phải script Premium. Không có kiểm tra trên iPhone, không có chứng nhận Premium hoạt động.

Đây là module **HIGH-RISK**, **chỉ dành cho kiểm tra có quyền**. Nó là tài liệu thử nghiệm mới, **không thay đổi** file `modules/Infiniti-All-In-One-Extended.sgmodule` đang được bạn dùng.

## URL cài bản thử nghiệm

```text
https://raw.githubusercontent.com/infiniti-money/Shadowrocket/main/modules/opt-in/Full-Source-Merge-Experimental.sgmodule
```

Không bật nó đồng thời với Gaucuto 10in1, duyvinh09 All In One, Infiniti Extended, Spotify/Locket/YouTube Experimental hoặc các module khác cùng intercept. Sao lưu cấu hình trước. Nếu ứng dụng lỗi TLS, đăng nhập hoặc phát video, tắt module và HTTPS Decryption, trở về bản ổn định.

## Kiểm tra trong repository

```bash
python3 scripts/validate_user_sources.py
python3 scripts/check_script_sources.py --online
```

Các lệnh kiểm tra cú pháp tĩnh và trạng thái truy cập của URL, không chạy JavaScript hay chứng minh khả năng giải mã thực tế.
