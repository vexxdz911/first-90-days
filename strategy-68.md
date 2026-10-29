# Strategy Guide — Scenario 68: "Ten Minutes in the Hallway"

*Game documentation for a fictional simulation in "The First 90 Days" (Tactic Watch). The family, the case, and every choice below are fictional. This guide is general information about how the scenario is built — it is not legal advice for any real case.*

## (1) The win

**Best ending: "Shelter Care Denied — Selin Goes Home Tonight."**

State it plainly and honestly: this is a full win, and it is **won at day 2, in a hallway, not at the trial.** At the shelter care hearing on Wednesday, January 13, 2027, the court declines to continue the removal on the agency's incomplete account, and Selin goes home that night with her grandmother as the approved backup staying in the home. The later adjudication never rebuilds the case: on the corrected record, the agency withdraws the petition rather than try to carry it. There is no dramatic courtroom rescue at day 14 in this scenario — by day 14 there is nothing left to rescue, because ten minutes on day 2 did the work.

## (2) The route

Verified by walking the scenario graph from the start node (see the verification note at the end). Key decision points, in order — node title, winning choice, and what it changes:

1. **The Evening the Truck Ran Long** — *Write down the evening as you know it while it is still tonight.* Sets **removed** (the removal happens in-story on day 0). Names, times, and grandmother's text exist on paper before shock can blur them.
2. **You Already Have a Lawyer** — *Ask the office what she will need from you tomorrow, and write the answer down.* Sets **counselContacted**. The answer — "anything in writing" — is the whole scenario in four words.
3. **The Fact Nobody Asked About** — *Write her name, her number, and "there until 7:00" at the top of a clean sheet.* Sets **grandmotherFact**. The decisive fact moves from a son's memory to a sheet of paper.
4. **One Page, Tonight** — *Write the one-page summary tonight — timeline, grandmother until 7:00, witness names and phone numbers.* Cash −5 (copies). Sets **pageWritten**; hidden item: the parent's one-page timeline, handed to counsel before the shelter care hearing. This is Hinge A: counsel can only know what the parent hands her.
5. **The Courthouse Morning** — *Tell her you have one page for her, in order, and that the first line is the one that matters.* No flag — it sets up the hallway: an overloaded lawyer learns in five seconds that this client brought paper.
6. **Ten Minutes in the Hallway** — *Hand her the page and name the witness first — "My mother was there until seven. The report says the home was empty at six."* This choice is flag-gated on **pageWritten**. Sets **witnessNamed**. This is Hinge B, and it is the single most important choice in the scenario: the witness is named first, not fourth, not never.
7. **The Shelter Care Hearing** — *Ask her to put it on the record now: call grandmother, and file counsel's written request for the agency record before any findings are made.* This choice is flag-gated on **witnessNamed**. Sets **recordsRequested** and **grandmotherOnRecord**; hidden item: grandmother named on the record at shelter care as present until 7:00 p.m. This is Hinge C — through counsel, on the record, before the findings, not after them.
8. **A Voice on the Phone** — *Ask Nakamura, before anyone leaves, what could still undo this at adjudication — and write it down.* Hidden item: the order — shelter care not sustained; Selin released to grandmother's care pending adjudication, the agency's 6:00 p.m. account found incomplete.
9. **Home, With a File Still Open** — *Make the one scheduled call with a written agenda — the record request, grandmother's statement, the adjudication date.* Sets **agendaCall**. Using appointed counsel well means ordered time, not more time.
10. **The Record Arrives** — *Go through it with Nakamura page by page and mark the contradiction together.* Sets **recordRead**; hidden item: the agency file released on counsel's written request (§ 3130.44(d)), its 6:00 p.m. "empty home" entry contradicting the worker's own 7:15 p.m. note.
11. **Delivered Before, Not During** — *Deliver the packet to Nakamura's office today, three days before the hearing.* Cash −10. Sets **packetDelivered**. Documents delivered before a hearing get read at a desk; documents delivered during one get carried into a courtroom unread.
12. **Adjudication — The Corrected Record** — *Let Nakamura put the corrected record — the 6:00 entry against the 7:15 note — in front of the judge.* This choice is flag-gated on **recordsRequested**. It leads to **Shelter Care Denied — Selin Goes Home Tonight**.

You finish the route with **$105 of the $120 starting cash remaining** (copies −5, delivery trip −10).

## (3) Why this wins — the law as it is supposed to work

Only principles from the scenario's verified set are stated here:

- **The clocks run first, and counsel is a right inside them.** A shelter care hearing must be held within 72 hours of a child being taken into custody (42 Pa.C.S. § 6332; 23 Pa.C.S. § 6315(d)), and the parent has the right to counsel — appointed if the parent cannot afford one (42 Pa.C.S. § 6337) — including counsel at the shelter care hearing itself (§ 6332(a)). The scenario's whole argument is the second half of that right: appointed counsel with forty cases is real counsel, but she knows only what she is handed, in time, in usable order.
- **The agency record is obtainable on request** — it "shall be released upon request" (55 Pa. Code § 3130.44(d)), and the rule is not to be read to protect agency employees' privacy as a basis for withholding (§ 3130.44(f)). Step 7 exercises that right through counsel, in writing, on the record, on day 2 — which is why the file's internal contradiction is in both lawyers' hands by day 8 instead of surfacing for no one.
- **At adjudication, the burden never moves.** The court may find a child dependent only "from clear and convincing evidence" (42 Pa.C.S. § 6341(c)); the parent does not have to prove innocence or fitness to win, the judge decides credibility, and a fact not proven is a fact the court cannot use. A petition that is not proven is dismissed and the child discharged (§ 6341(a)). The corrected record wins at adjudication precisely because the agency's own proof collapsed — the parent's side never had to carry a burden at all.
- **The losing branch shows the same law from the other side:** before a disposition that keeps a child out of the home, the court must enter findings on the record — continuation in the home contrary to the child's welfare, and whether reasonable efforts were made to prevent removal (42 Pa.C.S. § 6351(b)) — and permanency hearings then run within six months of removal and within six months of each previous one (§ 6351(e)(3)(i)).

## (4) The traps

Each trap below leads, by its own mechanics, to **"Seventy-Two Hours Become Thirty Days"** — shelter care sustained, dependency found at adjudication, placement continuing into the six-month permanency clock.

1. **The grievance hallway at "Ten Minutes in the Hallway."** Spending the ten minutes on the neighbor, the teenager, and the call that started the case. The grievance is legitimate; it is also not a witness. Cost: no **witnessNamed**, the gated hearing choice never opens, grandmother is never named on the record, and the judge rules on the report as written.
2. **Waiting for the lawyer to "find" the fact herself at "You Already Have a Lawyer."** She has forty cases; discovery is not her afternoon. A fact she is never told is a fact she cannot argue, however obvious it feels from the parent's chair. This trap compounds trap 1: by the time the fact is mentioned — at the end of a call on day 8 — shelter care has already been decided on the empty-house account.
3. **Treating appointed counsel as no counsel — or as an enemy — and withholding the page.** Saying very little in the hallway because "she's the lawyer," or never writing the page at "One Page, Tonight" because the hallway talk will cover it. Cost: no **pageWritten**, so the witness-first choice in the hallway is not even available; appointed counsel walks into court knowing the agency's report and nothing else, which is functionally the same as the parent having no counsel at all — a right unexercised at the one moment it could act.
4. **The late statement at "The Statement, Written at Last."** Grandmother's account finally written on day 11, delivered to an office on a Friday or carried to a hallway on Monday. It is the same true page as day 1's — stamped with a date that tells its own story. Shelter care is nine days decided, adjudication is built on it, and the fact arrives after the record it needed to enter has closed in stages.

## (5) What no strategy controls

The judge's willingness to take a grandmother's testimony by phone on a crowded morning. Whether the agency's lawyer, reading the contradiction, chooses to withdraw rather than fight. Ms. Nakamura's caseload, the docket's pace, a supervisor's decision about a broken truck, and the plain luck of a worker's own 7:15 p.m. note existing in the file at all. The route above controls none of that — it only guarantees that when the uncontrollable breaks your way, the fact it breaks on is on paper, in your lawyer's hand, in the right order, before the findings are made. Outcomes in this system turn on workers, judges, and luck as much as on any parent's choices. The strategy's whole claim is narrower: the parts that *were* yours — one page, one name spoken first, one request made on the record in time — were done on day 1 and day 2, when they could still change where a six-year-old sleeps.

---
*Verification: this route was walked programmatically against `scenario-68.json` — each named choice was followed from the start node in order; every intermediate node and choice exists; every flag-gated choice's requirements were satisfied by flags set earlier on the walk; the walk terminates at the ending node titled "Shelter Care Denied — Selin Goes Home Tonight" after visiting 13 nodes, with $105 of the $120 starting cash remaining.*
