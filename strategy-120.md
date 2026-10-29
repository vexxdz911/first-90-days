# Strategy Guide — Scenario 120: "The Medicine Log"

*The First 90 Days — a fictional composite. Fictional composites only; no real person or case. General information about how these hearings work, not legal advice.*

> **Route verification:** this guide's winning route was graph-walked programmatically through `scenario-120.json` (every step is a legal choice; every `requiresFlags` gate satisfied by flags accumulated earlier on the route; cash never negative). Path and totals are printed at the end.

## 1. The win

**"Ending — Every Change in Writing"** — the full win.

At the February 18 permanency hearing, the court **finds**: medication changes for a placed child are treatment decisions that belong in the record; the agency's practice produced a change the mother learned from a pharmacy bag. The court **orders** a medication log — drug, dose, date, prescriber, reason — maintained at the resource home and copied to the mother **monthly and at every change**, prescriber notification to the mother before non-urgent dose changes take effect, and Siobhan's own recorded views on the medication attached to the next court report. The win is structural: the next change, whenever it comes, arrives as a document with a reason, addressed to the mother — not as a bag on a counter.

## 2. The route — graph-verified

1. **The Bag on the Counter** ("What the Pharmacy Knew First") → **"Write it down tonight — bottle, label, dose, date — and keep the bag."** The discovery is preserved as an exhibit, not an anecdote.
2. **The Questions** → **"Send all three in writing tonight. Paper remembers what December forgets."** Sets `logRequested` — log, prescriber, and record, asked for in one dated letter.
3. **The Record Request** — the written § 3130.44(d) request goes out with the same letter. Sets `recordsRequested`.
4. **Her Daughter's Account** → **"Write her words down, verbatim, and date them."** Sets `siobhanHeard` — Siobhan's own description of the fog, in her words, enters the file through her mother and her GAL.
5. **The Prescriber** → **"Send the questions. A prescriber who answers a parent in writing has joined the record."** Sets `prescriberAsked` — Dr. Anwar answers: the increase was clinical, the routing failure is named by the prescriber herself, and a school note is promised.
6. **The Hearing** (dispatcher: `recordsRequested` + `prescriberAsked` + `siobhanHeard`) → **"Ask for the log ordered, the notice ordered, and Siobhan's views attached to every report."**

**Programmatically walked path (21 nodes):** start → how_siobhan → ellery_call → lawyer120 → request_sent → respite_story → pharmacy_bag → siobhan_words → visit2 → ellery_log → partial_log → prescriber_letter → school_note → noor_reply → gal_view → packet120 → agency_report120 → renner_whiteboard → night_before120 → hearing120 → end_writing. **Ending cash: $137 of $150 left.** *(Note: two node ids in the data retain the prescriber's pre-rename surname — `noor_reply` — the character is Dr. Anwar throughout the text.)*

## 3. Why this wins — the law

As with Scenario 119, this guide states no medical-consent statute — none was verified from primary text during this run — and the win is built from the verified dependency machinery instead:

- **Information about a child in placement is a status-hearing subject.** At a status review/permanency hearing the court reviews the child's safety, the continuing necessity and appropriateness of the placement, compliance with the permanency plan, and the progress made toward alleviating the circumstances that necessitated placement — 42 Pa.C.S. § 6351(f)(1). A medication change nobody documented is a compliance and safety fact the court can find and order corrected.
- **Appropriateness of a service runs to its manner.** In determining the appropriateness of a service the court may consider whether the child has been provided the opportunity to participate in the planning and provision of the service — § 6351(e)(3)(i), as worded in prior batches. A 14-year-old's recorded views on her own medication are a § 6351 subject, not a courtesy.
- **Medication changes are exactly the kind of event that belongs in the child's record.** The verified set's discipline about records — what is in them, who may see them (§ 3130.44(d)), and the principle that a record's contents are the evidentiary basis on which hearings proceed — carries the story: the agency file held the order, a three-line entry, and a note nobody routed. The order the court writes converts that gap into a maintained, shared log.
- **A parallel body of law on consent to psychotropic medication for placed children exists in many jurisdictions' rules and agency regulations**; this guide does not state it, because it was not verified from primary sources during this run. The scenario's win does not depend on it.

## 4. The traps

- **The log, eventually** (The Log, Eventually (partial)): asking once and trusting produces a real log — kept at the home, shown at visits, never copied to the mother. At the hearing the court notes improvement and moves on; the next change is discoverable the same way the first was. Partial, and labeled partial in the data.
- **Never writing the questions** (The Bag on the Counter): the February report records that "mother raised concerns about medication communication" — her concern becomes a sentence about her, and no document ever answers it.
- **Skipping Siobhan's own account**: without her words, the hearing hears two systems describe a 14-year-old's inner life. Her statement, carried by the GAL, is the only first-person evidence in the room about the medicine itself.

## 5. What no strategy controls

Whether the medication is the right one, at the right dose — that is Dr. Anwar's clinical judgment, and the scenario never asks the court to practice medicine. Whether Mrs. Ellery's care is warm (it is) and whether her kitchen notebook-keeping becomes reliable under an order; whether Siobhan's fog is the drug, the dose, the hour, or adolescence; and whether the agency's other homes document any better. The strategy controls the documentation duties and the notice — the conditions under which a mother can be a participant in her daughter's treatment instead of its audience. It cannot control the treatment itself, and this guide does not pretend otherwise.
