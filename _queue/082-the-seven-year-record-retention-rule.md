---
layout: post
title: "The Seven-Year Record Retention Rule for Pakistani VASPs"
date: 2026-01-01 09:00:00 +0500
categories: [Compliance]
author: "Malik Abbas"
description: "PVARA's NOC Regulations set a seven-year minimum for AML/CFT records and require them to be auditable, retrievable and tamper-evident."
---

Record retention sounds like an administrative afterthought until an examiner asks for a transaction file from four years ago and the system that held it no longer exists. Pakistan's pre-[licensing framework](https://www.coinconnect.site/pvara-guide) treats retention as a standalone control, not a by-product of having a database.

This analysis reads regulation 13 of the PVARA [No Objection Certificate](https://www.coinconnect.site/regulatory-licensing) Regulations 2025 as published, together with the related requirement in the [Regulatory Sandbox](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-sandbox-form-i-complete-walkthrough-2026-8) Guidelines, and sets out what a [virtual asset service provider](https://www.coinconnect.site/blog/coinconnect-insights-1/vasp-license-pakistan-3) ("VASP") actually has to build to meet it.

## How long must a VASP keep AML/CFT records under Pakistani law?

Regulation 13.1 of the PVARA [No Objection Certificate](https://blog.coinconnect.site/the-pvara-no-objection-certificate-a-complete-guide/) Regulations 2025 sets a floor of seven years for all [AML](https://www.coinconnect.site/blog/3/fit-and-proper-aml-pvara-mistakes-54)/CFT records. The Regulations state:

> "All AML/CFT records shall be maintained for a minimum of seven (7) years."

Two things follow directly from that wording. First, seven years is a minimum, not a target — nothing in regulation 13 caps retention at seven years, and firms with longer obligations under other Pakistani law are not excused from them by this figure. Second, the duty attaches to "AML/CFT records" as a category, not to a named list of documents. The [No Objection Certificate](https://www.coinconnect.site/regulatory-licensing) Regulations do not enumerate every record type this covers in regulation 13 itself, but Form A4 of the same Regulations lists the records the retention policy is expected to reach: customer due diligence files, transaction monitoring outputs, suspicious transaction report escalations, and the underlying data supporting the enterprise-wide risk assessment.

Section 47(4) of the [Virtual Assets Act](https://blog.coinconnect.site/pakistans-virtual-assets-act-2026-the-complete-guide/), 2026 reinforces the same floor at the full-licence stage, requiring a Licensee to maintain records of transactions, customer due-diligence data and risk assessments for a period prescribed by Regulations that "shall not be less than the period required under the Anti-Money Laundering Act, 2010." Read together, the seven-year figure in regulation 13.1 is the applicable minimum unless a future Regulation made under the Act sets a longer period.

## What standard must the records themselves meet?

Meeting the seven-year duration is not enough on its own. Regulation 13.2 imposes a separate quality standard on how those records are stored. The Regulations state:

> "Records shall be stored securely and must be auditable, retrievable and tamper-evident."

Each of the three words in that sentence describes a different capability a VASP's recordkeeping system has to demonstrate, not a single generic "backup" requirement:

- **Auditable** — a third party (PVARA, an external auditor, or law enforcement acting under section 57 of the Act) must be able to trace a record back to its source and confirm it has not been selectively altered.
- **Retrievable** — the record has to be producible on request within a reasonable timeframe, not merely stored somewhere it is technically possible to find.
- **Tamper-evident** — the storage method must make unauthorised alteration detectable, whether through cryptographic hashing, write-once storage, versioned logs, or an equivalent control.

In practice, our reading is that a conventional mutable database with periodic backups does not, by itself, satisfy "tamper-evident" unless the firm layers an integrity-checking mechanism on top of it. Regulation 13.2 does not name a required technology, and PVARA has not published a technical standard for this control among the three source documents reviewed for this analysis, so the specific mechanism is left to the applicant's own risk-based design — subject to PVARA's power under Form A4 to confirm the system is "implemented, tested and operational" before an application is submitted.

## Where does regulation 13 sit inside the wider AML/CFT framework?

Recordkeeping and data governance is one of the nine minimum components regulation 8.2 requires every applicant's AML/CFT framework to include, alongside customer due diligence and transaction monitoring. The table below places retention against the surrounding controls it depends on and feeds into.

| Framework component | How it connects to retention |
|---|---|
| CDD and EDD procedures | Generate the identification and verification records regulation 13 requires the firm to keep |
| Transaction monitoring | Produces alert and case data that forms part of the retained record |
| STR/CTR escalation procedures | The internal suspicious activity reports that must be retrievable years after filing |
| Recordkeeping and data governance policy | The document Form A1 requires the applicant to submit, covering the 7-year retention period explicitly |
| Outsourcing risk management framework | Governs retention where a third party stores records on the firm's behalf |

Form A1, the NOC application form, requires the applicant to confirm submission of a "Recordkeeping and Data Governance Policy (including 7-year retention)" as one of the documents supporting its AML/CFT framework. That policy is then certified as final and Board-approved through Form A4, signed by the Chief Executive Officer and the [Money Laundering Reporting Officer](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-license-pakistan-complete-guide-22), before the NOC is granted — so retention is assessed at the pre-[incorporation](https://www.coinconnect.site/corporate-setup) stage, not left until a full licence application.

## What does record retention look like during a sandbox test?

Firms testing a product inside PVARA's regulatory [sandbox](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-sandbox-reduced-capital-pakistan-19) face a parallel retention duty that applies even before an NOC or licence exists. The Undertaking every sandbox participant must sign, set out at Annexure-B of the Regulatory Sandbox Guidelines, commits the participant to specific obligations:

> "It shall ensure retention and confidentiality of consumer data as per Virtual Assets Ordinance 2025."

The same Undertaking separately commits the participant to "maintain proper records during testing period for reviews by Authority anytime," and to allow the Authority "complete access... to its core reporting/accounting/significant software." Our reading is that a sandbox participant cannot treat the testing phase as a lower-stakes environment where recordkeeping discipline can wait until formal registration — the Undertaking makes retrievability and Authority access conditions of continued sandbox participation, not aspirations. The Guidelines do not restate the seven-year figure from regulation 13.1 directly inside Annexure-B, and this analysis does not assume the sandbox retention period is identical to the seven-year NOC standard; a firm moving from sandbox testing into a full NOC application should confirm with PVARA whether sandbox-era records fall under the same seven-year clock.

## What happens if a firm cannot produce a record on request?

Neither regulation 13 nor the sandbox Undertaking states a specific penalty tied only to a retention failure. The consequence instead flows through the general enforcement provisions. Regulation 19.1 of the NOC Regulations lists "systemic or material AML/CFT failures" as a ground for revoking an Applicant's NOC, and recordkeeping is one of the nine components regulation 8.2 treats as a minimum element of the AML/CFT framework whose absence would qualify. Separately, section 54(6) of the Virtual Assets Act, 2026 makes wilful failure to comply with any order or decision of PVARA — which would include a document production order — punishable with imprisonment of up to one year, a fine of up to twenty-five million Pakistani Rupees, or both, alongside any administrative penalty the Authority imposes.

Two practical points follow for firms scoping this control:

- Seven years is the floor set by regulation 13.1; firms should check whether any other Pakistani law they are subject to sets a longer period before finalising a retention policy.
- "Tamper-evident" is a distinct requirement from "backed up" — a system that only prevents data loss, without also making unauthorised alteration detectable, does not on its own meet regulation 13.2.

## About this analysis

This analysis was prepared by the CoinConnect research desk from regulations 8.2, 13.1, 13.2 and 19.1 of the PVARA No Objection Certificate Regulations 2025, Form A1 and Form A4 of the same Regulations, Annexure-B of the PVARA Regulatory Sandbox Guidelines, and section 47(4) and section 54(6) of the Virtual Assets Act, 2026 as passed by the National Assembly, each read as published. No technical standard for "tamper-evident" storage was found in the three source documents reviewed, so none is stated here. Where practice is not yet settled or guidance has not been issued, that is stated in the text above.

Regulatory positions change and specific requirements should be verified against the current position published by the relevant authority before you act on them. This is information and analysis, not legal advice, and it does not create an advisory relationship. Take professional advice on your own circumstances.

## Flags for Malik

1. I did not find a stated technical standard for "tamper-evident" in any of the three source documents — I described the concept generically rather than naming a specific technology (hashing, WORM storage etc). Worth flagging to a client only as illustrative, not as a PVARA-mandated method.
2. I explicitly did not assume the sandbox's Annexure-B retention duty runs on the same seven-year clock as regulation 13.1, since Annexure-B doesn't restate a number. If you know PVARA's actual practice here, that would sharpen a revision.
3. Section 47(4) of the Act says the prescribed retention period "shall not be less than" the AMLA 2010 period — I did not state what that AMLA period actually is, since it isn't in our three source documents. Could be worth a follow-up article once we have the AMLA text on file.
