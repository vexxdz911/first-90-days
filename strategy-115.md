# Strategy Guide — Scenario 115: "Three Letters, Three Addresses"

*Game documentation for a fictional simulation in "The First 90 Days" (Tactic Watch). The family, the case, and every choice below are fictional. This guide is general information about how the scenario is built — it is not legal advice for any real case.*

## (1) The win

**Best ending: "Ending — Corrected on the Record, Restored in Part."**

State it honestly: this ending is labeled **PARTIAL**, and the label is the lesson. Two of the three systems are restored on their own trails' paper — the childcare arrangement is re-looked-at and restored, the benefits case is re-opened — and the dependency file's "family failed to attend" notation is **corrected on the record**: the invitation is entered as mailed to an address Shana never lived at, after her correct address update was already on file, and the briefing step is re-set for her to take. The third thread is restored only in position: her housing standing is put back to **where she would have stood** had the invitation reached her. **The lost months are not given back.** No ending in this scenario returns them, because corrections restore records and positions, not time. Anyone selling you one is selling you a different game.

## (2) The route

Verified by walking the scenario graph from the start node (see the verification note at the end). Key decision points, in order — node title, winning choice, and what it changes:

1. **The Update Form** — *Ask at the desk for a copy of the form you just signed.* Cash −2. Sets **updateCopy**. The form itself — her correct new address, in her handwriting, dated Thursday, February 5, 2026, **before all three mailings** — is the strongest page in the case, and this is its cheapest moment.
2. **A Trail for the First Letter** — the childcare closure letter went to the old apartment. *Write to the childcare office — the closure letter's own process, your current address at the top.* Cash −4. Sets **childcareTrail**. Trail one exists in writing, following the process stated on the letter's own face.
3. **A Trail for the Second Letter** — the benefits closure notice went to the shelter she had left. *Write to the benefits office — the notice's own process, current address at the top.* Cash −4. Sets **benefitsTrail**. Three systems, three files: a fix in one has never repaired another, so each gets its own trail.
4. **An Address You Never Lived At** — the briefing invitation went to a transposed-number address. There is no office trail for this thread from outside the file; its error is visible only where the agency's own pages sit side by side.
5. **Ask for the File** — *Put the request in writing — update form, mailing record, closure and briefing entries — and keep a copy.* Cash −6. Sets **recordsRequested** (required on every winning route in this series).
6. **The File, Against Itself** — *Copy the two pages into your packet, in that order — form first, mailing record second.* Sets **updateFormFound**. The packet received Wednesday, March 11, 2026 contains both: the correctly written form, dated before all three mailings, and the mailing record showing all three letters sent elsewhere. Order is the argument.
7. **Assemble the Packet, Raise It Aloud, or Wait** — *Assemble and file the whole packet with counsel — pattern page, forms, mailing record, trail replies.* Cash −8. Sets **packetFiled**. This choice is flag-gated: **recordsRequested** + **updateFormFound**. Filed in pieces, the pattern is three anecdotes; filed whole, it is one file correcting itself.
8. **The Hearing** (Tuesday, April 21, 2026) — *Put the agency's own pages before the room — the update form dated before all three mailings, beside the mailing record.* Flag-gated: **recordsRequested** + **packetFiled**. It leads to **Ending — Corrected on the Record, Restored in Part**.

Supporting route choices: the tenancy page and utility letter filed early at **The Tenancy Page** (proof of the rooms, assembled before it is needed), the three-row untangling page at **Which Letter Went Where** (addresses exact, including the wrong digits — they are the evidence), the address-proof assembly at **Proof of the Rooms**, and counsel's deliberately honest framing at **What a Correction Can and Cannot Do**, which is where the guide's PARTIAL label is set, in the fiction, before the hearing sets it in fact.

## (3) Why this wins — the law as it is supposed to work

Only principles from the scenario's verified set are stated here, and one hard caution governs the rest:

- **The agency's record is obtainable on request** — 55 Pa. Code § 3130.44(d) ("shall be released upon request"). Steps 5–6 are that right exercised in writing, and they are the whole ballgame for the third thread: the transposed digits exist nowhere outside the agency's file, so only the file can refute the file's notation.
- **Counsel** (42 Pa.C.S. § 6337) assembles and files the pattern as one packet and asks the room that owns the notation to correct it from its own pages — the form it accepted and the mailing record it kept.
- **Hard caution — no program's rules are stated as law anywhere in this scenario.** The childcare, benefits, and housing systems each have their own rulebooks, and this guide asserts none of them: no amounts, no eligibility rules, no voucher or payee rules. In the fiction, each letter states its own process on its face; the trails follow those faces; what each office restored was restored in its own process, on its own paper. The story turns on addresses, lags, postings, and paper — never on a program rule.

## (4) The traps

1. **Carrying a trail by phone** (no **childcareTrail** / no **benefitsTrail**). The explanation is accurate, the office is reasonable, and the thread enters the hearing with no dated page behind it. At best the route degrades toward **Ending — One Thread, Pulled Straight**, where the room corrects only what the agency's own two pages prove in a single glance.
2. **Never requesting the record** (no **recordsRequested**, no **updateFormFound**). The packet choice at the assembly node never appears — it is gated on the file's own pages. What remains is the oral raise (**Ending — Restored in Part, the Notation Standing**: the pattern believed personally, the sentence intact) or waiting (**Ending — Failure to Respond, As Written**).
3. **Raising the three letters orally** (sets **oralRaised** instead of filing). A transcript of counsel's sentences is not the update form and is not the mailing record; rooms correct notations from documents in the file, not from descriptions of documents in a drawer.
4. **Trusting the other offices' fixes to travel.** Each office restores in its own file. The dependency file keeps its sentence until somebody files the pages that answer it, in it. That subscription does not exist, in any system, anywhere in this scenario.

## (5) What no strategy controls

Whether a clerk propagates an update form into three other systems; whether two digits survive proofreading at reading speed; each office's pace in its own process; the housing queue's indifference to corrected records — the position is restored, the months are not, and no route in this scenario changes that arithmetic; and the room's reading of even a perfect packet. The route controls only this: every error was answered in writing, in its own system's own stated process, and the pattern was filed where the notation lived. Outcomes in this system turn on workers, offices, judges, and luck as much as on any parent's choices — and never on a parent's worth. Shana did the one affirmative act this tangle ever asked of her correctly and on time. The scenario's whole argument is that the file should have to say so.

---
*Verification: this route was walked programmatically against `scenario-115.json` — each named choice was followed from the start node in order; every intermediate node and choice exists; every flag-gated choice's requirements (recordsRequested + updateFormFound at the assembly; recordsRequested + packetFiled at the hearing) were satisfied by flags set earlier on the walk; the walk terminates at the ending node titled "Ending — Corrected on the Record, Restored in Part" after visiting 31 nodes, with $130 of the $170 starting cash remaining. Walked path: start -> update_form -> new_address -> landlord_note -> childcare_news -> childcare_reply -> benefits_news -> benefits_reply -> housing_news -> housing_reply -> three_threads -> records_learn -> records_fork -> file_arrives -> untangle -> mail_log_detail -> trail_childcare -> trail_benefits -> trail_housing -> assembly -> filed_scene -> ordinary_weeks -> twins_visit_mid -> address_proof -> summary_arrives -> counsel_second -> review_notice -> review_prep -> eve115 -> review -> end_restored_partial.*
