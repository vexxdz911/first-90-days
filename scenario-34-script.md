# THE FIRST 90 DAYS — Scenario 34: “The Missed Year”

*Human-readable script. This document and `scenario-34.json` are generated from a single source and match node-for-node: same IDs, same order, same choices, same effects.*

**The family is fictional — a composite. No real person's story appears here.**

**Content note:** This scenario depicts a dependency case across a year of caseworker turnover — a removal, services, visits, and a review hearing — told through procedure and paperwork. There is no graphic content. Players may skip any scene or use the quick exit at any time.

**How to read effects:** `cash −40` changes the player's cash. `FLAG: name` sets a flag the engine tracks. `HIDDEN + item` means the case file quietly records that item at this choice — the player does not see it when it happens. `NOTE:` is text shown to the player right after choosing.

Start date: Monday, March 2, 2026. Day offsets are days since the scenario's start date.

## [start] The Knock and the Bag
*Day 0 — Monday, March 2, 2026 — Monday, March 2, 2026 (dayOffset 0)*

You are Renee, a home-health aide, and Tobias's mother. Tobias is five. This winter your hours were cut, the landlord filed, and the arrangement that held your life together — a neighbor watching Tobias between your shift and your sister's — came apart one ordinary evening at a time.

Today the caseworker and a second person stand at your door with a court paper, and the paper says what the last month has been saying: the supervision arrangement is gone, the apartment is going, and no one can say, on paper, who is with Tobias while you work. A small bag is packed. Tobias asks whether his blue cup can go too. It can. It does.

No one in the hallway is cruel. That is worth saying at the start of this scenario, because everything that follows happens among people who are mostly not cruel — and happens anyway, in files.

**Choices:**
- Write down the names on the paper, and the time, before the door closes → **shelter_care**  _(FLAG: removed; HIDDEN + Removal — Monday, March 2, 2026; names and time recorded by parent)_
  - NOTE (shown after choosing): Your first entry. You do not know yet that it is the first entry in the only continuous record this case will have.

## [shelter_care] Seventy-Two Hours
*Day 3 — Thursday, March 5, 2026 — Thursday, March 5, 2026 (dayOffset 3)*

The shelter care hearing comes within seventy-two hours of Tobias being taken into custody, as the law requires (42 Pa.C.S. § 6332; 23 Pa.C.S. § 6315(d)) — Thursday, March 5, three days after Monday's hallway. A small courtroom. A judge. A file you have never seen, about a week you have just lived.

You have a lawyer. Counsel is your right, and appointed counsel is provided if you cannot afford one (42 Pa.C.S. § 6337). Yours is Mr. Whitfield, who has forty minutes of the case in his head and uses them well: Tobias stays in placement for now, with the Mensah family, and visits begin next week.

On the way out he says the sentence this scenario is built from: “Cases like yours are decided by records, Renee. Start one of your own. Today. Boring, dated, duplicated. Start today.”

**Choices:**
- Ask him what 'one of your own' means, exactly → **folder_begins**
  - NOTE (shown after choosing): “A folder. Everything they give you, everything you sign, every visit, every receipt. Copies of the copies. Boring will save you.”

## [folder_begins] A Folder of Your Own
*Day 7 — Monday, March 9, 2026 — Monday, March 9, 2026 (dayOffset 7)*

The folder costs less than lunch: a binder, dividers, a notebook with the dates already printed in the corners. You label the sections the way Mr. Whitfield said — COURT, SERVICES, VISITS, HOUSING, LETTERS — in the darkest marker the dollar store sells.

Your sister watches you do it. “You really think paper is going to matter more than the actual parenting?” she asks, not unkindly.

“I think paper is how they see the parenting,” you say, surprising yourself. “From their side of the desk, the folder is the parenting they can check.”

**Choices:**
- Make the first entry: the plan meeting, dated, with who said what → **worker_one_plan**
  - NOTE (shown after choosing): Four lines. It takes five minutes. It will still exist in a year, which is more than will be said for some things.

## [worker_one_plan] Worker One: The Plan
*Day 12 — Saturday, March 14, 2026 — Saturday, March 14, 2026 (dayOffset 12)*

Your first caseworker is Ms. Adeyemi, who is organized, warm, and carrying a caseload she mentions once, the way people mention weather in another county.

The family service plan has four lines that matter: complete a parenting program (ten sessions, Tuesdays); accept a referral to a housing navigator and work it; keep visits, twice a week; and rebuild a documented supervision plan for your work hours. Housing runs under all of it like a bass note: the navigator is supposed to be the bridge from your sister's couch to a lease.

“The navigator referral goes out this week,” Ms. Adeyemi says, and writes it in her notebook. You write it in yours. Two notebooks, one promise — remember that there were two.

**Choices:**
- Repeat the plan back to her before you leave, and write down her corrections → **sign_in_sheet**  _(HIDDEN + Plan — parenting program, housing navigator referral, visits, supervision plan; referral promised 'this week')_
  - NOTE (shown after choosing): She corrects one date and initials your notebook without being asked. A good first page.

## [sign_in_sheet] The Sign-In Sheet
*Day 20 — Sunday, March 22, 2026 — Sunday, March 22, 2026 (dayOffset 20)*

The parenting program meets in a room with a sign-in sheet by the door and coffee that improves as the weeks pass. Session one: you sign, and the facilitator, Ms. Lindt, dates the sheet herself.

At the break she says, to the room in general: “Keep your own count. Programs close, systems change, sheets get scanned crooked. The parents who do best in these rooms are the ones who could prove they were in them.”

You are already keeping your own count. What you have not yet decided is whether to keep proof, or just the count.

**Choices:**
- Ask at the end of every session for a dated copy or a stamp in your notebook → **receipts_habit**  _(FLAG: proofHabit; HIDDEN + Parenting program — parent collects dated proof at each session)_
  - NOTE (shown after choosing): Ms. Lindt stamps the notebook like a passport. Small ceremony, large consequences.
- Keep the count in your notebook — the program has the sheets; that should be enough → **receipts_habit**
  - NOTE (shown after choosing): It should be. Keep the sentence. This scenario is about sentences that begin 'it should be.'

## [receipts_habit] Receipts in Pencil
*Day 31 — Thursday, April 2, 2026 — Thursday, April 2, 2026 (dayOffset 31)*

Spring, in folder form: bus receipts in an envelope, a money order stub for the program's workbook fee, the visit center's printed confirmations, your work schedule with the new supervision arrangement penciled in — your sister's hours, initialled by her, because Mr. Whitfield said initialled paper is a different species from remembered paper.

None of it is impressive. All of it is dated. Your life, this spring, is a series of small rooms you were provably in.

**Choices:**
- Spend one evening a month copying the month's pages at the library → **visits_first_log**  _(cash −10)_
  - NOTE (shown after choosing): Copies at home, originals in the folder. Duplicated is a love language in this system.
- Skip the copying for now — the folder itself is the backup → **visits_first_log**
  - NOTE (shown after choosing): One folder. One copy of everything. Remember that you chose that.

## [visits_first_log] Visits, First Log
*Day 42 — Monday, April 13, 2026 — Monday, April 13, 2026 (dayOffset 42)*

Visits run twice a week at the center, and they are the best hours of the spring: Tobias's reading, out loud, mostly smooth; a card game you are losing on purpose less often than he thinks.

The visit center keeps a log, and so — because nobody told you to and Mr. Whitfield told you to — do you. Dates, times, who was at the desk. The two logs agree completely. Agreement between records is easy to maintain, you will learn, exactly as long as nothing changes.

**Choices:**
- Ask the desk for a copy of the center's log page each month → **notebook_habit**  _(HIDDEN + Visits — parent's log and center's log agree, spring; copies requested monthly)_
  - NOTE (shown after choosing): The desk clerk prints it without fuss. Paper is easy to give to people who ask calmly, with a folder.
- Trust the center's log — two logs for one visit is a lot of paper → **notebook_habit**
  - NOTE (shown after choosing): Your log continues anyway, in the notebook. Dates and desk names. It will turn out to be a kind of paper too.

## [notebook_habit] The Notebook Habit
*Day 55 — Sunday, April 26, 2026 — Sunday, April 26, 2026 (dayOffset 55)*

By early summer the notebook has a rhythm: date in the corner, names spelled as given, promises written the way they were spoken, including the wobbly ones. “Navigator referral this week” has been in it since March, initialled. Under it, in smaller writing, the follow-ups: asked in April — 'in process.' Asked in May — 'waiting on the list.'

The parenting program, meanwhile, is simply working: session follows session, stamp follows stamp, and Ms. Lindt has begun using your notebook as the room's example of the habit she preaches.

A file is growing in an office across town, too. It has the same spring in it. For now.

**Choices:**
- Finish the program → **certificate**
  - NOTE (shown after choosing): Endings, even small ones, should be signed in.

## [certificate] The Certificate
*Day 85 — Tuesday, May 26, 2026 — Tuesday, May 26, 2026 (dayOffset 85)*

Session ten. The certificate has your name spelled right and the program's seal, and Ms. Lindt signs the completion letter that goes with it: ten of ten, with the dates listed, because she lists dates the way other people list ingredients.

This letter is a door-closing document: one whole line of the plan, completed, under worker one, in a spring when the system and you were telling the same story.

What a completed line is worth depends entirely on whether anyone, later, can find it.

**Choices:**
- Put the original in the folder and copies in two other places → **supervisor_beat**  _(FLAG: certificateCopied; HIDDEN + Parenting program — completed 10 of 10 under worker one; certificate and completion letter copied and stored in three places)_
  - NOTE (shown after choosing): Folder, sister's house, a photograph on your phone. Completed, three times over.
- Put it in the folder — one careful place is enough → **supervisor_beat**  _(HIDDEN + Parenting program — completed 10 of 10 under worker one; certificate in the folder)_
  - NOTE (shown after choosing): One careful place. The folder rides the bus with you twice a week. Folders are mortal.

## [supervisor_beat] Asked in Writing
*Day 95 — Friday, June 5, 2026 — Friday, June 5, 2026 (dayOffset 95)*

The housing navigator referral is now three months old as a promise. 'In process' was April. 'Waiting on the list' was May. June's answer, from a covering worker on a day Ms. Adeyemi is at training, is: “Which referral?”

You show her your notebook — the initials, the dates. She is honest, and the honesty is its own information: the referral may have gone to a program that closed its list in spring. She cannot find a send confirmation. She will, she says, flag it.

Flags, you are learning, are where paper goes to be intended.

**Choices:**
- Write it up that night — the question, her answer, her name, the date → **handoff_one**  _(HIDDEN + Housing navigator referral — promised March, 'in process' April, 'waiting' May, no send confirmation found in June; all recorded by parent)_
  - NOTE (shown after choosing): Four lines in the notebook. The referral's whole biography, as it will turn out, exists only there.
- Leave it to the flag — she said she'd handle it → **handoff_one**
  - NOTE (shown after choosing): She meant it. Meaning it and it surviving the summer will turn out to be different countries.

## [handoff_one] Handoff One
*Day 122 — Thursday, July 2, 2026 — Thursday, July 2, 2026 (dayOffset 122)*

Ms. Adeyemi is leaving — a promotion, a going-away cake in an office kitchen, genuine good wishes. Your case transfers to a worker you will meet next week.

Transfers, in offices like this one, are a summary, a stack, and a deadline. What travels is what the summary says travels. Ms. Adeyemi offers you a handoff meeting to go through your folder against her file, line by line. It will take an unpaid afternoon. Unpaid afternoons are your scarcest currency this summer, scarcer than money.

**Choices:**
- Take the afternoon — go through the folder against the file, line by line → **worker_two**  _(cash −25; FLAG: handoffChecked; HIDDEN + Handoff one — parent and worker one reconciled folder and file line by line before transfer)_
  - NOTE (shown after choosing): Most lines match. The navigator line, in her file, reads 'referral pending.' You both look at it. She writes 'parent following up in writing' beside it, and initials it.
- Send her a one-page summary of where things stand instead → **worker_two**
  - NOTE (shown after choosing): She files it, she says later, on her last day. Last days are a busy country for filing.

## [worker_two] Worker Two: Starting Over
*Day 129 — Thursday, July 9, 2026 — Thursday, July 9, 2026 (dayOffset 129)*

Mr. Kowalski is brisk, new to the case, and reading from the transfer summary, which is shorter than the spring was. In the summary, your parenting program is “in progress.” Your visits are “regular.” Your housing is “unstable.” The navigator does not appear at all.

Summaries compress. Compression loses months the way a folded map loses towns.

He schedules your visits, re-explains the plan as if it were new, and asks you to re-sign two releases you signed in March. Starting over, you understand, is not his decision. It is the transfer's shape.

**Choices:**
- Show him the certificate copy and ask him to correct 'in progress' while you watch → **referral_lost**  _(HIDDEN + Handoff two — transfer summary described completed program as 'in progress'; parent flagged it at first meeting)_
  - NOTE (shown after choosing): He says he'll update it. The summary, corrected or not, has already been read by everyone who read it.
- Let it ride — you'll sort the details out as you go → **referral_lost**
  - NOTE (shown after choosing): Details, un-sorted, have a way of becoming the record. But it is a long summer and he is the second person to hold your spring.

## [referral_lost] The Referral That Was Never Re-Sent
*Day 138 — Saturday, July 18, 2026 — Saturday, July 18, 2026 (dayOffset 138)*

The housing question comes up in July, because housing always comes up, and Mr. Kowalski — checking, to his credit, while you sit there — finds no navigator referral in the transferred file at all. Not pending. Not closed. Absent.

His theory is reasonable, which makes it worse: referrals made by a departing worker are usually re-sent by the receiving worker; his transfer summary never mentioned one; so, in the system's own logic, there was nothing to re-send. The promise lived in two notebooks. One of them was yours. The other left with Ms. Adeyemi.

“I'll send it today,” he says, and does, in front of you. The new referral is dated July. The bridge the plan described in March begins, in the official story, in July. Four months of bridge exist only in a notebook with initials in it.

**Choices:**
- Ask for the send confirmation, dated, for your folder → **reprove**  _(HIDDEN + Housing navigator referral — re-sent July under worker two; send confirmation kept by parent; March promise documented only in parent's notebook)_
  - NOTE (shown after choosing): He prints it. August's date sits there honestly. Whether March's promise also exists, officially, is now a question about paper.
- Thank him and move on — at least it's sent now → **reprove**
  - NOTE (shown after choosing): It is sent. Forward motion is real. So is the shape a missing five months will give the story later.

## [reprove] Completed, Marked Incomplete
*Day 147 — Monday, July 27, 2026 — Monday, July 27, 2026 (dayOffset 147)*

The agency's next report reaches Mr. Whitfield's office before it reaches you, and he reads you the relevant line over the phone: parenting program — incomplete.

Completed in May. Marked incomplete in a report written in summer. Somewhere between a certificate, a transfer summary that said 'in progress,' and a report written from the summary, ten Tuesdays became a gap.

This is the beat the whole scenario has been walking toward: not an accusation, not a villain — a fact about you that is false, in a file, gaining the small authority that filed things gain.

**Choices:**
- Send the completion letter, with its dates, to the agency and the court — and keep the receipts → **visit_log_restarts**  _(cash −10; FLAG: completionReproved; HIDDEN + Parenting completion re-proved in writing — completion letter with dates sent to agency and court, receipts kept)_
  - NOTE (shown after choosing): Paper answers paper. The letter goes into the file next to the line it corrects, if files are fair. Files are fair when they are made to be.
- Correct it by phone — Mr. Kowalski knows the truth now, even if the report doesn't → **visit_log_restarts**
  - NOTE (shown after choosing): He does know. The report is what will be read in February by a person who has never met either of you.

## [visit_log_restarts] The Log That Restarts
*Day 160 — Sunday, August 9, 2026 — Sunday, August 9, 2026 (dayOffset 160)*

The visit center has a new system, a new desk clerk, and — you discover this month, asking for your monthly copy — a new log. The new log begins in August. The clerk is apologetic and precise: the old system's records were “migrated,” and what migrated, in your case, begins in August.

Your visits from March to August exist, as far as the center's paper is concerned, in your notebook: dates, times, who was at the desk, Tobias's reading level rising in the margins where you wrote it down because you were proud.

Two logs agreed all spring. Now there is one log, restarted, and a notebook.

**Choices:**
- Write up a one-page visit history from your notebook and file it with Mr. Whitfield now → **copy_shop**  _(FLAG: visitHistoryFiled; HIDDEN + Visits — center log restarts August; parent's contemporaneous notebook covers March onward; history filed with counsel in late summer)_
  - NOTE (shown after choosing): Filed in autumn, it is a record made from a record. Filed in February, it would be a claim. Timing is a kind of evidence too.
- Keep the notebook safe and say nothing yet — February is far away → **copy_shop**
  - NOTE (shown after choosing): February is exactly as far away as February always is, right up until it isn't.

## [copy_shop] Copies of the Copies
*Day 175 — Monday, August 24, 2026 — Monday, August 24, 2026 (dayOffset 175)*

An evening at the copy shop with the whole folder is the least dramatic scene in this scenario and, Mr. Whitfield will later say, possibly the most important one you play.

Page by page: certificate, completion letter, sign-in stamps, receipts, the referral pages, the notebook's summer. A second set, complete, for his office. Your set never has to travel together again. Loss, from here on, would have to happen twice to count.

**Choices:**
- Pay for the full duplicate set for your lawyer's office → **records_request**  _(cash −20; FLAG: folderDuplicated)_
  - NOTE (shown after choosing): Boring, dated, duplicated. The whole strategy, in a copy-shop bag.
- Copy only the certificate pages — the rest is in the folder → **records_request**
  - NOTE (shown after choosing): The folder is good. The folder is also singular. You have been taught the difference twice already this year.

## [records_request] Asking for the Whole File
*Day 185 — Thursday, September 3, 2026 — Thursday, September 3, 2026 (dayOffset 185)*

Mr. Whitfield raises the move the spring's leaflets described: separate from everything else, you may request your case record from the county agency, and it “shall be released upon request” (55 Pa. Code § 3130.44(d)). He is specific, as good lawyers are: the whole record, including the full assessment — the form itself, the item ratings, and the outcome — not only the summaries.

He adds the honest flag he always adds about the assessment: whether the adjudication-phase disclosure rule (Pa.R.J.C.P. 1340(B)(1)) reaches every scored item of an assessment form is untested. The direct record request does not depend on that question, which is why you are making it.

By now the request has a second purpose, and both of you know it: you are no longer only reading the file. You are auditing it, against a folder that has never changed hands.

**Choices:**
- Sign and send the request this week → **file_seams**  _(FLAG: recordsRequested)_
  - NOTE (shown after choosing): A stamp, a date, a copy for the folder. The audit begins.
- Wait until the new worker settles in — no need to look adversarial → **file_late**
  - NOTE (shown after choosing): Mr. Whitfield sends it anyway two weeks later, because 'adversarial' is a mood and the record is a fact, but the weeks will show in the dates.

## [file_seams] A File with Seams
*Day 200 — Friday, September 18, 2026 — Friday, September 18, 2026 (dayOffset 200)*

The returned record is thick, bound, official — and, read against your folder on your sister's kitchen table, visibly seamed. The assessment is there, form and ratings and outcome, plainer than you feared. The court orders are there. And then the seams: the visit record, continuous from August, thin before it. The parenting line, 'in progress,' long past May. The navigator, present from July, as if housing help had been invented in July.

It is not a false file. It is a restarted one — a year as remembered by a system that changed its memory twice. Your folder does not argue with it. Your folder simply continues through the months where it stops.

Three people's work is in that file. The only spring in it that was written by one person, start to finish, is yours.

**Choices:**
- Go through it with Mr. Whitfield, seam by seam, with your folder beside it → **folder_fills**  _(HIDDEN + Agency record returned — visit record thin before August, program long 'in progress,' navigator present only from July; seams identified against parent's folder)_
  - NOTE (shown after choosing): By the end of the appointment there are two stacks on his desk. Only one of them has no gaps in it.

## [file_late] A File with Seams, Later
*Day 200 — Friday, September 18, 2026 — Friday, September 18, 2026 (dayOffset 200)*

The record arrives two weeks further into the winter, and it is the same file its earlier twin would have been: official, bound, and seamed. Visits thin before August. The program 'in progress' past its own completion. The navigator born in July.

Late is not fatal. Late is just later — two fewer weeks to align your folder to its gaps before the review, and a lesson the notebook already taught you in March, at a kitchen table, for the price of a stamp.

**Choices:**
- Go through it with Mr. Whitfield, seam by seam, with your folder beside it → **folder_fills**  _(FLAG: recordsRequested; HIDDEN + Agency record returned late — same seams identified against parent's folder)_
  - NOTE (shown after choosing): Two stacks on his desk. Only one of them has no gaps in it.

## [folder_fills] Her Folder, His Months
*Day 207 — Friday, September 25, 2026 — Friday, September 25, 2026 (dayOffset 207)*

On the kitchen table, the two records interleave like two hands of the same deck. March: your notebook has the referral, initialled; the file has a promise. May: your folder has a certificate; the file has 'in progress.' July: both have the referral, finally sent. October: your notebook has visits; the file has a migration.

Nothing here required anyone to lie. That is the finding, and it is worse than a lie would be, because a lie can be caught. A seam just sits there, looking like a parent's empty spring, until somebody produces the spring.

You can produce the spring. Whether February believes paper produced by the person it is about is the whole remaining question.

**Choices:**
- Ask Mr. Whitfield to build February's filing out of exactly this — the seams, answered → **handoff_two**
  - NOTE (shown after choosing): “That's the filing,” he says. “Yours is not a better story. It's a continuous one. Continuity is the argument.”

## [handoff_two] Handoff Two
*Day 235 — Friday, October 23, 2026 — Friday, October 23, 2026 (dayOffset 235)*

In late October, Mr. Kowalski rotates to another unit. Worker three is coming. The year is about to change its memory again.

You know the shape of this day now. The question the day asks is only whether you will pay its price a second time, knowing what the first unpaid version cost.

**Choices:**
- Ask for a handoff meeting and reconcile the folder against the file again → **worker_three**  _(cash −25; FLAG: handoffChecked; HIDDEN + Handoff two — folder reconciled against file again before transfer; corrections noted in parent's hand)_
  - NOTE (shown after choosing): An afternoon's wages, a second time. Continuity, it turns out, has a price and you have decided it is a fair one.
- Send a summary and save the afternoon — you know how this goes now → **worker_three**
  - NOTE (shown after choosing): You do know how it goes. That is precisely what the afternoon was for.

## [worker_three] Worker Three: Another First Meeting
*Day 242 — Friday, October 30, 2026 — Friday, October 30, 2026 (dayOffset 242)*

Ms. Tran is careful, prepared, and working from a summary that has, by now, been summarized twice. In her summary, the year's shape is: a difficult spring, a program eventually completed, housing help engaged in July, visits steady since August.

She is the third person to hold your case, and the first to say the quiet part in a first meeting: “Tell me what the file gets wrong. Every file gets something wrong. I'd rather hear it now than read it in February.”

**Choices:**
- Tell her — calmly, with the folder: the spring the summaries keep losing → **plan_retyped**  _(HIDDEN + Worker three — briefed by parent, from the folder, at first meeting; seams named in December)_
  - NOTE (shown after choosing): She takes notes in a fresh notebook. You recognize the practice. You taught it to yourself in March.
- Keep it general — she's new; don't start by correcting her → **plan_retyped**
  - NOTE (shown after choosing): General is kind. February, however, is not a general kind of month.

## [plan_retyped] The Plan, Re-Typed
*Day 262 — Thursday, November 19, 2026 — Thursday, November 19, 2026 (dayOffset 262)*

The winter's updated plan arrives re-typed and mostly right, with one line carried faithfully forward by copy and paste through two summaries: parenting program — completed, it now says at last, but with the completion dated to the summer, when you re-proved it, instead of May, when you did it.

A small error, six months wide, sitting exactly where February's judge will look for how long the spring took you.

**Choices:**
- Ask, in writing, for the date to be corrected to May, with the completion letter attached → **visit_paper**  _(FLAG: dateCorrected; HIDDEN + Plan correction requested in writing — completion dated May, not summer, with letter attached)_
  - NOTE (shown after choosing): Dates are the load-bearing walls of this entire system. You straighten one.
- Leave the season wrong — completed is completed; don't fuss → **visit_paper**
  - NOTE (shown after choosing): 'Completed' is the big word. 'When' is merely the word February will ask about.

## [visit_paper] Sign Your Visits
*Day 280 — Monday, December 7, 2026 — Monday, December 7, 2026 (dayOffset 280)*

The last stretch of visits runs through the winter, and the new center log is reliable now, and stamps your arrivals without being asked.

Still, the habit is yours: you keep the notebook. Dates, desk names, Tobias's reading — by now he reads the card game's instructions aloud to you, in full, with expression, while you lose honestly.

February will ask about visits. Both logs, this time, will have an answer. What they cannot answer is the spring — for the spring, there is only one log left in the world, and it is in your handwriting.

**Choices:**
- Ask the desk to sign your notebook page at each visit, as well as logging it → **eli_question**  _(HIDDEN + Visits — winter visits doubly logged; spring visits covered only by parent's notebook)_
  - NOTE (shown after choosing): Desk signatures in your book. Two records again, agreeing — the way spring once was, rebuilt by hand.
- Rely on the center log now that it works → **eli_question**
  - NOTE (shown after choosing): It works. The spring, which it cannot see, remains where it always was: in the notebook.

## [eli_question] Is February a Holiday?
*Day 292 — Saturday, December 19, 2026 — Saturday, December 19, 2026 (dayOffset 292)*

Tobias asks whether February — the word the grown-ups keep using like a place — is a holiday, and whether he should make it a card.

You tell him the truth at his size: February is a meeting where people who have been helping decide what happens next, and your job at it is to bring the book of the whole year, and yes, a card would be a good idea for any month that has a meeting in it.

He makes the card that visit. It says FEBRUARY in letters of increasing size. You do not put it in the folder. Some things are not evidence. You write the date he made it in the notebook anyway, because by now the hand moves on its own.

**Choices:**
- Go home and spend the evening on the folder, not the feelings → **winter_visits**
  - NOTE (shown after choosing): Both, in truth. But the folder is the one February can hold.

## [winter_visits] Winter Visits, Steady
*Day 298 — Friday, December 25, 2026 — Friday, December 25, 2026 (dayOffset 298)*

The last visits before the review are steady in the way the plan once only hoped for: same days, same desk, a supervision plan that has held for months, a housing navigator — engaged at last, five months late in the official story — reporting real progress toward a lease you can almost touch.

Tobias's teacher sends a note through the visit bag, addressed to you: his reading is up; he tells the class his mom keeps 'the book of everything.'

Out of the mouths of five-year-olds: the book of everything. February is next.

**Choices:**
- Take the teacher's note for the folder, and go to the notice in the mail → **review_notice**
  - NOTE (shown after choosing): One more dated page. The folder is as ready as a year of evenings can make it.

## [review_notice] The Review Is Set
*Day 305 — Friday, January 1, 2027 — Friday, January 1, 2027 (dayOffset 305)*

The review is set for February — the month-twelve review, the year's examination. Ms. Tran gives you the agency's draft summary to read at home, which is new, and fair, and still: there it is. In the draft, your spring is a paragraph. A completed program, eventually. Help with housing, engaged. Visits, steady since August.

It is not the agency being unfair. It is the agency's record, summarized faithfully from a file with seams. Two histories of the same year now exist on paper, and February will be asked to choose between a summary and a folder.

Beyond February, Mr. Whitfield reminds you, the other clock still runs: Tobias was placed on March 2, 2026, and fifteen of the most recent twenty-two months arrives on June 2, 2027. February is not that hearing. But what February writes becomes what every later room reads.

**Choices:**
- Take the draft to Mr. Whitfield and lay it beside the folder → **folder_audit**
  - NOTE (shown after choosing): A paragraph, beside a year. The rest of the winter is for making February look at both.

## [folder_audit] Auditing Your Own Folder
*Day 318 — Thursday, January 14, 2027 — Thursday, January 14, 2027 (dayOffset 318)*

The audit is the least sentimental evening of the year: you and Mr. Whitfield, the folder open, a legal pad for what is missing.

What it holds: a completed spring, proved; visits, logged by you without a gap; referrals, promised and re-sent, both dated in your hand. What it holds less well depends on the year you actually played — a proof habit kept or skipped, copies made or trusted to one mortal folder, corrections filed or phoned in. The folder does not grade your love. It never could. It grades, precisely, your paper.

“February turns on whose paper survives contact with a judge,” he says. “Not whose year was harder. Yours was. That's not the question they'll ask.”

**Choices:**
- Decide, together, how the folder goes in → **hearing_eve**
  - NOTE (shown after choosing): Four ways remain. They lead to four different Februaries.

## [prep_choice] How the Folder Goes In
*Day 330 — Tuesday, January 26, 2027 — Tuesday, January 26, 2027 (dayOffset 330)*

Mr. Whitfield lays out the last choice of the year the way he laid out the first one: plainly, with prices attached.

File the whole folder early, indexed, every seam answered, so February is a discussion and not an ambush. File the services paper only, if that is the part your proof is strongest on, and let visits be argued. File the folder late, at the door, and trust its truth to outweigh its timing. Or take the reunification the agency's draft already half-offers, sign nothing, contest nothing — and let the official history stand as written.

“Choose like the person who has to live inside the file,” he says. “Because after February, the file is where the year lives.”

**Choices:**
- File the complete folder early, indexed, every seam answered → **review_prevails**  _(FLAG: folderFiled)_
  - NOTE (shown after choosing): Continuity, submitted on time, with page numbers.
- File the services paper — the certificate, the letters, the referrals — and argue visits from memory → **review_services_only**
  - NOTE (shown after choosing): Half the folder goes in like a wall. The other half goes in like a story.
- Bring the folder to the hearing and file it at the door → **review_partial**
  - NOTE (shown after choosing): True, complete, and un-read in advance. Judges read what they are given time to read.
- Take the half-offer: contest nothing, and let the draft stand → **review_divided**
  - NOTE (shown after choosing): Reunification first, history later. History, as you have learned, does not keep.

## [hearing_eve] The Folder, Read Whole
*Day 324 — Wednesday, January 20, 2027 — Wednesday, January 20, 2027 (dayOffset 324)*

The folder, a card that says FEBRUARY in letters of increasing size, a legal pad, and a pot of coffee. Mr. Whitfield's last instruction, weeks ago, was about the filing. Tonight's, by phone, is about sleep, and it is the only instruction of his you are going to half-disobey.

You read the year once, start to finish, in your own handwriting. It reads the way the year felt from inside it: slow, ordinary, stubborn. Whatever February decides about its paper, the paper itself is the one part of the year no transfer ever touched.

**Choices:**
- Close the folder, and decide how it goes in → **prep_choice**
  - NOTE (shown after choosing): Tomorrow the folder meets February. It is ready in the ways you made it ready.

## [review_prevails] The Review — The Continuous Record
*Day 347 — Friday, February 12, 2027 — Friday, February 12, 2027 (dayOffset 347)*

February. The agency presents its summary fairly: a difficult spring, a program completed, housing help engaged, visits steady. It is the file's year, told well.

Then the folder goes up — indexed, filed early, already read. The judge works through it in the order you lived it: the initialled referral promise from March beside its August re-sending; the completion letter's May dates beside summer's 'incomplete'; your notebook's unbroken visits beside a log that begins, apologetically, in autumn.

Ms. Tran, to her credit, confirms what her own file cannot: the seams are transfer seams, not parenting gaps. Three workers nod from three different chairs of the same year. The judge says the sentence the year was for: “The most reliable history of this case is the one that never changed hands.”

**Choices:**
- Listen to the order → **end_folder_prevails**
  - NOTE (shown after choosing): Substantially complete. A path home, with dates. And the record, this time, corrected to match the year.

## [review_partial] The Review — Filed at the Door
*Day 347 — Friday, February 12, 2027 — Friday, February 12, 2027 (dayOffset 347)*

February. The agency's summary goes first, and it is the only version the judge has had time to read in advance.

Your folder arrives at the door — true, complete, and heavy in the wrong way: a year of paper, unindexed, encountered for the first time in a hearing's short hour. The judge takes what an hour can hold. The certificate's May date lands. The referral's five missing months land, partly. The visits, spring's visits, remain a notebook being described rather than a record being read.

Nobody in the room disbelieves you. Disbelief was never the obstacle. Time, in a courtroom, is a form of evidence too, and you spent yours on truth instead of timing.

**Choices:**
- Listen to the order → **end_partly_credited**
  - NOTE (shown after choosing): Some of it lands. The rest is scheduled to be re-proved, a second year running.

## [review_services_only] The Review — Half a Wall
*Day 347 — Friday, February 12, 2027 — Friday, February 12, 2027 (dayOffset 347)*

February. Your services paper does its work completely: the certificate, the completion letter, the referral pages — the plan's service lines, credited, corrected, closed. The judge says so, in so many words.

Then visits. And here the room runs on the only visit record the agency can produce: a log that begins in August, and your spoken account of a spring of twice-weekly visits that no filed paper corroborates. You are believed, visibly, as a person. You are not credited, on paper, as a record — because belief and credit are different currencies, and February pays in the second one.

The judge's questions get shorter. The summary's version of the spring — visits beginning, for all official purposes, in autumn — survives, because nothing filed stood against it.

**Choices:**
- Listen to the order → **end_agency_summary**
  - NOTE (shown after choosing): Services: yours. Visits: the log's. A year, split down the middle by what was filed.

## [review_divided] The Review — The Order and the Archive
*Day 347 — Friday, February 12, 2027 — Friday, February 12, 2027 (dayOffset 347)*

February. The shortest hearing of the year. The agency's draft, uncontested, becomes the hearing's ground: a mother who completed her program eventually, engaged with housing help, steadied her visits by August — and who, on that described record, has done enough that the court orders reunification to proceed, on a plan, with dates.

You won the order. Tobias comes home on the order's schedule. Nobody in the room says an untrue word.

And the file closes over the year like water: eventually, engaged, by August. The spring you actually lived — the initialled promises, the ten Tuesdays, the visits that started in March — remains in one place only: a folder, in your home, that the official world will never open again.

**Choices:**
- Take the order home, and the folder with it → **end_divided**
  - NOTE (shown after choosing): Both are yours. They do not say the same thing. That is the ending.

## [end_folder_prevails] Ending — The Folder Prevails
*Day 354 — Friday, February 19, 2027 — Friday, February 19, 2027 (dayOffset 354)*

**Ending.**

**Debrief:**
- WHAT THE RECORD HELD (the hidden record, revealed): A year with no continuous author on the agency's side — three workers, two transfer summaries, a migrated visit log, a referral that existed for five months only as an initialled promise in a parent's notebook — set against one folder that never changed hands. The hearing did not hold that you were the better parent in some general sense. It held something narrower and more useful: where the two records conflicted, yours was contemporaneous, dated, duplicated, and filed in time to be read, and the agency's was a reconstruction. February credited the record that was written while the year was happening.
- THE LAW UNDER THIS PATH: The plan is now marked substantially complete and the reunification path reopens, on the court's order, with reviews continuing. The dates that frame the future are exact: Tobias was placed on March 2, 2026, and the federal fifteen-month date — 15 of the most recent 22 months — arrives June 2, 2027 (42 U.S.C. § 675(5)(E)), with its three exceptions (relative care; a documented compelling reason; services identified as necessary but not provided — a description your folder, unusually, could prove from the agency's own pages). February's corrected record is what any later room will read if that date ever matters. Your look at that record began with a request the regulation answers in five words — it 'shall be released upon request' (55 Pa. Code § 3130.44(d)) — and your counsel, who told you in March to start the folder, was your right from the first hearing (42 Pa.C.S. § 6337).
- THE HONEST PART: Paper prevailed this time partly because a judge read carefully, a third worker confirmed the seams aloud, and an agency lawyer presented a summary fairly instead of defending it past its evidence. Another courtroom, a busier morning, a supervisor who chose pride over accuracy, and the same folder is a parent's scrapbook against the state's bound file. Workers, judges, and luck are all in this ending. What your choices controlled was narrower and real: when the official memory failed — as, across three workers, it was always likely to — there existed a second memory, boring and dated and duplicated, that February could adopt as its own. You built the spare record in public, all year, for the price of evenings. It was enough. It is not guaranteed to be enough, and no honest debrief will promise that it is.

## [end_partly_credited] Ending — Partly Credited
*Day 354 — Friday, February 19, 2027 — Friday, February 19, 2027 (dayOffset 354)*

**Ending.**

**Debrief:**
- WHAT THE RECORD HELD (the hidden record, revealed): A complete and truthful folder that arrived too late to be read — the year's most common tragedy in miniature. The certificate's May date was credited; the referral's lost months were credited in part; the lost referrals are now re-made, properly, with confirmations. But a record credited in part, in an hour, leaves the rest of the year where summaries put it, and the clock consequences of the seams remain: reviews extend, the plan's completion is argued again from better paper, and time — Tobias's time, the only currency this system spends that cannot be refunded — has been spent on re-proving a spring that was proved once already.
- THE LAW UNDER THIS PATH: Nothing in this ending decides the case's end. The re-made referrals and corrected lines now sit in the record where later rooms will find them, and the framing date remains exact and ahead: placement on March 2, 2026 means 15 of the most recent 22 months arrives June 2, 2027 (42 U.S.C. § 675(5)(E)), with its exceptions — including, documented now in the file itself, services the plan identified as necessary that were not provided when promised. Your counsel's right to build that record with you (42 Pa.C.S. § 6337) and your right to the agency's record on request (55 Pa. Code § 3130.44(d)) are both still yours, and both now have a year of your own paper behind them.
- THE HONEST PART: Partly credited is what truth usually gets when it arrives at the door instead of in the mail: believed, in principle, and rationed, in practice. The same folder, filed a month early, plausibly ends this February differently — which is this scenario's coldest lesson, and not a moral one. You were not less truthful in this ending. You were later. Judges are people with an hour; workers are people with a summary; the system is people all the way down, which is why a record that hopes to survive it must arrive early enough for people to actually read. What remains yours is that the re-proving is now done, on the record, once — no third worker can un-send a confirmation that a court has read.

## [end_agency_summary] Ending — The Summary Prevails, in Part
*Day 354 — Friday, February 19, 2027 — Friday, February 19, 2027 (dayOffset 354)*

**Ending.**

**Debrief:**
- WHAT THE RECORD HELD (the hidden record, revealed): A split year, divided exactly along the line between what was filed and what was only true. The services you could prove on paper — certificate, completion letter, the referrals with their dates — were credited in full; the plan's service lines are corrected and closed. The visits you could only describe were not: a center log that begins in August, and a judge paying, as February pays, in filed paper, left the official spring visit-less. You documented the programs and not, in the end, the visits — and the file will remember the year in precisely that shape: a mother who completed services in a spring she apparently did not visit through.
- THE LAW UNDER THIS PATH: The case continues from this divided record, and the division is what later rooms will inherit. The framing date does not move: placed March 2, 2026, Tobias reaches 15 of the most recent 22 months on June 2, 2027 (42 U.S.C. § 675(5)(E)); if that date ever brings a filing question, its exceptions — relative care, a documented compelling reason, or necessary services not provided — will be argued from a record that now credits your services and understates your visits, which is a weaker hand than the year actually dealt you. The remedies that remain are the unglamorous ones this scenario teaches: file the notebook's visit history now, late but dated and contemporaneous in origin; keep requesting the record as it grows (55 Pa. Code § 3130.44(d)); and let counsel (42 Pa.C.S. § 6337) put every correction in writing, where corrections live.
- THE HONEST PART: It would be comforting to say the judge got the visits wrong. She did not, on the paper she was given — and that is the point this ending exists to make. Belief is not credit; a spoken spring, however true, weighs what spoken things weigh against a bound log with a start date in it. Workers changed, systems migrated, a clerk apologized — the luck and machinery in this outcome are real, and none of them required anyone's ill will. What was in your control was the difference between a notebook described and a notebook filed. Next time, file the notebook. That sentence, unkind as it sounds, is the most loving one this scenario owns.

## [end_divided] Ending — Reunified, Understated
*Day 354 — Friday, February 19, 2027 — Friday, February 19, 2027 (dayOffset 354)*

**Ending.**

**Debrief:**
- WHAT THE RECORD HELD (the hidden record, revealed): Two endings in one envelope. In the world: reunification, ordered, on a schedule — Tobias home, the plan closing behind him, a card that says FEBRUARY filed by its maker under 'art.' In the archive: a year that reads as eventual, engaged, by August — a spring of initialled promises, ten Tuesdays, and March visits that the official record will describe, forever, as if they had barely happened. The divided ending is not a loss. It is what winning looks like when the price of the order was leaving the summary uncorrected: the child comes home, and the history stays wrong.
- THE LAW UNDER THIS PATH: Legally, the order is the whole ballgame this February: reunification proceeds, and the case moves toward closing on its ordinary terms, with the federal date — June 2, 2027, fifteen months from the March 2, 2026 placement (42 U.S.C. § 675(5)(E)) — expected to pass with Tobias home, where it has nothing to operate on. But records outlive cases. If this family ever meets this system again, the first thing read will be this file, in this shape; the folder that contradicts it sits in a private home, aging, unaudited, one house-move away from legend. A parent's own record remains available to them on request (55 Pa. Code § 3130.44(d)) — including, should it ever matter, the corrected version February could have entered and didn't, because nobody asked it to.
- THE HONEST PART: Reasonable parents choose this ending every week, and this debrief will not call it a mistake: Tobias's homecoming is worth more than his mother's vindication, and she knew it, and she was right. The honesty is only about the price, which is real and permanent in one direction: systems remember what they wrote, not what happened, and the next worker, the next judge, the next February will meet the summary first and the truth, if at all, second. Workers, judges, and luck ran this year alongside you; the archive is simply the part of their work that never goes home. Keep the folder anyway. Paper kept by the person it is about has a way of being needed exactly once, years later, on a day nobody circled.
