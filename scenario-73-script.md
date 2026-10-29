# THE FIRST 90 DAYS — Scenario 73: “The Agency's Burden”

*Human-readable script. This document and `scenario-73.json` are generated from a single source and match node-for-node: same IDs, same order, same choices, same effects.*

**The family is fictional — a composite. No real person's story appears here.**

**Content note:** This scenario depicts an adjudication trial, including expert testimony about a child's injury. The injury is discussed, never described graphically. Players may skip any scene or use the quick exit at any time.

**How to read effects:** `cash −40` changes the player's cash. `FLAG: name` sets a flag the engine tracks. `HIDDEN + item` means the case file quietly records that item at this choice — the player does not see it when it happens. `REQUIRES FLAG: name` means the choice is only available if that flag was set earlier; `REQUIRES NO FLAG: name` means it is only available if that flag was never set. `NOTE:` is text shown to the player right after choosing.

Start date: Monday, November 2, 2026. Day offsets are days since the scenario's start date.

## [start] The ER, Then the Call
*Day 0 — Monday, November 2, 2026 (dayOffset 0)*

Your name is Stefan Novak. Your daughter Esme is five — all elbows, opinions, and questions asked at full volume. On Sunday she was at your sister's house, playing on the climbing frame in the yard with her cousin, the way she has a hundred times.

Yesterday she fell. She cried, she got a bruise on her thigh the size of a plum, and by this morning the bruise had darkened enough that you took her to the emergency room to have it looked at — because that is what you do when a bruise worries you.

The ER visit did two things. It found no fracture and a healthy, chatty five-year-old. And it produced a report: the hospital raised concerns of physical abuse, and a check of records added an allegation of medical neglect — three missed well-child appointments, listed in a row, without the reasons beside them.

**Choices:**
- Ask what happens next, and write down every name, time, and word you are given → **removal_hour**
  - NOTE (shown after choosing): Paper remembers what shock forgets. Starting tonight, that matters more than almost anything.
- Ask whether Esme can stay with your sister while this is sorted out → **removal_hour**
  - NOTE (shown after choosing): It is the right question. Tonight, the answer will come from a court process, not from the hallway.

## [removal_hour] The Hardest Hour
*Day 0 — Monday, November 2, 2026 (dayOffset 0)*

With the report open and no court yet involved, the county agency makes its decision: Esme will be taken into protective custody tonight while the court looks at the case. A worker named Mr. Petrov explains it as carefully as a person can explain a thing like this. Esme holds your sleeve. She asks if she did something wrong. She did not.

Hear this clearly, because the whole scenario depends on it: tonight is a decision about safety while facts are checked. It is not a finding. Nothing has been proven, because no court has heard anything yet.

Before they leave, you are handed a paper with a court date. The law's first promise in this case is a fast one: a shelter care hearing within 72 hours of removal. (42 Pa.C.S. § 6332; 23 Pa.C.S. § 6315(d)) That hearing is Thursday, November 5, 2026.

**Choices:**
- Help Esme pack her blanket and her stuffed fox, and tell her plainly: you did nothing wrong, and I will see you Thursday → **lawyer_meet**  _(FLAG: removed)_
  - NOTE (shown after choosing): She goes with the blanket. You go home with the paper. Both of you are carrying something.
- Keep your copy of the paper, folded, in your pocket — and get the worker's name and number before the door closes → **lawyer_meet**  _(FLAG: removed)_
  - NOTE (shown after choosing): Mr. Petrov. A phone number. A date. It is not much paper for the size of what it holds, and it is what you have.

## [lawyer_meet] Mr. Beaumont, the Next Morning
*Day 1 — Tuesday, November 3, 2026 (dayOffset 1)*

You have the right to be represented by a lawyer in this case, and if you cannot afford one, the court can appoint one for you. That right is in the law, not in anyone's kindness. (42 Pa.C.S. § 6337) Mr. Beaumont is the lawyer across the desk this morning — court-appointed, blunt, and uninterested in telling you what you want to hear.

"First, what Thursday is," he says. "Shelter care. One narrow question: where Esme stays while the case is sorted out. You will have counsel at that hearing — that is in the law too. (§ 6332(a)) The judge may well keep her placed on Thursday. Most do, this early, on this little paper."

"Then what is the real fight?" you ask. He taps the petition. "The adjudication. The trial. Currently set for Wednesday, December 2 and Thursday, December 3, 2026. That is where the agency has to prove this — all of it, in a courtroom, with witnesses you can question. Everything between now and then is preparation for those two days."

**Choices:**
- Ask him to explain the trial itself — who has to prove what, and to what standard → **burden_plan**
  - NOTE (shown after choosing): This is the conversation the next thirty days are built on.
- Ask what you should be doing this month, practically, day to day → **burden_plan**
  - NOTE (shown after choosing): "Paper," he says. "Witnesses. Dates. In that order — and we start today."

## [burden_plan] The Burden Speech
*Day 1 — Tuesday, November 3, 2026 (dayOffset 1)*

"Listen carefully," Mr. Beaumont says, "because everything else is commentary. At adjudication, the court may find a child dependent only from clear and convincing evidence. (42 Pa.C.S. § 6341(c)) That burden belongs to the agency. Not to you."

"You do not have to prove you are innocent. You do not have to prove you are a fit father. The agency must prove its allegations — the bruise, the appointments, each one — clearly and convincingly, with evidence the judge can actually rely on. A fact they do not prove is a fact the court cannot use. And if they do not carry that burden, the petition is dismissed and the child is discharged. (§ 6341(a)) Those are the rules of the trial we are going to."

"Your job this month is narrower than you think: make sure they actually have to prove their case — and be ready, with paper and witnesses, at the exact places where their proof can be answered. The judge decides who to believe. Our work is to make sure belief has something solid to stand on, on both sides of the room."

**Choices:**
- Write his sentence in your notebook: 'The burden is theirs. My job is to be ready where it can be answered.' → **shelter_hearing**
  - NOTE (shown after choosing): You will read that sentence a lot in the next thirty days.
- Ask what happens after adjudication, if it goes either way → **shelter_hearing**
  - NOTE (shown after choosing): "Disposition — what happens next — follows immediately, or at a postponed hearing not later than 20 days after adjudication, because Esme was removed. (§ 6341(c)) One fight at a time."

## [shelter_hearing] Shelter Care — Thursday
*Day 3 — Thursday, November 5, 2026 (dayOffset 3)*

The shelter care hearing comes on the third day, as promised: an informal hearing not later than 72 hours after Esme was placed. (42 Pa.C.S. § 6332; 23 Pa.C.S. § 6315(d)) A small courtroom, a thin file, a judge who has read the ER report and very little else — because very little else exists yet.

The agency asks that Esme remain placed while the petition is prepared for trial. Mr. Beaumont does not waste the court's patience arguing the whole case on day three. He makes one practical move instead: Esme's aunt — your sister, at whose home Esme was playing when she fell — is present, and available.

**Choices:**
- Have Mr. Beaumont name your sister on the record as a kin resource, willing to be assessed as a placement today → **shelter_after**  _(FLAG: kinshipOnRecord)_
  - NOTE (shown after choosing): One sentence, spoken in the room. It will still be in the transcript on the day anyone goes looking for it.
- Assume your sister's willingness will be noted in the agency's own file, and save the argument for trial → **shelter_after**
  - NOTE (shown after choosing): She means to note it. Workers mean to write down many things. The transcript only keeps what was said out loud.

## [shelter_after] Placement Continues — the Trial Is the Fight
*Day 3 — Thursday, November 5, 2026 (dayOffset 3)*

The judge continues Esme's placement for now, with visits, and confirms the adjudication dates: Wednesday, December 2 and Thursday, December 3, 2026. It stings in the specific way Mr. Beaumont predicted — not a finding, not a verdict, a holding pattern with a child's address changed.

"Now we work," he says, in the hallway. "One more clock, so you know it exists and then forget it: if a child is in placement 15 of the last 22 months, a court later asks whether a termination petition has been filed, with exceptions — a relative caring for the child, a documented compelling reason, or services the family was never given. (§ 6351(f)(9)) That clock started Monday. It is not this month's fight. This month's fight is two days in December, and it is winnable in the only way trials are winnable: on the evidence."

**Choices:**
- Ask for the visit schedule in writing before you leave the courthouse → **first_visit**
  - NOTE (shown after choosing): Dates, times, a room. Paper again — the visit version.
- Call your sister from the courthouse steps and tell her exactly what the judge said — and did not say → **first_visit**
  - NOTE (shown after choosing): She cries a little, then starts listing what she remembers about Sunday. You tell her to write it down. Today.

## [first_visit] One Hour, in a Room With a Clock
*Day 7 — Monday, November 9, 2026 (dayOffset 7)*

The visit is in a room with a couch, a toy kitchen, and a clock everyone can see. Esme runs to you, tells you about the foster home's cat, and asks — carefully, watching your face — when she is coming home. You give her the honest answer for a five-year-old: grown-ups are having meetings, and you will see her every week, every single week.

Mr. Petrov sits in the corner, kind and quiet, writing. He mentions, on your way out, that the agency's court report is being prepared, and that if you want to see the file the agency is building, 'the office can probably get you a summary.'

**Choices:**
- Take the bus across town to the visit — early, every time, even though the fare adds up → **record_choice**  _(cash −8)_
  - NOTE (shown after choosing): Early goes in the notes. So does everything. Eight dollars of it is bus fare; the rest is just the month you are living in.
- Ride with your sister to the visit, and use the drive to compare your memories of Sunday — separately, in writing → **record_choice**
  - NOTE (shown after choosing): Two accounts, written apart, that agree on the times. That agreement will matter more than either of you yet knows.

## [record_choice] The Written Request
*Day 7 — Monday, November 9, 2026 (dayOffset 7)*

At home, Mr. Beaumont calls with the first real decision of the case. "You can ask for the agency's record — your record — and the regulation says it 'shall be released upon request.' (55 Pa. Code § 3130.44(d)) Not a summary chosen by the office. The record. The rule is also not to be read to protect agency employees' privacy as a basis for withholding it. (§ 3130.44(f))"

"It has to be in writing, dated, with a copy kept. It costs a little — copies, postage, time. And I'll tell you what it buys, because I have watched parents skip it for thirty years: it buys you the right to prepare for the actual case they are bringing, instead of the case you imagine they are bringing. Those are rarely the same case."

Mr. Petrov's offered summary costs nothing. It also shows you only what the office chooses to summarize.

**Choices:**
- Send the written request for the complete agency record this week, and keep a dated copy → **record_found**  _(cash −20 ; FLAG: recordsRequested ; HIDDEN + File — complete agency record released on written request (§ 3130.44(d)); one ER photograph misfiled by date)_
  - NOTE (shown after choosing): Twenty dollars of copies and postage. Watch what it changes: you are about to read the exhibit list before the agency's lawyer does it for you.
- Take Mr. Petrov's summary for now — the written request can wait until things calm down → **record_missed**
  - NOTE (shown after choosing): Things do not calm down. That is rather the point of the next node.

## [record_found] The Photograph That Did Not Belong
*Day 12 — Saturday, November 14, 2026 (dayOffset 12)*

The record arrives in a thick envelope, and you and Mr. Beaumont go through it page by page on a Saturday afternoon: the ER report, the intake notes, the petition drafts — and the photographs, the agency's centrepiece. The petition speaks of 'pattern bruising,' supported by a set of ER photographs listed as exhibits.

On the second pass, Mr. Beaumont stops. One photograph in the set carries a date in its file information that does not match the ER visit — it belongs to a different date, filed in the wrong set. "Clerical," he says, before you can start. "Almost certainly clerical. Files this size breed errors like this, and nobody needs a conspiracy to explain a misfiled photograph. But understand what it is: it is in their exhibit list, attached to the word 'pattern.' At trial, their own exhibit list can be asked about — by us, on the record — because we found it in November instead of hearing about it in December."

This is what the request was for. Not a scandal. A fact, found in time.

**Choices:**
- Go through the rest of the record the same way — every date, every list, against your own calendar → **clinic_letters**
  - NOTE (shown after choosing): Two more small discrepancies, both innocent, both noted. Your notebook is becoming a document.
- Mark the misfiled photograph, flag the page, and set the packet aside for the trial folder → **clinic_letters**
  - NOTE (shown after choosing): Mr. Beaumont writes 'Petrov — exhibit list' on a sticky note. The trial is beginning to have a shape.

## [record_missed] The Summary of a Summary
*Day 12 — Saturday, November 14, 2026 (dayOffset 12)*

Mr. Petrov's summary arrives promptly: two courteous pages. The ER concerns, restated. The missed appointments, listed. The word 'pattern,' used once, without the photographs themselves, without the exhibit list, without dates you can check.

It is not dishonest. It is simply a summary — their selection, their emphasis, their shortening. Mr. Beaumont reads it in four minutes. "This tells us what they think the case is about," he says. "It does not tell us what they will offer at trial. A photograph with a wrong date on it, a letter nobody mentioned — a summary would iron all of that flat, and we would meet it for the first time from the witness stand. We prepare for the case as described, then. It is the only case we were shown."

**Choices:**
- Prepare from the summary, and turn to the clinic's letters — the part of the case that lives in your own paper → **clinic_letters**
  - NOTE (shown after choosing): Your side of the record, at least, you can still build in full.
- Ask Mr. Petrov one more time whether the photographs can be viewed at the office → **clinic_letters**
  - NOTE (shown after choosing): He says he will check. The month is not long, and checking takes the time it takes.

## [clinic_letters] The Clinic's Own Paper
*Day 12 — Saturday, November 14, 2026 (dayOffset 12)*

The petition lists three missed well-child appointments, in a row, as medical neglect. Your account has always been specific: one appointment fell in a month when the clinic itself closed for two weeks and rescheduled its patients; the others collided with shift changes at your work, and you called and rebooked. Two, you have always admitted, you simply missed and rebooked late — you are not going to pretend otherwise, to anyone.

Accounts are not exhibits. The clinic, however, keeps paper: closure notices sent to patients, a reschedule log, letters generated when appointments moved. The clinic's front desk will provide copies of what it sent and when — if someone asks, in November, with time for the copies to be made and certified.

**Choices:**
- Ask the clinic for copies of the closure and reschedule letters, to be offered as an exhibit at trial → **witness_call**  _(cash −10 ; HIDDEN + Exhibit — clinic closure and reschedule letters, admitted)_
  - NOTE (shown after choosing): Ten dollars of copy fees. The petition's neatest row of dates is about to meet the clinic's own dates, in the clinic's own words.
- Photograph the letters at the clinic window to show Mr. Beaumont what exists → **witness_call**
  - NOTE (shown after choosing): He sees they exist. Whether a judge can be handed them, marked and admitted, is a different and more demanding question.

## [witness_call] Calling Early, With Dates
*Day 12 — Saturday, November 14, 2026 (dayOffset 12)*

One witness matters more than any other in this case, and she is not an expert for hire. Ms. Nakamura is the nurse practitioner who has treated Esme since infancy — every well-child visit Esme ever attended, every bruise from every playground before this one, is in her memory and her charts.

She is also a working clinician with a December schedule that fills like weather. Mr. Beaumont is blunt: "If we call this week, with the trial dates and the subpoena information, she can arrange her clinic days and be there. If we call the week of trial, we will get her goodwill and her regrets, and a letter at best. Treating witnesses are won in November or not at all."

**Choices:**
- Have counsel call Ms. Nakamura today — trial dates, subpoena information, and what she would be asked about → **nakamura_secured**  _(FLAG: treatingWitness)_
  - NOTE (shown after choosing): She checks her December, moves two clinic sessions, and says the sentence that decides trials: 'I can be there.'
- Wait until the week of trial — she knows Esme; of course she will come → **nakamura_late**
  - NOTE (shown after choosing): She does know Esme. Her December, unfortunately, also knows her.

## [nakamura_secured] 'I Have Examined This Child Fourteen Times'
*Day 18 — Friday, November 20, 2026 (dayOffset 18)*

Ms. Nakamura confirms, in writing, that she will testify on Thursday, December 3, 2026. On the phone with Mr. Beaumont she is precise in the way clinicians are precise: she has examined Esme fourteen times since infancy; she holds the growth chart, the visit history, and her own notes on two previous playground falls and the bruising they left.

"I am not anyone's witness," she says. "I will answer what I am asked, from the chart and from examining her." Mr. Beaumont thanks her and hangs up smiling for the first time in the case. "That," he says, "is exactly what a treating witness is supposed to sound like. A person who examined the child beats a person who read about the child — in every courtroom I have ever stood in. When she is on the stand, the room will know the difference."

**Choices:**
- Send her the trial dates and courthouse information in writing, and confirm once more the week before → **sister_prep**
  - NOTE (shown after choosing): One letter, one confirmation. Witnesses are logistics before they are testimony.
- Ask Mr. Beaumont what she will be asked on cross-examination, so nobody is surprised in December → **sister_prep**
  - NOTE (shown after choosing): The missed appointments, of course. She knows the record better than the petition does — she is the record.

## [nakamura_late] Goodwill, and a Full December
*Day 18 — Friday, November 20, 2026 (dayOffset 18)*

The call, when it is finally made, reaches a clinician whose December was filled weeks ago: two clinic days she cannot move, patients booked since October, a covering colleague already committed elsewhere. Ms. Nakamura is sorry in a way that is plainly genuine. She can provide a letter summarising Esme's care. She cannot be in a courtroom on December 3.

Mr. Beaumont does not waste breath on blame; the month is what the month is. "A letter," he says, "can be read. It cannot be asked questions, and it cannot answer the agency's expert in the room, in front of the judge, with the chart in its hands. We will offer what we have. Understand what changed, though: the one person who has actually examined Esme, fourteen times, will be a piece of paper — in a trial that is otherwise all about who examined what."

**Choices:**
- Ask her for the fullest letter she can write, with the growth chart and visit history attached → **sister_prep**
  - NOTE (shown after choosing): It will be a good letter. The trial will show the difference between a good letter and a witness.
- Turn to your sister's testimony — she becomes, now, the defense's central live witness → **sister_prep**
  - NOTE (shown after choosing): She is willing. Willingness, rehearsed or not, is about to matter a great deal.

## [sister_prep] Rehearsing Dates, Not Feelings
*Day 18 — Friday, November 20, 2026 (dayOffset 18)*

Your sister was there. Esme fell at her house, from her climbing frame, on her watch — a sentence she has been carrying like a stone all month. Her testimony is simple: the date, the time, the fall, the ice, the tears that stopped, the bruise she saw form. Everything a fact witness is for.

Mr. Beaumont sits her down in his office. "They will not ask whether you love her, and if you answer feelings when they ask times, the times get lost. We rehearse the dates until the dates are boring: Sunday, the hour, who was in the yard, when Stefan was called, what the bruise looked like at bath time. Boring is what believable sounds like."

**Choices:**
- Rehearse with her the way counsel directs: date, time, the fall, who was present — dates, not feelings → **scored_report**  _(FLAG: kinReady)_
  - NOTE (shown after choosing): By the third run-through she is almost bored saying it. Bored, specific, and identical each time. That is the sound.
- Tell her to speak from the heart instead — the judge should see what this family is → **scored_report**
  - NOTE (shown after choosing): Her heart is real, and the court will believe it. What it may not retain, afterward, is a single time or date.

## [scored_report] The Scored Summary in the Court Report
*Day 18 — Friday, November 20, 2026 (dayOffset 18)*

The agency's court report for the adjudication arrives, and stapled into it is a one-page scored summary: a scored assessment form, filled in from the ER report and the intake, which rates 'physical safety: high concern.' It has categories, a score band, and no signature you recognise — and nobody named in the report as the person who scored it.

Mr. Beaumont reads it twice. "Now, the discipline," he says. "At adjudication, proof means testimony and exhibits the judge can weigh — witnesses, questioned. This page was never questioned by anyone. There is an argument, under Rule 1340, that a parent may ask for the evidence under a score — (A) and (B)(1) — present evidence and argument to rebut a provision — (E) — and challenge factual errors in it — (F). I will make that argument. Hear the warning that comes with it: whether Rule 1340 reaches a scored assessment summary has not been tested in a published opinion. It is an argument counsel makes, not a settled right. We make it properly, at the proper moment, and we do not pretend it is more than it is."

**Choices:**
- Ask exactly when, in the trial, an objection like that has to be made to count → **objection_plan**
  - NOTE (shown after choosing): "When it is offered," he says. "Not before, because there is nothing to object to. Not after, because by then it is simply in. When it is offered."
- Ask whether the summary can simply be argued about in closing instead → **objection_plan**
  - NOTE (shown after choosing): "Closing argues about evidence that came in. An objection contests whether it comes in at all. Different weapons, different moments — and only one of them is at the moment of offering."

## [objection_plan] When, Exactly, to Object
*Day 18 — Friday, November 20, 2026 (dayOffset 18)*

The plan is set, in the plain language of trial work. When the agency offers its court report at adjudication — report and scored summary together — Mr. Beaumont will object, on the record, in the room, at that moment: the summary should not be used as proof at adjudication without a witness who can be questioned about how it was scored. He will ask that any errors in it be correctable, and that the underlying evidence be produced for questioning. (Rule 1340(A), (B)(1), (E), (F) — the untested argument, flagged as untested, made anyway, properly.)

"And if the judge admits it anyway?" you ask. "Then the objection, the argument, and the ruling are in the transcript, word for word, forever — and the summary came in over a stated, reasoned objection, which is a different thing from the summary coming in like weather. An objection made at lunch, in a hallway, to the other lawyer, preserves nothing. The transcript is the trial, for everyone who was not in the room. We speak where the transcript can hear us, or we have not spoken."

**Choices:**
- Agree the plan: objection spoken in the room, on the record, at the moment the report and summary are offered → **thanksgiving**
  - NOTE (shown after choosing): He writes it on the trial outline in capital letters: OBJECT — WHEN OFFERED.
- Suggest he sound out the agency's lawyer about the summary beforehand, to keep the trial collegial → **thanksgiving**
  - NOTE (shown after choosing): Collegial is a virtue. It is not a preservation strategy, and hallways, as you have learned, keep nothing.

## [thanksgiving] Thanksgiving, With a Chair Empty
*Day 24 — Thursday, November 26, 2026 (dayOffset 24)*

Thursday, November 26, 2026. Your sister hosts, because your kitchen is too quiet to host in this year. Esme's chair holds her cousin's booster seat. Somebody's grandmother says grace and includes, without making a speech of it, 'the little one who isn't with us today, and may she be home for the next one.'

You brought the dish Esme always demands — the sweet potatoes with the top she picks off first — because making it was something your hands could do. The trial is six days away. The waiting, everyone at this table understands, is its own kind of labour, and it is not scored on any form.

**Choices:**
- Eat with your family, bring the trial folder home unopened, and sleep at a human hour → **thanksgiving_evening**  _(cash −25)_
  - NOTE (shown after choosing): Twenty-five dollars of groceries toward a table that held you up. Rest is preparation too — the least mechanical kind there is.
- Excuse yourself early and spend the evening with the ER report, reading it for the tenth time → **thanksgiving_evening**
  - NOTE (shown after choosing): The report says on the tenth reading exactly what it said on the first. You are not studying anymore. You are circling.

## [thanksgiving_evening] What Waiting Is For
*Day 24 — Thursday, November 26, 2026 (dayOffset 24)*

Late evening. The house is quiet in the way it has been quiet since November 2. Six days: then two days of trial that will decide what the next year of Esme's life is built on.

There are two things waiting can be. It can be the space where the folder gets finished, the witnesses get confirmed, and the hard questions get rehearsed until they are merely hard. Or it can be a room you walk in circles. The trial will not ask how the waiting felt. It will only ever see what the waiting produced.

**Choices:**
- Lay out the trial clothes, check the folder against counsel's list, and call your sister to confirm December 2 → **final_prep**
  - NOTE (shown after choosing): Everything on the list, checked once, in order. Then the folder closes, and so, eventually, do you.
- Stay up past two rereading the agency's court report, memorising your anger at it → **final_prep**
  - NOTE (shown after choosing): Anger memorised is not evidence prepared. You will be tired on the days tiredness costs the most.

## [final_prep] Final Prep, at Counsel's Office
*Day 29 — Tuesday, December 1, 2026 (dayOffset 29)*

Tuesday, December 1, 2026. Mr. Beaumont's office smells of coffee and copier heat. The trial folder is assembled on his desk: the agency record with the misfiled photograph flagged, the clinic letters ready to be offered, the witness list — Ms. Nakamura confirmed, your sister rehearsed — and, at the back, the one section that is about you.

"Tomorrow they go first," he says. "Petrov, then their expert. Thursday is ours: Ms. Nakamura, your sister — and then the last decision of the trial, which is yours. Whether you testify." He lets that sit. "There is no rule that you must. The burden is theirs; resting on their evidence is a real choice, and lawyers make it every week. But if you testify, you will be cross-examined on the appointments — all three, including the two you genuinely missed. That part cannot be improvised. It can only be rehearsed, or endured."

**Choices:**
- Pay for the final copies and the trial-day travel, and organise the folder exactly as counsel's outline orders it → **testimony_rehearse**  _(cash −12)_
  - NOTE (shown after choosing): Twelve dollars, and a folder that opens to the right page the first time. Trials are logistics before they are drama.
- Bring the folder as it is — the judge will hear people, not paperwork → **testimony_rehearse**
  - NOTE (shown after choosing): The judge will hear people. The people will be holding paperwork, and the difference will show by Thursday.

## [testimony_rehearse] The Hard Questions, Practised
*Day 29 — Tuesday, December 1, 2026 (dayOffset 29)*

Mr. Beaumont plays the agency's lawyer, and he does not play him gently. 'You missed three appointments, Mr. Novak.' 'You didn't think your daughter's health mattered.' 'Isn't it true you only rebooked when the agency got involved.' Each question is a small trap with the same shape: it wants a speech, a theory, an argument — anything long enough to get lost in.

The rehearsed answer is shorter and made of paper: the clinic closed, here is its letter; the shift changed, here is the reschedule; two appointments, yes, I missed, here is when I rebooked them, and I am not proud of it and I did rebook them. Said plainly, admitted where admission is due, it takes ninety seconds. Said unprepared, for the first time, under oath, with Esme's photograph on the agency's table — it could take the whole case with it.

**Choices:**
- Rehearse the hard questions until the answers are ninety seconds long: the letters, the admissions, nothing extra → **trial_eve**  _(FLAG: testifyReady)_
  - NOTE (shown after choosing): By the fourth run, your voice stops shaking at 'two I missed.' What remains is just the record, in your words.
- Stop rehearsing — honesty shouldn't need practice, and you'll answer better if you're not scripted → **trial_eve**
  - NOTE (shown after choosing): A real instinct, honestly held. Under oath, at speed, instinct is what produces speeches — and speeches are what cross-examination eats.

## [trial_eve] The Night Before Trial
*Day 29 — Tuesday, December 1, 2026 (dayOffset 29)*

The folder is by the door. The suit that fits is on the chair. Your sister texts: 'See you there. I know my dates.' Ms. Nakamura's confirmation, in writing, sits in the folder's front pocket. Somewhere across town, the agency's lawyer has a folder too — with a scored summary in it, and a photograph filed under the wrong date, and an expert who has read everything about Esme except Esme.

Tomorrow the agency has to prove its case, clearly and convincingly, out loud, in front of a judge who decides who to believe. (42 Pa.C.S. § 6341(c)) That has been the shape of this month since Mr. Beaumont's first sentence. Whatever tomorrow holds, it will at least be the real contest — witnesses, questions, answers — and not a summary deciding things in a quiet office.

**Choices:**
- Set the alarm, lay out Esme's photograph for your pocket, and go to bed → **trial_open**
  - NOTE (shown after choosing): The last preparation is sleep. It is also the only one that cannot be done at the courthouse.
- Do one final read of the trial outline — objection timing, witness order, the ninety-second answers → **trial_open**
  - NOTE (shown after choosing): OBJECT — WHEN OFFERED. Petrov, then Marsh. Then Thursday: Nakamura, your sister, and your decision. Then you close the folder.

## [trial_open] Trial Day One — the Agency Goes First
*Day 30 — Wednesday, December 2, 2026 (dayOffset 30)*

Wednesday, December 2, 2026. The courtroom is smaller than its power. The judge states the matter plainly for the record: a petition alleging dependency — physical abuse, and medical neglect by missed appointments. The agency bears the burden of proving its allegations by clear and convincing evidence. (42 Pa.C.S. § 6341(c)) The parent bears no burden to prove innocence or fitness. A fact not proven, the judge notes, is a fact the court cannot use.

The agency's lawyer rises, and begins the way agency cases often begin: not with a witness, but with paper — the court report, offered as the agency's first exhibit, with the scored summary stapled into it. 'The agency offers its court report, Your Honor.'

Mr. Beaumont looks at the exhibit, and then, fractionally, at you. This is the moment the plan was written for.

**Choices:**
- Sit still, hands folded, and let your lawyer work — your part of today is Thursday → **summary_offer**
  - NOTE (shown after choosing): Everything you want to say has a day assigned to it. Today belongs to their witnesses, and to one spoken sentence.
- Watch the exhibit as it moves toward the judge — the report, and the scored page inside it → **summary_offer**
  - NOTE (shown after choosing): A score band, two categories, no scorer in the room. In thirty seconds, what happens to that page will shape the whole trial.

## [summary_offer] The Summary Is Offered
*Day 30 — Wednesday, December 2, 2026 (dayOffset 30)*

"Agency's Exhibit One, Your Honor — the court report." The clerk reaches for it. The scored summary rides inside it: 'physical safety: high concern,' sourced to the ER report, scored by no one present, questioned by no one, ever.

Mr. Beaumont is on his feet at exactly the speed the plan required — or he is not. Trials are full of moments measured in seconds that echo for years, and almost all of them look, from the gallery, like nothing at all: a lawyer standing, or a lawyer still seated, deciding that lunch would be a friendlier time.

**Choices:**
- OBJECT, now, on the record: the scored summary should not be used as proof at adjudication without a witness who can be questioned about how it was scored → **objection_made**  _(FLAG: preservedObjection ; HIDDEN + Transcript — objection to the scored summary at the moment it was offered (Rule 1340 — untested))_
  - NOTE (shown after choosing): The words are spoken in the room, into the microphone, where transcripts live. Win or lose the ruling, this moment now exists forever.
- Hold the objection — Mr. Beaumont will raise the summary with the agency's lawyer at the lunch recess, off the record → **objection_lunch**  _(FLAG: preservedNothing)_
  - NOTE (shown after choosing): Lunch is in three hours. The exhibit is admitted in three seconds. The arithmetic of that choice is the rest of this trial.

## [objection_made] The Objection, on the Record
*Day 30 — Wednesday, December 2, 2026 (dayOffset 30)*

The argument takes nine minutes, and they are the most carefully built nine minutes of the case. Mr. Beaumont states it plainly: at adjudication the agency must prove dependency with evidence the court can weigh; this summary has no witness; its factual basis can be asked for and its errors challenged — the argument under Rule 1340(A) and (B)(1) for the evidence under a score, (E) to present evidence and argument in rebuttal, and (F) to challenge factual errors. He says the next sentence himself, before the agency can: whether Rule 1340 reaches a scored assessment summary has not been tested in a published opinion; he makes the argument because the record is where arguments are made.

The judge rules with care: the report comes in for what its witnesses will support, but the scored summary will not be treated as proof of anything at adjudication without a witness who can be questioned about it, and its stated factual basis may be challenged like any other. 'Note the objection and the ruling,' the judge tells the clerk. In the transcript, in type, the moment is preserved — four lines that will outlast everyone in the room's memory of this morning.

**Choices:**
- Take your seat and let the agency call its first witness — now the case must be proven with people → **petrov_direct**
  - NOTE (shown after choosing): The agency's lawyer opens a different folder. The trial, from here, is testimony.
- Note the judge's exact words in your notebook, word for word, while they are fresh → **petrov_direct**
  - NOTE (shown after choosing): 'Not proof without a witness who can be questioned.' You will hear that sentence again — in the closing, where it belongs.

## [objection_lunch] Lunch, in the Hallway
*Day 30 — Wednesday, December 2, 2026 (dayOffset 30)*

The exhibit was admitted in the morning without discussion — report, summary, score band and all. At lunch, in the hallway by the water fountain, Mr. Beaumont raises it with the agency's lawyer, collegially, reasonably, and entirely off the record. The agency's lawyer is sympathetic and immovable: the report is in; closing is the place for weight arguments.

Back in the courtroom, when Mr. Beaumont mentions the lunch conversation, the judge is courteous and exact: 'Counsel, the record will reflect what was said in this room.' What was said in this room, about the summary, is nothing — no objection, no argument, no ruling. The scored page sits in the exhibit binder now like weather: 'physical safety: high concern,' in front of the judge for the rest of the trial, unobjected-to, unanswered at the only moment answering was possible.

**Choices:**
- Return to your seat — the witnesses still have to testify, and testimony can still be cross-examined → **petrov_direct**
  - NOTE (shown after choosing): The trial is not over. But one door, the one marked with the summary, closed in the morning without a sound.
- Write down, yourself, what the lunch conversation contained — for your own folder, if nothing else → **petrov_direct**
  - NOTE (shown after choosing): Your note is accurate, dated, and sincere. It lives in your folder. The transcript, which is the trial for everyone else, does not contain it.

## [petrov_direct] Mr. Petrov Testifies
*Day 30 — Wednesday, December 2, 2026 (dayOffset 30)*

The agency's first witness is Mr. Petrov. He is not a villain and does not testify like one: he describes the ER call, the bruised thigh, the photographs taken that night — a set of them, he says, showing 'a pattern of bruising' — and the records check that produced the three missed appointments. His manner is careful. His evidence, laid end to end, is the petition exactly as written.

On the last part he is honest in a way that will matter: he did not take the photographs, he did not examine Esme, and the exhibit list in the court report was assembled from the file 'as it was received.' Mr. Beaumont rises for cross-examination with the agency's own record open at a flagged page — if, in November, anyone asked for that record.

**Choices:**
- Cross on the exhibit list: the photograph filed under a different date, in the agency's own record → **petrov_cross**  _(REQUIRES FLAG: recordsRequested)_
  - NOTE (shown after choosing): This cross-examination exists only because the record was requested in November. Without the flagged page, there is nothing to stand on but suspicion.
- Cross on what Mr. Petrov personally saw and did — careful, general, and without the file's specifics → **petrov_cross_thin**
  - NOTE (shown after choosing): He answers it easily. He saw a bruise and made a call; on that, everyone in the room already agrees.

## [petrov_cross] Cross: the Agency's Own Exhibit List
*Day 30 — Wednesday, December 2, 2026 (dayOffset 30)*

It takes six questions. Was this photograph part of the set offered as showing a pattern? It was. What date does the file information carry? A different date. Not the ER visit? Not the ER visit. How did it come to be in this set? A filing error, he believes — clerical — when the records were assembled. And the word 'pattern,' in the petition and the report — it rests on the set, as assembled? 'It rests on the photographs, yes.'

The judge directs the exhibit list corrected on the record, and the misfiled photograph removed from the set. Nobody alleges bad faith; Mr. Beaumont says, for the transcript, 'Clerical errors happen in files this size, Your Honor. What the defense asks is that the finding not be built on one.' What remains of the 'pattern' is one bruise, on one thigh, with a documented fall the agency's case has not yet mentioned. The room can feel the allegation change shape.

**Choices:**
- Sit down while the correction is still the last thing the judge heard → **marsh_direct**
  - NOTE (shown after choosing): The exhibit list, the petition's strongest word, and the transcript now disagree with each other. That disagreement is defense evidence.
- Thank Mr. Petrov for his candour — it costs nothing, and the judge notices who made the error easy to admit → **marsh_direct**
  - NOTE (shown after choosing): He answers like a professional because he was questioned like one. The record keeps both halves of that.

## [petrov_cross_thin] Cross: What One Man Saw
*Day 30 — Wednesday, December 2, 2026 (dayOffset 30)*

The cross is fair, and general, and lands where it lands: Mr. Petrov saw a concerning bruise, followed the process, and believed the report he assembled. Pressed on the photographs, he describes the set as it was given to him — a pattern, per the file. Nobody in the room has the file. Nobody can put a flagged page in front of him and ask about a date, because the only people holding the agency's exhibit list, complete with its file information, are the agency.

Mr. Beaumont sits down having established sincerity, which was never the question. In the exhibit binder, uncorrected, the misfiled photograph keeps its place in the set, and the word 'pattern' keeps its full weight — a weight assembled, in part, from a picture of a different day that no one outside the agency has ever seen.

**Choices:**
- Let the agency call its expert — the photographs' real defender is next, in any event → **marsh_direct**
  - NOTE (shown after choosing): The agency's lawyer is already standing. The pattern claim now rests, formally, on Dr. Marsh.
- Note, for closing, the one concession available: Mr. Petrov never examined Esme himself → **marsh_direct**
  - NOTE (shown after choosing): True, and useful — but it is a smaller sentence than the one about the exhibit list that might have been.

## [marsh_direct] Dr. Marsh, by Photograph and File
*Day 30 — Wednesday, December 2, 2026 (dayOffset 30)*

The agency's expert is Dr. Marsh, a paediatrician whose qualifications nobody disputes. Her opinion is measured and grave: the bruising, in the photographs and records she reviewed, is concerning for inflicted injury; in her differential — her list of possible causes — she has considered and set aside accident, 'based on the pattern and the history provided.' She has also reviewed the appointment history, and calls it 'a concerning gap in routine care.'

Mr. Beaumont's questions, when the judge nods to him, begin at the foundation rather than the conclusion. He has three documents in front of him. Two of them, Dr. Marsh has never seen. That fact, and not any quarrel with her qualifications, is what the next ten minutes are for.

**Choices:**
- Cross on the foundation: what she examined, what she was sent, and what her differential never contained → **marsh_cross**
  - NOTE (shown after choosing): Qualifications conceded, cheerfully, in the first sentence. Everything after that is about the file she was given.
- Let her opinion stand unexamined and save the defense's energy for its own witnesses tomorrow → **day1_close**
  - NOTE (shown after choosing): An expert un-crossed is an expert adopted. Her phrases — 'pattern,' 'concerning gap' — will be the agency's closing, unanswered.

## [marsh_cross] Cross: Never Examined the Child
*Day 30 — Wednesday, December 2, 2026 (dayOffset 30)*

"Doctor, you never examined Esme." — "I reviewed the records and photographs." "You were sent the ER report and the photographs. Were you sent the clinic's closure and reschedule letters?" A pause, and a look at the agency's table. "I don't recall them." "Were you sent any statement from the child's aunt — the adult present on the Sunday in question — describing a fall from playground equipment?" "No." "Is a fall from playground equipment the kind of event that would ordinarily appear in a differential for a bruise on a five-year-old's thigh?" "Ordinarily, yes — if it were in the history provided to me."

Nothing about her changed. Her opinion stands exactly as far as her materials reach — and the transcript now shows, in her own words, where those materials end: she never examined the child, she had not seen the clinic closure letters, and her differential omits the playground fall because nobody sent her the sister's statement. An expert who examined the child and an expert who read a file are not the same witness. After this cross, the judge knows precisely which kind each side has.

**Choices:**
- End the cross there — the last answer is the one to leave standing → **day1_close**  _(cash −6 ; HIDDEN + Transcript — agency expert: never examined the child; had not seen the clinic closure letters)_
  - NOTE (shown after choosing): Six dollars of parking and coffee is the whole cost of day one. The transcript of it is considerably more valuable.
- Ask one final question — whether she can rule out the fall she was never told about — and then sit down → **day1_close**  _(cash −6)_
  - NOTE (shown after choosing): 'I can only speak to the history I was given,' she says. It is the most important sentence of the agency's case, and their witness said it.

## [day1_close] Day One Ends
*Day 30 — Wednesday, December 2, 2026 (dayOffset 30)*

The agency rests. The judge looks at the clock, then at both tables. "The defense case tomorrow, counsel. Nine o'clock." Outside, the December dark has already fallen, and your sister is crying quietly on the courthouse steps — relief, exhaustion, and one more day of it, in equal parts.

Mr. Beaumont's summary in the car park is three sentences. "Their case is now exactly as strong as its witnesses, and both of their witnesses have told the judge the limits of what they know. The pattern has a hole in it, or it doesn't; their expert has a hole in her file, and she said so. Tomorrow, the judge hears from the people who were actually there."

**Choices:**
- Go home, eat standing up in the kitchen like a person in a film, and lay out Thursday's folder → **trial_day2**
  - NOTE (shown after choosing): Tomorrow the questions run the other way. Everything November built gets carried into one room, once.
- Call your sister from the car and tell her, plainly, what tomorrow needs from her: her dates, in order → **trial_day2**
  - NOTE (shown after choosing): 'Sunday. The hour. The fall. Bath time.' She recites them back. Boring. Specific. Ready.

## [trial_day2] Trial Day Two — the Defense Case
*Day 31 — Thursday, December 3, 2026 (dayOffset 31)*

Thursday, December 3, 2026. The judge takes the bench, the transcript machine starts its quiet work, and Mr. Beaumont calls the defense case. Everything in this case now turns on a short list of people: a nurse practitioner who has treated Esme since infancy, an aunt who watched her fall, and — if he chooses — a father with ninety seconds of rehearsed answers and a folder of clinic letters.

The first name called is the one November decided.

**Choices:**
- Call Ms. Nakamura — the treating nurse practitioner who has examined Esme since infancy → **nakamura_testimony**  _(HIDDEN + Transcript — treating nurse practitioner: 'I have examined this child fourteen times' ; REQUIRES FLAG: treatingWitness)_
  - NOTE (shown after choosing): She takes the oath with her chart in her hand. Fourteen examinations. The agency's expert had photographs; the room is about to hear the difference.
- Proceed without Ms. Nakamura's live testimony — offer her letter and the attached chart instead → **nakamura_absent**  _(REQUIRES NO FLAG: treatingWitness)_
  - NOTE (shown after choosing): The letter goes in as paper. Paper cannot be asked the question the whole trial is waiting for — and cannot answer it.

## [nakamura_testimony] 'I Have Examined This Child Fourteen Times'
*Day 31 — Thursday, December 3, 2026 (dayOffset 31)*

"I have examined this child fourteen times," Ms. Nakamura says, "from her two-week visit to this September." She walks the judge through the growth chart — steady, unremarkable, the curve of a thriving child. Through the appointment history, from the chart itself: the clinic closure, the rescheduled visits generated by its own letters, the two appointments Stefan missed and rebooked, dated in her handwriting. "That is not a concerning gap," she says. "That is a clinic that closed, and a parent who rebooked."

Then the bruise. She has treated two of Esme's playground falls before this one, and documented the bruising each left. "A single bruise, on the front of the thigh, in a five-year-old who fell from climbing equipment onto a yard toy — that is a bruise I have seen, in this child, from exactly that kind of fall. Pattern injuries look different, and there is one bruise here, not a pattern." On cross, the agency's lawyer is respectful and brief. There is, in the end, very little to cross a treating clinician about, in front of a judge, with her own chart open.

**Choices:**
- Rest the medical part of the defense there, and call the witness who was in the yard on Sunday → **sister_testimony**
  - NOTE (shown after choosing): Direct, cross, chart, done. The judge's notes from this witness run to two full pages. You counted.
- Have her confirm, finally, that Esme has never once presented with an unexplained injury in fourteen examinations → **sister_testimony**
  - NOTE (shown after choosing): 'Never,' she says. It is a short word, with fourteen examinations inside it.

## [nakamura_absent] A Letter, Read Aloud
*Day 31 — Thursday, December 3, 2026 (dayOffset 31)*

Ms. Nakamura's letter is admitted and read into the record: a careful clinician's summary of a healthy child, a clinic closure, a rebooked history. It is a good letter. The agency's lawyer does not even object to it.

That, Mr. Beaumont murmured at the recess, is rather the problem. Dr. Marsh testified live, answered questions, and left her authority standing in the room even after cross showed the edges of her file. A letter cannot do the counterweight's work: it cannot be handed the growth chart and asked to explain it, cannot say 'I have examined this child fourteen times' in a voice a judge can weigh, cannot answer the word 'pattern' with the words 'I have seen this child's bruises before.' Between an expert who read a file and a letter about a child, the court has only one live medical witness — and she is theirs.

**Choices:**
- Call your sister — the defense's medical voice is paper, so its eyewitness must be live and exact → **sister_testimony**
  - NOTE (shown after choosing): She is already standing. Everything now rides on Sundays and times and dates.
- Ask the judge to note, for the record, that the treating clinician's schedule was set months before the defense call reached her → **sister_testimony**
  - NOTE (shown after choosing): The judge notes it, neutrally. It explains an absence. Explanations of absences are not testimony.

## [sister_testimony] The Fall, the Timing
*Day 31 — Thursday, December 3, 2026 (dayOffset 31)*

Your sister testifies the way the fall happened: in order. Sunday afternoon. The yard, the climbing frame, the cousin, the fall onto the ride-on toy at the frame's base. The hour she called Stefan. The ice in a tea towel. The tears that stopped before the ice melted. The bruise at bath time, darkening, and the call the next morning — her call, she says, looking at the judge — that sent Stefan to the ER with her.

On cross, the agency's lawyer tests the times, gently at first, then properly. The times hold — because they were rehearsed as dates, or because she finds them as she goes. Either way, by the end, the fall exists in the transcript in sworn, specific form: a time, a place, a mechanism, a witness. It is no longer a claim in a father's interview. It is evidence, from a person who was there, that the agency's expert never received.

**Choices:**
- Watch the judge's pen through the cross — and let the dates do the work they were rehearsed to do → **stefan_decision**
  - NOTE (shown after choosing): The pen moves at the times. That is what pens at trials are for.
- Pass Mr. Beaumont the note you wrote — 'bath time, she saw it form' — in case the timing needs one more question → **stefan_decision**
  - NOTE (shown after choosing): He nods, asks it, and sits down. The eyewitness case is complete: a fall, a time, a bruise, in that order.

## [stefan_decision] Your Name, or Silence
*Day 31 — Thursday, December 3, 2026 (dayOffset 31)*

The last decision of the trial belongs to you, and Mr. Beaumont puts it without decoration, in the corridor, in four minutes. "You can testify: your account, in your words — the ER visit you chose to make, the clinic letters, the two appointments you missed and rebooked. Under cross, all of it, at speed."

"Or we rest. The burden was never yours; the judge has been told so by the law and by me. Resting is not surrender — it is a statement that their evidence should sink or swim on its own. What resting cannot do is put the clinic letters in your voice, or the words 'two I missed' said by the only man who can say them. Choose the consequences you understand, Stefan. That's all any witness decision ever is."

**Choices:**
- TESTIFY — rehearsed, narrow, with the clinic letters: ninety seconds of answers and nothing extra → **stefan_ready**  _(REQUIRES FLAG: testifyReady)_
  - NOTE (shown after choosing): You take the oath with the folder's last section in the clerk's hands. The hard questions are coming. You have already answered them four times.
- TESTIFY — unrehearsed, determined to finally explain everything, all of it, to the judge → **stefan_unready**  _(REQUIRES NO FLAG: testifyReady)_
  - NOTE (shown after choosing): Everything includes things nobody asked about. Under oath, 'everything' is a much larger and more dangerous country than it is in a corridor.
- REST — do not testify; the agency must carry its burden on its own evidence → **closing**
  - NOTE (shown after choosing): A principled silence. The judge has your sister, your clinician, and their holes. Whether that is enough, the closing will now argue.

## [stefan_ready] Ninety Seconds
*Day 31 — Thursday, December 3, 2026 (dayOffset 31)*

You testify the way the rehearsal built it: short, sworn, and made of dates. Yes, you took Esme to the ER yourself, on your sister's call, the morning after the fall. The closure letter, identified. The reschedule letter, identified. And then the trap question, arriving exactly on schedule: 'You missed appointments, Mr. Novak, didn't you.'

"Two," you say. "I missed two, and I rebooked both, and the dates are in the chart. I'm not proud of them. They are the only two." The agency's lawyer tries twice more — a speech about responsibility, a theory about indifference — and twice more the answer is a date or a letter, ninety seconds in total, and then there is nowhere else for the cross to go. You step down having given the trial nothing it did not already have on paper, and the judge something paper cannot give: the sound of a man admitting the true part.

**Choices:**
- Take your seat and let your lawyer close — the evidence, all of it, is now in → **closing**
  - NOTE (shown after choosing): Direct, cross, done. Your voice is in the transcript at its most credible length: the length of the truth.
- Ask, before closing, that the clinic letters be marked as admitted exhibits in the record → **closing**
  - NOTE (shown after choosing): The clerk marks them. Exhibits, not accounts — the distinction this entire month was about.

## [stefan_unready] The Speech
*Day 31 — Thursday, December 3, 2026 (dayOffset 31)*

It begins well. Then the appointment question comes, and instead of ninety seconds you give the judge a tour: the clinic, the shifts, the neighbour who has 'had it in for this family since the fence,' a theory about the hospital, the report, the whole month — unspooling, sincere, and entirely unasked. You can see the judge's pen slow, then stop. A volunteered theory about a neighbour's grudge, offered by the one witness who most needed to sound like a record, is a thing judges visibly discount — because it answers a question nobody posed, in place of the questions that were posed.

Worse, in the unspooling, the two appointments blur into four, then 'a few,' and the reschedule dates come out in the wrong order — small gaps, honestly made, and exactly the gaps a closing argument is built to walk through. You step down having done the one thing the burden speech warned against: you supplied, from the witness chair, the proof problems the agency's own case still had.

**Choices:**
- Keep explaining from the witness chair — the grudge, the clinic, the month, everything at once → **end_loss**
  - NOTE (shown after choosing): Every extra sentence is sworn, and permanent, and longer than the defense case it is burying.
- Answer one more question about the appointments from memory, without the letters, guessing at the order of the dates → **end_loss**
  - NOTE (shown after choosing): The guesses are wrong in the small ways that matter. The transcript will keep them at full size.

## [closing] Closing — Element by Element
*Day 31 — Thursday, December 3, 2026 (dayOffset 31)*

Mr. Beaumont closes the way the case was built: element by element, allegation by allegation, against the only standard in the room. Clear and convincing. (42 Pa.C.S. § 6341(c)) Not suspected, not summarised, not scored — proven, by witnesses who could be questioned, or not proven at all.

The judge takes the case under advisement for the length of a recess, and the corridor outside holds its breath: your sister, the foster mother's name on a visit form somewhere, Esme's photograph in your pocket. What Mr. Beaumont asks for, in his final sentence, depends on what the record actually contains — the objection, the cross-examinations, the treating witness, the letters. A closing can only spend what the trial deposited.

**Choices:**
- Close on the burden, element by element, and ask for findings naming each allegation that was NOT proven → **end_win**  _(HIDDEN + Order — findings list the allegations NOT proven, by name ; REQUIRES FLAG: recordsRequested ; REQUIRES FLAG: treatingWitness)_
  - NOTE (shown after choosing): This closing exists because the record was requested and the treating witness was called in November. Both sentences are literally true.
- Ask the court to disregard the scored summary based on the hallway discussion at lunch → **end_summary**  _(REQUIRES FLAG: preservedNothing)_
  - NOTE (shown after choosing): The judge's answer is already written in the morning's transcript — in the place where the objection is not.
- Close on the whole record as it stands — sister, letters, and the burden — without the photograph cross → **end_home**  _(REQUIRES NO FLAG: recordsRequested)_
  - NOTE (shown after choosing): A real closing, honestly argued. It concedes, by its shape, that the agency's exhibit list was never examined by anyone outside the agency.
- Close generally and submit the case on the record that exists → **end_home**
  - NOTE (shown after choosing): The judge will decide on what is actually in front of the court — which is, in the end, the only thing judges ever decide on.

## [end_win] Not Dependent — The Burden Was Not Carried
*Day 31 — Thursday, December 3, 2026 (dayOffset 31)*

The judge rules from the bench, allegation by allegation, in the order the petition pleaded them. Physical abuse: not proven by clear and convincing evidence — the only live medical testimony from a clinician who examined the child attributed the single bruise to the documented fall; the agency's expert, by her own testimony, never examined Esme, had not seen the clinic letters, and had never been given the fall. The 'pattern' rested in part on a photograph the agency's own witness corrected off its exhibit list, on the record. Medical neglect: not proven — the clinic's own letters account for the closure and the reschedules, and the two admitted misses, rebooked, do not carry the allegation to clear and convincing.

Under the law the judge states it in one sentence: where dependency is not proven, the petition is dismissed and the child is discharged. (42 Pa.C.S. § 6341(a); § 6341(c)) The findings list the allegations NOT proven, by name. Esme comes home on Thursday, December 3, 2026 — thirty-one days after she left — to her own bed, her stuffed fox, and a father who is allowed, finally, to stop keeping a folder on the kitchen counter. He keeps it anyway. Some habits outlast their necessity.

**Ending.**

**Debrief:**
- WHAT THE FILE SAID — The hidden record, revealed: the complete agency record, released on a written request (55 Pa. Code § 3130.44(d)), contained the trial: a photograph misfiled by date inside the 'pattern' exhibit set; the objection to the scored summary, spoken at the moment it was offered and ruled on in the transcript; the agency expert's own words — never examined the child, had not seen the clinic closure letters; the clinic closure and reschedule letters, admitted as exhibits; and the treating nurse practitioner's testimony — 'I have examined this child fourteen times.' The order's findings close the set: the allegations not proven, listed by name.
- THE LAW THAT CONTROLLED IT — At adjudication the court may find a child dependent only from clear and convincing evidence, and that burden is the agency's: the parent does not have to prove innocence or fitness. (42 Pa.C.S. § 6341(c)) Where the burden is not carried, the petition is dismissed and the child discharged. (§ 6341(a)) Agency records are released on written request (§ 3130.44(d)); the objection to the scored summary rested on Rule 1340(A), (B)(1), (E) and (F) — an argument counsel made on the record, expressly flagged as untested in any published opinion, and preserved either way.
- THE HONEST PART — This outcome turned on things no strategy fully controls: a judge who weighed a treating clinician over a file review, an expert honest about the limits of her materials, a caseworker who answered cross-examination candidly. A different judge could have credited the agency's evidence; trial courts weigh credibility, and credibility is not a lever a parent holds. What the strategy controlled was narrower and real: every fact that could have been lost in November — a file, a witness, a date, an objection — was in the room in December. This ending is not a verdict that Stefan was a perfect father. It is a ruling that the agency did not prove its case. Those are different sentences, and the difference is the whole game.

## [end_home] Dependent — But the Placement Ends
*Day 31 — Thursday, December 3, 2026 (dayOffset 31)*

The judge's findings are narrow, and their narrowness is the story. Physical abuse: NOT among the findings — the fall, the treating witness's chart or letter, and the single bruise do not carry that allegation to clear and convincing, and the judge says so. What stands is one thread of the neglect allegation: a missed appointment, unrebooked for a stretch the judge finds the letters do not fully cover, proven just clearly enough. On that thread alone, Esme is adjudicated dependent.

Disposition follows in the same hearing, as the law allows. (42 Pa.C.S. § 6341(c)) The judge orders the disposition that ends the placement: Esme remains in her father's legal and physical care, subject to conditions and supervision. (§ 6351(a)(1)) She goes home on Thursday, December 3, 2026 — home, with a supervision order, a services list, and a case that is not closed. The allegation that took her is not among the findings. The appointment that kept the case open is.

**Ending.**

**Debrief:**
- WHAT THE FILE SAID — The hidden record, revealed: the defense record was partial, and the findings trace its edges exactly. Where the treating witness was a letter instead of a live witness (no treatingWitness flag), or the agency's exhibit list was never examined because the record was never requested (no recordsRequested flag), the agency's account of the appointments stood longer than it should have. What was built — the clinic letters, the sister's account of the fall, the crosses that were made — was enough to defeat the abuse allegation outright. It was not quite enough to clear the last appointment.
- THE LAW THAT CONTROLLED IT — Dependency requires clear and convincing evidence, allegation by allegation (42 Pa.C.S. § 6341(c)); an allegation not carried to that standard cannot be a finding, which is why the abuse allegation is absent from the order. The proven thread supported adjudication, and at disposition the court chose the least restrictive listed option on these facts: the child remains with the parent subject to conditions and supervision. (§ 6351(a)(1)) Disposition followed immediately, within the discipline of § 6341(c).
- THE HONEST PART — This is a partial win, honestly labelled: Esme is home, and the worst allegation failed — and a dependency case, with supervision and services and the next hearing already calendared, is now part of this family's life. It turned on November logistics as much as on December law: a clinician's filled schedule, a record never requested, a photograph never questioned. Different timing, a different judge's weighing of one appointment — the same father lands in a different ending. Outcomes here turn on workers, judges, resources and luck. Paper and witnesses are simply the part of it a parent can hold.

## [end_summary] Dependent on the Summary
*Day 31 — Thursday, December 3, 2026 (dayOffset 31)*

The judge's findings lean, audibly, on the scored page. 'The assessment rates physical safety as high concern,' the ruling says, more than once — a conclusion no witness ever testified to, no cross-examination ever tested, and no objection ever contested at the moment it entered the case. The hallway conversation at lunch is nowhere in the ruling, because it is nowhere in the record. Against a scored 'high concern' that sits in the exhibit binder like a finding, the defense's live witnesses are weighed — and the summary, unobjected-to, anchors the scale.

Esme is adjudicated dependent. Her placement continues, and disposition is postponed to a hearing within the window the law sets — not later than 20 days after adjudication, because she was removed. (42 Pa.C.S. § 6341(c)) The salvage is thin and real: the crosses that were made, the witnesses who did testify, and every other preserved word remain in the transcript for the disposition fight and beyond. The summary, however, will be in the file at every hearing from now on — admitted, unobjected-to, and first in the binder.

**Ending.**

**Debrief:**
- WHAT THE FILE SAID — The hidden record, revealed: the scored summary shows 'physical safety: high concern,' sourced to the ER report, scored by no one who ever took an oath in this case. Because the objection was held for a hallway at lunch (flag: preservedNothing), the transcript contains no objection, no argument, and no ruling about it — for everyone who was not in the hallway, the objection simply never happened. The rest of the record — any photograph cross, treating testimony, clinic letters actually offered — is preserved and usable later. It is the salvage. It did not outweigh the page that came in like weather.
- THE LAW THAT CONTROLLED IT — Adjudication still required clear and convincing evidence (42 Pa.C.S. § 6341(c)) — but evidence admitted without objection is evidence the court may weigh, and a summary's conclusions, unobjected-to at the moment of offering, were weighed here as if they were testimony. The Rule 1340 argument about the evidence under a score — (A), (B)(1), (E), (F), untested in any published opinion as to scored summaries — was never made where the record could keep it, so no ruling on it exists. Disposition now follows within 20 days of adjudication. (§ 6341(c))
- THE HONEST PART — Label this honestly: it is a losing outcome, with one salvage — a preserved record, everywhere except the one moment that mattered most. It was not lost because Stefan loved his daughter less, or testified worse, than in any other ending. It was lost in three seconds on a Wednesday morning, when an exhibit moved toward a judge and a lawyer stayed seated to keep a lunch friendly — a timing decision, made of politeness and hope, of exactly the kind exhausted people make every day in real courtrooms. Workers, judges, calendars and luck held the rest. But the transcript holds only what the room gave it, and the room gave it silence.

## [end_loss] Adjudicated on Their Paper
*Day 38 — Thursday, December 10, 2026 (dayOffset 38)*

The adjudication ruling, on Thursday, December 3, 2026, finds every allegation proven: the abuse allegation carried by an exhibit set never corrected and an expert never effectively answered, the neglect allegation completed — in the judge's words — by 'the father's own account,' the unrehearsed testimony that blurred the dates, volunteered a grudge theory the court discounts on the record, and supplied the gaps the agency's witnesses had left open.

Disposition is postponed, and held on Thursday, December 10, 2026, within the 20 days the law allows after adjudication of a removed child. (42 Pa.C.S. § 6341(c)) At disposition the rules of evidence loosen in the way the statute provides — written reports and all evidence helpful to the determination may be received, subject to examination and cross-examination of their makers (§ 6341(d)(1), (2)) — and the court's order continues Esme's placement. Before ordering it, the judge reads the required findings onto the record: that continuation in the home would be contrary to Esme's welfare, and the court's determination on whether reasonable efforts were made to prevent removal. (42 Pa.C.S. § 6351(b)) A permanency hearing will follow within six months. (§ 6351(e)(3)(i)) The case is not over. It is, from here, a much longer road than the one November offered.

**Ending.**

**Debrief:**
- WHAT THE FILE SAID — The hidden record, revealed: the agency's paper went into the findings largely as written — an exhibit set whose misfiled photograph was never challenged because the record that would have exposed it was never in the defense's hands or never used; an expert opinion whose foundation was never fully tested; and a scored account of the missed appointments that the father's own unrehearsed testimony ended up corroborating in the places it was weakest. The file rated what it could see, and at the trial, what it could see was mostly the agency's version — because the defense's version arrived late, as letters, or as a speech.
- THE LAW THAT CONTROLLED IT — The burden never moved: dependency still required clear and convincing evidence from the agency. (42 Pa.C.S. § 6341(c)) What changed is that unrebutted paper, plus testimony that filled its gaps, allowed the court to find that burden carried on every allegation. Disposition followed within 20 days (§ 6341(c)); at disposition, reports may be received even if they would not have been competent at adjudication, with the makers subject to cross-examination (§ 6341(d)(1), (2)); and a placement disposition requires on-the-record findings on contrary-to-welfare and reasonable efforts. (§ 6351(b)) None of those rules failed. They were simply all exercised on a record the defense never built.
- THE HONEST PART — This ending is a loss, and it is not a verdict that Stefan is a bad father — the judge never found that, because courts do not find that; they find allegations proven or not proven, on records. It turned on logistics and record mechanics: a witness called too late or never effectively presented, a file never requested in time, a rehearsal skipped out of a sincere belief that honesty needs no practice. Another judge might have discounted the agency's paper more steeply; another worker might have flagged the photograph themselves. Workers, judges and luck held those pieces. What no strategy can recover, once the transcript closes, is a moment that passed inside it — which is why this scenario makes you live the moments in November, while they are still cheap.
