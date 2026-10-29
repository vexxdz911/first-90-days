# THE FIRST 90 DAYS — Scenario 103: “What the Form Calls Neglect”

*Human-readable script. This document and `scenario-103.json` are generated from a single source and match node-for-node: same IDs, same order, same choices, same effects.*

**The family is fictional — a composite. No real person's story appears here.**

**Content note:** This scenario depicts an in-home case opened on a family living in a motel: a school report, a home visit, a scored assessment, service offers, and a review. There is no graphic content. Players may skip any scene or use the quick exit at any time.

**How to read effects:** `cash −40` changes the player's cash. `FLAG: name` sets a flag the engine tracks. `HIDDEN + item` means the case file quietly records that item at this choice — the player does not see it when it happens. `REQUIRES FLAG: name` means the choice is only available if that flag was set earlier; `REQUIRES NO FLAG: name` means it is only available if that flag was never set. `NOTE:` is text shown to the player right after choosing.

Start date: Monday, April 6, 2026. Day offsets are days since the scenario's start date.

## [start] A Room Paid by the Week
*Day 0 — Monday, April 6, 2026 (dayOffset 0)*

Your name is Gloria Boateng. Your daughter Edith is ten. Since the eviction last month, the two of you have lived in one motel room off the highway — a bed each, a hot plate you use carefully, a small table where Edith does homework under the lamp.

You pay for the room week to week from cleaning work: offices at night, houses on Saturdays. It is not the home you had. It is, this month, the home you can pay for — and Edith has not missed her school, her bus stop, or the library across the street.

**Choices:**
- Start the week the way you always do — lunches, uniform, bus stop → **morning_routine**

## [morning_routine] The Morning Routine
*Day 1 — Tuesday, April 7, 2026 (dayOffset 1)*

Edith is tired some mornings. Cleaning shifts end late, the motel walls are thin, and breakfast is sometimes a granola bar eaten on the walk. Other mornings she is first at the bus stop, homework done, hair braided at the small table.

You keep the routine because routine is the one thing the room cannot take away. Same school. Same stop. Same library card, renewed at the desk across the street.

**Choices:**
- Walk Edith to the bus stop and go to your day shift → **bus_stop_scene**

## [bus_stop_scene] The Same Bus Stop
*Day 2 — Wednesday, April 8, 2026 (dayOffset 2)*

The bus stop is two corners from the motel, past the library. Edith knows the driver, the driver knows Edith, and the crossing guard saves her the good greeting. Stability, in a ten-year-old's life, is mostly this: the same faces, in the same order, every morning.

You file that thought where Vera's note will later join it. A form can record an address changing. It takes a person — or a folder — to record everything that did not change.

**Choices:**
- Continue → **school_gate**

## [school_gate] Vera at the School Gate
*Day 3 — Thursday, April 9, 2026 (dayOffset 3)*

Edith's teacher, Vera, meets you at pickup with a folder of Edith's work. Her reading is steady. Her attendance, Vera says, is better than half the class — a fact she says the way teachers say facts they have checked.

Vera also says, carefully, that Edith has been tired, and hungry some mornings, and that the school has noted the motel address. "I wrote down the attendance too," she says. "All of it. Not just the tired days."

**Choices:**
- Thank Vera and ask her to keep writing down all of it → **cleaning_shift**
  - NOTE (shown after choosing): A teacher who records the whole picture is a witness to stability, not just to worry.

## [cleaning_shift] The Night Shift
*Day 4 — Friday, April 10, 2026 (dayOffset 4)*

Your night cleaning shift runs office to office with a cart, a ring of keys, and a supervisor's sheet you sign at each stop. The work is invisible by design — offices are clean in the morning and nobody asks how.

Tonight you sign each sheet carefully and keep your copy. Invisible work still leaves paper, if the worker keeps it.

**Choices:**
- Continue → **report_call**

## [report_call] The Call About a Case Opening
*Day 5 — Saturday, April 11, 2026 (dayOffset 5)*

The agency calls on your break. A report has been made from the school — tiredness, hunger some mornings, an address that has changed too often. A case is being opened, and a caseworker, Ms. Harkness, will visit the motel.

The voice on the phone is not unkind. It is procedural. A visit, an interview, a form. You write the date and time on the back of a pay stub, because paper is what you have.

**Choices:**
- Write down the visit date, and tell your shift supervisor you may need an hour → **motel_visit_prep**

## [motel_visit_prep] Preparing the Room
*Day 6 — Sunday, April 12, 2026 (dayOffset 6)*

You could spend the evening hiding the room's poverty — the hot plate, the clothes in a suitcase, the food in a cooler. Or you could let the room show what it actually is: clean, ordered, paid for, and too small.

Edith puts her library books in a straight line on the table. "So she sees I read," she says. She understands more about being looked at than a ten-year-old should have to.

**Choices:**
- Clean the room, lay out the rent receipts, and let it be what it is → **motel_visit**  _(FLAG: roomDocumented ; HIDDEN + Home as observed — clean, ordered, motel room; rent receipts laid out)_

## [motel_visit] Ms. Harkness and the Form
*Day 7 — Monday, April 13, 2026 (dayOffset 7)*

Ms. Harkness is polite and thorough. She notes the room, the cooler, the hot plate, the absence of a kitchen. She asks about utilities — they are in the motel's name, not yours. She asks about food, and about how long you expect to stay.

As she talks, she completes a scored assessment form. You cannot see the items or the ratings. You can see the pen move at the words kitchen, utilities, food, housing — the prices of the room, written down one by one. None of them is a thing you chose carelessly. All of them are being recorded.

**Choices:**
- Answer plainly, and ask what happens next → **after_visit**

## [after_visit] What the Pen Was Writing
*Day 9 — Wednesday, April 15, 2026 (dayOffset 9)*

After she leaves, Edith asks if you passed. You do not know, and that not-knowing sits in the room all evening.

On the small table is the leaflet Ms. Harkness left: services, a phone number, and — in smaller print — words about records and representation. You read it twice, the way you read the motel receipt each week: looking for the line that matters.

**Choices:**
- Take the leaflet to a lawyer before you sign anything else → **leaflet_reading**

## [leaflet_reading] Reading the Leaflet Twice
*Day 10 — Thursday, April 16, 2026 (dayOffset 10)*

You read the leaflet again at the small table, slowly, with Edith's dictionary for two words. Most of it is services and phone numbers. The lines about records and counsel are short, and they are the lines you underline.

Underlining is not a legal act. It is the moment before one — the moment a right stops being print and starts being a plan.

**Choices:**
- Continue → **lawyer_meet**

## [lawyer_meet] Mr. Cordero Explains the Ground
*Day 11 — Friday, April 17, 2026 (dayOffset 11)*

Mr. Cordero is your attorney. He explains, in plain words, that you have the right to counsel in these proceedings, and to appointed counsel if you cannot afford one. (42 Pa.C.S. § 6337) He also explains the difference this case will turn on.

"Conditions are not conduct," he says. "A cooler is a condition. Feeding your daughter is conduct. The file right now may not separate them. Our job — yours and mine — is to make a record that does. Paper by paper."

**Choices:**
- Ask him where to start → **folder_choice**

## [folder_choice] A Folder, From Day One
*Day 13 — Sunday, April 19, 2026 (dayOffset 13)*

He slides a plain folder across the desk. "Everything, dated. Pay stubs. Rent receipts. School notes. Every letter you send, keep the copy. Every promise anyone makes you, write down who said it and when."

It is unglamorous advice, and it will cost you evenings at the small table after shifts. The alternative is to trust that the agency's folder — the one with the form in it — is keeping the same care for your side of the facts.

**Choices:**
- Start the folder tonight — pay stubs, motel receipts, school notes, dated → **work_paper**  _(FLAG: keptFolder ; HIDDEN + Parent folder — started day 13; receipts and school notes dated and kept)_
- Trust the agency's file to hold the facts — you are too tired for two folders → **work_paper**
  - NOTE (shown after choosing): One folder will still be kept in this case. It just will not be yours.

## [work_paper] The Work Record
*Day 18 — Friday, April 24, 2026 (dayOffset 18)*

Your cleaning work leaves a paper trail most jobs do not: agency invoices, house clients who pay by check, a supervisor who can confirm the night shifts. Together they show the thing the form's housing items cannot — the room is paid for by work that has not stopped.

Your supervisor can sign a short statement: shifts, dates, pay. Signed paper travels. A supervisor's memory, however kind, does not.

**Choices:**
- Ask your supervisor for a signed, dated work statement and file it → **records_request**  _(cash −5 ; FLAG: workRecords ; HIDDEN + Work — signed supervisor statement; shifts and pay documented)_
- Ask her to remember it for now — you can get it later if needed → **records_request**
  - NOTE (shown after choosing): Later is a tense this case uses a lot. It rarely improves paper.

## [records_request] The Record Request
*Day 20 — Sunday, April 26, 2026 (dayOffset 20)*

Mr. Cordero shows you the sentence he wants in a letter, in writing, to the agency: under 55 Pa. Code § 3130.44(d), the assessment record shall be released upon request. "Not a favour," he says. "A request the rule answers."

Sending it costs copies and postage and an evening. Not sending it means continuing to be scored by a form you have never seen — guessing at items while the pen is already moving.

**Choices:**
- Sign and send the written record request under § 3130.44(d) → **packet_arrives**  _(cash −10 ; FLAG: recordsRequested ; HIDDEN + Records — written request under 55 Pa. Code § 3130.44(d) sent day 20)_
- Wait until you know more before asking for the record → **packet_arrives**
  - NOTE (shown after choosing): You will know more eventually. The question is whether you will know it in time to correct it.

## [packet_arrives] The Packet Arrives
*Day 28 — Monday, May 4, 2026 (dayOffset 28)*

The packet arrives redacted, partial, and still transformative. For the first time, you can see the scored assessment form's items as they were filled in at the motel.

You read it at the small table after Edith is asleep, with Mr. Cordero's distinction in your head: conditions, conduct. The form, page after page, has recorded the first as if it were the second.

**Choices:**
- Read the items one by one, with a pencil → **reading_form**

## [reading_form] Reading the Items, One by One
*Day 31 — Thursday, May 7, 2026 (dayOffset 31)*

No kitchen. Utilities not in her name. Food insecurity. Unstable housing. Each item is true, in the narrow way a checkbox is true. The room has no kitchen — it is a motel room. The utilities are the motel's. Food is tight in the week before payday, and Edith eats breakfast at school on those mornings.

What the items do not record: that Edith has attended the same school without interruption, that her homework is done at that table nightly, that the room is paid current, that the library across the street knows her name. The form has no box for the bus stop she has never missed. That absence — not any single item — is the case.

**Choices:**
- Take the packet to Mr. Cordero and ask what can be corrected, in writing → **correction_letter**

## [correction_letter] The Correction Letter
*Day 34 — Sunday, May 10, 2026 (dayOffset 34)*

Together you draft a written correction — not an argument, a separation. Item by item: this is a condition of the motel, with the receipt attached; this is conduct, with the school's attendance record attached; this referral was offered, this one was not.

Mr. Cordero is precise about the tone. "We do not say the items are lies. We say they are prices, recorded as risks. Then we attach the paper that shows the difference." Filing it puts that separation in the agency's own file, where the next reader will meet it.

**Choices:**
- File the written correction with receipts and the attendance record attached → **services_offer**  _(cash −5 ; FLAG: correctionFiled ; HIDDEN + Correction — written separation of conditions from conduct filed with receipts)_
- Explain the difference to Ms. Harkness at the next visit instead → **services_offer**
  - NOTE (shown after choosing): Spoken corrections live in the listener's notes. Filed corrections live in the file.

## [services_offer] Services, Concrete and Otherwise
*Day 38 — Thursday, May 14, 2026 (dayOffset 38)*

The agency offers services. Some are concrete: a food support referral you can use this week, and a housing navigator who works from a list of actual landlords. One is a name on a leaflet and a phone number that rings to a full voicemail box.

Accepting help is not an admission. Mr. Cordero's rule: accept what is concrete, in writing; write down what was offered, when, and what actually arrived — because a referral that goes nowhere is a fact about the referral, not about you.

**Choices:**
- Accept the concrete services in writing, and log every offer with its date → **food_week**  _(FLAG: servicesAccepted ; HIDDEN + Services — concrete offers accepted in writing; offers logged by date)_
- Decline everything — accepting help feels like agreeing with the form → **food_week**
  - NOTE (shown after choosing): The form does not record your reasons. It records a refusal, in a box.

## [food_week] The Week the Food Arrived — and the Call That Didn't
*Day 42 — Monday, May 18, 2026 (dayOffset 42)*

The food support arrives, and the week's mornings change: Edith eats before the bus, at the small table, from a bag you unpack together. You log it — date, what arrived — the way you log everything now.

The voicemail-box referral does not call back. You log that too, with the dates you called. In other files, in other cases, that second log is the one nobody kept. In yours, it is on paper, in your handwriting, with Mr. Cordero holding a copy.

**Choices:**
- Keep both logs — what arrived, and what did not → **neighbour_help**  _(FLAG: serviceLog ; HIDDEN + Service log — delivery and non-delivery both recorded with dates)_

## [neighbour_help] The Corridor Neighbours
*Day 44 — Wednesday, May 20, 2026 (dayOffset 44)*

The family two doors down lends you a real saucepan and refuses it back until 'the kitchen situation improves.' Edith writes a thank-you note and delivers it like a diplomatic instrument.

You log the saucepan too — not from suspicion, but because this corridor, whatever the form calls it, has become a small documented community around your daughter: neighbours, a manager, a teacher, a librarian who knows her name.

**Choices:**
- Continue → **housing_navigation**

## [housing_navigation] The Housing Navigator and the List
*Day 46 — Friday, May 22, 2026 (dayOffset 46)*

The housing navigator is a practical person with a printed list. Your name can go on the housing waitlist — a real list, with a real position that will not move quickly — and she can write down, today, that you applied, with the date.

A dated application is not housing. It is the difference, on paper, between a mother waiting to be rescued and a mother in a queue she entered on a recorded date, still paying for a motel room in the meantime.

**Choices:**
- Apply, and get the dated application and waitlist position in writing → **manager_record**  _(cash −5 ; FLAG: waitlistPaper ; HIDDEN + Housing — dated waitlist application and position in writing)_
- Take the list home and apply when things settle down → **manager_record**
  - NOTE (shown after choosing): Things are not settling down. That is, in a sense, the whole form.

## [manager_record] The Manager's Ledger
*Day 50 — Tuesday, May 26, 2026 (dayOffset 50)*

The motel manager keeps a ledger — room, weeks, paid. He has watched families come and go, and he says, without ceremony, that yours is the room where the light is on over homework every night and the rent has never been late.

He will copy the ledger page and sign it. A motel ledger is not a lease. It is, however, a dated record kept by a stranger with no reason to favour you — the kind of paper files find hard to argue with.

**Choices:**
- Get the signed ledger copy and file it with the receipts → **second_visit**  _(FLAG: managerLetter ; HIDDEN + Motel ledger — signed copy; room paid current, week by week)_
- Skip it — a motel ledger might just underline the motel → **second_visit**
  - NOTE (shown after choosing): The file already knows it is a motel. What it may not know is 'paid current, every week.'

## [second_visit] The Second Visit
*Day 54 — Saturday, May 30, 2026 (dayOffset 54)*

Ms. Harkness returns. The room is the same room. What has changed is the paper around it: your folder on the table, the correction in her file, the waitlist application, the ledger.

She notes the food in the cupboard space you have made, Edith's library books, the homework chart on the wall. Her pen still moves — but you are no longer guessing entirely at what it can honestly write. Some items, on a second look, have somewhere else to go.

**Choices:**
- Walk her through the folder, item by item, calmly → **family_meeting**

## [family_meeting] The Family Meeting
*Day 58 — Wednesday, June 3, 2026 (dayOffset 58)*

At the family meeting, the agency lays out its concerns in the form's language, and Mr. Cordero lays out the correction in the file's language — receipts, attendance, dates. Vera's written note is there: Edith's attendance, her reading, the tired mornings recorded alongside the steady ones.

No one declares victory. Meetings in this system rarely do. But the conversation has changed its subject: from the prices of a motel room to the documented conduct of the mother who pays for it. That change of subject is the strategy, working.

**Choices:**
- Ask for the meeting's conclusions in writing before you leave → **removal_threat**  _(FLAG: meetingWritten ; HIDDEN + Family meeting — conclusions requested in writing; correction discussed on the record)_

## [removal_threat] The Night the Threat Was Made
*Day 62 — Sunday, June 7, 2026 (dayOffset 62)*

A week later, after a neighbour's loud night in the corridor and a fresh report that names the motel rather than anything Edith did, Ms. Harkness calls with a supervisor on the line. They are considering, she says, whether Edith should be placed tonight while the new report is looked into.

This is the moment the early paper was for. Mr. Cordero is on the phone within the hour. What happens next depends — as it was always going to — not on how tonight feels, but on what the file already holds when tonight arrives.

**Choices:**
- Put Mr. Cordero on speaker and lay the filed correction, the record packet, and the folder on the table → **threat_passes**  _(REQUIRES FLAG: recordsRequested ; REQUIRES FLAG: correctionFiled)_
  - NOTE (shown after choosing): This choice exists because the record was requested and the correction was filed — weeks ago, when it felt like paperwork.
- Plead tonight's facts from memory — the folder is disorganised and the correction was never filed → **removal_door**
- Tell them to leave the room and close the door — no one is taking Edith on a phone call → **removal_door**
  - NOTE (shown after choosing): The anger is understandable. The file will record the closed door, not the reasons for it.

## [threat_passes] Paper, Answered at Night
*Day 65 — Wednesday, June 10, 2026 (dayOffset 65)*

Mr. Cordero speaks in dates. The record was requested and received. A written correction, with receipts and attendance, is in the agency's file. Edith's school has not changed, her attendance has not broken, the room is paid current on a signed ledger, services accepted are logged — delivered and undelivered alike.

The supervisor is quiet for a moment. Placement tonight, on this file, would have to be explained against that paper in a courtroom within days. The decision, when it comes, is procedural and complete: no placement. A follow-up visit, scheduled, in writing. Edith sleeps in her own bed, in the room with the homework chart.

**Choices:**
- Write down tonight's decision, who made it, and the follow-up date → **services_gap**

## [services_gap] The Referral That Went Nowhere
*Day 69 — Sunday, June 14, 2026 (dayOffset 69)*

The voicemail-box referral surfaces again at review: the agency's notes show it as 'service offered.' Your log shows the dates you called, the full mailbox, the call that never came back — a referral that was, on paper, an action, and in Edith's life, nothing at all.

Mr. Cordero does not raise his voice about it. He asks that the log be attached to the file, so the record shows both halves: offered, and not delivered. A file that can hold that distinction, he says afterward, can hold the larger one too.

**Choices:**
- Ask for your service log to be attached to the agency file → **benefits_paper**  _(FLAG: serviceLog ; HIDDEN + Services — non-delivery log attached to agency file)_

## [benefits_paper] Paperwork in Motion
*Day 73 — Thursday, June 18, 2026 (dayOffset 73)*

There is other paperwork now, moving at the speed paperwork moves: the waitlist position, confirmed again in writing; an assistance application filed and stamped, its outcome not yours to promise Edith or anyone. You make no claims about it beyond the true one — it is filed, dated, and pending.

You file the stamped copies. Motion, documented, is not the same as arrival. But it is the opposite of the stillness the first form described.

**Choices:**
- File the stamped copies and update the folder's index → **vera_update**

## [vera_update] Vera's Second Note
*Day 77 — Monday, June 22, 2026 (dayOffset 77)*

Vera sends a second note at the end of term. Edith's attendance: unbroken. Her reading: ahead of where she started. Tired mornings: fewer, since the food support began — a sentence that quietly connects a service delivered to a worry receding.

You file it on top. Teachers' notes are not court orders. They are something rarer in this file: a record of the child, written by someone who sees her every day, in full sentences.

**Choices:**
- Take Vera's note and the updated folder to the review preparation → **review_prep**  _(FLAG: schoolLetter ; HIDDEN + School — second teacher note; attendance unbroken, reading progressing)_

## [review_prep] Preparing the Review
*Day 81 — Friday, June 26, 2026 (dayOffset 81)*

Mr. Cordero spreads the folder's index on his desk: work statement, ledger, correction, service log — delivered and undelivered — waitlist application, two teacher notes, meeting conclusions in writing.

"Read it as a stranger," he says. "A stranger should be able to tell, from paper alone, the difference between a family in danger and a family in a motel. If the stranger can, we are ready. If not, we write the missing page this week — not the night before."

**Choices:**
- Read it as a stranger, and write the one missing page together → **agency_review**

## [agency_review] The Review
*Day 85 — Tuesday, June 30, 2026 (dayOffset 85)*

The review is quieter than the night of the threat. The agency's reader has the whole file now — the form, and everything the form did not hold. The poverty items are still in it. They are no longer alone in it.

The recommendation, when it comes, is written: no adjudication sought. Services to continue while the waitlist moves. A closing review, dated, if the record stays as it stands. Edith, beside you, is drawing on the back of an agenda — a house, this time with a kitchen she has drawn first, largest, in the middle of the page.

**Choices:**
- Ask for the written recommendation, and file it that night → **closing_terms**

## [closing_terms] The Terms of Closing
*Day 87 — Thursday, July 2, 2026 (dayOffset 87)*

Mr. Cordero reads the written recommendation twice and makes you read it a third time. No adjudication sought. Services continue while the waitlist moves. A closing review on a stated date, if the record stays as it stands.

'If the record stays as it stands,' he repeats. 'So we keep the record standing. Same folder, same dates, until the closing paper is in your hands — not promised, in your hands.'

**Choices:**
- Continue → **recheck_visit**

## [recheck_visit] The Last Visit
*Day 89 — Saturday, July 4, 2026 (dayOffset 89)*

The last visit is short. Ms. Harkness notes the room, the food, the chart, Edith's books. There is no drama in it, and you have learned to be grateful for paperwork without drama.

She tells you the closing paperwork is being prepared. You ask — out of a habit that is now simply how you do things — for a copy, in writing, when it is filed.

**Choices:**
- File the last visit note with everything else → **end_best**

## [removal_door] At the Motel Door
*Day 62 — Sunday, June 7, 2026 (dayOffset 62)*

They come in the evening, with the new report in a folder and the first form underneath it — the one that recorded a motel room's prices as a child's risks, uncorrected, because no correction was ever filed and no record was ever requested in time to write one.

Edith is placed that night. It is done procedurally, with a bag packed at the small table and the library books left in their straight line. You are given papers, and among them the one that matters most tonight: the hearing date. A child placed in shelter care must have an informal hearing not later than 72 hours after placement. (42 Pa.C.S. § 6332; 23 Pa.C.S. § 6315(d))

**Choices:**
- Take the papers, note the hearing date, and call Mr. Cordero from the corridor → **shelter_hearing**
- Sign everything placed in front of you tonight without reading it → **shelter_hearing**
  - NOTE (shown after choosing): Tonight, of all nights, the reading matters.

## [shelter_hearing] Within Seventy-Two Hours
*Day 65 — Wednesday, June 10, 2026 (dayOffset 65)*

The shelter care hearing is held within the 72 hours the law requires. (42 Pa.C.S. § 6332; 23 Pa.C.S. § 6315(d)) Mr. Cordero is beside you, as counsel. (42 Pa.C.S. § 6337) He argues the difference between conditions and conduct — but tonight he argues it from memory and receipts produced from a bag, because the file itself holds only the form.

The court continues Edith's placement while the case is decided. An argument made at a hearing is a beginning. An argument already sitting in a file, dated weeks earlier, would have been evidence. The difference between those two things is the whole lesson of this branch, and it is a hard one.

**Choices:**
- Ask what happens next, and what paper can still be built → **shelter_after**
- Go home to the room and wait for the agency to call → **end_removal**

## [shelter_after] Building Paper, Late
*Day 68 — Saturday, June 13, 2026 (dayOffset 68)*

You build the folder now — receipts, work statement, Vera's note — and Mr. Cordero files what can still be filed. Late paper is not worthless. It is simply late: the adjudication will be decided on a record whose first and fullest account of your family is still the form from the motel visit.

Edith's visits begin. She asks about the library books. You tell her they are in their line, waiting — which is true, and not the same as her being there to read them.

**Choices:**
- Go to the adjudication hearing with the late-built folder → **visits_begin**

## [visits_begin] Visits Begin
*Day 72 — Wednesday, June 17, 2026 (dayOffset 72)*

Visits begin in a room with toys Edith is slightly too old for, which she plays with anyway, kindly, for the benefit of the adults watching. She tells you about her placement in the careful voice children use for news they have decided not to cry about.

You write the visit log yourself afterward — date, length, what was said about the next one — and Mr. Cordero files it. Even here, especially here, the folder grows.

**Choices:**
- Continue → **adjudication_hearing**

## [adjudication_hearing] The Adjudication Hearing
*Day 82 — Saturday, June 27, 2026 (dayOffset 82)*

At adjudication, the agency's case is the form, read fluently: no kitchen, utilities not in her name, food insecurity, unstable housing. Each item is proven the way checkboxes are proven — by the form that recorded them.

Mr. Cordero offers your folder, and the court hears the distinction he draws. But the distinction arrives as an argument about a record, not as a record itself — no requested packet, no filed correction, no dated log from the weeks when it could have changed the file's centre of gravity.

**Choices:**
- Hear the court's decision → **end_adjudication**

## [end_best] What the Form Calls Neglect
*Day 97 — Sunday, July 12, 2026 (dayOffset 97)*

The case is closed without adjudication. No court ever found Edith dependent. No night was ever spent apart — mother and daughter together throughout, in the room that became, on paper at least, legible for what it was.

The file's last entry is not the form. It is the corrected record: the separation, item by item, of what poverty costs from what a parent does — with receipts, attendance, a ledger, and a teacher's two notes attached. The form is still in the file, underneath. Files keep everything. What changed is what sits on top, and what any future reader will meet first.

Edith's drawing — the house with the kitchen drawn largest — is not in the file. It is on the motel wall, above the homework chart, where it belongs. The waitlist will move or it will not, at its own speed. Tonight, the room is paid, the folder is closed, and the light over the small table is on.

**Ending.**

**Debrief:**
- THE LAW, BEAT BY BEAT — Counsel: Gloria had an attorney, and the right to counsel (including appointed counsel if she could not afford one) is stated at 42 Pa.C.S. § 6337. Records: the turning point of this scenario is the written request under 55 Pa. Code § 3130.44(d) — the assessment record 'shall be released upon request' (flag: recordsRequested). Only with the packet could the written correction (flag: correctionFiled) separate conditions from conduct inside the agency's own file. Shelter care: on this route Edith was never placed, so the 72-hour rule (42 Pa.C.S. § 6332; 23 Pa.C.S. § 6315(d)) was never triggered — it appears only on the removal branch, where the hearing is held on Day 65, exactly three days after the Day 62 placement.
- THE HIDDEN FORM, MAPPED — The scored assessment form's items were all poverty markers recorded as risks: no kitchen, utilities not in the mother's name, food insecurity, unstable housing (hidden items from the motel visit). The winning route did not dispute that those items were factually true; it changed what else the file held beside them — work statement (workRecords), signed motel ledger (managerLetter), school attendance and teacher notes (schoolLetter), dated waitlist application (waitlistPaper), and a service log recording both delivery and non-delivery (serviceLog). The referral that was offered but never delivered is texture drawn from documented patterns of referrals lost as 'empty actions' — logged here, not argued as malice.
- Outcomes in this system also turn on workers, judges, resources, and luck — a different supervisor on the night of the threat, a different reader at review, or a waitlist that never moved could each have changed this ending, and none of them was in Gloria's control. This ending is not a verdict on any parent who did not reach it: it records what happened when the paper was built early enough to be in the file on the night it was needed.

## [end_removal] Removal at the Motel Door
*Day 65 — Wednesday, June 10, 2026 (dayOffset 65)*

Edith remains placed after the shelter care hearing, with visits to be scheduled and a case that will now be decided from inside a placement. The room keeps its straight line of library books. The folder you will now build starts weeks after the file that decided tonight was written.

Mr. Cordero is blunt, and kind in his bluntness: "We build from here. The next hearing is a real hearing, and paper filed before it counts. It counts less than paper filed before tonight would have. Both of those are true, and we work with the second without forgetting the first."

**Ending.**

**Debrief:**
- THE LAW, BEAT BY BEAT — Placement occurred on Day 62; the shelter care hearing was held on Day 65, within 72 hours as required (42 Pa.C.S. § 6332; 23 Pa.C.S. § 6315(d)), with counsel beside Gloria (42 Pa.C.S. § 6337). The record request under 55 Pa. Code § 3130.44(d) was never exercised in time on this route (no recordsRequested flag), so no filed correction (no correctionFiled flag) was in the agency's file when the placement decision was made — the form's poverty items stood in it uncorrected.
- THE HIDDEN FORM, MAPPED — As in every route, the form recorded conditions — no kitchen, utilities in the motel's name, food insecurity, motel housing — as risk items. Without the packet, Gloria could not see those items early enough to answer them in writing; without the folder (workRecords, managerLetter, schoolLetter), the hearing heard an argument instead of a record.
- Outcomes in this system also turn on workers, judges, resources, and luck, and a removal is a procedural step in a continuing case, never a verdict on a parent's worth. Parents have rebuilt cases from exactly this point. What this ending measures is timing: the same facts, filed later, met a decision that had already been made.

## [end_adjudication] Adjudicated on the Poverty Record
*Day 85 — Tuesday, June 30, 2026 (dayOffset 85)*

The court adjudicates Edith dependent on the record before it — a record whose centre is still the scored form from the first motel visit: the prices of poverty, proven as checkboxes, answered too late by paper that arrived as argument.

Edith remains placed while a plan is written. Gloria leaves with Mr. Cordero's list for the next stage — services, visits, reviews — and with the folder, now real, now growing, now chasing a file that had a seven-week head start. The case is not over. Cases rarely end at adjudication. But its hardest chapter will be written uphill, against a first account that was never corrected in time.

**Ending.**

**Debrief:**
- THE LAW, BEAT BY BEAT — This route passed through placement on Day 62 and a shelter care hearing on Day 65, within 72 hours (42 Pa.C.S. § 6332; 23 Pa.C.S. § 6315(d)), with counsel (42 Pa.C.S. § 6337). At adjudication the decisive material was the certified file as it stood. The record request (55 Pa. Code § 3130.44(d)) and the written correction that depends on it were the missing moves: without them, the distinction between conditions and conduct was argued orally, late, against a written form.
- THE HIDDEN FORM, MAPPED — The hidden items are the same on every route — kitchen, utilities, food, housing — because the room was the same room. What differed was the surrounding record: no early work statement in the file, no signed ledger, no dated service log separating a delivered service from an offered one. Adjudication on this record is the system reading its own first draft as if it were the whole book.
- Outcomes in this system also turn on workers, judges, resources, and luck — the adjudication judge's reading, the agency's posture, and the timing of every paper all mattered here, and an adjudication is a stage in a case, not a final judgment on a mother. This ending is included so the cost of the missing early paper is visible in the place it is actually paid: a hearing room, months of work later.
