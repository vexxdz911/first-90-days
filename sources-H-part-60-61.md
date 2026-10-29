# SOURCES AND ALTERATIONS — Part H: Scenarios 60–61 (Hard tier)

*How "The First 90 Days" Scenarios 60–61 were built from the published public record and the project's existing research, what was drawn, what was changed, and the date arithmetic for every clock.*

**Status:** Draft documentation, for internal development and attorney review. Nothing here or in the scenarios is published or sent.

**Source rule applied:** Every scenario is a composite built **only** from the project's existing research: published Pennsylvania Superior Court and Commonwealth Court opinions already in the project library (see `sources-and-alterations.md` and the batch source files) and documented system patterns across many cases. No private case, file, docket, or person from the development team's own orbit was used as source material, in any form; the private cases in the owner's orbit were excluded absolutely, as sources and as models. Patterns are stated as patterns, never as holdings.

**Alteration doctrine applied:** Names, ages, family structures, services, and all dialogue are invented. Each scenario merges beats from at least two documented patterns, so no real family maps onto any character. The families are fictional composites: Marta and Silas (Scenario 60); Tanya and Cora (Scenario 61).

**Engine-flag note (both scenarios):** The `removed` flag is deliberately **absent** from both scenarios, because no removal occurs inside either story — in Scenario 60 Silas has been in foster care for eight months when the story opens (month 8 of the case), and in Scenario 61 Cora's placement likewise predates the story. Setting `removed` would fire the engine's 72-hour shelter-care banner falsely. The `recordsRequested` flag **is** set on every winning route in both scenarios: in each, the parent herself signs the written request under 55 Pa. Code § 3130.44(d).

**New law verified in this part: NONE.** Both scenarios use only the shared verified set: record release on request (55 Pa. Code § 3130.44(d)); the release's confidentiality limit (55 Pa. Code § 3130.44(f)), worded exactly as in Scenario 31; and counsel (42 Pa.C.S. § 6337). Scenario 61's guide — and only the guide, never the game — additionally discusses the ASFA 15-of-22 filing rule and its services exception (42 U.S.C. § 675(5)(E)) in Scenario 14's disciplined form: a record-dependent argument that speaks to the filing decision, with any termination still to be proven by clear and convincing evidence. No assessment is called AI, machine learning, or predictive anywhere in either scenario, its script, or its guide.

---

## SCENARIO 60 — "The New Worker" (28 nodes, 3 endings, Hard)

*A mother eight months into her son's placement gets a new caseworker. The incoming worker inherits a summary with two stale lines — a completed service listed as open, a passed screen listed as missed — and, because the file copy is a draft, re-orders an assessment she already completed.*

### Documented pattern basis

Worker turnover and file-driven continuity loss, as documented across the published opinions in the project library. The pattern, stated as a pattern: later readers of a case — a successor worker, a report writer, an appellate court — meet only the file, and the file's errors and omissions become the case they act on. Two library textures carry the pattern most directly, and both are already documented in `sources-and-alterations.md`:

1. **In re Adoption of A.P.C.-D., No. 1432 MDA 2025 (Pa. Super. 2026)** — an appellate court parsing, line by line, which findings the certified record actually supported. Drawn on here for the discipline behind the scenario's spine: a new reader of the case can act only on what the record contains, so a stale summary line is not a misunderstanding to be talked away but a text to be corrected in writing. (Cited in `sources-and-alterations.md`, Scenario 3 sources, item 4.)
2. **Mulholland v. Government of Berks County (3d Cir. 2013)** — the footnote texture, noted in `sources-and-alterations.md` (Scenario 2 sources, item 7): a caseworker testifying years later with no independent recollection of the investigation, testifying solely from the form. Drawn on here for the successor worker's posture: Mr. Wilkes is not careless and not a villain; he reads what the file gives him to read, exactly as the Mulholland footnote's witness could only read what the form gave her.

Supporting pattern texture, from the same library: the repeated appearance in published opinions of parents whose compliance was summarized at a level the underlying record did not support, and corrected — if at all — only when primary paper (certificates, sign-in sheets, dated letters) was put into the record. The scenario's two stale lines are invented instances of that documented shape, not any case's lines.

### Beats drawn

- The goodbye letter and the handoff summary as the new worker's only map (pattern basis above, item 1).
- The two stale lines surfacing conversationally at the first meeting — a completed parenting program listed as open; a passed screen listed as missed (invented instances of the documented summary-vs.-record gap).
- The re-ordered assessment whose sole defect is that the file copy is a draft (the form-as-record texture, item 2: an unsigned working copy cannot testify to a completion).
- The parent's own binder, kept in date order from month one, as the parallel file (documented pattern across the project library: primary paper outlasts summaries).
- The one-page written status letter with certificates sent in the new worker's first weeks (the orientation move: primary documents arriving before the summary sets).
- The record request under § 3130.44(d) surfacing the *draft* review report — template lines and all — while it is still correctable.
- The written correction, filed with attachments before the review, versus the same correction raised orally at a meeting (the library's recurring filed-vs.-spoken contrast).

### Alterations

All source matters involve different family structures, postures, and procedural stages (appeals, expunction hearings, termination trials). None of their facts is used. The composite is one mother (Marta), one son (Silas, 9), an outgoing worker (Ms. Renshaw), an incoming worker (Mr. Wilkes), and the mother's lawyer (Ms. Parr) — all invented, as are the program, the screen, the assessment, the summary's two lines, and every document quoted or described. No county is named. The worker change is placed at month 8 so that the parent has a completed record worth losing — the loss the scenario studies is continuity, not compliance.

### Dates audited

Story opens **Monday, June 1, 2026** (day 0). First meeting with the new worker: day 9 = **Wednesday, June 10, 2026**. Status letter dated day 14 = **Monday, June 15, 2026** (inside the new worker's first weeks, as the beat requires). Record request: day 25 = **Friday, June 26, 2026**. Review: day 56 = **Monday, July 27, 2026** (a weekday, as a court review must be). All three endings land day 63 = **Monday, August 3, 2026**. Every kicker and every in-body date was computed from the start date by the generator (`datestr()` on startDateISO + dayOffset) and recomputed in validation; no date was hand-typed into the data. Silas's placement (eight months before day 0) is stated only relatively — no placement date is asserted, and no clock is computed from it.

### Law used

55 Pa. Code § 3130.44(d) (record released on request — the draft-report beat); 55 Pa. Code § 3130.44(f) (the redactions in the released packet, worded as in Scenario 31); 42 Pa.C.S. § 6337 (counsel, at review preparation). Nothing else is stated as law. The summary, the draft report, and the correction procedure are written as generic process description with no citation, and no deadline, appeal window, or filing rule is invented for any of them.

### Withholdings

- **No proposition about how often summaries are wrong, or about any agency's handoff practice as a fact.** The scenario depicts one handoff, as a composite of the documented record-bound-reader pattern; it asserts no rate and names no agency.
- **No claim that a filed correction binds a court or a report writer.** The win ending is written as the correction adopted on this record, by these readers; the guide states plainly that a different supervisor or report writer could have contested it.
- **No shelter-care, appeal-window, or ASFA date.** None arises on these facts, so none is stated; the verified set was available and deliberately not spent.

---

## SCENARIO 61 — "The Expired Referral" (27 nodes, 3 endings, Hard)

*A sequential plan: Step A (a trauma-therapy evaluation) must be completed before Step B (the parenting program) will enroll her. The referral for A is sent; A has a five-week waitlist; referrals expire after 60 days. The agency re-refers, but the queue restarts — and the review report's line is "A not completed."*

### Documented pattern basis

Sequential-services and referral mechanics, as documented practice patterns in published termination-of-parental-rights opinions' compliance discussions already in the project library — stated as patterns, never as holdings:

1. **In the Interest of J.L.L., No. 1714 EDA 2023 (Pa. Super. Apr. 26, 2024)** — the case-plan objective set (parenting classes, treatment, employment, housing) against which compliance is later measured item by item. Drawn on here for the sequential plan's structure: a plan written as an ordered set of objectives, where an early objective's non-completion is later read as the parent's compliance failure without regard to what produced it. (Cited in `sources-and-alterations.md`, Scenario 3 sources, item 1.)
2. **In re Adoption of N.R.A., No. 915 WDA 2025 (Pa. Super. 2026)** — waitlist testimony: a mother testifying she was on a waitlist, with the delay entering the compliance discussion only through later testimony. Drawn on here for the waitlist as a lived fact that the file records thinly or not at all — the pattern this scenario answers by documenting the wait, and the referral chain around it, as it happens. (Cited in `sources-and-alterations.md`, Scenario 3 sources, item 2.)

Supporting pattern texture, from the same library and from Scenario 14's documented basis: services whose availability, capacity, or administrative processing — not the parent's effort — determined when (or whether) a plan step could be completed, with the resulting gap later summarized in reports in grammar that assigns the delay to the parent ("A not completed" is this scenario's invented instance of that documented sentence-shape).

**Deliberate distinction from Scenario 14:** Scenario 14's mechanism is program *capacity* (one program, one waitlist, one late start). Scenario 61's mechanism is the *referral chain itself* — a validity window (60 days), an expiry, a re-referral, and the question of whose job the re-send was and whether the queue position survives it. No beat, document, or ending from Scenario 14 is reused; the shared element is only the series-wide discipline of documenting a system's delay before a report can reassign it.

### Beats drawn

- The sequential plan explained at the start (Step A gates Step B), with the referral "sent" on day 0 and its validity window unmentioned (pattern basis item 1: the plan's order is the court's; the chain's dates are nobody's stated job).
- The opening split: the referral copy **with its sent date and 60-day validity window** in writing (`referralDated`), versus trust in the phone call.
- Intake: waitlist confirmed at about five weeks, with evaluation appointments batched in a week that begins three days after the window closes — the collision visible only to a parent holding the dated copy.
- The middle weeks running clean (visits, screens, meetings) while the Step A line stands still (pattern basis item 1: the standing-still line is what the review will summarize).
- The day-50 written nudge before expiry (`diaryNudge`), versus assuming the re-send is handled — the beat that decides whether the lapse is documented as the sender's timing.
- The expiry playing out differently by the paper: with the dated referral and the nudge, the provider honors the original queue position on the re-send as a continuation; without them, the queue restarts silently and the re-referral is a new arrival.
- The re-referral proof kept (`rereferralProof`), the record request under § 3130.44(d) surfacing the agency's own referral and re-referral dates with no expiry note between them, Step B's enrollment letter arriving or not, and the gated review.

### Alterations

The source opinions involve multi-year cases, different plan objectives, and (in several) findings about parental compliance that this scenario does not adopt or invert. The composite is one mother (Tanya), one daughter (Cora, 3), and one worker (Ms. Beam) — all invented. The two-step plan (trauma-therapy evaluation gating a parenting program), the 60-day referral validity period, the five-week waitlist, the batch-week scheduling, the provider's continuation practice, and every document are invented as a composite of the documented patterns. The 60-day window is expressly written in-game and in the guide as administrative machinery (a provider's validity period), **not** as law. No county or provider is named, and the mother's lawyer is deliberately left unnamed.

### Dates audited

Story opens **Monday, June 15, 2026** (day 0) — the referral is sent that day. The written nudge on the winning route is sent day 50 = **Tuesday, August 4, 2026**, ten days before expiry. The referral's 60-day window closes day 60 = **Friday, August 14, 2026** (June 15 + 60 days, machine-computed and asserted in the generator). Evaluation appointments are batched in the week beginning day 63 = **Monday, August 17, 2026** — three days after the window closes, which is the collision the scenario is built on. The evaluation on the winning route is completed day 66 = **Thursday, August 20, 2026**. Review: day 91 = **Monday, September 14, 2026**. All three endings land day 98 = **Monday, September 21, 2026**. Every kicker and every in-body date was computed from the start date by the generator and recomputed in validation; no date was hand-typed into the data. Cora's placement predates the story and is stated only relatively; no ASFA date is asserted anywhere in the scenario.

### Law used

In the game: 55 Pa. Code § 3130.44(d) (the record request that surfaces the referral chain and the draft chronology) and 42 Pa.C.S. § 6337 (counsel). Nothing else is stated as law in the game — in particular, **no ASFA proposition appears in the scenario data at all**. In the strategy guide only: 42 U.S.C. § 675(5)(E), discussed in Scenario 14's disciplined form — the services exception as a record-dependent argument about the *filing decision*, which would still require any termination to be proven by clear and convincing evidence. The guide asserts no filing date for Cora (her entry date is never stated) and predicts no filing or termination outcome.

### Withholdings

- **The 60-day validity period is not presented as a rule of law, a regulation, or any real provider's policy.** It is a composite instance of documented referral-expiry practice, labeled in the guide as administrative machinery.
- **No holding is drawn from J.L.L. or N.R.A.** Both are used for documented practice patterns in compliance discussions (plan objective sets; waitlist testimony), exactly as characterized above — never for a proposition that a court must attribute a referral delay to an agency.
- **No claim that a provider must honor a queue position on re-referral.** The continuation in the win ending is written as this provider's documented response to a documented lapse, and the guide lists a provider who declines to honor it among the things no strategy controls.
- **No § 2511 grounds, no termination outcome, no reunification outcome.** The scenario ends at a review's attribution of a delay; Cora remains placed in all three endings.

---

*Compiled for Wave H, Scenarios 60–61 (Hard tier). Draft — not legal advice, not a depiction of any real case. Companion files: `scenario-60.json` / `scenario-60-script.md` / `strategy-60.md`, `scenario-61.json` / `scenario-61-script.md` / `strategy-61.md`, generated by `generate-scenarios-60-61.py`.*
