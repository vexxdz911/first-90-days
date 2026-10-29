# SOURCES AND ALTERATIONS — Part H: Scenarios 62–63 (Hard)

*How "The First 90 Days" Scenarios 62 and 63 were built from the published public record and the project's existing research, what was drawn from each source, what was changed, and the date arithmetic for every stated date.*

**Status:** Draft documentation, for internal development and attorney review. Nothing here or in the scenarios is published or sent.

**Source rule applied:** Every scenario is a composite built only from the project's existing research: published Pennsylvania Superior Court and Commonwealth Court opinions already in the project library, official regulatory text already verified in this project, and documented system patterns across many cases. No private case, file, docket, or person from the development team's own orbit was used as source material, in any form; the private cases in the owner's orbit were excluded absolutely, as sources and as models.

**Alteration doctrine applied:** Procedural spines and testimony-textured beats come from the published sources; names, ages, occupations, facilities, and identifying facts are changed and invented, and beats from more than one published source are merged in each scenario, so no real family maps onto any character. Both families are invented composites.

**Engine-flag note (both scenarios):** The `removed` flag is deliberately **absent** from Scenarios 62 and 63. In both stories the child's placement **predates** the playable story (Scenario 62 opens on an established twice-weekly supervised-visit routine; Scenario 63 opens on an established Tuesday/Saturday visit rhythm), and no removal occurs inside either story. Setting `removed` would fire the engine's 72-hour shelter-care banner falsely. The `recordsRequested` flag is set on every winning route in both scenarios — in each, the record request is the hinge of the strategy, not a subplot.

**New law verified in this part: NONE.** Both scenarios use only the shared verified set, worded as in v1: counsel (42 Pa.C.S. § 6337; § 6332(a) is in the set but is not needed and does not appear); record release on request (55 Pa. Code § 3130.44(d) — "shall be released upon request"); 55 Pa. Code § 3130.44(f) as recorded for Scenario 62 below. The ASFA 15-of-22-months framework (42 U.S.C. § 675(5)(E)) appears **only in the strategy guides' framing**, record-dependent, exactly as Scenario 14's guide teaches it: neither scenario states a placement date, computes a 15-month date, or depicts a filing decision. No assessment in either scenario is called AI, machine learning, or predictive.

---

## SCENARIO 62 — "The Visit Notes" (26 nodes, 3 endings)

*A mother in supervised visits learns that the visit notes are the case's memory: one note calls her "flat" after a double shift and is quoted, three reviews later in story terms, as a "possible impairment concern"; another note records a climbing-frame fall as "bruise observed… mother offered no explanation initially," although she reported it immediately. Her counters are her own same-day notes, the record request, and a written correction filed into the record.*

### Documented pattern basis (from the project's existing research only)

- **Visit-note and report language hardening into findings, across the published opinions in the project library.** The recurring documented pattern these scenarios are built from is that hearings and reviews are conducted from **contemporaneous notes and forms** — testimony and reports built from what was written at the time, quoted forward from document to document. Two library anchors, already recorded in `sources-and-alterations.md` (Scenario 2's source list):
  - **J.S. v. Commonwealth, Department of Public Welfare (Pa. Cmwlth. 1989)** — a caseworker's **contemporaneous observations carried into the hearing record** years of procedure later. Drawn on for the premise: what the supervisor writes in the room is what later rooms will treat as the event.
  - **Mulholland v. Government of Berks County (3d Cir. 2013)** — the footnote recording that the caseworker, testifying years later, had **no recollection of the investigation and testified solely from the CY-48 form**. Drawn on for the complementary premise: **the file outlives memory** — which is why the parent's own contemporaneous notes, and a correction filed *into* the file, are the scenario's whole strategy.
- **55 Pa. Code § 3130.44(f) — previously verified in this project.** The use here follows the reading recorded as previously verified in this project from the 55 Pa. Code text and used in v1 (Scenario 31's research line; verbatim text recorded in `sources-batch-E.md`): the release rule is **not to be read to protect agency employees' privacy**, and it is used in Scenario 62 for exactly that and nothing more — as the answer when a supervisor's visit observations are blacked out as "staff privacy." No broader proposition about § 3130.44(f) is stated or relied on.

### Beats drawn

- The note as the case's memory; summaries quoting notes, and reports quoting summaries, with wording drifting at each quotation ("flat" → "possible impairment concern"; an explanation recorded on the note's second page never quoted).
- The minor fall at a visit, reported immediately by the parent, recorded in a form that makes the report invisible ("offered no explanation initially") — texture from the library's injury-documentation pattern (J.S.'s contested caretaker/medical characterizations), reduced to a scraped arm and kept procedural: a sleeve held, a bandage negotiated. No injury detail beyond that.
- The redacted packet and the one-line wrong date (an attended visit marked missed) — documented-pattern composites of how release packets and logs actually arrive, drawn from the project's record-request scenarios (notably Scenario 31's redaction beats), not from any single case.
- The correction filed *into* the record, so the entry and its answer travel together — the Mulholland lesson inverted: if the file outlives memory, put the answer where the file lives.

### Alterations applied

No published case in the library is a "flat visit note" case, and none is reenacted. The composite merges the library's contemporaneous-note pattern (J.S.), its file-outlives-memory footnote (Mulholland), and the project's own redaction/record-request mechanics into an invented visit-room story. Mother (Felicia), child (Ezra, 6), supervisor (Ms. Goss), and caseworker (Mr. Henley) are invented; the double shift, the climbing frame, the clock drawing, the missed-date error, and all dialogue are invented. No county, facility name, or employer is given.

### Dates audited

Story opens **Monday, July 6, 2026** (day 0; weekday machine-asserted in the generator). All 26 kickers were recomputed against the real calendar in validation. In-body dates are computed by the generator from the start date, never hand-typed, including: the "flat" visit, **Thursday, July 9, 2026** (dayOffset 3); the good visit, **Monday, July 13, 2026** (dayOffset 7); the visit wrongly marked missed, **Thursday, July 23, 2026** (dayOffset 17); the review, dayOffset 73 (**Thursday, September 17, 2026**); all three endings at dayOffset 80 (**Thursday, September 24, 2026**). Day offsets are non-decreasing along every edge (validated).

### Law used

42 Pa.C.S. § 6337 (counsel); 55 Pa. Code § 3130.44(d) (records released on request); 55 Pa. Code § 3130.44(f) (as recorded above, v1 wording only). Everything else is generic process description, uncited. ASFA (42 U.S.C. § 675(5)(E)) appears only in `strategy-62.md`'s framing paragraph, record-dependent, with no date computed.

### Withholdings

- No CPSL, expunction, or Rule 1340 proposition is used; the discovery/disclosure questions those bodies of law raise are deliberately not reached — the scenario's record route is the direct § 3130.44(d) request only.
- No placement date, and therefore no ASFA clock, is stated in the scenario data.
- The fall is kept minor and procedural by design (design.md §7): a scraped arm, reported at once; no medical dispute, no injury detail beyond that, no graphic content.
- No "removed" flag, for the reason stated in the engine-flag note above: the placement predates the story and no removal occurs in it.

---

## SCENARIO 63 — "Cancelled, Again" (29 nodes, 3 endings)

*A mother whose son's visits run Tuesdays and Saturdays at a visitation center has three visits cancelled by the center for staffing — by phone, the morning of — with make-ups offered "when there's a slot," which is never a date. The review report then reads: "family attended 60% of scheduled visits." Her counters are written confirmations, same-day written answers to every cancellation, the record request, and a corrected attendance table attached to the review packet.*

### Documented pattern basis (from the project's existing research only)

- **In re T.J.J.M. (Pa. Super. 2018)** — already in the project library and recorded in `sources-and-alterations.md` (Scenario 3's source list, Studicata summary used for fact texture only): a parent willing to engage was offered **one Saturday visit, cancelled because of the foster family's unavailability and never rescheduled**, and services were **not fitted to the parent's schedule**. Scenario 63 draws **texture and pattern only** from it — a visit cancelled because of the other side's unavailability, never rescheduled; a system whose scheduling failures land in the parent's column — and states **no holding** from it. As recorded in the project's earlier withholding, the broader reasonable-efforts framing associated with that line of cases is **not** used as law anywhere in this scenario or its guide.
- The denominator mechanics — provider cancellations folded into the family's attendance percentage, and make-up slots logged as "scheduled" without dates ever being communicated — are **likely-composite** beats under the owner's doctrine: recurring documented practice patterns (summary arithmetic built from provider logs, as in the library's visit-log textures, e.g. Scenario 3's sources) assembled into one invented center, not drawn from any single case.

### Beats drawn

- Cancellation by phone, the morning of, three times in two months; make-ups offered as "when there's a slot," never as a date (T.J.J.M.'s cancelled-and-never-rescheduled visit, re-costumed from a single offered Saturday to a recurring center pattern).
- The third cancellation arriving after the parent has already taken the bus halfway — the services-not-fitted-to-the-parent's-life texture, made literal as a spent fare (cash costs fall on the losing branches, and on the Saturday branch on every path, because the fare is spent before the call comes).
- The report line "family attended 60% of scheduled visits," and the corrected table that answers it (scheduled / cancelled-by-center / held / attended) — the project's standing lesson that a finding is a document and can only be corrected by another document.

### Alterations applied

T.J.J.M. involved a father, a single offered visit, and a different procedural posture; none of its facts, parties, or holdings is used. The composite changes the cancelling party to a visitation center cancelling for **staffing** (the documented system pattern of provider-side cancellation, generalized), triples the cancellations across two months so the *pattern* — not any one call — is the subject, and invents the denominator arithmetic whole. Mother (Simone), child (Felix, 8), and center staff (Ms. Kessler) are invented; the foster parent appears only as an unnamed voice repeating report language she heard. The center, town, and bus route are unnamed and invented.

### Dates audited

Story opens **Monday, August 3, 2026** (day 0; weekday machine-asserted in the generator). All 29 kickers were recomputed against the real calendar in validation. In-body dates are computed by the generator, never hand-typed. The **report-window arithmetic is machine-asserted in the generator**: the window from the first visit (**Tuesday, August 4, 2026**, dayOffset 1) through the third cancellation (**Saturday, September 12, 2026**, dayOffset 40) contains exactly **12** Tuesday/Saturday visits. Cancellations fall on **Tuesday, August 18, 2026** (dayOffset 15), **Tuesday, September 1, 2026** (dayOffset 29), and **Saturday, September 12, 2026** (dayOffset 40). Held visits 9, attended 9. The center's summary counts 15 "scheduled" (12 real + 3 logged make-up slots never communicated): 9/15 = 60% (asserted in code). The review report is dated dayOffset 57 (**Tuesday, September 29, 2026**), the review sits at dayOffset 60 (**Friday, October 2, 2026**), and all three endings land at dayOffset 66 (**Thursday, October 8, 2026**). Day offsets are non-decreasing along every edge (validated).

### Law used

42 Pa.C.S. § 6337 (counsel); 55 Pa. Code § 3130.44(d) (the attendance summary and scheduling log, released on request). Nothing else is stated as law; the corrected table is arithmetic, presented as such in the scenario and its guide. ASFA (42 U.S.C. § 675(5)(E)) appears only in `strategy-63.md`'s framing paragraph, record-dependent, with no date computed.

### Withholdings

- **T.J.J.M.'s reasonable-efforts framing is not used as law** (see the basis note above and the identical withholding in `sources-and-alterations.md`): the scenario teaches a documentation strategy, not a legal entitlement to make-up visits; the win ending's ordered make-ups are written as the review's response to a corrected record, not as a cited right.
- No termination grounds, no filing decision, and no appeal day-count is stated or depicted.
- No "removed" flag, for the reason stated in the engine-flag note above: Felix's placement predates the story and no removal occurs in it.

---

*Compiled for Wave H (part-file for Scenarios 62–63). Draft — not legal advice, not a depiction of any real case. Companion files: `scenario-62.json` / `scenario-62-script.md` / `strategy-62.md`, `scenario-63.json` / `scenario-63-script.md` / `strategy-63.md`, generated by `generate-scenarios-62-63.py`.*
