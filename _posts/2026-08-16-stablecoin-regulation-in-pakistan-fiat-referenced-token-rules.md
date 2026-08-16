---
layout: post
title: "Stablecoin Regulation in Pakistan: Fiat-Referenced Token Rules"
date: 2026-08-16 18:58:40 +0500
categories: [Licensing]
author: "Malik Abbas"
description: "Section 31 of the Virtual Assets Act 2026 sets six requirements for issuing a fiat-referenced token in Pakistan, plus a ban on algorithmic stablecoins."
---

Pakistan now has a statutory definition of a stablecoin. The [Virtual Assets Act](https://blog.coinconnect.site/pakistans-virtual-assets-act-2026-the-complete-guide/) 2026 does not use the word "stablecoin" at all — it splits the category in two, calling one type a **[Fiat-Referenced Token](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-frt-stablecoin-issuance-32)** and the other an **[Asset-Referenced Token](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-art-tokenized-gold-issuance-33)**, and it attaches a separate set of issuance requirements to each.

For anyone planning to issue a rupee-referenced or dollar-referenced token in or from Pakistan, section 31 is the operative provision. It is short — six requirements in a single subsection — but each one carries a great deal of downstream work, and one of them depends on a definition the Act deliberately leaves to Regulations.

This analysis reads section 3(1)(ix), section 31 and section 53 of the Act as passed, and sets out what an issuer can plan around today and what it cannot.

## What is a fiat-referenced token under Pakistani law?

A fiat-referenced token is a virtual asset that tries to hold a stable value against **one** national currency and is redeemable at face value from the issuer. Section 3(1)(ix) of the Virtual Assets Act 2026 defines it as:

> "Fiat-Referenced Token" means a Virtual Asset that purports to maintain a stable value relative to a single Official Currency of any country and is redeemable at par value by its issuer.

Three elements matter in that sentence. First, *purports* — the test is what the token holds itself out as doing, not whether the peg actually holds. Second, *a single Official Currency* — a token referenced to a basket of currencies falls outside this definition and is dealt with as an Asset-Referenced Token under section 32(2). Third, *redeemable at par value by its issuer* — a token with no redemption right against an issuer is not an FRT, and if its stability mechanism is algorithmic it runs into section 53 instead.

"Official or Fiat Currency" is separately defined in section 3(1)(xxi) as a currency issued by the central bank or monetary authority of a country and recognised as legal tender under that country's laws. So a token pegged to the US dollar is caught just as squarely as one pegged to the rupee.

A digital rupee issued by the [State Bank of Pakistan](https://www.sbp.org.pk/) is not caught at all. Section 2(2)(c) takes digital representations of fiat currency issued by the SBP or any other central bank outside the scope of the Act entirely. Central bank digital currency is not a stablecoin for these purposes.

## What are the six issuance requirements under section 31?

Section 31(1) imposes six requirements on "any Issuer intending to issue a Fiat-Referenced Token in Pakistan". They are cumulative, not alternatives:

| # | Requirement (s.31(1)) | What it turns on |
|---|---|---|
| (a) | 100% reserve backing in HQLA or other prescribed assets, held as a segregated reserve | Definition of HQLA in Regulations |
| (b) | Mechanisms for redemption at par value without undue delay | Operational and banking capability |
| (c) | Audited reserve disclosures as prescribed by the Authority | Audit and attestation cycle |
| (d) | Robust AML, CFT, CPF and sanctions compliance programmes | AMLA 2010 and FATF standards |
| (e) | Prioritised holder protections in insolvency | Reserve structuring |
| (f) | Any other requirement prescribed by the Authority | Open-ended |

Section 31(2) then allows the Authority to differentiate. It may prescribe requirements based on "the size, scope, complexity, or risk profile of the Issuer, including, but not limited to, expedited approval, stress testing, ongoing supervision, and consultation with the State Bank of Pakistan on reserve arrangements."

In practice, that last clause is the one to plan around. The Act expressly contemplates PVARA consulting the SBP on reserve arrangements for fiat-referenced tokens. Any issuer whose reserve sits in rupee-denominated instruments or in Pakistani bank deposits should expect a second regulator's view on the structure, which is a different exercise from the [PVARA licensing](https://www.coinconnect.site/regulatory-licensing) file itself.

## What does the 100% segregated reserve requirement actually demand?

It demands full backing in high-quality liquid assets, held in a structure that is bankruptcy-remote from the issuer. The Act defines the structure but not the assets. Section 3(1)(xxvi) defines Segregated Reserve as:

> a pool of reserve assets that is kept separate from the Issuer's own assets, held in the name of the Issuer, or in a trust or special vehicle for the benefit of token holders, and under custody, with independent custodian or regulated financial institution, approved by the authority, so that the Issuer or its creditors cannot claim the assets.

Four structural obligations are embedded there: separation from own assets; holding in the issuer's name or in a trust or special purpose vehicle for holders' benefit; custody with an *independent* custodian or regulated financial institution; and that custodian being **approved by the Authority**. The same definition allows the Authority to prescribe further requirements on asset types, custody arrangements, audits, attestations and disclosures.

Note what is missing. "High-Quality Liquid Assets" is defined in section 3(1)(x) as "such high-quality liquid assets as may be prescribed by Regulations". As at the date of the Act as passed, that Regulation is not before us. An issuer therefore cannot yet know, from the statute alone, whether short-dated government paper, term deposits, money market instruments or some combination will qualify. Our reading is that this is the single largest open variable in stablecoin planning in Pakistan, and it should be raised with the Authority in writing rather than assumed. Verify the current position at [pvara.gov.pk](https://pvara.gov.pk/).

Two adjacent provisions apply to the custody leg. Section 28 provides that a custodian of reserve assets must comply with the requirements, oversight and inspection standards prescribed by Regulations. Section 27(1) requires a Licensee to furnish cryptographic proof-of-reserves reconciled against its liabilities to customers at prescribed intervals, and section 27(2) requires an annual audit by a firm of Chartered Accountants approved by the Division concerned. Where the issuer is itself licensed, the [customer asset segregation duties in section 24](https://www.coinconnect.site/blog/3/customer-assets-definition-pvara-pakistan-62) sit alongside the reserve rule rather than replacing it.

## Are algorithmic stablecoins banned in Pakistan?

They are prohibited unless Regulations specifically permit them. Section 53 of the Act states:

> No Person shall issue, offer, or market a Virtual Asset whose primary mechanism for maintaining value is algorithmic and not fully or adequately collateralized, unless specifically permitted by Regulations and subject to the safeguards prescribed therein.

Read the two limbs together. The prohibition bites where the primary stability mechanism is algorithmic **and** the token is not fully or adequately collateralised. A token that is algorithmically managed but genuinely fully collateralised is not, on the face of the provision, caught — though it would then need to satisfy section 31 or section 32 on its own terms.

The prohibition also covers offering and marketing, not just issuance. That reaches distributors and promoters, not only the originator. It applies to "no Person", with no territorial qualifier in the section itself, so the general scope rule in section 2(1) and the extraterritorial powers in section 4 need to be read with it.

There is a drafting point worth flagging. Section 54, which lists the criminal offences, does not create a specific offence for contravening section 53, in the way section 54(2) does for unlawful Initial Virtual Asset Offerings and section 54(3) for market abuse under section 52. What does apply is section 59(1), under which the Authority may sanction "a Person [who] has contravened any provision of this Act", with a financial penalty and, under section 59(4), a fine up to twenty-five million rupees. Our reading is that a section 53 breach is enforced administratively rather than as a stand-alone crime, but the analysis changes the moment an unlicensed service or a false statement to the Authority is also in play.

## How do fiat-referenced and asset-referenced tokens differ?

An FRT tracks one national currency and is redeemable at par. An ART represents ownership, claims or economic interests in underlying assets, or maintains stable value by reference to them. The requirement sets overlap but are not identical.

| Feature | Fiat-Referenced Token (s.31) | Asset-Referenced Token (s.32) |
|---|---|---|
| Reference point | A single Official Currency | Underlying assets, incl. a combination of official currencies |
| Backing rule | 100% in HQLA or prescribed assets | Reserve of the underlying assets, as prescribed, in custody |
| Reserve held as | Segregated reserve (s.3(1)(xxvi)) | Custody in accordance with Regulations |
| Redemption | At par value without undue delay | Not expressed in the same terms in s.32(1) |
| Backing by other virtual assets | Not addressed in s.31 | Expressly prohibited by s.32(2) |
| Audited reserve disclosures | Required | Required |
| AML/CFT/CPF and sanctions programme | Required | Required |
| Insolvency priority for holders | Required | Required |

Section 32(2) is the sharper of the two: an ART must at all times be fully backed by the underlying assets and "shall not be backed or derive its value from other Virtual Assets". We have set out the ART route separately in our note on [asset-referenced token issuance and tokenised gold](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-art-tokenized-gold-issuance-33), and the reserve mechanics in our earlier piece on [stablecoin issuance and reserve rules](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-frt-stablecoin-issuance-32).

Do not assume the label you choose decides the category. Section 9(1)(f) empowers the Authority to classify any virtual asset, service or offering "based on its substantive features, underlying function, method of use, or economic effect, irrespective of the nomenclature, structure, or designation assigned to it", subject to consultation with the SBP or SECP where the asset falls within their mandates.

## Who can issue, and what licence is needed?

Only a company incorporated in Pakistan, holding the relevant PVARA licence. Section 50(1) prohibits any person from carrying on a Virtual Asset Service in or from Pakistan unless it is incorporated under the Companies Act 2017 (or another Pakistani incorporation law) and holds a valid PVARA licence. Item 9 of Schedule I makes "Virtual Assets Issuance Services" a licensable category, described as the creation, issuance, initial offering, administration and ongoing management of virtual assets, including supply control, reserve management, redemption, governance and required disclosures.

The sequence, drawing the provisions together:

1. **No-Objection Certificate first.** Section 19(1) requires anyone intending to incorporate a company with the primary objective of engaging in Virtual Asset Services to apply for an NOC *before* starting incorporation. The [NOC Regulations 2025 process](https://www.coinconnect.site/pvara-guide) runs on Forms A1 to A8.
2. **Incorporate.** [Company registration with the SECP](https://www.coinconnect.site/blog/coinconnect-insights-1/secp-crypto-company-registration-pakistan-16) follows the NOC, not the other way round, and our [corporate setup](https://www.coinconnect.site/corporate-setup) note explains the object clause point.
3. **Licence application.** Under section 19(4), in the prescribed form with the prescribed non-refundable fee. Which of the [ten Schedule I categories](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-license-categories-explained-23) you need depends on whether you also intend to exchange, custody or transfer the token.
4. **Offering approval.** Section 30(1) restricts Initial Virtual Asset Offerings to legal entities registered in Pakistan meeting the eligibility criteria prescribed by Regulations; section 30(2) reserves the conditions, disclosure requirements and approval process to Regulations.
5. **Whitepaper and ongoing disclosure.** Section 42(1) requires an Issuer offering a virtual asset to the public to publish a whitepaper in the prescribed form; section 42(2) requires ongoing disclosure of material information *including reserve attestations*.
6. **Marketing.** Section 43(1) prohibits advertising or marketing a virtual asset unless the Issuer holds a valid licence or registration under the Act, and section 43(2) requires risk disclosures in all marketing material.

That last point deserves emphasis for exchanges rather than issuers. Our reading of section 43(1) is that it constrains the promotion of *third-party* stablecoins as much as one's own, which is a listing and marketing question for any [foreign exchange entering Pakistan](https://www.coinconnect.site/blog/coinconnect-insights-1/foreign-crypto-exchange-enter-pakistan-pvara-21) with major dollar-referenced tokens on its order book. Guidance on how it applies to globally issued tokens has not been issued; we would not act on an assumption either way.

Also note section 33: an Issuer meeting thresholds prescribed by Regulations is a **Significant Issuer**, must be registered with the Authority, and must comply with enhanced reporting, disclosure, governance and risk management requirements. The thresholds have regard to size, scale, systemic importance, market impact, number of holders and cross-border activity. They are not in the Act.

## About this analysis

This analysis was prepared by the CoinConnect research desk from the Virtual
Assets Act, 2026, the PVARA No Objection Certificate Regulations and the PVARA
Sandbox Guidelines 2026, read as published. Where practice is not yet settled or
guidance has not been issued, that is stated in the text above.

Regulatory positions change and specific requirements should be verified against
the current position published by the relevant authority before you act on them.
This is information and analysis, not legal advice, and it does not create an
advisory relationship. Take professional advice on your own circumstances.