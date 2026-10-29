# THE FIRST 90 DAYS — Scenario 113: “The Unit That Needed a Date”

*Human-readable script. This document and `scenario-113.json` are generated from a single source and match node-for-node: same IDs, same order, same choices, same effects.*

**The family is fictional — a composite. No real person's story appears here.**

**Content note:** This scenario depicts a mother in month 13 of her son's foster-care placement whose last open plan goal is housing, told through applications, a housing program's letter, a case record, and a permanency review ahead of the federal 15-of-22-months filing date. There is no graphic content. Players may skip any scene or use the quick exit at any time.

**How to read effects:** `cash −40` changes the player's cash. `FLAG: name` sets a flag the engine tracks. `HIDDEN + item` means the case file quietly records that item at this choice — the player does not see it when it happens. `REQUIRES FLAG: name` means the choice is only available if that flag was set earlier; `REQUIRES NO FLAG: name` means it is only available if that flag was never set. `NOTE:` is text shown to the player right after choosing.

Start date: Friday, April 3, 2026. Day offsets are days since the scenario's start date. Tier: Complex.

## [start] Month Thirteen, One Goal Left
*Day 0 — Friday, April 3, 2026 — Friday, April 3, 2026 (dayOffset 0)*

Your name is Farida. Your son Umar is ten, and he has been in foster care since Monday, March 3, 2025 — thirteen months of a childhood, measured by the system in reviews and by you in school terms. This morning the case has a shape it has never had before: of every goal on your plan, exactly one is still open.

Treatment: completed, certificate filed. Parenting program: completed. Employment: steady, pay stubs in the folder. Visits: kept, expanded, warm — Umar beats you at chess now and explains, each time, exactly how. The open goal is the one printed in the same bold type as all the others: HOUSING. You live in a single room whose lease does not permit a child to live in it. Everyone agrees you have done the work. Agreement has not yet produced an apartment.

Somewhere in the case there is a date the calendar is walking toward, and this month — month thirteen — your lawyer has asked to meet about it. Not because anything went wrong, she said. Because of what is about to be true.

**Choices:**
- Go to the meeting — and bring the folder, as always → **folder_audit113**
  - NOTE (shown after choosing): The folder holds the whole case in your handwriting: certificates in front, housing at the back, where the unfinished things live.

## [folder_audit113] The Folder, Audited
*Day 2 — Sunday, April 5, 2026 — Sunday, April 5, 2026 (dayOffset 2)*

Before the meeting, the folder gets its audit on the kitchen table — the small table, in the single room, that has served as desk, office, and evidence locker for thirteen months. Front section: every completion the plan ever asked for, dated. Back section: housing, and housing is a different kind of thick — applications, waitlist letters, stamped receipts, a year of paper proving effort against a list.

What the audit shows is the case in one image: your side is finished, and the unfinished side is not a task. It is a queue. Queues do not respond to effort. They respond, if they respond at all, to paper arriving in the right order.

Your lawyer, Ms. Adler, keeps a calendar with one date circled in pencil. Today she is going to tell you whose date it is.

**Choices:**
- Take the audited folder to Ms. Adler's office → **housing_office**
  - NOTE (shown after choosing): First, the housing office — the letter she asked you to collect on the way, with your position on it, dated.

## [housing_office] Position, Stamped
*Day 4 — Tuesday, April 7, 2026 — Tuesday, April 7, 2026 (dayOffset 4)*

The housing office waiting room has the chairs and the ticket machine that waiting rooms for lists always have. The clerk is not the enemy; she is the list's receptionist, and she has been yelled at by people who were told a month, so she does not tell months.

What she will do — what clerks of lists will reliably do for people who ask calmly, with a folder — is print the page: your name, your applications, their dates, your position, today's date stamped by the machine that stamps it. A position on a list is either a rumor or a fact, depending entirely on whether it is printed.

You take the printout for the folder, and one more piece of mail that has been waiting in your box at the residence: an envelope from the housing program itself.

**Choices:**
- Open the program's envelope at the table before you leave → **program_letter**  _(cash −4)_
  - NOTE (shown after choosing): Four dollars of bus fare for the trip. The envelope is thin, official, and — unusually for this case — about to be specific.

## [program_letter] The Letter With a Condition in It
*Day 6 — Thursday, April 9, 2026 — Thursday, April 9, 2026 (dayOffset 6)*

The program's letter is one page, and it says what it says on its face, in the plain language of programs: your application is complete and you are approved in principle for a family unit through the program — and the unit can be approved for occupancy once a return date for Umar exists, within sixty days of the approval, so that the unit and the child's return can be scheduled together. A return date, the letter says, is what the program needs from the court.

Read it again, because the whole scenario lives in this paragraph: the housing is not waiting for your effort, your income, or your position alone. It is waiting for a date — a date that only a court, on the agency's recommendation, can set.

You have been in this case thirteen months. This is the first time the barrier has been stated, in writing, as a thing the system itself is holding.

**Choices:**
- Decide what to do with a letter like this: keep the original safe, or carry it loose → **letter_after**
  - NOTE (shown after choosing): Letters that state systems' conditions in systems' own words are exhibits in waiting. They should be treated like glass.

## [letter_after] Glass, Filed
*Day 8 — Saturday, April 11, 2026 — Saturday, April 11, 2026 (dayOffset 8)*

The original goes in the folder's front pocket — the pocket for documents that would be hard to replace — and a copy goes behind it, because originals in this system travel and copies are how travel is survived.

You sit with the letter's arithmetic a moment, because arithmetic is about to matter: the program needs a return date within sixty days. The agency, at your last meeting, said — in words you wrote down in the car — that no return date can be set until housing is secured. Housing is secured when the program approves the unit. The program approves the unit when a return date exists.

A circle, drawn in two offices' handwriting, with your son in the middle of it. Circles in this system are not broken by effort. They are broken, if at all, by documents that make a room choose which half of the circle to act on first.

**Choices:**
- Get a dated copy made for Ms. Adler, and go to the agency meeting first → **agency_meeting**  _(cash −3; FLAG: programLetter; HIDDEN + Housing program letter — unit approvable once a return date within sixty days exists; dated copy obtained)_
  - NOTE (shown after choosing): Three dollars of copies. The letter now exists in two places, which in this system is the beginning of existing at all.
- Carry the original loose — Ms. Adler can read it at the meeting → **agency_meeting**
  - NOTE (shown after choosing): She can, and she will. What she cannot do, later, is cite a copy that was never made, from a letter that lives in a coat pocket.

## [agency_meeting] No Date Until Housing
*Day 10 — Monday, April 13, 2026 — Monday, April 13, 2026 (dayOffset 10)*

The agency meeting is courteous and short. Your worker, Ms. Beam, reports your progress the way the file reports it: everything complete but housing. You show her the program's letter. She reads it with the attention of a person reading her own side of a correspondence she did not know was one.

“The program needs a return date,” she says. “I understand that. But we can't recommend a return date until the housing is in place. That's the sequence. Housing first, then the date.”

You say, as gently as the sentence allows: the program's sequence is the other one. She does not disagree. She says she will note it in the file — and there, in miniature, is the whole case: a circle, noted, in a file, by two people who both see it and neither of whom, alone, can break it. Noting is not breaking. But a noted circle is at least a circle on paper, and paper is where breaking happens.

**Choices:**
- Ask her to note the letter itself in the file — not just the conversation → **counsel_meet113**  _(HIDDEN + Agency meeting — program letter shown; agency position restated: no return date until housing is secured)_
  - NOTE (shown after choosing): She writes the note while you watch. Whether it quotes the letter or summarizes it is a distinction this scenario has opinions about.

## [counsel_meet113] Two Circles and a Date
*Day 12 — Wednesday, April 15, 2026 — Wednesday, April 15, 2026 (dayOffset 12)*

Ms. Adler is your lawyer in this case, as the law provides for a parent (42 Pa.C.S. § 6337). She reads the program's letter twice, puts it down, and turns her desk calendar around: the circled date is Wednesday, June 3, 2026.

“Umar was placed on Monday, March 3, 2025. At fifteen of the most recent twenty-two months, the agency is generally to file a petition to terminate parental rights — unless an exception is documented (42 U.S.C. § 675(5)(E)). Fifteen months from his placement is Wednesday, June 3, 2026 — Wednesday, June 3, 2026, sixty-one days from the morning this chapter opened. That is the first circle's deadline: the housing circle has to be answered before the calendar answers it for us.”

“Generally is doing real work in that sentence,” she says. “There are three documented doors in it, and two of them may be standing open in your file already. Sit down. We are going to read what the file actually says — all of it, including the parts about what the agency was supposed to do about housing.”

**Choices:**
- Sit down, and ask her to say the exceptions slowly → **records_beat113**  _(HIDDEN + Counsel meeting — ASFA date Wednesday, June 3, 2026 named; housing circle and exceptions explained)_
  - NOTE (shown after choosing): She writes three numbered lines on a legal pad before she says another word.

## [records_beat113] Asking for the File
*Day 15 — Saturday, April 18, 2026 — Saturday, April 18, 2026 (dayOffset 15)*

“At fifteen months, the agency is generally to file — unless an exception is documented: the child is being cared for by a relative; or there is a documented compelling reason that filing would not serve the child; or the agency has not provided the services it identified as necessary for the child's safe return (42 U.S.C. § 675(5)(E)). Now hear the discipline of it: the exceptions are record-dependent. They exist as arguments only to the extent the case file documents them. So our first job is not arguing. It is reading the file the decision will be made from.”

There is a right that does not depend on any hearing: a parent may request the case record from the county agency, and under the regulation the material “shall be released upon request” (55 Pa. Code § 3130.44(d)). Ms. Adler drafts the request while you watch — the full record, the service plan, and everything the file holds about housing assistance.

**Choices:**
- Sign the written request for the complete record this week → **file_review113**  _(cash −6; FLAG: recordsRequested; HIDDEN + Case record requested in writing under 55 Pa. Code § 3130.44(d))_
  - NOTE (shown after choosing): Signed, dated, copied. The request itself is now a page in the file it asks about.
- Wait until after the next review — the circle is the urgent thing → **summary_only113**
  - NOTE (shown after choosing): Understandable, and the circle is urgent. The exception, though, lives or dies in the file the circle is drawn in — unread files keep their secrets in both directions.

## [file_review113] Reading for What Isn't There
*Day 18 — Tuesday, April 21, 2026 — Tuesday, April 21, 2026 (dayOffset 18)*

The record arrives: thick, partly blacked out, and readable. You and Ms. Adler read it the way she taught you — for the housing-assistance service specifically, because the plan identified housing assistance as a service necessary for Umar's safe return, and the third exception is about exactly that: what was identified, and what was actually provided.

The plan's housing page is thorough about you: applications to be made, documentation to be kept, lists to be joined — and your compliance is noted, complete, dated, month after month. The page is considerably thinner about the agency's half: a referral line with no follow-through entry; assistance described in the plan's language and then, in the chronology, largely unmentioned again.

Reading for an absence is a skill this case has been teaching you for thirteen months. This is its examination.

**Choices:**
- Mark every housing line — yours and theirs — and ask what the pattern proves → **housing_service_read**  _(HIDDEN + Agency record read with counsel — plan identified housing assistance; parent's housing compliance documented; agency follow-through entries sparse)_
  - NOTE (shown after choosing): Highlighter for yours, pencil for theirs. The pencil gets less exercise, and that is the exhibit.

## [summary_only113] Working from Summaries
*Day 18 — Tuesday, April 21, 2026 — Tuesday, April 21, 2026 (dayOffset 18)*

Without the record, you work from the review reports — which are fair about your progress and summary about everything else. A summary can tell you the agency considers housing your open goal. It cannot show you the plan's own housing-assistance language, or the chronology's thin places where the agency's half of that service was supposed to be entered.

Ms. Adler is blunt, kindly: “We can still build from your folder and the program's letter. What we cannot do is quote their file against itself — and in June, quoting their file against itself is the strongest version of this argument there is. Start with your stamps. They are, at least, unimpeachable.”

**Choices:**
- Start with your own paper — the stamped applications, in order → **housing_service_read**
  - NOTE (shown after choosing): The gaps are real either way. The question June asks is whether they are documented, and by whose paper.

## [housing_service_read] What the File Documents — and Doesn't
*Day 21 — Friday, April 24, 2026 — Friday, April 24, 2026 (dayOffset 21)*

On the legal pad, under the three exception lines, Ms. Adler writes two columns. DOCUMENTED: your applications, complete and dated; your waitlist positions, printed; the program's letter, with its condition stated on its face; your completions everywhere else on the plan. NOT DOCUMENTED: any entry showing the agency providing the housing assistance its own plan identified — no referral follow-through, no assistance contacts, no entry addressing a return date or the program's condition, in thirteen months of chronology.

“Hear me precisely,” she says, “because precision is the whole argument. I am not saying the agency did nothing out of malice. I am saying the file does not document the service the plan identified. The services exception is record-dependent: it is exactly as strong as this column is empty. And the compelling-reason door stands beside it: a parent who has completed everything but the goal the system's own circle is blocking, with a program letter proving the block — documented in the case plan, that is a reason, in writing, that filing would not serve Umar.”

“Two doors,” she says. “Both made of paper. Both need assembling before Wednesday, June 3, 2026.”

**Choices:**
- Read the chronology's silences closely, month by month, before assembling anything → **chronology_silence**
  - NOTE (shown after choosing): Dates first, as ever — including the dates that are missing, which are also a kind of date.

## [chronology_silence] The Silence, Read Closely
*Day 23 — Sunday, April 26, 2026 — Sunday, April 26, 2026 (dayOffset 23)*

One more pass through the chronology, slowly, the way you would read a letter from someone whose silences you have learned to translate. Month by month, your housing entries are verbs: applied, documented, waited, re-applied. The agency's housing entries are mostly nouns: housing, noted. Housing, pending. Housing, barrier.

A barrier is not a service. A note is not an assistance contact. The chronology does not accuse anyone — chronologies never do — it simply shows, in the agency's own sequence, a service that was identified in the plan and then documented mainly by its absence.

Ms. Adler closes the binder. “That,” she says, “is tab one of the packet. Tab two is your stamps. Tab three is the program's letter. Tab four is the compelling reason, which writes itself out of tabs one through three — if we write it carefully and file it in time.”

**Choices:**
- Turn to tab two — your applications, and their stamps → **waitlist_stamps**
  - NOTE (shown after choosing): A thin binder, labeled in pencil with a June date, opens on the table. Binders in this system are where arguments live before they are arguments.

## [waitlist_stamps] Tab Two: The Stamps
*Day 25 — Tuesday, April 28, 2026 — Tuesday, April 28, 2026 (dayOffset 25)*

Your applications, laid in a row, are a year of this case told in receiving stamps: the first application, filed in the case's early months; the renewals; the program application that produced the letter. Every one complete. Every one dated. The waiting list has moved at the speed waiting lists move, and the stamps prove the one thing the file must never be allowed to re-describe: the waiting was the list's, not yours.

Assembled into one stamped set, with a cover page of dates, they stop being errands you ran and become a document a stranger can read cold — which is the only kind of document June respects.

**Choices:**
- Assemble the dated application copies into one stamped set for the packet → **stamps_after**  _(cash −5; FLAG: housingDoc; HIDDEN + Housing — dated, complete applications and waitlist stamps assembled as one set)_
  - NOTE (shown after choosing): Five dollars of copies. A year of queues, in date order, with your name spelled right on every stamp.
- Rely on the summaries — they have always called your applications complete → **stamps_after**
  - NOTE (shown after choosing): They have. Summaries describe; stamps prove. June is a month that prefers proof, and strangers read stamps without needing to trust anyone.

## [stamps_after] A Year, in Date Order
*Day 27 — Thursday, April 30, 2026 — Thursday, April 30, 2026 (dayOffset 27)*

The stamped set goes behind tab two, and the binder gains the particular weight of paper that agrees with itself. Ms. Adler turns the pages slowly: applications, positions, the letter — or, where the assembling did not happen, your own clear recollection, which she does not mock and does not overvalue.

“Tab three next,” she says. “The program's letter is the packet's hinge — it is the system stating its own condition in its own words. Before we build on it, we confirm it: a call to the program, on the record of your log, so June hears the letter confirmed by the office that wrote it.”

**Choices:**
- Call the program and confirm the letter, on the log → **program_call**
  - NOTE (shown after choosing): Confirmation is a humble errand with an exhibit's consequences: a letter, verified, by its author, in your dated log.

## [program_call] The Program, Confirmed
*Day 29 — Saturday, May 2, 2026 — Saturday, May 2, 2026 (dayOffset 29)*

The program's coordinator is brisk and clear, the way people are clear about things they have put in writing. Yes, the letter states the program's position. Yes, your application is complete. Yes — and she repeats it slowly, for the log you tell her you are keeping — once a return date within sixty days exists, the unit can be approved for occupancy on that schedule.

She does not set return dates. She does not comment on the agency's sequence. She confirms her office's letter, on its face, and wishes you well with the specific warmth of a person who has watched this exact circle from her desk more than once.

In the log, the call takes four lines. Letters confirmed by their authors are the packet's load-bearing walls.

**Choices:**
- Log the call, file the log page behind tab three, and look at the circle whole → **circle_diagram**  _(HIDDEN + Housing program — letter's condition confirmed by the program by phone and logged with date)_
  - NOTE (shown after choosing): Tab three: a letter, confirmed. The circle now exists in documents from both of its offices.

## [circle_diagram] The Circle, Drawn
*Day 31 — Monday, May 4, 2026 — Monday, May 4, 2026 (dayOffset 31)*

Ms. Adler draws it on the legal pad, because some things have to be seen to be argued: HOUSING needs DATE. DATE needs HOUSING. A two-box loop with no entrance — except, she taps the pad, the doors the law keeps in exactly this wall.

“The exception packet is the entrance,” she says. “Not because paper is magic. Because the filing decision in June will be made on the file — and a file that documents a services gap and a compelling reason gives the decision somewhere lawful to land that is not a petition. And a documented return timeline, argued from the program's own letter, gives the court a date it can actually set — which is the thing the program is waiting for. The packet and the letter, together, are how a room breaks a circle: each unlocks the other's condition.”

“But hear the deadline inside the strategy,” she says. “A packet filed after Wednesday, June 3, 2026 is an argument about a decision already made. Ours goes in before. That is not a detail. It is the design.”

**Choices:**
- Ask what tab four — the compelling reason — needs from your life, not your file → **umar_visit**
  - NOTE (shown after choosing): It needs, she says, the ordinary evidence of a finished plan and a waiting child — which is to say, next Saturday's visit, documented like everything else.

## [umar_visit] Saturday, Month Fourteen
*Day 33 — Wednesday, May 6, 2026 — Wednesday, May 6, 2026 (dayOffset 33)*

Saturday's visit is at the foster family's home, and Umar — ten, all elbows and chess openings — has set up the board before you finish taking off your coat. He wins the first game. In the second, he explains, while winning more slowly out of kindness, that his class is doing a unit on maps.

He asks, in the middle of the map conversation, the question the program's letter asks in office language: when is he coming to your house — not the room, the house, the one with his room in it? You tell him the truth at his size: the grown-ups are working on the date, a judge helps decide dates, and your job is the visits and the paperwork, both of which you are doing.

He accepts this with a ten-year-old's completeness and returns to the map. On the bus home you think about dates: the one in pencil on a lawyer's calendar, and the one a boy just asked for, which is the same date, wearing its real clothes.

**Choices:**
- Write the visit up in the folder that night, dated → **umar_school**
  - NOTE (shown after choosing): Contemporaneous, as ever: written while the chess game is still set up in your head.

## [umar_school] The School Note
*Day 35 — Friday, May 8, 2026 — Friday, May 8, 2026 (dayOffset 35)*

Umar's teacher sends a note through the visit bag, addressed to you — a courtesy teachers extend and systems rarely notice: his reading is strong, his map unit was the class's best, he tells people his mom is “getting the house ready.” The foster mother passes it along promptly and without commentary, which you have learned is her form of precision: the file gets the fact, not her feelings about the fact.

Into the folder it goes, behind the visit write-up. Tab four is accumulating the way compelling reasons actually accumulate — not as an argument, but as a year of finished work and a child, documented, in the middle of it.

Ms. Adler's packet outline arrives by email that night: four tabs, two exceptions, one deadline. April is for assembly. The deadline is not in April.

**Choices:**
- File the note, and turn to the packet's assembly → **packet_plan**
  - NOTE (shown after choosing): A teacher's note is not law. It is what law's compelling reasons are made of, when they are made honestly.

## [packet_plan] The Packet, Planned
*Day 37 — Sunday, May 10, 2026 — Sunday, May 10, 2026 (dayOffset 37)*

The packet, planned on the legal pad, has the shape of the file itself. Tab one: the services gap — the plan's housing-assistance language, the chronology's thin follow-through, the two-column page you built from the record. Tab two: your stamped applications — the waiting proven to be the list's. Tab three: the program's letter, confirmed — the circle, in the system's own words. Tab four: the compelling reason — every other goal complete, visits kept, a unit waiting on a date, and a boy in month fourteen of a placement his mother's finished plan says he no longer needs to be in, for reasons the file itself documents.

Over it all, a covering statement from Ms. Adler that says what the packet is and is not: it does not accuse anyone of bad faith. It documents a services gap and a compelling reason, and asks that both be documented in the case plan when the filing decision is made — before the date the calendar has circled.

“Assembled from documents, it is an exhibit,” she says. “Assembled from memory, it is a claim. We file the first kind.”

**Choices:**
- Assemble it from the documents only — every entry checkable → **packet_contents**
  - NOTE (shown after choosing): Shorter than your memory of the thirteen months. Stronger, for exactly that reason.

## [packet_contents] Two Doors, One Binder
*Day 39 — Tuesday, May 12, 2026 — Tuesday, May 12, 2026 (dayOffset 39)*

Assembly is slow, unglamorous, decisive work: the chronology excerpts checked against the record, the stamps in order, the letter's copy crisp, the covering statement read aloud once for accuracy and once for tone. A packet that overclaims by one line loses the lines that were true, so the packet claims only what its tabs prove.

When it is done, the binder holds the whole strategy in a form a stranger can audit: a service identified and not documented as provided; a reason, documented, that filing would not serve this child; a program waiting on a date; a mother whose own lines in the file are complete. Two doors, one binder, and a date in June that does not negotiate.

**Choices:**
- Sign the packet's assembly page, and face the filing decision → **packet_draft**  _(cash −5; FLAG: packetBuilt; HIDDEN + Written exception packet assembled from documents — services gap and compelling reason, with exhibits)_
  - NOTE (shown after choosing): Five dollars of final copies. The packet exists. Existing, in this system, is the prerequisite for everything else.

## [packet_draft] The Covering Statement
*Day 41 — Thursday, May 14, 2026 — Thursday, May 14, 2026 (dayOffset 41)*

Ms. Adler's covering statement is two pages, and its discipline is the scenario's discipline in miniature. It names the date — Wednesday, June 3, 2026. It names the two exceptions the packet documents, in the statute's own shape: services identified as necessary for Umar's safe return that the file does not document as provided, and a compelling reason, documented in the case plan, that filing would not serve him (42 U.S.C. § 675(5)(E)). It attaches the program's letter and asks — in the same document, because they are the same ask — that a return date be set that lets the unit be approved.

Its last paragraph says what every page of this scenario has been careful to say: the packet speaks to the filing decision and to the plan. It decides nothing else, accuses no one, and predicts nothing. It is paper, filed in time, asking a file to tell the truth about itself.

What remains is the decision every packet in this series eventually faces: when, and whether, it actually gets filed.

**Choices:**
- Decide, with Ms. Adler, while deciding is still early → **packet_file_choice**
  - NOTE (shown after choosing): June does not move. Everything in this office still can.

## [packet_file_choice] File It, Hold It, or Say It
*Day 44 — Sunday, May 17, 2026 — Sunday, May 17, 2026 (dayOffset 44)*

Three ways, laid out honestly. One: file the packet now — in writing, with the agency and the court, weeks before Wednesday, June 3, 2026 — so the exception exists in the file the filing decision will be made from, and the pre-date review can act on it. Two: hold it and file it at the pre-date review itself — later, thinner, but still paper. Three: raise it orally at the review — your voice, her voice, a transcript, and no exhibits beneath any of it.

“My advice is the first,” Ms. Adler says. “It is also, in the end, your case and your decision. But understand what each week of holding costs: decisions inside agencies get drafted before they get announced, and paper that arrives after a draft hardens has to move furniture. Paper that arrives before is just — furniture, already in the room.”

**Choices:**
- File the written exception packet now, with counsel, before the fifteen-month date → **packet_filed_scene**  _(cash −8; FLAG: packetFiled; HIDDEN + Written exception packet filed with agency and court before the 15-month date; REQUIRES: packetBuilt, recordsRequested)_
  - NOTE (shown after choosing): Filed, stamped, copied — the exceptions now exist in the file the June decision will be made on.
- Hold the packet and file it at the pre-date review → **packet_held_scene**  _(FLAG: packetHeld)_
  - NOTE (shown after choosing): The binder stays assembled, in Ms. Adler's office, gaining nothing but age. Reviews, unlike wine, do not reward this.
- Raise the exceptions orally at the review instead → **oral_scene113**  _(FLAG: oralRaised)_
  - NOTE (shown after choosing): Two voices, clearly heard, with the binder closed on the conference table between them.

## [packet_filed_scene] Filed, Stamped, Copied
*Day 46 — Tuesday, May 19, 2026 — Tuesday, May 19, 2026 (dayOffset 46)*

The packet goes in on a weekday morning, with a stamp and a copy for your folder, and the ordinary anticlimax of important paper: a clerk, a receipt, a binder that is now a filing. Ms. Beam, at your next check-in, mentions it without edge: “I saw the packet. The letter — I hadn't seen the letter stated that way.” It is not agreement. It is the acknowledgment, from inside the circle, that the circle is now documented in both its halves.

The case, meanwhile, is still a child's ordinary weeks, and you keep them: visits, work, the folder, the bus. Filing is an event. The weeks after it are the medium it has to survive in.

**Choices:**
- Keep the visits, the work, and the routine exactly as they are → **month14_work**
  - NOTE (shown after choosing): The packet is filed. June will do what June does — from paper, this time, that includes yours.

## [packet_held_scene] The Binder, Waiting
*Day 46 — Tuesday, May 19, 2026 — Tuesday, May 19, 2026 (dayOffset 46)*

The decision is made and noted: the packet will be filed at the pre-date review. The binder sits in Ms. Adler's office, its tabs in order, its letter crisp — assembled, checkable, and, for now, legally indistinguishable from a rumor, because an unfiled packet exists only where it sits.

“We will file it in the room,” Ms. Adler says. “I want you to understand what that timing means. The agency's internal drafting will already have happened. We will not be furnishing a room. We will be asking a furnished room to make space — which rooms do, sometimes, for excellent paper, at a price in persuasion that early paper never has to pay.”

You keep the visits, the work, the routine. Your half of the file stays complete. The other half stays, for now, a binder on a shelf.

**Choices:**
- Prepare, with Ms. Adler, to file it the moment the review opens → **month14_work**
  - NOTE (shown after choosing): If the record will receive it late, it will at least receive it whole.

## [oral_scene113] Saved for the Room
*Day 46 — Tuesday, May 19, 2026 — Tuesday, May 19, 2026 (dayOffset 46)*

The decision is made and noted: the exceptions will be raised orally at the pre-date review. Ms. Adler prepares the statement with you, word by word, because if the record will hold only words, the words will at least be exact: the service, the silence, the letter, the circle, the date.

“Understand the medium,” she says. “A transcript preserves that we said it. Exhibits preserve what we said it about. Filing decisions are made from files. We are choosing to speak to a file in a voice it cannot keep.”

You keep the visits, the work, the routine. Somewhere in an office, a chronology with thin places sits in a drawer, unanswered by anything but a speech scheduled for June.

**Choices:**
- Rehearse the statement once more, and keep the weeks clean → **month14_work**
  - NOTE (shown after choosing): Exact words, exactly delivered, are still words. June will price the difference.

## [month14_work] Month Fourteen, at Work
*Day 48 — Thursday, May 21, 2026 — Thursday, May 21, 2026 (dayOffset 48)*

Month fourteen is mostly logistics, which is to say it is mostly the case: a shift change at work that threatens the Saturday visit, solved with a supervisor's signed schedule; a school form for Umar, signed and returned the same day; the residence's quiet, continued fact — a good room, for one person, that a child cannot live in.

Umar's foster mother mentions, kindly, that the agency has asked about “schedules in June.” She does not know more than that, and says so. June is acquiring a shape in other people's calendars too. Yours has held its shape since April: a date, circled in pencil, with a binder under it — filed, held, or spoken, depending on the road you chose.

**Choices:**
- Confirm the June dates in writing with everyone who needs them → **home_prep113**
  - NOTE (shown after choosing): One more month where the paper and the life agree with each other.

## [home_prep113] The Box Labeled UMAR'S ROOM
*Day 49 — Friday, May 22, 2026 — Friday, May 22, 2026 (dayOffset 49)*

In the corner of the single room there is a box you have kept for a year, labeled in marker: UMAR'S ROOM. Inside: his books, the chess set's spare queen, curtains bought on sale in a month when hope was cheaper. It is not an exhibit. No tab in any binder claims it.

It is included here because the packet, the letter, and the date are all, in the end, about the box: about whether a bureaucratic circle gets to decide how long a labeled box stays packed in a room a child cannot enter. The case will be decided on paper. The paper is about this.

You tape the box shut again, gently, and go to sleep in the room that is waiting to stop being the barrier.

**Choices:**
- Sleep, and face the agency's next letter in the morning → **agency_position**
  - NOTE (shown after choosing): Envelopes from agencies have a weight you can identify before you open them. June's are arriving early.

## [agency_position] The Agency's Draft Position
*Day 51 — Sunday, May 24, 2026 — Sunday, May 24, 2026 (dayOffset 51)*

The letter arrives on agency letterhead, and it is almost the letter Ms. Adler predicted: as the case approaches fifteen months in care, the agency will make and document its filing decision at the fifteen-month date — Wednesday, June 3, 2026 — on the case record. A second paragraph notes that permanency will also be addressed at the pre-date review, including, if the evidence supports it, the goal.

“On the case record,” Ms. Adler says, reading it over your shoulder. “That phrase is the whole spring, in their words this time. The record currently contains your completed plan, the program's letter, and — depending on a decision made in April — a filed packet, a held binder, or a speech we have not given yet. A decision made on the record can only use what the record holds.”

The review is days away. What the record holds is about to stop being a planning question.

**Choices:**
- Ask what the pre-date review can actually do, in order → **supervisor_read**
  - NOTE (shown after choosing): Reviews do specific things in a specific order, she says. Ours has two jobs: answer the date, and break the circle. In that order.

## [supervisor_read] A Cold Reader, Upstairs
*Day 53 — Tuesday, May 26, 2026 — Tuesday, May 26, 2026 (dayOffset 53)*

Personnel is weather in this system, and this month the weather is a supervisor you have never met, who will sign the filing decision and who reads files the way supervisors read them: cold, complete, and without a single memory of any meeting you have ever attended.

This is the moment the spring was quietly designed around. A cold reader cannot be told what everyone in the case happens to know about the circle. She can only read. If the packet is in the file, she reads a services gap with exhibits and a letter with a condition in it. If it is not, she reads a chronology that calls housing a barrier, a summary that calls it your open goal, and a date that says fifteen months.

“Files outlive the people who remember the case,” Ms. Adler says. “June's reader is the proof. Our remaining work is to make sure the paper in the room is the paper we chose.”

**Choices:**
- Go home — a call from the foster home is waiting in your log to return → **foster_call113**
  - NOTE (shown after choosing): Cold readers are not enemies. They are the audience every filed page was always written for.

## [foster_call113] A Call from the Foster Home
*Day 54 — Wednesday, May 27, 2026 — Wednesday, May 27, 2026 (dayOffset 54)*

Umar's foster mother calls about a practical matter — a school trip form, a signature, the ordinary plumbing of a placed child's week — and handles it with the practiced kindness of a woman who has learned which parts of a case are hers to carry. The form gets signed. The week gets plumbed.

“He asked the house question again,” she says, at the end, not unkindly. “I told him what you told him. Dates, and grown-ups working on them.” Two households, one sentence, agreed across a case file: some coordination in this system happens entirely without forms, and works — and the rest of it, the part June decides, happens only with them.

**Choices:**
- Note the call and the form in the folder, dated, and turn to the review notice → **review_notice113**
  - NOTE (shown after choosing): Even the un-formal parts get a dated line now. The habit no longer feels like a habit; it feels like the case's other language.

## [review_notice113] The Review Notice
*Day 55 — Thursday, May 28, 2026 — Thursday, May 28, 2026 (dayOffset 55)*

The notice for the pre-date review arrives with its date — days before Wednesday, June 3, 2026 — and its paperwork: the agency's pre-review summary. Your progress is reported fairly, in the summary's careful language: all goals complete except housing; housing, barrier; visits, warm and consistent.

What the summary does not contain is the circle. It describes housing as your unfinished goal and the date as the case's approaching fact, in separate paragraphs, the way summaries keep related truths in separate rooms so they never have to meet.

The review is where paragraphs meet. It is also, Ms. Adler reminds you on the phone, the last room in which the packet and the letter can be put in front of the date together — before the date stops being upcoming and becomes arrived.

**Choices:**
- Prepare the review the way Ms. Adler prepares everything: from the file outward → **review_prep113**
  - NOTE (shown after choosing): File outward: packet, letter, stamps, record. The room will supply the rest.

## [review_prep113] The Night Before the Review
*Day 57 — Saturday, May 30, 2026 — Saturday, May 30, 2026 (dayOffset 57)*

Preparation is assembly, one last time: the filed packet's stamped copy — or the held binder, or the oral statement's exact words — the program's letter, the stamped applications, the school note, the visit write-ups. The folder by the door. The bus fare in your coat.

Ms. Adler's last instruction is about order, because order is argument: “The packet first — what the file documents about the service and the reason. The letter second — what the system itself says it needs. The ask last, in one sentence: document the exceptions, and set the date the letter is waiting for. Rooms break circles in the order they are handed the pieces.”

You sleep as well as review eves allow, in the room with the labeled box.

**Choices:**
- Take the folder, and go to the review → **review_circle**
  - NOTE (shown after choosing): Fourteen months of paper, carried by the person it is about, into the room it was written for.

## [review_circle] The Review Before the Date
*Day 59 — Monday, June 1, 2026 — Monday, June 1, 2026 (dayOffset 59)*

The review is longer than the last one, and Wednesday, June 3, 2026 is named in it plainly, by the judge, on the record: fifteen months, days away. Your progress is reported, fairly again. The agency states that its filing decision will be documented at the date, on the record. Placement continues, today, as it was always going to today.

Then the judge turns to the housing paragraph — the barrier, in the summary's word — and to whatever your spring has put in the file about it. What happens next depends, with a precision this scenario has been honest about since April, on what your choices actually filed, held, or saved for your voice.

**Choices:**
- Put the filed packet and the program's letter before the court together — the exceptions, documented, and the date the letter is waiting for → **end_win113**  _(REQUIRES: packetFiled, programLetter, housingDoc)_
  - NOTE (shown after choosing): Packet first, letter second, ask last, in one sentence — the order rehearsed the night before.
- Let the review close on the filed packet, the program's letter never having arrived — the date will do what it does → **filing_eve**  _(REQUIRES: packetFiled; REQUIRES-NOT: programLetter)_
  - NOTE (shown after choosing): A filed packet, missing its letter: the review is brief, and June is not.
- Let the review close on the filed packet, the housing document still missing from it — the date will do what it does → **filing_eve**  _(REQUIRES: packetFiled, programLetter; REQUIRES-NOT: housingDoc)_
  - NOTE (shown after choosing): A filed packet, missing its housing paper: the review is brief, and June is not.
- File the held packet now, in the room, and ask that it be received before the date → **late_filed_scene**  _(REQUIRES: packetHeld)_
  - NOTE (shown after choosing): Whole paper, late arrival: the room is asked to make space for a binder it should have met in April.
- Let the review close on the summary — the date will do what it does → **filing_eve**  _(REQUIRES-NOT: packetFiled, packetHeld)_
  - NOTE (shown after choosing): A warm, brief review, silent on the only questions June asks.
- Hear the agency's goal request, unanswered by any filed paper → **end_goalchange**  _(REQUIRES-NOT: packetFiled, packetHeld)_
  - NOTE (shown after choosing): A goal, proposed in a room where the only exhibits are a summary and a date.

## [late_filed_scene] Filed Late, in the Decision's Window
*Day 63 — Friday, June 5, 2026 — Friday, June 5, 2026 (dayOffset 63)*

The review receives the packet — whole, checkable, and late. The court does not rule from the bench on the filing decision; it continues the documentation of that decision by days, into the window after Wednesday, June 3, 2026, and the packet, filed Friday, June 5, 2026, is in the file when the agency documents its decision inside that window.

Late is not early, and this scene will not pretend otherwise: the agency's draft position had already hardened, the date had already struck, and the packet had to move furniture in a furnished room. But furniture, moved by excellent paper in a window a court held open, is still moved.

What the decision document does with a packet it met late is June's last lesson, and it differs from what it does with one it met in April — by exactly the width of the word partial.

**Choices:**
- Read the documented decision when it arrives → **end_late**
  - NOTE (shown after choosing): Stamped, filed, days after the date. In this system, days are a currency and this packet spent them.

## [filing_eve] The Week the Date Arrives
*Day 60 — Tuesday, June 2, 2026 — Tuesday, June 2, 2026 (dayOffset 60)*

The last days run on rails laid in April. A visit, kept. A chess game, lost honestly. The binder — unfiled, or never assembled into the room — sits where it sits. There is nothing left to build, which is itself the lesson this scenario has been teaching since the program's envelope: by the week of a date like this, the case is the record, and the record is finished being written by everyone.

Ms. Adler calls the night before. “Whatever tomorrow documents,” she says, “remember what it is. A filing decision. Not a verdict on you, not a hearing, not an ending of anything except a question about a petition. Umar's case goes on either way, and so do you.”

**Choices:**
- Sleep, as well as a person can, and let the date come → **filing_day**
  - NOTE (shown after choosing): Wednesday, June 3, 2026. Fifteen months, to the day the count runs from.

## [filing_day] The Fifteenth Month
*Day 61 — Wednesday, June 3, 2026 — Wednesday, June 3, 2026 (dayOffset 61)*

Wednesday, June 3, 2026 — computed in this story as it is computed in the law: fifteen months from the Monday Umar was placed, Monday, March 3, 2025. The agency's filing decision is documented today, on the record the spring built.

There is no courtroom drama in this scene, because filing decisions rarely have any. There is a file, a cold reader's review of it, a decision, and a document that records the decision and its reasons. What those reasons can honestly be depends — as Ms. Adler said in April, as the agency's own letter said in its own words — on what the record holds: a completed plan, a barrier in a summary, a circle nobody filed an answer to.

**Choices:**
- Read the documented decision when it arrives → **end_undocumented**
  - NOTE (shown after choosing): The date arrives at a file that was never handed the documents that answer it.

## [end_win113] Ending — Documented: The Goal Stays Home (PARTIAL)
*Day 66 — Monday, June 8, 2026 — Monday, June 8, 2026 (dayOffset 66)*

The decision document, arriving days after the review, does the two things the packet was built to make possible, and it does them in writing. First: the agency documents the exceptions in the case plan — the file does not document the housing-assistance service the plan identified as necessary for Umar's safe return, and a compelling reason is documented that filing a termination petition would not serve him — and no petition is filed at the fifteen-month date. The goal stays what it has always been: reunification.

Second — and this is the circle, breaking on paper — the court sets the return timeline the packet asked for: a return date, named and dated, inside the window the program's letter stated. The letter goes back to the program with the date on it. The unit's approval, the program confirms, proceeds on that schedule: the occupancy the circle was withholding, unlocked by the date the circle was demanding, each condition met by the other's document.

Umar sleeps tonight where he slept last night. Read the next debrief before you call this anything. Then call it what it is.

**Ending.**

**Debrief:**
- WHAT THE RECORD HELD (the hidden record, revealed): A file with both halves present. Your half: every plan goal complete but housing, visits kept, a year of stamped applications proving the waiting was the list's. The system's half, documented by your spring's asking: a plan that identified housing assistance as necessary, a chronology that does not document it as provided, and a program letter — confirmed by its author — stating on its face that a unit could be approved once a return date within sixty days existed. Assembled as a written exception packet and filed, with counsel, before Wednesday, June 3, 2026, so that a cold reader, and then a court, met the services gap, the compelling reason, and the letter in one binder, in time.
- THE LAW UNDER THIS PATH — AND THE LABEL: At 15 of the most recent 22 months, the agency is generally to file a termination petition UNLESS an exception is documented: (i) the child is being cared for by a relative, (ii) a documented compelling reason that filing would not serve the child, or (iii) the agency has not provided services it identified as necessary for the child's safe return (42 U.S.C. § 675(5)(E)). This route built (ii) and (iii) together, exactly as the statute's discipline requires: documented, in the case plan, before the date. The route to the file began with the record released on request (55 Pa. Code § 3130.44(d)) and counsel throughout (42 Pa.C.S. § 6337). Label this win honestly — it is PARTIAL: the packet buys the documented exceptions and the goal stays reunification; a return date is set and a unit's approval proceeds on it — but Umar is still placed at this scenario's curtain, reunification itself happens, if it happens, in a later chapter this scenario does not depict, and no hearing on any petition was held or decided, because there is no petition.
- WHAT NO STRATEGY CONTROLS: A different cold reader could have weighed the same packet and filed anyway, turning the documented exceptions into arguments for a harder room; the program's unit could have been lost to its own list in the interval; a judge less willing to set a date on a letter's terms leaves the circle documented but unbroken. Workers, supervisors, judges, programs, and luck all hold pieces of this ending. What your choices controlled was narrower and real: whether, when the date arrived, the file documented the reasons it should not strike — and whether the letter that could break the housing circle was in the room where dates are set, before the date ran out.

## [end_late] Ending — Filed Late, and It Landed (PARTIAL)
*Day 66 — Monday, June 8, 2026 — Monday, June 8, 2026 (dayOffset 66)*

The documented decision, arriving inside the window the court held open, engages the packet it met late — and lands, in part. The exceptions are documented in the case plan, on the packet's exhibits: the services gap is entered as documented, the compelling reason is noted, and the agency does not file a petition on the strength of a date its own file could not survive being read aloud. The goal stays reunification.

What late cost is itemized in the same document's silences. No return date is set in this decision: the program's letter, answered weeks after it could first have been answered, must be taken up at the next review, with the unit's place on the program's schedule re-confirmed rather than proceeding. The circle is not broken in this ending. It is documented, conceded, and scheduled — which is more than undocumented circles get, and less than broken ones.

Umar's box stays packed a while longer, in a room the file now correctly describes as a barrier the system built. Correct descriptions, filed late, still change what happens next. They just change it next.

**Ending.**

**Debrief:**
- WHAT THE RECORD HELD (the hidden record, revealed): The same packet as the early path — the same tabs, the same letter, the same stamps — received after the agency's position had drafted and after Wednesday, June 3, 2026 had struck, inside a documentation window a court continued by days. It was enough to be engaged, documented, and acted on for the filing decision. It was not early enough to be in the room when the return date could have been set alongside it, and that difference — days, in a case of months — is the entire distance between this ending and the broken circle.
- THE LAW UNDER THIS PATH: The exceptions (42 U.S.C. § 675(5)(E)) are record-dependent and this record, once the packet landed, documented two of them — services identified and not documented as provided, and a compelling reason documented in the case plan. They speak to the filing decision, which is all that was decided here; a petition, had one been filed, would still have required proof by clear and convincing evidence at a hearing this scenario does not depict. The record itself came from the verified route — released on request (55 Pa. Code § 3130.44(d)), assembled with counsel (42 Pa.C.S. § 6337). Label this ending PARTIAL, twice over: the filing was answered, and the circle was not broken — the goal survives, the date does not yet exist, and the program's unit waits on a review still to come.
- THE HONEST PART: Late paper is this system's most common tragedy and its most survivable one: the packet was true in April and true in June, and only its timing was negotiable — which is to say, only its effect was. A reader who refused the late filing outright, a court that had not continued the window, a program slot lost in the interval: any of them demotes this ending without Farida changing a thing. What her choices bought, even late, was that the exceptions entered the file as exhibits instead of arriving as a parent's memory against a chronology's silence. Memory loses to dates. Exhibits, even late ones, have to be answered.

## [end_undocumented] Ending — The Date Strikes, Undocumented
*Day 66 — Monday, June 8, 2026 — Monday, June 8, 2026 (dayOffset 66)*

The agency's documented decision arrives by mail, and it is brief in the way of decisions that were never really contested: the child has been in care fifteen of the most recent twenty-two months; the agency will file. Your progress is noted, fairly, in a paragraph. Housing is listed as the open goal — your open goal, in the summary's grammar — with the circle nowhere in the document, because the circle lived in a letter nobody filed and a chronology nobody quoted.

Nothing in the decision is cruel, and no one in it is a villain. It is a date, doing what dates do to files that were never asked to answer them — and a housing barrier, described for fifteen months as a mother's unfinished task, completing its transformation into the reason her rights are now petitioned against.

Ms. Adler puts the decision in your folder, on top. “The packet still exists,” she says. “Everything in it is still true, and the case it can still help is the harder one that starts now. Paper filed late still files. It just files into a different case.”

**Ending.**

**Debrief:**
- WHAT THE FILE HELD (the hidden record, revealed): A completed plan, fairly reported, and an unanswered file: no record request that surfaced the plan's housing-assistance language, no chronology read for its silences, no packet assembled or filed, and a program letter — the system stating its own condition in its own words — that never became an exhibit in any room. The services gap happened; the circle happened; both are in this debrief because they were in your life. Neither entered the file as a document, and a filing decision made on the file could not see them. The date did not defeat an argument. It arrived where no argument had been filed.
- THE LAW UNDER THIS PATH: At 15 of the most recent 22 months, the filing the federal law generally directs (42 U.S.C. § 675(5)(E)) proceeded, with none of its three documented exceptions established in the record — not relative care, not a documented compelling reason, and not the services exception, which is record-dependent and was never documented. A petition is still only a petition: the agency would have to prove it by clear and convincing evidence at a hearing this scenario does not depict, and counsel (42 Pa.C.S. § 6337) and your own record, released on request (55 Pa. Code § 3130.44(d)), remain available for the case that now follows. Nothing about grounds has been decided by anyone.
- THE HONEST PART: Dates do not grade effort, and this ending must not be read as one: you completed everything the plan asked that a person can complete alone, and the one goal you could not complete alone was completed against you, as a filing. Another worker who quoted the letter herself, a supervisor who asked what the file documented about assistance, a lawyer who circled the date in February instead of April — the same luck and people run through every ending of this scenario. The difference here is only that the spring's assembly never reached a file, and paper, unlike memory, cannot be filed retroactively into a decision already documented.

## [end_goalchange] Ending — The Goal Changes on a Thin Record
*Day 62 — Thursday, June 4, 2026 — Thursday, June 4, 2026 (dayOffset 62)*

The agency's goal request is argued from the summary, and the summary is the only paper arguing: fifteen months approaching, one goal open, housing unresolved. Against it there is no packet, no letter in evidence, no chronology quoted — only your voice, accurate and unaccompanied, explaining a circle the file describes as a barrier.

The order changes the goal. Umar's permanency goal is no longer reunification; the agency is directed to pursue the new goal, and the case's machinery — its visits, its reviews, its summaries — re-aims itself accordingly, politely, in the weeks that follow. The housing circle does not break. It becomes, in the new goal's grammar, beside the point: the unit that needed a date will simply never be asked for one.

Outside, Ms. Adler does not dress it up. “Goals are changed on records,” she says. “Ours was a summary and a date. Theirs was the same summary and the same date, read in the direction summaries point. The packet would not have guaranteed anything. It would have made them argue against documents. Arguing against documents is harder, and sometimes that is the whole margin.”

**Ending.**

**Debrief:**
- WHAT THE FILE HELD (the hidden record, revealed): A thin record in the precise sense: a fair summary of a strong parent, an open housing goal described as hers, an approaching date — and none of the documents that re-describe either fact. No exception packet was filed (or held, or assembled from the record), the program's letter never entered evidence, and the chronology's silence about housing assistance was never read aloud by anyone. The goal was changed on what was in the room, and what was in the room was a summary.
- THE LAW UNDER THIS PATH: A goal decision at a permanency review is made on the record before the court, and this record contained no documented exception under 42 U.S.C. § 675(5)(E) for the court to weigh against the approaching date — no documented compelling reason, no documented services gap — although both existed in the world and in a folder. The filing date itself, Wednesday, June 3, 2026, still arrives on its schedule, and a petition, if filed under the new goal, would still require proof by clear and convincing evidence at a hearing this scenario does not depict. Counsel (42 Pa.C.S. § 6337) can still request the record (55 Pa. Code § 3130.44(d)) and build, for the harder proceedings ahead, the documentation this spring was for.
- THE HONEST PART: This is not an ending about a mother who failed to house her son. It is an ending about a system that described a queue as a character trait for fifteen months and then changed a child's goal on the strength of its own description — while the documents that corrected the description sat, true and unfiled, in a folder and a binder. A different judge could have asked for the letter unprompted; some do. This one weighed what was filed. The record from here is still being written, and the packet — assembled, whenever it is assembled — will be read by the next room, which is a harder room, and will need it more.
