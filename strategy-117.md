# Strategy Guide — Scenario 117: "The Bus That Crosses the Line"

*The First 90 Days — a fictional composite. Fictional composites only; no real person or case. General information about how these hearings work, not legal advice.*

> **Route verification:** this guide's winning route was graph-walked programmatically through `scenario-117.json` (every step is a legal choice; every `requiresFlags` gate satisfied by flags accumulated earlier on the route; cash never negative). Path and totals are printed at the end.

## 1. The win

**"Ending — Same Bus, Same School"** — the full win, and the only non-partial ending of the two.

At the October 6 review, the court **assumes jurisdiction over the educational finding**: Nolan stays enrolled at Whitfield Elementary, the district's own best-interest determination — made with his mother's input — is **recorded in the order** with the factors it rested on, and transportation is ordered as a **shared cost with a written schedule**, not as a home's unpaid duty. Gina's documented requests and the plan she built are noted, and the education fight closes. Every clock a child can hear — the bus, the classroom, Mrs. Pavlik — keeps running on the same schedule as before the removal.

## 2. The route — graph-verified

The decisive beats, in walk order:

1. **Shelter Care Morning** ("The Bus That Crosses the Line") → **"Ask the judge for time to speak about school before it ends."** School goes on the record at the first hearing, while nothing has hardened.
2. **Whose Desk Does Nolan Sit At?** → **"Ask for the best-interest determination in writing, now, with her input counted."** Sets `bidRequested`.
3. **The Point of Contact** → **"Write the letter. A school placement this specific deserves a paper trail with her name on it."** Sets `pocEngaged`.
4. **The Determination** → **"Sign nothing today; present the route plan at the determination meeting on Thursday."** Sets `transportPlan` — Gina drafts the route (mileage, pickup time, the neighbor's backup) instead of accepting a transfer recommendation unopposed.
5. **The Record** → **"Ask for the agency record in writing... Under § 3130.44(d) a parent or a parent's attorney may request it."** Sets `recordsRequested` — the custodian school-opening date is hers on paper, and so is the agency's placement file.
6. **The Review** (the dispatcher) — both gate flags held (`bidRequested` + `transportPlan`), so **"Ask the court to find on the record that Nolan remains at Whitfield, with transportation ordered as a shared cost and a schedule."** is available and lands the win.

**Programmatically walked path (13 nodes):** start → office → lawyer_call → plan_visit → hearing_day → school_call → poc_letter → bid_meeting → records_node → trial_run → review_prep → review_day → end_same_bus. **Ending cash: $120 of $120 left.**

## 3. Why this wins — the law

- **School of origin is the default, not a favor.** Under ESSA, a child in foster care is to enroll in or remain in the school of origin **unless a determination is made that it is not in the child's best interest**, based on all factors including the appropriateness of the current educational setting and proximity to the school where the child was enrolled at placement — 20 U.S.C. § 6311(g)(1)(E)(i)–(ii). If the determination goes the other way, the new school must enroll immediately even without the records normally required, and contact the prior school for them — § 6311(g)(1)(E)(iii). *Newly verified from the statute's text during this run; see `sources-batch-N.md`.*
- **Transportation is a written-procedure problem, not a household's problem.** Local education agencies must collaborate with the child welfare agency, designate a point of contact, and maintain **clear written procedures** for transportation so a child found to be best served by the school of origin can stay there for the duration of the placement, with additional transportation costs handled by agency reimbursement, LEA payment, or shared cost — 20 U.S.C. § 6312(c)(5)(B). *Newly verified during this run.* Gina's route plan is what that procedure looks like from the parent's side: a specific, priced, schedulable proposal the determination can attach to.
- **The best-interest determination is where the fight is.** It is made once, early, and mostly on whoever shows up with factors. A parent who asks for it in writing, attends it, and brings the transportation answer has converted a placement-side logistics problem into a documented educational finding the dependency court can adopt.
- **Fast clocks frame the opening.** Shelter care review sits inside 72 hours (42 Pa.C.S. § 6332; 23 Pa.C.S. § 6315(d)), and counsel is a right at every stage (42 Pa.C.S. § 6337; § 6332(a)) — the lawyer call on day 2 is what makes the day-3 school ask a finding instead of a plea.
- **The record request is the spine.** Under 55 Pa. Code § 3130.44(d), a client — or the client's attorney — may ask to review and obtain copies of information in the agency record. Everything this ending rests on (custodian's opening date, the determination, the route plan) ends up citable because it was put in writing and then pulled back out of the file.

## 4. The traps

- **Signing the packet and "letting it ride"** (A Desk Readied for October → A New Desk in October (partial)): the kindergarten-roundup packet is a transfer with a friendly name. Nolan enrolls across the line; the court notes the school change as *resolved by agreement*, and the stability argument is spent for the rest of the case.
- **Asking for the determination but leaving transportation empty** (The Morning It Starts → A New Desk in October (partial)): the determination keeps Whitfield, then the route fails on a work schedule in week two and the district re-opens the question — a stability win without a funded route is a postponement.
- **Turning down the October 6 review preparation** never reaches the dispatcher with the findings assembled; preparation is what converts paper into findings.

## 5. What no strategy controls

The district's transportation budget and route availability; whether Odessa's work schedule or health holds for a school year of 5:40 wake-ups; whether the county reimburses on time; the teacher Nolan gets next year; and whether the placement itself lasts — a move farther away restarts the same determination on harder facts. The strategy controls the paper: a written determination, a funded route, an order that names both. It cannot control the road between Lititz Road and the elementary school, and this guide does not pretend otherwise.
