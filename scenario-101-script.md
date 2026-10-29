# THE FIRST 90 DAYS — Scenario 101: “One Crib, Two Files”

*Human-readable script. This document and `scenario-101.json` are generated from a single source and match node-for-node: same IDs, same order, same choices, same effects.*

**The family is fictional — a composite. No real person's story appears here.**

**Content note:** This scenario depicts a teenage mother who is herself in foster care: two case files, a birth, placement decisions, and two reviews. There is no graphic content. Players may skip any scene or use the quick exit at any time.

**How to read effects:** `cash −40` changes the player's cash. `FLAG: name` sets a flag the engine tracks. `HIDDEN + item` means the case file quietly records that item at this choice — the player does not see it when it happens. `REQUIRES FLAG: name` means the choice is only available if that flag was set earlier; `REQUIRES NO FLAG: name` means it is only available if that flag was never set. `NOTE:` is text shown to the player right after choosing.

Start date: Monday, September 8, 2025. Day offsets are days since the scenario's start date.

## [start] A Daughter, in Two Senses
*Day 0 — Monday, September 8, 2025 (dayOffset 0)*

Your name is Desiree Vane. You are seventeen, and you live in foster care at Pauline's house — a brick twin with a school calendar on the refrigerator and your own key, which Pauline had cut for you in June and which still feels heavier than a key should.

This morning, in a hospital room that smells of soap and warm plastic, you gave birth to a daughter. You named her Sable. She is asleep in the clear bassinet beside the bed, one fist outside the blanket, entirely unaware that paperwork has already begun moving in a building she has never seen.

You are, starting today, a person in two files at once. In one file you are the child. In the other, you are the mother. Nobody has yet said whether those two files will ever be in the same room.

**Choices:**
- Ask the nurse who will decide where Sable goes when she leaves the hospital → **hospital_papers**
  - NOTE (shown after choosing): The nurse does not decide. She points, kindly, to the folder that arrived while you were in labor.

## [hospital_papers] The Folder That Arrived During Labor
*Day 1 — Tuesday, September 9, 2025 (dayOffset 1)*

The folder holds two discharge plans, printed separately. Yours returns you to Pauline's house, where your room, your schoolbooks, and your own case plan are. Sable's names a different foster home across town — a home approved for infants, the paper says, as if that settled the question.

No paper in the folder asks the joint question: is there a placement that takes both of you? Mr. Salas, the caseworker on your own case, works from your file. Ms. Kittredge, the caseworker assigned to Sable, works from hers. Each plan, read alone, looks reasonable. Read together, they separate a mother and a newborn by default, not by any finding about either of you.

A hospital social worker says Sable will be placed tomorrow while assessments are sorted out, and that a hearing will follow quickly — the law requires an informal shelter care hearing not later than 72 hours after a child is placed in shelter care. (42 Pa.C.S. § 6332; 23 Pa.C.S. § 6315(d))

**Choices:**
- Read both discharge plans side by side before signing either one → **two_files**
  - NOTE (shown after choosing): Side by side, the gap is visible: neither plan mentions the other person in this room.
- Sign yours so you can get back to Pauline's and sort out Sable's later → **two_files**
  - NOTE (shown after choosing): Your signature moves one file forward. Sable's file moves on its own track, at its own speed.

## [two_files] Two Desks
*Day 2 — Wednesday, September 10, 2025 (dayOffset 2)*

By phone, the two files describe themselves. Mr. Salas talks about your case: school attendance, your postpartum appointments, the permanency plan written for you before Sable existed — a plan whose pages do not contain her name. Ms. Kittredge talks about Sable's case: feeding, pediatric follow-up, a placement that can take an infant this week.

Both workers are courteous. Both answer the questions their own file asks. The question neither file asks — where can this mother and this baby live together? — has no desk to land on. That is not cruelty. It is structure, and structure is what you will have to write your way through.

Tomorrow's hearing is for Sable's placement. You will be there as her mother. You are also, in another courtroom on another day, the child whose own review is coming.

**Choices:**
- Call Ms. Radcliffe, your attorney, before the hearing and tell her about both files → **shelter_care**
  - NOTE (shown after choosing): She goes quiet for a moment. "Then we bring both files into the room," she says. "In writing."
- Plan to explain it all out loud at the hearing tomorrow → **shelter_care**
  - NOTE (shown after choosing): Out loud is where you are strongest. It is also, Ms. Kittredge's voicemail reminds you, a room where only some things get written down.

## [shelter_care] Shelter Care: Sable's Hearing
*Day 3 — Thursday, September 11, 2025 (dayOffset 3)*

The shelter care hearing happens on the third day, inside the 72-hour window the law sets. (42 Pa.C.S. § 6332; 23 Pa.C.S. § 6315(d)) Before it begins, you are told you have the right to counsel in Sable's case, and to appointed counsel if you cannot afford one. (42 Pa.C.S. § 6337; § 6332(a)) Ms. Radcliffe sits beside you.

The agency's position is paperwork, not accusation: Sable needs an infant-approved placement now; Pauline's home is approved for you, not for a baby as a separate placement; therefore, separate homes, with visits. No one testifies that you cannot care for Sable. No one needs to. The forms have already divided you.

The court continues Sable's temporary placement for now and sets review dates. What matters, Ms. Radcliffe whispers, is what gets asked for — in writing, in both cases — before those reviews.

**Choices:**
- Ask Ms. Radcliffe to state on the record that you are requesting a joint placement → **paulines_kitchen**  _(FLAG: jointOnRecord ; HIDDEN + Shelter care record — mother requested a joint placement on the record)_
  - NOTE (shown after choosing): The court reporter types it. A request spoken in this room exists in a way a hallway request does not.
- Let the hearing end — the judge seemed to understand the situation → **paulines_kitchen**
  - NOTE (shown after choosing): Understanding, unrecorded, travels poorly. The order that leaves this room mentions two placements and no request.

## [paulines_kitchen] Pauline's Kitchen Table
*Day 5 — Saturday, September 13, 2025 (dayOffset 5)*

Pauline makes tea she does not drink and says the practical things out loud: her home is approved for you; she does not know if it can be approved for you-and-a-baby, and nobody has asked that question in a form she can answer. She will keep your room exactly as it is. She will drive you to visits. She cannot, by wanting to, amend a placement approval.

On the refrigerator, under your school calendar, she pins Sable's hospital bracelet copy next to a photograph of the bassinet. "So this house remembers," she says, "even if the files don't."

Your own plan compliance — school, appointments, the check-ins Mr. Salas tracks — is suddenly not just your case. It is also, though no form says so, the evidence in Sable's.

**Choices:**
- Ask Pauline to write down what she told you — her willingness, her approval limits, the rides she can give → **radcliffe_office**  _(FLAG: fosterHomeStatement ; HIDDEN + Foster home — Pauline's willingness and approval limits stated in writing)_
  - NOTE (shown after choosing): She writes it in her careful hand and signs it. Paper from the home itself, not a summary of the home.
- Keep it as a conversation — Pauline's support is obvious to anyone who meets her → **radcliffe_office**
  - NOTE (shown after choosing): It is obvious in her kitchen. Hearings do not happen in her kitchen.

## [radcliffe_office] Ms. Radcliffe Draws Two Files
*Day 7 — Monday, September 15, 2025 (dayOffset 7)*

Ms. Radcliffe draws two rectangles on a legal pad and labels them YOURS and SABLE'S. Then she draws an arrow in each direction and labels both arrows with the same word: WRITING.

"A joint placement will not happen because it is sensible," she says. "It will happen, if it happens, because someone with the power to search for one was asked, in writing, in both cases, so neither file can honestly say the question never arrived. We also document your own plan — school, appointments — as if Sable's judge will read it. Because we are going to make sure she can."

She drafts a one-page request: placement together in a home approved for a mother and infant, or assessment of a home that could be; the request to be filed in your case and in Sable's case, with copies to Mr. Salas and Ms. Kittredge.

**Choices:**
- Sign the joint request and file it in BOTH cases, to both caseworkers → **joint_filed**  _(FLAG: jointRequestBoth ; HIDDEN + Joint placement — written request filed in both the mother's own case and the infant's case)_
  - NOTE (shown after choosing): Two copies, two files, two receipts. The joint question now has a desk. Two desks.
- Send it only in Sable's case — that is the baby's file, and yours feels separate → **joint_one_file**
  - NOTE (shown after choosing): Ms. Radcliffe does not argue. She writes 'filed — infant's case only' on her pad and underlines 'only' once.

## [joint_filed] Filed Twice
*Day 8 — Tuesday, September 16, 2025 (dayOffset 8)*

The receipts come back stamped, days apart, in two different envelopes. Mr. Salas calls: your file now carries the request, and your next review will have to reckon with it. Ms. Kittredge calls separately: Sable's file carries it too, and a search for a home that takes a mother and baby together — which exists, she says, though there are not many — can be documented as requested.

Nothing has been granted. Everything has changed shape: separation is no longer the default no one chose. It is now a position someone would have to defend against a written alternative.

**Choices:**
- Turn to your own case — the school term has started without asking permission → **school_term**

## [joint_one_file] Filed Once
*Day 8 — Tuesday, September 16, 2025 (dayOffset 8)*

Sable's file carries the request. Yours does not. At your next check-in, Mr. Salas is surprised — genuinely — to hear a joint search described as urgent; in his file, your plan still reads as it did before Sable: school, appointments, permanency for one person.

Ms. Radcliffe shrugs with her eyes. "One file knows," she says. "Cases are decided by the file in the room. We may get another chance to file it in yours. We may spend that chance explaining why it wasn't there."

**Choices:**
- Turn to your own case — the school term has started without asking permission → **school_term**

## [school_term] School, With a Newborn Elsewhere
*Day 11 — Friday, September 19, 2025 (dayOffset 11)*

Your plan, in your own case, is concrete: return to school on the phased schedule your counselor set, keep postpartum and pediatric-adjacent appointments, check in with Mr. Salas weekly. It was written for a student. It is now being lived by a student who is also visiting a newborn across town on agency time.

The scored assessment form in your file — a form you cannot see — is being updated from what the system can observe: attendance as recorded by the school, appointments as confirmed by offices, visits as logged at the agency. What it cannot observe, it leaves blank, and blank, on a form, rarely reads as neutral.

Keeping your own plan is not a distraction from Sable's case. On paper, it is half of it.

**Choices:**
- Keep a one-page log — school days, appointments, visit dates — and give a copy to Mr. Salas and Ms. Radcliffe → **plan_documented**  _(cash −10 ; FLAG: planDocumented ; HIDDEN + Mother's own plan — school and appointment compliance documented on one page and shared)_
  - NOTE (shown after choosing): Bus fare and copies: $10. The log is boring, dated, and exactly the shape evidence takes.
- Rely on the school and the offices to report it — that is their job → **plan_undocumented**
  - NOTE (shown after choosing): It is their job. Their reports go to one file, late, or to an inbox that changed hands in September.

## [plan_documented] The Log Goes in the Folder
*Day 13 — Sunday, September 21, 2025 (dayOffset 13)*

Mr. Salas attaches the log to your file without comment, which from Mr. Salas is approval. The school confirms attendance directly. Your postpartum check is stamped attended. When Ms. Kittredge, in Sable's case, asks how your own plan is going, there is now an answer that does not depend on anyone's memory of a phone call.

Desiree the child, on paper, is doing what her plan asks. That sentence is about to become the most useful sentence in Sable's file — if it can get there.

**Choices:**
- Go to the visit — Sable is three weeks old and already outgrowing the hospital blanket → **visits_two_addresses**

## [plan_undocumented] Attendance, Somewhere in a System
*Day 13 — Sunday, September 21, 2025 (dayOffset 13)*

The school's portal shows your attendance. The clinic's system shows your appointment. Neither system talks to a case file on its own, and a handoff in Mr. Salas's office — a covering worker for two weeks — means your October check-ins are summarized from memory in November as 'generally compliant, details unclear.'

'Generally' and 'unclear,' Ms. Radcliffe says, reading it, 'are the two most expensive words in your file.' The facts were fine. The record of the facts is what a hearing will meet.

**Choices:**
- Go to the visit — Sable is three weeks old and already outgrowing the hospital blanket → **visits_two_addresses**

## [visits_two_addresses] Visits Between Two Addresses
*Day 16 — Wednesday, September 24, 2025 (dayOffset 16)*

Visits happen at the agency office, on the agency's schedule, with Sable brought from the other home and you brought from Pauline's — two addresses, two drivers, one room, a clock. You feed her, you learn the particular way she settles against your shoulder, a staff member notes what the visit form asks it to note.

The visit form, Ms. Radcliffe says, is another scored surface: feeding as observed, settling as observed, the plan for the next visit as understood by the worker. What the form has no box for is the distance — that 'home,' for the two of you, is currently a room you are both delivered to.

After the visit, she tells you about the record — the whole agency record, in both cases — and the right to request it.

**Choices:**
- Listen carefully — she says this request is the one that changes what you can see → **records_beat**
  - NOTE (shown after choosing): "You cannot answer a form you have never seen," she says. "So we go and see it."

## [records_beat] The Request, in Both Files
*Day 19 — Saturday, September 27, 2025 (dayOffset 19)*

Under the agency's own regulation, records in the agency file are to be released on request. (55 Pa. Code § 3130.44(d)) Ms. Radcliffe drafts two short requests — one for Sable's record, as her mother; one for your own record, as the young person in care — each dated, each in writing, each filed where its file lives.

Requesting them costs postage, copies, and the bus across town to deliver the second one by hand. Not requesting them costs nothing today. The form goes on being scored either way; the only question is whether you ever get to read what it says while there is still time to answer it.

**Choices:**
- File written record requests in BOTH cases — Sable's record and your own → **records_arrive**  _(cash −15 ; FLAG: recordsRequested ; FLAG: ownRecordRequested ; HIDDEN + Records — agency records requested in writing in both cases under the release-on-request rule)_
  - NOTE (shown after choosing): Two requests, two receipts. This is the highest-leverage paper in either file so far.
- Ask Ms. Kittredge informally what is in Sable's file when you next speak → **records_partial**
  - NOTE (shown after choosing): She will tell you some of it, from memory, kindly. Memory is not a record you can hand to a judge.

## [records_arrive] What the Packets Show
*Day 23 — Wednesday, October 1, 2025 (dayOffset 23)*

The packets arrive redacted and partial, and still they redraw the case. In Sable's record: your joint request, stamped; the visit notes, warm and brief; and a scored assessment form summary whose context lines say 'mother's support system — unclear' and 'mother's own placement stability — not assessed.' Not assessed — because that fact lives in your file, which this form never opened.

In your own record: the one-page log (if you kept it), Pauline's statement (if she wrote it), and your plan's permanency language, still written for one person. Neither file is wrong, exactly. Each is incomplete in precisely the shape of the other.

Ms. Radcliffe puts the two packets side by side — the way you once put two discharge plans side by side. 'Now,' she says, 'we know what to correct, and we correct it in writing, in both places.'

**Choices:**
- Write the correction — one page, filed in both cases, naming the support system and asking both plans to name each other → **correction_filed**  _(FLAG: correctionFiled ; HIDDEN + Records — one-page correction filed in both cases; each plan asked to name the other)_
  - NOTE (shown after choosing): Pauline, the log, the joint request — cited by date, not described from memory.
- Save the correction for the hearing — it will sound stronger spoken aloud → **correction_held**
  - NOTE (shown after choosing): Spoken corrections enter a room and leave with it. Filed corrections are still there when the room empties.

## [records_partial] What a Phone Call Shows
*Day 23 — Wednesday, October 1, 2025 (dayOffset 23)*

Ms. Kittredge, kindly, summarizes: visits are going well; the joint search is 'noted'; your own stability, in Sable's form, is 'unclear — mother's case held separately.' The word 'unclear' does the quiet work it always does.

You have no pages to correct, because you have no pages. A summary you heard cannot be quoted to a judge, attached to a plan, or answered line by line. Ms. Radcliffe writes, on her pad, 'no packet — working from summaries,' and the sentence looks like what it is: a narrower case.

**Choices:**
- Prepare for the reviews with what can still be put in writing → **mother_baby_search**

## [correction_filed] One Page, Two Files
*Day 27 — Sunday, October 5, 2025 (dayOffset 27)*

The correction goes in stamped, in both cases: Pauline named, her written statement dated; your school and appointment log attached; the joint request's filing dates cited; and a single requested sentence — that your permanency plan name Sable, and Sable's plan name your placement, so neither plan is ever again written as if the other person did not exist.

Mr. Salas calls it 'helpful context.' Ms. Kittredge calls it 'received and filed.' Bureaucratically, those are love letters. The scored form's context lines, at the next update, have something to be updated from.

**Choices:**
- Ask what homes actually take a mother and baby together — and who is searching → **mother_baby_search**

## [correction_held] Saved for a Room
*Day 27 — Sunday, October 5, 2025 (dayOffset 27)*

You rehearse the correction with Ms. Radcliffe until it is clear and short. It is a good two minutes of speaking. Its weakness is not in what it says; it is in where it will live — in a transcript, maybe, if the hearing reaches it, and nowhere in the plan documents the next worker will actually open.

Meanwhile the search for a joint home, such as it is, proceeds at the speed of a noted request.

**Choices:**
- Ask what homes actually take a mother and baby together — and who is searching → **mother_baby_search**

## [mother_baby_search] Homes That Take Both
*Day 31 — Thursday, October 9, 2025 (dayOffset 31)*

They exist. That is the first fact, and it is not a small one: there are placements approved for a young mother in care together with her infant — fewer than the separate homes, with waiting shaped by other families' needs, but real, named, and searchable when someone is directed to search.

The second fact is procedural: a search is documented when it is requested in writing with a response requested in writing. A search mentioned in a meeting is documented as a meeting. Pauline, for her part, says she will support visits and keep your room whichever home you land in — and says it, again, in writing, for whichever file needs it.

Your own review hearing is next week; Sable's review follows it. Two rooms, two judges' lists, one family — unless the paper makes it one.

**Choices:**
- Put the joint-search request and a dated progress report in writing for BOTH review hearings → **review_packet**  _(cash −10 ; FLAG: searchDocumented ; HIDDEN + Joint placement — search and dated progress report filed in writing for both reviews)_
  - NOTE (shown after choosing): Copies for two courtrooms: $10. The same packet, in both rooms, on purpose.
- Bring the request to your own review and mention Sable's review is coming up too → **review_packet**
  - NOTE (shown after choosing): Mentioned in one room, it binds one room. The other room will open a file that has never heard your voice.

## [review_packet] Your Review: Desiree as the Child
*Day 36 — Tuesday, October 14, 2025 (dayOffset 36)*

Your permanency review is a hearing about you: your placement, your progress, your plan. Reviews of this kind are where the court examines placement and the plan's steps on the record. (42 Pa.C.S. § 6351) Pauline testifies briefly — rides, school mornings, the room kept. Mr. Salas reports your compliance, from the file: as documented, or as summarized, depending on the paper you made.

Then Ms. Radcliffe does the thing this whole case has been building toward. She asks the court to note, in your order, the pending joint-placement request in Sable's case by name and date — so your file, in its own courtroom, stops being a plan for one person. The judge looks at the packet. The packet is either there, stamped and complete, or it is a description of a packet.

**Choices:**
- Let the packet speak — your request, your log, Pauline's statement, the correction, all filed → **baby_review**
  - NOTE (shown after choosing): The judge notes the request in the order. One sentence. Your file now names your daughter.

## [baby_review] Sable's Review: Desiree as the Mother
*Day 41 — Sunday, October 19, 2025 (dayOffset 41)*

Five days later, the second room. Sable's review opens a file in which you are not a child at all; you are 'the mother,' with a plan of your own to be measured against. Ms. Kittredge reports visits, feeding, the pediatric record — and the status of the joint search, as documented, or as noted, depending on the paper you made.

Ms. Radcliffe hands up the same packet — including, now, your own review's order naming this case. Two courtrooms have each been shown the other file. Whatever the decision is, it will be a decision made about one family, in full view of itself — which is precisely what the default paperwork, back in September, was structured never to do.

The court takes the placement question under advisement and sets the decision for next week.

**Choices:**
- Wait for the decision — together, in Pauline's kitchen, with both files finally naming each other → **decision**
  - NOTE (shown after choosing): Pauline pins the hearing notice on the refrigerator, next to the bracelet copy. The collection is becoming a record of its own.

## [decision] The Decision Is a Placement Question
*Day 47 — Saturday, October 25, 2025 (dayOffset 47)*

The decision, when it comes, will not be a verdict on whether you love your daughter — no one in either file has ever doubted it, and love was never the scored item. It will be a placement decision, made from paper: was a joint placement asked for in a way that required a search; is your own plan documented as kept; do the two plans name one family, or two strangers who share a hospital bracelet?

Ms. Radcliffe lays out the possibilities plainly, the way she has laid out everything: together in a home that takes both, with both cases still open; apart, with visits between two addresses and a search that stays 'noted'; or — the quietest outcome — your own plan rewritten around a future that no longer mentions Sable at all, a goal drift no single hearing announces.

Which of those the paper supports depends, now, entirely on the paper there is.

**Choices:**
- The joint request was filed in both cases, the correction names one family, and both reviews saw the same packet → **end_together**  _(REQUIRES FLAG: jointRequestBoth ; REQUIRES FLAG: recordsRequested ; REQUIRES FLAG: correctionFiled)_
  - NOTE (shown after choosing): Every gate on this route was a piece of writing filed earlier, in both places.
- The family stays apart for now, with visits and a search still pending on paper → **end_separate**
  - NOTE (shown after choosing): The addresses are different. The question, at least, is now on file in both of them.
- Your own plan is rewritten at review — school, independence, a future described without Sable in it → **end_drift**  _(REQUIRES NO FLAG: correctionFiled)_
  - NOTE (shown after choosing): No one votes for this outcome. It arrives the way defaults arrive: by nobody writing the alternative down.

## [end_together] One Crib, Two Files
*Day 52 — Thursday, October 30, 2025 (dayOffset 52)*

A home is found — a placement approved for a young mother in care together with her baby, two bus routes from Pauline's, whose door, she says in writing and in person, stays open to you both. The crib goes against the wall of a room that is, for the first time since September, one room: your schoolbooks on the desk, Sable asleep where you can hear her without a visit form.

Nothing is closed. You are still in care yourself; your case has its reviews, your plan, your own road to eighteen and beyond. Sable's case is still open; her reviews will come on their own calendar. Both files remain on two desks. But each file now names the other, the joint request and the correction sit stamped in both, and no future worker opening either one will meet a plan written for a person who does not exist.

On your first night there, you put the one-page log — school, appointments, visits that are no longer visits — into a folder and start a new page. At the top, in your careful handwriting: 'Home. Both of us.'

**Ending.**

**Debrief:**
- THE LAW, BEAT BY BEAT — Shelter care: Sable's placement was heard inside the 72-hour window the law requires for a child placed in shelter care (42 Pa.C.S. § 6332; 23 Pa.C.S. § 6315(d)), with your right to counsel stated on the record (42 Pa.C.S. § 6337; § 6332(a)). Reviews: both permanency reviews proceeded on the record the files contained (42 Pa.C.S. § 6351) — which is why the packet, filed for both, mattered in both rooms. Records: the turning point of this scenario is the written request in both cases under 55 Pa. Code § 3130.44(d) — records released on request — which exposed the scored assessment form's unscored context ('not assessed,' 'unclear') while there was still time to correct it in writing.
- THE HIDDEN FORM, MAPPED — The form in each file rated only what that file could observe: joint request filed in both cases (flag: jointRequestBoth), the mother's own plan compliance documented on one page (flag: planDocumented), Pauline's willingness stated in writing (flag: fosterHomeStatement), records requested in both cases (flags: recordsRequested, ownRecordRequested), the correction filed in both (flag: correctionFiled), and the joint search documented for both reviews (flag: searchDocumented). Every 'unclear' in the debrief above was a place where the other file held the fact and this file held a blank.
- HONEST LIMITS — This is a PARTIAL win, and the scenario labels it so: mother and baby are together, and both cases remain open, with their own clocks, reviews, and risks — including the ordinary risk that a placement disrupts or a plan changes. Real outcomes also turn on workers, judges, available mother-baby placements, and luck; a county with no joint placement open that month has no writing that conjures one. This ending is not a verdict on Desiree as a parent or as a young person in care. It is a map of what the written record made possible: two files that finally describe one family.

## [end_separate] Two Addresses, One Bracelet
*Day 52 — Thursday, October 30, 2025 (dayOffset 52)*

The decision keeps the placements separate for now. The joint search remains open on paper — requested, documented, unfilled — and visits continue between two addresses, on a schedule, in a room neither of you lives in. Sable knows your shoulder and your voice. She also knows a crib in another house, and a second set of hands.

It is not the ending the folder was built for, and it is not stasis, either: because the request and the correction are filed in both cases, every future review must reckon with a joint question that has a date and a stamp, not a mother's recollection that she once asked. Searches stall. Stamped questions, at review after review, are harder to stall forever.

Pauline keeps your room. The bracelet copy stays on the refrigerator. So, now, does the stamped copy of the joint request — Pauline's addition, in a plastic sleeve, 'so this house remembers what it asked for.'

**Ending.**

**Debrief:**
- THE LAW, BEAT BY BEAT — The shelter care hearing was timely (42 Pa.C.S. § 6332; 23 Pa.C.S. § 6315(d)) and counsel was present (42 Pa.C.S. § 6337). Reviews under 42 Pa.C.S. § 6351 can only act on the record before them; where the joint request reached only one file, or the record was never requested under 55 Pa. Code § 3130.44(d) in time to correct its 'unclear' context lines, the other courtroom decided a narrower case than the family was actually living.
- THE HIDDEN FORM, MAPPED — Compare what the winning route files in both places (jointRequestBoth, recordsRequested, correctionFiled, planDocumented) with what this route holds: a request in one file travels to one room; a plan lived but not logged reads as 'generally compliant, details unclear'; a correction saved for speaking lives in a transcript at best. The separation in this ending was not ordered because anyone found Desiree unfit — it continued because the joint alternative, in at least one file, was a note instead of a packet.
- HONEST LIMITS — Separate placement with visits is a real and common interim outcome, and families reunify from it; this debrief does not call it failure. Real outcomes also turn on workers, judges, the actual supply of joint placements, and luck. What the paper controls is narrower: whether 'together' is a documented, pending, reviewable request in both cases, or a hope carried between two addresses by the only person who lives in both files — a seventeen-year-old with a bus pass.

## [end_drift] The Plan Without Her Name
*Day 52 — Thursday, October 30, 2025 (dayOffset 52)*

No hearing announces it. At a review of your own case — a hearing about school, placement, your road to eighteen — the updated plan is handed up, tidy and approvable, and Sable is not in it. Not removed in anger; omitted by template. The objectives are all about one person, because the template was written for one person, and nothing filed in your case ever required it to describe two.

Sable's case continues on its own desk, with its own plan, in which you appear as a visiting mother with a schedule. The two files, which began as an accident of paperwork, finish the season as a description of two separate lives — because in the one place it had to be written to be real, it never was.

You keep visiting. You keep the bracelet copy Pauline gives you when you move rooms. What you no longer have is a plan — yours, official, stamped — in which your daughter exists. Rebuilding that sentence into a plan is possible, lawyers and advocates do it, but it is next season's work, and it starts from further back.

**Ending.**

**Debrief:**
- THE LAW, BEAT BY BEAT — Nothing in this ending required anyone to break a rule: shelter care was timely (42 Pa.C.S. § 6332; 23 Pa.C.S. § 6315(d)), counsel existed (42 Pa.C.S. § 6337), and reviews were held (42 Pa.C.S. § 6351). The drift happened inside lawful process, in the gap between two files — which is the scenario's whole point. The counter-moves were all in the verified set: a joint request filed in both cases, records requested in both under 55 Pa. Code § 3130.44(d) so the unscored context could be seen and answered, and a correction asking each plan to name the other family member.
- THE HIDDEN FORM, MAPPED — This ending is reached when the correction was never filed (no correctionFiled flag): your own file's form kept rating a one-person plan — school as recorded, appointments as summarized, 'mother's permanency objectives' never scored at all, because no item on either form asks whether the child's plan and the mother's plan describe the same family. Hidden items in this system do not only punish; they omit, and an omission, repeated across updates, becomes a plan.
- HONEST LIMITS — A plan can be amended, a goal revisited, a request filed late and still heard; this ending is a season, not a life sentence, in the fiction and in the system it models. Real outcomes also turn on workers, judges, resources, and luck, and a young parent's own permanency — housing, school, a safe road out of care — is a real and worthy plan in its own right, not a distraction from her child's. The loss recorded here is specific and paper-sized: for one review cycle, the official story of Desiree's future was written without her daughter in it, and no one in the room had a document that said otherwise.
