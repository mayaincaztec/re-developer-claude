# Vault Layout — data contract của VN-RE-Research

> Source of truth cho **cấu trúc** vault dữ liệu market research. Data format chi tiết (frontmatter, template) do `_config/` trong vault quyết định; SOP do skill `vn-re-research` quyết định.

## Cây thư mục

```
<vault_root>/                      # vault Obsidian, khai báo trong re-workspace.yaml
  _config/
    TEMPLATES/PROJECT_TEMPLATE.md  # template file dự án — source of truth data format
    QUERIES/                       # dashboard Dataview (01-danh-sach… 05-stale-data)
    taxonomy/                      # manifest migration + geo-mapping.md
    AGENT_SKILL.md                 # con trỏ về skill vn-re-research trong plugin
  projects/
    <TINH>/                        # vùng thị trường: HCM | DNA | LAN | BDU | VTU
      _index.md                    # dashboard tỉnh (Dataview + bảng phân vùng giá)
      <quan-huyen>/                # lens thị trường cấp quận/huyện cũ (vd thu-duc, nhon-trach)
        <ten-du-an>.md             # tên không dấu, gạch ngang (vd king-bay.md)
        <cum>/                     # "cluster lens" — chỉ mở khi ≥5 dự án cùng micro-market
          <ten-du-an>.md           #   (vd q2/sala, q9/grand-park, q9/kdh)
  reports/
    market-analysis/<YYYY>/        # area study, monthly; weekly/ cho weekly note
    comparisons/<YYYY>/            # so sánh giá, xếp hạng; phase-sheets/ cho working sheet
    playbooks/                     # pricing playbook theo cụm — tài liệu sống, không theo năm
    field-audits/<YYYY>/           # báo cáo rà chất lượng dữ liệu
  assets/projects/<ten-du-an>/     # mỗi dự án tối đa vài ảnh chính (vị trí, masterplan)
  tools/ban-do-du-an.html          # bản đồ dự án — ăn theo trường toa_do trong frontmatter
```

## Naming

- File dự án: tên thương mại viết không dấu, gạch ngang (`the-global-city.md`).
- Báo cáo: `<YYYY-MM-DD>_<ten-bao-cao>.md` trong đúng nhánh reports.
- Playbook: `<cum>-pricing-playbook.md` (cập nhật tại chỗ, ghi ngày trong file).

## Vùng thị trường vs đơn vị hành chính (sau sáp nhập 2025)

Mã `<TINH>` (HCM/DNA/LAN/BDU/VTU) và cấp `<quan-huyen>` là **vùng thị trường** — giữ ổn định vì micro-market không đổi theo sáp nhập. Từ 01/07/2025 các đơn vị hành chính đã thay đổi (HCM+BDU+VTU → TP.HCM mới; chính quyền 2 cấp, bỏ cấp huyện). Quy tắc:

- Phân tích thị trường, so sánh giá, đặt path: dùng vùng thị trường.
- Trích dẫn hành chính/pháp lý trong báo cáo: dùng đơn vị mới theo `_config/taxonomy/geo-mapping.md` của vault; file dự án ghi ở trường `don_vi_hanh_chinh_2025`.

## Nguyên tắc đồng bộ vault ↔ skill

| Thứ | Source of truth | Khi đổi phải sync |
|---|---|---|
| Frontmatter schema, template dự án | vault `_config/TEMPLATES/` | `project-data-spec.md` (skill) + QUERIES |
| Taxonomy values | vault `_config/taxonomy/` (qua manifest, P6) | `project-data-spec.md` |
| SOP / protocols | skill `vn-re-research` | `AGENT_SKILL.md` chỉ là con trỏ, không chứa SOP |
| Template báo cáo | plugin `templates/market-research/` | `report-catalog.md` |

Không lưu credentials hoặc dữ liệu deal của Phòng Đầu tư trong vault này; hồ sơ deal nằm ở data workspace theo `../../../references/workspace-layout.md`.
