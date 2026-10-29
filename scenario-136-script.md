# THE FIRST 90 DAYS — Scenario 136: “The Marathon File”

*Human-readable script. This document and `scenario-136.json` are generated from a single source and match node-for-node: same IDs, same order, same choices, same effects.*

**The family is fictional — a composite. No real person's story appears here.**

**Content note:** This scenario depicts a complex multi-track dependency case with an appeal and a kinship placement in another county. There is no graphic content. Players may skip any scene or use the quick exit at any time.

**How to read effects:** `cash −40` changes the player's cash. `FLAG: name` sets a flag the engine tracks. `HIDDEN + item` means the case file quietly records that item at this choice — the player does not see it when it happens. `REQUIRES FLAG: name` means the choice is only available if that flag was set earlier; `REQUIRES NO FLAG: name` means it is only available if that flag was never set. `NOTE:` is text shown to the player right after choosing.

Start date: Monday, June 2, 2025. Day offsets are days since the scenario's start date (the elder child's foster-care entry date).

## [start] The Longest Folder
*Day 0 — Monday, June 2, 2025 (dayOffset 0)*

Your name is Olatz. Peru, ten, entered care on Monday, June 2, 2025, after the night your blood pressure took you to the emergency room and the neighbor who called the ambulance could not stay past midnight. The twins, Bittor and Nahia, three, entered three weeks later — Monday, June 23 — when the hospital kept you for the surgery nobody had scheduled and the emergency kinship plan ran out of emergencies it could absorb.

You come home in July to an empty house and the thickest folder of your life. Your sister Odile, one county over, is already asking the kinship question. And in the folder's first section sits the letter that will outrank everything for ninety days: an indicated report, notice dated Monday, June 30, 2025, its appeal window (23 Pa.C.S. § 6341(a)(2)) closing Sunday, September 28, 2025. Your lawyer, Ms. Castellanos, opens the folder, reads the dates, and says the sentence this scenario is built to honor: 'This is a marathon. We will run it in the order the deadlines expire, not the order the feelings arrive.'

**Choices:**
- Accept the order: appeal first, kinship second, plan third, clocks always → **order136**  _(FLAG: orderAccepted ; HIDDEN + Marathon sequencing accepted: deadlines in expiry order)_
  - NOTE (shown after choosing): Expiry order. The feelings will be attended to — in writing, on schedule.
- The children come first — the paperwork can queue behind them → **order136**
  - NOTE (shown after choosing): The children are the paperwork's entire subject. Queueing it behind them is how they wait longer.

## [order136] The Board of Boards
*Day 7 — Monday, June 9, 2025 (dayOffset 7)*

The board Ms. Castellanos draws covers a full wall of her office: SILAS (entered Jun 2, 2025; fifteen months Wednesday, September 2, 2026), TWINS (entered Jun 23, 2025; fifteen months Wednesday, September 23, 2026), APPEAL (notified Jun 30, 2025; due September 28, 2025), KINSHIP (Odile, cross-county — two counties' paper for one spare room), PLAN (services, with a vendor problem she already suspects). Counsel is your right (42 Pa.C.S. § 6337); in a marathon, counsel is also the course map.

'Every scenario you have lived so far is inside this one,' she says, 'including the ones you haven't lived yet. We do them in order.'

**Choices:**
- Do the paper version: dated, copied, filed → **or_a**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the case record)_
  - NOTE (shown after choosing): Another dated page joins the folder.
- Handle it with a conversation and move on → **or_a**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [or_a] The Twins' Second Envelope
*Day 18 — Friday, June 20, 2025 (dayOffset 18)*

The twins' entry order arrives in the mail of a week already full of envelopes — June 23's date entering the board as the second permanency clock, three weeks behind Peru's, a stagger that will matter in the marathon's final month and is therefore recorded now, in June, while recording is cheap.

Staggers recorded early are strategies. Staggers discovered late are ambushes.

**Choices:**
- Carry the page to its file → **or_b**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the record)_
  - NOTE (shown after choosing): Dated, copied, filed — the chain holds.
- Trust the conversation to carry it → **or_b**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [or_b] The Notice
*Day 28 — Monday, June 30, 2025 (dayOffset 28)*

Monday, June 30: the indicated notice, read twice at the kitchen table of the house you have just come home to — the report from the hospital night, the finding written from midnight forward, the 90 days running to Sunday, September 28, 2025.

The board takes its third column. Ms. Castellanos, by phone, is brief: 'Eleven days. We file it in eleven days, and then we never think about the window again.'

**Choices:**
- Carry the page to its file → **appeal136**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the record)_
  - NOTE (shown after choosing): Dated, copied, filed — the chain holds.
- Trust the conversation to carry it → **appeal136**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [appeal136] Day Eleven
*Day 39 — Friday, July 11, 2025 (dayOffset 39)*

The appeal goes out on day 11 of 90 — the half-page, the stamped copy, the calendar annotated with the Bureau's future: evidence, hearing, decision. It is deliberately unglamorous. Marathons are not won in the first mile, but they are most often lost there, to the runner who decided the first mile was beneath her.

Odile, watching the envelope go, begins her own folder that evening. The family's paper gene, Ms. Castellanos will later testify socially, is dominant.

**Choices:**
- Mail it, log the Bureau's clocks, and turn to the kinship file → **kinship136**  _(cash −10 ; FLAG: appealFiled ; HIDDEN + Indicated-report appeal filed on day 11 of the window)_
  - NOTE (shown after choosing): Mile one, run properly. The wall of dates loses its most perishable entry.
- Polish the appeal another week — first filings deserve care → **end_registry136**
  - NOTE (shown after choosing): Care is a virtue with a deadline. This branch discovers which one wins.

## [kinship136] Odile's County, Odile's Paper
*Day 45 — Thursday, July 17, 2025 (dayOffset 45)*

The kinship study for a caregiver in another county runs on two counties' rails: her home county's clearances and home study, your children's county's approval and placement paperwork, and a courier's worth of documents that must exist in both files, identical, or be treated as existing in neither.

A child being cared for by a relative stands inside the permanency clock's own exceptions (42 U.S.C. § 675(5)(E)) — but the placement must be real on paper in both counties before it is real in the children's lives. Odile's spare room is forty minutes away and, administratively, in another country.

**Choices:**
- Itemize the cross-county study in writing with both counties' workers, item by item → **kn_a**  _(cash −5 ; FLAG: studyList ; HIDDEN + Cross-county kinship study itemized in writing with both counties)_
  - NOTE (shown after choosing): Two counties, one checklist, no item owned by 'the other office.'
- Let the counties coordinate — that's their machinery → **kn_a**
  - NOTE (shown after choosing): Their machinery coordinates the way weather coordinates picnics. Itemize it yourself.

## [kn_a] Odile's First Checklist
*Day 52 — Thursday, July 24, 2025 (dayOffset 52)*

Odile's checklist, drawn with her county's kinship worker, lists what a spare room must become on paper: clearances for her household, the home visit, the training, the references — each with the other county's counterpart noted beside it, because every item in this study exists twice or not at all.

She works the list the way she has run a household for forty years: top to bottom, in pencil, with dates.

**Choices:**
- Carry the page to its file → **study136**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the record)_
  - NOTE (shown after choosing): Dated, copied, filed — the chain holds.
- Trust the conversation to carry it → **study136**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [study136] The Plan's Vendor Problem
*Day 60 — Friday, August 1, 2025 (dayOffset 60)*

Your services plan requires a specialized parenting program with exactly one vendor in the region — whose waitlist, the record will eventually show, ran four months that summer. The plan was signed in July. The enrollment letter is dated November. Between those dates, on the file's face, sits a mother apparently doing nothing.

You are not doing nothing. You are waitlisted, attending everything else, and — if the marathon's discipline holds — generating the dated paper that will later prove whose queue the season belonged to.

**Choices:**
- Get the waitlist position in writing from the vendor, dated, and file it → **vendor_letter**  _(cash −5 ; FLAG: waitlistDocumented ; HIDDEN + Vendor waitlist position documented in writing and filed)_
  - NOTE (shown after choosing): The queue, in writing, with a date. November's enrollment will read very differently beside July's letter.
- The agency knows about the waitlist — everyone does → **vendor_letter**
  - NOTE (shown after choosing): Everyone knowing is how it becomes no one's document. Get the letter.

## [vendor_letter] The Records, All of Them
*Day 78 — Tuesday, August 19, 2025 (dayOffset 78)*

The record request goes in writing (55 Pa. Code § 3130.44(d)) — and in this case, there are effectively three records to mirror: Peru's, the twins', and the study file growing one county over. You request what's yours, Odile requests what's hers, and counsel reconciles the three against the board.

What the mirrors show is mostly a system working at its ordinary speed — which is to say, too slowly for childhood, and documenting its own pace as it goes. The pace, documented, becomes the case's most useful exhibit: the services-not-provided exception writes itself out of the agency's own dates, if someone assembles them.

**Choices:**
- Assemble the pace exhibit: plan dates against service dates, per child → **vd_a**  _(cash −5 ; FLAG: recordsRequested ; HIDDEN + Case records requested under § 3130.44(d); plan-vs-service pace exhibit assembled)_
  - NOTE (shown after choosing): Their dates, your assembly. The marathon's central document is a table of the system's own calendar.
- Request Peru's record now and the twins' later → **vd_a**
  - NOTE (shown after choosing): Later is how one child's mirror ends up nine months staler than another's — in a case where the children share a hearing.

## [vd_a] Everything Else, Enrolled
*Day 84 — Monday, August 25, 2025 (dayOffset 84)*

While the vendor's queue holds the plan's centerpiece, everything else enrolls and runs: the health follow-ups from your surgery, the family sessions the agency runs in-house, the visitation cadence at two placements — a Plan B executed so completely that the file's only blank wears the vendor's name.

Completeness around a documented gap is the gap's best frame. The frame is built weekly, on time.

**Choices:**
- Carry the page to its file → **vd_b**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the record)_
  - NOTE (shown after choosing): Dated, copied, filed — the chain holds.
- Trust the conversation to carry it → **vd_b**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [vd_b] The Queue, Reconfirmed
*Day 90 — Sunday, August 31, 2025 (dayOffset 90)*

The waitlist letter is reconfirmed in September — position, movement, the vendor's own projection — because a July letter describing a queue is evidence; a July letter plus a September update is a record of the queue itself.

Queues keep moving or keep stalling; either way, dated paper knows which.

**Choices:**
- Carry the page to its file → **pace136**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the record)_
  - NOTE (shown after choosing): Dated, copied, filed — the chain holds.
- Trust the conversation to carry it → **pace136**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [pace136] The Appeal's Evidence
*Day 98 — Monday, September 8, 2025 (dayOffset 98)*

The Bureau's scheduling order triggers the agency's evidence duty: all evidence gathered in the investigation relevant to the determination, including the potentially exculpatory, within ten days (23 Pa.C.S. § 6341(c.2)(4)). The packet includes the ER's discharge timeline and the neighbor's statement — the neighbor who called the ambulance and stayed until midnight, whose account of a medical emergency reads nothing like the summary's 'failure to arrange care.'

The indicated finding was written from the midnight hour forward. The evidence packet preserves the day from the ambulance forward. Hearings are where timelines meet, and earlier usually beats louder.

**Choices:**
- Build the appeal exhibits around the day's timeline: ambulance, ER, neighbor, midnight → **pc_a**  _(FLAG: evidenceReceived ; HIDDEN + Investigation evidence obtained under § 6341(c.2)(4); timeline exhibit built)_
  - NOTE (shown after choosing): A day, in order, from primary paper. The summary's midnight-forward version is about to meet it.
- Your account of that night is the heart of the appeal → **pc_a**
  - NOTE (shown after choosing): Your account is the heart. The exhibits are the ribs that keep it standing under cross-examination.

## [pc_a] Three Mirrors, Reconciled
*Day 104 — Sunday, September 14, 2025 (dayOffset 104)*

The three records — Peru's, the twins', the study file's releasable pages — are reconciled against the board in October: dates agreed, two discrepancies found and filed as corrections, the pace exhibit's table verified line by line against primary pages.

Reconciliation is the marathon's least visible discipline and its most decisive: next year's hearings will meet one chronology, in three bindings, without a seam to pull.

**Choices:**
- Carry the page to its file → **pc_b**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the record)_
  - NOTE (shown after choosing): Dated, copied, filed — the chain holds.
- Trust the conversation to carry it → **pc_b**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [pc_b] The Pace Table, Drafted
*Day 111 — Sunday, September 21, 2025 (dayOffset 111)*

The pace table is drafted the way indictments and love letters are: plainly. Plan date, service date, days between, per child, per service — the system's year in arithmetic, requiring no adjectives because arithmetic doesn't accept them.

It will be filed without commentary. Tables this plain comment on themselves.

**Choices:**
- Carry the page to its file → **exhibits136**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the record)_
  - NOTE (shown after choosing): Dated, copied, filed — the chain holds.
- Trust the conversation to carry it → **exhibits136**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [exhibits136] Autumn Reviews
*Day 118 — Sunday, September 28, 2025 (dayOffset 118)*

The autumn reviews — one per docket, back to back — read a family visibly organizing itself: the appeal docketed, the study itemized and advancing on two counties' rails, the plan's everything-but-the-vendor complete or documented, the pace exhibit filed without drama.

Peru's judge delivers the season's sentence: 'The file reads like it is being kept by someone who expects it to be read.' It is the nicest thing a court has ever said about this family, and it is about the paperwork. The marathon accepts the compliment on the paperwork's behalf.

**Choices:**
- Do the paper version: dated, copied, filed → **wn_a**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the case record)_
  - NOTE (shown after choosing): Another dated page joins the folder.
- Handle it with a conversation and move on → **wn_a**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [wn_a] Winter: The Study's Middle
*Day 150 — Thursday, October 30, 2025 (dayOffset 150)*

The kinship study's middle months are a correspondence between two counties conducted at the speed of inter-office mail: Odile's home visit in November, her county's report in December, the children's county's questions in January — each leg dated in both files, because a study traveling between counties accrues exactly the delays its paper trail must later explain.

Delays with dates are process. Delays without them are suspicions. The study's folder prefers process.

**Choices:**
- Carry the page to its file → **wn_b**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the record)_
  - NOTE (shown after choosing): Dated, copied, filed — the chain holds.
- Trust the conversation to carry it → **wn_b**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [wn_b] Winter: Visits at Odile's
*Day 185 — Thursday, December 4, 2025 (dayOffset 185)*

Winter visits begin rotating through Odile's house — the placement rehearsing itself before it exists, the twins learning the spare room's geography, Peru annexing the garage workbench — documented by both counties' visit structures, reconciled monthly like everything else in this case.

Rehearsal visits are the kinship system's best idea. Documented, they become the placement's first chapter instead of its rumor.

**Choices:**
- Carry the page to its file → **wn_c**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the record)_
  - NOTE (shown after choosing): Dated, copied, filed — the chain holds.
- Trust the conversation to carry it → **wn_c**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [wn_c] Winter: The Plan's Other Half
*Day 210 — Monday, December 29, 2025 (dayOffset 210)*

Your own services' winter half completes in the in-house tracks: sessions attended, the health plan stabilized, the home-readiness assessment passed with the assessor noting the board of dates still on your kitchen wall, photographed into the report with something like respect.

The wall has become a character in the file. Characters with dates are believed.

**Choices:**
- Carry the page to its file → **study_travels**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the record)_
  - NOTE (shown after choosing): Dated, copied, filed — the chain holds.
- Trust the conversation to carry it → **study_travels**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [study_travels] The Study Completes — and Travels
*Day 230 — Sunday, January 18, 2026 (dayOffset 230)*

Odile's study completes in her county in the new year — and then must travel: certified into the children's county file, accepted, and converted into a placement approval, a journey of stamps that takes the exact number of weeks it takes, which is why the marathon started it in July.

The twins move to Odile's in February — Peru joining them for weekends and then, on the amended plan, for the school term's second half, the sibling group reassembled under one roof for the first time since June. A relative placement, documented in two counties. The clock's exception now has an address.

**Choices:**
- Get the study's acceptance in writing in the children's county file, dated → **kin_ready**  _(FLAG: kinReady ; HIDDEN + Cross-county kinship study accepted in writing; children placed with kin)_
  - NOTE (shown after choosing): Accepted, dated, filed in both counties. The exception has an address and a stamp.
- The placement itself proves the study — don't chase the stamp → **kin_ready**
  - NOTE (shown after choosing): Placements get questioned; stamps answer. Chase the stamp.

## [kin_ready] The Bureau Hearing
*Day 263 — Friday, February 20, 2026 (dayOffset 263)*

Friday, February 20, 2026. The agency must carry its burden — substantial evidence that the report should remain indicated (23 Pa.C.S. § 6341(c.2)(5)) — with a summary written from midnight forward, against an appellant's timeline written from the ambulance forward, sourced from its own evidence packet.

The neighbor testifies for nine minutes. The ER timeline is four. The hearing officer asks the agency's witness when the summary's author last read the neighbor's statement, and the transcript preserves a silence of the length that wins appeals.

**Choices:**
- Close on the timeline and the burden: their standard, their packet, your day → **appeal_decision136**
  - NOTE (shown after choosing): A day in order beats a summary in adjectives. Close on the paper.
- Close on the children and the year this entry has cost them → **appeal_decision136**
  - NOTE (shown after choosing): True, and not the standard. The officer must apply the standard; give her the paper that satisfies it.

## [appeal_decision136] Expunged, Mid-Marathon
*Day 285 — Saturday, March 14, 2026 (dayOffset 285)*

The decision — within the 45 days the rule allows (23 Pa.C.S. § 6341(c.3)) — amends the report to unfounded, entered with most of the marathon still to run. The children's-file reader will meet a mother whose report was examined and expunged, because the order will be carried into both dependency files by hand, the way all paper in this family travels: deliberately.

What remains is the permanency year: two clocks (September 2 and September 23, 2026), a kinship placement holding, a vendor's program finally enrolling you in its spring cohort, and a services record whose gaps all have the system's name on them.

**Choices:**
- File the expungement in both children's files with a cover note → **spring136**  _(FLAG: expungementFiled ; HIDDEN + Expungement order filed in both dependency files)_
  - NOTE (shown after choosing): Mile twenty, run like mile one. The corridor is the course.
- The courts read each other's outcomes eventually → **spring136**
  - NOTE (shown after choosing): Eventually is the marathon's enemy in a sash. File it this week.

## [spring136] Spring: The Vendor's Cohort
*Day 300 — Sunday, March 29, 2026 (dayOffset 300)*

The vendor's program — the plan's last open service — enrolls you in March, eight months after the plan signed for it, with the waitlist letter from July already in the file explaining exactly whose eight months those were. You attend like a woman with a September deadline and a folder to feed: perfectly, documentedly.

Completion lands in June. The certificate is filed beside the waitlist letter, the two documents bookending the plan's longest gap with the system's name on both covers.

**Choices:**
- File the completion beside the waitlist letter — the gap, bookended → **sp_a**  _(FLAG: servicesDone ; HIDDEN + Vendor program completed; certificate filed beside the waitlist letter)_
  - NOTE (shown after choosing): Bookended. Any future reader meets the explanation before the gap.
- File the certificate alone — completion speaks for itself → **sp_a**
  - NOTE (shown after choosing): Completion speaks. The gap, unbookended, speaks louder.

## [sp_a] The Cohort's Middle Weeks
*Day 315 — Monday, April 13, 2026 (dayOffset 315)*

The vendor program's middle weeks run through April and May with the attendance the waitlist letter promised you'd bring: perfect, documented, unremarkable in the way of all decisive things — the plan's last service converting from the file's biggest blank into its most ordinary page.

Ordinariness, at month eleven, is the sound of a case closing in on its answer.

**Choices:**
- Carry the page to its file → **sp_b**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the record)_
  - NOTE (shown after choosing): Dated, copied, filed — the chain holds.
- Trust the conversation to carry it → **sp_b**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [sp_b] Odile's Second Folder
*Day 332 — Thursday, April 30, 2026 (dayOffset 332)*

Odile opens the second folder — the support folder, for the placement's conversion to standing kinship support after the trial — with the same pencil discipline as the first, in both counties' formats, because a conversion documented in advance is a hearing's shortest agenda item.

The family's paper gene, dominant as charged, expresses itself one final time: the ending, pre-filed.

**Choices:**
- Carry the page to its file → **packets136**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the record)_
  - NOTE (shown after choosing): Dated, copied, filed — the chain holds.
- Trust the conversation to carry it → **packets136**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [packets136] The Packets, Per Child
*Day 350 — Monday, May 18, 2026 (dayOffset 350)*

Summer's assembly: an exception packet per child — Peru's, the twins' (theirs shared where the law shares it, separate where the dates divide) — each holding the relative-care documentation (Odile's approved, accepted, two-county placement), the compelling-reason case-plan language requested in writing, and the pace exhibit's per-child table: services identified, services provided, the difference dated and owned.

Three packets, two clocks, one hearing season. The marathon's last miles are run at a desk, which is where marathons in this library are always actually run.

**Choices:**
- File the packets and the case-plan language request together, per child → **plan_entries136**  _(cash −10 ; FLAG: packetBuilt ; HIDDEN + Per-child exception packets assembled; compelling-reason plan language requested)_
  - NOTE (shown after choosing): Per child, in writing, in the plan. The statute reads plans; the packets make sure the plans say it.
- One family packet tells the story better → **plan_entries136**
  - NOTE (shown after choosing): Stories lose to arithmetic at fifteen months. Packets are counted per child because children are.

## [plan_entries136] The Plan Entries Land
*Day 385 — Monday, June 22, 2026 (dayOffset 385)*

The case-plan amendments enter in their per-child forms: relative care, noted; compelling reason, written in the plans' own language — reunification trajectory documented, trial return proposed for the late summer; services gaps, recorded with their owners' dates. The exceptions now exist in the only place the statute reads for them.

Ms. Castellanos walks the wall of dates one final time and takes down September 28, 2025's card — the appeal, long resolved — leaving the two September 2026 dates standing. 'Two dates,' she says. 'Three children, two dates, one family. Bring me the summer without a surprise in it.'

**Choices:**
- Run the summer on the plan: visits expanding at Odile's, trial steps dated → **pe_a**  _(FLAG: planEntered ; HIDDEN + Exception language entered in both children's case plans)_
  - NOTE (shown after choosing): The plans now say, in writing, what the year has been proving. Summer, run on rails.
- Summer can breathe a little — the heavy paper is done → **pe_a**
  - NOTE (shown after choosing): Summers that breathe produce autumn surprises. The marathon's last miles are still miles.

## [pe_a] The Amendments, Read Back
*Day 395 — Thursday, July 2, 2026 (dayOffset 395)*

The amended plans are read back to you at the summer's first review — relative care, compelling reason, the gaps' owners' dates, all in the plans' own sentences now — and you initial each page the way litigants initial settlements: slowly, as someone who knows what sentences cost.

Initialed plans are the exceptions' legal address. The statute reads plans. These now say it.

**Choices:**
- Carry the page to its file → **pe_b**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the record)_
  - NOTE (shown after choosing): Dated, copied, filed — the chain holds.
- Trust the conversation to carry it → **pe_b**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [pe_b] Two Counties, Notified
*Day 408 — Wednesday, July 15, 2026 (dayOffset 408)*

The plan entries are certified into Odile's county file as well — the support clause's home county — so the conversion she has pre-filed meets plans that already describe it, in both buildings, before the hearing asks.

Paper that agrees with itself across county lines is the marathon's final luxury, purchased with a year of couriers.

**Choices:**
- Carry the page to its file → **summer136**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the record)_
  - NOTE (shown after choosing): Dated, copied, filed — the chain holds.
- Trust the conversation to carry it → **summer136**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [summer136] The Summer of the Trial
*Day 420 — Monday, July 27, 2026 (dayOffset 420)*

The trial return runs in stages across the summer: overnights at your home becoming weeks, Odile's converting — on paper, in both counties — from placement to the family's standing kinship support, the children's school enrollment settled in August in your district with her address as the documented backup.

The September dates approach in their order: Peru's fifteenth month on Wednesday, September 2, 2026; the twins' on Wednesday, September 23. Behind each date stands a plan entry, a packet, and a relative's documented home. The clocks will ask their question of a family that has been answering it, in installments, for fifteen months.

**Choices:**
- Propose the final order in writing: exceptions as documented, trial to convert, Odile's support in ink → **sm_a**  _(cash −5 ; FLAG: orderProposed ; HIDDEN + Final order proposed in writing with documented exceptions)_
  - NOTE (shown after choosing): Proposed, dated, per child. The hearing is a reading the family has already held at its own table.
- File for the vendor's program audit instead — its waitlist deserves a harder look → **end_petition136**
  - NOTE (shown after choosing): It does — in some other proceeding. Diverting the marathon at mile twenty-five is how petitions get drafted about you instead.

## [sm_a] August: Enrollment and Toothbrushes
*Day 430 — Thursday, August 6, 2026 (dayOffset 430)*

August is logistics elevated to evidence: school enrollment in your district completed early, Odile's address filed as the documented backup, toothbrushes resident in two houses by the children's own arrangement — the trial's paperwork indistinguishable, at last, from a family's ordinary administration.

Ordinary administration is the destination. The file's highest compliment, available only in August, is boredom.

**Choices:**
- Carry the page to its file → **sm_b**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the record)_
  - NOTE (shown after choosing): Dated, copied, filed — the chain holds.
- Trust the conversation to carry it → **sm_b**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [sm_b] The Binder's Last Pages
*Day 440 — Sunday, August 16, 2026 (dayOffset 440)*

The hearing binder's last pages are the summer's: trial logs, enrollment confirmations, the twins' preschool letters, Peru's workbench photograph (filed by Odile, annotated in pencil: 'his corner') — the marathon's evidence ending, as it began, with the children's lives rather than the system's forms.

The binder closes. What opens in September is a courtroom, and it will read.

**Choices:**
- Carry the page to its file → **hearing_prep136**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the record)_
  - NOTE (shown after choosing): Dated, copied, filed — the chain holds.
- Trust the conversation to carry it → **hearing_prep136**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [hearing_prep136] The Hearing, Prepared as a Reading
*Day 450 — Wednesday, August 26, 2026 (dayOffset 450)*

Preparation is the liturgy one last time: the pace exhibit refreshed, the plan entries certified from both counties, Odile's statement, the children's school pages, the expungement — the whole marathon, indexed, in three packets and one binder.

Ms. Castellanos's final instruction is the course map's first line, returned as a benediction: 'We ran it in the order the deadlines expired. Let the record show it.'

**Choices:**
- File the hearing binder a week early, in all three dockets → **hearing136**  _(FLAG: binderFiled ; HIDDEN + Hearing binder filed early in all three dockets)_
  - NOTE (shown after choosing): Early, everywhere, identical. The reading can begin.
- File it the morning of — the summer's facts are fresh → **hearing136**
  - NOTE (shown after choosing): Fresh facts, late paper. The court reads what was filed; the morning-of binder is a rumor with a cover.

## [hearing136] September 2, 2026
*Day 457 — Wednesday, September 2, 2026 (dayOffset 457)*

Peru's fifteenth month arrives as a hearing, which is what prepared-for fifteenth months become. The court works the packets: relative care, documented in two counties; the compelling reason, in the plans' own entries; the services pace, tabled from the agency's own dates — the exception for services identified but not provided, proved by the system's calendar rather than the mother's adjectives (42 U.S.C. § 675(5)(E)).

The filing question is asked and answered in the same hour, for Peru — and, the court notes for the record, the same documentation stands ready for the twins' date in three weeks. No petition is filed in any child's case. The goal never moved.

**Choices:**
- Ask for the final orders: trial converted, Odile's support in writing, closure set at the twins' review → **end_record_wins**  _(REQUIRES FLAG: recordsRequested ; REQUIRES FLAG: appealFiled ; REQUIRES FLAG: packetBuilt ; REQUIRES FLAG: kinReady)_
  - NOTE (shown after choosing): Asked on the first clock's day, with the second clock's answer already filed. The marathon ends the way it was run.
- Ask for immediate full closure of all three cases today → **end_mixed136**
  - NOTE (shown after choosing): The twins' clock runs three more weeks; closure today outruns their court's calendar. The best ending takes the dates in order — as it has all along.
- Let the hearing's momentum carry closure without proposing orders → **end_mixed136**
  - NOTE (shown after choosing): Momentum closes hearings. Orders close cases. Propose them.

## [end_record_wins] Ending — The Record Wins
*Day 470 — Tuesday, September 15, 2026 (dayOffset 470)*

At the twins' review, three weeks later, the same orders land in their dockets — the marathon's second finish line crossed with the same binder. By October the children are home outright, Odile's house holds the standing-support clause and a permanent population of spare toothbrushes, and the folder — the longest folder — is closed in your kitchen, by your hand, on an ordinary evening.

State it honestly, the house way, one final time: this is a partial win. Fifteen months of childhood were spent in the system's care, and the expungement cannot unspend them. What the record did — all it ever claimed to do — was ensure that no deadline in any track ever found this family late, undocumented, or unprepared; that every gap carried its true owner's name; and that when the clocks asked their questions, the answers had been filed in advance, per child, in the order the deadlines expired. In the hardest case in the library, that is what winning means.

**Ending.**

**Debrief:**
- THE MARATHON, AUDITED — Appeal: notified June 30, 2025; 90 days → Sunday, September 28, 2025 (23 Pa.C.S. § 6341(a)(2)); filed day 11; evidence under (c.2)(4); burden under (c.2)(5); decision within (c.3)'s 45 days. Peru: entered June 2, 2025 + 15 months = Wednesday, September 2, 2026. Twins: entered June 23, 2025 + 15 months = Wednesday, September 23, 2026. Exceptions under 42 U.S.C. § 675(5)(E) — relative care (cross-county, documented in both counties' files), case-plan compelling reason (entered in the plans in writing), services not provided (the pace exhibit, built from the agency's own plan-vs-service dates). Records: 55 Pa. Code § 3130.44(d). Counsel: 42 Pa.C.S. § 6337.
- WHY PARTIAL, AT THE LIBRARY'S CEILING — Every track resolved in the family's favor and the children still spent fifteen months placed. The guide's honesty rule peaks here: the marathon was winnable from its first week, the win was achieved in full documentary form — and it remains partial, because the prize was never the months back. It was that the months ended, on the family's terms, at the dates the board predicted in July 2025.
- WHAT NO STRATEGY CONTROLS — A blood-pressure emergency, a vendor's waitlist, two counties' stamp queues, and three children's separate experience of the same year. The route controlled order, documentation, and the naming of every gap's true owner. The library's whole curriculum is in this scenario; so is its humility.

## [end_mixed136] Ending — Two Finish Lines, One Still Painted
*Day 470 — Tuesday, September 15, 2026 (dayOffset 470)*

The marathon ends in installments: Peru's case converts on his date; the twins' requires another review cycle, their orders landing a season later than their brother's, the folder closing in two stages like the case opened.

Nothing was lost that paper protects — no petition filed, the goal intact, the registry clear. The split is a calendar's, not a verdict's: two counties and three dockets ran at their own speeds to the end, and the family's consolation is the marathon's own — every date was met by a family already standing there.

**Ending.**

**Debrief:**
- A SPLIT FINISH, NAMED HONESTLY — The gated route required **recordsRequested**, **appealFiled**, **packetBuilt**, and **kinReady** together at the final ask. Multi-docket cases resolve per docket even when they are won as a family; the difference between this ending and the best is a season, measured — as everything in this scenario is measured — in childhood.
- WHAT NO STRATEGY CONTROLS — Separate courts' calendars, which no binder synchronizes. The strategy's claim survives intact: no track was ever lost, late, or undocumented. Only the closing was staggered, because closings belong to courts.

## [end_petition136] Ending — The Petition Draft
*Day 470 — Tuesday, September 15, 2026 (dayOffset 470)*

In this branch, the fifteenth month is met the way unbuilt exceptions invite: with a petition drafted in one child's case and the goal formally in question — the services-not-provided truth still true, but now litigated as an argument instead of read as a plan entry.

The case is not lost; marathon families have recovered from petitions, at the cost of another season of hearings and a winter of proving backward what the summer's packets would have proved forward. The binder, opened again, begins its second year. It is heavier now, and so is everyone carrying it.

**Ending.**

**Debrief:**
- FORWARD VS. BACKWARD — The exceptions under 42 U.S.C. § 675(5)(E) decide cases in whichever tense they are documented. Documented forward — plan entries, packets, pace exhibits — they are findings waiting for a signature. Proved backward, they are litigation. Same facts, same statute, different year of a child's life.
- WHAT NO STRATEGY CONTROLS — A petition, once filed, has its own clocks and its own weather. The route's entire design was to make the filing question answerable in an hour, in September, from paper already filed. The draft exists in the branch where that design was abandoned at mile twenty-five.

## [end_registry136] Ending — The Entry That Outlived the Marathon
*Day 118 — Sunday, September 28, 2025 (dayOffset 118)*

The dependency marathon, in this branch, is run beautifully — kinship, plan, clocks, all of it — and the registry keeps its entry anyway, because the appeal letter spent its window being polished in a drawer, and September 28, 2025 passed on a Sunday, unmarked.

The entry surfaces in the years after: the school-volunteer form, the nursing-aide application Olatz had planned for the spring the children came home. The marathon was won. Its first mile had been forfeited in July, before the race was understood to have started.

**Ending.**

**Debrief:**
- MILE ONE — Notified Monday, June 30, 2025; 90 days → Sunday, September 28, 2025 (23 Pa.C.S. § 6341(a)(2)). Every other element of this scenario can be recovered, continued, re-documented, or cured. The appeal window cannot. The library repeats the lesson at every tier because the system repeats the trap at every scale: the smallest, quietest, earliest deadline is the one that outlives the case.
- WHAT NO STRATEGY CONTROLS — Nothing failed here except eleven days' worth of sequencing. That is the point of carving it on the marathon's trophy: in the longest case in the library, the decisive act took ten minutes in the second week.
