# THE FIRST 90 DAYS — Scenario 31: “The Confidential File”

*Human-readable script. This document and `scenario-31.json` are generated from a single source and match node-for-node: same IDs, same order, same choices, same effects.*

**The family is fictional — a composite. No real person's story appears here.**

**Content note:** This scenario depicts a dependency case told through a records dispute — requests, redactions, a discovery motion, and hearings — told through procedure and paperwork. There is no graphic content. A child's removal happens in the opening scene and is handled through procedure, not depiction. Players may skip any scene or use the quick exit at any time.

**How to read effects:** `cash −40` changes the player's cash. `FLAG: name` sets a flag the engine tracks. `HIDDEN + item` means the case file quietly records that item at this choice — the player does not see it when it happens. `NOTE:` is text shown to the player right after choosing.

Start date: Monday, February 2, 2026. Day offsets are days since the scenario's start date.

## [start] The Morning They Came
*Day 0 — Monday, February 2, 2026 — Monday, February 2, 2026 (dayOffset 0)*

You are Dana. You work nights as a home-health aide, and your daughter Wren, eight, is the kind of kid who reads under the blanket with a flashlight. Last week a school nurse asked about a bruise from a playground fall and about the mornings Wren arrived hungry. You answered everything. You thought answering was the end of it.

This morning it was not the end of it. A caseworker and a police officer came before your shift ended, and by nine o'clock Wren was in a car, placed with a foster family across town. Nobody was unkind. Everything was procedure. That is almost the hardest part to explain later: it was all procedure, and it still took your daughter.

**Choices:**
- Ask, before the car leaves, what happens next — and write down every word of the answer → **shelter**  _(FLAG: removed)_
  - NOTE (shown after choosing): A hearing. Within days, not weeks. You write the date on the back of a grocery receipt, because it is the paper you have.
- Stand in the doorway until the car is out of sight, then call your sister → **shelter**  _(FLAG: removed)_
  - NOTE (shown after choosing): She says one word — 'lawyer' — and then stays on the phone while you cry, which is its own kind of help.

## [shelter] Seventy-Two Hours
*Day 3 — Thursday, February 5, 2026 — Thursday, February 5, 2026 (dayOffset 3)*

The law gives the court three days, and the court uses them: Wren was removed on Monday, February 2, and the shelter care hearing is today, Thursday, February 5 — inside the 72 hours the law allows (42 Pa.C.S. § 6332; 23 Pa.C.S. § 6315(d)). The hearing is short. The judge finds the placement should continue for now, and sets the next hearing — the adjudication, where the agency must prove its case — for March.

What changes your life in this room is quieter: the judge appoints you a lawyer, because in these cases a parent who cannot afford counsel gets counsel (42 Pa.C.S. § 6337). Her name is Ms. Hart. In the hallway she says the sentence you will hear in your sleep for a month: 'First, we get the file. All of it. Then we'll know what we're actually answering.'

**Choices:**
- Ask her what 'the file' even is → **counsel**
  - NOTE (shown after choosing): Notes, reports, visit logs, medical pages — and, she says, a scored assessment form you have never seen.
- Ask when Wren can come home → **counsel**
  - NOTE (shown after choosing): 'That answer lives in the file and in the next hearing,' she says. 'Which is why the file comes first.'

## [counsel] Two Doors
*Day 5 — Saturday, February 7, 2026 — Saturday, February 7, 2026 (dayOffset 5)*

Ms. Hart's office has a plant that is winning and a whiteboard that is losing. She draws two doors. Door one is administrative: under the regulation, information in the county agency's case record 'shall be released upon request' to parents (55 Pa. Code § 3130.44(d)) — including, she says, the full scored assessment: the form, the item ratings, the outcome. You watched a worker fill in a form like that at your kitchen table in January. You have never seen what she wrote.

Door two is the court: later, in the adjudication phase, a rule of juvenile court procedure can be used to demand material items from the agency. 'Door one first,' Ms. Hart says. 'It's cheaper, it's faster, and the paper trail it makes is what door two stands on.'

**Choices:**
- Write the first request this week → **request1**
  - NOTE (shown after choosing): One page. Dated. A copy for your folder before the original goes anywhere.

## [request1] The First Request
*Day 6 — Sunday, February 8, 2026 — Sunday, February 8, 2026 (dayOffset 6)*

The request is one page, and Ms. Hart makes you draft it twice. The first draft says 'my whole file, please.' The second names things: the complete case record, and — specifically — the scored assessment completed in January: the form itself, every item rating, and the outcome it produced.

'Specific requests get specific answers,' she says. 'And later, if anyone asks what you asked for, the paper will remember even if people don't.'

**Choices:**
- Send the specific version — certified mail, and keep the receipt → **wait1**  _(cash −6; FLAG: recordsRequested; FLAG: specificRequest; HIDDEN + Request #1 — dated Feb 8; names the assessment form, item ratings, and outcome)_
  - NOTE (shown after choosing): A stamp, a green receipt card, a copy in the folder. The cheapest power in this whole system.
- Send the general version — 'my whole file' should cover it → **wait1**  _(cash −6; FLAG: recordsRequested; HIDDEN + Request #1 — dated Feb 8; asks for 'the whole file' in general terms)_
  - NOTE (shown after choosing): It goes out the same day. It says less. Paper remembers exactly what you teach it to remember.

## [wait1] The Receipt in the Folder
*Day 10 — Thursday, February 12, 2026 — Thursday, February 12, 2026 (dayOffset 10)*

Waiting, in this system, is a job with no pay. You work your night shifts. You visit Wren on Thursdays, supervised, in a room with a two-way mirror and a box of toys slightly too young for her. She asks when she can come home and you say the truest available sentence: 'Grown-ups are working on it, and I am one of them.'

Ms. Hart told you to start a log — one notebook page per ask: what you requested, the date, how it was sent, what came back. It feels like homework for a class you never enrolled in.

**Choices:**
- Start the log tonight — request, date, method, response → **stack**  _(FLAG: logStarted; HIDDEN + Log begun — every ask gets a dated line)_
  - NOTE (shown after choosing): Four columns. It takes four minutes. It will matter more than almost anything else you do this month.
- Skip the log — you'll remember; it's only one file → **stack**
  - NOTE (shown after choosing): You will remember most of it. 'Most' is a word that hearings are unkind to.

## [stack] The Redacted Stack
*Day 16 — Wednesday, February 18, 2026 — Wednesday, February 18, 2026 (dayOffset 16)*

The envelope is thick, which feels like winning until you read it. There are visit notes, the school nurse's report, a summary of the January home visit — and page after page where a black marker has eaten whole paragraphs. Some of that is the law working as written: what is released may not include material that violates another person's privacy or is confidential by law (55 Pa. Code § 3130.44(f)).

But one thing is not redacted. It is absent. The summary refers, twice, to 'the completed assessment (17 items) — see attached.' Nothing is attached. No form. No item ratings. No outcome page. The scored pages you watched being filled in at your kitchen table are simply not in the stack.

**Choices:**
- Build an index: two lists — pages you HAVE, pages the file itself says should exist → **index**  _(FLAG: indexBuilt; HIDDEN + Index — 'see attached' assessment referenced at summary pp. 2 and 5; not in production)_
  - NOTE (shown after choosing): Two columns on notebook paper. The second column is short, and it is the whole case.
- Call the agency and ask about the missing pages by phone → **phone_only**
  - NOTE (shown after choosing): A kind voice, a short call, and — this is the part that matters — nothing written down on their side or yours.
- Accept the stack as the file — it's thick; maybe the assessment is just a summary line → **accept_stack**
  - NOTE (shown after choosing): Thick is a property of envelopes. Complete is a property of records. They are not the same property.

## [index] Two Columns
*Day 19 — Saturday, February 21, 2026 — Saturday, February 21, 2026 (dayOffset 19)*

The index takes one evening and one pot of tea. Left column: 61 pages received, listed by date and type. Right column: what the file's own words say should exist — the assessment form with its 17 item ratings and outcome page ('see attached,' twice), and one home-visit note from January 20 that the summary quotes but the stack doesn't include.

You also count the black bars: eleven pages redacted in part, each with the same short cover note citing privacy and confidentiality. Those, Ms. Hart says, are a stated ground — arguable later. The missing pages are different. You cannot argue about a page nobody admits exists. First, you make them admit it — on paper.

**Choices:**
- Write the second request: name the missing pages exactly, cite the index, keep it logged → **second_request**
  - NOTE (shown after choosing): Not 'the rest of my file.' The assessment form. The item ratings. The outcome page. The January 20 note. Named, dated, numbered.

## [second_request] The Fuller Request
*Day 22 — Tuesday, February 24, 2026 — Tuesday, February 24, 2026 (dayOffset 22)*

The second request is two pages and reads like a receipt read back to a store: on February 8 you asked for the following; on February 18 you received the following; the following named items, referenced in your own summary at pages 2 and 5, were not included. Please produce them, or state the ground for withholding each one.

You send it certified. You log it: date, method, tracking number, one line. Ms. Hart reads the draft and changes exactly one word. 'You are not begging,' she says. 'You are building the record that the asking happened. There's a difference, and the difference is this letter.'

**Choices:**
- Mail it and log it the same day → **partial2**  _(cash −6; FLAG: secondRequest; HIDDEN + Request #2 — Feb 24; names four missing items; certified, logged)_
  - NOTE (shown after choosing): Ask, in writing. Name the pages. Keep the proof. That is the whole technology.

## [partial2] The Partial Second Production
*Day 31 — Thursday, March 5, 2026 — Thursday, March 5, 2026 (dayOffset 31)*

The second envelope is thinner and more honest. It contains the January 20 home-visit note — the one the summary quoted — and a cover letter. The letter says the assessment form and item ratings are 'internal scoring materials' withheld under the confidentiality limits of the regulation, and that the outcome page 'is reflected in the summary already provided.'

Ms. Hart reads the cover letter twice. 'Good,' she says, to your surprise. 'Now the withholding has a stated ground, in writing, with a date on it. That's not the end of the administrative track — it's the beginning of the court track. A judge can review a stated ground. A judge cannot review a shrug.'

**Choices:**
- Ask Ms. Hart to take it to court — start the Rule 1340 track → **court_track**
  - NOTE (shown after choosing): Door two. The paper trail from door one is what you carry through it.
- Write once more to the agency first — one more administrative try → **admin_third**
  - NOTE (shown after choosing): One more letter costs one more stamp and nine more days. Sometimes the record is worth both. Sometimes it isn't.

## [admin_third] One More Letter
*Day 36 — Tuesday, March 10, 2026 — Tuesday, March 10, 2026 (dayOffset 36)*

Your third letter is short: you dispute that a scored form about your own family is 'internal' in any sense that survives the release regulation, and you ask again, by item number, for the form, the ratings, and the outcome page.

The reply is shorter: the agency's position 'is as stated in our letter of March 5,' and 'questions of production for the upcoming hearing may be addressed to the court.' Even a refusal can be a signpost. This one points, in writing, at the courthouse.

**Choices:**
- Take the whole paper trail to Ms. Hart → **court_track**  _(HIDDEN + Agency letter — production questions 'may be addressed to the court')_
  - NOTE (shown after choosing): Three requests, two productions, one stated ground, one signpost. That is a record a judge can hold.

## [court_track] Door Two
*Day 38 — Thursday, March 12, 2026 — Thursday, March 12, 2026 (dayOffset 38)*

Ms. Hart lays out the court track on the whiteboard. Rule 1340 of the Rules of Juvenile Court Procedure is titled 'Discovery and Inspection.' Its mandatory-disclosure part says that in all cases, on request by a party, the county agency shall disclose the requested items that are material to the case, and let the party inspect and copy them (Pa.R.J.C.P. 1340(B)(1)). The rule starts, though, with an informal step: before anyone files a motion, the parties must make a good-faith effort to resolve the discovery question (Rule 1340(A)).

One honest warning before you file anything: Rule 1340 is a real rule with real words, and lawyers use it in dependency cases. But no court has yet decided whether this rule reaches the assessment form — asking is how that gets decided. You would be asking a question the courts have not answered, not reciting one they have.

**Choices:**
- Make the good-faith attempt first — a short written letter to the agency's solicitor → **goodfaith**
  - NOTE (shown after choosing): Unskippable, and not a courtesy. The rule's first paragraph is a door you have to knock on before the court will open the second one.
- File the motion now — the hearing is coming and paper is slow → **motion_rushed**
  - NOTE (shown after choosing): Ms. Hart files it, because you instruct her to. She files it the way lawyers file things they expect to lose the first round of: carefully, and without surprise.

## [goodfaith] The Good-Faith Letter
*Day 41 — Sunday, March 15, 2026 — Sunday, March 15, 2026 (dayOffset 41)*

The letter is five lines: counsel have conferred; the parent has requested the assessment form, item ratings, and outcome page under both the release regulation and Rule 1340; the agency has declined on a stated ground; the parent asks once more, informally, before moving the court. It attaches your log — three dated requests, two partial productions.

The solicitor's reply comes in three days, also in writing: the agency maintains its position. Ms. Hart puts it on top of the motion draft like a cherry. 'Now the motion can say the sentence the rule wants to hear: a good-faith effort was made, and it proved unsuccessful. And nobody has to take your word for any of it. It's all paper, and the paper is all filed.'

**Choices:**
- File the motion to compel — with the log and both requests attached → **motion_filed**  _(FLAG: goodFaithDone; FLAG: rule1340Filed; HIDDEN + Motion to compel filed Mar 18 — log, both requests, and agency letters attached)_
  - NOTE (shown after choosing): Everything you did in February, arriving in March wearing a caption and a docket number.

## [motion_rushed] The Motion, Early
*Day 41 — Sunday, March 15, 2026 — Sunday, March 15, 2026 (dayOffset 41)*

The motion is well written. It is also, in one specific way, naked: it cannot say that a good-faith effort to resolve the question informally was made and failed, because it wasn't — not in writing, not yet. The agency's response makes exactly that point, politely, in its first paragraph, and spends its second paragraph defending the withholding on confidentiality grounds.

Ms. Hart is not angry. 'We gave them the cheapest argument in the rulebook,' she says, 'and skipped the step that makes judges lean toward the asker. We may still win some of it. We will not win the posture.'

**Choices:**
- Go to the motion hearing and argue what's there → **motion_hearing_weak**  _(FLAG: rule1340Filed)_
  - NOTE (shown after choosing): Judges decide the record in front of them. This record has a gap shaped exactly like the step that was skipped.

## [motion_filed] Filed, With Receipts
*Day 44 — Wednesday, March 18, 2026 — Wednesday, March 18, 2026 (dayOffset 44)*

Filing is mostly waiting in a hallway with a time-stamp machine, and it is worth describing because it is the least dramatic and most decisive thing you have done all winter: your copy of the motion — with every request, every receipt, and the agency's own letters attached — goes into the court's own record, stamped, where no one can later misremember whether you asked.

Published cases turn on less. In one Pennsylvania appeal, a mother's Rule 1340 complaint faltered in part because no copy of her discovery request appeared in the certified record at all — the asking could not be proved from the paper. Your asking is the paper.

**Choices:**
- Prepare for the motion hearing: index in one hand, log in the other → **motion_hearing_full**  _(cash −45)_
  - NOTE (shown after choosing): An unpaid morning off work. The hearing is at ten. You are there at nine-fifteen, with the folder.

## [motion_hearing_full] The Motion Hearing
*Day 49 — Monday, March 23, 2026 — Monday, March 23, 2026 (dayOffset 49)*

The judge has read the file — your file, the paper one, the one with the log. The agency's solicitor defends the stated ground honestly: the form is a scoring worksheet; some pages touch another person's private information. Your index answers the first point page by page: you are not asking for anyone's private pages; you are asking for a form about your own family, referenced as 'attached' in a summary you were given.

The judge rules from the bench: the assessment form, the item ratings, and the outcome page are material to the adjudication, and shall be produced within seven days; the genuinely private redactions elsewhere in the stack may stand, with the ground for each stated in writing. 'The parent,' the judge says, 'asked properly, in writing, more than once. The record of asking is not in dispute. Production will follow the asking.'

**Choices:**
- Wait the seven days — and read what comes the way you read the stack: with the index open → **production_full**
  - NOTE (shown after choosing): Seven days. The adjudication is three weeks out. For the first time since February, the clock is on your side of the table.

## [production_full] The Whole File
*Day 55 — Sunday, March 29, 2026 — Sunday, March 29, 2026 (dayOffset 55)*

It arrives on day six: the form itself, seventeen items, each with a rating; the outcome page — a scored level, and the recommendation it fed. And at the back, the home-visit notes in full, including the January 20 note the summary had quoted in one line.

The full note says more than the line did. The summary's version read: 'Mother missed one scheduled visit; engagement inconsistent.' The note itself describes the visit being rescheduled by the agency's own office, twice, and your calls — logged, timed — asking for the new date. The item built on that visit carries a high rating. On the full paper, the rating is a conclusion standing on a sentence that the underlying note does not support. You cannot unscore it yourself. But at the adjudication, your lawyer can put the note and the summary side by side, and let the judge do arithmetic.

**Choices:**
- Spend the weekend with Ms. Hart building the item-by-item page for the adjudication → **adjud_full**  _(FLAG: fullProduction; HIDDEN + Assessment produced in full — form, 17 item ratings, outcome page (Mar 29))_
  - NOTE (shown after choosing): Seventeen items. Most, you leave alone. Two, the paper argues with. That restraint is also an argument.

## [adjud_full] The Adjudication, With the File
*Day 58 — Wednesday, April 1, 2026 — Wednesday, April 1, 2026 (dayOffset 58)*

The adjudication hearing lasts a full morning. The agency proves what it can prove, and some of it stands: the court finds the petition sustained on the housing-instability ground, and Wren remains placed for now, with services and a review date. Nothing about this hearing is a coronation, and nobody in it pretends otherwise.

But two things are different from the hearing you would have had in February. The 'missed visit' claim is withdrawn by the agency's own solicitor when the full note comes out — the item is re-scored on the record, lower, before lunch. And the judge's disposition order directs the agency to build its next review on the corrected file — the whole file, the one that now exists in the court's record because you asked for it properly, three times, on paper.

**Choices:**
- Go to Thursday's visit and tell Wren the truest available sentence → **end_full_intime**
  - NOTE (shown after choosing): 'Grown-ups are still working on it. And now they're working from the real file.'

## [phone_only] The Phone Call
*Day 19 — Saturday, February 21, 2026 — Saturday, February 21, 2026 (dayOffset 19)*

The voice is kind. The answer is short: the assessment is 'an internal tool,' the summary 'reflects it,' and what you received is 'everything releasable.' You thank her. You hang up. And then you sit with the specific emptiness of a conversation that happened entirely in the air: no date stamp, no letter, no line in any log — because you haven't started one — that the question was ever asked.

Ms. Hart, when you tell her, does not scold. 'A phone call is a conversation,' she says. 'A letter is an event. This system runs on events. We can still make some — it'll just be March's work instead of February's, and it will be thinner.'

**Choices:**
- Start now: build the index from the stack and your memory of the summary → **index_late**
  - NOTE (shown after choosing): Later and thinner is not nothing. Later and thinner is most of what second chances are made of.
- Skip the paper — have Ms. Hart take it straight to court → **court_track_weak**
  - NOTE (shown after choosing): 'I can file,' she says. 'Understand what I'd be filing with: your word that you asked, against their word that you got everything.'

## [index_late] The Index, From Memory
*Day 24 — Thursday, February 26, 2026 — Thursday, February 26, 2026 (dayOffset 24)*

You build it the way you can: the stack on the left, your memory on the right. You remember the summary said 'see attached.' You remember seventeen items, because the worker counted them aloud at your table. You do not remember the exact page the reference sat on, and you write that down too — 'page uncertain' — because an index that admits its gaps is worth more than one that bluffs.

It is a good index. It is not the index you would have built in February, and the difference will show up exactly where differences like that always show up: in what can be proved, and when.

**Choices:**
- Write the fuller request now — named items, from the index, and send it → **second_request_late**
  - NOTE (shown after choosing): Late paper is still paper. Send it like you mean it to be read by a judge someday, because it may be.

## [second_request_late] The Request, Late
*Day 27 — Sunday, March 1, 2026 — Sunday, March 1, 2026 (dayOffset 27)*

The request goes out on a Tuesday, ordinary mail, because the certified-mail line at the post office was twenty people deep and your shift started at three. You keep a copy. You do not keep a tracking number, because there isn't one.

Ms. Hart logs what exists: copy, date, your word. 'It's a real request,' she says. 'It's just a request whose birthday we can celebrate but not prove. Hold on to the copy like it's money.'

**Choices:**
- Wait for the reply — and work your shifts, and visit on Thursdays → **partial_late_reply**  _(FLAG: secondRequest; HIDDEN + Request #2 (late) — Mar 1; copy kept, no mailing proof)_
  - NOTE (shown after choosing): Somewhere, an envelope is moving at the speed of offices.

## [partial_late_reply] One Envelope, One Page
*Day 35 — Monday, March 9, 2026 — Monday, March 9, 2026 (dayOffset 35)*

The reply, when it comes, is one envelope: a short letter maintaining the agency's position on the assessment — and, almost as an afterthought, the visit-notes section you named, produced in full 'in the interest of completeness.'

Inside it is a page you have never seen: the agency's own scheduling note for the January visit, recording that the office rescheduled it twice and that you called — timed, logged — asking for the new date. The summary built on that visit says you 'missed' it. The agency's own page says otherwise, in the agency's own hand. The assessment form itself stays withheld. But one page, it turns out, can hold up a whole item.

**Choices:**
- Take the page to Ms. Hart today — not Thursday, today → **court_track_onpage**  _(FLAG: onePageInHand; HIDDEN + Scheduling note produced — agency rescheduled the 'missed' visit twice; mother's calls logged)_
  - NOTE (shown after choosing): One page, in an envelope, with a date on it. You carry it like a plate of water.

## [court_track_onpage] What One Page Can Do
*Day 38 — Thursday, March 12, 2026 — Thursday, March 12, 2026 (dayOffset 38)*

Ms. Hart is realistic about the calendar: a full motion fight over the assessment, started now, will not finish before the adjudication — the good-faith step alone takes a week the calendar doesn't have. 'So we do two things,' she says. 'We file the Rule 1340 request for the form and preserve the fight for the review hearing. And we build the adjudication around the page we have.'

One honest warning before you file anything: Rule 1340 is a real rule with real words, and lawyers use it in dependency cases. But no court has yet decided whether this rule reaches the assessment form — asking is how that gets decided. You would be asking a question the courts have not answered, not reciting one they have.

**Choices:**
- Build the adjudication around the one page — note versus summary, side by side → **adjud_onpage**  _(FLAG: rule1340Filed)_
  - NOTE (shown after choosing): Not the whole file. One page, honestly come by, impossible to un-see.

## [adjud_onpage] The Adjudication, With One Page
*Day 52 — Thursday, March 26, 2026 — Thursday, March 26, 2026 (dayOffset 52)*

The hearing is harder than the one in the other version of March — the version where you built the index in February — because most of the assessment still stands unseen behind its stated ground, and its summary is quoted twice by the agency's solicitor as if it were the thing itself.

Then your lawyer puts up the scheduling note beside the summary's line about the 'missed' visit, and the room does the arithmetic itself. The solicitor, to her credit, withdraws the line. The judge notes, on the record, that one produced page has altered one item's factual basis, and directs the agency to state — at the next review — the basis for each remaining rating or produce the form. The petition is sustained on another ground; Wren stays placed for now. But the item-by-item picture in the court's record is no longer the summary's picture. It has a correction in it, in ink.

**Choices:**
- Log the day in the notebook you finally started: page produced, line withdrawn, direction given → **end_one_page**
  - NOTE (shown after choosing): A thinner win than the whole file. A real one.

## [court_track_weak] Filing on a Handshake
*Day 38 — Thursday, March 12, 2026 — Thursday, March 12, 2026 (dayOffset 38)*

Ms. Hart drafts the motion carefully and files it with what exists: your account of a phone call, and a general first request that never named the assessment at all. There is no log. There are no certified receipts. There is no written good-faith attempt, because the informal step happened — if it happened — in the air.

She shows you the draft before it goes. 'Read the part where I have to describe the request,' she says. The part is one sentence long, and it has the word 'believes' in it. Motions should not need that word. Yours does.

**Choices:**
- Go to the motion hearing with the record there is → **motion_hearing_weak**  _(FLAG: rule1340Filed)_
  - NOTE (shown after choosing): Judges are not unkind about thin records. They are just unable to rule on paper that doesn't exist.

## [motion_hearing_weak] The Motion Hearing, Thin Record
*Day 49 — Monday, March 23, 2026 — Monday, March 23, 2026 (dayOffset 49)*

The judge is fair, and fairness has a sound: it is the sound of a person ruling on exactly what is in front of them. What is in front of them is an agency letter stating a ground — the assessment is withheld under the confidentiality limits of the release regulation, the same limits that let the agency withhold material that is private to another person or confidential by law — and, on your side, a request that cannot be produced, for pages that were never named in writing.

The motion is denied without prejudice, and the agency is granted a protective order covering the assessment pages on the stated ground. 'Without prejudice,' the judge says, looking at you, 'means the door is not locked. It means you will have to knock properly — in writing, by name, with the informal step first — and that takes time this hearing date doesn't have.'

**Choices:**
- Take the ruling, and the lesson, into the adjudication → **adjud_thin**
  - NOTE (shown after choosing): The adjudication will now be fought over a summary of a file you have never seen.

## [adjud_thin] The Adjudication, On a Summary
*Day 53 — Friday, March 27, 2026 — Friday, March 27, 2026 (dayOffset 53)*

The hearing proceeds the way hearings proceed when one side has the document and the other side has a description of it: the summary is quoted; the ratings are characterized; your lawyer objects, preserves, and does what can be done with cross-examination and a scheduling note that was never produced because it was never asked for by name.

The petition is sustained. Wren remains placed, services are ordered, a review is set. Your lawyer's objection — that the parent sought the underlying file and was refused — is in the transcript, and transcripts matter later. But on the day, the case was decided on a thinner record than the one that existed in a drawer at the agency, three miles away.

**Choices:**
- Start the notebook in the car afterward — late, and anyway → **end_withheld**
  - NOTE (shown after choosing): Page one: what you asked for, when, and what came back. The next review is in ninety days. Ninety days is enough — if the asking starts now.

## [accept_stack] Preparing With What's There
*Day 20 — Sunday, February 22, 2026 — Sunday, February 22, 2026 (dayOffset 20)*

You and Ms. Hart prepare with what's there, and some of it is usable: the nurse's report is fairer than you feared, the visit notes are kind about the apartment. But every few pages the summary reaches for its strongest language, and its strongest language reaches back to the assessment — the ratings, the outcome, the scored level — like a hand finding a railing.

'We are preparing to answer a document we cannot see,' Ms. Hart says, 'by reading a summary of it written by the people who wrote it. I've done it before. I'd rather not do it again by choice.'

**Choices:**
- Trust the preparation — go straight to the adjudication → **adjud_thin2**
  - NOTE (shown after choosing): One fight at a time was the plan. The plan has a price, and the price is named in the other room, in a drawer, in a file.
- Change course: file the Rule 1340 motion late, and ask for the file anyway → **motion_late**  _(FLAG: rule1340Filed)_
  - NOTE (shown after choosing): Late paper is still paper. It just arrives on a later calendar.

## [motion_late] The Late Motion
*Day 44 — Wednesday, March 18, 2026 — Wednesday, March 18, 2026 (dayOffset 44)*

Ms. Hart files it cleanly this time — good-faith letter first, a week of silence, then the motion with the request attached. The agency does not seriously fight it; the stated ground, examined by a judge, covers the private pages but not, the judge finds, the scored form about your own family.

There is one problem, and it is not legal. It is calendrical. The judge orders production — in twenty days. The adjudication is in nine. A continuance is requested and denied: Wren's case, the judge says, has already waited on adults long enough. The file will come. It will come after the hearing it was needed for.

**Choices:**
- Go into the adjudication knowing the file is coming — and make the objection that preserves it → **adjud_late**
  - NOTE (shown after choosing): Your lawyer will put the whole history of asking on the transcript, so the late paper lands in a record that's expecting it.

## [adjud_late] The Hearing Before the File
*Day 53 — Friday, March 27, 2026 — Friday, March 27, 2026 (dayOffset 53)*

Your lawyer does the hearing twice at once: the one in the room, argued from the summary, and the one on the transcript, where every ruling is met with a calm, specific objection — the parent requested the underlying assessment on a date, was refused on a ground, moved the court, and production has been ordered but not yet made. The petition is sustained; Wren remains placed; a review is set.

Walking out, Ms. Hart says the thing that is somehow both the worst and best sentence of the spring: 'We lost today's argument with a summary. We have already won the right to never have to do that again.'

**Choices:**
- Wait for the ordered production — and be home when it comes → **late_arrival**
  - NOTE (shown after choosing): Twenty days, the judge said. Offices count days the way rivers count rain.

## [late_arrival] The File, After
*Day 60 — Friday, April 3, 2026 — Friday, April 3, 2026 (dayOffset 60)*

It arrives on a Saturday, complete: the form, seventeen ratings, the outcome page, the full visit notes — including the scheduling note showing the 'missed' visit was rescheduled by the agency's own office, twice, under a summary line that blamed you for missing it.

You read it at the kitchen table with the hearing transcript beside it, and you can see, item by item, exactly which paragraphs of March would have sounded different if April's envelope had come in February. It would not have changed everything. It would have changed the record everything else gets built on — and at the review hearing, now, it will.

**Choices:**
- Take it to Ms. Hart with the transcript, and start the review-hearing folder → **end_late_paper**
  - NOTE (shown after choosing): Folder one: the asking. Folder two: the file. Folder three, empty, labeled with the review date.

## [adjud_thin2] The Adjudication, On a Summary
*Day 53 — Friday, March 27, 2026 — Friday, March 27, 2026 (dayOffset 53)*

It goes the way your lawyer feared in February: the summary is the agency's whole voice — its ratings quoted, its outcome treated as a finding — and your side answers it with testimony, character, and effort, which are real things that weigh less in a room than a scored form nobody has been shown.

The petition is sustained. Wren remains placed. The judge, setting the review date, remarks that the assessment itself was 'referenced but not produced' — a sentence your lawyer writes down word for word, because sentences like that are doors, later, for people who knock in writing.

**Choices:**
- Begin, that night, the written asking you skipped — for the review hearing → **end_withheld**  _(FLAG: recordsRequested)_
  - NOTE (shown after choosing): The review is in ninety days. This time the first request names the form on its first day.

## [end_full_intime] Ending — The File, Whole, in Time
*Day 62 — Sunday, April 5, 2026 — Sunday, April 5, 2026 (dayOffset 62)*

**Ending.**

**Debrief:**
- WHAT THE WITHHELD PAGES HELD (revealed): The assessment pages you fought for contained no secret accusation. They contained something more ordinary and more useful: a scored form whose weakest item — 'engagement,' rated high — rested on a summary line about a 'missed visit' that the agency's own underlying note contradicted: the office had rescheduled the visit twice, and your calls asking for the new date were logged and timed. Most of the other ratings were defensible readings of a hard winter. Two were not. You could not know any of that until the pages existed in your hands, which is the entire point: a summary is a claim about a file, and only the file can grade it.
- THE LAW UNDER THIS PATH: Your administrative requests rested on 55 Pa. Code § 3130.44(d) — information in case records 'shall be released upon request' to parents — and the redactions you accepted rested on its limit, § 3130.44(f): released material may not include what 'violates the right to privacy of another individual or is protected or made confidential by law.' Your court track rested on Pa.R.J.C.P. 1340: the informal good-faith step first (Rule 1340(A)), then mandatory disclosure, on a party's request, of material items (Rule 1340(B)(1)), with remedies including an order for production (Rule 1340(E)). Whether Rule 1340 reaches a scored assessment form at all was — and in the real world remains — undecided; in 2026 a Pennsylvania Superior Court memorandum called substantive interpretation of Rule 1340 an issue of first impression, and faulted a parent's discovery complaint in part because no copy of her request appeared in the certified record. Your request was the record. That is why this hearing could be about evidence instead of about whether you ever asked.
- THE HONEST PART: Wren did not come home at the adjudication, and this scenario does not pretend the file was a key that opened her foster family's door. What the file changed was the basis on which the case continues: a withdrawn claim, a re-scored item, a court's order building the next review on the corrected record. A different judge could have read the confidentiality ground more broadly; a slower mailroom could have eaten the seven days; the production order came from a record of asking that took you five weeks of stamps and notebooks to build, and building it was never guaranteed to be enough. Workers, judges, grounds, and luck all held pieces of this. What your choices controlled was narrower and real: whether the case would be decided from the file, or from a summary of it.

## [end_one_page] Ending — One Page
*Day 58 — Wednesday, April 1, 2026 — Wednesday, April 1, 2026 (dayOffset 58)*

**Ending.**

**Debrief:**
- WHAT THE WITHHELD PAGES HELD (revealed): You saw one of them, and it was the load-bearing one: the agency's own scheduling note, showing the 'missed' January visit was rescheduled twice by the agency's office and that you called, on logged dates, asking when it would happen. The pages you never saw — the form, the other sixteen ratings, the outcome page — stayed behind the agency's stated confidentiality ground, and this debrief will not invent their contents, because neither could the court: that is what 'withheld' means, and it is why the judge's direction for the next review matters. What can be said is what the one page proved about the summary's method: at least one of its sentences was stronger than the paper underneath it.
- THE LAW UNDER THIS PATH: The page reached you through the same door as everything else in this scenario — a parent's request for her own case record under 55 Pa. Code § 3130.44(d), made specific by naming the item — and your lawyer's Rule 1340 filing preserved the fight over the rest for the review hearing, with its untested reach toward the assessment form stated plainly rather than papered over. The lesson the published cases keep teaching is procedural, not dramatic: requests that exist on paper can be ruled on; requests that happened in the air mostly cannot. Your late index and unprovable mailing are why this ending is one page instead of seventeen items — the difference between the two endings in this scenario is not effort or worth. It is dates, receipts, and names of pages.
- THE HONEST PART: One page changed one item, in a case that continues. The petition was still sustained on another ground; Wren is still placed; the form still sits in a drawer with a stated ground on top of it. It would be easy to call this ending small, and wrong: the court's record now contains a correction in ink and a direction to the agency about the next review, and both exist because a page was asked for by name. Whether they grow into the whole file depends on the next ninety days of asking — and, as always, on which worker answers, which judge reads, and how the luck of calendars falls.

## [end_late_paper] Ending — The Paper Win, After
*Day 64 — Tuesday, April 7, 2026 — Tuesday, April 7, 2026 (dayOffset 64)*

**Ending.**

**Debrief:**
- WHAT THE WITHHELD PAGES HELD (revealed): Everything the early track would have shown in February, shown in April instead: the form, the seventeen ratings, the outcome page — and the scheduling note proving that the summary's 'missed visit' line described a visit the agency's own office had rescheduled twice. Reading it beside the hearing transcript is the specific ache of this ending: you can watch, paragraph by paragraph, a hearing that was argued against a summary, when the document that answered the summary was already written, already filed, already sitting in the agency's drawer. The law eventually agreed it was yours. The calendar did not care what the law agreed.
- THE LAW UNDER THIS PATH: Nothing in this ending failed legally — that is its sting. The release right (55 Pa. Code § 3130.44(d)), the confidentiality limit (§ 3130.44(f)), the good-faith step and mandatory disclosure of Rule 1340(A) and (B)(1), and the court's production remedy (Rule 1340(E)) all worked, in order, as written. What failed was sequencing: every one of those mechanisms runs on requests, responses, and motion practice measured in weeks, and they were started after the adjudication clock was already running. Deadlines in this system are not punishments for bad character; they are simply the medium the rights travel in. A right exercised late is not a fake right. It is a right that arrives at a later hearing — and the review hearing, where this file will now be the record, is a real hearing too.
- THE HONEST PART: It is tempting to score this ending as a loss with good paperwork, and tempting, too, to score it as a win that merely posted late. It is both, and it is neither's fault but the calendar's: the same letters, sent in the first week instead of the sixth, are the other ending. Workers' response times, a judge's continuance call, and the luck of hearing dates all held pieces of the outcome. What your choices controlled — eventually, completely — was whether the file would exist in the court's record at all. It does now. Cases are long. Records are longer. The review will be argued from the file, and that sentence was not true in March.

## [end_withheld] Ending — The Stated Ground Stands
*Day 59 — Thursday, April 2, 2026 — Thursday, April 2, 2026 (dayOffset 59)*

**Ending.**

**Debrief:**
- WHAT THE WITHHELD PAGES HELD (revealed): Honestly: you never saw them, and neither did the court, and this debrief is not going to pretend otherwise — inventing their contents here would repeat, in miniature, the exact harm of the summary, which was a confident description of pages nobody deciding anything had read. What is known is structural. A scored form exists: seventeen items, ratings, an outcome page. A summary of it was quoted at your hearing as if it were the thing itself. One of its source notes — the scheduling record for the January visit — exists too, and was never requested by name. Whether the form is fair or slanted, careful or rushed, is a question this ending leaves exactly where the system left it: unexamined, behind a stated ground, carrying weight.
- THE LAW UNDER THIS PATH: The withholding was not lawless; that is what makes this ending worth studying. The agency stated a ground rooted in the release regulation's own limit — material may be withheld where release would violate another person's privacy or disclose what is 'protected or made confidential by law' (55 Pa. Code § 3130.44(f)) — and Rule 1340 gives a court power to protect material on a sufficient showing (Rule 1340(F)). Against a stated ground, the counterweight is a record: a specific, dated, provable request, a good-faith informal attempt, a motion with the asking attached. Where that record was thin or absent, the ground stood — not because the ground was unanswerable, but because answering it is a paper procedure and the paper wasn't there. The judge's 'without prejudice' was the truest sentence in this ending: the door was never locked. It was knocked on in a way the court could not hear.
- THE HONEST PART: Parents reach this ending for reasons that have nothing to do with merit — night shifts, phone trees, fear of antagonizing the people who visit their child, the reasonable belief that a thick envelope must be the whole envelope. The system in this ending did not act through villains; it acted through procedure, defaults, and the quiet arithmetic of who had paper and who had summaries. Workers, judges, workloads, and luck all held pieces of it. The review hearing is in ninety days, and the first request — the specific one, naming the form, the ratings, the outcome page — can be in the mail this week. That is not a consolation. It is a calendar, and calendars, unlike summaries, can be answered.
