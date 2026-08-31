---
layout: post
title: "Segregation of Customer Assets: The Core Rule Under the Act"
date: 2026-01-01 09:00:00 +0500
categories: [Compliance]
author: "Malik Abbas"
description: "Section 24(1) of the Virtual Assets Act requires VASPs to hold customer virtual assets and fiat in accounts separate from the firm's own — what the duty covers."
---

Commingling customer funds with company funds is the single most common way a financial firm fails its customers when things go wrong. Pakistan's [Virtual Assets Act](https://blog.coinconnect.site/pakistans-virtual-assets-act-2026-the-complete-guide/), 2026 addresses this directly, with a standalone chapter built specifically around how [customer assets](https://www.coinconnect.site/blog/3/customer-assets-definition-pvara-pakistan-62) are held.

This analysis reads section 24 and section 3(1)(vii) of the Virtual Assets Act, 2026 as passed by the National Assembly, and sets out what the segregation duty requires and what falls inside the term "Customer Assets" it protects.

## What does section 24(1) actually require a VASP to do?

Section 24(1) requires every Licensee to hold customer assets in accounts kept separate from its own, at all times, without exception. The Act states:

> "A Licensee shall, at all times, hold Customer Assets in segregated accounts separate from its own assets, in the manner prescribed by Regulations."

Three things follow from that wording. First, "at all times" is a continuous duty, not a point-in-time check performed once at onboarding or once a year at audit — a firm that segregates assets correctly for eleven months and commingles them in the twelfth has not met the standard. Second, the duty is to hold assets in "segregated accounts," meaning the separation has to be structural — a distinct account or wallet — rather than achieved through internal bookkeeping alone that tracks ownership on paper while the underlying assets sit in one pool. Third, the phrase "in the manner prescribed by Regulations" signals that the Act sets the principle while [PVARA](https://www.coinconnect.site/pvara-guide) is expected to issue detailed technical Regulations on how segregation must be implemented in practice; those detailed Regulations are not among the three source documents reviewed for this analysis, so the operational mechanics beyond the principle itself are not stated here.

## What counts as a "Customer Asset" under the Act?

Section 3(1)(vii) defines the term precisely, and the definition is narrower than it might first appear. The Act states:

> "'Customer Assets' means Virtual Assets and fiat currency belonging to a customer that a Virtual Asset Service Provider holds, safeguards, or otherwise has custody or control over on that customer's behalf, and excludes assets owned by the Virtual Asset Service Provider."

Two elements of that definition matter for scoping the segregation duty correctly:

- **Both asset types are covered.** The definition names Virtual Assets and fiat currency together — a VASP holding customer PKR balances alongside customer crypto balances owes the segregation duty to both, not only to the on-chain assets.
- **The exclusion is explicit and deliberate.** The definition specifically excludes "assets owned by the [Virtual Asset Service Provider](https://www.coinconnect.site/blog/coinconnect-insights-1/vasp-license-pakistan-3)" — meaning the firm's own trading inventory, its own treasury holdings, and its own working capital sit outside the definition entirely and are not subject to the segregation duty in the same way, because they were never customer assets in the first place. The line the Act draws is about whose asset it is (the customer's) and why the firm holds it (safekeeping on the customer's behalf) — not merely where the asset physically or cryptographically sits.

The [custody](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-custody-license-safeguarding-customer-assets-25) obligation and the segregation obligation are related but distinct: a firm can hold an asset in [custody](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-custody-license-safeguarding-customer-assets-25) without segregating it correctly, which is precisely the failure mode section 24(1) is written to prevent.

## What else does the Act require of a Licensee handling Customer Assets, beyond segregation?

Section 24 does not stop at the segregation duty in subsection (1). The remaining subsections build a fuller picture of how a Licensee must treat customer assets day to day.

| Section 24 subsection | What it requires |
|---|---|
| 24(1) | Hold Customer Assets in segregated accounts, separate from the Licensee's own assets, at all times |
| 24(2) | Customer Assets do not form part of the Licensee's estate on insolvency or liquidation |
| 24(3) | The Licensee owes customers a fiduciary duty and must act honestly, fairly, and in customers' best interests when dealing with their assets |
| 24(4) | No rehypothecation, lending, pledging or encumbrance of Customer Assets without the customer's explicit, informed, and revocable written consent |

Subsection (3) is worth reading alongside subsection (1) because it sets the standard of conduct that governs how the segregated assets are treated, not only where they sit. A Licensee could technically hold customer assets in a correctly segregated account and still breach the Act by dealing with those assets in a way that is not honest, fair, or in the customer's best interests. Subsection (4) closes a specific gap that segregation alone does not: even a properly segregated customer account could, in principle, be pledged or lent out by the firm holding it — subsection (4) makes that unlawful without the customer's explicit, informed, and revocable written consent.

## How does this connect to the audit and proof-of-reserves duties elsewhere in the Act?

Section 27(2) requires a Licensee's annual audit, conducted by a firm of Chartered Accountants approved by the Division concerned, to "include a verification of the segregation of Customer Assets as required under section 24." This means segregation is not simply a standing obligation the Licensee self-certifies — it is independently tested at least once a year by an external auditor whose findings feed back to PVARA. Section 27(1) separately requires a Licensee to furnish PVARA with cryptographic proof-of-reserves "reconciled against its liabilities to customers," at intervals to be prescribed by Regulations, which gives PVARA an ongoing supervisory tool alongside the annual audit rather than relying on the audit alone.

## What happens to Customer Assets if a VASP becomes insolvent?

This question sits in section 24(2), which is addressed separately at length elsewhere, but it is worth stating plainly here because it is the practical reason segregation matters in the first place. Correct segregation under 24(1) is what makes the insolvency ring-fence in 24(2) actually work — a Licensee cannot claim its customer assets sit outside the insolvency estate under 24(2) if it never actually held those assets in genuinely separate accounts under 24(1). The two subsections function as cause and effect: segregation is the operational mechanism, and the insolvency protection is the legal consequence that only holds if the mechanism was real.

Two practical points follow for firms building out this control:

- "Segregated accounts" under section 24(1) means structural separation, not bookkeeping separation — a shared wallet with internal ledger entries tracking customer ownership is a materially weaker position than genuinely distinct accounts.
- Fiat currency is caught by the same duty as Virtual Assets under section 3(1)(vii) — a firm cannot treat its PKR customer balances as a lower-priority segregation task than its crypto holdings.

## Related reading

- [PVARA Exchange License: Capital, Rules & Obligations 2026](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-exchange-license-requirements-capital-obligations-24)
- [PVARA Transfer & Settlement License: Crypto Payments 2026](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-transfer-settlement-license-payments-remittance-28)
- [PVARA Licensing Process: NOC to Full Licence, Step by Step](https://blog.coinconnect.site/pvara-licensing-process-noc-to-full-licence-step-by-step/)
- [The PVARA Licensing Gold Rush: Pakistan's Crypto Frontier](https://www.coinconnect.site/blog/3/blogpvara-licensing-gold-rush-pakistan-crypto-frontier-56)

## About this analysis

This analysis was prepared by the CoinConnect research desk from sections 3(1)(vii), 24 and 27 of the Virtual Assets Act, 2026 as passed by the National Assembly, read as published. The detailed Regulations PVARA is expected to issue under section 24(1) prescribing "the manner" of segregation are not among the three source documents reviewed, so the operational mechanics beyond the statutory principle are not stated here. Where practice is not yet settled or guidance has not been issued, that is stated in the text above.

Regulatory positions change and specific requirements should be verified against the current position published by the relevant authority before you act on them. This is information and analysis, not legal advice, and it does not create an advisory relationship. Take professional advice on your own circumstances.

## Flags for Malik

1. Section 24(1) explicitly defers the operational detail of segregation to future Regulations — I did not speculate about what those Regulations will require (dedicated wallets, omnibus vs individual customer accounts, on-chain vs off-chain segregation) since none of that is in our three source documents.
2. This article and 086 (insolvency ring-fence) are a deliberate pair — I've kept this one focused on the segregation mechanism itself and left the insolvency consequence for the companion piece, with a forward pointer in the closing section rather than duplicating the 24(2) analysis here.
3. No penalty specific to a section 24 breach is named in the Act beyond the general administrative sanctions in section 59 — I did not state a specific fine figure tied to segregation failures since the Act doesn't isolate one.
