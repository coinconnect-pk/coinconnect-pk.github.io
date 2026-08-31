---
layout: post
title: "Proof of Reserves and the Annual Audit for Pakistani VASPs"
date: 2026-01-01 09:00:00 +0500
categories: [Compliance]
author: "Malik Abbas"
description: "Section 27 of the Virtual Assets Act 2026 requires cryptographic proof-of-reserves and an annual segregation audit. Here is what each obligation actually covers."
---

Segregating [customer assets](https://www.coinconnect.site/blog/3/customer-assets-definition-pvara-pakistan-62) and promising not to touch them, as sections 24(1) and 24(4) of the [Virtual Assets Act](https://blog.coinconnect.site/pakistans-virtual-assets-act-2026-the-complete-guide/), 2026 require, only protects customers if someone is checking that the promise is being kept. Section 27 is the verification layer of the Act's [custody](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-custody-license-safeguarding-customer-assets-25) regime — it requires a [virtual asset service provider](https://www.coinconnect.site/blog/coinconnect-insights-1/vasp-license-pakistan-3) to prove, on an ongoing basis, that customer holdings actually exist and match what customers are owed, and to have that proof independently audited every year.

This article sets out what section 27 requires, how its two limbs — proof-of-reserves and the annual audit — differ and reinforce each other, and where the detail is still left to Regulations.

## What does section 27 of the Virtual Assets Act 2026 require?

Section 27 imposes two separate obligations on every Licensee: furnishing cryptographic proof-of-reserves reconciled against customer liabilities at prescribed intervals, and undergoing an annual audit by an approved firm of Chartered Accountants that specifically verifies the segregation of Customer Assets required under section 24.

Section 27(1) states:

> A Licensee shall furnish to the Authority, at such intervals as may be Prescribed by Regulations, cryptographic proof-of-reserves reconciled against its liabilities to customers.

Section 27(2) states:

> A Licensee shall cause its operations to be audited annually by a firm of Chartered Accountants approved by the Division concerned. Such audit shall include a verification of the segregation of Customer Assets as required under section 24.

The two obligations run on different timelines and answer different questions. Proof-of-reserves under section 27(1) is furnished at intervals set by Regulations — meaning it could be required more frequently than annually — and answers the question "do the assets exist right now, and do they match what is owed to customers." The annual audit under section 27(2) runs on a fixed yearly cycle and answers a broader question: is the firm's operation, including its segregation practice, actually structured the way section 24 requires.

## What is "cryptographic proof-of-reserves" in this context?

The Act does not define the term further, but the phrase describes a verification method, well established in the wider [virtual asset](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-license-pakistan-complete-guide-22) industry, that uses cryptographic techniques to demonstrate a firm's holdings without necessarily disclosing the underlying customer account data in full. Typically, this involves a Merkle-tree structure that lets each customer independently verify their own balance is included in the total the firm claims to hold, combined with on-chain proof that the firm controls wallets holding assets equal to or exceeding the sum of customer liabilities.

Section 27(1) requires the proof to be "reconciled against its liabilities to customers" — meaning the proof-of-reserves exercise is not simply a demonstration that the firm holds some quantity of assets, but a specific matching exercise between assets held and the total the firm owes its customers. A firm that holds substantial assets but cannot show they are properly reconciled against liabilities has not met the requirement of section 27(1) as drafted.

The interval at which this proof must be furnished is left to Regulations, which had not been published at the time of writing. Firms should not assume proof-of-reserves is an annual exercise aligned with the section 27(2) audit — the statute allows the Authority to set a shorter, more frequent interval, and given how quickly a shortfall can develop in a firm handling customer trading and withdrawals daily, a quarterly or even monthly cadence would not be an unusual regulatory choice by international comparison.

## What does the annual audit under section 27(2) actually cover?

Section 27(2) requires the audit to cover the Licensee's operations generally, with an explicit requirement that it include verification of the section 24 segregation of Customer Assets. This is broader in scope than the proof-of-reserves exercise under section 27(1), which is narrowly focused on the reserves-versus-liabilities reconciliation.

Three features of section 27(2) are worth reading closely. First, the audit must be conducted by "a firm of Chartered Accountants approved by the Division concerned" — meaning the Licensee cannot simply choose any auditor; the audit firm must carry approval from the Cabinet Division, as defined in section 3(1)(viii) referencing the Rules of Business, 1973. Second, the audit is annual, a fixed statutory cadence, unlike the section 27(1) proof-of-reserves interval which is left open to Regulations. Third, the audit's coverage of segregation is described as something the audit "shall include" — meaning segregation verification is a mandatory minimum component of the audit, not the entirety of what the audit must cover; "operations" more broadly is the stated scope.

This connects section 27(2) directly to section 15(4), which requires the Authority's own accounts to be audited by the Auditor General of Pakistan and a firm of Chartered Accountants nominated by the Auditor General — a parallel, though separate, audit obligation that applies to the regulator itself rather than to Licensees.

## How do proof-of-reserves and the annual audit reinforce each other?

Proof-of-reserves is the higher-frequency, narrower check; the annual audit is the lower-frequency, broader check. Run together, they close different gaps a firm could otherwise exploit. A firm could, in principle, present an accurate proof-of-reserves snapshot on the specific day or dates the Regulations require it, while its actual day-to-day operational practice around segregation is weaker than the snapshot suggests. The annual audit under section 27(2) is structured to catch that gap, because it examines the firm's operations and segregation practice more broadly, rather than relying solely on point-in-time cryptographic snapshots.

Read together with sections 24(3) and 24(4), the audit and reconciliation requirements in section 27 are the mechanism that would surface a breach of the fiduciary duty or the rehypothecation prohibition. A Licensee that has lent out or pledged Customer Assets without valid consent, in breach of section 24(4), would in principle show up as a shortfall between customer liabilities and actual reserves — precisely what the section 27(1) reconciliation and the section 27(2) segregation audit are designed to detect.

## Who receives the proof-of-reserves and the audit results?

Section 27(1) states the proof-of-reserves is furnished "to the Authority" — it is a regulatory reporting obligation, not, on the text, a requirement to publish the proof to customers or the public directly. Section 27(2) is silent on who receives the audit report, though section 22(c) separately requires a Licensee to submit periodic returns, reports and audited financial statements as may be prescribed — which strongly suggests the section 27(2) audit output flows to the Authority through that same reporting channel.

Neither sub-section of section 27 explicitly requires public disclosure of reserve data to customers. This differs from the disclosure regime the Act builds for token issuers: section 42(2) requires Issuers to make ongoing disclosures of material information, "including reserve attestations", in the manner and frequency Regulations prescribe. Our reading is that section 27's proof-of-reserves and audit obligations are primarily supervisory tools for the Authority, while public reserve attestation is addressed separately, and more explicitly, for Issuers under section 42. A Licensee should not assume that meeting its section 27 obligations to the Authority also discharges any customer-facing transparency expectations that market practice, rather than the Act itself, may create.

## How does section 27 apply to reserve custodians specifically?

Section 28 imposes a separate, parallel obligation on the custodian of reserve assets — the entity actually holding the reserves, which may or may not be the Licensee itself — requiring compliance with requirements, oversight and inspection standards to be prescribed by Regulations. Section 27 obliges the Licensee to furnish proof-of-reserves and undergo audit; section 28 obliges whoever is physically holding those reserve assets to meet the Authority's oversight standards.

This distinction matters for firms that use a third-party custodian rather than self-custodying customer assets. Outsourcing custody does not relieve the Licensee of its section 27 obligations to reconcile and prove reserves to the Authority — it simply means the Licensee's reconciliation exercise depends on data and cooperation from a custodian who is, separately, subject to section 28's own oversight standards. Building a proof-of-reserves process that depends on a third party's timely, accurate reporting is a dependency worth stress-testing before it becomes a live compliance gap.

## What should a Licensee build now, ahead of the Regulations on intervals and format?

The specific proof-of-reserves interval, the technical format for the cryptographic proof, and the detailed scope of the section 27(2) audit had not been prescribed in Regulations at the time of writing. Waiting for that detail before building the underlying capability is the wrong sequencing, because the reconciliation infrastructure itself takes time to build properly and cannot be assembled retroactively once assets and liabilities have already diverged.

Practical steps worth prioritising:

- build a real-time or near-real-time internal ledger reconciling customer liabilities against actual held assets, so that whatever interval the Regulations eventually set can be met from data the firm already produces routinely
- select and engage an audit firm early, confirming the firm carries or can obtain approval from the Division concerned, since section 27(2) restricts who may conduct the annual audit
- design the [custody](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-custody-license-safeguarding-customer-assets-25) architecture so that proof-of-reserves data can be generated without exposing individual customer account details, consistent with the data-segregation obligations in section 40
- document the segregation practice required by section 24(1) in a form an external auditor can independently test, not merely in internal policy language
- if reserve assets sit with a third-party custodian, formalise reporting timelines and data-access rights with that custodian now, so the Licensee's own section 27 reconciliation is not held hostage to another firm's reporting cadence

Firms building their compliance calendar as part of [regulatory licensing](https://www.coinconnect.site/regulatory-licensing) preparation should treat section 27 as a continuous operational discipline rather than an annual filing exercise — the annual audit is only as credible as the reconciliation practice running underneath it all year.

## Related reading

- [PVARA Exchange License: Capital, Rules & Obligations 2026](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-exchange-license-requirements-capital-obligations-24)
- [PVARA Transfer & Settlement License: Crypto Payments 2026](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-transfer-settlement-license-payments-remittance-28)
- [PVARA Licensing Process: NOC to Full Licence, Step by Step](https://blog.coinconnect.site/pvara-licensing-process-noc-to-full-licence-step-by-step/)

## About this analysis

This analysis was prepared by the CoinConnect research desk from the Virtual Assets Act, 2026, read as published. Where practice is not yet settled or guidance has not been issued, that is stated in the text above.

Regulatory positions change and specific requirements should be verified against the current position published by the relevant authority before you act on them. This is information and analysis, not legal advice, and it does not create an advisory relationship. Take professional advice on your own circumstances.

## Flags for Malik

- The section on "who receives the proof-of-reserves and audit results" draws a distinction between s.27 (supervisory, to the Authority) and s.42 (public disclosure for Issuers) that I've labelled "our reading" — it's a reasonable structural inference from the text but the Act doesn't say this explicitly, so flag if you'd rather I soften that claim further.
- No Regulations on proof-of-reserves intervals or technical format existed in the source documents, so the "quarterly or monthly by international comparison" comment is explicitly framed as a plausible regulatory choice, not a stated requirement — check that framing reads cautiously enough for you.
