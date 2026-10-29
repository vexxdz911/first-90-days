# THE FIRST 90 DAYS — Scenario 130: “Across the County Line”

*Human-readable script. This document and `scenario-130.json` are generated from a single source and match node-for-node: same IDs, same order, same choices, same effects.*

**The family is fictional — a composite. No real person's story appears here.**

**Content note:** This scenario depicts a dependency case transferred between counties, with reviews and a permanency timeline. There is no graphic content. Players may skip any scene or use the quick exit at any time.

**How to read effects:** `cash −40` changes the player's cash. `FLAG: name` sets a flag the engine tracks. `HIDDEN + item` means the case file quietly records that item at this choice — the player does not see it when it happens. `REQUIRES FLAG: name` means the choice is only available if that flag was set earlier; `REQUIRES NO FLAG: name` means it is only available if that flag was never set. `NOTE:` is text shown to the player right after choosing.

Start date: Monday, January 5, 2026. Day offsets are days since the scenario's start date (the children's foster-care entry date).

## [start] Two Children, Two Clocks
*Day 0 — Monday, January 5, 2026 (dayOffset 0)*

Your name is Nerea. Iker, nine, and Aitana, six, entered foster care on Monday, January 5, 2026, after the winter your hours were cut and the rent math stopped working — a sentence this story insists on writing plainly, because the file's version ('housing instability') sounds like weather and this was arithmetic.

The children are with a foster family twenty minutes away. Your plan is underway: housing program, doubled shifts, visits kept. And last week, the warehouse across the county line offered you the full-time line job — the one that makes the rent math work forever instead of monthly. Moving for it moves the case. Cases, like families, do not always survive the trip intact.

**Choices:**
- Tell your lawyer, Mr. Ndiaye, before you tell anyone else → **winter_detail**  _(FLAG: lawyerTold ; HIDDEN + Counsel informed of the move before the agency)_
  - NOTE (shown after choosing): Sequence is a strategy. The lawyer hears it first; everyone else hears it as a plan.
- Tell the caseworker at Thursday's visit — transparency first → **winter_detail**
  - NOTE (shown after choosing): Transparency is a virtue. Unaccompanied transparency is a rumor with good intentions.

## [winter_detail] The Winter, Itemized
*Day 2 — Wednesday, January 7, 2026 (dayOffset 2)*

Before any of it moves, the winter deserves its true inventory: the hours cut in November, the landlord's letter, the housing program's intake date, Iker's school twenty minutes one way and Aitana's another — a family logistics problem that the file calls 'instability' the way maps call mountains 'terrain.'

You are not the summary. But the summary is what travels, unless the file is made to carry more.

**Choices:**
- Write the winter as a one-page chronology and give it to Mr. Ndiaye → **lawyer_first**  _(FLAG: winterWritten ; HIDDEN + Family's own chronology of the placement winter written)_
  - NOTE (shown after choosing): Your version exists now, with dates. Summaries hate competition.
- The file knows the story well enough → **lawyer_first**
  - NOTE (shown after choosing): The file knows a four-word version. Competition is coming whether you write it or not.

## [lawyer_first] The Transfer Problem
*Day 6 — Sunday, January 11, 2026 (dayOffset 6)*

Mr. Ndiaye does not talk you out of the job. He talks you into paperwork. 'A case that crosses a county line gets read twice,' he says, 'and the second reading starts from whatever physically arrives. Our job is to make sure what arrives is the whole story: the exception packet we're building, the visit log, the referral dates — not a summary of them.'

Counsel is your right (42 Pa.C.S. § 6337), and in a transfer it becomes logistics: who sends what, to whom, by when, receipt confirmed in writing.

**Choices:**
- Build the transfer inventory with him: every document, its date, its location in the file → **job_letter**  _(FLAG: inventoryBuilt ; HIDDEN + Transfer document inventory built with counsel)_
  - NOTE (shown after choosing): An inventory is a promise the file makes to its future self.
- Assume the counties handle transfers between themselves — it's routine → **job_letter**
  - NOTE (shown after choosing): It is routine. Routinely, pages go missing at exactly the rate nobody counted them.

## [job_letter] The Offer, On Letterhead
*Day 10 — Thursday, January 15, 2026 (dayOffset 10)*

The warehouse's offer letter is a beautiful document: full-time, benefits, a start date, a number. It is also, in a case file, a loaded one — proof of stability and evidence of disruption in the same paragraph, depending on who frames it first.

Framing is a race the early note almost won. The letter, filed with a plan wrapped around it, is a different exhibit from the letter discovered later, alone.

**Choices:**
- File the offer letter together with the transfer plan, as one exhibit → **inventory**  _(FLAG: offerFiled ; HIDDEN + Job offer filed together with the transfer plan)_
  - NOTE (shown after choosing): Framed by its plan. The exhibit argues stability because its context is attached.
- Keep the letter out of the file until the plan is approved → **inventory**
  - NOTE (shown after choosing): Letters kept out of files have a habit of arriving anyway, unaccompanied.

## [inventory] The Exception Packet, So Far
*Day 13 — Sunday, January 18, 2026 (dayOffset 13)*

What would travel: the record you requested in February's first weeks — wait, you haven't yet. Mr. Ndiaye stops the meeting. 'Before anything moves,' he says, 'we request the complete record here (55 Pa. Code § 3130.44(d)). You cannot inventory what you have not seen, and you cannot prove a page was lost if you never knew it existed.'

The packet you are building answers the clock both children share: entry January 5, 2026; fifteen months lands Monday, April 5, 2027. The compelling-reason documentation — your housing program completion, the new full-time job, the children's school stability — must exist in the case plan before any transfer, while this county still knows your name.

**Choices:**
- Sign the written record request today → **packet_copy**  _(cash −5 ; FLAG: recordsRequested ; HIDDEN + Case record requested in writing under § 3130.44(d) before transfer)_
  - NOTE (shown after choosing): Requested before the move. The mirror travels with you now.
- Request it after the move, from the new county — cleaner → **packet_copy**
  - NOTE (shown after choosing): Cleaner, and months later, and answered from whatever arrived. Order matters.

## [packet_copy] The Second Set
*Day 20 — Sunday, January 25, 2026 (dayOffset 20)*

Mr. Ndiaye's paralegal makes a complete second set of the file — every page, stamped COPY, in a box that will live at your sister's house. 'Files that exist twice,' he says, 'can survive one building's bad week. Files that exist once are a rumor away from being a summary.'

It costs an afternoon and a ream of paper. It is the cheapest insurance in the entire case.

**Choices:**
- Make the second set and store it outside both counties' buildings → **record_req130**  _(cash −10 ; FLAG: secondSet ; HIDDEN + Complete second copy of the file made and stored)_
  - NOTE (shown after choosing): Two sets, two buildings, one story. Insurance against entropy.
- The inventory list should be protection enough → **record_req130**
  - NOTE (shown after choosing): A list proves what existed. A copy replaces it. Different tools; entropy respects only one.

## [record_req130] What the Record Holds
*Day 27 — Sunday, February 1, 2026 (dayOffset 27)*

The record holds the whole winter: the visit log the foster parents countersigned, the housing program's dated letters, the referral chronology you requested in writing in week two — and one surprise: a case note describing your job offer as a 'possible relocation risk,' written the day you told the caseworker at the visit, before the plan existed to attach it to.

Notes written early harden first. The correction is not an argument; it is a dated document of your own, filed beside it.

**Choices:**
- File a dated statement: the job, the address, the school plan, the transfer request — beside the note, not against it → **record_index**  _(cash −5 ; FLAG: statementFiled ; HIDDEN + Parent's dated statement and transfer plan filed beside the early case note)_
  - NOTE (shown after choosing): Beside, not against. Files believe neighbors more than opponents.
- Ask for the note to be removed — it misrepresents you → **record_index**
  - NOTE (shown after choosing): Files almost never unwrite themselves. They do, however, accept additions with dates.

## [record_index] Indexing the Winter
*Day 34 — Sunday, February 8, 2026 (dayOffset 34)*

The record arrives in a box with no order anyone will admit to choosing. You and the paralegal index it in an evening: 212 pages, each numbered, dated where datable, the gaps listed as gaps — two missing referral pages noted by their absence, which is also a kind of presence.

From tonight, your case has a table of contents. Every later argument in either county can cite page numbers instead of memories.

**Choices:**
- Number and index every page; list the two gaps as items in the index → **statement130**  _(FLAG: recordIndexed ; HIDDEN + Case record indexed by page; gaps listed as items)_
  - NOTE (shown after choosing): 'Gap, pages 88–89' — an absence with an address can be filled. A vague one can't.
- Skim for highlights and trust the inventory → **statement130**
  - NOTE (shown after choosing): Highlights are for reading. Indexes are for winning arguments in buildings that love citations.

## [statement130] The Plan, Amended in Writing
*Day 41 — Sunday, February 15, 2026 (dayOffset 41)*

The current county's supervisor agrees to the transfer and — at Mr. Ndiaye's request, in the meeting, on paper — amends the case plan to document the compelling reason the clock will ask about next spring: reunification is progressing on dated evidence, and filing would not serve the children (the compelling-reason exception, 42 U.S.C. § 675(5)(E), lives or dies on whether the case plan documents it).

A supervisor's spoken agreement is weather. The amended plan, signed and copied to you, is climate.

**Choices:**
- Get the signed amended plan and the transfer letter before you give notice at the warehouse → **school_records**  _(cash −5 ; FLAG: packetBuilt ; HIDDEN + Case plan amended in writing to document the compelling reason before transfer)_
  - NOTE (shown after choosing): Signed, copied, in the folder. The exception now travels as a plan entry, not a hope.
- The supervisor agreed — start the job and let the paperwork follow → **school_records**
  - NOTE (shown after choosing): Paperwork that 'follows' a family across a county line arrives the way luggage follows a traveler: usually, eventually, lighter.

## [school_records] The Schools, Notified in Writing
*Day 47 — Saturday, February 21, 2026 (dayOffset 47)*

Both schools get letters before the move: Iker's counselor and Aitana's teacher, with the new address, the Sunday-dinner continuity plan, and a request — in writing — for the records transfer to include the counselors' own notes, not just grades.

Schools are the system's most honest witnesses because they see children daily and keep their own paper. A transfer that carries the counselors' voices carries your children's ordinary weeks across the line.

**Choices:**
- Send the letters and confirm receipt with both schools → **plan_amended**  _(cash −5 ; FLAG: schoolsNotified ; HIDDEN + Schools notified in writing; records transfer requested with counselor notes)_
  - NOTE (shown after choosing): Receipts confirmed. The children's ordinary weeks will travel with names on them.
- The district handles school transfers automatically → **plan_amended**
  - NOTE (shown after choosing): Districts handle enrollments automatically. Counselor notes travel only when somebody asks, in writing.

## [plan_amended] Moving Day Arithmetic
*Day 55 — Sunday, March 1, 2026 (dayOffset 55)*

The new apartment is smaller and nearer everything: the job, the children's new school, the bus that runs on Sundays. Iker has mapped the route to the foster family's house — they are keeping Sunday dinners, a line in the transfer plan you asked for and got, because continuity is a document too.

The file's journey is less visible: a box, a scan queue, a new county's intake stack. Somewhere between the two buildings, your case becomes somebody's Tuesday.

**Choices:**
- Send the receiving county a one-page introduction with your inventory attached — politely, through your lawyer → **notice_given**  _(cash −5 ; FLAG: introSent ; HIDDEN + Transfer inventory sent to the receiving county through counsel)_
  - NOTE (shown after choosing): The new county meets your case as a list before it meets it as a rumor.
- Wait to be contacted — you're the parent, they'll reach out → **notice_given**
  - NOTE (shown after choosing): They will. Eventually is a date other people's calendars choose.

## [notice_given] Notice, Given Properly
*Day 62 — Sunday, March 8, 2026 (dayOffset 62)*

You give notice at the old warehouse with the offer letter's start date circled, and your supervisor — the one who cut the winter hours — writes you the letter you did not expect: 'rehire-eligible, valued employee,' dated, signed. The file gains a page from an unlikely witness, which is the most believable kind.

Paper does not care about anyone's narrative. It just accumulates, in date order, into a climate.

**Choices:**
- File the supervisor's letter with the employment documents → **benefits_transfer**  _(FLAG: supervisorLetter ; HIDDEN + Former employer's dated reference letter filed)_
  - NOTE (shown after choosing): An unlikely witness, filed. Climates are built from exactly such pages.
- A warehouse reference doesn't belong in a child-welfare file → **benefits_transfer**
  - NOTE (shown after choosing): Everything about stability belongs in the file. The file decides what matters; your job is supply.

## [benefits_transfer] The Other Paperwork
*Day 69 — Sunday, March 15, 2026 (dayOffset 69)*

Benefits, medical cards, the housing program's file — each has its own county queue and its own idea of your address. You spend two days doing the unglamorous crossings: forms, confirmations, reference numbers read back over the phone and written down, because a confirmation number is a document too.

Families lose weeks in these seams. The seams are where the year hides.

**Choices:**
- Log every confirmation number in the folder, dated → **intro_sent**  _(FLAG: seamsLogged ; HIDDEN + Benefits and services transfers logged with confirmation numbers)_
  - NOTE (shown after choosing): Two days of seams, logged. The year will not hide there.
- The agencies will sort the transfers out between themselves → **intro_sent**
  - NOTE (shown after choosing): They will sort most of it, eventually, in some order. The folder prefers certainties.

## [intro_sent] The New County's Reading
*Day 76 — Sunday, March 22, 2026 (dayOffset 76)*

The receiving caseworker, Ms. Quintela, is brisk and not unkind. She has read — you can tell from her questions — the summary. The summary is four pages for a five-month case, and it does what summaries do: your winter becomes 'housing instability, services ongoing,' and the exception documentation becomes a clause.

'Your lawyer sent an inventory,' she says, almost surprised. 'The plan amendment is in it. The visit log is in it.' She turns a page. 'Mostly, things arrive thinner than this.'

**Choices:**
- Ask her to confirm, in writing, that the packet arrived complete against the inventory → **intake_call**  _(FLAG: arrivalConfirmed ; HIDDEN + Receiving county confirmed complete arrival against the inventory)_
  - NOTE (shown after choosing): 'Mostly' is doing heavy lifting in that sentence. The confirmation makes it arithmetic.
- Take her word — the important parts are clearly here → **intake_call**
  - NOTE (shown after choosing): The important parts are here. The confirmation is for the part you'll need in April, sight unseen.
- Skip the introduction, the walk, and the confirmation — the box is taped and the case is moved → **end_thin130**
  - NOTE (shown after choosing): What arrives will be whatever arrives. That is not a plan; it is a hope with a tracking number.

## [intake_call] The Intake Call
*Day 84 — Monday, March 30, 2026 (dayOffset 84)*

Ms. Quintela calls before the box even arrives — your lawyer's introduction letter saw to that — and the call is brisk: she has the summary, expects the file Friday, and asks three questions the summary couldn't answer. You answer them from the index, by page number.

There is a pause. 'You have the record,' she says. It is not quite a compliment. It is better: it is a recalibration.

**Choices:**
- Offer to walk the inventory with her when the box lands, page by page → **confirm_whole**  _(FLAG: walkOffered ; HIDDEN + Page-by-page inventory walk offered to the receiving worker)_
  - NOTE (shown after choosing): An offer that makes 'mostly arrived' impossible to say with a straight face.
- Let the file speak when it arrives → **confirm_whole**
  - NOTE (shown after choosing): It will — in the order it fell into the box. The walk imposes your order.

## [confirm_whole] School, Services, Sundays
*Day 97 — Sunday, April 12, 2026 (dayOffset 97)*

Autumn runs on the new county's rails: Iker's school counselor writes a stability letter; Aitana's teacher sends home a reading chart with stars; your services continue with a provider across the line, the referral re-sent with dates you requested in writing because the habit is now load-bearing.

The Sunday dinners continue. The foster parents' countersigned log continues. The file, in its new building, grows at the same dated pace as the old one.

**Choices:**
- Keep the rhythm: every letter filed, every log countersigned, the folder mirrored → **file_gap_found**  _(FLAG: rhythmKept ; HIDDEN + Documentation rhythm maintained after transfer)_
  - NOTE (shown after choosing): Transfers test habits. Habits, kept, become the record's accent: this family's paper sounds the same in both counties.
- Relax the paperwork — the new county clearly has the picture → **file_gap_found**
  - NOTE (shown after choosing): It has the picture as of July. Courts read the whole film.

## [file_gap_found] Page 88
*Day 108 — Thursday, April 23, 2026 (dayOffset 108)*

The walk finds it: pages 88–89 of the record — the referral chronology, the very heart of the services story — did not survive the trip. A scan queue ate them, or a box did. Entropy does not sign its work.

This is the moment the whole strategy was built for. A loss that can be proved can be cured; a loss that can't be proved becomes the case. You have the inventory, the index, and the second set.

**Choices:**
- Produce the second set's copies of pages 88–89 and amend the arrival confirmation to note the cure → **packet_resent**  _(cash −5 ; FLAG: gapCured ; HIDDEN + Missing pages cured from the family's second set; confirmation amended)_
  - NOTE (shown after choosing): Cured, noted, closed. The chain of custody holds — because it was a chain.
- Ask the sending county to re-send and hope the queue is kinder → **packet_resent**
  - NOTE (shown after choosing): Hope is not a custody procedure. The copies in your sister's closet are.

## [packet_resent] The Amended Confirmation
*Day 121 — Wednesday, May 6, 2026 (dayOffset 121)*

Ms. Quintela signs the amended confirmation herself: file complete as of today, two pages restored from the family's copy, restoration noted. 'In nine years,' she says, 'no family has ever handed me back my own file's missing pages.'

'In nine years,' you could say, 'no family was told to count.' You don't. The confirmation is signed. Some victories are complete in a signature and spoiled by a speech.

**Choices:**
- File the amended confirmation at the front of the new county's packet → **rhythm**  _(FLAG: amendedFiled ; HIDDEN + Amended arrival confirmation filed at the packet's front)_
  - NOTE (shown after choosing): Front of the packet: the proof that this file is whole, signed by the other side.
- Keep the confirmation in your folder only → **rhythm**
  - NOTE (shown after choosing): Your folder already believes you. The county's file is the one that needed convincing.

## [rhythm] The Receiving Review
*Day 150 — Thursday, June 4, 2026 (dayOffset 150)*

The new county's first full review is in October. The judge is new to your family; the file is not new to itself. She reads the amended plan's compelling-reason entry, the arrival confirmation, the school letters, the log.

'This case transferred,' she says, to no one in particular. 'They don't usually arrive like this.' It is the closest thing to applause this hallway gives.

**Choices:**
- Ask, through counsel, for the step-down the plan promised: overnights expanding to a trial return before the holidays → **fall_review**  _(REQUIRES FLAG: recordsRequested ; REQUIRES FLAG: packetBuilt ; REQUIRES FLAG: arrivalConfirmed)_
  - NOTE (shown after choosing): The plan promised it in the other county's ink. Plans, unlike summaries, bind their authors.
- Ask for immediate return — the file is overwhelming → **end_trial130**
  - NOTE (shown after choosing): Overwhelming files still end in steps. The best ending needed the plan's own words, quoted.
- Let the review ride on the file without proposing the step-down → **end_trial130**
  - NOTE (shown after choosing): Files propose nothing. People propose; files support.

## [fall_review] The Fall Review
*Day 185 — Thursday, July 9, 2026 (dayOffset 185)*

The receiving county's fall review is short. The judge works the plan box by box — the new county's services now have your requested dates attached, the schools' letters are in, the Sunday log continues — and the hearing has the texture the winter one never did: a court reading a file that reads back coherently.

'Step-down in the spring,' the judge says, 'if the winter looks like the fall.' It is a conditional sentence, and for the first time in the case, the condition is one your habits can meet.

**Choices:**
- Ask for the condition in the order's words: overnights by spring if the log and letters continue → **goal_question**  _(FLAG: conditionWritten ; HIDDEN + Step-down condition written into the review order)_
  - NOTE (shown after choosing): Conditions in orders bind. Conditions in memories evaporate.
- Accept the judge's tone as the promise → **goal_question**
  - NOTE (shown after choosing): Tone is not an order. The clerk types orders.

## [goal_question] The Goal, Questioned Once
*Day 214 — Friday, August 7, 2026 (dayOffset 214)*

In November the agency's report floats the sentence every long case eventually hears: whether the goal should be revisited in light of 'the extended timeline.' It is one sentence in a long report, and it is how goal changes begin — not with motions, but with weather.

Your answer is already in the file: the plan's own compelling-reason entry, the dated progress in two counties, the judge's conditional sentence. Weather is answered by climate, and climate is made of paper.

**Choices:**
- File a short written response quoting the plan's entry and the fall order, with dates → **holiday_visits**  _(cash −5 ; FLAG: goalAnswered ; HIDDEN + Goal question answered in writing from the plan and orders)_
  - NOTE (shown after choosing): One sentence, answered by three documents. The weather passes.
- Raise your objection verbally at the team meeting → **holiday_visits**
  - NOTE (shown after choosing): Meetings adjourn. Sentences in reports get quoted. Write the reply where the quote lives.

## [holiday_visits] The Holidays, Documented
*Day 243 — Saturday, September 5, 2026 (dayOffset 243)*

December in the new apartment: a tree Iker insists on measuring, Sunday dinners that now run in both directions — the foster parents come to you, bringing the pie and, one week, the original sign-in binder, retired with honors.

The caseworker visits, photographs the tree for the file, and writes 'home environment warm and organized' in the tone of a woman closing a question. Some sentences in files are endings wearing the costume of notes.

**Choices:**
- Keep the holiday log and file the caseworker's note with it → **spring_review**  _(FLAG: holidayLogged ; HIDDEN + Holiday period logged; favorable home-visit note filed)_
  - NOTE (shown after choosing): The winter that started the case, answered by a documented December.
- Holidays are private — keep them out of the paperwork → **spring_review**
  - NOTE (shown after choosing): Privacy is a value. So is a warm sentence in a file, in December, where a judge will find it in March.

## [spring_review] The Fifteenth Month, Elsewhere
*Day 455 — Monday, April 5, 2027 (dayOffset 455)*

Monday, April 5, 2027 — fifteen months from entry — arrives in the new county like weather in another town: noted, prepared for, unspectacular. The filing question is asked, as the statute requires it to be asked (42 U.S.C. § 675(5)(E)), and answered from the case plan the old county amended and the new county confirmed: a compelling reason, documented, that filing would not serve these children — while the trial return runs and the goal, never changed, completes itself.

No one calls this a victory in the hallway. It is a non-event with a paper trail, which is what winning a clock actually looks like.

**Choices:**
- Finish it: convert the trial return to full return at the spring review, aftercare in writing → **end_whole**
  - NOTE (shown after choosing): The last document of the case is the shortest: an order, two pages, both counties' ink on the story it closes.
- Let the trial period simply run out without a closing order → **end_trial130**
  - NOTE (shown after choosing): Open files invite new summaries. Close the file the way you carried it: in writing.

## [end_whole] Ending — The File Arrived Whole
*Day 470 — Tuesday, April 20, 2027 (dayOffset 470)*

The children come home for good in April, fifteen months after they left, in a different county from the one that took the case and the same family that finished it. Iker's map of the Sunday-dinner route is retired to the refrigerator, an artifact of the year the family lived in two places and the file lived in one piece.

At the closing, Ms. Quintela says the sentence you will remember longest: 'Your case was the only transfer this year that arrived with everything it left with.' It was not luck. It was an inventory, a confirmation, and a plan amended in ink before the box was taped.

**Ending.**

**Debrief:**
- THE TRANSFER'S LAW — The permanency clock does not pause for geography: entry Monday, January 5, 2026; fifteen of the most recent twenty-two months arrived Monday, April 5, 2027, in whichever county then held the case (42 U.S.C. § 675(5)(E)). The compelling-reason exception exists only as documentation — a case plan that says, in so many words, why filing would not be in the child's best interest — which is why the amendment was secured in writing before the move, from the county that knew the facts.
- THE PAPER CHAIN — Record requested before departure (55 Pa. Code § 3130.44(d); redactions under (f)); an inventory built with counsel (42 Pa.C.S. § 6337); a dated statement filed beside an early, hardening case note; written confirmation of complete arrival. Each link is small. The chain is the strategy: a loss can only be proved — and therefore prevented — against a list.
- WHAT NO STRATEGY CONTROLS — The receiving county's staffing, the new judge, the scan queue. Transfers lose pages in real systems; this route's claim is that the loss, had it happened, would have been visible, dated, and curable — because someone counted the file before it traveled and after it landed.

## [end_trial130] Ending — Home on a Longer Leash
*Day 470 — Tuesday, April 20, 2027 (dayOffset 470)*

The children do come home — on a trial basis that stretches across the spring, with the case open in the new county until summer. Nobody lost anything except time and certainty: the two currencies transfers spend.

The fifteenth month passes during the trial period, the filing question answered by the trial itself. It ends well. It ends the way cases end when the file arrives mostly whole: well, eventually, with extra hearings.

**Ending.**

**Debrief:**
- A PARTIAL WIN, NAMED HONESTLY — Return home, on the system's longer schedule. What separated this ending from the best one was the chain's paperwork: the pre-move record request (**recordsRequested**), the compelling-reason packet documented in the plan (**packetBuilt**), and the written arrival confirmation (**arrivalConfirmed**) that let the new court enforce the old county's plan as written.
- WHAT NO STRATEGY CONTROLS — Intake stacks, staffing, and the receiving judge's caution. A file that arrives whole still gets read by a stranger; the strategy's promise is only that the stranger reads your record, not a summary of it.

## [end_thin130] Ending — The Thin File
*Day 240 — Wednesday, September 2, 2026 (dayOffset 240)*

In this branch the transfer happened the way it usually does: a summary traveled, the packet didn't, and the receiving county met a four-page family. The compelling reason had been agreed — verbally, in a room in another county — and agreements do not transfer.

The new plan, written from the summary, does not mention an exception. The goal is questioned at the fall review; the filing conversation starts early and from the wrong end. The case is not over. But from here, the family must rebuild in a new building the record it already built once — the cruelest line item in any transfer, paid in months.

**Ending.**

**Debrief:**
- WHAT WAS LOST, ITEMIZED — Not effort, not progress: paper. The record never requested before departure (55 Pa. Code § 3130.44(d)); the compelling-reason documentation never entered into the case plan, where 42 U.S.C. § 675(5)(E) requires it to live to count; the arrival never confirmed against an inventory, so the loss itself could not be proved or repaired. The debrief is the inventory, read too late.
- WHAT NO STRATEGY CONTROLS — County systems are separate buildings with separate habits, and the clock (entry January 5, 2026; fifteen months April 5, 2027) reports to neither. The strategy for a crossing case is chain-of-custody thinking applied to a family's own story: count it, confirm it, and never let a summary travel alone.
