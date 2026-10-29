#!/usr/bin/env python3
"""Generate scenarios 123-124 (Wave 2, Batch 9: Education & Medical).
Fictional composites only."""
import sys
sys.path.insert(0, "/home/hatch/workspace/your_files/tacticwatch-game")
from batchN_lib import N, C, E, emit, fmt
from datetime import date, timedelta

# ============================================================ S123 (Complex)
S = date(2027, 1, 4)
assert fmt(S) == "Monday, January 4, 2027"
assert fmt(S + timedelta(days=52)) == "Thursday, February 25, 2027"   # review / permanency hearing

s123_meta = {
    "title": "The First 90 Days",
    "subtitle": "Scenario 123 — The Empty Chair (a fictional composite)",
    "startDateISO": "2027-01-04",
    "startNode": "start",
    "startCash": 150,
    "tier": "Complex",
    "summary": "You are Dalila Haddad. Your daughter Yasmin, fifteen, is in a residential placement, and her school has decided she needs an evaluation. The district has also decided — from a file with your address wrong — that you cannot be located, and that a stranger should be appointed to sit in your chair.",
}

s123 = [
 N("start", 0, "School mom",
   ["Yasmin delivers the news at the visit with a fifteen-year-old's precision for the jugular: \"They're getting me a school mom. Since you apparently live nowhere.\" The facility's education liaison used the word *surrogate*. The school district, having mailed two letters to an address you left in July and called a number disconnected in August, has determined that Yasmin's parent cannot be located — and is appointing someone to make her education decisions.",
    "You visit every week. You have never missed. The facility's own sign-in book has your name in it fourteen times, in your handwriting, next to your current phone number. Somewhere between that book and the district's file, you became unfindable."],
   [C("Ask Yasmin exactly what was said, by whom, and write it down before the visit ends.", "backstory123")]),

 N("backstory123", 0, "How Yasmin got here",
   ["The record, fairly: last year was a collapsing one — your hours cut, the eviction, the shelter summer, and Yasmin, fourteen then, absorbing the chaos the way teenagers do, by disappearing into it: school refusal, two runaway episodes, a year of grades falling off a table. The dependency finding named the circumstances accurately. Since October she has been at the residential program across the county; you are in stable housing since September, working, in family therapy, visiting weekly without exception.",
    "Your parental rights are intact and unquestioned in the dependency case. It is only in the school district's parallel universe — built from an intake form — that you are a missing person."],
   [C("Call the facility's education liaison, Ms. Phan, and ask what a 'surrogate' is being appointed to do, exactly.", "facility_call")]),

 N("facility_call", 1, "Routine, she says",
   ["Ms. Phan is brisk and not unkind. The school believes Yasmin needs a special-education evaluation. Evaluations need a parent's consent and a parent's participation. The district's letters came back; the district's calls failed; the district is following its process for students whose parents can't be located: assignment of a surrogate parent, an educational decision-maker. \"It's routine,\" she says. \"It doesn't affect your rights in the dependency case.\"",
    "\"It affects my rights in the room where her education gets decided,\" you say — and hear, in your own voice, the sentence this whole scenario is about. Ms. Phan, to her credit, does not argue. She gives you the district office's number and the name of the supervisor: Mr. Corvath."],
   [C("Ask what the facility has already signed in your place — then take the whole inventory to your lawyer.", "facility_forms")]),

 N("lawyer123", 2, "The rule, whole",
   ["Ms. Viteri reads the federal regulation the way she reads everything: in full, out loud, before discussing it. A school must ensure a child's rights are protected when no parent can be identified; when the agency, after reasonable efforts, cannot locate a parent; when the child is a ward of the State; or when the child is an unaccompanied homeless youth — and its duties include assigning an individual to act as a surrogate for the parents. (34 C.F.R. § 300.519(a), (b)) For a child who is a ward of the State, the surrogate may instead be appointed by the judge overseeing the child's case. (§ 300.519(c))",
    "\"Three things,\" she says. \"First: you are identifiable, locatable, and in weekly documented contact with the very facility the district got its address from — the factual premise of this process is false, and false premises are fought with paper, not outrage. Second: a surrogate, whoever it is, may not be an employee of the school, the district, or any agency involved in Yasmin's education or care. (§ 300.519(d)(2)(i)) Remember that; this case will test it. Third: the clock is real — the state must make reasonable efforts to assign a surrogate within thirty days of the determination that one is needed (§ 300.519(h)), and a surrogate, once seated, can consent to the evaluation and represent Yasmin in everything about it. (§ 300.519(g)) We have weeks, not months. We write today.\""],
   [C("Write today: to the district, the agency, the facility, and the court file — who you are, where you live, that your rights are intact, and that the consent decision is yours.", "letters_out", setFlags=["locatedInWriting"], addHidden=["Education — parent asserted identity, current address, and decision-making role in writing to district and agency"]),
    C("Call Mr. Corvath's office first. A human conversation may unwind this faster than a letter escalates it.", "district_call")]),

 N("facility_forms", 2, "The slope of signatures",
   ["On the drive home you inventory, with Yasmin's help by phone, what facility staff have already signed in your parental place: a field-trip permission. A photo release. A school dance form. Each one reasonable; each one a small rehearsal. Nobody decided to replace you. The replacement accreted, form by form, the way the address did — everything in this case accretes, and accretions are only visible when someone reads the whole file at once.",
    "An evaluation consent is not a field-trip form. It decides what gets tested, what gets found, what gets written into the record that follows a child for years. The slope ends there, or it doesn't end."],
   [C("Take the inventory to Ms. Viteri. You want the rule, whole, before you touch the machinery.", "lawyer123")]),

 N("district_call", 3, "Reasonable efforts",
   ["The district's special-education office is polite at the speed of process. The file shows, the staffer says, 'reasonable efforts': two letters mailed, returned; two calls to the number on file, disconnected. The determination that a surrogate is needed has been made; the assignment process is underway; if you are in fact the mother, you are welcome to 'provide documentation' for the file. Your existence is received as a claim to be processed — by the process that already concluded you don't exist.",
    "Ms. Viteri, debriefing the call, is succinct: \"Their reasonable efforts were reasonable attempts to reach a wrong address. A letter from you ends the factual question in a way no phone call can: it is the location, proving itself, in writing, with a date.\""],
   [C("Write the letters — to the district, the agency, the facility, the court — today.", "letters_out", setFlags=["locatedInWriting"], addHidden=["Education — parent located herself in writing after district's 'reasonable efforts' reached only a stale address"]),
    C("Wait for the assignment letter. If a qualified volunteer is appointed, perhaps the practical harm is small, and fighting looks like vanity.", "assignment_news")]),

 N("letters_out", 4, "Located",
   ["The letters go out in one afternoon — the most consequential mail run of your year. To the district: your identity, your current address and phone, your daughter's name and school, the statement that your parental rights are intact and unmodified by any court, and the conclusion the district is asked to draw: no surrogate is needed, because the predicate — a parent who cannot be identified or located — is false. To the agency and the facility: the same, plus a demand that the address be corrected in every file that feeds another file. To the court, through counsel: a copy, so February's review reads the correction from the record, not from memory.",
    "Copies cost you eleven dollars at the copy shop. You have spent more, for less, in this case — but never less, for more."],
   [C("Now ask for the file — the agency's record of how your address decayed. (55 Pa. Code § 3130.44(d))", "records123", cash=-11)]),

 N("records123", 6, "The file's archaeology",
   ["The written record request goes to the agency (55 Pa. Code § 3130.44(d)) — and asks, by name, for everything touching Yasmin's education and your address: intake forms, school correspondence, the notices the district copied to the agency, the determination paperwork itself.",
    "Files, excavated properly, tell on their own formation. This one is about to explain how a mother who visits weekly became, on paper, a person who could not be found."],
   [C("Sign, date, send, keep the receipt — and read what comes back like a geologist.", "mail_room", setFlags=["recordsRequested"], addHidden=["Record — agency record requested in writing, including education correspondence and address history"]),
    C("Let the letters do the work alone; the file's archaeology is a luxury.", "mail_room")]),

 N("mail_room", 7, "Returned to sender",
   ["The production begins with two envelopes — the district's own letters, returned, stamped *no longer at this address*, filed by the facility in a folder nobody had reason to open twice. Reasonable efforts, fossilized: the district mailed to the shelter you left in July; the facility filed the returns; the agency was copied on neither. Three institutions each held one piece of a simple fact — *the mother can be reached at her daughter's placement, every week, in person* — and no process existed whose job was to assemble it.",
    "Assembling it is now, by default and by letter, your job. You assemble it the way this game always teaches: in writing, with the pieces dated."],
   [C("Next stratum: the phone number that was 'disconnected.'", "phone_bill")]),

 N("phone_bill", 8, "Fourteen signatures",
   ["The number the district called was your old one — disconnected in August, when the shelter period ended and you consolidated your life into a new phone, a new address, a lease. Your current number appears in the facility's visitor log on fourteen consecutive weekly visits, in your own hand, next to your signature. The agency's review paperwork has carried the correct number since October. The district's source document — you can see it coming in the file like weather — is older than all of that.",
    "Institutions do not update each other. That is not malice; it is architecture. Parents are the only integration layer this system has ever reliably had, which is unfair, and true, and — handled in writing — usable."],
   [C("Read the source document itself: the intake form.", "address_file")]),

 N("address_file", 9, "July's handwriting",
   ["Here it is: the facility's intake form from July, completed during the shelter period by a clerk working from the emergency paperwork — the shelter's address, the old phone, and in the box for parental contact, a checkbox ticked: *whereabouts unverified*. It was true for perhaps a week in July, during the worst fortnight of your life. It has been false for six months. It has also been copied, unexamined, into the district's file, where it acquired the force of a finding.",
    "One checkbox. Everything since — the returned letters, the failed calls, the determination, the impending stranger in your chair — is that checkbox, compounding."],
   [C("Take the full file to Ms. Viteri. The premise fight is winnable; now the candidate question opens.", "intake_form")]),

 N("intake_form", 11, "The checkbox",
   ["Ms. Viteri spreads the archaeology on her table: July's form, the returned envelopes, the visitor log, your letters of January. \"Understand what happened,\" she says, \"because the court will want the story in one breath: a stale intake form declared you unverified; two systems mailed the stale address; the failures were filed as efforts; the efforts founded a determination; and the determination is about to appoint a person to exercise rights that were never lost, for a mother who was never missing. Against that story, the district has a process. Processes do not enjoy being narrated.\"",
    "Then she turns practical. \"The district will now float names — it must fill the process it started, unless it withdraws the determination. Who the names are matters. One of them, in cases like this, is very often exactly who the rule forbids.\""],
   [C("Ask for the candidate names in writing — before any assignment is made.", "candidate_list")]),

 N("candidate_list", 12, "Two names",
   ["The district's reply names the pool it is drawing from, and Ms. Viteri's prediction is standing in it. Name one: Mrs. Skye, a retired teacher, trained as a volunteer surrogate, no connection to any agency in Yasmin's life. Name two: the education coordinator of Yasmin's own facility — the person whose program houses her, employs her teachers' liaisons, and would, as surrogate, be consenting to evaluations of a child in her own institution's care.",
    "The regulation's criterion is plain: a surrogate may not be an employee of the state or local education agency, *or of any other agency involved in the education or care of the child*, and must have no interest conflicting with the child's. (34 C.F.R. § 300.519(d)(2)) Name two is not a close call. It is the textbook call."],
   [C("Object in writing to the facility-employee candidate, citing the rule, while affirming the mother's own availability makes any surrogate unnecessary.", "skye_visit", setFlags=["conflictRaised"], addHidden=["Education — written objection to surrogate candidate employed by an agency involved in the child's care"]),
    C("Say nothing about the names. Challenging the district's pool while your own status is contested may harden positions.", "assignment_news")]),

 N("skye_visit", 15, "Mrs. Skye",
   ["You ask to meet her, and the district — surprised into decency by the request — arranges it. Mrs. Skye is sixty-eight, precise, warm, and entirely uninterested in being anyone's weapon. She has served as surrogate for nine children. Her first question is the one that reorders the whole fight: \"Have they found you, then?\"",
    "\"I am a bridge for children with no one,\" she says. \"A located mother is not my case; she is my exit paperwork. If they appoint me anyway, I will do right by your daughter — but you should know that the honest sentence in this file is that I am unnecessary, and I'll write that sentence myself if they make me part of it.\""],
   [C("Thank her — and take the district's temperature in person, in Mr. Corvath's office, before any assignment lands.", "corvath_meeting")]),

 N("corvath_meeting", 16, "Mr. Corvath's file",
   ["Mr. Corvath receives you with the file open and the air of a man who has read it twice since your letters arrived. He is not a villain; he is a supervisor whose district processed a stale form into a determination, and who now has, on his desk, a located mother, a forbidden candidate, a permissible volunteer who calls herself unnecessary, and a February court date where a judge may ask about all of it.",
    "\"For a ward of the State,\" he says, \"the judge overseeing the case could appoint the surrogate instead of us. (§ 300.519(c)) That's not your daughter's posture as I now understand it — but you should know the road exists, because if this reaches February unresolved, it may be the road the court takes to end the uncertainty. A named person, appointed in open court, beats a process drifting.\" What he does not say — what his open file says for him — is that the district's cleanest exit is to withdraw the determination, and withdrawals are written by people who have been given the paper to justify them. You have given him the paper."],
   [C("Wait for the district's next move with the file complete and the clock running.", "assignment_news")]),

 N("assignment_news", 18, "The determination, revisited or not",
   ["Late January. What arrives from the district depends, with the usual total precision, on what your January put in front of it: whether you exist on paper as a located parent with an objection to the forbidden candidate — or whether the process simply continued, fed by silence, toward appointing whoever the pool produced first.",
    "The thirty-day effort clock (34 C.F.R. § 300.519(h)) is not the enemy here. It is the metronome. Everything in this case is a question of what exists in the file when it stops."],
   [C("Meanwhile, one voice in this case has not been filed anywhere: Yasmin's. Fix that.", "yasmin_wishes")]),

 N("yasmin_wishes", 20, "Her sentence",
   ["At the visit, you ask Yasmin the question the whole apparatus has been deciding without her: what does she want? Her answer is specific enough to quote, and with her permission you do: *I want the test. Maybe my brain has a reason and I'd like to know it. I want my mom at the table for it. No offense to the school mom, but I have a mom.* She writes it herself, signs it, dates it — a fifteen-year-old filing her own exhibit.",
    "It goes into the packet as what it is: the stated wishes of the person whose education every adult in the story is arranging. Files in this system are full of children's wishes paraphrased by professionals. Verbatim is rarer, and it reads differently in a courtroom. It reads like a person."],
   [C("Attach her page. Then face the paper that started all of this — the evaluation consent itself, finally addressed to you.", "evaluation_explainer", setFlags=["yasminWishes"]),
    C("Keep her page in the family. She has been documented enough this year.", "evaluation_explainer")]),

 N("evaluation_explainer", 22, "What the evaluation is",
   ["Ms. Viteri walks you through the thing your signature would actually authorize: testing and review to determine whether Yasmin is a child with a disability and what her educational needs are — the initial evaluation the federal rules contemplate, which a parent may request and must consent to. (34 C.F.R. § 300.301(b), (c)) It is not a placement. It is not a label nailed to a forehead. It is a measurement — the same species of measurement whose absence left a year of failing grades to be explained by character.",
    "Your fear, named honestly in her office, is that a finding follows Yasmin forever. Her answer: \"An unmeasured difficulty also follows her forever. It just follows her as blame.\" The consent form, when it comes, will be one page. The decision deserves this whole conversation, and has now had it."],
   [C("Read the consent request when it reaches your correct address — as, this month, things finally do.", "consent_paper")]),

 N("consent_paper", 24, "The form, addressed to you",
   ["The consent packet arrives at your real address, with your real name on it, proposing the evaluation's areas and your rights in plain print. It is, bureaucratically, the most beautiful document of your winter: proof that the file can be corrected, that a mother can be re-found by the simple expedient of being written to where she lives.",
    "What remains is the decision it was always actually about — not whether you may decide, but what you will decide. Ms. Viteri leaves it with you overnight, with one instruction: \"Decide it as a parent, not as a plaintiff. The chair is won. Chairs don't help children. Signatures and refusals do, depending on what's true.\""],
   [C("Sign the consent — dated, copied, returned with proof — and ask for the evaluation's timeline in writing.", "school_visit", setFlags=["consentGiven"], addHidden=["Education — parent consented to initial evaluation; surrogate process rendered unnecessary"]),
    C("Hold the consent unsigned while you think — a label, a file, a daughter's whole school future; a few more weeks of thinking is not unreasonable.", "consent_stall")]),

 N("school_visit", 26, "The name card",
   ["You visit Yasmin's school — the placement district's building, where her teachers know her as a failing student with a file full of weather. In the conference room, a staff member clears away the remnants of another student's meeting: a tent card, left behind, reading *Parent/Guardian*. You think about the meetings held in this room about your daughter, and the chair that stood empty at them — not because its occupant refused it, but because its occupant's address was a checkbox's casualty.",
    "Her English teacher, met in the hallway, says the sentence the evaluation exists to test: \"She's not lazy. Something's costing her more than it costs the others. I'd like to know what it is before we decide what she is.\" So, in the end, would everyone. The signature is how the knowing starts."],
   [C("Ask the guardian ad litem where she stands for February — Ms. Wexford has been reading a parallel file.", "gal123")]),

 N("gal123", 27, "The guardian ad litem",
   ["Ms. Wexford's position, delivered with a lawyer's economy: she will tell the court that Yasmin's mother is located, engaged, and the proper decision-maker for the evaluation; that no surrogate is needed; and that if any appointment were contemplated over that record, the facility's own coordinator would be disqualified by the regulation's plain terms. (§ 300.519(d)(2)(i)) Then she turns her pencil toward you. \"My support assumes the chair gets used, counselor's client. The evaluation is the point of the chair. If February finds the consent still unsigned, my speech writes itself differently.\"",
    "Allies in this system are conditional in proportion to their honesty. Hers is the honest kind."],
   [C("Build the February packet — and count the days the district's clock still has.", "thirty_days")]),

 N("thirty_days", 29, "The metronome",
   ["Count it as the regulation frames it: once a district determines a child needs a surrogate, the state must make reasonable efforts to assign one within thirty days. (34 C.F.R. § 300.519(h)) Your letters landed inside that window — which is why the determination is being revisited rather than executed — but windows close, processes resume, and February 25 is the date after which the dependency court, not the district, becomes the room where the question gets answered for good.",
    "The packet is nearly built. What it proves, in order: a mother locatable all along; efforts spent on a stale address; a candidate forbidden and a candidate unnecessary; a daughter's own sentence; and a signature — or its absence, which will also be evidence, of something."],
   [C("Spend the remaining weeks the way the case has taught you: on paper, in advance.", "consent_stall_check")]),

 N("consent_stall", 30, "Thinking, at length",
   ["The weeks of thinking have a texture Yasmin can feel from across the county. The evaluation does not begin — consent is the gate, and the gate is yours now, which makes the waiting yours too. Her grades continue their slide. A teacher, not unkindly, asks her whether 'the paperwork' is done yet, and she answers with the sentence that will reach you by phone and stay with you: \"Everyone fought about who gets to sign. Nobody signed.\"",
    "Ms. Viteri does not push. She observes, once, that winning a chair and declining to sit in it produces a specific documentary result: a file in which the obstacle to the child's evaluation is no longer an institution. Courts read such files with great attention to whose name the obstacle carries."],
   [C("Carry the unsigned form into February, and let the review read it.", "yasmin_school_day")]),

 N("consent_stall_check", 30, "The form's status",
   ["Before the packet closes, Ms. Viteri asks the only question that decides February's ending: the consent form — signed, or still thinking? Everything else in the file has been built. The chair was recovered with letters; the evaluation waits on a signature; and the review will read whichever fact your hand has made true.",
    "There is no fourth option in which the form decides itself."],
   [C("It is signed. The evaluation is already being scheduled — I decided it as a parent.", "yasmin_school_day", requiresFlags=["consentGiven"]),
    C("It is still unsigned. I won the right to decide, and I am still deciding.", "yasmin_school_day", requiresNoFlags=["consentGiven"])]),

 N("yasmin_school_day", 33, "Her school day",
   ["Yasmin's school day, as her teachers describe it in the letters Ms. Viteri collects: first period arrives before her brain does; reading assignments cost her triple and repay her half; the frustration that adults keep minuting as *attitude* has a rhythm any evaluator would recognize as a hypothesis. The evaluation — consented or not, scheduled or not — is the only instrument in the story built to convert that rhythm into knowledge.",
    "Whatever February decides about decision-makers, this is what the deciding is for. The packet closes with her teachers' letters on top, where they belong."],
   [C("One administrative crusade remains, and it is the one that started everything: the address.", "address_fix")]),

 N("address_fix", 36, "Four stamps",
   ["You correct your address the way addresses should be corrected and almost never are: in writing, four times, to the agency, the district, the facility, and the court — each with a request for written confirmation, each confirmation filed when it lands. It is an afternoon of envelopes to prevent a year of returned mail. The district's confirmation arrives with an attachment you did not request: a memo to its own staff, adding a verification step when a parent's mail is returned and the child has a placement file. Your case, anonymized, has become a procedure. That is what winning looks like at the systems level: a checkbox somebody else will now have to double-check.",
    "With the packet complete, Ms. Viteri drafts the February ask."],
   [C("Read the draft findings. Then the last call before court.", "packet123", setFlags=["addressFixed"])]),

 N("packet123", 40, "The ask",
   ["The ask is written as findings, in the order a judge can adopt them: that the child's mother is identified, located, and in continuous documented contact; that the surrogate determination rested on a stale address and a six-month-old checkbox; that the mother's written assertion of her role was served within the assignment window; that the evaluation consent has been exercised by the parent (or, in the version of this packet no one wants to file, remains pending by the parent's own hand); and that notices in this case shall issue to the corrected address in every system that touches Yasmin's education.",
    "It accuses no one of anything worse than architecture. Architecture, properly documented, is quite enough."],
   [C("One whiteboard session — the determinations February will actually make.", "viteri_whiteboard")]),

 N("viteri_whiteboard", 43, "What February decides",
   ["The review is a permanency hearing, and its determinations are the statute's: continuing necessity of placement, plan compliance, progress, and reasonable efforts. (42 Pa.C.S. § 6351(f)(1), (2), (3), (5.1)) \"The school question rides inside those words,\" Ms. Viteri says. \"A court deciding whether the agency made reasonable efforts is entitled to hear that its school arm spent the winter appointing a stranger to replace a mother who was sitting in its own visitor log. And a court deciding *your* progress will read your January. Everything you filed is about to be weighed as parenting. Which, in the end, is what it was.\"",
    "The agency's report arrives the next day. You read it for its school chapter first, the way everyone now reads everything."],
   [C("Read the report.", "report123")]),

 N("report123", 45, "The report's school chapter",
   ["The agency's report is, on the case plan, fair: your housing, your therapy, your fourteen visits, all credited. Its school chapter is three sentences — the district's determination described, the mother's objection 'noted,' the matter 'pending district process.' A winter of returned envelopes, forbidden candidates, and a daughter's verbatim sentence, compressed by summary into the passive voice. Reports compress; that is their nature and their defense.",
    "Which is why the packet exists: to be in the room, uncompressed, when the determinations are made. Ms. Viteri drafts the motion paragraph that will either end the surrogate question in open court or expose exactly how it survived."],
   [C("Draft it as an order: the determination withdrawn or vacated; notices to the corrected address; the parent's consent authority noted on the record.", "review_motion")]),

 N("review_motion", 47, "Drafted as an order",
   ["The motion is two pages. It asks the court to note the parent's availability on the record, to direct that education notices issue to the corrected address, and to record the disposition of the surrogate determination — withdrawn by the district, or, if the district insists on standing on it, decided by the court on the full file. For a ward of the State, the judge's own appointment power (§ 300.519(c)) is acknowledged in a footnote: the machinery exists; this record does not call for it.",
    "Whatever February does, it will now do it about documents. That transformation — from weather to documents — is the entire product of your January."],
   [C("The night before, Yasmin calls. Let her have the last word before the court has its.", "yasmin_call")]),

 N("yasmin_call", 49, "Her last word",
   ["\"If the judge asks,\" Yasmin says, \"tell her the school mom thing was weird but the test part is real. I still want the test.\" A pause, filled with fifteen years of accumulated precision. \"And tell her you live somewhere. She should have that address.\"",
    "You promise both messages, verbatim. Some exhibits a mother carries without a folder."],
   [C("Sleep. Tomorrow, the chair.", "night_before123")]),

 N("night_before123", 51, "The folder, squared",
   ["The packet, in order: July's form; two returned envelopes; fourteen signatures in a visitor log; four January letters with their receipts; a regulation with the relevant lines marked; a volunteer's honest sentence; a supervisor's open file; a daughter's page; a signed consent, or its unsigned ghost; four address confirmations. It is not a large folder, as case files go. It is large enough to hold a winter in which a mother was declared missing at her own daughter's school while visiting her every week — and to end the declaration.",
    "Tomorrow the court makes its determinations. The chair will be filled — by its owner, by a bridge, or by a mistake. By now, which of those it is has already been decided by the paper. The hearing is where the paper is read aloud."],
   [C("Go to court.", "review_day")]),

 N("review_day", 52, "Thursday, February 25",
   ["The permanency hearing makes its determinations (42 Pa.C.S. § 6351(f)) — and your case plan, fairly read, is found to be progressing. Then the school question is reached, on the fullest paper it has ever had, and the court addresses the surrogate determination directly, because the packet gives it no passive voice to hide in.",
    "The chair is filled now. By whom — and whether the evaluation it exists to authorize is moving — is the sum of your January and February, read back to you as an order."],
   [C("The file holds a located mother who wrote in time, the agency's own record of her fourteen visits, and a signed consent — the determination is withdrawn on the record and the chair was never anyone else's.", "end_signature", requiresFlags=["locatedInWriting", "consentGiven"]),
    C("The file holds a located mother and a recovered chair — and an unsigned consent form, two months into the thinking.", "end_withheld", requiresFlags=["locatedInWriting"], requiresNoFlags=["consentGiven"]),
    C("The file holds a mother's silence and a district's process — completed with the qualified volunteer, because the forbidden name was at least challenged and struck.", "end_season", requiresFlags=["conflictRaised"], requiresNoFlags=["locatedInWriting"]),
    C("The file holds returned envelopes, a checkbox, and a process that filled the chair from inside the institution the chair watches.", "end_filled_wrong")]),

 E("end_signature", 52, "Ending — Her Mother's Signature",
   ["The surrogate determination is withdrawn on the record — the district's counsel uses the word *moot*, which is institutions' dialect for *ended by a mother's paperwork*. The court's order notes your availability and corrected address as findings, directs education notices accordingly, and records that the evaluation consent has been exercised by the parent: the evaluation is scheduled, with your name on its distribution list, and Yasmin's own sentence — *I have a mom* — quoted in the colloquy by a judge who reads packets. The empty chair is filled by its owner, in open court, in writing.",
    "Name the machinery exactly. The regulation protects children when no parent can be identified, when a parent cannot be located after reasonable efforts, for wards of the State, and for unaccompanied youth (34 C.F.R. § 300.519(a)) — and every one of those predicates is a *fact to be proven*, not a mood to be presumed from returned mail. You disproved the predicate with the system's own documents: a visitor log, an October review, four January letters. You also policed the rule's boundary — the bar on surrogates employed by an agency involved in the child's care (§ 300.519(d)(2)(i)) — before it needed policing at a hearing. And you did the thing the chair exists for: you decided, and signed. The record was requested along the way (55 Pa. Code § 3130.44(d)), which is why February argued from the file instead of about it.",
    "What no strategy controls: the evaluation's findings, which may help Yasmin enormously or complicate her year; the dependency case's deeper road, which continues through your plan and its reviews; a district whose next stale form is already in a drawer somewhere. Yasmin remains placed tonight. But in every file that touches her education, her mother now exists — located, addressed, and signing — and the checkbox that erased her has been corrected in four systems and quoted in a court order. Permanence, in paperwork, is what repeated correction is called."]),

 E("end_withheld", 52, "Ending — The Consent Withheld (partial)",
   ["The court ends the surrogate question completely — your January saw to that; the determination is withdrawn, your role is noted, the chair is yours beyond argument. And then the hearing arrives at the evaluation, and the room's attention settles on the unsigned form in your folder. The judge's questions are gentle and exact. The order that results records your consent authority, directs the district to hold the evaluation open for a further thirty days, and states — in the findings, where your daughter will someday be able to read it — that the evaluation awaits the parent's decision. The obstacle has a name now, and the name is not an institution's.",
    "Do this ending the courtesy of precision. What you won was real and hard: a false predicate dismantled (34 C.F.R. § 300.519(a)), a forbidden candidate identified, a record built. The regulation's entire purpose is that a child whose parent exists should have decisions made by that parent — and that purpose is not served by the decision never being made. An evaluation is a measurement, requestable by a parent and gated by a parent's consent (34 C.F.R. § 300.301(b), (c)); declining to measure a struggling child's difficulty does not protect her from a label. It protects the label *struggling*, which she already wears, from ever being replaced by an explanation.",
    "Partial — and the most self-correcting ending in this batch, because the obstacle and the remedy are the same person, holding the same pen. Thirty days are on the order. Yasmin's sentence — *I still want the test* — is in the file, verbatim, waiting for her mother's signature to agree with it. Sign it, or refuse it on the record with reasons; either is a decision a court can respect. What the system cannot use, and a daughter cannot use, is the chair kept warm and empty at the same time."]),

 E("end_season", 52, "Ending — The Kind Stranger's Season (partial)",
   ["Mrs. Skye was appointed in late January, and she has been — as she promised a mother she had never met she would be — conscientious: she attended the meetings, asked the teachers the right questions, and consented to the evaluation in February after reading everything twice. The evaluation is underway. It will probably help Yasmin. And every one of its decisions was made, for a full season, by a kind stranger, because a mother's existence never got itself filed in the one office that was appointing her replacement. The review notes your objection to the facility candidate — the one written thing you did — and the appointment record reflects it: the qualified volunteer serves, not the institution's own coordinator. Your single intervention is visible in the outcome's shape, like a handprint in drying concrete.",
    "Read the counterfactual the way the file does. The regulation's predicate — a parent who cannot be located after reasonable efforts (34 C.F.R. § 300.519(a), (b)) — was false the whole season, and the proof of its falseness was sitting in a visitor log with your signature in it, fourteen times. Nothing was required to defeat the appointment but a dated letter asserting three facts. The objection you did file proves the paper would have been read: it struck the forbidden candidate (§ 300.519(d)(2)(i)) without argument. Paper works even when it is the only page. Imagine, the file says silently, a whole letter.",
    "Partial, and genuinely recoverable: a surrogate serves the child's education, not the parent's erasure — Mrs. Skye herself will tell the district, in writing, that a located mother ends her necessity, and parents re-enter these processes at exactly this point in real cases, with the evaluation's next stage (the program it recommends) decided at a table with the right chair filled. What the season cost is also real: a semester of decisions in a file that will describe your daughter's education as having been guided, during her mother's documented weekly visits, by an appointee. The file forgets nothing. Neither, after this winter, will you."]),

 E("end_filled_wrong", 52, "Ending — The Empty Chair, Filled Wrong",
   ["The facility's education coordinator was appointed surrogate in late January, and the appointment file contains no objection — because none was filed, by anyone, although the mother's name was in the visitor log of the appointee's own building the whole time. As surrogate she has consented to the evaluation of a child her institution houses, attended the school meetings in a room where her own program's performance is part of the context, and signed, in her two capacities, documents that will be difficult to disentangle for as long as Yasmin's record is read. The review notes the appointment as a district process, completed. The conflict that the regulation spells out in a single sentence never entered the record, because records do not raise their own objections.",
    "The sentence deserves to be read in the ending it governed: a surrogate may not be an employee of the state or local education agency, *or of any other agency that is involved in the education or care of the child*, and must have no conflicting interest. (34 C.F.R. § 300.519(d)(2)) It is not a technicality. It is the rule that keeps the watched from appointing their own watcher. Its enforcement mechanism, in a case where the district's own process produced the appointment, was a written objection from the one person positioned to file it — a person the process had already, conveniently and falsely, declared unfindable under § 300.519(a).",
    "Not sealed, because appointments can be revisited and parents located — and she is now, undeniably, located, by the crude expedient of being in this courtroom. But the evaluation's founding decisions were made inside the conflict, and later corrections argue uphill against signed consents. The doctrine of this scenario fits in the space between two facts: the system declared a weekly-visiting mother missing, and then filled her chair from inside the institution, in six weeks, without a single piece of paper objecting. Paper is not a courtesy in this system. It is the only immune response it has."]),
]
emit(123, s123_meta, s123, S, "a teenager in residential placement and a fight over who makes her education decisions. No graphic content.")

# ============================================================ S124 (Complex)
S = date(2026, 10, 19)
assert fmt(S) == "Monday, October 19, 2026"
assert fmt(S + timedelta(days=52)) == "Thursday, December 10, 2026"   # permanency hearing

s124_meta = {
    "title": "The First 90 Days",
    "subtitle": "Scenario 124 — The Whole Page (a fictional composite)",
    "startDateISO": "2026-10-19",
    "startNode": "start",
    "startCash": 140,
    "tier": "Complex",
    "summary": "You are Heather Valladolid. Your son Callum, eight, has been in foster care seven months; your trauma therapy is the spine of your case plan. The agency's new report quotes two lines from your treatment records to argue you are stalled. The lines are real. The page they were cut from says something else.",
}

s124 = [
 N("start", 0, "Two lines",
   ["The report reaches you through your lawyer, as bad paper usually does, with the two lines already underlined by someone else's pen: *Client continues to exhibit avoidance patterns. Engagement remains guarded; progress difficult to assess.* The agency's conclusion, built on them like a house on two stilts: mother's treatment has plateaued; permanency timeline should be re-examined; concurrent planning recommended.",
    "You have attended therapy since May. You have done the hardest reading of your life in that room, in order, without skipping the chapters that hurt. The report does not say you failed. It quotes your therapist's clinical shorthand, twice, and lets the quoting do the accusing."],
   [C("Read the lines again, slowly. Then call the person who wrote them — Dr. Sayegh's office.", "excerpt_anatomy")]),

 N("excerpt_anatomy", 1, "In context",
   ["You still have your own copies of the monthly summaries — treatment paperwork you requested from the start, a habit this scenario will reward. October's summary, the one quoted, contains the full sentence the report declined to carry: *Engagement remains guarded in discussion of the index events, consistent with phase-two trauma work; client is completing exposure exercises as scheduled, attendance 96%, and self-reports — corroborated by collateral — using grounding skills at home.*",
    "Two lines were quoted. The sentence they were cut from continues for four more clauses, and every clause changes the meaning. This is not falsification. It is something more common and harder to fight: excerpting — the file's way of being technically accurate and functionally false."],
   [C("Bring your copies to Dr. Sayegh. The author of the page deserves to see what the page became.", "backstory124")]),

 N("backstory124", 1, "How Callum got here",
   ["The record, without decoration: Callum's father is gone from both your lives by court order and by geography, and the year before he went was a year Callum spent listening through walls. Your own untreated trauma did the rest — the shutdowns, the missed mornings, the household drifting until the school and then the county named it neglect. The finding was, in its facts, fair. Callum has been with a foster family since April.",
    "Your plan is the standard architecture for your facts: trauma therapy (yours), play therapy (his), parenting work, visits. You have done all of it, on schedule, for seven months — which is why the word *plateaued*, arriving in the seventh month, lands like an accusation of forgery against a life you have receipts for."],
   [C("Dr. Sayegh's office. Bring the report, your copies, and your temper, in that order of usefulness.", "sayegh_office")]),

 N("sayegh_office", 2, "The author's reading",
   ["Dr. Sayegh reads the report's page twice, and her professional composure develops a visible crack. \"*Guarded* is a phase descriptor,\" she says. \"In phase two, guardedness about the index events is the *expected presentation* — it is, clinically, what doing the work looks like from inside this month. Whoever excerpted this either does not read treatment summaries professionally, or does. I cannot tell which possibility I like less.\"",
    "She offers the two instruments clinicians have: a full-context letter — the summaries' arc, phase by phase, with the quoted lines restored to their sentences — or her testimony at the December hearing. \"Letters get filed,\" she says. \"Testimony gets believed slightly more and scheduled slightly worse. Choose with your lawyer. But choose one: an excerpt unanswered becomes, in a file, the author's own summary of herself.\""],
   [C("Take both offers to Mr. Nasser, your lawyer, with the December hearing's calendar in hand.", "lawyer124")]),

 N("lawyer124", 3, "The determinations are the court's",
   ["Mr. Nasser draws the hearing the statute builds. At the permanency hearing — Thursday, December 10 — the court, not the agency's report, determines: the continuing necessity of placement; your compliance with the plan; your progress toward alleviating the circumstances that caused placement; and whether reasonable efforts were made to finalize the plan. (42 Pa.C.S. § 6351(f)(1), (2), (3), (5.1)) The agency's excerpts are evidence offered toward those determinations — and evidence can be examined, controverted, and answered. The principle is stated in the statute for disposition reports: parties may examine and controvert written reports, and cross-examine the people who made them. (42 Pa.C.S. § 6341(d)(2))",
    "\"There is a second front,\" he says. \"Page nine of the agency's packet is the scored assessment summary — one item, *caregiver-child interaction: limited warmth*, is doing work against you. It rests on a single supervised visit. There is a discovery rule — Rule 1340 — with a good-faith step, advance availability of assessments, and conferences to narrow issues. (Pa.R.J.C.P. 1340(A), (E), (F)) Lawyers use it in dependency cases. Whether it reaches a scored assessment summary has not been tested in a published opinion. I will use it, flagged as untested, because untested is not the same as unavailable — but I will not pretend to the court that it is settled law. Neither will you.\""],
   [C("Draw the whole campaign: the record, the provider, the rebuttal, the data. Then start with the record.", "nasser_whiteboard")]),

 N("nasser_whiteboard", 4, "Four fronts",
   ["The whiteboard fills in the order the hearing will care about. One: the agency's complete record — every therapy summary, every visit note, the assessment file — requested in writing, so the packet argues from the whole file. Two: Dr. Sayegh's voice, letter or testimony, restoring the excerpts to their page. Three: Callum's side — his therapist, Ms. Salazar, and the visitation center's own logs, against the single-visit warmth item. Four: the numbers — attendance, phases, certificates — the plan's compliance rendered as arithmetic.",
    "\"And underneath all four,\" Nasser says, \"the same sentence: the determinations belong to the court, on *all* the evidence. Our job is to make sure 'all' is a description of the record, not a courtesy.\""],
   [C("Front one: the record request, today.", "records124")]),

 N("records124", 5, "The whole file",
   ["The request goes out under the regulation (55 Pa. Code § 3130.44(d)) and it is specific, because specificity is what files answer: the complete case record; all treatment summaries as received by the agency; all visitation notes and the visitation center's logs; the scored assessment in full, with its item-level basis.",
    "What comes back will include the report's raw materials — and, if this case runs true to its form, the refutation of the report, filed by the agency's own correspondents, in the agency's own envelopes."],
   [C("Sign, date, send with a trail; and while the file travels, understand how the assessment got into the case.", "intake_score", setFlags=["recordsRequested"], cash=-9, addHidden=["Record — complete agency record requested in writing, including treatment summaries and assessment file"]),
    C("Ask for the record by phone to the caseworker — warmer, faster, and she knows you.", "intake_score")]),

 N("intake_score", 6, "How the summary entered",
   ["The assessment summary arrived the way such documents do: completed during the case's early weeks, attached to a court report, and quoted thereafter from report to report, acquiring authority with each copying. Its *limited warmth* item rests — as the file will show — on the supervised visit of September 12: the only visit that month scored by the rater who wrote the summary.",
    "Documents in files behave like rumors in families: the first version is the one that gets repeated at holidays. December's hearing is, among other things, an attempt to introduce the summary to its own footnotes."],
   [C("While the record travels: sit in on what phase two actually looks like, so you can describe it when it is misdescribed.", "phase_two")]),

 N("phase_two", 8, "Phase two",
   ["A Tuesday session, for the record the hearing will never see and the mother will never forget: the exposure work is exactly as bad as promised and exactly as scheduled; you do the grounding exercise with your hands shaking in the ordinary way; Dr. Sayegh notes the attendance, the completion, the presentation — *guarded*, yes, in the clinical sense of a person holding a door against weather while she repairs the house behind it.",
    "This is the work the excerpt called a plateau. Anyone who has done it recognizes the description problem instantly: from outside, in summary, in two lines, *doing the hardest part* and *stuck* are spelled almost identically. The difference exists only in context — which is why context is the whole fight."],
   [C("The record arrives. Read it like a prosecutor of your own case.", "file_arrives")]),

 N("file_arrives", 10, "Six envelopes",
   ["The agency's production is complete in the way of files that have never expected to be read by their subject: six monthly treatment summaries (the full arc, phase by phase, the quoted October lines sitting visibly inside their sentences); Ms. Salazar's quarterly letters (unquoted by the report, for reasons the report does not give); the visitation center's logs; and the assessment summary with its item sheet — Item 9, *limited warmth*, sourced, in the rater's own note, to *visit of 9/12, observed flat affect, limited physical affection*.",
    "Nasser reads the production once and says the sentence lawyers say when the other side's file contains your case: \"They kept everything. People who keep everything believe the file is theirs. December is when we introduce the file to its subject.\""],
   [C("Reconstruct September 12 — the scored visit — from the visitation center's own paper.", "visit_sep12")]),

 N("visit_sep12", 12, "September 12",
   ["The visitation center's log for September 12 is three-quarters of a page in a staff member's even hand. Callum arrived with a cold, listless, wanting mostly to lean. You read to him for ninety minutes because leaning was what he had. Your employer's letter — kept, fortunately, in your own folder — shows why you were grey-faced yourself: a double shift the night before, taken because refusing shifts is how warehouse hours evaporate.",
    "The rater scored the month's quietest hour. The log, read whole, describes a sick child being read to by an exhausted mother who showed up — which is, in most vocabularies the English language keeps, a description of warmth operating under load."],
   [C("Get the center's full logs — every visit, not just the scored one.", "visit_center_logs")]),

 N("visit_center_logs", 13, "Eleven visits",
   ["The center's complete log runs to eleven visits, and it is the most quietly devastating document in the case: the other ten. Callum arriving at a run. The breathing game you taught him — *smell the flower, blow the candle* — now part of the center staff's own repertoire with other children. The September 26 visit, two weeks after the scored one, in the same observer's hand: *child sought lap, sustained play, difficult goodbye (positive indicator)*.",
    "Item 9's evidence base is one visit. The rebuttal's is eleven. The difference between those numbers is the difference between a score and a sample, and December's packet exists to make a judge do that arithmetic out loud."],
   [C("Now Callum's therapist — Ms. Salazar has been writing letters nobody quoted.", "boateng_call", setFlags=["visitLogs"])]),

 N("boateng_call", 14, "Ms. Salazar's letters",
   ["Ms. Salazar's quarterly letters are everything the report's excerpts are not: longitudinal, specific, and boring in the way of genuine clinical progress. Callum's drawings have changed their weather — the house has a door now, and the figures have hands; his school functioning has measurably steadied; his attachment presentation in session, she writes, is *organized around the mother as the safe figure*, a sentence she underlined herself, in anticipation, apparently, of exactly this fight.",
    "\"I send these to the agency every quarter,\" she says. \"I have never once seen one quoted. I had begun to think quoting was against the rules.\" It is not against the rules. It is against the narrative — which is why her letter goes in the packet whole, with her offer to testify behind it."],
   [C("Ask her to write one more — current, addressed to the court, with the school observations included.", "sayegh_letter", setFlags=["therapistLetter"]),
    C("The quarterly letters are enough paper; don't make a therapist into a pen pal.", "sayegh_letter")]),

 N("sayegh_letter", 17, "Letter or witness",
   ["The Sayegh decision, with Nasser, on the calendar's evidence: December is crowded; the hearing is fixed; clinicians' schedules are weather systems of their own. The letter can be long, precise, and filed in advance — phase arc, the excerpts restored, attendance arithmetic, the prognosis stated in professional language. Testimony can be cross-examined — which cuts both ways: it exposes her to the agency's questions, and it lets the court watch the author of the two most-quoted lines in the case explain what she wrote.",
    "\"The letter is a document,\" Nasser says. \"The witness is an event. Judges remember events; files preserve documents. Given that December is a hearing and not a memoir, I lean event — but the letter is the safer artifact, and safe artifacts are what records are.\""],
   [C("The letter: full-context, filed in advance, with the complete summaries attached as her own exhibits.", "data_pull", setFlags=["providerLetter"]),
    C("The testimony: Dr. Sayegh live, cross-examination and all — the author defending her page in person.", "data_pull", setFlags=["providerTestified"])]),

 N("data_pull", 20, "Arithmetic",
   ["The compliance chapter assembles itself from the records nobody excerpted: therapy attendance 96% across six months; phase one complete, phase two two-thirds through, on the clinician's own schedule; the parenting program certificate, dated October; visits attended eleven of eleven. Nasser arranges the numbers in a single table with the report's two lines above it, and the table does what tables do: it makes the excerpts look like what they are — a sample of two, drawn from the one document genre in the file whose dialect is pessimism.",
    "\"Clinicians write *guarded* the way pilots write *turbulence*,\" Nasser says. \"It describes the working conditions, not the flight. December's judge has flown. We just have to show her the whole route map.\""],
   [C("Attach the employer's letter for September 12 — the double shift, documented.", "employer_letter", setFlags=["progressData"]),
    C("Numbers are numbers; the table stands without the shift letter.", "employer_letter")]),

 N("employer_letter", 22, "The double shift",
   ["Your employer's letter is one paragraph of warehouse prose: on September 11–12 you worked sixteen hours across two shifts, at the employer's request, with the schedule printout attached. It does not argue anything. It simply makes it impossible, in December, for a flat-affect observation of a woman who had been awake for most of a day and night to circulate as a finding about her warmth toward her son.",
    "Context is not excuse. Context is the difference between evidence and anecdote — the whole case, in one attachment."],
   [C("Now the assessment front: the Rule 1340 track, handled with its untested flag flying.", "assessment_fight")]),

 N("assessment_fight", 24, "The good-faith step",
   ["Rule 1340's structure is civility with deadlines: before motions, a good-faith effort between the parties to resolve the discovery question (Rule 1340(A)); assessments used in the proceeding to be available to all parties in advance of the pre-hearing conference (Rule 1340(E)); conferences to narrow the issues. (Rule 1340(F)) Nasser's good-faith letter is a model of the genre — it asks for Item 9's basis materials, proposes the visitation logs as the shared factual ground, and states the rebuttal's thesis in one line: *a single-visit sample, contradicted by the center's own eleven-visit record*.",
    "It also states, in a footnote Nasser insists on, that the rule's application to a scored assessment summary is untested in the published opinions — because a letter that concedes its own frontier is believed about everything else."],
   [C("Send it — with the eleven-visit log table attached, so the good faith is documented, not described.", "redaction_fight", setFlags=["rebuttalFiled"], cash=-7, addHidden=["Assessment — Rule 1340 rebuttal of single-visit item filed with visitation logs; untested application flagged in writing"]),
    C("Hold the rebuttal for the hearing itself — surprise is a weapon too, and the logs will keep.", "redaction_fight")]),

 N("redaction_fight", 27, "The black bars",
   ["The agency's response to the good-faith step is partial in the instructive way: the assessment itself is produced in advance of the conference (Rule 1340(E)) — with the rater's notes redacted under a privacy rationale. Nasser's reply is two paragraphs, and the second is a quotation: the record regulation is not to be read to protect agency employees' privacy as a basis for withholding. (55 Pa. Code § 3130.44(f)) The notes arrive the following week, lightly re-redacted — and the rater's own fuller note contains the sentence the summary dropped: *9/12 visit atypical — child ill, mother post-shift; recommend re-observation before scoring interaction items.*",
    "The file knew. The file, as in every scenario in this library, knew the whole time — in a drawer, in a note, in a fuller sentence. The packet's work is never to create the truth. It is to introduce the file's parts to one another in front of a judge."],
   [C("Add Callum's school counselor's note to the packet — one more primary observer.", "school_counselor")]),

 N("school_counselor", 29, "The counselor's note",
   ["Callum's school counselor writes in the plain style of people who watch children for a living: his mornings have steadied since September; he talks about the breathing game; when the class drew *who keeps me safe*, he drew you, with the book — the September visit, the one scored as limited warmth, is literally pictured on his classroom's wall, captioned by its subject.",
    "Nasser files it without comment. Some exhibits argue. This one just stands in the room."],
   [C("Into the Rule 1340 conference — the narrowing machine.", "conference124")]),

 N("conference124", 31, "Narrowed",
   ["The pre-hearing conference does what Rule 1340(F) builds conferences to do: it narrows. The agency will not withdraw Item 9 — supervisors and face are involved — but it stipulates to the visitation logs' authenticity, to the rater note's existence, and to Dr. Sayegh's summaries being received whole rather than excerpted, which is ninety percent of the war conceded in a conference room with no judge present. What remains for December is genuinely narrowed: the weight of one redacted-then-unredacted item, and the question whether two quoted lines can carry a *progress* finding against a six-month arc.",
    "Narrowing is an unglamorous victory. It is also the kind that survives contact with a hearing."],
   [C("The agency's final report lands next. Read what narrowing did to it — and what it didn't.", "fivemoreminutes")]),

 N("fivemoreminutes", 33, "Contextualized",
   ["The agency's counsel, in a hallway conversation Nasser reports verbatim, offers a peace: the final report will 'contextualize' the therapy quotations. The contextualized draft, when it arrives, restores exactly one clause — *attendance 96%* — and retains *plateaued* as its verb. Nasser declines the peace in writing, politely: the packet will supply its own context, from the documents, in the room.",
    "Offers like that are data: they tell you the other side has read the whole page too, and priced what it would cost them if a judge did."],
   [C("Read the final report in full — every page, the night it lands.", "agency_position")]),

 N("agency_position", 35, "The final report",
   ["The final report is the excerpt version with better manners: the arc is acknowledged, the certificate is listed — and the recommendation stands unchanged, resting where it always rested, on the two lines and Item 9. Concurrent planning language remains. The report is not dishonest. It is something more durable than dishonesty: it is a conclusion that was reached in October, defended thereafter by the selection of evidence, in good faith, by professionals who had a file they never re-read whole.",
    "December exists to make somebody re-read it whole, in public, in order. That somebody is a judge, and the re-reading is your packet."],
   [C("One more visit before December. Go be, briefly and entirely, not a litigant.", "visit_room_oct")]),

 N("visit_room_oct", 36, "The breathing game",
   ["The visitation center, late November: Callum teaches the breathing game to a new child in the corner, with a supervisor's smile over both of them — *smell the flower, blow the candle* — and the log for this visit, written by the same hand that wrote September 12's, will say *child regulated peer; mother-child play sustained; goodbye routine*. It goes in the packet as the logs' last page, unedited.",
    "You do not perform for the log. That is what makes the log worth filing. The packet's deepest claim is not that September 12 was misread — it is that eleven visits read together describe a relationship no single hour can assassinate."],
   [C("Assemble the packet: excerpts against pages, samples against populations.", "rowan_day")]),

 N("rowan_day", 38, "His sentence",
   ["Callum's contribution to the packet is unsolicited and, his therapist rules, admissible in the court of his mother regardless of any other: a drawing, captioned in his handwriting with Ms. Salazar's help — *MOM DOES THE BREATHING WITH ME* — the house with a door, the figures with hands, the book between them. It goes into the packet behind Ms. Salazar's letter, where sentiment is anchored to the clinical record rather than floating free of it.",
    "Eight-year-olds do not write strategy. They write findings, in crayon, and the system's adults spend December deciding whether the crayon agrees with the excerpts."],
   [C("Ask the guardian ad litem where the packet has moved her.", "gal124")]),

 N("gal124", 40, "The guardian ad litem, moved",
   ["The GAL's trajectory across the autumn is the packet's quietest evidence: she began, by her own admission, 'excerpt-persuaded' — the report's two lines are professionally shaped persuasion — and has been moved, document by document, to a different position. The Salazar letters did part of it. The rater's own *recommend re-observation* note did the rest. \"I read files for a living,\" she says. \"This is the first time this year the file read back.\"",
    "Her support at the hearing is not a favor. It is what happens to honest readers exposed to complete records — which is the entire theory of your December, stated by its most skeptical witness."],
   [C("Final assembly. The packet, in the statute's order.", "sayegh_prep")]),

 N("sayegh_prep", 41, "The author, ready",
   ["Whether Dr. Sayegh's voice arrives as a filed letter or a live witness, its content is the same three movements: the arc (phases, attendance, the work's internal logic); the lines (each excerpt restored to its sentence, each sentence to its month); and the prognosis, stated with a clinician's care — the trajectory is the treatment working, and interruptions to the attachment now would be, in her professional judgment, the risk the report claims to be managing.",
    "Nasser's instruction to both versions is identical: *No advocacy. Authorship.* The author of the page is not there to win. She is there to make the page whole — and the wholeness does the winning by itself."],
   [C("Build the packet.", "packet124")]),

 N("packet124", 44, "In the statute's order",
   ["The packet is arranged to answer the determinations in their statutory sequence. Necessity: the arc and the attachment record. Compliance: the arithmetic table. Progress: the whole page — summaries entire, the provider's voice, the therapist's letters, the counselor's note, a drawing with hands on its figures. Efforts: the agency's own — including an assessment item its rater flagged for re-observation, carried into a court report unre-observed. The rebuttal of Item 9 sits at the back, logs attached, its untested-rule footnote intact.",
    "It is the heaviest packet you have carried in this case. Weight, here, is not the argument. Alignment is: fifteen documents, four institutions, one story, zero excerpts."],
   [C("Add your own page — one, measured, signed — and close the folder.", "mother_statement", cash=-5)]),

 N("mother_statement", 46, "One page",
   ["Your statement is a page long because you cut it four times. It does not accuse the report of lying. It says what you did, month by month; what the therapy is, in a patient's words; what Callum is like now, in a mother's; and it closes with the sentence the whole packet exists to make true: *I am asking the court to decide from the whole record, including the parts of my own file that are hard to read. I have read them. They are in the packet too.*",
    "Candor is the packet's binding. A mother who files her own hard pages cannot be excerpted — there is nothing left to cut her sentences from that she has not already handed over whole."],
   [C("The eve of the hearing: the agency asks for time.", "rowan_question")]),

 N("rowan_question", 47, "What will the judge read",
   ["Callum's question arrives through the foster mother, at bedtime, in the faithful relay of eight-year-old intelligence services: *What will the judge read about us?* You answer it at Saturday's visit in the only terms that are both true and his size: \"She'll read the whole book, not just two sentences. That's what we spent the fall doing — putting the whole book in her hands.\"",
    "He considers this with the seriousness it deserves. \"Two sentences is not a book,\" he says — a literary judgment the packet could not have improved on, from its smallest cited authority."],
   [C("Carry that sentence into the last evening before court.", "continuance_choice")]),

 N("continuance_choice", 49, "The continuance",
   ["The agency's counsel calls Nasser on the eve: a continuance of the permanency hearing, thirty days, 'to allow the assessment issue to be further reviewed internally.' It is, depending on the reader, a concession wearing a scheduling costume — or an attempt to let December's assembled record cool. Nasser lays out the trade without dressing it: agree, and the review of Item 9 might quietly fix the file without a hearing's risks; oppose, and December 10 happens with the packet at full strength and the court's patience unspent.",
    "Either road reaches a hearing. They differ in what the hearing finds already done."],
   [C("Oppose. The record is built; the determinations are December's to make.", "night_before124"),
    C("Consent. Thirty days of internal review might correct the file — and a corrected file needs no one's cross-examination.", "night_before124")]),

 N("night_before124", 51, "The whole page",
   ["You read the packet once, end to end, in the order the judge will: the claim, the arc, the arithmetic, the pages entire. Somewhere in the middle, October's summary passes with its two famous lines sitting in their sentence like stones returned to a wall. You think about how the case will be described by whoever writes its next summary — and that December is, at bottom, a fight over who does the summarizing, and from how much of the page.",
    "Tomorrow, the court does it. From the whole record, or from the excerpts. That is the only question left, and you have spent two months making sure it is a real one."],
   [C("Go to court.", "hearing_day")]),

 N("hearing_day", 52, "Thursday, December 10",
   ["The permanency hearing makes the statute's determinations in their order — necessity, compliance, progress, efforts. (42 Pa.C.S. § 6351(f)(1), (2), (3), (5.1)) The agency's report is presented, its excerpts read aloud — where, in the room's acoustics, they sound thinner than they did on paper. Then the packet is presented: the pages entire, the author or her letter, the logs, the note that recommended re-observation, the arithmetic.",
    "The findings will now be written from whichever version of the record the court credits. That is not a metaphor. Findings are, literally, the sentences a judge writes — and the only thing that has ever decided which sentences get written is what was in the room to be read."],
   [C("The court finds from the whole record: six summaries entire, a provider's full context, eleven visits of logs, a rater's own caveat, and a mother's candor — the excerpts answered by their page.", "end_whole_page", requiresFlags=["providerLetter", "rebuttalFiled"]),
    C("The court credits the provider's live testimony — the arc is believed — but Item 9 stands unrebutted in the assessment file, and the return waits for a re-observation that has not happened.", "end_testimony", requiresFlags=["providerTestified"], requiresNoFlags=["rebuttalFiled"]),
    C("The court splits the record: compliance found, progress 'not yet demonstrated to the court's satisfaction' — the rebuttal landed, the provider's context never arrived in citable form.", "end_split", requiresFlags=["rebuttalFiled"], requiresNoFlags=["providerLetter"]),
    C("The court reads the report's version: two lines, one item, and a recommendation that met no organized answer.", "end_excerpts")]),

 E("end_whole_page", 52, "Ending — The Whole Page, Read Aloud",
   ["The findings come in the statute's order, and each one cites the record that carried it. Compliance: found — the arithmetic table, undisputed. Progress toward alleviating the circumstances of placement (42 Pa.C.S. § 6351(f)(3)): found — on the treatment arc read entire, the provider's full context, and the attachment record of eleven logged visits. On efforts, the court's sentence is dry and permanent: the assessment item relied upon had been flagged by its own rater for re-observation, and was carried into a court report unre-observed. The order is a stepped return: overnights beginning in January, Callum home by spring if the steps hold, therapy continuing through the transition on Dr. Sayegh's stated plan.",
    "Name the doctrine precisely, because this ending is its cleanest statement in the library. Nothing was falsified; everything was *excerpted* — and excerpting is defeated not by indignation but by completeness, filed in advance, in the statute's order: the complete record requested (55 Pa. Code § 3130.44(d)); the author restored to her page; reports examined and controverted as the disposition principle contemplates (42 Pa.C.S. § 6341(d)(2)); a single-visit score answered by its population of visits, through a discovery rule whose reach to that score was flagged, in writing, as untested. (Pa.R.J.C.P. 1340(A), (E), (F)) The court did not find that the agency lied. It found, from the whole record, that the truth was longer than the quotations. Those are different findings, and the second is the one that brings children home.",
    "What no strategy controls: the therapy's remaining work, which is real; a different judge's reading of the same page; the spring's steps, which must still be walked. Callum is not home tonight. But the file that will describe this family from now on describes it whole — and every future excerpt will have to reckon with a record that has already survived being read entire, in court, once. That is what a permanency record is for. That is what this one now is."]),

 E("end_testimony", 52, "Ending — Believed, and Waiting (partial)",
   ["Dr. Sayegh's testimony does what testimony does at its best: the arc becomes a narrative a court can hold, the two lines are restored to their sentences by their author under oath, and the progress finding is made — (42 Pa.C.S. § 6351(f)(3)) — in terms the agency's counsel does not seriously contest by the end. The return, however, is not ordered. It waits on a loose thread the packet left dangling: Item 9 stands in the assessment file unrebutted, its rater's *recommend re-observation* note never forced into the open, because the Rule 1340 track — the good-faith letter, the conference, the logs — was never run. The court orders the re-observation completed and reviewed in ninety days, and the stepped return is keyed to its result.",
    "The accounting is specific. Testimony persuades judges about people; documents corner institutions about paper. The assessment item was a paper problem — a sample of one visit, contradicted by ten others, caveated by its own author — and paper problems are solved by the discovery machinery (Pa.R.J.C.P. 1340(A), (E), (F)), with the application to a scored summary honestly flagged as untested, not by oratory. Leaving that machinery idle left the item standing as the file's one unexamined 'fact,' and courts key orders to unexamined facts with reluctance to move at all until they are examined.",
    "Partial, with the delay measured in a season rather than a year — and with the re-observation now court-ordered, which means the logs will be read by the institution that wrote them. Callum's spring may yet match the winning ending's; it will arrive by a road with one extra review on it. The lesson is about completeness of fronts: this scenario had four, and the one left idle was the one the order hung on. Files are patient. They wait for the front you skip."]),

 E("end_split", 52, "Ending — Split Findings (partial)",
   ["The findings divide the case at its waist. Compliance: found, on the arithmetic — undisputed, and credited to you in terms. Progress: *not yet demonstrated to the court's satisfaction* — the therapy arc, argued by counsel from summaries the court had not been given in citable, provider-voiced form, is weighed against the report's excerpts and found, in the judge's phrase, 'a dispute the court cannot resolve on quotations alone.' Item 9 falls — the rebuttal's logs see to that, and the assessment is ordered corrected — but a fallen item cannot carry a progress finding by itself. Placement continues; overnights are deferred to the next review; the packet's missing front is named in the order's logic for anyone who reads it.",
    "The diagnosis is a doctrine of this library: unanswered excerpts become findings; answered excerpts become disputes; and disputes are resolved by *voices with standing* — the author of the page, in a letter filed in advance or on the stand, whose context a court can cite. Ms. Salazar's letters and the logs did real work here; Dr. Sayegh's silence did the rest. A clinician's two lines, quoted against her patient, required the clinician's whole voice in reply — and that voice existed, offered in October, at the price of one decision the packet never made.",
    "Partial, and pointed: the next review is ninety days out, the assessment is corrected, the compliance finding is banked, and the missing exhibit has a name, an office, and a standing offer to write or appear. Nothing about this ending is mysterious, which is its usefulness. In a paper system, the unanswered page and the unanswered excerpt are the same wound — and both are closed the same way: by the author, in writing, before the hearing, in the file."]),

 E("end_excerpts", 52, "Ending — The Excerpts Stand",
   ["The hearing is shorter than the preparation for it was long in the other versions of this autumn, because there is less in the room. The report's two lines are read. The assessment's item is cited. Counsel argues context from memory and principle — the summaries exist, the logs exist, the author could explain — but existence argued is not existence filed, and the court's findings track the only version of the record that was actually placed before it: progress *not demonstrated*; placement's necessity *continuing*; concurrent planning language adopted, so that the file now formally walks toward two futures, one of which ends the family it describes.",
    "Read the mechanics without consolation. Every document that defeats this ending existed by October: six summaries with their sentences intact, a rater's caveat, eleven visits of logs, a therapist's unquoted letters, a clinician ready to write or appear. The record that contains them was releasable on a written request (55 Pa. Code § 3130.44(d)); the request was the cheapest document in the case, and it was never sent — or sent and then not followed by the building. Courts cannot find facts from files that are described to them. They find facts from files. The distinction is the whole game this library teaches, and this ending is its tuition.",
    "Not sealed — reviews recur, records can still be requested, authors can still write, and concurrent planning is a direction, not a decree. But the excerpts now have the force of findings, and findings are quoted forward by every subsequent report as the court's own words. The next fight starts uphill, against the judiciary's prose, in a case whose underlying facts never changed. Two lines did this. They will be quoted in this file for years — unless the whole page, filed at last, outquotes them."]),
]
emit(124, s124_meta, s124, S, "a parent's therapy records quoted in a permanency fight, and a scored assessment item. No graphic content.")
print("done")
