#!/usr/bin/env python3
"""Generate scenarios 121-122 (Wave 2, Batch 9: Education & Medical).
Fictional composites only."""
import sys
sys.path.insert(0, "/home/hatch/workspace/your_files/tacticwatch-game")
from batchN_lib import N, C, E, emit, fmt
from datetime import date, timedelta

# ============================================================ S121 (Complex)
S = date(2026, 9, 7)
assert fmt(S) == "Monday, September 7, 2026"
assert fmt(S + timedelta(days=11)) == "Friday, September 18, 2026"    # reconvened BID
assert fmt(S + timedelta(days=14)) == "Monday, September 21, 2026"    # scheduled transfer date
assert fmt(S + timedelta(days=38)) == "Thursday, October 15, 2026"    # review hearing
PLACED = date(2026, 8, 10)
assert fmt(PLACED + timedelta(days=457)) == "Wednesday, November 10, 2027"  # 15 calendar months in care

s121_meta = {
    "title": "The First 90 Days",
    "subtitle": "Scenario 121 — The Meeting That Happened Without Her (a fictional composite)",
    "startDateISO": "2026-09-07",
    "startNode": "start",
    "startCash": 160,
    "tier": "Complex",
    "summary": "You are Reginald Bly. Your daughter Alina, twelve, is placed with her grandmother two districts away. A letter has just informed you that her school was decided last Tuesday — at a best-interest meeting you were never told about, in a process you have never heard of.",
}

s121 = [
 N("start", 0, "Will be enrolled",
   ["The letter is from the school district where your mother lives, and its grammar is the first injury: *Alina Bly will be enrolled at Jefferson Middle School effective Monday, September 21.* Not *may*. Not *the district proposes*. Will — the future tense of a decision already made, arriving at the father's address like a weather report.",
    "Alina has been at her grandmother Wilma's since August 10, placed there by a court after your injury, your lost job, and the spring when a twelve-year-old quietly became the adult in your house. Her school — her math team, her science project, the counselor who knows the whole story — is nineteen miles in the other direction. Nobody has asked you about any of this. You did not know there was an asking."],
   [C("Call your mother first. If a decision was made, somebody in this family was in the room.", "backstory121")]),

 N("backstory121", 0, "How Alina got to Wilma's",
   ["The record, in the order it deserves: your wife died two years ago. Your back went in March — a warehouse lift, a disc, a surgery date that kept moving. By May, Alina was making the lunches, signing your name to the forms she could reach, and falling asleep in second period. The school reported what it saw, accurately. The petition that followed was, in its facts, also accurate.",
    "Dependency was found; disposition placed Alina with your mother — her grandmother, her favorite person, in a house an hour's bus ride from yours and two districts from her school. You visit twice a week. You are healing, working light duty since August, doing the plan. The plan, as written, mentions Alina's school exactly nowhere — an omission that seemed harmless until a letter used the words *will be enrolled*."],
   [C("Call Wilma.", "wilma_call")]),

 N("wilma_call", 1, "Bus paperwork",
   ["Wilma is indignant in the specific way of a woman discovering she has been used as a rubber stamp. Yes, she took a call on September 1 — from the agency, she thought, about *bus paperwork*. A nice man asked whether Alina was settled, whether the school near her house was 'fine.' She said the child was settled and the school was a school. Nobody said the words *best interest*. Nobody said a determination was being made. Her assent, such as it was, is apparently in a file somewhere wearing a suit.",
    "\"Reginald,\" she says, \"if they'd told me it was a meeting, I'd have worn my meeting voice. And I'd have told them to call her father.\" She is already reaching for a pen: whatever she said, she will now say what it was — on paper."],
   [C("Ask her to write exactly what that call was — and then find out what a 'best-interest determination' is supposed to be.", "bid_reveal", setFlags=["wilmaStatement"])]),

 N("bid_reveal", 2, "September 1",
   ["Ms. Vadnais, the caseworker, confirms the architecture without embarrassment. A best-interest determination — a BID — was held September 1 at the district office: agency, school district staff, and 'the caregiver, by phone.' The determination: transfer serves Alina's best interest, citing proximity to her placement. You were not notified, she explains, because school notifications to parents in your posture 'usually run through the agency,' and the agency's letter went to your previous address — the one on the petition, from March.",
    "Your current address is on the agency's visitation file, the medical file, and four months of sign-in sheets. It is not on the letter that decided your daughter's school."],
   [C("Call the guardian ad litem — Mr. Havel represents Alina. Was he in the room?", "gal121")]),

 N("gal121", 3, "Not in the room either",
   ["Mr. Havel was not in the room either — he learned of the BID from the same letter you did, a day later. His professional annoyance is a useful instrument: layered, precise, and aimed. \"A determination about a child's best interest,\" he says, \"was made by a subset of the people the word *interest* involves. I will be saying so, in writing, to both districts. Whether the court ever hears it depends on whether someone builds the record. That someone, Mr. Bly, is you.\"",
    "He gives you the lawyer's name — Ms. Anselmi — and the advice that organizes the rest of this scenario: \"Do not fight the letter. Fight for the determination to be made again, properly, before September 21. A process redone is winnable. A process denounced is just weather.\""],
   [C("Ms. Anselmi's office. Bring the letter, your mother's account, and every address you have ever given the agency.", "lawyer121")]),

 N("lawyer121", 3, "All the factors",
   ["Ms. Anselmi puts the federal standard on the whiteboard, because it is shorter than the system's behavior suggests. A child in foster care enrolls or remains in her school of origin *unless a determination is made that it is not in her best interest to attend it* — and that determination is to be based on *all factors relating to the child's best interest, including consideration of the appropriateness of the current educational setting and the proximity to the school in which she was enrolled when placed*. (20 U.S.C. § 6311(g)(1)(E)(i))",
    "\"Now measure September 1 against the sentence,\" she says. \"One factor — proximity. A caregiver consulted about bus paperwork. A parent at an address the agency itself doesn't use. A teacher never asked. That is not a determination based on all factors; it is a default wearing a determination's clothes. We ask — in writing, to the agency and both districts — for the determination to be made again, with the parent present, the teacher heard, and the answer written. And we ask before September 21, because undoing an enrollment is heavier than pausing one.\""],
   [C("Sign the written objection and demand for a reconvened determination — to the agency, both districts, copies everywhere.", "objection_sent", setFlags=["bidObjected"], addHidden=["School — written objection to best-interest determination; reconvened determination demanded before transfer date"]),
    C("Call Ms. Vadnais first. A demand letter feels like an escalation; a conversation might soften the agency into redoing it voluntarily.", "phone_fight")]),

 N("phone_fight", 4, "Expressed disagreement",
   ["The conversation is courteous and weightless. Ms. Vadnais understands your concern. The determination is, however, 'final for this semester' — a phrase with no citation attached, because none exists. She will note your objection in the file. When Ms. Anselmi later reads the file note, it says, in full: *father expressed disagreement re: school*.",
    "\"Expressed disagreement,\" Ms. Anselmi says, \"is what a written demand looks like after a phone call metabolizes it. We are going to write the letter anyway — a week of its force already spent on courtesy.\""],
   [C("Write the letter now: objection, the factor list, the demand for a reconvened determination before September 21.", "objection_sent", setFlags=["bidObjected"], addHidden=["School — written objection filed after verbal objection was recorded only as 'expressed disagreement'"]),
    C("Accept the finality. The districts have decided; spend your strength on the case plan instead.", "default_path")]),

 N("objection_sent", 5, "The letter, out",
   ["The objection goes to four addresses: the agency, the district of origin, the district of placement, and the court file through counsel. Its exhibits are modest and devastating: the enrollment letter's date; your mother's account of the September 1 call; the visitation file's address page — your real address, in the agency's own records since May. It asks for three things: the determination reconvened with all factors considered; the parent present; enrollment held meanwhile.",
    "Paper this specific creates a problem institutions cannot file under weather: someone, somewhere, has to answer it with their name attached."],
   [C("Now the file itself — ask for the agency record, and the BID's own paper, in writing.", "records121")]),

 N("records121", 6, "The determination's paper",
   ["The regulation gives you the ask: the agency's case record is to be released on request. (55 Pa. Code § 3130.44(d)) You request the whole record — and by name, everything touching the September 1 determination: the meeting notice, the attendee list, the BID form itself.",
    "Files answer lists. This list is about to learn what September 1 actually consisted of — which matters more than what it concluded."],
   [C("Sign it, date it, send it so it leaves a trail, keep the copies.", "vadnais_letter", setFlags=["recordsRequested"], cash=-10, addHidden=["Record — agency record and BID documentation requested in writing"]),
    C("Rely on the districts' copies instead — the agency's file will just duplicate them.", "vadnais_letter")]),

 N("vadnais_letter", 7, "As listed",
   ["The agency's written response arrives with the speed of an institution that has consulted its counsel: the determination, it maintains, was properly made; notice to the father was sent to the address 'as listed.' Attached — whether by candor or by clerical accident, you will never know — is the address page from the petition, March's address, beside a routing stamp from the visitation unit, bearing your current address, dated May.",
    "Ms. Anselmi puts both pages in one exhibit sleeve. \"Institutions rarely confess,\" she says. \"They file. We just make sure the filing reaches the room.\""],
   [C("Take the exhibit sleeve to the one office that has been silent so far: the district of origin's foster care point of contact.", "district_poc")]),

 N("district_poc", 8, "The other district",
   ["The district of origin keeps a foster care point of contact because federal law expects the collaboration to have a name: districts are to collaborate with the child welfare agency, designate a point of contact, and maintain clear written procedures for keeping a child in her school of origin — transportation included. (20 U.S.C. § 6312(c)(5)) The point of contact, reading your packet, displays the professional embarrassment of a man discovering his own district never received the BID notice either: September 1's 'district staff' were from the *receiving* district. The school that stands to lose Alina was not in the room when her best interest was determined.",
    "\"Then the room was missing three of its chairs,\" he says. \"Mine, yours, and her teacher's. I'll sign the request for a reconvened determination myself.\""],
   [C("With the district's own point of contact co-signing the ask, assemble the September 1 paper when it arrives.", "bid_paper", setFlags=["districtAlly"])]),

 N("bid_paper", 9, "One factor, scored",
   ["The BID file, produced under your record request, is four pages — and the determination's form is the most eloquent document in this case. Its factor list mirrors the statute's: appropriateness of the current educational setting; proximity; the child's attachments and programs; input from the parent; input from the child's teachers. Against nearly every line: *not obtained*. Against proximity alone: a score, a note, a signature.",
    "A determination 'based on all factors' (20 U.S.C. § 6311(g)(1)(E)(i)) cannot be built from one factor and four blanks. Nobody has to accuse September 1 of bad faith. Its own form accuses it of being unfinished."],
   [C("Fill the blanks. Start with the teacher who was never asked — Ms. Aldana, who has taught Alina for two years.", "teacher_call")]),

 N("teacher_call", 9, "The teacher who was never asked",
   ["Ms. Aldana answers the school's phone with two years of Alina in her voice. Advanced mathematics — placed by assessment in June, a track the receiving district rebuilds from its own testing, weeks into the term, if at all. The science-fair project, mid-build. The counselor relationship, built across the year her mother-in-fact — no, her *grandmother* — no. Built across the year Alina's mother died. \"Nobody asked me anything,\" she says. \"I read about the transfer in the office copy of the letter. I assumed you'd been consulted. Parents usually are. That's the assumption everyone at my end was working under.\"",
    "Assumptions, all the way down — and every one of them filing itself as a fact."],
   [C("Ask her to put it in writing for the reconvened determination: the track, the project, the counselor — dated, signed, on school letterhead.", "wilma_statement", setFlags=["teacherHeard"]),
    C("Take her verbal support as enough — the meeting will hear the father's voice; paper from a teacher is a bonus.", "wilma_statement")]),

 N("wilma_statement", 10, "Wilma's meeting voice",
   ["Your mother writes her statement at the kitchen table, in her meeting voice, in ink: what the September 1 call was (six minutes, about buses), what she was never told (that a determination was being made, that her answers were the caregiver consultation), and what she would have said if asked the real questions — including that Alina cries about the math team in the specific way she cries about nothing else.",
    "She signs it, dates it, and adds a postscript that advocates will quote for years: *I am the placement. I am not the parent. You have his address.*"],
   [C("One voice remains unconsulted in this entire file. Ask Alina what she wants — and whether she will write it.", "alina_voice121")]),

 N("alina_voice121", 10, "Her paragraph",
   ["Alina writes her paragraph at Wilma's table after dinner, with the seriousness of a girl who has been discussed in paragraphs for months and is finally holding the pen. She wants to stay at her school. The bus is long and she does not care. The math team is hers. She understands adults decide; she asks that this be in the file when they do: *I already changed houses. I don't want to change everything.*",
    "Whether a child's paragraph is evidence, input, or merely the point of the entire proceeding is a question systems answer differently. It is undisputed that a file deciding her best interest should contain it."],
   [C("Ask her permission to file it with the determination packet — her words, her name, her choice.", "bid_date", setFlags=["alinaVoice"]),
    C("Keep it in the family. She has been paperworked enough.", "bid_date")]),

 N("bid_date", 10, "Friday, September 18",
   ["The answer to the objection arrives from the agency's counsel, in the register institutions use when they are conceding the minimum real thing: *without prejudice to the September 1 determination*, a reconvened best-interest meeting will be held Friday, September 18 — the parent to attend, the child's teacher invited, both districts represented — and enrollment will be held in place pending its outcome. The stay exists because the objection asked for it in writing, with a date in it. September 21 stands still, for now, at the edge of the calendar.",
    "Three days. The packet is nearly built. What it still lacks is the piece that kills more school-stability cases than every legal argument combined: the ride."],
   [C("Do the transportation math before the meeting does it at you.", "transport_math")]),

 N("transport_math", 11, "Nineteen miles",
   ["The geography, unsentimentally: Wilma's house to Alina's school, nineteen miles. The origin district's bus route passes four miles from Wilma's door. Wilma works part-time afternoons and can drive mornings. You work light duty with Fridays variable. The statute's procedures exist for exactly this arithmetic: transportation to the school of origin is to be provided, arranged, and funded under the district's written procedures, with additional costs met by the child welfare agency's reimbursement, by the district, or shared. (20 U.S.C. § 6312(c)(5)(B))",
    "Three doors for the money. What the meeting needs is a father who has already walked through one of them, on paper."],
   [C("Draft the shared plan: Wilma drives mornings; the district extends its existing route the last four miles in the afternoons; the agency reimburses the mileage difference; you cover Fridays. Bring it printed.", "pre_bid_prep", setFlags=["transportPlan"]),
    C("Go to the meeting on the merits and let the professionals solve transportation, as the law's procedures promise they will.", "pre_bid_prep")]),

 N("pre_bid_prep", 11, "The factor walk",
   ["Ms. Anselmi rehearses you the way she rehearses everyone: the determination will walk the factor list, and you will have one disciplined sentence per factor, with a document behind each. Current setting: Ms. Aldana's letter. Proximity: nineteen miles, and a costed transport plan — or, without one, a hole the other side will pour concrete into. The child's own input: her paragraph, if she has allowed it. The September 1 paper: unfinished, on its own form.",
    "\"We are not arguing that proximity doesn't matter,\" she says. \"We are arguing that a determination is a thing with parts, and September 1 was missing most of them. Make them do it whole.\""],
   [C("Walk into the reconvened determination.", "bid_day")]),

 N("bid_day", 11, "The meeting, again",
   ["The room is fuller this time, which is the first finding. Both districts. The agency. Mr. Havel. Ms. Aldana by phone, her letter in the packet. Your mother's statement. Your daughter's paragraph, if it is in the file, read into the meeting's record by the chair without commentary — the sound of a child's handwriting being taken seriously is a particular silence.",
    "The factors are walked, one by one, because the objection demanded they be. And then the meeting arrives, as every such meeting arrives, at the last box on the form: transportation — the place where best interests go to be priced."],
   [C("Put your printed plan in the center of the table: who drives, which route, whose dollars — reimbursement, district, shared, in the statute's own three doors.", "bid_outcome_fork", setFlags=["transportFunded"]),
    C("Argue the merits and leave the last box to the room's goodwill — surely, with the factors this clear, someone will own the ride.", "bid_outcome_fork")]),

 N("bid_outcome_fork", 11, "What the room decides",
   ["The determination is re-made in the room — deliberated this time, on the full factor list, with your exhibits sweating in the middle of the table. What it decides turns on a brutally simple variable: whether staying at Alina's school is a plan with a funded ride inside it, or a principle with a hole where the ride should be.",
    "The letter confirming it will follow within days. Either way, the case now moves toward the October review — and the review will read whichever version of September your choices left in the file."],
   [C("The determination, re-made, keeps Alina at her school — with the transportation plan written into it as a term, funded and assigned.", "post_bid_origin", requiresFlags=["bidObjected", "transportFunded"]),
    C("The determination keeps Alina at her school in principle — and leaves transportation 'to be arranged,' unassigned and unfunded.", "post_bid_origin", requiresFlags=["bidObjected"], requiresNoFlags=["transportFunded"]),
    C("The determination, re-made on all the factors this time, still lands on transfer — proximity and a fresh start outweighing the rest, on a record that finally says why.", "post_bid_transfer", requiresFlags=["bidObjected"])]),

 N("post_bid_origin", 12, "The letter, corrected",
   ["The confirming letter uses a different grammar than the first one. Not *will be enrolled* — *will remain*. Alina keeps her school: her math track, her project, her counselor, her paragraph now permanently in the file that decides things about her. What remains to be seen is whether the arrangement survives contact with October — buses, mileage forms, a grandmother's alarm clock, a father's Fridays.",
    "School stability, it turns out, is not an event. It is a route that has to be driven, in both senses, every day."],
   [C("Drive it. The next three weeks are the review's evidence.", "first_bus_week")]),

 N("first_bus_week", 16, "The route, running",
   ["Week one of the arrangement: Wilma's car at 7:10, the handoff at the route's last stop, Alina boarding the origin district's bus with her project folder like a commuter with a briefcase. She is, her counselor reports, *annoyingly awake* in first period. The math team practices Tuesdays. The science fair board acquires its second panel.",
    "Ms. Aldana emails you — you, directly, because the file now has your address right — a one-line progress note. These are the documents October's review will be made of, and they are accumulating the way all decisive evidence accumulates: on ordinary days, without ceremony."],
   [C("Keep every one. And when the mileage invoice arrives, read it as carefully as any court paper.", "math_team")]),

 N("math_team", 21, "The math team final",
   ["The math team makes its regional final — a fact Alina delivers at Wilma's table with the paragraph-writer's own hand now steady enough to add: *told you*. Her placement on the team exists because a June assessment put her in the advanced track, and the track exists because a school across two district lines kept her file whole. In the transfer version of this autumn — the one September 1 designed — the final happens without her, and no document anywhere records the loss, because losses that consist of things not happening leave no paper. This one nearly did.",
    "You file the tournament program in the review packet, between the transport invoices — the two kinds of evidence a school case runs on: what it costs, and what it's for."],
   [C("The mileage invoice arrives. Paper meets paper.", "route_bill")]),

 N("route_bill", 24, "The invoice",
   ["The mileage and route-extension accounting arrives with an institutional stumble in it: the agency's share is processed late, the district's paperwork wants a form the agency hasn't countersigned, and for nine days the arrangement runs on Wilma's credit card and Wilma's faith. It is resolved — the countersignature lands, the reimbursement posts — because every party's obligation was written into a determination with names and numbers, and written obligations can be chased. Unwritten ones can only be mourned.",
    "You keep the whole paper trail: the promise, the stumble, the chase, the cure. At the review, it is the difference between *the plan works* and *the plan works on paper*."],
   [C("One honest conversation remains before the review: how long can Wilma carry the mornings?", "wilma_tired")]),

 N("wilma_tired", 30, "Wilma's alarm clock",
   ["Your mother, at her table, in her meeting voice: \"I will drive that girl until I am ninety if the court orders me to. But a plan that depends on a seventy-one-year-old never being sick is not a plan, it's a hope with a license plate.\" She is right, and her rightness is the review's business: the arrangement needs a documented backup — your Fridays formalized, a neighbor on the route vetted as the relief driver, the district's contingency noted in the file.",
    "You build the backup in writing, because backups, like everything else in this case, exist when they are on paper and evaporate when they are understood."],
   [C("File the backup plan with the agency and both districts; put a copy in the review packet.", "review_prep", cash=-14),
    C("Trust the arrangement's momentum. It has survived a month; don't reopen what works.", "review_prep")]),

 N("post_bid_transfer", 12, "A fairer letter",
   ["The confirming letter still says transfer — but it is a different species of document from September's. This one recites the factors: the advanced track, weighed; the counselor, weighed; your daughter's paragraph, quoted; proximity and the transport burden, weighed heavier. September 21 stands. Alina will change schools — after a determination that finally did the work its name promises, in a room you were in, on a record you can read, appeal, and hold the system to.",
    "Losing properly is not winning. But the record of a proper loss is a tool: it fixes the reasons, and reasons can change. What happens next decides whether the transfer is a rupture or a bridge."],
   [C("September 21. Enrollment day — and the law has instructions for that day too.", "enrollment_day")]),

 N("enrollment_day", 14, "Enrolled on the day",
   ["Alina is enrolled at Jefferson Middle School on Monday, September 21, immediately — as the federal assurances require when a determination goes against the school of origin: immediate enrollment in the new school even without the records normally required, and the enrolling school reaching back at once for her academic and other records. (20 U.S.C. § 6311(g)(1)(E)(ii), (iii)) She has a locker by ten and a schedule by eleven. The machinery of arrival works. What machinery cannot do is move her *placement in the advanced track* — that lives in assessments, and assessments have calendars.",
    "You watch her walk in with the folder she would not let anyone carry. The fight is not over. It has changed weapons: from preventing a transfer to prosecuting its paperwork."],
   [C("Chase the records transfer like it owes you money. Every day without her file is a placement decision being made by an empty folder.", "alina_new_school")]),

 N("alina_new_school", 17, "It's fine. It's just not mine",
   ["Alina's review of Jefferson, delivered at Wilma's table with a fork suspended: \"The kids are fine. The teachers are fine. It's fine. It's just not mine.\" Her classes are the standard track — the receiving school places by its own assessment, scheduled for October, and until then a girl who was doing advanced work does ordinary work well and gets quietly bored in the specific way that precedes trouble.",
    "The records from her old school arrive in pieces: grades first, then attendance, then — the piece that matters — nothing about the advanced placement, which traveled, as such things do, in a separate system that nobody requested by name."],
   [C("Request it by name: the assessment record, the track placement, the counselor's file — in writing, to both districts.", "records_chase")]),

 N("records_chase", 20, "By name",
   ["The lesson of this whole case applies to paper as to meetings: lists get answered. Requested by name, the assessment record surfaces in six days — June's scores, the placement memo, Ms. Aldana's cover note, which includes a sentence the receiving school's counselor reads twice: *This student should not be re-assessed downward by default; her placement reflects two years of data.*",
    "The receiving district schedules Alina's placement review — its own process, its own calendar — for late October. After the review hearing in her dependency case. Which means the October review, in court, becomes the room where the school question is argued with the whole record finally assembled, including what a proper determination costs when it still comes out *transfer*."],
   [C("Assemble it all for the review: both determinations, the full factor record, the enrollment paper, the assessment file.", "review_prep")]),

 N("default_path", 8, "Final for this semester",
   ["The phrase does its quiet work. No letter is written; no determination is reconvened; the file's account of your position remains four words — *father expressed disagreement* — and September moves at its usual speed toward the 21st. Ms. Vadnais is not unkind about it. Systems are rarely unkind about their defaults. They are simply already in motion, and motion is most of what a default is.",
    "Alina asks Wilma once whether the bus question was ever decided. Wilma, who took a six-minute call about paperwork, says the truest sentence in the case: \"Baby, I believe it was decided by people who never said the word *decided* out loud.\""],
   [C("September 21 arrives.", "transfer_monday")]),

 N("transfer_monday", 14, "A locker, eventually",
   ["Alina starts at Jefferson Middle School on September 21 — not immediately, in the way the federal assurances describe when a real determination has been made (20 U.S.C. § 6311(g)(1)(E)(ii)), but eventually, in the way of processed paperwork: two days of schedule confusion, a week for her records to be requested, longer for them to arrive, and an assessment for the advanced track scheduled at the district's convenience in November. Nobody violated anything anyone can point to. The determination that was supposed to structure all of this was made in six minutes, on one factor, and its thinness is now simply the medium Alina swims in.",
    "She adapts, the way the system counts on children adapting. The costs are itemized nowhere, which is where such costs prefer to live."],
   [C("Read the ending of the September that was decided by a phone call about buses.", "end_default")]),

 N("review_prep", 35, "The school chapter",
   ["The review packet's school chapter is, by now, a small book: two determinations — the six-minute original and its reconvened successor; the factor record, blanks and all, beside the same form filled; a teacher's letter; a grandmother's statement; a daughter's paragraph; invoices, programs, enrollment records, assessment files — whichever subset your autumn actually built.",
    "Ms. Anselmi arranges it in the order the court determines things. \"October's hearing is about the whole case — necessity, compliance, progress, efforts. (42 Pa.C.S. § 6351(f)) School is where several of those words will be read from. Let's make the reading accurate.\""],
   [C("One page of drafted findings language, in the statute's own order, and then court.", "anselmi_findings")]),

 N("anselmi_findings", 36, "Findings, drafted",
   ["Ms. Anselmi drafts the ask as findings, because judges sign findings more readily than essays. On the school question, in whichever direction the record runs: that the court note the determination history — what September 1 was, what September 18 made of it — and direct the parties to maintain the arrangement the record supports, with the transportation terms (or the placement review) stated in the order itself, where defaults cannot edit them.",
    "\"An order is the only memo a system cannot misfile,\" she says. \"We are asking the court to write the school chapter into one.\""],
   [C("Go to court.", "review_day")]),

 N("review_day", 38, "Thursday, October 15",
   ["The review runs the statute's determinations — continuing necessity of placement, compliance with the permanency plan, progress toward alleviating the circumstances that caused placement, reasonable efforts to finalize the plan. (42 Pa.C.S. § 6351(f)(1), (2), (3), (5.1)) Your progress is real and is found. Then the court reaches the school chapter, and reads — as courts do — what the file actually holds.",
    "The school question is answered by the autumn that built it."],
   [C("The file holds a gutted original determination, a reconvened one made on all the factors, and a funded transportation plan already running — with invoices to prove it.", "end_origin", requiresFlags=["bidObjected", "transportFunded"]),
    C("The file holds a proper determination and a kept school — but the ride belongs to a seventy-one-year-old's alarm clock, unfunded and unbacked.", "end_unfunded", requiresFlags=["bidObjected"], requiresNoFlags=["transportFunded"]),
    C("The file holds a determination done properly the second time — and a transfer that survived it, with the paperwork now prosecuted to a whole record.", "end_fair_transfer", requiresFlags=["bidObjected"])]),

 E("end_origin", 38, "Ending — Nineteen Miles, Funded",
   ["The review order does the thing Ms. Anselmi asked: it writes the school arrangement into the order itself. Alina remains at her school of origin; the transportation plan — Wilma's mornings, the district's extended afternoon route, the agency's reimbursement share, your Fridays, the documented backup — is recited as a term, with the invoice paper attached as the court's own exhibit of a plan that has already survived a month of Tuesdays. The judge's one oral addition is aimed at the file: \"The next determination about this child's schooling will be made the way the September one was made the second time. The first way is not a way.\"",
    "Name what won, with the statute open. The right is structural: remain in the school of origin unless a determination — based on *all* factors relating to best interest, including the appropriateness of the current setting and proximity — decides otherwise. (20 U.S.C. § 6311(g)(1)(E)(i)) September 1 honored it in the breach: one factor, four blanks, a parent notified at a dead address, a caregiver consulted about buses. The counter-machinery was equally structural: a written objection with the factor list in it; the agency record requested (55 Pa. Code § 3130.44(d)), whose four-page BID form testified against itself; a teacher's letter; a kin caregiver's statement; a child's paragraph; and — the load-bearing piece — a transportation plan walked through the statute's three funding doors (agency reimbursement, district payment, or shared cost, 20 U.S.C. § 6312(c)(5)(B)) and laid on the table before the room had to price a principle.",
    "What no strategy controls: November 10, 2027, when Alina reaches fifteen of her twenty-two months in care and the termination-petition question arrives with its own exceptions (42 U.S.C. § 675(5)(E)) — this scenario ends thirteen months before that clock strikes, and its debrief will not pretend the school win settles it. A route can be redrawn; a grandmother can get the flu; determinations can be revisited when facts change, by any side. What this autumn controlled was narrower and complete: the decision about a child's school was made on purpose, by the full list of people the word *interest* involves, in writing. That is the whole doctrine of this scenario. It is also, not incidentally, the law."]),

 E("end_unfunded", 38, "Ending — Kept, on a Grandmother's Alarm Clock (partial)",
   ["Alina keeps her school. The review confirms the reconvened determination, praises the factor record — and then the judge reads the transportation paragraph that your September left blank, and her pen slows. The arrangement she is asked to ratify runs on a seventy-one-year-old woman's mornings, unpriced and unbacked. The order ratifies it for sixty days and directs the parties to return with the transportation terms — funding, backup, contingency — in writing, the review continued on that single question. You won the school. You were assigned the ride as homework, by a judge who has seen what unfunded victories do by November.",
    "The accounting is exact. The reconvened determination happened because the objection was written, dated, and served — and because the record request (55 Pa. Code § 3130.44(d)) produced a four-page form that no advocate could have summarized as devastatingly as it summarized itself. The merits were fully built. What was left to 'goodwill' was the box the federal procedures exist to fill: transportation to the school of origin is to be provided, arranged, and funded under written procedures, the additional costs answered by reimbursement, district payment, or sharing. (20 U.S.C. § 6312(c)(5)(B)) A principle in that box is a plan with a hole in it, and holes in October become gaps in January.",
    "Partial — and the most recoverable partial in this library, because the remaining work is arithmetic rather than advocacy: sixty days, a costed plan, a named backup, a countersignature. Alina is thriving at the school she kept; her file now says why, in full; and the court has dated the question's return. Finish the box. The scenario's lesson is not that merits don't matter — they carried everything else. It is that in school-stability cases, merits decide *whether*, and transportation decides *whether it happens*."]),

 E("end_fair_transfer", 38, "Ending — A Fair Meeting, a New School (partial)",
   ["The review confirms the reconvened determination, and Jefferson Middle School stands as Alina's school. The court's language matters, and Ms. Anselmi makes sure you hear it: the September 18 determination — parent present, teacher heard, factors weighed, the child's own paragraph in the record — is commended as the process the first one should have been; its conclusion, on proximity and transition burden, is one this record permits. Alina's placement review at Jefferson is ordered expedited on the strength of the assessment file you chased down by name, and the advanced-track question is set for November with her June data in the packet. You lost the school. You won the record — and the record is already spending itself on her behalf.",
    "Hold this ending to the scenario's own standard, because it is the ending this doctrine most needs to say out loud: a proper process does not guarantee your outcome. The federal assurance is that a child remains in her school of origin *unless a determination, based on all factors, decides otherwise* (20 U.S.C. § 6311(g)(1)(E)(i)) — and a determination that genuinely weighs the advanced track, the counselor, the paragraph, and the nineteen miles can still land on transfer. What the rebuilt process bought, even in loss: immediate enrollment with records pursued (20 U.S.C. § 6311(g)(1)(E)(ii), (iii)), a transfer with stated reasons that can be revisited when facts change, and a father permanently inside the notification loop — no more dead addresses; the file was corrected in open court.",
    "What no strategy controls lives here most plainly: the weighing itself, done by other people, on factors the law lists but does not rank. September 1 was winnable because it was unfinished. September 18 was losable because it was finished honestly. Both things are true, and a training library that hides the second teaches a lie about the first. Alina's case continues — her placement review, her track, her father's progress — on the fullest record any version of this autumn produced."]),

 E("end_default", 14, "Ending — Enrolled on a Tuesday",
   ["There was no hearing about the school — no room, no moment, no loss anyone can appeal, because nothing was ever formally decided in a way the system had to defend. A six-minute phone call about bus paperwork became a determination; a determination became an enrollment; an enrollment became a girl in the standard track of a school she describes as *fine*, waiting until November for an assessment her old school completed in June. Her father's objection exists in the file in its entirety: *father expressed disagreement*. Four words, spelled correctly.",
    "The debrief is the statute, read against the file. The assurance is real: school of origin unless a determination based on all factors — the appropriateness of the current setting, proximity, the whole list — decides otherwise. (20 U.S.C. § 6311(g)(1)(E)(i)) The machinery is real: points of contact, written transportation procedures, funded rides. (20 U.S.C. § 6312(c)(5)) And none of it is self-executing. Every piece of it waits for a dated, written objection — the kind that creates a problem an institution must answer with a name attached — and for a record request (55 Pa. Code § 3130.44(d)) that drags the four-page form into the light. The father in this ending had every fact the winning father had. He had them in conversations. Conversations are where this system stores things it intends to lose.",
    "It is not sealed — determinations can be revisited, transfers appealed through the districts' own processes, records corrected at any review; Alina's November assessment may yet restore her track, months late and grades lighter. But September cannot be re-run, and September was when the asking was cheap. In the first ninety days of a case, the defaults load themselves into envelopes and letterhead. The only counterweight ever documented is paper, sent early, with the address right."]),
]
emit(121, s121_meta, s121, S, "a child in kinship care, a school best-interest determination held without the parent, and a transportation fight. No graphic content.")

# ============================================================ S122 (Complex)
S = date(2027, 2, 8)
assert fmt(S) == "Monday, February 8, 2027"
assert fmt(S + timedelta(days=38)) == "Thursday, March 18, 2027"   # adjudication
assert fmt(S + timedelta(days=45)) == "Thursday, March 25, 2027"   # disposition

s122_meta = {
    "title": "The First 90 Days",
    "subtitle": "Scenario 122 — Excused, Absent, Unexcused (a fictional composite)",
    "startDateISO": "2027-02-08",
    "startNode": "start",
    "startCash": 140,
    "tier": "Complex",
    "summary": "You are Bernadette Farrow. The dependency petition says your son Oren, ten, missed 23 days of school unexcused — educational neglect, in the agency's words. You count nine. Between your number and theirs stands a school office, a software migration, and a box of un-scanned excuse notes.",
}

s122 = [
 N("start", 0, "Twenty-three",
   ["The petition is served at the laundromat where you work, which is how you come to read the worst paragraph of your life with a customer's towels rotating behind you. Paragraph four: *During the fall term, the child accumulated twenty-three (23) unexcused absences from school, evidencing a pattern of educational neglect.* Twenty-three. The number is typeset with the confidence of a thing that has been printed before, in other files, about other mothers.",
    "Oren has asthma — real asthma, clinic asthma, a nebulizer shaped like a dragon that he has named. You count the fall on your fingers twice before your shift ends: sick days and clinic days, yes; days you kept him home on a whim, no. You count nine that were nobody's fault but the illness and two bad mornings. You cannot get to twenty-three without counting days you drove him to the clinic with a note in his backpack."],
   [C("Read the whole petition at the kitchen table tonight — every paragraph, not just the loud one.", "petition_read")]),

 N("petition_read", 0, "Paragraph nine",
   ["The rest of the petition is thinner than paragraph four's confidence suggests. There is the fall attendance. There is a paragraph about a missed well-child visit in the spring, already cured. And there is paragraph nine, written smaller, the way true things sometimes are in petitions: *In November, the child missed two scheduled asthma follow-up appointments; the mother reports transportation failure.*",
    "Paragraph nine is true. The car died on a Tuesday; the second appointment died with it, and though you called the clinic both times — you remember the hold music — the petition's version ends at *missed*. Your case, read whole, is one inflated number and one honest paragraph. They will require opposite handling, and confusing the two is how parents lose both."],
   [C("Count again, slowly, from the wall calendar — the one with the clinic stickers.", "lucinda_count")]),

 N("lucinda_count", 0, "Nine, maybe ten",
   ["The wall calendar is the family's true archive: clinic stickers on appointment days, your shift marks, the dragon drawings Oren adds to any square he considers under-decorated. Counting from it: fourteen days that were clinic or illness-with-a-note — notes you wrote, signed, and put in the backpack yourself. Nine unexcused, by your own honest count, including two in September when the bus route changed and you mismanaged a week you have never pretended was well managed.",
    "Fourteen plus nine is twenty-three. The petition's number is not invented — it is *converted*. Somewhere between the school office and the agency's word processor, excused stopped being a category your son was allowed."],
   [C("Call the lawyer the court appoints — Mr. Keller — before you call anyone else. Numbers this wrong need a strategy, not a phone manner.", "lawyer122")]),

 N("lawyer122", 1, "Two rooms",
   ["Mr. Keller teaches the case as architecture: two rooms, different rules. Room one is adjudication — did the agency prove its allegations? — and the burden there is the agency's, at the law's highest civil setting: a child may be found dependent only from clear and convincing evidence. (42 Pa.C.S. § 6341(c)) What is not proven is dismissed, and the child discharged on that allegation. (§ 6341(a))",
    "Room two is disposition — what happens next — where the rules relax: written reports and all evidence helpful to the determination may be received there, and the people who made the reports may be examined and cross-examined about them. (§ 6341(d)(1), (2)) \"The school's summary page,\" Keller says, \"is a room-two document dressed for room one. Our whole case is documents: the school's *detail* — not its summary — the clinic's records, and your calendar. We get them in writing, we get them early, and we make the agency's exhibit testify against itself.\""],
   [C("Start where the number was manufactured: the school office, and the file behind the summary.", "truancy_letter")]),

 N("truancy_letter", 2, "The October letter",
   ["In the drawer where school papers go, under the lunch menus, is the letter the number arrived in first: an automated truancy warning from October, generated when Oren's absences crossed a threshold — it cites the count, offers a meeting, and bears no human signature at all. You remember reading it with the specific dread of a parent who cannot tell whether she is in trouble. You filed it. You did not answer it, because it did not read as answerable; it read as weather.",
    "Keller, shown the letter later, will say the sentence that organizes this case: \"Weather is what unexamined systems call their own output. We're going to examine it.\""],
   [C("Take the letter, the calendar, and a written request to the school office.", "school_office")]),

 N("school_office", 3, "The summary and the screen",
   ["The school office produces, first, exactly what the agency has: the one-page summary — *23 unexcused*. It is only when you ask, in the words Keller gave you, for the *complete attendance detail with excuse coding and the note log* that the visit changes register. Ms. Baranski, the attendance clerk, turns her monitor — an act of minor institutional courage — and the detail tells a longer story: absence rows with code histories, and against fourteen of them a small flag from an older system: *note rcvd*.",
    "\"We migrated attendance software in October,\" she says, quietly. \"The notes stopped being scanned in September — staffing. The flags came across. The *meanings*—\" she touches the flag with one fingertip, \"—didn't, in every column. I have raised this. It is being reviewed at the district level, which is a speed, I grant you, but not a fast one.\""],
   [C("Ask for the detail in writing: the full printout, the code history, the note log — a formal request, dated, with a copy for your lawyer.", "oren_voice", setFlags=["schoolFile"], addHidden=["School records — attendance detail with code history requested in writing"]),
    C("Ask her to just tell you which days were excused, and write them down yourself at the counter.", "summary_only")]),

 N("summary_only", 4, "Counter notes",
   ["Ms. Baranski is willing, and the counter conversation is genuinely informative — and completely unusable. Your handwritten list of her verbal account has no stamp, no signature, no system's authority; it is a mother's notes about a clerk's memory, and it will be weighed exactly that way. She watches you write and arrives, visibly, at the same conclusion.",
    "\"Do the written request,\" she says. \"I'll print it myself. Paper from me counts. Paper about me doesn't.\""],
   [C("Do the written request. Full detail, code history, note log, for counsel.", "oren_voice", setFlags=["schoolFile"], addHidden=["School records — attendance detail requested in writing after verbal account proved unusable"])]),

 N("oren_voice", 5, "The dragon",
   ["Oren's evidence is offered at the kitchen table, unprompted, while demonstrating the nebulizer: \"The dragon days aren't school days. You can't do math when the dragon is loud. The nurse lady knows — she has my plan in her drawer.\" The school nurse holds his asthma action plan. The school, in one of its drawers, has always known exactly why those fourteen days happened; the knowledge simply lived in a different column than the counting.",
    "You write his sentence down in the notebook — not because a ten-year-old's testimony decides adjudications, but because the file will otherwise contain no trace of the person the numbers describe."],
   [C("Take the detail printout to Keller, and then go where the other half of the truth lives: the clinic.", "clerk_honesty")]),

 N("clerk_honesty", 6, "Printed and initialed",
   ["Ms. Baranski prints the detail — eleven pages — and does the thing that separates a witness from a bystander: she initials every page and dates the set. The code history is now legible to a lay reader: fourteen rows where a received note was mapped, by the migration, into *unexcused*; the original flag preserved in a legacy column, like a word in a dead language that the new system prints but no longer speaks.",
    "She cannot correct the codes herself — that authority sits with the principal, on review. \"But this—\" the initialed pages go into your folder, \"—is what a correction would be correcting *to*. There's a difference between a parent saying the record is wrong and a parent carrying the record that proves it. You are now carrying it.\""],
   [C("Next: the clinic's half of the torn page.", "dube_visit")]),

 N("dube_visit", 7, "The caseworker at the wall",
   ["Ms. Fontana's home visit is routine in every way but one: she stands in front of the wall calendar for a long moment — clinic stickers, shift marks, dragons — and asks, with the neutrality of a woman photographing something with her eyes, whether the calendar covers the fall term. It does. She notes the visit in her tablet in the usual phrases. Whether the calendar enters the agency's thinking is a question her face declines to answer.",
    "The petition, you reflect after she leaves, was assembled from a summary page and a phone call. Your kitchen wall knows more about Oren's fall than his case file does. The project of the next month is to move the wall's knowledge into the file — in forms a court can weigh."],
   [C("The clinic, then — Dr. Mbeki's office, where fourteen of the twenty-three days are appointments with timestamps.", "clinic_visit")]),

 N("clinic_visit", 8, "Dr. Mbeki's front desk",
   ["The clinic's front desk runs on its own paper religion, and it is a stricter one than the school's: appointment histories print with timestamps, cancellations carry reason codes, and the desk clerk finds, without being asked twice, the two November entries — both marked *mother called same day; car trouble; rescheduled by clinic*. The petition's paragraph nine, in the clinic's hand, has a second half.",
    "Fourteen fall visits match the absence detail, date for date, like two halves of a torn page. What remains is to make the clinic's half into evidence — which means asking for it the way evidence is asked for."],
   [C("Sign the release and request the complete appointment history in writing, stamped by the clinic.", "neighbor_note", setFlags=["clinicRecords"], addHidden=["Medical records — clinic appointment history requested in writing, matching school absence dates"]),
    C("Take the desk clerk's verbal rundown — she has told you the dates; surely Keller can use your notes.", "neighbor_note")]),

 N("neighbor_note", 9, "The rides",
   ["Twice in the fall, when the car was dead in its earlier, warning stages, your neighbor drove you and Oren to the clinic. She writes it down without being asked twice — dates, the dragon in his lap, the stickers — and signs it. It is a small exhibit. It corroborates the calendar, which corroborates the clinic, which corroborates the school's own flags. Cases like this are not won by a document. They are won by documents that agree with each other in front of a judge.",
    "Keller, receiving the growing folder, has begun using a word lawyers ration: *coherent*. \"The agency's story is one page. Ours is a system. Systems beat pages, given a judge who reads.\""],
   [C("Now the agency's own file — request it, and read what the petition was built from.", "clinic_records")]),

 N("clinic_records", 10, "Stamped",
   ["The clinic's printout arrives stamped and complete: fourteen fall appointments with timestamps; the November pair with their same-day-call annotations; the well-child visit, rescheduled and kept. It is the single most boring document in the case and, Keller says, holding it the way jewelers hold stones, quite possibly the most valuable.",
    "\"Petitions are written from summaries. Hearings are decided by alignments. Your son's fall, aligned: the school's flags, the clinic's stamps, a neighbor's rides, a mother's calendar — four independent records, one story. The agency has a number. Numbers without provenance are just typography.\""],
   [C("Request the agency record — the file the petition came out of — in writing.", "records122")]),

 N("records122", 12, "What the petition was built from",
   ["The agency's record is releasable on request (55 Pa. Code § 3130.44(d)), and what it holds is the anatomy of paragraph four: the school's summary page, the October truancy printout, and — three pages deeper — a caseworker note from November that you read standing up: *Mother states absences were medical/clinic-related; school to verify coding.* The verification has no follow-up entry. The petition was drafted in January from the summary, by a process that never walked back to its own November doubt.",
    "Keller tabs the note with the gentleness of a man handling the other side's gift. \"We don't have to call anyone careless,\" he says. \"The file calls itself unfinished. We just ask the court to finish it.\""],
   [C("File the request's copy, the tabbed note, and the clinic printout at the front of the hearing packet.", "oren_school_day", setFlags=["recordsRequested"], cash=-12, addHidden=["Record — agency record requested; file shows verification of absence coding was noted as pending and never completed"]),
    C("The packet is heavy enough. Save the postage and the point.", "oren_school_day")]),

 N("oren_school_day", 13, "The nurse's drawer",
   ["One more internal contradiction surfaces, through Oren's teacher, who mentions it as the most ordinary thing in the world: the school nurse's asthma action plan — signed by Dr. Mbeki's office in September, filed at school, known to everyone who supervises Oren's breathing. The institution that generated *23 unexcused* also held, the whole time, a clinical document explaining the absences' likeliest cause. Institutions are not minds. They do not know what their drawers know — until a hearing introduces the drawers to each other.",
    "Keller adds the action plan to the alignment: a fifth record, the school's own, agreeing with the other four."],
   [C("Read the agency note once more. Then decide what to do about paragraph nine — the true one.", "agency_note")]),

 N("agency_note", 14, "To verify",
   ["*To verify.* The two words sit in the file like an unmailed letter. Everything in this case — the petition, the number, the dread at the laundromat — descends from a verification that was assigned, in writing, by the agency to itself, and never performed. Keller is careful here, and the care is the lesson: \"We do not say they lied. We say the work is unfinished, the allegation is unproven until it is proven, and the burden never moved. (42 Pa.C.S. § 6341(c)) Unfinished work is not evidence. It is a to-do list with a caption.\"",
    "Your own November — the dead car, the two missed follow-ups, the calls you made — remains in the case, uncorrected by any of this. Strategy for a true paragraph is different from strategy for a false one: you do not rebut it. You own it, with its second half attached, and you fix its cause in writing."],
   [C("Build your side of paragraph nine: the calendar, the clinic's annotations, and a transport plan that survives a dead car.", "mother_calendar")]),

 N("mother_calendar", 16, "The wall, copied",
   ["The wall calendar comes down for copying with the ceremony of a flag being retired: photographed whole, then page by page, the clinic stickers and shift marks and dragons intact. Annotated, in your hand, only where annotation is undeniable — the bus-route change week in September, which you mark *my fault, fixed* without being asked, because a calendar that admits one bad week is believed about the other twenty.",
    "Keller adds it to the packet as what it is: a contemporaneous record, made before anyone knew there would be a case, which is the only kind of credibility money cannot buy and advocacy cannot fake."],
   [C("Send the annotated copy to counsel — and then face the meeting the agency has called.", "agency_conference", setFlags=["motherNotes"]),
    C("Keep the calendar at home. Some things are the family's, and the file has enough.", "agency_conference")]),

 N("agency_conference", 17, "The offer",
   ["The pre-hearing conference has coffee, a long table, and an offer — the system's standard instrument for making files like this one go away efficiently. Stipulate: agree that Oren is dependent on the attendance allegation, accept services and supervision, and the agency will recommend he remain at home. No hearing, no cross-examination, no correction of the school's record. The number 23 would stand in the adjudication as an admitted fact — with your signature under its neighborhood.",
    "It is not a villainous offer. It is a *priced* one, and the price is the truth of the fall term, permanently. Keller lets the silence after it run a full five seconds before he looks at you. The decision is yours in a way few decisions in this system are."],
   [C("Decline the stipulation. The attendance allegation is false in its operative number, and falsehoods admitted in March are quoted in September.", "correction_ask"),
    C("Accept the stipulation. Oren stays home, services begin, and the fight ends today — the number be damned.", "stipulated", setFlags=["stipulatedFlag"])]),

 N("stipulated", 18, "The bargain",
   ["The stipulation is signed in the conference room, in triplicate, with the coffee going cold. Dependency is admitted on the attendance allegation as written — twenty-three unexcused absences, a pattern of educational neglect, your name beside the words. Disposition is set for March 25, where the agency has signaled it will recommend what it promised: Oren home, under supervision, with services.",
    "Keller walks you out with the folder suddenly light. \"You bought certainty,\" he says. \"It is a real currency, and parents spend it for real reasons. I only note what was in the price, because the price is permanent: the school's record was never corrected, the clinic's alignment was never heard, and the number is now a fact you agreed to. It will be quoted back — in reviews, in reports — as an admission, not an error.\""],
   [C("Go to disposition with the bargain kept and the file unbuilt.", "disposition_day")]),

 N("correction_ask", 19, "The principal",
   ["The written request to Principal Truman is three pages: the initialed detail printout, the code history, the clinic alignment, and one ask — review the migrated coding for Oren's fall record, correct it if the review bears the detail out, and answer in writing. It is addressed to the only person in the school building who can make a correction outlive a conversation.",
    "What it is not is a demand. Keller's drafting principle: *write the letter the recipient can say yes to without confessing to anything.* The migration was the district's; the correction can be the principal's pride instead of his apology."],
   [C("Attach the initialed detail — the correction needs its target printed and initialed, not described.", "keller_second", requiresFlags=["schoolFile"]),
    C("Write from the clinic alignment alone, without the school's own detail printout to anchor it.", "no_audit")]),

 N("no_audit", 24, "Reviewed as presented",
   ["The principal's reply is prompt, courteous, and final in the way of decisions made on incomplete paper: the attendance record 'as it stands in the system of record' reflects the codes the system carries; individual coding histories are a district-level matter; the school 'cannot undertake case-by-case recoding on parental submission alone.' Your clinic printout is acknowledged as 'helpful context for the future.'",
    "The future is not where adjudications happen. Without the school's own detail — its flags, its legacy column, its clerk's initials — the correction had no skeleton to grow on, and an uncorrected official record walks into March as the fact of the case."],
   [C("Build the hearing packet around what exists: the clinic's alignment, the calendar, the agency's own unfinished note.", "hearing_prep122")]),

 N("keller_second", 21, "Owning paragraph nine",
   ["Keller's second session is about the paragraph you cannot rebut. \"We win paragraph four with documents,\" he says. \"We survive paragraph nine with candor and a repair. The calls are in the clinic's own annotations — good. The cause was a dead car — fixable, and we fix it visibly: the clinic runs a transport van for established patients; you enroll, in writing, this week. A judge reading a true allegation next to its documented repair reads a different mother than the petition describes.\"",
    "He writes the disposition theory on the pad: if — if — dependency is found on the narrow ground, the disposition the law offers includes the child remaining with the parent, subject to supervision and conditions the court prescribes. (42 Pa.C.S. § 6351(a)(1)) Home, with a case, is the honest best this petition can produce — and it is produced by winning the big paragraph and owning the small one."],
   [C("Enroll in the clinic transport program and keep the confirmation — in writing, in the folder.", "audit_wait", setFlags=["narrowPlan"], cash=-6)]),

 N("audit_wait", 24, "The audit",
   ["Truman's office confirms the review is underway — an audit of the migrated codes for Oren's record, with the district's data office involved. It will take weeks. Adjudication is March 18. The agency files its exhibit list in the meantime, and it is exactly one page long: the fall attendance summary, offered as a school record, plus the petition's other paragraphs trailing behind it like a tail.",
    "Keller studies the list with open contentment. \"They are bringing a summary to a documents fight. A summary is a conclusion wearing a table's clothes — and conclusions, at adjudication, are the one thing the burden of proof exists to cross-examine.\""],
   [C("While the audit runs, follow the migration's trail — other families, other files, one district memo.", "foster_shadow")]),

 N("foster_shadow", 26, "What placement would mean",
   ["The stakes, stated once and plainly, because strategy without stakes is bookkeeping: if the attendance allegation is proven as written, disposition could remove Oren — to a foster home, a new school, a nurse who does not have his plan in her drawer, a nebulizer routine in strangers' hands. The asthma that generated the absences would then be managed by the system that miscounted it. Everyone in the case knows this arithmetic. It is why the number matters, and why a stipulation priced at 'home' tempts, and why the correction — not sympathy, the correction — is the whole ballgame.",
    "You attend the next clinic visit by the new transport van, and the driver signs your trip slip, and the slip goes in the folder. Systems, again. Fossils of reliability, accumulating."],
   [C("The migration memo surfaces. Read it the way Keller reads everything: for what it admits.", "school_board")]),

 N("school_board", 28, "Known issue",
   ["The district's data office memo — obtained as an addendum to the school's production — is two paragraphs of bureaucratic prose with a live coal in the second: the October migration's handling of legacy absence flags was a *known issue* affecting 'a subset of records,' identified in November, with recoding 'to be completed as resources permit.' November: the same month the agency's file noted *to verify* and moved on. The district knew its counts were suspect while the agency was drafting a petition from one of them.",
    "No one conspires in this story. That is the story. Two institutions' unfinished work, multiplied by each other, became a mother's alleged neglect — and the only actor in the entire chain who finished her paperwork was the mother."],
   [C("Keller's evidence session: how the two rooms receive all of this.", "keller_evidence")]),

 N("keller_evidence", 29, "Two rooms, again",
   ["Keller marks the exhibits and rehearses the law's division of labor until you can recite it. Adjudication: the agency's burden, clear and convincing (42 Pa.C.S. § 6341(c)) — the summary must be *proven*, and its provenance is its weakness: a migrated count, from unverified coding, contradicted by the district's own detail and its own memo. What fails that standard is dismissed. (§ 6341(a))",
    "Disposition is the second room, and only if we reach it: there, written reports may be received freely — *and* examined and controverted, their makers cross-examined. (§ 6341(d)(1), (2)) \"In room one, we attack the number's birth certificate. In room two, we present the repair. Never confuse the rooms — parents do, lawyers do, and petitions count on it.\""],
   [C("The audit's answer is due. Everything now depends on whether it lands before March 18.", "correction_letter")]),

 N("correction_letter", 31, "The correction",
   ["Principal Truman's letter arrives on school letterhead, and it is the document this scenario exists to produce. The audit is complete. Oren's fall record is corrected in the system of record: **nine unexcused absences; fourteen excused — medical, with notes received**; the migration's mapping error is stated plainly, with the district memo cited; the corrected summary is attached, and the letter closes with the institutional sentence that matters most, because it can be quoted: *The previously issued summary should not be relied upon.*",
    "Keller reads it twice and puts it, without ceremony, at the front of the packet — ahead of the petition's own first page. \"Adjudication is a reading,\" he says. \"We have just changed what gets read first.\""],
   [C("Final preparation: the cross of the summary's maker, and the narrow paragraph's repair, in that order.", "expert_call", setFlags=["codingLetter"], addHidden=["School records — attendance record corrected in writing by the school: 9 unexcused, 14 excused-medical"])]),

 N("expert_call", 33, "Who made this page",
   ["The cross-examination rehearses itself in Keller's office in four questions, addressed to whoever the agency produces to sponsor its summary: Who generated this page? From what system? With what verification of the coding? Are you aware the issuing institution has withdrawn it? The questions are short because the record is long — the alignment does the arguing: school flags, clinic stamps, a neighbor's rides, a mother's calendar, a district's confession, an agency note that says *to verify*.",
    "\"At disposition, if we get there, reports can be examined and their makers questioned — that is the statute's own design (§ 6341(d)(2)),\" Keller says. \"At adjudication we need less: only the burden, doing its ordinary work on an extraordinary number.\""],
   [C("One last piece of disposition paper: the clinic van's confirmation, printed.", "clinic_van")]),

 N("clinic_van", 34, "The van, confirmed",
   ["The transport program's confirmation letter lists Oren as an established rider: pickup protocol, the clinic's address, your phone number, the backup arrangement for van failures. Paragraph nine's cause — a dead car — now has a documented, redundant system standing where a single point of failure stood in November.",
    "It is a one-page letter about a van. At disposition, it will be the difference between a mother who missed appointments and a mother who missed appointments, diagnosed why, and rebuilt the road. Courts do not grade intentions. They read repairs."],
   [C("Assemble the final packet: petition, detail, correction, alignment, repair — in that order.", "hearing_prep122")]),

 N("hearing_prep122", 36, "In that order",
   ["The packet's order is the argument: the petition's claim; the school's own detail, initialed; the district's *known issue* memo; the corrected summary — *should not be relied upon*; the clinic's alignment; the agency's unfinished note; the calendar; the van. Keller has written the adjudication ask in one sentence: the attendance allegation, as pleaded, is not proven by clear and convincing evidence, because the only institution that ever counted it has withdrawn the count. (42 Pa.C.S. § 6341(c), (a))",
    "Tomorrow the agency presents its case first. Its first exhibit is a page its own source has retracted. There are worse positions to defend a family from — Keller has had most of them, he says, and this is not one."],
   [C("Sleep in the specific way of people who have done the work. Court in the morning.", "night_before122")]),

 N("night_before122", 37, "Dragons, counted",
   ["Oren, told only that tomorrow is a court day about school, contributes his final exhibit voluntarily: a drawing of the dragon nebulizer, labeled in his careful capitals, with a speech bubble: *I WAS AT THE CLINIC.* It goes on the fridge, not in the packet — some evidence is for the family's record, and the family's record, after this winter, is in excellent order.",
    "You check the packet once. The wall calendar's space is already re-marked for spring: clinic stickers, shift marks, and — new this month — van pickups, in a different color. The archive continues. It was never the problem. It was always the proof."],
   [C("Go to court.", "adjudication")]),

 N("adjudication", 38, "Thursday, March 18",
   ["Adjudication proceeds as Keller built it. The agency presents: the petition, the summary's sponsor — a supervisor who generated the page from the system of record and concedes, in the cross's fourth question, that she has seen the correction letter and cannot speak for the withdrawn count. The alignment enters without drama: flags, stamps, memo, calendar. The courtroom's temperature is set, as predicted, not by advocacy but by provenance.",
    "The attendance allegation will be decided on whether a retracted number can carry a clear-and-convincing burden. Paragraph nine waits behind it, true and repaired. The court takes the matter under advisement and moves the case to disposition on March 25 — where everything the adjudication decided, and everything it didn't, becomes a plan for a boy's actual life."],
   [C("To disposition, on whatever the record has become.", "disposition_day")]),

 N("disposition_day", 45, "Thursday, March 25",
   ["Disposition is the second room, with its wider door: reports and evidence helpful to the determination may be received here, and their makers examined. (42 Pa.C.S. § 6341(d)(1), (2)) What the court orders for Oren — home or placement, supervision or none — will be built from the whole winter's record: the number's fate at adjudication, the narrow paragraph and its repair, and the correction's timing, which in this case was everything.",
    "The judge has read the packet. The judge has also, it turns out, read the file."],
   [C("The record holds a retracted count, an institutional correction in writing, a four-way alignment of independent records, and a true paragraph owned and repaired.", "end_narrow", requiresFlags=["schoolFile", "codingLetter"]),
    C("The record holds the clinic's alignment and the mother's calendar — but the school's record was never corrected, and the correction letter that would have settled it arrived after adjudication had already taken the official count as proven.", "end_corrected_late", requiresFlags=["clinicRecords"], requiresNoFlags=["codingLetter"]),
    C("The record holds an admitted allegation, signed for in a conference room — no hearing, no correction, no alignment ever heard.", "end_stipulated", requiresFlags=["stipulatedFlag"]),
    C("The record holds a summary, a sponsorship, and a mother's say-so — against a burden that was never hers to carry and a number nobody made the system defend.", "end_placed")]),

 E("end_narrow", 45, "Ending — Home, on the Narrow Ground",
   ["The attendance allegation is dismissed — not mitigated, not discounted: not proven. The court's adjudication findings say it in the burden's own grammar: on the attendance count, the evidence — a summary withdrawn by its issuing institution, contradicted by the institution's own detail, its own memo, and an alignment of clinic records — does not constitute clear and convincing evidence of educational neglect. (42 Pa.C.S. § 6341(c)) The allegation fails, and with it the petition's centerpiece. (§ 6341(a)) What remains is paragraph nine, the true one: two missed follow-ups, proven, and answered at disposition with their cause repaired in writing. The disposition is the statute's first option: Oren remains with you, subject to supervision and to conditions — the clinic van enrollment among them, recited in the order. (42 Pa.C.S. § 6351(a)(1))",
    "Name the win precisely, because its shape is the lesson. The number was defeated by provenance, not passion: a written request for the school's *detail* rather than its summary; a clerk's initialed printout; a principal's corrected letter — *should not be relied upon* — obtained by asking the one person who could issue it, in a letter he could say yes to; clinic records aligned date-for-date; the agency's own record (55 Pa. Code § 3130.44(d)) supplying the *to verify* that was never verified. And paragraph nine was not rebutted but owned, because a parent who concedes the true paragraph with a documented repair is believed about the false one. Both halves were strategy. Neither half works alone.",
    "What no strategy controls: a judge less patient with provenance; a clerk less brave than Ms. Baranski; a district that corrects slower. The case is not closed — supervision runs, reviews recur, and Oren's asthma does not consult the court calendar. But the file that follows this family now says what actually happened in the fall: nine, and fourteen-with-notes, and a mother who caught the error the institutions filed past each other. Permanently. In the record. Where it will be quoted from, correctly, from now on."]),

 E("end_corrected_late", 45, "Ending — Corrected, One Hearing Late (partial)",
   ["The correction letter reached the file on March 24 — six days after adjudication took the official record as it stood. It changed disposition profoundly and adjudication not at all. The court's disposition is merciful and specific: Oren remains home under supervision (42 Pa.C.S. § 6351(a)(1)), the corrected summary is attached to the order, and the agency is directed to conform its records. But the adjudication itself — dependency founded on the attendance allegation as pleaded, twenty-three unexcused — stands in the case's history as a found fact, correctable on paper everywhere except the one page that decided it.",
    "The autopsy is one of sequence, not effort. The clinic alignment was built. The calendar was kept. What never existed was the school's own *detail* — the initialed printout with the legacy flags — because the request for it was never made in writing, and without the detail, the principal's review had nothing to correct *to*, and answered, reasonably, from the system of record as it stood. Every institution in this story behaved the way institutions behave with the paper in front of them. The paper in front of them was the variable. It usually is.",
    "Partial, and far from empty: Oren is home, supervised, his school record corrected at the source, the agency directed to conform — a foundation most families would take. What was lost is narrower and worth naming in a training library: the difference between a record corrected before adjudication and after it is the difference between an allegation *dismissed as unproven* (§ 6341(a)) and an allegation *found, then forgiven*. Files remember which. So do future petitions. The detail request is a five-minute letter. File it in the first week, not the last."]),

 E("end_stipulated", 45, "Ending — The Bargain",
   ["Disposition keeps its promise: Oren remains at home, under supervision and services, exactly as the conference-room offer described. No removal, no foster home, no stranger holding the nebulizer. On the outcomes that keep a family intact, this ending delivers — and the debrief will not pretend otherwise, because parents who take this bargain are not fools, and a library that calls them fools teaches nothing.",
    "The price is itemized in the file, where prices in this system live. The adjudication rests on an *admission*: twenty-three unexcused absences, educational neglect, agreed and signed. The school never corrected its record under the pressure of a hearing; the clinic's alignment was never heard; the agency's *to verify* was never read aloud. Every future reader of this file — the next caseworker, the next report writer, the next judge — will meet the number first, armored now in the one thing that makes numbers immortal: the mother's own agreement. Reviews will quote it. Summaries will copy it. It will be, forever, what the fall of 2026 *was*.",
    "What no strategy controls is also honestly part of this ending: hearings are gambles, judges vary, and the certainty bought here — a son home tonight, services started, no removal risk this spring — is real value purchased with a real record. The scenario's doctrine is only about seeing the price tag before signing: a stipulation is not the end of a fight but a *settlement of the facts*, and in a system that runs on files, facts are the one currency that never devalues and never expires. The correction remains available — school records can still be pursued, reviews still argued. But it will now be argued uphill, against an admission, by the person who signed it."]),

 E("end_placed", 45, "Ending — Twenty-Three, Standing",
   ["The number stands. Adjudication found the attendance allegation proven on the strength of the only document anyone sponsored — the summary — the mother's contrary account being, in the court's unavoidable phrase, *uncorroborated by records*. Disposition continued the logic: placement with a foster family, services for the mother, reviews to come. Oren packs the dragon in a bag that a stranger's household will learn to plug in. The correction of his school record — if it ever comes — will arrive as an erratum to a case that has already been decided by its error.",
    "This is the ending the burden of proof exists to prevent, and its mechanics deserve the cold light. The burden never moved: dependency required clear and convincing evidence (42 Pa.C.S. § 6341(c)), and a migrated count from unverified coding is not that — *when someone makes the court look at it*. Nobody did. The detail was never requested in writing; the clinic's alignment was never assembled; the agency's record — with its own *to verify*, releasable on request (55 Pa. Code § 3130.44(d)) — was never requested at all. Against a sponsored summary, the defense offered the truth, unexhibited. Truth is the beginning of a case. It is not, in a paper system, the case.",
    "It is not the end of the story — reviews recur on the statute's clock, corrections can still be pursued and filed, and Oren's mother retains every tool this scenario inventoried, now at the higher prices appeals and reviews charge. But the doctrine has rarely had a cleaner demonstration: institutions generate numbers; numbers generate petitions; and the only force ever documented to reverse the sequence is a parent, early, in writing, asking the system for its own detail — and carrying the answer into the room where burdens live."]),
]
emit(122, s122_meta, s122, S, "a dependency adjudication built on school attendance records. No graphic content.")
print("done")
