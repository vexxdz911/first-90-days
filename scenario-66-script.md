# THE FIRST 90 DAYS — Scenario 66: “The Discharge Summary”

*Human-readable script. This document and `scenario-66.json` are generated from a single source and match node-for-node: same IDs, same order, same choices, same effects.*

**The family is fictional — a composite. No real person's story appears here.**

**Content note:** This scenario depicts a father in an intensive outpatient program who is discharged at week 10 of 12 because his benefit's session cap is reached, and whose agency goal is coded 'not completed.' It is told through discharge paperwork, notifications, and a review. There is no graphic content. Players may skip any scene or use the quick exit at any time.

**How to read effects:** `cash −40` changes the player's cash. `FLAG: name` sets a flag the engine tracks. `HIDDEN + item` means the case file quietly records that item at this choice — the player does not see it when it happens. `NOTE:` is text shown to the player right after choosing.

Start date: Monday, October 5, 2026. Day offsets are days since the scenario's start date. Tier: Complex.

## [start] Week Ten of Twelve
*Day 0 — Monday, October 5, 2026 — Monday, October 5, 2026 (dayOffset 0)*

You are Hector, and your son Dario is ten, and he is in foster care — placed before this story opens, in the season you are now ten weeks into repairing. The repair has a rhythm, and the rhythm is an intensive outpatient program: four evenings a week, a counselor named in your folder simply as the program, screens, group, and a chair that has become, in ten weeks, recognizably yours.

You are doing well. That is not your assessment; it is the program's, said in progress notes and in the counselor's plain speech. Two weeks remain of the twelve the plan describes. Your worker, Ms. Nakamura, has your attendance in her reports, and Dario's visits — kept, every one — have settled into the shape of a father and son who know where the puzzle box lives.

Doing well, in this system, is a sentence that has to survive being written down by other people. This scenario is about one sentence that almost didn't.

**Choices:**
- Go to this evening's session, the way you have gone to all of them → **intake_echo**
  - NOTE (shown after choosing): Week ten. The chair, the circle, the coffee. Ordinary is the achievement.

## [intake_echo] How Week One Felt
*Day 3 — Thursday, October 8, 2026 — Thursday, October 8, 2026 (dayOffset 3)*

Ten weeks ago you sat in the same circle certain you would be found out — as what, exactly, you could not have said; the feeling did not require specifics. The counselor's intake notes from that week, which you have never seen, would describe a man who answered questions as if each one were a door closing.

You think about that man on the bus sometimes, the way you think about weather you have come through. The program's own paperwork tells the distance better than your memory does: attendance, participation, screens — a record of a man arriving, four evenings a week, until arriving became the least remarkable thing about him.

**Choices:**
- Take your seat as the session begins → **program_rhythm**  _(HIDDEN + IOP — week 10 of 12; attendance and progress documented by the program)_
  - NOTE (shown after choosing): The circle fills. The work, tonight, is ordinary work, done ordinarily well.

## [program_rhythm] The Rhythm
*Day 6 — Sunday, October 11, 2026 — Sunday, October 11, 2026 (dayOffset 6)*

The rhythm of a good week: session Monday, session Tuesday, Dario's visit Wednesday, session Thursday, screen Friday, and the weekend held together by a part-time job, a sponsor's phone number, and a kitchen calendar with the program's logo magnet on it.

Ms. Nakamura's last report used the phrase “engaged and progressing,” which you read three times when your lawyer forwarded it, the way a man reads a letter from a country he hopes to live in. Your counsel in this case is your right (42 Pa.C.S. § 6337); the report is the agency's side of the conversation, and at week ten the conversation is, for once, easy to be part of.

**Choices:**
- Keep the week exactly as it is built → **screens_routine**
  - NOTE (shown after choosing): Rhythm is not the goal. Rhythm is how the goal gets reached without being carried.

## [screens_routine] Screens, Filed by Others
*Day 9 — Wednesday, October 14, 2026 — Wednesday, October 14, 2026 (dayOffset 9)*

Friday's screen is clean, as the others have been. The results travel to the agency on the provider's schedule — batched, late, in an envelope you will never see — which is one of this system's quiet arrangements: the facts of your progress exist in several buildings at once, and assemble into a file only when someone assembles them.

Your counselor mentions, in passing, that your insurer's authorization letter arrived at the program's office this week. “Administrative,” she says. “I'll explain Monday. It's not about your progress.” She says it easily, the way people deliver news they believe is small.

**Choices:**
- Go home, and keep the weekend's rhythm → **sponsor_beat**
  - NOTE (shown after choosing): Administrative. You have learned to hear that word the way sailors hear weather reports about other oceans.

## [sponsor_beat] The Saturday Call
*Day 11 — Friday, October 16, 2026 — Friday, October 16, 2026 (dayOffset 11)*

Saturday is your standing call with your sponsor — a man three years ahead of you in the same arithmetic, who treats your week the way an accountant treats a ledger: what came in, what went out, what is owed. You tell him about the authorization letter, and he is quiet a moment.

“Paper about benefits is paper about the program, not about you,” he says. “Programs run on paper. When the paper changes, get the new paper. That's the whole sermon.” You write it on the calendar, under the magnet, because this house writes things down now.

**Choices:**
- Go to Wednesday's visit with Dario → **visit_beat66a**
  - NOTE (shown after choosing): Dario has a new puzzle strategy to demonstrate. It involves, he has warned you, sorting by color first, ‘like a professional.’

## [visit_beat66a] Wednesday with Dario
*Day 14 — Monday, October 19, 2026 — Monday, October 19, 2026 (dayOffset 14)*

The visit room has a clock, a rug, and the puzzle. Dario sorts by color first, like a professional, and narrates his school week with the completeness of a ten-year-old who has decided which adult gets the full edition. You get the full edition. That fact is not in any file, and it is not nothing, and both of those things are true at once in this system, constantly.

Ms. Nakamura's observer notes the visit in the warm, flat language of visit notes. You have stopped minding the flatness. Flat, you have learned, is what good looks like in a file: attended, engaged, appropriate, concluded on time. Your whole recovery is learning to be legible in flat sentences — which is why the sentence that is coming matters.

**Choices:**
- Go to Monday's session, and the counselor's explanation → **employer_beat66**
  - NOTE (shown after choosing): She has the insurer's letter in a folder with your name on it. Your name, lately, is on a number of folders.

## [employer_beat66] The Employer, Notified in Writing
*Day 15 — Tuesday, October 20, 2026 — Tuesday, October 20, 2026 (dayOffset 15)*

A small beat with a long shadow: your part-time employer adjusts the schedule board for the coming month, and your program evenings survive the adjustment because — months ago, in a different season of this case — you put the program's hours in writing to the scheduler and kept her reply. The schedule comes out around your evenings the way water goes around a stone it has learned.

You note the new schedule in the folder. Systems accommodate what they can read; the folder's copies are how your life gets read by people who were never in the room.

**Choices:**
- Go to Monday's session, and the letter → **benefit_letter**
  - NOTE (shown after choosing): The program's rhythm holds, this week, on the strength of an old letter. Hold that thought; the scenario will.

## [benefit_letter] The Letter About Sessions
*Day 17 — Thursday, October 22, 2026 — Thursday, October 22, 2026 (dayOffset 17)*

The letter is from your insurer, and it is exactly as administrative as promised, which is to say it changes everything by arithmetic and nothing by judgment: your benefit covers a fixed number of intensive outpatient sessions. At the end of this week — week ten of twelve — the covered number will be reached. The program is not discharging you for cause. It is not discharging you for progress, exactly, either. It is discharging you because a count, in a benefits office, has finished counting.

“You have done everything we asked,” the counselor says. “I want that sentence in the room before the other sentence: the program cannot bill sessions the benefit will not cover, and self-pay at this rate is not a real option for — for almost anyone,” she finishes, accurately.

There is a step-down program — a lower-intensity program, the natural next step for someone doing well — across town. It can take you in three weeks. Three weeks, in a twelve-week plan, is a gap the plan did not draw. The agency's goal line, meanwhile, sits in a file across town, and it reads, in full: complete IOP.

**Choices:**
- Ask exactly what the discharge will say, and what you will be given → **counselor_talk**
  - NOTE (shown after choosing): Two questions, and the answers to both of them are paper. You can feel the scenario narrowing to the size of a document.

## [counselor_talk] A Counselor Who Is Sorry and Specific
*Day 20 — Sunday, October 25, 2026 — Sunday, October 25, 2026 (dayOffset 20)*

She is sorry, and — what matters more, professionally and humanly — she is specific. The discharge summary, she explains, is the program's final document: it will state your attendance, your participation, your progress, and the reason for discharge. The reason, in your case, will read: benefit limit reached. Not unsuccessful. Not non-compliant. Arithmetic.

“That summary is the program's last word about you,” she says. “It goes where you send it. People leave here with it in their hands, or they leave here with my handshake and my good opinion. My good opinion does not photocopy.” She is not being unkind. She is being a counselor at the exact moment her profession and the filing system agree with each other.

**Choices:**
- Decide how you will leave this program, on its last day → **call_insurer**
  - NOTE (shown after choosing): The last day is Friday. Between here and Friday there is one phone call you owe yourself first.

## [call_insurer] Calling the Number on the Letter
*Day 23 — Wednesday, October 28, 2026 — Wednesday, October 28, 2026 (dayOffset 23)*

The insurer's phone tree takes twenty minutes to reach a person, and the person is courteous and completely immovable: the session cap is the session cap; an appeal exists, on a timeline measured in weeks, decided by the same document that set the cap. You take the appeal information down — dated, with a reference number — because this house writes things down, and you file it without illusion: the appeal may matter to the benefit. It will not un-discharge you on Friday.

What the call confirms is the counselor's arithmetic: week ten is the end of the covered count, through no decision of yours or the program's. Two systems — a benefit and a case plan — have been running on different clocks, and Friday is where the clocks collide.

**Choices:**
- Go into the last week knowing exactly where you stand → **appeal_info**  _(cash −5; HIDDEN + Insurer session cap verified by phone — discharge at week 10 is a benefit limit, not a program decision)_
  - NOTE (shown after choosing): Five dollars of phone-era small change and one reference number later: the reason for Friday is now a fact you can cite, not a story you tell.

## [appeal_info] The Appeal, Filed Without Illusion
*Day 25 — Friday, October 30, 2026 — Friday, October 30, 2026 (dayOffset 25)*

The insurer's appeal goes in anyway — a one-page form, your counselor's supporting note, the reference number from the phone call — because a remedy unfiled is a rumor, and because its paperwork, win or lose, is one more dated document proving the cap was a cap: set by a benefit, verified by phone, appealed through channels.

It will be decided in its own season, probably after the review, possibly after the step-down ends. You file it the way you now file everything: completely, dated, and without confusing the filing with the outcome.

**Choices:**
- Go into the last week of the program → **summary_choice**  _(cash −3)_
  - NOTE (shown after choosing): Three dollars of copies. The arithmetic now has a paper trail in three buildings.

## [summary_choice] The Last Day: Paper or Handshake
*Day 26 — Saturday, October 31, 2026 — Saturday, October 31, 2026 (dayOffset 26)*

Friday, the last session. The circle does its closing ritual for a departing member — you are the third this season, and the other two, you realize, left to step-down programs and jobs, in the ordinary traffic of recovery. There is cake. There is a card the group signed. There is the counselor, at the door, with two versions of your departure in her hands, though only one of them is literally in her hands.

The discharge summary exists — printed, signed, stating your progress, your attendance, and the reason: benefit limit. Getting it is a matter of asking for it, signing the release, and carrying it out the door. Not getting it is a matter of a handshake, a warm ‘you did great,’ and a summary that stays in the program's file, available in principle, absent in practice from every file where your future will be read.

**Choices:**
- Ask for the discharge summary in writing before you leave — sign the release, take the document → **discharge_day**  _(cash −4; FLAG: dischargeSummary; HIDDEN + Discharge summary obtained in writing — progress, attendance, reason: benefit limit)_
  - NOTE (shown after choosing): Two pages, signed, warm from the printer. The program's last word about you, in your folder, where words about you belong.
- Take the handshake and the ‘you did great’ — she knows how you did, and so do you → **discharge_day**
  - NOTE (shown after choosing): She does, and you do. The agency's file, which knows neither of you, is about to be told something else entirely.

## [discharge_day] Discharged, in the Ordinary Sense
*Day 30 — Wednesday, November 4, 2026 — Wednesday, November 4, 2026 (dayOffset 30)*

You leave the program on a Friday evening with a card from the group, a cake's worth of goodwill, and either a signed summary in your folder or a compliment in your memory. The program's door closes behind you with the sound doors make. You have completed ten weeks of a twelve-week program, attended everything, progressed by every measure the program keeps — and your formal status, in the program's own system as of tonight, is: discharged.

Words travel between systems badly. ‘Discharged’ is about to travel from a program that means it arithmetically to an agency whose goal line says complete — and whose coding, as you are about to learn, has no arithmetic in it at all.

**Choices:**
- Go home, and call your sponsor from the kitchen → **last_day_scene**
  - NOTE (shown after choosing): He asks one question: ‘Did you get the paper?’ Your answer to it is the rest of the scenario.

## [last_day_scene] The Folder That Night
*Day 33 — Saturday, November 7, 2026 — Saturday, November 7, 2026 (dayOffset 33)*

That night the folder comes out on the kitchen table, as it does in weeks when the case turns. Its contents are the case as you hold it: attendance printouts, the insurer's letter, the appeal reference number, the visit notes you keep copies of — and the summary, if you have it, or the space where the summary would go, if you don't.

Your lawyer calls it ‘your half of the file.’ The other half is being written tonight, somewhere, by a system processing a discharge notification in the ordinary course: a form, a status field, a goal line. Two halves of the same ten weeks, about to describe them very differently.

**Choices:**
- Wait for the agency's side of the week to arrive → **coding_beat**
  - NOTE (shown after choosing): It arrives the way these things arrive: as a short phone call and a shorter sentence in a system.

## [coding_beat] How the System Codes a Discharge
*Day 36 — Tuesday, November 10, 2026 — Tuesday, November 10, 2026 (dayOffset 36)*

Ms. Nakamura calls on Tuesday, and she is careful in a way you have learned to respect: she tells you exactly what she can see. The program has notified the agency of the discharge. In the agency's system, the goal “complete IOP” has a status field, and the status that a discharge generates — any discharge, for any reason, before the program's full course — is the status the field was built to hold.

“On my screen,” she says, “your goal currently reads: not completed.” She pauses. “I know what your attendance has been, Hector. The field does not have a place for what I know. It has a place for documents. If the program's summary says what you tell me it says, the summary is how the field gets corrected.”

Four words — goal: not completed — now sit in a file where a review will read them, in a room you will have minutes to answer in. Ten weeks of evenings are currently losing to a status field.

**Choices:**
- Ask her exactly what would correct the coding, and in what order → **worker_call**  _(HIDDEN + Agency system codes IOP discharge as 'goal not completed' — reason not carried by the coding)_
  - NOTE (shown after choosing): Her answer is a list, and every item on it is paper, and every item has a deadline shaped like a review date.

## [worker_call] Ms. Nakamura's List
*Day 40 — Saturday, November 14, 2026 — Saturday, November 14, 2026 (dayOffset 40)*

Her list, in her order: one, the agency needs the discharge summary itself — attached to something in writing from you, so it enters the file as your submission with a date, not as a rumor at a check-in. Two, the step-down enrollment, when it happens, needs proof in the file the same way. Three, all of it needs to arrive before the review, because the review report will be written from the file as it stands when the report is drafted — not as it stands when you explain it in the room.

“I am not supposed to have a strategy for you,” she says. “Your lawyer is for strategy. I am telling you how the paperwork moves, because the paperwork is my job.” It is the most useful conversation you have had with the agency in ten weeks, and it is entirely about envelopes.

**Choices:**
- Call your lawyer that evening with the list in front of you → **nakamura_meeting**
  - NOTE (shown after choosing): He will have the same list, in legal order. Lawyers and workers agree about envelopes more often than either admits.

## [nakamura_meeting] The Plan, in Legal Order
*Day 44 — Wednesday, November 18, 2026 — Wednesday, November 18, 2026 (dayOffset 44)*

Your lawyer — your counsel in this case, as the law provides (42 Pa.C.S. § 6337) — rearranges Ms. Nakamura's list into a campaign: notify the agency in writing, with the summary attached, before the review; enroll in the step-down the week it opens, with the enrollment proof filed the same week; request your own record, to see exactly how the goal was coded and what the chronology says; and file a written correction, so the file's own words get fixed, not just supplemented.

“Note the verb in step three,” he says. “You may request your case record, and under the regulation it ‘shall be released upon request’ (55 Pa. Code § 3130.44(d)). We do not guess how the goal was coded. We read it.”

“And the clock,” he says, “is the three weeks. The step-down cannot take you for three weeks. Those weeks are the gap the review will ask about. We do not hide the gap. We paper it, in advance, as what it is: a wait for the next program the plan's own logic points to.”

**Choices:**
- Start with the step-down's intake paperwork, this week → **gap_explained**
  - NOTE (shown after choosing): The step-down's office keeps intake hours twice a week. The first one is tomorrow.

## [gap_explained] Three Weeks, Explained Slowly
*Day 48 — Sunday, November 22, 2026 — Sunday, November 22, 2026 (dayOffset 48)*

The gap, stated as the file will need it stated: you were discharged at week ten for a benefit limit. The step-down program — the clinically appropriate next step, the one your counselor named — has a three-week wait for an opening. In those three weeks you will attend your sponsor meetings, keep Dario's visits, keep your screens by arrangement with Ms. Nakamura's office, and wait, in the documented way, for a door that opens on a date the step-down itself will put in writing.

A gap explained in advance, with dates and a named next door, is a transition. The same gap, discovered by a review from a status field, is a disappearance. The three weeks will be identical either way. The file's version of them is entirely up to the paperwork done inside them.

**Choices:**
- Go to the step-down's intake office tomorrow → **stepdown_beat**
  - NOTE (shown after choosing): Intake paperwork: the least dramatic document in recovery, and this month, the most important one.

## [stepdown_beat] Intake Paperwork
*Day 52 — Thursday, November 26, 2026 — Thursday, November 26, 2026 (dayOffset 52)*

The step-down program's intake office is a smaller room with the same species of forms. The coordinator confirms the opening — three weeks out, dated — and offers the two versions of enrollment this system always offers: she can take your completed intake packet now, stamp it, and give you a dated enrollment confirmation for the opening; or she can take your name and phone number and call you when the opening approaches, the way programs have always done it, warmly and without a stamp.

**Choices:**
- Complete the intake packet now and take the dated enrollment confirmation → **gap_week**  _(cash −6; FLAG: stepdownEnrolled; HIDDEN + Step-down program — intake completed; dated enrollment confirmation for opening in three weeks)_
  - NOTE (shown after choosing): Stamped, dated, copied. In three weeks you will start; as of today, the file can already prove you will.
- Leave your name and number — they'll call when the opening is close → **gap_week**
  - NOTE (shown after choosing): They will call. Programs do. The file, meanwhile, will hold a three-week silence where an enrollment should be.

## [gap_week] The Gap, Week One
*Day 57 — Tuesday, December 1, 2026 — Tuesday, December 1, 2026 (dayOffset 57)*

Week one of the gap has no program evenings in it, and the evenings are long in a way the last ten weeks had trained you not to notice. You fill them the documented way: a support meeting, signed in; the Saturday sponsor call, kept; Dario's visit, kept; a screen, by arrangement, clean.

This is the week the scenario most wants you to see clearly, because it is the week a review will later compress into a phrase. ‘A three-week gap in treatment’ can be written by a report writer as a falling-off or as a bridged transition, and the difference will be made entirely of paper generated inside weeks like this one — or of its absence.

**Choices:**
- Keep the week's paper — sign-ins, visit, screen — in the folder, dated → **gap_support**
  - NOTE (shown after choosing): A bridged gap is built one ordinary kept evening at a time. So is every other kind of record.

## [gap_support] The Gap, Week Two
*Day 59 — Thursday, December 3, 2026 — Thursday, December 3, 2026 (dayOffset 59)*

Week two of the gap, and the shape of it is now clear: this is not an interruption in a recovery; it is a recovery, conducted without a program's rooms for three weeks, on the strength of meetings, a sponsor, a son's Wednesdays, and paperwork. Your sponsor, reviewing the ledger on Saturday, delivers his verdict in his dialect: “You're not between programs. You're in the part of the program nobody schedules.”

You write that down too, on the calendar, though it will never be filed anywhere. Some records are for the file. Some are for the man the file is about.

**Choices:**
- Finish the gap's second week, and turn to the agency → **transport_beat66**
  - NOTE (shown after choosing): One week of gap remains. The notification decision — the campaign's center — is next.

## [transport_beat66] The Bus Pass Decision
*Day 60 — Friday, December 4, 2026 — Friday, December 4, 2026 (dayOffset 60)*

Money, because this scenario insists money is always in the room: the step-down is across town, the bus pass is a real expense against a part-time wage, and the month has already produced a phone bill for an insurer's phone tree and a folder's worth of copies. Protecting the route to the step-down — the pass, bought now, good through the review and into the program's first weeks — is unglamorous in exactly the way the whole winning strategy in these scenarios is unglamorous.

**Choices:**
- Buy the pass now and protect the route to the step-down → **notify_beat**  _(cash −24)_
  - NOTE (shown after choosing): The route is now a fact, not an intention. Facts are what reviews can be told.
- Pay per ride and keep the cash — the route can be managed week to week → **notify_beat**
  - NOTE (shown after choosing): It can, most weeks. Reviews are not held in most weeks; they are held in the week the managing failed.

## [notify_beat] Notifying the Agency, Before the Review
*Day 64 — Tuesday, December 8, 2026 — Tuesday, December 8, 2026 (dayOffset 64)*

The notification is the campaign's central document, and its power is entirely in its timing and its attachment: a short written notice to the agency, from you, through your lawyer, stating that the program discharged you at week ten for a benefit limit — with the discharge summary attached, if you have it — and that you are enrolled in the step-down, with its dated confirmation attached, if you have that. Sent now, it lands in the file before the review report is drafted. Sent later, it is an argument made to a room about a report already written.

Ms. Nakamura's list and your lawyer's campaign agree on this point completely, which in this system is as close to certainty as advice ever gets: the review reads the file. Notify the file.

**Choices:**
- Send the written notification now, with the summary and enrollment attached → **letter_to_file**  _(cash −5; FLAG: agencyNotified; HIDDEN + Agency notified in writing before the review, discharge summary attached)_
  - NOTE (shown after choosing): Sent, dated, attached. The review report will now be drafted from a file that contains the program's own words.
- Wait and explain it at the review in person — you'll be in the room; your voice should count → **letter_to_file**
  - NOTE (shown after choosing): It will count, in the room, for the minutes the room gives it. The report was drafted the week before, from the file as it then stood.

## [letter_to_file] What the File Holds Tonight
*Day 68 — Saturday, December 12, 2026 — Saturday, December 12, 2026 (dayOffset 68)*

Tonight the file holds either a campaign or a hope. In the campaign version: the summary, with its arithmetic reason; the enrollment confirmation, with its date; a notification, stamped before the review. In the hope version: a status field reading ‘not completed,’ a counselor's good opinion in a program office across town, and a father who can explain everything, in a room, briefly, after the report is read.

Your lawyer's remaining steps are the audit and the repair: read the file itself, and correct its coding in writing. “We do not yet know,” he says, “whether the correction needs to fix a sentence or a status. So we read.”

**Choices:**
- Move to the audit: request the record → **records_beat66**
  - NOTE (shown after choosing): Reading, as ever in this system, is a right with a citation attached.

## [records_beat66] Reading the Coding
*Day 72 — Wednesday, December 16, 2026 — Wednesday, December 16, 2026 (dayOffset 72)*

The request is the one your lawyer named: your case record, from the agency, which under the regulation “shall be released upon request” (55 Pa. Code § 3130.44(d)). You sign it with the specific ask included — the goal-status history and the chronology entries for the discharge — because you are no longer asking whether the file misdescribes you. You are asking for the page and line where it does, so the correction can cite the page and line.

**Choices:**
- Sign and send the written records request this week → **coding_seen**  _(cash −4; FLAG: recordsRequested; HIDDEN + Case record requested in writing under 55 Pa. Code § 3130.44(d))_
  - NOTE (shown after choosing): Signed, dated, specific. The coding is about to become a document you hold, instead of a rumor you fear.
- Skip the request — Ms. Nakamura already told you how it reads → **coding_seen**
  - NOTE (shown after choosing): She told you honestly. A correction, however, has to cite the file — and citing requires the page, not the summary of the page.

## [coding_seen] Goal: Not Completed, in Print
*Day 77 — Monday, December 21, 2026 — Monday, December 21, 2026 (dayOffset 77)*

The record, when it comes, is as described and worse in the small way that matters: the chronology entry for your discharge is one line — ‘Parent discharged from IOP’ — with no reason attached, and the goal line reads, in the file's own typographic calm: Goal: Not Completed. Nothing in the entry is false. Everything in it is incomplete, which in a file is the more durable kind of wrong, because no one ever has to defend it as a statement.

Below the entry, if your notification arrived in time, sits your own submission — the summary, the enrollment, the dates — filed after the coding but before the report. The file now contains both versions of your ten weeks: the field's four words, and the program's two pages. A correction is how the first version gets amended to match the second.

**Choices:**
- Draft the written correction with your lawyer → **correction_beat66**  _(HIDDEN + Goal coding read in the parent's own record — 'not completed,' reason absent from the chronology)_
  - NOTE (shown after choosing): Page, line, status: identified. Corrections, like apologies, only work when they are specific.

## [correction_beat66] The Written Correction
*Day 82 — Saturday, December 26, 2026 — Saturday, December 26, 2026 (dayOffset 82)*

The correction is short, because the documents do the work: it asks that the chronology be amended to state the discharge's reason — benefit limit, per the program's attached summary — and that the goal be re-coded to reflect completion to the extent the benefit allowed, with the step-down enrollment, dated and confirmed, noted as the plan's continuation. It cites the summary's page, the enrollment's date, and the chronology's line. It accuses the status field of nothing; status fields have no intentions to accuse. It simply asks the file to say the whole thing.

**Choices:**
- File the written correction with the summary and enrollment attached → **hallway_beat66**  _(cash −5; FLAG: correctionFiled; HIDDEN + Written correction filed — discharge reason and goal re-coding requested, documents attached)_
  - NOTE (shown after choosing): Filed before the review. The report writer will now meet the correction in the file, in the ordinary course of writing.
- Hold the correction for the review — hand it up in the room, where it will be seen → **hallway_beat66**
  - NOTE (shown after choosing): It will be seen, in the room, by people reading a report that was finished without it. Seen is not the same as used.

## [hallway_beat66] The Week the Step-Down Opens
*Day 86 — Wednesday, December 30, 2026 — Wednesday, December 30, 2026 (dayOffset 86)*

The three weeks end the way dated openings do: on schedule. Before the step-down's first session, the remaining pressure arrives from the ordinary direction — Dario's school sends a note about a parent event, your employer's schedule shifts a half-day, and the visit lands midweek like a small holiday inside the logistics.

None of it is the case, and all of it is the case: the review will meet a father whose ten weeks became a discharge, a gap, and a new program, and the only version of that story guaranteed a hearing is the one already in the file.

**Choices:**
- Go to Dario's visit, the day before the step-down opens → **dario_visit**
  - NOTE (shown after choosing): He has been saving a question. Ten-year-olds save questions the way programs save documents: carefully, and for a date.

## [dario_visit] Dario's Question
*Day 90 — Sunday, January 3, 2027 — Sunday, January 3, 2027 (dayOffset 90)*

The visit is a good one — the puzzle, the full edition of the school week, a drawing produced from a backpack with ceremony. Near the end, in the unhurried minute while the pieces go back in the box, Dario asks it, looking at the puzzle lid and not at you, the way people ask the questions that matter most: “When do I come home?”

You give him the truth at his size, the way you have learned to: grown-ups are still working out the timing; a judge helps decide; your job is the program and the visits, and you are doing your job, all of it, including the new program that starts this week. He nods with the completeness children nod with, and holds your sleeve a moment at the door, and the visit concludes on time, as the note will say.

**Choices:**
- Write the visit up in your folder that night, dated, as always → **dario_school**  _(HIDDEN + Visit kept — Dario's question answered at his size; visit concluded on time)_
  - NOTE (shown after choosing): The note will say: attended, engaged, appropriate. The folder will hold the sleeve. Both records are true.

## [dario_school] The School Note
*Day 94 — Thursday, January 7, 2027 — Thursday, January 7, 2027 (dayOffset 94)*

Dario's school note is a small, ordinary piece of parent work — a form about the parent event, a signature line, a date — and it requires, as such forms now do, coordination with the agency about who signs what while a child is placed. You handle it the folder way: copy made, question asked in writing, answer kept.

It is not a beat in anyone's case plan. It is a father remaining a father at the level of forms, in a week when the large machinery of the case is deciding how to describe him in a status field. The scenario includes it because real cases are made of both, in the same weeks, at the same kitchen table.

**Choices:**
- File the school form copy and go to the step-down's first session → **stepdown_start**
  - NOTE (shown after choosing): Ordinary parent work, done in an unordinary week. Both facts belong in the folder.

## [stepdown_start] The New Chair
*Day 98 — Monday, January 11, 2027 — Monday, January 11, 2027 (dayOffset 98)*

The step-down's room is smaller, the circle is smaller, and the chair you are given is, in the way of chairs, nobody's yet. The counselor has your intake packet — stamped weeks ago, if you filed it that way — or takes your information fresh, if the enrollment waited for a phone call. Either way, you attend, you sign in, and the program's second chapter begins with the oldest sacrament in this system: a signature on a sign-in sheet, on a date, in a file.

Your participation is noted. Your status, in this program's system, is the word the agency's field never held: enrolled, attending, progressing. Whether the agency's file will say those words by the review depends on paper already sent — or on a voice, briefly, in a room.

**Choices:**
- Send the step-down's attendance confirmation to the agency and your lawyer → **money_beat66**  _(cash −4; HIDDEN + Step-down program — first session attended; attendance confirmation sent)_
  - NOTE (shown after choosing): Proof, filed while it is fresh. The gap now has a far shore, and the far shore has a date on it.

## [money_beat66] Payday, Thin and Sufficient
*Day 103 — Saturday, January 16, 2027 — Saturday, January 16, 2027 (dayOffset 103)*

The part-time paycheck lands, thin and sufficient, in the week before the review. The folder's arithmetic for the autumn is its own quiet argument: bus pass, copies, stamps, intake fees where they fell — a recovery administered at retail prices by a man who kept the receipts, because receipts, in this system, are a dialect of the truth.

Your lawyer asks for the folder one more time before the review. “Whatever the report says,” he says, “we answer from this. If the report says what the file now says, the folder rests. If it says the four words, the folder testifies.”

**Choices:**
- Bring the folder to the final preparation → **review_notice66**
  - NOTE (shown after choosing): The notice has already arrived. It is on the refrigerator, under the program's magnet, where the calendar used to be.

## [review_notice66] The Review Notice
*Day 108 — Thursday, January 21, 2027 — Thursday, January 21, 2027 (dayOffset 108)*

The review notice names the date and the room. Reviews in this system are stock-takings: the report is drafted from the file, the room hears summaries and brief answers, and the stock taken is, in large part, the file's own description of you — ‘engaged and progressing,’ from month two, against ‘goal: not completed,’ from week ten, unless the file between those phrases has been repaired.

Your lawyer lays the preparation out as a description, not a prediction: “The report writer is drafting this week. What she finds in the file is what the review will be. We have spent a month deciding what she finds. The rest is her pen and the judge's morning, which were never ours.”

**Choices:**
- Go to the final preparation with your lawyer → **counsel_prep66**
  - NOTE (shown after choosing): One folder, one file, one report being drafted across town. The campaign is finished; the audit is next.

## [counsel_prep66] Final Preparation
*Day 113 — Tuesday, January 26, 2027 — Tuesday, January 26, 2027 (dayOffset 113)*

Preparation is an audit, conducted at a conference table with the folder open: the summary, if it exists — obtained on the last day, in writing, with the reason stated. The enrollment, if it exists — dated, stamped, confirmed. The notification, if it was sent — before the review, with attachments. The record request, if it was made — and the correction, if it was filed, with its page and line citations.

Each document either is or is not in the agency's file tonight. There is no third state, and no preparation can create one. “Whatever is in there,” your lawyer says, “is what we argue from. What isn't, we explain — and explaining, in a review, is the tax you pay for paper not filed.”

**Choices:**
- Check the folder's last page, and sleep → **review_prep_docs**
  - NOTE (shown after choosing): Tomorrow the report gets read aloud. Tonight, the file is what it is, and so are you.

## [review_prep_docs] What the Report Will Say
*Day 118 — Sunday, January 31, 2027 — Sunday, January 31, 2027 (dayOffset 118)*

The night before the review, the honest inventory: a ten-week program, attended completely, ended by arithmetic. A three-week gap, bridged with meetings and paper or waited out on a promise. A new program, begun. A goal line in a file across town, coded in four words, corrected in writing or still standing. A son who asked a question at a puzzle table and got the truth at his size.

None of that is the review's business in narrative form. The review's business is the report. The report's business is the file. The file's business — this whole scenario's business — is what was put in it, in writing, before the drafting.

**Choices:**
- Go to the review → **eve_beat66**
  - NOTE (shown after choosing): The room, the report, the four words or their correction. Everything now depends on which documents the file held when the report was written.

## [eve_beat66] The Eve of the Review
*Day 121 — Wednesday, February 3, 2027 — Wednesday, February 3, 2027 (dayOffset 121)*

The evening before the review runs on the house's new rails: folder straightened, morning's clothes laid out, Dario's drawing from the last visit on the refrigerator under the program magnet that outlived the program. Your sponsor calls, briefly, in his ledger dialect: “Whatever they read tomorrow, you know what you did. The paper either says it or the next paper will.”

“That's the whole sermon now,” you tell him. “It got shorter.” “Sermons do,” he says, “when they're true.”

**Choices:**
- Sleep, and go to the review in the morning → **review66**
  - NOTE (shown after choosing): The room will read the file. The file is finished being written — by everyone, including you.

## [review66] The Review
*Day 123 — Friday, February 5, 2027 — Friday, February 5, 2027 (dayOffset 123)*

The review is orderly and brief in the way of rooms with many cases. The report is read in summary. The question the report must answer is narrow and enormous: what is the status of the plan's central goal — complete IOP — for a father who completed ten of its twelve weeks before a benefits office ended the count?

The answer is in the file, in one of three forms. In the first, the file holds the program's own summary, the agency's advance notification, the dated step-down enrollment, and a filed correction — and the report, drafted from that file, describes a goal re-coded and a plan continuing. In the second, the truth exists but arrived as explanation, after the report's coding had already done its work in the room. In the third, the file holds four words, a handshake's memory, and a counselor's good opinion in a building across town — and the report reads the four words, because the four words are what a report can read.

**Choices:**
- The report is read from the repaired file — summary, notification, enrollment, correction, all in before the drafting → **end_summary**  _(REQUIRES: dischargeSummary, agencyNotified, stepdownEnrolled)_
  - NOTE (shown after choosing): The file answered the question before the room had to.
- The truth is in the room, carried by voice and late paper, after the report relied on the code → **end_gap**  _(REQUIRES: dischargeSummary, correctionFiled; REQUIRES-NOT: agencyNotified)_
  - NOTE (shown after choosing): Everything you say is true. The report was written last week.
- The truth is in the room, in the father's own account, against the file's four words → **end_notcompleted**  _(REQUIRES-NOT: dischargeSummary)_
  - NOTE (shown after choosing): A counselor's good opinion does not photocopy. The review is about to demonstrate it.
- The report stands on the coding — the explanation exists, but no document carries it → **end_notcompleted**  _(REQUIRES-NOT: agencyNotified, correctionFiled)_
  - NOTE (shown after choosing): Four words, unopposed by paper, in a room that runs on paper.
- The report is read from the repaired file — summary and notification in before the drafting, the step-down still a promised first session → **end_notcompleted**  _(REQUIRES: dischargeSummary, agencyNotified; REQUIRES-NOT: stepdownEnrolled)_
  - NOTE (shown after choosing): Paper answered everything except the plan's central fact: the step-down never began.

## [end_summary] Ending — The Summary Says Progress
*Day 129 — Thursday, February 11, 2027 — Thursday, February 11, 2027 (dayOffset 129)*

The report, when its turn comes, does not read the four words. It reads the goal as the correction re-coded it: IOP completed to the extent the benefit allowed — ten weeks, full attendance, progress documented by the program's own summary — with step-down treatment underway as the plan's continuation. The judge notes the enrollment's date, the notification's date, and the summary's reason, in the tone of a person reading a file that agrees with itself.

“The record should say what happened,” the judge says, in passing, in the direction of no one in particular. “In this file, it does.” Dario is still placed at this scenario's curtain. The plan continues, the step-down continues, and the review closes on a file that describes the father Dario visited on Wednesday — which is all, and exactly, what the paperwork campaign was for.

**Ending.**

**Debrief:**
- WHAT THE RECORD HELD (the hidden record, revealed): A complete paper chain, each link dated before the review: the discharge summary, obtained in writing on the program's last day, stating progress, attendance, and the reason — benefit limit; a written notification to the agency, with the summary attached, sent before the review report was drafted; a step-down enrollment completed by intake packet, with a dated confirmation for the opening three weeks out; the parent's own record, requested and read (55 Pa. Code § 3130.44(d)), so the miscoding was seen on its page and line; and a written correction, filed with documents attached, re-coding the goal on the record. The four words were amended before they could testify.
- THE LAW UNDER THIS PATH: No exotic law was used, and the scenario says so plainly. Counsel's role (42 Pa.C.S. § 6337) was sequencing and filing; the record request (55 Pa. Code § 3130.44(d)) was the audit; the rest was timing — reviews are argued from reports, reports are drafted from files, and a correction that arrives before the drafting is a fact, while one that arrives in the room is an argument. Nothing in this ending decided Dario's placement or tested any burden of proof; the review continued the plan on a corrected record, honestly labeled PARTIAL: Dario is still placed, and the case continues.
- THE HONEST PART: This ending is not a verdict on Hector's worth, and it was not produced by virtue alone. A counselor willing to print the summary without being asked twice, a worker who explained the coding honestly, a step-down with an opening in three weeks rather than three months — people and luck hold their pieces of it, as they do in every ending here. A different report writer could have clung to the status field even against the correction. What Hector controlled was the chain itself: paper obtained at the door, notice given before the drafting, enrollment proven instead of promised. In a system that reads files, the father who papers his own arithmetic is the only author his progress reliably gets.

## [end_gap] Ending — A Gap, Explained Late
*Day 127 — Tuesday, February 9, 2027 — Tuesday, February 9, 2027 (dayOffset 127)*

The review hears the truth — all of it, from the father, with the summary produced and the correction handed up — and the truth is believed, in the personal way voices are believed in rooms that run on drafted reports. The report, however, was drafted the week before, from a file whose goal line read ‘not completed,’ and the review's own record now contains both: the coded report, and a father's correction, arriving after the coding had already framed the morning.

The judge directs that the correction be filed and the record amended going forward — it will govern the next report, and every summary after it. Going forward is the operative phrase, the same one that governs every late truth in this system: repaired, permanently, and one review too late to have framed this one.

**Ending.**

**Debrief:**
- WHAT THE RECORD HELD (the hidden record, revealed): The truth, in documents — eventually. The discharge summary existed and said what it said; a written correction was filed; the step-down was real. What the campaign lacked was the ordering: the agency was not notified in writing before the review report was drafted, so the report was written from the status field, and the correction, however complete, was received as an answer to a report instead of as part of the file the report was written from. The gap in treatment was three weeks. The gap in paperwork was longer, and it is the second gap this ending is named for.
- THE LAW UNDER THIS PATH: The verified tools were the same as in every path — counsel (42 Pa.C.S. § 6337), the parent's own record on request (55 Pa. Code § 3130.44(d)) — exercised here as repair rather than prevention. No placement was decided and no burden was tested in this review; the plan continues, the step-down continues, and the amended record will govern future reports, which in a long case is a real and material thing. PARTIAL, honestly labeled in the other direction: the file is right now, and was wrong when the report that framed this review was drafted from it.
- THE HONEST PART: Late truth governs the future, and the future is most of a case — this ending refuses both despair and flattery. A report writer who called the program herself, a worker who attached the summary on receipt, a review postponed a fortnight: any of them lands this correction on the right side of the drafting without Hector changing a thing, and a colder room could have received the same late paper and discounted it entirely. Workers, report writers, and calendars hold their pieces here. Hector's piece was the ordering — and ordering, in a file-driven system, is not a clerical detail. It is the difference between a fact and a rebuttal.

## [end_notcompleted] Ending — Goal: Not Completed
*Day 125 — Sunday, February 7, 2027 — Sunday, February 7, 2027 (dayOffset 125)*

The report reads the goal line the way reports read goal lines, without inflection: “Goal: not completed.” The father's explanation follows — accurate, complete, and carried entirely by his voice and a counselor's remembered kindness — and is noted in the review's record the way explanations are noted when no document carries them: heard, summarized in a clause, and filed beneath the coding, which remains the file's operative sentence about his ten weeks.

Outside, his lawyer says the sentence this scenario has been walking toward since the insurer's letter: “Four words just outlived a ten-week effort, because the effort's own document never entered the file. The counselor's summary still exists, Hector. Programs keep their paper. What can still be requested, filed, and corrected is most of it — for the next report. Next reports are where cases like yours are actually decided.”

**Ending.**

**Debrief:**
- WHAT THE RECORD HELD (the hidden record, revealed): A status field and nothing beneath it: a discharge with no reason in the chronology, a goal coded ‘not completed,’ a step-down waited on rather than enrolled in with proof, a notification never sent in writing before the drafting, a record never requested, a correction never filed. The ten weeks happened — attendance, progress, clean screens, a counselor's genuine good opinion — and almost none of it existed in the only medium the review could read. What the file cannot say, the report cannot summarize; what the report cannot summarize, the review cannot weigh.
- THE LAW UNDER THIS PATH: The tools remain exactly where they were in week ten, because none of them expire at a review: counsel (42 Pa.C.S. § 6337) can still sequence the repair; the parent's record ‘shall be released upon request’ (55 Pa. Code § 3130.44(d)), so the coding can still be read on its page and corrected in writing; the program's summary can still be obtained and filed. No placement was decided at this review and no burden of proof was tested; the plan continues under a coded failure that the documents, if filed now, can still amend for every future reader. That amendability is this ending's honest floor: the four words won this report, not the case.
- THE HONEST PART: This debrief does not call the outcome a judgment on the father, because it is not one: it is a judgment about a medium. A worker who requested the summary herself, a counselor who mailed it unasked, a coding field with a line for ‘reason’ — any of them prevents this ending without the father changing a single evening of his ten weeks. Systems, workers, and luck are all over this outcome. The father's share was narrower and heavier: he left the program with a handshake, in a case that runs on paper, and a handshake — however warm, however earned — is the one document the file cannot hold.
