# Strategy Guide — Scenario 124: "The Whole Page"

*The First 90 Days — a fictional composite. Fictional composites only; no real person or case. General information about how these hearings work, not legal advice.*

> **Route verification:** this guide's winning route was graph-walked programmatically through `scenario-124.json` (every step is a legal choice; every `requiresFlags` gate satisfied by flags accumulated earlier on the route; cash never negative). Path and totals are printed at the end.

## 1. The win

**"Ending — The Whole Page, Read Aloud"** — the full win, on this scenario's honest terms.

At the December 10 permanency hearing, the court **reads the whole page**: the excerpt is struck as a characterization of Dr. Sayegh's position; her filed letter and the rebuttal worksheet are admitted; the assessment's summary may be used in future reports only alongside its item responses, its stated data sources, and the parent's rebuttal — the order adopts the discipline this scenario argues for, and says expressly that the discipline's application to a scored assessment summary rests on the court's own fact-finding and on § 6351(f)'s evidence practice, **because Rule 1340's application to a scored assessment summary is untested, and the order says so rather than pretend otherwise**. The court finds the engagement excerpts accurate but materially incomplete, declines the increased-supervision recommendation the excerpts were carrying, and credits the verified progress data. The phase-two flag is ordered reassessed on the complete record before any recommendation is built on it. The honest label: the *paper* is won — the assessment still exists, the case continues, and no ending in this scenario erases either.

## 2. The route — graph-verified

1. **Anatomy of an Excerpt** ("Two Sentences of Seven Months") → **"Ask for everything: the whole file, in writing, tonight."** The strategy is set in the first scene: completeness, demanded, or nothing.
2. **The Record** → **"Ask for the agency record in writing... Under § 3130.44(d)..."** Sets `recordsRequested`; the file arrives with the assessment summary — redacted, items withheld — which starts the second fight on documented ground.
3. **The Provider's Letter** → **"Ask. The worst answer is a no you already have by silence."** Sets `providerLetter` — Dr. Sayegh in her own words: opened by saying she would not treat *"at any frequency"* without a safety protocol, and wrote one.
4. **The Measure of Change** → **"Ask for the numbers. If the form counts them, let the court count them too."** Sets `progressData` — 7 of 9 at start, 42 of 45 by November: the record's own arithmetic against its summary's adjectives.
5. **Item by Item** → **"Argue it as untested, and put the argument in the rebuttal so the record shows the care taken."** The Rule 1340 application to a scored assessment is framed in the filing itself as argument, never as settled law.
6. **Item by Item, Answered** → **"File it. An unanswered worksheet is homework; a filed one is evidence."** Sets `rebuttalFiled`.
7. **The Hearing** (dispatcher: `providerLetter` + `rebuttalFiled`) → **"Ask for the excerpts struck as characterization, the letter and worksheet admitted, and the summary used only whole — with the untested flag stated in the order."**

**Programmatically walked path (33 nodes):** start → excerpt_anatomy → backstory124 → sayegh_office → lawyer124 → nasser_whiteboard → records124 → intake_score → phase_two → file_arrives → visit_sep12 → visit_center_logs → boateng_call → sayegh_letter → data_pull → employer_letter → assessment_fight → redaction_fight → school_counselor → conference124 → fivemoreminutes → agency_position → visit_room_oct → rowan_day → gal124 → sayegh_prep → packet124 → mother_statement → rowan_question → continuance_choice → night_before124 → hearing_day → end_whole_page. **Ending cash: $119 of $140 left.** *(The son is Callum throughout the text; one node id — `rowan_day` — retains his pre-rename first name.)*

## 3. Why this wins — the law

- **A parent sees the whole record, not the agency's edition of it.** Under 55 Pa. Code § 3130.44(d), a client — or the client's attorney — may review and obtain copies of information in the agency record, and § 3130.44(f) requires the agency to explain withheld material as contrary to the client's best interests and permits an appeal of a refusal (as worded in prior batches). The summary's redactions survived exactly as long as the mother's unanswered questions; the *configuration sheet* — data sources, design office, per-item rubric ownership — was producible the moment it was demanded item by item.
- **Rule 1340, stated with its flag on.** Pa.R.J.C.P. 1340(A) and (E) require that an assessment report filed with the court address the Rule 1340(A) items — including (A)(11), the assessment tool, if any, used in the evaluation — and that the report be provided to the parties, with (F) giving the parent the right to challenge the form, content, and terms. Prior batches argued Rule 1340's application to a *scored assessment summary* is **UNTESTED**, because the verified law does not say whether the summary is a Rule 1340(E) "report." This scenario keeps the flag on in the filing, in the order, and in this guide: the win is built so it does not need the untested proposition — it rests on evidentiary completeness, which no one had to invent.
- **Summaries are evidence, and evidence can be answered.** A court report's characterizations are tested the way exhibits are tested: source documents (the provider's full letter), the underlying data (session counts, visit logs), and the opposing party's filed rebuttal. § 6351(f) hearings run on the child's health and education record, the permanency plan, and the parties' evidence — the whole page is simply what an exhibit looks like before anyone is allowed to quote half of it.
- **The assessment is described, never characterized.** Consistent with every prior batch: the guide calls the instrument a scored assessment summary with a one-page summary, item responses, and a configuration sheet. It is never called AI, machine learning, predictive, or an algorithm, because no verified source establishes what built it — only what it contains and how it was used.

## 4. The traps

- **Split Findings (partial)**: the provider testifies and the worksheet is filed, but the redactions were never fought — the court believes Heather and cannot verify the "whole page" claim, so the flag discussion is postponed to a reassessment the summary's owners schedule. Believed, and still half-papered.
- **Believed, and Waiting (partial)**: the letter and the data land, but no rebuttal worksheet is ever filed; the court credits her testimony and continues the matter for the agency to "review its summary practices." Credibility without filings produces continuances, not orders.
- **The Excerpts Stand**: fighting on character ("I have done everything") against an exhibit leaves the two sentences intact as the record's account of her own therapist — and the supervision recommendation they were carrying is adopted on their strength.

## 5. What no strategy controls

What the assessment's items actually measure, and whether its rubric would score her the same way scored whole — completeness disciplines the *use* of a summary; it does not validate the instrument, and no order in this scenario pretends to. Whether other counties' reports excerpt the same way; whether the phase-two reassessment, on a complete record, reaches a kinder flag; Dr. Sayegh's continued availability; Callum's school year; and the underlying case, which continues past December on its own facts. The strategy controls the record's completeness and the honesty of its labels. It cannot control the instrument's design, and this guide does not pretend otherwise.
