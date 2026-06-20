# LOI & Offer Guide — từ FS sang đề nghị giao dịch

Hướng dẫn dựng offer và LOI (Letter of Intent / Biên bản ghi nhớ) cho thương vụ BĐS, gắn với kết quả FS. Dùng cùng `re-inv-deal-structuring` và `../../../templates/loi.md`.

## Từ FS sang giá offer

- **Giá trần** = mức giá mà tại đó dự án vẫn đạt return tối thiểu (hurdle IRR/NPV ≥ 0 ở WACC) trong FS.
- **Giá offer** = giá trần − biên an toàn (rủi ro thực thi, downside case, chi phí DD/structuring chưa lường hết).
- Đối chiếu với **peak funding** để chắc cấu trúc vốn chịu được.
- Nêu rõ offer dựa trên **assumption nào** (giá bán, suất đầu tư, absorption) — offer là điều kiện theo các giả định đó.

## Cấu phần một offer

- Giá đề nghị + cơ sở định giá (tham chiếu FS).
- **Payment structure**: đặt cọc, các đợt theo mốc (signing, điều kiện pháp lý hoàn tất, closing).
- **Điều kiện tiên quyết (CP)**: DD thỏa mãn, phê duyệt nội bộ/IC, điều kiện pháp lý dự án (kéo `re-legal-licensing`), consents/approvals.
- **Exclusivity**: thời hạn độc quyền đàm phán.
- **Timeline**: từ LOI → DD → definitive agreement → closing.

## LOI — lưu ý then chốt

- **Ràng buộc / không ràng buộc:** phần lớn LOI là *không ràng buộc* về nghĩa vụ giao dịch, nhưng thường có một số điều khoản *ràng buộc*: bảo mật (NDA), exclusivity, chi phí, governing law/dispute. Phải tách rõ — đây là rủi ro pháp lý lớn nhất của LOI.
- Nêu rõ LOI **không thay** definitive agreement (SPA/SHA…); ký LOI không tạo nghĩa vụ mua/bán trừ phần ràng buộc.
- Điều kiện chấm dứt / hết hạn LOI.
- **Kéo `re-legal-counsel`** rà ngôn ngữ ràng buộc, exclusivity, CP và governing law trước khi phát hành.
- Nếu cấu trúc là share/asset/JV khác nhau → LOI phải phản ánh đúng đối tượng giao dịch và điều kiện pháp lý dự án (kéo `re-legal-licensing` cho điều kiện chuyển nhượng).

## Checklist trước khi phát hành LOI

- [ ] Giá offer truy được về FS (giả định nêu rõ)
- [ ] Payment structure + CP + exclusivity + timeline đầy đủ
- [ ] Đã tách phần ràng buộc / không ràng buộc
- [ ] `re-legal-counsel` đã rà ngôn ngữ pháp lý
- [ ] Điều kiện pháp lý dự án (chuyển nhượng…) đã xác nhận với `re-legal-licensing`
