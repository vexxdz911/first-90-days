# Strategy Guide — Scenario 88: "Thirty Days"

*Game documentation for a fictional simulation in "The First 90 Days" (Tactic Watch). The family, the case, and every choice below are fictional. This guide is general information about how the scenario is built — it is not legal advice for any real case.*

## (1) The win

**Best ending: "Filed on Time, Fed on Saturdays."**

State it honestly: this is a **partial** win. The notice of appeal was filed well inside its window, the appeal is docketed and being briefed from a complete record, and Tomek's case below is being fed with visits and filed paper. No judge has ruled on anything. There is no ending in this scenario where the Superior Court decides — the scenario's subject is the thirty days in which appeals are made possible or impossible, and the win is that nothing in them was wasted.

## (2) The route

Verified by walking the scenario graph from the start node (see the verification note at the end). Key decision points, in order:

1. **The Order in the Mail** — *Call the lawyer's office today and say the word "appeal" out loud.* Sets **calledDayOne**. Hallway remarks are weather; a dated message slip is climate.
2. **The Message Slip** — *Ask for the earliest appointment on the calendar, not a callback.* Sets **appointmentSet**. (The callback route costs eight days and arrives at the same office with a thinner file — see the traps.)
3. **Mr. Osei Counts Out Loud** — *Agree the plan: file within the week, order the transcript, request the complete record in writing.* Cash −20 (you finish with $100 of the $120 start). Sets **appealPlan** and **recordsRequested**. The plan is one page with three dates — the strategy, entire.
4. **Paper, Ordered** and **Saturday, With a Missing Tooth** — keep the visit, and ask in writing for the visit note to record the make-up reading. Sets **visitKept**, **visitLog**. The case below does not pause for an appeal, and its record is the one the family actually lives in.
5. **Signing Day** — *Sign the notice of appeal.* Flag-gated on **appealPlan**: the notice exists as a document because the plan produced it; the choice to take it home for a weekend exists on the other branch and spends the cushion for nothing.
6. The stamp, the docket number, and the continuing reviews below follow. The transcript and the complete agency record — ordered at step 3 — are what the brief will be built from.

## (3) Why this wins — the law as it is supposed to work

Only principles from the scenario's verified set are stated here:

- **The clock is Pa.R.A.P. 903(a):** the notice of appeal must be filed within 30 days after the entry of the order appealed from. This batch verified the rule's text from the official Rules of Appellate Procedure (210 Pa. Code Ch. 9). The order here was entered Monday, April 6, 2026; the deadline was Wednesday, May 6, 2026; the route files three weeks early because paper filed early can be fixed and paper filed at the deadline can only be late.
- **An untimely notice is not a curable defect.** The failure to file a timely notice implicates the appellate court's jurisdiction; the "Day Thirty-One" ending states the consequence the lawyers in the story state — the order stands, unreviewed, regardless of the arguments nobody filed.
- **The record request is 55 Pa. Code § 3130.44(d)** — released upon request — and counsel's presence is 42 Pa.C.S. § 6337's. Nothing else in the route is law. The rest is calendaring, which is the point: at this tier, the appellate skill being taught is a phone call made on day one.

## (4) The traps

1. **Leaving it at the callback at "The Message Slip."** Cost: eight days and the day-one appointment note. The compressed plan that follows (day eleven) still wins — this trap is a tax, not a death — but the scenario is honest that the tax is paid in margin the family may need for a later surprise.
2. **"Sometime this month" at the records step.** No transcript, no complete record; the notice can still be forced out the door in time (the route through "Sometime This Month" files it), but the appeal is briefed half-blind — and the same node carries the story's true loss: choosing *"let the office file it when they file it"* walks straight to day thirty-one and "Day Thirty-One," the ending in which the order becomes final while everyone involved was being reasonable.
3. **Taking the notice home for the weekend at "Signing Day."** Filed day twenty-one via the late receipt — alive, margin halved. The plan beat the clock; the weekend nearly un-beat it.

## (5) What no strategy controls

The panel's eventual reading, the lawyer's other emergencies, the clerk's backlog, an aunt's patience, a six-year-old's rate of tooth loss. The route controlled the appointment, the plan, the papers, and the Saturdays. A deadline does not measure a parent; it measures a filing. The whole strategy is to make the filing early, boring, and complete — and to keep being a father, on paper, in the case that never paused.

---
*Verification: this route was walked programmatically against `scenario-88.json` — each named choice was followed from the start node in order; every intermediate node and choice exists; the flag-gated signing choice's requirement (appealPlan) was satisfied by flags set earlier on the walk; the walk terminates at the ending node titled "Filed on Time, Fed on Saturdays" after visiting 11 nodes, with $100 of the $120 starting cash remaining.*
