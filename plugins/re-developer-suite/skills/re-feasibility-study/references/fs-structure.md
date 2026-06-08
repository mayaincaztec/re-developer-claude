# FS Structure — Spec chuẩn cho model khả thi BĐS

Nguồn sự thật về cấu trúc FS. 7 sheet, gắn kết qua sheet `Assumptions`. Đơn vị mặc định: VND (triệu hoặc tỷ — chọn nhất quán toàn model), diện tích m², thời gian theo quý hoặc năm.

## Sheet 1 — Assumptions (driver register)

Mỗi dòng: Chỉ tiêu | Giá trị | Đơn vị | Nguồn | Ngày | Confidence. Nhóm:

- **Đất & chỉ tiêu**: diện tích đất, mật độ XD, FAR, GFA, NSA, efficiency% (kéo `design-planning`).
- **Product mix**: theo dòng sản phẩm — số sản phẩm, diện tích bình quân, NSA bán được.
- **Giá bán**: đơn giá bán/m² hoặc /sản phẩm theo dòng (kéo `re-market-research`); escalation %/năm.
- **Chi phí**: tiền sử dụng đất/thuê đất, thuế–phí chuyển nhượng; suất đầu tư xây dựng (hard cost)/m² GFA; chi phí mềm % (thiết kế, PM, tư vấn); chi phí bán hàng & marketing %; dự phòng (contingency) %.
- **Tài chính**: tỷ lệ vốn chủ/vay, lãi suất vay, lịch giải ngân, lãi vốn hóa trong xây dựng; discount rate (WACC).
- **Tiến độ & absorption**: mốc bắt đầu/kết thúc từng giai đoạn; lịch hấp thụ doanh số (% theo kỳ); lịch thu tiền theo hợp đồng (payment schedule).

## Sheet 2 — Land & CAPEX

- Tiền đất = tiền SDĐ/thuê đất + thuế/phí + chi phí GPMB (nếu có).
- Hard cost = GFA × suất đầu tư/m² (tách theo hạng mục nếu cần: phần thân, hầm, hạ tầng, cảnh quan).
- Soft cost = % × hard cost (thiết kế, PM, tư vấn, phê duyệt).
- Marketing & bán hàng = % × doanh thu (đưa vào ở Revenue/Cashflow).
- Contingency = % × (hard + soft).
- **Total Development Cost (TDC)** = đất + hard + soft + contingency (chưa gồm lãi vay; lãi tính ở Financing).

## Sheet 3 — Revenue

- Theo từng dòng sản phẩm: Số sản phẩm × Diện tích × Đơn giá = Gross Development Value (GDV) dòng đó.
- Tổng **GDV** = Σ các dòng.
- Trừ chiết khấu/khuyến mãi (nếu có) → doanh thu thuần.
- Phân bổ theo **absorption schedule** ra từng kỳ; thu tiền theo **payment schedule** (không đồng nhất ký HĐ với thu tiền).

## Sheet 4 — Financing

- Nhu cầu vốn theo kỳ (từ Cashflow trước lãi).
- Equity vs Debt theo tỷ lệ giả định; lịch giải ngân vay.
- Lãi vay trong thời gian xây dựng → **vốn hóa** (cộng vào chi phí) hoặc tính vào dòng tiền tùy quy ước; ghi rõ.
- Lịch trả gốc/lãi.

## Sheet 5 — Cashflow (theo kỳ: quý hoặc năm)

| Dòng | Công thức |
|---|---|
| Inflow: thu tiền bán | từ Revenue × payment schedule |
| Outflow: tiền đất | Sheet 2, theo mốc thanh toán |
| Outflow: hard + soft + contingency | Sheet 2, phân bổ theo tiến độ xây dựng |
| Outflow: marketing & bán hàng | % doanh thu, theo kỳ bán |
| Outflow: lãi vay | Sheet 4 |
| Outflow: thuế (TNDN…) | theo quy ước, áp lên lợi nhuận |
| **Net cashflow** | Inflow − Σ Outflow |
| **Cumulative cashflow** | luỹ kế |

## Sheet 6 — Returns

- **NPV** = `=NPV(WACC, dải net cashflow các kỳ)` (+ kỳ 0 nếu có outflow ngay).
- **IRR dự án** = `=IRR(dải net cashflow)` (project-level, trước tài trợ vốn chủ).
- **IRR vốn chủ** = `=IRR(dải dòng tiền vốn chủ)` (sau nợ).
- **Payback** = kỳ cumulative đổi dấu sang dương.
- **Profit margin** = Lợi nhuận / TDC và Lợi nhuận / GDV.
- **Peak funding** = |min(cumulative cashflow)| — nhu cầu vốn đỉnh.

## Sheet 7 — Sensitivity

- Bảng 1 chiều: return (IRR/NPV) theo từng driver: đơn giá bán ±, suất đầu tư ±, tốc độ absorption ±, lãi suất ±, WACC ±.
- Bảng 2 chiều (Data Table): vd IRR theo (đơn giá bán × suất đầu tư xây dựng).
- Nêu rõ **base / upside / downside** tương ứng các kịch bản giá–chi phí–tiến độ.
