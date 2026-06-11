# Pricing Protocol — quy tắc đọc và ghi giá

> **Bắt buộc đọc trước mọi thao tác giá** (P1 bước 6, P2 toàn bộ). Tổng quát hóa từ Pricing Playbook thực chiến; bản playbook theo từng cụm nằm ở `reports/playbooks/` trong vault.

## 3 câu hỏi trước khi ghi bất kỳ con số nào

1. Đang nói tới **phase / block / cấu phần nào**?
2. Đang nói tới **sơ cấp hay thứ cấp**?
3. Đang nói tới **giá theo căn, theo lô hay theo m² (đất / sàn)**?

Chưa trả lời đủ 3 câu → chưa được ghi giá.

## 4 loại giá (không trộn)

| Loại | Là gì | Độ tin |
|---|---|---|
| **MBS sơ cấp** | giá CĐT công bố (rổ hàng, bảng giá) | cao về niêm yết, không phải giá giao dịch |
| **Asking thứ cấp** | giá rao trên listing | indicative — ghi số mẫu tin |
| **Chuyển nhượng thực** | giá khớp thực tế (môi giới, hợp đồng) | cao nhất, hiếm |
| **Khảo sát thực địa** | ghi nhận tại chỗ / sales nói | trung bình, ghi rõ bối cảnh |

Luôn ghi loại giá + diện tích tham chiếu + nguồn + ngày bên cạnh con số.

## Đơn vị phân tích (unit of analysis)

Chọn đơn vị **nhỏ nhất mà dữ liệu phân hóa**, theo thang:

```
toàn dự án → phase/phân khu → block/tòa → dòng sản phẩm → loại căn/lô → vị trí (góc/mặt đường/view/tầng)
```

Cú pháp chuẩn khi note giá: `[Phase] — [dòng sản phẩm] — [DT] — [giá/đơn giá] — [loại giá, nguồn, ngày]`.

## Anchor price vs average

- `gia_tb_*` trong frontmatter **chỉ fill khi một mặt bằng chung là hợp lệ** — dữ liệu không phân hóa mạnh theo phase/block/vị trí.
- Khi dữ liệu chưa sạch hoặc phân hóa: dùng **anchor price** (giá neo theo cấu phần, ghi trong bảng body 5A–5E) và để `gia_tb_*` = `null` + lý do. Một average giả tệ hơn không có số.

## Rule đọc giá theo 6 nhóm dự án

1. **Đất nền / lowrise market-driven** (vd HUD, Mega City 2): tách trục chính / nội khu / lô góc / lô thường / lộ giới; ưu tiên `gia_don_vi_dat_nen`; không lấy một lô đẹp đại diện cả dự án.
2. **Phase-project** (vd Swan Bay, King Bay): đơn vị tối thiểu là **phase**, sau phase mới tách dòng sản phẩm; không benchmark toàn dự án; dùng phase-sheet (template trong report-catalog) làm working sheet.
3. **Apartment / highrise**: đơn vị tối thiểu là **loại căn / block / view / tầng**; headline price chỉ là lớp ngoài.
4. **Mixed-use sơ cấp mới**: tách riêng apartment / nhà phố / shophouse; không average chung; thiếu block/phase thì chỉ anchor sơ cấp theo cấu phần.
5. **Multi-component / nhạy cấu trúc pháp lý** (có NOXH / tái định cư / thương mại lẫn nhau): tách theo cấu phần pháp lý trước khi bàn giá; chưa tách được thì không benchmark.
6. **Dự án đơn giản single-product**: được phép average, vẫn ghi range min–max + số mẫu.

## Trình tự update giá (mỗi dự án)

1. Chốt đơn vị phân tích (nhìn nhóm dự án ở trên + playbook cụm nếu có).
2. Thu thập theo đơn vị đó; ghi loại giá + DT + nguồn + ngày + số mẫu.
3. Cập nhật bảng giá **body** (5A–5E) — đây là nơi giữ sự thật chi tiết.
4. Cân nhắc frontmatter: đủ chắc → fill `gia_tb_*`/`min`/`max`; không → anchor + null + lý do.
5. `nguon_gia`, `ngay_cap_nhat_gia`, `ngay_cap_nhat`; biến động >5% → "Lịch sử Cập nhật".

## Sai lầm cấm

- Dùng giá sản phẩm đẹp nhất (villa ven sông, lô mặt tiền) đại diện cả phase/dự án.
- Dùng headline sơ cấp làm giá giao dịch thực.
- Gộp NOXH/tái định cư vào mặt bằng giá thương mại.
- Fill `gia_tb_*` để "cho đủ field" khi dữ liệu đang phân hóa.
- Lấy 1–2 listing kết luận cả thị trường; quên ghi ngày truy cập.
