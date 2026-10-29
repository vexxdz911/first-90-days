# Strategy Guide — Scenario 85: "Services the Plan Promised"

*Game documentation for a fictional simulation in "The First 90 Days" (Tactic Watch). The family, the case, and every choice below are fictional. This guide is general information about how the scenario is built — it is not legal advice for any real case.*

## (1) The win

**Best ending: "Ending — The Empty Boxes, Read Aloud."**

State it honestly: this is a **partial** win, and it is the best this scenario offers. The termination petition is not filed at the fifteen-month point because an exception is documented — but the child remains placed, the case continues, and no ending in this scenario turns a filing decision into a reunification by itself. What the route wins is the thing the clock was actually deciding: whether the agency must file, answered with paper.

## (2) The route

Verified by walking the scenario graph from the start node (see the verification note at the end). Key decision points, in order — node title, winning choice, and what it changes:

1. **The Record Request** — *Send the written request for the complete case record this week.* Cash −5; Sets **recordsRequested**, **recordSeen**.
2. **The Service That Is a Box** — *Ask for the referral's dates in writing — promised, sent, started.* Sets **referralDates**.
3. **Paper With a Date On It** — *Get it in a dated letter, on letterhead, and file your copy.* Cash −5; Sets **datedLetter**.
4. **The Family Name in the Minutes** — *Put the kinship request in writing and ask for the study to be ordered.* Sets **kinAsked**.
5. **The List** — *Get it in a dated letter, on letterhead, and file your copy.* Cash −5; Sets **datedLetter**.
6. **The Packet** — *File the packet and ask for the finding in writing.* Cash −15; Sets **packetBuilt**.
7. **The Services Track** — *Build this track's record completely, in writing.* Cash −10; Sets **servicesReady**.
8. **The Fifteen-Month Review** — *Put the packet's dates to the court and ask for the exception to be documented.* This choice is flag-gated: it is only available with **recordsRequested** + **packetBuilt** + the completed exception track.

Supporting choices along the same walk — every "paper version" choice (dated, copied, filed), every written visit-log request, and every dated letter — add the documentation the packet is later assembled from. The full walked path is printed in the verification note.

## (3) Why this wins — the law as it is supposed to work

- **The clock is a filing duty with exceptions, not an automatic termination.** At 15 of the most recent 22 months in foster care, the agency must file or join a termination petition *unless* an exception applies (42 U.S.C. § 675(5)(E)): the child is being cared for by a relative; the agency has documented a compelling reason in the case plan; or the agency has not provided the services the plan identified as necessary for safe return. This scenario is built on the word "documented": three referrals lost across two caseworker changes only counts when it exists as dated paper in the case plan and the record.
- **The record request is the reconnaissance.** Agency records are released on request — 55 Pa. Code § 3130.44(d). Without the record, the parent cannot know which boxes are empty; with it, the exception argument is built from the agency's own dates.
- **Counsel is part of the machinery, not a luxury** (42 Pa.C.S. § 6337) — the packet is assembled with the lawyer, filed before the date it answers, and argued from dates at the review.
- **A petition is not a termination.** If filed, it is a separate case the agency must prove by clear and convincing evidence. The route never treats the filing date as a finding — it works to keep the filing from being scheduled on an undocumented record.

## (4) The traps

1. **Trusting the summary instead of requesting the record** at "The Record Request." Cost: no **recordsRequested** — the hearing's winning choice is flag-gated on it, so the best ending closes before the story is half over, and every later date is argued from memory.
2. **Accepting the verbal estimate** at the letter/list beats. Cost: no **datedLetter** in the folder — the barrier stays a rumor with adverbs attached, and the packet loses its hardest fact.
3. **Carrying the packet to the hearing instead of filing it** at "The Packet." Cost: no **packetBuilt** — paper the other side has not read, delivered on the deadline, is treated as a speech, and the gated choice stays shut.
4. **Giving the speech at "The Fifteen-Month Review."** Cost: the whole case. It is a true speech, and it leads directly to "Ending — The Petition Is Filed" — because petitions are documents, and documents outlast speeches.

## (5) What no strategy controls

The waitlist, the study queue, the agency's filing choice, the judge's reading of the packet, and plain luck. The route controls only what was ever controllable: that the request was written, the letters were dated, the packet was filed before the date it answered. Outcomes in this system turn on workers, judges, and luck as much as on any parent's choices — the strategy's claim is narrower: when the fifteenth month arrived, it met a record.

---
*Verification: this route was walked programmatically against `scenario-85.json` — each named choice was followed from the start node in order; every flag-gated choice's requirements were satisfied by flags set earlier on the walk; the walk terminates at the ending node titled "Ending — The Empty Boxes, Read Aloud" after visiting 38 nodes, with $70 of the $230 starting cash remaining. Walked path: The Clock You Cannot See → The Lawyer Draws the Clock → The Record Request → The Folder → A Visit, Counted → The Service That Is a Box → Paper With a Date On It → The Family Name in the Minutes → The Shift and the Hearing → The School Note → A Review, Mid-Clock → The Small Proof → Getting There → The Call You Make in Writing → The List → The Home Half-Ready → The Wider Family → The Second Letter → A Visit, Noted → The Folder, Audited → The Review Where the Date Is Said → The Call You Make in Writing — Again, On Paper → The List — Again, On Paper → The Home Half-Ready — Again, On Paper → The Wider Family — Again, On Paper → The Second Letter — Again, On Paper → A Visit, Noted — Again, On Paper → The Folder, Audited — Again, On Paper → The Review Where the Date Is Said — Again, On Paper → A Review, Mid-Clock — Again, On Paper → The Small Proof — Again, On Paper → The Packet → Rehearsing the Hearing → The Night Before → The Morning Of → The Services Track → The Fifteen-Month Review → Ending — The Empty Boxes, Read Aloud.*