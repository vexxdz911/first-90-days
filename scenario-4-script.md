# THE FIRST 90 DAYS — Scenario 4: “The Kinship Door”

*Human-readable script. This document and `scenario-4.json` are generated from a single source and match node-for-node: same IDs, same order, same choices, same effects.*

**The family is fictional — a composite. No real person's story appears here.**

**Content note:** This scenario depicts a grandmother's kinship-placement request, a home study, and an approval denial — told through procedure and paperwork. There is no graphic content. Players may skip any scene or use the quick exit at any time.

**How to read effects:** `cash −40` changes the player's cash. `FLAG: name` sets a flag the engine tracks. `HIDDEN + item` means the case file quietly records that item at this choice — the player does not see it when it happens. `NOTE:` is text shown to the player right after choosing.

Start date: Monday, September 14, 2026 (the child was placed three weeks earlier). Day offsets are days since the scenario's start date.

## [start] The Stamped Copy
*Day 0 — Monday, September 14, 2026 — Monday, September 14, 2026 (dayOffset 0)*

Three weeks ago, at one in the morning, your daughter Leah's life came apart in a way that involved police lights and a caseworker's knock, and by sunrise your granddaughter Mia — five years old, solemn, missing one front tooth — was placed with a foster family across town. You asked that night, standing in your doorway in your robe, for Mia to come to you. The answer was honest and useless: clearances cannot be run at 1 a.m. Kinship would be looked at “during business hours.”

Business hours took three weeks. Leah is in treatment now, doing the hardest work of her life in a building with no locks on the inside of the doors. Mia asks for you on every visit. And you — sixty-one years old, twenty-two of them spent feeding other people's children in a school cafeteria — are done waiting to be looked at.

Today you file a written request at the agency office: that Mia be placed with you, her grandmother. The receptionist stamps your copy. The stamp is not an answer. It is proof the question exists.

**Choices:**
- File the original, keep the stamped copy in your purse → **study1**
  - NOTE (shown after choosing): Paper again. In this system, a stamped copy is a kind of seniority.
- Hand a second copy to Leah's lawyer at the courthouse window while you're downtown → **study1**  _(FLAG: copyShared)_
  - NOTE (shown after choosing): Two files, same question. Questions travel farther in duplicate.

## [study1] The Home Study, First Visit
*Day 4 — Friday, September 18, 2026 — Friday, September 18, 2026 (dayOffset 4)*

Ms. Ferreira, the kinship worker, arrives with a checklist and the good manners not to pretend it isn't one. She walks the rooms the way you once learned to read a kitchen before a health inspection: kindly, and missing nothing.

Mia's room stops her. It is already made up — the quilt from Mia's own bed at Leah's, the shelf of her books, the night-light shaped like a moon. “You did this before anyone promised you anything,” she says, and writes it down, and you decide you like her for writing it down where you could see.

Two findings, both small: medications belong in a lock box, not the bathroom cabinet; the smoke alarm in the hall is older than Mia. She gives you the weekend, and the form, and no promises at all — which you also decide you like.

**Choices:**
- Buy the lock box and the alarm this weekend and text her the receipts → **leah**  _(cash −18; FLAG: homeReady; HIDDEN + Home study — 'Room prepared for the child before approval was sought')_
  - NOTE (shown after choosing): Fixed by Sunday night. In files, speed reads as seriousness, because it usually is.
- Fix both this month, as the budget allows → **leah**
  - NOTE (shown after choosing): Reasonable, and recorded that way: found, unfixed, pending. Forms have no column for budgets.

## [leah] Thirty Days In
*Day 8 — Tuesday, September 22, 2026 — Tuesday, September 22, 2026 (dayOffset 8)*

The treatment center allows visitors on Tuesdays. Leah is thinner, and her eyes are the eyes she had at nineteen, before everything. Day thirty, the counselor says, like a mile marker.

She holds your hand across the visiting-room table with the grip of the child who used to hide behind your legs at the grocery store. “Ask them to let her live with you, Mom. Whatever they need. Whatever it takes.”

You tell her it is already filed, already stamped. She cries then — relief, you think, and also the particular grief of being the reason for a form. Both of you let the counselor's clock end the visit. Driving home, you think about the word “whatever.” It is a big word. It has not yet been itemized.

**Choices:**
- Go home and prepare for the study's second visit — the interview → **study2**
  - NOTE (shown after choosing): The first visit was your house. The second one is your life.

## [study2] The Interview
*Day 11 — Friday, September 25, 2026 — Friday, September 25, 2026 (dayOffset 11)*

The second visit is a conversation at your kitchen table, and it covers the topography of a life: the cafeteria years, the apartment years before this house, raising Leah mostly alone, the church, the sister in Ohio you call on Sundays.

Then Ms. Ferreira turns a page, and asks the standard question in the standard tone, the one that is asked of everyone and lands on each person differently: arrests, charges, convictions — anything, at any time.

Your page in that history is from 1998. You were twenty-four. There was a parking lot, and a woman who had been your friend, and a fight that went further than fights in stories are supposed to go. Aggravated assault. You served your sentence. You have been a school cafeteria worker, cleared and re-cleared among children, for twenty-two years since. The page is old. It is also, in the way of pages, exactly as legible as the day it was written.

**Choices:**
- Tell her about 1998 plainly, yourself, first — all of it, including 'it did not involve a child' → **fingerprints**  _(FLAG: selfDisclosed; HIDDEN + Applicant statement — conviction self-disclosed: 'I paid my debt. It did not involve a child.')_
  - NOTE (shown after choosing): She writes it in your words. However this goes, the first voice on that page will be yours.
- Answer the question asked, no more — the paperwork will show what it shows → **fingerprints**
  - NOTE (shown after choosing): It will. The only question paperwork ever leaves open is whose voice says it first.

## [fingerprints] The Errand of Being Checked
*Day 15 — Tuesday, September 29, 2026 — Tuesday, September 29, 2026 (dayOffset 15)*

Fingerprints at a storefront office that also ships packages. A state check, a federal check, a child-abuse-history clearance — the liturgy of being verified, one queue at a time.

The modern records come back fast and clean: decades of nothing, which is what a law-abiding life looks like in a database — a long, flat line. The old county court record travels slower, by older roads. Ms. Ferreira tells you the study is “essentially complete, pending the full history.”

Pending. You have come to understand that in this system, pending is a room where families sit, and the room has no clock.

**Choices:**
- Use the waiting the way you used it in 1998's aftermath: one ordinary week at a time → **visit1**
  - NOTE (shown after choosing): You are, it turns out, extensively trained for exactly this room.

## [visit1] Sunday Comes on Friday This Week
*Day 18 — Friday, October 2, 2026 — Friday, October 2, 2026 (dayOffset 18)*

Visits with Mia happen at the foster home, which is warm and crowded and run by Mrs. Pruitt, a woman who labels leftovers with dates and has the rested look of someone who has not been rested since 2019.

Mia shows you a drawing of your house — she has drawn the moon night-light, from memory, larger than the house. At the door she asks the question she asks every time, without drama, the way children ask about weather: “When can I sleep at your house, Nana?”

Mrs. Pruitt, packing Mia's snack bag, answers nothing, kindly. Everyone in the doorway knows the answer is sitting in a room marked pending.

**Choices:**
- Leave Mia's own pillowcase, so your house travels to her a little → **the_wait**  _(HIDDEN + Visit note — 'When can I sleep at your house, Nana?' asked at every visit)_
  - NOTE (shown after choosing): Mrs. Pruitt puts it on the bed herself. Allies in this system are often just people who put the pillowcase on.
- Ask Mrs. Pruitt what Mia says at bedtime, and write it down in the car → **the_wait**  _(FLAG: bedtimeNotes; HIDDEN + Visit note — child settles best with grandmother's quilt and the moon light)_
  - NOTE (shown after choosing): “You,” she says. “Every night, she says you.” Some evidence is not for hearings. Some is for lasting until them.

## [the_wait] Trim
*Day 21 — Monday, October 5, 2026 — Monday, October 5, 2026 (dayOffset 21)*

The study is complete. The answer is “in review.” You paint the trim in Mia's room anyway — white over white, the most optimistic paint there is.

Your sister in Ohio asks what happens if the answer is no. You tell her the truth: you don't know the shape of no yet. It will arrive, like everything else in this case, as a letter.

It arrives Friday.

**Choices:**
- Open Friday's mail → **denial**
  - NOTE (shown after choosing): The envelope is thin. Thin envelopes, in this system, rarely carry picnics.

## [denial] One Line
*Day 25 — Friday, October 9, 2026 — Friday, October 9, 2026 (dayOffset 25)*

The letter is one page. It thanks you for your interest in providing kinship care. It says the agency is unable to approve you as a resource caregiver for Mia. It gives the reason in a single sentence, in the passive voice, as if the sentence had no author:

Your criminal history record includes a conviction for aggravated assault (1998).

Nothing follows about the study's other pages — the room, the lock box, the twenty-two years of other people's children eating lunch safely in your line of sight. Nothing about the decades since. A conviction, in this letter, has no date on it that matters. It is twenty-eight years old, and it is this morning.

**Choices:**
- Read it a second time, at the kitchen table, with a pen — the way frightened people read everything now → **kitchen**  _(HIDDEN + Placement summary — 'Resource denied — criminal history (1998)')_
  - NOTE (shown after choosing): The pen finds nothing to correct. That is its own information: the letter is not wrong. It is short.
- Call the office number at the bottom → **kitchen**
  - NOTE (shown after choosing): A voicemail box, full. Even the fullness feels procedural.

## [kitchen] What Leah Can Ask
*Day 27 — Sunday, October 11, 2026 — Sunday, October 11, 2026 (dayOffset 27)*

Sunday calls from treatment are twenty minutes, and Leah uses four of them crying about the letter, and then she does something that reorders the whole case: she asks what she can do.

More than she knows. Leah is Mia's mother and a party to the case. A party may ask, in writing, for the case record — and under the regulation it “shall be released upon request” (55 Pa. Code § 3130.44(d)). The record would include the placement decision and the home study — the warm pages and the one line alike.

You cannot request Mia's file yourself; the case is not yours. But your daughter can, and the asking would take her four minutes, and she is a woman currently rebuilding her life out of four-minute acts of courage.

**Choices:**
- Ask Leah to sign the record request this week — for the study, the summary, all of it → **birthday**  _(FLAG: recordsRequested)_
  - NOTE (shown after choosing): She signs it on the counselor's clipboard, in her treatment handwriting: careful, new, hers.
- Spare her — treatment is enough weight for one person to carry → **birthday**
  - NOTE (shown after choosing): A kindness. It has a price, like most kindnesses in a paper system: you'll build from the letter alone.

## [birthday] Six Candles in a Park Pavilion
*Day 33 — Saturday, October 17, 2026 — Saturday, October 17, 2026 (dayOffset 33)*

Mia turns six at a park pavilion, in an extended visit that took three phone calls to arrange — the parallel track of this case, where you are not an applicant at all, just the grandmother, running the party.

Mrs. Pruitt brings the cake carrier and stays for coffee. Leah attends by video call from the center, propped on the picnic table, and Mia holds the phone up to show her the candles as they're lit, in a piece of stage management no court ordered and no form records.

This is what the file cannot hold and the case nevertheless runs on: a child, at the center of three households' worth of adults, coordinating her own birthday across all of them.

**Choices:**
- Go home to the painted room, and wait for what Leah's request brings → **reveal**
  - NOTE (shown after choosing): The packet comes Thursday. Packets in this story travel on Thursdays when they travel at all.
- Go home and start from the letter alone — the clinic for grandparents meets Saturday → **paths**
  - NOTE (shown after choosing): The denial letter, a pen, and twenty-eight years. Some advocates have built cases from less, and will tell you so.

## [reveal] The Warm Pages
*Day 38 — Thursday, October 22, 2026 — Thursday, October 22, 2026 (dayOffset 38)*

Leah's request brings copies: the home study, complete. You read your own house described by a professional stranger — “home environment: excellent. Preparation for the child: specific and sustained. Motivation: the child's grandmother, in the plainest sense the word can bear.” Page after page of a life, found sufficient.

Then the placement page. Under “Resource determination,” the study's warmth ends at a line break: “Denied — criminal history (1998).” One line. The twenty-eight years are not in the summary, because summaries are not where years live. Years live in packets, assembled by hand, by people who refuse to let a line do the work of a life.

You sit with both facts — the warm pages exist; the line is what travels — and you understand the actual mechanics of your case: whoever assembles the packet assembles the grandmother the court will meet.

**Choices:**
- Start the packet yourself: everything, dated, in a folder with Mia's name on it → **paths**  _(FLAG: keptFolder; HIDDEN + Home study summary — home environment: excellent; motivation: sustained; HIDDEN + Placement summary — one line: 'Denied — criminal history (1998)')_
  - NOTE (shown after choosing): Folder first. Strategy second. In paper systems, that order is not an accident.

## [paths] Three Doors
*Day 40 — Saturday, October 24, 2026 — Saturday, October 24, 2026 (dayOffset 40)*

The grandparents' legal clinic meets in the senior center's back room, and its lawyer — a woman who has heard this letter read aloud many times — does not insult you with surprise. She gives you, instead, geography.

“Door one: appeal the approval denial — in writing, and soon. Appeals in this world run on short clocks, and a late appeal isn't an appeal; it's a memorial to one. The grandmother in the case the students study waited, and lost the right to argue at all. Door two: the court. The agency's approval checklist binds the agency. The judge at Mia's review hearings answers a different question — where should this child live — and judges have, on a full record, placed children with grandparents their own agency could not approve. Door three: be the visit home, build your record there, and let time and truth accumulate.”

“Doors one and two are not enemies,” she says. “The appeal builds the record. The court reads it. Choose the order, and mind the clocks.”

**Choices:**
- Build the packet first — one folder for both doors → **packet_work**
  - NOTE (shown after choosing): Clocks noted. Folder started. The order is the strategy.
- Accept door three — be the visit home, wholly, and start tonight → **visit_role**
  - NOTE (shown after choosing): Not surrender. A different theory of the same case: be so central to Mia's week that the file grows around you.

## [packet_work] The Kitchen-Table Archive
*Day 51 — Wednesday, November 4, 2026 — Wednesday, November 4, 2026 (dayOffset 51)*

It assembles over three evenings, in the order a life actually leaves evidence: the 1998 docket sheet — one page, the whole of it — followed by twenty-eight years of the opposite of a record. The school district's letter: twenty-two years, thousands of children, no incident. The pastor's letter. Leah's counselor's note, careful and professional: Mia's attachment to her grandmother is a treatment asset, named as such.

And the home study itself — the warm pages, the prepared room — with the one-line summary paper-clipped to the front, so that no reader can mistake what this packet answers.

Copies at the library machine, in triplicate, smelling of warm toner. It is not a legal argument. It is a life, collated. Legal arguments, it turns out, are often just lives, collated, with a cover letter.

**Choices:**
- File the written appeal of the denial first — the short clock rules the order → **appeal_track**  _(cash −14; FLAG: appealFiled; HIDDEN + Packet — 1998 docket sheet, followed by 28 years of no record)_
  - NOTE (shown after choosing): Filed in time, with the packet attached. Whatever the appeal decides, the record now exists.
- Take the packet straight to the December review — prepare for the judge → **court_track**  _(cash −14)_
  - NOTE (shown after choosing): Through Leah's counsel, the packet goes to the court. The short clock on the appeal runs on — a risk, chosen with open eyes.

## [appeal_track] The Appeal, in Her Own Words
*Day 54 — Saturday, November 7, 2026 — Saturday, November 7, 2026 (dayOffset 54)*

The appeal form wants facts in boxes. The packet rides behind it like a second, larger shadow.

There is room, at the end, for a statement. Ms. Ferreira, months ago, wrote your disclosure down in your words. Now you write once more, for the officer who will decide: what 1998 was, what the sentence was, what the twenty-eight years have been — cafeteria lines, a daughter raised, a granddaughter expected. No adjectives doing push-ups. Just the years, in order.

An appeal filed on time is a door that stays a door even when it closes: what it gathers remains in the record, and records, unlike rulings, can be carried into other rooms.

**Choices:**
- Write the page, sign it, and send the whole thing before the week's end → **appeal_hearing**  _(FLAG: ownWords)_
  - NOTE (shown after choosing): One page. Twenty-eight years. It fits, because the years were mostly ordinary, and ordinary is the point.
- Let the documents speak — file the packet without a personal page → **appeal_hearing**
  - NOTE (shown after choosing): The packet is eloquent. Your voice in it is one page thinner. Officers notice whose voice is missing; they also notice bluster. It is genuinely close.

## [court_track] Preparing for a Room You're Not a Party To
*Day 55 — Sunday, November 8, 2026 — Sunday, November 8, 2026 (dayOffset 55)*

The December review has a shape you must learn precisely, because it is not the shape you expect: Mia's case belongs to its parties — Leah, the agency, Mia's advocate. A grandmother seeking placement may be heard on placement. She may not conduct the case. The difference between those two things is the difference between doors two and one.

Leah's counsel files your packet for the review. Mia's advocate visits your home on a Thursday and leaves, you think, converted — though advocates, like judges, are trained to keep their faces out of the record.

You prepare the way you prepared for the study: room ready, folder ready, and your two answers polished to plainness. If the judge asks about 1998, the answer is the one you gave Ms. Ferreira. If the judge asks about the years, the packet is the answer, and you are its index.

**Choices:**
- Go to the review dressed for waiting, because there will be waiting → **court_hearing**
  - NOTE (shown after choosing): Courthouse benches are the pews of this religion. You have sat in worse, for longer, for love.

## [appeal_hearing] The Hearing Officer
*Day 68 — Saturday, November 21, 2026 — Saturday, November 21, 2026 (dayOffset 68)*

The appeal hearing is in a county building with a flag and a water cooler, and the hearing officer is fair in the specific way of people whose job is a rule: she reads everything, she asks six precise questions, she thanks you without inflection for your candor about 1998.

The agency's position takes one sentence to state, because it is one sentence: the approval rule, as written, contains no time limit, and the agency has no authority to approve around it. Your position takes a packet, because it is a life.

She does not decide from the bench. People whose job is a rule rarely do. “You'll have my written decision within the month,” she says, and the month, like all months in this story, is not a metaphor — it is a unit in which a six-year-old measures time in lost weekends.

**Choices:**
- Wait for the letter, and keep the Saturday visits warm in the meantime → **appeal_decision**
  - NOTE (shown after choosing): Waiting, in this case, is also evidence. You have never once missed a visit. The log says so.

## [appeal_decision] The Decision, and What It Carries
*Day 75 — Saturday, November 28, 2026 — Saturday, November 28, 2026 (dayOffset 75)*

The decision upholds the denial. The officer's reasoning is careful and, on the approval question, probably unanswerable: the rule that binds the agency's approvals does not run on a clock, and an officer cannot write a time limit into it from a hearing room chair.

But read to the end — the way you have learned, the way frightened people and grandmothers read everything now. The written summary attaches your entire packet to Mia's case record: the docket sheet and the twenty-eight years, the district's letter, the study's warm pages, your own page. What the appeal could not decide, it has nevertheless done: it has made your record the court's record, ahead of December's review.

A closed door, it turns out, can be a conveyor belt.

**Choices:**
- Take the packet — now wearing the officer's stamp — into the December review → **court_hearing2**
  - NOTE (shown after choosing): This time, when the judge opens the file, the grandmother in it is twenty-eight years deep.
- Let the visit role be the answer — build there instead → **visit_role**
  - NOTE (shown after choosing): The packet stays in the record either way. Records wait better than people do.

## [court_hearing] The Review
*Day 70 — Monday, November 23, 2026 — Monday, November 23, 2026 (dayOffset 70)*

The courtroom is smaller than its reputation and kinder than its furniture. Leah appears by video from the center, doing well enough to be believed. Mia's advocate speaks first, and mentions your home the way one mentions weather that has been consistent: it simply keeps being there.

Then the judge does what the clinic lawyer said judges can do: she reads past the summary. She has the study open at the warm pages, and the one line, and your packet beside both. She asks the agency's lawyer one question — whether the agency's position is that the court, too, is barred from considering this placement — and the answer, after a pause the length of honesty, is no: the checklist binds the agency's approvals. It does not bind the court.

She turns to you. Two questions, she says. You have been preparing for both since September.

**Choices:**
- Answer plainly: 1998, in full — then the twenty-eight years, in order → **end_placement**
  - NOTE (shown after choosing): “It did not involve a child. I served my sentence. Since then I have fed other people's children for twenty-two years. Mia's room is ready. It has been ready since before anyone promised me anything.”
- Ask, instead, that visits move to your home while the court takes the matter under advisement → **visit_role**
  - NOTE (shown after choosing): A smaller ask, granted smaller doors. The judge nods at its reasonableness, and reasonableness, here, is a delay with good manners.

## [court_hearing2] The December Review
*Day 77 — Monday, November 30, 2026 — Monday, November 30, 2026 (dayOffset 77)*

December's review arrives in a courtroom with a wreath on the clerk's door and your packet riding at the front of Mia's file, wearing the hearing officer's stamp like a passport.

The agency's lawyer is gracious about the new geography: the denial stands — the agency cannot approve you — and the agency does not ask the court to refuse what the agency cannot grant. Leah, on the video screen, day ninety-one of treatment, says the sentence she has been saving: “She's asking for my daughter. I'm asking too.”

The judge looks at the one line, and then at the twenty-eight years the line was keeping out of the room, and she asks you her two questions.

**Choices:**
- Answer plainly — the same answers, because they're the same truth → **end_placement_appeal**
  - NOTE (shown after choosing): 1998, in full. The years, in order. The room, ready since September. Truths do not need revision between rooms.
- Ask that visits move to your home while the court considers it further → **visit_role**
  - NOTE (shown after choosing): The judge grants the visits and keeps the question. Some Decembers are for deciding; some are for almost.

## [visit_role] The Visit Home
*Day 80 — Thursday, December 3, 2026 — Thursday, December 3, 2026 (dayOffset 80)*

Visits move to your house on a Saturday morning with a sign-in text and a worker's first drop-in, and then — the system exhaling — on trust.

Mia runs the route she has been drawing for months: the moon light, the quilt, the shelf. She inspects the lock box like a small building inspector, approves the new smoke alarm, and informs you that your house “smells like Nana's house,” which is the review that matters, entered into no record anywhere.

Mrs. Pruitt packs the Saturday bag with the good snacks and a drawing for your refrigerator, and tells you, at the car, the thing foster parents know in their bones: “You're her constant. Constants are what get children through.” The case is not over. But Mia's week now has a center of gravity, and it is your kitchen table.

**Choices:**
- Host the Saturdays like the placement depends on them — because the record of them may, someday, be the placement case → **end_visitation**  _(cash −22)_
  - NOTE (shown after choosing): Every Saturday, logged. Every drawing, kept. The file grows around you, in the direction of your granddaughter.

## [end_placement] Ending — The Court's Different Question
*Day 77 — Monday, November 30, 2026 — Monday, November 30, 2026 (dayOffset 77)*

**Ending.**

**Debrief:**
- WHAT THE FILE HELD (the hidden record, revealed): Two documents lived in your file: a home study that found your home excellent and your preparation 'specific and sustained,' and a one-line summary that read only 'Denied — criminal history (1998).' For most of this scenario, the line is what traveled — to the placement page, to the summaries, toward the court. The study traveled only when you and Leah made it travel: her record request (the file “shall be released upon request,” 55 Pa. Code § 3130.44(d)) showed you both documents, and your packet put the years in front of the line. Judges, like the rest of us, decide from what is actually in front of them.
- THE PROCESS UNDER THIS PATH (described, as this scenario keeps its law to the verified set): The agency's approval checklist and the dependency court's placement decision are different doors with different keys. The checklist binds the agency — as the agency reads it, the criminal-history bar carries no clock, and no officer or worker can approve around it. The court answers a broader question — where should this child live — and on a full record it may designate a kinship placement the agency itself could not approve. That is discretion, and discretion is not a loophole: it is the system's design, the reason hearings have human beings in them. What discretion runs on is the record. A grandmother with your facts and no packet is a one-line summary; a grandmother with your facts and your packet is twenty-eight years deep. The facts were the same. The file was not.
- THE HONEST PART: Another judge, reading the same packet with a different sense of risk, could have kept Mia where she was — discretion cuts both ways, which is exactly why it exists and exactly why it frightens people. Workers, hearing officers, judges, and timing all held pieces of this outcome; what you held was the paper trail, the on-time filings, and a room that was ready before it was allowed to matter. In the published cases this scenario is built from, the grandmother who waited lost her argument to a deadline before any judge weighed her years. The lesson is not that the system is kind. It is that in a discretionary system, the paper trail is the part of the discretion that belongs to the family.

## [end_placement_appeal] Ending — Placement, by the Long Road
*Day 84 — Monday, December 7, 2026 — Monday, December 7, 2026 (dayOffset 84)*

**Ending.**

**Debrief:**
- WHAT THE FILE HELD (the hidden record, revealed): The same two documents as every path — the warm study and the one line — plus a third thing your choices created: an appeal record. The 1998 docket sheet with twenty-eight years stapled behind it; your own signed page; the hearing officer's summary carrying all of it into Mia's court file. When the judge finally weighed your years, she weighed them because the appeal — a door that closed in your face — had first carried them into the room.
- THE PROCESS UNDER THIS PATH (described, as this scenario keeps its law to the verified set): The approval appeal and the court's placement decision ran on separate tracks with separate logics. The appeal was decided on the approval rule as written — no clock in it, no exceptions an officer could invent — and you lost it fairly. The court's review was decided on the child: her attachments, her mother's voice, her advocate's report, and a full record of who you have been for twenty-eight years. On that question, on that record, the court could do what the agency could not. Nothing about the appeal loss prevented the court win; the loss built it. This is the deepest mechanic in this scenario, and the truest: in this system, a 'no' is often a ruling about which door you knocked on — and the doors share a hallway called the record.
- THE HONEST PART: The long road cost a season of a six-year-old's life — weekends in other people's houses while adults audited 1998. No one will give those back, and this scenario will not pretend the delay was a blessing in costume. What can be said is narrower and more useful: the grandmother in the published record who missed her appeal deadline never got her years weighed at all. You filed in time, lost in the right room, and won in the other one. Timing, paper, a daughter who could sign a request (55 Pa. Code § 3130.44(d)), and a judge willing to read past a summary — workers, officers, judges, and luck. Your share was the record. It was enough, this time, and 'this time' is the most honest phrase in family court.

## [end_visitation] Ending — The Visit Home
*Day 84 — Monday, December 7, 2026 — Monday, December 7, 2026 (dayOffset 84)*

**Ending.**

**Debrief:**
- WHAT THE FILE HELD (the hidden record, revealed): The denial never moved — it stands today exactly where it stood in October, one line long. What moved was everything around it: a visit log that now runs through your kitchen; a foster mother who calls you the constant; a daughter in treatment telling her counselor her daughter's center of gravity is your table; a study that says excellent to anyone who reads past the summary. Files like this do not stay frozen. They accumulate in a direction, and yours is accumulating toward Mia.
- THE PROCESS UNDER THIS PATH (described, as this scenario keeps its law to the verified set): Placement and presence are different legal objects, and this system guards the first far more strictly than the second. The approval checklist kept Mia from living with you; nothing in it could keep you from being her Saturday, her holiday table, her emergency contact, her person. Reviews recur. Records grow. A grandmother who becomes the documented center of a child's week is not a closed case — she is an open one, with the strongest possible exhibit still being added to, one Saturday at a time. And the doors from October do not vanish: approval decisions can be revisited as records change, and courts read files that have grown. What you would file next time is already half written — it is this autumn.
- THE HONEST PART: This ending is not the one you filed for in September, and calling it a victory would insult your intelligence and Mia's pillowcase. A six-year-old is sleeping in someone else's house tonight because of a fight in a parking lot in 1998 — a fact that reasonable people, reading the same file, weigh differently, which is precisely what discretion means and precisely why it is argued about. What is also true: children are kept by constants, and you have made yourself, on the record and off it, the most documented constant in your granddaughter's life. Workers, officers, judges, and calendars decided this round. The record — the thing you control — says the rounds are not finished.
