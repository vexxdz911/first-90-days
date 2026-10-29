# THE FIRST 90 DAYS — Scenario 42: “The Report from the Hospital”

*Human-readable script. This document and `scenario-42.json` are generated from a single source and match node-for-node: same IDs, same order, same choices, same effects.*

**The family is fictional — a composite. No real person's story appears here.**

**Content note:** This scenario depicts a hospital report about a toddler's fracture, an indicated determination, and an appeal. Medical detail is kept at the level of charts and letters. There is no graphic content. Players may skip any scene or use the quick exit at any time.

**How to read effects:** `cash −40` changes the player's cash. `FLAG: name` sets a flag the engine tracks. `HIDDEN + item` means the case file quietly records that item at this choice. `REQUIRES FLAG: name` means the choice is only available if that flag was set earlier.

Start date: Monday, April 13, 2026. Day offsets are days since the scenario's start date.

## [start] The Fall
*Day 0 — Monday, April 13, 2026 (dayOffset 0)*

Reuben is eighteen months old, which means his relationship with gravity is enthusiastic and ongoing. On Saturday afternoon he went over the arm of the couch the way he has done a hundred times, except this time he landed on the rug with his arm under him, and the cry that followed was a different instrument than his usual one.

Hannah Reilly did the things the books say: ice, watching, the pediatrician's after-hours line at seven ('Watch it; if the swelling's up in the morning or he won't use it, go in'). Sunday morning the swelling was up and he wouldn't use it. The emergency department found a forearm fracture, set it, splinted it, and gave him a sticker he wore like a medal.

That was Sunday. This is Monday, and the phone is the hospital social worker, kind and procedural: a report has been made, as the hospital is required to do. An investigation is open. A worker — Ms. Dominguez — will be calling.

**Choices:**
- Write down the social worker's words, the worker's name, and Saturday's hours — while they're today's → **c2**  _(FLAG: timelineWritten)_
  - NOTE (shown after choosing): 4:10 the fall. 7:00 the nurse line. Sunday, 9:30, the ER. Three times, in ink, are about to become the spine of everything — because 'inconsistent' is a word that feeds on missing times.
- Call Tom at work and reconstruct the weekend together out loud → **c2**
  - NOTE (shown after choosing): Two memories agreeing out loud is comfort. It is not a timeline. The file will not be grading your comfort.

## [c2] Two Readings
*Day 1 — Tuesday, April 14, 2026 (dayOffset 1)*

The ER paperwork, when Hannah reads it at the kitchen table, contains two voices. The treating resident wrote: 'Mechanism (fall from couch onto rug, arm beneath body) is plausible for this injury.' And a second note, from a consult requested by the department — a child-abuse pediatrics specialist, doing the job such specialists exist to do: 'Cannot rule out non-accidental trauma pending full records review.'

Plausible, and cannot rule out. Both are in the chart. Both are honest. They are not the same sentence, and the investigation will be built from whichever one the file picks up first.

The consult's sentence contains its own instruction, hiding in plain sight: pending full records review. Somebody has to assemble the full records. The hospital has a department for that. So, it turns out, does Reuben's kitchen table.

**Choices:**
- Decide the packet is the case: every record, from every source, assembled by you → **records**
  - NOTE (shown after choosing): The consult asked for a full record. Full records do not assemble themselves, and partial records assemble themselves into the wrong shape.
- Wait for the consult's final word — the specialists will sort it → **records**
  - NOTE (shown after choosing): They will sort what reaches them. What reaches them is a logistics problem, and logistics is about to become your job whether you take it or not.

## [records] What the File Says So Far
*Day 2 — Wednesday, April 15, 2026 (dayOffset 2)*

Hannah requests the record: the intake summary from the agency's file. Under 55 Pa. Code § 3130.44(d), the record is released on request. It arrives as one paragraph, and the paragraph contains a word that stops her eye the way a stone stops a shoe:

'Fracture, forearm, toddler. Explanation offered by parents described as inconsistent with injury.' Inconsistent. The resident's chart says plausible; the summary says inconsistent. Somewhere between the ER and the intake desk, the chart was compressed by someone who was holding only the consult line.

A summary is not the record. But until the record arrives in the file, the summary is what the file believes.

**Choices:**
- File the written request and mark the word: your answers now have a target → **nb**  _(FLAG: recordsRequested ; HIDDEN + Records — parent obtained the intake summary and identified its characterization of the explanation)_
  - NOTE (shown after choosing): 'Inconsistent' is the claim. Claims can be answered — with the chart's own sentence, once the chart is in the file beside the summary.
- Skip the summary — you know what you told them → **nb**
  - NOTE (shown after choosing): You do. The file knows what the summary told it. Those are different knowledges, and only one of them attends the determination meeting.

## [nb] The Hospital's Paper
*Day 3 — Thursday, April 16, 2026 (dayOffset 3)*

The hospital's medical-records department can produce the ER chart — for a fee, in some days, through a window with a number on it. The pediatrician's office can produce Reuben's whole chart faster, and Dr. Weiss, who has weighed this child since he was four days old, is in it.

Hannah pays the fee, takes the number, and starts the two clocks. Paper moves at the speed of departments. Determinations, unfortunately, move at the speed of files — and files accept whatever has arrived.

The race in this story is not against the agency. It is against the determination being drafted from a partial record.

**Choices:**
- Order the ER chart today and request the pediatric chart in the same afternoon → **med**  _(FLAG: erChartOrdered ; HIDDEN + Records — parent ordered the complete ER chart and requested the pediatric record immediately)_
  - NOTE (shown after choosing): Two requests, two clocks, one goal: the determination meeting should be the last thing that happens, not the first thing the partial record causes.
- Let the agency request the records itself — it's their investigation → **med**
  - NOTE (shown after choosing): It is. Their request goes into a queue with a number on it too, and their determination is not required to wait for their own paperwork.

## [med] Dr. Weiss
*Day 5 — Saturday, April 18, 2026 (dayOffset 5)*

Dr. Weiss's office assembles the other half of Reuben: eighteen months of well-child visits, growth tracking the chart's smooth curve, immunizations current, no prior injuries — none — and the after-hours log from Saturday night, 7:04 p.m., Hannah's call, the nurse's advice, in the record because the practice logs its line.

Weiss writes the letter herself, because she has opinions about forearm fractures in toddlers who fall off couches: developmentally typical mechanism, couch height, carpeted surface, no other findings, parents sought care appropriately and on advice. It is a strong letter. In a folder with the ER chart's 'plausible,' it is a wall.

A wall, however, only defends rooms it's built in. The folder is not the file — yet.

**Choices:**
- Assemble the full packet: ER chart, Weiss's letter, the well-child record, Saturday's timeline — one packet, ready to file → **eve**  _(FLAG: packetReady ; HIDDEN + Proof — complete medical packet assembled: ER chart, pediatrician letter, well-child record, timeline)_
  - NOTE (shown after choosing): Four documents, and the consult's own caveat is answered by three of them. The packet now exists. Its entire remaining job is to arrive.
- Keep the pediatric records for later — the hospital chart should be enough on its own → **eve**
  - NOTE (shown after choosing): The hospital chart contains 'cannot rule out.' On its own, it argues both sides. The packet was the argument; half a packet is a debate.

## [eve] The Night Before the Meeting
*Day 6 — Sunday, April 19, 2026 (dayOffset 6)*

Ms. Dominguez has scheduled the meeting at the agency office tomorrow. Tom will come — his account of Saturday matches Hannah's because Saturday only happened once, and both of them were standing in it.

On the table: the packet, or most of one. In the file across town: one paragraph with 'inconsistent' in it, and a consult that cannot rule anything out on a record it hasn't seen.

Meetings like tomorrow's have a physics: what is handed over gets weighed; what is described gets summarized. The folder's contents are about to be classified, permanently, into one of those two kinds.

**Choices:**
- Sleep. The packet is built; tomorrow it changes buildings → **gate**
  - NOTE (shown after choosing): Whatever the meeting holds, it will be met with the whole record. That was the entire job of the week.
- Rehearse the explanation until it sounds perfect → **gate**
  - NOTE (shown after choosing): Explanations are what got 'inconsistent' written in the first place. Paper doesn't rehearse. It just sits there, being checkable.

## [gate] The Determination Meeting
*Day 8 — Tuesday, April 21, 2026 (dayOffset 8)*

The office has the particular quiet of rooms where files are decided. Ms. Dominguez is professional, not hostile: the summary says inconsistent; the consult cannot rule out; those are her two facts, and she is — reasonably, on her paper — unconvinced.

She has not seen the ER chart's second page. She has not seen Dr. Weiss's letter, or eighteen months of uninjured well-child visits, or the 7:04 p.m. nurse-line log that turns 'waited until Sunday' into 'followed medical advice.' All of it exists. Existence, in this room, is not the test.

Arrival is.

**Choices:**
- Hand over the packet — the whole record — with the written timeline on top, and ask that it be filed before any determination → **w1**  _(REQUIRES FLAG: packetReady)_
  - NOTE (shown after choosing): She takes it with the slight pause of a worker whose file just changed species. 'The chart says plausible,' she says, reading the second page for the first time. 'Yes,' Hannah says. 'It always did.'
- Explain Saturday fully and fairly — and describe the records that exist, at home, in a folder → **h1**  _(HIDDEN + Response — parents explained the injury verbally; medical packet described but not filed at the meeting)_
  - NOTE (shown after choosing): She writes: 'Parents state records exist; packet to follow.' In the file's grammar, 'to follow' is a promissory note. Determinations are not required to wait for promissory notes.

## [w1] Read in the Room
*Day 10 — Thursday, April 23, 2026 (dayOffset 10)*

The meeting changes tense. Dominguez reads Weiss's letter standing up, the way people read things that alter their afternoon. A supervisor is fetched — not as an escalation, as a witness: the packet is logged, copied, and placed in the file in the parents' presence, with the intake summary's 'inconsistent' now sitting in a folder that also contains the chart it misdescribed.

One question remains, and it's a fair one, and the supervisor asks it plainly: 'Why Sunday? He fell Saturday.'

It is the question the whole investigation was secretly about. And it has a documentary answer — if the packet was built whole.

**Choices:**
- Point to the nurse-line log: Saturday, 7:04 p.m., advice given and followed, in the pediatrician's own record → **w1b**  _(FLAG: nurselineShown ; HIDDEN + Proof — after-hours nurse-line log shows care was sought Saturday and advice followed)_
  - NOTE (shown after choosing): The supervisor reads the log line twice. 'You called,' she says. 'You were told morning. You went in the morning.' Saturday's timeline, which the summary called inconsistent, is now the file's best-documented day.
- Explain the evening from memory — the ice, the watching, the call → **w1b**
  - NOTE (shown after choosing): She nods and writes 'parents report calling pediatrician Saturday evening.' Reports are weighed. Logs are read. The packet's strongest page is the one that didn't get pointed at.

## [w1b] The Supervisor's Question, Answered
*Day 12 — Saturday, April 25, 2026 (dayOffset 12)*

The determination is not made in the room — determinations never are — but its direction is set in rooms like this, and everyone present can feel the weather change. The file now contains: a chart that says plausible, a pediatrician who says typical, a record of eighteen uninjured months, a nurse-line log, and a summary that says inconsistent, authored by someone who had seen none of it.

What remains is the consult's final review — the specialist, reading the full record at last, because the full record is finally somewhere a specialist can read it.

Dominguez schedules nothing further. 'We'll await the final consult,' she says, 'and the determination will be in writing.'

**Choices:**
- Ask that the packet's filing be noted in the record, with today's date → **w2**  _(FLAG: filingNoted)_
  - NOTE (shown after choosing): Noted. When the consult's final word arrives, it will arrive in a file whose medical record is complete — and dated before the determination, which is the whole ballgame.
- Thank them and leave the packet to do its work → **w2**
  - NOTE (shown after choosing): It will. Paper is patient. But dated paper is patient with a timestamp, and timestamps are what determinations cite.

## [w2] Waiting on the Consult
*Day 15 — Tuesday, April 28, 2026 (dayOffset 15)*

Waiting, in an investigation, is its own discipline. Reuben's splint acquires signatures and a smell. The file, across town, is quiet — but it is a different quiet than before the meeting: the quiet of a complete record awaiting a reader, instead of a partial one awaiting a conclusion.

Hannah does the small clerical things that waiting allows: copies of everything, in her own folder, in order. If the determination surprises her, the next step — and there is a next step, with its own window — will start from a folder, not from scratch.

The consult's final report is due this week.

**Choices:**
- Call once, mid-week, and ask whether the final consult has arrived — politely, and note the answer with its date → **w2b**
  - NOTE (shown after choosing): It hasn't, yet, but the call is logged, and the log says the parents are engaged and the record is complete. Even waiting generates paper, if you let it.
- Wait in silence — calling might annoy them → **w2b**
  - NOTE (shown after choosing): Silence is also logged, as nothing. The file will show a gap where a call could have been.

## [w2b] The Final Consult
*Day 17 — Thursday, April 30, 2026 (dayOffset 17)*

It arrives on a Thursday, and Dominguez reads the operative sentence over the phone before the letter is even mailed: the specialist, on the full record — ER chart, well-child history, nurse-line log, mechanism — concludes the findings 'are consistent with the reported mechanism, with no additional concerns identified.'

Cannot rule out has become consistent with. The difference between those two sentences is not Hannah's innocence, which was constant. It is the record's completeness, which wasn't — until she built it.

The determination letter follows: the report's status, decided on the whole record at last.

**Choices:**
- Ask for the determination and the final consult in writing, for your folder → **w3**  _(FLAG: copiesRequested)_
  - NOTE (shown after choosing): Both will come. Her folder and the file are about to hold the same medicine, which is the strongest position a family in an investigation can occupy.
- Take the phone call as the ending and exhale → **w3**
  - NOTE (shown after choosing): Exhale, certainly. But the letter is the ending — phone calls are how endings get announced, not how they get recorded.

## [w3] The Letter
*Day 19 — Saturday, May 2, 2026 (dayOffset 19)*

The determination letter is two pages: the report is UNFOUNDED — not supported — the fracture explained by the documented mechanism, the record cited page by page, including the consult's final word and Dr. Weiss's letter. There is an acknowledgment line at the bottom: receipt, not agreement.

On the second page, the injury is described as a 'left forearm fracture.' It was the right arm. Reuben's splint, currently being used as a drumstick, is on the right arm. Even good letters compress, and compressions are forever unless somebody writes back.

**Choices:**
- Read it fully — sign, and send the one-line correction: right forearm, per the ER chart, page two → **end_good**  _(FLAG: readBeforeSigning)_
  - NOTE (shown after choosing): One line, filed. The file's last medical sentence now matches the chart it cites — and the correction itself is a small monument: this family reads what it signs.
- Sign it at the door — unfounded is unfounded → **end_good**
  - NOTE (shown after choosing): It is. The letter sails into the file with the wrong arm in it, harmless today, a small wrongness preserved in the record of a right outcome. Reuben, drumming, is indifferent. Files are not.

## [end_good] Unfounded, On the Whole Record
*Day 22 — Tuesday, May 5, 2026 (dayOffset 22)*

**DEBRIEF:**

The report was determined unfounded — because the determination was made on the whole medical record instead of its thinnest summary: an ER chart whose own words said 'plausible,' a pediatrician's letter, eighteen months of uninjured well-child visits, and a nurse-line log that turned the delay into advice followed. WIN: when two medical readings competed, the complete record — assembled and filed by the parent, before the determination — decided between them.

The record inside this story: under 55 Pa. Code § 3130.44(d), the intake summary came from her record, on request — which is how Hannah knew the file's word was 'inconsistent' and could answer the claim instead of the fog around it. The consult's caveat did the rest of the teaching: 'pending full records review' is an instruction, and the parent who follows it builds the record the specialist rules on.

Notice what never happened: no hearing, no appeal, no lawyer — because the fight was won at the filing stage, where fights are cheapest. The same packet, filed after an indicated determination, would have been an appeal exhibit instead of a determination input. Same documents. Different decade of effort.

Honesty requires this: the specialist could have read the same record and held firmer; a supervisor could have discounted a pediatrician as 'the family's own doctor.' Medicine argues with itself in every hospital. What the packet guaranteed was only this: that the argument happened on the whole record, with Hannah's evidence in the room — which is the most any parent can build, and it was enough.

## [h1] To Follow
*Day 10 — Thursday, April 23, 2026 (dayOffset 10)*

The meeting ends with handshakes and a sentence in the file — 'packet to follow' — doing the work of a wall it isn't. Dominguez is not unkind about what happens next: the determination must be drafted on the file as it stands while the packet is in transit, and the file as it stands contains a summary saying inconsistent and a consult saying cannot rule out.

In the meantime, an interim plan is put in place 'out of caution': Reuben will stay with Tom's mother, Mrs. Brennan, on the nights Hannah works late, and a follow-up visit is scheduled. Caution, in files, is a posture with a paperwork shadow: the plan will still be in the file when the determination is drafted, being read as evidence of its own necessity.

The packet, at home, waits for a copier, a stamp, a free afternoon. The determination does not wait.

**Choices:**
- Treat the packet as an emergency: copy it, file it in person tomorrow, get it date-stamped → **h1b**  _(FLAG: packetRushed)_
  - NOTE (shown after choosing): It goes in the next day, stamped. Whether it lands before the determination draft is now a race between a stamp and a supervisor's signature — a race that did not have to exist.
- Mail the packet this week, complete and careful → **h1b**
  - NOTE (shown after choosing): Complete, careful, and in the mail while a determination is being drafted from a one-paragraph summary. Care is not the variable. Timing is.

## [h1b] Nana Brennan's Living Room
*Day 12 — Saturday, April 25, 2026 (dayOffset 12)*

The interim weeks have a texture: Reuben at his grandmother's on late nights, learning her spoons; Hannah driving across town in the dark both ways; the splint acquiring signatures. Nothing about it is unsafe. Everything about it is in a file, described as a safety measure, acquiring the inertia safety measures acquire.

The packet lands — date-stamped, complete, read by Dominguez with genuine attention. 'This should have been in the meeting,' she says, not unkindly. She is right, and it doesn't matter: the determination draft is already with her supervisor, and drafts have their own gravity.

What the packet can still do is arrive before the signature. What it cannot do is arrive before the draft. The distance between those two events is where this case now lives.

**Choices:**
- Ask, in writing, that the determination be held until the full record — now filed — is reviewed → **h2**  _(FLAG: holdRequested)_
  - NOTE (shown after choosing): The request is reasonable, dated, and in the file. Reasonable requests are sometimes granted. The ones that are filed are the ones that can be appealed from, if it comes to that.
- Wait for the determination — the packet is in, surely it decides things → **h2**
  - NOTE (shown after choosing): Packets decide things in the order they're read. Yours is being read second, against a draft, by a supervisor who wrote neither.

## [h2] Indicated
*Day 18 — Friday, May 1, 2026 (dayOffset 18)*

The letter is dated Friday, May 1, 2026, and it is one page: the report is INDICATED. The determination rests on the file as drafted — the consult's preliminary 'cannot rule out,' the summary's 'inconsistent,' the interim plan's existence — and the full packet, filed after the draft, is noted in a single line: 'Additional records received; under review.'

Indicated is a status with consequences: it sits in the statewide record, it answers questions on clearances, and for Hannah — who works with other people's children — it is a professional fact as well as a parental one. Reuben stays home; the interim plan is lifted; and yet the letter changes the family's weather entirely.

The letter also contains the most important sentence in it, in the flattest type: an appeal may be requested in writing within 90 days of notification. Notification: May 1. Ninety days: July 30, 2026. A window, printed, ticking.

**Choices:**
- Write the dates on the folder tonight — May 1, July 30 — and treat the window as the case now → **h3**  _(FLAG: deadlineKept ; HIDDEN + Deadlines — parent calendared the 90-day appeal window from the determination letter's date)_
  - NOTE (shown after choosing): Under 23 Pa.C.S. § 6341(a)(2), the written request must be filed within 90 days of notification. The window is generous and absolute — the two qualities deadlines have instead of mercy.
- Put the letter in a drawer — Reuben is home, the plan is lifted, let sleeping files lie → **h2b**
  - NOTE (shown after choosing): The file is not sleeping. It is filed — in a statewide database, where it will answer clearance questions in Hannah's employer's voice for years. Drawers are where windows close.

## [h2b] The Drawer
*Day 44 — Wednesday, May 27, 2026 (dayOffset 44)*

May is kind and ordinary, which is how windows close: not with a slam but with a spring. The fracture becomes a story Hannah tells at the playground, badly, with gestures. The letter sits in the drawer under the good scissors.

What pulls it out, in late May, is a form: Hannah's employer, renewing clearances for the fall, and the quiet professional question of what an indicated status will say when it is asked. She takes the letter out and reads the flat sentence again: within 90 days of notification. May 1. The count, done on the folder with a pencil, is unforgiving and — this time — still survivable.

Twenty-six days gone. Sixty-four left. The window is not a metaphor; it is a subtraction problem, and it is still solvable.

**Choices:**
- Do the arithmetic out loud, today, and start the appeal from the folder — the packet is already built → **h3**  _(FLAG: deadlineKept)_
  - NOTE (shown after choosing): Late starts are the tax on drawers. The appeal will now be built at drawer speed — but the packet exists, complete, which is the difference between a scramble and an assembly.
- Decide July will be soon enough to think about it → **h3**
  - NOTE (shown after choosing): July is where this window goes to be tested. Appeals filed on day 89 count. Appeals contemplated on day 91 are biographies.

## [h3] The Appeal, Assembled
*Day 48 — Sunday, May 31, 2026 (dayOffset 48)*

An appeal under § 6341 is a written request — and a choice about what kind of appeal to make. The bare request preserves the right and nothing else: a letter, a date, a hearing someday on the file as it stands. The built request does something more: it invokes the appellant's right to the investigation evidence — 23 Pa.C.S. § 6341(c.2)(4) — and demands the complete file the determination rested on, including anything that helps her.

Hannah's packet is already the best evidence in the case. What she doesn't have is the agency's: the consult's working notes, the intake worksheet, whatever the summary's author was holding. Under (c.2)(4), that evidence is hers to see. Asking for it is not a courtesy the agency extends. It is a term of the appeal itself.

The request goes out this week either way. The question is its shape.

**Choices:**
- File the appeal with the evidence demand: the complete investigation file, including the consult's materials, under § 6341(c.2)(4) → **h3b**  _(FLAG: appealFiled ; FLAG: evidenceDemanded ; HIDDEN + Appeal — written request filed within the 90-day window, with a demand for the investigation evidence under § 6341(c.2)(4))_
  - NOTE (shown after choosing): Filed, dated, inside the window, with the demand in it. The agency must now assemble its own case — which means, for the first time, reading its file the way Hannah has: whole.
- File the bare request — preserve the right, keep it simple → **h4b**  _(FLAG: appealFiled ; HIDDEN + Appeal — written request filed within the 90-day window; no evidence demand made)_
  - NOTE (shown after choosing): The right is preserved and the hearing will come. It will be fought on the file as it stands — a file whose medical record is still, formally, a summary and a caveat.

## [h3b] The Evidence Packet
*Day 56 — Monday, June 8, 2026 (dayOffset 56)*

The agency's evidence arrives in a fat envelope, because (c.2)(4) says it must: the intake worksheet, Dominguez's notes, the consult's materials — and, paper-clipped to the consult's final review, a document Hannah has never seen: the specialist's amended conclusion, issued after the full packet landed, reading 'consistent with the reported mechanism.'

It was in the agency's file before the determination was signed. It is in Hannah's hands now because she demanded the evidence — all of it, including the kind that helps her. The determination said 'under review.' The review, it turns out, had concluded.

A pre-hearing review is scheduled — the agency, looking at its own assembled file. Files argue with their owners sometimes, when someone makes them whole.

**Choices:**
- Send one page ahead of the review: the amended consult conclusion, highlighted, with the packet's filing date beside the determination's → **h4**  _(FLAG: concessionSent)_
  - NOTE (shown after choosing): One page, two dates, no adjectives. It is the most persuasive document in the case, and Hannah didn't write a word of it — she demanded it.
- Let the review speak for itself — the file is whole now → **h4**
  - NOTE (shown after choosing): It is whole, and reviews read wholes. But a highlighted page is a kindness you do a busy reviewer, and kindnesses to reviewers are a genre of advocacy.

## [h4] The Review
*Day 60 — Friday, June 12, 2026 (dayOffset 60)*

The review does not require a hearing room. It requires a supervisor, the assembled file, and the amended consult conclusion sitting where the preliminary one used to sit alone. The agency's burden at any hearing would be substantial evidence — 23 Pa.C.S. § 6341(c.2)(5) — and the agency, reading its own evidence whole, reaches the conclusion its hearing officer would eventually reach for it.

The expungement is granted without a hearing: the indicated status is removed, the statewide record corrected, the letter issued in writing. It is dated June 12, 2026 — forty-two days after the determination it erases.

Forty-two days, a drawer-summer's worth of clearance anxiety, an interim plan, and a status that answered questions about Hannah before she could — all of it the price of a packet that arrived after a draft instead of before a determination.

**Choices:**
- File the expungement letter with the packet, the demand, and the determination — the whole arc, in order → **end_partial**  _(FLAG: arcFiled)_
  - NOTE (shown after choosing): The folder now contains the case's complete autobiography: founded on a summary, reversed on a record. It is the most instructive folder Hannah owns, and she built every page of the expensive half.
- Take the win and close the folder — it's over → **end_partial**
  - NOTE (shown after choosing): It's over. The folder, unfiled and unordered, will still teach its lesson to anyone who opens it: the documents existed on day one. The order they were filed in cost forty-two days.

## [end_partial] Appealed, In Time
*Day 62 — Sunday, June 14, 2026 (dayOffset 62)*

**DEBRIEF:**

The indicated determination was expunged on appeal — before any hearing, on the agency's own assembled evidence — so the ending is a win with an invoice attached: Reuben spent weeks under an interim plan, Hannah spent forty-two days as an indicated perpetrator in a system that answers her employer's questions, and the family took the long way through a door that was open at the determination meeting. PARTIAL WIN: the appeal worked exactly as the law builds it to; it should never have been needed.

The verified law inside this ending: an indicated report may be appealed by written request within 90 days of notification (23 Pa.C.S. § 6341(a)(2)) — May 1 to July 30, 2026, in this file — and the appeal carries the appellant's right to the investigation evidence, including what helps her (§ 6341(c.2)(4)). The amended consult conclusion was always in the agency's file. The demand is what moved it into Hannah's hands.

Notice the two filing dates that decided everything: the packet's (after the draft) and the appeal's (inside the window). The same documents, filed in the meeting instead of after it, end this story at 'Unfounded.' Sequence is not a detail in this system. Sequence is the system.

Honesty requires this: the agency could have defended its draft, the review could have split the difference, and (c.2)(4)'s envelope could have arrived thinner. Workers and reviewers vary. What did not vary: the window was used, the evidence was demanded, and a complete record — whenever it is finally assembled — is very hard for an honest file to argue with.

## [h4b] The Hearing
*Day 120 — Tuesday, August 11, 2026 (dayOffset 120)*

The hearing comes in the late summer, in a room with a flag and a court reporter, and it is more formal than Hannah expected and less fair than she hoped — not because anyone cheats, but because of what each side is carrying. The agency's case is its file: the summary, the consult's preliminary line, the determination. Hannah's case is her testimony, Dr. Weiss's letter, and her memory of a Saturday.

The agency's burden is substantial evidence — 23 Pa.C.S. § 6341(c.2)(5) — which is a real burden and a modest one: enough evidence that a reasonable mind could accept the conclusion. A specialist's 'cannot rule out,' plus an intake summary's 'inconsistent,' can clear it. Hannah's fuller record was never demanded under (c.2)(4), so the consult's amended conclusion — if one even exists — is not in this room. Rooms can only rule on what enters them.

The hearing officer listens to everyone, kindly and completely. Kindness is not the standard. The standard is the standard.

**Choices:**
- Have your counsel press the chart's own word — 'plausible' — against the summary's 'inconsistent' → **h5**
  - NOTE (shown after choosing): It is the best argument available, and counsel makes it well: the file contradicts itself, and a self-contradicting file is a thin foundation for substantial evidence. The officer writes for a long time. Long writing, at hearings, is not a verdict either way.
- Testify fully and trust the room to feel Saturday's truth → **h5**
  - NOTE (shown after choosing): The room feels it. Rooms are good at feeling. Rulings are made of standards, and the standard asked what the evidence could support — not what the room believed.

## [h5] The Decision
*Day 165 — Friday, September 25, 2026 (dayOffset 165)*

The decision arrives within the window the law sets for it — 45 days (23 Pa.C.S. § 6341(c.3)) — and it upholds the indicated status: the agency, the officer finds, carried its burden with the consult's assessment and the documented inconsistency in the initial explanations; the parents' additional records, while noted, did not displace that evidence on this record.

On this record. The qualifier is the case's epitaph: the record was the one Hannah let be built — no evidence demanded, the amended consult (if it existed) never seen, the packet an exhibit of memory instead of medicine.

The decision is not the end of the law: reconsideration may be sought within 15 days, and an appeal lies to the Commonwealth Court within 30 (23 Pa.C.S. § 6341(g)). Those windows are now the case — shorter, colder, and uphill, the way windows get as a case climbs.

**Choices:**
- Calendar the (g) windows tonight — 15 days, 30 days — and take both to a lawyer this week → **end_hard**  _(FLAG: windowsKept)_
  - NOTE (shown after choosing): The windows are real and they are the last ones this story contains. What they would need is the thing the appeal needed: the whole evidence, demanded this time, and a record built instead of remembered.
- Accept the decision — the system has spoken twice → **end_hard**
  - NOTE (shown after choosing): It has, both times on the record it was handed. A status upheld is a status that answers clearance questions for years, which is the system's way of continuing to speak.

## [end_hard] Upheld, With Fifteen Days
*Day 172 — Friday, October 2, 2026 (dayOffset 172)*

**DEBRIEF:**

The indicated status was upheld — not on the whole truth of a Saturday couch fall, but on the record as it stood at the hearing: a consult's preliminary caveat and a summary's adjective, carrying the agency's burden of substantial evidence because the evidence that would have answered them was never demanded and never filed. The decision notes the remaining windows — reconsideration within 15 days, Commonwealth Court within 30 (23 Pa.C.S. § 6341(g)) — and they are real, but they are appeals of a record, and the record is the problem.

The verified law inside this ending: the agency's burden at the hearing is substantial evidence (§ 6341(c.2)(5)); the appellant's right to the investigation evidence (§ 6341(c.2)(4)) exists whether or not it is exercised; decisions come within 45 days (§ 6341(c.3)). Hannah used the 90-day window of § 6341(a)(2) and nothing else the statute offered her. A right unexercised is a door unopened — the hearing happened in the room the open doors would have furnished.

Notice where this was decided: not in the hearing room, but at the determination meeting, when the packet stayed home in a folder, and at the appeal's drafting, when the demand stayed out of the letter. Hearings announce outcomes. Filing decisions make them.

Honesty requires this: another hearing officer weighs a self-contradicting summary differently, and 'plausible' might have carried the day. Officers vary. What doesn't: substantial evidence is a modest burden, and modest burdens are carried by whatever paper is in the room. Bring the record — all of it, demanded and filed — or the room will be furnished by the other side.
