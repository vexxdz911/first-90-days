# Strategy Guide — Scenario 118: "Sixty Days from a Signature"

*The First 90 Days — a fictional composite. Fictional composites only; no real person or case. General information about how these hearings work, not legal advice.*

> **Route verification:** this guide's winning route was graph-walked programmatically through `scenario-118.json` (every step is a legal choice; every `requiresFlags` gate satisfied by flags accumulated earlier on the route; cash never negative). Path and totals are printed at the end.

## 1. The win

**"Ending — Evaluated, and Heard"** — the full win.

The evaluation report is finished on day 56 of the federal 60, the IEP meeting is held with Darnell's written input attached and Khalil's own statement read aloud, and at the December 17 permanency hearing the court **finds the evaluation timely under 34 C.F.R. § 300.301(c)(1)**, credits the services to the case plan, and **orders the agency to report measurable progress at the next review**. Functioning stops being something a discipline file describes and becomes something measured services address. The partials are labeled partial in the data, and they are partial here: a late evaluation that still helps (late), and a discipline record standing where functioning should have been measured (no evaluation at all).

## 2. The route — graph-verified

1. **The School Chapter** ("The Referral That Slept") → **"Write the request. Your son's file gets a dated page with your name on it."** Sets `writtenRequest` — a signed, dated, delivered request to evaluate, not a conversation.
2. **Which Clock Starts When** → **"Ask for the framework in writing: trigger, consent date, deadline, report date."**
3. **The Permission Form** → **"Sign it today, and keep the date."** Sets `consentSigned` on Wednesday, October 14 — the signature that starts the 60-day clock (federal day 60: Sunday, December 13).
4. **The District Answers** → **"Write the input statement now, while the file is open."** Sets `parentInput` — a parent's written input page enters the evaluation file before testing begins.
5. **The Agency File** → **"Ask for the agency record in writing... Under § 3130.44(d)..."** Sets `recordsRequested` — verified: the district's referral was never transmitted.
6. **The Report Fork** (dispatcher: `writtenRequest` + `consentSigned`) → **"Call Ms. Ashby with the date, and attend the meeting on the fourteenth."** Report in hand December 10, day 57 of 60.
7. **The Evaluation Meeting** → **"Sign, attach your input statement, and ask for the signed IEP copy for the court packet."** Sets `packetFiled` — the evaluation reaches the dependency court as a document, not as the father's summary.
8. **What the Court Has** (dispatcher: `writtenRequest` + `consentSigned` + `packetFiled`) → **"Ask the court to find the evaluation timely, attach the services to the plan, and order progress reporting."**

**Programmatically walked path (16 nodes):** start → lawyer118 → consent_form → district_reply → visit_notes → records118 → testing_day2 → khalil_talk → waiting → ashby_clock → report_fork → report_ready → iep_meeting → hearing_prep → outcome118 → end_evaluated. **Ending cash: $141 of $150 left.**

## 3. Why this wins — the law

- **A parent starts the clock.** A request for an initial evaluation may be initiated by a parent of the child or by a public agency — 34 C.F.R. § 300.301(b). The request is the trigger; a referral an agency holds internally is not the parent's request and starts nothing for him.
- **The clock runs from consent, not from hope.** The initial evaluation must be conducted within 60 days of receiving parental consent for the evaluation, or within the state-established timeframe if the State has established one — 34 C.F.R. § 300.301(c)(1). *Both provisions newly verified from the eCFR text during this run; see `sources-batch-N.md`.* October 14 + 60 days = December 13; the report landed December 10. The guide states the federal 60-day frame and names the state-timeframe exception rather than inventing a Pennsylvania day count.
- **Functioning is a findings subject.** A permanency court reports the child's health and education record and reviews the child's safety, the continuing necessity and appropriateness of the placement, and the extent of compliance with the permanency plan — 42 Pa.C.S. § 6351(f)(1), (3). An evaluation and IEP in the record convert "functioning" from narrative into documents those findings can cite.
- **The record request is the spine.** Under 55 Pa. Code § 3130.44(d), a client or the client's attorney may obtain the agency record — which is how "the district never received the referral" stopped being an impression and became a verified file fact before the hearing.

## 4. The traps

- **The telephone season** (The Phone Loop → Waiting on a Clock That Never Started → Discipline Instead): two months of calls about a referral. Because no signed consent ever started a clock, there is no late evaluation to excuse — there is an *absent* one, and the hearing reads the suspension file instead.
- **A signature a week late** (The Report Is Late (partial)): the same evaluation, the same IEP, real help — and a permanency finding that says *initiated late*, credited to the father's hesitation rather than the agency's lost referral. Timeliness is a finding about the parent as much as about the district.
- **Signing the IEP and letting the packet ride**: if the signed IEP never reaches the court packet in citable form, the hearing still hears the father's account of a report instead of the report.

## 5. What no strategy controls

Whether Khalil qualifies for services under any particular category; the evaluator assigned and the quality of the testing; whether the district's staffing can deliver the IEP's minutes in a hard winter; how the behavior plan and the discipline code interact on a bad Tuesday; and what the next school year holds. The strategy controls the trigger, the consent date, the input page, and the packet — the paper that makes functioning a measured subject instead of a narrated one. It cannot control the measurement's result, and this guide does not pretend otherwise.
