# THE FIRST 90 DAYS — Scenario 133: “The Three-Chair Table”

*Human-readable script. This document and `scenario-133.json` are generated from a single source and match node-for-node: same IDs, same order, same choices, same effects.*

**The family is fictional — a composite. No real person's story appears here.**

**Content note:** This scenario depicts a kinship placement with a grandmother, a parent's services, and an indicated-report appeal. There is no graphic content. Players may skip any scene or use the quick exit at any time.

**How to read effects:** `cash −40` changes the player's cash. `FLAG: name` sets a flag the engine tracks. `HIDDEN + item` means the case file quietly records that item at this choice — the player does not see it when it happens. `REQUIRES FLAG: name` means the choice is only available if that flag was set earlier; `REQUIRES NO FLAG: name` means it is only available if that flag was never set. `NOTE:` is text shown to the player right after choosing.

Start date: Monday, January 12, 2026. Day offsets are days since the scenario's start date (the child's foster-care entry date).

## [start] Three Chairs
*Day 0 — Monday, January 12, 2026 (dayOffset 0)*

Your name is Lorea. Your son Matteo, ten, entered care on Monday, January 12, 2026, after the night the police came to your building for someone else's emergency and found yours: Matteo home alone for forty minutes while you ran to the pharmacy in a snow emergency the file describes in the flat voice it uses for everything.

He is with his grandmother — your mother — Itziar, whose spare room he has claimed with a completeness only ten-year-olds achieve. And a third chair stands at the table: an indicated report naming you, notice dated Friday, January 30, 2026, with the 90-day window (23 Pa.C.S. § 6341(a)(2)) closing Thursday, April 30, 2026. Three chairs: the kinship study, your services, the appeal. Pull one and the others move. Ignore one and the table tips.

**Choices:**
- Draw the table: three chairs, three clocks, one page — before anything else moves → **table133**  _(FLAG: tableDrawn ; HIDDEN + Three-track table drawn with all clocks)_
  - NOTE (shown after choosing): The table, drawn. Now it can be worked.
- Take the files as they come — there's a limit to planning → **table133**
  - NOTE (shown after choosing): There is also a limit to memory, and April 30 is past it.

## [table133] Ms. Kortazar Assigns the Chairs
*Day 4 — Friday, January 16, 2026 (dayOffset 4)*

Your lawyer, Ms. Kortazar, assigns each chair its worker: the kinship worker owns Itziar's study; the caseworker owns your services; the Bureau owns the appeal — and you, she says, own the calendar that connects them. Counsel is your right (42 Pa.C.S. § 6337); coordination, in a three-chair case, is your job description.

'The study and the services are marathons,' she says. 'The appeal is a sprint with a wall at the end of it. Sprint first.'

**Choices:**
- Do the paper version: dated, copied, filed → **tb_a**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the case record)_
  - NOTE (shown after choosing): Another dated page joins the folder.
- Handle it with a conversation and move on → **tb_a**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [tb_a] Each Chair Gets a Date
*Day 5 — Saturday, January 17, 2026 (dayOffset 5)*

The study gets its milestones, the services their sessions, the appeal its April wall — and beneath them all, the line the table exists for: what happens if two chairs need you on the same day. The answer is written down too, because it will happen.

It happens in week three. The written answer handles it. The table begins to earn its wall space.

**Choices:**
- Carry the page to its file → **tb_b**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the record)_
  - NOTE (shown after choosing): Dated, copied, filed — the chain holds.
- Trust the conversation to carry it → **tb_b**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [tb_b] Itziar Sees the Table
*Day 6 — Sunday, January 18, 2026 (dayOffset 6)*

Itziar studies the page the way she studies recipes she intends to improve, and adds one line in her own hand: Matteo's school concert, in May, attendance non-negotiable, all chairs.

The table accepts the amendment. Cases that forget concerts lose more than concerts.

**Choices:**
- Carry the page to its file → **appeal133**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the record)_
  - NOTE (shown after choosing): Dated, copied, filed — the chain holds.
- Trust the conversation to carry it → **appeal133**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [appeal133] The Sprint, Run Early
*Day 8 — Tuesday, January 20, 2026 (dayOffset 8)*

The appeal letter goes out on day 8 of 90, stamped copy filed, deadline retired. It is the same half-page as always — name, report number, amend or expunge — and it feels, as always, too small for its consequences.

Itziar watches you mail it and says the thing grandmothers say in this library: 'Paper first. Feelings on schedule.' She has started a folder. Of course she has.

**Choices:**
- Mail it and log the Bureau's future clocks on the table page → **sprint_done**  _(cash −10 ; FLAG: appealFiled ; HIDDEN + Indicated-report appeal filed in writing on day 8 of 90)_
  - NOTE (shown after choosing): The wall is behind you now. The marathons remain, at marathon pace.
- Give the letter one more week of thought — first impressions matter → **sprint_done**
  - NOTE (shown after choosing): It went out on day 15, inside the window and unimproved. The wall does not grade drafts.
- Set the appeal aside until the case settles — one proceeding is enough → **end_registry133**
  - NOTE (shown after choosing): One proceeding is exactly the problem. The window closes April 30 whether the case has settled or not.

## [sprint_done] Itziar's Study, Itemized
*Day 14 — Monday, January 26, 2026 (dayOffset 14)*

The kinship study's list is the familiar constellation: clearances for every adult in the house, references, the home visit, the training module, Matteo's room. Itziar's house passes inspection the way her kitchen passes holidays: completely, with documentation.

One item snags: a clearance for your brother, who stays over 'sometimes' — sometimes being a word studies do not accept. He gets the form, or the couch gets a rule. The study must be able to say which, in writing.

**Choices:**
- Itemize the study in writing with the kinship worker, item by item, dates attached → **st_a**  _(cash −5 ; FLAG: studyList ; HIDDEN + Kinship study itemized in writing with dates)_
  - NOTE (shown after choosing): A checklist instead of a cloud. The brother question gets a written answer.
- Let the study find its own pace — Itziar's house speaks for itself → **st_a**
  - NOTE (shown after choosing): Her house does. Studies speak paper, and the sometimes-couch is exactly what they speak about.

## [st_a] The Study's First Visit
*Day 16 — Wednesday, January 28, 2026 (dayOffset 16)*

The kinship worker's first visit is a study in competence meeting competence: Itziar's house, Matteo's room, the forms produced from a folder labeled in marker with the boy's name and a star.

The worker's notes, later visible in the record, use the word 'prepared' — the study's first exhibit, written by its examiner.

**Choices:**
- Carry the page to its file → **st_b**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the record)_
  - NOTE (shown after choosing): Dated, copied, filed — the chain holds.
- Trust the conversation to carry it → **st_b**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [st_b] The Brother Question, Answered in Ink
*Day 18 — Friday, January 30, 2026 (dayOffset 18)*

Your brother signs his clearance form at Itziar's table and accepts the couch rule in the same sitting — family governance conducted at the speed of love and documented at the speed of paper.

The study's only snag is retired in week three, in writing, with a signature. The table notes it and moves on.

**Choices:**
- Carry the page to its file → **study_items**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the record)_
  - NOTE (shown after choosing): Dated, copied, filed — the chain holds.
- Trust the conversation to carry it → **study_items**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [study_items] Your Services, On the Second Chair
*Day 21 — Monday, February 2, 2026 (dayOffset 21)*

Your plan: a parenting course, a safety-planning series, and the overnight-work problem — you clean offices at night, which is how the forty minutes happened. The plan's answer is a documented coverage roster: Itziar, your sister, the neighbor with the signed letter, a phone tree on paper.

Coverage rosters are the plan's least believed document when they are verbal and its most believed when three signatures deep. Collect the signatures like the plan's life depends on them, because at the review, it will.

**Choices:**
- Build the roster on paper: three names, three signatures, filed with the plan → **roster**  _(cash −5 ; FLAG: rosterSigned ; HIDDEN + Childcare coverage roster signed and filed with the service plan)_
  - NOTE (shown after choosing): Three signatures deep. The forty minutes now have a documented answer.
- The roster is real — your family knows the arrangement → **roster**
  - NOTE (shown after choosing): Real and undocumented is the plan's saddest genre. Sign it.

## [roster] The Record, Requested for the Whole Table
*Day 29 — Tuesday, February 10, 2026 (dayOffset 29)*

You request the case record in writing (55 Pa. Code § 3130.44(d)) — and, because the study is a file too, Itziar requests what she may of her own study record, so both marathons run with mirrors. Redactions under (f) black out the neighbors' names, as the rule provides.

The packet shows the investigation's account of the pharmacy night — and the ER's timestamped receipt you gave the investigator, placing the round trip at thirty-eight minutes. The indicated summary says 'extended period.' Receipts say thirty-eight minutes. Both are now in the appeal's future.

**Choices:**
- File the receipt and a one-page timeline in both the case record and the appeal packet → **winter_roster**  _(cash −5 ; FLAG: recordsRequested ; HIDDEN + Case record requested under § 3130.44(d); pharmacy receipt and timeline filed in both tracks)_
  - NOTE (shown after choosing): Thirty-eight minutes, timestamped, in both files. Adjectives lose to receipts.
- Keep the receipt for the appeal hearing — it's the best surprise → **winter_roster**
  - NOTE (shown after choosing): Surprises are for birthdays. Filed receipts are for hearings — in both tracks.

## [winter_roster] The Roster's Quiet Weeks
*Day 36 — Tuesday, February 17, 2026 (dayOffset 36)*

February and March pass without a roster event, which is the roster working as designed: coverage so ordinary it generates no paper, the plan's least visible success. You log the ordinary weeks anyway, one line each, because the file cannot tell the difference between a quiet month and a missing one.

Itziar, reading over your shoulder, approves the method: 'Even nothing, dated.' The family is converging on a philosophy.

**Choices:**
- Do the paper version: dated, copied, filed → **receipt_filed**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the case record)_
  - NOTE (shown after choosing): Another dated page joins the folder.
- Handle it with a conversation and move on → **receipt_filed**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [receipt_filed] The Appeal's Evidence Packet
*Day 43 — Tuesday, February 24, 2026 (dayOffset 43)*

The scheduling order triggers the agency's duty: all evidence gathered in the investigation relevant to the determination, including the potentially exculpatory, within ten days (23 Pa.C.S. § 6341(c.2)(4)). Their packet includes the building's incident report — which records that the police entry, the reason anyone was in your home at all, concerned the unit across the hall.

Context is not an excuse; it is worse for the agency than an excuse. It is the file admitting the investigation began inside someone else's emergency and summarized yours from the doorway.

**Choices:**
- Build the appeal exhibits: receipt, timeline, incident report, the neighbor's signed statement → **ev_a**  _(cash −5 ; FLAG: evidenceReceived ; HIDDEN + Appeal evidence obtained under § 6341(c.2)(4) and indexed)_
  - NOTE (shown after choosing): The doorway summary, answered by documents from inside the apartment.
- Argue the context yourself at the hearing — you lived it → **ev_a**
  - NOTE (shown after choosing): You did. The incident report lived it too, in writing, without cross-examination.

## [ev_a] The Timeline, One Page
*Day 47 — Saturday, February 28, 2026 (dayOffset 47)*

The timeline of the pharmacy night fits one page because timestamps are mercifully short: the call, the departure, the receipt, the police entry for the neighbor's unit, the return. Five lines, five times, no adjectives.

Adjectives are where timelines go to be argued with. This one declines.

**Choices:**
- Carry the page to its file → **ev_b**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the record)_
  - NOTE (shown after choosing): Dated, copied, filed — the chain holds.
- Trust the conversation to carry it → **ev_b**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [ev_b] Both Tracks, Same Page
*Day 51 — Wednesday, March 4, 2026 (dayOffset 51)*

The timeline is filed in the dependency record and the appeal packet on the same day, with the same cover note — the corridor walked deliberately, so neither building can later claim it summarized the other.

Identical paper in two buildings is this family's answer to the summary problem: refuse to be summarized.

**Choices:**
- Carry the page to its file → **exhibits133**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the record)_
  - NOTE (shown after choosing): Dated, copied, filed — the chain holds.
- Trust the conversation to carry it → **exhibits133**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [exhibits133] The Study's Last Item
*Day 57 — Tuesday, March 10, 2026 (dayOffset 57)*

The study's last item is the training module, which Itziar completes with the air of a woman defusing a formality — and one question the trainer flags kindly: Itziar's plan for the nights you work, when Matteo stays with her, needs to be written into the study as the standing arrangement it already is.

The kinship worker adds the page. The study, in its final form, describes the family as it actually functions — the description being, in the end, what studies are for.

**Choices:**
- Get the standing-arrangement page added and the study's completion in writing → **prep_a133**  _(FLAG: studyDone ; HIDDEN + Kinship study completed with the standing arrangement documented)_
  - NOTE (shown after choosing): Complete, written, dated. Chair one is pulled fully in.
- Verbal confirmation is enough — the study is clearly done → **prep_a133**
  - NOTE (shown after choosing): 'Clearly' is not a status the review can cite. Get the writing.

## [prep_a133] The Officer's Likely Questions
*Day 60 — Friday, March 13, 2026 (dayOffset 60)*

Preparation turns to the hearing officer's likely questions, each answered by a document before it is answered by a voice: how long, who else was home, what the building's emergency actually was. The answers exist. They are exhibits.

Ms. Kortazar's rule for the room: never say in June what a page can say from March.

**Choices:**
- Carry the page to its file → **prep_b133**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the record)_
  - NOTE (shown after choosing): The chain holds because every link is dated.

## [prep_b133] The Neighbor's Statement, Signed
*Day 65 — Wednesday, March 18, 2026 (dayOffset 65)*

The neighbor across the hall — the one whose emergency opened your door to the police — signs her statement: the entry was for her unit, the boy was found asleep, the officer asked about the pharmacy and she heard 'twenty minutes, maybe.' Her maybe is honest. Your receipt is exact. Together they are devastating.

She signs in Itziar's kitchen, over coffee, like a person returning something borrowed.

**Choices:**
- Carry the page to its file → **prep_c133**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the record)_
  - NOTE (shown after choosing): The chain holds because every link is dated.

## [prep_c133] The Packet, Numbered
*Day 68 — Saturday, March 21, 2026 (dayOffset 68)*

The appeal packet is numbered the way exhibits prefer: receipt first, incident report second, statement third, timeline as the cover — four pages that tell the night in the order it happened, which is the order summaries never use.

Numbered, copied, filed. June is now a reading, and readings favor the prepared.

**Choices:**
- Carry the page to its file → **study_done133**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the record)_
  - NOTE (shown after choosing): The chain holds because every link is dated.

## [study_done133] The Course and the Roster, Tested
*Day 71 — Tuesday, March 24, 2026 (dayOffset 71)*

Spring tests the second chair: the course completes (certificate filed), and the roster gets its unplanned examination when your shift runs long in April and the phone tree executes exactly as documented — sister by 9, Itziar by 9:20, Matteo asleep at his grandmother's with his homework done, the caseworker's check-in note recording the roster working as written.

A plan that survives its test becomes the file's favorite kind of fact: the kind with a witness.

**Choices:**
- File the check-in note and the course certificate together — the plan, tested and passed → **spr_a**  _(FLAG: servicesDone ; HIDDEN + Services completed; coverage roster tested and documented as working)_
  - NOTE (shown after choosing): Tested, passed, filed. Chair two is in.
- One good note doesn't need filing — don't gloat on paper → **spr_a**
  - NOTE (shown after choosing): Filing is not gloating. It is how good notes survive staff rotations.

## [spr_a] The Course's Middle Weeks
*Day 76 — Sunday, March 29, 2026 (dayOffset 76)*

The parenting course's middle weeks are unglamorous and documented: attendance perfect, the workbook's exercises done in the handwriting of a person taking the thing seriously because the file will.

The instructor's mid-course note says 'engaged.' It is filed without embellishment. Mid-course notes are the review's appetizer.

**Choices:**
- Carry the page to its file → **spr_b**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the record)_
  - NOTE (shown after choosing): Dated, copied, filed — the chain holds.
- Trust the conversation to carry it → **spr_b**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [spr_b] The Shift Problem, Engineered
*Day 82 — Saturday, April 4, 2026 (dayOffset 82)*

Your employer's letter — the office-cleaning schedule adjusted so your late runs end by nine — joins the roster in the plan file, converting the plan's weakest paragraph into its most documented one.

Problems that are engineered on paper stay solved longer than problems that are promised away in meetings.

**Choices:**
- Carry the page to its file → **spr_c**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the record)_
  - NOTE (shown after choosing): Dated, copied, filed — the chain holds.
- Trust the conversation to carry it → **spr_c**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [spr_c] The Test Nobody Scheduled
*Day 87 — Thursday, April 9, 2026 (dayOffset 87)*

The April night the roster executes is written up by the caseworker in the ordinary course — she does not know she is writing the review's favorite paragraph, which is exactly why it will be.

Documents written without an audience are the only ones hearings fully trust. This family keeps producing them on schedule.

**Choices:**
- Carry the page to its file → **review_prep133**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the record)_
  - NOTE (shown after choosing): Dated, copied, filed — the chain holds.
- Trust the conversation to carry it → **review_prep133**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [review_prep133] The Spring Review
*Day 92 — Tuesday, April 14, 2026 (dayOffset 92)*

The spring review hears the three chairs in sequence: the study (approved, complete, the standing arrangement written in), the services (complete, the roster tested in the wild), and the appeal (pending at the Bureau, hearing set for June — its own building, its own clock).

The judge's sentence is the one the table was built to earn: 'This family has organized itself around the plan. The plan should now organize itself around the family.' What remains is sequencing the ending so the appeal's decision and the case's return do not trip over each other.

**Choices:**
- Do the paper version: dated, copied, filed → **appeal_hearing133**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the case record)_
  - NOTE (shown after choosing): Another dated page joins the folder.
- Handle it with a conversation and move on → **appeal_hearing133**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.
- Consolidate everything into the appeal now and let the study and the roster coast → **end_tipped**
  - NOTE (shown after choosing): Coasting is how chairs fall. The study's last items and the roster's signatures were the case the appeal was supposed to be beside.

## [appeal_hearing133] The Bureau Hearing
*Day 158 — Friday, June 19, 2026 (dayOffset 158)*

Friday, June 19, 2026. The agency carries its burden — substantial evidence that the report should remain indicated (23 Pa.C.S. § 6341(c.2)(5)) — and its summary meets the exhibits: thirty-eight minutes by timestamp, an investigation opened inside a neighbor's emergency, a coverage roster now signed and tested, a study approved.

The hearing officer returns twice to the receipt. Paper that times a night beats adjectives that stretch it; 'extended period' does not survive cross-examination by a timestamp.

**Choices:**
- Close on the receipt and the burden: their standard, their summary, your timestamps → **hr_a**
  - NOTE (shown after choosing): The shortest closing in the library: a receipt, read aloud.
- Close on Itziar and the year the family has had → **hr_a**
  - NOTE (shown after choosing): Moving, true, and not the standard the officer must apply.

## [hr_a] The Wait, Used
*Day 163 — Wednesday, June 24, 2026 (dayOffset 163)*

The weeks between hearing and decision are used the table's way: the trial-return proposal drafted, Itziar's respite language drafted, the endgame drawn in pencil beneath the table's ink — prepared endings being this family's final discipline.

When the decision comes, the case will not need to improvise its response to good news.

**Choices:**
- Carry the page to its file → **hr_b**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the record)_
  - NOTE (shown after choosing): Dated, copied, filed — the chain holds.
- Trust the conversation to carry it → **hr_b**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [hr_b] Itziar's Folder, Closed and Open
*Day 169 — Tuesday, June 30, 2026 (dayOffset 169)*

Itziar closes her study folder and immediately opens a respite folder — same marker, same star — because the family's paper, like the family, plans past the verdict.

The gesture is small and total: the kinship door, once opened by documents, stays open by documents.

**Choices:**
- Carry the page to its file → **decision133**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the record)_
  - NOTE (shown after choosing): Dated, copied, filed — the chain holds.
- Trust the conversation to carry it → **decision133**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [decision133] Expunged — Chair Three
*Day 176 — Tuesday, July 7, 2026 (dayOffset 176)*

The decision arrives inside the 45-day window (23 Pa.C.S. § 6341(c.3)): the report is amended to unfounded. Chair three is pulled in. What remains is pure sequencing: the case's own permanency path, with Matteo's fifteenth month far off (entry January 12, 2026 → April 12, 2027) and the court's spring sentence still warm.

Ms. Kortazar draws the endgame on the table page: trial return in the fall, with Itziar's placement converting to the family's standing respite — the kinship door held open by its own study — and the case to close at the new year if the trial reads the way the roster did.

**Choices:**
- File the expungement in the dependency record and propose the dated endgame → **carry_a133**  _(FLAG: expungementFiled ; HIDDEN + Expungement order filed in the dependency case; dated endgame proposed)_
  - NOTE (shown after choosing): The corridor walked again, order in hand. Sequencing is the last skill.
- The court knows about the expungement by now → **carry_a133**
  - NOTE (shown after choosing): Courts know what is filed. File it.

## [carry_a133] The Order, Carried
*Day 185 — Thursday, July 16, 2026 (dayOffset 185)*

The expungement order is copied for the dependency file the same week it arrives — not because the court asked, but because paper does not walk between buildings, and this family has appointed itself the corridor in three cases now.

The clerk stamps it. The dependency file's next reader will meet the registry's answer before forming the registry's assumption.

**Choices:**
- Carry the page to its file → **carry_b133**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the record)_
  - NOTE (shown after choosing): The chain holds because every link is dated.

## [carry_b133] The Endgame, Proposed on Paper
*Day 205 — Wednesday, August 5, 2026 (dayOffset 205)*

The endgame proposal goes in as a document, not a hope: trial return in the fall, respite in writing, closure at the new year — three dates with a family's whole table behind them.

Proposals on paper get answered on paper. The agency's response, when it comes, concurs in a paragraph — the system's way of applauding.

**Choices:**
- Carry the page to its file → **endgame133**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the record)_
  - NOTE (shown after choosing): The chain holds because every link is dated.

## [endgame133] The Trial, Run Like the Roster
*Day 238 — Monday, September 7, 2026 (dayOffset 238)*

The fall trial runs the way the roster did: overnights becoming weeks, the phone tree retiring into an ordinary family's ordinary arrangements, Itziar's spare room reverting to a grandson's room with a standing invitation rather than a placement order.

The new-year review is eleven minutes. The file the judge reads is the table, completed: study, services, appeal — three chairs, three checkmarks, one boy home.

**Choices:**
- Ask for closure with the respite written into the final order — Itziar's door, in ink → **fall_a133**  _(REQUIRES FLAG: recordsRequested ; REQUIRES FLAG: appealFiled ; REQUIRES FLAG: studyDone ; REQUIRES FLAG: rosterSigned)_
  - NOTE (shown after choosing): Closed, with the door held open on paper. The table stands.
- Ask for closure today without the respite language → **end_trial133**
  - NOTE (shown after choosing): Closure either way, likely — but the respite in ink is the family's insurance, and insurance is written or it isn't.
- Let the review close the case on its own momentum → **end_trial133**
  - NOTE (shown after choosing): Momentum closes cases eventually. Orders close them completely.

## [fall_a133] The Trial's First Fortnight
*Day 246 — Tuesday, September 15, 2026 (dayOffset 246)*

Matteo's trial begins with the choreography already rehearsed at Itziar's table: school nights at home, the spare room kept as his by right rather than by order, the phone tree retired to a refrigerator magnet.

The caseworker's first trial note is two lines long. Two-line notes are the sound of a plan working.

**Choices:**
- Carry the page to its file → **fall_b133**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the record)_
  - NOTE (shown after choosing): Dated, copied, filed — the chain holds.
- Trust the conversation to carry it → **fall_b133**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [fall_b133] The Ordinary Weeks, Logged
*Day 254 — Wednesday, September 23, 2026 (dayOffset 254)*

The fall runs ordinary: homework, the concert's sequel, one roster revival for a late shift that executes exactly as its signatures promised — documented by habit now, the habit being the year's deepest change.

Ordinary weeks are the trial's evidence. This family logs them like verdicts.

**Choices:**
- Carry the page to its file → **fall_c133**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the record)_
  - NOTE (shown after choosing): Dated, copied, filed — the chain holds.
- Trust the conversation to carry it → **fall_c133**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [fall_c133] The Final Order, Drafted
*Day 261 — Wednesday, September 30, 2026 (dayOffset 261)*

The final order is drafted before the review that will adopt it: closure, the respite clause, the study's standing noted — the family's whole table converted into the court's stationery, ready for a signature.

Drafted orders get signed. Undrafted outcomes get continued.

**Choices:**
- Carry the page to its file → **end_three_chairs**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the record)_
  - NOTE (shown after choosing): Dated, copied, filed — the chain holds.
- Trust the conversation to carry it → **end_three_chairs**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [end_three_chairs] Ending — All Three Chairs
*Day 365 — Tuesday, January 12, 2027 (dayOffset 365)*

The case closes in January with Matteo home, the registry clear, and Itziar's spare room holding a respite clause and a grandson's spare toothbrush — the two artifacts of the year, one legal and one not, both earned.

State it the debrief way: the win was not any single chair. Studies complete every week in this system, and services complete, and appeals are won — by different families, in different cases. The capstone was the coordination: sprint first, marathons in parallel, every document carried across the table to the chair that needed it, until all three could be pulled in at once.

**Ending.**

**Debrief:**
- THE TABLE'S LAW, CHAIR BY CHAIR — Appeal: notified January 30, 2026; 90 days → Thursday, April 30, 2026 (23 Pa.C.S. § 6341(a)(2)); evidence under (c.2)(4); the agency's burden under (c.2)(5); decision within (c.3)'s 45 days. Kinship: the study completed with the standing arrangement written into it — the placement's paper form, and the factual basis for the relative-care posture within 42 U.S.C. § 675(5)(E). Case: services completed and the coverage roster tested and documented; records under 55 Pa. Code § 3130.44(d) supplied the timestamped receipt that decided the appeal; counsel (42 Pa.C.S. § 6337) coordinated the three postures.
- WHY THIS IS A FULL WIN — Rare for a capstone: every track resolves completely — registry expunged, case closed, child home, kinship preserved as respite. It is full because the situation allowed it: one child, an early kinship placement, a short factual dispute (thirty-eight minutes) that documents could settle outright. The guide labels it full and notes the allowance honestly — most marathon cases end partial because their facts, not their paperwork, are heavier.
- WHAT NO STRATEGY CONTROLS — The hearing officer's weighing, the study's queue, the neighbor's emergency that started it. The route controlled the table: sequence, signatures, and the carrying of paper between chairs. In a three-chair case, coordination is not administration. It is the strategy.

## [end_trial133] Ending — Home, Two Chairs Pulled
*Day 365 — Tuesday, January 12, 2027 (dayOffset 365)*

Matteo comes home on the trial schedule and the case closes a season later than the best ending — the respite unwritten, the file's final order thinner than the family's actual arrangements. The appeal is expunged; the study stands; the services are complete. Only the sequencing frayed at the end.

It is a good ending wearing the ordinary cost of the system's slowest habit: outcomes that everyone agrees on, arriving at the pace of whoever failed to propose them in writing.

**Ending.**

**Debrief:**
- A PARTIAL WIN, NAMED HONESTLY — Everything resolved; only the timing and the ink suffered. The gated route required **recordsRequested**, **appealFiled**, **studyDone**, and **rosterSigned** arriving together at the final ask — the roster's signatures and the study's completion letter being the two papers most often left verbal in real three-chair cases.
- WHAT NO STRATEGY CONTROLS — The last review's judge and calendar. A family that has pulled all three chairs in will be home either way; the strategy's claim is about the season, and about whether the grandmother's door is held open by an order or by a habit.

## [end_tipped] Ending — The Tipped Table
*Day 365 — Tuesday, January 12, 2027 (dayOffset 365)*

In this branch, one chair was ignored until it fell: the appeal polished past April 30, or the study left to speak for itself until its items hardened into findings, or the roster left unsigned until the night it was needed and doubted.

A three-chair table does not collapse all at once. It tips toward the neglected chair, and the case's center of gravity moves with it — the registry shadowing the mother's work, or the placement questioned, or the plan read as paper over a gap. Recovery is possible from any one tip. It costs the season the coordination would have saved.

**Ending.**

**Debrief:**
- THE NEGLECTED CHAIR, ITEMIZED — The appeal's window (23 Pa.C.S. § 6341(a)(2)) is the only chair with a wall behind it; the study's items and the roster's signatures are the two most commonly left verbal. Each failure mode is a paperwork failure before it is anything else — which is the capstone's whole curriculum: at three chairs, the binding constraint is not effort but coordination.
- WHAT NO STRATEGY CONTROLS — Very little in this ending was weather. That is its function in the library: the control case that proves the table was the strategy.

## [end_registry133] Ending — Cleared Case, Standing Word
*Day 176 — Tuesday, July 7, 2026 (dayOffset 176)*

The dependency case closes beautifully — study, services, trial, home — and the registry keeps its word anyway, because the appeal's window closed on April 30 while the marathons were being run, and no one ran the sprint.

The entry surfaces where entries surface: the school-district volunteer form, the home-health aide application Lorea had planned for the spring. The case is a success story with a footnote that outlives it — which is why the sprint is run first in every guide in this library, including this one.

**Ending.**

**Debrief:**
- THE SPRINT THAT WASN'T — Notified Friday, January 30, 2026; 90 days → Thursday, April 30, 2026 (23 Pa.C.S. § 6341(a)(2)). Every other chair in this scenario can be recovered, continued, re-studied, re-signed. The appeal window cannot. Its loss does not defeat the case — the dependency court never asked the registry's permission — but it permanently taxes the mother's working life.
- WHAT NO STRATEGY CONTROLS — Nothing failed here except a date. The marathons were run well. The lesson is carved on the table itself: in multi-track cases, do the perishable thing first, especially when it is small.
