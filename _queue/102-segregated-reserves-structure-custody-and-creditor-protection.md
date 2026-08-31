---
layout: post
title: "Segregated Reserves: The Structure That Protects Token Holders"
date: 2026-01-01 09:00:00 +0500
categories: [Compliance]
author: "Malik Abbas"
description: "Section 3(1)(xxvi) defines the Segregated Reserve that backs Pakistani stablecoins — a structure built to survive the issuer's own insolvency."
---

A reserve promise is only as good as the legal structure holding it. Pakistan's [Virtual Assets Act](https://blog.coinconnect.site/pakistans-virtual-assets-act-2026-the-complete-guide/), 2026 does not simply require issuers to say their tokens are backed — section 3(1)(xxvi) defines a specific legal structure, the Segregated Reserve, engineered so the backing survives even if the Issuer itself fails.

## What is a Segregated Reserve under the Act?

Section 3(1)(xxvi) defines a Segregated Reserve as a pool of reserve assets kept separate from the Issuer's own assets, held in the Issuer's name or in a trust or special vehicle for the benefit of token holders, under [custody](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-custody-license-safeguarding-customer-assets-25) with an independent custodian or regulated financial institution approved by the Authority, structured so the Issuer or its creditors cannot claim the assets.

Section 3(1)(xxvi) states a Segregated Reserve means:

> a pool of reserve assets that is kept separate from the Issuer's own assets, held in the name of the Issuer, or in a trust or special vehicle for the benefit of token holders, and under custody, with independent custodian or regulated financial institution, approved by the authority, so that the Issuer or its creditors cannot claim the assets. The Authority may, by Regulations, prescribe additional requirements regarding the types of assets, custody arrangements, audits, attestations, disclosures, and other safeguards.

This is a dense provision, and it is worth taking apart clause by clause because each one does separate work.

## What does "kept separate from the Issuer's own assets" actually require?

This is the segregation principle familiar from the Act's broader customer-asset regime. Section 24(1) imposes an analogous segregation duty on Licensees generally in respect of [Customer Assets](https://www.coinconnect.site/blog/3/customer-assets-definition-pvara-pakistan-62), and section 3(1)(xxvi) applies the same underlying logic to reserve assets specifically. The reserve cannot sit commingled in the Issuer's general operating accounts or balance sheet — it must be identifiably distinct, so that in a dispute or an insolvency, the reserve assets can be traced and separated from the Issuer's own property.

## Why does the definition offer two different holding structures?

The definition allows the reserve to be "held in the name of the Issuer, or in a trust or special vehicle for the benefit of token holders" — two structurally different options, joined by "or".

- **Held in the name of the Issuer**: the assets remain legally titled to the Issuer, but segregated and held under custody arrangements that keep them out of reach of the Issuer's creditors
- **Held in a trust or special vehicle**: the assets are placed in a separate legal structure — a trust, or a special purpose vehicle — created specifically to hold reserve assets for the benefit of token holders, adding a further legal layer of separation between the Issuer's own affairs and the reserve

The trust or special-vehicle route is the stronger structural protection, because it interposes an independent legal person or fiduciary relationship between the reserve and the Issuer's own legal identity. Holding assets merely "in the name of the Issuer, but segregated" relies more heavily on custody arrangements and accounting discipline to achieve the same practical outcome. The Act permits either, but they are not equivalent in the strength of the separation they provide, and an Issuer choosing between them should weigh that difference deliberately rather than default to whichever is administratively simpler.

## What does "custody, with independent custodian or regulated financial institution, approved by the authority" add?

This clause layers a custody requirement on top of whichever holding structure is chosen. Whether the reserve sits in the Issuer's own name or in a trust vehicle, it must additionally be held under custody with an independent custodian or a regulated financial institution, and that custodian or institution must be approved by the Authority. This custody layer is the trigger for section 28, which separately requires "a custodian of reserve assets" to comply with requirements, oversight and inspection standards Regulations prescribe — the Segregated Reserve definition and section 28 are companion provisions, one defining the structure, the other regulating the party holding it.

## What is the practical effect of "so that the Issuer or its creditors cannot claim the assets"?

This closing phrase states the purpose the entire definition is built to achieve: creditor remoteness. In an insolvency, an Issuer's general creditors ordinarily have claims against the Issuer's assets in accordance with insolvency law. A properly structured Segregated Reserve is designed to sit outside that pool entirely — token holders' claim to the reserve assets should not compete with, or be diluted by, the claims of the Issuer's ordinary creditors.

This purpose connects directly to two other provisions in the Act:

- section 24(2), which states that Customer Assets held by a Licensee "shall not form part of the Licensee's estate in the event of its insolvency or liquidation" — a parallel insolvency-remoteness principle applied to customer holdings generally
- section 31(1)(e) and section 32(1)(d), which both require "prioritized holder protections in insolvency" for [Fiat-Referenced Token](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-frt-stablecoin-issuance-32) and [Asset-Referenced Token](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-art-tokenized-gold-issuance-33) issuers respectively — the Segregated Reserve structure is the mechanism through which that prioritised protection is meant to be delivered in practice

## What does the Authority's power to prescribe "additional requirements" leave open?

The final sentence of section 3(1)(xxvi) gives the Authority power to prescribe, by Regulations, additional requirements covering the types of assets eligible for the reserve, custody arrangements, audits, attestations, disclosures, and other safeguards. None of this detail exists in the Act's text itself. At the time of writing, no Regulations elaborating on Segregated Reserve mechanics had been published, meaning several practical questions — precisely which custodians qualify for Authority approval, what audit frequency applies to the reserve specifically, and what disclosure format is required — remain open.

| Element of the definition | What it establishes | What is left to Regulations |
|---|---|---|
| Kept separate from Issuer's own assets | Segregation principle | Specific accounting or technical segregation standards |
| Held in Issuer's name, or in trust/special vehicle | Two permitted holding structures | No stated preference or further conditions between them |
| Custody with independent custodian or regulated institution, Authority-approved | Custody and approval requirement | Approval criteria for custodians (linked to section 28) |
| Creditor-remoteness purpose | The reserve's protective goal | Enforcement mechanics in an actual insolvency scenario |
| Authority's power to add requirements | Room for future detail | Asset types, custody rules, audit cadence, disclosure format |

## How does the Segregated Reserve requirement differ between Fiat-Referenced and Asset-Referenced Tokens?

The Segregated Reserve definition itself does not distinguish between token types — it is a single, general structure referenced by both section 31 (Fiat-Referenced Tokens, held as a Segregated Reserve of HQLA or other prescribed assets) and section 32 (Asset-Referenced Tokens, held in custody in accordance with Regulations). The underlying assets differ by token type, but the structural requirement — separation from the Issuer, an approved custody arrangement, and creditor remoteness — applies to both in the same terms.

## What should an issuer building a reserve structure decide now?

- choose deliberately between holding reserve assets in the Issuer's own name (segregated) or in a trust or special vehicle, rather than defaulting without weighing the stronger separation the trust route provides
- select a custodian or regulated financial institution with a credible path to Authority approval, since section 28 makes that approval a direct regulatory requirement on the custodian itself
- document the creditor-remoteness structure in the legal instruments governing the reserve — trust deeds, custody agreements, or equivalent — in terms an insolvency practitioner or court could rely on, not only in marketing or whitepaper language
- build the reserve's audit and disclosure practice to be ready for whatever cadence and format Regulations eventually prescribe, rather than waiting for those Regulations before establishing any audit trail
- coordinate the reserve structure with the section 27 proof-of-reserves and annual audit obligations that apply to the Licensee generally, so the two compliance workstreams reconcile rather than run separately

Issuers building either a [fiat-referenced token](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-frt-stablecoin-issuance-32) or [asset-referenced token](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-art-tokenized-gold-issuance-33) programme should treat the Segregated Reserve structure as a legal-engineering decision to get right at the outset, since restructuring reserve custody after token holders already exist is considerably harder than designing it correctly before launch, and this belongs early in [regulatory licensing](https://www.coinconnect.site/regulatory-licensing) preparation.

## Related reading

- [Reserve Custodians Under Pakistan's Virtual Assets Act](https://blog.coinconnect.site/pakistans-virtual-assets-act-2026-the-complete-guide/)
- [Customer Assets Definition Under PVARA Pakistan](https://www.coinconnect.site/blog/3/customer-assets-definition-pvara-pakistan-62)
- [Stablecoin Issuance Under PVARA: Reserve Rules 2026](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-frt-stablecoin-issuance-32)

## About this analysis

This analysis was prepared by the CoinConnect research desk from the Virtual Assets Act, 2026, read as published. Where practice is not yet settled or guidance has not been issued, that is stated in the text above.

Regulatory positions change and specific requirements should be verified against the current position published by the relevant authority before you act on them. This is information and analysis, not legal advice, and it does not create an advisory relationship. Take professional advice on your own circumstances.

## Flags for Malik

- This article deliberately covers different ground from the queued 092 reserve-custodians article (which focuses on section 28 oversight/inspection standards and the custodian relationship) by focusing on the Segregated Reserve structure itself — the trust-vs-own-name choice and creditor remoteness. There is necessarily some overlap since both are grounded in the same section 3(1)(xxvi) definition; flag if you'd rather I trim the overlap further.
- The "Related reading" link to the 092 reserve-custodians article points at the pillar-guide URL as a placeholder since 092 is queued but not yet published under its own URL — please swap in 092's actual published URL once it goes live, or drop the link if that's easier.
- The claim that the trust/special-vehicle route is the "stronger structural protection" compared to holding assets in the Issuer's own name is our analysis of the two options the Act permits, not a statement the Act itself makes — clearly labelled, but worth a second look given it's a substantive judgement call for issuers.
