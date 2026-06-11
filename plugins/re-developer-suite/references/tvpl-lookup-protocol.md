# TVPL Lookup Protocol — Tra cứu & kiểm chứng văn bản pháp luật

> **Single source of truth** cho cách dùng MCP `tvpl` (Thư Viện Pháp Luật) trong bundle pháp lý. Các skill `licensing-expert`, `legal-counsel`, `re-legal-verification-rules` trỏ về file này thay vì lặp lại quy trình.

## Vì sao có protocol này

`RE-Legal` yêu cầu "kiểm tra hiệu lực trước khi viện dẫn". MCP `tvpl` cho phép làm việc đó **tự động**: tra văn bản, đọc đúng điều khoản, kiểm tra tình trạng hiệu lực, và lần theo mạng dẫn chiếu giữa các luật. Đây là công cụ tra cứu — **không thay thế phán đoán của luật sư** và không nâng kết quả tool thành kết luận chắc chắn.

## Bộ công cụ tvpl

| Tool | Dùng để | Trả về chính |
|---|---|---|
| `tvpl_status` | chẩn đoán khi tool khác lỗi (đã login chưa) | logged_in, has_credentials |
| `search_van_ban(keyword, loai_van_ban, limit)` | tìm văn bản theo tên / số hiệu | danh sách {ten, url, so_hieu} |
| `get_van_ban(url)` | toàn văn + metadata | ten, so_hieu, ngay_hieu_luc, tinh_trang, toan_van, source_url |
| `check_hieu_luc(url)` | tình trạng hiệu lực + văn bản thay thế | tinh_trang, van_ban_thay_the[], source_url |
| `liet_ke_dieu(url)` | mục lục các Điều | muc_luc [{so_dieu, tieu_de}] |
| `get_dieu(url, so_dieu)` | toàn văn 1 Điều + dẫn chiếu trong điều | noi_dung, dan_chieu[], source_url |
| `get_luoc_do(url)` | mạng quan hệ dẫn chiếu (căn cứ / sửa đổi / thay thế / hướng dẫn) | nhom[] {loai, van_ban[]} |
| `so_sanh_dieu(url1, so_dieu1, url2, so_dieu2)` | diff 2 điều (vd luật cũ vs mới) | giong_nhau, diff |

**Rate limit ~2.5s/call** → tra có chọn lọc, không quét tràn lan.

## Khi nào bắt buộc tra tvpl

- Trước **mọi kết luận pháp lý material** có viện dẫn văn bản.
- Khi trích dẫn một **Điều/Khoản** cụ thể làm căn cứ.
- Khi nghi văn bản đã bị **sửa đổi / thay thế / hết hiệu lực** (đặc biệt các luật BĐS đổi nhiều 2023–2025).
- Khi danh sách **tĩnh** trong `licensing-expert` (`vn-legal-texts.md`, `vn-realestate-legal-framework.md`) là nguồn duy nhất — phải đối chiếu động bằng tvpl.

## Trình tự chuẩn theo tình huống

### (a) Xác minh hiệu lực một văn bản
1. `search_van_ban(tên hoặc số hiệu)` — lấy `url`. *(Mẹo: filter `loai_van_ban` có thể không ổn định; ưu tiên `tat_ca` rồi tự lọc theo tên.)*
2. `check_hieu_luc(url)` — đọc `tinh_trang` + `van_ban_thay_the`.
3. Nếu có văn bản thay thế → mở `url` của bản thay thế, lặp lại.

### (b) Tra một điều khoản cụ thể
1. `search_van_ban` → `url`.
2. `liet_ke_dieu(url)` → tìm đúng `so_dieu`.
3. `get_dieu(url, so_dieu)` → trích **nguyên văn** điều đó + xem `dan_chieu`.

### (c) Đối chiếu luật cũ ↔ mới / lần theo dẫn chiếu
1. `get_luoc_do(url)` — xem nhóm "bị/được thay thế", "được căn cứ", "hướng dẫn".
2. `so_sanh_dieu(url_cũ, điều_cũ, url_mới, điều_mới)` — xem diff để biết điều khoản đổi gì.

## Quy tắc trích dẫn & caveat (bắt buộc)

- Luôn ghi **`source_url` + ngày tra cứu + tình trạng** cho mỗi văn bản viện dẫn.
- **Trích xuất có thể thiếu:** một số trang trả `tinh_trang`/`ngay_hieu_luc` dạng placeholder (vd `"Đã biết"`) hoặc rỗng. Khi đó **phải mở `source_url` để xác nhận bằng mắt**, không kết luận từ field rỗng.
- Không nâng kết quả tool thành kết luận chắc chắn — giữ nguyên tinh thần "luật sư kiểm chứng trước khi kết luận" (cảnh báo rủi ro cao của chính tool).
- tvpl **bổ sung**, không thay `operating-contract.md` source rules. Với văn bản địa phương, tvpl có thể không đủ — nêu rõ giới hạn.
- Nếu chưa tra được (tool lỗi / rate-limit / không tìm thấy): **nói rõ "chưa kiểm chứng hiệu lực qua tvpl"** thay vì im lặng giả định còn hiệu lực.
