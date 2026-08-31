---
layout: post
title: "Cross-Border Outsourcing: Making Audit Rights Enforceable"
date: 2026-01-01 09:00:00 +0500
categories: [Compliance]
author: "Malik Abbas"
description: "Regulation 14.1(d) requires PVARA applicants to make audit rights over AML vendors legally enforceable, including across borders — what that means in practice."
---

A contract clause granting an applicant the right to audit its compliance vendor is only worth what it can achieve if the vendor refuses to cooperate. Pakistan's pre-[licensing framework](https://www.coinconnect.site/pvara-guide) treats that gap directly, requiring not just the right on paper but its practical enforceability, with cross-border arrangements called out by name.

This analysis reads regulation 14.1(d) of the PVARA [No Objection Certificate](https://www.coinconnect.site/regulatory-licensing) Regulations 2025 alongside Form A5, the statutory outsourcing declaration issued under regulation 14, and sets out what an enforceable cross-border audit right actually requires.

## What does regulation 14.1(d) actually require, beyond having an audit clause?

Regulation 14.1 permits an applicant to outsource an [AML](https://www.coinconnect.site/blog/3/fit-and-proper-aml-pvara-mistakes-54)-critical function only where four conditions are all met. The fourth is the enforceability condition. The Regulations state:

> "(d) ensures the legal enforceability of audit and supervisory rights, including cross-border arrangements."

This is a distinct requirement from condition (c), which simply requires the applicant to "retain audit and inspection rights." Condition (c) is satisfied by the contract text existing; condition (d) asks whether that text would actually hold up if the applicant tried to use it — and it names cross-border arrangements specifically as a context where this needs active attention, not passive assumption. In practice, our reading is that an applicant relying on a standard vendor services agreement drafted under a foreign jurisdiction's law, without checking whether an audit and inspection clause in that agreement is actually enforceable against the vendor in its home courts or under an applicable arbitration mechanism, has not met condition (d) even if condition (c) is satisfied on paper.

## Why is cross-border enforceability harder than domestic enforceability?

Regulation 14.1(d) does not explain the mechanics of cross-border enforcement, and this analysis does not invent legal doctrine the source document does not state. What the text does make clear is that PVARA treats cross-border arrangements as a named risk category requiring its own verification step, separate from the general audit-rights condition. Three practical frictions follow from that framing, though PVARA has not itself detailed them in the Regulations reviewed:

- A contractual right to audit means little if the vendor's home jurisdiction does not recognise the applicant's standing to compel compliance, or if enforcement requires a lengthy foreign judgment-recognition process.
- Data protection and localisation rules in the vendor's home country may restrict what the vendor can actually hand over during an audit, regardless of what the contract promises.
- Where a dispute over audit access arises, the applicant needs a pre-agreed mechanism — litigation venue, arbitration seat, or regulator-to-regulator cooperation — rather than discovering only after the fact that no workable route exists.

## What must the outsourcing contract contain, according to Form A5?

Form A5, the Outsourcing Declaration and Register issued under regulation 14, requires the Applicant's Compliance Officer to confirm specific contractual content before an NOC is granted. Section A of Form A5 states that the Applicant confirms all outsourcing contracts include:

> "appropriate service levels; data protection and confidentiality clauses; audit and inspection rights for the Applicant and PVARA; termination rights; controls to prevent unauthorised sub-outsourcing."

Note that the audit and inspection rights named here must run to the Applicant and to PVARA — meaning the contract has to grant the regulator its own access, not merely give the applicant a right it may or may not choose to use. Section A also requires the Applicant to confirm that "no outsourcing arrangement prevents or restricts the Applicant from complying with AMLA 2010, PVARA Regulations or FMU reporting requirements" — a clause aimed directly at the scenario where a foreign vendor's own data-handling restrictions could otherwise stand in the way of a Pakistani reporting obligation.

## What information does the outsourcing register require for each cross-border vendor?

Section B of Form A5 requires the Compliance Officer to complete a line-item register for every outsourced AML-relevant service. The table below sets out the fields most relevant to cross-border arrangements specifically.

| Register field | What it captures |
|---|---|
| Country of Incorporation / Operation | Where the vendor is based — the trigger for regulation 14.1(d) scrutiny |
| Function Outsourced | What AML task the vendor performs (e.g. blockchain analytics, transaction monitoring) |
| Data Shared With Provider | Whether KYC data, wallet addresses or logs cross the border to reach the vendor |
| Audit Rights | Yes/No — whether the contract grants audit access |
| Sub-Outsourcing Permitted | Yes/No — whether the vendor can itself delegate the work further |
| Termination Rights | Standard / Enhanced / None — the applicant's ability to exit the arrangement |
| Risk Assessment Summary | A Low/Medium/High rating with justification |

Recording "Country of [Incorporation](https://www.coinconnect.site/corporate-setup) / Operation" as a mandatory field means PVARA can identify every cross-border outsourcing relationship in the applicant's book at a glance during NOC assessment, rather than needing to infer it from the narrative sections of Form A1. A vendor register that answers "Yes" to Audit Rights but is based in a jurisdiction with no practical enforcement route available is exactly the gap regulation 14.1(d) is written to catch — and the risk rating field gives the Compliance Officer a place to flag that mismatch honestly rather than leaving it implicit.

## What data protection issue sits alongside the enforceability question?

Section 39 of the [Virtual Assets Act](https://blog.coinconnect.site/pakistans-virtual-assets-act-2026-the-complete-guide/), 2026 permits a Licensee to store or process data outside Pakistan, but only "subject to compliance with applicable laws relating to data protection, cybersecurity, and cross-border data transfers, and subject to such safeguards as shall be prescribed by Regulations." Section 39(2) separately preserves PVARA's power to require immediate localisation of specific datasets "where necessary in the interest of national security, financial stability, consumer protection, or enforcement effectiveness."

Read alongside regulation 14.1(d), this means a cross-border outsourcing arrangement carries two separate but related exposures: whether the applicant's audit rights over the vendor are enforceable, and whether the underlying customer data the vendor processes complies with Pakistan's data localisation and cross-border transfer rules at all. A contract can satisfy one of these questions without the other — enforceable audit rights do not, by themselves, establish that the underlying data transfer was lawful in the first place.

## What happens if these arrangements are found deficient after an NOC is granted?

Regulation 18.1(b) of the NOC Regulations requires a registered Applicant to "notify the Authority of any material changes affecting AML compliance, governance, ownership or technology" — a duty that, on its face, would capture a material change to an outsourcing arrangement, such as a vendor relocating operations to a new jurisdiction or losing the ability to grant contractual audit access. Regulation 19.1(d) lists "systemic or material AML/CFT failures" as grounds for revocation of an Applicant's NOC status, which regulation 14.2 makes clear an outsourcing arrangement cannot excuse, since it "must not impair the Applicant's ability to meet AMLA or PVARA obligations."

Two practical points follow for firms structuring cross-border vendor relationships:

- Verify enforceability of an audit clause against the vendor's home jurisdiction before signing, not after a dispute arises — regulation 14.1(d) treats this as a condition of lawful outsourcing, not a nice-to-have.
- Complete the Form A5 register honestly, including a genuine risk rating, since PVARA's assessment under regulation 16.1 draws directly on this documentation rather than the applicant's narrative assurances alone.

## Related reading

- [PVARA Exchange License: Capital, Rules & Obligations 2026](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-exchange-license-requirements-capital-obligations-24)
- [PVARA Transfer & Settlement License: Crypto Payments 2026](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-transfer-settlement-license-payments-remittance-28)
- [PVARA Licensing Process: NOC to Full Licence, Step by Step](https://blog.coinconnect.site/pvara-licensing-process-noc-to-full-licence-step-by-step/)
- [The PVARA Licensing Gold Rush: Pakistan's Crypto Frontier](https://www.coinconnect.site/blog/3/blogpvara-licensing-gold-rush-pakistan-crypto-frontier-56)
- [PVARA Custody License: Safeguard Customer Crypto 2026](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-custody-license-safeguarding-customer-assets-25)

## About this analysis

This analysis was prepared by the CoinConnect research desk from regulations 14.1, 14.2, 18.1 and 19.1 of the PVARA No Objection Certificate Regulations 2025, Form A5 of the same Regulations, and sections 39 and 46 of the Virtual Assets Act, 2026 as passed by the National Assembly, each read as published. Regulation 14.1(d) does not itself describe the specific legal mechanics of cross-border enforcement (choice of forum, arbitration, mutual recognition), and none are invented here beyond what the text supports. Where practice is not yet settled or guidance has not been issued, that is stated in the text above.

Regulatory positions change and specific requirements should be verified against the current position published by the relevant authority before you act on them. This is information and analysis, not legal advice, and it does not create an advisory relationship. Take professional advice on your own circumstances.

## Flags for Malik

1. I connected regulation 14.1(d) to section 39's data localisation provisions as a related-but-separate risk — this is my own analytical framing, not something the source documents state explicitly link together. Worth a sanity check.
2. I did not name specific enforcement mechanisms (arbitration seats, treaty frameworks) since none are specified in the three source documents. If CoinConnect has operator-side experience structuring these clauses, that would strengthen a revision considerably.
3. This is the second of a two-part pair with article 083 (outsourcing restrictions generally) — I kept 083 focused on the definitional/conditions question and this one on the enforceability/cross-border mechanics specifically to avoid repeating the same blockquotes.
