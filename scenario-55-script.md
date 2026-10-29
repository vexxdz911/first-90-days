# The County Line (a fictional composite) — Node-for-Node Script (Scenario 55)

Scenario 55 of *The First 90 Days* — script generated node-for-node from `scenario-55.json`; the JSON is the source of truth.

A fictional composite built from published Pennsylvania dependency practice and documented system patterns. Not a real family's case.

**Content note:** child removal, court hearings, family separation.

**How to read effects:** `cash` is money spent or received at that choice; `FLAG:` marks a fact the story remembers; `HIDDEN +` is an assessment item the player never sees scored; `REQUIRES:` gates a choice on an earlier fact; `NOTE:` is authorial, not spoken in-world. Endings are marked **Ending.** with a **Debrief:**.

**Start date:** Monday, November 2, 2026. **Tier:** Complex. **Start cash:** $205.

---

## [start] The school calls

*Day 0 — Monday, November 2, 2026*

You learn about the move from Zola's school, which is how you learn the school no longer has Zola. The secretary, gentle as a nurse with bad labs: "She was withdrawn Friday, sweetie. Transferred to Riverton Elementary. We assumed you knew." Riverton is in the next county. Zola's desk is there now. Her reading group is there. Her visits with you, until Friday a twelve-minute drive, are fifty-five minutes each way — when the agency's transport runs, which it does not on weekends.

You call the agency before you call anyone else, and Ms. Halvorsen gives you the sentence the system keeps for this: "It was an emergency placement disruption. There were no beds in the county."

**Choices:**
- Ask for it in the order the law will ask later: "When exactly was she moved, who decided, and where is it written?" → **when_who_written**  _(HIDDEN + move-notice)_

## [when_who_written] When, who, written

*Day 0 — Monday, November 2, 2026*

Thursday evening. A supervisor's approval by phone. Written — she hesitates — 'in the placement log.' You note the hesitation the way you have learned to note everything: in your notebook, dated, with the time of the call. Emergency moves are sometimes real emergencies. They are also sometimes the moment a file reveals what it was doing all along.

"And my sister?" you ask. "Beatrice was identified in February." A pause with keyboard sounds in it. "It says here a kinship packet was mailed to her February 12th. There's no response recorded."

**Choices:**
- Call Beatrice before the hour is out. Ask her one question: "What did you receive from the county in February?" → **call_beatrice**

## [call_beatrice] Beatrice keeps everything

*Day 0 — Monday, November 2, 2026*

Beatrice is a night-shift nurse who keeps a household the way hospitals keep charts: a binder, labeled by year, with sub-labels. She puts you on speaker and you can hear the binder open. "February," she says. "Car insurance. Your birthday card — you were late. A jury summons for March, which I served. Nothing from any county about Zola, because I would have framed it. Imani — I called them. February 20th and again in March. I spoke to a person. I wrote her name in this binder."

Two paper systems are now in conflict: the agency's file, which says a packet was mailed and ignored; and your sister's binder, which says two calls were made and nothing arrived. One of these systems is about to be audited by the other.

**Choices:**
- Call your counsel in the morning. The word for what you need is 'record' — and the fight has three fronts: the move, the kinship file, and Zola's fifty-five minutes. → **zola_call**

## [zola_call] Zola, by phone

*Day 1 — Tuesday, November 3, 2026*

Your first call with Zola in Riverton is eleven minutes long and conducted, on her end, from a bathroom — 'it's the quiet room' — in a voice doing eight-year-old bravery at professional standard. Her inventory: the foster mother is kind and braids 'almost like Aunt Bea'; the new school has a fish tank and no one who knows her reading level; she has been put in the 'blue group,' which she has assessed, correctly, as not the group she was in.

'Is Aunt Bea mad I didn't go to her house?' she asks, at the end, quietly — and there it is: a child absorbing a system's failure as a family's choice. 'Aunt Bea is not mad. Aunt Bea has a binder. The binder and I are working on it.'

**Choices:**
- Work means three fronts, in writing, this week. Call your counsel in the morning. → **counsel55**  _(HIDDEN + child-voice)_

## [counsel55] Three fronts

*Day 1 — Tuesday, November 3, 2026*

Your counsel lays it out on a legal pad in three columns. "Front one: review. A party can ask the court to look at a placement move — we file, and we ask for interim relief on visits and school transport so the status quo doesn't harden while we litigate. Front two: the record. Your written request under 55 Pa. Code § 3130.44(d) — the family-finding page, the placement log, the move memo, the call notes. Front three: Beatrice, again, from zero — a fresh written kinship submission, so complete the county can't lose it."

"And if the record says the move was planned before the 'emergency'?" — "Then front one gets much easier. File everything this week."

**Choices:**
- File all three: the review request, the § 3130.44(d) record request, and Beatrice's new written submission — with her February call dates in it. → **school_records**  _(cash −16; FLAG: reviewFiled; FLAG: recordsRequested; FLAG: kinFiled; HIDDEN + record-request; HIDDEN + named-kin)_

## [school_records] Her old school's file

*Day 2 — Wednesday, November 4, 2026*

Zola's old school releases her file to you as her mother, and it is the portrait of a specific child that a county-line transfer erases: reading group placement earned in October, the teacher's note ('Zola reads aloud to the kindergarten buddies on Fridays — a responsibility she guards'), attendance perfect since September. The Riverton school, through no fault of its own, received a name, a birthdate, and a 'blue group' guess.

Her teacher, told where Zola went, says the sentence school people say in these cases and mean as indictment: 'Nobody called us. We would have sent her records the same day — and we would have asked why.' The asking-why, institutionalized late, is your counsel's job now.

**Choices:**
- File all three fronts: review, record, and Beatrice from zero. → **file_three**

## [file_three] Filed in triplicate

*Day 3 — Thursday, November 5, 2026*

Beatrice's new submission is a small masterpiece of un-losability: hand-delivered, date-stamped copy kept; her clearances initiated the same day; her landlord's name and number included pre-emptively; her night-shift schedule attached with the overnight care plan already written into it, because she has read enough of your case to know that questions answered before they're asked are called facts, and questions answered after are called excuses.

The agency's response to your review filing arrives in four days: the move was necessary, the Riverton home is licensed and kind, 'no kinship resource was available,' and the matter is set for December 3rd.

**Choices:**
- December 3rd is a month of fifty-five-minute drives. Fight the interim first: ask the court for expanded visits and school continuity now, not at the review. → **agency_version**

## [agency_version] The agency's answer

*Day 4 — Friday, November 6, 2026*

The agency's written response to your review filing is courteous, complete, and — read carefully — an artifact of the file it defends: the move 'necessitated by an emergency disruption'; the Riverton home 'licensed, experienced, and available'; kinship 'explored at intake, with the identified relative non-responsive to outreach.' Non-responsive. Beatrice, who keeps a binder with sub-labels, has been filed under a word she would cross out in red pencil.

Your counsel tabs the sentence. 'This is the paragraph the record request exists for,' she says. 'Every factual claim in it is checkable against their own notes. We are going to check all of them, in order, and bring the receipts to December.'

**Choices:**
- Fight the interim first — visits and school continuity now, while the receipts accumulate. → **interim_ask**

## [interim_ask] The interim

*Day 6 — Sunday, November 8, 2026*

The interim ask is modest on purpose — courts grant modest asks from parties who are building to prove immodest ones. You ask for: weekend visits restored (at your home, supervised as before), agency transport for Wednesday visits, and Zola's school records and reading program shared with you weekly so her education doesn't fork into two counties' versions of third grade.

You get most of it within the week, in a short order. Modest asks also do quiet work: they put a judge's eyes on the file a month before the review — a judge who now knows there is a county line in this case, and a sister, and a binder.

**Choices:**
- Use the month. The record request is the engine — everything else is steering. → **transport_log**

## [transport_log] Fifty-five minutes, logged

*Day 7 — Monday, November 9, 2026*

You start the transport log the day the interim order issues: each visit's drive, timed, with the transport van's arrivals and one memorable non-arrival noted in the flat style the file has taught you. November 9th: 'Van 40 minutes late. Visit shortened. Zola asked if the van forgot her. Advised the van did not forget her; the schedule did.'

Distance in these cases is usually argued as a feeling. Logged, it becomes a record — hours of a childhood spent on a highway because a kinship file was mishandled in February. By December the log will hold nine round trips. You intend the judge to do that arithmetic herself.

**Choices:**
- Use the first restored weekend visit to see the Riverton home with your own eyes. → **first_riverton_visit**

## [first_riverton_visit] The Riverton home

*Day 8 — Tuesday, November 10, 2026*

The Riverton foster mother is as advertised — kind, experienced, unoffended by your existence — and her home runs the calm shift-work of a professional respite house: three children this month, a wall calendar in three colors, a quiet room that Zola has accurately described. She makes tea and says, without prompting, the thing that will matter in December: 'I take the emergencies. I'm good at the first month. I'm not set up to be somebody's whole school year, and I told them that when I took her.'

You write it down in the car, word for word, with her permission. The system's own placement is telling you it was a bridge. The only dispute is whether the far shore was ever looked for.

**Choices:**
- On the drive back, the agency calls: a new worker has inherited the file. Listen for what she inherits besides paper. → **halvorsen_call**

## [halvorsen_call] The new worker

*Day 9 — Wednesday, November 11, 2026*

Ms. Halvorsen took over the case in October — the fourth worker, by your count, since February — and she has the inheritor's honesty: 'I've read the file twice. I can't defend February, and I'm not going to try in this call. What I can tell you is the December review will get my honest read of the record as it stands then — including wherever Beatrice's study has gotten to.'

Worker turnover is one of the system's quiet engines: February's mistakes were made by a worker who has left; the file remains, and only the file can be cross-examined. Your record request — filed by you, answered to you — is about to become the case's memory. It arrives this week.

**Choices:**
- Read it the day it lands. Family finding first, placement log second, dates throughout. → **record_arrives55**

## [record_arrives55] The record arrives — first half

*Day 10 — Thursday, November 12, 2026*

The family-finding page is everything Beatrice's binder promised. Intake, February: 'Maternal aunt, Beatrice [surname], identified by mother. States willing. Packet to be mailed.' Then the call notes — the agency's own — February 20th: 'Aunt called; states no packet received; advised packet remailed.' March 9th: 'Aunt called again; packet still not received; aunt advised to await study scheduling.' After March 9th: silence, in the file's handwriting. No packet tracking. No study scheduled. No third call made by anyone.

The February 12th 'mailing' in the summary you were quoted was the intention. The remailed packet in the notes was the second intention. Neither intention has a tracking number, because neither, so far as this record shows, became an envelope.

**Choices:**
- Read on. The placement log and the move memo are the second half — and you are looking for a date. → **binder_scene**

## [binder_scene] The binder, reconciled

*Day 11 — Friday, November 13, 2026*

You and Beatrice reconcile the two paper systems at her kitchen table, page by page, the way auditors close a year: her binder's February 20th entry ('Called county. Spoke to a woman in intake. Said packet would be remailed.') beside the agency's own call note for the same date, with the same substance in a caseworker's hand. March 9th: binder and file agree again. The systems agree about everything except the conclusion the summary drew from them.

'I was never non-responsive,' Beatrice says, closing the binder with the calm of a woman who has been proven right by the opposing archive. 'I was responsive into a drawer.' The summary's word cannot survive its own file. Your counsel will make sure December knows it.

**Choices:**
- Read on into the placement log — you are looking for the date the Riverton bed entered the story. → **the_date55**

## [the_date55] October 20th

*Day 12 — Saturday, November 14, 2026*

The placement log entry for Zola's move is dated Thursday, October 29th, 6:40 p.m. — 'emergency disruption, foster father hospitalized.' That part was true; the foster father's surgery was real, and no one begrudges the agency Thursday night. But beneath it in the packet sits the placement unit's memo, dated Tuesday, October 20th — nine days before the emergency — listing 'anticipated bed need, one female age 8, Riverton resource identified and held.'

The Riverton bed was reserved nine days before the emergency that supposedly required it. What the memo actually documents is a unit managing capacity: a foster home known to be fragile — the father's health was in the file since September — and a contingency bed held in the next county because your county had none. The emergency was real. The county line was a plan.

**Choices:**
- Give both dates to your counsel. "October 20th and October 29th. The emergency was real and the line was planned. Both." → **september_flag**  _(FLAG: recordRead)_

## [september_flag] September, in the file

*Day 13 — Sunday, November 15, 2026*

The record's September pages complete the picture the two dates began: the original foster father's cardiac condition is documented in the file from September 15th — 'foster father under cardiology care; placement unit advised home may become unavailable; contingency planning recommended.' Recommended in September. Executed — nine days of it, ending at a county line with a bed already held — in late October. In the six weeks between the recommendation and the move, the file contains no kinship entry at all. Beatrice's name does not appear between March and your November filings.

Six weeks of contingency planning that never once contingently planned for the child's aunt. Your counsel underlines nothing; she doesn't have to. The absence underlines itself.

**Choices:**
- Two dates and one silence. Give all three to your counsel, in the order the file gives them. → **two_dates**

## [two_dates] What the dates do

*Day 14 — Monday, November 16, 2026*

Your counsel is careful, the way she is when something matters: "We do not argue they invented an emergency. We argue the honest version: they planned for a disruption for nine days and never once, in those nine days, picked up the kinship file with Beatrice's name in it — a file with two logged calls from the aunt herself. A planned move has room for a kinship check. That omission is the case. Not villains. An omission, documented by their own paper."

Meanwhile Beatrice's study, this time, must be impossible to lose. Her home county study is requested through the county where Zola's case sits — a courtesy study, in the jargon — and courtesy is exactly what you intend to audit.

**Choices:**
- Get the courtesy study request in writing — who sent it, to whom, what date — and give Beatrice a copy to chase from her side. → **supervisor_meet55**  _(FLAG: studyTracked)_

## [supervisor_meet55] The supervisor, conceding early

*Day 15 — Tuesday, November 17, 2026*

The agency supervisor, at a meeting your counsel requests before the courtesy study becomes the case's second lost envelope, is more candid than her position paper: 'The kinship exploration in February and March was inadequate. I'll stipulate the call notes say what they say. What I need from December is a study I can act on — run Beatrice now, run her properly, and if she's approved, my recommendation will follow the study.'

It is the sound of an institution correcting at the speed institutions do — slowly, verbally, and only after a record request has made the correction cheaper than the defense. Your counsel gets the substance into a letter the same day, because verbal concessions evaporate and letters don't.

**Choices:**
- Convert the concession into the study's tracking: who sends the courtesy request, to whom, on what date. → **imani_program**

## [imani_program] Your standing

*Day 16 — Wednesday, November 18, 2026*

Your own compliance gets its paragraph in the packet, and it is a good one: visits kept at a rate the transport log itself verifies (you showed up for all of them, including the shortened one); the program milestones met; your counsel's filings timely to the day. Standing in a placement fight is partly moral arithmetic — the parent who has done everything asked, on paper, gets to ask the court to hold the agency to the same standard — and your packet intends to ask exactly that.

'We're not claiming perfection,' your counsel says. 'We're claiming symmetry. February asked things of Beatrice that February's mail never delivered. December should be more careful with everybody.'

**Choices:**
- The courtesy study request goes out. This time, your copy has a date stamp and a chaser: you. → **courtesy_study**

## [courtesy_study] Lost, once

*Day 17 — Thursday, November 19, 2026*

The courtesy study request is 'sent' on a Tuesday. By the following Tuesday, Beatrice's county has no record of receiving it. This is the cross-county disease in its pure form: two bureaucracies, each certain the other is holding the baby. The difference this time is you — a person with a copy, a date, and a phone, standing between the two certainties until they reconcile.

It takes four days and one hand-carried duplicate, delivered by Beatrice to her own county's office with a date stamp, to get the study opened. Four days, charged to nobody's account but Zola's calendar.

**Choices:**
- Note it for the review: the study's timeline, including whose hands it passed through and whose it didn't. → **county_capacity**

## [county_capacity] The honest exhibit

*Day 18 — Friday, November 20, 2026*

Your counsel includes in the packet an exhibit that surprises the agency by helping it: the county's own placement-capacity report for October, showing zero available in-county beds for Zola's age group on the night of the move. She includes it deliberately. 'We concede the emergency and the bed map,' she tells you. 'Our case was never that a bed existed. It's that in nine days of planning — six weeks of documented warning — the kinship check that would have made the bed unnecessary was never run. Conceding what's true buys the right to be believed about what isn't.'

It is the batch's recurring strategy in one paragraph: the strongest advocates are the ones whose concessions the court can rely on.

**Choices:**
- Beatrice's clearances go in — hers, and her daughter's — while the study opens. → **beatrice_clearances**

## [beatrice_clearances] Clearances, again from zero

*Day 19 — Saturday, November 21, 2026*

Beatrice's clearances are filed with the grim comedy of a family doing a thing the second time as though it were the first: her prints, her daughter's prints (the daughter is the documented overnight adult on night-shift rotations), the child-abuse and state-police checks initiated with confirmation numbers Beatrice logs in the binder under a new sub-label: 'ZOLA — STUDY (SECOND ATTEMPT).'

The worker assigned in Beatrice's county is new to the case and reads the summary's 'non-responsive' line in Beatrice's presence. Beatrice opens the binder to February without a word. The worker reads. 'I'll note the discrepancy in the study,' she says, in the tone of a person revising a professional opinion of her own office.

**Choices:**
- Her interview is next — the study's heart. Be reachable; be nowhere near it. Studies interview households, not advocates. → **beatrice_interview**

## [beatrice_interview] Beatrice, interviewed

*Day 20 — Sunday, November 22, 2026*

The study interview runs two hours and covers the territory studies exist to cover: discipline (hospital rules — explain, redirect, document); the night shifts (daughter documented, neighbor as backup, the binder as evidence of a household that plans); Zola's school (she has already called the old school about re-enrollment timing — the registrar knows her voice); and the question underneath all of them, asked plainly: 'Why you, why now?'

'Because I was always the answer,' Beatrice says. 'February mailed it to the wrong conclusion. Ask the file — the real one, not the summary.' The worker writes it down. Workers write down the sentences that sound like the file agreeing with itself.

**Choices:**
- The study proceeds to the home visit and the landlord letter. The report is weeks out; December is closer. → **beatrice_study**

## [beatrice_study] The study, this time

*Day 21 — Monday, November 23, 2026*

Beatrice's home study proceeds with the eerie smoothness of a thing being watched: clearances filed and returned, the home visit thorough, her night-shift care plan examined and accepted — her daughter, grown and ten minutes away, documented as the overnight adult on work nights, clearances filed for her too. One wrinkle: the landlord's consent letter for a placement in a rental, requested late by the worker, obtained by Beatrice in forty-eight hours because nurses understand documentation the way sailors understand weather.

The report, when it issues, approves her without conditions. The woman the file wrote off in March as a non-response is approved in November on the first complete attempt.

**Choices:**
- Ask for the study report's transmittal to the hearing county in writing, with a date — paper has died on that road before. → **daughter_plan**  _(cash −10; FLAG: studyApproved)_

## [daughter_plan] The overnight plan, documented

*Day 23 — Wednesday, November 25, 2026*

Beatrice's daughter — a grown woman with a toddler of her own, ten minutes away — formalizes her role in a signed care plan: the overnight adult on Beatrice's three weekly night shifts, her clearances attached, her own daughter's sleeping arrangement in the plan spelled out because plans that spell out the small people are the ones courts trust. The worker verifies it by interview and notes, in the study's margin, 'multi-adult support structure documented and interviewed.'

Compare February, when the agency's whole knowledge of this family fit in the word 'non-responsive.' The distance between the file then and the file now is the scenario.

**Choices:**
- One more document: Zola's old school, on re-enrollment. Get it in writing before the transmittal fight. → **school_letter55**

## [school_letter55] Her seat in the circle

*Day 24 — Thursday, November 26, 2026*

Zola's old school writes back within the week — the registrar and her teacher signing jointly, a bureaucratic duet: re-enrollment can be effected within days of a court order; her reading-group placement 'will be restored on return, the group having kept her role in the Friday reading-aloud rotation in her absence.' Someone at that school kept a chair in a circle for a child the system had mislaid across a county line. The letter goes into the packet where sentiment would go, except that it is not sentiment — it is an enrollment office's official position, and courts can order around it.

You read the letter twice on the bus home. Then you turn to the study report's journey — the road where this case's paper has died before.

**Choices:**
- Get the report's transmittal to the hearing county in writing, with a date. → **transmittal**

## [transmittal] Zola's voice, and the Riverton truth

*Day 25 — Friday, November 27, 2026*

Two more documents complete the packet. Zola's counsel files her position: she likes the Riverton foster mother, who is kind and braids well; she wants her old school, her old reading group, and 'Aunt Bea's house, because it's ours.' Eight-year-olds in dependency cases are heard through counsel and the court's own care, and Zola's statement does what children's statements do at their best — it refuses to be anyone's exhibit and remains a person's wish list.

And the Riverton foster mother, when your counsel's investigator asks about her expectations, gives the answer that rearranges the hearing: "I took Zola as an emergency, thirty to sixty days. I'm a respite and emergency home. Nobody told me this was meant to be long-term." She is entitled to notice of the hearing and to be heard at it (42 Pa.C.S. § 6336.1). What she has to say serves Zola. It does not serve the move.

**Choices:**
- Prepare the review packet: the February notes, the two dates, the approved study, Zola's position, the foster mother's statement. → **zola_weekend**  _(FLAG: packetBuilt)_

## [zola_weekend] The test weekend

*Day 26 — Saturday, November 28, 2026*

Under the interim order, Zola spends a full weekend at Beatrice's before the review — the court testing the placement the way careful judges test all such placements: by letting it happen once, on paper, and reading the report. The report, filed by the agency's own visit supervisor, is three paragraphs of a child re-inhabiting her life: the binder toured, the bedroom claimed, the old school walked past 'to check it's still there,' and a Sunday collapse into sleep at 7 p.m., described by Beatrice as 'the tired of a kid who stopped holding her breath.'

Weekend reports like this are the hearing's advance guard: they convert December's question from 'whether' toward 'why not.'

**Choices:**
- Zola's own counsel files her position this week. The packet completes itself around her words. → **zola_counsel**

## [zola_counsel] Zola's position

*Day 27 — Sunday, November 29, 2026*

Zola's counsel files her position in the child's own priorities, translated but not improved: she likes the Riverton foster mother and wants to be able to say goodbye properly, 'not on a Thursday'; she wants her old school 'where the fish tank is not the best thing'; she wants Aunt Bea's house 'because it's ours and because Mom can walk there.' The filing also does counsel's sterner work: it opposes any further interim moves — 'this child has been transferred by adults' paperwork four times this year; the court's order should end the transfers, not schedule the next one.'

Four transfers. Counted by her lawyer, in a filing, where December must read it.

**Choices:**
- The Riverton foster mother's statement completes the voices. Then the packet closes. → **foster_statement55**  _(HIDDEN + child-voice)_

## [foster_statement55] The emergency home's statement

*Day 27 — Sunday, November 29, 2026*

The Riverton foster mother's written statement is short, professional, and — for the agency's theory — fatal in its kindness: she confirms she accepted Zola as a thirty-to-sixty-day emergency placement; that her home is 'structured for transition, not tenure'; that Zola 'speaks of her aunt's home as her address and of mine as her visit'; and that in her experience 'this child has a placement waiting, and it isn't mine.' She will attend the review and say it under her § 6336.1 right to be heard.

When the placement itself testifies that it was a bridge, a court needs a reason to make it a destination. The agency's position paper, arriving this week, will have to supply one.

**Choices:**
- Read the agency's paper when it lands — it is the last document before December 3rd. → **packet55**

## [packet55] December approaches

*Day 28 — Monday, November 30, 2026*

The agency's pre-review position paper holds its line with one crack in it: the move was necessary and lawful; the Riverton home is appropriate; 'kinship was explored.' Explored is doing heavy lifting in that sentence, and December 3rd is where sentences get weighed. Your counsel's final preparation is about posture: "We are not asking the court to punish anyone. We are asking it to place a child with her approved aunt, in her school district, in her county — and to notice that every document written since February points there."

Beatrice will be heard on her qualifications — as a potential kinship care resource she has that right under § 6336.1, and the court must then decide her notice and participation going forward. Her binder comes with her. Of course it does.

**Choices:**
- Go in with the binder, the two dates, and the study. → **agency_position_paper**

## [agency_position_paper] The position paper

*Day 29 — Tuesday, December 1, 2026*

The agency's pre-review position holds the necessity line and concedes, in a subordinate clause you have to read twice to believe, that 'kinship exploration in the first quarter was not completed to standard.' It opposes immediate return on stability grounds — the honest core of its case: Zola has now been in Riverton six weeks; a second move is also a disruption; the court should weigh the child's present attachments.

Your counsel marks the concession's page. 'They've given us February,' she says. 'Now they ask the court to forgive it for November's sake. Our answer is the weekend report and the school letter: the life she'd return to is not hypothetical. It's documented, enrolled, and has a chair kept in a circle.'

**Choices:**
- The night before the review: pack the binder, the log, the packet. Sleep like a litigant. → **night_before55**

## [night_before55] The night before

*Day 30 — Wednesday, December 2, 2026*

Beatrice lays out her binder's newest sub-label — 'ZOLA — REVIEW (DECEMBER)' — with the superstition of a nurse before a hard shift: clearances, study, care plan, the February pages copied and flagged. Your transport log is in your bag: nine round trips, four hundred ninety-five minutes each way's worth of a childhood in transit, itemized without a single adjective.

Zola, by phone, gives her final instruction: 'If the judge asks about the fish tank, tell her it was a good fish tank. I don't want her thinking I lied about that part.' Eight-year-olds understand credibility better than most litigants. Nothing in your packet lies about anything, including the fish tank. That is its power.

**Choices:**
- One call left: your counsel's final preparation, the morning of. → **pre_review_call55**

## [pre_review_call55] Posture

*Day 30 — Wednesday, December 2, 2026*

'Remember the posture,' your counsel says, on the courthouse steps call. 'We are not the prosecution of February. We are the family of December, with an approved aunt, a kept chair, a weekend report, and a file that corrects its own summary. The agency will ask the court to protect stability. We agree about stability. We simply brought evidence of where Zola's actually is.'

It is the whole batch in one instruction: the record, corrected and complete, argued without adjectives. Beatrice comes up the steps with the binder under her arm like a shield that has learned to be a book.

**Choices:**
- Go in. The binder, the two dates, the study, the child — in that order, the file walks into December. → **december_morning**

## [december_morning] December 3rd, the hallway

*Day 31 — Thursday, December 3, 2026*

The hallway outside the courtroom holds the case's entire cast in winter coats: Beatrice with the binder; Ms. Halvorsen with the file that now agrees with it; the Riverton foster mother, who drove fifty-five minutes — Zola's drive, reversed — to say four sentences in person; and you, with the transport log, whose arithmetic nobody will need to check because everybody in the hallway has lived it.

The judge's clerk opens the door. The file goes in first, the way files do. Then the family.

**Choices:**
- Hear the hearing run on documents — the February notes, the two dates, the approved aunt, the child's own words. → **review55**

## [review55] December 3rd

*Day 31 — Thursday, December 3, 2026*

The hearing runs on documents. The agency's worker is fair-minded and cornered by her own file: the February notes read aloud; the March silence; the October 20th memo; the October 29th entry. Beatrice is heard — qualifications, night shifts, the daughter ten minutes away, the binder produced once, to establish the February calls, and never flourished again. The Riverton foster mother, heard under § 6336.1, says her piece in four sentences and sits down.

The judge turns to the agency. "Counsel. Had the kinship study been run in March, or the aunt checked in the nine days before the move — where would this child be tonight?"

**Choices:**
- Listen. The answer to that question is the order. → **outcome55**

## [outcome55] Across the line

*Day 31 — Thursday, December 3, 2026*

The order depends on whether the court was shown a move that had to happen — or a kinship home that was never actually tried.

**Choices:**
- The packet was complete: the February record, the planned nine days, the approved aunt, the child's own position, and the emergency home's honest limits. → **end_backacrosstheline**  _(REQUIRES: recordRead; REQUIRES: studyApproved; REQUIRES: packetBuilt)_
- The court splits it: Zola stays in Riverton for stability now, with Beatrice approved and woven in — weekends, respite, school transport — and the placement relisted. → **end_bridge55**
- The move was defended as necessity and the kinship record never made it into evidence. → **end_fiftyminutes**

## [end_backacrosstheline] Ending — Back Across the Line

*Day 31 — Thursday, December 3, 2026*

**Ending.**

**Debrief:** Zola is placed with Beatrice, effective the following Monday, and re-enrolled in her old school, where her reading group has kept — her teacher confesses — her chair in the circle. The order recites the sequence that decided it: kin identified at intake; kin's own calls documented in the agency's notes; no completed kinship exploration before a move planned nine days in advance; an approved kinship home now available in the child's school district. The judge's phrasing for the county line is the one for the training manuals: the emergency justified a bed for a night; it did not justify a county for a childhood.

The method generalizes, because cross-county moves are where kinship goes to be forgotten: the record request (55 Pa. Code § 3130.44(d)) is the only instrument that reconstructs who knew what in February; dates do the arguing — a memo predating the emergency converts 'no choice' into 'unchosen option'; and the kin resource, resubmitted in un-losable form and heard on her qualifications (§ 6336.1), must be made a person in the present tense, not a February intention in the file's. Interim relief mattered too: the November order kept the visits and the school thread alive, so December's order restored a life instead of excavating one.

What no strategy controls: the bed map. Your county genuinely had no bed in October, and if Beatrice had failed her study — a record, a landlord, a daughter who moved away — the Riverton home would have been the right answer even on a perfect record. The strategy never promised Beatrice would pass. It promised she would be reached, studied, and answered in the open. In kinship work that promise, kept, is most of what 'family finding' is supposed to mean.

## [end_bridge55] Ending — A Bridge, Not a Move (partial)

*Day 38 — Thursday, December 10, 2026*

**Ending.**

**Debrief:** The court declines to move Zola mid-year: two school changes in five weeks, the judge rules, is its own harm — and instead builds the bridge with orders: Beatrice's approval finalized, Zola to spend weekends and school breaks at her aunt's, agency transport for your Wednesday visits restored, and the placement question relisted in ninety days with the kinship placement as the presumptive plan unless the agency shows cause. Zola keeps the Riverton foster mother she likes and gains back her aunt in writing, on a calendar.

Partial endings in move cases are often built this way — stability now, kinship scheduled — and whether this one is wisdom or delay will be decided by the ninety days, not by today. What the record bought is that the delay is the court's considered choice rather than the file's default drift: the February notes, the October dates, and Beatrice's approval are now findings-adjacent, and a relisted hearing inherits them. Drift loses cases slowly; documented bridges mostly finish crossing.

Walk the bridge deliberately: use every weekend, document every exchange, and let the ninety days produce the evidence the next order needs — a child thriving in both homes, with one of them hers by blood and law.

## [end_fiftyminutes] Ending — Fifty Minutes

*Day 38 — Thursday, December 10, 2026*

**Ending.**

**Debrief:** The move stands. The agency's necessity argument, unopposed by the February record, carries the day: an emergency, a licensed home, a kinship resource the file describes — still — as 'packet mailed, no response.' Beatrice, unstudied and unheard, remains a name in an intake form. Your visits remain fifty-five minutes away on the days the transport runs. Zola's chair in her old reading circle is given, in time, to another child.

Everything that decided this was paper that existed and was never introduced. The call notes proving Beatrice's February persistence were in the agency's file the whole time — a parent's written record request (§ 3130.44(d)) is the mechanism that moves such pages from the agency's drawer to the court's bench. The October dates were in the file too. Cases like this are not lost because the truth is unavailable; they are lost because truth held by one side, unread by the other, functions as though it did not exist.

The road from this ending is the scenario run in reverse and late: Beatrice's fresh submission (which no ruling here forecloses), the study, her right to be heard on her qualifications (§ 6336.1), and the next review — moves are revisited, and a completed kinship approval changes the question from 'should we explore' to 'why not yet.' Fifty minutes is a distance. It is not a verdict on your family, unless the file is allowed to make it one by default.
