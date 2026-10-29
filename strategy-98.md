# Strategy Guide — Scenario 98: "The Interpreter Who Wasn't Booked"

*Game documentation for a fictional simulation in "The First 90 Days" (Tactic Watch). The family, the case, and every choice below are fictional. This guide is general information about how the scenario is built — it is not legal advice for any real case.*

## (1) The win

**Best ending: "Read It With Her."**

State it honestly: this is a **full** win, and it is the best this scenario offers. Nora stays home throughout — she is never removed on this route — under a revised safety plan that Ramona has actually read, line by line, through an interpreter, with counsel. The "uncooperative" entries are corrected on the record, and interpreter bookings for every meeting are written into the plan itself as the agency's terms, not left as the mother's repeated request. The file does not close and the plan does not vanish; what the route wins is a case conducted in a language its subject can use, on paper she has read.

## (2) The route

Verified by walking the scenario graph from the start node (see the verification note at the end). Key decision points, in order — node title, winning choice, and what it changes:

1. **The Clinic Visit** — *That evening, write a dated note of what happened at the clinic — who was there, what was written, what she could not follow.* Sets **datedNote**; hidden item: the mother's dated account, written the same evening. It becomes the correction's first exhibit.
2. **A Knock, a Notebook** — *Write: 'Meetings about Nora need an ASL interpreter. Please book one. I will keep these pages.'* Sets **interpreterRequested**; hidden item: interpreter requested in writing at the first contact, notebook pages kept. From here on, the file can never honestly say she never asked.
3. **The Meeting With No Interpreter** — *Hand over the written request again, keep a copy, and write the date and 'no interpreter present' at the top of her notes.* Cash −4. Sets **meetingsDocumented**; hidden item: the un-interpreted meeting documented in writing, with a copy kept.
4. **A Plan, Pushed Across the Table** — *Write on the plan itself: 'I will review this with my attorney before I sign,' and take the copy home unsigned.* Sets **planWithCounsel** — and, just as important, does **not** set **signedUnread**. The review's winning choice is closed to any route that signed. Review first, signature after: a sequence, not a refusal.
5. **Ms. Iwu, By Video** — *Go through every line, and have Ms. Iwu send a written plain-language summary of what the plan actually requires.* Sets **planUnderstood** — one of the three flags the winning choice is gated on. This is also where the plan's Tuesday phone-call check-in — a term a Deaf mother could never perform — is caught in writing, before it can fail.
6. **Back to the Clinic, With Paper** — *Ask the clinic to note, in writing, how the next visit will communicate — before the visit, not at it.* Cash −7. Sets **clinicNote**.
7. **The Second Meeting** — *Write it in the notebook, in front of everyone: 'Nora is five. She will not interpret. I am asking again, in writing, for an interpreter.'* Sets **childNotInterpreter** and re-sets **meetingsDocumented**; hidden item: the refusal and the renewed request, documented. A hearing child is never used as interpreter on this route — that documented failure mode is refused in writing, in the room.
8. **What Ms. Iwu Sends** — *Send the written record request this week, through Ms. Iwu, and keep the dated copy.* Cash −5. Sets **recordsRequested**. The highest-leverage move in the scenario: it is how Ramona sees the scored form's "uncooperative" entries in March, while a correction can still answer them.
9. **Nora's Teacher Writes It Down** — *Ask the teacher for a clean copy for the case folder, and file it with the notebooks.* Sets **schoolNote**. A third party's dated account of the household, filed where the review can find it.
10. **The Correction Attaches the Notebook** — *File the correction with the notebook pages and both interpreter requests attached.* Cash −6. Sets **correctionFiled**. The correction does not argue about fairness; it attaches the meetings as they happened to the meetings as they were scored.
11. **The Plan, Again — Slower** — *Ask, in writing, for the revised plan in plain language — with the interpreter bookings for every meeting written into the plan itself.* Sets **bookingsInPlan**. Not an interpreter promised — an interpreter booked, as a term, so a missed booking is a missed term of the agency's.
12. **Rehearsing With Ms. Iwu** — *Rehearse from the folder: every answer a date, every date a page.* Cash −8. Sets **reviewReady**.
13. **The Review** — *Hand up the folder — the correction, the notebook pages, the written requests — and ask for the revised plan with interpreter bookings written into it.* This choice is flag-gated: it is only available with **recordsRequested** + **correctionFiled** + **planUnderstood** all set, and with **signedUnread** not set. It leads to **Read It With Her**.

Supporting route choice: walking the whole home routine in writing at **The Home Visit, In Writing** — the hidden home items (routines, visual schedule, emergency contact) are recorded as the mother explained them, not as a short visit's impressions.

## (3) Why this wins — the law as it is supposed to work

Only principles from the scenario's verified set are stated here — and this scenario's honesty about its set matters more than most:

- **Counsel is part of the machinery** (42 Pa.C.S. § 6337). The plan is read with Ms. Iwu, through an interpreter, *before* any signature — and that single sequence change is what converts the plan from a trap (an unperformable phone-call check-in, breached before it was understood) into terms Ramona can actually keep.
- **Agency records are obtainable on request** — 55 Pa. Code § 3130.44(d) ("shall be released upon request"). Step 8 is that right exercised in writing. The packet arrives partly redacted, and 55 Pa. Code § 3130.44(f) is the provision that limits what redactions may protect — but the cooperation items and their dates are there, and dates are where this case lives: both "uncooperative" entries sit beside meetings with no interpreter booked, preceded by written requests the form never recorded.
- **A safety plan is paper with consequences.** Nothing in the verified set is cited for an interpreter entitlement in this scenario, because the route does not need one: every beat is a documentation move — ask in writing, keep the pages, document the un-interpreted meeting, correct the record with exhibits. The scored form rated what it was built to rate; the correction supplies what it was not built to record.
- **What was deliberately not relied on:** specific disability-rights protections exist in this area, but they sit outside this scenario's verified set and were not relied on — not in the game's prose, not in its debriefs, and not in this route. The paper route wins without them. A real parent in Ramona's position should put the question to a lawyer, who can use every protection the law actually provides; the game's discipline is to teach only the moves it has verified.

## (4) The traps

1. **Signing the plan at the table** at "A Plan, Pushed Across the Table," so the meeting can end. Cost: sets **signedUnread**, and the review's winning choice requires that flag *not* be set — the best ending closes in February, with a pen. The plan's Tuesday phone-call check-in stays unread until it is missed, and a missed term in a signed plan is the removal ending's whole engine.
2. **Asking Ms. Pemberton to just say what the file says** at "What Ms. Iwu Sends." Cost: no **recordsRequested**, and no sight of the "uncooperative" entries while they can still be answered. A summary of a form is not the form.
3. **Sending a short letter saying the rating is unfair** at "The Correction Attaches the Notebook." Cost: no **correctionFiled**. Unfair, without exhibits, reads in a file like a disagreement about adjectives; the notebook pages are the argument, and unattached they stay in a drawer.
4. **Covering only the main points of the plan with Ms. Iwu** at "Ms. Iwu, By Video." Cost: no **planUnderstood** — the winning choice closes — and the unperformable check-in line survives into a signed plan. Plans fail in their standard lines.
5. **Letting Nora help interpret, just this once** at "The Second Meeting." Cost: not a flag but a record — the file will note that the meeting proceeded through the child, and it will not record whose idea it was. A five-year-old becomes the bridge in her own mother's case, and the form scores the meeting as communication achieved.

The ungated alternative at "The Review" — explaining, truly and well, how hard she tried to cooperate — leads to "The Order at the End of the Review" and then to "Signed, Not Read": placement, with the shelter care safeguards (a hearing within 72 hours — 42 Pa.C.S. § 6332; 23 Pa.C.S. § 6315(d) — and counsel under § 6337) operating, but on February's unanswered file.

## (5) What no strategy controls

Whether an interpreter is actually booked, and whether the one who comes is skilled. Whether a reviewer is willing to re-read a scored item next to its evidence. A lost notebook, a flooded drawer, a lawyer's full caseload, a teacher who does not write notes. The route controls only the documentation: that every request was written and dated, every un-interpreted meeting was recorded as one, no child was used as a bridge, and no signature was given before understanding was possible. Outcomes in this system turn on workers, judges, resources, and luck as much as on any parent's choices — the strategy's claim is narrower: when the review opened the file, the meetings were in it twice, and the second telling was hers.

---
*Verification: this route was walked programmatically against `scenario-98.json` — each named choice was followed from the start node in order; every intermediate node and choice exists; every flag-gated choice's requirements were satisfied by flags set earlier on the walk; the walk terminates at the ending node titled "Read It With Her" after visiting 16 nodes, with $130 of the $160 starting cash remaining.*
