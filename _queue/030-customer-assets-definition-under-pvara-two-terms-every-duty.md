---
layout: post
title: "Customer Assets Definition Under PVARA — Two Terms, Every Duty"
date: 2026-01-01 09:00:00 +0500
categories: [Compliance]
author: "Malik Abbas"
description: "How Pakistan's Virtual Assets Act 2026 defines customer and Customer Assets, and why those two terms drive segregation, custody, audit and insolvency duties."
---

Most of the operational burden in Pakistan's virtual asset framework does not come from a long compliance chapter. It comes from two short definitions in section 3(1) of the Virtual Assets Act, 2026 — "Customer" at sub-clause (vi) and "Customer Assets" at sub-clause (vii).

Get them right and the rest of the framework reads as a coherent set of duties. Get them wrong and you will under-scope your licence application, mis-design your wallet architecture, and discover in year two that a balance you treated as your own treasury is legally somebody else's property.

This analysis takes both definitions apart, then traces every downstream obligation they trigger — segregation, fiduciary duty, rehypothecation consent, proof-of-reserves, audit and insolvency ring-fencing.

## What is the definition of Customer Assets under Pakistan's Virtual Assets Act 2026?

Section 3(1)(vii) of the Virtual Assets Act, 2026 defines Customer Assets as virtual assets **and fiat currency** belonging to a customer that a Virtual Asset Service Provider holds, safeguards, or otherwise has custody or control over on that customer's behalf, excluding assets owned by the provider itself. The operative test is control, not title.

The statutory language is:

> "Customer Assets" means Virtual Assets and fiat currency belonging to a customer that a Virtual Asset Service Provider holds, safeguards, or otherwise has custody or control over on that customer's behalf, and excludes assets owned by the Virtual Asset Service Provider;

Four things follow directly from that wording.

**Fiat is inside the definition.** Rupee balances sitting in your on-ramp account against a customer ledger entry are Customer Assets in exactly the same way a customer's BTC balance is. Firms that build a careful segregation model for tokens and a casual one for fiat have solved half the problem. This is one reason the [banking side of the build](https://www.coinconnect.site/tax-banking) cannot be treated as an afterthought.

**"Or otherwise has custody or control over" is the widest limb.** Holding is obvious. Safeguarding is obvious. Control is where architecture decisions become legal ones — a co-signing key in a 2-of-3 multisig, an admin key on a smart contract, an ability to pause withdrawals or move balances unilaterally. In practice, our reading is that if your firm can move an asset without the customer's contemporaneous authorisation, you should assume you control it.

**Beneficial ownership stays with the customer.** The words are "belonging to a customer". The Act does not treat a deposit as a loan to the platform.

**Your own book is excluded.** Proprietary inventory, treasury and corporate fiat are not Customer Assets. That exclusion matters for capital planning, and it interacts with the [minimum financial resource requirements](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-capital-requirements-pakistan-18) under section 25, which are about your own resources, not customer property.

## Who counts as a "customer" under section 3(1)(vi)?

Section 3(1)(vi) defines a Customer as any natural or legal person who obtains or uses a Virtual Asset Service from a Licensee, or who enters into a business or contractual relationship with a Licensee for the provision of such service, "whether on a one-off or ongoing basis". There is no retail-only limit and no minimum relationship duration.

Three features of that definition are commercially significant:

- **Legal persons are customers.** Institutional counterparties, corporate treasuries and funds are customers, with the same asset-protection consequences as an individual. There is no professional-client carve-out in the definition itself.
- **One-off users are customers.** A single walk-up OTC trade creates a customer. You cannot escape the category by declining to open an account.
- **"Obtains or uses" is behavioural.** A person who uses the service is a customer even where the contractual paperwork points elsewhere.

There is a drafting asymmetry worth noting. Section 3(1)(vi) anchors "Customer" to a **Licensee**, while section 3(1)(vii) anchors "Customer Assets" to a **Virtual Asset Service Provider** — and section 3(1)(xxxiii) defines the latter as any person who, as a business, provides virtual asset services to third parties on a professional basis, licensed or not. Our reading is that the asset-protection concept is deliberately wider than the licensed perimeter, which is consistent with the prohibition on unlicensed services in section 50 and the criminal penalty in section 54(1). But the Act does not spell this out, and PVARA has not published guidance resolving it.

## Why do these definitions decide whether you need a licence at all?

Because three separate parts of the Act use Customer Assets as the switch that turns an unregulated activity into a licensable one. Whether you hold or control customer property determines your licence category — and sometimes whether you need a licence in the first place.

| Activity | Position without Customer Assets | Position with Customer Assets |
|---|---|---|
| Proprietary dealing | Schedule I, item 2 exempts a person dealing "solely on its own account" that does not execute customer orders and does not hold or control Customer Assets from broker-dealer services | Falls inside broker-dealer services; item 2(d) expressly covers "market-making using Customer Assets" |
| Wallet software | Schedule I, item 3 excludes "the mere provision of software, hardware or infrastructure that enables a customer to retain exclusive control over their own private keys" | Custody and Administration Services — safekeeping of assets or of the private keys allowing disposal |
| Mining | Section 37(2): "Pure mining, by itself, does not constitute a Virtual Asset Service requiring license" | Section 37(2): "Mining operations involving customer assets or funds… shall be treated as Virtual Asset Services and require licensing" |

That table is the single most useful diagnostic in the Act. Firms mapping their business onto the [ten Schedule I service categories](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-license-categories-explained-23) should run each product line through it before deciding what to apply for. The non-custodial exclusion in item 3 is narrow: it turns on the customer retaining **exclusive** control of their own keys. A "non-custodial" product where the operator holds a recovery share is unlikely to qualify. We work through the boundary in more detail in our notes on the [custody licence](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-custody-license-safeguarding-customer-assets-25), the [broker-dealer licence](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-broker-dealer-license-what-it-covers-27) and [mining under PVARA](https://www.coinconnect.site/blog/3/pakistan-pvara-virtual-asset-mining-licensing-63).

## What does section 24 require once assets are Customer Assets?

Section 24 imposes four obligations: continuous segregation from the licensee's own assets, exclusion of Customer Assets from the licensee's insolvency estate, a fiduciary duty to customers, and a prohibition on rehypothecation, lending, pledging or encumbrance without the customer's explicit, informed and revocable written consent.

Taken in order:

**Segregation (section 24(1)).** A licensee "shall, at all times, hold Customer Assets in segregated accounts separate from its own assets, in the manner prescribed by Regulations." The manner is left to regulations; the duty is not. "At all times" leaves no room for intra-day commingling.

**Insolvency ring-fencing (section 24(2)).**

> Notwithstanding anything to the contrary contained in any other law for the time being in force, Customer Assets held by a Licensee shall not form part of the Licensee's estate in the event of its insolvency or liquidation.

That is a statutory override, and it is the reason the definition matters so much. Everything captured by section 3(1)(vii) sits outside the estate. Anything falling outside it — most obviously, a balance the customer has been persuaded to lend to the platform — does not.

**Fiduciary duty (section 24(3)).** The licensee "owes a fiduciary duty to its customers and shall at all times act honestly, fairly, and in the best interests of its customers when dealing with Customer Assets." This sits alongside the general duty of integrity and fair dealing in section 41 and the conflict-of-interest duty in section 44, which prohibits placing the firm's own interests above those of its customers.

**No rehypothecation without consent (section 24(4)).** The licensee shall not rehypothecate, lend, pledge or otherwise encumber Customer Assets, whether virtual assets or fiat balances, "without the customer's explicit, informed, and revocable written consent." Three adjectives, each doing work: buried terms of service are not explicit, an undisclosed yield programme is not informed, and consent that cannot be withdrawn is not revocable. Any lending or borrowing product needs to be built around this from day one.

## How must Customer Assets be proved, audited and protected?

Through cryptographic proof-of-reserves under section 27(1), an annual audit that expressly verifies segregation under section 27(2), custody and key-management standards under section 26, and a possible customer compensation mechanism under section 29.

- **Proof-of-reserves.** Section 27(1) requires a licensee to furnish PVARA, at prescribed intervals, with "cryptographic proof-of-reserves reconciled against its liabilities to customers." Reconciliation against liabilities, not merely a wallet-balance attestation.
- **Audit.** Section 27(2) requires annual audit by a firm of Chartered Accountants approved by the Division concerned, and states that "such audit shall include a verification of the segregation of Customer Assets as required under section 24."
- **Custody standards.** Section 26 requires secure custody against unauthorised access, loss or misuse, plus operational resilience including disaster-recovery and business-continuity arrangements, with technical standards for key management to be prescribed.
- **Compensation.** Section 29 allows PVARA to establish a customer compensation or safeguard mechanism for losses arising from custodial failure, in a manner to be prescribed. It is permissive, not mandatory, and no scheme has been published.
- **Data.** Section 40(2) designates customer identification and due-diligence records, transaction-level data capable of identifying a customer, and private keys and wallet authentication data as sensitive information requiring logical and technical segregation and need-to-know access.
- **Emergency powers.** Section 60 permits PVARA to freeze related assets for up to thirty days on a systemic threat, manipulation, fraud or cybersecurity breach.

Firms should also note section 23(2): where a licence is revoked, the licensee must immediately cease providing services — which makes a pre-agreed customer asset return plan an operational necessity, not a nicety. Our [PVARA licensing guide](https://www.coinconnect.site/pvara-guide) and the [full VASP licence walkthrough](https://www.coinconnect.site/blog/coinconnect-insights-1/vasp-license-pakistan-3) set the sequencing out.

## Where do these definitions bite before you hold a full licence?

At both pre-licence gateways. The PVARA No Objection Certificate Regulations 2025 treat Custody Services as an AML-Registered Service and require customer due diligence to be completed before any such service is provided. The Sandbox Guidelines 2026 require segregation policies as an eligibility condition.

Under regulation 9.3 of the No Objection Certificate Regulations 2025, "CDD must be completed before the Applicant provides any AML Registered Service" — and regulation 2.3 lists Custody Services, Exchange Services, Broker-Dealer Services and Virtual Asset Derivative Services as those services. Regulation 13.1 sets a seven-year minimum retention period for AML/CFT records, and Form A1 requires disclosure of "use of custodians, banks and payment processors (onshore and offshore)". Registration on the FMU goAML platform follows issuance of the NOC; we cover that sequence in our note on [goAML registration for VASPs](https://www.coinconnect.site/blog/coinconnect-insights-1/fmu-goaml-vasp-pakistan-17).

On the sandbox side, the eligibility criteria in the PVARA Sandbox Guidelines 2026 require applicants to demonstrate "policies and procedures for handling/segregation client money and virtual assets" and "liability management policies and framework to safeguard clients from fraud", alongside safeguarding of consumer assets. The Annexure B undertaking goes further, requiring participants to obtain insurance coverage indemnifying clients against losses from fraud or gross negligence, and to notify PVARA of any material incident within one hour with a detailed report within 48 hours. The [Form I walkthrough](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-sandbox-form-i-complete-walkthrough-2026-8) covers the submission itself.

Two drafting points for readers to hold in mind. The No Objection Certificate Regulations and the Sandbox Guidelines are both drafted against the Virtual Assets Ordinance, 2025; section 74 of the Act saves anything done under the lapsed Ordinance. And section 70 transitional provisions require existing providers to apply within six months, with continued operation conditional on adherence to "core obligations of this Act, particularly regarding customer asset protection".

## What should a firm do with these two definitions before filing?

Treat them as a scoping exercise, not a policy drafting exercise. Work product by product:

1. **Map control.** For every wallet, every key, every fiat account, record who can move value and on whose authorisation. That register determines what is Customer Assets.
2. **Test each product against the three carve-outs.** Proprietary-only dealing, exclusive-key software, and pure mining are the only routes in the Act that avoid the consequence.
3. **Design segregation for fiat and tokens together.** Both are inside section 3(1)(vii).
4. **Rebuild consent flows** for any lending, staking or yield feature to meet the explicit, informed and revocable written consent standard in section 24(4).
5. **Build the reconciliation** that section 27(1) will ask you to produce, and appoint auditors who can attest to segregation under section 27(2).
6. **Align entity structure** so that segregation is capable of being evidenced by a Pakistan-incorporated entity — the [corporate setup](https://www.coinconnect.site/corporate-setup) and [regulatory licensing](https://www.coinconnect.site/regulatory-licensing) workstreams need to run in parallel, and controller disclosure obligations follow from the [Controller definition](https://www.coinconnect.site/blog/3/pakistan-pvara-controller-virtual-assets-act-2026-58) in section 3(1)(v).

Firms issuing tokens should note that reserve assets are governed by a separate concept — the "Segregated Reserve" defined at section 3(1)(xxvi), which underpins the [stablecoin reserve regime](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-frt-stablecoin-issuance-32). Reserve backing and Customer Assets segregation are two distinct duties and should not be run off the same account.

## About this analysis

This analysis was prepared by the CoinConnect research desk from the Virtual Assets Act, 2026 as passed by the National Assembly (including Schedule I), the PVARA No Objection Certificate Regulations 2025, and the PVARA Sandbox Guidelines 2026, each read as published. Where practice is not yet settled or guidance has not been issued — in particular the regulations prescribing the manner of segregation under section 24(1), the intervals for proof-of-reserves under section 27(1), and any compensation scheme under section 29 — that is stated above.

Regulatory positions change and specific requirements should be verified against
