# Infiniti Shadowrocket v1.1 — bảo trì và giám sát nguồn

Ngày cập nhật: 21/11/2026

## Những thay đổi đã thực hiện

1. **Giữ nguyên URL cài đặt chính:** `modules/Infiniti-All-In-One.sgmodule`, hiện gồm Advertising + Privacy từ blackmatrix7, không MITM.
2. **Thêm [rules/upstreams.json](../rules/upstreams.json):** danh sách cho phép (allowlist) các URL quy tắc cần giám sát.
3. **Thêm [scripts/check_upstreams.py](../scripts/check_upstreams.py):** tự kiểm tra URL, định dạng file, UTF-8, giới hạn kích thước và các dòng rule hợp lệ; không tải hoặc thực thi JavaScript.
4. **Nâng cấp GitHub Actions:** chạy các kiểm tra tĩnh và kiểm tra nguồn mỗi khi push, pull request, chạy thủ công, và theo lịch **02:17 UTC hàng ngày** (09:17 giờ Việt Nam).
5. **Giữ nguyên `modules/experimental/`:** hai bộ Premium gốc để nghiên cứu, không bật trong bản chính. Các script liên quan thuê bao và MITM không được tự kích hoạt.

## Lệnh kiểm tra

```bash
python3 scripts/validate.py
python3 scripts/check_upstreams.py --offline
python3 scripts/check_upstreams.py
```

`--offline` chỉ kiểm tra manifest và liên kết file tại repository, không cần Internet. Lệnh cuối kiểm tra nội dung quy tắc từ nguồn ngoài; có thể báo lỗi khi mạng/nguồn tạm gián đoạn.

## Cấu hình iPhone

Cài module chính tại:
```text
https://raw.githubusercontent.com/infiniti-money/Shadowrocket/main/modules/Infiniti-All-In-One.sgmodule
```

Nếu đang dùng `AdBlock-Lite` hoặc `Privacy-Only`, không bật cùng lúc vì quy tắc trùng lặp. Có thể thử `Vietnam-Threat-Protection` riêng, theo dõi REJECT để phát hiện false positive.

**Giới hạn:** Định dạng module được kiểm tra tĩnh, chưa kiểm tra bằng trình nhập Shadowrocket trên iPhone. Bộ rule không bảo đảm xóa quảng cáo trên YouTube/TikTok trong ứng dụng hoặc mở khóa Pro/Premium của bên thứ ba. Upstream sử dụng nhánh `master`, không ghim commit nên có thể thay đổi.

## Cách đọc kết quả CI

- Xanh: bộ kiểm tra tĩnh và các nguồn được tải thành công tại thời điểm chạy.
- Đỏ: mở Actions, xem bước nào lỗi; không nên tự sửa bằng cách thay URL trôi nổi.
- Không kết luận script Premium an toàn chỉ vì CI xanh: chúng được lưu làm tư liệu và **không nằm trong tập kiểm tra cho phép để bật**.

## Nguồn và giấy phép

- [blackmatrix7/ios_rule_script](https://github.com/blackmatrix7/ios_rule_script)
- [bigdargon/hostsVN](https://github.com/bigdargon/hostsVN)
- [Danh mục script nghiên cứu](../research/PREMIUM-SCRIPT-CATALOG.md)

Đây là bộ dự án riêng của infiniti-money, tham chiếu URL nguồn gốc; không tự nhận quyền tác giả đối với quy tắc và script bên ngoài.
