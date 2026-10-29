# Strategy Guide — Scenario 122: "Excused, Absent, Unexcused"

*The First 90 Days — a fictional composite. Fictional composites only; no real person or case. General information about how these hearings work, not legal advice.*

> **Route verification:** this guide's winning route was graph-walked programmatically through `scenario-122.json` (every step is a legal choice; every `requiresFlags` gate satisfied by flags accumulated earlier on the route; cash never negative). Path and totals are printed at the end.

## 1. The win

**"Ending — Home, on the Narrow Ground"** — the best outcome, labeled honestly.

The March 18 adjudication does not go the agency's way on the allegation the petition led with: the attendance exhibit is admitted **as corrected** — nine unexcused, fourteen excused medical — the truancy ground fails on the agency's own audit, and the court finds the petition proved only on the narrow, true ground (the February lapse in the asthma plan's paperwork), with the indicated report dismissed on the school ground under 42 Pa.C.S. § 6341(c). At the March 25 disposition Oren is **not committed**: under § 6351(a)(1) he remains with Bernadette under court supervision, with a service plan aimed at the real problem set — a workable morning routine, a clinic communication line, one school contact — and a 60-day review. The honest label: this is a *win on the facts with a disposition at home*, not a dismissal of the whole case — the February lapse was real, and the guide does not call the outcome an exoneration. Bernadette's victory is that the case is now sized to the truth: one lapse, addressed, instead of a fabricated pattern.

## 2. The route — graph-verified

1. **The Count** ("Twenty-Three") → **"Take the list home and match it against the clinic calendar. Numbers first, arguments second."** The mother's own count produces the first discrepancy: two days she knows were excused.
2. **The Lawyer** → **"All three. This case is won on the correction or it is not won at all."** The audit, the correction request, and the record, together.
3. **The Attendance Office** → **"Ask for the day-by-day file extract. Your son's whole school record, printed."** Sets `schoolFile` — the extract shows the gray codes clustering after the software migration.
4. **The Correction** → **"Submit it. Fourteen days, fourteen notes, one conclusion: the number is a software artifact."** Sets `codingLetter` — the school's own clerk signs the sentence the hearing needs: *the coding does not reflect the excuses received.*
5. **The Agency Record** → **"Ask for the agency record in writing... Under § 3130.44(d)..."** Sets `recordsRequested` — the petition's drafter copied the portal figure without ever requesting the day-by-day file; *the count was never checked* is now a record fact.
6. **Disposition** (dispatcher: `schoolFile` + `codingLetter`) → **"Ask the court to return Oren home today under (a)(1), with a plan aimed at the February lapse and a 60-day review."**

**Programmatically walked path (31 nodes):** start → petition_read → lucinda_count → lawyer122 → truancy_letter → school_office → oren_voice → clerk_honesty → dube_visit → clinic_visit → neighbor_note → clinic_records → records122 → oren_school_day → agency_note → mother_calendar → agency_conference → correction_ask → keller_second → audit_wait → foster_shadow → school_board → keller_evidence → correction_letter → expert_call → clinic_van → hearing_prep122 → night_before122 → adjudication → disposition_day → end_narrow. **Ending cash: $122 of $140 left.** *(The mother is Bernadette Farrow throughout the text; two early node ids retain her pre-rename first name — `lucinda_count` — for the same reason Scenario 120 keeps `noor_reply`.)*

## 3. Why this wins — the law

- **Adjudication is the Commonwealth's burden, element by element.** Dependency is not a status a court confers because a family looks struggling; the petition's grounds must be proved. A petition whose lead number collapses from 23 to 9 on the proponent's own audit has not merely lost a statistic — it has lost the factual predicate (a pattern of educational neglect) the number was carrying.
- **The CPSL track has its own burden and its own clock.** An indicated report may be amended or expunged when it is determined the report is inaccurate — 42 Pa.C.S. § 6341(a) — and the appeal machinery (§ 6341(c), (d)(1), (d)(2)) is where a parent forces the agency to defend the report's accuracy on the record. Bernadette's hearing does double duty: the corrected register defeats the indicated report's school ground and the petition's lead allegation in the same evidentiary stroke.
- **Disposition follows the proved ground, not the alleged one.** Where a child is found dependent, the court must enter the disposition best suited to the child's safety, protection, and physical, mental, and moral welfare — 42 Pa.C.S. § 6351(a), with remaining in the parent's home under supervision the least restrictive option on the § 6351(a)(1) rung used throughout this game. A petition proved only on a narrow lapse supports a narrow disposition; the correction is what makes "narrow" available.
- **The record request is the spine.** Under 55 Pa. Code § 3130.44(d), the mother or her attorney may obtain the agency record — and the intake note showing the count was lifted from a portal screen, unverified, is the exhibit that converts a data error from an embarrassment into a finding about the petition's reliability.

## 4. The traps

- **Corrected, One Hearing Late (partial)**: the audit exists but the correction letter doesn't, and the correction arrives at disposition instead of adjudication. Oren comes home — with two weeks of foster care, an adjudication on the uncorrected exhibit, and a record that says *twenty-three* in the adjudication order forever. Timing is substance: a corrected number at the wrong hearing is a smaller case, not a true one.
- **The Bargain (partial)**: stipulating to the petition "as a package" to end the stress adjudicates the 23 days as fact. Every future finding — reviews, school meetings, the next petition — inherits the false number as an admitted one.
- **Twenty-Three, Standing**: fighting on temperament ("I am a good mother") instead of on the count leaves the exhibit unchallenged; the court adjudicates on the agency's number and commits, because 23 unexcused days *would* be a pattern — the trap is that they weren't, and only documents could say so.

## 5. What no strategy controls

Whether the school's correction process moves at the speed of the hearing calendar — here it did, by ten days; in another county the audit could strand past adjudication and only the partial would be available. The judge assigned and their patience for data disputes; the clinic's record-keeping in a future February; Oren's asthma itself; and whether Bernadette's employer keeps tolerating clinic-morning absences. The strategy controls the count: whose number, from which documents, corrected by whom, in writing, before the hearing that mattered. It cannot control the asthma, the employer, or the calendar, and this guide does not pretend otherwise.
