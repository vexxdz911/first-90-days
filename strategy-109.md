# Strategy Guide — Scenario 109: "The Check That Kept Coming"

*Game documentation for a fictional simulation in "The First 90 Days" (Tactic Watch). The family, the case, and every choice below are fictional. This guide is general information about how the scenario is built — it is not legal advice for any real case.*

## (1) The win

**Best ending: "Ending — The Lag, On the Record."**

State it honestly: this is a **partial** win, and it is the best this scenario offers. The repayment is addressed through the letter's own process on a documented lag — the response form filed inside the window the letter itself stated, with the agency's own chronology attached — and the case note is corrected on the record to state that chronology instead of "mother retained child's benefits." Emeka does **not** come home at the end of this ending. His placement continues and his case continues, and any remaining balance follows the letter's own process on this record. The win is that the file now tells the truth about whose forty-two days they were. There is no ending in this scenario where the letter is simply torn up. Anyone selling you one is selling you a different game.

**A withholding that governs this whole guide:** no rule of any benefit program — no payee rule, no overpayment rule, no eligibility or amount rule — is stated anywhere in the scenario or in this guide, because none is in the project's verified law set. Everything procedural about the repayment comes from the fictional letter's own face: its stated amount, its enclosed response/waiver-request form, and its stated window. The strategy is documentary, not doctrinal, on purpose.

## (2) The route

Verified by walking the scenario graph from the start node (see the verification note at the end). The walk passes, in order, through: The Letter About the Money; What the Letter Itself Says; Spent the Way It Always Was; The Bank's Version; In and Out, in Type; The Landlord's Signature; Two Dates in One File; Ask for the Chronology; Forty-Two Days, in Their Own Hand; Five Words in a File; The Visit, Meanwhile; One Page of Dates; Six Lines, No Adjectives; The Form, Inside Its Own Window; Filed, With Days to Spare; Weeks of Ordinary Case; The Next Envelope; Ms. Harrington Builds the Packet; The Review. Key decision points:

1. **The Bank's Version** — *Order the bank statements for the six weeks and keep the bank's receipt.* Cash −6. Sets **bankRecords**. The bank's chronology — payments in, rent out — is the one account of the six weeks nobody can call the mother's version of events.
2. **Ask for the Chronology** — *Sign the written request for the record — chronology, processing entries, and the note.* Cash −3. Sets **recordsRequested**. This is the highest-leverage move in the scenario: it surfaces the agency's own entries showing the placement known on Monday, August 24, 2026 and the payee change processed six weeks later, in the week of Monday, October 5, 2026. The lag stops being a theory and becomes a subtraction any reader can do.
3. **One Page of Dates** — *Build the one-page timeline from the chronology, the statements, and the receipts.* Sets **timelineBuilt**. Six lines, no adjectives: placement, payments, rent, processing entry, letter. A lag shown is worth more than a lag argued.
4. **The Form, Inside Its Own Window** — *File the form inside the window — timeline, chronology, statements and receipts attached.* Cash −3. Sets **responseFiled**. The letter stated its window on its face — return the form by Wednesday, November 4, 2026 — and the filing lands Monday, November 2, 2026, disputing the claim on the documented lag, asking on the form's own line that repayment be waived or reduced, and asking separately that the case note be corrected to match the chronology.
5. **The Review** — *Present the documented lag — the agency chronology, the timeline, and the response filed inside the letter's window.* Cash −6 for the day. This choice is flag-gated: it is only available with **bankRecords** + **recordsRequested** + **timelineBuilt** + **responseFiled** all set. It leads to **Ending — The Lag, On the Record**.

Supporting route choices that cost nothing and keep the route honest: laying the landlord's signed rent receipts beside the bank statements at **The Landlord's Signature** (a third hand confirming the same six weeks), and keeping every later paper in date order through **Weeks of Ordinary Case**, so the review packet's order is its proof.

## (3) Why this wins — the law as it is supposed to work

Only principles from the scenario's verified set are stated here:

- **The case record is available on written request** — 55 Pa. Code § 3130.44(d) ("shall be released upon request"). Step 2 is that right, exercised in writing and aimed precisely: the placement chronology and the processing entries. Requesting the record is what puts the agency's processing date beside its placement date, where the forty-two days compute themselves.
- **Counsel assembles and files** (42 Pa.C.S. § 6337). Ms. Harrington's work is chronology, not eloquence: a one-page timeline with a document behind every line, attached to the letter's own form, filed inside the letter's own window.
- **Everything else is the letter's own process, used exactly as the letter instructs** — and that is stated without any program citation on purpose. The fictional letter encloses its own response/waiver-request form and states its own deadline; following a process a letter offers, on its own paper, inside its own window, requires no doctrine at all. The scenario deliberately claims no benefit-program rule, because the win never needs one: it needs dates.

## (4) The traps

1. **Working from memory at "The Bank's Version"** because you know exactly what you spent it on. Cost: no **bankRecords**, and the best presentation at the review closes. Memory attaches to nothing; a form is answered by attachments or it is answered by its own claim.
2. **Answering from your own paper alone at "Ask for the Chronology"** because the receipts speak for themselves. Receipts speak about rent. About the lag they are silent, because the lag never happened in your kitchen — it happened in a processing queue, and its date lives only in the record you declined to request. Cost: no **recordsRequested**, and the middle of the timeline stays missing in every later room.
3. **Paying the amount silently at "The Form, Inside Its Own Window."** The letter's account closes; the note's five words do not. Payment answers a letter, never a file, and a later reader may take the payment filed beneath those five words as agreement with them. This route reaches **"Ending — Paid, and Still Written That Way."**
4. **Letting the window close at the same node** because the case will be calmer later. Cases are never calmer later, and unanswered letters do not wait — they ripen into restated balances and a second file fact, notified-and-not-answered, sitting beside the note. This route reaches **"Ending — The Letter, Ripened."**

## (5) What no strategy controls

Whether the reader of the filed response weighs a documented lag generously or grudgingly; whether the reviewer corrects the note's wording and still presses Emeka's plan exactly as hard; whether a landlord in another story keeps poor receipts; whether the processing queue that caused all of this moves faster next time, for someone else. Emeka's own timeline — a nine-year-old in placement while adults subtract dates about his money — is not controlled by any of this either, and the route does not pretend otherwise. What the route controls is narrower: when the system took six weeks to process its own change, the proof of those six weeks existed — dated, attached, and filed inside the window the letter itself set. Outcomes in this system turn on workers, readers, reviewers, and luck as much as on any parent's choices. The strategy's whole claim is that a lag should be billed, on paper, to the desk where it happened.

---
*Verification: this route was walked programmatically against `scenario-109.json` — each named choice was followed from the start node in order; every intermediate node and choice exists; every flag-gated choice's requirements were satisfied by flags set earlier on the walk (flags at the ending: bankRecords, recordsRequested, responseFiled, timelineBuilt); cash never went negative on the walk. Walked path: start → letter_close → rent_open → bank_choice → bank_ordered → receipts_beat → counsel_visit → records_fork → record_arrives → note_phrase → emeka_visit → timeline_choice → timeline_built → response_choice → response_filed → wait_weeks → agency_reply → prep → review → end_win. The walk terminates at the ending node titled "Ending — The Lag, On the Record" after visiting 20 nodes, with $138 of the $160 starting cash remaining.*
