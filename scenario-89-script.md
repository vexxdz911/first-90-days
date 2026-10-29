# THE FIRST 90 DAYS — Scenario 89: “What the Panel Can See”

*Human-readable script. This document and `scenario-89.json` are generated from a single source and match node-for-node: same IDs, same order, same choices, same effects.*

**The family is fictional — a composite. No real person's story appears here.**

**Content note:** This scenario depicts a Superior Court appeal from a goal-change order — transcripts, briefs, a hearing remembered in flashback. There is no graphic content. Players may skip any scene or use the quick exit at any time.

**How to read effects:** `cash −40` changes the player's cash. `FLAG: name` sets a flag the engine tracks. `HIDDEN + item` means the case file quietly records that item at this choice — the player does not see it when it happens. `REQUIRES FLAG: name` means the choice is only available if that flag was set earlier; `REQUIRES NO FLAG: name` means it is only available if that flag was never set. `NOTE:` is text shown to the player right after choosing.

Start date: Monday, September 14, 2026. Day offsets are days since the scenario's start date.

## [start] The Order That Adopted a Report
*Day 0 — Monday, September 14, 2026 (dayOffset 0)*

Your name is Rosalind Fenn. Your daughter Blythe is nine, a serious child who alphabetizes her bookshelf and her worries in the same spirit. She has been in foster care for eleven months, since the winter your housing and your health unraveled in the same six weeks.

Last Thursday, at the permanency review, the court changed Blythe's goal from reunification to adoption. The written order arrived today. It is two paragraphs long. It says the court 'adopts the findings and recommendations of the agency's court report in full.' It does not say what you complied with, what you alleviated, or what efforts were made — the determinations a permanency hearing exists to make, listed in the statute (42 Pa.C.S. § 6351(f)) as questions the court itself must answer.

Your lawyer, Ms. Park, calls before you finish reading. "I need you to remember the hearing," she says. "Not the outcome. The middle. Because I think I did something in the middle that matters now."

The family is fictional — a composite. The missing findings are a documented shape of real orders.

**Choices:**
- Ask her what she did in the middle of the hearing → **lawyer**
  - NOTE (shown after choosing): "I objected," she says. "Out loud. On the record. Let me show you why that's the whole ballgame."

## [lawyer] Ms. Park and the Findings Page
*Day 2 — Wednesday, September 16, 2026 (dayOffset 2)*

Ms. Park puts the statute's list on her whiteboard: at a permanency hearing the court determines, among other things, compliance with the permanency plan, progress toward alleviating the circumstances that made placement necessary, reasonable efforts to finalize the plan, and — at fifteen of twenty-two months — the termination-filing question and its exceptions (42 Pa.C.S. § 6351(f)(2), (3), (5.1), (9)). "Determinations," she says. "The court's. Not the report's adjectives, adopted by reference."

"When the judge said 'the report is adopted,' I objected and asked the court to make its own findings on the record. The judge declined. That refusal is a ruling, and a ruling is the one thing an appellate panel can truly review. Our whole appeal lives in about ninety seconds of transcript. Which means step one is the same as it always is: get the record — all of it."

**Choices:**
- Ask what has to happen before any arguing happens → **two_lines**
  - NOTE (shown after choosing): She draws two lines on the pad. You have seen this drawing before, in another office, in another winter. It has not stopped being true.

## [two_lines] Two Lines on a Pad
*Day 3 — Thursday, September 17, 2026 (dayOffset 3)*

The top line is the appeal: notice, record, briefs, argument, decision — paper moving at the speed of paper. The notice of appeal is due within thirty days of the order (Pa.R.A.P. 903(a)); it was filed Friday, in time, because Ms. Park does not file things at deadlines.

The bottom line is Blythe's case below, and it does not pause: visits, reviews, services, and the federal fifteen-month clock (42 U.S.C. § 675(5)(E)) all continue while judges read. "We fight on both lines," Ms. Park says, "or the top line wins an argument about a case that no longer exists."

**Choices:**
- Start with the record — order what the appeal will be read from → **boxes**
  - NOTE (shown after choosing): Boxes. It always starts with boxes.

## [boxes] The Record, Boxed
*Day 6 — Sunday, September 20, 2026 (dayOffset 6)*

The certified record arrives: transcripts, the court report, the orders, the exhibits that were actually offered. Ms. Park's checklist offers the usual fork. Ordering the complete transcripts and requesting the agency's full record in writing costs $30 and weeks. Working from the agency's excerpts costs nothing but certainty.

Agency records are released on request (55 Pa. Code § 3130.44(d)). The appeal will be decided by people who read only what is in these boxes. Everything not in them — your memory of the hearing included — is, to the panel, weather.

**Choices:**
- Order the complete transcripts and request the full agency record, in writing → **receipt_drawer** _(cash −30 ; FLAG: recordsRequested ; FLAG: transcriptOrdered ; HIDDEN + Transcripts — complete set ordered; agency record requested in writing)_
  - NOTE (shown after choosing): The receipt goes in the folder. Ninety seconds of transcript are in there somewhere, and now they are findable.
- Work from the excerpts and save the money → **receipt_drawer**
  - NOTE (shown after choosing): Ms. Park circles 'excerpts only' on the checklist, the way you circle a word you are not sure is spelled right.

## [receipt_drawer] The Receipt Drawer
*Day 7 — Monday, September 21, 2026 (dayOffset 7)*

Your kitchen has a drawer that has become, over eleven months, the case's second office: receipts, visit slips, the schedule book, a birthday card Blythe made you in a visit room that you have read roughly four hundred times.

Tonight the transcript receipt joins them. Paper that proves other paper exists. This is not the part of parenting anyone photographs. It is, in this system, load-bearing anyway.

**Choices:**
- Close the drawer and read the transcript when it comes → **flash_hearing**
  - NOTE (shown after choosing): It comes in two envelopes. The hearing is the second one. You make tea first. Everyone in this story makes tea first.

## [flash_hearing] Flashback: 'Let the Record Reflect'
*Day 9 — Wednesday, September 23, 2026 (dayOffset 9)*

READING THE TRANSCRIPT — the permanency review, last Thursday. The agency's counsel finishes. The judge says: 'The court will adopt the findings and recommendations of the court report.'

And then Ms. Park stands. In the transcript it takes four lines: 'Objection, Your Honor. We ask the court to make its own determinations on the record — compliance, progress, efforts — as the statute requires, rather than adopting the report. The report's characterization of my client's compliance is contested, and the underlying logs are in evidence.' The judge: 'The objection is noted. The report is adopted in full.'

Noted. Declined.Ruled on. In the cold print of a transcript, those four lines are a door: a ruling exists, and rulings can be reviewed.

**Choices:**
- In the flashback: that was the moment — the objection was made and ruled on → **flash_ruling** _(FLAG: preservedObjection ; HIDDEN + Transcript — objection to adoption of report without § 6351(f) determinations, made and ruled on at the review)_
  - NOTE (shown after choosing): You read the four lines three times. Ninety seconds, eleven months ago in story-time, last Thursday in real time. The appeal lives there now.
- In the flashback: skim past it — the objection feels like a technicality → **flash_ruling**
  - NOTE (shown after choosing): Technicalities are what appeals are made of. Skimming is how they get lost.

## [flash_ruling] Flashback: What Happened Next
*Day 11 — Friday, September 25, 2026 (dayOffset 11)*

The transcript continues: Ms. Park, still standing, asks that the record reflect her request that the court state its determinations aloud, and that the exhibits she is about to offer be marked. The judge, to his credit, slows down for this part. 'Let the record reflect the request,' he says. 'Counsel may offer her exhibits.'

A small procedural kindness, preserved in print. It means the next thing that happened — the folder — happened inside the record, where a panel can see it.

**Choices:**
- In the flashback: watch what she does with the folder → **flash_progress** _(FLAG: rulingNoted)_
  - NOTE (shown after choosing): The transcript's stage directions are dry. 'Counsel approaches. Documents marked as Respondent's Exhibits 1 through 4.' History, in this format, wears no costume at all.

## [flash_progress] Flashback: The Folder of Saturdays
*Day 13 — Sunday, September 27, 2026 (dayOffset 13)*

Respondent's Exhibits 1 through 4: the visit log with the supervisor's signatures; the treatment attendance record, complete; the housing letter; your employer's schedule letter. The agency's report had called your compliance 'partial.' The exhibits called it documented — a different word, and the difference is the appeal's second pillar: the panel cannot weigh exhibits that were never offered, and these were offered, marked, and admitted.

The judge adopted the report anyway. But he adopted it over an objection, in a record that contains both the adjective and the paper that answers it.

**Choices:**
- In the flashback: offer the folder — every page of it → **issues** _(FLAG: exhibitInRecord ; HIDDEN + Exhibits — visit log, treatment record, housing and schedule letters offered and admitted at the review)_
  - NOTE (shown after choosing): Marked, admitted, numbered. The panel will be able to cite them by page. That is what 'offered' buys.
- In the flashback: hold the folder — the judge has clearly decided → **issues**
  - NOTE (shown after choosing): He had. Which is exactly when paper matters most: decisions get reviewed; folders in laps do not.

## [issues] Choosing the Issues
*Day 18 — Friday, October 2, 2026 (dayOffset 18)*

Ms. Park spreads the draft issue list on the table. It is long, and it is honest, and she crosses out half of it in front of you. "An appeal is not a suggestion box," she says. "We lead with what was preserved: the court changed the goal without making the determinations the statute requires (42 Pa.C.S. § 6351(f)), over objection, in a record whose own exhibits answer the report's adjectives.

"What we do not lead with: that the caseworker dislikes you, that the report was unfair in tone, that the system is rigged. Even the true ones. The panel has no lever for them. It has a lever for a ruling."

**Choices:**
- Build the brief on the preserved findings issue and the exhibits → **statement** _(FLAG: issueChosen ; HIDDEN + Brief — issues limited to the preserved findings objection and the admitted exhibits)_
  - NOTE (shown after choosing): A shorter brief. A heavier one. The crossing-out was the strategy.
- Insist the brief lead with how unfair the report's tone was → **statement**
  - NOTE (shown after choosing): Ms. Park writes it down — in the margin, in pencil, where unreviewable things live.

## [statement] The Statement of Errors
*Day 25 — Friday, October 9, 2026 (dayOffset 25)*

Appellate practice has a gatekeeping paper early on: a concise statement of the errors complained of, filed on the trial court's docket so the judge can write an opinion addressing them. It is due on a short clock, and it defines the appeal's borders — issues not raised in it are, in the ordinary course, not reached later.

Ms. Park drafts it from the transcript's four lines and the exhibit numbers. One page. Three errors, all preserved, all with record citations.

**Choices:**
- File the statement on time, built only from preserved issues → **transcript_gap** _(FLAG: statementFiled ; HIDDEN + Statement of errors — timely, limited to preserved issues with record citations)_
  - NOTE (shown after choosing): One page, filed with days to spare. The appeal's borders are now drawn around its strongest ground.
- File a longer statement adding every grievance from eleven months → **transcript_gap**
  - NOTE (shown after choosing): Every added grievance dilutes the three that a panel can act on. Volume is not a legal strategy; it is a hope wearing one.

## [transcript_gap] The Missing Findings Page
*Day 30 — Wednesday, October 14, 2026 (dayOffset 30)*

The trial judge's opinion arrives, responding to the statement — and it cites a page of the review transcript that is not in your set. Page 41, the findings discussion. Except your transcript jumps from 40 to 42. The court reporter confirms: page 41 exists; your copy is incomplete. Working from excerpts, you would never have known the page existed. With the complete set ordered, the gap is visible — and gaps, unlike memories, can be fixed for $15.

**Choices:**
- Order the missing page and renew the written request for the complete file → **brief_work** _(cash −15 ; FLAG: recordComplete ; HIDDEN + Record — missing transcript page ordered; complete agency file requested in writing)_
  - NOTE (shown after choosing): Page 41 arrives in four days. It helps the other side's framing in one paragraph and yours in two. Both are better than not knowing.
- Argue from the excerpts around the gap → **brief_work**
  - NOTE (shown after choosing): The other side has page 41. Now only one lawyer in the appeal will be surprised by it.

## [brief_work] The Brief, Built From Pages
*Day 40 — Saturday, October 24, 2026 (dayOffset 40)*

Brief-writing, from the client's chair, looks like watching someone build a house out of citations. Every fact sentence ends in a page number. Ms. Park reads the draft aloud once, and twice she stops: "That page says 'partial compliance.' The exhibit says complete attendance. We cite the exhibit and we say so, in those words."

It costs $10 in copies and an evening. Slow, unglamorous, decisive — the story's recurring trilogy.

**Choices:**
- Read the brief line by line against the certified record with her → **waiting_room** _(cash −10 ; FLAG: briefChecked ; HIDDEN + Brief — every citation checked against the certified record)_
  - NOTE (shown after choosing): Two citations were wrong. Now they aren't. This is the least dramatic sentence in the story and one of the most important.
- Trust the draft — she knows what she's doing → **waiting_room**
  - NOTE (shown after choosing): She does. The draft also contains one page citation that belongs to a different hearing. Trust is not a proofreading method.

## [waiting_room] The Waiting Room of the Appeal
*Day 44 — Wednesday, October 28, 2026 (dayOffset 44)*

Appeals have a season where nothing is due and everything is pending, and the case below does not observe it. Blythe's school sends a note home through the visit bag. The foster mother reports a nightmare week, then a better one. Your Saturday swaps accumulate in the schedule book like a second, quieter transcript — the one the bottom line keeps.

**Choices:**
- Keep the bottom line's transcript as carefully as the top line's → **appendix_trap**
  - NOTE (shown after choosing): A folder with two sections now. Both are evidence of the same thing: a mother keeping records in both directions of time.

## [appendix_trap] The Page That Isn't There
*Day 48 — Sunday, November 1, 2026 (dayOffset 48)*

A paralegal assembling the appendix finds it: the housing letter's second page — the paragraph where the landlord confirms the lease renewal — is cited in the brief's draft appendix. But checking it against the certified record shows the letter was admitted as a one-page exhibit; page two was in the folder you handed up, and it was never marked. To a panel, a page outside the certified record does not exist, and a brief that leans on it invites the one ruling nobody wants: disregard, or worse.

Ms. Park is already reaching for the pen.

**Choices:**
- Take the page out of the brief and argue from the admitted page one → **visits_below** _(FLAG: certifiedChecked ; HIDDEN + Brief — appendix-only page removed; argument rests on the certified record)_
  - NOTE (shown after choosing): It hurts to cut your best paragraph. It hurts more to have a panel cut it for you, along with its faith in the other ninety pages.
- Keep the page — it is true, and truth should count → **visits_below** _(FLAG: appendixKept)_
  - NOTE (shown after choosing): It is true. It is also, in the only sense the panel can act on, not there. Truth outside the record is a story; truth inside it is an argument.

## [visits_below] Visits, in the Present Tense
*Day 55 — Sunday, November 8, 2026 (dayOffset 55)*

Saturday. Blythe has a loose tooth and a new system for the bookshelf. The visit supervisor, initialing the log, mentions the make-up visit from the snow week is recorded as a no-show — your folder says it happened, with her predecessor's signature. Small discrepancy, large theme: the bottom line's record is being written weekly, by other people, in pencil.

**Choices:**
- Ask, in writing, for the visit log to be corrected to show the make-up visit → **school_note** _(FLAG: visitLog ; HIDDEN + Visit log — make-up visit correction requested and made in writing)_
  - NOTE (shown after choosing): Corrected while you watch. A good week, on paper, where good weeks count.
- Let it go — it's one visit → **school_note**
  - NOTE (shown after choosing): One visit, in a log, in a case where a judge once adopted adjectives over exhibits. The story has views about letting paper go.

## [school_note] The School Note
*Day 62 — Sunday, November 15, 2026 (dayOffset 62)*

Blythe's teacher sends a note through the proper channel: reading level up two grades since spring; the alphabetized bookshelf is famous in third grade. It belongs in the case below's file, filed before the next review, where progress toward alleviating circumstances is a determination somebody will have to make (42 Pa.C.S. § 6351(f)(3)) — next time, ideally, on the record.

**Choices:**
- File the teacher's note with the case below, with a copy for your folder → **review_below** _(FLAG: schoolFiled)_
  - NOTE (shown after choosing): Filed. The bottom line's file grows a page that no adjective can argue with.

## [review_below] The Review Below
*Day 75 — Saturday, November 28, 2026 (dayOffset 75)*

The interim review is short and strange: the appeal is pending, the goal on paper is adoption, and yet the room still runs on visits and services — because an appeal does not pause the case, and the child in the middle of it does not pause either. The judge asks about school. The agency answers from its report. This time, Ms. Park hands up your written progress summary with the corrected visit log and the teacher's note attached, and asks that it be filed.

**Choices:**
- Hand up the written summary with the log and the note attached → **aunt_call** _(cash −10 ; FLAG: reviewRecord ; HIDDEN + Review record — written progress summary with exhibits filed at interim review)_
  - NOTE (shown after choosing): The clerk stamps it. Below, as above: paper filed is paper that exists.
- Attend and let the agency's report carry the day → **aunt_call**
  - NOTE (shown after choosing): The report carries the day the way it carried the last one: completely, and in adjectives.

## [aunt_call] Your Sister Calls
*Day 85 — Tuesday, December 8, 2026 (dayOffset 85)*

Your sister, who once had Blythe every Thursday, calls to ask the question the whole family asks in rotation: 'If the appeal wins, does she come home?' You give her Ms. Park's answer, because it is the true one: 'If the appeal wins, the order falls and the hearing happens again — correctly this time. Winning the appeal wins the redo. The redo is where home gets decided.'

She is quiet a moment. 'Then we keep Thursdays warm,' she says.

**Choices:**
- Tell her the argument date and keep Thursdays warm → **argument_prep**
  - NOTE (shown after choosing): A support network, kept in the loop with honest math. It is a resource on both lines of the pad.

## [argument_prep] The Night Before Argument
*Day 92 — Tuesday, December 15, 2026 (dayOffset 92)*

Ms. Park moots the argument with two clinic students playing the panel. The hard questions are all about the same ninety seconds: Was the objection specific enough? Did the court rule? What findings, exactly, are missing, and where in the statute's list do they live? Every answer she gives ends in a page number.

You will not speak tomorrow. Your part was finished months ago, in a hearing room, when a folder changed hands and got exhibit numbers. Tomorrow is the reading of it.

**Choices:**
- Sleep, and let the record talk → **argument**
  - NOTE (shown after choosing): The folder stays home. Its contents are already where they need to be: in the record, in the brief, in the page numbers.

## [argument] Argument
*Day 100 — Wednesday, December 23, 2026 (dayOffset 100)*

The panel is three judges and a clock. The agency's counsel argues the report was evidence, the adoption goal was supported, and that any error was harmless given the whole picture. Then Ms. Park rises, and the case comes down to what she leads with.

**Choices:**
- Lead with the preserved findings objection AND the admitted exhibits → **decision_v** _(REQUIRES FLAG: preservedObjection ; REQUIRES FLAG: exhibitInRecord)_
  - NOTE (shown after choosing): Statute's list, objection, ruling, exhibits, page numbers. The panel asks eleven questions. Every answer is a citation.
- Lead with how unfair the report's tone was → **decision_a**
  - NOTE (shown after choosing): A judge asks, gently, where in the record the tone was objected to. The silence that follows is also in the record now.
- Rest on the brief, appendix page included → **decision_q** _(REQUIRES FLAG: appendixKept)_
  - NOTE (shown after choosing): A judge asks for the certified page. There isn't one. The room learns it at the same moment the brief's credibility does.
- Rest on the brief as filed → **decision_a** _(REQUIRES NO FLAG: appendixKept)_
  - NOTE (shown after choosing): The panel reads what it has. What it has, argued this way, is a report and a judge's signature adopting it.

## [decision_v] The Envelope From the Superior Court
*Day 112 — Monday, January 4, 2027 (dayOffset 112)*

The opinion is nineteen pages. The holding is on page two, and Ms. Park reads it to you over the phone, twice, because you ask her to: the order is VACATED. A permanency court must make the determinations the statute lists — the court's own findings, on its own record — and may not substitute the adoption of an agency report for them, over a preserved objection, where the admitted exhibits contradicted the report's central characterization.

The case is remanded for a new permanency hearing. Blythe does not come home today. The goal question will be decided again — this time by a court required to answer the statute's questions out loud, on a record that includes your exhibits.

**Choices:**
- Read the opinion's last page, about what happens next → **end_vacated**
  - NOTE (shown after choosing): 'We keep Thursdays warm,' your sister says, when you call. 'And now the hearing has to show its work.'

## [decision_a] The Envelope From the Superior Court
*Day 112 — Monday, January 4, 2027 (dayOffset 112)*

The opinion is eleven pages, respectful and final: AFFIRMED. Reviewing the record as argued, the panel finds the court report was competent evidence before the court, that the order adopting it is supported by that record, and that the arguments pressed on appeal — fairness, tone, the whole sad picture — do not present a reviewable error of law on the issues as framed.

The goal of adoption stands. The case below moves toward its next filings. Blythe's Thursdays, her bookshelf, her mother's folder — all continue, inside a case whose direction has now been confirmed by two courts.

**Choices:**
- Read the last page and call Ms. Park about what remains → **end_affirmed**
  - NOTE (shown after choosing): What remains is the case below: reviews, progress, and the determinations that will still have to be made — a narrower road, and a real one.

## [decision_q] The Envelope From the Superior Court
*Day 112 — Monday, January 4, 2027 (dayOffset 112)*

The order is three pages, and it is not about Blythe at all. The appeal is QUASHED in relevant part: material in the appellant's appendix and brief was not part of the certified record, contrary to the most basic rule of appellate practice — the panel reviews the record that was made below, and only that record. With the brief's centerpiece disregarded, the remaining issues do not carry the appeal, and the goal-change order stands undisturbed.

Nobody decided the findings question. The argument about the missing determinations — preserved, ruled on, real — was never reached, because the brief arrived carrying a page that did not exist.

**Choices:**
- Read it again, and then put it in the drawer with the receipts → **end_quashed**
  - NOTE (shown after choosing): The receipt drawer. Where this story keeps what paper does when it is handled carelessly, and when it isn't.

## [end_vacated] Ending — Vacated: The Hearing Has to Show Its Work
*Day 120 — Tuesday, January 12, 2027 (dayOffset 120)*

The goal change is undone — not because a panel decided Blythe should come home, but because the decision that changed her goal was made without the findings the law requires, and a lawyer objected at the moment it happened and a mother offered her folder into the record instead of holding it in her lap. The new hearing will be fought on exhibits, logs, and letters, with the statute's questions asked out loud. It could still go either way. It will not go by adjective.

Blythe remains in care while the case is reheard. The fifteen-month date will arrive on its schedule, and the exception packet work continues below. But the appeal did the one thing appeals can do: it made the system redo the decision properly.

**ENDING — Debrief:**

THE WIN, NAMED HONESTLY — A partial win, and the best this scenario offers. Vacated and remanded is not reunification, and this guide does not call it that. What it is: the goal-change order is gone, the redo must make 42 Pa.C.S. § 6351(f)'s determinations on the record, and the admitted exhibits — visit log, attendance record, housing and schedule letters — will be part of the record it is made on.

THE LAW IN THE BEATS — Permanency hearings must determine the matters listed in 42 Pa.C.S. § 6351(f), including (f)(2) compliance with the plan, (f)(3) progress toward alleviating the original circumstances, (f)(5.1) reasonable efforts to finalize the plan, and (f)(9) the fifteen-of-twenty-two-months filing question with its three exceptions; the outcome determinations follow under § 6351(f.1). Before a disposition, § 6351(b) likewise requires findings entered on the record. The appeal's clock was Pa.R.A.P. 903(a)'s thirty days. The record request rests on 55 Pa. Code § 3130.44(d). The panel reviews the certified record — which is why the appendix-only page had to come out of the brief.

THE HIGHEST-LEVERAGE MOVES — The objection in the hearing room (it created the only thing a panel can review: a ruling) and the offered exhibits (they gave the ruling something to bite on). Everything after — the record request, the checked brief, the cut page — was stewardship of those two moments.

WHAT NO STRATEGY CONTROLS — The panel's composition and reading, the trial judge's original haste, the agency's choices on remand. The route controlled preservation, paper, and deadlines. Outcomes also turn on judges and luck; that is stated here because it is true everywhere in this system, including in the endings that feel like victories.


## [end_affirmed] Ending — Affirmed: The Report Stood
*Day 120 — Tuesday, January 12, 2027 (dayOffset 120)*

The goal of adoption stands, confirmed. The case below proceeds toward the filings that follow a goal change, and Rosalind's road narrows to the one that remains in every posture of this system: the reviews below, the determinations still to come, and a record that — because she built it anyway — is stronger than the one the panel declined to disturb.

The appeal was not lost because the findings argument was imaginary. It was lost in the framing: led by grievances a panel has no lever for, the one preserved, ruled-on, reviewable error in the case was argued like a footnote, and panels decide the appeal that is briefed, not the one that might have been.

**ENDING — Debrief:**

WHY THIS ENDING — Appellate courts review preserved errors of law on the record made below. The findings objection existed in this record — made, noted, ruled on — and the exhibits were in it. An appeal that leads elsewhere spends its credibility before it arrives, and harmless-error review forgives much. The law in the winning route (§ 6351(f)'s determinations; § 6351(b)'s on-the-record findings; Pa.R.A.P. 903(a)'s clock; 55 Pa. Code § 3130.44(d)'s record release) was all present in this story. The framing was the failure, and framing is a choice.

WHAT REMAINS TRUE — Affirmance ends the appeal, not the case. Reviews continue at their statutory rhythm (42 Pa.C.S. § 6351(e)(3)(i)), determinations must still be made at each, and the exhibits Rosalind offered are in the record for every one of them. A termination petition, if filed, must still be proved by clear and convincing evidence. Narrower is not nothing.

WHAT NO STRATEGY CONTROLS — The panel, the judge, the report's author. What the player controlled was preservation and presentation. This ending exists to teach the second of those as plainly as the first: an appeal is an argument built for a reader with limited levers, and it must be built out of rulings.


## [end_quashed] Ending — Quashed on a Page That Wasn't There
*Day 118 — Sunday, January 10, 2027 (dayOffset 118)*

The appeal ends without the findings question ever being decided. The goal change stands — not affirmed on its merits, simply never reached, because the brief carried material outside the certified record and the panel stopped there, as panels do.

The bitter arithmetic: the objection was preserved. The exhibits were admitted. Page 41 was ordered. The whole record discipline of the winning route was performed — and then one beloved, true, unadmitted page was left in the appendix, and it spent the appeal.

**ENDING — Debrief:**

WHY THIS ENDING — Appellate review is confined to the certified record. Material outside it is disregarded, and an appeal built on it can be quashed or dismissed in the affected part. This is stated generically in the scenario, as appellate practice's ground rule rather than as a quoted rule — the same discipline the record-request beat teaches from the other side (55 Pa. Code § 3130.44(d) gets the record; nothing gets to add to it afterward).

THE LESSON, EXACTLY — Truth is necessary and not sufficient. Inside the record, a true page is an argument. Outside it, the identical page is a defect. The winning route's least dramatic move — cutting the paragraph — was the one this ending exists to honor.

WHAT NO STRATEGY CONTROLS — Nothing about Blythe, her mother, or their merits appears in this outcome, because the panel never reached them. That is the teaching: procedure is not the enemy of substance in this system. Procedure is the road substance travels on, and the road has rules about what may be loaded onto it.

