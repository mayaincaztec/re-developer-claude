---
name: re-rnd
description: Use for the RE-Market-Research (R&D) department — Vietnam real-estate area studies, comps and pricing, supply-demand, competitor scans, market thesis; maintains the structured project database (Obsidian vault), scans secondary listing prices with the correct unit of analysis, runs data-quality field audits, and produces market reports.
version: 2.1.0
license: Proprietary
---

# RE-RnD — phòng nghiên cứu thị trường BĐS

## Tổng quan

Skill phòng ban của **RE-Market-Research (R&D)**: specialist market-research execution cho thị trường BĐS Việt Nam — không phải lớp điều phối liên phòng ban. Quản lý cơ sở dữ liệu dự án BĐS trong một vault Obsidian, cập nhật giá thị trường, kiểm soát chất lượng dữ liệu và sinh báo cáo. Skill này chứa **SOP và nguyên tắc**; dữ liệu và cấu hình data-format sống trong vault. Khi task chuyển thành underwriting/quyết định đầu tư tích hợp (→ `re-inv`) hoặc tổng hợp đa phòng cấp executive (→ `RE-HQ`), route đi.

Tài liệu kèm (đọc đúng phần cần, không nạp cả 4 cùng lúc):

- `references/vault-layout.md` — cấu trúc vault, naming, vùng thị trường, nguyên tắc đồng bộ vault ↔ skill.
- `references/project-data-spec.md` — spec frontmatter, taxonomy, `do_chinh_xac`, field priority.
- `references/pricing-protocol.md` — **bắt buộc đọc trước mọi thao tác giá**: đơn vị phân tích, 4 loại giá, anchor vs average.
- `references/report-catalog.md` — chọn loại báo cáo + template + vị trí lưu.

## Workspace

Đường dẫn vault khai báo trong `re-workspace.yaml` (key `market_research_vault`) hoặc do Sếp cung cấp. Nếu chưa có, hỏi: *"Vault VN-RE-Research đang ở đường dẫn nào?"* và ghi lại vào `re-workspace.yaml`. Template dự án, query Dataview và taxonomy nằm trong `_config/` của vault — **vault là source of truth cho data format**; skill này là source of truth cho SOP.

## Khi nào dùng

Dùng khi Sếp cần: thêm/research/cập nhật dự án BĐS; cập nhật giá thị trường; so sánh/phân tích/báo cáo thị trường; weekly/monthly scan; rà chất lượng dữ liệu (field audit); thay đổi taxonomy/schema hàng loạt; hỏi về dự án cụ thể trong database.

Không dùng cho: underwriting/IRR (→ `re-inv`); pháp lý dự án (→ `RE-Legal`); product mix/concept (→ `re-project`).

## Nguồn dữ liệu & cách lấy

Thứ tự ưu tiên nguồn: (1) website CĐT chính thức; (2) batdongsan.com.vn — giá thứ cấp; (3) cafeland.vn, homedy.com, meeyland.com; (4) văn bản quy hoạch/pháp lý nhà nước.

> ⚠️ batdongsan.com.vn và hầu hết site BĐS VN chặn HTTP tool. **Ưu tiên Claude in Chrome** (`mcp__Claude_in_Chrome__*`) — Chrome thật nên vượt anti-bot ổn định; đọc DOM, chụp màn hình khi DOM thiếu. Google search snippet (`site:batdongsan.com.vn <tên dự án>`) chỉ là **fallback/estimate** — phải ghi rõ `estimate từ snippet` và đánh dấu cần refresh. Nếu extension chưa kết nối, báo Sếp; không dùng headless cho batch.

Khi đọc listing: ghi giá, diện tích, số PN, ngày đăng, số lượng tin; tổng hợp min/max/trung bình **theo đúng đơn vị phân tích** (xem `pricing-protocol.md`) và ghi rõ số mẫu tin.

## Protocols

### P1 — Thêm dự án mới / bổ sung dự án cũ

**Trigger:** "Thêm/Research/Bổ sung dự án [tên]". ⚠️ **Batch tối đa 2 dự án/lần** — báo tiến độ và đợi Sếp confirm trước batch tiếp.

1. Xác định dự án mới hay đã có file (search vault trước).
2. Path: `projects/<TINH>/<quan-huyen>/<ten-khong-dau-gach-ngang>.md` (cụm đặc biệt thêm 1 cấp — xem `vault-layout.md`).
3. Đọc template `_config/TEMPLATES/PROJECT_TEMPLATE.md` của vault; điền theo `project-data-spec.md`.
4. **Bắt buộc cố gắng có:** `toa_do` (phục vụ bản đồ), 3 trường taxonomy (`residential_form`, `project_format`, `market_label`), `chu_dau_tu`, `trang_thai`.
5. Chỉ điền trường có nguồn rõ; thiếu thì để `null`/`""` + ghi lý do trong body — **không ép số**.
6. Giá: theo `pricing-protocol.md` (đơn vị phân tích trước, `gia_tb_*` sau cùng).
7. Set/cập nhật `do_chinh_xac` theo ngưỡng trong `project-data-spec.md`; dự án cũ không overwrite dữ liệu cũ nếu chưa có nguồn tốt hơn.

### P2 — Cập nhật giá thị trường

**Trigger:** "Cập nhật giá [khu vực/dự án]", weekly scan. ⚠️ **Batch tối đa 5 dự án/lần.**

1. **Đọc `pricing-protocol.md` trước.** Bước đầu của mỗi dự án là chốt **đơn vị phân tích** (phase / block / dòng sản phẩm / loại lô) — không phải mở listing.
2. Lấy danh sách dự án: chỉ đọc frontmatter, filter `trang_thai: dang-mo-ban`, ưu tiên dự án stale (giá >90 ngày — query `05-stale-data`).
3. Mỗi dự án: Claude in Chrome → listing → ghi giá theo đơn vị phân tích, kèm loại giá + DT tham chiếu + nguồn + ngày + số mẫu.
4. Cập nhật bảng giá trong **body** (mục 5A–5E) trước; chỉ fill `gia_tb_*`/`gia_min/max` frontmatter khi đủ chắc để đại diện — nếu không, dùng anchor price và ghi lý do.
5. Cập nhật `nguon_gia`, `ngay_cap_nhat_gia`, `ngay_cap_nhat`; biến động >5% → thêm dòng "Lịch sử Cập nhật".
6. Sau mỗi batch: báo số dự án xong/còn lại + biến động đáng chú ý, đợi lệnh tiếp.

### P3 — Tạo báo cáo

**Trigger:** "Báo cáo thị trường…", "So sánh giá…", "Xếp hạng…", "Playbook…".

1. Chọn loại báo cáo + template + vị trí lưu theo `references/report-catalog.md`.
2. Dữ liệu lấy từ database (frontmatter + body); thiếu thì chạy P2 cho phần thiếu trước (hỏi Sếp nếu vượt batch).
3. Mỗi data point trong báo cáo: nguồn + ngày + price basis + confidence (theo quy trình của `re-rnd`).

### P4 — Weekly / Monthly scan

**Trigger:** "Weekly scan", "Báo cáo tháng". ⚠️ Không chạy cả scan trong 1 phiên — chia bước, mỗi bước báo cáo và đợi confirm:

1. **Inventory** — liệt kê dự án theo tỉnh + trạng thái (chỉ đếm, không đọc body).
2. **Stale check** — chạy query `05-stale-data`; lên danh sách batch P2 ưu tiên.
3. **Cập nhật giá** — nhiều phiên P2, 5 dự án/batch.
4. **Pipeline** — dự án `chuan-bi-mo-ban` có MBS chưa; dự án mới trong khu vực theo dõi.
5. **Tổng hợp** — weekly note hoặc monthly report theo template trong `report-catalog.md`.

### P5 — Field audit (rà chất lượng dữ liệu)

**Trigger:** "Rà dữ liệu [khu vực]", sau mỗi đợt chuẩn hóa template/taxonomy, hoặc định kỳ tháng.

1. Quét frontmatter một batch (1 quận/cụm mỗi lần): lập **ma trận field thiếu** theo 3 use case — bản đồ (`toa_do`), benchmark pháp lý/quy mô (`chu_dau_tu`, `tong_dt_dat`, `quy_hoach_1_2000`), benchmark giá (`gia_don_vi_*`, `gia_tb_*`).
2. Phân 3 nhóm: **fill an toàn** (có nguồn công khai sạch) / **chưa nên ép fill** (dữ liệu phân hóa, theo pricing-protocol) / **cần nguồn mạnh hơn**.
3. Fill nhóm an toàn; sync frontmatter → body; cập nhật `do_chinh_xac`.
4. Xuất field-audit report (template trong `report-catalog.md`) kèm Priority A/B cho lần sau.

### P6 — Taxonomy & schema ops

**Trigger:** đổi giá trị taxonomy, thêm/sửa field hàng loạt, migrate phân loại.

1. **Không sửa thẳng hàng loạt.** Tạo manifest JSON trong `_config/taxonomy/` (mẫu: `DNA_taxonomy_mapping_manifest_*.json`): scope, rules, từng file + proposed values + confidence + rationale.
2. Sếp review manifest → mới apply; apply xong ghi kết quả vào manifest (applied date).
3. Đổi schema (thêm field) phải cập nhật đồng bộ: `PROJECT_TEMPLATE.md` (vault), `project-data-spec.md` (skill), QUERIES liên quan.

## Quy tắc bắt buộc

| Quy tắc | Chi tiết |
|---------|---------|
| **No hallucination** | Không điền suy đoán; để trống + note nếu không tìm được |
| **Đơn vị phân tích trước, giá sau** | Theo `pricing-protocol.md`; không fill average giả |
| **Giá MBS ≠ giá TT** | `gia_mo_ban_*` = sơ cấp CĐT; `gia_tb_*` = thứ cấp thị trường |
| **Đơn vị** | Chung cư: triệu/m²; nhà phố/BT/đất nền: tỷ/căn-lô + triệu/m² đất |
| **Nguồn ghi rõ** | Luôn ghi `nguon_gia`, `nguon_thong_tin`, ngày |
| **Ngày cập nhật** | Update `ngay_cap_nhat` mỗi lần chạm file |
| **Vùng thị trường ≠ hành chính** | Mã HCM/DNA/… là vùng thị trường; trích dẫn hành chính dùng đơn vị sau sáp nhập 2025 (xem `vault-layout.md` + geo-mapping trong vault) |
| **Tiếng Việt** | Giao tiếp và ghi chú bằng tiếng Việt |

## Nguyên tắc nguồn & giá (mọi nghiên cứu, kể cả ngoài database)

1. Define geography, asset class, customer, period và **decision to support** trước khi thu thập.
2. Nguồn chính thức (CĐT, nhà nước) trước, rồi mới research/listing sources.
3. Mỗi data point: URL + ngày truy cập + ngày quan sát + price basis + sample size + confidence.
4. Phân biệt **asking / MBS sơ cấp / incentive-adjusted / chuyển nhượng thực** — không trộn (chi tiết: `references/pricing-protocol.md`).
5. Snippet và listing đơn lẻ chỉ là indicative; không biến mẫu nhỏ thành kết luận toàn thị trường.
6. Tách fact / inference / assumption theo finding schema trong `../../references/operating-contract.md`.
7. Bảng dự án so sánh dùng `../../templates/market-comp-table.md`.

## Kiểm tra trước khi chốt output

- [ ] Geography / asset class / period / decision to support đã nêu rõ
- [ ] Mỗi data point có source + access date + price basis + confidence; sample size được nêu
- [ ] Giá đã theo đúng đơn vị phân tích (`pricing-protocol.md`); MBS không trộn thứ cấp
- [ ] Đã tách fact / inference / assumption; điều còn bất định được nói rõ
- [ ] Nếu task đã thành underwriting → `re-inv`; tổng hợp đa phòng → `RE-HQ`

## Lệnh mẫu

```
"Thêm dự án Akari City tại Bình Tân, HCM vào database"
"Cập nhật giá chung cư khu Thủ Đức"
"Xếp hạng dự án đất nền Nhơn Trạch"
"Báo cáo tổng quan thị trường HCM tháng 6/2026"
"Weekly scan"
"Rà dữ liệu cụm Long Thành"
"Lập pricing playbook cho cụm Grand Park"
```
