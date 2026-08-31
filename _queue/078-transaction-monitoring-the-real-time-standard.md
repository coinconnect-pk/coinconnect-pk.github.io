---
layout: post
title: "Transaction Monitoring: The Real-Time Standard"
date: 2026-01-01 09:00:00 +0500
categories: [Compliance]
author: "Malik Abbas"
description: "Regulation 11.1 of the NOC Regulations requires VASPs to detect suspicious activity in real time or near real time. What that standard means for systems."
---

Most [anti-money laundering](https://www.coinconnect.site/blog/3/fit-and-proper-aml-pvara-mistakes-54) rules tell a business what to report and when to report it. Regulation 11.1 of the [PVARA](https://www.coinconnect.site/pvara-guide) [No Objection Certificate](https://www.coinconnect.site/regulatory-licensing) Regulations 2025 does something narrower and more demanding: it fixes the speed at which a [virtual asset service provider](https://www.coinconnect.site/blog/coinconnect-insights-1/vasp-license-pakistan-3) ("VASP") has to notice a problem in the first place.

This article reads Regulation 11.1 as published, sets out what "real time or near real time" actually requires of a monitoring system, and connects it to the reporting and readiness obligations that sit either side of it in the same Regulations.

## What does Regulation 11.1 actually require?

Every applicant granted AML Registration must run a monitoring system capable of catching suspicious or unusual activity as it happens, not after the fact. Regulation 11.1 states:

> "Each Applicant shall maintain monitoring systems capable of detecting suspicious or unusual activity in real time or near real time."

Three elements sit inside that single sentence. First, the obligation attaches to "monitoring systems" — plural, and a technical capability, not a policy document. Second, the detection standard is speed-based: activity has to be flagged as it occurs, or close to it, rather than surfaced during a periodic batch review days or weeks later. Third, the standard covers both "suspicious" and "unusual" activity — two overlapping but distinct categories, since not everything that looks unusual is necessarily suspicious, and a system built only to flag textbook suspicious patterns may miss the wider "unusual" activity the Regulation also requires it to catch.

## What does "real time or near real time" mean in practice?

The Regulations do not define either term numerically — no stated latency, no maximum delay in minutes or hours. Read against ordinary usage in transaction monitoring, "real time" means detection that occurs as the transaction is processed or immediately afterward, while "near real time" allows for a short, operationally necessary lag — the time a monitoring engine takes to ingest a transaction, run it against rule sets or models, and raise an alert. What the phrase excludes is clearer than what it precisely permits: a system that only reviews transaction data in a daily, weekly or monthly batch does not meet either standard, because by the time a batch job runs, the transaction has already settled and any funds involved may have moved again.

In practice, this pushes VASPs toward monitoring architecture that sits inline with, or immediately adjacent to, the transaction flow itself — screening at the point a transaction is initiated or confirmed, rather than monitoring built as a downstream reporting exercise. Our reading is that a monitoring system justified to PVARA purely as a periodic reconciliation process would struggle to meet Regulation 11.1's wording, though the Regulations leave the precise permissible lag to the applicant's own risk-based design and to PVARA's supervisory judgement on inspection.

## Why does the speed of detection matter this much under Pakistan's framework?

Because detection speed is the input the rest of the reporting chain depends on. Regulation 11.1 does not stand alone — it is the first of six provisions in Part 4 of the NOC Regulations dealing with monitoring, Suspicious Transaction Reports ("STRs"), Currency Transaction Reports ("CTRs") and [goAML](https://www.coinconnect.site/blog/coinconnect-insights-1/fmu-goaml-vasp-pakistan-17), the reporting platform run by Pakistan's Financial Monitoring Unit ("FMU").

| Regulation | What it covers |
|---|---|
| 11.1 | Real-time or near-real-time monitoring systems |
| 11.2 | STR filing in accordance with the Anti-Money Laundering Act, 2010 |
| 11.3 | CTR filing for fiat transactions meeting or exceeding the applicable threshold |
| 11.4 | Foreign entity registers on goAML following NOC issuance |
| 11.5 | Reporting role transfers to the local entity once licensed |
| 11.6 | Technical readiness to file STRs and CTRs immediately upon goAML registration |

A monitoring system that only detects activity after settlement cannot, by definition, support the "immediately upon" filing readiness Regulation 11.6 demands, because there is nothing yet to file. Regulation 11.1's real-time standard is therefore the foundation the rest of Part 4 is built on — weaken it and every downstream obligation in the chain becomes slower than the Regulations intend.

## What has to be in place to demonstrate compliance with Regulation 11.1?

Two Annex A forms give the clearest picture of what PVARA expects an applicant to show. Form A1, Section 6.2, requires the applicant to describe and, where appropriate, list all systems used for blockchain analytics, identity verification, sanctions and targeted financial sanctions screening, transaction monitoring and case management, and data storage, backup and archival. Section 6.3 then asks the applicant to confirm system readiness on a three-point scale: fully operational, in testing phase, or under implementation with an expected completion date.

Form A4, the AML/CFT Framework Submission Statement signed jointly by the Chief Executive Officer and the Money Laundering Reporting Officer ("MLRO"), requires confirmation that the applicant's AML-relevant systems — including transaction monitoring software and blockchain analytics tools — are "implemented, tested and operational". Declaring a system "under implementation" on Form A1 while separately confirming full operational readiness on Form A4 is the kind of inconsistency an assessor is positioned to catch, since both forms are submitted as part of the same application package.

- **A documented alert-generation methodology** — the scenarios, thresholds and typologies the system screens for, referenced in Form A1's technology section.
- **Evidence of latency**, however the applicant chooses to measure it — logs, testing results, or vendor specifications showing how quickly a transaction generates an alert once processed.
- **A case management and escalation workflow** feeding from the monitoring system into the internal suspicious activity reporting process, which Form A7 sets a minimum structure for.
- **A record of who reviews alerts and how quickly**, since a system that detects in real time but routes alerts into an unstaffed queue does not, in substance, deliver real-time protection.

## How does the real-time standard interact with outsourced monitoring?

Regulation 14.1 of the NOC Regulations treats transaction monitoring as an AML-critical function that may not be outsourced unless the applicant conducts due diligence on the service provider, maintains effective oversight arrangements, retains audit and inspection rights, and ensures those rights are legally enforceable, including across borders. A VASP that buys in a third-party monitoring platform or managed service therefore does not step outside Regulation 11.1's real-time standard by doing so — the obligation to meet that standard, and to be able to demonstrate it to PVARA, stays with the applicant regardless of who operates the underlying technology. Form A5, the Outsourcing Declaration and Register, requires the applicant to record the monitoring frequency it applies to each outsourced arrangement, which gives PVARA a direct line of sight into whether an outsourced monitoring function is actually being supervised at the pace the Regulation requires, rather than left to the vendor's own reporting cadence.

## What are the consequences of a monitoring system that falls short of the standard?

A monitoring gap sits inside the broader grounds on which PVARA can revoke a registered applicant's NOC and AML Registration status. Regulation 19.1(d) lists "systemic or material AML/CFT failures" as a revocation ground, applied proportionately under Regulation 19.2, having regard to the severity and impact of the breach. A monitoring system that detects suspicious activity only after settlement, rather than in real time or near real time, is a plausible candidate for that category, though the Regulations do not spell out where the line sits between an isolated technical shortfall and a systemic failure — that judgement rests with PVARA on the facts of a given case.

Separately, Regulation 8.2(d) requires "transaction monitoring processes" as one of the minimum components of the wider AML/CFT framework every applicant must maintain, and Regulation 18.1(a) makes [ongoing compliance](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-phase-2-compliance-failure-11) with all AML/CFT obligations — which necessarily includes Regulation 11.1 — a continuing duty of a registered applicant, not a one-off condition satisfied at the point of NOC approval. For the reporting obligations that a properly functioning monitoring system feeds into, see our companion pieces on [goAML registration](https://www.coinconnect.site/blog/coinconnect-insights-1/fmu-goaml-vasp-pakistan-17) and on the wider [regulatory and licensing](https://www.coinconnect.site/regulatory-licensing) process this sits within.

## Related reading

- [PVARA Exchange License: Capital, Rules & Obligations 2026](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-exchange-license-requirements-capital-obligations-24)
- [PVARA Transfer & Settlement License: Crypto Payments 2026](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-transfer-settlement-license-payments-remittance-28)

## About this analysis

This analysis was prepared by the CoinConnect research desk from Regulations 8.2(d), 11.1 through 11.6, 14.1, 18.1(a) and 19.1(d) of the PVARA No Objection Certificate Regulations 2025, together with Forms A1, A4, A5 and A7 at Annex A, read as published. Where practice is not yet settled or guidance has not been issued, that is stated in the text above.

Regulatory positions change and specific requirements should be verified against the current position published by the relevant authority before you act on them. This is information and analysis, not legal advice, and it does not create an advisory relationship. Take professional advice on your own circumstances.

## Flags for Malik

1. Regulation 11.1 does not define "real time" or "near real time" numerically, and I have deliberately not invented a latency figure (minutes, hours, etc.) to fill that gap — the text genuinely leaves it open, and PVARA does not appear to have issued separate technical guidance in the source documents reviewed.
2. My description of "real time" versus "near real time" as distinct concepts is my own reading of ordinary technical usage, not a distinction the Regulations themselves draw out or define — flagging in case you want that framed more cautiously.
3. This calendar row shares source material (reg 11.1, 11.6) with the goAML-focused rows in this same batch (013 and, indirectly, any existing goAML articles). I have kept this piece's focus narrowly on the monitoring-system standard itself rather than the registration/handover story, to minimise overlap, but worth a final read-through alongside the other Compliance-category pieces before publishing.
