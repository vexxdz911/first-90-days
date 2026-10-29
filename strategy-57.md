# Strategy Guide — Scenario 57: "The Referral That Never Came"

*Game documentation for a fictional simulation in "The First 90 Days" (Tactic Watch). The family, the case, and every choice below are fictional. This guide is general information about how the scenario is built — it is not legal advice for any real case.*

## (1) The win

**Best ending: "Ending — Engaged, On Paper."**

State it honestly: this is a **partial** win, and it is the best this scenario offers. At the review on Wednesday, April 29, 2026, the five missing weeks are attributed on the record to the referral that was never sent; the enrollment is ordered and the referral is sent that day, and the record is corrected to say so. Colleen does **not** finish anything at this ending: the twelve sessions of Brightpath Parenting are still ahead of her, the case is still open, and Nia — home throughout, as she was from the first page — remains home under supervision. The win is that the gap stops being recorded as a fact about the mother. Anyone selling you a bigger one is selling you a different game.

## (2) The route

Verified by walking the scenario graph from the start node (see the verification note at the end). Key decision points, in order — node title, winning choice, and what it changes:

1. **No Referral on File** — *Call Ms. Voss and tell her exactly what Brightpath said.* Hidden item: the program's "no referral on file" answer enters the file's quiet record. This call — made in week one, before any assurance can soften it — is the date the whole timeline is later built from.
2. **It's in Process** — *Send a written email tonight — to Ms. Voss and to Brightpath — saying the referral is not on file and asking both to confirm when it is sent.* Sets **referralChased**; hidden item: the written chase itself. This is the single most important choice in the scenario: it moves the gap from the world of phone calls into the world of paper, while the gap is still new.
3. **The Reply, in Writing** — *Save both replies with the plan.* Hidden item: Brightpath's written confirmation that no referral was received. The program has now documented its own empty file — the strongest kind of document there is, because its author is the system.
4. **Ask for the File, or Don't** — *Put the request in writing — service chronology and program notes — and keep a copy.* Cash −3. Sets **recordsRequested**. The packet that arrives shows the enemy sentence: "mother to enroll in parenting services," with no referral date — the chronology assigning the gap, by grammar, to the only person it names.
5. **Mother to Enroll** — *Keep the packet with your emails.* Hidden item: the chronology line itself, preserved for the packet. Folder and file now disagree about the same five weeks, in writing, with dates.
6. **One Page, or a Story** — *Build the one-page timeline from the sent emails and the chronology, in date order.* Sets **gapDocumented**; hidden item: the assembled timeline. Six dated lines — plan ordered Monday, March 16, 2026; the call; the email; the program's reply; the silent chronology; the "not yet engaged" note of Monday, April 20, 2026 — and no adjectives for anyone to argue with.
7. **The Review** — *Present the one-page timeline — the sent emails, the program's written reply, and the chronology attached.* This choice is flag-gated: it is only available with **referralChased** + **recordsRequested** + **gapDocumented** all set. It leads to **Ending — Engaged, On Paper**. (The review trip itself costs $6 of fare at **The Night Before the Review**; you finish the route with $141 of the $150 start.)

Supporting route texture: **The Flyer in the Folder** is where the record right is learned — it is taught by a waiting-room flyer, because in real cases it very often is — and **The Timeline, Assembled** makes the page's copies, because a page that exists in one copy attends one meeting.

## (3) Why this wins — the law as it is supposed to work

Only principles from the scenario's verified set are stated here:

- **Agency records are obtainable on request** — 55 Pa. Code § 3130.44(d) ("shall be released upon request"). Step 4 is that right, exercised in writing. It matters because the chronology's silence — no referral date, ever — is the strongest evidence in the scenario, and you cannot quote a silence you have never been shown.
- **Counsel presents the record in the room where the plan is measured against it** — the right to counsel, and to appointed counsel if a parent cannot afford one (42 Pa.C.S. § 6337). The lawyer's work here is not argument in the dramatic sense; it is sequence — asking that the record be completed before the "not yet engaged" line is weighed.
- Everything else on the route is generic process, deliberately without citation: chase a missing referral **in writing** so the chase has a date; keep the program's own reply; assemble dates in order. The scenario's thesis is that reviews weigh the record that exists when they sit — and that a parent can, lawfully and cheaply, change what that record contains about a delay she did not cause.

## (4) The traps

1. **Accepting the phone assurance at "It's in Process"** because Ms. Voss sounds certain and kind. Cost: no **referralChased**, and no dated anything. The review's gated presentation closes, and the route ends at **Ending — Not Engaged, As Written** — the referral is eventually sent, but the five weeks stay in the file as the mother's non-engagement.
2. **Waiting for the review at "Ask for the File, or Don't"** to explain it in person. Cost: no **recordsRequested**, so the chronology's "mother to enroll" is never seen, never quoted, and never answered. A spoken account is believed personally and set aside professionally; the ending is again **Ending — Not Engaged, As Written**.
3. **Going in with the story at "One Page, or a Story"** because the story is clear, in order, and true. Cost: no **gapDocumented**. The note in the file — one line, printed, already read — outlasts the telling, and the ending is **Ending — Not Engaged, As Written**.
4. **Presenting partial paper at "The Review."** Cost: the whole route's assembly work. Half a timeline is an argument with missing premises; the gated choice exists precisely because the room can only complete a record that arrives complete.

## (5) What no strategy controls

Whether the referral was lost by a person, a queue, or a software handoff nobody remembers approving. Ms. Voss's caseload, and whether a worker with a lighter one would have written the capacity problem into the note herself — some do. The reviewer's temperament: a different one could note the timeline and still press the schedule, because Nia's weeks are real too, and she spent them six years old while a program waited for a piece of paper. The route controls none of that. It controls only whether, when the uncontrollable is weighed, the five weeks arrive in the room as a documented system gap or as an unexplained silence with a mother's name beside it. Outcomes in this system turn on workers, reviewers, and luck as much as on any parent's choices; the strategy's claim is the narrower one the scenario is named for — when the system loses your referral, make it sign for the loss.

---
*Verification: this route was walked programmatically against `scenario-57.json` — each named choice was followed from the start node in order (start → program_call → worker_call → written_chase → wait_begins → flyer_beat → records_fork → file_arrives → progress_note → prep → timeline_built → review_eve → review → end_win); every intermediate node and choice exists; every flag-gated choice's requirements were satisfied by flags set earlier on the walk; the walk terminates at the ending node titled "Ending — Engaged, On Paper" after visiting 14 nodes, with $141 of the $150 starting cash remaining.*
