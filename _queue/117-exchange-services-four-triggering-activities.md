---
layout: post
title: "Exchange Services: The Four Activities That Trigger a Licence"
date: 2026-01-01 09:00:00 +0500
categories: [Licensing]
author: "Malik Abbas"
description: "Schedule I item 4 lists four activities that make a platform an Exchange Service in Pakistan — fiat pairs, crypto pairs, order matching and order books."
---

"Exchange" sounds like it should mean one thing — a platform where people trade crypto. Under Pakistan's [Virtual Assets Act](https://blog.coinconnect.site/pakistans-virtual-assets-act-2026-the-complete-guide/), 2026, the term is defined more precisely, as four separate activities that each independently trigger the licence. A platform can qualify as an Exchange Service through any one of the four, without doing all of them, and that structure matters for how a business assesses whether it needs authorisation.

This article sets out the four activities under [Schedule I](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-license-categories-explained-23) item 4, why they are drafted separately rather than as a single combined test, and how the category sits alongside the Act's other trading-related licences.

## What are Exchange Services under Schedule I item 4?

Schedule I item 4 defines Exchange Services as any of four listed activities. The Act states the category "means any of the following":

> "(a) exchanging Virtual Assets for fiat currency; (b) exchanging one or more types of Virtual Assets; (c) matching orders between buyers and sellers and executing conversions as described in (a) and (b); or (d) maintaining an order book for the above purposes."

Because the definition is structured as "any of the following" joined by "or," a platform needs to satisfy only one of the four limbs to fall within the category — it does not need to run a full order book, offer fiat pairs, and match orders all at once. A pure crypto-to-crypto conversion service that never touches fiat currency and never maintains an order book can still be an Exchange Service through limb (b) alone.

## What is the difference between limb (a) and limb (b)?

Limb (a) covers exchanging Virtual Assets for fiat currency — the on-ramp and off-ramp activity that converts a [Virtual Asset](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-license-pakistan-complete-guide-22) into Pakistani Rupees or another official currency, or back again. Limb (b) covers exchanging one or more types of Virtual Assets — conversion between two Virtual Assets, with no fiat currency involved at any point in the transaction.

The two limbs are drafted separately because a platform can offer one without the other. A crypto-to-crypto swap service that never handles fiat currency is still caught by limb (b), even though it never engages in the fiat-conversion activity limb (a) describes. Conversely, a service that only converts Virtual Assets to and from fiat, without ever facilitating a crypto-to-crypto trade, is caught by limb (a) alone.

## What does "matching orders" under limb (c) add that limbs (a) and (b) do not already cover?

Limb (c) covers "matching orders between buyers and sellers and executing conversions as described in (a) and (b)" — this is the activity of bringing two counterparties together and completing the transaction between them, as distinct from simply being one side of a conversion. A platform that operates as principal — buying and selling directly against its own inventory rather than matching two customers against each other — can fall within limbs (a) and (b) without engaging in the order-matching activity of limb (c) at all.

Limb (c) is the provision that captures peer-to-peer matching platforms and marketplace-style exchanges specifically, where the platform's core function is connecting a buyer's order with a seller's order and executing the resulting conversion between them, rather than trading against its own balance sheet.

## What does maintaining an order book under limb (d) actually mean?

Limb (d) covers "maintaining an order book for the above purposes" — operating the running record of buy and sell orders that a matching engine draws on to execute limbs (a), (b) and (c). An order book is the infrastructure layer beneath order matching: it is the list of outstanding, unexecuted orders at various prices that the platform holds and updates as new orders arrive and existing ones are filled or cancelled.

Because limb (d) is drafted as its own separate trigger, a technology provider that builds and operates order-book infrastructure for a Virtual Asset trading venue — even one that does not itself execute trades or hold customer funds — falls within Exchange Services on the plain wording, if that order book exists "for the above purposes" of exchanging assets under limbs (a) through (c). This is a broader reach than a narrower definition limited only to the party actually executing trades would produce.

## How does Exchange Services relate to Broker-Dealer Services under item 2?

The two categories overlap in practice but are drafted as separate licence types under Schedule I, and a single platform can require authorisation for both. [Broker-Dealer](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-broker-dealer-license-what-it-covers-27) Services under item 2 covers activities including arranging or facilitating orders between two parties, soliciting or accepting orders and consideration, trading on the provider's own account, market-making using [Customer Assets](https://www.coinconnect.site/blog/3/customer-assets-definition-pvara-pakistan-62), and placement or distribution services for Issuers. Exchange Services under item 4 covers the specific activities of fiat conversion, crypto-to-crypto conversion, order matching and order-book maintenance.

A platform that both matches customer orders (an Exchange Services activity under limb (c)) and also trades on its own account against those same customers (a Broker-Dealer Services activity under item 2, limb (c)) is likely to need authorisation under both categories, since nothing in either definition treats the two as mutually exclusive. Businesses building a combined trading venue should map their activity against both Schedule I entries separately rather than assuming a single "exchange" licence covers every function the platform performs.

## Is Exchange Services one of PVARA's phased AML-Registered Services?

Yes. Regulation 2.3 of [PVARA](https://www.coinconnect.site/pvara-guide)'s [No Objection Certificate](https://www.coinconnect.site/regulatory-licensing) Regulations 2025 designates Exchange Services as one of four "[AML](https://www.coinconnect.site/blog/3/fit-and-proper-aml-pvara-mistakes-54) Registered Services," alongside Broker-Dealer, [Custody](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-custody-license-safeguarding-customer-assets-25) and Virtual Asset [Derivatives](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-derivatives-leverage-license-31) Services. A firm that receives a [No Objection Certificate](https://blog.coinconnect.site/the-pvara-no-objection-certificate-a-complete-guide/) ("NOC") and completes registration on the [goAML](https://www.coinconnect.site/blog/coinconnect-insights-1/fmu-goaml-vasp-pakistan-17) portal may begin providing Exchange Services before a full licence is granted under section 21 of the Act, subject to any conditions PVARA imposes.

Regulation 18.1(f) still requires the registered applicant to "apply for and progress diligently toward a full VASP License within the time period required by the Authority," and Regulation 19.1(e) allows PVARA to revoke the NOC where an applicant fails to progress toward that full licence within the prescribed period — the phased pathway is a bridge to full licensing, not an alternative to it.

## What should a platform assessing whether it needs an Exchange Services licence check first?

- **Test all four limbs independently**, since satisfying only one — for example, running crypto-to-crypto conversion under limb (b) with no fiat exposure and no order book — is enough to trigger the category on its own.
- **Distinguish acting as principal from order matching.** A platform trading directly against its own inventory may sit under limbs (a) and (b) without limb (c)'s order-matching activity, while a peer-to-peer marketplace sits more clearly under limb (c).
- **Check whether order-book infrastructure alone brings a technology provider into scope** under limb (d), even where that provider does not itself execute trades or custody assets.
- **Map activity against Schedule I item 2 as well as item 4** where the platform also trades on its own account or arranges orders in ways that could separately qualify as Broker-Dealer Services.

## About this analysis

This analysis was prepared by the CoinConnect research desk from the Virtual Assets Act, 2026 — Schedule I items 2 and 4, and section 21 — read alongside PVARA's No Objection Certificate Regulations 2025, Regulation 2.3 and Regulation 18.1. Where practice is not yet settled or guidance has not been issued, that is stated in the text above.

Regulatory positions change and specific requirements should be verified against the current position published by the relevant authority before you act on them. This is information and analysis, not legal advice, and it does not create an advisory relationship. Take professional advice on your own circumstances.

## Flags for Malik

1. The reading that limb (d), order-book maintenance, could independently capture a pure infrastructure provider that never executes trades is a structural inference from the "any of the following" drafting, not a statement the Act makes explicitly about third-party technology vendors — flagged in the body as a plain-wording reading rather than settled guidance.
2. The overlap analysis between Exchange Services and Broker-Dealer Services (item 2) is my own structural comparison of the two Schedule I entries side by side. The Act does not state directly that a platform may need both licences simultaneously, though nothing in either definition excludes that outcome.
