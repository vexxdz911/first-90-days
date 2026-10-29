# THE FIRST 90 DAYS — Scenario 108: “The Renewal That Went to the Daycare”

*Human-readable script. This document and `scenario-108.json` are generated from a single source and match node-for-node: same IDs, same order, same choices, same effects.*

**The family is fictional — a composite. No real person's story appears here.**

**Content note:** This scenario depicts an in-home case under court supervision: a childcare renewal form mailed to the daycare instead of to the mother, a lapsed arrangement, two missed Tuesday parenting classes, progress notes, and a review hearing, told through forms, letters, and sign-in sheets. There is no graphic content. Players may skip any scene or use the quick exit at any time.

**How to read effects:** `cash −40` changes the player's cash. `FLAG: name` sets a flag the engine tracks. `HIDDEN + item` means the case file quietly records that item at this choice — the player does not see it when it happens. `REQUIRES FLAG: name` means the choice is only available if that flag was set earlier; `REQUIRES NO FLAG: name` means it is only available if that flag was never set. `NOTE:` is text shown to the player right after choosing.

Start date: Monday, June 1, 2026. Day offsets are days since the scenario's start date. Tier: Foundation.

## [start] The Form With Her Name On It
*Day 0 — Monday, June 1, 2026 — Monday, June 1, 2026 (dayOffset 0)*

Your name is Kendra. Your son Cato is two, and he is home with you — this is an in-home case, under court supervision, and the plan's centrepiece, on Tuesdays, is a parenting class across town.

The class does not admit toddlers — that is the class's own rule, printed on its sheet — so Tuesdays only work because Cato's childcare arrangement covers them. The same arrangement covers your work shifts. One arrangement, holding up both a job and a plan, the way one rope can hold two things and be cut once.

The call comes on the morning of Monday, June 1, 2026, from Cato's daycare, and it is not about Cato. “We got a form with your name on it,” the voice says. “It came in our mail. It looks important, and it has a date on it that already passed.”

**Choices:**
- Collect the form from the daycare tonight, and take Cato to drop-off in the morning as usual → **dropoff_lapse**
  - NOTE (shown after choosing): Tonight you will read the form at your kitchen table. Its face is plain about itself. What it cannot tell you is what its weeks in the wrong mail tray have already done.

## [dropoff_lapse] Turned Away at Drop-Off
*Day 1 — Tuesday, June 2, 2026 — Tuesday, June 2, 2026 (dayOffset 1)*

The form's face is plain about itself, the way forms are: sign, date, and return it to the address printed at the top, by Friday, May 29, 2026. It was mailed to the daycare instead of to you, it sat in the daycare's mail, and its printed date passed there. You sign it at the kitchen table on Monday, June 1, 2026 — after the date on its face, through no door of yours.

At drop-off on Tuesday, June 2, 2026 — a Tuesday, class day — the lapse is discovered in the most ordinary way there is: at the desk, with Cato's bag on your shoulder. The arrangement has lapsed, the desk tells you, gently and finally; until the renewal is back in place, Cato cannot stay under it. You carry him back out into a Tuesday that has just lost its childcare and its class at the same desk, in the same minute.

You miss the class. It is the first missed session in your file, and the file will record it in the file's grammar: missed. Not “the form went to the daycare.” Missed.

**Choices:**
- Call the childcare office from outside the daycare, with the signed form in your bag → **office_answers**  _(HIDDEN + Parenting class — session missed on the lapse day; the renewal form had been mailed to the daycare)_
  - NOTE (shown after choosing): Calling from the pavement, with a toddler on your hip and a signed form three days past its printed date, is not how anyone plans to fix a filing. It is how filings get fixed.

## [office_answers] It Went to the Daycare
*Day 3 — Thursday, June 4, 2026 — Thursday, June 4, 2026 (dayOffset 3)*

Two days of menus and holds later, on Thursday, June 4, 2026, a person at the childcare office can see the whole small disaster on her screen: the renewal form was mailed out, no return was received, and the arrangement lapsed. Where it was mailed to takes her a second screen to find. The daycare. It was mailed to the daycare.

To restart it, she says, the signed form has to reach the office — the form itself says so, on its face, with the address printed at the top. She can note your call on the account. A note, in her words, in her system, is what a call becomes.

Tonight the renewal can travel the way your account of it has travelled so far — spoken, noted by someone else — or it can travel filed, with a dated statement, copies kept, and its receipt confirmed in writing.

**Choices:**
- File the renewal with a dated written statement of the facts, keep copies of everything, and ask the office to confirm receipt in writing → **written_filing**  _(cash −5; FLAG: renewalFiled; HIDDEN + Renewal — filed with a dated written statement; copies kept; written confirmation of receipt requested)_
  - NOTE (shown after choosing): Five dollars of fares and copies across the errand. The statement is short: form mailed to the daycare; found there after its printed date; lapse discovered at drop-off; class missed. Every line dated.
- Post the form in the ordinary envelope and let the office's note of your call carry the explanation → **phone_only**
  - NOTE (shown after choosing): The form will arrive either way. What will not arrive with it is any account, in your words with your dates, of why it is late.

## [written_filing] Filed, With Copies
*Day 5 — Saturday, June 6, 2026 — Saturday, June 6, 2026 (dayOffset 5)*

By Saturday, June 6, 2026 the packet is filed: the signed renewal, your dated statement, and your request that receipt be confirmed in writing. Copies of all of it are in your folder, because copies are the difference between filed and merely sent.

The office's reply, when it comes, confirms receipt, and its letter states its own next steps on its face; you follow them the way you follow any letter — as this letter's instructions, for this case. The arrangement is not back yet. Tuesdays, meanwhile, keep arriving on schedule, indifferent to processing.

**Choices:**
- Keep the confirmation with the statement, and face the next Tuesday → **second_tuesday**  _(HIDDEN + Office reply — renewal receipt confirmed in writing)_
  - NOTE (shown after choosing): Receipt is not restoration. But for the first time in this story, a piece of the gap exists in the office's own writing, with your dates attached to it.

## [phone_only] Posted, and Noted
*Day 5 — Saturday, June 6, 2026 — Saturday, June 6, 2026 (dayOffset 5)*

The form goes in the ordinary post, alone: no statement with it, no copy in your folder, nothing in your handwriting anywhere in its envelope. Somewhere in the office's system there is a note of your call, in the call-taker's summary of your words, at the length call notes are kept.

If the lateness of this renewal is ever argued about in a room, the argument will be that note and your memory against the file's tally of missed sessions. You have been in this case long enough to know which of those three things rooms believe.

**Choices:**
- Face the next Tuesday, and keep the daycare's number close → **second_tuesday**
  - NOTE (shown after choosing): The form is travelling. So is the tally. They are travelling toward the same review, and only one of them is counting.

## [second_tuesday] The Second Tuesday
*Day 8 — Tuesday, June 9, 2026 — Tuesday, June 9, 2026 (dayOffset 8)*

Tuesday, June 9, 2026 is the second Tuesday. The arrangement is still lapsed — the renewal, however it travelled, has not landed yet — and at drop-off the desk, apologetic and immovable, turns Cato away again. You miss the second class, standing in the same entryway, holding the same bag.

In the file, the tally has now begun, in the file's own arithmetic: missed sessions, two. The tally counts sessions. It does not count causes, mail trays, or desks. A scored assessment form is part of cases like yours — filled in from notes like these, rating what it can see. What it can see this month is two empty Tuesdays.

The daycare knows the exact shape of the gap — they watched it happen at their desk, twice, and the form that caused it arrived in their own mail. Their knowledge can become paper, or it can stay a memory at a desk that sees a hundred families.

**Choices:**
- Ask the daycare in writing to confirm exactly which dates the lapse covered → **provider_written**  _(FLAG: lapseConfirmed; HIDDEN + Daycare — asked in writing to confirm the exact dates the lapse covered)_
  - NOTE (shown after choosing): Dates, not impressions: which Tuesdays, what happened at the desk, and where the form arrived. Asked in writing, so the answer comes back in writing.
- Ask at the desk and take their word for the dates — they were there, they know → **provider_verbal**
  - NOTE (shown after choosing): They were, and they do. Knowledge at a desk is real knowledge. It is just not the kind that can be attached to a review packet.

## [provider_written] The Dates, in Writing
*Day 11 — Friday, June 12, 2026 — Friday, June 12, 2026 (dayOffset 11)*

The daycare's reply arrives by Friday, June 12, 2026, and it is short in the way strong documents are short. In writing, the daycare confirms that the arrangement's lapse covered exactly two class Tuesdays — Tuesday, June 2, 2026 and Tuesday, June 9, 2026 — that Cato was turned away at drop-off on both, and that the renewal form had arrived in the daycare's own mail.

Your folder now holds a document authored by neither side of the argument the file is having with you: the desk that watched the lapse, dating it. It agrees with your statement about everything, because it is not agreeing with you — it is describing its own entryway.

**Choices:**
- Keep the daycare's letter with the office confirmation, in date order → **flyer_beat**  _(HIDDEN + Daycare letter — lapse dates and the form's arrival in the daycare's mail confirmed in writing)_
  - NOTE (shown after choosing): Two letters now, from two desks, neither of them yours, describing the same two Tuesdays. The tally in the file describes them too — in one word.

## [provider_verbal] The Dates, Out Loud
*Day 11 — Friday, June 12, 2026 — Friday, June 12, 2026 (dayOffset 11)*

The desk is happy to confirm it all out loud, and does, completely and accurately: the two Tuesdays, the turn-aways, the form in their mail tray. It is a full and truthful account, delivered in the entryway, to you, while Cato pulls at the door handle.

Nothing is written down. Next month the desk will have new staff, or the same staff on a harder day, and the account will be a memory of a conversation in an entryway — true, warm, and impossible to attach to anything.

**Choices:**
- Thank them, and go on with the month → **flyer_beat**
  - NOTE (shown after choosing): Being believed at a desk feels like the problem being solved. Desks do not attend reviews. Paper does.

## [flyer_beat] The Flyer in the Folder
*Day 14 — Monday, June 15, 2026 — Monday, June 15, 2026 (dayOffset 14)*

In the waiting room at the agency office there is a folder of flyers for parents, and one of them — the kind of paper most people walk past — says something you read twice: a parent may request their case record, and under 55 Pa. Code § 3130.44(d) the material “shall be released upon request.”

Your record. The class sign-in sheets, the progress notes, the tally in its original handwriting — the file's own version of your Tuesdays, which you have never seen. The flyer is not offering you a rescue. It is offering you the other side of the tally.

**Choices:**
- Take the flyer home and think about what the sign-in sheet would show → **records_fork**
  - NOTE (shown after choosing): You signed that sheet every Tuesday you were in the room. If it is in the record, the record knows exactly which Tuesdays you were not — and signatures have a way of raising the question of why.

## [records_fork] Ask for the File, or Don’t
*Day 16 — Wednesday, June 17, 2026 — Wednesday, June 17, 2026 (dayOffset 16)*

The request is simple and it is yours to make: ask, in writing, for your case record — the parenting class sign-in sheets and the progress notes about attendance. Under 55 Pa. Code § 3130.44(d), the record is to be released on request; the asking is a right, not a favor, and it leaves a date behind.

Or you can wait for the review and explain the mail tray there, out loud, to people reading a tally you have never seen.

**Choices:**
- Put the request in writing — sign-in sheets and attendance notes — and keep a copy → **packet_arrives**  _(cash −3; FLAG: recordsRequested)_
  - NOTE (shown after choosing): Three dollars of copies and postage across the errand. The request is dated, copied, and kept with the letters.
- Wait for the review — you can explain the daycare's mail in person → **no_packet**
  - NOTE (shown after choosing): In person is how the desk confirmed the dates: accurately, warmly, and in a form that cannot be handed to anyone.

## [packet_arrives] The Sign-In Sheet
*Day 21 — Monday, June 22, 2026 — Monday, June 22, 2026 (dayOffset 21)*

The packet arrives, and two of its documents belong side by side, so you put them side by side. The first is the class sign-in sheet: your signature, in your hand, on every Tuesday the class met — except Tuesday, June 2, 2026 and Tuesday, June 9, 2026, where your line is simply, eloquently, blank.

The second is the progress note, and its whole account of the same month is a tally: “missed sessions: 2.” No cause is recorded beside it — not the form, not the mail tray, not the desk. The system's own sheet proves which Tuesdays you missed and that you missed no others. The note, beside it, is what the review will quote.

Now you have seen both documents the review will weigh. The question is what paper will be sitting between them.

**Choices:**
- Keep the packet with the daycare's letter and the office confirmation, in date order → **tally_note**  _(HIDDEN + Class sign-in sheet — attendance on every class Tuesday except the two lapse Tuesdays, shown in the record)_
  - NOTE (shown after choosing): Signatures, a tally, and a daycare's letter, all describing the same two blank lines — in three different grammars. Only one of the grammars mentions a cause.

## [no_packet] What You Cannot Quote
*Day 21 — Monday, June 22, 2026 — Monday, June 22, 2026 (dayOffset 21)*

Without the packet, you cannot see the tally's exact wording, and you cannot show anyone the sign-in sheet's eloquent blanks — every Tuesday signed except two. You know what the sheet would show. You know it in the way that cannot be attached to a report.

Your account is true, detailed, and sincere. At the review, it will be weighed the way spoken accounts are weighed in rooms that run on attachments: personally, politely, and against a printed tally that says less and therefore somehow says it louder.

**Choices:**
- Go on toward the review with your account — and keep every letter you do have → **tally_note**
  - NOTE (shown after choosing): Whatever paper exists still exists. The review is weeks away, and weeks are where tallies harden.

## [tally_note] Missed Sessions
*Day 28 — Monday, June 29, 2026 — Monday, June 29, 2026 (dayOffset 28)*

By Monday, June 29, 2026 the arrangement is back in place — the renewal landed, on its own schedule — and on Tuesday, June 30, 2026 Cato stays at the daycare under it while you sit in the class and sign the sheet, in the row below the two blank lines.

The tally, though, survives the fix. At the month's check-in you hear it read the way the file holds it: missed sessions, two — a compliance fact now, travelling without its cause toward a review that will read it exactly as written.

Whether it arrives at that review still travelling alone depends on what gets assembled before the review sits.

**Choices:**
- Ask when the review is, and how much time is left to prepare for it → **prep**
  - NOTE (shown after choosing): Days, not weeks. Preparation, in this system, is mostly deciding what paper will be in the room.

## [prep] One Page, or a Story
*Day 31 — Thursday, July 2, 2026 — Thursday, July 2, 2026 (dayOffset 31)*

Your folder holds the whole gap, if you wrote it down: the dated statement, the office's confirmation, the daycare's letter with its two exact Tuesdays, and — if you requested it — the sign-in sheet with its two blank lines. Assembled in order, they fit on one page: the form's printed date passed in the daycare's mail; the form found; the lapse at drop-off; the renewal filed; the second Tuesday lost; the lapse confirmed in writing by the desk that watched it; the sheet signed again the week the arrangement returned.

Or the gap can stay where it has partly lived so far — in your head, in order, in a story you can tell well. Stories are true. Pages are portable. Reviews are rooms you speak in for minutes and files speak in forever.

**Choices:**
- Build the one-page timeline from the statement, the letters, and the sign-in sheet, in date order → **timeline_built**  _(FLAG: timelineBuilt; HIDDEN + Timeline — one-page dated timeline built from the statement, the daycare letter, and the sign-in sheet)_
  - NOTE (shown after choosing): One page. Every line dated. Nothing on it that the system's own paper does not support.
- Go in with the story in your head — you lived it, in order → **story_only**
  - NOTE (shown after choosing): You did, and you can tell it. The tally in the file can also be told — by the file, to every reader, whether you are in the room or not.

## [timeline_built] The Timeline, Assembled
*Day 33 — Saturday, July 4, 2026 — Saturday, July 4, 2026 (dayOffset 33)*

The page reads like a timetable, because it is one. The renewal form's printed return date, Friday, May 29, 2026 — passed while the form sat in the daycare's mail. The form found, Monday, June 1, 2026. The lapse at drop-off and the first missed class, Tuesday, June 2, 2026. The renewal filed with its statement, Saturday, June 6, 2026. The second missed class, Tuesday, June 9, 2026. The daycare's written confirmation, Friday, June 12, 2026. The sign-in sheet, obtained Monday, June 22, 2026, blank on exactly those two Tuesdays and signed on every other.

Seven lines, no adjectives. Your lawyer's word for a page like this is “quiet.” Quiet pages get read carefully, because there is nothing in them to argue with except their dates.

**Choices:**
- Make copies — one for the review, one for your lawyer, one for the folder → **review_eve**
  - NOTE (shown after choosing): Copies are how a page attends meetings you are not invited to. This one is about to attend the most important one.

## [story_only] The Story, Unwritten
*Day 33 — Saturday, July 4, 2026 — Saturday, July 4, 2026 (dayOffset 33)*

Your account is clear, in order, and true: the phone call, the form in the wrong mail, the desk, the bag on your shoulder, the second Tuesday in the same entryway. Sitting at the kitchen table you can tell it start to finish without a pause. It has only one flaw, and the flaw is not in the telling.

It exists in exactly one place, and that place cannot be handed to a reviewer, attached to a report, or read after you leave the room. The file's version — “missed sessions: 2” — exists everywhere the file goes.

**Choices:**
- Practice telling it once more, and get Cato settled for the morning → **review_eve**
  - NOTE (shown after choosing): The review will be short. Short rooms reward paper and punish nothing — they simply cannot hold what was never handed to them.

## [review_eve] The Night Before the Review
*Day 35 — Monday, July 6, 2026 — Monday, July 6, 2026 (dayOffset 35)*

The night before the review, your lawyer goes through your folder with you. You have one because the law provides for counsel in these cases, and for appointed counsel if a parent cannot afford one (42 Pa.C.S. § 6337) — she is the person whose job is to stand in the review room and make the paper speak in the right order.

“Reviews measure the plan against the record,” she says. “Tomorrow we find out which record yours is measured against — the tally's two words, or the tally plus everything that explains it.”

Cato is asleep. The folder is by the door. The bus fare for the morning is in your coat.

**Choices:**
- Take the folder and the fare, and go to the review → **review**  _(cash −6)_
  - NOTE (shown after choosing): Six dollars of fare. Tomorrow is a Tuesday — class day — and for once the folder, not the toddler, is what you have to get across town.

## [review] The Review
*Day 36 — Tuesday, July 7, 2026 — Tuesday, July 7, 2026 (dayOffset 36)*

The review sits on Tuesday, July 7, 2026 — a Tuesday, with Cato covered at the daycare under the restored arrangement, in the class's own hours. The plan is read line by line. On the attendance line, the progress note is quoted — “missed sessions: 2” — and the room begins, in the ordinary way, to treat the two Tuesdays as a fact about you.

Then your lawyer asks that the record be completed before the line is weighed. What happens next depends, with a precision this scenario has been honest about from its first phone call, on what your choices actually put in her hands.

**Choices:**
- Present the one-page timeline — the dated statement, the daycare's written confirmation, and the sign-in sheet attached → **end_win**  _(REQUIRES FLAG: renewalFiled; REQUIRES FLAG: lapseConfirmed; REQUIRES FLAG: recordsRequested; REQUIRES FLAG: timelineBuilt)_
  - NOTE (shown after choosing): Seven dated lines, three of them written by the system's own desks. The room does the arithmetic itself, out loud, which is where arithmetic changes a record.
- Present what paper you have — some of it, without the full set → **end_lose**
  - NOTE (shown after choosing): Part of a timeline is an argument with missing premises. The tally, whole and printed, is sitting across the table.
- Tell the two Tuesdays as a story — the call, the form, the desk → **end_lose**
  - NOTE (shown after choosing): Your voice is truthful and detailed. The file's voice is two words long and has already been read.

## [end_win] Ending — Attributed, On the Record
*Day 39 — Friday, July 10, 2026 — Friday, July 10, 2026 (dayOffset 39)*

**Ending.**

**Debrief:**
- WHAT THE FILE HELD (the hidden record, revealed): A dated account of the gap, authored largely by the system's own desks: your statement filed with the renewal, the childcare office's written confirmation of receipt, the daycare's written confirmation that the lapse covered exactly Tuesday, June 2, 2026 and Tuesday, June 9, 2026 and that the renewal form had arrived in the daycare's own mail, and the class sign-in sheet — signed every Tuesday except those two. At the review on Tuesday, July 7, 2026, the one-page timeline was put beside the tally, and the room attributed the two missed sessions on the record to the paperwork gap: the tally was corrected to carry its cause, the renewal stands filed, and the class was extended by two sessions so the missed ones can be made up. The assessment form rates what it can see; after this review, what it can see includes a form that went to the wrong address.
- THE PROCESS UNDER THIS PATH (described, keeping to this scenario's verified law): The one legal instrument was the verified one. The case record was yours on written request — it “shall be released upon request” (55 Pa. Code § 3130.44(d)) — and requesting it is what let you show the sign-in sheet's two blank lines instead of arguing against a summary of them. Counsel (42 Pa.C.S. § 6337) presented the timeline in the room where the plan is measured against the record. Everything else was generic process, deliberately without citation, and no program rule is stated anywhere in this ending, because none was needed: the renewal form and the office's letters stated their own instructions on their faces, and the story turned on where the form was mailed, what the desks confirmed in writing, and what the sheet showed. Reviews can only weigh paper that exists in time to be weighed.
- THE HONEST PART: Label this win honestly — it is partial. The two sessions are made up ahead of you, not behind you: the class continues, now two sessions longer, with all the ordinary difficulty of Tuesdays. The case is still open, Cato is home as he has been throughout, and the supervision continues. The two lost Tuesdays themselves — the entryway, the bag, the walk back out — are not returned by any correction. A different reviewer might have noted the timeline and kept the tally's wording anyway, and a daycare that had thrown the form away would have left you with nothing to confirm. Workers, desks, reviewers, and luck all held pieces of this. Your share was narrower and durable: when the system's form went to the wrong building, you made the system's own desks sign for where it went.

## [end_lose] Ending — Missed, As Tallied
*Day 39 — Friday, July 10, 2026 — Friday, July 10, 2026 (dayOffset 39)*

**Ending.**

**Debrief:**
- WHAT THE FILE HELD (the hidden record, revealed): Two words and a number. The progress note's tally — “missed sessions: 2” — with nothing in the record explaining the two Tuesdays behind it: no dated statement filed with the renewal, no daycare letter fixing the lapse's dates, no sign-in sheet quoted against the note. At the review, your account was heard and, in the way of spoken accounts, believed personally and set aside professionally. The renewal is in place now and Tuesdays are covered again. The tally stays in the file as written — two unexplained misses, available to every future reader, in a case where the renewal form spent its deadline in a daycare's mail tray.
- THE PROCESS UNDER THIS PATH (described, keeping to this scenario's verified law): The tools existed at every step and are modest ones. File the renewal with a dated written statement, so the filing carries its own explanation; ask the provider, in writing, to confirm exactly which dates the lapse covered, so the gap's shape is fixed by the desk that watched it; request the record, which “shall be released upon request” (55 Pa. Code § 3130.44(d)), so the sign-in sheet's blanks can be shown rather than described; and let counsel (42 Pa.C.S. § 6337) carry the assembled page into the room. No program rule needed stating for any of that: the form and the letters carried their own instructions on their faces. What was missing was never permission. It was paper.
- THE HONEST PART: Let this debrief be as fair as the review was not: you did the human part of this correctly and promptly. You collected the form the day the daycare found it, signed it that night, and stood at the desk on both Tuesdays ready to comply with a plan whose paperwork had gone to another building. What was lost was not effort — it was evidence, and the two are different currencies in a file. A different provider might have written the mailing failure into the note itself; some do. This file did not, and outcomes here turn on workers, desks, and luck as much as on parents. The tally in the file is not a verdict on you as a mother. It is a verdict on what was documented — and a folder started tonight, with the next letter, still changes what the next review reads.
