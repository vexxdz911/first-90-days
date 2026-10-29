# THE FIRST 90 DAYS — Scenario 35: “The Hearing That Wasn't”

*Human-readable script. This document and `scenario-35.json` are generated from a single source and match node-for-node: same IDs, same order, same choices, same effects.*

**The family is fictional — a composite. No real person's story appears here.**

**Content note:** This scenario depicts a dependency case whose hearings are repeatedly continued while a federal timeline runs — told through procedure, paperwork, and calendars. There is no graphic content. Players may skip any scene or use the quick exit at any time.

**How to read effects:** `cash −40` changes the player's cash. `FLAG: name` sets a flag the engine tracks. `HIDDEN + item` means the case file quietly records that item at this choice — the player does not see it when it happens. `NOTE:` is text shown to the player right after choosing.

Start date: Monday, March 10, 2025 (placement; the playable story opens at month 9, Wednesday, December 10, 2025). Day offsets are days since the scenario's start date.

## [start] Month Nine
*Day 275 — Wednesday, December 10, 2025 — Wednesday, December 10, 2025 (dayOffset 275)*

Nine months ago, on a March Monday you no longer talk about at work, your son Owen — seven, all elbows and questions — was placed with a foster family across town. The reasons are in a file. So is everything since: the classes, the screens, the visits you have not missed.

You are Paula. You work as a home-health aide, driving between other people's houses with a folder of your own paperwork riding in the trunk.

This morning your caseworker, Mr. Osei, said the sentence caseworkers say carefully: “We're coming up on some dates.” He did not mean the holidays. Owen has been in care nine months. A federal clock counts fifteen. It does not pause for anyone, and it is already more than half spent.

**Choices:**
- Ask him to show you the dates, in writing, before you leave → **wall**
  - NOTE (shown after choosing): He prints the review schedule. At the bottom, in the same plain type as everything else: June 10, 2026.

## [wall] Two Calendars
*Day 277 — Friday, December 12, 2025 — Friday, December 12, 2025 (dayOffset 277)*

At home you put two calendars side by side on the refrigerator. Yours runs in weeks: shifts, visits on Thursdays, Owen's school concert. The case's runs in months, and one of its dates is circled in a color you did not choose.

June 10, 2026. Fifteen months from the March morning Owen was placed. Your lawyer explained it once, early on: at fifteen of the most recent twenty-two months in care, the agency is generally expected to move toward a different kind of filing — unless an exception fits. It is not a verdict. It is a date when the conversation changes.

Your next review hearing is in January. That feels far away. Against June, it is not far at all.

**Choices:**
- Call your lawyer and ask what January is actually for → **counsel**
  - NOTE (shown after choosing): She answers on the second ring, which still surprises you, nine months in.

## [counsel] What Your Lawyer Can and Cannot Promise
*Day 280 — Monday, December 15, 2025 — Monday, December 15, 2025 (dayOffset 280)*

Ms. Okafor has represented you since the beginning — parents in these cases have the right to counsel, and she is yours (42 Pa.C.S. § 6337). She is honest in the way you have learned to trust: she tells you what she does not know.

“I can't promise you a hearing that stays on the calendar,” she says. “Hearings move. Witnesses get sick, reports run late, courtrooms get double-booked. I won't invent a rule for you — there isn't a simple one I can hand you.”

“What I can teach you is a practice. Before every date, we file a short written statement saying you are ready and what you are ready to show. If a date moves, we ask — in plain words, on the record — that the reason and the new date be stated. And you keep a running chronology: every date, every move, in order. Delay that is written down is delay the court can see.”

**Choices:**
- Ask what you should be keeping, starting tonight → **records**
  - NOTE (shown after choosing): “Everything,” she says. “But start with the file itself. You are allowed to see it.”

## [records] Your Own File, Again
*Day 284 — Friday, December 19, 2025 — Friday, December 19, 2025 (dayOffset 284)*

You have seen pieces of your case file — the plan, the visit notes. You have never asked for the whole record at once, including the assessment the agency completed: the form, the item ratings, the outcome.

Ms. Okafor explains the plain version: your case record “shall be released upon request” (55 Pa. Code § 3130.44(d)). One page, in writing, dated, with a copy for your folder. The request costs a stamp. Not asking costs whatever the file would have taught you.

**Choices:**
- Write the request this week — the full record, including the complete assessment → **records_arrive**  _(FLAG: recordsRequested; HIDDEN + Case record requested in writing — full record, assessment included)_
  - NOTE (shown after choosing): A stamp, a date, a copy for the folder. The cheapest power in this whole system.
- Skip it — the hearing is what matters, not the paper behind it → **no_records**
  - NOTE (shown after choosing): Understandable. January is coming. But hearings are made of paper, and this paper would have been yours.

## [records_arrive] Reading at the Kitchen Table
*Day 291 — Friday, December 26, 2025 — Friday, December 26, 2025 (dayOffset 291)*

The packet arrives in a thick envelope. Visit notes you remember living. Service letters you already had. And the assessment: pages of items, each rated, ending in an outcome you have heard described but never seen built.

Some ratings match your memory. Two do not — one rates a Thursday in October you can document differently, because you kept the sign-in sheet. You write the date and the sheet's location in the margin, in pencil, the way Ms. Okafor taught you.

A note on the disclosure rules, which she made you repeat back: when assessment material is disclosed in the adjudication phase under Rule 1340(B)(1), this assessment approach is untested — it has not been validated the way its use assumes. You write that down too. In this story, the ratings are a claim, not a verdict.

**Choices:**
- Start the chronology tonight — page one: March 10, 2025 → **prep1**  _(FLAG: chronologyKept; HIDDEN + Chronology started — placement date, every hearing date, in order)_
  - NOTE (shown after choosing): One page. Nine months compressed into dates. It is heavier than it looks.

## [no_records] The Envelope You Didn't Ask For
*Day 291 — Friday, December 26, 2025 — Friday, December 26, 2025 (dayOffset 291)*

No envelope comes, because no request went out. The file exists — it grows every week, in other people's handwriting — but your copy of it is the folder in your trunk: plan, visit notes, certificates.

Ms. Okafor does not scold you. “Then we work with what we have,” she says, “and we keep our own dates, carefully, because nobody will keep them for us.”

**Choices:**
- Start your own chronology from your folder and your phone → **prep1**  _(FLAG: chronologyKept; HIDDEN + Chronology started — from the folder and the phone calendar)_
  - NOTE (shown after choosing): Your dates, in your hand. It is a beginning, even without the file.

## [prep1] The One-Page Readiness Statement
*Day 298 — Friday, January 2, 2026 — Friday, January 2, 2026 (dayOffset 298)*

The January review is a week away. Ms. Okafor drafts with you at her office table: one page. Your name, Owen's name, the date. “Parent is ready to proceed. Parent has completed the following since the last review —” and a list, each item with its proof attached behind it.

“One page,” she says. “Filed before every date, whether the date holds or not. A continuance granted to a parent who was ready reads differently in a file than one granted to an empty chair. We are going to make sure the file never shows an empty chair.”

**Choices:**
- File it, with the certificates and the sign-in sheet attached → **kitchen_table**  _(cash −15; FLAG: readinessFiled; HIDDEN + Readiness statement #1 filed — ready, with proof attached)_
  - NOTE (shown after choosing): Copies, a bus ride, a stamped receipt. Fifteen dollars of ready.
- Plan to say it out loud at the hearing instead — paper feels like showing off → **kitchen_table**
  - NOTE (shown after choosing): Words said in a room stay in the room. Words filed stay in the file. Ms. Okafor lets you choose, and writes nothing down about it, which is its own sentence.

## [kitchen_table] The Night Before
*Day 302 — Tuesday, January 6, 2026 — Tuesday, January 6, 2026 (dayOffset 302)*

You lay out Owen's drawing of the foster family's dog, your work schedule, and the chronology — one page, nine months long — and you add today's line: “Readiness statement filed.”

Owen asked on Thursday's visit when the judge part happens. You told him soon, which was the truest available sentence. He accepted it the way children accept weather, and asked for a snack.

Tomorrow, the judge part happens. Or tomorrow, you find out what “happens” means in a system with this many calendars.

**Choices:**
- Sleep early. Be the ready one → **hearing1**
  - NOTE (shown after choosing): Your folder is by the door, where your work bag goes. Ready has a location now.

## [hearing1] The First Slide
*Day 305 — Friday, January 9, 2026 — Friday, January 9, 2026 (dayOffset 305)*

The courtroom smells like paper and radiator heat. Everyone is kind. Everyone is also, within twenty minutes, in agreement: the parenting instructor whose updated report the court was expecting has been called away on a family emergency, and her report is not filed.

The judge is apologetic and brisk. “We'll continue the review. Six weeks.” Papers shuffle. A new date is offered from a list, the way flights are offered at a counter after a cancellation.

Ms. Okafor stands. This is the practice, performed in plain words: “Parent was ready today, Your Honor — her statement is filed. We ask that the reason for the continuance and the new date be stated on the record.” The judge nods, and says them, slowly, for the record: witness unavailable; report not filed; new date, February 20.

**Choices:**
- Write it in the chronology in the hallway, before the elevator comes → **cont1**  _(FLAG: recordAsked; HIDDEN + Continuance #1 on the record — witness unavailable, report not filed; parent ready)_
  - NOTE (shown after choosing): Reason, new date, your readiness — all in the transcript now, not just in your memory.
- Go straight to your shift — you'll write it up tonight → **cont1**
  - NOTE (shown after choosing): Tonight becomes tomorrow becomes the weekend. The hallway had a bench. That was the moment.

## [cont1] Six Weeks Is Not Nothing
*Day 312 — Friday, January 16, 2026 — Friday, January 16, 2026 (dayOffset 312)*

Six weeks. You do the arithmetic the way parents in this system learn to do it: not in court time, in Owen time. Six Thursdays of visits. Six weeks of second grade. A loose tooth will come and go inside this continuance.

And against the other calendar: February 20 is still almost four months before June 10. There is time. That is what everyone says, and it is true, and it is also how time gets spent — in true sentences.

You keep working the plan. It is the only lever that has ever been fully yours.

**Choices:**
- Keep the Thursday visit exactly as it is — same time, same snack, same book → **visits1**
  - NOTE (shown after choosing): Continuity is a thing a child can hold. You hold the other end of it.

## [visits1] Thursdays
*Day 319 — Friday, January 23, 2026 — Friday, January 23, 2026 (dayOffset 319)*

The visit room has a couch the color of oatmeal and a bookshelf of donated puzzles. Owen is halfway through a chapter book about a dog who solves mysteries, and he reads you the good parts in his serious voice.

The visit supervisor writes her notes in the corner, kindly and constantly. You have stopped performing for the notebook. You just bring the snack, read the chapters, lose at the card game honestly.

On the bus home you update the chronology: visit, one hour, book chapters 9–11. It feels small. Small, dated, and true is what records are.

**Choices:**
- Finish the last parenting module this weekend — certificate before the next date → **service1**
  - NOTE (shown after choosing): One more line for the readiness statement. Proof first, adjectives later.

## [service1] The Certificate
*Day 326 — Friday, January 30, 2026 — Friday, January 30, 2026 (dayOffset 326)*

The last module is on a Saturday, in a church basement, with coffee that tastes like the urn. You pass the final exercise — a practice conversation with another parent playing a difficult caseworker — and the instructor signs your certificate with a flourish.

Every service goal on your plan is now complete except the one that was never a class: stable housing hours at the new apartment you moved into in November, which your landlord confirms in a one-line letter you request, in writing, the same day.

Your plan is done. What remains is a hearing at which to say so, in front of a judge, with the paper in the file. February 20.

**Choices:**
- Photograph the certificate for your phone, file the original → **letter_eli**
  - NOTE (shown after choosing): Original in the folder. Copy in the readiness packet. Photo in the phone. Paper, three deep.

## [letter_eli] Mail from the Foster Home
*Day 333 — Friday, February 6, 2026 — Friday, February 6, 2026 (dayOffset 333)*

The foster mother, Mrs. Hartley, includes a note with Thursday's returned lunchbox: Owen asked whether the judge “knows his name.” She told him judges read the folder first. He seemed satisfied, she writes, and asked if the folder has pictures.

It does now. You add the school concert program — Owen, third from the left, holding a recorder like a scepter — to the readiness packet, behind the certificates, where a person reading in order will reach it after the proof and before the end.

February 20 is two weeks away. You have never been more ready for anything.

**Choices:**
- File readiness statement number two — updated, with the certificate → **prep2**  _(cash −15; FLAG: readinessFiled; HIDDEN + Readiness statement #2 filed — all service goals complete, proof attached)_
  - NOTE (shown after choosing): Ready, again, in writing, before the date. That is the whole practice: again.

## [prep2] Readiness, Again
*Day 340 — Friday, February 13, 2026 — Friday, February 13, 2026 (dayOffset 340)*

Ms. Okafor reads the second statement and nods once. “Now the file shows a pattern,” she says. “Not a parent who was ready once. A parent who is ready every time, on paper, before anyone asks.”

She warns you about February anyway: the assessment summary the agency relies on has to be disclosed to your side in the adjudication-phase papers, and the agency's filing has been slow before. “If the paper isn't there,” she says, “the date may move again. If it does, we do the same things. Reason on the record. Chronology updated. Ready again.”

You hope she is wrong. You prepare as if she is not.

**Choices:**
- Go to February 20 ready to be heard — and ready to be continued → **hearing2**
  - NOTE (shown after choosing): Both folders packed: the hearing folder, and the hallway bench folder, with the chronology on top.

## [hearing2] The Second Slide
*Day 347 — Friday, February 20, 2026 — Friday, February 20, 2026 (dayOffset 347)*

The report is not filed. The agency's attorney is frank about it: the updated assessment summary — the disclosure your side is owed under Rule 1340(B)(1) — is still being prepared, and the caseworker who would explain it is reassigned.

And here is the flag Ms. Okafor taught you to carry into every room where that assessment is invoked: the assessment approach behind those ratings is untested. Its items produce numbers; the numbers' accuracy for families like yours has not been established the way its use in court assumes. A rating is a claim. Today, even the claim isn't in the room.

The judge continues the review to April 3. Ms. Okafor asks, again, in plain words: reason and new date on the record; parent's readiness noted. Granted, both. The transcript grows by a page. So does Owen's time in care: month eleven, becoming twelve.

**Choices:**
- File a short written objection before the next date — ready, again, in writing → **after2**  _(FLAG: objectionFiled; HIDDEN + Written objection filed — parent ready; reason and new date requested on the record)_
  - NOTE (shown after choosing): Not a rule. Not a threat. A dated page that says: I was ready, and the case moved anyway.
- Let this one slide without paper — objecting feels like making enemies → **after2**
  - NOTE (shown after choosing): The courtroom stays friendly. The file stays quieter. Both of those things are true, and only one of them is read later.

## [after2] What the File Shows Tonight
*Day 354 — Friday, February 27, 2026 — Friday, February 27, 2026 (dayOffset 354)*

At home you open the chronology. It is three pages now. Read quickly, it tells a story nobody intended: a case about a seven-year-old, in which every adult behaved reasonably, and in which the central event — a hearing — has not yet occurred.

March 10 will be one year since placement. Owen will have spent a seventh of his life in this. He is losing a tooth. He is learning fractions. The file's story and Owen's story are the same length, and only one of them is being lived at full speed.

April 3 is next. Then June 10 stops being a horizon and becomes a date.

**Choices:**
- Add tonight's line, and circle June 10 in your own color this time → **visits2**
  - NOTE (shown after choosing): Your color. Your calendar. The date was always yours too — Owen is yours.

## [visits2] The Loose Tooth
*Day 361 — Friday, March 6, 2026 — Friday, March 6, 2026 (dayOffset 361)*

The tooth comes out at Thursday's visit, into a tissue, with ceremony. Owen wants it noted “for the folder,” because he has absorbed, the way children do, the family's whole theory of the world: if it matters, it goes in the folder.

Mrs. Hartley photographs it for the tooth fairy's records. Everyone laughs. The supervisor writes something down, smiling, and for once you hope the note says exactly what happened.

Driving home, the arithmetic again: April 3 is the next date. After that, the calendar offers very little room before June.

**Choices:**
- Spend Saturday at the library printing the full chronology, clean → **payday**  _(cash −10; HIDDEN + Chronology printed clean — three pages, March 2025 to today)_
  - NOTE (shown after choosing): Ten dollars of copies. Three pages that took a year to write.

## [payday] The Cost of Ready
*Day 368 — Friday, March 13, 2026 — Friday, March 13, 2026 (dayOffset 368)*

Ready is not free. It is copies and bus fare and a shift swapped here, an hour unpaid there. You do the month's math at the kitchen table: the case has cost you, in small bills, about what a birthday party would. Owen's birthday is in May.

Ms. Okafor calls with two pieces of news. The April date is confirmed by the court — and the court's notice lists a courtroom. “Confirmed,” she says, “is a word this case has taught us to hold lightly. File the statement anyway.”

That is the practice, and by now it is also just your habit, like the folder by the door.

**Choices:**
- File readiness statement number three → **prep3**  _(cash −15; FLAG: readinessFiled; HIDDEN + Readiness statement #3 filed — ready for April 3)_
  - NOTE (shown after choosing): Ready, a third time, before the date. Patterns are what files believe.

## [prep3] Three Weeks Out
*Day 382 — Friday, March 27, 2026 — Friday, March 27, 2026 (dayOffset 382)*

Three weeks of ordinary life, lived at full speed on Owen's calendar and at filing speed on the case's. You work. He reads ahead in the dog book and refuses spoilers.

The evening before April 3, you iron the good blouse and lay out the folder. The chronology sits on top, three clean pages. Under it, three readiness statements, each stamped received. Under those, the certificates.

“Whatever happens tomorrow,” Ms. Okafor says by phone, “the file will show who was ready. That is not everything. It is not nothing, either. In this system, it is close to the main thing you control.”

**Choices:**
- Sleep early. Be the ready one, a third time → **hearing3**
  - NOTE (shown after choosing): Folder by the door. Alarm set. Owen's concert program still in the packet, third from the left.

## [hearing3] The Third Slide
*Day 389 — Friday, April 3, 2026 — Friday, April 3, 2026 (dayOffset 389)*

You wait all morning. Your case is called at noon, in a different courtroom than the notice said, because the listed courtroom was double-booked and a longer matter ran over. The bailiff is apologetic. The judge is apologetic. The calendar, examined closely, has no feelings at all.

There is no time left today to be heard. The review is continued — to May 15. Your unpaid morning is spent. Your good blouse is wilted. Ms. Okafor performs the practice without a flicker: reason — courtroom double-booked, matter ran over; parent ready, third statement filed; new date May 15, stated on the record.

In the hallway she says the quiet part: “May 15 is twenty-six days before June 10. Whatever May 15 is, it is the last date this case gets before the clock speaks.”

**Choices:**
- Submit the updated chronology to the court file before you leave the building → **strain**  _(FLAG: chronologyFiled; HIDDEN + Chronology submitted — every continuance, reason, and readiness statement, in order)_
  - NOTE (shown after choosing): The file now contains the case's true age, in your handwriting, where anyone deciding anything must step over it to decide.
- Keep the chronology for the hearing itself — whenever it comes → **strain**
  - NOTE (shown after choosing): It stays true in your folder. It just isn't in theirs, yet — and 'yet' is doing heavy work in this story.

## [strain] The Spring Squeeze
*Day 396 — Friday, April 10, 2026 — Friday, April 10, 2026 (dayOffset 396)*

April is the hardest month so far, and nothing in it is anyone's fault, which is somehow the hardest kind. Extra shifts appear and you take them, because ready costs money and so does May's birthday. A visit is shortened by a supervisor's double-booking — noted, kindly, in the chronology, with the make-up hour added the next week.

Your sister asks the question everyone asks: “How can a case about a kid move this slowly?” You have stopped trying to answer it in one sentence. The chronology answers it in three pages, without adjectives.

May 15 approaches. And with it, a notice about who will be asking for the date to move this time.

**Choices:**
- Read the notice twice, the way Ms. Okafor taught you: back page first → **notice4**
  - NOTE (shown after choosing): The back page is where letters like this keep their most important part. It works for notices too.

## [notice4] Counsel's Conflict
*Day 410 — Friday, April 24, 2026 — Friday, April 24, 2026 (dayOffset 410)*

The notice is from the agency's side this time: their attorney has a conflict on May 15 — a trial elsewhere, set long ago — and they will ask the court to continue the review again, into June.

Into June. The words sit on the page like a weather forecast. A June date would land on the far side of June 10 with the review still unheard: the fifteen-month point arriving while the case is mid-slide, the goal conversation changing in rooms you are not in.

Ms. Okafor is measured. “We can consent, or we can file our position before the date: parent is ready, parent objects to a continuance past June 10, parent asks that the reason and any new date be stated on the record. It is a page. It is not a guarantee. It is the practice, at the moment the practice matters most.”

**Choices:**
- Draft the page with her tonight → **folder_night**  _(FLAG: objectionFiled; HIDDEN + Objection to continuance past June 10 drafted with counsel)_
  - NOTE (shown after choosing): One page. Ready, objecting, asking for the record. The whole practice, at full size.
- Ask what consenting would look like — peace has value too → **folder_night**
  - NOTE (shown after choosing): It would look like a signature, and a June date, and a file that shows the parent agreed. That is also a kind of record.

## [folder_night] The Folder by the Door
*Day 417 — Friday, May 1, 2026 — Friday, May 1, 2026 (dayOffset 417)*

The night before the deadline to file your position, the folder is by the door, thick now: three readiness statements, the chronology, the certificates, the concert program. A year of being ready, in order.

You think about Owen at the Hartleys' table, doing fractions. You think about judges reading folders first — Mrs. Hartley's phrase, which has become the family's scripture: the folder is how the judge knows his name.

Tomorrow you decide what the folder says about May 15.

**Choices:**
- File the objection and the fourth readiness statement together → **prep4**  _(cash −15; FLAG: readinessFiled; FLAG: chronologyFiled; HIDDEN + Readiness statement #4 + objection filed — chronology attached)_
  - NOTE (shown after choosing): Ready, objecting, documented. If May 15 moves, it will move over your paper, in daylight.
- File the readiness statement, but hold the objection — stay agreeable → **prep4**  _(cash −15; FLAG: readinessFiled; HIDDEN + Readiness statement #4 filed — no objection)_
  - NOTE (shown after choosing): Ready, and silent about the slide. The file will show one of those things more clearly than the other.

## [prep4] May 15, Decided in Advance
*Day 424 — Friday, May 8, 2026 — Friday, May 8, 2026 (dayOffset 424)*

However the paper went in, the date arrives the way all the dates have: a courtroom, a bench, a morning of other people's cases moving at their own speeds toward their own children.

Ms. Okafor has one last piece of counsel, and it is about expectations, not law: “Courts continue cases for reasons. What we have built is not a wall against that. It is a record that makes the reason — and Owen's age in this — impossible to skip past. Watch what the judge does with it. That is the hearing inside the hearing.”

The case is called. The agency's attorney rises, conflict letter in hand, and asks for June.

**Choices:**
- The judge takes up the parent's filed position before she rules → **hearing4_obj**
  - NOTE (shown after choosing): “Counsel, the parent has filed a position.” The room's temperature changes by a degree. Paper, doing its work.
- The judge grants the June date — and the fight moves to what the record says before June 10 → **hearing4_slide**
  - NOTE (shown after choosing): The request is reasonable, the conflict is real, and reasonableness is how calendars move. What moves with it — your filed paper — is the remaining question.

## [hearing4_obj] Opposed, on the Record
*Day 431 — Friday, May 15, 2026 — Friday, May 15, 2026 (dayOffset 431)*

The judge reads your page in silence. Then she does the thing the practice was built to make possible: she states the whole picture out loud, for the record — the conflict, the request, the parent's readiness across four filed statements, the chronology, and the date nobody in the room says first: June 10.

“I will not continue this review past the fifteen-month date on a consent calendar,” she says. “The continuance is denied as requested. We will be heard on May 29 — a shortened list, this matter first — and the parent's chronology will be part of the record the court considers.”

One continuance, successfully opposed — not by a rule, but by a record that made the cost of granting it visible. The other slides still happened. May 29 is thirteen days before the clock. Both of those sentences are the story.

**Choices:**
- Go home and write May 15 in the chronology — the longest entry yet → **partial_review**  _(HIDDEN + Continuance opposed and denied as requested — hearing set May 29, before June 10)_
  - NOTE (shown after choosing): Reason stated. Objection noted. Date kept on your side of the line. In pen, this time.

## [hearing4_slide] Granted, Reasonably
*Day 431 — Friday, May 15, 2026 — Friday, May 15, 2026 (dayOffset 431)*

The request is granted the way all the others were: reasonably. A real conflict, a real trial elsewhere, a new date offered from the list — June 17 — accepted around the room with the small nods of people scheduling a dentist appointment.

Ms. Okafor asks for the reason and the new date on the record, and gets them, cleanly. She asks that your readiness and your filed position be noted, and they are. The transcript will show a parent who was ready, on paper, objecting — and a date that moved anyway. Objections, in this system, are weighed. They are not walls.

June 17. Seven days past the line. On the bus home, the arithmetic does itself: before June 17 comes June 10, and June 10 will not wait for the courtroom.

**Choices:**
- Spend the weeks before June 10 building the final packet anyway → **asfa_shadow**
  - NOTE (shown after choosing): Ready for a hearing whose meaning is about to change underneath it. Ready is still ready.
- Ask Ms. Okafor what June 10 changes, exactly, if the review is still unheard → **asfa_day**
  - NOTE (shown after choosing): “The conversation,” she says. “The agency will come to June 17 talking about goals, not just reviews. We will come talking about the record. Both matter. Ours is older.”

## [partial_review] May 29
*Day 445 — Friday, May 29, 2026 — Friday, May 29, 2026 (dayOffset 445)*

The shortened list is real: your matter is called first, in a quiet courtroom, with the judge's copy of your chronology already on the bench, its corners softened by reading.

There is time — not plenty, but enough — for the shape of the thing: services complete, housing stable, visits unmissed, and a case whose hearings slid for a year of stated reasons while its parent filed readiness like rent. The judge keeps the review open for written follow-up and sets the fuller hearing inside the summer, with dates stated, on the record, before anyone leaves.

Walking out, Ms. Okafor says: “One objection held. Three slides stand. That is not a victory parade. It is a record a court can act on — and it is yours.”

**Choices:**
- Go to Thursday's visit and tell Owen the judge knows his name → **end_partial**
  - NOTE (shown after choosing): She does. It is in the folder, third from the left, holding a recorder like a scepter.

## [asfa_shadow] The Conversation Changes
*Day 445 — Friday, May 29, 2026 — Friday, May 29, 2026 (dayOffset 445)*

The letter arrives in the last week of May, and it is not about a hearing. It is about a meeting: a permanency planning discussion, the agency writes, “in light of the upcoming fifteen-month date,” at which “all options, including goal change,” will be reviewed.

All options. You have learned to read this system's adjectives the way sailors read clouds. The review hearing — the one that was supposed to weigh your finished plan — is June 17. The clock's date is June 10. The clock will speak first, in a meeting room, unless the record speaks louder.

Ms. Okafor spreads the folder on her table. “Then we make sure the record is in the room, filed, before June 10 — chronology, statements, all of it. The clock gets a date. It does not get the only voice.”

**Choices:**
- File the full chronology packet — chronology, four statements, certificates — before June 10 → **final_prep**  _(FLAG: chronologyFiled; HIDDEN + Full packet filed before June 10 — chronology + readiness statements + proof)_
  - NOTE (shown after choosing): Filed, stamped, in the record before the date. Whatever June 10 becomes, it will not find an empty chair.
- Bring the folder to June 17 instead — filed paper feels finished, and you are not finished → **hearing_final_plain**
  - NOTE (shown after choosing): The folder stays in your trunk through June 10. True, complete — and, on the one date it mattered most, not in the room.

## [final_prep] Filed Before the Date
*Day 452 — Friday, June 5, 2026 — Friday, June 5, 2026 (dayOffset 452)*

The clerk stamps the packet on June 5. Chronology on top: three pages that have become five, every continuance with its reason, every readiness statement with its date, from a March morning in 2025 to a June morning in 2026.

June 10 comes and goes the way deadlines do — quietly, at full legal volume. The planning meeting happens with your record on the table, and the goal conversation happens around it, not instead of it. The agency's attorney uses a new phrase — “the exception question” — and Ms. Okafor, for the first time in fifteen months, smiles in a meeting.

June 17 is still on the calendar. For the first time, so are you — in writing, five pages deep, ahead of the date instead of behind it.

**Choices:**
- Walk into June 17 with the record already there → **hearing_final_record**
  - NOTE (shown after choosing): The judge has read the chronology. You can tell by the questions. They start in March 2025, not in June.

## [hearing_final_record] The Hearing, with the Whole Story in the Room
*Day 459 — Friday, June 12, 2026 — Friday, June 12, 2026 (dayOffset 459)*

The hearing, when it finally happens, is almost disappointingly ordinary: testimony, the plan, the certificates, the Hartleys kind and brief. What is not ordinary is the frame the judge puts around it, on the record, before the first witness:

“The court notes the parent's chronology, filed June 5, documenting four continuances across fifteen months, the stated reason for each, and the parent's filed readiness before every date. The court has considered the passage of time in this case — including the time attributable to continuances — as a fact in this record, and has weighed it.”

Delay, named as a fact, in the transcript, where facts live. Whatever follows from this hearing will be built on a record that shows the case's true age — and who was ready for all of it.

**Choices:**
- Hear the rest of your own hearing → **end_held_record**
  - NOTE (shown after choosing): You sit very still. Fifteen months of Thursdays, and the folder knew his name all along.

## [asfa_day] June 10
*Day 457 — Wednesday, June 10, 2026 — Wednesday, June 10, 2026 (dayOffset 457)*

June 10, 2026 arrives on a Wednesday, during your shift, between two other people's houses. Nothing happens. That is what the arrival of a legal date looks like from inside a life: nothing, at normal volume, with laundry.

The planning meeting that follows is polite and transformed. The agency speaks of the fifteen-month point as a door the case has now walked through; the goal conversation — adoption timelines, filing expectations, the exceptions and whether any fits — happens at a speed the review hearings never managed. Your folder is with you. Your chronology is accurate, complete — and unfiled, a private document at a public turning point.

June 17 is still coming. It will now be a hearing about where the case goes, held after the date that changed what the case is.

**Choices:**
- Go to June 17 anyway — late paper is still paper → **end_asfa**
  - NOTE (shown after choosing): You go. Ready, a fifth time, in a room where ready now means something different.

## [hearing_final_plain] The Hearing, on a Quiet File
*Day 459 — Friday, June 12, 2026 — Friday, June 12, 2026 (dayOffset 459)*

June 17 happens the way hearings do: testimony, the completed plan, the Hartleys kind and brief, a judge weighing what is in front of her with care. Your folder is on the table beside you — complete, accurate, yours.

What is not in front of her is any single page that adds the year up. The continuances sit in the docket as separate, reasonable entries. No chronology states the sum. Your readiness lives in three stamped statements, but nothing connects them into the pattern they made in your kitchen.

The hearing is fair to the file it has. The file it has is shorter than your year was.

**Choices:**
- Hear the rest of your own hearing → **end_held_silent**
  - NOTE (shown after choosing): Fifteen months of Thursdays, heard in an afternoon, on a record that shows almost none of the waiting.

## [end_held_record] Ending — Heard, with the Delay in the Record
*Day 466 — Friday, June 19, 2026 — Friday, June 19, 2026 (dayOffset 466)*

**Ending.**

**Debrief:**
- WHAT THE FILE HELD: Fifteen months, four continuances, four reasons — a witness's emergency, a report not filed, a double-booked courtroom, a counsel's conflict — each reasonable, together corrosive. What your choices changed was not whether the slides happened. It was whether they happened in the dark. The chronology you kept and filed, and the readiness you proved before every date, turned the case's true age into a fact the court stated on the record and weighed. The hearing was finally held on a record that included its own delay.
- THE LAW UNDER THIS PATH — AND ITS LIMITS: This scenario deliberately teaches no continuance rule, because none was verified for it: there is no simple deadline or limit on continuances stated anywhere in this game, and any source that handed you one should be doubted. What is real law here is the clock the delay ran against — at 15 of the most recent 22 months in care, a filing toward termination is generally expected unless an exception fits: the child is placed with a relative, a documented compelling reason exists, or the agency did not provide the services it identified as necessary (42 U.S.C. § 675(5)(E)) — and the record rights you used: your case record “shall be released upon request” (55 Pa. Code § 3130.44(d)), your right to counsel (42 Pa.C.S. § 6337), and the clear-and-convincing burden the agency carries in dependency. The readiness statement, the spoken request that reasons and new dates be stated on the record, and the filed chronology are practice, not entitlements — this ending shows practice working, not a rule firing.
- THE HONEST PART: A different judge could have read the same five pages and continued the case anyway; a fifth slide was always possible, and outcomes here turn on workers, judges, dockets, and luck as much as on paper. What the paper guaranteed was narrower and real: the delay could not be invisible, and your readiness could not be rewritten afterward as absence. In a system that decides from files, that is not a small thing. It is, on many days, the main thing a parent controls.

## [end_held_silent] Ending — Heard, on a Quiet File
*Day 466 — Friday, June 19, 2026 — Friday, June 19, 2026 (dayOffset 466)*

**Ending.**

**Debrief:**
- WHAT THE FILE HELD: The hearing was finally held — testimony taken, plan weighed, decisions made. What the file barely shows is how long it took to get there. Without a filed chronology, the case's fifteen months read as a smooth line: petition, plan, services, review. The four continuances exist as scattered docket entries, each with its reasonable face on, and no page anywhere adds them up. Delay happened to this family at full length. In the record, it is nearly invisible — and courts can only weigh what records show.
- THE LAW UNDER THIS PATH — AND ITS LIMITS: As in every path through this scenario, no continuance rule is taught or claimed — the readiness-and-record practice is a practice. The clock, however, is law: the 15-of-22-months point (42 U.S.C. § 675(5)(E)) arrived on June 10, 2026 regardless of the hearing calendar, with its three exceptions — relative placement, a documented compelling reason, and services identified but not provided. Your record rights were law too, whether or not they were used: release of your case record upon request (55 Pa. Code § 3130.44(d)) and counsel (42 Pa.C.S. § 6337). A hearing decides on the record in front of it; this ending is about what wasn't in front of it.
- THE HONEST PART: Nothing in this ending says the hearing itself was unfair, or that its outcome was wrong on the facts it heard. Workers were kind, reasons were real, and the judge weighed what the file contained. That is precisely the lesson: a true story that is never filed competes, in memory and in paper, against a shorter, smoother story that was. Workers, judges, and luck hold pieces of every outcome — but the file is the piece the parent holds, and this time it was held quietly.

## [end_asfa] Ending — The Date Arrived First
*Day 473 — Friday, June 26, 2026 — Friday, June 26, 2026 (dayOffset 473)*

**Ending.**

**Debrief:**
- WHAT THE FILE HELD: The fifteen-month date — June 10, 2026, fifteen calendar months after placement on March 10, 2025 — arrived while the review was still mid-slide, and the case's center of gravity moved: from 'is the parent ready?' to 'what should the goal now be?' That conversation happened first in a planning meeting, at planning-meeting speed, and the June 17 hearing inherited it. Your readiness was real, your plan was finished, your chronology was accurate — and the parts of that story that were never filed could not be weighed in the rooms where the goal conversation happened first.
- THE LAW UNDER THIS PATH: The clock is the law this scenario is built on: when a child has been in care for 15 of the most recent 22 months, a petition to terminate parental rights is generally to be filed unless an exception applies — (1) the child is being cared for by a relative, (2) a compelling reason, documented in the case plan, makes filing contrary to the child's best interests, or (3) the agency did not provide the services it identified as necessary for safe return (42 U.S.C. § 675(5)(E)). Note what the statute does not say: it does not pause for continued hearings. The exceptions are therefore where delayed cases are won or lost — and each exception is a documentation test, which is why the filed record, not the lived one, is the arena. Your other rights on this path were the same as always: your record on request (55 Pa. Code § 3130.44(d)), counsel (42 Pa.C.S. § 6337), and no invented continuance deadline anywhere — because there isn't one in this game.
- THE HONEST PART: The June 10 date is not a verdict, and this ending is not the end of the case — exceptions can still be documented, the hearing still held, the goal still contested, with workers, judges, and luck all holding pieces of what comes next. What changed is leverage and framing: after the date, the parent argues uphill, against a filing expectation, instead of across level ground. Time did that — not any person's villainy. Every continuance in this story had a reasonable face. The clock is the one participant that never has to explain itself.

## [end_partial] Ending — One Objection Held
*Day 466 — Friday, June 19, 2026 — Friday, June 19, 2026 (dayOffset 466)*

**Ending.**

**Debrief:**
- WHAT THE FILE HELD: A partial ending, and honestly labeled: of four continuances, three slid past exactly as scheduled — witness, report, courtroom — and the fourth, the one that would have carried the review past June 10, was opposed on the record and denied as requested. The hearing was pulled back to May 29, ahead of the fifteen-month date, with your chronology made part of the record the court considers. The delay was not undone. It was, once, at the moment it mattered most, refused — and the refusal is in the transcript, where refusals live.
- THE LAW UNDER THIS PATH — AND ITS LIMITS: The judge's ruling is depicted as discretion exercised on a record, not as a rule firing: this scenario verifies and teaches no continuance standard, no objection deadline, and no limit — the written objection and readiness statement are practice, performed in plain words, and a different judge could lawfully have granted the June date anyway. The hard law underneath remains the clock (42 U.S.C. § 675(5)(E): the 15-of-22 filing expectation and its three exceptions — relative placement, documented compelling reason, services identified but not provided), your record on request (55 Pa. Code § 3130.44(d)), and counsel (42 Pa.C.S. § 6337). May 29 mattered because June 10 was law. The objection mattered because May 29 was not guaranteed.
- THE HONEST PART: Partial is the honest shape of most wins in this system. Three slides still cost Owen three seasons of Thursdays; one held objection did not refund them. Workers granted, judges weighed, a courtroom's luck ran one way in May after running the other way all winter — and your paper was there for the one moment when the balance could tip. That is the whole claim this scenario makes for the practice: not that it stops time, but that it makes time visible, once, in the room where visibility counts.
