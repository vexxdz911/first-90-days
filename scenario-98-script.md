# THE FIRST 90 DAYS — Scenario 98: “The Interpreter Who Wasn't Booked”

*Human-readable script. This document and `scenario-98.json` are generated from a single source and match node-for-node: same IDs, same order, same choices, same effects.*

**The family is fictional — a composite. No real person's story appears here.**

**Content note:** This scenario depicts a Deaf mother's in-home case: meetings held without an interpreter, a safety plan presented for signature, and a review. There is no graphic content. Players may skip any scene or use the quick exit at any time.

**How to read effects:** `cash −40` changes the player's cash. `FLAG: name` sets a flag the engine tracks. `HIDDEN + item` means the case file quietly records that item at this choice — the player does not see it when it happens. `REQUIRES FLAG: name` means the choice is only available if that flag was set earlier; `REQUIRES NO FLAG: name` means it is only available if that flag was never set. `NOTE:` is text shown to the player right after choosing.

Start date: Monday, February 16, 2026. Day offsets are days since the scenario's start date.

## [start] The Clinic Visit
*Day 0 — Monday, February 16, 2026 (dayOffset 0)*

Your name is Ramona Dube. You are Deaf, and your first language is ASL. Your daughter Nora is five — hearing, bright, and fluent in the particular sign-and-gesture language the two of you have built at home, the way every family builds one.

This morning's clinic visit was for Nora's ear follow-up and a vaccination. No interpreter was booked. Communication ran on a clipboard: short written notes, in quick clinical handwriting, for a conversation that was not short. Ramona answered what she could read, nodded at what she could not, and left with an after-visit sheet she is still working through at the kitchen table.

She does not know that a report was called in from the clinic, about communication and follow-through. She knows the visit went badly in a way that was not hers.

**Choices:**
- That evening, write a dated note of what happened at the clinic — who was there, what was written, what she could not follow → **knock**  _(FLAG: datedNote ; HIDDEN + Clinic visit — mother's dated account written the same evening)_
  - NOTE (shown after choosing): Four lines and a date. It looks like nothing. In two months it will be the first page of the record that answers the other record.
- Go to bed and start fresh tomorrow → **knock**
  - NOTE (shown after choosing): Tomorrow will have its own paperwork. Today will have only the clinic's version.

## [knock] A Knock, a Notebook
*Day 2 — Wednesday, February 18, 2026 (dayOffset 2)*

Ms. Pemberton, from the county children and youth agency, comes to the door with a folder and no interpreter. Communication happens the way it happened at the clinic: a notebook, passed back and forth on the doorstep. She writes the concern — the clinic visit, questions about follow-through and how Ramona manages appointments. Ramona writes back about Nora: school, meals, the visual schedule on the refrigerator that runs their mornings.

The notebook works, slowly, for a doorstep. It is not a way to hold a meeting, sign a plan, or answer an investigation. At the bottom of the last page there is room for one more exchange.

**Choices:**
- Write: 'Meetings about Nora need an ASL interpreter. Please book one. I will keep these pages.' → **first_meeting**  _(FLAG: interpreterRequested ; HIDDEN + Interpreter — requested in writing at the first contact; notebook pages kept)_
  - NOTE (shown after choosing): A request, in writing, dated, kept. Whatever happens next, the file cannot honestly say she never asked.
- Write: 'Okay, thank you,' and close the door kindly → **first_meeting**
  - NOTE (shown after choosing): Kind, and brief. The file will record a cooperative doorstep — and no request at all.

## [first_meeting] The Meeting With No Interpreter
*Day 4 — Friday, February 20, 2026 (dayOffset 4)*

The office meeting is Friday. There is no interpreter. Ms. Pemberton talks; a colleague takes notes; Ramona follows perhaps half — the half that faces her, at speaking speed, in a room with the light behind the speaker. A scored assessment form is filled in as the meeting goes. Ramona cannot see the items on it. Nobody offers to show her.

On the table is her own notebook, open, with the request from Wednesday at the top of a fresh page.

**Choices:**
- Hand over the written request again, keep a copy, and write the date and 'no interpreter present' at the top of her notes → **safety_plan_pushed**  _(cash −4 ; FLAG: meetingsDocumented ; HIDDEN + Meeting — no interpreter present; fact documented by the mother in writing, with a copy kept)_
  - NOTE (shown after choosing): Copies cost money. So does everything in this system that works. The meeting now exists in two records: theirs, and hers.
- Try to follow, answer what she can, and save the requests for a better day → **safety_plan_pushed**
  - NOTE (shown after choosing): She answers bravely and partially. The form records the partial part.

## [safety_plan_pushed] A Plan, Pushed Across the Table
*Day 7 — Monday, February 23, 2026 (dayOffset 7)*

At the end of the meeting, a safety plan is pushed across the table: three pages, dense paragraphs, small type, a signature line. It is the kind of document lawyers read twice with a pen. It is offered to a mother who has understood half the meeting, in her second language's written form, with the pen already uncapped.

Nora, meanwhile, is at kindergarten, unaware that her home is being decided in a document her mother has not been given a way to read.

**Choices:**
- Write on the plan itself: 'I will review this with my attorney before I sign,' and take the copy home unsigned → **iwu_call**  _(FLAG: planWithCounsel ; HIDDEN + Safety plan — taken home unsigned for review with counsel; notation written on the plan itself)_
  - NOTE (shown after choosing): Not a refusal — a sequence. Review first, signature after. The sentence she wrote on their document travels with their document.
- Sign it, so the meeting can end and Nora's home is not in question → **iwu_call**  _(FLAG: signedUnread ; HIDDEN + Safety plan — signed at the meeting, before review with counsel)_
  - NOTE (shown after choosing): The signature is real ink on a real plan. What the plan says will be news to her later, at the worst available moment.

## [iwu_call] Ms. Iwu, By Video
*Day 9 — Wednesday, February 25, 2026 (dayOffset 9)*

Ms. Iwu is Ramona's attorney. You have the right to counsel in this process, and to appointed counsel if you cannot afford one (42 Pa.C.S. § 6337) — Ms. Iwu treats the right as machinery, not decoration. Their call runs by video, with an interpreter, and it is the first fully understood conversation Ramona has had about her own case.

They go through the plan the slow way: line by line, the interpreter signing, Ramona stopping it wherever she needs to. A check-in visit, a clinic follow-up, a Tuesday phone call to the agency — a phone call, in a plan, for a Deaf mother. That line, at least, they can fix before it fails.

**Choices:**
- Go through every line, and have Ms. Iwu send a written plain-language summary of what the plan actually requires → **clinic_followup**  _(FLAG: planUnderstood ; HIDDEN + Safety plan — reviewed line by line with counsel through an interpreter; plain-language summary requested in writing)_
  - NOTE (shown after choosing): The plan, in language she can use, with the phone-call line flagged in writing. Understanding, documented.
- Cover the main points and trust the rest to be standard → **clinic_followup**
  - NOTE (shown after choosing): Standard is where the Tuesday phone call lives. Plans fail in their standard lines.

## [clinic_followup] Back to the Clinic, With Paper
*Day 11 — Friday, February 27, 2026 (dayOffset 11)*

The clinic follow-up is Ramona's to prepare for this time. She arrives with written questions, the after-visit sheet from February marked where she could not follow it, and Nora's vaccination record in a folder. The nurse answers in writing, slowly, and the visit works the way visits work when both sides can see the words.

It is also a demonstration, available to anyone watching the file, of what changes when communication is actually arranged.

**Choices:**
- Ask the clinic to note, in writing, how the next visit will communicate — before the visit, not at it → **second_meeting**  _(cash −7 ; FLAG: clinicNote ; HIDDEN + Clinic — communication for future visits requested in writing, in advance)_
  - NOTE (shown after choosing): Bus fare and a morning spent. The note joins the folder: communication, requested in advance, in writing, again.
- Handle this visit well and let it speak for itself → **second_meeting**
  - NOTE (shown after choosing): It spoke well — in a room the case file does not sit in.

## [second_meeting] The Second Meeting
*Day 14 — Monday, March 2, 2026 (dayOffset 14)*

The agency's second meeting is at Ramona's kitchen table. Again, no interpreter has been booked, although the request now exists in writing twice. Partway through, Ms. Pemberton — meaning helpfully, reaching for the nearest bridge — turns to Nora, who has come in for a glass of water, and begins to ask her to help explain the next form.

Nora is five. She is hearing, and she loves her mother, and neither of those things makes her an interpreter. Ramona can see exactly how this would read in a file: the child, translating the state's words to her own mother, in her own case.

**Choices:**
- Write it in the notebook, in front of everyone: 'Nora is five. She will not interpret. I am asking again, in writing, for an interpreter.' → **home_visit**  _(FLAG: childNotInterpreter ; FLAG: meetingsDocumented ; HIDDEN + Meeting — child not used as interpreter; refusal and renewed interpreter request documented in writing)_
  - NOTE (shown after choosing): The meeting pauses. The sentence goes in the notebook, dated, where Ms. Pemberton has just read it. Nora goes back to her water.
- Let Nora help this once — she is quick, and the form is short → **home_visit**
  - NOTE (shown after choosing): Nora does her best, proudly. The file will record that the meeting proceeded through the child, and it will not record whose idea it was.

## [home_visit] The Home Visit, In Writing
*Day 18 — Friday, March 6, 2026 (dayOffset 18)*

The home visit runs on the notebook, slowly and completely: Nora's breakfast routine, the visual schedule, school pickup, the neighbor across the hall who is Nora's emergency contact and knows it. Ms. Pemberton fills in a scored assessment form as she goes — home, supervision, support — writing about a household she is watching run on pictures, routines, and a five-year-old's total confidence in both.

Ramona's notebook fills too. Every page is dated. She has started keeping the used notebooks in a drawer, in order.

**Choices:**
- Walk through the whole routine in writing — meals, school, the schedule on the fridge, the neighbor's role → **record_learn**  _(HIDDEN + Home as observed — routines, visual schedule, and emergency contact explained in writing by the mother)_
  - NOTE (shown after choosing): Slow, complete, on paper. What the worker can see, the mother makes sure the worker can also read.
- Answer the questions asked and keep the visit short → **record_learn**
  - NOTE (shown after choosing): Short answers in a notebook are shorter still. The form fills its blanks either way.

## [record_learn] What Ms. Iwu Sends
*Day 21 — Monday, March 9, 2026 (dayOffset 21)*

Ms. Iwu's email this week has a line Ramona reads twice, through the interpreter on their video call: you can ask for the agency's own record — the file, and the scored form's items — and under the regulation it "shall be released upon request." (55 Pa. Code § 3130.44(d))

Ramona thinks about the form, filled in at meetings she half-understood, in rooms where she could not see the questions, let alone the answers being written about her.

**Choices:**
- Send the written record request this week, through Ms. Iwu, and keep the dated copy → **school_note**  _(cash −5 ; FLAG: recordsRequested ; HIDDEN + Agency record — requested in writing under § 3130.44(d); dated copy kept)_
  - NOTE (shown after choosing): A dated request, a kept copy. Whatever the form says, she will read it before the review does.
- Ask Ms. Pemberton at the next visit to just say what the file says → **school_note**
  - NOTE (shown after choosing): She will summarize, kindly. A summary of a form is not the form, and it will not be in Ramona's drawer of notebooks.

## [school_note] Nora's Teacher Writes It Down
*Day 25 — Friday, March 13, 2026 (dayOffset 25)*

Kindergarten sends home a note the way kindergarten does: Nora is reading above her level, Nora explained the visual schedule to a classmate 'like a teacher,' Nora's mother has never missed a pickup. It is signed, dated, and covered in a sticker.

It is also, filed in the right drawer, a third party's dated account of this household — the kind of paper that answers a form without arguing with it.

**Choices:**
- Ask the teacher for a clean copy for the case folder, and file it with the notebooks → **record_arrives**  _(FLAG: schoolNote ; HIDDEN + School — teacher's dated note on attendance and the child's progress filed by the mother)_
  - NOTE (shown after choosing): The sticker stays. Some exhibits deserve to arrive exactly as life made them.
- Put it on the refrigerator, where it belongs → **record_arrives**
  - NOTE (shown after choosing): It does belong there. It can be in two places — that is what copies are for — but only if someone makes one.

## [record_arrives] 'Uncooperative,' In Quotes
*Day 28 — Monday, March 16, 2026 (dayOffset 28)*

The packet arrives: the agency's file, partly blacked out in places, and the scored assessment form's items. Ramona reads it with Ms. Iwu, through an interpreter, at the speed understanding actually takes.

There it is, twice, in the cooperation item: 'uncooperative at meetings.' The dates beside it are the clinic meeting and the office meeting — the two meetings with no interpreter booked, where she could not follow what was being said. The form did not record that she asked for an interpreter in writing before either of them. Forms record what they are built to record. Corrections exist for the rest.

**Choices:**
- Read every item with Ms. Iwu and mark the two dates against the notebook pages → **correction**
  - NOTE (shown after choosing): Two dates, two notebook pages, two written requests. The correction is already assembled; it only needs to be written as one.

## [correction] The Correction Attaches the Notebook
*Day 32 — Friday, March 20, 2026 (dayOffset 32)*

The correction is two pages. Ms. Iwu drafts; Ramona checks every claim against the drawer of notebooks, page by page, because a correction is only worth the paper it can point to.

It does not argue about fairness. It attaches: the dated clinic note, the doorstep request, the meeting notes headed 'no interpreter present,' the page where a five-year-old was almost used as an interpreter and her mother wrote no. It asks that the cooperation item be read next to the communication record that produced it.

**Choices:**
- File the correction with the notebook pages and both interpreter requests attached → **plan_rewrite**  _(cash −6 ; FLAG: correctionFiled ; HIDDEN + Correction — filed with notebook pages and written interpreter requests attached)_
  - NOTE (shown after choosing): Copies cost money; the drawer keeps the originals. The file now contains the meetings twice — as they were scored, and as they happened.
- Send a short letter saying the rating is unfair and she always cooperated → **plan_rewrite**
  - NOTE (shown after choosing): True, and unattached. Unfair, without exhibits, reads in a file like a disagreement about adjectives.

## [plan_rewrite] The Plan, Again — Slower
*Day 35 — Monday, March 23, 2026 (dayOffset 35)*

The agency proposes a revised plan and a meeting to sign it. Ramona has been here before: a document, a table, a pen. This time she has a folder, a lawyer, a correction on file, and a very clear idea of the difference between a plan she has read and a plan she has signed.

What she asks for now decides what the next plan is made of: promises, or terms.

**Choices:**
- Ask, in writing, for the revised plan in plain language — with the interpreter bookings for every meeting written into the plan itself → **review_prep**  _(FLAG: bookingsInPlan ; HIDDEN + Revised plan — plain-language version and interpreter bookings requested in writing as plan terms)_
  - NOTE (shown after choosing): Not an interpreter promised. An interpreter booked, named as a plan term, so a missed booking is a missed term — the agency's, this time.
- Accept the promise that an interpreter 'will be there this time' → **review_prep**
  - NOTE (shown after choosing): This time is a tense, not a term. The plan will say whatever it says, and it will not say that.

## [review_prep] Rehearsing With Ms. Iwu
*Day 38 — Thursday, March 26, 2026 (dayOffset 38)*

Rehearsal, through an interpreter, at kitchen-table speed: dates first, notebook open, the correction's attachments in order. Ms. Iwu's questions are the review's questions, asked in a kind voice that does not soften them: What happened at the February meetings? How do you know? Where is it written?

Every answer Ramona has is a page. That was not an accident, and it was not free — it cost notebooks, copies, bus fare, and the particular effort of writing everything down in a second language while being scored on the writing.

**Choices:**
- Rehearse from the folder: every answer a date, every date a page → **review**  _(cash −8 ; FLAG: reviewReady ; HIDDEN + Review — mother prepared to answer from dated documents, rehearsed with counsel)_
  - NOTE (shown after choosing): Bus fare, copies, an afternoon. The folder goes to the review tabbed, in order, ready to be handed up.
- Plan to explain it all directly at the review — they will understand when they see her → **review**
  - NOTE (shown after choosing): They will see her. What they will decide on is the file, and the file is what the folder is for.

## [review] The Review
*Day 42 — Monday, March 30, 2026 (dayOffset 42)*

The review room has the whole case in it: Ms. Pemberton's report, the scored form with its two 'uncooperative' entries, the plan history, and — filed or not filed, attached or unattached — Ramona's side of the paper. An interpreter is present today. Everyone notes it. Ramona notes who had to ask, in writing, four times, to make it so.

The question in front of the room is the plan: whether the home arrangement continues on a revised plan Ramona can actually use — or whether the plan she signed in February, with its unread terms and its missed check-in, is the record this case runs on.

**Choices:**
- Hand up the folder — the correction, the notebook pages, the written requests — and ask for the revised plan with interpreter bookings written into it → **end_win**  _(REQUIRES FLAG: recordsRequested ; REQUIRES FLAG: correctionFiled ; REQUIRES FLAG: planUnderstood ; REQUIRES NO FLAG: signedUnread)_
  - NOTE (shown after choosing): Dates answer dates. The 'uncooperative' entries meet the meetings that produced them, in the mother's own kept record.
- Explain, through the interpreter, how hard she has tried to cooperate → **removal_order**
  - NOTE (shown after choosing): It is true, and she says it well. Trying, explained at the review, is a speech. The file in front of the room is still the February file.

## [removal_order] The Order at the End of the Review
*Day 42 — Monday, March 30, 2026 (dayOffset 42)*

The room decides on the record it has. The February plan — signed, unread, with a Tuesday check-in Ramona never knew existed — was breached, on paper, weeks ago. Her cooperation, as scored at meetings she could not follow, is the file's account of her. The explanation she gave today is in the transcript. The documents that would have answered it are in a drawer, or were never made.

Nora is placed today, with a foster family the agency has used before, while the case continues. The goodbye runs on procedure: a bag packed, a visual schedule copied for the foster mother, a paper handed to Ramona with a date on it. The paper says there will be a shelter care hearing within 72 hours — by Thursday, April 2, 2026 — and that she has the right to counsel there.

**Choices:**
- Write down everything she is told, and send the hearing date to Ms. Iwu tonight → **end_removal**
  - NOTE (shown after choosing): Names, times, the date. Paper remembers what shock forgets — she has always known that; it is the lesson and the wound of this whole case.

## [end_win] Read It With Her
*Day 45 — Thursday, April 2, 2026 (dayOffset 45)*

The revised plan comes back in plain language, and it is read the way plans should be read: with Ramona, through an interpreter, line by line, at a table where stopping is allowed. The Tuesday phone call is gone — replaced with a written check-in she can actually perform. And in the plan's own terms, in writing, where terms live: an interpreter booked for every meeting, named as the agency's step, not her request.

The cooperation item is corrected on the record: the February meetings are re-read next to the notebook pages, and the file now says what happened in those rooms — a mother asking, in writing, for a way to understand, in a system that scored her for not understanding.

Nora never left home. She is at the kitchen table now, explaining the new plan's picture schedule to her mother, like a teacher. The plan she is explaining is one her mother has read.

**Ending.**

**Debrief:**
- WHAT THE FORM SAID (the hidden assessment, revealed): The items moving underneath this story were the home as observed (routines, the visual schedule, the emergency contact — all explained in writing), the school's dated account, and, decisively, cooperation as scored at meetings. That item read 'uncooperative' twice, and both dates were meetings with no interpreter booked, where Ramona could not follow what was said. The form recorded her presence as a rating and her requests not at all. What changed the item was not a better performance at the review — it was the dated paper: the doorstep request, the meeting notes headed 'no interpreter present,' the page where a five-year-old was not used as an interpreter, all attached to a written correction.
- THE LAW UNDER THIS PATH: Counsel was Ramona's right, not a favor (42 Pa.C.S. § 6337) — and counsel is where the plan got read before it got signed. The record that exposed the scored meetings exists because agency records "shall be released upon request" (55 Pa. Code § 3130.44(d)), requested in writing with a dated copy kept; the packet arrived partly redacted, and § 3130.44(f) is the provision that limits what redactions may protect. A safety plan, this scenario teaches procedurally, is paper with consequences: reviewing it with counsel before signing turned an unread signature into terms she could actually perform — including the fix of a phone-call check-in she could never have completed.
- A NOTE ON WHAT THIS SCENARIO DID NOT RELY ON: Ramona's wins here are documentation moves — written requests, kept notebooks, a correction with exhibits — that stand on the verified law above. Specific disability-rights protections exist in this area, but they sit outside this scenario's verified set and were deliberately not relied on, in the game or in this guide's route. The paper route worked without them; a real case would put the question to a lawyer, who could use every protection the law actually provides.
- THE HONEST PART: This ending also turned on things no strategy controls: an interpreter who was skilled and patient, a lawyer who answered, a teacher who wrote a note, a reviewer willing to re-read an item next to its evidence. A different worker, a lost notebook, a reviewer who treated the form as final — the same mother, the same requests, a different ending. Outcomes in this system also turn on workers, judges, resources, and luck — never on whether Ramona was a good mother, which was never the question the form was asking.

## [end_removal] Signed, Not Read
*Day 45 — Thursday, April 2, 2026 (dayOffset 45)*

The shelter care hearing is held on Thursday, April 2, 2026 — within 72 hours of Nora's placement, as the law requires (42 Pa.C.S. § 6332; 23 Pa.C.S. § 6315(d)). An interpreter is present; Ms. Iwu is beside Ramona, her right to counsel honored in the room (42 Pa.C.S. § 6337). The hearing asks one narrow question: where Nora stays while the case is sorted out.

On the record in front of the court — a signed plan, breached on its unread terms; a cooperation item scored at meetings without an interpreter; an explanation that exists in today's transcript but not in February's file — placement continues for now, with visits, a new plan to be built, and a further hearing ahead where the facts themselves get decided. Nora's visual schedule, copied carefully, goes with her. So does the date of the next hearing, written down by her mother, in a notebook, in order.

**Ending.**

**Debrief:**
- WHAT THE FORM SAID (the hidden assessment, revealed): The hidden items were the same as on every path — the home as observed, the school's account, and cooperation as scored. On this path the decisive combination was a signature and a silence: a safety plan signed before it was reviewed with counsel (its Tuesday phone-call check-in unknown until it was missed), and a cooperation item that rated two un-interpreted meetings without ever recording the written interpreter requests that preceded them. Whatever was missing — the unsigned plan taken home, the written record request, or the correction with the notebook attached — the February file reached the review unanswered, and the review decided on the file it had.
- THE LAW UNDER THIS PATH: The safeguards that remain are real and they operated: a shelter care hearing within 72 hours of placement (42 Pa.C.S. § 6332; 23 Pa.C.S. § 6315(d)), counsel at Ramona's side (42 Pa.C.S. § 6337), visits, and a further hearing ahead. The road not taken was the paper road: agency records "shall be released upon request" (55 Pa. Code § 3130.44(d)) — the request that would have shown the 'uncooperative' entries while a correction could still answer them, with the notebook pages as exhibits. As with the winning ending, this scenario relied only on those verified provisions; specific disability-rights protections exist in this area but sit outside the verified set and were not relied on here either.
- WHAT REMAINS OPEN: Placement at a shelter care hearing is not a finding on the facts, and this case is not over: the notebook drawer, the dated clinic note, and the written requests can still be assembled with counsel for the hearings ahead, and a plan can still be rebuilt in language its signer can read. Late paper is weaker than early paper. It is not worthless, and the next hearing has not been written yet.
- THE HONEST PART: Read this ending carefully, because nobody in it needed to be a villain. A plan was pushed across a table with a pen uncapped; a form rated what it was built to rate; a five-year-old was almost the bridge. The signature was the mother's, and so was everything she did to protect her daughter — the system simply never gave her a way to read what she was signing, and then graded her on it. Outcomes here also turn on workers, judges, resources, and luck. This one turned on a signature taken before understanding was possible, and that is a failure of arrangement, not of a mother.
