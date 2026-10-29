# THE FIRST 90 DAYS — Scenario 134: “The Appeal Beside the Case”

*Human-readable script. This document and `scenario-134.json` are generated from a single source and match node-for-node: same IDs, same order, same choices, same effects.*

**The family is fictional — a composite. No real person's story appears here.**

**Content note:** This scenario depicts an indicated-report appeal proceeding alongside a dependency case. There is no graphic content. Players may skip any scene or use the quick exit at any time.

**How to read effects:** `cash −40` changes the player's cash. `FLAG: name` sets a flag the engine tracks. `HIDDEN + item` means the case file quietly records that item at this choice — the player does not see it when it happens. `REQUIRES FLAG: name` means the choice is only available if that flag was set earlier; `REQUIRES NO FLAG: name` means it is only available if that flag was never set. `NOTE:` is text shown to the player right after choosing.

Start date: Monday, February 2, 2026. Day offsets are days since the scenario's start date (the appeal notice date).

## [start] The Boiler Room and the Letter
*Day 0 — Monday, February 2, 2026 (dayOffset 0)*

Your name is Koldo. You keep the boilers running at a school across town from the one your daughter Arantxa, six, attends — a fact the investigation never quite kept straight. The Saturday the furnace failed at your building, you brought Arantxa to your sister's, then to the boiler room for forty minutes with her tablet and a chair by the door while you and the super, Mr. Zubia, coaxed the plant back to life.

The report that followed says a child was left unsupervised in an industrial space. The dependency petition says the home needs services. And on Monday, February 2, 2026, the indicated notice arrives with its 90-day window (23 Pa.C.S. § 6341(a)(2)) — closing Sunday, May 3, 2026 — stapled, in your mind, to a case file that is not the same file. Two proceedings now run beside each other. They will be decided by different people, under different burdens, from different paper. Confusing them is the first way to lose both.

**Choices:**
- Draw two columns on one page: APPEAL and CASE, each with its own clock → **two_files**  _(FLAG: columnsDrawn ; HIDDEN + Two-proceeding board drawn with separate clocks)_
  - NOTE (shown after choosing): Two files, two columns, no bleeding ink between them.
- It's one problem with two envelopes — treat it as one → **two_files**
  - NOTE (shown after choosing): The envelopes disagree with you, and they get a vote.

## [two_files] Ms. Ndiaye Separates the Burdens
*Day 3 — Thursday, February 5, 2026 (dayOffset 3)*

Your lawyer, Ms. Ndiaye — counsel being your right in the dependency case (42 Pa.C.S. § 6337) — draws the distinction the year will run on: 'In the appeal, the agency must prove its report by substantial evidence (23 Pa.C.S. § 6341(c.2)(5)). In the case, the court asks what Arantxa needs and whether the plan is working. Different questions. Different evidence. The same man, unfortunately for your calendar.'

She is blunt about sequencing: the appeal's window closes May 3 and cannot be reopened; the case's reviews can be continued. 'Perishable first,' she says, 'in this family as in all families.'

**Choices:**
- Do the paper version: dated, copied, filed → **tw_a**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the case record)_
  - NOTE (shown after choosing): Another dated page joins the folder.
- Handle it with a conversation and move on → **tw_a**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [tw_a] Two Envelopes, Two Stamps
*Day 4 — Friday, February 6, 2026 (dayOffset 4)*

The two proceedings announce themselves in different paper stocks, different return addresses, different typefaces — the bureaucracy's way of saying what Ms. Ndiaye said in words: these are not the same case wearing two coats.

You buy two folders. The colors will matter at 2 a.m. more than any filing system: blue for the Bureau, manila for the court, and never the twain at the wrong hearing.

**Choices:**
- Carry the page to its file → **tw_b**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the record)_
  - NOTE (shown after choosing): Dated, copied, filed — the chain holds.
- Trust the conversation to carry it → **tw_b**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [tw_b] The Calendar Gets Two Colors
*Day 5 — Saturday, February 7, 2026 (dayOffset 5)*

The board's two columns get their colors, and the dates sort themselves by peril: May 3 alone in its season on the blue side; the case's reviews spread across the manila year like ordinary weather.

Peril, color-coded, is just planning. Uncolored, it was panic. The board is already earning its wall.

**Choices:**
- Carry the page to its file → **appeal_week**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the record)_
  - NOTE (shown after choosing): Dated, copied, filed — the chain holds.
- Trust the conversation to carry it → **appeal_week**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [appeal_week] Appeal Week
*Day 6 — Sunday, February 8, 2026 (dayOffset 6)*

The appeal letter is the library's half-page: name, report number, amend or expunge. It feels — as it always feels — too small to hold a man's working life, his clearances for every school building in the district riding on a registry he has never seen.

Your sister, who kept Arantxa that Saturday until the boiler room, watches you seal it and asks the practical question: 'And the case?' Both, you tell her. In order. The appeal this week because it expires; the case every week because it matters.

**Choices:**
- Mail the appeal this week, stamped copy filed, clocks calendared → **appeal_filed134**  _(cash −10 ; FLAG: appealFiled ; HIDDEN + Indicated-report appeal filed in the first week of the window)_
  - NOTE (shown after choosing): Day 10 of 90. The perishable is preserved.
- Focus on the case first — the appeal can wait until the spring review settles → **end_case_only**
  - NOTE (shown after choosing): It cannot, and this is where that discovery gets made, at leisure, in May.

## [appeal_filed134] Filed, and the Case Goes On
*Day 10 — Thursday, February 12, 2026 (dayOffset 10)*

With the appeal docketed, the case resumes its own rhythm: Arantxa is home under the plan — this case never took her, a fact worth remembering when the two files blur at 2 a.m. — with services, a safety plan for work emergencies, and reviews on the court's calendar, not the Bureau's.

The safety plan's coverage roster is your sister, the super's wife (a retired aide), and the neighbor — the Saturday problem answered in advance, in signatures.

**Choices:**
- Build the work-emergency roster in signatures and file it with the plan → **records134**  _(cash −5 ; FLAG: rosterSigned ; HIDDEN + Work-emergency coverage roster signed and filed)_
  - NOTE (shown after choosing): The Saturday that started this now has a documented answer for every future Saturday.
- Everyone knows the arrangement — signatures are bureaucracy → **records134**
  - NOTE (shown after choosing): Bureaucracy is the genre the plan is published in. Sign it.

## [records134] The Record, Requested
*Day 20 — Sunday, February 22, 2026 (dayOffset 20)*

You request the case record in writing (55 Pa. Code § 3130.44(d)) — the dependency mirror — and, in the same week, note what the appeal will separately compel: the investigation evidence itself, under the appeal's own rule. Two mirrors, two buildings, two requests.

What the case record holds is mostly fair. What matters is a cross-reference in the investigation summary: 'see facilities log, Saturday.' A log you did not know had been consulted. Logs have authors. Authors can be asked for copies.

**Choices:**
- Request the facilities log through counsel, in writing, this week → **rc_a**  _(cash −5 ; FLAG: recordsRequested ; HIDDEN + Dependency record requested under § 3130.44(d); facilities log requested)_
  - NOTE (shown after choosing): The summary cited a document. Documents can be summoned.
- The log is the school's business — leave it to the lawyers' timeline → **rc_a**
  - NOTE (shown after choosing): It is now your business; it was cited against you. Timelines, however, are how citations retire.

## [rc_a] Reading the Mirror's Margins
*Day 24 — Thursday, February 26, 2026 (dayOffset 24)*

The record's margins are where its honesty lives: the investigator's initials, the supervisor's one-line concurrence, the cross-reference to the facilities log tucked into a footnote's posture — cited, but minimized, the way files minimize what they cannot omit.

Minimized citations are still citations. The footnote is now the most important line in the mirror, and it knows it.

**Choices:**
- Carry the page to its file → **rc_b**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the record)_
  - NOTE (shown after choosing): Dated, copied, filed — the chain holds.
- Trust the conversation to carry it → **rc_b**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [rc_b] Counsel Asks for the Log
*Day 29 — Tuesday, March 3, 2026 (dayOffset 29)*

The request for the logbook goes out on counsel's letterhead, addressed to the district, citing the investigation's own citation — a request that is, formally, unanswerable with no: the agency relied on the document; the appellant may read it.

Five business days later, the facilities office calls. Clerks recognize clerks' paper being honored, and they cooperate with historians.

**Choices:**
- Carry the page to its file → **logbook**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the record)_
  - NOTE (shown after choosing): Dated, copied, filed — the chain holds.
- Trust the conversation to carry it → **logbook**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [logbook] Two Phone Calls
*Day 34 — Sunday, March 8, 2026 (dayOffset 34)*

The superintendent's logbook page for that Saturday is a clerk's masterpiece of indifference: furnace alarm 8:51; Zubia on site 9:02; 'called H. — daughter with sister, ETA agreed' — your call to the super at 9:04, arranging Arantxa's coverage before the boiler room; and at 11:47, 'H. called — leaving, sister has girl.' Two calls. Both logged. Neither in the summary.

The summary's version — a child left in an industrial space — required those two calls not to exist. They exist in a spiral notebook in a facilities office, in handwriting, with times. This is the appeal's spine, and it was never hidden. It was merely never asked for.

**Choices:**
- Index the logbook page as the appeal's centerpiece, copy filed in both tracks → **lg_a**  _(FLAG: logbookFiled ; HIDDEN + Superintendent's logbook page obtained and filed in both tracks)_
  - NOTE (shown after choosing): 9:04 and 11:47. The whole appeal will hang on two times a clerk wrote down without caring.
- Keep the logbook for the hearing — let them commit to the summary first → **lg_a**
  - NOTE (shown after choosing): They already committed, in writing, months ago. Filed paper testifies longer than surprises.

## [lg_a] The Super's Handwriting
*Day 38 — Thursday, March 12, 2026 (dayOffset 38)*

Mr. Zubia's handwriting is the handwriting of a man who has logged thirty years of furnaces: block capitals for events, cursive for people, times to the minute because boilers taught him minutes matter.

Your two calls sit in the cursive, timed in the capitals' discipline. The page is a small masterpiece of a mind that believed records were for later. Later has arrived.

**Choices:**
- Carry the page to its file → **lg_b**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the record)_
  - NOTE (shown after choosing): Dated, copied, filed — the chain holds.
- Trust the conversation to carry it → **lg_b**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [lg_b] Copies, Plural
*Day 43 — Tuesday, March 17, 2026 (dayOffset 43)*

The page is copied three ways at the district office copier: the appeal's, the case's, and the one for the super's own file, at his request — he has decided his logbook is a document of record and intends to keep treating it that way.

Redundancy, practiced by everyone the paper touches, is how single pages survive to win hearings.

**Choices:**
- Carry the page to its file → **intake_note**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the record)_
  - NOTE (shown after choosing): Dated, copied, filed — the chain holds.
- Trust the conversation to carry it → **intake_note**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [intake_note] The Intake Note's Own Correction
*Day 48 — Sunday, March 22, 2026 (dayOffset 48)*

The investigation's intake note — obtained with the appeal's evidence packet, which the agency must provide, including the potentially exculpatory, within ten days of the scheduling order (23 Pa.C.S. § 6341(c.2)(4)) — contains the report's first form: 'child at father's workplace, supervised by father and super, per caller.'

Somewhere between the intake note and the indicated summary, 'supervised by father and super' became 'left unsupervised.' The packet contains no document explaining the journey. Bureau hearings are where such journeys get explained, on the record, by their authors.

**Choices:**
- Build the exhibit set: intake note, logbook, summary — the journey, in three pages → **correction_addendum**  _(FLAG: evidenceReceived ; HIDDEN + Intake note obtained under § 6341(c.2)(4); exhibit set built)_
  - NOTE (shown after choosing): Three pages, one disappearance. The hearing will ask where the supervision went.
- Your testimony can walk the officer through the difference → **correction_addendum**
  - NOTE (shown after choosing): Testimony walks; exhibits stand still and get quoted. Build the standing kind.

## [correction_addendum] The Agency Corrects Itself
*Day 62 — Sunday, April 5, 2026 (dayOffset 62)*

Spring brings the document you did not request and will never give back: the agency's correction addendum to the investigation file, noting that the logbook 'was reviewed subsequent to the summary' and that the summary 'should be read with' the log. Bureaucratese, translated: the paper trail now contradicts the summary inside the agency's own file.

Ms. Ndiaye labels it Exhibit 1. 'Not the logbook,' she says. 'The addendum. Anybody can keep a log. An agency correcting itself is the rarest exhibit in the building.'

**Choices:**
- Make the addendum Exhibit 1 and the logbook Exhibit 2 — their correction leads → **spring_review134**  _(FLAG: addendumFiled ; HIDDEN + Agency correction addendum obtained and made Exhibit 1)_
  - NOTE (shown after choosing): Their own file, correcting their own summary. The burden is about to get heavy — for its owner.
- Lead with the logbook — it's the most human document → **spring_review134**
  - NOTE (shown after choosing): Human loses to official inside official buildings. The addendum is the agency's white flag in its own handwriting.

## [spring_review134] The Case's Spring Review
*Day 76 — Sunday, April 19, 2026 (dayOffset 76)*

The dependency review, in its own building on its own clock, reads the plan's ordinary excellence: services attended, roster signed and once used (a February furnace, a documented Saturday), Arantxa thriving in the first grade two streets from your sister's.

The judge asks about the 'other matter' and Ms. Ndiaye answers in the formula the two-column board made possible: 'Litigating in its own forum, on its own clock, Your Honor. Ahead of schedule in both.' The review continues the case toward a fall closing review — the tracks converging, at last, on a season instead of a collision.

**Choices:**
- Do the paper version: dated, copied, filed → **sr_a**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the case record)_
  - NOTE (shown after choosing): Another dated page joins the folder.
- Handle it with a conversation and move on → **sr_a**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [sr_a] The Addendum's Arrival
*Day 80 — Thursday, April 23, 2026 (dayOffset 80)*

The correction addendum arrives without a cover letter, in an envelope whose plainness is its own confession — agencies announce victories; they slip corrections under the door. It is dated, signed by a supervisor, and filed in the investigation record as an amendment, which means the file now formally disagrees with itself.

Files that disagree with themselves are the appellant's best friends. This one gets a tab of its own.

**Choices:**
- Carry the page to its file → **sr_b**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the record)_
  - NOTE (shown after choosing): Dated, copied, filed — the chain holds.
- Trust the conversation to carry it → **sr_b**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [sr_b] Reading It Twice
*Day 85 — Tuesday, April 28, 2026 (dayOffset 85)*

You read the addendum twice at the kitchen table: once for what it concedes (the logbook postdates the summary; the summary should be read with it) and once for what it does not (no apology, no amended finding — the Bureau's process still required, its burden still unmet).

Concessions without conclusions are the normal currency of spring. Conclusions are minted at hearings, from concessions.

**Choices:**
- Carry the page to its file → **exhibit_one**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the record)_
  - NOTE (shown after choosing): Dated, copied, filed — the chain holds.
- Trust the conversation to carry it → **exhibit_one**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [exhibit_one] Exhibit One, Framed
*Day 90 — Sunday, May 3, 2026 (dayOffset 90)*

The appeal packet is assembled the way the library's packets are: exhibits numbered, the addendum first, a one-page chronology signed by you and the super both — his signature obtained with a visit, a copy of his own logbook page, and the observation that clerks' handwriting has ended more arguments than lawyers'.

He signs with the air of a man whose record-keeping has been vindicated by history, which it has.

**Choices:**
- File the packet with the Bureau and a copy in the case record → **ex_a**  _(cash −10 ; FLAG: appealPacket ; HIDDEN + Appeal packet filed with the correction addendum as Exhibit 1)_
  - NOTE (shown after choosing): Filed in both buildings. Corridors walked. The hearing is now a reading.
- File with the Bureau only — the case file doesn't need appeal paper → **ex_a**
  - NOTE (shown after choosing): It needs exactly this paper; the fall review will ask what the Bureau decided and why.

## [ex_a] The Chronology, Co-Signed
*Day 100 — Wednesday, May 13, 2026 (dayOffset 100)*

The one-page chronology — alarm, arrival, the two calls, the sister, the departure — is drafted from the logbook and the intake note alone, no memory admitted, so that every line can be footnoted to a document the agency or the district already holds.

Chronologies built only from their paper are nearly unarguable. The super signs his footnote's worth with a clear conscience and a borrowed pen.

**Choices:**
- Carry the page to its file → **ex_b**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the record)_
  - NOTE (shown after choosing): Dated, copied, filed — the chain holds.
- Trust the conversation to carry it → **ex_b**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [ex_b] The Packet's Weight
*Day 115 — Thursday, May 28, 2026 (dayOffset 115)*

The assembled packet is thinner than the year's fear suggested: eleven pages, three exhibits, one chronology. Thin packets win paper cases because officers read all of them; thick ones get sampled.

It is filed with the Bureau, copied to the case record, and logged on the board in both colors — the corridor's traffic, made visible.

**Choices:**
- Carry the page to its file → **bureau_prep**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the record)_
  - NOTE (shown after choosing): Dated, copied, filed — the chain holds.
- Trust the conversation to carry it → **bureau_prep**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [bureau_prep] June's Quiet Work
*Day 130 — Friday, June 12, 2026 (dayOffset 130)*

June is the corridor month: the hearing set for Friday, July 10, 2026; the case's services completing on schedule; Arantxa's school year ending with a folder of first-grade evidence that no proceeding requested and the family keeps anyway.

Preparation is the library's June liturgy: the likely questions, each answered by an exhibit before it is answered by a voice; the closing, drafted short; the burden, memorized — theirs, substantial evidence, § 6341(c.2)(5).

**Choices:**
- Prepare the closing around three exhibits and one standard → **bp_a**  _(FLAG: closingReady ; HIDDEN + Hearing preparation completed against the exhibit set)_
  - NOTE (shown after choosing): Three exhibits, one standard, no adjectives. Ready.
- Prepare to tell the whole Saturday, start to finish → **bp_a**
  - NOTE (shown after choosing): Whole Saturdays are how witnesses wander. The exhibits tell it; you confirm it.

## [bp_a] The Officer's Questions, Rehearsed
*Day 136 — Thursday, June 18, 2026 (dayOffset 136)*

The likely questions are rehearsed against the exhibits: When did you arrive? (The log.) Who had the child? (The calls, the sister, the intake note's first form.) Why does the summary differ? (The addendum's question to answer, not yours.)

Each answer is a page number before it is a sentence. Witnesses who answer in page numbers are believed in proportion.

**Choices:**
- Carry the page to its file → **bp_b**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the record)_
  - NOTE (shown after choosing): Dated, copied, filed — the chain holds.
- Trust the conversation to carry it → **bp_b**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [bp_b] June, in the Case's Column
*Day 146 — Sunday, June 28, 2026 (dayOffset 146)*

The manila column keeps its own June: services completing, Arantxa's school year closing, the roster's summer version signed — the case advancing on its merits while the appeal ripens beside it, neither starved by the other's season.

Two proceedings, fed in parallel, all spring. This is what the board was for.

**Choices:**
- Carry the page to its file → **bureau134**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the record)_
  - NOTE (shown after choosing): Dated, copied, filed — the chain holds.
- Trust the conversation to carry it → **bureau134**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [bureau134] Friday, July 10
*Day 158 — Friday, July 10, 2026 (dayOffset 158)*

The hearing officer opens the agency's file and finds its own correction filed as the appellant's first exhibit — a geometry no cross-examination can straighten. The agency's witness walks the journey from intake note to summary and cannot produce the page where the supervision went.

The super testifies for eleven minutes, mostly about handwriting. The logbook's times — 9:04, 11:47 — enter the transcript through the least dramatic witness in the building's history, which is precisely their power.

**Choices:**
- Close on the burden and the addendum: their standard, their file, their correction → **decision134**
  - NOTE (shown after choosing): The closing writes itself; you just read the file back to its owners.
- Close on your credibility — a father's word against a summary → **end_split134**
  - NOTE (shown after choosing): Credibility contests are coin flips the burdened side loves. The paper was the case; abandoning it at the closing table loses what the exhibits won.

## [decision134] Day 31
*Day 189 — Monday, August 10, 2026 (dayOffset 189)*

The decision — inside the 45 days the rule allows (23 Pa.C.S. § 6341(c.3)) — amends the report to unfounded. The registry releases its hold on your clearances; the district's facilities office gets its boiler man back without an asterisk.

Ms. Ndiaye's caution arrives with the champagne of the moment still unopened: 'The appeal is won. The case is not the appeal. The fall review closes the case, and it will read what we file this fall — not what the Bureau decided.' Two columns, to the very end.

**Choices:**
- File the expungement in the dependency record the same week → **dc_a**  _(FLAG: expungementFiled ; HIDDEN + Expungement order filed in the dependency case record)_
  - NOTE (shown after choosing): The corridor, walked one last time. Paper does not travel alone.
- The court will learn the outcome through channels → **dc_a**
  - NOTE (shown after choosing): Channels summarize. File the order.

## [dc_a] The Letter, Opened Standing Up
*Day 190 — Tuesday, August 11, 2026 (dayOffset 190)*

The decision is opened standing at the mailbox, read twice before the walk back — amended to unfounded, the reasoning tracking the exhibits in order, the addendum quoted in the agency's own words against its own summary.

Eleven pages, three exhibits, one standard. The boiler room's Saturday is now, officially, what the logbook always said it was.

**Choices:**
- Carry the page to its file → **corridor_last**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the record)_
  - NOTE (shown after choosing): Dated, copied, filed — the chain holds.
- Trust the conversation to carry it → **corridor_last**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [corridor_last] The Corridor, Walked Last
*Day 191 — Wednesday, August 12, 2026 (dayOffset 191)*

The stamp lands. The dependency file now contains the Bureau's answer in full — the fall review's reader will meet the expungement as a document, not a rumor, and will meet Exhibit 1's lesson with it: this family's paper was checked against its sources and held.

What remains is the fall packet: the case's own closing argument, built the case's way — services, roster, school, the plan's completion in dates.

**Choices:**
- Do the paper version: dated, copied, filed → **fall_a**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the case record)_
  - NOTE (shown after choosing): Another dated page joins the folder.
- Handle it with a conversation and move on → **fall_a**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [fall_a] Services, Complete
*Day 195 — Sunday, August 16, 2026 (dayOffset 195)*

The plan's services complete in September with certificates filed on their dates — the parenting course, the safety-planning series, the home assessment's final visit signed off with a note about the Saturday shelf of labeled emergency supplies that made the assessor laugh, once, in writing.

Laughter in an assessment note is filed like anything else. It testifies.

**Choices:**
- Index the completions into the fall packet as they land → **fa_a**  _(FLAG: servicesDone ; HIDDEN + Plan services completed and indexed)_
  - NOTE (shown after choosing): Completion, dated, indexed. The packet assembles itself from the year's habits.
- Certificates can be gathered at the end — that's what packets are → **fa_a**
  - NOTE (shown after choosing): Gathered-at-the-end is how certificates become 'to be provided.' Index as they land.

## [fa_a] The Safety Shelf
*Day 198 — Wednesday, August 19, 2026 (dayOffset 198)*

The home assessment's final visit notes the labeled Saturday shelf — the emergency supplies, the roster's laminated copy, the sister's number in three places — and the assessor's laugh becomes, in the fall packet, a documented professional judgment that this home has metabolized its worst day into a system.

Systems are what assessments exist to find. This one was built out of a Saturday.

**Choices:**
- Carry the page to its file → **fa_b**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the record)_
  - NOTE (shown after choosing): Dated, copied, filed — the chain holds.
- Trust the conversation to carry it → **fa_b**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [fa_b] Completions, Landing Monthly
*Day 201 — Saturday, August 22, 2026 (dayOffset 201)*

The certificates arrive across September like the year's report cards: course, series, assessment — each filed the week it lands, each indexed in the fall packet's growing table, so October's assembly is an act of collation rather than archaeology.

Archaeology is for cases that filed in the fall what they earned in the spring. This family filed monthly, and October is clerical.

**Choices:**
- Carry the page to its file → **fall_prep134**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the record)_
  - NOTE (shown after choosing): Dated, copied, filed — the chain holds.
- Trust the conversation to carry it → **fall_prep134**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [fall_prep134] The Fall Packet
*Day 205 — Wednesday, August 26, 2026 (dayOffset 205)*

The fall packet mirrors the appeal packet's discipline in the case's own dialect: chronology first, completions second, the roster and its one documented use third, the expungement order where the judge will meet it without asking.

It is, in form, the same book as July's, translated: in the appeal, the agency's paper defeated the agency's summary; here, the family's paper simply is the family's summary — accurate because it was assembled monthly, not remembered in October.

**Choices:**
- File the fall packet two weeks before the closing review → **fall_b**  _(cash −10 ; FLAG: fallPacket ; HIDDEN + Fall closing packet assembled and filed early)_
  - NOTE (shown after choosing): Early, indexed, complete. The review is now a reading.
- File it the week of the review — fresher facts → **fall_b**
  - NOTE (shown after choosing): Facts don't freshen in folders. They just arrive late to the judge's reading.

## [fall_b] Ms. Ndiaye's Last Distinction
*Day 210 — Monday, August 31, 2026 (dayOffset 210)*

Over coffee she draws the two columns a final time and writes the year's lesson under both: the appeal was won by the agency's paper; the case will be closed by yours. 'People think these proceedings are about what happened,' she says. 'They are about what the file can prove happened, on the day somebody reads it.'

Arantxa, informed that the fall talking day is the last one, requests that her tablet be charged for it. Logistics of hope, handled.

**Choices:**
- Prepare your statement to match the packet, date for date → **fall_c**  _(FLAG: statementReady ; HIDDEN + Closing statement prepared against the fall packet)_
  - NOTE (shown after choosing): The witness and the book, agreeing. The year's last rehearsal.
- Prepare to finally say everything the year felt like → **fall_c**
  - NOTE (shown after choosing): The year felt like paper. Say the packet.

## [fall_c] The Sister's Page
*Day 215 — Saturday, September 5, 2026 (dayOffset 215)*

Your sister's one-page statement — the Saturdays, the roster, the February furnace executed exactly as signed — is the fall packet's final document, filed last because it was earned latest: the family's own addendum, correcting nothing, confirming everything.

She signs it at the boiler room door, where this began, with the super's pen. The building's stationery has a sense of humor, or history does.

**Choices:**
- File her statement and close the packet → **fall_review134**  _(FLAG: sisterFiled ; HIDDEN + Sister's corroborating statement filed)_
  - NOTE (shown after choosing): The packet closes the way the case opened: family, documented, on time.
- Her statement can be summarized in yours → **fall_review134**
  - NOTE (shown after choosing): Summaries are how sisters become hearsay. File the page.

## [fall_review134] The Closing Review
*Day 228 — Friday, September 18, 2026 (dayOffset 228)*

The fall review reads the year in twenty minutes. The expungement is in the file where you filed it; the completions are dated; the roster has its Saturday; the judge's questions are the questions the packet already answered, asked aloud so the record can hear them answered.

Ms. Ndiaye states the ask the two columns were built for: closure of the case, the expungement noted, the family's paper complete in both proceedings.

**Choices:**
- Ask for closure today, both proceedings complete, the record as filed → **end_dual**  _(REQUIRES FLAG: appealFiled ; REQUIRES FLAG: recordsRequested ; REQUIRES FLAG: fallPacket)_
  - NOTE (shown after choosing): Two columns, both closed. The board comes off the wall.
- Ask for one more review to be safe — the file is strong → **end_dual**
  - NOTE (shown after choosing): Strong files close. Extra reviews are how open cases collect new summaries.
- Thank the court and let it craft the order → **end_late134**
  - NOTE (shown after choosing): Loops back through courtesy into another season of openness. Propose the ending the paper earned.

## [end_dual] Ending — Both Columns Closed
*Day 235 — Friday, September 25, 2026 (dayOffset 235)*

The case closes at the fall review; the registry had already released you in August. You take the two-column page off the refrigerator and file it — where else — as the folder's last document, behind two closing orders that between them say the whole thing: unfounded, and closed.

Arantxa's school and yours both get their boiler-adjacent family back without annotation. The super asks, at the winter furnace check, whether you kept the logbook page. You did. Clerks' handwriting, framed by events, tends to get kept.

**Ending.**

**Debrief:**
- THE TWO PROCEEDINGS, AUDITED — Appeal: notified Monday, February 2, 2026; 90 days → Sunday, May 3, 2026 (23 Pa.C.S. § 6341(a)(2)); filed day 10. Evidence under § 6341(c.2)(4) produced the intake note; the record request (55 Pa. Code § 3130.44(d)) produced the logbook lead; the agency's burden (c.2)(5) failed against its own correction addendum; decision on day 31 of (c.3)'s 45. Case: services, roster, reviews, and a fall packet — closed on the family's paper, a season after the registry let go.
- WHY THE WIN REQUIRED TWO TRACKS — Neither proceeding could win the other. The dependency court never adjudicates the registry; the Bureau never closes a case. The capstone discipline was separation with a corridor: distinct burdens, distinct packets, and every decision physically carried into the other file. The gated route required **appealFiled**, **recordsRequested**, and **fallPacket** — the perishable filed, the mirror requested, and the closing book actually built.
- WHAT NO STRATEGY CONTROLS — A hearing officer, a superintendent's record-keeping habits, and a furnace. The route controlled the separation of the burdens and the summoning of the documents: the logbook existed all along, which is the scenario's whole thesis — decisive paper is usually already written, by someone else, waiting to be asked for.

## [end_split134] Ending — Expunged in One Building
*Day 189 — Monday, August 10, 2026 (dayOffset 189)*

In this branch the appeal is lost on credibility's coin flip — or the case is closed while the registry keeps its word — and the two columns close a season apart, one family's name cleared in one building and annotated in the other.

The split is survivable and instructive: the registry's answer can still be sought through reconsideration and the courts (23 Pa.C.S. § 6341(g) — reconsideration within 15 days of the mailing date; appeal within 30 days), clocks that run from mailing, not from the day the letter is opened. The corridor stays open. It is just longer than it needed to be.

**Ending.**

**Debrief:**
- THE SPLIT, AND THE DOOR LEFT IN IT — Section 6341(g) keeps a lost Bureau decision reviewable: reconsideration requested within 15 days of the decision's mailing date, and an appeal to the Commonwealth Court within 30 days. Both clocks run from mailing — the library's most unforgiving arithmetic, and the reason decisions are opened the day they arrive in winning households.
- WHAT NO STRATEGY CONTROLS — Coin-flip credibility calls, which are why the route refuses them: the exhibits (the agency's own addendum; a clerk's logbook) were built so no officer ever had to choose whose word to take. Abandoning the paper at the closing table re-opens the flip.

## [end_case_only] Ending — May 3, Unfiled
*Day 120 — Tuesday, June 2, 2026 (dayOffset 120)*

Sunday, May 3, 2026 passes in this branch the way unmarked deadlines do: quietly, on a weekend, while the case — the visible, serviced, reviewed case — proceeds in apparent health. The appeal window closes on a registry entry that will outlive the dependency case by years.

The case itself closes in the fall, a genuine success. The registry surfaces afterward, in clearance renewals, in the district's annual paperwork — a footnote with a man's name on it, renewed annually, appealable no longer. The two-column board exists to prevent exactly this: the healthy file hiding the expiring one.

**Ending.**

**Debrief:**
- THE PERISHABLE, UNPRESERVED — Notified February 2, 2026; 90 days → Sunday, May 3, 2026 (23 Pa.C.S. § 6341(a)(2)). The scenario's central trap is attention: a dependency case generates meetings, services, and paper weekly, while an appeal generates one deadline and silence. Everything urgent feels like the case. The appeal was the only item in either file that could not be continued, cured, or re-filed.
- WHAT NO STRATEGY CONTROLS — Nothing in this ending was weather. The window was known, dated, and drawn on the board in the route's first scene. Sequence is the strategy; this is the control case that proves it.

## [end_late134] Ending — Closed, Eventually
*Day 235 — Friday, September 25, 2026 (dayOffset 235)*

The case closes a season later than the paper earned — at a winter review nobody needed, on an order the court drafted in its own caution's image, with the respite and aftercare thinner than the family's actual arrangements.

Nothing was lost that paper protects; the registry was already clear, the goal never moved. What courtesy cost was a season and some ink — the system's standard tax on endings nobody proposes in writing.

**Ending.**

**Debrief:**
- THE TAX ON UNPROPOSED ENDINGS — Courts close cases on the orders in front of them. A family that arrives with a complete record and no proposed order gets the court's default craftsmanship: careful, slow, and thin where the family's paper was thick. The route's discipline — propose the ending, in writing, with the packet — exists because endings, like everything else in this library, are documents before they are events.
- WHAT NO STRATEGY CONTROLS — A judge's drafting pace. Everything else in this branch went right, which is its lesson: complete paper can still be taxed a season by an unwritten last page.
