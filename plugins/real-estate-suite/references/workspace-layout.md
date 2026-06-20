# Workspace Layout — quy ước data workspace

> **Single source of truth** cho cấu trúc data workspace (tách khỏi plugin). Mọi skill đọc/ghi file phải theo quy ước này. Workspace được tạo/kiểm tra bằng skill `initialize-re-workspace` (`scripts/initialize_workspace.py`); đường dẫn gốc khai báo trong `re-workspace.yaml`.

## Cây thư mục chuẩn

```
<workspace_root>/
  CLAUDE.md                  # working rules của workspace
  re-workspace.yaml          # config + paths
  deals/
    <deal-id>/               # mỗi thương vụ một thư mục
      _dossier.md            # file trạng thái deal (template: templates/deal-dossier.md)
      docs/                  # tài liệu nhận từ đối tác / data room export
      analysis/              # báo cáo screening, sơ bộ, FS, đầy đủ, IC memo
      legal/                 # legal memo, issue list, hybrid package của deal
      correspondence/        # LOI, thư từ, biên bản
  knowledge/
    shared/                  # tri thức nội bộ dùng chung
    departments/
      legal/  investment-finance/  market-research/  project-design/
  templates-local/           # template nội bộ override template plugin theo filename (khi Sếp yêu cầu)
  outputs/                   # deliverable xuất ra ngoài deal context (báo cáo định kỳ…)
```

## Quy ước theo loại output

| Output | Vị trí | Đặt tên |
|---|---|---|
| Deal dossier | `deals/<deal-id>/_dossier.md` | cố định |
| Screening note / báo cáo sơ bộ / báo cáo đầy đủ / IC memo | `deals/<deal-id>/analysis/` | `<YYYYMMDD>_<loại>_<deal-id>.md` |
| FS model | `deals/<deal-id>/analysis/` | `FS_<TenDuAn>_<YYYYMMDD>.xlsx` |
| Legal memo / issue list / hybrid package | `deals/<deal-id>/legal/` | `<YYYYMMDD>_<loại>.md` |
| LOI / offer | `deals/<deal-id>/correspondence/` | `<YYYYMMDD>_LOI_<deal-id>.md` |
| Báo cáo thị trường định kỳ (ngoài deal) | `outputs/` hoặc cấu trúc riêng của `re-rnd` | theo skill tương ứng |

## Quy tắc

1. **Mọi skill deal-lifecycle đọc `_dossier.md` khi bắt đầu, cập nhật khi kết thúc** (trạng thái giai đoạn, assumption mới chốt, findings, nhật ký phiên).
2. Không lưu dữ liệu deal, credentials hoặc tri thức nội bộ vào thư mục plugin.
3. Database dự án thị trường của `re-rnd` là một **vault Obsidian riêng** (đường dẫn khai báo ở key `market_research_vault` trong `re-workspace.yaml`); cấu trúc vault theo `../skills/re-rnd/references/vault-layout.md`.
4. Không gửi nội dung workspace ra dịch vụ ngoài nếu Sếp chưa duyệt (xem `operating-contract.md`).
