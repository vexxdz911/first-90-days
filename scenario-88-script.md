# THE FIRST 90 DAYS — Scenario 88: “Thirty Days”

*Human-readable script. This document and `scenario-88.json` are generated from a single source and match node-for-node: same IDs, same order, same choices, same effects.*

**The family is fictional — a composite. No real person's story appears here.**

**Content note:** This scenario depicts the month after a dependency disposition order — an appeal deadline, lawyers' offices, visits, and paperwork. There is no graphic content. Players may skip any scene or use the quick exit at any time.

**How to read effects:** `cash −40` changes the player's cash. `FLAG: name` sets a flag the engine tracks. `HIDDEN + item` means the case file quietly records that item at this choice — the player does not see it when it happens. `REQUIRES FLAG: name` means the choice is only available if that flag was set earlier; `REQUIRES NO FLAG: name` means it is only available if that flag was never set. `NOTE:` is text shown to the player right after choosing.

Start date: Monday, April 6, 2026. Day offsets are days since the scenario's start date.

## [start] The Order in the Mail
*Day 0 — Monday, April 6, 2026 (dayOffset 0)*

Your name is Casimir Zielinski — Cas, to everyone who has ever loaded a truck with you. Your son Tomek is six. Three weeks ago, after a winter of missed shifts and a supervision petition you still believe overstated one bad evening, the court adjudicated Tomek dependent and placed him, for now, with his aunt across town.

Today's mail holds the written order. On its last page, under the judge's signature, is a paragraph most people skim: notice that an appeal may be taken to the Superior Court, and that the notice of appeal must be filed within thirty days of the order's entry. Your lawyer mentioned appealing, in the hallway, in the tone people use for weather. The paragraph in the order is not weather. It is a date: Wednesday, May 6, 2026.

The family is fictional — a composite. The thirty days are not fictional at all.

**Choices:**
- Call the lawyer's office today and say the word 'appeal' out loud → **office_call** _(FLAG: calledDayOne)_
  - NOTE (shown after choosing): The receptionist hears the word. It goes in a message slip with today's date on it. Message slips, unlike hallway conversations, have a way of surviving.

## [office_call] The Message Slip
*Day 1 — Tuesday, April 7, 2026 (dayOffset 1)*

Mr. Osei is in court until Thursday. The receptionist is kind and exact: "I'll put it on his desk. He returns calls in order." She does not say which order, or how many desks' worth of slips are ahead of yours.

Thirty days is a long time, measured in shifts. It is a short time, measured in returned phone calls. Both measurements are running.

**Choices:**
- Ask for the earliest appointment on the calendar, not a callback → **appointment** _(FLAG: appointmentSet ; HIDDEN + Appeal — appointment set for day four; the 30-day date stated to the office in writing)_
  - NOTE (shown after choosing): Day four. She reads the date back to you twice. It goes in your folder and, more importantly, in hers.
- Leave it at the callback — he'll get to it → **callback_wait**
  - NOTE (shown after choosing): He will. The only question the story asks is: in what order, and by what date?

## [callback_wait] Eight Days of Order
*Day 8 — Tuesday, April 14, 2026 (dayOffset 8)*

Eight days pass the way days pass when you are working doubles: in bulk. Tomek's aunt sends a photo of him missing a front tooth. The lawyer's callback arrives on day eight, apologetic and brief: "Come in Thursday. Bring the order. And Cas — count the days with me when you get here." Thursday is day eleven. The appointment is made, but the week's silence taught the calendar nothing, and the file is thinner for it: no appointment note from day one, no written word to the office, just a slip that may or may not have survived three desks.

**Choices:**
- Take the day-eleven appointment and bring everything → **meet_late**
  - NOTE (shown after choosing): Eleven days gone. Nineteen remain. Enough — if nothing else goes quiet.

## [appointment] Day Four, Circled
*Day 2 — Wednesday, April 8, 2026 (dayOffset 2)*

The appointment is day four, Thursday, at 9 a.m., before your shift. You circle it on the kitchen calendar and write the other date above it in bigger numbers: MAY 6. Tomek's aunt, told the truth on the phone, says the thing family says when it is working: "Then we don't miss Thursday."

**Choices:**
- Spend the evening getting the folder ready for Thursday → **folder_night**
  - NOTE (shown after choosing): Order, notices, the aunt's address, your pay stubs. A folder is a meeting you have with yourself first.

## [folder_night] The Folder, The Night Before
*Day 3 — Thursday, April 9, 2026 (dayOffset 3)*

Everything you own about this case fits in a folder that cost a dollar. The order. The shelter care papers from March. The visit schedule. Your work schedule, which the petition described in a way you did not recognize and your supervisor's signature describes better.

You write one page of your own: what you think the judge got wrong, in plain sentences. It is not a legal document. It is the raw material one is made from.

**Choices:**
- Put the folder by the door and sleep → **meet**
  - NOTE (shown after choosing): Thursday, 9 a.m. The folder is the first thing you'll touch after the alarm.

## [meet] Mr. Osei Counts Out Loud
*Day 4 — Friday, April 10, 2026 (dayOffset 4)*

Mr. Osei reads the order the way pilots read weather. "Entered April 6," he says. "A notice of appeal is due within thirty days of entry (Pa.R.A.P. 903(a)) — May 6. We will not be filing on May 6. We will be filing weeks early, because paper filed early can be fixed and paper filed at the deadline can only be late."

"Two more things. First: an appeal does not pause Tomek's case. Reviews, visits, services — all of it continues, and all of it still matters, because the case below is where Tomek actually lives. Second: we appeal what the record supports. Bring me everything, and order the rest — the transcript of the adjudication, and the agency's complete record, requested in writing. Agency records are released on request (55 Pa. Code § 3130.44(d)); an appeal argued from excerpts is an appeal argued half-blind." The transcript costs $20.

**Choices:**
- Agree the plan: file within the week, order the transcript, request the complete record in writing → **records** _(cash −20 ; FLAG: appealPlan ; FLAG: recordsRequested ; HIDDEN + Appeal — plan set on day four; transcript ordered; complete agency record requested in writing)_
  - NOTE (shown after choosing): He writes the plan on one page and gives you the copy. One page, three dates, no hallway weather.
- Ask him to handle the papers sometime this month, without the transcript cost → **records_skip**
  - NOTE (shown after choosing): "Sometime this month" is how deadlines describe themselves right before they win.

## [meet_late] Mr. Osei Counts Faster
*Day 11 — Friday, April 17, 2026 (dayOffset 11)*

Day eleven. Mr. Osei reads the order and counts out loud, faster than you'd like. "May 6. We file this week — not because the rules changed, but because we spent our cushion on silence. From here, everything happens on the first try: we order the transcript today, we request the agency's complete record in writing today (55 Pa. Code § 3130.44(d)), and you sign the notice in this office, not by mail." The transcript costs $20, rush.

**Choices:**
- Sign onto the compressed plan and pay the rush transcript cost → **records** _(cash −20 ; FLAG: appealPlan ; FLAG: recordsRequested ; HIDDEN + Appeal — compressed plan set day eleven; transcript ordered rush; complete record requested in writing)_
  - NOTE (shown after choosing): Eleven days bought nothing. The remaining nineteen will have to buy everything.

## [records] Paper, Ordered
*Day 12 — Saturday, April 18, 2026 (dayOffset 12)*

The transcript is ordered; the written request for the complete agency record goes out with a date on it; the notice of appeal is drafted with the order attached. In the waiting room, Tomek's aunt texts: visit Saturday, his tooth is under the pillow, the fairy has been notified.

This is what an appeal looks like from the parent's chair: not argument, not drama — errands with deadlines, done in the right order, with receipts.

**Choices:**
- Keep Saturday's visit and bring the tooth-fairy report to the folder → **visit_sat** _(FLAG: visitKept)_
  - NOTE (shown after choosing): The case below does not pause. Neither, it turns out, does being his father.

## [records_skip] Sometime This Month
*Day 13 — Sunday, April 19, 2026 (dayOffset 13)*

The papers move at office speed, which is to say at the speed of every other family's emergency too. By day thirteen there is a draft notice, no transcript, and a plan to 'request the file when things calm down.' Things, in a dependency office, do not calm down; they accumulate. The appeal can still be filed — filing needs a notice and an order, not a transcript — but it will be an appeal whose lawyer meets the full record after the panel does.

**Choices:**
- Insist the notice be filed this week anyway, transcript or not → **filed_receipt** _(FLAG: noticeFiled)_
  - NOTE (shown after choosing): Filed is filed. The notice beats the clock even if the homework limps behind it.
- Let the office file it when they file it — they know the dates → **day31_node**
  - NOTE (shown after choosing): They do know the dates. Knowing and filing, in a busy office in a busy month, turn out to be different departments.

## [visit_sat] Saturday, With a Missing Tooth
*Day 19 — Saturday, April 25, 2026 (dayOffset 19)*

Visits are where the case below keeps its real ledger. The visit supervisor's notes will say: father arrived on time, brought the tooth fairy's official correspondence, read two chapters, left when the hour ended without making it strange. File paper is forever, and visit paper is the kind judges actually quote.

Your aunt hugs you at the door. "May 6 is handled," she says, "so handle Saturdays."

**Choices:**
- Ask, in writing, for the visit note to record today's make-up reading time → **sign_day** _(FLAG: visitLog ; HIDDEN + Visit log — on-time arrival and make-up reading noted in writing)_
  - NOTE (shown after choosing): The supervisor writes it while you watch. A good Saturday, on paper, where good Saturdays count.

## [sign_day] Signing Day
*Day 23 — Wednesday, April 29, 2026 (dayOffset 23)*

The notice of appeal is one page long. Under it: the order appealed from, identified by its date. Mr. Osei slides it across with the plan page. "Read the order's date back to me," he says, "and then sign." Filing early was the whole strategy: whatever the clerk's office finds wrong, there is a week to fix it in.

**Choices:**
- Sign the notice of appeal → **filed_receipt** _(FLAG: noticeFiled ; REQUIRES FLAG: appealPlan)_
  - NOTE (shown after choosing): Your signature, his signature, the order attached. It is not an argument. It is a door, opened on time.
- Ask to take it home and sign it over the weekend → **sign_late**
  - NOTE (shown after choosing): The weekend is two days. The plan had weeks of cushion. Both statements are true; only one of them is wise.

## [sign_late] The Weekend Signature
*Day 27 — Sunday, May 3, 2026 (dayOffset 27)*

The notice gets signed Sunday night, day twenty-seven, and driven to the office Monday — day twenty-eight of thirty, the cushion spent down to two days by a weekend of carrying one page around a kitchen. Mr. Osei files it without comment, which from him is a comment.

**Choices:**
- Let it be filed and keep every Saturday from here → **filed_receipt_late** _(FLAG: noticeFiled)_
  - NOTE (shown after choosing): Filed day twenty-eight. The clock was beaten by the plan, not by the weekend.

## [filed_receipt_late] The Clerk's Stamp, Later Than Planned
*Day 28 — Monday, May 4, 2026 (dayOffset 28)*

Filed, day twenty-eight of thirty — inside the window, with two days of margin where the plan had drawn weeks. The stamp gives the appeal a docket number in the Superior Court and gives you a receipt that goes in the folder behind the plan page. The appeal is alive and properly born, with its transcript ordered and its record requested; it is simply far closer to the edge than anything in this family was supposed to come.

It beats the alternative by exactly two days.

**Choices:**
- Go home and tell Tomek's aunt the appeal exists → **below_review**
  - NOTE (shown after choosing): "Exists," she says, tasting the word. "Good. Now it has to be fed. Saturdays."

## [filed_receipt] The Clerk's Stamp
*Day 25 — Friday, May 1, 2026 (dayOffset 25)*

Filed. The stamp gives the appeal a docket number in the Superior Court and gives you a receipt that goes in the folder behind the plan page. From here the appeal becomes a season of paper: the record is transmitted, briefs are written from it, and judges you will never meet read a case that, to them, is exactly as thick as what was filed below plus what was ordered since.

Which is why a transcript ordered on day four matters more than an opinion offered on day forty. The panel will read the hearing, not remember it.

**Choices:**
- Go home and tell Tomek's aunt the appeal exists → **below_review**
  - NOTE (shown after choosing): "Exists," she says, tasting the word. "Good. Now it has to be fed. Saturdays."

## [below_review] Meanwhile, Below
*Day 45 — Thursday, May 21, 2026 (dayOffset 45)*

Day forty-five finds the case where it always was: in a courtroom, on a review date, with Tomek's life proceeding at six-year-old speed. The appeal is pending; the judge below notes it in one sentence and moves on to visits, services, and the plan — because the appeal does not pause any of it, and the review is where returns are actually built.

Your written progress summary, with the visit log attached, is handed up and filed. Whatever the panel eventually decides about the order, the record below it is being written by someone who shows up on Saturdays.

**Choices:**
- Keep the folder growing while the appeal is read → **end_filed**
  - NOTE (shown after choosing): Two tracks, one father, paper on both.

## [end_filed] Ending — Filed on Time, Fed on Saturdays
*Day 80 — Thursday, June 25, 2026 (dayOffset 80)*

The appeal is alive: noticed on time, docketed, briefed from a complete record — the transcript ordered under the day-four plan and the agency file you requested in writing are open on your lawyer's desk, not sealed in an office across town. No judge has ruled. Tomek is still at his aunt's, still losing teeth at the correct developmental rate, and his case below moves through reviews where his father's Saturdays are a matter of record.

That is what thirty days bought: not a victory, a hearing in the court that can actually revisit the order — earned by a message slip, an appointment, and a folder, in that order.

**ENDING — Debrief:**

THE WIN, NAMED HONESTLY — This is a partial win: the appeal exists and is properly built. It decides nothing yet. No ending in this scenario has the Superior Court ruling — that reading takes the time it takes, and the story's subject was the window, not the outcome.

THE LAW IN THE BEATS — A notice of appeal must be filed within 30 days after the entry of the order appealed from (Pa.R.A.P. 903(a), verified from the official text of the Rules of Appellate Procedure for this batch). An appeal does not pause the dependency case below — reviews, visits, and services continue, and progress there is recorded the same way it always is. The complete-record request rests on 55 Pa. Code § 3130.44(d): agency records are released upon request. Counsel's role here is the one the rules assume: the parent has counsel (42 Pa.C.S. § 6337), and the strategy was calendaring, not heroics.

THE HIGHEST-LEVERAGE MOVES — Two, in order: the appointment asked for on day one (which turned a hallway remark into a dated plan), and the written request for the complete record on day four (§ 3130.44(d)). Appeals are read from paper. Both moves made paper.

WHAT NO STRATEGY CONTROLS — The panel's eventual reading, the lawyer's other emergencies, the clerk's backlog, an aunt's patience. The route controlled the dates and the documents — the only parts of an appeal a parent can hold in his hands. Outcomes also turn on judges and luck; a missed deadline turns on nothing at all, which is the point of beating it early.


## [day31_node] Day Thirty-One
*Day 31 — Thursday, May 7, 2026 (dayOffset 31)*

It is May 7. Somewhere in a courthouse, April 6 plus thirty days has quietly become April 6 plus thirty-one. No one calls to tell you. Deadlines in this system do not slam; they simply stop being available, the way a bus stop is not available after the bus has gone.

**Choices:**
- Call the office anyway and ask what exists now → **end_late**
  - NOTE (shown after choosing): Mr. Osei is kind about it, which somehow makes the arithmetic louder.

## [end_late] Ending — Day Thirty-One
*Day 31 — Thursday, May 7, 2026 (dayOffset 31)*

The notice of appeal was never filed inside its window. The order of April 6 stands as the last word of the court that made it — not because any judge weighed Cas's arguments and found them wanting, but because no filing ever carried them anywhere. The case below continues: reviews, visits, the plan. Those doors remain, and they are real doors. The appellate one does not.

Nobody in this ending behaved villainously. A message slip waited its turn. Callbacks came in order. The month was busy for everyone. The thirty days ran anyway, because running is all they do.

**ENDING — Debrief:**

WHY THIS ENDING — A notice of appeal must be filed within 30 days after the entry of the order (Pa.R.A.P. 903(a)). The failure to file a timely notice implicates the appellate court's jurisdiction: an untimely appeal is, in the ordinary course, quashed rather than heard. The scenario states this as the lawyers in it state it — a deadline that is not a guideline — and no filing trick in the story was allowed to revive it.

WHAT WAS AVAILABLE — The same moves as the winning route: an appointment asked for by name on day one, a plan with the date written on it, the complete record requested in writing under 55 Pa. Code § 3130.44(d), and counsel's help under 42 Pa.C.S. § 6337. Every one of them existed on April 6. All of them were cheaper than May 7.

WHAT NO STRATEGY CONTROLS — Said plainly, because this debrief owes it: Cas's love for his son appears nowhere in this outcome, because outcomes in this system turn on paper, calendars, workers, judges, and luck. The deadline did not measure him. It measured a filing. The training point of the scenario is that the filing was his to make — early, boring, and on time.

