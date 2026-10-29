# THE FIRST 90 DAYS — Scenario 28: “The Education File”

*Human-readable script. This document and `scenario-28.json` are generated from a single source and match node-for-node: same IDs, same order, same choices, same effects.*

**The family is fictional — a composite. No real person's story appears here.**

**Content note:** This scenario depicts a school-age child's first year in placement — a school transfer, two record systems, and the meetings and reviews of a dependency case — told through procedure and paperwork. There is no graphic content. Players may skip any scene or use the quick exit at any time.

**How to read effects:** `cash −40` changes the player's cash. `FLAG: name` sets a flag the engine tracks. `HIDDEN + item` means the case file quietly records that item at this choice — the player does not see it when it happens. `NOTE:` is text shown to the player right after choosing.

Start date: Monday, September 8, 2025. Day offsets are days since the scenario's start date.

## [opening] The Backpack by the Door
*Day 0 — Monday, September 8, 2025 — Monday, September 8, 2025 (dayOffset 0)*

Your son Sam is eight, in third grade at Lincoln Elementary, and proud of exactly two things: his reading folder, and the fact that he has only lost it twice since school started. He has an individual education plan — extra reading help in a small group, a check-in with a counselor most weeks, and a page of things that help him settle when the room gets loud. On good weeks, all of it happens.

You work the early shift at a bakery across town and clean offices two evenings a week. This month the arrangement that held your life together — your neighbor watching Sam between school and your evening shift — fell apart when she moved in with her sister. The agency has visited twice. The word in the letters is “supervision.” The word in your kitchen is “coverage,” and you do not have it.

This morning there is a note in the backpack from Lincoln about a planning meeting later this fall, and a second envelope, from the agency, asking you to come in tomorrow. Two systems, two envelopes, one backpack. That is the whole game, and it has already started.

**Choices:**
- Read both envelopes twice, and put the school note on the fridge → **removal_day**
  - NOTE (shown after choosing): The fridge is your first filing system. It will not be your last.
- Go to work — the envelopes will keep until your shift ends → **removal_day**
  - NOTE (shown after choosing): They keep. Paper is patient. That is not always a comfort.

## [removal_day] The Second Envelope
*Day 1 — Tuesday, September 9, 2025 — Tuesday, September 9, 2025 (dayOffset 1)*

The agency office has chairs in a row and a form for everything. The caseworker, Ms. Tran, is not unkind. She lays out the last two weeks the way the file lays them out: the evenings Sam was alone, the morning he walked to school by himself, the coverage you described as “being handled” when it was being improvised.

The agency asks the court for custody, and the court grants it on an emergency basis. Sam will stay with a foster parent across town while the case is sorted out. A hearing will follow within days, and you will have a lawyer there. Those are not courtesies. They are the structure, and Ms. Tran says them plainly.

Sam packs his reading folder first. You stand in the doorway of a room that is suddenly very tidy, holding a list of phone numbers someone printed for you, and the school note is still on the fridge, talking about a meeting at a school Sam may no longer attend.

**Choices:**
- Ask, before anyone leaves, exactly where Sam will sleep and which school he will go to → **shelter_hearing**  _(FLAG: removed; HIDDEN + Removal — emergency custody granted; placement across town)_
  - NOTE (shown after choosing): Ms. Tran writes both answers on the back of the phone list. Across town means a different school bus. A different school.
- Sign what is put in front of you and get home before you fall apart → **shelter_hearing**  _(FLAG: removed; HIDDEN + Removal — emergency custody granted; placement across town)_
  - NOTE (shown after choosing): Falling apart at home is allowed. The paperwork does not record it either way.

## [shelter_hearing] Seventy-Two Hours
*Day 3 — Thursday, September 11, 2025 — Thursday, September 11, 2025 (dayOffset 3)*

The shelter care hearing happens fast, because the law says it must: when a child is taken into protective custody, a hearing follows within 72 hours (42 Pa.C.S. § 6332; 23 Pa.C.S. § 6315(d)). Yours is Thursday, September 11, 2025 — two days after the removal, inside the window, in a courtroom smaller than you expected.

A lawyer is appointed for you — counsel for a parent in a case like this is part of the structure, not a favor (42 Pa.C.S. § 6337). Her name is Ms. Okafor, and she has read the file on the way in, which puts her one file ahead of you. Sam has his own advocate in the room. The judge keeps Sam in placement for now, sets visits twice a week, and says the word “review” with a date attached, in December.

In the hallway, Ms. Okafor gives you the only map she can draw today: the court case will run on court dates. Sam’s schooling will run on the school’s own calendar. “Those two clocks,” she says, “do not talk to each other. Anything that needs to travel between them travels in somebody’s hands. Assume it will have to be yours.”

**Choices:**
- Write down the December review date and the visit days, in ink, on the phone list → **placement_news**  _(HIDDEN + Shelter care — placement continued; counsel appointed (42 Pa.C.S. § 6337))_
  - NOTE (shown after choosing): Ink. In this system, ink is a technology.
- Ask Ms. Okafor who tells the new school about Sam’s plan → **placement_news**  _(HIDDEN + Shelter care — placement continued; counsel appointed (42 Pa.C.S. § 6337))_
  - NOTE (shown after choosing): “In theory, everyone,” she says. “In practice, we are going to find out.”

## [placement_news] Across Town
*Day 6 — Sunday, September 14, 2025 — Sunday, September 14, 2025 (dayOffset 6)*

Sam is staying with Mrs. Lindqvist, a foster parent with a spare room, a dog of advanced age, and a laminated list of house rules that Sam reads aloud to you on the phone like a weather report. She sounds steady. Sam sounds small, and then, a minute later, like himself, describing the dog.

Her house is in a different school’s neighborhood. Starting this week, Sam will go to Hillside Elementary, not Lincoln. Nobody made that decision in a meeting about Sam’s education. It was made by an address — where a bed was open — and the bus routes followed from there.

Mrs. Lindqvist enrolled him, because enrollment cannot wait for a file to catch up. She signed the forms put in front of her: name, address, emergency contact. She tells you, honestly, that she wrote “records to follow” in the margin of one of them, because that is what the agency told her.

**Choices:**
- Thank her, and ask what exactly she signed — and what the school asked her for → **new_school_call**  _(HIDDEN + Enrollment at Hillside signed by foster parent; ‘records to follow’ noted in margin)_
  - NOTE (shown after choosing): She lists it from memory, carefully, like someone reading a recipe she only cooked once.
- Call the agency first — surely the file went with him → **new_school_call**
  - NOTE (shown after choosing): Ms. Tran says the school records are “being sent.” Being sent is a tense, not a fact.

## [new_school_call] “Records to Follow”
*Day 9 — Wednesday, September 17, 2025 — Wednesday, September 17, 2025 (dayOffset 9)*

Hillside’s office is friendly and busy in the way of all school offices in September. The secretary finds Sam’s enrollment in seconds. What the school has is two pages: the enrollment form Mrs. Lindqvist signed, and a one-page summary the agency sent — Sam’s grade, his allergies (none), and the sentence “receives support services.”

What the school does not have: his education plan. The evaluation behind it. The page of things that help him settle. The reading group notes from Lincoln that say, in a teacher’s handwriting, what actually works. The school has its own evaluation process, its own meetings, its own letters — and it will, in time, build its own picture of Sam. Right now its picture is two pages thick.

You ask where the rest is. The secretary says records were requested from Lincoln when Sam enrolled. “Requested” is doing the same work “being sent” did. The file now lives in five places — Lincoln, Hillside, the agency, Mrs. Lindqvist’s kitchen drawer, and your fridge — and it is complete in none of them.

**Choices:**
- Ask the secretary to note, on Sam’s enrollment page, that you are his mother and want copies of school mail → **sending_school**  _(cash −4; HIDDEN + Hillside enrollment page — mother’s copy request noted by secretary)_
  - NOTE (shown after choosing): She writes it in pencil. Pencil is a start. You will be back with ink.
- Leave it for now — the school seems to have it handled → **sending_school**
  - NOTE (shown after choosing): It has the enrollment handled. The file is a different matter, and it is not handled. It is pending, in five places at once.

## [sending_school] The Sending School
*Day 14 — Monday, September 22, 2025 — Monday, September 22, 2025 (dayOffset 14)*

Lincoln’s office remembers Sam, which is its own small grief on a Monday morning. Yes, the secretary says, Hillside requested his records. Yes, a packet was put together. It was mailed to the address the school had on file for the family — your old apartment, the one from before the move in August — because that is the address in their system, and systems mail to the address they have.

A copy also went to the agency, she thinks. Or was requested by the agency. She is not being evasive; she is reading a screen that records that a packet left the building, not where it landed. The evaluation — the thick part, the part that explains Sam — was in the packet. The packet is in the mail’s memory now.

You stand at the counter with your new address in your hand, learning the first law of the education file: it does not follow the child. It follows addresses, requests, and signatures — and it follows them slowly, in envelopes, in September, while the child is already sitting in a new classroom being read as a stranger.

**Choices:**
- Give Lincoln your new address in writing and ask for a second copy of the packet, for you → **service_plan**  _(HIDDEN + Lincoln — packet originally mailed to old address; mother’s new address filed)_
  - NOTE (shown after choosing): She photocopies the cover sheet as a receipt. A receipt is a fact with a date on it.
- Ask Lincoln to re-send everything to Hillside and trust the mail this time → **service_plan**
  - NOTE (shown after choosing): She will. It may even work. You will have no paper that says it did.

## [service_plan] The Plan with Your Name on It
*Day 18 — Friday, September 26, 2025 — Friday, September 26, 2025 (dayOffset 18)*

The family service plan meeting is at the agency, around a table built for six and seating nine. Your goals are typed in bold, the way goals are: housing you can keep, a work schedule with coverage for Sam’s hours, parenting support, visits twice a week. Near the end, in ordinary type, is a line about Sam’s schooling: “Mother will remain involved in child’s education.”

Nobody at the table can tell you what that line requires, because the school is not at the table. The school is a third system, with its own letters and its own rooms, and this plan — the court’s paper — reaches it only if someone carries it there. Ms. Tran notes that Sam is “settling” at Hillside, per Mrs. Lindqvist, who is per the school’s first-week note.

You sign the plan. Your signature means you received it and will work it, and you intend to. But you leave with a question the bold type cannot answer: involved in his education — according to which file? The one at Lincoln, the one at Hillside, or the two pages and a summary that are currently standing in for your son?

**Choices:**
- Ask for a copy of the plan before you leave, and the caseworker’s email in writing → **missed_meeting**  _(HIDDEN + Family service plan signed — incl. ‘mother will remain involved in child’s education’)_
  - NOTE (shown after choosing): Copies are the difference between a plan you work and a plan that is worked on you.
- Sign and go — your shift starts in an hour → **missed_meeting**
  - NOTE (shown after choosing): The plan will be at the next meeting either way. So will the question.

## [missed_meeting] The Meeting That Already Happened
*Day 25 — Friday, October 3, 2025 — Friday, October 3, 2025 (dayOffset 25)*

At Thursday’s visit, between the puzzle and the juice boxes, Sam says his teacher asked why he didn’t bring his reading folder, and that “the meeting people” at his new school said he might not need the small group anymore. You ask what meeting. Sam shrugs the shrug of a child reporting weather in another country.

There was a meeting at Hillside last week — the school’s own planning meeting, to draft Sam’s plan for the year. The invitation went to the address on the enrollment form: Mrs. Lindqvist’s house. A copy went to your old apartment. The school read the file it had — two pages and a summary — and drafted a plan for the child in that file: fewer supports, no counselor check-in, a note that he “seems settled, no concerns raised by family.”

You were not absent from that meeting. You were never in the room it was sent to. There is a difference, and the difference is not written anywhere — the sign-in sheet just has an empty line where a mother’s name would go, and empty lines get read as choices.

**Choices:**
- Call Hillside the next morning and ask, calmly and in writing, how invitations are sent — and to whom → **foster_copy**  _(HIDDEN + Hillside planning meeting held without mother; invitation sent to foster home + old address)_
  - NOTE (shown after choosing): The office manager is quiet for a moment. “You should have gotten one,” she says. Should have is a tense, too.
- Call Ms. Tran and ask why the agency’s copy never reached you → **foster_copy**  _(HIDDEN + Hillside planning meeting held without mother; invitation sent to foster home + old address)_
  - NOTE (shown after choosing): She says she’ll look into it. She means it. Looking into it is not the same as it being in the file.

## [foster_copy] The Foster Parent’s Drawer
*Day 29 — Tuesday, October 7, 2025 — Tuesday, October 7, 2025 (dayOffset 29)*

Mrs. Lindqvist meets you at the door with an envelope she has clearly been keeping for you. Inside: the meeting invitation, the sign-in sheet with its empty line, and the draft plan Hillside wrote — she asked for copies of everything, “because it’s his schooling, and you’re his mother.” She assumed you had your own set. Everyone in this story assumes someone else has the paper.

She is not the obstacle. She drove Sam to the meeting, signed where she was asked to sign, and told the school he missed his reading group “because he talks about it.” But her signature is on forms yours should also be on, and the school now treats her kitchen drawer as the family’s address for Sam’s education.

You hold, for the first time, a complete copy of a school document about your son — three weeks into his school year, from the hands of the one person in the system who kept a copy for you on purpose.

**Choices:**
- Thank her, and ask her to keep handing you copies of anything the school sends her → **lawyer_map**  _(HIDDEN + Draft Hillside plan received via foster parent — fewer supports, no check-in)_
  - NOTE (shown after choosing): “Every time,” she says. “It’ll be in the drawer.” A drawer is not a system. But it is, today, the most reliable one you have.
- Take the copies to Ms. Okafor — this is a lawyer question now → **lawyer_map**  _(HIDDEN + Draft Hillside plan received via foster parent — fewer supports, no check-in)_
  - NOTE (shown after choosing): It is several lawyer questions, wearing one coat.

## [lawyer_map] Two Systems, Three Clocks
*Day 36 — Tuesday, October 14, 2025 — Tuesday, October 14, 2025 (dayOffset 36)*

Ms. Okafor clears her desk the way other people roll up sleeves. On the left, she puts the court’s paper. On the right, the school’s. “Dependency case here. Education case there. They are both about Sam. They share almost no paper.”

“On the court side, you have a right worth using in writing: you can request the agency’s records in your case, and the agency is to provide its records on request (55 Pa. Code § 3130.44(d)). That file will show what the agency thinks Sam’s schooling looks like. On the school side, there is no single form I can file for you — the school has its own evaluation process, its own meetings, its own letters. What works there is showing up on its paper: invitations to your address, your name on its forms, your copies of its copies.”

“And the clocks.” She counts them off. “The court’s: reviews, with the December date first. A federal clock, quieter: at 15 of the most recent 22 months in care, the agency must file or join a petition to end parental rights unless an exception applies — a relative caring for the child, a documented compelling reason not to file, or services the plan required that were never provided (42 U.S.C. § 675(5)(E)). Sam is in month one. That clock is not loud yet. And the third clock” — she taps the school’s paper — “is June. The school year ends whether anyone’s file is ready or not. Nobody cites June. Everybody lives by it.”

**Choices:**
- Ask her to start with the agency’s file — in writing, this week → **request_choice**
  - NOTE (shown after choosing): “In writing,” she agrees. “This week. Those are the two load-bearing words.”
- Ask her which clock you should be most afraid of → **request_choice**
  - NOTE (shown after choosing): “None of them, yet,” she says. “Be respectful of all three and afraid of the mail.”

## [request_choice] In Writing, This Week
*Day 38 — Thursday, October 16, 2025 — Thursday, October 16, 2025 (dayOffset 38)*

Ms. Okafor drafts the letter at her desk while you watch: a request, in writing, for the agency’s records in Sam’s case — the reports, the plan, the school-related pages, the scored assessment form summary from intake — sent to the agency with a copy kept for you, dated today, October 16, 2025.

“We could also just ask Ms. Tran at the next visit,” she says. “She’d probably say yes. Probably is how files get lost with everyone’s good intentions intact. A letter makes a date. A date makes a record. A record is the only version of this anyone will believe in December.”

Your bus pass is in your pocket and your shift starts in two hours. The letter needs copies, an envelope, and a walk to the post office that is not on the way to anything.

**Choices:**
- Sign it, copy it, and mail it today — the walk is the job → **school_chase**  _(cash −6; FLAG: recordsRequested; HIDDEN + Records request sent in writing under 55 Pa. Code § 3130.44(d), dated October 16, 2025)_
  - NOTE (shown after choosing): The post office clerk stamps your copy. A stamped copy is a small, dated fact, and it is yours.
- Ask Ms. Tran verbally at Thursday’s visit first — save the walk, keep it friendly → **verbal_detour**
  - NOTE (shown after choosing): Friendly matters. So does a date. You have chosen friendly, and the calendar has noticed.

## [verbal_detour] “I’ll Pull That Together”
*Day 45 — Thursday, October 23, 2025 — Thursday, October 23, 2025 (dayOffset 45)*

At Thursday’s visit, between the puzzle and the juice boxes, you ask Ms. Tran for the agency’s file — the reports, the plan, the school pages. She says, warmly and without hesitation, “Of course. I’ll pull that together for you.”

A week passes. A visit passes. Nothing arrives, because nothing was ever set in motion that produces arrival: no letter, no date, no task in anyone’s queue with your name on it. Ms. Tran is not stalling. She has nineteen other families, and a verbal request lives exactly as long as the conversation that held it.

Ms. Okafor, on the phone, does not say I told you so. She says, “Now we send the letter. It will be three weeks younger than it should have been. Send it anyway — a late date is still a date.”

**Choices:**
- Sign and mail the written request now — late, dated, and real → **late_request**  _(cash −6)_
  - NOTE (shown after choosing): Three weeks, spent on a lesson the system teaches everyone exactly once, if they’re lucky.
- Wait one more week — she said she’d pull it together → **late_request**
  - NOTE (shown after choosing): She did say that. The file room has not heard her say it.

## [late_request] A Late Date Is Still a Date
*Day 52 — Thursday, October 30, 2025 — Thursday, October 30, 2025 (dayOffset 52)*

The letter goes out with today’s date on it — October 30, 2025 — and your stamped copy goes on the fridge, next to the school note from September that started all of this. The fridge is becoming an archive. Archives need better housing, but they start where they start.

Ms. Tran replies by email within days, courteous and brief: the file is being copied and will be sent. This time there is a task in a queue with your name on it. The difference between the two requests is not politeness. It is paper.

While the agency copies, the school year does not pause: Sam is doing his homework at Mrs. Lindqvist’s table, in a classroom reading a two-page version of him, under a draft plan you have seen only because a foster parent kept you a copy in a drawer.

**Choices:**
- Wait for the file — and use the waiting weeks to list, from memory, everything you know the school file is missing → **file_arrives**  _(FLAG: recordsRequested; HIDDEN + Records request sent in writing (late), dated October 30, 2025; mother’s from-memory gap list started)_
  - NOTE (shown after choosing): Your list is four pages. Memory is a bad archive but an excellent index.

## [school_chase] While the Agency Copies
*Day 49 — Monday, October 27, 2025 — Monday, October 27, 2025 (dayOffset 49)*

The agency’s file will take some weeks to arrive — copying a case is a task that joins a queue. You use the wait the way Ms. Okafor told you to: on the school side, where there is no single form, you become the form. At Lincoln’s office you sign a release asking that Sam’s records be sent to Hillside and a copy to you. At Hillside’s office you sign the same request from the other direction, and you hand the secretary your address — the new one — on paper, again.

Two signatures, two dates, two stamped copies for the fridge. The school secretary at Hillside, reading your release, says, “Oh — you’re the mother. We had the foster address as the contact.” Had. Past tense is progress, in an office, in October.

It is not fast. Nothing in either system is fast. But for the first time since September, paper about Sam’s education is moving toward you on purpose, in envelopes with your name spelled right.

**Choices:**
- File both releases and keep both stamped copies together → **file_arrives**  _(FLAG: recordsRequested; HIDDEN + School records releases signed at both schools — copies to mother; contact address corrected at Hillside)_
  - NOTE (shown after choosing): Together is the operative word. A file in five places is a rumor. A file in one pair of hands is a tool.

## [file_arrives] The Agency’s Sam
*Day 60 — Friday, November 7, 2025 — Friday, November 7, 2025 (dayOffset 60)*

The agency’s file arrives in a envelope thick enough to need both hands. You read it at your kitchen table the way you were taught to read everything in this case: slowly, with a pen, dating the margins.

The agency’s Sam is a recognizable boy. The intake summary describes a child who “responds to structure and reading support.” The scored assessment form from intake rates his education needs as low — because, the notes say, his plan at Lincoln was “in place and working,” so no action was needed. The file holds the service plan, the visit notes, two court reports — and, for school records, a single page: the same one-page summary Hillside has. The agency never had the evaluation either. It had a sentence about the evaluation, and the sentence said things were fine.

You now hold two files about your son. Next week, side by side, they are going to introduce themselves to each other, and it will not go smoothly.

**Choices:**
- Read it all again tomorrow with the school papers beside it → **compare_files**  _(HIDDEN + Agency file received — intake assessment rated education needs ‘low’ because Lincoln plan was ‘in place’)_
  - NOTE (shown after choosing): Tomorrow. Tonight you make tea and look at the fridge, which is full, and incomplete, like everything else.

## [compare_files] Two Files, Two Children
*Day 67 — Friday, November 14, 2025 — Friday, November 14, 2025 (dayOffset 67)*

Side by side on the table, the files describe two different children with the same name and birthday.

The agency’s Sam — Lincoln’s Sam — is a boy whose reading support works, who settles with a check-in and a quiet corner, whose evaluation tells a story of a child learning to ask for help in words. The school’s Sam — Hillside’s Sam, built from two pages and six September weeks — is a boy who “resists reading tasks,” who “has difficulty settling,” about whom “family has not raised concerns.” Every one of those sentences is true of a child whose supports were quietly removed by a missing envelope. None of them is the whole child.

The draft plan Hillside wrote follows from the file Hillside had. The agency’s reports follow from the file the agency had. Nobody lied. Everybody filed. The child who fell out of the record fell between two systems that each assumed the other was holding him.

**Choices:**
- Start a single page: Sam’s dates, in order, from both files — where the stories split → **eval_consent**  _(HIDDEN + Comparison — agency file and school file describe materially different needs and history)_
  - NOTE (shown after choosing): One page. Two columns become one line of dates. It is the first document in either system that contains the whole fall.
- Call Ms. Tran and read her the two descriptions of your son, out loud → **eval_consent**  _(HIDDEN + Comparison — agency file and school file describe materially different needs and history)_
  - NOTE (shown after choosing): There is a silence on the line that is worth more than most sentences. “Send me that,” she says. “In writing.” She has learned the words too.

## [eval_consent] The School’s Own Process
*Day 74 — Friday, November 21, 2025 — Friday, November 21, 2025 (dayOffset 74)*

Hillside, to its credit, does not pretend its two pages are enough. The counselor calls — Mrs. Lindqvist first, then, because your name is now on the contact page, you — to say the school will run its own evaluation of Sam: classroom observation, reading checks, time with the counselor, over the coming weeks and into the winter. Its process, its letters, its pace. There is no court date for it and no shortcut through it, and the counselor does not offer one.

There is a consent form. It was sent to Mrs. Lindqvist, because the file said to. She has not signed it — she wrote your phone number across the top instead, in the handwriting of a woman who has decided which drawer things belong in. The school re-sends the form to you, at your address, with your name on it.

Your signature on that form is a small thing and a large one: the school’s paper will now say that Sam’s mother was asked, and answered, and can be asked again.

**Choices:**
- Sign the consent, copy it, and return it by hand so the date is witnessed → **address_fix**  _(HIDDEN + School evaluation consent signed by mother; school process running into winter)_
  - NOTE (shown after choosing): The office stamps your copy without being asked. Offices learn, too.
- Sign it and mail it back in the envelope provided → **address_fix**  _(HIDDEN + School evaluation consent signed by mother; school process running into winter)_
  - NOTE (shown after choosing): It will arrive. The envelope knows the way now — your address is finally the one in the system.

## [address_fix] Every Address You Live At, On Paper
*Day 84 — Monday, December 1, 2025 — Monday, December 1, 2025 (dayOffset 84)*

December is coming, and with it the court review. Ms. Okafor’s advice is unglamorous and total: “Every system that sends you paper gets your address in writing, from you, with a copy kept. Not the foster home’s address. Not the old apartment. Yours.”

The agency’s front desk takes your change-of-address form. The court clerk takes another. Hillside already has it, twice over. Lincoln has it. Each copy joins your growing pile with a date on it. It is the least dramatic paperwork of your life and it may be the most consequential: every missed meeting in this case began life as a letter that went somewhere you don’t live.

Mrs. Lindqvist, told of the project, nods approvingly and retires her drawer. “You’re the address now,” she says, like a title being handed over.

**Choices:**
- File the address change in writing with the agency, the court, and both schools — and keep every copy → **report_draft**  _(FLAG: addressFixed; HIDDEN + Address corrected in writing in all systems; mother is contact of record)_
  - NOTE (shown after choosing): Four stamps. Four dates. The mail, from here on, has a fighting chance.
- Tell Ms. Tran the new address at the next visit and let her update the system → **report_draft**
  - NOTE (shown after choosing): She’ll update her screen. Screens don’t send letters; the list that does may be a different one.

## [report_draft] One Sentence in a Draft
*Day 88 — Friday, December 5, 2025 — Friday, December 5, 2025 (dayOffset 88)*

Ms. Tran, fairly, sends you the agency’s draft report for December’s review so there are no surprises. Most of it is accurate, some of it is kind, and one sentence is neither: “Mother has not participated in education planning for the child this school year.”

It is the empty line on the sign-in sheet, grown up into a finding. The report does not say the invitation went to a foster home and a vacated apartment. It does not say you obtained the draft plan from a drawer, signed the school’s consent, filed releases at two schools, or hold the agency’s own file under a written request. The report was written from the agency’s file, and the agency’s file does not contain your fall — because your fall happened on the school’s paper, and the school’s paper is not in it.

The review is in one week. Sentences in reports are load-bearing. This one can still be answered — in writing, with dates, before a judge ever reads it as fact.

**Choices:**
- Write the correction: dated, factual, with the sign-in sheet and your stamped copies attached → **correction_filed**  _(FLAG: recordCorrected; HIDDEN + Written correction to draft report filed with dates and attachments)_
  - NOTE (shown after choosing): No anger in it. Dates don’t need anger. They need company: a stamp, a signature, a sheet with an empty line explained.
- Let it stand — the judge will see how hard you’ve worked → **dec_review**
  - NOTE (shown after choosing): Judges see what is in the record. Working hard and being recorded working hard are, in this building, different achievements.

## [correction_filed] The Correction Goes In
*Day 91 — Monday, December 8, 2025 — Monday, December 8, 2025 (dayOffset 91)*

Your letter is two pages and a small stack of attachments: the meeting invitation addressed to a house you don’t live in; the sign-in sheet; your consent form, stamped; the two school releases; the agency’s own records-request letter, with its date. Each claim in the letter has a paper standing behind it, the way Ms. Okafor taught you: “Sentences a stranger can check.”

Ms. Tran replies the next day — she is, you are learning, fair within the limits of her file — and amends the draft. The sentence now reads: “Mother was not invited to the fall planning meeting; invitations were sent to the foster home and a prior address. Mother has since obtained records, signed the school’s evaluation consent, and corrected her contact information in all systems.” It is longer. It is also true, which in a court file is the more important property.

December’s review will still be December’s review. But the record it reads has been repaired in the one way records accept: in writing, before the hearing, with dates.

**Choices:**
- Go to the review with your folder — the whole fall, in order → **dec_review**
  - NOTE (shown after choosing): The folder goes under your arm like a second spine.

## [dec_review] The December Review
*Day 95 — Friday, December 12, 2025 — Friday, December 12, 2025 (dayOffset 95)*

The review is Friday, December 12, 2025, in the small courtroom, with the flag. The judge has read the amended report — you can tell, because she asks the agency, not you, about the school file: what does Hillside actually have, what is its evaluation finding, when will the court see a school record that matches the child?

The answers are honest and thin. The evaluation is running, over the winter, on the school’s own schedule. The plan Sam is under is still the draft written from two pages. The judge continues the case, keeps the goal as reunification, notes your progress on housing and coverage — real progress, on paper — and orders the agency to include the school’s actual records in its next report, not a summary of a summary.

Ms. Okafor, in the hallway, translates: “The court has now noticed the second file. That took a correction, a consent, two releases, and a records request, and it is still only noticed, not fixed. Winter is for fixing. The school’s evaluation finishes when it finishes. What you do until then is collect the truth in dated form.” Month four of the federal clock closes quietly behind you. Nobody in the hallway says its number. Everybody with a file knows it.

**Choices:**
- Ask Ms. Okafor what ‘collect the truth in dated form’ means, concretely, for January → **january_eval**
  - NOTE (shown after choosing): “A log,” she says. “What the plan promises, what actually happens, dates. Boring. Decisive.”

## [january_eval] The Evaluation, When It Finishes
*Day 123 — Friday, January 9, 2026 — Friday, January 9, 2026 (dayOffset 123)*

The school’s evaluation finishes the way school processes finish: not with a hearing but with a packet, in the new year, after weeks of observation and reading checks and counselor time that happened on ordinary Tuesdays while you were at work. The packet describes Sam at length and, in large part, accurately — a boy who reads below where he should, who settles when the adults around him are predictable, who needs the small group and the check-in. Lincoln’s Sam, surfacing at last in Hillside’s own words.

But the packet lands in a school that has already been running a thinner draft plan for four months, and a packet is not a plan. The counselor says a meeting will be set to write the new one — “in the coming weeks.” In the gap between the evaluation and the meeting, Sam’s days are still governed by the September draft: the one written about the two-page child.

You read the packet twice. It is the first complete school document about your son produced since August. It agrees with Lincoln. It does not yet agree with Sam’s actual school day.

**Choices:**
- Ask the counselor, in writing, for the meeting date — and for a copy of the packet for the agency’s file → **delivery_gap**  _(HIDDEN + School evaluation completed (winter) — broadly confirms Lincoln’s picture; new plan not yet written)_
  - NOTE (shown after choosing): Two requests, one letter, one stamp. You are fluent now, in the only language either system files.
- Wait for the meeting invitation — the school knows your address now → **delivery_gap**  _(HIDDEN + School evaluation completed (winter) — broadly confirms Lincoln’s picture; new plan not yet written)_
  - NOTE (shown after choosing): It does know. That is new, and it is not nothing. It is also not a meeting date.

## [delivery_gap] Promised and Delivered
*Day 130 — Friday, January 16, 2026 — Friday, January 16, 2026 (dayOffset 130)*

Ms. Okafor’s log is a notebook from the dollar store, and it is becoming the most subversive document in the case. Each week you write two columns: what Sam’s plan — even the thin draft — says should happen, and what Sam reports, and Mrs. Lindqvist confirms, actually did. Small-group reading: promised most days; delivered, some weeks, twice. Counselor check-in: promised weekly; delivered most weeks, except the weeks it wasn’t, which have dates now.

Nobody is twirling a mustache. The small group loses its aide to other duties; the counselor covers a crisis down the hall. A school is a building full of other people’s emergencies. But a plan that exists on paper and evaporates in practice is a fact too, and until now it was a fact with no witness but an eight-year-old.

Your notebook has dates. Dates, Ms. Okafor says, are how a parent testifies without raising her hand.

**Choices:**
- Keep the log every week — promised beside delivered, with dates → **feb_meeting**  _(FLAG: serviceLog; HIDDEN + Dated services log begun — plan promises vs. actual delivery)_
  - NOTE (shown after choosing): Boring. Decisive. Yours.
- Rely on memory — you’ll know the pattern when it matters → **feb_meeting**
  - NOTE (shown after choosing): Patterns remembered are opinions. Patterns dated are evidence. The meeting will ask for one of those.

## [feb_meeting] The Meeting You’re Actually Invited To
*Day 151 — Friday, February 6, 2026 — Friday, February 6, 2026 (dayOffset 151)*

The invitation arrives at your address, in your name, with a date you can plan a shift around. It is a small envelope and it feels like a diploma.

The meeting writes Sam’s new plan from the school’s evaluation: the small group restored, the check-in restored, the settling page rewritten by the counselor who has now actually watched him settle. Mrs. Lindqvist attends and backs your account of his evenings. You attend, and the sign-in sheet fills its mother line for the first time this year. The plan, on paper, is finally Sam’s.

On paper. Your notebook sits in your bag with its two columns, and the counselor, fairly, says the restored supports will be “fully in place as staffing settles.” You have learned to hear the future tense in any sentence about your son’s schooling, in either system, and to write it down with its date.

**Choices:**
- Sign the new plan, take your copy, and ask that the agency get one too → **winter_visits**  _(HIDDEN + New school plan written with mother present — supports restored on paper)_
  - NOTE (shown after choosing): Three copies: school’s, agency’s, yours. The file, for once, is complete in three places at the same moment. Savor it. It is not the natural state of things.
- Sign, and raise the delivered-versus-promised weeks from your notebook, gently, with dates → **winter_visits**  _(HIDDEN + New school plan written with mother present — supports restored on paper; delivery gap raised with dates)_
  - NOTE (shown after choosing): The counselor does not bristle. She copies two of your dates into her own notes. Paper recognizes paper.

## [winter_visits] What Sam Reports
*Day 168 — Monday, February 23, 2026 — Monday, February 23, 2026 (dayOffset 168)*

Visits are at the agency’s family room and, increasingly, at the park near Mrs. Lindqvist’s when the weather allows a fiction of ordinary life. Sam is taller. He reads to you from the small-group book with the seriousness of a news anchor. He asks, with the same seriousness, whether he will go back to Lincoln “when this is over,” and whether his Lincoln teacher knows where he is.

You write down the question, with its date, because it is the question both systems keep failing to hold: for the adults, Sam has a placement, a plan, and a goal. For Sam, he has two schools, two sets of adults, one reading folder that has crossed town twice, and a year that is passing at the speed of childhood, which is faster than any clock in either building.

The next court review is in March. The school, content with its new plan, has scheduled its own spring meeting for the same week. Two rooms, one child, five days apart. You can feel the fall’s lesson gathering itself for a second examination.

**Choices:**
- Tell Sam the truth in eight-year-old size: nobody knows yet, and the grown-ups are writing it down → **same_week**
  - NOTE (shown after choosing): He considers this. “Write down that I asked,” he says. You already had. He is his mother’s son.
- Ask Mrs. Lindqvist to keep noting what the school sends home — every scrap → **same_week**
  - NOTE (shown after choosing): The drawer reopens for business. Systems improve. Drawers endure.

## [same_week] The Same Week, Twice
*Day 186 — Friday, March 13, 2026 — Friday, March 13, 2026 (dayOffset 186)*

On Tuesday, March 10, 2026, the school’s spring meeting reviews Sam’s new plan and finds a success story: reading gains, settled weeks, a boy thriving. The team floats easing back the counselor check-in — he is doing so well, why pathologize it? Your notebook, uninvited but present in your bag, shows the check-ins he is supposedly thriving without were delivered most weeks. He is thriving with them. The file in this room cannot see that, because the delivery log is not the school’s document. It is yours.

On Thursday, March 12, 2026, the court review reads the agency’s report — now carrying the school’s actual records, as ordered — and the same spring is described in a different grammar: placement stable, education “a continuing concern,” a question about whether services are being delivered as written, and a judge noting that the plan at school and the plan at court still do not cite each other. Same child. Same week. Two rooms reading two subsets of one life and reaching two different conclusions, each reasonable from its own paper.

In the hallway, Ms. Okafor says the thing she has been building toward since October: “The files don’t need another correction. They need to be one file, in both rooms, at the same time. That is not a form anyone issues. That is a binder you build.”

**Choices:**
- Ask her what, exactly, goes in the binder — and what it costs → **lawyer_hinge**
  - NOTE (shown after choosing): “Everything, in order, with the dates facing outward,” she says. “It costs a weekend and some pride. It pays in rooms you haven’t entered yet.”

## [lawyer_hinge] The Binder, Specified
*Day 193 — Friday, March 20, 2026 — Friday, March 20, 2026 (dayOffset 193)*

On Ms. Okafor’s desk, the specification is a list, and the list is short enough to fit on the fridge: the agency’s file, complete, obtained in writing. The school’s file — Lincoln’s packet, Hillside’s evaluation, both plans, the sign-in sheets. Your log, promised beside delivered. And in front of all of it, one timeline: Sam’s year on a single set of dated pages, so that any stranger, in either building, can see where the stories split and where they rejoin.

“A timeline is not a summary,” she says. “A summary is an opinion with the evidence removed. A timeline is the evidence, wearing dates. When the judge reads that the invitation went to the wrong house, she should be reading it on the page where the meeting happened, in September, between the enrollment and the draft plan — not hearing it as an excuse in March.”

The March review is continued to April to let the school plan settle — a few weeks of grace with a date on it. What you build before April decides which Sam the April rooms meet: the one in their separate files, or the one in yours.

**Choices:**
- Look at the list, and at your next two weekends, and decide → **build_decision**
  - NOTE (shown after choosing): The fridge list watches you make tea. It is patient. June is not.

## [build_decision] The Weekend of the Binder
*Day 200 — Friday, March 27, 2026 — Friday, March 27, 2026 (dayOffset 200)*

It is the last weekend of March. The dollar store sells a two-inch binder, dividers, and a three-hole punch for less than a shift’s tips. Your kitchen table clears the way it did in November, for two files becoming — this time — one.

The full build is a weekend: both files complete, every gap flagged where a document should be, the timeline typed at the library, the log copied clean. A partial build is an evening: the timeline alone, from the agency’s file and your memory of the school’s. And there is the third option, the one that has been available all year: your folder, as it is — real, growing, and readable by exactly one person who already believes you.

April’s rooms will read whatever you carry into them. Choose what you carry.

**Choices:**
- Build the whole binder — both files, reconciled, with the dated timeline in front → **binder_build**  _(cash −18; FLAG: binderBuilt; HIDDEN + Binder built — agency + school files reconciled, dated timeline, services log)_
  - NOTE (shown after choosing): Two days, one blister from the hole punch, and a table of contents. It is the first complete file about Sam that exists anywhere.
- Build the timeline only — one evening, from the agency file and memory → **partial_build**  _(FLAG: timelineOnly; HIDDEN + Timeline built from agency file only; school file not reconciled into it)_
  - NOTE (shown after choosing): The dates you have are real. The school’s half of the year is in it the way September’s meeting is in the agency’s report: as an absence with a date.
- Skip it — the folder has been enough so far, and April is busy → **drift**
  - NOTE (shown after choosing): The folder is real. ‘Enough so far’ is the sentence this whole year has been quietly cross-examining.

## [binder_build] Table of Contents
*Day 207 — Friday, April 3, 2026 — Friday, April 3, 2026 (dayOffset 207)*

The binder, finished, has a plain cover and an unreasonable weight. Tab one: the timeline, four pages, every event dated twice where the systems dated it differently. Tab two: the agency’s file. Tab three: Lincoln. Tab four: Hillside — enrollment, draft plan, evaluation, new plan, sign-in sheets, your consent, your releases. Tab five: the log, promised beside delivered, September to March. Tab six: your address, filed everywhere, four stamps.

Nothing in it is new. That is its power. Every page already existed — in a drawer, a file room, a fridge, a school office, an agency queue. What did not exist, until your kitchen table, was all of it in one pair of hands, in order, with the splits showing.

You carry it to Ms. Okafor first, because April has two rooms and she has standing in one of them. She reads the timeline in silence, then says the most lawyerly sentence of your acquaintance: “Now we file it in both places, and we make them keep it.”

**Choices:**
- File a copy with the court through Ms. Okafor, and hand one to Hillside’s counselor yourself → **binder_court**
  - NOTE (shown after choosing): Two deliveries, two receipts. The binder now lives in three places, complete in all of them. Nobody in this story has ever been able to say that before.

## [binder_court] April in the Courtroom
*Day 214 — Friday, April 10, 2026 — Friday, April 10, 2026 (dayOffset 214)*

The April review is a different temperature. The judge works from the binder’s timeline because it is the only document in the room that contains both systems, and she says so, for the record: where the files disagreed, the dates resolved it; where a service was promised, the log says whether it happened; where a meeting occurred, the sign-in sheet says who was actually invited.

The agency’s report, corrected in December and now reconciled in April, recommends what the record finally supports: placement stable at Mrs. Lindqvist’s through the school year, visits expanded, your housing and coverage goals — met, documented, dated — weighed as met. The judge orders the agency to keep the binder’s timeline updated in its own file. Your kitchen table has been entered into the record of a court. It will not be the last time a judge prefers the parent’s paper; it is the first time it has happened to you.

The goal stays reunification. The question for May is no longer whether the record believes you. It is what the record now makes possible.

**Choices:**
- Ask Ms. Okafor, in the hallway, what ‘possible’ includes — before June ends the school year → **binder_school**
  - NOTE (shown after choosing): “It includes a conversation nobody schedules for parents whose files are thin,” she says. “It starts at the school.”

## [binder_school] April in the School Meeting
*Day 221 — Friday, April 17, 2026 — Friday, April 17, 2026 (dayOffset 221)*

The school’s meeting reads the same binder and reaches, this time, the same conclusions as the court — because, for the first time, it is reading the same evidence. The counselor, turning the log’s pages, goes quiet at the check-in proposal from March: the team withdraws it. Sam is thriving with the check-ins, the log shows, on the weeks they happened; the plan keeps them, staffed, with a named backup so a crisis down the hall no longer silently cancels your son.

The final plan for the year is written with the evaluation, the log, and both files open on the table. Supports as promised, delivery to be noted weekly — the school adopts your two columns as its own form, which is either flattery or surrender, and in a school office they are the same gesture. Mrs. Lindqvist signs. You sign. The sign-in sheet is full, and every name on it has read the same pages.

Sam’s year, which began as two children in two files, is now one child in one record, in three buildings. There is one decision left, and June is holding the door for it.

**Choices:**
- Go to May’s review and let the two rooms, reading one record, decide Sam’s summer → **spring_choice**
  - NOTE (shown after choosing): Same binder, both rooms. Whatever May decides, it will decide about the real Sam.

## [spring_choice] May’s Question
*Day 235 — Friday, May 1, 2026 — Friday, May 1, 2026 (dayOffset 235)*

The May review is short, because the record is no longer an argument. Your housing has held since winter — lease, receipts, dated. Your coverage plan is a written schedule with two named backups, tested on ordinary Tuesdays. Sam’s school year is stable, his plan delivered, his reading a full shelf higher than September’s. The agency supports a trial return home; the school, asked, supports it too — with a condition it writes down: if Sam comes home, he returns to Lincoln in the fall, and the handover should be a file, complete, carried in hands that know it.

The judge lays out the choice the record has earned. Trial return in June, as the school year ends — Sam home for the summer, the case open, reviews continuing, Lincoln receiving the binder as its returning-student file. Or placement through the summer for maximum stability, reunification revisited in the fall, with Sam the only child in his class whose file would survive the summer intact either way.

Both are defensible. Both are, for once, decisions about Sam rather than about his paper. The paper has done its work. The rest is parenting, which was the point of all of it.

**Choices:**
- Take the June trial return — and carry the binder to Lincoln yourself, in person → **end_reunified**  _(cash −40; FLAG: handoverReady)_
  - NOTE (shown after choosing): The binder changes hands one last time: from evidence, to inheritance.
- Choose stability through the summer — reunification in the fall, on a complete record → **end_aligned**
  - NOTE (shown after choosing): Not a refusal. A date, with a record that will keep until it arrives.

## [partial_build] One Evening’s Timeline
*Day 207 — Friday, April 3, 2026 — Friday, April 3, 2026 (dayOffset 207)*

The timeline takes an evening, and it is good work: the court side of Sam’s year, dated and ordered — removal, plan, reviews, your goals met one by one, the December correction in its place. From the agency’s file, the year coheres. A stranger could follow it, and a judge will.

The school’s half is in it the way weather is in a diary: noted where it touched the court’s paper, absent where it didn’t. The September meeting is a line — “school meeting held; mother not invited” — without the invitation, the sign-in sheet, or the draft plan attached. The delivery log is summarized in a sentence, not copied. The evaluation is cited, not included. It is a true document. It is half of one.

April will read what you carry into it. You are carrying the half that the court already half-believes, in a neater order. The half that lives at Hillside stays at Hillside.

**Choices:**
- File the timeline with the court through Ms. Okafor → **partial_court**
  - NOTE (shown after choosing): She files it without comment, which from Ms. Okafor is a comment.

## [partial_court] April in the Courtroom, Partial
*Day 214 — Friday, April 10, 2026 — Friday, April 10, 2026 (dayOffset 214)*

In court, the timeline works exactly as far as it reaches. The judge credits your progress in full — housing, coverage, visits — because every line of it is dated and checkable, and the December correction holds: nobody in this room will again describe you as a mother who did not participate. The agency’s report aligns. The review is the best you have ever had.

Then the judge asks about school — the evaluation, the plan, whether services are delivered as written — and the room goes back to summaries of summaries. The agency does not have Hillside’s file; your timeline cites documents that are not attached; the school is not in this building and cannot be cross-examined by a binder that isn’t here. The judge notes education as “improved, documentation incomplete,” and sets the next review for the summer. Reunification stays the goal. It does not get a date.

You fixed the court’s picture of you. The court was never the only room.

**Choices:**
- Take the timeline to Hillside yourself — maybe paper carried late still counts → **partial_school**
  - NOTE (shown after choosing): It counts for something. Counting is not the same as arriving in time.

## [partial_school] April at the School, Partial
*Day 221 — Friday, April 17, 2026 — Friday, April 17, 2026 (dayOffset 221)*

The counselor is glad to see you, and the meeting goes better than September’s ghost would have predicted: you are invited, you attend, your name is on the sheet. When you lay the timeline down, she reads it with respect — and then reaches, twice, for documents it mentions that neither of you has in the room: the evaluation’s full text, the delivery weeks in their original columns.

Still, the meeting is not a loss. With the evaluation open and your account dated where you have it, the team confirms Sam’s supports in full and writes the spring plan to match them. The check-in survives — barely, and without the log’s full weight behind it, the staffing fix the plan needs is noted as “to be arranged.” To be arranged is a tense. You have learned to hear it.

Sam’s schooling, as of April, is right on paper in both buildings. What remains unbuilt is the bridge: neither room holds the other’s proof, and summer — staff changes, a new year’s planning — is coming for paper that lives in single copies.

**Choices:**
- Finish the school year on a school file that finally fits Sam — and a court date in the summer → **end_split**
  - NOTE (shown after choosing): Two rooms, two decent files, no bridge. June arrives on schedule, indifferent to architecture.

## [drift] April, Unbuilt
*Day 207 — Friday, April 3, 2026 — Friday, April 3, 2026 (dayOffset 207)*

April is busy, the way Ms. Okafor predicted and the way you feared. The folder grows the way it has grown all year — a copy here, a note there, everything real, nothing reconciled. The agency has its file. Hillside has its file. You have the only set that overlaps, and it overlaps the way a junk drawer overlaps a toolbox: everything is in there, in the order it arrived, findable by exactly one person, on a good day, with time.

Mrs. Lindqvist, in the same weeks, gets news of her own: her sister, two counties away, is ill, and by summer she will need to move in with her. She tells the agency early, and tells you herself, with genuine sorrow — she has kept Sam’s drawer faithfully for eight months. Foster parents’ lives move too. That is not a failure of character. It is a fact with a date on it, arriving in a case whose paper cannot travel without hands.

A placement change means a school change, because beds and buses are married in this system. Sam’s file — all five partial copies of it — is about to be asked to move house again.

**Choices:**
- Ask the agency, in writing, what will be sent to the next school — and when → **disruption**
  - NOTE (shown after choosing): The answer, when it comes, is a familiar tense: being sent.
- Start gathering your folder into order — now, with a move coming → **disruption**
  - NOTE (shown after choosing): You start. Starting in April what September needed is its own entry in the timeline nobody is keeping.

## [disruption] The Second Move
*Day 228 — Friday, April 24, 2026 — Friday, April 24, 2026 (dayOffset 228)*

The new foster home is kind, and farther: a different neighborhood, a different elementary school — Riverbend, Sam’s third school in one school year. The move is handled gently, with a goodbye dinner and the dog photographed for Sam’s wall. The systems are gentle too, in their way: an enrollment form, signed; a records request, sent; a summary, one page, forwarded.

What Riverbend receives is what Hillside received in September: a name, a grade, a sentence about support services. Hillside’s evaluation — the winter’s work, the first complete picture of Sam since Lincoln — is in Hillside’s file, and Hillside’s file awaits a request that must name it correctly to release it correctly. The new school, friendly and busy, begins its own process: observations, reading checks, counselor time, over the coming weeks and months. Its letters will use its own words. Its picture of Sam starts, again, at two pages.

Sam, told he is changing schools again, asks whether the new teacher will know about the quiet corner. Nobody can honestly say yes. That answer is the cost of the year, itemized in one question.

**Choices:**
- Give Riverbend everything you have — the folder, the copies, all of it, in person → **reset_spring**
  - NOTE (shown after choosing): You do. It helps. A folder in arrival order, with gaps nobody flagged, helps the way a pile of bricks helps: the materials are real, and the building is not built.
- Call Ms. Okafor and ask what can still be salvaged before June → **reset_spring**
  - NOTE (shown after choosing): “His next school year,” she says. “We build for September what we didn’t build for April. It is not nothing. It is not June, either.”

## [reset_spring] May, the Third Time
*Day 256 — Friday, May 22, 2026 — Friday, May 22, 2026 (dayOffset 256)*

Riverbend is a good school. That is part of the lesson and most of the ache: the system did not fail Sam by malice in any of its three buildings. It failed him by filing — each school building an honest picture from partial paper, each picture discarded by an address change, each new picture started from two pages while the child in front of them carried the whole year in his head and his reading folder.

Riverbend’s planning meeting — you are invited; your address work held — drafts a plan from observation and the one-page summary. It is a reasonable plan for the two-page child. The small group will be “considered as the evaluation proceeds.” The evaluation proceeds over the coming weeks and months, into the summer, toward a fall you can already see: a third September, a fourth first picture.

June approaches with its unstatuted deadline. Sam will finish the year — a year in which he was evaluated completely once, planned for three times, and known fully by no single file — and the dependency case will hold its summer review with education described, accurately and terribly, as “in transition.”

**Choices:**
- Go to the summer review with your folder, and Ms. Okafor’s September plan → **end_reset**
  - NOTE (shown after choosing): The record from here is still being written. That sentence has not changed. What it costs has.

## [end_aligned] Ending — Two Files, One Child
*Day 273 — Monday, June 8, 2026 — Monday, June 8, 2026 (dayOffset 273)*

**Ending.**

**Debrief:**
- THE WHOLE BOARD: Dependency track — the case stays open with reunification as the goal and a fall date to revisit it; Sam remains with Mrs. Lindqvist through the summer by the court’s order, visits expanded. The federal clock (42 U.S.C. § 675(5)(E)) stands at roughly nine of the fifteen-of-twenty-two months: the filing point was never reached this year, and the three exceptions — relative care, a documented compelling reason, services required but not provided — were never needed, because the goal the clock points toward is the one the record now supports on a schedule. School track — the evaluation finished over the winter, the plan written from it in February and corrected in April is being delivered as written, with the school itself now logging promised beside delivered. School-year clock — Sam finishes the year at Hillside, the school he started in September: one school change this year, not two, and a file that will survive the summer because it exists, complete, in three buildings.
- WHAT THE RECORD SHOWED: The binder did the work paper can do. Built from the agency file obtained by your written request (55 Pa. Code § 3130.44(d)), the school files from both schools, your dated services log, and a single reconciled timeline, it let a courtroom and a classroom read the same child in the same week and agree. The December draft sentence that called you uninvolved was corrected by attachments, not adjectives. The March proposal to cut Sam’s check-ins died against your log. None of this was argued. All of it was filed.
- THE HONEST PART: This ending is stability, not a finish line — reunification is a fall question, and falls have their own weather. It also rested on people and luck no binder controls: a foster parent who kept copies in a drawer for you, a caseworker who amended a draft when shown dates, a counselor who adopted your two columns, a judge who preferred a timeline to a summary. A mother identical to you, with a drawer that stayed shut or a review one month earlier, ends this year in a thinner place. What your choices changed was which facts were in the rooms when the rooms decided. In this system, that is most of what anyone controls.

## [end_reunified] Ending — Home, With the Binder
*Day 280 — Monday, June 15, 2026 — Monday, June 15, 2026 (dayOffset 280)*

**Ending.**

**Debrief:**
- THE WHOLE BOARD: Dependency track — the June order returns Sam home on a trial basis as the school year ends: the case remains open, supervision and reviews continue, and nothing about this ending is a closing. The federal clock (42 U.S.C. § 675(5)(E)) never reached its fifteen-of-twenty-two filing point during the school year; no exception had to be invoked, because the permanency the clock exists to force is the one being tested at your kitchen table. Your counsel (42 Pa.C.S. § 6337) stays your counsel for the reviews ahead, and any future petition by anyone would still have to be proven by clear and convincing evidence — the record that would be read at such a hearing is the record this year built. School track — Sam finishes the year at Hillside with his plan delivered as written; in the fall he returns to Lincoln, and Lincoln does not receive a one-page summary. It receives the binder: evaluation, both plans, the log, the timeline — a handover file, carried in person, by his mother. School-year clock — June, the deadline nobody cites, is met with the file ready instead of the file pending.
- WHAT THE RECORD SHOWED: One written records request (55 Pa. Code § 3130.44(d)) produced the agency’s half; releases, a consent signed by the right parent, and an address corrected in writing in four places produced the school’s half; a correction with attachments repaired the sentence that would have followed you; a dated log turned ‘services are fine’ into a checkable claim; and a single reconciled binder made two systems reach one conclusion about one child in the same week. The trial return was not granted because a judge felt persuaded. It was granted because every fact the judge needed existed, dated, in the room, in both rooms.
- THE HONEST PART: A trial return is a test, not a trophy — the case is open, the summer is supervised, and the fall will ask its own questions, starting with whether Lincoln’s welcome matches its file. This ending also leaned on fortune: a foster parent who treated your motherhood as a fact to be filed rather than a complication, a placement that lasted the whole school year, a counselor and a caseworker who responded to paper with paper. Another mother, identical in effort, with a placement that disrupted in April, does not stand in this June. Outcomes here turn on workers, judges, timing, and luck — and on the record, which is the one item on that list that was ever yours to build. You built it like it was Sam’s, because it was.

## [end_split] Ending — Fixed at School, Open at Court
*Day 273 — Monday, June 8, 2026 — Monday, June 8, 2026 (dayOffset 273)*

**Ending.**

**Debrief:**
- THE WHOLE BOARD: School track — genuinely fixed: the evaluation is complete, Sam’s plan matches it, his supports are in place at Hillside, and he finishes the year in the school he started, with a mother whose name is on the sign-in sheet and the consent forms. Dependency track — unfinished: the summer review is pending, reunification remains the goal without a date, and your housing and coverage progress, though credited in full, now waits on a court that still describes his education as ‘documentation incomplete.’ The federal clock (42 U.S.C. § 675(5)(E)) stands at roughly ten of fifteen-of-twenty-two months — not at the filing point, but audible now in a way it was not in December, and the exceptions (relative care; a documented compelling reason; required services never provided) remain unbuilt arguments rather than documented facts. School-year clock — June is met at school and missed at court: the same month, two verdicts.
- WHAT THE RECORD SHOWED: The timeline you built in one evening did real work — it permanently corrected the court’s picture of your participation, because the agency’s half of the year, dated, is unanswerable. What it could not do was testify about documents it didn’t contain. The school’s evaluation, sign-in sheets, and delivery weeks were cited but never attached, carried, or filed in the court’s record; the court’s order was never carried into the school’s file either. Each system ended the year holding a decent, partial record — and a judge asked to set a reunification date on partial paper did what judges do with partial paper: she continued the case.
- THE HONEST PART: This is not a failure ending, and it is not a success ending; it is a map of exactly where the year’s effort stopped — at the border between two systems, with the bridge half-built. Nothing here was decided by your worth. It was decided by which documents were in which rooms in April, plus the usual silent partners: a caseworker’s queue, a judge’s caution, a school’s staffing, the luck of a placement that held. The summer review is a real second chance, and it will ask for precisely what April lacked: the whole file, in both rooms, at once. That build is still available. It is simply no longer available in time for June.

## [end_reset] Ending — The Third School
*Day 280 — Monday, June 15, 2026 — Monday, June 15, 2026 (dayOffset 280)*

**Ending.**

**Debrief:**
- THE WHOLE BOARD, IN ELAPSED MONTHS: September — Sam changes schools because his placement’s address changed; his education file is mailed to an apartment he no longer lives in. October — a planning meeting is held without his mother, from a two-page file; a thinner plan is written. November to January — the agency’s file is obtained, an evaluation is completed at the second school, a fuller plan is written in February: the year’s one complete picture of Sam, held in one building. April to May — a foster parent’s family emergency, nobody’s fault, moves Sam again; the picture stays in the second school’s file room while a third school starts over from a one-page summary, its own evaluation to run over the coming weeks and months, into the summer. June — the school year ends with Sam ‘in transition’ in every system that describes him. Dependency track — reviews held, goal unchanged, progress credited, education a standing concern; the federal clock (42 U.S.C. § 675(5)(E)) at roughly ten of fifteen-of-twenty-two months, its exceptions unbuilt. Counted honestly, the loss is not a villain or a verdict. It is nine months in which a child was fully known by no single file, and two school years’ worth of starting over inside one.
- WHAT THE RECORD SHOWED: Fragments, honestly kept by five different hands: an enrollment margin note (‘records to follow’), a draft plan in a foster parent’s drawer, an agency file obtained in writing (55 Pa. Code § 3130.44(d)) and read carefully, school papers on a fridge. What was never built was the single reconciled file — both systems, one timeline, carried into both rooms — and so each room, each time, decided reasonably from partial paper and produced, collectively, an unreasonable year. Your address corrections held (Riverbend invited you; you attended). Your counsel (42 Pa.C.S. § 6337) remains in the case, and the September build Ms. Okafor described — the binder, aimed at the fall — is real, available work with a real chance to make Sam’s next school his last new school for a long while.
- THE HONEST PART: Read the board again and notice what is not on it: a villain. A foster parent moved to care for her sister. Schools built honest pictures from the paper they had. A caseworker answered every written request. The year was lost to hand-offs — to the space between five partial files and the one pair of hands that could have joined them in time. Another mother, with a placement that lasted or a move that came in July instead of April, keeps the February plan and finishes a different June with the same folder you carried. Workers, judges, addresses, timing, and luck held most of this year. The record was the share that was yours. It still is — September is coming, and for the first time, you know exactly what to build before it arrives.
