# Strategy Guide — Scenario 89: "What the Panel Can See"

*Game documentation for a fictional simulation in "The First 90 Days" (Tactic Watch). The family, the case, and every choice below are fictional. This guide is general information about how the scenario is built — it is not legal advice for any real case.*

## (1) The win

**Best ending: "Vacated: The Hearing Has to Show Its Work."**

State it honestly: this is a **partial** win. The Superior Court vacates the goal-change order and remands for a new permanency hearing at which the court must make its own determinations on the record. Blythe does **not** come home at the end of this ending, the goal question will be decided again, and it could be decided the same way — on a proper record this time. What was won is that an order changing a child's life was undone because it was made by adopting a report instead of making the findings the statute lists, over a preserved objection, in a record whose exhibits answered the report.

## (2) The route

Verified by walking the scenario graph from the start node (see the verification note at the end). Key decision points, in order:

1. **The Record, Boxed** — *Order the complete transcripts and request the full agency record, in writing.* Cash −30. Sets **recordsRequested**, **transcriptOrdered** (55 Pa. Code § 3130.44(d)).
2. **Flashback: "Let the Record Reflect"** — *The objection was made and ruled on.* Sets **preservedObjection** — the single most important flag in the scenario. Counsel objected to the court adopting the report without making its own § 6351(f) determinations, and the court ruled. A ruling is what a panel reviews.
3. **Flashback: The Folder of Saturdays** — *Offer the folder — every page of it.* Sets **exhibitInRecord**. Together with the objection, this unlocks the vacated ending at argument: the panel must be able to see both the error and the evidence the error ignored.
4. **Choosing the Issues** — *Build the brief on the preserved findings issue and the exhibits.* Sets **issueChosen**. The crossed-out grievances (tone, fairness, the caseworker) stay crossed out — panels have no lever for them.
5. **The Statement of Errors** — *File the statement on time, built only from preserved issues.* Sets **statementFiled**; the appeal's borders are drawn around its strongest ground.
6. **The Missing Findings Page** — *Order the missing page and renew the written request for the complete file.* Cash −15. Sets **recordComplete**. Excerpts would never have revealed the gap.
7. **The Brief, Built From Pages** — *Read the brief line by line against the certified record.* Cash −10. Sets **briefChecked**; two wrong citations get fixed.
8. **The Page That Isn't There** — *Take the page out of the brief and argue from the admitted page one.* Sets **certifiedChecked**. The beloved appendix-only page comes out before it can spend the appeal (see trap 3).
9. Below the appeal: the corrected visit log (**visitLog**), the filed school note (**schoolFiled**), and the written progress summary at the interim review (**reviewRecord**, cash −10). You finish with $95 of the $160 start.
10. **Argument** — *Lead with the preserved findings objection AND the admitted exhibits.* Flag-gated on **preservedObjection** + **exhibitInRecord**. It leads to the vacatur.

## (3) Why this wins — the law as it is supposed to work

Only principles from the scenario's verified set are stated here:

- **A permanency hearing has statutory work to do.** Under 42 Pa.C.S. § 6351(f), the court determines — itself — the matters the subsection lists, including (f)(2) compliance with the plan, (f)(3) progress toward alleviating the original circumstances, (f)(5.1) reasonable efforts to finalize the plan, and (f)(9) the fifteen-of-twenty-two-months filing question with its three exceptions. The outcome then follows under § 6351(f.1). Before a disposition, § 6351(b) likewise requires findings entered on the record. An order that "adopts the report in full" performs none of this visibly — which is the error the appeal exists to correct.
- **The panel reviews the certified record, preserved issues, and rulings.** The objection created the ruling; the exhibits gave the ruling something to bite on; the statement of errors kept both inside the appeal's borders; the appendix discipline kept the brief inside the record. The appeal clock was Pa.R.A.P. 903(a)'s thirty days, and the record itself was assembled under 55 Pa. Code § 3130.44(d).
- **The case below never paused:** reviews continue on § 6351(e)(3)(i)'s rhythm, and the ASFA fifteen-of-twenty-two date (42 U.S.C. § 675(5)(E)) arrives on its own schedule regardless of the appeal — which is why steps below the line are in the winning route at all.

## (4) The traps

1. **Skimming past the objection in the flashback** because it feels like a technicality. Cost: no **preservedObjection** — the vacated ending closes, and the only leads left at argument are the ones that end in affirmance. Technicalities are what appeals are made of.
2. **Holding the folder at "Flashback: The Folder of Saturdays"** because the judge had clearly decided. Cost: no **exhibitInRecord**. The objection survives as an abstraction with nothing for the panel to weigh it against; a findings error about a record the appellant never built is a much harder appeal.
3. **Keeping the appendix page at "The Page That Isn't There"** because it is true. It sets **appendixKept**, which opens the argument choice that rests on the brief as filed — and ends at "Quashed on a Page That Wasn't There." Truth outside the certified record is a defect, not an argument.
4. **Leading with the report's tone at argument.** The panel's question — where in the record was that objected to? — is unanswerable, and the appeal affirmatively spends the credibility the preserved issue needed. Ends at "Affirmed: The Report Stood."

## (5) What no strategy controls

The panel's composition and reading; the trial judge's original haste; the agency's advocacy on remand; the new hearing's outcome, which a correct process does not predetermine. The route controlled preservation, exhibits, citations, and the bottom line's paper. It could not control whether three judges, reading cold, would care as much about the findings list as the statute does. Here, they did. The guide records that as the system's design working — not as a promise about the next panel.

---
*Verification: this route was walked programmatically against `scenario-89.json` — each named choice was followed from the start node in order; every intermediate node and choice exists; the flag-gated argument choice's requirements (preservedObjection, exhibitInRecord) were satisfied by flags set earlier on the walk; the walk terminates at the ending node titled "Vacated: The Hearing Has to Show Its Work" after visiting 22 nodes, with $95 of the $160 starting cash remaining.*
