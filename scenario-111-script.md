# THE FIRST 90 DAYS — Scenario 111: “The Costs Column”

*Human-readable script. This document and `scenario-111.json` are generated from a single source and match node-for-node: same IDs, same order, same choices, same effects.*

**The family is fictional — a composite. No real person's story appears here.**

**Content note:** This scenario depicts a father whose son is in kinship care whose old fines-and-costs payment plan lapses on two late postings, and who misses a Saturday visit rather than drive against a clerk's letter, told through letters, receipts, a visit note, and a review. There is no graphic content. No rule about fines, costs, or driving is stated; the letters in the story state their own instructions. Players may skip any scene or use the quick exit at any time.

**How to read effects:** `cash −40` changes the player's cash. `FLAG: name` sets a flag the engine tracks. `HIDDEN + item` means the case file quietly records that item at this choice — the player does not see it when it happens. `REQUIRES FLAG: name` means the choice is only available if that flag was set earlier; `REQUIRES NO FLAG: name` means it is only available if that flag was never set. `NOTE:` is text shown to the player right after choosing.

Start date: Monday, August 17, 2026. Day offsets are days since the scenario's start date. Tier: Hard.

## [start] The Clerk's Letter
*Day 0 — Monday, August 17, 2026 — Monday, August 17, 2026 (dayOffset 0)*

Your name is Terrell. Your son Zane is six, and he is in kinship care with his aunt Sonya — placed before this story opens, in a house where his height is marked on a doorframe in pencil. Your case with Zane is one case. The letter in today's mail is from a different one.

The letter, dated Monday, August 17, 2026, is from a clerk's office, about an old matter from before Zane's case existed: fines and costs, long since assessed, that you have been paying down on a payment plan. The letter says, in its own words, that the plan has lapsed. It states its own deadline — respond and bring the plan current through the process it describes by Monday, September 7, 2026 — and it states, in its own words, its own consequence if you do not: your driving privileges will be acted on under the process the letter describes.

It is one page. It does not mention Zane, visits, or any court in his case. The two matters share nothing except you — and, as this story will show, a Saturday.

**Choices:**
- Read the letter a second time, including its deadline and its stated process → **letter_close**
  - NOTE (shown after choosing): The letter is the whole law of this scenario: what it says, by when, and what it says happens next. Read only that, and read it exactly.

## [letter_close] What Lapsed, Exactly
*Day 1 — Tuesday, August 18, 2026 — Tuesday, August 18, 2026 (dayOffset 1)*

On the second reading, the letter is precise in the way clerk's letters are precise: the plan exists; two payments are recorded as late; because of them, the plan is shown as lapsed. The letter does not say you did not pay. It says the payments posted late — recorded so, in a ledger, in a column.

Posted late is a phrase with two possible authors: a man who paid late, or a process that posted late. The letter, fairly, does not choose between them. It reports a ledger. Ledgers can be answered — with the paper that ledgers are made from, if the paper was kept.

Your payment receipts live the way most such paper lives: some in a drawer, some in a glove compartment, all of them real. Whether they survive as evidence depends on a decision you make this week, before any Saturday arrives to complicate it.

**Choices:**
- Look at the old plan itself — how it ran, before it lapsed → **old_plan**
  - NOTE (shown after choosing): A plan that ran for years and lapsed on two postings is a different object from a plan that was never honored. The drawer decides which one can be proved.

## [old_plan] The Plan That Ran
*Day 2 — Wednesday, August 19, 2026 — Wednesday, August 19, 2026 (dayOffset 2)*

The plan is old — older than Zane's case, older than Zane's school, a leftover column of numbers from a younger man's matter, paid down month by month in the unglamorous way such columns are paid: steadily, mostly on time, in amounts that were never large and never nothing.

Two payments in that long run are now recorded as late. You remember those months. You remember paying — at the counter, through the processor the plan uses, with receipts that printed warm. Paying and posting are different events, separated, in the processor's world, by days. In the ledger's world, only one of them has a date.

The letter's deadline stands at the date the letter stated. Before it stands a Saturday: Zane's visit, at Sonya's, across town — a drive you have made every week of his placement.

**Choices:**
- Find the receipts for the two payments the letter calls late → **receipts_choice**
  - NOTE (shown after choosing): Two months, two receipts. The whole first half of this scenario is whether warm-printed paper survived a glove compartment.

## [receipts_choice] Warm Paper, Kept or Lost
*Day 4 — Friday, August 21, 2026 — Friday, August 21, 2026 (dayOffset 4)*

The drawer and the glove compartment between them hold your payment history the way they hold everything: truly, and without an index. The two receipts in question exist — printed at the counter on the days you paid, showing the payment date, days before the dates the ledger recorded. Kept together, dated, they are the difference between a man who paid late and a posting that lagged. Left scattered, they are litter with numbers on it.

Gathering them costs an evening. The letter's clock, and Zane's Saturday, will not wait for a more convenient evening to exist.

**Choices:**
- Gather both receipts tonight and keep them with the letter, in date order → **receipts_found**  _(cash −3; FLAG: receiptsKept; HIDDEN + Payment receipts — both payments made before the ledger's posted dates; receipts kept)_
  - NOTE (shown after choosing): Three dollars of copies and a folder. The receipts now sit beside the letter they answer, which is where receipts do their work.
- Leave the receipts where they live — you know you paid, and that's the truth of it → **receipts_scattered**
  - NOTE (shown after choosing): It is the truth of it. Truth, unattached, is about to meet a ledger, and ledgers do not attend kitchen tables.

## [receipts_found] Paid, Then Posted
*Day 5 — Saturday, August 22, 2026 — Saturday, August 22, 2026 (dayOffset 5)*

Side by side, the paper tells a small, complete story. Receipt one: paid on its date, in the month the letter questions. The ledger's entry for that payment: posted days later, across the plan's due line. Receipt two: the same shape, the same lag, the same column's verdict — late. You paid on time, twice. A processor posted late, twice. The ledger recorded the second event and called it by the first event's name.

None of this, yet, is filed anywhere it matters. It is a folder on a table, on the morning of Zane's visit — and the letter, unanswered, has already stated what it says happens to your driving privileges if its process is not followed by its date.

**Choices:**
- Face the Saturday decision with the letter open on the table → **saturday_choice**
  - NOTE (shown after choosing): The visit is today. The letter is also today. This scenario lives in the space between those two sentences.

## [receipts_scattered] True, and Somewhere in a Drawer
*Day 5 — Saturday, August 22, 2026 — Saturday, August 22, 2026 (dayOffset 5)*

Your memory of the two payments is exact: the counter, the amounts, the warm receipts going into the glove compartment or the drawer or a coat. Any person who knows you believes the account instantly. The ledger, which does not know you, has already published its version: late, late, lapsed.

Today is Zane's visit — a drive across town, as every week — and the clerk's letter, unanswered on the table, has stated in its own words what it says happens to your driving privileges under its process. Memory does not answer letters. But the Saturday decision arrives whether memory is ready or not.

**Choices:**
- Face the Saturday decision with the letter open on the table → **saturday_choice**
  - NOTE (shown after choosing): Two pieces of paper are in this room: a letter with a deadline, and a visit with a boy. Only one of them can be rescheduled by wanting to.

## [saturday_choice] The Saturday Decision
*Day 5 — Saturday, August 22, 2026 — Saturday, August 22, 2026 (dayOffset 5)*

The visit with Zane is today, Saturday, August 22, 2026, at Sonya's, across town. The drive is the ordinary drive of Zane's whole placement. The letter on the table says — in its own words, which are the only words this scenario treats as its process — that your driving privileges are acted on under its process if the plan is not brought current by the process and date it states, and that date has not yet come, and the plan is, on the ledger, lapsed today.

You can decline to drive against the letter: miss the visit, take the bus nowhere, and be a father who was not there on a Saturday his son counts by. Or you can drive anyway — the ordinary drive, on the ordinary road — and convert a paper problem, receipts and postings, into whatever a stop on that road would make of it.

There is no third option on the table. There is only the question of what gets written down afterward, and by whom.

**Choices:**
- Do not drive against the letter — miss the visit, and stay off the road until the letter's process is answered → **visit_missed**  _(FLAG: didNotDrive; HIDDEN + Visit — missed rather than drive against the clerk's letter; no written explanation sent that day)_
  - NOTE (shown after choosing): You stay home. The road stays un-driven. What the day will be recorded as is now entirely up to what the file gets told, and when.
- Drive anyway — the visit matters more than a clerk's column → **visit_driven**  _(FLAG: droveAnyway; HIDDEN + Visit — father drove to the visit while the letter's stated consequence was outstanding)_
  - NOTE (shown after choosing): The visit happens. The drive also happens, on a road where a paper problem can stop being paper at any set of lights.

## [visit_missed] The Empty Chair
*Day 6 — Sunday, August 23, 2026 — Sunday, August 23, 2026 (dayOffset 6)*

Saturday passes with an empty chair at Sonya's table. Zane asks where you are, in the direct way six-year-olds ask the only question there is, and Sonya answers kindly and truthfully, in the version available to her: something about a letter and a car. You call, that evening. Your voice is there. Your chair was not.

What you do not do — today, or in the days after — is tell anyone in writing. The call is warm, human, and unrecorded in every file that will ever be read by Zane's review. A missed visit, unexplained in writing, is a blank space in a log. Blank spaces, in this system, are filled by whoever writes next — and the next writer is never the father.

**Choices:**
- Read what the visit log writes about the Saturday you stayed home → **note_phrase**
  - NOTE (shown after choosing): Logs are short. That is not a mercy. Short is how a sentence gets quoted forever.

## [visit_driven] The Visit, and the Drive Back
*Day 6 — Sunday, August 23, 2026 — Sunday, August 23, 2026 (dayOffset 6)*

The visit is good — visits with Zane are good in the uncomplicated way that makes the rest of this case bearable — and the drive there is uneventful. The drive back is the one the letter was about: a paper status, traveling at road speed, through a world where statuses get checked. Nothing, this time, checks yours. You arrive home with the visit kept and the gamble won, this time.

What the file records is a kept visit. What it does not record is the drive. Both facts are now true, and only one of them is in any file — until the day, if it comes, when the other one gets written by someone whose job is writing exactly that.

**Choices:**
- Go on into the week — the letter still on the table, its date still coming → **note_phrase**
  - NOTE (shown after choosing): Kept visits are recorded. Kept gambles are recorded later, by other hands, if they are recorded at all.

## [note_phrase] No Explanation
*Day 8 — Tuesday, August 25, 2026 — Tuesday, August 25, 2026 (dayOffset 8)*

On Tuesday, August 25, 2026 you see the visit note, because Sonya, who keeps her own copies of everything in a labeled binder that shames your drawer, shows you hers. If you stayed home, the note reads, in full: 'Father missed visit, no explanation.' Three facts in six words, and one of them — the explanation — is false in the way an absence can be false: there was an explanation. It was a letter, a deadline, and a stated consequence. It simply was never sent anywhere the note's author could read it.

If you drove, the note reads 'visit held,' and is true, and sits in the file beside a drive that no note mentions. Either way, the file's account of that Saturday is now a sentence other people will quote, and the only question left is whether your paper ever joins it.

A second envelope from the clerk's office is already in the mail. In this system, second envelopes are how first letters grow.

**Choices:**
- Open the second envelope when it comes → **second_letter**
  - NOTE (shown after choosing): You already know its shape. What you do not know is its number — second letters in this column always have a bigger one.

## [second_letter] The Balance, Grown
*Day 11 — Friday, August 28, 2026 — Friday, August 28, 2026 (dayOffset 11)*

The second letter arrives on Friday, August 28, 2026. It restates the lapsed plan. It raises the balance: added costs, listed in its own column, in its own words, bringing the total to the figure it states. And it repeats its process: the form it encloses, the office it names, and its own new deadline — Friday, September 18, 2026 — for bringing the plan current or having it reinstated through the process the letter describes.

Two letters now. Between them they contain every procedural fact this scenario will ever use: dates, amounts as the letters state them, a form, an office, deadlines, consequences in the letters' own words. No other law of fines or driving will be consulted, because none is needed: the letters are the process, and the process can be followed, in writing, on time.

Zane's review is also coming — the room where 'no explanation' will be read, unless the explanation, in writing, gets there first.

**Choices:**
- Lay both letters beside the receipts and the visit note, and call your lawyer in Zane's case → **ledger_beat**
  - NOTE (shown after choosing): Four documents, two cases, one kitchen table. Lawyers in this series earn their keep at exactly this table.

## [ledger_beat] Receipts Against a Ledger
*Day 12 — Saturday, August 29, 2026 — Saturday, August 29, 2026 (dayOffset 12)*

Receipts against a ledger is a fair fight, if it is ever actually fought. The receipts say paid, with dates. The ledger says posted, with later dates. Two of the plan's late entries are the distance between those two columns — a processor's lag, measurable in days, provable in print, if the print is assembled and filed in both directions: to the clerk's process, to answer the letters, and into Zane's record, to answer the note.

The explanation for the missed visit is, at bottom, the same document set: the first letter, dated before the Saturday it cost; the stated consequence, in the letter's own words; and the receipts showing why the letter was wrong about the lapse that triggered it. One packet, two files, every date in it older than the events it explains — because the letter itself predates the Saturday. That sequence is the explanation's whole strength: it cannot have been invented afterward, because its first page was mailed before.

**Choices:**
- Ask your lawyer how each file gets its copy, in writing → **counsel_visit**
  - NOTE (shown after choosing): You have a lawyer in Zane's case. What the clerk's file needs, she will tell you, is its own process, followed on its own paper.

## [counsel_visit] Two Files, One Packet
*Day 13 — Sunday, August 30, 2026 — Sunday, August 30, 2026 (dayOffset 13)*

You have had a lawyer throughout Zane's case, as the law provides (42 Pa.C.S. § 6337). Ms. Rutledge reads both letters, the receipts, and Sonya's note copy, in that order, and says the sentence this scenario has been walking toward: 'The letter explains the Saturday. But a letter in your drawer explains it to your drawer. Filed, it explains it to every reader the note will ever have.'

'Two filings, then. The clerk's, through the process the letters themselves describe — the form, the receipts, the reinstatement request. And Zane's: a written explanation, filed before the review, attaching the first letter, so the visit note and the reason for the visit's absence travel together from now on.'

Or the explanation can stay where it has lived since Saturday: in phone calls, in Sonya's kindness, in your own certainty — everywhere except a file.

**Choices:**
- Ask for Zane's file itself — the visit note in its official copy → **records_fork**
  - NOTE (shown after choosing): 'Quote it exactly, or correct a summary of it,' she says. 'There is no third kind of correction.'

## [records_fork] Ask for the Visit Record
*Day 15 — Tuesday, September 1, 2026 — Tuesday, September 1, 2026 (dayOffset 15)*

A party may request the case record, and the material in it 'shall be released upon request' (55 Pa. Code § 3130.44(d)). The visit notes and the review summary are part of that record: the note in its official wording, and any summary already carrying the Saturday forward in its own words.

The alternative is to write the explanation against Sonya's copy and your memory of the note — close, probably, and unverifiable in exactly the way that lets a room keep its original sentence.

**Choices:**
- Sign the written request for the record — visit notes and draft summary → **record_arrives**  _(cash −3; FLAG: recordsRequested; HIDDEN + Case record — requested in writing, including the visit note and draft review summary)_
  - NOTE (shown after choosing): Signed, dated, copied. The note's exact six words are about to be in your hands, where corrections can reach them.
- Write against Sonya's copy — her binder has never been wrong yet → **no_record**
  - NOTE (shown after choosing): Her binder is excellent. It is also hers. The file's copy is the one the review will read, word for word.

## [record_arrives] Six Words, Officially
*Day 21 — Monday, September 7, 2026 — Monday, September 7, 2026 (dayOffset 21)*

The packet arrives on Monday, September 7, 2026 — the same date the first letter stated as its deadline, which has its own quiet symmetry. The visit note is there in its official copy, exactly as Sonya's binder promised: 'Father missed visit, no explanation' (or, on the road not taken, 'visit held,' with no sentence anywhere about a drive). The draft review summary carries the Saturday in the file's grammar, one line, unadorned.

A draft is a mercy, if you get to see it in time: every line in it is still soft enough to be joined by another line. The joining document is the explanation — and its first attachment predates the Saturday, which is a property no document created now can fake.

**Choices:**
- Decide how the explanation is filed — in writing before the review, or aloud at it → **explanation_choice**
  - NOTE (shown after choosing): Before, it joins the note. At, it argues with it. The note has waited patiently; it can afford to. It is already filed.

## [no_record] The Note, at One Remove
*Day 21 — Monday, September 7, 2026 — Monday, September 7, 2026 (dayOffset 21)*

Without the packet, the explanation will be written against a copy of a copy: Sonya's binder version of a note, your memory of a Saturday, a lawyer's draft of both. It may still be filed. But the review reads the file's wording, and a correction aimed one word off its target is a correction a room can honestly call unproven.

Ms. Rutledge is plain: 'We file what we can. Understand what it will be weighed as: an account, not a joining. The note stays the file's sentence; ours becomes its footnote, if we are lucky.'

**Choices:**
- Decide how the explanation is delivered — in writing before the review, or aloud at it → **explanation_choice**
  - NOTE (shown after choosing): Footnotes are not nothing. They are also not the text. Choose with the difference in view.

## [explanation_choice] The Explanation, Filed or Spoken
*Day 24 — Thursday, September 10, 2026 — Thursday, September 10, 2026 (dayOffset 24)*

The written explanation is short, because its attachments do the work: one paragraph — the visit was missed (on the road where it was missed) because a clerk's letter, dated before that Saturday, stated a consequence for driving that the father would not drive against; the letter is attached, with its date; the receipts are attached, showing the lapse behind the letter was a posting lag, not a nonpayment. It asks that the explanation be filed with the visit note and reflected in the summary.

Filed before the review, it is a joining: note and reason, traveling together. Spoken at the review, it is a story told to people holding the note — believed, perhaps, and entered nowhere.

**Choices:**
- File the written explanation before the review — first letter and receipts attached → **explanation_filed**  _(cash −4; FLAG: explanationFiled; HIDDEN + Written explanation — filed before the review, with the pre-Saturday letter and payment receipts attached)_
  - NOTE (shown after choosing): Stamped, copied, joined to the note it answers. Every future reader of that Saturday now reads it in the order it happened.
- Explain it at the review — your voice, and Sonya's, will carry it → **explanation_oral**
  - NOTE (shown after choosing): Voices carry rooms. Files carry reviews, and every room after this one. The note is a file. Your voice, that day, will not be.

## [explanation_filed] Joined, Not Argued
*Day 26 — Saturday, September 12, 2026 — Saturday, September 12, 2026 (dayOffset 26)*

The explanation goes in with its attachments, and the file accepts it the way files accept everything: without comment, and permanently. The visit note now has company of a kind notes rarely get — a dated, earlier letter that makes the note's last two words ('no explanation') simply inaccurate as a description of the record, whatever they described about that Saturday's phone calls.

Ms. Rutledge keeps her copy. Sonya, told about it, adds her own copy to the labeled binder, with a tab. The binder, at least, was always a file. Now Zane's is one too.

**Choices:**
- Turn to the clerk's letters themselves — the plan still stands lapsed on their paper → **reinstatement_choice**
  - NOTE (shown after choosing): One file corrected. The other file — the one with the column — is still waiting for its own process to be followed.

## [explanation_oral] True, at Speaking Speed
*Day 26 — Saturday, September 12, 2026 — Saturday, September 12, 2026 (dayOffset 26)*

The explanation stays in the world of voices: yours, Sonya's, Ms. Rutledge's assurance that it will be raised. Raised is a tense that reviews are fluent in discounting. The note, meanwhile, sits in the draft summary, filed, quoted, at rest — a sentence with a head start measured in weeks.

What can still be done, fully and on time, is the other filing: the clerk's own process, in the clerk's own window, with the receipts that answer its ledger.

**Choices:**
- Turn to the clerk's letters themselves — the plan still stands lapsed on their paper → **reinstatement_choice**
  - NOTE (shown after choosing): Ledgers, unlike reviews, can only be answered one way: in their own process, with their own paper, by their own dates.

## [reinstatement_choice] The Letters' Own Process
*Day 28 — Monday, September 14, 2026 — Monday, September 14, 2026 (dayOffset 28)*

The second letter stated the process on its face: its enclosed form, its named office, its deadline of Friday, September 18, 2026. The reinstatement request, assembled, is the ledger's answer in the ledger's language: the form, the two receipts with their payment dates, and a one-line request that the plan be reinstated on the ground the documents state — the payments were made on time and posted late, by days, through the processor.

Filing it costs copies and a fare. Not filing it costs nothing this week, and leaves two letters, a grown balance, and a stated consequence all standing in their harder tense at their stated date.

**Choices:**
- File the reinstatement request through the letters' own process — form and receipts, inside the stated window → **reinstatement_filed**  _(cash −5; FLAG: reinstatementFiled; HIDDEN + Payment plan — reinstatement requested through the letters' own process, receipts attached, inside the window)_
  - NOTE (shown after choosing): Filed with days to spare. The ledger now has to reckon, in its own column, with the receipts' dates sitting beside its own.
- Let the letters wait — Zane's review matters more than an old column → **reinstatement_ignored**
  - NOTE (shown after choosing): Reviews do matter more. Columns, unattended, do not stay columns. That is the second letter's whole message, in its own words.

## [reinstatement_filed] Filed, in Its Own Language
*Day 30 — Wednesday, September 16, 2026 — Wednesday, September 16, 2026 (dayOffset 30)*

Filed on Wednesday, September 16, 2026, inside the window the second letter stated. The office's receipt is a small, stamped thing, and you keep it the way you now keep everything: dated, copied, with the letters it answers. Whatever the office decides, it will decide it about documents — a ledger's dates against receipts' dates — which is the first fair fight this old column has ever been offered.

Zane's next visit, meanwhile, is coming on its ordinary Saturday rhythm, and the road to Sonya's is, for now, a road the letters' process is actively answering.

**Choices:**
- Take the bus-and-ride Saturday combination to Zane's next visit, carefully, while the filing is read → **zane_visit**
  - NOTE (shown after choosing): Slower, costlier in time, and entirely off the ledger's road. Visits, unlike columns, cannot be reinstated once missed. They can only be kept, one by one.

## [reinstatement_ignored] The Column, Standing
*Day 30 — Wednesday, September 16, 2026 — Wednesday, September 16, 2026 (dayOffset 30)*

The letters wait, in the way letters with stated dates wait: briefly, and then not at all. The balance stands with its added costs. The stated consequence stands in the second letter's words. And the road to Sonya's — the ordinary Saturday road of Zane's whole placement — now carries all of it, unaddressed, at road speed.

Zane's next visit arrives on schedule regardless. Schedules in this story have never once consulted the files they run beside.

**Choices:**
- Face the next visit with the letters still unanswered → **zane_visit**
  - NOTE (shown after choosing): A boy, a Saturday, a road, and a column. The visit will be recorded. So, in their ways, will the other three.

## [zane_visit] The Next Visit, Kept
*Day 33 — Saturday, September 19, 2026 — Saturday, September 19, 2026 (dayOffset 33)*

The visit on Saturday, September 19, 2026 is kept — by whatever road your choices have left open, it is kept, and it is good: Zane has a doorframe measurement to report and a joke he has been saving, in the way six-year-olds save jokes, by telling it immediately. Sonya feeds everyone. The visit note, this time, will say the visit was held, because it was.

One kept visit does not erase a missed one in a log. Logs are cumulative, not merciful. What decides the missed one's meaning at the review is whether its explanation is in the file beside it — and whether the letters that caused it are being answered in their own process or ripening in their drawer.

**Choices:**
- Prepare for the review with Ms. Rutledge → **prep**  _(HIDDEN + Visits — subsequent visit kept; explanation and reinstatement filings pending the review)_
  - NOTE (shown after choosing): Kept, and noted as kept. The review will now read two Saturdays, and whatever paper joins each of them.

## [prep] Two Saturdays, in Two Piles
*Day 38 — Thursday, September 24, 2026 — Thursday, September 24, 2026 (dayOffset 38)*

Ms. Rutledge spreads the matter in two piles. Pile one: a clerk's first letter, a ledger's two late postings, a six-word visit note, a second letter with a grown balance. Pile two — if your choices built it — two warm-printed receipts with earlier dates than the ledger's, a record packet quoting the note exactly, an explanation filed before this room convenes with the pre-Saturday letter attached, and a reinstatement request filed inside the second letter's own window.

'The review will read the missed Saturday from one of these piles,' she says. 'Our whole job, for six weeks, was choosing which.'

**Choices:**
- Assemble the packet in date order, with copies → **review**  _(cash −4; HIDDEN + Review packet — letters, receipts, visit note and filed explanation, in date order)_
  - NOTE (shown after choosing): Date order matters here more than anywhere in this series: the letter predates the Saturday. The packet's order is its proof.

## [review] The Review
*Day 44 — Wednesday, September 30, 2026 — Wednesday, September 30, 2026 (dayOffset 44)*

The review convenes on Wednesday, September 30, 2026. Zane's plan is the business of it; the missed Saturday is one line — and lines, in reviews, are read from the note unless something filed displaces them. The clerk's matter is not before this room, and Ms. Rutledge does not pretend otherwise: what is before this room is a visit note, and what a father's other file did to a Saturday. She rises with whatever your choices actually put in her hands.

Choose the presentation the paper you built can carry.

**Choices:**
- Present the joined record — the explanation filed before today, the pre-Saturday letter, and the receipts, with the plan's reinstatement filed → **end_win**  _(REQUIRES FLAG: receiptsKept; REQUIRES FLAG: recordsRequested; REQUIRES FLAG: explanationFiled; REQUIRES FLAG: reinstatementFiled; REQUIRES NO FLAG: droveAnyway)_
  - NOTE (shown after choosing): This presentation exists because the explanation was filed, not spoken — and because its first attachment is dated before the Saturday it explains.
- Explain the Saturday aloud — the letter, the road, the choice you made → **end_note_stands**
  - NOTE (shown after choosing): Every word true. The note, printed and already read, sits across the table with the head start this scenario measured in weeks.
- Present the kept visit and let the drive stand as the answer → **end_drove**  _(REQUIRES FLAG: droveAnyway)_
  - NOTE (shown after choosing): The visit was kept. This presentation asks the room to price the visit and ignore the road it took to get there.

## [end_win] Ending — Explained, On the Record
*Day 51 — Wednesday, October 7, 2026 — Wednesday, October 7, 2026 (dayOffset 51)*

**Ending.**

**Debrief:**
- WHAT THE FILE HELD (the record, revealed): A Saturday, fully documented at last. A clerk's letter dated Monday, August 17, 2026 — before the missed visit — stating its own deadline and, in its own words, its own consequence for driving. Two payment receipts showing both questioned payments made on time and posted late by the processor, days later, across the plan's due line: the lapse was a posting lag, proved from the counter's own paper. A written explanation filed before the review, joining the letter and the receipts to the visit note, so that 'father missed visit, no explanation' no longer travels alone — at the review, the visit record was corrected on the record to state the explanation the documents carry. And in the clerk's own process, the reinstatement request — form and receipts filed on Wednesday, September 16, 2026, inside the second letter's stated window — reinstated the payment plan on the documented posting dates, the grown balance corrected to the plan's own terms as the letters describe them.
- THE PROCESS UNDER THIS PATH (described, keeping to this scenario's verified law): Two verified instruments did the joining in Zane's case: the case record, released on request (55 Pa. Code § 3130.44(d)), which put the note's exact wording in the father's hands while the draft summary was still correctable, and counsel (42 Pa.C.S. § 6337), who filed the explanation where the note lives. Everything in the clerk's matter — the lapse, the balance, the reinstatement — was handled through the letters' own stated process, on the letters' own forms, inside the letters' own windows, and this ending states no statute about fines, costs, or driving privileges because none was used and none is in the verified set: the letters were the process, followed exactly. Label this win honestly: it is partial. Zane remains in kinship care with Sonya, his case continues, the old column continues to be paid down month by month, and one Saturday with a six-year-old is gone in every ending this scenario has. What was won is that the record of that Saturday, and of the plan, now says what actually happened — in both files.
- THE HONEST PART: A different clerk's office could have read the same receipts ungenerously; a different reviewer could have corrected the note and still weighed the missed visit heavily; the processor's lag, in another month, might have left no receipts to find, because glove compartments are not archives. Sonya's binder, her copies, her labeled tabs — luck wearing an apron — held pieces of this outcome too. What your choices controlled was the paper: receipts gathered before a Saturday complicated them, a record requested while a draft was soft, an explanation filed instead of spoken, and a reinstatement sought through the very process the letters offered, in their own window. Outcomes in this system turn on clerks, reviewers, processors, and luck as much as on any father's choices. This one also turned on refusing, once, to let a ledger's dates be the only dates in the room.

## [end_note_stands] Ending — No Explanation, Still Standing
*Day 51 — Wednesday, October 7, 2026 — Wednesday, October 7, 2026 (dayOffset 51)*

**Ending.**

**Debrief:**
- WHAT THE FILE HELD (the record, revealed): At the review, the visit note was read as it was written on the Saturday it describes: 'Father missed visit, no explanation.' The explanation — a real letter, a real stated consequence, a real posting lag behind both — was offered aloud, in parts, at speaking speed, against a printed line the room had already read. It was believed in the way spoken explanations are believed in rooms that run on attachments: personally, and without a filing to attach the belief to. The note stands into the next review as the file's account of that Saturday, available to every future summary, and the missed visit will be weighed in Zane's case as what the note calls it: unexplained.
- THE PROCESS UNDER THIS PATH (described, keeping to this scenario's verified law): The instruments that join an explanation to a note are the verified ones, and they were available from the week the note was written: the case record on written request (55 Pa. Code § 3130.44(d)), to quote the note exactly and answer its exact words, and counsel (42 Pa.C.S. § 6337) to file the explanation — letter and receipts attached — where the note lives, before the review convenes. Paper filed before a hearing joins the record; the same truth spoken at a hearing annotates it, at best, in minutes nobody quotes. In the clerk's matter, the same distinction governed: the letters offered their own process, in their own words and windows, and processes, like notes, credit filings, not accounts. Nothing in this ending required anyone's bad faith — only the ordinary physics of whose paper was in which file on the day each room convened.
- THE HONEST PART: Let this debrief be as fair as the note was not: the Saturday was missed for a reason the file's own attachments could have proved in one page — a letter that predated it, stating a consequence no careful father drives against, issued over a lapse that was itself a processor's lag. You weighed a clerk's stated consequence against a six-year-old's Saturday and chose the road not taken, literally, and then the explanation lived where explanations go to be forgotten: in phone calls. A different worker might have asked, that week, why the chair was empty, and written the answer down herself; some do. Yours wrote six words, accurately, from an empty file. The explanation can still be filed now — the letter still predates the Saturday, the receipts still predate the ledger — and the next review can still be given a joined record. It will arrive as a correction, argued, instead of as the record it could simply have been.

## [end_drove] Ending — A Paper Problem, Driven Into a Legal One
*Day 51 — Wednesday, October 7, 2026 — Wednesday, October 7, 2026 (dayOffset 51)*

**Ending.**

**Debrief:**
- WHAT THE FILE HELD (the record, revealed): A kept visit, recorded as kept — and, outside every file until it mattered, a drive taken while a clerk's letter's stated consequence for driving was outstanding. The gamble that nothing would check the status on that ordinary road was, in the short run, won: no stop, no entry, a good visit. In the longer run the drive converted the matter's whole character. A lapsed plan is a column of numbers, answerable with receipts in the letters' own process. A drive taken against a letter's stated consequence is a different kind of fact — one that, if it is ever entered by the hands whose job is entering such facts, re-prices everything else in both files: the receipts become background, the posting lag becomes a detail, and the Saturday becomes the day the father was told, in writing, and drove anyway.
- THE PROCESS UNDER THIS PATH (described, keeping to this scenario's verified law): This ending states no statute about fines, costs, or driving privileges, because none is in the verified set and none is needed to see the shape of it: the letters carried their own process on their faces — a form, an office, deadlines, a stated consequence — and following that process (form and receipts filed inside the stated window) keeps a paper problem paper-sized. Counsel in Zane's case (42 Pa.C.S. § 6337) and the visit record on request (55 Pa. Code § 3130.44(d)) were the instruments for the dependency side of the Saturday, exactly as in every other ending. What changed here was not the law of anything. It was the exposure: a documented, dated warning was answered with a drive instead of a filing, and exposure, unlike a balance, cannot be paid down on a plan.
- THE HONEST PART: Be clear about the choice's human weight, because the file never will be: you drove to a six-year-old who counts his week in Saturdays, on the ordinary road of his whole placement, because the alternative was an empty chair — and parents in this system are handed that exact exchange, letters against Saturdays, more often than any policy admits. The visit itself was good, and Zane's memory of that day is a kept day, not a missed one; no debrief here will call that nothing. But the system you both live in prices papers, not reasons, and it had offered a paper answer — receipts, a form, a window — at the price of one Saturday. This ending is what declining that price can cost when the road, one day, decides to check. Outcomes turn on luck here more nakedly than anywhere else in this series: the same drive, on a luckier road, is a kept visit and a closed file. Luck is not a filing system, and it is not a defense. It is only, on this road, what happened not to happen — this time.
