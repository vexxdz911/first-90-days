# THE FIRST 90 DAYS — Scenario 24: “The Appeal Record”

*Human-readable script. This document and `scenario-24.json` are generated from a single source and match node-for-node: same IDs, same order, same choices, same effects.*

**The family is fictional — a composite. No real person's story appears here.**

**Content note:** This scenario depicts a dependency appeal told through transcripts, reviews, and paperwork — the proceeding itself, retold in flashback. There is no graphic content. Players may skip any scene or use the quick exit at any time.

**How to read effects:** `cash −40` changes the player's cash. `FLAG: name` sets a flag the engine tracks. `HIDDEN + item` means the case file quietly records that item at this choice — the player does not see it when it happens. `REQUIRES FLAG: name` means the choice is only available if that flag was set earlier; `REQUIRES NO FLAG: name` means it is only available if that flag was never set. `NOTE:` is text shown to the player right after choosing.

Start date: Monday, January 12, 2026. Day offsets are days since the scenario's start date.

## [start] The Order in the Mail
*Day 0 — Monday, January 12, 2026 (dayOffset 0)*

Your name is Mara Ellison. Your son Eli is eight. He has been living with a foster family since May 7, 2025, and learning — the way children do, faster than anyone wants — the geography of a second home.

Today's mail holds the next piece of paper: the court has ruled in Eli's dependency case, and your lawyer is filing an appeal. An appeal, she told you on the phone, is not a second hearing. Nobody new testifies. Nobody new explains.

An appeal is a reading. A panel of judges will read the record of what already happened — every word said, every paper offered, every silence — and decide whether the law was followed in the making of it. This story is about that reading, and about the days when the record was still being written.

**Choices:**
- Meet your appellate lawyer and learn what an appeal can actually reach → **lawyer_map**
  - NOTE (shown after choosing): Her office has three chairs, a kettle, and a shelf of bound transcripts like bricks.

## [lawyer_map] Ms. Okafor Draws Two Timelines
*Day 3 — Thursday, January 15, 2026 (dayOffset 3)*

Ms. Okafor, your appellate lawyer, draws two lines on a legal pad. The top line is the appeal: filings, briefs, argument, a decision — moving at the speed of paper.

The bottom line is Eli's case below, and it does not pause. Reviews will still be held. Visits will still happen or not happen. And the federal timeline keeps counting the months Eli has been in care: at fifteen of the most recent twenty-two months, the agency's duty about filing a termination petition changes, unless an exception is documented. (42 U.S.C. § 675(5)(E)) That date, on Eli's clock, is Friday, August 7, 2026.

"Two rules will run this whole story," she says. "The panel can only review what is in the record that was made below. And an issue nobody raised down there is, generally, an issue the panel will not reach up here. So before we argue about what the record means, we have to find out what the record is."

**Choices:**
- Ask what 'the record' includes, exactly → **boxes**
  - NOTE (shown after choosing): "Transcripts. Exhibits that were actually offered. Orders." She taps the pad. "Not memories. Not intentions. Paper and spoken words, preserved."
- Ask whether you can just explain it to the panel yourself → **boxes**
  - NOTE (shown after choosing): She is gentle about it. "That is the hardest part of an appeal. The explaining had a season. We are in the reading season now."

## [boxes] The Record Arrives in Boxes
*Day 10 — Thursday, January 22, 2026 (dayOffset 10)*

The certified record arrives the way weather arrives: in bulk, without apology. Two boxes of transcripts from the hearings last spring and summer, the agency's reports, the court's orders — the whole case, flattened into paper.

Ms. Okafor has a checklist. Transcripts can be ordered in full, and the agency's records can be requested — records in the agency's file are to be released on request. (55 Pa. Code § 3130.44(d)) Ordering the complete set costs money and takes weeks. Working from the excerpts the agency already provided costs nothing, and might skip the very pages the appeal will turn on.

Everything in this scenario turns on a version of this choice, made over and over: build the written record, or trust that somebody else did.

**Choices:**
- Order the complete transcripts and request the full agency record, in writing → **flash_shelter**  _(cash −35 ; FLAG: recordsRequested ; FLAG: transcriptOrdered ; HIDDEN + Transcripts — complete set ordered; agency record requested in writing)_
  - NOTE (shown after choosing): The receipt goes in your folder. Weeks from now, a page number you paid for will matter more than anything you could say out loud.
- Work from the agency's excerpts for now and save the money → **flash_shelter**
  - NOTE (shown after choosing): Ms. Okafor writes 'excerpts only' on the checklist and circles it, the way you circle a word you are not sure is spelled right.

## [flash_shelter] Flashback: The First Hearing
*Day 14 — reading the transcript — Monday, January 26, 2026 (dayOffset 14)*

FLASHBACK — Friday, May 9, 2025. You are reading the transcript now, in Ms. Okafor's office, but the words are yours, spoken when Eli had been in care for two days.

The shelter care hearing came quickly, because the law makes it come quickly: an informal hearing not later than 72 hours after a child is placed in shelter care. (42 Pa.C.S. § 6332; 23 Pa.C.S. § 6315(d)) Before it began, the court told you what Ms. Okafor underlines now: you had the right to counsel, and to appointed counsel if you could not afford one. (42 Pa.C.S. § 6337) Your trial lawyer, Mr. Bennett, sat beside you smelling faintly of courthouse coffee.

The agency asked that Eli stay placed while things were sorted out. Mr. Bennett said one sentence Ms. Okafor has marked with a sticky note: "For the record, my client's mother — Eli's grandmother, Mrs. Doyle — is in the hallway and is willing to be assessed as a placement today." Then the hearing moved on.

**Choices:**
- In the flashback: that sentence was enough — let the hearing move on → **flash_shelter_after**  _(FLAG: kinshipOnRecord ; HIDDEN + Transcript — grandmother named on the record at shelter care as a placement resource)_
  - NOTE (shown after choosing): One sentence. It will still be sitting in the transcript, exactly there, on the day the panel reads it.
- In the flashback: assume the caseworker will note grandmother's name in her own file → **flash_shelter_after**
  - NOTE (shown after choosing): She meant to. Caseworkers mean to write down many things. The transcript only keeps what was said out loud, in the room.

## [flash_shelter_after] What a Sentence Can Carry
*Day 17 — reading the transcript — Thursday, January 29, 2026 (dayOffset 17)*

Ms. Okafor closes that transcript. "People think a record is a summary of a case," she says. "It isn't. It's the case, for anyone who wasn't in the room. The panel wasn't in the room."

She opens the next volume — the adjudication hearing, Monday, June 2, 2025 — and her sticky notes multiply. "This," she says, "is the day the appeal was mostly written. You just didn't know it yet."

**Choices:**
- Turn the page into the adjudication hearing → **first_read**
  - NOTE (shown after choosing): Your own handwriting is in the margin of your copy, from last summer: 'long day.' It was.

## [first_read] How to Read a Transcript
*Day 20 — reading the transcript — Sunday, February 1, 2026 (dayOffset 20)*

Ms. Okafor teaches you to read the way the panel will: not for story, but for rulings. Every 'Objection' is a door someone built. Every 'Admitted' without one is a wall. Speaker labels, page numbers, the clerk's timestamps — the transcript is not a summary of the hearing. For everyone who was not in the room, it replaces the hearing.

"You were there," she says, "so your memory will keep volunteering. The panel doesn't have your memory. They have this. When the two disagree about what the case is, this wins."

**Choices:**
- Open the adjudication transcript → **flash_adjud**
  - NOTE (shown after choosing): June of last year, in type. Your handwriting is not in this margin. It will be, in pencil, by day 24.

## [flash_adjud] Flashback: The Exhibit
*Day 24 — reading the transcript — Thursday, February 5, 2026 (dayOffset 24)*

FLASHBACK — Monday, June 2, 2025. The adjudication hearing. The agency's lawyer offers a packet: the caseworker's report, with a one-page scored assessment form summary stapled to the back — a form that sorts Eli's case into categories and a score band, with no one in the room who filled it out.

The judge looks at Mr. Bennett. This is the moment Ms. Okafor has read four times. "Everything in an appeal," she says quietly, over the transcript, "is either side of this moment. If your lawyer objects — objects to the summary coming in without anyone to answer questions about it — the objection, and the judge's ruling, are in the record forever, and the panel can reach them. If nobody objects, the page comes in like weather, and the moment passes out of the record's reach."

You are back in that chair. Mr. Bennett is looking at the packet. The judge is looking at Mr. Bennett.

**Choices:**
- OBJECT — "Objection. The summary should not come in without a witness who can be questioned about it." → **obj_made**  _(FLAG: preservedObjection ; HIDDEN + Transcript — objection to assessment summary made and ruled on at adjudication)_
  - NOTE (shown after choosing): The judge hears argument and rules. Win or lose the ruling, the objection now exists where appeals live: on the record.
- Stay silent — the judge has seen a hundred of these packets; objecting feels like making a scene → **obj_silent**
  - NOTE (shown after choosing): The packet is admitted without discussion. The hearing moves to the next witness. Nothing in the transcript marks the moment at all.

## [obj_made] The Line in the Transcript
*Day 24 — reading the transcript — Thursday, February 5, 2026 (dayOffset 24)*

On the page, it takes four lines: the objection, the agency's answer, the judge's ruling admitting the summary anyway, and Mr. Bennett's "Note my exception" — old-fashioned words that mean: this is preserved.

Ms. Okafor exhales. "The panel may agree with the ruling or not," she says. "But they can reach it. That is the difference between an argument and a regret."

**Choices:**
- Keep reading — the agency rests its case → **flash_exhibit**

## [obj_silent] The Page Where Nothing Happens
*Day 24 — reading the transcript — Thursday, February 5, 2026 (dayOffset 24)*

On the page, the packet is simply "admitted." No objection, no argument, no ruling to examine. Ms. Okafor turns the transcript page slowly, as if the moment might be hiding under it.

"I want to be honest with you," she says. "We can still describe this page in a brief. But an appellate panel reviews rulings. Where there is no objection, there is usually no ruling — and generally, nothing for them to reach. We'll build what we can from the rest of the record."

**Choices:**
- Keep reading — your side of the case is next → **flash_exhibit**

## [flash_exhibit] Flashback: The Folder in Your Lap
*Day 31 — reading the transcript — Thursday, February 12, 2026 (dayOffset 31)*

FLASHBACK — later the same hearing day, Monday, June 2, 2025. Your side of the case. In your lap that day was a folder: your treatment-completion certificate, your work schedule, and a letter from Eli's pediatrician about his asthma care at your home — the inhaler log you kept on the refrigerator, in your careful handwriting.

An exhibit only enters the record if it is offered — handed up, marked, and admitted or refused on the record. A folder in a lap is not an exhibit. A letter at home is not an exhibit. Ms. Okafor's voice, over the transcript: "Watch your hands in this part. Whatever they did is what the panel gets."

**Choices:**
- OFFER the folder — ask Mr. Bennett to hand up the certificate, the schedule, and the pediatrician's letter → **offer_made**  _(FLAG: exhibitInRecord ; HIDDEN + Exhibits — treatment certificate, work schedule, pediatrician letter offered and marked at adjudication)_
  - NOTE (shown after choosing): The clerk marks them. The judge admits two and takes the letter under advisement — but offered is offered: they are in the record now, numbered, permanent.
- Hold the folder — the judge seems impatient, and the letter feels thin compared to the agency's packet → **offer_held**
  - NOTE (shown after choosing): The folder goes home in your bag. The hearing ends without it ever being mentioned. The transcript does not know it existed.

## [offer_made] Marked and Numbered
*Day 31 — reading the transcript — Thursday, February 12, 2026 (dayOffset 31)*

Respondent's Exhibits 1 through 3. In the transcript they are only numbers; in the boxes in Ms. Okafor's office they are the actual pages, stamped and filed.

"When we write the brief," she says, "we will cite these by page. A panel can hold them. That is what 'support in the record' means — not that something was true, but that it is there, where they are allowed to look."

**Choices:**
- Keep reading — the last witness decision of the day → **flash_testify**

## [offer_held] What the Record Doesn't Know
*Day 31 — reading the transcript — Thursday, February 12, 2026 (dayOffset 31)*

"Can we send the panel the letter now?" you ask. Ms. Okafor shakes her head, not unkindly. "An appeal is decided on the record that was made below. A letter that was never offered isn't in it. Sending it now doesn't put it in — it just proves it existed, somewhere the panel can't use."

She turns the page. "One more decision that day is in here. The biggest one, for a lot of parents."

**Choices:**
- Keep reading — whether to testify → **flash_testify**

## [flash_testify] Flashback: Your Name Is Called
*Day 38 — reading the transcript — Thursday, February 19, 2026 (dayOffset 38)*

FLASHBACK — the end of the adjudication hearing. Mr. Bennett leans over: "You can testify, or you can rest on the agency's evidence. Testifying puts your account — the inhaler log, the work shifts, who was home that week — into the record in your own words, where the panel can read it. It also means cross-examination, and every answer is permanent. Resting means the only account in the transcript is the agency's."

There is no safe choice here. There is only the choice whose consequences you understand. Ms. Okafor, over the page: "Whatever you did, we're about to read it."

**Choices:**
- TESTIFY — tell it in your own words, and take the cross-examination → **testified**  _(FLAG: parentTestified ; HIDDEN + Transcript — parent testified at adjudication; account of care and work schedule on the record)_
  - NOTE (shown after choosing): It is not smooth. It is sworn, specific, and yours — dates, times, the refrigerator log. The cross is hard and also permanent, in both directions.
- REST — do not testify; the agency should have to prove its case on its own evidence → **rested**
  - NOTE (shown after choosing): A principled choice, and a real one — the burden was the agency's. But silence is also a record: the transcript's only narrative of that week is theirs.

## [testified] Your Voice, in Type
*Day 38 — reading the transcript — Thursday, February 19, 2026 (dayOffset 38)*

Reading your own testimony is strange: your sentences, flattened into transcript type, with "(pause)" where you cried.

"Panels read this," Ms. Okafor says. "Not to decide if they like you. To decide what the trial court had in front of it. Your account was in front of it. That widens what we can argue — and it means we argue from the record, not around it."

**Choices:**
- Close the adjudication transcript → **inventory**

## [rested] The Quiet Pages
*Day 38 — reading the transcript — Thursday, February 19, 2026 (dayOffset 38)*

The transcript ends your case in two lines: counsel rests; the court takes the matter under advisement.

"We work with the record we have," Ms. Okafor says. "Resting protected you from cross. It also means that when the panel looks for your account of that week, the chair is empty. Both of those are true at once. That's most of appellate law, honestly."

**Choices:**
- Close the adjudication transcript → **inventory**

## [inventory] The Inventory
*Day 45 — Thursday, February 26, 2026 (dayOffset 45)*

Ms. Okafor makes the inventory on the legal pad, in two columns: IN THE RECORD / NOT IN THE RECORD. Everything the flashbacks decided sits in one column or the other. The brief can only be built from the left-hand column.

"One more volume," she says. "Disposition — Monday, June 30, 2025. And then we stop reading the past and go watch the present, because Eli's case below is having a review next week, appeal or no appeal."

**Choices:**
- Read the disposition transcript first → **flash_dispo**
  - NOTE (shown after choosing): The disposition hearing decided where Eli would live and what the plan would be. Appeals reach backward to it, too.

## [flash_dispo] Flashback: Disposition and the Plan
*Day 52 — reading the transcript — Thursday, March 5, 2026 (dayOffset 52)*

FLASHBACK — Monday, June 30, 2025. At disposition, the agency presents the family service plan and recommends Eli remain placed, with visits at the agency office. Its report mentions grandmother only as "a relative expressing interest" — no name, no assessment date.

Mr. Bennett can object and ask the court to order the kinship assessment of Mrs. Doyle on the record, with the plan corrected — or he can raise it informally with the caseworker in the hallway afterward, where hallway agreements live and die.

**Choices:**
- OBJECT and ask, on the record, for grandmother's assessment to be ordered and the plan corrected → **dispo_object**  _(FLAG: preservedDispo ; HIDDEN + Transcript — disposition objection; kinship assessment of grandmother ordered on the record)_
  - NOTE (shown after choosing): The judge orders the assessment and says the plan will be corrected in writing. It is now a ruling — reachable, enforceable, real.
- Handle it in the hallway — the caseworker promises to "get grandmother assessed soon" → **dispo_hallway**
  - NOTE (shown after choosing): She meant it, probably. Hallway promises are not rulings. Nothing in the transcript will ever mention it.

## [dispo_object] A Ruling, Not a Promise
*Day 52 — reading the transcript — Thursday, March 5, 2026 (dayOffset 52)*

Ms. Okafor adds a line to the left-hand column. "This one matters twice," she says. "Up here, it's a preserved issue. Down below, it's an order the agency actually has to follow while the appeal crawls. The record isn't only for judges. It's how anything gets done."

**Choices:**
- Go to Eli's review hearing below — the present tense resumes → **review_below1**

## [dispo_hallway] Soon, Unwritten
*Day 52 — reading the transcript — Thursday, March 5, 2026 (dayOffset 52)*

The assessment, the transcript suggests, was still 'being scheduled' at the next two reviews.

"Soon," Ms. Okafor says, "is the saddest word in a case file. It never has a date attached." She closes the last volume. "Now — the present. Eli's review is Thursday, and the judge below has never heard of our appeal strategy and is not required to care."

**Choices:**
- Go to Eli's review hearing below → **review_below1**

## [review_below1] Meanwhile, Below: The Review
*Day 60 — Friday, March 13, 2026 (dayOffset 60)*

The review hearing below is smaller and faster than you remembered from inside the flashbacks — because this time you are watching the record being made, in real time, with Ms. Okafor's two columns in your head.

Your progress is reported: treatment done, work steady, visits kept. The caseworker reports grandmother's assessment is 'in process.' The judge continues Eli's placement and sets the next review. Nothing about the appeal is mentioned. The appeal does not stop this room; this room does not wait for the appeal.

You can hand the judge a short written summary of your progress — dated, with the certificates attached — so it enters this record too, or you can let the caseworker's oral report carry it.

**Choices:**
- Hand up the written summary with certificates attached, and ask that it be filed → **work_shifts**  _(cash −10 ; FLAG: reviewRecord ; HIDDEN + Review record — parent's written progress summary filed at review during appeal)_
  - NOTE (shown after choosing): The clerk stamps it. Below, as above: paper filed is paper that exists.
- Let the oral report carry it — the caseworker said it all anyway → **work_shifts**
  - NOTE (shown after choosing): She said most of it. The transcript of this review will keep her version, at her length, in her words.

## [work_shifts] Two Courts, One Work Schedule
*Day 66 — Thursday, March 19, 2026 (dayOffset 66)*

The appeal's least legal problem is its most human one: everything happens at 10 a.m. on weekdays, in two different buildings, and your shifts are also on weekdays. Your supervisor, who has covered for you twice, starts a sentence with 'Company policy…' and you hear the third covering become a different conversation.

Ms. Okafor cannot fix this and does not pretend to. "Put every request in writing," she says, "to your job and to the courts. If a date ever has to move, the side with the paper trail about asking moves it." Another record. They are all another record.

**Choices:**
- Put the schedule requests in writing, to work and to both courts → **gap_pages**  _(FLAG: schedulePaper ; HIDDEN + Schedule — court-date accommodation requests made in writing)_
  - NOTE (shown after choosing): Three short letters. The folder gains a section you never wanted and will absolutely need.
- Handle it by phone — people have been understanding so far → **gap_pages**
  - NOTE (shown after choosing): So far is a tense. The letters would have been a record; the calls are a memory, held by people whose job is not to hold it.

## [gap_pages] The Missing Forty Pages
*Day 74 — Friday, March 27, 2026 (dayOffset 74)*

Bad news in a thin envelope: the transcript set is incomplete. Forty pages of the disposition hearing — the part with the plan discussion — were never transcribed, and the agency's excerpt packet skips the same stretch.

Ms. Okafor is calm. The missing pages can be ordered and the record corrected — that is paperwork, and paperwork can be done. The agency's own file can also still be requested in full; agency records are released on request. (55 Pa. Code § 3130.44(d)) Both take time the briefing clock will feel. Skipping them means arguing the disposition issue from memory — hers, yours, anyone's. Appeals do not run on memory.

**Choices:**
- Order the missing transcript pages and renew the written request for the complete agency file → **brief_draft**  _(cash −20 ; FLAG: recordsRequested ; FLAG: recordComplete ; HIDDEN + Record — missing disposition pages ordered; complete agency file requested in writing)_
  - NOTE (shown after choosing): It costs weeks and dollars. It buys the only currency the panel accepts: pages.
- Brief around the gap — argue the disposition point from the excerpts you have → **brief_draft**
  - NOTE (shown after choosing): Ms. Okafor writes 'gap — disposition' in the margin of the draft, in pencil, the way you mark a place you may fall through.

## [brief_draft] The Brief Takes Shape
*Day 92 — Tuesday, April 14, 2026 (dayOffset 92)*

The draft brief comes back with Ms. Okafor's marginalia. The arguments are sorted the way panels sort them: what was preserved and is in the record goes in the front, argued fully, with page citations. Anything else — however true, however unfair it felt — can only be described, not argued, because a panel reviews the record made below and generally will not reach an issue that was never raised there.

She asks you to read it and mark anything factually wrong. "Your job now," she says, "is accuracy. Mine is architecture. The record's job is everything else."

**Choices:**
- Read it line by line against the transcripts, checking every page citation → **appendix_beat**  _(FLAG: briefChecked ; HIDDEN + Brief — every citation checked against the certified record)_
  - NOTE (shown after choosing): Slow, unglamorous, decisive. Two citations were wrong. Now they aren't.
- Skim it and sign off — she does this for a living → **appendix_beat**
  - NOTE (shown after choosing): She does. The brief goes out with two citations pointing at pages that say something adjacent to, but not quite, the point.

## [appendix_beat] The Appendix Fight
*Day 100 — Wednesday, April 22, 2026 (dayOffset 100)*

Ms. Okafor holds up two binders. The thin one is the certified record — the official set, the only set the panel is bound to treat as existing. The thick one is the reproduced record, the excerpts your side prints for convenience, which may contain anything — and proves nothing by containing it.

"A document that lives only in the thick binder," she says, "is, to the panel, a rumor with a tab. I have read decisions that say it in almost those words: what is not in the certified record is treated as non-existent, and stapling it into your own appendix does not cure that." She checks, one by one, that every page the brief cites is in the thin binder — or the citation comes out.

**Choices:**
- Check every cited page against the certified record, line by line → **visits_below**  _(FLAG: certifiedChecked ; HIDDEN + Brief — all citations verified against the certified record, not the appendix)_
  - NOTE (shown after choosing): One beloved page is appendix-only. It comes out of the brief, and Ms. Okafor's face does the arithmetic of a lawyer who has seen this exact page sink an appeal before.
- Trust the appendix — the pages are real, whoever bound them → **visits_below**
  - NOTE (shown after choosing): The pages are real. Reality, in this building, is a property conferred by certification, not by existence.

## [visits_below] Visits, in the Present Tense
*Day 110 — Saturday, May 2, 2026 (dayOffset 110)*

Eli has grown an inch during the appeal. He shows you, standing against the agency office doorframe where other children's heights are penciled — a whole archive of other people's children, in graphite.

Visits are the part of the bottom timeline that does not feel like paperwork, which is exactly why the paperwork about them matters: the visit log is a record too, and it is being written every week, by whoever holds the pen.

**Choices:**
- Ask, in writing, for the visit log to note today's make-up visit and Eli's school award → **eli_school**  _(FLAG: visitLog ; HIDDEN + Visit log — make-up visit and school award noted in writing)_
  - NOTE (shown after choosing): The worker adds it while you watch. A good week, on paper, where good weeks count.
- Just enjoy the visit — not everything needs to be a document → **eli_school**
  - NOTE (shown after choosing): Both things are true. Only one of them will be in the file at the next review.

## [eli_school] The School Report, Meanwhile
*Day 120 — Tuesday, May 12, 2026 (dayOffset 120)*

Eli's teacher sends a note through the foster parents: his reading has jumped a level; he told the class his mom is 'working with the judges.' The foster mother, Mrs. Ito, passes it along promptly and without commentary, which you have learned is her form of kindness — the file gets the fact, not her feelings about the fact.

Below, this goes into a school record the next review will see. Above, it goes nowhere — it postdates the record, and the panel reviews the record that was made below, not the boy's spring. Holding both of those truths at once, without letting either erase the other, is the emotional arithmetic of an appeal.

**Choices:**
- Thank Mrs. Ito, and file the teacher's note with the case below where it belongs → **argument_prep**
  - NOTE (shown after choosing): In the right binder, at last: the present-tense one, where the boy's spring is exactly what the next hearing is about.
- Ask Ms. Okafor to send it to the panel anyway — they should know → **argument_prep**
  - NOTE (shown after choosing): She explains, once more, gently: sending it doesn't put it in the record. Knowing why is most of what she's for.

## [argument_prep] Preparing for Questions
*Day 132 — Sunday, May 24, 2026 (dayOffset 132)*

Argument prep is Ms. Okafor reading the panel's likely questions aloud in a kind voice that does not soften them: "Counsel, where in the record was that objected to?" "Counsel, where is that exhibit?" "Counsel, what ruling are we being asked to reverse?"

Every question is the same question, really: show me the page. The appeal you have is the set of pages you can answer with.

**Choices:**
- Practice answering each question with a page number → **asfa_packet**
  - NOTE (shown after choosing): Where a page exists, the answer is short. Where one doesn't, the silence in the practice room is the whole lesson.
- Ask her to lead with fairness — the panel should hear how it felt → **asfa_packet**
  - NOTE (shown after choosing): "They should," she says, "and the way they hear it is through the record. Feeling travels on paper or it doesn't travel."

## [asfa_packet] The Other Clock, Up Close
*Day 152 — Saturday, June 13, 2026 (dayOffset 152)*

The bottom timeline arrives on paper: a notice that Eli's case is approaching fifteen months in care, on Friday, August 7, 2026. The agency's filing duty changes then — unless an exception is documented: Eli being cared for by a relative, a documented compelling reason a termination filing would not serve him, or services the agency was required to provide but did not. (42 U.S.C. § 675(5)(E))

Exceptions, Ms. Okafor reminds you, are not hopes. They are documents. Your lawyer below can submit a packet now — grandmother's status, your completed services, the visit record — asking that an exception be documented in the file, or the packet can be 'mentioned' at the next review and live the way hallway promises live.

**Choices:**
- Build and file the written exception packet below, with grandmother's status and your service record attached → **review_below2**  _(cash −10 ; FLAG: compellingPacket ; HIDDEN + ASFA — written exception packet filed below before the fifteen-month date)_
  - NOTE (shown after choosing): Stamped, filed, dated before the clock strikes. Whatever the agency decides, it will have to decide about a document.
- Raise it orally at the next review — the judge already knows your progress → **review_below2**
  - NOTE (shown after choosing): The judge knows a version of it. The file will know the caseworker's version of the review. Those are not the same knowledge.

## [review_below2] Meanwhile, Below: Another Review
*Day 160 — Sunday, June 21, 2026 (dayOffset 160)*

The review below has its own weather. Eli is doing well in placement — a fact that helps him and complicates you, and the judge says both halves of that sentence out loud, to the record, which is more honesty than the system always manages.

Your packet is in the file. The agency reports the kinship assessment complete and the exception question 'under review at the agency level' — a phrase with no date attached, sitting next to your packet, which has several. The judge continues placement, notes the pending appeal in one sentence, and moves to the next case on the list. Two courts, one boy, no pauses anywhere.

**Choices:**
- Ask your lawyer below to press for a date on the exception decision — in writing → **the_wait**
  - NOTE (shown after choosing): A date, requested in writing, answered or not. Either way, the asking joins the record.
- Accept 'under review' — pressing might annoy the agency → **the_wait**
  - NOTE (shown after choosing): It might. Silence has annoyed no one in this case so far, and has accomplished roughly the same amount.

## [the_wait] The Court's Calendar
*Day 168 — Monday, June 29, 2026 (dayOffset 168)*

Two messages arrive the same week. The appellate court offers an argument date — and it is close, and Ms. Okafor is ready, and the brief is the brief the record allows. Separately, Eli's next review below is set, and life, which has not consulted either court, schedules your work shifts across both.

The appellate court's calendar also holds a later slot — months later, past August 7, 2026. Taking it would be easier on everyone's schedule. It would also mean the bottom timeline reaches its date while the top timeline is still waiting to be heard.

**Choices:**
- Take the first argument date — argue the appeal before the other clock strikes → **argument_day**
  - NOTE (shown after choosing): Ready or not, the record is what it is — and it is not getting longer. That, in the end, is the point of it.
- Take the later, easier slot — months from now, when work is calmer → **end_pending**
  - NOTE (shown after choosing): The confirmation letter is polite and routine. So is the other letter it will eventually cross in the mail.

## [argument_day] Argument Day
*Day 183 — Tuesday, July 14, 2026 (dayOffset 183)*

The courtroom up here is quiet in a different way: no witnesses, no Eli, no folder in your lap. Three judges, a clock, and the record — two boxes, now tabbed and cited, sitting on counsel's table like the case's skeleton.

Ms. Okafor rises. What she can argue — really argue, with pages — depends entirely on what those boxes contain. She looks at the tabs, and chooses her lead.

**Choices:**
- Ms. Okafor makes the argument the record allows → **decision_wait**
  - NOTE (shown after choosing): Twenty-five minutes. Three judges, a dozen questions, and every answer she gives is a page number or an honest silence.

## [decision_wait] Counsel Rises
*Day 190 — Tuesday, July 21, 2026 (dayOffset 190)*

The argument itself takes twenty-five minutes, and it is built — visibly, audibly — out of the boxes. Each of the panel's questions lands on a page or on an absence. Ms. Okafor answers the ones the record lets her answer, concedes the ones it doesn't with a steadiness you recognize as its own kind of advocacy, and sits down.

What happens next will happen in writing, in weeks, in a room you will never see. What it can contain was decided by which lead was available to her when she stood up.

**Choices:**
- Lead with the preserved objection AND the offered exhibits — 'The objection is at page 112; the exhibits the court had are Respondent's 1 through 3.' → **end_remand**  _(REQUIRES FLAG: preservedObjection ; REQUIRES FLAG: exhibitInRecord)_
  - NOTE (shown after choosing): This argument exists because the objection was made and the folder was offered. Both sentences are literally true.
- Lead with the preserved objection alone — the ruling was wrong even without the exhibits → **end_mixed**  _(REQUIRES FLAG: preservedObjection)_
  - NOTE (shown after choosing): This argument exists because the objection was made. It is narrower, and the panel hears the narrowness.
- Try to lead with the assessment summary anyway — object now, on appeal, for the first time → **end_affirmed**  _(REQUIRES NO FLAG: preservedObjection)_
  - NOTE (shown after choosing): This is the only lead left when the moment passed in silence below. The panel's first question is already on the practice-room wall.
- Ask the panel to consider the pediatrician's letter, which is in your bag, as it was in your lap → **end_affirmed**  _(REQUIRES NO FLAG: exhibitInRecord)_
  - NOTE (shown after choosing): The letter is real. It is also, in the only sense this room recognizes, not here.

## [end_remand] Remand — The Argument That Existed
*Day 200 — Friday, July 31, 2026 (dayOffset 200)*

The panel's decision arrives as a document, the way everything in this story arrives. On the preserved issue, the court agrees: the scored assessment summary should not have been admitted the way it was, on a record that gave the trial court — and you — no one to question about it. The adjudication order is vacated and the case is remanded: sent back below for a new hearing, on a proper record.

Read it twice, the way Ms. Okafor taught you. It does not say Eli comes home. It does not say the agency was wrong about everything. It says the argument that existed — because an objection was spoken and a folder was offered on a day last summer — was reached, and it was right, and the case must be done again, correctly.

Eli is told, in words for an eight-year-old, that there will be another hearing. His placement continues until there is. The bottom timeline did not stop for any of this — but the packet you filed is in the record below, dated before August 7, 2026, and it will be on the table at the new hearing too.

**Ending.**

**Debrief:**
- THE BOARD, MAPPED — Appeal track: argued on Tuesday, July 21, 2026 and decided on Friday, July 31, 2026, before the fifteen-month date of Friday, August 7, 2026. The decisive argument was reachable only because two flashback choices built it: the objection (flag: preservedObjection) created a ruling to review, and the offered exhibits (flag: exhibitInRecord) gave the panel the parent's evidence in citable form. The complete transcripts and agency record (flag: recordsRequested) are what let the brief cite pages instead of memories.
- Placement/review track below: reviews continued throughout the appeal; Eli remained placed; the written progress summary and visit log entries (flags: reviewRecord, visitLog) are the record the new hearing will start from. ASFA track: Eli reaches fifteen of twenty-two months on Friday, August 7, 2026; the filed exception packet (flag: compellingPacket) means any filing decision must reckon with a documented exception claim — relative care, a documented compelling reason, or services not provided (42 U.S.C. § 675(5)(E)) — rather than with silence.
- What was never in your control: the panel's reading of the ruling, the trial judge's original decision to admit the summary, the appellate calendar, and the pace of the new hearing. A remand is a second chance at a fair process, not a verdict on your worth as a parent — outcomes in this system also turn on workers, judges, and luck, and this one turned on something narrower and more durable than luck: words spoken at the right moment, in the room, on the record.

## [end_mixed] Split — One Door Open, One Closed
*Day 200 — Friday, July 31, 2026 (dayOffset 200)*

The decision splits, the way Ms. Okafor warned you decisions do. On the preserved objection, the panel agrees the assessment summary was admitted without a proper foundation and that part of the order cannot stand. On everything that would have given the argument its full force — the exhibits that were never offered, the account that exists only in the agency's telling — the panel has nothing before it to review, and says so, in the courteous language courts use for locked doors.

The case goes back below on the one issue, and continues on all the others. Eli's placement continues under the parts of the order that were affirmed. There will be another hearing, narrower than a fresh start and wider than nothing.

**Ending.**

**Debrief:**
- THE BOARD, MAPPED — Appeal track: argued Tuesday, July 21, 2026, decided Friday, July 31, 2026. One issue was reached and won because it was preserved (flag: preservedObjection); the rest of the appeal ran aground on the empty places — an exhibit never offered is not in the record, and a panel reviews the record that was made below. That is the whole mechanics of this ending: one door was built in the flashbacks, and only that door opened.
- Placement/review track below: Eli remained placed through every review held during the appeal; the case below never paused. ASFA track: the fifteen-month date is Friday, August 7, 2026. Whether a documented exception is in the file (flag: compellingPacket, if you filed the packet) now decides how much room the case below has; if it was only raised orally, the file holds the agency's version of that conversation.
- What was never in your control: how the panel weighed the one preserved issue, the trial court's rulings, the calendars of two courts at once. A split outcome is not a grade on your parenting. It is an exact map of a record — what was built in time, and what was not — and outcomes here also turn on workers, judges, and luck.

## [end_affirmed] Affirmed — The Empty Chair
*Day 200 — Friday, July 31, 2026 (dayOffset 200)*

The decision is short, and its shortness is the story. Again and again, the panel's answer is the practice-room question: where was this raised below? The assessment summary came in without objection, so there is no ruling to reverse. The letter was never offered, so it is not in the record the panel may review. Issue by issue, the appeal does not lose on the merits. It is never reached at all.

The order below is affirmed. Eli's case continues in the court that has always held it — reviews, plans, visits — under the order as written. Ms. Okafor puts the decision in your folder, on top. "The next record," she says, "starts at the next review. It is always being written. That part is still yours."

**Ending.**

**Debrief:**
- THE BOARD, MAPPED — Appeal track: argued Tuesday, July 21, 2026, decided Friday, July 31, 2026, affirmed. The record showed: no objection at the decisive moment (no preservedObjection flag), so no ruling existed for the panel to examine; any exhibit never offered (no exhibitInRecord flag) was outside the certified record, however real it was in a lap or a kitchen. Appellate courts review the record made below, and unpreserved issues are generally not reached — this ending is that principle, experienced from the inside.
- Placement/review track below: reviews continued all along, unaffected by the appeal; Eli remained placed, and the affirmed order governs the case going forward. ASFA track: Eli reaches fifteen of twenty-two months on Friday, August 7, 2026; from here the fight moves entirely to the court below — including whether a documented exception under 42 U.S.C. § 675(5)(E) is in the file when the agency weighs a termination filing, where the agency would still have to prove its grounds clearly and convincingly.
- What was never in your control: the panel's hands were tied by the same record that tied yours; the original rulings, the other lawyer's choices that day, and the calendars were never yours either. This outcome measures a transcript, not a mother. Outcomes in this system also turn on workers, judges, and luck — and the record of the next hearing, unlike the last one, has not been written yet.

## [end_pending] Still Pending — The Other Clock Struck First
*After the date — Saturday, August 29, 2026 (dayOffset 229)*

The later slot was easier on everyone's schedule. That part was true. The rest arrived by mail, in two envelopes, eleven days apart.

First, the notice from below: Eli has now been in care for fifteen of the most recent twenty-two months — the date was Friday, August 7, 2026 — and the agency has filed the petition the federal timeline points it toward, the exception question to be argued from whatever the file holds. A petition is not a termination; the agency would still have to prove its grounds clearly and convincingly at a hearing. But the weather of the case below has changed, permanently, while the appeal was still waiting for its morning in court.

Second, the appellate court's scheduling letter, setting argument — finally — for next month. Two timelines, drawn on one legal pad in January. The bottom one reached its date first.

**Ending.**

**Debrief:**
- THE BOARD, MAPPED — Appeal track: still pending at Saturday, August 29, 2026; no decision, no ruling on any issue — preserved or not, the record's contents (flags: preservedObjection, exhibitInRecord, recordsRequested, if set) still wait, intact, for a panel that has not yet read them. Nothing about the appeal was lost except time, and time turned out to be the one thing the other track was counting.
- Placement/review track below: reviews continued throughout; Eli remained placed; his case acquired, on Friday, August 7, 2026, a termination petition that will now run on its own track, in its own court, whether or not the appeal later succeeds — a successful appeal could still unsettle the orders beneath it, but it does not un-file a petition or un-run a clock. ASFA track: struck on schedule at fifteen of twenty-two months (42 U.S.C. § 675(5)(E)); whether a documented exception was in the file (flag: compellingPacket) is now the first argument in the case below.
- What was never in your control: the appellate court's calendar was never yours — the choice here was only which slot to accept, inside a system that set both. Judges' schedules, workers' filings, and luck all moved on their own tracks. This ending is not a judgment on your worth; it is a collision between two clocks, only one of which ever claimed to be waiting for you.
