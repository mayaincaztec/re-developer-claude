# Skill Authoring Guide — Real Estate Suite

Quy ước để thêm/sửa skill trong suite một cách nhất quán. Đọc trước khi tạo skill mới hoặc refactor.

## Frontmatter (bắt buộc)

```yaml
---
name: <kebab-case, tiếng Anh>
description: <tiếng Anh, hướng trigger — "Use for/when ...">
version: <semver, vd 1.0.0>
license: MIT
---
```
- `name`/`description` để tiếng Anh giúp Claude trigger chính xác; **body viết tiếng Việt**.
- `description` phải mô tả *khi nào dùng* (Claude chọn skill dựa vào đây), không phải mô tả nội bộ.

## Ngôn ngữ & giọng

- Body, workflow, SOP **và tiêu đề mục (`##`/`###`)**: **tiếng Việt**. Tiếng Anh chỉ khi không có từ tương đương hoặc cần giữ thuật ngữ chuẩn (vd FS, NPV, IRR, LOI, DD, FAR, MAC, SPA) — ưu tiên kiểu **Việt ngữ (Anh ngữ)**.
- KHÔNG dùng tiêu đề tiếng Anh có sẵn từ Việt (When to Use → Khi nào dùng, Workflow → Quy trình, Overview → Tổng quan, Output shapes → Dạng đầu ra, Common Pitfalls → Lỗi thường gặp, Verification → Kiểm tra).
- Thuật ngữ quan trọng: kiểu **Việt ngữ (Anh ngữ)**, vd Rà Soát Thẩm Định (Due Diligence).
- Phần hội thoại: xưng **em**, gọi người dùng **Sếp**.
- **Ngôn ngữ làm việc ≠ ngôn ngữ deliverable:** body/SOP luôn tiếng Việt; deliverable theo yêu cầu của Sếp hoặc ngôn ngữ bối cảnh chi phối (vd hợp đồng tiếng Anh → memo tiếng Anh). Xem `operating-contract.md` mục Output language. Skill nào tạo deliverable nên nêu rõ deliverable có thể đa ngôn ngữ.

## Cấu trúc body khuyến nghị

`Overview` → `When to Use` + `Do not use for` → `Workflow` (các bước) → `Output shapes` → `Common Pitfalls` → `Verification Checklist`. Tham khảo `re-legal-licensing`, `re-inv-feasibility-study` làm mẫu.

## Templates vs references — khi nào dùng cái nào

Quy ước thống nhất cho toàn suite:

- **`templates/` (dùng chung, gốc plugin):** mọi **deliverable** — khung output mà người dùng nhận hoặc nộp (memo, report, matrix, issue list, LOI, screening note, IC memo, brief…). Đây là "vỏ" trình bày, không gắn cứng với một skill.
- **`references/` (trong từng skill):** chỉ **spec kỹ thuật / tài liệu nền** mà skill cần để thực thi — bảng tra (calc engine, QCVN, dictionaries), spec cấu trúc (FS structure, FS Excel build guide), guide nội bộ (entry-points, ma-document-guides, loi-and-offer-guide, tvpl protocol đặt ở `references/` gốc plugin vì dùng chung).

Quy tắc nhanh: *output giao đi → `templates/`; tài liệu để skill làm việc → `references/`.* Một skill "operations layer" như `re-legal-operations` chỉ **chọn và trỏ** tới `../../templates/...`, không tự chứa file deliverable.

## Đường dẫn

- Dùng **đường dẫn tương đối đúng**: từ `SKILL.md` → `../../references/...` (references gốc plugin), `../../templates/...`; từ file trong `references/` của skill → `../../../...`.
- `tests/test_bundle.py::test_internal_md_references_resolve` **bắt buộc mọi reference resolve** — chạy test sau khi thêm/đổi đường dẫn.

## Routing & ownership (single source of truth)

- Doctrine định tuyến ở `routing-map.md` — **không lặp lại bảng routing** trong skill; chỉ trỏ tới.
- **Deal lifecycle** (screening → FS → reports → structuring/LOI → DD → IC) thuộc `RE-Investment-Finance`.
- **Tổng hợp đa phòng cấp executive / trọng tài** thuộc `RE-HQ`.
- **Specialist legal execution** thuộc `RE-Legal` (không ôm coordination).

## Hợp đồng xuyên suốt (phải tuân theo)

- **Finding schema + handoff packet**: `operating-contract.md`.
- **Pháp lý**: kiểm chứng hiệu lực văn bản qua MCP `tvpl` theo `tvpl-lookup-protocol.md`, hoặc gắn caveat "chưa kiểm chứng".
- **Verification layer**: mỗi phòng có `*-verification-rules`; chạy trước khi chốt output chính thức.

## Naming convention

- Entry phòng ban: `re-<dept>` (vd `re-legal`, `re-inv`).
- Hạ tầng phòng ban: `re-<dept>-<role>` (vd `re-legal-operations`, `re-inv-verification-rules`).
- Workflow/specialist dùng chung hoặc đặc thù: tên trần mô tả (vd `re-legal-licensing`, `re-inv-dd-coordinator`, `re-project-design-planning`).
- **Grandfather:** tên skill là định danh ổn định (nhiều nơi tham chiếu). Không đổi tên chỉ vì mỹ quan — Claude trigger theo `description`, không theo tên. Áp convention cho skill **mới**; đổi tên skill cũ chỉ khi thật cần và phải cập nhật mọi tham chiếu + chạy lại test.

## Khi thêm / xóa một skill

1. Tạo/xóa thư mục `skills/<name>/SKILL.md`.
2. Cập nhật `scripts/check_bundle.py` (`expected_skills`).
3. Cập nhật `README.md` (số lượng + danh sách skill).
4. Thêm mục `CHANGELOG.md` + bump version (`plugin.json` và `marketplace.json` khớp nhau).
5. Chạy `python scripts/check_bundle.py` và `python -m unittest discover -s tests`.

## Bảo trì & anti-drift

Mục này dành cho người bảo trì suite (không phải skill runtime).

**Đồng bộ khi đổi boundary/ownership:** so entry phòng ban + operations/operating-matrix + verification-rules + `routing-map.md` của các phòng liên quan. Routing chỉ được sống ở `routing-map.md`; mọi chỗ khác chỉ trỏ về.

**Khi thay một skill bằng source folder bên ngoài (sync canonical copy):**
1. Backup target folder trước khi ghi đè (tên backup đủ rõ để rollback).
2. Copy đúng source trước, **không auto-normalize** trong cùng bước; nếu bản mới lệch chuẩn suite (frontmatter, ngôn ngữ, đường dẫn), báo rõ và tách thành bước normalize tùy chọn sau.
3. Verify sau sync: file đã copy, source–target khớp, frontmatter còn hợp lệ (dấu `---` đóng đúng).
4. Rà tác động: cross-references còn resolve (`tests/test_bundle.py`), bảng Markdown không lệch cột, boundary wording không bị kéo lùi về doctrine cũ.

**Checklist sau mỗi đợt sửa bundle:**
- [ ] `check_bundle.py` + `python -m unittest discover -s tests` xanh
- [ ] README (số lượng + danh sách skill) khớp thực tế
- [ ] Entry phòng ban, operations layer và verification-rules nói cùng một load order
- [ ] Boundary `RE-Legal` / `RE-Investment-Finance` / `RE-HQ` nhất quán với `routing-map.md`
- [ ] CHANGELOG + version (`plugin.json` và `marketplace.json` khớp nhau)

**Chu kỳ rà kiến thức tĩnh (mỗi quý hoặc khi có luật mới):** chạy tvpl `check_hieu_luc` cho danh mục trong `re-legal-licensing/references/vn-legal-texts.md`; rà các bảng số liệu có `as-of` (thuế trong `structuring-tax-guide.md`, cơ quan thẩm quyền trong `agencies-and-authority.md`) và cập nhật ngày `as-of` sau khi xác nhận.
