---
name: re-full-investment-report
description: Use to build a full (đầy đủ) real-estate investment report and the IC memo — a deeper version of the preliminary report with FS-backed numbers, base/upside/downside cases, risks, and a go/no-go investment recommendation for the investment committee.
version: 1.0.0
license: MIT
---

# RE Full Investment Report + IC Memo (Báo cáo đầu tư đầy đủ)

Báo cáo đầu tư chuyên sâu cuối cùng trong `RE-Investment-Finance`, gắn số từ FS, dùng để trình quyết định đầu tư (Investment Committee). Là bản sâu hơn của `re-preliminary-investment-report`, với phân tích và bằng chứng đầy đủ.

## Khi nào dùng

Dùng khi: deal đã có Báo cáo sơ bộ Go/Conditional và đã chạy FS; cần báo cáo đầy đủ + IC memo để ra quyết định đầu tư; cần recommendation có thesis/cases/conditions cho cấp duyệt.

Không dùng cho: đánh giá sơ bộ (→ `re-preliminary-investment-report`); chỉ dựng model (→ `re-feasibility-study`).

## Cấu trúc

Mở rộng 5 phần của báo cáo sơ bộ, chuyên sâu hơn và gắn số FS:

1. **Thông tin chung & cấu trúc giao dịch** — đầy đủ; tóm tắt phương án cấu trúc (link `deal-structuring-advisor`).
2. **Pháp lý dự án & giao dịch** — kéo `licensing-expert` (dự án) + `legal-counsel` (giao dịch); hiệu lực văn bản kiểm chứng qua `tvpl`; nêu blocker, CP, missing docs.
3. **Phân tích thị trường** — kéo `re-market-research`/`vn-re-research`; comps đầy đủ, định vị, absorption, rủi ro thị trường.
4. **Nghiên cứu khả thi (FS)** — kết quả từ `re-feasibility-study`: TDC, GDV, NPV, IRR dự án & vốn chủ, payback, peak funding, margin; **base/upside/downside** + sensitivity; "what must be true".
5. **Kết luận & khuyến nghị đầu tư** — Go / Conditional / No-Go; thesis; upside/downside; điều kiện tiên quyết; rủi ro chính & mitigation; owners & next steps.

## IC Memo

Đóng gói kết luận thành IC memo dùng template `../../templates/investment-memo.md` (Recommendation, Thesis, Asset & Transaction, Market Evidence, Development & Product, Underwriting Assumptions, Base/Upside/Downside, Legal & Execution Risks, What Must Be True, Conditions, Open Questions). Báo cáo dài dùng `../../templates/full-investment-report.md`.

## Nguyên tắc

- Đọc `deals/<deal-id>/_dossier.md` khi bắt đầu; khi chốt, cập nhật trạng thái giai đoạn, recommendation và conditions vào dossier.
- Mọi con số tài chính tie-out với FS; phân biệt calculated / assumption / external.
- Recommendation phải dựa trên căn cứ đủ mạnh; nếu facts còn thiếu, qualify đúng mức.
- Không trộn legal/market specialist conclusion với phán đoán đầu tư — ghi rõ owner từng phần.
- Qua `re-investment-verification-rules` trước khi chốt.

## Kiểm tra

- [ ] 5 phần đầy đủ + gắn số FS
- [ ] Pháp lý dự án + giao dịch đã kéo specialist; hiệu lực văn bản kiểm chứng qua `tvpl`
- [ ] Base/upside/downside + sensitivity có trong phần FS
- [ ] IC memo có thesis / cases / what-must-be-true / conditions / owners
- [ ] Recommendation go/conditional/no-go rõ + điều kiện + next steps
