# THE FIRST 90 DAYS — Scenario 38: “The Card in the Door”

*Human-readable script. This document and `scenario-38.json` are generated from a single source and match node-for-node: same IDs, same order, same choices, same effects.*

**The family is fictional — a composite. No real person's story appears here.**

**Content note:** This scenario depicts the opening days of an investigation — a card left in a door, phone calls, a home visit, and paperwork. There is no graphic content. Players may skip any scene or use the quick exit at any time.

**How to read effects:** `cash −40` changes the player's cash. `FLAG: name` sets a flag the engine tracks. `HIDDEN + item` means the case file quietly records that item at this choice. `REQUIRES FLAG: name` means the choice is only available if that flag was set earlier.

Start date: Monday, April 6, 2026. Day offsets are days since the scenario's start date.

## [start] Wedged in the Door
*Day 0 — Monday, April 6, 2026 (dayOffset 0)*

You come up the walk with a grocery bag on each arm and find it at eye level, wedged where the door meets the frame: a county business card. On the back, in pen: 'Please call — Mr. Tomasetti,' and a number. Your daughter Anaya, six, is at the table inside doing what she calls homework and is mostly drawing horses.

The card says nothing else. Cards never do. Everything the card doesn't say is currently being said by your imagination, at volume.

**Choices:**
- Put the groceries away, sit down, and look at the card like a document instead of an omen → **n2**
  - NOTE (shown after choosing): It has a name, an agency, a number. Three facts. Fear will supply the rest for free, and bill you later.
- Call the number immediately, from the doorstep, groceries still in hand → **n2**
  - NOTE (shown after choosing): Calling fast feels like cooperation. Calling informed is cooperation. They are not the same call.

## [n2] Nine Minutes
*Day 1 — Tuesday, April 7, 2026 (dayOffset 1)*

Before any call, the house assembles its own facts. Your sister Luz meets Anaya's bus every school day — her shift ends at three, the bus comes at three-twenty. Last Tuesday, Luz's own bus broke down across town. Anaya waited at the stop, alone, for nine minutes, watched — it turns out — by a neighbor who did not know the arrangement, and who did the arithmetic a stranger does.

Nine minutes, once, with a reason. That is the whole event. What it becomes depends on the paper it lands on.

**Choices:**
- Write down Tuesday's timeline tonight — times, the broken bus, the nine minutes → **records**  _(FLAG: timelineWritten)_
  - NOTE (shown after choosing): Written tonight, it is a record. Written next week, it is a reconstruction. Files can smell the difference.
- Keep it in your head — it's simple, and true → **records**
  - NOTE (shown after choosing): Simple and true are qualities of the event. The file will grade the telling, not the event.

## [records] Know Your Own File First
*Day 2 — Wednesday, April 8, 2026 (dayOffset 2)*

There is a file already — an intake summary with the report's sentences in it. You can answer a file you haven't read, the way you can answer a letter you haven't opened: energetically, and at a disadvantage.

You make the request in writing: a copy of the record the agency holds about this report.

**Choices:**
- File the written request for the intake summary from your record → **prep**  _(FLAG: recordsRequested ; HIDDEN + Records — parent requested the intake summary in writing before the first interview)_
  - NOTE (shown after choosing): Under 55 Pa. Code § 3130.44(d), the record is released on request. The summary is one line: 'Child, 6, observed unsupervised at bus stop, Tuesday.' No nine minutes. No broken bus. One line is what you are answering.
- Skip it — you'll find out what it says at the visit → **prep**
  - NOTE (shown after choosing): You will find out the way the summary's author intended: as a conclusion already formed, in a room where you are the guest.

## [prep] Schedules, Gathered
*Day 3 — Thursday, April 9, 2026 (dayOffset 3)*

The proof of an arrangement is schedules: Luz's work schedule showing three o'clock, the transit alert about her bus that Tuesday (still in her phone, timestamped), and your own shift roster. Separately, they are clutter in three pockets. Together, assembled, they are an arrangement with one bad day in it — which is what actually happened.

Assembling things is a job. It is about to be yours.

**Choices:**
- Assemble them: Luz's schedule, the transit alert, your roster, the timeline → **eve**  _(FLAG: proofGathered ; HIDDEN + Proof — sister's schedule, transit disruption alert, and parent's roster collected)_
  - NOTE (shown after choosing): Four documents. The nine minutes shrink back to their actual size, on paper, with timestamps.
- Decide you can explain the arrangement better than paper can → **eve**
  - NOTE (shown after choosing): You probably can, out loud, once. Paper explains it every time the file is opened, including times you are not in the room.

## [eve] The Call, Rehearsed
*Day 4 — Friday, April 10, 2026 (dayOffset 4)*

Tomorrow you call Mr. Tomasetti. Anaya is asleep; the folder is thin; the phone is a small black door. You can treat the call as a conversation — warm, human, forgettable — or as the first document of the case, which, functionally, it is: he will write a summary of it before his coffee cools.

What he writes will begin with what you give him to write with.

**Choices:**
- Plan the call as a document: facts first, timeline offered, everything confirmed in writing after → **split**  _(FLAG: callPlanned)_
  - NOTE (shown after choosing): Short, dated, checkable. The call becomes an exhibit instead of an anecdote.
- Plan to be natural — people respond to people → **split**
  - NOTE (shown after choosing): They do. Files respond to paper. You are about to meet both, in that order.

## [split] The First Call
*Day 5 — Saturday, April 11, 2026 (dayOffset 5)*

He answers on the second ring, and he is not a villain; he is a man with a caseload, reading from a one-line summary. 'We had a report your daughter was alone at the bus stop.' The call will go one of two ways, and the difference is not tone.

It is whether, when he hangs up, there exists a piece of paper with your name on it that says what you said.

**Choices:**
- Give the short account — and then confirm the call in writing, timeline and schedules attached → **p1**  _(FLAG: callConfirmed ; HIDDEN + Response — parent confirmed the first call in writing, with timeline and schedules attached)_
  - NOTE (shown after choosing): His summary and your letter land in the file on the same day, saying the same things. The file's first draft of your family is co-authored.
- Give the short account, warmly, and let the call be the record → **u1**  _(HIDDEN + Response — parent's account given by phone; no written confirmation sent)_
  - NOTE (shown after choosing): He writes it up kindly. Kindly is not the same as precisely. One word in his summary will do quiet damage for months.

## [p1] His Summary, and Yours Beside It
*Day 7 — Monday, April 13, 2026 (dayOffset 7)*

Two days later he calls back — a different call than it would have been. 'Your letter's in the file,' he says. 'The timeline checks out with the transit alert.' The home visit is scheduled, and he tells you what it will cover, because people tell you more when you've shown them paper.

Luz will be there. The arrangement will be demonstrated, not described.

**Choices:**
- Ask him to note in the file that the visit is by agreement, at a set time → **p2**
  - NOTE (shown after choosing): Noted. Small sentences in files are load-bearing.
- Thank him and prepare the house within an inch of its life → **p2**
  - NOTE (shown after choosing): The house is fine. The file is what he's grading, and the file is already better than the house needs to be.

## [p2] The Visit, Demonstrated
*Day 8 — Tuesday, April 14, 2026 (dayOffset 8)*

Luz comes at three. At three-twenty, on the dot, she walks the route to the stop with Anaya while Mr. Tomasetti watches the choreography that happens every school day: the wave from the corner, the key, the snack, the horses. He asks Luz two questions and writes down her answers next to yours, where they agree, because you gave them to him in the same words twice — once on the phone, once on paper.

Before he leaves, he describes the arrangement back to you, and suggests putting it in the file as the plan.

**Choices:**
- Ask for the plan as he described it — in writing, with the backup arrangement named → **p3**  _(FLAG: planInWriting)_
  - NOTE (shown after choosing): A plan in writing is a plan you can be measured against — which cuts both ways, and both ways are fairer than being measured against a summary of a phone call.
- Agree warmly and skip the writing part → **u3**  _(HIDDEN + Plan — arrangement agreed verbally at the visit; no written copy to parent)_
  - NOTE (shown after choosing): Warm agreement, cool record. If the arrangement is ever described by someone else, the file will contain a plan-shaped space.

## [p3] The Backup Gets Tested
*Day 10 — Thursday, April 16, 2026 (dayOffset 10)*

On Thursday, Luz's shift changes with four hours' notice — the arrangement's first weather. The backup in the written plan is the neighbor across the hall, Mrs. Harkins, who has known Anaya since she was two. She meets the bus. It is noted in the plan's own log line, in the file, as the plan working.

Plans are not proven by the weeks nothing happens. They are proven by the Thursday something does.

**Choices:**
- Log the afternoon in your own notes tonight — date, time, who met the bus → **p4**  _(FLAG: ownNotes)_
  - NOTE (shown after choosing): Your notes and the file's now agree. Agreement between records is the quietest form of winning.
- Skip the notes — the day worked out → **p4**
  - NOTE (shown after choosing): It did. Worked-out days still benefit from being written down, because the next reader was not there.

## [p4] Closing, In Preparation
*Day 12 — Saturday, April 18, 2026 (dayOffset 12)*

Mr. Tomasetti calls: the investigation is concluding. The determination will be that the report is not supported — a single brief lapse in an otherwise documented arrangement, already addressed by the family. He offers to send the closing summary.

Your folder and his have been saying the same things for two weeks. That is not an accident. That is the whole method.

**Choices:**
- Ask for the closing summary in writing, for your folder → **p5**  _(FLAG: copyFiled)_
  - NOTE (shown after choosing): It arrives in three days. Your side of this story now lives in two buildings, saying the same thing.
- Let his file be the only copy → **p5**
  - NOTE (shown after choosing): His file is a fine home for it. Yours would have been a second one.

## [p5] The Last Paragraph
*Day 14 — Monday, April 20, 2026 (dayOffset 14)*

The closing summary arrives. It is accurate in every paragraph but the last, where the arrangement is described as 'created in response to agency involvement' — as if Luz, the schedules, the three-twenty bus, began the day the card landed in your door. They didn't. The file's own earlier pages prove they didn't — if anyone reads them in order.

There is a line for your signature: acknowledgment of receipt.

**Choices:**
- Read it all, sign the acknowledgment — and attach a one-line note with the arrangement's real history → **end_good**  _(FLAG: readBeforeSigning)_
  - NOTE (shown after choosing): One line: 'Family arrangement predates the report; see intake response, April.' The last paragraph now argues with a footnote, and the footnote is right.
- Sign it at the door — it's closed, that's what matters → **end_partial**
  - NOTE (shown after choosing): It is closed. The summary's version stands unamended: an arrangement 'created in response to agency involvement.' Nobody will ever know it wasn't — but the file.

## [end_good] The Call, On Paper
*Day 16 — Wednesday, April 22, 2026 (dayOffset 16)*

**DEBRIEF:**

The investigation closed as unfounded, and the file — unusually — reads like the family it describes: an arrangement that existed, one bad Tuesday, a backup that worked on its first test. What won was not charm on a phone call. It was that the call existed in two forms, his summary and your letter, and they agreed, because you wrote yours.

The record inside this story: under 55 Pa. Code § 3130.44(d), the one-line intake summary came from your record, on request — which is how you knew the file's question was nine minutes long before you answered it. Everything after was the same move at different scales: timeline, schedules, plan, correction. In writing, dated, filed.

Notice what the written plan did when Luz's shift changed: it converted a second 'lapse' into a demonstration. Unwritten arrangements cannot do that. They can only be described, afterwards, by whoever holds the pen.

Honesty requires this: Mr. Tomasetti read the paper fairly, and a different worker summarizes your letter as 'father is fixated on documentation,' and the same moves curdle. Workers vary. The paper doesn't guarantee the reader. It guarantees only that the reader meets your version in your words, first, in order.

## [u1] Routinely
*Day 7 — Monday, April 13, 2026 (dayOffset 7)*

His summary of the call is kind, professional, and one word wrong. The one line in the file now reads: 'Father states daughter is met at bus by sister; one lapse occurred.' But in his spoken summary to his supervisor — the part that gets typed into the assessment — the sentence became: 'child routinely waits at bus stop.'

Routinely. Nine minutes, once, with a broken bus — and the file's adverb says it happens all the time. Adverbs are how files exaggerate without lying.

**Choices:**
- Call him and ask how the arrangement gets described accurately — in writing → **u2**
  - NOTE (shown after choosing): There is a way. It is the way it always was. It now has to correct a sentence instead of preventing one.
- Let it go — he meant well, and the visit will clear it up → **u2**
  - NOTE (shown after choosing): The visit will be conducted by a man reading his own summary on the way to your door. It clears up what it confirms.

## [u2] The Repair Door
*Day 8 — Tuesday, April 14, 2026 (dayOffset 8)*

He is plain on the phone: bring the paper — Luz's schedule, the transit alert, your timeline — and the summary can be corrected before the file hardens. Supervisors read files, not memories of phone calls.

It is the same door as before, with the draught coming through: your account, in writing, this week.

**Choices:**
- Assemble it and send the written account — timeline, schedules, transit alert — today → **p3**  _(FLAG: accountSent ; HIDDEN + Response — parent's written account with schedules provided after the first summary)_
  - NOTE (shown after choosing): It lands in the file behind his summary, dated. Files are read in order; your paper will sit right behind the word 'routinely' and correct it forever.
- Tell him you'll explain it all at the visit, face to face → **u3**  _(HIDDEN + Response — explanation deferred to the home visit; documentation not yet provided)_
  - NOTE (shown after choosing): Face to face is warmer. It is also, to the file, indistinguishable from not yet.

## [u3] The Plan, Handed Down
*Day 10 — Thursday, April 16, 2026 (dayOffset 10)*

At the visit — Luz at work, because nobody scheduled around her — the arrangement is described by the person who wasn't there to see it, to the person who wrote 'routinely.' The plan that arrives is pre-written: daily check-in calls for a month, the bus stop arrangement 'to be monitored,' a review in sixty days.

Anaya's afternoons have not changed. What changed is who authored the plan about them, and how much trust its terms assume.

**Choices:**
- Read the plan carefully and ask what would end the check-ins early → **u4**
  - NOTE (shown after choosing): A fair question, and a fair answer: a clean month, documented. Documented is doing heavy lifting in that sentence.
- Sign it to get the meeting over with → **u4**
  - NOTE (shown after choosing): It is signed either way. The difference is whether you know what it says.

## [u4] A Clean Month, Documented
*Day 12 — Saturday, April 18, 2026 (dayOffset 12)*

He offers the door plainly: one month of afternoons, documented — Luz's arrivals logged, the backup named in writing, any late day explained the same day — and the check-ins end early and the summary gets rewritten with the arrangement described as it actually is.

It is the same work as the letter would have been. It is simply later, and louder, and done under supervision instead of at a kitchen table.

**Choices:**
- Do the month in writing — log every afternoon, name the backup, send the packet at month's end → **p5**  _(FLAG: packetSent ; HIDDEN + Documentation — parent submitted a documented month of the bus-stop arrangement)_
  - NOTE (shown after choosing): The packet goes in complete. Whatever the closing letter concludes, the file's last word about Anaya's afternoons will be yours and dated.
- Do the month and trust the check-in calls to speak for themselves → **u5**
  - NOTE (shown after choosing): Check-in calls speak in checkboxes. Your packet would have spoken in sentences.

## [u5] Sixty Days
*Day 14 — Monday, April 20, 2026 (dayOffset 14)*

The month passes cleanly — because the afternoons were never the problem the one line imagined. Luz meets the bus; the backup covers once; the horses multiply on the refrigerator.

What remains open is the shape of the ending: whether the file closes this chapter with your documentation in it, or with one adverb and a plan you didn't write and nothing in your hand at all.

**Choices:**
- Wait for the closing summary → **end_partial**
  - NOTE (shown after choosing): It will come. They always come. The question was only ever what would be in the file when it was written.

## [end_partial] Routinely, In the File
*Day 16 — Wednesday, April 22, 2026 (dayOffset 16)*

**DEBRIEF:**

The investigation closed eventually — the afternoons were always sound — but it closed on the system's schedule and the system's terms: a plan handed down instead of demonstrated, a month of check-ins, and a file whose first draft of your family contains the word 'routinely,' uncorrected, where nine documented minutes should have been. Anaya stayed home throughout. What was lost was authorship.

The record inside this story: under 55 Pa. Code § 3130.44(d), the intake summary was yours for the asking, early — answering the one line with paper attached is a different call than answering it from memory and warmth.

Phone calls end. Their summaries don't. The first call in a case is a document whether you write it or not — the only choice is whose handwriting it's in.

Honesty requires this: Mr. Tomasetti offered a genuine repair door, and many workers would not have. A different office reads 'routinely' and escalates. You cannot choose the reader. You can choose whether your afternoons exist in the file before the reader forms an opinion.
