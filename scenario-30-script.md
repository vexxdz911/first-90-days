# THE FIRST 90 DAYS — Scenario 30: “The Third Removal”

*Human-readable script. This document and `scenario-30.json` are generated from a single source and match node-for-node: same IDs, same order, same choices, same effects.*

**The family is fictional — a composite. No real person's story appears here.**

**Content note:** This scenario depicts a new child-welfare assessment on a family with closed prior cases, and — on one path — a removal sought on the strength of history and a shelter care hearing, told through procedure and paperwork. There is no graphic content. Players may skip any scene or use the quick exit at any time.

**How to read effects:** `cash −40` changes the player's cash. `FLAG: name` sets a flag the engine tracks. `HIDDEN + item` means the case file quietly records that item at this choice — the player does not see it when it happens. `NOTE:` is text shown to the player right after choosing.

Start date: Monday, September 14, 2026. Day offsets are days since the scenario's start date.

## [start] The Third Knock
*Day 0 — Monday, September 14, 2026 — Monday, September 14, 2026 (dayOffset 0)*

The knock is polite. They usually are, the worker says — Ms. Adeyemi, new to you — standing on your step with a folder that is thicker than this visit should need.

There is a new report, she says. The school referred your son Ben, nine: eleven absences this term, and a morning he told his teacher that “Mom sleeps in the day.” You work nights at the warehouse. You sleep in the day the way other parents sleep at night, with your neighbour Mrs. Lindt downstairs listening for the children after school. Nobody has alleged a bruise, an injury, or a mark of any kind. The report, in its own words, is about attendance and supervision.

Your children — Ben, and Lily, six — are at school. The folder on Ms. Adeyemi's arm holds two closed cases and a voluntary service period before it holds anything about this autumn. Everyone who reads it will meet your past before they meet your present. This scenario is about whether the present gets read at all.

**Choices:**
- Invite her in, and ask to start with this autumn — the report itself, first → **intake_call**
  - NOTE (shown after choosing): A reasonable order of reading. Whether the folder allows it is the story.

## [intake_call] What the Report Actually Says
*Day 2 — Wednesday, September 16, 2026 — Wednesday, September 16, 2026 (dayOffset 2)*

You read the referral summary at the kitchen table while Ms. Adeyemi waits, because you have learned — slowly, over years — to read before answering. Eleven absences. “Mother sleeps during the day.” No allegation about the children's health, food, or safety at home. Ben is, the school adds, “a pleasure, behind in reading.”

“And the rest of the folder?” you ask.

“Your history is part of the assessment,” she says, not unkindly. “It is standard to review it.” She does not say it is part of the evidence. You notice the difference, and you write her sentence down, dated, while she watches. She notices you writing it down.

**Choices:**
- Ask what happens next, and write that down too → **history_reads**  _(HIDDEN + New referral — 11 school absences; 'mother sleeps during the day'; no injury alleged)_
  - NOTE (shown after choosing): Dates on everything. You are starting the present-facts record already, without knowing its name.

## [history_reads] History, Read Aloud
*Day 4 — Friday, September 18, 2026 — Friday, September 18, 2026 (dayOffset 4)*

At the office two days later, a supervisor joins for the first part — “given the history,” she says, the way other people say “given the weather.” The history, read aloud, goes like this:

2018: a case opened around housing and supervision, services provided, case closed. 2021: a voluntary family-support period — you asked for it, after Lily was born — completed, period ended. 2023: a case opened after a report about the children's care during your shift change, assessed, case closed. Three episodes. All closed. The readings take nine minutes. This autumn takes, so far, one paragraph.

“So,” the supervisor says, “help us understand what's different now.” It is a fair question pointed in a strange direction: it asks you to prove the present is not the past.

**Choices:**
- Answer by building the present first — a dated account of this autumn, in writing → **present_choice**  _(HIDDEN + HISTORY entry read as current — 2018 housing case (closed); HIDDEN + HISTORY entry read as current — 2021 voluntary support period (ended); HIDDEN + HISTORY entry read as current — 2023 case (closed))_
  - NOTE (shown after choosing): The file's momentum is the other track in this case. It runs whether or not anyone pushes it.

## [present_choice] Then and Now, in Writing
*Day 7 — Monday, September 21, 2026 — Monday, September 21, 2026 (dayOffset 7)*

Ms. Ferreira — the lawyer you consult at the library clinic, the same calm reader of frightening paperwork — gives you the playable skill of this whole scenario in one sentence: “Separate THEN from NOW in writing, with dates and sources, so a reader can check each line against its own year.”

She sketches the shape. A short packet: the new report's actual words; this autumn's facts, each with a source (the school's own attendance printout, your shift schedule, Mrs. Lindt's letter, the lease at your current address); and a separate, clearly labelled history page that agrees with the file where the file is right — and says so.

“Agreeing where it's right,” she says, “is what makes the corrections believable where it isn't.” You do not know yet that there are corrections to make. You will.

**Choices:**
- Start the packet with this autumn, sourced and dated → **now_first**  _(FLAG: presentPacketStarted; HIDDEN + Present-facts packet begun — new report's words, this autumn only, sourced)_
  - NOTE (shown after choosing): Now, first. Then, labelled. That order is the argument.
- Answer their history questions fully and orally first — cooperation now, packet later → **history_path**
  - NOTE (shown after choosing): You cooperate completely. Cooperation, unrecorded by you, will be recorded by them — in their order, not yours.

## [now_first] Now, First
*Day 10 — Thursday, September 24, 2026 — Thursday, September 24, 2026 (dayOffset 10)*

The first page takes an evening. “September–October: Ben absent 11 days. Of these, the school's printout marks 7 excused with notes sent (ear infection, two; school closed, one; bus, four — route cancelled). Four unexcused: the mornings after your shift changed and the alarm arrangement failed; arrangement since changed (see Mrs. Lindt's letter).”

Every line has a year on it, and the year is this one. It reads, you realise, like a different genre from the folder: a report about a family, instead of a summary of a history.

Ms. Ferreira reads it and says the thing that opens the next door: “Now let's see whether their file's history page matches your memory of it. There's a way to look. There has always been a way to look.”

**Choices:**
- Learn how to look at your own file → **records_lesson**
  - NOTE (shown after choosing): The door from the flyers. It is the same door in every one of these stories.

## [history_path] Cooperation, Summarized
*Day 10 — Thursday, September 24, 2026 — Thursday, September 24, 2026 (dayOffset 10)*

You answer everything: the housing in 2018, the support period in 2021, the closed case in 2023. You answer accurately and in order, for an hour. The notes taken are not inaccurate. They are simply arranged past-first, so that this autumn arrives at the end of your own story, as a footnote to three closed episodes.

On the bus home, you understand the mechanic without anyone explaining it: a reader of those notes will feel they know this family before they reach the page about Ben's reading level and the cancelled bus route.

At the library clinic that Friday, Ms. Ferreira listens and says, “Cooperation was right. The order was the problem — and order can still be fixed, in writing. But first, let's look at the file itself. There's a way. There has always been a way.”

**Choices:**
- Learn how to look at your own file → **records_lesson**
  - NOTE (shown after choosing): What was said can be answered. What is written must be read.

## [records_lesson] Your Own File
*Day 14 — Monday, September 28, 2026 — Monday, September 28, 2026 (dayOffset 14)*

Separate from the new assessment, you may ask the county agency for your own case record — the prior files, the notes, the summaries, and the scored assessment material from then and now. Under the regulation, it “shall be released upon request” (55 Pa. Code § 3130.44(d)). Ms. Ferreira is specific: ask for the complete record, including the full scored assessment — the form, the item ratings, the outcome.

She adds the honest caution her profession owes you: at the adjudication stage there are disclosure rules for assessment and discovery material (Pa.R.J.C.P. 1340(B)(1)) — and whether Rule 1340 reaches every scored item of an assessment is untested. “We ask under the regulation we can quote,” she says. “We flag the rule we cannot. That is not weakness. That is accuracy.”

The request is one page. The stamp is one stamp. What comes back will tell you which parts of THEN are accurate, which are stale, and which were never true.

**Choices:**
- Write the request this week — the complete record, prior cases and the new assessment → **records_request**
  - NOTE (shown after choosing): Dated, copied, kept. You are about to become the only person in this case who has read the whole folder.
- Wait — building the present packet feels more urgent than reading the past → **records_request**
  - NOTE (shown after choosing): The packet matters. So does knowing what the packet will be read against.

## [records_request] The Request Goes In
*Day 17 — Thursday, October 1, 2026 — Thursday, October 1, 2026 (dayOffset 17)*

You file it on a Tuesday, between school drop-off and your shift. The clerk stamps your copy. Somewhere, a folder with your name on it acquires a new first page that you wrote.

Ms. Ferreira uses the waiting days well: the school prints Ben's attendance record for you (seven excused, as your page says — the source checks out); the warehouse confirms your shift schedule in a letter with a supervisor's signature; Mrs. Lindt writes her letter in pencil first, then in pen, because “pen is for true things.”

The packet of your records is due back within the agency's ordinary processing time. It arrives on a Saturday, in an envelope thick enough to change the weekend.

**Choices:**
- Request the record in writing and keep the stamped copy → **packet_arrives**  _(cash −10; FLAG: recordsRequested; HIDDEN + Record request — complete record incl. prior cases and scored assessment, form, ratings, outcome)_
  - NOTE (shown after choosing): The stamped copy goes in your folder, first page. Everything after this is checked reading.
- Ask for the record by phone instead, to save the trip → **thin_file**
  - NOTE (shown after choosing): A phone request leaves no stamped copy, no date you can prove, and — this month — no packet.

## [packet_arrives] Reading the Whole Folder
*Day 22 — Tuesday, October 6, 2026 — Tuesday, October 6, 2026 (dayOffset 22)*

It is partly blacked out, and still: there it all is. 2018, as you remember it — housing, services, closed. 2023, as you remember it — assessed, closed. The summaries are fairer than you feared, and you write that down too, because the corrections you are about to make will be believed in proportion to the agreements around them.

And then, in the 2021 voluntary period summary — the period you asked for, and completed — one line stops your eye the way a step that isn't there stops a foot:

“Mother declined parenting support sessions (2021).” You did not decline them. You attended them, on Thursdays, with Lily in a carrier. You have a completion certificate in a drawer, with a gold-ish seal.

**Choices:**
- Keep reading — check the addresses and the household lines before you decide anything → **stale_line**  _(HIDDEN + File line found — 'Mother declined parenting support sessions (2021)')_
  - NOTE (shown after choosing): One wrong line is a mistake. A pattern of wrong lines is a correction. Keep reading.

## [thin_file] What a Phone Request Gets
*Day 22 — Tuesday, October 6, 2026 — Tuesday, October 6, 2026 (dayOffset 22)*

The phone request is noted somewhere, by someone, as “mother inquired re: records.” No packet arrives. Ms. Ferreira is gentle and blunt in equal measure: “Then we work with what we can get another way — the school's records, your own papers — and we make the request again, in writing, because the regulation's promise follows the request, and a request we cannot prove is a request we cannot follow up.”

You make it again, in writing, the following week. It costs you ten days the written request would not have. When the packet arrives, your eye goes — the way Ms. Ferreira said it would — to the 2021 summary, and stops.

“Mother declined parenting support sessions (2021).” You attended those sessions on Thursdays, with Lily in a carrier. The certificate is in a drawer, with a gold-ish seal.

**Choices:**
- Check the rest of the folder before deciding anything → **stale_line**  _(FLAG: recordsRequested; HIDDEN + File line found — 'Mother declined parenting support sessions (2021)' (after a written re-request))_
  - NOTE (shown after choosing): Late paper, again: worth less than on-time paper, worth far more than none.

## [stale_line] Stale, Wrong, and Never True
*Day 25 — Friday, October 9, 2026 — Friday, October 9, 2026 (dayOffset 25)*

By Sunday you have three lists, in three colours of pen, the way Ms. Ferreira taught you. ACCURATE: the 2018 housing case and its closure; the 2023 assessment and its closure; the dates of the voluntary period. STALE: the file's current address is Elm Street — you moved two years ago; the “current household” line still lists a cousin who stayed for six weeks in 2021. And NEVER TRUE: the declined-sessions line — contradicted by the certificate in your drawer — and a household line naming a “partner, D.,” a person who has never lived in any home of yours.

Stale is not sinister. Files age the way milk does, by standing still while life moves. Never-true is different, and rarer, and — documented calmly, with a certificate — correctable.

Correction, though, is a move with a fork in it.

**Choices:**
- Decide how the corrections reach the file → **correction_choice**  _(HIDDEN + STALE — file address is two years old; household lists a cousin who left in 2021; HIDDEN + NEVER TRUE — 'declined sessions' contradicted by completion certificate; 'partner D.' never lived in the home)_
  - NOTE (shown after choosing): Three lists, three colours. You now know more about your file than anyone deciding from it.

## [correction_choice] How a Correction Travels
*Day 28 — Monday, October 12, 2026 — Monday, October 12, 2026 (dayOffset 28)*

Ms. Ferreira: “A correction told to a person enters that person's memory. A correction filed in writing, with its source attached, enters the file — attached to the line it corrects, where the next reader cannot miss the pairing.”

The written version is short. “Re: 2021 summary, line 4. The attached completion certificate (Thursdays, March–June 2021) shows the sessions were attended and completed; the word ‘declined’ appears to be in error. Re: address — current lease attached; Elm Street ended [two years ago]. Re: household — no person ‘D.’ has resided in this home; see lease and school forms.” Dated. Signed. Sources clipped behind it like evidence behind an argument.

It takes an evening and a bus ride. The telling would take four minutes. That difference is the whole lesson of this scenario, and you already know it.

**Choices:**
- File the written correction, certificate and lease attached, and keep the stamped copy → **correction_filed**  _(cash −12; FLAG: correctionFiled; HIDDEN + Written correction filed — certificate and lease attached, paired to the lines corrected)_
  - NOTE (shown after choosing): Stamped, copied, clipped to its sources. The next reader meets the correction with the error, together.
- Tell Ms. Adeyemi the corrections in your next call — she is reasonable, and she will note them → **verbal_correction**
  - NOTE (shown after choosing): She is reasonable. Her note of your call will be a summary. You have seen what summaries do.

## [correction_filed] Filed, With Sources
*Day 31 — Thursday, October 15, 2026 — Thursday, October 15, 2026 (dayOffset 31)*

Your correction goes into the file — not over the old lines (files do not erase; they accumulate, which is their virtue and their menace) but attached to them. A reader now gets the declined-sessions line and the certificate in the same eyeful. Stale address, current lease, same eyeful.

Ms. Adeyemi, to her credit, confirms in an email that the correction has been added and the address updated. You print the email. Of course you print the email.

What remains is the present packet itself — the autumn, finished and sourced — and one home visit still to come, where NOW will either be examined or be narrated by THEN.

**Choices:**
- Finish the present-facts packet → **present_packet**
  - NOTE (shown after choosing): Now the autumn gets its final, checkable form.

## [verbal_correction] Told, and Noted
*Day 31 — Thursday, October 15, 2026 — Thursday, October 15, 2026 (dayOffset 31)*

Ms. Adeyemi listens, believes you — you can hear that she does — and notes the call. Her note, when you later see it in a summary of the assessment, reads: “Mother disputes a 2021 entry.” Disputes. The certificate stayed in your drawer. The gold-ish seal impressed no one, because no one saw it.

“A dispute is a claim,” Ms. Ferreira says. “A filed correction with a source is a fact with a paperclip. We can still file it — late helps less than on-time, and more than never.” You file it that week. It enters the file after the assessment draft, instead of before it. Order, again: not a detail, but the mechanism.

What remains is the present packet — and a home visit where NOW will be examined beside a file whose wrongest line now wears the word “disputed” instead of a certificate.

**Choices:**
- Finish the present-facts packet → **present_packet**  _(FLAG: correctionFiled)_
  - NOTE (shown after choosing): Filed late, sourced, real. The packet will have to carry weight the correction should have carried.

## [present_packet] The Present-Facts Packet
*Day 35 — Monday, October 19, 2026 — Monday, October 19, 2026 (dayOffset 35)*

The finished packet is nine pages, and every page is boring in the way true things are boring. Page one: the new report's actual words. Page two: the attendance printout, excused and unexcused marked by the school's own hand, and what changed after the unexcused mornings. Page three: your shift letter. Page four: Mrs. Lindt's letter. Page five: the lease, current address. Page six: the children's health card — check-ups current. Pages seven to nine: the history, in your words, agreeing with the file where it is right, citing your filed correction where it is not, every episode labelled with its year and its ending: closed, ended, closed.

Ms. Ferreira reads it twice. “This is not an argument that nothing ever happened,” she says. “It is an argument that what happened has dates. That is much stronger.”

One choice remains before the home visit: whether another reader checks the packet first.

**Choices:**
- Decide who reads the packet before the visit → **help_choice**
  - NOTE (shown after choosing): Nine pages, three years separated from one autumn. Presentation is now the variable.

## [help_choice] A Second Reader
*Day 38 — Thursday, October 22, 2026 — Thursday, October 22, 2026 (dayOffset 38)*

Ms. Ferreira can review the packet at the clinic on Friday — line by line, the way she read your frightening letter in another story's world — if you can get there between drop-off and shift. The school family worker, too, has offered to confirm the attendance page against the school's system, so the packet's most important page arrives pre-checked by its own source.

Or you can send it as it is. It is accurate. Accuracy, you have learned, and presentation are cousins, not twins.

**Choices:**
- Take the packet to the clinic and the school first — checked, confirmed, then submitted → **packet_checked**  _(cash −15; FLAG: packetChecked; HIDDEN + Packet reviewed by counsel; attendance page confirmed by the school against its own system)_
  - NOTE (shown after choosing): A Friday spent like money. The packet now carries other people's signatures beside yours.
- Send the packet as it is — it is accurate, and time is not free → **packet_solo**
  - NOTE (shown after choosing): Accurate, unaccompanied. Its readers will check it — or trust the folder instead. That is the gamble, stated plainly.

## [packet_checked] Checked and Confirmed
*Day 41 — Sunday, October 25, 2026 — Sunday, October 25, 2026 (dayOffset 41)*

The clinic review changes eleven words and one order: the history pages move behind the autumn pages, so a reader meets NOW first even inside your own document. The school confirms the attendance page with a stamp of its own. “Seven excused is the school's number now,” Ms. Ferreira says, “not your claim. Numbers with owners are heavier.”

You submit the packet formally — to the worker, the supervisor, and your own folder — with a one-line cover note: “Present facts, sourced; history at pages 7–9; correction filed separately.” Dated, of course.

The home visit is set for Tuesday. It will be the first time anyone deciding this case has stood in the present-tense home with the present-tense packet already read.

**Choices:**
- Prepare for the home visit → **assessment_visit**
  - NOTE (shown after choosing): You have changed the order of reading. The visit will show whether it changed the reading.

## [packet_solo] Sent As It Is
*Day 41 — Sunday, October 25, 2026 — Sunday, October 25, 2026 (dayOffset 41)*

The packet goes in — to the worker's email, with the cover note you drafted: present facts first, history at the back, correction filed. No clinic stamps ride on it. Its numbers are yours, offered honestly, awaiting a checker who may or may not come.

The home visit is set for Tuesday anyway. Visits do not wait for verification. Ms. Adeyemi will stand in your kitchen holding two documents: a folder whose first nine minutes are history, and a packet whose first page is this autumn. Which one she reads from, in the room, is the scene you are walking into.

**Choices:**
- Prepare for the home visit → **assessment_visit**
  - NOTE (shown after choosing): Your facts are in the room. So is the folder. The visit is a contest of reading order, held in a kitchen.

## [assessment_visit] The Visit, in the Present Tense
*Day 48 — Sunday, November 1, 2026 — Sunday, November 1, 2026 (dayOffset 48)*

Tuesday, 4 p.m. The home is the home: school bags by the door, a reading book with a cracked spine, dinner at the stage of dinner that looks like a decision is still being made. Ben shows Ms. Adeyemi his reading chart without being asked. Lily shows her a drawing of the house, with the correct number of people in it — a detail you notice, and say nothing about, and remember.

Ms. Adeyemi asks about the mornings. You walk her through the packet's page two in the room it describes: the alarm, the shift change, Mrs. Lindt's knock since October. She checks the lease address against the door she came through. It matches. It is a small moment. Files live on small moments, matched or unmatched.

What she writes will be compared — by a supervisor, and possibly one day by a court — against both documents. And hidden in her form, as in every one of these stories, are the history entries, still sitting there, readable as current by anyone in a hurry.

**Choices:**
- Ask, before she leaves, that the visit note record what was seen today, dated today → **visit_record**  _(HIDDEN + Home visit (today) — attendance arrangement shown; lease address matched the home visited)_
  - NOTE (shown after choosing): A request for the present to be dated as the present. It sounds small. It is the scenario.

## [visit_record] What the Visit Note Says
*Day 51 — Wednesday, November 4, 2026 — Wednesday, November 4, 2026 (dayOffset 51)*

Her note, when the summary reaches you, is two paragraphs. The first is today: the home, the children, the arrangement, the reading chart. The second begins “Historically…” — and in that word, historically, the whole contest of this case is contained. What follows it is accurate, dated, and closed. It does not say “currently.” Three closed episodes have finally been written in the past tense.

That did not happen by itself. It happened page by page: a record read, a line corrected with a certificate, an autumn documented by its own sources, a visit that matched its packet.

A supervisor review is next. Reviews are where reading order becomes decision.

**Choices:**
- Go to the supervisor review → **supervisor_review**
  - NOTE (shown after choosing): The past is in the past tense. Whether the decision follows the grammar is the remaining question.

## [supervisor_review] The Supervisor Review
*Day 55 — Sunday, November 8, 2026 — Sunday, November 8, 2026 (dayOffset 55)*

You are not in the room for the review, which is ordinary, and which your lawyer prepares you for without varnish. “Two files will be on that table,” Ms. Ferreira says. “The folder, opening in 2018. And your packet, opening this autumn, with a correction clipped inside the folder itself. The decision will be made by a person who has read one of them first.”

She lays out the remaining fork with her usual plainness. How the packet travels from here — formally submitted with its cover note already acknowledged, or carried informally by the worker's summary — determines which file is the working file.

And she names the stake in the scenario's own title: if the history carries the day, the agency may seek a third removal — not on a new injury, for there is none, but on the strength of THEN read as NOW. That is what “The Third Removal” means here. It has not happened. Whether it is sought is the next scene.

**Choices:**
- Decide how the packet travels to the decision → **decision_fork**
  - NOTE (shown after choosing): Form is not decoration in this system. Form is the road facts travel on.

## [decision_fork] How Facts Travel
*Day 59 — Thursday, November 12, 2026 — Thursday, November 12, 2026 (dayOffset 59)*

The formal road: your packet is already submitted, acknowledged, stamped into the record; Ms. Ferreira sends a one-page letter adopting it as your account, so the decision-maker must either use it or explain around it. The informal road: everything you built exists, but it travels as the worker's summary of it — three lines, past-first, the way any family's words travel once they are summarized.

You have spent this whole scenario learning what summaries do. Choose with that knowledge, and with your eyes open about cost: the formal road takes one more evening and one more stamp.

**Choices:**
- Send it formally — the letter, the packet, the acknowledgment kept → **formal_submit**  _(FLAG: formallySubmitted; HIDDEN + Packet formally submitted and acknowledged as the parent's account)_
  - NOTE (shown after choosing): One more evening. The working file at the review will now open in the present tense.
- Let it travel with the worker's summary — she is fair, and you are tired → **informal_path**
  - NOTE (shown after choosing): She is fair. Summaries are still summaries. Tired is real, and the system prices it anyway.

## [formal_submit] The Working File Opens in Autumn
*Day 62 — Sunday, November 15, 2026 — Sunday, November 15, 2026 (dayOffset 62)*

The acknowledgment comes back in two days: packet received, letter received, filed. Ms. Ferreira allows herself one dry sentence: “Your history is now an appendix. Appendices get read last and believed in proportion to their sources — which is where closed cases belong.”

The decision meeting is set. Three outcomes are genuinely live in that room, and which one emerges will turn on the order in which a small group of tired professionals read two stacks of paper about the same family — plus the thing no packet controls, which is who is in the room and what their last case was like.

You wait the way parents in these stories wait: at work, at the school gate, with a phone that stays face-up.

**Choices:**
- Go to the decision → **outcome_prep**
  - NOTE (shown after choosing): Everything you could put on paper is on paper, in order, with sources. The rest is the room.

## [informal_path] Three Lines, Travelling
*Day 62 — Sunday, November 15, 2026 — Sunday, November 15, 2026 (dayOffset 62)*

The worker's summary of your packet is fair, and three lines long: “Mother provided documentation re: attendance and supervision; mother disputes a 2021 entry; family has an extensive history of involvement (2018, 2021, 2023).” All true. The packet's nine sourced pages have become a claim (“provided documentation”), its correction a posture (“disputes”), and its autumn a sentence that ends, as your story began, with the history.

Ms. Ferreira does not say I-told-you-so; she is not built that way. She says, “The decision meeting will now decide which document is the case. We attend, we speak, we ask that the packet itself be read. Sometimes the asking works, in the room, late. Sometimes the room has already read.”

The decision meeting is set. The stake, if the folder carries the room, is the one she named: removal sought on the strength of history.

**Choices:**
- Go to the decision → **outcome_prep**  _(HIDDEN + Worker's summary of packet — 'mother disputes a 2021 entry; extensive history (2018, 2021, 2023)')_
  - NOTE (shown after choosing): You bring the packet itself, all nine pages, to a room that may have already decided from three lines.

## [outcome_prep] The Decision Meeting
*Day 65 — Wednesday, November 18, 2026 — Wednesday, November 18, 2026 (dayOffset 65)*

The meeting room has the tissues-in-the-middle table you are beginning to recognise as this system's furniture. The supervisor has both stacks. The worker has her form. Your lawyer has your folder, which — for the first time in this family's long acquaintance with folders — is as thick as theirs, and better ordered.

The supervisor opens the discussion. What she opens with will tell you which file is the case.

**Choices:**
- Hear the decision framed on the present facts — the packet read first → **closing_review**
  - NOTE (shown after choosing): Autumn first: the report's words, the school's numbers, today's home.
- Hear the decision framed on the history — the folder read first → **petition_path**
  - NOTE (shown after choosing): 2018 first: three closed episodes, arriving in the room ahead of the autumn they were supposed to follow.

## [closing_review] Deciding on the Present Facts
*Day 68 — Saturday, November 21, 2026 — Saturday, November 21, 2026 (dayOffset 68)*

The supervisor reads the referral's actual words aloud — attendance, supervision, no injury — and then the school's confirmed numbers, and then the visit note's present-tense paragraph. The history is discussed last and briefly, the way appendices are: real, dated, closed.

“The question before us,” she says, “is what this family needs now, on these facts.” Your lawyer says nothing for a full minute, because nothing needs saying; the packet is saying it, in order, with signatures.

What remains is the form of the ending: closed outright, closed with a voluntary period — offered, this time, as a choice with paper — or closed while the file quietly keeps one thing you fought. Listen for which.

**Choices:**
- Accept closure on the present facts, and confirm it in writing → **end_closed**
  - NOTE (shown after choosing): Closed on NOW. The letter, when it comes, will say so — because you will read it, and keep it.
- Accept a short voluntary support period — in writing, with its end date on its face → **end_voluntary**
  - NOTE (shown after choosing): Services again — but this time as a written, dated choice, not a momentum.
- Close the case — and let the file's remaining lines be a fight for another day → **end_split**
  - NOTE (shown after choosing): Closure now, correction unfinished. Some families take that trade with open eyes. Know that you are taking it.

## [petition_path] Removal Sought on the Strength of History
*Day 68 — Saturday, November 21, 2026 — Saturday, November 21, 2026 (dayOffset 68)*

The supervisor reads the folder first. By the time this autumn is reached — three closed episodes in — the room's picture of your family was formed in 2018 and has been merely updated since. The attendance numbers are described as “a pattern.” The correction is described as “a dispute.” The word “extensive” does the work that evidence does in other rooms.

The agency's decision: to seek removal of Ben and Lily, and a hearing. Your lawyer is on her feet in the procedural sense — calm, immediate, specific. “Then the hearing will test exactly one thing,” she says, for the record. “Whether NOW was ever examined.”

Removal, if the court grants the agency's request for temporary custody pending that hearing, starts a clock that does not negotiate: a shelter care hearing within 72 hours. The date will be computed, not estimated. It always is.

**Choices:**
- Face the removal request and the clock it starts → **removal_day**
  - NOTE (shown after choosing): The threat in this scenario's title is no longer a threat. It is a date being calculated.

## [removal_day] The Third Removal
*Day 71 — Tuesday, November 24, 2026 — Tuesday, November 24, 2026 (dayOffset 71)*

The order is granted on an emergency basis — temporary custody, pending the hearing — on the papers, which is to say on the folder. Ben goes to a foster home two streets away with his school bag and his reading book. Lily goes with him; keeping siblings together is the one sentence in the order you are grateful for, and gratitude and grief share the room without either leaving.

There is no scene of force and no villain. There is a car, a kind driver, a worker who looks at the floor, and your children being brave in the specific way children are brave when adults have run out of procedure.

The notice in your hand gives the hearing date. Count it: the removal is today, and the shelter care hearing is three days from today — within 72 hours, as the law requires (42 Pa.C.S. § 6332; 23 Pa.C.S. § 6315(d)). Your lawyer circles it. “Three days,” she says. “We will spend them putting NOW in front of a judge, in order, with sources. Bring the packet. Bring the certificate. Bring the stamped copies.”

**Choices:**
- Go to the shelter care hearing — three days later, no sooner, no later → **shelter_hearing**  _(FLAG: removed; HIDDEN + Removal (in-story, emergency temporary custody) — shelter care clock started: hearing in 3 days / 72 hours)_
  - NOTE (shown after choosing): The clock is the law's, the packet is yours. Both arrive on the same morning.

## [shelter_hearing] The Shelter Care Hearing
*Day 74 — Friday, November 27, 2026 — Friday, November 27, 2026 (dayOffset 74)*

Three days. The courtroom is small. The agency's case is presented first, and it is, in substance, the folder: 2018, 2021, 2023, the word “pattern,” the word “extensive,” a summary of a summary of your autumn.

Then your lawyer does the thing this scenario exists to teach. She walks the judge through the packet by its dates. The report's actual words — no injury alleged. The school's own confirmed numbers — seven excused. The visit note's first paragraph — this home, this month. The correction, with its certificate, clipped to the line it corrects. “Your Honour,” she says, “the agency's evidence is a history. We ask the court to require what the burden requires: clear and convincing evidence about these children, now.”

The judge reads. The room waits the way rooms wait when reading, not summarising, is finally happening.

**Choices:**
- Let the judge finish reading the packet itself → **end_hearing**
  - NOTE (shown after choosing): Whatever she decides, she will decide it from the documents — all of them, in order, at last.
- Add your own voice, briefly — this autumn, in your own words, then stop → **end_hearing**  _(HIDDEN + Parent's testimony at shelter care hearing — this autumn, in her own words)_
  - NOTE (shown after choosing): Brief, dated, present-tense. Then you stop, and let the paper carry it.

## [end_closed] Ending — Closed on the Facts of Now
*Day 78 — Tuesday, December 1, 2026 — Tuesday, December 1, 2026 (dayOffset 78)*

**Ending.**

**Debrief:**
- WHAT THE FILE HELD (the hidden record, revealed): Three history entries that arrived dressed as current facts — a 2018 housing case, a 2021 voluntary period, a 2023 case, all closed — and, inside them, a stale address, a cousin listed two years after she left, a partner who never existed in the home, and one never-true line, “declined parenting support sessions,” contradicted by a completion certificate with a gold-ish seal. The new report itself alleged no injury: eleven absences, seven of them excused by the school's own record, and a night-shift mother's daytime sleep, supervised by a neighbour whose letter was in the packet.
- WHAT THE CLOCKS AND THE PAPER DID: The record request — the record “shall be released upon request” (55 Pa. Code § 3130.44(d)), including the full scored assessment, form, item ratings and outcome — surfaced the stale line while there was still time to correct it. The written correction, filed with its sources, travelled with the error. The present-facts packet, checked by counsel and confirmed by the school, changed the order of reading: the decision was made on this autumn, and the history was read last, as an appendix, in the past tense. Counsel's role rests on 42 Pa.C.S. § 6337 (counsel, and appointed counsel if unaffordable). Disclosure at the adjudication stage is governed by Pa.R.J.C.P. 1340(B)(1); its application to every scored assessment item is untested, as stated in-game. Dependency decisions require clear and convincing evidence — a burden that, in this ending, had to be carried about the present, and on the present facts it was not.
- WHAT REMAINS OPEN: The file still exists, corrected lines and all — files accumulate; they do not erase. A future report would be read by a future worker, and the correction you filed is the reason that reader would meet the error and its certificate together. That is not a small thing. It is, in this scenario, the thing.
- THE HONEST PART: The same packet, read by a different supervisor after a different last case, could have carried this family to the hearing ending; parents reach that ending with strong paper and this ending with thin paper, and the line runs through rooms, workloads, and luck. Workers, supervisors, judges, and chance held pieces of this outcome. What your choices changed was what there was to read, and in what order — which, in a system that decides from files, is most of what a parent can ever change.

## [end_voluntary] Ending — Services Again, on Paper
*Day 78 — Tuesday, December 1, 2026 — Tuesday, December 1, 2026 (dayOffset 78)*

**Ending.**

**Debrief:**
- WHAT THE FILE HELD: The same hidden history as every path — three closed episodes read as momentum, a stale address, a never-true “declined” line — answered, this time, by a filed correction with its certificate, a sourced present-facts packet, and a visit note written in the present tense. The agency's decision reflects both stacks of paper: not confident enough in NOW to close the file outright, not willing — on a present-tense record — to pretend THEN was evidence about this autumn.
- THE TERMS ARE THE ENDING: A short voluntary support period, accepted by you, in writing, with services named, a review date stated, and an end date on its face. That is a different instrument from the momentum that opened this story. Voluntary means you chose it; written means its promises bind the offeror as well as you; dated means it ends. Read it before signing, keep the copy, and let the period's own paperwork — attendance, again, but this time yours to file — become the record.
- THE LAW UNDER THIS PATH: The record on request, including the scored assessment (55 Pa. Code § 3130.44(d)); counsel (42 Pa.C.S. § 6337); adjudication-phase disclosure (Pa.R.J.C.P. 1340(B)(1)), untested as to every scored assessment item; and the clear-and-convincing burden for dependency decisions — never reached here, because no petition was filed, which is itself information about what the present-facts record did. This scenario asserts no deadline or rule for voluntary services beyond what is written on the agreement you sign; read the paper, because the paper is the rule you agreed to.
- THE HONEST PART: Some parents experience any services, however written, as a loss — and some supervisors offer them as a face-saving middle that a different room would have skipped for outright closure. Both readings can be true. Workers, rooms, and luck held pieces of this. What your paper changed is the shape of the middle: chosen, sourced, and ending on a date — a period that will close on paper the way your 2021 period should have been recorded as doing.

## [end_split] Ending — Closed, but the Stale Line Stays
*Day 78 — Tuesday, December 1, 2026 — Tuesday, December 1, 2026 (dayOffset 78)*

**Ending.**

**Debrief:**
- WHAT THE FILE HELD: Everything the winning paths held — and one thing more, or rather one thing less corrected. The case is closed on the present facts. Ben is behind in reading and catching up; Lily's drawing of the house hangs on the fridge. And in the closed file, a line survives uncorrected in its working form — in this ending, the summary still says you “disputed” a 2021 entry, the stale household line still stands in at least one copy of the record, and the certificate remains where it has always been: in your drawer, believed by everyone who saw it and filed by no one.
- WHY THIS IS A PARTIAL LOSS, STATED PLAINLY: Closure is real, and this debrief does not take it from you. But files outlive cases. A future report — a new school, a new worker, a new autumn — would be read against this file, and that reader would meet the stale line without its correction, and the whole work of this scenario would need doing again, faster, under worse conditions. The quiet losses in this system are rarely events. They are lines that stay.
- THE LAW UNDER THIS PATH: The tools remain what they were: the record on request (55 Pa. Code § 3130.44(d)) — which is how the line was found, and how, on a future request, its survival could be found again; counsel (42 Pa.C.S. § 6337); disclosure under Pa.R.J.C.P. 1340(B)(1), untested as to scored assessment items; the clear-and-convincing burden for any future dependency decision. A correction can still be filed after closure; this scenario does not invent a deadline for it, and does not claim one — it says only what the story showed: on-time paper outperforms late paper, and filed paper outperforms a certificate in a drawer.
- THE HONEST PART: Families take this trade for good reasons — exhaustion is a reason, and so is a child's need for an ordinary autumn — and no debrief written by anyone who has not carried the folder should call it failure. Workers, supervisors, timing, and luck divide this ending from the full closure along lines no strategy fully controls. What is true is narrower: the case is closed, the children are home, the present was finally read as the present — and one line of the past is still in there, misdated, waiting. Paper is patient. That was always the whole problem, and the whole opportunity.

## [end_hearing] Ending — Removal Sought, and the Hearing Tests Now
*Day 77 — Monday, November 30, 2026 — Monday, November 30, 2026 (dayOffset 77)*

**Ending.**

**Debrief:**
- WHAT THE FILE HELD: The folder, read first, did what this scenario warned it would: three closed episodes supplied the momentum, the present arrived as a “pattern,” a filed-or-unfiled correction was heard as a “dispute,” and removal was sought — and granted on an emergency basis — on the strength of history. No new injury was ever alleged. That sentence is in the agency's own referral, and in the end it was the packet, not rhetoric, that put it in front of a judge.
- WHAT THE HEARING DID: The shelter care hearing was held within 72 hours of the removal — three days, computed from the removal date — as the law requires (42 Pa.C.S. § 6332; 23 Pa.C.S. § 6315(d)). At it, the court heard the history in full and then, page by dated page, required the present to be examined: the report's actual words, the school's confirmed numbers (seven of eleven absences excused), the present-tense visit note, the certificate clipped to the line it corrects. On that record the court did not find the clear-and-convincing showing a dependency decision requires to keep the children removed on these facts, and ordered them returned home with the assessment closed to further action on this report — while noting, as courts do, that the file, corrected lines included, remains the file. Whether the next stage goes the same way depends, as it always does, on what is in front of the next judge.
- THE LAW UNDER THIS PATH: Shelter care within 72 hours (42 Pa.C.S. § 6332; 23 Pa.C.S. § 6315(d)); counsel (42 Pa.C.S. § 6337); the record on request, including the scored assessment (55 Pa. Code § 3130.44(d)) — the move that surfaced the stale line in time for it to matter in a courtroom; adjudication-phase disclosure (Pa.R.J.C.P. 1340(B)(1)), untested as to every scored item; and the clear-and-convincing burden for dependency decisions, which in this ending had to be carried about NOW, and was not.
- THE HONEST PART: A hearing is a human weighing, and a different judge, reading the same two stacks in a different order after a different morning, could have continued the removal and set the family on a far longer road — parents reach that version with every piece of paper in this packet, and this debrief will not pretend otherwise. Workers, judges, courtroom minutes, and luck held pieces of this outcome. What the paper changed was the question the hearing had to answer — from “what does the history suggest” to “what, exactly, has been shown about this autumn.” Getting that question asked, in time, under a 72-hour clock, was the playable skill — and the three days between a removal and its hearing are why the packet had to exist before anyone knocked.
