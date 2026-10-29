# SOURCES, ALTERATIONS, LAW, AND VALIDATION — HARD BATCH C (Scenarios 17–21)

*Production record for “The First 90 Days,” Hard scenarios 17–21. Draft documentation for internal development and attorney review. Nothing in this batch is legal advice or a depiction of a real family.*

## Source and alteration rule

Every scenario is a fictional composite built only from published Pennsylvania Superior Court or Commonwealth Court material and, for Scenario 20, the official text of Act 119 of 2013. Names, ages, counties, occupations, family configurations, and identifying facts were altered, and published beats were merged rather than copied as a single family’s story. No private case, person, file, or fact from the project’s own orbit was used.

The legal rule was equally narrow: a proposition appears as law only if it is in the batch’s shared verified set. Everything else is either generic process, a fictional office’s stated procedure, or deliberately withheld.

## Batch validation summary

All five JSON files were centrally re-audited after production, independent of the individual writers’ checks:

| Scenario | Nodes | Endings | Script parity | Records flag | Removal flag | Strategy path |
|---|---:|---:|---|---|---|---|
| 17 — The Empty Apartment | 30 | 3 | 30/30 IDs, same order | Set once | Absent | Verified, 25-node route |
| 18 — The Paternity Question | 32 | 3 | 32/32 IDs, same order | Set by each parent on separate choices | Absent | Verified, 23-node route |
| 19 — The Probation Crossover | 31 | 3 | 31/31 IDs, same order | Set once | Absent | Verified, 19-node route |
| 20 — The Daycare Letter | 32 | 3 | 32/32 IDs, same order | Set once | Absent | Verified, 18-node route |
| 21 — The Relapse Report | 33 | 3 | 33/33 IDs, same order | Set on written-request choices | Set on exactly one removal choice | Verified, 13-node route |

For every scenario, the central audit confirmed:

- JSON parses and node IDs are unique.
- Every choice target resolves and every node is reachable from `start`.
- Every non-ending has choices; every ending has `ending: true`, no choices, and a debrief.
- `dayOffset` never decreases along any choice edge.
- Every kicker’s stated weekday and calendar date equals `startDateISO + dayOffset`.
- Each strategy guide contains the five required sections and names its scenario’s best ending exactly as that ending is titled in the JSON.
- Each strategy route below was checked as a sequence of actual graph edges, not inferred from the prose.

### Winning routes checked

- **17:** `start → inspection_day → the_list → records_request → landlord_clock → triage → hardware_run → hot_water_letter → shift_trade → dated_photos → visit_planning → receipt_folder → reinspect_request → prep_thorough → plumber_day → worker_check → extension_talk → money_crunch → records_arrive → packet_night → reinspection_day → result_pass → movein_prep → transition_weekend → end_repaired`
- **18:** `start → mom_notice → father_reply → father_counsel → mom_visit → father_work → mom_records → father_dates → mom_boundaries → father_availability → first_contact → mom_stability → father_follow → setback → mom_writing → worker_checkin → packet_build → mom_packet → the_folder → strong_deliver → mom_strong → review_strong → end_documented`
- **19:** `start → po_sheet → agency_paper → portal → records → bus_ledger → shift → confirmations → cousin → missed_call → trip → counsel_check → collision → collision_written → clean_reschedule → clean_packet → clean_night → clean_review → end_clean`
- **20:** `start → read_letter → daycare → two_clocks → counsel → appeal_filed → records_dep → service_plan → visit → evidence_packet → divided → gather → prehearing → hearing_strong → review_prep_exp → review_exp → decision_exp → end_expunged`
- **21:** `start → first_calls → kin_call → caseworker_strong → voluntary → assessment_day → lab_questions → records_request → supervision_plan → wed_visit → followup_week → december_review → end_home`

### Coordinator QA correction

The first drafts of Scenarios 17 and 19 accidentally reused the exact parent/child names “Dana Ellis” and “Eli,” despite different ages and incompatible story postures. Before delivery, Scenario 19’s parent and child were renamed **Tessa Morgan** and **Jonah** in the JSON and matching script. No node, choice, graph edge, or strategy route changed; script/JSON parity for Scenario 19 was rechecked after the rename.

---

## Scenario 17 — “The Empty Apartment”

**Best ending, exactly as titled:** “Ending — Repairs Verified: Move-In and Reunification Proceed”

**Story:** Dana Ellis, a home-health aide, has reunification approved in principle. Her new apartment fails inspection on four fixable items. The pressure is a landlord’s lease hold expiring Wednesday, February 4, 2026 — expressly a contractual/practical deadline, not a statute — interacting with transition visits, shift work, and money.

### Published sources and texture

1. *In re: Adoption of A.P.C.-D.*, No. 1432 MDA 2025 (Pa. Super. Apr. 13, 2026) — housing described in agency testimony as “the only barrier remaining to reunification,” and the broader record-discipline theme that a court can act only on the record before it. https://law.Justia.com/cases/pennsylvania/superior-court/2026/1432-mda-2025.html
2. *In the Interest of L.W.*, 2025 PA Super 157, No. 1218 WDA 2024 — a caseworker’s position that reunification would be recommended but for a single pending barrier, and paper remediation of housing/income-verification items. https://www.casemine.com/judgement/us/6882085ce89456b75691459c/amp
3. *In re K.J.C.* (Pa. Super. 2024), Studicata summary used for texture only — housing barriers partly outside the parent’s control and the relevance of documented efforts. https://www.studicata.com/summaries/superior-court-of-pennsylvania/in-re-k-j-c-2024-srha1l/

### Alterations

The composite parent is a 31-year-old home-health aide; her son Eli is seven. The county is unnamed. The four inspection findings (hall detector, bathroom latch, outlet covers, hot-water element), the lease hold, the landlord, the repair sequence, and all dialogue were invented around the published “one remaining barrier + paper record” structure. No published family’s housing facts were reproduced as a matching set.

### Law used

- **55 Pa. Code § 3130.44(d)** only: the parent requests the case record in writing, including inspection and service-plan material; the scenario uses the verified formulation that the record “shall be released upon request.”

### Deliberately withheld

- Shelter-care timing, because no removal occurs in-story.
- Counsel, CPSL appeal provisions, ASFA, Rule 1340, and burden language, because none is the governing pressure in this scenario.
- Any suggestion that the February 4 lease date is statutory. The story and every ending debrief call it the landlord’s deadline.

---

## Scenario 18 — “The Paternity Question”

**Best ending, exactly as titled:** “Ending — A Documented Role, and a Path”

**Story:** Four-year-old June is already in placement when a father is identified and notified late. The game interleaves the father’s effort to appear on paper before he appears in person with the mother’s effort to document the stability any change must protect. The June 15, 2026 review is the pressure point. The best ending is expressly partial: a documented role and path, not immediate placement.

### Published sources and texture

1. *In Re: K.A.M., Appeal of: S.M., Father*, No. 922 EDA 2014 (Pa. Super. Oct. 16, 2014) — a father who responded in writing while incarcerated, followed by court-appointed counsel; the contrast between letters/testimony and what the file actually contains. https://law.justia.com/cases/pennsylvania/superior-court/2014/922-eda-2014.html
2. *In the Interest of: A.M.L., Appeal of: T.C.*, No. 1017 MDA 2025 (Pa. Super. Jan. 16, 2026) — a father surfacing long after the case began, with a dispute over whether the agency had his identity and a file containing no earlier calls or messages from him. https://law.Justia.com/cases/pennsylvania/superior-court/2026/1017-mda-2025.html
3. *In the Interest of: S.L.M.R.’s, Appeal of: K.C.* (Pa. Super. 2025), used at search/summary level for parent-locator and contact-attempt texture only. https://law.justia.com/cases/pennsylvania/superior-court/2025/3156-eda-2024.html

### Alterations

The child became June, age four. The father is not incarcerated in the game; his constraints are late notice, work, transport, and the approaching review. The mother gave the name she had but lacked an address at case opening; neither parent is framed as a villain. Names for the parents, workplaces, county, and dialogue were invented or altered, and beats from the sources were merged rather than assigned to one family.

### Law used

- **42 Pa.C.S. § 6337:** counsel, stated only in the verified broad terms.
- **55 Pa. Code § 3130.44(d):** both parents use written case-record requests on separate beats, and the notice/service-plan dates they see change their planning.

### Deliberately withheld

- Paternity testing, standing, service/notice validity, and any narrower counsel-eligibility rule. Those beats remain procedural and uncited.
- ASFA, shelter-care timing, § 6341, Rule 1340, and burden language.

---

## Scenario 19 — “The Probation Crossover”

**Best ending, exactly as titled:** “Ending — One Calendar, Two Stamps”

**Story:** Tessa Morgan’s son Jonah lives at home while Tessa follows a dependency family service plan and separately reports to a fictional adult probation office. Two portals, two instruction sheets, and two same-time appointments create the pressure. The skill is not a claimed legal doctrine: it is written disclosure to both offices, one calendar, and saved confirmations.

### Published sources and texture

Published dependency material mentioning probation was comparatively thin. The opinions below supplied dependency-side service-plan, appointment, work-schedule, and record texture; the ordinary portal/collision details and the fictional office’s instruction sheet were invented as fiction, not presented as a real office’s rules.

1. *In re: Adoption of M.A.B.* (Pa. Super. 2017) — permanency-plan and missed-appointment texture, including adult probation appearing among the entities in a multi-system case. https://law.justia.com/cases/pennsylvania/superior-court/2017/1720-wda-2016.html
2. *In the Interest of E.J.A.* (Pa. Super. 2023) — layered family-service-plan obligations, including a probation-related plan item, and home-visit/service compliance texture. https://law.Justia.com/cases/pennsylvania/superior-court/2023/740-mda-2022.html
3. *In the Interest of C.C.R.* (Pa. Super. 2019) — family-service-plan objectives and missed appointments treated as record facts. https://law.justia.com/cases/pennsylvania/superior-court/2019/1048-eda-2019.html
4. *In re P.A.R.* (Pa. Super. 2015) — missed visits and the practical importance of whether a parent’s work schedule was ever provided to the agency. https://law.Justia.com/cases/pennsylvania/superior-court/2015/779-wda-2015.html

### Alterations

After coordinator QA, the parent is Tessa Morgan, 34, and her son is Jonah, seven, living at home. The probation office, reporting officer, portals, instruction sheet, family events, and appointment collision are fictional composites. No scenario event is modeled on a real person known to the project.

### Law used

- **55 Pa. Code § 3130.44(d):** written request for the dependency case record.
- **42 Pa.C.S. § 6337:** dependency counsel, in the verified broad formulation.

### Deliberately withheld — and affirmatively not asserted

- No probation rule, violation standard, sanction, eligibility rule, reporting right, or other criminal-law proposition is stated.
- The probation office’s dates, portal, and check-in instructions are described only as that fictional office’s own paperwork.
- No removal occurs in-story, so shelter-care law is not used.

---

## Scenario 20 — “The Daycare Letter”

**Best ending, exactly as titled:** “Ending — Expunged, and Read Accurately”

**Story:** Lena Morales’s son Eli is in a pre-story dependency placement while Lena works at a daycare and follows a service plan. A separate fall involving her cousin’s daughter Ana produces an indicated report. The CPSL appeal and dependency review proceed on separate records. The CPSL notice date is Monday, February 2, 2026; the exact 90th day is **Sunday, May 3, 2026**. The dependency review is Monday, June 1, 2026.

### Published sources and texture

1. *Philadelphia County Department of Human Services v. Department of Human Services*, No. 292 C.D. 2024 (Pa. Cmwlth. July 2, 2025) — an account found consistent with the medical record, the agency’s substantial-evidence burden not carried, and expungement affirmed. https://law.justia.com/cases/pennsylvania/commonwealth-court/2025/292-c-d-2024.html
2. *In the Interest of A.B.*, No. 3353 EDA 2019 (Pa. Super. July 7, 2020) — child-protective and dependency tracks proceeding separately and not mechanically deciding one another. https://law.justia.com/cases/pennsylvania/superior-court/2020/3353-eda-2019.html
3. *In re J.M.*, No. 1182 MDA 2023 (Pa. Super. Jan. 10, 2024) — permanency-review texture: compliance ratings, visit percentages, transportation barriers, and service-plan gaps read from the dependency record. https://law.justia.com/cases/pennsylvania/superior-court/2024/1182-mda-2023.html
4. **Act 119 of 2013**, official text, for the CPSL provisions used in the game. https://www.palegis.us/statutes/unconsolidated/law-information/view-statute?txtType=PDF&SessYr=2013&ActNum=0119.&SessInd=0

### Alterations

The composite mother is Lena Morales, 34. Her dependency child is Eli, seven; the child in the separate incident is her cousin’s daughter Ana. The porch-step fall, daycare, evidence packet, photographs, and all names/dialogue were altered or invented. The daycare’s schedule pause is expressly the fictional employer’s stated process, not an employment-law rule.

### Law used

- **23 Pa.C.S. § 6341(a)(2):** written appeal within 90 days of notification; February 2 + 90 days = May 3, 2026.
- **23 Pa.C.S. § 6341(c.2)(4):** investigation evidence, including potentially exculpatory material, in the CPSL appeal track.
- **23 Pa.C.S. § 6341(c.2)(5):** the department or county agency bears the burden of proving by substantial evidence that the report should remain indicated.
- **23 Pa.C.S. § 6341(c.3):** the fictional chronology conforms to the decision window — hearing concludes May 12 and the decision is entered June 5, 24 days later.
- **23 Pa.C.S. § 6341(g):** used only in the upheld ending’s debrief, with the 15-day reconsideration and 30-day Commonwealth Court perfection clocks stated from the final order’s mailing date.
- **55 Pa. Code § 3130.44(d):** Eli’s separate dependency case record, requested on written request and kept distinct from CPSL investigation disclosure.
- **42 Pa.C.S. § 6337:** dependency counsel in the verified broad formulation.

### Deliberately withheld

- Employment-law rights or consequences.
- Any retention period for an indicated report.
- Any § 6381(d) presumption mechanics noticed in source texture.
- Rule 1340/UA and ASFA propositions, because neither is needed to decide this scenario’s two tracks.

---

## Scenario 21 — “The Relapse Report”

**Best ending, exactly as titled:** “Ending — Home, Under a Documented Plan”

**Story:** Seven-year-old Sam has been home full-time for six weeks during expanded trial-home time at month eight when one screen is reported positive. The first 48 hours — treatment contact, support-person contact, assessment, provider questions, a written case-record request, and a concrete supervision plan — determine whether the result travels with context or alone. A voluntary kin arrangement is possible; an in-story removal occurs on only one branch.

### Published sources and texture

1. *In the Interest of Z.J., Appeal of B.J.*, No. 1797 EDA 2025 (Pa. Super. Dec. 9, 2025) — substantial treatment progress followed by a positive screen, communication falling off, and no return to treatment; used mainly as the counterfactual thin-record path. https://law.justia.com/cases/pennsylvania/superior-court/2025/1797-eda-2025.html
2. *In the Interest of S.R.S., Appeal of C.M.*, No. 1070 WDA 2022 (Pa. Super. Mar. 17, 2023) — one late-provided screen, missed screens, and review complicated by missing documentation. https://law.justia.com/cases/pennsylvania/superior-court/2023/1070-wda-2022.html
3. *In the Interest of A.O., Appeal of D.A.K.*, No. 346 EDA 2018 (Pa. Super. Sept. 11, 2018) — substantial compliance discussed alongside a positive screen, kin safety planning, and provider progress material that did not reach the file. https://law.justia.com/cases/pennsylvania/superior-court/2018/346-eda-2018.html

### Alterations

The composite child is Sam, seven. The parent is unnamed. The story uses a six-week trial-home posture, an adult sister/kin support named Lou, a sponsor/support contact, and a 48-hour documentation sequence assembled across the sources. Substance specifics from the opinions were not carried over as an identifying fact pattern, and no real person known to the project was modeled.

### Law used

- **55 Pa. Code § 3130.44(d):** written request for case-record material around the reported result and the following two days.
- **42 Pa.C.S. § 6337:** counsel on the court paths.
- **42 Pa.C.S. § 6332 and 23 Pa.C.S. § 6315(d):** on the sole removal branch, removal at day 0 (Monday, November 2, 2026) leads to the shelter-care date at day 3, **Thursday, November 5, 2026**.

Flag logic was exhaustively path-checked by the writer and centrally sampled: `removed` is set only by `visit_unprepared → removal_night`; no path carrying `removed` reaches the home ending, and every path to the shelter-return or continued-placement ending carries it.

### Deliberately withheld

- Any right to a retest, withdrawal of a result, or particular laboratory standard. The game documents questions asked; it does not convert them into entitlements.
- Any automatic consequence from one screen.
- Criminal or probation law.
- The clear-and-convincing burden at the shelter-care stage.
- CPSL appeal, ASFA, and Rule 1340 material, because none is needed for this scenario’s decision structure.

---

## Strategy guides delivered with this batch

- [Strategy 17](sandbox://workspace/your_files/tacticwatch-game/strategy-17.md)
- [Strategy 18](sandbox://workspace/your_files/tacticwatch-game/strategy-18.md)
- [Strategy 19](sandbox://workspace/your_files/tacticwatch-game/strategy-19.md)
- [Strategy 20](sandbox://workspace/your_files/tacticwatch-game/strategy-20.md)
- [Strategy 21](sandbox://workspace/your_files/tacticwatch-game/strategy-21.md)

Each guide is framed as documentation for its fictional scenario, states the best outcome without overselling it, identifies graph-verified decision points and traps, separates verified law from documentation strategy, and closes with the limits imposed by workers, judges, records, and chance.
