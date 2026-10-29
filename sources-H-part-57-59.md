# SOURCES AND ALTERATIONS — Part H: Scenarios 57–59 (Foundation)

*How "The First 90 Days" Scenarios 57–59 were built from the patterns documented in the project's existing research, what was drawn from each pattern, what was changed, and the date arithmetic for every stated date.*

**Status:** Draft documentation, for internal development and attorney review. Nothing here or in the scenarios is published or sent.

**Source rule applied:** Every scenario in this part is a fictional composite built **only** from patterns already documented in this project's research files — published Pennsylvania Superior Court opinions as catalogued in `sources-and-alterations.md` and the batch source files — and from the shared verified law set. No private case, file, docket, or person from the development team's own orbit was used as source material, in any form; the named private cases in the owner's orbit were excluded absolutely, as sources and as models. No new legal research was opened for this part, and no new legal proposition is asserted anywhere in it.

**Alteration doctrine applied:** The documented pattern supplies the procedural spine and the texture; names, ages, counties, programs, occupations, and all dialogue are invented, and each scenario re-costumes its pattern so that no real family maps onto any character. Where a pattern comes from an opinion's compliance discussion, it is used as **pattern and texture only — never as a holding** — and the scenarios say nothing about what any court held.

**Engine-flag note (all three scenarios):** `recordsRequested` is set on every winning route — in this part the record request is the load-bearing move in all three stories. The `removed` flag is deliberately **absent** from all three scenarios, for the per-scenario reasons stated below; setting it would fire the engine's 72-hour shelter-care banner falsely in each case. No assessment is called AI, machine learning, or predictive anywhere in this part; the one instrument mentioned (Scenario 57) is "a scored assessment form," in the project's standard wording.

**New law verified in this part: NONE.** All three scenarios use only two items from the shared verified set: records released on request (55 Pa. Code § 3130.44(d), quoted in the project's verified wording, "shall be released upon request") and counsel / appointed counsel (42 Pa.C.S. § 6337). Pa.R.J.C.P. 1340 is **not used** in this part, by design. Everything else in the three scenarios — a plan's tally language, a provider consolidation, a sign-in sheet — is generic process description with no citation, inventing no rule, deadline, or right.

---

## SCENARIO 57 — "The Referral That Never Came" (18 nodes, 2 endings)

*A mother whose daughter is home under court supervision is ordered into a named parenting program; the worker says the referral was sent; the program has no record of her; five weeks later a progress note calls her "not yet engaged in parenting services."*

### Documented pattern basis
- **The services / referral-gap pattern documented across the published termination-of-parental-rights opinions in the project library:** compliance is measured at review and at termination against the services the *record* shows were ordered — the case-plan objective sets catalogued in `sources-and-alterations.md`'s Scenario 3 discussion of **In the Interest of J.L.L., No. 1714 EDA 2023 (Pa. Super. Apr. 26, 2024)** (parenting classes, treatment, employment, housing as plan objectives, with compliance rated from the record) supply the texture of a plan whose lines are later read as facts about the parent.
- **In re T.J.J.M. (Pa. Super. 2018)**, as catalogued in the same discussion: a parent willing to engage whose services were **not fitted to his circumstances** — used here only for its recurring shape, services that exist on the plan's page but not, in usable form, in the parent's life. Scenario 57 is that shape with the failure moved one step earlier: the service is not mis-fitted but never transmitted at all, the mildest and most ordinary version of the documented gap, and the one most completely provable from paper.

### Beats drawn
The plan ordering a named program; the worker's verbal assurance that a referral "was sent"; the program's empty file; the five-week silence; the progress note rating the parent against the unstarted service ("not yet engaged"); and a review that weighs the note. Each beat is the documented pattern's beat, re-costumed.

### Alterations
Mother (Colleen), daughter (Nia, 6), worker (Ms. Voss), and the program ("Brightpath Parenting") are invented entire; no county, employer, or town is named. The posture is changed from the sources' posture: the child is **home under supervision in an in-home case**, not placed — deliberately the lowest-stakes posture in the library, so the drama is purely documentary. The gap is compressed to five weeks and a single service line. All dialogue, the flyer beat, and the one-page-timeline device are invented as the composite's taught skill.

### Dates audited
Start Monday, March 16, 2026 (day 0). The progress note lands on day 35 — Monday, April 20, 2026 — exactly five weeks after the plan, as the outline requires. Review day 44, Wednesday, April 29, 2026; endings day 47, Saturday, May 2, 2026. Every kicker and every in-body date was computed by the generator's `datestr()` helper from the start date plus dayOffset and machine-checked against the real calendar in validation.

### Law used
55 Pa. Code § 3130.44(d) (the file request that surfaces the chronology's "mother to enroll in parenting services," with no referral date) and 42 Pa.C.S. § 6337 (counsel presenting the timeline at the review). No other law is stated as law.

### Withholdings
- **No holding is claimed** from J.L.L. or T.J.J.M. about referrals, reasonable efforts, or compliance; the opinions are used for the documented pattern of record-measured compliance only, exactly as the Scenario 3 discussion framed them.
- **No referral deadline, transmittal rule, or agency duty timeline is stated** — none is in the verified set, so the scenario claims only that the referral was ordered, was said to be sent, and was not received; the remedy shown is documentary (a dated written chase, the requested chronology, a corrected record), not a legal entitlement to a send date.
- **No finding about why the referral failed** is made or implied: the scenario deliberately never shows the worker's side of the desk, and its debriefs state that the cause is unknown.

### Why no `removed` flag
Nia is home throughout, under court supervision, in an in-home case; no removal occurs before or during the playable story. A `removed` flag would falsely start the 72-hour shelter-care clock in a story whose whole point is that the child never left home.

---

## SCENARIO 58 — "The Missed Screen" (18 nodes, 2 endings)

*A mother in recovery whose son is in kinship care with his grandmother is summoned by text at 9:40 p.m. to a screen across town at 8:00 the next morning; her shift starts at 8:30; the plan records a missed screen as a failed appearance, tallied the same as a positive result.*

### Documented pattern basis
- **Documented practice pattern (stated as pattern, not as a holding):** screens and schedule conflicts as they appear in the compliance discussions of the published opinions in the project library — principally the texture catalogued from **In the Interest of J.L.L. (Pa. Super. 2024)** in `sources-and-alterations.md`'s Scenario 3 discussion, where a parent's progress is rated from the record of what was attended, submitted, and shown, and where the logistics of a working parent's life meet plan requirements written without them. Scenario 58 isolates one joint in that machinery: a random summons whose time, place, and tally rule are all set by the system, colliding with a fixed work shift, and a record that keeps the entry but not the arithmetic.

### Beats drawn
The verbally-explained protocol; the night-before text summons; the cross-town collection window (7–9 a.m.) against an 8:30 shift; the plan's tally language for a missed screen; a second screen in month two whose **result posting** lags its completion, so a completed screen sits in the file as "not received"; and a review that tallies entries until the underlying times are put beside them.

### Alterations
Mother (Desirae), son (Leo, 5), and grandmother (Lorraine) are invented entire; the caseworker is deliberately left unnamed; no county, employer, site, or program is named. The kinship placement predates the story and is never litigated in it. All substance content is procedural only — summonses, windows, shifts, confirmations, logs — with no substance, use, or result described beyond completed / recorded / tallied; the recovery itself appears only as a schedule of meetings and work, which is how the scenario insists it be read.

### Dates audited
Start Monday, April 13, 2026 (day 0). The summons text arrives day 7 — Monday, April 20, 2026, at 9:40 p.m. — for a screen on day 8, Tuesday, April 21, 2026. Month two's screen is completed on day 36, Tuesday, May 19, 2026. Review day 56, Monday, June 8, 2026; endings day 59, Thursday, June 11, 2026. Every kicker and every in-body date was computed by `datestr()` and machine-checked in validation.

### Law used
55 Pa. Code § 3130.44(d) (the screen log as part of the case record, released on request) and 42 Pa.C.S. § 6337 (counsel). The plan's "failed appearance" tally language is presented throughout as **the plan's own wording in the fiction** — generic process description, with no citation and no claim that any real plan, rule, or statute uses it.

### Withholdings
- **No proposition about drug testing, screen validity, tally rules, or consequences is stated as law** — nothing on those subjects is in the verified set, so the scenario's default rule lives only inside its fictional plan and is labelled as such in the text and in the strategy guide.
- **No holding is drawn from J.L.L.** about screens or compliance; the opinion supplies documented texture for how records rate parents, and the scenario is explicit in its debriefs that the tally it depicts is a paperwork event, not a finding about recovery.
- **No relapse, use, or positive result is depicted or implied** in either ending; the losing ending's title ("Positive, By Default") is explained in its debrief as the plan's default paperwork, and the debrief states expressly that no test was failed.

### Why no `removed` flag
Leo's kinship placement with his grandmother predates the playable story; no removal occurs inside it, and the story never returns to the placement decision. A `removed` flag would falsely fire the shelter-care clock for a move the game does not depict.

---

## SCENARIO 59 — "Two Buses to the Visit" (19 nodes, 2 endings)

*A father's Saturday visits, held a short walk from his home, are moved by letter to a visitation center across the county after a provider consolidation: two buses, ninety minutes. He arrives twenty minutes late, the visit is shortened, and the note reads "father arrives late; visit shortened." Three Saturdays become a pattern of "lateness" in the pre-review summary.*

### Documented pattern basis
- **In re T.J.J.M. (Pa. Super. 2018)**, as catalogued in `sources-and-alterations.md`'s Scenario 3 discussion: testimony texture of a parent willing to engage who was offered **one Saturday visit, cancelled because of the foster family's unavailability and never rescheduled**, in a case where services were **not fitted to the parent's circumstances**. Scenario 59 re-costumes that documented shape — a visit made effectively unavailable by the system's own arrangements, with the unavailability then visible in the record only as the parent's failure — as a visit *site* moved across a county: the visit is never cancelled, it is simply made ninety minutes away, and each arrival is then noted without its journey.

### Beats drawn
The system's rearrangement of a visit the parent was keeping; the shortened visit; the visit note that records the parent's arrival and nothing about the arrangement ("father arrives late; visit shortened"); repetition hardening single notes into a summary "pattern"; and a review at which the underlying documents — the move letter, the center's own sign-in times — either are or are not put beside the pattern.

### Alterations
Father (Andre) and daughter (Ruby, 7) are invented entire; the caseworker, the foster family, and the center's staff are deliberately left unnamed; no county, provider, bus route, or town is named. The T.J.J.M. beat is transformed in kind, not just in costume: cancellation becomes relocation, a single lost visit becomes three shortened ones, and the unavailability is produced by an ordinary administrative consolidation rather than by any household's choice — because the composite's subject is how a file converts logistics into character, not any actor's fault. The arrival-log and sign-in-sheet devices are invented as the taught skill.

### Dates audited
Start Monday, May 11, 2026 (day 0) — the move letter is dated to day 0 in the text by the generator's helper. The three moved visits fall on Saturdays, as the story's framing requires: day 5, Saturday, May 16, 2026; day 12, Saturday, May 23, 2026; day 19, Saturday, May 30, 2026. The pre-review summary lands day 23, Wednesday, June 3, 2026; review day 42, Monday, June 22, 2026; endings day 45, Thursday, June 25, 2026. Every kicker and every in-body date was computed by `datestr()` and machine-checked in validation; the Saturday placement of all three visit nodes was verified against the real calendar before delivery.

### Law used
55 Pa. Code § 3130.44(d) (the visit notes as part of the case record, released on request — the center's own recorded times) and 42 Pa.C.S. § 6337 (counsel). The nearer site and transportation support in the winning ending are depicted as a review outcome on this fictional record — process, ordered in the fiction — and **not** as an entitlement any cited law creates; the strategy guide states this limit expressly.

### Withholdings
- **No reasonable-efforts or services holding from T.J.J.M. is used as law** — consistent with the project's standing withholding (the D.C.D./T.J.J.M. reasonable-efforts line was rejected by the Supreme Court, as recounted in In re T.R.C. and noted in `sources-and-alterations.md`): T.J.J.M. appears here as testimony texture only, exactly as in Scenario 3.
- **No right to a visit location, transportation support, or a visit of any particular length is stated** — none is in the verified set; the scenario claims only that a move can be answered in writing and its consequences documented.
- **No finding about the original placement is made** — it predates the story, is never described, and no beat in the scenario reaches back to it.

### Why no `removed` flag
Ruby was placed before the story opens; no removal occurs inside the playable story, which is entirely about visits to an already-placed child. A `removed` flag would falsely start the 72-hour shelter-care clock at the date of a letter about bus routes.

---

*Compiled for Wave H, Part 57–59 (Foundation). Draft — not legal advice, not a depiction of any real case. Companion files: `scenario-57.json` / `scenario-57-script.md` / `strategy-57.md`, `scenario-58.json` / `scenario-58-script.md` / `strategy-58.md`, `scenario-59.json` / `scenario-59-script.md` / `strategy-59.md`, generated by `generate-scenarios-57-59.py`.*
