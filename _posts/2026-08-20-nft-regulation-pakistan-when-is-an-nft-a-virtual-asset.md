---
layout: post
title: "NFT Regulation Pakistan: When Is an NFT a Virtual Asset?"
date: 2026-08-20 20:07:37 +0500
categories: [Compliance]
author: "Malik Abbas"
description: "Pakistan's Virtual Assets Act 2026 carves most NFTs out of regulation — but not all. The payment-or-investment test and the substance test decide which."
---

Most people reading Pakistan's new virtual asset law stop at the word "exempt" and put the document down. Section 2(2)(d) of the Virtual Assets Act, 2026 does exclude non-fungible tokens from the Act. It excludes them conditionally.

The conditions are the whole story. An NFT project in Karachi that mints artwork and an NFT project that fractionalises an apartment block sit on opposite sides of a line drawn in a single sub-clause — and only one of them needs a licence from the Pakistan Virtual Asset Regulatory Authority.

This article works through the two tests the Act applies: the **payment-or-investment test** in section 2(2)(d), and the broader **substance, function or economic effect test** in section 2(2)(e), reinforced by the Authority's classification power in section 9(1)(f). If you are building anything that mints, sells, custodies or lists NFTs in or from Pakistan, these two tests decide whether you are outside the perimeter or inside it.

## Is an NFT regulated in Pakistan?

An NFT is not regulated under the Virtual Assets Act, 2026 only if it is not used for payment or investment **and** does not represent, reference, or derive value from any security, commodity, financial asset, or other regulated instrument. Fail either limb and the NFT is treated as a Virtual Asset, bringing licensing, AML and conduct obligations into play.

The Act defines the token type at section 3(1)(xx):

> "Non-Fungible Token" or "NFT" means a unique, non-interchangeable digital representation of value or rights recorded on a distributed ledger or similar technology, where each token is distinguishable from every other token.

Note what that definition does *not* do. It does not exempt anything. Being non-fungible is a technical property, not a regulatory status. The exemption lives separately, in the scope provision at section 2(2), which lists the digital representations the Act does not apply to "insofar as they meet the conditions stated below".

That phrase — *insofar as they meet the conditions* — is the load-bearing language. The carve-out is conditional in form, and the burden of showing the conditions are met sits with the person relying on it.

## What is the payment-or-investment test in section 2(2)(d)?

Section 2(2)(d) exempts:

> a non-fungible token that is not used for payment or investment and does not represent, reference, or derive value from any security, commodity, financial asset, or other regulated instrument

There are two cumulative limbs, and both must hold:

| Limb | What it asks | Fails when |
|---|---|---|
| Use limb | Is the token used for payment or investment? | Token is accepted as consideration, or marketed and held for financial return |
| Reference limb | Does it represent, reference or derive value from a security, commodity, financial asset or other regulated instrument? | Token is tied to gold, equity, debt, rental income, a fund unit |

The use limb is drafted around *use*, not intention. That matters. A collectible minted with no financial purpose can drift into "used for payment" if a merchant network starts accepting it, or into "used for investment" if the issuer builds buy-back, yield or revenue-share features around it. The Act's scope is assessed against what the token does in the market, not what the whitepaper said on day one.

The reference limb is broader than most founders expect. "Commodity" and "financial asset" are wide categories, and the clause captures tokens that merely *reference* or *derive value from* them — no direct legal claim is needed. An NFT whose redemption price tracks the spot price of a metal references a commodity even if the holder owns no metal.

Our reading is that the reference limb is where most tokenised real-world-asset projects fail. If you are tokenising anything with an underlying, read our analysis of [asset-referenced token issuance under PVARA](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-art-tokenized-gold-issuance-33) before you assume NFT status protects you.

## What does the substance, function or economic effect test add?

Section 2(2)(e) adds a second, catch-all exclusion for "any non-fungible token or digital collectible that does not constitute a Virtual Asset, having regard to its substance, function, or economic effect." Read with section 9(1)(f), it gives the Authority express power to look past labels and classify a token by what it actually is.

Section 9(1)(f) empowers the Authority to:

> assess, determine, and classify any Virtual Asset, service, activity, offering, issuer, or service provider based on its substantive features, underlying function, method of use, or economic effect, irrespective of the nomenclature, structure, or designation assigned to it

Three consequences follow, and each is worth stating plainly.

- **Labelling is worthless.** Calling something an NFT, a membership pass, a digital collectible or a utility receipt does not change its classification. The Act says "irrespective of the nomenclature".
- **Classification is the Authority's to make.** It is not a self-assessment that binds the regulator, though a reasoned self-assessment is what you will be asked to produce.
- **Where the token looks like a security or a commodity claim, other regulators are consulted.** Section 9(1)(f) requires consultation with the State Bank of Pakistan or the [Securities and Exchange Commission of Pakistan](https://www.secp.gov.pk/) where the asset exhibits characteristics falling within their mandates. Section 2(2)(b) separately excludes securities, derivatives and collective investment schemes that already sit within SBP or SECP jurisdiction.

In practice, an NFT can therefore be regulated by PVARA as a Virtual Asset, regulated by SECP as a security, or fall outside both. It is a three-way question, not a binary. That interaction is one we cover in the broader [PVARA licence guide](https://www.coinconnect.site/pvara-guide).

## Which NFT models are likely to be caught?

The following table sets out how the two tests typically apply. It is analysis, not a statement of the Authority's published position — no NFT-specific guidance has been issued at the time of writing.

| Model | Likely status | Why |
|---|---|---|
| One-off digital artwork, no buy-back, no yield | Likely outside | Neither payment nor investment use; no regulated underlying |
| Event ticket or venue access pass, non-transferable outside the platform | Likely outside; may also engage the closed-loop carve-out | Utility function; check section 2(2)(a) conditions |
| Fractionalised NFT over property, giving rental income | Likely inside | References a financial asset; economic entitlement present |
| NFT redeemable for a fixed quantity of a metal | Likely inside | Derives value from a commodity |
| Gaming item freely tradable on external marketplaces and marketed on price appreciation | Fact-dependent, risk of inside | Investment use may be established by market behaviour |
| NFT accepted as consideration across merchants | Likely inside | Payment use on the face of the use limb |

Note the interaction with the closed-loop exclusion at section 2(2)(a), which exempts tokens that satisfy all of a long list of conditions — usable only within a restricted platform, not transferable outside it, not exchangeable for fiat, not convertible into any other Virtual Asset, not tradable on any secondary venue. We have broken that provision down separately in our piece on the [closed-loop token exemption](https://www.coinconnect.site/blog/3/pakistan-pvara-closed-loop-token-exemption-2026-60). Many in-game NFT models fail it at the transferability condition.

Section 2(2)(f) also lets the Authority expressly exclude "any other digital representation of value or rights". That is a power to widen the perimeter's exits, not a promise to use it.

## What obligations follow if your NFT is caught?

If the token is a Virtual Asset, three separate obligation sets can attach: issuance, service provision, and marketing. They are independent of one another.

1. **Issuance.** Under section 3(1)(xiii), the Issuer is the legal person that originates or creates the asset and retains primary control over initial supply, reserve assets or on-chain governance. Schedule I item 9 makes Virtual Assets Issuance Services a licensable category. Section 42(1) requires an Issuer offering to the public to publish a whitepaper in the prescribed form.
2. **Service provision.** A marketplace is rarely just a marketplace. Matching buyers and sellers or maintaining an order book is Exchange Services under Schedule I item 4; holding private keys for users is Custody and Administration Services under item 3; arranging orders between two parties is Broker-Dealer Services under item 2. Our breakdown of the [ten PVARA licence categories](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-license-categories-explained-23) sets out where each line is drawn, and the [exchange licence analysis](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-exchange-license-requirements-capital-obligations-24) and [custody licence analysis](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-custody-license-safeguarding-customer-assets-25) go deeper on the two most common.
3. **Marketing.** Section 43(1) is blunt: "No person shall advertise or market a Virtual Asset unless the Issuer holds a valid license or registration under this Act." Marketing exposure can therefore arise for parties who never touch the token.

Section 50 prohibits carrying on any Virtual Asset Service by way of business in or from Pakistan unless the person is a company incorporated in Pakistan **and** holds a valid licence. Section 19(1) requires a No-Objection Certificate from the Authority *before* incorporation begins — the sequencing catches people out, and it is the first thing we address in [corporate setup work](https://www.coinconnect.site/corporate-setup). Wilfully providing an unlicensed service is punishable under section 54(1) with imprisonment up to five years, a fine up to fifty million rupees, or both.

Where the token is caught, AML obligations follow too. Section 46(1) deems licensed Virtual Asset Service Providers to be financial institutions for the purposes of the Anti-Money Laundering Act, 2010, with suspicious transaction reporting to the Financial Monitoring Unit and the [goAML registration](https://www.coinconnect.site/blog/coinconnect-insights-1/fmu-goaml-vasp-pakistan-17) that goes with it. Section 47 applies travel rule obligations consistent with [FATF](https://www.fatf-gafi.org/) recommendations. Custody models additionally engage the segregation duty in section 24, which we unpack in our note on the [definition of Customer Assets](https://www.coinconnect.site/blog/3/customer-assets-definition-pvara-pakistan-62).

## How should an NFT business document its position?

Build a written classification file before you launch, not after a regulator asks. Because section 9(1)(f) lets the Authority classify on substance and method of use, the file must address how the token behaves in the market — not only how it is described.

A workable file covers:

- The token's technical properties and the ledger it sits on.
- A limb-by-limb analysis against section 2(2)(d), separating the use limb from the reference limb.
- Any underlying asset, index or price feed the token references, however indirectly.
- Secondary-market controls: whether transfer outside your platform is possible, and if so, what that does to the closed-loop analysis.
- Marketing copy review, since investment framing in promotional material is evidence of investment use.
- The trigger events that would require re-assessment — adding buy-backs, revenue share, external listings or merchant acceptance.

Where the answer is genuinely uncertain, the Act provides routes short of a full licence. Section 35 allows the Authority to establish a regulatory sandbox and, under section 35(3), to issue guidance, no-objection statements or no-action communications in accordance with Regulations. The PVARA Sandbox Guidelines set out an agile intake, a self-assessment checklist and a sixty-working-day evaluation window after initial screening. We compare that route against the NOC and full-licence paths in [PVARA routes compared](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-routes-compared-sandbox-noc-license-20).

Two practical points. First, if you were already providing Virtual Asset Services immediately before commencement, section 70 gives six months to apply for a licence or cease. Second, if you disagree with a classification, section 63 allows an appeal to the Virtual Assets Appellate Tribunal within thirty days of communication of the order.

Classification is the cheapest work you will ever do on an NFT project and the most expensive to skip. If you want that analysis run properly against your token design, our [regulatory and licensing practice](https://www.coinconnect.site/regulatory-licensing) does exactly this, and the [FAQ](https://www.coinconnect.site/faq) answers the questions we are asked most often. Tax treatment sits on a separate track and is dealt with in our [tax and banking](https://www.coinconnect.site/tax-banking) work.

## About this analysis

This analysis was prepared by the CoinConnect research desk from the Virtual Assets Act, 2026 as passed by the National Assembly, the PVARA Sandbox Guidelines 2026, and the PVARA No Objection Certificate Regulations 2025, read as published. Where practice is not yet settled or guidance has not been issued — and no NFT-specific classification guidance has been issued at the time of writing — that is stated above.

Regulatory positions change and specific requirements should be verified against the current position published by the relevant authority before you act on them. This is information and analysis, not legal advice, and it does not create an advisory relationship. Take professional advice on your own circumstances.
