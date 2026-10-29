# Strategy Guide — Scenario 128: "Two Doors, One Hallway"

*Game documentation for a fictional simulation in "The First 90 Days" (Tactic Watch). The family, the case, and every choice below are fictional. This guide is general information about how the scenario is built — it is not legal advice for any real case.*

## (1) The win

**Best ending: "Ending — Both Doors."**

This is a **full** win: the report amended to unfounded and Anouk home on the court's own plan. It is a Hard scenario because both victories run through the same small set of paper moves — an early appeal, an evidence demand the statute entitles the appellant to make, a record request, and one chronology carried deliberately through both doors.

## (2) The route

Verified by walking the scenario graph from the start node (see the verification note at the end). Key decision points, in order — node title, winning choice, and what it changes:

1. **The Notice and the Nursery** — *Put both tracks on one page: APPEAL by July 5; CASE reviews monthly* Sets **calendarSet**.
2. **Reading for the Date That Isn't There** — *Write 'July 5' on the envelope itself, in ink* Sets **deadlineInked**.
3. **Maite's Refrigerator** — *Align your folder to hers — same dates, same order, copies both ways* Sets **foldersAligned**.
4. **Ms. Zabala Draws Two Doors** — *File the appeal this week, stamped copy in the folder* Cash −$10; Sets **appealFiled**.
5. **Maite's Porch** — *Ask the kinship worker, in writing, what the study still needs and by when* Cash −$5; Sets **studyList**.
6. **The Chin, Healing** — *Keep the dated photos with the medical records in both folders* Sets **photosKept**.
7. **The Evidence You Are Owed** — *Build the appeal around the addendum and the stitch record — the agency's own paper* Cash −$5; Sets **evidenceReceived**.
8. **The Case File, Requested** — *Sign the written request and file the stamped copy* Cash −$5; Sets **recordsRequested**.
9. **Indexing the Packet** — *File the index with the packet in both tracks* Sets **indexFiled**.
10. **What the Case Record Shows** — *Write a one-page chronology — referral dates, visit dates, certificates — and file it in both tracks* Cash −$5; Sets **chronologyFiled**.
11. **The Nine Arranged-Later Days** — *Write the nine days into the chronology with the staffing note cited by date* Sets **gapOwned**.
12. **The Scheduling Order** — *Prepare the review like it's the appeal's opening statement — chronology, certificates, the study checklist, all filed a week early* Sets **reviewFiled**.
13. **The Certificate** — *File the certificate and the instructor's letter in both tracks the same week* Cash −$5; Sets **certificateFiled**.
14. **The Night Course** — *File the attendance record and the employer's letter before the July review* Cash −$5; Sets **employerLetter**.
15. **Your Sister's Statement** — *File her statement in the appeal packet and the case record* Cash −$5; Sets **sisterStatement**.
16. **The Pediatrician's Paragraph** — *Request a copy for the appeal packet the same day* Sets **pedsLetter**.
17. **The Redaction Question** — *Note the redacted page by number in the chronology and move on* Sets **redactionNoted**.
18. **The Job That Waits on the Registry** — *File the posting and your employer's hold-letter in the packet* Sets **stakesFiled**.
19. **The July Review** — *Propose the dated finish: study completion, two more class sessions, step-down to overnights at Maite's, return on the September review* This choice is flag-gated: it is only available with **recordsRequested** + **appealFiled** + **chronologyFiled**.
20. **The Bureau Hearing** — *Close on the addendum and the burden: their paper, their standard, their burden* This choice is flag-gated: it is only available with **evidenceReceived**.

Supporting choices along the same walk — every "paper version" choice (dated, copied, filed), every written request, and every dated letter — add the documentation the packet is later assembled from. The full walked path is printed in the verification note.

## (3) Why this wins — the law as it is supposed to work

- **The appeal clock and the burden, together.** Written appeal within 90 days of notification (23 Pa.C.S. § 6341(a)(2)); at the hearing, the agency bears the burden of proving by substantial evidence that the report should remain indicated (23 Pa.C.S. § 6341(c.2)(5)). The route files early precisely so the hearing can be about the burden, not about the calendar.
- **The evidence you are owed.** The appellant is entitled to all relevant investigation evidence, including the potentially exculpatory, within ten days of the scheduling order (23 Pa.C.S. § 6341(c.2)(4)). The triage addendum — the case's decisive page — arrives through this door and no other.
- **The decision has a clock too:** entered, filed, and served within 45 days of the hearing's conclusion (23 Pa.C.S. § 6341(c.3)); the win lands on day 36 of that window. If the appeal had been upheld, § 6341(g)'s 15-day reconsideration and 30-day Commonwealth Court clocks would run from the order's mailing date — the losing ending's debrief teaches them.
- **The case track runs on the same fuel:** the § 3130.44(d) record request (redactions under (f) are design, not withholding), counsel under 42 Pa.C.S. § 6337, and a chronology filed in both tracks because paper does not walk hallways by itself.

## (4) The traps

1. **Polishing the appeal letter past the window at "A Month of Reviews"** — Day 92 is day never: the route ends at **Day Ninety-Two** with the registry door closed for good.
2. **Resting on your own account instead of the evidence packet at "The Evidence You Are Owed"** — your testimony must be believed; the nurse's addendum only has to be read. The closing built on fairness instead of the burden ends at **Upheld, and Home Anyway**.
3. **Skipping the case record request** — the July review is argued from memory, the referral gap stays in the passive voice, and the gated choice — requiring **recordsRequested** + **appealFiled** + **chronologyFiled** — stays shut; the route lands on the step-down.
4. **Treating the July review as a formality** — the review is the appeal's opening statement; the hallway hears everything twice.

## (5) What no strategy controls

The hearing officer's weighing of two medical sentences written on the same night, the agency's litigation posture, and the individual judge. The route controls whether the decisive page is in the room and whose burden it is — in a paper case, that is most of the game.

---
*Verification: this route was walked programmatically against `scenario-128.json` — each named choice was followed from the start node in order; every flag-gated choice's requirements were satisfied by flags set earlier on the walk; the walk terminates at the ending node titled "Ending — Both Doors" after visiting 22 nodes, with $135 of the $180 starting cash remaining. Walked path: The Notice and the Nursery → Reading for the Date That Isn't There → Maite's Refrigerator → Ms. Zabala Draws Two Doors → Maite's Porch → The Chin, Healing → The Evidence You Are Owed → The Case File, Requested → Indexing the Packet → What the Case Record Shows → The Nine Arranged-Later Days → The Scheduling Order → The Certificate → The Night Course → Your Sister's Statement → The Pediatrician's Paragraph → The Redaction Question → The Job That Waits on the Registry → The July Review → The Night Before Door One → The Bureau Hearing → Ending — Both Doors.*
