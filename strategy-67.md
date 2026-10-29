# Strategy Guide — Scenario 67: "The Room Where It Happens"

*Game documentation for a fictional simulation in "The First 90 Days" (Tactic Watch). The family, the case, and every choice below are fictional. This guide is general information about how the scenario is built — it is not legal advice for any real case.*

## (1) The win

**Best ending: "The Petition Is Dismissed."**

State it honestly: this is a full win at the adjudication stage, and it is exactly what the law provides for when the agency does not carry its burden. The judge finds Tuesday not proven and Thursday a single, owned lapse with care now arranged on paper; the petition is dismissed under 42 Pa.C.S. § 6341(a) and § 6341(c), and Amos is home the same night. It is not a finding that Thursday never happened, or that Colette was a perfect parent. It is a finding that dependency was not proven by clear and convincing evidence — the only question room one ever asked.

## (2) The route

Verified by walking the scenario graph from the start node (see the verification note at the end). Key decision points, in order — node title, winning choice, and what it changes:

1. **The Evening It Happens** — *Use the ten minutes for paper: hand her the printed quit text and write down your mother's name and number, your work roster, and who was with Amos on Tuesday.* Sets **removed** (the removal happens in-story, on this choice) and **nightOnePaper**; hidden item: "File — sitter's resignation text, printed and handed to the worker on night one." What is in the file on night one is in the file at every hearing after.
2. **The Morning After** — *Write down Mr. Beaumont's three questions and start a folder tonight.* No flag, no cost: the discipline the rest of the route runs on. You also learn the two load-bearing facts: shelter care is Friday, within 72 hours (42 Pa.C.S. § 6332), and at adjudication the agency — not you — must prove its case by clear and convincing evidence (42 Pa.C.S. § 6341(c)).
3. **The Folder, or the Empty Hands** (shelter care) — *You brought the folder — and you ask Mr. Beaumont to name your mother on the record as an approved backup caregiver.* Sets **folderReady**; hidden item: "Transcript — grandmother named at shelter care as an approved backup caregiver." A name in a transcript is findable at every later hearing; a name in a caseworker's memory is not.
4. **The Judge Asks You Directly** (shelter care) — *Answer plainly and briefly: "My mother was with him Tuesday, Your Honor. Thursday he was alone for forty minutes. That was my decision, and it was wrong." Then stop.* Sets **plainAnswers**. Short, specific, and finished — the answer a judge can write down and use.
5. **The Week Between: Ask for the File** — *Send the written request for the agency record today, and keep a dated copy.* Cash −5. Sets **recordsRequested**. The record "shall be released upon request" (55 Pa. Code § 3130.44(d)) — and asking is what later reveals that the agency's file carries the wrong roster for Tuesday.
6. **A Plan That Is Actually Arranged** — *Pay the deposit and get Ms. Ferreira's commitment in writing, with your mother as named backup.* Cash −40. Sets **sitterCommitted**. A name, nights, a phone number, a signature: what an answer to "who, exactly?" looks like.
7. **The Roster in Their File** — *Go through the packet with Mr. Beaumont line by line and mark every place the file's version differs from your paper.* The discrepancy, found a week early instead of in the hearing room: their roster shows you on shift Tuesday; your real roster shows the swap — you were off, and Amos was at your mother's.
8. **Two Stages, Two Different Tests** and **What the Judge Must Say Out Loud** (prep) — *Repeat the frame back until it is cold, and rehearse only the arranged facts.* Adjudication (§ 6341(c)) and disposition (§ 6341(d)) are different rooms with different rules, and a § 6351(b) disposition's findings belong on the record. Knowing which room you are in is what keeps a Thursday answer from becoming a Thursday argument.
9. **The Room Where It Happens** (adjudication) — *Take your seat, folder in front of you, and let the agency go first.* Cash −10. It is their burden to carry; order is the structure of the hearing working, not passivity.
10. **The Offer** — *OFFER the roster and the new sitter's written commitment as an exhibit.* Flag-gated on **sitterCommitted**; hidden item: "Exhibit — work roster and new sitter's written commitment, offered at adjudication." An arrangement handed up as an exhibit has to be dealt with; one described in testimony can simply be disbelieved.
11. **Clear and Convincing, or Not** — *Mr. Beaumont asks the court to dismiss: Tuesday was not proven, and one owned lapse with an arranged plan does not carry the burden.* Flag-gated on **folderReady** + **plainAnswers** + **recordsRequested**; hidden item: "Order — petition dismissed; the two unproven dates are not findings." This leads to **The Petition Is Dismissed**, with $105 of the $160 starting cash remaining.

## (3) Why this wins — the law as it is supposed to work

Only principles from the scenario's verified set are stated here:

- **The burden is the agency's, and it is a heavy one.** At adjudication the court may find a child dependent only "from clear and convincing evidence" (42 Pa.C.S. § 6341(c)). The parent does not have to prove innocence or fitness to win; the judge decides credibility; and a fact not proven is a fact the court cannot use. The route is built entirely around that allocation: it does not try to make Colette look good — it makes Tuesday unprovable on the agency's own evidence, because the agency's only witness was not there and its file's roster was wrong.
- **When the proof fails, the petition ends.** If dependency is not proven, the petition is dismissed and the child discharged (42 Pa.C.S. § 6341(a)). That is why there is no disposition in the win ending: disposition — with its broader evidence rules (42 Pa.C.S. § 6341(d)(1)–(2)) and its on-the-record findings (42 Pa.C.S. § 6351(b)) — is a room you only enter if adjudication is lost.
- **The early clocks and rights held.** Shelter care came within 72 hours of removal (42 Pa.C.S. § 6332; 23 Pa.C.S. § 6315(d)), with counsel appointed under 42 Pa.C.S. § 6337, present at the shelter care hearing under § 6332(a).
- **Agency records are obtainable on request** — 55 Pa. Code § 3130.44(d) ("shall be released upon request"). Step 5 is that sentence exercised in writing, and it is the single highest-leverage move in the scenario: without it, the roster discrepancy in the agency's file is never seen by anyone on Colette's side of the table.

## (4) The traps

1. **Arguing with the caseworker from your seat at "The Judge Asks You Directly"** because the summary is wrong and she is right there. Cost: no **plainAnswers** — judges tend to discount everything a witness says after that, and the dismissal argument at the verdict node closes. The path runs through disposition to **"Dependent — And the Clock Starts."**
2. **Coming empty-handed to shelter care** because the roster is on the counter and the letter is still a phone call. Cost: no **folderReady**, no grandmother named on the transcript — the folder that adjudication is later built from never starts existing. Same ending: **"Dependent — And the Clock Starts."**
3. **Waiting to see the record at the hearing** instead of requesting it in writing at "The Week Between." Cost: no **recordsRequested** — the agency file's wrong Tuesday roster is never compared against the real one, Tuesday is never shown unproven on paper, and counsel meets the discrepancy, if at all, in the room where it is too late to build on. Same ending: **"Dependent — And the Clock Starts."**
4. **Promising a plan you haven't actually arranged** at "A Plan That Is Actually Arranged" — describing a neighbor's "probably" as coverage lined up. Cost: no **sitterCommitted**, so the exhibit offer at adjudication is unavailable, and the promised plan collapses on the judge's one question: "who, exactly?" Same ending: **"Dependent — And the Clock Starts."**

## (5) What no strategy controls

Whether the agency's witness testifies as honestly about her limits as Ms. Alvarado does here. Whether the neighbor's account, tested, really covers only one evening. The judge's reading of a single lapse, a supervisor's roster-keeping, a grandmother's health, a sitter's reliability next month. The route above controls none of that — it only guarantees that when the agency is put to its proof, your side of the proof exists: handed over on night one, named on a transcript on Friday, requested in writing on Monday, and offered as an exhibit on the day. Outcomes in this system turn on workers, judges, and luck as much as on any parent's choices.

---
*Verification: this route was walked programmatically against `scenario-67.json` — each named choice was followed from the start node in order; every intermediate node and choice exists; every flag-gated choice's requirements were satisfied by flags set earlier on the walk; the walk terminates at the ending node titled "The Petition Is Dismissed" after visiting 17 nodes, with $105 of the $160 starting cash remaining.*
