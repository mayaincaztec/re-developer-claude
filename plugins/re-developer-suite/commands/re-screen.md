---
description: Sàng lọc nhanh một deal BĐS đầu vào (go / pass / watch) bằng workflow RE-Investment-Finance
argument-hint: [tên deal hoặc mô tả / đường dẫn teaser/CIM]
---

Dùng skill `re-inv-screening` (RE Developer Suite) để sàng lọc deal sau: $ARGUMENTS

- Nếu Sếp đưa đường dẫn file (teaser/CIM), đọc file trước.
- Áp bộ tiêu chí screening, kết luận Proceed / Pass / Watch theo template `deal-screening-note`.
- Nếu Proceed: tạo deal dossier theo `templates/deal-dossier.md` tại `deals/<deal-id>/_dossier.md` và ghi kết quả.
- Qua `re-inv-verification-rules` trước khi chốt.
