---
layout: post
title: "SECP, SBP or PVARA? Who Regulates Your Virtual Asset"
date: 2026-01-01 09:00:00 +0500
categories: [Compliance]
author: "Malik Abbas"
description: "Which digital assets fall outside PVARA to the SBP or SECP under the Virtual Assets Act 2026, and how PVARA classifies borderline instruments."
---

Most regulatory disputes in a new virtual asset market are not about whether a business is compliant. They are about who it is compliant *to*. A tokenised sukuk, a stablecoin pegged to the rupee, a platform offering perpetual futures on Bitcoin — each of these sits near a line drawn between the Pakistan Virtual Asset Regulatory Authority, the State Bank of Pakistan and the Securities and Exchange Commission of Pakistan.

The Virtual Assets Act, 2026 draws that line in three places: section 2(2), which carves certain instruments out of the Act entirely; section 5(3), which vests primary jurisdiction in PVARA; and section 9(1)(f), which gives PVARA the power to look past what you call your product and classify it on what it actually does.

This article works through all three, and explains what a business should do when it genuinely cannot tell which regulator it answers to.

## Which digital assets fall outside PVARA's remit entirely?

Under section 2(2) of the Virtual Assets Act, 2026, the Act does not apply to securities, derivatives, collective investment schemes, depositary receipts or other traditional financial instruments falling within the regulatory jurisdiction of the State Bank of Pakistan or the Securities and Exchange Commission of Pakistan; digital representations of fiat currency issued by a central bank; qualifying closed-loop tokens; and certain non-fungible tokens.

The provision reads, in relevant part:

> (2) For the avoidance of doubt, this Act shall not apply to the following digital representations of value or rights, insofar as they meet the conditions stated below— … (b) securities, derivatives, collective investment schemes, depositary receipts, or other traditional financial instruments that fall within the regulatory jurisdiction of the State Bank of Pakistan or the Securities and Exchange Commission of Pakistan; (c) digital representations of fiat currency issued by the State Bank of Pakistan or any central bank or monetary authority of another sovereign jurisdiction …

Two features of the drafting matter more than they first appear.

First, the carve-out in section 2(2)(b) is not framed by reference to the *form* of the instrument. It turns on whether the instrument "falls within the regulatory jurisdiction" of the SBP or SECP. So the question is not "is this a token?" but "would a Pakistani regulator, applying its own statute, treat this as a security or derivative?" That is a question of securities law before it is a question of virtual asset law.

Second, the carve-outs are conditional. Section 2(2) opens with the words "insofar as they meet the conditions stated below". An instrument that starts inside a carve-out and drifts outside it — a closed-loop token that becomes transferable, for instance — loses the exemption. We have covered the closed-loop conditions in detail in our analysis of [Pakistan's closed-loop token exemption](https://www.coinconnect.site/blog/3/pakistan-pvara-closed-loop-token-exemption-2026-60), and the NFT carve-outs in [NFT exemption under PVARA](https://www.coinconnect.site/blog/coinconnect-insights-1/nft-exemption-pakistan-pvara-virtual-assets-act-2026-61).

## What does the definition of "Virtual Asset" itself say about securities?

The definition in section 3(1)(xxxi) of the Act excludes securities and other regulated financial assets — but with an important qualifier. It excludes them "except where represented, issued, or transferred using distributed ledger technology". That exception pulls tokenised traditional instruments back towards the Act, and sits in some tension with the carve-out in section 2(2)(b).

The full definition:

> "Virtual Asset" means a digital representation of value that can be digitally traded or transferred and used for payment or investment purposes, but does not include digital representations of fiat currency, securities or other financial assets regulated under any other law except where represented, issued, or transferred using distributed ledger technology. For the avoidance of doubt, Virtual Assets are not legal tender;

**Our reading is** that these two provisions must be read together rather than in isolation, and that the practical resolution lies in section 5(3) and in PVARA's classification power. Section 2(2)(b) removes instruments that fall within SBP or SECP jurisdiction; section 3(1)(xxxi) signals that DLT representation is not, by itself, enough to keep an instrument outside the Act. Where the two pull in different directions — a tokenised equity, say — the Act does not resolve it on the face of the text. It resolves it procedurally, by giving PVARA a classification power exercisable in consultation with the other regulator.

**In practice**, a business in that position should not self-classify and hope. It should seek a determination. We say more about how below.

## Who has primary jurisdiction over tokenisation and blockchain?

Section 5(3) of the Act vests primary regulatory and supervisory responsibility for virtual assets, virtual asset service providers, tokenisation of real-world assets and blockchain technology in PVARA, "in coordination with other relevant regulators where applicable". Section 5(1) makes the Act additional to other laws and gives it primacy in the event of inconsistency, with two exceptions.

The relevant text:

> (3) The regulation and supervision of Virtual Assets, Virtual Asset Service Providers, tokenization of real-world assets, and blockchain technology shall vest primarily in the Authority under this Act, in coordination with other relevant regulators where applicable.

The two exceptions to PVARA's primacy under section 5 are worth noting because they cut in opposite directions:

| Provision | Effect |
|---|---|
| s.5(1) | The Act prevails over inconsistent laws — **except** the Foreign Exchange Regulation Act, 1947 |
| s.5(2) | Laws on data protection, data governance, cybersecurity, financial secrecy and cross-border personal data transfer **prevail over** the Act |
| s.5(3) | Primary jurisdiction over virtual assets, VASPs, tokenisation and blockchain vests in PVARA |

So the foreign exchange regime is not displaced. Neither is the data protection regime. Both bind licensees alongside the Act, and both matter enormously to a cross-border exchange arranging fiat rails — a point we develop in our work on [banking access for licensed VASPs](https://www.coinconnect.site/blog/coinconnect-insights-1/crypto-banking-pakistan-vasp-15).

## How does PVARA classify a borderline asset?

Section 9(1)(f) of the Act empowers PVARA to classify any virtual asset, service, activity, offering, issuer or service provider on its substantive features, underlying function, method of use or economic effect — regardless of what it is called or how it is structured. Where the asset shows characteristics within SBP or SECP mandates, PVARA must consult that regulator.

The provision, in full:

> (f) assess, determine, and classify any Virtual Asset, service, activity, offering, issuer, or service provider based on its substantive features, underlying function, method of use, or economic effect, irrespective of the nomenclature, structure, or designation assigned to it. Such classification may include, but is not limited to the determination of whether an asset is a Virtual Asset, whether a Person qualifies as a Virtual Asset Service Provider, or whether an offering constitutes a financial activity within the scope of this Act subject to consultation with the State Bank of Pakistan or the Securities and Exchange Commission of Pakistan where the asset exhibits characteristics falling within their respective mandates;

Three things follow from this drafting, and they should shape how anyone structures a product for the Pakistani market:

- **Labels carry no weight.** "Irrespective of the nomenclature, structure, or designation assigned to it" is about as clear as statutory drafting gets. Calling a yield product a "reward" or an offering a "distribution" changes nothing.
- **Economic effect is a test in its own right.** An instrument that functions as a pooled investment will be assessed as one, even if the legal wrapper says otherwise.
- **Consultation is mandatory, not discretionary,** where the asset exhibits characteristics within the SBP or SECP mandate. That is a safeguard for the applicant as much as a coordination mechanism between regulators.

Section 9(2)(l) reinforces the point by allowing PVARA to enter cooperation arrangements with domestic and foreign regulators, and section 17(1) requires the Authority to share supervisory and enforcement information with the SBP, the SECP, the Financial Monitoring Unit, the Federal Investigation Agency and the Federal Board of Revenue. A jurisdictional question raised in one forum will not stay in one forum.

## Where do the real borderline cases sit?

The hardest cases in practice cluster around four product types: tokenised securities, asset-referenced tokens, virtual asset derivatives and stablecoins. Each has statutory anchors on both sides of the line, and each requires a determination rather than an assumption.

**Virtual asset derivatives.** Section 2(2)(b) carves out derivatives within SBP or SECP jurisdiction. Yet Schedule I, item 6, expressly lists "Virtual Asset Derivatives Services" — the offering, facilitation, execution, clearing, trading or arranging of futures, options, swaps and contracts for difference — as a licensable virtual asset service. The distinction the Act appears to draw is between derivatives *on virtual assets*, which PVARA licenses, and derivatives on conventional underlyings, which do not become PVARA's business merely because they are recorded on a ledger. We set out the licensing consequences in our note on the [PVARA derivatives and leverage licence](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-derivatives-leverage-license-31).

**Asset-referenced tokens.** Section 32(2) permits an asset-referenced token to reference "commodities, real estate, real-world assets, securities, financial assets, or a combination of official currencies" — but prohibits backing by other virtual assets. A token referencing listed securities is therefore contemplated by the Act while also touching the SECP's core mandate squarely. Section 32(3) allows PVARA to prescribe eligible categories of underlying assets and to restrict or prohibit types. Our analysis of [asset-referenced token issuance](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-art-tokenized-gold-issuance-33) works through the reserve mechanics.

**Fiat-referenced tokens.** Section 31 sets the issuance requirements — one hundred per cent reserve backing in high-quality liquid assets held as a segregated reserve, redemption at par without undue delay, audited reserve disclosures, AML/CFT/CPF programmes and prioritised holder protections in insolvency. Section 31(2) expressly contemplates "consultation with the State Bank of Pakistan on reserve arrangements". A rupee-referenced token is not a central bank digital currency and is not carved out by section 2(2)(c), but it plainly engages the SBP's monetary mandate. The [stablecoin issuance analysis](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-frt-stablecoin-issuance-32) covers the reserve rules.

**Tokenised traditional instruments.** This is the genuinely unsettled category, for the reasons set out in the section above. The Act does not, as published, provide a bright-line test. Guidance has not been issued.

## What should a business do when the jurisdiction is unclear?

Seek a classification determination before you build, not after. Section 9(1)(f) gives PVARA the power to classify; section 35 provides for a regulatory sandbox; and section 35(3) permits the Authority to issue guidance, no-objection statements or no-action communications. Those are the instruments designed for exactly this problem.

A practical sequence:

1. **Map the instrument against the section 2(2) carve-outs first.** If every condition of a carve-out is satisfied and will remain satisfied, the Act does not apply. Document why, in writing, at the design stage.
2. **Test the economic substance, not the wrapper.** Ask what a supervisor applying section 9(1)(f) would conclude about function, method of use and economic effect.
3. **Consider the sandbox route.** The PVARA Sandbox Guidelines 2026 operate on an agile basis, with applications accepted across the year, and the guidelines identify a "Genuine Need for Sandbox" criterion covering propositions that require "regulatory flexibility to test novel mechanisms (token issuance, DeFi protocols, smart contracts, custodial services)". Our comparison of the [sandbox, NOC and full licence routes](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-routes-compared-sandbox-noc-license-20) sets out the trade-offs, and the [Form I walkthrough](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-sandbox-form-i-complete-walkthrough-2026-8) covers the submission itself.
4. **Do not assume a foreign classification travels.** Section 9(1)(f) applies Pakistani statutory tests. A token treated as a utility elsewhere may be assessed differently here.
5. **Disclose existing licences honestly.** Form A1 of the No Objection Certificate Regulations 2025, at Sections 9.1 and 9.2, requires disclosure of any licence held from the SBP, the SECP or any other Pakistani authority, and of any foreign regulatory licence or registration.

Getting this wrong is not a paperwork problem. Section 50 prohibits unlicensed virtual asset services, and section 54(1) makes wilfully providing one punishable with imprisonment up to five years, a fine up to fifty million rupees, or both. Section 54(4) attaches up to three years and a fine up to twenty million rupees to knowingly making a false or misleading statement in an application. A misclassification defended by a plausible-sounding label is not a defence the Act contemplates.

The [PVARA licence guide](https://www.coinconnect.site/pvara-guide) sets out the wider framework, and our [regulatory and licensing](https://www.coinconnect.site/regulatory-licensing) and [corporate setup](https://www.coinconnect.site/corporate-setup) pages cover the entity and filing work that follows a classification decision. Tax obligations run separately under section 66 and are addressed on our [tax and banking](https://www.coinconnect.site/tax-banking) page.

## About this analysis

This analysis was prepared by the CoinConnect research desk from the Virtual Assets Act, 2026 as passed by the National Assembly, the PVARA No Objection Certificate Regulations 2025, and the PVARA Sandbox Guidelines 2026, read as published. Where practice is not yet settled or guidance has not been issued — in particular on the interaction between the section 2(2)(b) carve-out and the distributed ledger technology exception in the definition of "Virtual Asset" — that is stated above.

Regulatory positions change and specific requirements should be verified against the current position published by the relevant authority before you act on them. This is information and analysis, not legal advice, and it does not create an advisory relationship. Take professional advice on your own circumstances.

## Flags for Malik

1. **Genuine drafting tension flagged, not resolved.** Section 2(2)(b) carves out securities/derivatives within SBP/SECP jurisdiction, but the s.3(1)(xxxi) definition of "Virtual Asset" excludes securities "except where represented, issued, or transferred using distributed ledger technology". Read literally, a tokenised equity is both carved out and pulled in. I have flagged this openly and pointed readers to the classification power as the procedural resolution rather than asserting an answer. Worth your view on whether we take a firmer position.

2. **Sandbox Guidelines reference the Ordinance, the Act supersedes it.** The Sandbox Guidelines 2026 cite the Virtual Assets Ordinance, 2025 sections 42–45 throughout; the Act's sandbox provision is s.35 and s.74 saves acts done under the Ordinance. I have cited the Act for the sandbox power and the Guidelines only for operational content, avoiding Ordinance section numbers. Consider whether we should write a standalone piece on the Ordinance-to-Act renumbering.

3. **"Consultation is mandatory."** The s.9(1)(f) wording is "subject to consultation with the State Bank of Pakistan or the Securities and Exchange Commission of Pakistan where the asset exhibits characteristics falling within their respective mandates". I read "subject to" as mandatory in that circumstance. Flagging in case you read it as a condition on PVARA's power rather than a duty owed to applicants.

4. **No PVARA determination/no-action procedure exists yet in the documents.** Section 35(3) permits no-objection statements and no-action communications "in accordance with Regulations", and the Sandbox Guidelines cover No-Action Relief. But there is no published standalone classification-ruling procedure. I have described the route generally rather than inventing a form or timeline.

5. **Word count approx. 1,760. Title 51 characters. Description 148 characters. 11 internal links.**
