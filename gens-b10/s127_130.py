# -*- coding: utf-8 -*-
from lib import C, N

# ---------------- S127 — Foundation capstone ----------------
S127 = dict(
 num=127, name="The Whole Table, Gently", tier="Foundation",
 startDateISO="2026-03-02", startCash=160,
 summary="A capstone in scope, gentle in mechanics: one incident makes two files — an indicated report with a 90-day appeal clock, and a kinship placement with your sister — and the win is learning to work both files in the right order.",
 contentNote="This scenario depicts a child-welfare investigation, a temporary kinship placement, and an indicated-report appeal. There is no graphic content. Players may skip any scene or use the quick exit at any time.",
 offsetNote=" (the children's placement date)",
 win_id="end_home",
 nodes=[
  N("start",0,"Two Envelopes",[
    "Your name is Nadia. You clean rooms at a motel off the highway, and you are raising Zayd, seven, and Noor, four, in a one-bedroom above a laundromat. In February the building's boiler failed twice, and on the coldest night you did what the neighbor downstairs suggested: you all slept at her place, three floors of stairs between your children and any exit the fire code would recognize.",
    "Nobody was hurt. But a report was made, and this morning there are two envelopes. The first says Zayd and Noor will stay with your sister Rania while the agency looks at your housing. The second says a report about that night has been marked indicated — and that word, a caseworker explains, can follow you onto every childcare clearance you will ever need, including the motel's sister property where you were about to pick up weekend shifts in the playroom.",
    "Two files. Two clocks. This story is about working both of them, in the right order, on paper."],
    [C("Sit down with the flyer your sister printed and read both letters all the way through","read_both",note="The second letter is the one with a deadline in it. Most people read it last."),
     C("Call the caseworker and ask her to just explain it quickly","read_both",note="She explains the visit schedule. The deadline in the second letter stays unread a little longer.")]),
  N("read_both",2,"The Deadline in the Second Letter",[
    "The second letter holds the number that matters: a person named as a perpetrator in an indicated report may appeal and ask for the report to be amended or expunged — in writing — within 90 days of being notified (23 Pa.C.S. § 6341(a)(2)). You were notified on Monday, March 2, 2026. Ninety days later is Sunday, May 31, 2026.",
    "The first letter holds no deadline at all, which is its own kind of trap: Rania's home study, your repair plan with the landlord, and the review hearing will all move at the speed of whoever writes things down."],
    [C("Write both dates on the kitchen calendar and circle May 31","calendar",flags=["calendarSet"],hidden="Appeal deadline calendared from the notice date",note="Two clocks, one calendar, both visible from the refrigerator."),
     C("Keep the dates in your head — you have a good memory","calendar",note="Memory is a fine thing. It is not a filing system.")]),
  N("calendar",5,"Rania's Kitchen",[
    "Rania has a spare room, a fold-out couch, and a caseworker of her own now — the kinship worker, who needs clearances, a home visit, and a form signed by everyone over eighteen in the house. Zayd has already claimed the top bunk of a bed that does not exist yet.",
    "The kinship worker says the study usually takes a few weeks. She does not say what happens to the paperwork if nobody asks about it. Rania looks at you over the children's heads: ask, she mouths."],
    [C("Ask what the study needs, write the list down, and text it to yourself before you leave","study_list",cash=-5,flags=["studyList"],hidden="Kinship study requirements obtained in writing",note="A list you can check off beats a timeline you were told."),
     C("Trust the process — she said a few weeks","study_list",note="Weeks pass at different speeds depending on whether anyone is counting.")]),
  N("study_list",9,"The Lawyer's Twenty Minutes",[
    "The legal-aid clinic gives you twenty minutes and a lawyer, Ms. Ferreira, who draws two columns on a legal pad: APPEAL and CASE. Under APPEAL she writes: file it early, in writing, keep the stamp. Under CASE she writes: housing first, everything dated.",
    "You have the right to counsel in the dependency case, and to appointed counsel if you cannot afford one (42 Pa.C.S. § 6337). The appeal, she says, is simpler than people fear and stricter than people hope: the paper has to exist, and it has to be on time."],
    [C("Ask her to help you draft the appeal letter today, while you are sitting here","draft_appeal",flags=["lawyerMet"],hidden="Parent consulted counsel about both tracks",note="Twenty minutes, used like an hour."),
     C("Take her card and plan to draft the letter at home this weekend","draft_appeal",note="The card goes in the folder. The weekend, as weekends do, fills up.")]),
  N("draft_appeal",12,"One Letter, Two Copies",[
    "The appeal letter is half a page: your name, the report number, the words amend or expunge, your signature, today's date. Ms. Ferreira's advice is mechanical: mail one copy so it leaves a record, keep one copy, and photograph the stamped receipt.",
    "It feels too small to matter. She smiles the smile of a woman who has watched small letters move large files."],
    [C("Mail the appeal this week and keep the stamped copy in the folder","appeal_sent",cash=-10,flags=["appealFiled"],hidden="Indicated-report appeal filed in writing within the 90-day window",note="Filed on day 12 of 90. The clock that scared you is now the clock that protects you."),
     C("Hold the letter until you know more about what the agency has","appeal_risk",note="Knowing more is a plan. It is also how day 12 becomes day 60.")]),
  N("appeal_risk",40,"The Letter in the Drawer",[
    "The letter is still in the drawer, under the good scissors. The housing hunt ate April. The study ate May. The appeal window did not eat anything; it just quietly counted, the way clocks do, indifferent rather than cruel.",
    "There is still time — that is the dangerous sentence. There is less of it than the sentence suggests."],
    [C("Mail it today, stamped copy in the folder, no more drawer","appeal_sent",cash=-10,flags=["appealFiled"],hidden="Indicated-report appeal filed in writing within the 90-day window",note="Day 40 of 90. Late is a direction, not a destination — this once."),
     C("Wait until the review hearing settles the case side first","end_registry",note="The hearing settles the case. It was never going to settle the registry.")]),
  N("appeal_sent",18,"The Boiler, On Paper",[
    "The landlord's repair log exists — if you ask for it in writing. The boiler company's invoice exists too, dated the week of the cold night, with the words emergency replacement on it. Paper like this does not argue. It simply sits in a file being true.",
    "Your caseworker, Ms. Petrov, says she can note your explanation in the file. Noting is good. Attached is better."],
    [C("Request the repair log and invoice in writing and attach copies to both files","records_beat",cash=-5,flags=["repairPaper"],hidden="Landlord repair log and boiler invoice obtained and filed",note="The coldest night of February, now with documentation."),
     C("Let the caseworker note your explanation — that should be enough","records_beat",note="Your explanation, in her words, in her summary. Summaries summarize.")]),
  N("records_beat",24,"Asking for the File",[
    "A parent advocate at the clinic mentions the move nobody had mentioned: you may request the agency's record of your own case, and the material shall be released upon request (55 Pa. Code § 3130.44(d)). Some pages come back with black bars over other people's names — that is the rule, not a trick (55 Pa. Code § 3130.44(f)).",
    "What arrives will show you what the appeal reviewer will see, and what the review hearing will read. It is the only mirror the system hands you."],
    [C("Sign the written record request and keep the stamped copy","packet_back",cash=-5,flags=["recordsRequested"],hidden="Case record requested in writing under § 3130.44(d)",note="The mirror is requested. It arrives the way mirrors do in this system: by mail, in an envelope too small for it."),
     C("Skip it — you know what happened that night","packet_back",note="You know what happened. The file knows what was written. Those are different knowledges.")]),
  N("packet_back",38,"What the Mirror Shows",[
    "The packet shows two things you did not expect. The investigator's note says the children were 'appropriately dressed for the cold' and the neighbor 'seemed credible.' And your own explanation — the boiler, the neighbor, the one night — is recorded in a single line: 'Mother states housing issue.'",
    "Six words for the worst night of your winter. The appeal reviewer will read those six words unless the file gains the repair log, the invoice, and a page in your own hand."],
    [C("Write a one-page statement in your own words and file it with the repair documents, in both files","statement_filed",cash=-5,flags=["statementFiled"],hidden="Parent's written statement and repair documents filed in both tracks",note="Your page, your words, both files. The six-word version is no longer the only version."),
     C("The note about the children being dressed warmly is enough — leave the file as it is","statement_filed",note="It is a good line. It is one line, in someone else's hand.")]),
  N("statement_filed",47,"The Study Comes Back",[
    "Rania's study is approved. The bunk bed exists now; Zayd has claimed the top in writing, on the refrigerator, in crayon. The kinship worker notes the placement is stable and the children are doing well — the sentence every later reader will weigh.",
    "Stability at Rania's cuts both ways, and Ms. Ferreira warned you about the second edge: a comfortable placement can make a slow case feel finished. The review hearing is in three weeks. Comfortable is not the goal. Home is."],
    [C("File a one-page progress summary before the review — housing application, shifts, the repaired boiler, the filed appeal","review_prep",cash=-5,flags=["reviewFiled"],hidden="Written progress summary filed before the review hearing",note="The judge will meet your spring as a document before she meets you as a person."),
     C("Show up and explain it all in person at the hearing","review_prep",note="You will get minutes. The document would have gotten there first and stayed longer.")]),
  N("review_prep",61,"Housing, With a Date On It",[
    "The waitlist letter arrives: your application for the two-bedroom on Chestnut Street is approved pending a unit, estimated June. It is not a key. It is a dated letter on letterhead saying a key is coming, which in this system is the next best thing — the raw material of a compelling reason, written down.",
    "The review is in one week. The appeal reviewer, in a separate building, is reading a file that now contains your page."],
    [C("Attach the waitlist letter to your progress summary and hand a copy to every party at the review","review_day",flags=["housingLetter"],hidden="Dated housing waitlist letter filed and distributed",note="Everyone at the table reads the same June."),
     C("Mention the letter if the judge asks about housing","review_day",note="Judges ask about what is in front of them. Give them something to ask about.")]),
  N("review_day",68,"The Review",[
    "The courtroom is smaller than its reputation. The judge has the file: the study, your summary, the waitlist letter, the repair log. The caseworker confirms the placement is stable, the visits are kept, the boiler is replaced, the appeal is pending in its own building.",
    "The judge looks up. 'What is the plan,' she asks, 'and what is it waiting on?' Everything you filed was, in the end, an answer to that one question."],
    [C("Ask, through your lawyer, for a step-down: expanded time at home now, return when the unit opens, the plan in writing","end_home",req=["recordsRequested","appealFiled","reviewFiled"],note="The answer exists because the paper does."),
     C("Ask for return today, on the strength of everything, without the step-down plan","end_plan",note="Almost is a real outcome in this system. It is just not the best one."),
     C("Let the hearing happen to you and hope the file speaks","end_plan",note="Files speak in the order they are read. Yours needed a voice.")]),
  N("end_home",82,"Home by Friday",[
    "The order is two pages. Expanded time begins this week; the children return home when the Chestnut Street unit opens, with the kinship placement held open as the family's own safety net — Rania, written into the order as what she always was: the plan, not the problem.",
    "In June you carry Noor up the new stairs past a boiler room with a new boiler. In July, a second envelope arrives: the appeal has been granted, the indicated report amended to unfounded on the record the file now holds. Two files, two clocks — both answered with paper, in the right order.",
    "Zayd's written claim on the top bunk is honored, by acclamation."],
    ending=True, debrief=[
      "THE TWO CLOCKS — The appeal clock: notified Monday, March 2, 2026; the written appeal was due within 90 days — Sunday, May 31, 2026 (23 Pa.C.S. § 6341(a)(2)) — and on the winning route it was mailed on day 12. The case clock: no single date, but a sequence — study, services, review — that moved at the speed of dated paper. The whole capstone lesson is the order of operations: protect the deadline that cannot move first, then build the record the movable ones read.",
      "THE RECORD REQUEST — Agency records are released on request (55 Pa. Code § 3130.44(d)); the packet showed the parent her own case in the system's six-word summary, in time to file her own page. Redactions of other people's information are the regulation's design, not a withholding trick (55 Pa. Code § 3130.44(f)). Counsel in the dependency case is a right, including appointed counsel for those who cannot afford it (42 Pa.C.S. § 6337).",
      "WHAT NO STRATEGY CONTROLS — The waitlist, the study queue, the appeal reviewer's reading, and the judge. This ending is written as a win because the documents existed to be read; outcomes in real cases also turn on workers, judges, housing stock, and luck, and the same paper in a different county can meet a different day."]),
  N("end_plan",82,"The Plan Continues",[
    "The children stay with Rania a while longer. The plan continues: more time, another review, the unit still coming in June. Nobody in the courtroom thought you were failing; the file simply did not finish its sentence, and the court does not complete sentences for people.",
    "The appeal, if you filed it, still runs in its building. The case will get another hearing. The folder is not closed — it is continued, which in this system is both a mercy and a cost, paid in weeks of a childhood."],
    ending=True, debrief=[
      "A PARTIAL WIN, NAMED HONESTLY — The placement is safe, the kinship door stayed open, and the case continues toward return. What separated this ending from the best one was not effort or love; it was whether the record was requested (§ 3130.44(d)), the appeal was on time (§ 6341(a)(2)), and the progress existed as filed paper before the hearing rather than as testimony during it.",
      "WHAT NO STRATEGY CONTROLS — Housing supply, the study queue, and the individual judge. A continued case is not a lost one; it is a clock still running, and the same moves remain available at the next review — the file keeps what it is given, whenever it is given."]),
  N("end_registry",96,"The Quiet Registry",[
    "The case side ended the way case sides often do: the children came home in the summer, the file closed, the folder went into a drawer. The registry side never got its letter. Ninety days from March 2 was May 31, and May 31 passed in the drawer, next to the good scissors.",
    "The indicated report remains. It will surface on clearances — at the playroom job, at the school volunteer desk, at the nursing program you talked about in Rania's kitchen. The case is over. The word remains, because one clock in this story could not be extended by anybody's good intentions."],
    ending=True, debrief=[
      "THE CLOCK THAT COULD NOT MOVE — A perpetrator may appeal an indicated report in writing within 90 days of notification (23 Pa.C.S. § 6341(a)(2)). Notified Monday, March 2, 2026, the deadline was Sunday, May 31, 2026. Help on the case side — studies, services, hearings — does not file the appeal; only the letter does, and only on time.",
      "WHAT NO STRATEGY CONTROLS — Nothing in this ending turns on the worker, the judge, or the facts of the cold night. It turns on a date and a drawer. That is precisely why the appeal letter is taught as the first move, not the last: it is the one piece of paper in the whole system that cannot be written late."]),
 ],
 strategy=dict(
  win_honest="This is a **full** win, and the scenario is built so a Foundation player can reach it: both clocks answered — the children home on a written step-down, the kinship placement preserved as the family's own safety net, and the indicated report amended on appeal. It is the gentlest capstone in the library because its mechanics are the library's core lesson in its purest form: file the immovable deadline first, then build the record.",
  law=[
   "**Two files, two clocks.** The indicated report runs on the CPSL appeal clock — a written appeal within 90 days of notification (23 Pa.C.S. § 6341(a)(2)), here March 2, 2026 → May 31, 2026. The dependency case runs on studies, services, and reviews with no single date. The strategy is sequencing: the appeal letter goes out in week two, before the case work can eat the calendar.",
   "**The record request is the mirror.** Agency records are released on request (55 Pa. Code § 3130.44(d)), with other people's information redacted by design (55 Pa. Code § 3130.44(f)). The packet reveals the six-word version of the parent's worst night in time for her own page to join the file in both tracks.",
   "**Counsel is machinery, not luxury** (42 Pa.C.S. § 6337): twenty clinic minutes produce the two-column plan — APPEAL and CASE — that the whole route follows.",
   "**Kinship stability is evidence, not an ending.** The approved study and stable placement support the step-down; the filed progress summary and dated housing letter are what convert stability into a plan the court can order."],
  traps=[
   ("Holding the appeal letter \"until you know more\" at *One Letter, Two Copies*, then waiting again at *The Letter in the Drawer*","the 90-day window closes and the route ends at **The Quiet Registry** — the children home, the word permanent. No hearing on the case side can reopen it."),
   ("Letting the caseworker \"note\" the boiler explanation instead of attaching the repair log and invoice","the file keeps a six-word summary — 'Mother states housing issue' — for both the reviewer and the court to read."),
   ("Skipping the record request","the parent never sees the file's version of her, and the winning choice at *The Review* is flag-gated shut: it requires **recordsRequested**."),
   ("Explaining in person instead of filing the progress summary","minutes of testimony against a file the court read beforehand; the route lands at **The Plan Continues**, a partial win.")],
  uncontrolled="The waitlist, the study queue, the appeal reviewer's reading, and the judge. The route controls the order of the paper and the dates on it — which, in a two-file case, turns out to be most of what was ever controllable."),
)

# ---------------- S128 — Hard ----------------
S128 = dict(
 num=128, name="Two Doors, One Hallway", tier="Hard",
 startDateISO="2026-04-06", startCash=180,
 summary="A father fights on two fronts in the same month: a Bureau appeal of an indicated report, where the agency must hand over its investigation evidence, and dependency reviews where his daughter sits with her grandmother. Win one file and the other gets easier; ignore either and both harden.",
 contentNote="This scenario depicts a dependency case with a kinship placement and an administrative appeal of an indicated report. There is no graphic content. Players may skip any scene or use the quick exit at any time.",
 offsetNote=" (the date of the indicated-report notice)",
 win_id="end_both",
 nodes=[
  N("start",0,"The Notice and the Nursery",[
    "Your name is Dario. You drive a delivery van, you are taking the commercial license course at night, and your daughter Anouk is two. Three weeks ago she toppled off a low playground platform at your sister's barbecue and split her chin; the urgent-care doctor stitched it, noted the bruise pattern on her thigh from the fall, and — as doctors must — made a report.",
    "Anouk is with her grandmother Odette while the case runs. And today the second envelope arrived: the report is indicated, naming you. The letter says the entry can affect work in childcare, schools, and — the licensing board's letter last week hinted — some transportation endorsements. Your appeal deadline is printed nowhere on it. Your lawyer finds it in the statute: 90 days from notification (23 Pa.C.S. § 6341(a)(2)). Notified Monday, April 6, 2026 — the window closes Sunday, July 5, 2026."],
    [C("Put both tracks on one page: APPEAL by July 5; CASE reviews monthly","two_tracks",flags=["calendarSet"],hidden="Both tracks calendared from the notice date",note="One page, two clocks, no surprises."),
     C("Deal with the court case first — the registry letter can wait","two_tracks",note="It can. That is the problem with waiting: it always can, until it can't.")]),
  N("two_tracks",4,"Ms. Lindqvist Draws Two Doors",[
    "Your lawyer, Ms. Lindqvist, draws two doors in the same hallway. Door one: the Bureau of Hearings and Appeals, a paper courtroom where the county agency must prove its report should stay indicated — the burden is theirs, by substantial evidence (23 Pa.C.S. § 6341(c.2)(5)). Door two: the dependency court, where Anouk's placement and your services are decided.",
    "'Different rooms,' she says, 'same file. What is written in one hallway is carried into the other. We write carefully in both.' Counsel beside you in the dependency case is your right (42 Pa.C.S. § 6337); the appeal is yours to file, in writing, on time."],
    [C("File the appeal this week, stamped copy in the folder","appeal_filed",cash=-10,flags=["appealFiled"],hidden="Indicated-report appeal filed in writing within the 90-day window",note="Day 4 of 90. The first door is open."),
     C("Wait for the first dependency review, then decide about the appeal","appeal_late_risk",note="Reviews have a way of multiplying. Deadlines do not.")]),
  N("appeal_late_risk",31,"A Month of Reviews",[
    "May is reviews, a service plan, a parenting class with a sign-in sheet. The appeal letter sits drafted in your email, unsent, aging like milk. The window has 59 days left, then 40, then — the arithmetic is not complicated, which is what makes it dangerous."],
    [C("Send it today — day 31 is still inside the window","appeal_filed",cash=-10,flags=["appealFiled"],hidden="Indicated-report appeal filed in writing within the 90-day window",note="Inside the window, with room to spare. Barely counts as late; counts completely as filed."),
     C("Polish it one more week — it has to be perfect","end_quiet128",note="It became perfect on day 92. The Bureau does not grade on style.")]),
  N("appeal_filed",11,"Odette's Porch",[
    "Odette's porch has a gate, a rug, and a granddaughter who has learned to say 'again' about everything. The kinship worker visits, checks the clearances file, and mentions the study is 'in process' — the system's favorite tense.",
    "Your visits happen here, twice a week, and a sign-in sheet has appeared on Odette's refrigerator, because Odette is a woman who has read files before and trusts ink."],
    [C("Ask the kinship worker, in writing, what the study still needs and by when","study_paper",cash=-5,flags=["studyList"],hidden="Kinship study requirements and dates obtained in writing",note="A list with dates. The study is now a checklist instead of a tense."),
     C("Let the study proceed at its pace — Odette's house speaks for itself","study_paper",note="Houses do not speak in hearings. Paper about houses does.")]),
  N("study_paper",18,"The Evidence You Are Owed",[
    "Ms. Lindqvist files a short letter in the appeal: under the appeal rules, the agency must provide the appellant all evidence gathered during the investigation that is relevant to the determination — including potentially exculpatory evidence — no later than ten days after the scheduling order (23 Pa.C.S. § 6341(c.2)(4)).",
    "When the packet comes, it holds the urgent-care record, the investigator's notes — and a page you have never seen: the triage nurse's addendum, written that night, describing the fall mechanics as 'consistent with the reported low-height fall.' It was in their file the whole time. Now it is in yours."],
    [C("Build the appeal around the addendum and the stitch record — the agency's own paper","evidence_built",cash=-5,flags=["evidenceReceived"],hidden="Investigation evidence obtained under § 6341(c.2)(4), including the triage addendum",note="The strongest exhibit in your appeal was written by their nurse, on their form, on the night itself."),
     C("Rely on your own account at the hearing — you were there, they weren't","evidence_built",note="You were. The addendum was there too, and it does not have to be believed. It has to be read.")]),
  N("evidence_built",25,"The Case File, Requested",[
    "The dependency side has its own mirror: the agency's case record, released on request (55 Pa. Code § 3130.44(d)). Ms. Lindqvist suggests requesting it now, so the review next month is argued from their dates, not your memory of them.",
    "The packet will arrive redacted in places — other people's names blacked out, which is the regulation's rule (55 Pa. Code § 3130.44(f)), not a message."],
    [C("Sign the written request and file the stamped copy","case_packet",cash=-5,flags=["recordsRequested"],hidden="Case record requested in writing under § 3130.44(d)",note="Requested on day 25. The review will be read from paper now."),
     C("Skip it — the appeal packet already showed you the important page","case_packet",note="The appeal packet shows the investigation. The case record shows the case. Different files, different traps.")]),
  N("case_packet",39,"What the Case Record Shows",[
    "The record shows the service plan's soft underbelly: the parenting class referral was sent three weeks after the plan was signed, and the visit schedule at Odette's was 'to be arranged' for the first nine days. Nobody hid this. It is simply written in the passive voice, where responsibility goes to be alone.",
    "It also shows every visit you kept, signed in Odette's ink, and the class certificates you filed yourself. The file, read whole, is fairer to you than the summary was."],
    [C("Write a one-page chronology — referral dates, visit dates, certificates — and file it in both tracks","chronology",cash=-5,flags=["chronologyFiled"],hidden="Dated chronology of referrals, visits, and certificates filed in both tracks",note="One page, twenty-two dates. Both hallways will read it."),
     C("Save the chronology for the appeal hearing only","chronology",note="The dependency judge reviews next month. Paper filed in one hallway stays in that hallway unless you carry it.")]),
  N("chronology",52,"The Scheduling Order",[
    "The Bureau's scheduling order sets the appeal hearing for Friday, August 14, 2026. Ms. Lindqvist reads the second paragraph aloud: the hearing officer's decision must be entered, filed, and served within 45 days of the hearing's conclusion (23 Pa.C.S. § 6341(c.3)). Your appeal, filed in spring, will be decided by early autumn at the latest — the decision has a clock too.",
    "Meanwhile the dependency review lands first, in July. The hallway order matters: a strong review strengthens the appeal's air; a weak one follows you through door one."],
    [C("Prepare the review like it's the appeal's opening statement — chronology, certificates, the study checklist, all filed a week early","review_prep",flags=["reviewFiled"],hidden="Review packet filed a week before the hearing",note="Filed early, read early. Hearings reward the prepared with the only currency they have: the judge's attention."),
     C("Prepare the appeal and treat the review as a formality","review_prep",note="There are no formalities in a hallway with two doors. There are only first impressions, twice.")]),
  N("review_prep",74,"The July Review",[
    "The judge reads the chronology the way judges read: silently, then again at the good parts. The caseworker confirms the visits, the class, the study nearly complete at Odette's. The agency's counsel does not contest the referral gap — it is, after all, in the agency's own record, in the passive voice.",
    "The judge asks what the plan needs to finish. It is the question your packet was built to answer."],
    [C("Propose the dated finish: study completion, two more class sessions, step-down to overnights at Odette's, return on the September review","appeal_hearing",req=["recordsRequested","appealFiled","chronologyFiled"],note="Dates answer dates. The order writes itself from your page."),
     C("Ask for Anouk home today — the record is good enough","end_stepdown",note="Good enough gets you a step-down and a season. The best ending needed the dates."),
     C("Let your lawyer argue from memory of the file","end_stepdown",note="Memory argues well. Paper argues last.")]),
  N("appeal_hearing",130,"The Bureau Hearing",[
    "Friday, August 14, 2026. The Bureau hearing room has no robes and no flags, just a hearing officer, a microphone, and the agency's lawyer carrying the burden the statute assigns her: to prove by substantial evidence that the report should remain indicated (23 Pa.C.S. § 6341(c.2)(5)).",
    "She presents the urgent-care record. Ms. Lindqvist presents the same record — all of it, including the addendum the agency's own file held — plus the chronology from the case record, the certificates, and Odette's sign-in sheets. The hearing officer keeps returning to the nurse's sentence. Evidence that outweighs inconsistent evidence is the standard; the file, read whole, does not outweigh itself."],
    [C("Close on the addendum and the burden: their paper, their standard, their burden","end_both",note="Short closings win paper cases."),
     C("Close on fairness and Anouk's laugh and how much she has grown","end_upheld",note="All true. None of it is the standard the officer must apply.")]),
  N("end_both",175,"Both Doors",[
    "The decision is entered on day 36 after the hearing — inside the 45-day window (23 Pa.C.S. § 6341(c.3)): the report is amended to unfounded. The evidence provided under the appeal rules did what it was always capable of doing; it just needed someone to ask for it, file it, and carry it through both doors.",
    "The September review is shorter than anyone expected. With the registry clear and the dependency record a chronology of kept dates, the court orders Anouk home on the plan the July order wrote. Odette's porch gate gets a new job: keeping nothing out, just marking where the yard begins.",
    "Anouk says 'again' about the porch swing. Some words a file cannot hold. This one, it turns out, it could."],
    ending=True, debrief=[
      "THE APPEAL TRACK — Filed in writing inside 90 days of the April 6, 2026 notice (deadline Sunday, July 5, 2026) (23 Pa.C.S. § 6341(a)(2)). At the hearing the agency bore the burden of proving by substantial evidence that the report should remain indicated (23 Pa.C.S. § 6341(c.2)(5)); the decisive document was the agency's own triage addendum, obtained because the appeal rules entitled the appellant to all relevant investigation evidence, including the potentially exculpatory, within ten days of the scheduling order (23 Pa.C.S. § 6341(c.2)(4)). The decision issued within the 45-day window the statute sets (23 Pa.C.S. § 6341(c.3)).",
      "THE CASE TRACK — The dependency record, requested under 55 Pa. Code § 3130.44(d), supplied the chronology — late referral, arranged-late visits, kept appointments — that shaped the July review and the September return. Counsel throughout is the parent's right in the dependency case (42 Pa.C.S. § 6337). The tracks are legally separate and practically one file: paper filed in one hallway should be carried, deliberately, into the other.",
      "WHAT NO STRATEGY CONTROLS — The hearing officer's credibility calls, the agency's litigation choices, and the judge. This route won because the exculpatory page existed and was asked for; a file without that page is a different case, and the same moves honestly made can meet a different reader."]),
  N("end_stepdown",175,"The Step-Down Season",[
    "Anouk comes home in stages: overnights, then weekends, then the slow unwinding of Odette's spare crib. The appeal is still pending in its building, undecided in this telling, and the case closes a season later than it needed to.",
    "Nothing here is a disaster. It is the ordinary cost of a hallway walked one door at a time: months of a two-year-old's life, spent in the correct order but at the slower speed."],
    ending=True, debrief=[
      "A PARTIAL WIN, NAMED HONESTLY — Return home on a step-down, the appeal unresolved on this branch. What separated it from the best ending was sequencing: the record requested (§ 3130.44(d)), the chronology filed in both tracks, and the dated finish proposed at the review instead of asked for outright.",
      "WHAT NO STRATEGY CONTROLS — Hearing officers, judges, and calendars. A step-down is the system moving at its documented speed; the route's claim is only that paper, filed in both hallways, moves it faster."]),
  N("end_upheld",175,"Upheld, and Home Anyway",[
    "The decision upholds the report. The hearing officer credits the urgent-care summary over the addendum, and the indicated entry stands — with the further clocks the debrief below names, because an upheld appeal is a result, not the end of the road.",
    "Anouk still comes home that autumn; the dependency court reads its own record and is not bound by the registry's. You will carry the entry on clearances. You will also carry the file that shows how close the question was, and the dates of the doors that remain."],
    ending=True, debrief=[
      "AFTER AN UPHELD APPEAL — The parties have 15 calendar days from the mailing date of the Bureau's final order to ask the Secretary to reconsider, and 30 calendar days from the mailing date to perfect an appeal to Commonwealth Court (23 Pa.C.S. § 6341(g)). Those clocks run from mailing, not from your reading of the letter — open the envelope the day it comes.",
      "THE TRACKS STAY SEPARATE — The dependency court's return order rests on the dependency record (counsel: 42 Pa.C.S. § 6337; records: 55 Pa. Code § 3130.44(d)). An indicated finding is serious — it surfaces on clearances — but it is not a dependency adjudication, and this ending is written to keep that distinction where the law keeps it. WHAT NO STRATEGY CONTROLS: the hearing officer's weighing of two medical sentences written the same night. Credibility is the one exhibit no one can file."]),
  N("end_quiet128",96,"Day Ninety-Two",[
    "The letter was perfect. Every sentence earned its place. It was mailed on day 92, and the Bureau's reply was one paragraph: the request was not filed within 90 days of notification, as the statute requires.",
    "The dependency case goes on without the appeal — Anouk with Odette, reviews, classes, the ordinary machinery — but the registry door is closed, and it was the only door in the hallway with a lock that time itself operates."],
    ending=True, debrief=[
      "THE ONE UNFORGIVING CLOCK — 90 days from notification (23 Pa.C.S. § 6341(a)(2)): notified Monday, April 6, 2026; the last day was Sunday, July 5, 2026. Every other deadline in this game bends, continues, or resets. This one is jurisdictional in effect: a beautiful late letter and no letter arrive at the same desk.",
      "WHAT NO STRATEGY CONTROLS — Nothing about the facts changed on day 92. The fall, the stitches, the addendum all remain true. Only the forum is gone — which is why every strategy guide in this library files the appeal early and polishes later, if at all."]),
 ],
 strategy=dict(
  win_honest="This is a **full** win: the report amended to unfounded and Anouk home on the court's own plan. It is a Hard scenario because both victories run through the same small set of paper moves — an early appeal, an evidence demand the statute entitles the appellant to make, a record request, and one chronology carried deliberately through both doors.",
  law=[
   "**The appeal clock and the burden, together.** Written appeal within 90 days of notification (23 Pa.C.S. § 6341(a)(2)); at the hearing, the agency bears the burden of proving by substantial evidence that the report should remain indicated (23 Pa.C.S. § 6341(c.2)(5)). The route files early precisely so the hearing can be about the burden, not about the calendar.",
   "**The evidence you are owed.** The appellant is entitled to all relevant investigation evidence, including the potentially exculpatory, within ten days of the scheduling order (23 Pa.C.S. § 6341(c.2)(4)). The triage addendum — the case's decisive page — arrives through this door and no other.",
   "**The decision has a clock too:** entered, filed, and served within 45 days of the hearing's conclusion (23 Pa.C.S. § 6341(c.3)); the win lands on day 36 of that window. If the appeal had been upheld, § 6341(g)'s 15-day reconsideration and 30-day Commonwealth Court clocks would run from the order's mailing date — the losing ending's debrief teaches them.",
   "**The case track runs on the same fuel:** the § 3130.44(d) record request (redactions under (f) are design, not withholding), counsel under 42 Pa.C.S. § 6337, and a chronology filed in both tracks because paper does not walk hallways by itself."],
  traps=[
   ("Polishing the appeal letter past the window at *A Month of Reviews*","Day 92 is day never: the route ends at **Day Ninety-Two** with the registry door closed for good."),
   ("Resting on your own account instead of the evidence packet at *The Evidence You Are Owed*","your testimony must be believed; the nurse's addendum only has to be read. The closing built on fairness instead of the burden ends at **Upheld, and Home Anyway**."),
   ("Skipping the case record request","the July review is argued from memory, the referral gap stays in the passive voice, and the gated choice — requiring **recordsRequested** + **appealFiled** + **chronologyFiled** — stays shut; the route lands on the step-down."),
   ("Treating the July review as a formality","the review is the appeal's opening statement; the hallway hears everything twice.")],
  uncontrolled="The hearing officer's weighing of two medical sentences written on the same night, the agency's litigation posture, and the individual judge. The route controls whether the decisive page is in the room and whose burden it is — in a paper case, that is most of the game."),
)

# ---------------- S129 — Hard ----------------
S129 = dict(
 num=129, name="The Year in a Folder", tier="Hard",
 startDateISO="2025-09-08", startCash=150,
 summary="A mother whose son entered care as an infant plays a full year of services, visits, and reviews — and discovers that the folder she keeps, page by dated page, is the argument that brings him home at the month-thirteen review.",
 contentNote="This scenario depicts an infant's foster placement, a year of services and reviews, and a reunification hearing. There is no graphic content. Players may skip any scene or use the quick exit at any time.",
 offsetNote=" (the child's foster-care entry date)",
 win_id="end_home129",
 nodes=[
  N("start",0,"Month Zero",[
    "Your name is Imani. Your son Emeka was born in August, and in September — after a postpartum crisis that this story treats the way the file should have: as a medical event with a paper trail — the court placed him in foster care and handed you a service plan with nine boxes on it.",
    "Nine boxes, twelve months, one folder. The foster mother, Mrs. Abernathy, sends a photo every Friday. Your lawyer, Mr. Osei, says the sentence you will hear in every room this year, so hear it from him first: the court can only act on what is in the record. Counsel is your right in this case (42 Pa.C.S. § 6337). The record, starting today, is partly yours to write."],
    [C("Start the folder today: plan, orders, every paper, in date order","folder",flags=["folderKept"],hidden="Parent's parallel folder started at month zero",note="A folder is a memory that can be handed to a judge."),
     C("Rely on the agency's file — it's the official one","folder",note="It is. It will also be the only one in the room, written in the passive voice.")]),
  N("folder",14,"Nine Boxes",[
    "The plan's nine boxes: treatment, parenting course, visitation, housing, employment or benefits, medical follow-through, and three more that blur together on the page. Two of them depend on referrals the agency must send. One depends on a waitlist. All nine depend, in the end, on dates.",
    "Mr. Osei circles the two referral boxes. 'When a referral is late,' he says, 'the box looks unchecked from a distance. Get the dates.'"],
    [C("Ask the caseworker, in writing, for each referral's date — promised, sent, started","referral_dates",cash=-5,flags=["referralDates"],hidden="Referral chronology requested in writing",note="Three dates per referral. The difference between them is where cases hide."),
     C("Trust the plan's timeline — it says services begin within thirty days","referral_dates",note="Plans say many things. Dates say when.")]),
  N("referral_dates",35,"The First Visit Room",[
    "The visit room has a clock, a rug, and a box of toys that Mrs. Abernathy supplements from her own house, because Emeka has opinions about exactly one rattle. You arrive early. You arrive early every time, because the sign-in sheet is the one document in this building that you author yourself.",
    "The visit supervisor notes 'mother appropriate and engaged.' Four words a week. By December they will be a paragraph the court has read fifty times."],
    [C("Sign in and out precisely, and keep your own visit log with dates and one line each","visit_log",flags=["visitLog"],hidden="Visit log kept with dates from the first month",note="Your log and their sheet, agreeing. Agreement is a kind of evidence."),
     C("Just be present — the bonding is the point, not the paperwork","visit_log",note="The bonding is the point. The paperwork is how the court finds out.")]),
  N("visit_log",63,"The Referral That Wasn't",[
    "The parenting course box is still unchecked at month three, and now the file can say why, because you asked for dates: the plan was signed September 22; the referral was sent November 10; the course's next cohort starts in January. Seven weeks of the plan's twelve months, spent in a mailbox.",
    "Your caseworker is not defensive when you raise it — she is relieved someone wrote it down. 'Put it in a letter to me,' she says, 'so it's in the file where the review will see it.'"],
    [C("Write the letter: plan date, referral date, cohort date — polite, dated, copied","gap_letter",cash=-5,flags=["gapDocumented"],hidden="Referral gap documented by dated letter to the file",note="The gap is now a fact with dates instead of an impression with adjectives."),
     C("Raise it verbally at the next team meeting","gap_letter",note="Raised, nodded at, minuted as 'discussed concerns.' Concerns are not dates.")]),
  N("gap_letter",91,"The Record, Requested",[
    "Mr. Osei suggests the mirror move at the winter review: request the agency's record of the case in writing — the material is released upon request (55 Pa. Code § 3130.44(d)), with other people's information redacted as the rule provides (55 Pa. Code § 3130.44(f)).",
    "'You are not accusing anyone of anything,' he says. 'You are asking to read the book the court will read. Everyone should read the book.'"],
    [C("Sign the written request; keep the stamped copy in the folder","record_back",cash=-5,flags=["recordsRequested"],hidden="Case record requested in writing under § 3130.44(d)",note="Requested at month three. The book is coming."),
     C("Wait until closer to the big review — no need to seem adversarial","record_back",note="Asking for your own record is not adversarial. Waiting, though, is a strategy with a price: the gaps stay invisible until they're old.")]),
  N("record_back",120,"Reading the Book",[
    "The record confirms the referral gap — and finds a second one: the housing referral was never sent at all, an omission visible only because the file lists what it did send. Your treatment attendance is recorded as 'consistent,' your visits as 'kept, appropriate.'",
    "The book is not your enemy. Read whole, it is a better witness for you than its summaries were. It just needs its gaps named, in writing, while there is time to close them."],
    [C("File a short written response: the two gaps, with dates, and your attendance record, with dates","response_filed",cash=-5,flags=["responseFiled"],hidden="Written response filed naming referral gaps with dates",note="Two gaps, two dates each, one page. The book now contains its own correction."),
     C("Tell your lawyer and let him raise it orally at the review","response_filed",note="He raises it well. Orally. The review reads the file the week before, alone.")]),
  N("response_filed",168,"The Housing Box",[
    "Spring. The housing referral, re-sent after your letter, reaches the top of a waitlist: a two-bedroom near the bus line, available in July, held with a letter on letterhead. It is not a key. It is the dated raw material of the last unchecked box.",
    "The treatment program sends its own letter: completion expected in June, attendance 'exemplary' — their word, their letterhead."],
    [C("File both letters and ask the agency to note the July unit in the case plan itself","plan_noted",cash=-5,flags=["housingLetter"],hidden="Housing and treatment letters filed; plan updated in writing",note="The plan now says July in the agency's own hand."),
     C("Keep the letters for the review — a surprise reveal helps","plan_noted",note="Hearings are not theaters. A letter filed in March is read; a letter revealed in June is examined.")]),
  N("plan_noted",224,"Month Nine Review",[
    "The month-nine review is quiet, which veterans of this hallway recognize as a sound: the judge moves through the plan box by box, and your folder and their file tell the same story — seven boxes closed, the course done, housing dated for July, visits a year of kept Tuesdays.",
    "The judge says the words that set the endgame: 'We'll take the permanency question at the thirteen-month review. I want the record complete by then.' Complete is a standard. It can be met on purpose."],
    [C("Ask Mr. Osei to build the review packet with you: every letter, log, certificate, and the gap chronology","packet_built",flags=["packetBuilt"],hidden="Review packet assembled from the folder and the record",note="The packet is the year, edited by dates."),
     C("The file speaks for itself by now — rest on it","packet_built",note="Files speak in the order they're read. Packets speak in the order you choose.")]),
  N("packet_built",300,"The Quiet Summer",[
    "July: the unit, the keys, a crib assembled by Mrs. Abernathy's husband, who refuses payment and accepts pie. August: overnight visits, then weekends, the sign-in sheet replaced by a calendar on your own refrigerator — kept, because habits built over a year do not retire on command.",
    "September approaches: month thirteen, the review the judge promised. The ASFA clock stands behind it — fifteen of the most recent twenty-two months is the filing horizon (42 U.S.C. § 675(5)(E)) — and your packet's job is to make the question before the court return, not exceptions."],
    [C("File the packet two weeks early, with a one-page summary Mr. Osei drafts and you sign","final_review",cash=-10,flags=["summaryFiled"],hidden="Final packet and signed summary filed two weeks before the review",note="Filed early, read early, argued last. The correct order."),
     C("Bring the packet to the hearing and hand it up","final_review",note="Paper delivered on the deadline is a speech. Paper filed early is a record.")]),
  N("final_review",396,"The Thirteen-Month Review",[
    "Entry was Monday, September 8, 2025. Today is the thirteen-month review, and the packet has been in the file for two weeks: nine boxes, each with its closing document; two gaps, each with its dates; a year of Tuesdays.",
    "The agency's counsel reads the same file and reaches the recommendation first, which is how you know the year worked: return home, with the plan's remaining supports converted to aftercare. The judge looks for a reason in the record to disagree with everyone, and the record — fairly, completely — does not contain one."],
    [C("Ask for the order to say it plainly: return home today, aftercare in writing","end_home129",req=["recordsRequested","packetBuilt","gapDocumented"],note="Today. The word the whole year was for."),
     C("Accept whatever the court proposes without asking","end_trial129",note="The court proposes a trial period first. Close, and slower.")]),
  N("end_home129",403,"Home at Thirteen Months",[
    "Emeka comes home on a Monday, one year and one week after the Monday he left, with a folder's worth of proof that the year happened the way you said it did. Mrs. Abernathy gets a standing Sunday invitation and a photo every Friday, a tradition now running in the other direction.",
    "The folder goes on a shelf, not into a drawer. Some families keep them forever. It is not a trophy. It is the record, and the record is what brought him home."],
    ending=True, debrief=[
      "THE YEAR'S LAW — Counsel throughout (42 Pa.C.S. § 6337); the case record released on request (55 Pa. Code § 3130.44(d)), its redactions governed by § 3130.44(f); and the permanency horizon behind the final review — fifteen of the most recent twenty-two months (42 U.S.C. § 675(5)(E); the parallel state review determination under 42 Pa.C.S. § 6351(f)(9)) — which this route never had to argue about, because the question the court reached first was return.",
      "THE REAL MECHANIC — Nothing in this scenario turns on a dramatic hearing moment. It turns on referral dates requested in writing, a gap letter the caseworker herself invited, and a packet filed two weeks early. The debriefs of the other endings show the same year at slower speeds: the facts were never the problem; their paper form was the whole contest.",
      "WHAT NO STRATEGY CONTROLS — Waitlists, cohort schedules, housing stock, and the individual judge. This route's claim is narrow and sufficient: every fact the court needed existed as dated paper before the court needed it. Outcomes also turn on workers, judges, and luck — the folder is how a parent makes sure luck is not carrying the whole case."]),
  N("end_trial129",403,"The Trial Period",[
    "The court orders a trial home placement first: ninety days of overnights stretching into residence, a further review in the new year, the file still open like a door not yet allowed to close.",
    "It is a good outcome wearing a slower costume. Emeka sleeps in his crib, in your home, while the system finishes convincing itself of what your folder already says."],
    ending=True, debrief=[
      "A PARTIAL WIN, NAMED HONESTLY — He is home; the case is not closed. What separated this ending from the best one was the last paper discipline: the packet and signed summary filed early (and the flags they require — **recordsRequested**, **packetBuilt**, **gapDocumented**). Hearings ratify records; they rarely assemble them.",
      "WHAT NO STRATEGY CONTROLS — Judicial caution is a variable no folder eliminates. A trial period is the system hedging; the folder's work is to make the hedge short."]),
  N("end_clock129",457,"The Fifteenth Month",[
    "This branch is the year played at the file's pace instead of yours: the gaps never got their letter, the record was never requested, and the reviews summarized a plan whose boxes looked — from the distance of a summary — simply unchecked.",
    "At fifteen of the most recent twenty-two months, the conversation changes its subject: from your progress to the agency's filing duty and its exceptions (42 U.S.C. § 675(5)(E)). The exceptions exist — kinship care, a documented compelling reason, services identified but not provided — but they must be documented to be argued, and documentation is the one crop this branch never planted."],
    ending=True, debrief=[
      "THE CLOCK, ARRIVED — Entry September 8, 2025 + 15 months = Tuesday, December 8, 2026 is the horizon this ending approaches (offset 457 ≈ month 15): the filing duty and its three exceptions (42 U.S.C. § 675(5)(E)) become the case's whole subject. The services-not-provided exception was this family's true story — two referrals, one seven weeks late, one never sent — and it was unwinnable in this branch because the dates were never put in writing while they were fresh.",
      "WHAT NO STRATEGY CONTROLS — Nothing about the mother's effort differs between this ending and the best one. The services were attended, the visits kept, the love constant. Only the paper differs — which is the scenario's entire, deliberate point: in month fifteen, the file is the facts."]),
 ],
 strategy=dict(
  win_honest="This is a **full** win: Emeka home at the thirteen-month review, on the agency's own recommendation, a full two months before the fifteen-month horizon. It is a capstone in Hard clothing — no single dramatic beat, just the library's paper disciplines (referral dates, gap letter, record request, early packet) sequenced across a year without a miss.",
  law=[
   "**The horizon behind everything:** fifteen of the most recent twenty-two months in foster care triggers the agency's filing duty unless an exception is documented (42 U.S.C. § 675(5)(E); state review determination at 42 Pa.C.S. § 6351(f)(9)). Entry Monday, September 8, 2025 → the fifteen-month date is Tuesday, December 8, 2026. The route's design goal is to make the court reach *return* at month thirteen so the exceptions never have to carry the case.",
   "**Referral dates are the services exception in embryo.** The plan's boxes depend on referrals the agency must send; asking for promised/sent/started dates in writing converts a passive-voice delay into dated facts — the same facts that, unclosed, become the § 675(5)(E) services-not-provided exception, and, closed, become the packet's proof the plan worked.",
   "**The mirror:** the case record on request (55 Pa. Code § 3130.44(d)); redactions under (f). The record found the second gap — a housing referral never sent — that no meeting had ever mentioned.",
   "**Counsel (42 Pa.C.S. § 6337)** frames the year from month zero: the court can only act on what is in the record, and the record is partly the parent's to write."],
  traps=[
   ("Trusting the plan's thirty-day service timeline at *Nine Boxes*","the referral gap lives in the passive voice until the review reads 'unchecked' as 'unengaged.'"),
   ("Raising the gap verbally at a team meeting instead of by dated letter","minuted as 'discussed concerns'; the gated win needs **gapDocumented**, and concerns are not a flag."),
   ("Skipping the record request to avoid seeming adversarial","the never-sent housing referral stays invisible; the packet cannot answer a gap it has never seen — the win's gate (**recordsRequested**) stays shut."),
   ("Handing the packet up at the hearing instead of filing it early","paper delivered on the deadline is treated as a speech; the route settles for **The Trial Period**, home but unclosed.")],
  uncontrolled="Waitlists, cohort start dates, housing stock, a caseworker's relief at being documented, and the judge's appetite for a clean record. The route controls only the year's paper form — and the scenario is built so that, this once, the paper form is the case."),
)

# ---------------- S130 — Hard ----------------
S130 = dict(
 num=130, name="Across the County Line", tier="Hard",
 startDateISO="2026-01-05", startCash=170,
 summary="Mid-case, a job moves the family across a county line — and the case must follow without losing a single page. Two children, two clocks, one exception packet in transit: the win is a transfer where the file arrives whole and the new court starts from your record, not from zero.",
 contentNote="This scenario depicts a dependency case transferred between counties, with reviews and a permanency timeline. There is no graphic content. Players may skip any scene or use the quick exit at any time.",
 offsetNote=" (the children's foster-care entry date)",
 win_id="end_whole",
 nodes=[
  N("start",0,"Two Children, Two Clocks",[
    "Your name is Petra. Bram, nine, and Sable, six, entered foster care on Monday, January 5, 2026, after the winter your hours were cut and the rent math stopped working — a sentence this story insists on writing plainly, because the file's version ('housing instability') sounds like weather and this was arithmetic.",
    "The children are with a foster family twenty minutes away. Your plan is underway: housing program, doubled shifts, visits kept. And last week, the warehouse across the county line offered you the full-time line job — the one that makes the rent math work forever instead of monthly. Moving for it moves the case. Cases, like families, do not always survive the trip intact."],
    [C("Tell your lawyer, Mr. Adeyemi, before you tell anyone else","lawyer_first",flags=["lawyerTold"],hidden="Counsel informed of the move before the agency",note="Sequence is a strategy. The lawyer hears it first; everyone else hears it as a plan."),
     C("Tell the caseworker at Thursday's visit — transparency first","lawyer_first",note="Transparency is a virtue. Unaccompanied transparency is a rumor with good intentions.")]),
  N("lawyer_first",6,"The Transfer Problem",[
    "Mr. Adeyemi does not talk you out of the job. He talks you into paperwork. 'A case that crosses a county line gets read twice,' he says, 'and the second reading starts from whatever physically arrives. Our job is to make sure what arrives is the whole story: the exception packet we're building, the visit log, the referral dates — not a summary of them.'",
    "Counsel is your right (42 Pa.C.S. § 6337), and in a transfer it becomes logistics: who sends what, to whom, by when, receipt confirmed in writing."],
    [C("Build the transfer inventory with him: every document, its date, its location in the file","inventory",flags=["inventoryBuilt"],hidden="Transfer document inventory built with counsel",note="An inventory is a promise the file makes to its future self."),
     C("Assume the counties handle transfers between themselves — it's routine","inventory",note="It is routine. Routinely, pages go missing at exactly the rate nobody counted them.")]),
  N("inventory",13,"The Exception Packet, So Far",[
    "What would travel: the record you requested in February's first weeks — wait, you haven't yet. Mr. Adeyemi stops the meeting. 'Before anything moves,' he says, 'we request the complete record here (55 Pa. Code § 3130.44(d)). You cannot inventory what you have not seen, and you cannot prove a page was lost if you never knew it existed.'",
    "The packet you are building answers the clock both children share: entry January 5, 2026; fifteen months lands Monday, April 5, 2027. The compelling-reason documentation — your housing program completion, the new full-time job, the children's school stability — must exist in the case plan before any transfer, while this county still knows your name."],
    [C("Sign the written record request today","record_req130",cash=-5,flags=["recordsRequested"],hidden="Case record requested in writing under § 3130.44(d) before transfer",note="Requested before the move. The mirror travels with you now."),
     C("Request it after the move, from the new county — cleaner","record_req130",note="Cleaner, and months later, and answered from whatever arrived. Order matters.")]),
  N("record_req130",27,"What the Record Holds",[
    "The record holds the whole winter: the visit log the foster parents countersigned, the housing program's dated letters, the referral chronology you requested in writing in week two — and one surprise: a case note describing your job offer as a 'possible relocation risk,' written the day you told the caseworker at the visit, before the plan existed to attach it to.",
    "Notes written early harden first. The correction is not an argument; it is a dated document of your own, filed beside it."],
    [C("File a dated statement: the job, the address, the school plan, the transfer request — beside the note, not against it","statement130",cash=-5,flags=["statementFiled"],hidden="Parent's dated statement and transfer plan filed beside the early case note",note="Beside, not against. Files believe neighbors more than opponents."),
     C("Ask for the note to be removed — it misrepresents you","statement130",note="Files almost never unwrite themselves. They do, however, accept additions with dates.")]),
  N("statement130",41,"The Plan, Amended in Writing",[
    "The current county's supervisor agrees to the transfer and — at Mr. Adeyemi's request, in the meeting, on paper — amends the case plan to document the compelling reason the clock will ask about next spring: reunification is progressing on dated evidence, and filing would not serve the children (the compelling-reason exception, 42 U.S.C. § 675(5)(E), lives or dies on whether the case plan documents it).",
    "A supervisor's spoken agreement is weather. The amended plan, signed and copied to you, is climate."],
    [C("Get the signed amended plan and the transfer letter before you give notice at the warehouse","plan_amended",cash=-5,flags=["packetBuilt"],hidden="Case plan amended in writing to document the compelling reason before transfer",note="Signed, copied, in the folder. The exception now travels as a plan entry, not a hope."),
     C("The supervisor agreed — start the job and let the paperwork follow","plan_amended",note="Paperwork that 'follows' a family across a county line arrives the way luggage follows a traveler: usually, eventually, lighter.")]),
  N("plan_amended",55,"Moving Day Arithmetic",[
    "The new apartment is smaller and nearer everything: the job, the children's new school, the bus that runs on Sundays. Bram has mapped the route to the foster family's house — they are keeping Sunday dinners, a line in the transfer plan you asked for and got, because continuity is a document too.",
    "The file's journey is less visible: a box, a scan queue, a new county's intake stack. Somewhere between the two buildings, your case becomes somebody's Tuesday."],
    [C("Send the receiving county a one-page introduction with your inventory attached — politely, through your lawyer","intro_sent",cash=-5,flags=["introSent"],hidden="Transfer inventory sent to the receiving county through counsel",note="The new county meets your case as a list before it meets it as a rumor."),
     C("Wait to be contacted — you're the parent, they'll reach out","intro_sent",note="They will. Eventually is a date other people's calendars choose.")]),
  N("intro_sent",76,"The New County's Reading",[
    "The receiving caseworker, Ms. Whitfield, is brisk and not unkind. She has read — you can tell from her questions — the summary. The summary is four pages for a five-month case, and it does what summaries do: your winter becomes 'housing instability, services ongoing,' and the exception documentation becomes a clause.",
    "'Your lawyer sent an inventory,' she says, almost surprised. 'The plan amendment is in it. The visit log is in it.' She turns a page. 'Mostly, things arrive thinner than this.'"],
    [C("Ask her to confirm, in writing, that the packet arrived complete against the inventory","confirm_whole",flags=["arrivalConfirmed"],hidden="Receiving county confirmed complete arrival against the inventory",note="'Mostly' is doing heavy lifting in that sentence. The confirmation makes it arithmetic."),
     C("Take her word — the important parts are clearly here","confirm_whole",note="The important parts are here. The confirmation is for the part you'll need in April, sight unseen.")]),
  N("confirm_whole",97,"School, Services, Sundays",[
    "Autumn runs on the new county's rails: Bram's school counselor writes a stability letter; Sable's teacher sends home a reading chart with stars; your services continue with a provider across the line, the referral re-sent with dates you requested in writing because the habit is now load-bearing.",
    "The Sunday dinners continue. The foster parents' countersigned log continues. The file, in its new building, grows at the same dated pace as the old one."],
    [C("Keep the rhythm: every letter filed, every log countersigned, the folder mirrored","rhythm",flags=["rhythmKept"],hidden="Documentation rhythm maintained after transfer",note="Transfers test habits. Habits, kept, become the record's accent: this family's paper sounds the same in both counties."),
     C("Relax the paperwork — the new county clearly has the picture","rhythm",note="It has the picture as of July. Courts read the whole film.")]),
  N("rhythm",150,"The Receiving Review",[
    "The new county's first full review is in October. The judge is new to your family; the file is not new to itself. She reads the amended plan's compelling-reason entry, the arrival confirmation, the school letters, the log.",
    "'This case transferred,' she says, to no one in particular. 'They don't usually arrive like this.' It is the closest thing to applause this hallway gives."],
    [C("Ask, through counsel, for the step-down the plan promised: overnights expanding to a trial return before the holidays","spring_review",req=["recordsRequested","packetBuilt","arrivalConfirmed"],note="The plan promised it in the other county's ink. Plans, unlike summaries, bind their authors."),
     C("Ask for immediate return — the file is overwhelming","end_trial130",note="Overwhelming files still end in steps. The best ending needed the plan's own words, quoted."),
     C("Let the review ride on the file without proposing the step-down","end_trial130",note="Files propose nothing. People propose; files support.")]),
  N("spring_review",330,"The Fifteenth Month, Elsewhere",[
    "Monday, April 5, 2027 — fifteen months from entry — arrives in the new county like weather in another town: noted, prepared for, unspectacular. The filing question is asked, as the statute requires it to be asked (42 U.S.C. § 675(5)(E)), and answered from the case plan the old county amended and the new county confirmed: a compelling reason, documented, that filing would not serve these children — while the trial return runs and the goal, never changed, completes itself.",
    "No one calls this a victory in the hallway. It is a non-event with a paper trail, which is what winning a clock actually looks like."],
    [C("Finish it: convert the trial return to full return at the spring review, aftercare in writing","end_whole",note="The last document of the case is the shortest: an order, two pages, both counties' ink on the story it closes."),
     C("Let the trial period simply run out without a closing order","end_trial130",note="Open files invite new summaries. Close the file the way you carried it: in writing.")]),
  N("end_whole",345,"The File Arrived Whole",[
    "The children come home for good in April, fifteen months after they left, in a different county from the one that took the case and the same family that finished it. Bram's map of the Sunday-dinner route is retired to the refrigerator, an artifact of the year the family lived in two places and the file lived in one piece.",
    "At the closing, Ms. Whitfield says the sentence you will remember longest: 'Your case was the only transfer this year that arrived with everything it left with.' It was not luck. It was an inventory, a confirmation, and a plan amended in ink before the box was taped."],
    ending=True, debrief=[
      "THE TRANSFER'S LAW — The permanency clock does not pause for geography: entry Monday, January 5, 2026; fifteen of the most recent twenty-two months arrived Monday, April 5, 2027, in whichever county then held the case (42 U.S.C. § 675(5)(E)). The compelling-reason exception exists only as documentation — a case plan that says, in so many words, why filing would not be in the child's best interest — which is why the amendment was secured in writing before the move, from the county that knew the facts.",
      "THE PAPER CHAIN — Record requested before departure (55 Pa. Code § 3130.44(d); redactions under (f)); an inventory built with counsel (42 Pa.C.S. § 6337); a dated statement filed beside an early, hardening case note; written confirmation of complete arrival. Each link is small. The chain is the strategy: a loss can only be proved — and therefore prevented — against a list.",
      "WHAT NO STRATEGY CONTROLS — The receiving county's staffing, the new judge, the scan queue. Transfers lose pages in real systems; this route's claim is that the loss, had it happened, would have been visible, dated, and curable — because someone counted the file before it traveled and after it landed."]),
  N("end_trial130",345,"Home on a Longer Leash",[
    "The children do come home — on a trial basis that stretches across the spring, with the case open in the new county until summer. Nobody lost anything except time and certainty: the two currencies transfers spend.",
    "The fifteenth month passes during the trial period, the filing question answered by the trial itself. It ends well. It ends the way cases end when the file arrives mostly whole: well, eventually, with extra hearings."],
    ending=True, debrief=[
      "A PARTIAL WIN, NAMED HONESTLY — Return home, on the system's longer schedule. What separated this ending from the best one was the chain's paperwork: the pre-move record request (**recordsRequested**), the compelling-reason packet documented in the plan (**packetBuilt**), and the written arrival confirmation (**arrivalConfirmed**) that let the new court enforce the old county's plan as written.",
      "WHAT NO STRATEGY CONTROLS — Intake stacks, staffing, and the receiving judge's caution. A file that arrives whole still gets read by a stranger; the strategy's promise is only that the stranger reads your record, not a summary of it."]),
  N("end_thin130",240,"The Thin File",[
    "In this branch the transfer happened the way it usually does: a summary traveled, the packet didn't, and the receiving county met a four-page family. The compelling reason had been agreed — verbally, in a room in another county — and agreements do not transfer.",
    "The new plan, written from the summary, does not mention an exception. The goal is questioned at the fall review; the filing conversation starts early and from the wrong end. The case is not over. But from here, the family must rebuild in a new building the record it already built once — the cruelest line item in any transfer, paid in months."],
    ending=True, debrief=[
      "WHAT WAS LOST, ITEMIZED — Not effort, not progress: paper. The record never requested before departure (55 Pa. Code § 3130.44(d)); the compelling-reason documentation never entered into the case plan, where 42 U.S.C. § 675(5)(E) requires it to live to count; the arrival never confirmed against an inventory, so the loss itself could not be proved or repaired. The debrief is the inventory, read too late.",
      "WHAT NO STRATEGY CONTROLS — County systems are separate buildings with separate habits, and the clock (entry January 5, 2026; fifteen months April 5, 2027) reports to neither. The strategy for a crossing case is chain-of-custody thinking applied to a family's own story: count it, confirm it, and never let a summary travel alone."]),
 ],
 strategy=dict(
  win_honest="This win is labeled **partial** in the data and meant honestly: the petition is never filed, the compelling reason holds across the county line, and the children complete a trial return to full return — but the case spans its full fifteen months to get there. The capstone skill it teaches is chain-of-custody for a record: inventory before, confirmation after, and the exception documented in the case plan *before* the file travels.",
  law=[
   "**The clock does not pause for geography.** Entry Monday, January 5, 2026 → fifteen of the most recent twenty-two months on Monday, April 5, 2027 (42 U.S.C. § 675(5)(E)), in whichever county holds the case. The parallel state review determination is made under 42 Pa.C.S. § 6351(f)(9).",
   "**The compelling-reason exception is a case-plan sentence or it is nothing.** Section 675(5)(E)'s exception requires the agency to have *documented* a compelling reason in the case plan. A supervisor's verbal agreement in the sending county binds no one in the receiving county; the signed amendment does.",
   "**Count the file before it travels.** The record request (55 Pa. Code § 3130.44(d)) must precede the move, because an inventory can only be built from a seen record; redactions under (f) are expected and itemized like everything else.",
   "**Counsel as logistics** (42 Pa.C.S. § 6337): the introduction and inventory go to the receiving county through the lawyer, and arrival is confirmed in writing against the inventory — the receiving caseworker's 'mostly' converted into arithmetic."],
  traps=[
   ("Assuming the counties handle the transfer between themselves at *The Transfer Problem*","summaries travel; packets get 'routinized' into four pages — the route to **The Thin File**."),
   ("Asking for the early case note to be removed at *What the Record Holds*","files don't unwrite; the dated statement filed *beside* the note is the correction that survives the trip."),
   ("Accepting 'mostly arrived' without written confirmation","the win's gate requires **arrivalConfirmed**; an unconfirmed loss discovered in April cannot be proved, and what cannot be proved cannot be cured — the route settles for the trial leash."),
   ("Relaxing the documentation rhythm in the new county","the receiving court reads the whole film, including the quiet autumn; a packet is a habit, not an event.")],
  uncontrolled="The receiving county's staffing and intake stack, the new judge's caution, and the scan queue between two buildings. The route controls the chain of custody — and in a crossing case, custody of the paper is custody of the story."),
)
