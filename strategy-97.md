# Strategy Guide — Scenario 97: "The Plan, Mailed Inside"

*Game documentation for a fictional simulation in "The First 90 Days" (Tactic Watch). The family, the case, and every choice below are fictional. This guide is general information about how the scenario is built — it is not legal advice for any real case.*

## (1) The win

**Best ending: "The Credit on Paper."**

State it honestly: this is a **partial** win, and it is the best this scenario offers. Rowan stays with his grandmother Dolores, Terrence's completed work is corrected onto the record, and the return-home step on his release is written into the plan with a review date named. Terrence is **still inside** when the story ends — release is weeks away — and Rowan does not come home in this ending either. What the route wins is the thing the review was actually deciding: whether a semester of work done behind a wall exists in the only place the system reads, the file. There is no ending in this scenario where the prison door opens early. Anyone selling you one is selling you a different game.

## (2) The route

Verified by walking the scenario graph from the start node (see the verification note at the end). Key decision points, in order — node title, winning choice, and what it changes:

1. **A Report About a House He Is Not In** — *Ask your mother, Dolores, to write down tonight that Rowan can live with her — her name, her address, and that she is saying yes.* Sets **kinshipNamed**; hidden item: grandmother named in writing on day one as Rowan's placement. Kinship enters this case as a document, not a phone call.
2. **Ms. Kovich Meets Dolores** — *Dolores hands Ms. Kovich the written note and asks to be heard on her qualifications at any hearing.* Sets **kinshipStated**; hidden item: the home as observed — Rowan settled, spare room made up, school bag by the door.
3. **The Arrangement, On Paper** — *Read every line together before Dolores signs, and circle the check-in date.* Sets **readPlan**. Reading first surfaces the video-visit term nobody had said out loud.
4. **The Plan, Mailed Inside** — *Write back the same day: acknowledge the plan, list its steps back in his own words, and ask for a complete copy for his folder.* Cash −4. Sets **planAcknowledged**.
5. **Pages 4 Through 6, Missing** — *Ask, in writing through his attorney, for the missing pages before the step deadlines start.* Sets **planComplete**. The incomplete copy is reported before anyone can call the unseen steps ignored.
6. **Mr. Salas, On the Clock** — *Use the call to fix the steps and dates, and ask Mr. Salas to confirm them in a follow-up letter.* Sets **stepsWritten**. Steps confirmed in counsel's letter, not held in memory from an eleven-minute call.
7. **Classes Behind the Wall** — *Attend every session, and ask after each one for a copy of his sign-in or a dated note of attendance.* Sets **classesEnrolled**; hidden item: attendance being documented session by session at the father's request. The binder stays in the library; the copies are what travel.
8. **Video Visit, Fifteen Minutes** — *Ask Dolores to keep her own dated log of every video visit — date, length, one line about Rowan.* Sets **visitLog**. Two logs in two buildings are hard to lose.
9. **The Work Detail Log** — *Ask the supervisor for a dated note of the work record, and mail a copy out to Dolores.* Cash −4. Sets **workRecorded**.
10. **Certificates in an Envelope** — *Mail copies of both certificates to Dolores and to Mr. Salas, with a dated cover letter — the originals stay in his folder.* Cash −6. Sets **certificatesFiled** — one of the three flags the review's winning choice is gated on.
11. **Dolores Carries the Paper** — *Dolores hands over the certificate copies at the door and asks Ms. Kovich to note the handover date.* Sets **copiesHanded**. A handover with a date is a fact; a handover described is a claim.
12. **A Line in a Letter** — *Sign the written record request and send it this week, through Mr. Salas, keeping a dated copy.* Cash −4. Sets **recordsRequested**. This is the highest-leverage move in the scenario: it is how Terrence learns, in February, that his file reads "no progress" — while a correction can still land before the March review.
13. **The Correction, In Pencil First** — *Build the full correction — dates first, certificates and the visit log attached, copies for the agency, Dolores, and counsel.* Cash −6. Sets **correctionFiled**. The correction lists facts with dates; it does not argue.
14. **Three Copies** — *File the correction this week, before the review, and keep the stamped copy.* Sets **filedBeforeReview**. Paper filed before a hearing is paper the other side has read.
15. **Dolores Will Be Heard** — *Dolores prepares her one page — qualifications in order, each one backed by a document she can hand over.* Sets **kinshipHeard**.
16. **The Review Hearing** — *Hand up the correction — the requested record answered with certificates, the work note, and Dolores's log — and have Dolores heard on her qualifications.* This choice is flag-gated: it is only available with **recordsRequested** + **certificatesFiled** + **correctionFiled** all set. It leads to **The Credit on Paper**.

Supporting route choice: reading the packet line by line with Mr. Salas at **What the File Says: Nothing** — the single forced beat where the four empty boxes become a list instead of a fear.

## (3) Why this wins — the law as it is supposed to work

Only principles from the scenario's verified set are stated here:

- **Kinship is a legal category, not a sentiment.** Dolores is a potential kinship care resource as defined at 42 Pa.C.S. § 6302, and under 42 Pa.C.S. § 6336.1 (as amended by Act 48 of 2023) she may be heard at a hearing on her qualifications to provide kinship care. Steps 1, 2, and 15 are that framework used precisely: named in writing on day one, and heard on the narrow subject the law seats her for.
- **Counsel is part of the machinery** (42 Pa.C.S. § 6337). Nearly every winning move in this scenario travels through Mr. Salas — the missing-pages request, the steps letter, the record request, the correction — because from inside, counsel is the father's postal service, photocopier, and filing clerk as well as his advocate.
- **Agency records are obtainable on request** — 55 Pa. Code § 3130.44(d) ("shall be released upon request"). Step 12 is that right exercised in writing, and it is what converts the file's quiet verdict — "no progress noted" — from a March surprise into a February worklist. The system's failure mode here is documented across the published cases: work recorded nowhere because referrals, handoffs, and binders in other buildings never reached the file. The correction answers the file with the file's own missing contents.
- **The review decides on the record in front of it.** The review is the court's placement and plan review (42 Pa.C.S. § 6351). Nothing in the winning route persuades anyone of Terrence's worth; it ensures that when the court reviews placement and the plan, the progress items are documents with dates instead of a voice on a phone line saying *trust me*.

## (4) The traps

1. **Keeping the certificates safe in his locker folder** at "Certificates in an Envelope." Cost: no **certificatesFiled** — the review's winning choice is flag-gated on it, so the best ending closes. Safe and invisible are the same address in this system.
2. **Asking Ms. Kovich to just tell him what the file says** at "A Line in a Letter." Cost: no **recordsRequested**, and worse than the flag: he never sees the "no progress" boxes at all, so there is nothing to correct. The first time he hears the file's version is at the review, where it is read as fact.
3. **Sending a short letter saying he disagrees and has been trying hard** at "The Correction, In Pencil First." Cost: no **correctionFiled**. Trying hard, without dates and attachments, reads in a file exactly like the empty boxes it answers — the correction's power is entirely in its exhibits.
4. **Describing the classes himself over the phone line** at "The Review Hearing." Cost: the whole case. It is all true, and it leads directly to "The File Nobody Corrected" — placement formalized, the plan escalated, and the progress record restarted from zero on the day of the hearing.

A supporting trap: working from the three-page plan copy at "Pages 4 Through 6, Missing" without reporting it in writing. The unseen steps do not disappear; only his proof that he never saw them does.

## (5) What no strategy controls

The prison mail room. A housing transfer that moves a man away from his class, his folder, or his lawyer's visiting day. An instructor who does not keep the binder. A grandmother's health, a caseworker's caseload, a judge's crowded morning. The route controls only what was ever controllable from a cell: that the asks were written, the copies travelled, the request was signed, and the correction was filed before the hearing it answered. Outcomes in this system turn on workers, judges, and luck as much as on any parent's choices — the strategy's whole claim is narrower: when the review opened the file, the work was in it.

---
*Verification: this route was walked programmatically against `scenario-97.json` — each named choice was followed from the start node in order; every intermediate node and choice exists; every flag-gated choice's requirements were satisfied by flags set earlier on the walk; the walk terminates at the ending node titled "The Credit on Paper" after visiting 18 nodes, with $66 of the $90 starting cash remaining.*
