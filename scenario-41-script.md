# THE FIRST 90 DAYS — Scenario 41: “The Night They Came Twice”

*Human-readable script. This document and `scenario-41.json` are generated from a single source and match node-for-node: same IDs, same order, same choices, same effects.*

**The family is fictional — a composite. No real person's story appears here.**

**Content note:** This scenario depicts an investigation with two evening visits, a disputed agreement, and — on one path — an emergency placement with a relative and a shelter care hearing. There is no graphic content. Players may skip any scene or use the quick exit at any time.

**How to read effects:** `cash −40` changes the player's cash. `FLAG: name` sets a flag the engine tracks. `HIDDEN + item` means the case file quietly records that item at this choice. `REQUIRES FLAG: name` means the choice is only available if that flag was set earlier.

Start date: Saturday, February 21, 2026. Day offsets are days since the scenario's start date.

## [start] The Store at Dusk
*Day 0 — Saturday, February 21, 2026 (dayOffset 0)*

The corner store is two doors down, close enough that Cosette Barr watches Caleb make the trip from the front window the way her own mother once watched her: nine years old, sent for milk, tall for his age, instructed to come straight back. Cleo, five, went with him because Cleo goes everywhere Caleb goes, holding the list like a passport.

They were gone eleven minutes. In the twelfth, a woman Cosette doesn't know was at the store counter asking whose children these were. In the twentieth, there was a knock, and a woman Cosette doesn't know was at her own door instead: Ms. Gable, from the county agency, with a notebook already open.

It is 7 p.m. on a Saturday. The milk is in the refrigerator. The investigation is in the living room.

**Choices:**
- Let her in, keep the children in earshot, and listen more than you talk → **c2**
  - NOTE (shown after choosing): Listening is not surrender. It is reconnaissance — and everything she says tonight is about to matter twice.
- Object — it's Saturday night, the children are home, this can wait until Monday → **c2**
  - NOTE (shown after choosing): It cannot, from her chair: a report of unsupervised children gets a same-day look. The objection is noted. So is everything after it.

## [c2] What Was Agreed
*Day 1 — Sunday, February 22, 2026 (dayOffset 1)*

Ms. Gable is brisk and, in her way, fair. She looks at the store from the window. She asks Caleb about the trip (he narrates it like a sports replay). Then she says the sentence the whole case will turn on: 'We're in agreement, then — no more errands alone, and I'll write it up and we'll close this out.' Cosette says yes to exactly that. Gable writes for a while, closes the notebook, and leaves into the dark.

Agreement is a word two people can carry out of a room in different sizes. Tonight it leaves in hers: a notebook, closed.

Yours is still available — in the next hour, while the words are exact.

**Choices:**
- Write down tonight's visit verbatim — times, her sentence, your yes — dated and signed → **n2b**  _(FLAG: notesWritten ; HIDDEN + Record — parent wrote a verbatim, dated account of the first visit the same night)_
  - NOTE (shown after choosing): Eleven lines. It takes nine minutes. It will be the only first-person account of Saturday night in existence that isn't a summary.
- Trust the agreement — it was simple, and she seemed straight → **n2b**
  - NOTE (shown after choosing): She probably is. Straight people summarize too, and summaries drift toward the summarizer's institution.

## [n2b] Sunday, Quietly
*Day 2 — Monday, February 23, 2026 (dayOffset 2)*

Sunday is ordinary, which feels illegal. Caleb is not sent for milk. Cleo holds an imaginary list and walks to the window and back, practicing. Cosette watches the store from the window out of new habit and thinks about the errand the way the file now will: a nine-year-old, a five-year-old, eleven minutes, dusk.

The truth has texture: the store is two doors down; the trip is a family institution; the woman at the counter was a stranger to all of it. Texture is exactly what summaries remove.

Tomorrow there is a meeting at the agency. Meetings are where texture goes to be decided about.

**Choices:**
- Decide what Monday needs: not an argument — the record, corrected while it's young → **records**
  - NOTE (shown after choosing): Files are most correctable before their second reader. Monday is soon. Good.
- Decide Monday will be a formality — she said they'd close it out → **records**
  - NOTE (shown after choosing): She did say that. Whether her notebook says it is a question Monday will answer.

## [records] Your Own Record, First
*Day 3 — Tuesday, February 24, 2026 (dayOffset 3)*

Before Monday's meeting, Cosette requests the file: the intake summary and the visit note. The record is released on request — 55 Pa. Code § 3130.44(d) — and reading it Sunday night, at her own table, is the first time she sees Saturday in the system's handwriting.

The intake is one line: 'Two children, 9 and 5, unsupervised at retail store, evening.' The visit note is longer, and mostly fair.

Mostly.

**Choices:**
- File the written request for the intake summary and the visit note → **m1**  _(FLAG: recordsRequested ; HIDDEN + Records — parent obtained the intake summary and first visit note before the follow-up meeting)_
  - NOTE (shown after choosing): What arrives is enough to prepare with: the report's one line, and Gable's note — which Cosette now reads the way editors read, pen in hand.
- Wait for Monday — reading their notes feels like studying for a test you didn't sign up for → **m1**
  - NOTE (shown after choosing): It is exactly that test. The only choice is whether you sit it prepared.

## [m1] What the Note Says
*Day 4 — Wednesday, February 25, 2026 (dayOffset 4)*

Gable's note, read closely: 'Mother cooperative. Children sent to nearby store unaccompanied at dusk; mother states she observed from window. Mother agreed: children will not be sent on errands unaccompanied. Follow-up Monday; anticipate closure.'

It is accurate. All of it happened, in that order, in those words. Cosette reads it twice more, hunting for the trap, and finds only this: it is the only account that will be in the room Monday. Hers — if she wrote it — is the second. If she didn't, Monday's meeting will be a discussion between a note and a memory.

**Choices:**
- Annotate your copy — where the note is right, where your account adds the window, the eleven minutes, the watching → **prep**  _(FLAG: copyAnnotated)_
  - NOTE (shown after choosing): Her note says 'observed from window' already — Gable was fair. The annotation's job is not combat. It's ballast: your words, beside hers, in the same file.
- Close the folder — the note is fair, Monday will take care of itself → **prep**
  - NOTE (shown after choosing): The note is fair. Monday, as it happens, will not be run by the woman who wrote it.

## [prep] The Neighbor at the Window
*Day 5 — Thursday, February 26, 2026 (dayOffset 5)*

Mrs. Deveraux, across the street, watched Saturday too — watched Cosette at the window, in fact, for the whole eleven minutes, because her television was broken and the street was the show. Her account exists. Like all accounts, it will matter in proportion to how much of it is on paper.

And there is the confirmation to draft: a short letter for Monday, asking the agency to confirm in the file what was agreed Saturday — errands, unaccompanied, ended — and nothing else. Short letters, carried into meetings, have a way of becoming file entries.

**Choices:**
- Get Mrs. Deveraux's statement in writing, and draft the confirmation letter tonight → **eve**  _(FLAG: neighborSeen ; FLAG: confirmReady ; HIDDEN + Proof — neighbor's written statement obtained; written confirmation of the agreed terms drafted)_
  - NOTE (shown after choosing): Her statement is six lines and mentions the broken television, which is the kind of detail truth has and inventions don't. The letter is five lines. Both fit in one folder.
- Mention the neighbor at the meeting if it comes up — paper feels like lawyering up → **eve**
  - NOTE (shown after choosing): It is lawyering up, in the literal sense: it is what the record looks like when a parent builds it on purpose. The meeting will decide whether that's a criticism or a compliment.

## [eve] The Night Before Monday
*Day 6 — Friday, February 27, 2026 (dayOffset 6)*

The folder is ready or it isn't: Gable's note, the intake line, the neighbor's six lines, the confirmation letter, and — if Saturday night went the way it should have — Cosette's own eleven lines, written while the words were warm.

Across town, a coverage schedule is being made that Cosette can't see: Ms. Gable is off Monday. The meeting will be run by Mr. Venn, who has read the file exactly once, quickly, the way covering workers do.

He has read Gable's note as broader than she wrote it. Readers do that. It's why files need ballast.

**Choices:**
- Sleep. The folder is the argument, and it's made → **gate**
  - NOTE (shown after choosing): Whatever Monday holds, it will be met with paper. That was the whole job of the weekend.
- Rehearse arguments against a broader reading until midnight → **gate**
  - NOTE (shown after choosing): Arguments against a reading are wind. Paper against a reading is weight. The folder — if it's built — already contains the rebuttal.

## [gate] The Meeting, With a Different Reader
*Day 7 — Saturday, February 28, 2026 (dayOffset 7)*

Mr. Venn is polite, harried, and reading from Gable's note with a supervisor's summary clipped to it. The summary — which Gable did not write — says: 'Mother agreed to safety plan: children supervised at all times; any recurrence to be addressed by petition.'

'Supervised at all times' is not in the note. 'Petition' is not in the note. But the summary is on top of the file, and summaries are what covering workers enforce. Venn looks up: 'So — we're agreed on the plan as summarized?'

This is the decision the weekend built toward. The folder is on the table. So is his summary.

**Choices:**
- Hand him the confirmation letter: the agreed terms as actually agreed Saturday — and ask that the file be corrected to them → **w1**  _(REQUIRES FLAG: confirmReady)_
  - NOTE (shown after choosing): The letter names the agreement in five lines: errands unaccompanied — ended; no other terms discussed. It is dated this weekend, signed, and now it is in his hands before his summary hardens into the plan.
- Tell him that's not what was agreed — explain Saturday again, fully, out loud → **h0**
  - NOTE (shown after choosing): He listens. He nods. He writes two words in the margin of the summary, and they are not your words. They are: 'Mother disputes.'

## [w1] Gable, By Phone
*Day 9 — Monday, March 2, 2026 (dayOffset 9)*

Venn does something covering workers don't always do: he calls Gable, on speaker, with Cosette in the room. Gable, from wherever days off happen, is crisp: 'Errands, unaccompanied. That's what we discussed. I wrote closure for Monday.'

The summary's author is not in the room and never will be. The note's author has just outranked it, live. Venn unclips the summary from the file — a small sound, like a verdict — and writes on the note itself.

**Choices:**
- Ask him to read back what he's writing into the note → **w1b**
  - NOTE (shown after choosing): He does. Workers who will read back their corrections are workers whose corrections happen. Listen for the errands, and for the absence of the petition.
- Let him write — pressing feels ungrateful, mid-rescue → **w1b**
  - NOTE (shown after choosing): Gratitude is a virtue. Verification is a discipline. The file is indifferent to both and records only one.

## [w1b] Amended, In Ink
*Day 10 — Tuesday, March 3, 2026 (dayOffset 10)*

The amendment, read back: 'Correction per worker Gable, confirmed by phone 2/23: agreed term is that children will not be sent on errands unaccompanied. No supervision plan or petition term was discussed or agreed. File to close following one follow-up visit.' His initials. The date.

It is not an apology and it is not a victory speech. It is better than both: it is the file, agreeing with Saturday, in ink, before any second reader builds on the summary.

Cosette asks for a copy for her folder. He makes one without being asked twice.

**Choices:**
- File your copy tonight, with the neighbor's statement and your Saturday lines behind it → **w2**  _(FLAG: amendmentCopied ; HIDDEN + Record — parent kept a copy of the corrected file note with her own account and the neighbor's statement)_
  - NOTE (shown after choosing): Two buildings, one story. The file's most dangerous page — the summary — no longer exists in either.
- Let his copy be the record — the correction is what counts → **w2**
  - NOTE (shown after choosing): The correction counts double if it can be produced in a year, in one page, to a stranger.

## [w2] The Confirmation, In Writing
*Day 11 — Wednesday, March 4, 2026 (dayOffset 11)*

The formal confirmation letter arrives Wednesday, and it says the agreement in the agency's own letterhead the way Cosette's five lines said it in hers: errands, unaccompanied, ended; follow-up visit Friday; closure to follow.

Two texts, one agreement, matching. This is what the system looks like when it works — not warmth, exactly. Correspondence.

Friday's visit remains. It will be conducted by Venn, who now owns this file's truth and seems, if anything, relieved to.

**Choices:**
- Prepare Friday the way Saturday should be: ordinary, documented, nothing to perform → **w2b**
  - NOTE (shown after choosing): The plan is the week itself, lived visibly: no errands, homework, the window. Documentation of ordinary is a short log and a clear conscience.
- Prepare Friday like an inspection — the house has never been this ready for anything → **w2b**
  - NOTE (shown after choosing): Houses can be too ready; children sense stagecraft. The visit grades the week, not the staging.

## [w2b] A Week on the Narrow Plan
*Day 13 — Friday, March 6, 2026 (dayOffset 13)*

The week complies with itself. Caleb walks to the window once, list in hand, and conducts the errand in pantomime, to general acclaim. Mrs. Deveraux's television gets fixed; she reports this as a loss. Cosette logs the week in five lines — dates, evenings, nothing to report — because a plan this narrow deserves a record as narrow and exact as it is.

The log is not required. That is rather the point of it: required paper proves compliance; voluntary paper proves authorship.

Friday comes.

**Choices:**
- Bring the log to Friday's visit — offer it for the file → **w3a**  _(FLAG: complianceLog ; HIDDEN + Documentation — parent kept and offered a dated log of the agreed plan's first week)_
  - NOTE (shown after choosing): Venn takes it with the air of a man whose file just got easier to close. Correspondence, again — the system's native love language.
- Keep the week in your head — it was unremarkable → **w3a**
  - NOTE (shown after choosing): Unremarkable weeks are the goal of every plan ever written. Written down, they are also evidence. In your head, they are a mood.

## [w3a] The Draft Summary
*Day 15 — Sunday, March 8, 2026 (dayOffset 15)*

Friday's visit is twenty minutes of ordinariness, professionally witnessed. Venn drafts the closing summary at the kitchen table, and — because this file has taught him its reader is attentive — he turns it around when he's done: 'Read it before I file it. Anything wrong, say so now.'

It is right in every line but one, and the line is small and human: 'Mother initially hostile to Saturday visit.' Cosette was not hostile. She was startled, in a doorway, at 7 p.m., in socks. The difference will matter to some future reader exactly as much as 'supervised at all times' was about to.

There is a pen on the table.

**Choices:**
- Point to the line, once, with Saturday's own paper beside it — your eleven lines say 'startled,' in your hand, from that night → **w3**  _(FLAG: lineCorrected)_
  - NOTE (shown after choosing): He reads your Saturday account — which exists, dated that night — shrugs the shrug of a man caught being approximate, and strikes 'hostile' for 'startled.' One word. In ink. Before filing.
- Let it stand — the case is closing, and 'hostile' is one word → **w3**
  - NOTE (shown after choosing): One word is exactly the size of every problem this week contained. Summaries are made of them.

## [w3] Sign Here
*Day 16 — Monday, March 9, 2026 (dayOffset 16)*

The closing letter follows Monday: investigation closed, report not supported as to supervision, agreement noted and satisfied. The acknowledgment line waits at the bottom — receipt, not agreement — and above it, the summary paragraph, in which the whole case is compressed one final time.

Everything you have done for nine days has been about what such paragraphs say. This one deserves the nine days' discipline, one last time.

**Choices:**
- Read the whole letter, then sign and file it with the rest → **end_good**  _(FLAG: readBeforeSigning)_
  - NOTE (shown after choosing): Every sentence checks: errands, ended; Saturday, startled; agreement, as agreed. Your name goes under a letter you have actually read, into a folder that holds the whole correction, start to finish.
- Sign — it's closed, and closed was the goal → **end_partial**
  - NOTE (shown after choosing): It is closed. The summary paragraph, which you did not read, describes 'a safety plan, complied with' — the plan that never existed, resurrected in summary, where summaries live forever. Venn's amendment is in the file too, one page deeper, where corrections live. Readers read summaries.

## [end_good] On Her Own Paper
*Day 18 — Wednesday, March 11, 2026 (dayOffset 18)*

**DEBRIEF:**

The investigation closed on the agreement as it was actually made — errands, unaccompanied, ended — because at the one meeting where a stranger's summary tried to enlarge it, the enlargement met paper: a five-line confirmation, drafted before the meeting, naming the terms as agreed. WIN: the file records Cosette's Saturday, in Cosette's terms, corrected in ink in her presence.

The record inside this story: under 55 Pa. Code § 3130.44(d), the intake summary and Gable's note came from her record, on request, before the meeting — which is how she knew the note was fair and the summary wasn't, and could aim at the difference instead of at the agency. The neighbor's statement and her own same-night lines did the rest: ballast, in writing, dated.

Notice the hinge: a covering worker read a supervisor's summary instead of the note. That is not villainy; it is Tuesday, in every office on earth. What defeated it was not argument — the argumentative route exists in this story, and it is longer — but a document that predated the summary.

Honesty requires this: Gable answered her phone on her day off and told the truth crisply, and Venn unclipped the summary in front of a witness. Different offices let the summary stand and dare you to appeal it. Workers vary, summaries vary. The letter works because it exists before it's needed — which is the only time such letters can be written.

## [h0] “Mother Disputes”
*Day 8 — Sunday, March 1, 2026 (dayOffset 8)*

Venn writes 'mother disputes plan' in the margin and the temperature of the file changes. A dispute, in a file, is not a disagreement — it is a posture, and postures get planned around. He slides a paper across the table: a voluntary placement agreement. The children would stay with Cosette's sister Marla 'until this is sorted out.'

'It's not a removal,' he says, and that is technically true. 'You'd be agreeing.' The paper has a signature line, a start date, and — Cosette reads it twice, because her weekend taught her to — no end date. 'Sorted out' is not a date.

Marla is good people. That is not what the paper is asking.

**Choices:**
- Ask what 'sorted out' means, in dates, before anything is signed → **h1**
  - NOTE (shown after choosing): His answer is honest and useless: 'Until the assessment is complete and a plan is agreed.' The plan, recall, is the thing being disputed.
- Refuse flatly — no paper, no placement, no plan that wasn't agreed → **h1**
  - NOTE (shown after choosing): Refusal is also a posture, and the file already has a word for yours. The refusal will be answered procedurally, which is slower and colder than being answered personally.

## [h1] The Paper With No Date
*Day 10 — Tuesday, March 3, 2026 (dayOffset 10)*

Here is the fork, and it is a real one. Sign, and the children sleep at Marla's tonight under a paper with no end date, while the agency completes an assessment of a plan Cosette never agreed to. Decline, and the agency does by petition what the paper tried to do by signature: the children go to Marla's anyway tonight — as an emergency kinship placement — and a judge reviews it within days.

Both roads lead to Marla's couch. They differ in everything else: in what the file says Cosette chose, and in whether a court is watching the clock.

**Choices:**
- Sign — Marla's is safe, and fighting looks worse than agreeing → **h2sign**
  - NOTE (shown after choosing): Signed at 11 a.m. By noon the file reads 'mother agreed to voluntary placement.' Agreed is doing the same work 'disputes' did, in the other direction.
- Decline in writing — one line, dated: 'I do not agree to placement; the agreed terms were as stated Saturday' — and take the hearing → **h2decline**  _(FLAG: declinedInWriting ; FLAG: removed)_
  - NOTE (shown after choosing): It is the first paper of Cosette's in this file since Saturday, if the weekend's were never written — and it changes the legal weather: now there must be a hearing, quickly, with a judge and a lawyer for her in it.

## [h2sign] Marla's Couch
*Day 11 — Wednesday, March 4, 2026 (dayOffset 11)*

The children think it's a sleepover for exactly one evening. By the third, Caleb is asking questions with right angles. 'Sorted out' enters its second week without acquiring a date. The assessment proceeds at office pace. Cosette visits daily and is written up as 'engaged,' which she is, and 'compliant,' which is a word files use for people who signed.

On day twelve, a supervisor asks Venn why the children of a disputed errand report are still placed. Venn has no answer with a date in it. Neither, it turns out, does the paper Cosette signed — which is now the problem, in a system that runs on dates.

A review is scheduled — not a hearing, because she agreed, and agreement doesn't get hearings. It gets reviews.

**Choices:**
- Write, tonight, the demand the paper should have contained: return by a date, or a hearing — in writing → **h3a**  _(FLAG: returnDemanded)_
  - NOTE (shown after choosing): Late paper is weaker than early paper and stronger than no paper, which is the complete taxonomy. It goes in dated, and the review is now about a demand, not a mood.
- Wait for the review — surely they'll just send them home → **h3a**
  - NOTE (shown after choosing): Surely is not a scheduling system. The review will consider what's in the file, and the file contains a signature and a summary.

## [h2decline] The Knock, Again
*Day 11 — Wednesday, March 4, 2026 (dayOffset 11)*

That evening there is a second knock — the night they came twice, eight days later. The petition is granted over the phone by a judge Cosette never sees; the children go to Marla's as an emergency placement, with a hearing now required by law and a clock now running by law.

Caleb packs like a soldier. Cleo packs the list. Cosette stands in the doorway in her socks again, and this time she does one thing Saturday taught her — or didn't: she watches what she has to put in front of a judge within three days.

What a shelter care hearing hears is narrow: whether the children must remain out of the home while the case is decided. Narrow, and entirely about risk — which is to say, entirely about paper.

**Choices:**
- Call Marla tonight: the hearing is within days; the children need their routines, their beds' worth of normal, documented → **h3a**
  - NOTE (shown after choosing): Kinship placement is the system's least-bad door, and Marla holding it open matters. What matters next is what gets carried into the hearing room.
- Spend the night planning what you'll say to the judge → **h3a**
  - NOTE (shown after choosing): Saying is the smallest part of a hearing. Exhibits are the rest.

## [h3a] Counsel, in the Hallway
*Day 12 — Thursday, March 5, 2026 (dayOffset 12)*

The courthouse hallway smells of floor wax and other people's worst weeks. Cosette's lawyer — appointed, because counsel in these hearings is a right, not a luxury — has eleven minutes and a legal pad: 'Tell me what we have. Not what happened. What we have.'

The inventory is the whole game. Saturday's agreement lives in four possible exhibits: Gable's note (fair, and in the file), Cosette's verbatim lines from that night (if written), Mrs. Deveraux's statement (if gathered), and the summary that enlarged it all (in the file, on top). Two of those four were Cosette's to make. A hearing is where it is decided whether she made them.

The lawyer looks at whatever the folder holds and does arithmetic judges do.

**Choices:**
- Hand over everything the weekend produced — all of it, copies for counsel → **h3**
  - NOTE (shown after choosing): Whatever exists, exists. The hearing will now be about documents, which is the only terrain where Saturday can beat the summary.
- Explain Saturday fully, so counsel can argue it from the heart → **h3**
  - NOTE (shown after choosing): Heart is admissible nowhere. Counsel nods, writes 'client states she watched from window,' and the file's version remains the only version with a exhibit sticker.

## [h3] The Hearing
*Day 13 — Friday, March 6, 2026 (dayOffset 13)*

A shelter care hearing comes fast by law — within 72 hours of a removal (42 Pa.C.S. § 6332; 23 Pa.C.S. § 6315(d)) — and it feels like it: a small room, a tired judge, the agency's lawyer reading from the file's top page, which is the summary.

Cosette's counsel rises with whatever the folder held. If the weekend's paper exists — her own dated lines from Saturday night, and a neighbor's signed statement that she watched Cosette watch — the hearing has a second text to read, and judges read texts. If it doesn't, the hearing has her voice, raised in a small room, against a summary in a calm one.

The judge looks from the file to the folder, and rules on the paper in front of her.

**Choices:**
- Put the weekend's paper to the court: the same-night account and the neighbor's statement → **end_partial**  _(REQUIRES FLAG: notesWritten ; REQUIRES FLAG: neighborSeen)_
  - NOTE (shown after choosing): The judge reads both — actually reads, pen moving — and then reads Gable's note against the summary clipped to it. 'The note doesn't say what the summary says,' she observes, to no one in particular, which is how judges say it to everyone. The children are returned tonight — on the plan as filed: Venn's. Supervision terms, check-ins, a review in sixty days. Home, on their paper.
- Ask for a week — time to get the neighbor's statement and reconstruct Saturday's account properly → **h4**
  - NOTE (shown after choosing): Continuances at shelter care are measured in days and granted in reluctance. She gets until next week. The children stay at Marla's. The clock that was her right is now also her wait.
- Argue Saturday from memory — fully, fiercely, the way it deserves → **end_hard**
  - NOTE (shown after choosing): She does, and it deserves better than it gets: 'The court has the agency's documentation and the mother's testimony,' the judge says, in the formula that means the documentation weighed more. The placement continues. The plan as summarized stands. Adjudication will rehear it all — in weeks, on a file whose top page has not changed.

## [h4] One Week at Marla's
*Day 15 — Sunday, March 8, 2026 (dayOffset 15)*

The week is a workshop with one product: the paper that Saturday night and Sunday should have made. Mrs. Deveraux, located and willing, writes her six lines — the window, the eleven minutes, the broken television. Cosette reconstructs her account from texts she sent that night (two, timestamped, describing Gable's visit — better than memory, worse than a page written that night).

Counsel files both ahead of the continued hearing. Late paper, the taxonomy says: weaker than early, stronger than none. The question the judge will answer is whether it's strong enough to move a placement that has already settled into Marla's routines.

**Choices:**
- File both documents before the continued hearing — statement, reconstruction, and the confirmation letter for good measure → **end_partial**  _(FLAG: latePacket)_
  - NOTE (shown after choosing): The judge reads them in chambers this time. The ruling, when it comes, is the same shape as the week's: the children come home Thursday — on the plan as the agency filed it. Supervision terms, check-ins, a review in sixty days. The paper was strong enough to bring them home. It was not strong enough to change whose paper they came home under.
- Let counsel argue the reconstruction orally — filing feels like overkill now → **end_hard**
  - NOTE (shown after choosing): Oral reconstructions are summaries, and summaries are the other side's weapon, not yours. The judge continues the placement. 'The plan, continued,' she says, and the file closes over Saturday like water.

## [end_partial] Home, On Their Paper
*Day 18 — Wednesday, March 11, 2026 (dayOffset 18)*

**DEBRIEF:**

The children came home — that is not nothing; it is, in fact, the main thing — but they came home under the agency's paper, not the agreement as it was made Saturday: supervision terms, check-ins, a sixty-day review, 'mother disputes plan' in the margin of the family's file forever. PARTIAL WIN: the kinship door and the hearing did their work; the authorship was lost on the Saturday night it wasn't written down, or the Monday it was argued instead of handed over.

The verified law inside this ending: a shelter care hearing comes within 72 hours of removal (42 Pa.C.S. § 6332; 23 Pa.C.S. § 6315(d)), and counsel at it is a right (42 Pa.C.S. § 6337; § 6332(a)). The law gave Cosette a judge, a lawyer, and a clock. It could not give her the eleven lines from Saturday night. Only Saturday night could.

Notice what the judge did with paper when paper finally existed: she read Gable's note against its own summary and found the case in the gap. The gap was always there. It needed exhibits to become visible.

Honesty requires this: another judge weighs a neighbor's broken television differently, and Marla's couch could have become a placement of months if the assessment had found a second thing. Workers vary; judges vary; couches vary. What doesn't vary: hearings rule on the paper in front of them, and paper is made before hearings, or it is not made at all.

## [end_hard] The Plan, Continued
*Day 18 — Wednesday, March 11, 2026 (dayOffset 18)*

**DEBRIEF:**

The placement continued — not because a nine-year-old bought milk, but because at every decision point the file contained exactly one account of Saturday, and it wasn't Cosette's. The summary said 'supervised at all times' and 'petition,' and in the absence of any earlier paper, the summary simply became the plan, and the plan simply continued.

The verified law inside this ending: the shelter care hearing came within 72 hours, as the law requires (42 Pa.C.S. § 6332; 23 Pa.C.S. § 6315(d)), and Cosette had counsel (42 Pa.C.S. § 6337). The system's promises were kept. What failed was not the law; it was the evidence — a neighbor never asked for a statement, a night never written down, a confirmation never drafted. Hearings cannot weigh documents that don't exist.

Notice the sequence, because it is the whole lesson: the case was lost on Saturday night (unwritten), confirmed on Monday (argued instead of handed over), and merely announced at the hearing. By the time lawyers were in a room, the outcome was already in the file.

Honesty requires this: some judges dig, some workers correct their own summaries unprompted, and some cases like this end at the first visit. None of that was available to be counted on. The only version of Saturday that attends every meeting is the written one — and in this story, no one wrote it.
