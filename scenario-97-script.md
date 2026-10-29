# THE FIRST 90 DAYS — Scenario 97: “The Plan, Mailed Inside”

*Human-readable script. This document and `scenario-97.json` are generated from a single source and match node-for-node: same IDs, same order, same choices, same effects.*

**The family is fictional — a composite. No real person's story appears here.**

**Content note:** This scenario depicts an incarcerated father's dependency case worked by mail: a kinship safety arrangement, a case plan sent into a county prison, classes, video visits, and a review hearing. There is no graphic content. Players may skip any scene or use the quick exit at any time.

**How to read effects:** `cash −40` changes the player's cash. `FLAG: name` sets a flag the engine tracks. `HIDDEN + item` means the case file quietly records that item at this choice — the player does not see it when it happens. `REQUIRES FLAG: name` means the choice is only available if that flag was set earlier; `REQUIRES NO FLAG: name` means it is only available if that flag was never set. `NOTE:` is text shown to the player right after choosing.

Start date: Monday, January 5, 2026. Day offsets are days since the scenario's start date.

## [start] A Report About a House He Is Not In
*Day 0 — Monday, January 5, 2026 (dayOffset 0)*

Your name is Terrence Boone. You are in the county prison, serving a short sentence, with a release date in late March — close enough to count in weeks, far enough that your son's life cannot wait for it.

Your son Rowan is six. While you have been inside, he has been staying with a neighbor family down the street, in an arrangement made by phone and good intentions. Yesterday a report was called in about Rowan's living situation, and the agency has questions a phone arrangement cannot answer.

You learn all of this in a five-minute phone call, standing against a wall, with a line forming behind you. Everything in this story happens the way things happen from inside: on paper, by mail, through other people's hands.

**Choices:**
- Ask your mother, Dolores, to write down tonight that Rowan can live with her — her name, her address, and that she is saying yes → **grandmother_door**  _(FLAG: kinshipNamed ; HIDDEN + Kinship as recorded — grandmother named in writing on day one as Rowan's placement)_
  - NOTE (shown after choosing): A grandmother, in writing, on day one. Watch what that piece of paper is worth.
- Wait for the agency to sort out where Rowan goes → **grandmother_door**
  - NOTE (shown after choosing): Sorting out is what the agency calls it. From inside, it feels like weather.

## [grandmother_door] Ms. Kovich Meets Dolores
*Day 2 — Wednesday, January 7, 2026 (dayOffset 2)*

Ms. Kovich, the caseworker, goes first to the neighbor's house, then to Dolores's small rowhouse two streets over. Rowan's school is four blocks from Dolores's door. His spare clothes are already in her spare room, because grandmothers plan the way agencies wish families planned.

Dolores is a potential kinship care resource — family who can take Rowan as kin, in the category the law defines at 42 Pa.C.S. § 6302. Ms. Kovich looks at the room, the school run, the neighbor next door who can cover Dolores's Thursday shift at the diner. She fills in a scored assessment form as she goes. Dolores cannot see the items on it. Nobody offers to show her.

**Choices:**
- Dolores hands Ms. Kovich the written note and asks to be heard on her qualifications at any hearing → **safety_paper**  _(FLAG: kinshipStated ; HIDDEN + Home as observed — Rowan settled at grandmother's; school bag by the door, spare room made up)_
  - NOTE (shown after choosing): Under 42 Pa.C.S. § 6336.1, a potential kinship care resource may be heard on her qualifications. Dolores asks for that in the doorway, politely, in writing.
- Dolores explains it all out loud, warmly and at length → **safety_paper**
  - NOTE (shown after choosing): She means every word. The form keeps what was written down, and the note stayed in her hand.

## [safety_paper] The Arrangement, On Paper
*Day 4 — Friday, January 9, 2026 (dayOffset 4)*

Rowan will stay with Dolores under a safety arrangement while the case is sorted out — kinship, not a stranger placement. Ms. Kovich writes the arrangement at Dolores's kitchen table: Rowan sleeps at Dolores's, Dolores gets him to school, a check-in visit in two weeks, and Terrence — from inside — is part of the plan, not an afterthought to it.

It is two pages. It asks for Dolores's signature, and a copy will be mailed to Terrence at the prison.

**Choices:**
- Read every line together before Dolores signs, and circle the check-in date → **plan_mail**  _(FLAG: readPlan ; HIDDEN + Safety arrangement — read before signing; check-in date and video-visit term known)_
  - NOTE (shown after choosing): One line surprises them both — video visits, twice a week, that nobody had said out loud. Now it is a term, not a hope.
- Dolores signs so Rowan can get to bed at his usual time → **plan_mail**
  - NOTE (shown after choosing): A reasonable hour, a tired six-year-old. The unread lines will still be there in the morning, unread.

## [plan_mail] The Plan, Mailed Inside
*Day 7 — Monday, January 12, 2026 (dayOffset 7)*

The case plan arrives at the prison in a thick envelope, three days after Dolores signed it. Mail inside moves at its own speed: opened, inspected, delivered at evening count. Terrence reads it standing at his bunk, twice, the way you read anything that decides your family.

The plan's steps for him are real: a parenting class offered inside, a work detail, letters and video visits with Rowan, and a review hearing in March where his progress — as the file records it — will be the whole argument.

**Choices:**
- Write back the same day: acknowledge the plan, list its steps back in his own words, and ask for a complete copy for his folder → **missing_pages**  _(cash −4 ; FLAG: planAcknowledged ; HIDDEN + Case plan — acknowledged by the father in writing, steps listed back with dates)_
  - NOTE (shown after choosing): Postage and copies are not free inside. Neither is a plan acknowledged in writing — it becomes part of the record of what he was told and when.
- Put the envelope in his locker and start the class when it starts → **missing_pages**
  - NOTE (shown after choosing): The class will start either way. The difference is whether the file knows he knew.

## [missing_pages] Pages 4 Through 6, Missing
*Day 9 — Wednesday, January 14, 2026 (dayOffset 9)*

Dolores's copy of the plan has six pages. Terrence's copy has three. Somewhere between the agency's copier and the prison mail room, pages 4 through 6 — the pages with the class schedule and the video-visit instructions — went missing.

Nobody lost them on purpose. That is the point. Paper in this system is lost the way socks are lost: routinely, blamelessly, and always the pair you needed.

**Choices:**
- Ask, in writing through his attorney, for the missing pages before the step deadlines start → **salas_call**  _(FLAG: planComplete ; HIDDEN + Case plan — incomplete copy reported in writing; complete copy requested)_
  - NOTE (shown after choosing): A short letter, a date, a copy kept. The request itself tells the file the copy was incomplete — before anyone can say he ignored steps he never saw.
- Work from the three pages he has and ask around the block for the rest → **salas_call**
  - NOTE (shown after choosing): The block knows many things. The file will only ever know what was mailed.

## [salas_call] Mr. Salas, On the Clock
*Day 11 — Friday, January 16, 2026 (dayOffset 11)*

Mr. Salas is Terrence's attorney. Legal calls inside run on a clock neither of them controls, and he uses his minutes the way good lawyers do: steps, dates, and what to keep. You have the right to counsel in this process, and to appointed counsel if you cannot afford one (42 Pa.C.S. § 6337) — Mr. Salas intends to make that right worth the paper it is written on.

"Everything you do in there," he says, "happens twice: once in the room, and once in the file. Your whole case is making sure the second one happens."

**Choices:**
- Use the call to fix the steps and dates, and ask Mr. Salas to confirm them in a follow-up letter → **classes_inside**  _(FLAG: stepsWritten ; HIDDEN + Plan steps — confirmed to the father in counsel's follow-up letter)_
  - NOTE (shown after choosing): The letter arrives four days later. Steps, dates, and the March review — in writing, in his folder, where memory cannot be cross-examined.
- Memorize the steps on the call and save the letter-writing for later → **classes_inside**
  - NOTE (shown after choosing): His memory is good. The call was eleven minutes, three weeks ago, by the time anyone asks.

## [classes_inside] Classes Behind the Wall
*Day 14 — Monday, January 19, 2026 (dayOffset 14)*

The parenting class meets Tuesday and Thursday evenings in a room that is also the library. There is a waitlist, a sign-in sheet, and an instructor named Mr. Osei-Bonsu who takes attendance like it matters — because, he tells the class on the first night, someday a judge may ask whether it happened, and this sheet is the answer.

Terrence's name is called. He signs. The sheet goes into a binder that stays in the room. What leaves the room is whatever Terrence carries out of it.

**Choices:**
- Attend every session, and ask after each one for a copy of his sign-in or a dated note of attendance → **video_visit**  _(FLAG: classesEnrolled ; HIDDEN + Parenting class — attendance being documented session by session at the father's request)_
  - NOTE (shown after choosing): Small paper, asked for politely, twice a week. It looks like nothing. It is the whole case, in installments.
- Attend every session and trust the binder to speak for itself → **video_visit**
  - NOTE (shown after choosing): The binder will speak — to anyone who goes to that room and opens it. Files in other buildings cannot hear it.

## [video_visit] Video Visit, Fifteen Minutes
*Day 18 — Friday, January 23, 2026 (dayOffset 18)*

The video visit is fifteen minutes on a screen in a noisy room. Rowan holds up a drawing of Dolores's house with the spare room labeled, in six-year-old capitals, ROWAN'S ROOM. He asks when Terrence is coming home, and Terrence gives him the true answer in weeks, the way they practiced.

A staff member logs the visit in a book by the door: date, time, names. The log stays in that room too.

**Choices:**
- Ask Dolores to keep her own dated log of every video visit — date, length, one line about Rowan → **work_detail**  _(FLAG: visitLog ; HIDDEN + Video visits — dated log kept by grandmother from the first week)_
  - NOTE (shown after choosing): Dolores's kitchen-calendar log and the room's log will agree. Two records, kept in two places, are hard to lose.
- Let the visits just be visits — not everything has to become evidence → **work_detail**
  - NOTE (shown after choosing): Both things are true. Only one of them will be in the file in March.

## [work_detail] The Work Detail Log
*Day 21 — Monday, January 26, 2026 (dayOffset 21)*

Terrence's work detail is the kitchen crew: early shifts, a supervisor who writes initials in a box on a clipboard for every completed week. Six boxes are filled. The clipboard hangs by a door he passes twice a day.

Work inside counts toward the plan only if the plan's file ever hears about it. Files do not walk past clipboards.

**Choices:**
- Ask the supervisor for a dated note of the work record, and mail a copy out to Dolores → **certificates**  _(cash −4 ; FLAG: workRecorded ; HIDDEN + Work detail — dated record mailed out of the facility to grandmother)_
  - NOTE (shown after choosing): One page, six initials, a date. It leaves the building the only way anything does: in an envelope, with a name on it.
- Wait until release, when he can explain the work record in person → **certificates**
  - NOTE (shown after choosing): Release is in late March. The review is in early March. The order of those two dates is the whole problem.

## [certificates] Certificates in an Envelope
*Day 25 — Friday, January 30, 2026 (dayOffset 25)*

The parenting class ends the way it began, with paper: a completion certificate, Terrence's name spelled right, the instructor's signature, a date. A second certificate — the work program's — comes the same week. Two pages that say, in the system's own language, that a man in a cell did what the plan asked.

They are also just two pages, in a folder, in a locker, in a building the case file has never visited.

**Choices:**
- Mail copies of both certificates to Dolores and to Mr. Salas, with a dated cover letter — the originals stay in his folder → **bernice_visit**  _(cash −6 ; FLAG: certificatesFiled ; HIDDEN + Certificates — parenting class and work program copies mailed to grandmother and counsel with a dated cover letter)_
  - NOTE (shown after choosing): Copies travel; originals stay safe. The cover letter lists what is enclosed, so the file can never say the envelope was empty.
- Keep the certificates safe in his locker folder until he can hand them over himself → **bernice_visit**
  - NOTE (shown after choosing): Safe, and invisible. In this system those are the same address.

## [bernice_visit] Dolores Carries the Paper
*Day 32 — Friday, February 6, 2026 (dayOffset 32)*

Ms. Kovich's check-in visit at Dolores's house goes well: Rowan's room, Rowan's school folder, Rowan explaining the Thursday arrangement with the neighbor in the tone of a boy reciting a bus route. Ms. Kovich fills in the scored assessment form as she goes — home, supervision, support.

What she writes about Terrence depends on what is in front of her in this kitchen. Dolores has an envelope on the counter. Or she has a story about an envelope.

**Choices:**
- Dolores hands over the certificate copies at the door and asks Ms. Kovich to note the handover date → **record_learn**  _(FLAG: copiesHanded ; HIDDEN + Certificates — copies handed to the caseworker at the home visit; handover date noted)_
  - NOTE (shown after choosing): The worker takes them, and writes. A handover with a date is a fact. A handover described is a claim.
- Dolores tells her about the classes and the certificates, warmly and in detail → **record_learn**
  - NOTE (shown after choosing): Detail is not the problem. The problem is the difference between 'mother reports father completed class' and the certificate itself.

## [record_learn] A Line in a Letter
*Day 35 — Monday, February 9, 2026 (dayOffset 35)*

Mr. Salas's letter this week has a line Terrence reads three times: you can ask for the agency's own record — the file, the plan as the agency wrote it, the scored form's items — and under the regulation the material "shall be released upon request." (55 Pa. Code § 3130.44(d))

Almost nobody inside ever hears that sentence. Terrence is holding it in a letter, with a drafted request clipped behind it, needing only a signature.

**Choices:**
- Sign the written record request and send it this week, through Mr. Salas, keeping a dated copy → **record_arrives**  _(cash −4 ; FLAG: recordsRequested ; HIDDEN + Agency record — requested in writing under § 3130.44(d); dated copy kept)_
  - NOTE (shown after choosing): A signature, a date, a copy in the folder. The cheapest power in this whole system, exercised from a cell.
- Ask Ms. Kovich on the next call to just tell him what the file says → **record_arrives**
  - NOTE (shown after choosing): She will summarize, kindly and briefly. A summary is not a record, and it will not be in his folder in March.

## [record_arrives] What the File Says: Nothing
*Day 42 — Monday, February 16, 2026 (dayOffset 42)*

The packet arrives the way the plan did: thick envelope, evening count. Some lines are blacked out. But the part Terrence turns to first is there — the progress section, the scored assessment form's items, the plan's own checkboxes.

Parenting class: no progress noted. Work program: no record. Video visits: 'sporadic contact.' The file does not say he failed. It says something quieter and worse: it says nothing happened. Every sheet he signed is in a binder in a library. Every certificate is — he hopes — in an envelope Dolores handed over. The file was written by people who never saw any of it.

**Choices:**
- Read the packet with Mr. Salas on the next call, line by line, and mark every empty box → **correction_draft**
  - NOTE (shown after choosing): Eleven minutes, four empty boxes. Each one has a piece of paper somewhere that answers it. That is now a list, not a fear.

## [correction_draft] The Correction, In Pencil First
*Day 45 — Thursday, February 19, 2026 (dayOffset 45)*

The correction is one page. Mr. Salas drafts it; Terrence checks every date against Dolores's kitchen-calendar log and his own folder, in pencil, the way you check anything that will outlive your memory of it.

It does not argue. It lists: the class, with dates and the certificate attached; the work record; the video visits, with Dolores's log; the missing plan pages, reported in writing in January. Facts with dates, in the father's words, asking to be filed next to the form that said nothing happened.

**Choices:**
- Build the full correction — dates first, certificates and the visit log attached, copies for the agency, Dolores, and counsel → **review_prep**  _(cash −6 ; FLAG: correctionFiled ; HIDDEN + Correction — dated progress correction with certificates and visit log, prepared for filing)_
  - NOTE (shown after choosing): It costs copies and postage. It buys the only thing the review will read: a record that answers the record.
- Send a short letter saying he disagrees with the file and has been trying hard → **review_prep**
  - NOTE (shown after choosing): He has been. Trying hard, without dates attached, reads in a file exactly like the empty boxes it answers.

## [review_prep] Three Copies
*Day 49 — Monday, February 23, 2026 (dayOffset 49)*

Dolores makes three copies at the library: one for the agency, one for Mr. Salas, one for her own folder, which now has sections and tabs, because Dolores has become the kind of grandmother this system produces — the kind with a filing system.

The review hearing is in a week. Paper filed before a hearing is paper the other side has read. Paper handed up at a hearing is paper everyone reads for the first time, at speed, while a judge waits.

**Choices:**
- File the correction this week, before the review, and keep the stamped copy → **kinship_heard**  _(FLAG: filedBeforeReview)_
  - NOTE (shown after choosing): Stamped, dated, in the file before anyone sits down. The review will now be about a record, not a rumor of one.
- Bring the correction to the review and hand it up there → **kinship_heard**
  - NOTE (shown after choosing): It will still be true. It will be true at the worst possible moment to introduce truth.

## [kinship_heard] Dolores Will Be Heard
*Day 52 — Thursday, February 26, 2026 (dayOffset 52)*

Mr. Salas confirms the last piece: at the review, Dolores — as Rowan's potential kinship care resource, the category defined at 42 Pa.C.S. § 6302 — may be heard on her qualifications to provide kinship care (42 Pa.C.S. § 6336.1). Not on Terrence's case. On the narrow, decisive question: can this woman take this child, and keep taking him.

Dolores writes her page: the room, the school run, the Thursday neighbor, the diner schedule with her supervisor's initials beside the shift she traded. Qualifications, in order, with paper behind them.

**Choices:**
- Dolores prepares her one page — qualifications in order, each one backed by a document she can hand over → **review**  _(FLAG: kinshipHeard ; HIDDEN + Kinship — grandmother prepared to be heard on her qualifications, with documents)_
  - NOTE (shown after choosing): A page she can defend line by line. Narrow rights, precisely used, are how kin move outcomes.
- Dolores plans to speak from the heart about what Rowan means to her → **review**
  - NOTE (shown after choosing): The heart is real, and it is not the subject the law seats her to speak on. The room will hear love and learn nothing it can use.

## [review] The Review Hearing
*Day 56 — Monday, March 2, 2026 (dayOffset 56)*

The review courtroom is small. Rowan is at school. Dolores is in the second row with her folder. Terrence is on the phone line from the prison, a voice on a speaker, which is how fathers in his position attend their children's hearings — present, and one wall away from present.

The agency's report recommends the case escalate: Rowan's placement to be formalized and Terrence's plan marked as showing no progress, on the strength of a file that says nothing happened. Mr. Salas rises. What he can hand up depends entirely on what travelled, in envelopes, in the weeks before today.

**Choices:**
- Hand up the correction — the requested record answered with certificates, the work note, and Dolores's log — and have Dolores heard on her qualifications → **end_win**  _(REQUIRES FLAG: recordsRequested ; REQUIRES FLAG: certificatesFiled ; REQUIRES FLAG: correctionFiled)_
  - NOTE (shown after choosing): Dates, certificates, a log, a grandmother with a page. The file that said nothing is answered by the paper that says everything.
- Terrence describes the classes himself, over the phone line, as best he can → **end_escalation**
  - NOTE (shown after choosing): It is all true. It is also, in the only form this room can keep, a voice on a speaker saying trust me.

## [end_win] The Credit on Paper
*Day 63 — Monday, March 9, 2026 (dayOffset 63)*

The judge reads the correction the way judges read paper that arrives before the hearing: slowly, and twice. The agency does not dispute the certificates. Its report said no progress because its file said no progress — and its file, everyone in the room now understands, was simply the last to know.

The order keeps Rowan with Dolores. It corrects Terrence's progress on the record — class completed, work documented, visits logged — and it writes the next step into the plan in so many words: on Terrence's release, weeks from now, a return-home plan with Dolores's support written in, reviewed at a date the order names.

Terrence hears the order over a phone line, standing against a wall. He is still inside when this story ends. But his son is two streets from his school, in a room with his name on a drawing, and the file finally says what he did.

**Ending.**

**Debrief:**
- WHAT THE FORM SAID (the hidden assessment, revealed): The items moving underneath this story were kinship as recorded on day one, the home as observed at Dolores's (Rowan settled, the spare room made up, the school bag by the door), the safety arrangement as read or unread before signing, and — decisively — the father's progress as recorded. For most of the story that item read 'no progress noted,' not because nothing happened, but because everything that happened happened in rooms the file never visited: a library classroom, a kitchen crew, a video-visit log book. Certificates that travelled moved the item. Certificates that stayed in a locker did not.
- THE LAW UNDER THIS PATH: Dolores's place in the case is the kinship framework — a potential kinship care resource as defined at 42 Pa.C.S. § 6302, who may be heard on her qualifications at a hearing under 42 Pa.C.S. § 6336.1 (as amended by Act 48 of 2023). Terrence's counsel is his right, not a favor (42 Pa.C.S. § 6337). The record that exposed the empty progress boxes exists because agency records "shall be released upon request" (55 Pa. Code § 3130.44(d)) — requested in writing, from inside, through counsel. The review itself is the court's placement and plan review (42 Pa.C.S. § 6351): it decided on the record in front of it, which is why what was filed before it mattered more than what was said at it.
- WHY THIS IS ONLY A PARTIAL WIN: Terrence does not come home in this ending, and Rowan does not either — he stays with Dolores, which was always the arrangement's strength and its limit. What changed is the plan's next step: return home is written into it, dated, with his progress credited on the record instead of erased from it. Release is weeks away; the step is paper, not a door opening.
- THE HONEST PART: This ending turned on envelopes — on a mail room that delivered, a grandmother who could carry paper two streets and keep a calendar log, an instructor who took attendance like it mattered, and a lawyer who answered letters. A lost envelope, a transferred housing unit, a different judge reading the same correction — the same father, the same work, a different ending. Outcomes in this system also turn on workers, judges, resources, and luck. This one turned on whether the work became paper in time, and that is not a verdict on Terrence as a parent — it never was.

## [end_escalation] The File Nobody Corrected
*Day 63 — Monday, March 9, 2026 (dayOffset 63)*

The agency's report is the only complete document in the room. It is not cruel and it is not invented: it says, accurately, what its file says — no progress noted, contact sporadic, plan unworked. Over the phone line, Terrence describes the classes. The judge listens kindly and asks the question this system always asks: is any of that in the file?

The order formalizes Rowan's placement and escalates Terrence's plan: more steps, a new review after his release, and a progress record that starts, officially, from zero — dated from today, as if the library classroom, the kitchen crew, and fifteen-minute visits had happened to somebody else.

Dolores keeps Rowan — the kinship arrangement holds, and that is not nothing; Rowan sleeps in the room with his name on the drawing. But the return-home step Terrence worked for is not in the plan. It will have to be built again, from release, on a clock that has been running the whole time.

**Ending.**

**Debrief:**
- WHAT THE FORM SAID (the hidden assessment, revealed): The hidden items were the same as on every path — kinship recorded or merely spoken, the home as observed at Dolores's, the arrangement as read or unread — and, decisively, the father's progress as recorded. On this path that item was never answered: whatever was missing — the written record request, the travelled certificates, or the dated correction — the progress boxes reached the review exactly as the packet showed them in February: 'no progress noted.' The work was real. The file is what reviews read.
- THE LAW UNDER THIS PATH: The kinship framework still held — Dolores, a potential kinship care resource (42 Pa.C.S. § 6302), kept Rowan and may be heard on her qualifications at hearings (42 Pa.C.S. § 6336.1). Counsel was Terrence's right (42 Pa.C.S. § 6337), and the review was the court's placement and plan review (42 Pa.C.S. § 6351), decided on the record in front of it. The road not taken was the record request: agency records "shall be released upon request" (55 Pa. Code § 3130.44(d)). Without seeing the file's empty boxes in February, nobody could answer them in March — the correction that wins the other ending begins with that packet.
- WHAT REMAINS OPEN: Escalation is not termination, and a formalized placement is not a finding about a father's worth. The steps can be worked again from release, this time with the paper carried as it is made; Dolores's kinship placement and her right to be heard remain in the case; and the record request can still be sent — late is worse than early, and better than never.
- THE HONEST PART: Nothing in this ending says Terrence did not do the work. It says the system he had to do it in grades the file, not the effort — and that a mail delay, a missing three pages, a supervisor's clipboard, or a judge's crowded morning can outweigh a semester of sign-in sheets no one carried. Outcomes here also turn on workers, judges, resources, and luck. The file said nothing happened because nobody made the file say otherwise, and that is a failure of paper, not of a parent.
