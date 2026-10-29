# THE FIRST 90 DAYS — Scenario 74: “Goal: Changed?”

*Human-readable script. This document and `scenario-74.json` are generated from a single source and match node-for-node: same IDs, same order, same choices, same effects.*

**The family is fictional — a composite. No real person's story appears here.**

**Content note:** This scenario depicts a permanency hearing at which the agency asks the court to change a child's goal from reunification to adoption. There is no graphic content. Players may skip any scene or use the quick exit at any time.

**How to read effects:** `cash −40` changes the player's cash. `FLAG: name` sets a flag the engine tracks. `HIDDEN + item` means the case file quietly records that item at this choice — the player does not see it when it happens. `REQUIRES FLAG: name` means the choice is only available if that flag was set earlier; `REQUIRES NO FLAG: name` means it is only available if that flag was never set. `NOTE:` is text shown to the player right after choosing.

Start date: Tuesday, December 8, 2026. Day offsets are days since the scenario's start date.

## [start] The Filing in the Mail
*Day 0 — Tuesday, December 8, 2026 (dayOffset 0)*

Your name is Josephine Haas — Josie to everyone who has ever actually met you. Your son Quinn is four. He has been living in foster care since February 9, 2026, after an adjudication that followed a relapse you do not waste breath denying anymore. That was ten months ago. The woman in that paperwork has been, piece by piece, replaced.

Today's mail holds the agency's newest filing. It asks the court, at the permanency hearing on Thursday, December 17, to change Quinn's permanency goal from reunification to adoption.

Your hands do the thing they used to do in March. Then you put the kettle on, sit down, and read the whole filing twice — because the first thing your lawyer taught you is that a filing is a list of claims, and claims can be answered.

**Choices:**
- Call your lawyer before you call anyone else → **filing_terms**
  - NOTE (shown after choosing): "Read me the caption and the last page," she says. "Then breathe."
- Read it a third time, alone, until the words stop swimming → **filing_terms**
  - NOTE (shown after choosing): By the third pass, one sentence stands out: the agency is asking. Asking is not getting.

## [filing_terms] What a Goal Change Is — and Is Not
*Day 0 — Tuesday, December 8, 2026 (dayOffset 0)*

Your lawyer, Ms. Adler, explains it plainly, the way she explains everything: a permanency goal is what the plan aims at. Right now the plan aims at Quinn coming home, and every service, visit, and review is organized around that aim. The agency wants the court to change the aim itself.

"Here is what it is not," she says. "It is not a termination of your rights. Nobody's rights end at a goal-change hearing — termination, if it ever comes, is its own case, and the agency would have to prove it by clear and convincing evidence. Here is what it is: when the goal changes, the energy changes with it. Services aimed at return wind down. Visits stop being rehearsals for home. Everyone in the system starts working toward a different ending."

"So we don't argue about whether you love him," she says. "We argue about what the evidence shows. That fight, we can prepare for."

**Choices:**
- Ask what the judge actually has to decide on December 17 → **counsel_map**
  - NOTE (shown after choosing): "Now you're asking the hearing's real question."
- Ask whether eight months of doing everything counts for anything → **counsel_map**
  - NOTE (shown after choosing): "It counts if the court can see it. Seeing it is our job for the next nine days."

## [counsel_map] Two Questions, in the Law's Order
*Day 0 — Tuesday, December 8, 2026 (dayOffset 0)*

Ms. Adler draws the hearing the way the statute builds it. This is a permanency hearing — held within six months of removal and within six months of each previous permanency hearing (42 Pa.C.S. § 6351(e)(3)(i)) — and at each one the court must determine specific things: the continuing necessity of placement; compliance with the permanency plan; progress toward alleviating the circumstances that caused placement; and whether reasonable efforts were made to finalize the plan. (§ 6351(f)(1), (2), (3), (5.1))

"Only after those determinations — based upon the determinations made under subsection (f) and all relevant evidence — does the court choose the outcome." (§ 6351(f.1)) The outcomes on the menu are: return to parent; adoption, with the agency to file for termination; a legal custodian; a fit and willing relative; or another planned permanent living arrangement. (§ 6351(f.1))

"Sequence is the law's, not the agency's," she says. "Determinations first. Outcome second. If we win the first part honestly, the second part is a much shorter argument."

**Choices:**
- Start where she starts: with the agency's own file → **record_request**
  - NOTE (shown after choosing): "Nine days. The file first, then your proof, then the people. In that order."
- Ask if the hearing can be postponed to buy preparation time → **record_request**
  - NOTE (shown after choosing): "It almost certainly can't, and asking spends goodwill we'll need. Nine days is enough — if we spend them on paper."

## [record_request] Hinge A: The Written Request
*Day 2 — Thursday, December 10, 2026 (dayOffset 2)*

Ms. Adler wants the agency's complete record — not the summary the caseworker reads from, the file itself: notes, referrals, the scored summary, all of it. The regulation is one sentence long and she makes you say it back to her: the record "shall be released upon request." (55 Pa. Code § 3130.44(d)) And it is not to be read to protect agency employees' privacy as a basis for withholding. (§ 3130.44(f))

"You have asked for pieces of this file before, on the phone, and been told pieces were coming," she says. "Phone requests live where hallway promises live. This one goes in writing, dated, with a copy kept — so that on December 17 there is a request in the world that can be pointed to."

**Choices:**
- Sign the written request for the complete agency record, through counsel, today → **request_receipt**  _(FLAG: recordsRequested ; HIDDEN + File — agency record on written request (§ 3130.44(d)): housing referral drafted March 4, sent May 27)_
  - NOTE (shown after choosing): One page. It will take days to be filled — and what it surfaces on day 6 will matter more than anything said in the hallway.
- Ask the caseworker by phone to just send the important parts → **request_receipt**
  - NOTE (shown after choosing): She says she'll "get the highlights together." Highlights chosen by the other side have a way of highlighting the other side.

## [request_receipt] A Copy, a Receipt, a Date
*Day 2 — Thursday, December 10, 2026 (dayOffset 2)*

The request goes out with a copy for your folder — the folder that now lives on your kitchen counter the way other people's Bibles used to, consulted daily and carried everywhere. Ms. Adler dates her copy, stamps yours, and writes the hearing date across the top of both in red pen.

"Whatever arrives, arrives against a deadline," she says. "And whatever doesn't arrive, we'll be able to say exactly when we asked. In this system, the asking is half the evidence."

**Choices:**
- File the stamped copy at the front of the folder, where the hearing exhibits will go → **gal_call**
  - NOTE (shown after choosing): Front of the folder. Where, nine days from now, a judge's clerk will be able to find it in seconds.
- Put it in the folder's back pocket — the folder is getting crowded → **gal_call**
  - NOTE (shown after choosing): Crowded is what a worked case looks like. Back pockets are where good paper goes to be forgotten, though.

## [gal_call] The Guardian ad Litem's Voice
*Day 2 — Thursday, December 10, 2026 (dayOffset 2)*

Quinn has his own lawyer in this — the guardian ad litem, Mr. Osei — whose job is Quinn's interests, not yours and not the agency's. Ms. Adler calls him with you on the line, because a fact learned secondhand arrives bent.

He is measured, the way he always is, and then he is not: he has watched Quinn run to you at every visit for months; he has read the aftercare reports; he is not prepared to tell a court that this case should stop aiming at home. "If the record at the hearing is what you describe," he says, "I will support more time — and I will say so on the record."

"On the record" is the only dialect this building fully trusts. You write his words in the folder, with the date, while he is still saying them.

**Choices:**
- Ask him exactly what he wants to see in the packet before he commits to a schedule → **aunt_first**  _(FLAG: galSupport)_
  - NOTE (shown after choosing): "Dates," he says. "Give me a return that happens on dates, and I can defend it. Give me 'soon' and I can't."
- Thank him and take the support as settled → **aunt_first**
  - NOTE (shown after choosing): Support is real, and it is also conditional in the way of all courtroom things: on the record he is shown.

## [aunt_first] Ohio, on the Phone
*Day 2 — Thursday, December 10, 2026 (dayOffset 2)*

Your sister Lori lives in Ohio, four hours and one state line away, and she has spent the autumn doing something the agency's filing does not mention: a full home study, completed, approved, filed in her county — she is cleared to take Quinn if a court ever asks her to.

On the phone she is blunt in the family way. "I am not trying to take your son, Josie. I am trying to make sure nobody can stand up in that courtroom and say adoption by strangers is the only permanence on the table. Because it isn't. I'm on the table."

She is right about the law's menu, too: alongside return to a parent and adoption, the court may choose a fit and willing relative. (§ 6351(f.1)) Her study doesn't replace your case. It removes the agency's favorite sentence — "there is no other option" — from the room.

**Choices:**
- Ask her to keep December 17 completely clear, in case counsel needs her live → **evidence_shelf**
  - NOTE (shown after choosing): "Cleared since October," she says. "Tell your lawyer I'm a phone call, not a hope."
- Ask her to write it all in a letter instead — live testimony feels like a lot to ask → **evidence_shelf**
  - NOTE (shown after choosing): A letter is something. A voice that can answer the judge's questions is something else. The choice comes back on day 4.

## [evidence_shelf] The Shelf of Proof
*Day 2 — Thursday, December 10, 2026 (dayOffset 2)*

That evening you lay eight months on the kitchen table, literally. Treatment completion certificate, framed by nobody, creased by your folder. Aftercare attendance records. Screen results — every one negative since spring, a small stack of unglamorous miracles. The visit log. The lease, signed in June, and five months of rent receipts paper-clipped behind it.

It is a lot of proof, and it is shaped like a pile. Ms. Adler's voice in your head is unkind and accurate: a pile persuades nobody. Judges read exhibits — numbered, indexed, findable in the thirty seconds a fact is being argued about.

The difference between your eight months and the agency's version of your eight months is, in large part, stationery.

**Choices:**
- Spend day 4 turning the pile into a packet — numbered exhibits, one-page index → **exhibits_build**
  - NOTE (shown after choosing): Stationery, yes. Also the whole ballgame.
- Trust that the caseworker's report already tells this story → **exhibits_build**
  - NOTE (shown after choosing): Her report tells a story. You have read her summaries before. It is not this one.

## [exhibits_build] Hinge B: A Packet With an Index
*Day 4 — Saturday, December 12, 2026 (dayOffset 4)*

Saturday is for the unglamorous sacrament: the copy shop, the three-hole punch, the tabs. Ms. Adler's paralegal loans you the template — Exhibit 1, treatment; Exhibit 2, aftercare; Exhibit 3, screens; Exhibit 4, visits; Exhibit 5, housing — and a one-page index that says, in plain lines, what each exhibit proves and which determination it answers.

Copies for the court, the agency, the GAL, and you. The register tape says twenty dollars. It is the best-funded argument you own.

**Choices:**
- Build the full packet — five exhibits, one-page index, four copies → **treatment_records**  _(cash −20 ; FLAG: exhibitsReady ; HIDDEN + Exhibit — progress packet with index: treatment, aftercare, screens, visits, lease)_
  - NOTE (shown after choosing): When a fact is argued on December 17, this is the difference between 'it's in there somewhere' and 'Exhibit 3, Your Honor.'
- Bring the originals in the folder and let counsel sort it out at the hearing → **treatment_records**
  - NOTE (shown after choosing): Originals in a lap are not exhibits. You have heard this sentence before, in other parents' stories. It is still true in yours.

## [treatment_records] Aftercare, in Writing
*Day 4 — Saturday, December 12, 2026 (dayOffset 4)*

The treatment program's counselor, Ms. Tran, answers on a Saturday, which tells you something about her. Yes, she will put it in writing: program completed in July; aftercare attended weekly since; relapse-prevention plan in place and, as far as her records show, lived.

"Everyone in your hearing will say the word 'progress,'" Ms. Adler says, reading the letter when it arrives. "This letter is what progress looks like when it's a document instead of an adjective. It answers the (f)(3) question — progress toward alleviating the circumstances that caused placement — in a professional's own hand."

**Choices:**
- Ask Ms. Tran to include the aftercare dates, not just the completion date → **screens_history**  _(FLAG: providerLetter)_
  - NOTE (shown after choosing): Dates are the difference between a claim and a chronology. She adds them without being asked twice.
- Take the letter as it stands — it says completed, and completed is the point → **screens_history**
  - NOTE (shown after choosing): It does say that. It just doesn't yet say the eight quiet months after it, which are the actual argument.

## [screens_history] Eight Months of Screens
*Day 4 — Saturday, December 12, 2026 (dayOffset 4)*

The screen history, printed out, is a column of dates and a column of one repeated word. Negative. Negative. Negative. Random screens, scheduled screens, screens after visits and screens after holidays — the spring relapse that started this case has not repeated, and the column is the proof in its least poetic form.

Ms. Adler slides it into Exhibit 3 without ceremony. "The agency's filing says 'history of relapse' eleven times," she says. "This exhibit says the history has a second half."

**Choices:**
- Have the lab print the complete history, including the random screens → **visit_log_node**
  - NOTE (shown after choosing): Random screens are the ones nobody can accuse you of scheduling around. They go in front.
- Use the summary page the program already sent → **visit_log_node**
  - NOTE (shown after choosing): The summary is accurate and thinner — it omits the spring randoms, which happen to be the strongest pages.

## [visit_log_node] Never Missed
*Day 4 — Saturday, December 12, 2026 (dayOffset 4)*

The visit log is the exhibit you did not have to build, only to obtain: every scheduled visit since March, and in the attendance column, a perfect record — through the bus strike in October, through the week Quinn had an ear infection and the visit moved to the agency's quiet room, through your double shift in November.

Quinn's foster mother, initialling the log each week, has been writing your (f)(2) compliance evidence all year without either of you calling it that. Compliance with the permanency plan is one of the determinations the court must make (§ 6351(f)(2)) — and here it is, initialled, dated, boring, perfect.

**Choices:**
- Get a clean copy of the full log for Exhibit 4, initialled pages included → **housing_lease**
  - NOTE (shown after choosing): The initialled pages are the exhibit. A summary of them would be a rumor about an exhibit.
- Note the perfect record in the index and rely on the agency's copy → **housing_lease**
  - NOTE (shown after choosing): The agency's copy exists. Whether it is the copy the judge's packet opens to is another question, and not yours to control.

## [housing_lease] The Lease and the Quiet Months
*Day 4 — Saturday, December 12, 2026 (dayOffset 4)*

Housing is where filings go to sound reasonable. The agency's filing says you were "without stable housing into the summer" — true, in the way a photograph of March is true of December. You signed the lease in June. Six months of receipts say the apartment has been yours, paid, quiet, and ready since.

What the filing does not say — what you do not yet know, because it is sitting in the agency's own file waiting for your written request to surface it — is why the spring housing search took as long as it did. That answer arrives on day 6, in the agency's own handwriting.

For now, the lease goes into Exhibit 5 with the receipts behind it, and the index line writes itself: housing stable since June.

**Choices:**
- Add the rent receipts and the June lease together, so the stability has a start date → **aunt_prep**
  - NOTE (shown after choosing): A start date turns 'stable now' into 'stable for six months' — a different sentence in a judge's mouth.
- Include the lease alone — the receipts feel like overkill → **aunt_prep**
  - NOTE (shown after choosing): In this building there is no overkill. There is only proof and the absence of it, wearing similar clothes.

## [aunt_prep] Hinge C: Will She Testify?
*Day 4 — Saturday, December 12, 2026 (dayOffset 4)*

Ms. Adler is direct: Lori's completed home study is already a document, and documents are good. But at the hearing, the agency will argue that adoption is the only permanence available — and a document cannot answer a judge's follow-up question. A person can. Lori can testify by phone or video; courts do this routinely, and her study would be handed up while she speaks.

"Her being live reframes the whole (f.1) menu," Ms. Adler says. "It's no longer mother-or-adoption. It's mother, with a studied, approved relative standing behind the return — and that same relative as an option herself if the court wants one. The agency's 'only option' argument dies either way."

**Choices:**
- Ask Lori to testify live by video, home study in hand → **records_reveal**  _(FLAG: kinTestifies)_
  - NOTE (shown after choosing): "Four hours is a long drive to be a letter," Lori says. "Set up the camera."
- File her home study and letter, and spare her the witness chair → **records_reveal**
  - NOTE (shown after choosing): The study will be in the packet either way. What won't be there is a voice, answering, when the judge leans forward.

## [records_reveal] The Record Arrives
*Day 6 — Monday, December 14, 2026 (dayOffset 6)*

The agency's record arrives Monday, in response to the written request — thick, partly blacked out at the edges, and entirely worth the asking. Ms. Adler reads it the way she reads everything: with a ruler, a highlighter, and no expression at all.

Then she stops. She turns back four pages. She turns forward again. "Josie," she says, in the tone of a woman laying down a winning card she intends to play politely, "tell me about the housing referral."

"What housing referral?" you say. "Exactly," she says.

**Choices:**
- Read the referral pages with her, line by line, dates first → **referral_timeline**
  - NOTE (shown after choosing): Dates first. In this file, dates are the whole story.
- Ask her to summarize — the file's handwriting makes your eyes ache → **referral_timeline**
  - NOTE (shown after choosing): She summarizes. But she makes you look at the two dates yourself before she puts the ruler down.

## [referral_timeline] Eleven Weeks, in Two Dates
*Day 6 — Monday, December 14, 2026 (dayOffset 6)*

The dates are these: the agency's housing referral — the referral your plan required, to the program that eventually found your apartment — was drafted on March 4. It was sent on May 27. Eleven weeks in a drawer, or an outbox, or wherever unsent referrals go, while your file recorded you as 'not yet housed' and your plan clock ran.

Your June lease, in other words, is not evidence that you were slow. Part of the delay was the agency's own — and that is not gossip, it is reasonable-efforts material: at the hearing the court must determine whether reasonable efforts were made to finalize the permanency plan. (§ 6351(f)(5.1))

"We don't wave this like a flag," Ms. Adler says. "We lay it down like a date. March 4. May 27. The court can do its own arithmetic."

**Choices:**
- Build a one-page timeline — drafted, sent, lease signed — and put it behind the index → **casa_choice**  _(FLAG: referralDated)_
  - NOTE (shown after choosing): One page, three dates, no adjectives. It is the most dangerous page in the packet precisely because it has no adjectives.
- Raise it orally at the hearing and let the judge ask for the file → **casa_choice**
  - NOTE (shown after choosing): Oral arithmetic fades by lunch. A timeline in the packet is still true, and still findable, at 4 p.m.

## [casa_choice] Hinge D: The Stale Report
*Day 6 — Monday, December 14, 2026 (dayOffset 6)*

The other document in the judge's packet is the CASA report — the court-appointed advocate's summary, warm in tone and five months old. It describes a woman in early, fragile recovery: missed appointments, unstable housing, 'limited insight.' It describes July's Josie, faithfully. It will be read on Thursday as if it describes December's.

Ms. Adler is calm about the fix and firm about the method. "We do not attack a volunteer. We correct a document. A short written correction, filed through counsel before the hearing — two pages, dates, proof attached — so the judge reads the correction alongside the report, not instead of hearing about it for the first time mid-testimony. Objecting cold in the room makes it a fight. Filing makes it a record."

**Choices:**
- File the short written correction through counsel before the hearing, proof attached → **summary_rebuttal**  _(FLAG: casaCorrected ; HIDDEN + Filing — written correction to the CASA report, filed before the hearing)_
  - NOTE (shown after choosing): Two pages, dated, courteous, and impossible to un-read. The judge's packet now corrects itself.
- Save it for the hearing — object when the report is mentioned, in the moment → **summary_rebuttal**
  - NOTE (shown after choosing): In the moment is where corrections go to sound like arguments. The report, meanwhile, will have sat in the packet, uncorrected, for days.

## [summary_rebuttal] One Line in the Scored Summary
*Day 6 — Monday, December 14, 2026 (dayOffset 6)*

There is a second stale line, smaller and colder. The scored assessment summary in the file still carries a provision from the spring: "housing: unstable." It was a true line in April. It rides into December's hearing stapled to the agency's paperwork as if nothing since had happened — no lease, no receipts, no June.

Ms. Adler drafts a short rebuttal to file alongside the CASA correction, citing the rule that lets a party present evidence and argument to rebut a provision, and challenge factual errors. (Pa.R.J.C.P. 1340(E), (F)) Then she says the sentence she says about this rule every single time, because it is true every single time: whether Rule 1340 reaches a scored assessment summary has NOT been tested in a published opinion — it is an argument counsel makes, not a settled right.

"We file it as an argument, labeled as an argument," she says. "The lease is the proof. The rule is the door we knock on."

**Choices:**
- File the rebuttal with the lease attached, Rule 1340 flagged as untested in the filing itself → **clock_answer**  _(FLAG: summaryRebutted)_
  - NOTE (shown after choosing): Honest paper: the proof is certain, the rule is an argument, and the filing says which is which.
- Leave the summary line alone — the lease exhibit already answers it → **clock_answer**
  - NOTE (shown after choosing): The lease does answer it — in your packet. The summary line sits in theirs, unanswered in the place it was written.

## [clock_answer] Answering a Clock That Has Not Struck
*Day 6 — Monday, December 14, 2026 (dayOffset 6)*

Ms. Adler rehearses the agency's best argument before they can make it, because it is coming: Quinn has been in care ten months. In five more, he reaches fifteen of the most recent twenty-two months — and the agency will stand up and call that a deadline with your name on it.

"Here is the honest law," she says. "The fifteen-of-twenty-two determination is not today's question. At fifteen months, the court determines whether the agency has filed or joined a termination petition — unless the child is cared for by a relative, or the agency has documented a compelling reason filing would not serve the child, or the family was not provided the services necessary for safe return within the plan's time frames. (§ 6351(f)(9)) At month ten, that determination has not been triggered. Nobody gets to borrow May's clock to win December's hearing."

"And the services clause matters in embryo," she adds. "A referral that sat unsent for eleven weeks is the plan's own time frame, testified against itself. We don't hide from the clock. We date it, and we answer it."

**Choices:**
- Prepare the answer: the (f)(9) determination is not triggered at month ten — and the plan's time frames cut both ways → **packet_sent**  _(FLAG: clockAnswered)_
  - NOTE (shown after choosing): Named, dated, answered. A clock that has been answered out loud loses most of its power to frighten a courtroom.
- Hope the judge doesn't raise the timeline if counsel doesn't → **packet_sent**
  - NOTE (shown after choosing): Judges raise timelines. It is, in a real sense, the job description. An unanswered clock is the loudest thing in the room.

## [packet_sent] Paper, Filed Before the Hearing
*Day 6 — Monday, December 14, 2026 (dayOffset 6)*

By Monday evening the machinery is in motion: the progress packet ready to hand up, the CASA correction filed, the summary rebuttal filed with it, the referral timeline behind the index, Lori's testimony arranged, the GAL's support spoken aloud and written down in your folder with its date.

Copies go to the GAL's office so Mr. Osei reads your version before Thursday, not during it. Postage and printing come out of the envelope in your purse marked, in your own hand, COURT.

**Choices:**
- Send the GAL a courtesy copy of the full packet today, and keep the mailing receipt → **stepped_draft**  _(cash −10 ; FLAG: packetShared)_
  - NOTE (shown after choosing): An ally who has read the packet is a different witness from an ally who is handed it in the hallway.
- Let the hearing itself be the GAL's first full look → **stepped_draft**
  - NOTE (shown after choosing): First looks in courtrooms happen at courtroom speed. Mr. Osei's support was promised against a record — this choice makes him find it live.

## [stepped_draft] The Ask, With Dates
*Day 8 — Wednesday, December 16, 2026 (dayOffset 8)*

The night before the hearing is for the most important drafting in the case, and it is not a speech. It is the ask. Ms. Adler spreads two versions on the table. Version one says: give Josie more time. Version two says something else entirely.

"Quinn's life is not on hold while we deliberate — the agency will say that sentence, and it is a true sentence," she says. "So our answer cannot be 'more open-ended time.' Our answer is a stepped return, with dates: unsupervised day visits in January, overnights by February, full return by the spring review, services and screens continuing through every step. That is (f.1)(1) — return to parent — drawn as a schedule instead of a hope. It gives the judge something to sign. 'More time' gives the judge something to refuse."

**Choices:**
- Draft the ask as a stepped return with dates — overnights by February, full return by the spring review → **findings_language**  _(FLAG: steppedAsk)_
  - NOTE (shown after choosing): A schedule is an argument a judge can grant. It also answers the clock: this plan finishes before May ever arrives.
- Ask for more time under the current goal, and trust the progress to speak for itself → **findings_language**
  - NOTE (shown after choosing): Progress does not speak. Exhibits speak, witnesses speak, and asks get granted or refused. 'More time' is the ask this hearing was built to refuse.

## [findings_language] Findings Language
*Day 8 — Wednesday, December 16, 2026 (dayOffset 8)*

Ms. Adler drafts the closing the way she drew the hearing on day 0: determinations first, outcome second, in the statute's own sequence. Substantial compliance with the plan — § 6351(f)(2) — and the visit log, the aftercare record, and the screens are its exhibits. The circumstances that caused placement, alleviated — § 6351(f)(3) — treatment completed, relapse unrepeated for eight months, housing stable since June.

And then the honest sentence, laid down like a date: on reasonable efforts to finalize the plan — § 6351(f)(5.1) — the record shows a mother who did her parts on time, and a housing referral that sat unsent for eleven weeks of the plan's own spring. "We ask the court to find the efforts were not all reasonable," Ms. Adler says, "and then to choose the outcome the determinations point to: (f.1)(1), return, on the stepped schedule. Findings first. Outcome second. That order is not our preference. It is the law's."

**Choices:**
- Rehearse the closing in that order until the sequence is automatic → **aunt_logistics**
  - NOTE (shown after choosing): Determinations, then outcome. By the third rehearsal you could recite it in your sleep, which is roughly the plan.
- Ask her to lead with the fairness of it — eight months of work should open the argument → **aunt_logistics**
  - NOTE (shown after choosing): "Fairness is the closing's heart," she says, "but the statute is its skeleton. Hearts without skeletons don't stand up in court."

## [aunt_logistics] Testing the Link
*Day 8 — Wednesday, December 16, 2026 (dayOffset 8)*

Wednesday evening is logistics, the unglamorous load-bearing wall of every hearing: the video link tested twice, Lori's home study scanned and in the packet, her phone charged, her testimony outlined in four plain points — who she is, what the study found, that she supports Quinn going home to his mother, and that she stands ready herself if the court ever wants a fit and willing relative instead.

"She is not your backup plan," Ms. Adler says, watching the test call connect. "In the law's language she is a permanency option — (f.1)(4) — and her existing is what makes 'adoption or nothing' untrue. Those are different jobs and she does both by simply showing up."

**Choices:**
- Run the full test — link, study, four points — and end the night early → **rehearsal**
  - NOTE (shown after choosing): Everything that can be rehearsed has been. What remains is sleep, which is also preparation.
- Keep polishing the packet past midnight — there is always one more page → **rehearsal**
  - NOTE (shown after choosing): There is always one more page. There is only one of you, and she has a hearing at nine.

## [rehearsal] What Is Different This Time?
*Day 8 — Wednesday, December 16, 2026 (dayOffset 8)*

Last rehearsal. Ms. Adler takes the judge's chair — a kitchen chair, turned around — and asks the question she guarantees is coming, in the plainest voice she owns: "Ms. Haas. There was a relapse before. What is different this time?"

It is the question the whole case hides inside. A promise answers it badly; the year has heard promises. A record answers it well: treatment completed, aftercare kept, a column of negative screens, visits never missed, a lease six months old — each one a page the judge can be handed while you say it.

"Don't tell the court you're different," Ms. Adler says, turning the chair back. "Show the court the difference, one exhibit at a time. Differences that can be handed up survive cross-examination. Differences that are only said are just weather."

**Choices:**
- Answer it with the record — exhibit by exhibit, date by date → **night_before**  _(FLAG: answerReady)_
  - NOTE (shown after choosing): By the last answer, you are not pleading. You are indexing. It feels, strangely, like dignity.
- Answer it from the heart — the judge should hear a mother, not a filing cabinet → **night_before**
  - NOTE (shown after choosing): The judge will hear a mother either way. The question is whether she'll also be holding the proof while she listens.

## [night_before] The Night Before
*Day 8 — Wednesday, December 16, 2026 (dayOffset 8)*

Quinn's drawing is on your refrigerator: a house, a sun doing its best, two figures holding hands with the seriousness of architecture. He drew it at a visit in November and the worker let you keep it, and it has been supervising your kitchen ever since.

The folder is packed. The packet is copied. The ask has dates. Somewhere in Ohio your sister is charging her phone; somewhere across town a stale report sits in a judge's packet next to its correction, like a photograph next to its negative; and the agency's own file now contains two dates — March 4, May 27 — that it will have to carry into the room itself.

You sleep the way people sleep before weather: lightly, and in full knowledge that you've done the preparing that preparing can do.

**Choices:**
- Set the alarm, lay out the folder, and sleep → **hearing_open**
  - NOTE (shown after choosing): Tomorrow the record speaks. Tonight, remarkably, there is nothing left to file.
- Read the agency's filing one last time, to know the other side cold → **hearing_open**
  - NOTE (shown after choosing): You know it cold by page two. Some things a year teaches you completely.

## [hearing_open] The Permanency Hearing
*Day 9 — Thursday, December 17, 2026 (dayOffset 9)*

The courtroom is smaller than its consequences. The judge has the packet — the agency's reports, the CASA report and, filed days ago and already in her hands, its correction. Ms. Adler sits close enough that her sleeve brushes yours when she writes. Mr. Osei, Quinn's lawyer, sits where Quinn's interests sit, which today is its own geography.

The judge opens the way the statute opens: this is a permanency hearing; the court will make its determinations on placement, compliance, progress, and reasonable efforts, and then determine the permanency outcome. (§ 6351(f), (f.1)) Sequence, announced out loud, on the record. Your lawyer's whole strategy, spoken by the court itself.

**Choices:**
- Take the bus in early, packet on your lap, and be seated before the agency arrives → **agency_opening**  _(cash −10)_
  - NOTE (shown after choosing): Early is a small exhibit too. The bailiff notices. Bailiffs notice everything.
- Arrive with counsel at the call of the list, packet in her briefcase → **agency_opening**
  - NOTE (shown after choosing): On time, represented, prepared. The hearing does not grade arrivals — but it remembers textures.

## [agency_opening] The Agency's Ask
*Day 9 — Thursday, December 17, 2026 (dayOffset 9)*

The agency's counsel is professional and unhurried. Quinn, she says, has been in care ten months. His mother relapsed once, after a period of sobriety, which is precisely the pattern this court must weigh. The plan has run most of a year. Children, she says, cannot wait indefinitely on adult recovery timelines — Quinn deserves a decision, and the decision the evidence supports is a goal of adoption under § 6351(f.1).

It is a well-built argument. Notice what it is built of: the spring, the pattern, the passage of time. Notice what it does not yet contain: a single document dated after July.

**Choices:**
- Listen without reacting — your turn is a place in the order, not an interruption → **agency_witness**
  - NOTE (shown after choosing): Ms. Adler writes one word on her pad and turns it toward you: sequence.
- Whisper corrections to Ms. Adler as each spring fact lands → **agency_witness**
  - NOTE (shown after choosing): She writes two of them down. The rest, her pad says without looking up, are already exhibits.

## [agency_witness] The Caseworker's Spring
*Day 9 — Thursday, December 17, 2026 (dayOffset 9)*

The caseworker testifies honestly about the case she knows best: the February relapse, the March chaos, housing searched for and not found, a mother at the beginning of treatment whose insight was, in the file's phrase, limited. Cross-examination is gentle and chronological. When did treatment complete? July. Screens since? The witness consults the file. Negative, all of them. Visits missed? A pause. None.

The testimony does not collapse — the spring was real, and nobody in your chair pretends otherwise. It simply acquires a second half, question by dated question, until the witness has described two different women and the file only has a name for one of them.

**Choices:**
- Let the chronology do the work — counsel keeps the cross short and dated → **agency_clock**
  - NOTE (shown after choosing): Short crosses end on the strongest answer. The strongest answer here was a pause, then: none.
- Signal counsel to press the witness on why the reports stop at July → **agency_clock**
  - NOTE (shown after choosing): She asks it once, cleanly, and sits down on the answer: the reports are written on a cycle. The cycle, not the mother, is what stopped at July.

## [agency_clock] Fifteen Months Is Five Months Away
*Day 9 — Thursday, December 17, 2026 (dayOffset 9)*

Then the agency plays the clock, exactly as rehearsed. In five months, counsel says, Quinn will have been in placement fifteen of the most recent twenty-two months. The law's patience has a number, and the number is approaching. Quinn's childhood, counsel says, is not a waiting room; every month of limbo is a month of a four-year-old's life spent between addresses.

It lands, because half of it is true: Quinn does deserve a decision. What the argument quietly does is borrow a determination the statute schedules for month fifteen (§ 6351(f)(9)) and spend it at month ten, in a hearing whose actual questions are compliance, progress, and efforts. Ms. Adler's pen moves once. She has been waiting, politely, for this exact sentence.

**Choices:**
- Let Ms. Adler answer the clock in the closing, where the determinations live → **agency_packet**
  - NOTE (shown after choosing): Clocks are answered with dates, and the dates are all in the closing's first five minutes.
- Ask her to object now — the fifteen-month rule isn't this hearing's rule → **agency_packet**
  - NOTE (shown after choosing): She shakes her head once, barely. "Not an objection," she whispers. "A determination. We answer it in the (f) findings, where it can't be waved off."

## [agency_packet] The Packet They Brought
*Day 9 — Thursday, December 17, 2026 (dayOffset 9)*

The agency rests on its packet: the caseworker's reports, the CASA summary — five months old, warm, describing July — and the scored assessment summary with its spring provision still reading "housing: unstable." The judge turns pages with the particular stillness of a person comparing documents against each other.

In her packet, because your side filed them days ago, sit the correction and the rebuttal, each with its proof attached: the lease behind one, the receipts behind the other. Nobody has to announce them. That is the entire point of filing before the hearing: the packet corrects itself while the agency is still talking.

**Choices:**
- Watch the judge read — the filed paper is doing its work without you → **josie_case**
  - NOTE (shown after choosing): Paper filed early works in silence. It is the only advocate in the room who never gets nervous.
- Ask Ms. Adler to highlight the stale dates out loud for the transcript → **josie_case**
  - NOTE (shown after choosing): "She's seen them," Ms. Adler murmurs. "Watch her bookmark. Judges bookmark what they're going to use."

## [josie_case] Exhibit by Exhibit
*Day 9 — Thursday, December 17, 2026 (dayOffset 9)*

Your case is not a speech. It is a handing-up. Exhibit 1: treatment, completed, with the provider's letter and its aftercare dates. Exhibit 2 becomes Exhibit 3 in the judge's hands — she is reading ahead — screens, a column of one word, eight months long. Exhibit 4: the visit log, initialled, complete, unbroken. Exhibit 5: the lease, June, with the receipts standing behind it like ushers.

Ms. Tran's letter is read into the record. The (f)(2) compliance story and the (f)(3) progress story are the same exhibits wearing their two statutory hats, and counsel says so, once, so the transcript knows it. The judge asks two questions — both about dates. Dates are the questions this packet was built to survive.

**Choices:**
- Hand up each exhibit as counsel names it, in index order → **referral_cross**
  - NOTE (shown after choosing): Index order. Thirty seconds a fact, exactly as the one-page index promised the court.
- Let counsel handle the paper and keep your eyes on the judge → **referral_cross**
  - NOTE (shown after choosing): Either way, the exhibits arrive numbered. The judge's bookmarks multiply at the end of the table.

## [referral_cross] March 4. May 27.
*Day 9 — Thursday, December 17, 2026 (dayOffset 9)*

Then counsel lays down the timeline, politely, the way it was rehearsed: not an accusation, a page. The housing referral — required by the plan, necessary to the housing the agency's filing calls late — drafted March 4. Sent May 27. The lease the mother obtained anyway: June. The page comes from the agency's own record, produced on the mother's written request under § 3130.44(d).

The agency's counsel does not dispute the dates; there is nothing in them to dispute. The judge writes for a long moment. Whatever the (f)(5.1) reasonable-efforts determination says at the end of this hearing, it will now be written in a room where those two dates have been said out loud, on the record, with the file to prove them.

**Choices:**
- Sit still through the silence after the dates — it is working → **gal_testimony**
  - NOTE (shown after choosing): Silence after a date is the sound of a determination changing shape.
- Look at the caseworker — not in triumph, just to see if she knew → **gal_testimony**
  - NOTE (shown after choosing): Her face suggests the drawer had an owner, and it wasn't her. Files outlive the hands that fill them. That's the system's mercy and its menace.

## [gal_testimony] Quinn's Lawyer Speaks
*Day 9 — Thursday, December 17, 2026 (dayOffset 9)*

Mr. Osei rises for Quinn — not for you, and he says so, which is why the room believes what follows. He has watched the visits. He has read the aftercare reports and the screen history. In his judgment, Quinn's interest is not served by ending the aim of return while the return is, demonstrably, being built — and he supports the stepped schedule, because it is a schedule: "Dates, Your Honor. The child gets either a homecoming or a record of exactly where it stopped, and either way he is not asked to wait in the abstract."

Support from the child's own lawyer is not a favor banked. It is a professional judgment, entered on the record, and the judge receives it the way she receives exhibits: as something that will still exist tomorrow.

**Choices:**
- Listen the way Quinn would want you to — as his mother, not as a litigant collecting allies → **aunt_testimony**
  - NOTE (shown after choosing): For four seconds the hearing is about a small boy and a drawing of a house. Then it is a courtroom again.
- Note his exact words in your folder, dated, while he says them → **aunt_testimony**
  - NOTE (shown after choosing): "Not asked to wait in the abstract." You will think about that sentence for years, whatever happens next.

## [aunt_testimony] The Voice From Ohio
*Day 9 — Thursday, December 17, 2026 (dayOffset 9)*

The clerk brings up the video link, or the packet's tab is turned to Lori's study — the form depends on choices made days ago — and Quinn's aunt enters the record: your sister, in Ohio, studied and approved, four plain points delivered in a voice so much like your mother's that you have to look at the table for a moment.

She supports Quinn going home to you; she says it first, before anything about herself. And she is, herself, a completed study and a standing option — a fit and willing relative under § 6351(f.1) — which means the sentence the agency built its opening around, the only-permanence sentence, cannot be said in this room anymore with a straight face.

**Choices:**
- Lori testifies live by video, and her completed home study is handed up as she speaks → **casa_moment**  _(HIDDEN + Transcript — maternal aunt testified; completed home study filed ; REQUIRES FLAG: kinTestifies)_
  - NOTE (shown after choosing): The judge asks her two questions directly, and she answers them like a person, not a document. That was the whole argument for live.
- Counsel hands up Lori's home study and letter, and summarizes her position for the record → **casa_moment**  _(REQUIRES NO FLAG: kinTestifies)_
  - NOTE (shown after choosing): The study is real and filed. The judge reads it in the time she has, which is less time than a voice would have been given.

## [casa_moment] Correcting a Document, Not a Person
*Day 9 — Thursday, December 17, 2026 (dayOffset 9)*

Near the end, the CASA report surfaces by name — the judge has it, and its age comes up the way ages of documents do in courtrooms: in a question that sounds casual and isn't. "This describes the spring, does it not?"

This is the moment the day-6 choice was made for. The correction is either already in the packet — filed, dated, courteous, proof attached — or it has to be manufactured now, out loud, against a volunteer who came to help a child and whose only error was writing in July about July. How counsel handles the next sixty seconds will be remembered by the one person whose memory decides the case.

**Choices:**
- Counsel addresses the paper, not the person: "The report was accurate when written; the correction and its proof were filed Monday, Your Honor." → **josie_question**
  - NOTE (shown after choosing): The judge nods at the packet, not at the argument. Filed paper gets nods. Volunteers keep their dignity. Both things stay in the room.
- Counsel challenges the volunteer personally — how closely has she actually followed this case since summer? → **josie_question**  _(FLAG: casaAttacked)_
  - NOTE (shown after choosing): The question lands badly in the way Ms. Adler predicted: the room's sympathy moves, visibly, to the volunteer — and the court's confidence in your side's judgment cools with it.

## [josie_question] "What Is Different This Time?"
*Day 9 — Thursday, December 17, 2026 (dayOffset 9)*

Then the judge turns to you, and it is the kitchen-chair question, except the chair is real and so is the silence around it. "Ms. Haas. There was a relapse before this case, in a period when things were also, I am told, going well. What is different this time?"

Every eye in the room is a weight. The woman you were in February would have answered with a vow. The woman in this chair has a folder, an index, and eight months of dated paper, and she answers the way she rehearsed — or she answers from the heart alone, and the heart, in this room, has no exhibit number.

**Choices:**
- Answer with the record: treatment, aftercare, the column of screens, the unbroken visits, the June lease — date by date → **closing**
  - NOTE (shown after choosing): "Different," you say, "is a paper trail, Your Honor. February me made promises. I brought you the receipts instead."
- Answer from the heart: tell her what Quinn's drawing on your refrigerator means to you → **closing**
  - NOTE (shown after choosing): It is true, every word. Truth without an exhibit number is the most perishable substance in this building, and the moment carries it away like weather.

## [closing] Determinations First
*Day 9 — Thursday, December 17, 2026 (dayOffset 9)*

Closings. The agency's is brief and returns to its strengths: the spring, the pattern, the clock, a child's life not on hold. Then Ms. Adler stands, and the whole nine days stand with her, because a closing can only argue what a record contains.

She begins where the statute begins. The court must make its determinations under § 6351(f) — placement's necessity, compliance, progress, reasonable efforts — on this record; and only based upon those determinations and all relevant evidence does the court choose among § 6351(f.1)'s outcomes. What she asks the court to choose depends, in the most literal way, on what the last nine days put into the room. She takes a breath, and chooses her ask.

**Choices:**
- Close in sequence: (f)(2) compliance, (f)(3) progress, (f)(5.1) the unsent referral — then (f.1)(1), the stepped return with dates → **end_win**  _(HIDDEN + Order — determinations under § 6351(f)(2), (3), (5.1) made on the record ; HIDDEN + Order — stepped return schedule with dates ; REQUIRES FLAG: recordsRequested ; REQUIRES FLAG: exhibitsReady ; REQUIRES FLAG: steppedAsk ; REQUIRES NO FLAG: casaAttacked)_
  - NOTE (shown after choosing): Every element of this ask exists because a choice built it: the record was requested, the packet was indexed, the return was drafted as a schedule.
- Ask only to hold the goal at reunification, with a short review — no return schedule proposed → **end_partial**  _(HIDDEN + Order — determinations under § 6351(f)(2), (3), (5.1) made on the record)_
  - NOTE (shown after choosing): The goal survives this ask. A schedule does not — and a judge left to set the tempo sets it with the clock out loud.
- Argue the goal in the abstract — eight months of effort, a mother's fairness claim — without tying it to the determinations → **end_loss**  _(HIDDEN + Order — the findings that preserve the issues)_
  - NOTE (shown after choosing): Fairness, argued in the air, meets an evidence fight on the ground. The room can feel which one the statute is listening to.

## [end_win] Goal Held — Reunification, With a Date
*Day 10 — Friday, December 18, 2026 (dayOffset 10)*

The order arrives the next day, and Ms. Adler reads it to you over the phone slowly, the way you'd read a letter from the front. The agency's request to change Quinn's permanency goal is denied. The goal remains reunification. And under § 6351(f.1)(1), the court orders the return it was actually offered: a stepped schedule, with dates — unsupervised day visits in January, overnights by February, full return by the spring review, services and screens continuing through every step.

Inside the order, in the findings, the determinations sit in their statutory order: substantial compliance with the plan (§ 6351(f)(2)); the circumstances that caused placement, alleviated in the respects the exhibits proved (§ 6351(f)(3)); and on reasonable efforts to finalize the plan (§ 6351(f)(5.1)), a single dry sentence noting that the agency's housing referral was drafted March 4 and sent May 27, and that the resulting delay is not the mother's.

Quinn is told, in words for a four-year-old, that home now has a calendar. You put the order in the folder, in front of the request that started it all. The folder, for once, is a happy archive.

**Ending.**

**Debrief:**
- WHAT THE FILE SAID — The record the court acted on contained: the agency record produced on the written request under 55 Pa. Code § 3130.44(d), whose own pages dated the housing referral March 4 (drafted) and May 27 (sent); the indexed progress packet — treatment and aftercare, eight months of negative screens, the unbroken visit log, the June lease; the maternal aunt's live testimony and completed home study; the written correction to the five-month-old CASA report, filed before the hearing; the rebuttal to the scored summary's stale "housing: unstable" line; and the GAL's stated support. The hidden assessment in this scenario rated the same items the form always rates — what the file could see. This time, the file could see December.
- THE LAW THAT CONTROLLED IT — A permanency hearing must determine continuing necessity, compliance with the plan (§ 6351(f)(2)), progress toward alleviating the circumstances that caused placement (§ 6351(f)(3)), and whether reasonable efforts were made to finalize the plan (§ 6351(f)(5.1)); only based upon those determinations and all relevant evidence does the court choose the § 6351(f.1) outcome. The stepped return was that outcome — (f.1)(1), return to parent. The § 6351(f)(9) fifteen-of-twenty-two determination was not triggered at month ten and decided nothing here; and the aunt's presence kept (f.1)(4), a fit and willing relative, on the table, defeating the claim that adoption was the only permanency available.
- THE HONEST PART — This ending was built from paper, and paper is never the whole story: a different judge could have weighed the spring more heavily; the GAL could have landed the other way; the referral page could have been missing from the produced record, as pages sometimes are. Outcomes in this system turn on workers, judges, resources, and luck as much as on any parent's work, and this outcome is not a verdict that Josie is a good mother — it is a record of what a court could see, on the day it had to decide. The return still has steps, and steps can stumble. What changed is that the plan aims at home again, with dates — and dates, unlike hopes, can be kept.

## [end_partial] Goal Held — The Clock Named Aloud
*Day 10 — Friday, December 18, 2026 (dayOffset 10)*

The order holds the line and names the price of holding it. The agency's request to change the goal is denied — reunification remains Quinn's permanency goal. But the court orders no return schedule. Placement continues, services continue, and a review is set ninety days out.

And then, in the hearing's last minutes and again in the order's final paragraph, the judge does the thing unanswered clocks invite judges to do: she dates it. Quinn reaches fifteen of the most recent twenty-two months next May — May 2027 — and at that point the § 6351(f)(9) determination will be this court's business in earnest. "Everyone in this case," the order concludes, "should conduct themselves between now and then as if that date were on the cover of the file." It is now. She put it there.

You won the goal and lost the tempo. The folder goes home with you, thicker, and the spring is suddenly a deadline with exhibits due.

**Ending.**

**Debrief:**
- WHAT THE FILE SAID — The goal survived on whatever of the record was actually built and argued: the progress was real, and enough of it reached the court to defeat a goal change today. What the file did not contain — or what the closing did not ask for — was a return the court could sign: no dated, stepped schedule under § 6351(f.1)(1) was granted, whether because the packet was never indexed, the agency record was never requested in writing (so the unsent referral stayed unproven), the CASA paper went personally contested instead of corrected, or the ask itself was framed as open-ended time. The court kept the aim and kept the child placed, and filled the silence where a schedule should have been with the only date left in the room: the clock's.
- THE LAW THAT CONTROLLED IT — The § 6351(f) determinations were made and supported holding the goal; the § 6351(f.1) outcome chosen was continuation under the existing goal with a ninety-day review, not a return. The § 6351(f)(9) determination — whether, at fifteen of the last twenty-two months, the agency has filed or joined a termination petition, subject to the relative-care, documented-compelling-reason, and services-not-provided exceptions — is not triggered at month ten, and this judge did not pretend otherwise. She did something courts may always do: she named the coming date aloud, in May 2027, and set the case's tempo by it. A named clock is not a ruling. It is a promise about the next hearing's weather.
- THE HONEST PART — A partial win is a real win with a fuse in it, and this ending is not a judgment on Josie's worth or effort — outcomes here turn on workers, judges, calendars, and luck, and on which papers existed when a particular judge looked up. The ninety days ahead are not a lesser version of the fight; they are the fight, at higher speed, with one advantage the last nine days proved: the machinery of paper — requests, packets, corrections, schedules — is learnable, and it is now learned. The clock is named. Named clocks can be answered. The next hearing is where the answering is due.

## [end_loss] Goal Changed — The Record She Built
*Day 10 — Friday, December 18, 2026 (dayOffset 10)*

The order changes the goal. Under § 6351(f.1), Quinn's permanency goal is now adoption, and the agency is directed to proceed accordingly. Ms. Adler reads the whole order to you, including the parts that hurt, because she has never once edited the truth for you and is not starting on the worst day.

Read it the way she taught you, all the way to the end. The goal change is not a termination of your rights — no rights ended today, and termination, if the agency ever seeks it, remains its own proceeding at which the agency would have to prove its grounds by clear and convincing evidence. Your exhibits are in the record. The aunt's completed home study is filed in this case, where no future court can pretend it doesn't exist. The determinations were made on a record that contains your December, not only your spring — and records outlast orders.

In February, Quinn went into care, and a file began rating a woman it could barely see. The woman it rates now has a folder, a lawyer whose chair she can picture, and a sister in Ohio with an approved home. The goal changed. The record she built did not disappear with it — and every future fight in this case starts from that record, not from zero.

**Ending.**

**Debrief:**
- WHAT THE FILE SAID — In this ending the evidence fight was lost on its mechanics, not on the year's facts: the progress existed, but too little of it reached the court in usable form — the agency record never requested in writing, so the eleven-week referral delay stayed an assertion instead of two dates; or the proof arrived as a pile rather than an indexed packet; or the closing argued the goal in the abstract while the agency argued determinations. What survives in the file matters and is real: the exhibits that were offered, the aunt's filed home study, the corrections and timelines that were filed — the findings that preserve the issues for whatever comes next.
- THE LAW THAT CONTROLLED IT — Based on the determinations made under § 6351(f) and the evidence as the court weighed it, the court chose the § 6351(f.1) outcome of adoption, directing the agency to file for termination. That choice changes what the plan aims at and what the system works toward — and it is all it does today. It is not itself a termination: parental rights end, if ever, only at a separate termination proceeding where the agency bears the burden of proof by clear and convincing evidence. The fifteen-of-twenty-two determination under § 6351(f)(9) was not the basis of this order — at month ten it is not yet triggered — but the changed goal now runs toward it, which is why the preserved record matters.
- THE HONEST PART — This is the bad outcome, and no strategy guide should dress it as a secret victory: a goal changed to adoption is a serious, grievous turn in a family's case. It is also not a verdict that Josie failed as a mother — her eight months happened; the screens, the visits, the lease are facts regardless of what one hearing did with them. Outcomes in this system turn on workers, judges, resources, and luck, alongside preparation, and the same record in a different courtroom can end differently. What no one can take is what the preparation built: a mother who knows how this system reads, a filed study in Ohio, and a record — hers now, as much as theirs — that every next step starts from.
