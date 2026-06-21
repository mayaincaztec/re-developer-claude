> **Lưu ý kiểm chứng:** Mọi quy định, ngưỡng, thủ tục và cơ quan có thẩm quyền phải được kiểm tra lại bằng nguồn chính thức còn hiệu lực tại ngày sử dụng (qua MCP `legal` theo `../../../references/legal-lookup-protocol.md`).

# Corporate Legal Records Checklist — CTCP (công ty cổ phần)

> Reference của `re-legal-counsel` cho **rà soát hồ sơ pháp lý doanh nghiệp (entity-level)** — dùng trong **Transaction Legal DD (Mode 4)** khi target là một CTCP, và cho review tính đầy đủ hồ sơ pháp lý nội bộ.
> Nguồn gốc: checklist quản trị nội bộ hồ sơ pháp lý CTCP (10 nhóm) mà CEO/HĐQT cần lưu trữ đầy đủ; ở đây được chuyển thành **công cụ DD/review**.

## Ranh giới sở hữu (đọc trước)

- **`re-legal-counsel` (file này)** — sở hữu **pháp lý DOANH NGHIỆP / entity**: tư cách pháp nhân, ĐKKD, cổ đông/vốn/chủ sở hữu hưởng lợi (BO), quản trị nội bộ, giấy phép con **cấp doanh nghiệp**, hợp đồng, kế toán–thuế, lao động, dữ liệu cá nhân, tài sản/IP/bảo hiểm, thanh tra–tranh chấp.
- **`re-legal-licensing` (kéo riêng)** — sở hữu **pháp lý DỰ ÁN**: đất đai, chấp thuận chủ trương, quy hoạch 1/500, giấy phép xây dựng, điều kiện mở bán, PCCC/ĐTM **của dự án cụ thể**. Trong DD đây là một workstream tách (WORKSTREAM II của `re-inv-dd-coordinator`).
- Lằn ranh Nhóm IV (giấy phép con): **điều kiện kinh doanh cấp pháp nhân** (vd giấy phép sàn giao dịch BĐS, chứng chỉ năng lực hoạt động xây dựng của công ty, PCCC/môi trường của **trụ sở**) → counsel; **giấy phép gắn dự án cụ thể** → licensing.

## Cách dùng trong DD (4 nhịp)

1. **Request** — phát DRL theo 10 nhóm (ưu tiên P1/P2/P3 ở dưới); ánh xạ vào WORKSTREAM I của DD Coordinator.
2. **Completeness** — đánh trạng thái từng mục: **Có / Thiếu / Không áp dụng (N/A)**; ghi version/ngày khi có lịch sử thay đổi.
3. **Red flag** — soi dấu hiệu rủi ro (cột "Soi & red flag"); material hay không lấy ngưỡng từ handoff/dossier, **không tự bịa**.
4. **Finding** — phát biểu theo Quote-First; cuộn lên `../../../templates/transaction-dd-findings-memo.md` (narrative) hoặc xuất trực tiếp **review grid** ở cuối file này.

Ưu tiên: **P1** = trọng yếu/deal-gating · **P2** = cần có, rủi ro trung bình · **P3** = nên có.

---

## I. Hồ sơ pháp lý doanh nghiệp
| Hồ sơ | P | Soi & red flag |
|---|---|---|
| GCN ĐKDN bản mới nhất + toàn bộ bản cũ | P1 | khớp ngành nghề/vốn/người đại diện với thực tế; lịch sử thay đổi liên tục không |
| Hồ sơ đăng ký thành lập ban đầu (đề nghị, Điều lệ, DS cổ đông sáng lập) | P1 | cổ đông sáng lập còn trong thời hạn hạn chế chuyển nhượng |
| Các thông báo/hồ sơ thay đổi ĐKDN qua từng lần | P1 | thay đổi chưa đăng ký → vi phạm |
| Điều lệ hiện hành | P1 | cơ cấu ĐHĐCĐ/HĐQT/BKS, thẩm quyền ký, quyền cổ đông |
| Các bản sửa đổi, bổ sung Điều lệ (kèm NQ thông qua) | P1 | sửa Điều lệ thiếu nghị quyết có thẩm quyền |
| Mã số thuế, thông báo cơ quan thuế quản lý | P2 | — |
| Hồ sơ trụ sở chính (HĐ thuê/mượn, biên bản bàn giao) | P2 | trụ sở không hợp pháp → rủi ro ĐKDN |
| Hồ sơ chi nhánh/VPĐD/địa điểm kinh doanh | P2 | hoạt động không đăng ký |
| Hồ sơ người đại diện theo pháp luật (CCCD/hộ chiếu, QĐ bổ nhiệm, phạm vi thẩm quyền) | P1 | phạm vi ủy quyền ký vượt thẩm quyền |
| Hồ sơ con dấu (mẫu dấu, QĐ sử dụng, quy chế) | P2 | — |
| Hồ sơ chữ ký số, tài khoản thuế điện tử, tài khoản ĐKKD | P2 | ai giữ token/mật khẩu, lịch gia hạn |
| Danh mục ngành nghề kinh doanh hiện tại | P1 | ngành nghề có điều kiện chưa đủ điều kiện |
| Giấy phép, chứng nhận, văn bằng khác | P2 | còn hiệu lực / đã gia hạn |

## II. Cổ đông, cổ phần, vốn điều lệ & chủ sở hữu hưởng lợi (BO)
| Hồ sơ | P | Soi & red flag |
|---|---|---|
| Danh sách cổ đông sáng lập | P1 | hạn chế chuyển nhượng còn hiệu lực |
| Danh sách cổ đông là nhà đầu tư nước ngoài | P1 | tỷ lệ sở hữu nước ngoài, điều kiện tiếp cận thị trường |
| **Sổ đăng ký cổ đông** (current cap table) | P1 | 🔴 không khớp thực tế; thiếu sổ |
| GCN cổ phần/cổ phiếu đã phát hành | P2 | tình trạng thu hồi/cấp lại |
| Chứng từ góp vốn bằng tiền (sao kê, chứng từ chuyển khoản) | P1 | góp vốn ảo / chưa góp đủ |
| Hồ sơ góp vốn bằng tài sản (định giá, bàn giao, sang tên) | P1 | định giá khống; chưa sang tên |
| Cam kết/thỏa thuận góp vốn của cổ đông | P1 | nghĩa vụ góp chậm/thiếu |
| Hồ sơ tăng vốn/phát hành thêm cổ phần | P1 | trình tự phát hành đúng luật không |
| Hồ sơ giảm vốn điều lệ | P1 | cam kết bảo đảm thanh toán nợ |
| **Hồ sơ chuyển nhượng cổ phần** | P1 | 🔴 ROFR chưa tiết lộ; thuế chuyển nhượng |
| Hồ sơ mua lại/buyback cổ phần | P2 | cập nhật sổ + vốn điều lệ |
| Hồ sơ cổ phần ưu đãi | P2 | quyền ưu đãi, hạn chế chuyển nhượng |
| Hồ sơ quyền mua/chào bán riêng lẻ | P2 | — |
| Hồ sơ trả cổ tức | P2 | NQ thông qua, khấu trừ thuế |
| Hồ sơ cổ đông lớn/cổ đông liên quan | P1 | giao dịch với người liên quan |
| Hồ sơ người đại diện theo ủy quyền của cổ đông tổ chức | P2 | phạm vi/thời hạn ủy quyền |
| **Danh sách chủ sở hữu hưởng lợi (BO)** | P1 | 🔴 BO khác đăng ký → tranh chấp quyền sở hữu |
| Tài liệu xác định BO (sơ đồ sở hữu, quyền chi phối) | P1 | quyền bổ nhiệm/quyết định ẩn |
| Danh sách người có liên quan & bên liên quan | P1 | kiểm soát giao dịch nội bộ |
| **Hồ sơ hạn chế chuyển nhượng cổ phần** | P1 | 🔴 SHA/cam kết hạn chế tạo quyền cho bên thứ ba |

## III. Quản trị nội bộ & điều hành
| Hồ sơ | P | Soi & red flag |
|---|---|---|
| Quy chế quản trị nội bộ; Sơ đồ tổ chức | P2 | — |
| Quy chế phân quyền & ủy quyền; **Ma trận thẩm quyền phê duyệt** | P1 | ai được ký HĐ/duyệt chi/đầu tư |
| Quy chế tài chính; quy chế chi tiêu nội bộ | P2 | — |
| Quy chế phối hợp; quy chế kiểm soát nội bộ | P3 | — |
| Quy trình mua hàng; **quy trình ký kết & quản lý hợp đồng** | P2 | có bước pháp lý–tài chính trước khi ký không |
| Quy trình quản lý con dấu/chữ ký số/tài khoản | P2 | rủi ro ký sai thẩm quyền |
| QĐ bổ nhiệm/miễn nhiệm Chủ tịch HĐQT, thành viên HĐQT | P1 | kèm biên bản/NQ hợp lệ |
| QĐ bổ nhiệm/miễn nhiệm GĐ/TGĐ, Kế toán trưởng | P1 | thẩm quyền ký của người điều hành |
| Hồ sơ Ban kiểm soát/Ủy ban kiểm toán | P2 | — |
| **Thông báo mời họp + tài liệu + Biên bản + NQ/QĐ ĐHĐCĐ** (3 năm) | P1 | trình tự triệu tập/thông qua hợp lệ; quyết định về vốn/Điều lệ/giao dịch lớn |
| **Thông báo mời + tài liệu + Biên bản + NQ/QĐ HĐQT** (3 năm) | P1 | quyết định đúng thẩm quyền |
| Báo cáo điều hành định kỳ của GĐ/TGĐ | P3 | — |
| **Quy chế phòng chống xung đột lợi ích** | P2 | giao dịch với cổ đông/người liên quan |
| Quy trình lưu trữ hồ sơ nội bộ | P3 | — |

## IV. Giấy phép con & điều kiện kinh doanh *(cấp pháp nhân — project-specific → licensing)*
| Hồ sơ | P | Soi & red flag |
|---|---|---|
| GCN đăng ký đầu tư (IRC) nếu có vốn nước ngoài | P1 | bắt buộc nếu FDI |
| Các QĐ điều chỉnh IRC | P1 | mỗi lần đổi mục tiêu/vốn/địa điểm/tiến độ |
| **Giấy phép đủ điều kiện kinh doanh chuyên ngành** (vd sàn BĐS) | P1 | ngành có điều kiện thiếu giấy phép → vi phạm |
| Chứng chỉ hành nghề của cá nhân phụ trách chuyên môn | P2 | đủ nhân sự có chứng chỉ |
| Hồ sơ công bố/đăng ký chất lượng sản phẩm | P3 | — |
| Hồ sơ PCCC *(của trụ sở; PCCC dự án → licensing)* | P2 | nghiệm thu, tập huấn, kiểm tra định kỳ |
| Hồ sơ môi trường *(cấp pháp nhân; ĐTM dự án → licensing)* | P2 | giấy phép môi trường, quan trắc |
| Hồ sơ website/app/sàn TMĐT | P3 | điều khoản sử dụng, chính sách bảo mật |
| Báo cáo định kỳ theo giấy phép chuyên ngành | P2 | quá hạn nộp → rủi ro |
| Công văn làm việc với cơ quan cấp phép | P2 | lưu hỏi–đáp, yêu cầu bổ sung |

## V. Hợp đồng & giao dịch thương mại
| Hồ sơ | P | Soi & red flag |
|---|---|---|
| HĐ khách hàng; HĐ nhà cung cấp/đối tác | P1 | thanh toán, phạt, bồi thường; **Change-of-Control** |
| HĐ dịch vụ thường xuyên (retainer); HĐ lao động/quản lý cấp cao | P2 | non-compete, bảo mật |
| Báo giá/đề xuất; Đơn đặt hàng/PO/SOW | P2 | căn cứ phạm vi/giá |
| Biên bản bàn giao; biên bản nghiệm thu; biên bản thanh lý | P2 | nghĩa vụ còn tồn đọng |
| **Hồ sơ công nợ** (đối chiếu, xác nhận nợ) | P1 | nợ phải thu/phải trả trọng yếu |
| Thư vi phạm/chấm dứt/yêu cầu bồi thường | P1 | tranh chấp tiềm ẩn |
| Hợp đồng bảo mật/NDA | P2 | — |
| **Ủy quyền ký hợp đồng (POA)** | P1 | đúng người/phạm vi/hạn mức |
| **Hồ sơ phê duyệt HĐ lớn/giao dịch rủi ro** (kèm NQ/QĐ) | P1 | chứng minh đúng thẩm quyền |

> Rà clause trọng yếu theo `transaction-clause-checklists.md`; nhiều HĐ cùng loại → tabular review (`transaction-dd-playbook.md` + `../../../templates/clause-review-grid.md`); danh mục HĐ trọng yếu → `../../../templates/material-contract-schedule.md`.

## VI. Kế toán, tài chính, thuế & hóa đơn
| Hồ sơ | P | Soi & red flag |
|---|---|---|
| Quy chế tài chính/kế toán nội bộ; sổ kế toán; chứng từ kế toán | P2 | — |
| **BCTC năm** (đã kiểm toán, 3 năm) + báo cáo quản trị nội bộ | P1 | doanh thu khớp tiến độ; off-balance-sheet |
| Tờ khai thuế GTGT/TNDN/TNCN | P1 | 🔴 nợ thuế lớn buyer gánh |
| Hồ sơ lệ phí môn bài | P3 | — |
| Hóa đơn điện tử đầu ra/đầu vào; hồ sơ điều chỉnh/hủy hóa đơn | P2 | khớp HĐ–nghiệm thu–thanh toán |
| Sao kê ngân hàng; hồ sơ tài khoản ngân hàng DN | P2 | người ủy quyền, hạn mức |
| **Hồ sơ khoản vay, lãi vay, bảo lãnh** | P1 | thế chấp cổ phần/tài sản; bảo lãnh đã cấp |
| Hồ sơ TSCĐ & khấu hao; kiểm kê hàng tồn/tài sản | P2 | — |
| **Hồ sơ quyết toán/kiểm tra thuế** | P1 | nghĩa vụ sau thanh tra |

## VII. Lao động, nhân sự, tiền lương & BHXH
| Hồ sơ | P | Soi & red flag |
|---|---|---|
| Sổ quản lý lao động; hồ sơ cá nhân NLĐ | P2 | — |
| **HĐ lao động** + phụ lục; mô tả công việc | P2 | đủ HĐ ký cho toàn bộ nhân sự |
| Quy chế lương/thưởng/phụ cấp; thang bảng lương; quy chế KPI | P3 | — |
| Bảng chấm công; bảng lương; hồ sơ làm thêm giờ | P3 | — |
| **Nội quy lao động** (≥10 NLĐ phải bằng văn bản) + đăng ký | P2 | thiếu khi đủ điều kiện → vi phạm |
| Quy trình & hồ sơ xử lý kỷ luật lao động | P2 | đúng trình tự khi có tranh chấp |
| Hồ sơ nghỉ phép/nghỉ việc; **hồ sơ chấm dứt HĐLĐ** | P2 | tranh chấp lao động |
| **Hồ sơ BHXH/BHYT/BHTN** | P1 | truy đóng/nợ BHXH |
| Hồ sơ an toàn, vệ sinh lao động | P2 | tai nạn lao động |
| **Hồ sơ lao động nước ngoài** (giấy phép LĐ/visa/TRC) | P1 | làm việc không phép → vi phạm |

## VIII. Bảo vệ dữ liệu cá nhân & công nghệ
| Hồ sơ | P | Soi & red flag |
|---|---|---|
| Chính sách bảo vệ DLCN; thông báo xử lý DLCN; mẫu đồng ý | P2 | tuân thủ NĐ về bảo vệ DLCN |
| Hồ sơ đánh giá tác động xử lý DLCN | P2 | khi thuộc diện phải đánh giá |
| Hồ sơ chuyển DLCN ra nước ngoài | P2 | khi có transfer xuyên biên giới |
| HĐ/thỏa thuận xử lý dữ liệu với bên thứ ba | P2 | CRM, cloud, kế toán, marketing |
| Danh mục hệ thống lưu trữ; ma trận phân quyền truy cập | P3 | ai xem/sửa/tải/chia sẻ |
| Quy trình xử lý sự cố rò rỉ/mất dữ liệu; nhật ký yêu cầu chủ thể dữ liệu | P3 | đầu mối, quy trình thông báo |

## IX. Tài sản, sở hữu trí tuệ & bảo hiểm
| Hồ sơ | P | Soi & red flag |
|---|---|---|
| Danh mục tài sản công ty; **giấy tờ chứng minh quyền sở hữu tài sản** | P1 | tài sản đứng tên đúng pháp nhân |
| Biên bản bàn giao tài sản cho nhân sự/bộ phận | P3 | — |
| **HĐ thuê văn phòng/kho/nhà xưởng** | P2 | thời hạn, điều kiện chấm dứt |
| Văn bằng bảo hộ nhãn hiệu; domain/website/hosting; bản quyền phần mềm/source code | P2 | quyền sở hữu/sử dụng/chuyển giao rõ ràng |
| HĐ bảo hiểm tài sản/trách nhiệm; bảo hành–bảo trì | P2 | phạm vi, thời hạn, điều kiện bồi thường |
| **Hồ sơ thế chấp, cầm cố, bảo đảm nghĩa vụ** | P1 | 🔴 tài sản/cổ phần đang bảo đảm → giải chấp trước closing |

## X. Kiểm tra, thanh tra, tranh chấp & tuân thủ
| Hồ sơ | P | Soi & red flag |
|---|---|---|
| Biên bản làm việc với cơ quan thuế/lao động/BHXH/PCCC–môi trường | P1 | nghĩa vụ khắc phục còn treo |
| **Kết luận thanh tra/kiểm tra**; QĐ xử phạt VPHC | P1 | nghĩa vụ sau kiểm tra; phạt chưa nộp |
| Hồ sơ khiếu nại/giải trình với cơ quan nhà nước | P2 | — |
| **Hồ sơ tranh chấp hợp đồng; hồ sơ tố tụng tại Tòa/Trọng tài** | P1 | 🔴 đang kiện tụng/điều tra → rủi ro nghiêm trọng |
| Ý kiến tư vấn pháp lý đã nhận | P2 | cơ sở ra quyết định |
| **Danh mục rủi ro pháp lý nội bộ; kế hoạch khắc phục sau rà soát** | P2 | cập nhật hằng quý |

---

## Dạng đầu ra — Corporate Legal Records Review Grid

Xuất khi cần bản rà tính đầy đủ + red flag (bổ trợ cho findings memo narrative):

```md
| Nhóm | Hồ sơ | Trạng thái (Có/Thiếu/N/A) | P | Red flag | Ghi chú / kiểm chứng | Owner |
|---|---|---|---|---|---|---|
| II | Sổ đăng ký cổ đông | Thiếu | P1 | 🔴 cap table không khớp | yêu cầu bổ sung trước closing | counsel |
| IX | Cầm cố cổ phần | Có | P1 | 🔴 giải chấp trước closing | HĐ cầm cố số … | counsel |
```

- Trạng thái material/severity lấy ngưỡng từ handoff/dossier; dẫn chiếu luật kiểm chứng qua MCP `legal`.
- Mục thuộc **pháp lý dự án** (đất/quy hoạch/GPXD/điều kiện mở bán/PCCC–ĐTM dự án) **không** đánh giá ở đây → chuyển `re-legal-licensing` (WORKSTREAM II của DD).
- Cuộn narrative + bottom-line theo `../../../templates/transaction-dd-findings-memo.md`; là **legal input** cho `re-inv-dd-coordinator`, không phải DD report tổng.
