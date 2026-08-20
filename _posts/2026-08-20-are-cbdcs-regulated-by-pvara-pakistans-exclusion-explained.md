---
layout: post
title: "Are CBDCs Regulated by PVARA? Pakistan's Exclusion Explained"
date: 2026-08-20 08:34:43 +0500
categories: [Compliance]
author: "Malik Abbas"
description: "Central bank digital currency is expressly outside the Virtual Assets Act 2026. What section 2(2)(c) excludes, and what it does not."
---

A digital rupee issued by the State Bank of Pakistan would not be a Virtual Asset. It would not need a licence from the Pakistan Virtual Asset Regulatory Authority, and its issuer would not be an Issuer for the purposes of the Virtual Assets Act, 2026. That is not a policy inference. It is written into the scope provision of the Act itself.

The exclusion matters far beyond central bank policy. It is the same drafting choice that determines whether a tokenised deposit, a foreign digital currency, or a stablecoin referencing the rupee falls inside or outside the perimeter. Most of the commercial questions we are asked about central bank digital currency ("CBDC") are really questions about the boundary between a sovereign-issued digital currency and a privately issued token that references one.

This analysis reads the exclusion as drafted, identifies exactly how far it reaches, and sets out where the line sits for firms building payment or settlement products in Pakistan.

## Are CBDCs regulated by PVARA?

No. Under section 2(2)(c) of the Virtual Assets Act, 2026, the Act does not apply to digital representations of fiat currency issued by the State Bank of Pakistan or by any central bank or monetary authority of another sovereign jurisdiction. A CBDC therefore sits outside PVARA's licensing and supervisory perimeter entirely, both for the domestic digital rupee and for foreign CBDCs.

The operative wording of section 2(2)(c) is short:

> digital representations of fiat currency issued by the State Bank of Pakistan or any central bank or monetary authority of another sovereign jurisdiction;

Two features of that drafting are worth pausing on. First, it is symmetrical: a foreign CBDC is excluded on identical terms to a domestic one. Second, the trigger is the identity of the issuer, not the technology. A CBDC recorded on a distributed ledger is excluded because a central bank issued it, not because of how it is recorded.

## Why does the definition of "Virtual Asset" also exclude fiat?

Because the exclusion appears twice. Section 3(1)(xxxi) defines "Virtual Asset" as a digital representation of value that can be digitally traded or transferred and used for payment or investment purposes, but expressly carves out digital representations of fiat currency. So a CBDC fails the definitional test and is separately excluded from the Act's scope.

The definition reads, in relevant part:

> "Virtual Asset" means a digital representation of value that can be digitally traded or transferred and used for payment or investment purposes, but does not include digital representations of fiat currency, securities or other financial assets regulated under any other law except where represented, issued, or transferred using distributed ledger technology. For the avoidance of doubt, Virtual Assets are not legal tender;

Read that carefully, because there is a genuine drafting tension. The "except where represented, issued, or transferred using distributed ledger technology" clause appears to pull DLT-based instruments back into the definition. On its face, that could suggest a CBDC issued on a blockchain re-enters scope through the definition even though section 2(2)(c) pushes it out.

Our reading is that section 2(2) governs. It opens with "this Act shall not apply to the following digital representations of value or rights", which is a scope exclusion operating on the whole statute, and it names central bank issuance without any technology qualifier. A scope provision that disapplies the Act cannot sensibly be overridden by a definitional carve-back inside the Act. But the interaction between the two is not perfectly drafted, and PVARA has not, so far as the published documents show, issued guidance resolving it. Anyone building around this boundary should confirm the position directly with [the Authority](https://pvara.gov.pk) rather than rely on a textual reading alone.

## What is the difference between a CBDC and a Fiat-Referenced Token?

A CBDC is issued by a central bank and excluded from the Act. A Fiat-Referenced Token ("FRT") is issued by a private party, is fully within the Act, and is one of its most heavily regulated instruments. Section 3(1)(ix) defines an FRT as a Virtual Asset that purports to maintain a stable value relative to a single Official Currency and is redeemable at par by its issuer.

That distinction carries the entire regulatory weight. A rupee-denominated stablecoin issued by a company is not a digital rupee; it is a private claim referencing the rupee, and section 31 of the Act imposes a demanding regime on it.

| | CBDC | Fiat-Referenced Token |
|---|---|---|
| Issuer | Central bank or monetary authority (s.2(2)(c)) | Private legal person, the Issuer under s.3(1)(xiii) |
| Within the Act? | No — excluded by s.2(2)(c) | Yes |
| Legal tender | Recognised as legal tender under the law of the issuing country (s.3(1)(xxi)) | Expressly not legal tender (s.3(1)(xxxi)) |
| Reserve requirement | Not applicable | 100% backing in HQLA or prescribed assets, held as a Segregated Reserve (s.31(1)(a)) |
| Redemption | Central bank obligation | At par without undue delay (s.31(1)(b)) |
| Licensing | None under this Act | Full PVARA regime, plus consultation with the State Bank on reserves (s.31(2)) |

If you are structuring a rupee-referenced token, the reserve and redemption architecture is the whole compliance problem, and we have set out how that regime operates in detail in our analysis of [stablecoin issuance under PVARA](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-frt-stablecoin-issuance-32). Firms building tokens referencing commodities rather than currency face a related but distinct set of obligations under section 32, covered in our note on [asset-referenced token issuance](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-art-tokenized-gold-issuance-33).

## Does the CBDC exclusion mean you can build CBDC services without a licence?

No. The exclusion covers the instrument, not every business built around it. If a firm provides Virtual Asset Services as defined in section 18 and Schedule I, it needs a licence for those services regardless of whether a CBDC also features somewhere in the product. The exclusion removes the CBDC from the definition of Virtual Asset. It does not create a licence-free zone for the firm.

Consider the practical permutations:

- **A wallet that holds only CBDC.** No Virtual Asset is involved, so Schedule I item 3 (Custody and Administration Services) is not engaged. The activity will, however, almost certainly sit inside the State Bank of Pakistan's own perimeter — section 2(2)(b) of the Act separately excludes instruments within [SBP](https://www.sbp.org.pk) or [SECP](https://www.secp.gov.pk) jurisdiction.
- **An exchange offering CBDC against Bitcoin.** Bitcoin is a Virtual Asset. Under Schedule I item 4, exchanging Virtual Assets for fiat currency is Exchange Services. A licence is required. Our breakdown of [the ten PVARA licence categories](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-license-categories-explained-23) maps which activities attach to which category.
- **A settlement rail that moves CBDC and stablecoins.** The stablecoin leg is a Virtual Asset. Schedule I item 8, Virtual Asset Transfer and Settlement Services, is engaged for that leg. The [transfer and settlement licence](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-transfer-settlement-license-payments-remittance-28) analysis covers the scope question.
- **Custody of CBDC on behalf of a government body.** Section 38 of the Act contemplates a Strategic Digital Wallet Company, wholly owned or designated by the Federal Government, to perform custody and administration and to operate wallet infrastructure for the Government of Pakistan and designated public bodies. Section 38(2) provides that it "shall not provide services to the private persons."

The general prohibition in section 50 is the point to hold onto: no person may, by way of business, engage in any Virtual Asset Services in or from Pakistan unless incorporated in Pakistan and holding a valid PVARA licence. Whether you need [regulatory licensing support](https://www.coinconnect.site/regulatory-licensing) turns on whether any leg of your product touches a Virtual Asset, not on how you describe the product.

## What about tokenised deposits and bank-issued digital money?

Tokenised commercial bank deposits are not addressed by name in the Act. The likely route out of scope is section 2(2)(b), which excludes securities, derivatives, collective investment schemes, depositary receipts and other traditional financial instruments falling within the regulatory jurisdiction of the State Bank of Pakistan or the Securities and Exchange Commission of Pakistan. A bank deposit sits within SBP jurisdiction.

But there is a real classification risk, and it is deliberate. Section 9(1)(f) gives PVARA power to:

> assess, determine, and classify any Virtual Asset, service, activity, offering, issuer, or service provider based on its substantive features, underlying function, method of use, or economic effect, irrespective of the nomenclature, structure, or designation assigned to it

That subsection requires consultation with the State Bank or the SECP where the asset exhibits characteristics falling within their respective mandates. So the classification of a tokenised deposit is a substance question decided by the Authority in consultation with the incumbent regulator — not a question you settle by choosing a label in your own documentation. We have written separately on how substance-over-form classification cuts through naming conventions in the context of the [closed-loop token exemption](https://www.coinconnect.site/blog/3/pakistan-pvara-closed-loop-token-exemption-2026-60) and the [NFT exemption](https://www.coinconnect.site/blog/coinconnect-insights-1/nft-exemption-pakistan-pvara-virtual-assets-act-2026-61).

In practice, if your product is close to this boundary, the honest answer is that you need a written classification view before you commit engineering resource — and, where the answer is genuinely unsettled, the [regulatory sandbox](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-sandbox-form-i-complete-walkthrough-2026-8) under section 35 exists precisely to test propositions that require regulatory flexibility.

## Does the CBDC exclusion affect AML obligations?

Not for licensed firms. Section 46(1) of the Act deems Virtual Asset Service Providers licensed under the Act to be financial institutions for the purposes of the Anti-Money Laundering Act, 2010, with all the obligations that follow. Those obligations attach to the licensee, not to individual asset types, so a licensee cannot narrow its AML perimeter by pointing at a CBDC leg.

Three consequences follow directly:

1. **Reporting.** Section 46(2)(a) requires suspicious transaction reporting to the [Financial Monitoring Unit](https://www.fmu.gov.pk). Our [FMU goAML registration guide](https://www.coinconnect.site/blog/coinconnect-insights-1/fmu-goaml-vasp-pakistan-17) covers the mechanics.
2. **Travel rule.** Section 47(1) requires originator and beneficiary information to be obtained, held and transmitted on transfers of Virtual Assets meeting the prescribed threshold, consistent with the [FATF](https://www.fatf-gafi.org) Recommendations. A CBDC leg is not a Virtual Asset transfer, but a mixed transaction still has a Virtual Asset leg.
3. **Records.** Section 47(4) requires transaction, customer due diligence and risk assessment records to be kept for a period prescribed by Regulations, not less than the AMLA 2010 period. The PVARA No Objection Certificate Regulations 2025 set a minimum of seven years at Regulation 13.1 for AML/CFT records.

Firms working through pre-licence obligations should note that the NOC Regulations designate Broker-Dealer, Custody, Exchange and Virtual Asset Derivative Services as "AML Registered Services", which may be provided after goAML registration and NOC issuance and before a full licence. That phased pathway, and the [corporate setup](https://www.coinconnect.site/corporate-setup) and [tax and banking](https://www.coinconnect.site/tax-banking) work it triggers, is where most market entrants actually spend their first six months.

## About this analysis

This analysis was prepared by the CoinConnect research desk from the Virtual Assets Act, 2026 as passed by the National Assembly (including Schedule I) and the PVARA No Objection Certificate Regulations 2025, read as published. Where practice is not yet settled or guidance has not been issued, that is stated above.

Regulatory positions change and specific requirements should be verified against the current position published by the relevant authority before you act on them. This is information and analysis, not legal advice, and it does not create an advisory relationship. Take professional advice on your own circumstances.
