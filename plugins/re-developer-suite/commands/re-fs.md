---
description: Dựng feasibility study (FS) — model Excel .xlsx với NPV/IRR/payback/sensitivity cho một dự án BĐS
argument-hint: [deal-id hoặc tên dự án]
---

Dùng skill `re-feasibility-study` (RE Developer Suite) để dựng FS cho: $ARGUMENTS

- Đọc `deals/<deal-id>/_dossier.md` trước nếu có (assumption đã chốt, kết quả báo cáo sơ bộ).
- Chốt assumption register (source/date/owner/confidence) trước khi dựng model; kéo `design-planning` cho GFA/NSA và `re-market-research` cho đơn giá nếu thiếu.
- Dựng model 7 sheet theo spec fs-structure trong references của skill `re-feasibility-study`, xuất `.xlsx` vào `deals/<deal-id>/analysis/`.
- Tie-out, chạy `re-investment-verification-rules`, rồi cập nhật dossier.
