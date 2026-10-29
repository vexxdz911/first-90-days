# THE FIRST 90 DAYS — Scenario 75: “Two Experts, One Child”

*Human-readable script. This document and `scenario-75.json` are generated from a single source and match node-for-node: same IDs, same order, same choices, same effects.*

**The family is fictional — a composite. No real person's story appears here.**

**Content note:** This scenario depicts a permanency review hearing built around a psychological evaluation. There is no graphic content. Players may skip any scene or use the quick exit at any time.

**How to read effects:** `cash −40` changes the player's cash. `FLAG: name` sets a flag the engine tracks. `HIDDEN + item` means the case file quietly records that item at this choice — the player does not see it when it happens. `REQUIRES FLAG: name` means the choice is only available if that flag was set earlier; `REQUIRES NO FLAG: name` means it is only available if that flag was never set. `NOTE:` is text shown to the player right after choosing.

Start date: Monday, November 16, 2026. Day offsets are days since the scenario's start date.

## [start] The Word in the Packet
*Day 0 — Monday, November 16, 2026 (dayOffset 0)*

Your name is Vernon Quill. Your daughter Paloma is six. She has been placed with a foster family since Monday, March 16, 2026 — placed after the spring you do not make excuses for anymore: the DUI, the adjudication, the court taking the case the way courts do when a parent is drinking and driving with his life coming apart in the passenger seat.

That was then. You finished treatment. You have been sober eight months — meetings, screens, a sponsor who answers on the second ring. Paloma's permanency review is set for Wednesday, December 2, 2026, and today the court packet arrives: the agency's report, the plan update, and, near the back, an evaluation.

One word in it stops you the way a step missing in a staircase stops you. Dr. Marsh, a psychologist, evaluated your bond with Paloma and concluded it is "attenuated." Return home, the evaluation says, is "not recommended."

**Choices:**
- Read the evaluation again, slowly, pencil in hand → **packet_detail**
  - NOTE (shown after choosing): Second readings are where reports stop being verdicts and start being documents — with authors, dates, and page counts.
- Call your lawyer before you read another line → **packet_detail**
  - NOTE (shown after choosing): She answers on the fourth ring. "Bring the packet Thursday," she says. "All of it. Especially the parts that scare you."

## [packet_detail] Two Forty-Five-Minute Visits
*Day 0 — Monday, November 16, 2026 (dayOffset 0)*

The pencil finds the method section, because there is one, and it is short. Dr. Marsh observed you and Paloma together twice — two sessions, forty-five minutes each, in a visit room at the agency office. Ninety minutes, total, on two afternoons in October. The rest of the evaluation is a review of records: the agency file, the spring's reports, the history.

Nowhere in it does Dr. Marsh describe watching Paloma with her foster parents, for comparison. Nowhere does it mention Ms. Ferro — the therapist who has seen Paloma every week for fourteen months — except as a name in a list of providers. And the records it leans on hardest are the oldest ones in the file: the ones from before treatment, before the eight months.

Ninety minutes and a stale file produced a word — attenuated — that is now sitting in a court packet like a stone in a shoe. The question this scenario asks is not whether the word is fair. It is whether the word gets examined, or just repeated.

**Choices:**
- Write your questions in the margin: how long, compared to what, based on which records → **counsel_meet**
  - NOTE (shown after choosing): Three questions. They look small in pencil. In a courtroom, asked at the right moment, they are the whole case.
- Take a photograph of the conclusion page for your sister, then put the packet in your folder → **counsel_meet**
  - NOTE (shown after choosing): Your sister texts back one line: "Attenuated is an adjective, Vernon. Not a sentence." She is righter than she knows.

## [counsel_meet] An Opinion Is an Input
*Day 3 — Thursday, November 19, 2026 (dayOffset 3)*

Your lawyer, Ms. Voss, reads the evaluation the way she reads everything: method first, conclusion last. "Understand what this is," she says. "An expert opinion is an input. It has a method, and the method can be examined. No rule requires a formal bonding evaluation at all — the agency chose to get one, and now it has to stand behind how it was made."

"And understand what the hearing is. At a permanency hearing the court — not Dr. Marsh, not the agency — has to determine the continuing necessity of placement, your compliance with the permanency plan, your progress toward alleviating the circumstances that caused placement, and whether reasonable efforts were made to finalize the plan. (42 Pa.C.S. § 6351(f)(1), (2), (3), (5.1)) Those findings belong to the judge, on all the evidence. The people who see Paloma every week are witnesses too. A therapist of fourteen months is not a footnote to a psychologist of ninety minutes — unless we let the packet arrange it that way."

"So the next two weeks are about arrangement. First: we cannot cross-examine a report we have only read once, in a packet, the week it landed. We need the evaluation's whole file — her notes, her scoring sheets, everything under the conclusion. There is a way to ask for that, and it starts today, not at the hearing."

**Choices:**
- Ask her to show you exactly what to request, and how → **request_choice**
  - NOTE (shown after choosing): "In writing," she says. "Everything in this case that matters will turn out to have been in writing."

## [request_choice] Ask for the Whole File
*Day 3 — Thursday, November 19, 2026 (dayOffset 3)*

Ms. Voss drafts it on her letterhead while you watch: a written request for the complete agency record — and, named separately so it cannot be overlooked, the complete evaluation file: Dr. Marsh's raw session notes, her scoring sheets, and the list of records she reviewed. The agency's record "shall be released upon request" (55 Pa. Code § 3130.44(d)), and the rule is not to be read to protect agency employees' privacy as a basis for withholding (55 Pa. Code § 3130.44(f)).

She is plain about the alternative. At disposition, the law states the principle outright: written reports may be examined and controverted, and the people who made them may be cross-examined. (42 Pa.C.S. § 6341(d)(2)) A permanency review runs on the same paper logic — but only for a report whose maker can actually be questioned, which means only for a report you have actually read, down to the notes. Getting the file costs copying and postage. Not getting it costs the cross-examination.

The envelope is addressed. The hearing is thirteen days away. Envelopes, unlike hearings, can move today.

**Choices:**
- Send the written request today — full agency record plus the complete evaluation file, named item by item → **request_filed**  _(cash −20 ; FLAG: recordsRequested)_
  - NOTE (shown after choosing): Stamped, copied, dated. Whatever Dr. Marsh wrote in that visit room, in her own hand, is now on its way to being read by the person it describes.
- Ask the caseworker informally to pass the evaluation along when she gets a chance → **request_skipped**
  - NOTE (shown after choosing): She says she'll look into it, kindly, in a hallway. Hallway requests have no date on them, and this case runs on dates.

## [request_filed] The Request, in Writing
*Day 3 — Thursday, November 19, 2026 (dayOffset 3)*

The request goes out with a certificate of mailing, and Ms. Voss calendars the response the way other people calendar birthdays. "If the notes exist," she says, "they will say what she actually saw, in the room, before the conclusion was workshopped into an adjective. Notes are written for the file. Conclusions are written for the reader. I want the file version."

You go home and do the unglamorous arithmetic of the next two weeks: visits on Saturdays, meetings on Tuesdays and Fridays, work in between, and a hearing at the end of it that will be decided — Ms. Voss has now said it three ways — by what is in the record when the judge opens it.

**Choices:**
- Keep the week's ordinary machinery running — visits, meetings, work — while the file travels → **waiting_week**
  - NOTE (shown after choosing): Sobriety at eight months is mostly this: ordinary machinery, maintained, on days when nobody is watching. The file will note that too.

## [request_skipped] The Packet Is What You Have
*Day 3 — Thursday, November 19, 2026 (dayOffset 3)*

The caseworker is pleasant about it. Of course, she'll see what can be shared; the evaluation is in the packet, after all — you've seen the conclusion, haven't you? What you have seen, you realize on the drive home, is four pages: a summary, a method paragraph, and a recommendation. Whatever Dr. Marsh's own notes say about those two afternoons — what Paloma actually did in that room — is in a file you have now asked about, out loud, to a person who wrote nothing down.

Ms. Voss does not scold you. She just moves the word "attenuated" to the top of her legal pad and underlines it once. "Then we prepare against the four pages," she says, "and we hope the notes, if we ever see them, agree with them."

**Choices:**
- Keep the week's ordinary machinery running — visits, meetings, work → **waiting_week**
  - NOTE (shown after choosing): The visits still happen. The logs still get written. Some of the record is being made whether you requested the rest of it or not.

## [waiting_week] Visits, Meetings, Ordinary Days
*Day 6 — Sunday, November 22, 2026 (dayOffset 6)*

Saturday's visit: Paloma teaches you a card game she is inventing as she goes, with rules that favor her, and you let them. Ms. T., the visit supervisor, sits where she always sits, kind and quiet, writing in the logbook she keeps for every visit. Thirty visits since spring, give or take. Thirty entries.

Sunday, Ms. Voss calls — not about the file, which hasn't arrived, but about December 2. "Dr. Marsh will testify," she says. "Agency counsel will walk her through her conclusion. Then it will be my turn, and my turn is only as good as its preparation. There are two ways to spend this week. I can build the cross-examination now — a one-page method memo, every question sourced to a page — or we can plan to lean on Ms. Ferro's letter and improvise the rest. Improvisation is what the other side is counting on."

**Choices:**
- Spend the week building the one-page method memo with Ms. Voss — question by question, page by page → **memo_choice**
  - NOTE (shown after choosing): A cross-examination is not an argument. It is a staircase, built in advance, that a witness walks down one fact at a time.

## [memo_choice] Build the Cross Before You Need It
*Day 6 — Sunday, November 22, 2026 (dayOffset 6)*

The memo practically writes its own outline from the method section: How many minutes did you observe, Doctor? Ninety. Did you observe Paloma with her foster parents, for comparison? You did not. Which records did you review — and do the heaviest ones predate Mr. Quill's treatment? They do. What have you never seen? The last five months of visits.

Building it properly costs you an unpaid afternoon at Ms. Voss's office and the patience to read the packet a fourth time. The alternative is real, and many parents choose it: Ms. Ferro has already written a warm, thorough letter. Letters, though, cannot be asked follow-up questions, and neither can they ask any. A memo can do the asking — if it exists before the witness is sworn, not during.

**Choices:**
- Build the method memo — every question tied to a page, the staircase built in advance → **memo_built**  _(cash −15 ; FLAG: crossReady)_
  - NOTE (shown after choosing): One page. Four questions, each with a document under it. Ms. Voss puts it in the hearing folder, on top.
- Rely on Ms. Ferro's letter and the strength of your progress — save the afternoon → **memo_skipped**
  - NOTE (shown after choosing): The letter is genuinely good. It will sit in the packet being genuinely good at whatever reader picks it up. It will not cross-examine anyone.

## [memo_built] Ninety Minutes, on One Page
*Day 6 — Sunday, November 22, 2026 (dayOffset 6)*

The memo is done by dark. It does not call Dr. Marsh unqualified — she is qualified, and the memo is careful never to pretend otherwise, because judges can smell a credential fight and it bores them. It goes after the only soft thing in the evaluation: its method. Ninety minutes. No comparison observation. Records that end where your sobriety begins. Five months of visits, unseen.

"If her file ever reaches us," Ms. Voss says, tapping the last line of the memo, "there may be a fifth question. Her own notes. Witnesses are hardest to argue with when the argument is their own handwriting."

**Choices:**
- Go home and wait for Wednesday — the file, if it is coming, is due → **notes_day**
  - NOTE (shown after choosing): Waiting is also a strategy, when the mailbox is doing the work.

## [memo_skipped] The Letter Will Have to Do
*Day 6 — Sunday, November 22, 2026 (dayOffset 6)*

Ms. Voss reads Ms. Ferro's letter once more and sets it down gently. "Fourteen months of work, summarized by the person who did it, in two pages. A judge can read this in ninety seconds — which, you'll notice, is the same unit of attention Dr. Marsh gave your daughter's bond. The difference is that Ms. Ferro earned her summary."

"We'll offer the letter and argue from your progress," she says. "But hear me: when agency counsel says 'attenuated' for the fourth time, the letter will not stand up and answer. Paper doesn't interrupt. Only a prepared lawyer, or a live witness, does that."

**Choices:**
- Go home and wait for Wednesday — whatever the mailbox holds → **notes_day**
  - NOTE (shown after choosing): The week moves the way weeks in this case move: at the speed of other people's offices.

## [notes_day] Day Nine: What the Envelope Holds
*Day 9 — Wednesday, November 25, 2026 (dayOffset 9)*

Wednesday. Ms. Voss calls you into her office for the last full working day before the holiday, and what is on her desk depends — as so much in this case depends — on a decision made on day 3, in an envelope, for the price of postage.

If the written request went out, the agency's production has arrived: the full record, and inside it, clipped together, the evaluation file — Dr. Marsh's raw session notes and scoring sheets, the pages under the conclusion. If it didn't, her desk holds the same four packet pages you have already read, and a caseworker's hallway assurance, still unwritten, still warm, still useless.

**Choices:**
- Open the evaluation file and read Dr. Marsh's own session notes, line by line, with Ms. Voss → **notes_read**  _(HIDDEN + File — evaluation raw notes released on written request (§ 3130.44(d)): 'sought father's lap repeatedly' ; REQUIRES FLAG: recordsRequested)_
  - NOTE (shown after choosing): Her handwriting is small and unhurried. What it says is about to change the temperature of December 2.
- There are no notes to open — prepare from the four pages you have → **notes_absent**  _(REQUIRES NO FLAG: recordsRequested)_
  - NOTE (shown after choosing): You cannot miss what you never saw. That is precisely the problem, and it has a date on it: day 3, an envelope, unsent.

## [notes_read] 'Sought Father's Lap Repeatedly'
*Day 9 — Wednesday, November 25, 2026 (dayOffset 9)*

Session one, in Dr. Marsh's own hand: "Child sought father's lap repeatedly. Proximity-seeking consistent throughout." Session two: "Separation protest strong at session end; child asked when father returns." The scoring sheets tally their items. And then the conclusion, four pages later, in type: attenuated.

Ms. Voss sits back. "Her observations and her adjective are in tension," she says. "That happens in evaluations more often than anyone admits — the notes are written in the room, and the conclusion is written for the referral question, weeks later, out of a file that mostly predates your treatment. A judge should get to hear both. Now the judge can — because on December 2, I can hand Dr. Marsh her own notes and ask her to read the lap line out loud."

She adds a fifth question to the folder. "This," she says, "is what a records request is for. Not the paper. The tension inside the paper."

**Choices:**
- Turn to the other witness decision — Ms. Ferro, and whether she will be in the room → **therapist_choice**
  - NOTE (shown after choosing): One witness's notes are now evidence. The other witness is still a scheduling question with a deadline of today.

## [notes_absent] Reading a Report With No Notes Under It
*Day 9 — Wednesday, November 25, 2026 (dayOffset 9)*

You read the conclusion a fifth time. It does not change. Conclusions never do — that is what notes are for, and the notes are in a file across town, unrequested in any form the agency had to answer.

"For all we know," Ms. Voss says, "her session notes describe a warm, attached child, and the conclusion was assembled from the old file. For all we know, they describe exactly what she concluded. We will go into a hearing about your bond with your daughter not knowing what the only person who watched you together, in a professional capacity, wrote down while she watched. Sit with whose choice that was. It wasn't hers."

She is not cruel about it. She is a lawyer marking the exact size of a hole, because on December 2 she will have to argue around it.

**Choices:**
- Turn to the other witness decision — Ms. Ferro, and whether she will be in the room → **therapist_choice**
  - NOTE (shown after choosing): Whatever else is missing, this one is still makable. Today is the last day it is.

## [therapist_choice] A Witness or a Letter
*Day 9 — Wednesday, November 25, 2026 (dayOffset 9)*

Ms. Ferro has treated Paloma for fourteen months — weekly sessions, the slow repair work of a six-year-old learning that her father went away to get well and kept his promise to come back to the visiting room. She knows things about this family that exist nowhere else: what Paloma says about you when you are not there, in the third person, to the dollhouse.

She has already written her letter. But Ms. Voss is blunt: "A letter is a summary a judge skims. Testimony is a person the judge watches being questioned — and surviving it. Ms. Ferro will come and testify live if she is asked properly, with her session records subpoenaed so she can speak from them. But therapists arrange their Wednesdays weeks out. She has to be asked by today, or she is not there, and on December 2 the letter testifies alone." The subpoena and record copies cost money. The asking costs a phone call made on time.

**Choices:**
- Ask today — Ms. Voss confirms Ms. Ferro's live appearance and subpoenas her session records → **therapist_confirmed**  _(cash −35 ; FLAG: therapistLive)_
  - NOTE (shown after choosing): Fourteen months of Thursdays, sworn, in the room, where the judge can watch her answer questions. That is a different object than two pages in a packet.
- Let the letter speak for her — she wrote it carefully, and the packet already has it → **therapist_letter_sent**
  - NOTE (shown after choosing): The letter will be in the judge's packet. Whether it will be in the judge's mind at the moment of decision is a question letters cannot answer.

## [therapist_confirmed] Ms. Ferro Will Be There
*Day 9 — Wednesday, November 25, 2026 (dayOffset 9)*

Ms. Ferro agrees on the phone, in the tone of a person who has been waiting to be asked correctly. Her records will be certified and brought with her. "Tell Mr. Quill," she says, "that I will answer whatever they ask me. Including the hard questions. Especially the hard questions — the work holds up under them. That's rather the point of the work."

Ms. Voss writes her name on the witness list in ink. "Now December 2 has a shape," she says. "Their ninety minutes, crossed. Our fourteen months, live. And the visit logs, if we handle Saturday right."

**Choices:**
- Go to Saturday's visit — the last one before the hearing → **visit_day**
  - NOTE (shown after choosing): Thirty visits of logbook have been written by somebody else's hand. Saturday, you finally pay attention to the logbook itself.

## [therapist_letter_sent] Two Pages, Signed
*Day 9 — Wednesday, November 25, 2026 (dayOffset 9)*

The letter goes into the packet: two pages, careful, warm, specific about the repair work and Paloma's words. Ms. Voss reads it a final time and files it without complaint. "It says everything right," she says. "It just says it at the speed of reading, to a judge with a stack of packets, and it cannot raise its hand when agency counsel misquotes it."

"If the judge asks me why the treating therapist isn't here," she adds, "I will say she was not called. Judges notice who a side didn't call. They notice it in the direction you'd expect."

**Choices:**
- Go to Saturday's visit — the last one before the hearing → **visit_day**
  - NOTE (shown after choosing): One record is still being written in real time, in a logbook, by a neutral hand. Saturday matters more than it looks.

## [visit_day] The Visit Room, Saturday
*Day 12 — Saturday, November 28, 2026 (dayOffset 12)*

Paloma arrives at the visit room door at a run — she does this, Ms. T. mentions, every week; it is in the logs — and the hour unspools the way the good hours do: the invented card game, a drawing of a house with two doors "so nobody gets locked out of coming back," the goodbye that she has learned to do in stages, like landings.

Afterward, in the hallway, you finally ask Ms. T. about the logbook. Thirty visits, each one logged by the supervisor who sat in the corner: arrivals, departures, and the small behaviors in between — who Paloma ran to, how she settled, how she left. It is the longest continuous record of your bond with your daughter that exists. It was never an evaluation. It was never trying to be. That may be exactly why a judge would trust it.

**Choices:**
- Ask Ms. Voss what can be done with thirty visits of logs before Wednesday → **visit_summary_choice**
  - NOTE (shown after choosing): "Filed, summarized, and offered," she says. "Or left sitting in a file the judge may never open. Guess which version exists at a hearing."

## [visit_summary_choice] Thirty Visits, in a Logbook
*Day 12 — Saturday, November 28, 2026 (dayOffset 12)*

The logs are in the released agency record. Ms. Voss can prepare a short written summary — thirty visits, dates, Paloma's approach behavior at the door, the settling, the goodbyes — and file it through counsel as an exhibit for the review, so the judge meets the pattern on paper before anyone argues about it. Copying and filing cost a little money and an afternoon.

Or the logs can stay where they are: accurate, complete, and functionally invisible, one more true thing in a thick file that no one is obliged to read aloud. Hearings run on what is offered. Files run on what is in them. The two systems overlap less than anyone outside a courtroom believes.

**Choices:**
- File the written summary of the supervisor's logs through counsel, as an exhibit for the review → **visit_filed**  _(cash −10 ; FLAG: visitRecordFiled ; HIDDEN + Exhibit — visit supervisor logs: 30 visits, child's approach behavior documented)_
  - NOTE (shown after choosing): Thirty Saturdays, condensed by the person whose job was only to watch. It goes into the judge's packet with a tab on it.
- Leave the logs in the file — if they matter, the judge will find them → **visit_unfiled**
  - NOTE (shown after choosing): Judges find what is handed to them, cited to them, and argued to them. The rest is furniture in a room they walk through quickly.

## [visit_filed] The Logs, Filed as an Exhibit
*Day 12 — Saturday, November 28, 2026 (dayOffset 12)*

The summary is four pages and almost aggressively plain: dates in a column, behaviors in another, no adjectives of its own anywhere. Thirty visits. Zero missed. A six-year-old's running start, documented by a neutral witness who was never asked to have an opinion about it.

"Notice the difference in kind," Ms. Voss says. "Dr. Marsh offers a conclusion about the bond. This offers the bond, in installments, with dates. Courts are allowed to prefer evidence to conclusions. Let's give this one the chance."

**Choices:**
- Turn to the last paper problem — the scored summary in the court packet → **scored_summary**
  - NOTE (shown after choosing): One document in the packet has been quietly quoting Dr. Marsh all along, without naming her.

## [visit_unfiled] In the File, Unfiled
*Day 12 — Saturday, November 28, 2026 (dayOffset 12)*

The logbook closes on Saturday's entry and goes back into the file. Everything in it is true. Almost none of it, Ms. Voss warns, will be in the courtroom in any usable form — a judge cannot credit a pattern nobody put in front of her, and agency counsel is under no obligation to summarize the other side's best evidence.

"If I mention the logs in argument," she says, "the judge will ask where they are. 'In the agency's file, Your Honor' is an answer. It is not a good one. It sounds like what it is: a thing we knew about and did not bring."

**Choices:**
- Turn to the last paper problem — the scored summary in the court packet → **scored_summary**
  - NOTE (shown after choosing): The packet still has one more quiet mechanism in it, and it has been working since day 0.

## [scored_summary] The Adjective Travels
*Day 12 — Saturday, November 28, 2026 (dayOffset 12)*

The last document in the court packet is the scored summary — a scored assessment form, filled in by the agency, that sorts Paloma's case into items and scores. On the line about the parental bond, it does not describe anything anyone observed. It imports a word: attenuated. Dr. Marsh's conclusion, copied into the agency's own form, where it now sits wearing the agency's authority instead of hers.

This is how conclusions travel in this system: an expert writes an adjective, a form absorbs it, a report cites the form, and by the time a judge reads it, the word has three institutional voices and no visible author. Nobody lied at any step. The steps are the problem.

Ms. Voss turns the summary over. "There's an argument for answering this in writing before the hearing — and I mean an argument, in both senses. We'll talk about exactly how solid its ground is, because I won't file anything I can't describe honestly to you."

**Choices:**
- Hear her out — what would a written rebuttal say, and what would it stand on → **rebuttal_choice**
  - NOTE (shown after choosing): "It would say: this line is not an observation, it's a quotation — and the thing quoted doesn't survive its own notes. As for what it stands on—" She opens the rule book.

## [rebuttal_choice] Answer It in Writing
*Day 12 — Saturday, November 28, 2026 (dayOffset 12)*

The argument runs through Pa.R.J.C.P. 1340: subsection (E), that a party may present evidence and argument to rebut a provision, and subsection (F), that factual errors may be challenged. A written rebuttal would do both: it would identify the bond line as an imported conclusion rather than a scored observation, attach the session-note language and the visit pattern, and ask that the line be corrected or disregarded.

And here is Ms. Voss, honest as promised: "Whether Rule 1340 reaches a scored assessment summary in this posture has not been tested in a published opinion. It is an argument counsel makes, not a settled right. Filing it costs a little money and an afternoon. Not filing it costs nothing today — and leaves 'attenuated' standing in the agency's own document, unanswered, where findings get drafted from. Judges' findings borrow language. I would rather they not borrow that word unopposed."

**Choices:**
- File the written rebuttal — the imported adjective answered, with the notes and logs attached → **rebuttal_filed**  _(cash −10 ; FLAG: summaryRebutted ; HIDDEN + Rebuttal — scored summary's imported adjective answered in writing (Rule 1340(E)/(F) — untested))_
  - NOTE (shown after choosing): It goes in flagged for exactly what it is: an untested argument, made carefully, on the record, where unanswered words used to live alone.
- Leave the summary unanswered — argue it orally at the hearing if it comes up → **rebuttal_skipped**
  - NOTE (shown after choosing): Oral argument evaporates at the courtroom door. The summary will still be in the packet on the day findings are written. So will its adjective.

## [rebuttal_filed] A Rebuttal on the Record
*Day 12 — Saturday, November 28, 2026 (dayOffset 12)*

The rebuttal is three pages and makes no claim it cannot carry. It does not say the summary is fraudulent. It says the bond line is a quotation wearing a score's clothing; that the quoted source observed ninety minutes and wrote 'sought father's lap repeatedly' in her own notes; and that thirty supervised visits, logged by a neutral witness, are also evidence about a bond. It asks for correction, or disregard, under Rule 1340(E) and (F) — and says, in its own footnote, that the rule's reach to a scored summary is untested. Honesty, filed as a feature.

Whatever the judge does with it, the packet no longer speaks with one voice. That, Ms. Voss says, is sometimes the whole job.

**Choices:**
- Spend Monday — the eve of the hearing — on the ask itself → **eve_prep**
  - NOTE (shown after choosing): Evidence is half the hearing. The other half is knowing exactly what you're asking the judge to write.

## [rebuttal_skipped] Unanswered, by Default
*Day 12 — Saturday, November 28, 2026 (dayOffset 12)*

The scored summary stays as it is. Ms. Voss shrugs the shrug of a lawyer conserving fights. "Maybe the judge discounts it on her own. Judges sometimes do — they know what these forms are. And sometimes a findings draft lifts the packet's language wholesale, because findings are written at 4:40 p.m. by tired people, and 'attenuated' will be right there, spelled correctly, in the agency's own document."

"We've chosen to find out which kind of afternoon December 2 is," she says, "rather than spend ten dollars and an afternoon making the word fight for its place. Noted. Let's go build the ask."

**Choices:**
- Spend Monday — the eve of the hearing — on the ask itself → **eve_prep**
  - NOTE (shown after choosing): What remains is the shape of the request: the words the judge would have to use to give you what you want.

## [eve_prep] The Night Before the Review
*Day 14 — Monday, November 30, 2026 (dayOffset 14)*

Ms. Voss's office, Monday evening, the whiteboard doing its work. She writes the four determinations the court must make at the review — continuing necessity of placement; compliance with the permanency plan; progress toward alleviating the circumstances that caused placement; reasonable efforts to finalize the plan (42 Pa.C.S. § 6351(f)(1), (2), (3), (5.1)) — and under them, the outcomes the court may order, which include return to a parent. (42 Pa.C.S. § 6351(f.1))

"One clock is not today's fight," she says. "Paloma is at eight months in placement. The fifteen-of-twenty-two-months determination — whether the agency has filed a termination petition, and the exceptions to that — is a later hearing's question. (42 Pa.C.S. § 6351(f)(9)) Today is simpler and harder: whose account of the bond does the court credit, and what follows from the crediting."

Then she erases the board and writes one sentence: THE ASK. "Judges grant requests they can picture as orders. Tomorrow we either hand her one, or we ask her to invent one while three lawyers watch."

**Choices:**
- Draft the ask with her, in findings language → **findings_choice**
  - NOTE (shown after choosing): An ask with findings language, steps, and dates is a draft order wearing a request's clothes. Judges recognize the tailoring.

## [findings_choice] Ask in Findings Language
*Day 14 — Monday, November 30, 2026 (dayOffset 14)*

The drafted ask takes an hour and fits on one page. Findings: progress under § 6351(f)(3) — treatment completed, eight months sober, thirty visits kept, the circumstances that caused placement alleviated by the work itself. Order: a stepped return — expanded unsupervised visits now, overnights on a schedule, and return home by the next review if the steps hold, with Ms. Ferro's treatment continuing through the transition.

And a fallback, drafted just as carefully, in case the court wants more evaluation before it moves: then let the question be a focused one — the bond as it stands now, after treatment — put to an evaluator who must observe current visits and review current records. Not the same instrument, run again, over the same stale file.

The alternative is the ask most parents walk in with, through no fault of their own: please, just send her home. It is the truest sentence in the building. It is also, as an instrument of decision, nearly empty — it gives the judge nothing to sign.

**Choices:**
- Go in with the drafted ask — findings, stepped return, and the focused-question fallback → **findings_drafted**  _(FLAG: steppedAsk)_
  - NOTE (shown after choosing): One page. If the court credits your witnesses tomorrow, the order she needs is already written, in her own findings' grammar.
- Go in with the plain plea — the judge has children too; let her hear a father, not a filing → **findings_generic**
  - NOTE (shown after choosing): She will hear a father either way; he'll be sworn. What she won't have, if the evidence breaks your way, is a draft of what to do about it.

## [findings_drafted] Progress, Stepped Return, a Focused Question
*Day 14 — Monday, November 30, 2026 (dayOffset 14)*

You read the page twice. It asks for less than everything and more than nothing, in the exact grammar of the statute the judge will be applying while everyone is still seated. It also does something subtler: it tells the judge what your side thinks the evidence will show, in advance, so that tomorrow, every witness who performs as expected is a promise kept.

"Sleep," Ms. Voss says, in the tone of a professional instruction. "Tomorrow is a listening contest. Dr. Marsh talks first. Then the record talks. Then, if we've done this right, the judge talks last, in findings."

**Choices:**
- Sleep — and walk into the review with a folder that knows its own contents → **hearing_open**
  - NOTE (shown after choosing): Sixteen days of envelopes, memos, subpoenas, and logbooks, all of it aimed at one morning.

## [findings_generic] 'Just Send Her Home'
*Day 14 — Monday, November 30, 2026 (dayOffset 14)*

Ms. Voss doesn't argue. "It's your case and your daughter," she says. "I'll argue the evidence as hard as it can be argued. But understand the mechanics: if the judge credits our side and wants to move Paloma home in steps, she will have to construct the steps herself, at the bench, in a crowded list — or continue the case to construct them later. Momentum is a physical property in courtrooms. A drafted ask has it. A plea asks the judge to manufacture it."

You sleep the way people sleep before hearings: in installments, like the visits, with the goodbye parts too long.

**Choices:**
- Walk into the review → **hearing_open**
  - NOTE (shown after choosing): Whatever the folder holds — or doesn't — the morning is here, and mornings in this system do not reschedule for readiness.

## [hearing_open] The Permanency Review Opens
*Day 16 — Wednesday, December 2, 2026 (dayOffset 16)*

The courtroom is smaller than the size of what happens in it. The judge opens the review the way the statute opens it: this is a permanency hearing, held within six months of the last one (42 Pa.C.S. § 6351(e)(3)(i)), and the court will determine the continuing necessity of placement, compliance with the permanency plan, progress toward alleviating the circumstances that caused placement, and whether reasonable efforts were made to finalize the plan. (42 Pa.C.S. § 6351(f)(1), (2), (3), (5.1))

The agency's report is received. Your progress is reported — treatment, sobriety, visits — largely without dispute; the caseworker's own account of your compliance is, to her credit, fair. The agency's position rests, in the end, on one pillar, and agency counsel says so with admirable clarity: "The evaluation, Your Honor. Dr. Marsh is here."

Everything the agency has comes down to ninety minutes and an adjective. Everything you have comes down to what the last sixteen days put in the folder. The judge calls the witness.

**Choices:**
- Listen to Dr. Marsh the way Ms. Voss taught you: method first, conclusion last → **marsh_direct**
  - NOTE (shown after choosing): She takes the stand with the confidence of a person whose report has never yet been read back to her. That may be about to change. Or not — it depends on the folder.

## [marsh_direct] Dr. Marsh Testifies
*Day 16 — Wednesday, December 2, 2026 (dayOffset 16)*

Direct examination is smooth the way rehearsed things are smooth. Credentials: impeccable. Experience: long. The two observed sessions are described in warm, general terms. The records review is summarized. And then the conclusion, delivered to the judge in the level tone of a person reading weather: the father-daughter bond is attenuated; the child's attachment needs would, in her opinion, be better served by permanency in the current placement; return home is not recommended.

Agency counsel sits down well pleased. The word has now been said under oath, by a doctor, in a courtroom — three more institutional voices added to its collection. It hangs in the air of the room, waiting to find out whether anyone in the next twenty minutes is going to ask it a single question about how it was made.

The judge looks at Ms. Voss. "Your witness, counsel."

**Choices:**
- Rise for cross-examination → **cross_choice**
  - NOTE (shown after choosing): What happens next was decided on days 3, 6, and 9 — in an envelope, a memo, and a set of notes. Courtrooms only reveal preparation; they do not create it.

## [cross_choice] Your Cross-Examination
*Day 16 — Wednesday, December 2, 2026 (dayOffset 16)*

Cross-examination is a choice of target. There are three available, and they are not equal. The witness's credentials are gleaming — a fight there is a fight on her strongest ground, in front of a judge who has qualified a hundred experts and likes approximately none of the lawyers who waste her time pretending a résumé is a method. The witness's conclusion is unmovable — experts do not recant conclusions on cross, ever. And the witness's method — the ninety minutes, the missing comparison, the stale file, and whatever her own notes say — is simply a set of facts she has already admitted in writing, waiting to be asked about in order.

Ms. Voss stands with whatever the last sixteen days actually built. A prepared cross exists only if the memo was built and the file was obtained. An improvised one exists in every courtroom, every day, and the witness has survived a hundred of them.

**Choices:**
- Cross on the method — the memo, the notes, the staircase: ninety minutes, no comparison, stale records, her own words read back → **cross_method**  _(FLAG: methodCrossDone ; HIDDEN + Transcript — cross-examination: 90 minutes observed; no comparison observation; records pre-dated treatment ; REQUIRES FLAG: crossReady ; REQUIRES FLAG: recordsRequested)_
  - NOTE (shown after choosing): Question one is the gentlest sentence in the room: "Doctor, let's start with what you actually saw."
- Cross on the credentials — challenge whether Dr. Marsh is qualified to judge this family at all → **cross_credentials**
  - NOTE (shown after choosing): She is qualified, and everyone in the room including the judge is about to be reminded of it, at length, by her.
- Waive cross — the report speaks for itself, and attacking a doctor may backfire → **cross_none**
  - NOTE (shown after choosing): The report does speak for itself. That is the difficulty. It will now do so, uninterrupted, for the rest of the hearing.

## [cross_method] Ninety Minutes
*Day 16 — Wednesday, December 2, 2026 (dayOffset 16)*

It is not dramatic. That is why it works. "You observed Mr. Quill and Paloma together for how long, in total?" Ninety minutes, Doctor. "Two sessions of forty-five minutes." Yes. "You never observed Paloma with her foster parents, for comparison?" That was not part of the referral. "The records you reviewed — the ones your report cites most heavily — were written before Mr. Quill entered treatment, correct?" They were the records provided. "You have not seen the visit logs for the last five months?" No.

Then the notes. Ms. Voss hands the witness her own session notes — obtained on written request, marked, admitted — and asks her to read the highlighted line aloud. Dr. Marsh reads: "Child sought father's lap repeatedly." A pause. "And at the end of session two, Doctor — your handwriting again." "Separation protest strong." "Thank you. Nothing further."

Dr. Marsh does not recant; experts never do. She says observations and conclusions are different things, which is true, and the judge writes something down — which is the whole game. The conclusion now has a visible seam in it, and the seam is the witness's own handwriting.

**Choices:**
- Sit down. The other witnesses are next → **evidence_turn**
  - NOTE (shown after choosing): The adjective is still in the record. It is no longer alone in it, and it is no longer unquestioned. Those are different accomplishments; both matter.

## [cross_credentials] The Wrong Fight
*Day 16 — Wednesday, December 2, 2026 (dayOffset 16)*

The credential cross goes the way credential crosses go against qualified experts: each question becomes an occasion for the witness to recite another qualification. Board certifications. Years. Hundreds of evaluations. Two courts' worth of prior testimony, which the judge — who has heard Dr. Marsh before, it emerges — receives with a small nod of recognition.

By the time Ms. Voss sits down, the evaluation's conclusion has not been dented, and its author has been burnished for twenty minutes at your side's expense. The judge's one interjection lands where it lands: "Counsel, I take it the doctor's qualifications are not really your point. If you have a point about the work itself, the court will hear it at argument." The work itself — the ninety minutes, the notes — was the soft part. It remains, largely, unpressed.

Not a catastrophe. A tax: credibility spent on the witness's strongest ground buys nothing on her weakest.

**Choices:**
- Move on — the other witnesses are next, and they are yours → **evidence_turn**
  - NOTE (shown after choosing): Cases are rarely lost in one cross-examination. They are, however, priced there.

## [cross_none] The Report Stands
*Day 16 — Wednesday, December 2, 2026 (dayOffset 16)*

"No questions, Your Honor." It takes two seconds. Dr. Marsh steps down having said, under oath and without interruption, exactly what her report said — the conclusion now indistinguishable, in the record, from a fact. There were things that could have been asked. How many minutes. Compared to what. Which records, from when. What her own notes recorded, in the room, before the conclusion was written. None of it was asked, because the preparation for asking it — the file, the memo — was the part of the case that happened, or didn't, on days 3, 6, and 9, far from any courtroom.

Agency counsel, in the corridor of the hearing's middle, is already saying the word again. Attenuated. It will be in their closing. It will be in the proposed findings they hand up. Unopposed words usually are.

**Choices:**
- Move on — your side of the evidence is next → **evidence_turn**
  - NOTE (shown after choosing): What remains is what remains: a therapist, a logbook, and a father. Whether they are in the room is a different question than whether they exist.

## [evidence_turn] The Other Witnesses
*Day 16 — Wednesday, December 2, 2026 (dayOffset 16)*

Your case, Ms. Voss announces, calls the treating therapist. Or it doesn't — because a witness who was never confirmed cannot be called, only described, and the letter in the packet will be offered and read the way letters are read: silently, at the speed of the stack, by a judge who has already heard a live expert hold the room for forty minutes.

Ms. Voss looks at the witness door, and then at you, and what happens in the next ten minutes is the second thing the last sixteen days decided.

**Choices:**
- Call Ms. Ferro — live, sworn, with fourteen months of session records in her hands → **ferro_live_node**  _(HIDDEN + Transcript — treating therapist testified live: fourteen months of sessions ; REQUIRES FLAG: therapistLive)_
  - NOTE (shown after choosing): She comes through the door the way she comes into sessions: unhurried, prepared, and entirely unafraid of the questions.
- Offer Ms. Ferro's letter and ask the court to give it the weight it deserves → **ferro_letter_node**
  - NOTE (shown after choosing): The clerk marks it. The judge reads it in the time it takes agency counsel to find a page in the evaluation. Both documents are now 'in evidence.' They are not the same size in the room.

## [ferro_live_node] Fourteen Months, Live
*Day 16 — Wednesday, December 2, 2026 (dayOffset 16)*

Ms. Ferro testifies the way she therapists: precisely, and without performing. Fourteen months of weekly sessions. The early Paloma, who drew her father small and at the edge of the page. The repair work, session by session — the apologies made in the visit room and what a six-year-old does with an apology that turns out to be true. The recent Paloma, who drew the house with two doors and explained, to the dollhouse, that her father "went to get fixed and then he stayed fixed."

Agency counsel crosses her — fairly, and she survives it the way she promised: yes, she is the treating therapist, not a neutral evaluator; no, that is not a defect, it is a different vantage; ninety minutes is a photograph, fourteen months is a film, and the court is welcome to weigh both for exactly what they are.

The judge asks two questions of her own — about the transition plan, about what Paloma needs if visits expand — the kind of questions judges ask witnesses they are building findings on. You learn to hear the difference. It sounds like carpentry.

**Choices:**
- Rest your evidence — one witness remains, and he is not an expert → **judge_question**
  - NOTE (shown after choosing): The judge turns to you with the expression of a person saving the simplest question for last. It is not simple.

## [ferro_letter_node] Read Into the Record
*Day 16 — Wednesday, December 2, 2026 (dayOffset 16)*

The letter is received. The judge reads it — you watch her read it, both pages, which is more than many letters get — and sets it with the packet. It says everything right, at the speed of reading, with no voice attached, and when agency counsel says, at argument, "the therapist's letter, Your Honor, is a treatment summary, not an evaluation," there is no one in the room who can stand up and answer: I know the difference; I have watched this child for fourteen months; ask me anything.

Ms. Voss argues the letter as hard as paper can be argued. But the asymmetry is now the architecture of the hearing: their witness was a person; yours is a document. Judges are readers by profession, and even they remember voices longer than pages.

**Choices:**
- Rest your evidence — one witness remains, and he is not an expert → **judge_question**
  - NOTE (shown after choosing): The judge turns to you. Whatever your side lacked in paper, this part will not lack in candor — or it will lack everything.

## [judge_question] The Judge Asks About the DUI Year
*Day 16 — Wednesday, December 2, 2026 (dayOffset 16)*

You testify last, briefly — Ms. Voss walks you through the compliance record: treatment, the screens, the meetings, the visits, the work. Then the judge leans forward, and the room changes temperature. "Mr. Quill. I have read about the spring. I want to hear from you: what was happening, the night of the arrest — and what is different, specifically, now?"

Every person in the room knows what this question is. It is not about the evaluation. It is the judge deciding, in real time, whether the man in front of her is the author of his own progress or the audience of it. There is a version of the answer that treats the spring like weather that happened to you. And there is the version you have practiced in a hundred meetings, one honest sentence at a time.

**Choices:**
- Answer it straight — the drinking, the driving, the arrest, and then the specific, dated, unglamorous machinery of the eight months since → **closing_choice**  _(FLAG: answeredStraight)_
  - NOTE (shown after choosing): The judge's pen moves through the whole answer. Some testimony is weighed. Some is simply believed. The difference is audible.
- Keep it brief and safe — that year was a hard time, mistakes were made, you're doing better now → **closing_choice**
  - NOTE (shown after choosing): Every word is defensible. None of it is evidence. The judge's pen, you notice, does not move.

## [closing_choice] Closing: What the Record Can Carry
*Day 16 — Wednesday, December 2, 2026 (dayOffset 16)*

Closing argument is accounting. Agency counsel counts what the agency has: a qualified expert, a conclusion, a scored summary that agrees with it, and the word — said now, under oath and in print, more times than you have counted. "The evaluation is the only professional assessment of the bond before this court, and it does not recommend return."

Ms. Voss rises to count what you have — and what she can count depends, with total precision, on the last sixteen days. A cross that happened or didn't. A therapist who testified or wrote. Logs that were filed or left. A rebuttal that answered the adjective or let it stand. A drafted ask, in findings language, or a plea. The judge is not grading effort, or love, or suffering. She is deciding what this record can carry, and then she will write it down in findings under § 6351(f) — where, as ever, it will become the case.

**Choices:**
- Argue the whole record — the crossed method, the live therapist, the filed logs, the answered adjective — and hand up the drafted ask: stepped return under § 6351(f)(3) and (f.1) → **end_win**  _(HIDDEN + Order — findings credit the treating witnesses; stepped return ordered ; REQUIRES FLAG: therapistLive ; REQUIRES FLAG: crossReady ; REQUIRES FLAG: recordsRequested ; REQUIRES FLAG: visitRecordFiled ; REQUIRES FLAG: summaryRebutted ; REQUIRES FLAG: methodCrossDone)_
  - NOTE (shown after choosing): Every element of this argument exists because of a specific day in November. The judge has the draft order in front of her before the words are finished.
- Argue the method doubt — whatever the court does about return, it should not rest on ninety minutes; ask for a focused re-evaluation of the post-treatment bond → **end_partial**  _(REQUIRES FLAG: crossReady)_
  - NOTE (shown after choosing): A prepared cross bought this much: the conclusion is no longer comfortable enough to simply adopt. The ask matches the doubt — a better question, put properly, this time.
- Argue the therapist's evidence — fourteen months against ninety minutes — and ask for the focused re-evaluation with expanded visits meanwhile → **end_partial**  _(REQUIRES FLAG: therapistLive)_
  - NOTE (shown after choosing): The treating witness gave the court a second vantage it cannot un-hear. It is enough to stop the evaluation's momentum, if not yet to reverse it.
- Rest on the progress record — treatment, sobriety, visits — and ask the court to weigh it against the evaluation → **end_loss**  _(REQUIRES NO FLAG: crossReady ; REQUIRES NO FLAG: therapistLive)_
  - NOTE (shown after choosing): The progress is real, and the judge honors it — aloud. But an unexamined expert conclusion is still standing across the room from it, and real progress, unaccompanied, is about to be weighed against a word nobody questioned.

## [end_win] The Evaluator Is Not the Judge
*Day 17 — Thursday, December 3, 2026 (dayOffset 17)*

The findings come down from the bench on Wednesday and the written order follows on Thursday, and the sentence in it that matters is not about you. It is about the evidence. The court credits the treating therapist and the visit record over the evaluation's conclusion: the evaluation, the court finds, rested on limited observation and a record that substantially predated the father's treatment, and its own session notes did not support the weight its conclusion was asked to carry.

Findings under 42 Pa.C.S. § 6351(f)(3) are entered for you — progress toward alleviating the circumstances that caused placement, proven by the work itself. The order is a stepped return: expanded unsupervised visits now, overnights on the drafted schedule, and return home by the next review if the steps hold, with Ms. Ferro's treatment continuing through the transition. Paloma is told in words for a six-year-old: more sleeps at Dad's are coming, on a calendar she can see, with the second door on the house she drew.

Dr. Marsh's report stays in the file, where reports live. It just no longer lives there as a verdict — because somewhere along the way, a father and his lawyer treated it as what it was: an opinion, with a method, that a judge was free to weigh and free to set down.

**Ending.**

**Debrief:**
- WHAT THE FILE SAID — The hidden record told the real story: the evaluation's own raw notes, released on written request under 55 Pa. Code § 3130.44(d), recorded a child who 'sought father's lap repeatedly,' in tension with the conclusion's adjective; the cross-examination transcript fixed the method at ninety minutes observed, no comparison observation, and records that pre-dated treatment; the treating therapist testified live from fourteen months of sessions; the visit supervisor's logs documented thirty visits and the child's approach behavior; a written rebuttal answered the scored summary's imported adjective; and the final order credited the treating witnesses and ordered the stepped return. Sixteen days of paper became one afternoon of findings.
- THE LAW THAT CONTROLLED IT — A permanency hearing belongs to the court: at it, the court must determine the continuing necessity of placement, compliance with the permanency plan, progress toward alleviating the circumstances that caused placement, and whether reasonable efforts were made to finalize the plan (42 Pa.C.S. § 6351(f)(1), (2), (3), (5.1)), and its options include return to a parent (42 Pa.C.S. § 6351(f.1)). No rule required the evaluation, and none made its conclusion binding — it was evidence, weighed against other evidence. The agency record was released on request (55 Pa. Code § 3130.44(d)); the posture toward the report — examine it, controvert it, cross-examine its maker — is the principle stated for disposition at 42 Pa.C.S. § 6341(d)(2). The rebuttal of the scored summary argued Pa.R.J.C.P. 1340(E) and (F), whose reach to a scored assessment summary has not been tested in a published opinion.
- THE HONEST PART — This ending was not a verdict that Vernon is a good father, and the other endings are not verdicts that he is a bad one. The same man, the same eight months sober, the same daughter running to the same door, can land in any of the three endings depending on envelopes mailed in November, a therapist's Wednesday calendar, and a judge's weighing of two professionals on a given afternoon. Outcomes here turn on workers, judges, resources, and luck as much as on any parent. What the route controlled was narrower and real: when the weighing happened, there was something on both sides of the scale.

## [end_partial] Two Reports, One More Question
*Day 17 — Thursday, December 3, 2026 (dayOffset 17)*

The court splits it, the way courts split things they are not done thinking about. The order, issued Thursday, does not return Paloma — the evaluation's recommendation is not adopted, but neither is it discarded, and the court says the honest version of why: on this record, it cannot fully credit a conclusion whose foundations were shown to be thinner than its confidence, and it will not end a placement on a doubt, either.

So the court orders the question asked again, properly: a focused re-evaluation, limited to the bond as it stands after treatment, with the evaluator required to observe current visits and review current records — the stale file is named in the order as the problem it was. Meanwhile, visits expand. Ms. Ferro's work continues. The next review is set, and it will open with a better question than this one did.

It is not the ending Vernon asked for. It is also not the ending the packet had written for him on day 0, in which one word, unexamined, simply became the plan.

**Ending.**

**Debrief:**
- WHAT THE FILE SAID — Some of the record got built and some didn't, and the order is an exact map of which. Where the evaluation was actually pressed — a prepared cross on its method, or a treating therapist testifying live from fourteen months of sessions — the court balked at adopting its conclusion. Where the record stayed thin — a letter instead of a witness, a credential fight instead of a method cross, an adjective in the scored summary that no written rebuttal answered — the court's doubt had nothing further to stand on, and doubt alone does not end a placement. The remedy reflects the gap precisely: the same question, re-asked with current observations and current records.
- THE LAW THAT CONTROLLED IT — The determinations at a permanency hearing are the court's to make on all the evidence (42 Pa.C.S. § 6351(f)(1), (2), (3), (5.1)), and its options include return to a parent (42 Pa.C.S. § 6351(f.1)) — which this record did not yet carry it to. The agency record is released on written request (55 Pa. Code § 3130.44(d)); reports may be examined and controverted and their makers cross-examined, the principle stated for disposition at 42 Pa.C.S. § 6341(d)(2); and a rebuttal aimed at the scored summary rests on Pa.R.J.C.P. 1340(E) and (F), whose reach to a scored assessment summary has not been tested in a published opinion. An expert's recommendation, it turns out, is the beginning of the court's analysis when somebody makes it one — and the end of it when nobody does.
- THE HONEST PART — A partial ending measures a record, not a father. The same sobriety, the same visits, the same daughter drew a different order here because one or two November decisions went the other way — an envelope, an afternoon, a phone call not made by a Wednesday deadline. A different judge might have returned Paloma on this record, or adopted the evaluation outright; workers, judges, and luck hold pieces of every outcome in this system. What is durable here is the order's own instruction: the next evaluation will observe the present, not inherit the past. The question got better because somebody made the court look at it twice.

## [end_loss] Forty-Five Minutes
*Day 16 — Wednesday, December 2, 2026 (dayOffset 16)*

The hearing is not long. Your progress is reported and credited — the judge thanks you for it, sincerely, the way one thanks a man for weather he cannot use. Then agency counsel rises and does the simplest thing available to her: she asks the court to adopt the evaluation's recommendation, and she uses its word three times in the goal discussion. Attenuated. Attenuated. Attenuated. No one in the room has ever asked the word a question, so the word never has to become anything smaller than a finding.

The court adopts the recommendation nearly verbatim. Placement continues. The goal discussion moves, in the evaluation's own vocabulary, toward permanency in the current placement. Paloma's next visit is Saturday, in the room with the logbook, and the hour will be a good hour — the file will simply never know what it meant, because the parts of the record that could have told it were never requested, never built, never called.

Somewhere across town, in an unopened file, a psychologist's session notes say a little girl sought her father's lap repeatedly, in two forty-five-minute sessions, while a conclusion was being prepared that she would never read.

**Ending.**

**Debrief:**
- WHAT THE FILE SAID — The record the court weighed was the packet as it arrived on day 0: an evaluation received late in the preparation, read for its conclusion, and never crossed on its method; a scored summary carrying the word 'attenuated' as an agency data line, unanswered in writing. What the file never contained was the counter-record: the evaluator's raw session notes — which described proximity-seeking and strong separation protest, in tension with the conclusion, and which a written request under 55 Pa. Code § 3130.44(d) would have produced in November — the treating therapist's live testimony, and a filed summary of thirty supervised visits. The adjective was contradicted the whole time. It was contradicted in a file nobody requested.
- THE LAW THAT CONTROLLED IT — The permanency determinations were still the court's to make (42 Pa.C.S. § 6351(f)(1), (2), (3), (5.1)), and return to a parent was still among its options (42 Pa.C.S. § 6351(f.1)); nothing in the law required the court to adopt the evaluation — and nothing in the law required it to doubt a conclusion no one had examined. The tools existed and were not used: the record released on request (55 Pa. Code § 3130.44(d)); reports examined and controverted, their makers cross-examined, as stated for disposition at 42 Pa.C.S. § 6341(d)(2); a rebuttal of the scored summary under Pa.R.J.C.P. 1340(E) and (F) — untested, as any such argument must honestly be labeled, but unmade entirely here.
- THE HONEST PART — This ending is not a finding that Vernon loves his daughter less, or parented her worse, than in the other endings. He did the treatment. He kept the visits. He stayed sober. What he did not do was mail an envelope, build a memo, and make a phone call by three November deadlines — logistics and record mechanics, not virtue — and a different judge, a different evaluator, or a caseworker who volunteered the notes could have changed the afternoon entirely. Outcomes in this system turn on workers, judges, and luck. The bleakest sentence in this debrief is also the most useful one: the notes said what they said the whole time, and the case was lost in the distance between a file that existed and a file that was asked for.
