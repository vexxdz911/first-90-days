# SOURCES AND ALTERATIONS — Scenarios 2–4

*How "The First 90 Days" Scenarios 2–4 were built from the published public record, what was drawn from each source, what was changed, and which legal propositions were newly verified before use.*

**Status:** Draft documentation, for internal development and attorney review. Nothing here or in the scenarios is published or sent.

**Source rule applied:** Every scenario derives only from published Pennsylvania Superior Court and Commonwealth Court opinions in dependency, termination-of-parental-rights, and CPSL expunction matters, and from the official statutory text. No private case, file, docket, or person from the development team's own orbit was used as source material, in any form. Where a search result surfaced a private matter, it was not opened.

**Alteration doctrine applied:** Each scenario is a composite. The procedural spine and testimony-textured beats come from the published sources; names, ages, counties, occupations, substances, and identifying facts are changed, and beats from at least two published sources are merged in every scenario, so that no real family maps onto any character.

**Engine-flag note (all three scenarios):** The `removed` flag is deliberately **absent** from Scenarios 2–4, because no removal occurs inside any of these stories — Scenario 2 is a CPSL registry track with no dependency removal; Scenario 3's placement predates the playable story (it opens at month 13); Scenario 4's child was placed three weeks before the story opens. Setting `removed` would fire the engine's 72-hour shelter-care banner falsely. The `recordsRequested` flag is set in all three: in Scenarios 2 and 3 by the parent herself; in Scenario 4 by the child's mother — a party to the case — signing the request at the grandmother's asking, because the regulation's right belongs to the case's subjects, not to a placement applicant.

---

## SCENARIO 2 — "The Indicated Letter" (24 nodes, 3 endings)

*The CPSL track: a preschool aide and mother receives an indicated report after her toddler's playground injury produces two medical opinions pointing in different directions.*

### Published sources used

1. **J.S. v. Commonwealth, Department of Public Welfare (Pa. Cmwlth. 1989)** (companion to K.S. v. DPW, 564 A.2d 561) — Studicata summary: https://www.studicata.com/summaries/commonwealth-court-of-pennsylvania/j-s-v-com-department-of-public-welfare-1989-sa7k6d/
   - *Beats/textures drawn:* An injury (bruising) documented medically; the contest between the caretaker's characterization and the medical evidence; a caseworker's contemporaneous observations carried into the hearing record years of procedure later.
2. **K. & L.N. v. Commonwealth (Pa. Cmwlth. 1989)** — Studicata summary: https://www.studicata.com/summaries/commonwealth-court-of-pennsylvania/k-l-n-v-commonwealth-1989-sa4awo/
   - *Beats/textures drawn:* Parents' claim that injuries resulted from an accidental fall; medical testimony that the injuries could not have resulted as claimed; the parents' inconsistent accounts treated as a significant factor. Our scenario inverts the outcome possibilities but keeps the texture: an explanation that shifts in wording becomes load-bearing.
3. **Lackawanna County Children & Youth Services v. Department of Public Welfare (Pa. Cmwlth. 2012)** — Studicata summary: https://www.studicata.com/summaries/commonwealth-court-of-pennsylvania/lackawanna-county-children-youth-servs-v-department-of-public-welfare-2012-swk0hs/
   - *Beats/textures drawn:* Expungement affirmed where the agency's proof failed; the ALJ's exclusion of a substitute witness's testimony because of pre-hearing witness-disclosure requirements — the direct source of the scenario's exhibit-exchange beat ("evidence the other side has never seen can be kept out"); credibility as the hearing's real currency.
4. **F.R. v. Department of Public Welfare (Pa. Cmwlth. 2010)** — FindLaw full text: https://caselaw.findlaw.com/court/pa-commonwealth-court/1537028.html
   - *Beats/textures drawn:* The burden statement — "The Department has the burden of proof in expungement cases and must show by substantial evidence that the indicated report of child abuse is accurate" (citing S.T. v. DPW, 962 A.2d 679, 682 (Pa. Cmwlth. 2008)); the Bureau as ultimate fact-finder with credibility authority.
5. **K.C. v. Department of Public Welfare, No. 1548 C.D. 2011 (Pa. Cmwlth. 2012)** — Justia full text: https://law.Justia.com/cases/pennsylvania/commonwealth-court/2012/1548-c-d-2011.html
   - *Beats/textures drawn:* Findings of fact each tied to record evidence; the perpetrator-by-omission analysis quoting K.S. — used only as texture for how hearings are assembled from paper, not for its facts.
6. **P.H. v. Department of Public Welfare, No. 47 C.D. 2012 (Pa. Cmwlth. 2012)** — Justia: https://law.justia.com/cases/pennsylvania/commonwealth-court/2012/47-c-d-2012.html
   - *Beats/textures drawn:* A mother's appeal from an indicated report of physical abuse; the procedural spine (indicated report → appeal → Bureau hearing), and the statutory warning that a registry entry "may adversely affect that person's ability to obtain employment in a childcare facility or program or a public or private school" (citing 23 Pa.C.S. § 6338) — the texture of the game's letter and its job consequences.
7. **Mulholland v. Government of Berks County (3d Cir. 2013)** — FindLaw: https://caselaw.findlaw.com/court/us-3rd-circuit/1621266.html
   - *Beats/textures drawn:* The footnote recording that the caseworker, testifying years later, had no recollection of the investigation and testified solely from the CY-48 form; also its verbatim quotation of the CPSL definitions of founded/indicated/unfounded reports. Source of the hearing beat: "I don't have an independent memory of the interview. My note says…"
8. **G.V. v. Department of Public Welfare (Pa. 2014)** — official opinion PDF, pacourts.us (J-81-2013; the URL as published contains spaces): `https://www.pacourts.us/assets/opinions/Supreme/out/J-81-2013mo - 1017920122180751.pdf`
   - *Beats/textures drawn:* The notification that the perpetrator's "ability to obtain employment in a child-care facility or program or a public or private school may be adversely affected" by the registry entry (23 Pa.C.S. § 6338(a)); the framing that the burden rests on the county agency under §§ 6303 and 6341.

### Alterations applied
The subjects of the sources are parents and caretakers in sexual-abuse, corporal-punishment, and failure-to-protect matters; none of those fact patterns is used. The composite subject is a preschool aide whose **own** toddler is injured in a playground fall — a fact pattern assembled from the "competing explanation + divided medical reading" mechanics of sources 1–2, with the employment stakes of sources 6 and 8. Child renamed and re-aged (Theo, 3); professions, county, facility, playground, and all dialogue invented; the two-doctor structure is drawn from the opinions' recurring pattern of conflicting medical testimony, not from any single case's doctors.

### Dates audited
Notice received Monday, April 6, 2026 (day 0). The § 6341(a)(2) deadline — notice + 90 days — is **Sunday, July 5, 2026**, computed programmatically and stated in-game in the `read_letter` node and the `end_quiet` debrief. Hearing June 19, 2026; decision July 25, 2026 — 36 days after the hearing concluded, inside the 45-day decision window verified below.

---

## SCENARIO 3 — "Fifteen Months" (25 nodes, 4 endings)

*The long game: a mother in recovery housing has completed every service goal except housing when the ASFA 15-of-22 filing point arrives; the playable strategy is building the record toward one of the statute's three exceptions.*

### Published sources used

1. **In the Interest of J.L.L., No. 1714 EDA 2023 (Pa. Super. Apr. 26, 2024)** — Justia full text read: https://law.Justia.com/cases/pennsylvania/superior-court/2024/1714-eda-2023-0.html
   - *Beats/textures drawn:* The case-plan objective set (parenting classes, substance-abuse treatment, employment, housing); compliance "initially substantial or complete… minimal by the Fall of 2021" — the source of the game's progress-rating vocabulary; employment proven by pay stubs; visits "generally appeared for" but "often late" — the visit-log texture; and a mother who originally *asked* the system for help with housing and treatment.
2. **In re Adoption of N.R.A., No. 915 WDA 2025 (Pa. Super. 2026)** — Justia: https://law.Justia.com/cases/pennsylvania/superior-court/2026/915-wda-2025.html
   - *Beats/textures drawn:* A mother testifying she was **on a waitlist for housing** and could return to her job; a compliance rating that never rose above "minimal"; nearly two years in the system. Our scenario deliberately inverts the rating arc (rising, not flat) to isolate housing as the sole barrier — the waitlist texture and the rating scale are this case's.
3. **In re T.J.J.M. (Pa. Super. 2018)** — Studicata summary: https://www.studicata.com/summaries/superior-court-of-pennsylvania/in-re-t-j-j-m-2018-snsx7h/
   - *Beats/textures drawn:* Testimony texture only — a parent willing to engage who was offered **one Saturday visit, canceled because of the foster family's unavailability and never rescheduled**; services not fitted to his work schedule. This is the direct source of the scenario's cancellation/no-make-up beats and its services-gap theme. **Not used as law:** the broader reasonable-efforts holding associated with this line of cases (see "Deliberately not used," below).
4. **In re Adoption of A.P.C.-D., No. 1432 MDA 2025 (Pa. Super. 2026)** — Justia: https://law.Justia.com/cases/pennsylvania/superior-court/2026/1432-mda-2025.html
   - *Beats/textures drawn:* An appellate court parsing which findings the certified record actually supported (notably on parent–agency communication) — the discipline behind the scenario's repeated lesson that the court can only act on what is in the record.
5. **In re A.L.K. (Pa. Super. 2016)** — Justia: https://law.Justia.com/cases/pennsylvania/superior-court/2016/1050-wda-2016.html
   - *Beats/textures drawn:* The counterweight voice of the child's timeline ("a child's life cannot be held in abeyance"), present in the scenario's lawyer framing and debriefs so the exceptions are taught honestly, against the child's own clock.
6. **In re T.D., 949 A.2d 910 (Pa. Super. 2008)** — Justia: https://law.Justia.com/cases/pennsylvania/superior-court/2008/s14014-08.html
   - *Beats/textures drawn:* The permanency-review framework in which "whether the child has been placed into foster care for 15 out of the last 22 months" is a determination made on the record at review (42 Pa.C.S. § 6351(f)(9) discussion) — the texture of the game's review scenes.

### Alterations applied
The sources involve multi-year cases, multiple children, and (in several) untreated addiction or minimal engagement at the filing point. The composite compresses to one child (Noah, 7), one parent whose compliance arc *rises*, and a single open goal — housing, blocked by a waitlist and a recovery-residence rule — so the ASFA exceptions, not parental failure, carry the drama. All names, employers, programs, towns, and dialogue are invented; the canceled-visit beat is re-costumed from a father's one offered Saturday to a mother's recurring Saturday pattern across a spring.

### Dates audited
Placement Monday, March 3, 2025. Play opens at month 13 (day 396 = Friday, April 3, 2026). The 15-month point is day 457 = **Wednesday, June 3, 2026**, and all four review nodes sit exactly on it. Reunification ending at month 16 (day 490 = Monday, July 6, 2026). All kickers and stated dates machine-checked against the real calendar.

---

## SCENARIO 4 — "The Kinship Door" (23 nodes, 3 endings)

*A grandmother seeks placement of her granddaughter; her own 1998 aggravated-assault conviction produces a one-line denial; the scenario teaches the difference between the agency's approval checklist and the court's placement question, and what a paper trail does inside a discretionary system.*

### Published sources used

1. **In re D.S., 979 A.2d 901 (Pa. Super. 2009)** (2009 PA Super 144) — Justia full text read: https://law.Justia.com/cases/pennsylvania/superior-court/2009/a15034-09.html
   - *Beats/textures drawn:* A disqualification discovered **during the foster-parent qualification investigation** (¶3); children removed from the grandmother's home and weekly unsupervised visits continued (¶4); the trial court's observation that the grandmother **could have pursued administrative remedies and appealed the disqualification pursuant to 55 Pa. Code § 3700.72 — and did not** (¶18); the untimely appeal of the removal order (¶19, citing the 30-day appeal period of Pa.R.A.P. 903(a)); the alternative holding that the disqualifying statute "prohibits the authorization, **without exception**" and "does not provide any time limitation" (¶20); and the separate custody-petition door, deferred rather than denied (¶¶11, 16). This case is the scenario's spine and its cautionary ghost: nearly every path in the game is a road this grandmother did not take in time.
2. **In re J.P. (Pa. Super. 2010)** — FindLaw full text read: https://caselaw.findlaw.com/court/pa-superior-court/1526426.html
   - *Beats/textures drawn:* The grandmother's **nineteen-year-old aggravated-assault conviction, voluntarily disclosed by her** after FBI/State Police clearances initially did not reveal it (¶2 & n.1); her testimony that the conviction "did not relate to a minor child," that she had "paid her debt to society," and that she was seeking its expungement (n.1); DHS and the guardian ad litem *agreeing the child should remain with her* while disputing only payments (¶2); the juvenile court's order of kinship care, affirmed on appeal because 23 Pa.C.S. § 6344 and 55 Pa. Code § 3490.123(d)(2) limit the **agency's** approval authority and "do[] not limit the powers of the trial court to designate such a person as a foster parent if the designation is in the best interests of the child" (¶¶9–10). This case supplies the scenario's court-door texture and its placement endings.
3. **In re K.T.W.E., No. 333 WDA 2020 (Pa. Super. 2020)** — Justia: https://law.Justia.com/cases/pennsylvania/superior-court/2020/333-wda-2020.html
   - *Beats/textures drawn:* The 1:30 a.m. emergency in which the maternal grandmother "could not be a kinship placement at that time" "[b]ased upon a prior criminal history and the emergent nature of the placement," with the agency explaining it would take "further steps to determine if she was eligible for placement during normal business hours"; the paternal aunt's next-morning call asking what steps she could take. Source of the scenario's opening night and its "not tonight ≠ not ever" theme.

### Alterations applied
In D.S. the conviction was the step-grandfather's (12 years old) and the children had already lived with the grandmother for over a year; in J.P. it was the grandmother's own (19 years old) and the child stayed with her throughout. The composite merges them: the conviction is the **grandmother's own**, aged to **28 years** (1998), and the child is placed with strangers first (K.T.W.E.'s posture), so the study, denial, appeal, and court tracks all occur inside the story. The daughter's treatment entry, the granddaughter (Mia, 5 turning 6), the cafeteria career (an amplification of J.P.'s "debt paid" testimony into a working life among children), and all dialogue are invented. The two "placement" endings follow **J.P.'s** posture — a court weighing a full record — and are written as discretion exercised on a record, never as an entitlement; the appeal ending is deliberately written as a *loss* on the approval question that builds the record the court later reads, which is the reverse image of D.S.'s waiver.

### Dates audited
Story opens Monday, September 14, 2026 (child placed Monday, August 24, 2026, three weeks earlier — referenced, never played). All 23 nodes' kickers and stated dates machine-checked; endings land Monday, November 30 and Monday, December 7, 2026. **No day-count is stated anywhere in-game for the approval appeal** — the clinic beat says only that such appeals "run on short clocks." D.S. describes the § 3700.72 route without the game needing its count, and no verified source for a specific count was read in this research, so none is claimed.

---

## NEW LEGAL PROPOSITIONS — VERIFICATION RECORD

Everything below was verified **before** use, from primary text, in this research round. Anything not listed here and not in the previously verified set (72-hour shelter care; counsel; 90-day appeal; ASFA 15/22 + three exceptions; § 3130.44(d) release; Rule 1340(B)(1) with its untested flag; clear-and-convincing burden) does **not** appear in Scenarios 2–4 as law.

1. **Agency's burden at the expunction hearing — 23 Pa.C.S. § 6341(c.2)(5).** Read in the official text of Act of Dec. 18, 2013, P.L. 1201, No. 119, at palegis.us (https://www.palegis.us/statutes/unconsolidated/law-information/view-statute?txtType=PDF&SessYr=2013&ActNum=0119.&SessInd=0): *"(5) The department or county agency shall bear the burden of proving by substantial evidence that the report should remain categorized as an indicated report."* Used in Scenario 2 (clinic, hearing, both merits debriefs), quoted verbatim in the `end_expunged` debrief. Corroborated by F.R. v. DPW (source S2-4) and S.B. v. DPW (Pa. Cmwlth. 2011).
2. **"Substantial evidence" defined — 23 Pa.C.S. § 6303.** Definition as quoted verbatim from the CPSL in B.B. (B.L.) v. DPW (Pa. Cmwlth. 2011) (https://caselaw.findlaw.com/court/pa-commonwealth-court/1563438.html) and Mulholland (S2-7): an indicated report rests on a determination "that substantial evidence of the alleged abuse exists based on any of the following: (1) Available medical evidence. (2) The child protective service investigation. (3) An admission of the acts of abuse by the perpetrator"; and "'[S]ubstantial evidence' is '[e]vidence which outweighs inconsistent evidence and which a reasonable person would accept as adequate to support a conclusion.'" Used in Scenario 2's `end_expunged` debrief (quoted) and paraphrased in the clinic beat.
3. **Appellant's right to the investigation evidence — 23 Pa.C.S. § 6341(c.2)(4).** Same official Act 119 text: *"(4) The department or county agency shall provide a person making an appeal with all evidence gathered during the child abuse investigation that is relevant to the determination, including potentially exculpatory evidence. The evidence shall be provided not later than ten days following the entry of a scheduling order."* Used in Scenario 2 (clinic beat, `packet` node, `end_expunged` debrief).
4. **Decision deadline — 23 Pa.C.S. § 6341(c.3).** Same official text: the ALJ's/hearing officer's decision "shall be entered, filed and served upon the parties within 45 days of the date upon which the proceeding or hearing is concluded," extendable for good cause by no more than 60 days. Used in Scenario 2's chronology (decision on day 36 post-hearing) and cited in the `end_expunged` debrief.
5. **Further review clocks — 23 Pa.C.S. § 6341(g).** Same official text: parties "have 15 calendar days from the mailing date of the final order of the Bureau of Hearings and Appeals to request the secretary to reconsider the decision or appeal to Commonwealth Court," and "30 calendar days from the mailing date of the final order… to perfect an appeal to Commonwealth Court." Used, stated exactly, in Scenario 2's `end_upheld` debrief.
6. **§ 6341(a)(2) re-confirmed.** Already in the verified set; its current text was nonetheless re-read verbatim in the official act print (legis.state.pa.us, https://www.legis.state.pa.us/WU01/LI/LI/US/PDF/2014/0/0045..PDF): "Any person named as a perpetrator… may, within 90 days of being notified of the status of the report, request an administrative review by, or appeal and request a hearing before, the secretary to amend or expunge an indicated report… The request shall be in writing…"

## DELIBERATELY NOT USED (researched and withheld)

- **A specific day-count for a kinship/resource-caregiver approval appeal.** D.S. establishes the route (55 Pa. Code § 3700.72) but the regulation's text and window were not read from a primary source in this round; Scenario 4 therefore states no number.
- **Any statutory "waiver" of a criminal-history bar for kinship approval.** No such mechanism was verified; the game claims only what D.S. and J.P. show — the agency bound by its rule, a court exercising its own placement discretion on a full record. The word "waiver" in the sources file refers to *waiver by inaction* in D.S. (rights lost by missing deadlines), which is how the scenario teaches it.
- **Reasonable efforts as an element of termination grounds.** The Superior Court's D.C.D./T.J.J.M. line was rejected on that point by the Supreme Court (see the discussion in In re T.R.C., No. 947 WDA 2017 (Pa. Super. 2018), recounting the reversal). Scenario 3 accordingly uses **only** the distinct, verified ASFA filing exception for services identified but not provided (42 U.S.C. § 675(5)(E)), and ends at the filing decision — no § 2511 grounds are analyzed, and no TPR outcome is depicted or predicted.
- **45-day appeal windows** appearing in older expunction cases (e.g., S.D. v. DHS (Pa. Cmwlth. 2016), describing pre-amendment procedure). Superseded for this purpose by the verified § 6341(a)(2) 90-day rule; the game uses 90 days only.
- **Retention periods** for indicated reports. Not verified from primary text; Scenario 2's quiet-ending debrief says the entry "remains in the Statewide database" and surfaces on clearances — and nothing more specific.

## ACCESS NOTES

Full texts were read for: In re D.S. (Justia), In re J.P. (FindLaw), In re J.L.L. (Justia), K.C. v. DPW (Justia), F.R. v. DPW (FindLaw), and Act 119 of 2013 (palegis.us official PDF). Studicata pages are editorial summaries, not opinions; they were used for fact texture only (J.S., K. & L.N., Lackawanna County CYS, T.J.J.M.), and every proposition of law drawn near them was independently verified as recorded above. No paywalled source (Westlaw/Lexis) was needed or used. The pacourts.us G.V. PDF link contains spaces as published; its operative passages were cross-checked against the FindLaw mirror. No source was found inaccessible in a way that left a gap in the deliverables: every legal proposition in the three scenarios is either in the previously verified set or in the verification record above.

---

*Compiled under the Agents Orchestrator pattern (Legal Researcher, Narrative Designer, Legal Compliance Checker personas). Draft — not legal advice, not a depiction of any real case. Companion files: `scenario-2.json` / `scenario-2-script.md`, `scenario-3.json` / `scenario-3-script.md`, `scenario-4.json` / `scenario-4-script.md`.*

---

## EXPANSION NOTE — SCENARIOS 37–136 (added 2026-10-29)

One hundred new scenarios were produced in two waves of five batch teams each, under the same doctrine as Version 1: fictional composites only, built from published opinions and documented patterns; no private case in the author's orbit was used as a source; every scenario is winnable to its best outcome, with partial wins labeled partial in the guides; new law entered the game only from primary text read during production and recorded in the batch sources files.

**Batch map.** Wave 1 — Batch F, *The Front Door* (S37–46); Batch G, *Placement & Kinship* (S47–56); Batch H, *Services & Compliance* (S57–66); Batch I, *The Courtroom* (S67–76); Batch J, *Permanency Clocks* (S77–86). Wave 2 — Batch K, *Appeals & Post-Permanency* (S87–96); Batch L, *Special Circumstances* (S97–106); Batch M, *Money, Benefits & Housing* (S107–116); Batch N, *Education & Medical* (S117–126); Batch O, *Capstones* (S127–136). Per-batch sources: `sources-batch-F.md` through `sources-batch-O.md`, alongside the scenarios.

**Totals.** The expansion adds 3,056 scenes and 313 endings (Foundation 20 / Hard 35 / Complex 45 across the 100). The full library now stands at 136 scenarios, 4,104 scenes, 430 endings (Foundation 27 / Hard 48 / Complex 61).

**Final verified-law additions** (beyond the Version 1 set recorded above): kinship notice and definitions — 42 Pa.C.S. § 6336.1 (as amended by Act 48 of 2023) and the "potential kinship care resource" definition at 42 Pa.C.S. § 6302, with the CPSL kinship definitions at 23 Pa.C.S. § 6302 (Batch G; carried in the shared set per Batch L's record); adjudication and disposition — 42 Pa.C.S. § 6341(a), (c), (d) and § 6351(a), (b), (e)(3)(i), (f) (incl. (f)(9) and its exceptions), (f.1) (Batch I); the 30-day appellate window — Pa.R.A.P. 903(a), (b) (Batch K); school stability and surrogate parents — 20 U.S.C. § 6311(g)(1)(E), § 6312(c)(5)(B), 34 C.F.R. § 300.301, § 300.519 (Batch N). Everything else the expansion cites was already in the verified set. Senate Bill 1499 (2025–26) is mentioned once, in Scenario 51's debrief, worded exactly as what it is: introduced and in committee, not law.

**Integration alterations (2026-10-29).** A cross-batch rename pass applied five principal-name renames inside the expansion (S86 Amara→Nyla; S105 Beatrix→Maren and Rosalind→Vivian; S100 Pearl→Iris; S110 Fern→Alma) — full log at `expansion-rename-log.md`. Central validation then found and repaired four flag-gate defects, each fixed at the source (JSON, script, and guide together): Scenario 123's partial ending *The Kind Stranger's Season* was unreachable (its objection beat sat downstream of the location letters it required the player not to have sent; an objection choice was added at the assignment node, where the scenario's own text stages it); and the decision nodes of Scenarios 64, 66, and 113 each had a hole in their flag partitions — a reachable combination of documents with no available choice — closed with one (S64, S66) or two (S113) summation choices in the node's own voice, landing where each scenario's guide already sends a thinner file. No other story logic was altered. Final verification is recorded in `expansion-completion.md`.
