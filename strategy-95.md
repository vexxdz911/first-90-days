# Strategy Guide — Scenario 95: "Earning the Last Order"

*Game documentation for a fictional simulation in "The First 90 Days" (Tactic Watch). The family, the case, and every choice below are fictional. This guide is general information about how the scenario is built — it is not legal advice for any real case.*

## (1) The win

**Best ending: "Closed: The Last Order."**

This one is a **full** win, and the guide says so without the usual qualifier: Cyril is home, supervision is discharged, and the dependency case is **closed** — the determinations made on the record, the aftercare plan adopted as the family's own document, the file archived. It is the only full win in this batch, and the scenario earns it the hard way: the closure was available only to a record so complete that the court's caution had nothing left to stand on — including the winter's worst twenty minutes, which are in the packet, documented by the mother, in front of the police report that confirms them.

## (2) The route

Verified by walking the scenario graph from the start node (see the verification note at the end). Key decision points, in order:

1. **Reading the Trial-Home File** — *Read it all and mark the two places the notes are wrong.* Cash −10. Sets **recordsRequested** (55 Pa. Code § 3130.44(d)). Closure cases are audited before they are argued; the file's trial-home notes are the evidence for discharge, and two of them are wrong.
2. **What the File Says About the Trial Home** — *File a written correction with the clinic letter and your sister's statement attached.* Sets **fileCorrected**. Errors answered by documents, adjacent to the errors, before April instead of during it.
3. **Two Sessions Left** — *Trade the shifts, attend both, and pay for the certificate.* Cash −15. Sets **sessionsDone** — one of the two flags the winning hearing choice requires. "Complete," not "substantially complete."
4. **The Unsigned Aftercare Plan** — *Chase the signatures: yours, the counselor's, the school's.* Sets **aftercareSigned** — the second required flag. Unsigned, the plan is a brochure; signed, it is the infrastructure the court can close a case onto.
5. The supporting record, in order: the night rotation documented in writing (**scheduleDocumented**), the landlord's signed line (**landlordNote**), the school's stability letter (**schoolLetter**), the home log kept flatly through the step-down (**homeLog**), and a pharmacy receipt (cash −8) that stands in for the winter's hundred proofs of the ordinary.
6. **The Loud Week** — *Write the account tonight and send it to the worker in writing tomorrow, with the officer's card copied.* Sets **incidentDocumented**. The scenario's hinge (see §3): a police-attended doorstep incident, survivable exactly once — as a documented event the parent reported first.
7. **The Worker's Call** — her concordant note confirmed in writing (**workerConfirmed**).
8. **Assembling the Last Packet** — in the statute's order, incident included, at its own tab (cash −7; **packetBuilt**). You finish with $110 of the $150 start.
9. **The Last Hearing** — *Ask the court to discharge Cyril from supervision and close the case, on the aftercare plan as written.* Flag-gated on **sessionsDone** + **aftercareSigned**. The full ask, made because the record supports it — contrast trap 2.

## (3) Why this wins — the law as it is supposed to work

Only principles from the scenario's verified set are stated here:

- **The posture is 42 Pa.C.S. § 6351(a)(1)** — the child permitted to remain with the parent under conditions and supervision — reaching its natural end at a permanency hearing: the court makes the § 6351(f) determinations (safety; whether supervision remains necessary; (f)(2) compliance; (f)(3) progress) and chooses the outcome under § 6351(f.1), on hearings recurring within six months (§ 6351(e)(3)(i)). Discharge and closure are what the menu's reunification outcome looks like when nothing remains for supervision to do; the scenario frames the final order in those terms and no stronger.
- **The engine is 55 Pa. Code § 3130.44(d):** the complete record, read in February, corrected in writing in February, so that April's hearing is a reading instead of an investigation. Both of the file's errors were small, innocent, and — uncorrected — exactly the size of a judge's hesitation.
- **The aftercare plan is practice, not statute,** and the scenario labels it so: a document agencies prepare so that closure leaves a family equipped. Its legal weight in the fiction is the weight a court gives a signed plan while making a necessity determination — presented, argued, and no more.
- **The loud week's lesson is about sequence, not doctrine:** in a supervision case, the court's confidence that the record is complete *is* the closure asset. A documented disturbance, self-reported in writing before the police report arrived, strengthened that confidence. The same twenty minutes, discovered, destroyed it (trap 3).

## (4) The traps

1. **Asking the provider to waive the last two sessions,** or bringing the workbook instead of the certificate. No **sessionsDone** — the closure choice closes. Effort is not completion, and completion is the determination.
2. **Asking, at the hearing, for six more months of supervision "to be safe."** Ends at "Continued: Six More Months of Almost" — a full record spent on a smaller request, granted exactly as asked. Together with Scenario 91's middle ending, this is the game's repeated proof that courts rarely upgrade asks.
3. **Saying nothing about the loud week.** Available only when the incident went undocumented (the choice is closed to players who documented it — documentation forecloses the mistake), and it ends at "Revoked: The Week That Wasn't Written": the incident narrated by the agency from the police report, the trial home's basis shaken, Cyril back at his aunt's. The difference between this ending and the full win is one page, written in twenty minutes, in March.
4. **Leaving the aftercare plan to be finalized after the hearing.** Judges notice sequences: a plan that postdates the decision it was meant to support cannot support it.

## (5) What no strategy controls

The ex's arrival at the door — the scenario is explicit that the incident itself was uncontrollable and is not the parent's failure; the neighbor's phone call; the judge's temperament at the margin. The route controlled the list, the signatures, the corrections, and the sequence of the writing. The guide's closing honesty is the scenario's own: outcomes turn on the controllable and the uncontrollable together — and this winter, for once, the controllable was sufficient. The game does not promise that is typical. It promises it is possible, and shows the paperwork.

---
*Verification: this route was walked programmatically against `scenario-95.json` — each named choice was followed from the start node in order; every intermediate node and choice exists; the flag-gated hearing choice's requirements (sessionsDone, aftercareSigned) were satisfied by flags set earlier on the walk, and the revocation choice was confirmed closed on this route (incidentDocumented set); the walk terminates at the ending node titled "Closed: The Last Order" after visiting 30 nodes, with $110 of the $150 starting cash remaining.*
