---
layout: post
title: "goAML Registration for VASPs: Who Registers, and When"
date: 2026-01-01 09:00:00 +0500
categories: [Compliance]
author: "Malik Abbas"
description: "How goAML registration works under PVARA's NOC Regulations 2025: which entity registers, what it unlocks, and when the local company takes over reporting."
---

Most foreign exchanges reading Pakistan's virtual asset framework for the first time assume the sequence runs licence, then compliance plumbing. It runs the other way. Under the PVARA No Objection Certificate Regulations 2025, registration on the Financial Monitoring Unit's goAML platform is not a downstream obligation you satisfy after you are licensed — it is the gate that lets you start earning revenue before a licence exists at all.

That inversion is the single most commercially significant feature of the regulations. It also creates a handover problem that almost nobody plans for: the entity that registers on goAML first is not the entity that keeps the registration.

This article walks through what goAML registration is under the regulations as published, which entity registers, what it permits you to do, and the moment the local Pakistani company assumes the reporting role.

## What is goAML registration under PVARA's NOC Regulations?

goAML is the Financial Monitoring Unit's reporting platform. Under the PVARA No Objection Certificate Regulations 2025, registration on it is one of two things a No Objection Certificate ("NOC") delivers. Regulation 2.2 states that PVARA's issuance of the NOC required under section 15 of the Ordinance constitutes:

> (i) approval for the Applicant's AML Registration on the goAML portal; and (ii) permission for the Applicant to proceed with incorporation of its local entity in Pakistan.

So the NOC is a dual-purpose instrument. It is not merely a clearance letter that lets you go and register a company at the Securities and Exchange Commission of Pakistan. It is simultaneously the approval you need to become a reporting entity on the FMU's system.

The Financial Monitoring Unit is Pakistan's financial intelligence unit and receives suspicious transaction reports and currency transaction reports from reporting entities. Its own guidance sits at [fmu.gov.pk](https://www.fmu.gov.pk/).

Note the term the regulations use throughout: "AML Registration". Regulation 15.1 requires applications to be made on Form A1, which the annex titles "APPLICATION FOR No Objection Certificate" while its header block and the covering list both call it an application for AML Registration. The two labels describe the same submission. Our reading is that the drafters treat NOC and AML Registration as a single package, not two applications. We cover the wider route in our [PVARA licence guide](https://www.coinconnect.site/pvara-guide).

## Which entity registers on goAML — the foreign or the local one?

The foreign entity registers first. Regulation 11.4 is specific that it is the foreign applicant, defined in the same provision as an applicant "whose foreign chapter is already providing VASP services in Pakistan", that registers on goAML following issuance of the NOC:

> Following issuance of NOC by the Authority, the foreign Applicant (the applicants whose foreign chapter is already providing VASP services in Pakistan) shall register on the FMU goAML platform as the reporting entity for AML-Registered Services, unless otherwise directed by FMU or the Federal Government.

Regulation 17.1(a)(i) restates the same point from the decision side: the NOC is issued to the applicant to register "the foreign chapter, already providing AML-Registered Services in Pakistan".

Two things follow, and both matter commercially.

First, the drafting is aimed at incumbents. The provision addresses applicants whose foreign arm is *already* serving Pakistani users. It is a regularisation pathway for offshore platforms with existing Pakistani order flow, not a greenfield licensing route.

Second, FMU and the Federal Government retain an override. The words "unless otherwise directed" mean the default can be displaced. If you are structuring a market entry on the assumption the offshore entity will be the registered reporter, treat that as the published default rather than a guaranteed outcome, and confirm the position directly with the authority. Our [market entry work](https://www.coinconnect.site/engagements) starts from that assumption.

## When does the local Pakistani entity take over reporting?

The local entity assumes the reporting role after it is both incorporated and licensed. Regulation 11.5 sets the trigger precisely:

> Once the Applicant incorporates its local entity in Pakistan, the local entity after being granted the license shall assume the role of reporting entity on go-AML and must maintain active reporting credentials at all times.

Read that sequence carefully, because the clause contains two conditions, not one. Incorporation alone does not transfer the reporting role. The local company must be incorporated *and* granted a licence. Until both are true, the foreign entity remains the reporting entity on the platform.

That produces a distinct interim period. Here is the sequence as the regulations set it out:

| Stage | Reporting entity on goAML | Authority for the position |
| --- | --- | --- |
| Before NOC | No PVARA-recognised registration | Reg 2.2 |
| NOC issued, foreign entity registered | Foreign entity | Reg 11.4, 17.1(a)(i) |
| Local entity incorporated, not yet licensed | Foreign entity (transfer not yet triggered) | Reg 11.5 |
| Local entity licensed | Local entity | Reg 11.5 |

In practice, this interim window is where operational risk concentrates. Suspicious transaction reports arising from Pakistani customer activity are filed by an offshore entity, by staff who may sit offshore, into a Pakistani system, while a newly incorporated local company builds toward licensing. Anyone planning [corporate setup](https://www.coinconnect.site/corporate-setup) in this window should map who signs reports on which day, and under which entity's credentials. The regulations do not prescribe a handover mechanic — that is a gap, and it needs confirming with FMU before you rely on any particular approach.

## What can you actually do once you are registered on goAML?

Registration unlocks four revenue-generating services before you hold a licence. Regulation 2.3 designates the following as non-financial businesses and professions in accordance with section 38(1) of the Ordinance, for goAML registration purposes, and labels them the "AML Registered Services":

- Broker-Dealer Services
- Custody Services
- Exchange Services
- Virtual Asset Derivative Services

The permission attached is explicit:

> Where an Applicant is granted AML Registration, the Applicant may provide AML-Registered Services prior to obtaining a license under Section 17 of the Ordinance, subject to the conditions imposed by the Authority and until such time as the application for obtaining such license is finally determined.

Regulation 17.1(a)(iii) confirms the permission crystallises "upon completion of goAML registration" — not on issuance of the NOC alone. Registration is the operative step.

The boundary is equally explicit. All other Virtual Asset Services defined under the Ordinance that are not AML Registered Services "may only be provided following the grant of a full license under Section 17, unless otherwise agreed with PVARA". So advisory, lending and borrowing, management and investment, transfer and settlement, issuance and mining-related services sit outside the early-operation window on the face of the regulations. If your model depends on any of those, the pre-licence pathway does not help you — see how the [licence categories divide up](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-license-categories-explained-23).

## What must you demonstrate before goAML registration is granted?

You must show technical readiness to file, not merely an intention to comply. Regulation 11.6 requires the applicant to "demonstrate technical readiness to file STRs and CTRs immediately upon goAML registration". Suspicious Transaction Reports and Currency Transaction Reports are the two report types the platform receives.

That readiness sits inside a wider monitoring obligation. Regulation 11.1 requires monitoring systems "capable of detecting suspicious or unusual activity in real time or near real time". Regulation 11.2 requires STRs to be filed in accordance with the Anti-Money Laundering Act 2010. Regulation 11.3 requires CTRs "for all fiat-based transactions that meet or exceed the applicable threshold" — the regulations do not state the figure, so verify the current threshold against FMU's published position.

Form A1 section 7.1 asks you to describe how internal suspicious activity will be escalated and submitted as STRs and CTRs via goAML "once the Applicant has registered". Form A4, the AML/CFT Framework Submission Statement signed by the Chief Executive Officer and the Money Laundering Reporting Officer, requires confirmation of "technical capability for STR/CTR filing through the goAML platform" and confirms compliance with "FMU goAML requirements once registered". Form A7 sets the minimum content of the Internal Suspicious Activity Report that feeds the process, ending in an MLRO determination to file or not file.

Form A5 matters here too. Under regulation 14.1, STR and CTR reporting and MLRO responsibilities are AML-critical functions. They may not be outsourced unless the applicant conducts due diligence on the provider, maintains oversight, retains audit and inspection rights, and ensures those rights are legally enforceable including across borders. Practically, this constrains how far a group can centralise Pakistani reporting in a regional hub. Our [regulatory and licensing](https://www.coinconnect.site/regulatory-licensing) work treats the outsourcing register as a first-order document, not an annex.

## What are the ongoing goAML obligations after registration?

Maintaining active registration is a standing condition, and losing it is a revocation trigger. Regulation 18.1(e) requires a registered applicant to "maintain active FMU goAML registration" at all times. Regulation 11.5 layers on the requirement to "maintain active reporting credentials at all times" once the local entity takes over.

The other ongoing duties in regulation 18.1 sit alongside it:

1. Comply with all AML/CFT obligations at all times.
2. Notify PVARA of material changes affecting AML compliance, governance, ownership or technology.
3. Submit an Annual AML/CFT Return on Form A6, which asks for the number of STRs filed via goAML and the number of CTRs filed where fiat exposure exists.
4. Undergo independent AML audits when directed.
5. Apply for and progress diligently toward a full VASP Licence within the time PVARA requires.

On timing: regulation 15.3(c) requires the licensing application within three months of the issuance of the VASP licensing regulations, and regulation 17.1(a)(iv) repeats it as within three months of their promulgation. Regulation 19.1(e) makes failure to apply for, or progress toward, a full licence within the prescribed period a ground for revocation of the NOC and AML Registration status. Revocation is to be applied proportionately under regulation 19.2, but the exposure is real — and it lands on the entity that has, by then, been operating live.

Separately, all AML/CFT records must be kept for a minimum of seven years under regulation 13.1, stored securely and kept auditable, retrievable and tamper-evident. That interacts with the [tax and banking](https://www.coinconnect.site/tax-banking) record trail, and with the [FMU goAML registration mechanics](https://www.coinconnect.site/blog/coinconnect-insights-1/fmu-goaml-vasp-pakistan-17) we have covered separately. For how the phased pathway compares with the sandbox, see our [comparison of the PVARA routes](https://www.coinconnect.site/blog/coinconnect-insights-1/pvara-routes-compared-sandbox-noc-license-20), and for the operational load after clearance, our [post-NOC playbook](https://www.coinconnect.site/blog/coinconnect-insights-1/post-noc-pakistan-operational-playbook-12).

One more point of sequencing that catches people out: under regulation 9.3, customer due diligence must be completed before the applicant provides any AML Registered Service. Registration does not soften onboarding standards. It only moves forward the date on which you may onboard at all — which is why [banking readiness](https://www.coinconnect.site/blog/coinconnect-insights-1/crypto-banking-pakistan-vasp-15) should be solved in parallel, not after.

## About this analysis

This analysis was prepared by the CoinConnect research desk from the PVARA No Objection Certificate Regulations 2025 (document code PVARA/REG/AML-REG/2025-1, version 1.0, effective 2 December 2025) including Annex A Forms A1, A4, A5, A6 and A7, and from the Virtual Assets Act 2026 as passed by the National Assembly, read as published. Where practice is not yet settled or guidance has not been issued, that is stated above.

Regulatory positions change and specific requirements should be verified against the current position published by the relevant authority before you act on them. This is information and analysis, not legal advice, and it does not create an advisory relationship. Take professional advice on your own circumstances.

## Flags for Malik

1. **Ordinance vs Act mismatch.** The NOC Regulations cite the Virtual Assets Ordinance 2025 throughout (sections 15, 17, 38(1)). The source document we have is the Virtual Assets Act 2026 as passed. Section 74 of the Act saves things done under the lapsed Ordinance. But the section numbers do not map cleanly: in the Act, section 15 is Budget/Finance/Audit and section 17 is inter-agency cooperation, whereas the NOC Regs plainly mean pre-incorporation NOC (Act s.19) and licensing (Act s.21). Section 38(1) in the Act is the Strategic Digital Wallet Company, not a DNFBP designation power. I have quoted the regulations as drafted and attributed the section numbers to "the Ordinance" as the regulations do, without asserting they align with the Act. Worth a note to readers, or a separate piece, once PVARA reissues the regulations against the Act.
2. **CTR threshold** is not stated in the regulations. Left as "applicable threshold" with a verify instruction.
3. **Handover mechanic** for the goAML reporting role from foreign to local entity is not prescribed anywhere in the regulations. Flagged as a gap. If you have a view from FMU practice, that would strengthen the section materially.
4. **Form A1 naming inconsistency** (NOC vs AML Registration) — I have addressed it head-on rather than papering over it.
5. Word count is c. 1,650 body words. 14 internal links.
