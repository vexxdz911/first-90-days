# Strategy Guide — Scenario 135: "Four Seasons"

*Game documentation for a fictional simulation in "The First 90 Days" (Tactic Watch). The family, the case, and every choice below are fictional. This guide is general information about how the scenario is built — it is not legal advice for any real case.*

## (1) The win

**Best ending: "Ending — The Goal Survives."**

This is a **partial** win, labeled so by the house rule: the goal survives intact for all three children, the exceptions are adopted, the trial converts, the children are home — after fifteen months. The strategy's triumph is documentary and total; the year is nonetheless spent, and the guide refuses to call that anything but partial. It is the best possible outcome the documented situation allows.

## (2) The route

Verified by walking the scenario graph from the start node (see the verification note at the end). Key decision points, in order — node title, winning choice, and what it changes:

1. **September, Three Times** — *Start the compendium now: one binder, three sections, every date from day one* Sets **compendiumStarted**.
2. **Ms. Mendieta's Wheel** — *Do the paper version: dated, copied, filed* Cash −$5; Sets **paperTrail**.
3. **Three Sections, Two Clocks** — *Carry the page to its file* Cash −$5; Sets **paperTrail**.
4. **The First Pages** — *Carry the page to its file* Cash −$5; Sets **paperTrail**.
5. **Fall: The Services Begin** — *Log every enrollment and every waitlist date in the compendium, monthly* Sets **waitsLogged**.
6. **October's Enrollment Letters** — *Carry the page to its file* Cash −$5; Sets **paperTrail**.
7. **The Cousin's September** — *Carry the page to its file* Cash −$5; Sets **paperTrail**.
8. **Fall: The Visits Find Their Rhythm** — *Reconcile both placements' notes into the compendium monthly* Sets **notesReconciled**.
9. **November's Reconciliation** — *Carry the page to its file* Cash −$5; Sets **paperTrail**.
10. **December at Two Placements** — *Carry the page to its file* Cash −$5; Sets **paperTrail**.
11. **Winter: The Therapy Gap** — *Write the gap letter: plan date, referral date, vacancy — filed, with both dates attached* Cash −$5; Sets **gapDocumented**.
12. **The Vacancy, Confirmed** — *Carry the page to its file* Cash −$5; Sets **paperTrail**.
13. **Winter: The Record, Requested** — *File the corrections as dated pages and index the mirror against the binder* Sets **recordsRequested**.
14. **The Mirror's Gaps** — *Carry the page to its file* Cash −$5; Sets **paperTrail**.
15. **Corrections, Filed as Pages** — *Carry the page to its file* Cash −$5; Sets **paperTrail**.
16. **Winter: The Review** — *Do the paper version: dated, copied, filed* Cash −$5; Sets **paperTrail**.
17. **February's Applications** — *Carry the page to its file* Cash −$5; Sets **paperTrail**.
18. **The Children's Winter Pages** — *Carry the page to its file* Cash −$5; Sets **paperTrail**.
19. **Spring: The Housing Answer** — *Get every element in writing, on letterhead, dated — and file them together* Cash −$5; Sets **housingLetter**.
20. **Spring: The Children's Pages** — *File the children's pages in the compendium and the case record* Sets **chorusFiled**.
21. **The Landlord's Conditions** — *Carry the page to its file* Cash −$5; Sets **paperTrail**.
22. **The Answer, Assembled** — *Carry the page to its file* Cash −$5; Sets **paperTrail**.
23. **Spring: The Review** — *Do the paper version: dated, copied, filed* Cash −$5; Sets **paperTrail**.
24. **June's First Assembly** — *Carry the page to its file* Cash −$5; Sets **paperTrail**.
25. **The Trial, Proposed on Paper** — *Carry the page to its file* Cash −$5; Sets **paperTrail**.
26. **Summer: The Exceptions, Built** — *Assemble the exception section child by child, each with its own dates* Cash −$10; Sets **exceptionsBuilt**.
27. **Each Child, Their Own Page** — *Carry the page to its file* Cash −$5; Sets **paperTrail**.
28. **The Compendium, Closed for Building** — *Rule the compendium complete and index it for the fall* Sets **compendiumBuilt**.
29. **Summer: The Trial Begins** — *Document the trial's stages in the compendium as they happen* Sets **trialDocumented**.
30. **Nico's Packet** — *Carry the page to its file* Cash −$5; Sets **paperTrail**.
31. **The Second Fall** — *Answer the position in writing: exceptions documented per child, trial running, housing letter attached* Cash −$5; Sets **positionAnswered**.
32. **The Hearing Where the Goal Is the Question** — *Ask for the order: goal unchanged, trial to convert, exceptions as documented per child* This choice is flag-gated: it is only available with **recordsRequested** + **gapDocumented** + **compendiumBuilt** + **housingLetter**.

Supporting choices along the same walk — every "paper version" choice (dated, copied, filed), every written request, and every dated letter — add the documentation the packet is later assembled from. The full walked path is printed in the verification note.

## (3) Why this wins — the law as it is supposed to work

- **Per-child clocks across a wheel of a year.** Elders entered September 1, 2025 → fifteen months Tuesday, December 1, 2026; Nico entered September 29, 2025 → Tuesday, December 29, 2026 (42 U.S.C. § 675(5)(E)). The scenario's length is its lesson: the dates that decide the case are visible from day one, and the strategy is simply a year spent walking toward them with a binder.
- **Waits are facts.** The therapy gap (plan October, referral January) becomes the services-not-provided exception only because it was logged monthly and lettered in its own season. Undocumented gaps are charged to the parent; documented ones are charged to their true owner.
- **The compelling reason must live in the case plan.** The summer exception section — per child, per exception, each with dates — is the scenario's core mechanic, built *before* the agency's position made it necessary. The record request (§ 3130.44(d)) reconciles the mirror against the binder mid-year, when corrections are still cheap.
- **Housing answers are documents.** Projection + confirmation + landlord commitment, dated and filed together, convert the case's open wound into a treatment plan a hearing can adopt. Counsel (42 Pa.C.S. § 6337) supplies the wheel; the parent supplies the keeping.

## (4) The traps

1. **Deferring the binder — 'get through the first month first'** — the first month is the part no one can reconstruct in month thirteen. The compendium's gate flag (**compendiumBuilt**) is earned by a year of monthly keeping, and the win requires it.
2. **Raising the therapy gap orally at the winter review** — unfiled gaps are attributed to the raiser at the hearing. The letter, with both dates, is the exception's first brick.
3. **Asking for a December continuance 'to strengthen the record' at "The Second Fall"** — December is the clock's address, not a neutral month. That choice walks directly into the December ending.
4. **Answering the goal question with a speech instead of the compendium** — hearings reward binders and punish speeches — the goal-changed ending is the receipt.

## (5) What no strategy controls

The housing market, the provider's staffing, the cousin's surgery, and a judge's instinct for compromise. The route controlled the keeping: monthly reconciliation, seasonal letters, summer exceptions, and the mirror checked while corrections were cheap.

---
*Verification: this route was walked programmatically against `scenario-135.json` — each named choice was followed from the start node in order; every flag-gated choice's requirements were satisfied by flags set earlier on the walk; the walk terminates at the ending node titled "Ending — The Goal Survives" after visiting 33 nodes, with $65 of the $190 starting cash remaining. Walked path: September, Three Times → Ms. Mendieta's Wheel → Three Sections, Two Clocks → The First Pages → Fall: The Services Begin → October's Enrollment Letters → The Cousin's September → Fall: The Visits Find Their Rhythm → November's Reconciliation → December at Two Placements → Winter: The Therapy Gap → The Vacancy, Confirmed → Winter: The Record, Requested → The Mirror's Gaps → Corrections, Filed as Pages → Winter: The Review → February's Applications → The Children's Winter Pages → Spring: The Housing Answer → Spring: The Children's Pages → The Landlord's Conditions → The Answer, Assembled → Spring: The Review → June's First Assembly → The Trial, Proposed on Paper → Summer: The Exceptions, Built → Each Child, Their Own Page → The Compendium, Closed for Building → Summer: The Trial Begins → Nico's Packet → The Second Fall → The Hearing Where the Goal Is the Question → Ending — The Goal Survives.*
