---
layout: post
title: "Targeted Financial Sanctions Screening and Asset Freezes"
date: 2026-01-01 09:00:00 +0500
categories: [Compliance]
author: "Malik Abbas"
description: "PVARA's NOC Regulations require VASPs to screen every customer and transaction for sanctions matches, then freeze and report designated persons immediately."
---

Sanctions screening is not a feature a [virtual asset service provider](https://www.coinconnect.site/blog/coinconnect-insights-1/vasp-license-pakistan-3) ("VASP") can add later. Under Pakistan's pre-[licensing framework](https://www.coinconnect.site/pvara-guide) it is one of the minimum controls an applicant must already have running before the Pakistan Virtual Asset Regulatory Authority ("PVARA" or "the Authority") will grant a [No Objection Certificate](https://www.coinconnect.site/regulatory-licensing) ("NOC").

This analysis reads regulation 12 of the PVARA No Objection Certificate Regulations 2025 as published, sets out exactly what it requires an applicant to screen and to do when a match is found, and places that duty inside the wider AML/CFT framework the same Regulations impose.

## What must an NOC applicant screen under regulation 12?

Regulation 12.1 requires every applicant to implement controls that screen four categories — customers, beneficial owners, counterparties and transactions — against both domestic and United Nations sanctions lists, before those persons or transactions are dealt with. The obligation is a screening duty, not a one-off onboarding check. The Regulations state:

> "Applicants shall implement controls to screen all customers, beneficial owners, counterparties and transactions against domestic and United Nations sanctions lists."

Four things follow from that wording. First, the screening universe is wider than the [customer](https://www.coinconnect.site/blog/3/customer-assets-definition-pvara-pakistan-62) relationship itself — beneficial owners and counterparties are named separately, so a firm cannot satisfy regulation 12.1 by screening its direct account holders alone while leaving underlying beneficial owners or the other side of a trade unchecked. Second, "transactions" is screened as its own category, meaning the control has to operate at the point of movement, not only at onboarding. Third, the reference list is dual — domestic sanctions lists and United Nations lists together — so a control built against only one source does not meet the text. Fourth, the Regulations do not specify a screening technology or vendor; the obligation is the outcome, and the method is left to the applicant's own risk-based design.

## What happens when a sanctions match is found?

Regulation 12.2 imposes a two-part duty once a match is confirmed: immediate asset freezing, and immediate reporting of that freeze to the Financial Monitoring Unit ("FMU") and any other authority designated under Pakistan's targeted financial sanctions ("TFS") framework. The Regulations state:

> "Applicants must immediately freeze assets of designated persons and report such freezes to FMU and any other designated authority in accordance with Pakistan's TFS framework."

The word "immediately" is doing real work here — there is no grace period, no internal escalation window built into the text, and no discretion to delay a freeze pending further verification. In practice, our reading is that a firm's sanctions programme has to be capable of freezing a matched account and generating the FMU report in the same operational moment the match is confirmed, which is a materially higher bar than transaction monitoring alerts that route to a human queue for review before action. The [FMU](https://www.fmu.gov.pk/) is Pakistan's national financial intelligence unit; its own published material sits at fmu.gov.pk and should be checked directly for the current mechanics of TFS reporting, which are not restated in full in the three source documents reviewed for this analysis.

## Where does sanctions screening sit inside the wider AML/CFT framework?

TFS screening is one of nine minimum components regulation 8.2 requires every applicant's AML/CFT framework to include, alongside customer due diligence, transaction monitoring and suspicious transaction reporting. Regulation 8.2 lists these as the floor, not the ceiling, of what an applicant's framework must contain:

| Component | What regulation 8.2 requires |
|---|---|
| AML/CFT Policy | Approved by the Applicant Board |
| CDD and EDD procedures | Documented, covering [customer](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-license-pakistan-complete-guide-22) identification and enhanced checks |
| TFS screening procedures | The subject of regulation 12 |
| Transaction monitoring | Processes capable of detecting suspicious activity |
| STR/CTR escalation procedures | Internal routes to filing with FMU |
| ML/TF risk assessment | A documented, enterprise-wide assessment |
| Recordkeeping and data governance policy | Covered separately under regulation 13 |
| AML/CFT training programme | Applies across relevant staff |
| Outsourcing risk management framework | Governs any AML function performed by a third party |

Read together with regulation 4, which requires the Applicant Board itself to oversee AML/CFT compliance — including approval of policies and review of enterprise-wide risk assessments — the TFS control is not a standalone technical system. It has to be board-approved, documented, and sit inside a framework the [fit and proper](https://www.coinconnect.site/blog/coinconnect-insights-1/url-slug-fit-and-proper-test-pvara-form-a3-14) Compliance Officer and Money Laundering Reporting Officer are accountable for.

## What must a TFS policy document, in practice?

Two of the statutory forms attached to the NOC Regulations spell out what a TFS policy has to cover in more granular terms than regulation 12 itself states. Form A1, the [NOC](https://www.coinconnect.site/regulatory-licensing) application form, requires the applicant to confirm submission of a "Sanctions / Targeted Financial Sanctions (TFS) Policy and Procedures" document as part of its AML/CFT framework documentation. Form A4, the AML/CFT Framework Submission Statement signed by the Chief Executive Officer and the Money Laundering Reporting Officer, describes the same document in more detail as a policy "including wallet-address screening, name screening, freeze and reporting procedures."

That description matters because it names a control most fiat-only sanctions programmes do not need: wallet-address screening sits alongside name screening as an explicit, separately named element. A TFS policy built only around name-matching against sanctions lists — the standard approach for a traditional bank or money service business — does not, on the wording of Form A4, meet what PVARA expects a virtual asset service provider's policy to document. The policy also has to be tested, not merely written: Form A4 requires confirmation that sanctions and TFS screening systems are "implemented, tested and operational" before the application is submitted, alongside blockchain analytics tools and transaction monitoring software addressed elsewhere in the same Statement.

## Who counts as a "designated person" under Pakistan's sanctions framework?

The NOC Regulations use the term "designated persons" in regulation 12.2 without defining it, and the phrase does not appear in the definitions sections of the three source documents reviewed for this analysis. Our reading is that the term draws its meaning from Pakistan's wider TFS legal framework — the designation mechanisms operated under domestic law and United Nations Security Council processes referenced in regulation 12.1 — rather than from anything internal to the NOC Regulations themselves. Applicants should not assume the meaning of "designated person" from general international practice; the operative designation lists are maintained outside the three documents this analysis is built on, and firms should confirm the current list sources directly with FMU or PVARA before finalising screening logic. The Financial Action Task Force, the intergovernmental standard-setter behind the global TFS framework referenced obliquely in Pakistan's own [anti-money laundering](https://www.coinconnect.site/blog/3/fit-and-proper-aml-pvara-mistakes-54) architecture, publishes its own material at [fatf-gafi.org](https://www.fatf-gafi.org/).

## How does the TFS duty carry over once a firm holds a full VASP licence?

Regulation 12 sits inside the No Objection Certificate Regulations, which the [Virtual Assets Act](https://blog.coinconnect.site/pakistans-virtual-assets-act-2026-the-complete-guide/), 2026 layers underneath full licensing rather than replaces once a licence is granted. Section 46(1) of the Act deems every licensed [virtual asset service provider](https://www.coinconnect.site/blog/coinconnect-insights-1/vasp-license-pakistan-3) a financial institution for the purposes of the Anti-Money Laundering Act, 2010, and section 46(2) separately requires reporting of suspicious transactions to FMU and the maintenance of internal AML controls. Section 60 of the Act gives PVARA its own emergency powers, permitting the Authority to freeze related assets for up to thirty days where it identifies a systemic threat, market manipulation, fraud or cybersecurity breach — a regulator-level freeze power that sits alongside, rather than replaces, the applicant's own immediate freeze duty under regulation 12.2.

The ongoing obligations set out in Part 6 of the NOC Regulations reinforce the same continuity: a registered applicant must comply with all AML/CFT obligations at all times, and the Authority may revoke NOC status, including AML registration, where systemic or material AML/CFT failures occur. A sanctions screening system that worked at the point of application but is never retested against updated lists is, on this framework, a live compliance gap rather than a historic one. Firms building out their [licence application](https://www.coinconnect.site/regulatory-licensing) should treat the TFS control as permanent infrastructure, reviewed on the same cadence as the transaction monitoring and [customer due diligence](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-license-pakistan-complete-guide-22) systems it sits beside.

Two practical points follow for firms scoping this control:

- Screening has to run continuously across four categories — customers, beneficial owners, counterparties and transactions — not just at the moment an account is opened.
- The freeze-and-report duty in regulation 12.2 has no stated grace period; "immediately" should be read as an operational design constraint, not an aspiration.

## About this analysis

This analysis was prepared by the CoinConnect research desk from regulations 4, 8.2, 12.1 and 12.2 of the PVARA No Objection Certificate Regulations 2025, together with Form A1 and Form A4 of the same Regulations, and cross-referenced against sections 46 and 60 of the Virtual Assets Act, 2026 as passed by the National Assembly, each read as published. The term "designated persons" is not defined in any of the three source documents reviewed, and the current designation list sources were not restated here for that reason. Where practice is not yet settled or guidance has not been issued, that is stated in the text above.

Regulatory positions change and specific requirements should be verified against the current position published by the relevant authority before you act on them. This is information and analysis, not legal advice, and it does not create an advisory relationship. Take professional advice on your own circumstances.

## Flags for Malik

1. I linked "FMU" to fmu.gov.pk directly in the body text (not just the About section) — this is an approved external host, but check the anchor phrasing reads naturally to you.
2. "Designated persons" is undefined in all three source documents. I deliberately did not guess at Pakistan's designation-list mechanics (e.g. which domestic list, which statute administers it) since that sits outside the reviewed material — worth a follow-up article once we have the primary TFS legislation to hand.
3. Regulation 12 does not state a screening frequency (real-time vs batch vs periodic) — I did not invent one. If you have operator-side knowledge of what PVARA expects in practice, that would strengthen a future revision.
