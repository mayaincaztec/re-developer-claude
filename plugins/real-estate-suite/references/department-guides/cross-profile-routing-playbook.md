# Cross-Profile Routing Playbook

## Purpose
Tài liệu này chuẩn hóa cách `RE-HQ` và các specialist profiles phối hợp với nhau trong hệ thống của Sếp.

## Golden rules
1. Profile là boundary dài hạn cho memory/skills/workflow.
2. Subagent là executor ngắn hạn cho từng task.
3. Không tạo profile mới chỉ để xử lý một tác vụ nhỏ lẻ.
4. Nếu một profile đã đủ phù hợp, ưu tiên route đúng profile thay vì trả lời lan sang domain khác.
5. Luôn giữ xưng hô: em — Sếp.

## Canonical routing map

Bảng routing chi tiết (department scope, route triggers theo từng phòng, cơ chế điều phối trên Claude, escalation) nằm ở `../routing-map.md` — single source of truth. File này chỉ giữ các nguyên tắc phối hợp và handoff bên dưới.

## Standard handoff packet
Khi giao từ profile này sang profile khác, packet tối thiểu nên gồm:
- objective
- scope
- facts already known
- assumptions
- requested output format
- level of urgency

## Suggested final deliverable owners
- cross-functional memo -> `RE-HQ`
- legal memo -> `RE-Legal`
- market note -> `RE-Market-Research`
- investment recommendation -> `RE-Investment-Finance`
- concept/design brief -> `RE-Project-Design`

## Escalation
Nếu specialist profile thấy task đã vượt domain:
1. nêu rõ vì sao vượt phạm vi
2. đề xuất route tiếp theo
3. giữ lại phần kết luận trong domain của mình
