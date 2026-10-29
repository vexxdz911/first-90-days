# THE FIRST 90 DAYS — Scenario 104: “Fifteen Months, From Inside”

*Human-readable script. This document and `scenario-104.json` are generated from a single source and match node-for-node: same IDs, same order, same choices, same effects.*

**The family is fictional — a composite. No real person's story appears here.**

**Content note:** This scenario depicts a permanency year played from inside a state correctional institution: letters, certificates, reviews, and the fifteen-month filing decision. There is no graphic content. Players may skip any scene or use the quick exit at any time.

**How to read effects:** `cash −40` changes the player's cash. `FLAG: name` sets a flag the engine tracks. `HIDDEN + item` means the case file quietly records that item at this choice — the player does not see it when it happens. `REQUIRES FLAG: name` means the choice is only available if that flag was set earlier; `REQUIRES NO FLAG: name` means it is only available if that flag was never set. `NOTE:` is text shown to the player right after choosing.

Start date: Monday, June 2, 2025. Day offsets are days since the scenario's start date (the child's foster-care entry date).

## [start] Day Zero, Written Down
*Day 0 — Monday, June 2, 2025 (dayOffset 0)*

Your name is Latrice Pettigrew. Your daughter Harlow is three. Today — Monday, June 2, 2025 — is the day Harlow entered foster care, and it is the day a federal clock starts that almost nobody will mention to you for months.

Harlow does not go to a stranger. She goes to her grandmother, Geraldine — your mother — whose house has the spare room, the yard, and the particular steadiness of a woman who has already raised one daughter and intends to see her raised out of this. You are serving a sentence in a state correctional institution. Your release is possible, but it is possible after a date this clock cares about. This story is played in the permanency year that follows — in letters, certificates, and copies.

**Choices:**
- Begin where the year is actually played — with the paper that has to travel → **first_letter**

## [first_letter] The First Letter
*Day 7 — Monday, June 9, 2025 (dayOffset 7)*

Your first letter to the agency is short, because you do not yet know what letters in this system are for. You think they are for saying you love Harlow, and you say it, truly, in every line.

Geraldine, visiting Harlow's new room into order, says the practical thing: "Love is assumed, baby. Write dates. Write what you did. Keep the copy." She has kept every paper anyone has ever given her, in a drawer that sticks. It is about to become the most important drawer in this case.

**Choices:**
- Take Geraldine's rule — dates, actions, copies, from now on → **letters_rule**

## [letters_rule] Geraldine's Drawer
*Day 15 — Tuesday, June 17, 2025 (dayOffset 15)*

Geraldine shows you — by photograph, on a call — the drawer: Harlow's placement papers on top, your first letter underneath, everything dated in pencil in the corner in her hand.

'Every paper that comes into this house about you two goes in here,' she says. 'And a copy of every paper that goes out. Drawers remember what people get tired of remembering.'

**Choices:**
- Continue → **clock_explained**

## [clock_explained] Ms. Thornbury Draws the Clock
*Day 30 — Wednesday, July 2, 2025 (dayOffset 30)*

Ms. Thornbury is your attorney. On a video call she draws it plainly: at fifteen of the most recent twenty-two months in foster care, the agency must file or join a termination petition — unless an exception is documented. (42 U.S.C. § 675(5)(E)) Harlow entered care on June 2, 2025. Fifteen calendar months later is Wednesday, September 2, 2026. That is the date everything in this story is aimed at.

"Three exceptions," she says. "A child cared for by a relative — Harlow is, if the file says so in so many words. A documented compelling reason. And services the agency was required to provide and did not. Exceptions are not hopes, Latrice. They are documents, filed before the date they answer. And if a petition is filed, understand this: a petition is not a termination. The agency would still have to prove its case by clear and convincing evidence. Our job is to make sure it never gets to decide on an empty file."

**Choices:**
- Ask what paper you can make from inside → **video_call_room**

## [video_call_room] The Video Call Room
*Day 38 — Thursday, July 10, 2025 (dayOffset 38)*

Calls and video visits from inside happen in a room built for noise — other families, other clocks, a guard's radio. You learn to speak in short, dated sentences anyway, the way your letters now read.

Ms. Thornbury's clock is on the legal pad she holds to the camera: entry, fifteen months, the review. You copy it onto the inside cover of your notebook, where you will see it every day for a year.

**Choices:**
- Continue → **institution_file**

## [institution_file] Two Filing Cabinets
*Day 45 — Thursday, July 17, 2025 (dayOffset 45)*

Here is the geography of your case. In the institution, there is a file: your program enrolments, your work assignment, your conduct record — a year of documented behaviour, kept by people who see you every day.

At the agency, there is another file, kept by Ms. Aubert, your caseworker. Between the two filing cabinets there is, at the start of this story, almost nothing: no bridge, no routine copy, no shared page. Your progress exists. It simply exists in the wrong building. Cases like yours are not usually lost on what a mother did. They are lost in the corridor between those two cabinets.

**Choices:**
- Ask Ms. Thornbury how paper crosses that corridor → **two_cabinets**

## [two_cabinets] Naming the Corridor
*Day 52 — Thursday, July 24, 2025 (dayOffset 52)*

You give the problem its working name in your notebook: the corridor. Everything in this year will be an attempt to carry one true page down it, and get a receipt.

Geraldine, characteristically, improves the plan: she will be the corridor's other end — collecting, copying, and hand-delivering what the post loses.

**Choices:**
- Continue → **records_request**

## [records_request] The Record Request
*Day 60 — Friday, August 1, 2025 (dayOffset 60)*

Step one, she says, is to see the agency's file as it stands — what it says about Harlow's placement, about you, about visits and services. Agency records are released on request: the material shall be released upon request. (55 Pa. Code § 3130.44(d)) A written request, from you through counsel, starts that.

It costs postage and patience. Without it, you will spend fifteen months answering a file you have never read — sending certificates into a cabinet whose contents are a rumour.

**Choices:**
- Send the written record request through counsel under § 3130.44(d) → **packet_arrives**  _(cash −5 ; FLAG: recordsRequested ; HIDDEN + Records — written request under 55 Pa. Code § 3130.44(d) sent from inside)_
- Save the effort — write your letters and trust the file to be fair → **packet_arrives**
  - NOTE (shown after choosing): Files are not fair or unfair. They are full or empty, in specific places.

## [packet_arrives] What the Agency File Holds
*Day 95 — Friday, September 5, 2025 (dayOffset 95)*

The record arrives through counsel, redacted and partial. Harlow is thriving with Geraldine — the file says so, in a worker's brief, kind lines. Visits are noted. Services for you are listed in the plan's tidy boxes.

What the file does not hold is you: no program record, no work record, no conduct record, no page that describes the mother Harlow will come back to — because no page describing her has ever been sent. The file's silence about Latrice Pettigrew is not hostility. It is logistics. Logistics, unanswered for fifteen months, hardens into a conclusion.

**Choices:**
- Start sending the institution's paper across — every certificate, twice → **harlow_preschool**

## [harlow_preschool] Harlow, in the File and Out of It
*Day 110 — Saturday, September 20, 2025 (dayOffset 110)*

The file says Harlow is 'settled and thriving.' Geraldine's letters say more: pre-school songs sung at full volume, a best friend, a fierce attachment to a red cup that must be located before any meal can legally begin.

Both accounts are true. You keep both — the file's version for the record, Geraldine's for the winter nights — and you learn not to confuse which one a court can use.

**Choices:**
- Continue → **certificates_first**

## [certificates_first] The First Certificate
*Day 120 — Tuesday, September 30, 2025 (dayOffset 120)*

You complete your first program inside — a certificate with your name spelled right, a date, and a seal that smudges if you touch it too soon. It is, institutionally, a small thing. In the agency file, if it ever gets there, it will be the first page that says what you did with this year.

Mail from inside is slow and sometimes simply lost. Geraldine's rule applies double here: copy everything, mail it twice — once to Ms. Aubert, once to Ms. Thornbury — and write down both dates.

**Choices:**
- Copy the certificate, mail it twice, and log both dates → **mail_room**  _(cash −5 ; FLAG: certificatesCopied ; HIDDEN + Institution progress — first certificate copied, mailed twice, dates logged)_
- Mail the original once to the agency and trust the post → **mail_room**
  - NOTE (shown after choosing): The original is the one copy the mail can lose completely.

## [mail_room] Mail, Twice
*Day 135 — Wednesday, October 15, 2025 (dayOffset 135)*

The mail room teaches you the year's arithmetic: one letter is a hope, two letters are a system. Everything is copied, everything is logged, everything is sent by two routes when it matters.

It costs time at the copier and favours owed to the woman who runs it. It is the cheapest insurance in this entire case, and nobody outside this room will ever know you bought it.

**Choices:**
- Continue → **quarterly_letter1**

## [quarterly_letter1] A Quarterly Letter, Written Like a Record
*Day 150 — Thursday, October 30, 2025 (dayOffset 150)*

Your quarterly letter to the agency changes its genre. It still says you love Harlow — one line, because it is true — and then it becomes a record: programs by name and date, work assignment, conduct standing, the visits that happened and the ones that were scheduled in ways the institution could not honour.

Geraldine reads her copy at the kitchen table and nods once. "Now it sounds like evidence," she says, "instead of a cry for help." Both were always in the letters. Only one of them files well.

**Choices:**
- Send the quarterly letter, copied, to the agency and to counsel → **geraldine_visit_day**

## [geraldine_visit_day] Geraldine at the Glass
*Day 165 — Friday, November 14, 2025 (dayOffset 165)*

Geraldine visits with Harlow's drawings and a list of her own: questions for Ms. Aubert, written down, with spaces left for the answers and the dates they were given.

'Your caseworker isn't the enemy, baby,' she says. 'She's a person with forty files. We are going to make ours the easiest one in the pile to say yes to — because everything in it is already written down.'

**Choices:**
- Continue → **kinship_statement**

## [kinship_statement] Geraldine's Statement
*Day 180 — Saturday, November 29, 2025 (dayOffset 180)*

The relative-placement exception is alive in this case from Day Zero — Harlow lives with her grandmother. But Ms. Thornbury is exact about the difference between a fact and a documented fact: "The file must say it, in a form the agency can cite when the filing decision is made. A statement from Geraldine — her name, Harlow's name, the placement, the date it began, her willingness to continue — signed and filed."

Geraldine writes it that Sunday, in her clear hand, and signs it twice because the first signature 'looked rushed.' Geraldine does not do rushed, on paper that matters.

**Choices:**
- Have Geraldine's signed kinship statement filed with the agency and the court → **phone_call_home**  _(cash −5 ; FLAG: kinshipStatement ; HIDDEN + Kinship — grandmother's signed statement of placement and willingness filed)_
- Let the placement speak for itself — everyone knows Harlow lives with her grandmother → **phone_call_home**
  - NOTE (shown after choosing): Everyone knows it. The filing decision will be made by people reading a file.

## [phone_call_home] The Phone Call
*Day 195 — Sunday, December 14, 2025 (dayOffset 195)*

On the phone, Harlow tells you about the red cup, a song, and Geraldine's garden, in that order of importance. She calls Geraldine's house 'home' once and your photograph 'Mama's picture' twice, and both of those are survivable because Geraldine reports them without flinching and without decoration.

Afterward you write the call into the log — date, length, Harlow well, routine unbroken. Even this goes in the folder. Especially this.

**Choices:**
- Continue → **visit_problem1**

## [visit_problem1] The Visit That Could Not Happen
*Day 210 — Monday, December 29, 2025 (dayOffset 210)*

A visit is scheduled — at a time, and then at a facility arrangement, that the institution cannot honour. It is cancelled. In the agency's notes, the week shows a blank where a visit should be. In your log, it shows a date, a scheduled time, and the institution's stated reason it could not proceed.

Cancelled visits have a way of being remembered by files as visits that did not happen, full stop — the reason evaporating, the blank remaining. Unless someone writes the reason down, in a letter, the same week.

**Choices:**
- Write the cancellation, its date, and its reason into your next letter the same week → **second_quarterly**  _(FLAG: servicesLog ; HIDDEN + Visits — cancelled visit logged same week with date and institutional reason)_
- Wait for the rescheduled visit — raising it feels like complaining → **second_quarterly**
  - NOTE (shown after choosing): No reschedule arrives on its own. The blank, meanwhile, is already filed.

## [second_quarterly] The Second Quarterly Letter
*Day 225 — Tuesday, January 13, 2026 (dayOffset 225)*

The second quarterly letter is easier to write and harder to read: a season of your daughter's life, summarised by its mother from another building, in dated bullet points about herself.

You send it anyway, twice, with the visit log attached. A record is not required to be cheerful. It is required to exist.

**Choices:**
- Continue → **work_record**

## [work_record] The Work Assignment Record
*Day 240 — Wednesday, January 28, 2026 (dayOffset 240)*

Your work assignment inside has its own paper: supervisor sign-offs, months of shifts completed, a record as boring and as valuable as any pay stub outside. Boring paper is the best paper. It has dates on it, and other people's signatures.

You request a copy of the work record through the institution's process, the way you have learned to request everything: in writing, with a copy kept.

**Choices:**
- Request the work record in writing and copy it for both cabinets → **institution_class**  _(cash −5 ; FLAG: institutionRecord ; HIDDEN + Institution — work assignment record requested in writing and copied)_
- Mention the work in your letters instead — the detail is in your head → **institution_class**
  - NOTE (shown after choosing): Detail in a letter is a claim. Detail on a signed record is a fact.

## [institution_class] The Class List
*Day 255 — Thursday, February 12, 2026 (dayOffset 255)*

You put your name on the list for the longer, plan-named program months before a place opens. The list itself is paper: your name, the date you signed, the date the place came — proof that the completion later was pursued, not stumbled into.

You copy the list page when you sign it. In this year, you copy everything. The corridor forgives nothing that travels in a single copy.

**Choices:**
- Continue → **conduct_record**

## [conduct_record] A Clear Conduct Record
*Day 270 — Friday, February 27, 2026 (dayOffset 270)*

A year of clear conduct inside is not a small thing, and it produces the smallest paper of all: a record with nothing adverse on it — page after page of ordinary days, no infractions, no findings.

Emptiness, documented, is evidence here. An empty conduct record that sits in the institution's cabinet proves nothing at the agency's table. The same empty record, copied and filed in both, becomes a sentence a lawyer can say out loud at a review: 'A clear record, for the entire period, and it is in the file.'

**Choices:**
- Copy the clear conduct record into both files, with a covering letter → **holiday_paper**  _(FLAG: conductRecord ; HIDDEN + Institution — clear conduct record copied to agency and counsel)_

## [holiday_paper] Paper at the Holidays
*Day 285 — Saturday, March 14, 2026 (dayOffset 285)*

The holidays inside are a season of other people's visits and a thin mail bag. Geraldine sends photographs — Harlow mid-song, Harlow asleep against her shoulder — and, with them, a dated note of Harlow's routine across the holiday weeks: unbroken.

You file the note's copy in your notebook and send your thanks as a letter, copied like everything else. Sentiment, in this family, now travels with a date on it.

**Choices:**
- Continue → **plan_mailed**

## [plan_mailed] The Plan That Came Back Unclaimed
*Day 300 — Sunday, March 29, 2026 (dayOffset 300)*

Geraldine tells you, on a call, something Ms. Aubert mentioned at her door: a copy of the case plan was mailed to the institution for your signature — and came back unclaimed, the envelope unopened, the plan unsigned. Nobody re-sent it. Nobody noted, beyond a line in a log, that the mother whose plan it was had never seen it.

An unsigned plan in a file can look, to a later reader, like a mother who did not engage with her plan. The truth — an envelope, a mail room, a return — is smaller and dumber and entirely documentable, if it is documented now.

**Choices:**
- Write, through counsel, asking for the plan to be re-sent and the returned envelope noted in the file → **review_prep_104**  _(cash −5 ; FLAG: planCorrected ; HIDDEN + Plan — returned-unclaimed mailing raised in writing; re-send requested)_
- Sign whatever version reaches you next and say nothing about the envelope → **review_prep_104**
  - NOTE (shown after choosing): The line in the log stays the file's only account of why the plan was unsigned.

## [review_prep_104] Preparing to Be Described
*Day 315 — Monday, April 13, 2026 (dayOffset 315)*

Before the mid-clock review, Ms. Thornbury rehearses you: 'They will describe Harlow for ten minutes and you for one sentence. Our job is not to lengthen the sentence with adjectives. It is to attach exhibits to it.'

You list the exhibits on the call — certificates, work, conduct, letters, logs — and she checks each against what the agency has acknowledged receiving. Two gaps are found, and re-sent that week.

**Choices:**
- Continue → **mid_review**

## [mid_review] A Review, Mid-Clock
*Day 330 — Tuesday, April 28, 2026 (dayOffset 330)*

At a permanency review you attend by video, Harlow's life with Geraldine is described warmly and in detail. Your life is described in one sentence: 'Mother remains incarcerated and is participating in services.' Participating. The word does the work of a filing cabinet that was never opened.

Ms. Thornbury does not argue with the sentence. She asks that the institution records already sent — certificates, work record, conduct record — be noted as received and filed. Paper, acknowledged on a record, stops being mail and becomes evidence.

**Choices:**
- Ask, through counsel, for the sent records to be noted as received and filed → **visit_problem2**  _(FLAG: quarterlyLetters ; HIDDEN + Review — institution records noted as received and filed at counsel's request)_

## [visit_problem2] The Second Impossible Visit
*Day 355 — Saturday, May 23, 2026 (dayOffset 355)*

It happens again, differently: a service session in the plan is scheduled in a way the institution's calendar cannot accommodate — offered, missed, and entered. Two such entries, unanswered, begin to compose a story in the file about a mother who does not attend.

Your log composes the other story, date by date: scheduled, impossible as scheduled, written objection sent, alternative requested. Ms. Thornbury reads both versions side by side and says, 'One of these is a pattern of a parent. The other is a pattern of a schedule. The file currently holds the first. We are going to make it hold the second.'

**Choices:**
- Log it, write it, and have counsel send the scheduling record to the agency → **harlow_birthday**  _(FLAG: servicesLog ; HIDDEN + Services — second impossible scheduling logged; written record sent through counsel)_
- Keep attending what you can and let the missed entries speak for themselves → **harlow_birthday**
  - NOTE (shown after choosing): Missed entries do speak. That is precisely the problem.

## [harlow_birthday] A Birthday, Documented
*Day 368 — Friday, June 5, 2026 (dayOffset 368)*

Harlow turns four at Geraldine's table, with a cake, the red cup, and a photograph that Geraldine mails twice — once to you, once to the folder.

Your birthday letter to the agency is mostly a record — Harlow well, placement stable, your program progressing on its named dates — with one line of birthday in it. Geraldine approves the ratio. 'One line is enough,' she says. 'She'll read the rest when she's grown, in the drawer.'

**Choices:**
- Continue → **geraline_health**

## [geraline_health] Geraldine's Knee
*Day 380 — Wednesday, June 17, 2026 (dayOffset 380)*

Geraldine's knee gives her a bad month, and for the first time the kinship arrangement shows its human fragility: a grandmother, a three-year-old, a staircase. A neighbour helps. Geraldine recovers, slowly, the way she does everything — completely, and without asking for credit.

She writes that down too, and the help she got, and that Harlow missed nothing — not a meal, not a story, not a day of pre-school routine. Kinship care is not a legal abstraction in this house. It is a grandmother with a bad knee who arranged cover before she sat down. The file should know the arrangement is cared for, not just present.

**Choices:**
- File Geraldine's short written update — the bad month, the help, Harlow's unbroken routine → **folder_audit**  _(FLAG: kinshipStatement ; HIDDEN + Kinship — caregiver update filed; support during illness documented)_

## [folder_audit] The Folder, Audited
*Day 395 — Thursday, July 2, 2026 (dayOffset 395)*

Geraldine spreads the folder on the kitchen table — her drawer, emptied for an audit — and you and Ms. Thornbury go through it on speakerphone, page by page, against the agency file's index.

It takes an evening. Two pages are missing from the agency's side and are re-copied and hand-delivered by Geraldine the next day, with a receipt. This is the quarter of the case nobody will ever dramatise, and it is the quarter the case is won in.

**Choices:**
- Continue → **program_complete**

## [program_complete] The Second Certificate
*Day 410 — Friday, July 17, 2026 (dayOffset 410)*

You complete the longer program — the one the plan named. The certificate is heavier paper, or it feels that way. Behind it, the folder Geraldine keeps now holds the year's whole architecture: certificates, work record, conduct record, quarterly letters, visit and scheduling logs, the kinship statement and its update.

Ms. Thornbury audits the folder against the agency file, line by line, on a call. 'This,' she says, 'is no longer a mother asking to be believed. This is a record asking to be read. Now we build the packet that makes them read it before September 2.'

**Choices:**
- Copy the second certificate twice, mail it twice, log both dates → **release_dates**  _(cash −5 ; FLAG: certificatesCopied ; HIDDEN + Institution progress — second, plan-named program completed; certificate mailed twice)_

## [release_dates] Release, Written as Dates
*Day 435 — Tuesday, August 11, 2026 (dayOffset 435)*

Your release is possible after September 2, 2026 — that fact does not change, and this scenario does not pretend otherwise. What can change is whether the plan treats release as a rumour or as a sequence: a possible release window, the steps after it, Geraldine's continuing role, Harlow's transition written as dates and stages rather than as a cliff edge.

A plan with dates in it gives a reviewer something to protect. A plan with a cliff in it gives a filing decision only one obvious direction. Ms. Thornbury drafts the sequence with you, line by dated line.

**Choices:**
- Build the post-release sequence — window, steps, Geraldine's role — as dated plan language → **packet_prep**  _(FLAG: releasePlan ; HIDDEN + Release — post-release reunification sequence drafted as dated plan language)_
- Leave release out of the packet — it is after the date, so it may not count → **packet_prep**
  - NOTE (shown after choosing): After the date is exactly where a permanency plan is supposed to look.

## [packet_prep] Assembling, Not Arguing
*Day 442 — Tuesday, August 18, 2026 (dayOffset 442)*

Packet preparation is assembly, not argument: statements in order, logs behind them, certificates behind those, every page dated, every claim in the covering letter pointing at a page beneath it.

Ms. Thornbury's rule for the covering letter: no sentence the packet cannot prove. The letter shrinks by a third under the rule, and gets stronger by exactly the same amount.

**Choices:**
- Continue → **exception_packet**

## [exception_packet] The Exception Packet
*Day 450 — Wednesday, August 26, 2026 (dayOffset 450)*

The packet Ms. Thornbury assembles is not long. That is its strength. One: Harlow is cared for by a relative — Geraldine's filed statement, the placement from June 2, 2025, the update. Two: a documented compelling reason, in the agency's own plan terms — a mother whose entire institutional record is in the file, whose release sequence is written as dates. Three: services the plan identified that were scheduled in ways the institution could not honour — the log, with dates, and the letters that answered each blank the week it appeared.

It must be filed before the fifteen-month review — filed, stamped, and in the agency's hands in time to be read, not carried in on the morning. Filing costs copies. Carrying it in costs the case.

**Choices:**
- File the documented-exception packet before the fifteen-month review → **fifteen_review**  _(cash −10 ; FLAG: exceptionPacket ; HIDDEN + ASFA — documented-exception packet filed before the fifteen-month review)_
- Bring the packet to the review and hand it up there → **fifteen_review**
  - NOTE (shown after choosing): Paper handed up on the day is paper the other side reads for the first time in public. It rarely gets read twice.
- Trust the facts to be obvious at the review without a packet → **goal_change_hearing**
  - NOTE (shown after choosing): Facts that live in two filing cabinets are obvious to no one in either building.

## [fifteen_review] The Fifteen-Month Review
*Day 457 — Wednesday, September 2, 2026 (dayOffset 457)*

Wednesday, September 2, 2026. Fifteen calendar months after Monday, June 2, 2025 — the date computed at the start of this story, arriving, as these dates do, on an ordinary weekday in a courtroom with a list of other families before and after yours.

The agency's filing duty is now live. (42 U.S.C. § 675(5)(E)) What the agency and the court do with it depends on what is in front of them: a file, and whatever was filed into it before today. You attend by video. Geraldine attends in person, Harlow's drawing folded in her bag. Ms. Thornbury rises.

**Choices:**
- Put the filed exception packet to the court — relative placement, documented compelling reason, services not provided as scheduled → **end_best**  _(REQUIRES FLAG: recordsRequested ; REQUIRES FLAG: exceptionPacket ; REQUIRES FLAG: kinshipStatement)_
  - NOTE (shown after choosing): This choice exists because the record was requested, the kinship statement was filed, and the packet was filed before today.
- Make the speech — fifteen months of love and effort, told from the heart by video → **end_petition**
- Ask the court to note that Geraldine has had Harlow all along, packet or no packet → **end_goal_change**  _(REQUIRES NO FLAG: exceptionPacket)_

## [goal_change_hearing] The Goal-Change Conversation
*Day 450 — Wednesday, August 26, 2026 (dayOffset 450)*

Without a filed packet, the review's weather changes earlier and more quietly: the agency speaks of Harlow's need for permanency, of a long placement becoming a long childhood, and the word 'goal' begins to move in the room — away from reunification, toward something the file's silence seems to support.

Ms. Thornbury argues what can be argued from letters and memory. It is a good argument. It is being made against a file, and files do not have to argue back. They just sit there, being the record.

**Choices:**
- Hear the court's direction → **end_goal_change**

## [end_best] Fifteen Months, From Inside
*Day 464 — Wednesday, September 9, 2026 (dayOffset 464)*

At the fifteen-month review, the exception packet is in the record — all three doors documented, the first of them open since the day Harlow went to her grandmother's house and now, finally, saying so in the file's own language. The agency does not file a petition. No petition is filed.

Harlow stays with Geraldine. That is not the end of the case, and this ending does not call it one. What is written into the plan, with dates, is what happens next: your possible release window, the steps after it in sequence, Geraldine's continuing place in Harlow's life through the transition, and a review date that answers to that sequence instead of to a cliff.

From inside, you hear the outcome the way you have heard everything this year — through a speaker, in a room with a clock. Geraldine cries, briefly, in the corridor, where Harlow cannot see. Then she goes home and writes the date in the drawer that sticks, on top of the folder that made it, because in this family paper is how love proves it was paying attention.

**Ending.**

**Debrief:**
- THE CLOCK, AUDITED — Harlow entered foster care on Monday, June 2, 2025 (Day 0). Fifteen calendar months later is Wednesday, September 2, 2026 — Day 457, the day of the fifteen-month review node, computed from the entry date and checked against the calendar. At fifteen of the most recent twenty-two months, the agency must file or join a termination petition unless an exception is documented (42 U.S.C. § 675(5)(E)). All three exceptions were documented here: relative placement (flag: kinshipStatement — Harlow cared for by her grandmother from Day 0, stated in a filed, signed statement); a documented compelling reason (the complete institutional record and dated release sequence, flags: institutionRecord, conductRecord, releasePlan); and services not provided as scheduled (flag: servicesLog — visits and plan services repeatedly scheduled in ways the institution could not honour, logged the week each occurred).
- THE PAPER, MAPPED — The route's engine was the corridor between two filing cabinets. The record request under 55 Pa. Code § 3130.44(d) (flag: recordsRequested) revealed the agency file's silence about Latrice; certificates copied and mailed twice (certificatesCopied), the work and conduct records (institutionRecord, conductRecord), quarterly letters written as records (quarterlyLetters), and counsel's filed exception packet (exceptionPacket) filled that silence before the date it answered. Counsel's role is as stated at 42 Pa.C.S. § 6337. No termination grounds are analysed here, and no termination outcome is depicted or predicted — this scenario ends, deliberately, at the filing decision. Had a petition been filed, the agency would still have had to prove its case by clear and convincing evidence at a separate hearing.
- This is a partial win, labelled honestly: Harlow is not reunified in this ending, Latrice is not released in this ending, and the plan's dated sequence still has to survive contact with release boards, housing, and time — none of which any strategy controls. Outcomes in this system also turn on workers, judges, resources, and luck. What the strategy controlled was narrower and, on September 2, 2026, decisive: when the filing decision was made, it was made about a record — not about an absence mistaken for one.

## [end_petition] The Petition, Filed on an Empty Drawer
*Day 464 — Wednesday, September 9, 2026 (dayOffset 464)*

The petition is filed. The speech was true — every word of it — and the file it was spoken into still did not hold the institution's paper: certificates that existed in one cabinet, a conduct record in another, a grandmother's care described everywhere except in a filed statement the decision-maker could cite.

A petition is not a termination, and Ms. Thornbury says so first, before anything else, because it is both true and important: the agency would still have to prove its case by clear and convincing evidence, in a separate proceeding this story does not enter. But the fight that now begins did not have to begin on this record. It begins here because fifteen months of documented progress lived in the wrong building, and the corridor between the buildings was never walked in time.

**Ending.**

**Debrief:**
- THE CLOCK, AUDITED — Entry: Monday, June 2, 2025. Fifteen months: Wednesday, September 2, 2026 (Day 457), the review at which the filing duty under 42 U.S.C. § 675(5)(E) became live. On this route the exception packet was not in the record in citable form (no exceptionPacket flag at the decisive choice, or the packet's foundations — recordsRequested, kinshipStatement — were missing), so no documented exception stood between the clock and the filing.
- THE PAPER, MAPPED — The institutional progress on this route was real and, in the agency file, absent: the pattern this scenario is built from — progress made inside a facility, filed nowhere the decision is made — is a documented system pattern, not a finding about any worker. The record request (55 Pa. Code § 3130.44(d)), the twice-mailed certificates, and Geraldine's signed statement are the bridges that were not built in time. Counsel (42 Pa.C.S. § 6337) argued from what existed; courts decide from what is filed.
- Outcomes in this system also turn on workers, judges, resources, and luck, and a filed petition is a beginning of a separate case — one in which the agency bears a clear-and-convincing burden — not a verdict on a mother, and not the end of this one. This ending measures a logistics failure with a human cost, which is exactly why the game makes you live the logistics.

## [end_goal_change] Goal Change on an Unbuilt Record
*Day 464 — Wednesday, September 9, 2026 (dayOffset 464)*

The goal is changed. The plan that had pointed, however slowly, toward Harlow coming home now points elsewhere — on a record that never received the kinship statement in filed form, never assembled the exceptions into a packet, and left the institution's year of documented progress in the institution.

Geraldine keeps Harlow, for now, in the house with the drawer that sticks — a drawer that, on this route, holds less than it should. Ms. Thornbury begins the next stage of work with the sentence she has used all year, now sadder and still true: 'Then we build the record for the next hearing. It will be a better record. It will also be a later one.'

**Ending.**

**Debrief:**
- THE CLOCK, AUDITED — Entry: Monday, June 2, 2025; fifteen-month date: Wednesday, September 2, 2026 (Day 457), under 42 U.S.C. § 675(5)(E). Harlow was, in fact, cared for by a relative for the entire period — the relative-placement exception existed as a fact on every route of this scenario. On this route it did not exist as a documented fact (no filed kinshipStatement relied on at the review, no exceptionPacket), and an exception that is only true, but not documented, does not answer a filing duty that is written in the word 'documented.'
- THE PAPER, MAPPED — Missing or late on this route: the written record request (55 Pa. Code § 3130.44(d)), the twice-copied institutional records, the same-week logs of impossible schedulings, and the pre-filed packet. None of those absences is a measure of Latrice's love or Geraldine's care, both of which the story states plainly and repeatedly. They are absences of paper at a decision that is made from paper.
- Outcomes in this system also turn on workers, judges, resources, and luck — a different reviewer, a caseworker who carried a certificate across the corridor herself, or a slower goal-change calendar could each have altered this ending, and none was in the player's control. A goal change is a direction set at a review, not a final judgment on a family; what this ending records is the cost of arriving at the permanency year with an unbuilt record, in the currency the system actually charges.
