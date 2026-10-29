# THE FIRST 90 DAYS — Scenario 112: “The Empty Months”

*Human-readable script. This document and `scenario-112.json` are generated from a single source and match node-for-node: same IDs, same order, same choices, same effects.*

**The family is fictional — a composite. No real person's story appears here.**

**Content note:** This scenario depicts a grandmother caring for her two grandchildren as a kinship caregiver while her caregiver approval and payments are delayed for months, told through stamped copies, call logs, a case chronology, and a permanency review. There is no graphic content. Players may skip any scene or use the quick exit at any time.

**How to read effects:** `cash −40` changes the player's cash. `FLAG: name` sets a flag the engine tracks. `HIDDEN + item` means the case file quietly records that item at this choice — the player does not see it when it happens. `REQUIRES FLAG: name` means the choice is only available if that flag was set earlier; `REQUIRES NO FLAG: name` means it is only available if that flag was never set. `NOTE:` is text shown to the player right after choosing.

Start date: Monday, January 12, 2026. Day offsets are days since the scenario's start date. Tier: Complex.

## [start] Two Children, One Kitchen Table
*Day 0 — Monday, January 12, 2026 — Monday, January 12, 2026 (dayOffset 0)*

Your name is Bernice. You are sixty-four, retired from thirty-one years of school kitchens, and since Monday, October 20, 2025 your house has held two more people: your grandchildren, Joaquin, who is eight, and Mireya, who is four. They came to you as a kinship placement when their mother — your daughter, Dena — entered the part of her case that could not be done with children in the house. The children are Dena's case. The beds, the lunches, the nightmares at two in the morning: those are yours.

In the first week you did the caregiver paperwork the way you have done every form since 1987: completely, in ink, with copies. You submitted your approval packet on Friday, October 24, 2025 and kept the stamped copies in a folder on the kitchen table. The payments that were supposed to follow the packet have not followed. The answer, every time you ask, is the same two words: in process.

Your savings were not large. They were, however, yours — and for almost three months they have been quietly doing the job the missing payments were supposed to do. This story is about those empty months, and about what a file does with a grandmother who is running out of money keeping two children fed.

**Choices:**
- Open the folder on the kitchen table — the one with the stamped copies → **folder_copies**
  - NOTE (shown after choosing): The folder is the first character in this story after you. It will be in more rooms than you will.

## [folder_copies] The Stamped Copies
*Day 2 — Wednesday, January 14, 2026 — Wednesday, January 14, 2026 (dayOffset 2)*

The folder holds your whole half of the paperwork: the approval packet's stamped copy, dated Friday, October 24, 2025; the home-study notes; the children's school and clinic papers; a call log you started in November, in pencil, because a woman at the senior center told you that in this system a date you cannot show is a date that did not happen.

Nothing in the folder is dramatic. That is its power. Stamps, dates, initials — the small change of a case, kept by the one person in it who was never issued a file cabinet.

What the folder does not hold is any explanation of the missing payments. Explanations, so far, have all been spoken.

**Choices:**
- Call the agency and ask, again, where the payments are → **payment_call1**
  - NOTE (shown after choosing): You write the date of the call at the top of a fresh page before you dial. Habits are strategies that have stopped introducing themselves.

## [payment_call1] In Process, Again
*Day 5 — Saturday, January 17, 2026 — Saturday, January 17, 2026 (dayOffset 5)*

The call on Saturday, January 17, 2026 goes the way the December calls went. The worker who answers is polite. The packet is in process. Processing takes time. There is nothing you need to do — that sentence, again — and nothing she can tell you about when it will finish.

You ask whether anything is missing from the packet. Nothing is missing, she says. You ask whether anything needs a signature. Not yours, she says — which is true, and is also, though neither of you knows it yet, the most precise sentence anyone will say about this case for weeks.

You write it all in the log: the date, the words, the name of the person who said them. The log is getting long. Long logs are either a burden or an exhibit, depending on whether anyone ever has to read one.

**Choices:**
- Thank her, hang up, and do the week's grocery math at the table → **grocery_math**  _(HIDDEN + Call log — payment inquiry; agency answer: packet in process, nothing missing, no signature of caregiver's needed)_
  - NOTE (shown after choosing): The math is next. Math, in this house, is also a document.

## [grocery_math] The Grocery Math
*Day 9 — Wednesday, January 21, 2026 — Wednesday, January 21, 2026 (dayOffset 9)*

Two children eat the way weather happens: constantly, and without consulting anyone. The week's groceries, the school lunch account, Mireya's clinic co-pay, Joaquin's outgrown shoes — the list on the refrigerator is ordinary, and the total is not, and the difference between those two facts is coming out of an account that was supposed to be for your old age.

You are not careless with money. You are careful with money in a house whose income stopped matching its size in October, for reasons that live in a folder marked in process.

A neighbor asks how the agency lets this happen. You tell her the truth: nobody has let anything happen, visibly. That is the problem. Invisible things do not get fixed; they get described — later, by other people, in other words.

**Choices:**
- Pay for the week's groceries and the shoes, and write the total in the log → **dena_sunday**  _(cash −24)_
  - NOTE (shown after choosing): Twenty-four dollars this round, and not the last round. The log gains a column it never wanted.

## [dena_sunday] Dena, on Sunday
*Day 13 — Sunday, January 25, 2026 — Sunday, January 25, 2026 (dayOffset 13)*

Dena visits on Sundays, at your table, in the part of the week that still belongs to the family instead of the case. She is doing the work her plan asks of her — the counselor's reports say so, in their careful language — and the children treat her arrival the way they treat weather clearing.

She asks about the money. You tell her some of it: the payments are still in process; the savings are holding. She hears the part you did not say, the way daughters do. “Mom. If this gets bad because of paperwork—”

“Then we will fix the paperwork,” you say, with more confidence than the folder currently justifies. It is the truest sentence available. It is also a promise, and promises, in this family, get logged too.

**Choices:**
- Walk her to the bus, and come home to the week's ordinary work → **letter_in_process**
  - NOTE (shown after choosing): Ordinary work: lunches, laundry, a form for Joaquin's school that asks for a guardian signature you can actually give.

## [letter_in_process] The Letter That Says Nothing, in Writing
*Day 16 — Wednesday, January 28, 2026 — Wednesday, January 28, 2026 (dayOffset 16)*

A letter arrives from the agency, and for one envelope's width your heart does the thing it has learned to do. Inside: a single page confirming that your caregiver approval remains in process and that payments will commence upon approval. It is dated Wednesday, January 28, 2026. It does not say what is being processed, or by whom, or what remains to happen.

You file it behind the stamped packet copy, where it belongs: the agency's own words, in writing, saying that in the third month of two children living in your house, the paper that pays for their care had still not finished moving.

Letters like this are not answers. They are timestamps with letterhead. Timestamps, assembled later, become chronologies — and chronologies are the one language every room in this system reads.

**Choices:**
- File the letter, and get ready for the home visit this week → **home_visit**  _(HIDDEN + Agency letter — approval still in process in the third month of placement; payments to commence upon approval)_
  - NOTE (shown after choosing): Stamped copy, meet letter. The folder is becoming a conversation the agency does not know it is having.

## [home_visit] The Visit That Goes Fine
*Day 18 — Friday, January 30, 2026 — Friday, January 30, 2026 (dayOffset 18)*

The home visit goes fine, because your home is fine. The worker — the first one, Ms. Larkin, who has carried the case since October — walks the rooms, compliments Mireya's drawing taped to the refrigerator, confirms the children are settled, in school, in routine.

She asks how you are managing. You say what grandmothers say: we manage. She writes something down. What she writes, you will not see for weeks — and when you do see it, the gap between we manage and what the note made of it will be one of this story's lessons.

Nothing about the visit is wrong. That is worth saying plainly, because what happens later does not require anyone to have been wrong in this room. It only requires a file that keeps summaries and loses causes.

**Choices:**
- See her out, and help Joaquin with the homework he has been avoiding → **worker_goodbye**
  - NOTE (shown after choosing): Fractions. He is better at them than he believes. So, it turns out, are you — the household kind.

## [worker_goodbye] A Goodbye in the Hallway
*Day 21 — Monday, February 2, 2026 — Monday, February 2, 2026 (dayOffset 21)*

Ms. Larkin is leaving the agency — a new job, a shorter commute, the ordinary weather of other people's lives. She tells you at the door, kindly, and says the case will transfer and the new worker will have the file.

The file. Everything the new worker will know about Joaquin, Mireya, Dena, and you will arrive as paper: reports, notes, summaries — and somewhere in it, an approval packet that has been in process since Friday, October 24, 2025.

Worker changes are not anyone's fault. They are, however, resets: whatever the departing worker knew in her head — and she knew the payments were late, because you told her monthly — leaves with her head. What stays is what the paper says.

**Choices:**
- Thank her, wish her well, and write the transfer in the log → **new_worker**
  - NOTE (shown after choosing): One line in the log: worker changed. Underneath it, everything the new worker will have to learn from a file.

## [new_worker] The New Worker Reads the Summary
*Day 24 — Thursday, February 5, 2026 — Thursday, February 5, 2026 (dayOffset 24)*

The new worker, Mr. Osei, is courteous, prepared, and working from the summary — which is to say, from the shortest version of your family that exists. He knows the children are placed with their grandmother. He knows Dena's plan is progressing. What the summary says about your approval, in full, is the two words you could have predicted.

He has a suggestion, offered helpfully, the way resets always offer themselves: the fastest way to get the approval moving, he says, is to resubmit the packet — fresh copies, current dates, a clean start for the file.

A clean start. Your folder, with its stamped copy from Friday, October 24, 2025, sits in your bag like a second opinion.

**Choices:**
- Decide what to put in front of him: the stamped copies, or a fresh packet → **resubmit_beat**
  - NOTE (shown after choosing): This is a small choice with a long shadow: whether the file learns that the packet already exists, with a date on it.

## [resubmit_beat] Resubmit, or Show the Stamp
*Day 26 — Saturday, February 7, 2026 — Saturday, February 7, 2026 (dayOffset 26)*

Resubmitting is easy, and ease is its own argument: new copies, new date, no friction with the new man in his first month. It also has a cost that does not appear on any form: a fresh packet carries a fresh date, and a fresh date quietly rewrites when this began. October becomes this week. The empty months become nobody's months — a gap with no start, attributable to no one, and therefore, in the way of files, attributable to you.

Or you can do the slightly harder thing: lay the stamped copy on the table — submitted Friday, October 24, 2025, stamp and all — and ask, politely, that the file note what already happened before anyone resubmits anything.

**Choices:**
- Lay the stamped copy on the table and ask that the original submission date be noted in the file → **resubmit_after**  _(FLAG: submissionProven; HIDDEN + Approval packet — original submission date shown from caregiver's stamped copy and noted)_
  - NOTE (shown after choosing): He photographs the stamp for the file. October is back in the record, where October belongs.
- Resubmit a fresh packet — clean start, no friction → **resubmit_after**
  - NOTE (shown after choosing): The new copies are accepted warmly. The fresh date is clean, recent, and — in every way that will matter later — wrong about when this started.

## [resubmit_after] What the File Now Knows
*Day 28 — Monday, February 9, 2026 — Monday, February 9, 2026 (dayOffset 28)*

Whichever paper you handed over, the meeting ends the same way on the surface: Mr. Osei will check on the approval, and the approval will take the time it takes. The difference is underneath, in what the file can now say about the months behind you.

A file that knows a packet was submitted in October tells one story about a grandmother's empty months. A file whose earliest packet is dated this week tells another — and the second story has a hole in it exactly the shape of your savings account.

You go home and write the meeting in the log, either way. Logging is what you do instead of shouting, and it has better handwriting.

**Choices:**
- Go home — Joaquin's school form is due, and Mireya has opinions about dinner → **school_costs**
  - NOTE (shown after choosing): The case pauses for no one's childhood. That is the case's flaw and the children's protection, in one sentence.

## [school_costs] School Costs, Clinic Costs
*Day 30 — Wednesday, February 11, 2026 — Wednesday, February 11, 2026 (dayOffset 30)*

Joaquin needs a field-trip fee and a permission slip. Mireya needs a clinic follow-up and a prescription that costs what prescriptions cost. Neither item is large. Together with the month's groceries they are the arithmetic that has been running since October, arriving in its usual installments.

You pay, because the alternative — children going without, so that a grandmother's file can look comfortable — is not an alternative anyone in this house is willing to file.

The log's money column is now the most honest document in the case. It is also, read cold by a stranger, the most dangerous one: it shows strain, and strain, in a summary, can be made to mean almost anything.

**Choices:**
- Pay both, log both, and check the savings balance you have been avoiding → **savings_low**  _(cash −18)_
  - NOTE (shown after choosing): Eighteen dollars this round. The balance, when you look, is a number with a date attached whether you write it down or not.

## [savings_low] The Balance, Looked At
*Day 33 — Saturday, February 14, 2026 — Saturday, February 14, 2026 (dayOffset 33)*

The savings account that took a decade of school-kitchen overtime to build is down to its last layer. You do the arithmetic three times, the way people do when the answer is the problem: at this rate, the house has weeks of cushion left, not months.

Two honest options sit on the table, and this scenario will not pretend either is painless. You can keep going — keep the house, keep the routine, and fight the paperwork with what is left. Or you can give the agency written notice that you cannot continue as the placement if the payments do not begin — a true statement, with a consequence you can see from here: a disrupted placement, and two children moved to strangers while the adults argue about a signature.

Nobody should have to choose between those at a kitchen table. The choice is here anyway, because the empty months put it here.

**Choices:**
- Keep going — and fight the paperwork with what is left → **strain_note**
  - NOTE (shown after choosing): Not heroism. Arithmetic plus stubbornness, logged like everything else.
- Give written notice that you cannot continue without the payments → **notice_beat**
  - NOTE (shown after choosing): A true sentence, sent in writing. True sentences still have consequences, and this one's are immediate.

## [notice_beat] The Notice, Sent
*Day 35 — Monday, February 16, 2026 — Monday, February 16, 2026 (dayOffset 35)*

The notice is short, factual, and the hardest page you have ever signed: at the current rate of household spending, with no caregiver payments received since the children's arrival, you cannot continue the placement beyond the end of the month. You keep the stamped copy. Of course you keep the stamped copy.

The agency answers the way systems answer ultimatums they cannot process: with urgency about the children and silence about the packet. A placement meeting is mentioned. A foster home is mentioned — as a contingency, everyone says, in the tone people use for a word they hope will frighten you back into silence.

It does not frighten you. It informs you, precisely, of what the empty months were always risking — and you make the decision the notice was written to force, in the only direction left.

**Choices:**
- Tell the children, at their sizes, that a change is coming → **end_disrupt**
  - NOTE (shown after choosing): Joaquin asks if it is because of money. You tell him the truth at his size, which is the only size truth should ever be told to children.

## [strain_note] The Word in the Summary
*Day 36 — Tuesday, February 17, 2026 — Tuesday, February 17, 2026 (dayOffset 36)*

A copy of a case summary reaches you through Dena — a page she was given for her own plan meeting — and there it is, in the summary's flat language, next to your name: caregiver experiencing financial strain.

Five words. Every one of them true, and the sentence they make is false — because the summary records the strain and not its cause, the way a photograph of a flood records water and not the broken pipe. Somewhere ahead is a review, and reviews read summaries, and a summary that says strain, standing alone, can be read as a question about whether this placement is stable.

You sit with the page a long time. Then you do the thing this whole story has been teaching: you ask what paper could sit beside it.

**Choices:**
- Ask Dena who can explain what a review will do with a line like that → **advocate_beat**  _(HIDDEN + Case summary — 'caregiver experiencing financial strain,' with no cause stated)_
  - NOTE (shown after choosing): Dena has a lawyer. Lawyers, in this system, are translators between families and files.

## [advocate_beat] What a Review Actually Decides
*Day 39 — Friday, February 20, 2026 — Friday, February 20, 2026 (dayOffset 39)*

Dena's lawyer is Ms. Hart, provided for Dena as a party's counsel in this case (42 Pa.C.S. § 6337). She meets you both in a courthouse conference room and translates the review into its working parts, the way she would want it translated for her own mother.

“A permanency review is a hearing with a list,” she says. “The court determines whether the placement is still necessary, whether the plan is being complied with, what progress has been made, and whether reasonable efforts were made to finalize the plan. (42 Pa.C.S. § 6351(f)(1), (2), (3), (5.1)) Every one of those is decided from evidence — from paper that is actually put in front of the judge.”

“Right now,” she says, “the paper in front of the judge-to-be says strain, and nothing about a packet. If we want the judge to weigh a cause, the cause has to arrive as documents. And the first document we need is the agency's own chronology — which you, Bernice, cannot request. That right belongs to the case's subjects. Dena can.”

**Choices:**
- Look at Dena — the asking is about to become hers to make → **dena_ask**
  - NOTE (shown after choosing): The regulation's right belongs to the case's subjects, not to a placement applicant. Ms. Hart says it plainly so no one mistakes whose signature this needs.

## [dena_ask] Asking Dena
*Day 42 — Monday, February 23, 2026 — Monday, February 23, 2026 (dayOffset 42)*

The request itself is simple: Dena, as the children's mother and a party to the case, signs a written request for the case record — the chronology, the approval file, the placement notes — which under the regulation “shall be released upon request” (55 Pa. Code § 3130.44(d)). You cannot sign it; your name on it would make it a placement applicant's letter, and the right is not yours. Dena's name makes it what the rule contemplates.

Asking her is not simple. She is mid-treatment, mid-plan, carrying her own file's worth of judgments. You can ask her to carry this one page too — at your kitchen table, with the folder open and the stamped packet copy on top — or you can spare her, and build the review answer from your folder alone.

**Choices:**
- Ask Dena, at the kitchen table, to sign the record request this week → **dena_after**  _(cash −4; FLAG: recordsRequested; HIDDEN + Case record requested in writing by the children's mother, a party, under 55 Pa. Code § 3130.44(d), at the kinship caregiver's asking)_
  - NOTE (shown after choosing): She reads it twice, asks two exact questions, and signs. Four dollars of copies. The request is dated, copied, and kept with the plan.
- Spare Dena — build the answer from your own folder alone → **dena_after**
  - NOTE (shown after choosing): A kindness with a price: your folder knows your half cold. The agency's chronology — the half with the signature page in it — stays unread.

## [dena_after] A Signature That Is Hers
*Day 44 — Wednesday, February 25, 2026 — Wednesday, February 25, 2026 (dayOffset 44)*

Whether the request went out over Dena's signature or stayed in the folder as a road not taken, the week moves the way weeks in this house move: school runs, a clinic visit, Dena's Sunday table, Joaquin's fractions improving against his will.

If Dena signed, the request is now a page in the file it asks about — which means the chronology, when it comes, will come because a party asked for it in writing, on a date, and dates are the spine of everything you are building.

Ms. Hart's instruction for the waiting is one sentence: keep logging. “Chronologies answer chronologies,” she says. “Yours is the only other one in this case. Keep it boring and keep it exact.”

**Choices:**
- Keep the log, keep the house, and wait for the packet to answer → **dena_progress**
  - NOTE (shown after choosing): Boring and exact. A decade of school kitchens taught you both, in that order.

## [dena_progress] Dena's Progress, in Careful Language
*Day 46 — Friday, February 27, 2026 — Friday, February 27, 2026 (dayOffset 46)*

Dena's counselor's report arrives for her plan meeting, and Dena — who is learning, at thirty-one, to read her own file without flinching — shows it to you at the table. Progress, in the careful language: attendance complete, goals met, the plan on its rails.

It matters here for a plain reason: the review ahead is about the children's placement, and the children's placement is steady partly because their mother is steady and their grandmother's house is the fixed point both of those steadinesses lean on. A review that reads strain without reading any of this will be reading a summary, not a family.

“Tell them the house part,” Dena says. “Not me. The house.” She means: make the paper show what the house has actually been doing. It is the best legal advice anyone gives in this story, and she gives it for free.

**Choices:**
- Put her report copy in the folder, beside your log → **record_arrives**
  - NOTE (shown after choosing): Two files becoming one folder, at a kitchen table, without anyone calling it a strategy.

## [record_arrives] The Chronology Arrives — Or Doesn't
*Day 49 — Monday, March 2, 2026 — Monday, March 2, 2026 (dayOffset 49)*

If Dena's request went out, the packet arrives the way records arrive: thick, partly blacked out, and heavier than its paper. If it never went out, what you have instead is the summary Dena was given, your folder, and your log — true, dated, and entirely from your side of the desk.

Either way, Ms. Hart spreads what exists on her conference table and goes looking for one line: the approval packet's journey through the agency, in the agency's own chronology. Received, routed, signed, paid — the verbs a packet is supposed to collect on its way through a building.

What the chronology shows — if you are holding the chronology — stops both of you mid-sentence.

**Choices:**
- Read the approval lines together, slowly → **signature_page**
  - NOTE (shown after choosing): Slowly is how you read a page you have been waiting three months to see.

## [signature_page] The Blank Line
*Day 52 — Thursday, March 5, 2026 — Thursday, March 5, 2026 (dayOffset 52)*

The chronology, in the agency's own hand, is short enough to memorize. Approval packet received: Friday, October 24, 2025 — your stamped copy's date, confirmed by the other side of the desk. Routed for signature: the following week. And then — nothing. No signature entry. No approval entry. No payment entry. Month after month of nothing, in a column where nothing is itself the entry.

On the packet's own signature page, reproduced in the packet Dena requested, the line where an approver was to sign sits blank beneath a routing stamp from the week the children arrived. The packet did not fail an inspection. It was never inspected. It sat — unsigned, unacted on, unmentioned — while the file learned to call your savings account a stability question.

Nobody in the room says villain. Ms. Hart says the useful word instead: “Documented.”

**Choices:**
- Ask her what a documented blank line can do at a review → **bank_book**  _(HIDDEN + Agency chronology — approval packet received and routed the week the children arrived; no signature, approval, or payment entry thereafter)_
  - NOTE (shown after choosing): A blank line with a routing stamp above it. The smallest exhibit in this story, and the largest.

## [bank_book] Your Side of the Ledger
*Day 55 — Sunday, March 8, 2026 — Sunday, March 8, 2026 (dayOffset 55)*

Your bank book is the other half of the chronology, and it needs no lawyer to read it: a balance line descending, month by month, in amounts that match — almost to the dollar, because you logged them — the groceries, the shoes, the clinic, the lunch account. Two documents, kept by two institutions that have never spoken, telling one story in two columns.

Ms. Hart puts them side by side on the table: their silence, your spending. “This,” she says, “is what attribution looks like when it is made of paper instead of adjectives. The gap has a start date, a routing stamp, and a blank line. The strain has the same start date. A judge does not need to be persuaded of anything. A judge needs to be shown a calendar.”

What remains is assembly: turning two columns into one page a review can hold.

**Choices:**
- Ask her to lay out the assembly, step by step → **counsel_meet112**
  - NOTE (shown after choosing): Assembly is a humble word for the most important work in this case.

## [counsel_meet112] The Assembly, Step by Step
*Day 58 — Wednesday, March 11, 2026 — Wednesday, March 11, 2026 (dayOffset 58)*

“Step one,” Ms. Hart says, “is the chronology page — one page, dates only, every line checkable against a document: children placed, packet submitted, in-process letter, worker changed, resubmission requested, strain noted. Step two is the exhibits behind it: the stamped copy, the chronology's approval lines, the signature page, your log, your bank book. Step three is filing it — with the agency and the court, in writing, before the review — so the review reads it in advance instead of meeting it as a surprise.”

“And step zero,” she says, “is the one you have already done, since October, without knowing its name: you kept the copies. Everything we are about to build is built out of a folder on a kitchen table. Grandmothers who throw paper away do not get this meeting.”

The review, she reminds you, will make its determinations from evidence (42 Pa.C.S. § 6351(f)). The plan is to make sure the evidence includes a cause.

**Choices:**
- Build the one-page chronology with her, from the documents only → **chronology_build**
  - NOTE (shown after choosing): Documents only. If a line cannot be checked against a page, it does not go on the page.

## [chronology_build] One Page, Dates Only
*Day 61 — Saturday, March 14, 2026 — Saturday, March 14, 2026 (dayOffset 61)*

The page assembles the way the log was kept: without adjectives. Placed with grandmother. Packet submitted — stamped copy attached. Agency letter: still in process. Worker changed; resubmission requested; original submission date shown and noted. Record requested by the children's mother; chronology received; approval lines end at a blank signature line. Household spending logged throughout; savings drawn down across the same months.

It fits on one page because the truth of it is not complicated. It only needed to be assembled before a room that runs on summaries could summarize it wrongly.

**Choices:**
- Build it — one page, dates only, every line checkable → **chronology_after**  _(cash −6; FLAG: chronologyBuilt; HIDDEN + One-page chronology — placement, packet submission, agency lag, and household drawdown assembled from documents)_
  - NOTE (shown after choosing): Six dollars of copies, in triplicate. One page that answers five words — caregiver experiencing financial strain — with eleven dates.
- Carry the documents loose — the folder can speak for itself at the review → **chronology_after**
  - NOTE (shown after choosing): Folders do not speak. Pages assembled from them do. The exhibits are real either way; only one version of them is readable in twenty minutes.

## [chronology_after] Eleven Dates
*Day 63 — Monday, March 16, 2026 — Monday, March 16, 2026 (dayOffset 63)*

The chronology page, finished, is the least emotional document you have ever made about the most emotional winter of your life, and Ms. Hart reads it the way judges read: once, quickly, and then again at the line where the approval column stops.

“There,” she says. “That is the whole case, and it took eleven dates. Everything else — the strain, the stability question, the payments — is commentary on this page. Our job now is to make the review do its commenting with this page open.”

Two errands remain: a written confirmation from the payments office, and the filing itself.

**Choices:**
- Go to the payments office and ask for the confirmation in writing → **payment_office**
  - NOTE (shown after choosing): In writing is doing all the work in that sentence, as it has since October.

## [payment_office] The Payments Office
*Day 65 — Wednesday, March 18, 2026 — Wednesday, March 18, 2026 (dayOffset 65)*

The payments office is a window, a clerk, and a screen she turns — after a moment's hesitation you will remember kindly — far enough for you to see the approval's status line. It says what the chronology said, in the system's own present tense: awaiting signature.

The clerk can confirm it verbally, which helps no file anywhere. Or she can print the status page — dated today, with the packet's received date and its awaiting-signature status on it — if you ask for the printout by name.

**Choices:**
- Ask for the printed status page, dated, with the received date on it → **review_notice**  _(cash −4; FLAG: unsignedConfirmed; HIDDEN + Payments status printout — packet received in the week the children arrived; status: awaiting signature)_
  - NOTE (shown after choosing): One printed page. The blank line, confirmed by the office that owns the line, on the day you asked.
- Take the verbal confirmation — she was clear, and the bus is coming → **review_notice**
  - NOTE (shown after choosing): Clear, kind, and unusable in a hearing room: a confirmation that exists only in your log, in your handwriting, again.

## [review_notice] The Review Notice
*Day 67 — Friday, March 20, 2026 — Friday, March 20, 2026 (dayOffset 67)*

The review notice arrives with the hearing's date and its paperwork: the agency's pre-review summary, in which the five words have grown a sentence. The summary now reports that the caregiver's financial strain raises a question about placement stability, and that the review will consider what supports the placement may need.

Read cold, it is a reasonable paragraph. Read with your chronology open beside it, it is a paragraph about a flood that never mentions the pipe. Both readings will be available in the courtroom. Only one of them will be in the file unless the chronology is filed before the hearing — Ms. Hart's step three, and the last errand on her list.

The hearing itself is a permanency hearing, held within six months of the children's placement (42 Pa.C.S. § 6351(e)(3)(i)). Six months is a clock too. This one, for once, is on your side: the review comes while the paper is still warm.

**Choices:**
- Decide, with Ms. Hart, whether the chronology goes in ahead of the hearing → **paper_filed**
  - NOTE (shown after choosing): Filed ahead, it is read in advance. Carried in, it is an ambush — and ambushes, even truthful ones, read worse than pages.

## [paper_filed] Filed Ahead, or Carried In
*Day 69 — Sunday, March 22, 2026 — Sunday, March 22, 2026 (dayOffset 69)*

Filing ahead costs copies, a trip, and the small social price of being the grandmother who files things. It buys the only thing that has ever mattered in this case: readers who have seen the cause before they weigh the strain.

Carrying it in costs nothing today. It also means the judge meets eleven dates for the first time in a twenty-minute hearing, while the summary's sentence — the one that has been in the file for weeks — sits already read, already underlined, already halfway to being a finding.

**Choices:**
- File the chronology and exhibits with the agency and the court, in writing, before the review → **review_prep**  _(cash −6; FLAG: paperOnRecord; HIDDEN + Chronology and exhibits filed in writing with agency and court before the permanency review)_
  - NOTE (shown after choosing): Stamped, copied, logged. The review will now be the second reading of your page, not the first.
- Carry the folder to the hearing — let the judge see it fresh → **review_prep**
  - NOTE (shown after choosing): Fresh is a quality of salads. In hearing rooms, the word for it is untested.

## [review_prep] Preparing Without Rehearsing
*Day 71 — Tuesday, March 24, 2026 — Tuesday, March 24, 2026 (dayOffset 71)*

Preparation, in Ms. Hart's office, is mostly subtraction: the chronology, the exhibits, Dena's progress report, your log. What Bernice will say, if asked, fits in three sentences, and she writes them on an index card in the handwriting that has labeled a thousand lunch trays: the children came in October. The packet went in that week. The money trouble is the packet's shadow, and the packet is in the file.

“Do not perform,” Ms. Hart says. “Grandmothers who perform get weighed as performances. Hand up paper and answer questions. The paper is better at this than any of us.”

Dena, on the phone that night, asks if she should come. She is a party; of course she comes. “Then we both go,” you say, “and we let the dates talk.”

**Choices:**
- Put the index card in the folder, and go home to the children's week → **household_week**
  - NOTE (shown after choosing): Three sentences on a card. Eleven dates on a page. A winter on both.

## [household_week] The Week the Case Waits
*Day 73 — Thursday, March 26, 2026 — Thursday, March 26, 2026 (dayOffset 73)*

The week before the review is, defiantly, ordinary: Joaquin loses a tooth and negotiates its price like a union man; Mireya insists on pouring her own milk and mostly succeeds; Dena's Sunday visit runs long because nobody watches the clock when the story Mireya is telling reaches its third act.

This is the placement whose stability a summary is about to question: two children, in their grandmother's house, in a routine so settled it has its own weather. The routine cost money to build. It is now being read, in an office across town, as evidence that the builder is a risk.

You log the week anyway — tooth, milk, story — because the log's job was never only the money. It is the house, in dates.

**Choices:**
- Log the week, and lay out the children's clothes for the hearing morning → **bedtime_beat112**
  - NOTE (shown after choosing): Hearing mornings start the night before, in houses that run on preparation.

## [bedtime_beat112] What Mireya Asks at Bedtime
*Day 75 — Saturday, March 28, 2026 — Saturday, March 28, 2026 (dayOffset 75)*

Mireya, at bedtime, asks the question underneath the whole case, in the grammar of four: “Are we staying at your house a long time?”

You give her the truth at her size: you are staying, the grown-ups are doing their paperwork, and her job is sleep. She accepts this with the completeness children accept things, and is asleep inside the story's first page.

Joaquin, eight and therefore a lawyer, asks from the doorway what happens at the review. “A judge reads the papers,” you say, “and decides if the papers tell the truth.” He considers this. “Do ours?” “Ours are dates,” you say. “Dates are the truest papers there are.”

**Choices:**
- Turn out the light, and check the folder one last time → **strain_deepens**
  - NOTE (shown after choosing): Folder, card, copies. The house sleeps. The file, across town, does not — files never do.

## [strain_deepens] The Form Learns a Word
*Day 77 — Monday, March 30, 2026 — Monday, March 30, 2026 (dayOffset 77)*

Two days before the review, Dena brings word of the pre-review paperwork's other half: a scored assessment form has been updated for the review, and among the things it rates — from the visits, the notes, and the summary — is placement stability, and the rating has absorbed the summary's sentence the way forms absorb everything: without its cause attached.

You cannot see the form's working. That is not this story's complaint; it is this story's weather. What you can do — the only thing anyone in your chair has ever been able to do — is make sure the room where the rating is weighed also holds the documents the rating never met.

Ms. Hart, on the phone, is calm in the specific way of people holding stamped copies: “Forms rate what they can see. Reviews decide what counts. Ours is filed. Let it count.”

**Choices:**
- Ask whether the new worker has seen the filed chronology → **worker_ack**  _(HIDDEN + Scored assessment form updated for the review — placement-stability rating drawn from the summary, cause not attached)_
  - NOTE (shown after choosing): A form's rating and a file's cause are about to be introduced, in a room with a judge in it.

## [worker_ack] The New Worker's Second Reading
*Day 79 — Wednesday, April 1, 2026 — Wednesday, April 1, 2026 (dayOffset 79)*

Mr. Osei calls the evening before the review, and his voice has the particular care of a man who has read a file twice. The chronology reached him. He checked the approval's status himself, he says — the words awaiting signature are, as of this week, no longer a secret the building was keeping from itself.

He does not promise an outcome; workers who promise outcomes are writing checks the system cashes selectively. He says the smaller, truer thing: “The summary was written before the packet's history was in front of us. The review will have both.”

Both. For five months the case had a strain with no cause in it. Tonight, on the eve of the room that decides, it has both halves of its own story in the same file.

**Choices:**
- Thank him, log the call, and sleep as well as hearing eves allow → **review_eve**
  - NOTE (shown after choosing): Logged: call, date, words. Some habits outlast the cases that taught them.

## [review_eve] The Night Before the Review
*Day 81 — Friday, April 3, 2026 — Friday, April 3, 2026 (dayOffset 81)*

The folder is by the door. The index card is in the folder. Dena will meet you at the courthouse steps, a party arriving for her children's hearing with her mother beside her — which is, whatever the file calls it, the family's actual structure, arriving in person.

You think about the winter in its true units: not months of process, but a stamped copy kept, a log kept, a daughter asked, a chronology assembled, a page filed. None of it was dramatic. All of it is about to be weighed in a room that weighs nothing else.

Across town, the summary's sentence sits in the file too, waiting for the same room. Sentences, like grandmothers, are patient. Tomorrow they meet a calendar.

**Choices:**
- Take the folder, take Dena's arm at the steps, and go in → **morning_review**
  - NOTE (shown after choosing): Two generations of the same family, one folder. The courthouse has seen worse delegations.

## [morning_review] Courthouse Steps
*Day 83 — Sunday, April 5, 2026 — Sunday, April 5, 2026 (dayOffset 83)*

The courthouse morning runs on its rails: the metal detector, the list on the wall, the conference-room wait in which every family in the corridor is holding a version of the same folder. Dena's hands are steady. Yours are steady. Steadiness, in this building, is a form of testimony.

Ms. Hart goes through the exhibits once, in order, the way she will hand them up: stamped copy, chronology page, signature page, status printout, log, bank book. “Dates first,” she says. “Feelings in the hallway, where they belong and where I will have plenty of my own afterward.”

The clerk calls the case. The children's case. The room, as ever, is smaller than what happens in it.

**Choices:**
- Go in, and let the hearing be a hearing → **review_hearing**
  - NOTE (shown after choosing): Twenty minutes, a judge, and two versions of one winter: a sentence, and a calendar.

## [review_hearing] The Review
*Day 85 — Tuesday, April 7, 2026 — Tuesday, April 7, 2026 (dayOffset 85)*

The judge opens the way the statute opens: this is a permanency hearing, and the court will determine the continuing necessity of the placement, compliance with the plan, the progress made, and whether reasonable efforts were made to finalize the plan (42 Pa.C.S. § 6351(f)(1), (2), (3), (5.1)) — and it will determine them from the evidence.

The agency's summary is read first: the placement is going well; the children are settled; the caregiver is experiencing financial strain, raising a stability question. The sentence lands in the room exactly as written — true words, missing their cause, halfway to a finding.

Then Ms. Hart rises, and what happens next depends — with a precision this story has been honest about since October — on what your winter actually put in her hands.

**Choices:**
- Put the full paper on the record — the stamped copy, the eleven dates, the blank signature line → **end_win**  _(REQUIRES: recordsRequested, chronologyBuilt, paperOnRecord)_
  - NOTE (shown after choosing): Exhibit by exhibit: received, routed, unsigned, unpaid — and a household ledger that matches the silence, month for month.
- Accept the agency's hallway offer — payments started this week, the stability sentence left for another day → **end_middle**
  - NOTE (shown after choosing): Money now; language later. It is a real offer, and its price is written in the part of the file that travels.
- Answer the stability question out loud — the winter, told by the woman who lived it → **end_strain**  _(REQUIRES-NOT: paperOnRecord)_
  - NOTE (shown after choosing): Every word of it is true. The summary is printed, filed, and already read; your voice is in the room for twenty minutes and in the transcript forever — at a summary's length, in a summary's words.

## [end_win] Ending — Payments Begin, and the File Tells the Truth (PARTIAL)
*Day 88 — Friday, April 10, 2026 — Friday, April 10, 2026 (dayOffset 88)*

The review does the thing reviews do when a cause arrives as exhibits: it re-describes the winter. The chronology is walked line by line — the packet's received date confirmed from the agency's own chronology, the routing stamp, the blank signature line, the status printout reading awaiting signature five months after the children arrived. The judge asks the agency one question — when the signature will happen — and accepts, on the record, the answer the building owed you in November: this week.

The order that follows keeps the placement exactly where it is, and writes the winter correctly while it does it: the caregiver's financial strain is attributed, in the findings, to the delayed approval — an agency processing lag — and not to the caregiver. Payments are directed to begin, with the approval completed on the record's own dates. The stability question, as a question about Bernice, is withdrawn by the only mechanism that ever withdraws such questions: better paper, in the same file, read by the person who decides.

You walk out with Dena's arm in yours and a folder that weighs the same as it did this morning. What it means has changed entirely.

**Ending.**

**Debrief:**
- WHAT THE FILE HELD (the hidden record, revealed): Two columns that finally met. Their column: a packet received Friday, October 24, 2025, routed the following week, and then a blank signature line and an awaiting-signature status for five months — the agency's own chronology and its own payments printout, obtained because Dena, a party, requested the record that “shall be released upon request” (55 Pa. Code § 3130.44(d)). Your column: the stamped copy that proved October, the call log, the bank book whose descent matched the silence month for month, and a one-page chronology of eleven checkable dates, filed with the agency and the court before the hearing. At the hearing the court made its determinations from evidence (42 Pa.C.S. § 6351(f)(1), (2), (3), (5.1)) — and the evidence had a cause in it.
- LABEL THIS WIN HONESTLY — IT IS PARTIAL: Payments begin, the record attributes the gap to the lag and not to the caregiver, and the placement is steadied on a truthful file. The drained savings are not restored by this ending or any ending in this scenario: the decade of overtime that the empty months spent stays spent, and no order in this story writes it back. What the win returns is the future — a placement read correctly from here, and payments that now arrive in the present tense. Anyone who calls that whole is selling something. It is enough, and it is not everything, and both halves of that sentence are the lesson.
- WHAT NO STRATEGY CONTROLS: A different judge could have noted the chronology and pressed the stability question anyway; a payments office that lost the printout, a worker who never re-read the file, a daughter too deep in her own crisis to sign a page — any of them thins this ending without Bernice changing a thing. Workers, judges, clerks, and luck held pieces of it. What her choices controlled was narrower and durable: when the system finally weighed her winter, it weighed a calendar she had kept since October, instead of a sentence it had written about her in her absence.

## [end_middle] Ending — Paid, With the Note Still Standing
*Day 88 — Friday, April 10, 2026 — Friday, April 10, 2026 (dayOffset 88)*

The hallway offer is real, and you take it with open eyes: the approval is completed that week — the signature, it turns out, was always a week's work — and the first payment arrives before the month turns. Groceries stop being arithmetic. The house exhales.

Inside the courtroom, the review is brief and kind. The placement continues. And the summary's sentence — caregiver experiencing financial strain, stability question noted — is adopted into the review's paperwork without its cause ever being put beside it, because the chronology that carries the cause was never the price of the hallway deal. The strain is over. Its description remains, filed, quotable, and available to every future reader of this case.

You have won the money and lost the sentence. Both facts will travel with the file. Only one of them was ever going to pay for shoes.

**Ending.**

**Debrief:**
- WHAT THE FILE HELD (the hidden record, revealed): The same two columns as every path — the agency's blank signature line and your descending bank book — but assembled, if at all, only as a private folder, never as the review's evidence. The payments were fixed in a hallway, administratively, the moment the building was embarrassed into a signature. The record of why they were late was nobody's exhibit. So the file keeps both truths in their unbalanced forms: payments, current; strain, unexplained — a caregiver whose file says she struggled financially in the winter her grandchildren arrived, with the reason living in her kitchen-table folder instead of in the case.
- THE PROCESS UNDER THIS PATH: The right that would have corrected the sentence was the verified one — the case record, released on a party's written request (55 Pa. Code § 3130.44(d)), signed by Dena because the right belongs to the case's subjects, not to a placement applicant — and the review that would have weighed the correction decides its questions from evidence put before it (42 Pa.C.S. § 6351(f)). A hallway can start payments. Only a record can re-describe a winter, and this winter's re-description was traded away, knowingly, for speed. The trade is understandable. Trades still cost what they cost.
- THE HONEST PART: This ending is not a failure, and this debrief will not pretend the money is a small thing — it is rent, food, and a grandmother sleeping without arithmetic. It is a partial ending with the partiality located precisely: the future is paid for and the past is misdescribed, and the misdescription is the part with a forwarding address. A later review, a different worker, a new summary quoting the old one — the note will be read again by people who were not in the hallway. Whether it is ever corrected will depend on paper that, as of tonight, still lives only in a folder on a kitchen table — where, to Bernice's credit and this system's instruction, it at least still exists.

## [end_strain] Ending — Strain, Entered as Instability
*Day 88 — Friday, April 10, 2026 — Friday, April 10, 2026 (dayOffset 88)*

You tell the winter beautifully. You tell it in order, with the dates you know by heart, and the room listens the way rooms listen to grandmothers: with respect, and with a printed summary open in front of them.

The order, when it comes, is not cruel. The placement continues — the children are settled, everyone agrees — and the court, weighing the only paper it was given about the money, does what paper invites: it notes the caregiver's financial strain as a placement-stability concern, directs supportive services aimed at the caregiver's budgeting and household management, and sets the next review to examine whether the strain has resolved.

Services, arriving at last — aimed, with perfect administrative logic, at the one diagnosis the file contained. The packet, unsigned on a desk across town, is not mentioned in the order. It is not mentioned anywhere. That is what unmentioned things do: they continue.

**Ending.**

**Debrief:**
- WHAT THE FILE HELD (the hidden record, revealed): A summary's sentence, adopted: strain, entered as instability, with services ordered around the wrong diagnosis — budgeting help for a woman whose budget was raided by a missing signature. Your account of the lag was spoken at the review and is preserved the way spoken accounts are: summarized, briefly, in someone else's words. The chronology that would have proven it — the agency's own approval lines ending at a blank signature line, obtainable on a party's written request under 55 Pa. Code § 3130.44(d) — was never requested, or never assembled, or never filed, and a court making its determinations from evidence (42 Pa.C.S. § 6351(f)(1), (2), (3), (5.1)) cannot weigh a cause it was never handed.
- THE PROCESS UNDER THIS PATH: Nothing in this ending required bad faith from anyone in the room. The summary said strain; no exhibit said lag; the order therefore treated strain. That is the mechanism this scenario exists to teach: in a permanency review, the file's description of a problem becomes the court's prescription for it, and descriptions are only ever corrected by other documents — filed, dated, and in the record before the hearing weighs them. An oral history, however true, enters the record as the note-taker's summary of it, and summaries are how this winter got misdescribed in the first place.
- THE HONEST PART: Be fair to the woman in this ending, because the file was not: she fed two children for five months out of her own old age, kept every copy, and told the truth in the room. The system's failure to sign a packet became, on paper, her instability — and the services now ordered will consume her afternoons teaching her to manage money she managed correctly all along. A kinder judge might have asked the agency for its approval chronology unprompted; some do. This one weighed what was filed. The folder on the kitchen table still holds the correction. Folders, unlike hearings, do not expire — but they do wait, and waiting is what the empty months were made of.

## [end_disrupt] Ending — Notice Given: The Placement Disrupts
*Day 38 — Thursday, February 19, 2026 — Thursday, February 19, 2026 (dayOffset 38)*

The contingency becomes the plan, in the brisk language of placement meetings: the children will move to a foster home at the end of the month, as a temporary measure, everyone says, until the caregiver's circumstances stabilize. Temporary is a word this system uses the way families use soon — sincerely, and without a date attached.

Joaquin packs his school bag and a second bag, and asks whether the new house will know that Mireya cannot sleep without the story. You write it on a card for the new caregiver, in your clearest hand: the story, the milk, the tooth money rates. It is the last document you file in this case, and like all your documents, it is exact.

The approval packet, the record will eventually show, was signed some weeks after the children moved — in process, completed at last, in an empty house's file. Nobody in this ending acted from cruelty. A signature was late, a savings account was finite, and two children paid the exchange rate between those two facts.

**Ending.**

**Debrief:**
- WHAT THE FILE HELD (the hidden record, revealed): A grandmother who did everything in ink — packet submitted Friday, October 24, 2025, stamped copy kept, calls logged — and an agency chronology nobody in this path ever requested, in which the packet she submitted sat unsigned from the week the children arrived. The notice Bernice sent was true when she sent it: the money was gone because the payments had never come, and the payments had never come because of a blank line in a building she had never entered. The disruption is recorded in the file as a caregiver's inability to continue. Its cause is recorded nowhere, because the document that would record it was never asked for.
- THE PROCESS UNDER THIS PATH: The instrument that changes this ending is the verified one, and it was never Bernice's to sign: the case record “shall be released upon request” (55 Pa. Code § 3130.44(d)), and the right belongs to the case's subjects — Dena, a party, signing at her mother's asking, as the kinship scenario in this series teaches it. With the chronology in hand, the review's determinations (42 Pa.C.S. § 6351(f)) would have had a cause to weigh. Without it, the file weighed the only thing it held: a finite bank account. Notice, in this system, is also a document — and a true notice, sent without the chronology behind it, reads to every later reader as a capacity finding instead of a billing record.
- THE HONEST PART: This ending must not be read as a grandmother failing two children. It is a placement ended by arithmetic that an unsigned packet imposed on a fixed income — the documented administrative-lag pattern this scenario is built from, run to its end. A worker who escalated the signature, a supervisor who audited awaiting-signature packets, a daughter positioned to sign a request in November instead of February: other people's paper held pieces of this too, and any one of them changes it. What Bernice controlled — the copies, the log, the truth told at kitchen-table size — she did, from the first week, in ink. The system's blank line outlasted her savings anyway. That sentence is the indictment this scenario files, and it is filed against a line, not a woman.
