# THE FIRST 90 DAYS — Scenario 57: “The Referral That Never Came”

*Human-readable script. This document and `scenario-57.json` are generated from a single source and match node-for-node: same IDs, same order, same choices, same effects.*

**The family is fictional — a composite. No real person's story appears here.**

**Content note:** This scenario depicts an in-home case under court supervision: a court-ordered parenting program, a referral that goes missing, progress notes, and a review hearing, told through calls, emails, and file pages. There is no graphic content. Players may skip any scene or use the quick exit at any time.

**How to read effects:** `cash −40` changes the player's cash. `FLAG: name` sets a flag the engine tracks. `HIDDEN + item` means the case file quietly records that item at this choice — the player does not see it when it happens. `REQUIRES FLAG: name` means the choice is only available if that flag was set earlier; `REQUIRES NO FLAG: name` means it is only available if that flag was never set. `NOTE:` is text shown to the player right after choosing.

Start date: Monday, March 16, 2026. Day offsets are days since the scenario's start date. Tier: Foundation.

## [start] The Plan and the Promise
*Day 0 — Monday, March 16, 2026 — Monday, March 16, 2026 (dayOffset 0)*

Your name is Colleen. Your daughter Nia is six, and she is home with you — this is an in-home case, under court supervision, and the plan is the paper version of the help everyone agreed your family would get.

The plan orders a parenting program: Brightpath Parenting, twelve sessions, the one the plan names by name. At the last meeting, your worker, Ms. Voss, told you the referral had been sent. All you have to do, she said, is call Brightpath and schedule.

You believe her. There is no reason not to. Believing people is not the problem in this story; what the file does with the next five weeks is.

**Choices:**
- Call Brightpath this week to schedule, the way the plan says → **program_call**
  - NOTE (shown after choosing): You call on your lunch break, with the plan open on the table and a pen ready for dates.

## [program_call] No Referral on File
*Day 2 — Wednesday, March 18, 2026 — Wednesday, March 18, 2026 (dayOffset 2)*

You call Brightpath on Wednesday, March 18, 2026. The intake worker is pleasant. She types, she waits, she types again. Then she says the sentence this scenario is built from: there is no referral on file for you. Not pending, not misfiled — not there.

She checks under your name twice, and under Nia's. Nothing. She suggests, kindly, that you ask your worker to send it, and gives you the program's email address in case it helps to have it in writing.

You hang up with an email address, a pen still in your hand, and a plan that says a thing has happened which, at the program that would know, has not.

**Choices:**
- Call Ms. Voss and tell her exactly what Brightpath said → **worker_call**  _(HIDDEN + Brightpath Parenting — no referral on file when mother called to schedule)_
  - NOTE (shown after choosing): Exactly what they said, in their words: no referral on file. You write the date of this call on the plan itself.

## [worker_call] It’s in Process
*Day 4 — Friday, March 20, 2026 — Friday, March 20, 2026 (dayOffset 4)*

Ms. Voss is not dismissive. She says the referral was submitted, that these things take time to land, that it is “in process” and she will check on it. She sounds certain. She may even be right about having submitted something, somewhere.

What you have, at the end of the call, is her certainty — spoken, unrecorded, and held entirely in her memory and yours. What Brightpath has is an empty search result. The case will be measured later by whichever of those two things got written down.

Tonight you can leave it in the world of phone calls, or you can move it into the world of paper. The difference will not matter this week. It will matter in five weeks, in a room you have not been in yet.

**Choices:**
- Send a written email tonight — to Ms. Voss and to Brightpath — saying the referral is not on file and asking both to confirm when it is sent → **written_chase**  _(FLAG: referralChased; HIDDEN + Referral — mother emailed worker and program in writing that no referral was on file)_
  - NOTE (shown after choosing): Short, polite, dated: the plan orders Brightpath; you called; no referral is on file; please confirm when it is sent. Sent emails keep their own dates.
- Accept the assurance — she said she will check on it → **phone_only**
  - NOTE (shown after choosing): She probably will. Checking on it is a thing she will do inside a system that does not record her doing it.

## [written_chase] The Reply, in Writing
*Day 7 — Monday, March 23, 2026 — Monday, March 23, 2026 (dayOffset 7)*

You send the email that evening. Brightpath replies within days, in writing, and their reply is worth more than its two lines suggest: as of this week, the program confirms, it has received no referral for you, and it will contact you the moment one arrives.

Ms. Voss replies too: she is looking into it. No send date is given, because — though nobody writes this part — there may not be one to give.

Your sent folder now holds something the case file does not: a dated account of the gap, written while the gap was still new, by you and by the program itself.

**Choices:**
- Save both replies with the plan, and go on with everything else in the case → **wait_begins**  _(HIDDEN + Program reply — no referral received, confirmed by the program in writing)_
  - NOTE (shown after choosing): Everything else — Nia's school, the home visits, the check-ins — keeps its own schedule. Only this one line is stuck.

## [phone_only] Assured, and Waiting
*Day 7 — Monday, March 23, 2026 — Monday, March 23, 2026 (dayOffset 7)*

You let the phone call carry it. The week feels ordinary: Nia's school, your shifts, the home visit that goes fine. Nothing arrives from Brightpath, but nothing was supposed to arrive quickly — referrals take time to land; you were told so, warmly, by the person whose job it is to know.

What you do not have is any way, later, to show when you first learned the referral was missing, or that you raised it at all. Your memory of the call is clear. Memories are clear in exactly the rooms where they cannot be attached to anything.

**Choices:**
- Go on with everything else in the case, and wait for the referral to land → **wait_begins**
  - NOTE (shown after choosing): The rest of the plan does not wait. Only this one line does — silently, in a file you have not seen.

## [wait_begins] Week Two, Quietly
*Day 10 — Thursday, March 26, 2026 — Thursday, March 26, 2026 (dayOffset 10)*

Week two. Nia loses a tooth and gains a gap she shows everyone. Your home visits go the way they have been going: the worker looks, you talk, notes are taken in the ordinary way, on the other side of the table.

A scored assessment form is part of cases like yours — filled in from visits and notes, rating what it can see. What it can see, this month, is a mother whose ordered program has not started. Why it has not started is not a box on the form. It is a fact living in a sent folder, or in a phone call, or nowhere.

**Choices:**
- At the next visit, ask Ms. Voss again about Brightpath — and notice what is said, and what is written → **flyer_beat**
  - NOTE (shown after choosing): She says it is still in process. The note she takes does not mention Brightpath at all.

## [flyer_beat] The Flyer in the Folder
*Day 14 — Monday, March 30, 2026 — Monday, March 30, 2026 (dayOffset 14)*

In the waiting room at the agency office there is a folder of flyers for parents, and one of them — the kind of paper most people walk past — says something you read twice: a parent may request their case record, and under 55 Pa. Code § 3130.44(d) the material “shall be released upon request.”

Your record. The chronology, the notes, the service lines — the file's own version of these five weeks, which you have never seen. The flyer is not offering you a rescue. It is offering you a look.

**Choices:**
- Take the flyer home and think about what your file currently says about Brightpath → **records_fork**
  - NOTE (shown after choosing): Somewhere in that file is a service line with your name beside a program you have never attended. You would like to read it before a review does.

## [records_fork] Ask for the File, or Don’t
*Day 16 — Wednesday, April 1, 2026 — Wednesday, April 1, 2026 (dayOffset 16)*

The request is simple and it is yours to make: ask, in writing, for your case record — the service chronology and the notes about the parenting program. Under 55 Pa. Code § 3130.44(d), the record is to be released on request; the asking is a right, not a favor, and it leaves a date behind.

Or you can wait for the review and explain the five weeks there, out loud, to people reading a file you have never seen.

**Choices:**
- Put the request in writing — service chronology and program notes — and keep a copy → **file_arrives**  _(cash −3; FLAG: recordsRequested)_
  - NOTE (shown after choosing): Three dollars of copies and postage across the errand. The request is dated, copied, and kept with the plan.
- Wait for the review — you can explain it in person → **no_file**
  - NOTE (shown after choosing): In person is how you have explained everything so far. The file, meanwhile, explains you to everyone else, daily, without you.

## [file_arrives] Mother to Enroll
*Day 21 — Monday, April 6, 2026 — Monday, April 6, 2026 (dayOffset 21)*

The packet arrives, and you read the service chronology first, the way you would read weather about your own house. The Brightpath line, in full: “mother to enroll in parenting services.” No referral date. No program name beside a date. No entry recording that anyone sent anything, anywhere.

“Mother to enroll.” As if enrolling were a door standing open that you had not walked through — instead of a referral that had to be sent by someone else before you could walk through anything. The file does not accuse you. It does something quieter: it writes the gap in grammar that assigns it to the only person named in the sentence.

Now you have seen the sentence the review will read. The question is what paper will be sitting next to it.

**Choices:**
- Keep the packet with your emails — the chronology and the replies belong in the same folder → **progress_note**  _(HIDDEN + Case chronology — ‘mother to enroll in parenting services,’ with no referral date shown)_
  - NOTE (shown after choosing): Your folder and their file now disagree about the same five weeks, in writing, with dates. That disagreement is the most useful thing you own.

## [no_file] What You Cannot Quote
*Day 21 — Monday, April 6, 2026 — Monday, April 6, 2026 (dayOffset 21)*

Without the file, you cannot see the service line you are being measured against — “mother to enroll,” or however it is worded — and you cannot quote what it leaves out. You know what happened. You know it in the way that cannot be attached to a report.

Your account is true, detailed, and sincere. At the review, it will be weighed the way spoken accounts are weighed in rooms that run on attachments: personally, politely, and against a printed page that says less and therefore somehow says it louder.

**Choices:**
- Go on toward the review with your account — and keep every email you do have → **progress_note**
  - NOTE (shown after choosing): Whatever paper exists still exists. The review is weeks away, and weeks are where sentences harden.

## [progress_note] Not Yet Engaged
*Day 35 — Monday, April 20, 2026 — Monday, April 20, 2026 (dayOffset 35)*

Five weeks after the plan was signed — Monday, April 20, 2026 — the case gets its next progress note, and you hear its key phrase from Ms. Voss at a check-in, in a level voice: you are recorded as “not yet engaged in parenting services.”

Not yet engaged. You called the program the first week. You were told — by the program — that there was nothing to engage with. You check once more, and Brightpath's answer has not changed: still no referral on file.

A review is coming. Reviews read notes. The note currently says the gap is a fact about you. Whether it stays that way depends on what gets assembled before the review reads it.

**Choices:**
- Ask when the review is, and how much time is left to prepare for it → **prep**
  - NOTE (shown after choosing): Days, not weeks. Preparation, in this system, is mostly deciding what paper will be in the room.

## [prep] One Page, or a Story
*Day 38 — Thursday, April 23, 2026 — Thursday, April 23, 2026 (dayOffset 38)*

Your sent folder holds the whole five weeks, if you wrote the email: your message, the program's reply, the dates. Your packet, if you requested it, holds the chronology with its missing referral date. Assembled in order, they fit on one page: plan ordered, mother called, no referral found, gap raised in writing, program confirmed, chronology silent, note written.

Or the five weeks can stay where they have lived so far — in your head, in order, in a story you can tell well. Stories are true. Pages are portable. Reviews are rooms you speak in for minutes and files speak in forever.

**Choices:**
- Build the one-page timeline from the sent emails and the chronology, in date order → **timeline_built**  _(FLAG: gapDocumented; HIDDEN + Timeline — one-page dated timeline built from the sent emails and the chronology)_
  - NOTE (shown after choosing): One page. Every line dated. Nothing on it that the system's own paper does not support.
- Go in with the story in your head — you lived it, in order → **story_only**
  - NOTE (shown after choosing): You did, and you can tell it. The note in the file can also be told — by the file, to every reader, whether you are in the room or not.

## [timeline_built] The Timeline, Assembled
*Day 40 — Saturday, April 25, 2026 — Saturday, April 25, 2026 (dayOffset 40)*

The page reads like a timetable, because it is one. Plan ordered, Monday, March 16, 2026. You called Brightpath, Wednesday, March 18, 2026 — no referral on file. The gap raised in writing, Monday, March 23, 2026 — the program confirmed it in writing. The chronology, received Monday, April 6, 2026, shows no referral date. The progress note, Monday, April 20, 2026, calls you not yet engaged.

Five weeks, six lines, no adjectives. Your lawyer's word for a page like this is “quiet.” Quiet pages get read carefully, because there is nothing in them to argue with except their dates.

**Choices:**
- Make copies — one for the review, one for your lawyer, one for the folder → **review_eve**
  - NOTE (shown after choosing): Copies are how a page attends meetings you are not invited to. This one is about to attend the most important one.

## [story_only] Clear in Her Head
*Day 40 — Saturday, April 25, 2026 — Saturday, April 25, 2026 (dayOffset 40)*

Your account is clear, in order, and true: the call, the assurance, the weeks, the note. Sitting at the kitchen table you can tell it start to finish without a pause. It has only one flaw, and the flaw is not in the telling.

It exists in exactly one place, and that place cannot be handed to a reviewer, attached to a report, or read after you leave the room. The file's version — “not yet engaged” — exists everywhere the file goes.

**Choices:**
- Practice telling it once more, and get Nia settled for the morning → **review_eve**
  - NOTE (shown after choosing): The review will be short. Short rooms reward paper and punish nothing — they simply cannot hold what was never handed to them.

## [review_eve] The Night Before the Review
*Day 43 — Tuesday, April 28, 2026 — Tuesday, April 28, 2026 (dayOffset 43)*

The night before the review, your lawyer goes through your folder with you. You have one because the law provides for counsel in these cases, and for appointed counsel if a parent cannot afford one (42 Pa.C.S. § 6337) — she is the person whose job is to stand in the review room and make the paper speak in the right order.

“Reviews measure the plan against the record,” she says. “Tomorrow we find out which record yours is measured against — the file's one line, or the file's one line plus everything that answers it.”

Nia is asleep. The folder is by the door. The bus fare for the morning is in your coat.

**Choices:**
- Take the folder and the fare, and go to the review → **review**  _(cash −6)_
  - NOTE (shown after choosing): Six dollars of fare. The folder weighs almost nothing. Both facts are misleading about their value tomorrow.

## [review] The Review
*Day 44 — Wednesday, April 29, 2026 — Wednesday, April 29, 2026 (dayOffset 44)*

The review is orderly and brief. The plan is read line by line. On the Brightpath line, the progress note is quoted — “not yet engaged in parenting services” — and the room begins, in the ordinary way, to treat the five weeks as a fact about you.

Then your lawyer asks that the record be completed before the line is weighed. What happens next depends, with a precision this scenario has been honest about from its first page, on what your choices actually put in her hands.

**Choices:**
- Present the one-page timeline — the sent emails, the program's written reply, and the chronology attached → **end_win**  _(REQUIRES FLAG: referralChased; REQUIRES FLAG: recordsRequested; REQUIRES FLAG: gapDocumented)_
  - NOTE (shown after choosing): Six dated lines. The room does the arithmetic itself, out loud, which is where arithmetic changes a record.
- Present what paper you have — some of it, without the full set → **end_lose**
  - NOTE (shown after choosing): Part of a timeline is an argument with missing premises. The note, whole and printed, is sitting across the table.
- Tell the five weeks as a story — the call, the assurance, the waiting → **end_lose**
  - NOTE (shown after choosing): Your voice is truthful and detailed. The file's voice is one line long and has already been read.

## [end_win] Ending — Engaged, On Paper
*Day 47 — Saturday, May 2, 2026 — Saturday, May 2, 2026 (dayOffset 47)*

**Ending.**

**Debrief:**
- WHAT THE FILE HELD (the hidden record, revealed): A dated account of the gap, authored largely by the system itself: your email of Monday, March 23, 2026 raising the missing referral in writing, Brightpath's written reply confirming no referral had been received, and the agency chronology's own line — “mother to enroll in parenting services” — with no referral date beside it. At the review on Wednesday, April 29, 2026, the one-page timeline was put beside the progress note, and the room attributed the five weeks to the missing referral: the enrollment was ordered and the referral sent that day, and the record was corrected to say so. The assessment form rates what it can see; after this review, what it can see includes the reason.
- THE PROCESS UNDER THIS PATH (described, keeping to this scenario's verified law): The two instruments were the verified ones. The case record was yours on written request — it “shall be released upon request” (55 Pa. Code § 3130.44(d)) — and requesting it is what let you quote the chronology's silence instead of arguing against a summary of it. Counsel (42 Pa.C.S. § 6337) presented the timeline in the room where the plan is measured against the record. Nothing here invented a new right: the written chase created the dates, the request revealed the file, and the timeline assembled them. Reviews can only weigh paper that exists in time to be weighed.
- THE HONEST PART: Label this win honestly — it is partial. The parenting program is still ahead of you: twelve sessions, starting now, with all the ordinary difficulty of attending anything for twelve weeks. The case is still open, Nia is home as she has been throughout, and the supervision continues. A different reviewer might have noted the timeline and pressed the schedule anyway, and a worker with a lighter caseload might have caught the unsent referral in week one. Workers, reviewers, and luck all held pieces of this. Your share was narrower and durable: when the system lost five weeks, you made the system sign for them.

## [end_lose] Ending — Not Engaged, As Written
*Day 47 — Saturday, May 2, 2026 — Saturday, May 2, 2026 (dayOffset 47)*

**Ending.**

**Debrief:**
- WHAT THE FILE HELD (the hidden record, revealed): One line and one note. The plan's line — a program ordered — and the progress note's phrase — “not yet engaged in parenting services” — with nothing in the record explaining the five weeks between them: no dated email, no program reply, no chronology quoted against itself. At the review, your account was heard and, in the way of spoken accounts, believed personally and set aside professionally. The referral was finally sent after the review. The five weeks stayed in the file as yours — a period of non-engagement, available to every future reader, in a case where you had called the program in the first week.
- THE PROCESS UNDER THIS PATH (described, keeping to this scenario's verified law): The tools existed at every step and are the verified ones: chase the gap in writing, so the chase itself has a date; request the record, which “shall be released upon request” (55 Pa. Code § 3130.44(d)), so the chronology's missing referral date can be shown rather than described; and let counsel (42 Pa.C.S. § 6337) carry the assembled page into the room. None of that requires anyone to have acted in bad faith. It only requires paper — because in a review, the burden of explaining a gap quietly falls on the person the gap is written about, whether or not she caused it.
- THE HONEST PART: Let this debrief be as fair as the review was not: you did the human part of this correctly and promptly. You called the program the week the plan was signed; the referral was lost on the system's side of the desk, not yours. What was lost with it was not effort — it was evidence, and the two are different currencies in a file. A different worker might have written the capacity problem into the note herself; some do. This one did not, and outcomes here turn on workers and luck as much as on parents. The sentence in the file is not a verdict on you as a mother. It is a verdict on what was documented — and a folder started tonight, with the next email, still changes what the next review reads.
