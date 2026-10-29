# SOURCES AND ALTERATIONS — Batch D (Complex Scenarios 22–28)

*How "The First 90 Days" Complex scenarios 22–28 were built from the published public record, what was drawn from each source, what was changed, and which legal propositions were newly verified before use. Consolidated from the four production fragments (sources-D-a/b/c/d.md) at batch validation; the fragments remain in this folder as the writers' working records.*

**Status:** Draft documentation, for internal development and attorney review. Nothing here or in the scenarios is published or sent.

**Source rule applied:** Every scenario derives only from published Pennsylvania Superior Court and Commonwealth Court opinions in dependency, termination-of-parental-rights, and CPSL expunction matters, and from official statutory text where a proposition is stated as law. No private case, file, docket, or person from the development team's own orbit was used as source material, in any form.

**Alteration doctrine applied:** Each scenario is a composite. The procedural spine and testimony-textured beats come from the published sources; names, ages, counties, occupations, and identifying facts are changed, and beats from at least two published sources are merged in every scenario, so that no real family maps onto any character.

**Batch law result:** No new law was verified or added anywhere in Batch D. Every proposition stated as law in Scenarios 22–28 comes from the project's shared verified set. Each fragment below records its own withholdings — propositions seen in the sources that were deliberately NOT used.

**Batch validation (independent, run at consolidation over the on-disk files):** all seven JSONs parse; node counts 34/37/36/34/36/35/42 (spec 32–45); 4 endings each (ending:true, no choices, board-mapping debriefs); every choice target resolves; BFS from each startNode reaches every node; dayOffsets non-decreasing on every edge; `recordsRequested` set in all seven; `removed` set only where a removal occurs inside the story (23, 25, 28) and absent where placement predates play (22, 24, 26, 27); scripts match their JSONs node-for-node in exact order; every full calendar date appearing in any node carries the correct weekday; and the batch's stated deadlines were recomputed independently — S22 ASFA point = placement Feb 4, 2025 + 15 months = Monday, May 4, 2026 (offset 454); S23 shelter care = birth Jan 12, 2026 + 3 days = Thursday, January 15, 2026; S25 shelter care = removal Feb 10, 2026 + 3 = Friday, February 13, 2026, and its § 6341(a)(2) date = notice + 90 days = May 30, 2026; S26 ASFA point = Oct 6, 2025 + 15 months = January 6, 2027 (offset 457); S27 ASFA point = Jan 5, 2026 + 15 months = April 5, 2027 (offset 455); S28's same-week collision (education meeting Tuesday, March 10, 2026; court review Thursday, March 12, 2026) verified against the real calendar. Strategy guides strategy-22…28.md each name a real ending from their data and carry a programmatic path check reported by their writers and spot-confirmed at consolidation (guide-named endings verified present in the JSONs).

---

# SOURCES FRAGMENT D-a — Scenarios 22 and 23

*How Scenarios 22 and 23 of "The First 90 Days" were built from the published public record, what was drawn from each source, what was changed, and what was deliberately withheld. Companion to `sources-and-alterations.md` (Scenarios 2–4), whose source rule and alteration doctrine were applied unchanged.*

**Status:** Draft documentation, for internal development and attorney review. Nothing here or in the scenarios is published or sent.

**Source rule applied:** Published Pennsylvania Superior Court opinions only (read on Justia), plus the previously verified law set. No private case, file, docket, or person from the development team's orbit was used, in any form.

---

## SCENARIO 22 — "Fifteen Months, Twins" (34 nodes, 4 endings)

*Four-year-old twins, placed together, whose readiness splits at the ASFA fifteen-month date: one thriving toward return, one mid-treatment. The exceptions to 42 U.S.C. § 675(5)(E) are analyzed and built child by child.*

### Published sources used

1. **In re R.N.J. & G.J., 2009 PA Super 248 (Pa. Super. Dec. 18, 2009)** — Justia full text read: https://law.Justia.com/cases/pennsylvania/superior-court/2009/s66014-09.html
   - *Beats/textures drawn:* The controlling texture for the whole scenario — a trial court giving siblings in the same case **different permanency outcomes** after "extensive testimony regarding each child's unique emotional needs," and the appellate court affirming that child-by-child analysis against the mother's argument that differing sibling goals were themselves error; the permanency-hearing frame in which whether a child "has been placed into foster care for fifteen out of the last twenty-two months" is determined on the record (42 Pa.C.S. § 6351(f)(9) discussion, ¶4 n.4); the clear-and-convincing burden framing for any later termination hearing.
2. **In the Interest of H.J., 2019 PA Super 68 (Pa. Super. Mar. 5, 2019)** — Justia full text read: https://law.justia.com/cases/pennsylvania/superior-court/2019/1382-mda-2018.html
   - *Beats/textures drawn:* The split-readiness engine — two siblings at "diametrically opposed" places, one "ready to live in a community setting," the other not, with different goals (adoption vs. subsidized permanent legal custody) entered for each; the court's reasoning that one child's permanency should not be put "on hold for the sake of" the sibling; expert/treatment testimony as the record on which the split rested. Our scenario converts the goal-split into a return/continued-treatment split at the filing decision (it ends at filing/deferral/return, and depicts no termination outcome).
3. **In the Interest of J.L.L., No. 1714 EDA 2023 (Pa. Super. Apr. 26, 2024)** — Justia full text read: https://law.justia.com/cases/pennsylvania/superior-court/2024/1714-eda-2023-0.html
   - *Beats/textures drawn:* The case-plan objective set (parenting, substance-abuse treatment, employment proven by pay stubs, housing); a compliance arc that was "initially substantial or complete" and later fell — deliberately inverted here (the composite mother's arc rises) so the ASFA exceptions, not parental failure, carry the drama; visits generally kept but often late — the visit-log texture behind the cancellation/make-up beat; kinship placement texture.
4. **In re Adoption of L.A.B. & A.L.B., No. 1143 MDA 2023 (Pa. Super. Jan. 24, 2024)** — Justia full text read: https://law.justia.com/cases/pennsylvania/superior-court/2024/1143-mda-2023.html
   - *Beats/textures drawn:* Twin-specific texture only: twins with developmental diagnoses receiving speech, behavioral, and physical therapy in a structured program; the testimony that such children "need a lot of consistency" and a daily routine — the factual feel behind Milo's continuity-of-treatment record. (The case is a private custody/termination dispute, not a dependency case; nothing of its posture, parties, or outcome is used.)

### Alterations applied
Names (Maya, Milo, Rosa, Mrs. Adeyemi, Priya), ages (twins aged to 4), county, occupations, the mother's history, the housing facts, and all dialogue are invented. The sources involve older siblings, multi-year placements, residential treatment, and (in R.N.J.) actual terminations; the composite compresses to one placement, a rising compliance arc, two service referrals, and the filing *decision* only. The split ending follows R.N.J./H.J.'s documented principle — each child assessed individually, siblings lawfully ending a review with different placements and clocks — and is written as a dated, reviewable placement outcome, never as a termination or a prediction.

### Dates audited
Placement Tuesday, February 4, 2025 (day 0). Play opens day 392. The fifteen-month date — placement + 15 calendar months, computed in the generator — is **Monday, May 4, 2026** (dayOffset 454), and all four review nodes sit exactly on it. All kickers and stated dates machine-checked against the real calendar.

### New law verified
**None.** Every proposition of law stated is from the shared verified set: ASFA 15 of the most recent 22 months and its three exceptions (42 U.S.C. § 675(5)(E)); records released on request (55 Pa. Code § 3130.44(d)); clear-and-convincing burden for termination grounds (stated generically, at the filing stage only).

### Deliberate withholdings
- No § 2511 grounds analysis and no termination outcome is depicted or predicted for either twin; the scenario ends at filing, deferral, trial return, or split placement.
- No day-count is stated for any post-filing hearing ("months away" only).
- The scored assessment form, Rule 1340, and all AI/ML framing: not used in this scenario.
- Reasonable efforts as an element of termination: not used (see the withholding recorded for Scenario 3).

---

## SCENARIO 23 — "The Hospital Hold" (37 nodes, 4 endings)

*A newborn is not discharged to her mother after a substance-exposure concern at birth, while her five-year-old sister is safe at their grandmother's. Three interleaved tracks: hospital, agency (including whether the baby's case reaches the sibling), and court.*

### Published sources used

1. **In the Interest of S.G., No. 2967 EDA 2022 (Pa. Super. Nov. 7, 2023)** — Justia full text read: https://law.Justia.com/cases/pennsylvania/superior-court/2023/2967-eda-2022.html
   - *Beats/textures drawn:* The hospital spine — a report arising from the birth itself, the baby remaining in the hospital, an Order of Protective Custody obtained days after the birth (Oct. 17, 2022) and a shelter care hearing two days later (Oct. 19, 2022), with the child remaining in agency custody; workers seeing the mother in the hospital the day after the birth; a parent's undocumented claim (a screen taken but confirmation never provided) weighing against him — the direct texture of the scenario's "attended but undocumented" beats; parents present with court-appointed counsel at the later hearing.
2. **In the Interest of L.B., 2017 PA Super 411 (Pa. Super. Dec. 27, 2017)** — Justia full text read: https://law.justia.com/cases/pennsylvania/superior-court/2017/884-mda-2017.html
   - *Beats/textures drawn:* A newborn who remained in the hospital for an extended monitored period (nineteen days) after birth; an Application for Emergency Protective Custody and, three days later (Feb. 7 → Feb. 10, 2017), the expressly-labeled "72 hour Shelter Care Hearing" continuing custody with the agency — the procedural rhythm the scenario's court track mirrors (custody day 0, hearing day 3). **Its legal holding (prenatal conduct and the CPSL abuse definition) is deliberately NOT used** — see withholdings.
3. **In the Interest of S.R.S., No. 1070 WDA 2022 (Pa. Super. Mar. 17, 2023)** — Justia full text read: https://law.justia.com/cases/pennsylvania/superior-court/2023/1070-wda-2022.html
   - *Beats/textures drawn:* The sibling-reach texture — a referral at a newborn's birth (NICU admission after exposure) that led, within days, to emergency custody of the newborn's **older siblings as well** and their placement together; the speed with which a birth-day case can become a whole-family case; treatment intake and assessment in the first days (evaluation completed the day after the birth referral, inpatient recommendation). Our composite inverts the sibling outcome on the strong paths (the older child is *not* drawn in) precisely so the player can see the fork this case took the other way.

### Alterations applied
Names (Wren, June, Rosa, Ms. Park, Mr. Osei, Ms. Ferreira), county, occupations, and all dialogue are invented. The sources involve contested adjudications, additional parents, prior agency history, and (in S.R.S.) eventual terminations after eighteen months; the composite has one mother, no prior case, a grandmother whose home is undisputedly safe, and ends inside the first three weeks. The medicine is kept to the single plain sentence the task required; no substances, test results, dosages, or withdrawal detail from any source opinion appears in the scenario. Hospital procedure is written generically and cited to nothing.

### Dates audited
Birth and (on the court track) custody: **Monday, January 12, 2026** (day 0). The `removed` flag is set only on the two `first_paper` choices that produce the day-zero custody order. Shelter care hearing: day 3, **Thursday, January 15, 2026** — exactly 72 hours after the removal, computed in the generator and stated in the lawyer, hearing, and court-track debrief texts. On the plan track no custody is taken and no hearing occurs, and the debriefs say so expressly. Court review nodes sit on Monday, January 26, 2026 (day 14). All kickers machine-checked.

### New law verified
**None.** Every proposition of law stated is from the shared verified set: shelter care hearing within 72 hours (42 Pa.C.S. § 6332; 23 Pa.C.S. § 6315(d)); right to counsel / appointed counsel (42 Pa.C.S. § 6337); records released on request (55 Pa. Code § 3130.44(d)).

### Deliberate withholdings
- **The L.B. holding** — whether prenatal conduct can constitute child abuse under 23 Pa.C.S. § 6303(b.1) — is not stated, argued, or hinted as law anywhere in the scenario, although L.B. is a fact-texture source; the scenario's agency action is framed procedurally (report, investigation, custody, hearing), never as an abuse finding.
- **23 Pa.C.S. § 6386** (health-care-provider reporting for infants under one year), although quoted inside L.B.'s text as read, is not cited in the scenario: the hospital's report is depicted generically ("as it does in cases like this") with no citation, per the task's hospital-procedure rule.
- No substance is named; no test, result, or symptom is described beyond the single plain monitored-care sentence.
- No day-counts are stated for adjudication, disposition, or any later review; the sibling-services track is depicted as administrative practice texture, with no legal entitlement or deadline claimed for it.

---

*Compiled for the Tactic Watch development files. Draft — not legal advice, not a depiction of any real case. Companion files: `scenario-22.json` / `scenario-22-script.md` / `strategy-22.md`, `scenario-23.json` / `scenario-23-script.md` / `strategy-23.md`.*

---

# Sources Fragment D-b — Scenarios 24 & 25 ("The First 90 Days")

*Public record only. Every scenario below is a fictional composite built from published opinions; names, ages, counties, occupations, injuries, and identifying facts were changed. Nothing here draws on any private case, person, or file.*

---

## Scenario 24 — "The Appeal Record"

### Sources actually read

1. **In Re: A.S., Appeal of: J.S.**, Superior Court of Pennsylvania, 2019 (No. 1048 MDA 2018).
   URL: https://law.justia.com/cases/pennsylvania/superior-court/2019/1048-mda-2018.html
   Beats drawn: (a) a discovery order that was **not in the certified record** — included only in the reproduced record — was treated as non-existent, and the deficiency could not be cured by the appendix ("any document which is not part of the official certified record is considered to be non-existent"); (b) failure to timely raise non-compliance below resulted in **waiver** ("Failure to timely object to a basic and fundamental error … will result in waiver of that issue. On appeal, the Superior Court will not consider a claim which was not called to the trial court's attention at a time when any error committed could have been corrected."); (c) the texture of an appeal fought entirely over what the paper record does and does not contain.
2. **In the Interest of: L.R.M., Appeal of: M.M.**, Superior Court of Pennsylvania, 2026 (No. 2305 EDA 2025).
   URL: https://law.Justia.com/cases/pennsylvania/superior-court/2026/2305-eda-2025.html
   Beats drawn: (a) an issue (lack of written notice of an aggravated-circumstances finding) held **waived** because "neither Mother nor her counsel objected" at the hearing; (b) the appellate court **confirming preservation by reading the transcript** ("Our review of the transcript confirms neither Mother nor her counsel objected…"); (c) the principle stated in the opinion that issues not raised in the trial court are waived and cannot be raised for the first time on appeal.
3. **In Re: N.C. et al.**, Superior Court of Pennsylvania, 2006 (2006 PA Super 285).
   URL: https://law.justia.com/cases/pennsylvania/superior-court/2006/s41021-06.html
   Beats drawn: permanency/goal proceedings continuing on their own track while an appeal is pending; the ASFA-era permanency framework running underneath the appeal; the focus of dependency proceedings on the child, child by child.

### Alterations
Composite mother "Mara Ellison" and son "Eli" (age 8) are invented; the underlying published matters involved different parties, postures (a termination decree in *A.S.*; an aggravated-circumstances dispute in *L.R.M.*; a goal-change appeal in *N.C.*), counties, and facts. The playable core — a scored assessment summary admitted at adjudication, an exhibit folder offered or held, a testify/rest decision — is a constructed teaching device assembled from the *mechanics* those opinions describe (certified record, objection, waiver), not a retelling of any one case. No language from any real child or parent is reproduced.

### New law verified
**None.** No new statute or rule is cited in the scenario text beyond the shared verified set (42 Pa.C.S. § 6332; 23 Pa.C.S. § 6315(d); 42 Pa.C.S. § 6337; 55 Pa. Code § 3130.44(d); 42 U.S.C. § 675(5)(E); clear-and-convincing burden for TPR grounds, referenced generically in debriefs).

### Withholdings (documented, deliberate)
- **Appellate law is stated generically and citation-free, by design:** "appellate courts review the record made below; unpreserved issues are generally not reached; the child's case continues meanwhile." The opinions above quote Pa.R.A.P. 302(a) ("Issues not raised in the trial court are waived and cannot be raised for the first time on appeal"), but the rule's text was not independently verified from a primary source (official rule text) in this pass, so **no rule citation appears in the scenario**. The proposition is carried by published-opinion texture and stated only in general terms.
- **No appeal deadlines or day counts are stated anywhere.** No filing window, briefing schedule, or decision timeline is given a number; the appellate clock is shown through offsets, calendar offers, and the collision with the (verified) ASFA 15-of-22-months date, which is computed from the fictional placement date.
- The scored assessment form is called exactly that — never AI/ML/predictive scoring. Pa.R.J.C.P. 1340 was not used in this scenario, so no disclosure proposition about it is stated.

---

## Scenario 25 — "The Expert Split"

### Sources actually read

1. **In the Interest of: M.M.-A., a Minor**, Superior Court of Pennsylvania, 2017 (No. 928 MDA 2017).
   URL: https://law.justia.com/cases/pennsylvania/superior-court/2017/928-mda-2017.html
   Beats drawn: (a) an infant's fractures discovered incidentally at a medical visit, with parents who had no explanation; (b) **four experts split** — one child-abuse pediatrician attributing the injuries to abuse, three others attributing them to clinical/bone-fragility causes (rickets, bone fragility, a possible genetic collagen disorder); (c) the trial court weighing the **parents' regular pediatric care** (and that the treating physician, a mandated reporter, never reported) as part of the totality; (d) a **split result**: dependency adjudicated, but the requested child-abuse finding declined because the agency's abuse proof did not meet **clear and convincing** evidence; (e) the appellate court refusing to reweigh conflicting expert testimony credited by the trial court.
2. **In the Interest of: La.-Ra. W. and Ly.-Ro. W.**, Superior Court of Pennsylvania, 2021 (2021 PA Super 227; Nos. 354 & 359 EDA 2021).
   URL: https://cases.justia.com/pennsylvania/superior-court/2021-354-eda-2021.pdf?ts=1637608920
   Beats drawn: (a) the presenting texture — a parent noticing **swelling and fussiness during ordinary care (diaper changes)** and bringing the baby in; (b) parents who **consistently denied any fall, drop, or accident**, leaving the injury unexplained; (c) a **follow-up skeletal survey** finding additional healing fractures not seen (or only subtly seen) on the first survey — the source of this scenario's "complete imaging set, including follow-up views" hinge; (d) dueling qualified experts (the hospital's child-abuse attending vs. defense experts on bone health and radiology), with bone-health and genetic testing run and weighed; (e) dependency and abuse findings affirmed on the credited expert's testimony — this scenario's adverse-ending texture.
3. Supporting texture (search-result summaries read, opinions not opened in full): *Matter of J.P.* (Pa. Super. 1990) — caregivers offering **inconsistent accounts** of how fractures occurred, undermining credibility — the source of the "inconsistent accounts" chart phrase and the timeline-building beat. Not relied on for any stated proposition of law.

### Alterations
Composite mother "June Park," father "Theo," and daughter "Wren" (7 months, single arm fracture) are invented. The published matters involved rib fractures (dozens, in *M.M.-A.*) and femur fractures/subdural hematoma in infant twins (*La.-Ra. W.*), Lackawanna and Philadelphia Counties, and different family structures and outcomes; this scenario uses one child, one fracture, a daycare-worker parent (to make the indicated-report employment stakes concrete), invented grandparents/grandparent-care window, and a fictional third-opinion specialist. Medical content is kept at the general level the opinions themselves use ("more force than ordinary handling," "bone fragility," labs and follow-up imaging) — no diagnostic specifics beyond that are stated, and no real person's medical facts are reproduced.

### New law verified
**None.** All cited propositions come from the shared verified set: shelter care hearing within 72 hours (42 Pa.C.S. § 6332; 23 Pa.C.S. § 6315(d)); right to counsel/appointed counsel (42 Pa.C.S. § 6337); records released on request (55 Pa. Code § 3130.44(d)); indicated-report appeal within 90 days (23 Pa.C.S. § 6341(a)(2)); agency burden by substantial evidence at the expunction hearing (23 Pa.C.S. § 6341(c.2)(5)); appellant's right to the investigation evidence (23 Pa.C.S. § 6341(c.2)(4)); clear-and-convincing burden at dependency adjudication. The 90-day deadline in the scenario is computed in the generator from the fictional notice date (notice + 90 days); the 72-hour shelter-care deadline is computed from the fictional removal date (+3 days).

### Withholdings (documented, deliberate)
- **§ 6341(c.3)'s 45-day decision window and § 6341(g)'s reconsideration/Court clocks are not stated.** The split ending shows the expunction decision arriving after the dependency decision, without attaching a day-count rule to it.
- **No prima-facie/presumption proposition is stated.** The published dependency opinions discuss an evidentiary presumption tied to injuries that would not ordinarily occur absent a caregiver's act or omission; that proposition is outside the verified set and was not independently verified from primary text in this pass, so the scenario dramatizes only its pressure (an unexplained injury, a burden the agency must carry with evidence) and never states the presumption as law.
- **No Frye / novel-science proposition is stated**, although both lead opinions discuss expert-admissibility fights; admissibility doctrine was left out rather than paraphrased from secondary discussion.
- The assessment concept is not used in this scenario; where a form appears it is paperwork, never "AI/ML/predictive scoring."

---

## Validation note (both scenarios)
Generators `/tmp/gen24.py` and `/tmp/gen25.py` emit JSON + script from a single data source per scenario; kickers and every date stated in body/note/debrief text are computed with Python `datetime` from `startDateISO` + `dayOffset` (Scenario 24's ASFA date via a months-addition on the fictional placement date; Scenario 25's 90-day and 72-hour dates via day addition). Validator confirmed for each: JSON parses; node count in 32–45; 4 endings with `ending: true`, no choices, debriefs present; all `next` targets resolve; BFS reaches every node; `dayOffset` non-decreasing on every edge; `recordsRequested` is set; stated deadlines recomputed and matched. Strategy-guide route walks were run programmatically against the emitted JSON (see strategy-24.md / strategy-25.md companion verification, reported with this fragment).

---

# SOURCES FRAGMENT D-c — Scenarios 26–27

*How "The First 90 Days" Scenarios 26–27 were built from the published public record, what was drawn from each source, what was changed, and what was withheld. Draft documentation for internal development and attorney review. Nothing here or in the scenarios is published or sent.*

**Source rule applied:** Published Pennsylvania Superior Court opinions only (full texts read on Justia), plus the previously verified statutory set. No private case, file, docket, or person from the development team's own orbit was used, in any form.

**Alteration doctrine:** Each scenario is a composite merging beats/textures from at least two published sources. Names, ages, counties, occupations, family structures, and identifying facts are changed throughout; all dialogue is invented.

**Engine-flag note:** `recordsRequested` is set in both scenarios (Scenario 26: twice, by the father; Scenario 27: twice, by the mother). `removed` is deliberately **absent** from both — in Scenario 26 the children's placement predates the playable story (the father learns of it by mail at week six), and in Scenario 27 the child's placement likewise precedes the playable opening by a week. Setting it would falsely imply an in-story removal.

---

## SCENARIO 26 — "The Incarcerated Father" (36 nodes, 4 endings)

*Playable story opens at week six: a father in a state correctional facility learns by mail of his two children's dependency case. Parallel tracks: his paper track, the mother's at-home plan track, his sentence timeline, and the ASFA 15/22 clock (placement Monday, October 6, 2025; 15-month point Wednesday, January 6, 2027, dayOffset 457, computed programmatically).*

### Published sources used

1. **In Re: T.L.H., Jr., No. 1474 MDA 2024 (Pa. Super. May 13, 2025)** — Justia full text read: https://law.justia.com/cases/pennsylvania/superior-court/2025/1474-mda-2024.html
   - *Beats/textures drawn:* Agency letters to an incarcerated father over more than a year; dependency orders noting on their face that, due to his incarceration, the father "has not had access to services," with services and visitation framed to begin "upon Father's release"; the father testifying he never received a dependency order and writing to the court himself; counsel who communicated with him only twice; a parenting class requested but unavailable (he testified he was not classified as a parent in the prison's computer system, so staff could not enroll him); a psychological evaluation requested on an inmate request form and answered in writing that the system does "not provide psych evaluations for this purpose"; video contact that existed only as a by-product of the mother's supervised visits and ended when her track changed; cards sent to the child (a monster-truck card) and an inmate call log as the paper proof of contact; the agency advising the father, when the child had been in care over fifteen months, that it was required to petition. This case is the scenario's spine — its father is the inverse image of ours in one respect (the Superior Court *reversed* the termination there) and the scenario borrows its procedural texture, not its outcome.
2. **In Re: C.L.C., Jr., No. 1725 MDA 2024 (Pa. Super. June 10, 2025)** — Justia full text read: https://law.justia.com/cases/pennsylvania/superior-court/2025/1725-mda-2024.html
   - *Beats/textures drawn:* The counter-texture: a father initially engaged in services and supervised visits whose participation "decreased and eventually ceased"; only one video visit held during incarceration; the father present by video (Teams) for day one of a hearing and absent for day two; a file that ends up describing a father in summaries ("barely communicated") — the source of the scenario's thin-record ending and its warning that the file's adjectives are built from documented acts and omissions, in both directions.
3. **In Re: T.R.C., No. 947 WDA 2017 (Pa. Super. Jan. 5, 2018)** — Justia full text read: https://law.justia.com/cases/pennsylvania/superior-court/2018/947-wda-2017.html
   - *Beats/textures drawn:* A father identified late whom the agency effectively kept out of the dependency proceedings and to whom it provided few services (one video visit, one in-person visit, per the line of the case recounted there); the trial court's rebuke of the agency's treatment of him; and — used only as a *withholding discipline*, see below — the Pennsylvania Supreme Court's reversal of the proposition that an agency's reasonable efforts are an element of the termination grounds.

### Alterations applied
The composite father (Marcus) has two children (Eli, 8; June, 5) — T.L.H. and C.L.C. each involve one child, T.R.C. one daughter. The mother is alive, in recovery, and working her own parallel plan (in T.L.H. the mother consented to adoption; in T.R.C. the mother died). The facility, county, counsel ("Ms. Hart"), caseworker dialogue, program names, and all letters' wording are invented; the unavailable-evaluations and not-classified-as-a-parent beats are re-costumed from T.L.H.'s testimony into generic facility-window exchanges. No sentence length, charge, or parole fact from any source is used; the father's release is described only as a timeline past the children's clock, with no parole law stated. No termination hearing is depicted and no § 2511 ground is analyzed — the scenario ends at the filing/exception decision and, in one ending, at a noted record for a future, generically described request.

### New law verified this round
**None.** The scenario states only law from the shared verified set: shelter care hearing within 72 hours (42 Pa.C.S. § 6332; 23 Pa.C.S. § 6315(d)); right to counsel / appointed counsel (42 Pa.C.S. § 6337); records released on request (55 Pa. Code § 3130.44(d), "shall be released upon request"); ASFA 15 of the most recent 22 months and its three exceptions (42 U.S.C. § 675(5)(E)); clear-and-convincing burden for termination grounds generally.

### Withholdings
- **Reasonable efforts as an element of termination grounds — deliberately NOT asserted.** That Superior Court line was rejected by the PA Supreme Court (as recounted in T.R.C.). The services point appears in this scenario *only* inside the § 675(5)(E) filing exception for services the plan identified as necessary but that were not provided, exactly as the shared contract requires.
- **No parole, transfer, classification, or prison-program law.** Mail delay, legal calls, video hearings, waiting lists, and transfers are texture only, uncited.
- **No § 2511 grounds analysis and no predicted TPR outcome.** Every ending stops at filing / documented exception / preserved record.
- **Post-case mechanics kept generic.** The release-approach ending describes the built record as "the foundation a future request stands on" and states no modification standard, form, or timeline.

---

## SCENARIO 27 — "The Long Way Home" (35 nodes, 4 endings)

*Parent's chosen placement is her sister, an aunt in another state: willing, known to the child, local checks clear — while the interstate placement process crawls. Parallel clocks: the child's ASFA 15/22 clock (placement Monday, January 5, 2026; 15-month point Monday, April 5, 2027, dayOffset 455, computed programmatically), the aunt's approvals expiring/renewing, and the parent's own plan progress.*

### Published sources used

1. **In the Interest of: E.M.P., No. 3401 EDA 2019 (Pa. Super. Apr. 21, 2020)** — Justia full text read: https://law.justia.com/cases/pennsylvania/superior-court/2020/3401-eda-2019.html
   - *Beats/textures drawn:* A maternal aunt in another state (Colorado, there) identified as a permanent kinship resource through the interstate process, who traveled for weekend visits with the child; the interstate process still **not finalized** at the permanency/goal-change hearing many months in; and the appellate court's observation that even if an interstate transfer "is derailed for some unforeseen reason," the family court retains discretion over the goal — the texture of a placement that is perpetually "anticipated."
2. **In the Interest of: E.P., No. 1171 WDA 2018 (Pa. Super. Feb. 28, 2019)** — Justia full text read: https://law.justia.com/cases/pennsylvania/superior-court/2019/1171-wda-2018.html
   - *Beats/textures drawn:* A relative in Tennessee pursued as a placement resource; caseworker testimony that she contacted the other state's office in August 2017 and "submitted all the required paperwork," then learned in mid-September that the other state would not complete the home study (a level-of-care determination), with a private provider to be pursued instead; the Superior Court's conclusion that the stall "was not CYF's, or the relative's, fault" — the scenario's central texture: a delay belonging to process, not to any family or worker. (The source's underlying abuse facts are not used in any form; only its interstate home-study mechanics are drawn.)
3. **In the Matter of: R.E.-C.E., No. 921 MDA 2024 (Pa. Super. Dec. 5, 2024)** — Justia full text read: https://law.justia.com/cases/pennsylvania/superior-court/2024/921-mda-2024.html
   - *Beats/textures drawn:* Two kinship resources in Delaware approved through the interstate process (on or about February 12, 2024) whom the agency nevertheless did not recommend, citing the child's stability with a foster family and the limited relationship — approval arriving yet not deciding; and, in the same opinion, the receiving state's letter closing an interstate home-study request because "we have not been able to begin the home study process… we are closing this request for this home study" — the documentary source of the scenario's placement-closure/drift ending: a file closed for non-engagement while everyone believed it was in motion.

### Alterations applied
The composite merges E.M.P.'s out-of-state aunt, E.P.'s home-study stall across two state systems, and R.E.-C.E.'s approved-but-unacted-on resources and its closure letter. Child renamed and re-aged (Milo, 6, one child rather than E.P.'s several or E.M.P.'s toddler); aunt renamed (Carla), her state left unnamed in-game (the sources name Colorado, Tennessee, Delaware, and Maryland); the parent is the mother, whose own plan (treatment, parenting, housing) is an amplification of E.M.P.'s reunification track; the "logged as sent, never received" gap, the finished study sitting in a review queue, the expiring-clearance renewals, and the Sunday-call/video-call logs are composite constructions from the sources' recurring pattern of requests sent, re-requested, and closed — not any single case's facts. All dialogue is invented.

### New law verified this round
**None.** The scenario states only law from the shared verified set: records released on request (55 Pa. Code § 3130.44(d)); ASFA 15 of the most recent 22 months and its exceptions (42 U.S.C. § 675(5)(E)), with the relative-placement exception as the scenario's shield; clear-and-convincing burden for termination grounds generally.

### Withholdings
- **No interstate compact rules are named, and no interstate law is cited, in the game text.** Per the added interstate discipline: the compact is never named in the scenario; mechanics are kept generic (two states' agencies exchanging forms, a home study requested and re-requested, acknowledgments of receipt, queues), **no timelines are invented** for the interstate process (all "how long it takes" beats are framed as unknowns or as this fictional case's elapsed story time, never as a rule), and no approval validity period is stated — renewals are depicted generically as windows closing, with no day or month count claimed.
- **No claim that the relative-placement exception applies before placement.** The exception ending is written carefully: the documented record of continuous relative-placement pursuit is what the agency documents as its reason to defer filing *while placement completes*; the before-the-clock ending is the one where the child is actually placed with the relative.
- **No § 2511 grounds analysis, no goal-change law, and no prediction of any hearing's outcome.**

---

*Compiled for Scenarios 26–27 (fragment D-c). Draft — not legal advice, not a depiction of any real case. Companion files: `scenario-26.json` / `scenario-26-script.md`, `scenario-27.json` / `scenario-27-script.md`, `strategy-26.md`, `strategy-27.md`.*

---

# SOURCES FRAGMENT D-d — Scenario 28, “The Education File”

*How Scenario 28 was built from the published public record, what was drawn from each source, what was changed, and which legal propositions were newly verified before use (none). Companion to `scenario-28.json` / `scenario-28-script.md` and `strategy-28.md`.*

**Status:** Draft documentation, for internal development and attorney review. Nothing here or in the scenario is published or sent.

**Source rule applied:** The scenario derives only from published Pennsylvania Superior Court opinions in dependency / termination-of-parental-rights matters, used for fact texture (how education, evaluations, and school progress appear in testimony and findings). No private case, file, docket, or person from the development team's own orbit was used as source material, in any form.

**Education-law discipline applied:** All education law in the scenario is **generic and uncited** — evaluations, meetings, plans, and school records are described only as process (“the school has its own evaluation process, its own meetings, its own letters”), with no statute names, no regulation cites, and no day-counts or deadlines for the school track. Dependency-side law stays entirely within the shared verified set. The agency-side assessment is described only as a “scored assessment form.”

**Engine-flag note:** The `removed` flag **is** set in this scenario, because the removal occurs inside the story (day 1, with the shelter care hearing on day 3, inside the verified 72-hour window). The `recordsRequested` flag does double duty by design: it is set by the mother's written agency-records request and again by her signed school-records releases — the playable theme is who holds which paper. The best endings (`end_aligned`, `end_reunified`) are gated on the `binderBuilt` flag's edge: a validator check confirms both are unreachable if that edge is removed from the graph.

---

## SCENARIO 28 — “The Education File” (42 nodes, 4 endings)

*A mother whose 8-year-old is placed across town watches him change schools on an address, then discovers his education file lives in five places and is complete in none of them. Parallel tracks: the dependency review clock and the quiet federal 15-of-22 count; the school's own evaluation process, running in weeks and months; and the school-year calendar, ending in June. The hinge is a single reconciled binder, carried into both rooms.*

### Published sources used

1. **In the Interest of K.B., Appeal of T.D., No. 1974 EDA 2025 (Pa. Super. Mar. 13, 2026)** — Justia full text read: https://law.Justia.com/cases/pennsylvania/superior-court/2026/1974-eda-2025.html
   - *Beats/textures drawn:* A permanency review at which it “was further recommended that K.B. be evaluated to see if he was eligible for an individualized education program (IEP)” — an evaluation recommendation entering the record through review testimony rather than through the school file itself; school behaviors (aggression, bus incidents) noted at one review and subsided by a later one; grades and vocabulary improvement recited at the termination hearing as needs-and-welfare evidence. Source of the scenario's texture that school progress reaches court as testimony about a file, long after the school produced it.
2. **In re Adoption of A.J.L.G., No. 7 MDA 2018 (Pa. Super. May 25, 2018)** — Justia full text read: https://law.justia.com/cases/pennsylvania/superior-court/2018/7-mda-2018.html
   - *Beats/textures drawn:* The teacher's testimony that “neither Mother nor Father were involved in the updating of the child's IEP in February 2017,” contrasted with foster parents who “attend every conference that is scheduled” and are “in constant communication” with the teacher; the child's instructional-support classroom placement and speech services in and out of school; grade-level progress (kindergarten/beginning-first-grade level rising to mid-first-grade reading) testified to as compliance/permanency evidence. Source of the scenario's sign-in-sheet and “who was in the room” beats — inverted: in the composite, the mother was never sent the invitation.
3. **In re D.R.S., No. 2581 EDA 2023 (Pa. Super. Aug. 28, 2024)** — Justia full text read: https://law.Justia.com/cases/pennsylvania/superior-court/2024/2581-eda-2023.html
   - *Beats/textures drawn:* The single record sentence — “Older Children all have an individualized education plan (‘IEP’). The school invited Mother to attend IEP meetings, and Mother failed to attend.” — as an example of how an invitation history hardens into a finding; a dedicated agency truancy caseworker among the witnesses. The composite keeps the mechanism (the file records invitation-and-absence, not the reason) and reverses the cause: the invitation went to a foster home and a vacated apartment.
4. **In re Adoption of L.B.M., No. 1834 MDA 2015 (Pa. Super. May 31, 2016)** — Justia full text read: https://law.justia.com/cases/pennsylvania/superior-court/2016/1834-mda-2015.html
   - *Beats/textures drawn:* A placement-modification analysis weighing “the educational and health needs of the boys” against a move — a child who “likes his current school,” a younger child's “significant strides in his speech” through weekly therapy in the current placement — and denying the move partly to avoid “again upsetting such stability.” Source of the scenario's premise that placement decisions are made on beds and addresses while their educational consequences arrive afterward, and of the second-school-change ending's cost accounting.

### Alterations applied
All four sources are termination endgames in which the courts found sustained parental non-compliance over many months or years, with school non-involvement as one strand of that record. The composite inverts the parental posture entirely: the mother is engaged, working, and progressing on every plan goal, and the education gap is produced by addressing, mailing, and filing mechanics — an evaluation that doesn't follow the child, an invitation sent to two wrong addresses, an intake assessment that rated education needs “low” because a plan was nominally “in place.” Child renamed and re-aged (Sam, 8, third grade); mother unnamed (second person); foster parent, caseworker, and counsel invented (Mrs. Lindqvist, Ms. Tran, Ms. Okafor); schools invented (Lincoln, Hillside, Riverbend Elementary); no county is named; mother's occupations (bakery shift, office cleaning) and the supervision-coverage reason for removal are invented. Beats from all four sources are merged, so no real family maps onto any character.

### Dates audited
Story opens Monday, September 8, 2025 (day 0). Removal Tuesday, September 9 (day 1); shelter care hearing Thursday, September 11 (day 3) — inside the verified 72-hour window, which runs to Friday, September 12. The “same week” collision node is dated Friday, March 13, 2026 (day 186), and its interpolated meeting/review dates — Tuesday, March 10 (day 183) and Thursday, March 12, 2026 (day 185) — were machine-verified as real Tuesdays/Thursdays. Endings land Monday, June 8 and Monday, June 15, 2026. The federal 15-of-22 point (December 2026) falls outside the story by design; debriefs state Sam's position as “roughly nine/ten of fifteen” months, as narrative approximation, and no exception is invoked as an outcome. **No school-track date, deadline, or day-count is stated anywhere in the scenario**; school timing is described only in weeks and months, and the June endpoint is framed as the calendar's, not a statute's.

### New law verified
**None.** No new legal proposition was verified or used in this scenario. Every proposition stated as law comes from the previously verified set: shelter care within 72 hours (42 Pa.C.S. § 6332; 23 Pa.C.S. § 6315(d)); counsel for a parent (42 Pa.C.S. § 6337); agency records on request (55 Pa. Code § 3130.44(d)); the ASFA 15-of-22 filing rule and its three exceptions (42 U.S.C. § 675(5)(E)); and the clear-and-convincing burden, referenced only as the standard any future petition would have to meet. The § 6341 expunction provisions and Rule 1340(B)(1) are not used — they do not belong to this fact pattern.

### Deliberately not used (researched or available, and withheld)
- **All education-law specifics.** Research surfaced advocacy materials describing school-stability rights, educational decision makers, enrollment and records-transfer timelines (including a “10 business days” transfer claim in a secondary publication). None of it was verified from primary text in this round, and per the scenario's discipline none of it appears: no statute or program names, no transfer windows, no evaluation timelines, no decision-maker doctrine. The school track is process and paper only.
- **Termination grounds and outcomes.** The sources are termination cases; the scenario states no § 2511 ground, files no petition, and predicts no termination outcome. The story ends inside the dependency case, at trial return, stability, split, or reset.
- **An invoked ASFA exception.** The three exceptions are stated once, as the verified rule's text, in the lawyer's map. The in-story clock never reaches 15 of 22 months, so no ending turns on an exception being granted.
- **Any characterization of the scored assessment form** beyond its existence as an intake form with a rating and a note. No methodology, vendor, or predictive claim is made or implied.

### Access notes
Full texts were read on Justia for all four sources. No paywalled source (Westlaw/Lexis) was needed or used. Every legal proposition in the scenario is in the previously verified set, as recorded above.
