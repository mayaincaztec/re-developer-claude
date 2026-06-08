# RE Developer Suite Operating Contract

## Handoff packet

Every delegated workstream must state:

- objective and decision to support;
- scope and explicit exclusions;
- facts and documents already available;
- assumptions already approved;
- requested deliverable and level of detail;
- urgency and materiality;
- workspace paths the specialist may read or write.

## Finding schema

Use this schema for material findings:

```text
Finding ID:
Status: confirmed | inferred | assumed | unresolved
Fact and source:
Issue:
Severity: critical | high | medium | low
Investment/design implication:
Missing information:
Recommended action:
Owner:
Last updated: YYYY-MM-DD
```

Never upgrade an inference or assumption into a confirmed fact.

## Source rules

- Cite workspace documents by path and, where useful, page or section.
- For current external facts, use verifiable sources and record the access date.
- Legal conclusions require current primary legal sources where available.
- Market listing data is indicative, not an executed transaction price.
- Do not send private workspace contents to external tools unless the user explicitly authorizes it.

## Escalation

Return work to RE-HQ when the decision requires multiple departments, a multi-owner tracker, transaction architecture, or an integrated recommendation.

## Output language (ngôn ngữ đầu ra)

Tách **ngôn ngữ làm việc** khỏi **ngôn ngữ deliverable**:

- **Ngôn ngữ làm việc** của skill (phân tích, lập luận, SOP) luôn là **tiếng Việt**.
- **Ngôn ngữ deliverable** theo thứ tự ưu tiên: (1) Sếp yêu cầu rõ; (2) ngôn ngữ của bối cảnh chi phối — vd hợp đồng/SPA bản tiếng Anh → memo/redline tiếng Anh; tài liệu nộp cơ quan VN → tiếng Việt; (3) mặc định **tiếng Việt**.
- Hỗ trợ **song ngữ** khi một bên là tổ chức/cá nhân VN cần bản tiếng Việt, hoặc khi Sếp yêu cầu.
- Khi xuất deliverable tiếng Anh: giữ văn phong chuyên nghiệp tiếng Anh (không dịch máy từ tiếng Việt); thuật ngữ pháp lý/giao dịch dùng đúng chuẩn tiếng Anh. Lưu ý: khi có mâu thuẫn bản Việt–Anh trong hợp đồng, bản tiếng Việt thường được ưu tiên tại tòa Việt Nam → nêu rõ controlling language.
- Tên skill và `description` luôn giữ tiếng Anh (phục vụ trigger), độc lập với ngôn ngữ deliverable.
