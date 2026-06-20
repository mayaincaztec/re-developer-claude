# Routing Map

> **Single source of truth for routing.** Mọi tài liệu khác (`re-hq` skill, các operating guide, cross-profile routing playbook) chỉ trỏ về file này, không lặp lại bảng routing để tránh lệch.

## Department scope

| Department | Primary scope |
|---|---|
| RE-HQ | Executive-level cross-department synthesis, ambiguous intake, final integrated recommendation, conflict arbitration |
| RE-Legal | Project legal status, land, planning, permits, compliance, contracts and legal risk |
| RE-Investment-Finance | **Owns the full deal lifecycle**: screening, preliminary & full investment reports, feasibility study (FS), underwriting, scenarios, IC memos, deal structuring + LOI, and DD coordination |
| RE-Market-Research | Area studies, competitors, pricing, supply-demand, pipeline and market thesis |
| RE-Project-Design | Benchmarks, product mix, positioning, concept and consultant briefs, 1/500 planning-indicator calculation and design review |

RE-HQ owns executive integrated deliverables and arbitrates cross-department conflicts. A specialist owns conclusions inside its domain. The deal lifecycle (screening → FS → reports → structuring/LOI → DD → IC) is owned by RE-Investment-Finance, which pulls Legal and Market as specialist inputs.

## Route triggers

**→ RE-Legal** khi có: title / ownership / legal DD; permits / approvals / compliance; zoning / land use / planning; contract review / clause risk / transaction-structure legal risk.

**→ RE-Market-Research** khi có: comps / pricing / supply-demand; area study / competitor scan; pipeline / launch / market movement; market thesis từ dữ liệu công khai. Database dự án VN, scan giá thứ cấp và báo cáo thị trường dùng skill `re-rnd`.

**→ RE-Investment-Finance** khi có: screening deal đầu vào; báo cáo đầu tư (sơ bộ / đầy đủ); feasibility study (FS); underwriting / scenario / risk-return; IC memo / recommendation; **deal structuring + LOI**; **điều phối DD**. Đây là phòng sở hữu toàn bộ deal lifecycle, kéo Legal/Market làm input.

**→ RE-Project-Design** khi có: concept brief / benchmark project; program mix / positioning implication; consultant brief / design option framing.

**Giữ ở RE-HQ** khi: task còn mơ hồ chưa rõ phòng nào; cần tổng hợp đa phòng ở tầm executive; cần trọng tài khi các phòng xung đột; cần memo tích hợp cuối cho cấp quyết định cao nhất. (Deal lifecycle KHÔNG giữ ở RE-HQ — thuộc RE-Investment-Finance.)

## Cơ chế điều phối trên Claude Code / Cowork

Trên runtime này, 5 "phòng ban" là **skills cùng cấp**, không phải agent riêng. RE-HQ (và RE-Investment-Finance với deal lifecycle) điều phối bằng một trong hai cách:

1. **Sequential skill loading** (mặc định) — load tuần tự skill phòng ban / sub-skill cần dùng, tự tổng hợp kết quả.
2. **Subagents qua `Agent` tool** — chỉ khi Sếp yêu cầu chạy song song / nhiều phòng ban cùng lúc. Plugin định nghĩa sẵn 4 agent phòng ban trong `agents/`: `re-legal`, `re-rnd`, `re-project`, `re-inv` — spawn đúng agent theo workstream; mỗi subagent nhận handoff packet trong `operating-contract.md` và trả distilled findings theo finding schema.

Không cần bước cài đặt riêng — skills và agents được Claude tự quét khi cài plugin. Ngoài ra có các slash command vào thẳng workflow: `/re-screen`, `/re-fs`, `/re-dd`, `/re-status`.

## Escalation

Khi một specialist thấy task vượt domain của mình:
1. nêu rõ vì sao vượt phạm vi;
2. đề xuất route tiếp theo;
3. giữ lại phần kết luận trong domain của mình và trả phần điều phối về owner phù hợp.

DD coordination → `re-inv-dd-coordinator`; deal structuring / transaction architecture + LOI → `re-inv-deal-structuring`. **Cả hai là workflow của RE-Investment-Finance** (deal lifecycle owner), kéo RE-Legal cho legal findings. Chỉ route RE-HQ khi cần quyết định đa phòng cấp executive.
