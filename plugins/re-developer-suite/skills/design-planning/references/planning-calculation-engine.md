# Planning Calculation Engine — công thức & bảng tra chỉ tiêu quy hoạch

Bộ máy tính toán cho `design-planning`. Mọi con số phải có nguồn (QCVN/TCVN/giả định có căn cứ/thị trường).

## Thuật ngữ & công thức nền tảng

- `S_total` = tổng diện tích đất dự án (m²/ha) — đầu vào
- `S_lot` = diện tích lô đất xây dựng — đầu vào hoặc tính từ cơ cấu
- `D` (Density) = mật độ xây dựng (%) = (S_footprint / S_lot) × 100
- `S_footprint` = diện tích chiếm đất = D × S_lot / 100
- `H` = tầng cao (số tầng) — đầu vào; `H_m` = chiều cao (m) = tổng chiều cao từng tầng từ cos ±0.00
- `FAR` (hệ số SDĐ) = GFA_above / S_lot (lần)
- `GFA` = tổng diện tích sàn xây dựng = tổng DT sàn tất cả các tầng
- `GFA_above` = S_footprint × H (ước lượng nhanh) hoặc Σ DT sàn từng tầng
- `GFA_basement` = DT sàn hầm × số tầng hầm; `GFA_total` = GFA_above + GFA_basement
- `NSA` = diện tích sàn sử dụng ròng = GFA_above × Efficiency%
- `Pop` (dân số) = Σ căn hộ × hệ số nhân khẩu
- `n_units` = NSA_residential / S_avg_unit
- `S_parking` = Parking_car × 30 + Parking_moto × 3.5 (m², gồm lối đi)

**Lưu ý FAR (QCVN 01:2021/BXD):** FAR = tổng DT sàn trên mặt đất / DT lô; tầng hầm thường KHÔNG tính FAR trừ khi 1/2000 ghi rõ; tầng kỹ thuật/áp mái tùy định nghĩa; mái che không tính nếu bao che < 50% chu vi.

## Bảng hệ số hiệu suất sàn (Efficiency Rate)

| Loại hình | Efficiency |
|---|---|
| Chung cư cao cấp | 70–75% |
| Chung cư trung cấp | 72–78% |
| Chung cư bình dân | 75–82% |
| Officetel / Soho | 65–72% |
| Văn phòng Grade A | 65–70% |
| Văn phòng Grade B/C | 70–75% |
| TTTM / Retail podium | 55–65% |
| Khách sạn 4–5 sao | 55–65% |
| Condotel / Serviced Apt | 60–70% |
| Bệnh viện | 55–65% |
| Trường học | 60–70% |
| Biệt thự / Townhouse | 85–92% |
| Shophouse | 80–88% |
| Nhà xưởng / Kho | 85–92% |

## Chiều cao tầng điển hình (tính H_m)

Hầm đỗ xe 3.0–3.3m; trệt thương mại/lobby 4.5–6.0m; TMDV (podium) 4.2–5.5m; căn hộ CC 3.0–3.3m (thông thủy 2.7–3.0m); căn hộ cao cấp/penthouse 3.3–3.6m; văn phòng 3.5–4.0m; khách sạn 3.2–3.6m; kỹ thuật/refuge 3.0–4.0m; mái/áp mái 2.5–3.5m.

## Mật độ xây dựng tối đa tham chiếu (QCVN 01:2021/BXD)

- Nhà ở liền kề ≤ 90%; Biệt thự ≤ 50%.
- Chung cư ≤ 5 tầng: lô <3.000m² ≤60%; 3.000–10.000m² ≤55%; >10.000m² ≤50%.
- Chung cư 6–19 tầng: <3.000m² ≤50%; 3.000–10.000m² ≤45%; >10.000m² ≤40%.
- Chung cư ≥ 20 tầng: <3.000m² ≤45%; 3.000–10.000m² ≤40%; >10.000m² ≤35%.
- Công trình TMDV: <3.000m² ≤70%; 3.000–10.000m² ≤60%; >10.000m² ≤50%.
- Hỗn hợp: áp theo chức năng chính.

> Đây là tham chiếu chung. Nếu có chỉ tiêu 1/2000 cụ thể → ưu tiên dùng chỉ tiêu đó.

## Khoảng lùi công trình (setback) tham chiếu

| Lộ giới | ≤19 tầng | ≥20 tầng |
|---|---|---|
| <19m | ≥3m | ≥6m |
| 19–22m | ≥4m | ≥6m |
| 22–28m | ≥5m | ≥7m |
| >28m | ≥6m | ≥8m |

## Hệ số nhân khẩu

Studio/1PN 1.5–2.0 người/căn; 2PN 2.5–3.0; 3PN 3.5–4.0; biệt thự/townhouse 4.0–5.0.

## Nhu cầu hạ tầng xã hội (QCVN 01:2021/BXD)

- Mầm non: 50 chỗ/1.000 dân, 25–30 m² đất/chỗ
- Tiểu học: 65 chỗ/1.000 dân, 15–20 m² đất/chỗ
- THCS: 55 chỗ/1.000 dân, 15–20 m² đất/chỗ
- Trạm y tế: 1/10.000–15.000 dân
- Cây xanh công cộng cấp đơn vị ở ≥ 2 m²/người; cấp khu ở ≥ 1 m²/người (bổ sung)

## Ratio đỗ xe tham chiếu

- CC cao cấp/hạng sang (nội đô HCM/HN): ô tô 0.3–0.7 chỗ/căn, xe máy 1.0–1.5
- CC trung cấp: ô tô 0.15–0.3, xe máy 1.0–1.5
- CC bình dân: ô tô 0.1–0.2, xe máy 1.0–2.0
- Văn phòng: ô tô 1 chỗ/100–200m² GFA, xe máy 1 chỗ/30–50m² GFA
- TTTM: ô tô 1 chỗ/50–100m² GFA, xe máy 1 chỗ/20–30m² GFA
- Khách sạn: ô tô 0.2–0.5 chỗ/phòng

## Cơ cấu sử dụng đất tham chiếu (khu đô thị mới)

- Đất đơn vị ở 50–60% (đất xây nhà ở thường 30–50% tổng)
- Đất công trình dịch vụ đô thị cấp đơn vị ở 5–8%
- Đất cây xanh ≥ 2 m²/người cấp đơn vị ở
- Đất giao thông 18–26%
- Đất hạ tầng kỹ thuật 1–3%

## Công thức bước 6 (đỗ xe & hầm)

`Parking_car = n_units × ratio_car` ; `Parking_moto = n_units × ratio_moto` ; `S_parking = Parking_car × 30 + Parking_moto × 3.5` ; `N_tầng_hầm = ROUNDUP(S_parking / S_footprint_hầm)`.

## Công thức bước 8 (tối ưu)

`FAR_dư = FAR_max − FAR_tính` ; `GFA có thể thêm = FAR_dư × S_lot`. Nếu FAR < FAR_max → đề xuất tăng H hoặc D. Nếu D > D_max → giảm D tăng H.
