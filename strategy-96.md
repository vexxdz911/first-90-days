# Strategy Guide — Scenario 96: "Thirty Days After the Decree"

*Game documentation for a fictional simulation in "The First 90 Days" (Tactic Watch). The family, the case, and every choice below are fictional. This guide is general information about how the scenario is built — it is not legal advice for any real case.*

## (1) The win

**Best ending: "Vacated: The Decree Falls."**

State it honestly: this is a **partial** win, and it is the largest one appellate law offers in this posture. The Superior Court vacates the termination decree and remands for a new trial: Beatrix is, in law, Alban's mother again tonight, and the adoption petition — premised on the decree — cannot proceed on a vacated foundation. Alban does **not** come home at the end of this ending; a new trial will be held, and it could reach the same destination by a corrected road. What was won is the legality of the asking: a decree that ended a parent-child relationship was built on a report nobody could cross-examine and a finding refuted by the agency's own admitted exhibit, and a court reading a complete, findable record said so.

## (2) The route

Verified by walking the scenario graph from the start node (see the verification note at the end). Key decision points, in order:

1. **The Decree** — *Read the date, then call the lawyer's office.* Sets **dateFirst**. The decree was entered Monday, May 4, 2026; Pa.R.A.P. 903(a) gives thirty days — Wednesday, June 3.
2. **Flashback: The Objection at Trial** — *The objection was made, argued, and ruled on.* Sets **preservedObjection** — the first required flag, earned by trial counsel in a losing minute last month.
3. **Flashback: The Referral That Wasn't** — *The cross was made and the exhibit offered and admitted.* Sets **servicesExhibits**: the agency's own referral log, showing the March referral was drafted and never sent, admitted against the decree's Finding 14.
4. **The Notice, Signed on Day Eight** — *Confirm the filing yourself: call for the receipt on day ten.* Sets **noticeFiled**. The delegation branch exists at this node and is the batch's most expensive alternative (trap 4).
5. **The Second Opinion** — *Order the trial transcripts and request the complete agency file, in writing.* Cash −35. Sets **recordsRequested** (55 Pa. Code § 3130.44(d)). The appeal's two pressure points are record-shaped; the route treats them as a factual question with a checkable answer.
6. **The Other Petition** — *Have Fenwick file the written notice of the pending appeal in the adoption matter.* Sets **notedBelow**. An appeal does not pause the adoption track; knowledge, in writing, is what the parent can put in its file.
7. **The Brief of a Trial** — *Check every citation against the certified binders.* Cash −10. Sets **briefChecked**; two citations corrected.
8. **The Appendix, Audited** and **The Missing Day of Trial** — *File the correction so the log sits where a reader will find it.* Cash −15. Sets **recordComplete** — the second required flag. The referral log was in the certified record all along: misfiled as an attachment to the wrong volume, present and functionally invisible. The $15 lodging correction is the difference between a true sentence in the brief and a findable one.
9. The parallel life, kept documented: the written contact log (**visitLog**), Greta's Sundays and her letter to the IF file (**gretaLetter**), the school note (**ifSectionGrown**), the remand section growing (**remandSection**), groceries at Greta's (cash −12). You finish with $88 of the $160 start.
10. **Argument** — *Lead with the preserved report objection AND the Finding 14 exhibit.* Flag-gated on **preservedObjection** + **recordComplete**. The panel asks the agency the moot's question — "is there a page where this referral is *sent*?" — and the record answers in four seconds, because someone paid $15 to make it findable.

## (3) Why this wins — the law as it is supposed to work

Only principles from the scenario's verified set are stated here:

- **The clock is Pa.R.A.P. 903(a), verified from the official rule text for this batch:** a notice of appeal must be filed within 30 days after the entry of the order. An untimely notice implicates the appellate court's jurisdiction and the appeal is quashed — the rule behind both this scenario's day-ten receipt and its day-thirty-three ending.
- **The burden the decree had to carry is clear and convincing evidence** — in the verified set, and stated at the trial posture generically, as Version 1 stated it: the appeal asks whether the grounds were proved as the law requires and whether termination served the child's needs and welfare, in that order.
- **Everything else appellate here is ground rule, not quoted rule** — deliberately, under the accuracy doctrine: panels review the certified record; issues must be preserved below to be reviewed above; issues preserved but not pressed at argument are not reached; an appeal does not by itself suspend parallel proceedings below. The scenario dramatizes these as the discipline its lawyers practice, the same treatment Version 1 gave appellate mechanics in Scenario 24.
- **The record itself is 55 Pa. Code § 3130.44(d)** — released upon request — plus the trial transcripts, purchased. "RecordComplete" in this scenario means something precise and unglamorous: not more paper, but paper where readers' eyes land.

## (4) The traps

1. **Skimming the flashback objection** because it lost. Cost: no **preservedObjection**, and the report question — the decree's broadest weakness — becomes unreviewable weather. Overruled objections are assets; that is the flashback's whole curriculum.
2. **Passing over the services cross in the flashback.** Finding 14 stands unopposed in the record, and the appeal is reduced to a single pillar that harmless-error review can absorb.
3. **Leaving the misfiled log "technically in the record" at "The Missing Day of Trial."** No **recordComplete**; the winning argument choice closes. What remains is the split route at best — and the split ending ("Split: Half the Decree Falls") is itself the other great trap: **dropping the report objection at argument** as "too technical," which wins Finding 14 and forfeits Finding 9 in a single sentence, the panel noting the abandonment as it goes.
4. **Delegating the filing receipt at "The Notice, Signed on Day Eight."** Ends at "Quashed: Three Days Late": signed day eight, filed day thirty-three, appeal quashed without a reading, the decree final while every substantive thing in the case was strong. The guide states the professional-responsibility aftermath the way the scenario does — it exists, it is fact-specific, and mapping it is beyond this game's honest reach.
5. **Leading at argument with Alban's Sundays and his mother's transformation.** All true; all in the IF tab, which is to say outside the certified record and outside the panel's jurisdiction to reward. Ends at "Affirmed: The Footnote" — the preserved issues footnoted as preserved, and as unpressed.

## (5) What no strategy controls

The panel's weighing through harmless-error lenses; the new trial's outcome, where the agency's remaining evidence is real and Alban's two years of placement are real; the foster family's next steps; a seven-year-old's clock, which runs faster than any court's and does not toll for briefing. The route controlled preservation (earned at trial), timing (verified, not delegated), and the record's completeness and findability. That is the whole of an appellant's power. This scenario's claim is only that it is real power — sufficient, here, to unmake a decree; sufficient nowhere to promise a childhood — and that the smallest item in it, a $15 filing about where a page sits, was the one the outcome finally turned on.

---
*Verification: this route was walked programmatically against `scenario-96.json` — each named choice was followed from the start node in order; every intermediate node and choice exists; the flag-gated argument choice's requirements (preservedObjection, recordComplete) were satisfied by flags set earlier on the walk; the walk terminates at the ending node titled "Vacated: The Decree Falls" after visiting 33 nodes, with $88 of the $160 starting cash remaining.*
