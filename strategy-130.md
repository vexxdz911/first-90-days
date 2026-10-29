# Strategy Guide — Scenario 130: "Across the County Line"

*Game documentation for a fictional simulation in "The First 90 Days" (Tactic Watch). The family, the case, and every choice below are fictional. This guide is general information about how the scenario is built — it is not legal advice for any real case.*

## (1) The win

**Best ending: "Ending — The File Arrived Whole."**

This win is labeled **partial** in the data and meant honestly: the petition is never filed, the compelling reason holds across the county line, and the children complete a trial return to full return — but the case spans its full fifteen months to get there. The capstone skill it teaches is chain-of-custody for a record: inventory before, confirmation after, and the exception documented in the case plan *before* the file travels.

## (2) The route

Verified by walking the scenario graph from the start node (see the verification note at the end). Key decision points, in order — node title, winning choice, and what it changes:

1. **Two Children, Two Clocks** — *Tell your lawyer, Mr. Ndiaye, before you tell anyone else* Sets **lawyerTold**.
2. **The Winter, Itemized** — *Write the winter as a one-page chronology and give it to Mr. Ndiaye* Sets **winterWritten**.
3. **The Transfer Problem** — *Build the transfer inventory with him: every document, its date, its location in the file* Sets **inventoryBuilt**.
4. **The Offer, On Letterhead** — *File the offer letter together with the transfer plan, as one exhibit* Sets **offerFiled**.
5. **The Exception Packet, So Far** — *Sign the written record request today* Cash −$5; Sets **recordsRequested**.
6. **The Second Set** — *Make the second set and store it outside both counties' buildings* Cash −$10; Sets **secondSet**.
7. **What the Record Holds** — *File a dated statement: the job, the address, the school plan, the transfer request — beside the note, not against it* Cash −$5; Sets **statementFiled**.
8. **Indexing the Winter** — *Number and index every page; list the two gaps as items in the index* Sets **recordIndexed**.
9. **The Plan, Amended in Writing** — *Get the signed amended plan and the transfer letter before you give notice at the warehouse* Cash −$5; Sets **packetBuilt**.
10. **The Schools, Notified in Writing** — *Send the letters and confirm receipt with both schools* Cash −$5; Sets **schoolsNotified**.
11. **Moving Day Arithmetic** — *Send the receiving county a one-page introduction with your inventory attached — politely, through your lawyer* Cash −$5; Sets **introSent**.
12. **Notice, Given Properly** — *File the supervisor's letter with the employment documents* Sets **supervisorLetter**.
13. **The Other Paperwork** — *Log every confirmation number in the folder, dated* Sets **seamsLogged**.
14. **The New County's Reading** — *Ask her to confirm, in writing, that the packet arrived complete against the inventory* Sets **arrivalConfirmed**.
15. **The Intake Call** — *Offer to walk the inventory with her when the box lands, page by page* Sets **walkOffered**.
16. **School, Services, Sundays** — *Keep the rhythm: every letter filed, every log countersigned, the folder mirrored* Sets **rhythmKept**.
17. **Page 88** — *Produce the second set's copies of pages 88–89 and amend the arrival confirmation to note the cure* Cash −$5; Sets **gapCured**.
18. **The Amended Confirmation** — *File the amended confirmation at the front of the new county's packet* Sets **amendedFiled**.
19. **The Receiving Review** — *Ask, through counsel, for the step-down the plan promised: overnights expanding to a trial return before the holidays* This choice is flag-gated: it is only available with **recordsRequested** + **packetBuilt** + **arrivalConfirmed**.
20. **The Fall Review** — *Ask for the condition in the order's words: overnights by spring if the log and letters continue* Sets **conditionWritten**.
21. **The Goal, Questioned Once** — *File a short written response quoting the plan's entry and the fall order, with dates* Cash −$5; Sets **goalAnswered**.
22. **The Holidays, Documented** — *Keep the holiday log and file the caseworker's note with it* Sets **holidayLogged**.

Supporting choices along the same walk — every "paper version" choice (dated, copied, filed), every written request, and every dated letter — add the documentation the packet is later assembled from. The full walked path is printed in the verification note.

## (3) Why this wins — the law as it is supposed to work

- **The clock does not pause for geography.** Entry Monday, January 5, 2026 → fifteen of the most recent twenty-two months on Monday, April 5, 2027 (42 U.S.C. § 675(5)(E)), in whichever county holds the case. The parallel state review determination is made under 42 Pa.C.S. § 6351(f)(9).
- **The compelling-reason exception is a case-plan sentence or it is nothing.** Section 675(5)(E)'s exception requires the agency to have *documented* a compelling reason in the case plan. A supervisor's verbal agreement in the sending county binds no one in the receiving county; the signed amendment does.
- **Count the file before it travels.** The record request (55 Pa. Code § 3130.44(d)) must precede the move, because an inventory can only be built from a seen record; redactions under (f) are expected and itemized like everything else.
- **Counsel as logistics** (42 Pa.C.S. § 6337): the introduction and inventory go to the receiving county through the lawyer, and arrival is confirmed in writing against the inventory — the receiving caseworker's 'mostly' converted into arithmetic.

## (4) The traps

1. **Assuming the counties handle the transfer between themselves at "The Transfer Problem"** — summaries travel; packets get 'routinized' into four pages — the route to **The Thin File**.
2. **Asking for the early case note to be removed at "What the Record Holds"** — files don't unwrite; the dated statement filed *beside* the note is the correction that survives the trip.
3. **Accepting 'mostly arrived' without written confirmation** — the win's gate requires **arrivalConfirmed**; an unconfirmed loss discovered in April cannot be proved, and what cannot be proved cannot be cured — the route settles for the trial leash.
4. **Relaxing the documentation rhythm in the new county** — the receiving court reads the whole film, including the quiet autumn; a packet is a habit, not an event.

## (5) What no strategy controls

The receiving county's staffing and intake stack, the new judge's caution, and the scan queue between two buildings. The route controls the chain of custody — and in a crossing case, custody of the paper is custody of the story.

---
*Verification: this route was walked programmatically against `scenario-130.json` — each named choice was followed from the start node in order; every flag-gated choice's requirements were satisfied by flags set earlier on the walk; the walk terminates at the ending node titled "Ending — The File Arrived Whole" after visiting 24 nodes, with $125 of the $170 starting cash remaining. Walked path: Two Children, Two Clocks → The Winter, Itemized → The Transfer Problem → The Offer, On Letterhead → The Exception Packet, So Far → The Second Set → What the Record Holds → Indexing the Winter → The Plan, Amended in Writing → The Schools, Notified in Writing → Moving Day Arithmetic → Notice, Given Properly → The Other Paperwork → The New County's Reading → The Intake Call → School, Services, Sundays → Page 88 → The Amended Confirmation → The Receiving Review → The Fall Review → The Goal, Questioned Once → The Holidays, Documented → The Fifteenth Month, Elsewhere → Ending — The File Arrived Whole.*
