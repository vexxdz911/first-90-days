# Strategy Guide — Scenario 101: "One Crib, Two Files"

*Game documentation for a fictional simulation in "The First 90 Days" (Tactic Watch). The family, the case, and every choice below are fictional. This guide is general information about how the scenario is built — it is not legal advice for any real case.*

## (1) The win

**Best ending: "One Crib, Two Files."**

State it honestly: this is a **partial** win, and it is the best this scenario offers, labeled partial in the scenario itself. Desiree and Sable are placed together in a home approved for a mother in care together with her infant. Desiree is still in foster care herself, her case remains open with its own reviews and its own road to eighteen, and Sable's case remains open on its own calendar. Nothing closes. The win is narrower and more durable than closure: the two files now name each other, the joint request and the correction sit stamped in both, and no future worker opening either file will meet a plan written for a person who does not exist. There is no ending in this scenario where either case is dismissed. Anyone selling you one is selling you a different game.

## (2) The route

Verified by walking the scenario graph from the start node (see the verification note at the end). Key decision points, in order — node title, winning choice, and what it changes:

1. **Shelter Care: Sable's Hearing** — *Ask Ms. Radcliffe to state on the record that you are requesting a joint placement.* Sets **jointOnRecord**; hidden item: the request spoken into the shelter care record. A request in the transcript exists in a way a hallway request does not.
2. **Pauline's Kitchen Table** — *Ask Pauline to write down her willingness, her approval limits, and the rides she can give.* Sets **fosterHomeStatement**; hidden item: the foster home's own statement, signed, instead of a summary of the home.
3. **Ms. Radcliffe Draws Two Files** — *Sign the joint request and file it in BOTH cases, to both caseworkers.* Sets **jointRequestBoth** — the single most important flag in the scenario. The joint question now has a desk in each file; separation stops being the default nobody chose and becomes a position someone would have to defend against a written alternative.
4. **School, With a Newborn Elsewhere** — *Keep a one-page log of school days, appointments, and visit dates, and give a copy to Mr. Salas and Ms. Radcliffe.* Cash −10. Sets **planDocumented**. Desiree-the-child's plan compliance, documented, is the evidence Desiree-the-mother's case will later need.
5. **The Request, in Both Files** — *File written record requests in BOTH cases — Sable's record and your own.* Cash −15. Sets **recordsRequested** and **ownRecordRequested**. This is the highest-leverage paper in either file: it is what reveals the scored assessment form's context lines reading "not assessed" and "unclear" while there is still time to answer them.
6. **What the Packets Show** — *Write the correction: one page, filed in both cases, naming the support system and asking both plans to name each other.* Sets **correctionFiled**. Pauline, the log, and the joint request are cited by filing date, not described from memory.
7. **Homes That Take Both** — *Put the joint-search request and a dated progress report in writing for BOTH review hearings.* Cash −10. Sets **searchDocumented**. The same packet in both courtrooms, on purpose — each review sees one family, not half of one.
8. **The Decision Is a Placement Question** — *The joint request was filed in both cases, the correction names one family, and both reviews saw the same packet.* This choice is flag-gated: it is only available with **jointRequestBoth** + **recordsRequested** + **correctionFiled** all set. It leads to **One Crib, Two Files**.

Supporting route choices that cost nothing and keep the record honest: reading both discharge plans side by side at **The Folder That Arrived During Labor**, calling Ms. Radcliffe about both files at **Two Desks**, and letting the packet speak at **Your Review: Desiree as the Child**, where the court notes the joint request in Desiree's own order by name and date.

## (3) Why this wins — the law as it is supposed to work

Only principles from the scenario's verified set are stated here:

- **The baby's placement was heard promptly, with counsel.** Sable's shelter care hearing fell inside the 72-hour window the law sets after a child is placed in shelter care (42 Pa.C.S. § 6332; 23 Pa.C.S. § 6315(d)), and Desiree's right to counsel — and to appointed counsel if she could not afford one — was stated on the record (42 Pa.C.S. § 6337; § 6332(a)). The joint-placement request was made in that room, where requests become record.
- **Agency records are obtainable on request, in both cases** — 55 Pa. Code § 3130.44(d) ("shall be released upon request"). Step 5 exercises that right twice, once for each file, because each file's scored assessment form held a blank exactly where the other file held the fact.
- **Reviews act on the record before them.** Both permanency reviews proceeded under 42 Pa.C.S. § 6351 on the files as written — which is why the same packet was filed for both. A court cannot order, note, or reckon with a joint placement that its own file never mentions.
- The separation this scenario depicts required no finding against anyone; it was produced by two locally reasonable files that never met. The route wins by the symmetrical counter-move: no heroic act, just the joint question, the compliance log, the record, and the correction — each filed in writing, in both places, before the reviews that would decide.

## (4) The traps

1. **Filing the joint request in Sable's case only** at "Ms. Radcliffe Draws Two Files," because the baby's file feels like the relevant one. Cost: no **jointRequestBoth** — Desiree's own review proceeds on a one-person plan that has never heard the request described as urgent, and the best ending's gate stays closed. One file knows; cases are decided by the file in the room.
2. **Relying on the school and clinic systems to report compliance** at "School, With a Newborn Elsewhere." Cost: no **planDocumented**. After a two-week caseworker handoff, the file summarizes October as "generally compliant, details unclear" — the two most expensive words in the scenario — and Sable's form keeps rating a mother whose own stability is "not assessed."
3. **Asking informally what is in Sable's file** at "The Request, in Both Files," instead of filing the written requests. Cost: no **recordsRequested**, no packets, nothing quotable or correctable — the family works from a kind phone summary while the scored context lines stay "unclear" through both reviews.
4. **Saving the correction to be spoken at the hearing** at "What the Packets Show." Cost: no **correctionFiled**. Spoken corrections leave with the room; the drift ending — Desiree's own plan rewritten without Sable's name in it — becomes reachable precisely because no filed document ever required either plan to describe two people.

## (5) What no strategy controls

Whether a mother-baby placement is actually open in the county that month — writing can require a documented search, and cannot conjure a bed. Either judge's reading of the packet. A placement disrupting for reasons no one filed. The ordinary arithmetic of two open cases, two review calendars, and a seventeen-year-old's own road out of care, which is a real plan in its own right and not a distraction from her daughter's. The route above does not control any of that — it only guarantees that when the uncontrollable happens, it happens to a record in which this family appears whole, in both files, by name. Outcomes in this system turn on workers, judges, resources, and luck as much as on any parent's choices. The strategy's whole claim is narrower: the parts that *were* hers — a request filed twice, a log kept, a record read, a correction stamped into both cases — were done in writing, in both places, on time.

---
*Verification: this route was walked programmatically against `scenario-101.json` — each named choice was followed from the start node in order; every intermediate node and choice exists; every flag-gated choice's requirements were satisfied by flags set earlier on the walk; the walk terminates at the ending node titled "One Crib, Two Files" after visiting 18 nodes, with $85 of the $120 starting cash remaining.*
