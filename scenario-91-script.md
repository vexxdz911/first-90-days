# THE FIRST 90 DAYS — Scenario 91: “After the Order”

*Human-readable script. This document and `scenario-91.json` are generated from a single source and match node-for-node: same IDs, same order, same choices, same effects.*

**The family is fictional — a composite. No real person's story appears here.**

**Content note:** This scenario depicts a post-permanency winter: a teenager, a long-named permanency goal, and the hearing at which the goal is reconsidered. There is no graphic content. Players may skip any scene or use the quick exit at any time.

**How to read effects:** `cash −40` changes the player's cash. `FLAG: name` sets a flag the engine tracks. `HIDDEN + item` means the case file quietly records that item at this choice — the player does not see it when it happens. `REQUIRES FLAG: name` means the choice is only available if that flag was set earlier; `REQUIRES NO FLAG: name` means it is only available if that flag was never set. `NOTE:` is text shown to the player right after choosing.

Start date: Monday, January 11, 2027. Day offsets are days since the scenario's start date.

## [start] The Goal With the Long Name
*Day 0 — Monday, January 11, 2027 (dayOffset 0)*

Your name is Lucretia Moss. Your son Emory is fourteen, taller than you since October, and living in a foster home with a family he describes, in the tone teenagers reserve for weather reports, as 'fine.'

At the last permanency review, the court changed his goal. Not to adoption — Emory's age and Emory's stated wishes made that a poor fit — but to the longest phrase in the outcome list: another planned permanent living arrangement (42 Pa.C.S. § 6351(f.1)). In plain terms: the plan stopped being 'home' and became 'somewhere, planned, permanent, other.' The case did not close. Cases like Emory's rarely close; they continue, with reviews every six months (§ 6351(e)(3)(i)), at which the court must still make its determinations (§ 6351(f)) — including how much progress has been made toward alleviating the circumstances that brought him into care.

The next hearing is March 15. In January, 'APPLA' sounds like a destination. Emory, on the phone, has begun calling it 'the long name,' and asking what would have to be true for the plan to have a shorter one.

The family is fictional — a composite. The long name is real, and so is what it takes to shorten it.

**Choices:**
- Start answering Emory's question like it's a research project, not a hope → **clinic_call**
  - NOTE (shown after choosing): Because at a permanency hearing, it is one. The determinations are the rubric. The file is the exam.

## [clinic_call] The Clinic's Rubric
*Day 2 — Wednesday, January 13, 2027 (dayOffset 2)*

The parent-defense clinic attorney, Ms. Whitfield, does not deal in hopes either; she deals in the statute's list. "At the hearing, the court determines: is Emory safe and protected; is the placement still necessary; how is compliance with the plan; how much progress toward alleviating the original circumstances (§ 6351(f)(1), (2), (3)). Then it chooses the outcome (§ 6351(f.1)). APPLA is an outcome a court picks when the record gives it nothing better that fits a fourteen-year-old's life.

"So between now and March 15, our job is to make the record give it something better: your progress, documented; housing, documented; and Emory's own voice, in the file, where determinations get made. Courts hear children. Paper makes sure of it."

**Choices:**
- Ask for the first concrete step → **worker_meeting**
  - NOTE (shown after choosing): "Read your own file," she says. "All of it. You'd be amazed what the progress section says about a woman it hasn't updated since October."

## [worker_meeting] The New Worker's Questions
*Day 4 — Friday, January 15, 2027 (dayOffset 4)*

Emory's case has a new worker — the third — who meets you with a laptop and the particular honesty of a person reading a file she did not write. The file's summary of you is four months old and ends mid-sentence, in spirit if not in fact: 'Mother engaged but progress limited.' Since that sentence: you finished the first course, renewed the lease, and kept every dinner visit. None of it is in her laptop. All of it is in your folder.

**Choices:**
- Hand her a written update with the certificates attached, and keep the copy → **records** _(FLAG: updateFiled ; HIDDEN + Agency file — mother's written progress update filed, updating a four-month-old summary)_
  - NOTE (shown after choosing): She scans it into the file while you sit there. The summary of you is now partly written by you. That is not vanity; that is the record correcting itself.
- Tell her everything and trust the laptop to remember → **records**
  - NOTE (shown after choosing): Laptops remember what is typed into them. Conversations are typed, later, by other people, in summary, from memory. The story has views.

## [records] Reading Your Own File
*Day 6 — Sunday, January 17, 2027 (dayOffset 6)*

Ms. Whitfield's second step costs $10 and a signature: request the complete agency record, in writing. Agency records are released on request (55 Pa. Code § 3130.44(d)). For a post-permanency case the file is the case: two years of reviews, ratings, visit notes, and the plan documents that produced the long name. You cannot argue with a file you haven't read, and you cannot fix progress entries that nobody told you were wrong.

**Choices:**
- Sign the written request for the complete record → **emory_letter** _(cash −10 ; FLAG: recordsRequested ; HIDDEN + Record — complete agency file requested in writing in the post-permanency phase)_
  - NOTE (shown after choosing): The request is stamped and copied. When the file arrives it will be heavier than Emory was at birth, and you will read it at the kitchen table with a pencil, like an editor with a grievance and a deadline.
- Skip it — two years of paper won't change March → **emory_letter**
  - NOTE (shown after choosing): It might not. But the March hearing will be decided from inside that paper, and one side will have read all of it.

## [emory_letter] Emory's Letter, In His Own Hand
*Day 10 — Thursday, January 21, 2027 (dayOffset 10)*

Emory has written a letter. It is one page, in pencil, in the handwriting of a boy who types everything: he likes the foster family; he is not asking anyone to pretend otherwise; he wants the plan to include living with his mother again 'on a schedule that is written down,' starting with overnights, and he wants the court to know that this is his idea and he has 'thought about it since November.'

A fourteen-year-old's wishes are not a garnish in his own permanency case. They are evidence about what arrangement fits his life — but only if the letter reaches the file through the proper channels instead of living in your purse.

**Choices:**
- Help him send it through his lawyer and the case team, and file a copy with the court record → **school_counselor** _(FLAG: childVoice ; HIDDEN + Child's voice — Emory's own letter filed through counsel, in the record before the hearing)_
  - NOTE (shown after choosing): Filed. Whatever the court decides, it will decide it having heard from the person the long name is about.
- Keep the letter safe in your purse to show the judge if there's a chance → **school_counselor**
  - NOTE (shown after choosing): Purses do not testify. Letters in files do. The chance, if it comes, will come in a form that punishes the difference.

## [school_counselor] The Counselor Who Keeps Receipts
*Day 13 — Sunday, January 24, 2027 (dayOffset 13)*

Emory's school counselor has the other half of his year: grades recovered from the fall's crater, attendance near-perfect since January, the machine-shop elective where he is, she says, 'the kid other kids ask.' She will write it — counselors in this story write things when asked in writing, with a date, for a named hearing. March 15 gives her all three.

**Choices:**
- Ask her, in writing, for a letter for the March 15 hearing → **mentor** _(FLAG: schoolLetter ; HIDDEN + School — counselor's letter on grades, attendance, and stability obtained for the hearing)_
  - NOTE (shown after choosing): Signed, on letterhead, with the attendance numbers in a table. Judges read tables the way teenagers read texts: first, and completely.
- Mention it to the worker and let the system carry it → **mentor**
  - NOTE (shown after choosing): The system carries many things. Unrequested letters are not among its demonstrated skills.

## [mentor] The Mentor From the Machine Shop
*Day 16 — Wednesday, January 27, 2027 (dayOffset 16)*

The community mentor program paired Emory with a retired machinist who treats reliability as a moral category. His letter is two paragraphs and devastating in the way of plain men: Emory has missed one Saturday in five months, his own choice; the boy talks about his mother's dinners, her lease, her course certificates, 'like a kid reading a forecast he's decided to believe in.'

A mentor's letter proves nothing alone. In a file, beside a school letter and a teenager's own page, it becomes a chord.

**Choices:**
- Ask him to sign the letter and send a copy for the court file → **bus_talk** _(FLAG: mentorLetter ; HIDDEN + Mentor — signed letter on Emory's reliability and stated wishes added to the record)_
  - NOTE (shown after choosing): He signs it with a machinist's pencil, in block letters, and asks if courts prefer ink. 'Courts prefer filed,' you say, and he nods like that's a tolerance he respects.

## [bus_talk] The Bus Ride Inventory
*Day 20 — Sunday, January 31, 2027 (dayOffset 20)*

On the bus to the dinner visit, you inventory March 15 the way Ms. Whitfield taught you: determinations are made from the file. Yours now contains: your update, the complete record (read, with corrections penciled), Emory's letter, the school's table, the mentor's two paragraphs. The file's remaining thin places are equally listable: housing proof is a verbal assurance from your landlord, and the final parenting course — the teenagers one, the one that actually fits this case — ends March 1, unfiled until the certificate prints.

**Choices:**
- Treat the thin places as the next two errands, in order → **housing_proof**
  - NOTE (shown after choosing): Errands with deadlines. The story's love language, by now, in two counties.

## [housing_proof] The Lease, Renewed
*Day 22 — Tuesday, February 2, 2027 (dayOffset 22)*

Your landlord is a man who communicates in nods. The lease renewal is real — signed in December, through next December — but to a court, a nod is not a housing record. What the file needs is the renewal itself, copied, and a one-line letter: tenant, address, term, rent current. He signs it at the kitchen table of the duplex while his dog supervises, in the manner of landlords since the invention of leases.

**Choices:**
- Get the signed letter and a copy of the renewal into the packet → **services_done** _(FLAG: housingProof ; HIDDEN + Housing — signed landlord letter and lease renewal filed; rent current)_
  - NOTE (shown after choosing): Housing: documented. The file's second thin place is now a page with a signature instead of a hope with a nod.
- Tell the court the lease is renewed — he'll confirm if asked → **services_done**
  - NOTE (shown after choosing): Courts ask files, not landlords. A confirmation nobody requested, from a man of nods, is weather.

## [services_done] The Last Certificate
*Day 29 — Tuesday, February 9, 2027 (dayOffset 29)*

The parenting-teenagers course ends March 1: eight Saturdays of a curriculum that finally matches your actual child — curfews, phones, the negotiation of a household with a person who is nearly a man. The certificate costs $15 to print officially, which is absurd, and you pay it, because the certificate is the exhibit and the exhibit is the argument: progress toward alleviating the original circumstances (§ 6351(f)(3)), in the specific, unglamorous, completable form the plan demanded.

**Choices:**
- Pay for the official certificate and file it the day it prints → **folder_audit** _(cash −15 ; FLAG: servicesDone ; HIDDEN + Services — final course certificate filed; plan services complete)_
  - NOTE (shown after choosing): Filed March 2. The plan's service list is now, for the first time, a list of finished things.
- Bring the course workbook to the hearing instead → **folder_audit**
  - NOTE (shown after choosing): Workbooks show effort. Certificates show completion. Determinations, you have learned, are made about the second word.

## [folder_audit] The Folder Audit
*Day 33 — Saturday, February 13, 2027 (dayOffset 33)*

Ms. Whitfield audits the packet against the statute's list, one finger per determination. Safety: the file's own recent notes support it. Necessity: the contested one — your progress is the argument. Compliance: complete, with certificates. Progress: documented, dated, rising. The outcome menu: she taps § 6351(f.1) and says the sentence the whole winter was for: 'We are going to ask the court to change the outcome — stepped return, written into the order, with overnights starting in April.'

"Not because you're owed it," she says. "Because the record now supports it better than it supports the long name. That's the only currency this building accepts, and we've spent two months minting it."

**Choices:**
- Ask what could still go wrong, and write that list down too → **visit_dinner** _(FLAG: packetBuilt)_
  - NOTE (shown after choosing): The list is short and honest: a judge's caution, an agency's inertia, a teenager's bad week in the wrong week. All real. None of them paper-shaped. The paper is done.

## [visit_dinner] Dinner Visits, Logged
*Day 36 — Tuesday, February 16, 2027 (dayOffset 36)*

The dinner visits run twice a week now, at your table, with Emory's homework spread beside the plates and his phone face-down by house rule — his rule, announced in January like a treaty. The visit notes, kept by the agency, are kind and vague. Kind and vague, in a file, weighs about half of specific.

**Choices:**
- Ask, in writing, for the log to note the homework, the rule, and the on-time endings → **sister_call** _(FLAG: visitLog ; HIDDEN + Visit log — dinner visits documented specifically, in writing, at the parent's request)_
  - NOTE (shown after choosing): The note gets specific. Specific notes are the ones that get quoted in courtrooms. You have been quoted before; it cuts both ways; this time it cuts yours.

## [sister_call] Your Sister Asks the Odds
*Day 44 — Wednesday, February 24, 2027 (dayOffset 44)*

Your sister — Emory's aunt, his emergency contact, his second dinner table — asks the family question: what are the odds? You give her the clinic's answer, because by now it is yours too: 'The odds are a record. We built the best one the facts allowed. A judge reads it on March 15 and makes determinations. Nobody honest gives you a number.'

'Then we cook on the 15th either way,' she says. Family, in this system, is logistics plus casserole.

**Choices:**
- Tell her the hearing time and keep cooking → **letter_to_emory**
  - NOTE (shown after choosing): March 15, 10 a.m. She writes it on the recipe card. Some calendars are paper in the ways that count.

## [letter_to_emory] A Letter You Don't File
*Day 50 — Tuesday, March 2, 2027 (dayOffset 50)*

The night you write it, Emory is at the foster home, and the letter is not for a file: it is for a fourteen-year-old who asked a court, in pencil, for a written-down schedule with his mother. It says you are proud of the letter he wrote. It says whatever March 15 decides, the plan for his life includes you showing up, in writing and in person, at the volume he can verify. It says the long name never fooled either of you about what he is to you.

Some paper is evidence. Some is just true. A complete life, like a complete file, contains both kinds, kept in their proper folders.

**Choices:**
- Mail it in the morning and finish the hearing folder → **hearing_prep**
  - NOTE (shown after choosing): Mailed. The folder, by contrast, is all evidence — and it is finished.

## [hearing_prep] The Week Before the Hearing
*Day 55 — Sunday, March 7, 2027 (dayOffset 55)*

The packet is assembled in the statute's order, because hearings are read in the statute's order: safety, necessity, compliance, progress, outcome. Emory's letter is tabbed second, after your update, because Ms. Whitfield believes judges are readers and readers remember beginnings. Your testimony outline is three sentences long. Everything else you might say is already in the exhibits, with page numbers.

**Choices:**
- Sleep, and be at the courthouse early → **courthouse**
  - NOTE (shown after choosing): Early is a strategy in buildings where your name is called from a list by people holding files.

## [courthouse] The Hallway Bench
*Day 60 — Friday, March 12, 2027 (dayOffset 60)*

The hallway bench outside the courtroom is the system's true waiting room, and every family on it is holding a folder. Emory is there with his foster mother, who has brought his letter's twin — his school report card, 'for the file, whichever way it goes,' she says, with the grace of a woman who understands her exact role in a boy's life and performs it kindly. His lawyer nods at your packet's tabs with professional approval.

The clerk calls the case. The determinations are about to be made from a file. This time, you know what's in it, because you wrote half of it.

**Choices:**
- Go in and let the file be read → **hearing**
  - NOTE (shown after choosing): Two months of errands, one winter of paper. The reading takes twenty minutes.

## [hearing] The Six-Month Hearing
*Day 63 — Monday, March 15, 2027 (dayOffset 63)*

The judge works the statute's list aloud. Compliance: complete, certificates in evidence. Progress: documented and rising, school and mentor and the boy's own letter all in the file. The agency's position is read from its report — a report whose progress section was updated, in January, by the mother sitting at the table. The judge looks at Emory's letter for a long moment, and then at Emory.

What the court chooses from the outcome menu (42 Pa.C.S. § 6351(f.1)) now depends on what it was given to choose with.

**Choices:**
- Ask the court to change the outcome: reunification, stepped, with overnights written into the order → **out_goal** _(REQUIRES FLAG: servicesDone ; REQUIRES FLAG: childVoice)_
  - NOTE (shown after choosing): Your lawyer makes the ask in the statute's language, exhibit by exhibit. The file answers every question the bench asks. That sound — a record answering — is two months of errands, audible.
- Ask only for APPLA to continue with expanded visits and your role enlarged → **out_expanded**
  - NOTE (shown after choosing): A smaller ask, made from a record that could have carried a bigger one. Courts usually grant what is asked, and note what wasn't.
- Let the agency's report carry the hearing → **out_same**
  - NOTE (shown after choosing): Reports carry hearings the way rivers carry boats: in their own direction, at their own speed.

## [out_goal] The Outcome, Changed
*Day 63 — Monday, March 15, 2027 (dayOffset 63)*

The judge makes the determinations on the record: compliance complete; progress toward alleviating the original circumstances substantial and documented; the arrangement that fits this child's life is no longer the long name. The outcome under § 6351(f.1) is changed: the goal is reunification, on a stepped schedule written into the order — overnights beginning in April, expanding through the summer, with the next review set and the conditions listed one by one.

Emory reads the schedule over your shoulder in the hallway, at his full height, and says the most teenage sentence available: 'Okay. That's actually written down.' It is. That was the entire technology: written down.

**Choices:**
- Walk out with the order and its dates → **goal_order**
  - NOTE (shown after choosing): April overnights. Summer expansion. A review date. A shorter name for the plan, at last.

## [out_expanded] The Outcome, Enlarged
*Day 63 — Monday, March 15, 2027 (dayOffset 63)*

The court continues the long-named goal — and enlarges everything inside it: unsupervised dinner visits extended to full weekends monthly, Lucretia named in the plan as the placement's partner for school and medical decisions, a mentoring role formalized, the next review in six months with the progress determinations noted favorably on the record.

It is more than January promised and less than the record could have carried. The judge remarks, almost in passing, that the file showed a family mid-return; the ask, however, is what a court grants, and the ask was for enlargement.

**Choices:**
- Walk out with the enlarged order → **expanded_order**
  - NOTE (shown after choosing): Weekends, in writing. A door opened exactly as wide as it was asked to be.

## [out_same] The Outcome, Renewed
*Day 63 — Monday, March 15, 2027 (dayOffset 63)*

The hearing takes eleven minutes. The agency's report is adopted in its particulars; the determinations recite the plan's continuation; the goal with the long name is renewed for another six months, with the standard encouragement to continue progress. Emory's letter is in the file — someone mentions it — but an unargued file is a quiet one, and the court rules on what is presented to it.

In the hallway, Emory shrugs with the whole-body fluency of fourteen. 'Six more months of the long name,' he says. His foster mother drives him to school. The next review is in September (§ 6351(e)(3)(i)). The file, at least, is heavier now — if anyone chooses to argue from it.

**Choices:**
- Walk out with the September date circled → **same_order**
  - NOTE (shown after choosing): September. The file will keep. The question is whether the ask will change.

## [goal_order] The Order, At the Kitchen Table
*Day 66 — Thursday, March 18, 2027 (dayOffset 66)*

The order goes on the refrigerator under the April calendar, where Emory will see it at Easter with his own overnights listed in a judge's prose. Your sister reads it twice and puts the recipe card beside it. Determinations, made from a record, in a courtroom — and their natural habitat turns out to be a refrigerator door.

**Choices:**
- Start April → **end_goal**
  - NOTE (shown after choosing): April: two overnights. May: four. The schedule is written down. Emory checked.

## [expanded_order] The Order, At the Kitchen Table
*Day 66 — Thursday, March 18, 2027 (dayOffset 66)*

The enlarged order goes on the refrigerator: one weekend a month, decision rights named, the favorable determinations in black and white. It is a real improvement in Emory's actual life — more mother, more say, more record — filed under a goal whose name still doesn't say 'home.' Both of those things are true, and the refrigerator, like the file, holds them without flinching.

**Choices:**
- Start the first weekend → **end_expanded**
  - NOTE (shown after choosing): A weekend, in writing. The next review's record starts accumulating tonight.

## [same_order] The Order, At the Kitchen Table
*Day 70 — Monday, March 22, 2027 (dayOffset 70)*

The renewed order goes in the folder, behind January's. Nothing in Emory's week changes. What changed, invisibly, is the file: it now contains a teenager's letter, a school table, a mentor's paragraphs, a landlord's signature, a final certificate — an argument, assembled and unmade before a court. Files keep. The next hearing's outcome will be chosen from this file plus whatever the spring adds.

**Choices:**
- Start September's file tonight → **end_same**
  - NOTE (shown after choosing): September is six months of errands away. You know the route now. Knowing it was most of the cost.

## [end_goal] Ending — The Goal Moves Back: Reunification, With Dates
*Day 70 — Monday, March 22, 2027 (dayOffset 70)*

Emory's plan has a shorter name. Overnights begin in April under an order a judge signed, with the conditions listed and the review date set — not a promise, not a hope, a schedule. He will still be, for a while, a child with two addresses. But the arrangement the system now plans for is the one he asked for in pencil: home, stepped, written down.

Lucretia keeps the folder. The determinations that changed the goal were made from it — her update, her certificates, her landlord's signature, his letter. Post-permanency turned out not to be after anything. It was the same work, at a longer wavelength: the record, argued from, on time.

**ENDING — Debrief:**

THE WIN, NAMED HONESTLY — A partial win, and the best this scenario offers: the (f.1) outcome changed from another planned permanent living arrangement back to reunification on a stepped schedule. Emory is not home tonight, the case is not closed, and conditions attach. What changed is the plan's direction and its dates — which, in a permanency case, is the substance judges actually control.

THE LAW IN THE BEATS — Permanency hearings recur within six months (42 Pa.C.S. § 6351(e)(3)(i)) and must make the determinations in § 6351(f) — including (f)(2) compliance and (f)(3) progress toward alleviating the original circumstances — before choosing an outcome from § 6351(f.1)'s menu. A goal once changed can be changed again on a later record; the menu is chosen from each time, on the file then before the court. The complete-record work rests on 55 Pa. Code § 3130.44(d).

THE HIGHEST-LEVERAGE MOVE — The written record request in January (§ 3130.44(d)): it exposed the four-month-old summary, which made the update necessary, which made the determinations arguable. Post-permanency cases are won in the file's present tense.

WHAT NO STRATEGY CONTROLS — The judge's caution, the agency's inertia, a teenager's spring. The route controlled the record and the ask. Note what decided this ending: both. A record without an ask is the third ending; an ask without a record is a speech. The system, at its best-functioning, grants documented requests.


## [end_expanded] Ending — APPLA, With Her Name Back In It
*Day 70 — Monday, March 22, 2027 (dayOffset 70)*

The long name stays, and nearly everything inside it improved: weekends, decisions, a formal role, favorable determinations on the record that the next review will start from. Emory's life got measurably more mother in it, and his file got measurably more honest.

What it did not get was the change of direction — because the change was never asked for. Courts in this system grant requests; they rarely upgrade them. The record Lucretia built could have carried the bigger ask, which is precisely what makes this ending a middle one: the loss is located in a single sentence that was not said in a courtroom, on a day when everything needed to support it was already in the room.

**ENDING — Debrief:**

THE WIN, NAMED HONESTLY — A partial outcome below the best: real gains, honestly labeled. The (f) determinations were favorable and are now precedent inside this case; the (f.1) outcome is unchanged. If Lucretia asks in September with this record plus a spring of kept weekends, she asks from strength — the scenario's consolation, and its lesson, are the same fact.

THE LAW IN THE BEATS — Same § 6351 frame: (e)(3)(i)'s six-month rhythm, (f)'s determinations, (f.1)'s menu, and the practical rule this batch teaches alongside the statute — the outcome chosen is chosen from the requests actually made, on the record actually built. The record request remains 55 Pa. Code § 3130.44(d).

WHAT NO STRATEGY CONTROLS — Nothing external decided this ending. That is its discomfort and its use: sometimes the binding constraint is not the worker, the judge, or the clock, but the size of the request a parent believes she is allowed to make. The file said otherwise. Files, unlike fears, can be checked.


## [end_same] Ending — The Long Name, Renewed
*Day 77 — Monday, March 29, 2027 (dayOffset 77)*

Another six months under the longest phrase in the outcome list. Emory's life continues: school, the machine shop, dinners on Tuesdays and Thursdays, a foster family that is kind, a mother who is present and documented and — in the only forum where it had to be argued — unheard, because the argument was never made out loud.

Nothing was decided against Lucretia in this ending, which is the bleakest thing about it. The hearing ran on the agency's paper because hers, though built, was never presented. The determinations were made from a file whose best pages sat in a folder on a hallway bench.

**ENDING — Debrief:**

WHY THIS ENDING — Permanency outcomes are chosen at hearings, from presented records and stated requests (42 Pa.C.S. § 6351(f), (f.1)). An unargued record does not argue itself. The scenario's January–March work — the § 3130.44(d) request, the update, the letters, the certificates — remains in the file and remains usable in September; what was spent was six months of a fourteen-year-old's life, which is the one currency this system never refunds.

WHAT NO STRATEGY CONTROLS — The judge cannot be faulted in this ending for failing to grant what was not requested; the agency cannot be faulted for its report carrying an unopposed hearing. The lesson is structural, not moral: in this forum, presence is not participation. The file must be argued from, by name, exhibit by exhibit, in the room, on the day.

