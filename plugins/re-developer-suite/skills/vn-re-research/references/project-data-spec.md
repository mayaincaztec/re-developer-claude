# Project Data Spec — quy tắc điền dữ liệu file dự án

> Đọc cùng `_config/TEMPLATES/PROJECT_TEMPLATE.md` của vault (source of truth schema). File này quy định **cách điền đúng**, không lặp lại toàn bộ schema.

## Nhóm trường & ưu tiên theo use case

| Use case | Trường bắt buộc cố gắng có | Vì sao |
|---|---|---|
| Bản đồ | `toa_do` ("lat, lng"), `google_map` | tools/ban-do-du-an.html ăn theo `toa_do` |
| Benchmark pháp lý/quy mô | `chu_dau_tu`, `tong_dt_dat`, `quy_hoach_1_2000`, `trang_thai_phap_ly` | so sánh dự án + screening deal |
| Benchmark giá | bảng giá body (5A–5E) trước, `gia_don_vi_*`/`gia_tb_*` sau | theo `pricing-protocol.md` |
| Phân loại/query | `residential_form`, `project_format`, `market_label`, `phan_khuc`, `trang_thai` | Dataview + lọc thị trường |

## Taxonomy v2 (bắt buộc cho file mới)

- **`residential_form`**: `lowrise` (thuần thấp tầng/đất nền) | `highrise` (thuần căn hộ; retail đế nhỏ không đổi phân loại) | `hybrid` (cả hai cấu phần đều đáng underwriting riêng).
- **`project_format`**: `single-product` | `mixed-product-residential` (nhiều dòng sản phẩm ở nhưng chưa phải mixed-use) | `mixed-use` (≥2 công năng chính: residential + retail/office/hotel…) | `master-planned-community` (đại đô thị nhiều phase).
- **`market_label`**: `khu-dan-cu` | `khu-do-thi` | `township` | `compound` | `phuc-hop` | `khu-can-ho` | `tai-dinh-cu`.
- `loai_hinh` là trường legacy giữ cho backward compatibility; nếu lệch taxonomy mới, ghi rationale trong mục 9 của file dự án.
- Đổi giá trị taxonomy hàng loạt → bắt buộc qua manifest (P6), không sửa thẳng.

## Trường hành chính

- `tinh_thanh` + `quan_huyen` + `phuong_xa`: **vùng thị trường** (giữ tên cũ, ổn định cho phân tích).
- `don_vi_hanh_chinh_2025`: đơn vị hành chính hiện hành sau sáp nhập (vd "phường Long Tân, TP.HCM") — dùng khi báo cáo cần trích dẫn chính thức; tra `_config/taxonomy/geo-mapping.md`.

## `do_chinh_xac` — ngưỡng

- `cao`: ≥70% trường trọng yếu có nguồn rõ, giá có đơn vị phân tích đúng.
- `trung-binh`: 40–70%.
- `thap`: <40% hoặc nguồn chủ yếu là snippet/estimate.
- `chua-xac-nhan`: mới khởi tạo, chưa kiểm.

## Quy tắc điền

1. **Null + lý do** thay vì ép số: trường không có nguồn rõ để `null`/`""` và ghi lý do trong body (mục liên quan hoặc "Xung đột dữ liệu").
2. **Frontmatter → body sync**: dữ liệu đã có trong frontmatter phải xuất hiện ở bảng body tương ứng (Tổng quan, Quy mô…), không để body trống trong khi frontmatter có số.
3. **Không overwrite bằng nguồn yếu hơn**: dữ liệu cũ có nguồn tốt chỉ được thay khi nguồn mới mạnh hơn hoặc mới hơn rõ rệt; ghi vào "Lịch sử Cập nhật".
4. **Tiện ích hiện hữu ≠ marketing claim**; **giá MBS ≠ giá thứ cấp** — không trộn.
5. Mỗi lần chạm file: update `ngay_cap_nhat`; chạm giá: update thêm `nguon_gia` + `ngay_cap_nhat_gia`.

## Bảng phân khúc tham chiếu (as-of 2025, chuẩn HCM)

| Phân khúc | Giá CC (tr/m²) | Giá NP (tr/m² đất) |
|-----------|----------------|---------------------|
| affordable | <35 | <80 |
| mid-end | 35–70 | 80–150 |
| high-end | 70–120 | 150–250 |
| luxury | 120–200 | 250–400 |
| ultra-luxury | >200 | >400 |

Vùng vệ tinh điều chỉnh giảm ~10–20%. Bảng này để **gán `phan_khuc`**, không phải benchmark giá; mặt bằng giá từng khu xem `_index.md` của tỉnh trong vault (cập nhật theo dữ liệu thật). Rà lại bảng này mỗi năm.
