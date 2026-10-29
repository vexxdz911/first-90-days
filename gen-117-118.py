#!/usr/bin/env python3
"""Generate scenarios 117-118 (Wave 2, Batch 9: Education & Medical).
Fictional composites only."""
import sys
sys.path.insert(0, "/home/hatch/workspace/your_files/tacticwatch-game")
from batchN_lib import N, C, E, emit, fmt
from datetime import date, timedelta

# ============================================================ S117 (Foundation)
S = date(2026, 9, 14)
assert fmt(S) == "Monday, September 14, 2026"
assert fmt(S + timedelta(days=3)) == "Thursday, September 17, 2026"   # shelter care, within 72 hours
assert fmt(S + timedelta(days=22)) == "Tuesday, October 6, 2026"      # review

s117_meta = {
    "title": "The First 90 Days",
    "subtitle": "Scenario 117 — The Bus That Crosses the Line (a fictional composite)",
    "startDateISO": "2026-09-14",
    "startNode": "start",
    "startCash": 120,
    "tier": "Foundation",
    "summary": "You are Gina. The water was shut off on a Friday, you worked the weekend anyway, and on Monday the county took Nolan, nine, into care. He is sleeping at your sister Odessa's — safe, loved, and one school district too far away.",
}

s117 = [
 N("start", 0, "The shutoff notice, come due",
   ["The water went off on Friday, while you were at the warehouse. The landlord's letter blamed the building's pipes; the city's notice named a date three weeks out. You filled the tub, bought jugs, and worked your weekend shifts because the alternative to a paycheck is not a principle — it is another shutoff.",
    "Nolan, nine, spent Saturday at the neighbor's and Sunday telling you the flushing trick he had invented. On Monday the school nurse asked him why he smelled of the corner-store wipes, and by three o'clock a caseworker, Ms. Iversen, was standing in your kitchen reading the notice on the fridge. By six, the decision was made: Nolan cannot stay in a home without water tonight."],
   [C("Ask the only question that matters tonight: \"Where does he sleep?\"", "office")]),

 N("office", 0, "Where he sleeps",
   ["Ms. Iversen's answer is better than you feared and worse than you hoped. Nolan will stay with your sister Odessa — the county calls that a kinship placement, and Odessa said yes before the worker finished the question. He will sleep in a house he knows, with his cousins, twenty-five minutes away.",
    "\"One thing to hear clearly,\" Ms. Iversen says. \"Odessa lives across the district line. Nolan's school is here. What happens about school is a separate decision from where he sleeps — and it starts moving on its own, fast, unless somebody asks for it to be made properly.\""],
   [C("Write that sentence down, word for word, in the notebook you bought at the dollar store.", "lawyer_call")]),

 N("lawyer_call", 1, "A lawyer, and a clock",
   ["Mr. Rahal, the attorney the court appoints for you, meets you in a courthouse hallway with a folder already started. The rights are not favors: you are entitled to counsel in this case (42 Pa.C.S. § 6337), and the first hearing — shelter care — must happen within 72 hours of Nolan being taken into care. (42 Pa.C.S. § 6332; 23 Pa.C.S. § 6315(d)) Thursday, he says. Count it yourself.",
    "\"Thursday decides placement — whether care continues, and where. School is decided elsewhere, by the districts and the agency, in meetings that happen in offices. Parents lose the school fight in those offices all the time, usually without knowing there was one. We are not going to.\""],
   [C("\"Then tell me what the school fight even is.\"", "plan_visit")]),

 N("plan_visit", 2, "Sleepover rules",
   ["Odessa's spare room has Nolan's spare toothbrush in it already, which breaks your heart in the useful direction. He shows you the bed, the cousins' chore chart with his name added in marker, and then asks the question sideways, the way nine-year-olds ask the real ones: \"Do I still go to my school? Mrs. Pavlik said our class gets the reading corner in October.\"",
    "The federal education law has an answer-shaped shape: children in foster care are supposed to stay in their school of origin — the school they attended when they entered care — unless a determination is made, on all the factors, that it is not in their best interest. (20 U.S.C. § 6311(g)(1)(E)(i)) Nobody has made any determination about Nolan. A transfer is simply what happens by default while nobody makes one."],
   [C("Tell him the truth at his size: \"I am asking for that decision to be made properly, in writing. I will tell you what it says.\"", "hearing_day", addHidden=["School — child told a decision will be made and shared with him"]),
    C("Tell him, \"Of course you keep your school, baby,\" because he is nine and it is bedtime.", "hearing_day")]),

 N("hearing_day", 3, "Thursday",
   ["Shelter care is a small room and a fast clock. The judge continues Nolan's care for now — a home without water is a home without water — and confirms the placement with Odessa, with the kinship approval to be completed on a schedule the court says out loud. Mr. Rahal raises the school question on the record, and the judge is plain about its address.",
    "\"School placement is determined by the districts with the agency, on the child's best interest — not by this court today. But hear me: get the request in writing, and bring me the answer at the review. A decision nobody wrote down is a decision nobody can appeal, revisit, or enforce.\" The review is set for Tuesday, October 6, 2026."],
   [C("In the hallway, ask Mr. Rahal: \"So we write. To whom, exactly?\"", "school_call")]),

 N("school_call", 4, "The enrollment packet",
   ["Odessa calls that evening, holding two envelopes. One is the kinship paperwork. The other is from the school district where she lives: an enrollment packet for Nolan, with a friendly cover letter and a start date of next Monday already penciled in. Nobody decided to move Nolan's schooling. The packet is just what a system sends when a child arrives in a new district — momentum, with a return envelope.",
    "\"If I sign it, it's done?\" Odessa asks. \"And if I don't, is he truant?\" Both good questions. The honest answer to the second is no — a child whose school placement is under an open best-interest question is not a truant for staying put — but the packet makes signing feel like the only responsible move in the house."],
   [C("Ask Odessa not to sign anything yet — and put the request in writing yourself tonight: Nolan is to remain in his school of origin while a best-interest determination is made, with all factors considered.", "poc_letter", setFlags=["bidRequested"], addHidden=["School — best-interest determination requested in writing before any transfer"]),
    C("Let Odessa sign. A school is a school, the packet looks official, and fighting the district feels like one fight too many.", "transfer_path")]),

 N("transfer_path", 5, "Signed, and not final",
   ["The packet goes back in the mail, and the receiving school schedules Nolan's first day for Monday. It is only when Mr. Rahal hears about it — from you, two days later, mentioned as an errand already run — that the room changes temperature.",
    "\"Signed is not the same as decided,\" he says. \"No determination was ever made; a form was processed. You can still ask, in writing, for the determination to actually happen — the factors looked at, the answer written down. It is harder to ask a system to undo than to pause. It is not impossible, and Monday has not happened yet.\""],
   [C("Ask anyway — in writing, tonight, copies kept. Undoing is slower than pausing, and you will pay the difference in days, not in rights.", "poc_letter", setFlags=["bidRequested"], addHidden=["School — determination requested after enrollment packet signed; transfer not yet effected"]),
    C("Let it ride. Nolan will adjust; children do. Spend your fight on the water, the landlord, the case.", "review_prep")]),

 N("poc_letter", 6, "The point of contact",
   ["Your letter goes to two addresses, because Mr. Rahal insists the system has two hands. To the agency: Ms. Iversen. To the school district of origin: its foster care point of contact — a named role the district must be able to produce, because federal law requires districts to collaborate with the child welfare agency, designate a point of contact, and keep clear written procedures for how a child in foster care gets to their school of origin when staying is in their best interest. (20 U.S.C. § 6312(c)(5))",
    "The point of contact has a name — Mr. Clayton — and, to his credit, a phone manner like a man who has been waiting for someone to use the procedure on paper. \"We hold enrollment as-is while the determination is pending,\" he says. \"There's a meeting. You should be in it. You are a factor — proximity and the current setting both are.\" (20 U.S.C. § 6311(g)(1)(E)(i))"],
   [C("Ask for the meeting date in writing, and for Mrs. Pavlik — Nolan's teacher — to be heard in it, by phone if she cannot come.", "bid_meeting", setFlags=["pocEngaged"]),
    C("Take the verbal assurance and save the postage. He sounded like he meant it.", "bid_meeting", cash=-4)]),

 N("bid_meeting", 9, "All the factors",
   ["The meeting is a district office, a speakerphone, and a one-page form with more honesty in it than you expected. Factor by factor, the way the federal standard lists the considerations: the appropriateness of the current educational setting — Mrs. Pavlik, on the phone, describes Nolan's reading group, his IEP-free but carefully built support plan, the corner he has been promised in October. Proximity: Odessa's house is twenty-five minutes from the school, on a route a bus already runs most of.",
    "Then the form's last box: transportation. Staying is only real if somebody drives it. The district's written procedures exist for exactly this box: transportation to the school of origin is to be provided and arranged under them, with additional costs handled by reimbursement, by the district, or shared. (20 U.S.C. § 6312(c)(5)(B)) The box sits empty while everyone looks at it."],
   [C("Fill the box with a plan, out loud and then in writing: Odessa drives mornings on her way to work; the district's existing route covers afternoons with one added stop; you cover the two Friday gaps. Ask that the plan be written into the determination.", "records_node", setFlags=["transportPlan"]),
    C("Wait for the professionals to solve the last box among themselves. It is their procedure, after all.", "transport_gap")]),

 N("transport_gap", 10, "In principle",
   ["The meeting ends with the warmest empty phrase in public administration: in principle, everyone agrees Nolan should stay. In principle does not drive a car at 7:40 in the morning. Mr. Clayton closes his folder and says the determination will be finalized when the transportation piece is confirmed — and you can hear the default, patient as water, waiting to resume.",
    "You have two days of the system's attention left before the file cools. The proposal that fills the box is four sentences long. You wrote a harder letter than this the night Nolan was taken."],
   [C("Write the four sentences and send them to Mr. Clayton and Ms. Iversen tonight: who drives, which days, what it costs, who pays which share.", "records_node", setFlags=["transportPlan"], cash=-12, note="The $12 is a gas card for Odessa, because a plan that costs your sister money in silence is a plan with an expiration date."),
    C("Let the principle stand and hope the box fills itself before the review.", "review_prep")]),

 N("records_node", 12, "Read what they wrote",
   ["Mr. Rahal's last instruction before the review is the one he gives in every case, in the same flat tone: \"Ask for the record.\" Under Pennsylvania's regulation, the agency's case record is to be released on request (55 Pa. Code § 3130.44(d)) — and this case's record now contains your letter, the meeting notes, and whatever the school correspondence says about your son when you are not in the room.",
    "What the record shows, when it comes, is mostly kind and entirely useful: your request, dated. The meeting, minuted. Mrs. Pavlik's sentence about the reading corner, quoted. Paper that agrees with you is still paper you should hold before a judge reads it."],
   [C("Sign the written request and send it today, copies of everything in your own folder.", "trial_run", setFlags=["recordsRequested"], addHidden=["Record — agency record requested in writing, including school correspondence"]),
    C("Skip it. The meeting went well; paper about paper feels like gilding.", "trial_run")]),

 N("trial_run", 15, "A dry run at dawn",
   ["Odessa does the route once on a Sunday, stopwatch on the dash out of pure auntie spite: twenty-three minutes, door to door, arriving with four minutes of margin and one opinion — \"It works if nobody's sick and nobody's late, same as every plan God ever made.\" Nolan rides along in his pajamas, timing the turns, and delivers the review that matters most to him: the bus he would have taken passes them at the corner, going his school's way.",
    "The trial run goes in the folder as a single dated page: route, time, margin, driver. It is the least legal document in the packet and, if the transportation plan is ever questioned, the most persuasive one."],
   [C("File the page. Tuesday's judge reads paper, but she also reads the smell of paper that has been somewhere.", "review_prep")]),

 N("review_prep", 18, "The folder, squared",
   ["The review packet assembles itself the way good packets do: the judge's Thursday words, your dated request, the determination meeting's notes, the transportation plan in four sentences, Mrs. Pavlik's line about October. Mr. Rahal reads it once and says the sentence lawyers say when the work is done: \"Now the hearing is about the documents. Hearings about documents are the kind we can win.\"",
    "The water, for the record, is back on — the landlord's pipes, the city's date, your receipts in the folder's back pocket. The case is not over. But the review on Tuesday is about one question the system tried to answer by envelope: where does Nolan go to school?"],
   [C("Sleep. Tuesday is a school day, whichever school it is.", "review_day")]),

 N("review_day", 22, "Tuesday, October 6",
   ["The review is short, the way hearings are when the paper has already argued. The agency reports the kinship approval complete and the water restored. Then the judge turns to the school question — the one she told you, in a hallway's worth of words, to bring back to her in writing.",
    "What happens next is decided by what is actually in front of her."],
   [C("The file holds a written best-interest determination, made on all the factors, with a transportation plan inside it — and your dated request that started the whole thing.", "end_same_bus", requiresFlags=["bidRequested", "transportPlan"]),
    C("The file holds a transfer, processed by packet — or a principle, unwritten, with the last box empty.", "end_new_desk")]),

 E("end_same_bus", 22, "Ending — Same Bus, Same School",
   ["Nolan stays at his school of origin. The written determination says why, in the statute's own factors: the setting is appropriate — a teacher who knows his reading, a class mid-year, a corner with his name effectively on it — and the proximity is workable, because the transportation plan inside the same document says who drives, which days, and who pays which share: Odessa's mornings, the district route's afternoons, your Fridays. (20 U.S.C. § 6311(g)(1)(E)(i); § 6312(c)(5)(B)) He rides the bus that crosses the line, twice a day, and the line loses.",
    "Read what actually won this. Not a speech — a sequence. The request for a determination was made in writing before the default could harden (and even after the packet was signed, asking still worked, because signed is not decided). The district's point of contact was found and used. The transportation box — the place school-stability rights go to die — was filled with a plan instead of a hope. And the case record was requested (55 Pa. Code § 3130.44(d)), so the review argued from documents everyone had read.",
    "The case itself continues: Nolan is still in care, at Odessa's, and the road home runs through the plan, the visits, the next review. School was never the whole case. It was the part of the case that would have been lost by envelope, in a week when you had bigger griefs — which is exactly when these parts are always lost. What no strategy controls: a different determination on the same factors, a bus route redrawn in January, a judge less patient with paper. What this one controlled: the decision was made on purpose, in writing, where you could see it."]),

 E("end_new_desk", 22, "Ending — A New Desk in October (partial)",
   ["Nolan starts at the school near Odessa's on a Monday in October, with a kind teacher, a borrowed cubby, and a reading assessment scheduled to rediscover what Mrs. Pavlik could have told them in one phone call. He will be fine, the way children are fine — at a price adults keep the receipt for. His records followed him the following week; the law at least requires the enrolling school to reach back for them at once. (20 U.S.C. § 6311(g)(1)(E)(iii)) Nobody did anything wrong in a way you could point to. That is the point of this ending: nothing was decided, so everything was.",
    "Read the debrief honestly. The right existed the whole time: a child in foster care remains in the school of origin unless a determination — made on all factors relating to best interest, including the appropriateness of the current setting and proximity — says otherwise. (20 U.S.C. § 6311(g)(1)(E)(i)) Districts must keep written transportation procedures for exactly this, with the cost question answered by reimbursement, district payment, or sharing. (20 U.S.C. § 6312(c)(5)(B)) What was missing was never the law. It was the dated, written request that forces a determination to happen — and, at the meeting, a plan in the transportation box instead of a principle.",
    "This ending is a partial one, and it is not sealed. Determinations can be revisited when facts change; a request can be made at the next review as well as the first; the record — yours to request under 55 Pa. Code § 3130.44(d) — will show what was and was not decided, which is where a second attempt starts. Nolan's case continues, and so does his schooling. The lesson the scenario exists to teach is only about timing: in the first ninety days, the defaults are loaded and moving, and paper is how a parent steps in front of them."]),
]
emit(117, s117_meta, s117, S, "child removal, a kinship placement, and a school-transfer fight. No graphic content.")

# ============================================================ S118 (Hard)
S = date(2026, 10, 5)
assert fmt(S) == "Monday, October 5, 2026"
CONSENT = S + timedelta(days=9)                 # Wed Oct 14, 2026
assert fmt(CONSENT) == "Wednesday, October 14, 2026"
assert fmt(CONSENT + timedelta(days=60)) == "Sunday, December 13, 2026"   # federal 60-day date
ER = S + timedelta(days=66)
assert fmt(ER) == "Thursday, December 10, 2026"                            # report issued, inside the window
assert fmt(S + timedelta(days=73)) == "Thursday, December 17, 2026"        # permanency hearing

s118_meta = {
    "title": "The First 90 Days",
    "subtitle": "Scenario 118 — Sixty Days from a Signature (a fictional composite)",
    "startDateISO": "2026-10-05",
    "startNode": "start",
    "startCash": 150,
    "tier": "Hard",
    "summary": "You are Darnell. Your son Khalil, eleven, has been in foster care four months, and his new school reads his frustration as defiance. You have asked twice, out loud, for him to be evaluated. Out loud is where requests go to disappear.",
}

s118 = [
 N("start", 0, "The suspension notice",
   ["The call comes from Mrs. Greer, Khalil's foster mother, who delivers school news the way she delivers everything — completely, and slightly out of breath. Khalil is suspended for two days. A reading passage, a worksheet he could not start, a chair that ended up on its side. Eleven years old, four months into foster care, in a school where nobody yet knows that he reads two years below the room he sits in — because nobody has ever tested where he reads at all.",
    "\"I told them at the meeting in September,\" you say, \"and I told the counselor on the phone. I asked them to evaluate him.\" Mrs. Greer is gentle: \"Did you ever write it down, hon?\" You did not. You asked the way parents ask — out loud, in rooms, trusting the room."],
   [C("Call your lawyer before you call the school. Asking is about to become a discipline.", "lawyer118")]),

 N("lawyer118", 1, "Asking, in writing",
   ["Ms. Ashby has a whiteboard habit: she writes the rule before she discusses the case. First line: either a parent or the school may initiate a request for an initial evaluation to find out whether a child is a child with a disability. (34 C.F.R. § 300.301(b)) Your September asks were real. They were also unwritten, undated, and — she says this without cruelty — unprovable.",
    "Second line: once the school has your signed consent, the evaluation must be conducted within 60 days of receiving it — or within the timeframe your state establishes, if the state has set its own. (34 C.F.R. § 300.301(c)(1)) \"Two clocks,\" Ms. Ashby says. \"The request starts nothing until it's paper. The consent starts the clock. We do both, dated, with copies.\""],
   [C("Draft the letter at her table: dated, signed, one page — request for a full initial evaluation, and a request for the consent form.", "consent_form", setFlags=["writtenRequest"], addHidden=["Education — initial evaluation requested by parent in writing, dated"]),
    C("Call the school counselor once more first — a relationship is worth one more conversation before it becomes correspondence.", "phone_loop")]),

 N("phone_loop", 2, "Noted",
   ["The counselor is warm, busy, and fluent in the dialect of the unrecorded. She will absolutely raise it with the team. She remembers your September call — she thinks. Something will be noted. The call ends with everyone thanked and nothing dated, and Khalil's file acquires no new page.",
    "That evening Mrs. Greer sets a plate down and says the thing foster mothers are positioned to say: \"Paper, Darnell. The school runs on it, the agency runs on it. Give them paper.\""],
   [C("Write the letter. Date it, sign it, keep a copy, send it so it leaves a trail.", "consent_form", setFlags=["writtenRequest"], addHidden=["Education — initial evaluation requested by parent in writing, dated, after two undocumented verbal requests"]),
    C("Give the team meeting a chance to happen. Chasing paper feels like accusing people who mean well.", "drift")]),

 N("consent_form", 9, "The consent form",
   ["The consent form arrives through Mrs. Greer on Wednesday, October 14, 2026 — the school moved at the speed schools move when a request exists in writing. It is one page: evaluation areas, a signature line, and a date line that matters more than the rest of the document combined. The day this signature is received starts the federal clock: the evaluation conducted within 60 days of consent, or within the state's own timeframe if it sets one. (34 C.F.R. § 300.301(c)(1)) Counted on the federal measure, day sixty is Sunday, December 13, 2026.",
    "Your permanency hearing is Thursday, December 17, 2026. Signed today, the evaluation can land before it. Signed next week, it cannot. The form does not know about your hearing. The calendar does."],
   [C("Sign it today, date it today, hand it back through Mrs. Greer today — and photograph your copy.", "district_reply", setFlags=["consentSigned"], addHidden=["Education — consent signed and returned the day the form arrived; clock running"]),
    C("Sign it next week, after payday and the visit and the shift swap settle. A week is a week.", "district_reply", setFlags=["consentSigned", "consentLate"], addHidden=["Education — consent returned a week after the form arrived; clock started late"])]),

 N("district_reply", 12, "Received, and stamped",
   ["The district's acknowledgment comes back with the rarest ornament in public administration: a received stamp, with a date on it. Whatever else this case becomes, the evaluation now has a paper birthday, and a paper deadline, and both are in your folder rather than in your memory of a phone call.",
    "Ms. Ashby adds the second document to the folder's front: a short letter from you to the evaluation team — your own observations, dated, in your words. What Khalil reads at your visits. Where the frustration starts. The team is required to build the evaluation out of more than its own tests; a parent's dated notes are part of the material a real evaluation is made from, and more to the point, they are the part only you can supply."],
   [C("Write the observations letter tonight: three visits, two books, one worksheet, all dated.", "visit_notes", setFlags=["parentInput"]),
    C("Let the testers test. Your notes are a father's worry, not data.", "eval_track")]),

 N("visit_notes", 16, "What a father sees",
   ["The letter writes itself out of the visit notebook you have kept since June: the graphic novel he reads fluently because the pictures carry the plot; the chapter book he 'forgets' at the bottom of his bag; the homework sheet he crumpled in August with the sentence you have thought about since — \"I'm not doing the baby page.\"",
    "It goes to the evaluation team, the school counselor, and your folder. Somewhere across town, a file that said only *defiant* gains a dimension."],
   [C("Now ask for the other file — the agency's — so the court reads the same dates you do.", "records118")]),

 N("eval_track", 16, "The quiet weeks",
   ["Testing weeks look like nothing from the outside: a nice professional, a quiet room, a boy who reports only that \"the lady let me read the comic ones and the hard ones.\" The evaluation is moving through its machinery at the speed the clock allows, and there is nothing for a father to do but attend visits and not become a rumor in his own case.",
    "Ms. Ashby uses the quiet for the second file. The agency's case record — its school correspondence included — is releasable to you on request. (55 Pa. Code § 3130.44(d)) What the agency's file says about September matters: it is where your two spoken requests went, or didn't."],
   [C("Sign the written record request and send it, dated, copies kept.", "records118", setFlags=["recordsRequested"], addHidden=["Record — agency record requested in writing, including school correspondence"]),
    C("Leave the agency file alone. The evaluation is the fight; don't open a second front.", "testing_day2")]),

 N("records118", 24, "What September became",
   ["The record arrives in a fat envelope, and page order tells the story before you read a word. Your September meeting: minuted as *father expressed concerns re: behavior expectations*. Your September phone call: *parent called re: homework*. The word evaluation appears in the agency's file for the first time on the page that copies your October letter.",
    "It would be easy to read this as malice. Ms. Ashby reads it as weather: \"Spoken words condense. Written words precipitate. Your October letter is the first thing in this file that can start a clock, and it did. Keep the envelope — the permanency hearing is where dates go to be believed.\""],
   [C("Put the envelope's key pages in the hearing packet, in date order, with the received stamp on top.", "testing_day2", setFlags=["recordsRequested"], addHidden=["Record — agency file shows verbal evaluation requests recorded as general concerns; written request is the first clock-starting document"])]),

 N("testing_day2", 38, "The hard ones",
   ["Khalil emerges from the second testing session with a sticker and a review: \"She said I don't have to read out loud if I don't want. Can all school be like that?\" The evaluation is doing the thing evaluations exist to do — finding the shape of the problem under the behavior — and the behavior, at school, has already begun to change around the edges, because one adult in that building now has a hypothesis that is not *defiance*.",
    "There are five weeks left on the federal measure of the clock. The report, when it comes, will either be a document the December hearing reads — or a rumor the December hearing hears about."],
   [C("Send the evaluator a dated thank-you with one factual addition: the visit-notebook page about the 'baby page' worksheet.", "khalil_talk", cash=-3),
    C("Wait for the machinery. It is moving; don't lean on it.", "khalil_talk")]),

 N("khalil_talk", 50, "His side of the worksheet",
   ["At the visit, Khalil explains the chair. Not excuses — mechanics. \"The words swim when everybody's watching. Then Jaylen laughs, then I'm already mad before I know I'm mad.\" He says the testing lady let him read in a room with a door, and he read four pages without swimming.",
    "You write it down in front of him, dated, in his words — and he watches you do it, and something about being transcribed, accurately, by his father, lands on him like a hand on a shoulder. Whether or not this page ever reaches a file, it has already done one piece of its work."],
   [C("Ask his permission to include his words in your letter to the IEP team, if a team is convened.", "waiting", setFlags=["childVoice"]),
    C("Keep the page in the notebook. Some paper is for the family, not the file.", "waiting")]),

 N("waiting", 58, "The last quiet week",
   ["December opens with the evaluation in its final week on the federal count. The agency's report for the permanency hearing is already being drafted somewhere — from the file as it stands, which means, as of tonight, it says what agency reports say in the absence of an evaluation: *school functioning remains a concern; father's advocacy noted*.",
    "Everything now depends on a date arithmetic problem you solved in October, with a signature. Either the report exists before the hearing, or the hearing is told about a report."],
   [C("Call Ms. Ashby and build the hearing packet either way: request, consent stamp, clock, and whatever the school produces.", "ashby_clock")]),

 N("ashby_clock", 62, "Count it forward",
   ["Ms. Ashby does the arithmetic on the whiteboard one final time, in marker, the way she did in October. Consent received: Wednesday, October 14, 2026. The federal measure: the evaluation conducted within 60 days of that receipt, or within the state's own timeframe if the state sets one. (34 C.F.R. § 300.301(c)(1)) Day sixty: Sunday, December 13, 2026. The hearing: Thursday, December 17.",
    "\"Notice what the arithmetic does not contain,\" she says. \"Effort. Sympathy. How busy the school was. A clock is the only participant in this case that cannot be lobbied — which is why we started it early, on paper, where everyone can see it running.\""],
   [C("Photograph the whiteboard for the folder. Then go see your son.", "report_fork")]),

 N("report_fork", 66, "December 10",
   ["Thursday, December 10, 2026. What the school issues today depends, with total precision, on when a one-page form was signed in October — on whether day sixty falls before the hearing or after it."],
   [C("The report is issued today — inside the window the signature bought.", "report_ready", requiresNoFlags=["consentLate"]),
    C("The testing is done; the written report is not — its window runs past the hearing.", "report_pending", requiresFlags=["consentLate"])]),

 N("report_ready", 66, "The report",
   ["The evaluation report is eleven pages, and its finding is a sentence you read four times: Khalil has a specific learning disability in basic reading — the words swim for a documented, testable, teachable reason. He is eligible. An IEP team will be convened, and services will be written into a plan with the force of a program behind it.",
    "The chair, the worksheet, the 'baby page' — all of it re-reads, in the report's level light, as a boy asking for help in the only dialect he had. You were right in September. The difference between September and now is not rightness. It is paper."],
   [C("Convened means scheduled — ask for the IEP meeting date in writing, and for the report to go to the agency and the court packet today.", "iep_meeting", setFlags=["iepConvened"]),
    C("Read it once more at the kitchen table. Some victories deserve a minute before they become exhibits.", "iep_meeting")]),

 N("iep_meeting", 71, "The team",
   ["The IEP meeting is a school table with your chair kept for you — you attend by phone from a break room, on speaker, with Mrs. Greer in the room itself, and it works anyway, because the report does the talking. Reading services, four sessions a week. A plan for the frustration moments that is a plan, not a punishment. Your observations letter is in the team's folder; Khalil's sentence about the swimming words is quoted in the present-levels page, with his permission, in quotation marks.",
    "Ms. Ashby's remaining task is plumbing: the signed IEP and the evaluation report go into the permanency packet, so that on Thursday the judge reads a school plan with dates on it — not a concern with adjectives on it."],
   [C("Sign the IEP, keep your copy, and confirm the packet copy went to the agency in writing.", "hearing_prep", setFlags=["packetFiled"], cash=-6),
    C("Sign, and trust the school to forward its own paperwork to the agency.", "hearing_prep", setFlags=["packetFiled"], note="Mrs. Greer confirms the packet copy reached the agency — trust, verified once, in writing.")]),

 N("report_pending", 66, "Testing done, report not",
   ["The testing is complete — two sessions, a file of protocols — but the written report is still inside the school's window, because the window started a week later than it could have. The evaluator is apologetic and precise: the report will issue the week after the permanency hearing, comfortably inside the deadline the October signature actually set.",
    "Ms. Ashby is blunter. \"We will tell the court the evaluation exists and what its clock says. Courts can continue a question; they cannot find facts from a report that doesn't exist yet. We ask for a step, not a leap — and we bring the consent stamp, so the court can see exactly whose week this was.\""],
   [C("Build the packet around the stamp: request, consent, clock, testing log — and a written ask for a dated step at the next review.", "hearing_prep")]),

 N("hearing_prep", 72, "The packet",
   ["The packet is thin or thick depending on the autumn you chose: a father's dated request; a consent form with a received stamp; a sixty-day count; an evaluation report or the space where it will be; an IEP with services and dates, or a testing log and a promise. Ms. Ashby arranges what exists in date order, the way judges forgive everything except confusion.",
    "\"Tomorrow the court makes the permanency determinations — placement's necessity, your compliance, your progress, and the agency's efforts. (42 Pa.C.S. § 6351(f)) School is about to become one of the places those determinations are read from. Let's make sure it's read accurately.\""],
   [C("Sleep badly, arrive early, bring the folder.", "outcome118")]),

 N("drift", 6, "The team will meet",
   ["Weeks pass at the speed of other people's priorities. The team meeting is scheduled, then folded into a larger meeting, then described as having happened — in a corridor, between other agenda items, with a conclusion nobody writes down: *continue to monitor*. Khalil's reading does not improve under monitoring. His behavior record, which is the only document growing, grows.",
    "October becomes November. The suspension count reaches three. Each one is documented, dated, stamped, and filed — the school's paperwork machinery works beautifully, aimed at the wrong target."],
   [C("At the November visit, say it plainly to Khalil: \"I should have written the letter. I'm writing it now.\"", "late_letter", setFlags=["writtenRequest"]),
    C("Keep trusting the corridor. The permanency hearing is coming, and surely the court will ask why nobody evaluated him.", "suspension3")]),

 N("late_letter", 40, "A letter, late",
   ["The letter goes in November — dated, signed, correct in every particular except its relationship to the calendar. The school responds properly; a consent form follows; testing will be scheduled. Every deadline the letter can start, it starts — six weeks after it could have, with a permanency hearing five weeks away and a sixty-day clock that will not be hurried by remorse.",
    "Ms. Ashby files the letter and the consent stamp where the court will see them, and says the thing she is paid to say at exactly this pitch: \"Late paper is still paper. It converts your December from a verdict into a progress report. But it is a conversion, not an erasure.\""],
   [C("Sign the consent the day it arrives — the lesson has been paid for once already.", "hearing_prep", setFlags=["consentSigned", "consentLate"])]),

 N("suspension3", 45, "The third suspension",
   ["The third suspension comes with a new document: a behavior plan, written by the school, proposing consequences in ascending order for a boy whose core difficulty has still never been measured. The agency's court report will quote it. Reports like quoting plans; plans sound like somebody is handling it.",
    "At the December permanency hearing, the question *why has this child never been evaluated* will be asked in a room where the answer *his father requested it twice* exists only in your memory — and memory, Ms. Ashby told you in October, is not a page the court can turn to."],
   [C("Arrive at the hearing with the truth and no exhibits, and learn what that combination is worth.", "hearing_prep")]),

 N("outcome118", 73, "Thursday, December 17",
   ["The permanency hearing opens with the agency's report, and the school chapter is read aloud — in whichever version your autumn wrote. The judge's determinations are the statute's: whether placement remains necessary, whether the plan has been complied with, what progress has been made toward the circumstances that brought Khalil here, and whether reasonable efforts were made to finalize the plan. (42 Pa.C.S. § 6351(f)(1), (2), (3), (5.1))",
    "Into those determinations now falls the education record — the whole of it, or the hole where it should be."],
   [C("The record holds a dated request, a consent signed the day it arrived, an evaluation completed inside its window, an IEP with services running, and a father's observations in the file — advocacy with stamps on it.", "end_evaluated", requiresFlags=["writtenRequest", "consentSigned", "packetFiled"]),
    C("The record holds an evaluation that exists but a report that doesn't — a clock started a week late, ticking past today's hearing.", "end_late", requiresFlags=["consentLate"]),
    C("The record holds suspensions, a behavior plan, and a father's unprovable memory of asking.", "end_discipline")]),

 E("end_evaluated", 73, "Ending — Evaluated, and Heard",
   ["The findings come in the statute's order, and the school chapter does real work in them. On progress toward alleviating the circumstances of placement (42 Pa.C.S. § 6351(f)(3)), the court cites the evaluation itself: a father who identified his son's core difficulty, pursued it through the correct machinery, in writing, until the machinery produced services — is a circumstance of this case changing in front of the court. The order is a stepped return: expanded visits now, Khalil home by spring if the steps hold, the IEP traveling with him to whichever school serves your neighborhood, its services uninterrupted by the move.",
    "Hold the honest shape of this win. The evaluation did not reunify this family; the court did, on a record. What the paper did was convert *father's concerns* — the file's September phrase — into findings a judge could act on: a dated request under 34 C.F.R. § 300.301(b), a consent whose stamp started the 60-day clock in § 300.301(c)(1), a report inside that window, a plan with services and dates. The agency record you requested (55 Pa. Code § 3130.44(d)) is what let the hearing argue from the file's own pages about when you asked, instead of from anyone's recollection.",
    "What no strategy controls: the evaluator's finding itself — a report can come back *no disability found*, and this route's honesty depends on saying so. A different judge could weigh the same packet and order a slower step. What the strategy controlled was narrower and real: when the system finally looked at Khalil, it looked because his father had asked in the only dialect the system files — and the looking happened in time to matter."]),

 E("end_late", 73, "Ending — The Report Arrives Late (partial)",
   ["The court does what courts do with a clock that is still running: it continues the question. The evaluation is credited as underway — the consent stamp is in the packet, the testing log is real, the evaluator's date is written into the order — and the stepped return is deferred to a review set for the spring, when the report and the IEP will exist as documents instead of as expectations. Khalil stays with Mrs. Greer. Nothing was denied. Everything was postponed, by the width of one week in October.",
    "Read the arithmetic without flinching. The federal measure gives the school 60 days from consent, or the state's own timeframe if it sets one. (34 C.F.R. § 300.301(c)(1)) A consent signed the day the form arrived puts day sixty on Sunday, December 13, 2026 — before the hearing. A consent signed a week later puts the report's deadline after it, and a permanency hearing cannot find facts from a report that does not exist yet, however sympathetic the room. The request letter suffered the same physics: the November version was a fine letter. The October version would have been a finding.",
    "This ending is partial, and it is genuinely recoverable — more recoverable than most. The report will issue; the IEP will be written; the spring review will read a complete school file, and the record you can request under 55 Pa. Code § 3130.44(d) will show a father whose paper, once he learned its price, never ran late again. The scenario's lesson is not that a week is fatal. It is that in this system a week is a unit of your child's life, and the calendar does not round."]),

 E("end_discipline", 73, "Ending — Discipline Instead",
   ["The hearing reads the school chapter the school wrote: three suspensions, a behavior plan, *functioning remains a concern*. Nobody in the room is lying. The documents are accurate, stamped, and entirely about a boy whose reading was never measured — because the request to measure it lives in two memories and no file. The court continues placement, notes the behavior plan as the school's response, and the permanency determinations are made from a record in which *defiance* has paperwork and *disability* has a father's say-so. (42 Pa.C.S. § 6351(f))",
    "The debrief owes you the unflinching version. The right was never obscure: a parent may initiate a request for an initial evaluation. (34 C.F.R. § 300.301(b)) The machinery was never unwilling: when the request finally exists in writing, schools produce consent forms in days. What failed was the dialect. September's asks were spoken in rooms that minuted them as *concerns* and *homework* — and a system that runs on paper cannot be blamed, in any way a court can act on, for failing to file what it was never handed.",
    "It is not over — evaluations can be requested in December as well as September, and this scenario's worst ending is still only a season, not a sentence. But notice what the delay cost beyond time: the behavior record written in the evaluation's absence will now be quoted in rooms for years, long after a report explains it. First drafts are sticky. Write yours."]),
]
emit(118, s118_meta, s118, S, "a child in foster care, school discipline, and a special-education evaluation fight. No graphic content.")
print("done")
