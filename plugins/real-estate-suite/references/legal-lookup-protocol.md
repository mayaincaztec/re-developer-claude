# Legal Lookup Protocol — Tra cứu & kiểm chứng văn bản pháp luật

> **Single source of truth** cho cách dùng MCP `legal` trong bundle pháp lý. Các skill `re-legal-licensing`, `re-legal-counsel`, `re-legal-verification-rules` trỏ về file này thay vì lặp lại quy trình.

## Vì sao có protocol này

`RE-Legal` yêu cầu "kiểm tra hiệu lực trước khi viện dẫn". MCP `legal` cho phép làm việc đó **tự động**: tra văn bản, đọc đúng điều khoản, kiểm tra tình trạng hiệu lực, và lần theo mạng dẫn chiếu giữa các luật. Đây là công cụ tra cứu — **không thay thế phán đoán của luật sư** và không nâng kết quả tool thành kết luận chắc chắn.

## Hai nguồn trong MCP `legal`

`legal` gộp 2 nguồn, chọn qua tham số `source` ở mọi tool:

| `source` | Hành vi |
|---|---|
| `"auto"` (mặc định) | thử **vbpl** trước; nếu **0 kết quả** → tự fallback **tvpl** |
| `"vbpl"` | Cơ sở dữ liệu quốc gia về pháp luật (vbpl.vn, Bộ Tư pháp) — chính thống, miễn phí, hiệu lực có **mã máy đọc** |
| `"tvpl"` | Thư Viện Pháp Luật (thuvienphapluat.vn) — cập nhật nhanh, có văn bản vbpl **chưa index** (vd nghị định mới ban hành) |

**Định danh văn bản (`ref`) khác nhau theo nguồn** — mỗi item kết quả mang theo `source` + `ref`:
- vbpl: `ref` = `doc_id` (GUID hoặc số).
- tvpl: `ref` = URL trên thuvienphapluat.vn.

Các tool chi tiết tự định tuyến khi `source="auto"`: `ref` là URL → tvpl, còn lại → vbpl.

## Bộ công cụ legal

| Tool | Dùng để | Trả về chính |
|---|---|---|
| `legal_status()` | chẩn đoán cả 2 nguồn (vbpl config, tvpl đã login chưa) | primary, fallback, vbpl, tvpl |
| `search_van_ban(keyword, source, search_in, match_mode, scope, doc_type, issue_date_from, issue_date_to, eff_status, loai_van_ban, page_size, page)` | tìm văn bản theo tên / số hiệu, kèm filter | {source, total, items[{source, ref, doc_num, title, doc_type, issue_date, eff_status}]} |
| `get_van_ban(ref, source)` | toàn văn + metadata | doc_num, title, eff_status(+code), full_text, file_pdf/doc, source_url |
| `check_hieu_luc(ref, source)` | tình trạng hiệu lực | eff_status, eff_status_code, eff_from/to, source_url |
| `liet_ke_dieu(ref, source)` | mục lục các Điều | dieu_list [{so_dieu, tieu_de}] |
| `get_dieu(ref, so_dieu, source)` | nguyên văn 1 Điều | text, found, source_url |
| `get_luoc_do(ref, source)` | mạng quan hệ dẫn chiếu (căn cứ / sửa đổi / thay thế / hướng dẫn) | references[] (vbpl: kèm quan hệ cấp điều khoản) |
| `so_sanh_dieu(ref1, so_dieu1, ref2, so_dieu2, source1, source2)` | diff 2 điều — **được phép khác nguồn** (vd luật cũ ở tvpl ↔ luật mới ở vbpl) | diff, left/right.found |

### Filter nâng cao của `search_van_ban` (áp cho nhánh vbpl)
- `search_in`: `all` | `title` | `content` | `docnum`
- `match_mode`: `all_words` | `exact_phrase`
- `scope`: `tw` (Trung ương) | `dp` (Địa phương) | `all`
- `doc_type`: `luat` | `nghi_dinh` | `thong_tu` | `bo_luat` | `phap_lenh`
- `issue_date_from` / `issue_date_to`: `YYYY-MM-DD` (cần **cả hai** mốc)
- `eff_status`: mã hiệu lực (vd `CCHL` chưa hiệu lực, `HHL1P` hết hiệu lực một phần)
- `loai_van_ban`: lọc loại cho nhánh **tvpl** (tat_ca/luat/nghi_dinh/thong_tu/…)

**Rate limit:** vbpl ~1.5s/call, tvpl ~2.5s/call → tra có chọn lọc, không quét tràn lan.

## Khi nào bắt buộc tra legal

- Trước **mọi kết luận pháp lý material** có viện dẫn văn bản.
- Khi trích dẫn một **Điều/Khoản** cụ thể làm căn cứ.
- Khi nghi văn bản đã bị **sửa đổi / thay thế / hết hiệu lực** (đặc biệt các luật BĐS đổi nhiều 2023–2025).
- Khi danh sách **tĩnh** trong `re-legal-licensing` (`vn-legal-texts.md`, `vn-realestate-legal-framework.md`) là nguồn duy nhất — phải đối chiếu động bằng `legal`.

## Trình tự chuẩn theo tình huống

### (a) Xác minh hiệu lực một văn bản
1. `search_van_ban(tên hoặc số hiệu)` — lấy `ref` + `source` của đúng văn bản. *(Tra số hiệu: dùng `search_in="docnum"` + `match_mode="exact_phrase"` cho chính xác.)*
2. `check_hieu_luc(ref, source)` — đọc `eff_status` (+ `eff_status_code`).
3. Văn bản thay thế/sửa đổi → xem `get_luoc_do(ref, source)`, mở `ref` của bản liên quan, lặp lại.

### (b) Tra một điều khoản cụ thể
1. `search_van_ban` → `ref` + `source`.
2. `liet_ke_dieu(ref, source)` → tìm đúng `so_dieu`.
3. `get_dieu(ref, so_dieu, source)` → trích **nguyên văn** điều đó.

### (c) Đối chiếu luật cũ ↔ mới / lần theo dẫn chiếu
1. `get_luoc_do(ref, source)` — xem nhóm "bị/được thay thế", "được căn cứ", "hướng dẫn".
2. `so_sanh_dieu(ref_cũ, điều_cũ, ref_mới, điều_mới)` — diff để biết điều khoản đổi gì (kể cả khi 2 bản ở 2 nguồn khác nhau).

### (d) Văn bản mới ban hành nhưng vbpl chưa có
Để `source="auto"`: vbpl trả 0 → tự fallback tvpl. Hoặc ép `source="tvpl"` khi biết văn bản vừa ban hành (vbpl index chậm hơn). Ghi rõ nguồn trong dẫn chiếu.

## Quy tắc trích dẫn & caveat (bắt buộc)

- Luôn ghi **`source_url` + `source` (vbpl/tvpl) + ngày tra cứu + tình trạng** cho mỗi văn bản viện dẫn.
- **Ưu tiên nguồn chính thống:** khi cùng một văn bản có ở cả hai, lấy hiệu lực từ **vbpl** (Bộ Tư pháp, có mã hiệu lực) làm chuẩn; tvpl để đối chiếu/khi vbpl chưa có.
- **Trích xuất có thể thiếu:** nếu field hiệu lực rỗng/placeholder, **mở `source_url` xác nhận bằng mắt**, không kết luận từ field rỗng.
- Không nâng kết quả tool thành kết luận chắc chắn — giữ tinh thần "luật sư kiểm chứng trước khi kết luận".
- `legal` **bổ sung**, không thay `operating-contract.md` source rules. Văn bản địa phương: dùng `scope="dp"` (vbpl), nếu vẫn thiếu thì nêu rõ giới hạn.
- Nếu chưa tra được (tool lỗi / rate-limit / không tìm thấy ở cả hai nguồn): **nói rõ "chưa kiểm chứng hiệu lực qua legal"** thay vì im lặng giả định còn hiệu lực.
