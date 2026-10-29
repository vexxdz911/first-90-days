# -*- coding: utf-8 -*-
from lib import C, N

def insert_chain(scen, after_id, chain):
    nodes = scen["nodes"]
    idx = next(i for i, n in enumerate(nodes) if n["id"] == after_id)
    node = nodes[idx]
    targets = {c["next"] for c in node.get("choices", [])}
    assert len(targets) == 1, (after_id, targets)
    orig = targets.pop()
    for c in node["choices"]: c["next"] = chain[0]["id"]
    for c in chain[-1].get("choices", []): c["next"] = orig
    nodes[idx + 1:idx + 1] = chain

def expand(S127, S128, S129, S130):
    # ---------- S127 additions (15 -> 20 nodes) ----------
    insert_chain(S127, "calendar", [
      N("visits127", 8, "Visits at Rania's Table", [
        "Visits happen at Rania's kitchen table, twice a week, with the refrigerator sign-in sheet Rania invented on day one: date, time in, time out, one line about the day. Zayd signs his name in letters that improve weekly, which the sheet records whether anyone meant it to or not.",
        "The caseworker calls this 'supervised by kin.' Rania calls it dinner. Both descriptions are accurate; only one of them is in the file, and it is the one with the sign-in sheet attached."],
        [C("Keep the sheet religiously and copy it monthly into your folder", "study_list", flags=["visitLog"], hidden="Kinship visit sign-in sheet kept and copied", note="A small sheet, doing a large job."),
         C("Enjoy the visits and skip the clerical part", "study_list", note="Dinner is dinner. The file, however, eats paper or it eats nothing.")])])
    insert_chain(S127, "appeal_sent", [
      N("appeal_ack", 23, "The Acknowledgment", [
        "A thin letter comes back: your appeal has been received and docketed. It decides nothing. It proves everything about timing — the date on it is inside the window, and the window was the whole battle of the appeal's first phase.",
        "Ms. Ferreira makes you file it on top of the appeal copy. 'First page of the appeal file,' she says. 'Proof before argument. Always in that order.'"],
        [C("File the acknowledgment with the stamped copy and note the docket number on the calendar", "records_beat", flags=["appealDocketed"], hidden="Appeal acknowledgment filed; docket number calendared", note="The appeal is now a case with a number, not a hope with a stamp."),
         C("Put it in the folder and move on to the housing hunt", "records_beat", note="In the folder is good. On top, in order, is better — but the folder forgives.")])])
    insert_chain(S127, "packet_back", [
      N("mirror_detail", 43, "The Line You Underline", [
        "One more page of the packet deserves its own evening: the scored assessment form's summary — present in redacted form — rates 'housing stability' at the bottom of its scale, dated the week of the cold night. It does not mention the boiler, the repair order, or the new unit's waitlist, because on the day it was scored, none of that paper existed yet.",
        "Forms are photographs. They show the day they were taken. The strategy of this whole case is to make sure later photographs get taken — with the repair log in the frame."],
        [C("Write the form's date on your statement's first line: 'As of the night scored, the following was also true'", "statement_filed", flags=["formDated"], hidden="Assessment summary dated and answered on the record", note="You cannot retake the photograph. You can caption it, with dates."),
         C("Leave the form alone — arguing with a score looks defensive", "statement_filed", note="Captioning is not arguing. But the statement still gets filed, and it carries most of the weight.")])])
    insert_chain(S127, "statement_filed", [
      N("school_note", 52, "The School's Sentence", [
        "Zayd's teacher, asked by the caseworker how he is doing, does something teachers are not required to do: she writes it down. One paragraph — attendance perfect, reading ahead, 'asks when the boiler at Mom's is fixed, in the tone of a boy expecting an answer.'",
        "It is the single most believed document in most files: a professional with no stake, writing about an ordinary week."],
        [C("Ask for a copy for both files and thank her in writing", "review_prep", cash=-5, flags=["schoolLetter"], hidden="Teacher's written statement filed in both tracks", note="Filed in both. Paper does not walk hallways by itself; you are the hallway."),
         C("Let the caseworker forward it if she thinks of it", "review_prep", note="She might. The file's memory for favors is shorter than its memory for documents.")])])
    insert_chain(S127, "review_prep", [
      N("shift_swap", 64, "The Schedule, Signed", [
        "Your motel supervisor signs the schedule you will need when the children come home: no overnight shifts on school nights, weekends at the playroom rate — the weekend job the registry almost took. A signed schedule is the plan's least poetic and most cross-examined page.",
        "Ms. Ferreira calls documents like this 'load-bearing paper': unglamorous, and the wall stands on them."],
        [C("File the signed schedule with the progress summary before the review", "review_day", flags=["schedulePaper"], hidden="Signed work schedule filed before the review", note="The plan now has a timetable, signed by someone other than you."),
         C("Bring the schedule to the hearing in your bag", "review_day", note="In your bag is a location. In the file is an argument.")])])

    # ---------- S128 additions (14 -> 26 nodes + hearing_eve) ----------
    insert_chain(S128, "start", [
      N("letter_detail", 1, "Reading for the Date That Isn't There", [
        "You read the indicated letter three times looking for the deadline, because deadlines are supposed to be in letters. It gives you the finding, the category, the warning about employment — and no date at all. The 90 days live in the statute, not in the envelope.",
        "It is the first lesson of the hallway: the system's letters tell you what it decided. The clocks you must find yourself, or have a lawyer find for you."],
        [C("Write 'July 5' on the envelope itself, in ink", "two_tracks", flags=["deadlineInked"], hidden="Appeal deadline written on the notice envelope", note="Crude, visible, effective. The envelope goes on the refrigerator."),
         C("Trust the calendar entry in your phone", "two_tracks", note="Phones lose things. Ink on an envelope is a technology too.")])])
    insert_chain(S128, "letter_detail", [
      N("porch_first", 7, "Odette's Refrigerator", [
        "Odette has already started the archive: the visit sign-in sheet, the class schedule, a photograph of Anouk's healed chin dated by the phone that took it. 'I raised a driver,' she says, 'not a defendant. But paper is paper.'",
        "Grandmothers who keep records are a documented advantage in this system, and this one keeps them in date order."],
        [C("Align your folder to hers — same dates, same order, copies both ways", "appeal_filed", flags=["foldersAligned"], hidden="Parent's and kinship caregiver's folders aligned", note="Two folders, one chronology. Files that agree are hard to argue with."),
         C("Let her keep her system and you keep yours", "appeal_filed", note="Two systems, two stories, one reconciliation owed later.")])])
    insert_chain(S128, "appeal_filed", [
      N("porch2", 14, "The Chin, Healing", [
        "The stitches are out. What remains is a small white line and a pediatrician's instruction to photograph it monthly for the well-child file — ordinary medicine that doubles, without anyone intending it, as a dated record of a healing child in a documented home.",
        "The caseworker photographs it too, for her file. For once, both files take the same picture."],
        [C("Keep the dated photos with the medical records in both folders", "study_paper", flags=["photosKept"], hidden="Dated medical photographs kept with records", note="A timeline no one has to testify to."),
         C("One photo is plenty — this feels like building a case against yourself", "study_paper", note="It is building the case that already exists, in the order it actually happened.")])])
    insert_chain(S128, "evidence_built", [
      N("packet_index", 31, "Indexing the Packet", [
        "Ms. Lindqvist makes an index for the appeal packet: one page, eleven exhibits, each with a date and a one-line description. It takes twenty minutes. 'Hearing officers read indexes,' she says, 'the way judges read chronologies. Give the reader a map and they will follow you anywhere in the file.'",
        "The addendum is Exhibit 4. She does not star it. The map does the starring."],
        [C("File the index with the packet in both tracks", "case_packet", flags=["indexFiled"], hidden="Exhibit index filed with the appeal packet and the case chronology", note="Eleven exhibits, one page, no stars. The map is the argument's skeleton."),
         C("Skip the index — the exhibits speak for themselves", "case_packet", note="Exhibits speak in the order they are found. Indexes decide the order.")])])
    insert_chain(S128, "case_packet", [
      N("gap_found128", 46, "The Nine Arranged-Later Days", [
        "Your chronology draft has a hole you keep stepping over: the plan says visits 'to be arranged,' and then nine days pass in the record like a held breath before Odette's first sign-in. The agency's own notes fill two of those days with a staffing shortage — written, dated, theirs.",
        "A gap owned by the file is a gap the other side cannot assign to you at the review. The chronology's job is to make every date belong to whoever actually owned it."],
        [C("Write the nine days into the chronology with the staffing note cited by date", "chronology", flags=["gapOwned"], hidden="Visit-arrangement gap documented from the agency's own notes", note="Their note, your chronology, no one's adjective. Dates are polite that way."),
         C("Leave the nine days blank — drawing attention to them helps no one", "chronology", note="Blank days get narrated by whoever speaks first at the review. It will not be you.")])])
    insert_chain(S128, "chronology", [
      N("class_done", 58, "The Certificate", [
        "The parenting course ends with a certificate and an instructor who writes, unprompted, that you asked for the reading list 'for the grandmother too.' It is a small sentence with a long reach: it describes a family organizing itself around a child, which is the case's whole argument in one line.",
        "Certificates go in the folder the day they are issued. Paper that waits in a car visor until a hearing is paper at risk."],
        [C("File the certificate and the instructor's letter in both tracks the same week", "night_shift", cash=-5, flags=["certificateFiled"], hidden="Course certificate and instructor letter filed in both tracks", note="Same week. The folder's rule is: paper travels at the speed of the event, not the deadline."),
         C("Keep the certificate for the appeal hearing — fresher that way", "night_shift", note="Nothing about a certificate improves with age except its chance of being lost.")])])
    insert_chain(S128, "class_done", [
      N("night_shift", 66, "The Night Course", [
        "The commercial license course meets Tuesdays and Thursdays, and the instructor signs attendance the way Odette signs visits: without ceremony, in ink, every time. Your employer writes the letter the file loves most — a promotion contingent on the license, with a number in it: the raise, dated, on letterhead.",
        "Why does a delivery company's letter belong in a child-welfare file? Because 'stability' is a scored word, and this is what it looks like with a date on it."],
        [C("File the attendance record and the employer's letter before the July review", "review_prep", cash=-5, flags=["employerLetter"], hidden="License-course attendance and employer letter filed", note="Stability, documented by the two institutions that can actually vouch for it."),
         C("Mention the course at the review if it comes up", "review_prep", note="It comes up if it's filed. Very little else comes up.")])])
    insert_chain(S128, "night_shift", [
      N("sister_call", 70, "Your Sister's Statement", [
        "Your sister — whose barbecue it was — offers to 'tell them what really happened.' Ms. Lindqvist redirects the offer into the form this system believes: a written statement, signed, dated, describing only what she saw: the platform's height, the grass, the rail she now admits was loose, the drive to urgent care.",
        "She signs it in Odette's kitchen. It is three paragraphs. It has the great virtue of being about a railing, not about you."],
        [C("File her statement in the appeal packet and the case record", "medical_letter", cash=-5, flags=["sisterStatement"], hidden="Eyewitness statement signed, dated, and filed in both tracks", note="What she saw, in writing, in both hallways."),
         C("Save her for live testimony at the appeal — more powerful in person", "medical_letter", note="Live witnesses get cross-examined. Filed statements get read twice, alone, by the person deciding.")]),
      N("medical_letter", 76, "The Pediatrician's Paragraph", [
        "Anouk's pediatrician, at the well-child visit, writes the paragraph pediatricians write when they are not worried: growth on curve, chin healed, 'no concerns.' Six months of the case have produced a small library; this paragraph is its quietest and, to a hearing officer, possibly its most credible page.",
        "Professionals with no stake write the sentences that decide paper cases. Collect them like weather reports from a clear sky."],
        [C("Request a copy for the appeal packet the same day", "records_supp", flags=["pedsLetter"], hidden="Pediatrician's well-child letter filed in the appeal packet", note="Same day. Clear skies do not need to be chased, just copied."),
         C("It's in the medical file if anyone needs it", "records_supp", note="Whose medical file, in which building, under which name? Copies end that inquiry.")]),
      N("records_supp", 82, "The Redaction Question", [
        "A page of the case record arrives with a whole paragraph blacked out — a neighbor's statement, you are told, withheld under the regulation's confidentiality rules (55 Pa. Code § 3130.44(f)). It looks like a secret. Ms. Lindqvist reads the citation and shrugs: 'Their rule, applied as written. We note the page and move on — the appeal packet doesn't need it.'",
        "Knowing which black bars are the system working and which are the system hiding is a skill. The citation is how you tell them apart."],
        [C("Note the redacted page by number in the chronology and move on", "daycare_letter", flags=["redactionNoted"], hidden="Redacted page noted by number; § 3130.44(f) basis recorded", note="Noted, numbered, un-feared. The file keeps its secrets in the open that way."),
         C("Write a complaint about the blacked-out paragraph", "daycare_letter", note="Complaints about lawful redactions spend credibility the appeal will need.")]),
      N("daycare_letter", 88, "The Job That Waits on the Registry", [
        "The playroom at your employer's sister property posts its weekend shifts — the extra money that was supposed to fund the bigger apartment. The posting carries the sentence you knew was coming: childcare clearance required. The registry is not an abstraction; it is a shift differential.",
        "Ms. Lindqvist files the posting itself in the appeal packet. 'Stakes are not evidence,' she says, 'but hearing officers are people, and people should know what their signature does.'"],
        [C("File the posting and your employer's hold-letter in the packet", "hearing_eve", flags=["stakesFiled"], hidden="Clearance-requiring job posting filed to show the registry's concrete stakes", note="Not evidence. Context, dated — the kind hearing officers remember at signature time."),
         C("Leave employment out of it — the appeal is about the fall", "hearing_eve", note="The appeal is about the fall. The fall's consequences hold a job hostage. Both things are in the statute's warning, verbatim.")])])
    # hearing_eve sits between the July review and the Bureau hearing: manual append + rewire
    _he = N("hearing_eve", 124, "The Night Before Door One", [
        "Tomorrow: the Bureau hearing. The packet is indexed, the chronology filed in both tracks, Odette's sheet copied, the addendum at Exhibit 4. Ms. Lindqvist's final instruction is procedural and almost kind: 'Say less than the paper. The paper has been preparing for months. Let it talk.'",
        "Anouk sleeps at Odette's, unaware that her chin's white line has become a legal document with an index. Some childhoods are measured in summers. Hers, this year, is measured in exhibits — and the exhibits, at last, are complete."],
        [C("Sleep. The packet is the preparation.", "appeal_hearing", note="The hallway's oldest advice, and its best.")])
    S128["nodes"].append(_he)
    for _n in S128["nodes"]:
        if _n["id"] == "review_prep":
            for _c in _n["choices"]:
                if _c["next"] == "appeal_hearing":
                    _c["next"] = "hearing_eve"

    # ---------- S129 additions (13 -> 26 nodes) ----------
    for n in S129["nodes"]:
        if n["id"] == "packet_built":
            n["title"] = "The Packet, Assembled"
            n["body"] = ["Mr. Osei spreads the folder and the record side by side on his office table: nine boxes across the top, their closing documents beneath, the two gaps with their dates, the letters in the order the court will want them. 'A packet is an argument,' he says, 'that has stopped needing you in the room.'",
                         "It goes in two weeks before the review, with a one-page summary on top — because the first page of a packet is the only page guaranteed a reading, and the summary makes the rest worth turning."]
    insert_chain(S129, "folder", [
      N("boxes_detail", 21, "Reading the Plan Like a Contract", [
        "You and Mr. Osei read the nine boxes the way landlords read leases: for the verbs. 'Parent will attend' is yours. 'Agency will refer' is theirs. Three boxes have their verbs; two are written in a fog of 'as appropriate' that no one will ever be measured against.",
        "He writes the fog-boxes on an index card. 'These are the ones that come back as surprises,' he says. 'We will ask about them monthly, in writing, until they have dates.'"],
        [C("Start the monthly written check-in on the fog-boxes", "referral_dates", flags=["fogTracked"], hidden="Plan's vague provisions tracked by monthly written check-ins", note="Fog, pursued monthly, precipitates into dates."),
         C("The plan is the plan — don't over-lawyer a service plan", "referral_dates", note="The plan is a contract the court will enforce from memory of summaries. Over-lawyering is the job.")])])
    insert_chain(S129, "visit_log", [
      N("winter_visit", 77, "The Visit Room in Winter", [
        "December visits smell of wet coats. Emeka, four months old, tracks your face the way the developmental chart says he should, and the supervisor writes it down because you have learned to ask, politely, at the end of every visit: 'Will today's note say what he did?'",
        "Asking about the note is not vanity. The notes are the visit, as far as every future reader is concerned. A parent who asks is a parent whose visits get described carefully."],
        [C("Ask, and add your own line to your log: what he did, what you did, what was said", "gap_letter", flags=["notesAsked"], hidden="Parent confirms each visit note and mirrors it in her own log", note="Two accounts, agreeing. The file's favorite kind of fact."),
         C("Don't make it awkward — just enjoy the hour", "gap_letter", note="The hour is enjoyed either way. Only one version leaves a careful note behind.")])])
    insert_chain(S129, "record_back", [
      N("winter_review", 140, "The Winter Review", [
        "The winter review is ten minutes long. The judge has read the summaries, which say 'progressing,' and your response — not yet filed — exists only as your lawyer's spoken sentence: 'The record shows two referral gaps, Your Honor, which we will document.'",
        "The judge nods and writes something. What she writes, you will never see. What you file, she cannot avoid seeing. The difference between those two sentences is the rest of this scenario."],
        [C("Leave court determined: the response gets filed this week, not 'in due course'", "response_filed", flags=["responsePrompted"], hidden="Winter review attended; filing resolve set by the court's nod", note="'In due course' is where documents go to be forgotten politely."),
         C("Take the nod as good news and let the lawyer handle timing", "response_filed", note="The nod was good news. It was also, unmistakably, a test.")])])
    insert_chain(S129, "response_filed", [
      N("course_cohort", 182, "The January Cohort", [
        "The parenting course finally starts — the one whose referral spent seven weeks in a mailbox. The instructor's sign-in sheet has your name in the first row, because you arrive the way you arrive at visits: early, with a pen that works.",
        "Eight sessions. Eight signatures. At the end, a certificate with a seal that means nothing to you and everything to a file."],
        [C("Attend all eight, file the certificate the week it issues", "treatment_letter", flags=["courseDone"], hidden="Parenting course completed; certificate filed", note="Eight signatures, one seal, filed while the ink is still a fact."),
         C("Miss the rainy one — one absence can't matter", "treatment_letter", note="It can. Not because of the absence; because of the blank space where a signature argues by its absence.")]),
      N("treatment_letter", 196, "The Program's Word", [
        "Your treatment program's counselor writes the letter programs write when attendance has been, in her word, exemplary: dates enrolled, sessions attended, screens clear, prognosis 'excellent, with supports.' It is addressed 'To Whom It May Concern,' which in this system means: to the file.",
        "Letters like this have a half-life. Filed in February, it is evidence. Produced in June, it is archaeology."],
        [C("File it in February, with a copy to every party", "visit_expand129", cash=-5, flags=["treatmentFiled"], hidden="Treatment completion letter filed with copies to all parties", note="Evidence, not archaeology. The half-life is respected."),
         C("Keep it for the final review — save the good material", "visit_expand129", note="Saved material arrives as a claim. Filed material arrives as a fact.")]),
      N("visit_expand129", 210, "Longer Tuesdays", [
        "Visits expand: two hours, then an afternoon, then — the milestone the supervisor announces without ceremony — a Saturday at Mrs. Abernathy's house, where Emeka's other life is, so you can learn its geography: the crib, the rattle, the dog's name.",
        "Expansion is the plan voting with its feet. Each lengthening is a document, and the documents now agree with each other in two folders at once."],
        [C("Log every expanded visit, and write Mrs. Abernathy a thank-you she can keep", "plan_noted", flags=["expansionLogged"], hidden="Expanded visits logged; foster caregiver thanked in writing", note="Gratitude, in writing, in a file — the system reads kindness as stability because, usually, it is."),
         C("Just live the longer visits — don't document joy", "plan_noted", note="Joy documented is not diminished. Joy undocumented is just unproven.")])])
    insert_chain(S129, "plan_noted", [
      N("unit_viewing", 240, "The Unit", [
        "The July letter becomes a June viewing: a second-floor two-bedroom with a window over a courtyard, a lease contingent on the review's word. The housing worker photographs the empty rooms for the file — bare floors that read, in this context, like a promise with measurements.",
        "You photograph them too, from the doorway, where a parent stands in a home that is not yet hers, learning its light."],
        [C("File the lease-contingent letter and the housing worker's photos", "foster_letter", cash=-5, flags=["leaseFiled"], hidden="Contingent lease and unit documentation filed", note="Bare floors, dated. The court has seen a thousand promises; measurements are rarer."),
         C("Wait for the actual keys before troubling the file", "foster_letter", note="Keys trouble files pleasantly. Contingencies, filed early, trouble them usefully.")]),
      N("foster_letter", 258, "Mrs. Abernathy's Letter", [
        "Mrs. Abernathy writes to the court — foster parents may, and the good ones do — a page about Emeka's year: his first food, his sleep, his laugh at the dog, and the sentence that matters: 'His mother has never missed a Tuesday. I would trust her with him because I have watched her earn it weekly.'",
        "It is the only document in the file written by someone who had the child and gave him back, weekly, on time, smiling. Judges read those letters twice."],
        [C("Thank her, copy the letter into your packet exactly as written", "month9_review", flags=["fosterLetter"], hidden="Foster caregiver's support letter included in the packet", note="Exactly as written. Her credibility is the exhibit; editing is not your privilege."),
         C("Let the letter travel through the agency on its own", "month9_review", note="Letters traveling alone sometimes don't. The packet is its escort.")]),
      N("month9_review", 276, "The Nine-Month Review", [
        "The nine-month review goes the way the winter one didn't: the judge works from filed paper — the letters, the logs, the gap chronology with its two corrected dates — and her questions are the questions of a court checking a list it expects to complete.",
        "'We'll take the permanency question at the thirteen-month review,' she says. 'I want the record complete by then.' This time, complete is not a hope. It is an inventory, and most of it is already checked."],
        [C("Treat the sentence as a specification: list everything the record still lacks", "packet_built", flags=["specListed"], hidden="Court's completeness standard converted into a checklist", note="A specification can be met on purpose. It now will be."),
         C("Take the good tone as the victory and coast to September", "packet_built", note="Tone is weather. The specification was the climate. Coasting is how packets stay unbuilt.")])])
    insert_chain(S129, "packet_built", [
      N("overnights", 322, "Overnights", [
        "August: Emeka sleeps at your apartment for the first time since he was six weeks old — the contingent lease signed after the nine-month review, the crib assembled by Mrs. Abernathy's husband, who accepts pie as full payment and files a verbal receipt: 'Sturdy.'",
        "You keep the calendar on the refrigerator anyway. Habits built over a year do not retire on command, and this one has become less a strategy than a description of the household: what happens here gets written down."],
        [C("Log the overnights and the first-week pediatrician visit, and file both", "aftercare_plan", flags=["overnightsLogged"], hidden="Overnight trial logged with pediatric follow-through filed", note="The trial writes its own evidence, one dated morning at a time."),
         C("He's home-ish — stop logging and just be his mother", "aftercare_plan", note="You are his mother either way. The log is for the one remaining reader: the September court.")]),
      N("aftercare_plan", 344, "Aftercare, In Writing", [
        "The agency proposes aftercare supports — the visiting nurse, the early-intervention screening, the treatment program's alumni group — and for once you are the one saying the sentence: 'Wonderful. Put it in writing, with dates.'",
        "The caseworker laughs and does. A year ago the system's paper was something done to you. The folder changed the direction of the ink."],
        [C("Get the aftercare plan signed and filed before the review", "packet_audit", flags=["aftercareWritten"], hidden="Aftercare plan reduced to writing and filed", note="Signed, dated, filed. The case's last document is written the way its first ones should have been."),
         C("Accept the verbal plan — everyone's aligned now", "packet_audit", note="Alignment is a mood. Writing is a commitment with a date on it.")]),
      N("packet_audit", 366, "The Audit", [
        "Two weeks out, you and Mr. Osei audit the packet against the judge's specification, line by line: nine boxes, nine closing documents; two gaps, two chronologies; a year of Tuesdays, signed twice. One page is missing — the treatment program's final discharge summary, promised for Friday.",
        "An audit that finds nothing is a ritual. An audit that finds one page is a rescue."],
        [C("Chase the discharge summary in writing and file it the day it issues", "night_before129", cash=-5, flags=["auditDone"], hidden="Packet audited against the court's standard; final document chased in writing", note="Complete, on purpose, with one rescue to prove the audit worked."),
         C("Friday's summary can be handed up at the review — close enough", "night_before129", note="Handed-up paper is a speech. Filed paper is a record. The audit existed to teach exactly this.")]),
      N("night_before129", 384, "The Night Before Month Thirteen", [
        "The packet is filed. The summary is signed. Emeka sleeps in the crib in the next room on the last night of the trial that the calendar still calls a trial, and the folder — a year thick, tabbed, in date order — sits on the table like a second, quieter attorney.",
        "Tomorrow the court reads the book everyone wrote. You just made sure you were one of its authors."],
        [C("Sleep. The year is the preparation.", "final_review", note="The folder's last service is a quiet house the night before.")])])
    for n in S129["nodes"]:
        if n["id"] == "plan_noted":
            n["choices"].append(C("Consider the folder finished — the letters can speak for themselves from here", "end_clock129", note="Folders finished early have a way of being read as finished cases."))
        if n["id"] == "end_clock129":
            n["body"] = ["This branch is the year played at the file's pace instead of yours: the letters stopped in spring, the packet was never assembled, and the reviews summarized a plan whose remaining boxes looked — from the distance of a summary — simply open.",
                         "At fifteen of the most recent twenty-two months, the conversation changes its subject: from your progress to the agency's filing duty and its exceptions (42 U.S.C. § 675(5)(E)). The exceptions exist — kinship care, a documented compelling reason, services identified but not provided — but they must be documented to be argued, and documentation is the one crop this branch stopped planting in the spring."]

    # ---------- S130 additions (13 -> 26 nodes) ----------
    insert_chain(S130, "start", [
      N("winter_detail", 2, "The Winter, Itemized", [
        "Before any of it moves, the winter deserves its true inventory: the hours cut in November, the landlord's letter, the housing program's intake date, Bram's school twenty minutes one way and Sable's another — a family logistics problem that the file calls 'instability' the way maps call mountains 'terrain.'",
        "You are not the summary. But the summary is what travels, unless the file is made to carry more."],
        [C("Write the winter as a one-page chronology and give it to Mr. Adeyemi", "lawyer_first", flags=["winterWritten"], hidden="Family's own chronology of the placement winter written", note="Your version exists now, with dates. Summaries hate competition."),
         C("The file knows the story well enough", "lawyer_first", note="The file knows a four-word version. Competition is coming whether you write it or not.")])])
    insert_chain(S130, "lawyer_first", [
      N("job_letter", 10, "The Offer, On Letterhead", [
        "The warehouse's offer letter is a beautiful document: full-time, benefits, a start date, a number. It is also, in a case file, a loaded one — proof of stability and evidence of disruption in the same paragraph, depending on who frames it first.",
        "Framing is a race the early note almost won. The letter, filed with a plan wrapped around it, is a different exhibit from the letter discovered later, alone."],
        [C("File the offer letter together with the transfer plan, as one exhibit", "inventory", flags=["offerFiled"], hidden="Job offer filed together with the transfer plan", note="Framed by its plan. The exhibit argues stability because its context is attached."),
         C("Keep the letter out of the file until the plan is approved", "inventory", note="Letters kept out of files have a habit of arriving anyway, unaccompanied.")])])
    insert_chain(S130, "inventory", [
      N("packet_copy", 20, "The Second Set", [
        "Mr. Adeyemi's paralegal makes a complete second set of the file — every page, stamped COPY, in a box that will live at your sister's house. 'Files that exist twice,' he says, 'can survive one building's bad week. Files that exist once are a rumor away from being a summary.'",
        "It costs an afternoon and a ream of paper. It is the cheapest insurance in the entire case."],
        [C("Make the second set and store it outside both counties' buildings", "record_req130", cash=-10, flags=["secondSet"], hidden="Complete second copy of the file made and stored", note="Two sets, two buildings, one story. Insurance against entropy."),
         C("The inventory list should be protection enough", "record_req130", note="A list proves what existed. A copy replaces it. Different tools; entropy respects only one.")])])
    insert_chain(S130, "record_req130", [
      N("record_index", 34, "Indexing the Winter", [
        "The record arrives in a box with no order anyone will admit to choosing. You and the paralegal index it in an evening: 212 pages, each numbered, dated where datable, the gaps listed as gaps — two missing referral pages noted by their absence, which is also a kind of presence.",
        "From tonight, your case has a table of contents. Every later argument in either county can cite page numbers instead of memories."],
        [C("Number and index every page; list the two gaps as items in the index", "statement130", flags=["recordIndexed"], hidden="Case record indexed by page; gaps listed as items", note="'Gap, pages 88–89' — an absence with an address can be filled. A vague one can't."),
         C("Skim for highlights and trust the inventory", "statement130", note="Highlights are for reading. Indexes are for winning arguments in buildings that love citations.")])])
    insert_chain(S130, "statement130", [
      N("school_records", 47, "The Schools, Notified in Writing", [
        "Both schools get letters before the move: Bram's counselor and Sable's teacher, with the new address, the Sunday-dinner continuity plan, and a request — in writing — for the records transfer to include the counselors' own notes, not just grades.",
        "Schools are the system's most honest witnesses because they see children daily and keep their own paper. A transfer that carries the counselors' voices carries your children's ordinary weeks across the line."],
        [C("Send the letters and confirm receipt with both schools", "plan_amended", cash=-5, flags=["schoolsNotified"], hidden="Schools notified in writing; records transfer requested with counselor notes", note="Receipts confirmed. The children's ordinary weeks will travel with names on them."),
         C("The district handles school transfers automatically", "plan_amended", note="Districts handle enrollments automatically. Counselor notes travel only when somebody asks, in writing.")])])
    insert_chain(S130, "plan_amended", [
      N("notice_given", 62, "Notice, Given Properly", [
        "You give notice at the old warehouse with the offer letter's start date circled, and your supervisor — the one who cut the winter hours — writes you the letter you did not expect: 'rehire-eligible, valued employee,' dated, signed. The file gains a page from an unlikely witness, which is the most believable kind.",
        "Paper does not care about anyone's narrative. It just accumulates, in date order, into a climate."],
        [C("File the supervisor's letter with the employment documents", "benefits_transfer", flags=["supervisorLetter"], hidden="Former employer's dated reference letter filed", note="An unlikely witness, filed. Climates are built from exactly such pages."),
         C("A warehouse reference doesn't belong in a child-welfare file", "benefits_transfer", note="Everything about stability belongs in the file. The file decides what matters; your job is supply.")]),
      N("benefits_transfer", 69, "The Other Paperwork", [
        "Benefits, medical cards, the housing program's file — each has its own county queue and its own idea of your address. You spend two days doing the unglamorous crossings: forms, confirmations, reference numbers read back over the phone and written down, because a confirmation number is a document too.",
        "Families lose weeks in these seams. The seams are where the year hides."],
        [C("Log every confirmation number in the folder, dated", "intro_sent", flags=["seamsLogged"], hidden="Benefits and services transfers logged with confirmation numbers", note="Two days of seams, logged. The year will not hide there."),
         C("The agencies will sort the transfers out between themselves", "intro_sent", note="They will sort most of it, eventually, in some order. The folder prefers certainties.")])])
    insert_chain(S130, "intro_sent", [
      N("intake_call", 84, "The Intake Call", [
        "Ms. Whitfield calls before the box even arrives — your lawyer's introduction letter saw to that — and the call is brisk: she has the summary, expects the file Friday, and asks three questions the summary couldn't answer. You answer them from the index, by page number.",
        "There is a pause. 'You have the record,' she says. It is not quite a compliment. It is better: it is a recalibration."],
        [C("Offer to walk the inventory with her when the box lands, page by page", "confirm_whole", flags=["walkOffered"], hidden="Page-by-page inventory walk offered to the receiving worker", note="An offer that makes 'mostly arrived' impossible to say with a straight face."),
         C("Let the file speak when it arrives", "confirm_whole", note="It will — in the order it fell into the box. The walk imposes your order.")])])
    insert_chain(S130, "confirm_whole", [
      N("file_gap_found", 108, "Page 88", [
        "The walk finds it: pages 88–89 of the record — the referral chronology, the very heart of the services story — did not survive the trip. A scan queue ate them, or a box did. Entropy does not sign its work.",
        "This is the moment the whole strategy was built for. A loss that can be proved can be cured; a loss that can't be proved becomes the case. You have the inventory, the index, and the second set."],
        [C("Produce the second set's copies of pages 88–89 and amend the arrival confirmation to note the cure", "packet_resent", cash=-5, flags=["gapCured"], hidden="Missing pages cured from the family's second set; confirmation amended", note="Cured, noted, closed. The chain of custody holds — because it was a chain."),
         C("Ask the sending county to re-send and hope the queue is kinder", "packet_resent", note="Hope is not a custody procedure. The copies in your sister's closet are.")])])
    insert_chain(S130, "file_gap_found", [
      N("packet_resent", 121, "The Amended Confirmation", [
        "Ms. Whitfield signs the amended confirmation herself: file complete as of today, two pages restored from the family's copy, restoration noted. 'In nine years,' she says, 'no family has ever handed me back my own file's missing pages.'",
        "'In nine years,' you could say, 'no family was told to count.' You don't. The confirmation is signed. Some victories are complete in a signature and spoiled by a speech."],
        [C("File the amended confirmation at the front of the new county's packet", "rhythm", flags=["amendedFiled"], hidden="Amended arrival confirmation filed at the packet's front", note="Front of the packet: the proof that this file is whole, signed by the other side."),
         C("Keep the confirmation in your folder only", "rhythm", note="Your folder already believes you. The county's file is the one that needed convincing.")])])
    # fall chain after the receiving review (rhythm): manual insert + single-choice rewire
    _chain130 = [
      N("fall_review", 185, "The Fall Review", [
        "The receiving county's fall review is short. The judge works the plan box by box — the new county's services now have your requested dates attached, the schools' letters are in, the Sunday log continues — and the hearing has the texture the winter one never did: a court reading a file that reads back coherently.",
        "'Step-down in the spring,' the judge says, 'if the winter looks like the fall.' It is a conditional sentence, and for the first time in the case, the condition is one your habits can meet."],
        [C("Ask for the condition in the order's words: overnights by spring if the log and letters continue", "goal_question", flags=["conditionWritten"], hidden="Step-down condition written into the review order", note="Conditions in orders bind. Conditions in memories evaporate."),
         C("Accept the judge's tone as the promise", "goal_question", note="Tone is not an order. The clerk types orders.")]),
      N("goal_question", 214, "The Goal, Questioned Once", [
        "In November the agency's report floats the sentence every long case eventually hears: whether the goal should be revisited in light of 'the extended timeline.' It is one sentence in a long report, and it is how goal changes begin — not with motions, but with weather.",
        "Your answer is already in the file: the plan's own compelling-reason entry, the dated progress in two counties, the judge's conditional sentence. Weather is answered by climate, and climate is made of paper."],
        [C("File a short written response quoting the plan's entry and the fall order, with dates", "holiday_visits", cash=-5, flags=["goalAnswered"], hidden="Goal question answered in writing from the plan and orders", note="One sentence, answered by three documents. The weather passes."),
         C("Raise your objection verbally at the team meeting", "holiday_visits", note="Meetings adjourn. Sentences in reports get quoted. Write the reply where the quote lives.")]),
      N("holiday_visits", 243, "The Holidays, Documented", [
        "December in the new apartment: a tree Bram insists on measuring, Sunday dinners that now run in both directions — the foster parents come to you, bringing the pie and, one week, the original sign-in binder, retired with honors.",
        "The caseworker visits, photographs the tree for the file, and writes 'home environment warm and organized' in the tone of a woman closing a question. Some sentences in files are endings wearing the costume of notes."],
        [C("Keep the holiday log and file the caseworker's note with it", "spring_review", flags=["holidayLogged"], hidden="Holiday period logged; favorable home-visit note filed", note="The winter that started the case, answered by a documented December."),
         C("Holidays are private — keep them out of the paperwork", "spring_review", note="Privacy is a value. So is a warm sentence in a file, in December, where a judge will find it in March.")])]
    for _n in S130["nodes"]:
        if _n["id"] == "rhythm":
            for _c in _n["choices"]:
                if _c["next"] == "spring_review":
                    _c["next"] = "fall_review"
    _idx = next(i for i, _n in enumerate(S130["nodes"]) if _n["id"] == "rhythm")
    S130["nodes"][_idx + 1:_idx + 1] = _chain130
    for n in S130["nodes"]:
        if n["id"] == "intro_sent":
            n["choices"].append(C("Skip the introduction, the walk, and the confirmation — the box is taped and the case is moved", "end_thin130", note="What arrives will be whatever arrives. That is not a plan; it is a hope with a tracking number."))
    return S127, S128, S129, S130
