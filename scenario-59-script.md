# THE FIRST 90 DAYS — Scenario 59: “Two Buses to the Visit”

*Human-readable script. This document and `scenario-59.json` are generated from a single source and match node-for-node: same IDs, same order, same choices, same effects.*

**The family is fictional — a composite. No real person's story appears here.**

**Content note:** This scenario depicts a father whose visits with his daughter in foster care are moved to a center across the county: bus journeys, shortened visits, visit notes, and a review hearing. There is no graphic content. Players may skip any scene or use the quick exit at any time.

**How to read effects:** `cash −40` changes the player's cash. `FLAG: name` sets a flag the engine tracks. `HIDDEN + item` means the case file quietly records that item at this choice — the player does not see it when it happens. `REQUIRES FLAG: name` means the choice is only available if that flag was set earlier; `REQUIRES NO FLAG: name` means it is only available if that flag was never set. `NOTE:` is text shown to the player right after choosing.

Start date: Monday, May 11, 2026. Day offsets are days since the scenario's start date. Tier: Foundation.

## [start] The Letter About the Visits
*Day 0 — Monday, May 11, 2026 — Monday, May 11, 2026 (dayOffset 0)*

Your name is Andre. Your daughter Ruby is seven, and she is in foster care — placed before this story opens, in a home across the county from yours. Your visits with her have been the steady part of this case: Saturday afternoons at the neighborhood office, a short walk from your door, in a room Ruby knows.

The letter that arrives on Monday, May 11, 2026 is one page and entirely procedural. Because of a provider consolidation, visits are moving: starting this week, they will be held at a visitation center across the county. Same day, same time. What the letter does not mention is the journey — two buses, ninety minutes each way, with a connection that works when it works.

Nothing in the letter invites a reply. Letters like this rarely do. Whether one is sent anyway is the decision this scenario is built from.

**Choices:**
- Take the two buses to the new center for the first moved visit → **first_trip**  _(cash −12)_
  - NOTE (shown after choosing): Twelve dollars of fares for the round trip. You leave ninety minutes before the visit — the letter's own arithmetic, done by you, at your kitchen table.

## [first_trip] Two Buses, Ninety Minutes
*Day 5 — Saturday, May 16, 2026 — Saturday, May 16, 2026 (dayOffset 5)*

The first trip teaches you the route's true shape. The first bus is fine. The connection is not: it leaves as your bus arrives, and the next one costs you twenty minutes you had already spent twice in your head. You reach the center on Saturday, May 16, 2026 twenty minutes after the visit was to start, having left home ninety minutes early.

The visit is shortened by exactly the lateness. Ruby takes it the way seven-year-olds take shortened things — completely, and then, because she is Ruby, she gets on with the visit there is. You sign the center's sign-in sheet on the way in. Its clock says what time you arrived. It does not say when you left home, or why the road took what it took.

**Choices:**
- Sign in, take the visit there is, and keep the transfer stubs in your pocket → **note_exists**  _(HIDDEN + Visit note — ‘father arrives late; visit shortened’)_
  - NOTE (shown after choosing): The stubs go in your pocket out of habit. Habits like that are about to matter more than they should have to.

## [note_exists] Father Arrives Late
*Day 6 — Sunday, May 17, 2026 — Sunday, May 17, 2026 (dayOffset 6)*

Days later, you hear the first visit described the way the file describes it, in the note that follows the visit: “father arrives late; visit shortened.” Four words of arrival, one of consequence. No letter, no move, no buses, no ninety minutes — a note about a man who was late, written about a journey it does not mention.

The note is not false. You did arrive late, and the visit was shortened. It is simply the journey with the journey removed — and a file, read over months, becomes the notes it is made of. Future readers will meet this sentence before they ever meet you.

The move can still be answered — in writing, asking for a nearer site or for transportation support, on paper where answers live. Or it can be absorbed, Saturday by Saturday, one shortened visit at a time.

**Choices:**
- Decide how to answer the move — on paper, or not at all → **split_request**
  - NOTE (shown after choosing): Not at all is also an answer. It is the one the file is currently assuming you gave.

## [split_request] Answer the Move, or Absorb It
*Day 7 — Monday, May 18, 2026 — Monday, May 18, 2026 (dayOffset 7)*

A written answer is a small, plain thing: a dated letter or email to your caseworker and the center, saying the visits moved, what the new journey takes — two buses, ninety minutes — and asking for a nearer site or for transportation support. It does not refuse anything. It does not threaten anything. It puts the journey into the same file that currently holds only the arrival.

Absorbing it is also plain: leave earlier, run the same buses, say nothing on paper, and let the notes keep their four words. The visits will happen either way. What differs is what the review, months from now, will be able to read about why they started late.

**Choices:**
- Answer the move in writing — nearer site or transportation support, asked for on paper → **written_track**  _(cash −12; FLAG: visitMoveAnswered; HIDDEN + Visit move — answered in writing; nearer site or transportation support requested)_
  - NOTE (shown after choosing): Dated, copied, kept. Twelve more dollars of fares take you to the second visit — the asking and the going now travel together.
- Absorb it quietly — leave earlier and say nothing on paper → **quiet_track**  _(cash −12)_
  - NOTE (shown after choosing): Twelve dollars of fares, an earlier alarm, and no letter. The journey gets longer and the file stays exactly as short as it was.

## [written_track] Asked, on Paper
*Day 9 — Wednesday, May 20, 2026 — Wednesday, May 20, 2026 (dayOffset 9)*

Your letter goes in this week, and the reply, when it comes, is honest about the system's shape: the consolidation is provider-wide, your request is noted, and a nearer site or support will be “considered as capacity allows.” No change is promised. No date is given.

And yet the file is different tonight than it was last week. It now contains two documents about Saturdays: a note that says you arrive late, and a dated letter that says what arriving now requires and what you asked for. Reviews are where documents like those meet. They have not met yet.

**Choices:**
- Go to the second visit — and pay attention to the sign-in sheet this time → **log_beat**
  - NOTE (shown after choosing): The center's sheet records arrivals to the minute. Minutes, it turns out, can be evidence — if anyone keeps them.

## [quiet_track] The Same Trip, Quietly
*Day 9 — Wednesday, May 20, 2026 — Wednesday, May 20, 2026 (dayOffset 9)*

You leave earlier. The buses do not reward it reliably — connections keep their own counsel — and the second Saturday's journey takes what it takes. Nothing about the trip is written anywhere except the stubs in your pocket and the sign-in sheet at the other end.

Quiet has a cost structure of its own: it costs nothing today, in nerve or postage, and it charges later, in a room where the only account of your Saturdays is a column of arrival times with no journey attached to any of them.

**Choices:**
- Go to the second visit — and pay attention to the sign-in sheet this time → **log_beat**
  - NOTE (shown after choosing): The sheet is by the door, with its clock and its ruled lines. It has been recording your case all along. The question is whether you start keeping a copy of its story.

## [log_beat] The Sign-In Sheet
*Day 12 — Saturday, May 23, 2026 — Saturday, May 23, 2026 (dayOffset 12)*

The second visit, Saturday, May 23, 2026: the journey runs long again — not by your choosing, which is rather the point — and you sign in below the other names, at the time the center's clock gives you. The sheet is a plain document: names, times, a column for the room. It will be filed. It is, whether anyone calls it this, the center's own record of what the move costs.

You can start keeping your own arrival log — photograph the sign-in sheet each visit, note your departure time and the buses, keep the stubs — so that arrival times someday sit beside journey times. Or you can sign, go in, and spend the visit being a father instead of a filing system, which is also a completely understandable choice, and the one the file is quietly counting on.

**Choices:**
- Photograph the sign-in sheet and start a dated arrival log — departures, buses, arrivals → **third_visit**  _(FLAG: arrivalLog; HIDDEN + Arrival log — sign-in times photographed; departures and buses logged by father)_
  - NOTE (shown after choosing): Thirty seconds with a phone, at a door, each Saturday. The log is boring. Boring, dated, and yours — the three qualities exhibits are made of.
- Sign in and go straight in — the visit is the point, not the paperwork → **third_visit**
  - NOTE (shown after choosing): The visit is the point. It is also, in note form, the only part of the day the file will describe as shortened — and the log is the only version of the journey that would ever be attached to it.

## [third_visit] The Third Saturday
*Day 19 — Saturday, May 30, 2026 — Saturday, May 30, 2026 (dayOffset 19)*

The third visit, Saturday, May 30, 2026, runs the way the route runs: a connection missed or made by minutes, an arrival after the start, a visit shortened by the difference. If you are keeping the log, this Saturday's page joins the others — departure, buses, sign-in time, each dated, none of them argued about.

Ruby has started managing the shortened visits the way she manages everything: completely, and then practically. She has a order she does things in now, so the important things happen first in case the end comes early. It is a sensible system. It is also a sentence no parent should have to watch a seven-year-old invent, and the file's version of its cause is still four words long: father arrives late.

**Choices:**
- Pay the third trip's fares into the same pocket as the stubs, and go home the long way → **pattern_note**  _(cash −12)_
  - NOTE (shown after choosing): Twelve dollars, third time. The fares are the move's real price list, and so far you are the only one keeping it.

## [pattern_note] Three Times, One Word
*Day 23 — Wednesday, June 3, 2026 — Wednesday, June 3, 2026 (dayOffset 23)*

The pre-review summary arrives, and your Saturdays are in it as a pattern now: three visits, each described with the same word. Late. Late. Late — shortened, shortened, shortened. Patterns in summaries are how single notes grow into character, and character is how summaries get used at reviews.

The summary does not mention the letter that moved the visits, because the summary was written from the notes, and the notes never mentioned it either. A pattern built from arrivals alone is now the official shape of your effort — unless the underlying documents are ever put beside it.

The visit notes themselves — the center's own pages, with their recorded times — are part of your case record. You have not seen them. You could.

**Choices:**
- Ask how to get the visit notes themselves, in writing → **records_fork**
  - NOTE (shown after choosing): Not the summary of the notes. The notes — the center's own times, in the center's own hand, for all three Saturdays.

## [records_fork] Ask for the Notes
*Day 25 — Friday, June 5, 2026 — Friday, June 5, 2026 (dayOffset 25)*

The request is yours to make: ask, in writing, for the visit notes from your case record. Under 55 Pa. Code § 3130.44(d), the record is to be released on request — the material “shall be released upon request” — and visit notes are the record of the very Saturdays the summary has been describing in one word.

Or you can go to the review armed with the summary and your own account of the buses, and ask the room to take the journey on your word, against the pattern on its paper.

**Choices:**
- Request the visit notes in writing — all three visits — and keep a copy of the request → **notes_arrive**  _(cash −3; FLAG: recordsRequested)_
  - NOTE (shown after choosing): Three dollars of copies across the errand. The notes, when they come, will be the center's own account — which is exactly why they are worth requesting.
- Work from the summary — you know what the notes will say → **no_notes**
  - NOTE (shown after choosing): You know what you lived. What the notes say — their exact times, their exact words — is a different piece of knowledge, and reviews run on the second kind.

## [notes_arrive] The Center’s Own Times
*Day 30 — Wednesday, June 10, 2026 — Wednesday, June 10, 2026 (dayOffset 30)*

The notes arrive, and you read them with the letter open beside them. The center recorded what it records: scheduled starts, sign-in times, shortened endings — arrivals twenty, fifteen, and eighteen minutes after the start, across the three Saturdays, each one dated, each one in the center's own hand.

Read alone, they are the pattern. Read beside the move letter of Monday, May 11, 2026 and your log — departures ninety minutes before each start, buses, connections — they become something else: the system's own measurements of the journey the system imposed. The center timed your lateness very carefully. It is only fair that its times be allowed to testify about the whole trip.

**Choices:**
- Put the notes with the letter and the log, in date order → **prep**  _(HIDDEN + Visit notes — center’s recorded arrival times obtained and kept with the move letter)_
  - NOTE (shown after choosing): Letter, log, notes. Three documents, three different authors, one journey. Assembled, they are the first complete account of your Saturdays anyone has made.

## [no_notes] Summaries of Summaries
*Day 30 — Wednesday, June 10, 2026 — Wednesday, June 10, 2026 (dayOffset 30)*

Without the notes, the review will be a meeting about a summary of notes you have never seen — their times summarized into a word, the word repeated into a pattern, the pattern carried into a room as your record. At each step the journey fell away, because at each step the journey was in nobody's document.

You still know it by heart: the departure times, the connection, the clock over the sign-in sheet. Knowledge by heart is real knowledge. It is just not the kind that gets photocopied for a review packet.

**Choices:**
- Turn to preparing for the review, with what you have → **prep**
  - NOTE (shown after choosing): What you have is true, warm, and unattached. The review is the kind of room that attaches things or it does not weigh them.

## [prep] One Packet, in Date Order
*Day 36 — Tuesday, June 16, 2026 — Tuesday, June 16, 2026 (dayOffset 36)*

Preparation is assembly: the move letter with its date, your written answer if you sent one, your arrival log if you kept one, the center's notes if you requested them. In date order they make a single argument without raising their voice: the visits moved on this date; the journey became this; the arrivals became that; here is every document, including the system's own.

Or the Saturdays can be carried in as a story — a father, two buses, a little girl with an order she does things in. It is a story that deserves a better room than the one it is about to be told in, because that room runs on packets.

**Choices:**
- Assemble the packet — letter, written answer, log, and notes — in date order → **packet_ready**  _(cash −4; FLAG: reviewPacket; HIDDEN + Review packet — move letter, written answer, arrival log, and visit notes in date order)_
  - NOTE (shown after choosing): Four dollars of copies. The packet's first page is the move letter — because chronology is the argument, and chronology starts there.
- Bring the story and the stubs — the room should hear it from you → **story_only**
  - NOTE (shown after choosing): The stubs are real, and in a pocket they are almost documents. In a packet they would have been pages. The distance between those two is this scenario's whole geography.

## [packet_ready] Letter, Log, and Notes
*Day 38 — Thursday, June 18, 2026 — Thursday, June 18, 2026 (dayOffset 38)*

The packet is not thick. It does not need to be. Its power is sequence: a one-page letter moves a visit; a dated reply answers the move; a log records the journeys; the center's own notes record the arrivals; and the summary's one word — late — is left sitting on top of four documents that explain it more completely than it explains itself.

Your lawyer, reading it through, taps the move letter once. “Everything after this page is a consequence of this page,” she says. “Tomorrow we just ask the record to admit it.”

**Choices:**
- Make a copy for the folder, and go home the long way one more time → **review_eve**
  - NOTE (shown after choosing): Ninety minutes home, the route the packet is about. Tomorrow, for once, the journey gets described by the people who made it — on paper, in order.

## [story_only] What He Knows, Unwritten
*Day 38 — Thursday, June 18, 2026 — Thursday, June 18, 2026 (dayOffset 38)*

You know your Saturdays completely: when you leave, which connection fails, the clock over the sign-in sheet, Ruby's order of important things. The knowledge is exact, lived, and entirely in one person's keeping — yours.

Tomorrow it will be offered, out loud, against a printed pattern. Rooms like tomorrow's do not doubt fathers like you, particularly. They simply have a rule they cannot say out loud: what is not in the packet is, for the record, a claim; and claims are weighed against documents the way voices are weighed against clocks.

**Choices:**
- Get the fare ready for the morning, and go to bed early → **review_eve**
  - NOTE (shown after choosing): Early bed, early bus — the disciplines of a man whose file says the opposite of his alarms. Both facts will be in the room tomorrow. Only one of them is printed.

## [review_eve] The Night Before the Review
*Day 41 — Sunday, June 21, 2026 — Sunday, June 21, 2026 (dayOffset 41)*

The night before the review, your lawyer goes through the materials with you one last time. You have counsel because the law provides for it in these cases, and for appointed counsel if a parent cannot afford one (42 Pa.C.S. § 6337); her job tomorrow is to make the record describe a journey instead of a trait.

“Late,” she says, “is a conclusion. Tomorrow we find out whether the record underneath it gets read — the letter, the log, their own times — or whether the conclusion gets to keep standing in for all of it.”

**Choices:**
- Take the folder and the morning fare, and go to the review → **review**
  - NOTE (shown after choosing): The folder, the fare, and the earliest bus there is. Some preparations are paper. Some are just mornings, made on purpose.

## [review] The Review
*Day 42 — Monday, June 22, 2026 — Monday, June 22, 2026 (dayOffset 42)*

The review on Monday, June 22, 2026 takes up your visits in their summary form: a pattern of lateness, three shortened visits, a concern noted about consistency. The words are read aloud in the level tone of people reading weather.

Then your lawyer asks that the underlying documents be put beside the summary — the move, the answer, the journeys, the center's own times — before the pattern is adopted as your record. What happens next depends, with a precision this scenario has been honest about since the first bus, on what your choices actually put in her hands.

**Choices:**
- Present the packet — the move letter, the written answer, the arrival log, and the center’s own notes → **end_win**  _(REQUIRES FLAG: visitMoveAnswered; REQUIRES FLAG: arrivalLog; REQUIRES FLAG: recordsRequested; REQUIRES FLAG: reviewPacket)_
  - NOTE (shown after choosing): Chronology does the arguing: first the move, then the asking, then the journeys, then their own times. The pattern is re-read in the room, in order.
- Present what you have — part of the packet, without the full sequence → **end_lose**
  - NOTE (shown after choosing): Part of a chronology is a story with its first page missing. The summary, whole and printed, has no missing pages.
- Tell the Saturdays as a story — the departures, the buses, Ruby’s order of things → **end_lose**
  - NOTE (shown after choosing): It is the truest telling in the room. The pattern across the table is the printed one, and printed things are what reviews adopt.

## [end_win] Ending — On Time, On Record
*Day 45 — Thursday, June 25, 2026 — Thursday, June 25, 2026 (dayOffset 45)*

**Ending.**

**Debrief:**
- WHAT THE FILE HELD (the hidden record, revealed): A complete chronology, written by four different hands: the move letter of Monday, May 11, 2026 relocating the visits across the county; your dated written answer asking for a nearer site or transportation support; your arrival log — departures, buses, stubs — kept from the second visit on; and the visitation center's own notes, obtained on request, recording the arrivals its move produced. At the review, the pattern was re-attributed on the record: the lateness belonged to the move, not to the father. Visits were ordered to a nearer site for the next cycle, with transportation support in the meantime, and the note language was corrected to carry the journey with the arrival.
- THE PROCESS UNDER THIS PATH (described, keeping to this scenario's verified law): The instruments were the verified ones. The visit notes were part of your case record, released on request (55 Pa. Code § 3130.44(d)) — requesting them is what turned the center's times into evidence for the journey instead of only against the arrival. Counsel (42 Pa.C.S. § 6337) presented the packet in sequence. The rest was generic process, done early and on paper: a move answered in writing while it was still new, and a log kept from the second visit, when the log-keeping was still a choice. Nothing here required the center or the agency to have acted in bad faith — only that consequences, to be weighed fairly, have to be documented by someone. This time, they were.
- THE HONEST PART: Label this win honestly — it is partial. Ruby is still in foster care tonight; this ending moves visits, not custody, and the three shortened visits already happened: that time with her is not returned by any order, and Ruby's careful order-of-things will take longer to unlearn than it took to learn. A different reviewer might have noted the journey and kept the far site anyway; a center whose sign-in times were sloppier would have given the packet less to work with. Workers, centers, reviewers, and bus connections all held pieces of this. Your share was the paper: you answered a one-page letter with a dated letter, and then you kept the receipts of every journey the letter imposed. On the record now, you were on time where it counts — in the documents, in order, from the first week.

## [end_lose] Ending — Late, As Recorded
*Day 45 — Thursday, June 25, 2026 — Thursday, June 25, 2026 (dayOffset 45)*

**Ending.**

**Debrief:**
- WHAT THE FILE HELD (the hidden record, revealed): Three notes and a summary: “father arrives late; visit shortened,” repeated into a pattern, and read at the review as a concern about consistency. The move letter is in the file too — filed, unanswered by you, and unconnected to the notes by any document: no dated request, no arrival log, no visit notes obtained and put beside the summary. Your account at the review was detailed and, in the way of unaccompanied accounts, believed personally and adopted never. The far site stands. The shortened visits continue. The pattern now has the review's weight behind it, available to every future reader as the settled shape of your Saturdays.
- THE PROCESS UNDER THIS PATH (described, keeping to this scenario's verified law): The tools existed from the first week, and they are the verified ones plus one habit. Answer the move in writing — a nearer site or transportation support, asked for on paper, so the asking has a date. Keep an arrival log, so journey times exist beside arrival times. And request the visit notes, which as part of your case record are released on request (55 Pa. Code § 3130.44(d)), so the center's own times can be read beside the letter that caused them; counsel (42 Pa.C.S. § 6337) can then present a chronology instead of a claim. None of this guarantees a nearer site. It guarantees the review must describe a journey before it may describe a trait — and in this ending, no one made it.
- THE HONEST PART: The record's sentence is not a verdict on you as a father, and this debrief will not pretend it is a fair summary of you either: you left ninety minutes early, paid the fares three times over, and showed up — across a county, on two buses — for every visit there was. The system moved the room and then recorded the journey as a flaw in the traveler, because arrivals are timed by clocks and journeys are only recorded by the people who make them. A different center might have written the move into its own notes; some do. This one timed instead. What remains yours is portable: the next visit can be logged, the move can still be answered in writing, and a log begun next Saturday is worth more at the next review than this paragraph's fairness. Late, as recorded, is a description of a file. It was never a description of the effort.
