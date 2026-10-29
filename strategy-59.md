# Strategy Guide — Scenario 59: "Two Buses to the Visit"

*Game documentation for a fictional simulation in "The First 90 Days" (Tactic Watch). The family, the case, and every choice below are fictional. This guide is general information about how the scenario is built — it is not legal advice for any real case.*

## (1) The win

**Best ending: "Ending — On Time, On Record."**

State it honestly: this is a **partial** win, and it is the best this scenario offers. At the review on Monday, June 22, 2026, the pattern of "lateness" is re-attributed on the record to the visit move that caused it; visits are ordered to a nearer site for the next cycle, with transportation support in the meantime, and the note language is corrected to carry the journey with the arrival. Andre does **not** win custody of anything at this ending: Ruby is still in foster care, as she was before the story opened, and the three shortened visits already happened — that time is not returned by any order. The win is that the file stops describing a journey as a trait. Anyone selling you a bigger one is selling you a different game.

## (2) The route

Verified by walking the scenario graph from the start node (see the verification note at the end). Key decision points, in order — node title, winning choice, and what it changes:

1. **Two Buses, Ninety Minutes** — *Sign in, take the visit there is, and keep the transfer stubs in your pocket.* Hidden item: the first note — "father arrives late; visit shortened" — enters the file's quiet record. The stubs are the journey's first, accidental documents. (The trip itself cost $12 of fares at **The Letter About the Visits**; every route in this scenario pays the move's fares, winning or losing.)
2. **Answer the Move, or Absorb It** — *Answer the move in writing — nearer site or transportation support, asked for on paper.* Cash −12 (the second visit's fares, charged on this choice). Sets **visitMoveAnswered**; hidden item: the dated written answer. This is the scenario's founding choice: a one-page letter moved the visits, and only a dated letter can make the file hold the journey beside the arrival.
3. **The Sign-In Sheet** — *Photograph the sign-in sheet and start a dated arrival log — departures, buses, arrivals.* Sets **arrivalLog**; hidden item: the log begun at the second visit. Thirty seconds at a door each Saturday, converting the center's clock from the file's only witness into a shared one.
4. **Ask for the Notes** — *Request the visit notes in writing — all three visits — and keep a copy of the request.* Cash −3. Sets **recordsRequested**. The notes that arrive record the center's own times — arrivals twenty, fifteen, and eighteen minutes after the start — which, read beside the move letter of Monday, May 11, 2026, become the system's own measurements of the journey it imposed. Hidden item (at **The Center's Own Times**): the notes obtained and kept.
5. **One Packet, in Date Order** — *Assemble the packet — letter, written answer, log, and notes — in date order.* Cash −4. Sets **reviewPacket**; hidden item: the assembled packet. Its first page is the move letter, because chronology is the argument.
6. **The Review** — *Present the packet — the move letter, the written answer, the arrival log, and the center’s own notes.* This choice is flag-gated: it is only available with **visitMoveAnswered** + **arrivalLog** + **recordsRequested** + **reviewPacket** all set. It leads to **Ending — On Time, On Record**. (Counting the third trip's $12 at **The Third Saturday**, you finish the route with $97 of the $140 start — the win costs $43, and $36 of it is bus fares the move imposed on every route alike.)

Supporting route texture: **Three Times, One Word** is the scenario's hinge — the pre-review summary where three single notes harden into a "pattern," which is the moment the underlying documents stop being optional.

## (3) Why this wins — the law as it is supposed to work

Only principles from the scenario's verified set are stated here:

- **Visit notes are part of the case record, and the record is released on request** — 55 Pa. Code § 3130.44(d) ("shall be released upon request"). Step 4 is that right, exercised in writing. It matters because the center's own times are the one account of the arrivals that the review cannot discount as the father's version — requested, they testify about the whole trip, including the part the center imposed.
- **Counsel presents the chronology in the room where the pattern is adopted** — the right to counsel, and to appointed counsel if a parent cannot afford one (42 Pa.C.S. § 6337). Her sentence is the scenario's method: "Late is a conclusion" — and conclusions can be re-read when the documents underneath them are put beside them, in order.
- Everything else is generic process, deliberately without citation: answer a move **in writing** while it is new (a nearer site, transportation support — asked for on paper, where answers live); keep your own arrival log from the second visit, while keeping it is still a choice; assemble in date order. No rule in the scenario guarantees a nearer site. What the record guarantees is narrower: the review must describe a journey before it may describe a trait.

## (4) The traps

1. **Absorbing the move quietly at "Answer the Move, or Absorb It"** — leaving earlier, saying nothing on paper. Cost: no **visitMoveAnswered**. The file holds a move letter with no answer in it, and the notes keep their four words unopposed. The gated presentation closes, and the route ends at **Ending — Late, As Recorded**.
2. **Signing in and going straight in at "The Sign-In Sheet."** Cost: no **arrivalLog**. Arrival times remain the center's alone; no departure, no bus, no journey ever acquires a date. The ending is again **Ending — Late, As Recorded**.
3. **Working from the summary at "Ask for the Notes."** Cost: no **recordsRequested**. The review becomes a meeting about a summary of notes the father has never seen, and the center's own times never testify. The ending is **Ending — Late, As Recorded**.
4. **Bringing the story and the stubs at "One Packet, in Date Order."** Cost: no **reviewPacket**. The truest telling in the room is weighed against a printed pattern, and printed things are what reviews adopt. The ending is **Ending — Late, As Recorded** — with the fares paid anyway, which is the trap inside the trap: the losing routes in this scenario cost almost exactly what the winning one costs. The difference was never money. It was paper.

## (5) What no strategy controls

The buses, the connection, and the provider consolidation that moved the room in the first place — none of it answers to a parent, a log, or this guide. The center's record-keeping habits: a center whose sign-in times were sloppy would give any packet less to work with. The reviewer's reading: a different one could note the journey in full and keep the far site anyway, weighing Ruby's settled routine more heavily than her father's Saturdays. And Ruby herself — her careful order of doing the important things first, in case the end of a visit comes early — will take longer to unlearn than any order takes to write. Workers, centers, reviewers, and luck hold pieces of every outcome here. The route controls only whether the record those pieces land on contains the journey — dated, logged, and confirmed by the center's own clock — or only the arrival it produced.

---
*Verification: this route was walked programmatically against `scenario-59.json` — each named choice was followed from the start node in order (start → first_trip → note_exists → split_request → written_track → log_beat → third_visit → pattern_note → records_fork → notes_arrive → prep → packet_ready → review_eve → review → end_win); every intermediate node and choice exists; every flag-gated choice's requirements were satisfied by flags set earlier on the walk; the walk terminates at the ending node titled "Ending — On Time, On Record" after visiting 15 nodes, with $97 of the $140 starting cash remaining.*
