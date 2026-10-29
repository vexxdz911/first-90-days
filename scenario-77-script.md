# THE FIRST 90 DAYS — Scenario 77: “The Fifteenth Month, Written Down”

*Human-readable script. This document and `scenario-77.json` are generated from a single source and match node-for-node: same IDs, same order, same choices, same effects.*

**The family is fictional — a composite. No real person's story appears here.**

**Content note:** This scenario depicts a permanency timeline — reviews, a possible termination-petition filing decision, and paperwork. There is no graphic content. Players may skip any scene or use the quick exit at any time.

**How to read effects:** `cash −40` changes the player's cash. `FLAG: name` sets a flag the engine tracks. `HIDDEN + item` means the case file quietly records that item at this choice. `REQUIRES FLAG: name` means the choice is only available if that flag was set earlier.

Start date: Monday, February 3, 2025. Day offsets are days since the scenario's start date (the child's foster-care entry date).

## [start] The Clock You Cannot See
*Day 0 — Monday, February 3, 2025 (dayOffset 0)*

Your name is Selma. Your child Tova, 6, has been in foster care since the date the court set — and a second calendar started that day, one nobody handed you a copy of.

Fifteen of the most recent twenty-two months. That is the federal permanency clock (42 U.S.C. § 675(5)(E)), and this story is the fifteen months, played honestly: a housing waitlist that moves one name a month. Tova keeps her library card in a sandwich bag so it survives the shelter, the bus, and your purse.

**Choices:**
- Do the paper version: dated, copied, filed → **map**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the case record)_
  - NOTE (shown after choosing): Another dated page joins the folder.
- Handle it with a conversation and move on → **map**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [map] The Lawyer Draws the Clock
*Day 35 — Monday, March 10, 2025 (dayOffset 35)*

Your lawyer draws one line: Tova's months in care, counted from the entry date. At month fifteen the agency's duty about filing a termination petition changes — unless an exception is documented.

She underlines one word three times: documented. Progress the file cannot show is, to the clock, progress that did not happen. Counsel is yours in this process (42 Pa.C.S. § 6337) — use the appointments like court dates.

**Choices:**
- Do the paper version: dated, copied, filed → **record**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the case record)_
  - NOTE (shown after choosing): Another dated page joins the folder.
- Handle it with a conversation and move on → **record**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [record] The Record Request
*Day 70 — Monday, April 14, 2025 (dayOffset 70)*

The agency file holds the ratings, the referral log, and the plan as the agency wrote it. Records in that file are to be released on request (55 Pa. Code § 3130.44(d)).

Requesting it costs a stamp and a week of waiting. Not requesting it means arguing the fifteenth month from memory against people reading from paper.

**Choices:**
- Send the written request for the complete case record this week → **folder**  _(cash −5 ; FLAG: recordsRequested ; FLAG: recordSeen ; HIDDEN + Case record requested in writing under § 3130.44(d))_
  - NOTE (shown after choosing): The request is dated. Reconnaissance has a postmark.
- Ask the worker to just tell you what the file says → **folder**
  - NOTE (shown after choosing): She summarizes kindly. A summary is not a record, and next month it will not be in your folder.

## [folder] The Folder
*Day 105 — Monday, May 19, 2025 (dayOffset 105)*

Your folder holds what your life can prove: pay stubs, certificates, sign-in sheets, and Tova's drawings in the back, because folders are also archives.

The question this month is not whether you worked. It is whether the work exists anywhere outside your kitchen table.

**Choices:**
- Do the paper version: dated, copied, filed → **visit1**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the case record)_
  - NOTE (shown after choosing): Another dated page joins the folder.
- Handle it with a conversation and move on → **visit1**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [visit1] A Visit, Counted
*Day 140 — Monday, June 23, 2025 (dayOffset 140)*

The visit goes well. Tova leaves with the practiced wave of a child who has learned the choreography of goodbye.

What the log will say is a separate event from what the visit was. Logs are written by people with pens, and pens can be asked, in writing, to write more.

**Choices:**
- Ask, in writing, for the visit log to note what actually happened → **service**  _(FLAG: visitLog ; HIDDEN + Visit log corrected/completed at the parent's written request)_
  - NOTE (shown after choosing): The log now shows a visit and a parent who writes things down.
- Let the log stand as written → **service**
  - NOTE (shown after choosing): The blank stays blank. Blanks get read as absence.

## [service] The Service That Is a Box
*Day 175 — Monday, July 28, 2025 (dayOffset 175)*

On the plan, one line matters most: the family-housing list. Beside it, a box. The state of that box — sent, started, completed, empty — is a fact about the agency as much as about you.

Boxes do not fill themselves, and they do not testify. Dates do.

**Choices:**
- Ask for the referral's dates in writing — promised, sent, started → **letter**  _(FLAG: referralDates ; HIDDEN + Referral chronology requested in writing)_
  - NOTE (shown after choosing): Three dates, requested politely. One of them does not exist, and now that is written down too.
- Trust that the referral is moving somewhere → **letter**
  - NOTE (shown after choosing): Somewhere is not a date.

## [letter] Paper With a Date On It
*Day 209 — Sunday, August 31, 2025 (dayOffset 209)*

A letter can do what a phone call cannot: exist in two months at once. One copy for the agency, one for the folder, one for the lawyer.

What needs dating this month is a housing waitlist that moves one name a month — said by the person who administers it, on paper, with a date.

**Choices:**
- Get it in a dated letter, on letterhead, and file your copy → **kinbeat**  _(cash −5 ; FLAG: datedLetter ; HIDDEN + Key barrier documented by a dated letter)_
  - NOTE (shown after choosing): A rumor becomes a fact with a date on it.
- Accept the verbal estimate — the number sounded right → **kinbeat**
  - NOTE (shown after choosing): Around, approximately, roughly. The file will keep the adverbs and lose the number.

## [kinbeat] The Family Name in the Minutes
*Day 244 — Sunday, October 5, 2025 (dayOffset 244)*

A relative has been named at two reviews; the name lives in the minutes and nowhere else.

Kinship is the first exception the statute names — but a name spoken at a review is not a placement, a study, or a fact. It has to be built like everything else: in writing, early.

**Choices:**
- Put the kinship request in writing and ask for the study to be ordered → **work**  _(FLAG: kinAsked ; HIDDEN + Kinship placement requested in writing; study asked for)_
  - NOTE (shown after choosing): A name in the minutes becomes a request with a date.
- Let the family offer ride on the meeting's goodwill → **work**
  - NOTE (shown after choosing): Goodwill is real. It is also not a study.

## [work] The Shift and the Hearing
*Day 279 — Sunday, November 9, 2025 (dayOffset 279)*

Work does not pause for permanency. Your supervisor has learned the shape of your court dates the way she learned the holiday schedule.

Every accommodation you need exists twice: once as a favor, once as a signed schedule. Only one of those survives a supervisor change.

**Choices:**
- Do the paper version: dated, copied, filed → **school**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the case record)_
  - NOTE (shown after choosing): Another dated page joins the folder.
- Handle it with a conversation and move on → **school**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [school] The School Note
*Day 314 — Sunday, December 14, 2025 (dayOffset 314)*

Tova's teacher sends home proof of an ordinary life continuing — grades, a comment, a drawing with too many suns.

File it. At month fifteen, ordinary life, documented, is evidence that the story the petition tells is not the only story in the room.

**Choices:**
- Do the paper version: dated, copied, filed → **folder2**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the case record)_
  - NOTE (shown after choosing): Another dated page joins the folder.
- Handle it with a conversation and move on → **folder2**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [folder2] The Folder, Audited
*Day 349 — Sunday, January 18, 2026 (dayOffset 349)*

Your lawyer spreads the folder on her desk like a hand of cards and tells you which ones the court can actually play.

Affection is not an exhibit. Certificates are exhibits. Letters are exhibits. The folder is only as strong as its dates.

**Choices:**
- Do the paper version: dated, copied, filed → **review2**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the case record)_
  - NOTE (shown after choosing): Another dated page joins the folder.
- Handle it with a conversation and move on → **review2**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [review2] The Review Where the Date Is Said
*Day 384 — Sunday, February 22, 2026 (dayOffset 384)*

This time the date is said aloud, in the room, on the record: the fifteenth month, and what the agency must do when it arrives unless an exception applies.

Hearing it said is the moment the case changes tense — from someday to scheduled.

**Choices:**
- Ask what exception the agency intends to document, and ask on the record → **packet**  _(FLAG: askedOnRecord ; HIDDEN + Agency asked on the record which exception it will document)_
  - NOTE (shown after choosing): The question is now part of the case, not just part of the day.
- Contest the goal change out loud, at length, from the heart → **packet**
  - NOTE (shown after choosing): The heart is not the record. The goal question moves without your paper in it.
- Say nothing and save your energy for the hearing → **packet**
  - NOTE (shown after choosing): Silence conserves energy and spends leverage.

## [packet] The Packet
*Day 394 — Wednesday, March 4, 2026 (dayOffset 394)*

The packet is the whole paper case in one stack: the record you requested, the letters, the log corrections, the dated proof — tabbed, copied, filed before the date it answers.

Filing it converts your fifteen months from a story you tell into a document the agency must reckon with.

**Choices:**
- File the packet and ask for the finding in writing → **prep**  _(cash −15 ; FLAG: packetBuilt ; HIDDEN + Exception packet filed before the fifteen-month date)_
  - NOTE (shown after choosing): Filed, stamped, copied. The clock now has something to meet.
- Bring the packet to the hearing and hand it up there → **prep**
  - NOTE (shown after choosing): Paper delivered at the deadline is paper the other side has not read. Timing is part of evidence.

## [prep] Rehearsing the Hearing
*Day 426 — Sunday, April 5, 2026 (dayOffset 426)*

Your lawyer rehearses you the way lawyers do: short answers, dates first, no speeches.

"The judge has read the packet," she says. "Your job is to be the person the packet describes."

**Choices:**
- Do the paper version: dated, copied, filed → **lawyer2**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the case record)_
  - NOTE (shown after choosing): Another dated page joins the folder.
- Handle it with a conversation and move on → **lawyer2**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [lawyer2] The Night Before
*Day 440 — Sunday, April 19, 2026 (dayOffset 440)*

The night before the review, the folder is closed and the clock is what it is.

Everything controllable has been controlled or it has not. What remains is to walk in with the record you built.

**Choices:**
- Do the paper version: dated, copied, filed → **eve**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the case record)_
  - NOTE (shown after choosing): Another dated page joins the folder.
- Handle it with a conversation and move on → **eve**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [eve] The Morning Of
*Day 448 — Monday, April 27, 2026 (dayOffset 448)*

Court clothes on a chair. The packet in a bag by the door. A child, somewhere across town, eating breakfast in a house that is not this one.

Fifteen months comes down to a morning, the way every deadline does.

**Choices:**
- Do the paper version: dated, copied, filed → **track**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the case record)_
  - NOTE (shown after choosing): Another dated page joins the folder.
- Handle it with a conversation and move on → **track**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [track] The Compelling-Reason Track
*Day 452 — Friday, May 1, 2026 (dayOffset 452)*

The second exception: the agency documents in the case plan a compelling reason why filing would not be in the child's best interest (42 U.S.C. § 675(5)(E)). "Documented in the case plan" is a place and a page, not a feeling in a meeting.

Build the packet that gives the agency a reason it can write down: dated progress, dated barriers, dated proof.

**Choices:**
- Build this track's record completely, in writing → **hearing**  _(cash −10 ; FLAG: compellingReady ; HIDDEN + Exception track record completed and filed)_
  - NOTE (shown after choosing): The exception is no longer an argument. It is a stack of dated facts.
- Argue the exception from the facts everyone already knows → **hearing**
  - NOTE (shown after choosing): Known to you. The file is the room's memory, and it was not in the room.

## [hearing] The Fifteen-Month Review
*Day 454 — Sunday, May 3, 2026 — THE FIFTEEN-MONTH DATE: Sunday, May 3, 2026 (dayOffset 454)*

The review is held on the date the clock named: Sunday, May 3, 2026 — fifteen months from Monday, February 3, 2025. The agency must file or join a termination petition unless an exception is documented (42 U.S.C. § 675(5)(E)).

What happens next was decided by paper filed before today. That was always the design of this clock — and of this story.

**Choices:**
- Put the packet's dates to the court and ask for the exception to be documented → **end_win**  _(REQUIRES FLAG: recordsRequested ; REQUIRES FLAG: packetBuilt ; REQUIRES FLAG: compellingReady)_
  - NOTE (shown after choosing): The dates do the talking.
- Give the speech about everything you have done → **end_petition**
  - NOTE (shown after choosing): It is a true speech. The petition is a document. Documents outlast speeches.

## [end_win] Ending — Documented, Not Filed
*Day 484 — Tuesday, June 2, 2026 (dayOffset 484)*

The exception is documented — written into the case plan, dated, on the record. The petition the clock pointed at is not filed. Tova remains placed and the case continues toward its goal, but the fifteenth month met a record instead of a rumor.

Read the order twice. Then keep the folder. Cases like this one are not finished by endings; they are continued by them.

**DEBRIEF:**

THE CLOCK, ANSWERED: entry Monday, February 3, 2025 + 15 months = Sunday, May 3, 2026. At 15 of the most recent 22 months in foster care, the agency must file or join a petition to terminate parental rights — unless an exception applies (42 U.S.C. § 675(5)(E)). The three exceptions, as this scenario states them: the child is being cared for by a relative; the agency has documented a compelling reason in the case plan why filing would not be in the child's best interest; or the agency has not provided the services the plan identified as necessary for the child's safe return.

Agency records are released on request — 55 Pa. Code § 3130.44(d) ("shall be released upon request"). The record request is the reconnaissance that makes every later date arguable. A termination petition, if filed, is a separate case the agency must still prove by clear and convincing evidence. A filing date is not a finding, and this scenario ends at the filing decision — it depicts no termination outcome.

THE HONEST PART: the packet did not guarantee this. It guaranteed the agency and the court had to reckon with dated facts instead of impressions. Workers, judges, housing lists, and luck still decided their parts — your choices decided what paper they decided on.

## [end_petition] Ending — The Petition Is Filed
*Day 464 — Wednesday, May 13, 2026 (dayOffset 464)*

The petition is filed on the clock's schedule, from the file as it stood. Your effort was real. Too much of it was undated, unmailed, or unspoken in the rooms where the file was written.

**DEBRIEF:**

THE CLOCK, UNANSWERED: at Sunday, May 3, 2026 no exception stood documented, so the filing duty operated (42 U.S.C. § 675(5)(E)).

A termination petition, if filed, is a separate case the agency must still prove by clear and convincing evidence. A filing date is not a finding, and this scenario ends at the filing decision — it depicts no termination outcome. The case now changes forums and burdens — it does not end today.

THE HONEST PART: petitions are filed against parents who worked hard, when the work never became paper. That is the lesson this scenario exists to teach before it costs anyone anything real.
