---
name: re-investment-screening
description: Use to quickly screen an inbound real-estate deal (teaser, CIM, broker offer, or basic project info) and produce a fast go / pass gate before committing analyst time to a preliminary investment report.
version: 1.0.0
license: MIT
---

# RE-Investment Screening

Cổng go/no-go nhanh ở đầu vòng đời thương vụ trong `RE-Investment-Finance`. Mục tiêu là **lọc deal** trước khi bỏ công làm Báo cáo đầu tư sơ bộ, không phải phân tích sâu.

## When to Use

Dùng khi: nhận teaser / CIM / chào deal từ môi giới / thông tin dự án cơ bản; cần quyết định nhanh **theo đuổi hay bỏ**; cần shortlist nhiều deal cùng lúc.

Do not use for: phân tích khả thi chi tiết (→ `re-preliminary-investment-report` / `re-feasibility-study`); thẩm định sâu (→ `dd-coordinator`).

## Workflow

### Bước 1 — Tóm tắt deal
Chốt nhanh: loại tài sản, vị trí, quy mô (diện tích/GFA/số sản phẩm), giá chào / tổng mức đầu tư ước tính, hình thức (share/asset/JV), bên bán, mốc thời gian.

### Bước 2 — Áp bộ tiêu chí sàng lọc
Đánh giá nhanh từng nhóm (Pass / Flag / Fail):
- **Chiến lược**: có khớp khẩu vị đầu tư (loại hình, địa bàn, ticket size) không?
- **Pháp lý sơ bộ**: có red flag rõ ràng (đất chưa sạch, chưa có chủ trương, tranh chấp, condotel/officetel hạn chế sổ) — nếu cần, kéo `licensing-expert` 1 câu hỏi.
- **Thị trường sơ bộ**: giá vào so với mặt bằng khu vực hợp lý không (kéo `re-market-research`/`vn-re-research` nếu cần 1 con số).
- **Tài chính sơ bộ**: giá chào vs giá trị ước tính thô; có khả năng đạt return tối thiểu không?
- **Thực thi**: có deal-breaker hiển nhiên về timeline / vốn / đối tác không?

### Bước 3 — Kết luận go / pass
Chốt **Proceed** (chuyển sang Báo cáo đầu tư sơ bộ) / **Pass** (bỏ) / **Watch** (theo dõi, chưa làm), kèm 2–3 lý do và các câu hỏi tối thiểu cần làm rõ nếu Proceed.

## Output

Dùng template `../../templates/deal-screening-note.md`. Tối thiểu: tóm tắt deal, bảng tiêu chí (Pass/Flag/Fail), kết luận go/pass/watch, lý do, câu hỏi mở.

## Nguyên tắc

- Nhanh và bảo thủ: khi thiếu dữ kiện, nêu giả định rõ, không bịa số.
- Không biến screening thành mini-FS; nếu deal đáng theo đuổi, chuyển tiếp đúng skill.
- Một red flag pháp lý/định giá đủ nghiêm trọng có thể Fail ngay mà không cần chấm hết tiêu chí.

## Verification

- [ ] Đã tóm tắt đủ deal ở mức tối thiểu
- [ ] Đã chấm các nhóm tiêu chí chính
- [ ] Kết luận go/pass/watch rõ ràng + lý do
- [ ] Nếu Proceed, đã nêu câu hỏi/cần dữ kiện cho bước sơ bộ
