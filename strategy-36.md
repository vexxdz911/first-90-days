# STRATEGY GUIDE — Scenario 36: “The Whole Table” (Capstone)

*Game documentation for a fictional simulation in “The First 90 Days.” The family in this scenario is a composite; nothing here describes a real case. This guide is general information about how the scenario is built — it is not legal advice for any real case. The route below was verified by walking the finished choice graph (`scenario-36.json`) node by node.*

---

## 1. The win

**“Ending — The Whole Table, Tended (Composite State).”**

This capstone has no single-outcome endings, and the win must be read the way the data states it — as a composite state, child by child and clock by clock:

- **Jonah (8) and Wren (5):** still placed with their grandmother, Rosa — and not merely placed there, but *documented* there: the relative-placement exception is written into the case plan in particular (placement, stability, duration, child by child), which pre-answers their share of the fifteen-month date. Their track is as secure as an open case gets.
- **Maya (14):** *not* home, and not placed with family — anyone selling this ending as a clean victory is overselling it. What she has is a bent track: the long-term language is out of her goal, replaced by a family-direction paragraph; expanded time at Rosa's; a kinship assessment of Rosa's home for Maya too; and her own stated wish — “living with family for high school” — existing as a filed document instead of a memory. Open, contested, and pointed toward family.
- **The CPSL clock:** answered in time and still unresolved. The written appeal was filed on day 80 of 90, with the item rebuttal attached. No hearing has happened yet; what the filing bought is a proceeding the agency must defend — its burden, its evidence, a decision clock after the hearing. “Pending, well-built” is the honest state.
- **The dependency clock:** still running. The ASFA date — May 2, 2027 — has not arrived and has not been cancelled; it has been *answered in advance* for two of the three children and left genuinely open for the third.

That is the best reachable state in the game: nothing finished, everything filed, every track pointing the right way on paper. In this scenario's terms, that is what winning looks like.

## 2. The route

Walked and verified in the graph: `start → night1 → shelter → placements → two_homes → visits_split → payday → adj_prep → adjudication → kitchen_table → letter → clocks → bus_routes → records_arrive → school_forms → wren_birthday → grandma_track → maya_track → triage → packet → sibling_visit → visits2 → grandma_paperwork → appeal_decision → filed_node → exception_work → maya_hardens → review_full → end_whole` (cash 260 → 160; flags set along the way: `removed`, `chronologyKept`, `recordsRequested`, `itemRebuttal`, `thenVsNow`, `exceptionDocumented`, `appealFiled`).

The decision points that carry the route, in order:

1. **Monday, After School** (`start`) — *Choose: call your mother from the courthouse steps.* Sets `removed` (the engine's 72-hour clock starts from the truth: the removal happened in-story). Everything downstream — kinship, the Thursday hearing — is unlocked by treating Rosa as a resource from hour one.
2. **Thursday: The 72-Hour Hearing** (`shelter`) — *Choose: ask, on the record, that Rosa be assessed this week — not “soon.”* The expedited kinship assessment is what turns Saturday's split placement (younger two to Grandma, Maya across town) from an improvisation into the case's structure.
3. **The Geography of Your Week** (`two_homes`) — *Choose: start the chronology properly — one page per child, plus one for the case.* Sets `chronologyKept`. In a three-child case the chronology is not bookkeeping; it is the only place the whole family exists in one document.
4. **The Request That Feeds Everything** (`bus_routes`) — *Choose: write the request this week — full record, full assessment, in writing.* Sets `recordsRequested`. This single stamp feeds all three tracks: the appeal (what did they write?), the reviews (what do the ratings claim?), and Maya's page most of all. Skipping it doesn't lock a door in the graph, but it leaves the assessment unread — the direct road to “Ending — The Unread Assessment (Composite State).”
5. **The Grandmother Track** (`grandma_track`) — *Choose: draft the one-page exception memo for Jonah and Wren.* Sets `exceptionDocumented`. The memo is what converts a true fact (the little ones live with their grandmother) into the documented relative placement the statute's first exception contemplates.
6. **One Week, Two Uses** (`triage`) — *Choose: build the item rebuttal* (cash −20). Sets `itemRebuttal`. The alternative — a week of in-person presence for Maya (cash −60) — is genuinely worthy, and the scenario doesn't pretend otherwise; the rebuttal wins the tie because it is the only asset that works in rooms you aren't in, on all three children's pages at once.
7. **Late May, in Three Directions** (`visits2`) — *Choose: forward Maya's counselor email to Ms. Ferreira, with a written request attached* (cash −10). A fourteen-year-old's wish becomes a filed document. That conversion — spoken wish → dated filing — is the whole craft this capstone teaches.
8. **The Appeal, Decided** (`appeal_decision`) — *Choose: file it now, with the rebuttal and the packet attached.* Sets `appealFiled` on day 80 of 90 — three weeks inside the May 24 deadline. This is the route's single most load-bearing click: page *and* weight, filed together, while filing is still cheap.
9. **Maya's Track, Setting** (`maya_hardens`) — *Choose: bring the full board — rebuttal, packet, exception memo, Maya's filed words* → `review_full`. Then, at **The June Review: The Full Board** (`review_full`):
10. *Choose: accept this board, and work the dated task list.* Counter-intuitive and verified: demanding Maya's immediate move at this review is the trap (below). Accepting the bent track — with its dated tasks — is what reaches the win.

## 3. Why this wins — the law as it is supposed to work

Every principle below is from the scenario's verified set; the guides add no new law.

- **Shelter care within 72 hours.** When children are taken into protective custody, the shelter care hearing comes within 72 hours — Monday's removal, Thursday's hearing (42 Pa.C.S. § 6332; 23 Pa.C.S. § 6315(d)). The route uses that first hearing for the thing it can actually do: putting the kinship assessment on the record, expedited.
- **Counsel.** Parents have the right to counsel (42 Pa.C.S. § 6337); the route is built with counsel at every load-bearing step.
- **Dependency's burden, child by child.** Adjudication requires clear and convincing evidence as to *each* child — which is why the packet is built per-child and why the findings come back narrower than the agency's draft.
- **The 90-day written appeal.** A person named as a perpetrator in an indicated report may, within 90 days of being notified, request in writing that it be amended or expunged (23 Pa.C.S. § 6341(a)(2)). Computed in this scenario: notice Monday, February 23, 2026 → deadline **Sunday, May 24, 2026**. The route files on day 80, with weight attached — before the window is a threat.
- **At the CPSL hearing, the burden is the agency's** — proof by substantial evidence that the report should remain indicated (23 Pa.C.S. § 6341(c.2)(5)) — and **the agency must produce all the evidence it gathered, including anything that helps you** (23 Pa.C.S. § 6341(c.2)(4)). A decision follows within 45 days of the hearing's close (23 Pa.C.S. § 6341(c.3)). Filing the appeal is what makes all of that owed to you.
- **Your record, on request — assessment included.** Case records “shall be released upon request” (55 Pa. Code § 3130.44(d)). Where the assessment is invoked through adjudication-phase disclosure (Pa.R.J.C.P. Rule 1340(B)(1)), the scenario's standing flag applies: the assessment approach is untested, so its item ratings are claims — and claims can be answered item by item, which is exactly what the rebuttal does.
- **The 15-of-22 clock and its exceptions.** At 15 of the most recent 22 months in care, a termination filing is generally expected unless an exception fits — relative placement, a documented compelling reason, or services identified but not provided (42 U.S.C. § 675(5)(E)). Computed here: placement February 2, 2026 → **May 2, 2027**. The route's insight is the statute's texture: the relative-placement exception is *live by the facts* for Jonah and Wren from the first Saturday — but it only protects them once it is **documented in particular**. Truth plus paper is the exception; truth alone is a hope.

## 4. The traps

Each trap was checked against the graph: from the trap's subtree, the win is unreachable.

1. **“Wait — two more weeks of packet-polish will make it undeniable”** (`appeal_decision` → `wait_risk`). The most tempting choice in the capstone, because the packet really does get better. From `wait_risk` the only endings reachable are “Ending — Two Clocks Held, One Track Hardening” (via a bare, last-edge filing) and **“Ending — The Window That Closed Quietly (Composite State)”** — one more day of polish past May 24 and the appeal, the hearing, and the agency's burden all cease to exist. Cost: an entire legal track, traded for cleaner copies.
2. **Demanding Maya move to Rosa's this month** (`review_full` → “Push further at this review”). It feels like advocacy and reads like it in the transcript. The graph is blunt: it cools the room and lands on **“Ending — Two Clocks Held, One Track Hardening (Composite State)”** — the judge declines to leapfrog the kinship assessment, and the board you keep is the partial one.
3. **Bringing only the exception memo and the folder as it stands** (`maya_hardens` → `review_norecords`). The younger two's paper is impeccable, which makes this feel safe. From `review_norecords` only **“Ending — The Unread Assessment (Composite State)”** is reachable: Maya's track is decided by ratings nobody on your side ever read closely enough to answer.
4. **Filing the appeal bare** (`appeal_decision` → “File the page now, bare”). The near-trap, stated honestly: it does *not* lock the win in the graph — the clock is stopped, and the full board can still be brought to the June review. What it costs is weight at the hearing the page buys: a record that starts as one page, against a file that starts as a winter. The route files page and weight together because “supplement it later” is, in this family's experience and in this graph's other branches, the most dangerous sentence in the system.

## 5. What no strategy controls

Rosa's steadiness is not a strategy; it is a grandmother. Mrs. Bell's decency, a school counselor who bothered to write an email, a judge who worked the case child by child — none of these were chosen at any decision point, and a different draw of any of them changes the board. The CPSL hearing hasn't happened in the winning state, and a hearing officer could weigh the same rebuttal and keep the report indicated; Maya's kinship assessment could come back with conditions nobody predicted; the 2027 clock will keep its own counsel regardless. Workers, judges, and luck hold real pieces of every ending in this scenario, including the best one. What the route controls is sequence and documentation — the page before the polish, the file before the rebuttal, the exception written down before the date it answers. In a case with three children and three clocks and one pair of hands, the order you do things in is not a detail of the strategy. It is the strategy.
