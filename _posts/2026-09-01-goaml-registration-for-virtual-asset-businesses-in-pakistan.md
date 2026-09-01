---
layout: post
title: "goAML Registration for Virtual Asset Businesses in Pakistan"
date: 2026-09-01 18:27:02 +0500
categories: [Compliance]
author: "Malik Abbas"
description: "Regulation 11.4–11.6 of the NOC Regulations sets when a foreign VASP registers on goAML, and when the role passes to the licensed local entity."
---

[goAML](https://www.coinconnect.site/blog/coinconnect-insights-1/fmu-goaml-vasp-pakistan-17) is the Financial Monitoring Unit's ("FMU") reporting platform, and registration on it is not a one-off event for a Pakistan-facing [virtual asset](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-license-pakistan-complete-guide-22) business. Regulations 11.4 to 11.6 of [PVARA](https://www.coinconnect.site/pvara-guide)'s [No Objection Certificate](https://www.coinconnect.site/regulatory-licensing) Regulations 2025 describe a role that moves from a foreign applicant to a locally licensed entity as the business progresses through Pakistan's [licensing stages](https://www.coinconnect.site/pvara-guide).

This article sets out what goAML registration is, who is required to register at each stage, and the technical readiness standard the Regulations attach to it.

## What is goAML, and why does a virtual asset business need to register on it?

goAML is the reporting platform operated by Pakistan's [Financial Monitoring Unit](https://fmu.gov.pk), the government body that receives suspicious transaction reports from regulated entities. Regulation 2.2 of the NOC Regulations confirms that PVARA's issuance of a No-Objection Certificate ("NOC") constitutes, among other things, "approval for the Applicant's [AML](https://www.coinconnect.site/blog/3/fit-and-proper-aml-pvara-mistakes-54) Registration on the goAML portal." goAML registration is therefore the mechanism through which a [virtual asset service provider](https://www.coinconnect.site/blog/coinconnect-insights-1/vasp-license-pakistan-3) ("VASP") becomes a recognised reporting entity for [anti-money laundering](https://www.coinconnect.site/blog/3/fit-and-proper-aml-pvara-mistakes-54) purposes, distinct from the NOC or licence itself.

## Who registers on goAML first — the foreign entity or the Pakistan company?

The foreign entity, initially. Regulation 11.4 states:

> "Following issuance of NOC by the Authority, the foreign Applicant (the applicants whose foreign chapter is already providing VASP services in Pakistan) shall register on the FMU goAML platform as the reporting entity for AML-Registered Services, unless otherwise directed by FMU or the Federal Government."

Registration happens after the NOC issues, not before, and the entity that registers is the foreign chapter already active in Pakistan — the same body applying for the NOC — rather than the future local company that has not yet been incorporated. The Regulations do carve out an exception: FMU or the Federal Government may direct otherwise, though neither the NOC Regulations nor the other source documents reviewed describe what circumstances would trigger a different direction.

## When does the newly incorporated local entity take over as the reporting entity?

Once it holds a licence, not simply once it exists. Regulation 11.5 sets the handover point:

> "Once the Applicant incorporates its local entity in Pakistan, the local entity after being granted the license shall assume the role of reporting entity on go-AML and must maintain active reporting credentials at all times."

This creates a three-stage progression for who is registered on goAML, matching the wider NOC-to-licence pathway:

| Stage | Reporting entity on goAML | Governed by |
|---|---|---|
| Post-NOC, pre-incorporation | Foreign applicant / foreign chapter | Regulation 11.4 |
| Post-incorporation, pre-licence | No stated change — foreign entity remains reporting entity | Regulations 11.4–11.5 (by omission) |
| Post-licence | Local licensed entity | Regulation 11.5 |

The Regulations state clearly what happens at the first and third stages. They do not directly address the middle stage — a company that has incorporated in Pakistan but has not yet been granted a full licence. Our reading is that the foreign entity continues as the reporting entity through that middle stage, since Regulation 11.5 ties the handover specifically to the grant of the licence, not to [incorporation](https://www.coinconnect.site/corporate-setup) alone, but this is inference rather than an express statement in the text.

## What does "maintain active reporting credentials at all times" actually require?

The phrase appears once, in Regulation 11.5, without further definition. Read plainly, it means the local entity's goAML account cannot lapse, go dormant, or be left unmonitored once it becomes the reporting entity — reporting access has to remain live and usable on an ongoing basis, not merely obtained once and left inactive. The Regulations do not specify a renewal cycle, a minimum login frequency, or a technical uptime standard for this obligation, so an entity relying on it should build internal monitoring of its own credential status rather than assume the platform will flag an issue.

## What technical readiness does PVARA expect at the point of goAML registration?

Regulation 11.6 sets a readiness test that applies once registration happens, not a future aspiration:

> "The Applicant shall demonstrate technical readiness to file STRs and CTRs immediately upon goAML registration."

"Immediately upon" leaves no grace period in the text — the applicant is expected to be able to file [Suspicious Transaction Reports](https://www.coinconnect.site/regulatory-licensing) ("STRs") and Currency Transaction Reports ("CTRs") as soon as the goAML account exists, not to build that capability afterwards. This connects directly to Regulation 11.1, which requires monitoring systems capable of detecting suspicious or unusual activity "in real time or near real time" — a system built to that standard should, in principle, already be capable of generating the reports Regulation 11.6 requires the applicant to file on registration.

Form A4, PVARA's AML/CFT Framework Submission Statement, asks the Chief Executive Officer and Money Laundering Reporting Officer ("MLRO") to jointly confirm that the applicant has established "technical capability for STR/CTR filing through the goAML platform" as one of its operational readiness confirmations — the same standard Regulation 11.6 sets, restated as a signed declaration at the point of application.

## What should an applicant prepare before goAML registration happens?

Three things follow directly from Regulations 11.4 to 11.6:

- **Confirm which entity registers first.** The foreign chapter registers under Regulation 11.4, not the not-yet-incorporated local company — an applicant should not assume the Pakistan entity can or should register early.
- **Build STR/CTR filing capability before, not after, registration.** Regulation 11.6's "immediately upon" standard means the case management and escalation workflow — described in Form A1's Section 7 on FMU compliance — needs to be operational at the point registration is granted, not scheduled as a post-registration project.
- **Plan the credential handover for licensing day.** Since Regulation 11.5 ties the reporting-entity handover to the grant of the full licence, the transfer of active goAML credentials from the foreign chapter to the local entity should be mapped as a defined step in the [licensing process](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-license-pakistan-complete-guide-22), not left until the licence is actually issued.

Applicants unclear on which stage of this sequence their business currently sits in should treat that ambiguity as a compliance risk in its own right — a lapsed or misassigned goAML registration sits close to the "systemic or material AML/CFT failures" ground for [NOC revocation](https://www.coinconnect.site/blog/3/pvara-application-rejected-36) under Regulation 19.1(d).

## Does goAML registration replace the need for a full VASP licence?

No. Regulation 2.2 is explicit that AML Registration and the services it opens up are a bridge, not a destination — an applicant granted AML Registration may provide the four AML-Registered Services "prior to obtaining a license under Section 17, unless otherwise agreed with PVARA." Under Regulation 18.1(f), a registered applicant must "apply for and progress diligently toward a full VASP License within the time period required by the Authority." goAML registration establishes reporting capability for a defined interim window; it does not substitute for the licensing application Regulation 15.3(c) requires within three months of the licensing regulations being issued. An applicant that treats AML Registration as the finish line, rather than as one requirement on the way to a full licence, risks the revocation ground in Regulation 19.1(e) — failure to apply for or progress toward a full licence within the prescribed period.

## About this analysis

This analysis was prepared by the CoinConnect research desk from PVARA's No Objection Certificate Regulations 2025 — principally Regulations 2.2, 11.1 and 11.4 to 11.6 — read alongside Form A1 and Form A4 at Annex A. Where a provision is silent, as with the reporting-entity status of a company that has incorporated but not yet been licensed, that gap is stated in the text above rather than filled with assumption.

Regulatory positions change and specific requirements should be verified against the current position published by the relevant authority before you act on them. This is information and analysis, not legal advice, and it does not create an advisory relationship. Take professional advice on your own circumstances.
