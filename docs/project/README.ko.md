# DCOR — 데이터센터 최적화 및 절감

**[English](../../README.md) | [Português](README.pt-br.md) | [Español](README.es.md) | [Français](README.fr.md) | [日本語](README.ja.md) | [简体中文](README.zh.md) | 한국어 | [Tiếng Việt](README.vi.md) | [Bahasa Indonesia](README.id.md) | [Italiano](README.it.md)**

**연결. 측정. 시뮬레이션. 최적화. 검증.**

DCOR는 데이터센터의 에너지, 냉각, 비용, 탄소 및 운영을 최적화하기 위한 벤더 중립적 플랫폼입니다.

> **SCADA는 보여준다. DCIM은 정리한다. BMS는 제어한다. DCOR는 설명하고, 시뮬레이션하고, 최적화하고, 검증한다.**

## 정체성

### Otto — DCOR 마스코트

![Otto — DCOR mascot](../../assets/dcor-mascot.svg)

Otto는 수달입니다. 물의 효율적 사용, 적응력, 관측 가능성, 냉각, 회복탄력성 및 제약 조건 내 최적화를 상징합니다. **Otto는 행동하기 전에 관찰하고, 제약 조건 안에서 최적화하며, 결과를 검증합니다.**

## 아키텍처 원칙

DCOR는 SCADA, BMS, DCIM 또는 EPMS를 대체하지 않습니다. 커넥터를 통해 데이터를 수집하고, 정규화된 Canonical Data Model로 변환한 뒤 Twin, Analytics, Optimization 및 Verification으로 전달합니다. 대시보드는 이 계약의 소비자이며 시작점이 아닙니다.

## 다중 언어 전략

DCOR는 **경계별 polyglot** 전략을 사용합니다. 언어는 이념이 아니라 런타임, 프로토콜, 메모리, 지연 시간, 결정성 및 배포 환경에 따라 선택합니다.

| 계층 | 기본 언어 | 대안 |
|---|---|---|
| Canonical model / domain | Python | Go, Rust |
| Connector | Python | Go, Rust |
| Edge / 저메모리 | Go | Rust, Python |
| 고성능 프로토콜/디바이스 | Rust | Go, C/C++ |
| 산업/레거시 | C/C++ | Rust, Python |
| 과학/연구 | Python | Julia |
| 최적화/ML | Python | Julia, Rust/C++ |
| API | Python | Go, Rust |
| Web | TypeScript | JavaScript |
| Firmware | C/C++ / Rust | — |

작동하는 Python을 단순히 언어 수를 늘리기 위해 Go나 Rust로 다시 작성하지 않습니다. 새로운 언어는 측정 가능한 이점이 있을 때만 도입합니다.

## 개발

```sh
./scripts/bootstrap.sh
./scripts/test.sh
```

로컬 게이트와 CI 게이트는 동일한 검증 경로를 사용하며 패키지 커버리지 목표는 **100%**입니다.

## 로드맵 S0–S11

`PLANNED → IN PROGRESS → CI VALIDATED → DONE`

S0 기반/CI → S1 아키텍처/계약 → S2 Connector SDK → S3 Frontier → S4 NLR/DOE → S5 CSV/Parquet → S6 MQTT/REST → S7 Twin/Baseline → S8 최적화 → S9 DQN/RL → S10 검증/제어 → S11 SaaS/프로덕션.

## 최적화 순서

**baseline → rules → PID/MPC/MILP → DQN → Double/Dueling DQN → PPO/SAC**

## 문서

- [Architecture](../../ARCHITECTURE.md)
- [Standards](../../STANDARDS.md)
- [Backlog](../../BACKLOG.md)
- [Development](../DEVELOPMENT.md)
- [Compatibility](../COMPATIBILITY.md)
- [Delivery Manifest](../DELIVERY_MANIFEST.md)

**상태:** S0/S1/S2 기반 작업 진행 중. 다음 주요 단계는 gate 검증 후 S3 Frontier입니다.
