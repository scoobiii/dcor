# DCOR — Optimasi & Pengurangan Konsumsi Data Center

**[English](../../README.md) | [Português](README.pt-br.md) | [Español](README.es.md) | [Français](README.fr.md) | [日本語](README.ja.md) | [简体中文](README.zh.md) | [한국어](README.ko.md) | [Tiếng Việt](README.vi.md) | Bahasa Indonesia | [Italiano](README.it.md)**

**Hubungkan. Ukur. Simulasikan. Optimalkan. Verifikasi.**

DCOR adalah platform vendor-neutral untuk mengoptimalkan energi, pendinginan, biaya, karbon, dan operasi data center.

> **SCADA menampilkan. DCIM mengorganisasi. BMS mengendalikan. DCOR menjelaskan, mensimulasikan, mengoptimalkan, dan memverifikasi.**

## Identitas

### Otto — maskot DCOR

![Otto — DCOR mascot](../../assets/dcor-mascot.svg)

Otto adalah berang-berang? Tidak — Otto adalah **berang-berang laut (otter)**. Ia mewakili penggunaan air yang efisien, adaptasi, observabilitas, pendinginan, ketahanan, dan optimasi dengan batasan. **Otto mengamati sebelum bertindak, mengoptimalkan dalam batasan, dan memverifikasi hasil.**

## Prinsip arsitektur

DCOR tidak menggantikan SCADA, BMS, DCIM, atau EPMS. Data masuk melalui connector, dinormalisasi ke Canonical Data Model, lalu diteruskan ke Twin, Analytics, Optimization, dan Verification. Dashboard adalah konsumen kontrak data, bukan titik awal.

## Strategi multi-bahasa

DCOR menggunakan strategi **polyglot berdasarkan boundary**. Bahasa dipilih berdasarkan runtime, protokol, memori, latensi, determinisme, dan target deployment.

| Lapisan | Pilihan utama | Alternatif |
|---|---|---|
| Canonical model / domain | Python | Go, Rust |
| Connector | Python | Go, Rust |
| Edge / memori rendah | Go | Rust, Python |
| Protokol/perangkat performa tinggi | Rust | Go, C/C++ |
| Industri / legacy | C/C++ | Rust, Python |
| Sains / riset | Python | Julia |
| Optimisasi / ML | Python | Julia, Rust/C++ |
| API | Python | Go, Rust |
| Web | TypeScript | JavaScript |
| Firmware | C/C++ / Rust | — |

Jangan menulis ulang Python yang sudah bekerja hanya untuk menambah jumlah bahasa. Bahasa baru hanya diperkenalkan jika memberikan keuntungan yang dapat diukur.

## Pengembangan

```sh
./scripts/bootstrap.sh
./scripts/test.sh
```

Local gate dan CI gate menggunakan jalur validasi yang sama; target coverage package adalah **100%**.

## Roadmap S0–S11

`PLANNED → IN PROGRESS → CI VALIDATED → DONE`

S0 baseline/CI → S1 arsitektur/kontrak → S2 Connector SDK → S3 Frontier → S4 NLR/DOE → S5 CSV/Parquet → S6 MQTT/REST → S7 Twin/Baseline → S8 optimisasi → S9 DQN/RL → S10 verifikasi/kontrol → S11 SaaS/produksi.

## Urutan optimisasi

**baseline → rules → PID/MPC/MILP → DQN → Double/Dueling DQN → PPO/SAC**

## Dokumentasi

- [Architecture](../../ARCHITECTURE.md)
- [Standards](../../STANDARDS.md)
- [Backlog](../../BACKLOG.md)
- [Development](../DEVELOPMENT.md)
- [Compatibility](../COMPATIBILITY.md)
- [Delivery Manifest](../DELIVERY_MANIFEST.md)

**Status:** fondasi S0/S1/S2 sedang berjalan; S3 Frontier adalah milestone berikutnya setelah gate tervalidasi.
