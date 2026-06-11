---
name: re-inv-feasibility-study
description: Use to build a feasibility study (FS) for a real-estate project — an assumption-driven financial model covering land and CAPEX, revenue from product mix, financing, phased cashflow, returns (NPV/IRR/payback), and sensitivity. Produces both a markdown spec and a working Excel (.xlsx) model.
version: 1.0.0
license: MIT
---

# RE Feasibility Study (FS)

Dựng nghiên cứu khả thi tài chính cho dự án BĐS trong `RE-Investment-Finance`. Deliverable gồm **(a)** model Excel `.xlsx` chạy được và **(b)** cấu trúc/spec chuẩn để tái lập. FS gắn số cho Báo cáo đầu tư đầy đủ và làm nền cho structuring/LOI.

## Khi nào dùng

Dùng khi: cần model tài chính dự án (đất + CAPEX + doanh thu + dòng tiền + return); cần NPV/IRR/payback + sensitivity; cần con số cho IC memo hoặc offer/LOI.

Không dùng cho: ước lượng định hướng nhanh (→ phần pre-FS trong `re-inv-preliminary-report`); chỉ tiêu quy hoạch (→ `re-project-design-planning`).

## Tài liệu kèm

- `references/fs-structure.md` — spec chuẩn các sheet, dòng, công thức (nguồn sự thật của cấu trúc FS).
- `references/fs-excel-build-guide.md` — hướng dẫn dựng `.xlsx` thật qua skill `xlsx` (named ranges, công thức NPV/IRR, data table sensitivity).

## Điều kiện tiên quyết (để sinh .xlsx)

Việc xuất file `.xlsx` cần skill `xlsx` (dùng `openpyxl`). Nếu môi trường chưa có `openpyxl`, skill `xlsx` sẽ tự xử lý khi được gọi; nếu không cài được, vẫn có thể giao FS ở dạng spec/bảng theo `references/fs-structure.md` và nêu rõ chưa xuất được Excel. Không hardcode số — luôn giữ công thức sống trong file.

## Quy trình

### Bước 1 — Chốt assumption register
Mọi driver phải có **source / date / owner / confidence**. Tối thiểu: diện tích đất & chỉ tiêu (GFA/NSA — có thể kéo `re-project-design-planning`), product mix & số sản phẩm, đơn giá bán (kéo `re-rnd`), suất đầu tư xây dựng/m², chi phí mềm %, tiền đất & thuế/phí, lịch tiến độ & absorption, cấu trúc vốn (equity/debt, lãi suất, giải ngân), discount rate (WACC), escalation.

### Bước 2 — Dựng model theo `references/fs-structure.md`
7 sheet: Assumptions → Land & CAPEX → Revenue → Financing → Cashflow → Returns → Sensitivity. **Công thức Excel thật**, tham chiếu ô từ sheet Assumptions; không hardcode số vào công thức.

### Bước 3 — Sinh file .xlsx
Theo `references/fs-excel-build-guide.md`, dùng skill `xlsx` để xuất file. Đặt tên chuyên nghiệp (vd `FS_<TenDuAn>_<YYYYMMDD>.xlsx`).

### Bước 4 — Tie-out & đọc kết quả
Kiểm tra: balance dòng tiền (cumulative cuối khớp tổng profit), NPV/IRR tính ra hợp lý, peak funding khớp cấu trúc vốn. Đọc kết quả thành kết luận: return vs hurdle, độ nhạy lớn nhất nằm ở driver nào.

### Bước 5 — QC
Qua `re-inv-verification-rules`: không bịa số, phân biệt calculated/assumption/external, base/upside/downside có trong sensitivity, what-must-be-true rõ.

## Output

- File `.xlsx` (7 sheet) + 1 trang tóm tắt return (NPV, IRR dự án & vốn chủ, payback, margin, peak funding) + 2–3 dòng kết luận khả thi.
- Lưu file theo `../../references/workspace-layout.md` (`deals/<deal-id>/analysis/FS_<TenDuAn>_<YYYYMMDD>.xlsx`); cập nhật `_dossier.md`: trạng thái FS, return chính và assumption register đã chốt.

## Nguyên tắc

- Assumption-driven: đổi 1 ô ở Assumptions là cả model cập nhật.
- Phân biệt rõ **calculated output** (NPV/IRR…) với **management assumption** (giá bán, suất đầu tư) và **external evidence** (comps, tiền đất).
- Thiếu dữ kiện → giả định bảo thủ + đánh dấu, không bỏ trống âm thầm.
- FS là model giả định, không phải cam kết; nêu rõ giới hạn và ngày dữ liệu.

## Kiểm tra

- [ ] Assumption register đủ source/date/owner/confidence
- [ ] Công thức tham chiếu Assumptions, không hardcode
- [ ] Dòng tiền tie-out; NPV/IRR/payback/peak-funding hợp lý
- [ ] Sensitivity ≥1 chiều cho driver trọng yếu (giá bán, suất đầu tư, absorption)
- [ ] File .xlsx tồn tại, mở được, công thức tính đúng
