# THE FIRST 90 DAYS — Scenario 40: “The Letter with a Case Number”

*Human-readable script. This document and `scenario-40.json` are generated from a single source and match node-for-node: same IDs, same order, same choices, same effects.*

**The family is fictional — a composite. No real person's story appears here.**

**Content note:** This scenario depicts an investigation opened by letter — a response window, phone calls, a yard visit, and paperwork. There is no graphic content. Players may skip any scene or use the quick exit at any time.

**How to read effects:** `cash −40` changes the player's cash. `FLAG: name` sets a flag the engine tracks. `HIDDEN + item` means the case file quietly records that item at this choice. `REQUIRES FLAG: name` means the choice is only available if that flag was set earlier.

Start date: Monday, June 1, 2026. Day offsets are days since the scenario's start date.

## [start] The Envelope
*Day 0 — Monday, June 1, 2026 (dayOffset 0)*

The letter is on agency letterhead, which makes it heavier than the other mail. Inside: a case number, your name rendered correctly, and three paragraphs saying that a report has been received concerning your twins, Bram and Willa, four years old, and that an investigation is open. A worker, Mr. Halloran, will be in contact.

What the twins did, according to the street's retelling economy, is play in your front yard on a Saturday while you drank coffee on the porch — visible, but through a hedge, and therefore, to someone, 'outside alone.'

**Choices:**
- Read the letter twice, then put it — and its envelope — in a folder, together → **n2**  _(FLAG: envelopeKept)_
  - NOTE (shown after choosing): The envelope is a document: it carries the postmark, which carries the date, which carries the window. People throw away the envelope. Files are built by people who didn't.
- Read it once and leave it on the counter to deal with later → **n2**
  - NOTE (shown after choosing): Later is where windows go to close quietly.

## [n2] The Window
*Day 1 — Tuesday, June 2, 2026 (dayOffset 1)*

The letter is dated Wednesday. It arrived Saturday — the postmark says so, in smudged blue. The last paragraph contains the sentence that matters most and reads the dullest: responses and information may be submitted in writing, and the investigation will conclude within the period described.

A letter with a window in it is a clock wearing a disguise. The first skill is simply noticing it is ticking — and writing down, today, when it started and when it ends.

**Choices:**
- Write the dates on the folder: letter date, postmark, today — the window, made visible → **records**  _(FLAG: datesLogged ; HIDDEN + Deadlines — parent logged the letter's dates and response window from the postmark)_
  - NOTE (shown after choosing): Three dates on a folder tab. The investigation now has a shape you can plan against instead of a fog you worry inside.
- Trust you'll keep the timing in your head → **records**
  - NOTE (shown after choosing): Heads keep birthdays and grudges reliably. Administrative windows, less so.

## [records] Read the File You're Answering
*Day 2 — Wednesday, June 3, 2026 (dayOffset 2)*

A report exists in sentences somewhere: an intake summary. You can answer the letter's three careful paragraphs, or you can answer the report's actual claims. The second requires reading them, and the record is yours to request.

You make the request in writing: a copy of the record the agency holds about this report.

**Choices:**
- File the written request for the intake summary from your record → **prep**  _(FLAG: recordsRequested ; HIDDEN + Records — parent requested the intake summary in writing at the start of the investigation)_
  - NOTE (shown after choosing): Under 55 Pa. Code § 3130.44(d), the record is released on request. The summary says: 'Twins, 4, observed unsupervised in unfenced front yard, Saturday.' Three claims: unsupervised, unfenced, in the yard. You were on the porch. The fence exists — three sides of it. Now you know what you're answering.
- Skip it — the letter told you enough → **prep**
  - NOTE (shown after choosing): The letter told you there was a question. The summary is the question.

## [prep] The Yard, Documented
*Day 3 — Thursday, June 4, 2026 (dayOffset 3)*

The facts have artifacts. The porch, where you sat, in sight of the yard. The fence: three sides standing, and the fourth side — the gate side, by the driveway — where the latch failed in April. You texted the landlord about it; the thread is still in your phone, dated. On Sunday you replaced the latch yourself and kept the receipt.

A dated photo of the new latch, a screenshot of the April texts, and Mrs. Johansson from across the street — who watched the whole Saturday from her garden, coffee in hand, waving at the twins — are an answer, if they are assembled.

**Choices:**
- Assemble them: dated photo of the latch, the landlord texts, Mrs. Johansson's statement → **eve**  _(FLAG: proofGathered ; HIDDEN + Proof — dated latch photo, landlord message thread, and neighbor statement collected)_
  - NOTE (shown after choosing): Three artifacts, three dates, one Saturday. 'Unsupervised' and 'unfenced' are about to meet their paperwork.
- Decide the visit will sort it out — anyone can see the fence → **eve**
  - NOTE (shown after choosing): Anyone can. The file cannot. The file sees what is filed.

## [eve] The Night Before He Calls
*Day 4 — Friday, June 5, 2026 (dayOffset 4)*

Mr. Halloran calls tomorrow. The twins are asleep in the heroic sprawl of four-year-olds. Your folder holds the letter, the envelope, the summary, three artifacts. The call can be a conversation about a Saturday — or the delivery of an answer, in writing, inside the window the letter opened.

Paper has a property voices lack: it arrives before opinions finish forming, if you send it early enough.

**Choices:**
- Plan the call as delivery: the short account, then the written answer with artifacts, inside the window → **split**  _(FLAG: callPlanned)_
  - NOTE (shown after choosing): Account, artifacts, dates. The investigation's first draft of your Saturday gets co-authored.
- Plan to explain it naturally — it's a misunderstanding, and he'll hear that → **split**
  - NOTE (shown after choosing): He may. His summary will hear only what he writes, and summaries are written from paper or from memory — his, not yours.

## [split] The Call
*Day 5 — Saturday, June 6, 2026 (dayOffset 5)*

He is courteous and reads from the summary: 'Twins observed unsupervised in an unfenced yard.' This is the decision the week has been walking toward — not your tone, not your indignation, but whether the answer to those three claims exists in writing, with dates, while the window is open.

You can tell him about the porch, the latch, Mrs. Johansson. Or you can hand him all three, on paper, today.

**Choices:**
- Give the short account — and send the written answer today: porch, dated latch photo, landlord texts, neighbor statement → **p1**  _(FLAG: answerSent ; HIDDEN + Response — parent answered the report in writing, with dated documentation, inside the response window)_
  - NOTE (shown after choosing): It goes in dated, inside the window, against the summary's own three claims, one by one. Files respect answers that arrive shaped like them.
- Give the full account warmly by phone — the paper can follow if needed → **u1**  _(HIDDEN + Response — account given by phone; written answer and documentation not yet submitted)_
  - NOTE (shown after choosing): Warm, complete, and unrecorded. His summary of the call compresses your Saturday into a sentence with a word in it you will be meeting again.

## [p1] Point by Point
*Day 7 — Monday, June 8, 2026 (dayOffset 7)*

His reply, when it comes, has the structure of a man working down a list: porch — noted, corroborated by the neighbor. Latch — photographed, dated, replaced before the report was even written. Yard — fenced three sides, gate side now latched and documented. 'The summary,' he says, 'was thinner than the Saturday.'

It is as close as the system comes to saying the report described a yard that didn't exist.

**Choices:**
- Ask him to describe the amended findings — and to send them in writing → **p2**  _(FLAG: summaryInWriting)_
  - NOTE (shown after choosing): He will, and does. The file's thinnest page now has its thickest right behind it.
- Thank him and let the finding live in his file alone → **p2**
  - NOTE (shown after choosing): It lives there either way. Your copy is the one you can produce in a year, in one page, to a stranger.

## [p2] The Yard, Visited
*Day 8 — Tuesday, June 9, 2026 (dayOffset 8)*

The home visit is brief, because the yard does half the talking: fence, latch — he tests it, twice, like a man who has been lied to by latches — porch chair with its sightline to the sandbox. Mrs. Johansson, gardening with theatrical casualness across the street, confirms her Saturday view over the fence.

He writes for a while in the car before driving off. Long writing, after a visit like this, is the sound of a file agreeing with itself.

**Choices:**
- Ask what remains open, if anything → **p3**
  - NOTE (shown after choosing): 'The letter of determination,' he says. 'And your copies, if you want them.' You do. You've learned to want them out loud.
- Wave him off and reclaim the weekend → **p3**
  - NOTE (shown after choosing): The weekend is yours either way. So, now, is most of the file.

## [p3] Copies
*Day 10 — Thursday, June 11, 2026 (dayOffset 10)*

The determination is being drafted: not supported. He offers the closing documents — findings, summary, determination — as they're filed. Each one your folder receives becomes a second home for the record, in a building whose staff cannot be reassigned.

Twins, meanwhile, have discovered the gate latch's click and are conducting rigorous independent testing. The latch holds. So, increasingly, does the file.

**Choices:**
- Ask for copies of the closing documents as they're filed → **p4**  _(FLAG: copyFiled)_
  - NOTE (shown after choosing): They arrive in order, like the story. Your folder now holds the whole arc: letter, postmark, summary, answer, findings, closing.
- Let his file be the only copy → **p4**
  - NOTE (shown after choosing): His file is a fine home for it. Yours would have been a second one.

## [p4] The Determination Letter
*Day 12 — Saturday, June 13, 2026 (dayOffset 12)*

The determination letter is shorter than the first letter and says more: the report is not supported; the investigation is closed; the findings describe a supervised Saturday and a repaired latch, documented before the report was filed.

There is an acknowledgment line — receipt, not agreement — and, in the letter's summary paragraph, one eye-catching word choice about the yard, waiting to be read or missed.

**Choices:**
- Read the letter to the end before signing the acknowledgment → **p5**  _(FLAG: readBeforeSigning)_
  - NOTE (shown after choosing): The word is 'enclosed.' The yard is described as 'enclosed,' which it now is — the summary paragraph quietly credits the fence as found, and the timeline in the findings keeps the repair's true date. Both are worth noticing. One of them is worth a note.
- Sign it — closed is closed → **p5**
  - NOTE (shown after choosing): Closed is closed. Reading is how you'd know what closed means in this file's dialect.

## [p5] One Word
*Day 14 — Monday, June 15, 2026 (dayOffset 14)*

Here is the small print of victory: the findings have it right — latch failed in April, reported by you, replaced in May, before the report. The summary paragraph's 'enclosed' is harmless today. But summaries are what get quoted, and a future reader could mistake 'enclosed as found' for 'nothing was ever wrong here' — or worse, hold today's summary against a future, different Saturday.

One line, in writing, noting the findings' dates govern, keeps the record honest in both directions — including the direction that protects the agency's own file from its summary.

**Choices:**
- Send the one-line note: the findings' dates govern the summary's shorthand → **end_good**  _(FLAG: correctionSent)_
  - NOTE (shown after choosing): It is filed without ceremony. The record now corrects its own summary, permanently, in your hand — the last small discipline in a case made of them.
- Let it stand — the case is closed and the twins are four → **end_partial**
  - NOTE (shown after choosing): The case is closed. The summary sails on with 'enclosed' in it, and someday a reader will build a conclusion on the summary, the way readers do.

## [end_good] Kept, Dated, Answered
*Day 16 — Wednesday, June 17, 2026 (dayOffset 16)*

**DEBRIEF:**

The investigation closed with the report not supported — on a record that answered the report point by point, inside the window the first letter opened: a porch with a sightline, a latch photographed and dated, a repair that predated the report, a neighbor who watched it all. What won was clerical, mostly: an envelope kept, a postmark read, a window calendared, an answer filed while answers were still being taken.

The record inside this story: under 55 Pa. Code § 3130.44(d), the intake summary came from your record, on request — which is how you knew the claims were 'unsupervised' and 'unfenced' before you answered them, instead of answering the letter's fog. Windows matter in this system, and so does knowing precisely what you're answering.

Notice what the dates did: they made the repair older than the report. Sequence is an argument no one has to make out loud — the file makes it, in order, forever.

Honesty requires this: Mr. Halloran worked his list fairly, and a different worker files your answer unread behind a summary already drafted. Latches also fail again. You cannot choose the reader or the latch. You can choose whether the dates are in the file when both are tested.

## [u1] In the Yard
*Day 7 — Monday, June 8, 2026 (dayOffset 7)*

His summary of the call is professional, brief, and wrong in the way summaries specialize in: the twins were 'in the yard unsupervised for a period.' A period. Your porch, your coffee, your sightline — compressed into a preposition's worth of absence. The latch is not mentioned. The fence is 'partial,' which is true the way a three-legged chair is partial.

The window in the first letter is still open — for written answers, with dates. It will not stay open while you decide whether phone calls count.

**Choices:**
- Call and ask exactly what a written answer needs — then send it, inside the window → **u2**
  - NOTE (shown after choosing): Paper, dates, the neighbor. The same answer it always was — now filed against his sentence instead of before it.
- Assume the home visit will correct the record on its own → **u2**
  - NOTE (shown after choosing): Visits correct what visitors see. Summaries are corrected by paper, or they sail.

## [u2] The Repair Door
*Day 8 — Tuesday, June 9, 2026 (dayOffset 8)*

He is plain: a written answer, with the latch photo dated, the landlord thread, and a line from Mrs. Johansson — filed before the window closes — and the findings will be drafted on the whole Saturday instead of the summary's version of it.

It is the same door as before, with the draught coming through it, and a date on it now.

**Choices:**
- Assemble and file the written answer — photo, texts, neighbor's statement — inside the window → **p3**  _(FLAG: answerSent ; HIDDEN + Response — written answer with dated documentation filed inside the response window)_
  - NOTE (shown after choosing): It lands behind his summary, inside the window. Files are read in order; your answer will sit right behind the words 'for a period' and correct them forever.
- Send the photo alone — the rest is surely overkill → **u3**  _(HIDDEN + Response — latch photo submitted without the landlord thread or neighbor statement)_
  - NOTE (shown after choosing): The photo proves a latch. The thread proved you'd reported its failure in April; the neighbor proved the porch. One artifact carries one claim. The summary made three.

## [u3] Partial, Like the Fence
*Day 10 — Thursday, June 11, 2026 (dayOffset 10)*

The findings draft, when he reads it to you, reflects the arithmetic of what was filed: the latch, credited. The supervision claim — 'for a period' — stands, because the only account of the porch in the file is his summary of your phone call. Mrs. Johansson's Saturday remains unwitnessed by the record, because the record never received her.

A claim unanswered in writing is a claim answered by whoever wrote first.

**Choices:**
- Ask what would still be accepted before the determination is final → **u4**
  - NOTE (shown after choosing): The thread. The neighbor. In writing, this week — after which the determination drafts itself from whatever the file holds.
- Accept the draft — the case will close either way → **u4**
  - NOTE (shown after choosing): It will. Closures are shapes, and 'for a period' is the shape this one is taking.

## [u4] By the Window's End
*Day 12 — Saturday, June 13, 2026 (dayOffset 12)*

He offers it cleanly: the landlord thread and Mrs. Johansson's statement, filed before the window closes, and the findings get drafted whole — porch, repair history, Saturday — with the determination to match. After the window, the same paper becomes correspondence about a closed case, which is a weaker species of document.

Deadlines in this system are rarely announced twice. This one was announced in the first letter, in the dullest paragraph, which nobody reads. You read it. It is in your folder, with the envelope.

**Choices:**
- File the thread and the neighbor's statement before the window closes → **p5**  _(FLAG: answerComplete ; HIDDEN + Documentation — repair history and neighbor statement filed before the window closed)_
  - NOTE (shown after choosing): Complete, dated, in time. Whatever the letter concludes, the file's last word about that Saturday will be documented, witnessed, and yours.
- Let the window close — the photo should be enough → **u5**
  - NOTE (shown after choosing): Windows close without ceremony. So, mostly, do cases — around whatever happens to be inside them.

## [u5] Closed Around a Sentence
*Day 14 — Monday, June 15, 2026 (dayOffset 14)*

The determination is being drafted from the file as it stands: a credited latch, an unanswered 'period,' a fence described as partial. The case will close — it was always going to close; Saturdays on porches are not removals. What is being decided in the drafting is only what the closing documents will say the Saturday was.

Your folder holds a letter, an envelope, and a photograph. The file holds a sentence. One of these will be quoted someday, and it will not be the photograph.

**Choices:**
- Wait for the determination letter → **end_partial**
  - NOTE (shown after choosing): It will come. They always come. The question was only ever what would be in the file when it was written.

## [end_partial] Unsupervised, In the Summary
*Day 16 — Wednesday, June 17, 2026 (dayOffset 16)*

**DEBRIEF:**

The investigation closed — the twins were never in danger of anything but a description — but it closed with 'unsupervised for a period' in the findings, uncorrected, and a fence on record as 'partial.' Both sentences are false in the way that matters: they will be read, someday, by someone deciding something, as the truth about a Saturday you spent on your porch.

The record inside this story: under 55 Pa. Code § 3130.44(d), the intake summary was yours for the asking, early — and the window for written answers was printed in the first letter, in the envelope you almost threw away. Claims in this system are answered in writing, inside windows, or they are answered by the summary.

Notice the arithmetic that governed everything: three claims, three artifacts. The photograph answered one. The other two were answered by a phone call, which is to say, by the other side's summary of it.

Honesty requires this: Mr. Halloran offered the repair door plainly, twice, and many workers would not have. A different office drafts findings without reading answers at all. You cannot choose the reader. You can choose whether the whole Saturday — porch, texts, neighbor — is in the file before the reader writes 'findings.'
