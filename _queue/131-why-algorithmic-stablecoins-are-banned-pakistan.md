---
layout: post
title: "Why Algorithmic Stablecoins Are Banned Under Pakistan's Act"
date: 2026-01-01 09:00:00 +0500
categories: [Enforcement]
author: "Malik Abbas"
description: "Section 53 bans undercollateralised algorithmic tokens outright. The collateralisation test, the narrow exception, and what it means for issuers in Pakistan."
---

Section 53 of the [Virtual Assets Act](https://blog.coinconnect.site/pakistans-virtual-assets-act-2026-the-complete-guide/) 2026 is one short sentence, and it settles a question that collapsed billions of dollars of value in other markets: can a token maintain its value through an algorithm alone, without assets standing behind it? In Pakistan, under this Act, the answer is no — unless the Pakistan [Virtual Asset](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-license-pakistan-complete-guide-22) Regulatory Authority ("[PVARA](https://www.coinconnect.site/pvara-guide)" or "the Authority") specifically permits it by Regulations.

This is a narrower and more precise prohibition than a blanket ban on algorithmic mechanisms. The section does not prohibit algorithms; it prohibits an algorithm being the *primary* mechanism for maintaining value where the token is *not* fully or adequately collateralised. That distinction is the whole article.

## What does section 53 actually prohibit?

Section 53 prohibits any person from issuing, offering, or marketing a virtual asset whose primary mechanism for maintaining value is algorithmic and not fully or adequately collateralised, unless the Authority specifically permits it by Regulations and subject to the safeguards those Regulations prescribe. The text reads:

> "No Person shall issue, offer, or market a Virtual Asset whose primary mechanism for maintaining value is algorithmic and not fully or adequately collateralized, unless specifically permitted by Regulations and subject to the safeguards prescribed therein."

Three elements have to be present together for section 53 to bite. First, the token's *primary* mechanism for maintaining value must be algorithmic — a rebasing supply, a mint-and-burn arbitrage loop, or a comparable code-driven stabilisation mechanism, rather than a reserve. Second, that token must be *not* fully or adequately collateralised — meaning it lacks assets held in reserve sufficient to back its claimed value. Third, no Regulations have specifically permitted the particular mechanism and its safeguards. All three conditions have to line up before the prohibition applies; remove any one of them and the token falls outside section 53's ban.

## What does "not fully or adequately collateralized" mean?

The Act does not define "fully or adequately collateralized" within section 53 itself, but the collateralisation standard it applies elsewhere gives the clearest available guide. Section 31, governing Fiat-Referenced Tokens, requires hundred percent reserve backing with High-Quality Liquid Assets or other prescribed assets, held as a segregated reserve. Section 32, governing Asset-Referenced Tokens, requires the token to "at all times be fully backed by the underlying assets".

| Token type | Collateralisation standard | Source |
|---|---|---|
| Fiat-Referenced Token | 100% reserve backing in HQLA or prescribed assets, segregated | Section 31(1)(a) |
| Asset-Referenced Token | Fully backed by underlying assets at all times | Section 32(2) |
| Algorithmic token (banned form) | Not fully or adequately collateralised, value maintained primarily by algorithm | Section 53 |

Our reading is that "fully or adequately collateralized" in section 53 is meant to be read against these two collateralisation standards set elsewhere in the Act — a token that meets the section 31 or section 32 reserve tests is, almost by definition, not the kind of token section 53 is aimed at, because its value-maintenance mechanism is the reserve, not an algorithm. The provision the Act has not published is precisely where the line sits between "adequately" collateralised and "fully" collateralised — whether partial collateralisation with an algorithmic top-up mechanism could ever qualify as "adequate" is not addressed in the source text, and should be verified with [PVARA](https://pvara.gov.pk) rather than assumed.

## What does "Fiat-Referenced Token" and "Asset-Referenced Token" mean, and how do they relate to section 53?

A [Fiat-Referenced Token](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-frt-stablecoin-issuance-32), defined at section 3(1)(ix), is a virtual asset that purports to maintain a stable value relative to a single official currency and is redeemable at par value by its issuer. An [Asset-Referenced Token](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-art-tokenized-gold-issuance-33), defined at section 3(1)(i), represents ownership rights, claims or economic interests in one or more underlying assets, or is designed to maintain a stable value by reference to those assets.

Both definitions describe value-stability mechanisms built on a reserve relationship, not an algorithm. A [stablecoin](https://www.coinconnect.site/regulatory-licensing) issuer operating under sections 31 or 32 is, by construction, outside section 53's prohibition — provided the reserve requirements in those sections are actually met in practice, not just in the whitepaper. Section 32(2) adds a further restriction relevant here: an Asset-Referenced Token "shall not be backed or derive its value from other Virtual Assets" — meaning a reserve made up of other crypto tokens does not satisfy the collateralisation test either, even where the tokens are fully algorithmic in mechanism themselves.

## Is there any way to legally issue an algorithmic token in Pakistan?

Yes, narrowly. Section 53 itself carves out an exception: an undercollateralised, algorithmically-stabilised token may be issued, offered or marketed if it is "specifically permitted by Regulations and subject to the safeguards prescribed therein." That is a two-part exception — the Authority must issue Regulations that specifically permit the mechanism, and any issuer relying on the exception must comply with whatever safeguards those Regulations attach.

As at the date of this analysis, no such Regulations are disclosed in the source documents reviewed for this piece. Until PVARA publishes them, the practical position for any issuer considering an algorithmic stability mechanism is that section 53 applies in full, and the exception is not yet available to rely on. This is also the route by which the [regulatory sandbox](https://www.coinconnect.site/regulatory-licensing) under section 35 becomes relevant — testing a novel stabilisation mechanism under controlled [sandbox](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-sandbox-reduced-capital-pakistan-19) conditions, with the Authority's oversight, is a materially different position from issuing it to the public under a claimed section 53 exemption that has not yet been prescribed.

## Why does the Act treat algorithmic tokens differently from other virtual assets?

The Statement of Objects and Reasons attached to the Act frames the entire statute around investor protection, transparency and market integrity, and around combating illicit use of virtual assets. Section 53 sits in Chapter 9, "Prohibitions", alongside the ban on unlicensed [virtual asset services](https://www.coinconnect.site/regulatory-licensing) under section 50, the ban on unauthorised Initial Virtual Asset Offerings under section 51, and the market manipulation and insider trading prohibitions under section 52. Placing algorithmic tokens in the same chapter as unlicensed activity signals that the drafters treat an uncollateralised, purely code-stabilised token as a structural risk to market integrity rather than a product-design choice to be disclosed and left to the market.

The Act does not state a specific rationale within section 53 itself beyond the collateralisation test, so this reading is drawn from the surrounding structure of the Act rather than from an explicit legislative note attached to the section.

## What penalty applies to a section 53 breach?

This is where the Act is less precise than it is on other prohibitions. Section 54, which sets out the Act's criminal offences, does not name a section 53 contravention among its six enumerated offences at subsections (1) through (6) — those cover unlicensed services, unauthorised Initial Virtual Asset Offerings, market manipulation and insider trading, false statements, obstruction, and non-compliance with an order, in that order. Section 53 is not listed.

That leaves two possible enforcement routes, both general rather than section-specific. First, section 59(1) allows the Authority to impose administrative sanctions — reprimand, a directive to cease or remedy, a financial penalty, licence suspension or revocation, or disqualification from office — for any contravention of the Act, which section 53 plainly is. Section 59(4) caps a financial penalty under that general power at twenty-five million Rupees. Second, if the same conduct also amounts to marketing or issuing a virtual asset without a licence, it could separately trigger section 54(1)'s unlicensed-service offence, which carries up to five years' imprisonment or a fine up to fifty million Rupees, or both — but that route depends on the underlying activity also breaching the licensing requirement, not on the algorithmic-token prohibition itself.

## What should an issuer take from this?

Anyone structuring a token intended for the Pakistani market needs to decide, at the design stage, whether the stability mechanism is reserve-based or algorithm-based, and size the reserve accordingly before approaching PVARA. A design that blends partial collateralisation with an algorithmic top-up sits in the most exposed position under section 53, because it is precisely the kind of hybrid the "fully or adequately collateralized" test was written to catch, and no published Regulations yet define where "adequate" ends. Structuring toward the section 31 or section 32 reserve standards — full backing, segregated [custody](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-custody-license-safeguarding-customer-assets-25), audited disclosure — is the only currently documented route to certainty, and it is worth building that into the [corporate setup](https://www.coinconnect.site/corporate-setup) and [licence application](https://www.coinconnect.site/regulatory-licensing) planning from day one rather than retrofitting it after a Regulations gap becomes a live enforcement question.

## About this analysis

This analysis was prepared by the CoinConnect research desk from the Virtual Assets Act 2026 as passed by the National Assembly — principally sections 3(1)(i), 3(1)(ix), 31, 32, 35, 50 to 54, and 59 — read as published. Where guidance or Regulations have not yet been issued, that is stated in the text above.

Regulatory positions change and specific requirements should be verified against the current position published by the relevant authority before you act on them. This is information and analysis, not legal advice, and it does not create an advisory relationship. Take professional advice on your own circumstances.

## Flags for Malik

1. Section 53 has no dedicated criminal penalty in section 54's enumerated list. I described the two general routes (section 59 administrative sanction, and section 54(1) only if the conduct is also an unlicensed service) rather than inventing a specific penalty — this mirrors the same gap flagged in our section 54 penalties piece.
2. "Fully or adequately collateralized" is not defined within section 53. I cross-referenced the section 31 and 32 reserve standards as the closest available benchmark, but the Act does not state that these standards apply to section 53 by cross-reference — that is my inference, flagged as such in the text ("Our reading is").
3. No Regulations permitting an algorithmic mechanism under the section 53 exception are disclosed in the source documents. If PVARA has since published such Regulations, this article needs a refresh before it goes further into distribution.
