# Strategy Guide — Scenario 23: "The Hospital Hold"

*Game documentation for a fictional simulation in "The First 90 Days" (Tactic Watch). The family, the choices, and the outcomes below exist only in this scenario. This is general information about how the simulation is built — not legal advice for any real case.*

*Route verified by walking `scenario-23.json` programmatically from `startNode` through the choices named below: the walk reaches the named ending in 12 nodes, with every intermediate node and choice present in the data.*

## (1) The win

**Ending — Home With a Safety Plan, One Case, Not Two** (`end_home`).

Stated honestly: the baby comes home under a written safety plan, with agency oversight that steps down on a date certain — she is not discharged to the mother alone, the grandmother is a named part of the plan, and the file closes only after the plan is lived. What makes it the win is comparative: no custody order was ever signed, no shelter care hearing was ever needed, and the older child was never drawn into a case at all. The best outcome in this scenario is that most of the system never has to happen.

## (2) The route

1. **The First Paperwork** ("The First Paperwork") — *Ask for copies of everything, and get Rosa's discharge plan in writing, signed, before anything else is signed.* Sets `planWritten`; hidden item records the signed day-zero plan naming the grandmother. This single choice is the scenario's hinge: it routes the story onto the plan track, where the agency's next step is to *check* the plan instead of replacing it. The other two choices at this node both set the `removed` flag and put the baby in the agency's custody on day zero.
2. **The Plan, Checked** ("The Plan, Checked") — *Ask Mr. Osei to note, in writing, that June's placement with Rosa predates today and is stable.* Hidden item places the older child's pre-existing, stable arrangement in the agency's own notes on day 1 — the sentence later questions about the sibling have to argue with.
3. **Asking for the Records, Week One** ("Asking for the Records, Week One") — *Sign and send both requests — hospital records and agency records.* Sets `recordsRequested`. It unlocks **What the First File Says**, where the mother reads the agency's early, accurate sentence about her older child ("no concerns identified at this time") while the file is still short enough to manage.
4. **Discharge Day** ("Discharge Day") — *Keep every appointment sheet and hand Rosa a copy of each, the day it happens.* Two folders, kept current: the plan's promises stay checkable against the house.
5. **The Home Visit, and June's Question** ("The Home Visit, and June's Question") — *Give him June's school and doctor letters, in writing, for her own page in the file.* Sets `juneRecord`; hidden item documents the older child's status. This is the beat that keeps the baby's case from becoming the sibling's case: June's page now argues for itself at the agency review.
6. **The Agency Review — Plan Track** ("The Agency Review — Plan Track") — *Ask for the step-down in writing, with its date.* Leads through **Step-Down, Dated** to the win (cash −15 on the final choice).

If the day-zero paper goes the other way, the best reachable outcome changes: on the court track, the equivalent discipline (written plan built for the hearing, records requested before it, treatment attended *and documented*, June's letters handed over at the sibling meeting) reaches **Ending — Placed Short-Term, With a Dated Path Home** — a real, respectable result that still costs the family weeks the plan track never spends.

## (3) Why this wins — the law as it is supposed to work

- A parent may request the case record, which "shall be released upon request" (55 Pa. Code § 3130.44(d)). The route uses the right in the first week — for the hospital record and the agency record, and for *both* children — so the mother manages the case knowing what the file says about each child.
- The parent has the right to counsel, including appointed counsel (42 Pa.C.S. § 6337). On the winning route counsel is barely needed; on the court track she is the person who converts a grandmother's kitchen-table readiness into a plan a judge can weigh at the hearing.
- A child taken into custody is entitled to a shelter care hearing within 72 hours (42 Pa.C.S. § 6332; 23 Pa.C.S. § 6315(d)). In this scenario that clock is honest by construction: on the court track, custody is taken on day 0 (Monday, January 12, 2026) and the hearing falls on day 3 (Thursday, January 15, 2026). The win consists partly in never needing that protection — because a written plan existed before anyone asked a court for custody, the emergency machinery was never switched on.

## (4) The traps

- **Signing the forms as they are handed to you** at "The First Paperwork." Four minutes of cooperation that sets the `removed` flag, puts the newborn in agency custody on day zero, and starts the 72-hour clock — after which the family is asking a court for its own baby back instead of having the agency check a plan.
- **The warm conversation with no paper** (the third choice at the same node). Identical legal result to signing blind: a grandmother who is ready in fact but absent from the record cannot be weighed at a hearing three days later.
- **Answering June's questions verbally** at "The Home Visit, and June's Question." Nothing goes wrong for the baby — but June's thin page pushes the agency to seek court oversight anyway, converting the win into the short-term placement ending.
- **Agreeing to sibling services without asking for the basis in writing** (court track, "Does the Baby's Case Reach June?"). It feels like the cooperative move; it writes "family receiving services" as the first sentence of a five-year-old's file and produces **Ending — Baby Placed, and a Sibling Drawn Into Services**.
- **Choosing the visit over the documented intake** (court track). A missed, unexcused, undocumented appointment reads in the file as disengagement, and is the first step on the road to **Ending — The Paper Trail That Was Never Built in Time**.

## (5) What no strategy controls

That a report is made at the hospital at all; which worker arrives and whether he slows down when a mother asks for copies; the judge assigned if custody is taken; scheduling systems that set a mother's treatment intake against her newborn visits; and the grandmother herself — her proximity, her health, her spare bassinet, her fridge rules. The same mother with a grandmother two counties away signs different forms on day zero and lives a different month. Outcomes in this scenario turn on workers, judges, hospital routines, and luck as well as on the parent. The route above controls only what is written down, and when — which, in the first week of a case, happens to be most of what the later weeks are made of.
