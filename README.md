# RE Developer Suite — Claude Code / Cowork plugin

Bộ workflow tiếng Việt cho mô hình vận hành của một Chủ đầu tư bất động sản,
đóng gói theo chuẩn plugin của Claude Code / Cowork.

> Bản này được chuyển đổi từ marketplace Codex gốc (`mayaincaztec/re-developer`)
> sang chuẩn Claude. Nội dung skills, references, templates giữ nguyên; chỉ thay
> lớp manifest (`.claude-plugin/`).

## Bao gồm

- RE-HQ — điều phối và phân luồng yêu cầu
- RE-Legal — pháp lý (licensing-expert, legal-counsel, legal-writing, deliverable templates…)
- RE-Investment-Finance
- RE-Market-Research
- RE-Project-Design
- Due diligence và deal-structuring workflows

Plugin chỉ chứa workflow và template. Lưu hồ sơ deal, tri thức nội bộ, credentials
và output sinh ra ở một data workspace riêng.

## Cài đặt (Claude Code / Cowork)

```
/plugin marketplace add mayaincaztec/re-developer-claude
/plugin install re-developer-suite
```

Sau khi cài, mở thread mới và gọi các skill, ví dụ:

- "Dùng RE-HQ để phân luồng yêu cầu này."
- "Điều phối due diligence cho thương vụ này."
- "Soạn công văn pháp lý cho dự án ..."

## Cấu trúc

```
.claude-plugin/marketplace.json          # marketplace ở gốc repo
plugins/re-developer-suite/
  .claude-plugin/plugin.json             # manifest plugin
  skills/                                # 25 skills (SKILL.md) — Claude tự quét
  references/                            # tài liệu tham chiếu
  templates/                            # template deliverable
  scripts/  tests/                       # tiện ích bổ sung
```

## Skills

25 skills: dd-coordinator, deal-structuring-advisor, design-planning, doc-renamer,
initialize-re-workspace, legal-counsel, legal-writing, licensing-expert,
re-feasibility-study, re-full-investment-report, re-hq, re-investment-finance,
re-investment-operating-matrix, re-investment-screening, re-investment-verification-rules,
re-legal, re-legal-deliverable-templates, re-legal-intake-router, re-legal-operating-matrix,
re-legal-skill-maintenance, re-legal-verification-rules, re-market-research,
re-preliminary-investment-report, re-project-design, vn-re-research.

Phòng Đầu tư (`re-investment-finance`) sở hữu toàn bộ deal lifecycle: screening →
báo cáo sơ bộ → FS → báo cáo đầy đủ/IC → deal structuring + LOI → DD coordination.

## Ghi chú

- `scripts/check_bundle.py` (kiểm tra cấu trúc) và `scripts/initialize_workspace.py`
  (tạo data workspace với `CLAUDE.md`) là tiện ích Python tùy chọn; Claude không tự chạy.
- Để chạy kiểm thử bundle (tuỳ chọn, Python 3.11+):
  ```
  python plugins/re-developer-suite/scripts/check_bundle.py
  python -m unittest discover -s tests -v
  ```
