# THE FIRST 90 DAYS — Scenario 27: “The Long Way Home”

*Human-readable script. This document and `scenario-27.json` are generated from a single source and match node-for-node: same IDs, same order, same choices, same effects.*

**The family is fictional — a composite. No real person's story appears here.**

**Content note:** This scenario depicts a child waiting in foster care while a relative placement in another state moves through two agencies' paperwork — told through procedure, forms, and elapsed time. There is no graphic content. Players may skip any scene or use the quick exit at any time.

**How to read effects:** `cash −40` changes the player's cash. `FLAG: name` sets a flag the engine tracks. `HIDDEN + item` means the case file quietly records that item at this choice — the player does not see it when it happens. `NOTE:` is text shown to the player right after choosing.

Start date: Monday, January 5, 2026 (placement). Day offsets are days since the scenario's start date.

## [named_at_table] The Name You Say First
*Week 1 — Monday, January 12, 2026 — Monday, January 12, 2026 (dayOffset 7)*

Your son Milo, six, has been in foster care with a family he had never met before this month. At the family meeting — a table, a worker, a list of questions that move faster than grief — you are asked whether there is family. There is.

Your sister Carla, Milo's aunt, lives in another state, in the house with the yard where Milo spent two summers. She has known him since he was born. She is, you say, the first name. The worker writes it down, and a second process — slower, farther away, and run between two states' offices — begins beside your own case.

Nobody at the table can tell you how long that process takes. You will learn why: it does not take time the way a line takes time. It takes time the way weather takes time — in systems nobody at this table can see whole.

**Choices:**
- Give Carla's name, address, and phone number in writing before you leave → **aunt_call**  _(HIDDEN + Family meeting — aunt in another state named by Mother in writing on day one)_
  - NOTE (shown after choosing): Written at the first table where writing was possible. That timing will matter more than anyone here can yet say.

## [aunt_call] Carla Says Yes Before You Finish
*Week 2 — Monday, January 19, 2026 — Monday, January 19, 2026 (dayOffset 14)*

You call her from the visit room phone with your list beside you, because good news delivered badly still has to be delivered. You get as far as 'Milo is—' before she says: 'He comes here. Tell them he comes here. What do I sign?'

She means it completely, which is not the same as the system being ready for her to mean it. Her yes starts a file in two states. It also starts a clock on her own life: forms, checks, visits to her home, questions about rooms and income and everyone who lives there — an examination she did not cause and does not resent, yet.

Your job, you will learn, is not only your own plan. It is keeping this yes alive, and documented, across however many months the distance takes.

**Choices:**
- Write down Carla's yes, the date, and everything she is told to expect — in your folder → **local_checks**  _(FLAG: auntNamed; HIDDEN + Aunt's agreement — dated, with her contact details confirmed in writing)_
  - NOTE (shown after choosing): A yes is a fact. A dated yes, in a folder, is a fact that can travel.

## [local_checks] Her Local Checks Come Back Clear
*Month 1 — Monday, February 2, 2026 — Monday, February 2, 2026 (dayOffset 28)*

The first news is good and quick, which will make the rest harder to understand. Carla's local checks — the ones run where she lives — come back clear. Her references speak well of her. By every early measure her state can run quickly, she is who you said she was: willing, related, and known to Milo.

Then the process changes altitude. Her home must be studied by her state's system, requested through yours. Forms must travel between offices that measure urgency in different units. The worker here is kind about it: 'It's moving,' she says, in the tone of a person reading a status she did not write.

Milo, meanwhile, starts a new school from a stranger's address, and learns his foster family's dog's name, and asks you on visits when Aunt Carla's house is.

**Choices:**
- Ask, in writing, what has been sent to Carla's state and when → **own_plan**
  - NOTE (shown after choosing): The answer you get is a verb: 'requested.' Verbs without dates are where this scenario lives.

## [own_plan] Your Own Plan, in Parallel
*Month 1 — Monday, February 9, 2026 — Monday, February 9, 2026 (dayOffset 35)*

Your case plan is not small: treatment, parenting work, housing, employment — the ordinary architecture of a parent rebuilding in public. You start it the week it is handed to you, because Milo's case has never had the luxury of a parent who waits, and because your track is the one track you fully touch.

Hold both truths, because the case will: Carla's placement is a real, parallel path to Milo being with family — and it is not a substitute for your plan. If her paperwork fails, your plan is the whole case. If your plan finishes first, her paperwork becomes a safety net that was never needed. Either way, both tracks have to be run as if the other might fail. That is not pessimism. That is the design.

Your worker, Ms. Bell, is fair within her caseload: 'Do your plan like she's never coming,' she says. 'And help me keep her coming like your plan is all that matters. Both. I know how it sounds.'

**Choices:**
- Start treatment intake and the parenting program this week → **forms_claim**  _(cash −20; FLAG: planStarted; HIDDEN + Mother's plan — treatment and parenting started in the first month)_
  - NOTE (shown after choosing): Fees, bus fare, copies. Your track starts moving at the only speed you control: yours.

## [forms_claim] 'Sent,' Says the File
*Month 2 — Monday, February 23, 2026 — Monday, February 23, 2026 (dayOffset 49)*

At the next meeting, Ms. Bell has an update with a clean shape: the request for Carla's home study has been sent to her state. The forms are in motion. Carla should expect contact. Everyone at the table relaxes by exactly the amount a clean shape allows.

You ask a question that will become this scenario's refrain: sent when, and to whom, and how would we know if it arrived? Ms. Bell does not take offense. She writes the sending date on a sticky note for you — the first date in the interstate part of your file that anyone has handed you on paper.

Carla, that weekend, has heard nothing. 'It's early,' you tell her, and mean it. It is early. Early is a real place, and files also get lost there.

**Choices:**
- Put the sticky-note date in your log, and tell Carla to keep every envelope she receives → **waiting**  _(HIDDEN + Home study request — sending date obtained from worker and logged by Mother)_
  - NOTE (shown after choosing): A date received verbally is a start. A date in your log is a tool.

## [waiting] Month Three, in Two States
*Month 2 — Monday, March 9, 2026 — Monday, March 9, 2026 (dayOffset 63)*

Your track moves in visible units: sessions attended, a certificate in progress, a part-time job found through the treatment program. Milo's visits are the week's fixed star. You are, by the ratings language of your plan, progressing.

Carla's track moves invisibly. She has rearranged the spare room. She has told her employer she may need flexibility 'for family.' She has received, in three months, one form — which she completed and returned within the week, keeping her copy, because you asked her to run her own folder the way you run yours.

Two systems, two states, one child waiting with strangers between them. Nobody is refusing anything. That is the hardest part to explain later: how a placement can starve in a room where everyone says yes.

**Choices:**
- Ask to see your own file — find out exactly where Carla's paperwork is → **records_choice**
  - NOTE (shown after choosing): You have been patient with summaries. Summaries are where this placement currently lives.

## [records_choice] Reading Your Own Record
*Month 2 — Monday, March 16, 2026 — Monday, March 16, 2026 (dayOffset 70)*

You may request your case record, and it 'shall be released upon request' (55 Pa. Code § 3130.44(d)). Parents in this system ask for their files for many reasons. Yours is specific and new in your caseworker's experience: not to argue about the past, but to locate a piece of paper in the present — where, exactly, between two states, is Carla's home study request?

The request is one page. You name what you need: the interstate placement correspondence log — what was sent, when, to which office, and what came back.

Ms. Bell signs off on the visit to review it without a flicker. 'Honestly,' she says, 'I'd like to know too.'

**Choices:**
- Sign and send the records request, naming the interstate correspondence specifically → **records_reveal**  _(cash −5; FLAG: recordsRequested; HIDDEN + Records request — interstate correspondence log specifically named)_
  - NOTE (shown after choosing): One page, dated, copied. Somewhere, a file is about to be opened by the person it is about.
- Take Ms. Bell's summaries — she is on your side; don't make it formal → **no_records**
  - NOTE (shown after choosing): She is on your side. Her summaries are still summaries — written from a system that can only see its own half of the distance.

## [records_reveal] Logged as Sent. Never Received.
*Month 3 — Monday, March 30, 2026 — Monday, March 30, 2026 (dayOffset 84)*

The correspondence log is a tidy page, and its tidiness is the problem. Request sent — dated, initialed, correct form. Follow-up: none recorded. Response from Carla's state: a blank where a receipt should be.

You do the arithmetic nobody had done in one sitting: the request your state logged as sent was never logged as received by hers. Somewhere between an outbox and an inbox — a wrong office, a changed address, a system migration nobody announced — Milo's aunt's home study spent two months not existing, in a case where everyone involved believed it was underway.

There is no villain in this paragraph. There is a blank in a log, a child in a stranger's home, and a date — today's, yours — when someone finally looked.

**Choices:**
- Put the gap in writing to Ms. Bell — dates, the blank, and a request to resend and confirm receipt → **resend**  _(FLAG: gapFound; HIDDEN + Interstate log — request logged as sent; no receipt ever recorded in the receiving state)_
  - NOTE (shown after choosing): Written, dated, unaccusatory. A gap described precisely is a gap that can finally be filled.

## [no_records] Summaries, Reassured
*Month 3 — Monday, March 23, 2026 — Monday, March 23, 2026 (dayOffset 77)*

'Still in process,' Ms. Bell reports, after checking. 'These take time. Carla's side is probably scheduling.' It sounds true. It has the texture of everything you have been told, which is the texture of a system reporting on its own intentions.

Carla, that weekend, laughs the laugh of a woman who has rearranged a room for a child and heard from no one: 'If they're scheduling, they're scheduling quietly.' You both let it go. Letting it go feels like patience, and patience feels like what good parents in cases are supposed to supply in unlimited quantity.

Somewhere, a request sits in a log marked sent, in a state that never received it. This month, nobody looks. The looking was the whole skill, and it was available, and it waits — records requests do not expire unmade; they just start later, over older gaps.

**Choices:**
- Go on — work your plan, and keep Carla close the ways you can → **resend**
  - NOTE (shown after choosing): Your plan is real work and it matters. So would the file. The case is about to charge interest on the difference.

## [resend] Resent — and This Time, Confirmed
*Month 3 — Monday, April 13, 2026 — Monday, April 13, 2026 (dayOffset 98)*

Whether you found the gap in the log or Ms. Bell found it in a routine check a month later, it is found: the study request is resent, and this time the process grows a second half — confirmation. Carla's state acknowledges receipt, with a date, and the acknowledgment is forwarded to you because you asked for it in writing.

Carla gets her first real call from her own state's worker. She cries a little afterward, from relief and embarrassment at relief. 'I thought they'd decided no and were being polite,' she says. Nobody had decided anything. That is the sentence this scenario was built to contain: nobody had decided anything, for two months, about a six-year-old's home.

You log both dates: sent, received. The distance between them is now a fact with edges. Facts with edges can be argued from.

**Choices:**
- Ask Carla to log every call and letter from her state, and to send you copies monthly → **study_visit**  _(FLAG: receiptConfirmed; HIDDEN + Home study request — resent; receipt confirmed with a date by the receiving state)_
  - NOTE (shown after choosing): Two folders, two states, one log between them. You are building the bridge the systems didn't.

## [study_visit] The Study Visit Is Scheduled. Then It Isn't.
*Month 4 — Monday, May 11, 2026 — Monday, May 11, 2026 (dayOffset 126)*

Carla's home study visit is scheduled — a real appointment, a worker's name, a Saturday she cleans for like a holiday. Then it is postponed: her worker's caseload, a training, a week that filled. Then it is rescheduled, weeks later, by a different worker, who asks Carla questions the first worker's forms had already answered, because the forms and the worker changed places in a queue.

None of this is refusal. All of it is elapsed time, billed to a child who is learning a second foster family's routines while his aunt's spare room holds a bed in plastic wrap.

What Carla does with the postponement is the playable skill of this entire scenario, and it is not in her hands alone. It is in yours, on the phone, on Sunday nights, keeping a willing woman willing inside a process that keeps forgetting to speak to her.

**Choices:**
- Set a standing Sunday call with Carla — case talk, then ordinary family talk, logged briefly → **approvals_clock**  _(FLAG: sundayCalls; HIDDEN + Aunt contact — standing weekly calls between Mother and aunt, logged)_
  - NOTE (shown after choosing): Engagement is a practice, not a feeling. Practices survive postponements. Feelings file for extensions less reliably.
- Give her space — she knows you're grateful; calls every week might feel like pressure → **approvals_clock**
  - NOTE (shown after choosing): Space is kind in ordinary life. In a months-long process run on paper, silence reads as something else entirely.

## [approvals_clock] Approvals Age, Even When People Don't Change
*Month 5 — Monday, June 8, 2026 — Monday, June 8, 2026 (dayOffset 154)*

A letter arrives for Carla that she forwards to you with three exclamation points of alarm: one of her approval steps — a clearance she completed at the very start — has a validity window, and the window is closing while her study is still pending. Nothing about her has changed. Paper, unlike aunts, expires on schedule.

This is the second clock you did not know your case had: not the child's, not yours — the paperwork's own. Each document in Carla's file was born on a date and some of them die on one, and renewal requires her to notice, act, and document, again, while being told the placement itself is 'close.'

She asks you, in a smaller voice than her yes had: 'How many times do I have to become approved?' You do not have an answer. You have a log, a calendar, and a Sunday call. In this system, those are not nothing. They are, in fact, most of what there is.

**Choices:**
- Put every expiry in Carla's file on both your calendars, with a month's warning → **renewal_beat**
  - NOTE (shown after choosing): Two calendars, one set of dates. Expiring paper is a surprise only once.

## [renewal_beat] Renewal Season
*Month 6 — Monday, June 22, 2026 — Monday, June 22, 2026 (dayOffset 168)*

You build Carla's renewal kit together by phone and mail: fresh forms where forms are wanted, her kept copies where copies will serve, a cover note that lists what is enclosed and when the originals were filed. She sends it before the window closes and keeps her proof of sending the way you taught her — dated, copied, logged.

It is unglamorous in the precise way permanency actually is. No courtroom, no speech. A woman in one state re-proving, to a second state, a set of facts that never stopped being true, so that a file about a child in a third place — the foster home where Milo is doing second-grade math — can stay alive.

Her study visit, when it finally happens, goes well. The worker likes the house, the room, the yard, and Carla. 'If it were up to the visit,' Carla says, 'we'd be done.' It is not up to the visit. It is up to the paper about the visit, traveling.

**Choices:**
- Help Carla renew early — kit sent, proof kept, copies to you → **study_draft**  _(cash −10; FLAG: renewalDone; HIDDEN + Aunt's approvals — renewed before expiry; proof of sending kept and copied)_
  - NOTE (shown after choosing): Cost: copies, postage, an evening. Benefit: a file that never lapses while it waits.
- Trust the timeline — the study is done; renewal can wait until they ask → **study_draft**
  - NOTE (shown after choosing): They will ask. The asking and the expiring do not consult each other, and the gap between them is billed in months.

## [study_draft] A Finished Study, Traveling Slowly
*Month 7 — Monday, August 3, 2026 — Monday, August 3, 2026 (dayOffset 210)*

Carla's home study is finished and favorable — a document that says, in professional language, what you said at a table in one sentence months ago: this child is known here, wanted here, and the home is ready. She reads you the conclusion line over the phone and you both sit in the sound of it.

Then the finished study begins its own journey: from her worker to her state's office, from her state to yours, from your state's office to your worker and the court file. Each handoff is, by itself, days or weeks of queue. The study is a fact. In transit, it is a rumor with excellent documentation.

Milo's foster family, who have been kind, ask Ms. Bell whether they should stop saving his place at their table for weekends after a move 'in case it confuses him.' Kind people, making reasonable plans, inside elapsed time. Elapsed time is the only antagonist this story needs.

**Choices:**
- Ask, in writing, where the finished study is this week — and log the answer → **parent_progress**
  - NOTE (shown after choosing): The refrain, again: where is it, when was it sent, how do we know it arrived. Asking is tracking. Tracking is the case.

## [parent_progress] Your Track, Suddenly Interesting
*Month 8 — Monday, August 31, 2026 — Monday, August 31, 2026 (dayOffset 238)*

While paper travels, your plan completes its middle chapters: treatment certificate filed, parenting program done, employment steady, and housing — the goal that looked least movable — opens a real door: a two-bedroom through a program your counselor names, with a wait measured in weeks, not seasons. Your progress rating reaches the plan's strongest word.

Ms. Bell says it carefully at the review table: 'If your housing lands, your track may finish before Carla's paperwork does. I did not expect to say that sentence when this started.'

Two paths home, racing at bureaucratic and human speeds respectively. Milo's case now has the strangest of its problems: abundance, arriving late, in an order nobody scheduled.

**Choices:**
- Tell Carla the truth — your housing may land first, and her yes still matters completely → **foster_beat**  _(FLAG: truthTold; HIDDEN + Mother's progress — treatment and parenting complete; housing opening documented)_
  - NOTE (shown after choosing): A family that can survive good news delivered honestly can survive this process. She takes it the way she took everything: 'Then I'll be the backup plan every kid deserves.'

## [foster_beat] What Waiting Looks Like From Milo's Chair
*Month 9 — Monday, September 28, 2026 — Monday, September 28, 2026 (dayOffset 266)*

Milo has been in care for most of a school year. He has a foster family's routines, a best friend on their street, and a reading level his teacher is proud of. He also lights up for your visits in a way that makes the visit supervisor write the same sentence month after month, and he asks about Carla's dog by name on video calls.

On those calls — arranged through the workers, kept to schedule — Carla reads him a chapter a week of a book she is also sending, a chapter behind, to his foster home, so the story lives in both houses. It is a small, deliberate thread across a year of process.

Whether that thread is logged anywhere is, like everything else in this case, a choice somebody makes on paper.

**Choices:**
- Ask the workers to log Carla's video calls with Milo — dates, in the file → **where_records**  _(FLAG: contactLogged; HIDDEN + Aunt-child contact — regular video calls arranged and logged)_
  - NOTE (shown after choosing): A bond that is logged is a bond a court can see. A bond that lives only in kitchens is real, and invisible, in unequal measure.
- The calls are family business, not case business — leave them unlogged → **where_records**
  - NOTE (shown after choosing): Family business, warmly kept. The file, asked later what relationship waited on the other end of all that paperwork, will have to answer from memory.

## [where_records] Asking Where It Is, Again
*Month 10 — Monday, October 26, 2026 — Monday, October 26, 2026 (dayOffset 294)*

The study is finished. The placement is not made. The distance between those two sentences is where this case now lives, and it deserves one more precise question, asked in the tool this scenario keeps handing you: request the record again — the record 'shall be released upon request' (55 Pa. Code § 3130.44(d)) — and trace, this time, the finished study's journey, office by office, date by date.

You have done this before. That is the point. A parent who asks twice is not difficult. She is a tracking system for a child who cannot track his own paperwork.

**Choices:**
- Send the second records request — trace the finished study's transmission, with dates → **trace_reveal**  _(cash −5; FLAG: recordsRequested; FLAG: studyTraced; HIDDEN + Second records request — finished study's transmission to be traced with dates)_
  - NOTE (shown after choosing): One page. The answer will either produce the study's location or produce the admission that nobody has it. Both are progress.
- Call Ms. Bell instead — she'll check informally → **trace_skip**
  - NOTE (shown after choosing): She will, and she'll mean it, and informal checking produces no dated artifact for anyone — including her, when she needs leverage inside her own system.

## [trace_reveal] The Study Was in a Queue With No Name
*Month 10 — Monday, November 9, 2026 — Monday, November 9, 2026 (dayOffset 308)*

The trace works the way the first one did: by making someone assemble dates in one place. The finished study reached your state and entered a review queue. There it sat, complete and favorable, while reviews of Milo's case reported the placement as 'pending study.' The study was not pending. Its being acted on was pending — a distinction that cost a season and belongs to no villain, only to a queue with no name and no clock of its own.

With the trace in the file, the sentence changes everywhere it is repeated: at the next review, Ms. Bell reports the study as 'received, favorable, and awaiting final placement approval' — because now the paper says so, in her own system's handwriting.

You log the dates — finished, sent, received, found. Four dates. Together they are the proof that the delay in this case was process, not family. Proof like that has a legal use you are about to meet.

**Choices:**
- Take the four dates to the next review, and ask what they change → **hearing_late**  _(FLAG: delayDocumented; HIDDEN + Study trace — delay shown to be transmission and queue time, documented with four dates)_
  - NOTE (shown after choosing): Process, not family: five words, with dates under them. Keep them dry. Dry facts travel furthest in courtrooms.

## [trace_skip] 'Still Pending,' One More Season
*Month 10 — Monday, November 9, 2026 — Monday, November 9, 2026 (dayOffset 308)*

Ms. Bell checks, kindly, and reports what her screen says: study 'pending.' It is what her screen has said for months. Neither of you says the thing the first records request taught this case: screens summarize queues they cannot see into, and a finished document can be pending in a system the way a letter can be pending in a drawer.

Carla renews another expiring item. Her voice on Sundays has acquired a note you each pretend not to hear — the sound of a person deciding, in real time, how much more of this she can hold. She has not decided anything. Drift does not announce itself as a decision. That is its entire method.

Your own track, meanwhile, does not drift at all. It is close enough now to cast a shadow on the whole interstate question.

**Choices:**
- Go to the late review with your plan's record — and Carla's endurance, as you know it → **hearing_late**
  - NOTE (shown after choosing): You know both tracks by heart. The file knows one of them well. Which one it knows is about to matter at review speed.

## [hearing_late] The Review Where the Clock Speaks
*Month 11 — Monday, December 7, 2026 — Monday, December 7, 2026 (dayOffset 336)*

A new voice appears at reviews when a case gets long, and it appears now: the federal timeline. Milo has been in care since January 5, 2026. At fifteen of the most recent twenty-two months — April 5, 2027 — the agency's duty about filing a termination petition changes. Nobody says it to threaten you. It is said to the record, in your presence, which in this system amounts to the same weather arriving through a different window.

And with it, a door you have been building without knowing its name: among the exceptions to that filing duty (42 U.S.C. § 675(5)(E)) is the case where the child is being cared for by a relative — and, beside it, the need for the file to show what is true. Carla is not yet Milo's placement. But a documented record that a relative placement has been pursued continuously, and delayed by process rather than by family, is the raw material from which courts and agencies document why a case should continue toward that relative instead of filing on a schedule.

Ms. Bell looks at you across the table. 'This is where the paperwork becomes the argument,' she says. 'All of it. At once. In the next few weeks.'

**Choices:**
- Ask what gets built, for which ending, starting this week → **aunt_fatigue**
  - NOTE (shown after choosing): Four endings are still in this room. The next month decides how many of them leave it.

## [aunt_fatigue] Carla's Voice, Thinner
*Month 12 — Monday, January 4, 2027 — Monday, January 4, 2027 (dayOffset 364)*

The Sunday call runs short. Carla's employer has stopped being flexible. Another renewal notice arrived — addressed, she says, 'to the woman I was at the start of this.' Her sister asks her, reasonably, whether anyone is ever actually sending this child, or whether she is keeping a room ready for a system that has forgotten her address in every sense but the literal one.

She has not quit. Quitting is not how placements like this die. They die the way she is describing: a form answered a week slower, a renewal let lapse, a call not returned within the window a tired person allows a queue — silence, accumulating at both ends of a process that runs on replies.

Keeping her is not a sentiment. It is logistics, gratitude, and dates — delivered by you, weekly, on purpose. This is the month it counts most, because it is the month it is hardest.

**Choices:**
- Go to Carla — a visit, her folder reviewed together, her importance said plainly and in writing to the file → **parent_housing**  _(cash −30; FLAG: auntHeld; HIDDEN + Aunt's engagement — sustained through the final stretch; her file complete and current)_
  - NOTE (shown after choosing): Bus fare, a day, a letter for the record naming what she has done and kept current. Expensive in your currency. Priced correctly.
- She is family — family doesn't need tending; focus everything on your housing finish → **parent_housing**
  - NOTE (shown after choosing): Family, untended across a year of queues, behaves the way everything untended does. The file will use the word 'drift' if anyone writes a summary.

## [parent_housing] Your Housing Letter Arrives
*Month 13 — Monday, February 1, 2027 — Monday, February 1, 2027 (dayOffset 392)*

The program's letter is real: your name, a unit, a move-in window weeks — not months — away. Your lawyer reads it twice at the review table with the expression of a person watching a race change leaders in the final stretch.

If the unit lands and Milo trials at home before the fifteen-month point, the interstate process becomes what Carla, with her whole heart, already volunteered to be: the backup, the summers, the safety net — family in reserve instead of family in queue.

If it slips — and housing letters in this system have slipped before — Carla's file, current and documented, is the whole ballgame. The final build must therefore do something that feels unfair and is simply true: prepare both endings at full strength, in the same weeks, with the same paper.

**Choices:**
- Build the final record with Ms. Bell and your lawyer — for every door still open → **strategy_choice**
  - NOTE (shown after choosing): One build season. Four doors. The file you have actually made decides which of them can bear weight.

## [strategy_choice] Choosing the Final Build
*Month 14 — Monday, March 1, 2027 — Monday, March 1, 2027 (dayOffset 420)*

The clock date is April 5, 2027. Your lawyer lays out the builds plainly. Push Carla's placement to completion now — study favorable, trace done, approvals current: it could land before the clock. Or build the exception record — the dated proof that a relative placement was pursued without pause and delayed by process — so that if the clock arrives first, the file documents why filing should wait for the relative. Or lead with your own track: housing, completion, trial return — the ending that makes every other paper moot. Or let the season pass on summaries, renewals unchased, and Carla's silence compounding.

'Each build spends the same weeks,' she says. 'Choose where the paper goes.'

**Choices:**
- Push the placement — every office, every date, weekly written follow-ups until Carla's approval lands → **push_aunt**  _(FLAG: pushBuilt)_
  - NOTE (shown after choosing): Pressure, politely, in writing, at the speed of queues that only move when watched.
- Build the exception record — assemble the dated proof of continuous family effort and process delay → **exception_packet**  _(FLAG: exceptionBuilt)_
  - NOTE (shown after choosing): If the clock wins the race, this packet is the reason the race doesn't end the case.
- Lead with reunification — finish your track at full strength, Carla documented as the standing backup → **parent_first**  _(FLAG: parentLed)_
  - NOTE (shown after choosing): Your housing, your certificates, your visits — and Carla's file, current, in reserve.
- Let it ride — everyone means well; the systems will sort it out → **drift_path**
  - NOTE (shown after choosing): Meaning well is the fuel this process has run on all year. Elapsed time is what it produces.

## [push_aunt] Watched Queues Move
*Month 14 — Monday, March 15, 2027 — Monday, March 15, 2027 (dayOffset 434)*

It is not magic and it is not fairness — it is the physics of watched paper. Written follow-ups, dated, weekly, from you and (twice) from your lawyer, asking each office the only two questions in this scenario: where is it, and what happens next, by when. Carla keeps her end current to the day. Her state's final approval is issued and transmitted — with, this time, a confirmation of receipt logged on both ends within the same week.

The approval lands days before the fifteen-month point, close enough that Ms. Bell reads the date twice before she smiles.

Milo packs a bag in a foster kitchen, kindly, with a card from the family who kept him while two states learned to talk to each other. He is moving to family. He has been, in the paperwork sense, moving there for over a year. Now the moving is real.

**Choices:**
- Go to the final review — placement with Carla, before the clock date → **review_push**
  - NOTE (shown after choosing): The review is almost short. Almost-short reviews are what a finished record buys.

## [exception_packet] The Packet of Dates
*Month 14 — Monday, March 15, 2027 — Monday, March 15, 2027 (dayOffset 434)*

It assembles like an argument because it is one: the family meeting note naming Carla at the start. Her dated yes. The first request, logged as sent and never received — and the date you found the gap, in a record you requested. The resend, and the confirmed receipt. Her renewals, each before its expiry. The Sunday-call log. The video-call log. The study's four dates: finished, sent, received, found in a queue. Her final approvals, current.

Laid end to end, the dates tell one story in the file's own language: this family never stopped. The delay was made of transmission, queues, and expiring paper — process, documented as process, month by month.

Your lawyer's cover letter asks for exactly one thing: that if the clock arrives before the placement completes, the record document the relative-placement path as the reason filing waits (42 U.S.C. § 675(5)(E)) — a child headed, on paper and in fact, to a relative's care.

**Choices:**
- File the packet before the clock date, with the court and the agency → **review_exception**
  - NOTE (shown after choosing): Filed early, so the fifteen-month review reads dates instead of hearing about them.

## [parent_first] Your Track, at Full Strength
*Month 14 — Monday, March 15, 2027 — Monday, March 15, 2027 (dayOffset 434)*

Your build is the oldest work in the case, finished at full strength: the housing letter with its window, the certificates, the visit record that grew from supervised to long weekends as the year turned, the counselor's final letter. Carla's file rides in the packet too — current, documented, and labeled honestly: the family's standing placement, pursued without pause, ready if this ending falters.

Your lawyer is blunt about the race: 'If your move-in holds, the court may never have to decide anything about interstate paperwork. The best way to beat a slow process is to finish a fast one. Yours became fast when the housing landed. Keep it landed.'

You do the unglamorous final tasks in order: deposits, documents, the room made ready — a bed actually assembled this time, in a home that is yours, for a child whose year has been spent between other people's tables.

**Choices:**
- Go to the final review leading with the return → **review_parent**
  - NOTE (shown after choosing): Your folder, her folder, one child. The court finally gets to choose between two goods with dates on them.

## [drift_path] A Quiet Month, Compounding
*Month 14 — Monday, March 15, 2027 — Monday, March 15, 2027 (dayOffset 434)*

Nobody decides anything this month, which is itself the decision this path is about. Carla's renewal notice sits in a drawer during a hard week at her job. Her Sunday call goes to voicemail twice — once from her side, once from yours. A form her state sends to the address it has is answered after its window, by a woman who has been approved, in every human sense, since the first month — and whose paper now says otherwise.

Your own track continues — you finish strongly, but a step slower than the build season required, because a parent's weeks are finite and you spent yours trusting queues.

At the month's end, Ms. Bell calls with her voice arranged carefully: Carla's file has been closed in her state's system for non-response — 'without prejudice to reopening,' the notice says, in the coldest warm phrase in this scenario. Reopening is possible. Reopening is also a beginning, and beginnings are what this child has already had too many of.

**Choices:**
- Go to the final review and hear what a closed file does to a case → **review_drift**
  - NOTE (shown after choosing): The review will be conducted, as all of them are, from the paper. The paper just changed authors.

## [review_push] The Final Review — Approved, in Time
*Month 15 — Monday, March 29, 2027 — Monday, March 29, 2027 (dayOffset 448)*

The placement approval is in the file — received, confirmed, current — and the review is the rare one that spends its time on arrangements instead of obstacles: travel, school records, the chapter book's remaining pages to be read in the right house.

The fifteen-month point, April 5, 2027, is days away and, for once, beside the point: Milo will be cared for by a relative, which is the first of the exceptions the law names (42 U.S.C. § 675(5)(E)) — not argued, described. Your case remains open; your plan continues; your visits become trips to a house where your sister keeps your son's room.

Ms. Bell closes her folder. 'It should not have taken this long,' she says, to the room generally. The room, which contains no villains, agrees, generally.

**Choices:**
- Sign the placement paperwork, and call Carla from the courthouse steps → **end_aunt**
  - NOTE (shown after choosing): She answers on the first ring. She has been, in every way the file can now prove, answering all year.

## [review_exception] The Fifteen-Month Review — The Packet of Dates
*Month 15 — Monday, April 5, 2027 — Monday, April 5, 2027 (dayOffset 455)*

The clock date arrives: April 5, 2027. Carla's final placement approval has not quite landed — a last transmission sits in its last queue — and the agency's lawyer rises to address the filing duty, in the tone of a person reading weather they did not make.

Then your lawyer stands with the packet. Date by date, the record shows a relative named at the start, a yes never withdrawn, requests lost and resent and confirmed, renewals kept current, contact logged, a study completed and then located, by a parent's records request, in a queue with no name. The delay in this case, the packet concludes, was process — and here is its biography, in the system's own dates.

The agency does not contest a single date. Contesting your own log tends to concentrate the mind wonderfully on agreeing with it.

**Choices:**
- Listen for the words 'documented' and 'deferred' in the same sentence → **end_exception**
  - NOTE (shown after choosing): A continuance toward a relative is not the ending anyone drew in the first month. It is the ending the record built when time ran out.

## [review_parent] The Final Review — Your Track, Finished First
*Month 15 — Monday, March 29, 2027 — Monday, March 29, 2027 (dayOffset 448)*

The housing held. The letter became keys, the keys became a trial schedule, and the final review is held with Milo's overnight bag already, in the plan's careful language, 'transitioning.' The judge spends her questions where this case's strength has quietly moved: your completion, your visits, the room, the school plan — your track, documented at every step you controlled.

Carla appears in the order in one sentence your lawyer insisted on and the file fully supports: the relative placement, pursued continuously and near completion, is noted and held in reserve should it ever be needed. It will, everyone in the room now believes, never be needed. It is in the order anyway, because this family has learned what undone paperwork costs.

The interstate process does not get finished today. It gets something better: outrun, by a parent, in public, on paper.

**Choices:**
- Take Milo home on the trial schedule — the paperwork still traveling behind you → **end_reunified**
  - NOTE (shown after choosing): Keys in one hand, folder in the other. The folder got lighter this year only once: today.

## [review_drift] The Fifteen-Month Review — The Closed File
*Month 15 — Monday, April 5, 2027 — Monday, April 5, 2027 (dayOffset 455)*

The clock date is April 5, 2027, and the review is conducted from a file that changed while nobody was tending it. Carla's placement: closed for non-response in her state, reopening possible, timeline unknown — the worker reads it flatly, the way one reads any fact one did not cause and cannot repair from a chair. Your track: strong, and months from housing — honored in the report and insufficient, today, to carry the hearing alone.

No exception is documented. The relative is not caring for Milo, and the record of why not — a year of process delay that was never assembled into dates while it happened — cannot be built retroactively in a morning, though your lawyer, to her credit, tries with what exists. The agency states it will file, and the judge, who can only rule on the record in front of her, does not disagree on the record in front of her.

In the corridor afterward, you call Carla. She is horrified — at the closure, at herself, at a system that let a willing aunt lapse on a form. 'I didn't quit,' she says, and she is right, and the file says otherwise, and both of those facts will outlive this afternoon.

**Choices:**
- Go home and open a new folder — labeled, this time, with everything you've learned → **end_collapse**
  - NOTE (shown after choosing): The case resets to one track. Yours. It has been the strongest track all along; now it has to be the only one, and on a harder clock.

## [end_aunt] Ending — With Carla, Before the Clock
*Month 15 — Friday, April 2, 2027 — Friday, April 2, 2027 (dayOffset 452)*

**Ending.**

**Debrief:**
- THE BOARD, WHOLE: Three clocks ran. Milo's reached toward fifteen of the most recent twenty-two months — the point, April 5, 2027, when the agency's filing duty changes (42 U.S.C. § 675(5)(E)) — and the placement landed days before it. Carla's paperwork clock ran its own race of expiries and renewals, and finished current. Your clock ran in parallel the whole way: treatment, parenting, work, housing-in-progress — unfinished at the placement, and deliberately so; your case stays open, your plan continues, and the goal it now serves is a child already living with family.
- WHAT THE RECORD SHOWED: A relative named in writing at the first table. A study request lost between states — and found, because a parent requested her record (55 Pa. Code § 3130.44(d): 'shall be released upon request') and read a log nobody had assembled. A resend with a confirmed receipt. Renewals made before their windows closed. A finished study traced through a nameless queue by a second records request, its delay documented as transmission and queue time — process, not family. In the end the exception in § 675(5)(E) for a child being cared for by a relative was not an argument anyone had to make. It was a description the paperwork finally caught up to.
- WHAT WAS NEVER YOURS TO CONTROL: Two states' queues, a caseworker's caseload in a state you have never visited, which judge read the file, Carla's employer's flexibility, and plain luck — the lost first request could have stayed lost another season, and in many cases like this one, it does. Outcomes turn on workers, judges, and luck as much as on families. What your choices controlled was whether the family's effort stayed visible and current while time passed. Time passed anyway. The effort is why it did not pass in vain.

## [end_exception] Ending — The Clock Struck; the Record Answered
*Month 16 — Monday, May 3, 2027 — Monday, May 3, 2027 (dayOffset 483)*

**Ending.**

**Debrief:**
- THE BOARD, WHOLE: Milo's clock struck fifteen of the most recent twenty-two months on April 5, 2027 (42 U.S.C. § 675(5)(E)) with the placement approved in substance but not yet complete — the last paperwork still traveling. Carla's clock finished current: every renewal made, every form answered, her file never lapsing. Your clock kept running beside both — progress documented, housing not yet landed — and your case remains open on your track, unfiled-against and unfinished. Days after the review, the final approval completed its journey, and Milo's placement with Carla was made — after the clock date, on the strength of a record built before it.
- WHAT THE RECORD SHOWED: The exception was documented, not presumed. At the fifteen-month review, the file — in the agency's own correspondence logs and the packet assembled from them — showed a relative placement pursued from the first month, delayed at identified points by a request never received, a study waiting in a queue, and paper expiring on schedule: delay by process, proved with dates, not delay by family. On that record the agency documented its reason and deferred filing while the relative placement completed (42 U.S.C. § 675(5)(E)). Read the victory precisely: no rights were terminated, none were restored, and your reunification track was neither won nor lost — it was preserved, alongside a child now living with his aunt. The records requests that found the gaps (55 Pa. Code § 3130.44(d)) were the hinge: without them, this packet is a family's sincere claim. With them, it was the system's own biography of its year.
- WHAT WAS NEVER YOURS TO CONTROL: The queues themselves, the lost request, the expiry dates, a stranger-judge's reading, Carla's stamina being finite, and the luck that the gaps in your case were findable gaps. Another family, equally continuous, whose lost paper left no log to request, reaches the filing ending in this same scenario. Outcomes turn on workers, judges, and luck. What your family controlled — a yes maintained, dated, renewed, and logged across fifteen months — turned out to be the only currency the clock accepts. You paid it on time, in installments, all year.

## [end_reunified] Ending — Home With You; the Paperwork Outrun
*Month 15 — Monday, April 19, 2027 — Monday, April 19, 2027 (dayOffset 469)*

**Ending.**

**Debrief:**
- THE BOARD, WHOLE: Milo's clock was days from its fifteen-month point (April 5, 2027; 42 U.S.C. § 675(5)(E)) when the trial return began — ordered before the point, on your track's documented completion: treatment, parenting, employment, and housing that landed, after a year of looking unlandable, in the final stretch. Carla's clock finished the year current and unneeded: her placement remains noted in the order as the family's standing resource, approved in substance, its paperwork completing at its own pace behind an ending that no longer waits on it. The interstate process — the slow antagonist of this whole scenario — was not defeated. It was outrun, which is the only way it ever loses.
- WHAT THE RECORD SHOWED: Two complete files. Yours: a plan started in the first month and finished in the open, visits that grew as you did, a housing letter that became keys. Carla's: a relative named on day one (in your writing), a yes sustained and documented — records requested and read (55 Pa. Code § 3130.44(d)), a lost request found and resent, renewals met, contact logged — so that at the final review the court was choosing between two documented goods instead of rescuing one stranded hope. That abundance was built, not found: it exists because both tracks were run, all year, as if the other might fail. Either track alone reaches a poorer room in this scenario; together they reached this one.
- WHAT WAS NEVER YOURS TO CONTROL: The housing program's timing most of all — a letter arriving a season later moves this child to his aunt's ending or worse, through no change in your effort — plus two states' queues, Carla's employer, judicial assignment, and the foster family's kindness, which was luck wearing a human face. Reunification orders also come with supervision and a case that closes slowly behind them; this ending is a beginning with paperwork, not a curtain. Outcomes turn on workers, judges, and luck. Your piece was running both tracks on paper until one of them came home. One of them did.

## [end_collapse] Ending — The Placement That Died of Silence
*Month 15 — Monday, April 19, 2027 — Monday, April 19, 2027 (dayOffset 469)*

**Ending.**

**Debrief:**
- THE BOARD, WHOLE: Milo's clock struck fifteen of the most recent twenty-two months on April 5, 2027 with no exception documented, and the agency filed as its duty directed (42 U.S.C. § 675(5)(E)). Carla's clock is the cautionary one: her approvals did not fail — they lapsed, unanswered, in the final stretch, and her file was closed for non-response, reopenable in theory at the speed of a new beginning. Your clock was the strongest of the three and still short: documented progress, housing months away — a track that must now carry the whole case, alone, under a filed petition, on a harder schedule than any it has run yet.
- WHAT THE RECORD SHOWED: A willing aunt, proved willing for a year and then unprovable in the month it counted, because willingness lives in the file only where it is renewed, logged, and answered. The early record was genuinely good — named at the start, checks clear, study favorable — but the late record is the one reviews are conducted from, and the late record showed gaps where renewals and replies should have been, because the tracking tools this scenario keeps offering — records requested and read (55 Pa. Code § 3130.44(d)), dated logs in two states — were used early and then set down. No villain closed Carla's file. Elapsed time and silence did, operating exactly as designed on everything unmaintained. The judge did not find that this family did not care. She found a file that could no longer prove it in time, which in this system is the colder and more useful lesson.
- WHAT WAS NEVER YOURS TO CONTROL — AND WHAT REMAINS: The lost first request, two queues, Carla's job, a dozen pieces of luck — much of this collapse was weather, not choice, and it is not a verdict on anyone's love, least of all Carla's: drift is what the process does to unlogged devotion, in every state. Read the filing accurately, too: a petition is an accusation with a hearing attached, not a termination; grounds must still be proved by clear and convincing evidence, with counsel beside you and your — now strongest — track as the centerpiece. Carla's file can be reopened; your housing can land; the record from here can be built the way the early record was, without the late silence. Parents reach this ending with their devotion intact and their documentation lapsed. What remains fully theirs is the file from today. It is still being written.
