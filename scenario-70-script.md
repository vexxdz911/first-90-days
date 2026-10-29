# THE FIRST 90 DAYS — Scenario 70: “A Report Is Not a Witness”

*Human-readable script. This document and `scenario-70.json` are generated from a single source and match node-for-node: same IDs, same order, same choices, same effects.*

**The family is fictional — a composite. No real person's story appears here.**

**Content note:** This scenario depicts an adjudication hearing built around a written report and the witnesses who did and did not appear. There is no graphic content. Players may skip any scene or use the quick exit at any time.

**How to read effects:** `cash −40` changes the player's cash. `FLAG: name` sets a flag the engine tracks. `HIDDEN + item` means the case file quietly records that item at this choice — the player does not see it when it happens. `REQUIRES FLAG: name` means the choice is only available if that flag was set earlier; `REQUIRES NO FLAG: name` means it is only available if that flag was never set. `NOTE:` is text shown to the player right after choosing.

Start date: Monday, November 23, 2026. Day offsets are days since the scenario's start date.

## [start] The Sentence He Has Read Four Times
*Day 0 — Monday, November 23, 2026 (dayOffset 0)*

Your name is Emmett Merritt. Your daughter Jade is eight. She has been living with a foster family since October — that placement happened before this story opens — and her backpack now lives by someone else's front door, packed for visits with you.

The dependency petition is on your kitchen table, and one sentence in it has been read so many times the page is soft: that on a Thursday night in October, you left Jade unsupervised overnight. You know that night. Your work trip ran late, Jade had dinner at your neighbor Mr. Danquah's table like she had a dozen times, your car was in your drive that evening, and you carried a half-asleep Jade home in her socks.

The sentence, you have slowly realized, did not come from anyone who was there. It came from a written report by the school nurse, Mrs. Castellano, summarizing something Jade said at school the next day. Adjudication — the hearing where the facts themselves get decided — is in one week, on Monday, November 30, 2026.

**Choices:**
- Call your lawyer's office and ask, plainly, what happens next → **october_context**
  - NOTE (shown after choosing): Mr. Beaumont's paralegal books you in for tomorrow and tells you to bring the petition, a pen, and every question you have.
- Read the petition a fifth time, looking for the nurse's name among the witnesses → **october_context**
  - NOTE (shown after choosing): Her name appears inside the report's lines. It does not appear on the agency's witness list. You circle that, twice.

## [october_context] October, in the Rear-View Mirror
*Day 0 — Monday, November 23, 2026 (dayOffset 0)*

October moved the way these cases move: a report, a placement, and then a shelter care hearing held quickly, because the law makes it come quickly — an informal hearing not later than 72 hours after a child is placed in shelter care. (42 Pa.C.S. § 6332; 23 Pa.C.S. § 6315(d)) At that hearing the court continued Jade's placement while the case was sorted out. That was a decision about where she would stay in the meantime. It was not a decision about the facts.

Before that hearing, the court told you what the law promises: you had the right to counsel, and to appointed counsel if you could not afford one (42 Pa.C.S. § 6337), and the right to counsel at the shelter care hearing itself. (§ 6332(a)) That is how Mr. Beaumont came to be sitting beside you, and why he will be sitting beside you next Monday.

Since October there have been visits, a folder growing on your counter, and Jade asking — in the careful voice children use for large questions — when the judge part happens. Next Monday is the judge part.

**Choices:**
- Ask Mr. Beaumont to explain adjudication as if you have never been in a courtroom → **lawyer_meet**
  - NOTE (shown after choosing): You have been in a courtroom. You have never been in this one, for this question, and the difference matters.
- Bring the petition, annotated in the margins, to tomorrow's meeting → **lawyer_meet**  _(FLAG: petitionNotes)_
  - NOTE (shown after choosing): Your notes are mostly question marks. Beaumont has said, more than once, that question marks are a fine thing to bring a lawyer.

## [lawyer_meet] Mr. Beaumont and the Two Rooms
*Day 1 — Tuesday, November 24, 2026 (dayOffset 1)*

Mr. Beaumont draws a line down the middle of a legal pad. "Same building," he says, "same judge, maybe. Two different rooms, with two different rules. Everything about next Monday is knowing which room you are standing in."

Room one is adjudication. There, the court may find a child dependent only "from clear and convincing evidence" (42 Pa.C.S. § 6341(c)). The agency must prove its allegations. You do not have to prove innocence, and you do not have to prove fitness, to win. The judge decides credibility — who and what to believe — and a fact that is not proven is a fact the court cannot use.

"Room two," Beaumont says, tapping the other half of the pad, "is disposition, and we only get there if the agency proves its case in room one. Different room, different welcome for paper. That difference is your case."

**Choices:**
- Ask what actually counts as proof in room one → **two_rooms**
  - NOTE (shown after choosing): "Testimony, from people in the room, who can be questioned. And exhibits that survive being objected to. Hold on to both halves of that sentence."
- Ask why the nurse's report feels like proof if the nurse is not coming → **two_rooms**
  - NOTE (shown after choosing): Beaumont smiles without much humor in it. "Because paper is confident. Paper never has to answer a follow-up question. That is exactly the problem — for them, if we say so at the right moment."

## [two_rooms] A Report Is Not a Witness
*Day 1 — Tuesday, November 24, 2026 (dayOffset 1)*

Here is the plan, and the law under it. Written reports get their wide welcome at disposition: there, "all evidence helpful," including written reports, may be received even if it would not be competent at adjudication. (42 Pa.C.S. § 6341(d)(1)) And even at disposition, the parties may examine and controvert written reports and cross-examine the people who made them. (§ 6341(d)(2))

At adjudication, the agency will offer the nurse's report through the caseworker, Ms. Alvarado. Ms. Alvarado can testify about her own work. She did not write the nurse's note, she was not at the school that day, and she cannot answer what Jade meant. A report whose maker never appears cannot carry adjudication by itself — that is the argument counsel makes, on the record, before the report is relied on. Not in the hallway afterward. At the moment it is offered.

"So the plan has three legs," Beaumont says. "We object when the report is offered. We ask that any finding rest on testimony. And we build the testimony: you, briefly — and Mr. Danquah, who actually saw your car that night. There is a fourth thing. We find out what the nurse actually wrote."

**Choices:**
- Ask how you get what the nurse actually wrote → **records_decision**
  - NOTE (shown after choosing): "It should be sitting in the agency's own file. Files, as it happens, can be asked for."
- Ask about Mr. Danquah first — what would he even say? → **records_decision**
  - NOTE (shown after choosing): "That Jade ate at his table, and that your car was in your drive by 9:40 p.m. Short, plain, and from a man who was there. We will get to him. Paper first."

## [records_decision] Paper the Petition Didn't Quote
*Day 1 — Tuesday, November 24, 2026 (dayOffset 1)*

The agency's file should contain Mrs. Castellano's original note — the thing the petition summarized. The law on asking for it is unusually plain: the record "shall be released upon request" (55 Pa. Code § 3130.44(d)), and the rule is not to be read to protect agency employees' privacy as a basis for withholding. (§ 3130.44(f))

Beaumont is careful about what the note might say. "It might say exactly what the petition says, and then we know. But petitions are written by advocates, and nurses write like nurses — dates, quotes, maybes. If her note says less than the petition claims, Monday changes. Without it, our objection is principle without paper: right, and much harder to hand a judge."

A written request costs a stamp, copies, and days — and this is Thanksgiving week, when every office in the county runs slow. It has to go out today to have any chance of landing before Monday.

**Choices:**
- Sign the written request for the agency file today, and keep a stamped copy for your folder → **records_sent**  _(cash −10 ; FLAG: recordsRequested)_
  - NOTE (shown after choosing): One page, dated, copied, sent. Beaumont files his copy where he can put a hand on it in a courtroom.
- Hold off — pressing the agency for its file might look adversarial before the hearing → **records_skipped**
  - NOTE (shown after choosing): Beaumont writes 'no request' in the margin of the plan and underlines it once, the way you mark a sentence you expect to read again.

## [records_sent] Thanksgiving, With a Copy in the Folder
*Day 3 — Thursday, November 26, 2026 (dayOffset 3)*

Thursday is Thanksgiving. The courthouse is closed, the agency is closed, and the case — for one day — makes no sound at all. The stamped copy of your request sits in the folder on your counter, doing its slow work somewhere in a mail tray.

Jade calls from the foster home after lunch, full of turkey and somebody else's cranberry sauce, and tells you about a puzzle with a missing corner piece. You tell her Monday is the judge day, in words for an eight-year-old, and that whatever the judge decides, you will tell her the truth about it the same day.

That night you write out the timeline of the October Thursday, while it is still yours to remember plainly: the work site two hours away, the long drive back, Jade at the Danquahs' table, your car in the drive, Jade carried home asleep.

**Choices:**
- Photograph the timeline and send it to Beaumont before you sleep → **neighbor_decision**  _(FLAG: timelineWritten)_
  - NOTE (shown after choosing): His reply is two words: 'Good. Saturday?' — meaning Mr. Danquah, and whether you have actually asked him.
- Keep the timeline on paper, in the folder, for Saturday → **neighbor_decision**
  - NOTE (shown after choosing): Paper in the folder. Saturday's job is a person, not a document: the neighbor who saw your car.

## [records_skipped] Thanksgiving, Without One
*Day 3 — Thursday, November 26, 2026 (dayOffset 3)*

Thursday is Thanksgiving. The courthouse is closed, the agency is closed, and the case — for one day — makes no sound at all. Your folder is one page thinner than it could have been, and the thinness has a specific shape: somewhere in the agency's file sits a nurse's note you have never read.

Jade calls from the foster home after lunch, full of turkey and somebody else's cranberry sauce, and tells you about a puzzle with a missing corner piece. You tell her Monday is the judge day, in words for an eight-year-old, and that whatever the judge decides, you will tell her the truth about it the same day.

Beaumont leaves a voicemail in the evening, kind and blunt: "The objection on Monday still exists, Emmett. It's a good objection. But if that note says less than the petition does, we won't be able to show the judge the less. We'll only be able to say it. There's still the neighbor — he's testimony, not paper. Ask him properly."

**Choices:**
- Write out the October Thursday timeline anyway — your own memory, dated and signed → **neighbor_decision**  _(FLAG: timelineWritten)_
  - NOTE (shown after choosing): Your account, in your hand. It is not the nurse's note. It is still more than a recollection.
- Spend the quiet day on Saturday's job: figuring out how to ask Mr. Danquah properly → **neighbor_decision**
  - NOTE (shown after choosing): What 'properly' means, Beaumont said, is: in person, with the date, and with an honest account of what testifying involves.

## [neighbor_decision] The Neighbor Who Saw the Car
*Day 5 — Saturday, November 28, 2026 (dayOffset 5)*

Mr. Danquah lives next door. On the October Thursday, Jade ate dinner at his family's table and did homework with his kids while your work trip ran long, and he saw your car come into your drive by 9:40 p.m. He is not hostile to anyone in this case. He is busy — he works Saturdays at a warehouse across the county — and he has never testified to anything in his life.

Beaumont was specific about the mechanics, in the plain way that matters: a witness becomes a witness by being asked properly and early enough for counsel to arrange it. Asked properly means in person, with the actual date, and an honest description of what testifying means — an oath, questions from both lawyers, half a day at the courthouse. A man who hears all that on Saturday can be in a courtroom on Monday. A man who gets a voicemail saying 'court thing, probably?' cannot.

It is Saturday morning. His break at the warehouse is at eleven. Your car, your gas, your call.

**Choices:**
- Drive across the county on his break: ask him in person, give him the date, explain what testifying means, then call Beaumont within the hour → **neighbor_asked**  _(cash −12 ; FLAG: witnessReady)_
  - NOTE (shown after choosing): Gas and parking you could have used elsewhere. Beaumont, on the phone: 'Now he's a witness. I'll take care of the arrangements today.'
- Leave him a voicemail — 'There's a court thing Monday, you'd really help, come if you can' — and assume he'll probably come → **neighbor_assumed**
  - NOTE (shown after choosing): The message is warm, vague, and missing the courthouse, the hour, and everything testifying involves. You feel better for about an hour.

## [neighbor_asked] Asked Properly
*Day 5 — Saturday, November 28, 2026 (dayOffset 5)*

In the warehouse break room, between a vending machine and a corkboard of shift swaps, Mr. Danquah listens to the whole of it — the date, the oath, the questions from a lawyer whose job is to test what he says. He asks two practical questions, about parking and about how long, and then he puts Monday into his phone while you watch.

"Jade ate at my table," he says. "Your car was in the drive by 9:40. That is what I know, and I can say what I know." He does not offer to say more than he knows, and you understand, standing there, that this is exactly what makes him worth hearing.

Beaumont confirms it an hour later: arrangements made, witness ready, expected at the courthouse Monday morning. One leg of the plan is now standing on an actual person.

**Choices:**
- Tell Beaumont exactly what Danquah saw — the car in the drive by 9:40 p.m., Jade at his table before that — and nothing beyond it → **mail_arrives**
  - NOTE (shown after choosing): Dates, times, one man's actual knowledge. Counsel can build on that. Counsel cannot build on embroidery.
- Let Danquah tell it entirely his own way on Monday — no rehearsing beyond the date and the logistics → **mail_arrives**
  - NOTE (shown after choosing): The honest division of labor: you gave him the when and the where. The what is his, and it stays his.

## [neighbor_assumed] Probably Coming
*Day 5 — Saturday, November 28, 2026 (dayOffset 5)*

By Saturday evening there has been no callback. Mr. Danquah is on a double, his phone is in a locker, and your voicemail — warm, vague, easy to misunderstand — is sitting in it unheard while Jade's case quietly loses its only eyewitness.

Beaumont hears about it on your evening call, and there is a silence of a very specific professional length. "Emmett. 'Probably coming' is not a witness. I can only arrange testimony for a man I know about, who knows where to be and when. He's not arranged. If he walks in Monday, it's luck, and we don't build Mondays on luck."

You think about the drive you did not take, to a break room across the county, and how small it looks from Saturday night.

**Choices:**
- Text him the courthouse address and the hour anyway — a late, clear message is better than a vague one → **mail_arrives**
  - NOTE (shown after choosing): It is clearer. It is also two days late and lands in a locker phone. Hope is not an arrangement.
- Tell Beaumont the plain truth: Danquah is a hope, not a plan, and Monday's prep should assume an empty chair → **mail_arrives**
  - NOTE (shown after choosing): Candor stings and helps in the same minute. Beaumont rebuilds the plan around the record he actually has.

## [mail_arrives] Saturday's Mail
*Day 5 — Saturday, November 28, 2026 (dayOffset 5)*

Saturday's delivery — the mailbox, and Beaumont's forwarded copies — holds whatever Tuesday set in motion. A written request, sent on a Tuesday, has had four days to travel through an agency file room in a holiday week.

On your kitchen table, the prep packet from Beaumont is already open: the petition, the agency's witness list with no nurse on it, and a one-page scored summary of the assessment form that quotes the petition's version of that October night — 'left unsupervised overnight' — as if it were a settled fact about you, rather than a sentence somebody wrote.

**Choices:**
- Open the agency's packet first, and find the school nurse's original note → **note_read**  _(HIDDEN + File — school nurse's original note released on written request (§ 3130.44(d)) — three lines shorter than the petition ; REQUIRES FLAG: recordsRequested)_
  - NOTE (shown after choosing): It is there, because it was asked for, in writing, on Tuesday. Three lines, in a school nurse's careful hand.
- Go through Beaumont's prep packet — there is no agency packet, and no original note in it → **no_note**  _(REQUIRES NO FLAG: recordsRequested)_
  - NOTE (shown after choosing): Everything in the packet, you have already seen. The one document Monday turns on is in a file room you never asked to open.

## [note_read] Three Lines Shorter
*Day 5 — Saturday, November 28, 2026 (dayOffset 5)*

The nurse's original note, in full, is three lines. Jade said her dad "was gone a long time" — possibly the evening work trip, per Jade. Possibly. Per Jade. The petition took a tired eight-year-old's 'a long time,' dropped the 'possibly,' dropped the work trip, and built 'left unsupervised overnight' out of what was left.

The third line does quieter work: the missed school week — the petition's second allegation — is right there in the nurse's own note. Jade home ill that week; her father telephoned the school on the Tuesday. The absence the petition calls unexplained was explained to the school, by you, at the time, and the nurse wrote it down.

"Mrs. Castellano is not your enemy," Beaumont says on the phone. "Look at the note. She's a careful writer whose careful note got summarized by people who were not careful. On Monday, her own three lines are an exhibit — if we offer them, through counsel, at the right moment."

**Choices:**
- Ask Beaumont to have the note marked and ready to offer as an exhibit on Monday → **hearing_prep**
  - NOTE (shown after choosing): Copied, clipped, and placed where his hand will find it between the objection and the ruling. Paper, positioned.
- Read the three lines once more, and underline two words: 'possibly' and 'per Jade' → **hearing_prep**
  - NOTE (shown after choosing): The whole gap between the petition and the truth is in those two words. Monday is about making a judge read them.

## [no_note] Principle Without Paper
*Day 5 — Saturday, November 28, 2026 (dayOffset 5)*

Beaumont does not dress it up. "On Monday, our objection is correct, and it is only principle. We can argue that a report shouldn't carry adjudication without its maker. We cannot show the judge what the maker actually wrote. Judges can agree with a principle in part — strike the worst allegation — and still go looking for something smaller to rest a finding on. Paper is what stops that search."

The scored summary in the prep packet quotes the petition's version of the night, not the nurse's. Whatever the original note says — more careful, or exactly as bad — it will spend Monday in a file room, saying it to nobody.

What remains is real, and Beaumont lists it without flinching: the objection itself, your testimony, and whatever Monday brings. "We work the room we're in," he says. "Prep like it."

**Choices:**
- Ask whether Mrs. Castellano could still be called by the agency on Monday → **hearing_prep**
  - NOTE (shown after choosing): "She could — if the judge continues the session and the agency chooses to bring her. Watch for that offer from the bench. What the agency does with it is their decision, and our luck."
- Focus the prep on what can actually be proven and said on Monday, with the record that exists → **hearing_prep**
  - NOTE (shown after choosing): Timeline, testimony, objection. A shorter list than you wanted, and every item on it real.

## [hearing_prep] The Summary That Quotes the Petition
*Day 5 — Saturday, November 28, 2026 (dayOffset 5)*

One more piece of paper needs a decision before Monday: the scored summary. It is a scored assessment form's summary page, and on the supervision item it does not describe your October Thursday — it quotes the petition's sentence about it, word for word, as the thing being scored. The form has rated what the file says, and the file says the petition.

Beaumont explains the argument, with its limit attached. Under Pa.R.J.C.P. 1340(E), a party may present evidence and argument to rebut a provision, and under Rule 1340(F), factual errors may be challenged. But hear the flag he plants on it, because he plants it every time: whether Rule 1340 reaches a scored assessment summary has NOT been tested in a published opinion. It is an argument counsel makes — not a settled right anyone can promise you.

The rebuttal itself is cheap to prepare: your timeline, the Danquah arrangement, and — if it exists in your folder — three lines in a nurse's handwriting that say 'possibly.'

**Choices:**
- Have Beaumont challenge the summary's factual error under Rule 1340(E) and (F) — knowing, and saying, that the argument is untested → **adjud_morning**  _(cash −15 ; FLAG: summaryChallenged)_
  - NOTE (shown after choosing): Copies for the court and the agency, made Saturday night. The challenge may or may not be reached. It will exist, dated before the hearing, either way.
- Save every argument for the report itself on Monday — the summary is not the petition, and Monday is not long → **adjud_morning**
  - NOTE (shown after choosing): A defensible allocation of a short day. The summary's borrowed sentence goes into Monday unanswered on paper.

## [adjud_morning] Adjudication Morning
*Day 7 — Monday, November 30, 2026 (dayOffset 7)*

The courthouse on a Monday has a particular smell — floor wax, coffee, other people's worst days. Beaumont meets you at security with the folder, and runs the checklist on the walk to the courtroom, the way pilots run one: the objection moment, the witness arrangements, your testimony — brief, dated, and finished when it is finished.

He says the burden sentence one last time, because everything today hangs off it: at adjudication the agency must prove dependency by clear and convincing evidence (42 Pa.C.S. § 6341(c)). You are not on trial for being a perfect father. The petition is on trial for being proven.

Ms. Alvarado is already inside, with the agency's lawyer and a file cart. On the cart, in a folder with an exhibit sticker half-peeled, is a written report by a woman who is not in the building.

**Choices:**
- Pay the parking, take the folder from Beaumont, and go in early enough to sit down and breathe → **agency_case**  _(cash −8)_
  - NOTE (shown after choosing): Early, seated, breathing. Judges notice none of it on the record, and all of it in the room.
- Walk in with Beaumont at the call of the case, and let him carry the folder → **agency_case**
  - NOTE (shown after choosing): His folder, his checklist, your one job: say nothing until your name is called, and then say only what is true.

## [agency_case] The Agency's Case
*Day 7 — Monday, November 30, 2026 (dayOffset 7)*

Ms. Alvarado testifies first, and she testifies like what she is: a caseworker reading a case she worked, not a villain in anyone's story. Visits attended. The home in order on her checks. The week of school Jade missed in October, which the school's calls to the agency left, in her telling, unexplained. And Jade's visit to the school nurse the morning after the long Thursday — as it was reported to her.

On cross-examination, Beaumont is gentle and exact. She was not at the school that day. She has never spoken to Mrs. Castellano about the note. She did not write the nurse's report, has not brought its author, and cannot say what Jade meant by any of it. "I can only tell you what the report says," she says, honestly — which is, though she does not know it, the whole of Beaumont's closing argument, delivered early by the other side's witness.

The agency's lawyer stands. "At this point, the agency offers its casework report, incorporating the school nurse's written report of the child's statement." The judge looks at Beaumont. The room goes the particular quiet of a door about to open or close.

**Choices:**
- Watch Beaumont write a single word on his legal pad: 'Now.' → **report_offer**
  - NOTE (shown after choosing): Everything since Tuesday — the pad with two rooms, the folder, the timeline — was rehearsal for the next thirty seconds.
- Keep your hands flat on the table and let the lawyers work → **report_offer**
  - NOTE (shown after choosing): Your part of this moment is stillness. His part is a word the transcript will keep forever — if he says it.

## [report_offer] The Moment the Report Is Offered
*Day 7 — Monday, November 30, 2026 (dayOffset 7)*

This is the moment the whole week was built around, and it is smaller than you expected: no music, no pause in the proceedings, just a lawyer offering a folder and a judge glancing up. Mrs. Castellano is not on the agency's witness list. She is not in the hallway. The agency's lawyer says she is at the school, doing physicals, and that the caseworker can present the report.

If Beaumont objects now — on the record, before the report is relied on — the objection and the judge's ruling exist forever, and the report has to survive being argued about. If nobody objects, the report comes in like weather, and the hearing simply continues, with the petition's strongest sentence now resting on paper nobody in the room wrote and nobody in the room can question.

Letting it pass would feel cooperative. Beaumont said on Tuesday what cooperative silence is, in a courtroom: it is also a record. It is the record of not objecting.

**Choices:**
- Beaumont rises: "Objection. The report should not carry adjudication without its maker here to be examined." → **objection_made**  _(FLAG: objectionMade ; HIDDEN + Transcript — objection to the written report at adjudication, made and ruled on)_
  - NOTE (shown after choosing): His voice is ordinary, almost conversational. The court reporter’s fingers move. It is in the record now — all of it, whatever happens next.
- Let it pass — objecting to a school nurse's report might look uncooperative, and the judge has seen a hundred of these → **report_admitted**
  - NOTE (shown after choosing): The judge nods once and makes a note. The folder goes to the bench. Nothing in the transcript will ever mark the size of what just happened.

## [objection_made] Objection. On the Record.
*Day 7 — Monday, November 30, 2026 (dayOffset 7)*

Beaumont argues it the way he drew it on the pad. This is adjudication: the agency must prove its allegations by clear and convincing evidence. (42 Pa.C.S. § 6341(c)) The wide welcome for written reports — "all evidence helpful," received even if not otherwise competent — is the rule for disposition, the second room. (§ 6341(d)(1)) And even in that room, parties may examine and controvert written reports and cross-examine the people who made them. (§ 6341(d)(2)) Ms. Alvarado, with respect, can do none of that for Mrs. Castellano's note. She cannot say why the note says 'possibly.' She cannot say what Jade meant.

The agency's lawyer answers that school reports are the ordinary currency of these cases, that the nurse is a neutral professional, that the court can weigh the report for what it is worth. It is not a foolish argument. It is simply an argument for letting paper do a witness's work.

The judge takes the petition in one hand and the report in the other, and reads both, slowly, in the silence that court reporters render as '(pause).'

**Choices:**
- Sit still while the judge reads the petition's sentence and the report's lines side by side → **ruling**
  - NOTE (shown after choosing): Your stillness is not evidence. But the two documents, side by side on the bench, are about to become an argument all by themselves.
- Whisper to Beaumont: "Say the burden part again" — and he does, in one sentence, for the record → **ruling**
  - NOTE (shown after choosing): "The burden is the agency's, Your Honor, and it is clear and convincing. Paper that cannot be questioned cannot carry it alone." The reporter’s fingers move.

## [report_admitted] Admitted Without a Word
*Day 7 — Monday, November 30, 2026 (dayOffset 7)*

The report is admitted. The judge underlines something on its second page — you will think about that underline for a long time — and the hearing moves on to the next item as if a door had not just closed. In a sense it hasn't, visibly. That is the nature of the loss: nothing broke. A folder changed hands.

Beaumont does not look at you, which is his way of saying a true thing without words: the moment for the objection was the offer. What follows now — testimony, explanations, your whole true account of that night — will be weighed against an exhibit that nobody ever had to defend, because nobody ever made them.

Your account still matters. It will be heard. But it will be heard as an answer to the report, instead of the report being heard as a claim that needed a witness.

**Choices:**
- Testify anyway when your turn comes, and tell the whole night as plainly as you can → **findings_on_paper**
  - NOTE (shown after choosing): You tell it well. The judge listens as judges listen — and then looks back down at the exhibit, which has been sitting there, unanswered in the only way that counts, all afternoon.
- Keep your testimony brief and careful — the damage is in the exhibit, not in your demeanor → **findings_on_paper**
  - NOTE (shown after choosing): Brief and careful is usually right. Today it changes nothing about what the bench is holding.

## [ruling] Sustained, in Part
*Day 7 — Monday, November 30, 2026 (dayOffset 7)*

The ruling, when it comes, is measured — and it moves the whole case. Sustained in part: the overnight allegation cannot rest on the unexamined report. The judge will not use Mrs. Castellano's paper to prove the petition's central claim. If the agency wants that allegation proven by its author, it may call the nurse at a continued session — or it may proceed today on what it actually has.

There is a conference at the bench you cannot hear. The agency elects to proceed. Whatever Mrs. Castellano would have said — more careful than her summary, like her note, or worse for you than the petition — stays unsaid, in a school office across town. That was the agency's choice, made with the judge's offer on the table. It is also, though no one says so, the sound of a burden being carried by the side that owns it.

The report is not burned, and Beaumont never claimed it should be. If dependency is proven on something else, paper like it gets its wide welcome at disposition. But the overnight sentence now stands in this room with nothing under it — and your side's case is next.

**Choices:**
- Beaumont offers the nurse's original note through counsel, and asks the court to read all three lines → **call_witness**  _(HIDDEN + Exhibit — nurse's original note offered through counsel ; REQUIRES FLAG: recordsRequested)_
  - NOTE (shown after choosing): Marked, handed up, read. 'Possibly the evening work trip, per Jade' — in the nurse's own hand, in the record, where the petition's version used to sit alone.
- Proceed on the ruling alone — there is no original note to offer, and the objection has done its work → **call_witness**  _(REQUIRES NO FLAG: recordsRequested)_
  - NOTE (shown after choosing): The ruling stands on principle, well argued. What the nurse actually wrote remains, even now, a thing nobody in this room has read.

## [call_witness] Call the Neighbor
*Day 7 — Monday, November 30, 2026 (dayOffset 7)*

Your side of the case begins, and its first question is not legal at all. It is a question about a hallway: who is sitting in it?

Beaumont turns, the way he has turned in a hundred hearings, toward the courtroom door — toward the difference between a witness who was asked properly, in person, with the date and the truth about testifying, arranged through counsel in time… and a voicemail in a locker, sent to a man on a double shift.

He calls a name, or he doesn't. The transcript will keep whichever happened, in the same flat type it keeps everything.

**Choices:**
- Beaumont calls Mr. Danquah, who stands, takes the oath, and gives his name to the reporter → **neighbor_testifies**  _(HIDDEN + Transcript — neighbor testified: father's car in the drive by 9:40 p.m. ; REQUIRES FLAG: witnessReady)_
  - NOTE (shown after choosing): He is nervous in the ordinary way of honest people in courtrooms. He brought the parking stub Beaumont told him to keep.
- Beaumont looks at the empty hallway chair, and tells the court the defense will proceed with the testimony it has → **no_neighbor**  _(REQUIRES NO FLAG: witnessReady)_
  - NOTE (shown after choosing): No speech about it, no blame in the room. A chair, empty, doing the arguing.

## [neighbor_testifies] By 9:40, the Car Was in the Drive
*Day 7 — Monday, November 30, 2026 (dayOffset 7)*

Mr. Danquah testifies the way he said he would in the break room: only to what he knows. Jade ate dinner at his table that Thursday, did homework with his children, fell half-asleep over a board game. He saw Emmett's car come into the drive by 9:40 p.m. Minutes later Emmett was at his door, apologizing for the late hour, carrying Jade home in her socks.

On cross-examination he concedes, freely, the limits of it: he was not inside Emmett's house that evening, he cannot swear to any hour but the ones he saw. The concessions do not weaken him. A witness who will not overclaim the small things is a witness a judge can believe about the large one — and the large one is fatal to 'overnight': Jade was fed, supervised, and collected by 9:40 at night, by a neighbor, in front of a witness who has now said so under oath.

The overnight allegation — the petition's first and worst sentence — now has live testimony against it, and an unexamined report for it, which the judge has already said cannot carry it.

**Choices:**
- Thank him in the hallway during the recess — briefly, like a neighbor, not a litigant → **andre_decision**
  - NOTE (shown after choosing): He waves it off and asks if Jade can come to dinner when this is over, either way it goes. You say yes before you know whether you should have. It was the right yes.
- No celebration — the judge is still deciding credibility, and your own testimony is still to come → **andre_decision**
  - NOTE (shown after choosing): Beaumont gathers you with a look. 'Your turn. Brief. Dates. Then stop talking like your freedom depends on the next sentence — it doesn't. The record's in good shape.'

## [no_neighbor] The Empty Hallway Chair
*Day 7 — Monday, November 30, 2026 (dayOffset 7)*

Mr. Danquah is at a warehouse across the county. His phone, sometime this afternoon, will show a voicemail and a text with a courthouse address in it — both sent to a man who could not have acted on them in time, because the asking that mattered was the one that never happened in a break room on Saturday.

Beaumont does not ask for time to fetch him, and later, in the hallway, he tells you why without cruelty: the court offered the agency a continued session for its missing witness, and got a ruling in exchange. Asking for the same grace, for a witness the defense never arranged, would spend credibility the rest of your case needs. The objection still stands. The overnight allegation is still weakened. What is missing is corroboration — the difference between an allegation the agency couldn't prove with paper, and an evening the court has heard proven by a neighbor.

Your testimony is next, and it now has to carry more than it should have.

**Choices:**
- Ask Beaumont anyway whether a continuance could get Danquah here Thursday → **andre_decision**
  - NOTE (shown after choosing): His answer is honest: he can ask, the answer will almost certainly be no, and asking costs the goodwill your testimony is about to spend. He leaves the choice out of your hands by advising against it — firmly, and on the record of his own advice.
- Proceed — let the case be decided on today's record, rather than keep Jade in limbo for a maybe → **andre_decision**
  - NOTE (shown after choosing): Today's record it is: the objection, the testimony that exists, and a chair that stayed empty for logistical reasons that had nothing to do with the truth.

## [andre_decision] Emmett Takes the Stand
*Day 7 — Monday, November 30, 2026 (dayOffset 7)*

Your name is called, and the chair is harder than it looks from the gallery. Beaumont's advice, given in the hallway in the tone of a man tying a knot: testify briefly. The work site, the drive, Danquah's table, the car in the drive by 9:40, Jade carried home. Corroborate what can be corroborated, answer the cross-examination, and stop — you do not have to prove innocence, and a man re-arguing an entire petition from the witness chair starts proving things he never meant to raise.

The temptation is real, and it is not vanity. It is seven weeks of visits, a backpack by someone else's door, a sentence read four times until the page went soft — all of it wanting its say, all at once, in the one room where saying more can quietly become evidence for the other side.

The court reporter looks up. Beaumont asks his first question.

**Choices:**
- Testify briefly — the timeline, Danquah's table, the car by 9:40, Jade carried home — and then stop → **closing_strong**  _(FLAG: testifiedBriefly)_
  - NOTE (shown after choosing): Twelve minutes. Specific, dated, unadorned. On cross, nothing moves. Beaumont sits down looking like a man whose knot held.
- Re-argue the whole petition from the stand — every line, the school week, the report, the fairness of all of it → **closing_messy**
  - NOTE (shown after choosing): It pours out of you, all seven weeks of it. Some of it helps. Some of it — the phone battery, the unconfirmed arrangements, the call you might have made Tuesday or Wednesday — is new, and new, in this room, belongs to everyone.

## [closing_strong] Closing: What Was Proven, and What Wasn't
*Day 7 — Monday, November 30, 2026 (dayOffset 7)*

Closing argument, in Beaumont's hands, is not a speech. It is a map of the record, read aloud: what the agency alleged, what it proved with testimony a judge can weigh, and what it tried to prove with a folder carried into court by someone who didn't write it.

The judge retires with the file. In the hallway, Jade's foster mother texts a photograph of Jade asleep on a couch with a book open on her chest, not knowing — how could she — that three rooms away, the shape of Jade's next year is being decided by which papers are in a folder and which men and women said which words into a microphone.

Beaumont comes back down the corridor with two versions of the ask folded in his hand, because a lawyer prepares the ask the record can support — and fights, one more time, for the larger one if the record under it is real.

**Choices:**
- Ask the court to dismiss the petition: the overnight allegation is unproven, and the nurse's own note explains the school week → **end_win**  _(HIDDEN + Order — the overnight allegation is not among the findings ; REQUIRES FLAG: recordsRequested ; REQUIRES FLAG: witnessReady)_
  - NOTE (shown after choosing): This ask exists because every leg of it was built before it was needed: the objection, the note in evidence, the neighbor under oath, and testimony that corroborated instead of wandering.
- Ask the court, at minimum, to strike the overnight allegation and find only what the testimony actually proved → **end_partial**
  - NOTE (shown after choosing): The smaller ask, honestly framed: whatever else the court finds in this record, the petition's central sentence should not survive it.

## [closing_messy] Closing, After the Long Version
*Day 7 — Monday, November 30, 2026 (dayOffset 7)*

Your long testimony did one thing Beaumont feared and one thing he didn't: it was plainly sincere — no one in the room doubted you love Jade, or that the overnight sentence is wrong — and it opened doors nobody had planned to walk through. You conceded you'd never confirmed the Danquahs would be home that Thursday until Jade was already there. Your phone died on the work trip. The school call, under cross-examination, slid between Tuesday and Wednesday and stayed blurry.

None of it proves the petition's central claim, and the objection still stands guard over that claim. But a narrower set of supervision questions — coverage assumed instead of confirmed, communication left loose — now has your own sworn words to rest on, and narrower questions are what judges reach for when the large one has been taken away from them.

Beaumont's closing is shorter than planned. He salvages what the record still holds and asks, carefully, for exactly what it can bear.

**Choices:**
- Beaumont asks the court to strike the overnight allegation outright, whatever else it finds → **end_partial**
  - NOTE (shown after choosing): The allegation the nurse's report carried into this room does not survive the day. What your own testimony built, in its place, is smaller — and standing.
- Beaumont asks for outright dismissal, and presses the point that the overnight claim was the petition's core → **end_partial**
  - NOTE (shown after choosing): He is right, and it does not carry the day: the judge strikes the core, and then does the arithmetic of the narrower record your testimony left behind.

## [findings_on_paper] Findings, Written From Paper
*Day 7 — Monday, November 30, 2026 (dayOffset 7)*

The judge reads the findings in the level voice judges use for weather and for ruin. The report — admitted without objection, weighed without cross-examination of its author — does the work its author was never asked to do. The overnight sentence from the petition appears in the findings nearly word for word, because the only document that ever described that night in detail was the one nobody challenged, and the judge, deciding credibility, credits the paper over the father.

Your testimony is described in a single courteous line, as testimony from an interested party often is. Somewhere in the file, a nurse is doing afternoon physicals, unaware that her summary — possibly longer than her note, possibly not; no one ever checked — has just decided where a child will sleep.

Beaumont is quiet until the courtroom empties. Then he says the thing he will say once, and not again: "The objection existed the whole time, Emmett. It was right there. It just never got said in the room where saying it counts."

**Choices:**
- Ask him what the one word would have cost, there at the offer → **end_loss**
  - NOTE (shown after choosing): "Nothing," he says. "That's the part that will follow us. It cost nothing, and it had to be spent in about ten seconds, a month of preparation behind it."
- Hold the drawing Jade made in the visit room, and listen while the clerk reads the next dates → **end_loss**
  - NOTE (shown after choosing): Dates, in this system, are what grief gets scheduled into. The next ones are disposition dates — the second room, where the rules the report enjoys finally apply to it.

## [end_win] Dismissed — A Report Is Not a Witness
*Day 7 — Monday, November 30, 2026 (dayOffset 7)*

The order is short, the way Beaumont said the good ones are. The court finds the overnight allegation not proven — not by clear and convincing evidence, not by any evidence the court can weigh: an unexamined report, contradicted by its author's own three lines and by a neighbor under oath. What remains of the petition — the missed school week — is explained by the nurse's note itself: a sick child, a father's phone call to the school on the Tuesday, written down at the time by the agency's own witness-who-never-came.

What is not proven cannot carry a petition. The petition is dismissed and Jade is discharged (42 Pa.C.S. § 6341(a)) — the judge says the words in the level voice, and for once the level voice is reading your weather, and it is fair.

Jade comes home that evening with her backpack and the puzzle with the missing corner piece, which she presents to you as a case the household must now solve together. The folder stays on the counter a while. Paper got her into this. Paper, spoken aloud at the right ten seconds, is also what got her out.

**Ending.**

**Debrief:**
- WHAT THE FILE SAID — The hidden record of this playthrough: the agency file, released on written request, held the school nurse's original note — three lines shorter than the petition, with 'possibly' and 'per Jade' still in it (55 Pa. Code § 3130.44(d)). At the offer, an objection to the written report was made and ruled on, on the record. The note itself was offered through counsel as an exhibit. The neighbor testified that the father's car was in the drive by 9:40 p.m. And the court's order carries the cleanest item of all: the overnight allegation is not among the findings. The scored summary had quoted the petition's version of the night all along; the hearing replaced that borrowed sentence with testimony.
- THE LAW THAT CONTROLLED — Adjudication first, disposition second: the court may find a child dependent only from clear and convincing evidence (42 Pa.C.S. § 6341(c)), the agency bears that burden, and if dependency is not proven the petition is dismissed and the child discharged (§ 6341(a)). The wide welcome for written reports — 'all evidence helpful,' even if not otherwise competent — belongs to disposition (§ 6341(d)(1)), where makers of reports can still be cross-examined (§ 6341(d)(2)). The file that changed the case was obtained because the record 'shall be released upon request' (§ 3130.44(d)).
- What no strategy controlled: the agency could have taken the judge's offer and called Mrs. Castellano at a continued session — her live testimony might have clarified her note, or hardened against you, and either was possible. The judge's credibility calls, Mr. Danquah's employer letting him leave, the foster mother's kindnesses — none of that was yours to command. This ending is not a verdict that you are a flawless father. Outcomes here turn on workers, judges, resources, and luck as well as choices; this one turned, unusually cleanly, on words and paper placed in the record at the moments the law provides for them.

## [end_partial] Dependent on Less Than the Agency Asked
*Day 8 — Tuesday, December 1, 2026 (dayOffset 8)*

The judge strikes the heart out of the petition first, and says so plainly: the overnight allegation — the claim the written report carried into the courtroom — is not among the findings. A report could not do a witness's work, and on that, the day was won.

But a case is not only its worst sentence. On the narrower ground the presented record actually supported — an evening's coverage arranged by assumption instead of confirmation, a school week the evidence left only partly explained — the court finds dependency proven, by the standard the law requires, on evidence the court could weigh. Less than the agency asked for. More than nothing, and enough.

Disposition follows the next day, and it is the outcome hidden inside the disappointment: Jade comes home to you, remaining with her parent subject to conditions and supervision (42 Pa.C.S. § 6351(a)(1)) — check-ins, a supervision plan, a case that stays open while she sleeps in her own bed, with her backpack by her own door.

**Ending.**

**Debrief:**
- WHAT THE FILE SAID — The objection to the written report was made and ruled on, and it did its work: the overnight allegation was struck, and the report never carried adjudication. But the record underneath was incomplete in one of the ways records get incomplete — the nurse's original note was never obtained or never offered, or the neighbor's corroboration sat in an empty hallway chair, or the father's own testimony supplied the narrower facts himself. The scored summary, quoting the petition's version, stood unanswered in whichever gap remained, and the court built its smaller finding out of what was actually in front of it.
- THE LAW THAT CONTROLLED — The burden never moved: dependency may be found only from clear and convincing evidence (42 Pa.C.S. § 6341(c)), and the agency, not the parent, had to carry it — the overnight allegation fell because paper without its maker could not carry it, a ruling built on the line between adjudication's standard and disposition's wider welcome for written reports (§ 6341(d)(1)), where report-makers may still be examined and controverted (§ 6341(d)(2)). At disposition, the court chose the least restrictive of its listed options on these facts: the child remaining with the parent, subject to conditions and supervision (§ 6351(a)(1)).
- What no strategy controlled: how a particular judge weighs a partial record, whether the agency might have called the nurse and changed the evidence entirely, a neighbor's shift schedule, a phone battery on a work trip. A partial win is the honest arithmetic of a real hearing — the largest allegation gone, a smaller one standing, a child home under supervision. It is not a grade on Emmett as a father. Outcomes in this system turn on workers, judges, and luck alongside anything a parent does, and the part of this record that was Emmett's to build was, in the end, only partly built.

## [end_loss] Adjudicated on Paper
*Day 8 — Tuesday, December 1, 2026 (dayOffset 8)*

The adjudication stands on the report. Jade is found dependent on findings that track the petition — its central sentence included — because the one document the court was handed about that October night was a summary nobody objected to, written by a woman nobody called, about words a child said that nobody in the courtroom heard her say.

At disposition, before ordering that Jade's placement continue, the court enters its findings on the record — that continuation in the home would be contrary to her welfare, and on the reasonable efforts made to prevent removal (42 Pa.C.S. § 6351(b)) — speaking, even now, in the language of a case proven rather than a case defaulted. Jade stays where October put her. Visits continue. The folder on your counter gains an order instead of losing a case.

In the hallway afterward — the hallway version of the day, where everything is always said too late — Beaumont reconstructs the ten seconds at the offer of the report, when one word, spoken on the record, would have forced the agency to prove its central claim with a witness or lose it. The word existed the whole time. It was never spoken in the room.

**Ending.**

**Debrief:**
- WHAT THE FILE SAID — The file won this one, and the debrief has to say exactly how: the written report was admitted without objection, so there was no ruling limiting it, no transcript of an argument, nothing to weigh against it; the scored summary quoted the same borrowed version of the night and was never answered on paper; the nurse's original note was never placed in front of the judge, and no neighbor ever swore to the car in the drive by 9:40 p.m. Every corrective document in this story existed somewhere. None of them existed in the courtroom, which is the only address the court can read mail at.
- THE LAW THAT CONTROLLED — The burden was the agency's throughout: dependency only from clear and convincing evidence (42 Pa.C.S. § 6341(c)), and the father never had to prove innocence or fitness. What the agency had to prove it with was the question the unspoken objection would have put to the court — the wide welcome for written reports ('all evidence helpful,' even if not otherwise competent) is disposition's rule (§ 6341(d)(1)), and even there report-makers may be examined, controverted, and cross-examined (§ 6341(d)(2)). Unchallenged, the report was simply weighed as evidence, and it outweighed a father's denial. Before placement continued at disposition, the court entered the findings § 6351(b) requires on the record.
- What no strategy controlled: a different judge might have limited the report unasked — judges have that discretion and use it unevenly — or the agency, forced to choose, might have called the nurse and proven more, or less, than her paper did. Workers' habits, judges' instincts, and luck saturate this outcome, as they do every outcome in this system. Adjudication on paper measures a hearing, not a father's love, and the record of the next hearing in this case — unlike this one — has not been written yet. The objection, notably, still exists. It is waiting, as it waited all along, to be spoken in a room.
