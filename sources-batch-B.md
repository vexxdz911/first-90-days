# SOURCES AND ALTERATIONS — Batch B: Scenarios 12–16 (Hard batch 1)

*How "The First 90 Days" Scenarios 12–16 were built from the published public record, what was drawn from each source, what was changed, which legal propositions were used, and what was deliberately withheld.*

**Status:** Draft documentation, for internal development and attorney review. Nothing here or in the scenarios is published or sent.

**Source rule applied:** Every scenario derives only from published Pennsylvania Superior Court opinions in dependency and termination-of-parental-rights matters, and from legal propositions already in this project's verified set. No private case, file, docket, or person from the development team's own orbit was used as source material, in any form.

**Alteration doctrine applied:** Each scenario is a composite. Procedural spines and testimony-textured beats come from the published sources; names, ages, counties, occupations, and identifying facts are changed, and beats from at least two published sources are merged in every scenario, so that no real family maps onto any character.

**Engine-flag note (all five scenarios):** The `removed` flag is deliberately **absent** from Scenarios 12–16, because no removal occurs inside any of these stories — each child was placed before the playable story opens (S12: siblings already in two placements; S13: son already placed; S14: daughter placed ten months earlier; S15: son placed with his aunt before the story opens; S16: daughter placed eight months earlier). Setting `removed` would fire the engine's 72-hour shelter-care banner falsely. The `recordsRequested` flag is set in all five, in each case by the parent herself as a party to the case. Every scenario's win route was additionally verified to pass through `recordsRequested` (see Validation, below).

**Law used (all five scenarios, nothing beyond the shared verified set):** the case record "shall be released upon request" (55 Pa. Code § 3130.44(d)); the right to counsel in dependency proceedings (42 Pa.C.S. § 6337); the ASFA 15-of-22-months framework and its three exceptions, including the exception for services identified but not provided to the family (42 U.S.C. § 675(5)(E)) — S14 and S16 principally, by reference in S16's debriefs; and the clear-and-convincing burden, referenced generically in debriefs (S14, S15). No scenario states any other statute, rule, or day-count as law. Inter-county transfer mechanics (S16), plan-amendment procedure (S13), sibling-visit scheduling (S12), and service documentation practice (S14, S15) are described generically and without citation, as process rather than law. The assessment in these scenarios is never described as AI, machine learning, or predictive.

---

## SCENARIO 12 — "Two Homes" (25 nodes, 3 endings)

*Siblings split between two placements with two workers; sibling visits never scheduled because scheduling belongs to no one; the playable skill is one written request, sent to everyone responsible at once, that forces coordination onto the record.*

### Published sources used

1. **In the Interest of C.D.M., Jr. / C.D.M.M. (Pa. Super. Oct. 18, 2017)** (J-S52011-17) — https://cases.justia.com/pennsylvania/superior-court/2017-647-mda-2017.pdf?ts
   - *Beats/textures drawn:* Siblings in separate pre-adoptive homes; a caseworker who had spoken with both foster families about the separation; the children's advocate questioning sibling-contact arrangements; a court that ultimately directed the agency and advocate to meet with the foster parents and ordered a minimum of two hours per week of sibling time plus a weekly conference call. Source of the scenario's spine: coordination that happens only when a court or a formal item makes it someone's job.
2. **In Re J.M.G. (Pa. Super. Feb. 2, 2026)** — https://law.justia.com/cases/pennsylvania/superior-court/2026/1015-wda-2025.html
   - *Beats/textures drawn:* Siblings split by household — girls placed together in one foster home, boys together in a separate one — with supervised visitation ordered across the split. Texture for the two-household, two-routine texture of the composite's placements.
3. **In the Interest of Z.N.B. (2024 PA Super 262)** — https://law.justia.com/cases/pennsylvania/superior-court/2024/241-wda-2024.html
   - *Beats/textures drawn:* The youngest child placed in a pre-adoptive home separate from older siblings, and the frequency of the mother's offered visitation fluctuating over years. Texture for drift as the default: contact that expands and contracts with no single decision producing it.

### Alterations applied
The sources involve pre-adoptive placements and termination postures; the composite is set earlier, at an ordinary review, with reunification still the plan. Two children only (Mara, 9; Jonah, 6), two foster households, two workers in two offices, and a Sunday visit-room solution invented for the composite. The court-ordered minimum contact in C.D.M. is **not** imported as an entitlement — the game's order adopts the arrangement the parent's own paper produced, and the guide says expressly that no verified rule schedules sibling visits by itself.

### Dates audited
Start Monday, March 2, 2026. The review date stated in-game — **Thursday, April 30, 2026** — is start + 59 days, generated from the same arithmetic as the hearing node's dayOffset (59) and machine-checked. All 25 kickers machine-checked against the real calendar.

### Deliberately not used
- **42 Pa.C.S. § 6351 sibling-visitation provisions**, which surfaced in research: outside this project's verified-law set, so the scenario claims no statutory sibling-visit right and the order is framed as the court acting on the documented record, not on a cited mandate.

---

## SCENARIO 13 — "The Night Shift" (27 nodes, 3 endings)

*Every service in the plan is scheduled inside a night-shift mother's sleep; the playable skill is an employer letter plus a written plan-amendment request — with quitting the job kept fully playable, and priced.*

### Published sources used

1. **Adoption of H.J.M. (Pa. Super. Jan. 14, 2022)** — https://law.justia.com/cases/pennsylvania/superior-court/2022/884-wda-2021.html
   - *Beats/textures drawn:* A mother working a full-time overnight shift whose visits were scheduled at 9 A.M.; she occasionally fell asleep after work; on cross-examination she testified the agency worked with her on visit times and that she had requested the 9 A.M. visits. The scenario deliberately varies the last point — its parent never chose the times — while keeping the texture of a file that records fatigue without recording its cause.
2. **In the Interest of D.A.C.N. (Pa. Super. Mar. 23, 2020)** — https://law.justia.com/cases/pennsylvania/superior-court/2020/1953-eda-2019.html
   - *Beats/textures drawn:* A mother attributing missed visits to her work schedule, and her claim that she could not attend a random drug screen within 24 hours of notification because of her work schedule and lack of money. Direct texture for the closed-window screen beat and for explanations offered after the fact, in testimony, when the notes had already hardened.
3. **In re T.J.J.M. (Pa. Super. 2018)** — Studicata editorial summary (texture only, not opinion text): https://www.studicata.com/summaries/superior-court-of-pennsylvania/in-re-t-j-j-m-2018-snsx7h/
   - *Beats/textures drawn:* A father's work obligations colliding with the services offered him — including a single offered Saturday visit, canceled for the foster family's unavailability and never rescheduled — and services not fitted to his schedule. Texture for the scenario's services-gap theme. **Not used as law:** any broader reasonable-efforts holding associated with this line of cases (consistent with this project's prior withholding of that doctrine in Scenario 3).

### Alterations applied
Sources are termination appeals looking backward; the composite is set mid-case at a review, with the mother employed, housed, and engaged — isolating the schedule itself as the defect. Warehouse job, supervisor, provider cohort, and all documents invented; the father's facts in T.J.J.M. re-costumed to the mother; the 9 A.M. visit texture from H.J.M. generalized to the whole service plan.

### Dates audited
Start Monday, April 13, 2026. Hearings sit at dayOffset 49 — Monday, June 1, 2026 (the offset was deliberately moved off 48, which lands on a Sunday). All 27 kickers machine-checked.

### Deliberately not used
- Any legal entitlement to rescheduled services. None was verified; the scenario and guide state expressly that the amendment is administrative and discretionary, which is why the written request — the pending item — carries the strategy.

---

## SCENARIO 14 — "The Waiting List" (25 nodes, 3 endings)

*The court-ordered treatment program has a six-week waitlist; the playable skill is building the record that proves the delay belongs to the system — the record the ASFA services exception runs on.*

### Published sources used

1. **In Re B.L.D. (Pa. Super. May 29, 2025)** — https://law.justia.com/cases/pennsylvania/superior-court/2025/1511-wda-2024.html
   - *Beats/textures drawn:* A mother's testimony that she did not participate in the parenting program because she was on a waiting list and, as she understood it, not permitted to start until she had "been 30 days clean" — and her testimony that the agency was not forthcoming with information. The scenario's premise verbatim in structure: a parent kept from a program by the program's and system's gates, explaining it afterward, from the witness stand.
2. **In Re T.L.H., Jr. (2025 PA Super 102)** — https://law.justia.com/cases/pennsylvania/superior-court/2025/1474-mda-2024.html
   - *Beats/textures drawn:* A father's testimony that he could not obtain evaluations because of a long waiting list for programs and services — and the documentary counterexample the case also contains: his written request for an evaluation and the institution's written response that it did "not provide psych evaluations for this purpose." Texture for the scenario's central mechanic: a request and a refusal that exist *in writing* can be attached; a wait that was only ever spoken about cannot.
3. **In Re B.B. (Pa. Super. 2014)** (search-result level only; not opened in full) — https://law.justia.com/cases/pennsylvania/superior-court/2014/979-mda-2014.html
   - *Use limited to corroborating texture:* a waiting list affecting parenting classes, and a six-week treatment program appearing in testimony. No proposition and no specific beat rests on this source alone.

### Alterations applied
The sources' parents testified about waitlists retrospectively, at termination. The composite moves the waitlist into the present tense and makes the parent document it prospectively — the scenario is explicitly the road those testimonies did not get to take. Program ("Harborview"), child (Wren, 4), the Thursday-email ritual, the triage week, and all documents are invented; the six-week length is drawn from B.B.'s texture and B.L.D.'s structure, set as the program's stated intake estimate.

### Dates audited
Start Monday, May 4, 2026. Intake at dayOffset 3 (Thursday, May 7, 2026); the stated program start — **Thursday, June 18, 2026** — is intake + 42 days exactly, generated programmatically, appears identically in the intake and start-day nodes, and matches the start-day node's dayOffset (45 = start + 45 days). All 25 kickers machine-checked. The case's month-ten posture is stated without a computed 15-month date; no filing date is depicted or predicted, and the story ends at the review, consistent with the ASFA exception's actual scope (the filing decision).

---

## SCENARIO 15 — "The Protective Parent" (24 nodes, 3 endings)

*A survivor is alleged, in the plural, to have "failed to protect," while the other parent is the danger; the playable skill is safety documentation and the documentary separation of her record from his. No graphic detail appears anywhere in the scenario.*

### Published sources used

1. **In Re A.S., Jr. (Pa. Super. Feb. 14, 2025)** — https://law.justia.com/cases/pennsylvania/superior-court/2025/1418-mda-2024.html
   - *Beats/textures drawn (procedural only):* An intake worker's repeated home attempts met by the paramour denying he knew the mother and threatening the worker off, so first contact with the mother came only after petitions were filed; an expert who testified unaware that the mother had left the relationship and obtained a Protection from Abuse order, describing her as a victim of her circumstances; and the later beat of the partner's interference with her car affecting her ability to get to work. The scenario uses only the documentation texture — protective steps that exist but never reached the file, a "parents"-level summary written before the mother was ever spoken to, and a car break-in rendered without attribution or detail. **None of the source's accounts of abuse are reproduced, described, or alluded to in-game.**
2. **In the Interest of E.L.C. (Pa. Super. Nov. 25, 2025)** — https://law.justia.com/cases/pennsylvania/superior-court/2025/447-mda-2025.html
   - *Beats/textures drawn:* A mother who had obtained a PFA against the father; the father discharged from a multi-session batterers' intervention program three separate times; and the documentation gap at the case's center — the caseworker testifying only that "there was some contact" with the Domestic Violence Center, with no dates or times, while the mother testified only that she "spoke with" the center. The scenario's "Some Contact" node and its center-letter beat are built directly on that gap. The source's later reconciliation/withdrawal posture is **not** used; the composite mother does not reconcile.
3. **K.C. v. Department of Public Welfare (Pa. Cmwlth. 2012)** — Studicata editorial summary (background only): https://www.studicata.com/summaries/commonwealth-court-of-pennsylvania/k-c-v-department-of-public-welfare-2012-swj0fp/
   - *Use:* Background only — the "perpetrator by omission" / failure-to-protect framing as an allegation category. The source's facts are severe and are **not** used, in any form, in the scenario.

### Alterations applied
One child (Sam, 6), placed with his maternal aunt; the petition's language generalized to "exposure to domestic conflict"; the mother's protective record (order, center engagement, lock change, school transfer, leaving) assembled as a composite of the two principal sources' documentation beats; the father's program discharge set at one in-story discharge letter (his longer history referenced, not enumerated). All names, workplaces, and documents invented.

### Dates audited
Start Monday, June 1, 2026. Hearing at dayOffset 56 — Monday, July 27, 2026 (offset moved off 54, a Saturday). All 24 kickers machine-checked.

### Deliberately not used
- Any statutory test for "failure to protect," any PFA procedure or day-count, and any protective-order law. None is in the verified set; the scenario keeps its law to § 6337, § 3130.44(d), and the generically referenced clear-and-convincing burden, and frames separation as evidentiary practice, not doctrine.

---

## SCENARIO 16 — "The Second County" (25 nodes, 3 endings)

*A family moves counties mid-case for housing; the official file takes thirty-four days to follow; every clock keeps running; the playable skill is carrying her own copies across the border so the case does not restart from zero.*

### Published sources used

1. **Adoption of M.A.B. (2017 PA Super 202, June 29, 2017)** — https://law.justia.com/cases/pennsylvania/superior-court/2017/1720-wda-2016.html
   - *Beats/textures drawn:* A case begun in Venango County; the mother moved to Erie for treatment; jurisdiction transferred to Erie County in July 2014 and Erie OCY moved the children to a second foster home (later a third); the Erie court largely continuing the Venango plan. Source of the scenario's spine: transfer as a real event with real lag, and a receiving county working from the sending county's plan.
2. **Adoption of E.M.W.H.-R. (Pa. Super. Oct. 15, 2024)** — https://law.justia.com/cases/pennsylvania/superior-court/2024/600-wda-2024.html
   - *Beats/textures drawn:* Siblings' cases sitting in different counties (Warren/Schuylkill); one child's case transferred to the other county after she was moved into the same kinship home as her sibling (May 2022), with the dependency proceedings thereafter heard simultaneously, before multiple rotating judges. Texture for multi-county simultaneity — two systems, one family, proceedings that must somehow be heard as one case.

### Alterations applied
The sources are adoption/termination postures after transfer; the composite is set mid-case at an ordinary review, with the move driven by an eviction rather than treatment, one child (Ivy, 8), and fictional county names ("Alder," "Bexley") used throughout so no real county's procedures are depicted or implied. The thirty-four-day transfer lag, the missing-certificates detail, the cousin's sixty-day guest limit, and the parent-carried binder are invented mechanics built to dramatize the documented phenomenon (cases arriving thinned and re-baselined) rather than any single case's timeline. The child remains placed in the sending county during the story — a deliberate simplification, flagged here: the sources show placements moving with transfers, and the game's choice keeps the review court's and the child's placement stable so the paperwork problem stays in focus.

### Dates audited
Start Monday, August 3, 2026. The review date stated in-game — **Monday, September 14, 2026** — is start + 42 days, generated from the same arithmetic as the review node's dayOffset (42) and machine-checked; the box's arrival at day 34 and the review at day 42 keep the story's stated eight-day gap exact. All 25 kickers machine-checked.

### Deliberately not used
- Any transfer statute, venue rule, or inter-county procedure stated as law. None is in the verified set; transfer mechanics are described generically ("the agency's process," intake practice) and the only law the scenario claims is the record right itself (§ 3130.44(d)), counsel (§ 6337, via the lawyer's role), and the ASFA clock reference (§ 675(5)(E)) — run, in the debriefs' framing, from the child's life rather than the file's itinerary.

---

## VALIDATION RECORD (all five scenarios, run 2026-10-28)

Each `scenario-N.json` was generated from the same single source as its `scenario-N-script.md` and validated programmatically:

- **Schema/shape:** parses as JSON; `meta.tier` = "Hard"; one-line `summary` present; `startNode` resolves; node IDs unique; node counts 25 / 27 / 25 / 24 / 25 (all inside the Hard band of 24–34); exactly **3 endings** each; endings carry `debrief` and no choices; every non-ending carries at least one choice; every choice's `next` resolves.
- **Graph:** full BFS reachability from `start` — every node, including all three endings, is reachable in each scenario; `dayOffset` is non-decreasing along every edge.
- **Flags:** `recordsRequested` is set in each scenario, and on each scenario's verified win route; `removed` is set in none (see the engine-flag note above); hidden items per scenario: 9 / 6 / 6 / 8 / 8.
- **Dates:** every node's kicker recomputed from `startDateISO + dayOffset` and matched exactly (weekday, month, day, year); the three in-text deadline dates (S12 review, S14 program start, S16 review) are generated from the same arithmetic and match their nodes' offsets.
- **Law scan:** every statutory citation in the five files was extracted and checked against the verified set — no citation outside § 6337, § 3130.44(d), § 675(5)(E), and the generically referenced burden appears in any scenario, script, or guide; the words "predictive" and "machine learning" appear nowhere.
- **Script parity:** every node header and every choice edge in each JSON appears in its `scenario-N-script.md`.
- **Strategy-guide path checks:** each `strategy-N.md` route was walked programmatically against the final JSON (choice-by-choice, from `start` to the named ending): S12 → "Ending — One Calendar" (14 steps, end cash $196/$210); S13 → "Ending — The Plan Moves" (12 steps, $156/$165); S14 → "Ending — The Delay Has a Name" (18 steps, $38/$140); S15 → "Ending — Two Files, Not One" (16 steps, $122/$190); S16 → "Ending — The File Arrives With Her" (19 steps, $155/$230). All five walks pass on the shipped files.

## ACCESS NOTES

Research for this batch was conducted in the prior session (2026-10-28) via browser search and full-text reads of the opinions listed, principally on Justia. Studicata pages are editorial summaries, not opinions; they were used for fact texture only (T.J.J.M.; K.C. as background), and no proposition of law rests on them. In re J.R. (CaseMine) surfaced in search results for S14 but could not be opened (captcha) and was **not** used. In Re B.B. was used at search-result level only, as flagged above, with no beat resting on it alone. No paywalled source was needed or used. Every legal proposition in the five scenarios is in the previously verified set; this batch verified no new law and claims none.

---

*Compiled under the Agency Agents pattern (Orchestrator, Narrative Designer, Legal Researcher, Legal Compliance Checker personas). Draft — not legal advice, not a depiction of any real case. Companion files: `scenario-12.json` / `scenario-12-script.md` / `strategy-12.md` through `scenario-16.json` / `scenario-16-script.md` / `strategy-16.md`.*
