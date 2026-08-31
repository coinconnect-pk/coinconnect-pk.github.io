---
layout: post
title: "Can a VASP Lend or Pledge Customer Crypto in Pakistan?"
date: 2026-01-01 09:00:00 +0500
categories: [Compliance]
author: "Malik Abbas"
description: "Section 24(4) of the Virtual Assets Act 2026 bans rehypothecation of customer assets by default. Here is the rule, the consent exception, and its limits."
---

Rehypothecation — a firm reusing a customer's assets for its own purposes, such as [lending](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-lending-borrowing-license-30) them out, pledging them as collateral, or using them to back the firm's own trading — is one of the failure patterns behind the biggest collapses in crypto history. Customers believed their holdings were sitting safely with the platform; in fact the platform had put those holdings to work elsewhere, and when the trade went wrong, the customer's assets went with it.

Pakistan's [Virtual Assets Act](https://blog.coinconnect.site/pakistans-virtual-assets-act-2026-the-complete-guide/), 2026 addresses this directly. Section 24(4) prohibits a Licensee from rehypothecating, lending, pledging or otherwise encumbering [Customer Assets](https://www.coinconnect.site/blog/3/customer-assets-definition-pvara-pakistan-62) — but the prohibition is not absolute. This article sets out exactly what the rule bans, the narrow consent exception that survives it, and what a compliant consent process looks like under the Act as passed.

## What does section 24(4) of the Virtual Assets Act 2026 say?

Section 24(4) prohibits a Licensee from rehypothecating, lending, pledging, or otherwise encumbering a customer's virtual assets or fiat balances, unless the customer has given explicit, informed and revocable written consent to that specific use. The default position is a ban; consent is the only route around it.

The provision reads:

> A Licensee shall not rehypothecate, lend, pledge, or otherwise encumber Customer Assets, whether Virtual Assets or fiat balances, without the customer's explicit, informed, and revocable written consent.

Four things stand out in that sentence. First, the list of prohibited acts is broad and deliberately non-exhaustive — "rehypothecate, lend, pledge, or otherwise encumber" — so a Licensee cannot escape the rule by structuring a novel arrangement that achieves the same economic effect through different documentation. Second, the prohibition covers both Virtual Assets and fiat balances, so a customer's cash sitting with the Licensee is protected on the same terms as their crypto holdings. Third, the exception requires consent that is explicit, informed and revocable — three separate qualifying words, each doing distinct work. Fourth, the consent must be in writing.

"Customer Assets" carries the definition set out in section 3(1)(vii): virtual assets and fiat currency belonging to a customer that a Licensee holds, safeguards, or otherwise has [custody](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-custody-license-safeguarding-customer-assets-25) or control over on the customer's behalf, excluding assets the Licensee owns itself.

## What counts as rehypothecation, lending, pledging or encumbering?

Rehypothecation is the practice of a custodian or intermediary reusing an asset that was deposited with it for safekeeping, typically as collateral for the intermediary's own borrowing or trading. Lending, in this context, means the Licensee making a customer's assets available to a third party under an obligation to return equivalent assets later. Pledging means putting a customer's assets up as security for the Licensee's own obligation. "Otherwise encumber" is a catch-all covering any arrangement that creates a claim, lien or restriction over a customer's assets in favour of a party other than the customer.

Read against [Schedule I](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-license-categories-explained-23) of the Act, this maps closely onto the boundary between two different licensed services. Category 3, Custody and Administration Services, means the safekeeping or administration of Virtual Assets or private keys "on behalf of customers and pursuant to their instructions" — an activity built on the assumption that the asset stays the customer's and is not put to other use. Category 5, [Lending and Borrowing Services](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-lending-borrowing-license-30), by contrast, is defined as the facilitation, arrangement, intermediation or direct provision of lending arrangements where lenders transfer virtual assets to borrowers under a contractual obligation to return equivalent assets. Section 24(4) is the rule that stops a custody arrangement quietly turning into a lending arrangement without the customer's knowledge and consent.

## What makes consent "explicit, informed and revocable"?

Our reading is that each of the three qualifying words rules out a specific way that consent is sometimes engineered to look real without actually being real.

- **Explicit** rules out consent implied from silence, from a customer simply continuing to use the platform, or from a pre-ticked box. It requires an affirmative act by the customer specifically directed at authorising the use in question.
- **Informed** rules out consent obtained without the customer understanding what they are agreeing to. A customer cannot meaningfully consent to a risk they were not told about — at minimum, this should mean disclosure of what the assets will be used for, what happens if the counterparty in a lending or pledging arrangement defaults, and how the arrangement affects the customer's position if the Licensee itself becomes insolvent.
- **Revocable** rules out consent that, once given, locks the customer in permanently. The customer must be able to withdraw consent going forward, which in turn means the Licensee needs an operational process for unwinding or ceasing the encumbrance once consent is withdrawn, not just a legal acknowledgement that revocation is theoretically possible.

The Act does not prescribe a specific consent form or disclosure template for section 24(4), and no such standard had been published in Regulations at the time of writing. Where guidance has not been issued, the safer course for a Licensee is to design the consent process to withstand each of the three tests independently, rather than to rely on a single blanket clause buried in standard terms of service.

## Is bundling consent into the general terms of service enough?

This is not answered directly in the Act, and our reading is that it is genuinely ambiguous on the statutory text alone. A strong argument exists that consent buried in lengthy standard terms — accepted as a condition of opening an account, rather than sought for the specific use — fails the "explicit" and "informed" limbs, because the customer has not made an affirmative, understanding choice about that particular use of their assets. An equally available reading is that the Act sets no formal separation requirement, so long as the terms clearly and specifically describe the use and the customer affirmatively accepts them.

Given that ambiguity, and given that section 24(3) separately imposes a fiduciary duty on a Licensee to act honestly, fairly and in the best interests of its customers, the more defensible operational choice is a standalone, specific consent mechanism — separate from general account terms, naming the exact use, and giving the customer a clear mechanism to say no or later withdraw. A firm that treats a bundled clause as sufficient is taking on interpretive risk that a specific, freestanding consent flow avoids.

## How does section 24(4) interact with segregation and the insolvency ring-fence?

Sections 24(1) and 24(2) work alongside 24(4) to protect customer holdings on three separate fronts. Section 24(1) requires Customer Assets to be held in segregated accounts, separate from the Licensee's own assets. Section 24(2) provides that, notwithstanding any other law, Customer Assets do not form part of the Licensee's estate on insolvency or liquidation. Section 24(4) then closes the gap those two provisions leave open on their own: segregation and the insolvency ring-fence protect assets that are sitting still, but they do nothing to stop a firm actively putting segregated assets to work elsewhere before insolvency occurs. The rehypothecation ban is what keeps segregated assets segregated in substance, not just in bookkeeping, unless the customer has knowingly agreed otherwise.

This is also why proof-of-reserves matters here. Section 27(1) requires a Licensee to furnish cryptographic proof-of-reserves, reconciled against customer liabilities, at prescribed intervals, and section 27(2) requires an annual audit by a firm of Chartered Accountants that verifies the section 24 segregation. A Licensee that has rehypothecated assets without valid consent would, in principle, show up in that reconciliation as a shortfall between what customers are owed and what the firm actually holds on their behalf — which is precisely the audit trail regulators use to detect this kind of failure in other jurisdictions.

## What are the consequences of breaching section 24(4)?

Breach of section 24(4) is a contravention of the Act and falls within the Authority's general enforcement powers under Chapter 10, rather than carrying its own bespoke penalty in the text. Section 59(1) allows the Authority to impose a written reprimand or public censure, a directive to cease or remedy the contravention, a financial penalty up to the prescribed maximum, suspension or revocation of the licence, or disqualification of individuals from holding office in a Licensee. Section 59(4) sets a general fine ceiling of up to twenty-five million rupees for a contravention of the Act.

Section 23(1)(a) separately lists contravention of any provision of the Act as grounds on which the Authority may vary, suspend or revoke a licence, following written notice and an opportunity to be heard. Where unauthorised use of Customer Assets caused actual loss, section 59(5) allows a court to order restitution, disgorgement of profits, or other relief it considers appropriate — a route distinct from, and additional to, the Authority's own administrative sanctions. A Licensee that disagrees with the Authority's finding may appeal to the Virtual Assets Appellate Tribunal within thirty days under section 63.

## How should a Licensee design its systems around section 24(4)?

The rule is straightforward to state and harder to operationalise, because it requires the firm's technology and its legal documentation to agree with each other. A wallet architecture that physically pools customer and firm assets makes the section 24(1) segregation duty difficult to evidence in the first place, which in turn makes it harder to prove that no unauthorised encumbrance under section 24(4) has occurred.

Points worth building into a [custody](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-custody-license-safeguarding-customer-assets-25) and product design process:

- keep any product that lends, stakes for yield, or otherwise puts customer assets to work legally and operationally distinct from pure custody, so that consent is tied to a specific, named product rather than assumed across the account
- log consent at the level of the individual customer and the individual use, with a timestamped record capable of being produced to the Authority or an auditor
- build a working revocation path — not just a legal right to revoke, but an operational process for unwinding the customer's position when they do
- align internal risk and finance teams with compliance on this rule specifically, since the commercial incentive to use idle customer balances for the firm's own liquidity is exactly the incentive section 24(4) exists to block
- treat any [lending](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-lending-borrowing-license-30) product built on customer assets as requiring its own licensing analysis under Schedule I, not merely a consent clause added to an existing custody service

Firms still deciding their [licensing](https://www.coinconnect.site/pvara-guide) scope should treat section 24(4) as a design constraint from day one, not a compliance patch applied after the product is built.

## Related reading

- [PVARA Exchange License: Capital, Rules & Obligations 2026](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-exchange-license-requirements-capital-obligations-24)

## About this analysis

This analysis was prepared by the CoinConnect research desk from the Virtual Assets Act, 2026, read as published. Where practice is not yet settled or guidance has not been issued, that is stated in the text above.

Regulatory positions change and specific requirements should be verified against the current position published by the relevant authority before you act on them. This is information and analysis, not legal advice, and it does not create an advisory relationship. Take professional advice on your own circumstances.

## Flags for Malik

- The "is bundling consent into general terms enough" section is explicitly flagged in the article as ambiguous — the Act genuinely doesn't answer it, and I've given the more conservative reading as our recommended operational position rather than presenting it as settled law. Worth checking that framing matches how you want to advise clients.
- No Regulations under s.24(4) were in the source documents, so the "what makes consent explicit/informed/revocable" breakdown is my own textual analysis of the three words, not a citation to a defined standard. Flagged in the text as "our reading."
