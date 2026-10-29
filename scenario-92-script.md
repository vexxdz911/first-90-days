# THE FIRST 90 DAYS — Scenario 92: “Heard, Not a Party”

*Human-readable script. This document and `scenario-92.json` are generated from a single source and match node-for-node: same IDs, same order, same choices, same effects.*

**The family is fictional — a composite. No real person's story appears here.**

**Content note:** This scenario depicts a kinship caregiver preparing to be heard at her granddaughter's permanency hearing. There is no graphic content. Players may skip any scene or use the quick exit at any time.

**How to read effects:** `cash −40` changes the player's cash. `FLAG: name` sets a flag the engine tracks. `HIDDEN + item` means the case file quietly records that item at this choice — the player does not see it when it happens. `REQUIRES FLAG: name` means the choice is only available if that flag was set earlier; `REQUIRES NO FLAG: name` means it is only available if that flag was never set. `NOTE:` is text shown to the player right after choosing.

Start date: Monday, October 5, 2026. Day offsets are days since the scenario's start date.

## [start] The Notice in the Mailbox
*Day 0 — Monday, October 5, 2026 (dayOffset 0)*

Your name is Philomena Rios. You are sixty-one, retired from the school cafeteria where you fed two generations of other people's children, and for eight months your granddaughter Solana, eight, has lived in your second bedroom — placed with you by the court as a kinship resource when her mother's case began.

Today's mail holds a hearing notice with your name on it, and that itself is a piece of law: as Solana's resource caregiver, you are entitled to notice of her permanency hearing and an opportunity to be heard at it (42 Pa.C.S. § 6336.1). The hearing is November 16. What the notice does not say — what a clinic lawyer will have to tell you, in the gentlest available wording — is everything you are not entitled to.

Last week, Solana's caseworker mentioned, in the doorway, in the tone of weather, that the agency is 'looking at placement options with full licensure.' Solana's desk, her school, her mother's Sunday visits at your table, are all in this house. The weather is changing.

The family is fictional — a composite. The doorway remark is a documented genre.

**Choices:**
- Read the notice twice and write the date on the kitchen calendar → **notice_read** _(FLAG: noticeKept)_
  - NOTE (shown after choosing): November 16, in ink, next to Solana's dentist appointment. Both are appointments with people who will make decisions about her. Only one of them knows it yet.

## [notice_read] What the Notice Doesn't Say
*Day 1 — Tuesday, October 6, 2026 (dayOffset 1)*

The notice gives a courtroom, a time, and a case number. It does not give you a lawyer, a seat at the table, the right to see the agency's report, or the right to ask anyone questions. You have fed a school district for thirty years and you know an institutional document when you see one: this one is an invitation with most of the verbs removed.

What it gives — notice, and the chance to be heard — is real. Rights in this system are frequently load-bearing out of proportion to their size, but only for people who learn their exact shape before the hearing, not after.

**Choices:**
- Find out the right's exact shape from someone whose job is knowing → **clinic**
  - NOTE (shown after choosing): The legal clinic's intake line has heard this exact question before. That is both sad and extremely useful.

## [clinic] What 'Opportunity to Be Heard' Means
*Day 3 — Thursday, October 8, 2026 (dayOffset 3)*

Ms. Romano, at the clinic, draws the shape precisely. "Section 6336.1 — Act 48 of 2023 — gives resource caregivers, including kinship resources like you, notice of the hearing and an opportunity to be heard. It does not make you a party. Parties can file motions, see the record as of right, cross-examine. You cannot. Unless you held legal custody under § 6357 — you don't — you have no standing to ask the court for anything."

"But hear me," she says, and leans in. "'Heard' is not nothing. The judge will make determinations about Solana's placement and progress (42 Pa.C.S. § 6351(f)) from what's presented. You are the only person in that room who can testify — be heard — about her actual daily life: school, health, her mother's visits at your table. If your statement is prepared, specific, and supported by paper, judges use it. If it's a plea from the heart with no dates in it, it evaporates by lunch. You have six weeks. Spend them like a party would."

**Choices:**
- Ask what paper a non-party should bring → **mother_call**
  - NOTE (shown after choosing): "School. Health. The visit log. And one thing more — her mother's record. You're not the only person whose paper matters on November 16, and hers you can actually help with."

## [mother_call] Calling Solana's Mother
*Day 5 — Saturday, October 10, 2026 (dayOffset 5)*

Your daughter Daniela — Solana's mother — is eight months into her own case: services underway, visits on Sundays at your table, progress that is real and, in the agency's file, thinly written. She is a party. Parties can do the thing you cannot: request the agency's complete record, which is released on request (55 Pa. Code § 3130.44(d)) — including the placement recommendation being drafted about your house.

You call her with a request that is also a strategy: sign the records request, in writing, this week — so that what the agency plans to say about both of you on November 16 is something you have both read by November 10.

**Choices:**
- Ask her to sign the written request for the complete record this week → **school_records** _(FLAG: recordsRequested ; HIDDEN + Record — complete agency file requested in writing by the mother, at the kinship caregiver's asking)_
  - NOTE (shown after choosing): She signs it at your table on Sunday, between Solana's math homework and the visit's end. A party's signature, requested by a grandmother, aimed at a hearing. The right shapes, combined.
- Let her handle her own case her own way → **school_records**
  - NOTE (shown after choosing): Her own way, so far, has produced an eight-month file that describes her progress in one sentence. Autonomy is a value. So is November 16.

## [school_records] The School File
*Day 8 — Tuesday, October 13, 2026 (dayOffset 8)*

Solana's school knows her in the record-keeping way schools do: attendance near-perfect since she moved to your house (the year before, in the old apartment, it was not), reading at grade level, the nurse's notes, the counselor who gets her on bad mornings. A letter from the counselor, with the attendance figures, is the kind of paper that turns 'she's settled' from a grandmother's claim into a documented fact. Copies cost nothing but the asking, in writing, with the date of the hearing named.

**Choices:**
- Ask the counselor, in writing, for the letter with the attendance figures → **neighbor** _(FLAG: schoolPacket ; HIDDEN + School — counselor's letter with attendance and stability record obtained for the hearing)_
  - NOTE (shown after choosing): The letter arrives in Solana's backpack, in an envelope the counselor sealed like it mattered. It did.

## [neighbor] The Neighbor With the Spare Key
*Day 10 — Thursday, October 15, 2026 (dayOffset 10)*

Your neighbor of twenty years keeps your spare key and Solana's emergency card copy, and has watched the school bus stop outside your house for eight months of mornings. She offers, unprompted, the thing neighbors offer in this system that actually counts: 'If somebody official ever asks, I'll tell them what this street sees.' Somebody official, as of November 16, might. A short written statement — signed, dated, specific about mornings and homework and Sunday visits — is a neighbor's eyesight converted into a document.

**Choices:**
- Ask her to write it down: signed, dated, specific → **med_records** _(FLAG: neighborStatement ; HIDDEN + Community — neighbor's signed, dated statement on the household's daily stability)_
  - NOTE (shown after choosing): Two paragraphs, in her good handwriting. The street, on the record, in the only sense records recognize.

## [med_records] The Pediatrician's Summary
*Day 12 — Saturday, October 17, 2026 (dayOffset 12)*

Solana's pediatrician has seen her four times since the placement: the asthma plan updated, the inhaler technique now Solana's own party trick, weight and sleep and mood all charted in the direction of a child whose life became regular. A one-page summary costs $10 to print officially and says, in medical prose, what stability looks like from an examining room.

**Choices:**
- Pay for the official summary for the hearing packet → **church_letter** _(cash −10 ; FLAG: medPacket ; HIDDEN + Health — pediatrician's summary of stability and care obtained for the hearing)_
  - NOTE (shown after choosing): One page, four visits, everything trending the way pediatricians like things to trend. Filed in the packet between the school letter and the photographs you are not bringing, because paper, not sentiment, is your brief.

## [church_letter] The Letter From the Parish Hall
*Day 15 — Tuesday, October 20, 2026 (dayOffset 15)*

Solana does her homework at the parish hall on Thursdays while you run the food pantry shift, supervised by a retired teacher who has logged every Thursday since March in a spiral notebook she keeps for reasons of pure disposition. Her letter is a list: dates, times, a child's homework improving in a room full of donated soup. As evidence of a stable daily life, it has the great virtue of having been written before anyone knew it was evidence.

**Choices:**
- Ask her for a copy of the Thursday log as a letter → **statement_draft** _(FLAG: thursdayLog ; HIDDEN + Community — Thursday homework log letter added to the hearing packet)_
  - NOTE (shown after choosing): She copies it in her careful hand and signs it. A spiral notebook's worth of ordinary Thursdays, now admissible in the only court that matters: a judge's attention.

## [statement_draft] Two Pages, In Her Own Words
*Day 17 — Thursday, October 22, 2026 (dayOffset 17)*

Ms. Romano's last clinic session is the statement itself. "Two pages. Who Solana is, what her days look like, what her mother's visits look like from your kitchen, what a move would interrupt — school, doctor, Thursdays — and one sentence about what you're asking: not for anything. You're not a party. You are asking to be heard, and then letting the judge do the judging. Judges protect children. Give the judge facts to protect her with."

Writing it takes three evenings. It is the hardest homework of your life, and you spent thirty years feeding a school district. Dates keep trying to become feelings. You keep making them dates again.

**Choices:**
- Write the two pages, dated and specific, and practice reading them in under five minutes → **bus_ride** _(FLAG: statementWritten ; HIDDEN + Statement — caregiver's written statement prepared: specific, dated, inside the § 6336.1 opportunity to be heard)_
  - NOTE (shown after choosing): Four minutes, forty seconds, reading aloud to the kitchen. Solana, from the doorway: 'That's just our house, Abuela.' 'Yes,' you say. 'That's the whole argument.'

## [bus_ride] The Bus Ride Ledger
*Day 20 — Sunday, October 25, 2026 (dayOffset 20)*

Everything costs something in this story, including bus fare to the clinic and the pharmacy and the school meeting — the ledger of being heard, kept in a sixty-one-year-old's checkbook. The packet is nevertheless assembled: statement, school letter, pediatric summary, neighbor's page, Thursday log, and — arriving this week, because Daniela signed in time — the agency's own file, including the draft recommendation you have not yet seen.

**Choices:**
- Keep the ledger and wait for the file → **visit_sunday**
  - NOTE (shown after choosing): The file arrives Thursday. The recommendation is exactly as feared, and entirely different read on paper than feared in a doorway: arguable, specific, and wrong in two places you can document.

## [visit_sunday] Sunday at Philomena's Table
*Day 22 — Tuesday, October 27, 2026 (dayOffset 22)*

Daniela's Sunday visit runs the way the good ones run: homework checked, hair braided with professional commentary from the chair, a meal, a walk, a goodbye that is sad in the ordinary size. You have kept a simple log since March — dates, times, what happened, in a notebook by the phone — because the agency's version of these Sundays, when it appears, is three lines long and two of them are the date.

At the hearing, the question of Daniela's progress (42 Pa.C.S. § 6351(f)(3)) will be answered partly from records of these Sundays. Yours is the only complete one in existence.

**Choices:**
- Bring the Sunday log up to date and copy the key pages for the packet → **worker_visit** _(FLAG: visitLog ; HIDDEN + Visit log — grandmother's contemporaneous Sunday-visit log, complete since March)_
  - NOTE (shown after choosing): Eight months of Sundays, in a grandmother's handwriting. The file's thinnest subject, documented by the only person who was at every single one.

## [worker_visit] The Worker's Visit
*Day 27 — Sunday, November 1, 2026 (dayOffset 27)*

The caseworker's October visit is pleasant and devastating in the modern manner: Solana's room admired, the log noticed ('you keep records?'), and then, at the door, the recommendation confirmed — the agency will ask the court to move Solana to a licensed non-kin foster home, citing 'resource limitations' and the agency's preference for fully licensed placements. Your house, she says kindly, 'has been wonderful as an emergency solution.' Eight months, reclassified as an emergency.

A recommendation described in a doorway can be answered only with sympathy. A recommendation in writing can be answered with documents.

**Choices:**
- Ask for the recommendation in writing, for your daughter and yourself → **photo_album** _(FLAG: recInWriting ; HIDDEN + Agency position — placement recommendation obtained in writing before the hearing)_
  - NOTE (shown after choosing): It arrives by email in two days: two pages, specific claims, two of them checkably wrong about school distance and the asthma plan. Writing is a gift your opponents give you when you ask for it.
- Accept the explanation and trust the hearing to sort it out → **photo_album**
  - NOTE (shown after choosing): Hearings sort out what is presented to them. Doorway explanations are not presented; they are remembered, warmly, by nobody.

## [photo_album] The Photograph You Don't Bring
*Day 30 — Wednesday, November 4, 2026 (dayOffset 30)*

The packet is done, and the temptation arrives on schedule: the photograph album — Solana asleep on the porch, Solana's birthday, eight months of a childhood visibly being lived well. Ms. Romano was clear: photographs are feelings in a frame, and you are not being heard as a grandmother with feelings. You are being heard as the record-keeper of a stable placement. The album stays home. That it stays home is, itself, a kind of testimony about how seriously you took the assignment.

**Choices:**
- Leave the album, take the packet → **sister_phone**
  - NOTE (shown after choosing): The packet is heavier anyway. It has dates in it.

## [sister_phone] Your Sister Calls From Ohio
*Day 33 — Saturday, November 7, 2026 (dayOffset 33)*

Your sister asks the question everyone asks: 'If you can't file anything, and you can't ask for anything, what exactly do you do in there?' You give her Ms. Romano's answer, which by now you believe in your bones: 'I get heard. The judge has to decide where Solana's placement serves her, from the determinations in the statute. The agency brings its recommendation. Her mother brings her progress. I bring Solana's actual life, on paper, in five minutes. Judges can only use what's in the room. I am making sure her life is in the room.'

'Five minutes,' your sister says. 'Thirty years of cafeteria and it comes down to five minutes.' 'Everything does,' you say. 'Lunch was twenty.'

**Choices:**
- Tell her the date and hang up to practice the statement once more → **prep_call**
  - NOTE (shown after choosing): Four minutes, thirty-eight seconds. The kitchen applauds in its fashion: the kettle, clicking off.

## [prep_call] Ms. Romano's Last Call
*Day 35 — Monday, November 9, 2026 (dayOffset 35)*

"Final shape," Ms. Romano says. "You will be called when the court reaches the placement question. Stand, say who you are, hand up the packet if the court permits, read the statement — don't summarize it, read it; summaries drift — and answer questions directly, including the hard one about your daughter. You are not there to win against Daniela or for yourself. You are there so the determinations (§ 6351(f)) get made about a real child's real year. Do that, and whatever the judge decides will at least be decided about Solana."

**Choices:**
- Confirm the plan: read it, hand up the packet, answer straight → **hearing_prep**
  - NOTE (shown after choosing): 'That's the whole of it,' she says. 'Being heard is a small right. You're about to find out how much weight small rights carry when somebody loads them properly.'

## [hearing_prep] The Night Before
*Day 38 — Thursday, November 12, 2026 (dayOffset 38)*

The packet is by the door: statement, school letter, pediatric summary, neighbor's statement, Thursday log, Sunday log copies, Daniela's progress pages (she sent hers over with a note: 'Tell them about the braiding. It's in your log anyway.'). Solana is asleep in the second bedroom, in the middle of the life everyone will discuss tomorrow in the third person.

You could still decide this is too much — that a grandmother's place is the kitchen, not the courtroom; that being heard is for other people. The notice will still be in the mailbox either way. The right, however, is only real on the day it's used.

**Choices:**
- Set two alarms and go — being heard only happens in the room → **courthouse_steps**
  - NOTE (shown after choosing): Two alarms. The packet by the door like a dog that knows the route. Solana's breakfast things laid out, because tomorrow is also a school day, whatever the court decides.
- Decide the courtroom is no place for a grandmother, and stay home → **out_absent**
  - NOTE (shown after choosing): The hearing will happen at 10 a.m. with or without the only person who can describe Solana's year. It will be decided from the paper in the room. Yours won't be.

## [courthouse_steps] The Courthouse Steps
*Day 41 — Sunday, November 15, 2026 (dayOffset 41)*

You are not at the table. That is the shape of the right, and the hallway teaches it again: the parties' lawyers at their tables, Daniela at hers, looking small and determined, and a chair along the wall for the people the statute gives notice to. Ms. Romano's words ride with you: you are not there to be a party. You are there to be a record with a voice.

The clerk calls the case. The agency's counsel presents its report and its recommendation, in the smooth prose of people who present every week.

**Choices:**
- Sit in the notice chair and wait to be called to be heard → **hearing**
  - NOTE (shown after choosing): Waiting, in the chair the statute built. It is not a throne. It is a place from which a judge can hear you, which turns out to be a different and better thing.

## [hearing] Called to the Front
*Day 42 — Monday, November 16, 2026 (dayOffset 42)*

The placement question arrives. The agency's counsel recommends transfer to a licensed foster home: resource limitations, licensure, a school 'equidistant' — the word from the written recommendation, the one you read on Thursday — and then the judge looks along the wall. 'Mrs. Rios. The court will hear from the resource caregiver.'

Five minutes. The packet is in your hands. What happens now depends on what the last six weeks made of them.

**Choices:**
- Read the statement and hand up the packet: school, health, Sundays, Thursdays → **out_stays** _(REQUIRES FLAG: statementWritten ; REQUIRES FLAG: schoolPacket)_
  - NOTE (shown after choosing): The judge stops you once — at the attendance figures — and asks the agency's counsel a question whose answer takes longer than your whole statement. Equidistant gets a workout. So does 'emergency solution.'
- Speak from the heart, from memory, without the packet → **out_stays_plain**
  - NOTE (shown after choosing): The heart is fluent and the memory is sincere, and neither contains a single attendance figure. The judge is kind. Kindness is not a determination.

## [out_stays] The Determinations, Made About Solana
*Day 42 — Monday, November 16, 2026 (dayOffset 42)*

The judge makes the determinations aloud, and Solana's actual year is in every one of them: placement with the kinship resource is serving her safety and stability; the school's and pediatrician's records are credited by name; Daniela's progress is found real and ongoing, with her Sundays documented; the agency's recommendation is declined, its two factual errors noted without heat. Solana remains with her grandmother. The agency is directed to support the placement and to address Daniela's remaining services with dates. Next review in six months (42 Pa.C.S. § 6351(e)(3)(i)).

Daniela cries at her table in the good way. Along the wall, a sixty-one-year-old record-keeper closes a packet and sits down in the chair the statute built, which held.

**Choices:**
- Walk out into the hallway where Solana's life resumes → **heard_order**
  - NOTE (shown after choosing): The written order will say 'the caregiver was heard pursuant to § 6336.1.' Five words for six weeks of evenings. You will frame none of it. You will keep the log.

## [out_stays_plain] The Determinations, Made Around Solana
*Day 42 — Monday, November 16, 2026 (dayOffset 42)*

The judge thanks you warmly and turns back to the paper. On the paper, the placement question is between the agency's specific recommendation and Daniela's thin file — and a grandmother's evident love, which every person in the room believes and no determination can cite. The court compromises: Solana remains with you 'for the present,' the recommendation is tabled rather than declined, and the agency is asked to 'revisit licensure pathways' and report back — a door left open for the same recommendation to return, better written.

Daniela's services get no dates. The next review is in six months. You kept your granddaughter tonight. You did not change the weather she lives in.

**Choices:**
- Walk out with the 'for the present' order → **plain_order**
  - NOTE (shown after choosing): 'For the present' is a real thing to win and a fragile thing to hold. The packet you didn't bring is still makable. The next review is a date, and dates are your trade now.

## [out_absent] The Hearing, In Her Absence
*Day 42 — Monday, November 16, 2026 (dayOffset 42)*

The hearing takes thirty-five minutes. The agency's recommendation is presented with its two errors uncorrected, because the only person who had read it closely is at home with a packet by her door. Daniela's counsel argues progress from a thin file. The determinations are made from the paper in the room, and the paper in the room recommends a move.

The court orders the transfer to proceed on a transition schedule, with Solana's school transfer to be 'minimized' — a word doing heavy work in a sentence nobody in the room could test against an attendance record.

**Choices:**
- Learn the outcome from Daniela, at your own kitchen table → **moved_call**
  - NOTE (shown after choosing): She tells you gently, and then you both look at the second bedroom's door for a while. The packet is still by yours.

## [heard_order] The Order, Read at the Table
*Day 45 — Thursday, November 19, 2026 (dayOffset 45)*

The written order is four pages. Page two contains the sentence you will remember when the rest is forgotten: 'The court heard the resource caregiver pursuant to 42 Pa.C.S. § 6336.1, whose statement and exhibits the court credits.' Heard. Credits. Two verbs, earned in the only currency the building accepts.

Solana reads over your shoulder as far as 'attendance' and wanders off to her homework, in her room, in her house, on a school night. The order also sets Daniela's service dates and the next review. The case goes on. It goes on around a child who gets to stay where her life is.

**Choices:**
- File the order in the packet and update the Sunday log → **end_heard**
  - NOTE (shown after choosing): The log's next entry is already determined in outline: Sunday, Daniela, braiding, homework. The ordinary, continuing, on the record.

## [plain_order] The Order, Read at the Table
*Day 45 — Thursday, November 19, 2026 (dayOffset 45)*

The written order is two pages, and the phrase 'for the present' appears twice, which is once more than a family can build on. Solana stays — that is real, and tonight it is enough for cocoa. But the agency's door is open, its recommendation alive, its errors uncorrected, and Daniela's services float without dates above a six-month horizon.

The packet you prepared too late to use is on the counter. It is not wasted. It is, now, a head start on a review that will decide whether 'the present' becomes 'the placement' or 'the former placement.' September is a date. You have begun, belatedly, to specialize in them.

**Choices:**
- Put the packet on the calendar's first page and start again → **end_plain**
  - NOTE (shown after choosing): March's log-keeping was the apprenticeship. September is the journeyman piece. Solana, from her room: 'Abuela, spelling.' Some reviews are nightly.

## [moved_call] The Transition Schedule
*Day 45 — Thursday, November 19, 2026 (dayOffset 45)*

The transition schedule arrives by mail: introductory visits to the new home over three weeks, the move on the fourth, school transfer 'to be arranged,' Solana's belongings inventoried in a checklist that includes, you notice, no line for a grandmother. Your notice rights for the next hearing remain — the statute does not withdraw them — and Solana's life will still generate facts. But the facts now accumulate in someone else's kitchen, described by someone else's log, in a case whose determinations will be made, next time, about a child described entirely by professionals.

Daniela's case continues; her Sundays become visits somewhere else, recorded in three lines. The packet by your door keeps its shape. Paper keeps. Children, moved, are not paper, and do not keep the same way.

**Choices:**
- Begin the transition the way the schedule demands, and keep every record anyway → **end_moved**
  - NOTE (shown after choosing): Keeping records after the loss feels pointless in November. It is, in fact, the only move the story has ever endorsed, and it is not nothing: cases continue, children come back to tables, and files outlast orders.

## [end_heard] Ending — Heard, and It Moved the Order
*Day 49 — Monday, November 23, 2026 (dayOffset 49)*

Solana stays. The agency's recommendation was declined on facts — hers: attendance, asthma, Thursdays, Sundays — presented by the one person positioned to know them, through a right so small it fits in one sentence of a statute: notice, and an opportunity to be heard.

Philomena never became a party. She filed nothing, objected to nothing, cross-examined no one. She prepared like a party, read the other side's paper like a party, and spoke for five minutes like the record-keeper of a child's year. The determinations that kept Solana home cite her exhibits. Small rights, properly loaded, carry children.

**ENDING — Debrief:**

THE WIN, NAMED HONESTLY — A partial win: the placement holds and Daniela's services got dates, but Solana is not 'home' in the law's final sense — her mother's case continues, reviews continue, and a future agency recommendation can return. What was won is the present, documented and ordered, plus a record that makes the next recommendation harder to write carelessly. In permanency practice, that is a large win wearing plain clothes.

THE LAW IN THE BEATS — 42 Pa.C.S. § 6336.1 (Act 48 of 2023) gives foster parents, resource caregivers, and kinship resources (§ 6302's definition) notice of permanency hearings and an opportunity to be heard; it does not confer party standing, which Philomena was told plainly and never claimed — standing to participate as a party runs through custody (§ 6357), which she does not hold. The hearing's work was § 6351(f)'s determinations and the six-month rhythm of § 6351(e)(3)(i). The complete file was obtained through the mother's written request under 55 Pa. Code § 3130.44(d), because the regulation's right belongs to the case's subjects — a limit the scenario respects rather than wishes away.

THE HIGHEST-LEVERAGE MOVE — Getting the recommendation in writing before the hearing. It converted a doorway remark into two checkable errors and a winnable argument. The statement mattered; the written recommendation is what gave the statement something to defeat.

WHAT NO STRATEGY CONTROLS — The judge's receptivity, the agency's future filings, Daniela's road. The route controlled preparation, paper, and presence — the full extent of what § 6336.1 offers, used to its full extent. Outcomes also turn on the people in the room; this one turned on the only person in the room who knew where Solana does her homework.


## [end_plain] Ending — 'For the Present': The Win That Isn't Finished
*Day 49 — Monday, November 23, 2026 (dayOffset 49)*

Solana stays, provisionally, in a case whose underlying weather did not change: the recommendation lives, its errors stand, the services float. The difference between this ending and the best one is not love, effort, or truth — Philomena's spoken account was every word true. It is the difference between testimony and exhibits: a judge can credit paper in a determination; a judge can only thank a memory.

The next review is in six months, and this time the packet exists. Whether 'for the present' hardens into a placement or dissolves into a transfer will be decided, as this was, by what's in the room.

**ENDING — Debrief:**

NAMED HONESTLY — A middle outcome: the child is not moved, and nothing was decided that prevents her being moved later. The scenario ranks it above the transfer ending and below the credited-statement ending, because that is what it is.

THE LAW IN THE BEATS — The same § 6336.1 right, exercised at half its capacity: heard, but without the exhibits that let § 6351(f) determinations cite her. Notice and opportunity guarantee a voice in the room. They do not supply its contents; preparation does, and preparation is made of paper requested, letters asked for, and logs kept — including the mother's § 3130.44(d) request, which in this route went unmade or unused.

WHAT NO STRATEGY CONTROLS — The compromise itself was a judge's mercy, and mercy is not a strategy either. The route's lesson runs the other way: the difference between the two stay endings was entirely within the grandmother's control, which is rare in this system and worth saying plainly when it's true.


## [end_moved] Ending — The Room She Wasn't In
*Day 49 — Monday, November 23, 2026 (dayOffset 49)*

Solana moves in December, on a transition schedule, to a licensed home across the district, with a school transfer arranged in the sense that a form was completed. Daniela's Sundays relocate to a visit room. Philomena's notice rights continue for future hearings, and she will use them — that is the epilogue this ending permits, and it is not a small one — but the determinations of November 16 were made without the only complete account of Solana's year in existence.

Nothing in this ending required anyone to be cruel. The agency recommended as agencies recommend; the court decided from what was presented. The absence in the room was the decisive fact, and absences, in this system, are never entered into evidence. They simply shape everything that is.

**ENDING — Debrief:**

WHY THIS ENDING — 42 Pa.C.S. § 6336.1's opportunity to be heard is exactly that: an opportunity, exercisable only in the room, on the day. Unexercised, it does not linger as a claim over the resulting order; the § 6351(f) determinations are made from the presented record, and the presented record here was the agency's. The scenario does not pretend Philomena could have filed anything — she had no standing (§ 6357) — which is what makes the missed five minutes total: it was the only move the law gave her, and it was enough, and it went unplayed.

WHAT REMAINS TRUE — The case continues; reviews recur (§ 6351(e)(3)(i)); placement can be revisited on a later record; and a grandmother with a packet, a log, and six months of new facts is a different witness in May than she would have been in November. The story's doctrine holds even here: outcomes turn on workers, judges, and luck — and on whether the person who knows the child's life is in the room when it's described.

