# THE FIRST 90 DAYS — Scenario 12: “Two Homes”

*Human-readable script. This document and `scenario-12.json` are generated from a single source and match node-for-node: same IDs, same order, same choices, same effects.*

**The family is fictional — a composite. No real person's story appears here.**

**Content note:** This scenario depicts siblings placed in two different foster homes and a parent trying to get their visits coordinated. It is told through calendars, visit logs, and letters. There is no graphic content. Players may skip any scene or use the quick exit at any time.

**How to read effects:** `cash −40` changes the player's cash. `FLAG: name` sets a flag the engine tracks. `HIDDEN + item` means the case file quietly records that item at this choice — the player does not see it when it happens. `NOTE:` is text shown to the player right after choosing.

Start date: Monday, March 2, 2026. Day offsets are days since the scenario's start date. Tier: Hard.

## [start] Two Addresses
*Day 0 — Monday, March 2, 2026 — Monday, March 2, 2026 (dayOffset 0)*

Your children came into care together and were placed apart. Mara, nine, lives with the Hartleys across town, and her caseworker is Ms. Okafor. Jonah, six, lives with Ms. Bell in the next township, and his caseworker is Mr. Delgado — a different worker, in a different office, with a different calendar.

Nobody decided your children should rarely see each other. Nobody had to. Two placements, two workers, and two visit schedules were quite enough. You see each child every week. What you almost never see is both of them in the same room — and lately Mara has started asking why her brother is never at her visits, in the tone children use for questions they already suspect the answers to.

**Choices:**
- Ask both workers, this week, when the children will see each other → **calendars**  _(HIDDEN + Sibling contact — parent asked for joint visits in week one; no joint visit scheduled)_
  - NOTE (shown after choosing): Both workers say some version of 'we're working on it.' Working on it has no date.
- Focus on your own visits first — one problem at a time → **calendars**
  - NOTE (shown after choosing): Reasonable. It is also how 'later' becomes a season.

## [calendars] Two Calendars
*Day 3 — Thursday, March 5, 2026 — Thursday, March 5, 2026 (dayOffset 3)*

Ms. Okafor sends Mara's schedule: your visits Tuesdays and Thursdays, at the Hartleys', after school. Mr. Delgado sends Jonah's: Wednesdays and Saturdays, at Ms. Bell's, late morning. Sibling time, both messages say, is 'to be arranged between the placements.'

Arranged by whom is not stated. The Hartleys work weekdays. Ms. Bell cares for her mother on weekends. Each household is reasonable. Each worker is reasonable. The arrangement is nobody's job, which in practice makes it yours — except you are the one person in this case who cannot schedule anything.

**Choices:**
- Keep both calendars on the refrigerator and wait for the overlap → **first_clash**
  - NOTE (shown after choosing): You study them like a puzzle. There is no overlapping square. That is the puzzle.

## [first_clash] The Same Hour
*Day 7 — Monday, March 9, 2026 — Monday, March 9, 2026 (dayOffset 7)*

On Saturday, Jonah's visit moves to the exact hour of Mara's rescheduled Thursday visit — a dentist appointment shifted everything — and the two visits land in two towns at the same time. You cannot be in both. No one can. You choose Mara's, because Mara's was moved first, and you tell yourself Jonah is six and will not keep score.

Mr. Delgado's log for that day has one line for you: 'Mother did not attend.' It does not say where you were. Logs rarely do, unless somebody makes them.

**Choices:**
- Call Mr. Delgado from the Hartleys' driveway and explain — today, while it's fresh → **clash_noted**  _(cash -6; HIDDEN + Visit log — Jonah: mother at sibling's simultaneous visit; conflict reported by phone the same day)_
  - NOTE (shown after choosing): He is decent about it. 'I'll add a note,' he says. Notes are small. So is thread, and thread holds coats together.
- Go home and deal with it Monday — you're wrung out → **clash_plain**
  - NOTE (shown after choosing): Monday comes. The log line doesn't change. Log lines almost never do, once the day closes.

## [clash_noted] The Note in the Margin
*Day 8 — Tuesday, March 10, 2026 — Tuesday, March 10, 2026 (dayOffset 8)*

Mr. Delgado does add the note. You know because he reads it back to you: 'Mother at sibling's visit, same hour, called to explain.' Nine words. The 'did not attend' is still there — logs are additive, not corrective — but now the line has company, and company changes what a line means to the next reader.

The next reader matters. Files in this system are read by people who have never met you, in rooms you will never see, on days when you cannot speak. You are beginning to understand that you have two cases: the one you live, and the one on paper. They are supposed to be the same case.

**Choices:**
- Ask Mr. Delgado who is supposed to schedule the siblings together → **phone_tag**
  - NOTE (shown after choosing): 'Coordination,' he says, 'is usually the placing workers together.' Usually. Together. Neither word is a name.

## [clash_plain] Did Not Attend
*Day 8 — Tuesday, March 10, 2026 — Tuesday, March 10, 2026 (dayOffset 8)*

On Monday you explain, and Mr. Delgado is kind, and the kind explanation goes nowhere in particular, because the day is closed and the log is written and Monday's words have no box to live in. 'I'll keep it in mind,' he says, and you believe he means it, and you also understand that 'in mind' is not a place a court can look.

The line in Jonah's log now reads, to any future reader, like all the other lines like it in all the other files: a mother who didn't come. The fact that you were with your other child, at a visit his own agency scheduled, exists only in your memory and the Hartleys' kitchen.

**Choices:**
- Ask Mr. Delgado who is supposed to schedule the siblings together → **phone_tag**
  - NOTE (shown after choosing): 'Coordination,' he says, 'is usually the placing workers together.' Usually. Together. Neither word is a name.

## [phone_tag] Phone Tag
*Day 11 — Friday, March 13, 2026 — Friday, March 13, 2026 (dayOffset 11)*

You spend a week in the space between two offices. Ms. Okafor says sibling visits are arranged through the children's placements jointly and Mr. Delgado's office holds Jonah's transport. Mr. Delgado says transport follows the visit schedule, and the schedule is set with the placing worker — Ms. Okafor. Each statement is true. Together they describe a circle.

Meanwhile the children ask about each other in parallel, in two kitchens, and two foster mothers pass the questions along to two workers, who pass them into two files. Four adults are carrying messages between your children. Your children have not been in the same room in five weeks.

**Choices:**
- Bring the circle to your lawyer — there must be a way to make this somebody's job → **records_fork**  _(HIDDEN + Coordination — each worker attributes sibling scheduling to the other office)_
  - NOTE (shown after choosing): Your lawyer listens to the whole circle before speaking. Lawyers in this story charge by the hour and listen like it.

## [records_fork] What the File Would Say
*Day 14 — Monday, March 16, 2026 — Monday, March 16, 2026 (dayOffset 14)*

Your lawyer — appointed for you in this case, as parents in dependency cases may be (42 Pa.C.S. § 6337) — asks a question that reorders the week: 'Have you seen the visit logs? Both of them?' You have seen your own calendars. You have not seen what the agency's paper says about the last five weeks.

A party may ask, in writing, for the case record, and under the regulation it 'shall be released upon request' (55 Pa. Code § 3130.44(d)). The logs would show — in the agency's own hand — how many sibling visits were scheduled, how many happened, and what the file says about why. Paper about paper. It is how this system is audited: from inside its own handwriting.

**Choices:**
- Sign the written request for the record — both children's logs, complete → **records_arrive**  _(FLAG: recordsRequested)_
  - NOTE (shown after choosing): Signed in the lawyer's office, copied at the library. The request itself becomes a page in the file it asks about. That is normal here, and strange, and useful.
- Work from your own notebook for now — the lawyer has limited hours → **own_notes**
  - NOTE (shown after choosing): Your notebook is honest and detailed. It is also, in the language of hearings, just your word. Your word is true. That is a different property than being believed on paper.

## [records_arrive] Two Logs, Side by Side
*Day 21 — Monday, March 23, 2026 — Monday, March 23, 2026 (dayOffset 21)*

The packet arrives in a manila envelope, and you lay the two logs on the kitchen table the way you laid the calendars on the refrigerator — side by side, looking for the overlap. Mara's log: visits with you, regular, warm notes from the Hartleys. Jonah's log: visits with you, regular, one 'did not attend' with Mr. Delgado's margin note or without it, depending on a phone call you did or didn't make.

And sibling visits — the thing you actually asked about — have a section in each log, and in seven weeks the two sections contain, between them, zero entries. Not canceled ones. Not failed ones. None. The absence has a shape when you see it in the agency's own hand: it is not that joint visits went wrong. It is that they were never anybody's line to fill in.

**Choices:**
- Take the logs to the lawyer and draft the request — one letter, both workers' names on it → **draft_a**  _(HIDDEN + Sibling visits — none joint in the first seven weeks (agency's own logs))_
  - NOTE (shown after choosing): Seven weeks, zero entries, their handwriting. Some arguments you make. Some you just lay on the table.

## [own_notes] Your Notebook
*Day 21 — Monday, March 23, 2026 — Monday, March 23, 2026 (dayOffset 21)*

Your spiral notebook has every visit, every call, every 'we're working on it,' dated in your hand, going back to the first week. It is a good notebook. You show it to your lawyer, who reads two pages with genuine respect and then says the sentence that governs this entire system: 'I believe you. Now let's make it so we don't have to ask anyone else to.'

What your notebook cannot do is prove the negative in the agency's own hand — that no joint visit was ever scheduled. For that you would need their logs. What it can do is anchor a letter: dates you asked, people you asked, answers you got. A letter written from a notebook is a request. A letter written from their logs is a record correcting itself.

**Choices:**
- Draft the letter from the notebook — dates, names, and the ask, in writing → **draft_b**
  - NOTE (shown after choosing): Weaker paper, same ask. You write it that night, because the children are not getting less separate while you wait for better evidence.

## [draft_a] One Letter, Two Names
*Day 24 — Thursday, March 26, 2026 — Thursday, March 26, 2026 (dayOffset 24)*

The letter your lawyer helps you draft is one page, and it is addressed — this is the whole design of it — to Ms. Okafor and Mr. Delgado together, with a copy to each of their supervisors and one to the court file through your lawyer. It cites no law. It does something ruder: it cites the logs. 'In the first seven weeks of placement, the children's logs record no joint sibling visit. I am requesting a coordinated sibling visit, at the same time and place, weekly, scheduled jointly by both workers.'

One letter, two names, every desk at once. A circle cannot survive being written down as a circle — once the request exists on both desks on the same day, 'the other office handles it' stops being an answer either office can give.

**Choices:**
- Send it to both workers, both supervisors, and the court file — and keep your stamped copy → **response_a**  _(cash -4; FLAG: writtenRequest; HIDDEN + Written request — coordinated weekly sibling visit, sent to both workers and supervisors)_
  - NOTE (shown after choosing): Four envelopes, one morning. The post office clerk does not know she has just changed a case. Clerks rarely do. That's what stamps are for.
- Hand it to Ms. Okafor at Thursday's visit — she's the warmer of the two → **sent_one**
  - NOTE (shown after choosing): She accepts it kindly and promises to raise it. It now lives on one desk, in one file, as a favor asked — not a request pending before everyone responsible.

## [draft_b] A Letter From a Notebook
*Day 24 — Thursday, March 26, 2026 — Thursday, March 26, 2026 (dayOffset 24)*

You draft the same one page at your kitchen table: the dates you asked, the answers you received, and the request itself — a coordinated sibling visit, same time and place, weekly, scheduled jointly by both workers. Your lawyer reads it over the phone and changes only the last line: 'Please respond in writing.' Four words that turn a letter into a debt.

It is a good letter. Its weakness is not in its sentences; it is in its footings. Everything it asserts rests on your notebook, and the agency can answer a notebook with a shrug in a way it cannot answer its own logs. You send it anyway. A request on paper, even thin paper, is a different object from a request in the air.

**Choices:**
- Send it to both workers and both supervisors, with 'please respond in writing' intact → **response_b**  _(cash -4; FLAG: writtenRequest)_
  - NOTE (shown after choosing): Four envelopes. Whatever comes back — even silence — now has a date on it.
- Hand it to Ms. Okafor at Thursday's visit — she's the warmer of the two → **sent_one**
  - NOTE (shown after choosing): She accepts it kindly and promises to raise it. One desk, one file, one person's goodwill standing between your children and each other.

## [sent_one] One Desk
*Day 25 — Friday, March 27, 2026 — Friday, March 27, 2026 (dayOffset 25)*

Ms. Okafor raises it, the way she promised. You know this because she tells you she did, at the next visit, while braiding Mara's hair with the ease of a woman who has done it a hundred times. What you do not have is anything in writing: no reply, no date, no decision — because the request never formally existed anywhere except her desk and her goodwill.

Goodwill is real, and Ms. Okafor has it. But goodwill does not attend meetings, does not get copied to supervisors, and does not appear in Jonah's file at all. In his file, this week looks exactly like the last five: two separate logs, two separate children.

**Choices:**
- Wait for the reply that may come through her → **response_b**
  - NOTE (shown after choosing): It comes, eventually, in the form all single-desk requests come in: as news, not as an answer.

## [response_a] A Reply With Both Names On It
*Day 28 — Monday, March 30, 2026 — Monday, March 30, 2026 (dayOffset 28)*

The reply arrives in four days, and it is an email with both supervisors copied, which tells you before you read a word of it that the circle is broken. A coordination meeting is scheduled — both workers, both foster parents, and you, by phone — 'to establish a standing sibling visit.' The logs are mentioned. Your letter is mentioned, by its date.

Nothing in the reply apologizes, and you find you don't need it to. What you needed was for the request to become an item — a thing with a date, an owner, and a next step — in two files at once. It has. Items get minuted. Minutes get read by judges.

**Choices:**
- Join the coordination meeting by phone, notebook open → **meeting**
  - NOTE (shown after choosing): You take the call in the Hartleys' driveway before your visit, because that is where your life happens now: in driveways, between appointments, on time.

## [response_b] We'll Look Into It
*Day 28 — Monday, March 30, 2026 — Monday, March 30, 2026 (dayOffset 28)*

The reply, when it comes, is two sentences: the agency 'is looking into sibling visit coordination' and will 'advise when arrangements are finalized.' No date for a decision. No meeting. No mention of your letter's date — or, if your letter went to one desk only, no reply at all, just Ms. Okafor's kind report that it's being discussed.

'Looking into it' is where requests go to be neither granted nor denied, and the review hearing is now a month away. What is not answered in writing before a review tends to be described at the review — by whoever holds the pen that day. At the moment, that is not you.

**Choices:**
- File a second written request — short, dated, referencing the first — before the review → **push**  _(cash -4; FLAG: writtenRequest; HIDDEN + Written request — second request filed before the review, referencing the first)_
  - NOTE (shown after choosing): A second letter converts 'looking into it' into a timeline: asked, answered vaguely, asked again. Timelines are arguments that make themselves.
- Let it ride to the review — the workers mean well → **push**
  - NOTE (shown after choosing): They may. Meaning well is a quality of people. Reviews run on qualities of paper.

## [meeting] The Coordination Meeting
*Day 35 — Monday, April 6, 2026 — Monday, April 6, 2026 (dayOffset 35)*

The meeting takes twenty minutes, eight of which are spent discovering that the Hartleys cannot do Saturdays and Ms. Bell cannot do weekday evenings — the exact knot that defeated five weeks of goodwill. It is untied the ordinary way knots are: somebody proposes Sunday afternoons at the agency's visit rooms, transport split between the two offices on alternating weeks, and everybody watches it work on paper before anyone has to drive anywhere.

You say almost nothing. You don't have to. Your letter is doing the talking, the way paper does when it has been sent to everyone: it sits in the middle of the table as the reason eleven people are solving a problem that five weeks of phone calls described as unsolvable.

**Choices:**
- Confirm the plan back in writing — a short email: Sundays, visit rooms, alternating transport → **joint1**  _(cash -4; HIDDEN + Coordination meeting — standing Sunday sibling visit agreed, transport split between offices)_
  - NOTE (shown after choosing): The reply 'confirmed' takes eleven minutes. You print it at the library and put it in front of the refrigerator calendars, where this story started.

## [push] Asking Again, On Paper
*Day 35 — Monday, April 6, 2026 — Monday, April 6, 2026 (dayOffset 35)*

Your second letter is three sentences long and references the first by its date. It asks for a decision — not a visit, a decision — before the review hearing, and it goes to the same full set of desks. Short letters written second are a genre of their own: they do not argue. They count.

Whether the agency answers this one or not, the review now has a shape it didn't have before: a request, a vague reply or none, and a renewal — all dated, all in the file the judge will read. You have not gotten your children a single extra hour together yet. You have gotten something that hearings run on: a record that cannot be described as 'the parent never raised it.'

**Choices:**
- Go to Mara's visit — and tell her, carefully, that you're working on Sundays → **joint_partial**
  - NOTE (shown after choosing): You don't promise her the day. You have learned what promises cost in this system. You tell her the truth instead: it's on paper now, and paper is how things here become real.

## [joint1] Ninety Minutes, Both of Them
*Day 39 — Friday, April 10, 2026 — Friday, April 10, 2026 (dayOffset 39)*

The first joint visit is ninety minutes in a visit room with a couch, a rug, and a box of toys meant for every age and therefore perfect for none. Jonah shows Mara a loose tooth with the ceremony of a state occasion. Mara reads him a whole picture book, including the parts she is plainly making up, and he believes the made-up parts most.

At the end, neither child cries, which the visit supervisor writes down, and both workers' logs — for the first time in the case — record the same event on the same day: sibling visit, held. Two files, one afternoon. You stand in the parking lot afterward understanding that this is what coordination looks like. It looks like a room where your children already knew how to be siblings, waiting for the adults' calendars to catch up.

**Choices:**
- Drive home past both foster homes, the long way, on purpose → **strain**  _(HIDDEN + Sibling visit — first joint visit held, 90 minutes, recorded in both children's logs)_
  - NOTE (shown after choosing): The long way costs four dollars in gas you do not have and is worth it in a currency that doesn't spend anywhere else.

## [joint_partial] A Visit That Almost Happens
*Day 39 — Friday, April 10, 2026 — Friday, April 10, 2026 (dayOffset 39)*

A joint visit does get scheduled before the review — a Saturday at Ms. Bell's, arranged by phone. On the day, the transport from the Hartleys' side falls through: a car seat issue, a driver swap, a reason no one writes down because the visit was never written down. Mara joins by video call for twenty minutes, propped against Ms. Bell's kitchen fruit bowl, pixelated and brave.

Twenty minutes of video is not nothing. It is also not a visit, and in the logs it becomes one line in each file — 'sibling contact, virtual' in Jonah's, nothing at all in Mara's, because her office didn't arrange it. Even the almost-visit gets filed asymmetrically. That asymmetry is the case, in miniature, and it is now — because of your letters — a documented miniature.

**Choices:**
- Write down what happened, date it, and send it to your lawyer for the review → **strain**  _(cash -3; HIDDEN + Sibling contact — scheduled joint visit failed on transport; 20-minute video call instead)_
  - NOTE (shown after choosing): Your lawyer files it with your letters. The packet for the review is now a story with a beginning, a middle, and a missing car seat.

## [strain] A New Name on the File
*Day 45 — Thursday, April 16, 2026 — Thursday, April 16, 2026 (dayOffset 45)*

In April, Mr. Delgado rotates off Jonah's case — caseloads shift; nothing personal — and Jonah's file passes to a new worker, Ms. Pryce, who will meet your son for the first time next week. Everything Ms. Pryce will ever know about the sibling question, she will learn from the file before she learns it from any person.

This is the moment every choice you have made about paper was actually for. A worker can be told. A file can only be read. What Ms. Pryce finds — letters with dates, logs with zero entries and then entries, a meeting, a plan — or, on the thinner paths, a notebook's worth of asking that exists nowhere she can see — determines whether 'coordination' is a live item in Jonah's case or a rumor about his mother.

**Choices:**
- Prepare for the review with your lawyer — everything, in date order → **review_prep**
  - NOTE (shown after choosing): Date order. In this system, chronology is not a style. It's the argument.

## [review_prep] Paper for the Review
*Day 52 — Thursday, April 23, 2026 — Thursday, April 23, 2026 (dayOffset 52)*

The review hearing is set for Thursday, April 30, 2026. Your lawyer lays out what the judge will have: the placement summaries, two logs, and whatever your choices have added to them. 'The judge cannot order a history,' she says. 'She can only order a future. Our job is to make the history impossible to describe wrong.'

She is blunt about the limits: the hearing will not reunify the children into one home — that question isn't before the court today, and pretending otherwise wastes the credibility the paper bought. What is before the court is narrower and winnable: whether sibling contact becomes a scheduled, written, owned part of both children's plans, or stays a favor the calendar grants when it can.

**Choices:**
- Carry the full packet in — logs, letters, and the visit record → **hearing_strong**
  - NOTE (shown after choosing): The packet is not thick. Thickness was never the point. Sequence was.
- Carry yourself in — tell the judge, and let the summaries speak for the rest → **hearing_plain**
  - NOTE (shown after choosing): You know this story cold. The question the hearing will answer is whether knowing it is the same as it being known.

## [hearing_strong] The Review — One Schedule
*Day 59 — Thursday, April 30, 2026 — Thursday, April 30, 2026 (dayOffset 59)*

The judge reads the packet in the order your lawyer arranged it: two logs with seven weeks of empty sibling sections; one letter with two names on it; a meeting; a plan; a visit both logs record. The agency's counsel does not dispute any of it — it is, after all, the agency's own paper — and describes the Sunday arrangement as 'in place and working.'

'Then it can be in the order,' the judge says, in the tone of a woman concluding a sentence someone else started. She turns to you for the only question she needs answered aloud: whether Sundays at the visit rooms, transport alternating between the offices, works for you. Behind the question sits the whole case: she is not asking whether you love your children. She is asking whether the plan on paper can be made the plan in the order.

**Choices:**
- Say yes — and ask that the schedule, the place, and the transport split be written into the order itself → **end_together**
  - NOTE (shown after choosing): 'So ordered.' Two words. Your children have had longer sentences written about them; few have mattered more.
- Accept the agency's verbal assurance instead — the judge seems satisfied, and pressing feels risky → **end_visits_only**
  - NOTE (shown after choosing): The hearing ends warmly. Warmth, like goodwill, does not get copied to supervisors.

## [hearing_plain] The Review — Two Files
*Day 59 — Thursday, April 30, 2026 — Thursday, April 30, 2026 (dayOffset 59)*

Without the packet, the review is a shorter and smoother hearing. Two summaries are read: Mara, doing well; Jonah, doing well. 'Did not attend' appears once, unexplained, the way unexplained lines do — quietly, and in the direction of the parent. Sibling contact is described by counsel as 'being coordinated between the placements,' a sentence in the present continuous tense, where it has lived for two months.

The judge looks at you over the summaries. She can only order what is before her, and what is before her is two files that do not mention each other. 'Is there anything about the children's time together you'd like on the record?' she asks — an open door, and the last one in this story.

**Choices:**
- Use the door: lay out the dates from your notebook and ask for a written sibling schedule → **end_visits_only**
  - NOTE (shown after choosing): Judges remember parents who answer a direct invitation with dates. What she can do with late paper is less than what she could have done with early paper — but it is not nothing.
- Say they're working on it — you don't want to sound like you're accusing anyone → **end_drift**
  - NOTE (shown after choosing): The hearing ends in five minutes. Everyone is pleasant. Pleasant hearings are how cases drift: nothing decided, nothing denied, nothing scheduled.

## [end_together] Ending — One Calendar
*Day 66 — Thursday, May 7, 2026 — Thursday, May 7, 2026 (dayOffset 66)*

**Ending.**

**Debrief:**
- WHAT THE FILE HELD (the hidden record, revealed): The agency's own logs recorded no joint sibling visit in the first seven weeks — not a failed visit, an unscheduled one. Your written request, sent to both workers and both supervisors on the same day, converted that absence into an item with a date and owners; a coordination meeting followed; the first joint visit was then recorded in both children's logs on the same day. At the review, that sequence — absence, request, meeting, visit — is what the court ordered continued. Judges order futures, but they build them out of documented pasts.
- THE PROCESS UNDER THIS PATH (described, keeping to this scenario's verified law): You were entitled to the record you built the letter from — the case record 'shall be released upon request' (55 Pa. Code § 3130.44(d)) — and to the lawyer who helped you aim it (42 Pa.C.S. § 6337). No statute in this scenario's verified set schedules sibling visits by itself. What the law supplied was access and counsel; what you supplied was the mechanism that makes agencies move: one written request, addressed to everyone responsible at once, that no office could answer by pointing at the other. The court's order did the rest — and note what the win actually is. Your children still live in two homes tonight. What changed is that their time together is now a scheduled, written, court-ordered part of both plans, owned by named workers, instead of a favor two calendars granted when they happened to agree.
- THE HONEST PART: Another judge could have left the Sunday plan as an agency arrangement rather than an order, and a different pair of foster households could have made Sundays impossible and forced a harder negotiation. Workers rotated, transport failed once in this story's other paths, and luck — a supervisor who answered in four days — played its part. Your share was narrower and entirely real: you made the invisible problem legible, in the agency's own handwriting, early enough for a court to act on it. In the published cases this scenario is built from, courts ended up directing sibling contact themselves after long stretches in which it belonged to no one. The lesson is not that letters are magic. It is that coordination, like everything else in this system, happens on paper first or not at all.

## [end_visits_only] Ending — Visits, Unwritten
*Day 66 — Thursday, May 7, 2026 — Thursday, May 7, 2026 (dayOffset 66)*

**Ending.**

**Debrief:**
- WHAT THE FILE HELD (the hidden record, revealed): Your children are seeing each other — that part is real, and it matters to them more than any document. What the file does not hold is a schedule anyone owns: the arrangement lives in workers' intentions, foster parents' goodwill, and (on this path) a judge's recollection of a parent speaking up late. The first time a worker rotates, a car seat fails, or a household's circumstances change, the arrangement has no paper to stand on, and the five-week silence that opened this story is the documented precedent for how long 'arranged between the placements' can last.
- THE PROCESS UNDER THIS PATH (described, keeping to this scenario's verified law): Nothing about this ending is a legal defeat — no motion was denied, no right was refused. You had access to the record (55 Pa. Code § 3130.44(d)) and to counsel (42 Pa.C.S. § 6337) throughout; what varied across this scenario's paths was never the law, only how much of your asking existed in the form the system acts on. Verbal assurances from an agency are worth exactly the tenure of the person who gave them. Written requests create items; items create meetings; court orders create obligations that survive staff changes. The distance between this ending and 'One Calendar' is not effort or love — the visits happened either way. It is one envelope's worth of formality, applied early.
- THE HONEST PART: It is possible this arrangement holds for months on goodwill alone — foster parents like the Hartleys and Ms. Bell are often the load-bearing walls of these cases, and your children may never miss a Sunday. It is also possible it quietly dissolves, the way it silently didn't exist for the first seven weeks, and that a future review reads two logs that once again do not mention each other. Workers, judges, households, and luck will decide which. What this path leaves you is the knowledge — now earned — of the exact mechanism that turns goodwill into schedule, and a review cycle that comes around again. The letter can still be written. It just works better written first.

## [end_drift] Ending — Two Separate Files
*Day 59 — Thursday, April 30, 2026 — Thursday, April 30, 2026 (dayOffset 59)*

**Ending.**

**Debrief:**
- WHAT THE FILE HELD (the hidden record, revealed): Two placement summaries that do not mention each other; one unexplained 'did not attend'; a sibling relationship that exists richly in two children's lives and almost nowhere in their paperwork. Nothing in this ending was decided against you. That is precisely the problem the scenario was built to show: in a two-worker, two-placement case, the default outcome requires no one's decision. Drift is not an event. It is the absence of one — an item never created, a request never made in the form that survives the asking.
- THE PROCESS UNDER THIS PATH (described, keeping to this scenario's verified law): The system did not withhold your tools. The record was available on written request (55 Pa. Code § 3130.44(d)); counsel was available to help use it (42 Pa.C.S. § 6337); the court, at the review, expressly invited you to put the sibling question on the record. What was never supplied — by anyone, including you — was the single artifact this scenario is about: one dated, written request, sent to everyone responsible, that makes coordination a pending item in two files at once. Agencies respond to pending items. They are organized, staffed, and audited around them. A concern carried only in conversation is, administratively, a concern that has not yet been raised.
- THE HONEST PART: Your children are, by every summary, doing well in two decent homes, and their bond is being carried meanwhile by the oldest technology in this story: two kids asking about each other in two kitchens. That bond is tougher than paperwork, and it may well outlast this case. But permanency planning is done from files, and files that treat siblings as separate cases tend, over time, to produce separate plans. Workers rotate, judges read what is in front of them, and luck favors the documented. The hopeful truth inside this ending is that nothing here is final — reviews recur, and the request that would have changed this hearing can still change the next one. It is one page. It has two names on it. Now you know why both of those things matter.
