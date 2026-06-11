# Report Catalog — chọn loại báo cáo, template, vị trí lưu

> Template nằm ở `../../../templates/market-research/`. Vị trí lưu tính từ gốc vault.

| Loại báo cáo | Khi nào dùng | Template | Lưu tại |
|---|---|---|---|
| **Market snapshot** | cần view nhanh 1 trang về một khu/phân khúc | `market-snapshot.md` | `reports/market-analysis/<YYYY>/` |
| **Area study** | nghiên cứu sâu một khu vực (hạ tầng → cung → giá → absorption) | `area-study.md` | `reports/market-analysis/<YYYY>/` |
| **So sánh giá / xếp hạng** | so dự án trong cụm, ranking theo tiêu chí | `price-comparison-ranking.md` | `reports/comparisons/<YYYY>/` |
| **Weekly scan note** | chốt bước 5 của P4 weekly | `weekly-scan.md` | `reports/market-analysis/<YYYY>/weekly/` |
| **Monthly market report** | báo cáo tháng theo khu vực | `monthly-market-report.md` | `reports/market-analysis/<YYYY>/` |
| **Pricing playbook cụm** | khóa cách đọc giá đúng cho một cụm thị trường | `pricing-playbook.md` | `reports/playbooks/` (tài liệu sống) |
| **Field audit report** | chốt P5 rà chất lượng dữ liệu | `field-audit.md` | `reports/field-audits/<YYYY>/` |
| **Phase sheet** | working sheet giá theo phase cho dự án nhóm 2 | `phase-sheet.md` | `reports/comparisons/<YYYY>/phase-sheets/` |

## Quy tắc chung cho mọi báo cáo

- Tên file: `<YYYY-MM-DD>_<ten>.md` (trừ playbook: `<cum>-pricing-playbook.md`).
- Mỗi data point: nguồn + ngày truy cập + price basis + confidence; số mẫu tin khi là listing.
- Phân biệt asking / MBS sơ cấp / chuyển nhượng / khảo sát (theo `pricing-protocol.md`).
- Kết luận phải nói rõ **điều còn bất định**; không over-generalize từ mẫu nhỏ.
- Báo cáo phục vụ deal của Phòng Đầu tư → giao theo finding schema trong `../../../references/operating-contract.md` và lưu thêm bản vào `deals/<deal-id>/analysis/` của data workspace nếu có deal-id.
