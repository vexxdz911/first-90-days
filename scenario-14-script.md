# THE FIRST 90 DAYS — Scenario 14: “The Waiting List”

*Human-readable script. This document and `scenario-14.json` are generated from a single source and match node-for-node: same IDs, same order, same choices, same effects.*

**The family is fictional — a composite. No real person's story appears here.**

**Content note:** This scenario depicts a parent in early recovery whose court-ordered program has a six-week waiting list, while the rest of her case plan runs at full speed. It is told through intake letters, check-in emails, and review reports. There is no graphic content. Players may skip any scene or use the quick exit at any time.

**How to read effects:** `cash −40` changes the player's cash. `FLAG: name` sets a flag the engine tracks. `HIDDEN + item` means the case file quietly records that item at this choice — the player does not see it when it happens. `NOTE:` is text shown to the player right after choosing.

Start date: Monday, May 4, 2026. Day offsets are days since the scenario's start date. Tier: Hard.

## [start] The Order and the List
*Day 0 — Monday, May 4, 2026 — Monday, May 4, 2026 (dayOffset 0)*

The review order is specific, and specific is supposed to be good: the court ordered you into Harborview, the county's trauma-informed parenting and recovery program — twelve weeks, the one your counselor called 'the real one, not the checkbox one.' Your daughter Wren, four, is with a foster family across the river. You are ten months into this case, doing everything on the plan that can be done by trying.

You call Harborview the same afternoon, from the courthouse steps, because you have learned that in this system the day you are told to do a thing is the day the clock starts judging you for not having done it. The intake worker is kind and completely unhurried. There is a waitlist, she says. It is running about six weeks.

**Choices:**
- Take the intake appointment she offers — the soonest one, this week → **intake**
  - NOTE (shown after choosing): Six weeks to start a twelve-week program, in a case with its own calendar. You write the date on your hand, the way you used to write everything that mattered.

## [intake] Name on the List
*Day 3 — Thursday, May 7, 2026 — Thursday, May 7, 2026 (dayOffset 3)*

Intake takes ninety minutes and you bring everything: ID, insurance card, the court order itself, folded twice in your bag. The worker completes your assessment, confirms you're an appropriate referral — the program wants you — and writes your name on the waitlist. Fourteenth, she says, though the number moves as crises bump people up, which you cannot begrudge and cannot fix.

Your earliest start, if the list moves at its usual pace, is Thursday, June 18, 2026 — six weeks out. She says it conversationally, the way people state weather. In your file, in six weeks' worth of reports, that sentence will have many chances to be rewritten by other hands. The only question this scenario asks is whether it gets written down now, by the program, in ink.

**Choices:**
- Ask for the waitlist confirmation in writing — position, date, earliest start → **letter**  _(cash -3; HIDDEN + Waitlist — intake completed; start six weeks out, confirmed by the program in writing)_
  - NOTE (shown after choosing): She prints it without fuss. Programs print these every day. The fuss is never in the printing; it's in the remembering to ask.
- Take the verbal estimate — you don't want to seem difficult at a program you need → **no_letter**
  - NOTE (shown after choosing): Difficult is a reputation you can't afford. Neither, it turns out, is its opposite. You leave with a date in your memory and nothing in your hand.

## [letter] The Letter, Kept
*Day 4 — Friday, May 8, 2026 — Friday, May 8, 2026 (dayOffset 4)*

The confirmation is one page: your name, your intake date, your waitlist position, the earliest projected start — Thursday, June 18, 2026 — and a line you read three times on the bus: 'Delay is due to program capacity.' Eight words. You put the page in the folder where Wren's drawings from visits live, because that is your filing system now: the case, and the reason for the case, in one folder.

You do not know yet what this page is worth. Nobody can tell you, because its value depends on a room you haven't been in yet — a review, months from now, where someone reads a report that says when you 'began services.'

**Choices:**
- Go on with the rest of the plan — visits, screens, meetings, all of it → **meanwhile**
  - NOTE (shown after choosing): The waitlist waits. Everything else in the plan does not. That asymmetry is the next two months of your life.

## [no_letter] A Date in Your Memory
*Day 4 — Friday, May 8, 2026 — Friday, May 8, 2026 (dayOffset 4)*

The date lives in your memory, where it is accurate, sincerely held, and completely inadmissible. Memories don't get attached to reports. In the weeks ahead, when the subject of Harborview comes up — and it will come up in rooms you're not in — the available facts will be the program's start date and the order's date, with six weeks of unexplained space between them, and unexplained space in a case file is a vacuum that other people's sentences rush to fill.

You go on with the rest of the plan, because the rest of the plan is not waiting for anything. Only the ordered treatment is. Only you know why. Knowing is not the same as the record knowing, and the record is what's coming.

**Choices:**
- Go on with the rest of the plan — visits, screens, meetings, all of it → **meanwhile**
  - NOTE (shown after choosing): Fourteen names ahead of yours. A plan running at full speed around one frozen line.

## [meanwhile] Everything Else on the List
*Day 10 — Thursday, May 14, 2026 — Thursday, May 14, 2026 (dayOffset 10)*

The rest of the plan does not care about the waitlist. Visits with Wren, twice a week, on time, with the snack she likes and the book you're reading to her in installments. Screens, random, all submitted. Support meetings, signed sheets. Your counselor's other groups. Your part-time shifts at the diner, scheduled around all of it by a manager who has decided, privately, to be one of the people who helps.

At the team meeting you don't attend, your case is summarized in the ordinary way: strong engagement across services — and, on the Harborview line, a blank that is already starting to be described in the draft language of reports as 'pending parent initiation.' Pending. Initiation. You initiated it on the courthouse steps, the day of the order. The draft has not met your folder yet.

**Choices:**
- Ask your lawyer what happens to a six-week wait on paper — before it hardens into a sentence about you → **records_fork**
  - NOTE (shown after choosing): 'Pending parent initiation.' Two words doing the work of an accusation, in draft, where accusations are still soft enough to correct.

## [records_fork] Whose Delay Is It?
*Day 14 — Monday, May 18, 2026 — Monday, May 18, 2026 (dayOffset 14)*

Your lawyer listens to the whole story — the call from the courthouse steps, the intake, the list — and asks the question this scenario turns on: 'If the agency's report says you started late, what paper answers it?' A party may request the case record in writing, and it 'shall be released upon request' (55 Pa. Code § 3130.44(d)). The file would show what the agency itself recorded about Harborview: the referral date, and what, if anything, anyone wrote about capacity.

She is equally clear about the second instrument: the program. A waitlist is a fact about a program, and facts about programs can be documented by anyone they happen to — if that person keeps the paper and keeps asking, in writing, on a schedule.

**Choices:**
- Sign the written request for the record — referral, case notes, all of it → **file_copy**  _(FLAG: recordsRequested)_
  - NOTE (shown after choosing): Signed, dated, copied. Whatever the file says about the wait, you'll soon be able to quote it instead of characterizing it.
- Rely on your own account — you know what you did and when → **memory_track**
  - NOTE (shown after choosing): You do. The review will not ask what you know. It will ask what can be shown, and those are different examinations.

## [file_copy] The File So Far
*Day 20 — Sunday, May 24, 2026 — Sunday, May 24, 2026 (dayOffset 20)*

The record, when it comes, is illuminating in the specific way of empty rooms. The agency's referral to Harborview is dated the week after the order — good, prompt, on the record. And then: nothing. No note about capacity. No note about a waitlist. The service line in the case chronology reads, in full: 'Harborview — referred. Parent to begin.'

'Parent to begin.' As if beginning were a door you were standing in front of, declining to open. The file doesn't accuse you. It does something more dangerous: it describes a six-week system delay in grammar that assigns the delay to the only person named in the sentence — you.

**Choices:**
- Show your lawyer the waitlist letter (if you have it) and ask what else the record needs → **bus_money**  _(HIDDEN + Case chronology — 'Harborview: referred. Parent to begin.' No mention of capacity or waitlist)_
  - NOTE (shown after choosing): 'The file says you were referred and told to begin,' she says. 'Now we document why beginning wasn't yours to schedule.'
- Ask what can still be done from here — the wait is half over → **bus_money**
  - NOTE (shown after choosing): Half a wait documented late is still a wait documented. The record needs a second half with paper in it.

## [memory_track] Your Word Against a Form
*Day 20 — Sunday, May 24, 2026 — Sunday, May 24, 2026 (dayOffset 20)*

Without the file, you can't see the sentence you're up against — 'Parent to begin' — and you can't quote the referral date that actually helps you. Your lawyer works from what you carry: your memory of the intake, your sign-in sheets from everything else, your certainty. She believes you, in the way of this entire system: warmly, personally, and in a manner that cannot be attached to a report.

What she can still build, she says, is the forward record: from today, the wait gets documented as it happens, in writing, on both ends — yours to the program, and the program's replies to you. Dated paper generated now beats remembered paper argued later, every time, in every room.

**Choices:**
- Start the forward record today — every contact about the wait, in writing → **bus_money**
  - NOTE (shown after choosing): Today. The waitlist doesn't pause while the record catches up, but the record can start catching up while the waitlist runs.

## [bus_money] Two Buses
*Day 22 — Tuesday, May 26, 2026 — Tuesday, May 26, 2026 (dayOffset 22)*

A practical chapter, because cases are lost on logistics as often as on law: Harborview is two buses from your room, the diner is one, and Wren's visits are a third route entirely. Your manager gives you the shifts that fit the visits. The bus pass is a line in your budget written in the ink of actual arithmetic: $96 a month, non-negotiable, because every service you can control runs on it.

You think about the shape of your case the way you'd describe it to Wren someday: everything you could do, done — and the one thing you couldn't, waiting on a list with your name spelled right, while the calendar that judges you keeps its own counsel about whose delay it was.

**Choices:**
- Spend the pass money and protect the routes — visits and meetings are yours to control → **weekly**  _(cash -96)_
  - NOTE (shown after choosing): Ninety-six dollars to remain, on every line except one, a person who shows up. Showing up is your whole reputation. It is worth the money. It is also all the money.
- Save the pass and walk the long routes when you can → **weekly**
  - NOTE (shown after choosing): Walking saves money and spends the only other currency you have. Either way, the waitlist doesn't shorten. Only your documentation of it can grow.

## [weekly] The Thursday Call
*Day 24 — Thursday, May 28, 2026 — Thursday, May 28, 2026 (dayOffset 24)*

The wait has a rhythm available to it, if you choose to impose one: Harborview's intake office answers email. A short message every Thursday — your name, your waitlist position, a request to confirm you're still active and whether any slot has opened — creates a thread. Threads have dates. Dates are the bricks records are built from.

The alternative rhythm is the telephone: kind, human, immediate — and gone. A phone call about a waitlist proves, later, exactly as much as the waitlist coordinator's memory of it, which is to say whatever she happens to write down, which is usually the slot changes and not your calls.

**Choices:**
- Write the Thursday email — and write it every Thursday, replies saved → **paper_trail**
  - NOTE (shown after choosing): First reply comes in an hour: position confirmed, no movement, 'thank you for checking in.' A nothing of an email. Nothings with dates are somethings.
- Call instead — a voice feels harder to ignore → **verbal_trail**
  - NOTE (shown after choosing): She is warm. She remembers you. Warmth and memory are excellent qualities in a person and terrible qualities in a filing system.

## [paper_trail] A Thread of Thursdays
*Day 25 — Friday, May 29, 2026 — Friday, May 29, 2026 (dayOffset 25)*

The thread grows: your check-in, her reply; your check-in, her reply. Position twelve. Position eleven. 'No clinical slots this week.' Each exchange is thirty words and none of them will ever be read aloud anywhere — that is not what they're for. They are for the day someone writes 'parent delayed beginning services,' when your lawyer can attach a thread that shows you knocking, in writing, every seven days, on a door that opened on the program's schedule and no one else's.

At your support meeting, a woman six months ahead of you in her own case says the thing veterans of this system say: 'The wait isn't the problem. The wait being your fault on paper is the problem.' You go home and send the Thursday email a day early, just to watch it sit there, dated.

**Choices:**
- Keep the rhythm — and keep everything else on the plan perfect → **sponsor**  _(HIDDEN + Waitlist check-ins — written weekly; program replies saved, positions confirmed)_
  - NOTE (shown after choosing): Perfect is a heavy word. In this case it just means: the only blank line in your file is the one the program owns.

## [verbal_trail] Warm and Unrecorded
*Day 25 — Friday, May 29, 2026 — Friday, May 29, 2026 (dayOffset 25)*

The calls are pleasant and the coordinator does remember you — she says your name before you give it, which feels like progress and is, in every way except the one that will matter. Nothing is written: not your calls, not the positions she quotes you, not the week a slot opened and closed to a crisis referral while you were at the diner with your phone in your locker.

You are, in the lived sense, managing this wait actively and well. In the filed sense, the wait is happening to a person who has made no documented contact with the program since intake. Both statements are true. Only one of them will be in the room at the review.

**Choices:**
- Keep calling — and start writing down each call afterward, date, time, what was said → **sponsor**
  - NOTE (shown after choosing): Notes made after calls are weaker than threads and stronger than silence. The ladder has many rungs; the mistake is standing on none of them.

## [sponsor] The Woman From the Meeting
*Day 28 — Monday, June 1, 2026 — Monday, June 1, 2026 (dayOffset 28)*

Denise, from your support meeting — two years sober, a lanyard of service chips, a voice like a closing argument — offers you her spare bus pass for the month and a ride on Harborview start day, whenever it comes. Accepting help is a skill this system quietly tests for and never lists: the plan says 'natural supports,' and means, in part, whether anyone in your life would drive you to the door that finally opens.

You accept the ride and decline the pass — you already spent your own $96, or you're walking; either way you keep the arrangement small and specific, the way durable help usually is. She writes her number on the back of a meeting schedule, which you file, because by now you file everything. Paper is a habit. Habits are what files are made of.

**Choices:**
- File her number, thank her, and check the list again Thursday → **opening**
  - NOTE (shown after choosing): Start day: unknown. Ride: arranged. In a case being decided by calendars, an arranged ride is a form of readiness.

## [opening] A Slot Opens — For Someone Else
*Day 31 — Thursday, June 4, 2026 — Thursday, June 4, 2026 (dayOffset 31)*

In week five, a slot opens at Harborview — and closes the same day to an emergency referral, a mother whose situation the program triages ahead of yours. You learn about it Thursday, in reply to your check-in (or on the phone, in the warm voice, leaving no trace of itself). You cannot begrudge the woman who got it. You have been the emergency in rooms like this. Triage is not injustice; it's arithmetic with a conscience.

But arithmetic needs recording, because five weeks from now, in a report, 'the program had an opening the parent did not take' is a sentence that could exist — wrong, but available — unless the paper already says what actually happened: a slot opened, a crisis took it, and you were confirmed still waiting, in writing, that same week.

**Choices:**
- Ask the program to confirm the triage week in writing — slot opened, crisis referral, you're still listed → **in_writing**  _(cash -3; HIDDEN + Waitlist — slot opened week five, filled by crisis referral; parent confirmed still waiting, in writing)_
  - NOTE (shown after choosing): The reply is two lines and worth more than most letters in your folder: the program's own account of its own queue, dated inside your wait.
- Raise it at the front desk next time you're nearby — it should be acknowledged → **desk_scene**
  - NOTE (shown after choosing): Acknowledged it may be, warmly, in person, unrecorded — the official motto of every path in this story that ends badly.

## [in_writing] Two Lines, Dated
*Day 33 — Saturday, June 6, 2026 — Saturday, June 6, 2026 (dayOffset 33)*

The program's reply sits in your folder like a coin from another country: small, dense, legal tender somewhere else. 'Slot opened and was assigned per triage protocol. You remain active on the waitlist.' With it, your folder now contains an unbroken account of the wait, authored substantially by the system itself: the order, the intake confirmation, the Thursday thread, the triage note.

Your lawyer, shown the folder, says the sentence that is this scenario's entire thesis: 'If the report says you delayed, we don't argue. We attach.'

**Choices:**
- Keep everything — and go on showing up to everything else → **screen_day**
  - NOTE (shown after choosing): Attach. Not argue. You practice the folder the way you practice everything else now: in date order.

## [desk_scene] The Front Desk
*Day 33 — Saturday, June 6, 2026 — Saturday, June 6, 2026 (dayOffset 33)*

The front-desk conversation is everything the email would not have been: human, sympathetic, and evanescent. The coordinator agrees the triage was hard luck, agrees you were 'right there,' agrees it's 'not fair how it looks.' All of it true, all of it spoken, none of it kept. Her screen shows your name and a status — 'waitlist — active' — that has not changed its wording since intake day and does not mention you at all.

You walk out understanding that fairness, in this building, is a thing people feel and files don't. The wait has two more weeks in it. What fills them, on paper, is still largely up to you.

**Choices:**
- Go on showing up to everything else — and start putting the calls in writing too, late but now → **screen_day**
  - NOTE (shown after choosing): Late documentation is a lesser instrument. It is not a useless one. The wait still has weeks to testify about.

## [screen_day] The Other List
*Day 38 — Thursday, June 11, 2026 — Thursday, June 11, 2026 (dayOffset 38)*

While Harborview's list crawls, the plan's other machinery keeps perfect time: a random screen this week, submitted within the window; Wren's visits, both of them, with the installment book nearly finished; a support meeting where Denise speaks and you hear your own sixth week described by someone who survived hers.

Your file, for anyone who reads all of it, now has a strange and telling shape: page after page of compliance with dates attached — and one line, Harborview, standing still. Standing-still lines in files get explained by whoever writes the next summary. The candidates for that authorship are the agency's report writer, working from the chronology, or your folder, if your lawyer puts it in front of them first.

**Choices:**
- Wait for the call — you're next, or next-but-one, and Denise's car is ready → **start_day**  _(HIDDEN + Compliance during wait — screens submitted, visits kept, meetings signed; only the waitlisted service outstanding)_
  - NOTE (shown after choosing): Everything you control: controlled. The list: not yours. The folder: yours. That is the whole geometry, and the review will draw it.

## [start_day] Week Seven
*Day 45 — Thursday, June 18, 2026 — Thursday, June 18, 2026 (dayOffset 45)*

The call comes on a Tuesday: a slot, yours, starting Thursday, June 18, 2026 — six weeks and a day after intake, because lists move the way they move. Denise drives you, as arranged, and sits in the parking lot with the engine off and a paperback, the way people wait when waiting is a form of love.

Harborview is everything the counselor promised: serious, unhurried, human. Your clinician, Ms. Adeyemi, does your treatment plan and says the program runs twelve weeks — which means it will end after the next review, not before it. The review will therefore judge a program in progress, begun six weeks after it was ordered. Everything now depends on a question of attribution: whose six weeks were they?

**Choices:**
- Attend the first session like it's the courthouse steps all over again — fully, on time, documented → **counselor_call**
  - NOTE (shown after choosing): Session one: attended, noted, signed. The start date is finally in the file. The question is what stands next to it.

## [counselor_call] The Clinician's Question
*Day 52 — Thursday, June 25, 2026 — Thursday, June 25, 2026 (dayOffset 52)*

Two sessions in, Ms. Adeyemi asks you — clinically, not unkindly — about the gap: 'The order was in May. You were ready in May. The file note I got says 'began late.' Do you know why it says that?' It is the first time anyone inside the system has asked you the question directly, and you hear your answer come out in the two dialects your case now speaks: the lived one ('I was on the list the same week as the order') and the filed one, which depends entirely on what your folder can show her.

She writes something in her own notes. Clinicians' notes become reports; reports become records; records become the version of your spring that outlives everyone's memory of it, including yours.

**Choices:**
- Tell her the whole chronology — and offer the folder's dates if she wants them for her report → **progress**
  - NOTE (shown after choosing): Dates, offered without heat. You have learned the system's deepest stylistic rule: the calmest document in the room usually wins the room.

## [progress] Three Sessions In
*Day 59 — Thursday, July 2, 2026 — Thursday, July 2, 2026 (dayOffset 59)*

Three sessions in, your attendance is perfect and Ms. Adeyemi's progress note says so, in the vocabulary files respect: 'engaged, prepared, progressing.' The program will take nine more weeks. The review is in three. Wren's visits continue; the installment book has been finished and a new one started, because four-year-olds experience sequels as a moral category.

Your lawyer requests the agency's draft report for the review — an ordinary move, rarely made — because drafts are where sentences like 'began services late' can still be met with attachments instead of arguments. The draft arrives the week before the hearing, and the sentence is there, almost exactly as predicted. Almost. What follows it depends on what your choices have put in your lawyer's hands.

**Choices:**
- Read the draft sentence twice, the way frightened people read everything now — then prepare the answer → **agency_report**  _(HIDDEN + Harborview progress — three sessions attended; clinician note: engaged, progressing)_
  - NOTE (shown after choosing): 'Parent began services in late June, approximately six weeks after referral.' A true sentence, arranged to imply a false one. The reply is an arrangement too.

## [agency_report] The Draft Report
*Day 66 — Thursday, July 9, 2026 — Thursday, July 9, 2026 (dayOffset 66)*

The draft's Harborview paragraph is four lines long. Referred in May — began in June — progressing well. Between the first line and the second, six weeks pass without an owner. Your lawyer reads it and says: 'Reports hate a vacuum almost as much as nature does. Reviewers fill gaps with the nearest character trait. Our whole job this week is to fill this one with the program's own paper first.'

She assembles the reply the way this scenario has taught you everything is assembled: the order, the intake confirmation or its absence, the Thursday thread or its absence, the triage note or its absence, the chronology line — 'Parent to begin' — that nobody in the agency can now unwrite. The folder goes to the agency and into the court packet. What the hearing does with it is the hearing's. What it cannot do is unexist.

**Choices:**
- Go to the review with the folder in date order → **hearing**
  - NOTE (shown after choosing): Date order. The wait, testified to by the wait's own paperwork.

## [hearing] The Review
*Day 73 — Thursday, July 16, 2026 — Thursday, July 16, 2026 (dayOffset 73)*

The agency presents its report first, and the Harborview line gets its four lines — but reports are read against packets now, and the packet is in the judge's hands before the sentence is reached. What happens next depends, with a precision this scenario has been honest about from its first page, on what your choices actually put in that packet.

The judge looks at you once during the Harborview discussion, not unkindly. Judges see this exact gap — an order, a wait, a late start — in file after file. What they rarely see is the gap documented by the family and the program together, in date order, with no heat in it. Rare things get read carefully. That is the only promise this scenario has ever made you.

**Choices:**
- Let the full packet speak — order, intake letter, Thursday thread, triage note, chronology → **end_record**
  - NOTE (shown after choosing): Your lawyer says eleven sentences. The attachments say the rest. The room does the arithmetic out loud, which is where arithmetic changes minds.
- Present what you have — some paper, partly dated, assembled late → **end_partial**
  - NOTE (shown after choosing): Half a folder is an argument with missing premises. It still beats the alternative, and the alternative is in the room too, watching.
- Answer from memory — the folder was never built, and your voice is what's left → **end_blamed**
  - NOTE (shown after choosing): Your voice is truthful, detailed, and believed in the way voices are believed in rooms that run on attachments: personally, warmly, and without effect.

## [end_record] Ending — The Delay Has a Name
*Day 80 — Thursday, July 23, 2026 — Thursday, July 23, 2026 (dayOffset 80)*

**Ending.**

**Debrief:**
- WHAT THE FILE HELD (the hidden record, revealed): An unbroken, dated account of the six weeks, authored mostly by the system itself: the program's intake confirmation ('delay is due to program capacity'), your weekly written check-ins with the program's replies, the triage note for the week-five slot, and the agency chronology's own fatal phrase — 'Parent to begin' — now answered by the program's paper. At the review, the report's implication did not survive contact with its own attachments: the delay was attributed, on the record, to the waitlist. Your program continues — nine weeks remain, and no honest debrief will call this case won. What is won is narrower and load-bearing: the six weeks are recorded as the system's, and every future reader of this file will meet them that way.
- THE PROCESS UNDER THIS PATH (described, keeping to this scenario's verified law): This is the record the federal clock makes valuable. Under the ASFA framework in this scenario's verified set, when a child has been in foster care for 15 of the most recent 22 months, the agency is generally to file for termination — except, among the statute's three exceptions, where the agency has identified services necessary for the child's safe return that it has not provided to the family (42 U.S.C. § 675(5)(E)). A court-ordered program that sat on a six-week waitlist is that exception's exact shape — but only if the record proves the service was identified and not provided in time, rather than offered and declined. Your folder is what makes it provable. Note what the exception is and is not: it speaks to the filing decision, and any later termination case would still have to be proven by the agency by clear and convincing evidence on grounds this scenario does not reach. The exception buys the truth a hearing. It does not decide the hearing.
- THE HONEST PART: The judge could have noted the attribution and pressed the timeline anyway — children's clocks are real too, and Wren spent those six weeks four years old, in someone else's house, whatever the paperwork says. A different report writer might have contested the folder; a different program might never have put 'capacity' in writing. Workers, clinicians, judges, and a coordinator who answered emails all held pieces of this. Your share was the discipline the scenario is named for: you documented a delay that everyone agreed was not your fault, as if it would someday be treated as your fault — because in this system, undocumented innocence expires. It didn't, this time, because you didn't let it.

## [end_partial] Ending — Started Late, Half-Credited
*Day 80 — Thursday, July 23, 2026 — Thursday, July 23, 2026 (dayOffset 80)*

**Ending.**

**Debrief:**
- WHAT THE FILE HELD (the hidden record, revealed): A partial account: some dates, some paper, assembled partly after the fact — a program status line here, your own notes there, gaps where the Thursday thread or the intake letter would have been. At the review, the partial record did partial work: the judge declined to adopt the report's implication wholesale, the agency conceded the program 'had capacity constraints' in general terms, and the six weeks were entered as contested rather than attributed. Your program continues, your compliance elsewhere is undisputed, and the file's account of the wait is a draw — which, against a draft that began as 'parent began late,' is movement, and against what the full folder would have done, is a lesson with a price tag.
- THE PROCESS UNDER THIS PATH (described, keeping to this scenario's verified law): The ASFA services exception (42 U.S.C. § 675(5)(E)) — services identified in the plan but not provided to the family — is a record-dependent argument: it lives or dies on whether the documentation establishes that the delay was the system's. Contested paper produces contested outcomes. The tools were the verified ones throughout: the case record on written request (55 Pa. Code § 3130.44(d)) showed the chronology's 'Parent to begin' and the bare referral date, and counsel (42 Pa.C.S. § 6337) could build only from what existed. Nothing in this ending says you failed at the wait — managing it by phone and memory is managing it. It says the review priced your proof, not your effort, because reviews can only price what is in front of them.
- THE HONEST PART: A contested six weeks may matter less than it feels today: you are progressing in the program, your other lines are clean, and the next review will weigh nine more weeks of attendance against a stale argument about a spring waitlist. Judges differ in how much ambiguity they hold against the party who didn't create it, and this judge split the difference, as many do. What remains true is the mechanism, and it is portable to everything else in this case and beyond it: in a paper system, the side that documents the system's delays owns them, and the side that merely survives them rents the explanation month by month. Your folder, from here, is a habit looking for its next use. It will find one.

## [end_blamed] Ending — Six Weeks, Rewritten
*Day 80 — Thursday, July 23, 2026 — Thursday, July 23, 2026 (dayOffset 80)*

**Ending.**

**Debrief:**
- WHAT THE FILE HELD (the hidden record, revealed): Four lines in a report — referred in May, began in June — and a folder that was never built to answer them. The review adopted the report's framing, because the report was the only framed thing in the room: the six weeks entered the record as a period of parental delay. Not because anyone proved you delayed. Because no one could prove, from paper, that you didn't — and in this system, at review, the burden of explaining a gap falls on the person the gap is about, whether or not she caused it. The waitlist coordinator who remembers your calls will not be at the next review. Her memory was never the record. It was just the truth, which is a different and less durable substance here.
- THE PROCESS UNDER THIS PATH (described, keeping to this scenario's verified law): This is the ending the ASFA services exception exists to prevent — and it shows the exception's precondition. Under 42 U.S.C. § 675(5)(E), identified-but-unprovided services can except a case from the 15-of-22 filing rule; but the exception is an argument, and arguments need exhibits. The exhibits existed in potential all spring: the program would have confirmed the wait in writing (programs do, daily, when asked); the case record was available on written request (55 Pa. Code § 3130.44(d)) and quoted the chronology against itself; counsel (42 Pa.C.S. § 6337) was there to assemble it. Any future termination case would still require the agency to prove its grounds by clear and convincing evidence — that protection is real and untouched by this ending. But the filing decision this record invites is the one the exception, documented, exists to forestall.
- THE HONEST PART: Let the record of this debrief be as fair as the review wasn't: you did everything except document. You called from the courthouse steps, you completed intake in three days, you kept every other line of the plan, and the delay was the program's capacity — full stop. The injustice of this ending is not that the system doubted your sincerity; it's that sincerity was the wrong currency, and nobody handed you the exchange rate until the draft report was written. Workers with smaller caseloads sometimes write the capacity note themselves; the published cases behind this scenario include parents whose waitlists were testified about only afterward, when the testimony could describe the delay but no longer relocate it. Your program continues either way, and a folder begun at the next review is worth more than this paragraph's regret. The wait was the system's. Next time, make the system sign for it.
