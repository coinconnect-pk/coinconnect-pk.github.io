---
layout: post
title: "Customer Data Privacy Rules for VASPs Under Section 49"
date: 2026-01-01 09:00:00 +0500
categories: [Compliance]
author: "Malik Abbas"
description: "Section 49 of the Virtual Assets Act 2026 sets a consent standard for customer data, and section 5(2) makes external data protection law override the Act."
---

Two short provisions in the [Virtual Assets Act](https://blog.coinconnect.site/pakistans-virtual-assets-act-2026-the-complete-guide/), 2026 govern how a [Virtual Asset Service Provider](https://www.coinconnect.site/blog/coinconnect-insights-1/vasp-license-pakistan-3) (VASP) handles customer data: section 49, which sets a consent standard for data processing, and section 5(2), which decides which law actually controls when a data protection statute conflicts with the Act. Neither section is long, but together they define the outer boundary of what a licensee may do with the personal data it collects. This article reads both in full and sets out what a VASP can rely on today.

## What does section 49 of the Virtual Assets Act require?

Section 49 requires every Licensee to implement strict limits on the collection, use, and sharing of customer data, and to obtain explicit, informed, and revocable consent before carrying out any non-essential data processing. The obligation applies at all times a licence is held, not only at onboarding.

Section 49 states:

> Each licensee shall implement strict limits on the collection, use, and sharing of customer data, requiring explicit, informed, and revocable consent for any non-essential data processing.

The section names three qualities the consent must have: it must be explicit (given actively, not inferred from silence or a pre-ticked box), informed (the customer understands what they are consenting to), and revocable (the customer can withdraw it later). All three conditions apply together — consent that is explicit but not revocable, for example, would not satisfy section 49 as drafted.

## What counts as "non-essential" data processing under section 49?

The Act does not define "non-essential" anywhere in section 3's definitions or elsewhere in the text. This is a genuine gap: section 49 draws a line between processing that requires explicit consent and processing that apparently does not, but it does not say where that line sits.

- processing plainly required to deliver the [Virtual Asset](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-license-pakistan-complete-guide-22) Service itself — identity verification for [customer due diligence](https://www.coinconnect.site/blog/3/fit-and-proper-aml-pvara-mistakes-54), transaction execution, and regulatory reporting under the Act's [anti-money laundering](https://www.coinconnect.site/blog/3/fit-and-proper-aml-pvara-mistakes-54) chapter — is the strongest candidate for "essential" processing that section 49 does not require separate consent for, since the Act elsewhere makes that processing mandatory
- processing beyond that core function — marketing communications, sharing data with unrelated third parties, or secondary analytics use — is the more obvious candidate for "non-essential" processing requiring the explicit, informed and revocable consent section 49 demands
- this distinction is our reading of how section 49 is likely to operate, not a definition drawn from the Act itself, and [PVARA](https://www.coinconnect.site/pvara-guide) has not published Regulations clarifying the boundary

Where a VASP is uncertain whether a specific processing activity is essential or non-essential, treating it as non-essential and obtaining the section 49 consent standard is the more defensible position until PVARA states otherwise.

## Does section 49 apply on top of, or instead of, other data protection law?

Section 5(2) of the Act answers this directly, and the answer favours external law. Section 5 governs the Act's relationship with other laws generally, and section 5(1) states that the Act prevails over other laws in the event of inconsistency — except where section 5(2) applies.

Section 5(2) states:

> Where any law prescribes measures relating to data protection, data governance, or cybersecurity, financial secrecy or cross-border transfer of personal data, such provisions shall prevail and be complied with by the Authority and Licensees.

This is a carve-out, not a general statement about data protection. Section 5(1) would otherwise let the Virtual Assets Act override an inconsistent provision in another statute. Section 5(2) reverses that specifically for data protection, data governance, cybersecurity, financial secrecy, and cross-border personal data transfer — meaning any applicable Pakistani data protection law takes precedence over the Act on these subjects, and both PVARA and Licensees must comply with it.

| Question | Governing provision | What it means |
|---|---|---|
| What consent standard applies to non-essential customer data processing? | Section 49 | Explicit, informed, revocable consent |
| Does the Act or external data protection law govern where they conflict? | Section 5(2) | External data protection, governance, cybersecurity and cross-border transfer law prevails |
| Does the Act override other law generally? | Section 5(1) | Yes, except for the section 5(2) carve-out |

## Why does section 5(2) matter more than it looks?

Section 5(2) means a VASP cannot treat the Virtual Assets Act as its complete data compliance framework. Even where the Act is silent, permissive, or less demanding than another Pakistani law on data protection, data governance, cybersecurity, financial secrecy, or cross-border data transfer, that other law governs. A Licensee's compliance programme therefore has to be built against two sources simultaneously — the Act's own provisions, including section 49's consent standard and section 40's sensitive-information controls, and whatever separate data protection legislation applies in Pakistan.

This also affects a VASP's [data localisation](https://www.coinconnect.site/regulatory-licensing) planning. Section 39 of the Act permits a Licensee to store or process data outside Pakistan subject to compliance with applicable data protection, cybersecurity and cross-border transfer laws — the same category of law that section 5(2) already gives priority to. The two sections point the same direction: cross-border data movement is not primarily an Act question, it is a question for whichever data protection statute applies, with the Act's own safeguards sitting alongside it.

## How does section 49 interact with the Act's sensitive information rules?

Section 40 of the Act separately requires a Licensee to segregate "sensitive information" — including customer identification records, transaction data capable of identifying a customer, and private cryptographic keys — from other operational data, with defined controls around access, encryption and audit trails. Section 49's consent standard and section 40's segregation duty address different problems: section 49 is about the lawful basis for processing customer data at all, while section 40 is about how that data, once collected, is protected and controlled internally. A VASP's data governance framework needs to satisfy both — consent at the point of collection under section 49, and technical and organisational controls once the data is held under section 40.

## What should a VASP do to prepare for section 49 compliance?

- map every category of customer data processing the business performs, and classify each as plausibly essential or non-essential, documenting the reasoning since the Act itself does not define the line
- build a consent mechanism that is explicit, informed, and — critically — genuinely revocable, since section 49 requires all three, not just one
- identify which Pakistani data protection, cybersecurity, financial secrecy or cross-border transfer laws apply to the business independently of the Virtual Assets Act, since section 5(2) makes them the controlling authority on these subjects
- align the consent and data-handling framework with the sensitive-information controls required under section 40, rather than treating the two as separate compliance projects
- avoid assuming that anything not expressly required elsewhere in the Act is automatically "essential" processing exempt from section 49 consent — until PVARA issues guidance, the conservative reading is safer

Section 49 sets the consent principle; section 5(2) decides which statute actually governs the technical detail of data protection. A VASP preparing its [licence application](https://www.coinconnect.site/regulatory-licensing) case should treat both provisions as a single compliance question, not two separate ones, and should confirm which external data protection law currently applies in Pakistan before finalising its consent architecture.

## Related reading

- [PVARA Exchange License: Capital, Rules & Obligations 2026](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-exchange-license-requirements-capital-obligations-24)
- [PVARA Transfer & Settlement License: Crypto Payments 2026](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-transfer-settlement-license-payments-remittance-28)

## About this analysis

This analysis was prepared by the CoinConnect research desk from the Virtual Assets Act, 2026, read as published. Where practice is not yet settled or guidance has not been issued, that is stated in the text above.

Regulatory positions change and specific requirements should be verified against the current position published by the relevant authority before you act on them. This is information and analysis, not legal advice, and it does not create an advisory relationship. Take professional advice on your own circumstances.

## Flags for Malik

- Neither the Act nor either regulatory source document defines "non-essential" for section 49 purposes. My essential/non-essential split is a reasoned inference from other provisions of the Act (CDD, AML reporting), not a statutory test — flagged clearly in the text as "our reading."
- I did not name a specific Pakistani data protection statute (e.g. a personal data protection bill or act) because none of the three source documents names one, and the Act's own text in section 5(2) refers only generically to "any law." Naming a specific statute here would be an unverifiable addition.
- The link between section 49 and section 39 (data localisation) is my own connection based on both sections pointing to the same category of external law — worth double-checking this reads naturally rather than as overreach.
