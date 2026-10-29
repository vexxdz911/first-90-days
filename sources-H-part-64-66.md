# SOURCES AND ALTERATIONS — PART H: Scenarios 64–66

*How "The First 90 Days" Scenarios 64–66 were built from the project's existing research, what was drawn from each source, what was changed, and what was deliberately withheld.*

**Status:** Draft documentation, for internal development and attorney review. Nothing here or in the scenarios is published or sent.

**Source rule applied:** Every scenario derives only from the project's existing research — published Pennsylvania Superior Court and Commonwealth Court opinions already used in this project, the official statutory text previously verified in this project, and documented system patterns stated as patterns. No private case, file, docket, or person from the development team's own orbit was used as source material, in any form; the private matters in the owner's orbit (Christine May, Annie Roth, Camden Ransing) are expressly excluded as sources.

**Alteration doctrine applied:** Each scenario is a composite. Procedural spines and testimony-textured beats come from the published sources; names, ages, counties, occupations, and identifying facts are changed, and beats from at least two sources or documented patterns are merged in every scenario, so that no real family maps onto any character. All character names were pre-cleared for this batch and no other characters are first-named in any scenario.

**Engine-flag note (all three scenarios):** The `removed` flag is deliberately **absent** from Scenarios 64–66, because no removal occurs inside any of these stories — in each scenario the child's placement predates the playable story (Scenario 64's placement is Monday, November 3, 2025, ten months before the story opens; Scenarios 65 and 66 open with placements already in being). Setting `removed` would fire the engine's 72-hour shelter-care banner falsely. The `recordsRequested` flag is set in all three scenarios, and on every winning route.

---

## SCENARIO 64 — "Fifteen Months of Paper" (42 nodes, 4 endings)

*A mother at month 10 of her daughter's placement builds the written record of two services that were ordered but not provided — a parenting/recovery program reached only after an 8-week waitlist at month 2, and a therapy referral sent to a provider whose intake had closed and re-sent six weeks later — ahead of the federal 15-of-22-months filing date.*

### Documented basis used (project research only)

1. **In the Interest of J.L.L., No. 1714 EDA 2023 (Pa. Super. 2024)** — previously used in this project for Scenario 3. *Beats/textures drawn:* the case-plan objective set (parenting classes, treatment, housing), the compliance texture of a parent whose progress is real but unevenly documented, and proof assembled from dated paper (pay stubs, attendance).
2. **In re Adoption of N.R.A. (Pa. Super. 2026)** — previously used in this project for Scenario 3. *Beats/textures drawn:* waitlist testimony — a parent describing, on the record, a service she could not enter because a list stood in front of it — compressed here from housing to a program waitlist and a closed therapy intake.
3. **In re T.D. (Pa. Super. 2008)** — previously used in this project for Scenario 3. *Beats/textures drawn:* the permanency-review framework, including the 15-of-22-months determination made on the record at review — the texture of the month-12 and month-14 review scenes and of the filing decision being documented, not dramatized.
4. **42 U.S.C. § 675(5)(E)** — the ASFA filing duty and its three documented exceptions, as previously verified in this project (Scenarios 1, 3, 24, 33): (i) the child is being cared for by a relative, (ii) a documented compelling reason that filing would not serve the child, or (iii) the agency has not provided services it identified as necessary for the child's safe return. Only exception (iii) is built here. Also used, as previously verified: counsel (42 Pa.C.S. § 6337; § 6332(a)) and record release on request (55 Pa. Code § 3130.44(d)).

### Alterations applied

The sources involve multi-year cases, multiple children, and contested termination or goal-change hearings. The composite compresses to one child (Amara, 5) and one parent (Katrina) whose own completions are finished and clean, so that the services record — not parental failure — carries the drama. The waitlist is re-costumed from housing testimony to a program waitlist at month 2; the therapy gap (a referral sent to a closed intake, re-sent six weeks later) is a composite of the referral-failure texture documented across the project's sources, not a fact from any one of them. All names (mother Katrina; daughter Amara; counsel Mr. Sandoval; worker Ms. Yoder), the county, the program, and all dialogue are invented.

### Dates audited

Placement: **Monday, November 3, 2025** (pre-story, stated in the opening node). Story opens at month 10: **Monday, August 31, 2026** (startDateISO). The ASFA date — placement + 15 calendar months — is **Wednesday, February 3, 2027**, computed in the generator by calendar-month addition and asserted in code; it is also dayOffset **156** from the start date (August 31, 2026 + 156 days = February 3, 2027, asserted), and the filing-decision node (`filing_day`) sits exactly on dayOffset 156 with its kicker recomputed and asserted as "Day 156 — Wednesday, February 3, 2027". Every other kicker and in-body date is computed from the start date by the same generator; the validator recomputed all kickers against the real calendar and extracted every in-body stated date (2 found: the placement date and the ASFA date), matching each against a computed node date or the ASFA date.

### Law used

42 U.S.C. § 675(5)(E) (filing duty and exceptions, worded as in v1); 42 Pa.C.S. § 6337 and § 6332(a) (counsel); 55 Pa. Code § 3130.44(d) (record release on request); dependency/TPR burden stated only as clear and convincing. No other authority is cited anywhere in the scenario, its script, or its guide (validator citation sweep).

### Deliberate withholdings

- **Reasonable-efforts-as-TPR-element was rejected and is not used** (per the withholding already recorded in `sources-and-alterations.md`: In re T.R.C. recounting the D.C.D./T.J.J.M. reversal). No scenario in this batch argues it, and Scenario 64 is explicit that the services exception is **not** a merits defense: it is record-dependent, it speaks only to the filing decision, and a petition, if filed, must still be proven by clear and convincing evidence at a hearing.
- **No TPR outcome is depicted anywhere.** The two "filed" endings stop at the filing document; no hearing, grounds, or disposition is shown or predicted.
- The assessment instrument is never named or characterized as AI/ML/predictive (validator sweep); this scenario in fact barely uses the scored-form mechanic, because its subject is the services chronology.

---

## SCENARIO 65 — "Two Plans" (38 nodes, 3 endings)

*Two separated parents, each a party with their own case plan and their own worker, discover that scheduling collisions (his Tuesday-evening group vs. her only Tuesday make-up visit slot; her Friday-morning screens vs. his Friday class check-in, one car between them) and file bleed (his missed screen summarized inside her review report; her misread visit note inside his file) are structural, and repair both in writing.*

### Documented basis used (project research only)

- **Two-plan / file-bleed as a composite of documented record-bound practice — stated as pattern, not holding.** The pattern basis is the discipline this project drew from **In re Adoption of A.P.C.-D. (Pa. Super. 2026)** (previously used in Scenarios 3 and 24): appellate courts are confined to the certified record and parse which findings the record actually supports. Scenario 65 transposes that discipline one level down: reviews are argued from reports, reports are written from files, and a line copied into the wrong parent's file does its work in the wrong parent's review. Multi-party cases with separate plans per parent, and summaries that describe a "household" instead of a party, are recurring documented practice patterns; the specific collisions, the missed screen, and the early-closing visit note are invented composites, not facts from any opinion.

### Alterations applied

The composite invents both parents (mother Trina, worker Ms. Whelan; father Curtis, worker Mr. Murdock) and their daughter (Hattie, 4), the employers, the car, the visit center, and all dialogue. The parents are written with dignity throughout and the marriage is never the problem: the conflict is assigned, explicitly and repeatedly, to the paperwork — two workers each reading one file, and copying that happens between desks. No source case's facts, family structure, or outcome is reproduced.

### Dates audited

Story opens **Monday, September 21, 2026** (startDateISO; weekday asserted in the generator). No placement date is stated in-game (placement is pre-story and undated by design, so no ASFA computation is implied); every kicker is computed from the start date by the generator and recomputed by the validator against the real calendar. No in-body calendar dates are stated (validator extraction: 0 found), so no stated date can be wrong.

### Law used

42 Pa.C.S. § 6337 (each party's own counsel); 55 Pa. Code § 3130.44(d) (each parent's own record, released on their own request — the scenario is careful that neither parent can request the other's file, which is why the winning route requires two requests). No other authority is cited (validator citation sweep). No burden of proof is stated or tested; no hearing decides anything.

### Deliberate withholdings

- No joint-counsel shortcut: the parents act jointly exactly once, in a single letter **through** their separate counsel, because the scenario teaches that two parties remain two parties even when they cooperate.
- No removal, adjudication, or termination event is depicted or sourced; the placement predates the story (see the engine-flag note above for why no `removed` flag is set).

---

## SCENARIO 66 — "The Discharge Summary" (40 nodes, 3 endings)

*A father in week 10 of a 12-week intensive outpatient program is discharged because his benefit's session cap is reached — an arithmetic discharge, not a failure discharge — while the agency's goal line ("complete IOP") is coded by its system as "goal not completed," ahead of a review and a three-week wait for a step-down program.*

### Documented basis used (project research only)

- **Early discharge / session-limit arithmetic as a documented practice pattern in published opinions' treatment discussions — stated as pattern, not holding.** The texture is the one this project drew from **In the Interest of J.L.L. (Pa. Super. 2024)** (previously used in Scenario 3): treatment engagement measured through attendance and provider paper, with a parent's progress and the system's description of that progress diverging in the record. Benefit session caps ending treatment episodes independently of clinical progress, discharge summaries as the document that carries a program's account of a parent into the agency file, and status coding that cannot represent the reason for a discharge are recurring patterns in those treatment discussions; no opinion in the project's research holds that such a coding must be corrected in any particular way, and the scenario claims no such holding — the correction succeeds, when it succeeds, because the review reads the file, not because a rule compels the outcome.

### Alterations applied

The composite invents the father (Hector), his son (Dario, 10), the worker (Ms. Nakamura), the program, the insurer, and all dialogue. The discharge reason (benefit limit), the three-week step-down wait, and the "goal: not completed" coding are composite pattern elements assembled for this scenario; they are not the facts of J.L.L. or of any other single case. The visit beat in which Dario asks when he comes home is written per design.md §7 — procedure and a sleeve held, no graphic content — and is original to this scenario.

### Dates audited

Story opens **Monday, October 5, 2026** (startDateISO; weekday asserted in the generator). The program's week count (week 10 of 12), the insurer's session cap, and the step-down's three-week wait are stated as durations, not calendar dates; every kicker is computed from the start date by the generator and recomputed by the validator against the real calendar. No in-body calendar dates are stated (validator extraction: 0 found).

### Law used

42 Pa.C.S. § 6337 (counsel); 55 Pa. Code § 3130.44(d) (record release on request). No other authority is cited (validator citation sweep). No burden of proof is stated or tested; no placement is decided.

### Deliberate withholdings

- The benefit cap is never framed as anyone's fault, and the insurer's appeal is filed "without illusion" — the scenario refuses to teach that an appeal of a benefit determination is a case strategy; its function in the story is documentary only.
- No treatment outcome is promised by the step-down enrollment: the win ending re-codes a goal on the record and continues the plan. It does not depict reunification, and its debrief labels it PARTIAL in so many words.
- The placement predates the story, so no `removed` flag is set (see the engine-flag note above).
