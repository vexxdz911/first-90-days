# THE FIRST 90 DAYS — Scenario 81: “The Month-by-Month Ledger”

*Human-readable script. This document and `scenario-81.json` are generated from a single source and match node-for-node: same IDs, same order, same choices, same effects.*

**The family is fictional — a composite. No real person's story appears here.**

**Content note:** This scenario depicts a permanency timeline — reviews, a possible termination-petition filing decision, and paperwork. There is no graphic content. Players may skip any scene or use the quick exit at any time.

**How to read effects:** `cash −40` changes the player's cash. `FLAG: name` sets a flag the engine tracks. `HIDDEN + item` means the case file quietly records that item at this choice. `REQUIRES FLAG: name` means the choice is only available if that flag was set earlier.

Start date: Monday, December 2, 2024. Day offsets are days since the scenario's start date (the child's foster-care entry date).

## [start] The Clock You Cannot See
*Day 0 — Monday, December 2, 2024 (dayOffset 0)*

Your name is Mireille. Your child Keiko, 8, has been in foster care since the date the court set — and a second calendar started that day, one nobody handed you a copy of.

Fifteen of the most recent twenty-two months. That is the federal permanency clock (42 U.S.C. § 675(5)(E)), and this story is the fifteen months, played honestly: fifteen months of small documented facts that either add up to an exception or add up to nothing. Keiko keeps a paper chain in her foster home — one loop for every visit — and refuses to let anyone throw it away.

**Choices:**
- Do the paper version: dated, copied, filed → **map**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the case record)_
  - NOTE (shown after choosing): Another dated page joins the folder.
- Handle it with a conversation and move on → **map**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [map] The Lawyer Draws the Clock
*Day 13 — Sunday, December 15, 2024 (dayOffset 13)*

Your lawyer draws one line: Keiko's months in care, counted from the entry date. At month fifteen the agency's duty about filing a termination petition changes — unless an exception is documented.

She underlines one word three times: documented. Progress the file cannot show is, to the clock, progress that did not happen. Counsel is yours in this process (42 Pa.C.S. § 6337) — use the appointments like court dates.

**Choices:**
- Do the paper version: dated, copied, filed → **record**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the case record)_
  - NOTE (shown after choosing): Another dated page joins the folder.
- Handle it with a conversation and move on → **record**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [record] The Record Request
*Day 27 — Sunday, December 29, 2024 (dayOffset 27)*

The agency file holds the ratings, the referral log, and the plan as the agency wrote it. Records in that file are to be released on request (55 Pa. Code § 3130.44(d)).

Requesting it costs a stamp and a week of waiting. Not requesting it means arguing the fifteenth month from memory against people reading from paper.

**Choices:**
- Send the written request for the complete case record this week → **folder**  _(cash −5 ; FLAG: recordsRequested ; FLAG: recordSeen ; HIDDEN + Case record requested in writing under § 3130.44(d))_
  - NOTE (shown after choosing): The request is dated. Reconnaissance has a postmark.
- Ask the worker to just tell you what the file says → **folder**
  - NOTE (shown after choosing): She summarizes kindly. A summary is not a record, and next month it will not be in your folder.

## [folder] The Folder
*Day 40 — Saturday, January 11, 2025 (dayOffset 40)*

Your folder holds what your life can prove: pay stubs, certificates, sign-in sheets, and Keiko's drawings in the back, because folders are also archives.

The question this month is not whether you worked. It is whether the work exists anywhere outside your kitchen table.

**Choices:**
- Do the paper version: dated, copied, filed → **visit1**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the case record)_
  - NOTE (shown after choosing): Another dated page joins the folder.
- Handle it with a conversation and move on → **visit1**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [visit1] A Visit, Counted
*Day 53 — Friday, January 24, 2025 (dayOffset 53)*

The visit goes well. Keiko leaves with the practiced wave of a child who has learned the choreography of goodbye.

What the log will say is a separate event from what the visit was. Logs are written by people with pens, and pens can be asked, in writing, to write more.

**Choices:**
- Ask, in writing, for the visit log to note what actually happened → **service**  _(FLAG: visitLog ; HIDDEN + Visit log corrected/completed at the parent's written request)_
  - NOTE (shown after choosing): The log now shows a visit and a parent who writes things down.
- Let the log stand as written → **service**
  - NOTE (shown after choosing): The blank stays blank. Blanks get read as absence.

## [service] The Service That Is a Box
*Day 66 — Thursday, February 6, 2025 (dayOffset 66)*

On the plan, one line matters most: the treatment program. Beside it, a box. The state of that box — sent, started, completed, empty — is a fact about the agency as much as about you.

Boxes do not fill themselves, and they do not testify. Dates do.

**Choices:**
- Ask for the referral's dates in writing — promised, sent, started → **letter**  _(FLAG: referralDates ; HIDDEN + Referral chronology requested in writing)_
  - NOTE (shown after choosing): Three dates, requested politely. One of them does not exist, and now that is written down too.
- Trust that the referral is moving somewhere → **letter**
  - NOTE (shown after choosing): Somewhere is not a date.

## [letter] Paper With a Date On It
*Day 80 — Thursday, February 20, 2025 (dayOffset 80)*

A letter can do what a phone call cannot: exist in two months at once. One copy for the agency, one for the folder, one for the lawyer.

What needs dating this month is fifteen months of small documented facts that either add up to an exception or add up to nothing — said by the person who administers it, on paper, with a date.

**Choices:**
- Get it in a dated letter, on letterhead, and file your copy → **kinbeat**  _(cash −5 ; FLAG: datedLetter ; HIDDEN + Key barrier documented by a dated letter)_
  - NOTE (shown after choosing): A rumor becomes a fact with a date on it.
- Accept the verbal estimate — the number sounded right → **kinbeat**
  - NOTE (shown after choosing): Around, approximately, roughly. The file will keep the adverbs and lose the number.

## [kinbeat] The Family Name in the Minutes
*Day 93 — Wednesday, March 5, 2025 (dayOffset 93)*

Your sister Ruth has a spare room and a standing offer nobody has written down.

Kinship is the first exception the statute names — but a name spoken at a review is not a placement, a study, or a fact. It has to be built like everything else: in writing, early.

**Choices:**
- Put the kinship request in writing and ask for the study to be ordered → **work**  _(FLAG: kinAsked ; HIDDEN + Kinship placement requested in writing; study asked for)_
  - NOTE (shown after choosing): A name in the minutes becomes a request with a date.
- Let the family offer ride on the meeting's goodwill → **work**
  - NOTE (shown after choosing): Goodwill is real. It is also not a study.

## [work] The Shift and the Hearing
*Day 106 — Tuesday, March 18, 2025 (dayOffset 106)*

Work does not pause for permanency. Your supervisor has learned the shape of your court dates the way she learned the holiday schedule.

Every accommodation you need exists twice: once as a favor, once as a signed schedule. Only one of those survives a supervisor change.

**Choices:**
- Do the paper version: dated, copied, filed → **school**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the case record)_
  - NOTE (shown after choosing): Another dated page joins the folder.
- Handle it with a conversation and move on → **school**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [school] The School Note
*Day 119 — Monday, March 31, 2025 (dayOffset 119)*

Keiko's teacher sends home proof of an ordinary life continuing — grades, a comment, a drawing with too many suns.

File it. At month fifteen, ordinary life, documented, is evidence that the story the petition tells is not the only story in the room.

**Choices:**
- Do the paper version: dated, copied, filed → **review1**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the case record)_
  - NOTE (shown after choosing): Another dated page joins the folder.
- Handle it with a conversation and move on → **review1**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [review1] A Review, Mid-Clock
*Day 133 — Monday, April 14, 2025 (dayOffset 133)*

The review is polite. Progress is praised in the vocabulary of ratings. Nobody says the words "fifteen months" out loud.

Politeness is not a plan. The date does not need to be mentioned to be approaching.

**Choices:**
- Do the paper version: dated, copied, filed → **screens**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the case record)_
  - NOTE (shown after choosing): Another dated page joins the folder.
- Handle it with a conversation and move on → **screens**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [screens] The Small Proof
*Day 146 — Sunday, April 27, 2025 (dayOffset 146)*

Certificates accumulate: screens passed, sessions attended, a program letter with the word "consistent" in it.

Consistency is a paper quality. It is proven by sequences — dated, consecutive, kept.

**Choices:**
- Do the paper version: dated, copied, filed → **transport**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the case record)_
  - NOTE (shown after choosing): Another dated page joins the folder.
- Handle it with a conversation and move on → **transport**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [transport] Getting There
*Day 159 — Saturday, May 10, 2025 (dayOffset 159)*

The bus, the transfer, the visit room across town: logistics are the tax this system charges in hours instead of dollars.

Every arrival you can prove is a rebuttal to the only narrative the clock carries — that time passed and nothing changed.

**Choices:**
- Do the paper version: dated, copied, filed → **call**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the case record)_
  - NOTE (shown after choosing): Another dated page joins the folder.
- Handle it with a conversation and move on → **call**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [call] The Call You Make in Writing
*Day 173 — Saturday, May 24, 2025 (dayOffset 173)*

Some calls should be emails. Some emails should be letters. The medium is the evidence.

Mr. Aldan is not unkind. Mr. Aldan is carrying forty cases. What survives a caseload is what was written to it.

**Choices:**
- Do the paper version: dated, copied, filed → **waitlist**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the case record)_
  - NOTE (shown after choosing): Another dated page joins the folder.
- Handle it with a conversation and move on → **waitlist**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [waitlist] The List
*Day 186 — Friday, June 6, 2025 (dayOffset 186)*

The list that governs fifteen months of small documented facts that either add up to an exception or add up to nothing moves at the speed of other people's housing, other people's luck.

A position on a list, stated verbally, is a rumor. The same position in a dated letter is a fact a court can hold.

**Choices:**
- Get it in a dated letter, on letterhead, and file your copy → **home**  _(cash −5 ; FLAG: datedLetter ; HIDDEN + Key barrier documented by a dated letter)_
  - NOTE (shown after choosing): A rumor becomes a fact with a date on it.
- Accept the verbal estimate — the number sounded right → **home**
  - NOTE (shown after choosing): Around, approximately, roughly. The file will keep the adverbs and lose the number.

## [home] The Home Half-Ready
*Day 199 — Thursday, June 19, 2025 (dayOffset 199)*

You prepare a home for a child who does not live in it yet, in the order the inspections will ask about.

Hope is not a housing plan, but a lease, a letter, and a dated application are the skeleton of one.

**Choices:**
- Do the paper version: dated, copied, filed → **sibling**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the case record)_
  - NOTE (shown after choosing): Another dated page joins the folder.
- Handle it with a conversation and move on → **sibling**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [sibling] The Wider Family
*Day 212 — Wednesday, July 2, 2025 (dayOffset 212)*

The case is about one child on paper and a whole family in fact. Siblings, grandparents, the people who show up — the file flattens them into "supports."

Supports that exist in writing get weighed. Supports that exist at Thanksgiving get mentioned. There is a difference, and month fifteen knows it.

**Choices:**
- Do the paper version: dated, copied, filed → **letter2**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the case record)_
  - NOTE (shown after choosing): Another dated page joins the folder.
- Handle it with a conversation and move on → **letter2**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [letter2] The Second Letter
*Day 226 — Wednesday, July 16, 2025 (dayOffset 226)*

The first letter started a paper trail. The second one proves the trail is a practice, not an accident.

Agencies answer letters on agency time. Silence, dated, is also an answer — and it can be attached.

**Choices:**
- Do the paper version: dated, copied, filed → **visit2**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the case record)_
  - NOTE (shown after choosing): Another dated page joins the folder.
- Handle it with a conversation and move on → **visit2**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [visit2] A Visit, Noted
*Day 239 — Tuesday, July 29, 2025 (dayOffset 239)*

This visit, Keiko asks the question directly: when? The supervisor's note will record the visit. What it records about the answer is up to who writes first.

Ask for the note to be complete. A log that shows a question and a plan reads differently from a log that shows a blank.

**Choices:**
- Ask, in writing, for the visit log to note what actually happened → **folder2**  _(FLAG: visitLog ; HIDDEN + Visit log corrected/completed at the parent's written request)_
  - NOTE (shown after choosing): The log now shows a visit and a parent who writes things down.
- Let the log stand as written → **folder2**
  - NOTE (shown after choosing): The blank stays blank. Blanks get read as absence.

## [folder2] The Folder, Audited
*Day 252 — Monday, August 11, 2025 (dayOffset 252)*

Your lawyer spreads the folder on her desk like a hand of cards and tells you which ones the court can actually play.

Affection is not an exhibit. Certificates are exhibits. Letters are exhibits. The folder is only as strong as its dates.

**Choices:**
- Do the paper version: dated, copied, filed → **review2**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the case record)_
  - NOTE (shown after choosing): Another dated page joins the folder.
- Handle it with a conversation and move on → **review2**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [review2] The Review Where the Date Is Said
*Day 266 — Monday, August 25, 2025 (dayOffset 266)*

This time the date is said aloud, in the room, on the record: the fifteenth month, and what the agency must do when it arrives unless an exception applies.

Hearing it said is the moment the case changes tense — from someday to scheduled.

**Choices:**
- Ask what exception the agency intends to document, and ask on the record → **callx25**  _(FLAG: askedOnRecord ; HIDDEN + Agency asked on the record which exception it will document)_
  - NOTE (shown after choosing): The question is now part of the case, not just part of the day.
- Contest the goal change out loud, at length, from the heart → **end_goal**
  - NOTE (shown after choosing): The heart is not the record. The goal question moves without your paper in it.
- Say nothing and save your energy for the hearing → **callx25**
  - NOTE (shown after choosing): Silence conserves energy and spends leverage.

## [callx25] The Call You Make in Writing — Again, On Paper
*Day 279 — Sunday, September 7, 2025 (dayOffset 279)*

Some calls should be emails. Some emails should be letters. The medium is the evidence.

Mr. Aldan is not unkind. Mr. Aldan is carrying forty cases. What survives a caseload is what was written to it.

**Choices:**
- Do the paper version: dated, copied, filed → **waitlistx26**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the case record)_
  - NOTE (shown after choosing): Another dated page joins the folder.
- Handle it with a conversation and move on → **waitlistx26**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [waitlistx26] The List — Again, On Paper
*Day 292 — Saturday, September 20, 2025 (dayOffset 292)*

The list that governs fifteen months of small documented facts that either add up to an exception or add up to nothing moves at the speed of other people's housing, other people's luck.

A position on a list, stated verbally, is a rumor. The same position in a dated letter is a fact a court can hold.

**Choices:**
- Do the paper version: dated, copied, filed → **homex27**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the case record)_
  - NOTE (shown after choosing): Another dated page joins the folder.
- Handle it with a conversation and move on → **homex27**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [homex27] The Home Half-Ready — Again, On Paper
*Day 305 — Friday, October 3, 2025 (dayOffset 305)*

You prepare a home for a child who does not live in it yet, in the order the inspections will ask about.

Hope is not a housing plan, but a lease, a letter, and a dated application are the skeleton of one.

**Choices:**
- Do the paper version: dated, copied, filed → **siblingx28**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the case record)_
  - NOTE (shown after choosing): Another dated page joins the folder.
- Handle it with a conversation and move on → **siblingx28**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [siblingx28] The Wider Family — Again, On Paper
*Day 319 — Friday, October 17, 2025 (dayOffset 319)*

The case is about one child on paper and a whole family in fact. Siblings, grandparents, the people who show up — the file flattens them into "supports."

Supports that exist in writing get weighed. Supports that exist at Thanksgiving get mentioned. There is a difference, and month fifteen knows it.

**Choices:**
- Do the paper version: dated, copied, filed → **letter2x29**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the case record)_
  - NOTE (shown after choosing): Another dated page joins the folder.
- Handle it with a conversation and move on → **letter2x29**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [letter2x29] The Second Letter — Again, On Paper
*Day 332 — Thursday, October 30, 2025 (dayOffset 332)*

The first letter started a paper trail. The second one proves the trail is a practice, not an accident.

Agencies answer letters on agency time. Silence, dated, is also an answer — and it can be attached.

**Choices:**
- Do the paper version: dated, copied, filed → **visit2x30**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the case record)_
  - NOTE (shown after choosing): Another dated page joins the folder.
- Handle it with a conversation and move on → **visit2x30**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [visit2x30] A Visit, Noted — Again, On Paper
*Day 345 — Wednesday, November 12, 2025 (dayOffset 345)*

This visit, Keiko asks the question directly: when? The supervisor's note will record the visit. What it records about the answer is up to who writes first.

Ask for the note to be complete. A log that shows a question and a plan reads differently from a log that shows a blank.

**Choices:**
- Ask, in writing, for the visit log to note what actually happened → **folder2x31**  _(FLAG: visitLog ; HIDDEN + Visit log corrected/completed at the parent's written request)_
  - NOTE (shown after choosing): The log now shows a visit and a parent who writes things down.
- Let the log stand as written → **folder2x31**
  - NOTE (shown after choosing): The blank stays blank. Blanks get read as absence.

## [folder2x31] The Folder, Audited — Again, On Paper
*Day 358 — Tuesday, November 25, 2025 (dayOffset 358)*

Your lawyer spreads the folder on her desk like a hand of cards and tells you which ones the court can actually play.

Affection is not an exhibit. Certificates are exhibits. Letters are exhibits. The folder is only as strong as its dates.

**Choices:**
- Do the paper version: dated, copied, filed → **review2x32**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the case record)_
  - NOTE (shown after choosing): Another dated page joins the folder.
- Handle it with a conversation and move on → **review2x32**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [review2x32] The Review Where the Date Is Said — Again, On Paper
*Day 372 — Tuesday, December 9, 2025 (dayOffset 372)*

This time the date is said aloud, in the room, on the record: the fifteenth month, and what the agency must do when it arrives unless an exception applies.

Hearing it said is the moment the case changes tense — from someday to scheduled.

**Choices:**
- Do the paper version: dated, copied, filed → **review1x33**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the case record)_
  - NOTE (shown after choosing): Another dated page joins the folder.
- Handle it with a conversation and move on → **review1x33**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [review1x33] A Review, Mid-Clock — Again, On Paper
*Day 385 — Monday, December 22, 2025 (dayOffset 385)*

The review is polite. Progress is praised in the vocabulary of ratings. Nobody says the words "fifteen months" out loud.

Politeness is not a plan. The date does not need to be mentioned to be approaching.

**Choices:**
- Ask what exception the agency intends to document, and ask on the record → **packet**  _(FLAG: askedOnRecord ; HIDDEN + Agency asked on the record which exception it will document)_
  - NOTE (shown after choosing): The question is now part of the case, not just part of the day.
- Contest the goal change out loud, at length, from the heart → **end_goal**
  - NOTE (shown after choosing): The heart is not the record. The goal question moves without your paper in it.
- Say nothing and save your energy for the hearing → **packet**
  - NOTE (shown after choosing): Silence conserves energy and spends leverage.

## [packet] The Packet
*Day 395 — Thursday, January 1, 2026 (dayOffset 395)*

The packet is the whole paper case in one stack: the record you requested, the letters, the log corrections, the dated proof — tabbed, copied, filed before the date it answers.

Filing it converts your fifteen months from a story you tell into a document the agency must reckon with.

**Choices:**
- File the packet and ask for the finding in writing → **prep**  _(cash −15 ; FLAG: packetBuilt ; HIDDEN + Exception packet filed before the fifteen-month date)_
  - NOTE (shown after choosing): Filed, stamped, copied. The clock now has something to meet.
- Bring the packet to the hearing and hand it up there → **prep**
  - NOTE (shown after choosing): Paper delivered at the deadline is paper the other side has not read. Timing is part of evidence.

## [prep] Rehearsing the Hearing
*Day 427 — Monday, February 2, 2026 (dayOffset 427)*

Your lawyer rehearses you the way lawyers do: short answers, dates first, no speeches.

"The judge has read the packet," she says. "Your job is to be the person the packet describes."

**Choices:**
- Do the paper version: dated, copied, filed → **lawyer2**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the case record)_
  - NOTE (shown after choosing): Another dated page joins the folder.
- Handle it with a conversation and move on → **lawyer2**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [lawyer2] The Night Before
*Day 441 — Monday, February 16, 2026 (dayOffset 441)*

The night before the review, the folder is closed and the clock is what it is.

Everything controllable has been controlled or it has not. What remains is to walk in with the record you built.

**Choices:**
- Do the paper version: dated, copied, filed → **eve**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the case record)_
  - NOTE (shown after choosing): Another dated page joins the folder.
- Handle it with a conversation and move on → **eve**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [eve] The Morning Of
*Day 449 — Tuesday, February 24, 2026 (dayOffset 449)*

Court clothes on a chair. The packet in a bag by the door. A child, somewhere across town, eating breakfast in a house that is not this one.

Fifteen months comes down to a morning, the way every deadline does.

**Choices:**
- Do the paper version: dated, copied, filed → **track**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the case record)_
  - NOTE (shown after choosing): Another dated page joins the folder.
- Handle it with a conversation and move on → **track**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [track] The Compelling-Reason Track
*Day 453 — Saturday, February 28, 2026 (dayOffset 453)*

The second exception: the agency documents in the case plan a compelling reason why filing would not be in the child's best interest (42 U.S.C. § 675(5)(E)). "Documented in the case plan" is a place and a page, not a feeling in a meeting.

Build the packet that gives the agency a reason it can write down: dated progress, dated barriers, dated proof.

**Choices:**
- Build this track's record completely, in writing → **hearing**  _(cash −10 ; FLAG: compellingReady ; HIDDEN + Exception track record completed and filed)_
  - NOTE (shown after choosing): The exception is no longer an argument. It is a stack of dated facts.
- Argue the exception from the facts everyone already knows → **hearing**
  - NOTE (shown after choosing): Known to you. The file is the room's memory, and it was not in the room.

## [hearing] The Fifteen-Month Review
*Day 455 — Monday, March 2, 2026 — THE FIFTEEN-MONTH DATE: Monday, March 2, 2026 (dayOffset 455)*

The review is held on the date the clock named: Monday, March 2, 2026 — fifteen months from Monday, December 2, 2024. The agency must file or join a termination petition unless an exception is documented (42 U.S.C. § 675(5)(E)).

What happens next was decided by paper filed before today. That was always the design of this clock — and of this story.

**Choices:**
- Put the packet's dates to the court and ask for the exception to be documented → **end_win**  _(REQUIRES FLAG: recordsRequested ; REQUIRES FLAG: packetBuilt ; REQUIRES FLAG: compellingReady)_
  - NOTE (shown after choosing): The dates do the talking.
- Accept the documented deferral the agency offers at the table → **end_partial**
  - NOTE (shown after choosing): Not the best door — but a door with the exception's name on it.
- Give the speech about everything you have done → **end_petition**
  - NOTE (shown after choosing): It is a true speech. The petition is a document. Documents outlast speeches.

## [end_win] Ending — Home at Month Sixteen
*Day 485 — Wednesday, April 1, 2026 (dayOffset 485)*

The record did what records can do when they are complete early: the plan's last barrier breaks on paper before the hearing, and the court orders Keiko home under its order. Fifteen months of dates end in a date that is yours.

Read the order twice. Then keep the folder. Cases like this one are not finished by endings; they are continued by them.

**DEBRIEF:**

THE CLOCK, ANSWERED: entry Monday, December 2, 2024 + 15 months = Monday, March 2, 2026. At 15 of the most recent 22 months in foster care, the agency must file or join a petition to terminate parental rights — unless an exception applies (42 U.S.C. § 675(5)(E)). The three exceptions, as this scenario states them: the child is being cared for by a relative; the agency has documented a compelling reason in the case plan why filing would not be in the child's best interest; or the agency has not provided the services the plan identified as necessary for the child's safe return.

Agency records are released on request — 55 Pa. Code § 3130.44(d) ("shall be released upon request"). The record request is the reconnaissance that makes every later date arguable. A termination petition, if filed, is a separate case the agency must still prove by clear and convincing evidence. A filing date is not a finding, and this scenario ends at the filing decision — it depicts no termination outcome.

THE HONEST PART: the packet did not guarantee this. It guaranteed the agency and the court had to reckon with dated facts instead of impressions. Workers, judges, housing lists, and luck still decided their parts — your choices decided what paper they decided on.

## [end_partial] Ending — Documented, and Waiting
*Day 458 — Thursday, March 5, 2026 (dayOffset 458)*

The exception is documented and the filing is deferred — a real legal win with a child still placed at the end of it. The case continues, the goal survives, and the next review has a date too.

**DEBRIEF:**

THE CLOCK, DEFERRED: at Monday, March 2, 2026 the agency documented an exception rather than filing (42 U.S.C. § 675(5)(E)). Deferral is not dismissal; it is time, in writing.

A termination petition, if filed, is a separate case the agency must still prove by clear and convincing evidence. A filing date is not a finding, and this scenario ends at the filing decision — it depicts no termination outcome.

THE HONEST PART: this ending is what the strongest controllable strategy usually buys — not the child home, but the petition unfilled and the record improved. It is labeled partial because it is one.

## [end_petition] Ending — The Petition Is Filed
*Day 465 — Thursday, March 12, 2026 (dayOffset 465)*

The petition is filed on the clock's schedule, from the file as it stood. Your effort was real. Too much of it was undated, unmailed, or unspoken in the rooms where the file was written.

**DEBRIEF:**

THE CLOCK, UNANSWERED: at Monday, March 2, 2026 no exception stood documented, so the filing duty operated (42 U.S.C. § 675(5)(E)).

A termination petition, if filed, is a separate case the agency must still prove by clear and convincing evidence. A filing date is not a finding, and this scenario ends at the filing decision — it depicts no termination outcome. The case now changes forums and burdens — it does not end today.

THE HONEST PART: petitions are filed against parents who worked hard, when the work never became paper. That is the lesson this scenario exists to teach before it costs anyone anything real.

## [end_goal] Ending — The Goal Changes
*Day 435 — Tuesday, February 10, 2026 (dayOffset 435)*

The goal changes to adoption on a record that showed effort without documentation. The reunification track closes; an appeal or a new record would have to reopen it.

**DEBRIEF:**

THE GOAL, ON THE RECORD: goal changes are decided on the paper in the room — compliance shown, services documented, exceptions arguable or absent.

Agency records are released on request — 55 Pa. Code § 3130.44(d) ("shall be released upon request"). The record request is the reconnaissance that makes every later date arguable.

THE HONEST PART: speaking from the heart at the review was human and understandable. The system runs on exhibits. The strategy guides exist so the next parent brings both.
