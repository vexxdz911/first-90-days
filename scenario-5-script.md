# THE FIRST 90 DAYS — Scenario 5: “The Missed Appointment” (Foundation tier)

*Human-readable script. This document and `scenario-5.json` are generated from a single source and match node-for-node: same IDs, same order, same choices, same effects.*

**The family is fictional — a composite. No real person's story appears here.**

**Content note:** This scenario depicts a first service plan, a drug-screen appointment, a bus that does not come, and how a missed appointment gets written down. There is no graphic content. Players may skip any scene or use the quick exit at any time.

**How to read effects:** `cash −4` changes the player's cash. `FLAG: name` sets a flag the engine tracks. `HIDDEN + item` means the case file quietly records that item at this choice — the player does not see it when it happens. `NOTE:` is text shown to the player right after choosing.

Start date: Monday, January 5, 2026. Day offsets are days since the scenario's start date. Starting cash: $140.

## [start] The Plan, Signed
*Day 0 — Monday, January 5, 2026 (dayOffset 0)*

Your son Noah is eight, home with you, and likely to stay that way — nobody is talking about removal. What you have instead is a family service plan, signed last week after the school called the agency about the mornings Noah arrived hungry and half asleep.

The plan is mostly things you agreed with: a steadier bedtime, breakfast before the bus, a parenting class on Saturdays. One line is not about Noah at all. It is about you, and an old part of your life you have been working to leave behind: a drug screen, at a testing office across town, on Friday, January 9, 2026, at 9:00 in the morning.

**Choices:**
- Read the plan again tonight, all the way through → **n2**
  - NOTE (shown after choosing): The appointment line is on page two. Page two is where plans keep their teeth.
- Sign it and put it on the refrigerator → **n2**
  - NOTE (shown after choosing): It is on the refrigerator either way. The question is whether you have read what is on it.

## [n2] Two Buses
*Day 1 — Tuesday, January 6, 2026 (dayOffset 1)*

The testing office is not far on a map. By bus it is two buses: the 14 to the transit center, then the 6, with a twelve-minute connection if the first bus is on time and a forty-minute wait if it is not.

Your caseworker, Ms. Hart, mentioned none of this. On paper, the appointment is a line. In your life, it is a morning arranged like dominoes.

**Choices:**
- Map the route tonight — both buses, the transfer, the walk → **records**
  - NOTE (shown after choosing): Twelve minutes of connection, if everything behaves. You write the times on the back of the appointment slip.
- Trust that it will work out on the day → **records**
  - NOTE (shown after choosing): It might. Hope is not a schedule, but it is what most mornings run on.

## [records] Your Copy, Your Proof
*Day 1 — Tuesday, January 6, 2026 (dayOffset 1)*

At the agency office to drop off a form, you stop at the desk. Ms. Hart has told you the plan is 'in the system.' Systems have lost things before. You would like the paper itself.

You ask — out loud, and then, because the desk clerk suggests it, in a short written note — for a copy of your service plan and the appointment slip for your own records.

**Choices:**
- Ask for the copies in writing, and wait while they are made → **prep**  _(FLAG: recordsRequested; HIDDEN + Records — parent requested and received copies of the plan and appointment slip)_
  - NOTE (shown after choosing): The clerk stamps your request and hands you the copies. Under 55 Pa. Code § 3130.44(d), agency records about your family are released on request — the asking is a right, not a favor.
- Take Ms. Hart’s word that it is all in the system → **prep**
  - NOTE (shown after choosing): Her word may be good. It is still not something you can hold up at a testing-office desk.

## [prep] The Night Before, Ready
*Day 2 — Wednesday, January 7, 2026 (dayOffset 2)*

Wednesday night you lay it out like a work uniform: the appointment slip, your ID, bus fare in the envelope from the kitchen drawer, phone charging where you will see it.

Noah's breakfast things are on the counter. His grandmother will walk him to his bus at 7:40. Your bus leaves at 7:15. The morning has no slack in it at all, and now at least you can see all of it.

**Choices:**
- Set two alarms and put the fare envelope in your coat → **eve**  _(cash −4)_
  - NOTE (shown after choosing): Four dollars of bus fare, moved from the drawer to the coat. Small money, spent the night before, is what slack looks like.
- Decide you will remember everything in the morning → **eve**
  - NOTE (shown after choosing): You might. Memory is the first thing a bad morning takes.

## [eve] A Quiet Evening
*Day 3 — Thursday, January 8, 2026 (dayOffset 3)*

Thursday evening. Noah does his reading at the table while you check the plan copy one more time: testing office, Friday, January 9, 2026, 9:00. Check-in closes fifteen minutes early, the slip says, in smaller print.

You are asleep by ten. Whatever tomorrow is, you have done the parts of it that could be done tonight.

**Choices:**
- Sleep. The morning is planned as far as planning reaches → **split**
  - NOTE (shown after choosing): Planning reaches to the curb of the bus stop. After that, the city drives.

## [split] The Bus That Doesn’t Come
*Day 4 — Friday, January 9, 2026 (dayOffset 4)*

Friday, 7:15. The 14 does not come. At 7:25 the transit app changes its mind twice. At 7:31 a bus finally sighs to the curb — twenty minutes of your twelve-minute connection, gone.

You do the arithmetic standing in the cold. You will reach the transit center after the 6 has left. The next 6 gets you to the testing office at about 9:20 — twenty minutes after your appointment, five past the late window. Your phone is in your hand. The testing office opens at 8:00. It is 7:31.

**Choices:**
- Call the testing office and Ms. Hart now, before 9:00, and say exactly what happened → **p1**  _(FLAG: calledAhead; HIDDEN + Missed screen — parent called ahead, before the appointment time)_
  - NOTE (shown after choosing): The office logs the call at 7:34. Ms. Hart’s voicemail gets the same message. The miss now has a timestamp on your side of it.
- Ride it out and explain everything at the desk when you get there → **u1**  _(HIDDEN + Missed screen — no call received before the appointment time)_
  - NOTE (shown after choosing): Explanations at a desk are worth something. They are worth less at 9:20 than at 7:34.

## [p1] Logged at 7:34
*Day 4 — Friday, January 9, 2026 (dayOffset 4)*

The woman at the testing office is brisk and not unkind. 'You’re the 7:34 call,' she says. 'We can hold a late slot at 10:30 if you can get here. After that it’s Monday.'

Ms. Hart calls back at 8:05 — she has the voicemail, and the office has confirmed the call time. 'Get the 10:30,' she says. 'And keep whatever the bus gave you.'

**Choices:**
- Take the 10:30 slot and stay downtown → **p2**  _(cash −6)_
  - NOTE (shown after choosing): Six more dollars — coffee you nurse for two hours and a second fare. The slot is worth more than the money, and it still stings.
- Ask whether there is a second late slot, in case the bus strands you again → **p2**
  - NOTE (shown after choosing): There isn’t — 10:30 is the day’s last mercy. The call is what bought you a choice at all.

## [p2] Paper at the Desk
*Day 4 — Friday, January 9, 2026 (dayOffset 4)*

At the testing office, the receptionist starts a form. 'Reason for the late arrival?' she asks, pen ready. This is the moment the morning turns into a sentence in a file — the only question is which sentence.

In your coat pocket: the transfer stub from the second bus, and your phone, with the call log open at 7:34.

**Choices:**
- Show her the transfer stub and the 7:34 call log, and ask her to note both → **p3**  _(FLAG: proofShown; HIDDEN + Documentation — transfer stub and call log provided and noted)_
  - NOTE (shown after choosing): She writes: "Transportation failure — parent called ahead 7:34, transfer stub shown." One sentence. It will be read by everyone who reads this file after her.
- Tell the story again, and ask her to just put down that the bus was late → **u3**  _(HIDDEN + Documentation — none provided; explanation given verbally at desk)_
  - NOTE (shown after choosing): She writes: "Parent states bus late." Four words, and no way for anyone after her to check them.

## [p3] The Screen, Done
*Day 7 — Monday, January 12, 2026 (dayOffset 7)*

The screen itself takes ten minutes and no drama at all. The result goes where results go. What stays with you is the paperwork about the morning, which will outlive the result by years.

Ms. Hart updates the plan note that afternoon. You will not see her screen — but you can ask for the updated copy, the same way you asked for the first one.

**Choices:**
- Ask for the updated plan copy for your folder → **p4**  _(FLAG: copyFiled)_
  - NOTE (shown after choosing): Two days later it is in your mailbox, with the 7:34 sentence inside it. Your folder and her file now say the same thing.
- Head home — the screen is done, and that’s the point → **p4**
  - NOTE (shown after choosing): The screen was the requirement. The paper about the screen is the protection. They are not the same errand.

## [p4] Read Back to You
*Day 9 — Wednesday, January 14, 2026 (dayOffset 9)*

At the next plan meeting, Ms. Hart reads the month aloud, the way workers do: services attended, screen completed, one transportation issue — noted as resolved, called ahead, documented.

There is a pause where a worse sentence could have been. She moves on to Noah's bedtime routine, which is going well, and his breakfast, which is going better.

**Choices:**
- Ask her to keep the note exactly as written — "called ahead, documented" — in the plan summary → **p5**  _(FLAG: wordingKept)_
  - NOTE (shown after choosing): She shrugs and types it. Exact words, asked for politely, have a way of surviving.
- Let the summary take care of itself → **p5**
  - NOTE (shown after choosing): Summaries are written by whoever writes them. Today that was almost you.

## [p5] Sign Here
*Day 11 — Friday, January 16, 2026 (dayOffset 11)*

The plan summary lands in your mailbox: two pages, this month compressed. Screen: completed. Attendance: good. And one line about the missed morning, carried forward into the summary that future readers will actually read.

There is a signature line for you at the bottom, and a pen already in your hand.

**Choices:**
- Read both pages before you sign — and keep your copy → **end_good**  _(FLAG: readBeforeSigning)_
  - NOTE (shown after choosing): The line reads: "Transportation failure — parent called ahead, documented." It is the truest sentence in the file, and now it is in the summary too.
- Sign quickly — it’s only a summary → **end_partial**
  - NOTE (shown after choosing): You do not see that the summary writer shortened the line to "screen rescheduled after no-show." Summaries are where careful sentences go to be simplified.

## [end_good] Recorded as What It Was
*Day 13 — Sunday, January 18, 2026 (dayOffset 13)*

**ENDING.** Debrief:

- The miss is in the file as what it was: a bus that did not come, a parent who called at 7:34, a screen completed. The plan continues unchanged — no extra check-ins, no tightened terms.
- The law inside this story: under 55 Pa. Code § 3130.44(d), the copies you asked for at the desk are released on request. They were not a courtesy. Holding your own copy is what let you check the record against the morning you actually lived.
- Notice what the winning moves were made of: a phone call placed before the appointment time, a transfer stub kept in a pocket, exact words asked for at a desk. None of it cost more than six dollars and some nerve.
- Honesty requires this: a stricter office might have closed the late window anyway, and a different worker might have written the morning colder. Part of every outcome in this system is the person across the desk, and part is luck. What the record gave you was a fair chance with all of them.

## [u1] 9:20
*Day 4 — Friday, January 9, 2026 (dayOffset 4)*

You arrive at 9:20 to a locked check-in screen and a receptionist who is sorry in the way people are sorry about weather. The late window closed at 9:15. The form she completes has a box for this, and the box is small: NO-SHOW.

She is not cruel and she does not make the rules. But the box is now the morning, as far as the file is concerned.

**Choices:**
- Ask what can still be done — today, this week, in writing → **u2**
  - NOTE (shown after choosing): Asking is still possible. It is just happening after the box instead of before it.
- Go home. You’ll explain it all to Ms. Hart when she calls → **u2**
  - NOTE (shown after choosing): She will call. Explaining second is a weaker position than explaining first, and both of you will know it.

## [u2] The Call, a Day Late
*Day 5 — Saturday, January 10, 2026 (dayOffset 5)*

Ms. Hart calls the next afternoon. Her voice is not angry. It is worse than angry: it is updating. 'The office has it as a no-show,' she says. 'Was there a problem?'

There was. There still is, as a story. What there is not, yet, is anything on paper that happened before 9:00 on Friday.

**Choices:**
- Ask to fix it properly: a make-up screen this week, and a written statement from you for the file → **p3**  _(FLAG: repairAsked; HIDDEN + Repair — parent requested make-up screen and filed a written statement)_
  - NOTE (shown after choosing): She agrees to both. A written statement, late, is not as strong as a 7:34 phone call — but it is far stronger than a story told on the phone.
- Explain that the bus company is the one she should be asking → **u3**  _(HIDDEN + Missed screen — parent attributed the miss to the bus company; no documentation filed)_
  - NOTE (shown after choosing): She writes something down. You can hear the pen. It is probably not the sentence you would have chosen.

## [u3] The Plain Version
*Day 7 — Monday, January 12, 2026 (dayOffset 7)*

At the plan review, the miss is read aloud in its plain version: 'Parent no-showed one screen; rescheduled.' Nobody in the room was on the bus. Nobody in the room has any reason to improve the sentence, and one person in the room — you — has no paper to improve it with.

The plan does not end. It tightens: two extra check-ins a month, added in the tone of a precaution, which is the system's word for a doubt.

**Choices:**
- Sit with it, and start the folder you should have started in January → **u4**  _(FLAG: folderStarted)_
  - NOTE (shown after choosing): Late folders still catch paper. The next appointment is already on the calendar.
- Argue the morning one more time, from memory → **u4**
  - NOTE (shown after choosing): The room listens politely. Memory, unaccompanied by paper, has a short life in rooms like this.

## [u4] One More Chance to Put It in Writing
*Day 9 — Wednesday, January 14, 2026 (dayOffset 9)*

Ms. Hart, to her credit, offers a door: 'If you write down what happened that morning — dates, times, the buses — I can attach it to the file before the summary is written.'

It is late for the statement to do everything a 7:34 call would have done. It is not too late for it to do something.

**Choices:**
- Write the statement tonight — dates, times, both buses — and hand it in → **p5**  _(FLAG: statementFiled; HIDDEN + Statement — parent’s written account of the missed morning filed before the summary)_
  - NOTE (shown after choosing): It goes into the file with her initials on it. The summary will now have two documents to draw from, and one of them is yours.
- Let it go. It was one miss → **u5**
  - NOTE (shown after choosing): It was one miss. Files, unfortunately, do not have a sense of proportion — only a sense of wording.

## [u5] The Second Appointment
*Day 11 — Friday, January 16, 2026 (dayOffset 11)*

The second screen comes and goes without incident — you attend, early, and it changes nothing about the first one, because the first one was never about attendance. It was about a sentence.

The plan summary is being written this week, from the file as it stands.

**Choices:**
- Open the summary when it comes → **end_partial**
  - NOTE (shown after choosing): You already know which sentence is in it.

## [end_partial] A Miss With No Story Attached
*Day 13 — Sunday, January 18, 2026 (dayOffset 13)*

**ENDING.** Debrief:

- The no-show stands in the summary unexplained: no call, no stub, no statement — just a parent-shaped gap at 9:00 on a Friday. The plan continues, tighter. Noah is home, and was never in danger of anything else; what was lost here was wording, and wording is what plans are enforced from.
- The law inside this story: under 55 Pa. Code § 3130.44(d), copies of the plan and your records are released on request. A copy in your hands, early, is how you know what the file says before the file is read aloud in a room.
- The system's memory is the file. A story told at a desk becomes four words. A call placed before the hour becomes a timestamp. This scenario is about which of those the file got.
- Honesty requires this: even a perfect paper trail cannot make a bus come, and a kind worker repaired some of this anyway, late, because she chose to offer the door. Workers vary. Luck varies. The paper is the part that is yours.
