---
name: re-project-design
description: Use for real-estate project benchmarks, positioning implications, product and program mix, concept briefs, option comparisons, consultant instructions, and detailed 1/500 planning-indicator calculation and design review.
version: 1.1.0
license: MIT
---

# RE-Project-Design

Specialist project-strategy và design framing cho dự án BĐS, không phải lớp điều phối liên phòng ban. Làm việc ở giao điểm business – market – concept; route integrated investment decisions về `RE-HQ` / `RE-Investment-Finance`.

## Khi nào dùng

Dùng khi: benchmark dự án & product references; positioning & product/program mix; concept brief / consultant brief / option comparison; **tính chỉ tiêu quy hoạch 1/500 (FAR/GFA/NSA/mật độ/dân số/đỗ xe)**; kiểm tra tuân thủ QCVN; rà soát & phản biện hồ sơ thiết kế.

Không dùng cho: thẩm định pháp lý dự án (→ `licensing-expert`); FS tài chính (→ `re-feasibility-study`); area study / comps (→ `re-market-research`); quyết định đầu tư tích hợp (→ `RE-Investment-Finance` / `RE-HQ`).

## Bộ máy & skill đi kèm

- **`design-planning`** là skill specialist của phòng: calc engine + quy trình 9 bước tính chỉ tiêu quy hoạch + kiểm tra tuân thủ QCVN + design review (ĐẠT / RỦI RO / TỐI ƯU). **Load `design-planning`** cho mọi việc tính toán chỉ tiêu hoặc rà hồ sơ thiết kế.
- Template brief: `../../templates/design-brief.md`.
- Cross-link: `re-investment-finance`/`re-feasibility-study` (FS dùng GFA/NSA/product mix), `licensing-expert` (khả năng phê duyệt / điều chỉnh quy hoạch), `tvpl` (hiệu lực QCVN/luật).

## Quy trình

1. Xác nhận business objective, site constraints, target customer, decision stage.
2. Dùng market evidence + benchmark phù hợp, ghi rõ vì sao comparable.
3. Khi cần chỉ tiêu/khối tích → load `design-planning` (9 bước, công thức ở engine reference).
4. Dịch evidence thành product, program, amenity, phasing, design implication.
5. Show options & trade-offs, không trình bày sở thích như sự thật; ≥ 2 phương án.
6. Flag câu hỏi kỹ thuật cần kỹ sư / tư vấn có chứng chỉ.
7. Dùng `../../templates/design-brief.md` cho formal brief; trả integrated investment decisions về `RE-HQ`/`RE-Investment-Finance`.

## Dạng đầu ra

- Concept brief / consultant brief
- Benchmark note
- Product mix summary (gắn chỉ tiêu từ `design-planning`)
- Option comparison memo (≥ 2 phương án)
- Bảng chỉ tiêu quy hoạch + kiểm tra tuân thủ (qua `design-planning`)

## Kiểm tra

- [ ] Business objective / site / target / decision stage rõ
- [ ] Benchmark có lý do comparable
- [ ] Chỉ tiêu quy hoạch (nếu có) đã chạy qua `design-planning` + kiểm tra QCVN
- [ ] ≥ 2 phương án + trade-offs
- [ ] Câu hỏi kỹ thuật cần consultant đã được flag, không giả vờ certify
