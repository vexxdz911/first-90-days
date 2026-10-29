# THE FIRST 90 DAYS — Scenario 44: “The Morning Test”

*Human-readable script. This document and `scenario-44.json` are generated from a single source and match node-for-node: same IDs, same order, same choices, same effects.*

**The family is fictional — a composite. No real person's story appears here.**

**Content note:** This scenario depicts an investigation involving a drug screen and a prescription — a kitchen accident, phone calls, letters, and paperwork. There is no graphic content. Players may skip any scene or use the quick exit at any time.

**How to read effects:** `cash −40` changes the player's cash. `FLAG: name` sets a flag the engine tracks. `HIDDEN + item` means the case file quietly records that item at this choice. `REQUIRES FLAG: name` means the choice is only available if that flag was set earlier.

Start date: Monday, September 14, 2026. Day offsets are days since the scenario's start date.

## [start] The Kettle
*Day 0 — Monday, September 14, 2026 (dayOffset 0)*

Ray Kaczmarek works nights at the warehouse, eleven to seven, and Saturday mornings are a country he crosses carefully: home at seven-thirty, Molly up at eight with cartoons and the confidence of a six-year-old who owns the remote, kettle on for tea, couch for 'ten minutes.'

The kettle boiled dry. That is the whole event, and its smell — hot metal, scorched steam — is what woke him, twenty minutes into the ten, with Molly unconcerned on the rug three feet away, narrating a cartoon. No fire. No smoke but a wisp. A burner left on low under an empty kettle, a sleeping man, a child who told her teacher about it on Monday with a storyteller's completeness: 'Daddy fell asleep and the stove was on and it smelled like burning.'

Children's sentences do not include the word 'low,' or 'twenty minutes,' or 'three feet away.' Files built from children's sentences inherit the omissions. By Monday afternoon, the agency has called: a report, an investigation, a worker — Ms. Vance — and an interview.

**Choices:**
- Write Saturday down tonight — times, burner, kettle, Molly's rug — while it's still a memory and not yet a summary → **c2**  _(FLAG: timelineWritten)_
  - NOTE (shown after choosing): 7:30 home. 8:05 kettle. 8:25 the smell. Three times and a distance. Investigations run on exactly this fuel, and it evaporates by the day.
- Explain it to Molly's mother on the phone until it sounds small → **c2**
  - NOTE (shown after choosing): It is small. Small, retold, becomes a summary; summaries are how small things get filed at full size.

## [c2] The Ask
*Day 1 — Tuesday, September 15, 2026 (dayOffset 1)*

Ms. Vance is direct on the phone, and her directness contains the case's hinge: alongside the interview, the agency asks Ray to take a drug screen. It is a routine ask in reports that mention a sleeping adult — the file wants to know whether the sleep was chemistry.

Ray's sleep was shift work. But his file at the pharmacy contains something the screen will find: a medication, prescribed by Dr. Amponsah after the back injury in March, taken as directed, refilled monthly — and squarely on the list of substances a standard screen flags. A positive result is not a possibility. It is a scheduled event, three days after the cup.

A result, in a file, is a fact with a date. An explanation is a document that either predates it or chases it. The whole case is a race between a letter and a lab.

**Choices:**
- Decide the letter gets requested today — before the screen is even scheduled → **records**  _(FLAG: letterRequestedEarly)_
  - NOTE (shown after choosing): Prescribers' offices write letters at office speed. Labs report at lab speed. The race is winnable only if it starts now, before anyone says the word 'positive.'
- Take the screen first and explain when you see the result → **records**
  - NOTE (shown after choosing): Explanation-after-result is the natural order of conversations and the losing order of files. Results are read as facts; explanations after them are read as responses.

## [records] What the File Says So Far
*Day 2 — Wednesday, September 16, 2026 (dayOffset 2)*

Ray requests the record: the intake summary, released on request under 55 Pa. Code § 3130.44(d). It is one paragraph, and the paragraph's last phrase is the one that matters: 'Father asleep while stove in use; child, 6, unsupervised in kitchen area; possible impairment to be assessed.'

Possible impairment. The screen exists because of that phrase — and the phrase exists because a six-year-old's sentence had no room in it for 'low,' 'twenty minutes,' or 'three feet.' The file is not lying. It is doing something more dangerous: compressing, in the direction of concern.

What answers compression is not indignation. It is the uncompressed record — Saturday's timeline, the work schedule that explains the sleep, and the prescriber's letter that explains the screen before the screen explains itself.

**Choices:**
- File the written request and mark the phrase: 'possible impairment' is the claim the letter must pre-answer → **nb**  _(FLAG: recordsRequested ; HIDDEN + Records — parent obtained the intake summary and identified the impairment characterization the screen is meant to test)_
  - NOTE (shown after choosing): A claim identified is a claim that can be answered in advance. The prescriber's letter now has an addressee: that phrase, in that file, before Thursday.
- Skip the summary — you were there, you know what happened → **nb**
  - NOTE (shown after choosing): You were. The file wasn't. The file was at an intake desk, being written from a child's sentence, in the direction of concern.

## [nb] Saturday, Reconstructed
*Day 3 — Thursday, September 17, 2026 (dayOffset 3)*

The corroboration assembles quietly. The warehouse schedule: Friday night, eleven to seven, badge-out at 7:04 a.m. — Ray's sleep has a timesheet. Mr. Ashford, next door, heard the kettle's whistle die and smelled the scorch through the shared wall at about 8:25, and knocked — a fact with a witness. Molly's cartoons have a timestamp in the streaming history, for whatever a file makes of such things.

And the pharmacy printout: fills, monthly, regular as rent, since March — a document that proves a prescription exists and says nothing about why, at what dose, under whose direction, or whether the prescriber knows about the warehouse, the couch, or the kettle.

A printout is a fact looking for its interpreter. The interpreter is a letter, and letters take days.

**Choices:**
- Assemble it all: schedule, timeline, Ashford's statement, the pharmacy printout — and note what's missing: the letter → **prep**  _(FLAG: proofGathered ; HIDDEN + Proof — work schedule, timeline, neighbor statement, and pharmacy printout collected)_
  - NOTE (shown after choosing): Four documents and a hole shaped exactly like a prescriber's signature. The hole is the case. Everything else is scenery the letter will stand in front of.
- Decide the printout speaks for itself — it has the medication's name and the dates, right there → **prep**
  - NOTE (shown after choosing): It speaks, in the flat voice of a database. What it says is: this substance, this man, monthly. Files complete such sentences themselves, in the direction of concern.

## [prep] The Letter, Requested
*Day 4 — Friday, September 18, 2026 (dayOffset 4)*

Dr. Amponsah's office, reached Tuesday, is willing and slow: the letter — prescribed medication, dose as directed, treatment since March, no impairment concerns, patient compliant — will be ready 'by the end of the week.' The screen, Ms. Vance mentions in the same hour, can be taken Thursday, with results in about three days.

The arithmetic assembles itself into the case's second hinge: if the letter is filed before the result posts, the result arrives pre-explained, a lab value with its context already in the folder. If the result posts first, the letter becomes a rebuttal, and rebuttals in files are read the way apologies are — noted, and weighed against the fact they chase.

Office speed versus lab speed. The race is not Ray's to schedule — but it is his to enter early, requesting, reminding, and, if necessary, collecting the letter in person with a folder in his hand.

**Choices:**
- Press the office, politely and daily: collect the letter in person the day it's ready, and file it with the packet before Thursday → **eve**  _(FLAG: packetReady ; HIDDEN + Proof — prescriber's letter obtained and assembled with the packet before the screen result)_
  - NOTE (shown after choosing): It comes out Wednesday, signed, complete: medication, dose, direction, March, compliant. The packet is whole — Saturday, the schedule, the neighbor, the printout, and now the interpreter. Its entire remaining job is to arrive before a lab does.
- Let the office mail it — end of the week is soon enough → **eve**
  - NOTE (shown after choosing): Mail is a vehicle. So is a lab result. Only one of them is racing you.

## [eve] Molly's Teacher
*Day 5 — Saturday, September 19, 2026 (dayOffset 5)*

Ms. Kowalczyk calls Wednesday evening, careful and kind: she made the report, as she's required to, and she's been thinking about Molly's sentence all week. 'She also said you snore funny,' the teacher offers. 'That part didn't go in.'

It is a small mercy and a perfect diagram of the whole system: the sentence that went in was the alarming clause; the sentence that stayed out was the child. Files are built from clauses. Families live in whole sentences.

Tomorrow is the screen, and the interview after it. Ray's folder holds the whole sentence now — if it is carried into the room and filed, in time, in the right order. Order is the last variable, and tomorrow decides it.

**Choices:**
- Write the teacher's words into the timeline tonight — the snore, dated, beside the kettle → **gate**  _(FLAG: teacherNote)_
  - NOTE (shown after choosing): Humor is not evidence. But a file that contains the whole child — snore and all — is a file that has been near the truth, and readers can tell.
- Thank her and let the clause stand as the record of Saturday → **gate**
  - NOTE (shown after choosing): The clause will stand wherever wholes aren't filed. Tomorrow's room is where filing happens.

## [gate] The Screen
*Day 6 — Sunday, September 20, 2026 (dayOffset 6)*

Thursday. The collection site has the beige calm of all such places. Ms. Vance meets Ray there with the file, and the file — as of this morning — contains an intake summary with 'possible impairment' in it and nothing else of Ray's.

The cup is filled. The lab's clock starts: about three days. And in Ray's folder, if the week was run right, is a packet with a prescriber's letter in it — a document that can be filed now, today, before any result exists, so that when the result posts it posts into a file that already knows what it means.

Or the packet can be described, promised, mailed, or held for a better moment. Files are indifferent to intentions. They are exquisitely sensitive to order.

**Choices:**
- Hand Vance the packet now — letter on top — before the result exists anywhere → **w1**  _(REQUIRES FLAG: packetReady)_
  - NOTE (shown after choosing): She takes it, reads the letter standing in the beige room, and writes the sentence the whole week was for: 'Prescriber letter filed [today's date], prior to screen result.' Prior to. Two words, in ink, that the lab cannot outrun.
- Hand her the printout and explain the prescription fully, out loud — the letter, you say, is coming → **m1**  _(HIDDEN + Response — parent provided the pharmacy printout and explained verbally; prescriber's letter not yet filed)_
  - NOTE (shown after choosing): She writes: 'Father reports prescribed medication; documentation to follow.' The printout is filed. The explanation is a summary. The letter is a promise. Three different species of paper, racing one lab.
- Decline the screen — you're prescribed, you're tired of being tested, and refusal is your right in an investigation → **h1**
  - NOTE (shown after choosing): She notes the refusal without heat, which is the coldest way to note anything. The file's phrase — 'possible impairment' — has just lost its only scheduled contradiction.

## [w1] Filed Before the Result Exists
*Day 8 — Tuesday, September 22, 2026 (dayOffset 8)*

The interview follows, and it is a different interview than the summary promised: with the letter in the file, 'possible impairment' is a phrase being retired in real time. Vance works through Saturday with the timeline open — badge-out 7:04, kettle 8:05, Ashford's knock at 8:25 — and the account she writes is the account the documents dictate: a night-shift worker, a twenty-minute nap, a dry kettle, a child three feet away, a neighbor at the wall.

She is not charmed into this. She is documented into it, which is more durable.

What remains is the lab. In three days a result will post that says, in its entirety, one word and a substance name. The file it posts into already contains the letter. Order, achieved, does its silent work.

**Choices:**
- Ask her to confirm in the file that the packet was filed today — date, contents, letter first → **w1b**  _(FLAG: filingConfirmed)_
  - NOTE (shown after choosing): Confirmed, in writing, in the file: packet received, letter noted, date entered. When the result posts, its reader will meet the letter first. Readers read files front to back. Ray has arranged to be read in the right order.
- Thank her and trust the folder's journey → **w1b**
  - NOTE (shown after choosing): Folders journey at the speed of offices. Confirmations travel at the speed of ink. The difference matters exactly once — in about three days.

## [w1b] Three Days
*Day 9 — Wednesday, September 23, 2026 (dayOffset 9)*

The three days are ordinary, which is to say they are surveilled by their own participant: Ray sleeps after shifts with the door open and one ear up, the way he always has and now notices. Molly retells Saturday to her grandmother with the snore promoted to the lead role. The file, across town, waits for a lab the way a held breath waits.

On the third day, the result posts. In another version of this week — one where the letter is in an envelope, in a mail truck — the result posts into a summary and a promise, and becomes the file's biggest fact.

In this file, it posts into a letter that has been sitting in front of it for three days, patient as paper. Watch what it becomes.

**Choices:**
- Call Vance and ask for the result — and for how it will be recorded → **w2**
  - NOTE (shown after choosing): Asking is not anxiety. It is the last step of the strategy: verify that the order held, in the file, in writing — because a race isn't won until the finish is recorded.
- Wait for the agency to call you — good news travels on its own schedule → **w2**
  - NOTE (shown after choosing): All news travels on the file's schedule. Verifying the recording is how a parent attends the finish line of a race he ran all week.

## [w2] Positive, With a Footnote Already There
*Day 11 — Friday, September 25, 2026 (dayOffset 11)*

The result is positive — for the prescribed substance, at levels the lab reports flatly. And the file note that records it is the whole story of the week in two lines: 'Screen positive for [prescribed medication]. Prescriber letter on file (filed prior to result) confirms medication prescribed since March, taken as directed; no impairment concerns per prescriber.'

Positive, and explained, in the same breath, by a note written by the agency itself. There is nothing to rebut, because nothing was ever asserted. The lab value never got to be the file's biggest fact; it got to be a footnote to a letter.

Vance's remaining questions are housekeeping: the determination will be that the report is not supported, and the closing will be in writing. Saturday — the kettle, the nap, the snore — is about to become a closed file that describes it accurately.

**Choices:**
- Ask for the closing documents in writing, for your folder — the screen note included → **w2b**  _(FLAG: copiesRequested)_
  - NOTE (shown after choosing): The screen note is the document to keep: it is the agency, on paper, explaining Ray's own result correctly. In a folder, forever, beside the letter that made it inevitable.
- Take the win by phone and let the file keep its own copies → **w2b**
  - NOTE (shown after choosing): The file will. Yours is the copy that survives office moves, worker changes, and time.

## [w2b] The Closing, Drafted
*Day 12 — Saturday, September 26, 2026 (dayOffset 12)*

The closing summary, when Vance shares the draft, is right in every particular but one, because summaries compress even in victory: the medication is described as 'a prescribed sleep aid.' It is not a sleep aid — it is a back medication, and the distinction is not pedantry: a file that says 'sleep aid' beside 'fell asleep' builds an implication neither document supports.

One phrase. The letter in the file contradicts it already, by name and purpose. Whether the summary gets corrected is a question of whether anyone reads the draft as if it matters — the family discipline, applied one final time, to a friendly document.

**Choices:**
- Point to the phrase once, letter in hand, and ask for the medication to be named as the letter names it → **w3**  _(FLAG: phraseCorrected)_
  - NOTE (shown after choosing): She corrects it at the desk, initialing the change — 'per prescriber letter on file.' The summary now cites its own correction's source. Files rarely get more honest than that.
- Let it stand — the case is closing in your favor → **w3**
  - NOTE (shown after choosing): It closes. The phrase sails into the permanent file, where 'sleep aid' will sit beside 'fell asleep' for any future reader to assemble into a story the letter disproves one page deeper.

## [w3] Sign Here
*Day 14 — Monday, September 28, 2026 (dayOffset 14)*

The closing letter arrives: the report is not supported; the investigation is closed; the screen is recorded as explained by the prescriber's documentation on file. The acknowledgment line waits — receipt, not agreement — beneath a summary paragraph that now names the medication as the prescriber named it, or doesn't, depending on a desk-side correction.

Ray has spent two weeks learning the system's single transferable skill. The letter is its final exam, and it is an easy one: read, then sign, then file — in that order, like everything else that worked.

**Choices:**
- Read the whole letter, sign, and file it with the packet — the race's complete record → **end_good**  _(FLAG: readBeforeSigning)_
  - NOTE (shown after choosing): Every sentence checks. The folder closes on the whole Saturday: a clause, a timeline, a letter that arrived before a lab — the file, the family, and the truth, in the same order for once.
- Sign it at the door — closed is closed → **end_good**
  - NOTE (shown after choosing): It is closed, and correctly. The folder at home holds the packet unordered, which in ten years will matter to exactly one person trying to remember how he won this. He won it in order, whether the folder shows it or not.

## [end_good] Explained Before It Posted
*Day 17 — Thursday, October 1, 2026 (dayOffset 17)*

**DEBRIEF:**

The investigation closed with the report not supported, and the drug screen — the week's scheduled disaster — sits in the file as a two-line note in which the agency itself explains the positive by the prescriber's letter. WIN: the letter was filed before the result existed, so the result never had an unexplained day in the file. Nothing was rebutted, because nothing was ever asserted — order did what argument couldn't.

The record inside this story: under 55 Pa. Code § 3130.44(d), the intake summary came from his record, on request — which is how Ray knew the file's phrase was 'possible impairment' and that the prescriber's letter had an appointment to keep: before Thursday's lab posted. The printout alone could never have done it; printouts state facts, and only the prescriber's letter interprets them — medication, dose, direction, no impairment concerns, in a professional's signature.

Notice the two words the whole case turned on: 'prior to.' Determinations are drafted from files, and files are read in order. A fact that arrives second is a rebuttal; a document that arrives first is the context. Same letter, same lab — the order is the outcome.

Honesty requires this: Ms. Vance filed the letter fairly and wrote the note straight, and other workers lose packets, misdate filings, or read positives as verdicts regardless of what's stapled to them. Labs also vary, and some results take five days and some letters two. What doesn't vary: a letter cannot predate a result it hasn't been filed before. The race is the strategy, and it is won in offices, in person, early.

## [m1] The Printout Isn't the Letter
*Day 8 — Tuesday, September 22, 2026 (dayOffset 8)*

The interview goes the way interviews go when the strongest document is a promise: Vance is fair, the Saturday account is believed provisionally, and everything waits on two clocks — the lab's three days, and the prescriber office's 'end of the week,' racing each other through different buildings.

The printout is in the file. What the printout establishes: the medication's name, Ray's name, monthly fills. What it cannot establish: that a doctor directs this, at this dose, for a back, with no concern about impairment. A printout is a receipt. Receipts prove purchases. Nobody has ever been exonerated by a receipt alone, because a receipt is equally consistent with the story it's meant to refute.

Three days pass the way held breaths do.

**Choices:**
- Call the prescriber's office daily — the letter is now the case, and cases get chased → **m1b**  _(FLAG: letterChased)_
  - NOTE (shown after choosing): Offices respond to polite persistence the way files respond to paper: eventually, and in writing. The letter is promised for Friday. The lab is promised for Monday. The race tightens.
- Wait for both clocks — they'll land when they land → **m1b**
  - NOTE (shown after choosing): They will. Clocks land in an order, and order is the whole case. Waiting is a strategy for choosing the order by default.

## [m1b] Two Clocks
*Day 9 — Wednesday, September 23, 2026 (dayOffset 9)*

Friday brings the letter — signed, complete, everything the printout couldn't say. Ray files it the same afternoon, in person, date-stamped, and for one weekend the file is in the right order: explanation first, result to come.

Monday brings the lab. Except — the lab's clock, it turns out, ran faster than its estimate, and the result posted Friday morning, hours before the letter's stamp. Three days from Thursday, the clerk says, counting Thursday. Ray counts differently. The file counts the clerk's way, because the file is the clerk's.

The result therefore exists in the file unexplained for a weekend before the letter arrives behind it. Three days of a positive standing alone — during which the file is read by a supervisor performing a Monday review of weekend postings.

Order, lost by hours. Consequences arrive on schedule.

**Choices:**
- Ask, in writing, for the file note to record both dates — result's posting, letter's filing — so the sequence is at least honest → **m2**  _(FLAG: datesNoted)_
  - NOTE (shown after choosing): The note is made. The file now tells the truth about its own weekend, which is the precondition for anyone, ever, correcting what the weekend caused.
- Protest the counting — Thursday to Monday is the three days you were promised → **m2**
  - NOTE (shown after choosing): The protest is noted beneath the result. Protests are read as feelings. Dates are read as facts. The file has room for both and a preference for one.

## [m2] Ten Days Unexplained
*Day 11 — Friday, September 25, 2026 (dayOffset 11)*

The Monday supervisor review does what reviews do with unexplained positives: it opens a case. Not a removal — the Saturday facts never supported that — but an opened case with a monitoring plan: the result 'pending explanation review,' a follow-up screen in sixty days, check-ins. The letter, when it lands in the review packet, ends the argument — and cannot un-open the case, because opened cases close by process, not by vindication.

For ten days the file's biggest fact was a positive with no interpreter. The interpreter's arrival is total: Dr. Amponsah's letter is accepted without reservation, the explanation is recorded as resolved, and the plan shrinks to its process minimum — the sixty-day screen (which will also be positive, and also explained, in advance this time), and a closing review.

Ray signs nothing in anger. He has learned the system's arithmetic: explanations that arrive second are believed second, after the machinery they triggered has had its ten days.

**Choices:**
- File the prescriber's letter for the sixty-day screen now — before that result exists, months early → **m3**  _(FLAG: letterPreFiled ; HIDDEN + Documentation — parent pre-filed the prescriber's letter for the follow-up screen)_
  - NOTE (shown after choosing): The lesson, applied: the second screen's file note will be born explained. Some tuition only has to be paid once, if the student files the receipt.
- Wait and file it when the sixty-day screen is scheduled → **m3**
  - NOTE (shown after choosing): Scheduling letters for later is how this file got its ten days. Calendars are cheap. Weekends in files are not.

## [m3] The Second Screen
*Day 14 — Monday, September 28, 2026 (dayOffset 14)*

Sixty days later the second screen posts — positive, as chemistry promised — into a file that either contains its explanation already (pre-filed, dated, waiting like a trap for the result) or receives it afterward in the now-familiar chase.

The closing review follows. The case that should never have opened is ready to close, and its closing summary is being drafted from a file whose middle chapters include an opened case, a monitoring plan, and a ten-day weekend that a supervisor read alone.

The summary will say 'case opened following positive screen; explanation subsequently provided and accepted.' Subsequently. The whole story of this story is in that adverb.

**Choices:**
- Read the closing summary before signing — and check its adverbs → **end_partial**  _(FLAG: readBeforeSigning)_
  - NOTE (shown after choosing): 'Subsequently provided' — accurate, and permanent. The letter's content was never doubted. Only its timing was ever the charge, and the summary convicts the timing with one adverb, correctly, forever.
- Sign — a closed case is a closed case → **end_partial**
  - NOTE (shown after choosing): Closed, yes. The summary's version of how it opened remains the file's account of Ray: a positive, explained subsequently. Files remember sequences. So, now, does Ray.

## [end_partial] Ten Days Unexplained
*Day 17 — Thursday, October 1, 2026 (dayOffset 17)*

**DEBRIEF:**

The case closed and the explanation was accepted completely — but a case existed at all, with a monitoring plan and a sixty-day screen, because a lab result spent ten days (a posting weekend, a supervisor's review, a process) unexplained while its interpreter traveled between offices. PARTIAL WIN: vindication, total and documented — purchased with an opened case that early filing would have made unnecessary.

The record inside this story: under 55 Pa. Code § 3130.44(d), the intake summary was Ray's to read from the start, and its phrase — 'possible impairment' — named the exact claim the prescriber's letter existed to pre-answer. The printout was never going to do it: receipts prove fills. Only the prescriber interprets — medication, dose, direction, no impairment concerns — and only in writing, and only in the file.

Notice the margin: hours. The letter lost its race by the width of a weekend because its author started even with the lab instead of ahead of it. In this system, 'eventually explained' and 'explained' are different outcomes with different paperwork, and the difference is measured in days a result spends alone.

Honesty requires this: the supervisor's review was mechanical, not malicious, and the case it opened was the mildest available response to an unexplained positive. A hotter office escalates the same ten days further. What doesn't vary: results post on lab time, letters travel on office time, and the file believes whichever one it reads first. Start the letter when the screen is first mentioned. That is the whole tactic, and it is enough.

## [h1] Unable to Assess
*Day 7 — Monday, September 21, 2026 (dayOffset 7)*

The refusal is noted in the file in three flat words — 'screen declined' — and the file's one open question, 'possible impairment,' loses its scheduled answer. Investigations do not end at unanswered questions. They change venue.

Vance explains the path without relish: the agency cannot close a report alleging impairment without assessing impairment; refused voluntarily, the question will be put to a court, attached to the Saturday facts — a child's sentence, a dry kettle, a sleeping night-shift worker — which, presented without the screen's resolution, read worse than they lived.

Ray's prescription sits in his pharmacy's computer, still fully capable of explaining everything, to a judge, eventually — after a petition, a hearing, and weeks of the file believing the worst available version.

Rights have prices in this system. The price list is printed in delays.

**Choices:**
- Reconsider within the week — call and take the screen voluntarily, letter racing beside it → **h1b**  _(FLAG: reconsidered)_
  - NOTE (shown after choosing): Reconsideration is noted as cooperation, and the screen gets taken — late, voluntary, and still ahead of any court. The letter now has a second chance to run its race, against a lab instead of a judge.
- Stand on the refusal — let them take it to a judge → **h1b**
  - NOTE (shown after choosing): They will. It is, procedurally, the only door left open, and doors in this system are used in the order they remain.

## [h1b] The Petition
*Day 8 — Tuesday, September 22, 2026 (dayOffset 8)*

If Ray reconsiders, the story shortens: the screen is taken, and its fate becomes the familiar race. If he stands, the petition is filed — a dependency petition built from the school report and the refusal, asking a court to order what the investigation asked for: assessment, including screens, under supervision.

Either way, the next room has a judge in it, and judges ask the question files ask: what explains the sleep? The prescriber's letter — requestable since the first phone call, fileable since the first week — becomes, in this branch, a courtroom exhibit instead of a file note, produced at litigation speed, which is to say weeks late and under cross-examination.

Dr. Amponsah's office, asked now, can have the letter ready in days. It always could. The letter was never the problem. The calendar was.

**Choices:**
- Get the letter now — before any hearing — and file it with the court and the agency → **h2**  _(FLAG: packetReady ; HIDDEN + Proof — prescriber's letter obtained and filed ahead of the court hearing)_
  - NOTE (shown after choosing): Late, but in the room where it now counts. The hearing will at least be fought on the whole record: Saturday, the prescription, and the refusal, each documented, each in its least flattering and most accurate form.
- Let the hearing sort it — a judge will see the prescription bottle's label, surely → **h2**
  - NOTE (shown after choosing): Labels are printouts with curves. Judges, like files, prefer interpreters with signatures.

## [h2] The Hearing
*Day 10 — Thursday, September 24, 2026 (dayOffset 10)*

The hearing is small and procedural and consequential in the way of such rooms. The agency's case: a report of a sleeping parent and a hot stove, and an impairment question the parent declined to answer voluntarily — a refusal the agency's counsel mentions the way one mentions weather, as a condition everything else happened in.

Ray's counsel — appointed, because counsel in dependency matters is a right (42 Pa.C.S. § 6337) — presents what exists: the timeline, the schedule, Ashford's statement, and, if it was finally obtained, Dr. Amponsah's letter, which explains the prescription completely and cannot explain the refusal at all.

The judge rules the way judges rule on unanswered questions: the question gets answered, by order, on the court's schedule, under the court's supervision — with a case opened to hold the answer.

**Choices:**
- Ask the court to note the prescriber's letter as the screen's standing explanation, for every future result → **h2b**  _(FLAG: letterNotedByCourt)_
  - NOTE (shown after choosing): Noted, if the letter exists in the room. It is the one durable good available today: every future positive in this case now arrives pre-explained, by court order's own paperwork.
- Argue the refusal itself — the principle of it → **h2b**
  - NOTE (shown after choosing): The principle is real and the ruling is unaffected by it. Courts answer unanswered questions; principles are preserved for appeals, in writing, by lawyers, later.

## [h2b] Ordered
*Day 12 — Saturday, September 26, 2026 (dayOffset 12)*

The order issues: a case is opened; screens will be taken on the agency's schedule for ninety days; services are attached — a parenting class, check-ins — sized to a file whose central fact is an unanswered question rather than an answered one.

The first ordered screen posts positive within the fortnight, and it is explained — by the letter, if the letter exists in the file by then, completely and boringly; by another scramble, if it doesn't. Either way, the explanation now happens inside an open case, on court time, with the refusal in the file's front chapters explaining why everyone is here.

Ninety days of ordered answers to a question that was offered, free, on a Thursday.

**Choices:**
- Run the ninety days the way the letter taught: everything pre-filed, everything read before signing → **h3**
  - NOTE (shown after choosing): The case will close on compliance, and its closing summary will be drafted from a file that begins with a refusal. Discipline now governs the ending's margins, not its existence.
- Run the ninety days in protest, minimally, as a wronged man → **h3**
  - NOTE (shown after choosing): Protest is recorded as engagement quality, in the file's colder vocabulary. Ninety days is long enough for a posture to become a description.

## [h3] Day Ninety, Ordered
*Day 14 — Monday, September 28, 2026 (dayOffset 14)*

The case closes at the end of its ordered season: screens explained, class attended, check-ins checked. The closing summary is being drafted, and its raw material is the file in order — a child's clause, a refused cup, a petition, an order, ninety days of answers.

What the summary cannot contain, because it never happened, is the version where the impairment question was answered voluntarily in week one and the file stayed an investigation — two weeks, a letter, a closed report — instead of becoming a case.

The acknowledgment line waits beneath the draft summary paragraph.

**Choices:**
- Read the closing summary fully before signing — know what the case says you were → **end_hard**  _(FLAG: readBeforeSigning)_
  - NOTE (shown after choosing): It says: 'Father declined screening during investigation; assessment completed under court order; medication explanation accepted.' Every clause true. The truth, arranged by a refusal, reads like a different man than the one who napped by a kettle.
- Sign it — ninety days is enough of this file → **end_hard**
  - NOTE (shown after choosing): Signed. The file's first paragraph about Ray Kaczmarek now begins with a refusal, and first paragraphs are the ones that get read.

## [end_hard] The Test, Ordered
*Day 17 — Thursday, October 1, 2026 (dayOffset 17)*

**DEBRIEF:**

The screen Ray declined voluntarily was taken by court order, inside an opened case, for ninety days — and its result was explained by the same prescription that would have explained it in week one. Nothing about the medicine ever changed. What changed was the venue, the duration, and the file's opening chapters, which now begin with a refusal instead of a letter.

The verified law inside this ending: parents in dependency proceedings have the right to counsel (42 Pa.C.S. § 6337), and Ray had it — counsel explained his options accurately, including this one. Declining an investigation-stage screen is a choice the system permits and prices: an unanswered impairment question does not close; it escalates to a court, which answers it with supervision attached. The price list is printed in delays.

Notice the asymmetry the case teaches: the prescriber's letter, whenever it finally arrived, was believed instantly and completely. Its content was never the contest. The contest was always procedural — who would ask the question, in what room, under whose order — and procedure is decided by the choices made before anyone reaches a courtroom.

Honesty requires this: some families decline screens on advice, on principle, or on lawyers' strategy, and some of those cases end better than this one — judges vary, petitions get withdrawn, agencies relent. What doesn't vary: an explained positive and an unanswered question are the same chemistry in different postures, and the system prices the postures, not the chemistry. Take the test. File the letter first.
