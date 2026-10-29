# Strategy Guide — Scenario 9: “The Neighbor’s Couch” (Foundation tier)

*Game documentation for a fictional simulation in* The First 90 Days. *It describes choices and outcomes inside this scenario only — general information, not legal advice for any real case.*

## The win

**A Weekend With an End Date** (`end_good`) — the best ending reachable in this scenario. It is a partial, honest win: The win here is honest and modest: Sam was home Thursday, the plan closed in writing, and the file says the thing that actually happened — a voluntary plan, bounded by dates, completed as written. No court was ever involved, and none was needed.

## The route

- **The Copy You’re Entitled To** (`records`) → choose: “Ask for a written copy of the safety plan as entered” — Sets recordsRequested. Your copy of the plan is the instrument that lets you see what it does not say.
- **What’s Not in It** (`prep`) → choose: “Write down the two missing things: an end date, and a review if the repair slips” — Sets gapsNoted. The draft’s silence becomes two specific, askable dates instead of a vague unease.
- **Before the First Night** (`split`) → choose: “Ask now, plainly: end date Sunday night, review Monday if the repair slips — in the written plan” — Sets endDateAdded before the first night — the cheapest moment in the whole scenario, and the decision everything else stands on.
- **Monday, 10 A.M.** (`p2`) → choose: “Read the extension before you sign it, dates first” — Sets extensionRead. When the repair slips, the plan stretches by written dates instead of drifting — the mechanic the whole story teaches.
- **On File, Closed** (`p5`) → choose: “Sign, having read it — the line matches what happened” — The final gate: the review line says "completed as written," and your signature goes under a true sentence.

Path check: this route was walked programmatically through the scenario's choice graph (start → start → n2 → records → prep → eve → split → p1 → p2 → p3 → p4 → p5 → end_good) and reaches `end_good`. Verified at generation time; the graph validation for this scenario reported no errors.

## Why this wins — the law as it is supposed to work

- 55 Pa. Code § 3130.44(d): the safety plan is part of your case record, and your record is released on request. The route depends on that right at the exact moment it is most useful — before the plan starts, when its gaps can still be filled for free.
- A voluntary plan is, in this scenario, an agreement — and the verified principle the route operationalizes is that agreements in this system are enforced as written, by readers who were not at the kitchen table. Dates written in are honored by people who never met you. Dates left as phrases depend on everyone remembering them the same way, forever.

## The traps

- **Before the First Night** (`split`) → “Let him go on the spoken plan — everyone means well, and Monday is soon” — Costs the ending its shape. The plan has no end date or review, the repair slips, and the win survives only through the written escalation at u2 or u4.
- **Monday, 10 A.M.** (`p2`) → “Sign it quickly — it’s the same plan, just longer” — Costs the extension’s terms: you drop to the drift track at u3 having agreed, unread, to a new plan wearing the old one’s coat.
- **On File, Closed** (`p5`) → “Sign without reading — Ms. Tran has been straight with you throughout” — Closes the win at the review line: her supervisor’s wording, "extended placement, resolved," becomes the file’s memory of your weekend.
- **The Review, Eventually** (`u4`) → “Accept the verbal plan for Friday — it’s nearly over” — Declines written closure terms — so the confirmation loop misses its window and the weekend takes one more weekend from Sam.

## What no strategy controls

Ms. Abernathy was wonderful, Ms. Tran was responsive once asked in writing, and the pipe was nobody's fault — and the plan still drifted on the partial path, because drift needs no villain, only a missing date. A harder worker reads a long informal stay as a concern instead of a plumbing story; a faster plumber erases the whole problem. No strategy controls the pipe, the inspector's calendar, or the reader. It controls whether the plan your child is living under has an ending that exists outside anyone's memory.
