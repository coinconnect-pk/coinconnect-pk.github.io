---
layout: post
title: "Asset-Referenced Tokens and the Backing Rule Under the Act"
date: 2026-01-01 09:00:00 +0500
categories: [Licensing]
author: "Malik Abbas"
description: "Section 32 of the Virtual Assets Act 2026 lets an asset-referenced token back with real-world assets but expressly bans backing it with other virtual assets."
---

Tokenising gold, real estate, or a basket of currencies works differently under Pakistan's [Virtual Assets Act](https://blog.coinconnect.site/pakistans-virtual-assets-act-2026-the-complete-guide/), 2026 than tokenising a single fiat peg. Section 32 governs this category — the [Asset-Referenced Token](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-art-tokenized-gold-issuance-33) — and draws one bright line that issuers building on this model need to understand before they choose what sits behind their token.

## What is an Asset-Referenced Token under the Act?

Section 3(1)(i) defines an Asset-Referenced Token as a [Virtual Asset](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-license-pakistan-complete-guide-22) that represents, directly or indirectly, ownership rights, claims or economic interests in one or more underlying assets, or that is designed to maintain a stable value by reference to such assets.

Section 3(1)(i) states an Asset-Referenced Token means:

> a Virtual Asset that represents, directly or indirectly, ownership rights, claims, or economic interests, including entitlements to receive or share income, returns, or other economic benefits, in respect of one or more underlying assets, or is designed to maintain a stable value by reference to such underlying assets.

This definition is broader than the [Fiat-Referenced Token](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-frt-stablecoin-issuance-32) definition in two respects. It is not limited to a single reference asset — "one or more underlying assets" — and it covers both value-stability designs and income or ownership-representation designs, not only pegged-value tokens. A token representing fractional ownership of a real estate portfolio and a token pegged to the value of a gold reserve could both fall within this single definition, depending on their design.

## What does section 32(1) require of an Asset-Referenced Token issuer?

Section 32(1) sets five requirements, broadly mirroring the structure of the Fiat-Referenced Token requirements in section 31(1), but adapted to a reserve of underlying assets rather than HQLA specifically.

Section 32(1) states an Issuer intending to issue an Asset-Referenced Token in Pakistan shall comply with the following requirements:

> (a) a reserve of the underlying assets, as prescribed, for Assets-referenced token held in custody in accordance with Regulations; (b) audited reserve disclosures as prescribed by the Authority; (c) robust AML, CFT, CPF and sanctions compliance programs; (d) prioritized holder protections in insolvency; and (e) any other requirement prescribed by the Authority.

| Requirement | What it means in practice |
|---|---|
| (a) Reserve of underlying assets in custody | The specific assets the token references must be held in custody, in a manner Regulations prescribe |
| (b) Audited reserve disclosures | Independent verification and disclosure of the reserve, in the form the Authority prescribes |
| (c) AML, CFT, CPF and sanctions compliance | A robust compliance programme covering money laundering, terrorist financing, proliferation financing and sanctions |
| (d) Prioritized holder protections in insolvency | Token holders must rank ahead of ordinary creditors, or otherwise be protected, if the Issuer becomes insolvent |
| (e) Any other requirement prescribed | An open-ended power for the Authority to add further requirements by Regulations |

## What is the core backing rule under section 32(2)?

Section 32(2) requires an Asset-Referenced Token to be fully backed by its underlying assets at all times, and lists the categories of assets it may reference — but it also states, expressly, what it may not be backed by.

Section 32(2) states:

> An Asset-Referenced Token shall at all times be fully backed by the underlying assets and may reference tangible or intangible assets, including but not limited to commodities, real estate, real-world assets, securities, financial assets, or a combination of official currencies, but shall not be backed or derive its value from other Virtual Assets.

Two things follow from this wording. First, "fully backed" and "at all times" set a continuous, not point-in-time, obligation — a token that was fully backed at issuance but has since drifted below full backing would not meet this standard, regardless of how it started. Second, the closing clause is an express prohibition: an Asset-Referenced Token cannot be backed by, or derive its value from, other Virtual Assets. A token collateralised by another cryptocurrency, rather than by a real-world asset, does not qualify as a compliant Asset-Referenced Token under this section.

## Why does the Act ban backing an Asset-Referenced Token with other virtual assets?

The Act does not state a reason in its text, but the prohibition addresses a structural risk that has caused well-documented failures in other markets — a token backed by another Virtual Asset carries the volatility of that backing asset directly through to the token's own value, and a sharp fall in the backing asset's price can trigger a simultaneous collapse in the token that depends on it. By excluding Virtual Asset backing from the Asset-Referenced Token category entirely, section 32(2) forces any such structure either to be built on genuinely external, real-world collateral, or to fall outside this category — and potentially outside what the Act permits at all, since section 53 separately prohibits algorithmic tokens whose primary value mechanism is not fully or adequately collateralised.

## What kinds of assets can lawfully back an Asset-Referenced Token?

Section 32(2)'s list is illustrative rather than exhaustive, signalled by the phrase "including but not limited to". The named categories are commodities, real estate, real-world assets, securities, financial assets, or a combination of official currencies.

- **commodities** — physical goods such as precious metals, agricultural products, or energy resources
- **real estate** — property or property-backed interests
- **real-world assets** more generally — a broad category capturing tangible or economically real assets beyond the specifically named types
- **securities and financial assets** — instruments that themselves may separately engage [SECP](https://www.coinconnect.site/corporate-setup) or SBP jurisdiction, depending on their nature
- **a combination of official currencies** — distinguishing this multi-currency basket structure from the single-currency Fiat-Referenced Token category in section 31

Where the underlying reference includes securities or financial assets, an Issuer should also consider whether the SECP or SBP has an independent regulatory interest in that underlying instrument, separate from [PVARA](https://www.coinconnect.site/pvara-guide)'s jurisdiction over the token itself — the Act's section 5(3) and section 9(1)(f) both point toward coordination between regulators where an asset's characteristics touch more than one mandate.

## How does section 32(3) allow the Authority to shape what qualifies?

Section 32(3) gives the Authority the same differentiated-requirements power that applies to Fiat-Referenced Tokens, and adds a further power specific to Asset-Referenced Tokens: prescribing eligible categories of underlying assets, and restricting or prohibiting particular asset types.

Section 32(3) states:

> The Authority may prescribe differentiated requirements based on the size, scope, complexity, or risk profile of the Issuer, including, but not limited to, expedited approval, stress testing, ongoing supervision, and consultation with the State Bank of Pakistan on reserve arrangements. The Authority may prescribe eligible categories of underlying assets and may restrict or prohibit types of assets for the issuance of Asset-Referenced Token.

This means the section 32(2) list of permitted asset categories, broad as it reads today, is not necessarily the final word. The Authority retains express power to narrow eligible asset categories by Regulations, or to prohibit specific types outright — a power that had not been exercised in the source documents at the time of writing, but which any issuer relying on an unusual or exotic underlying asset should factor into their planning.

## How does an Asset-Referenced Token differ from a Fiat-Referenced Token in practice?

| Feature | Fiat-Referenced Token (section 31) | Asset-Referenced Token (section 32) |
|---|---|---|
| Reference | A single Official Currency | One or more underlying assets — commodities, real estate, securities, currency baskets, and more |
| Reserve composition | 100% HQLA or other prescribed assets | Reserve of the specific underlying assets referenced |
| Redemption standard | At par value, without undue delay | Not separately specified in section 32 |
| Virtual Asset backing | Not addressed by section 31 directly | Expressly prohibited by section 32(2) |
| Authority's asset-restriction power | Not stated in section 31 | Expressly stated in section 32(3) |

## What should an issuer designing an Asset-Referenced Token check first?

- confirm every component of the intended backing is a real-world or otherwise permitted asset, and specifically confirm none of the backing derives from another Virtual Asset, given section 32(2)'s express prohibition
- build [custody](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-custody-license-safeguarding-customer-assets-25) and reserve-audit arrangements around whichever underlying asset is chosen, since a commodity reserve, a real-estate reserve and a securities reserve each carry different custody logistics
- monitor for Regulations narrowing eligible asset categories under section 32(3) before finalising a design built around an asset type that has not yet been tested with the Authority
- treat "fully backed... at all times" as a continuous monitoring obligation, not a one-time issuance check
- where the underlying asset is a security or financial instrument, confirm the position with SECP or SBP alongside PVARA, given the Act's cross-regulator coordination language

Issuers exploring an Asset-Referenced Token as part of their [regulatory licensing](https://www.coinconnect.site/regulatory-licensing) strategy should treat the section 32(2) backing rule as a design constraint to build around from day one, not a compliance detail to resolve after the token's structure is already fixed.

## Related reading

- [Asset-Referenced Token Issuance Under PVARA: Gold 2026](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-art-tokenized-gold-issuance-33)
- [Stablecoin Issuance Under PVARA: Reserve Rules 2026](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-frt-stablecoin-issuance-32)
- [PVARA Custody License: Safeguard Customer Crypto 2026](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-custody-license-safeguarding-customer-assets-25)

## About this analysis

This analysis was prepared by the CoinConnect research desk from the Virtual Assets Act, 2026, read as published. Where practice is not yet settled or guidance has not been issued, that is stated in the text above.

Regulatory positions change and specific requirements should be verified against the current position published by the relevant authority before you act on them. This is information and analysis, not legal advice, and it does not create an advisory relationship. Take professional advice on your own circumstances.

## Flags for Malik

- The "why does the Act ban Virtual Asset backing" section explains the rationale by reference to well-known market failures generally, not to anything the Act itself states — clearly framed as background reasoning, not a statutory claim, but worth checking the framing reads as analysis rather than fact.
- The cross-reference to section 53's algorithmic token ban as a related but separate restriction is accurate to the source text but worth a second look to confirm it doesn't overstate the connection between the two provisions.
- No Regulations under section 32(1)(a) or 32(3) existed in the source documents, so custody mechanics and any asset-category restrictions are described as pending.
