# Strategy Guide — Scenario 132: "The Hearing That Read the Year"

*Game documentation for a fictional simulation in "The First 90 Days" (Tactic Watch). The family, the case, and every choice below are fictional. This guide is general information about how the scenario is built — it is not legal advice for any real case.*

## (1) The win

**Best ending: "Ending — Home From the Hearing."**

This is a **full** win — Maialen home from the hearing itself — and the library's proof case for its own doctrine. It is labeled full because the outcome is complete (return ordered at the hearing, case set to close at winter review) and because the scenario exists to demonstrate the ceiling of the paper strategy when every discipline is executed without a miss for fourteen months.

## (2) The route

Verified by walking the scenario graph from the start node (see the verification note at the end). Key decision points, in order — node title, winning choice, and what it changes:

1. **Month Fourteen, Minus One** — *Treat the month as a production schedule: every document, dated, filed, indexed* Sets **productionSet**.
2. **Fourteen Months in One Sentence** — *Carry the page to its file* Cash −$5; Sets **paperTrail**.
3. **The Horizon, Named** — *Carry the page to its file* Cash −$5; Sets **paperTrail**.
4. **The Inventory of a Year** — *List the gaps as tasks with owners and dates, not as worries* Sets **gapList**, **recordsRequested**.
5. **Tabs, Numbered** — *Carry the page to its file* Cash −$5; Sets **paperTrail**.
6. **The Copies** — *Carry the page to its file* Cash −$5; Sets **paperTrail**.
7. **The Missing Month** — *Ask Ms. Grey for the calendar pages and file them with the explanation* Cash −$5; Sets **gapCured**.
8. **October, Reconstructed on Paper** — *Carry the page to its file* Cash −$5; Sets **paperTrail**.
9. **The Rotation, Explained by Its Author** — *Carry the page to its file* Cash −$5; Sets **paperTrail**.
10. **The Exception Question, In Writing** — *Send it by a method that proves delivery, and calendar the silence* Cash −$5; Sets **exceptionAsked**.
11. **The Calendar, Copied at the Kitchen Table** — *Carry the page to its file* Cash −$5; Sets **paperTrail**.
12. **The Explanation, One Page** — *Carry the page to its file* Cash −$5; Sets **paperTrail**.
13. **The Record, Refreshed** — *Index the refresh into the packet and note the exception letter's status by date* Sets **recordRefreshed**.
14. **The Silence, Calendared** — *Carry the page to its file* Cash −$5; Sets **paperTrail**.
15. **The Refresh, Requested Meanwhile** — *Carry the page to its file* Cash −$5; Sets **paperTrail**.
16. **Maialen's School Page** — *File the teacher's letter and the attendance record* Sets **schoolFiled**.
17. **The Winter Choir** — *File it and note its date in the inventory* Sets **paperTrail**.
18. **The Employer's Page** — *Do the paper version: dated, copied, filed* Cash −$5; Sets **paperTrail**.
19. **The Aunt's Standing Offer** — *File Josune's letter in the packet under both tabs* Sets **kinLetter**.
20. **The Pediatrician's Paragraph** — *Carry the page to its file* Cash −$5; Sets **paperTrail**.
21. **The Neighbor's Line** — *Carry the page to its file* Cash −$5; Sets **paperTrail**.
22. **The Chorus, Indexed** — *Carry the page to its file* Cash −$5; Sets **paperTrail**.
23. **The Packet's First Page** — *Sign it and file the packet two weeks before the hearing* Cash −$10; Sets **packetBuilt**.
24. **The First Page, Read Aloud** — *Carry the page to its file* Cash −$5; Sets **paperTrail**.
25. **The Filing Receipt** — *Carry the page to its file* Cash −$5; Sets **paperTrail**.
26. **The Agency Answers, Partly** — *Prepare your testimony to match the packet, page for page — nothing new, nothing contradicted* Sets **testimonyReady**.
27. **Reading Their Answer Closely** — *Carry the page to its file* Cash −$5; Sets **paperTrail**.
28. **No Position, Positioned** — *Carry the page to its file* Cash −$5; Sets **paperTrail**.
29. **The Last Week's Quiet Jobs** — *Carry the page to its file* Cash −$5; Sets **paperTrail**.
30. **Questions at Kitchen-Table Speed** — *Carry the page to its file* Cash −$5; Sets **paperTrail**.
31. **The Drawings, Decided** — *Carry the page to its file* Cash −$5; Sets **paperTrail**.
32. **The Hearing That Read the Year** — *Ask for the order: return home today, aftercare and Josune's respite in writing, case to close at the winter review* This choice is flag-gated: it is only available with **recordsRequested** + **packetBuilt** + **gapCured** + **exceptionAsked**.

Supporting choices along the same walk — every "paper version" choice (dated, copied, filed), every written request, and every dated letter — add the documentation the packet is later assembled from. The full walked path is printed in the verification note.

## (3) Why this wins — the law as it is supposed to work

- **The fifteen-month question, asked early.** Entry August 4, 2025 → fifteen months Wednesday, November 4, 2026 (42 U.S.C. § 675(5)(E); review determination under 42 Pa.C.S. § 6351(f)(9)). The route's signature move is putting the exception question to the agency *in writing, a month before the hearing* — their answer documents an exception; their silence documents that the question was asked and the progress was, in their own later filing, 'substantial and documented.'
- **Gaps are cured from other chairs' paper.** The missing visit month is repaired not by testimony but by the foster caregiver's own calendar — the file as ecosystem. A hearing cross-examines absences; it cannot cross-examine a countersigned calendar.
- **The mirror, refreshed.** An updated record request (55 Pa. Code § 3130.44(d)) before the hearing prevents arguing from a nine-month-old file; redactions under (f) are indexed as rules, not treated as concealment.
- **Counsel as editor-in-chief** (42 Pa.C.S. § 6337): the packet's first page — nine dated sentences — is the hearing's steering document, and testimony is prepared *against* the packet so the witness and the book never contradict each other in the room.

## (4) The traps

1. **Skipping the missing month — 'one month in fourteen can't decide a hearing'** — one month is precisely the cross-examination's size. The win's gate requires **gapCured**; uncured, the hearing becomes **The Contested Reading**.
2. **Saving the exception question for cross-examination** — surprise is a trial tactic; in a permanency hearing, the unanswered letter is worth more than the ambush — its dated silence is an exhibit.
3. **Preparing testimony beyond the packet** — witnesses who outrun their exhibits contradict them; the packet's story, in the parent's voice, is the whole performance.
4. **Filing the packet the Friday before** — judges read on weekends. The early filing is why the agency's response conceded the ground before the hearing began.

## (5) What no strategy controls

The judge's temperament, the agency's choice to contest or concede, and the original accident. The route controls the book — completeness, currency, and the questions asked in writing in time. This scenario is the argument that, at the ceiling, the book is enough.

---
*Verification: this route was walked programmatically against `scenario-132.json` — each named choice was followed from the start node in order; every flag-gated choice's requirements were satisfied by flags set earlier on the walk; the walk terminates at the ending node titled "Ending — Home From the Hearing" after visiting 34 nodes, with $65 of the $190 starting cash remaining. Walked path: Month Fourteen, Minus One → Fourteen Months in One Sentence → The Horizon, Named → The Inventory of a Year → Tabs, Numbered → The Copies → The Missing Month → October, Reconstructed on Paper → The Rotation, Explained by Its Author → The Exception Question, In Writing → The Calendar, Copied at the Kitchen Table → The Explanation, One Page → The Record, Refreshed → The Silence, Calendared → The Refresh, Requested Meanwhile → Maialen's School Page → The Winter Choir → The Employer's Page → The Aunt's Standing Offer → The Pediatrician's Paragraph → The Neighbor's Line → The Chorus, Indexed → The Packet's First Page → The First Page, Read Aloud → The Filing Receipt → The Agency Answers, Partly → Reading Their Answer Closely → No Position, Positioned → The Last Week's Quiet Jobs → The Night Before the Reading → Questions at Kitchen-Table Speed → The Drawings, Decided → The Hearing That Read the Year → Ending — Home From the Hearing.*
