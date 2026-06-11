# FS Excel Build Guide — dựng model .xlsx qua skill `xlsx`

Hướng dẫn xuất FS thành file Excel chạy được. Dùng skill `xlsx` (openpyxl) để tạo workbook 7 sheet theo `fs-structure.md`. Mục tiêu: model **assumption-driven**, công thức Excel thật, đổi input là cập nhật toàn bộ.

## Nguyên tắc dựng

1. **Named ranges cho mọi assumption.** Đặt tên ô ở sheet `Assumptions` (vd `gia_ban_canho`, `suat_dau_tu`, `wacc`, `ty_le_no`). Công thức ở các sheet khác tham chiếu tên này, **không** gõ số trực tiếp.
2. **Một chiều phụ thuộc:** Assumptions → Land&CAPEX / Revenue → Financing → Cashflow → Returns → Sensitivity. Không tạo vòng lặp (trừ lãi vốn hóa — nếu cần, bật iterative calc hoặc tính lãi đơn giản hóa và ghi chú).
3. **Định dạng số:** phân tách hàng nghìn, đơn vị nhất quán (triệu hoặc tỷ VND). Tô màu ô input (vd nền vàng) khác ô công thức.
4. **Kỳ thời gian** theo cột (T0, T1, …) ở Cashflow; mỗi dòng chi phí/doanh thu phân bổ bằng công thức theo lịch tiến độ/absorption ở Assumptions.

## Công thức chính (Excel)

- GDV dòng SP: `=so_san_pham * dien_tich_bq * don_gia_ban`
- Hard cost: `=GFA * suat_dau_tu`
- Soft / contingency: `=hard_cost * soft_pct` ; `=(hard_cost+soft_cost)*contingency_pct`
- TDC: `=tien_dat + hard_cost + soft_cost + contingency`
- Net cashflow kỳ i: `=inflow_i - SUM(outflow_i_range)`
- Cumulative: `=cum_{i-1} + net_i`
- **NPV**: `=NPV(wacc, net_cashflow_T1:Tn) + net_cashflow_T0`
- **IRR dự án**: `=IRR(net_cashflow_T0:Tn)` (hoặc `=XIRR(values, dates)` nếu có ngày)
- **IRR vốn chủ**: `=IRR(equity_cashflow_T0:Tn)`
- **Payback**: tìm kỳ đổi dấu cumulative (dùng cột phụ + `MATCH`/`INDEX` hoặc đọc tay).
- **Peak funding**: `=ABS(MIN(cumulative_range))`
- Profit margin: `=loi_nhuan/TDC` và `=loi_nhuan/GDV`

## Sensitivity (Data Table)

- 1 chiều: cột giá trị driver (vd giá bán −10%…+10%) → cột kết quả tham chiếu ô IRR/NPV; dùng Data Table (`What-If`). Nếu openpyxl không dựng được Data Table động, thay bằng **bảng tính sẵn nhiều kịch bản** (mỗi cột là một bộ assumption → IRR/NPV), ghi chú rõ là kịch bản tĩnh.
- 2 chiều: hàng = giá bán, cột = suất đầu tư, ô giao = IRR.
- Đánh dấu **Base / Upside / Downside** trên bảng.

## Lưu ý openpyxl

- openpyxl ghi **công thức** chứ không tự tính giá trị; người mở bằng Excel/LibreOffice sẽ thấy kết quả. Để kiểm tra giá trị trong môi trường headless, có thể tính song song bằng Python để tie-out, nhưng file giao cho Sếp phải giữ **công thức sống**.
- Hàm `IRR`/`NPV` là hàm Excel chuẩn → openpyxl ghi chuỗi `=IRR(...)` là đủ.
- Đặt `data_only=False` khi lưu để giữ công thức.

## Đặt tên file

`FS_<TenDuAn_khong_dau>_<YYYYMMDD>.xlsx`. Lưu ngoài plugin (data workspace), không commit vào repo.
