---
layout: post
title: "The Five Categories of Sensitive Information Under PVARA"
date: 2026-01-01 09:00:00 +0500
categories: [Compliance]
author: "Malik Abbas"
description: "Section 40(2) of the Virtual Assets Act 2026 lists five categories of sensitive information, from customer records to private keys, that VASPs must segregate."
---

Not all data a [Virtual Asset Service Provider](https://www.coinconnect.site/blog/coinconnect-insights-1/vasp-license-pakistan-3) (VASP) holds carries the same risk if it leaks. A marketing mailing list and a private cryptographic key are both "data," but only one of them, if exposed, lets someone move a customer's funds. The [Virtual Assets Act](https://blog.coinconnect.site/pakistans-virtual-assets-act-2026-the-complete-guide/), 2026 draws this distinction explicitly in section 40, defining "sensitive information" as a category subject to its own protection duties, separate from a VASP's general data-handling obligations.

## What does section 40 of the Act require in general terms?

Section 40(1) requires every Licensee to implement appropriate technical, organisational, and governance measures to ensure the segregation of sensitive information from other operational data, in the manner to be prescribed by Regulations under the Act.

Section 40(1) states:

> Every Licensee shall implement appropriate technical, organisational, and governance measures to ensure the segregation of sensitive information from other operational data, in such manner as may be prescribed by Regulations.

The duty has three limbs — technical, organisational, and governance measures — meaning a purely technical fix, such as encrypting a database, would not on its own satisfy section 40(1) if the Licensee lacks the organisational and governance controls to go with it, such as clear internal ownership of who is responsible for sensitive data handling.

## What counts as "sensitive information" under the Act?

Section 40(2) sets out five categories, introduced with language stating the list is illustrative rather than closed. This is the operative definition for the rest of section 40 and for any future Regulations built on it.

Section 40(2) states:

> For the purposes of this section, "sensitive information" shall include, but not be limited to— (a) customer identification and due-diligence records; (b) transaction-level data capable of identifying a customer; (c) private keys, cryptographic credentials, or wallet authentication data; (d) proprietary trading data and risk-management systems; and (e) any other category of information designated as sensitive by the Authority.

| Category | Statutory reference | What it covers |
|---|---|---|
| Customer identification and due-diligence records | Section 40(2)(a) | KYC and CDD documentation gathered on onboarding and ongoing basis |
| Transaction-level data capable of identifying a customer | Section 40(2)(b) | Individual transactions, not just aggregated or anonymised statistics |
| Private keys, cryptographic credentials, or wallet authentication data | Section 40(2)(c) | The technical means of accessing or moving Virtual Assets |
| Proprietary trading data and risk-management systems | Section 40(2)(d) | Internal commercial and risk infrastructure, not customer data at all |
| Any other category designated as sensitive by the Authority | Section 40(2)(e) | Open-ended, Authority-driven addition to the list |

## Why is category (d) — proprietary trading data — grouped with customer data?

This is worth pausing on, because categories (a) to (c) are customer-facing while category (d) is not. Proprietary trading data and risk-management systems belong to the Licensee itself, not to a customer, yet section 40(2) places them in the same protected category as customer identification records and private keys.

Our reading is that the drafting reflects two different rationales sitting under one umbrella term. Categories (a) to (c) protect customers from harm if their identity, transaction history, or key material is exposed. Category (d) protects market integrity and the Licensee's own operational safety — proprietary trading and risk-management systems, if exposed, could be exploited by a third party to predict or manipulate the Licensee's positions, which is a market-conduct risk rather than a customer-privacy risk. The Act does not state this rationale explicitly; it is inferred from the nature of what each category actually contains.

## Is the list of five categories closed, or can PVARA add more?

Open. Category (e) — "any other category of information designated as sensitive by the Authority" — means the four named categories in section 40(2)(a) to (d) are a floor, not a ceiling. The Authority can expand the definition of sensitive information for a given Licensee or the market generally through a written designation, without needing to amend the Act itself.

- categories (a) to (d) are fixed in the statute and apply to every Licensee without further Authority action
- category (e) is a live power the Authority can exercise at any time to bring new data types within the sensitive-information regime
- a Licensee handling a novel data type not obviously covered by categories (a) to (d) — biometric onboarding data, for instance, if the business uses it — should not assume it falls outside section 40 simply because it is not named; the Authority retains the power to designate it under category (e)

## Do customer identification records and transaction-level data overlap?

Partially, but the Act treats them as distinct categories. Section 40(2)(a) covers customer identification and due-diligence records — the documents and information gathered to establish who a customer is. Section 40(2)(b) covers transaction-level data capable of identifying a customer — records of what a customer has done, not who they are. A dataset combining the two, such as a transaction log tagged with the customer's verified identity, would likely engage both categories simultaneously, though the Act does not state this combination explicitly and treats the two as separately defined categories of sensitive information.

This distinction matters for a Licensee's data architecture. Segregating "sensitive information" under section 40(1) is not a single technical boundary around one dataset — it potentially requires separate controls around identity records, transaction records, key material, and proprietary systems, each of which may need to be treated as sensitive even where the others are not present in the same system.

## What obligations follow from data being classified as "sensitive information"?

Section 40(2) supplies the definition; section 40(3) and section 40(4) supply the operative controls that attach to anything falling within it — logical and technical segregation, need-to-know access, encryption and secure key management, and audit trails, with detailed technical standards left to future Regulations. These controls are addressed in full in a companion analysis of section 40(3) and (4), and are not repeated here in detail, but the essential point is that classification under section 40(2) is the trigger — a dataset that falls within one of the five categories is automatically subject to those downstream controls, whether or not the Licensee has separately labelled it as "sensitive" internally.

## What should a VASP do to correctly classify its data under section 40?

- map every dataset the business holds against the four fixed categories in section 40(2)(a) to (d), rather than assuming only obviously customer-facing data qualifies
- treat proprietary trading data and risk-management systems as sensitive information requiring the same rigour as customer records, since section 40(2)(d) places them in the same category
- build a process for tracking Authority designations under section 40(2)(e), since the sensitive-information perimeter can expand without notice through this open-ended category
- avoid conflating identity data and transaction data into a single "customer data" bucket internally, since the Act defines them as separate categories under section 40(2)(a) and (b)
- treat private keys and wallet authentication data as the highest-consequence category in practice, since section 40(2)(c) is the category most directly tied to irreversible loss of [customer assets](https://www.coinconnect.site/blog/3/customer-assets-definition-pvara-pakistan-62) if exposed

Section 40(2) gives every VASP a concrete starting checklist rather than a vague instruction to "protect sensitive data." Firms preparing their [regulatory licensing](https://www.coinconnect.site/regulatory-licensing) application should classify their data holdings against these five categories explicitly, document the classification, and be ready to show [PVARA](https://www.coinconnect.site/pvara-guide) how each category is treated differently — because the Act itself treats them as distinct, not interchangeable.

## Related reading

- [PVARA Exchange License: Capital, Rules & Obligations 2026](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-exchange-license-requirements-capital-obligations-24)
- [PVARA Transfer & Settlement License: Crypto Payments 2026](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-transfer-settlement-license-payments-remittance-28)
- [PVARA Licensing Process: NOC to Full Licence, Step by Step](https://blog.coinconnect.site/pvara-licensing-process-noc-to-full-licence-step-by-step/)
- [The PVARA Licensing Gold Rush: Pakistan's Crypto Frontier](https://www.coinconnect.site/blog/3/blogpvara-licensing-gold-rush-pakistan-crypto-frontier-56)
- [PVARA Custody License: Safeguard Customer Crypto 2026](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-custody-license-safeguarding-customer-assets-25)

## About this analysis

This analysis was prepared by the CoinConnect research desk from the Virtual Assets Act, 2026, read as published. Where practice is not yet settled or guidance has not been issued, that is stated in the text above.

Regulatory positions change and specific requirements should be verified against the current position published by the relevant authority before you act on them. This is information and analysis, not legal advice, and it does not create an advisory relationship. Take professional advice on your own circumstances.

## Flags for Malik

- The rationale I gave for why proprietary trading data (category d) sits alongside customer-facing categories is my own inference from the nature of the data types, not a stated explanation in the Act — clearly flagged as "our reading."
- I referenced section 40(3) and (4) briefly as the operative controls following classification, without restating their content in full, since that is the subject of a companion article (108) rather than this one — worth checking the two pieces read consistently together once both are live.
- No Regulations designating additional sensitive-information categories under section 40(2)(e) existed in the source documents, so none are named.
