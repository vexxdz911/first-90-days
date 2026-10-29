# THE FIRST 90 DAYS — Scenario 7: “The School Note” (Foundation tier)

*Human-readable script. This document and `scenario-7.json` are generated from a single source and match node-for-node: same IDs, same order, same choices, same effects.*

**The family is fictional — a composite. No real person's story appears here.**

**Content note:** This scenario depicts a school attendance warning, asthma appointments, a changed bus route, and answering a letter with proof. There is no graphic content. Players may skip any scene or use the quick exit at any time.

**How to read effects:** `cash −4` changes the player's cash. `FLAG: name` sets a flag the engine tracks. `HIDDEN + item` means the case file quietly records that item at this choice — the player does not see it when it happens. `NOTE:` is text shown to the player right after choosing.

Start date: Tuesday, September 8, 2026. Day offsets are days since the scenario's start date. Starting cash: $130.

## [start] The Letter from School
*Day 0 — Tuesday, September 8, 2026 (dayOffset 0)*

Your son Eli is nine, and small for it, and brave about exactly one thing: his inhaler, which he handles like a tool he respects. He has asthma — managed, documented, and mostly boring, which is how his doctor likes it.

This fall the district changed the bus routes. Eli's pickup moved twenty minutes earlier and two streets over, and the new stop has no shelter and a crossing guard who arrives when she arrives. Twice this month he has missed the bus entirely. Three times he has been late. And twice, breathing appointments across town ran long and swallowed a school morning.

**Choices:**
- Read the letter that came home in Eli’s backpack tonight → **n2**
  - NOTE (shown after choosing): Backpack letters are the school’s way of whispering. This one is not whispering.
- Put it with the other school papers and deal with it this weekend → **n2**
  - NOTE (shown after choosing): The letter has a date on it. Dates in letters are rarely decoration.

## [n2] Seven Absences, It Says
*Day 1 — Wednesday, September 9, 2026 (dayOffset 1)*

The letter is a warning: Eli's attendance shows seven absences and five tardies since September, and the pattern 'must improve.' It asks for a written response by Sunday, September 20, 2026, and it says a copy has gone to the family's support worker — which means it is in two files now, not one.

What the letter does not say: bus route, crossing guard, pulmonology. Letters like this count. Counting is all they do.

**Choices:**
- Call Ms. Ruiz, your family support worker, and tell her the letter came → **records**
  - NOTE (shown after choosing): She has seen the copy. "I wondered when you’d call," she says, in a tone that could go either way.
- Plan to explain it all at the next home visit → **records**
  - NOTE (shown after choosing): The home visit is in three weeks. The letter’s deadline is in twelve days. One of those dates matters to the letter.

## [records] The Record, Requested
*Day 2 — Thursday, September 10, 2026 (dayOffset 2)*

Before you answer a letter, it helps to know exactly what it was answering. Ms. Ruiz can show you the attendance summary the school sent — across a desk, briefly — or you can have your own copy, to sit with at your own table.

You ask, in writing, for a copy of the attendance summary and the school's referral note from your record, so your response can meet the actual numbers.

**Choices:**
- File the written request for the attendance summary and referral note → **prep**  _(FLAG: recordsRequested; HIDDEN + Records — parent requested copies of the attendance summary and school referral)_
  - NOTE (shown after choosing): Under 55 Pa. Code § 3130.44(d), the record is released on request. The summary arrives the next morning: seven absences, five tardies — and no codes, no notes, no reasons attached to any of them.
- Work from the letter’s numbers — seven and five are close enough → **prep**
  - NOTE (shown after choosing): Close enough is how a response ends up answering the wrong absence.

## [prep] Proof, Gathered Slowly
*Day 3 — Friday, September 11, 2026 (dayOffset 3)*

The proof exists. It is just scattered like Eli's homework: the district's route-change notice (mailed in August, filed by you under 'school stuff'), the clinic's appointment slips for the two breathing visits, and the pharmacy printout showing the new inhaler picked up on time, every time.

Nobody assembled it because assembling things is a job, and it was nobody's job. It is about to be yours.

**Choices:**
- Spend the evening assembling it: route notice, clinic slips, pharmacy printout → **eve**  _(FLAG: proofGathered; HIDDEN + Proof — district route-change notice and clinic slips collected by parent)_
  - NOTE (shown after choosing): Three documents and a timeline. The seven absences shrink, on paper, into two stories — a bus and a pair of lungs — both of them true.
- Decide the letter can be answered from memory — you lived those mornings → **eve**
  - NOTE (shown after choosing): You did. The file, however, was not there, and the file is who you are answering.

## [eve] The Draft
*Day 4 — Saturday, September 12, 2026 (dayOffset 4)*

At the kitchen table, with the summary on one side and the proof on the other, the response almost writes itself — or it would, if kitchen tables wrote letters. They don't. Pens do, held by tired people.

The deadline is Sunday, September 20, 2026. The school office, the support worker, and the file are all waiting to see what kind of answer yours will be: a document, or a conversation they have to remember for you.

**Choices:**
- Write the draft tonight, while the proof is warm → **split**  _(FLAG: draftWritten)_
  - NOTE (shown after choosing): Four paragraphs. No anger, no apology tour — just dates, documents, and a plan for the new bus stop.
- Sleep on it — there are still days left → **split**
  - NOTE (shown after choosing): There are. Days left is a resource that spends itself.

## [split] Send It, or Say It
*Day 5 — Sunday, September 13, 2026 (dayOffset 5)*

Morning. The response is drafted — or mostly drafted, in the way of things written at kitchen tables. The school office is on your way to work. Ms. Ruiz's next visit is not for weeks, but her phone number is right there, and explaining feels so much more human than envelopes.

The letter asked for a written response by a date. That request was not a formality. It was the whole game, stated plainly.

**Choices:**
- Send the written response — school and Ms. Ruiz — with the proof attached, before the deadline → **p1**  _(FLAG: responseSent; HIDDEN + Response — written response with documentation received before the deadline)_
  - NOTE (shown after choosing): Two copies mailed, one hand-carried, receipts kept. The answer now lives in every file the question lived in.
- Wait and explain it properly, in person, at the home visit → **u1**  _(HIDDEN + Response — no written response received by the deadline)_
  - NOTE (shown after choosing): The deadline passes quietly, the way deadlines do when nobody is watching them for you.

## [p1] Received and Stamped
*Day 7 — Tuesday, September 15, 2026 (dayOffset 7)*

The school secretary stamps your copy without looking up, which is the sound of a system working. Ms. Ruiz calls two days later, and her tone has changed — the letter is in front of her, with its little army of attachments.

'The route change,' she says. 'Nobody told us the stop moved.' Nobody had. Telling them, in writing, with the district's own notice attached, was the entire trick.

**Choices:**
- Ask her what happens to the absences now that the proof is in → **p2**
  - NOTE (shown after choosing): The two clinic mornings can be coded as medical. The bus mornings need a plan, not a code — and plans, she says, are next.
- Thank her and let the process take it from here → **p2**
  - NOTE (shown after choosing): The process is people with paper. Right now, the paper is good.

## [p2] Codes and Plans
*Day 8 — Wednesday, September 16, 2026 (dayOffset 8)*

The clinic absences are the easy part — slips in hand, they become 'medical' in the record. The bus mornings are the real item: five tardies and two missed buses, caused by a stop that moved and a guard who comes when she comes.

Ms. Ruiz proposes a short attendance plan: a neighbor two doors down — whose daughter rides the same bus — as the bad-morning backup, and a call to the school on any morning the bus fails, before first period.

**Choices:**
- Agree to the plan, and ask for it in writing with your name spelled right → **p3**  _(FLAG: planInWriting)_
  - NOTE (shown after choosing): A plan in writing is a plan you can be measured against — which cuts both ways, and both ways are fairer than being measured against a rumor.
- Agree warmly and skip the writing part → **u3**  _(HIDDEN + Plan — attendance plan agreed verbally; no written copy to parent)_
  - NOTE (shown after choosing): Warm agreement, cool record. If the plan is ever disputed, the file will contain a plan-shaped space.

## [p3] A Morning the Bus Fails
*Day 10 — Friday, September 18, 2026 (dayOffset 10)*

On Friday, September 18, 2026, the bus simply does not come — the plan's first test, arriving right on schedule, as tests do. The neighbor's daughter knocks at 7:05. By 7:20 Eli is in a car he knows, with a seatbelt he can work, driven two miles by a woman who has known him since he was four.

At 7:40 you call the school, per the plan, before first period. The absence-that-wasn't is logged as a plan success instead — your call, timed and noted.

**Choices:**
- Note the morning in your own records tonight — date, time, who drove → **p4**  _(FLAG: ownNotes)_
  - NOTE (shown after choosing): Your notes and the school’s now agree. Agreement between records is the quietest form of winning.
- Skip the notes — the day worked out → **p4**
  - NOTE (shown after choosing): It did. Worked-out days still benefit from being written down, because the next reader was not there.

## [p4] The Deadline, Met
*Day 12 — Sunday, September 20, 2026 (dayOffset 12)*

The response deadline arrives and finds nothing to punish: the letter is answered, the absences are coded, the plan is written and already tested once. Ms. Ruiz closes the school item in her review with a sentence you get to hear read aloud.

'Family responded in writing with documentation,' she reads. 'Attendance plan in place.' It is not poetry. It is better than poetry. It is a file, behaving.

**Choices:**
- Ask for a copy of the review page for your records → **p5**  _(FLAG: copyFiled)_
  - NOTE (shown after choosing): She prints it while you wait. Your side of this story is now in two buildings and your own folder, saying the same thing.
- Let the review live in her file → **p5**
  - NOTE (shown after choosing): Her file is a fine home for it. Yours would have been a second one.

## [p5] The Follow-Up Letter
*Day 14 — Tuesday, September 22, 2026 (dayOffset 14)*

A follow-up letter comes from the school: the warning is resolved, the plan continues, thank you for your response. It is the kind of letter that asks for nothing. It still gets opened carefully, at the kitchen table, the way all letters get opened now.

There is a line at the bottom to acknowledge receipt.

**Choices:**
- Sign the acknowledgment after reading it — and file the letter → **end_good**  _(FLAG: readBeforeSigning)_
  - NOTE (shown after choosing): Resolved, in writing, in your folder. The warning letter and its answer will outlive the bus route that caused them.
- Sign it at the door for the mail carrier’s convenience → **end_partial**
  - NOTE (shown after choosing): You miss the middle paragraph: the resolved warning stays on Eli’s school record as "resolved after escalation." Nothing escalated. Nobody will ever know that but you — and you didn’t read it.

## [end_good] Answered, With Proof
*Day 16 — Thursday, September 24, 2026 (dayOffset 16)*

**ENDING.** Debrief:

- The warning is resolved on the strength of an answer: written, documented, and early. The absences are coded for what they were — two medical mornings and a bus route the district moved — and the plan that replaced the warning was built with you, not handed to you.
- The law inside this story: under 55 Pa. Code § 3130.44(d), your copy of the attendance summary came from your record, on request. Answering the school's actual numbers — instead of the letter's summary of them — is what made the response land.
- Notice what won: not an argument, an assembly. Route notice, clinic slips, pharmacy printout, one kitchen-table letter. The school counted absences; you supplied the mornings.
- Honesty requires this: a school office can lose a stamped letter, and a support worker can read proof ungenerously. Ms. Ruiz read it fairly. Workers vary, offices vary, luck varies. A written answer is the only version of your mornings that attends every meeting after you.

## [u1] The Quiet Deadline
*Day 7 — Tuesday, September 15, 2026 (dayOffset 7)*

The deadline passes on an ordinary day. No one calls about it. That is the thing about deadlines in letters: they do not punish you loudly. They simply move your name from one mental pile to another in an office you will never see.

In the school file, the warning now carries a second line: 'No response received.' Four words, and every reader from now on will meet them before they meet you.

**Choices:**
- Call Ms. Ruiz now and tell her the explanation, before the visit → **u2**
  - NOTE (shown after choosing): Late is not never. But late is a genre, and you are now writing in it.
- Wait for the home visit — it’ll be better face to face → **u2**
  - NOTE (shown after choosing): It will be warmer face to face. It will also be three weeks after the letter asked, in writing, by a date.

## [u2] Explaining, Late
*Day 8 — Wednesday, September 16, 2026 (dayOffset 8)*

On the phone, the mornings sound like what they were: a bus, a boy, a pair of lungs, a mother doing arithmetic at a curb. Ms. Ruiz listens like a person. Then she does the thing people in her job must do — she asks what you can show her.

Memory is vivid on your side of the phone. On her side, there is a form, and the form has boxes, and none of the boxes is labeled 'she sounded sincere.'

**Choices:**
- Gather the proof now — route notice, clinic slips — and send the written response, late, with them attached → **p3**  _(FLAG: responseSent; HIDDEN + Response — written response with documentation received after the deadline)_
  - NOTE (shown after choosing): Late paper is still paper. It goes into the file with a date on it, and files are read in order — your answer will sit right behind the "no response" line and correct it forever.
- Tell her the proof is all at home somewhere, and you’ll bring it to the visit → **u3**  _(HIDDEN + Response — explanation given by phone; documentation not yet provided)_
  - NOTE (shown after choosing): Somewhere is not an address a file can use.

## [u3] The Plan, Handed Down
*Day 10 — Friday, September 18, 2026 (dayOffset 10)*

At the home visit — moved up, the way unanswered warnings move things up — the plan arrives already written: stricter than the one in the other version of this story, because it was built from a file with an unanswered warning in it. Daily check-ins for a month. A requirement to call the agency — not the school — on any absence, before 8 a.m. A review in sixty days.

Eli's mornings have not changed. What changed is who authored the plan about them, and how much trust its terms assume.

**Choices:**
- Read the plan carefully and ask what would shorten the check-in period → **u4**
  - NOTE (shown after choosing): A fair question, and she gives a fair answer: a clean month, documented. Documented is doing heavy lifting in that sentence.
- Sign it to get the meeting over with → **u4**
  - NOTE (shown after choosing): It is signed either way. The difference is whether you know what it says.

## [u4] A Clean Month, Documented
*Day 12 — Sunday, September 20, 2026 (dayOffset 12)*

She offers the door plainly: one month of mornings, documented — calls made, slips kept, the bus plan in writing — and the check-ins end early and the warning is marked resolved-with-monitoring instead of open.

It is the same work as the letter would have been. It is simply later, and louder, and done under supervision instead of at a kitchen table.

**Choices:**
- Do the month in writing — every call logged, every slip filed — and send the packet at month’s end → **p5**  _(FLAG: packetSent; HIDDEN + Documentation — parent submitted a documented month of attendance records)_
  - NOTE (shown after choosing): The packet goes in complete. Whatever the review concludes, the file’s last word about Eli’s mornings will be yours and dated.
- Do the month and trust the check-ins to speak for themselves → **u5**
  - NOTE (shown after choosing): Check-ins speak in checkboxes. Your packet would have spoken in sentences.

## [u5] Sixty Days
*Day 14 — Tuesday, September 22, 2026 (dayOffset 14)*

The month passes cleanly — because the mornings were never the problem the letter imagined. Eli rides the neighbor's car twice, the bus mostly behaves, the inhaler does its quiet work.

What remains open is the shape of the ending: whether the file closes this chapter with your documentation in it, or with the school's count and the agency's plan and nothing in your hand at all.

**Choices:**
- Wait for the review letter → **end_partial**
  - NOTE (shown after choosing): It will come. They always come. The question was only ever what would be in the file when it was written.

## [end_partial] A Warning Left Unanswered
*Day 16 — Thursday, September 24, 2026 (dayOffset 16)*

**ENDING.** Debrief:

- The warning resolved eventually — the mornings were always explainable — but it resolved on the system's schedule and the system's terms: a plan handed down instead of built, a month of check-ins, and a file whose first draft of your family was a count without reasons. Eli stayed home throughout. What was lost was authorship.
- The law inside this story: under 55 Pa. Code § 3130.44(d), the attendance summary in your record was yours for the asking, early — answering the real numbers, with proof attached, is a different letter than answering a warning from memory.
- Letters that ask for a written response by a date are not being formal. They are telling you the rules of the room your family will be discussed in: paper, dated, filed. This scenario is about answering in the room's language.
- Honesty requires this: Ms. Ruiz offered a genuine repair door, and many workers would not have. A different office escalates an unanswered warning further and faster. You cannot choose the reader. You can choose whether your mornings exist in the file before the reader forms an opinion.
