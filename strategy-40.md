# Strategy Guide — Scenario 40: "The Letter with a Case Number"

*Game documentation for a fictional simulation in "The First 90 Days" (Tactic Watch). The family, the case, and every choice below are fictional. This guide is general information about how the scenario is built — it is not legal advice for any real case.*

## (1) The win

**Best ending: "Kept, Dated, Answered"**.

This is a **full** win. An investigation that arrives by letter is a case conducted at the speed of paper — an envelope, a postmark, a response window. The route treats each of those as evidence: the envelope is kept, the window is calendared off the postmark, the record is requested before the answer is written, and the answer is sent in writing inside the window. The file closes on findings the answer actually addressed.

## (2) The route

Verified by walking the scenario graph from the start node (see the verification note at the end). Key decision points, in order — node title, winning choice, and what it changes:

1. **The Envelope** — *Read the letter twice, then put it — and its envelope — in a folder, together.* Sets **envelopeKept**.
2. **The Window** — *Write the dates on the folder: letter date, postmark, today — the window, made visible.* Sets **datesLogged**.
3. **Read the File You're Answering** — *File the written request for the intake summary from your record.* Sets **recordsRequested**.
4. **The Yard, Documented** — *Assemble them: dated photo of the latch, the landlord texts, Mrs. Johansson's statement.* Sets **proofGathered**.
5. **The Call** — *Give the short account — and send the written answer today: porch, dated latch photo, texts, statement.* Sets **answerSent**.
6. **Point by Point** — *Ask him to describe the amended findings — and to send them in writing.* Sets **summaryInWriting**.
7. **One Word** — *Send the one-line note: the findings' dates govern the summary's shorthand.* Sets **correctionSent**.

## (3) Why this wins — the law as it is supposed to work

- **The envelope is part of the letter.** A response window runs from a date, and the postmark is the proof of which date. Keeping the envelope with the letter converts "the window" from something the agency asserts into something the parent can show.
- **Read the file before answering it.** Agency records are released on request — 55 Pa. Code § 3130.44(d). The written answer in this route responds point by point to the intake summary that exists, not to the three paragraphs of the letter, which are a summary of a summary.
- **Answers given on calls evaporate; answers sent in writing become findings' raw material.** The closing determination letter quotes the file. The route makes sure the file contains the answer — dated, with its attachments — before the determination is drafted.

## (4) The traps

1. **Answering the letter instead of the file** (the u-branch). Cost: the response addresses the summary's shorthand, and the closing adopts it — "Unsupervised, In the Summary" — a word the findings never supported, preserved because nobody answered the document underneath it.
2. **Discarding the envelope.** Cost: no **envelopeKept**, no **datesLogged** — the window becomes the agency's recollection of a date, and the answer's timeliness becomes arguable.
3. **Fixing the yard but not documenting it.** Cost: the repair is real and the file shows a fence in the same condition as the report described, because a dated photo was never taken.

## (5) What no strategy controls

The mail's speed, the worker's drafting habits, and whether the determination letter is written by the person who visited the yard. The route controls only what was ever controllable: that the envelope was kept, the dates were written on the folder, the record was requested before the answer, and the answer was sent in writing inside the window. Outcomes in this system turn on workers, judges, and luck as much as on any parent's choices — the strategy's claim is narrower: the summary that outlives this case describes what the findings found.

---
*Verification: this route was walked programmatically against `scenario-40.json` — each named choice was followed from the start node in order; the walk terminates at the ending node titled "Kept, Dated, Answered" after visiting 12 nodes, with $175 of the $175 starting cash remaining (no choice in this scenario carries a cash cost; the starting cash never moves). Walked path: The Envelope → The Window → Read the File You're Answering → The Yard, Documented → The Night Before He Calls → The Call → Point by Point → The Yard, Visited → Copies → The Determination Letter → One Word → Kept, Dated, Answered.*
