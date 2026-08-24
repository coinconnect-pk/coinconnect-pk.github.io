---
layout: post
title: "Official Currency and Person: Definitions That Decide"
date: 2026-08-24 20:23:05 +0500
categories: [Compliance]
author: "Malik Abbas"
description: "Whether your token is a Fiat-Referenced Token turns on two short definitions in section 3(1). Most stablecoin analysis gets decided here, not in Chapter 5."
---

Two of the shortest definitions in the [Virtual Assets Act](https://blog.coinconnect.site/pakistans-virtual-assets-act-2026-the-complete-guide/), 2026 carry more weight than their length suggests. "Official or Fiat Currency" runs to one sentence. "Person" runs to six words. Between them they decide whether a token falls into the most heavily regulated category in the Act.

If you are building anything that holds a stable value, the analysis starts here — not in the chapter about stablecoins.

## What counts as an Official or Fiat Currency?

Section 3(1)(xxi) defines it as "a currency issued by the central bank or monetary authority of a country that is recognized as legal tender under the laws of that country".

Three elements have to be present together:

1. **Issued by a central bank or monetary authority** — not by a commercial bank, a private consortium, or a corporation
2. **Of a country** — a sovereign issuer
3. **Recognised as legal tender** under that country's own laws

All three must hold. A currency failing any one of them is not an Official Currency for the purposes of this Act, however widely it is used.

## Why does that definition decide stablecoin classification?

Because it is the hinge of the [Fiat-Referenced Token](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-frt-stablecoin-issuance-32) definition.

Section 3(1)(ix) defines a Fiat-Referenced Token as a [Virtual Asset](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-license-pakistan-complete-guide-22) that "purports to maintain a stable value relative to a single Official Currency of any country and is redeemable at par value by its issuer".

Read that against section 3(1)(xxi) and the test becomes mechanical:

| Your token references | Fiat-Referenced Token? |
|---|---|
| One sovereign legal-tender currency, redeemable at par | Yes |
| A basket of several currencies | No — the Act says "a single Official Currency" |
| Gold, or another commodity | No — that is the Asset-Referenced Token question |
| Another virtual asset | No |
| A currency, but not redeemable at par | No — both limbs are required |

Two limbs, both mandatory: single official currency, **and** redeemable at par by the issuer. A token satisfying one but not the other is not an FRT, which does not mean it is unregulated — it means it is classified somewhere else, most likely as an [asset-referenced token](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-art-tokenized-gold-issuance-33) or as an ordinary [virtual asset](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-license-pakistan-complete-guide-22).

The phrase "of any country" also matters. A token referencing the US dollar is caught in Pakistan just as a rupee-referenced token would be. The Act does not limit the definition to the Pakistani rupee, so a foreign-currency [stablecoin](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-frt-stablecoin-issuance-32) offered in or from Pakistan engages the same classification.

## What does "purports to" do in the definition?

It shifts the test from outcome to representation, and this is easy to miss.

Section 3(1)(ix) says a token that "purports to maintain" a stable value. It does not say a token that succeeds in maintaining one. A token that claims parity and then breaks it does not leave the category by failing — if anything, that is precisely when the category matters most.

Our reading is that classification attaches at the point of representation to the market. That means marketing material, whitepapers and product descriptions are part of the classification analysis, not separate from it. A product team that describes a token as "pegged" or "always redeemable 1:1" has made a classification decision whether or not it intended to. This reading should be confirmed with the Authority before a business relies on it.

## Why does the definition of "Person" matter?

Section 3(1)(xxii) defines "Person" as "a natural or legal Person" — six words that appear throughout the Act and quietly determine who can be caught by it.

Because the definition covers both individuals and legal entities, the obligations that attach to a "Person" attach to both. That is why the [Issuer](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-license-categories-explained-23) definition in section 3(1)(xiii) refers to "the legal Person" specifically — where the Act wants to exclude natural persons, it says so.

Note also section 3(2), which provides that words not defined in the Act but defined in the State Bank of Pakistan Act, 1956, the Securities Act, 2015, the [Anti-Money Laundering](https://www.coinconnect.site/blog/3/fit-and-proper-aml-pvara-mistakes-54) Act, 2010, or the Companies Act, 2017 carry the meanings assigned in those Acts, unless the context requires otherwise.

That is a significant provision for anyone reading the Act in isolation. Terms you cannot find in section 3 may still be defined — just somewhere else. Before concluding that a term is undefined and therefore open, check those four statutes.

## What should a token project actually do with this?

The classification work belongs before the build, not after it:

- **Identify the reference asset precisely.** One sovereign currency, a basket, a commodity, or another virtual asset — each leads somewhere different.
- **Decide the redemption promise deliberately.** "Redeemable at par value by its issuer" is a limb of the FRT test, not marketing language. Whether you make that promise is a regulatory decision.
- **Audit your own marketing.** If the token is described as pegged or par-redeemable anywhere, treat it as caught until advised otherwise.
- **Check the four borrowed statutes.** Section 3(2) means an undefined term may not be undefined at all.

Where a token sits genuinely near the boundary — a partially-backed unit, or one referencing a currency without a firm redemption promise — the [regulatory sandbox](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-sandbox-form-i-complete-walkthrough-2026-8) exists for exactly that uncertainty. Testing under supervision beats launching on an assumption.

Getting this right early also shapes the rest of the entry sequence, because the classification determines which obligations you are structuring for when you reach [SECP registration](https://www.coinconnect.site/corporate-setup), [banking](https://www.coinconnect.site/blog/coinconnect-insights-1/crypto-banking-vasp-15) and the [licence application](https://www.coinconnect.site/regulatory-licensing) itself.

## What is a "Segregated Reserve", and when does it apply?

If your token turns out to be reserve-backed, this is the definition that shapes the operating model.

Section 3(1)(xxvi) defines a Segregated Reserve as a pool of reserve assets kept separate from the Issuer's own assets, held in the name of the Issuer or in a trust or special vehicle for the benefit of token holders, and under custody with an independent custodian or regulated financial institution approved by the Authority — "so that the Issuer or its creditors cannot claim the assets".

That closing clause is the point of the whole definition. The structure exists to survive the issuer's insolvency.

Four requirements sit inside it:

- **Separation** from the issuer's own assets
- **Holding structure** — in the issuer's name, or a trust or special vehicle for token holders
- **Independent custody** — a custodian or regulated financial institution
- **Authority approval** of that custodian

The subsection then reserves further detail to Regulations: asset types, custody arrangements, audits, attestations, disclosures "and other safeguards".

For a project, the practical consequence is that reserve backing is not an accounting arrangement you can design internally. It requires an approved third party, and the approval sits with the Authority. That makes custodian selection a dependency with a lead time, in the same category as [banking](https://www.coinconnect.site/blog/coinconnect-insights-1/crypto-banking-vasp-15) and audit — and it should be raised early rather than treated as an implementation detail after the [licence application](https://www.coinconnect.site/regulatory-licensing) is filed.

## About this analysis

This analysis was prepared by the CoinConnect research desk from the Virtual Assets Act, 2026 as passed by the National Assembly, read as published. Where practice is not yet settled or guidance has not been issued, that is stated in the text above.

Regulatory positions change and specific requirements should be verified against the current position published by the relevant authority before you act on them. This is information and analysis, not legal advice, and it does not create an advisory relationship. Take professional advice on your own circumstances.
