#!/usr/bin/env python3
"""Generate scenarios 119-120 (Wave 2, Batch 9: Education & Medical).
Fictional composites only."""
import sys
sys.path.insert(0, "/home/hatch/workspace/your_files/tacticwatch-game")
from batchN_lib import N, C, E, emit, fmt
from datetime import date, timedelta

# ============================================================ S119 (Hard)
S = date(2026, 11, 2)
assert fmt(S) == "Monday, November 2, 2026"
assert fmt(S + timedelta(days=31)) == "Thursday, December 3, 2026"   # review hearing
assert fmt(S + timedelta(days=36)) == "Tuesday, December 8, 2026"    # surgery, win path

s119_meta = {
    "title": "The First 90 Days",
    "subtitle": "Scenario 119 — Two Signatures (a fictional composite)",
    "startDateISO": "2026-11-02",
    "startNode": "start",
    "startCash": 130,
    "tier": "Hard",
    "summary": "You are Kavita Raman. Your daughter Navya, six, is in foster care while you recover and rebuild. She needs dental surgery under anesthesia — and the consent form for it was sent to everyone except you.",
}

s119 = [
 N("start", 0, "The tooth",
   ["Navya mentions it at the visit the way six-year-olds file major reports — between the juice box and the drawing. \"The dentist lady counted my teeth and one is sick. They're going to fix it when I'm asleep. Mrs. Yuen has the paper.\" She is not frightened. She is, if anything, pleased to have news.",
    "You are frightened enough for both of you. Not by dentistry — by the geography of the information. A surgery, however small, however routine, has been scheduled into existence around your daughter, and the first draft of it reached you as a child's visit-table announcement."],
   [C("Ask Mrs. Yuen about the paper tonight — calmly, and with a notebook open.", "how_we_got_here")]),

 N("how_we_got_here", 0, "How Navya got here",
   ["The short version, because the case deserves accuracy more than it deserves length: in August you were hospitalized for nine days with an infection that had been misread for a month, and there was no one — no one the county could verify that week — to take Navya. She went to Mrs. Yuen's, ten minutes from your building. Your case plan is a recovery plan: medical follow-ups, a parenting course you are halfway through and quietly acing, and visits that have never once been missed.",
    "Nothing in the plan says you stopped being Navya's mother. Papers, however, have begun to route around you as if it did."],
   [C("Call Mrs. Yuen.", "yuen_call")]),

 N("yuen_call", 1, "Mrs. Yuen has the paper",
   ["Mrs. Yuen answers on the second ring and, to her lasting credit, does not enjoy her part in this. The dentist's office handed her a packet at Navya's cleaning: proposed treatment — extractions and crowns under general anesthesia — and a consent form with a signature line. \"I told them I keep her bed, not her decisions,\" she says. \"They said sign anyway, it's standard. I haven't. It sits on my fridge under a magnet shaped like a strawberry, and it has bothered me every day.\"",
    "The dentist is a Dr. Sorrel. The surgery is not scheduled yet — the packet is what starts scheduling. Nothing has been decided except, apparently, who was worth sending the paper to."],
   [C("Thank her — genuinely — and ask her to keep that form unsigned and on that fridge until a court has spoken. Then call your lawyer.", "lawyer119")]),

 N("lawyer119", 2, "The map of who signs",
   ["Mr. Petrillo draws the honest map, and it has more weather in it than law. For a child in placement, consent runs on rails laid by court orders, agency practice, and the forms providers keep in drawers. Routine care and genuine emergencies move fast, through whoever is standing there — as they should. A scheduled surgery under anesthesia is neither, and it is exactly the class of decision a parent can ask the court to structure in advance.",
    "\"Your review is Thursday, December 3,\" he says. \"Courts can write the arrangement into an order: who consents to what, who gets notice, who may be present. What we cannot do is win that order with surprise and indignation. We win it with a paper trail showing you asked, reasonably, in writing, in time — and with a plan that is better than the default. Also: ask for the agency's record. (55 Pa. Code § 3130.44(d)) I want to see exactly what was sent to whom, and what the file thinks a mother is for.\""],
   [C("Write to the agency today: notice to you before any non-emergency procedure, your consent or a court's for scheduled surgery, and your presence at Navya's side — in writing, copies kept.", "dentist_call", setFlags=["noticeAsked"], addHidden=["Medical — parent requested written notice and consent role for non-emergency procedures"]),
    C("Call the dentist's office first. Forms live there; maybe the fix does too.", "dentist_call")]),

 N("dentist_call", 3, "The scheduling desk",
   ["Dr. Sorrel's office is kind and entirely procedural, a combination that explains most of this case. The packet is standard for 'the responsible party.' Scheduling requires a signature; the surgery is elective in timing — a window of weeks, not days — and a second opinion, the coordinator says, is something parents arrange 'all the time, usually the foster parents, honestly.' She offers the sentence that becomes your north star: \"Nothing is on the calendar. Nothing will be, until a signature exists.\"",
    "You ask her to note your name and number in Navya's chart as mother, to be contacted about scheduling. She types while you listen. Whether typing becomes record is a question this whole case keeps asking."],
   [C("Ask her to read back what the chart now says about who gets called.", "visit_teeth", setFlags=["chartNoted"]),
    C("Take the verbal note as done, and turn to the agency letter.", "visit_teeth")]),

 N("visit_teeth", 5, "The sick tooth, examined",
   ["Saturday's visit includes a flashlight inspection, conducted by Navya, of your teeth, followed by her verdict: \"Yours are boring. Mine has a sick one.\" She demonstrates the tooth's location with the seriousness of a tour guide. It does not hurt, she says. It is not an emergency. It is a scheduled thing, moving at the speed of signatures.",
    "In the visit room's plastic chairs you do the arithmetic every parent in this system learns: the review is December 3. A surgery signed by the wrong hand could be over before then. A surgery refused by yours could wait past sense. The middle road — everything in writing, a second opinion, a court order — is not indecision. It is the whole strategy, and it has a calendar."],
   [C("Write the agency letter tonight if you haven't; then walk it through, person by person, until it is answered on paper.", "agency_reply")]),

 N("agency_reply", 6, "Standard packet",
   ["Ms. Franca, the caseworker, replies with professional speed and a phrase that will follow this case to court: the packet sent to the foster home was 'our standard packet.' She confirms nothing is scheduled. She describes the agency's usual arrangement — consent handled at the agency level for treatment the agency's process has approved — in the tone of a woman reading a bus schedule: not unkindly, and without any sense that the schedule could be otherwise.",
    "You take notes. Dated ones. 'Standard' is doing a great deal of work in that reply, and work done by adjectives in October tends to be examined by judges in December."],
   [C("Ask for a meeting — in person, with the file — to go over exactly what the file holds about this surgery and this mother.", "franca_meeting"),
    C("Accept the explanation. The agency handles hundreds of children; their standard is presumably a standard for a reason.", "second_opinion")]),

 N("franca_meeting", 8, "The file, opened",
   ["The meeting is Ms. Franca, a supervisor by speakerphone, and the file — which, opened on the table, tells the story in routing slips. Cleaning: October. Treatment plan: generated. Consent packet: mailed to the foster home, copy to the agency's medical unit. The distribution list has two names on it. Neither is yours. No one in the room defends this as a decision; it is defended, more honestly, as a default.",
    "\"Defaults,\" Mr. Petrillo says later, \"are what orders are for. We are not going to prove anyone meant this. We are going to make it impossible to repeat, in writing, with a judge's signature — which is better.\""],
   [C("Visit the dentist's office in person. You want to see the consent form with your own eyes.", "dentist_office")]),

 N("dentist_office", 9, "The pre-filled line",
   ["The consent form rewards the trip. The signature line is blank, but the line above it — *responsible party* — has been filled in by a careful hand, in advance, with Mrs. Yuen's name. Not maliciously. Pre-emptively, the way forms absorb the shape of the last hundred files. Your daughter's surgery paperwork had a mother's part in it, and the part had been cast before you were told there was a play.",
    "The office manager, to her credit, looks at the form the way you do. She offers to attach your contact sheet to the chart, on top. Paper on top of paper: the whole case, in one gesture."],
   [C("Now the second opinion — a children's dental clinic across town, and no one's standard packet.", "second_opinion")]),

 N("second_opinion", 11, "A second set of eyes",
   ["The children's dental clinic will do a consult: an examination, the existing images, and a written opinion on the treatment plan. It costs time, a bus ride, and the agency's cooperation to get Navya there — cooperation you request in writing, with the reason stated plainly: a second opinion before anesthesia is not an accusation; it is what careful systems do on purpose.",
    "The alternative is to accept Dr. Sorrel's plan whole. It is probably a fine plan. 'Probably fine' is a description of most defaults, and of why they survive."],
   [C("Book the consult, request the transport and the records in writing, and put the date in your folder.", "navya_questions", setFlags=["secondOpinion"], cash=-18, addHidden=["Medical — second opinion on anesthesia treatment plan obtained before consent"]),
    C("Accept the plan. Two dentists agreeing wouldn't change the surgery, only the calendar.", "packet119"),
    C("Refuse the surgery entirely. No signature, no anesthesia, no exceptions — let them take you to court if they want her teeth fixed.", "standoff", setFlags=["surgeryRefused"])]),

 N("navya_questions", 12, "Sleep medicine",
   ["Navya's questions arrive at bedtime, through Mrs. Yuen, by phone: Will it hurt when I'm awake or only when I'm asleep? Can you be there when I fall asleep? Will the sick tooth be in a jar? You answer the ones you can and write down the ones you can't, and it becomes very clear that the right to be present at induction is not, for you, a legal theory. It is the second question on a six-year-old's list.",
    "You add it to the written ask — presence at induction and in recovery — with her questions attached. Adults' paperwork improves when children's questions are stapled to it."],
   [C("Go to the consult with her questions in your pocket and her drawing of the tooth in your folder.", "consult_day")]),

 N("consult_day", 14, "The consult",
   ["The clinic's dentist agrees with Dr. Sorrel's diagnosis and amends the plan: surgery under anesthesia is warranted; two of the three planned extractions can instead be crowned. It is a smaller surgery. The consult letter, written for the chart, adds the sentence you will carry into December: the child's mother is engaged, informed, and — for induction and recovery — *clinically beneficial to have present*.",
    "A second opinion did what second opinions do at their best: it changed the medicine a little and the politics entirely. The plan is now partly yours, because part of it was written in a room you were in."],
   [C("Now pull the paper together — starting with the agency's own file.", "records119")]),

 N("standoff", 16, "The refusal",
   ["Your letter refuses consent for the surgery in terms that leave no handle: no signature will be forthcoming, for this or any procedure, at any time. The effect is immediate and double-edged. Scheduling stops — that part works. But so does everything else: the dentist discharges the plan as 'family declined,' the agency documents a parent 'refusing necessary treatment,' and a tooth that was a scheduled problem becomes, week by week, a ripening one.",
    "Refusal is a wall, and walls protect and imprison with the same stones. Mr. Petrillo, reading your letter, says the thing lawyers say when a client has used a real power at the wrong setting: \"You had a veto-shaped tool. What you needed was a pen.\""],
   [C("Build the December packet anyway — the court will now decide with your refusal in the front of the file.", "packet119")]),

 N("records119", 17, "Read the routing slips",
   ["The agency's record, requested in writing (55 Pa. Code § 3130.44(d)), arrives with the routing slips intact: the cleaning, the treatment plan, the packet's distribution list of two names. It also holds Mrs. Yuen's call note — *foster mother states consent should involve mother* — which means the file knew, in the foster mother's handwriting-adjacent typing, what the file's owner never acted on.",
    "You are not building a scandal. You are building a chronology, and chronologies are what turn a judge's sympathy into a judge's order."],
   [C("Sign nothing you haven't read; file everything you've got; build the ask.", "transport_plan119", setFlags=["recordsRequested"], addHidden=["Record — agency record requested; consent packet distribution list documented"]),
    C("The chronology is in your head well enough. Save the effort for the hearing.", "transport_plan119")]),

 N("transport_plan119", 20, "Who drives, who waits",
   ["Logistics, the unglamorous load-bearing wall of every good intention: if the surgery proceeds, who brings Navya, who signs the day-of forms, who is in the waiting room, who takes her home and watches her that night at Mrs. Yuen's. You write a one-page plan that answers all of it — you present for induction and recovery, Mrs. Yuen for the night after, the agency for the bill and the file copy — and send it to Ms. Franca and the dentist's office alike.",
    "A plan like this does quiet persuasive work: it shows a court that what you are asking for is not a principle but a Tuesday, fully staffed."],
   [C("Ask Mrs. Yuen to add her sentence to it — the foster home's side, in the foster mother's words.", "yuen_support")]),

 N("yuen_support", 22, "The strawberry magnet",
   ["Mrs. Yuen writes four lines and signs them: she was given the form; she did not sign it; she believes the mother should be asked, and present; she will keep the child the night after surgery and follow whatever the court orders. She delivers it to you at the visit with the original consent form still attached to a copy — strawberry magnet sold separately, she says, deadpan, and Navya laughs for a full minute.",
    "The packet is now a small coalition on paper: a mother, a foster mother, a consulting dentist. Coalitions are what 'standard practice' has the hardest time surviving."],
   [C("Assemble the packet for December 3.", "packet119")]),

 N("packet119", 24, "The ask",
   ["The packet, built with Mr. Petrillo, asks the court for an arrangement instead of an apology — orders are made of arrangements. One: routine care and genuine emergencies proceed through the caregiver standing there. Two: scheduled, non-emergency procedures require written notice to you in advance, and your written consent or the court's approval. Three: you may be present at induction and recovery. Four: second-opinion consults are facilitated, not obstructed. Five: any consent paper in Navya's case lists you on its distribution, by name.",
    "It is four pages. It accuses nobody. It simply proposes that a six-year-old's medical life have a mother's name in its routing — permanently, in an order, where defaults cannot quietly edit it out."],
   [C("Serve the packet and wait for the agency's answer in its court report.", "objection")]),

 N("objection", 27, "Streamlined",
   ["The agency's report for the review recommends the opposite arrangement, in one efficient word: consent for Navya's treatment should be *streamlined* to the agency, to avoid 'delays attendant on multi-party consent processes.' Attached: nothing about your letters. Your notice request is not mentioned. Your second opinion — if you obtained one — is not mentioned. The report reads as if December's question had been authored by the standard packet itself.",
    "Mr. Petrillo is almost pleased. \"A report that ignores the file invites the court to read the file. We will help the court do that — in writing, with tabs.\""],
   [C("File a written response: the chronology, the routing slips, the consult letter, Mrs. Yuen's four lines — tabbed, dated, short.", "gal_call", setFlags=["responseFiled"], cash=-9),
    C("Save it for oral argument. Judges read enough paper; your voice in the room will carry it.", "gal_call")]),

 N("gal_call", 29, "The other lawyer",
   ["Navya's guardian ad litem calls two days before the hearing — a short call with a long shadow. She has read the file, including, this time, your response if you filed one. Her position is forming around the child's interests rather than either institution's convenience, and a six-year-old's bedtime questions — which she has now seen, because somebody stapled them to the paperwork — feature in it.",
    "\"For what it's worth,\" she says, \"courts write consent orders like yours more often than agencies admit. They just write them one case at a time, for the parents who show up with paper.\""],
   [C("Sleep. Tomorrow the question is asked in the room where answers become orders.", "night_before119")]),

 N("night_before119", 30, "The night before",
   ["You lay out the folder, the chronology, the drawing of the tooth. The case underneath this case — your recovery, your course, your unmissed visits — is in good order, and tomorrow's determinations will say so. But tomorrow is really about a narrower thing, small enough to fit on a consent form: whether the system that holds your daughter's bed also gets to hold, unexamined, her signature lines.",
    "You have done the thing this game keeps insisting on. You asked, in writing, early, with copies — and you built a better plan instead of only objecting to theirs."],
   [C("Go to court.", "hearing119")]),

 N("hearing119", 31, "Thursday, December 3",
   ["The review proceeds through the statute's determinations — placement's continuing necessity, your compliance, your progress, the agency's efforts (42 Pa.C.S. § 6351(f)(1), (2), (3), (5.1)) — and your case is found, in the flat language that means everything, to be on track. Then the court reaches the medical question, on a record that contains either a chronology or a silence.",
    "Consent is decided by what the file can prove about who asked, who answered, and what the child needs. The judge turns the packet's pages."],
   [C("The file holds a mother who asked in writing in time, a second opinion that improved the plan, the agency's own routing slips, and a foster mother's four lines.", "end_order", requiresFlags=["noticeAsked", "secondOpinion"]),
    C("The file holds a second opinion and a better plan — but the asking was never made in writing to the agency, and the surgery has already happened under the standard packet.", "end_afterwards", requiresFlags=["secondOpinion"]),
    C("The file holds a refusal, a ripening tooth, and a system that documented its way around both.", "end_nobody", requiresFlags=["surgeryRefused"]),
    C("The file holds good intentions, phone calls, and a standard packet — and the court writes the only order such a file can carry.", "end_afterwards")]),

 E("end_order", 36, "Ending — The Order Names Who Signs",
   ["The order is four paragraphs, and it will outlive everyone in the room. Routine and emergency care: the caregiver present. Scheduled non-emergency procedures: written notice to you in advance, your written consent or the court's approval, second opinions facilitated. Your presence at induction and recovery: ordered, with the consult letter's word — *beneficial* — quoted in the findings. And the distribution lists in Navya's case, from this day forward, carry your name by the order's own instruction. On Tuesday, December 8, 2026, you hold your daughter's hand while the sleep medicine starts, with two crowns in the plan where three extractions used to be, and Mrs. Yuen waiting with the car and a juice box.",
    "Name what won this, precisely. Not a statute about dental consent — the scenario asserts none, because the honest map of this territory is orders, practices, and forms. What won was a sequence any parent can run: ask in writing before the default hardens; get a second opinion that improves the plan you're consenting to; request the record (55 Pa. Code § 3130.44(d)) so the routing slips testify; bring the court an arrangement instead of a grievance, at a hearing where the court is already making determinations about the case (42 Pa.C.S. § 6351(f)). The order did not declare you the only signer. It did something more durable: it named who signs, in advance, in writing.",
    "What no strategy controls: a different judge's appetite for consent orders; a true emergency, which will always outrun every paragraph ever written (and should); the surgery's own outcome, which belongs to medicine. Navya is still in care, and the road home runs through your plan and your recovery. But in the file that follows her, the signature lines now have a mother's name printed where a default used to be — and that change, unusually for this system, is permanent."]),

 E("end_afterwards", 31, "Ending — Told Afterwards (partial)",
   ["The surgery is already done by the time the court writes anything. It went well — children are resilient, and the plan, improved or not, was competent dentistry — and you learned its date the way you learned of its existence: from Navya, at a visit, as news. The review order does give you prospective ground: notice of scheduled procedures from now on, your name added to the distributions. It gives it in the agency's own language of reasonableness, unaccompanied by the consent right, the presence right, or any finding about how the packet was routed. The past is unaddressed. The future is improved by exactly the width of what you could prove.",
    "Read the difference between the two orders without flinching. A second opinion, standing alone, improved Navya's surgery — two crowns are a real and permanent gift. But consent follows the asking, and the asking that counts is written, addressed, dated, and served on the institution, not remembered by it. The record request that was skipped (55 Pa. Code § 3130.44(d)) was the difference between a court reading routing slips and a court reading a summary of them. What you proved got ordered. What you only knew got sympathized with.",
    "This is a partial ending, and a recoverable one: the prospective notice language is a foothold, orders can be revisited at later reviews on fuller paper, and Navya's case — like your recovery — is on track. The scenario's lesson is about the half-life of being right. You were right in November, in conversations. In this system, a right becomes real at the speed of its paperwork — and surgery schedules do not wait for conversations to precipitate."]),

 E("end_nobody", 31, "Ending — Nobody Signed",
   ["December arrives with the tooth still in place and the temperature changed around it. Your refusal stopped the scheduled surgery; the agency's response stopped everything else; and in the last week of November the tooth made its own decision — pain, swelling, an urgent visit, and an extraction performed as an urgent matter on a frightened six-year-old, with consent handled by whoever was standing there. Every adult in the story can produce a document defending their part. The documents are all accurate. The outcome is the one outcome nobody's paperwork was for.",
    "The debrief owes you this plainly: refusal was a real power, aimed at the wrong target. The enemy in this scenario was never the surgery — two dentists' worth of evidence said Navya needed it — but the routing: consent designed to flow around you. A refusal stops the medicine along with the routing. A structured ask — written notice, your consent or a court's, your presence, a second opinion — stops only the routing, and the review hearing (42 Pa.C.S. § 6351(f)) was already on the calendar as the place to get it ordered.",
    "What no strategy controls is also real: you were handed a frightening surprise about your child's body, at a visit table, secondhand — the anger that wrote that letter was earned, and the system that provoked it documented your reaction more carefully than its own default. But courts can only order what a record proposes. The wall protected nothing; the pen was loaded the whole time. Navya's case continues, her remaining dental plan still needs an arrangement, and the next review is another chance to propose one — in writing, in advance, in the shape of an order."]),
]
emit(119, s119_meta, s119, S, "a young child in foster care, a dental surgery, and a fight over who consents. No graphic content.")

# ============================================================ S120 (Hard)
S = date(2027, 1, 11)
assert fmt(S) == "Monday, January 11, 2027"
assert fmt(S + timedelta(days=38)) == "Thursday, February 18, 2027"   # permanency hearing

s120_meta = {
    "title": "The First 90 Days",
    "subtitle": "Scenario 120 — The Medicine Log (a fictional composite)",
    "startDateISO": "2027-01-11",
    "startNode": "start",
    "startCash": 150,
    "tier": "Hard",
    "summary": "You are Maureen Brackett. Your daughter Siobhan, fourteen, has been in foster care five months. At today's visit she is quiet in a way that is new — and she tells you, in a level voice, that 'the pills changed again.'",
}

s120 = [
 N("start", 0, "Watching school",
   ["Siobhan has always visited at full volume — grievances, jokes, a running commentary on the foster home's television. Today she sits inside a quieter weather. Sentences arrive late and leave early. Twice she loses the thread of her own story and shrugs, unbothered, in a way that frightens you more than tears have ever managed.",
    "\"I'm fine,\" she says. \"I just feel like I'm watching school. Like, from the hallway.\" A pause. \"The pills changed again. In December. Didn't they tell you?\" Nobody told you. You did not know there were pills whose changes could be numbered."],
   [C("Ask her — gently, concretely — what she takes, and since when, and what December changed.", "how_siobhan")]),

 N("how_siobhan", 0, "How Siobhan got here",
   ["The record, briefly and fairly: your illness last summer — the surgery, the complications, the months of recovery on a couch that was also your address — left Siobhan effectively unsupervised at the precise age supervision matters most, and the county's petition said so, in those words, accurately. She has been with Mrs. Ellery since August. Your plan is half medical recovery, half housing: you are in a medical-respite apartment now, working part-time, attending everything, missing nothing.",
    "What your plan has never mentioned, in any of its versions, is medication — because until this visit, no one had ever mentioned medication to you."],
   [C("Call Mrs. Ellery tonight. She hands Siobhan the pills every morning; start with the person who pours the water.", "ellery_call")]),

 N("ellery_call", 1, "The bottles",
   ["Mrs. Ellery is a retired school secretary, and her kitchen runs on labeled shelves. Yes, there are medications — two, currently. They arrive from the pharmacy with agency paperwork; she administers what the bottles say, at the times the bottles say, and she keeps a notebook — her own, because secretaries keep notebooks — of every dose given, every refusal, every comment Siobhan makes about how she feels.",
    "\"I've wondered when you'd ask,\" she says, without triumph. \"You're the mother. I give the pills; I don't decide them. The deciding happens somewhere above both of us, and it has never once sent me a letter either.\" She reads you the bottle labels over the phone, slowly, twice. You write down names and doses you cannot yet spell."],
   [C("Write the names down exactly as heard — then call your lawyer and ask what a parent can actually demand here.", "lawyer120")]),

 N("lawyer120", 2, "The paper above the pills",
   ["Ms. Renner maps the territory without inflating it. Medication for a child in placement is decided in prescribers' offices and agency processes, and no slogan changes that. But the decisions generate paper — prescriptions, medication administration records, visit notes, logs — and the paper is reachable. The agency's case record is released on request (55 Pa. Code § 3130.44(d)); you ask in writing, and you ask for the medication records by name. The permanency hearing on Thursday, February 18 will make the court's own determinations about this case (42 Pa.C.S. § 6351(f)) — and a court cannot determine what it cannot see.",
    "\"Two more tools,\" she says. \"Written questions to the prescriber — real questions, about indications, changes, monitoring. Prescribers answer letters more often than they answer feelings. And your daughter's own account, in her words, with her permission. She is fourteen. A file that medicates a person should somewhere contain that person's testimony about it.\""],
   [C("Write the request today: the full record, the medication administration records by name, the prescriber's identity and visit notes.", "request_sent", setFlags=["recordsRequested", "logRequested"], addHidden=["Medical — medication administration records requested by parent in writing"]),
    C("Call the agency's nurse line first. A conversation might get you the story faster than a letter gets you the file.", "nurse_call")]),

 N("nurse_call", 3, "The nurse line",
   ["The agency nurse is kind, fluent, and document-free. Siobhan's medications are 'managed by her prescriber in coordination with the team.' The December change was 'a routine adjustment.' The log? 'Kept between the foster home and the pharmacy, I believe.' She cannot send you anything, but she is happy to note your concern in the call record — a record you will never see, summarizing a call whose summary is its only artifact.",
    "You hang up knowing the shape of the answer and owning none of it. Somewhere there is a log with your daughter's name on it, and the distance between you and it is one written request long."],
   [C("Send the written request. Full record, medication records by name, prescriber identified.", "request_sent", setFlags=["recordsRequested", "logRequested"], addHidden=["Medical — medication administration records requested in writing after verbal inquiry produced no documents"]),
    C("Let the note in the call record stand. Professionals are coordinating; don't become the difficult file.", "waiting120")]),

 N("waiting120", 6, "Coordinated",
   ["January coordinates itself onward. The team coordinates; the prescriber prescribes; the bottles arrive; the notebook at Mrs. Ellery's fills with doses and one-word reviews — *flat, flat, slept through breakfast*. Your knowledge of your daughter's medication remains exactly what it was in the visit room: what a fourteen-year-old could carry to you in conversation.",
    "At the second January visit Siobhan has a new piece of data, offered with the ghost of her old delivery: \"There's a bag in my backpack from the pharmacy. It has papers in it. Nobody said you can't read papers.\""],
   [C("Read the papers — with her permission, at the visit table, in the open.", "pharmacy_bag")]),

 N("request_sent", 5, "The request, out",
   ["The request goes out in writing, dated, copied: the full case record under the regulation (55 Pa. Code § 3130.44(d)), the medication administration records expressly named, the prescriber's name and visit notes, and the pharmacy fill history if the file holds it. Ms. Renner reviews the draft and changes one word — *all* — into a list. \"Lists,\" she says, \"are what files answer. 'All' is what they hide behind.\"",
    "While the file travels, life continues at visit-table scale. Siobhan has brought you a data point in a backpack."],
   [C("Saturday's visit: she has something to show you.", "respite_story")]),

 N("respite_story", 6, "The October week",
   ["On the record request's way out, Siobhan finally tells you about October — the week she has been alluding to in pieces. A respite stay while Mrs. Ellery had her own surgery; a night of panic that would not come down; an emergency department; a doctor she saw once, who started the first medication. By the time she returned to Mrs. Ellery's, the prescription had become a routine, the way weather becomes climate. Nobody designed a secret. A crisis made a decision, and then the decision made itself permanent, one refill at a time.",
    "It is told without drama and deserves to be believed without decoration. It is also — you understand, listening — a story that exists in no document anyone has offered you."],
   [C("Ask what she brought in the backpack.", "pharmacy_bag")]),

 N("pharmacy_bag", 8, "The pharmacy bag",
   ["The bag holds the pharmacy's own paperwork: a fill history and an information sheet for a second medication — one whose name is not on either bottle Mrs. Ellery read to you, because it is the December addition, administered at school by the nurse, in the middle of the day you do not see. Prescriber: Dr. Anwar. Dates: December 9, and refills since.",
    "Siobhan watches you read it. \"You can take a picture,\" she says. \"It's my bag.\" You photograph every page, and you understand that a fourteen-year-old has just performed, with a backpack, the document production this case's adults had not."],
   [C("Ask her whether you may write down, in her exact words, what the medications feel like — for your lawyer, and only where she agrees.", "siobhan_words", cash=-5),
    C("Take the photographs and let her words stay hers for now. The paper trail may be enough.", "visit2")]),

 N("siobhan_words", 10, "Watching school, transcribed",
   ["Her account takes ten minutes and one page, and she edits it like an author: *The morning one makes first period like watching it from the hallway. I fall asleep in math twice. The new one at lunch helps the panic but my hands feel far away. I am not saying stop everything. I am saying nobody asked me.* She signs it, dates it, and writes under the signature, unprompted: *You can show the judge. That's why I said it good.*",
    "Ms. Renner, reading it later, is quiet for a moment. \"Files medicate children every day,\" she says. \"Almost none of them contain a sentence from the child about what the medicine is like. Courts notice sentences like hers. So do prescribers.\""],
   [C("File her page with counsel, and ask what comes next: the log itself.", "visit2", setFlags=["siobhanHeard"], addHidden=["Medical — child's own account of medication effects recorded verbatim, with her consent"])]),

 N("visit2", 13, "First period",
   ["The next visit adds a corroborating witness of the accidental kind: Siobhan's school counselor mentioned — to Siobhan, in passing — that her first-period teacher has flagged sleeping in class, twice, in the grade portal the foster home can see. The picture assembling itself has three independent hands in it now: a daughter's account, a teacher's flags, a pharmacy's dates. Pictures like that are called, in courtrooms, exhibits.",
    "What is still missing is the document at the center: the medication administration record itself — who prescribed, who changed, who administered, who was told. Your written request has been out for two weeks."],
   [C("Go to Mrs. Ellery's notebook — she offered it the first night, and secretaries keep the truth.", "ellery_log")]),

 N("ellery_log", 15, "The secretary's notebook",
   ["Mrs. Ellery's notebook is everything the official record will turn out not to be: dated, contemporaneous, complete. Every dose. Every change. And December 9 — the day the midday medication began — carries her careful annotation: *begun per agency phone instruction; no prescriber visit this week; S. says hands feel strange.* She makes you a copy at her kitchen table, with a retired secretary's full ceremony, and initials every page.",
    "\"I keep it because somebody should,\" she says. \"I always assumed the agency kept the same. If theirs has a hole in it, that's their hole, not mine.\""],
   [C("Take the copy to counsel. Two logs exist in this case now, and they are about to be compared.", "partial_log", setFlags=["kitchenLog"])]),

 N("partial_log", 17, "The hole in December",
   ["The agency's production arrives: records, reports — and a medication administration record with a six-week gap across December and early January, the exact weeks of the change. The prescriber's visit notes are 'held by the provider' and not produced. Whether the gap is sloppiness or something else, the document the court would naturally rely on cannot currently account for the most consequential month in Siobhan's medication history.",
    "Ms. Renner tabs the gap with a yellow flag and writes one sentence on the packet memo: *The official log cannot say who decided December. The foster mother's notebook can say who was told: no one, by phone, off paper.* At a hearing, it is worth remembering, reports that are relied on can be examined and their makers questioned — the principle the law states expressly for disposition (42 Pa.C.S. § 6341(d)(2)) is the posture this packet takes toward every page."],
   [C("Write to the prescriber directly — real questions, listed, dated, through counsel.", "prescriber_letter")]),

 N("prescriber_letter", 20, "Questions for Dr. Anwar",
   ["The letter to Dr. Anwar is a page of questions a mother is entitled to have answers exist for: What is each medication for? What prompted the December addition, and the setting in which it was decided? What monitoring is in place for a fourteen-year-old's mornings? Who, in the current arrangement, is notified before a change — and who should be? It accuses no one. It asks a prescriber to do, on paper, what prescribers do in their heads.",
    "It can go in the mail, through counsel, with the log gap and Siobhan's page referenced. Or it can wait for a conversation that has no date, no address, and no obligation to occur."],
   [C("Send it — copies to the agency and the file, the questions numbered so answers can be too.", "school_note", setFlags=["prescriberAsked"], cash=-8, addHidden=["Medical — written questions to prescriber sent: indications, December change, monitoring, notice"]),
    C("Raise the questions at the next team meeting instead — faces persuade better than letters.", "noor_silence")]),

 N("school_note", 24, "The school nurse's page",
   ["One more exhibit surfaces through the record: the school nurse's log — the midday dose, administered daily, with two notations in a nurse's flat hand: *slept through period 1 following dose timing change; teacher notified.* The system, it turns out, has been recording Siobhan's mornings faithfully, in four separate buildings, in four separate files. What it never did was let the files meet — or let her mother read any of them.",
    "Your packet introduces the files to each other. That is most of what advocacy is, at this altitude: introductions between documents."],
   [C("Wait for Dr. Anwar's answer — or its absence — with the packet nearly built.", "noor_reply")]),

 N("noor_silence", 26, "The meeting that isn't",
   ["The team meeting, when it finally convenes, has an agenda with eleven items and yours at the bottom in the category of *family input*, scheduled against the room's fatigue. You raise the questions. They are received warmly, noted generally, and answered in the specific way meetings answer: a follow-up will occur. No letter comes. No answers arrive with names or dates on them. The December decision remains, officially, something that happened the way weather happens.",
    "Ms. Renner adds the meeting's minutes — one line, *mother raised medication questions; follow-up noted* — to the packet. \"Sometimes the exhibit is the thinness,\" she says."],
   [C("Build the packet around what exists: the gapped log, the notebook, the pharmacy dates, a daughter's page.", "packet120")]),

 N("noor_reply", 27, "Dr. Anwar replies",
   ["Dr. Anwar's reply is three pages, professional and — in the way of documents written by people who expect to be read by courts — precise. The October start: crisis, documented. The December addition: hers, by phone consultation with the agency during a reported escalation, with a visit to follow that scheduling then lost. Monitoring: described. And on the last page, the sentence the packet was built to earn: the morning dose's timing *should be reviewed against the school-day sedation reports*, and notice of non-urgent changes to the parent and counsel is, she writes, *appropriate and will be my practice in this case*.",
    "A prescriber has now said, in writing, most of what you intend to ask the court to order. Orders are easiest to win when somebody with a title has already agreed they describe ordinary care."],
   [C("Ask the guardian ad litem to read the whole packet — her position will be heard on February 18.", "gal_view")]),

 N("gal_view", 30, "The guardian ad litem reads",
   ["Ms. Zielinska reads the packet the way she reads everything: completely, with a pencil. Siobhan's page gets the longest pause. \"I visit her monthly,\" she says. \"She told me she was 'fine.' She told you the truth because you asked about the pills specifically. There's a lesson in that I intend to be annoyed about later.\" Her position for the hearing aligns: notice of changes to mother and counsel, the log produced monthly, the dose-timing review completed and reported.",
    "The agency's report, when it lands, will describe Siobhan as *medication compliant*. You now hold four documents that give that phrase a cross-examination."],
   [C("Final assembly: the packet, in date order, gaps flagged, titles facing up.", "packet120")]),

 N("packet120", 33, "Date order",
   ["The packet tells December's story in the order December happened: a phone instruction; a pharmacy fill; a foster mother's notebook; a six-week hole in the official log; a nurse's two flat sentences; a daughter's signed page; a prescriber's letter, or a meeting's one-line minute where a letter should be. Ms. Renner writes the ask in findings language: that the court direct notice of non-urgent medication changes to you and counsel in advance; production of the complete medication log monthly; completion of the dose-timing review with a report to all parties.",
    "Nothing in the ask claims you should prescribe. It claims you should be told — a distinction the packet states on its first page, before anyone can misstate it."],
   [C("Read the agency's report when it comes, and mark every sentence about medication.", "agency_report120")]),

 N("agency_report120", 35, "Medication compliant",
   ["The agency's report for the permanency hearing is competent on housing, silent where it should be specific on school, and — on medication — two sentences long. *Youth is medication compliant. Medication is managed by the prescriber in coordination with the team.* The team, as a body, has never been defined. The coordination has never been documented. December does not appear. It is, Ms. Renner says, turning the page, \"a perfect report, if the file it summarizes were a different file. Ours will be in the room.\"",
    "Reports at a hearing can be examined, and the people who made them questioned — the packet is built to make that examination short and factual."],
   [C("One whiteboard session, then court.", "renner_whiteboard")]),

 N("renner_whiteboard", 36, "What the court must decide",
   ["Ms. Renner draws the hearing the statute builds. At the permanency hearing the court determines: the continuing necessity of placement; compliance with the plan; progress toward alleviating the circumstances that caused placement; and whether reasonable efforts were made to finalize the plan. (42 Pa.C.S. § 6351(f)(1), (2), (3), (5.1))",
    "\"Medication is not a fifth determination,\" she says. \"It is evidence inside the four — about necessity, about efforts, about what this placement is actually doing to her mornings. Our job is to make sure the court decides from the whole file, including the file's holes. Especially the holes.\""],
   [C("Sleep. Tomorrow the file goes in front of the one person who can order it closed.", "night_before120")]),

 N("night_before120", 37, "The folder, again",
   ["You think about the visit room in January: a girl inside a quieter weather, saying *didn't they tell you* — the question underneath this entire case. No conspiracy told her no. A set of defaults did: the packet routed here, the log kept there, the note filed elsewhere, the mother informed nowhere. Defaults are not villains. They are just undefeated until somebody files paper against them.",
    "Tomorrow, somebody does."],
   [C("Go to court.", "hearing120")]),

 N("hearing120", 38, "Thursday, February 18",
   ["The permanency hearing runs the statute's determinations (42 Pa.C.S. § 6351(f)), and the medication chapter is reached with the whole record in the room — or with as much of it as your winter assembled. The agency's two sentences are read. Then yours are. The judge's questions go where judges' questions go: to the documents.",
    "What is ordered about Siobhan's medication — and about who is told what, in advance, in writing — is decided by what the file could prove when the room went quiet."],
   [C("The file holds the mother's written requests, the foster mother's complete notebook, the daughter's own signed account, and a prescriber's letter agreeing that notice is appropriate.", "end_writing", requiresFlags=["recordsRequested", "prescriberAsked", "siobhanHeard"]),
    C("The file holds the record and its December hole — but the questions to the prescriber were only ever raised aloud, and the daughter's account was never written down.", "end_eventually", requiresFlags=["recordsRequested"]),
    C("The file holds a nurse-line note and a mother's memory of a visit-room conversation.", "end_counter")]),

 E("end_writing", 38, "Ending — Every Change in Writing",
   ["The order adopts the ask nearly whole, because the packet made it the path of least resistance: non-urgent medication changes require advance written notice to you and to counsel; the complete medication administration record is to be produced to all parties monthly; Dr. Anwar's dose-timing review is to be completed and reported within thirty days — and the first concrete result arrives before the ink is metaphorically dry, when the morning dose moves to evening and Siobhan's first period reopens like a window. The judge's last words on the subject are the ones your daughter wrote, quoted back into the record: *nobody asked me* — followed by the court's own sentence: \"She has been asked now. It will stay that way.\"",
    "Name the machinery honestly. No statute in this scenario handed a mother a veto over prescriptions, and the scenario asserts none. What the record did — the request under 55 Pa. Code § 3130.44(d), the questions a prescriber answered in writing, a foster mother's secretary-grade notebook, a child's signed page — was convert a default into a determination: at a hearing where the court must decide necessity, compliance, progress, and efforts (42 Pa.C.S. § 6351(f)), the medication chapter could no longer be two sentences long. Notice is not control. But notice is the difference between a parent and an audience.",
    "What no strategy controls: the medicine itself, which may genuinely be helping and may change again for good reasons; a different judge's reluctance to write medication orders; the case's deeper road, which still runs through your recovery and housing. Siobhan remains in care tonight. But the log has a reader now, the changes have an addressee, and a fourteen-year-old's testimony about her own mornings is in the file that medicates her — permanently, in her own words, signed."]),

 E("end_eventually", 38, "Ending — The Log, Eventually (partial)",
   ["The court acts on what it can see, and what it can see is a hole. The order directs the agency to produce the complete medication administration record and a prescriber's summary before the next review, and notes — in the dry language courts use for weather they disapprove of — that the December gap 'should not recur.' The dose-timing question is deferred to that production. The notice arrangement you asked for is not ordered: the prescriber was never asked in writing, your daughter's account exists in your testimony rather than her handwriting, and a court asked to structure a practice prefers exhibits to recollections.",
    "Do the honest accounting. The written record request (55 Pa. Code § 3130.44(d)) did its work — it produced the log, and the log's gap became the hearing's most durable fact. What was skipped skipped in a specific direction: the questions existed, but they were asked in a meeting, and meetings answer in minutes of one line. The daughter's account existed, but it was carried in her mother's voice, at one remove, discounted the way all secondhand things are discounted — the principle that written reports may be examined and their makers questioned (42 Pa.C.S. § 6341(d)(2)) cuts for the parent with paper and against the parent with a summary.",
    "Partial, and pointed at a remedy: the next review now has a court-ordered production deadline in front of it, and nothing about this ending prevents the letters from being written in February instead of January. They will land differently — later, and into a file that already has a gap flagged by a judge — but paper filed late in this system is still paper. The log will be read. Eventually was this ending's title, not its epitaph."]),

 E("end_counter", 38, "Ending — The Bag on the Counter",
   ["The hearing's medication chapter is two sentences long, because two sentences is what the file held. And then, in the corridor afterward, Mrs. Ellery mentions — kindly, as one mentions weather — that the pharmacy bag on her counter this week held a new printout: the morning dose is being split, half at breakfast, half at school. You learn of the third change in your daughter's medication the way you learned of the first: by accident, from a kind person, after it had already happened. The system did not hide it from you. It simply never built a road from the decision to you, and no one had yet made it build one.",
    "The debrief is the scenario itself, compressed: every document in this story existed. The log existed — at a foster home, in a secretary's notebook. The record existed — releasable on a written request (55 Pa. Code § 3130.44(d)) that was never sent. The daughter's knowledge existed — in her own precise sentences, never written down. The prescriber's willingness to answer existed. What did not exist was the paper connecting any of it to the one person the whole arrangement assumes is peripheral: the mother. Systems route information to the addresses they are given, in writing. Give them the address.",
    "Nothing here is sealed. A request can be filed in February; questions can be numbered and mailed in March; permanency hearings recur on the statute's clock (42 Pa.C.S. § 6351(e)(3)(i)), and each one is a fresh chance to put the file in the room. But Siobhan's mornings between now and then will be medicated on information her mother receives by accident — and in this system, accident is what fills every space that paper doesn't."]),
]
emit(120, s120_meta, s120, S, "a teenager in foster care and a dispute over medication records and notice. No graphic content.")
print("done")
