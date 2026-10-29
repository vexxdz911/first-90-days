# Strategy Guide — Scenario 121: "The Meeting That Happened Without Her"

*The First 90 Days — a fictional composite. Fictional composites only; no real person or case. General information about how these hearings work, not legal advice.*

> **Route verification:** this guide's winning route was graph-walked programmatically through `scenario-121.json` (every step is a legal choice; every `requiresFlags` gate satisfied by flags accumulated earlier on the route; cash never negative). Path and totals are printed at the end.

## 1. The win

**"Ending — Nineteen Miles, Funded"** — the full win.

The reconvened best-interest determination — held with the father present, the teacher heard, and the transportation math on the table — finds for Alina's school of origin, and the October 15 review **orders the transportation funded**: $612 a month through inter-agency cost sharing while Alina is placed, so Wilma is a grandmother again instead of a route. The court expressly addresses permanency progress and the ASFA clock under 42 Pa.C.S. § 6351(f)(9) and declines to start a filing while the plan is working. The honest labeling the data carries: the school fight is won completely; the *case* is not over, and the guide says so in section 5. Two partials flank it — the school kept on an unpaid grandmother's labor (partial), and a fair meeting that still moves her (partial) — plus the unconsulted transfer.

## 2. The route — graph-verified

1. **The Paper Trail of September First** ("The Determination She Never Attended") → **"Do not sign it."** Declining to endorse a determination made without him preserves the objection.
2. **The Objection** → **"Send the objection tonight. The September 21 date gets an opponent with a timestamp."** Sets `bidObjected` — the objection lands before the transfer's effective date, in writing, to district and agency.
3. **The Agency Record** → **"Ask for the agency record in writing... Under § 3130.44(d)..."** Sets `recordsRequested` — the agency's own note ("placement distance noted; school impact to be addressed at review") becomes an exhibit.
4. **The District's Point of Contact** → **"Say it plainly. A district that hears its procedure criticized by its own parent usually fixes the procedure."** The district concedes the notice failure and re-offers the meeting.
5. **The Reconvened Determination** (Friday, September 18) → **"Present it whole. Every factor, every document, every dollar."** The teacher's projected-midyear-transfer testimony, Wilma's alarm-clock statement, Alina's letter, and the priced route go into one determination record.
6. **The Math** → **"Put the gap in writing to both agencies."** The $612 figure, the cost-sharing frame, and the duration limit are in two inboxes before the review.
7. **The Review** (dispatcher: `bidObjected` + `transportFunded`) → **"Ask the court to order the transportation funded and to note the father's objection and the reconvened determination in the findings."**

**Programmatically walked path (28 nodes):** start → backstory121 → wilma_call → bid_reveal → gal121 → lawyer121 → objection_sent → records121 → vadnais_letter → district_poc → bid_paper → teacher_call → wilma_statement → alina_voice121 → bid_date → transport_math → pre_bid_prep → bid_day → bid_outcome_fork → post_bid_origin → first_bus_week → math_team → route_bill → wilma_tired → review_prep → anselmi_findings → review_day → end_origin. **Ending cash: $136 of $160 left.**

## 3. Why this wins — the law

- **School of origin is the statutory default, and the determination is the whole ballgame.** A child in foster care remains in the school of origin unless a determination is made that it is not in the child's best interest, based on all factors including appropriateness of the current educational setting and proximity to the school attended at placement — 20 U.S.C. § 6311(g)(1)(E)(i)–(ii); if not in the child's best interest, the new school enrolls immediately and obtains records from the prior school — § 6311(g)(1)(E)(iii). *Newly verified from the statute's text during this run; see `sources-batch-N.md`.* A determination made without the parent is not attacked here as void — no authority for that proposition was verified — it is attacked as *incomplete on its own terms*: a factor-weighing that never heard the teacher, the child, or the transportation plan did not weigh the factors the statute lists. The cure the scenario wins is the statute's own cure: a real determination.
- **Transportation has an assigned owner: the written procedure.** LEAs must collaborate with the child welfare agency and maintain clear written procedures for transportation to the school of origin, with additional costs handled by agency reimbursement, LEA payment, or shared cost — 20 U.S.C. § 6312(c)(5)(B). *Newly verified during this run.* The $612 route is priced against that frame, which is why the court can order funding as administration rather than as charity.
- **Permanency findings discipline the long game.** At review the court reports whether the child has been in placement 15 of the last 22 months and addresses the filing consequence and its exceptions — 42 Pa.C.S. § 6351(f)(9), (f.1), tracking 42 U.S.C. § 675(5)(E). Alina entered care August 10, 2026; the 15-month date is November 10, 2027. Naming the clock early is what lets the education win compound instead of being overrun by it.
- **The record request is the spine.** Under 55 Pa. Code § 3130.44(d), the father or his attorney may obtain the agency record — the placement note that deferred the school question "to review" is the exhibit that makes the review answer it.

## 4. The traps

- **Kept, on a Grandmother's Alarm Clock (partial)**: winning the determination and accepting the unfunded route. Alina keeps her school; Wilma absorbs $500 a month of driving on a fixed income; the court's findings credit "family support" for what a statute assigns to a written procedure. The first breakdown — a surgery, a transmission — reopens everything from weakness.
- **A Fair Meeting, a New School (partial)**: the reconvened determination is scrupulously fair and still finds the burden too great, because the transportation answer arrived as testimony instead of a funded commitment. Alina transfers with dignity, records in hand (§ 6311(g)(1)(E)(iii) doing its work) — and loses the math team, the teacher, and the bus route anyway. Fairness of process is not the same as the outcome the factors supported.
- **Enrolled on a Tuesday**: signing the September 1 summary, or never objecting in writing, lets the transfer execute on schedule; the October review "notes" a school change that no one is ordered to undo.

## 5. What no strategy controls

Whether Alina comes home — the dependency case turns on the original safety concerns, not on the school fight, and this scenario deliberately wins the education question while the case continues. Wilma's health and car across a school year; the district's transportation budget in the next fiscal year; a placement move that changes the 19 miles into 40; and the November 2027 clock, which excellent school findings slow but do not stop. The strategy controls the determination's completeness and the route's funding. It cannot control the road, the budget year, or the underlying case, and this guide does not pretend otherwise.
