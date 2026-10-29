# -*- coding: utf-8 -*-
from lib import C, N

PAPER = lambda nxt: [C("Do the paper version: dated, copied, filed", nxt, cash=-5, flags=["paperTrail"], hidden="Dated documentation added to the case record", note="Another dated page joins the folder."),
                     C("Handle it with a conversation and move on", nxt, note="Conversations end. The file keeps what it was given.")]

# ---------------- S131 — Complex ----------------
S131 = dict(
 num=131, name="Three Files, One Family", tier="Complex",
 startDateISO="2025-11-03", startCash=200,
 summary="Two children entered care on two different dates; a third file — an indicated report against the mother — runs beside both. Three clocks, three buildings, one folder: sequence the appeal before its window closes, document the exceptions child by child, and arrive at the fifteen-month table with every file answered.",
 contentNote="This scenario depicts two siblings in placement on staggered timelines, an indicated-report appeal, and a permanency review. There is no graphic content. Players may skip any scene or use the quick exit at any time.",
 offsetNote=" (the elder child's foster-care entry date)",
 win_id="end_answered",
 nodes=[
  N("start",0,"Three Envelopes",[
    "Your name is Celeste. Teo, eleven, entered foster care on Monday, November 3, 2025, after the school called in the bruises from his bicycle crash and the story took a weekend to sort out. Cosette, eight, followed on Friday, November 21 — the second entry the file records, eighteen days later, when the first placement could not take siblings and the case widened instead of narrowing.",
    "And in December a third envelope joined the others: an indicated report, naming you, arising from the same crash — with a 90-day appeal window (23 Pa.C.S. § 6341(a)(2)) that closes Monday, March 16, 2026, counted from the December 16 notice. Three files. Three clocks. One mother. This is the marathon version of the lesson every smaller scenario taught: sequence is survival."],
    [C("Build the master calendar first: every clock, every date, one page","calendar131",flags=["calendarSet"],hidden="Master calendar of all three tracks built",note="Three clocks, one page, on the refrigerator, where fear can't blur them."),
     C("Handle each file as it comes up — you're organized enough","calendar131",note="Organized enough is the epitaph of many a deadline.")]),
  N("calendar131",4,"Ms. Onyema Draws the Board",[
    "Your lawyer, Ms. Onyema, draws the board the way the appeal scenario taught: three columns — TEO (entered Nov 3, 2025; fifteen months = Tuesday, February 3, 2027), COSETTE (entered Nov 21, 2025; fifteen months = Sunday, February 21, 2027), APPEAL (notified Dec 16, 2025; due March 16, 2026). 'Different children, different months,' she says. 'The statute counts children, not families.'",
    "Counsel is your right (42 Pa.C.S. § 6337) — and here, counsel is also cartography. 'The appeal goes first,' she says, tapping March. 'It is the only date on this board that cannot be continued.'"],
    PAPER("appeal_first")),
  N("appeal_first",9,"The Appeal, Filed in Week One",[
    "The appeal letter is the half-page the library's families know by heart: name, report number, amend or expunge, signature, date. It goes out on day 9 of 90 — not because the appeal is the most important file, but because it is the most perishable.",
    "The clerk stamps your copy. March 16 is now a date you own instead of a date that owns you."],
    [C("Mail it with the stamped copy filed, and note the Bureau's clocks on the calendar: evidence, hearing, decision","appeal_done",cash=-10,flags=["appealFiled"],hidden="Indicated-report appeal filed in writing on day 9 of 90",note="Filed first because it perishes first. Sequence is the strategy."),
     C("Draft it carefully and mail it after the January review settles your thinking","appeal_done",note="January reviews have eaten bigger windows than this one. You mailed it — day 30-plus, inside, and lucky.")]),
  N("appeal_done",16,"Two Placements, Two Logs",[
    "Teo is with a foster family near his school; Cosette is with a resource family across town, because the sibling home fell through in week two — a fact the file records in one line and the children record in every Sunday visit, which happens at a park between the two houses, weather permitting, love insisting.",
    "Sibling visits are a plan item. Plan items generate paper or they generate apologies. Your job, per Ms. Onyema: make them generate paper."],
    [C("Keep one sibling-visit log for both children, signed by both resource families","records131",flags=["siblingLog"],hidden="Sibling visit log kept and countersigned by both placements",note="One log, two signatures, two children in the same document — the file rarely sees them together. Make it."),
     C("Each home keeps its own notes — that's their job","records131",note="Their job is care. The log is yours.")]),
  N("records131",23,"Both Records, Requested",[
    "Two dependency cases means two case records, and the request that unlocks them is the same in each: the material is released upon request (55 Pa. Code § 3130.44(d)), with redactions for others' information under (f). You sign both requests in one sitting, because partial mirrors produce partial strategies.",
    "What comes back will show you each child's file as its own court will read it — including whether either file even mentions the other's clock."],
    [C("Sign both written requests; file both stamped copies in the master folder","packets_back",cash=-10,flags=["recordsRequested"],hidden="Both children's case records requested in writing under § 3130.44(d)",note="Two mirrors, requested together. The board is about to get honest."),
     C("Request Teo's now — his clock is the urgent one","packets_back",note="His is earlier by eighteen days. Cosette's is the one that will surprise you.")]),
  N("packets_back",44,"What the Two Files Say",[
    "Teo's file is orderly: services dated, visits logged, the bicycle-crash investigation summarized fairly. Cosette's file is thinner and stranger: her entry paperwork carries a wrong date — November 12, nine days before she entered care — inflating her clock by over a week, an error no one made on purpose and everyone downstream has been copying.",
    "Clocks built on copied errors are still clocks, until someone files the correction. You are someone. The correction is a page with the true date, the entry order attached, and a request that both files carry it."],
    [C("File the date correction in both children's files, entry order attached","correction_filed",cash=-5,flags=["dateCorrected"],hidden="Cosette's entry-date error corrected in writing in both files",note="Nine days, returned to an eight-year-old by a photocopy. The calendar is a moral instrument."),
     C("Mention the wrong date at the next review so the judge can note it","correction_filed",note="Judges note what is filed. What is mentioned gets noted as mentioned.")]),
  N("correction_filed",58,"The Appeal's Evidence",[
    "The Bureau's scheduling order arrives, and with it the duty the appeal rules place on the agency: provide the appellant all evidence gathered during the investigation relevant to the determination, including the potentially exculpatory, within ten days of the order (23 Pa.C.S. § 6341(c.2)(4)).",
    "The packet holds the school nurse's note from the crash day — 'spoke with Teo; states he fell from bicycle onto handlebars; bruising pattern consistent' — the sentence the indicated summary had compressed into 'injuries unexplained.' The hallway's rule holds in the third file too: the decisive page is usually already written, by someone else, waiting to be asked for."],
    [C("Build the appeal exhibit set around the nurse's note and the dated photos","services131",cash=-5,flags=["evidenceReceived"],hidden="Investigation evidence obtained under § 6341(c.2)(4)",note="Their packet, your exhibits. The burden will be theirs at the hearing (23 Pa.C.S. § 6341(c.2)(5)); the paper is already yours."),
     C("Your own account of the crash should carry the appeal","services131",note="Accounts need corroboration the way clocks need dates. The nurse wrote both.")]),
  N("services131",73,"Two Service Plans, One Mother",[
    "Your services run on two plans in two files that occasionally forget they describe the same woman: a parenting course (Teo's file), a family-therapy referral (Cosette's), and a housing application that both files cite and neither owns. The therapy referral, the record shows, was sent five weeks after Cosette's plan was signed.",
    "Gaps that live between two files belong fully to neither — which means, at the permanency table, they can be charged to you in both. The letter that prevents this is short: dates, plan, referral, in both files."],
    [C("Write the referral-gap letter once and file it in both children's cases","gap_both",cash=-5,flags=["gapDocumented"],hidden="Therapy referral gap documented in both children's files",note="One letter, two files. The gap now belongs to its true owner in both courtrooms."),
     C("Raise the gap in Teo's file — the therapy matters most there","gap_both",note="It matters in Cosette's file, where it happened. Gaps must be filed where they live.")]),
  N("gap_both",95,"The Spring Reviews",[
    "Spring reviews for both children land in the same week — a scheduling accident that functions as a rehearsal for every combined hearing to come. The judges (two of them; the files never merged) each read a file that now contains the correction, the logs, the gap letter, and the appeal's existence noted by date.",
    "Teo's judge says the sentence: 'I see the mother's other matters are being litigated in their proper forums, on time.' It is the sound of three files agreeing about you."],
    PAPER("appeal_hearing131")),
  N("appeal_hearing131",152,"The Bureau Hearing",[
    "Monday, June 8, 2026. The agency must prove by substantial evidence that the report should remain indicated (23 Pa.C.S. § 6341(c.2)(5)). Its case is the summary. Yours is the packet: the nurse's note, the dated photographs, the school counselor's statement, the crash-weekend timeline your sister signed in April.",
    "The hearing officer asks the agency's witness one question — whether the investigation file contained the nurse's note when the summary was written. The answer is in the transcript forever now: yes."],
    [C("Close on the burden and the note: their standard, their file, their omission","decision131",note="Short closings win paper cases. This one was written by a school nurse in November."),
     C("Close on the children's year and what the registry would cost them all","decision131",note="True, moving, and not the standard. The officer must apply the standard.")]),
  N("decision131",188,"Expunged, and What It Doesn't Do",[
    "The decision — entered within the 45 days the statute allows (23 Pa.C.S. § 6341(c.3)) — amends the report to unfounded. You read it twice at the kitchen table, and Ms. Onyema's voice is in your ear from November: 'Winning the third file does not win the first two. It clears the air they breathe.'",
    "She is right. Teo's clock still reads February 2027; Cosette's, February 2027 (corrected). The dependency cases do not care about the registry — except that every future reader of either file will now meet a mother whose indicated report was examined and expunged, instead of assumed."],
    [C("File the expungement order in both dependency files, with a cover page noting the date","kinship131",flags=["expungementFiled"],hidden="Expungement order filed in both dependency cases",note="Paper does not walk between buildings. You are the corridor."),
     C("The dependency courts will hear about it through the agency","kinship131",note="They will hear a summary of it. Summaries are how good news goes to be diminished.")]),
  N("kinship131",214,"Aunt Selene's Application",[
    "Autumn brings the kinship door: your aunt Selene, retired from the school district, applies to take both children together — the sibling placement that fell through last November, now with a study, a spare house, and a year of Sunday visits to point to. Kinship care, if it comes, is also one of the permanency clock's own exceptions: a child being cared for by a relative is outside the filing duty (42 U.S.C. § 675(5)(E)).",
    "The study needs the usual constellation: clearances, references, the home visit, dates. You know the choreography by now. So does Selene, who has started a folder of her own — the family resemblance is administrative."],
    [C("Support the study with the sibling log and a written request that both files note it","study131",cash=-5,flags=["kinAsked"],hidden="Kinship study supported with the sibling log; request noted in both files",note="The log does double duty: it proves the bond the placement would protect."),
     C("Let the study proceed without your fingerprints on it","study131",note="Support visible in the file reads as a family organizing itself. Absence reads as absence.")]),
  N("study131",246,"The Study and the Services",[
    "The study proceeds; your services complete in their two files: course certificate (filed, Teo), therapy goals met (filed, Cosette — with the gap letter explaining the plan's arithmetic to any reader who wonders why it took until fall).",
    "Housing remains the board's last open square: your application, filed in spring, reaches its letter in November — a dated waitlist position with a projected February opening, on letterhead, in both files now."],
    [C("Assemble the exception packets child by child: Teo's and Cosette's, each with its own dates","packets131",cash=-10,flags=["packetBuilt"],hidden="Per-child exception packets assembled with individual dates",note="Two packets, two clocks, no blended arithmetic. The statute counts children; so do you."),
     C("Build one family packet — the story is the same","packets131",note="The story rhymes; the dates don't. Blended packets are where child-specific exceptions go to blur.")]),
  N("packets131",290,"The Winter Push",[
    "Winter is the long middle of every marathon case: visits expand at both placements, overnights begin at Selene's newly approved home — both children, together, the study approved in December with the court's blessing noted in both files (a relative placement, documented) — and your overnights at your own apartment begin in January, with the February unit letter framed like art.",
    "The fifteen-month dates now approach in their corrected forms: Teo, Tuesday, February 3, 2027; Cosette, Sunday, February 21, 2027. Behind each date stands a packet, a plan entry, and a relative's approved home. The clocks will ask their question. The files are ready to answer in triplicate."],
    PAPER("review131")),
  N("review131",330,"The Review Where the Dates Are Said",[
    "January's combined review — the two judges have begun, sensibly, to sit in sequence on the same morning — hears the state of all three files: the appeal, closed and expunged; the placements, united at Selene's; the services, complete with their gaps documented and owned by their true dates.",
    "The agency's counsel states the permanency position carefully: the February dates will be met, as the statute contemplates, by the documented exceptions — relative care for both children, and the compelling reason written into each case plan this month at your lawyer's request: reunification on track, trial return scheduled, filing not in either child's interest (42 U.S.C. § 675(5)(E))."],
    [C("Ask both courts to write it: exceptions documented, trial return to begin, goal unchanged in both files","february131",req=["recordsRequested","appealFiled","packetBuilt","dateCorrected"],note="Asked in both rooms, answered in both orders. The board is fully lit."),
     C("Ask for immediate return of both children — everything is documented","end_trial131",note="Everything is documented except the last step, which is a step. The best ending takes it in order."),
     C("Let the agency's statement stand without asking for orders","end_trial131",note="Statements evaporate. Orders accumulate.")]),
  N("february131",457,"February, Twice",[
    "Tuesday, February 3, 2027 — Teo's fifteenth month — passes the way prepared-for dates do: as a review already held, an exception already documented, a trial return already running. Sunday, February 21 — Cosette's, on her corrected clock — passes the same way, eighteen days later, the echo arriving exactly when the master calendar always said it would.",
    "No petition is filed in either case. The question the statute asks at fifteen months was answered in January, in writing, child by child. This is what the finish line of a marathon case looks like: not a tape, but a table — three files, all answered, and a trial return converting to a return while the folder, at last, gets lighter instead of heavier."],
    [C("Convert the trial return at the spring review, both children, aftercare in writing in both files","end_answered",note="The last move is the first lesson, twice: in writing, in both files."),
     C("Let the trial simply run its course","end_trial131",note="Open files collect new summaries. Close them the way you carried them.")]),
  N("end_answered",470,"Every Clock Answered",[
    "By spring both children are home — returned on orders written in two courtrooms, built on one folder. Selene's home stays in the orders as the family's standing respite, the kinship door held open by the same paperwork that opened it. The registry holds nothing against you; the Bureau saw to that in a decision your grandchildren could read.",
    "State it honestly, the way the debriefs insist: the children spent fifteen months in care, and no strategy gives those months back. What the strategy did was narrower and total: no clock in any of the three files ever found this family unprepared, undocumented, or late. In a marathon case, that is not a consolation. That is the win."],
    ending=True, debrief=[
      "THE THREE CLOCKS, AUDITED — Appeal: notified December 16, 2025; 90 days → Monday, March 16, 2026; filed day 9 (23 Pa.C.S. § 6341(a)(2)); evidence under (c.2)(4); burden on the agency under (c.2)(5); decision within (c.3)'s 45 days. Teo: entered November 3, 2025 + 15 months = Tuesday, February 3, 2027. Cosette: entered November 21, 2025 (her file's copied November 12 was corrected on the record) + 15 months = Sunday, February 21, 2027. The filing duty and its exceptions — relative care, documented compelling reason, services not provided (42 U.S.C. § 675(5)(E)) — are counted per child, which is why the packets were built per child.",
      "WHY THIS IS LABELED PARTIAL — The best ending this scenario offers keeps the goal intact, defeats every clock, and returns both children — after fifteen months of placement. A strategy guide that called that unqualified victory would be lying about the cost. The win is real: it is the best possible outcome the documented situations allow, and it was reached by sequencing — perishable deadline first, mirrors second, corrections and packets child by child, orders asked for in both rooms.",
      "WHAT NO STRATEGY CONTROLS — Two judges, a hearing officer, a study queue, a housing waitlist, and a bicycle. The route controlled the order of the paper and the accuracy of the dates — in a three-file case, the two things most likely to be lost and the two things that decide it. Counsel (42 Pa.C.S. § 6337) and the record requests (55 Pa. Code § 3130.44(d)) are the load-bearing walls; everything else is the family, living its year in date order."]),
  N("end_trial131",470,"Home in Stages, Both Files Open",[
    "The children come home in stages across the spring — Teo first, on his earlier clock's order; Cosette on a trial that stretches toward summer — with both cases still open, both folders still growing, and the fifteenth months survived but not, as in the best ending, answered in advance.",
    "Nothing failed here. The exceptions held, the appeal is expunged, the goal never moved. The difference is the texture of the ending: orders asked for late produce returns that arrive late, in a system where late is measured in childhoods."],
    ending=True, debrief=[
      "A PARTIAL WIN, SLOWER THAN THE BEST — The same facts, the same clocks, a later set of asks. The gated route required **recordsRequested**, **appealFiled**, **packetBuilt**, and **dateCorrected** — the correction alone was worth nine days of a child's clock, and it existed only because both records were requested and read.",
      "WHAT NO STRATEGY CONTROLS — Judicial sequencing across two courtrooms. Two files can be won in the same season and still close in different months; the strategy's claim is that neither was ever lost to a date."]),
  N("end_one_clock",470,"The Clock That Got Away",[
    "In this branch the appeal was polished instead of filed, or Cosette's date was never corrected, or one file's packet was left to a summary — and the board's discipline is shown by its absence: one of the three clocks, the one nobody was watching that month, ran out.",
    "A petition in one child's case, or a registry entry that outlives both dependency files: the marathon's cruelty is arithmetic. Attention divided by three files is still attention, but the clocks do not divide at all."],
    ending=True, debrief=[
      "THE MARATHON'S LESSON — Every deadline in this scenario was computed from primary dates: the 90-day appeal window (23 Pa.C.S. § 6341(a)(2)), and per-child fifteen-month dates under 42 U.S.C. § 675(5)(E). The failures that produce this ending are never effort failures. They are sequencing failures — the perishable filed late, the copied error uncorrected, the second child's packet blended into the first's.",
      "WHAT NO STRATEGY CONTROLS — Very little, in this ending, was outside the strategy: that is what makes it the cautionary one. The board on the refrigerator — every clock, every date, one page — is the whole defense. Keep the board."]),
  N("end_split131",380,"Two Files Won, One Still Running",[
    "This branch ends mid-marathon: the appeal expunged, one child home, the other's case converted to a longer plan after a goal the court questioned in the fall and the file answered too late.",
    "It is the most common shape of real multi-file cases — not triumph, not disaster, but a split decision measured in different bedtimes in different houses. The folder remains open on the kitchen table, because one file is still running, and it will be run the same way: in date order, to the end."],
    ending=True, debrief=[
      "A SPLIT, NAMED HONESTLY — Multi-file cases rarely resolve in a single hearing, and this ending refuses to pretend otherwise. The tracks that were won were won on the library's constants: early appeal (§ 6341(a)(2)), evidence under (c.2)(4), records under § 3130.44(d), per-child exceptions under § 675(5)(E).",
      "WHAT NO STRATEGY CONTROLS — Courts sequence siblings by their own calendars, and a goal questioned in the fall can take a season to answer even with the right paper. The split is not the strategy failing; it is the strategy still running, one file short of the table."]),
 ],
 strategy=dict(
  win_honest="This is a **partial** win, labeled so in the guide because honesty is the house rule: every clock is answered, the appeal is expunged, both children come home — after fifteen months in care. No route in this scenario returns the months; the best route ensures no month was lost to a missed date, a copied error, or a blended packet. That is the best possible outcome the situation allows, and the guide says so.",
  law=[
   "**Per-child arithmetic.** ASFA's filing duty counts each child's months in care (42 U.S.C. § 675(5)(E)): Teo, entered November 3, 2025 → fifteen months Tuesday, February 3, 2027; Cosette, entered November 21, 2025 → Sunday, February 21, 2027. The scenario's planted trap — her file's copied November 12 entry date — is worth nine days and is curable only by a written correction filed in both cases.",
   "**Sequencing is doctrine.** The appeal is the only perishable item on the board: notified December 16, 2025, the 90-day window (23 Pa.C.S. § 6341(a)(2)) closed Monday, March 16, 2026. It is filed on day 9, before the marathon's middle can eat the calendar.",
   "**The appeal's machinery, reused at capstone weight:** evidence including the exculpatory under § 6341(c.2)(4); the agency's burden by substantial evidence under (c.2)(5); the decision inside (c.3)'s 45 days. The expungement order is then carried — physically, by the parent — into both dependency files.",
   "**Exceptions are documented per child:** relative care (Selene's approved study) and the case-plan compelling reason, written into each plan (42 U.S.C. § 675(5)(E)). Mirrors for both cases: § 3130.44(d) requests, redactions under (f); counsel as cartographer (42 Pa.C.S. § 6337)."],
  traps=[
   ("Building one blended family packet at *Assemble the Exception Packets*","the statute counts children, not families — blended arithmetic blurs exactly the dates each exception stands on."),
   ("Mentioning Cosette's wrong entry date at a review instead of filing the correction","mentions are minuted; corrections are filed. Nine days of a child's clock ride on the difference — and the win's gate requires **dateCorrected**."),
   ("Filing the appeal after the January review 'settles your thinking'","the window closes March 16 whether or not your thinking is settled; the late branch is the road to **The Clock That Got Away**."),
   ("Letting the agency's January statement stand without asking for orders in both rooms","statements evaporate in two courtrooms at once; the route settles for **Home in Stages**.")],
  uncontrolled="Two judges, a hearing officer, a kinship study queue, a housing waitlist, and a loose bicycle rail. The route controls sequence, accuracy, and paper — the three things a three-file case most reliably loses."),
)

# ---------------- S132 — Complex ----------------
S132 = dict(
 num=132, name="The Hearing That Read the Year", tier="Complex",
 startDateISO="2025-08-04", startCash=190,
 summary="Fourteen months of record-building converge on a single permanency hearing: a father whose daughter entered care as a toddler asks the court to do in one morning what the file has been saying for a year. Every earlier scenario's skill appears exactly once — and the hearing uses all of them.",
 contentNote="This scenario depicts a long-running dependency case culminating in a permanency hearing. There is no graphic content. Players may skip any scene or use the quick exit at any time.",
 offsetNote=" (the child's foster-care entry date)",
 win_id="end_home132",
 nodes=[
  N("start",0,"Month Fourteen, Minus One",[
    "Your name is Jerome. Your daughter Willa, five, entered foster care on Monday, August 4, 2025, when you were hospitalized after the accident at the warehouse and there was, for one weekend, no adult standing between her and the system's default answer. You stood up again by Friday. The case, once opened, did not close on the same schedule.",
    "Now it is month thirteen, and the court has set the hearing that the whole case has been walking toward: the permanency hearing of Monday, September 14, 2026 — just past Willa's thirteen-month mark, with her fifteenth month (Wednesday, November 4, 2026) visible on the horizon like weather. Your lawyer, Mr. Baptiste, puts it plainly: 'Hearings like this are not won at the hearing. They are read there. We have one month to finish the book.'"],
    [C("Treat the month as a production schedule: every document, dated, filed, indexed","production",flags=["productionSet"],hidden="Hearing production schedule set with counsel",note="A hearing is a reading. You are finishing the book it will read."),
     C("Prepare to testify well — this is finally your day in court","production",note="It is your day. The court will spend most of it reading. Feed the reading.")]),
  N("production",5,"The Inventory of a Year",[
    "The inventory of the year's paper, spread on Mr. Baptiste's table: the visit logs (fifty-one weeks, two signatures), the treatment completion letter, the employer's accommodation schedule, the pediatrician's paragraph, the housing file, the record you requested last winter under 55 Pa. Code § 3130.44(d), your written responses to the two referral gaps, the kinship study of Willa's aunt — approved, then held as the family's reserve.",
    "And the gaps in the inventory, listed as honestly: one missing month of visit notes (the supervisor's rotation), and the exception question nobody has yet made the agency answer in writing."],
    [C("List the gaps as tasks with owners and dates, not as worries","gap_tasks",flags=["gapList"],hidden="Hearing inventory built; gaps listed as dated tasks",note="Worries pace. Tasks get done."),
     C("The record is strong — don't let the perfect audit the good","gap_tasks",note="The audit is the good, at capstone weight. One missing month is a door the other side will open.")]),
  N("gap_tasks",10,"The Missing Month",[
    "The missing visit notes belong to October 2025, when the visit supervisor rotated and the new one's notes were 'to be uploaded.' The visits happened — Willa's foster mother, Ms. Grey, kept her own calendar, as the careful ones do, with your arrivals in her handwriting.",
    "A fact that happened and a fact the file can show are cousins, not twins. The cure for a gap in one file is a document from another: Ms. Grey's calendar, copied, signed, and filed with a one-page explanation."],
    [C("Ask Ms. Grey for the calendar pages and file them with the explanation","grey_calendar",cash=-5,flags=["gapCured"],hidden="Missing visit month cured from the foster caregiver's own calendar",note="Another chair's record, rescuing yours. Files are ecosystems."),
     C("Skip October — one month in fourteen can't decide a hearing","grey_calendar",note="One month is exactly the size of the question the agency will ask: 'What happened in October?' Answer it with paper or with weather.")]),
  N("grey_calendar",15,"The Exception Question, In Writing",[
    "Mr. Baptiste drafts the letter the year has been pointing at: a short request that the agency state, in writing, its position on the fifteen-month question — whether it will file, and if not, which exception it will document: relative care, a case-plan compelling reason, or services identified but not provided (42 U.S.C. § 675(5)(E)).",
    "Agencies answer letters like this slowly and sometimes not at all. Both responses are evidence. A documented silence, at a hearing, is a exhibit with a date on it."],
    [C("Send it by a method that proves delivery, and calendar the silence","exception_letter",cash=-5,flags=["exceptionAsked"],hidden="Agency asked in writing to state its fifteen-month exception position",note="The letter asks the question the hearing will ask. Their answer, or its absence, joins the book."),
     C("Save the question for cross-examination — surprise has value","exception_letter",note="Surprise has value in trials. In permanency hearings, foreshadowed questions with unanswered letters have more.")]),
  N("exception_letter",24,"The Record, Refreshed",[
    "The case record has grown since winter; you request the updated record in writing (55 Pa. Code § 3130.44(d)), because arguing from a nine-month-old mirror at a fourteen-month hearing is how parents get surprised by their own files.",
    "The refresh arrives with the redactions the rule provides (55 Pa. Code § 3130.44(f)) and one new page: the agency's internal note that your exception letter was 'received and under review.' Under review is the system's favorite tense. It is also, now, a dated fact."],
    [C("Index the refresh into the packet and note the exception letter's status by date","refresh_indexed",flags=["recordRefreshed"],hidden="Updated case record requested and indexed before the hearing",note="The book, current edition. The hearing will read nothing older than your preparation."),
     C("The winter record plus your folder is enough","refresh_indexed",note="Enough is a number the other side gets to test. Refresh the mirror.")]),
  N("refresh_indexed",31,"Willa's School Page",[
    "Willa started kindergarten in August, at the school two streets from your apartment — the placement's geography having accidentally served the reunification plan. Her teacher's letter is the file's newest voice: attendance, adjustment, 'asks for her dad at pickup-story time, in the tone of a child expecting him.'",
    "Collect the voices with no stake. They are the chorus the hearing trusts most, because they wanted nothing from the case except a child educated."],
    [C("File the teacher's letter and the attendance record","chorus",flags=["schoolFiled"],hidden="Kindergarten teacher's letter and attendance filed",note="The chorus gains its youngest-voiced member. Filed, not mentioned."),
     C("The teacher's letter can be mentioned in testimony","chorus",note="Mentioned letters are rumors with good reputations. File it.")]),
  N("chorus",38,"The Aunt's Standing Offer",[
    "Willa's aunt Renata — the approved kinship reserve — writes her own one-page letter: the study is current, the room is ready, and if the court wants a bridge instead of a verdict, her door is the bridge. It is an offer with a date on it, which makes it a document the court can use in either direction.",
    "Mr. Baptiste files it under both tabs: as the relative-care answer if the clock is pressed, and as the family's own safety net if she comes home. Paper that argues two ways, honestly, is the strongest kind."],
    [C("File Renata's letter in the packet under both tabs","packet132",flags=["kinLetter"],hidden="Kinship caregiver's standing offer filed",note="A bridge, documented, that the court can use without building one at the hearing."),
     C("Hold the letter — it might read as doubt about return","packet132",note="Courts read standing kin as strength. Doubt is what undocumented families radiate.")]),
  N("packet132",45,"The Packet's First Page",[
    "The packet's first page is its summary — one page, drafted by Mr. Baptiste, signed by you: the year in nine sentences, each with a date, each pointing to a tab. Hearings read first pages the way rivers read banks: everything after is steered by them.",
    "You read it at the kitchen table at midnight. It is accurate, which grieves you a little: nine sentences for a year of Tuesdays. Then you remember the alternative — nine adjectives — and sign it."],
    [C("Sign it and file the packet two weeks before the hearing","filed_early",cash=-10,flags=["packetBuilt"],hidden="Hearing packet assembled and signed",note="Filed early, read early. The book is finished; the reading can begin."),
     C("File it the Friday before — fresher","filed_early",note="Filings don't ripen. They just arrive late to the judge's weekend reading.")]),
  N("filed_early",52,"The Agency Answers, Partly",[
    "Three days after your packet lands, the agency files its position: it will not seek a goal change, it takes no position on return 'at this time,' and — in the paragraph your letter forced into existence — it confirms the exception letter is under review and notes your 'substantial documented progress.'",
    "No position is a position, when the file's weight is all on one side. Mr. Baptiste smiles like a man reading weather he ordered: 'They have read the book. Now the court reads it aloud.'"],
    [C("Prepare your testimony to match the packet, page for page — nothing new, nothing contradicted","testimony_prep",flags=["testimonyReady"],hidden="Testimony prepared against the filed packet",note="The witness and the book, in agreement. Cross-examination hates agreement."),
     C("Prepare to finally tell the whole story, beyond the packet","testimony_prep",note="The whole story is how witnesses contradict their own exhibits. Tell the packet's story, in your voice.")]),
  N("testimony_prep",59,"The Night Before the Reading",[
    "Willa, told that tomorrow is 'the talking day,' has packed her own folder: drawings, in date order she insists are correct, of the apartment, the school, the park, and a house with three figures she declines to label. Ms. Grey will bring her to the courthouse playroom in the morning.",
    "Your folder is heavier and less honest about its feelings. Both folders are ready. Sleep is the last document either of you can file."],
    [C("Sleep. The book is written; tomorrow it is read.","hearing132",note="The library's oldest instruction, at its highest stakes.")]),
  N("hearing132",63,"The Hearing That Read the Year",[
    "Monday, September 14, 2026. The courtroom does what courtrooms do with complete records: it moves without friction. The agency's counsel, facing a packet she has read and a position she has filed, does not manufacture a contest the file won't support. The judge works the tabs — visits, treatment, the cured October, the exception letter and its dated silence, the teacher's page, Renata's standing offer.",
    "'Mr. Baptiste,' the judge says, 'your client seems to have conducted this case as if the record were the client.' It is not quite a compliment. It is better: it is a finding, forming. The question she puts to you is the question the year built: 'What does Willa come home to, and who stands behind it?' Your testimony, prepared against the packet, answers in the packet's own dates."],
    [C("Ask for the order: return home today, aftercare and Renata's respite in writing, case to close at the winter review","end_home132",req=["recordsRequested","packetBuilt","gapCured","exceptionAsked"],note="Today. The word fourteen months of Tuesdays were for."),
     C("Ask for return with a ninety-day trial first, to be safe","end_trial132",note="Safe is a slower word for the same address. The file argued for today."),
     C("Let the judge craft the order without proposing one","end_trial132",note="Unproposed orders arrive wearing the court's caution. Propose the one the book supports.")]),
  N("end_home132",70,"Home From the Hearing",[
    "Willa comes home from the hearing — not from a later visit, not after a transition plan, but in your car, that afternoon, with her folder of drawings on her lap and Ms. Grey waving from the courthouse steps with the complicated smile of a woman whose year of Tuesdays mattered and is over.",
    "The order is four pages: return, aftercare in writing, Renata's respite named, closure set for the winter review. Behind it, doing the work orders cannot do, is the book: a year of paper that left the court nothing to guess. State the win plainly, because it is one: sometimes — when the record is complete, the gaps are cured, and the questions were asked in writing in time — the hearing reads the year, and the year says home."],
    ending=True, debrief=[
      "THE HEARING'S LAW — The permanency framework asks, at fifteen of the most recent twenty-two months, whether the filing duty is triggered and whether an exception is documented (42 U.S.C. § 675(5)(E); the state review determination under 42 Pa.C.S. § 6351(f)(9) — entry August 4, 2025; fifteen months Wednesday, November 4, 2026). This route never lets the question ripen: the agency was asked in writing to state its exception position a month before the hearing, and its non-answer is itself part of the record the court read. Counsel (42 Pa.C.S. § 6337) built the book; the record requests (55 Pa. Code § 3130.44(d)) supplied its contents; the redactions under (f) were treated as rules, not obstacles.",
      "WHY THIS ENDING IS FULL — Willa comes home from the hearing itself. The scenario is the library's proof case for its own doctrine: a complete record — visits counted, gap cured from another chair's calendar, exceptions asked about in writing, chorus filed, packet early — can convert a permanency hearing from a contest into a reading. It does not claim hearings are usually like this. It claims the difference, when they are, is paper.",
      "WHAT NO STRATEGY CONTROLS — The judge, the agency's litigation posture, and the accident that started it all. A different courtroom can read the same book more slowly (see the trial ending). The strategy's claim is only that nothing the court needed was missing, contradicted, or late — and that claim, this time, was enough."]),
  N("end_trial132",70,"Home on the Court's Schedule",[
    "The court orders a ninety-day trial return — Willa home that week, the case open until winter, the file technically unfinished. It is the same address as the best ending, reached by the court's road instead of yours: the book persuaded, but the proposal it ratified was caution's.",
    "Ninety days of documented mornings later, the case closes without ceremony. The book's last page is an order you did not draft, saying almost what you asked, three months after you asked it."],
    ending=True, debrief=[
      "A PARTIAL WIN, NAMED HONESTLY — Home, on the court's schedule. The gated route required **recordsRequested**, **packetBuilt**, **gapCured**, and **exceptionAsked** together: the refreshed mirror, the early packet, the cured October, and the exception question put in writing in time for its silence to testify.",
      "WHAT NO STRATEGY CONTROLS — Judicial caution, which no packet abolishes. The trial period is the court hedging against its own reading; the book's work is to make the hedge short and the closing certain."]),
  N("end_contested132",70,"The Contested Reading",[
    "In this branch the hearing becomes what hearings become when the book has holes: October is a cross-examination, the exception question is asked for the first time aloud, and the agency — surprised into advocacy — asks for time to answer both.",
    "Time is granted, because unanswered questions are the one exhibit courts always admit. The case continues into the fifteenth month with the filing question now open and the goal under weather. Nothing is lost forever. Everything is later, which in a five-year-old's calendar is its own kind of loss."],
    ending=True, debrief=[
      "WHAT THE HOLES COST — An uncured month invites the inference it might have answered; an unasked exception question leaves 42 U.S.C. § 675(5)(E) to be litigated cold at the worst moment. The route's devices were all cheap: a calendar from the foster mother's drawer, a letter with proof of delivery, a refreshed record (55 Pa. Code § 3130.44(d)). Hearings do not punish parents; they punish gaps, impersonally and completely.",
      "WHAT NO STRATEGY CONTROLS — Even holed, this record might have persuaded a different judge. The scenario's narrower claim: holes are choices, made months earlier, at kitchen tables — and at capstone weight, the hearing is merely where they are read aloud."]),
  N("end_clock132",92,"November 4",[
    "Wednesday, November 4, 2026 — the fifteenth month — arrives in the branch where the hearing was continued and the packet never quite closed. The filing question is now the case. The exceptions exist, as they always did, in the statute's text (42 U.S.C. § 675(5)(E)); the question the winter will litigate is whether they exist in the case plan, in writing, in time.",
    "Willa asks her foster mother why the talking day keeps moving. There is no answer in the file. That is the answer, and it is the one this ending exists to prevent."],
    ending=True, debrief=[
      "THE CLOCK, ARRIVED — Entry Monday, August 4, 2025 + 15 months = Wednesday, November 4, 2026. The filing duty and its three exceptions (42 U.S.C. § 675(5)(E)) become the whole litigation. The services-not-provided exception and the compelling-reason documentation were this family's true story all year; unwritten, they are arguments. Written, they would have been findings.",
      "WHAT NO STRATEGY CONTROLS — Continuances, crowded dockets, and one judge's calendar can strand even a strong case at the clock. The strategy's defense was to finish the book a month early — the one schedule in the case the parent controlled outright."]),
 ],
 strategy=dict(
  win_honest="This is a **full** win — Willa home from the hearing itself — and the library's proof case for its own doctrine. It is labeled full because the outcome is complete (return ordered at the hearing, case set to close at winter review) and because the scenario exists to demonstrate the ceiling of the paper strategy when every discipline is executed without a miss for fourteen months.",
  law=[
   "**The fifteen-month question, asked early.** Entry August 4, 2025 → fifteen months Wednesday, November 4, 2026 (42 U.S.C. § 675(5)(E); review determination under 42 Pa.C.S. § 6351(f)(9)). The route's signature move is putting the exception question to the agency *in writing, a month before the hearing* — their answer documents an exception; their silence documents that the question was asked and the progress was, in their own later filing, 'substantial and documented.'",
   "**Gaps are cured from other chairs' paper.** The missing visit month is repaired not by testimony but by the foster caregiver's own calendar — the file as ecosystem. A hearing cross-examines absences; it cannot cross-examine a countersigned calendar.",
   "**The mirror, refreshed.** An updated record request (55 Pa. Code § 3130.44(d)) before the hearing prevents arguing from a nine-month-old file; redactions under (f) are indexed as rules, not treated as concealment.",
   "**Counsel as editor-in-chief** (42 Pa.C.S. § 6337): the packet's first page — nine dated sentences — is the hearing's steering document, and testimony is prepared *against* the packet so the witness and the book never contradict each other in the room."],
  traps=[
   ("Skipping the missing month — 'one month in fourteen can't decide a hearing'","one month is precisely the cross-examination's size. The win's gate requires **gapCured**; uncured, the hearing becomes **The Contested Reading**."),
   ("Saving the exception question for cross-examination","surprise is a trial tactic; in a permanency hearing, the unanswered letter is worth more than the ambush — its dated silence is an exhibit."),
   ("Preparing testimony beyond the packet","witnesses who outrun their exhibits contradict them; the packet's story, in the parent's voice, is the whole performance."),
   ("Filing the packet the Friday before","judges read on weekends. The early filing is why the agency's response conceded the ground before the hearing began.")],
  uncontrolled="The judge's temperament, the agency's choice to contest or concede, and the original accident. The route controls the book — completeness, currency, and the questions asked in writing in time. This scenario is the argument that, at the ceiling, the book is enough."),
)

# ---------------- S133 — Complex ----------------
S133 = dict(
 num=133, name="The Three-Chair Table", tier="Complex",
 startDateISO="2026-01-12", startCash=185,
 summary="A grandmother approved as kinship caregiver, a mother in services, and an indicated-report appeal — three chairs at one table, three different legal postures, one boy. The win requires all three chairs to pull at once: the grandmother's study, the mother's record, and the appeal filed before its window closes.",
 contentNote="This scenario depicts a kinship placement with a grandmother, a parent's services, and an indicated-report appeal. There is no graphic content. Players may skip any scene or use the quick exit at any time.",
 offsetNote=" (the child's foster-care entry date)",
 win_id="end_three_chairs",
 nodes=[
  N("start",0,"Three Chairs",[
    "Your name is Rosa. Your son Matteo, ten, entered care on Monday, January 12, 2026, after the night the police came to your building for someone else's emergency and found yours: Matteo home alone for forty minutes while you ran to the pharmacy in a snow emergency the file describes in the flat voice it uses for everything.",
    "He is with his grandmother — your mother — Sabine, whose spare room he has claimed with a completeness only ten-year-olds achieve. And a third chair stands at the table: an indicated report naming you, notice dated Friday, January 30, 2026, with the 90-day window (23 Pa.C.S. § 6341(a)(2)) closing Thursday, April 30, 2026. Three chairs: the kinship study, your services, the appeal. Pull one and the others move. Ignore one and the table tips."],
    [C("Draw the table: three chairs, three clocks, one page — before anything else moves","table133",flags=["tableDrawn"],hidden="Three-track table drawn with all clocks",note="The table, drawn. Now it can be worked."),
     C("Take the files as they come — there's a limit to planning","table133",note="There is also a limit to memory, and April 30 is past it.")]),
  N("table133",4,"Ms. Whitaker Assigns the Chairs",[
    "Your lawyer, Ms. Whitaker, assigns each chair its worker: the kinship worker owns Sabine's study; the caseworker owns your services; the Bureau owns the appeal — and you, she says, own the calendar that connects them. Counsel is your right (42 Pa.C.S. § 6337); coordination, in a three-chair case, is your job description.",
    "'The study and the services are marathons,' she says. 'The appeal is a sprint with a wall at the end of it. Sprint first.'"],
    PAPER("appeal133")),
  N("appeal133",8,"The Sprint, Run Early",[
    "The appeal letter goes out on day 8 of 90, stamped copy filed, deadline retired. It is the same half-page as always — name, report number, amend or expunge — and it feels, as always, too small for its consequences.",
    "Sabine watches you mail it and says the thing grandmothers say in this library: 'Paper first. Feelings on schedule.' She has started a folder. Of course she has."],
    [C("Mail it and log the Bureau's future clocks on the table page","sprint_done",cash=-10,flags=["appealFiled"],hidden="Indicated-report appeal filed in writing on day 8 of 90",note="The wall is behind you now. The marathons remain, at marathon pace."),
     C("Give the letter one more week of thought — first impressions matter","sprint_done",note="It went out on day 15, inside the window and unimproved. The wall does not grade drafts.")]),
  N("sprint_done",14,"Sabine's Study, Itemized",[
    "The kinship study's list is the familiar constellation: clearances for every adult in the house, references, the home visit, the training module, Matteo's room. Sabine's house passes inspection the way her kitchen passes holidays: completely, with documentation.",
    "One item snags: a clearance for your brother, who stays over 'sometimes' — sometimes being a word studies do not accept. He gets the form, or the couch gets a rule. The study must be able to say which, in writing."],
    [C("Itemize the study in writing with the kinship worker, item by item, dates attached","study_items",cash=-5,flags=["studyList"],hidden="Kinship study itemized in writing with dates",note="A checklist instead of a cloud. The brother question gets a written answer."),
     C("Let the study find its own pace — Sabine's house speaks for itself","study_items",note="Her house does. Studies speak paper, and the sometimes-couch is exactly what they speak about.")]),
  N("study_items",21,"Your Services, On the Second Chair",[
    "Your plan: a parenting course, a safety-planning series, and the overnight-work problem — you clean offices at night, which is how the forty minutes happened. The plan's answer is a documented coverage roster: Sabine, your sister, the neighbor with the signed letter, a phone tree on paper.",
    "Coverage rosters are the plan's least believed document when they are verbal and its most believed when three signatures deep. Collect the signatures like the plan's life depends on them, because at the review, it will."],
    [C("Build the roster on paper: three names, three signatures, filed with the plan","roster",cash=-5,flags=["rosterSigned"],hidden="Childcare coverage roster signed and filed with the service plan",note="Three signatures deep. The forty minutes now have a documented answer."),
     C("The roster is real — your family knows the arrangement","roster",note="Real and undocumented is the plan's saddest genre. Sign it.")]),
  N("roster",29,"The Record, Requested for the Whole Table",[
    "You request the case record in writing (55 Pa. Code § 3130.44(d)) — and, because the study is a file too, Sabine requests what she may of her own study record, so both marathons run with mirrors. Redactions under (f) black out the neighbors' names, as the rule provides.",
    "The packet shows the investigation's account of the pharmacy night — and the ER's timestamped receipt you gave the investigator, placing the round trip at thirty-eight minutes. The indicated summary says 'extended period.' Receipts say thirty-eight minutes. Both are now in the appeal's future."],
    [C("File the receipt and a one-page timeline in both the case record and the appeal packet","receipt_filed",cash=-5,flags=["recordsRequested"],hidden="Case record requested under § 3130.44(d); pharmacy receipt and timeline filed in both tracks",note="Thirty-eight minutes, timestamped, in both files. Adjectives lose to receipts."),
     C("Keep the receipt for the appeal hearing — it's the best surprise","receipt_filed",note="Surprises are for birthdays. Filed receipts are for hearings — in both tracks.")]),
  N("receipt_filed",43,"The Appeal's Evidence Packet",[
    "The scheduling order triggers the agency's duty: all evidence gathered in the investigation relevant to the determination, including the potentially exculpatory, within ten days (23 Pa.C.S. § 6341(c.2)(4)). Their packet includes the building's incident report — which records that the police entry, the reason anyone was in your home at all, concerned the unit across the hall.",
    "Context is not an excuse; it is worse for the agency than an excuse. It is the file admitting the investigation began inside someone else's emergency and summarized yours from the doorway."],
    [C("Build the appeal exhibits: receipt, timeline, incident report, the neighbor's signed statement","exhibits133",cash=-5,flags=["evidenceReceived"],hidden="Appeal evidence obtained under § 6341(c.2)(4) and indexed",note="The doorway summary, answered by documents from inside the apartment."),
     C("Argue the context yourself at the hearing — you lived it","exhibits133",note="You did. The incident report lived it too, in writing, without cross-examination.")]),
  N("exhibits133",57,"The Study's Last Item",[
    "The study's last item is the training module, which Sabine completes with the air of a woman defusing a formality — and one question the trainer flags kindly: Sabine's plan for the nights you work, when Matteo stays with her, needs to be written into the study as the standing arrangement it already is.",
    "The kinship worker adds the page. The study, in its final form, describes the family as it actually functions — the description being, in the end, what studies are for."],
    [C("Get the standing-arrangement page added and the study's completion in writing","study_done133",flags=["studyDone"],hidden="Kinship study completed with the standing arrangement documented",note="Complete, written, dated. Chair one is pulled fully in."),
     C("Verbal confirmation is enough — the study is clearly done","study_done133",note="'Clearly' is not a status the review can cite. Get the writing.")]),
  N("study_done133",71,"The Course and the Roster, Tested",[
    "Spring tests the second chair: the course completes (certificate filed), and the roster gets its unplanned examination when your shift runs long in April and the phone tree executes exactly as documented — sister by 9, Sabine by 9:20, Matteo asleep at his grandmother's with his homework done, the caseworker's check-in note recording the roster working as written.",
    "A plan that survives its test becomes the file's favorite kind of fact: the kind with a witness."],
    [C("File the check-in note and the course certificate together — the plan, tested and passed","review_prep133",flags=["servicesDone"],hidden="Services completed; coverage roster tested and documented as working",note="Tested, passed, filed. Chair two is in."),
     C("One good note doesn't need filing — don't gloat on paper","review_prep133",note="Filing is not gloating. It is how good notes survive staff rotations.")]),
  N("review_prep133",92,"The Spring Review",[
    "The spring review hears the three chairs in sequence: the study (approved, complete, the standing arrangement written in), the services (complete, the roster tested in the wild), and the appeal (pending at the Bureau, hearing set for June — its own building, its own clock).",
    "The judge's sentence is the one the table was built to earn: 'This family has organized itself around the plan. The plan should now organize itself around the family.' What remains is sequencing the ending so the appeal's decision and the case's return do not trip over each other."],
    PAPER("appeal_hearing133")),
  N("appeal_hearing133",141,"The Bureau Hearing",[
    "Friday, June 19, 2026. The agency carries its burden — substantial evidence that the report should remain indicated (23 Pa.C.S. § 6341(c.2)(5)) — and its summary meets the exhibits: thirty-eight minutes by timestamp, an investigation opened inside a neighbor's emergency, a coverage roster now signed and tested, a study approved.",
    "The hearing officer returns twice to the receipt. Paper that times a night beats adjectives that stretch it; 'extended period' does not survive cross-examination by a timestamp."],
    [C("Close on the receipt and the burden: their standard, their summary, your timestamps","decision133",note="The shortest closing in the library: a receipt, read aloud."),
     C("Close on Sabine and the year the family has had","decision133",note="Moving, true, and not the standard the officer must apply.")]),
  N("decision133",176,"Expunged — Chair Three",[
    "The decision arrives inside the 45-day window (23 Pa.C.S. § 6341(c.3)): the report is amended to unfounded. Chair three is pulled in. What remains is pure sequencing: the case's own permanency path, with Matteo's fifteenth month far off (entry January 12, 2026 → April 12, 2027) and the court's spring sentence still warm.",
    "Ms. Whitaker draws the endgame on the table page: trial return in the fall, with Sabine's placement converting to the family's standing respite — the kinship door held open by its own study — and the case to close at the new year if the trial reads the way the roster did."],
    [C("File the expungement in the dependency record and propose the dated endgame","endgame133",flags=["expungementFiled"],hidden="Expungement order filed in the dependency case; dated endgame proposed",note="The corridor walked again, order in hand. Sequencing is the last skill."),
     C("The court knows about the expungement by now","endgame133",note="Courts know what is filed. File it.")]),
  N("endgame133",238,"The Trial, Run Like the Roster",[
    "The fall trial runs the way the roster did: overnights becoming weeks, the phone tree retiring into an ordinary family's ordinary arrangements, Sabine's spare room reverting to a grandson's room with a standing invitation rather than a placement order.",
    "The new-year review is eleven minutes. The file the judge reads is the table, completed: study, services, appeal — three chairs, three checkmarks, one boy home."],
    [C("Ask for closure with the respite written into the final order — Sabine's door, in ink","end_three_chairs",req=["recordsRequested","appealFiled","studyDone","rosterSigned"],note="Closed, with the door held open on paper. The table stands."),
     C("Ask for closure today without the respite language","end_trial133",note="Closure either way, likely — but the respite in ink is the family's insurance, and insurance is written or it isn't."),
     C("Let the review close the case on its own momentum","end_trial133",note="Momentum closes cases eventually. Orders close them completely.")]),
  N("end_three_chairs",268,"All Three Chairs",[
    "The case closes in January with Matteo home, the registry clear, and Sabine's spare room holding a respite clause and a grandson's spare toothbrush — the two artifacts of the year, one legal and one not, both earned.",
    "State it the debrief way: the win was not any single chair. Studies complete every week in this system, and services complete, and appeals are won — by different families, in different cases. The capstone was the coordination: sprint first, marathons in parallel, every document carried across the table to the chair that needed it, until all three could be pulled in at once."],
    ending=True, debrief=[
      "THE TABLE'S LAW, CHAIR BY CHAIR — Appeal: notified January 30, 2026; 90 days → Thursday, April 30, 2026 (23 Pa.C.S. § 6341(a)(2)); evidence under (c.2)(4); the agency's burden under (c.2)(5); decision within (c.3)'s 45 days. Kinship: the study completed with the standing arrangement written into it — the placement's paper form, and the factual basis for the relative-care posture within 42 U.S.C. § 675(5)(E). Case: services completed and the coverage roster tested and documented; records under 55 Pa. Code § 3130.44(d) supplied the timestamped receipt that decided the appeal; counsel (42 Pa.C.S. § 6337) coordinated the three postures.",
      "WHY THIS IS A FULL WIN — Rare for a capstone: every track resolves completely — registry expunged, case closed, child home, kinship preserved as respite. It is full because the situation allowed it: one child, an early kinship placement, a short factual dispute (thirty-eight minutes) that documents could settle outright. The guide labels it full and notes the allowance honestly — most marathon cases end partial because their facts, not their paperwork, are heavier.",
      "WHAT NO STRATEGY CONTROLS — The hearing officer's weighing, the study's queue, the neighbor's emergency that started it. The route controlled the table: sequence, signatures, and the carrying of paper between chairs. In a three-chair case, coordination is not administration. It is the strategy."]),
  N("end_trial133",268,"Home, Two Chairs Pulled",[
    "Matteo comes home on the trial schedule and the case closes a season later than the best ending — the respite unwritten, the file's final order thinner than the family's actual arrangements. The appeal is expunged; the study stands; the services are complete. Only the sequencing frayed at the end.",
    "It is a good ending wearing the ordinary cost of the system's slowest habit: outcomes that everyone agrees on, arriving at the pace of whoever failed to propose them in writing."],
    ending=True, debrief=[
      "A PARTIAL WIN, NAMED HONESTLY — Everything resolved; only the timing and the ink suffered. The gated route required **recordsRequested**, **appealFiled**, **studyDone**, and **rosterSigned** arriving together at the final ask — the roster's signatures and the study's completion letter being the two papers most often left verbal in real three-chair cases.",
      "WHAT NO STRATEGY CONTROLS — The last review's judge and calendar. A family that has pulled all three chairs in will be home either way; the strategy's claim is about the season, and about whether the grandmother's door is held open by an order or by a habit."]),
  N("end_tipped",268,"The Tipped Table",[
    "In this branch, one chair was ignored until it fell: the appeal polished past April 30, or the study left to speak for itself until its items hardened into findings, or the roster left unsigned until the night it was needed and doubted.",
    "A three-chair table does not collapse all at once. It tips toward the neglected chair, and the case's center of gravity moves with it — the registry shadowing the mother's work, or the placement questioned, or the plan read as paper over a gap. Recovery is possible from any one tip. It costs the season the coordination would have saved."],
    ending=True, debrief=[
      "THE NEGLECTED CHAIR, ITEMIZED — The appeal's window (23 Pa.C.S. § 6341(a)(2)) is the only chair with a wall behind it; the study's items and the roster's signatures are the two most commonly left verbal. Each failure mode is a paperwork failure before it is anything else — which is the capstone's whole curriculum: at three chairs, the binding constraint is not effort but coordination.",
      "WHAT NO STRATEGY CONTROLS — Very little in this ending was weather. That is its function in the library: the control case that proves the table was the strategy."]),
  N("end_registry133",176,"Cleared Case, Standing Word",[
    "The dependency case closes beautifully — study, services, trial, home — and the registry keeps its word anyway, because the appeal's window closed on April 30 while the marathons were being run, and no one ran the sprint.",
    "The entry surfaces where entries surface: the school-district volunteer form, the home-health aide application Rosa had planned for the spring. The case is a success story with a footnote that outlives it — which is why the sprint is run first in every guide in this library, including this one."],
    ending=True, debrief=[
      "THE SPRINT THAT WASN'T — Notified Friday, January 30, 2026; 90 days → Thursday, April 30, 2026 (23 Pa.C.S. § 6341(a)(2)). Every other chair in this scenario can be recovered, continued, re-studied, re-signed. The appeal window cannot. Its loss does not defeat the case — the dependency court never asked the registry's permission — but it permanently taxes the mother's working life.",
      "WHAT NO STRATEGY CONTROLS — Nothing failed here except a date. The marathons were run well. The lesson is carved on the table itself: in multi-track cases, do the perishable thing first, especially when it is small."]),
 ],
 strategy=dict(
  win_honest="This is a **full** win — registry expunged, study complete, case closed, Matteo home, kinship preserved as written respite. The guide notes the allowance honestly: the facts permitted a full win (one child, kinship from the start, a thirty-eight-minute factual dispute that documents could settle). The capstone skill is coordination itself: three legal postures advanced in parallel and pulled together at one table.",
  law=[
   "**Sprint first.** The appeal window is the table's only immovable date: notified January 30, 2026 → Thursday, April 30, 2026 (23 Pa.C.S. § 6341(a)(2)). It is filed on day 8, before either marathon can eat the calendar.",
   "**The appeal is decided by a receipt.** The agency's burden (23 Pa.C.S. § 6341(c.2)(5)) meets a timestamped pharmacy receipt (thirty-eight minutes) and an incident report that opens the investigation inside a neighbor's emergency — evidence the appellant obtained through the case record (§ 3130.44(d)) and the appeal's own evidence rule (§ 6341(c.2)(4)); decision inside (c.3)'s window.",
   "**Kinship is a document, not a relationship.** The study itemized in writing — including the sometimes-couch problem and the standing-arrangement page — is what converts a grandmother's spare room into a placement the court can order and later convert to respite.",
   "**A roster is believed at three signatures.** The coverage plan answers the case's founding fact (forty minutes alone) in the only currency the review accepts: names, signatures, and a tested execution the caseworker herself documented. Counsel (42 Pa.C.S. § 6337) assigns the chairs; the parent owns the calendar that connects them."],
  traps=[
   ("Leaving the brother's 'sometimes' stays unaddressed in the study","studies speak about exactly such words; an unitemized study hardens its questions into findings."),
   ("Keeping the pharmacy receipt as a hearing surprise","filed receipts testify in both tracks for months; surprised hearing officers admit them once. The appeal's evidence packet and the case record each needed it."),
   ("Leaving the roster as a family understanding","understandings are doubted on the exact night they are needed; signatures are not — and the win's gate requires **rosterSigned**."),
   ("Polishing the appeal while the marathons run","the sprint has a wall: April 30. Its loss is the one ending no other chair can compensate (**Cleared Case, Standing Word**).")],
  uncontrolled="The hearing officer, the study queue, and the neighbor's emergency that opened the case. The route controlled sequence, signatures, and the carrying of paper between chairs — in a three-chair case, the whole of the controllable."),
)
