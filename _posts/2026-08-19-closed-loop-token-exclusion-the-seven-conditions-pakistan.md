---
layout: post
title: "Closed-Loop Token Exclusion: The Seven Conditions (Pakistan)"
date: 2026-08-19 08:34:30 +0500
categories: [Compliance]
author: "Malik Abbas"
description: "Section 2(2)(a) of Pakistan's Virtual Assets Act 2026 excludes closed-loop tokens only if seven conditions are met. We read each one, and the drafting gap."
---

Most product teams that come to us with a points balance, a loyalty credit or an in-game currency arrive with the same assumption: because the token never leaves their app, it cannot be a virtual asset, so nothing in Pakistan's new framework applies. That assumption is sometimes right. It is right far less often than people think.

The Virtual Assets Act, 2026 does carve out closed-ecosystem tokens. But it does so through a list of conditions that are, read together, much narrower than the phrase "closed-loop" suggests in ordinary commercial usage. One bridge, one secondary market listing, one redemption for a real-world voucher, and the carve-out is gone.

This article sets out the seven conditions in full, explains what each one actually forecloses, and identifies the one drafting question in the provision that no guidance has yet resolved.

## What is the closed-loop token exclusion under Pakistan's Virtual Assets Act?

The closed-loop exclusion is in section 2(2)(a) of the Virtual Assets Act, 2026. It removes closed-ecosystem digital tokens from the Act entirely — no licence, no No-Objection Certificate, no issuer obligations — but only where the token satisfies all seven listed conditions by design, technical architecture, or enforceable system controls.

The framing matters. Section 2(2) opens:

> For the avoidance of doubt, this Act shall not apply to the following digital representations of value or rights, insofar as they meet the conditions stated below—

Two things follow. First, the exclusion is from the whole Act, not from a single licensing category — so it is not the same kind of relief as one of the [ten PVARA licence categories](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-license-categories-explained-23) or a sandbox admission. Second, "insofar as they meet the conditions" is a live, continuing test. A token that qualifies at launch stops qualifying the moment its design changes.

Sitting alongside paragraph (a) are separate exclusions for securities and traditional instruments within State Bank or SECP jurisdiction (paragraph (b)), digital representations of fiat currency issued by a central bank (paragraph (c)), certain non-fungible tokens (paragraphs (d) and (e)), and anything else "expressly excluded by the Authority" (paragraph (f)). The [NFT exclusion](https://www.coinconnect.site/blog/coinconnect-insights-1/nft-exemption-pakistan-pvara-virtual-assets-act-2026-61) operates on a different test and should not be conflated with this one.

## What are the seven conditions in full?

Section 2(2)(a) applies to "closed-ecosystem or closed-loop digital tokens, including any digital representation of value or rights that, by design, technical architecture, or enforceable system controls, satisfies all of the following conditions". Those conditions, in the Act's own words:

> (i) is usable or redeemable solely within a restricted digital platform, ecosystem, application, or network administered by the issuer or operator;
>
> (ii) is not transferable outside such platform, ecosystem, application, or network, whether directly or indirectly;
>
> (iii) is not exchangeable for fiat currency or legal tender outside such ecosystem;
>
> (iv) is not redeemable for real-world goods or services outside such ecosystem;
>
> (v) is not convertible into, exchangeable for, or interoperable with any other Virtual Asset;
>
> (vi) is not saleable, tradable, or transferable on any external market, exchange, or secondary trading venue; or
>
> (vii) is not designed, marketed, or used for payment, investment, or value-transfer purposes beyond such ecosystem.

Read as a set, these conditions do more than require a walled garden. They require a walled garden with no exits, no on-ramps, no interoperability, and no marketing that implies any of the above.

| Condition | What it forecloses | The design that typically breaks it |
|---|---|---|
| (i) Sole use within a restricted platform administered by the issuer or operator | Any use case outside the administered environment | Partner or franchise networks the issuer does not administer |
| (ii) No transferability outside, directly or indirectly | Peer-to-peer transfer off-platform | Wallet export, self-custody, a public-chain deployment |
| (iii) Not exchangeable for fiat or legal tender outside | Cash-out | Refund-to-card, PKR withdrawal, agent cash-out |
| (iv) Not redeemable for real-world goods or services outside | Off-platform spending | Third-party gift cards, retail vouchers, merchant acceptance |
| (v) Not convertible into or interoperable with any other Virtual Asset | Crypto convertibility | A bridge, a swap, an ERC-20 wrapper |
| (vi) Not saleable, tradable or transferable on any external venue | Secondary market | Any listing, including one the issuer did not arrange |
| (vii) Not designed, marketed or used for payment, investment or value-transfer beyond the ecosystem | Positioning as money or as an investment | "Earn yield", "future exchange listing", "spend anywhere" |

Condition (vii) is the one commercial teams underestimate. It reaches marketing and actual use, not just architecture. A token can be technically sealed and still fail because of how it was sold. Note also the drafting: the condition bites on how the token is "designed, marketed, or used", so third-party use patterns the issuer tolerates are relevant.

## Does a token have to meet all seven conditions, or only one?

Our reading is that all seven must be satisfied. The lead-in to section 2(2)(a) says the token must "satisfy all of the following conditions", which is conjunctive language. However, condition (vi) ends with "or" rather than a semicolon, which is disjunctive drafting. The two cannot both be given effect.

This is a genuine ambiguity and we flag it as one. On ordinary principles of construction the governing lead-in prevails over a connector inside the enumerated list, and the lead-in is unambiguous. A disjunctive reading would also collapse the exclusion into absurdity: any token that merely failed to be listed on an exchange would escape the Act, which cannot have been intended given the Act's stated purpose of investor protection and market integrity.

No guidance has been issued on this point. Until the Authority resolves it — through regulations under section 68, or through its classification power — the only defensible compliance position is to assume every condition must be met. Do not build a product on the "or".

## Who decides whether a token is closed-loop?

The Authority decides, not the issuer. Section 9(1)(f) gives PVARA express power to classify any virtual asset, service, activity, offering, issuer or service provider on its substantive features, underlying function, method of use, or economic effect — "irrespective of the nomenclature, structure, or designation assigned to it".

> ...assess, determine, and classify any Virtual Asset, service, activity, offering, issuer, or service provider based on its substantive features, underlying function, method of use, or economic effect, irrespective of the nomenclature, structure, or designation assigned to it.

That power is expressly framed as including the determination of "whether an asset is a Virtual Asset". Where the asset shows characteristics falling within the mandate of the [State Bank of Pakistan](https://www.sbp.org.pk/) or the [SECP](https://www.secp.gov.pk/), section 9(1)(f) requires the Authority to consult them before classifying.

In practice this means a self-assessment memorandum is a defensive document, not a permission. It records the basis on which you concluded the Act does not apply. It does not bind the Authority. If your token sits near the boundary, the substantive route is to test the position — the [regulatory sandbox](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-sandbox-reduced-capital-pakistan-19) under section 35, or one of the other [entry routes compared here](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-routes-compared-sandbox-noc-license-20). Note the tension, though: the Sandbox Guidelines' own self-assessment checklist at Annexure-A treats a model "not related to Virtual Asset Services or the related eco-system" as a negative indicator of scope. A genuinely excluded token may therefore be outside the sandbox as well as outside the Act, leaving no formal comfort mechanism. We regard that as an unresolved gap.

## What does "by design, technical architecture, or enforceable system controls" require?

It requires that the closure be built in and enforceable, not merely promised. Terms of service that prohibit off-platform transfer, without technical controls that prevent it, are unlikely to satisfy section 2(2)(a) — particularly where condition (ii) extends to transfer "whether directly or indirectly".

Practical questions to work through before you conclude the exclusion applies:

- Is the ledger permissioned and administered by you, or is the token deployed on a public network where anyone can construct a transfer?
- Can a user export a key, seed phrase or signed message that lets them move the balance?
- Does any third party — a payments partner, a marketplace, an aggregator — accept, price or quote the token?
- Is there any redemption path that terminates in fiat, in a gift card, or in goods you do not supply?
- Could a bridge or wrapper be deployed by someone other than you? Condition (v) speaks to interoperability, not just to interoperability you authorised.
- Has any of your marketing, in any language or market, described the token as an investment, a payment instrument or a future listing?

If the honest answer to any of these is uncertain, treat the token as in scope and plan accordingly. The [PVARA licensing pathway](https://www.coinconnect.site/pvara-guide) and the [full VASP licence analysis](https://www.coinconnect.site/blog/coinconnect-insights-1/vasp-license-pakistan-3) set out what that involves.

## What happens if the classification is wrong?

Getting it wrong is a criminal exposure, not a paperwork problem. Under section 54(1) of the Act, wilfully providing an unlicensed virtual asset service is punishable with imprisonment up to five years, a fine up to fifty million rupees, or both. Section 59(4) allows the Authority a further administrative fine up to twenty-five million rupees for any contravention.

Three consequences follow from a token being in scope when you assumed it was not:

1. **Licensing.** Section 50 prohibits any person from providing virtual asset services in or from Pakistan by way of business unless it is a company incorporated in Pakistan and holds a valid PVARA licence. Section 19(1) requires a No-Objection Certificate *before* incorporation, which reorders the usual [company registration sequence](https://www.coinconnect.site/blog/coinconnect-insights-1/secp-crypto-company-registration-pakistan-16) — see our note on [corporate setup](https://www.coinconnect.site/corporate-setup).
2. **Marketing.** Section 43(1) prohibits advertising or marketing a virtual asset unless the issuer holds a valid licence or registration. An in-scope token that has been promoted is already in breach.
3. **Distribution and access.** Section 61 lets the Authority block or direct the blocking of websites, apps, adverts and payment links relating to an unlicensed virtual asset service, with directions capable of being issued to app stores, hosting providers and payment providers.

Note too that exclusion from this Act is not exclusion from everything else. Section 5(1) states that the Act's provisions are "in addition to, and not in derogation of, any other law". A closed-loop token can be outside PVARA and still engage consumer protection, data protection, foreign exchange and tax obligations — which is why the [tax and banking](https://www.coinconnect.site/tax-banking) analysis runs in parallel to the classification question, and why an excluded product still needs the [general position on Pakistan's crypto rules](https://www.coinconnect.site/faq) checked before launch.

## About this analysis

This analysis was prepared by the CoinConnect research desk from the Virtual
Assets Act, 2026, the PVARA No Objection Certificate Regulations and the PVARA
Sandbox Guidelines 2026, read as published. Where practice is not yet settled or
guidance has not been issued, that is stated in the text above.

Regulatory positions change and specific requirements should be verified against
the current position published by the relevant authority before you act on them.
This is information and analysis, not legal advice, and it does not create an
advisory relationship. Take professional advice on your own circumstances.