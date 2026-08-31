---
layout: post
title: "Custody Standards and Key Management Under the Act"
date: 2026-01-01 09:00:00 +0500
categories: [Compliance]
author: "Malik Abbas"
description: "Section 26 of the Virtual Assets Act 2026 sets two custody duties for VASPs and leaves technical key-management standards to Regulations. Here is what exists now."
---

[Custody](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-custody-license-safeguarding-customer-assets-25) is the highest-stakes activity a licensed [virtual asset service provider](https://www.coinconnect.site/blog/coinconnect-insights-1/vasp-license-pakistan-3) can undertake, because it is the point where the firm holds something that, if lost or stolen, cannot simply be reissued the way a bank can reissue a debit card. Section 26 of the [Virtual Assets Act](https://blog.coinconnect.site/pakistans-virtual-assets-act-2026-the-complete-guide/), 2026 is short — two sub-sections — but it sets the statutory floor that every custody operation in Pakistan will have to build against.

This article covers exactly what section 26 requires today, what it deliberately leaves to future Regulations, and where a Licensee should focus its custody build in the meantime.

## What does section 26 of the Virtual Assets Act 2026 require?

Section 26 imposes two duties on any Licensee providing [custody](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-custody-license-safeguarding-customer-assets-25) services for Virtual Assets: secure custody and protection against unauthorised access, loss or misuse, and operational resilience through disaster-recovery and business-continuity arrangements. It then commits the Authority to prescribing the detailed technical standards separately.

The operative text of section 26(1) reads:

> A Licensee providing custody services for Virtual Assets shall: (a) ensure the secure custody and protection of Virtual Assets against unauthorized access, loss, or misuse; and (b) maintain operational resilience, including robust disaster-recovery and business-continuity arrangements.

Section 26(2) then states:

> The Authority shall prescribe detailed technical standards, operational requirements, and audit procedures to ensure that Licensees meet the obligations under this clause, including but not limited to, standards for key management, custody mechanisms, and verification or assurance processes.

Read together, the structure is deliberate: section 26(1) fixes the outcome a custodian must achieve, and section 26(2) commits the Authority to prescribing how that outcome must be demonstrated, through Regulations that had not been published at the time of writing. A Licensee is bound by the section 26(1) duty now; the section 26(2) technical detail — key-management standards, custody mechanisms, and verification or assurance processes — is still to come.

## Who does section 26 apply to?

Section 26 applies specifically to "a Licensee providing custody services for Virtual Assets" — it is scoped to the custody activity, not to every Licensee under the Act generally. [Schedule I](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-license-categories-explained-23), referenced in section 18, defines Custody and Administration Services at category 3 as the safekeeping or administration, on behalf of customers and pursuant to their instructions, of Virtual Assets or of private cryptographic keys or other means of access that let a customer transfer or dispose of their assets independently.

Schedule I's category 3 description carries one important carve-out: it "excludes the mere provision of software, hardware or infrastructure that enables a customer to retain exclusive control over their own private keys." A firm that sells a self-custody wallet application, without itself ever holding or having access to customer keys, falls outside the definition of Custody and Administration Services and, on the text, outside the licensing requirement for that category — because the customer, not the firm, retains control. Where a firm's product design sits close to that line, the classification question should be resolved before assuming section 26 does or does not apply, since section 9(1)(f) gives the Authority the power to classify any service based on its substantive features rather than its label.

It is also worth noting that custody obligations are not confined to firms licensed solely for category 3. A [broker-dealer](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-broker-dealer-license-what-it-covers-27) or exchange that holds [customer assets](https://www.coinconnect.site/blog/3/customer-assets-definition-pvara-pakistan-62) pending settlement, or an investment manager exercising discretion under category 7, is, in substance, also providing custody over those assets for the period it holds them — and section 26 is drafted around the activity of custody, not around a single licence category label.

## What does "secure custody and protection" mean in practice?

Section 26(1)(a) states the outcome — protection against unauthorised access, loss, or misuse — without prescribing the specific technical means. In practice, this is the category of control most closely associated with private key security: how keys are generated, stored, backed up, and authorised for use in a transaction.

Common industry approaches that sit within the scope of what section 26(1)(a) is aimed at include multi-signature wallet architectures, where more than one independent key holder must approve a transaction before it executes; hardware security modules and cold storage, which keep private keys offline and away from internet-connected systems; and multi-party computation, where a key is never assembled in one place at all but is instead split across parties who jointly compute a signature. None of these specific technologies are named or mandated in the Act itself — the choice of mechanism is left open, provided the outcome in section 26(1)(a) is achieved and can be evidenced to the Authority.

"Misuse" in section 26(1)(a) is a distinct risk from "unauthorised access" and "loss". Unauthorised access covers an external attacker or an internal actor accessing keys without permission. Loss covers keys or assets becoming irretrievable, whether through technical failure, a lost seed phrase, or a similar accident. Misuse covers a scenario where access was authorised in a technical sense but the assets were used for a purpose outside what the customer permitted — which connects section 26 directly back to the rehypothecation prohibition in section 24(4) and the fiduciary duty in section 24(3): a custodian that has secure key management but then uses customer assets in a way the customer never consented to has satisfied section 26(1)(a) on access controls while still breaching section 24.

## What counts as "operational resilience" under section 26(1)(b)?

Section 26(1)(b) requires "robust disaster-recovery and business-continuity arrangements" — the ability of a custody operation to keep functioning, or to recover functioning quickly, after a disruptive event. This sits alongside, but is distinct from, the general [cybersecurity](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-custody-license-safeguarding-customer-assets-25) and operational-resilience obligations that section 34 imposes on all Licensees, not just custodians.

Disaster-recovery, in this context, typically covers the ability to restore custody operations — including, critically, the ability to access and move customer assets — after an event such as infrastructure failure, a natural disaster affecting a firm's primary site, or a catastrophic loss of a subset of key material. Business-continuity is the broader discipline of keeping the firm's operations running, or resuming them within an acceptable timeframe, across a wider range of disruptive scenarios. For a custodian, the two overlap heavily on one central point: a business-continuity plan that cannot demonstrate how customer assets remain accessible and recoverable is not meeting the standard section 26(1)(b) sets, however strong its general IT continuity planning is on paper.

## What has PVARA committed to prescribing under section 26(2)?

Section 26(2) names three categories of technical standard the Authority is to prescribe: standards for key management, custody mechanisms, and verification or assurance processes — described as a non-exhaustive list ("including but not limited to"), so the eventual Regulations could extend further. None of these had been published at the time of writing, meaning the specific technical bar — for example, minimum thresholds for multi-signature or MPC schemes, cold-versus-hot storage ratios, or mandatory third-party attestation formats — is not yet fixed in public law.

"Verification or assurance processes" is the phrase most directly connected to proof-of-reserves and audit. Section 27(1) separately requires a Licensee to furnish cryptographic proof-of-reserves, reconciled against customer liabilities, at prescribed intervals, and section 27(2) requires an annual audit by a firm of Chartered Accountants that verifies segregation of Customer Assets under section 24. Our reading is that the "verification or assurance processes" contemplated by section 26(2) will likely connect to, or overlap with, that section 27 audit and reporting cycle, rather than sit as an entirely separate technical certification regime — though the Act does not state this explicitly, and a Licensee should not assume the two will be merged until Regulations confirm it.

## How does custody under section 26 relate to segregation under section 24?

The two sections work at different layers of the same problem. Section 24(1) requires Customer Assets to be held in segregated accounts, separate from a Licensee's own assets — a legal and accounting requirement about whose assets are whose. Section 26 requires that, however those assets are held, they are held securely and resiliently — an operational and technical requirement about how the holding itself is protected. A custodian could, in theory, satisfy section 24's segregation on the ledger while still failing section 26 if its key-management controls are weak enough that the segregated assets remain vulnerable to theft or loss. Both duties have to be met independently; neither substitutes for the other.

## What should a custody operation build now, ahead of the technical standards?

Given that the detailed key-management and audit standards under section 26(2) are still to be prescribed, the more defensible approach is to build custody infrastructure against recognised international practice now, so the firm is not retrofitting its architecture once Regulations land.

Areas worth prioritising:

- key-generation and storage architecture that does not rely on any single point of failure, whether a single person, a single device, or a single location
- a documented, tested disaster-recovery plan specific to key recovery, not just general IT system recovery, with recovery time objectives the firm can evidence to the Authority
- clear internal segregation of duties between whoever can initiate a transaction and whoever can authorise it, reducing the risk that "misuse" under section 26(1)(a) becomes possible from a single insider
- a reconciliation process capable of supporting the section 27(1) proof-of-reserves obligation on an ongoing basis, not built as an annual scramble ahead of the section 27(2) audit
- engagement early with an audit firm experienced in [virtual asset](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-license-pakistan-complete-guide-22) custody, since section 27(2) requires the annual audit to be conducted by a firm of Chartered Accountants approved by the Division concerned

Firms weighing whether to build custody in-house or rely on a third-party custodian as part of their [regulatory licensing](https://www.coinconnect.site/regulatory-licensing) strategy should treat section 26 as the baseline either party must meet — outsourcing custody does not outsource the Licensee's own responsibility under the Act for how its customers' assets are protected.

## About this analysis

This analysis was prepared by the CoinConnect research desk from the Virtual Assets Act, 2026, read as published. Where practice is not yet settled or guidance has not been issued, that is stated in the text above.

Regulatory positions change and specific requirements should be verified against the current position published by the relevant authority before you act on them. This is information and analysis, not legal advice, and it does not create an advisory relationship. Take professional advice on your own circumstances.

## Flags for Malik

- No custody-specific Regulations were in the source documents, so the whole "what should a custody operation build now" section is best-practice guidance derived from the statutory outcome (s.26(1)) rather than a cited technical standard. I've kept the specific technologies (multi-sig, HSM, MPC) framed as "common industry approaches", explicitly not mandated by the Act, to avoid implying they're a legal requirement.
- The link connecting s.26(2)'s "verification or assurance processes" to the s.27 proof-of-reserves audit is my own inference, flagged in the text as "our reading" — the Act doesn't explicitly tie the two sections together.
