---
name: re-preliminary-investment-report
description: Use to build a preliminary (sơ bộ) real-estate investment report for a potential project — general info, project legal status, market analysis, pre-feasibility math, and an investment conclusion (go / conditional / no-go).
version: 1.0.0
license: MIT
---

# RE Preliminary Investment Report (Báo cáo đầu tư sơ bộ)

Đánh giá sơ bộ ban đầu cho một dự án tiềm năng trong `RE-Investment-Finance`, sau khi đã qua sàng lọc (`re-investment-screening`) và trước khi làm FS đầy đủ. Đây là báo cáo **định hướng quyết định theo đuổi**, dựa trên dữ kiện hiện có + giả định có căn cứ.

## Khi nào dùng

Dùng khi: một deal đã Proceed từ screening và cần đánh giá sơ bộ đa chiều; cần go/conditional/no-go view trước khi đầu tư công sức làm FS chi tiết.

Không dùng cho: sàng lọc nhanh (→ `re-investment-screening`); mô hình tài chính chi tiết (→ `re-feasibility-study`); báo cáo chuyên sâu cuối (→ `re-full-investment-report`).

## Cấu trúc 5 phần

### 1. Thông tin chung
Tên dự án, chủ thể/bên bán, vị trí, quy mô đất/GFA, loại hình & product mix dự kiến, giá chào / tổng mức đầu tư ước tính, hình thức giao dịch, mục tiêu đầu tư.

### 2. Pháp lý dự án (kéo `licensing-expert`)
Rà sơ bộ 3 trục trọng yếu cho quyết định đầu tư: **đất đai** (nguồn gốc, loại đất, GCN, thế chấp/tranh chấp), **đầu tư** (chủ trương đầu tư, lựa chọn nhà đầu tư), **quy hoạch** (phù hợp 1/2000–1/500, chỉ tiêu). Kéo `licensing-expert` cho kết luận pháp lý; kiểm chứng hiệu lực văn bản qua `tvpl`. Nêu rõ blocker và missing docs. (Pháp lý giao dịch sâu hơn → `legal-counsel` ở bước structuring/DD.)

### 3. Phân tích thị trường (kéo `re-market-research`)
Cung-cầu khu vực, comps & mặt bằng giá (sơ cấp/thứ cấp), absorption, định vị sản phẩm. Kéo `re-market-research` / `vn-re-research`. Mỗi số liệu có nguồn + ngày + price basis + confidence.

### 4. Nghiên cứu khả thi sơ bộ (pre-FS)
Quick math, chưa cần model đầy đủ:
- chỉ tiêu quy hoạch thô (GFA, NSA, product mix) — có thể kéo `design-planning`;
- doanh thu ước tính = Σ(NSA × đơn giá thị trường từ phần 3);
- chi phí thô: tiền đất + CAPEX xây dựng ước/m² + chi phí mềm;
- biên lợi nhuận / margin thô, payback định hướng.
Đánh dấu rõ giả định; nếu thiếu đơn giá/chi phí, ghi [CẦN BỔ SUNG].

### 5. Kết luận đầu tư
**Go / Conditional Go / No-Go** + luận điểm chính, upside/downside lớn, điều kiện tiên quyết, và **next step** (thường là: làm FS đầy đủ + DD nếu Go/Conditional).

## Output

Dùng template `../../templates/preliminary-investment-report.md`. Qua `re-investment-verification-rules` trước khi chốt.

Đọc `deals/<deal-id>/_dossier.md` khi bắt đầu (kết quả screening, câu hỏi mở); khi chốt, cập nhật dossier: trạng thái giai đoạn, kết luận go/conditional/no-go, assumption mới và findings trọng yếu.

## Nguyên tắc

- Phân biệt fact / inference / assumption (finding schema trong `../../references/operating-contract.md`).
- Không bịa số; thiếu thì giả định có căn cứ + đánh dấu.
- Pháp lý và thị trường là **specialist input** — Investment tổng hợp, không tự kết luận thay specialist.
- Pre-FS là ước lượng định hướng, **không thay FS**; nói rõ giới hạn.

## Kiểm tra

- [ ] Đủ 5 phần; mỗi phần có kết luận sơ bộ, không chỉ liệt kê
- [ ] Pháp lý đã kéo `licensing-expert` + kiểm chứng hiệu lực qua `tvpl` cho điểm trọng yếu
- [ ] Thị trường có nguồn + ngày + confidence
- [ ] Pre-FS nêu rõ giả định và giới hạn
- [ ] Kết luận go/conditional/no-go + điều kiện + next step rõ ràng
