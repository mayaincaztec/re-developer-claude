# RE Developer Suite — Claude Code / Cowork plugin

Bộ workflow tiếng Việt cho mô hình vận hành của một Chủ đầu tư bất động sản,
đóng gói theo chuẩn plugin của Claude Code / Cowork.

## Bao gồm

- RE-HQ — điều phối, tổng hợp đa phòng cấp executive, trọng tài xung đột
- RE-Legal — pháp lý (licensing-expert, legal-counsel, legal-writing, re-legal-operations…)
- RE-Investment-Finance — sở hữu toàn bộ deal lifecycle
- RE-Market-Research — nghiên cứu thị trường (engine `vn-re-research`)
- RE-Project-Design — thiết kế, chỉ tiêu quy hoạch 1/500 (`design-planning`)
- 4 agents phòng ban (`agents/`) cho chế độ chạy song song + 4 slash commands (`commands/`)

Plugin chỉ chứa workflow và template. Hồ sơ deal, tri thức nội bộ, credentials
và output sinh ra lưu ở một data workspace riêng (xem
`plugins/re-developer-suite/references/workspace-layout.md`); mỗi deal có file
trạng thái `deals/<deal-id>/_dossier.md` để giữ ngữ cảnh xuyên session.

## Cài đặt (Claude Code / Cowork)

```
/plugin marketplace add mayaincaztec/re-developer-claude
/plugin install re-developer-suite
```

Sau khi cài, mở thread mới và gọi skill hoặc command, ví dụ:

- `/re-screen <tên deal>` — sàng lọc deal đầu vào
- `/re-fs <deal-id>` — dựng feasibility study (.xlsx)
- `/re-dd <deal-id>` — điều phối due diligence
- `/re-status` — xem trạng thái các deal
- "Dùng RE-HQ để phân luồng yêu cầu này." / "Soạn công văn pháp lý cho dự án …"

## Cấu trúc

```
.claude-plugin/marketplace.json          # marketplace ở gốc repo
plugins/re-developer-suite/
  .claude-plugin/plugin.json             # manifest plugin
  skills/                                # 22 skills (SKILL.md) — Claude tự quét
  agents/                                # 4 agent phòng ban (chạy song song qua Agent tool)
  commands/                              # 4 slash commands (/re-screen, /re-fs, /re-dd, /re-status)
  references/                            # tài liệu tham chiếu (routing-map, operating-contract,
                                         #   workspace-layout, tvpl-lookup-protocol, authoring guide)
  templates/                             # template deliverable (kèm deal-dossier.md)
  scripts/                               # tiện ích Python (check bundle, init workspace)
tests/                                   # kiểm thử bundle (gốc repo)
```

## Skills

22 skills: dd-coordinator, deal-structuring-advisor, design-planning, doc-renamer,
initialize-re-workspace, legal-counsel, legal-writing, licensing-expert,
re-feasibility-study, re-full-investment-report, re-hq, re-investment-finance,
re-investment-operating-matrix, re-investment-screening, re-investment-verification-rules,
re-legal, re-legal-operations, re-legal-verification-rules, re-market-research,
re-preliminary-investment-report, re-project-design, vn-re-research.

Phòng Đầu tư (`re-investment-finance`) sở hữu toàn bộ deal lifecycle: screening →
báo cáo sơ bộ → FS → báo cáo đầy đủ/IC → deal structuring + LOI → DD coordination.
Trạng thái mỗi deal sống trong deal dossier (`templates/deal-dossier.md`).

## Phạm vi (scope) có chủ đích

Suite hiện cover từ sourcing đến quyết định đầu tư (screening → IC → structuring/LOI → DD).
Các giai đoạn hậu đầu tư — giám sát triển khai, vận hành bán hàng / mở bán, quản lý sau
đầu tư, thoái vốn — **chưa nằm trong scope** và là hướng mở rộng dự kiến.

## Ghi chú

- `scripts/check_bundle.py` (kiểm tra cấu trúc + lint description/header) và
  `scripts/initialize_workspace.py` (tạo data workspace với `CLAUDE.md`) là tiện ích
  Python tùy chọn; Claude không tự chạy.
- Để chạy kiểm thử bundle (tuỳ chọn, Python 3.11+):
  ```
  python plugins/re-developer-suite/scripts/check_bundle.py
  python -m unittest discover -s tests -v
  ```
- Quy ước viết/sửa skill: `plugins/re-developer-suite/references/skill-authoring-guide.md`
  (bao gồm mục Bảo trì & anti-drift và chu kỳ rà kiến thức tĩnh theo quý).
