# THE FIRST 90 DAYS — Scenario 67: “The Room Where It Happens”

*Human-readable script. This document and `scenario-67.json` are generated from a single source and match node-for-node: same IDs, same order, same choices, same effects.*

**The family is fictional — a composite. No real person's story appears here.**

**Content note:** This scenario depicts a removal, a shelter care hearing, and an adjudication hearing. There is no graphic content. Players may skip any scene or use the quick exit at any time.

**How to read effects:** `cash −40` changes the player's cash. `FLAG: name` sets a flag the engine tracks. `HIDDEN + item` means the case file quietly records that item at this choice — the player does not see it when it happens. `REQUIRES FLAG: name` means the choice is only available if that flag was set earlier; `REQUIRES NO FLAG: name` means it is only available if that flag was never set. `NOTE:` is text shown to the player right after choosing.

Start date: Tuesday, October 20, 2026. Day offsets are days since the scenario's start date.

## [start] The Evening It Happens
*Day 0 — Tuesday, October 20, 2026 (dayOffset 0)*

Your name is Colette Voss. You work the overnight shift at a warehouse, and your son Amos is nine — old enough to make toast, young enough that the law, and you, agree he should not be alone at night.

At 6 p.m. your sitter quit by text. Your shift started at seven. Your mother, Amos's grandmother, did not answer either call. You made the choice you have been re-living ever since — and then, on Thursday, with the replacement sitter a no-show, you made it again, for forty minutes, and your neighbor Mrs. Quist, who was worried and not wrong to be, called the agency.

Tonight there is a knock. Ms. Alvarado, from the county agency, is kind and immovable: Amos will be taken into care tonight while the court looks at this. A car is coming. You have perhaps ten minutes, and what you do with them turns out to matter more than almost anything you say later.

**Choices:**
- Use the ten minutes for paper: hand her the printed quit text and write down your mother's name and number, your work roster, and who was with Amos on Tuesday → **lawyer_call**  _(FLAG: removed ; FLAG: nightOnePaper ; HIDDEN + File — sitter's resignation text, printed and handed to the worker on night one)_
  - NOTE (shown after choosing): She puts it in the file, in front of you. What is in the file on night one is in the file at every hearing after.
- Use the ten minutes only for Amos — his bag, his bear, a note in his pocket — and let the paperwork wait until you can think → **lawyer_call**  _(FLAG: removed)_
  - NOTE (shown after choosing): Understandable, and human. The bear goes with him. The facts about Tuesday stay in your head, where no judge can read them.

## [lawyer_call] The Morning After
*Day 1 — Wednesday, October 21, 2026 (dayOffset 1)*

You barely sleep. The paper Ms. Alvarado left says you have the right to a lawyer, and to one appointed by the court if you cannot afford one. (42 Pa.C.S. § 6337) By nine o'clock you have a name: Mr. Beaumont, appointed counsel, who will sit beside you at the shelter care hearing.

That hearing is Friday — within 72 hours of a child being taken into care, the law requires it. (42 Pa.C.S. § 6332; 23 Pa.C.S. § 6315(d)) Mr. Beaumont tells you the thing nobody said last night: "At the big hearing, you do not have to prove you are a good mother. The agency has to prove its petition — by clear and convincing evidence. That is their job, not yours." (42 Pa.C.S. § 6341(c))

"Friday is narrower," he says. "Friday only decides where Amos stays while we get there. Bring me anything that is paper."

**Choices:**
- Write down his three questions — who was with Amos each night, what is arranged now, what is on paper — and start a folder tonight → **shelter_room**
  - NOTE (shown after choosing): A folder with three sections. It looks small. It is the beginning of your side of the record.
- Spend the day calling family instead — the folder can wait until after Friday → **shelter_room**
  - NOTE (shown after choosing): The calls matter. So does the order you do things in, and Friday is in two days.

## [shelter_room] Who Is in the Room
*Day 3 — Friday, October 23, 2026 (dayOffset 3)*

The courtroom is smaller than you expected, and fuller. One by one, Mr. Beaumont names them for you, the way you asked: the judge, who will decide; the agency's lawyer, who will present the petition; Ms. Alvarado, the caseworker; a lawyer appointed for Amos, to speak for Amos's interests; and Mr. Beaumont, yours — counsel at this hearing is part of the right, not a favor. (42 Pa.C.S. § 6332(a); § 6337)

Mrs. Quist is not here. She called because she found a nine-year-old alone at dusk and it frightened her; Mr. Beaumont says that plainly, and it helps to hear it said that way — she is a witness, not a villain.

The judge explains the narrow question: not whether the petition is true — that is for the adjudication hearing — but where Amos stays until then.

**Choices:**
- Listen to each person in turn and let Mr. Beaumont do the talking for your side → **shelter_folder**
  - NOTE (shown after choosing): Your job in this room, he told you, is smaller than you feared: answer when the judge asks you, and hand up paper when there is paper.
- Ask Mr. Beaumont, before it starts, what each person in the room can and cannot decide today → **shelter_folder**
  - NOTE (shown after choosing): Nobody in this room can end the case today. Knowing that keeps today in proportion.

## [shelter_folder] The Folder, or the Empty Hands
*Day 3 — Friday, October 23, 2026 (dayOffset 3)*

The agency's lawyer describes the two evenings and asks that Amos remain in care until adjudication. Then the judge looks toward your table.

What Mr. Beaumont can hand up depends entirely on what you brought through the courthouse door this morning: the work roster, the sitter's quit text, and your mother's short letter saying she was with Amos on Tuesday and can be backup care any night she is asked in advance — or nothing but your memory of all three.

**Choices:**
- You brought the folder — and you ask Mr. Beaumont to name your mother on the record as an approved backup caregiver → **shelter_question**  _(FLAG: folderReady ; HIDDEN + Transcript — grandmother named at shelter care as an approved backup caregiver)_
  - NOTE (shown after choosing): The judge reads the letter. Grandmother's name is now in the transcript, where later hearings can find it — not just in a caseworker's notes.
- You came empty-handed — the roster is on the kitchen counter and the letter is still a phone call you meant to make → **shelter_question**
  - NOTE (shown after choosing): Mr. Beaumont does his best with words. Words from a lawyer are argument. Paper would have been evidence.

## [shelter_question] The Judge Asks You Directly
*Day 3 — Friday, October 23, 2026 (dayOffset 3)*

The judge turns to you — not to your lawyer, to you. "Ms. Voss. Who was with Amos on Tuesday?"

The room is very quiet. Ms. Alvarado is three chairs away, and there are things in her summary you believe are wrong, and she is right there, and the judge is waiting, and everything you feel about the last three days arrives in your chest at the same moment as the question.

**Choices:**
- Answer plainly and briefly: "My mother was with him Tuesday, Your Honor. Thursday he was alone for forty minutes. That was my decision, and it was wrong." Then stop → **shelter_ruling**  _(FLAG: plainAnswers)_
  - NOTE (shown after choosing): Short, specific, and finished. The judge writes something down — judges write down answers they can use.
- Turn and answer Ms. Alvarado instead — correct her summary, point by point, from your seat → **shelter_ruling**  _(FLAG: arguedFromSeat)_
  - NOTE (shown after choosing): Every correction may be true. Delivered that way, in that room, they land as argument, not testimony — and judges tend to discount everything a witness says after it.

## [shelter_ruling] Where He Stays for Now
*Day 3 — Friday, October 23, 2026 (dayOffset 3)*

The judge is careful about what today is: a shelter care decision, not a ruling on the petition. Amos will remain in care until the adjudication hearing, set for Thursday, November 5 — close enough that Mr. Beaumont calls it "a runway, not a sentence." Your mother may be assessed as backup care. A visit is set for Monday.

"Between now and November 5," Mr. Beaumont says in the hallway, "the case is mostly built out of paper. The agency is writing theirs. The question is whether you are writing yours."

**Choices:**
- Get the visit time, the assessment contact, and the November 5 date in writing before you leave the building → **first_visit**
  - NOTE (shown after choosing): Three dates, on paper, in your folder. The hallway version of this case is already over; the paper version is just starting.
- Go home and sleep first — you have been awake since Tuesday, in every way that counts → **first_visit**
  - NOTE (shown after choosing): Sleep is not a strategy failure. The dates will still be given to you — by the agency, in their letter, on their schedule.

## [first_visit] One Hour on Monday
*Day 6 — Monday, October 26, 2026 (dayOffset 6)*

The visit is in a room with a couch, a board game with half its pieces, and a clock. Amos tells you about the foster home's cat, carefully, watching your face. He asks when he is coming home and you give him the honest shape of it: a judge will decide after a hearing on November 5, and grown-ups are working on the plan for every night after that.

A worker sits in the corner, kind and quiet, writing. What she writes is a record too — the visit log is one of the few parts of the file that is about an hour like this one.

**Choices:**
- Be early, bring his drawing folder from home, and let the hour be an hour → **week_between**
  - NOTE (shown after choosing): The log will say what it saw: a boy who settled, a mother who came. Ordinary, documented.
- Use the hour to rehearse Amos on what to tell the judge → **grandmother_call**
  - NOTE (shown after choosing): He goes quiet in a way that tells you, immediately, that this was the wrong use of an hour — and the worker's pen noticed the quiet too.

## [grandmother_call] Your Mother Answers
*Day 6 — Monday, October 26, 2026 (dayOffset 6)*

That evening your mother calls back. She has been carrying the week since it happened, and she says it plainly: Amos was with her on the Tuesday in the petition, she will say so anywhere, and she will be assessed as backup care whenever the agency calls.

Mr. Beaumont's advice about your mother is his advice about everything: her willingness matters, and it matters most in a form the file can hold — a short letter, her name spoken on a record, an assessment with a date on it. Love that leaves paper is what a courtroom can use.

**Choices:**
- Ask her to write the short letter tonight — Tuesday, the backup offer, her phone number — and bring it to you tomorrow → **week_between**
  - NOTE (shown after choosing): One page, in her handwriting. It joins the folder next to the roster, where pages reinforce each other.
- Thank her and let her willingness stand as a phone call for now → **week_between**
  - NOTE (shown after choosing): She means it, completely. The file, which was not on the call, will have to take your word for what she said.

## [week_between] The Week Between: Ask for the File
*Day 6 — Monday, October 26, 2026 (dayOffset 6)*

Back home, Mr. Beaumont calls with the week's two jobs. Job one is a sitter, in writing. Job two surprises you: "Request the agency's record. In writing. The regulation says the record shall be released upon request — those words, 'shall be released upon request,' are the whole sentence." (55 Pa. Code § 3130.44(d))

"What's in it that I don't know?" you ask. "That's the point of asking," he says. "Somewhere in their file is the roster they are relying on. I would like us to see it before a judge does."

**Choices:**
- Send the written request for the agency record today, and keep a dated copy → **new_sitter**  _(cash −5 ; FLAG: recordsRequested)_
  - NOTE (shown after choosing): Five dollars of copies and postage. What it buys is the chance to read the file's version of your own work schedule before November 5.
- Wait and see the record at the hearing — Mr. Beaumont can handle whatever is in it, in the room → **new_sitter**
  - NOTE (shown after choosing): He can handle a lot in a room. He cannot read, in the room, a discrepancy nobody has had a week to find.

## [new_sitter] A Plan That Is Actually Arranged
*Day 10 — Friday, October 30, 2026 (dayOffset 10)*

Job one comes due. A coworker's sister, Ms. Ferreira, watches two other warehouse families' children and has a Thursday-night opening and some Tuesdays. She is willing — for a deposit, and she will put it in a short written commitment with her name, the nights, and her phone number.

The other option costs nothing tonight: tell Mr. Beaumont — and later, the judge — that coverage is "lined up," based on a conversation with a neighbor who said "probably, most weeks."

**Choices:**
- Pay the deposit and get Ms. Ferreira's commitment in writing, with your mother as named backup → **record_review**  _(cash −40 ; FLAG: sitterCommitted)_
  - NOTE (shown after choosing): A name, nights, a phone number, a signature. When a judge asks 'who, exactly?' this is what an answer looks like.
- Keep the money and describe the neighbor's 'probably' as the plan — it will surely firm up by Thursday → **record_review**  _(FLAG: planPromised)_
  - NOTE (shown after choosing): It sounds fine in your kitchen. Plans described to judges get exactly one question — 'who, exactly?' — and 'probably' does not survive it.

## [record_review] The Roster in Their File
*Day 10 — Friday, October 30, 2026 (dayOffset 10)*

If your written request went out on Monday, a thick packet is on Mr. Beaumont's desk by Friday — and on page after page, there it is: the roster the agency copied into its file shows you on shift on Tuesday. Your real roster, the one in your folder, shows the swap you made that week: you were off Tuesday, and Amos was at your mother's.

If the request never went out, this hour is thinner: Mr. Beaumont works from the summary the agency provided, the Tuesday roster in their file stays their roster, and nobody on your side of the table ever sees the discrepancy at all.

"This is why we ask," he says. "A fact not proven is a fact the court cannot use — but somebody has to give the court the means to see it wasn't proven." (42 Pa.C.S. § 6341(c))

**Choices:**
- Go through the packet with him line by line and mark every place the file's version differs from your paper → **prep_stages**
  - NOTE (shown after choosing): Two rosters, side by side, with the swap sheet clipped to yours. That paperclip is about to do serious work.
- Skim the summary pages and spend the hour on how you will come across instead → **prep_stages**
  - NOTE (shown after choosing): How you come across matters. What the agency can and cannot prove matters more, and it is decided on pages like these.

## [prep_stages] Two Stages, Two Different Tests
*Day 13 — Monday, November 2, 2026 (dayOffset 13)*

Mr. Beaumont draws the hearing as two rooms. "Room one is adjudication: was it proven? The agency must prove Amos dependent by clear and convincing evidence, or the petition is dismissed and he is discharged — those are the only two doors out of room one." (42 Pa.C.S. § 6341(c); § 6341(a))

"Room two is disposition: what happens now — and we only enter it if room one goes against us. Different rules live there. At disposition, the court may receive all evidence helpful in deciding, including written reports, even things that wouldn't be competent in room one — and your side may examine and challenge those reports and cross-examine the people who wrote them." (42 Pa.C.S. § 6341(d)(1); § 6341(d)(2))

"Most parents prepare for one blur of a hearing," he says. "We are going to prepare for two rooms."

**Choices:**
- Repeat it back to him until you can say it cold: 'Stage one, they prove it. Stage two, only if stage one is lost.' → **prep_findings**
  - NOTE (shown after choosing): It sounds simple. In the room, with your heart going, simple is what survives.
- Ask him to just tell you what to say when your turn comes → **prep_findings**
  - NOTE (shown after choosing): He will. But a parent who understands the two rooms hears the hearing differently — and answers the judge's actual question, not the feared one.

## [prep_findings] What the Judge Must Say Out Loud
*Day 13 — Monday, November 2, 2026 (dayOffset 13)*

"One more piece of room two," Mr. Beaumont says, "because you should hear it here first, not there. Before any disposition that keeps Amos out of your home, the court must put findings on the record: that staying home would be contrary to his welfare, and whether reasonable efforts were made to prevent the removal. On the record — spoken, in the transcript, where they can be reviewed." (42 Pa.C.S. § 6351(b))

Then the rehearsal, and it is gentle and exact: "If the judge asks who is with Amos on your shift nights — answer only what is actually arranged. A plan you have only promised collapses on one question. A plan on paper doesn't have to be defended. It just has to be read."

**Choices:**
- Rehearse the answer with only the arranged facts: Ms. Ferreira's nights, your mother's backup, the roster as it actually was → **adjudication_arrival**
  - NOTE (shown after choosing): Nothing in the answer needs the word 'probably.' That is what arranged means.
- Ask whether a little confidence would sound better than a short answer → **adjudication_arrival**
  - NOTE (shown after choosing): "A short true answer," he says, "is the most confident sound in a courtroom. The second most confident sound is silence after it."

## [adjudication_arrival] The Room Where It Happens
*Day 16 — Thursday, November 5, 2026 (dayOffset 16)*

Same small room. Same five chairs filled the same way. What is different is the folder on your table — and whether there is one.

The judge opens the adjudication hearing and states the burden out loud, for the record: the agency must prove, by clear and convincing evidence, that Amos is a dependent child. (42 Pa.C.S. § 6341(c)) "Ms. Voss does not have to prove anything," the judge says. "The agency will present its case."

**Choices:**
- Take your seat beside Mr. Beaumont, folder in front of you, and let the agency go first — it is their burden to carry → **adjudication_witness**  _(cash −10)_
  - NOTE (shown after choosing): Bus fare and parking, $10. Sitting still while the other side goes first is not passivity. It is the structure of the hearing, working.
- Ask the judge, before anything starts, to hear your side first so the record is fair → **adjudication_witness**
  - NOTE (shown after choosing): The judge declines, politely. Order is not fairness's enemy here — the burden, and who carries it, is the fairness.

## [adjudication_witness] The Only Witness
*Day 16 — Thursday, November 5, 2026 (dayOffset 16)*

The agency calls one witness: Ms. Alvarado. She is careful and honest about the limits of what she knows — she was not there on either evening; she is testifying from the file. Under Mr. Beaumont's questions, the file's Tuesday roster meets your folder's Tuesday roster, and they are not the same document.

Then Mrs. Quist. She says what she saw, which is Thursday: a boy alone at dusk, her knocking, her worry. Tested, gently, she is clear that she saw nothing on Tuesday — she was at her sister's. She looks at you once, not unkindly. She was a neighbor who found a child alone. The hearing can hold both that truth and the question of what the agency has proven.

And Thursday itself: forty minutes, a sitter who did not show, a decision you have already owned out loud in this room. The judge is watching what the agency does with one proven lapse and a care plan — and what it cannot do with Tuesday.

**Choices:**
- Let the cross-examination stand as it is — the agency's own witness has marked the edge of the agency's proof → **adjudication_offer**
  - NOTE (shown after choosing): Nothing you could add from your seat is stronger than what their witness just conceded on the record.
- Whisper urgently at Mr. Beaumont to make her admit the whole file is wrong → **adjudication_offer**
  - NOTE (shown after choosing): He shakes his head once. The file is not 'wrong' — it is short of proof on one date, and short is enough, if the offer comes next.

## [adjudication_offer] The Offer
*Day 16 — Thursday, November 5, 2026 (dayOffset 16)*

Your side's turn is short, the way Mr. Beaumont planned it: not a speech, an offer. The roster — the real one, with the swap sheet — and the new sitter's written commitment, handed up, marked, and placed in front of the judge, where evidence lives.

An arrangement that exists only in your testimony can be believed or not. An arrangement handed up as an exhibit has to be dealt with.

**Choices:**
- OFFER the roster and the new sitter's written commitment as an exhibit → **adjudication_verdict**  _(HIDDEN + Exhibit — work roster and new sitter's written commitment, offered at adjudication ; REQUIRES FLAG: sitterCommitted)_
  - NOTE (shown after choosing): The clerk marks it. The judge reads the nights, the name, the phone number — the plan, as paper.
- Rest on the cross-examination alone and offer nothing → **adjudication_verdict**
  - NOTE (shown after choosing): A real strategy — burdens matter. But a judge deciding whether a lapse was a pattern can only weigh the plan she can see.

## [adjudication_verdict] Clear and Convincing, or Not
*Day 16 — Thursday, November 5, 2026 (dayOffset 16)*

The judge takes a recess that lasts eleven minutes and feels geological. Mr. Beaumont does not fill it with talk. "Whatever happens," he says, "happens on the record we made. That part is done, and it was done right or it wasn't — we are about to find out which."

The judge returns. The ruling will follow the proof: what was proven about Tuesday, what was proven about Thursday, and whether the two together carry the agency's burden — or whether what stands in the room is one lapse, owned, with a plan now in place on paper.

**Choices:**
- Mr. Beaumont asks the court to dismiss: Tuesday was not proven, and one owned lapse with an arranged plan does not carry the burden → **end_win**  _(HIDDEN + Order — petition dismissed; the two unproven dates are not findings ; REQUIRES FLAG: folderReady ; REQUIRES FLAG: plainAnswers ; REQUIRES FLAG: recordsRequested)_
  - NOTE (shown after choosing): This argument exists because the folder was brought, the answers were plain, and the record was requested — the discrepancy was seen before this room, not discovered in it.
- Mr. Beaumont argues the proven Thursday lapse alone should not keep Amos placed, given the plan now arranged → **disposition_hearing**  _(REQUIRES FLAG: sitterCommitted)_
  - NOTE (shown after choosing): A narrower argument, for a record with a gap in it — it asks the court to be lenient where the full argument would have asked it to find the burden unmet.
- Wait for the court's ruling on the record exactly as it stands → **disposition_hearing**
  - NOTE (shown after choosing): The record as it stands is the record as you built it — or didn't. The judge rules from it either way.

## [disposition_hearing] Room Two: The Findings
*Day 16 — Thursday, November 5, 2026 (dayOffset 16)*

The adjudication goes the other way. On the record as it stood — a folder not brought, a file never requested and read, an answer that became an argument, a plan that was a promise — the judge credits the agency's account, and Amos is found dependent. The hearing moves, the same afternoon, into room two: disposition, where the court may receive all evidence helpful in deciding what happens now. (42 Pa.C.S. § 6341(d)(1))

Hear what Mr. Beaumont made you ready to hear. Before this disposition, the judge states the findings on the record: that continuation in your home would be contrary to Amos's welfare at this time, and the court's view of whether reasonable efforts were made to prevent the removal. (42 Pa.C.S. § 6351(b)) The words are formal and they sting, and they are also now written down, reviewable, and dated — which matters for everything that comes next.

Amos will remain placed for now. The judge sets the case on its next clock, out loud, so you hear it from the bench and not from a rumor.

**Choices:**
- Write down, before you leave, the next date the judge names — and what has to be different by then → **end_placed**
  - NOTE (shown after choosing): The case is not over. It has a clock now, and clocks, unlike hearings, can be prepared for the whole way along.

## [end_win] The Petition Is Dismissed
*Day 16 — Thursday, November 5, 2026 (dayOffset 16)*

The ruling takes four minutes. Tuesday: not proven — the agency's only witness was not there, its file's roster was not your roster, and the neighbor's honest account covers Thursday only. Thursday: a single lapse, owned by the parent in plain words in this room, with care now arranged on paper. Together, the judge finds, they do not prove dependency by clear and convincing evidence.

The petition is dismissed. Amos is discharged to you. (42 Pa.C.S. § 6341(a); § 6341(c)) There is no room two today, because room one did its work.

He sleeps in his own bed that night, with the bear. On the kitchen counter is a folder — a quit text, a roster, a letter, a sitter's signed page — that turned out to be the most important furniture in the house.

**Ending.**

**Debrief:**
- WHAT THE FILE SAID — The pieces that decided this were in the file because you put them there: the sitter's resignation text, handed to the worker on night one; your mother's name, spoken on the record at shelter care as an approved backup caregiver; the roster and the new sitter's written commitment, offered as an exhibit at adjudication. And the record you requested in writing showed you the agency's own file carried the wrong roster for Tuesday — a discrepancy that is invisible to a parent who never asks to see the file. The file rated what it could see; you made sure it could see the truth.
- THE LAW — At adjudication the agency, not the parent, must prove dependency by clear and convincing evidence (42 Pa.C.S. § 6341(c)); a fact not proven is a fact the court cannot use. Where the proof fails, the petition is dismissed and the child discharged (42 Pa.C.S. § 6341(a)). The shelter care hearing came within 72 hours (42 Pa.C.S. § 6332; 23 Pa.C.S. § 6315(d)), with appointed counsel (42 Pa.C.S. § 6337), and the agency record was yours on written request (55 Pa. Code § 3130.44(d)).
- THE HONEST PART — This ending turned on a grandmother who answered, a sitter who would sign her name, a worker who testified honestly about what she had not seen, and a judge who held the burden where the law puts it. A different worker, a sterner judge, a roster swap never documented — the same mother, the same love, a different ending. Outcomes in this system turn on workers, judges, resources, and luck. This one is not a verdict that you were a perfect parent; Thursday was real, and you owned it. It is a verdict that the agency did not prove its case — which is a different, and narrower, thing.

## [end_placed] Dependent — And the Clock Starts
*Day 17 — Friday, November 6, 2026 (dayOffset 17)*

The morning after a disposition is very quiet. The apartment is the same apartment. What has changed is that Amos's case now has a formal shape: an adjudication, a disposition, findings on a record — and a clock.

The next date that matters is the permanency hearing: the law sets it within six months of removal, and within six months of each permanency hearing after that, where the court will ask whether placement is still necessary, whether the plan is being followed, what progress has been made, and whether reasonable efforts were made to finalize it. (42 Pa.C.S. § 6351(e)(3)(i); § 6351(f)) Between now and then, every visit, every arranged night, every signed page is the record that hearing will read.

You put the folder — thinner than it needed to be — on the counter, and you start, this time, with the pages.

**Ending.**

**Debrief:**
- WHAT THE FILE SAID — On this path the court ruled on the record as it stood, and the record was largely the agency's: whichever pieces were missing — the folder not brought to shelter care, the agency record never requested and read so its roster was never checked, the answer that turned into an argument from the seat, or the care plan that existed as a promise instead of a signed commitment — were exactly the pieces that could have tested the agency's proof. The file rated what it could see. On this path, there was less of your side in it to see.
- THE LAW — The judge credited the agency's proof at adjudication (42 Pa.C.S. § 6341(c)) and, at disposition, entered the required findings on the record before continuing placement: that remaining home would be contrary to Amos's welfare, and the court's view of reasonable efforts to prevent removal (42 Pa.C.S. § 6351(b)). The case now runs on the permanency clock: a permanency hearing within six months of removal and within six months of each one after (42 Pa.C.S. § 6351(e)(3)(i)), where placement's continuing necessity, plan compliance, progress, and reasonable efforts are all re-examined (42 Pa.C.S. § 6351(f)(1),(2),(3),(5.1)) — and where a fuller record can change the answers.
- THE HONEST PART — Nothing about this ending grades you as a mother, and it must not be read that way. It records that on one Thursday in November, in one room, the paper on one side of the table was thicker than the paper on the other — and outcomes in this system also turn on workers, judges, resources, and luck: a supervisor's roster practice, a neighbor's eyesight, a judge's reading of a single witness. The clock that started today is real, and so is this: the record for the next hearing has not been written yet, and writing it is still, in large part, yours.
