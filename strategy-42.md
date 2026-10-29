# Strategy Guide — Scenario 42: "The Report from the Hospital"

*Game documentation for a fictional simulation in "The First 90 Days" (Tactic Watch). The family, the case, and every choice below are fictional. This guide is general information about how the scenario is built — it is not legal advice for any real case.*

## (1) The win

**Best ending: "Unfounded, On the Whole Record"**.

This is a **full** win — and it is won at the determination meeting, before any appeal exists. A toddler's fracture produced two medical readings that do not match. The route assembles the whole medical record — ER chart, treating physician's letter, well-child record, the nurse-line log — and puts it in the agency's hands, filed and noted, while the determination is still being written. The agency, reading its own evidence whole, reaches the conclusion its hearing would have reached. The two lesser endings are the same evidence arriving later and later: on appeal, in time (partial), and at a hearing the parent walks into with a summary instead of a record (hard).

## (2) The route

Verified by walking the scenario graph from the start node (see the verification note at the end). Key decision points, in order — node title, winning choice, and what it changes:

1. **The Fall** — *Write down the social worker's words, the worker's name, and Saturday's hours while they are exact.* Sets **timelineWritten**.
2. **What the File Says So Far** — *File the written request and mark the word the report actually used.* Sets **recordsRequested**.
3. **The Hospital's Paper** — *Order the ER chart today and request the pediatric chart in the same afternoon.* Sets **erChartOrdered**.
4. **Dr. Weiss** — *Assemble the full packet: ER chart, Weiss's letter, the well-child record, Saturday's timeline.* Sets **packetReady** — the flag the meeting is gated on.
5. **The Determination Meeting** — *Hand over the packet — the whole record — with the written timeline on top.* Flag-gated on **packetReady**.
6. **Read in the Room** — *Point to the nurse-line log: Saturday, 7:04 p.m., advice given and followed, in the chart.* Sets **nurselineShown**.
7. **The Letter** — *Read it fully — sign, and send the one-line correction: right forearm, per the ER chart.* Sets **readBeforeSigning**.

## (3) Why this wins — the law as it is supposed to work

- **A determination is only as good as the record it rests on, and the parent can complete the record.** The report rested on one reading. The whole record — both readings, the treating chart, the advice line called and followed that evening — is a different evidentiary object, and assembling it is the parent's move, not the agency's errand.
- **The record request comes first** (55 Pa. Code § 3130.44(d)): the parent reads what the file says so far before deciding what the file still needs.
- **The appeal law is the route's shadow, and the debriefs teach it on the branches that need it.** An indicated report may be appealed within 90 days of notification (23 Pa.C.S. § 6341(a)(2)); the appeal carries the appellant's right to the investigation evidence — all of it, including what helps her (§ 6341(c.2)(4)); at the hearing the agency bears the burden by substantial evidence (§ 6341(c.2)(5)); a decision is due within 45 days (§ 6341(c.3)); and reconsideration within 15 days or the Commonwealth Court within 30 remains after that (§ 6341(g)). The win route exists so the family never has to spend those windows — the partial and hard endings show what each window is worth when it is the only road left.

## (4) The traps

1. **Letting the determination be written from the first reading** (the h-branch). Cost: "Indicated" — and the family's whole position moves into the appeal, where the same packet must now be assembled under a 90-day clock instead of before a meeting.
2. **Filing the appeal without the evidence demand.** Cost: the appeal argues against a file the parent has never seen whole; the amended consult — the document that decides the case — stays in the agency's drawer until a hearing officer asks for it, if one does.
3. **Rushing a partial packet to the meeting** instead of the whole record. Cost: no **packetReady** as the data defines it — a packet missing the treating chart reads as advocacy, and is weighed as advocacy.
4. **Missing the shape of the hard ending**: at the hearing, sincerity is credited and still loses, because the agency's modest burden — substantial evidence (§ 6341(c.2)(5)) — can be carried by summaries when the whole record was never put in front of the officer in time.

## (5) What no strategy controls

What the consult ultimately says, whether the ER chart is released promptly, and the officer on the branches where a hearing happens. The route controls only what was ever controllable: that the charts were ordered the same week, the packet was assembled whole, and its filing was noted in the record with a date. Outcomes in this system turn on workers, judges, and luck as much as on any parent's choices — the strategy's claim is narrower: the determination in this case was made on the whole record, because the parent is the one who made it whole.

---
*Verification: this route was walked programmatically against `scenario-42.json` — each named choice was followed from the start node in order; every flag-gated choice's requirements were satisfied by flags set earlier on the walk; the walk terminates at the ending node titled "Unfounded, On the Whole Record" after visiting 13 nodes, with $160 of the $160 starting cash remaining (no choice in this scenario carries a cash cost; the starting cash never moves). Walked path: The Fall → Two Readings → What the File Says So Far → The Hospital's Paper → Dr. Weiss → The Night Before the Meeting → The Determination Meeting → Read in the Room → The Supervisor's Question, Answered → Waiting on the Consult → The Final Consult → The Letter → Unfounded, On the Whole Record.*
