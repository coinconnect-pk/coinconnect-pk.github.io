---
layout: post
title: "STRs and CTRs: What VASPs Must File"
date: 2026-01-01 09:00:00 +0500
categories: [Compliance]
author: "Malik Abbas"
description: "Regulations 11.2, 11.3 and 11.6 of the NOC Regulations set two distinct report types a VASP must file, and the readiness test attached to both."
---

Pakistan's [virtual asset](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-license-pakistan-complete-guide-22) framework asks a registered business to file two different kinds of report to the Financial Monitoring Unit ("FMU"), triggered by two different things. Confusing the two, or treating them as a single reporting obligation, is an easy mistake for a team building out its compliance function for the first time.

This article separates the two report types the [PVARA](https://www.coinconnect.site/pvara-guide) [No Objection Certificate](https://www.coinconnect.site/regulatory-licensing) Regulations 2025 require, sets out what triggers each one, and explains the technical readiness standard that applies to both.

## What are the two report types a VASP must file?

Suspicious Transaction Reports ("STRs") and Currency Transaction Reports ("CTRs"). Regulation 11.2 and Regulation 11.3 of the NOC Regulations address them separately:

> "11.2 Applicants shall file STRs in accordance with AMLA 2010.
> 11.3 Applicants shall file CTRs for all fiat-based transactions that meet or exceed the applicable threshold."

Both provisions sit inside Part 4 of the Regulations, under the same heading — "Monitoring, STRs, CTRs, [goAML](https://www.coinconnect.site/blog/coinconnect-insights-1/fmu-goaml-vasp-pakistan-17)" — alongside the real-time monitoring standard in Regulation 11.1 and the goAML registration provisions in Regulations 11.4 to 11.6. They are grouped together because they are functionally connected, not because they are the same obligation.

## How does an STR differ from a CTR?

An STR is triggered by suspicion; a CTR is triggered by a threshold. That is the core distinction, and it changes what a compliance team is actually watching for.

| | Suspicious Transaction Report (STR) | Currency Transaction Report (CTR) |
|---|---|---|
| Trigger | Suspicion of money laundering, terrorist financing or related illicit activity | A fiat-based transaction meeting or exceeding the applicable threshold |
| Governing standard | Anti-Money Laundering Act, 2010 ("AMLA 2010") | Regulation 11.3, "applicable threshold" |
| Judgement required | Yes — a subjective assessment of suspicion | Largely mechanical — value-based trigger |
| Applies to | Any transaction type, virtual asset or fiat, where suspicion arises | Fiat-based transactions specifically |
| Filed via | goAML | goAML |

Regulation 11.2 does not restate AMLA 2010's own definition of what counts as suspicious — it requires filing "in accordance with" that separate statute, which sits outside the three source documents behind this analysis and should be consulted directly for its own detail on what triggers an STR. Regulation 11.3, by contrast, is a value-based trigger scoped specifically to "fiat-based transactions" — meaning it does not, on its own wording, appear to extend to purely virtual-asset-to-virtual-asset transfers that never touch fiat currency. The Regulations do not state the threshold figure itself; that is set elsewhere and should be verified against FMU's published position before it is relied on operationally.

## Why does Regulation 11.3 limit the CTR trigger to "fiat-based transactions"?

Because a currency transaction report is, by its nature, about currency — legal tender — rather than about virtual assets as such. The Regulations' Regulation 11.3 language tracks that distinction directly, scoping CTR filing to fiat-based transactions that meet or exceed the applicable threshold, rather than to virtual asset transactions generally.

Our reading is that this leaves an open question the source documents do not resolve: whether a large virtual-asset-only transaction — one with no fiat leg at all — falls under the CTR regime, the STR regime (if suspicion independently arises), the Travel Rule obligations set out separately in the [Virtual Assets Act](https://blog.coinconnect.site/pakistans-virtual-assets-act-2026-the-complete-guide/), or none of the three unless a separate threshold rule is issued for virtual-asset-to-virtual-asset transfers. This is a gap in the published material, not a settled position, and it should be confirmed with FMU or PVARA directly rather than assumed either way.

## What technical readiness does PVARA expect before these reports can be filed?

Immediate capability, not a plan to build one. Regulation 11.6 sets a single readiness standard covering both report types:

> "The Applicant shall demonstrate technical readiness to file STRs and CTRs immediately upon goAML registration."

The word "immediately" removes any grace period from the text. An applicant is expected to be able to generate and submit both STRs and CTRs through the goAML platform from the moment its registration is granted — not to treat filing capability as a feature to be added once the business is already live and processing customer transactions.

Form A1, Section 7.1, asks the applicant to describe its internal STR/CTR workflow directly:

> "Briefly describe how internal suspicious activity will be escalated and submitted as STRs/CTRs via goAML once the Applicant has registered (or cross-reference the relevant section of the attached STR/CTR procedures)."

Form A4 restates the same readiness point as a signed declaration. The Chief Executive Officer and Money Laundering Reporting Officer ("MLRO") jointly confirm that the applicant has established "a functioning internal suspicious activity reporting mechanism", "a documented escalation process to the MLRO", and "technical capability for STR/CTR filing through the goAML platform".

## What internal process sits behind an STR before it is filed?

An internal escalation and determination step, evidenced through Form A7 — the Internal Suspicious Activity Report ("ISAR"). PVARA permits a VASP to use its own internal form, but sets the minimum content Form A7 must capture:

- Reporter details — name, position, date of the report.
- Customer details — customer name or identifier, wallet addresses, account numbers.
- Transaction details — dates, amounts, transaction type, and on-chain or off-chain specifics.
- A suspicion narrative describing the relevant facts, observed behaviour, indicators and any applicable red flags.
- An MLRO determination: file the STR, do not file, or seek additional information first, with the MLRO's signature against that decision.

This structure makes clear that not every internally escalated concern becomes an externally filed STR — the MLRO's determination is the point at which internal suspicion either converts into a formal filing to FMU or is closed without one. A CTR, by contrast, does not appear to require the same judgement-based escalation step in the source material, since Regulation 11.3's trigger is a value threshold rather than a suspicion assessment — though the applicant's own internal controls should still capture and log every qualifying fiat transaction for CTR purposes.

## Can STR and CTR filing be outsourced?

Not without meeting a specific set of conditions, because both functions sit inside the category of [AML](https://www.coinconnect.site/blog/3/fit-and-proper-aml-pvara-mistakes-54)-critical functions the NOC Regulations restrict. Regulation 14.1 lists "STR/CTR reporting" and MLRO responsibilities among the functions that "go to the core of the Applicant's AML/CFT duties" and may not be outsourced unless the applicant conducts due diligence on the service provider, maintains effective oversight arrangements, retains audit and inspection rights, and ensures those rights are legally enforceable, including in cross-border arrangements. Form A5, the Outsourcing Declaration and Register, requires the applicant to disclose the AML relevance, data shared, and audit rights attached to any outsourced function — meaning a VASP that routes STR or CTR filing through a regional compliance hub still has to document that arrangement to PVARA's standard, not simply note that filing "happens centrally".

## What are the consequences of getting STR or CTR filing wrong?

Two separate exposures follow from the source documents. First, Regulation 19.1(b) lists a breach of AML/CFT obligations as a ground on which PVARA may revoke a registered applicant's NOC and AML Registration status, applied proportionately under Regulation 19.2 having regard to severity and impact. Second, Regulation 18.1(c) requires a registered applicant to submit an Annual AML/CFT Return on Form A6, which asks directly for the number of STRs filed via goAML during the reporting period, the broad categories of suspicion reported, and the number of CTRs filed where fiat exposure exists — meaning filing activity, or the lack of it, is a figure PVARA reviews formally at least once a year, not only on inspection.

Records generated by both processes carry a standing retention duty: all AML/CFT records must be kept for a minimum of seven years, stored securely and kept auditable, retrievable and tamper-evident. Teams building [corporate setup](https://www.coinconnect.site/corporate-setup) and compliance infrastructure together should design STR and CTR logging, and the seven-year archive behind it, as one system rather than two separate workflows bolted together after the fact. For how these obligations connect to the wider goAML registration and handover process, see our companion piece on [goAML registration for VASPs](https://www.coinconnect.site/blog/coinconnect-insights-1/fmu-goaml-vasp-pakistan-17), and for the monitoring capability that feeds both report types, our piece on the [real-time detection standard](https://www.coinconnect.site/regulatory-licensing).

## Related reading

- [PVARA Exchange License: Capital, Rules & Obligations 2026](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-exchange-license-requirements-capital-obligations-24)

## About this analysis

This analysis was prepared by the CoinConnect research desk from Regulations 11.2, 11.3, 11.6, 14.1, 18.1(c) and 19.1(b) of the PVARA No Objection Certificate Regulations 2025, together with Forms A1, A4, A5, A6 and A7 at Annex A, read as published. The Anti-Money Laundering Act, 2010, referenced by Regulation 11.2 for the substance of what triggers an STR, was not among the three source documents reviewed, and its own definitions are not restated here. Where practice is not yet settled or guidance has not been issued, that is stated in the text above.

Regulatory positions change and specific requirements should be verified against the current position published by the relevant authority before you act on them. This is information and analysis, not legal advice, and it does not create an advisory relationship. Take professional advice on your own circumstances.

## Flags for Malik

1. The NOC Regulations do not state the CTR fiat threshold figure — I have not guessed at a number and have flagged this explicitly in the text. Worth confirming FMU's current published threshold before this goes out, since it is likely the single most practically useful fact a reader searching "CTR threshold Pakistan" wants.
2. I raised, as an open question, whether a large virtual-asset-only transaction with no fiat leg falls under CTR, STR, the Travel Rule, or none of the three under the published text — this is my own analytical gap-flagging, not a position stated anywhere in the source documents. Please sanity-check this framing before publication, since it borders on speculation even though I've labelled it as an open question rather than an answer.
