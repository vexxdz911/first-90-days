# Strategy Guide — Scenario 58: "The Missed Screen"

*Game documentation for a fictional simulation in "The First 90 Days" (Tactic Watch). The family, the case, and every choice below are fictional. This guide is general information about how the scenario is built — it is not legal advice for any real case. All substance content in the scenario and in this guide is procedural: summonses, windows, shifts, and logs.*

## (1) The win

**Best ending: "Ending — Documented, Not Positive."**

State it honestly: this is a **partial** win, and it is the best this scenario offers. At the review on Monday, June 8, 2026, the compliance tally is corrected against its own underlying times: the conflict morning is recorded as a screen completed at the nearer site after a written request, the late-posted result is entered as a late posting, and no failed appearance — which the plan counts the same as a positive result — stands against Desirae. Nothing larger is won: the screens continue, the case is still open, and Leo is still living at his grandmother Lorraine's. The win is a tally that describes scheduling facts instead of replacing them. Anyone selling you a bigger one is selling you a different game.

## (2) The route

Verified by walking the scenario graph from the start node (see the verification note at the end). Key decision points, in order — node title, winning choice, and what it changes:

1. **The 9:40 Text** — *Text back tonight, in writing: the site, your 8:30 shift, the conflict — and ask for the nearer site or a later window.* Sets **screenMoved**; hidden item: the conflict documented **before** it happened. This is the single most important choice in the scenario. A conflict written down the night before is a scheduling problem; the same conflict explained the morning after is, in the plan's language, an entry.
2. **The Nearer Window** — *Keep the reply and the completion slip with your other case papers.* Hidden item: the screen completed at the nearer site inside the window. The morning now exists in the file the way it existed in her life — raised, answered, completed.
3. **Ask for the Log** — *Request the screen log in writing — summonses, sites, and result entries — and keep a copy of the request.* Cash −3. Sets **recordsRequested**; the log itself, when it arrives, records the 9:40 p.m. summons of Monday, April 20, 2026 and every site and entry since. Hidden item (at **The Log, on Paper**): the log obtained and kept.
4. **The Second Text** — *Keep the confirmation text and the dated slip, and send a written note that the screen was completed on its date.* Cash −8 (that screen day's fares — spent on either branch). Sets **proofKept**; hidden item: month two's completion of Tuesday, May 19, 2026 documented before the late posting could harden into "result not received." This is step 1's lesson applied a second time, to a delay that is the system's rather than hers.
5. **Assemble the Paper** — *Assemble the packet — texts, log, confirmations, slips — in date order, with your lawyer.* Sets **packetBuilt**; hidden item: the assembled packet. No adjectives — just times, from three different hands, agreeing with each other.
6. **The Review** — *Present the packet — the night-before message, the screen log, and the completion confirmations.* This choice is flag-gated: it is only available with **screenMoved** + **recordsRequested** + **packetBuilt** all set. It leads to **Ending — Documented, Not Positive**. (The review trip costs $6 of fare at **The Night Before the Review**; you finish the route with $103 of the $120 start.)

Supporting route texture: **What the Week Wrote Down** is where counsel enters — the lawyer's only question is "what does the log itself say," because everything after that scene is the work of answering it.

## (3) Why this wins — the law as it is supposed to work

Only principles from the scenario's verified set are stated here:

- **The screen log is part of the case record, and the record is released on request** — 55 Pa. Code § 3130.44(d). Step 3 is that right, exercised in writing. It matters because a tally can only be corrected by the times underneath it, and the times live in a document the parent has to ask for.
- **Counsel assembles and presents the packet in the room where compliance is tallied** — the right to counsel, and to appointed counsel if a parent cannot afford one (42 Pa.C.S. § 6337).
- The decisive move is generic process, deliberately without citation: **document a scheduling conflict in writing before it happens**, and ask on paper for the adjustment (a nearer site, a later window). The plan's default — a missed screen recorded as a failed appearance and counted the same as a positive result — is a rule about records, and it is beaten by a record: on the winning route, on paper, there was never a miss. Nothing in the scenario states any other rule about screens, testing, or recovery, and no result in it is ever described beyond completed, recorded, and tallied.

## (4) The traps

1. **Saying nothing at "The 9:40 Text"** and trying to make both. Cost: no **screenMoved** — the window closes at 9:00, the form records a failed appearance with no line for buses or arithmetic, and the plan's default converts it toward a positive in the tally. The gated presentation at the review closes, and the route ends at **Ending — Positive, By Default**.
2. **Working from the summaries at "Ask for the Log."** Cost: no **recordsRequested**. The summons times and sites behind the tally's one-line entries are never seen, so the tally can never be corrected against them — only argued with. The ending is again **Ending — Positive, By Default**.
3. **Trusting the portal at "The Second Text."** Cost: no **proofKept**. A completed screen sits in the file as "result not received" while the review packet is assembled, and absences in a tally are read in the direction the plan's language points. The ending is **Ending — Positive, By Default**.
4. **Bringing the phone to "Assemble the Paper"** instead of building the packet. Cost: no **packetBuilt**. The account is accurate in every particular and unaccompanied by exhibits; the tally runs on entries, and the ending is **Ending — Positive, By Default**.

## (5) What no strategy controls

The buses, and whether they run on the one morning they must. Whether the collection site answers a night-before message — a different site might never have replied, and then the written request would have mattered as evidence rather than as a solution, which is a smaller win this scenario does not pretend is the same one. The posting queue, the supervisor's patience, the caseworker's caseload, and the plain luck of which mornings get summoned at all. A recovery lived on a schedule — meetings, shifts, a five-year-old at his grandmother's — is not measured by any tally in either direction, and this debrief tradition holds here too: outcomes turn on workers, sites, and luck as much as on parents. The route controls one thing only: whether the file's account of two mornings is written from timestamps or from defaults.

---
*Verification: this route was walked programmatically against `scenario-58.json` — each named choice was followed from the start node in order (start → night_text → morning_moved → week_after → records_fork → log_arrives → month_two → paper_kept → prep → packet_ready → review_eve → review → end_win); every intermediate node and choice exists; every flag-gated choice's requirements were satisfied by flags set earlier on the walk; the walk terminates at the ending node titled "Ending — Documented, Not Positive" after visiting 13 nodes, with $103 of the $120 starting cash remaining.*
