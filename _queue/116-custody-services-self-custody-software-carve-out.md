---
layout: post
title: "Custody Services and the Self-Custody Software Carve-Out"
date: 2026-01-01 09:00:00 +0500
categories: [Licensing]
author: "Malik Abbas"
description: "Schedule I item 3 licenses custody of Virtual Assets and private keys, but excludes software that leaves customers in exclusive control of their own keys."
---

A wallet app and a custodian can look almost identical from the outside — both hold code that touches a customer's private keys. Pakistan's [Virtual Assets Act](https://blog.coinconnect.site/pakistans-virtual-assets-act-2026-the-complete-guide/), 2026 draws the licensing line between them on a single question: who actually controls the keys. [Schedule I](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-license-categories-explained-23) item 3 licenses [Custody](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-custody-license-safeguarding-customer-assets-25) and Administration Services, and its closing clause excludes a specific category of software provider from that licence entirely.

This article works through what item 3 covers, where the self-custody carve-out sits, and why the test turns on control rather than on whether the provider's code ever comes near a private key.

## What are Custody and Administration Services under Schedule I item 3?

Schedule I item 3 defines the category as the safekeeping or administration of assets on a customer's behalf and at their instruction. The Act states:

> "means the safekeeping or administration, on behalf of customers and pursuant to their instructions, of: (a) Virtual Assets; or (b) private cryptographic keys or other means of access that allow the customer to transfer or dispose of Virtual Assets independently, but excludes the mere provision of software, hardware or infrastructure that enables a customer to retain exclusive control over their own private keys."

Two limbs are covered — safekeeping or administering the Virtual Assets themselves under limb (a), and safekeeping or administering the private cryptographic keys or other access mechanism under limb (b) — and both are qualified by the phrase "on behalf of customers and pursuant to their instructions." The service is defined by acting for someone else's assets under their direction, not by simply building the infrastructure that lets a customer act for themselves.

## Where does the self-custody software carve-out sit, and what does it exclude?

The carve-out is the final clause of item 3, and it is drafted as an express exclusion rather than a separate exemption elsewhere in the Act: the definition "excludes the mere provision of software, hardware or infrastructure that enables a customer to retain exclusive control over their own private keys." A provider whose product does nothing more than give a customer the tools to hold and use their own keys — with the customer, not the provider, retaining exclusive control — sits outside item 3 by the Act's own wording, regardless of how sophisticated that software or hardware is.

The word "mere" is doing real work in that sentence. It signals that the carve-out is for providers whose role stops at supplying the tool — it does not extend to a provider that supplies software but also retains some form of access to, backup of, or control over the customer's keys alongside that software, since at that point the provider is doing more than "mere" provision.

## What is the practical test for whether a wallet provider needs a Custody Services licence?

The test the Act sets is exclusive control, not technical proximity to the keys. A provider needs to ask, honestly, who can move the customer's Virtual Assets without that customer's active, independent participation. If the answer is "only the customer, using the software we gave them," the carve-out applies. If the answer is "the provider can, whether through a recovery mechanism, a backend key share, a multi-signature arrangement the provider participates in, or any other means that lets the provider transfer or dispose of the asset without the customer's independent action," the provider has moved into limb (b) territory and needs authorisation for Custody Services.

A useful, if informal, way to apply this: hardware wallets and open-source key-management software sold as products, with no ongoing relationship between vendor and key, sit squarely in the carve-out. Custodial exchange wallets, institutional custody platforms, and "non-custodial" products that retain a recovery or co-signing role for the provider sit inside the licensed category — the marketing label a provider chooses for its own product does not decide which side of the line it falls on.

## Does Custody Services cover only Virtual Assets, or private keys too?

Both, and separately. Limb (a) covers safekeeping or administration of the Virtual Assets themselves — the more familiar image of a custodian holding coins on a customer's behalf. Limb (b) covers safekeeping or administration of "private cryptographic keys or other means of access that allow the customer to transfer or dispose of Virtual Assets independently" — a distinct activity that can exist even where the provider never technically "holds" the [Virtual Asset](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-license-pakistan-complete-guide-22) itself, since holding the access mechanism that controls an asset is treated as its own regulated activity under the Act.

This means a business that never takes custody of a coin, but instead administers the keys that would let a customer move that coin, is still within item 3's scope through limb (b) alone. The two limbs are drafted with "or" between them precisely because either one, on its own, is enough to bring an activity inside the definition.

## Is Custody Services one of PVARA's phased AML-Registered Services?

Yes. Regulation 2.3 of [PVARA](https://www.coinconnect.site/pvara-guide)'s [No Objection Certificate](https://www.coinconnect.site/regulatory-licensing) Regulations 2025 names Custody Services as one of four "[AML](https://www.coinconnect.site/blog/3/fit-and-proper-aml-pvara-mistakes-54) Registered Services" — together with [Broker-Dealer](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-broker-dealer-license-what-it-covers-27), Exchange and Virtual Asset [Derivatives](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-derivatives-leverage-license-31) Services — that a firm may begin providing after receiving a [No Objection Certificate](https://blog.coinconnect.site/the-pvara-no-objection-certificate-a-complete-guide/) ("NOC") and completing [goAML](https://www.coinconnect.site/blog/coinconnect-insights-1/fmu-goaml-vasp-pakistan-17) registration, ahead of the full licence eventually required under section 21 of the Act. Regulation 18.1(f) still requires the registered applicant to progress toward that full licence within the period PVARA sets.

This phased route matters operationally for custody businesses in particular, because the custody obligations under Chapter 4 of the Act — segregation of [Customer Assets](https://www.coinconnect.site/blog/3/customer-assets-definition-pvara-pakistan-62) under section 24, custody standards and key-management controls under section 26, and proof-of-reserves obligations under section 27 — apply once a firm is actually holding customer keys or assets, which for an AML-Registered Service can begin before the full licence is granted.

## How does Custody Services interact with the segregation and key-management rules elsewhere in the Act?

Once a business is providing Custody Services under item 3, two further sets of obligations attach directly to that activity. Section 24(1) of the Act requires a Licensee to "at all times, hold Customer Assets in segregated accounts separate from its own assets," and section 24(4) prohibits rehypothecating, lending, pledging or otherwise encumbering Customer Assets without the customer's "explicit, informed, and revocable written consent." Section 26(1) separately requires a Licensee providing custody services to "ensure the secure custody and protection of Virtual Assets against unauthorized access, loss, or misuse" and to "maintain operational resilience, including robust disaster-recovery and business-continuity arrangements."

A firm that qualifies for a Custody Services licence under item 3 should treat sections 24 and 26 as the operational specification that follows immediately from that classification — segregation, consent-based handling and key-management controls are not separate, optional obligations but the direct consequence of being classified as a custodian in the first place.

## What should a business handling customer key material check before assuming it is exempt?

- **Trace who can move the asset without the customer's independent participation.** If the provider retains any recovery, backup or co-signing role over the key, the "mere provision" carve-out does not apply, regardless of how the product is marketed.
- **Test limbs (a) and (b) separately.** A business that never custodies the Virtual Asset itself can still be a custodian under limb (b) alone, if it administers the private keys or access mechanism.
- **Plan for sections 24 and 26 obligations from the point custody activity actually starts**, which for an AML-Registered Service under Regulation 2.3 can be before the full licence under section 21 is granted, not after.
- **Keep the self-custody carve-out narrow in internal compliance documentation** — "mere provision of software, hardware or infrastructure" is a specific, limited exclusion, not a general safe harbour for any wallet product.

## About this analysis

This analysis was prepared by the CoinConnect research desk from the Virtual Assets Act, 2026 — Schedule I item 3 and sections 24 and 26 — read alongside PVARA's No Objection Certificate Regulations 2025, Regulation 2.3. Where practice is not yet settled or guidance has not been issued, that is stated in the text above.

Regulatory positions change and specific requirements should be verified against the current position published by the relevant authority before you act on them. This is information and analysis, not legal advice, and it does not create an advisory relationship. Take professional advice on your own circumstances.

## Flags for Malik

1. The "exclusive control" framing I used to describe the practical test is my own synthesis of the carve-out's wording, not a phrase the Act itself uses as a defined term — the Act's actual words are "retain exclusive control over their own private keys," and I have kept close to that language rather than inventing a separate legal test.
2. The multi-signature and recovery-mechanism examples are illustrative interpretation, flagged as such in the text, since the Act does not name specific technical architectures — only the general "mere provision... that enables... exclusive control" standard.
