---
layout: post
title: "Who Is an Issuer Under Pakistan's Virtual Assets Act?"
date: 2026-08-23 18:59:18 +0500
categories: [Licensing]
author: "Malik Abbas"
description: "The Act defines Issuer by control, not by involvement. An express carve-out protects marketers, brokers and developers who never touch supply or reserves."
---

"Issuer" is one of the few terms in the [Virtual Assets Act](https://blog.coinconnect.site/pakistans-virtual-assets-act-2026-the-complete-guide/), 2026 that comes with its own express carve-out. The legislature wrote a definition, then immediately wrote a paragraph explaining who the definition does not catch.

That structure tells you something. Somebody anticipated that a broad reading would sweep in every business that touches a token — the exchange listing it, the agency marketing it, the development shop maintaining the contract — and drafted against that outcome.

## What is an "Issuer" under the Act?

Section 3(1)(xiii) defines an Issuer as the legal Person that "originates or creates a [Virtual Asset](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-license-pakistan-complete-guide-22) and retains primary control over its initial supply, reserve assets (if any) or on-chain governance", may distribute it as part of an initial offering, and bears the ongoing obligations prescribed by the Authority.

The operative word is **control**. Creating a token is not sufficient on its own; the definition requires origination *and* retained primary control over at least one of three things.

Reading the provision carefully, the three control limbs are alternatives, not cumulative:

- **Initial supply** — control over how much exists and how it enters circulation
- **Reserve assets**, where there are any — control over the backing
- **On-chain governance** — control over how the protocol's rules change

A Person controlling any one of these, having originated the asset, falls inside the definition.

## Who is expressly NOT an Issuer?

The Explanation to section 3(1)(xiii) is unusually direct:

> "A Person is not an Issuer solely because it markets, advertises, promotes, facilitates secondary-Market trading (including third-party brokerage, distribution or exchange), or provides technical development or maintenance services without control over issuance, supply or reserve assets."

Five activities are named, and the qualifier at the end governs all of them: **without control over issuance, supply or reserve assets**.

| Activity | Issuer? |
|---|---|
| Marketing or advertising a token | No, on this ground alone |
| Promoting a token | No, on this ground alone |
| Facilitating secondary-market trading | No, on this ground alone |
| Third-party brokerage, distribution or exchange | No, on this ground alone |
| Technical development or maintenance | No, on this ground alone |
| Any of the above **plus** control over supply or reserves | Yes |

Note the word "solely". The Explanation does not immunise these businesses. It says the listed activity is not by itself enough. Add control, and the carve-out stops applying.

## Why does this distinction matter commercially?

Because issuer status brings a separate body of obligation, and because the carve-out defines the boundary of several ordinary crypto business models.

An exchange that lists a third-party token is facilitating secondary-market trading. On the face of the Explanation, that does not make it the issuer of that token — which matters, because otherwise every [exchange licence](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-exchange-license-requirements-capital-obligations-24) holder would inherit issuer obligations for every asset on its order book. That would be commercially impossible and the drafting avoids it.

The same logic protects three other common structures:

1. **Launchpads and distribution partners** that sell an issuer's token without controlling supply
2. **Marketing agencies** running campaigns for a foreign issuer
3. **Development shops** building or maintaining a contract for a client

Each is outside the definition on the stated ground — provided the control test is genuinely not met.

## Where does the carve-out stop protecting you?

At the point where commercial reality diverges from the paperwork. Three situations deserve care:

**Where the "developer" holds the keys.** A development shop that retains admin control over minting, or holds the upgrade key to a contract, has control over supply or governance regardless of what the services agreement calls the relationship. The Explanation asks what you control, not what your contract says you do.

**Where a distribution partner controls the float.** A distributor holding and releasing the initial supply on its own judgement is exercising control over initial supply.

**Where governance is nominal.** Where a token has on-chain governance in form but one party can pass any proposal in practice, the honest answer is that control has not moved.

The Act does not address these cases expressly, and we are not aware of published guidance on them. Our reading is that the control test is substantive rather than formal, because a test that could be satisfied by contract drafting alone would defeat the purpose of having one. That reading should be confirmed with the Authority before a business relies on it.

## What about a token with no reserve and no governance?

This is the gap worth noticing. The definition requires control over initial supply, reserve assets "(if any)" or on-chain governance.

The parenthetical concedes that some assets have no reserve. Where a token also has no meaningful on-chain governance, the only remaining limb is initial supply — which makes supply control the decisive question for a large category of ordinary tokens.

For anything that maintains a stable value against a currency, the analysis moves elsewhere: a [stablecoin](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-frt-stablecoin-issuance-32) engages the [Fiat-Referenced Token](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-frt-stablecoin-issuance-32) definition, and an [asset-referenced token](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-art-tokenized-gold-issuance-33) engages its own. Issuer status and token classification are separate questions and should be answered separately.

## What should a business do with this?

Work out honestly where control sits before deciding what you are.

- **Map control, not roles.** Who can mint? Who holds reserve assets? Who can change the protocol? The answers determine issuer status; job titles do not.
- **Do not rely on the carve-out where you hold keys.** Retained admin control is control.
- **Treat classification as a separate exercise.** Being an Issuer tells you who bears obligations; the token type tells you which ones.
- **Document the position before you launch.** If you conclude you are outside the definition, record why, against each limb of the test.

Where the model genuinely sits near the line, the [regulatory sandbox](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-sandbox-form-i-complete-walkthrough-2026-8) route exists precisely for products whose classification is unsettled — and testing under supervision is a better outcome than a confident answer that turns out to be wrong. Getting the analysis right at the [licence application](https://www.coinconnect.site/regulatory-licensing) stage is considerably cheaper than revisiting it after launch, which is why classification belongs early in any [market entry](https://www.coinconnect.site/launch-growth) sequence alongside [SECP registration](https://www.coinconnect.site/blog/coinconnect-insights-1/secp-crypto-company-registration-pakistan-16).

## How does issuer status connect to an initial offering?

Directly, and the Act treats the two as related but separate.

Section 3(1)(xiv) defines an "Initial Virtual Asset Offering" as a method of raising funds by an Issuer through the public offering of Virtual Assets in exchange for funds, other Virtual Assets, or anything of commercial value — subject to the limitations and disclosure requirements prescribed under the Act.

Two features of that definition matter commercially:

1. **It is keyed to the Issuer.** Only an Issuer conducts an Initial Virtual Asset Offering. If you are outside the Issuer definition, you are not conducting one, whatever the marketing calls it.
2. **Consideration is drawn widely.** "Funds or other Virtual Assets or anything of commercial value" is deliberately broad. Structuring a raise to take payment in tokens rather than currency does not move it outside the definition.

The definition also confirms that the Issuer definition is not merely descriptive. Section 3(1)(xiii) ends by saying the Issuer "bears the ongoing obligations as prescribed by the Authority", and section 3(1)(xiv) makes the offering itself "subject to the limitations and disclosure requirements Prescribed under this Act". Both defer the detail to Regulations.

Our reading is that the practical burden of issuer status will therefore be set largely outside the Act, in instruments not yet published at the time of writing. For a project planning a raise, that is the honest position: the category you fall into is knowable now from section 3(1)(xiii), but the obligations attaching to it are not yet fully knowable. Confirm the current position with the Authority before committing to an offering structure.

## About this analysis

This analysis was prepared by the CoinConnect research desk from the Virtual Assets Act, 2026 as passed by the National Assembly, read as published. Where practice is not yet settled or guidance has not been issued, that is stated in the text above.

Regulatory positions change and specific requirements should be verified against the current position published by the relevant authority before you act on them. This is information and analysis, not legal advice, and it does not create an advisory relationship. Take professional advice on your own circumstances.
