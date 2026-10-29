# THE FIRST 90 DAYS — Scenario 131: “Three Files, One Family”

*Human-readable script. This document and `scenario-131.json` are generated from a single source and match node-for-node: same IDs, same order, same choices, same effects.*

**The family is fictional — a composite. No real person's story appears here.**

**Content note:** This scenario depicts two siblings in placement on staggered timelines, an indicated-report appeal, and a permanency review. There is no graphic content. Players may skip any scene or use the quick exit at any time.

**How to read effects:** `cash −40` changes the player's cash. `FLAG: name` sets a flag the engine tracks. `HIDDEN + item` means the case file quietly records that item at this choice — the player does not see it when it happens. `REQUIRES FLAG: name` means the choice is only available if that flag was set earlier; `REQUIRES NO FLAG: name` means it is only available if that flag was never set. `NOTE:` is text shown to the player right after choosing.

Start date: Monday, November 3, 2025. Day offsets are days since the scenario's start date (the elder child's foster-care entry date).

## [start] Three Envelopes
*Day 0 — Monday, November 3, 2025 (dayOffset 0)*

Your name is Celeste. Teo, eleven, entered foster care on Monday, November 3, 2025, after the school called in the bruises from his bicycle crash and the story took a weekend to sort out. Irati, eight, followed on Friday, November 21 — the second entry the file records, eighteen days later, when the first placement could not take siblings and the case widened instead of narrowing.

And in December a third envelope joined the others: an indicated report, naming you, arising from the same crash — with a 90-day appeal window (23 Pa.C.S. § 6341(a)(2)) that closes Monday, March 16, 2026, counted from the December 16 notice. Three files. Three clocks. One mother. This is the marathon version of the lesson every smaller scenario taught: sequence is survival.

**Choices:**
- Build the master calendar first: every clock, every date, one page → **cal_a**  _(FLAG: calendarSet ; HIDDEN + Master calendar of all three tracks built)_
  - NOTE (shown after choosing): Three clocks, one page, on the refrigerator, where fear can't blur them.
- Handle each file as it comes up — you're organized enough → **cal_a**
  - NOTE (shown after choosing): Organized enough is the epitaph of many a deadline.

## [cal_a] The Envelopes, Opened in Order
*Day 1 — Tuesday, November 4, 2025 (dayOffset 1)*

Each envelope is opened at the kitchen table and read twice — once for what it says, once for what it starts. Three start-dates, three different kinds of clock, and a household that has just learned the difference between them.

You write the three dates on an index card before you do anything else. The card will outlive the envelopes.

**Choices:**
- Carry the page to its file → **cal_b**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the record)_
  - NOTE (shown after choosing): Dated, copied, filed — the chain holds.
- Trust the conversation to carry it → **cal_b**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [cal_b] What a Calendar Cannot Do
*Day 2 — Wednesday, November 5, 2025 (dayOffset 2)*

A calendar cannot attend a hearing, file a letter, or love two children in two placements. What it can do — all it can do, and everything — is make sure none of those things is ever attempted late.

Counsel gets the second index card. The refrigerator gets the first. The folder gets the originals.

**Choices:**
- Carry the page to its file → **calendar131**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the record)_
  - NOTE (shown after choosing): Dated, copied, filed — the chain holds.
- Trust the conversation to carry it → **calendar131**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [calendar131] Ms. Urrutia Draws the Board
*Day 4 — Friday, November 7, 2025 (dayOffset 4)*

Your lawyer, Ms. Urrutia, draws the board the way the appeal scenario taught: three columns — TEO (entered Nov 3, 2025; fifteen months = Wednesday, February 3, 2027), COSETTE (entered Nov 21, 2025; fifteen months = Sunday, February 21, 2027), APPEAL (notified Dec 16, 2025; due March 16, 2026). 'Different children, different months,' she says. 'The statute counts children, not families.'

Counsel is your right (42 Pa.C.S. § 6337) — and here, counsel is also cartography. 'The appeal goes first,' she says, tapping March. 'It is the only date on this board that cannot be continued.'

**Choices:**
- Do the paper version: dated, copied, filed → **appeal_first**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the case record)_
  - NOTE (shown after choosing): Another dated page joins the folder.
- Handle it with a conversation and move on → **appeal_first**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [appeal_first] The Appeal, Filed in Week One
*Day 9 — Wednesday, November 12, 2025 (dayOffset 9)*

The appeal letter is the half-page the library's families know by heart: name, report number, amend or expunge, signature, date. It goes out on day 9 of 90 — not because the appeal is the most important file, but because it is the most perishable.

The clerk stamps your copy. March 16 is now a date you own instead of a date that owns you.

**Choices:**
- Mail it with the stamped copy filed, and note the Bureau's clocks on the calendar: evidence, hearing, decision → **appeal_done**  _(cash −10 ; FLAG: appealFiled ; HIDDEN + Indicated-report appeal filed in writing on day 9 of 90)_
  - NOTE (shown after choosing): Filed first because it perishes first. Sequence is the strategy.
- Draft it carefully and mail it after the January review settles your thinking → **appeal_done**
  - NOTE (shown after choosing): January reviews have eaten bigger windows than this one. You mailed it — day 30-plus, inside, and lucky.

## [appeal_done] Two Placements, Two Logs
*Day 16 — Wednesday, November 19, 2025 (dayOffset 16)*

Teo is with a foster family near his school; Irati is with a resource family across town, because the sibling home fell through in week two — a fact the file records in one line and the children record in every Sunday visit, which happens at a park between the two houses, weather permitting, love insisting.

Sibling visits are a plan item. Plan items generate paper or they generate apologies. Your job, per Ms. Urrutia: make them generate paper.

**Choices:**
- Keep one sibling-visit log for both children, signed by both resource families → **two_a**  _(FLAG: siblingLog ; HIDDEN + Sibling visit log kept and countersigned by both placements)_
  - NOTE (shown after choosing): One log, two signatures, two children in the same document — the file rarely sees them together. Make it.
- Each home keeps its own notes — that's their job → **two_a**
  - NOTE (shown after choosing): Their job is care. The log is yours.

## [two_a] Two Sundays
*Day 18 — Friday, November 21, 2025 (dayOffset 18)*

The Sunday visit, in a park between two placements, becomes the family's fixed point: sandwiches, the log, the children's running audit of each other's weeks. Resource families who sign a log together start, slowly, to coordinate like one.

Coordination between placements is not the agency's job to invent. It can be the family's job to document.

**Choices:**
- Carry the page to its file → **two_b**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the record)_
  - NOTE (shown after choosing): Dated, copied, filed — the chain holds.
- Trust the conversation to carry it → **two_b**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [two_b] The Log's Second Signature
*Day 20 — Sunday, November 23, 2025 (dayOffset 20)*

Teo's resource mother signs; Irati's signs beneath her, in a different hand, and the log becomes the first document in either file that contains both children's names on the same page for a family reason.

Small paper. The marathon is made of it.

**Choices:**
- Carry the page to its file → **records131**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the record)_
  - NOTE (shown after choosing): Dated, copied, filed — the chain holds.
- Trust the conversation to carry it → **records131**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [records131] Both Records, Requested
*Day 23 — Wednesday, November 26, 2025 (dayOffset 23)*

Two dependency cases means two case records, and the request that unlocks them is the same in each: the material is released upon request (55 Pa. Code § 3130.44(d)), with redactions for others' information under (f). You sign both requests in one sitting, because partial mirrors produce partial strategies.

What comes back will show you each child's file as its own court will read it — including whether either file even mentions the other's clock.

**Choices:**
- Sign both written requests; file both stamped copies in the master folder → **packets_back**  _(cash −10 ; FLAG: recordsRequested ; HIDDEN + Both children's case records requested in writing under § 3130.44(d))_
  - NOTE (shown after choosing): Two mirrors, requested together. The board is about to get honest.
- Request Teo's now — his clock is the urgent one → **packets_back**
  - NOTE (shown after choosing): His is earlier by eighteen days. Irati's is the one that will surprise you.

## [packets_back] What the Two Files Say
*Day 44 — Wednesday, December 17, 2025 (dayOffset 44)*

Teo's file is orderly: services dated, visits logged, the bicycle-crash investigation summarized fairly. Irati's file is thinner and stranger: her entry paperwork carries a wrong date — November 12, nine days before she entered care — inflating her clock by over a week, an error no one made on purpose and everyone downstream has been copying.

Clocks built on copied errors are still clocks, until someone files the correction. You are someone. The correction is a page with the true date, the entry order attached, and a request that both files carry it.

**Choices:**
- File the date correction in both children's files, entry order attached → **read_a**  _(cash −5 ; FLAG: dateCorrected ; HIDDEN + Irati's entry-date error corrected in writing in both files)_
  - NOTE (shown after choosing): Nine days, returned to an eight-year-old by a photocopy. The calendar is a moral instrument.
- Mention the wrong date at the next review so the judge can note it → **read_a**
  - NOTE (shown after choosing): Judges note what is filed. What is mentioned gets noted as mentioned.

## [read_a] Reading Teo's File First
*Day 50 — Tuesday, December 23, 2025 (dayOffset 50)*

Teo's file reads like a case being run by adults: dated services, honest summaries, the crash investigation closed fairly. You index it in an evening and feel, briefly, the system's competence as a personal kindness.

Then you open Irati's, and the evening changes.

**Choices:**
- Carry the page to its file → **read_b**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the record)_
  - NOTE (shown after choosing): Dated, copied, filed — the chain holds.
- Trust the conversation to carry it → **read_b**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [read_b] Reading Irati's File
*Day 53 — Friday, December 26, 2025 (dayOffset 53)*

Hers is thinner — second children in widened cases often get the thinner file — and on its third page sits the entry date, November 12, nine days before the entry order you hold in your other hand says November 21.

You read the page three times. Then you do what the library exists to teach: you reach for a pen, not a phone.

**Choices:**
- Carry the page to its file → **correction_filed**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the record)_
  - NOTE (shown after choosing): Dated, copied, filed — the chain holds.
- Trust the conversation to carry it → **correction_filed**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [correction_filed] The Appeal's Evidence
*Day 58 — Wednesday, December 31, 2025 (dayOffset 58)*

The Bureau's scheduling order arrives, and with it the duty the appeal rules place on the agency: provide the appellant all evidence gathered during the investigation relevant to the determination, including the potentially exculpatory, within ten days of the order (23 Pa.C.S. § 6341(c.2)(4)).

The packet holds the school nurse's note from the crash day — 'spoke with Teo; states he fell from bicycle onto handlebars; bruising pattern consistent' — the sentence the indicated summary had compressed into 'injuries unexplained.' The hallway's rule holds in the third file too: the decisive page is usually already written, by someone else, waiting to be asked for.

**Choices:**
- Build the appeal exhibit set around the nurse's note and the dated photos → **evid_a**  _(cash −5 ; FLAG: evidenceReceived ; HIDDEN + Investigation evidence obtained under § 6341(c.2)(4))_
  - NOTE (shown after choosing): Their packet, your exhibits. The burden will be theirs at the hearing (23 Pa.C.S. § 6341(c.2)(5)); the paper is already yours.
- Your own account of the crash should carry the appeal → **evid_a**
  - NOTE (shown after choosing): Accounts need corroboration the way clocks need dates. The nurse wrote both.

## [evid_a] The School's Letter
*Day 63 — Monday, January 5, 2026 (dayOffset 63)*

Teo's school counselor writes the letter the appeal will want in June: the crash, the nurse's note, the boy's account consistent across three tellings — the small, boring consistency that investigations are supposed to notice.

It is requested in writing, received in writing, and filed in both tracks. Boring consistency, documented, is a theme of this family's year.

**Choices:**
- Carry the page to its file → **evid_b**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the record)_
  - NOTE (shown after choosing): Dated, copied, filed — the chain holds.
- Trust the conversation to carry it → **evid_b**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [evid_b] The Photographs, Dated
*Day 67 — Friday, January 9, 2026 (dayOffset 67)*

The crash-weekend photographs — the bicycle, the handlebar bruise, the helmet split along its seam — are printed with their dates and filed beside the counselor's letter. Photographs without dates are allegations; with dates, they are exhibits.

The folder gains a section. June is five months away and already losing.

**Choices:**
- Carry the page to its file → **services131**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the record)_
  - NOTE (shown after choosing): Dated, copied, filed — the chain holds.
- Trust the conversation to carry it → **services131**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [services131] Two Service Plans, One Mother
*Day 73 — Thursday, January 15, 2026 (dayOffset 73)*

Your services run on two plans in two files that occasionally forget they describe the same woman: a parenting course (Teo's file), a family-therapy referral (Irati's), and a housing application that both files cite and neither owns. The therapy referral, the record shows, was sent five weeks after Irati's plan was signed.

Gaps that live between two files belong fully to neither — which means, at the permanency table, they can be charged to you in both. The letter that prevents this is short: dates, plan, referral, in both files.

**Choices:**
- Write the referral-gap letter once and file it in both children's cases → **gap_both**  _(cash −5 ; FLAG: gapDocumented ; HIDDEN + Therapy referral gap documented in both children's files)_
  - NOTE (shown after choosing): One letter, two files. The gap now belongs to its true owner in both courtrooms.
- Raise the gap in Teo's file — the therapy matters most there → **gap_both**
  - NOTE (shown after choosing): It matters in Irati's file, where it happened. Gaps must be filed where they live.

## [gap_both] The Spring Reviews
*Day 95 — Friday, February 6, 2026 (dayOffset 95)*

Spring reviews for both children land in the same week — a scheduling accident that functions as a rehearsal for every combined hearing to come. The judges (two of them; the files never merged) each read a file that now contains the correction, the logs, the gap letter, and the appeal's existence noted by date.

Teo's judge says the sentence: 'I see the mother's other matters are being litigated in their proper forums, on time.' It is the sound of three files agreeing about you.

**Choices:**
- Do the paper version: dated, copied, filed → **fall_reviews**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the case record)_
  - NOTE (shown after choosing): Another dated page joins the folder.
- Handle it with a conversation and move on → **fall_reviews**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [fall_reviews] The Reviews Before the Hearing
*Day 118 — Sunday, March 1, 2026 (dayOffset 118)*

May's reviews, one per child, rehearse June: Teo's judge notes the appeal pending and says nothing more about it — its own building, its own burden — while Irati's commends the corrected file by name, an eight-year-old's nine days entered into a court record as a lesson in proofreading with consequences.

The Bureau's hearing notice is already in the folder. The spring's last job is the witness list, filed in both tracks, so no June morning begins with a missing name.

**Choices:**
- Do the paper version: dated, copied, filed → **appeal_hearing131**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the case record)_
  - NOTE (shown after choosing): Another dated page joins the folder.
- Handle it with a conversation and move on → **appeal_hearing131**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [appeal_hearing131] The Bureau Hearing
*Day 217 — Monday, June 8, 2026 (dayOffset 217)*

Monday, June 8, 2026. The agency must prove by substantial evidence that the report should remain indicated (23 Pa.C.S. § 6341(c.2)(5)). Its case is the summary. Yours is the packet: the nurse's note, the dated photographs, the school counselor's statement, the crash-weekend timeline your sister signed in April.

The hearing officer asks the agency's witness one question — whether the investigation file contained the nurse's note when the summary was written. The answer is in the transcript forever now: yes.

**Choices:**
- Close on the burden and the note: their standard, their file, their omission → **bur_a**
  - NOTE (shown after choosing): Short closings win paper cases. This one was written by a school nurse in November.
- Close on the children's year and what the registry would cost them all → **bur_a**
  - NOTE (shown after choosing): True, moving, and not the standard. The officer must apply the standard.

## [bur_a] The Transcript's Quiet Pages
*Day 225 — Tuesday, June 16, 2026 (dayOffset 225)*

After the hearing, before the decision, there is the transcript request — made in writing, because the words said in June will be quoted in rooms the family never enters, and quotations prefer originals.

The agency's witness's answer about the nurse's note is on page forty-one. You will never need to quote it. Everyone will know you can.

**Choices:**
- Carry the page to its file → **bur_b**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the record)_
  - NOTE (shown after choosing): Dated, copied, filed — the chain holds.
- Trust the conversation to carry it → **bur_b**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [bur_b] Waiting, Documented
*Day 238 — Monday, June 29, 2026 (dayOffset 238)*

The decision window — forty-five days under the statute — is waited out the documented way: services continuing, visits logged, the kinship study of Aunt Selene begun at the agency's own suggestion, paper accumulating in all three files at the pace of a family that has stopped fearing it.

Waiting is a skill. This family has made it a record.

**Choices:**
- Carry the page to its file → **decision131**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the record)_
  - NOTE (shown after choosing): Dated, copied, filed — the chain holds.
- Trust the conversation to carry it → **decision131**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [decision131] Expunged, and What It Doesn't Do
*Day 253 — Tuesday, July 14, 2026 (dayOffset 253)*

The decision — entered within the 45 days the statute allows (23 Pa.C.S. § 6341(c.3)) — amends the report to unfounded. You read it twice at the kitchen table, and Ms. Urrutia's voice is in your ear from November: 'Winning the third file does not win the first two. It clears the air they breathe.'

She is right. Teo's clock still reads February 2027; Irati's, February 2027 (corrected). The dependency cases do not care about the registry — except that every future reader of either file will now meet a mother whose indicated report was examined and expunged, instead of assumed.

**Choices:**
- File the expungement order in both dependency files, with a cover page noting the date → **kinship131**  _(FLAG: expungementFiled ; HIDDEN + Expungement order filed in both dependency cases)_
  - NOTE (shown after choosing): Paper does not walk between buildings. You are the corridor.
- The dependency courts will hear about it through the agency → **kinship131**
  - NOTE (shown after choosing): They will hear a summary of it. Summaries are how good news goes to be diminished.

## [kinship131] Aunt Selene's Application
*Day 305 — Friday, September 4, 2026 (dayOffset 305)*

Autumn brings the kinship door: your aunt Selene, retired from the school district, applies to take both children together — the sibling placement that fell through last November, now with a study, a spare house, and a year of Sunday visits to point to. Kinship care, if it comes, is also one of the permanency clock's own exceptions: a child being cared for by a relative is outside the filing duty (42 U.S.C. § 675(5)(E)).

The study needs the usual constellation: clearances, references, the home visit, dates. You know the choreography by now. So does Selene, who has started a folder of her own — the family resemblance is administrative.

**Choices:**
- Support the study with the sibling log and a written request that both files note it → **study131**  _(cash −5 ; FLAG: kinAsked ; HIDDEN + Kinship study supported with the sibling log; request noted in both files)_
  - NOTE (shown after choosing): The log does double duty: it proves the bond the placement would protect.
- Let the study proceed without your fingerprints on it → **study131**
  - NOTE (shown after choosing): Support visible in the file reads as a family organizing itself. Absence reads as absence.

## [study131] The Study and the Services
*Day 322 — Monday, September 21, 2026 (dayOffset 322)*

The study proceeds; your services complete in their two files: course certificate (filed, Teo), therapy goals met (filed, Irati — with the gap letter explaining the plan's arithmetic to any reader who wonders why it took until fall).

Housing remains the board's last open square: your application, filed in spring, reaches its letter in November — a dated waitlist position with a projected February opening, on letterhead, in both files now.

**Choices:**
- Assemble the exception packets child by child: Teo's and Irati's, each with its own dates → **study_winter**  _(cash −10 ; FLAG: packetBuilt ; HIDDEN + Per-child exception packets assembled with individual dates)_
  - NOTE (shown after choosing): Two packets, two clocks, no blended arithmetic. The statute counts children; so do you.
- Build one family packet — the story is the same → **study_winter**
  - NOTE (shown after choosing): The story rhymes; the dates don't. Blended packets are where child-specific exceptions go to blur.

## [study_winter] The Winter of Two Bedtimes
*Day 334 — Saturday, October 3, 2026 (dayOffset 334)*

December splits the children's evenings between Selene's house and their placements' trial overnights, a geography of toothbrushes in three bathrooms. The log — the one document that has followed both children everywhere — records it all without commentary, which is what logs are for.

Ms. Urrutia reads a page and says the sentence the winter deserves: 'This is what a family looks like when it refuses to let two files raise two strangers.'

**Choices:**
- Do the paper version: dated, copied, filed → **ord_a**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the case record)_
  - NOTE (shown after choosing): Another dated page joins the folder.
- Handle it with a conversation and move on → **ord_a**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [ord_a] The Study's References
*Day 340 — Friday, October 9, 2026 (dayOffset 340)*

Selene's references are collected the study's way: three letters, three phone calls, each logged by the worker with dates. A retired principal writes that Selene 'kept the district's lost children found for thirty years,' a sentence no home study was ever improved by and none was ever hurt by.

References, like everything else in this case, are paper or they are weather.

**Choices:**
- Carry the page to its file → **ord_b**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the record)_
  - NOTE (shown after choosing): Dated, copied, filed — the chain holds.
- Trust the conversation to carry it → **ord_b**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [ord_b] The Home Visit
*Day 346 — Thursday, October 15, 2026 (dayOffset 346)*

The home visit finds the spare room already plural: two beds, two hooks, a calendar on the wall with both children's school breaks marked in a grandmother-generation hand that predates the case by decades of practice.

The worker photographs the room for the study. The room, being Selene's, photographs like an argument.

**Choices:**
- Carry the page to its file → **ord_c**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the record)_
  - NOTE (shown after choosing): Dated, copied, filed — the chain holds.
- Trust the conversation to carry it → **ord_c**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [ord_c] Both Files Note the Study
*Day 352 — Wednesday, October 21, 2026 (dayOffset 352)*

Your written request — that both children's files note the study's progress by date — is granted the way such requests are granted when they are reasonable, written, and early: without discussion, in both files, by Friday.

Two files, one study, no divergence. The marathon's arithmetic improves every time the paper agrees with itself.

**Choices:**
- Carry the page to its file → **packets131**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the record)_
  - NOTE (shown after choosing): Dated, copied, filed — the chain holds.
- Trust the conversation to carry it → **packets131**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [packets131] The Winter Push
*Day 362 — Saturday, October 31, 2026 (dayOffset 362)*

Winter is the long middle of every marathon case: visits expand at both placements, overnights begin at Selene's newly approved home — both children, together, the study approved in December with the court's blessing noted in both files (a relative placement, documented) — and your overnights at your own apartment begin in January, with the February unit letter framed like art.

The fifteen-month dates now approach in their corrected forms: Teo, Wednesday, February 3, 2027; Irati, Sunday, February 21, 2027. Behind each date stands a packet, a plan entry, and a relative's approved home. The clocks will ask their question. The files are ready to answer in triplicate.

**Choices:**
- Do the paper version: dated, copied, filed → **review131**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the case record)_
  - NOTE (shown after choosing): Another dated page joins the folder.
- Handle it with a conversation and move on → **review131**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.
- File one blended family packet covering both children and rest → **end_one_clock**
  - NOTE (shown after choosing): One packet, two clocks — and one child's exception blurred past reading. The blended file is where the marathon is lost.

## [review131] The Review Where the Dates Are Said
*Day 398 — Sunday, December 6, 2026 (dayOffset 398)*

January's combined review — the two judges have begun, sensibly, to sit in sequence on the same morning — hears the state of all three files: the appeal, closed and expunged; the placements, united at Selene's; the services, complete with their gaps documented and owned by their true dates.

The agency's counsel states the permanency position carefully: the February dates will be met, as the statute contemplates, by the documented exceptions — relative care for both children, and the compelling reason written into each case plan this month at your lawyer's request: reunification on track, trial return scheduled, filing not in either child's interest (42 U.S.C. § 675(5)(E)).

**Choices:**
- Ask both courts to write it: exceptions documented, trial return to begin, goal unchanged in both files → **feb_a**  _(REQUIRES FLAG: recordsRequested ; REQUIRES FLAG: appealFiled ; REQUIRES FLAG: packetBuilt ; REQUIRES FLAG: dateCorrected)_
  - NOTE (shown after choosing): Asked in both rooms, answered in both orders. The board is fully lit.
- Ask for immediate return of both children — everything is documented → **end_trial131**
  - NOTE (shown after choosing): Everything is documented except the last step, which is a step. The best ending takes it in order.
- Let the agency's statement stand without asking for orders → **end_trial131**
  - NOTE (shown after choosing): Statements evaporate. Orders accumulate.
- Accept the agency's split proposal: Teo home now, Irati's goal revisited in the fall → **end_split131**
  - NOTE (shown after choosing): A split offered in January is a split that lasts. The board was built to refuse it politely, with paper.

## [feb_a] The January Paper, Assembled
*Day 420 — Monday, December 28, 2026 (dayOffset 420)*

Before February's dates arrive, the packets are assembled in their final form: per child, per exception, each document dated, each date matching the master calendar — which is checked, one last time, against the entry orders themselves.

Trust, in this family, is a thing that gets verified against originals. The calendar passes.

**Choices:**
- Carry the page to its file → **feb_b**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the record)_
  - NOTE (shown after choosing): Dated, copied, filed — the chain holds.
- Trust the conversation to carry it → **feb_b**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [feb_b] The Trial's First Weeks
*Day 444 — Thursday, January 21, 2027 (dayOffset 444)*

The trial return's first weeks are documented the way the whole case has been: visits converting to overnights, overnights to weeks, the log's signatures changing from supervision to simple acknowledgment that the children were, as expected, home.

February approaches on the calendar like a date that has already been answered — because, in January's orders, it has.

**Choices:**
- Carry the page to its file → **february131**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the record)_
  - NOTE (shown after choosing): Dated, copied, filed — the chain holds.
- Trust the conversation to carry it → **february131**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [february131] February, Twice
*Day 457 — Wednesday, February 3, 2027 (dayOffset 457)*

Wednesday, February 3, 2027 — Teo's fifteenth month — passes the way prepared-for dates do: as a review already held, an exception already documented, a trial return already running. Sunday, February 21 — Irati's, on her corrected clock — passes the same way, eighteen days later, the echo arriving exactly when the master calendar always said it would.

No petition is filed in either case. The question the statute asks at fifteen months was answered in January, in writing, child by child. This is what the finish line of a marathon case looks like: not a tape, but a table — three files, all answered, and a trial return converting to a return while the folder, at last, gets lighter instead of heavier.

**Choices:**
- Convert the trial return at the spring review, both children, aftercare in writing in both files → **end_answered**
  - NOTE (shown after choosing): The last move is the first lesson, twice: in writing, in both files.
- Let the trial simply run its course → **end_trial131**
  - NOTE (shown after choosing): Open files collect new summaries. Close them the way you carried them.

## [end_answered] Ending — Every Clock Answered
*Day 470 — Tuesday, February 16, 2027 (dayOffset 470)*

By spring both children are home — returned on orders written in two courtrooms, built on one folder. Selene's home stays in the orders as the family's standing respite, the kinship door held open by the same paperwork that opened it. The registry holds nothing against you; the Bureau saw to that in a decision your grandchildren could read.

State it honestly, the way the debriefs insist: the children spent fifteen months in care, and no strategy gives those months back. What the strategy did was narrower and total: no clock in any of the three files ever found this family unprepared, undocumented, or late. In a marathon case, that is not a consolation. That is the win.

**Ending.**

**Debrief:**
- THE THREE CLOCKS, AUDITED — Appeal: notified December 16, 2025; 90 days → Monday, March 16, 2026; filed day 9 (23 Pa.C.S. § 6341(a)(2)); evidence under (c.2)(4); burden on the agency under (c.2)(5); decision within (c.3)'s 45 days. Teo: entered November 3, 2025 + 15 months = Wednesday, February 3, 2027. Irati: entered November 21, 2025 (her file's copied November 12 was corrected on the record) + 15 months = Sunday, February 21, 2027. The filing duty and its exceptions — relative care, documented compelling reason, services not provided (42 U.S.C. § 675(5)(E)) — are counted per child, which is why the packets were built per child.
- WHY THIS IS LABELED PARTIAL — The best ending this scenario offers keeps the goal intact, defeats every clock, and returns both children — after fifteen months of placement. A strategy guide that called that unqualified victory would be lying about the cost. The win is real: it is the best possible outcome the documented situations allow, and it was reached by sequencing — perishable deadline first, mirrors second, corrections and packets child by child, orders asked for in both rooms.
- WHAT NO STRATEGY CONTROLS — Two judges, a hearing officer, a study queue, a housing waitlist, and a bicycle. The route controlled the order of the paper and the accuracy of the dates — in a three-file case, the two things most likely to be lost and the two things that decide it. Counsel (42 Pa.C.S. § 6337) and the record requests (55 Pa. Code § 3130.44(d)) are the load-bearing walls; everything else is the family, living its year in date order.

## [end_trial131] Ending — Home in Stages, Both Files Open
*Day 470 — Tuesday, February 16, 2027 (dayOffset 470)*

The children come home in stages across the spring — Teo first, on his earlier clock's order; Irati on a trial that stretches toward summer — with both cases still open, both folders still growing, and the fifteenth months survived but not, as in the best ending, answered in advance.

Nothing failed here. The exceptions held, the appeal is expunged, the goal never moved. The difference is the texture of the ending: orders asked for late produce returns that arrive late, in a system where late is measured in childhoods.

**Ending.**

**Debrief:**
- A PARTIAL WIN, SLOWER THAN THE BEST — The same facts, the same clocks, a later set of asks. The gated route required **recordsRequested**, **appealFiled**, **packetBuilt**, and **dateCorrected** — the correction alone was worth nine days of a child's clock, and it existed only because both records were requested and read.
- WHAT NO STRATEGY CONTROLS — Judicial sequencing across two courtrooms. Two files can be won in the same season and still close in different months; the strategy's claim is that neither was ever lost to a date.

## [end_one_clock] Ending — The Clock That Got Away
*Day 470 — Tuesday, February 16, 2027 (dayOffset 470)*

In this branch the appeal was polished instead of filed, or Irati's date was never corrected, or one file's packet was left to a summary — and the board's discipline is shown by its absence: one of the three clocks, the one nobody was watching that month, ran out.

A petition in one child's case, or a registry entry that outlives both dependency files: the marathon's cruelty is arithmetic. Attention divided by three files is still attention, but the clocks do not divide at all.

**Ending.**

**Debrief:**
- THE MARATHON'S LESSON — Every deadline in this scenario was computed from primary dates: the 90-day appeal window (23 Pa.C.S. § 6341(a)(2)), and per-child fifteen-month dates under 42 U.S.C. § 675(5)(E). The failures that produce this ending are never effort failures. They are sequencing failures — the perishable filed late, the copied error uncorrected, the second child's packet blended into the first's.
- WHAT NO STRATEGY CONTROLS — Very little, in this ending, was outside the strategy: that is what makes it the cautionary one. The board on the refrigerator — every clock, every date, one page — is the whole defense. Keep the board.

## [end_split131] Ending — Two Files Won, One Still Running
*Day 470 — Tuesday, February 16, 2027 (dayOffset 470)*

This branch ends mid-marathon: the appeal expunged, one child home, the other's case converted to a longer plan after a goal the court questioned in the fall and the file answered too late.

It is the most common shape of real multi-file cases — not triumph, not disaster, but a split decision measured in different bedtimes in different houses. The folder remains open on the kitchen table, because one file is still running, and it will be run the same way: in date order, to the end.

**Ending.**

**Debrief:**
- A SPLIT, NAMED HONESTLY — Multi-file cases rarely resolve in a single hearing, and this ending refuses to pretend otherwise. The tracks that were won were won on the library's constants: early appeal (§ 6341(a)(2)), evidence under (c.2)(4), records under § 3130.44(d), per-child exceptions under § 675(5)(E).
- WHAT NO STRATEGY CONTROLS — Courts sequence siblings by their own calendars, and a goal questioned in the fall can take a season to answer even with the right paper. The split is not the strategy failing; it is the strategy still running, one file short of the table.
