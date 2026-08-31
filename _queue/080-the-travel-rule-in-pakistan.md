---
layout: post
title: "The Travel Rule in Pakistan"
date: 2026-01-01 09:00:00 +0500
categories: [Compliance]
author: "Malik Abbas"
description: "Section 47 of the Virtual Assets Act sets Pakistan's Travel Rule: originator and beneficiary data, FATF alignment, and a record-retention floor."
---

The "Travel Rule" is FATF shorthand for a requirement most [virtual asset](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-license-pakistan-complete-guide-22) businesses have already met in some form elsewhere: when a transfer of value crosses from one institution to another, information about who sent it and who is receiving it has to travel with the transfer itself, not stay locked inside the sending institution's own records.

Section 47 of the [Virtual Assets Act](https://blog.coinconnect.site/pakistans-virtual-assets-act-2026-the-complete-guide/), 2026 writes that requirement into Pakistani law for licensed virtual asset service providers. This article reads section 47 as passed, sets out what it requires, and separates the statutory text from the parts of the obligation the Act leaves to future Regulations.

## What does section 47 of the Act actually require?

A licensee has to obtain, hold and transmit originator and beneficiary information for virtual asset transfers that meet or exceed a threshold the Pakistan Virtual Asset Regulatory Authority ("[PVARA](https://www.coinconnect.site/pvara-guide)" or "the Authority") sets, and has to do so consistently with the Financial Action Task Force's own recommendations. Section 47(1) reads:

> "A Licensee shall obtain, hold and transmit originator and beneficiary information in any transfer of Virtual Assets meeting or exceeding the threshold prescribed by the Authority, in a manner consistent with Recommendations of Financial Action Task Force, as updated from time to time."

Four things follow from that single subsection. First, the duty covers all three stages of the information's lifecycle — obtaining it, holding it, and transmitting it — not merely collecting it at onboarding and filing it away. Second, the obligation attaches specifically to "originator and beneficiary information," meaning identifying data about both the sender and the recipient of a transfer, not just the licensee's own customer. Third, the trigger is a threshold the Authority itself sets by Regulation — the Act does not fix a value in section 47 itself, so the operative figure is not yet published in the source documents reviewed for this analysis. Fourth, the compliance standard is tied to an external, moving target: the Financial Action Task Force's ("FATF") Recommendations, "as updated from time to time" — meaning the obligation is designed to track FATF's own evolving standard rather than freeze it at the text as it reads today.

## Who is FATF, and why does Pakistani law defer to its recommendations?

FATF is the intergovernmental body that sets the global standards on [anti-money laundering](https://www.coinconnect.site/blog/3/fit-and-proper-aml-pvara-mistakes-54) and countering the financing of terrorism; its recommendations, including Recommendation 16, are the source of what is commonly called the Travel Rule internationally, and its own material sits at [fatf-gafi.org](https://www.fatf-gafi.org/). Pakistan's own explanatory material behind the Act states the legislative intent directly, in the Statement of Objects and Reasons: the framework aims to combat money laundering and terrorist financing "in accordance with international standards", and section 46(3) of the Act separately requires PVARA to "align its supervisory framework with the standards of the Financial Action Task Force" through its own AML, CFT and CPF Regulations.

Section 47(1)'s reference to FATF Recommendations "as updated from time to time" is the mechanism that keeps section 47 current without requiring Parliament to amend the Act each time FATF revises its guidance. In practice, this means a licensee cannot treat compliance with section 47 as a fixed checklist frozen at the point of licensing — the "manner consistent with" standard moves as FATF's own recommendations move, and PVARA's own Regulations under section 47(3) are the mechanism by which that international standard gets translated into a specific Pakistani filing requirement.

## What information counts as "originator and beneficiary information"?

The Act does not itself define the term in section 47, or list the specific data fields required. This is a gap the text leaves open, and it should be read as deliberately structural rather than an oversight: section 47(3) gives PVARA the power to "prescribe detailed procedures, standards, and formats for record-keeping, reporting, and transmission of information through Regulations." Internationally, Travel Rule regimes modelled on FATF Recommendation 16 typically require, at minimum, the originator's name, account or wallet identifier, and address or another form of identifying data, together with equivalent beneficiary details — but Pakistan's own version of that field list is not stated in the Act itself and has not, on the documents reviewed, yet been published as a PVARA Regulation. Applicants should not assume a specific field list until PVARA issues it, and should build data-collection processes flexible enough to accommodate a prescribed format once it exists.

## How does section 47 interact with data protection and cybersecurity law?

The Travel Rule obligation does not override Pakistan's other data protection rules — it has to be carried out inside them. Section 47(2) states:

> "Such obligations shall be implemented in compliance with applicable data protection, data governance, and cybersecurity laws, ensuring the confidentiality, integrity, and security of the information."

This connects directly to section 5(2) of the Act, which provides that where any other law prescribes measures relating to data protection, data governance, cybersecurity, financial secrecy or cross-border transfer of personal data, those provisions "shall prevail and be complied with" by the Authority and licensees — one of the few places the Act expressly subordinates itself to other legislation rather than asserting overall precedence. A licensee building its Travel Rule transmission process therefore has to solve two problems together, not sequentially: moving originator and beneficiary data between institutions in the manner FATF-aligned standards require, while simultaneously meeting whatever data protection and cybersecurity obligations apply under Pakistan's separate data protection framework. Section 40 of the Act reinforces the same discipline internally, requiring licensees to segregate sensitive information — including customer due-diligence records and transaction-level data capable of identifying a customer — from other operational data, with encryption, tokenisation and access controls applied on a need-to-know basis.

## How long must originator and beneficiary records be kept?

At least as long as the Anti-Money Laundering Act, 2010 requires, and potentially longer if PVARA prescribes a longer period. Section 47(4) sets the retention floor:

> "A Licensee shall maintain records of transactions, customer due-diligence data and risk assessments for a period prescribed by Regulations, which shall not be less than the period required under the Anti-Money Laundering Act, 2010 (VII of 2010)."

The provision works as a floor, not a fixed figure. PVARA's own Regulations set the applicable period, but whatever period PVARA prescribes cannot be shorter than the Anti-Money Laundering Act, 2010 ("AMLA 2010") requirement — a statute outside the three source documents reviewed for this analysis, and one that should be consulted directly for its own specific retention duration. Separately, the PVARA [No Objection Certificate](https://www.coinconnect.site/regulatory-licensing) Regulations 2025 fix a seven-year minimum retention period for AML/CFT records generally, stored securely and kept auditable, retrievable and tamper-evident — a figure that gives a practical benchmark for [how long](https://www.coinconnect.site/blog/3/how-long-pvara-license-takes-39) Travel Rule data is likely to need to be held, even though section 47(4) itself leaves the exact period to Regulations rather than stating seven years directly.

## How does the Travel Rule fit alongside PVARA's other AML obligations?

Section 47 sits inside Chapter 8 of the Act, alongside the wider anti-money laundering, counter-terrorism-financing and counter-proliferation-financing framework. Section 46(1) deems every licensed [virtual asset service provider](https://www.coinconnect.site/blog/coinconnect-insights-1/vasp-license-pakistan-3) a financial institution for the purposes of AMLA 2010, and section 46(2) separately requires reporting of suspicious transactions to the Financial Monitoring Unit, maintenance of customer due-diligence and transaction records, and internal controls including the appointment of an AML, CFT or CPF compliance officer. Section 48 requires licensees to establish secure reporting channels and, where required, automated interfaces enabling PVARA and other notified agencies to access prescribed data for supervisory purposes.

| Provision | What it covers |
|---|---|
| Section 46 | VASPs deemed financial institutions under AMLA 2010; STR filing; compliance officer |
| Section 47(1) | Originator/beneficiary data obtained, held and transmitted, above a PVARA-set threshold, FATF-aligned |
| Section 47(2) | Implementation subject to data protection, governance and cybersecurity law |
| Section 47(3) | PVARA's power to prescribe detailed Travel Rule procedures and formats |
| Section 47(4) | Record retention floor tied to AMLA 2010 |
| Section 48 | Real-time data access and secure reporting interfaces for PVARA and notified agencies |

Read together, section 47 is the data-transmission piece of a wider reporting architecture — it governs what travels with a transfer between institutions, while section 46 governs what gets reported to the state when something looks suspicious, and section 48 governs how PVARA itself gets access to the underlying data on an ongoing basis. A [virtual asset service provider](https://www.coinconnect.site/blog/coinconnect-insights-1/vasp-license-pakistan-3) building its compliance stack should treat all three as one connected system rather than three separate filing exercises, since the same transaction data typically flows through each.

## Related reading

- [PVARA Exchange License: Capital, Rules & Obligations 2026](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-exchange-license-requirements-capital-obligations-24)
- [PVARA Transfer & Settlement License: Crypto Payments 2026](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-transfer-settlement-license-payments-remittance-28)

## About this analysis

This analysis was prepared by the CoinConnect research desk from sections 5(2), 40, 46, 47 and 48 of the Virtual Assets Act, 2026 as passed by the National Assembly, together with the Statement of Objects and Reasons appended to the Act, and cross-referenced against the seven-year retention standard in the PVARA No Objection Certificate Regulations 2025, read as published. The Anti-Money Laundering Act, 2010, referenced directly by section 47(4), was not among the three source documents reviewed, and its specific retention period is not restated here. Where practice is not yet settled or guidance has not been issued, that is stated in the text above.

Regulatory positions change and specific requirements should be verified against the current position published by the relevant authority before you act on them. This is information and analysis, not legal advice, and it does not create an advisory relationship. Take professional advice on your own circumstances.

## Flags for Malik

1. Section 47(1) leaves the actual Travel Rule threshold to a future PVARA Regulation, and it has not, on the documents reviewed, been published yet — I have not guessed at a figure. Worth checking whether PVARA has since issued this Regulation, since the threshold is the single most commercially relevant number in the whole provision.
2. Section 47's own text does not define "originator and beneficiary information" with a specific field list. I described the FATF Recommendation 16 convention (name, account/wallet identifier, address) as international context for what such regimes typically require, clearly separated from what Pakistan's own statute says — please check this framing doesn't read as implying it is already the Pakistani standard, since it is only offered as background.
3. Section 47(4)'s AMLA 2010 retention floor was not verifiable against AMLA 2010 itself, which was outside the three source documents provided for this batch. I used the seven-year NOC Regulations figure as a practical benchmark only, flagged explicitly as not the same as the section 47(4) floor itself.
