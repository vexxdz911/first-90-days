# THE FIRST 90 DAYS — Scenario 61: “The Expired Referral”

*Human-readable script. This document and `scenario-61.json` are generated from a single source and match node-for-node: same IDs, same order, same choices, same effects.*

**The family is fictional — a composite. No real person's story appears here.**

**Content note:** This scenario depicts a parent working a sequential service plan — an evaluation that must be completed before a parenting program will enroll her — while the evaluation's referral runs toward its expiry date, told through referral copies, waitlist letters, and review reports. There is no graphic content. Players may skip any scene or use the quick exit at any time.

**How to read effects:** `cash −40` changes the player's cash. `FLAG: name` sets a flag the engine tracks. `HIDDEN + item` means the case file quietly records that item at this choice — the player does not see it when it happens. `REQUIRES FLAG: name` means the choice is only available if that flag was set earlier; `REQUIRES NO FLAG: name` means it is only available if that flag was never set. `NOTE:` is text shown to the player right after choosing.

Start date: Monday, June 15, 2026. Day offsets are days since the scenario's start date. Tier: Hard.

## [start] Two Steps, In Order
*Day 0 — Monday, June 15, 2026 — Monday, June 15, 2026 (dayOffset 0)*

You are Tanya. Your daughter Cora is three, and she has been in foster care since before this story opens — long enough that the visit room has a chair she claims as hers and a shelf of board books she has memorized in the wrong order, proudly.

Your plan has a spine, and the spine is sequential. Step A is a trauma-therapy evaluation: a specialist evaluation that must be completed first. Step B is the parenting program — and the program will not enroll you until Step A's evaluation is complete and its report is in. A before B. No exceptions, the plan says, because B is built on what A finds.

Today, Monday, June 15, 2026, your worker, Ms. Beam, tells you the referral for Step A has been sent. Sent is a good word. It is also, as this scenario will show, a word with a date attached to it — and a second date, sixty days later, that nobody in this conversation mentions.

**Choices:**
- Ask what happens next, and when → **copy_choice**
  - NOTE (shown after choosing): “They'll call you for intake,” Ms. Beam says. “There's a waitlist — about five weeks.” Five weeks, inside a sixty-day window nobody has named yet.

## [copy_choice] Sent — But On What Paper?
*Day 2 — Wednesday, June 17, 2026 — Wednesday, June 17, 2026 (dayOffset 2)*

A referral is a small machine with three moving parts: the date it was sent, the place it was sent to, and the date it stops being valid. Referrals expire — providers hold a place only so long, agencies resend only when asked — and the expiry date is the part of the machine nobody volunteers, because to everyone in the system except you, it is routine.

You can ask for the referral copy in writing: the sent date, the provider, and the validity window, printed on the agency's own letterhead. It takes a request, a few days, and a small copying cost. Or you can take today's phone call as the record of itself — Ms. Beam's summary, her assurance, her memory of having sent it.

Everything in this scenario is downstream of a choice that looks, today, like a choice about paperwork fussiness. It is actually a choice about which dates you will own in August.

**Choices:**
- Ask for the referral copy in writing — sent date and validity window included → **copy_kept**  _(cash -3; FLAG: referralDated; HIDDEN + Referral — copy in parent's hands: sent Monday, June 15, 2026, valid through Friday, August 14, 2026)_
  - NOTE (shown after choosing): Three dates on one page: sent, received, expires. The third one is the one this whole case will turn on.
- Trust the phone call — Ms. Beam sent it, and she'll be tracking it → **trust_call**
  - NOTE (shown after choosing): She sent it. That part is true, and will stay true. What a phone call cannot do is testify in August about what it said in June.

## [copy_kept] Sixty Days, In Print
*Day 4 — Friday, June 19, 2026 — Friday, June 19, 2026 (dayOffset 4)*

The copy arrives, and there it is in the provider's own print: referral sent Monday, June 15, 2026. Valid for sixty days. The window closes Friday, August 14, 2026.

You do the arithmetic the way parents in this system learn to do all arithmetic — against the waitlist. Five weeks of waiting lands in late July. The evaluation itself will be scheduled after that. The window and the wait are on a collision course so slow that nobody will call it a collision; it will be called, in a report, something else. By you.

You write the date where you will see it: Friday, August 14, 2026, in the diary you keep for visits and screens, with a line under it. A date in a diary is not yet a defense. It is the raw material defenses are made of.

**Choices:**
- Go to intake at the evaluation provider → **intake**
  - NOTE (shown after choosing): Intake is where the waitlist stops being a rumor and becomes a number with your name under it.

## [trust_call] About Two Months
*Day 4 — Friday, June 19, 2026 — Friday, June 19, 2026 (dayOffset 4)*

What you carry out of the phone call is a shape, not a date: the referral is sent, the waitlist is about five weeks, referrals are good for 'about two months,' someone will call. Every part of that is roughly accurate. Roughly accurate is a property that survives beautifully in conversation and not at all in reports.

You write 'referral — June' in your diary, because June is what you know. June is a month. The machine runs on dates, and the difference between a month and a date is the entire plot of the summer you are about to have.

**Choices:**
- Go to intake at the evaluation provider → **intake**
  - NOTE (shown after choosing): At intake, at least, there will be forms — and forms, whatever else they do, have dates on them.

## [intake] Name on the List, Date on the Wall
*Day 7 — Monday, June 22, 2026 — Monday, June 22, 2026 (dayOffset 7)*

Intake is thorough and kind: history, insurance, the court paperwork, an hour of questions about Cora and about you. You are an appropriate referral, the intake worker confirms. Your name goes on the waitlist for an evaluation slot.

Then the scheduling reality, stated conversationally, the way weather is stated: the wait to reach the top of the list is running about five weeks — and evaluations are booked in batches, with the next batch of appointments falling in the week that begins Monday, August 17, 2026.

You do the arithmetic, or you don't, depending on what paper you are holding. The batch week begins three days after Friday, August 14, 2026 — the day a sixty-day referral, sent Monday, June 15, 2026, stops being valid. The waitlist and the window are going to arrive at the same week from opposite directions, and which of them the file blames will depend on who wrote what down, starting now.

**Choices:**
- Write down the intake date, the wait, and the batch week before you leave the building → **middle_weeks**  _(HIDDEN + Intake — completed; waitlist about five weeks; evaluation batch week begins Monday, August 17, 2026)_
  - NOTE (shown after choosing): Your name, their dates, your handwriting. A small page that will be asked, later, to do a large job.

## [middle_weeks] Everything Else Runs Clean
*Day 14 — Monday, June 29, 2026 — Monday, June 29, 2026 (dayOffset 14)*

While Step A waits, the rest of your plan does not — and you run it the way you have learned to run everything in this case: visits with Cora twice a week, on time, with the installment book and the snack she negotiates for like a tiny union. Screens, random, submitted. Meetings, signed. Work shifts arranged around all of it by a manager who has quietly become one of the people who helps.

At the team meeting you do not attend, your case is summarized in the ordinary way: strong engagement across the plan — and, on the Step A line, the single word 'pending.' Pending is a neutral word in June. Left alone in a file, month after month, it ferments. By a review, 'pending' can be poured into a sentence about a parent, and the sentence will not mention waitlists, windows, or batches at all.

**Choices:**
- Keep every other line exactly this clean — and watch the Step A clock → **visit_clean**
  - NOTE (shown after choosing): The plan's other lines are yours to control. Step A's line is controlled by a calendar and a queue. The review will read them as if both were yours.

## [visit_clean] The Installment Book, Finished
*Day 21 — Monday, July 6, 2026 — Monday, July 6, 2026 (dayOffset 21)*

Cora finishes the installment book at today's visit — she has been rationing the last pages for two weeks, a three-year-old's instinct for suspense — and demands a new one be started next time, which it will be, because the machinery of your visits is the part of this case that has never once failed to run.

Your file, for anyone who reads all of it, is acquiring a shape this series keeps returning to: page after page of dated compliance, and one line standing still. Standing-still lines get explained at reviews by whoever holds the pen. There are two candidates for that authorship: the report writer, working from a chronology that will say 'A not completed,' or your paper — if you have built any, and if it arrives first.

**Choices:**
- Start the new book next visit — and read the letter that came from the provider → **provider_letter**  _(HIDDEN + Compliance during the wait — visits kept, screens submitted, meetings signed; only the waitlisted evaluation outstanding)_
  - NOTE (shown after choosing): The letter is one paragraph. It contains, between its lines, the whole rest of your summer.

## [provider_letter] A Letter With Two Dates In It
*Day 28 — Monday, July 13, 2026 — Monday, July 13, 2026 (dayOffset 28)*

The provider's letter is routine, which is what makes it dangerous: your position on the waitlist is confirmed; you are approaching the top; evaluation appointments for your group will be scheduled in the batch week beginning Monday, August 17, 2026. Thank you for your patience. No action is needed from you at this time.

No action is needed. If you are holding the referral copy, you can see the sentence the letter doesn't write: the batch week begins after Friday, August 14, 2026, when the referral that put you on this list expires. If you are not holding it, the letter reads as pure good news — you are nearly there — and the cliff edge three days past the finish line is invisible.

No action is needed from you at this time. It is the most expensive sentence in this scenario, and the provider does not even know it wrote it.

**Choices:**
- Take the letter to your lawyer and ask what an expiring referral does to a sequential plan → **lawyer_check**
  - NOTE (shown after choosing): Because Step B will not enroll you without A — and A is about to need a referral that is about to stop existing.

## [lawyer_check] Your Lawyer Reads the Window
*Day 35 — Monday, July 20, 2026 — Monday, July 20, 2026 (dayOffset 35)*

You have had a lawyer since the start of this case, as the law provides (42 Pa.C.S. § 6337). She reads the provider's letter twice, asks the question the letter was hoping nobody would ask — 'When does the referral itself expire?' — and then either turns to your copy, with its printed window, or to your diary, with its month.

“Understand the machine,” she says. “When a referral lapses, the provider doesn't keep your place out of kindness or lose it out of spite. The place belongs to the referral. A re-referral is a new machine part: unless the lapse is documented as the sender's timing — the waitlist outrunning a window the agency chose — the queue treats a re-referral as a new arrival. The difference between those two sentences is entirely paper: the dated referral, and a nudge in writing before the window closes, asking the agency to re-send in time.”

She is clear that none of this is a promise about any court or clock beyond this plan: it is a point about whose delay the file will describe, and files describe what their paper lets them describe.

**Choices:**
- Check the waitlist again this week — in writing, the way dates are made → **queue_check**
  - NOTE (shown after choosing): The window closes in twenty-five days. The queue is three names from your name. Both facts need witnesses.

## [queue_check] Three Names Ahead
*Day 38 — Thursday, July 23, 2026 — Thursday, July 23, 2026 (dayOffset 38)*

The provider answers questions about the waitlist two ways, and the two ways produce two different cases. By email, a reply has a date, a position, and a sentence you can keep: 'You are third on the list; your group is scheduled in the batch week.' By phone, the same facts arrive warmly, personally, and evanescently, in a voice that will remember being helpful and will not remember the number.

Third on the list. The batch week is fixed. The window is fixed. The only variable left in the whole machine is whether anyone with the power to re-send the referral is asked, in writing, before it lapses — and 'asked in writing' is a thing that either exists as paper or does not exist at all.

**Choices:**
- Write the check-in — position, batch week, and your name, in an email you keep → **waiting_weeks**  _(HIDDEN + Waitlist check-ins — written; provider replies saved, position and batch week confirmed)_
  - NOTE (shown after choosing): Third, confirmed, dated. The queue now has a witness besides you.
- Call instead — a voice is harder to put on hold → **waiting_weeks**
  - NOTE (shown after choosing): She is kind, she confirms third, and she keeps no record of having said so. Kindness is not a filing system.

## [waiting_weeks] The Quiet Weeks
*Day 44 — Wednesday, July 29, 2026 — Wednesday, July 29, 2026 (dayOffset 44)*

Late July is the plan's long corridor: visits kept, screens clean, work held together, and over it all the ticking nobody hears but you — a referral aging toward a date, a queue inching toward a batch week, a three-year-old finishing one board book and starting another in a visit room.

Ms. Beam's check-in is brief and untroubled. Step A is 'in process,' she says. Step B is 'next.' If you ask about the referral's window, she will reassure you; if you do not, she will not raise it, because in her file the referral is filed under 'sent,' and 'sent' is a completed act in every system except the one that expires.

The diary page is coming: day fifty, Tuesday, August 4, 2026. Ten days after it, the window closes. What a parent does in those ten days, in writing or in trust, is the last decision this machine leaves to anyone.

**Choices:**
- Open the diary to day fifty → **nudge_choice**
  - NOTE (shown after choosing): Ten days of margin. In this system, ten days of margin, used in writing, is an fortune. Unused, it is a date that passes.

## [nudge_choice] Day Fifty: The Nudge
*Day 50 — Tuesday, August 4, 2026 — Tuesday, August 4, 2026 (dayOffset 50)*

Today is Tuesday, August 4, 2026. The referral you may or may not be holding expires Friday, August 14, 2026 — ten days from now. You are at or near the top of the waitlist. The batch week begins Monday, August 17, 2026. The collision is no longer theoretical; it has dates, and the dates are inside one diary page of each other.

A written nudge is a small, unglamorous machine: a short letter or email to Ms. Beam, copied to the provider, stating the referral's sent date and expiry, the waitlist position, and the batch week — and asking, plainly, that the referral be re-sent before it lapses so your queue position is preserved as a continuation. It creates the one document the whole summer has been missing: proof that the lapse, if it comes, was seen coming, by name, by the person it would be blamed on — and reported, in time, to the people whose job the re-send was.

The alternative is trust: the system sent the referral, the system knows its own windows, the system will surely handle its own machine.

**Choices:**
- Send the written nudge today — agency and provider, dates stated, copies kept → **nudge_sent**  _(cash -3; FLAG: diaryNudge; HIDDEN + Written nudge — sent Tuesday, August 4, 2026, before expiry; re-send requested as a continuation, copies kept)_
  - NOTE (shown after choosing): Ten days early, in writing, with the dates spelled out. Whatever happens next now has to happen against this page.
- Assume it is handled — the agency sent it, and agencies track their own referrals → **assume_handled**
  - NOTE (shown after choosing): A belief held by reasonable people in every waiting room in this system. The machine is about to grade it.

## [nudge_sent] A Letter Doing Its Quiet Work
*Day 52 — Thursday, August 6, 2026 — Thursday, August 6, 2026 (dayOffset 52)*

The nudge does not produce drama. It produces a reply: Ms. Beam's office acknowledges the dates — a sentence you keep — and the provider's intake office notes your file. Somewhere in the machinery, a referral that was going to expire unattended is now expiring attended, which turns out to be a completely different event wearing the same date.

You go back to the plan's ordinary weeks: visits, screens, the new board book's early chapters. The window is still closing. The difference is that its closing is now an item on other people's desks, in writing, with your letter underneath it — and systems, whatever their faults, route items that are on desks.

**Choices:**
- Wait for the window to close — and watch what the machine does with a documented referral → **expiry_kept**
  - NOTE (shown after choosing): Eight days. Your letter is older than the lapse will be. Sequence is about to become evidence.

## [assume_handled] Handled, Presumably
*Day 52 — Thursday, August 6, 2026 — Thursday, August 6, 2026 (dayOffset 52)*

Nothing happens, which feels like confirmation. No call comes; no letter arrives; Step A remains 'in process' at every check-in, because in process is where a referral lives in the file right up until the morning it doesn't. You keep the rest of the plan perfectly — visits, screens, meetings — and the perfection is real, and it is all happening on lines of the plan that were never in danger.

The danger is on the one line you cannot touch: a date, printed on a document you never asked for, approaching at the speed of calendars. Eight days from now, the machine will make its decision about your queue position, in a room you are not in, based on paper you did not write.

**Choices:**
- Wait for the window to close → **expiry_restart**
  - NOTE (shown after choosing): It closes quietly, the way administrative dates do. The consequences arrive later, wearing other dates.

## [expiry_kept] The Window Closes — On Paper
*Day 60 — Friday, August 14, 2026 — Friday, August 14, 2026 (dayOffset 60)*

On Friday, August 14, 2026, the original referral reaches the end of its sixty days — and because the re-send was requested in writing, ten days early, with the waitlist position and batch week stated, the agency re-sends it as a continuation and the provider honors the original queue position. The lapse is documented, in the provider's own note, as the sender's timing: a five-week waitlist outrunning a sixty-day window was never a delay the parent could have prevented, and now the file says so in someone else's handwriting.

Your place is not a favor. It is a record: referral, waitlist letter, nudge, re-send, continuation note — a chain with no missing links, each link dated by the person who forged it. Chains like that are what reviews cannot argue with. They can only read them.

**Choices:**
- Go to the evaluation — in the batch week, at the top of the list, as scheduled → **evaluation_done**
  - NOTE (shown after choosing): The appointment letter names the original referral and its continuation on the same line. Keep it. Keep everything.

## [expiry_restart] The Window Closes — Silently
*Day 60 — Friday, August 14, 2026 — Friday, August 14, 2026 (dayOffset 60)*

On Friday, August 14, 2026, the referral expires. No alarm sounds; expiry is not an event, it is an absence that a computer notices on a schedule. The provider's list, which is a list of live referrals, quietly stops containing your name at the position you had waited five weeks to reach.

The re-referral is sent days later, when the lapse surfaces — promptly, by the standards of an office that did not know it had a deadline. It is a new referral. The queue, which is a machine for ordering new referrals, places it where new referrals go: at the back. Five weeks of waiting are not stolen by anyone. They are simply not recorded anywhere the queue can read, because the paper that would have preserved them was never created.

Your new position comes with a new projected batch week, in the following month. Step B's door, which opens only on Step A's completion, stays shut — and the chronology line being drafted for the review requires only four words to describe all of it: 'A not completed.'

**Choices:**
- Ask what your place is now, and when the evaluation can happen → **evaluation_waiting**
  - NOTE (shown after choosing): The answer is kind, apologetic, and five weeks long. Kindness does not shorten queues. Paper would have.

## [evaluation_done] The Evaluation, Completed
*Day 66 — Thursday, August 20, 2026 — Thursday, August 20, 2026 (dayOffset 66)*

On Thursday, August 20, 2026, in the batch week as scheduled, you sit for the Step A evaluation: the history taken again, the questions answered, Cora's needs and your plan discussed in the specialist's unhurried hour. It is, in the lived sense, the thing itself — the step the plan ordered, completed.

The paper around it matters almost as much: the appointment record names the original referral and its continuation; the provider's report will follow in days. There is one more document to secure, and it is the one the review will ask about first: the re-referral confirmation itself — the page that shows the chain, original date to re-send to honored position, without a gap for a report writer to fill with your name.

**Choices:**
- File the re-referral confirmation with the original referral copy, in date order → **records_beat**  _(cash -4; FLAG: rereferralProof; HIDDEN + Re-referral proof — continuation confirmation kept, showing the original date and the honored queue position)_
  - NOTE (shown after choosing): Chain, complete: sent, waited, nudged, re-sent, honored, completed. Every link dated. Every link kept.
- Leave the confirmation in the provider's portal — the evaluation is done, and done is what counts → **records_beat**
  - NOTE (shown after choosing): Done is what counts in the room where it happened. In the review room, what counts is what can be shown — and portals are not packets.

## [evaluation_waiting] Still Waiting, From the Back
*Day 66 — Thursday, August 20, 2026 — Thursday, August 20, 2026 (dayOffset 66)*

The new queue moves at the old queue's pace: about five weeks, the provider says, to a batch week in the following month. You attend everything else. You keep the visits, the screens, the meetings — a plan running at full speed around one line that a calendar reset while nobody was watching it.

There is one piece of paper in this branch worth keeping, and you may or may not think to keep it: the re-referral letter itself, with its new date. It cannot restore your position. What it can do — in a review, in a lawyer's hands — is prove when the clock restarted, which is the difference between a gap with an explanation attached and a gap with your name in it.

**Choices:**
- Keep the re-referral letter and its date, whatever else happens → **records_beat**  _(HIDDEN + Re-referral letter — kept, showing the restart date after the silent expiry)_
  - NOTE (shown after choosing): A lesser document than the chain would have been. It is not nothing. In this system, dated paper is never nothing.
- Let the provider's office keep its own letters — they'll have them if anyone asks → **records_beat**
  - NOTE (shown after choosing): They will have them, filed under a referral number you don't know, in a system your lawyer cannot attach to a report.

## [records_beat] Ask for the File Itself
*Day 71 — Tuesday, August 25, 2026 — Tuesday, August 25, 2026 (dayOffset 71)*

Your lawyer raises the other instrument, the one that answers the review before it convenes: the agency's draft chronology already contains the line 'A not completed,' and lines like that are met with attachments or they are met with nothing. A party may request the case record, and the material in it 'shall be released upon request' (55 Pa. Code § 3130.44(d)).

The request is one page, in writing: the referral record, the re-referral record, the chronology, the draft report. What it would show you is the file's own account of the summer — the sent date the agency itself recorded, the absence of any expiry note, and the exact wording your packet has to answer. What it cannot show you is anything you never made: requests reveal files; they do not retroactively create the paper inside them.

**Choices:**
- Sign the written request for the record — referral chain, chronology, draft report → **record_arrives**  _(FLAG: recordsRequested; HIDDEN + Case record — requested in writing, including the referral chain and the draft review report)_
  - NOTE (shown after choosing): Signed, dated, copied. The file's version of the summer is about to be quotable — by you, for once, instead of only about you.
- Rely on the provider's letters — the agency's file is its own business → **no_record**
  - NOTE (shown after choosing): The agency's file is also the review's script. Declining to read the script does not cancel the performance.

## [record_arrives] The File's Version of the Summer
*Day 77 — Monday, August 31, 2026 — Monday, August 31, 2026 (dayOffset 77)*

The record, when it comes, is illuminating in the specific way of unguarded documents. The agency's referral is there, dated Monday, June 15, 2026 — prompt, proper, on the record. The re-referral is there too, with its date. Between them: nothing. No expiry date noted. No waitlist note. No record that the window and the queue were ever compared by anyone.

And in the draft chronology, the summer's epitaph, already typed: 'A not completed.' Four words that are, depending on the chain you built, either about to be answered by their own file — the referral, the waitlist letter, the nudge, the continuation, the completion — or about to stand as the whole account, because a chronology does not know what it does not contain.

Your lawyer spreads the packet beside the draft. 'We don't argue with four words,' she says. 'We outnumber them.'

**Choices:**
- Read what Step B does next — the enrollment letter → **enroll_letter**
  - NOTE (shown after choosing): Step B enrolls on paper too. Its letter is the last piece of the chain, or the last proof of the gap.

## [no_record] The Script, Unread
*Day 77 — Monday, August 31, 2026 — Monday, August 31, 2026 (dayOffset 77)*

Without the file, you and your lawyer prepare from your side of the paper: the provider's letters you kept, the diary, the evaluation's own documents or the re-referral's. Your account of the summer is accurate. What you cannot do is quote the other side's — and the review will be conducted from the other side's, in a chronology whose four-word line you have not seen and therefore cannot answer word for word.

“We present what we have,” your lawyer says, “and we will be answering a sentence we haven't read, in a room that has.” She says it without drama. Sequence, in this system, is not a detail. It is most of the game.

**Choices:**
- Read what Step B does next — the enrollment letter → **enroll_letter**
  - NOTE (shown after choosing): Step B's letter does not know about chronologies. It knows one thing: whether Step A is complete.

## [enroll_letter] Step B Answers
*Day 83 — Sunday, September 6, 2026 — Sunday, September 6, 2026 (dayOffset 83)*

Step B's letter arrives the way every decisive thing in this case has arrived: routinely, on letterhead, with a date. Its content is a pure function of the chain. Where the evaluation is complete and its report has landed, the letter enrolls you: a start date, a schedule, the plan's spine restored to the order it was written in — A, then B, as designed. Where the evaluation is still waiting out a restarted queue, the letter says the other thing, in the same courteous type: enrollment cannot proceed until Step A is completed.

Hold the two versions side by side and the scenario's whole mechanism is visible without a single villain in it: the same mother, the same effort, the same plan — separated by whether a referral's second date was ever written down by the person it could hurt.

**Choices:**
- Prepare for the review with your lawyer → **review_prep**
  - NOTE (shown after choosing): The review will read the chronology and the packet. Only one of them is still yours to assemble.

## [review_prep] The Packet, In Date Order
*Day 87 — Thursday, September 10, 2026 — Thursday, September 10, 2026 (dayOffset 87)*

Your lawyer builds the review packet the way this scenario has built everything: in date order, so the chain tells itself. The referral copy with its window, or its absence. The intake page. The waitlist letters. The nudge, or the silence where it would be. The re-referral — as continuation or as restart. The evaluation report, or the new queue letter. Step B's answer.

“Reviews believe sequences,” she says. “A sequence with a missing link gets narrated by whoever dislikes the gap least — and it is never narrated as a machine's gap. Machines don't get blamed in reports. People with names in the chronology do. Our whole job is to make the machine's part of this sequence as documented as yours.”

She copies the packet for the court. What it proves, and what it cannot, will be decided by which links your summer actually forged.

**Choices:**
- Make the court copies and go to the review → **review**  _(cash -6; HIDDEN + Review packet — referral chain assembled in date order, from referral copy to Step B's letter)_
  - NOTE (shown after choosing): Date order. The summer, testified to by its own paperwork, in the order the paperwork happened.

## [review] The Review
*Day 91 — Monday, September 14, 2026 — Monday, September 14, 2026 (dayOffset 91)*

The review convenes on Monday, September 14, 2026. The agency presents its chronology, and the Step A line gets its four words: 'A not completed' — or, where the evaluation landed, 'A completed late,' with the lateness offered without an owner. Reports are read against packets now, and the packet is in the room.

What happens next depends, with a precision this scenario has been honest about since its first phone call, on the chain itself: whether the referral was dated in your hands in June, whether the nudge went out in writing before the window closed, whether the continuation was kept, and whether the file was ever requested and quoted back to its authors.

Your lawyer rises. Choose the presentation the chain you actually built can carry.

**Choices:**
- Present the whole chain — dated referral, written nudge, continuation proof, and the agency's own record → **end_win**  _(REQUIRES FLAG: referralDated; REQUIRES FLAG: diaryNudge; REQUIRES FLAG: rereferralProof; REQUIRES FLAG: recordsRequested)_
  - NOTE (shown after choosing): This presentation exists because four pieces of paper exist, dated, in order, from June to September.
- Present the agency's own record — the referral and re-referral dates it recorded itself → **end_partial**  _(REQUIRES FLAG: recordsRequested)_
  - NOTE (shown after choosing): The file answers part of the charge against itself. The rest of the chain is thinner — and the room can feel where.
- Present what paper you have — provider letters and the diary, assembled as a sequence → **end_partial**
  - NOTE (shown after choosing): Half a chain is an argument with missing links. It still changes the room — just less, and later.
- Explain the summer yourself — the waitlist, the window, the queue, as you lived them → **end_worst**
  - NOTE (shown after choosing): Your account is accurate in every particular. Accuracy, unattached, is the currency this room accepts least.

## [end_win] Ending — Referred, Continuously
*Day 98 — Monday, September 21, 2026 — Monday, September 21, 2026 (dayOffset 98)*

**Ending.**

**Debrief:**
- WHAT THE FILE HELD (the chain, revealed): At the review on Monday, September 14, 2026, the chronology's line did not survive its own attachments. The chain was complete and dated at every link: the referral copy showing it sent Monday, June 15, 2026 and valid through Friday, August 14, 2026; the intake and waitlist letters; the written nudge sent ten days before the window closed; the provider's continuation note honoring the original queue position because the lapse was documented as the sender's timing; the evaluation completed Thursday, August 20, 2026; and Step B's enrollment letter, issued on the completed evaluation. The delay was attributed, on the record, to the referral mechanics — a five-week queue outrunning a sixty-day window — and not to you. Cora remains in foster care and Step B has weeks to run; no honest debrief will call this case won. What is won is the attribution, permanently, for every future reader of this file.
- THE PROCESS UNDER THIS PATH (described, keeping to this scenario's verified law): No new right was invented here. The case record was available on written request — it 'shall be released upon request' (55 Pa. Code § 3130.44(d)) — and requesting it is what let your lawyer quote the agency's own referral dates back to the chronology that omitted them. Counsel's role was the one the law assigns from the start (42 Pa.C.S. § 6337): assembling dated paper into a sequence a review cannot narrate around. The referral window itself is not a statute in this scenario; it is a piece of administrative machinery — a provider's validity period — and the scenario's claim is only the modest one the paper supports: machinery like that decides cases unless somebody documents it, and documenting it is a skill, not a virtue.
- THE HONEST PART: A different provider might never have honored a continuation, nudge or no nudge; a different report writer might have contested the chain link by link; Ms. Beam's office might have missed the re-send even with your letter on the desk, and no nudge compels an office to be prompt. Workers, providers, judges, and the plain luck of a batch week's timing all held pieces of this outcome. And the deepest honesty is the same as in every scenario in this series: Cora spent this summer three years old, in someone else's house, whatever the paperwork says about whose delay it was. What your choices changed was narrower and load-bearing — whether the file tells the truth about a machine's failure, or tells it as yours. Outcomes here are not verdicts on a parent. This one is a verdict on a chain of paper, and for once the chain held.

## [end_partial] Ending — A Gap, Half-Explained
*Day 98 — Monday, September 21, 2026 — Monday, September 21, 2026 (dayOffset 98)*

**Ending.**

**Debrief:**
- WHAT THE FILE HELD (the chain, revealed): A partial chain: some links dated and kept — a provider letter here, a re-referral date there, perhaps the agency's own record quoted back to it — and gaps where the dated referral copy, the written nudge, or the continuation confirmation would have been. At the review on Monday, September 14, 2026, partial paper did partial work. The review declined to adopt 'A not completed' as a statement about you in full; the agency conceded, in general terms, that 'referral processing' had contributed to the timeline; and the gap was entered as contested rather than attributed — shared, vaguely, between a mother and a machine, in proportions nobody was required to specify. Step B's position improved or waits, depending on the chain; the plan continues; and the file's account of the summer is a draw, which against a chronology that began as four flat words is movement — and against what the whole chain would have done, is a lesson with a price.
- THE PROCESS UNDER THIS PATH (described, keeping to this scenario's verified law): The tools were the verified ones, used partly. The case record, on written request (55 Pa. Code § 3130.44(d)), could show the referral and re-referral dates the agency itself recorded — the strongest single answer to its own chronology — and counsel (42 Pa.C.S. § 6337) could build only from the links that existed. Nothing in this ending says you failed the summer: you waited the wait, kept every other line, and may have managed the referral diligently by phone and trust. It says the review priced your proof, not your diligence, because reviews can only price what is in front of them — and a chain, unlike an effort, cannot be half-forged in the room and expected to hold weight.
- THE HONEST PART: A contested gap may matter less by the next review than it does today: Step B will be running or the evaluation long completed, and nine weeks of new compliance will outweigh an argument about a summer referral. Judges differ in how much ambiguity they hold against the party who didn't create it, and this one split the difference, as many do. What remains true is the mechanism, and it is portable to every referral, waitlist, and sequential step still ahead of you in this case: the side that documents the machine's dates owns the machine's delays, and the side that merely survives them rents the explanation, review by review. Your packet, from here, is a habit looking for its next referral. It will find one.

## [end_worst] Ending — Expired, As Written
*Day 98 — Monday, September 21, 2026 — Monday, September 21, 2026 (dayOffset 98)*

**Ending.**

**Debrief:**
- WHAT THE FILE HELD (the chain, revealed): At the review on Monday, September 14, 2026, the chronology stood as written, because it was the only written thing in the room that described the whole summer: referred, waited, 'A not completed.' The referral's expiry was never mentioned as a fact about a machine; the restarted queue was never mentioned at all; the five weeks you spent at the top of a list exist nowhere the review could read them. Your account — accurate in every detail — was received the way unattached accounts are received in rooms that run on attachments: personally, and without effect. The plan's spine stays broken at the same joint: Step B cannot enroll you, the evaluation waits out its second queue, and the next report is already drafting itself from this one's four words.
- THE PROCESS UNDER THIS PATH (described, keeping to this scenario's verified law): No rule says an expired referral is a parent's failure. What produced this ending was an absence of paper at the three moments paper was available: the referral copy, requestable in June with its window in print; the written nudge, sendable ten days before the window closed, which would have made the re-send a documented duty instead of a discovered lapse; and the case record itself, available on written request (55 Pa. Code § 3130.44(d)), whose own dates answer its own chronology. Counsel was there throughout (42 Pa.C.S. § 6337) to assemble any of it. The system did not defeat a strategy here. It simply ran, unattended, on its default settings — and its default setting is that an undated delay belongs to the only named person in the sentence.
- THE HONEST PART: Let this debrief be as fair as the review was not: the delay was never yours. You presented for intake, you waited the wait in good faith, you kept every line of the plan that a parent can touch, and the referral expired in a computer, on a date nobody told you, while a provider's letter was assuring you no action was needed. The injustice of this ending is not that the system doubted your effort; it is that effort was the wrong currency, and the exchange rate — dated referrals, written nudges, kept confirmations — was never posted in the waiting room. Workers with lighter caseloads sometimes catch an expiring referral themselves; some parents are rescued by exactly that luck. Yours was not, and luck is not a system. The chain can still be started — at the next referral, in writing, on day one — and it will matter at the next review. It simply cannot retroactively date the summer that just passed undated.
