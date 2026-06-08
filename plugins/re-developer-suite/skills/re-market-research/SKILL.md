---
name: re-market-research
description: Use for Vietnam real-estate area studies, project and competitor scans, comparable pricing, supply-demand, launch pipeline, absorption observations, and market thesis development.
version: 1.1.0
license: MIT
---

# RE-Market-Research

Specialist market-research execution cho thị trường BĐS Việt Nam, không phải lớp điều phối liên phòng ban. Khi task chuyển thành tổng hợp đa phòng ban hoặc ra quyết định đầu tư tích hợp, route về `RE-HQ`.

## When to Use

Dùng khi trọng tâm là: area study / khu vực; comps & pricing; supply-demand & pipeline mở bán; competitor / project scan; absorption observation; xây dựng market thesis từ dữ liệu công khai.

Do not use for: underwriting / IRR (→ `RE-Investment-Finance`); legal status / pháp lý dự án (→ `RE-Legal`); product mix / concept (→ `RE-Project-Design`); tổng hợp đa phòng ban (→ `RE-HQ`).

## Engine & companion

- **`vn-re-research`** là engine vận hành của phòng này: quản lý database dự án BĐS VN có cấu trúc, scan giá thứ cấp (batdongsan.com.vn qua Claude in Chrome), và sinh báo cáo thị trường theo 4 protocol (thêm dự án / cập nhật giá / báo cáo / weekly scan). **Mặc định load `vn-re-research`** khi task liên quan database, scan giá hoặc báo cáo định kỳ.
- Template comparable: `../../templates/market-comp-table.md`.
- Browser: ưu tiên Claude in Chrome (`mcp__Claude_in_Chrome__*`) cho site BĐS VN có anti-bot; fallback WebFetch / WebSearch.

## Workflow

1. Define geography, asset class, customer, period và decision to support.
2. Search official developer và government sources first, then reputable research và listing sources.
3. Record URL, access date, observation date, price basis, sample size và confidence cho từng data point.
4. Distinguish asking price, primary offer, incentive-adjusted price và transacted price — không trộn 4 loại giá này.
5. Treat snippets và isolated listings as indicative only; ghi rõ số mẫu tin đã đọc.
6. Separate fact, inference và assumption (theo finding schema trong `operating-contract.md`).
7. Dùng `../../templates/market-comp-table.md` cho bảng dự án so sánh.
8. Explain implications và remaining uncertainty; không biến một mẫu nhỏ thành kết luận toàn thị trường.

## Output shapes

- **Market snapshot** — tóm tắt cung-cầu, giá, pipeline + nhận định ngắn.
- **Comparable table** — theo template, mỗi dòng có price basis + source + access date + confidence.
- **Area / sector study** — bối cảnh, comps, xu hướng, hệ quả cho quyết định.
- **Market thesis** — luận điểm + bằng chứng + rủi ro / điểm còn bất định.

## Verification checklist

- [ ] Đã nêu rõ geography / asset class / period / decision to support
- [ ] Mỗi data point có source + access date + price basis + confidence
- [ ] Đã phân biệt asking / primary / incentive-adjusted / transacted price
- [ ] Sample size được nêu; không over-generalize từ mẫu nhỏ
- [ ] Đã tách fact / inference / assumption
- [ ] Giá MBS (sơ cấp CĐT) không bị trộn với giá thứ cấp thị trường
- [ ] Nếu task đã thành tổng hợp đa phòng ban, đã route `RE-HQ`

## Common pitfalls

1. Trộn giá rao bán với giá giao dịch thực.
2. Lấy 1–2 listing làm kết luận toàn thị trường.
3. Không ghi access date → dữ liệu nhanh lỗi thời mà không biết.
4. Dùng WebFetch cho batdongsan rồi báo "không lấy được" thay vì thử Claude in Chrome.
5. Ôm phần underwriting / IRR đáng ra thuộc `RE-Investment-Finance`.
