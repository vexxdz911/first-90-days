# THE FIRST 90 DAYS — Scenario 129: “The Year in a Folder”

*Human-readable script. This document and `scenario-129.json` are generated from a single source and match node-for-node: same IDs, same order, same choices, same effects.*

**The family is fictional — a composite. No real person's story appears here.**

**Content note:** This scenario depicts an infant's foster placement, a year of services and reviews, and a reunification hearing. There is no graphic content. Players may skip any scene or use the quick exit at any time.

**How to read effects:** `cash −40` changes the player's cash. `FLAG: name` sets a flag the engine tracks. `HIDDEN + item` means the case file quietly records that item at this choice — the player does not see it when it happens. `REQUIRES FLAG: name` means the choice is only available if that flag was set earlier; `REQUIRES NO FLAG: name` means it is only available if that flag was never set. `NOTE:` is text shown to the player right after choosing.

Start date: Monday, September 8, 2025. Day offsets are days since the scenario's start date (the child's foster-care entry date).

## [start] Month Zero
*Day 0 — Monday, September 8, 2025 (dayOffset 0)*

Your name is Edurne. Your son Unai was born in August, and in September — after a postpartum crisis that this story treats the way the file should have: as a medical event with a paper trail — the court placed him in foster care and handed you a service plan with nine boxes on it.

Nine boxes, twelve months, one folder. The foster mother, Mrs. Beltran, sends a photo every Friday. Your lawyer, Mr. Olano, says the sentence you will hear in every room this year, so hear it from him first: the court can only act on what is in the record. Counsel is your right in this case (42 Pa.C.S. § 6337). The record, starting today, is partly yours to write.

**Choices:**
- Start the folder today: plan, orders, every paper, in date order → **folder**  _(FLAG: folderKept ; HIDDEN + Parent's parallel folder started at month zero)_
  - NOTE (shown after choosing): A folder is a memory that can be handed to a judge.
- Rely on the agency's file — it's the official one → **folder**
  - NOTE (shown after choosing): It is. It will also be the only one in the room, written in the passive voice.

## [folder] Nine Boxes
*Day 14 — Monday, September 22, 2025 (dayOffset 14)*

The plan's nine boxes: treatment, parenting course, visitation, housing, employment or benefits, medical follow-through, and three more that blur together on the page. Two of them depend on referrals the agency must send. One depends on a waitlist. All nine depend, in the end, on dates.

Mr. Olano circles the two referral boxes. 'When a referral is late,' he says, 'the box looks unchecked from a distance. Get the dates.'

**Choices:**
- Ask the caseworker, in writing, for each referral's date — promised, sent, started → **boxes_detail**  _(cash −5 ; FLAG: referralDates ; HIDDEN + Referral chronology requested in writing)_
  - NOTE (shown after choosing): Three dates per referral. The difference between them is where cases hide.
- Trust the plan's timeline — it says services begin within thirty days → **boxes_detail**
  - NOTE (shown after choosing): Plans say many things. Dates say when.

## [boxes_detail] Reading the Plan Like a Contract
*Day 21 — Monday, September 29, 2025 (dayOffset 21)*

You and Mr. Olano read the nine boxes the way landlords read leases: for the verbs. 'Parent will attend' is yours. 'Agency will refer' is theirs. Three boxes have their verbs; two are written in a fog of 'as appropriate' that no one will ever be measured against.

He writes the fog-boxes on an index card. 'These are the ones that come back as surprises,' he says. 'We will ask about them monthly, in writing, until they have dates.'

**Choices:**
- Start the monthly written check-in on the fog-boxes → **referral_dates**  _(FLAG: fogTracked ; HIDDEN + Plan's vague provisions tracked by monthly written check-ins)_
  - NOTE (shown after choosing): Fog, pursued monthly, precipitates into dates.
- The plan is the plan — don't over-lawyer a service plan → **referral_dates**
  - NOTE (shown after choosing): The plan is a contract the court will enforce from memory of summaries. Over-lawyering is the job.

## [referral_dates] The First Visit Room
*Day 35 — Monday, October 13, 2025 (dayOffset 35)*

The visit room has a clock, a rug, and a box of toys that Mrs. Beltran supplements from her own house, because Unai has opinions about exactly one rattle. You arrive early. You arrive early every time, because the sign-in sheet is the one document in this building that you author yourself.

The visit supervisor notes 'mother appropriate and engaged.' Four words a week. By December they will be a paragraph the court has read fifty times.

**Choices:**
- Sign in and out precisely, and keep your own visit log with dates and one line each → **visit_log**  _(FLAG: visitLog ; HIDDEN + Visit log kept with dates from the first month)_
  - NOTE (shown after choosing): Your log and their sheet, agreeing. Agreement is a kind of evidence.
- Just be present — the bonding is the point, not the paperwork → **visit_log**
  - NOTE (shown after choosing): The bonding is the point. The paperwork is how the court finds out.

## [visit_log] The Referral That Wasn't
*Day 63 — Monday, November 10, 2025 (dayOffset 63)*

The parenting course box is still unchecked at month three, and now the file can say why, because you asked for dates: the plan was signed September 22; the referral was sent November 10; the course's next cohort starts in January. Seven weeks of the plan's twelve months, spent in a mailbox.

Your caseworker is not defensive when you raise it — she is relieved someone wrote it down. 'Put it in a letter to me,' she says, 'so it's in the file where the review will see it.'

**Choices:**
- Write the letter: plan date, referral date, cohort date — polite, dated, copied → **winter_visit**  _(cash −5 ; FLAG: gapDocumented ; HIDDEN + Referral gap documented by dated letter to the file)_
  - NOTE (shown after choosing): The gap is now a fact with dates instead of an impression with adjectives.
- Raise it verbally at the next team meeting → **winter_visit**
  - NOTE (shown after choosing): Raised, nodded at, minuted as 'discussed concerns.' Concerns are not dates.

## [winter_visit] The Visit Room in Winter
*Day 77 — Monday, November 24, 2025 (dayOffset 77)*

December visits smell of wet coats. Unai, four months old, tracks your face the way the developmental chart says he should, and the supervisor writes it down because you have learned to ask, politely, at the end of every visit: 'Will today's note say what he did?'

Asking about the note is not vanity. The notes are the visit, as far as every future reader is concerned. A parent who asks is a parent whose visits get described carefully.

**Choices:**
- Ask, and add your own line to your log: what he did, what you did, what was said → **gap_letter**  _(FLAG: notesAsked ; HIDDEN + Parent confirms each visit note and mirrors it in her own log)_
  - NOTE (shown after choosing): Two accounts, agreeing. The file's favorite kind of fact.
- Don't make it awkward — just enjoy the hour → **gap_letter**
  - NOTE (shown after choosing): The hour is enjoyed either way. Only one version leaves a careful note behind.

## [gap_letter] The Record, Requested
*Day 91 — Monday, December 8, 2025 (dayOffset 91)*

Mr. Olano suggests the mirror move at the winter review: request the agency's record of the case in writing — the material is released upon request (55 Pa. Code § 3130.44(d)), with other people's information redacted as the rule provides (55 Pa. Code § 3130.44(f)).

'You are not accusing anyone of anything,' he says. 'You are asking to read the book the court will read. Everyone should read the book.'

**Choices:**
- Sign the written request; keep the stamped copy in the folder → **record_back**  _(cash −5 ; FLAG: recordsRequested ; HIDDEN + Case record requested in writing under § 3130.44(d))_
  - NOTE (shown after choosing): Requested at month three. The book is coming.
- Wait until closer to the big review — no need to seem adversarial → **record_back**
  - NOTE (shown after choosing): Asking for your own record is not adversarial. Waiting, though, is a strategy with a price: the gaps stay invisible until they're old.

## [record_back] Reading the Book
*Day 120 — Tuesday, January 6, 2026 (dayOffset 120)*

The record confirms the referral gap — and finds a second one: the housing referral was never sent at all, an omission visible only because the file lists what it did send. Your treatment attendance is recorded as 'consistent,' your visits as 'kept, appropriate.'

The book is not your enemy. Read whole, it is a better witness for you than its summaries were. It just needs its gaps named, in writing, while there is time to close them.

**Choices:**
- File a short written response: the two gaps, with dates, and your attendance record, with dates → **winter_review**  _(cash −5 ; FLAG: responseFiled ; HIDDEN + Written response filed naming referral gaps with dates)_
  - NOTE (shown after choosing): Two gaps, two dates each, one page. The book now contains its own correction.
- Tell your lawyer and let him raise it orally at the review → **winter_review**
  - NOTE (shown after choosing): He raises it well. Orally. The review reads the file the week before, alone.

## [winter_review] The Winter Review
*Day 140 — Monday, January 26, 2026 (dayOffset 140)*

The winter review is ten minutes long. The judge has read the summaries, which say 'progressing,' and your response — not yet filed — exists only as your lawyer's spoken sentence: 'The record shows two referral gaps, Your Honor, which we will document.'

The judge nods and writes something. What she writes, you will never see. What you file, she cannot avoid seeing. The difference between those two sentences is the rest of this scenario.

**Choices:**
- Leave court determined: the response gets filed this week, not 'in due course' → **response_filed**  _(FLAG: responsePrompted ; HIDDEN + Winter review attended; filing resolve set by the court's nod)_
  - NOTE (shown after choosing): 'In due course' is where documents go to be forgotten politely.
- Take the nod as good news and let the lawyer handle timing → **response_filed**
  - NOTE (shown after choosing): The nod was good news. It was also, unmistakably, a test.

## [response_filed] The Housing Box
*Day 168 — Monday, February 23, 2026 (dayOffset 168)*

Spring. The housing referral, re-sent after your letter, reaches the top of a waitlist: a two-bedroom near the bus line, available in July, held with a letter on letterhead. It is not a key. It is the dated raw material of the last unchecked box.

The treatment program sends its own letter: completion expected in June, attendance 'exemplary' — their word, their letterhead.

**Choices:**
- File both letters and ask the agency to note the July unit in the case plan itself → **course_cohort**  _(cash −5 ; FLAG: housingLetter ; HIDDEN + Housing and treatment letters filed; plan updated in writing)_
  - NOTE (shown after choosing): The plan now says July in the agency's own hand.
- Keep the letters for the review — a surprise reveal helps → **course_cohort**
  - NOTE (shown after choosing): Hearings are not theaters. A letter filed in March is read; a letter revealed in June is examined.

## [course_cohort] The January Cohort
*Day 182 — Monday, March 9, 2026 (dayOffset 182)*

The parenting course finally starts — the one whose referral spent seven weeks in a mailbox. The instructor's sign-in sheet has your name in the first row, because you arrive the way you arrive at visits: early, with a pen that works.

Eight sessions. Eight signatures. At the end, a certificate with a seal that means nothing to you and everything to a file.

**Choices:**
- Attend all eight, file the certificate the week it issues → **treatment_letter**  _(FLAG: courseDone ; HIDDEN + Parenting course completed; certificate filed)_
  - NOTE (shown after choosing): Eight signatures, one seal, filed while the ink is still a fact.
- Miss the rainy one — one absence can't matter → **treatment_letter**
  - NOTE (shown after choosing): It can. Not because of the absence; because of the blank space where a signature argues by its absence.

## [treatment_letter] The Program's Word
*Day 196 — Monday, March 23, 2026 (dayOffset 196)*

Your treatment program's counselor writes the letter programs write when attendance has been, in her word, exemplary: dates enrolled, sessions attended, screens clear, prognosis 'excellent, with supports.' It is addressed 'To Whom It May Concern,' which in this system means: to the file.

Letters like this have a half-life. Filed in February, it is evidence. Produced in June, it is archaeology.

**Choices:**
- File it in February, with a copy to every party → **visit_expand129**  _(cash −5 ; FLAG: treatmentFiled ; HIDDEN + Treatment completion letter filed with copies to all parties)_
  - NOTE (shown after choosing): Evidence, not archaeology. The half-life is respected.
- Keep it for the final review — save the good material → **visit_expand129**
  - NOTE (shown after choosing): Saved material arrives as a claim. Filed material arrives as a fact.

## [visit_expand129] Longer Tuesdays
*Day 210 — Monday, April 6, 2026 (dayOffset 210)*

Visits expand: two hours, then an afternoon, then — the milestone the supervisor announces without ceremony — a Saturday at Mrs. Beltran's house, where Unai's other life is, so you can learn its geography: the crib, the rattle, the dog's name.

Expansion is the plan voting with its feet. Each lengthening is a document, and the documents now agree with each other in two folders at once.

**Choices:**
- Log every expanded visit, and write Mrs. Beltran a thank-you she can keep → **plan_noted**  _(FLAG: expansionLogged ; HIDDEN + Expanded visits logged; foster caregiver thanked in writing)_
  - NOTE (shown after choosing): Gratitude, in writing, in a file — the system reads kindness as stability because, usually, it is.
- Just live the longer visits — don't document joy → **plan_noted**
  - NOTE (shown after choosing): Joy documented is not diminished. Joy undocumented is just unproven.

## [plan_noted] Month Nine Review
*Day 224 — Monday, April 20, 2026 (dayOffset 224)*

The month-nine review is quiet, which veterans of this hallway recognize as a sound: the judge moves through the plan box by box, and your folder and their file tell the same story — seven boxes closed, the course done, housing dated for July, visits a year of kept Tuesdays.

The judge says the words that set the endgame: 'We'll take the permanency question at the thirteen-month review. I want the record complete by then.' Complete is a standard. It can be met on purpose.

**Choices:**
- Ask Mr. Olano to build the review packet with you: every letter, log, certificate, and the gap chronology → **unit_viewing**  _(FLAG: packetBuilt ; HIDDEN + Review packet assembled from the folder and the record)_
  - NOTE (shown after choosing): The packet is the year, edited by dates.
- The file speaks for itself by now — rest on it → **unit_viewing**
  - NOTE (shown after choosing): Files speak in the order they're read. Packets speak in the order you choose.
- Consider the folder finished — the letters can speak for themselves from here → **end_clock129**
  - NOTE (shown after choosing): Folders finished early have a way of being read as finished cases.

## [unit_viewing] The Unit
*Day 240 — Wednesday, May 6, 2026 (dayOffset 240)*

The July letter becomes a June viewing: a second-floor two-bedroom with a window over a courtyard, a lease contingent on the review's word. The housing worker photographs the empty rooms for the file — bare floors that read, in this context, like a promise with measurements.

You photograph them too, from the doorway, where a parent stands in a home that is not yet hers, learning its light.

**Choices:**
- File the lease-contingent letter and the housing worker's photos → **foster_letter**  _(cash −5 ; FLAG: leaseFiled ; HIDDEN + Contingent lease and unit documentation filed)_
  - NOTE (shown after choosing): Bare floors, dated. The court has seen a thousand promises; measurements are rarer.
- Wait for the actual keys before troubling the file → **foster_letter**
  - NOTE (shown after choosing): Keys trouble files pleasantly. Contingencies, filed early, trouble them usefully.

## [foster_letter] Mrs. Beltran's Letter
*Day 258 — Sunday, May 24, 2026 (dayOffset 258)*

Mrs. Beltran writes to the court — foster parents may, and the good ones do — a page about Unai's year: his first food, his sleep, his laugh at the dog, and the sentence that matters: 'His mother has never missed a Tuesday. I would trust her with him because I have watched her earn it weekly.'

It is the only document in the file written by someone who had the child and gave him back, weekly, on time, smiling. Judges read those letters twice.

**Choices:**
- Thank her, copy the letter into your packet exactly as written → **month9_review**  _(FLAG: fosterLetter ; HIDDEN + Foster caregiver's support letter included in the packet)_
  - NOTE (shown after choosing): Exactly as written. Her credibility is the exhibit; editing is not your privilege.
- Let the letter travel through the agency on its own → **month9_review**
  - NOTE (shown after choosing): Letters traveling alone sometimes don't. The packet is its escort.

## [month9_review] The Nine-Month Review
*Day 276 — Thursday, June 11, 2026 (dayOffset 276)*

The nine-month review goes the way the winter one didn't: the judge works from filed paper — the letters, the logs, the gap chronology with its two corrected dates — and her questions are the questions of a court checking a list it expects to complete.

'We'll take the permanency question at the thirteen-month review,' she says. 'I want the record complete by then.' This time, complete is not a hope. It is an inventory, and most of it is already checked.

**Choices:**
- Treat the sentence as a specification: list everything the record still lacks → **packet_built**  _(FLAG: specListed ; HIDDEN + Court's completeness standard converted into a checklist)_
  - NOTE (shown after choosing): A specification can be met on purpose. It now will be.
- Take the good tone as the victory and coast to September → **packet_built**
  - NOTE (shown after choosing): Tone is weather. The specification was the climate. Coasting is how packets stay unbuilt.

## [packet_built] The Packet, Assembled
*Day 300 — Sunday, July 5, 2026 (dayOffset 300)*

Mr. Olano spreads the folder and the record side by side on his office table: nine boxes across the top, their closing documents beneath, the two gaps with their dates, the letters in the order the court will want them. 'A packet is an argument,' he says, 'that has stopped needing you in the room.'

It goes in two weeks before the review, with a one-page summary on top — because the first page of a packet is the only page guaranteed a reading, and the summary makes the rest worth turning.

**Choices:**
- File the packet two weeks early, with a one-page summary Mr. Olano drafts and you sign → **overnights**  _(cash −10 ; FLAG: summaryFiled ; HIDDEN + Final packet and signed summary filed two weeks before the review)_
  - NOTE (shown after choosing): Filed early, read early, argued last. The correct order.
- Bring the packet to the hearing and hand it up → **overnights**
  - NOTE (shown after choosing): Paper delivered on the deadline is a speech. Paper filed early is a record.

## [overnights] Overnights
*Day 322 — Monday, July 27, 2026 (dayOffset 322)*

August: Unai sleeps at your apartment for the first time since he was six weeks old — the contingent lease signed after the nine-month review, the crib assembled by Mrs. Beltran's husband, who accepts pie as full payment and files a verbal receipt: 'Sturdy.'

You keep the calendar on the refrigerator anyway. Habits built over a year do not retire on command, and this one has become less a strategy than a description of the household: what happens here gets written down.

**Choices:**
- Log the overnights and the first-week pediatrician visit, and file both → **aftercare_plan**  _(FLAG: overnightsLogged ; HIDDEN + Overnight trial logged with pediatric follow-through filed)_
  - NOTE (shown after choosing): The trial writes its own evidence, one dated morning at a time.
- He's home-ish — stop logging and just be his mother → **aftercare_plan**
  - NOTE (shown after choosing): You are his mother either way. The log is for the one remaining reader: the September court.

## [aftercare_plan] Aftercare, In Writing
*Day 344 — Tuesday, August 18, 2026 (dayOffset 344)*

The agency proposes aftercare supports — the visiting nurse, the early-intervention screening, the treatment program's alumni group — and for once you are the one saying the sentence: 'Wonderful. Put it in writing, with dates.'

The caseworker laughs and does. A year ago the system's paper was something done to you. The folder changed the direction of the ink.

**Choices:**
- Get the aftercare plan signed and filed before the review → **packet_audit**  _(FLAG: aftercareWritten ; HIDDEN + Aftercare plan reduced to writing and filed)_
  - NOTE (shown after choosing): Signed, dated, filed. The case's last document is written the way its first ones should have been.
- Accept the verbal plan — everyone's aligned now → **packet_audit**
  - NOTE (shown after choosing): Alignment is a mood. Writing is a commitment with a date on it.

## [packet_audit] The Audit
*Day 366 — Wednesday, September 9, 2026 (dayOffset 366)*

Two weeks out, you and Mr. Olano audit the packet against the judge's specification, line by line: nine boxes, nine closing documents; two gaps, two chronologies; a year of Tuesdays, signed twice. One page is missing — the treatment program's final discharge summary, promised for Friday.

An audit that finds nothing is a ritual. An audit that finds one page is a rescue.

**Choices:**
- Chase the discharge summary in writing and file it the day it issues → **night_before129**  _(cash −5 ; FLAG: auditDone ; HIDDEN + Packet audited against the court's standard; final document chased in writing)_
  - NOTE (shown after choosing): Complete, on purpose, with one rescue to prove the audit worked.
- Friday's summary can be handed up at the review — close enough → **night_before129**
  - NOTE (shown after choosing): Handed-up paper is a speech. Filed paper is a record. The audit existed to teach exactly this.

## [night_before129] The Night Before Month Thirteen
*Day 384 — Sunday, September 27, 2026 (dayOffset 384)*

The packet is filed. The summary is signed. Unai sleeps in the crib in the next room on the last night of the trial that the calendar still calls a trial, and the folder — a year thick, tabbed, in date order — sits on the table like a second, quieter attorney.

Tomorrow the court reads the book everyone wrote. You just made sure you were one of its authors.

**Choices:**
- Sleep. The year is the preparation. → **final_review**
  - NOTE (shown after choosing): The folder's last service is a quiet house the night before.

## [final_review] The Thirteen-Month Review
*Day 396 — Friday, October 9, 2026 (dayOffset 396)*

Entry was Monday, September 8, 2025. Today is the thirteen-month review, and the packet has been in the file for two weeks: nine boxes, each with its closing document; two gaps, each with its dates; a year of Tuesdays.

The agency's counsel reads the same file and reaches the recommendation first, which is how you know the year worked: return home, with the plan's remaining supports converted to aftercare. The judge looks for a reason in the record to disagree with everyone, and the record — fairly, completely — does not contain one.

**Choices:**
- Ask for the order to say it plainly: return home today, aftercare in writing → **end_home129**  _(REQUIRES FLAG: recordsRequested ; REQUIRES FLAG: packetBuilt ; REQUIRES FLAG: gapDocumented)_
  - NOTE (shown after choosing): Today. The word the whole year was for.
- Accept whatever the court proposes without asking → **end_trial129**
  - NOTE (shown after choosing): The court proposes a trial period first. Close, and slower.

## [end_home129] Ending — Home at Thirteen Months
*Day 403 — Friday, October 16, 2026 (dayOffset 403)*

Unai comes home on a Monday, one year and one week after the Monday he left, with a folder's worth of proof that the year happened the way you said it did. Mrs. Beltran gets a standing Sunday invitation and a photo every Friday, a tradition now running in the other direction.

The folder goes on a shelf, not into a drawer. Some families keep them forever. It is not a trophy. It is the record, and the record is what brought him home.

**Ending.**

**Debrief:**
- THE YEAR'S LAW — Counsel throughout (42 Pa.C.S. § 6337); the case record released on request (55 Pa. Code § 3130.44(d)), its redactions governed by § 3130.44(f); and the permanency horizon behind the final review — fifteen of the most recent twenty-two months (42 U.S.C. § 675(5)(E); the parallel state review determination under 42 Pa.C.S. § 6351(f)(9)) — which this route never had to argue about, because the question the court reached first was return.
- THE REAL MECHANIC — Nothing in this scenario turns on a dramatic hearing moment. It turns on referral dates requested in writing, a gap letter the caseworker herself invited, and a packet filed two weeks early. The debriefs of the other endings show the same year at slower speeds: the facts were never the problem; their paper form was the whole contest.
- WHAT NO STRATEGY CONTROLS — Waitlists, cohort schedules, housing stock, and the individual judge. This route's claim is narrow and sufficient: every fact the court needed existed as dated paper before the court needed it. Outcomes also turn on workers, judges, and luck — the folder is how a parent makes sure luck is not carrying the whole case.

## [end_trial129] Ending — The Trial Period
*Day 403 — Friday, October 16, 2026 (dayOffset 403)*

The court orders a trial home placement first: ninety days of overnights stretching into residence, a further review in the new year, the file still open like a door not yet allowed to close.

It is a good outcome wearing a slower costume. Unai sleeps in his crib, in your home, while the system finishes convincing itself of what your folder already says.

**Ending.**

**Debrief:**
- A PARTIAL WIN, NAMED HONESTLY — He is home; the case is not closed. What separated this ending from the best one was the last paper discipline: the packet and signed summary filed early (and the flags they require — **recordsRequested**, **packetBuilt**, **gapDocumented**). Hearings ratify records; they rarely assemble them.
- WHAT NO STRATEGY CONTROLS — Judicial caution is a variable no folder eliminates. A trial period is the system hedging; the folder's work is to make the hedge short.

## [end_clock129] Ending — The Fifteenth Month
*Day 456 — Tuesday, December 8, 2026 (dayOffset 456)*

This branch is the year played at the file's pace instead of yours: the letters stopped in spring, the packet was never assembled, and the reviews summarized a plan whose remaining boxes looked — from the distance of a summary — simply open.

At fifteen of the most recent twenty-two months, the conversation changes its subject: from your progress to the agency's filing duty and its exceptions (42 U.S.C. § 675(5)(E)). The exceptions exist — kinship care, a documented compelling reason, services identified but not provided — but they must be documented to be argued, and documentation is the one crop this branch stopped planting in the spring.

**Ending.**

**Debrief:**
- THE CLOCK, ARRIVED — Entry September 8, 2025 + 15 months = Tuesday, December 8, 2026 is the horizon this ending approaches (offset 457 ≈ month 15): the filing duty and its three exceptions (42 U.S.C. § 675(5)(E)) become the case's whole subject. The services-not-provided exception was this family's true story — two referrals, one seven weeks late, one never sent — and it was unwinnable in this branch because the dates were never put in writing while they were fresh.
- WHAT NO STRATEGY CONTROLS — Nothing about the mother's effort differs between this ending and the best one. The services were attended, the visits kept, the love constant. Only the paper differs — which is the scenario's entire, deliberate point: in month fifteen, the file is the facts.
