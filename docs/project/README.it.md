# DCOR — Ottimizzazione e Riduzione dei Data Center

**[English](../../README.md) | [Português](README.pt-br.md) | [Español](README.es.md) | [Français](README.fr.md) | [日本語](README.ja.md) | [简体中文](README.zh.md) | [한국어](README.ko.md) | [Tiếng Việt](README.vi.md) | [Bahasa Indonesia](README.id.md) | Italiano**

**Connettere. Misurare. Simulare. Ottimizzare. Verificare.**

DCOR è una piattaforma vendor-neutral per l'ottimizzazione dell'energia, del raffreddamento, dei costi, del carbonio e delle operazioni dei data center.

> **SCADA mostra. DCIM organizza. BMS controlla. DCOR spiega, simula, ottimizza e verifica.**

## Identità

### Otto — la mascotte di DCOR

![Otto — DCOR mascot](../../assets/dcor-mascot.svg)

Otto è una lontra: rappresenta l'uso efficiente dell'acqua, l'adattabilità, l'osservabilità, il raffreddamento, la resilienza e l'ottimizzazione sotto vincoli. **Otto osserva prima di agire, ottimizza entro i vincoli e verifica il risultato.**

## Principi architetturali

DCOR non sostituisce SCADA, BMS, DCIM o EPMS. I dati entrano attraverso connector, vengono normalizzati nel Canonical Data Model e quindi passano a Twin, Analytics, Optimization e Verification. La dashboard è un consumatore del contratto dati, non il punto di partenza.

## Strategia multilingue

DCOR adotta una strategia **polyglot per boundary**. Il linguaggio viene scelto in base a runtime, protocollo, memoria, latenza, determinismo e ambiente di deployment.

| Livello | Preferito | Alternative |
|---|---|---|
| Canonical model / dominio | Python | Go, Rust |
| Connector | Python | Go, Rust |
| Edge / bassa memoria | Go | Rust, Python |
| Protocollo/dispositivo ad alte prestazioni | Rust | Go, C/C++ |
| Industriale / legacy | C/C++ | Rust, Python |
| Scienza / ricerca | Python | Julia |
| Ottimizzazione / ML | Python | Julia, Rust/C++ |
| API | Python | Go, Rust |
| Web | TypeScript | JavaScript |
| Firmware | C/C++ / Rust | — |

Non riscriviamo Python funzionante solo per aumentare il numero di linguaggi. Un nuovo linguaggio viene introdotto solo quando offre un vantaggio misurabile.

## Sviluppo

```sh
./scripts/bootstrap.sh
./scripts/test.sh
```

Il gate locale e il gate CI utilizzano lo stesso percorso di validazione; l'obiettivo di coverage del package è **100%**.

## Roadmap S0–S11

`PLANNED → IN PROGRESS → CI VALIDATED → DONE`

S0 baseline/CI → S1 architettura/contratti → S2 Connector SDK → S3 Frontier → S4 NLR/DOE → S5 CSV/Parquet → S6 MQTT/REST → S7 Twin/Baseline → S8 ottimizzazione → S9 DQN/RL → S10 verifica/controllo → S11 SaaS/produzione.

## Ordine dell'ottimizzazione

**baseline → rules → PID/MPC/MILP → DQN → Double/Dueling DQN → PPO/SAC**

## Documentazione

- [Architecture](../../ARCHITECTURE.md)
- [Standards](../../STANDARDS.md)
- [Backlog](../../BACKLOG.md)
- [Development](../DEVELOPMENT.md)
- [Compatibility](../COMPATIBILITY.md)
- [Delivery Manifest](../DELIVERY_MANIFEST.md)

**Stato:** fondazione S0/S1/S2 in corso; S3 Frontier è il prossimo milestone dopo la validazione del gate.
