---
description: Xem trạng thái deal — đọc deal dossier và tóm tắt giai đoạn, kết luận, findings và việc còn treo
argument-hint: [deal-id, hoặc bỏ trống để liệt kê mọi deal]
---

Báo cáo trạng thái deal: $ARGUMENTS

1. Nếu có deal-id: đọc `deals/<deal-id>/_dossier.md` và tóm tắt cho Sếp: giai đoạn lifecycle hiện tại + kết luận từng giai đoạn đã xong, findings trọng yếu còn mở (severity cao trước), câu hỏi / việc còn treo kèm owner, và next step đề xuất.
2. Nếu không có deal-id: liệt kê các thư mục trong `deals/`, đọc bảng "Trạng thái lifecycle" của từng `_dossier.md` (chỉ phần đó, không đọc cả file) và trả về bảng tổng hợp: deal, giai đoạn, kết luận gần nhất, ngày cập nhật.
3. Nếu dossier không tồn tại, nói rõ và đề xuất tạo từ `templates/deal-dossier.md`.
