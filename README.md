# Real Estate Suite — Claude Code / Cowork plugin

Bộ workflow tiếng Việt cho mô hình vận hành của một Chủ đầu tư bất động sản,
đóng gói theo chuẩn plugin của Claude Code / Cowork.

## Bao gồm

- RE-HQ — điều phối, tổng hợp đa phòng cấp executive, trọng tài xung đột
- RE-Legal — pháp lý (re-legal-licensing, re-legal-counsel, re-legal-writing, re-legal-operations…)
- RE-Investment-Finance — sở hữu toàn bộ deal lifecycle
- RE-Market-Research — nghiên cứu thị trường (engine `re-rnd`)
- RE-Project-Design — thiết kế, chỉ tiêu quy hoạch 1/500 (`re-project-design-planning`)
- 4 agents phòng ban (`agents/`: re-legal, re-rnd, re-inv, re-project) cho chế độ chạy song song + 4 slash commands (`commands/`)

Plugin chỉ chứa workflow và template. Hồ sơ deal, tri thức nội bộ, credentials
và output sinh ra lưu ở một data workspace riêng (xem
`plugins/real-estate-suite/references/workspace-layout.md`); mỗi deal có file
trạng thái `deals/<deal-id>/_dossier.md` để giữ ngữ cảnh xuyên session.

## Cài đặt (Claude Code / Cowork)

```
/plugin marketplace add mayaincaztec/real-estate-suite
/plugin install real-estate-suite
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
plugins/real-estate-suite/
  .claude-plugin/plugin.json             # manifest plugin
  skills/                                # 21 skills (SKILL.md) — Claude tự quét
  agents/                                # 4 agent phòng ban (chạy song song qua Agent tool)
  commands/                              # 4 slash commands (/re-screen, /re-fs, /re-dd, /re-status)
  references/                            # tài liệu tham chiếu (routing-map, operating-contract,
                                         #   workspace-layout, legal-lookup-protocol, authoring guide)
  templates/                             # template deliverable (kèm deal-dossier.md)
  scripts/                               # tiện ích Python (check bundle, init workspace)
tests/                                   # kiểm thử bundle (gốc repo)
```

## Skills

21 skills, đặt tên theo prefix phòng ban (entry mỗi phòng trùng tên agent):

- **HQ & chung:** re-hq, initialize-re-workspace
- **RE-Inv (Đầu tư):** re-inv (entry), re-inv-screening, re-inv-preliminary-report,
  re-inv-feasibility-study, re-inv-full-report, re-inv-deal-structuring,
  re-inv-dd-coordinator, re-inv-operating-matrix, re-inv-verification-rules
- **RE-Legal (Pháp lý):** re-legal (entry), re-legal-operations, re-legal-licensing,
  re-legal-counsel, re-legal-writing, re-legal-doc-renamer, re-legal-verification-rules
- **RE-RnD (Thị trường):** re-rnd (entry + engine database vault Obsidian)
- **RE-Project (Thiết kế):** re-project (entry), re-project-design-planning

Phòng Đầu tư (`re-inv`) sở hữu toàn bộ deal lifecycle: screening →
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
  python plugins/real-estate-suite/scripts/check_bundle.py
  python -m unittest discover -s tests -v
  ```
- Quy ước viết/sửa skill: `plugins/real-estate-suite/references/skill-authoring-guide.md`
  (bao gồm mục Bảo trì & anti-drift và chu kỳ rà kiến thức tĩnh theo quý).
