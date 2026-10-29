# Strategy Guide — Scenario 65: "Two Plans"

*Game documentation for a fictional simulation in "The First 90 Days" (Tactic Watch). The family, the case, and every choice below are fictional. This guide is general information about how the scenario is built — it is not legal advice for any real case.*

## (1) The win

**Best ending: "Ending — Two Files, Two Records."**

State it honestly: this is a **partial** win. The schedules are de-conflicted in writing, each review report is corrected to its own parent, and both plans are on track. Hattie is **still placed** at the curtain. Nothing about placement was decided, and the conflict this scenario resolves was never the marriage — it was the paperwork: two plans that had never read each other, and two files that kept absorbing each other's worst lines.

## (2) The route

Verified by walking the scenario graph from the start node (see the verification note at the end). The full walked route, with decision points explained:

1. **Two Plans, One Kitchen Table** → **Two Lawyers, Explained at the Table** — two parties, two plans, two workers (hers: Ms. Whelan; his: Mr. Murdock), one car. Each parent has their own counsel (42 Pa.C.S. § 6337).
2. **Two Binders or One Shoebox** — *Give each plan its own binder, its own folder, its own color of tab.* Cash −8. Sets **ownFolder**. → **House Rules for Paper** → **The Collision Calendar** — the traps are named before they spring: his Tuesday-evening group vs. her only Tuesday make-up visit slot; her Friday-morning screens vs. his Friday class check-in across town; one car.
3. **Letters to Two Workers** — *Send the written de-confliction request to BOTH workers, a copy for each file.* Cash −4. Sets **deconflictLetter**. → **The Workers Reply — or Don't** → **One Car, Honestly Described** → **The Bus Plan, Written Down** → **Friday, the First Time** → **His Tuesday Group** — the collisions are survived, logged, and on record as predicted logistics rather than discovered non-compliance.
4. **The Week Everything Lands at Once** → **The Missed Screen** → **The Reschedule, Kept** — his miss: the car on a lift, a same-day call, a rescheduled screen kept clean. The loop closes in his folder.
5. **A Line in the Wrong Report** — the bleed, found in her report: his missed screen summarized as "the household's" complication. → **The Tuesday That Tests the Calendar** → **What Tuesday Wrote** — the de-conflicted slot absorbs the make-up visit.
6. **Asking for Both Files** — *Both of you sign and send your own records requests this week.* Cash −6. Sets **recordsRequested**. Each parent requests only their own file — neither can request the other's — so both requests happen by design.
7. **Reading Each Other's Paper** → **The Kitchen-Table Audit** → **The Late Visit Note** — *Get the visit center's own log entry for that day, in writing.* Cash −4. Her "late visit" in his file was the center's early closing; the log proves it. → **Two Desks, Visited in Person**.
8. **Separating the Records, in Writing** — *File the written correction with BOTH workers, copies in both folders.* Cash −6. Sets **correctionFiled** — filed before the review reports are written. → **The Acknowledgments**.
9. **The Joint Visit** — *Ask, in writing, that the joint visit be noted in both files.* Cash −3. The visit went well and was noted in only one file; the absence is corrected like an error. → **One Sentence, Requested Twice** → **One Letter, Two Signatures, Through Counsel** — *Sign the joint letter through counsel.* Cash −6. Sets **jointLetter**.
10. **Two Jobs, One Payday Problem** → **Payday Arithmetic, Twice** → **Hattie, at the Visit** → **Two Reviews, One Week** → **Her Counsel, Her Folder** → **His Counsel, His Folder** — two folder audits, each checking that the folder contains only its owner's life.
11. **The Reviews** — *Both reviews are argued from the separated records.* This choice is flag-gated: **deconflictLetter** + **correctionFiled** + **recordsRequested**. It leads to **Ending — Two Files, Two Records**.

## (3) Why this wins — the law as it is supposed to work

Only principles from the scenario's verified set are stated here:

- **Two parties, two records.** Each parent is a party with their own right to counsel (42 Pa.C.S. § 6337) and their own case plan. Reviews are argued from reports, and reports are written from files — so which file a fact sits in is not housekeeping; it is the evidence each parent will be judged by.
- **Each parent's record is theirs on request** — 55 Pa. Code § 3130.44(d) ("shall be released upon request"). The right belongs to each parent for their own file, which is why step 6 requires two requests, not one: the bleed is only visible when both files are on the same table.
- **Corrections are timing instruments.** A written correction filed before reports are drafted changes the reports. The same correction filed after a review has relied on the bleed changes only the future — the difference between this scenario's best ending and its middle one is a date, not an argument.

## (4) The traps

1. **Absorbing the collisions at "Letters to Two Workers"** (no **deconflictLetter**). The Tuesdays and Fridays still collide — now unannounced. Even with the correction filed, the reviews gate closes the best ending: the route lands at **Ending — Untangled, Late**, because a review has already relied on the bleed and the calendar was never repaired in writing.
2. **Skipping the records requests at "Asking for Both Files"**. The bleed stays a suspicion about one stray paragraph instead of a mapped, correctable set of lines. Corrections attempted from summaries are thinner, later, or never filed.
3. **Raising the bleed orally at "Separating the Records, in Writing"** (no **correctionFiled**). Voices in a room, against reports already drafted from the uncorrected files. Both review-gate choices that require the filed correction close, and the route ends at **Ending — One File, Shared Blame**: each parent's record permanently carries the other's worst line.
4. **The shoebox at "Two Binders or One Shoebox"** (no **ownFolder**). Not itself fatal — but the household that cannot tell its own paper apart cannot audit the agency's, and every later correction is built on sand.

## (5) What no strategy controls

Whether two conscientious workers cross-check each other's files themselves (in another week, they might, and the bleed never forms); whether a supervisor reads both files side by side and untangles them unaided; the visit center's staffing closures; the car's brake line. Workers, judges, employers, and luck hold pieces of every ending here. The route controls only the structural repairs: collisions named in writing before they happen, each record requested and read, the bleed separated on paper before the reports were written. It does not grade either parent — the scenario's whole point is that the failures it depicts belong to the paperwork, not to the people inside it.

---
*Verification: this route was walked programmatically against `scenario-65.json` — each named choice was followed from the start node in order; every intermediate node and choice exists; the flag-gated review choice's requirements (deconflictLetter + correctionFiled + recordsRequested) were satisfied by flags set earlier on the walk; the walk terminates at the ending node titled "Ending — Two Files, Two Records" after visiting 35 nodes, with $153 of the $190 starting cash remaining. Walked path: start -> separate_counsel -> two_binders -> paper_habits -> calendar_beat -> deconflict_beat -> reply_week -> car_beat -> bus_plan -> screens_beat -> program_night -> his_miss_setup -> his_miss -> reschedule_kept -> her_report -> visit_makeup -> makeup_outcome -> records_beat65 -> file_arrives65 -> kitchen_audit -> her_note_his_file -> two_desks -> correction_beat -> ack_beat -> joint_visit -> note_followup -> joint_letter_beat -> work_beat65 -> money_beat65 -> hattie_beat -> prep_split -> counsel_prep_her -> counsel_prep_his -> reviews_week -> end_two.*
