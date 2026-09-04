# DCOR — Tối ưu hóa & Giảm tiêu thụ năng lượng Trung tâm Dữ liệu

**[English](../../README.md) | [Português](README.pt-br.md) | [Español](README.es.md) | [Français](README.fr.md) | [日本語](README.ja.md) | [简体中文](README.zh.md) | [한국어](README.ko.md) | Tiếng Việt | [Bahasa Indonesia](README.id.md) | [Italiano](README.it.md)**

**Kết nối. Đo lường. Mô phỏng. Tối ưu. Xác minh.**

DCOR là nền tảng trung lập với nhà cung cấp để tối ưu hóa năng lượng, làm mát, chi phí, carbon và vận hành trung tâm dữ liệu.

> **SCADA hiển thị. DCIM tổ chức. BMS điều khiển. DCOR giải thích, mô phỏng, tối ưu và xác minh.**

## Nhận diện

### Otto — linh vật DCOR

![Otto — DCOR mascot](../../assets/dcor-mascot.svg)

Otto là rái cá, đại diện cho việc sử dụng nước hiệu quả, khả năng thích nghi, khả năng quan sát, làm mát, khả năng phục hồi và tối ưu hóa có ràng buộc. **Otto quan sát trước khi hành động, tối ưu trong các ràng buộc và xác minh kết quả.**

## Nguyên tắc kiến trúc

DCOR không thay thế SCADA, BMS, DCIM hoặc EPMS. Dữ liệu đi qua các connector, được chuẩn hóa thành Canonical Data Model, sau đó mới đến Twin, Analytics, Optimization và Verification. Dashboard chỉ là bên tiêu thụ hợp đồng dữ liệu và không phải điểm khởi đầu.

## Chiến lược đa ngôn ngữ

DCOR áp dụng chiến lược **polyglot theo ranh giới**. Ngôn ngữ được chọn dựa trên runtime, giao thức, bộ nhớ, độ trễ, tính xác định và môi trường triển khai.

| Lớp | Ưu tiên | Thay thế |
|---|---|---|
| Canonical model / domain | Python | Go, Rust |
| Connector | Python | Go, Rust |
| Edge / bộ nhớ thấp | Go | Rust, Python |
| Giao thức/thiết bị hiệu năng cao | Rust | Go, C/C++ |
| Công nghiệp / legacy | C/C++ | Rust, Python |
| Khoa học / nghiên cứu | Python | Julia |
| Optimization / ML | Python | Julia, Rust/C++ |
| API | Python | Go, Rust |
| Web | TypeScript | JavaScript |
| Firmware | C/C++ / Rust | — |

Không viết lại Python đang hoạt động chỉ để tăng số lượng ngôn ngữ. Ngôn ngữ mới chỉ được thêm khi có lợi ích đo được.

## Phát triển

```sh
./scripts/bootstrap.sh
./scripts/test.sh
```

Local gate và CI gate dùng cùng một đường dẫn kiểm thử; mục tiêu coverage của package là **100%**.

## Lộ trình S0–S11

`PLANNED → IN PROGRESS → CI VALIDATED → DONE`

S0 nền tảng/CI → S1 kiến trúc/hợp đồng → S2 Connector SDK → S3 Frontier → S4 NLR/DOE → S5 CSV/Parquet → S6 MQTT/REST → S7 Twin/Baseline → S8 tối ưu hóa → S9 DQN/RL → S10 xác minh/điều khiển → S11 SaaS/sản xuất.

## Thứ tự tối ưu hóa

**baseline → rules → PID/MPC/MILP → DQN → Double/Dueling DQN → PPO/SAC**

## Tài liệu

- [Architecture](../../ARCHITECTURE.md)
- [Standards](../../STANDARDS.md)
- [Backlog](../../BACKLOG.md)
- [Development](../DEVELOPMENT.md)
- [Compatibility](../COMPATIBILITY.md)
- [Delivery Manifest](../DELIVERY_MANIFEST.md)

**Trạng thái:** nền tảng S0/S1/S2 đang được triển khai; S3 Frontier là mốc tiếp theo sau khi gate được xác minh.
