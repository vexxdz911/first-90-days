# STRATEGY GUIDE — Scenario 29: "The Teen Who Says No"

*Game documentation for a fictional simulation ("The First 90 Days," Tactic Watch). This guide describes choices inside this scenario only. It is general information about how the scenario is built — not legal advice for any real case.*

*Route verified programmatically against `scenario-29.json`: the walk below was scripted from the start node, following each listed choice, and reaches the named ending (see "Path check" at the end).*

---

## (1) The win

**Ending — She Stabilizes, and the Case Turns Toward Home**

Stated honestly: this is a strong ending, not a total one. In this scenario the teen stabilizes in the new placement (sessions she helped redesign, kin time with her aunt written in), the plan is adjusted to the teenager who actually exists, and the case goal remains return home with the case moving toward closure with the mother. It is not an instant reunification, and the scenario does not call it one. The case is still open at the final debrief; what was won is the direction, a fair record, and a plan the mother can actually perform.

## (2) The route

Key decision points, in order, using the scenario's node titles:

1. **What the Notebook Holds** — Choose: *"Ask, in writing, that Kayla's own words be quoted in the summary."*
   Changes: sets FLAG `teenQuoted`; the file gains the hidden item "Mother's written request — teen's words to be quoted, not summarized." The refusal acquires its real owner — the teen — and the fair-record and stabilization endings stay open. The summary path stays playable but starts the case with the refusal filed under the mother's name.

2. **Your Own File** — Choose: *"Write the request this week — the full record, including the scored assessment."*
   Changes: sets FLAG `recordsRequested`; hidden item records the request for the full record and scored assessment (form, item ratings, outcome). This is the scenario's highest-leverage move: it is what makes the later "Scored Form" and "Reading the Grid Beside the Truth" scenes possible.

3. **After She Leaves** (following **The Session She Walks Out Of**) — Choose: *"Write the outreach log tonight — calls, texts, the ride offered, times."*
   Changes: sets FLAG `outreachLog`; cash −15; hidden item records the dated outreach log. The teen's leaving and the mother's reaching now both exist in the record, so the walkout cannot be summarized as the mother's failure alone.

4. **The Morning After, on Paper** — Choose: *"Send the written account this week — her quoted words, Rosa's account, your call times."*
   Changes: sets FLAG `nightDocumented`; hidden item records the whole overnight account. The night the teen chose where to sleep becomes a fair paragraph instead of the one line "mother aware."

5. **Rebuilding the Record** — Choose: *"Do the rebuilding — introductions, packet to the new worker, statement drafted with your lawyer."*
   Changes: sets FLAGS `rebuiltRecord` and `writtenStatement`; hidden item records the written statement to the court (mother's actions, teen's quoted words, request for an adjusted plan). After the placement change resets the practical work, this is what stops the old summaries from becoming the new file.

6. **Before the Final Review** — Choose: *"Bring the full packet — logs, quotes, statements, the fair file."*
   Changes: routes to **The Final Review, Full File** instead of **The Final Review, Thin File**. This is the fork that closes the blame and drift endings and keeps the two record-based endings open.

7. **The Final Review, Full File** — Choose: *"Ask the court to adjust the plan to the teenager who exists — shorter sessions she helped design, kin time with Rosa written in, and a path home."*
   Changes: reaches the win ending above. (The other choice at this node reaches the partial win, "Ending — Her Refusals, Fairly Recorded; the Plan Adjusted.")

Supporting moves on the same route that are not forks but matter to the fiction of the file: staying for the full session after the teen leaves (**The Session She Walks Out Of**), sending the teen's quoted condition — "Maybe. If they let me talk first." — to the lawyer the same evening (**Kayla's Question**, sets `teenQuoted` again), and the cash costs of showing up (bus fare at **The Review Is Coming**, −12; rebuilding travel at **A New Address**, −20).

**Full verified route:** A Plan With Two Names on It → The Review Is Coming → Kayla, in Her Own Voice → What the Notebook Holds → Quoted, Not Summarized → Your Own File → Six Quiet Days → Visitation, in a Waiting Room → The Scored Form → Reading the Grid Beside the Truth → The Session She Walks Out Of → After She Leaves → The Log → Where She Sleeps Tonight → The Morning After, on Paper → A Fair Paragraph → Kayla's Question → The First Review → A New Address → Rebuilding the Record → The New File Opens Fairly → Twenty Minutes at a Time → Before the Final Review → The Final Review, Full File → **Ending — She Stabilizes, and the Case Turns Toward Home**

## (3) Why this wins — the law as it is supposed to work

The route operationalizes only principles from the scenario's verified legal set:

- **Counsel.** The parent is entitled to counsel, and to appointed counsel if she cannot afford it (42 Pa.C.S. § 6337). Every strategic move in the route arrives through, or is checked with, the lawyer — that is the right working as designed.
- **The record on request.** The case record "shall be released upon request" (55 Pa. Code § 3130.44(d)), and the route asks for the full scored assessment by name — the form, the item ratings, the outcome — not just the narrative summaries. Seeing the grid is what lets the parent reattach actions to the people who actually did them.
- **Disclosure, with its limit stated.** Assessment/discovery disclosure in the adjudication phase is addressed by Pa.R.J.C.P. 1340(B)(1). The scenario states in-game, wherever this rule is invoked about the assessment, that Rule 1340's application to the Universal Assessment is untested. The route never rests a move on the untested proposition; it rests on the regulation that can be quoted.
- **The burden.** Dependency and termination decisions are governed by a clear-and-convincing-evidence burden. A fair, sourced, quoted record is the kind of record that burden is meant to be weighed on — it lets the court separate the mother's actions from the teen's, instead of weighing a summary that merges them.
- **The teen's words as record.** No special rule is claimed for quoting the teen. The route's point is procedural and ordinary: a written request, a written statement to the court, and a dated outreach log are all ways a party puts facts into a file that hearings are decided from.

## (4) The traps

1. **"Let the summary stand" at What the Notebook Holds.** Tempting because the teen *was* heard in the room. Cost: the room is not the record. Her refusal enters the file under the mother's name ("mother to ensure youth attends"), and every later reader inherits that grammar. The stabilization path can still be reached in the graph, but the fiction of the file — and the debrief's account of it — is worse from this point on.
2. **Skipping the record request at Your Own File.** Tempting because the review feels far away and paper feels like a second fight. Cost: the parent never sees the scored form whose items rate the teen's actions under the family's name, and cannot correct its grammar line by line. The scenario's highest-leverage move is the one most easily postponed.
3. **"Let tonight go" after the walkout, and "let the report line stand" after the overnight.** Both are framed in-game as trust and rest, and both are understandable. Cost: unlogged outreach reads as no outreach; the overnight becomes the single line "mother aware." These two quiet evenings are what the thin-file final review is made of.
4. **"Bring what you have and speak from memory" at Before the Final Review.** Tempting because memory is true and speaking is sincere. Cost: it routes to **The Final Review, Thin File**, closing the stabilization and fair-record endings and opening only **Ending — The Record Blames the Mother** and **Ending — Toward the Horizon, With a True Record**. Judges weigh what is in front of them; memory, in the scenario's repeated phrase, is what the system reads last.

## (5) What no strategy controls

The teen's twenty minutes in the redesigned session were the teen's. No parental paperwork can make a fifteen-year-old stay in a room, choose a placement, or speak at a review — and this scenario is built so that it cannot be won by controlling her. A different worker's summary habits, a placement that disrupts a second time, a judge who reads the same fair file with a different hand, a bad week landing on the review week: in this scenario as in real cases, outcomes turn on workers, judges, placements, teenagers, and luck. The route controls only what a parent can control — what is quoted, what is logged, what is filed, and showing up anyway. The debriefs say so, and so does this guide.

---

**Path check (programmatic):** route node sequence above walked from `start` in `scenario-29.json` → ending reached: **Ending — She Stabilizes, and the Case Turns Toward Home** (`end_stabilize`). ✔
