# THE FIRST 90 DAYS — Scenario 69: “Answer the Question Asked”

*Human-readable script. This document and `scenario-69.json` are generated from a single source and match node-for-node: same IDs, same order, same choices, same effects.*

**The family is fictional — a composite. No real person's story appears here.**

**Content note:** This scenario depicts an adjudication hearing, including cross-examination of a parent. There is no graphic content. Players may skip any scene or use the quick exit at any time.

**How to read effects:** `cash −40` changes the player's cash. `FLAG: name` sets a flag the engine tracks. `HIDDEN + item` means the case file quietly records that item at this choice — the player does not see it when it happens. `REQUIRES FLAG: name` means the choice is only available if that flag was set earlier; `REQUIRES NO FLAG: name` means it is only available if that flag was never set. `NOTE:` is text shown to the player right after choosing.

Start date: Monday, November 9, 2026. Day offsets are days since the scenario's start date.

## [start] Three Days Out
*Day 0 — Monday, November 9, 2026 (dayOffset 0)*

Your name is Ingrid Sorensen. Your son Finn is eleven. He has been living with a foster family since Monday, October 19, 2026 — that placement happened before this story begins, and nothing in these three days changes where he sleeps tonight.

It started at school: bruises from a fall at recess became a report, the report became a petition, and the petition alleges inadequate supervision and a chaotic home. The hearing that decides whether those allegations are proven — the adjudication — is Thursday, November 12, 2026.

Your instinct, honest and complete, is to tell the judge everything. Everything you know about Finn, about that week, about yourself. Your lawyer, Ms. Nakamura, has asked you to come to her office tomorrow before you decide how much telling helps.

**Choices:**
- Go to Ms. Nakamura's office tomorrow and hear her out before you decide anything → **petition_paper**
  - NOTE (shown after choosing): Three days is not much time. It is enough time to learn the shape of the room you are walking into.
- Spend tonight writing out everything you want the judge to know, in your own words → **petition_paper**
  - NOTE (shown after choosing): The pages are heartfelt and long. You bring them with you. What Ms. Nakamura does with them surprises you.

## [petition_paper] The Petition, Line by Line
*Day 0 — Monday, November 9, 2026 (dayOffset 0)*

At home you read the petition the slow way, with a pencil. Two allegations carry the whole case: that Finn was inadequately supervised, and that the home was chaotic. The bruises are described in one paragraph. The recess fall Finn described to the school nurse is not described at all.

A petition is a list of things the county agency says it can prove. It is not proof itself. Until Thursday, every sentence in it is only a claim waiting for evidence — and the evidence, not the claim, is what the judge is allowed to use.

**Choices:**
- Mark every sentence that is a claim, and write 'evidence?' in the margin beside it → **lawyer_prep**
  - NOTE (shown after choosing): By the last page the margin is full of the same question. That question is, more or less, the hearing.
- Mark the sentences that feel unfairest, so you can answer those first → **lawyer_prep**
  - NOTE (shown after choosing): Understandable. Unfair and unproven are different words, though, and Thursday only runs on one of them.

## [lawyer_prep] The Three Rules of the Witness Chair
*Day 1 — Tuesday, November 10, 2026 (dayOffset 1)*

Ms. Nakamura clears her desk except for one chair, which she turns to face her own. "That is the witness chair," she says. "If you testify Thursday, the agency's lawyer gets to ask you questions in it. There are three rules. Listen to the whole question. Answer that question — the one that was asked. Then stop."

"Stopping is the hard one," she says. "Every extra sentence is a gift to the other side. Not because you are hiding anything. Because a volunteered sentence can become their evidence, in your voice, and they do not have to prove it anymore."

She offers to practice, question by question, until stopping feels less like silence and more like a skill.

**Choices:**
- Practice with counsel — run the hard questions until listen, answer, stop becomes a habit → **prep_rules**  _(cash +0 ; FLAG: preppedWitness)_
  - NOTE (shown after choosing): It takes an hour. Twice you explain past the answer; twice she raises one finger. By the end, the stopping is yours.
- "I'll just be honest, that's enough" — honesty, you feel, should not need rehearsing → **prep_rules**
  - NOTE (shown after choosing): Honesty matters enormously. It is also not, by itself, a strategy for cross-examination — a truthful answer and a volunteered extra fact can leave the chair in the same sentence.

## [prep_rules] Whose Job Thursday Is
*Day 1 — Tuesday, November 10, 2026 (dayOffset 1)*

"Now the part parents find hardest to believe," Ms. Nakamura says. "Thursday is not your day to prove you are a good mother. At adjudication, the court may find a child dependent only from clear and convincing evidence — and the agency is the side that has to produce it. (42 Pa.C.S. § 6341(c)) If an allegation is not proven to that standard, the court cannot use it. If the petition is not proven, it is dismissed and the child is discharged. (42 Pa.C.S. § 6341(a))"

"You do not have to prove innocence or fitness to win," she says. "They have to prove dependency. The burden starts on their side of the room, and it stays there unless the evidence moves it. Your job — if you testify at all — is to not carry their evidence in for them."

**Choices:**
- Ask her to say the burden sentence once more, and write it on the inside cover of your folder → **record_choice**
  - NOTE (shown after choosing): "Clear and convincing, and it is theirs." You will read it in the hallway on Thursday, more than once.
- Ask what happens if the judge seems to like you — does that count for anything? → **record_choice**
  - NOTE (shown after choosing): "Judges watch credibility, including yours," she says. "But liking is not the standard. Proof is. That protects you more than charm ever could."

## [record_choice] Ask for the File, in Writing
*Day 1 — Tuesday, November 10, 2026 (dayOffset 1)*

Ms. Nakamura turns to the caseworker's evidence. "Mr. Petrov will testify about his home visit. His notes are in the agency's file. The agency's record shall be released upon request. (55 Pa. Code § 3130.44(d)) I want that request in writing, today, for his visit notes specifically — what Petrov wrote at the time is worth more than what he remembers on Thursday."

"The alternative," she says, "is that I work from the summary of his visit that is already in the court report, and we trust it. Summaries are written by the side that wrote the petition."

**Choices:**
- Sign the written request for the agency record, including Mr. Petrov's home-visit notes → **notes_arrive_records**  _(FLAG: recordsRequested ; HIDDEN + File — home-visit notes released on written request (§ 3130.44(d)))_
  - NOTE (shown after choosing): One signed page, dated Tuesday, November 10, 2026. What it brings back tomorrow is a date nobody expected to argue about.
- Rely on counsel's summary of the visit — the request feels like it might antagonize the agency → **notes_arrive_summary**
  - NOTE (shown after choosing): Ms. Nakamura notes the decision without arguing. The summary says what it says. What the notes themselves say, no one on your side will know.

## [notes_arrive_records] October 21, in His Own Hand
*Day 2 — Wednesday, November 11, 2026 (dayOffset 2)*

The packet arrives Wednesday morning: Mr. Petrov's home-visit notes, released on your written request. Ms. Nakamura reads them twice, then turns the page around so you can see it.

The notes are dated Wednesday, October 21, 2026 — and they describe the visit in detail, in Petrov's own hand. That matters for a plain reason: the petition, with its description of your home already written into it, was drafted before October 21. And in the court report, Petrov's visit is described as having happened a week earlier, on October 14.

"He may testify to October 14 on Thursday," Ms. Nakamura says quietly. "His own notes say October 21. A witness corrected by his own handwriting is a different witness. We do not have to call him careless or worse. We just have to hold up the page."

**Choices:**
- Ask counsel to build Thursday's cross-examination of Petrov around his own dated notes → **summary_choice**  _(FLAG: notesDateKnown)_
  - NOTE (shown after choosing): The page goes into the folder with a tab on it. It is, Ms. Nakamura says, the best kind of evidence: theirs.
- Make a clean copy of the dated page for your own folder, and let counsel decide how to use it → **summary_choice**
  - NOTE (shown after choosing): Copy made, tab placed. Whether Thursday uses it will still depend on the questions counsel chooses to ask.

## [notes_arrive_summary] The Summary Will Have to Do
*Day 2 — Wednesday, November 11, 2026 (dayOffset 2)*

Without the written request, Wednesday brings only what was already in the court report: a short paragraph summarizing Mr. Petrov's home visit, dated October 14 in the report, describing a cluttered kitchen and a mother who seemed overwhelmed.

It may be accurate in every particular. It may not. From your side of the table there is no way to check it, because the underlying notes — what Petrov wrote at the time, with the date he wrote at the top — are still inside a file nobody asked for in writing.

"We work with what we have," Ms. Nakamura says. "On Thursday, his memory will be the only version of that visit in the room."

**Choices:**
- Read the summary paragraph three times, so at least its claims will not surprise you on Thursday → **summary_choice**
  - NOTE (shown after choosing): No surprises is worth something. It is not the same as something to cross-examine with.
- Ask counsel one more time whether it is too late to request the notes — and accept her answer that Thursday will not wait → **summary_choice**
  - NOTE (shown after choosing): She is right about the calendar, which is exactly why the request mattered on Tuesday. The hearing is tomorrow.

## [summary_choice] Supervision: Unclear
*Day 2 — Wednesday, November 11, 2026 (dayOffset 2)*

The last pages of the court report hold the scored summary — a scored assessment form, filled in from the file, that the judge will likely read before anyone speaks on Thursday. On supervision it says one word: "unclear." Under it, two factual statements support the rating, and both are wrong in checkable ways: a neighbor who watches Finn after school is listed as "no identified caregiver," and a single missed check-in call is listed as a pattern.

Ms. Nakamura explains the argument counsel can make: under Pa.R.J.C.P. 1340(E) a party may present evidence and argument to rebut a provision, and under Rule 1340(F) factual errors may be challenged. She is equally plain about the limit: whether Rule 1340 reaches a scored assessment summary has NOT been tested in a published opinion — it is an argument counsel makes, not a settled right.

"Untested is not the same as useless," she says. "A short written rebuttal, filed through me, with the two facts and their dates, gives the judge a reason to read that word 'unclear' with care. Leaving it alone leaves it standing as the first thing the judge learns about you."

**Choices:**
- File the one-page written rebuttal through counsel, answering the two factual errors with dates → **eve_prep**  _(FLAG: rebuttalFiled ; HIDDEN + Rebuttal — two factual errors in the scored summary answered in writing (Rule 1340(E)/(F) — untested))_
  - NOTE (shown after choosing): Filed Wednesday, November 11, 2026, with the untested flag stated in counsel's own filing. The word 'unclear' now has company in the report.
- Leave the summary alone — an untested argument feels like a risk you do not need → **eve_prep**
  - NOTE (shown after choosing): The caution is real, and the cost is quiet: the summary goes to the judge exactly as written, unanswered, first.

## [eve_prep] The Night Before
*Day 2 — Wednesday, November 11, 2026 (dayOffset 2)*

Wednesday evening is logistics, not law: clothes laid out, the folder by the door, the bus route checked twice. Ms. Nakamura's last instruction by phone is not about evidence at all. "Eat something. Sleep if you can. Judges watch credibility, and credibility starts with a witness who is present, not performing."

You practice the three rules once, out loud, to the empty kitchen: listen; answer that question; stop. The stopping still feels strange. It also, for the first time, feels possible.

**Choices:**
- Set the alarm early, put the folder by the door, and get what sleep you can → **call_finn**
  - NOTE (shown after choosing): Preparation, at this point, is mostly a quiet house and a charged phone.
- Stay up re-reading the petition until the allegations have lost their power to startle you → **call_finn**
  - NOTE (shown after choosing): By midnight the words are familiar, which was the point. Sleep, when it comes, is thinner than counsel advised.

## [call_finn] A Phone Call, Supervised and Short
*Day 2 — Wednesday, November 11, 2026 (dayOffset 2)*

The scheduled call lasts twelve minutes. Finn tells you about a spelling test, a loose tooth that is not loose yet, and the foster family's cat, who sleeps on the laundry and is, Finn reports, "in charge."

He asks when he is coming home. You tell him the truth in the size an eleven-year-old can carry: grown-ups are meeting tomorrow to talk about it, his teacher will be there, and you will tell him what happens as soon as you know. You do not promise him an outcome no one has promised you.

Afterward the house is very quiet. Tomorrow, strangers will argue about your home in a room built for arguing. Tonight it is just a home with his shoes still by the door.

**Choices:**
- Write down what Finn said about school and the recess fall, with tonight's date, and add it to the folder → **court_morning**
  - NOTE (shown after choosing): Dated, in your hand, before the hearing — not a memory reconstructed after it.
- Leave the folder closed tonight; tomorrow will add enough paper on its own → **court_morning**
  - NOTE (shown after choosing): True enough. The folder by the door is already heavier than it was on Monday.

## [court_morning] The Hallway Outside the Courtroom
*Day 3 — Thursday, November 12, 2026 (dayOffset 3)*

Thursday, November 12, 2026. The courthouse hallway smells of floor cleaner and other people's worst days. Mr. Petrov arrives with a file box. Finn's teacher arrives alone, early, holding a folder of her own and looking like she would rather be in her classroom — which, Ms. Nakamura murmurs, is usually what an honest witness looks like.

Ms. Nakamura reviews the order of battle: the agency goes first, because the burden is theirs. Petrov, then the teacher. Then your side decides whether you testify. "Nothing about today requires you to fill a silence," she says. "Remember whose job the proving is."

**Choices:**
- Take the early bus in, arrive with time to spare, and read the burden sentence in the hallway → **adjud_open**  _(cash −6)_
  - NOTE (shown after choosing): Early, seated, breathing. Credibility, Ms. Nakamura says, starts before the first question.
- Drive in and pay for parking, rereading the petition in the car until the doors open → **adjud_open**  _(cash −12)_
  - NOTE (shown after choosing): The allegations are no more proven in the parking garage than they were at your kitchen table. The hearing will decide that, not the rereading.

## [adjud_open] The Judge States the Standard
*Day 3 — Thursday, November 12, 2026 (dayOffset 3)*

The judge opens the adjudication plainly, the way judges do when they know a parent in the room has never heard it: this hearing decides whether the agency has proven, by clear and convincing evidence, that Finn is a dependent child. (42 Pa.C.S. § 6341(c)) Allegations alone are not evidence. Witnesses and admitted documents are.

The judge's eyes move around the room as she speaks — to the agency's lawyer, to Petrov, to you. Ms. Nakamura had told you: this judge watches credibility more than paper. Watching the judge watch the room, you understand that paper and credibility are about to become the same thing — a date on a page, a witness who stands by it or does not.

**Choices:**
- Listen for the burden in every question the agency asks — whose proof is this, and is it clear and convincing? → **agency_case**
  - NOTE (shown after choosing): It changes how the morning sounds. Claims arrive labeled, in your ear, as claims.
- Watch the judge's face during the openings, to learn what she seems to care about → **agency_case**
  - NOTE (shown after choosing): What she cares about, visibly, is whether witnesses say only what they actually know. Noted.

## [agency_case] Mr. Petrov Testifies
*Day 3 — Thursday, November 12, 2026 (dayOffset 3)*

The agency calls Mr. Petrov first. He is not a villain in the telling and you should not need him to be: he is a caseworker with a full caseload, testifying from memory and a file, about a visit he made weeks ago.

He describes your kitchen on the day of his home visit — dishes, laundry, a tired mother — and he dates the visit, with the confidence of a man reading it off an internal page: "That was October 14." On supervision, he says Finn's after-school arrangements were "never clear to me," and the scored summary's word — unclear — enters the record in a human voice.

What he does not offer is any direct evidence that Finn was left alone and unsupervised. Listening for it, burden in your ear, you notice its absence the way you would notice a missing step on a stair.

**Choices:**
- Pass Ms. Nakamura a note with one word on it: the date → **petrov_cross_choice**
  - NOTE (shown after choosing): She does not nod. Lawyers in hearings rarely do. But her pen moves to the tabbed page in the folder.
- Sit on your hands and let counsel run her own cross-examination her own way → **petrov_cross_choice**
  - NOTE (shown after choosing): Also a discipline. The cross that follows is hers to build — from whatever material your side actually holds.

## [petrov_cross_choice] Cross-Examination: The Date
*Day 3 — Thursday, November 12, 2026 (dayOffset 3)*

Ms. Nakamura stands for cross-examination. This is the hinge the whole week built: what can she actually put in front of this witness?

If your side holds Petrov's own notes, she can do the quietest, strongest thing in a courtroom — hand a witness his own handwriting and ask him to read the date at the top. If your side holds only the report's summary, October 14 stands unchallenged, because there is nothing in your folder to challenge it with.

She looks at the folder, and chooses.

**Choices:**
- Cross on the date — hand Petrov his own notes and ask him to read the date he wrote: October 21, not October 14 → **petrov_crossed**  _(HIDDEN + Transcript — caseworker's visit date corrected on cross-examination (October 21, not October 14) ; REQUIRES FLAG: recordsRequested)_
  - NOTE (shown after choosing): No raised voice. One page, one date, read aloud by the man who wrote it. The judge writes something down.
- Cross on the visit itself — what he saw, how long he stayed, what Finn was doing → **petrov_uncrossed**
  - NOTE (shown after choosing): Fair questions, and he answers them steadily. The description of the kitchen survives cross intact.
- Ask nothing — save counsel's energy for the teacher and the closing → **petrov_uncrossed**
  - NOTE (shown after choosing): Petrov steps down with every sentence he arrived with, including the date, exactly as he delivered it.

## [petrov_crossed] Corrected by His Own Handwriting
*Day 3 — Thursday, November 12, 2026 (dayOffset 3)*

"Mr. Petrov, your notes of that visit — the notes you wrote — are dated what day?" A pause that fills the room. "October 21." "Not October 14?" "The notes say October 21. I must have misspoken."

Ms. Nakamura asks one more question and no more: whether the petition's description of the home was already drafted before October 21. Petrov looks at his file, and agrees that it was. She sits down.

Nothing dramatic has happened, and something important has: the agency's central witness has been corrected, on the record, by his own contemporaneous notes, on a fact the petition was built around. The judge watched the correction happen. Credibility, in this room, just moved — and it did not move because anyone called Petrov a liar. It moved because a date was a date.

**Choices:**
- Keep your face still and your eyes on the judge — let the moment stay the size counsel made it → **teacher_node**
  - NOTE (shown after choosing): Stillness, here, is testimony of a kind too: a mother who lets the record speak.
- Write 'Oct 21 — his notes' in your folder, dated and timed, while the words are fresh → **teacher_node**
  - NOTE (shown after choosing): Your own record, made the same way his was: at the time, in writing.

## [petrov_uncrossed] October 14 Stands
*Day 3 — Thursday, November 12, 2026 (dayOffset 3)*

The cross-examination ends without the date ever moving. Petrov's account — the visit on October 14, the kitchen as he described it, supervision 'never clear' — stands in the transcript exactly as he delivered it.

Ms. Nakamura is not careless and neither are you; there was simply nothing in your side's folder to put against his memory. A cross-examination cannot invent its material. It can only use what was gathered before the hearing, in writing, on time.

The agency's case is not stronger than it was an hour ago. It is exactly as strong as it was — which, with the date uncorrected, may be strong enough for part of it.

**Choices:**
- Take the lesson in the form it arrived: paper gathered before a hearing is the hearing → **teacher_node**
  - NOTE (shown after choosing): A hard sentence to learn at a counsel table. It will not be the last hearing this lesson is true at.
- Focus forward — the teacher is next, and her testimony has limits of its own → **teacher_node**
  - NOTE (shown after choosing): True. An honest, limited witness cuts in the direction of whatever the limits are.

## [teacher_node] The Teacher, Honest and Limited
*Day 3 — Thursday, November 12, 2026 (dayOffset 3)*

Finn's teacher testifies the way Ms. Nakamura predicted an honest witness would: carefully, and only about what she knows. The bruises, she says, were consistent with what Finn and two classmates described — a fall off the climbing structure at recess, witnessed, logged by the school nurse the same day. She reported what procedure required her to report. She has never been in your home. She knows nothing about Finn's supervision after school, in either direction.

She also says, because it is true and she was asked, that Finn is a settled, funny, well-kept child in her classroom, whose mother has never missed a school meeting.

The agency's second witness, examined honestly, has proven the recess fall and very little else. The supervision allegation still has no direct witness. It has a word in a summary — unclear — and a caseworker's impression.

**Choices:**
- Have counsel cross gently, to lock in the recess account and the limits: nurse's log, same day, no home knowledge → **agency_rests**
  - NOTE (shown after choosing): Three short questions. The teacher agrees with all of them, because they are simply what she already said, arranged.
- Ask the teacher nothing — she has helped by being exactly as limited as she is → **agency_rests**
  - NOTE (shown after choosing): Also defensible: nothing she said needs rescuing, and a grateful silence can be its own cross-examination.

## [agency_rests] The Agency Rests
*Day 3 — Thursday, November 12, 2026 (dayOffset 3)*

"The agency rests." Four words, and the shape of the case is suddenly measurable. What the agency has proven, and what it has only alleged, are now two different piles on the table — and everyone in the room, including the judge, can see the size of each.

The bruises: explained by a recess fall, on the agency's own witness. The home: described by one witness, on a visit whose date may or may not still be standing. Supervision: a word — unclear — and no witness who saw Finn left alone. Clear and convincing is a high pile to build. Whether theirs reaches it is the judge's call, after closings.

First, one decision remains, and it is yours: whether to testify.

**Choices:**
- Talk it through with Ms. Nakamura in the hallway before you decide — five minutes, honestly used → **testify_choice**
  - NOTE (shown after choosing): "You don't need to testify to win," she says. "If you do, the cross is the price. Decide about the price, not about whether you have something to say. You always have something to say."
- Decide from the counsel table, on what the agency's case actually turned out to be → **testify_choice**
  - NOTE (shown after choosing): Measured against the two piles on the table, the decision looks different than it did in the hallway this morning.

## [testify_choice] Whether to Take the Chair
*Day 3 — Thursday, November 12, 2026 (dayOffset 3)*

Ms. Nakamura lays out the fork without decoration. If you testify, your account goes on the record in your own voice — Finn's after-school neighbor, the school meetings, the ordinary order of your home — and then the agency's lawyer cross-examines you, and every word you say, including every extra word, becomes evidence anyone may use.

If you rest, your side stands on the agency's evidence and the burden: they had to prove it, and the argument is that they did not. Resting is not surrender. It is a position about whose job Thursday was.

There is no choice here that a good mother makes and a bad mother does not. There is only the choice whose mechanics you understand.

**Choices:**
- Testify — give your account on direct, and take the cross-examination at its price → **testify_direct**
  - NOTE (shown after choosing): You walk to the chair you practiced facing. It is smaller than it looked from counsel's desk. Most important chairs are.
- Rest on the agency's evidence — the burden was theirs, and your side will argue it was not carried → **closing_main**
  - NOTE (shown after choosing): A principled position, held by many lawyers in many rooms. The transcript of your case will contain no sentence in your voice — for better and for worse.

## [testify_direct] Direct Examination: Your Voice, Arranged
*Day 3 — Thursday, November 12, 2026 (dayOffset 3)*

Ms. Nakamura's direct examination is the practiced one: short questions, your short answers. The neighbor, named, who has Finn after school until you are home. The school meetings, all of them. The recess fall, as Finn told it to you that night, ice pack and all. The ordinary, unglamorous order of a home that contains an eleven-year-old and a working mother.

You sound, to your own ears, almost too plain. That, counsel had said, is what credible sounds like from the inside. The judge is listening the way she listened to Petrov — for the edges of what a witness actually knows.

Then direct ends, and the agency's lawyer stands up with a legal pad and a different tone, and the real test of Tuesday's practice begins.

**Choices:**
- Take a breath, find the judge's clock on the wall, and listen for the first whole question before answering anything → **cross_exam**
  - NOTE (shown after choosing): Listen. Answer that question. Stop. The rules fit on an index card. Living them is the hearing.
- Remind yourself why you are in this chair: Finn, and nothing else, in either direction → **cross_exam**
  - NOTE (shown after choosing): Love brought you to this chair. Whether love helps here depends entirely on whether it can stop talking when the answer is done.

## [cross_exam] Cross-Examination: Answer the Question Asked
*Day 3 — Thursday, November 12, 2026 (dayOffset 3)*

The agency's lawyer is polite, which is the dangerous kind. The questions come in a rhythm designed to loosen a witness: yes-or-no questions with a story tucked inside them. "You'd agree Finn needs watching at all times?" "And there were evenings this fall when your schedule was tight?" "And you're the kind of mother who would tell this court everything, isn't that right?"

Twenty-one questions, if anyone counts them later. Each one can be answered truly, briefly, and completely — the question that was asked, and nothing volunteered around it. Or a witness can do the most natural thing in the world for a mother in that chair: explain. Explain everything, all at once, so the judge will finally KNOW her.

The trap in this room is not foolishness. It is love, talking past the end of an answer.

**Choices:**
- Answer each question asked — truly, briefly — and then stop, twenty-one times in a row → **cross_done**  _(FLAG: answerDiscipline ; HIDDEN + Transcript — parent testified; answered twenty-one questions; volunteered nothing ; REQUIRES FLAG: preppedWitness)_
  - NOTE (shown after choosing): It feels, each time, like leaving something unsaid. That feeling is the price — and the whole point — of Tuesday's practice.
- Answer honestly but at length, explaining the context around each question so nothing is misunderstood → **rambled_node**
  - NOTE (shown after choosing): Nothing you say is untrue. Much of it was not asked. The judge listens to all of it, and so does the transcript.
- Volunteer the full explanation: "I only left him once, and that was the night the car—" — tell them everything, so they finally know you → **volunteered_node**
  - NOTE (shown after choosing): You mean it as honesty, and as love. Hear, as it leaves you, what it is in this room: the supervision allegation's first direct support, supplied by the only witness who had it.

## [cross_done] Twenty-One Questions, Nothing Volunteered
*Day 3 — Thursday, November 12, 2026 (dayOffset 3)*

"No further questions." The agency's lawyer sits down with a legal pad that has not gained the page he was hoping for.

Your testimony stands in the transcript the way counsel built it on Tuesday: an account, given plainly, cross-examined fully — and not one volunteered sentence for the agency to carry into its closing. The supervision allegation still has no direct witness. It has a summary word and an impression, and now it has your sworn, specific account of the neighbor arrangement standing against them, unexploded by any extra fact.

Ms. Nakamura, gathering her notes for closing, says the quiet part at counsel-table volume: "Now we argue about what they proved. Not about what you are."

**Choices:**
- Ask counsel to close exactly there — on the burden, and on the elements that were never proven → **closing_main**
  - NOTE (shown after choosing): She was always going to. Now the record lets the argument land at its full weight.
- Sit down, drink the water, and let the hearing become lawyers talking about a record you helped keep clean → **closing_main**
  - NOTE (shown after choosing): Your part of the record is finished. That it is finished — that it stops where you stopped — is its strength.

## [volunteered_node] The Sentence That Kept Going
*Day 3 — Thursday, November 12, 2026 (dayOffset 3)*

It started as the most honest sentence in the room: you only left him once. You were explaining — the car, the night, the neighbor who was supposed to be home, how it was forty minutes and never again and how you have thought about it every day since.

Every word of it may be true, and all of its context may matter, and none of that changes what just happened mechanically: before that sentence, no witness had directly supported the claim that Finn was left unsupervised. The agency's lawyer had asked about schedules in the abstract because the abstract was all he had. Now he has a specific night, a specific duration, and a specific admission — in the transcript, in your voice, requiring no further proof from anyone.

Ms. Nakamura does not look angry. She looks like a lawyer watching a burden quietly change hands in the middle of a sentence, and doing the arithmetic of what a closing can still honestly say.

**Choices:**
- Finish the answer as truthfully as it began, and do not compound it by arguing with the next question → **closing_loss**
  - NOTE (shown after choosing): What is said is said. The closing will be about what one night, admitted and explained, should and should not carry.
- Try, on the next question, to take the explanation back into context all at once → **closing_loss**
  - NOTE (shown after choosing): The attempt is heartfelt and adds two more sentences to the same page of the transcript. Context, in a record, rarely subtracts.

## [rambled_node] True, Long, and Everywhere
*Day 3 — Thursday, November 12, 2026 (dayOffset 3)*

Your cross-examination was honest in every sentence and disciplined in almost none of them. Answers wandered into context, context wandered into other weeks, other weeks wandered into explanations of people who were not in the room. Nothing you said admitted the supervision allegation outright — but the account that was so plain on direct is now tangled, in the transcript, with weeks nobody asked about.

The judge, who watches credibility more than paper, watched a witness who could not seem to find the end of an answer. That is not a finding. It is an impression, and impressions are the weather in which findings get made.

One allegation — the chaotic home, as Petrov described it — now feels, to the room, easier to credit than it did an hour ago. The supervision allegation still lacks a direct witness. Both of those things will matter in the closing, in opposite directions.

**Choices:**
- Let counsel use the closing to pull the record back to the burden and the unproven elements → **closing_main**
  - NOTE (shown after choosing): It is the strongest argument left, and it is a real one — the agency's proof did not grow just because your answers did.
- Ask counsel, quietly, whether your testimony hurt — and accept her honest answer that it complicated things → **closing_main**
  - NOTE (shown after choosing): "Complicated, not decided," she says. "Closings exist for complicated." It is not comfort. It is accurate, which is her form of it.

## [closing_main] Closing: The Burden, or Fairness
*Day 3 — Thursday, November 12, 2026 (dayOffset 3)*

Closing argument is where counsel tells the judge what the record — the whole record, and nothing outside it — adds up to. Ms. Nakamura has two closings available to her, and they are not the same speech.

One closing walks the standard: the agency had to prove dependency by clear and convincing evidence (42 Pa.C.S. § 6341(c)); element by element, here is what was proven, here is what was only alleged, here is a witness corrected by his own notes, here is an allegation with no direct witness at all. If the petition is not proven to that standard, it is dismissed. (42 Pa.C.S. § 6341(a))

The other closing argues fairness: a good mother, a hard fall at recess, a system that moved too fast. It is all true, and Ms. Nakamura says it to you plainly in the hallway of this decision: "Fairness is not the standard, Ingrid. The burden is. Fairness asks the judge to feel something. The burden requires the other side to have done something — and lets us count, precisely, whether they did."

**Choices:**
- Close on the burden — element by element, the corrected date, the unproven supervision allegation, nothing volunteered to fill the gaps → **end_win**  _(HIDDEN + Order — petition dismissed; no findings made against the parent ; REQUIRES FLAG: recordsRequested ; REQUIRES FLAG: preppedWitness ; REQUIRES FLAG: answerDiscipline)_
  - NOTE (shown after choosing): Every premise of this closing was built before it was spoken: a request on Tuesday, a practice hour, a tabbed page, twenty-one stopped answers.
- Close on the burden generally — the agency's proof, as it stands, does not reach clear and convincing on the whole petition → **end_partial**
  - NOTE (shown after choosing): A sound argument on a thinner record. The judge will weigh it against everything that survived cross-examination uncorrected.
- Close on fairness — the judge should hear what kind of mother you are, and how this case began → **end_partial**
  - NOTE (shown after choosing): The judge hears it, and is not unmoved. Moved, however, is a feeling. The ruling will be written in the language of proof.

## [closing_loss] Closing After the Admission
*Day 3 — Thursday, November 12, 2026 (dayOffset 3)*

Ms. Nakamura closes as well as this record allows anyone to close. She walks the burden faithfully: clear and convincing evidence, element by element (42 Pa.C.S. § 6341(c)). She is careful, and she is honest, and at the supervision element she has to spend her time where no closing wants to spend it — arguing about the weight of a fact rather than its absence.

Because the fact is no longer absent. It is in the transcript in your own voice, explained and contextualized and entirely real, and the agency's closing needs only to read it back. Their lawyer does, once, without embellishment. He does not have to embellish it.

The judge thanks both counsel, looks once at you — not unkindly — and takes the matter under advisement for the ruling.

**Choices:**
- Hear the agency's closing read your own sentence back, and understand exactly what Tuesday's third rule was for → **end_loss**
  - NOTE (shown after choosing): Listen; answer that question; stop. The rules were never about hiding. They were about whose evidence your voice becomes.
- Hold on to what is also true: one admitted night was explained, contextualized, and never repeated — and closings can argue weight → **end_loss**
  - NOTE (shown after choosing): Counsel argued exactly that, well. Weight arguments matter. They start, though, from a fact the other side no longer has to prove.

## [end_win] Not Proven — The Burden Stayed Where It Belongs
*Day 4 — Friday, November 13, 2026 (dayOffset 4)*

The order arrives Friday, November 13, 2026, and it is short in the way rulings are short when the reasoning was done in the hearing: the agency did not prove the petition by clear and convincing evidence. The supervision allegation had no direct witness and, against it, a specific sworn account. The home-visit evidence was materially weakened when the caseworker's own notes corrected his date. The petition is dismissed. (42 Pa.C.S. § 6341(a))

No findings are made against you. Finn comes home that day — home, not on conditions, not under a plan, because there is no adjudication to build a disposition on. His shoes go back by the door, next to yours, in a house the record now describes the way Thursday left it: alleged, examined, and not proven.

**Ending.**

**Debrief:**
- WHAT THE FILE SAID — The hidden record on this route: the home-visit notes were released on written request (55 Pa. Code § 3130.44(d)) and showed October 21, not the October 14 the court report carried; Mr. Petrov was corrected by that date on cross-examination, on the transcript; the scored summary's "supervision: unclear" rating was answered in writing, its two factual errors named with dates; and the parent's own testimony ran to twenty-one cross-examination questions with nothing volunteered. The order that ended it — petition dismissed, no findings made against the parent — was built out of those four pieces of paper and restraint, in that order.
- THE LAW THAT CONTROLLED IT — At adjudication the court may find a child dependent only from clear and convincing evidence, and that burden is the agency's: the parent does not have to prove innocence or fitness to win. (42 Pa.C.S. § 6341(c)) Where the petition is not proven to that standard, it is dismissed and the child is discharged. (42 Pa.C.S. § 6341(a)) The agency record that supplied the impeachment was released on written request. (55 Pa. Code § 3130.44(d)) The written rebuttal of the scored summary was argued under Pa.R.J.C.P. 1340(E) and (F) — an argument whose reach to a scored assessment summary has NOT been tested in a published opinion, and which helped here, at most, as careful reading, not as a settled right.
- THE HONEST PART — This ending turned on a date in a caseworker's own notes, a practice hour, and a mother who could stop talking in a chair built to make mothers talk. A different judge might have weighed Petrov's correction less heavily; a different caseworker might have written a different date, or none; the recess fall had an honest teacher and a nurse's log, which is luck as much as anything. Dismissal is not a verdict that you are a perfect parent, and the other endings are not verdicts that you are a bad one. Outcomes here turn on workers, judges, resources, and luck — this one also turned on the burden staying exactly where the law put it, because nobody carried the other side's evidence across the room for them.

## [end_partial] Dependent, But Home
*Day 3 — Thursday, November 12, 2026 (dayOffset 3)*

The ruling comes from the bench, in two halves. One allegation — the condition of the home as the caseworker described it, on a visit date that stood as he gave it, or against a record thinned by unfocused testimony — is found proven by clear and convincing evidence. The supervision allegation, with no direct witness behind it, is not proven, and the court says so.

One proven allegation is enough for dependency, and Finn is adjudicated dependent. Then the case moves, the same day, to what follows from that finding — and here the second half of the ruling matters: Finn is returned to your home, subject to conditions and supervision by the agency, rather than remaining in placement while services run. You leave the courthouse with your son, a list of conditions, and a case that is still open — a real outcome, and a partial one, and both halves of that sentence are true at once.

**Ending.**

**Debrief:**
- WHAT THE FILE SAID — The hidden record on this route was thinner, and the ruling maps it exactly: the caseworker's October 14 date and kitchen description stood uncorrected if the visit notes were never requested in writing; the scored summary's "supervision: unclear" stood unanswered if no written rebuttal was filed; and testimony that rambled, or a decision to rest, left less in the transcript to set against the agency's account. What saved the second half of this ending was what also survived: the supervision allegation never gained a direct witness — no volunteered admission supplied it — and the teacher's honest, limited testimony proved a recess fall, not a chaotic home.
- THE LAW THAT CONTROLLED IT — Dependency requires clear and convincing evidence (42 Pa.C.S. § 6341(c)), allegation by allegation: an allegation not proven to that standard cannot be used, and here the supervision allegation was not proven — but one proven allegation sufficed for adjudication. At disposition, among the options available to the court is allowing the child to remain with the parent subject to supervision and to conditions the court prescribes. (42 Pa.C.S. § 6351(a)(1)) That is this ending's legal shape: dependent, but home. The rebuttal argument under Pa.R.J.C.P. 1340(E) and (F), where it was made, remains what it always was — NOT tested in a published opinion as applied to a scored assessment summary.
- THE HONEST PART — A partial outcome is not a grade halfway between good mother and bad mother. It is a map of a record: which pieces of paper existed on Thursday, which corrections were in the folder, how a particular judge weighed a caseworker's uncorrected memory. A different worker's notes, a different judge's credibility call, a bus that ran late on the morning a request had to be filed — the same mother lands elsewhere. What a parent controls is narrower and real: ask for the record in writing, practice stopping, and let the agency carry its own burden. The rest turns on workers, judges, and luck.

## [end_loss] Dependent — Every Word Counted Twice
*Day 3 — Thursday, November 12, 2026 (dayOffset 3)*

The ruling is careful, and it quotes you. On supervision — the allegation the agency had supported, all morning, with a word in a summary and a caseworker's impression — the court now has direct evidence: your own testimony, given fully and honestly, about the one night you left Finn, and the court finds that allegation proven by clear and convincing evidence, substantially on your words. With it, the home-condition allegation is credited as well.

Finn is adjudicated dependent, and his placement with the foster family continues, with services and a plan and dates to work toward. Nothing about you has been found monstrous, or even unusual. The order reads, in its quiet way, like what it is: a case the agency had not finished proving, finished — in the transcript, in a mother's voice, by a mother trying to be fully known.

Ms. Nakamura walks you out. "Their case did not get better today, Ingrid," she says, finally. "The transcript did. That is a different thing, and it is the thing we practiced against."

**Ending.**

**Debrief:**
- WHAT THE FILE SAID — The decisive hidden item on this route is a single transcript page: on cross-examination, the parent volunteered — beyond any question asked — the one night Finn was left alone, supplying the supervision allegation's only direct support. Everything else in the file stayed as it was: the caseworker's testimony, corrected on his visit date or not; the scored summary rating supervision "unclear"; the teacher's recess-fall account. None of that, by itself, was the agency's strongest evidence. The volunteered admission was, because an admitted fact needs no further proof, and a parent's own words are counted twice in a courtroom — once as testimony, and once as a concession the other side never had to earn.
- THE LAW THAT CONTROLLED IT — The burden never moved in law: at adjudication the agency must prove dependency by clear and convincing evidence, and the parent does not have to prove innocence or fitness. (42 Pa.C.S. § 6341(c)) What moved was the evidence available to carry that burden — testimony is evidence, volunteered testimony emphatically included, and a court finding dependency on proven allegations proceeds to disposition, where continued placement is among the outcomes the court may order. The agency record, where it was requested, was released on request (55 Pa. Code § 3130.44(d)); the Rule 1340(E)/(F) rebuttal of the scored summary, where it was filed, remains an argument NOT tested in a published opinion. None of those rules failed here. A sentence simply joined the agency's side of the ledger.
- THE HONEST PART — Hear this the way the scenario means it: the volunteered sentence was not foolish, and it was not a lie, and it was not bad parenting in the telling — it was a mother trying to be fully honest in a chair that punishes extra honesty with permanence. The trap is structural, not moral. It is also not the whole future: adjudication is not termination, placement continues under a plan with hearings ahead, and parental rights, if they are ever challenged, would likewise have to be proven by clear and convincing evidence. Outcomes turn on workers, judges, and luck — and, on this route, on one true sentence that a different kind of love, the practiced kind, would have left for the agency to try to prove on its own.
