# Strategy Guide — Scenario 125: "Page Nine of the Chart"

*The First 90 Days — a fictional composite. Fictional composites only; no real person or case. General information about how these hearings work, not legal advice.*

> **Route verification:** this guide's winning route was graph-walked programmatically through `scenario-125.json` (every step is a legal choice; every `requiresFlags` gate satisfied by flags accumulated earlier on the route; cash never negative). Path and totals are printed at the end.

## 1. The win

**"Ending — The Whole Chart"** — the best outcome, labeled with its exact scope.

On June 25, 2027 — sixteen days after the hearing, well inside the 45-day decision window — the Secretary's designee issues the written decision: the indicated report is **inaccurate under 42 Pa.C.S. § 6341(c)(1)**, the bone survey is radiologically consistent with the metabolic explanation documented on the chart's own page nine, the agency did not carry its burden by substantial evidence under § 6341(c.2)(5), and the report is ordered **expunged under § 6341(c)**, with the ChildLine record amended and the dismissal entered in the dependency matter on the same evidence. The honest scope, stated in the data and here: this win is on the **indicated track**. The dependency case *continues* — Mateo remains at his grandmother's under supervision while the feeding plan and monitoring proceed — because dependency and the registry were always two cases wearing one family's name, and only one of them was about the past. Expungement still matters concretely: the clearances Bianca needs for work are no longer blocked by a finding the evidence never supported.

## 2. The route — graph-verified

1. **The First Question** ("Four Days Old in a Hospital") → **"Ask what the injury is, what caused it in their view, and what happens next — in that order."** Calm, specific, and on the record from hour one.
2. **The Record, From Day One** → **"The complete chart and the complete agency record, both in writing, tonight."** Sets `recordsRequested` — under § 3130.44(d) and the Act 119 chart right (§ 6341(a), as worded at the hearing-room door), the requests go out before any summary can harden into the case.
3. **The Paper Arrives** → **"Read it all, but mark page nine."** The chart contains its own correction: the hematology consult the reporting summary never mentioned. Sets `cpslEvidence` through the chart audit that follows.
4. **The Appeal** → **"Draft it as what it is: the case, in writing, with the chart attached."** Sets `appealBuilt` — filed April 14, day 2 of 90, with pagination, the consult highlighted, and the burden framed under § 6341(c.2)(5).
5. **Page Nine's Author** → **"Write the letter. Consultants answer letters; rumors answer nothing."** Sets `whitbyLetter` — Dr. Whitby confirms her consult, its date, and that no one from the agency ever contacted her.
6. **The Hearing** (June 9) → **"Open with the chart. Page nine first, then the summary, then the burden."**
7. **The Decision** (dispatcher: `cpslEvidence` + `whitbyLetter`) → the written decision expunges.

**Programmatically walked path (37 nodes):** start → what_happened → investigator → nursery_detail → samira_arrives → lawyer125 → er_resident → quashie → page_nine_rumor → kinship_paper → discharge → records125 → notice_day → chart_arrives → summary_vs_chart → phone_notes → appeal_choice → registry_letter → evidence_packet → investigator_notes → whitby_contact → samira_visit → dependency_track → second_pediatrician → workup_explainer → adjudication125 → workup_complete → gal125 → hearing_prep125 → ansel_whiteboard → agency_offer → hearing_eve → hearing_day125 → waiting_decision → reconsideration_prep → decision_day → end_whole_chart. **Ending cash: $121 of $140 left.**

## 3. Why this wins — the law

- **The appeal clock is 90 days, and the chart is the appellant's right.** A subject may appeal an indicated determination to the Secretary within 90 days of notice — 42 Pa.C.S. § 6341(a)(2) (holidays and the § 6341(g) mailing rule counted, as in prior batches) — and under Act 119 a party to the appeal may review the reports and evidence in the agency record, the reports and evidence language that lets the chart itself be the exhibit. Notice dated Monday, April 12, 2027 puts day 90 at Sunday, July 11, 2027 (machine-audited); Bianca filed on day 2.
- **The burden sits with the agency, at substantial evidence.** Act 119 (Senate Bill 1499, per prior batches' verified wording): on appeal, the agency bears the burden of proving the report's accuracy by substantial evidence — § 6341(c.2)(5) — and the hearing officer weighs the evidence the parties present under § 6341(c.2)(4). An appellant who arrives with the complete chart and the consult's author has not merely raised a doubt; she has made the agency's burden unmeetable on its own file.
- **Expungement follows inaccuracy.** Where it is determined the indicated report is inaccurate, it is amended or expunged — § 6341(a), (c) — and the written decision issues within 45 days of the hearing unless all parties agree to an extension — § 6341(c.3). Sixteen days is inside the window; the guide prints the window because the window is part of the win.
- **The dependency echo is a separate proof.** The dependency adjudication (May 20) proceeded on its own evidence, and the indicated hearing was never its substitute — the chart audit served both tracks because facts are portable, but the expungement's legal effect runs to the registry and the dependency dismissal follows from the evidence, not from administrative contagion. The guide states this precisely because overstating it ("expunged means the case closes") would be the kind of claim this project does not make.
- **The record requests are the spine.** § 3130.44(d) (agency record) and the Act 119 review right (chart) went out on day one and day seven; everything after — the audit, the packet, page nine's author — is downstream of paper demanded before summaries settled.

## 4. The traps

- **Sixteen Days, and the Next Door (partial)**: the complete record without Dr. Whitby. The agency *wins* the appeal on the paper — a decision inside the window, appeal rights to Commonwealth Court preserved — and the indicated report stands against Bianca's clearances while the next, slower, more expensive case is built. Partial precisely because the record was complete and the witness was the difference.
- **Two Pages**: fighting from the summary — the agency's two pages against a mother's character testimony. The burden never moves, because the chart that would have moved it was never demanded in writing; the appeal is denied and the dependency track hardens around a finding that the complete record contradicted from the start.
- **Taking the agency's "agreement to disagree"**: the offered trade — no contest at the dependency adjudication in exchange for softened language — would have surrendered the stronger track to settle the weaker wording. It appears in the route as a refused node, and the refusal is part of the win.

## 5. What no strategy controls

The medicine: whether the metabolic explanation is right is a question for hematologists, and the scenario is careful that the *burden*, not the mother's certainty, decides the appeal — a different chart, without page nine, loses this appeal on identical strategy. Whether the workup stays normal; whether a future injury, in a child with a real bone condition, restarts the same machinery with the same fear; the hearing officer assigned; and the dependency case, which continues at Samira's on its own facts and its own calendar. The strategy controls the record's completeness and the appeal's timing. It cannot control the biology, and this guide does not pretend otherwise.
