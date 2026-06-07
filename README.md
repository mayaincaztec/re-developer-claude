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
  skills/                                # 20 skills (SKILL.md) — Claude tự quét
  references/                            # tài liệu tham chiếu
  templates/                            # template deliverable
  agent-templates/  scripts/  tests/     # tiện ích bổ sung
```

## Skills

20 skills: dd-coordinator, deal-structuring-advisor, deal-structuring, doc-renamer,
initialize-re-workspace, legal-counsel, legal-writing, licensing-expert, re-hq,
re-investment-finance, re-legal, re-legal-deliverable-templates, re-legal-intake-router,
re-legal-operating-matrix, re-legal-skill-maintenance, re-legal-verification-rules,
re-market-research, re-project-design, setup-re-agents, vn-re-research.

## Ghi chú

- `agent-templates/*.toml` và `scripts/*.py` là tiện ích từ bản Codex; Claude không
  tự chạy chúng — giữ lại để tham chiếu, có thể lược bỏ sau.
- Để chạy kiểm thử bundle (tuỳ chọn, Python 3.11+):
  ```
  python plugins/re-developer-suite/scripts/check_bundle.py
  python -m unittest discover -s tests -v
  ```
