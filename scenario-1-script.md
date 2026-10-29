# THE FIRST 90 DAYS — Scenario 1: "The Thursday Gap"

*Human-readable script. This document and `scenario-1.json` are generated from a single source and match node-for-node: same IDs, same order, same choices, same effects.*

**The family is fictional — a composite. No real person's story appears here.**

**Content note:** This scenario depicts a child-welfare investigation and a temporary removal, told through procedure and paperwork. There is no graphic content. Players may skip any scene or use the quick exit at any time.

**How to read effects:** `cash −40` changes the player's cash. `FLAG: name` sets a flag the engine tracks. `HIDDEN + item` means the scored assessment form quietly rates that item at this choice — the player does not see it when it happens. `NOTE:` is text shown to the player right after choosing.

Start date: Monday, March 2, 2026. Day offsets are days since that date. Removal, when it happens, occurs on Day 0; the shelter care hearing falls on Day 3 — Thursday, March 5, 2026 — exactly 72 hours later.

## [start] The Argument, Then the Quiet
*Day 0 — Monday, March 2, 2026 — Monday, March 2, 2026 (dayOffset 0)*

You work the evening shift at a warehouse outside town. You have two children: Eli, seven, and June, four.

Yesterday, you and Marcus — their father, who moved out last year — argued on the phone about pickup times. It got loud. It ended with him saying, "We'll see what a judge thinks."

This morning, while you did laundry, Eli and June stayed next door with Mrs. Okafor, like they have a hundred times. You do not know yet that a report was called in after the argument.

**Choices:**
- Text your sister Dana about the argument, so someone else knows it happened → **door**  _(FLAG: sisterAware)_
  - NOTE (shown after choosing): Dana replies: "Save the messages. All of them."
- Keep it between you and Marcus → **door**

## [door] Someone at the Door
*Day 0 — The knock — Monday, March 2, 2026 (dayOffset 0)*

There is a knock at 12:40, before your shift. A woman with a badge and a folder introduces herself: Ms. Bell, from the county children and youth agency.

She says a report came in. The concerns, as she describes them: the children were said to be left alone, and there are questions about conditions in the home. She needs to see the children and the home today.

**Choices:**
- Let her in now → **home_visit**  _(HIDDEN + Home environment — rated from an unprepared visit)_
- Ask what the report says, and whether you can have thirty minutes first → **pause**
  - NOTE (shown after choosing): She agrees to wait. She also writes down that you asked. Asking questions is allowed — and it is noticed.

## [home_visit] The House, As It Is
*Day 0 — The visit — Monday, March 2, 2026 (dayOffset 0)*

The house is mid-week real: a laundry pile on the couch, dishes in the sink, June's cereal bowl still on the table. The children are fine — fed, dressed, watching a show, happy to show her their drawings.

Ms. Bell walks through slowly. She opens the refrigerator. She looks in the children's room. She writes the whole time.

**Choices:**
- Explain the morning plainly: the kids were with Mrs. Okafor during laundry, like always → **interview**  _(HIDDEN + Supervision arrangement — neighbor, informal)_
  - NOTE (shown after choosing): She writes that down too. What you say becomes part of the record — in your words, if you give them.
- Say the house is usually neater, and leave it at that → **interview**  _(HIDDEN + Supervision arrangement — not explained)_

## [pause] Thirty Minutes
*Day 0 — Thirty minutes — Monday, March 2, 2026 (dayOffset 0)*

Mrs. Okafor takes Eli and June next door for a snack. You move fast: dishes, laundry into a basket, floor cleared. Your hands shake once, on the stairs.

When Ms. Bell comes in, the house looks different. She looks at the clock on the wall, and then at the rooms, and writes.

**Choices:**
- Invite her to look wherever she needs to → **interview**  _(HIDDEN + Home environment — rated after a short delay)_
  - NOTE (shown after choosing): The delay helped the house. It is part of the record too — both the asking and the tidier rooms.

## [interview] Questions, and a Form You Cannot See
*Day 0 — The interview — Monday, March 2, 2026 (dayOffset 0)*

At your kitchen table, Ms. Bell asks about your shift, your schedule, and who watches the children while you work. As you answer, she fills in a scored assessment form. You cannot see the items on it. Nobody offers to show you.

Your childcare is a patchwork: Mrs. Okafor on Tuesdays, Dana on weekends, a coworker's teenager sometimes. Thursdays, between your shift start and Mrs. Okafor getting home, there is a gap you have been covering by leaving twenty minutes late and hoping.

**Choices:**
- Describe the patchwork honestly — including the Thursday gap → **interview2**  _(HIDDEN + Supervision plan — Thursday gap, named by you)_
  - NOTE (shown after choosing): The hard part is now on the record — in your words, and next to your plan to fix it.
- Say childcare is "handled," and keep it short → **interview2**  _(HIDDEN + Supervision plan — unclear to the worker)_
  - NOTE (shown after choosing): Short answers feel safer. On a form, "unclear" is itself an answer.

## [interview2] The Rest of the Questions
*Day 0 — The interview, part two — Monday, March 2, 2026 (dayOffset 0)*

She asks about Marcus. About the argument. About whether anything like this has happened before, and whether there is anyone you call when things get hard.

Some of these questions are about safety. Some become items on the form. From your side of the table, there is no way to tell which are which.

**Choices:**
- Tell her the argument was about custody — and that the report came the next day → **decision**  _(HIDDEN + Report context — custody dispute, on the record)_
  - NOTE (shown after choosing): Context travels with the file now, wherever the file goes.
- Keep the argument private — it is family business → **decision**  _(HIDDEN + Report context — not on the record)_

## [decision] She Steps Outside to Call Her Supervisor
*Day 0 — The decision — Monday, March 2, 2026 (dayOffset 0)*

Ms. Bell steps onto the porch to call her office. Through the door you can hear the tone, not the words.

When she comes back in, she is honest about the shape of it: the Thursday gap is the problem she has to answer for. What happens next turns on one practical question — whether a safe adult can be with the children while the gap gets fixed.

**Choices:**
- Call Dana. She can come tonight, and stay the week → **safety_plan**  _(FLAG: supportEngaged)_
  - NOTE (shown after choosing): A person who can show up is not a small thing in this system. It is the thing.
- There is no one who can come tonight → **removal**  _(FLAG: removed)_
  - NOTE (shown after choosing): Hear this clearly: this branch is about tonight's logistics — a shift, a distance, a phone that wasn't answered. It is not a verdict on you as a parent.

## [safety_plan] Paper Instead of Goodbye
*Day 0 — Evening — Monday, March 2, 2026 (dayOffset 0)*

Dana arrives with an overnight bag. Ms. Bell writes a safety plan at your table: the children sleep at Dana's tonight; Mrs. Okafor confirms Tuesdays in writing; you have one week to close the Thursday gap, with proof.

It is two pages. It asks for your signature.

**Choices:**
- Read every line before you sign → **home_week**  _(FLAG: readPlan)_
  - NOTE (shown after choosing): One line surprises you — a check-in visit you hadn't heard out loud. Now you have.
- Sign, so the children can get to bed on time → **home_week**

## [home_week] Closing the Thursday Gap
*Day 2 — Wednesday, March 4, 2026 — Wednesday, March 4, 2026 (dayOffset 2)*

The plan gives you until Friday to prove Thursdays are covered. Your supervisor can maybe move things. Dana has offered twice. The clock on a safety plan does not care that you also worked two shifts and June had a fever.

Paperwork week has begun.

**Choices:**
- Swap Thursday shifts with a coworker — it costs you your weekend hours → **home_records**  _(cash -40; FLAG: thursdayCovered; HIDDEN + Supervision plan — Thursday covered, documented)_
  - NOTE (shown after choosing): Coverage, with a name and a schedule. On the form, that is a different item than a promise.
- Ask Dana to cover Thursdays until June, and get it in a text you can show → **home_records**  _(FLAG: thursdayCovered; HIDDEN + Supervision plan — Thursday covered by family)_

## [home_records] The Flyer at the Library
*Day 5 — Saturday, March 7, 2026 — Saturday, March 7, 2026 (dayOffset 5)*

At the library, a parent advocate has left flyers by the door. One line stops you: you have the right to ask for your own assessment record — and under the regulation, it "shall be released upon request."

You did not know you could ask. Almost nobody does. (55 Pa. Code § 3130.44(d))

**Choices:**
- Write the request tonight and send it in the morning → **home_reveal**  _(FLAG: recordsRequested)_
  - NOTE (shown after choosing): It costs a stamp and ten minutes. Watch what it changes.
- Let it go — things seem to be going fine → **home_review**
  - NOTE (shown after choosing): Fine is real. So is not knowing what the form says about you.

## [home_reveal] Reading What Was Written About You
*Day 8 — Tuesday, March 10, 2026 — Tuesday, March 10, 2026 (dayOffset 8)*

The packet arrives in a thick envelope. Some lines are blacked out. But the scored items are there: supervision, home environment, cooperation, support.

You can see the Thursday item — written when the gap was real. You can also see that the neighbor arrangement was recorded in a single short line. You write a one-page correction, calmly, with dates, and keep a copy.

**Choices:**
- Bring the packet and your correction to the review → **home_review**  _(FLAG: broughtCorrection)_
  - NOTE (shown after choosing): Your words, in the file, next to theirs. That is what the request is for.

## [home_review] The First Review
*Day 12 — Saturday, March 14, 2026 — Saturday, March 14, 2026 (dayOffset 12)*

Ms. Bell comes back with a checklist. Thursday coverage: proven. Dana's nights: confirmed. Mrs. Okafor's letter: in the file.

She tells you what remains: a few more weeks of check-ins, and the plan steps down. The children never left your home. The file, though, does not close as fast as the visits do.

**Choices:**
- Ask what, exactly, remains open — and write it down → **end_home**
  - NOTE (shown after choosing): She lists two items. Two is a number you can finish.

## [end_home] Ending — Home, With Paperwork
*Day 15 — Tuesday, March 17, 2026 — Tuesday, March 17, 2026 (dayOffset 15)*

**ENDING.**

> WHAT THE FORM SAID (the hidden assessment, revealed): Your playthrough was rated on items you could not see — home environment (rated from whichever visit you allowed), supervision arrangement, the Thursday supervision gap, report context, and your support network. Honest answers did not erase the Thursday item; they changed what was written beside it. Coverage that was documented moved the supervision item. Coverage that was only promised did not.

> THE LAW UNDER THIS PATH: The record you requested is yours to ask for — the agency's file material "shall be released upon request" (55 Pa. Code § 3130.44(d)). If a report is ever marked "indicated" against a parent, that parent can ask for it to be amended or expunged, and the written request must be made within 90 days of being notified (23 Pa.C.S. § 6341(a)(2)).

> THE HONEST PART: This ending was not earned by being a good parent, and the other endings are not punishments for being a bad one. This one turned on a sister who could drive over, a neighbor who answered her door, and a supervisor who allowed a swap. Different worker, different week, different luck — the same parent can land in a different ending. That is the thing this scenario exists to show.

## [removal] The Hardest Hour
*Day 0 — Removal — Monday, March 2, 2026 (dayOffset 0)*

With no safe adult available tonight, Ms. Bell makes the call she warned you about. The children will be placed in emergency care while the court looks at the case. June holds your sleeve. Eli asks twice if he did something wrong. He did not. Neither, the record will show, is this hour a finding about you.

Before she leaves, she hands you a paper with a court date and a phone number, and tells you the law's promise: there must be a shelter care hearing within 72 hours — by Thursday, March 5, 2026.

**Choices:**
- Write down everything she says, even through tears → **counsel**  _(FLAG: tookNotes)_
  - NOTE (shown after choosing): Names, times, the phone number. Paper remembers what shock forgets.
- Hold the paper. It is all you can do tonight → **counsel**

## [counsel] A Lawyer of Your Own
*Day 1 — Tuesday, March 3, 2026 — Tuesday, March 3, 2026 (dayOffset 1)*

The paper says you have the right to be represented by a lawyer — and if you cannot afford one, the court can appoint one for you. That right is in the law, not in anyone's kindness. (42 Pa.C.S. § 6337)

The hearing is Thursday. The phone at the courthouse rings a long time before anyone picks up.

**Choices:**
- Stay on the line and ask how to get counsel appointed before Thursday → **hearing**  _(FLAG: counsel)_
  - NOTE (shown after choosing): A name, an office, a person expecting your call. Thursday just changed shape.
- Decide to speak for yourself on Thursday → **hearing**
  - NOTE (shown after choosing): Allowed — and much harder. The judge will have the agency's lawyer across the room.

## [hearing] The Shelter Care Hearing
*Day 3 — Thursday, March 5, 2026 — Thursday, March 5, 2026 (dayOffset 3)*

A small courtroom. The judge has the report and a summary of the scored assessment. You do not have either one. This hearing asks one narrow question: where the children stay while the case is sorted out. (42 Pa.C.S. § 6332)

It has been 72 hours, as promised. What the judge decides will turn on what can be shown, today, about Thursdays.

**Choices:**
- Hand up Dana's letter and your supervisor's note: Thursdays are covered, starting now → **return_home**  _(FLAG: planPresented)_
  - NOTE (shown after choosing): Paper, names, dates. The judge reads all of it.
- You do not yet have proof of Thursday coverage → **continued**
  - NOTE (shown after choosing): Not because coverage is impossible — because proof takes days you have not been given yet.

## [return_home] Home Tonight, On Conditions
*Day 3 — Thursday, March 5, 2026 — Thursday, March 5, 2026 (dayOffset 3)*

The judge returns the children to you tonight, under a court-ordered safety plan: Dana's letter filed, Thursday coverage in place, check-in visits to come, and a further hearing ahead where the facts themselves get decided.

Eli sleeps in his own bed. The folder on your counter is now the most important furniture in the house.

**Choices:**
- Ask the worker, before you leave, what the first check-in will look at → **return_checkin**
  - NOTE (shown after choosing): She tells you: coverage proof, the sign-in sheet, the plan's first page. Now you know the test before you take it.

## [return_checkin] The First Check-In
*Day 7 — Monday, March 9, 2026 — Monday, March 9, 2026 (dayOffset 7)*

The worker visits for an hour. She checks the coverage letters, the sign-in sheet from Mrs. Okafor, food in the refrigerator, the plan on the counter. She writes as she goes — but this time you have a fair idea what the items are.

June shows her a drawing. Some visits are just visits. This one mostly is.

**Choices:**
- Show her the folder you have started keeping — dates, receipts, letters → **return_discovery**  _(FLAG: keptFolder; HIDDEN + Documentation — parent-kept folder)_
  - NOTE (shown after choosing): Your record, kept in parallel with theirs, from the first week.
- Walk her through the week from memory → **return_discovery**

## [return_discovery] Seeing the Case Against You
*Day 10 — Thursday, March 12, 2026 — Thursday, March 12, 2026 (dayOffset 10)*

Your lawyer explains the next phase plainly: before the hearing that decides the facts, the assessment and reports the agency will rely on can be requested — you get to see the evidence first. (Pa.R.J.C.P. 1340(B)(1))

She is honest about the edge of it: whether that rule reaches every scored item of an assessment form has not been tested. She intends to ask anyway. She also reminds you the assessment record itself can be requested directly — it "shall be released upon request." (55 Pa. Code § 3130.44(d))

**Choices:**
- Ask her to request everything the rule covers — and file your own record request too → **end_return**  _(FLAG: recordsRequested)_
  - NOTE (shown after choosing): Two requests, two paper trails. This is the highest-leverage move in this scenario, and it costs almost nothing.
- Focus on the services list for now → **end_return**

## [end_return] Ending — Home After a Hearing, Case Open
*Day 13 — Sunday, March 15, 2026 — Sunday, March 15, 2026 (dayOffset 13)*

**ENDING.**

> WHAT THE FORM SAID (the hidden assessment, revealed): The items moving underneath this path were the Thursday supervision gap, the day-0 home environment rating, report context, and documentation. The hearing did not turn on whether you are a loving parent — the judge never doubted it out loud. It turned on proof: a letter, a schedule, names and dates that could be handed up.

> THE LAW UNDER THIS PATH: A shelter care hearing must be held within 72 hours of a child being taken into custody (42 Pa.C.S. § 6332; 23 Pa.C.S. § 6315(d)). You had the right to counsel, and to appointed counsel if you could not afford one (42 Pa.C.S. § 6337). Disclosure of the material the agency relies on in the adjudication phase is provided for by Pa.R.J.C.P. 1340(B)(1) — untested, as your lawyer said, for every part of a scored assessment form. Your own record request rests on 55 Pa. Code § 3130.44(d). If an indicated report is ever at issue, the appeal window is 90 days from notification (23 Pa.C.S. § 6341(a)(2)).

> THE HONEST PART: The children came home in this ending because a sister wrote a letter and a supervisor signed a schedule inside of three days. A slower mail day, a supervisor on vacation, a sterner judge — the same parent, the same love, a different ending. Outcomes here turn on workers, judges, resources, and luck as much as on anything a parent does. The game will never tell you otherwise.

## [continued] Not Yet
*Day 3 — Thursday, March 5, 2026 — Thursday, March 5, 2026 (dayOffset 3)*

The judge continues the placement for now. The children stay in care while services are set up and the coverage question gets answered with documents, not hope.

You are handed one page: a visit schedule, two referrals, and dates. It is not much paper for the size of what it holds.

**Choices:**
- Ask, before you leave the courtroom, exactly what has to change → **first_visit**  _(FLAG: askedBenchmarks)_
  - NOTE (shown after choosing): The list is specific: coverage proof, the parenting class, home visits. Specific can be finished.

## [first_visit] One Hour, Supervised
*Day 6 — Sunday, March 8, 2026 — Sunday, March 8, 2026 (dayOffset 6)*

The visit is in a room with a couch, a toy kitchen, and a clock that everyone can see. June runs to you. Eli tells you about the foster home's dog, carefully, watching your face.

A worker sits in the corner, kind and quiet, writing. The goodbye takes four minutes and costs the rest of your day.

**Choices:**
- Take the bus across town — you are twenty minutes early → **service_plan**  _(cash -12)_
  - NOTE (shown after choosing): Early, every time. It goes in the notes. So does everything.
- Ride with a friend, and bring the children's favorite snacks → **service_plan**

## [service_plan] The Service Plan
*Day 9 — Wednesday, March 11, 2026 — Wednesday, March 11, 2026 (dayOffset 9)*

The plan arrives as a stack: a parenting class on Tuesdays — your shift day; home visits twice a month; Thursday coverage to be documented; a drug screen you did not expect, from a checkbox you never saw.

Each item is reasonable alone. Together, they are a second job, unpaid, with court dates.

**Choices:**
- Read every page, and ask for the class schedule in writing → **records_removal**  _(FLAG: readPlan)_
  - NOTE (shown after choosing): The Tuesday class has a Thursday section. You would never have known without asking.
- Sign at the office so you do not miss your shift → **records_removal**

## [records_removal] The Same Flyer, a Different Week
*Day 11 — Friday, March 13, 2026 — Friday, March 13, 2026 (dayOffset 11)*

Your lawyer mentions it in passing, the way people mention weather: you can request your assessment record. By law it "shall be released upon request." Most parents never hear the sentence. (55 Pa. Code § 3130.44(d))

You think about the form on the kitchen table — the one filled in while you could not see it.

**Choices:**
- Send the written request this week → **reveal_removal**  _(FLAG: recordsRequested)_
  - NOTE (shown after choosing): A stamp, a date, a copy for your folder. The cheapest power in this whole system.
- Skip it — the service plan is enough to carry → **discovery**
  - NOTE (shown after choosing): Understandable. The plan is heavy. But the form will be at the next hearing whether you have read it or not.

## [reveal_removal] Your File, in Your Hands
*Day 14 — Monday, March 16, 2026 — Monday, March 16, 2026 (dayOffset 14)*

The packet is thick, and partly blacked out, and still: there it is. The supervision item, scored from day 0 — before your Thursday fix existed. The home environment item, rated from a mid-week house. A cooperation item you did not know you were earning.

You write a correction with your lawyer: dates, the new schedule, Dana's letter. It goes into the file, in your words, before the review.

**Choices:**
- Make sure the correction is filed before the review hearing → **discovery**  _(FLAG: broughtCorrection)_
  - NOTE (shown after choosing): The file the judge reads now contains your voice too.

## [discovery] Before the Next Hearing
*Day 15 — Tuesday, March 17, 2026 — Tuesday, March 17, 2026 (dayOffset 15)*

Your lawyer requests the assessment and the reports the agency will rely on at the next phase — you are entitled to see the evidence before the hearing that decides the facts. (Pa.R.J.C.P. 1340(B)(1))

She flags the limit honestly: whether that rule reaches every scored item on an assessment form is untested. Asking costs nothing; the answer will teach the next family something too.

**Choices:**
- Read what arrives with your lawyer, line by line → **end_continued**
- Ask for the summary — work is crushing this month → **end_continued**
  - NOTE (shown after choosing): The summary leaves out the supervision item's date. Dates are where this case lives. Your lawyer keeps the full copy anyway.

## [end_continued] Ending — Still Placed, Plan Running
*Day 18 — Friday, March 20, 2026 — Friday, March 20, 2026 (dayOffset 18)*

**ENDING.**

> WHAT THE FORM SAID (the hidden assessment, revealed): Underneath this path sat the Thursday supervision gap (scored on day 0, before any fix was possible), the home environment rating from an unprepared house, a cooperation item shaped by how the first interview went, and report context. Notice what is not on that list: how much you love your children. The form has no item for it.

> THE LAW UNDER THIS PATH: The shelter care hearing came within 72 hours, as required (42 Pa.C.S. § 6332; 23 Pa.C.S. § 6315(d)). Counsel was your right (42 Pa.C.S. § 6337). Your record request rests on 55 Pa. Code § 3130.44(d) — "shall be released upon request" — and disclosure for the adjudication phase on Pa.R.J.C.P. 1340(B)(1), untested for every part of a scored assessment form. If an indicated report is at issue, its appeal window is 90 days from notification (23 Pa.C.S. § 6341(a)(2)). And a federal clock now runs quietly in the background of this case: if a child remains in foster care for 15 of the most recent 22 months, the law presses toward filing for termination of parental rights, with exceptions (42 U.S.C. § 675(5)(E)). Nobody may mention that clock to you. It runs anyway.

> THE HONEST PART: This ending is not a loss, and you did not cause it by failing some test of parenthood. The children are still placed at day 18 because proof moves slower than hearings, because a class met on your shift day, because a form was scored before help was offered. Workers, judges, calendars, and luck all hold pieces of this outcome. What the record request changed — and it is the single highest-leverage move in this scenario — is that at the next hearing, your voice is inside the file too.

---
*End of script. 27 nodes, 3 endings. Companion files: `design.md` (game design document), `scenario-1.json` (engine data, identical structure).*