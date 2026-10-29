# Excused, Absent, Unexcused (a fictional composite) — Node-for-Node Script (Scenario 122)

Scenario 122 of *The First 90 Days* — script generated node-for-node from `scenario-122.json`; the JSON is the source of truth.

A fictional composite built from published Pennsylvania dependency practice and documented system patterns. Not a real family's case.

**Content note:** a dependency adjudication built on school attendance records. No graphic content.

**How to read effects:** `cash` is money spent or received at that choice; `FLAG:` marks a fact the story remembers; `HIDDEN +` is an assessment item the player never sees scored; `REQUIRES:` gates a choice on an earlier fact; `NOTE:` is authorial, not spoken in-world. Endings are marked **Ending.** with a **Debrief:**.

**Start date:** Monday, February 8, 2027. **Tier:** Complex. **Start cash:** $140.

---

## [start] Twenty-three

*Day 0 — Monday, February 8, 2027*

The petition is served at the laundromat where you work, which is how you come to read the worst paragraph of your life with a customer's towels rotating behind you. Paragraph four: *During the fall term, the child accumulated twenty-three (23) unexcused absences from school, evidencing a pattern of educational neglect.* Twenty-three. The number is typeset with the confidence of a thing that has been printed before, in other files, about other mothers.

Oren has asthma — real asthma, clinic asthma, a nebulizer shaped like a dragon that he has named. You count the fall on your fingers twice before your shift ends: sick days and clinic days, yes; days you kept him home on a whim, no. You count nine that were nobody's fault but the illness and two bad mornings. You cannot get to twenty-three without counting days you drove him to the clinic with a note in his backpack.

**Choices:**
- Read the whole petition at the kitchen table tonight — every paragraph, not just the loud one. → **petition_read**

## [petition_read] Paragraph nine

*Day 0 — Monday, February 8, 2027*

The rest of the petition is thinner than paragraph four's confidence suggests. There is the fall attendance. There is a paragraph about a missed well-child visit in the spring, already cured. And there is paragraph nine, written smaller, the way true things sometimes are in petitions: *In November, the child missed two scheduled asthma follow-up appointments; the mother reports transportation failure.*

Paragraph nine is true. The car died on a Tuesday; the second appointment died with it, and though you called the clinic both times — you remember the hold music — the petition's version ends at *missed*. Your case, read whole, is one inflated number and one honest paragraph. They will require opposite handling, and confusing the two is how parents lose both.

**Choices:**
- Count again, slowly, from the wall calendar — the one with the clinic stickers. → **lucinda_count**

## [lucinda_count] Nine, maybe ten

*Day 0 — Monday, February 8, 2027*

The wall calendar is the family's true archive: clinic stickers on appointment days, your shift marks, the dragon drawings Oren adds to any square he considers under-decorated. Counting from it: fourteen days that were clinic or illness-with-a-note — notes you wrote, signed, and put in the backpack yourself. Nine unexcused, by your own honest count, including two in September when the bus route changed and you mismanaged a week you have never pretended was well managed.

Fourteen plus nine is twenty-three. The petition's number is not invented — it is *converted*. Somewhere between the school office and the agency's word processor, excused stopped being a category your son was allowed.

**Choices:**
- Call the lawyer the court appoints — Mr. Keller — before you call anyone else. Numbers this wrong need a strategy, not a phone manner. → **lawyer122**

## [lawyer122] Two rooms

*Day 1 — Tuesday, February 9, 2027*

Mr. Keller teaches the case as architecture: two rooms, different rules. Room one is adjudication — did the agency prove its allegations? — and the burden there is the agency's, at the law's highest civil setting: a child may be found dependent only from clear and convincing evidence. (42 Pa.C.S. § 6341(c)) What is not proven is dismissed, and the child discharged on that allegation. (§ 6341(a))

Room two is disposition — what happens next — where the rules relax: written reports and all evidence helpful to the determination may be received there, and the people who made the reports may be examined and cross-examined about them. (§ 6341(d)(1), (2)) "The school's summary page," Keller says, "is a room-two document dressed for room one. Our whole case is documents: the school's *detail* — not its summary — the clinic's records, and your calendar. We get them in writing, we get them early, and we make the agency's exhibit testify against itself."

**Choices:**
- Start where the number was manufactured: the school office, and the file behind the summary. → **truancy_letter**

## [truancy_letter] The October letter

*Day 2 — Wednesday, February 10, 2027*

In the drawer where school papers go, under the lunch menus, is the letter the number arrived in first: an automated truancy warning from October, generated when Oren's absences crossed a threshold — it cites the count, offers a meeting, and bears no human signature at all. You remember reading it with the specific dread of a parent who cannot tell whether she is in trouble. You filed it. You did not answer it, because it did not read as answerable; it read as weather.

Keller, shown the letter later, will say the sentence that organizes this case: "Weather is what unexamined systems call their own output. We're going to examine it."

**Choices:**
- Take the letter, the calendar, and a written request to the school office. → **school_office**

## [school_office] The summary and the screen

*Day 3 — Thursday, February 11, 2027*

The school office produces, first, exactly what the agency has: the one-page summary — *23 unexcused*. It is only when you ask, in the words Keller gave you, for the *complete attendance detail with excuse coding and the note log* that the visit changes register. Ms. Baranski, the attendance clerk, turns her monitor — an act of minor institutional courage — and the detail tells a longer story: absence rows with code histories, and against fourteen of them a small flag from an older system: *note rcvd*.

"We migrated attendance software in October," she says, quietly. "The notes stopped being scanned in September — staffing. The flags came across. The *meanings*—" she touches the flag with one fingertip, "—didn't, in every column. I have raised this. It is being reviewed at the district level, which is a speed, I grant you, but not a fast one."

**Choices:**
- Ask for the detail in writing: the full printout, the code history, the note log — a formal request, dated, with a copy for your lawyer. → **oren_voice**  _(FLAG: schoolFile; HIDDEN + School records — attendance detail with code history requested in writing)_
- Ask her to just tell you which days were excused, and write them down yourself at the counter. → **summary_only**

## [summary_only] Counter notes

*Day 4 — Friday, February 12, 2027*

Ms. Baranski is willing, and the counter conversation is genuinely informative — and completely unusable. Your handwritten list of her verbal account has no stamp, no signature, no system's authority; it is a mother's notes about a clerk's memory, and it will be weighed exactly that way. She watches you write and arrives, visibly, at the same conclusion.

"Do the written request," she says. "I'll print it myself. Paper from me counts. Paper about me doesn't."

**Choices:**
- Do the written request. Full detail, code history, note log, for counsel. → **oren_voice**  _(FLAG: schoolFile; HIDDEN + School records — attendance detail requested in writing after verbal account proved unusable)_

## [oren_voice] The dragon

*Day 5 — Saturday, February 13, 2027*

Oren's evidence is offered at the kitchen table, unprompted, while demonstrating the nebulizer: "The dragon days aren't school days. You can't do math when the dragon is loud. The nurse lady knows — she has my plan in her drawer." The school nurse holds his asthma action plan. The school, in one of its drawers, has always known exactly why those fourteen days happened; the knowledge simply lived in a different column than the counting.

You write his sentence down in the notebook — not because a ten-year-old's testimony decides adjudications, but because the file will otherwise contain no trace of the person the numbers describe.

**Choices:**
- Take the detail printout to Keller, and then go where the other half of the truth lives: the clinic. → **clerk_honesty**

## [clerk_honesty] Printed and initialed

*Day 6 — Sunday, February 14, 2027*

Ms. Baranski prints the detail — eleven pages — and does the thing that separates a witness from a bystander: she initials every page and dates the set. The code history is now legible to a lay reader: fourteen rows where a received note was mapped, by the migration, into *unexcused*; the original flag preserved in a legacy column, like a word in a dead language that the new system prints but no longer speaks.

She cannot correct the codes herself — that authority sits with the principal, on review. "But this—" the initialed pages go into your folder, "—is what a correction would be correcting *to*. There's a difference between a parent saying the record is wrong and a parent carrying the record that proves it. You are now carrying it."

**Choices:**
- Next: the clinic's half of the torn page. → **dube_visit**

## [dube_visit] The caseworker at the wall

*Day 7 — Monday, February 15, 2027*

Ms. Fontana's home visit is routine in every way but one: she stands in front of the wall calendar for a long moment — clinic stickers, shift marks, dragons — and asks, with the neutrality of a woman photographing something with her eyes, whether the calendar covers the fall term. It does. She notes the visit in her tablet in the usual phrases. Whether the calendar enters the agency's thinking is a question her face declines to answer.

The petition, you reflect after she leaves, was assembled from a summary page and a phone call. Your kitchen wall knows more about Oren's fall than his case file does. The project of the next month is to move the wall's knowledge into the file — in forms a court can weigh.

**Choices:**
- The clinic, then — Dr. Mbeki's office, where fourteen of the twenty-three days are appointments with timestamps. → **clinic_visit**

## [clinic_visit] Dr. Mbeki's front desk

*Day 8 — Tuesday, February 16, 2027*

The clinic's front desk runs on its own paper religion, and it is a stricter one than the school's: appointment histories print with timestamps, cancellations carry reason codes, and the desk clerk finds, without being asked twice, the two November entries — both marked *mother called same day; car trouble; rescheduled by clinic*. The petition's paragraph nine, in the clinic's hand, has a second half.

Fourteen fall visits match the absence detail, date for date, like two halves of a torn page. What remains is to make the clinic's half into evidence — which means asking for it the way evidence is asked for.

**Choices:**
- Sign the release and request the complete appointment history in writing, stamped by the clinic. → **neighbor_note**  _(FLAG: clinicRecords; HIDDEN + Medical records — clinic appointment history requested in writing, matching school absence dates)_
- Take the desk clerk's verbal rundown — she has told you the dates; surely Keller can use your notes. → **neighbor_note**

## [neighbor_note] The rides

*Day 9 — Wednesday, February 17, 2027*

Twice in the fall, when the car was dead in its earlier, warning stages, your neighbor drove you and Oren to the clinic. She writes it down without being asked twice — dates, the dragon in his lap, the stickers — and signs it. It is a small exhibit. It corroborates the calendar, which corroborates the clinic, which corroborates the school's own flags. Cases like this are not won by a document. They are won by documents that agree with each other in front of a judge.

Keller, receiving the growing folder, has begun using a word lawyers ration: *coherent*. "The agency's story is one page. Ours is a system. Systems beat pages, given a judge who reads."

**Choices:**
- Now the agency's own file — request it, and read what the petition was built from. → **clinic_records**

## [clinic_records] Stamped

*Day 10 — Thursday, February 18, 2027*

The clinic's printout arrives stamped and complete: fourteen fall appointments with timestamps; the November pair with their same-day-call annotations; the well-child visit, rescheduled and kept. It is the single most boring document in the case and, Keller says, holding it the way jewelers hold stones, quite possibly the most valuable.

"Petitions are written from summaries. Hearings are decided by alignments. Your son's fall, aligned: the school's flags, the clinic's stamps, a neighbor's rides, a mother's calendar — four independent records, one story. The agency has a number. Numbers without provenance are just typography."

**Choices:**
- Request the agency record — the file the petition came out of — in writing. → **records122**

## [records122] What the petition was built from

*Day 12 — Saturday, February 20, 2027*

The agency's record is releasable on request (55 Pa. Code § 3130.44(d)), and what it holds is the anatomy of paragraph four: the school's summary page, the October truancy printout, and — three pages deeper — a caseworker note from November that you read standing up: *Mother states absences were medical/clinic-related; school to verify coding.* The verification has no follow-up entry. The petition was drafted in January from the summary, by a process that never walked back to its own November doubt.

Keller tabs the note with the gentleness of a man handling the other side's gift. "We don't have to call anyone careless," he says. "The file calls itself unfinished. We just ask the court to finish it."

**Choices:**
- File the request's copy, the tabbed note, and the clinic printout at the front of the hearing packet. → **oren_school_day**  _(cash −12; FLAG: recordsRequested; HIDDEN + Record — agency record requested; file shows verification of absence coding was noted as pending and never completed)_
- The packet is heavy enough. Save the postage and the point. → **oren_school_day**

## [oren_school_day] The nurse's drawer

*Day 13 — Sunday, February 21, 2027*

One more internal contradiction surfaces, through Oren's teacher, who mentions it as the most ordinary thing in the world: the school nurse's asthma action plan — signed by Dr. Mbeki's office in September, filed at school, known to everyone who supervises Oren's breathing. The institution that generated *23 unexcused* also held, the whole time, a clinical document explaining the absences' likeliest cause. Institutions are not minds. They do not know what their drawers know — until a hearing introduces the drawers to each other.

Keller adds the action plan to the alignment: a fifth record, the school's own, agreeing with the other four.

**Choices:**
- Read the agency note once more. Then decide what to do about paragraph nine — the true one. → **agency_note**

## [agency_note] To verify

*Day 14 — Monday, February 22, 2027*

*To verify.* The two words sit in the file like an unmailed letter. Everything in this case — the petition, the number, the dread at the laundromat — descends from a verification that was assigned, in writing, by the agency to itself, and never performed. Keller is careful here, and the care is the lesson: "We do not say they lied. We say the work is unfinished, the allegation is unproven until it is proven, and the burden never moved. (42 Pa.C.S. § 6341(c)) Unfinished work is not evidence. It is a to-do list with a caption."

Your own November — the dead car, the two missed follow-ups, the calls you made — remains in the case, uncorrected by any of this. Strategy for a true paragraph is different from strategy for a false one: you do not rebut it. You own it, with its second half attached, and you fix its cause in writing.

**Choices:**
- Build your side of paragraph nine: the calendar, the clinic's annotations, and a transport plan that survives a dead car. → **mother_calendar**

## [mother_calendar] The wall, copied

*Day 16 — Wednesday, February 24, 2027*

The wall calendar comes down for copying with the ceremony of a flag being retired: photographed whole, then page by page, the clinic stickers and shift marks and dragons intact. Annotated, in your hand, only where annotation is undeniable — the bus-route change week in September, which you mark *my fault, fixed* without being asked, because a calendar that admits one bad week is believed about the other twenty.

Keller adds it to the packet as what it is: a contemporaneous record, made before anyone knew there would be a case, which is the only kind of credibility money cannot buy and advocacy cannot fake.

**Choices:**
- Send the annotated copy to counsel — and then face the meeting the agency has called. → **agency_conference**  _(FLAG: motherNotes)_
- Keep the calendar at home. Some things are the family's, and the file has enough. → **agency_conference**

## [agency_conference] The offer

*Day 17 — Thursday, February 25, 2027*

The pre-hearing conference has coffee, a long table, and an offer — the system's standard instrument for making files like this one go away efficiently. Stipulate: agree that Oren is dependent on the attendance allegation, accept services and supervision, and the agency will recommend he remain at home. No hearing, no cross-examination, no correction of the school's record. The number 23 would stand in the adjudication as an admitted fact — with your signature under its neighborhood.

It is not a villainous offer. It is a *priced* one, and the price is the truth of the fall term, permanently. Keller lets the silence after it run a full five seconds before he looks at you. The decision is yours in a way few decisions in this system are.

**Choices:**
- Decline the stipulation. The attendance allegation is false in its operative number, and falsehoods admitted in March are quoted in September. → **correction_ask**
- Accept the stipulation. Oren stays home, services begin, and the fight ends today — the number be damned. → **stipulated**  _(FLAG: stipulatedFlag)_

## [stipulated] The bargain

*Day 18 — Friday, February 26, 2027*

The stipulation is signed in the conference room, in triplicate, with the coffee going cold. Dependency is admitted on the attendance allegation as written — twenty-three unexcused absences, a pattern of educational neglect, your name beside the words. Disposition is set for March 25, where the agency has signaled it will recommend what it promised: Oren home, under supervision, with services.

Keller walks you out with the folder suddenly light. "You bought certainty," he says. "It is a real currency, and parents spend it for real reasons. I only note what was in the price, because the price is permanent: the school's record was never corrected, the clinic's alignment was never heard, and the number is now a fact you agreed to. It will be quoted back — in reviews, in reports — as an admission, not an error."

**Choices:**
- Go to disposition with the bargain kept and the file unbuilt. → **disposition_day**

## [correction_ask] The principal

*Day 19 — Saturday, February 27, 2027*

The written request to Principal Truman is three pages: the initialed detail printout, the code history, the clinic alignment, and one ask — review the migrated coding for Oren's fall record, correct it if the review bears the detail out, and answer in writing. It is addressed to the only person in the school building who can make a correction outlive a conversation.

What it is not is a demand. Keller's drafting principle: *write the letter the recipient can say yes to without confessing to anything.* The migration was the district's; the correction can be the principal's pride instead of his apology.

**Choices:**
- Attach the initialed detail — the correction needs its target printed and initialed, not described. → **keller_second**  _(REQUIRES: schoolFile)_
- Write from the clinic alignment alone, without the school's own detail printout to anchor it. → **no_audit**

## [keller_second] Owning paragraph nine

*Day 21 — Monday, March 1, 2027*

Keller's second session is about the paragraph you cannot rebut. "We win paragraph four with documents," he says. "We survive paragraph nine with candor and a repair. The calls are in the clinic's own annotations — good. The cause was a dead car — fixable, and we fix it visibly: the clinic runs a transport van for established patients; you enroll, in writing, this week. A judge reading a true allegation next to its documented repair reads a different mother than the petition describes."

He writes the disposition theory on the pad: if — if — dependency is found on the narrow ground, the disposition the law offers includes the child remaining with the parent, subject to supervision and conditions the court prescribes. (42 Pa.C.S. § 6351(a)(1)) Home, with a case, is the honest best this petition can produce — and it is produced by winning the big paragraph and owning the small one.

**Choices:**
- Enroll in the clinic transport program and keep the confirmation — in writing, in the folder. → **audit_wait**  _(cash −6; FLAG: narrowPlan)_

## [no_audit] Reviewed as presented

*Day 24 — Thursday, March 4, 2027*

The principal's reply is prompt, courteous, and final in the way of decisions made on incomplete paper: the attendance record 'as it stands in the system of record' reflects the codes the system carries; individual coding histories are a district-level matter; the school 'cannot undertake case-by-case recoding on parental submission alone.' Your clinic printout is acknowledged as 'helpful context for the future.'

The future is not where adjudications happen. Without the school's own detail — its flags, its legacy column, its clerk's initials — the correction had no skeleton to grow on, and an uncorrected official record walks into March as the fact of the case.

**Choices:**
- Build the hearing packet around what exists: the clinic's alignment, the calendar, the agency's own unfinished note. → **hearing_prep122**

## [audit_wait] The audit

*Day 24 — Thursday, March 4, 2027*

Truman's office confirms the review is underway — an audit of the migrated codes for Oren's record, with the district's data office involved. It will take weeks. Adjudication is March 18. The agency files its exhibit list in the meantime, and it is exactly one page long: the fall attendance summary, offered as a school record, plus the petition's other paragraphs trailing behind it like a tail.

Keller studies the list with open contentment. "They are bringing a summary to a documents fight. A summary is a conclusion wearing a table's clothes — and conclusions, at adjudication, are the one thing the burden of proof exists to cross-examine."

**Choices:**
- While the audit runs, follow the migration's trail — other families, other files, one district memo. → **foster_shadow**

## [foster_shadow] What placement would mean

*Day 26 — Saturday, March 6, 2027*

The stakes, stated once and plainly, because strategy without stakes is bookkeeping: if the attendance allegation is proven as written, disposition could remove Oren — to a foster home, a new school, a nurse who does not have his plan in her drawer, a nebulizer routine in strangers' hands. The asthma that generated the absences would then be managed by the system that miscounted it. Everyone in the case knows this arithmetic. It is why the number matters, and why a stipulation priced at 'home' tempts, and why the correction — not sympathy, the correction — is the whole ballgame.

You attend the next clinic visit by the new transport van, and the driver signs your trip slip, and the slip goes in the folder. Systems, again. Fossils of reliability, accumulating.

**Choices:**
- The migration memo surfaces. Read it the way Keller reads everything: for what it admits. → **school_board**

## [school_board] Known issue

*Day 28 — Monday, March 8, 2027*

The district's data office memo — obtained as an addendum to the school's production — is two paragraphs of bureaucratic prose with a live coal in the second: the October migration's handling of legacy absence flags was a *known issue* affecting 'a subset of records,' identified in November, with recoding 'to be completed as resources permit.' November: the same month the agency's file noted *to verify* and moved on. The district knew its counts were suspect while the agency was drafting a petition from one of them.

No one conspires in this story. That is the story. Two institutions' unfinished work, multiplied by each other, became a mother's alleged neglect — and the only actor in the entire chain who finished her paperwork was the mother.

**Choices:**
- Keller's evidence session: how the two rooms receive all of this. → **keller_evidence**

## [keller_evidence] Two rooms, again

*Day 29 — Tuesday, March 9, 2027*

Keller marks the exhibits and rehearses the law's division of labor until you can recite it. Adjudication: the agency's burden, clear and convincing (42 Pa.C.S. § 6341(c)) — the summary must be *proven*, and its provenance is its weakness: a migrated count, from unverified coding, contradicted by the district's own detail and its own memo. What fails that standard is dismissed. (§ 6341(a))

Disposition is the second room, and only if we reach it: there, written reports may be received freely — *and* examined and controverted, their makers cross-examined. (§ 6341(d)(1), (2)) "In room one, we attack the number's birth certificate. In room two, we present the repair. Never confuse the rooms — parents do, lawyers do, and petitions count on it."

**Choices:**
- The audit's answer is due. Everything now depends on whether it lands before March 18. → **correction_letter**

## [correction_letter] The correction

*Day 31 — Thursday, March 11, 2027*

Principal Truman's letter arrives on school letterhead, and it is the document this scenario exists to produce. The audit is complete. Oren's fall record is corrected in the system of record: **nine unexcused absences; fourteen excused — medical, with notes received**; the migration's mapping error is stated plainly, with the district memo cited; the corrected summary is attached, and the letter closes with the institutional sentence that matters most, because it can be quoted: *The previously issued summary should not be relied upon.*

Keller reads it twice and puts it, without ceremony, at the front of the packet — ahead of the petition's own first page. "Adjudication is a reading," he says. "We have just changed what gets read first."

**Choices:**
- Final preparation: the cross of the summary's maker, and the narrow paragraph's repair, in that order. → **expert_call**  _(FLAG: codingLetter; HIDDEN + School records — attendance record corrected in writing by the school: 9 unexcused, 14 excused-medical)_

## [expert_call] Who made this page

*Day 33 — Saturday, March 13, 2027*

The cross-examination rehearses itself in Keller's office in four questions, addressed to whoever the agency produces to sponsor its summary: Who generated this page? From what system? With what verification of the coding? Are you aware the issuing institution has withdrawn it? The questions are short because the record is long — the alignment does the arguing: school flags, clinic stamps, a neighbor's rides, a mother's calendar, a district's confession, an agency note that says *to verify*.

"At disposition, if we get there, reports can be examined and their makers questioned — that is the statute's own design (§ 6341(d)(2))," Keller says. "At adjudication we need less: only the burden, doing its ordinary work on an extraordinary number."

**Choices:**
- One last piece of disposition paper: the clinic van's confirmation, printed. → **clinic_van**

## [clinic_van] The van, confirmed

*Day 34 — Sunday, March 14, 2027*

The transport program's confirmation letter lists Oren as an established rider: pickup protocol, the clinic's address, your phone number, the backup arrangement for van failures. Paragraph nine's cause — a dead car — now has a documented, redundant system standing where a single point of failure stood in November.

It is a one-page letter about a van. At disposition, it will be the difference between a mother who missed appointments and a mother who missed appointments, diagnosed why, and rebuilt the road. Courts do not grade intentions. They read repairs.

**Choices:**
- Assemble the final packet: petition, detail, correction, alignment, repair — in that order. → **hearing_prep122**

## [hearing_prep122] In that order

*Day 36 — Tuesday, March 16, 2027*

The packet's order is the argument: the petition's claim; the school's own detail, initialed; the district's *known issue* memo; the corrected summary — *should not be relied upon*; the clinic's alignment; the agency's unfinished note; the calendar; the van. Keller has written the adjudication ask in one sentence: the attendance allegation, as pleaded, is not proven by clear and convincing evidence, because the only institution that ever counted it has withdrawn the count. (42 Pa.C.S. § 6341(c), (a))

Tomorrow the agency presents its case first. Its first exhibit is a page its own source has retracted. There are worse positions to defend a family from — Keller has had most of them, he says, and this is not one.

**Choices:**
- Sleep in the specific way of people who have done the work. Court in the morning. → **night_before122**

## [night_before122] Dragons, counted

*Day 37 — Wednesday, March 17, 2027*

Oren, told only that tomorrow is a court day about school, contributes his final exhibit voluntarily: a drawing of the dragon nebulizer, labeled in his careful capitals, with a speech bubble: *I WAS AT THE CLINIC.* It goes on the fridge, not in the packet — some evidence is for the family's record, and the family's record, after this winter, is in excellent order.

You check the packet once. The wall calendar's space is already re-marked for spring: clinic stickers, shift marks, and — new this month — van pickups, in a different color. The archive continues. It was never the problem. It was always the proof.

**Choices:**
- Go to court. → **adjudication**

## [adjudication] Thursday, March 18

*Day 38 — Thursday, March 18, 2027*

Adjudication proceeds as Keller built it. The agency presents: the petition, the summary's sponsor — a supervisor who generated the page from the system of record and concedes, in the cross's fourth question, that she has seen the correction letter and cannot speak for the withdrawn count. The alignment enters without drama: flags, stamps, memo, calendar. The courtroom's temperature is set, as predicted, not by advocacy but by provenance.

The attendance allegation will be decided on whether a retracted number can carry a clear-and-convincing burden. Paragraph nine waits behind it, true and repaired. The court takes the matter under advisement and moves the case to disposition on March 25 — where everything the adjudication decided, and everything it didn't, becomes a plan for a boy's actual life.

**Choices:**
- To disposition, on whatever the record has become. → **disposition_day**

## [disposition_day] Thursday, March 25

*Day 45 — Thursday, March 25, 2027*

Disposition is the second room, with its wider door: reports and evidence helpful to the determination may be received here, and their makers examined. (42 Pa.C.S. § 6341(d)(1), (2)) What the court orders for Oren — home or placement, supervision or none — will be built from the whole winter's record: the number's fate at adjudication, the narrow paragraph and its repair, and the correction's timing, which in this case was everything.

The judge has read the packet. The judge has also, it turns out, read the file.

**Choices:**
- The record holds a retracted count, an institutional correction in writing, a four-way alignment of independent records, and a true paragraph owned and repaired. → **end_narrow**  _(REQUIRES: schoolFile; REQUIRES: codingLetter)_
- The record holds the clinic's alignment and the mother's calendar — but the school's record was never corrected, and the correction letter that would have settled it arrived after adjudication had already taken the official count as proven. → **end_corrected_late**  _(REQUIRES: clinicRecords; REQUIRES-NOT: codingLetter)_
- The record holds an admitted allegation, signed for in a conference room — no hearing, no correction, no alignment ever heard. → **end_stipulated**  _(REQUIRES: stipulatedFlag)_
- The record holds a summary, a sponsorship, and a mother's say-so — against a burden that was never hers to carry and a number nobody made the system defend. → **end_placed**

## [end_narrow] Ending — Home, on the Narrow Ground

*Day 45 — Thursday, March 25, 2027*

**Ending.**

**Debrief:** The attendance allegation is dismissed — not mitigated, not discounted: not proven. The court's adjudication findings say it in the burden's own grammar: on the attendance count, the evidence — a summary withdrawn by its issuing institution, contradicted by the institution's own detail, its own memo, and an alignment of clinic records — does not constitute clear and convincing evidence of educational neglect. (42 Pa.C.S. § 6341(c)) The allegation fails, and with it the petition's centerpiece. (§ 6341(a)) What remains is paragraph nine, the true one: two missed follow-ups, proven, and answered at disposition with their cause repaired in writing. The disposition is the statute's first option: Oren remains with you, subject to supervision and to conditions — the clinic van enrollment among them, recited in the order. (42 Pa.C.S. § 6351(a)(1))

Name the win precisely, because its shape is the lesson. The number was defeated by provenance, not passion: a written request for the school's *detail* rather than its summary; a clerk's initialed printout; a principal's corrected letter — *should not be relied upon* — obtained by asking the one person who could issue it, in a letter he could say yes to; clinic records aligned date-for-date; the agency's own record (55 Pa. Code § 3130.44(d)) supplying the *to verify* that was never verified. And paragraph nine was not rebutted but owned, because a parent who concedes the true paragraph with a documented repair is believed about the false one. Both halves were strategy. Neither half works alone.

What no strategy controls: a judge less patient with provenance; a clerk less brave than Ms. Baranski; a district that corrects slower. The case is not closed — supervision runs, reviews recur, and Oren's asthma does not consult the court calendar. But the file that follows this family now says what actually happened in the fall: nine, and fourteen-with-notes, and a mother who caught the error the institutions filed past each other. Permanently. In the record. Where it will be quoted from, correctly, from now on.

## [end_corrected_late] Ending — Corrected, One Hearing Late (partial)

*Day 45 — Thursday, March 25, 2027*

**Ending.**

**Debrief:** The correction letter reached the file on March 24 — six days after adjudication took the official record as it stood. It changed disposition profoundly and adjudication not at all. The court's disposition is merciful and specific: Oren remains home under supervision (42 Pa.C.S. § 6351(a)(1)), the corrected summary is attached to the order, and the agency is directed to conform its records. But the adjudication itself — dependency founded on the attendance allegation as pleaded, twenty-three unexcused — stands in the case's history as a found fact, correctable on paper everywhere except the one page that decided it.

The autopsy is one of sequence, not effort. The clinic alignment was built. The calendar was kept. What never existed was the school's own *detail* — the initialed printout with the legacy flags — because the request for it was never made in writing, and without the detail, the principal's review had nothing to correct *to*, and answered, reasonably, from the system of record as it stood. Every institution in this story behaved the way institutions behave with the paper in front of them. The paper in front of them was the variable. It usually is.

Partial, and far from empty: Oren is home, supervised, his school record corrected at the source, the agency directed to conform — a foundation most families would take. What was lost is narrower and worth naming in a training library: the difference between a record corrected before adjudication and after it is the difference between an allegation *dismissed as unproven* (§ 6341(a)) and an allegation *found, then forgiven*. Files remember which. So do future petitions. The detail request is a five-minute letter. File it in the first week, not the last.

## [end_stipulated] Ending — The Bargain

*Day 45 — Thursday, March 25, 2027*

**Ending.**

**Debrief:** Disposition keeps its promise: Oren remains at home, under supervision and services, exactly as the conference-room offer described. No removal, no foster home, no stranger holding the nebulizer. On the outcomes that keep a family intact, this ending delivers — and the debrief will not pretend otherwise, because parents who take this bargain are not fools, and a library that calls them fools teaches nothing.

The price is itemized in the file, where prices in this system live. The adjudication rests on an *admission*: twenty-three unexcused absences, educational neglect, agreed and signed. The school never corrected its record under the pressure of a hearing; the clinic's alignment was never heard; the agency's *to verify* was never read aloud. Every future reader of this file — the next caseworker, the next report writer, the next judge — will meet the number first, armored now in the one thing that makes numbers immortal: the mother's own agreement. Reviews will quote it. Summaries will copy it. It will be, forever, what the fall of 2026 *was*.

What no strategy controls is also honestly part of this ending: hearings are gambles, judges vary, and the certainty bought here — a son home tonight, services started, no removal risk this spring — is real value purchased with a real record. The scenario's doctrine is only about seeing the price tag before signing: a stipulation is not the end of a fight but a *settlement of the facts*, and in a system that runs on files, facts are the one currency that never devalues and never expires. The correction remains available — school records can still be pursued, reviews still argued. But it will now be argued uphill, against an admission, by the person who signed it.

## [end_placed] Ending — Twenty-Three, Standing

*Day 45 — Thursday, March 25, 2027*

**Ending.**

**Debrief:** The number stands. Adjudication found the attendance allegation proven on the strength of the only document anyone sponsored — the summary — the mother's contrary account being, in the court's unavoidable phrase, *uncorroborated by records*. Disposition continued the logic: placement with a foster family, services for the mother, reviews to come. Oren packs the dragon in a bag that a stranger's household will learn to plug in. The correction of his school record — if it ever comes — will arrive as an erratum to a case that has already been decided by its error.

This is the ending the burden of proof exists to prevent, and its mechanics deserve the cold light. The burden never moved: dependency required clear and convincing evidence (42 Pa.C.S. § 6341(c)), and a migrated count from unverified coding is not that — *when someone makes the court look at it*. Nobody did. The detail was never requested in writing; the clinic's alignment was never assembled; the agency's record — with its own *to verify*, releasable on request (55 Pa. Code § 3130.44(d)) — was never requested at all. Against a sponsored summary, the defense offered the truth, unexhibited. Truth is the beginning of a case. It is not, in a paper system, the case.

It is not the end of the story — reviews recur on the statute's clock, corrections can still be pursued and filed, and Oren's mother retains every tool this scenario inventoried, now at the higher prices appeals and reviews charge. But the doctrine has rarely had a cleaner demonstration: institutions generate numbers; numbers generate petitions; and the only force ever documented to reverse the sequence is a parent, early, in writing, asking the system for its own detail — and carrying the answer into the room where burdens live.
