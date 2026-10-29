# THE FIRST 90 DAYS — Scenario 128: “Two Doors, One Hallway”

*Human-readable script. This document and `scenario-128.json` are generated from a single source and match node-for-node: same IDs, same order, same choices, same effects.*

**The family is fictional — a composite. No real person's story appears here.**

**Content note:** This scenario depicts a dependency case with a kinship placement and an administrative appeal of an indicated report. There is no graphic content. Players may skip any scene or use the quick exit at any time.

**How to read effects:** `cash −40` changes the player's cash. `FLAG: name` sets a flag the engine tracks. `HIDDEN + item` means the case file quietly records that item at this choice — the player does not see it when it happens. `REQUIRES FLAG: name` means the choice is only available if that flag was set earlier; `REQUIRES NO FLAG: name` means it is only available if that flag was never set. `NOTE:` is text shown to the player right after choosing.

Start date: Monday, April 6, 2026. Day offsets are days since the scenario's start date (the date of the indicated-report notice).

## [start] The Notice and the Nursery
*Day 0 — Monday, April 6, 2026 (dayOffset 0)*

Your name is Ander. You drive a delivery van, you are taking the commercial license course at night, and your daughter Anouk is two. Three weeks ago she toppled off a low playground platform at your sister's barbecue and split her chin; the urgent-care doctor stitched it, noted the bruise pattern on her thigh from the fall, and — as doctors must — made a report.

Anouk is with her grandmother Maite while the case runs. And today the second envelope arrived: the report is indicated, naming you. The letter says the entry can affect work in childcare, schools, and — the licensing board's letter last week hinted — some transportation endorsements. Your appeal deadline is printed nowhere on it. Your lawyer finds it in the statute: 90 days from notification (23 Pa.C.S. § 6341(a)(2)). Notified Monday, April 6, 2026 — the window closes Sunday, July 5, 2026.

**Choices:**
- Put both tracks on one page: APPEAL by July 5; CASE reviews monthly → **letter_detail**  _(FLAG: calendarSet ; HIDDEN + Both tracks calendared from the notice date)_
  - NOTE (shown after choosing): One page, two clocks, no surprises.
- Deal with the court case first — the registry letter can wait → **letter_detail**
  - NOTE (shown after choosing): It can. That is the problem with waiting: it always can, until it can't.

## [letter_detail] Reading for the Date That Isn't There
*Day 1 — Tuesday, April 7, 2026 (dayOffset 1)*

You read the indicated letter three times looking for the deadline, because deadlines are supposed to be in letters. It gives you the finding, the category, the warning about employment — and no date at all. The 90 days live in the statute, not in the envelope.

It is the first lesson of the hallway: the system's letters tell you what it decided. The clocks you must find yourself, or have a lawyer find for you.

**Choices:**
- Write 'July 5' on the envelope itself, in ink → **porch_first**  _(FLAG: deadlineInked ; HIDDEN + Appeal deadline written on the notice envelope)_
  - NOTE (shown after choosing): Crude, visible, effective. The envelope goes on the refrigerator.
- Trust the calendar entry in your phone → **porch_first**
  - NOTE (shown after choosing): Phones lose things. Ink on an envelope is a technology too.

## [porch_first] Maite's Refrigerator
*Day 2 — Wednesday, April 8, 2026 (dayOffset 2)*

Maite has already started the archive: the visit sign-in sheet, the class schedule, a photograph of Anouk's healed chin dated by the phone that took it. 'I raised a driver,' she says, 'not a defendant. But paper is paper.'

Grandmothers who keep records are a documented advantage in this system, and this one keeps them in date order.

**Choices:**
- Align your folder to hers — same dates, same order, copies both ways → **two_tracks**  _(FLAG: foldersAligned ; HIDDEN + Parent's and kinship caregiver's folders aligned)_
  - NOTE (shown after choosing): Two folders, one chronology. Files that agree are hard to argue with.
- Let her keep her system and you keep yours → **two_tracks**
  - NOTE (shown after choosing): Two systems, two stories, one reconciliation owed later.

## [two_tracks] Ms. Zabala Draws Two Doors
*Day 4 — Friday, April 10, 2026 (dayOffset 4)*

Your lawyer, Ms. Zabala, draws two doors in the same hallway. Door one: the Bureau of Hearings and Appeals, a paper courtroom where the county agency must prove its report should stay indicated — the burden is theirs, by substantial evidence (23 Pa.C.S. § 6341(c.2)(5)). Door two: the dependency court, where Anouk's placement and your services are decided.

'Different rooms,' she says, 'same file. What is written in one hallway is carried into the other. We write carefully in both.' Counsel beside you in the dependency case is your right (42 Pa.C.S. § 6337); the appeal is yours to file, in writing, on time.

**Choices:**
- File the appeal this week, stamped copy in the folder → **appeal_filed**  _(cash −10 ; FLAG: appealFiled ; HIDDEN + Indicated-report appeal filed in writing within the 90-day window)_
  - NOTE (shown after choosing): Day 4 of 90. The first door is open.
- Wait for the first dependency review, then decide about the appeal → **appeal_late_risk**
  - NOTE (shown after choosing): Reviews have a way of multiplying. Deadlines do not.

## [appeal_late_risk] A Month of Reviews
*Day 31 — Thursday, May 7, 2026 (dayOffset 31)*

May is reviews, a service plan, a parenting class with a sign-in sheet. The appeal letter sits drafted in your email, unsent, aging like milk. The window has 59 days left, then 40, then — the arithmetic is not complicated, which is what makes it dangerous.

**Choices:**
- Send it today — day 31 is still inside the window → **packet_index**  _(cash −10 ; FLAG: appealFiled ; HIDDEN + Indicated-report appeal filed in writing within the 90-day window)_
  - NOTE (shown after choosing): Inside the window, with room to spare. Barely counts as late; counts completely as filed.
- Polish it one more week — it has to be perfect → **end_quiet128**
  - NOTE (shown after choosing): It became perfect on day 92. The Bureau does not grade on style.

## [appeal_filed] Maite's Porch
*Day 11 — Friday, April 17, 2026 (dayOffset 11)*

Maite's porch has a gate, a rug, and a granddaughter who has learned to say 'again' about everything. The kinship worker visits, checks the clearances file, and mentions the study is 'in process' — the system's favorite tense.

Your visits happen here, twice a week, and a sign-in sheet has appeared on Maite's refrigerator, because Maite is a woman who has read files before and trusts ink.

**Choices:**
- Ask the kinship worker, in writing, what the study still needs and by when → **porch2**  _(cash −5 ; FLAG: studyList ; HIDDEN + Kinship study requirements and dates obtained in writing)_
  - NOTE (shown after choosing): A list with dates. The study is now a checklist instead of a tense.
- Let the study proceed at its pace — Maite's house speaks for itself → **porch2**
  - NOTE (shown after choosing): Houses do not speak in hearings. Paper about houses does.

## [porch2] The Chin, Healing
*Day 14 — Monday, April 20, 2026 (dayOffset 14)*

The stitches are out. What remains is a small white line and a pediatrician's instruction to photograph it monthly for the well-child file — ordinary medicine that doubles, without anyone intending it, as a dated record of a healing child in a documented home.

The caseworker photographs it too, for her file. For once, both files take the same picture.

**Choices:**
- Keep the dated photos with the medical records in both folders → **study_paper**  _(FLAG: photosKept ; HIDDEN + Dated medical photographs kept with records)_
  - NOTE (shown after choosing): A timeline no one has to testify to.
- One photo is plenty — this feels like building a case against yourself → **study_paper**
  - NOTE (shown after choosing): It is building the case that already exists, in the order it actually happened.

## [study_paper] The Evidence You Are Owed
*Day 18 — Friday, April 24, 2026 (dayOffset 18)*

Ms. Zabala files a short letter in the appeal: under the appeal rules, the agency must provide the appellant all evidence gathered during the investigation that is relevant to the determination — including potentially exculpatory evidence — no later than ten days after the scheduling order (23 Pa.C.S. § 6341(c.2)(4)).

When the packet comes, it holds the urgent-care record, the investigator's notes — and a page you have never seen: the triage nurse's addendum, written that night, describing the fall mechanics as 'consistent with the reported low-height fall.' It was in their file the whole time. Now it is in yours.

**Choices:**
- Build the appeal around the addendum and the stitch record — the agency's own paper → **evidence_built**  _(cash −5 ; FLAG: evidenceReceived ; HIDDEN + Investigation evidence obtained under § 6341(c.2)(4), including the triage addendum)_
  - NOTE (shown after choosing): The strongest exhibit in your appeal was written by their nurse, on their form, on the night itself.
- Rely on your own account at the hearing — you were there, they weren't → **evidence_built**
  - NOTE (shown after choosing): You were. The addendum was there too, and it does not have to be believed. It has to be read.

## [evidence_built] The Case File, Requested
*Day 25 — Friday, May 1, 2026 (dayOffset 25)*

The dependency side has its own mirror: the agency's case record, released on request (55 Pa. Code § 3130.44(d)). Ms. Zabala suggests requesting it now, so the review next month is argued from their dates, not your memory of them.

The packet will arrive redacted in places — other people's names blacked out, which is the regulation's rule (55 Pa. Code § 3130.44(f)), not a message.

**Choices:**
- Sign the written request and file the stamped copy → **packet_index**  _(cash −5 ; FLAG: recordsRequested ; HIDDEN + Case record requested in writing under § 3130.44(d))_
  - NOTE (shown after choosing): Requested on day 25. The review will be read from paper now.
- Skip it — the appeal packet already showed you the important page → **packet_index**
  - NOTE (shown after choosing): The appeal packet shows the investigation. The case record shows the case. Different files, different traps.

## [packet_index] Indexing the Packet
*Day 31 — Thursday, May 7, 2026 (dayOffset 31)*

Ms. Zabala makes an index for the appeal packet: one page, eleven exhibits, each with a date and a one-line description. It takes twenty minutes. 'Hearing officers read indexes,' she says, 'the way judges read chronologies. Give the reader a map and they will follow you anywhere in the file.'

The addendum is Exhibit 4. She does not star it. The map does the starring.

**Choices:**
- File the index with the packet in both tracks → **case_packet**  _(FLAG: indexFiled ; HIDDEN + Exhibit index filed with the appeal packet and the case chronology)_
  - NOTE (shown after choosing): Eleven exhibits, one page, no stars. The map is the argument's skeleton.
- Skip the index — the exhibits speak for themselves → **case_packet**
  - NOTE (shown after choosing): Exhibits speak in the order they are found. Indexes decide the order.

## [case_packet] What the Case Record Shows
*Day 39 — Friday, May 15, 2026 (dayOffset 39)*

The record shows the service plan's soft underbelly: the parenting class referral was sent three weeks after the plan was signed, and the visit schedule at Maite's was 'to be arranged' for the first nine days. Nobody hid this. It is simply written in the passive voice, where responsibility goes to be alone.

It also shows every visit you kept, signed in Maite's ink, and the class certificates you filed yourself. The file, read whole, is fairer to you than the summary was.

**Choices:**
- Write a one-page chronology — referral dates, visit dates, certificates — and file it in both tracks → **gap_found128**  _(cash −5 ; FLAG: chronologyFiled ; HIDDEN + Dated chronology of referrals, visits, and certificates filed in both tracks)_
  - NOTE (shown after choosing): One page, twenty-two dates. Both hallways will read it.
- Save the chronology for the appeal hearing only → **gap_found128**
  - NOTE (shown after choosing): The dependency judge reviews next month. Paper filed in one hallway stays in that hallway unless you carry it.

## [gap_found128] The Nine Arranged-Later Days
*Day 46 — Friday, May 22, 2026 (dayOffset 46)*

Your chronology draft has a hole you keep stepping over: the plan says visits 'to be arranged,' and then nine days pass in the record like a held breath before Maite's first sign-in. The agency's own notes fill two of those days with a staffing shortage — written, dated, theirs.

A gap owned by the file is a gap the other side cannot assign to you at the review. The chronology's job is to make every date belong to whoever actually owned it.

**Choices:**
- Write the nine days into the chronology with the staffing note cited by date → **chronology**  _(FLAG: gapOwned ; HIDDEN + Visit-arrangement gap documented from the agency's own notes)_
  - NOTE (shown after choosing): Their note, your chronology, no one's adjective. Dates are polite that way.
- Leave the nine days blank — drawing attention to them helps no one → **chronology**
  - NOTE (shown after choosing): Blank days get narrated by whoever speaks first at the review. It will not be you.

## [chronology] The Scheduling Order
*Day 52 — Thursday, May 28, 2026 (dayOffset 52)*

The Bureau's scheduling order sets the appeal hearing for Friday, August 14, 2026. Ms. Zabala reads the second paragraph aloud: the hearing officer's decision must be entered, filed, and served within 45 days of the hearing's conclusion (23 Pa.C.S. § 6341(c.3)). Your appeal, filed in spring, will be decided by early autumn at the latest — the decision has a clock too.

Meanwhile the dependency review lands first, in July. The hallway order matters: a strong review strengthens the appeal's air; a weak one follows you through door one.

**Choices:**
- Prepare the review like it's the appeal's opening statement — chronology, certificates, the study checklist, all filed a week early → **class_done**  _(FLAG: reviewFiled ; HIDDEN + Review packet filed a week before the hearing)_
  - NOTE (shown after choosing): Filed early, read early. Hearings reward the prepared with the only currency they have: the judge's attention.
- Prepare the appeal and treat the review as a formality → **class_done**
  - NOTE (shown after choosing): There are no formalities in a hallway with two doors. There are only first impressions, twice.

## [class_done] The Certificate
*Day 58 — Wednesday, June 3, 2026 (dayOffset 58)*

The parenting course ends with a certificate and an instructor who writes, unprompted, that you asked for the reading list 'for the grandmother too.' It is a small sentence with a long reach: it describes a family organizing itself around a child, which is the case's whole argument in one line.

Certificates go in the folder the day they are issued. Paper that waits in a car visor until a hearing is paper at risk.

**Choices:**
- File the certificate and the instructor's letter in both tracks the same week → **night_shift**  _(cash −5 ; FLAG: certificateFiled ; HIDDEN + Course certificate and instructor letter filed in both tracks)_
  - NOTE (shown after choosing): Same week. The folder's rule is: paper travels at the speed of the event, not the deadline.
- Keep the certificate for the appeal hearing — fresher that way → **night_shift**
  - NOTE (shown after choosing): Nothing about a certificate improves with age except its chance of being lost.

## [night_shift] The Night Course
*Day 66 — Thursday, June 11, 2026 (dayOffset 66)*

The commercial license course meets Tuesdays and Thursdays, and the instructor signs attendance the way Maite signs visits: without ceremony, in ink, every time. Your employer writes the letter the file loves most — a promotion contingent on the license, with a number in it: the raise, dated, on letterhead.

Why does a delivery company's letter belong in a child-welfare file? Because 'stability' is a scored word, and this is what it looks like with a date on it.

**Choices:**
- File the attendance record and the employer's letter before the July review → **sister_call**  _(cash −5 ; FLAG: employerLetter ; HIDDEN + License-course attendance and employer letter filed)_
  - NOTE (shown after choosing): Stability, documented by the two institutions that can actually vouch for it.
- Mention the course at the review if it comes up → **sister_call**
  - NOTE (shown after choosing): It comes up if it's filed. Very little else comes up.

## [sister_call] Your Sister's Statement
*Day 70 — Monday, June 15, 2026 (dayOffset 70)*

Your sister — whose barbecue it was — offers to 'tell them what really happened.' Ms. Zabala redirects the offer into the form this system believes: a written statement, signed, dated, describing only what she saw: the platform's height, the grass, the rail she now admits was loose, the drive to urgent care.

She signs it in Maite's kitchen. It is three paragraphs. It has the great virtue of being about a railing, not about you.

**Choices:**
- File her statement in the appeal packet and the case record → **medical_letter**  _(cash −5 ; FLAG: sisterStatement ; HIDDEN + Eyewitness statement signed, dated, and filed in both tracks)_
  - NOTE (shown after choosing): What she saw, in writing, in both hallways.
- Save her for live testimony at the appeal — more powerful in person → **medical_letter**
  - NOTE (shown after choosing): Live witnesses get cross-examined. Filed statements get read twice, alone, by the person deciding.

## [medical_letter] The Pediatrician's Paragraph
*Day 76 — Sunday, June 21, 2026 (dayOffset 76)*

Anouk's pediatrician, at the well-child visit, writes the paragraph pediatricians write when they are not worried: growth on curve, chin healed, 'no concerns.' Six months of the case have produced a small library; this paragraph is its quietest and, to a hearing officer, possibly its most credible page.

Professionals with no stake write the sentences that decide paper cases. Collect them like weather reports from a clear sky.

**Choices:**
- Request a copy for the appeal packet the same day → **records_supp**  _(FLAG: pedsLetter ; HIDDEN + Pediatrician's well-child letter filed in the appeal packet)_
  - NOTE (shown after choosing): Same day. Clear skies do not need to be chased, just copied.
- It's in the medical file if anyone needs it → **records_supp**
  - NOTE (shown after choosing): Whose medical file, in which building, under which name? Copies end that inquiry.

## [records_supp] The Redaction Question
*Day 82 — Saturday, June 27, 2026 (dayOffset 82)*

A page of the case record arrives with a whole paragraph blacked out — a neighbor's statement, you are told, withheld under the regulation's confidentiality rules (55 Pa. Code § 3130.44(f)). It looks like a secret. Ms. Zabala reads the citation and shrugs: 'Their rule, applied as written. We note the page and move on — the appeal packet doesn't need it.'

Knowing which black bars are the system working and which are the system hiding is a skill. The citation is how you tell them apart.

**Choices:**
- Note the redacted page by number in the chronology and move on → **daycare_letter**  _(FLAG: redactionNoted ; HIDDEN + Redacted page noted by number; § 3130.44(f) basis recorded)_
  - NOTE (shown after choosing): Noted, numbered, un-feared. The file keeps its secrets in the open that way.
- Write a complaint about the blacked-out paragraph → **daycare_letter**
  - NOTE (shown after choosing): Complaints about lawful redactions spend credibility the appeal will need.

## [daycare_letter] The Job That Waits on the Registry
*Day 88 — Friday, July 3, 2026 (dayOffset 88)*

The playroom at your employer's sister property posts its weekend shifts — the extra money that was supposed to fund the bigger apartment. The posting carries the sentence you knew was coming: childcare clearance required. The registry is not an abstraction; it is a shift differential.

Ms. Zabala files the posting itself in the appeal packet. 'Stakes are not evidence,' she says, 'but hearing officers are people, and people should know what their signature does.'

**Choices:**
- File the posting and your employer's hold-letter in the packet → **review_prep**  _(FLAG: stakesFiled ; HIDDEN + Clearance-requiring job posting filed to show the registry's concrete stakes)_
  - NOTE (shown after choosing): Not evidence. Context, dated — the kind hearing officers remember at signature time.
- Leave employment out of it — the appeal is about the fall → **review_prep**
  - NOTE (shown after choosing): The appeal is about the fall. The fall's consequences hold a job hostage. Both things are in the statute's warning, verbatim.

## [review_prep] The July Review
*Day 95 — Friday, July 10, 2026 (dayOffset 95)*

The judge reads the chronology the way judges read: silently, then again at the good parts. The caseworker confirms the visits, the class, the study nearly complete at Maite's. The agency's counsel does not contest the referral gap — it is, after all, in the agency's own record, in the passive voice.

The judge asks what the plan needs to finish. It is the question your packet was built to answer.

**Choices:**
- Propose the dated finish: study completion, two more class sessions, step-down to overnights at Maite's, return on the September review → **hearing_eve**  _(REQUIRES FLAG: recordsRequested ; REQUIRES FLAG: appealFiled ; REQUIRES FLAG: chronologyFiled)_
  - NOTE (shown after choosing): Dates answer dates. The order writes itself from your page.
- Ask for Anouk home today — the record is good enough → **end_stepdown**
  - NOTE (shown after choosing): Good enough gets you a step-down and a season. The best ending needed the dates.
- Let your lawyer argue from memory of the file → **end_stepdown**
  - NOTE (shown after choosing): Memory argues well. Paper argues last.

## [appeal_hearing] The Bureau Hearing
*Day 130 — Friday, August 14, 2026 (dayOffset 130)*

Friday, August 14, 2026. The Bureau hearing room has no robes and no flags, just a hearing officer, a microphone, and the agency's lawyer carrying the burden the statute assigns her: to prove by substantial evidence that the report should remain indicated (23 Pa.C.S. § 6341(c.2)(5)).

She presents the urgent-care record. Ms. Zabala presents the same record — all of it, including the addendum the agency's own file held — plus the chronology from the case record, the certificates, and Maite's sign-in sheets. The hearing officer keeps returning to the nurse's sentence. Evidence that outweighs inconsistent evidence is the standard; the file, read whole, does not outweigh itself.

**Choices:**
- Close on the addendum and the burden: their paper, their standard, their burden → **end_both**  _(REQUIRES FLAG: evidenceReceived)_
  - NOTE (shown after choosing): Short closings win paper cases.
- Close on fairness and Anouk's laugh and how much she has grown → **end_upheld**
  - NOTE (shown after choosing): All true. None of it is the standard the officer must apply.

## [end_both] Ending — Both Doors
*Day 175 — Monday, September 28, 2026 (dayOffset 175)*

The decision is entered on day 36 after the hearing — inside the 45-day window (23 Pa.C.S. § 6341(c.3)): the report is amended to unfounded. The evidence provided under the appeal rules did what it was always capable of doing; it just needed someone to ask for it, file it, and carry it through both doors.

The September review is shorter than anyone expected. With the registry clear and the dependency record a chronology of kept dates, the court orders Anouk home on the plan the July order wrote. Maite's porch gate gets a new job: keeping nothing out, just marking where the yard begins.

Anouk says 'again' about the porch swing. Some words a file cannot hold. This one, it turns out, it could.

**Ending.**

**Debrief:**
- THE APPEAL TRACK — Filed in writing inside 90 days of the April 6, 2026 notice (deadline Sunday, July 5, 2026) (23 Pa.C.S. § 6341(a)(2)). At the hearing the agency bore the burden of proving by substantial evidence that the report should remain indicated (23 Pa.C.S. § 6341(c.2)(5)); the decisive document was the agency's own triage addendum, obtained because the appeal rules entitled the appellant to all relevant investigation evidence, including the potentially exculpatory, within ten days of the scheduling order (23 Pa.C.S. § 6341(c.2)(4)). The decision issued within the 45-day window the statute sets (23 Pa.C.S. § 6341(c.3)).
- THE CASE TRACK — The dependency record, requested under 55 Pa. Code § 3130.44(d), supplied the chronology — late referral, arranged-late visits, kept appointments — that shaped the July review and the September return. Counsel throughout is the parent's right in the dependency case (42 Pa.C.S. § 6337). The tracks are legally separate and practically one file: paper filed in one hallway should be carried, deliberately, into the other.
- WHAT NO STRATEGY CONTROLS — The hearing officer's credibility calls, the agency's litigation choices, and the judge. This route won because the exculpatory page existed and was asked for; a file without that page is a different case, and the same moves honestly made can meet a different reader.

## [end_stepdown] Ending — The Step-Down Season
*Day 175 — Monday, September 28, 2026 (dayOffset 175)*

Anouk comes home in stages: overnights, then weekends, then the slow unwinding of Maite's spare crib. The appeal is still pending in its building, undecided in this telling, and the case closes a season later than it needed to.

Nothing here is a disaster. It is the ordinary cost of a hallway walked one door at a time: months of a two-year-old's life, spent in the correct order but at the slower speed.

**Ending.**

**Debrief:**
- A PARTIAL WIN, NAMED HONESTLY — Return home on a step-down, the appeal unresolved on this branch. What separated it from the best ending was sequencing: the record requested (§ 3130.44(d)), the chronology filed in both tracks, and the dated finish proposed at the review instead of asked for outright.
- WHAT NO STRATEGY CONTROLS — Hearing officers, judges, and calendars. A step-down is the system moving at its documented speed; the route's claim is only that paper, filed in both hallways, moves it faster.

## [end_upheld] Ending — Upheld, and Home Anyway
*Day 175 — Monday, September 28, 2026 (dayOffset 175)*

The decision upholds the report. The hearing officer credits the urgent-care summary over the addendum, and the indicated entry stands — with the further clocks the debrief below names, because an upheld appeal is a result, not the end of the road.

Anouk still comes home that autumn; the dependency court reads its own record and is not bound by the registry's. You will carry the entry on clearances. You will also carry the file that shows how close the question was, and the dates of the doors that remain.

**Ending.**

**Debrief:**
- AFTER AN UPHELD APPEAL — The parties have 15 calendar days from the mailing date of the Bureau's final order to ask the Secretary to reconsider, and 30 calendar days from the mailing date to perfect an appeal to Commonwealth Court (23 Pa.C.S. § 6341(g)). Those clocks run from mailing, not from your reading of the letter — open the envelope the day it comes.
- THE TRACKS STAY SEPARATE — The dependency court's return order rests on the dependency record (counsel: 42 Pa.C.S. § 6337; records: 55 Pa. Code § 3130.44(d)). An indicated finding is serious — it surfaces on clearances — but it is not a dependency adjudication, and this ending is written to keep that distinction where the law keeps it. WHAT NO STRATEGY CONTROLS: the hearing officer's weighing of two medical sentences written the same night. Credibility is the one exhibit no one can file.

## [end_quiet128] Ending — Day Ninety-Two
*Day 92 — Tuesday, July 7, 2026 (dayOffset 92)*

The letter was perfect. Every sentence earned its place. It was mailed on day 92, and the Bureau's reply was one paragraph: the request was not filed within 90 days of notification, as the statute requires.

The dependency case goes on without the appeal — Anouk with Maite, reviews, classes, the ordinary machinery — but the registry door is closed, and it was the only door in the hallway with a lock that time itself operates.

**Ending.**

**Debrief:**
- THE ONE UNFORGIVING CLOCK — 90 days from notification (23 Pa.C.S. § 6341(a)(2)): notified Monday, April 6, 2026; the last day was Sunday, July 5, 2026. Every other deadline in this game bends, continues, or resets. This one is jurisdictional in effect: a beautiful late letter and no letter arrive at the same desk.
- WHAT NO STRATEGY CONTROLS — Nothing about the facts changed on day 92. The fall, the stitches, the addendum all remain true. Only the forum is gone — which is why every strategy guide in this library files the appeal early and polishes later, if at all.

## [hearing_eve] The Night Before Door One
*Day 124 — Saturday, August 8, 2026 (dayOffset 124)*

Tomorrow: the Bureau hearing. The packet is indexed, the chronology filed in both tracks, Maite's sheet copied, the addendum at Exhibit 4. Ms. Zabala's final instruction is procedural and almost kind: 'Say less than the paper. The paper has been preparing for months. Let it talk.'

Anouk sleeps at Maite's, unaware that her chin's white line has become a legal document with an index. Some childhoods are measured in summers. Hers, this year, is measured in exhibits — and the exhibits, at last, are complete.

**Choices:**
- Sleep. The packet is the preparation. → **appeal_hearing**
  - NOTE (shown after choosing): The hallway's oldest advice, and its best.
