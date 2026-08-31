---
layout: post
title: "Data Segregation Controls Every VASP Licensee Must Implement"
date: 2026-01-01 09:00:00 +0500
categories: [Compliance]
author: "Malik Abbas"
description: "Section 40(3) of the Virtual Assets Act 2026 sets four data controls VASPs must implement: segregation, need-to-know access, encryption and audit trails."
---

Defining "sensitive information" is only half of what section 40 of the [Virtual Assets Act](https://blog.coinconnect.site/pakistans-virtual-assets-act-2026-the-complete-guide/), 2026 does. The other half — section 40(3) — tells a [Virtual Asset Service Provider](https://www.coinconnect.site/blog/coinconnect-insights-1/vasp-license-pakistan-3) (VASP) exactly what it must do once data falls into that category. Unlike much of the Act, which leaves detail to future Regulations, section 40(3) names four specific controls directly in the statute. This article sets out what those four controls require and what is still left open for Regulations to fill in.

## What must a VASP do once data is classified as sensitive information?

Section 40(3) requires a Licensee to ensure four things in relation to its sensitive information, as defined under section 40(2): logical and technical segregation from non-sensitive data, need-to-know access control, encryption and secure key management aligned with internationally recognised standards, and audit trails with monitoring mechanisms.

Section 40(3) states:

> A Licensee shall ensure that— (a) sensitive information is logically and technically segregated from non-sensitive data; (b) access to sensitive information is strictly controlled on a need-to-know basis; (c) encryption, tokenization, and secure key-management protocols are implemented in accordance with internationally recognised standards; and (d) appropriate audit trails and monitoring mechanisms are maintained.

Each of the four limbs is a "shall" obligation, meaning none of them is optional once a dataset falls within section 40(2)'s definition of sensitive information — a Licensee cannot pick, for example, encryption while skipping audit trails, or logical segregation while allowing access on a broader-than-need-to-know basis.

## What does "logically and technically segregated" actually mean?

Section 40(3)(a) requires both logical and technical segregation, which are two different things. Logical segregation refers to how data is organised and access-controlled within systems — separate databases, separate access permission sets, or separate application layers for sensitive versus non-sensitive data, even where they run on shared underlying infrastructure. Technical segregation goes further and typically implies physical or architectural separation — distinct storage systems, network segments, or environments.

The Act does not define either term precisely, and the specific storage architectures required are left to future Regulations under section 40(4). What is clear from the statutory language itself is that logical controls alone — access permissions on a shared database, for instance — are unlikely to satisfy section 40(3)(a) on their own, since the sub-section requires both logical and technical segregation conjunctively, not one or the other.

## What does "need-to-know" access mean in practice?

Section 40(3)(b) requires access to sensitive information to be "strictly controlled on a need-to-know basis." This is a role-based access principle: an employee or system should have access to sensitive information only where their specific function requires it, not by default because of general seniority or department membership.

- a customer support agent handling a billing query does not automatically need access to a customer's private key material under section 40(2)(c), even though both sit within the same Licensee's systems
- a compliance officer conducting due diligence needs access to customer identification records under section 40(2)(a), but that access does not automatically extend to proprietary trading data under section 40(2)(d)
- the word "strictly" in section 40(3)(b) suggests the Authority will expect documented access controls, not an informal understanding of who should and should not see particular data

## What standard does the encryption requirement point to?

Section 40(3)(c) requires "encryption, tokenization, and secure key-management protocols" to be implemented "in accordance with internationally recognised standards." The Act names three distinct techniques — encryption, tokenisation, and key management — rather than treating them as interchangeable, and ties compliance to an external, unnamed benchmark of "internationally recognised standards" rather than setting a Pakistan-specific standard itself.

| Control | Statutory reference | What it requires |
|---|---|---|
| Logical and technical segregation | Section 40(3)(a) | Separation of sensitive from non-sensitive data, both in access structure and in underlying architecture |
| Need-to-know access | Section 40(3)(b) | Role-based restriction of who can access sensitive information |
| Encryption, tokenisation, key management | Section 40(3)(c) | Technical protection measures benchmarked against unnamed international standards |
| Audit trails and monitoring | Section 40(3)(d) | Ongoing, recorded visibility into who accessed sensitive information and when |

This is one of the few places in the Act where the drafting points outward to an external reference rather than to future [PVARA](https://www.coinconnect.site/pvara-guide) Regulations. Our reading is that a Licensee should not wait for PVARA to name a specific standard before implementing recognised cryptographic practice, since section 40(3)(c) already requires alignment with international standards as a present obligation, not a future one contingent on Regulations. The Act does not, however, name which specific standards — such as any particular ISO or NIST framework — would satisfy this requirement, and confirming that with the Authority directly is the more defensible approach than assuming a particular standard is sufficient.

## What do "audit trails and monitoring mechanisms" require under section 40(3)(d)?

Section 40(3)(d) requires "appropriate audit trails and monitoring mechanisms" to be maintained for sensitive information. Read alongside section 40(3)(b)'s need-to-know access requirement, the two work together: need-to-know access limits who can reach sensitive information in the first place, while audit trails create a record of who actually did, so that access can be reviewed after the fact and any misuse can be detected and traced.

The Act does not specify retention periods for these audit trails, monitoring frequency, or the format in which they must be kept. Section 40(4), discussed below, leaves these details to future Regulations, which means a Licensee currently has a stated duty to maintain audit trails without a stated technical specification for how.

## What is still left to future Regulations under section 40?

Section 40(4) gives the Authority power to prescribe, by Regulations, "minimum technical standards, cybersecurity controls, storage architectures, encryption requirements, and data-governance frameworks to give effect to this section."

Section 40(4) states:

> The Authority may prescribe, by Regulations, minimum technical standards, cybersecurity controls, storage architectures, encryption requirements, and data-governance frameworks to give effect to this section.

At the time of writing, no such Regulations had been published. This means the four controls in section 40(3) are binding obligations right now, in general terms, while the specific technical thresholds that would let a Licensee demonstrate precise compliance — minimum encryption strength, required storage architecture patterns, or a defined audit-log retention period, for example — remain undefined until Regulations appear.

## How does section 40 interact with the Act's broader cybersecurity duty?

Section 40 is narrower and more specific than the general cybersecurity duty under section 34, which applies to a Licensee's systems and operations as a whole. Section 40 applies specifically to the sensitive information defined in section 40(2), and sets out named controls directly in the statute rather than leaving the entire substance to future Regulations, as section 34 largely does. A Licensee's overall cybersecurity programme, built to satisfy section 34 and the ongoing obligations of section 22(e), should treat section 40(3)'s four controls as a specific, higher-bar sub-requirement applying to a defined subset of its data — not as duplicative of its general cybersecurity controls.

## What should a VASP do to build section 40(3) compliance now?

- implement both logical and technical segregation for sensitive information now, rather than logical controls alone, since section 40(3)(a) requires both conjunctively
- document a formal need-to-know access policy naming which roles may access which categories of sensitive information under section 40(2), rather than relying on informal practice
- adopt a recognised international encryption, tokenisation and key-management standard now, since section 40(3)(c) is a present obligation not contingent on future Regulations, and confirm the specific standard with the Authority where uncertainty remains
- build audit-trail and monitoring infrastructure with generous retention and detail, since section 40(3)(d) does not specify minimums and Regulations under section 40(4) may later raise the bar
- track PVARA's publication of section 40(4) Regulations closely, since they will define the specific technical thresholds a Licensee's existing controls will be measured against

The four controls in section 40(3) are among the most concrete, self-executing obligations in the entire Act — they do not wait for Regulations to become binding. A VASP building its [regulatory licensing](https://www.coinconnect.site/regulatory-licensing) case should treat logical and technical segregation, need-to-know access, internationally recognised encryption, and audit trails as controls to demonstrate at application stage, not as items to defer until PVARA's technical standards under section 40(4) are eventually published.

## Related reading

- [PVARA Exchange License: Capital, Rules & Obligations 2026](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-exchange-license-requirements-capital-obligations-24)
- [PVARA Transfer & Settlement License: Crypto Payments 2026](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-transfer-settlement-license-payments-remittance-28)
- [PVARA Licensing Process: NOC to Full Licence, Step by Step](https://blog.coinconnect.site/pvara-licensing-process-noc-to-full-licence-step-by-step/)
- [The PVARA Licensing Gold Rush: Pakistan's Crypto Frontier](https://www.coinconnect.site/blog/3/blogpvara-licensing-gold-rush-pakistan-crypto-frontier-56)
- [PVARA Custody License: Safeguard Customer Crypto 2026](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-custody-license-safeguarding-customer-assets-25)
- [goAML Registration for VASPs: Who Registers, and When](https://blog.coinconnect.site/goaml-registration-for-vasps-who-registers-and-when/)

## About this analysis

This analysis was prepared by the CoinConnect research desk from the Virtual Assets Act, 2026, read as published. Where practice is not yet settled or guidance has not been issued, that is stated in the text above.

Regulatory positions change and specific requirements should be verified against the current position published by the relevant authority before you act on them. This is information and analysis, not legal advice, and it does not create an advisory relationship. Take professional advice on your own circumstances.

## Flags for Malik

- No section 40(4) Regulations existed in the source documents, so all specific technical thresholds (encryption strength, retention periods, storage architecture detail) are correctly left undefined in the article rather than invented.
- The definitions I gave for "logical" versus "technical" segregation are ordinary-meaning explanations, not statutory definitions — the Act does not define either term, and I've flagged this as inference.
- I did not name a specific international standard (e.g. ISO 27001 or a named NIST framework) for the encryption/key-management requirement under section 40(3)(c), since none is named in the Act text and naming one would be an unverifiable addition — worth confirming PVARA's eventual position once Regulations issue.
