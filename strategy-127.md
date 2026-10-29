# Strategy Guide — Scenario 127: "The Whole Table, Gently"

*Game documentation for a fictional simulation in "The First 90 Days" (Tactic Watch). The family, the case, and every choice below are fictional. This guide is general information about how the scenario is built — it is not legal advice for any real case.*

## (1) The win

**Best ending: "Ending — Home by Friday."**

This is a **full** win, and the scenario is built so a Foundation player can reach it: both clocks answered — the children home on a written step-down, the kinship placement preserved as the family's own safety net, and the indicated report amended on appeal. It is the gentlest capstone in the library because its mechanics are the library's core lesson in its purest form: file the immovable deadline first, then build the record.

## (2) The route

Verified by walking the scenario graph from the start node (see the verification note at the end). Key decision points, in order — node title, winning choice, and what it changes:

1. **The Deadline in the Second Letter** — *Write both dates on the kitchen calendar and circle May 31* Sets **calendarSet**.
2. **Garazi's Kitchen** — *Ask what the study needs, write the list down, and text it to yourself before you leave* Cash −$5; Sets **studyList**.
3. **Visits at Garazi's Table** — *Keep the sheet religiously and copy it monthly into your folder* Sets **visitLog**.
4. **The Lawyer's Twenty Minutes** — *Ask her to help you draft the appeal letter today, while you are sitting here* Sets **lawyerMet**.
5. **One Letter, Two Copies** — *Mail the appeal this week and keep the stamped copy in the folder* Cash −$10; Sets **appealFiled**.
6. **The Boiler, On Paper** — *Request the repair log and invoice in writing and attach copies to both files* Cash −$5; Sets **repairPaper**.
7. **The Acknowledgment** — *File the acknowledgment with the stamped copy and note the docket number on the calendar* Sets **appealDocketed**.
8. **Asking for the File** — *Sign the written record request and keep the stamped copy* Cash −$5; Sets **recordsRequested**.
9. **What the Mirror Shows** — *Write a one-page statement in your own words and file it with the repair documents, in both files* Cash −$5; Sets **statementFiled**.
10. **The Line You Underline** — *Write the form's date on your statement's first line: 'As of the night scored, the following was also true'* Sets **formDated**.
11. **The Study Comes Back** — *File a one-page progress summary before the review — housing application, shifts, the repaired boiler, the filed appeal* Cash −$5; Sets **reviewFiled**.
12. **The School's Sentence** — *Ask for a copy for both files and thank her in writing* Cash −$5; Sets **schoolLetter**.
13. **Housing, With a Date On It** — *Attach the waitlist letter to your progress summary and hand a copy to every party at the review* Sets **housingLetter**.
14. **The Schedule, Signed** — *File the signed schedule with the progress summary before the review* Sets **schedulePaper**.
15. **The Review** — *Ask, through your lawyer, for a step-down: expanded time at home now, return when the unit opens, the plan in writing* This choice is flag-gated: it is only available with **recordsRequested** + **appealFiled** + **reviewFiled**.

Supporting choices along the same walk — every "paper version" choice (dated, copied, filed), every written request, and every dated letter — add the documentation the packet is later assembled from. The full walked path is printed in the verification note.

## (3) Why this wins — the law as it is supposed to work

- **Two files, two clocks.** The indicated report runs on the CPSL appeal clock — a written appeal within 90 days of notification (23 Pa.C.S. § 6341(a)(2)), here March 2, 2026 → May 31, 2026. The dependency case runs on studies, services, and reviews with no single date. The strategy is sequencing: the appeal letter goes out in week two, before the case work can eat the calendar.
- **The record request is the mirror.** Agency records are released on request (55 Pa. Code § 3130.44(d)), with other people's information redacted by design (55 Pa. Code § 3130.44(f)). The packet reveals the six-word version of the parent's worst night in time for her own page to join the file in both tracks.
- **Counsel is machinery, not luxury** (42 Pa.C.S. § 6337): twenty clinic minutes produce the two-column plan — APPEAL and CASE — that the whole route follows.
- **Kinship stability is evidence, not an ending.** The approved study and stable placement support the step-down; the filed progress summary and dated housing letter are what convert stability into a plan the court can order.

## (4) The traps

1. **Holding the appeal letter "until you know more" at "One Letter, Two Copies", then waiting again at "The Letter in the Drawer"** — the 90-day window closes and the route ends at **The Quiet Registry** — the children home, the word permanent. No hearing on the case side can reopen it.
2. **Letting the caseworker "note" the boiler explanation instead of attaching the repair log and invoice** — the file keeps a six-word summary — 'Mother states housing issue' — for both the reviewer and the court to read.
3. **Skipping the record request** — the parent never sees the file's version of her, and the winning choice at *The Review* is flag-gated shut: it requires **recordsRequested**.
4. **Explaining in person instead of filing the progress summary** — minutes of testimony against a file the court read beforehand; the route lands at **The Plan Continues**, a partial win.

## (5) What no strategy controls

The waitlist, the study queue, the appeal reviewer's reading, and the judge. The route controls the order of the paper and the dates on it — which, in a two-file case, turns out to be most of what was ever controllable.

---
*Verification: this route was walked programmatically against `scenario-127.json` — each named choice was followed from the start node in order; every flag-gated choice's requirements were satisfied by flags set earlier on the walk; the walk terminates at the ending node titled "Ending — Home by Friday" after visiting 17 nodes, with $120 of the $160 starting cash remaining. Walked path: Two Envelopes → The Deadline in the Second Letter → Garazi's Kitchen → Visits at Garazi's Table → The Lawyer's Twenty Minutes → One Letter, Two Copies → The Boiler, On Paper → The Acknowledgment → Asking for the File → What the Mirror Shows → The Line You Underline → The Study Comes Back → The School's Sentence → Housing, With a Date On It → The Schedule, Signed → The Review → Ending — Home by Friday.*
