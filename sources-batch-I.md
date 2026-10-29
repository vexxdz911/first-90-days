# Sources and Alterations — Batch I: Scenarios 67–76, "The Courtroom"

*Wave 1 expansion, produced 2026-10-29 under the owner's doctrine: scenarios built from "likely or documented situations that could happen and how to win the best possible outcome." Documented = published PA Superior/Commonwealth Court opinions and documented system patterns; likely = composites of recurring documented practice. Every family below is a fictional composite. No real person's identifiable case is used; the private cases in the owner's orbit (Christine May, Annie Roth, Camden Ransing) were excluded as sources in full. Drafts only — nothing sent or published; attorney verification remains the gate before any organizational or parent-facing use, as with all Tactic Watch material.*

## How this batch was sourced

Each scenario's courtroom mechanics were drawn from (a) the statutory text of the Juvenile Act provisions that govern the hearing depicted, read in full from the official consolidated-statute text during this run (see "New law verified" below); (b) published Pennsylvania Superior Court opinions depicting the same hearing postures — adjudication trials where the agency's proof was tested element by element, permanency and goal-change reviews, continuance fights, and expert/bonding testimony — used for TEXTURE (what these rooms are like, what judges weigh, what the record shows on appeal), never for a family's facts; and (c) the verified law set carried over from Version 1, worded as in Version 1. No opinion's family, facts, or outcome is reproduced; every scenario is winnable to its best ending by construction, which the published record — full of affirmances — is not.

Opinions read or drawn on for texture this run (published; cited here as research sources, not in player-facing text): *In re L.Z.*, 91 A.3d 208 (Pa. Super. 2014) (en banc) (adjudication proof and credibility deference); *In re C.Z.* (Pa. Super. 2014) (the two-stage adjudication/disposition structure; continuance denial upheld where the stated reason had no record support); *In re W.Z.* (Pa. Super. 2014) (stipulated adjudication by clear and convincing evidence); *In re A.O.* (Pa. Super. 2014) (counsel's role in dependency); *In re R.J.T.*, 9 A.3d 1179 (Pa. Super. 2010) (goal change; § 6351(f)/(f.1); a child's life cannot be held in abeyance); *In re K.B.* (Pa. Super. 2023) (goal-change review; kinship resource); *In re A.A.R.P.* (Pa. Super. 2019) (§ 6351(f.1) determinations); *In re E.C.* (Pa. Super. 2026) (the § 6351(f)(9) fifteen-of-twenty-two determination and documented compelling reasons at permanency review); *In re Mother* (Pa. Super. 2017) (continuance denial reversed where the parent was denied the chance to confront witnesses — the other side of Scenario 71's coin); *In re R.R.* (Pa. Super. 2026) (agency petition DENIED at trial; the court credited the family's expert witnesses over the agency's — the documented basis for Scenario 73's and 75's winnability); *In re K.M.S.* (Pa. Super. 2022) (bonding/parenting evaluation testimony weighed at hearing); *In re Z.P.*, 994 A.2d 1108 (Pa. Super. 2010), and *In re T.S.M.*, 71 A.3d 251 (Pa. 2013) (no formal bonding evaluation or expert testimony is legally required; the court weighs all of the evidence — the principle under Scenario 75, stated in player text only generically).

## New law verified this run (primary text read in full)

The Version 1 verified set is unchanged. Added this run, from the official text of Title 42 (read via the General Assembly's consolidated-statute publication):

- **42 Pa.C.S. § 6341(c)** — a child may be found dependent only "from clear and convincing evidence"; disposition follows immediately or at a postponed hearing "not later than 20 days after adjudication if the child has been removed." § 6341(a): if the child is not found dependent, the court "shall dismiss the petition" and discharge the child.
- **42 Pa.C.S. § 6341(d)** — at disposition, "all evidence helpful," including written reports, may be received "even though not otherwise competent in the hearing on the petition"; the parties "shall be afforded an opportunity to examine and controvert written reports so received and to cross-examine individuals making the reports." This two-stage evidence rule is the spine of Scenarios 70 and 75 — and it is why those scenarios are careful to fight the report at ADJUDICATION (where the wide welcome does not apply) rather than pretend reports are never admissible anywhere.
- **42 Pa.C.S. § 6351(a)(1), (a)(2)(i)** — disposition may leave the child with the parent subject to conditions and supervision, or transfer temporary legal custody to a qualified individual, "including any relative."
- **42 Pa.C.S. § 6351(b)** — before a disposition removing the child, the court "shall enter findings on the record": continuation in the home contrary to the child's welfare, and whether reasonable efforts were made to prevent removal. Scenario 76's closing beat is built on the phrase "on the record."
- **42 Pa.C.S. § 6351(e)(3)(i)** — permanency hearings within six months of removal and of each previous permanency hearing. (Version 1 strategy guides spoke of the six-month review rhythm generically; it is now citation-verified.)
- **42 Pa.C.S. § 6351(f)** — the determinations each permanency hearing must make, including (f)(2) compliance with the permanency plan, (f)(3) progress toward alleviating the original circumstances, (f)(5.1) reasonable efforts to finalize the plan, and (f)(9): at 15 of the last 22 months, whether the agency has filed or joined a termination petition UNLESS (i) relative care, (ii) a documented compelling reason, or (iii) the family was not provided the services necessary for safe return within the plan's time frames. Scenarios 72, 74, 75, and 76 are built directly on this subsection's list.
- **42 Pa.C.S. § 6351(f.1)** — the outcome determinations that follow from (f): return; adoption with a termination filing; legal custodian; fit and willing relative; another planned permanent living arrangement.

NOT newly verified, and therefore used only as in Version 1: § 6302 definitions; § 6381(d) prima facie evidence (researched as texture for Scenario 73's medical proof and deliberately NOT cited in any player-facing text); hearing-notice and subpoena mechanics (kept generic — "counsel arranges it"); appellate procedure (stated generically, as in Version 1). Rule 1340's application to a scored assessment summary remains expressly UNTESTED everywhere it appears — unchanged from Version 1.

## Engine-flag note (removed / recordsRequested)

`recordsRequested` is set on at least one choice on the winning route of all ten scenarios (validator-enforced). `removed` is set ONLY where a removal physically occurs inside the playable story: Scenarios 67, 68, and 73 (removals on day 0 of each). In Scenarios 69–72 and 74–76 the children's placements predate the story (stated in each opening), the flag is absent by design, and no 72-hour banner should fire — the shelter care clock is not those stories' clock. Scenario 76's children entered care October 20, 2026; the fifteen-month date — January 20, 2028 — matches the production deadline test suite's permanent case (foster entry October 20, 2026 → January 20, 2028), and Scenario 67's removal (October 20, 2026) and shelter care hearing (October 23, 2026) match the suite's shelter care case.

## Dates audited

Every kicker in all ten scenarios was recomputed programmatically against the real calendar (weekday, month, day, year from startDateISO + dayOffset); day offsets are non-decreasing along every edge of every graph (validator output in the batch report). Scenario start dates: S67 Tue Oct 20, 2026 · S68 Mon Jan 11, 2027 · S69 Mon Nov 9, 2026 · S70 Mon Nov 23, 2026 · S71 Mon Nov 16, 2026 · S72 Mon Nov 30, 2026 · S73 Mon Nov 2, 2026 · S74 Tue Dec 8, 2026 · S75 Mon Nov 16, 2026 · S76 Wed Dec 1, 2027.

## Scenario 67 — "The Room Where It Happens" (Foundation, 20 nodes, 2 endings)

**Family:** Colette Voss, an overnight-shift warehouse worker; her son Amos (9). The sitter quits by text at 6 p.m.; a worried neighbor calls; Amos is taken that night.
**Documented patterns drawn on:** the shelter care hearing as the first courtroom a parent ever sees (who is in the room, what it can and cannot decide); adjudication failing on an unproven date — the agency's witness was not present for the day alleged (burden texture from the adjudication opinions above, esp. *In re L.Z.* and *In re C.Z.*'s two-stage account).
**Law in the data:** § 6332 / § 6315(d) (72 hours); § 6337 / § 6332(a) (counsel); § 6341(c)/(a) (clear and convincing; dismissal); § 6341(d)(1)–(2) (the two stages, taught in prep); § 6351(b) (findings, in the placed branch); § 6351(e)(3)(i) (the six-month clock named in the placed debrief); § 3130.44(d).
**Alterations:** composite in full; the neighbor is written as worried, not hostile — a deliberate counterweight to villain-casting in training material.
**Deliberately not used:** no scored-assessment beat (kept out of the Foundation tier's first courtroom on purpose — the burden lesson lands cleaner alone); no Rule 1340.

## Scenario 68 — "Ten Minutes in the Hallway" (Foundation, 19 nodes, 2 endings)

**Family:** Karl Hale, a delivery driver; his daughter Selin (6). A work emergency runs long; Selin is left with a neighbor's teenage son; she is taken that evening.
**Documented patterns drawn on:** appointed counsel meeting the parent minutes before the shelter care hearing — a recurring, documented feature of high-volume dependency practice; the decisive fact (grandmother present until 7 p.m.) existing in the family's knowledge but not in the agency's account; counsel-effectiveness texture from *In re A.O.*
**Law in the data:** § 6337; § 6332(a); § 6332 / § 6315(d); § 3130.44(d)/(f); § 6341(c)/(a); § 6351(b); § 6351(e)(3)(i).
**Alterations:** the appointed lawyer is competent and overloaded, never lazy or corrupt — the failure mode taught is information logistics (one page, witness named first, ten minutes used in the right order), not bad lawyers.
**Deliberately not used:** no ineffectiveness litigation beat — the scenario teaches the parent-side moves that make counsel effective, not the appeal that follows when they fail.

## Scenario 69 — "Answer the Question Asked" (Hard, 29 nodes, 3 endings)

**Family:** Ingrid Sorensen; her son Finn (11), placed October 19, 2026 (pre-story) after a recess fall became a supervision petition.
**Documented patterns drawn on:** cross-examination of the parent as the moment adjudications actually turn; credibility as the fact-finder's call (*In re L.Z.*); the caseworker's testimony impeached by the caseworker's own notes — a documented appellate texture, here produced by the § 3130.44(d) request rather than by luck.
**Law in the data:** § 6341(c)/(a); § 6351(a)(1) (partial ending); § 3130.44(d); Rule 1340(E)/(F) rebuttal, flagged untested at every appearance.
**Alterations:** the volunteered-admission trap is written as love, not foolishness — the mother wants the judge to *know* her; the strategy guide says so plainly.
**Deliberately not used:** no hearsay doctrine (kept out; Scenario 70 carries the evidence-stage lesson); the teacher witness is honest and limited, not a plant.

## Scenario 70 — "A Report Is Not a Witness" (Hard, 30 nodes, 3 endings)

**Family:** Emmett Merritt; his daughter Jade (8), placed October 2026 (pre-story). The petition's central allegation quotes a school nurse's report at one remove; the nurse is not on the witness list.
**Documented patterns drawn on:** petitions that outrun their source documents; the two-stage evidence structure of § 6341 (the report's wide welcome exists at disposition, § 6341(d)(1) — the scenario's objection is therefore staged at adjudication and framed exactly, including the § 6341(d)(2) right to controvert reports and cross-examine their makers).
**Law in the data:** § 6341(c)/(a); § 6341(d)(1)/(2); § 6351(a)(1)/(b); § 3130.44(d)/(f); Rule 1340(E)/(F) for the scored summary's quotation of the petition's version, flagged untested.
**Alterations:** the nurse, when her original note is produced, is careful and fair; the error is in the retelling, not in her.
**Deliberately not used:** no subpoena mechanics (kept generic — "counsel arranges it, if told early"); no claim that reports are inadmissible everywhere — the debriefs state the two-stage rule accurately in both directions.

## Scenario 71 — "Four More Weeks" (Hard, 28 nodes, 3 endings)

**Family:** Teresa Garza; her son Omar (13), living with his aunt since September 14, 2026 (pre-story kinship placement).
**Documented patterns drawn on:** the morning-of continuance ask, and the two published directions of travel — denial upheld where the stated reason had no record support (*In re C.Z.*, citing *In re K.J.*), reversal where proceeding without the parent denied confrontation (*In re Mother*, 2017). The scenario teaches the parent-side constant in both: outcomes follow what the record shows about diligence, readiness, and the child's time. No case is cited in player text.
**Law in the data:** § 6341(c)/(a) (the burden the agency must carry if the hearing proceeds); § 6341(d) (the supervisor-reading-a-file contrast); § 6351(a)(1) (the partial ending's disposition); § 3130.44(d).
**Alterations:** all three strategies (oppose / consent with terms / let it happen) are written as genuinely defensible; the loss comes from drift and silence, not from choosing the "wrong" branch — consent-with-teeth is a partial win by design, because a month of a 13-year-old's life is a real cost even when the ending is home.
**Deliberately not used:** continuance doctrine is stated generically (discretion + record), with no invented rule or deadline — none was verified, so none is stated.

## Scenario 72 — "The Word 'Minimal'" (Hard, 30 nodes, 3 endings)

**Family:** Deanna Fenn; her son Ravi (7), placed June 15, 2026 (pre-story). The court report for the six-month permanency review calls her compliance "minimal"; her folder and the agency's own visit logs say otherwise.
**Documented patterns drawn on:** narrative court reports whose adjectives outrun the underlying logs; § 6351(f)'s determinations as evidence-driven findings rather than report adoptions — the scenario is built directly on the verified text of (f)(2), (f)(3), and (f)(5.1).
**Law in the data:** § 6351(e)(3)(i); § 6351(f)(1),(2),(3),(5.1); § 3130.44(d); Rule 1340(E)/(F), flagged untested.
**Alterations:** the two missed visits are given a documented, ordinary cause (a suspended bus route, with the transit letter as an exhibit) — logistics, not virtue, per the design pillars.
**Deliberately not used:** no goal-change threat is adjudicated here — agency counsel "floats" it in the loss ending only, and Scenario 74 carries the full goal-change fight.

## Scenario 73 — "The Agency's Burden" (Complex, 44 nodes, 4 endings)

**Family:** Stefan Novak; his daughter Esme (5), removed in-story on day 0 after an ER visit for a bruised thigh; adjudication tried over two days (days 30–31); the placed branch's disposition lands day 38, inside § 6341(c)'s 20-day discipline.
**Documented patterns drawn on:** the full adjudication trial — element-by-element proof, credibility findings, an examining treating witness against a records-review expert. Winnability is documented, not wished: in *In re R.R.* (Pa. Super. 2026) the trial court denied the agency's petition and credited the family's experts over the agency's; the misfiled-photograph beat is a composite of ordinary file-error practice, framed as clerical, never sinister.
**Law in the data:** § 6341(c)/(a) (burden; dismissal); § 6341(d) posture for the scored summary fight (with the Rule 1340(A)/(B)(1)/(E)/(F) argument, flagged untested at every use); § 6351(b) (day-38 findings); § 6351(a)(1) (partial ending); § 3130.44(d); § 6332 (shelter care beat).
**Alterations:** the agency's expert is qualified and wrong on method (never examined the child; never saw the clinic letters), not unqualified — cross goes to method, per the documented texture.
**Deliberately not used:** § 6381(d) prima facie evidence — researched, not verified from primary text this run, and therefore nowhere cited in the data; medical specifics kept at the level of "what the witness examined and what she was never sent."

## Scenario 74 — "Goal: Changed?" (Complex, 40 nodes, 3 endings)

**Family:** Josephine ("Josie") Haas; her son Quinn (4), in care since February 9, 2026 (pre-story). At month 10 the agency asks the court to change the goal from reunification to adoption.
**Documented patterns drawn on:** the goal-change framework of *In re R.J.T.* and *In re K.B.* — the (f) determinations first, the (f.1) outcome second; a kinship resource reframing the (f.1) menu; a stale CASA report describing a parent who no longer exists; the unsent-referral reasonable-efforts failure, a documented pattern given statutory footing here through (f)(5.1).
**Law in the data:** § 6351(f)(2),(3),(5.1); § 6351(f.1)(1),(2),(4); § 6351(f)(9) framed honestly as NOT yet triggered at month 10 (with (iii)'s services principle argued through (f)(5.1), not smuggled into (f)(9)); § 3130.44(d); Rule 1340(E)/(F) once, flagged untested; termination burden (clear and convincing) stated in the loss debrief.
**Alterations:** the agency's "a child's life cannot be held in abeyance" argument is given its full force and answered with a dated stepped return rather than dismissed — both sides of *R.J.T.*'s principle are real, and the guide says so.
**Deliberately not used:** no appeal mechanics (stated generically, as in Version 1); the aunt's out-of-state study is described without interstate-compact specifics, which were not verified.

## Scenario 75 — "Two Experts, One Child" (Complex, 42 nodes, 3 endings)

**Family:** Vernon Quill; his daughter Paloma (6), placed March 16, 2026 (pre-story). The agency's permanency-review case rests on a bonding/parenting evaluation built on two 45-minute observations; the treating therapist of fourteen months and the visit supervisor's logs point the other way.
**Documented patterns drawn on:** evaluation testimony weighed — and discounted on method — at permanency and termination hearings (*In re K.M.S.* texture); the governing principle from *In re Z.P.* and *In re T.S.M.* that no formal bonding evaluation or expert is legally required and that the court weighs all the evidence — stated in player text only generically ("the evaluator is not the judge"), with no new citation introduced into the data beyond the verified set.
**Law in the data:** § 6351(f)(1),(2),(3),(5.1), (f.1), (f)(9) awareness, (e)(3)(i); § 3130.44(d)/(f) (the evaluation's raw notes obtained on written request); § 6341(d)(2)'s examine-and-controvert principle, framed honestly in the guide as the disposition-statute principle carried into the review posture; Rule 1340(E)/(F), flagged untested.
**Alterations:** the evaluator is qualified; only her method is thin (90 minutes, no comparison observation, pre-treatment records) — and her own raw notes, fairly read, cut against her conclusion's adjective.
**Deliberately not used:** no named psychological instruments, no diagnosis talk, no claim that evaluations are worthless — the partial ending (a focused re-evaluation on a properly limited question) is written as a legitimate judicial answer, because it is one.

## Scenario 76 — "The Last Fifteen Minutes" (Complex, 46 nodes, 4 endings) — batch capstone

**Family:** Miriam Brandt; her children Kian (8) and Zara (5), in foster care since October 20, 2026 (pre-story by fourteen months). A combined disposition-review/permanency day at month 14; the fifteen-month date is January 20, 2028.
**Documented patterns drawn on:** the (f)(9) determination as it actually appears at permanency review (*In re E.C.* texture — the court's fifteen-of-twenty-two determination and the documented-compelling-reason inquiry); findings dictated from the bench at the close and the written order that follows — the gap between them is a documented failure mode of busy courtrooms, and the scenario's closing discipline (ask for the findings aloud, in the room) is built on § 6351(b)'s "on the record" and (f)'s determination list.
**Law in the data:** § 6351(f)(9)(ii)–(iii) and its federal twin 42 U.S.C. § 675(5)(E); § 6351(f)(3),(5.1); § 6351(a)(2)(i) (temporary legal custody to the grandmother); § 6351(f.1)(4) (fit and willing relative); § 6351(b); § 3130.44(d).
**Alterations:** the exception packet is argued on BOTH available grounds — documented compelling reason (ii) and services not provided in the plan's time frames (iii) — because the file supports both; the grandmother's bridge placement is presented as a bridge (the win keeps reunification as the goal with dates), never as a quiet permanent transfer.
**Deliberately not used:** Rule 1340 plays no part (the summary is not this hearing's fight, and the batch says so rather than forcing the beat); no termination-hearing procedure — the loss debrief states only the verified burden and that a filing is not an outcome.

## Batch validation record

All ten scenario graphs were walked programmatically (structure, next-resolution, reachability, ending debriefs, monotonic dayOffsets, kicker dates recomputed against the real calendar) and every strategy guide's route was re-walked independently, with the guide's stated node count and final cash matched against the walker's output — 10/10 exact. Citation sweep: no citation appears in any Batch I file outside the verified set (Version 1 set plus the § 6341/§ 6351 family verified this run). First names of all protagonists and children were checked against every other scenario file in the corpus (1–36, 37–66, 77–136 as landed during production): nine collisions with concurrently-landing batches were found at central validation and resolved by renaming within this batch (Colette/Amos, Karl/Selin, Emmett, Teresa, Ravi, Quinn, Zara are this batch's final names). `recordsRequested` is set on the winning route of all ten scenarios; `removed` appears only in 67, 68, and 73, where the removal happens on stage.
