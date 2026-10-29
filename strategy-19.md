# Strategy Guide — Scenario 19: “The Probation Crossover”

*Game documentation for a fictional simulation in “The First 90 Days” (Tactic Watch). The family, the offices, and every instruction sheet in this scenario are invented composites. This guide is general information about how the scenario works — it is not legal advice, and it describes no real office's rules.*

## The win

**Ending — One Calendar, Two Stamps** (`end_clean`)

Be honest about its size: this is a **partial win, and the scenario says so**. What you win is the communication record. A shared written calendar prevents the one major collision — the two 10:00 a.m. appointments on Monday, October 26 — and the dependency review goes forward with both files telling the same October. The dependency case itself is not “won”: it continues on its own track, with its own questions, after the review. Nothing in this ending resolves the separate matter that has you reporting to the second office; the scenario never even describes that matter's rules. The win is that, for one month, two systems that never talk to each other were made to read from the same page — by the only person who stands in both rooms.

## The route

Verified by walking the finished choice graph. Winning path, node IDs in order:

`start → po_sheet → agency_paper → portal → records → bus_ledger → shift → confirmations → cousin → missed_call → trip → counsel_check → collision → collision_written → clean_reschedule → clean_packet → clean_night → clean_review → end_clean`

Key decision points, in order:

1. **Two Files, One Kitchen Table** (`start`) — *“Start one calendar tonight — both offices' dates on a single page, in pen.”* Sets `oneCalendar`; puts both offices' October dates on one page. Every later conflict becomes visible before it becomes an absence. All endings still open.
2. **Two Inboxes** (`portal`) — *“Make a folder — paper and phone — labelled for both offices, and save every confirmation in it from now on.”* Costs $8; sets `packetKept`. The folder becomes the timeline the review is later read from.
3. **Ask for the Record in Writing** (`records`) — *“Send the written request this week, through the agency portal and on paper, and save both confirmations.”* Sets `recordsRequested`. Both tracks that reach a review with the record in hand (`clean_packet`, `repair_packet`) depend on being able to read your own file before the court does.
4. **The Bus-Fare Ledger** (`bus_ledger`) — *“Buy the monthly pass and a paper backup calendar for your bag.”* Costs $46. Pure logistics: it removes fare arithmetic from every appointment for the rest of the month.
5. **The Shift Moves** (`shift`) — *“Send the new schedule in writing to both offices today.”* Sets `shiftWritten`; the hidden record now shows the written shift notice **in both files**, not a phone summary in one.
6. **Saturday at Your Cousin's** (`cousin`) — *“Log the overnight in both portals before you leave, with Marisol's address.”* Costs $20; sets `cousinLogged`. The same ordinary Saturday reads identically in both files.
7. **The Missed Call** (`missed_call`) — *“Send a written message through the office portal today explaining the dead phone… and mention it in writing to the agency too.”* Sets `callRepaired`. A two-hour-old problem gets a same-day written explanation in both files instead of a dated silence in one.
8. **The Family Trip** (`trip`) — *“Enter the trip in both portals before Wednesday, with the return time.”* Sets `tripWritten`. The trip enters both files as a plan — the most boring version of it, which is the best version.
9. **Ask Your Lawyer What Paper Is** (`counsel_check`) — *“Take the advice literally: a standing rule that every conflict goes to both offices in writing, the same day.”* Sets `clarificationRule`. This is the rule you will use at the gate three nodes later; adopting it before the crisis is what makes it usable during one.
10. **The Collision** (`collision`) — *“Send a written conflict notice to both offices today, attaching both schedules, and ask each for a new time in writing.”* Sets `conflictWritten`. **This is the gate.** It is the only choice at this node that keeps `end_clean` reachable; the other two route to the repair track and the scattered track respectively, permanently.
11. **The Packet Assembles Itself** (`clean_packet`) — *“Copy the folder for Ms. Hart and bring the original to the review.”* Costs $14. Cash at the ending on this route: **$102** of the $190 start.

From `collision_written` onward the clean track is a corridor — reschedule confirmations, the packet, the review — with no further forks. The game is won or lost at the collision and in the habits built before it.

## Why this wins — the law as it is supposed to work

Only two items of verified child-welfare law do any work in this scenario, and the route uses both:

- **Records on request — 55 Pa. Code § 3130.44(d).** A parent may request the case record, and it “shall be released upon request.” That is why the `records` node insists on a *written* request with saved confirmations: the released record is how you learn what the agency file actually contains — which notices arrived, which visits were logged — before a review reads it. In the clean ending's debrief, the record is what lets the court see, page by page, that both offices were told the same things.
- **Counsel — 42 Pa.C.S. § 6337.** You have the right to be represented by counsel in the dependency proceeding, and the route uses counsel (Ms. Hart) for exactly what she is for in this scenario: advice on the dependency case, a second reader of the file, and the person who carries the folder into the review.

Everything else on the winning route is **documentation and communication discipline, not a claimed legal entitlement**. No rule cited anywhere in this scenario entitles you to a rescheduled meeting, to both offices coordinating, or to a favourable review because your paperwork was tidy. Putting a scheduling conflict in writing to both offices, keeping one calendar, saving confirmations, and asking for written clarification when two instruction sheets point in different directions are habits — habits that change what the files contain, and reviews run on what files contain. The scenario deliberately asserts **no criminal-law principles at all**: the second office's instruction sheet is invented paperwork for a fictional office, and nothing in the scenario or this guide states any rule, standard, consequence, eligibility rule, or right concerning probation.

## The traps

1. **The Collision — “Call the agency, reach a person, and leave a voicemail at the probation office.”** The most tempting choice in the scenario, because it feels like communicating. It closes the win outright: you route to the repair track (`collision_partial`), the best ending left is **Ending — The Repaired Month**, and October 26 becomes a missed morning that a repair letter can contain but never erase.
2. **The Collision — “Pick the meeting that feels more urgent and simply not be at the other one.”** Choosing by instinct, documented nowhere. This closes both better endings and routes to **Ending — Two Files, Half a Month**: both files show gaps, and the next month is scheduled more tightly because the record — not the parent — failed to show up.
3. **Ask for the Record in Writing — “Ask Ms. Okafor about the record at the next visit instead.”** Skipping the written request means `recordsRequested` is never set: no stamped copy, no released record, and your first full look at your own file is the review itself. You give up the one verified tool that lets you audit the record before the court does.
4. **The small verbal defaults — “mention it by phone,” “explain afterwards,” “let it go.”** At `shift`, `cousin`, `missed_call`, and `trip`, each verbal or silent option leaves the hidden record asymmetric: one file holds a compressed summary in someone else's words, the other holds a blank. None of them feels like a decision. Together they are the difference between the clean ending's file — both offices reading the same October — and a file the review has to interrogate.

## What no strategy controls

This route controls the paper trail, and only the paper trail. It does not control whether an office answers promptly or at all, whether a caseworker compresses your words fairly in a note, which judge reads the file, or how that judge weighs a documented month against everything else in a case this scenario never shows you. The clean ending's own debrief says it plainly: the same folder, read by a different judge on a different day, could have drawn harder questions, and the same notices sent to offices having a worse week could have been answered late. Workers, judges, offices, and luck hold most of every real outcome. What the strategy holds is the one part that was ever yours — one calendar, both offices in writing, every confirmation saved — and in this scenario, that part turned out to be the part that mattered most. That is a statement about this fictional simulation, not a promise about any real case.
