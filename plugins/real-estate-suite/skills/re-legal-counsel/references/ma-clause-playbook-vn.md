> **Lưu ý kiểm chứng:** Mọi điều luật, ngưỡng, thẩm quyền phải được kiểm tra lại hiệu lực qua MCP `legal` (`../../../references/legal-lookup-protocol.md`) tại ngày sử dụng — đặc biệt các văn bản 2025 (LDN sửa đổi, Luật Đầu tư 2025, mô hình CQĐP 2 cấp) có thể tiếp tục thay đổi.

# M&A Clause Playbook — căn cứ pháp lý Việt Nam

> Bổ trợ cho `re-legal-counsel` Mode 1 (review) và Mode 2 (drafting) khi hợp đồng là **SPA/SHA M&A**. Đi cùng `ma-document-guides.md` (chuẩn thị trường US/ABA, Delaware/SIAC — dùng để biết "thị trường đang ở đâu") và `transaction-clause-checklists.md` (rà nhanh dạng tabular). File này trả lời câu hỏi khác: **điều khoản kiểu Anh-Mỹ đó có đứng vững dưới luật Việt Nam không, và nếu viết lại thì bám vào điều luật nào.**
>
> **Nguồn gốc:** đúc kết từ *"Bẫy trong điều khoản hợp đồng"* (Herman, Henry & Dominic, ấn bản 2026, lưu hành nội bộ & chia sẻ cộng đồng) — Chương 21 (M&A và đầu tư, 10 case) + Chương 2 (phương pháp đọc/soát). Toàn văn case gốc (điều khoản mẫu đầy đủ, tình huống tranh chấp VIAC thực tế, bản viết lại chú thích) nằm tại `assets/re-legal-counsel/Herman, Henry & Dominic _So tay hanh nghe - Bay trong dieu khoan hop dong.md` — mở file đó khi cần **nguyên văn điều khoản để soạn thảo**, file này chỉ tóm lược để tra nhanh khi review.

## Nguyên tắc nền khi Anh-Mỹ hoá gặp luật Việt Nam

Phần lớn SPA/SHA tại Việt Nam là **template Anh-Mỹ dịch sang tiếng Việt** mà không hiệu chỉnh khái niệm. Rủi ro gốc: "warranty", "indemnification", "escrow", "MAC" **không có ánh xạ trực tiếp trong BLDS 2015** — dùng nguyên xi làm nền tranh cãi về "tính chất pháp lý" khi ra trọng tài/tòa. Quy tắc chung: **dịch sang khái niệm BLDS** (cam kết/tuyên bố, bồi thường thiệt hại do vi phạm nghĩa vụ...) và **định lượng mọi ngưỡng** ("trọng yếu", "hợp lý" → số cụ thể) trước khi ký.

## 1. Reps & Warranties (R&W)
- **Bẫy:** giữ nguyên "warranty" tiếng Anh; "material"/"best knowledge" không định lượng.
- **Căn cứ VN:** Điều 385, 404 (giải thích hợp đồng — contra proferentem k.6), 419 BLDS 2015; Điều 4, 127 LDN 2020.
- **Bắt buộc có:** dùng "cam kết và tuyên bố" thay "warranty"; Phụ lục Loại Trừ (Disclosure Schedule); định nghĩa "Hiểu biết" gắn Knowledge Group cụ thể; "Trọng yếu" có ngưỡng số (đơn lẻ + cộng dồn).
- **Checklist nhanh:** đủ 9 nhóm R&W (pháp lý/tài chính/thuế/lao động/IP/tài sản/HĐ quan trọng/tuân thủ/tranh chấp)? có Phụ lục Loại Trừ + Knowledge Group? "material"/"MAC" định lượng? có survival period?

## 2. Indemnification
- **Bẫy:** không giới hạn (uncapped, unlimited duration) — rủi ro cả 2 bên; thiếu De minimis/Basket khiến claim nhỏ tốn kém.
- **Căn cứ VN:** Điều 419, 13, 360 BLDS (bồi thường thiệt hại do vi phạm nghĩa vụ — đây là cơ sở pháp lý cho "indemnification", không phải khái niệm riêng); Điều 429 (thời hiệu khởi kiện 3 năm — Survival Period là thỏa thuận điều kiện thực hiện quyền, khác thời hiệu); Luật Quản lý Thuế 2019 (thời hiệu truy thu thuế tới 10 năm → R&W thuế phải survival dài hơn R&W chung).
- **Bắt buộc có:** De minimis (mỗi claim) · Basket/tipping basket (cộng dồn) · Cap riêng cho R&W thường/cơ bản/thuế · Survival Period lệch theo loại R&W · quy trình Notice of Claim (thời hạn phản hồi) · thứ tự thanh toán (Escrow trước, tài sản Bên Bán sau).
- Đối chiếu benchmark US: xem `ma-document-guides.md §1 Indemnification Market Benchmarks` — nhưng **luôn khớp lại với thời hiệu thuế VN** trước khi chốt Cap/Survival.

## 3. MAC (Material Adverse Change)
- **Bẫy:** không định nghĩa/không ngưỡng — tranh chấp mất 12–24 tháng vì mỗi bên tự diễn giải (case thực: dịch COVID có phải MAC không — VIAC mất 18 tháng).
- **Căn cứ VN:** Điều 404 (giải thích hợp đồng khi không định nghĩa rõ), Điều 423 (huỷ bỏ hợp đồng — MAC là "điều kiện không closing", khác căn cứ huỷ bỏ, phải tách rõ trong hợp đồng); án lệ Delaware (IBP v. Tyson, Akorn v. Fresenius) chỉ tham khảo, không phải nguồn luật VN.
- **Bắt buộc có:** ngưỡng định lượng theo từng loại sự kiện (doanh thu/EBITDA/khách hàng/nhân sự cấp cao/pháp lý/tài sản/giấy phép) + carve-outs rõ (kinh tế chung, pandemic, thay đổi luật, hành vi Bên Mua, công bố giao dịch) + quyền lựa chọn khi MAC xảy ra (walk-away / điều chỉnh giá / closing có indemnification bổ sung) + giới hạn thời gian viện dẫn (chỉ giữa Ký Kết và Closing).
- Đối chiếu carve-out chuẩn US: `ma-document-guides.md §3 MAC/MAE Carve-outs`.

## 4. Earn-out
- **Bẫy:** metric dễ thao túng (Bên Mua nắm quyền điều hành sau Closing có thể chuyển doanh thu, đổi cách ghi nhận) — case thực: mất 100% earn-out do bị thao túng, đòi lại chỉ được ~50%.
- **Căn cứ VN:** Điều 3 BLDS (thiện chí — khó chứng minh một mình); **Điều 120.2 BLDS — mấu chốt:** nếu một bên **cố ý cản trở** điều kiện xảy ra thì coi như điều kiện đã xảy ra (áp dụng buộc Earn-out Target coi như đạt 100% khi Bên Mua cố ý cản trở); Điều 420 (hoàn cảnh thay đổi cơ bản khi tái cấu trúc lớn).
- **Bắt buộc có:** metric khó thao túng (EBITDA điều chỉnh, loại trừ giao dịch liên kết) · quyền audit độc lập (Big 4/tương đương) + cơ chế chia phí · cam kết vận hành thiện chí + không sáp nhập/chuyển doanh thu trong giai đoạn earn-out · cơ chế catch-up · dẫn chiếu Điều 120.2 khi cố ý cản trở.

## 5. Escrow
- **Bẫy:** Việt Nam **chưa có Escrow Agent chuyên nghiệp phổ biến** như Mỹ/Singapore — bê nguyên cấu trúc Mỹ vào SPA VN dễ vướng khi thực thi (ngân hàng VN thường đòi văn bản đồng thuận 2 bên mới giải toả, chậm).
- **Căn cứ VN:** không có khái niệm "escrow" trực tiếp trong BLDS; Luật Các TCTD 2024 (dịch vụ tài khoản phong toả); NĐ 21/2021/NĐ-CP (biện pháp bảo đảm); Pháp lệnh Ngoại hối (nếu escrow ở nước ngoài).
- **3 phương án thay thế thực tế tại VN:** (a) tài khoản phong toả 3 bên tại ngân hàng VN — đơn giản nhưng giải toả có thể chậm; (b) **Bảo lãnh ngân hàng on-demand** — Bên Bán nhận 100% ngay, chi phí bảo lãnh 0.5–2%/năm — thường thực tế hơn tại VN; (c) escrow nước ngoài (SG/HK) — vướng đăng ký ngoại hối.
- **Bắt buộc có:** cơ chế giải toả rõ 3 nhánh (đồng ý/phản đối có lý do/không phản hồi) · giải toả định kỳ giữa kỳ (giảm rủi ro bị giữ tiền lâu) · quyền chuyển đổi Escrow ↔ Bảo lãnh ngân hàng.
- Đối chiếu kiến trúc 2-pool (adjustment vs indemnification): `ma-document-guides.md §10 Escrow Architecture`.

## 6. Drag-along / Tag-along
- **Bẫy:** Power of Attorney trong SHA để cổ đông lớn ký thay cổ đông nhỏ khi Drag-along bị từ chối — **có thể bị thu hồi** theo Điều 569 BLDS (đơn phương chấm dứt uỷ quyền) nếu không cấu trúc chặt.
- **Căn cứ VN:** Điều 127, 24, 115–117 LDN 2020 (SHA phải phù hợp Điều lệ — hạn chế chuyển nhượng chỉ có hiệu lực nếu ghi trong Điều lệ); Điều 138, 562–569 BLDS (uỷ quyền); Điều 569 (rủi ro thu hồi uỷ quyền — cần "uỷ quyền không huỷ ngang" có cơ sở).
- **Bắt buộc có:** điều kiện kích hoạt Drag-along cụ thể (ngưỡng % cổ đông lớn, giá ≥ giá tham chiếu định giá độc lập ≤12 tháng, bên mua 100%, không phải đối thủ cạnh tranh) · phân chia giá theo loại cổ phần nếu có cổ phần ưu đãi · POA có cam kết không thu hồi + bồi thường nếu bị thu hồi · loại trừ chuyển nhượng nội bộ/thừa kế · cam kết cập nhật Điều lệ khớp SHA.

## 7. ROFR / ROFO
- **Bẫy:** nhầm ROFR (chỉ được chấp nhận/từ chối theo đúng giá bên thứ ba) với ROFO (đàm phán giá trước, chưa có offer ngoài) — case thực: cổ đông "đàm phán lại giá" bị trọng tài coi là đã từ chối ROFR.
- **Căn cứ VN:** Điều 127 LDN 2020 (hạn chế chuyển nhượng theo Điều lệ); Điều 52 LDN 2020 (công ty TNHH — ưu tiên mua cho thành viên hiện hữu, gần với ROFR theo thiết kế luật); Điều 404 k.6 (contra proferentem khi tranh chấp phạm vi).
- **Bắt buộc có:** ghi rõ ROFR chỉ cho quyền "chấp nhận cùng điều kiện hoặc từ chối" — không có quyền đàm phán · thời hạn quyết định (30 ngày) · fallback rõ khi từ chối (thời hạn bán ra ngoài, ROFR áp lại nếu điều kiện đổi) · tương tác với Drag-along (ROFR thường bị loại trừ khi Drag-along kích hoạt).

## 8. Non-compete với cổ đông cũ/founder sau M&A
- **Điểm khác biệt quan trọng:** Non-compete **trong M&A** (bảo vệ giá trị đã trả cho founder) có cơ sở pháp lý **vững hơn hẳn** Non-compete trong hợp đồng lao động (thường bị toà tuyên vô hiệu/thu hẹp — xem case tương ứng trong sổ tay Ch.16 §6). Đừng áp cùng một chuẩn khắt khe.
- **Căn cứ VN:** Điều 3 BLDS (tự do giao kết); Điều 33 Hiến pháp 2013 (giới hạn — phạm vi phải tương xứng, không vi hiến); Điều 419 (bồi thường tương xứng thiệt hại thực tế — liquidated damages quá cao dễ bị giảm, case thực: đòi 80 tỷ bị giảm còn 30 tỷ).
- **Phạm vi hợp lý:** thời hạn 1–3 năm (5 năm chấp nhận được với giao dịch lớn/founder vai trò quyết định; >5 năm khó công nhận) · lãnh thổ = nơi Target thực sự hoạt động · ngành = ngành chính của Target · đối tượng mở rộng: founder + Bên Liên Quan (vợ/chồng, công ty kiểm soát).
- **Bắt buộc có:** ghi rõ giá trị Non-compete đã tính vào Giá Giao Dịch (consideration) · loại trừ đầu tư tài chính thụ động ≤5% · liquidated damages tương xứng (đừng đặt quá cao — dễ bị hội đồng trọng tài giảm) · quyền yêu cầu biện pháp khẩn cấp tạm thời + specific performance.

## 9. Conditions Precedent (CP) gắn phê duyệt nhà nước
- **Bẫy:** "mọi phê duyệt cần thiết" mơ hồ, không Long Stop Date → giao dịch **treo vô thời hạn** (case thực: 14 tháng chờ Bộ Y Tế phê duyệt, cuối cùng phải đàm phán lại giảm giá 10%).
- **Căn cứ VN:** Điều 120 BLDS (giao dịch có điều kiện — k.2 "deemed satisfaction/deemed failure" khi một bên cố ý cản trở/thúc đẩy); Luật Đầu tư 2025 (thủ tục thay đổi nhà đầu tư, ngưỡng phê duyệt); Luật Cạnh tranh 2018 (ngưỡng thông báo tập trung kinh tế cho Cục CT&BVNTD); Điều 26 LDN 2020 (đăng ký thay đổi sau M&A).
- **Danh mục CP cần liệt kê cụ thể (không viết chung chung):** phê duyệt Sở Tài chính (đổi nhà đầu tư/đăng ký KD) · thông báo tập trung kinh tế nếu vượt ngưỡng · phê duyệt bộ chuyên ngành theo lĩnh vực Target · NHNN nếu Target là TCTD · UBCK nếu công ty đại chúng · phê duyệt nội bộ (NQ HĐQT/ĐHĐCĐ, Lender consent).
- **Bắt buộc có:** Long Stop Date + cơ chế gia hạn có điều kiện · nghĩa vụ hợp tác phân chia rõ trách nhiệm mỗi CP · dẫn chiếu Điều 120.2 khi cố ý cản trở · cơ chế xử lý tiền đặt cọc khi chấm dứt vì CP không thoả.

## 10. Hợp đồng cổ đông (SHA) vs Điều lệ
- **Bẫy phổ biến nhất:** câu "SHA thắng Điều lệ khi mâu thuẫn" (chuẩn common law) **không đứng vững** dưới LDN 2020 cho các nội dung bắt buộc phải có trong Điều lệ và đăng ký nhà nước.
- **Căn cứ VN:** Điều 24 LDN 2020 (nội dung bắt buộc Điều lệ); Điều 20.2/21.2/22.2 (Điều lệ là một phần hồ sơ đăng ký); Điều 115, 138–152 (ĐHĐCĐ, quyền cổ đông — một số bắt buộc, một số Điều lệ tự quy định được); Điều 419 (bồi thường khi vi phạm SHA).
- **Nguyên tắc phân định:** (a) vấn đề LDN bắt buộc trong Điều lệ + đăng ký nhà nước (vốn, cơ cấu vốn, người đại diện pháp luật) → **Điều lệ thắng**, quyết định nội bộ theo Điều lệ vẫn hợp lệ về thủ tục dù trái SHA; (b) quan hệ thuần giữa các cổ đông (Drag/Tag/ROFR, biểu quyết đặc biệt) → **SHA ràng buộc**, cổ đông vi phạm phải bồi thường dù đã tuân thủ đúng Điều lệ.
- **Bắt buộc có:** điều khoản phân định rõ 2 nhóm trên · cam kết cập nhật Điều lệ khớp SHA trong thời hạn cụ thể (thường 30 ngày) · cơ chế bảo vệ cổ đông nhỏ khi đa số tự sửa Điều lệ trái SHA (bồi thường, không huỷ quyết định đã đăng ký).

## Cách dùng trong review/drafting
1. Xác định điều khoản đang review thuộc nhóm nào trong 10 nhóm trên (hoặc `transaction-clause-checklists.md` cho các dấu hiệu tabular khác: CoC, assignment, successor liability).
2. Kiểm căn cứ VN tương ứng — **verify hiệu lực qua MCP `legal`** trước khi trích dẫn trong finding.
3. So khớp với benchmark US ở `ma-document-guides.md` nếu cần biết "thị trường đang ở đâu" cho đàm phán.
4. Cần **nguyên văn điều khoản mẫu tiếng Việt** để soạn thảo → mở file gốc tại `assets/re-legal-counsel/` (mục Ch.21 §1–§10 tương ứng).
5. Phân loại Must-Win/Negotiate/Accept theo `negotiation-and-dispute-playbook.md`.
