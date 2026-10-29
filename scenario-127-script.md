# THE FIRST 90 DAYS — Scenario 127: “The Whole Table, Gently”

*Human-readable script. This document and `scenario-127.json` are generated from a single source and match node-for-node: same IDs, same order, same choices, same effects.*

**The family is fictional — a composite. No real person's story appears here.**

**Content note:** This scenario depicts a child-welfare investigation, a temporary kinship placement, and an indicated-report appeal. There is no graphic content. Players may skip any scene or use the quick exit at any time.

**How to read effects:** `cash −40` changes the player's cash. `FLAG: name` sets a flag the engine tracks. `HIDDEN + item` means the case file quietly records that item at this choice — the player does not see it when it happens. `REQUIRES FLAG: name` means the choice is only available if that flag was set earlier; `REQUIRES NO FLAG: name` means it is only available if that flag was never set. `NOTE:` is text shown to the player right after choosing.

Start date: Monday, March 2, 2026. Day offsets are days since the scenario's start date (the children's placement date).

## [start] Two Envelopes
*Day 0 — Monday, March 2, 2026 (dayOffset 0)*

Your name is Tomasa. You clean rooms at a motel off the highway, and you are raising Zayd, seven, and Leire, four, in a one-bedroom above a laundromat. In February the building's boiler failed twice, and on the coldest night you did what the neighbor downstairs suggested: you all slept at her place, three floors of stairs between your children and any exit the fire code would recognize.

Nobody was hurt. But a report was made, and this morning there are two envelopes. The first says Zayd and Leire will stay with your sister Garazi while the agency looks at your housing. The second says a report about that night has been marked indicated — and that word, a caseworker explains, can follow you onto every childcare clearance you will ever need, including the motel's sister property where you were about to pick up weekend shifts in the playroom.

Two files. Two clocks. This story is about working both of them, in the right order, on paper.

**Choices:**
- Sit down with the flyer your sister printed and read both letters all the way through → **read_both**
  - NOTE (shown after choosing): The second letter is the one with a deadline in it. Most people read it last.
- Call the caseworker and ask her to just explain it quickly → **read_both**
  - NOTE (shown after choosing): She explains the visit schedule. The deadline in the second letter stays unread a little longer.

## [read_both] The Deadline in the Second Letter
*Day 2 — Wednesday, March 4, 2026 (dayOffset 2)*

The second letter holds the number that matters: a person named as a perpetrator in an indicated report may appeal and ask for the report to be amended or expunged — in writing — within 90 days of being notified (23 Pa.C.S. § 6341(a)(2)). You were notified on Monday, March 2, 2026. Ninety days later is Sunday, May 31, 2026.

The first letter holds no deadline at all, which is its own kind of trap: Garazi's home study, your repair plan with the landlord, and the review hearing will all move at the speed of whoever writes things down.

**Choices:**
- Write both dates on the kitchen calendar and circle May 31 → **calendar**  _(FLAG: calendarSet ; HIDDEN + Appeal deadline calendared from the notice date)_
  - NOTE (shown after choosing): Two clocks, one calendar, both visible from the refrigerator.
- Keep the dates in your head — you have a good memory → **calendar**
  - NOTE (shown after choosing): Memory is a fine thing. It is not a filing system.

## [calendar] Garazi's Kitchen
*Day 5 — Saturday, March 7, 2026 (dayOffset 5)*

Garazi has a spare room, a fold-out couch, and a caseworker of her own now — the kinship worker, who needs clearances, a home visit, and a form signed by everyone over eighteen in the house. Zayd has already claimed the top bunk of a bed that does not exist yet.

The kinship worker says the study usually takes a few weeks. She does not say what happens to the paperwork if nobody asks about it. Garazi looks at you over the children's heads: ask, she mouths.

**Choices:**
- Ask what the study needs, write the list down, and text it to yourself before you leave → **visits127**  _(cash −5 ; FLAG: studyList ; HIDDEN + Kinship study requirements obtained in writing)_
  - NOTE (shown after choosing): A list you can check off beats a timeline you were told.
- Trust the process — she said a few weeks → **visits127**
  - NOTE (shown after choosing): Weeks pass at different speeds depending on whether anyone is counting.

## [visits127] Visits at Garazi's Table
*Day 8 — Tuesday, March 10, 2026 (dayOffset 8)*

Visits happen at Garazi's kitchen table, twice a week, with the refrigerator sign-in sheet Garazi invented on day one: date, time in, time out, one line about the day. Zayd signs his name in letters that improve weekly, which the sheet records whether anyone meant it to or not.

The caseworker calls this 'supervised by kin.' Garazi calls it dinner. Both descriptions are accurate; only one of them is in the file, and it is the one with the sign-in sheet attached.

**Choices:**
- Keep the sheet religiously and copy it monthly into your folder → **study_list**  _(FLAG: visitLog ; HIDDEN + Kinship visit sign-in sheet kept and copied)_
  - NOTE (shown after choosing): A small sheet, doing a large job.
- Enjoy the visits and skip the clerical part → **study_list**
  - NOTE (shown after choosing): Dinner is dinner. The file, however, eats paper or it eats nothing.

## [study_list] The Lawyer's Twenty Minutes
*Day 9 — Wednesday, March 11, 2026 (dayOffset 9)*

The legal-aid clinic gives you twenty minutes and a lawyer, Ms. Mendieta, who draws two columns on a legal pad: APPEAL and CASE. Under APPEAL she writes: file it early, in writing, keep the stamp. Under CASE she writes: housing first, everything dated.

You have the right to counsel in the dependency case, and to appointed counsel if you cannot afford one (42 Pa.C.S. § 6337). The appeal, she says, is simpler than people fear and stricter than people hope: the paper has to exist, and it has to be on time.

**Choices:**
- Ask her to help you draft the appeal letter today, while you are sitting here → **draft_appeal**  _(FLAG: lawyerMet ; HIDDEN + Parent consulted counsel about both tracks)_
  - NOTE (shown after choosing): Twenty minutes, used like an hour.
- Take her card and plan to draft the letter at home this weekend → **draft_appeal**
  - NOTE (shown after choosing): The card goes in the folder. The weekend, as weekends do, fills up.

## [draft_appeal] One Letter, Two Copies
*Day 12 — Saturday, March 14, 2026 (dayOffset 12)*

The appeal letter is half a page: your name, the report number, the words amend or expunge, your signature, today's date. Ms. Mendieta's advice is mechanical: mail one copy so it leaves a record, keep one copy, and photograph the stamped receipt.

It feels too small to matter. She smiles the smile of a woman who has watched small letters move large files.

**Choices:**
- Mail the appeal this week and keep the stamped copy in the folder → **appeal_sent**  _(cash −10 ; FLAG: appealFiled ; HIDDEN + Indicated-report appeal filed in writing within the 90-day window)_
  - NOTE (shown after choosing): Filed on day 12 of 90. The clock that scared you is now the clock that protects you.
- Hold the letter until you know more about what the agency has → **appeal_risk**
  - NOTE (shown after choosing): Knowing more is a plan. It is also how day 12 becomes day 60.

## [appeal_risk] The Letter in the Drawer
*Day 40 — Saturday, April 11, 2026 (dayOffset 40)*

The letter is still in the drawer, under the good scissors. The housing hunt ate the spring. The appeal window did not eat anything; it just quietly counted, the way clocks do, indifferent rather than cruel.

There is still time — that is the dangerous sentence. There is less of it than the sentence suggests.

**Choices:**
- Mail it today, stamped copy in the folder, no more drawer → **appeal_sent**  _(cash −10 ; FLAG: appealFiled ; HIDDEN + Indicated-report appeal filed in writing within the 90-day window)_
  - NOTE (shown after choosing): Day 40 of 90. Late is a direction, not a destination — this once.
- Wait until the review hearing settles the case side first → **end_registry**
  - NOTE (shown after choosing): The hearing settles the case. It was never going to settle the registry.

## [appeal_sent] The Boiler, On Paper
*Day 44 — Wednesday, April 15, 2026 (dayOffset 44)*

The landlord's repair log exists — if you ask for it in writing. The boiler company's invoice exists too, dated the week of the cold night, with the words emergency replacement on it. Paper like this does not argue. It simply sits in a file being true.

Your caseworker, Ms. Agirre, says she can note your explanation in the file. Noting is good. Attached is better.

**Choices:**
- Request the repair log and invoice in writing and attach copies to both files → **appeal_ack**  _(cash −5 ; FLAG: repairPaper ; HIDDEN + Landlord repair log and boiler invoice obtained and filed)_
  - NOTE (shown after choosing): The coldest night of February, now with documentation.
- Let the caseworker note your explanation — that should be enough → **appeal_ack**
  - NOTE (shown after choosing): Your explanation, in her words, in her summary. Summaries summarize.

## [appeal_ack] The Acknowledgment
*Day 48 — Sunday, April 19, 2026 (dayOffset 48)*

A thin letter comes back: your appeal has been received and docketed. It decides nothing. It proves everything about timing — the date on it is inside the window, and the window was the whole battle of the appeal's first phase.

Ms. Mendieta makes you file it on top of the appeal copy. 'First page of the appeal file,' she says. 'Proof before argument. Always in that order.'

**Choices:**
- File the acknowledgment with the stamped copy and note the docket number on the calendar → **records_beat**  _(FLAG: appealDocketed ; HIDDEN + Appeal acknowledgment filed; docket number calendared)_
  - NOTE (shown after choosing): The appeal is now a case with a number, not a hope with a stamp.
- Put it in the folder and move on to the housing hunt → **records_beat**
  - NOTE (shown after choosing): In the folder is good. On top, in order, is better — but the folder forgives.

## [records_beat] Asking for the File
*Day 52 — Thursday, April 23, 2026 (dayOffset 52)*

A parent advocate at the clinic mentions the move nobody had mentioned: you may request the agency's record of your own case, and the material shall be released upon request (55 Pa. Code § 3130.44(d)). Some pages come back with black bars over other people's names — that is the rule, not a trick (55 Pa. Code § 3130.44(f)).

What arrives will show you what the appeal reviewer will see, and what the review hearing will read. It is the only mirror the system hands you.

**Choices:**
- Sign the written record request and keep the stamped copy → **packet_back**  _(cash −5 ; FLAG: recordsRequested ; HIDDEN + Case record requested in writing under § 3130.44(d))_
  - NOTE (shown after choosing): The mirror is requested. It arrives the way mirrors do in this system: by mail, in an envelope too small for it.
- Skip it — you know what happened that night → **packet_back**
  - NOTE (shown after choosing): You know what happened. The file knows what was written. Those are different knowledges.

## [packet_back] What the Mirror Shows
*Day 58 — Wednesday, April 29, 2026 (dayOffset 58)*

The packet shows two things you did not expect. The investigator's note says the children were 'appropriately dressed for the cold' and the neighbor 'seemed credible.' And your own explanation — the boiler, the neighbor, the one night — is recorded in a single line: 'Mother states housing issue.'

Six words for the worst night of your winter. The appeal reviewer will read those six words unless the file gains the repair log, the invoice, and a page in your own hand.

**Choices:**
- Write a one-page statement in your own words and file it with the repair documents, in both files → **mirror_detail**  _(cash −5 ; FLAG: statementFiled ; HIDDEN + Parent's written statement and repair documents filed in both tracks)_
  - NOTE (shown after choosing): Your page, your words, both files. The six-word version is no longer the only version.
- The note about the children being dressed warmly is enough — leave the file as it is → **mirror_detail**
  - NOTE (shown after choosing): It is a good line. It is one line, in someone else's hand.

## [mirror_detail] The Line You Underline
*Day 62 — Sunday, May 3, 2026 (dayOffset 62)*

One more page of the packet deserves its own evening: the scored assessment form's summary — present in redacted form — rates 'housing stability' at the bottom of its scale, dated the week of the cold night. It does not mention the boiler, the repair order, or the new unit's waitlist, because on the day it was scored, none of that paper existed yet.

Forms are photographs. They show the day they were taken. The strategy of this whole case is to make sure later photographs get taken — with the repair log in the frame.

**Choices:**
- Write the form's date on your statement's first line: 'As of the night scored, the following was also true' → **statement_filed**  _(FLAG: formDated ; HIDDEN + Assessment summary dated and answered on the record)_
  - NOTE (shown after choosing): You cannot retake the photograph. You can caption it, with dates.
- Leave the form alone — arguing with a score looks defensive → **statement_filed**
  - NOTE (shown after choosing): Captioning is not arguing. But the statement still gets filed, and it carries most of the weight.

## [statement_filed] The Study Comes Back
*Day 66 — Thursday, May 7, 2026 (dayOffset 66)*

Garazi's study is approved. The bunk bed exists now; Zayd has claimed the top in writing, on the refrigerator, in crayon. The kinship worker notes the placement is stable and the children are doing well — the sentence every later reader will weigh.

Stability at Garazi's cuts both ways, and Ms. Mendieta warned you about the second edge: a comfortable placement can make a slow case feel finished. The review hearing is in three weeks. Comfortable is not the goal. Home is.

**Choices:**
- File a one-page progress summary before the review — housing application, shifts, the repaired boiler, the filed appeal → **school_note**  _(cash −5 ; FLAG: reviewFiled ; HIDDEN + Written progress summary filed before the review hearing)_
  - NOTE (shown after choosing): The judge will meet your spring as a document before she meets you as a person.
- Show up and explain it all in person at the hearing → **school_note**
  - NOTE (shown after choosing): You will get minutes. The document would have gotten there first and stayed longer.

## [school_note] The School's Sentence
*Day 71 — Tuesday, May 12, 2026 (dayOffset 71)*

Zayd's teacher, asked by the caseworker how he is doing, does something teachers are not required to do: she writes it down. One paragraph — attendance perfect, reading ahead, 'asks when the boiler at Mom's is fixed, in the tone of a boy expecting an answer.'

It is the single most believed document in most files: a professional with no stake, writing about an ordinary week.

**Choices:**
- Ask for a copy for both files and thank her in writing → **review_prep**  _(cash −5 ; FLAG: schoolLetter ; HIDDEN + Teacher's written statement filed in both tracks)_
  - NOTE (shown after choosing): Filed in both. Paper does not walk hallways by itself; you are the hallway.
- Let the caseworker forward it if she thinks of it → **review_prep**
  - NOTE (shown after choosing): She might. The file's memory for favors is shorter than its memory for documents.

## [review_prep] Housing, With a Date On It
*Day 78 — Tuesday, May 19, 2026 (dayOffset 78)*

The waitlist letter arrives: your application for the two-bedroom on Chestnut Street is approved pending a unit, estimated June. It is not a key. It is a dated letter on letterhead saying a key is coming, which in this system is the next best thing — the raw material of a compelling reason, written down.

The review is in one week. The appeal reviewer, in a separate building, is reading a file that now contains your page.

**Choices:**
- Attach the waitlist letter to your progress summary and hand a copy to every party at the review → **shift_swap**  _(FLAG: housingLetter ; HIDDEN + Dated housing waitlist letter filed and distributed)_
  - NOTE (shown after choosing): Everyone at the table reads the same June.
- Mention the letter if the judge asks about housing → **shift_swap**
  - NOTE (shown after choosing): Judges ask about what is in front of them. Give them something to ask about.

## [shift_swap] The Schedule, Signed
*Day 81 — Friday, May 22, 2026 (dayOffset 81)*

Your motel supervisor signs the schedule you will need when the children come home: no overnight shifts on school nights, weekends at the playroom rate — the weekend job the registry almost took. A signed schedule is the plan's least poetic and most cross-examined page.

Ms. Mendieta calls documents like this 'load-bearing paper': unglamorous, and the wall stands on them.

**Choices:**
- File the signed schedule with the progress summary before the review → **review_day**  _(FLAG: schedulePaper ; HIDDEN + Signed work schedule filed before the review)_
  - NOTE (shown after choosing): The plan now has a timetable, signed by someone other than you.
- Bring the schedule to the hearing in your bag → **review_day**
  - NOTE (shown after choosing): In your bag is a location. In the file is an argument.

## [review_day] The Review
*Day 85 — Tuesday, May 26, 2026 (dayOffset 85)*

The courtroom is smaller than its reputation. The judge has the file: the study, your summary, the waitlist letter, the repair log. The caseworker confirms the placement is stable, the visits are kept, the boiler is replaced, the appeal is pending in its own building.

The judge looks up. 'What is the plan,' she asks, 'and what is it waiting on?' Everything you filed was, in the end, an answer to that one question.

**Choices:**
- Ask, through your lawyer, for a step-down: expanded time at home now, return when the unit opens, the plan in writing → **end_home**  _(REQUIRES FLAG: recordsRequested ; REQUIRES FLAG: appealFiled ; REQUIRES FLAG: reviewFiled)_
  - NOTE (shown after choosing): The answer exists because the paper does.
- Ask for return today, on the strength of everything, without the step-down plan → **end_plan**
  - NOTE (shown after choosing): Almost is a real outcome in this system. It is just not the best one.
- Let the hearing happen to you and hope the file speaks → **end_plan**
  - NOTE (shown after choosing): Files speak in the order they are read. Yours needed a voice.

## [end_home] Ending — Home by Friday
*Day 96 — Saturday, June 6, 2026 (dayOffset 96)*

The order is two pages. Expanded time begins this week; the children return home when the Chestnut Street unit opens, with the kinship placement held open as the family's own safety net — Garazi, written into the order as what she always was: the plan, not the problem.

In June you carry Leire up the new stairs past a boiler room with a new boiler. In July, a second envelope arrives: the appeal has been granted, the indicated report amended to unfounded on the record the file now holds. Two files, two clocks — both answered with paper, in the right order.

Zayd's written claim on the top bunk is honored, by acclamation.

**Ending.**

**Debrief:**
- THE TWO CLOCKS — The appeal clock: notified Monday, March 2, 2026; the written appeal was due within 90 days — Sunday, May 31, 2026 (23 Pa.C.S. § 6341(a)(2)) — and on the winning route it was mailed on day 12. The case clock: no single date, but a sequence — study, services, review — that moved at the speed of dated paper. The whole capstone lesson is the order of operations: protect the deadline that cannot move first, then build the record the movable ones read.
- THE RECORD REQUEST — Agency records are released on request (55 Pa. Code § 3130.44(d)); the packet showed the parent her own case in the system's six-word summary, in time to file her own page. Redactions of other people's information are the regulation's design, not a withholding trick (55 Pa. Code § 3130.44(f)). Counsel in the dependency case is a right, including appointed counsel for those who cannot afford it (42 Pa.C.S. § 6337).
- WHAT NO STRATEGY CONTROLS — The waitlist, the study queue, the appeal reviewer's reading, and the judge. This ending is written as a win because the documents existed to be read; outcomes in real cases also turn on workers, judges, housing stock, and luck, and the same paper in a different county can meet a different day.

## [end_plan] Ending — The Plan Continues
*Day 96 — Saturday, June 6, 2026 (dayOffset 96)*

The children stay with Garazi a while longer. The plan continues: more time, another review, the unit still coming in June. Nobody in the courtroom thought you were failing; the file simply did not finish its sentence, and the court does not complete sentences for people.

The appeal, if you filed it, still runs in its building. The case will get another hearing. The folder is not closed — it is continued, which in this system is both a mercy and a cost, paid in weeks of a childhood.

**Ending.**

**Debrief:**
- A PARTIAL WIN, NAMED HONESTLY — The placement is safe, the kinship door stayed open, and the case continues toward return. What separated this ending from the best one was not effort or love; it was whether the record was requested (§ 3130.44(d)), the appeal was on time (§ 6341(a)(2)), and the progress existed as filed paper before the hearing rather than as testimony during it.
- WHAT NO STRATEGY CONTROLS — Housing supply, the study queue, and the individual judge. A continued case is not a lost one; it is a clock still running, and the same moves remain available at the next review — the file keeps what it is given, whenever it is given.

## [end_registry] Ending — The Quiet Registry
*Day 110 — Saturday, June 20, 2026 (dayOffset 110)*

The case side ended the way case sides often do: the children came home in the summer, the file closed, the folder went into a drawer. The registry side never got its letter. Ninety days from March 2 was May 31, and May 31 passed in the drawer, next to the good scissors.

The indicated report remains. It will surface on clearances — at the playroom job, at the school volunteer desk, at the nursing program you talked about in Garazi's kitchen. The case is over. The word remains, because one clock in this story could not be extended by anybody's good intentions.

**Ending.**

**Debrief:**
- THE CLOCK THAT COULD NOT MOVE — A perpetrator may appeal an indicated report in writing within 90 days of notification (23 Pa.C.S. § 6341(a)(2)). Notified Monday, March 2, 2026, the deadline was Sunday, May 31, 2026. Help on the case side — studies, services, hearings — does not file the appeal; only the letter does, and only on time.
- WHAT NO STRATEGY CONTROLS — Nothing in this ending turns on the worker, the judge, or the facts of the cold night. It turns on a date and a drawer. That is precisely why the appeal letter is taught as the first move, not the last: it is the one piece of paper in the whole system that cannot be written late.
