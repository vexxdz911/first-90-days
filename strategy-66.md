# Strategy Guide — Scenario 66: "The Discharge Summary"

*Game documentation for a fictional simulation in "The First 90 Days" (Tactic Watch). The family, the case, and every choice below are fictional. This guide is general information about how the scenario is built — it is not legal advice for any real case.*

## (1) The win

**Best ending: "Ending — The Summary Says Progress."**

State it honestly: this is a **partial** win. The agency goal is re-coded on the record as completed-to-the-extent-the-benefit-allowed, with the step-down underway, before the review report is drafted. Dario is **still placed** at the curtain. The discharge was never a failure — it was arithmetic, a benefit's session cap reached at week 10 of 12 — and the win is only that the file ends up saying so, in the file's own language, in time.

## (2) The route

Verified by walking the scenario graph from the start node (see the verification note at the end). The full walked route, with decision points explained:

1. **Week Ten of Twelve** → **How Week One Felt** → **The Rhythm** → **Screens, Filed by Others** → **The Saturday Call** → **Wednesday with Dario** → **The Employer, Notified in Writing** — ten weeks of documented progress: attendance, screens, visits, a sponsor, an employer whose schedule bends around program evenings because they were put in writing months ago.
2. **The Letter About Sessions** → **A Counselor Who Is Sorry and Specific** → **Calling the Number on the Letter** — Cash −5. The discharge is a benefit limit, verified by phone; the counselor states exactly what the discharge summary will say. → **The Appeal, Filed Without Illusion** — Cash −3; the insurer appeal documents the cap through channels.
3. **The Last Day: Paper or Handshake** — *Ask for the discharge summary in writing before you leave — sign the release, take the document.* Cash −4. Sets **dischargeSummary**. This is the scenario's hinge: the summary states his progress, his attendance, and the reason — benefit limit.
4. **Discharged, in the Ordinary Sense** → **The Folder That Night** → **How the System Codes a Discharge** — the agency's goal line ("complete IOP") is coded by status field: *goal: not completed*, with no place for the reason. → **Ms. Nakamura's List** → **The Plan, in Legal Order** — the campaign, agreed by worker and counsel (42 Pa.C.S. § 6337): notify in writing with the summary attached, before the review; enroll in the step-down with proof; read the coding via the record; correct it in writing.
5. **Three Weeks, Explained Slowly** → **Intake Paperwork** — *Complete the intake packet now and take the dated enrollment confirmation.* Cash −6. Sets **stepdownEnrolled**. → **The Gap, Week One** → **The Gap, Week Two** → **The Bus Pass Decision** — *Buy the pass now.* Cash −24. The three-week gap is bridged and documented, not waited out.
6. **Notifying the Agency, Before the Review** — *Send the written notification now, with the summary and enrollment attached.* Cash −5. Sets **agencyNotified**. Timing is the entire mechanism: the review report will be drafted from a file that already holds the program's own words. → **What the File Holds Tonight**.
7. **Reading the Coding** — *Sign and send the written records request this week.* Cash −4. Sets **recordsRequested** (55 Pa. Code § 3130.44(d)). → **Goal: Not Completed, in Print** — the miscoding read on its page and line, next to his own filed submission.
8. **The Written Correction** — *File the written correction with the summary and enrollment attached.* Cash −5. Sets **correctionFiled**: discharge reason stated, goal re-coding requested, documents cited. → **The Week the Step-Down Opens** → **Dario's Question** → **The School Note** → **The New Chair** — *Send the step-down's attendance confirmation.* Cash −4. The gap now has a far shore with a date on it.
9. **Payday, Thin and Sufficient** → **The Review Notice** → **Final Preparation** → **What the Report Will Say** → **The Eve of the Review** — the audit is complete: every campaign document either is or is not in the agency's file, and on this route all of them are.
10. **The Review** — *The report is read from the repaired file.* This choice is flag-gated: **dischargeSummary** + **agencyNotified** + **stepdownEnrolled**. It leads to **Ending — The Summary Says Progress**.

## (3) Why this wins — the law as it is supposed to work

Only principles from the scenario's verified set are stated here:

- **No exotic law is used, and the guide says so.** The scenario runs on process, not doctrine: a discharge summary is a provider document; a coding field is an agency artifact; a review is argued from a report; a report is drafted from a file. The legal content is the scaffolding that makes the paperwork moves available.
- **Counsel** (42 Pa.C.S. § 6337) sequences the campaign: the same documents, sent after the report is drafted, would have been a rebuttal instead of a record.
- **The parent's own record is released on request** — 55 Pa. Code § 3130.44(d) ("shall be released upon request"). Step 7 is the audit that turns "the coding is wrong" from a belief into a page-and-line citation a correction can attach to.
- **What the win is not.** No placement was decided, no burden of proof was tested, and no hearing on any petition is depicted. The review continued the plan on a corrected record. That is the whole claim.

## (4) The traps

1. **The handshake at "The Last Day: Paper or Handshake"** (no **dischargeSummary**). The counselor's "you did great" is sincere, remembered, and unusable. Every later document loses its anchor exhibit, and the review gate's choices collapse to **Ending — Goal: Not Completed** — four words outliving a ten-week effort.
2. **Waiting to be contacted at "Intake Paperwork"** (no **stepdownEnrolled**). The step-down will call; programs do. The file holds a three-week silence where an enrollment should be, and the best-ending choice at "The Review" closes. What remains open lands on **Ending — Goal: Not Completed**: even with the summary obtained and the agency notified in advance, the report reads a plan whose central step never began.
3. **Explaining at the review instead of notifying before it** (no **agencyNotified**). The summary and correction may still exist — believed in the room, minuted in a clause — but the report was drafted from the status field: **Ending — A Gap, Explained Late**. The truth arrives; the framing already happened.
4. **Holding the correction for the room at "The Written Correction"** (no **correctionFiled** filed in time). Seen is not the same as used; the report writer never met it in the file.

## (5) What no strategy controls

The insurer's cap itself, and its appeal's season; a counselor less specific or a program that keeps worse paper; a worker less honest about her own screen than Ms. Nakamura is; a step-down whose next opening is in three months rather than three weeks; a report writer who clings to the status field even against a filed correction. People, systems, and luck hold pieces of every ending here. The route controls only the chain: paper obtained at the door on the last day, notice given before the drafting, enrollment proven instead of promised, the coding read and corrected in writing. It never controls whether Hector is a good father — the scenario is careful, throughout, that the four words were never a measurement of that.

---
*Verification: this route was walked programmatically against `scenario-66.json` — each named choice was followed from the start node in order; every intermediate node and choice exists; the flag-gated review choice's requirements (dischargeSummary + agencyNotified + stepdownEnrolled) were satisfied by flags set earlier on the walk; the walk terminates at the ending node titled "Ending — The Summary Says Progress" after visiting 38 nodes, with $100 of the $160 starting cash remaining. Walked path: start -> intake_echo -> program_rhythm -> screens_routine -> sponsor_beat -> visit_beat66a -> employer_beat66 -> benefit_letter -> counselor_talk -> call_insurer -> appeal_info -> summary_choice -> discharge_day -> last_day_scene -> coding_beat -> worker_call -> nakamura_meeting -> gap_explained -> stepdown_beat -> gap_week -> gap_support -> transport_beat66 -> notify_beat -> letter_to_file -> records_beat66 -> coding_seen -> correction_beat66 -> hallway_beat66 -> dario_visit -> dario_school -> stepdown_start -> money_beat66 -> review_notice66 -> counsel_prep66 -> review_prep_docs -> eve_beat66 -> review66 -> end_summary.*
