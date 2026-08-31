---
layout: post
title: "Which AML Functions Can a Pakistani VASP Not Outsource?"
date: 2026-01-01 09:00:00 +0500
categories: [Compliance]
author: "Malik Abbas"
description: "PVARA's NOC Regulations name CDD, sanctions screening, monitoring and MLRO duties as AML-critical, and set four conditions before they can go to a vendor."
---

Outsourcing compliance technology is normal practice for a new [virtual asset service provider](https://www.coinconnect.site/blog/coinconnect-insights-1/vasp-license-pakistan-3) ("VASP") — few applicants build blockchain analytics or transaction monitoring software in-house. What Pakistan's pre-[licensing framework](https://www.coinconnect.site/pvara-guide) does not permit is outsourcing the accountability that sits behind those functions.

This analysis reads regulation 14.1 of the PVARA [No Objection Certificate](https://www.coinconnect.site/regulatory-licensing) Regulations 2025 as published and sets out which functions it names as [AML](https://www.coinconnect.site/blog/3/fit-and-proper-aml-pvara-mistakes-54)-critical, and the four conditions attached to using a third party for them.

## Which AML functions does regulation 14.1 treat as off-limits to outsource freely?

Regulation 14.1 names five specific functions as "AML-critical," meaning functions that "go to the core of the Applicant's AML/CFT duties." The Regulations state:

> "Applicants may not outsource AML-critical functions, meaning those that go to the core of the Applicant's AML/CFT duties such as CDD, EDD, sanctions/TFS screening, transaction monitoring, STR/CTR reporting and MLRO responsibilities, unless the Applicant..."

That sentence names customer due diligence ("CDD"), enhanced due diligence ("EDD"), sanctions and targeted financial sanctions ("TFS") screening, transaction monitoring, suspicious and currency transaction report ("STR"/"CTR") reporting, and Money Laundering Reporting Officer ("MLRO") responsibilities as the functions caught by the rule. The word "such as" before the list matters: on its plain wording, regulation 14.1 gives examples of AML-critical functions rather than a closed list, so a function not named here could still fall inside the prohibition if it genuinely "goes to the core" of the applicant's AML/CFT duties. The Regulations do not define a boundary test beyond that phrase, and this analysis does not attempt to supply one where the source document does not.

## Does regulation 14.1 ban outsourcing these functions outright?

No. The prohibition is conditional, not absolute — regulation 14.1 permits outsourcing of AML-critical functions where four specific conditions are met. Read in full, the Regulations state that Applicants may not outsource these functions "unless the Applicant:"

> "(a) conducts due diligence on the service provider; (b) maintains effective oversight arrangements; (c) retains audit and inspection rights; and (d) ensures the legal enforceability of audit and supervisory rights, including cross-border arrangements."

All four conditions read together, not as alternatives — the "and" joining (c) and (d) signals a conjunctive test. In practice, our reading is that an applicant cannot satisfy regulation 14.1 by contracting for audit rights on paper (condition (c)) while leaving those rights practically unenforceable against a foreign vendor (condition (d)). The two conditions are related but distinct: (c) is about the contract granting the right, and (d) is about whether that right actually holds up, including where the vendor sits in another jurisdiction.

| Condition | What it requires of the applicant |
|---|---|
| Due diligence on the provider | Assess the vendor before appointing it, not only afterward |
| Effective oversight arrangements | Ongoing supervision of the outsourced function, not a one-time onboarding check |
| Audit and inspection rights | The contract must grant the applicant the right to audit and inspect the vendor's work |
| Legal enforceability of those rights | The audit and supervisory rights must be enforceable in practice, including across borders |

## Why does cross-border enforceability get named specifically?

Regulation 14.1(d) singles out "cross-border arrangements" because a large share of the AML-critical functions VASPs are likely to outsource — blockchain analytics, sanctions screening databases, KYC verification tools — are typically supplied by vendors headquartered outside Pakistan. Our reading is that PVARA is anticipating exactly this pattern and closing off a foreseeable gap: a contract clause granting audit rights against a foreign vendor is not automatically worth the same as the identical clause against a Pakistani one, because enforcing it may require litigating or arbitrating in another jurisdiction under another jurisdiction's procedural rules. Form A5, the [Outsourcing](https://www.coinconnect.site/regulatory-licensing) Declaration and Register issued under regulation 14, requires the applicant's Compliance Officer to record the "Country of [Incorporation](https://www.coinconnect.site/corporate-setup) / Operation" for every outsourced service provider precisely so this exposure is visible to PVARA at the point of NOC assessment, not discovered later.

## What must an outsourcing contract actually contain?

Form A5, issued under regulation 14 of the NOC Regulations, translates the four conditions in regulation 14.1 into specific contractual terms the applicant must confirm are in place. Section A of Form A5 requires the Applicant to declare that all outsourcing contracts include:

> "appropriate service levels; data protection and confidentiality clauses; audit and inspection rights for the Applicant and PVARA; termination rights; controls to prevent unauthorised sub-outsourcing."

Two details in that list go beyond what regulation 14.1 states directly. First, the audit and inspection rights have to run to PVARA itself, not only to the applicant — a contract that lets the applicant audit its vendor but gives the regulator no equivalent access does not, on the wording of Form A5, satisfy the declaration. Second, Form A5 requires "controls to prevent unauthorised sub-outsourcing," meaning the applicant is expected to police whether its vendor is itself relying on a further sub-contractor to perform the AML-critical work — a risk regulation 14.1 does not mention by name but that Form A5 treats as material.

Form A5's outsourcing register also asks the Compliance Officer to record, for each outsourced AML function, whether audit rights exist, whether sub-outsourcing is permitted, what data is shared with the provider, and a risk rating of low, medium or high — creating a documented inventory PVARA can review rather than relying on the applicant's general assurance that regulation 14.1 has been met.

## Does outsourcing reduce the applicant's own responsibility?

No. Regulation 14.2 makes clear that outsourcing does not transfer, dilute or cap the applicant's own regulatory exposure. The Regulations state:

> "Outsourcing arrangements must not impair the Applicant's ability to meet AMLA or PVARA obligations."

"AMLA" refers to the Anti-Money Laundering Act, 2010, which section 46(1) of the [Virtual Assets Act](https://blog.coinconnect.site/pakistans-virtual-assets-act-2026-the-complete-guide/), 2026 separately applies to every licensed VASP by deeming it a financial institution for AMLA purposes. Form A5 restates the same principle from the applicant's side, requiring the Compliance Officer to confirm that "the Applicant retains full responsibility and oversight for all outsourced functions." In practice, our reading is that an applicant cannot point to a vendor's failure as a defence to a compliance breach — regulation 14.2 places the full weight of AMLA and PVARA obligations on the applicant regardless of which functions it has outsourced, and this sits alongside the [fit and proper](https://www.coinconnect.site/blog/coinconnect-insights-1/url-slug-fit-and-proper-test-pvara-form-a3-14) accountability the MLRO and Compliance Officer already carry personally.

Two practical points follow for firms scoping their outsourcing arrangements:

- Treat "such as" in regulation 14.1 as a non-exhaustive signal — a function not named in the list can still be AML-critical if it goes to the core of AML/CFT duties.
- Audit rights that exist on paper but cannot practically be enforced against a foreign vendor do not meet condition (d), regardless of what condition (c) already grants.

## Related reading

- [PVARA Exchange License: Capital, Rules & Obligations 2026](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-exchange-license-requirements-capital-obligations-24)
- [PVARA Transfer & Settlement License: Crypto Payments 2026](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-transfer-settlement-license-payments-remittance-28)

## About this analysis

This analysis was prepared by the CoinConnect research desk from regulations 14.1 and 14.2 of the PVARA No Objection Certificate Regulations 2025, together with Form A5 of the same Regulations and section 46(1) of the Virtual Assets Act, 2026 as passed by the National Assembly, each read as published. Regulation 14.1 does not define the outer boundary of "functions that go to the core" of AML/CFT duties beyond the named examples, and no such boundary is invented here. Where practice is not yet settled or guidance has not been issued, that is stated in the text above.

Regulatory positions change and specific requirements should be verified against the current position published by the relevant authority before you act on them. This is information and analysis, not legal advice, and it does not create an advisory relationship. Take professional advice on your own circumstances.

## Flags for Malik

1. I read "such as" in regulation 14.1 as making the list non-exhaustive — this is a plain-text reading, not a PVARA interpretive statement, since no guidance on the point exists in our three source documents. Worth confirming against any PVARA FAQ or circular if one is issued.
2. I did not attempt to define a threshold for what makes a non-listed function "go to the core" of AML/CFT duties — that judgement call sits outside what the source text supports.
3. This pairs naturally with the cross-border outsourcing article (084) — I've kept the emphasis here on the definition/conditions and left the deeper contractual mechanics for that piece to avoid duplicating content.
