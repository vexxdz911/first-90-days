# Strategy Guide — Scenario 60: "The New Worker"

*Game documentation for a fictional simulation in "The First 90 Days" (Tactic Watch). The family, the case, and every choice below are fictional. This guide is general information about how the scenario is built — it is not legal advice for any real case.*

## (1) The win

**Best ending: "Ending — Continuity, Supplied by You."**

State it honestly: this is a **partial** win, and it is the best this scenario offers. The review report's three contested lines are corrected on the record — the completed program reads as completed, the passed screen reads as passed, the spring assessment reads as completed — because the correction was filed, with attachments, before the review convened. Silas does **not** come home at the end of this ending. His placement continues and the plan continues. The win is continuity itself: the case Mr. Wilkes inherited on paper is the case Marta actually lived, and every future reader of the file will meet that version first. There is no ending in this scenario where a worker change is painless. Anyone selling you one is selling you a different game.

## (2) The route

Verified by walking the scenario graph from the start node (see the verification note at the end). The walk passes, in order, through: The Goodbye Letter; What the Letter Says, and Doesn't; The Kitchen-Table Archive; Date Order; Mr. Wilkes, Week One; Two Lines, Both Wrong; The First-Week Letter; Sent, Copied, Dated; The Assessment, Again; The Certificate Answers; Ask for the File Itself; The Draft, With Template Lines; Correct It Where It Lives; Filed, Not Just Said; The Second Meeting; The Check-In Call; Visits, and Everything Else; Ms. Parr Builds the Packet; Date Order, Again; The Review. Key decision points:

1. **The Kitchen-Table Archive** — *Bring the binder current tonight — tabs, copies, everything in date order.* Cash −10. Sets **binderKept**; hidden item: the binder in date order from month one. This is the earliest choice in the scenario and the one every later room prices.
2. **The First-Week Letter** — *Send the status letter this week, with the certificates attached.* Cash −6. Sets **letterSent**. Sent inside Mr. Wilkes's first weeks, the letter is orientation; the same letter sent later would be a dispute. It makes the summary's stale lines expensive to repeat, because repeating them now means repeating them against attachments.
3. **The Assessment, Again** — *Answer in writing — attach the completion certificate and the dated sign-in page.* Cash −4. The re-order is withdrawn because the draft file copy is answered by the finished thing it was a draft of. Quietly redoing it (cash −30) buys a second, later date that the file will forever be tempted to mistake for the first.
4. **Ask for the File Itself** — *Sign the written request for the record — draft report, assessment copies, all of it.* Sets **recordsRequested**. This is what surfaces the draft review report — template lines and all — while every line in it is still soft enough to correct.
5. **Correct It Where It Lives** — *File the written correction before the review, certificates attached.* Cash −5. Sets **correctionFiled**. A correction filed weeks ahead becomes the report's new text; the same points raised orally at a meeting become a note on a busy worker's pad.
6. **Assemble the final packet (Date Order, Again)** — Cash −5. The packet filed for the court in date order: goodbye letter, the two lines as noted word for word, status letter, assessment correspondence, draft beside correction, the clean recent weeks.
7. **The Review** — *Present the corrected record — binder, first-week letter, record packet, and the correction filed before today.* This choice is flag-gated: it is only available with **binderKept** + **letterSent** + **recordsRequested** + **correctionFiled** all set. It leads to **Ending — Continuity, Supplied by You**.

Supporting route choices that cost nothing and keep the route honest: noting the two stale lines word for word at **Mr. Wilkes, Week One** (the correction is later built out of the exact sentences it corrects), and running the plan's ordinary weeks perfectly at **Visits, and Everything Else**, so the review reads a whole file that is clean, not only three repaired lines.

## (3) Why this wins — the law as it is supposed to work

Only principles from the scenario's verified set are stated here:

- **The case record is available on written request** — 55 Pa. Code § 3130.44(d) ("shall be released upon request"). Step 4 is that right, exercised in writing, and it is the highest-leverage move in the scenario: it converts a rumored draft into a quotable text, weeks before the review reads it.
- **The release has a lawful limit, and the route honors it** — released material may omit what violates another person's privacy or is protected or made confidential by law (55 Pa. Code § 3130.44(f)). The packet's redactions are accepted, not fought; what is fought is the stale text that no confidentiality claim ever protected.
- **Counsel assembles and files** (42 Pa.C.S. § 6337). Ms. Parr's work in the route is inventory, not eloquence: each stale line answered by its own attachment, filed where the next report writer cannot miss it.
- **Everything else is process, stated without citation on purpose:** a summary is a derivative document. It inherits the errors of the report it was copied from and lends them its own authority. The route wins by going underneath the summary to primary paper — certificate, result, sign-in page — and filing the correction where future summaries are written from.

## (4) The traps

1. **Leaving the shoebox as it is at "The Kitchen-Table Archive"** because you know what's in it. Cost: no **binderKept**, and the best presentation at the review closes. Knowledge that cannot be handed across a table is, in a review room, a rumor about yourself.
2. **Waiting at "The First-Week Letter"** for Mr. Wilkes to learn the case the way Ms. Renshaw did. She had eight months; the review is closer than that. Cost: no **letterSent** — the summary sets, report by report, and your later letter arrives as a dispute instead of as orientation.
3. **Redoing the assessment quietly at "The Assessment, Again."** Cost: cash −30, two appointments, and a second completion date in the file that future summaries can mistake for the only one — cooperation that manufactures the very lateness the plan will later hold against you.
4. **Raising the correction orally at "Correct It Where It Lives."** Mr. Wilkes agrees with every word, in person, and writes himself a note. Cost: no **correctionFiled**. The best presentation closes, and the correction that reaches the review at all arrives in the room, contested, at speaking speed — **"Ending — Reset, Then Repaired."** Presenting from memory alone reaches **"Ending — Starting Over at Month Nine"**: the stale lines harden into findings and the plan restarts services that were already completed.

## (5) What no strategy controls

Whether Mr. Wilkes is conscientious or merely busy; whether his supervisor contests a correction or waves it through; whether the report writer reads attachments or copies the last report; whether the next worker change lands next month and starts the whole problem over with a new reader. Silas's own timeline — a nine-year-old spending his ninth year between two homes while adults correct his file — is not controlled by any of this either, and the route does not pretend otherwise. What the route controls is narrower: when the file was wrong, the correction existed as dated paper, filed early, in the room before the room convened. Outcomes in this system turn on workers, judges, and luck as much as on any parent's choices. The strategy's whole claim is that a handoff should not get to tax a parent's record for the handoff's own incompleteness — and that the tax, when it comes, is payable in copies and stamps instead of in months.

---
*Verification: this route was walked programmatically against `scenario-60.json` — each named choice was followed from the start node in order; every intermediate node and choice exists; every flag-gated choice's requirements were satisfied by flags set earlier on the walk (flags at the ending: binderKept, correctionFiled, letterSent, recordsRequested); cash never went negative on the walk. Walked path: start → handover_note → binder_beat → binder_kept → first_meeting → stale_detail → letter_choice → letter_sent → reorder → attach_cert → records_beat → record_arrives → correction_choice → correction_filed → second_meeting → wilkes_checkin → visits_meanwhile → review_prep → packet_assembly → review → end_win. The walk terminates at the ending node titled "Ending — Continuity, Supplied by You" after visiting 21 nodes, with $130 of the $160 starting cash remaining.*
