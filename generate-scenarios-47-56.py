#!/usr/bin/env python3
"""Generate scenarios 47-56 (Wave 1, Batch 2: Placement & Kinship) for
'The First 90 Days' — JSON + node-for-node script, following the v1 pattern
(see generate-scenarios-33-34.py). Fictional composites only."""
import json
from datetime import date, timedelta

GAME_DIR = "/home/hatch/workspace/your_files/tacticwatch-game"

def fmt(d):
    return d.strftime("%A, %B %-d, %Y")

def build(meta, raw_nodes, start):
    nodes = []
    for nd in raw_nodes:
        d = start + timedelta(days=nd["off"])
        item = {"id": nd["id"],
                "kicker": f"Day {nd['off']} — {fmt(d)}",
                "dayOffset": nd["off"],
                "title": nd["title"]}
        if nd.get("ending"):
            item["ending"] = True
            item["body"] = []
            item["debrief"] = nd["debrief"]
        else:
            item["body"] = nd["body"]
            item["choices"] = nd["choices"]
        nodes.append(item)
    return {"meta": meta, "nodes": nodes}

def N(id, off, title, body, choices):
    return {"id": id, "off": off, "title": title, "body": body, "choices": choices}

def C(text, next, **fx):
    c = {"text": text, "next": next}
    c.update(fx)
    return c

def E(id, off, title, debrief):
    return {"id": id, "off": off, "title": title, "ending": True, "debrief": debrief}

# ============================================================ S47 (Foundation)
S = date(2026, 3, 9)
assert fmt(S) == "Monday, March 9, 2026"
SHELTER = S + timedelta(days=3)
assert fmt(SHELTER) == "Thursday, March 12, 2026"   # within 72 hours of the night placement

s47_meta = {
    "title": "The First 90 Days",
    "subtitle": "Scenario 47 — The First Night (a fictional composite)",
    "startDateISO": "2026-03-09",
    "startNode": "start",
    "startCash": 140,
    "tier": "Foundation",
    "summary": "You are Renata. Your sitter canceled, your shift did not, and your seven-year-old was home alone for part of one evening. Tonight a caseworker is deciding where Ines sleeps — and whether the first name the file ever holds is your sister's.",
}
s47 = [
 N("start", 0, "6:40 p.m.",
   ["Your sitter's text came at 6:12, while you were already on the bus to the diner: her car died, she cannot come. Ines is seven. She has been alone before for twenty minutes while you ran to the corner store, never for a whole shift, and you told yourself the whole ride that the neighbor upstairs would check in — she always does at seven.",
    "At 6:40 there is a knock that is not Mrs. Halloway's. A county caseworker, Ms. Krajewski, stands with a police officer and explains, evenly, that a caller reported a child alone in the apartment. Ines is on the couch with her tablet, fed, unhurt, and frightened mostly by the uniforms."],
   [C("Cooperate. Let them in, answer plainly, and say nothing you would not want written down.", "the_checklist")]),
 N("the_checklist", 0, "The checklist",
   ["Ms. Krajewski works through a form on a tablet: who lives here, who watches Ines, Ines's school, her doctor. The questions are ordinary. The tablet is not. Everything you say is becoming the first page of a file that will outlive this night, and it will be quoted back at you in rooms you have not seen yet.",
    "She asks the question the form saves for last: \"Is there a relative or another adult Ines knows well — someone she could stay with tonight, if it comes to that?\""],
   [C("Answer it in full — out loud and in writing on her form: \"My sister, Yolanda Reyes. She lives ten minutes away. Ines stays with her every other weekend. Here is her number — write it exactly like this.\"", "named_in_writing", setFlags=["auntNamedEarly"], addHidden=["named-kin"]),
    C("Answer out loud, carefully: \"My sister Yolanda. She is close with Ines.\" You assume the tablet caught it.", "named_outloud")]),
 N("named_outloud", 0, "What the tablet caught",
   ["Ms. Krajewski nods and keeps typing. What the form will actually hold, you cannot see from where you stand — and a name spoken in a doorway at night has a way of becoming, in the file, \"mother states sister may be available.\" No number. No address. Nobody will fault the worker; the night is full of doorways.",
    "You can still fix it before she leaves — if you think of it."],
   [C("Ask her to add the number and address to the form now, and to read back what the form says about your sister.", "named_in_writing", setFlags=["auntNamedEarly"], addHidden=["named-kin"]),
    C("Let it stand. She said she would note it, and tonight is not the night to argue with the person holding the pen.", "the_decision")]),
 N("named_in_writing", 0, "Ink, not air",
   ["Ms. Krajewski reads it back: Yolanda Reyes, address, phone, \"maternal aunt; child stays with her regularly; mother requests aunt be contacted first.\" It is eleven words longer than a name spoken aloud, and it is the eleven words that will still exist on Thursday.",
    "Names in a file get called. Names in the air get remembered, sometimes."],
   [C("Thank her, and ask what happens next, step by step.", "the_decision")]),
 N("the_decision", 0, "The decision",
   ["The decision comes inside the hour, and it is not the one you prayed for: Ines cannot stay here tonight. The county is taking emergency custody, and a judge will review it at a shelter care hearing that must happen within 72 hours — by Thursday. The law behind that clock is 23 Pa.C.S. § 6315(d) and 42 Pa.C.S. § 6332, though tonight nobody says the citations out loud.",
    "Where Ines sleeps until Thursday is a separate question from whether she had to leave — and it is the question your next hour is about."],
   [C("Ask it plainly: \"Before any foster home — will you call my sister tonight?\"", "the_call")]),
 N("the_call", 0, "The call",
   ["Ms. Krajewski calls Yolanda from your kitchen table. Yolanda answers on the second ring, and does not hesitate: \"Tell me what she needs. I am coming.\" What Yolanda cannot do tonight is pass, on the spot, every check the county runs before a child sleeps in a kinship home — some of those checks simply take days, and a Tuesday night cannot be argued into a Thursday.",
    "Ines will sleep tonight in an emergency foster home, with a kind stranger named Mrs. Halloway. The fight is not about tonight anymore. It is about Thursday — and about what is ready by then."],
   [C("Pack Ines's bag yourself: her blanket, her school clothes, the stuffed fox. Put Yolanda's number in the front pocket, on paper.", "the_bag", cash=-0, addHidden=["child-comfort"])]),
 N("the_bag", 0, "The bag",
   ["You pack like a woman who has done it for weekends at her sister's, because you have. Ines holds the fox and asks if Aunt Yo's couch bed counts as a sleepover. You say: Thursday, baby. First a judge listens, then sleepovers.",
    "Ms. Krajewski gives you a paper with a court date and a name you do not recognize — and one instruction worth more than the paper: \"Call the public defender's office in the morning. You are entitled to a lawyer.\""],
   [C("Write Yolanda's number on the back of the court paper too. Paper goes where you go.", "morning")]),
 N("morning", 1, "The public defender's office",
   ["Ms. Fontaine, the attorney the court appoints for you, has the file's first pages before you sit down. The right is not a favor: in a dependency case you are entitled to counsel — 42 Pa.C.S. § 6337 guarantees it for parents, and § 6332(a) does the same at the shelter care stage. Ms. Fontaine reads the doorway page twice.",
    "\"Thursday is a shelter care hearing,\" she says. \"The judge decides whether Ines stays in care at all — and if she does, where. The where is a real question at shelter care, not a detail for later.\""],
   [C("\"Then where is my whole case. What does the judge need to see by Thursday?\"", "what_judge_needs")]),
 N("what_judge_needs", 1, "What the judge needs",
   ["\"Three things,\" Ms. Fontaine says. \"Your sister, in the courtroom or on the phone, saying yes out loud. Whatever checks the agency can finish by Thursday, finished — which means your sister calls them tomorrow morning, not the other way around. And a childcare plan from you that is not 'it won't happen again' — names, shifts, backups. Judges place children with plans, not promises.\"",
    "She slides a card across the desk: the agency's records office. \"And one more thing. You may ask for your record. Parents ask; agencies produce. Ask early.\""],
   [C("Call Yolanda before you leave the office. Put her on the phone with Ms. Fontaine.", "sister_calls", setFlags=["sisterEngaged"]),
    C("Take the card and go home to think. Thursday feels far away.", "thinking")]),
 N("thinking", 1, "Thinking",
   ["Home is quiet in the wrong way. Ines's cup is still in the sink. You think for an evening, and the thinking costs a day — the checks that could have started Wednesday morning will now start Wednesday afternoon, and Thursday does not move for anybody.",
    "By Wednesday you are doing everything on Ms. Fontaine's list anyway. You are just doing it a day poorer."],
   [C("Do the list. All of it, a day late.", "sister_calls", setFlags=["sisterEngaged"])]),
 N("sister_calls", 2, "Yolanda goes first",
   ["Yolanda does not wait to be found. She calls the agency Wednesday morning, gives her clearances information, opens her door for a walk-through that afternoon, and says the sentence kinship runs on: \"She has a bed here. She has always had a bed here.\" The walk-through notes a home that a seven-year-old already knows — her toothbrush is in the bathroom.",
    "Ms. Fontaine files a one-page request ahead of the hearing: if care continues, placement with the maternal aunt — the relative named in the file from the first night."],
   [C("Spend Wednesday evening writing your childcare plan: the sitter, the backup sitter, Yolanda, and your manager's letter about the shift swap.", "the_plan", cash=-6)]),
 N("the_plan", 2, "The plan, on paper",
   ["It takes two pages. Primary sitter, with a phone number. Backup: the neighbor on the third floor, asked and agreed, in writing. Yolanda as emergency contact for any gap longer than an hour. And your manager's letter: your Tuesday and Thursday shifts move to daytime for ninety days, signed.",
    "It is not an apology. It is better than an apology. It is a system."],
   [C("Give a copy to Ms. Fontaine. Keep the original.", "records_ask")]),
 N("records_ask", 2, "One more envelope",
   ["Ms. Fontaine asks if you want the agency's record started toward you now. \"Pennsylvania's regulation gives a parent the right to ask for their child's and their own case record in writing — 55 Pa. Code § 3130.44(d). What Thursday decides will be written down. You should be able to read what was written.\"",
    "The request takes four lines and a stamp."],
   [C("Sign it and mail it today.", "hearing_day", setFlags=["recordsRequested"], addHidden=["record-request"]),
    C("Skip it. Thursday is the fight; paper can wait.", "hearing_day")]),
 N("hearing_day", 3, "Thursday",
   ["The courtroom is small and the clock on the wall is loud. Ms. Krajewski testifies first: a child alone, a sitter who canceled, a mother who cooperated. Then Ms. Fontaine presents the plan, the manager's letter — and calls on Yolanda, sitting in the second row with her clearance paperwork in a folder on her knees.",
    "The judge looks at the agency. \"Counsel, the aunt. Where are we?\""],
   [C("Listen. This is the moment the first night built — or didn't.", "hearing_outcome")]),
 N("hearing_outcome", 3, "The question",
   ["Everything since Monday narrows to what the file can prove about your sister: whether she was named early enough to be checked, engaged enough to be ready, and standing close enough to be heard. The judge turns the pages of the doorway form.",
    "What happens next is decided by what is actually in front of her."],
   [C("The file names Yolanda from the first night, with her number — and she is here, checks underway, asking to be heard about taking Ines tonight.", "end_kin", requiresFlags=["auntNamedEarly", "sisterEngaged"]),
    C("The file is thinner than that — a sister mentioned, a study barely begun.", "end_wait")]),
 E("end_kin", 3, "Ending — Home by Thursday",
   ["The judge continues Ines's care — the night alone was real, and no judge waves it away — but orders her placed with Yolanda tonight, with the kinship approval to be completed on a date the court sets and says out loud. Ines's sleepover ruling comes with rules: your plan governs, your shifts are day shifts, and any childcare gap goes to the names on your two pages, in order.",
    "You have won the outcome this scenario exists to teach: in an emergency, the placement fight is won or lost in the first hours. The law gave you the clock — a shelter care hearing within 72 hours (42 Pa.C.S. § 6332; 23 Pa.C.S. § 6315(d)) and a lawyer to stand with you (42 Pa.C.S. § 6337; § 6332(a)). The rest was sequence: the relative named in writing at the door, the relative who called the agency before the agency called her, and a plan with names in it. Caseworkers change; the first page of the file does not.",
    "What no strategy controls: the judge. A different judge could have kept Ines in the foster home until the aunt's approval was complete, on the same papers. What the early naming bought was not a guarantee — it bought the question being asked at all, on Thursday instead of next month."]),
 E("end_wait", 10, "Ending — Named Too Late (partial)",
   ["The judge continues Ines's care and keeps her with Mrs. Halloway for now — kindly, and with a date: the aunt's study is ordered opened, kinship placement to be revisited at a review in ten days if the checks are complete. It is not a loss. It is the same road, walked ten days longer, with a seven-year-old sleeping at a stranger's in between.",
    "Read the debrief honestly: nothing about Yolanda changed between the two endings. Her house, her heart, and her toothbrush were identical. What changed was when the file learned her name in a form the system could act on — a name spoken in a doorway became \"may be available,\" and maybes do not get clearance appointments. The shelter care clock (within 72 hours — 42 Pa.C.S. § 6332; 23 Pa.C.S. § 6315(d)) protects the hearing. It does not protect the placement. That part is yours, and it starts at the door.",
    "This ending is a partial win, and it is recoverable: the study is open, the date is real, and the record — which you can request in writing under 55 Pa. Code § 3130.44(d) — will carry your sister's name correctly from here. Parents reach the kinship ending from here all the time. They just reach it later than the first night allowed."]),
]

# ============================================================ S48 (Foundation)
S = date(2026, 4, 6)
assert fmt(S) == "Monday, April 6, 2026"
REVIEW48 = S + timedelta(days=24)
assert fmt(REVIEW48) == "Thursday, April 30, 2026"

s48_meta = {
    "title": "The First 90 Days",
    "subtitle": "Scenario 48 — The Spare Room (a fictional composite)",
    "startDateISO": "2026-04-06",
    "startNode": "start",
    "startCash": 120,
    "tier": "Foundation",
    "summary": "You are Gwen. Your son Hugo, nine, has been in a foster home for two weeks while you finish a treatment program. Your father has a spare room, a steady pension, and a heart condition he manages like a train schedule. Between his offer and Hugo's bed in that room stands a home study — and everything a study can get wrong on paper.",
}
s48 = [
 N("start", 0, "Your father's kitchen",
   ["Your father Walter keeps a list on his refrigerator of everything his cardiologist has ever told him, in chronological order, and he follows it the way he followed a bus route for thirty-one years: exactly. He pours coffee and says the thing he has clearly rehearsed.",
    "\"The spare room is Hugo's. It was always going to be Hugo's, since before any of this. You finish your program. The boy sleeps under my roof. Tell them.\" You are two weeks into the program that is the center of your case, and Hugo is two weeks into a foster home across town with a kind family, the Delacroix family."],
   [C("\"I will, Pop. In writing — so it lands in the file, not just in a phone call.\"", "tell_in_writing", setFlags=["kinNamedWritten"], addHidden=["named-kin"]),
    C("\"I will, Pop.\" You will tell Hugo's worker, Mr. Solberg, when you see him Thursday.", "tell_thursday")]),
 N("tell_thursday", 3, "Thursday, in passing",
   ["You tell Mr. Solberg in the hallway after your visit with Hugo, while he is balancing a coffee and a laptop bag, and he says \"That's great, I'll note it\" the way people do in hallways. A week later, at your program review, you learn what the note became: one line — \"maternal grandfather may be resource.\" No address. No phone. The study clock has not started, because as far as the paperwork is concerned, there is barely a person to study.",
    "The fix is unglamorous and entirely within your power."],
   [C("Write it properly this time: a letter to the agency with his full name, address, phone, and the words \"I am asking for a kinship home study.\"", "tell_in_writing", setFlags=["kinNamedWritten"], addHidden=["named-kin"])]),
 N("tell_in_writing", 3, "The letter",
   ["However it got there, the file now holds a letter with a person's name, address, and telephone number, and a request a supervisor can route: kinship home study, maternal grandfather. Walter gets a call within days — not because the system is fast, but because a named, reachable person is the one thing every system knows how to process.",
    "The study has three parts, Mr. Solberg explains: background clearances, a home visit, and interviews. \"It's not a test he passes by being a good man,\" he says. \"It's a list. We go down the list.\""],
   [C("\"Then get him the list. All of it, up front — not one surprise at a time.\"", "the_list", setFlags=["listRequested"])]),
 N("the_list", 5, "The list",
   ["To Mr. Solberg's credit, the list arrives as one document: clearances for Walter and any adult in the home, income verification, a medical statement from his doctor, and the home itself — sleeping arrangements, safety items, medications secured. Walter reads it twice at the kitchen table with a pencil, the way he used to read route changes.",
    "\"Medicines,\" he says. \"Mine are in the bathroom cabinet. Boy could reach them on a chair.\" He says it before any worker does. That will matter more than he knows."],
   [C("Help him start on the fixable things this weekend — the list is a ladder if you climb it before the visit, and a verdict if you read it after.", "fix_weekend")]),
 N("fix_weekend", 6, "Saturday work",
   ["The weekend becomes a project with a nine-year-old's name on it. A lockbox for the medications, screwed to the closet shelf. A handrail for the basement stairs, which Walter has been meaning to fix since 2019 and now fixes in an afternoon with his neighbor's drill. Hugo's room gets the bed from the attic, clean sheets, and the shelf of model buses moved down to eye level.",
    "None of it is expensive. All of it is the difference between a study that reports problems and a study that reports solutions."],
   [C("Spend $25 at the hardware store and keep the receipt in the study folder.", "clearances", cash=-25, setFlags=["homeFixed"]),
    C("Do the work with what is in the garage — lockbox from your brother, rail repaired not replaced.", "clearances", cash=-8, setFlags=["homeFixed"])]),
 N("clearances", 9, "Paper that travels slowly",
   ["Walter's clearances go in with his fingerprints on a Tuesday. His doctor's statement takes longer — the cardiologist's office faxes it to the wrong number once, because medical offices are where faxes go to be reborn as mysteries. You learn the study's least dramatic rule: nothing is submitted until somebody confirms it arrived.",
    "You call the agency twice that week. The second call finds the fax. Persistence is not a personality trait in this system; it is a tracking method."],
   [C("Ask Mr. Solberg for a checklist of what is still missing, in writing, so the study has a finish line you can see.", "checklist", setFlags=["checklistKept"])]),
 N("checklist", 12, "The finish line",
   ["The written checklist says: clearances — received. Medical statement — received. Home visit — scheduled. One interview — Walter's, and one with you. Your program counselor will send attendance verification directly. For the first time since Hugo left your apartment, a piece of this case has an end you can point at.",
    "The home visit is set for next week. Walter asks if he should bake. You tell him caseworkers have seen everything and pie is not on the list. He bakes anyway."],
   [C("Be there for the visit if the agency allows — a daughter who shows up is data too.", "home_visit")]),
 N("home_visit", 16, "The walk-through",
   ["Mr. Solberg walks the house with his list, and the house answers him: medications locked, handrail solid, Hugo's bed made, smoke detectors beeping their small green assent. He opens the bathroom cabinet out of professional habit and finds toothpaste and a man who planned ahead. \"Your father fixed these before I flagged them,\" he says, and writes for a while.",
    "What a home study records is not a house. It is whether the adults around a problem move toward it or wait to be told."],
   [C("Walk him out. Ask the only question that matters: \"What happens at the review on April 30th?\"", "before_review")]),
 N("before_review", 20, "Before the review",
   ["What happens depends on the study being finished — reports written, approvals signed — and on the recommendation the agency carries into the courtroom. Yours is assembling well. One piece remains that is yours alone: a short written statement to the court supporting the placement, so the judge hears your voice asking for your father's home, not just the agency's voice reporting it.",
    "Parents are parties in their children's cases. Parties may be heard. The smallest version of that right is a page with your name on it, filed before the hearing instead of wished for after it."],
   [C("Write it: one page — the program, the plan, your father, and what Hugo asks for when he calls you (his room at Pop's).", "the_review", setFlags=["motherStatement"]),
    C("You will speak at the review instead. Writing feels like homework from a system that already took your son.", "the_review")]),
 N("the_review", 24, "The review",
   ["The courtroom version of your father's spare room is a two-page report: clearances clear, medical managed, home safe, fixes made before they were findings. Mr. Solberg presents it. Mrs. Delacroix, Hugo's foster mother, tells the judge Hugo talks about his grandfather's model buses \"like church.\"",
    "The judge reads the report's last page, where the recommendation lives."],
   [C("Wait for the sentence the whole spring has been walking toward.", "outcome")]),
 N("outcome", 24, "The recommendation",
   ["What the judge can order depends on what the study can support — a finished study with an approval, or an unfinished one with a promise."],
   [C("The study is complete and approved — clearances, medical, home, your statement — and the agency recommends the move.", "end_move", requiresFlags=["homeFixed", "checklistKept", "motherStatement"]),
    C("The study is nearly there, but a piece of paper is still traveling.", "end_study")]),
 E("end_move", 24, "Ending — The Spare Room, Occupied",
   ["The court orders Hugo placed with his grandfather, effective this weekend, with your program schedule written into the order so visits and overnights build toward home. Walter, who dressed for court in his route-supervisor tie, accepts the judge's thanks with the nod of a man who has been handed a route he intends to run on time. Hugo's bed — the one from the attic, with the model buses at eye level — gets its boy.",
    "Nothing in this scenario required money, connections, or a brilliant legal move. It required the kinship basics, in order: the relative named in writing with a way to reach him; the study treated as a list to climb before the visit instead of a verdict to fear after it; every slow-moving paper tracked until somebody confirmed it arrived; and your own voice in the file asking for it. Courts can only approve the homes that paper makes visible. Walter was ready in March. The study's job — and yours — was making the file able to see it.",
    "What no strategy controls: the clearances and the judge. A clearance can surface something a family did not know it had to answer, and no letter fixes that overnight. This story's grandfather had a clean record and a managed heart. Another family's story has more chapters. The sequence still matters: it is how those chapters get found early, answered in writing, and weighed as facts — instead of arriving as surprises at the hearing."]),
 E("end_study", 38, "Ending — Approved in Principle (partial)",
   ["The judge praises the study's progress, approves your father as a placement resource in principle, and sets the move for the next review — fourteen days out — when the last verification is filed. Hugo spends two more weeks with the Delacroix family, who send him to Walter's for Sunday dinner in the meantime with the court's blessing. It is a good outcome wearing a waiting room's clothes.",
    "The lesson is about paper travel time. Somewhere between the cardiologist's fax, the clearance office, and the report writer's desk, this case kept losing days it could not see — and the only instrument that finds lost days is a checklist, requested in writing, checked by a person who calls twice. Ask for the study's finish line early: what is missing, who holds it, and what date it is due. A study with a visible finish line finishes. A study without one becomes weather — everybody discusses it, nobody can schedule around it.",
    "This ending is a partial win, and a common one: the placement is approved, the boy is loved in both houses, and the only cost was time. Name the cost anyway. In a child's calendar, two weeks is not a rounding error — and the next family over, the one that tracks its paper from day one, is the reason this scenario exists."]),
]

# ============================================================ S49 (Hard)
S = date(2026, 2, 16)
assert fmt(S) == "Monday, February 16, 2026"
REVIEW49 = S + timedelta(days=31)
assert fmt(REVIEW49) == "Thursday, March 19, 2026"

s49_meta = {
    "title": "The First 90 Days",
    "subtitle": "Scenario 49 — Two Houses (a fictional composite)",
    "startDateISO": "2026-02-16",
    "startNode": "start",
    "startCash": 190,
    "tier": "Hard",
    "summary": "You are Deshawn. A furnace fire took your apartment, not your children — but the shelter system took them anyway, into two different foster homes, because no single home that night had two beds. Your great-aunt Odette has a house, two spare rooms, and one complication: a grandson who stays some weekends, about whom everything must be written down exactly right.",
}
s49 = [
 N("start", 0, "The night of the fire",
   ["The furnace fire did not hurt anybody, and it took everything anyway: the apartment is red-tagged, your shifts at the warehouse come with a cot at your cousin's for you, and Kira (ten) and Micah (six) are, as of tonight, in two different foster homes across the county from each other — because the emergency list had no house with two open beds, and a sibling set of two is, to a placement desk at midnight, a math problem.",
    "The caseworker, Ms. Moreau, is apologetic in the practiced way of someone delivering weather. \"It's temporary. We'll work on getting them together.\" Temporary is a word whose meaning depends entirely on who is keeping the calendar."],
   [C("Ask — tonight, before she leaves — \"Who keeps the calendar on 'together,' and when is it reviewed?\" Get the hearing date and write it on the shelter's discharge paper.", "the_date", addHidden=["placement-split"])]),
 N("the_date", 0, "The date",
   ["The shelter care hearing is Thursday — emergency placements get reviewed within 72 hours by law (42 Pa.C.S. § 6332). Cohesion is not on that hearing's short agenda; custody is. But Ms. Moreau, pinned gently to specifics, gives you two useful things: the names of both foster homes' neighborhoods, and confirmation that the children can see each other — visits between siblings are arranged, not automatic, and arranging starts with asking.",
    "On the bus back to your cousin's couch, you make the call that this whole scenario will turn on. Your great-aunt Odette — your grandmother's sister, sixty-three, retired from the school cafeteria, in the brick house on Walnut with the porch — has two spare rooms and has been asking about the children since midnight."],
   [C("Call her now, from the bus, and ask the question whole: \"Aunt Odette — both of them. Your house. Would you?\"", "aunt_call")]),
 N("aunt_call", 1, "Odette",
   ["She answers like the phone insulted her by ringing so late with so obvious a question. \"Boy, I changed your diapers in that house. Get me whatever papers they need. Both rooms. Kira gets the blue one — she'll say it's hers anyway.\" Then, practical as a tide table: \"My grandson Tomas stays some weekends when his shift runs late. He's twenty-four. Sleeps on the third floor. That's part of the house too. Put it in whatever they ask.\"",
    "A household is everyone who sleeps under the roof — on the form, in the study, and in the truth. Odette has just handed you the fact that will make or break her application, depending on what you do with it."],
   [C("Put Odette's offer in writing to the agency tomorrow — full name, address, phone, both children named, and Tomas's weekend stays stated in the letter itself.", "letter_full", setFlags=["kinNamedWritten", "householdHonest"], addHidden=["named-kin"]),
    C("Put Odette's offer in writing tomorrow — name, address, phone, both children. Tomas is a grown man with his own apartment; weekends hardly count as living there. Leave him out of it.", "letter_short", setFlags=["kinNamedWritten"])]),
 N("letter_short", 2, "The shorter letter",
   ["The letter goes in clean and simple, and that is exactly its problem. Somewhere in a database the agency can search — because agencies search households, not just people — Tomas's name is attached to that address from an old matter in another county. It may be nothing. It may be a dismissed charge from when he was nineteen. But the study will find it, and when it does, the question will not be about Tomas. It will be about the letter that didn't mention him.",
    "You hear about the match from Ms. Moreau, carefully, a week later — and spend the rest of the study climbing out of a hole labeled 'omission.'"],
   [C("Correct it in writing, immediately and completely: Tomas's full name, his own address, his weekend pattern, and an apology for the gap — then help Odette get his clearances started anyway.", "the_study", setFlags=["omissionCorrected"], cash=-10)]),
 N("letter_full", 2, "The whole letter",
   ["Your letter names everybody who sleeps in that house, including the one who sleeps there eight nights a month. Ms. Moreau reads it and does something that tells you the letter worked: she starts asking you questions about Tomas as logistics, not as secrets. \"He'll need clearances too, as a household member for study purposes. Can he get fingerprinted this week?\"",
    "A disclosed complication is a task. An undisclosed one is a finding."],
   [C("Call Tomas yourself. \"Aunt Odette's taking the kids. The county needs your prints. It's not about you — it's the shape of the house.\"", "the_study")]),
 N("the_study", 4, "The study",
   ["Odette's study opens with her clearances, Tomas's fingerprints, and a home visit that she treats like a church inspection: the blue room gets a second bed before the worker arrives, not after. Ms. Moreau walks the third floor, notes the separate bathroom, asks Tomas his schedule directly, and writes it all down in front of him — which is what honest paper looks like.",
    "Then the pace changes. Studies move at the speed of their slowest document, and Odette's slowest document is her late husband's death certificate, needed to clear an old joint account flag on a background report. Nobody thinks it means anything. It still has to arrive."],
   [C("Get the certificate yourself — county office, same week, fee paid — and hand-deliver a copy to the agency with a receipt.", "certificate", cash=-18, setFlags=["paperChased"]),
    C("Let the agency request it through channels. It is their study; the flag is their paperwork.", "certificate_slow")]),
 N("certificate_slow", 9, "Through channels",
   ["Channels take nineteen days. In those nineteen days, Kira has a birthday in one foster home and Micah loses a tooth in the other, and you spend both events in a family visitation room with party hats from a dollar store, doing arithmetic about what 'temporary' costs when other people hold the calendar.",
    "When the certificate lands, the study resumes exactly where it stopped. Nothing was denied. Nothing was decided. That is the most common way sibling placements stay split: not by ruling, but by drift."],
   [C("From here in, nothing travels without you carrying a copy. Ask for the sibling visits in writing while you wait.", "sibling_visits", setFlags=["visitsWritten"])]),
 N("certificate", 9, "Paper, chased",
   ["The certificate arrives inside the week. The flag clears. And because you are at the agency anyway, you do the second thing this scenario is about: you put the sibling visits in writing. Kira and Micah have seen each other twice in three weeks, both times because a foster parent volunteered a drive. That is kindness. Kindness is not a schedule.",
    "\"I'm asking that sibling visits be written into the plan — weekly, arranged by the agency, until they're placed together.\" Ms. Moreau types it where requests go to become obligations."],
   [C("Weekly sibling visits, in the plan, in writing — starting this Saturday.", "sibling_visits", setFlags=["visitsWritten"])]),
 N("sibling_visits", 13, "Saturdays",
   ["The visits change the children's weather. Micah's foster mother reports he sleeps better on Saturday nights; Kira keeps a countdown on a paper chain. The file now documents something agencies are supposed to weigh and often only notice when it's written down: these two are not a caseload of two. They are a set.",
    "Odette's study, meanwhile, has one more room in it: the interview where she is asked, as every kinship applicant is asked now, about Tomas — when he stays, where he sleeps, what the children call him. There is only one way to answer it that helps her."],
   [C("\"Everything in my letter is everything there is. Tomas stays two weekends a month, third floor, and here's his number — ask him.\"", "tomas_check", setFlags=["householdHonest"])]),
 N("tomas_check", 18, "The check",
   ["Tomas's record is what Odette said it would be: a single charge at nineteen, dismissed, in a county two hours away. The dismissed charge is a fact. What the study writes about it is a judgment — and the judgment it writes, when the household was disclosed from the first letter, is 'household composition known; adult member's history reviewed; no current concern.'",
    "Had it surfaced as a discovery, the same facts would have been written as a credibility problem for the applicant. Same Tomas. Different letter."],
   [C("Ask Ms. Moreau what remains before the March review — and get the answer as a list.", "the_list2", setFlags=["checklistKept"])]),
 N("the_list2", 22, "What remains",
   ["The list is short: the study report to be written, Odette's approval signature from a supervisor, and the hearing itself. It is also the moment to make sure the review hears the person the law added to the room. Since 2023, a potential kinship care resource — someone who meets the emergency-caregiver requirements and has said yes to being a kinship caregiver — has a statutory right to be heard at a hearing on one subject: her qualifications to provide kinship care (42 Pa.C.S. § 6336.1, as amended by Act 48 of 2023; the definition sits at 42 Pa.C.S. § 6302).",
    "It is not standing, and Ms. Fontaine, your appointed counsel — yours by right under 42 Pa.C.S. § 6337 — is careful about the difference. \"She can't argue your case. But on whether she can take them, the court must hear her, and must then decide whether she gets notice and a voice going forward. Make sure she's there.\""],
   [C("Odette will be there, in her good coat, with her folder. Ask Ms. Fontaine to note her presence for the record at the start.", "records49", setFlags=["auntHeard"])]),
 N("records49", 26, "The record, both ways",
   ["Before the review, Ms. Fontaine suggests the request she suggests in every case: the agency's file, in writing — a parent's right under 55 Pa. Code § 3130.44(d). The placement summaries confirm the split was a bed-count accident, not a clinical judgment: both foster homes rate the children thriving; both note the sibling countdown chains.",
    "Paper that agrees with you is still worth having. Judges trust documents that were written before anybody knew they'd be exhibits."],
   [C("File the request. Bring the summaries to the review.", "the_review49", setFlags=["recordsRequested"], addHidden=["record-request"])]),
 N("the_review49", 31, "March 19th",
   ["The judge has the study, the sibling-visit log, and a great-aunt in the second row. Ms. Moreau presents the agency's position; Ms. Fontaine presents yours; and when the question of the kinship home arrives, Odette is heard — on her qualifications, which turn out to be a life story with a spare room attached.",
    "\"Ms. Moreau,\" the judge says, \"the agency's recommendation on placement with the great-aunt?\""],
   [C("Hold still. The answer was assembled in February, one letter at a time.", "outcome49")]),
 N("outcome49", 31, "One roof, or two",
   ["The recommendation depends on what the study could honestly say about the whole household — and on how much of the month the paper spent traveling instead of arriving."],
   [C("The household was disclosed from the first letter, the certificate chased, the visits documented, and Odette has been heard on her qualifications: the agency recommends both children to her home.", "end_oneroof", requiresFlags=["householdHonest", "paperChased", "auntHeard"]),
    C("The study supports Kira — school-age, blue room ready — but the agency wants 'more time' on the household picture before Micah, the younger child, moves too.", "end_splitfix"),
    C("The file is too thin to recommend a joint move today.", "end_visits")]),
 E("end_oneroof", 31, "Ending — One Roof",
   ["Kira and Micah move to Walnut Street on Saturday, into the blue room and the room beside it, with Tomas's third-floor weekends written into the safety plan like the ordinary fact they always were. The judge, granting Odette notice and participation going forward, says the quiet part into the record: the kinship resource was ready before the system was, and the file shows it.",
    "Three things carried this outcome. The kinship offer was made in writing on day one, with the whole household in it — a disclosed complication is a task, an undisclosed one is a credibility finding. The sibling bond was made into paper: weekly visits, requested in writing, logged, and impossible to un-know by March. And Odette used the voice current law gives her: under 42 Pa.C.S. § 6336.1 (Act 48 of 2023), a potential kinship care resource (§ 6302) must be heard on her qualifications to provide kinship care, and the court must then decide her notice and participation going forward. She still has no standing in your case — the statute is explicit — but her qualifications are now a courtroom fact instead of a file hope.",
    "What no strategy controls: the hearing judge's view of a six-year-old and a dismissed charge at nineteen, and Tomas himself. If his record had held more, this ending narrows. The strategy's job was never to guarantee Odette's house wins — it was to make sure it was judged on its actual contents, all of them, from the first letter forward."]),
 E("end_splitfix", 45, "Ending — One Roof, One Still Away (partial)",
   ["Kira moves to Walnut Street. Micah does not — not yet: the court keeps him in his foster home 'pending household stabilization' and sets the question again in six weeks, with Odette approved as his respite and weekend home in the meantime. It is half a family under one roof and half a countdown chain, and Micah's half is the heavier half to carry out of the courtroom.",
    "Be honest about what produced the split: not Tomas, and not his record — the delay. Paper that travels by channel instead of by hand cost the study the weeks in which a supervisor's caution might have been answered twice over. Every reviewer of a young child's placement is choosing between two risks, and an unfinished file makes 'wait' the defensible choice. Finished files are how parents take 'wait' off the table.",
    "This is a partial win with a working engine: Odette is approved, heard, and in the case with notice going forward (§ 6336.1). The six-week review is a date, not a hope. Keep the Saturday visits in writing, keep the countdown chains in the file, and let the next hearing decide about a household that has been running, visibly and without incident, for a month and a half."]),
 E("end_visits", 45, "Ending — Sundays Together (partial)",
   ["The children stay where they are, in two houses, and the court's order does the one solid thing this file could support today: sibling visits every Saturday, agency-arranged, written into the plan where they cannot quietly evaporate — and Odette's study kept open with a review date, her right to be heard on her qualifications acknowledged on the record.",
    "It is not the ending this family aimed at, and the debrief owes you the unvarnished reason: the joint placement failed on file depth. A study slowed by undisclosed household facts and slow paper presented the judge a choice between two thriving foster placements and an unfinished kinship file — and unfinished files lose that comparison even when the home behind them is the right one. The bond evidence (the visits, the countdowns) did its work: it is why the visits are ordered and the study kept open rather than closed.",
    "Treat this ending as a waypoint, not a verdict. The study continues; the next review inherits a complete household picture, a documented sibling bond, and a kinship resource the court has already heard once. Families reach One Roof from exactly here. The road is just measured in reviews instead of weeks."]),
]

# ============================================================ S50 (Hard)
S = date(2026, 5, 4)
assert fmt(S) == "Monday, May 4, 2026"
REVIEW50 = S + timedelta(days=17)
assert fmt(REVIEW50) == "Thursday, May 21, 2026"

s50_meta = {
    "title": "The First 90 Days",
    "subtitle": "Scenario 50 — The Move Nobody Announced (a fictional composite)",
    "startDateISO": "2026-05-04",
    "startNode": "start",
    "startCash": 165,
    "tier": "Hard",
    "summary": "You are Talia. Your son Ruben, eleven, has lived for six months with a foster mother he calls Tía, in his own school district, three bus stops from your apartment. Tonight at visitation he tells you he is moving — new home, new school, new county. You are hearing it from an eleven-year-old. The agency has not told you at all.",
}
s50 = [
 N("start", 0, "What Ruben said",
   ["\"Tía—\" he stops himself; her name is Mrs. Renaud, whatever six months of dinners have renamed her in his head — \"Mrs. Renaud's husband got the job in Pittsburgh. She cried. She said I move before school ends. A new house. She said the agency would tell you.\" The visitation room has a clock, a box of crayons with the good colors gone, and your son doing the arithmetic of another goodbye out loud.",
    "The agency has not told you. The foster mother learned last week; Ruben learned today; the person with legal standing to object — you, his mother, a party to his case — is learning it from an eleven-year-old over a board game. Placement moves are where parents discover what their file says they were told."],
   [C("Before the visit ends, ask Ruben three things and write down his exact words: when did she tell him, what did she say the reason was, and what did he say back.", "exact_words", addHidden=["move-notice"])]),
 N("exact_words", 0, "His exact words",
   ["He told her: \"Can I finish the school year?\" She said she asked, and the answer was the calendar — her husband starts in June, the house closes in June, and the agency wants Ruben 'settled before summer.' Ruben has been settled. He has a desk with his name taped to it, a reading level that finally moved, and a best friend two doors from Mrs. Renaud's whose mother lets them build blanket forts on Saturdays.",
    "Six months is not a visit. It is a childhood address. You write his sentence down word for word, because children are believed in proportion to how exactly adults quote them."],
   [C("Call your lawyer, Ms. Marchetti, tonight — not Monday. Moves run on agency calendars, and objections run on court ones.", "call_lawyer50")]),
 N("call_lawyer50", 1, "Two calendars",
   ["Ms. Marchetti listens the way lawyers do when the clock is the case. \"A placement change is the agency's administrative act — until it isn't,\" she says. \"What makes it a court's business is a party asking, on paper, fast. We'll file for a review and ask that the move wait for it. And we'll do the thing agencies least enjoy: ask for the file. The file will say when this decision was actually made, and by whom, and what it says you were told.\"",
    "Your rights here are not exotic. You are a party; parties get heard; and a parent may request the case record in writing under 55 Pa. Code § 3130.44(d)."],
   [C("\"File both. The review request and the record request. Tomorrow.\"", "file_both", setFlags=["reviewFiled", "recordsRequested"], addHidden=["record-request"], cash=-12)]),
 N("file_both", 2, "Filed",
   ["Both documents go in with timestamps — a fact this scenario will lean on. The review is set for May 21st. The agency's response, when it comes, is courteous and total: the move is necessary, the new home is excellent, the school is 'comparable,' and your objection is noted. Noted is what agencies write on the way to doing what they planned.",
    "Mrs. Renaud calls you that evening, apologetic in a different key. \"I told them March,\" she says. \"March 30th, I told them about Pittsburgh. They said they'd plan.\" March 30th. Ruben learned on May 4th. You were planned at, apparently, for five weeks."],
   [C("Write down her date and her words, with her permission, in the notebook you now keep for this case.", "march30", setFlags=["fosterTimeline"])]),
 N("march30", 3, "March 30th",
   ["Your notebook is becoming the second file — the one that records what the first file leaves out. Mrs. Renaud's March 30th matters because it converts the story: this was never an emergency move. It was a known move, planned for five weeks, during which nobody planned the part where a mother is told.",
    "Foster parents occupy a specific place in the law here: under 42 Pa.C.S. § 6336.1, the court directs the agency to give a foster parent timely notice of hearings, and the foster parent has the right to be heard at them. Mrs. Renaud has been Ruben's daily life for six months. If there is a hearing about where he lives next, she is entitled to stand in it — and what she says may not be what the agency expects."],
   [C("Ask her, carefully and without coaching: \"Will you come to the hearing? Will you say what you told me — in your own words?\"", "kessler_speaks")]),
 N("kessler_speaks", 5, "In her own words",
   ["\"I already told them,\" she says, \"and I'll tell the judge. He should finish his school year. And if there's family — real family, in the district — that should have been the first call, not the last.\" She pauses. \"There is your cousin, isn't there? The one at his birthday?\"",
    "Anita. Your cousin, Ruben's godmother in every way but the paperwork, two streets from his school, who has asked twice — twice, out loud, at family things — \"why not me?\" and been told the placement was stable and not to rock it. The placement is no longer stable. The rocking has been done by other hands."],
   [C("Call Anita tonight. Ask the question whole: \"The agency is moving him out of the district. Will you be studied — fast, this month — to take him?\"", "anita_call", setFlags=["kinIdentified"])]),
 N("anita_call", 6, "Anita",
   ["Anita does not finish her tea before answering. \"I have the room. I had the room in October when I asked. Tell me what papers.\" You give her Ms. Marchetti's number and the agency's, and the instruction that matters most: put it in writing herself, tomorrow, and keep a copy.",
    "Kinship that exists only as family conversation does not exist in court. By Friday, Anita must exist as a letter, a clearance application, and a name a judge can say."],
   [C("Anita files her written kinship request and clearances on Friday. You file a copy with your review papers.", "anita_files", setFlags=["kinWritten"], addHidden=["named-kin"])]),
 N("anita_files", 8, "The record arrives",
   ["Your § 3130.44(d) record request pays its rent on Tuesday: the placement file, with the move memo inside it. The memo is dated April 2nd — three days after Mrs. Renaud told them, a month before Ruben told you. It lists the new placement, the new school, and one line that Ms. Marchetti reads aloud twice in her office: \"Parent to be notified of move at next scheduled contact.\"",
    "Next scheduled contact. The memo's author scheduled your knowledge for whenever. \"This,\" your lawyer says, \"is why we request records. The summary they send you is a story. The record is the evidence.\""],
   [C("Ask what else the record holds that the summary didn't: the school-stability note, the visit logs, the therapist's letter.", "read_fully", setFlags=["recordRead"])]),
 N("read_fully", 10, "Reading fully",
   ["The record holds more than the memo. Ruben's school counselor wrote in February that his attendance and reading 'transformed' this year. His therapist's March note recommends 'minimizing transitions; patient has attached after prior instability.' The agency's own file, in other words, argues against the agency's own move — it just argues in documents nobody had assembled into one pile.",
    "Assembling the pile is the work. Courts decide on what's in front of them, and what's in front of them is what the parties carry in."],
   [C("Build the hearing packet with Ms. Marchetti: memo, school letter, therapist note, Anita's filing, Ruben's sentence about finishing the school year.", "packet50", setFlags=["packetBuilt"])]),
 N("packet50", 13, "The packet",
   ["The packet is eleven pages and it has a shape: a known move, delayed notice, a documented school transformation, a clinician's transition warning, a foster mother willing to speak, and a kinship home inside the school district with its paperwork already moving. Shape is what separates an objection from an argument.",
    "The agency's filing, by contrast, is four pages: necessity, excellence of the new home, comparability of the school, and your noted objection. It describes Ruben's next address in detail. It does not mention his current life at all."],
   [C("At the pre-hearing call, ask the question the packet was built to ask: \"Has anyone from the agency spoken to Ruben's school or his therapist about this move?\"", "the_hearing50")]),
 N("the_hearing50", 17, "May 21st",
   ["The judge works the packet in order. The agency's worker, Mr. Wexler, confirms the March 30th notice from Mrs. Renaud and the April 2nd memo. He confirms the 'next scheduled contact' line with the expression of a man reading someone else's handwriting in his own file. The school counselor's letter is read into the record. Then Mrs. Renaud is heard — her right, as the foster parent, under 42 Pa.C.S. § 6336.1 — and she says what she told you, in her own words: finish the school year; family first.",
    "Finally, Anita. As a potential kinship care resource — the category Act 48 of 2023 wrote into § 6336.1, defined at § 6302 — she may be heard on her qualifications to provide kinship care. She is: the room, the school two streets away, the clearances already filed. The judge turns to the agency."],
   [C("\"Counsel — given your own file, why is the move in this child's interest, and why is the kinship home not the answer?\" Listen.", "outcome50")]),
 N("outcome50", 17, "Where he lands",
   ["The order depends on whether the hearing was a review of a decision — or a reading of a record the decision never considered."],
   [C("The packet was complete: the memo, the clinician, the school, the foster mother's voice, and a kinship home filed and present.", "end_sameschool", requiresFlags=["packetBuilt", "fosterTimeline", "kinWritten"]),
    C("The objection was real, but the kinship piece was late or the packet thin — the move is softened, not stopped.", "end_softlanding"),
    C("The objection lived in phone calls and a visitation room. Nothing was filed; the record was never requested.", "end_busroute")]),
 E("end_sameschool", 17, "Ending — Same School, Family Address",
   ["The court stops the cross-county move and orders Ruben placed with Anita — expedited kinship approval to be completed within thirty days, Mrs. Renaud to host the transition, including Ruben's last blanket-fort Saturday. He finishes the school year at his desk, with his name still taped to it. The judge's reasoning, read into the record, is a list of your documents: the therapist's transition warning, the school's letter, the memo's notice line, and a kinship home two streets from the school that asked in October and filed in May.",
    "The doctrine in one paragraph: placement moves are administrative until a party makes them judicial — in writing, fast. The record request (55 Pa. Code § 3130.44(d)) is what turned your objection from a feeling into an exhibit: the agency's own memo proved the notice failure and the agency's own clinicians argued against the move. And two voices the law specifically seats at the table did the rest: the foster parent's right to be heard (42 Pa.C.S. § 6336.1) and, since Act 48 of 2023, the potential kinship care resource's right to be heard on her qualifications (§ 6336.1; § 6302). Neither has standing in your case. Both changed it.",
    "What no strategy controls: the receiving home's quality or the judge's temperament, and Anita herself — a kinship resource who falters in her own study ends this scenario differently no matter how good the packet is. The packet's job was narrower and decisive: it made the court compare the move against the child's actual documented life, instead of against nothing. Moves ordered against nothing are the ones that happen in May because a memo said so in April."]),
 E("end_softlanding", 24, "Ending — A Softer Landing (partial)",
   ["The move happens, but not as written. Ruben stays with Mrs. Renaud through the end of the school year — the judge adopts her transition plan as the order — and moves in July to the new home with a written transition: two overnight visits first, his therapist consulted, his school records transferred with the counselor's letter attached, and Anita approved for weekends and respite with her kinship study kept open and dated. It is a loss with engineering in it.",
    "Partial endings like this one are where most placement fights actually land, and the difference between this and the unmodified move is everything the filed paper bought: time (seven weeks of school), sequence (visits before the move, not after), and a kinship door held open by an order instead of a hope. The debrief in S4's doctrine applies verbatim: a courtroom loss with a strong record outperforms a courtroom absence with a strong grievance.",
    "Keep building from here: Anita's study completes or it doesn't, and the next review — with her approved and Ruben's transition documented — is a different hearing from this one. Placement stability is a cumulative argument. You have started the accumulation."]),
 E("end_busroute", 24, "Ending — The Bus Route Changed",
   ["Ruben moves the first week of June, as the memo always intended. The new home is, as promised, excellent. The new school is, as promised, comparable. His reading level slips over the summer — not catastrophically, just the way a plant slips when it's moved mid-season — and his new bus route passes, twice a day, three stops from your apartment, in the district where he no longer attends school.",
    "This ending exists to be read carefully, because nobody in it villainously twirled anything. The agency executed a plan it had documented since April. The foster mother cooperated and cared. The system worked exactly as it works when one party is absent from the paperwork. Your objection was real; it lived in a visitation room and a phone call, and neither of those places is where placement decisions get reviewed. The hearing that never happened is the whole lesson: parties who file get hearings, records get read, kinship resources get heard (§ 6336.1) — and parents who are only 'noted' get noted.",
    "If you are reading this debrief instead of living it: file the review request, file the record request (55 Pa. Code § 3130.44(d)), name the kin in writing, and do it in the first week — moves are perishable, and the calendar that governs them starts running before anyone tells you there is a move at all."]),
]

# ============================================================ S51 (Hard)
S = date(2026, 6, 1)
assert fmt(S) == "Monday, June 1, 2026"
REVIEW51 = S + timedelta(days=38)
assert fmt(REVIEW51) == "Thursday, July 9, 2026"

s51_meta = {
    "title": "The First 90 Days",
    "subtitle": "Scenario 51 — The Second Study (a fictional composite)",
    "startDateISO": "2026-06-01",
    "startNode": "start",
    "startCash": 210,
    "tier": "Hard",
    "summary": "You are Francine, and this time the player is the kin. Your nephew Benny, eight, is in foster care while your sister Silvia is in treatment. Your own kinship study came back denied — two reasons, both about your house. One of them is wrong. The other is a misunderstanding with a tape measure. You are not a party to Benny's case. You are about to learn what a non-party can still do.",
}
s51 = [
 N("start", 0, "The denial",
   ["The letter is two paragraphs, which is two paragraphs more than many kin ever get, and you should be grateful for them — Ms. Tomas, the worker, says so, kindly, when she calls. Paragraph one: your application to be a kinship caregiver for your nephew Benny is denied. Paragraph two gives the reasons: (1) household composition unclear — additional adults residing in the home whose clearances were not provided; (2) sleeping arrangements inadequate — the child would share a room beyond the approved configuration.",
    "You read it standing in the house the letter describes, and the house disagrees. Downstairs is your daughter Petra's apartment — separate entrance, separate lease, separate electric meter, a family of her own. Upstairs, the finished attic room — the one with Benny's name already on a box of his cousin's outgrown books — apparently did not make it into anybody's floor plan."],
   [C("Do not call in anger. Do the first disciplined thing: request, in writing, the specific findings behind each reason — which adults, which rooms, measured how.", "request_findings", addHidden=["kinship-denial"])]),
 N("request_findings", 1, "Findings, requested",
   ["Your letter is short because short letters get answered: you ask for the study's factual basis — the household members the agency counted, the rooms it counted, and the standard applied to each. You are not a party to Benny's dependency case, and nobody owes you his file. What an agency does owe an applicant is its own decision's basis, and asking for it in writing converts a phone-call denial into a documented one.",
    "Ms. Tomas responds in a week with the study summary. It is worse than the letter, and better: worse, because now you can see the errors itemized; better, for the same reason."],
   [C("Read it with a pencil. List every sentence that is factually wrong, unclear, or missing a room.", "read_summary")]),
 N("read_summary", 8, "The summary, annotated",
   ["Item by item: 'Adults in home: applicant, applicant's daughter, daughter's partner, infant.' Your daughter's family, folded into your household like a footnote — their separate lease, entrance, and meter nowhere in the document. 'Bedrooms: two.' The attic — finished, heated, with the egress window your brother-in-law installed in 2019 — counted as storage. 'Child would share with applicant's son (10).' Benny would share with no one; the plan, stated at the home visit and unheard, was the attic.",
    "Three errors, none of them malice. A study is a snapshot taken by a busy person through a doorway. Your job is not to accuse the snapshot. It is to retake it, with documents."],
   [C("Build the correction packet: Petra's lease and a utility bill in her name, photos and measurements of the attic, the egress window's receipt, and your own one-page floor plan.", "correction_packet", cash=-15, setFlags=["packetBuilt"])]),
 N("correction_packet", 12, "Documents, not arguments",
   ["Notice what the packet does not contain: no adjectives, no accusations, no paragraph about what Benny means to you. Adjectives are for the hearing. This packet is a measuring tape in paper form — every claim has a document stapled to it, and every document has a date.",
    "One document is beyond your reach, and the reaching matters: the home-visit notes themselves sit in Benny's case record, which belongs to the case — and to the parties. You are family. You are not a party. There is exactly one person whose signature opens that file for this purpose, and she is working very hard in a treatment program three counties away."],
   [C("Call Silvia. Not for permission to fight — for her signature on a records request, as Benny's mother and a party, so the record can correct your study.", "call_lucia")]),
 N("call_lucia", 14, "Silvia",
   ["Treatment calls are fifteen minutes and monitored by a clock neither of you controls. Silvia cries for the first two, then does the hardest thing recovery asks of her this month: she trusts the plan. \"You're not taking him from me,\" she says. \"You're holding him until I can. Sign what? Tell me exactly where.\"",
    "As a party, Silvia may request the case record in writing — 55 Pa. Code § 3130.44(d). Her signed request goes in with your correction packet, and what it is aimed at is narrow: the visit notes and household summary underlying your study's facts."],
   [C("Silvia signs. The request is mailed, certified, with your packet following as a separate submission — two envelopes, one argument.", "two_envelopes", setFlags=["recordsRequested"], addHidden=["record-request"], cash=-9)]),
 N("two_envelopes", 17, "What the notes say",
   ["The visit notes, when they come, are the scenario's fulcrum. The visiting worker's own handwriting, from the day: 'Dtr + family downstairs — separate unit?' with the question mark intact, and 'attic — finished, see photos' — photos that never made it into the summary. The summary's author worked from a different visit's template and never saw the question mark.",
    "You now hold something stronger than your opinion that the study is wrong: the study's own source documents disagreeing with it. That is the only kind of correction agencies reliably accept — their own record, quoted back."],
   [C("Write the reconsideration request: each finding, the note or document that contradicts it, and the remedy asked — a re-study visit to the actual house.", "reconsideration", setFlags=["reconsiderFiled"])]),
 N("reconsideration", 21, "Reconsideration, requested",
   ["Pennsylvania's kinship approval process runs through agencies and their internal reviews; there is no courtroom appeal of a study the way there is of an indicated report, and this guide will not invent one for you. What exists — and what families underuse — is the documented reconsideration: a written request that the agency revisit its findings on a corrected record, with the correction attached. Agencies reverse themselves on paper far more readily than on pride, if the paper makes reversal the defensible move.",
    "Yours makes it defensible: their own notes, a lease, a meter bill, an egress receipt, and a floor plan. Ms. Tomas calls within the week. Her tone has changed in the way tones change when a file gets heavier than a decision."],
   [C("\"We'll schedule a re-study visit,\" she says. \"And Ms. — Francine. The attic. Was it finished when we visited, or finished since?\" Answer carefully: the truth, with its receipt.", "tricky_question")]),
 N("tricky_question", 24, "The attic question",
   ["This is the question the whole packet exists to survive. If the attic was finished after the denial, your packet is a renovation story — real, but it moves the approval date and invites the argument that you gamed the timeline. If it was finished before — finished in 2019, receipted, photographed in the visit notes — then the denial rested on a fact that was never true, and the re-study is a correction, not a favor.",
    "Everything you have is dated. Dates are why you kept the receipt."],
   [C("\"Finished in 2019. The egress receipt is in the packet, page six, and your own visit notes say 'attic — finished, see photos.' I'm asking the re-study to look at the house that was here in June.\"", "restudy_set", setFlags=["recordCorrected"])]),
 N("restudy_set", 27, "The re-study",
   ["The re-study visit is conducted by a second worker with the full packet in her bag — the system auditing itself, which happens more often than cynics say and less often than it should. She measures the attic. She photographs Petra's separate entrance and meter. She interviews Petra's family as the separate household they are, clearances offered and accepted for the file.",
    "Her summary, when it comes, contains a sentence worth framing: 'Prior findings regarding household composition and sleeping arrangements are not sustained on re-inspection.'"],
   [C("Ask, in writing, what remains between 'not sustained' and an approval — and whether the July review can hear you on your qualifications in the meantime.", "july_review", setFlags=["restudyDone"])]),
 N("july_review", 38, "July 9th — the review",
   ["You are in the courtroom because the law puts you there. Under 42 Pa.C.S. § 6336.1 — amended by Act 48 of 2023 — a potential kinship care resource (defined at 42 Pa.C.S. § 6302: someone who meets the emergency-caregiver requirements and has expressed willingness to be a kinship caregiver) has the right to be heard at a hearing on her qualifications to provide kinship care, and the court must then decide whether she may receive notice and participate going forward. It is not standing. You cannot argue Silvia's case. But on the question 'can this woman take this child,' your voice is a statutory right, not a courtesy.",
    "Silvia's counsel presents the re-study. Ms. Tomas presents the agency's position — which, as of this morning, is one of two things."],
   [C("Hear it.", "outcome51")]),
 N("outcome51", 38, "The agency's position",
   ["Agencies bring to reviews the file they have — corrected, or uncorrected."],
   [C("The correction packet, the record, and the re-study are all in: the agency withdraws the denial, approves Francine, and joins the placement request.", "end_secondlook", requiresFlags=["packetBuilt", "reconsiderFiled", "recordCorrected"]),
    C("The re-study sustained your facts, but the approval signature is still pending — the court hears you on qualifications and acts anyway.", "end_heardplaced"),
    C("The denial stands on the original study, uncorrected and unrevisited.", "end_longway")]),
 E("end_secondlook", 38, "Ending — Approved on the Second Look",
   ["The denial is withdrawn, the approval signed, and Benny is placed with you at the review — into the attic room that was finished in 2019 and invisible until paper made it visible. Silvia, on the phone that evening from the program, cries again, differently. You put Benny's name on the box of books with a marker, which settles the question of whose room it is.",
    "The method, because it is the whole lesson: a kinship denial is a document, and documents can be corrected. Request the findings in writing. Annotate them against proof — leases, meters, receipts, measurements. Use the party's record right (55 Pa. Code § 3130.44(d), here Silvia's) to reach the source notes beneath the summary; a summary contradicted by its own notes is the strongest reconsideration there is. And know the honest shape of the remedy: reconsideration on a corrected record, not a courtroom appeal of the study — plus, at the review, your statutory right as a potential kinship care resource to be heard on your qualifications (42 Pa.C.S. § 6336.1; § 6302).",
    "A note on timing and truth: a bill pending in Harrisburg — Senate Bill 1499, introduced and in committee, not law — proposes a dedicated kinship licensing track with documented denial reasons and individualized assessment. It changes nothing you did here. Current law, used in sequence, was enough. What no strategy controls: the second worker's honesty and your sister's recovery. The re-study could have been a rubber stamp; Silvia could have relapsed in June and changed every question the court asks. You controlled the record. In kinship work, the record is most of the game — but it is not all of it, and the rest is family."]),
 E("end_heardplaced", 45, "Ending — Heard, and Placed by the Court (partial)",
   ["The approval signature is still traveling through the agency, but the court does not wait for it: having heard you on your qualifications (§ 6336.1), with the re-study's findings undisputed on the record, the judge orders Benny placed with you now, the agency's approval paperwork to be completed within fourteen days under the court's eye. He sleeps in the attic room Friday. The paper catches up the following week, slightly out of breath.",
    "This is a partial win only in form. In substance Benny is home with kin — but the distinction matters, and this guide preserves it: the placement rests on the court's order, not the agency's approval, and until the approval issues, your status is court's-kin rather than agency-approved, which can matter for payments and for how the next worker reads the file. Chase the signature. Courts order; agencies administer; the document that pays and protects is the approval.",
    "The route here ran on the same rails as the full win — findings requested, errors documented, the party's record right used, reconsideration filed — and stopped one signature short. If your family's story pauses at this station, the work is not wasted; it is the platform the final approval stands on."]),
 E("end_longway", 45, "Ending — The Long Way Around",
   ["The denial stands. The judge, without a corrected record or a re-study in front of her, has only the original study to weigh — and the original study says the house fails. You are approved instead for what the system offers denied kin: visits at your home, overnights evaluated later, a place in Benny's life that is real and not enough. Silvia's counsel notes the denial for the record. The next review is in ninety days.",
    "Read this ending for its mechanics, not its mood: the denial survived because it was never made expensive to keep. Findings unrequested stay vague; vague findings cannot be contradicted; uncontradicted findings become the house's official shape. Every step in the other endings — the findings letter, the lease and meter bill, the party-signed record request (§ 3130.44(d)), the dated receipts — exists to make the true house more documented than the mistaken one.",
    "The long way around is still a way: ninety days is enough to build the entire packet from a standing start, and a reconsideration filed before the next review forces the agency to answer documents instead of impressions. Many kinship approvals in Pennsylvania are second studies. Almost none are unrequested ones."]),
]

# ============================================================ S52 (Hard)
S = date(2026, 8, 3)
assert fmt(S) == "Monday, August 3, 2026"
NOTICE_END52 = S + timedelta(days=30)
assert fmt(NOTICE_END52) == "Wednesday, September 2, 2026"
REVIEW52 = S + timedelta(days=24)
assert fmt(REVIEW52) == "Thursday, August 27, 2026"

s52_meta = {
    "title": "The First 90 Days",
    "subtitle": "Scenario 52 — The Notice on the Fridge (a fictional composite)",
    "startDateISO": "2026-08-03",
    "startNode": "start",
    "startCash": 175,
    "tier": "Hard",
    "summary": "You are Noelle. Your daughter Sanaa, thirteen, has lived eight months with the Kellermans, a foster family who are good at teenagers. Tonight they tape their thirty-day notice to their own fridge: a parent's illness, a house to sell, an ending they hate. The agency's plan for a thirteen-year-old on a deadline is the plan agencies keep for teenagers nobody claims: a group placement. Sanaa's uncle Hakim would claim her in a heartbeat. The file says he was 'contacted.' He says his phone never rang.",
}
s52 = [
 N("start", 0, "Two phone calls",
   ["The first call is from Mrs. Kellerman, and she is crying in the controlled way of a woman reading from a paper she wrote so she would say it right: her mother's care, a move to Ohio, the house — and the formal thirty-day notice the agency requires, given today, August 3rd. Sanaa's placement with them ends September 2nd. \"We asked them to tell you first. They said the plan would be shared when there's a plan.\"",
    "The second call is yours, to the agency, and Ms. Nowak is honest in the way that should worry you more than evasion would: \"For a thirteen-year-old, on thirty days, our realistic option is the group placement on Route 30. Family homes don't take teens on short notice. We'll list her and see.\" Listed. Like a house. Like the Kellermans'."],
   [C("Write down the two dates before anything else: notice given August 3rd; placement ends September 2nd. Then ask the question the system hopes you'll ask later: \"What kin has been contacted for Sanaa — by name?\"", "by_name", addHidden=["move-notice"])]),
 N("by_name", 1, "By name",
   ["The answer comes by email the next day, because you asked for it in writing: family finding for Sanaa consists of one entry, dated March: 'Paternal uncle (Hakim B.) — left voicemail, no response.' One voicemail, to a number with a transposed digit — you can see it from your chair, because you have been texting Hakim at the right number for a decade. Family finding did not fail. It dialed wrong once, in March, and stopped.",
    "Sanaa, thirteen and done being managed, supplies the verdict at your next visit: \"Uncle Hakim has the same number since I was six. He makes the rice the right way. Why does the paper say he doesn't answer?\""],
   [C("Ask Sanaa to write it — her uncle's correct number, in her own handwriting, on the visit sign-in sheet where it enters the record.", "her_handwriting", setFlags=["correctNumber"])]),
 N("her_handwriting", 2, "Her handwriting",
   ["Teenagers' knowledge is the most underused database in child welfare: they hold the family's real phone tree, the real addresses, the real names people go by. The sign-in sheet now holds the number in Sanaa's hand. What it does not do by itself is travel — paper in a visit file waits; paper filed with the court and the agency moves.",
    "Ms. Nowak, to her credit, does not defend the March entry when you send her the correction. \"Then we call him today,\" she says. \"You'll want it in writing that we did.\""],
   [C("In writing: your letter names Hakim fully — address, phone, his relationship, his willingness — and asks for an expedited kinship study, with the September 2nd date stated in the letter's first line.", "the_letter52", setFlags=["kinWritten"], addHidden=["named-kin"], cash=-6)]),
 N("the_letter52", 3, "Hakim",
   ["Hakim answers on the first ring, because that is what his phone does when it is dialed correctly. He is thirty-eight, a school bus driver with a spare room, a daughter at college whose room Sanaa already calls 'the room,' and a record consisting of one parking ticket. He listens to the whole story — the notice, the date, the group placement — in a silence with a shape.",
    "\"September 2nd,\" he says. \"Then I have thirty days to become a paperwork uncle. Tell me every form. I will do them in order.\""],
   [C("Give him the list as the agency gives it: clearances, fingerprints, home visit, references — and the family's part: you and Sanaa document what he is to her. Godfather at her christening. Every Eid dinner. The rice.", "hakim_list")]),
 N("hakim_list", 5, "Expedited",
   ["Expedited is a word agencies use for studies done at the speed of a deadline instead of the speed of a queue, and Hakim's study earns it: clearances filed within the week, fingerprints done on his lunch break, a home visit where the worker photographs the room, the desk, and — noted in the margin, because workers are human — the rice cooker, plugged in and warm.",
    "The Kellermans, meanwhile, are doing the thing good foster parents do at the end: telling the truth early. Their notice was honest; their worry now is the cliff — Sanaa packed on September 2nd whether or not the next door is open."],
   [C("Ask Mrs. Kellerman the question that protects Sanaa most: \"If Hakim's approval lands after the 2nd — days after — would you keep her those extra days, if the court asked?\"", "kellerman_ask")]),
 N("kellerman_ask", 9, "Days after",
   ["\"If the court asks and the agency pays the days, yes,\" she says. \"A week. Maybe two. We close on the house the 21st — I can't lie to you past that.\" She will say it in the courtroom too: foster parents receive notice of hearings and may be heard at them (42 Pa.C.S. § 6336.1), and what she has to say is not opposition — it is a bridge, offered with an honest far shore.",
    "The review is August 27th — six days before the notice runs out. Everything in this scenario is now a race between a study's last signature and a calendar."],
   [C("File the record request too — Sanaa's file, your right as a party under 55 Pa. Code § 3130.44(d) — so the family-finding entry and its wrong digit are exhibits, not anecdotes.", "records52", setFlags=["recordsRequested"], addHidden=["record-request"], cash=-8)]),
 N("records52", 12, "The wrong digit",
   ["The file, when it arrives, contains the March entry exactly as described, and the intake form from Sanaa's first week — on which you, exhausted and half-conscious in a hospital chair, wrote Hakim's number correctly. The agency had the right number in its own file for eight months. The voicemail went to a stranger, who presumably still wonders about it.",
    "You do not need to prove anyone lazy or cruel. You need the court to see a sequence: correct number on file, wrong number dialed once, no second attempt, 'no response' recorded — and a group placement proposed at the end of it. Sequences indict themselves."],
   [C("Build the review packet with your counsel (appointed, as always, under 42 Pa.C.S. § 6337): the intake form, the March entry, Hakim's study status, the Kellermans' bridge offer.", "packet52", setFlags=["packetBuilt"])]),
 N("packet52", 18, "Six days of margin",
   ["Hakim's approval is the race's photo finish: clearances clear, home approved, references glowing — and the final supervisor signature scheduled for August 26th, the day before the review, if the supervisor's queue cooperates. Ms. Nowak confirms the timeline in writing, because by now everyone on this case has learned what writing is for.",
    "Sanaa packs a 'maybe bag' at the Kellermans' — her words — with two compartments she labeled herself: 'Uncle's' and 'Elsewhere.' Thirteen-year-olds should not have to label bags like that. The review decides which label was right."],
   [C("At the review, ask that Hakim be heard on his qualifications as a potential kinship care resource (§ 6336.1) whether or not the signature has landed.", "review52", setFlags=["hakimHeard"])]),
 N("review52", 24, "August 27th",
   ["The courtroom holds the whole geometry: the Kellermans in the second row, entitled to notice and to be heard, offering their bridge; Hakim in a tie Sanaa picked, heard on his qualifications under § 6336.1 — the school bus route he drives past her school, the room, the decade of Eid dinners; and Sanaa's own statement, taken by the judge in chambers and summarized with care: 'Uncle's. Please. Uncle's.'",
    "Ms. Nowak presents the agency's plan. This morning, it is one of two documents. The signature is either on it, or it isn't."],
   [C("Listen for which document she is holding.", "outcome52")]),
 N("outcome52", 24, "The signature",
   ["Thirty days was never much time. What filled it — the corrected number, the expedited study, the bridge, the packet — decides what the agency can recommend today."],
   [C("Hakim's approval is signed, his qualifications heard, the Kellermans' transition offered: placement with the uncle, before September 2nd.", "end_familyaddress", requiresFlags=["kinWritten", "packetBuilt", "hakimHeard"]),
    C("The approval is days short of signed. The Kellermans' bridge covers the gap — barely — and the group placement waits in between.", "end_elevendays"),
    C("No kin was ever reached in time, and the file shows a plan built on one wrong number.", "end_defaultplan")]),
 E("end_familyaddress", 24, "Ending — A Family Address, Not a Facility",
   ["Sanaa moves to Hakim's on August 30th — three days inside the deadline — with the Kellermans carrying her boxes and staying for the rice, which is, she reports, right. The group placement's bed goes to a teenager whose family search is still running. The judge's order does one more thing: it directs the agency to note the corrected family-finding entry, so the file's March mistake stops being the family's official history.",
    "The sequence that won: the deadline was written down the day it existed (August 3rd → September 2nd); kinship was investigated by name, not by category — 'what kin has been contacted, by name' is the question that found a wrong digit; the teenager's own knowledge was put into the record in her own hand; the study ran expedited because the letter stated the date in its first line; and at the hearing, both seated voices were used — the foster parents' right to notice and to be heard, and the potential kinship care resource's right to be heard on qualifications (42 Pa.C.S. § 6336.1; the definition at § 6302, added by Act 48 of 2023). Underneath it all, the parent's record right (§ 3130.44(d)) supplied the exhibit that made 'family finding' answer for itself.",
    "What no strategy controls: Hakim. A willing uncle with a clear record and a spare room is not a strategy output — he is a family's luck, and many families' searches find less. The strategy's promise is narrower: if the Hakim exists, he will be found in time, dialed correctly, studied fast, and heard. Group placements fill with teenagers whose Hakims were in the file the whole time, under the wrong number."]),
 E("end_elevendays", 35, "Ending — Eleven Days Between (partial)",
   ["The approval lands September 4th — two days after the notice ran, nine days after the Kellermans' house closing forced the end of their bridge. Sanaa spends eleven days in the group placement: a bed in a room with three other girls, a worker who is kind, a curfew bell. Then she moves to Hakim's, where the room had been waiting, painted, since August. She counts the eleven days the way teenagers count such things: exactly, and forever.",
    "This partial ending is the honest center of the scenario, because deadlines in kinship work are not lost in courtrooms — they are lost in queues: a supervisor's signature queue, a clearance queue, a queue for a queue. Everything in the winning route was done here too, and done well; the margin was simply thinner than the bureaucracy. The lesson is not 'do it better.' It is 'start the clock-watching earlier than feels reasonable.' The March entry sat wrong for five months before the notice made it urgent. Families cannot audit what they cannot see — which is why the record request (§ 3130.44(d)) belongs at the START of a placement, not at the emergency.",
    "Sanaa's eleven days are in the file now, and so is the sequence that caused them. If this system ever asks her to trust it again, it will have to answer for the digit. Files remember. That, in the end, is the family's leverage and the system's teacher."]),
 E("end_defaultplan", 35, "Ending — The Default Plan",
   ["Sanaa moves to the group placement on September 2nd, on schedule, because schedules are what default plans have instead of people. Her file's recommendation says 'no available kinship resource,' a sentence that will be copied into the next review's packet, and the next, acquiring truth by repetition — about an uncle whose phone never rang, at a number that was in the file all along.",
    "This ending is the scenario's reason to exist. It requires no villainy: one transposed digit, one unreturned-by-stranger voicemail, a category assumption ('family homes don't take teens') doing the work family finding was supposed to do. Default plans are what happen to unexamined files, and teenagers — whose placements are the system's hardest and whose voices are its most discounted — absorb the defaults. The countermeasures are all unglamorous: ask for contacts by name, in writing; put the child's own family knowledge in the record; request the file early and read the family-finding page first; and treat 'contacted' as a claim to be verified, not a fact to be accepted.",
    "From here, the road back runs through the next review: Hakim, once alerted, can still be studied and heard (§ 6336.1), and group placements are reviewed, not eternal. But the guide's honesty requires the ending's real name: the default won this round, and it won in March, silently, one digit at a time."]),
]

# ============================================================ S53 (Complex)
def add_months(d, m):
    y = d.year + (d.month - 1 + m) // 12
    mo = (d.month - 1 + m) % 12 + 1
    return date(y, mo, d.day)

S = date(2027, 1, 4)
assert fmt(S) == "Monday, January 4, 2027"
PLACED53 = date(2026, 2, 2)
ASFA53 = add_months(PLACED53, 15)
assert ASFA53 == date(2027, 5, 2), ASFA53          # fifteen months after Feb 2, 2026
REVIEW53 = S + timedelta(days=108)
assert fmt(REVIEW53) == "Thursday, April 22, 2027"

s53_meta = {
    "title": "The First 90 Days",
    "subtitle": "Scenario 53 — Every Bed in the County (a fictional composite)",
    "startDateISO": "2027-01-04",
    "startNode": "start",
    "startCash": 240,
    "tier": "Complex",
    "summary": "You are Cyrus. Your three children have been in care since February 2nd of last year — Selah, twelve, in one foster home; Rafi, nine, and Nina, five, in another, forty minutes apart. Your mother Esther said in March she could take Nina. Only Nina. On May 2nd your children reach fifteen months in care, and the law's permanency clock strikes. This scenario is about what gets built before it does.",
}
s53 = [
 N("start", 0, "Month twelve",
   ["The letter from the agency is polite and has a date in it, which makes it not polite at all: a permanency review is scheduled for April 22nd, and the children's time in care — placed February 2, 2026 — will reach fifteen months on May 2, 2027. Fifteen months is not an anniversary. Under the federal Adoption and Safe Families Act, when a child has been in foster care for 15 of the most recent 22 months, the state must file to terminate parental rights or document a statutory exception (42 U.S.C. § 675(5)(E)).",
    "You have three children in two houses and one grandmother who said a sentence in March that the file turned into a wall. The next sixteen weeks are this scenario."],
   [C("Read the letter twice. Then call your counsel — appointed under 42 Pa.C.S. § 6337 — and ask the only useful first question: \"What are the three exceptions, exactly, and which ones could this family actually build?\"", "three_exceptions", addHidden=["asfa-clock"])]),
 N("three_exceptions", 1, "The three doors",
   ["Your counsel, Mr. Zielinski, keeps a yellow pad for arithmetic. \"Door one: the child is being cared for by a relative. Door two: a documented compelling reason that filing isn't in the child's best interest. Door three: the agency didn't provide the services it was supposed to provide. Door one is the strongest, because it isn't an argument — it's an address. Whose address?\"",
    "\"My mother's,\" you say. \"For one of them. In March she said she could take Nina. The file says she 'declined placement.'\" Mr. Zielinski puts his pen down in the particular way lawyers do when a case changes shape. \"Then the first fight is about what your mother actually said.\""],
   [C("Get the record. All of it — your written request under 55 Pa. Code § 3130.44(d) goes in this week, aimed first at the March kinship notes.", "record53", setFlags=["recordsRequested"], addHidden=["record-request"], cash=-10)]),
 N("record53", 6, "What March actually said",
   ["The March note, when it arrives, is three lines: 'Paternal grandmother contacted. States she could take the youngest 'if it comes to that.' States three is too many with her arthritis. Declined placement of sibling group.' Read it again: she answered a question about all three, at once, in a cold call, three weeks after the children were taken — and the answer to that question got filed as the answer to every question.",
    "Nobody lied. A narrower question was simply never asked: not 'all three, tonight, alone forever' — but 'what could you take, with what help, starting when?'"],
   [C("Write the correction: a letter for the file stating what Esther was asked, what she answered, and that she is now asking to be studied for a plan — with supports — for all three.", "correction53", setFlags=["marchCorrected"])]),
 N("correction53", 9, "Asking the narrower question",
   ["Esther, at her kitchen table, is precise about her own limits, which is why she can be trusted about her capacity: \"Three children, alone, at sixty-nine, with these hands — no. Three children with the after-school program at the church, with your sister doing Saturdays, with you twelve minutes away and off the truck route by five — ask me that question.\"",
    "A kinship plan with supports is not a smaller promise. It is a specified one. The study that follows will test the specification, which is why every support has to be a document, not a hope."],
   [C("Build the support plan as paper: the church program's letter, your sister's signed Saturday commitment, your employer's route letter.", "support_plan", cash=-12)]),
 N("support_plan", 13, "The plan, specified",
   ["Three letters, three signatures, three phone numbers. The after-school program confirms Selah and Rafi weekdays until six, Nina in the preschool room. Your sister commits Saturdays in writing 'for as long as it takes, which is what family means.' Your employer's letter moves your last delivery to 4:40 p.m. The pile is thin and total: it converts 'Esther plus hope' into 'Esther plus a system.'",
    "Ms. Nilsen, the children's worker, receives the packet with the expression of a woman whose March note just became a January plan. \"A resubmission,\" she says. \"New study, based on the plan. I'll schedule it.\""],
   [C("\"Schedule it with dates. Study visit, clearance renewals, report — I want the dates in a letter.\"", "study_dates", setFlags=["studyScheduled"])]),
 N("study_dates", 16, "Dates, in a letter",
   ["The letter that comes lists them: home visit February 9th; Esther's updated clearances filed; interviews with each child; report due March 20th. Between now and the report sit three problems you already know about: the stairs to the bedrooms and Esther's arthritis; Nina's preschool transport; and the person this scenario has been avoiding — Selah, twelve years old, who has her own opinion and, it turns out, her own lawyer.",
    "Children have counsel too. Selah's has requested a meeting. With you."],
   [C("Go. Listen more than you talk. She is not a obstacle to the plan; she is one of its authors.", "selah_voice")]),
 N("selah_voice", 20, "Selah's position",
   ["Selah's counsel lays it out with the care of someone translating, not negotiating. \"Selah loves her grandmother. She also has a life: her school, two years in the same building, the art teacher who wrote her a recommendation, and a foster mother who taught her to braid and shows up. She is asking: why does helping Rafi and Nina require her to be the one who moves?\"",
    "It is the best question in the case, and it is asked by a twelve-year-old through a lawyer, which is how this system hears children when it hears them at all. The answer cannot be 'because the clock.' It has to be an address that keeps her life intact — or an honest acceptance that her door is a different door."],
   [C("Ask the factual question before the emotional one: \"What school district is my mother's house in — and is it Selah's?\"", "school_question")]),
 N("school_question", 22, "One district",
   ["It is. Esther's house sits in the same school district as Selah's foster home — geography's small mercy, verified in writing from the district office at your request, because in this scenario nothing is true until it is paper. Selah could move to her grandmother's and keep her school, her art teacher, and her recommendation.",
    "What she cannot keep, if she moves, is the daily presence of the foster mother — unless the plan keeps that too."],
   [C("Ask Selah's counsel to put Selah's terms to her precisely: same school guaranteed, monthly overnight with her foster mother, her art portfolio wall at Grandma's — and her answer given the weight it deserves.", "selah_terms", setFlags=["selahHeard"])]),
 N("selah_terms", 27, "Her terms",
   ["Selah's answer, when it comes back through her counsel, is a twelve-year-old's treaty: yes to Grandma's — if the school letter is real, if the overnights are written into the plan and not 'when possible,' and if nobody makes her call it anything but what it is: a move she chose with conditions, not a rescue she was handed. She also asks to keep braiding lessons. Some conditions are just love with appointments.",
    "Mr. Zielinski writes the terms into the placement proposal verbatim. \"Courts can smell when an adult paraphrases a child into compliance. We will not be doing that. Her words, her conditions, addressed one by one.\""],
   [C("File the proposal: Esther, all three, supports specified, Selah's terms attached and answered.", "proposal_filed", setFlags=["selahPlan"], addHidden=["child-voice"])]),
 N("proposal_filed", 31, "The study visit",
   ["February 9th arrives with a worker, a tape measure, and Esther's house scrubbed to surgical brightness. The rooms pass. The clearances pass. The stairs do not — not as a failure of the house, but as a question: a sixty-nine-year-old with arthritis, three children, bedtime upstairs. The worker writes 'mobility — plan?' in the margin and keeps walking, which is the study system working exactly as it should: a question, asked in time to be answered.",
    "Your answer takes ten days and a contractor cousin: a first-floor room — the dining room, which has hosted four dinners a decade — converted to Esther's bedroom, with the bathroom beside it. The children get the upstairs. The stairs become the children's problem, and children are stair professionals."],
   [C("Convert the room. Document it: photos, the cousin's invoice, and Esther's doctor's note confirming the arrangement.", "room_fix", cash=-30, setFlags=["stairsSolved"])]),
 N("room_fix", 41, "Problem, answered",
   ["The study's addendum records the conversion in the flat prose that moves courts: 'Mobility concern addressed; primary caregiver sleeping quarters relocated to first floor with adjacent bath.' Underneath the prose is the recurring arithmetic of kinship: a problem found early is a project; the same problem found at the hearing is a reason.",
    "Two voices remain to be reckoned with, and both belong to people who have loved your children daily: Rafi and Nina's foster parents."],
   [C("Ask Ms. Nilsen what their position will be at the review — and do not flinch from the answer.", "foster_position")]),
 N("foster_position", 48, "The other attachment",
   ["Rafi and Nina's foster parents have had the two youngest for a year. Nina calls their dog by a name she invented and believes is its real name. They will be heard at the review — foster parents receive notice of hearings and have the right to be heard (42 Pa.C.S. § 6336.1) — and what they will say is honest: the children are attached; another move is another loss; they are willing to keep both children 'as long as needed.'",
    "This is the part of kinship work that slogans skip. Their love is real evidence, and it will be weighed. What answers it is not denying it — it is the documented whole: siblings together, with family, in one district, on terms the eldest set herself."],
   [C("Propose the bridge in writing: Rafi and Nina keep monthly visits with their foster parents, written into the plan — continuity, not erasure.", "bridge53", setFlags=["bridgeOffered"])]),
 N("bridge53", 55, "Continuity, not erasure",
   ["The foster parents receive the written proposal through the agency and respond in kind, in writing, with a sentence Mr. Zielinski reads twice: 'If the court moves them, we will help them land. We ask that the landing include us, a little, for a while.' It is the sound of a system working at its best — attachments treated as assets to be transferred, not territories to be defended.",
    "March 20th, the study report issues: Esther approved for the sibling group of three, with the support plan incorporated by reference. The paper part of door one — the relative exception — is now buildable."],
   [C("Ask Mr. Zielinski to draft the ASFA exception documentation for the April review: children to be cared for by a relative, placed before the fifteen-month date.", "exception_draft", setFlags=["studyApproved"])]),
 N("exception_draft", 66, "Door one, documented",
   ["The exception paperwork is almost anticlimactic, which is its virtue: if Selah, Rafi, and Nina are placed with their grandmother before May 2nd, the statute's relative-care exception is satisfied by the placement itself, and the filing obligation the clock creates is answered with an address and a date (42 U.S.C. § 675(5)(E)). The review on April 22nd is where the placement must be ordered — ten days before the clock strikes.",
    "What remains is the agency's recommendation, and agencies recommend what their files make easy. Mr. Zielinski inventories yours in the office, the week before: study approved; supports signed; Selah's terms answered; bridges offered; March corrected. \"There is one more document,\" he says, \"that I want in the judge's hands. The children's own words — collected by their counsel, not by you.\""],
   [C("Their counsel collects them. You do not rehearse, coach, or even ask what was said. Some pages must arrive clean.", "children_words", setFlags=["childrenWords"])]),
 N("children_words", 78, "Clean pages",
   ["What the children said becomes known to you only as the court will know it: Rafi asked if Grandma's house has 'room for the fort.' Nina asked about the dog. Selah restated her terms and added one: 'Tell them I said yes myself.' The statements are filed by their counsel as the children's position, and your disciplined absence from them is what makes them evidence instead of choreography.",
    "April approaches with the docket's ordinary weather: a continuance scare, resolved; a supervisor's signature, obtained; a school letter re-verified. Then the 22nd."],
   [C("Go in with the file you built. It is, in the end, the argument.", "review53")]),
 N("review53", 108, "April 22nd",
   ["The courtroom is crowded with your children's lives: Esther in her good dress, approved and documented; the foster parents, heard under § 6336.1, saying their honest piece and their written bridge; Selah's counsel stating Selah's terms and Selah's yes; the agency, Ms. Nilsen presenting, with a recommendation that the last four months either built or didn't.",
    "The judge looks up from the packet. \"The fifteen-month date is May 2nd. Counsel, tell me why this court is not looking at a filing obligation — or tell me about the filings.\""],
   [C("Let Mr. Zielinski answer with the file. It is the moment the file was built for.", "outcome53")]),
 N("outcome53", 108, "May 2nd, answered in April",
   ["The answer depends on which doors the winter actually built — a relative's address, a child's own terms, or only an argument."],
   [C("Esther is approved for all three, the supports are documents, Selah's terms are in the plan, and placement can occur this week — before the clock: the relative exception, satisfied by placement.", "end_allthree", requiresFlags=["studyApproved", "selahHeard", "selahPlan", "marchCorrected"]),
    C("The younger two are ready for Esther's; Selah's terms could not be met, and she stays — by her own stated choice, documented, with her siblings twenty minutes closer than before.", "end_twohome"),
    C("No placement is ready, but the exception and compelling-reason documentation is complete and filed, answering the clock while the plan continues.", "end_clockanswered"),
    C("The file reaches April thin — a March sentence uncorrected, a study still pending, a child unheard.", "end_fifteenmonths")]),
 E("end_allthree", 108, "Ending — All Three, One Table",
   ["Placement is ordered for Friday, April 23rd — nine days before the clock. Selah keeps her school and gets her overnight clause in writing; Rafi gets a yard with fort jurisdiction; Nina gets a grandmother and, by written bridge, keeps a little of the dog. When May 2nd arrives, it finds the children where the statute's first exception contemplates: being cared for by a relative (42 U.S.C. § 675(5)(E)). No petition is filed, because the law's filing duty is answered by the placement itself.",
    "Inventory the win, because it was assembled, not granted: a March sentence corrected with the March record (requested under 55 Pa. Code § 3130.44(d)); a grandmother's capacity specified as a system of signed supports rather than asserted as a virtue; a mobility problem converted into a converted room; a twelve-year-old treated as an author rather than an obstacle — her terms taken verbatim, her school verified in writing, her yes obtained instead of assumed; and foster attachments bridged rather than bulldozed, with the foster parents heard as § 6336.1 provides. Each piece is a document. The stack of documents is the outcome.",
    "What no strategy controls: Esther's health across the years this plan must run, Selah's heart across the first hard month, and a judge who might have weighed the foster attachments differently on the same packet. ASFA's clock is often described as the parent's enemy. This scenario's truer lesson: the clock is a deadline, and deadlines reward the side that builds toward them. The agency had a calendar. This time, so did the family."]),
 E("end_twohome", 108, "Ending — Two Home, One by Choice (partial)",
   ["Rafi and Nina move to Esther's on Friday. Selah does not — and the order says why, in her counsel's words, not an adult's summary: her terms could not all be met this spring, and she elects to remain where she is, with sibling time doubled, Esther's house as her second address, and the question expressly preserved for the next review. The relative exception covers the two who moved; Selah's permanency takes the documented-compelling-reason road, with her own statement as the documentation.",
    "Call this what it is: a partial win with an honest spine. The system's easiest story — 'the grandmother took the little ones; the teenager was left' — is false here, and the record proves it false: Selah was offered the move on terms she set, the terms were pursued, and her no was treated as information rather than defiance. In dependency law, an older child's documented choice is not a failed placement. It is permanency planning done at the speed of consent.",
    "The next review inherits a running household, two settled children, and a teenager whose trust was kept. Families reunify in stages more often than in single orders. This stage was built correctly."]),
 E("end_clockanswered", 112, "Ending — The Clock, Answered (partial)",
   ["No beds move in April — but no petition is filed in May either. The court accepts the documentation: Esther's approval finalized in principle, the placement plan dated, and the compelling reasons written with specificity rather than incantation — which is what the exceptions in 42 U.S.C. § 675(5)(E) actually require when they apply: not that the clock be ignored, but that its exceptions be documented like facts instead of hoped like weather.",
    "This is the ending for families whose facts are strong and whose timing is not, and it is a real outcome, not a consolation: the difference between a documented exception and an undocumented intention is the difference between a plan and a termination petition. Many cases are lost precisely here — an exception that existed in the family's living room but never made it into the agency's documentation.",
    "The work continues with the clock answered: the study completes, the placement follows in June, and the next review reads a file that treats May 2nd as a date that was prepared for. Prepared-for is the entire discipline."]),
 E("end_fifteenmonths", 121, "Ending — Fifteen Months",
   ["May 2nd arrives with the children still in two foster homes, Esther's study still pending, and a March sentence still standing uncorrected in the file — and the law does what the law said it would do: the agency files petitions to terminate your parental rights, citing fifteen of the last twenty-two months in care (42 U.S.C. § 675(5)(E)). The petitions are not the end of the case — termination must still be proven by clear and convincing evidence, grounds and needs-and-welfare both, at a hearing where everything in this scenario could still be built. But the case's center of gravity moves, permanently, from 'when do they come home' to 'whether you remain their father in law.'",
    "Read the route that led here without flinching: the clock was known in January. What was missing was never love, time, or even cooperation — it was sequence. The March record unrequested; the narrower question unasked; the study unstarted while weeks did what weeks do. ASFA does not require families to be perfect. It requires the file to be built before the date, and it is pitiless about the difference between 'in progress' and 'documented.'",
    "If you are living this ending: the petitions raise the stakes; they do not seal them. Build now what January asked for — the corrected record, the specified kinship plan, the children's own voices — and build it for a termination hearing's higher burden. Many fathers have. The calendar that hurt you is also the calendar that tells you exactly how much time the other side needs to prove its case. Use yours better."]),
]

# ============================================================ S54 (Complex)
S = date(2026, 10, 5)
assert fmt(S) == "Monday, October 5, 2026"
CONF54 = S + timedelta(days=17)
assert fmt(CONF54) == "Thursday, October 22, 2026"     # Rule 1340 pre-hearing conference
REVIEW54 = S + timedelta(days=24)
assert fmt(REVIEW54) == "Thursday, October 29, 2026"

s54_meta = {
    "title": "The First 90 Days",
    "subtitle": "Scenario 54 — The Assessment Nobody Signed (a fictional composite)",
    "startDateISO": "2026-10-05",
    "startNode": "start",
    "startCash": 230,
    "tier": "Complex",
    "summary": "You are Veronica. Your son Otto, six, has been placed for four months, and the agency now recommends moving him to a 'higher level of care' home across the county — based on a scored assessment you have never seen, whose central item contradicts the visit logs you have. Your father's name is Salvatore. He has been at every visit. The assessment has never heard of him. This scenario is about making the court decide on the whole record.",
}
s54 = [
 N("start", 0, "The recommendation",
   ["The agency's review summary is three pages, and its conclusion is one sentence: 'Based on the assessment results, the agency recommends placement in a therapeutic foster home (Level II), Riverton County.' Otto is six. His current foster home is eleven minutes from your apartment. Riverton County is fifty. The word 'assessment' appears four times in the summary. The assessment itself appears zero times.",
    "Your father Salvatore, who has sat beside you at every supervised visit for four months, reads the summary twice and asks the question that organizes this entire scenario: \"Where is this test, that it knows Otto better than the visits?\""],
   [C("Ask your counsel, Ms. Lindgren, the procedural version of your father's question: \"Can they recommend a move on a document I can't read?\"", "counsel54", addHidden=["assessment-score"])]),
 N("counsel54", 1, "Two keys",
   ["\"Two keys open that document,\" Ms. Lindgren says. \"First, your record right: as a party, you may request the case record in writing — 55 Pa. Code § 3130.44(d) — and the assessment used to justify a placement recommendation is part of the record of your son's case. Second, the rules: under Pa.R.J.C.P. 1340(E), when an assessment is used in a dependency proceeding, it must be made available to all parties in advance of the pre-hearing conference. Our conference is October 22nd. The review is the 29th. Both clocks are ours to use.\"",
    "\"And if they send it redacted to alphabet soup?\" — \"Then we read 55 Pa. Code § 3130.44(f) together: the confidentiality rules 'shall not be construed as protecting the agency's employees.' Names get complicated. Scores and items don't get to hide at all.\""],
   [C("File the § 3130.44(d) request today, naming the assessment expressly: the full instrument, item responses, and scoring — not the summary.", "request54", setFlags=["recordsRequested"], addHidden=["record-request"], cash=-9)]),
 N("request54", 3, "What arrives",
   ["What arrives, eleven days later, is the assessment — most of it. The item pages are there: twenty-two scored items, a composite, and a recommendation grid. What is blacked out is instructive: the rater's name and signature line, two narrative paragraphs, and — bizarrely — the header of the scoring page, as if the form's own title were a state secret.",
    "The redactions are annoying. They are also the least important thing in the packet, because the items are readable, and one of them is wrong in a way you can prove."],
   [C("Go to the item the recommendation rests on. Find it before you fight about ink.", "the_item")]),
 N("the_item", 5, "Item 14",
   ["Item 14, 'Supervision incidents during family time (90 days),' is scored 3 — 'multiple incidents' — and the recommendation grid maps a 3 on Item 14 to 'consider Level II placement.' The narrative beside the score says: 'Mother required redirection regarding supervision on three occasions.' Three occasions. You have attended eleven supervised visits in ninety days. The supervisor's logs — signed, dated, kept by the visitation center — are documents you have never been given, because you never asked for them in writing. You ask now.",
    "One redirection you remember, because it was real: you arrived seven minutes late once, in the rain, and the log will say so. Three is a different number. Three is a placement across the county."],
   [C("Request the visitation center's logs for all eleven visits — your own written request, as a party, added to the record list.", "visit_logs", setFlags=["logsRequested"])]),
 N("visit_logs", 8, "Eleven logs",
   ["The logs arrive as eleven one-page forms, and they are the most beautiful documents in this scenario, because they are boring: arrivals, activities, a supervisor's initials, the small weather of ordinary visits. 'Redirection regarding supervision' appears once — visit three, your late arrival, noted and closed. Two other visits record the supervisor stepping in — both times to assist with a spilled juice and a broken toy truck, both logged as 'environmental,' neither about you.",
    "Item 14's 'three occasions' appears to have been assembled from one real redirection and two juice spills, the way scores get built when a rater works from a summary of a summary. You do not know that yet. What you know is narrower and stronger: the signed primary records of the visits say one."],
   [C("Take the logs and Item 14 to Ms. Lindgren. \"What do we file, and when?\"", "correction_filing")]),
 N("correction_filing", 10, "The correction memorandum",
   ["\"A correction memorandum, filed before the conference, so the conference has something to confer about,\" she says. \"Rule 1340's structure is our friend: under Rule 1340(A) we file a pre-hearing conference statement summarizing the evidence; under 1340(E) the assessment was to be available to all parties in advance — it was, barely, and redacted; under 1340(F) the conference exists to narrow the issues for the hearing. Our narrowed issue is one item, one number, and eleven logs.\"",
    "She is equally clear about the frontier: whether Rule 1340's assessment provisions reach the newer standardized assessment instruments the agency used here is a question Pennsylvania's appellate courts have not squarely decided. \"We argue the rule's text — an assessment used in a dependency proceeding. We do not tell the judge it's settled law. Judges forgive frontiers. They do not forgive being told a frontier is a highway.\""],
   [C("File the memorandum: Item 14, the eleven logs, the grid it fed — and a request that the rater be identified and available.", "memo_filed", setFlags=["correctionFiled"], addHidden=["item-rebuttal"])]),
 N("memo_filed", 12, "The rater",
   ["The rater's identity comes out through the redaction fight, and it is anticlimactic in the way that matters: a caseworker — not yours — who completed the assessment from the file during a staffing crunch, and whose signature the agency shielded as though she were an informant. Section 3130.44(f) exists for exactly this reflex: the regulation 'shall not be construed as protecting the agency's employees,' and once Ms. Lindgren quotes it, the name is produced by stipulation rather than order.",
    "Whether she attends the hearing is contested. What is no longer contested is that the assessment has an author, the author worked from summaries, and the summaries were wrong about the visits."],
   [C("Before the conference, make the call this scenario has been walking toward since page one: \"Dad. If the move is stopped, the next question is where Otto thrives — not just where he isn't moved from. Will you be studied?\"", "salvatore_call")]),
 N("salvatore_call", 14, "Salvatore",
   ["Your father is seventy-one, a retired tool-and-die man with a house he has owned for forty years, a garden that feeds the street, and a grandson who has spent four months of visits teaching him dinosaurs. He has also been waiting — he tells you now — for someone to ask him as a plan rather than thank him as a visitor. \"I thought the foster home was the plan,\" he says. \"If the plan can be me, then the plan is me.\"",
    "His written kinship submission goes in the same week: name, address, the spare room that was Otto's father's childhood room, and his request to be studied — filed early enough to be an alternative at the hearing, not an aspiration after it."],
   [C("Salvatore files his written kinship request and begins clearances before the conference.", "salvatore_files", setFlags=["kinFiled"], addHidden=["named-kin"], cash=-14)]),
 N("salvatore_files", 16, "The conference",
   ["October 22nd. The pre-hearing conference does what Rule 1340(F) says conferences are for: it narrows. The agency, confronted with its own visitation center's logs, does not defend the number three — it defends the move anyway, on the composite score and 'clinical judgment.' Ms. Lindgren accepts the concession and frames the hearing: the composite embeds Item 14; remove the error and the grid's own logic no longer maps Otto to Level II at all.",
    "What the conference cannot do is settle it. It settles the shape of the fight: one item, one grid, one alternative with a name and a garden."],
   [C("Ask the conference to record the narrowed issues in its order — including the agency's non-defense of Item 14 as scored.", "narrowed_order", setFlags=["issuesNarrowed"])]),
 N("narrowed_order", 18, "Narrowed, in an order",
   ["The conference order is two paragraphs, and the second one is the scenario's trophy: 'The parties stipulate that Item 14 of the assessment, as scored, is not supported by the visitation records; the agency's recommendation is otherwise maintained.' Stipulations are the load-bearing walls of hearings — facts no longer requiring proof, agreed by the side that loses by them.",
    "The agency's remaining position is honest and thin: judgment, gestalt, caution. Against it stands a corrected arithmetic and a grandfather. Ms. Lindgren spends the last week on the only question left."],
   [C("\"Prepare Salvatore to be heard on his qualifications — § 6336.1 gives a potential kinship care resource that right, and the court must then decide his notice going forward.\"", "hearing_prep54", setFlags=["salvatoreReady"])]),
 N("hearing_prep54", 21, "Preparing a grandfather",
   ["Preparation, for a man of Salvatore's generation, is mostly wardrobe and one sentence. The sentence is his, arrived at after two evenings of your questions: \"I am not asking the court to reward me. I am asking it to count me — I have been at every visit, and Otto has a room in my house that was ready before this case had a name.\" His clearances are back, clean. His home visit is done and written up without a single flagged item — a fact the agency does not contest.",
    "The hearing is October 29th. The agency brings its recommendation. You bring the record it was built on, corrected — and the man it never mentioned."],
   [C("Go in.", "review54")]),
 N("review54", 24, "October 29th",
   ["The agency's witness presents the assessment honestly now: the composite, the grid, the residual judgment. On cross, the stipulation does its silent work — Item 14 falls out of the arithmetic in front of the judge, and the recommendation is left standing on the word 'caution.' Then Salvatore is heard, on his qualifications, as § 6336.1 provides — and a retired man's forty years in one house turn out to be a short, complete answer to 'higher level of care.'",
    "The judge asks the agency the question the whole scenario built: \"On the corrected record — the whole record — why Riverton County?\""],
   [C("Listen to whether the answer names anything in Otto's actual life.", "outcome54")]),
 N("outcome54", 24, "The whole record",
   ["Recommendations survive on the record beneath them. What this one rests on, today, is a choice the last three weeks made."],
   [C("The correction was stipulated, the item fell out of the grid, and a qualified kinship alternative stood in the room: the court rules on the whole record.", "end_readinfull", requiresFlags=["correctionFiled", "issuesNarrowed", "kinFiled"]),
    C("The move was defeated on the arithmetic, but no alternative placement was ready to be ordered today.", "end_movethatwasnt"),
    C("The court heard only the summary — the assessment unread, the logs unrequested, the grandfather unmentioned.", "end_summary")]),
 E("end_readinfull", 24, "Ending — Read in Full",
   ["The court declines the Riverton County move, finds the assessment's corrected arithmetic does not support a higher level of care, and orders Otto placed with his grandfather — Salvatore approved on the completed study, the placement to occur this weekend, with your visits expanding into his kitchen, where they apparently already lived. The order's reasoning paragraph does something worth more than the outcome: it directs that the corrected assessment be filed of record, so the next reader of Otto's file inherits the fixed number.",
    "The toolkit, in sequence: the party's record right (55 Pa. Code § 3130.44(d)) obtained the instrument itself, not the summary of it; § 3130.44(f) stripped the reflex redactions ('shall not be construed as protecting the agency's employees'); Pa.R.J.C.P. 1340(E) supplied the timing — assessment available to all parties in advance of the pre-hearing conference — and 1340(A)/(F) supplied the machinery: a conference statement, a conference that narrowed the case to one stipulated error. The kinship alternative was not a speech but a filed, studied, cleared grandfather, heard on his qualifications under 42 Pa.C.S. § 6336.1. And the frontier stayed labeled: whether Rule 1340's assessment provisions squarely govern the newer standardized instruments is untested in the appellate courts — argued from the rule's text, disclosed as argument, and strong enough on these facts because the agency's own logs did the heavy lifting.",
    "What no strategy controls: the rater could have been right. If the logs had shown three real redirections, this toolkit produces a fair loss instead of a win — the same memorandum, the same stipulation, the opposite arithmetic. The discipline is not a machine for winning. It is a machine for making the court decide on the true record — which is why it is worth building even when, especially when, you do not know what the record will say."]),
 E("end_movethatwasnt", 31, "Ending — The Move That Wasn't (partial)",
   ["The Riverton County move is denied — the corrected arithmetic saw to that — but the court keeps Otto in his current foster home for now, with Salvatore's kinship approval to be completed and the placement question relisted in thirty days. You leave with the loss converted: no fifty-mile move, no new school, no Level II label settling into his file like sediment. The grandfather question is not answered. It is scheduled.",
    "Partial endings in assessment fights usually take exactly this shape, because courts separate questions that parents experience as one: 'should he move up a level' is not 'should he move to kin.' Winning the first bought the time and the record for the second. The corrected assessment is filed of record; the stipulated error cannot quietly re-enter the next packet; Salvatore's study completes into a courtroom that has already heard his voice once.",
    "Thirty days is a short road when the paper is already built. Keep it built: attend everything, log everything, and let the relisted hearing decide about a boy whose file now tells the truth about his visits."]),
 E("end_summary", 31, "Ending — Decided on a Summary",
   ["Otto is moved to Riverton County on the strength of a three-page summary of a document no party read. The judge, presented with a composite score and an agency's assurance, did what judges do with unopposed arithmetic: accepted it. Your objection — sincere, accurate, and entirely oral — is noted in the order in the passive voice, where objections go to be forgotten.",
    "Nothing in this ending required the assessment to be right. It required only that it be unexamined. The counterfactual is the scenario: a written record request (§ 3130.44(d)) would have produced the instrument; the instrument would have produced Item 14; the logs would have answered Item 14; the conference machinery (Rule 1340(A), (E), (F)) would have narrowed the hearing to a stipulation. Each step is days of work and dollars of postage. Their combined price is a childhood address — his school's name, his grandfather's street, the eleven minutes between his home and yours.",
    "If you are reading this from inside it: the move is ordered, not eternal. Placement orders are revisited at every review, and the toolkit remains exactly as available next month as it was in October — heavier now by one exhibit, the move itself, and what it cost a six-year-old. Build the record for the review that follows this one. Summaries rule only the hearings where nobody brings the book."]),
]

# ============================================================ S55 (Complex)
S = date(2026, 11, 2)
assert fmt(S) == "Monday, November 2, 2026"
REVIEW55 = S + timedelta(days=31)
assert fmt(REVIEW55) == "Thursday, December 3, 2026"

s55_meta = {
    "title": "The First 90 Days",
    "subtitle": "Scenario 55 — The County Line (a fictional composite)",
    "startDateISO": "2026-11-02",
    "startNode": "start",
    "startCash": 205,
    "tier": "Complex",
    "summary": "You are Imani. Your daughter Zola, eight, was moved across the county line last Thursday — a foster home emergency, the agency says, and no beds in your county. Your sister Beatrice, in your county, was identified as kin at intake in February. The file says a packet was mailed to her. Beatrice says nothing ever came, and Beatrice keeps everything. One of them is wrong, and the proof is in a record you have the right to read.",
}
s55 = [
 N("start", 0, "The school calls",
   ["You learn about the move from Zola's school, which is how you learn the school no longer has Zola. The secretary, gentle as a nurse with bad labs: \"She was withdrawn Friday, sweetie. Transferred to Riverton Elementary. We assumed you knew.\" Riverton is in the next county. Zola's desk is there now. Her reading group is there. Her visits with you, until Friday a twelve-minute drive, are fifty-five minutes each way — when the agency's transport runs, which it does not on weekends.",
    "You call the agency before you call anyone else, and Ms. Halvorsen gives you the sentence the system keeps for this: \"It was an emergency placement disruption. There were no beds in the county.\""],
   [C("Ask for it in the order the law will ask later: \"When exactly was she moved, who decided, and where is it written?\"", "when_who_written", addHidden=["move-notice"])]),
 N("when_who_written", 0, "When, who, written",
   ["Thursday evening. A supervisor's approval by phone. Written — she hesitates — 'in the placement log.' You note the hesitation the way you have learned to note everything: in your notebook, dated, with the time of the call. Emergency moves are sometimes real emergencies. They are also sometimes the moment a file reveals what it was doing all along.",
    "\"And my sister?\" you ask. \"Beatrice was identified in February.\" A pause with keyboard sounds in it. \"It says here a kinship packet was mailed to her February 12th. There's no response recorded.\""],
   [C("Call Beatrice before the hour is out. Ask her one question: \"What did you receive from the county in February?\"", "call_beatrice")]),
 N("call_beatrice", 0, "Beatrice keeps everything",
   ["Beatrice is a night-shift nurse who keeps a household the way hospitals keep charts: a binder, labeled by year, with sub-labels. She puts you on speaker and you can hear the binder open. \"February,\" she says. \"Car insurance. Your birthday card — you were late. A jury summons for March, which I served. Nothing from any county about Zola, because I would have framed it. Imani — I called them. February 20th and again in March. I spoke to a person. I wrote her name in this binder.\"",
    "Two paper systems are now in conflict: the agency's file, which says a packet was mailed and ignored; and your sister's binder, which says two calls were made and nothing arrived. One of these systems is about to be audited by the other."],
   [C("Call your counsel in the morning. The word for what you need is 'record' — and the fight has three fronts: the move, the kinship file, and Zola's fifty-five minutes.", "counsel55")]),
 N("counsel55", 1, "Three fronts",
   ["Your counsel lays it out on a legal pad in three columns. \"Front one: review. A party can ask the court to look at a placement move — we file, and we ask for interim relief on visits and school transport so the status quo doesn't harden while we litigate. Front two: the record. Your written request under 55 Pa. Code § 3130.44(d) — the family-finding page, the placement log, the move memo, the call notes. Front three: Beatrice, again, from zero — a fresh written kinship submission, so complete the county can't lose it.\"",
    "\"And if the record says the move was planned before the 'emergency'?\" — \"Then front one gets much easier. File everything this week.\""],
   [C("File all three: the review request, the § 3130.44(d) record request, and Beatrice's new written submission — with her February call dates in it.", "file_three", setFlags=["reviewFiled", "recordsRequested", "kinFiled"], addHidden=["record-request", "named-kin"], cash=-16)]),
 N("file_three", 3, "Filed in triplicate",
   ["Beatrice's new submission is a small masterpiece of un-losability: hand-delivered, date-stamped copy kept; her clearances initiated the same day; her landlord's name and number included pre-emptively; her night-shift schedule attached with the overnight care plan already written into it, because she has read enough of your case to know that questions answered before they're asked are called facts, and questions answered after are called excuses.",
    "The agency's response to your review filing arrives in four days: the move was necessary, the Riverton home is licensed and kind, 'no kinship resource was available,' and the matter is set for December 3rd."],
   [C("December 3rd is a month of fifty-five-minute drives. Fight the interim first: ask the court for expanded visits and school continuity now, not at the review.", "interim_ask")]),
 N("interim_ask", 6, "The interim",
   ["The interim ask is modest on purpose — courts grant modest asks from parties who are building to prove immodest ones. You ask for: weekend visits restored (at your home, supervised as before), agency transport for Wednesday visits, and Zola's school records and reading program shared with you weekly so her education doesn't fork into two counties' versions of third grade.",
    "You get most of it within the week, in a short order. Modest asks also do quiet work: they put a judge's eyes on the file a month before the review — a judge who now knows there is a county line in this case, and a sister, and a binder."],
   [C("Use the month. The record request is the engine — everything else is steering.", "record_arrives55")]),
 N("record_arrives55", 10, "The record arrives — first half",
   ["The family-finding page is everything Beatrice's binder promised. Intake, February: 'Maternal aunt, Beatrice [surname], identified by mother. States willing. Packet to be mailed.' Then the call notes — the agency's own — February 20th: 'Aunt called; states no packet received; advised packet remailed.' March 9th: 'Aunt called again; packet still not received; aunt advised to await study scheduling.' After March 9th: silence, in the file's handwriting. No packet tracking. No study scheduled. No third call made by anyone.",
    "The February 12th 'mailing' in the summary you were quoted was the intention. The remailed packet in the notes was the second intention. Neither intention has a tracking number, because neither, so far as this record shows, became an envelope."],
   [C("Read on. The placement log and the move memo are the second half — and you are looking for a date.", "the_date55")]),
 N("the_date55", 12, "October 20th",
   ["The placement log entry for Zola's move is dated Thursday, October 29th, 6:40 p.m. — 'emergency disruption, foster father hospitalized.' That part was true; the foster father's surgery was real, and no one begrudges the agency Thursday night. But beneath it in the packet sits the placement unit's memo, dated Tuesday, October 20th — nine days before the emergency — listing 'anticipated bed need, one female age 8, Riverton resource identified and held.'",
    "The Riverton bed was reserved nine days before the emergency that supposedly required it. What the memo actually documents is a unit managing capacity: a foster home known to be fragile — the father's health was in the file since September — and a contingency bed held in the next county because your county had none. The emergency was real. The county line was a plan."],
   [C("Give both dates to your counsel. \"October 20th and October 29th. The emergency was real and the line was planned. Both.\"", "two_dates", setFlags=["recordRead"])]),
 N("two_dates", 14, "What the dates do",
   ["Your counsel is careful, the way she is when something matters: \"We do not argue they invented an emergency. We argue the honest version: they planned for a disruption for nine days and never once, in those nine days, picked up the kinship file with Beatrice's name in it — a file with two logged calls from the aunt herself. A planned move has room for a kinship check. That omission is the case. Not villains. An omission, documented by their own paper.\"",
    "Meanwhile Beatrice's study, this time, must be impossible to lose. Her home county study is requested through the county where Zola's case sits — a courtesy study, in the jargon — and courtesy is exactly what you intend to audit."],
   [C("Get the courtesy study request in writing — who sent it, to whom, what date — and give Beatrice a copy to chase from her side.", "courtesy_study", setFlags=["studyTracked"])]),
 N("courtesy_study", 17, "Lost, once",
   ["The courtesy study request is 'sent' on a Tuesday. By the following Tuesday, Beatrice's county has no record of receiving it. This is the cross-county disease in its pure form: two bureaucracies, each certain the other is holding the baby. The difference this time is you — a person with a copy, a date, and a phone, standing between the two certainties until they reconcile.",
    "It takes four days and one hand-carried duplicate, delivered by Beatrice to her own county's office with a date stamp, to get the study opened. Four days, charged to nobody's account but Zola's calendar."],
   [C("Note it for the review: the study's timeline, including whose hands it passed through and whose it didn't.", "beatrice_study")]),
 N("beatrice_study", 21, "The study, this time",
   ["Beatrice's home study proceeds with the eerie smoothness of a thing being watched: clearances filed and returned, the home visit thorough, her night-shift care plan examined and accepted — her daughter, grown and ten minutes away, documented as the overnight adult on work nights, clearances filed for her too. One wrinkle: the landlord's consent letter for a placement in a rental, requested late by the worker, obtained by Beatrice in forty-eight hours because nurses understand documentation the way sailors understand weather.",
    "The report, when it issues, approves her without conditions. The woman the file wrote off in March as a non-response is approved in November on the first complete attempt."],
   [C("Ask for the study report's transmittal to the hearing county in writing, with a date — paper has died on that road before.", "transmittal", setFlags=["studyApproved"], cash=-10)]),
 N("transmittal", 25, "Zola's voice, and the Riverton truth",
   ["Two more documents complete the packet. Zola's counsel files her position: she likes the Riverton foster mother, who is kind and braids well; she wants her old school, her old reading group, and 'Aunt Bea's house, because it's ours.' Eight-year-olds in dependency cases are heard through counsel and the court's own care, and Zola's statement does what children's statements do at their best — it refuses to be anyone's exhibit and remains a person's wish list.",
    "And the Riverton foster mother, when your counsel's investigator asks about her expectations, gives the answer that rearranges the hearing: \"I took Zola as an emergency, thirty to sixty days. I'm a respite and emergency home. Nobody told me this was meant to be long-term.\" She is entitled to notice of the hearing and to be heard at it (42 Pa.C.S. § 6336.1). What she has to say serves Zola. It does not serve the move."],
   [C("Prepare the review packet: the February notes, the two dates, the approved study, Zola's position, the foster mother's statement.", "packet55", setFlags=["packetBuilt"])]),
 N("packet55", 28, "December approaches",
   ["The agency's pre-review position paper holds its line with one crack in it: the move was necessary and lawful; the Riverton home is appropriate; 'kinship was explored.' Explored is doing heavy lifting in that sentence, and December 3rd is where sentences get weighed. Your counsel's final preparation is about posture: \"We are not asking the court to punish anyone. We are asking it to place a child with her approved aunt, in her school district, in her county — and to notice that every document written since February points there.\"",
    "Beatrice will be heard on her qualifications — as a potential kinship care resource she has that right under § 6336.1, and the court must then decide her notice and participation going forward. Her binder comes with her. Of course it does."],
   [C("Go in with the binder, the two dates, and the study.", "review55")]),
 N("review55", 31, "December 3rd",
   ["The hearing runs on documents. The agency's worker is fair-minded and cornered by her own file: the February notes read aloud; the March silence; the October 20th memo; the October 29th entry. Beatrice is heard — qualifications, night shifts, the daughter ten minutes away, the binder produced once, to establish the February calls, and never flourished again. The Riverton foster mother, heard under § 6336.1, says her piece in four sentences and sits down.",
    "The judge turns to the agency. \"Counsel. Had the kinship study been run in March, or the aunt checked in the nine days before the move — where would this child be tonight?\""],
   [C("Listen. The answer to that question is the order.", "outcome55")]),
 N("outcome55", 31, "Across the line",
   ["The order depends on whether the court was shown a move that had to happen — or a kinship home that was never actually tried."],
   [C("The packet was complete: the February record, the planned nine days, the approved aunt, the child's own position, and the emergency home's honest limits.", "end_backacrosstheline", requiresFlags=["recordRead", "studyApproved", "packetBuilt"]),
    C("The court splits it: Zola stays in Riverton for stability now, with Beatrice approved and woven in — weekends, respite, school transport — and the placement relisted.", "end_bridge55"),
    C("The move was defended as necessity and the kinship record never made it into evidence.", "end_fiftyminutes")]),
 E("end_backacrosstheline", 31, "Ending — Back Across the Line",
   ["Zola is placed with Beatrice, effective the following Monday, and re-enrolled in her old school, where her reading group has kept — her teacher confesses — her chair in the circle. The order recites the sequence that decided it: kin identified at intake; kin's own calls documented in the agency's notes; no completed kinship exploration before a move planned nine days in advance; an approved kinship home now available in the child's school district. The judge's phrasing for the county line is the one for the training manuals: the emergency justified a bed for a night; it did not justify a county for a childhood.",
    "The method generalizes, because cross-county moves are where kinship goes to be forgotten: the record request (55 Pa. Code § 3130.44(d)) is the only instrument that reconstructs who knew what in February; dates do the arguing — a memo predating the emergency converts 'no choice' into 'unchosen option'; and the kin resource, resubmitted in un-losable form and heard on her qualifications (§ 6336.1), must be made a person in the present tense, not a February intention in the file's. Interim relief mattered too: the November order kept the visits and the school thread alive, so December's order restored a life instead of excavating one.",
    "What no strategy controls: the bed map. Your county genuinely had no bed in October, and if Beatrice had failed her study — a record, a landlord, a daughter who moved away — the Riverton home would have been the right answer even on a perfect record. The strategy never promised Beatrice would pass. It promised she would be reached, studied, and answered in the open. In kinship work that promise, kept, is most of what 'family finding' is supposed to mean."]),
 E("end_bridge55", 38, "Ending — A Bridge, Not a Move (partial)",
   ["The court declines to move Zola mid-year: two school changes in five weeks, the judge rules, is its own harm — and instead builds the bridge with orders: Beatrice's approval finalized, Zola to spend weekends and school breaks at her aunt's, agency transport for your Wednesday visits restored, and the placement question relisted in ninety days with the kinship placement as the presumptive plan unless the agency shows cause. Zola keeps the Riverton foster mother she likes and gains back her aunt in writing, on a calendar.",
    "Partial endings in move cases are often built this way — stability now, kinship scheduled — and whether this one is wisdom or delay will be decided by the ninety days, not by today. What the record bought is that the delay is the court's considered choice rather than the file's default drift: the February notes, the October dates, and Beatrice's approval are now findings-adjacent, and a relisted hearing inherits them. Drift loses cases slowly; documented bridges mostly finish crossing.",
    "Walk the bridge deliberately: use every weekend, document every exchange, and let the ninety days produce the evidence the next order needs — a child thriving in both homes, with one of them hers by blood and law."]),
 E("end_fiftyminutes", 38, "Ending — Fifty Minutes",
   ["The move stands. The agency's necessity argument, unopposed by the February record, carries the day: an emergency, a licensed home, a kinship resource the file describes — still — as 'packet mailed, no response.' Beatrice, unstudied and unheard, remains a name in an intake form. Your visits remain fifty-five minutes away on the days the transport runs. Zola's chair in her old reading circle is given, in time, to another child.",
    "Everything that decided this was paper that existed and was never introduced. The call notes proving Beatrice's February persistence were in the agency's file the whole time — a parent's written record request (§ 3130.44(d)) is the mechanism that moves such pages from the agency's drawer to the court's bench. The October dates were in the file too. Cases like this are not lost because the truth is unavailable; they are lost because truth held by one side, unread by the other, functions as though it did not exist.",
    "The road from this ending is the scenario run in reverse and late: Beatrice's fresh submission (which no ruling here forecloses), the study, her right to be heard on her qualifications (§ 6336.1), and the next review — moves are revisited, and a completed kinship approval changes the question from 'should we explore' to 'why not yet.' Fifty minutes is a distance. It is not a verdict on your family, unless the file is allowed to make it one by default."]),
]

# ============================================================ S56 (Complex)
S = date(2026, 12, 7)
assert fmt(S) == "Monday, December 7, 2026"
NOTICE56 = date(2026, 12, 9)
assert fmt(NOTICE56) == "Wednesday, December 9, 2026"
DEADLINE56 = NOTICE56 + timedelta(days=90)
assert fmt(DEADLINE56) == "Tuesday, March 9, 2027"     # 90 days from the Dec 9 notice (23 Pa.C.S. § 6341(a)(2))
HEARING56 = S + timedelta(days=51)
assert fmt(HEARING56) == "Wednesday, January 27, 2027"
REVIEW56 = S + timedelta(days=95)
assert fmt(REVIEW56) == "Friday, March 12, 2027"

s56_meta = {
    "title": "The First 90 Days",
    "subtitle": "Scenario 56 — The Wrong Gregory (a fictional composite)",
    "startDateISO": "2026-12-07",
    "startNode": "start",
    "startCash": 260,
    "tier": "Complex",
    "summary": "You are Katya, in your fifth month of recovery. Your son Lev, four, is in foster care, and two paper walls stand between him and his uncle Gregory's home. The first is yours: an indicated report from the day Lev fell at the park — with a ninety-day appeal clock already running. The second is Gregory's: his kinship study is stalled by a record that belongs to a different man with his name. Two files, two corrections, one winter.",
}
s56 = [
 N("start", 0, "The letter and the stall",
   ["Two envelopes arrive in the same week, which is how you learn that trouble travels in convoys. The first is from Children and Youth: the report from the park — the afternoon Lev climbed too high and fell, the ambulance, the nine stitches — has been determined 'indicated,' naming you. You have ninety days from the notice to appeal it, or it becomes permanent: the appeal right and its clock are 23 Pa.C.S. § 6341(a)(2), and the notice, dated December 9th, starts a count that ends March 9th.",
    "The second envelope is worse-dressed and sadder: your brother Gregory, whose kinship study for Lev began in November, has been told his approval is 'on hold pending record clarification.' Gregory's record, to your certain knowledge, contains one speeding ticket. 'Record clarification' is doing something in that sentence, and it is not clarifying."],
   [C("Put both envelopes in the folder you now keep. Then sort the winter: your clock first (it is the one that expires), his stall second (it is the one that festers).", "sort_winter", addHidden=["indicated-clock"])]),
 N("sort_winter", 1, "Your clock",
   ["Your counsel — appointed under 42 Pa.C.S. § 6337 — reads the indicated notice the way she reads everything: twice, with the second reading aloud. \"Ninety days to request the appeal hearing, and here's what changed under Act 119: the appeal isn't you begging to be believed. At the hearing, the agency has to prove the report accurate by substantial evidence — that's § 6341(c.2)(5) — and before the hearing, you're entitled to the evidence the agency collected, including anything in it that helps you — (c.2)(4). If we win, the report is expunged and the county and the Department get ordered to fix their files.\"",
    "\"And if we file and wait?\" — \"The hearing gets scheduled; the report sits 'indicated' while it pends. Your recovery program, your job applications — the report is a fact about you in every database until a hearing officer says otherwise. We file this week. Early is free.\""],
   [C("File the appeal request now — the § 6341(a)(2) appeal, in writing, weeks inside the deadline.", "appeal_filed", setFlags=["appealFiled"], cash=-8)]),
 N("appeal_filed", 3, "Gregory's envelope",
   ["With your clock stopped from being an emergency, you turn to the stall. Gregory, thirty-five, a finish carpenter with a duplex and a workshop, shows you his letter and his humiliation in equal measure: the hold cites 'an indicated report (2011) appearing in the household clearance summary under the applicant's name.' In 2011 Gregory was twenty, working in Ohio, and — this is the part that matters — his name is shared, in full, by a cousin in another county neither of you has spoken to in a decade. A cousin whose middle initial is M. Gregory's is T.",
    "\"They asked if I had anything to tell them,\" he says. \"Like a confession was the form I was missing.\""],
   [C("Ask the agency, in writing, for the specific identifiers behind the hold: the full name, date of birth, and report number the summary relied on.", "identifiers_ask", setFlags=["identifiersAsked"])]),
 N("identifiers_ask", 6, "Identifiers",
   ["The agency's reply takes nine days and contains the confession the file owed him: the clearance summary lists 'Gregory M.,' a date of birth in a different year, and a report number from a different county — merged into Gregory T.'s summary, the worker writes, 'during data migration.' Two men, one name, and a database that treats a name as an identity. Gregory's study didn't stall on his history. It stalled on his cousin's, wearing his name like a borrowed coat.",
    "Ms. Barlow, the worker, is apologetic and precise about the fix: the summary must be corrected by the source, the clearances re-run under full identifiers, and the study resumed. Apologies do not correct databases, however. Written corrections, transmitted to every holder of the summary, do."],
   [C("Ask for the correction in writing, addressed to the file, with transmittal to every office that received the original summary.", "correction56", setFlags=["conflationDocumented"])]),
 N("correction56", 9, "Your own record, opened",
   ["There is a second reason to move now, and it belongs to your side of the winter: as Lev's mother and a party, you may request the case record in writing — 55 Pa. Code § 3130.44(d). Your request names two things: Lev's placement file (which contains Gregory's study and the tainted summary, where a second correction may be needed) and the park investigation file underlying your indicated report — the evidence (c.2)(4) entitles you to see, including whatever the agency collected that cuts your way.",
    "One signature, two files, both corrections. Requests are cheap. Winters are long."],
   [C("File the § 3130.44(d) request covering both files.", "records56", setFlags=["recordsRequested"], addHidden=["record-request"], cash=-9)]),
 N("records56", 14, "What the investigation file holds",
   ["The investigation file arrives in January, and reading it is the strangest hour of your recovery: your worst afternoon, documented by strangers. It holds the worker's narrative (the fall, the ambulance, 'mother appeared distressed and distracted'), the hospital note (nine stitches, 'no other injuries; child calm; mother appropriate at bedside'), and — on page eleven, collected by the agency and never mentioned in its summary — a signed statement from the parks department attendant.",
    "The attendant's statement says the things you have been saying since November into rooms that wrote down only some of them: you were twenty feet away, helping your elderly neighbor who had fallen on the path; Lev was on the age-appropriate structure; the attendant himself was the adult nearest the structure; and the fall 'could have happened with any parent present.' The agency had this the whole time. Under (c.2)(4), its evidence — all of it, including the parts that help you — is now yours to use."],
   [C("Give page eleven to your counsel with both hands. \"This was in their file since November.\"", "page_eleven", setFlags=["exculpatoryFound"])]),
 N("page_eleven", 17, "Gregory's correction, traveling",
   ["While your appeal strengthens, Gregory's correction does its slow paperwork: the corrected summary issues with his full identifiers; his clearances re-run clean under his own date of birth; the study resumes — home visit repeated (the first one, absurdly, must be redone because its paperwork references the wrong file number), references re-called. Gregory endures the rerun with a carpenter's philosophy: 'Measure twice. They measured the wrong man once.'",
    "His part of the winter is now a schedule instead of a mystery: study completion estimated mid-February. Yours is a hearing: January 27th."],
   [C("Prepare the hearing with your counsel: the attendant subpoenaed if needed, the hospital note, your program's attendance record — and the burden where it belongs: on the agency, by substantial evidence (c.2)(5).", "hearing_prep56", setFlags=["hearingReady"])]),
 N("hearing_prep56", 21, "Preparation",
   ["Your counsel's preparation has a notable shape: she spends less time on you than on the agency's proof. \"Under Act 119, they carry it. Our job is to make them carry it in the open: their narrative says 'distracted.' Their own file says twenty feet, a fallen neighbor, an attendant present, age-appropriate equipment. Substantial evidence is not a mountain — but it is more than an adjective. When their case is a summary of their file and our case is their file, hearing officers can count.\"",
    "Your program counselor provides the attendance record: five months, one absence (the ambulance day does not count, and the record says why). Recovery is not the subject of this hearing. It is, all the same, the room the hearing happens in."],
   [C("January 27th. Bring the file. Bring Gregory — he is not a witness in your appeal, but his presence is a fact about Lev's options, and hearing officers notice families.", "hearing56")]),
 N("hearing56", 51, "The appeal hearing",
   ["The hearing is administrative — a hearing officer, a table, a record made by a stenographer — and it is decided on exactly the evidence Act 119 prescribes. The agency presents its narrative and its worker, who is honest under oath-adjacent pressure: yes, the attendant's statement was collected; no, it wasn't in her summary because 'the summary focused on the mother's position.' The attendant, subpoenaed, repeats page eleven in person. The hospital note is stipulated.",
    "Your counsel closes in one paragraph: the agency must prove the report accurate by substantial evidence; its own collected evidence describes a supervised child, a momentarily diverted mother rendering aid to a fallen elderly woman, and an accident on appropriate equipment. 'Distracted,' the adjective, is asked to carry a finding. It cannot."],
   [C("The decision does not come from the bench. It will come by mail, within the time the statute allows — up to 45 days under § 6341(c.3). Wait, and work Gregory's track.", "the_wait56")]),
 N("the_wait56", 58, "The wait, used",
   ["February is study season: Gregory's re-run home visit (a worker who apologizes to his empty rooms for the delay), his references — a pastor, two clients, your mother by phone from Arizona — and his safety plan for a four-year-old, which includes, on the advice of no one, a workshop lock and a gate at the top of the stairs that he built in an afternoon because waiting is easier with sawdust.",
    "The study completes February 18th: approved, without conditions, under his own name and identifiers, with the corrected summary stapled in front of the wrong one so the file remembers its own error. Lev's placement review is set for March 12th. Your appeal decision is somewhere in the mail's weather."],
   [C("Ask the agency to confirm Gregory's approval and the March 12th review in writing — the winter has taught everyone what writing is for.", "confirm56", setFlags=["gregoryApproved"], cash=-6)]),
 N("confirm56", 66, "March approaches",
   ["The confirmation letter arrives. The decision letter — yours — does not, yet. " + fmt(DEADLINE56) + " was your filing deadline, met in December; the decision runs on (c.3)'s clock, not yours, and hearing decisions in these appeals arrive when they arrive, up to the statutory outside limit. Your counsel files nothing and calls once, for the record, to confirm the decision is pending issuance.",
    "On March 5th, two envelopes from Harrisburg are in your mailbox. You open them in the car, because some letters cannot wait for a kitchen."],
   [C("Open them.", "decision56")]),
 N("decision56", 88, "The decision",
   ["The hearing officer's decision is eleven pages and it reads the agency's file back to it: the attendant's statement, the hospital note, the stipulated facts — and the conclusion the arithmetic required. What the decision orders is the last piece of the winter. What Gregory's approval already settled is the other. The March 12th review will assemble them, one way or another."],
   [C("Read the operative paragraph. Then call Gregory.", "outcome56")]),
 N("outcome56", 95, "March 12th — the review",
   ["The courtroom has both files in it now — yours, decided; Gregory's, corrected — and a four-year-old's address is, as always, the only question actually on the table. Ms. Barlow presents the agency's recommendation. Your counsel presents the winter. The judge reads the decision's operative paragraph one more time before ruling."],
   [C("Hear the ruling.", "final_gate56")]),
 N("final_gate56", 95, "Two files",
   ["Everything the winter built is in this room: a timely appeal, an expunged — or upheld — report; a corrected identity; an approved uncle. The ruling is assembled from whichever of those actually happened."],
   [C("The report is expunged on the agency's own evidence, and Gregory — the right Gregory — is approved: placement with his uncle.", "end_bothfiles", requiresFlags=["appealFiled", "exculpatoryFound", "gregoryApproved"]),
    C("Gregory is approved and Lev is placed with him — but the report stands, and it will follow Katya into every background check until it ages or is revisited.", "end_onefile"),
    C("The report stands, and the study — uncorrected or unfinished — means Lev waits in foster care for the next review.", "end_upheldwaiting")]),
 E("end_bothfiles", 95, "Ending — Both Files, Corrected",
   ["The report is expunged — the hearing officer finds the agency did not carry its burden of proving it accurate by substantial evidence, its own attendant's statement outweighing its summary's adjective — and the orders go out as § 6341(c.3) provides: the report expunged, the county agency and the Department directed to amend their records. At the review, Lev is placed with Gregory T. — the uncle whose own name was restored to him in writing in January, whose study was completed under his own identifiers, and whose gate-at-the-stairs craftsmanship is noted in the approval without official comment on its quality, which is high.",
    "Two disciplines won this winter, and both are paper disciplines. On your side: the appeal was filed inside the 90-day clock (§ 6341(a)(2)) — early, in December, because early is free — and then Act 119's architecture did the work: the agency's burden (c.2)(5), and its duty that the evidence it collected, including what helped you, be available (c.2)(4). The attendant's statement existed since November. The appeal is what made the agency answer for ignoring it. On Gregory's side: an identity error is corrected the way it was made — in writing, at the source, transmitted to every holder of the wrong summary — with identifiers demanded before arguments were offered. 'The wrong man' is not a defense you plead. It is a fact you document until the database agrees.",
    "What no strategy controls: the hearing officer. Another officer, on the same record, could have found the narrative sufficient; Act 119's burden shift raises the floor, it does not appoint the judge. And Gregory's cousin's actual record was the winter's dark luck — had the conflated report been Gregory's own, the study's question would have been real, and this ending unavailable. The strategy's claim is narrower and complete: both files now say what is true. Courts can work with true files. Families can build on them. It is the false ones — unappealed, uncorrected, unexamined — that quietly decide addresses."]),
 E("end_onefile", 102, "Ending — One File Corrected (partial)",
   ["Lev goes to Gregory's — the identity correction held, the study approved the right man, and placement follows. But the indicated report stands: the hearing officer found the agency's proof sufficient, or the evidence landed differently than the file promised. Katya leaves the courthouse simultaneously a mother whose son is with family and a woman whose name sits in ChildLine as indicated — with consequences she will meet at job applications and program paperwork for years, blunted only partly by the knowledge that the report ages and that further review rights exist and are time-limited, as the decision letter itself will state.",
    "Hold the two facts apart, because the system won't: the kinship track and the appeal track are separate files with separate burdens, and winning one does not launder the other. Gregory's correction was total because it was provable — identifiers are arithmetic. Katya's appeal was a judgment call because supervision is a judgment — and judgment calls, by design, sometimes land on the family. The record built here (the attendant's statement, the hospital note, the stipulations) is preserved in the hearing record; it is the foundation any further review stands on, and it did not exist until the appeal forced the file open.",
    "This is a partial win with a long shadow, and the guide names it plainly: Lev is home with family, which is the outcome childhood is measured in; and the report is a debt Katya will pay in installments of explanation. Both are true. The winter's work made one of them true. The other is the reason the next family should file in December too — the clock is the same, and sometimes the officer is different."]),
 E("end_upheldwaiting", 102, "Ending — Upheld and Waiting",
   ["The report is upheld, and Gregory's study — its correction still traveling, or its re-run still queued at the review date — is not ready to carry a placement. Lev stays in his foster home, kindly kept and officially temporary, and the next review is a season away. Katya walks out with two files that both, in different ways, say 'not yet' about people they do not describe accurately — one by judgment, one by clerical gravity.",
    "The post-mortem is the scenario: every mechanism that fixes these files is time-shaped. The appeal clock (§ 6341(a)(2)) ran from December 9th whether or not anyone felt ready; identity corrections move at the speed of the offices that made the error; studies re-run at queue speed. What beats the shapes is starting inside them early — appeal filed in the first weeks, identifiers demanded in the first letter, the record request (§ 3130.44(d)) filed while the tracks were still warm. None of that guarantees outcomes. All of it guarantees that the system's delays are spent on your case's real questions instead of its clerical ones.",
    "From here: the correction, once landed, reopens Gregory's study on a court's impatience rather than an agency's queue, and the next review reads a different file. Winters end. The discipline is to make sure yours ends because the paper became true — not merely because the season changed."]),
]

# ============================================================ EXPANSIONS
# Inserted beats: rewire a predecessor's choice to the first inserted node,
# chain the inserted nodes, land on the original target. List order and
# dayOffsets stay non-decreasing; the validator re-walks every graph.
def _idx(lst, nid):
    for i, nd in enumerate(lst):
        if nd["id"] == nid:
            return i
    raise KeyError(nid)

def ins(lst, after, *news):
    i = _idx(lst, after)
    lst[i + 1:i + 1] = list(news)

def rw(lst, nid, old, new):
    nd = lst[_idx(lst, nid)]
    hit = False
    for c in nd["choices"]:
        if c["next"] == old:
            c["next"] = new
            hit = True
    if not hit:
        # Authoring redundancy: the node may already point at the new target.
        assert any(c["next"] == new for c in nd["choices"]), (nid, old, new)

# ---- S48 (+5 -> 18)
ins(s48, "tell_in_writing",
    N("phone_interview", 4, "The phone interview",
      ["Mr. Solberg calls Walter the next afternoon, and you listen on the extension your father insists on holding six inches from his ear. The worker asks about the house, the heart, the spare room, and Hugo — in that order, which Walter later reports with approval: 'He asked about the boy last and longest.'",
       "At the end, Mr. Solberg says the sentence that separates a study from a rumor: 'I'm going to send you the requirements list. Everything on it. At once.'"],
      [C("Thank him, and tell your father to clear the kitchen table. Paper is coming.", "the_list")]))
rw(s48, "tell_in_writing", "the_list", "phone_interview")
ins(s48, "clearances",
    N("program_letter", 10, "Your side of the file",
      ["A kinship study examines the caregiver. Your case examines you. Your program counselor's letter — attendance, phase progress, a drug screen history as clean as the program keeps — goes into the same review packet, because a judge deciding whether Hugo moves to his grandfather is also, always, deciding how this story is trending.",
       "You are not the placement. You are the reason the placement is a bridge instead of a destination. The letter says so in a counselor's flat, credible prose."],
      [C("Ask Mr. Solberg for the study checklist anyway — and put in your own written request for the case record under 55 Pa. Code § 3130.44(d), so the study's paper reaches you too.", "checklist", setFlags=["recordsRequested"], addHidden=["record-request"])]))
rw(s48, "clearances", "checklist", "program_letter")
ins(s48, "home_visit",
    N("hugo_visit", 18, "Hugo, inspecting",
      ["The agency arranges Hugo's next visit at Walter's house — part visit, part quiet evidence. Hugo inspects the spare room with the seriousness of a building department: the bed, the shelf, the model bus at eye level. He tests the handrail twice, like a man who has seen a worker do it.",
       "On the porch he asks his grandfather whether the school bus that stops at the corner is 'his bus.' It is the right route for Hugo's same school — a fact you confirm with the district that week, in writing, because school continuity is a sentence judges underline."],
      [C("Confirm it in writing: same school, same route, stop at the corner.", "before_review", setFlags=["schoolConfirmed"])]))
rw(s48, "home_visit", "before_review", "hugo_visit")
ins(s48, "before_review",
    N("voss_call", 21, "Mrs. Delacroix calls",
      ["Mrs. Delacroix — Hugo's foster mother — calls you the week before the review, which foster parents are not required to do and the good ones do anyway. 'He talks about the room,' she says. 'If the court moves him, we'll pack his things properly and I'll send the bus shelf photo with him. I wanted you to hear that from me.'",
       "Foster parents receive notice of hearings and may be heard at them (42 Pa.C.S. § 6336.1). What Mrs. Delacroix will say, if asked, is that Hugo is ready and the grandfather is real. Support like that cannot be bought or faked — but it can be welcomed, in writing, so it reaches the file."],
      [C("Thank her in a letter the agency gets a copy of. Bridges get built from both banks.", "walter_letter")]))
rw(s48, "before_review", "the_review", "voss_call")
ins(s48, "voss_call",
    N("walter_letter", 22, "Walter's page",
      ["Walter writes his own statement for the court, one page, in handwriting like a route manifest: the house, the heart ('managed, see doctor's letter'), the room, the years he has known his grandson, and the last line, which he reads to you twice to make sure it is spelled right: 'I am not a backup plan. I am his grandfather.'",
       "It is not a legal document. Courts are moved by legal documents that have a pulse. Your own statement is already filed; his will sit beside it, and the pair of them say what the study alone cannot: this placement has two generations asking for it."],
      [C("File his page with yours. Then sleep. Tomorrow is paperwork's last mile.", "the_review")]))
ins(s48, "the_review",
    N("the_drive", 24, "The drive to court",
      ["Walter drives, because Walter always drives, and parks with the care of a man for whom parking was once a profession. In the courthouse hallway, Hugo's file goes past on a cart — two inches thick already, for a nine-year-old who has done nothing but be loved in inconvenient circumstances.",
       "Everything the spring built is in those two inches: your letter, his list, the lockbox receipt, the fax that was found. The judge is about to read the last page first, the way judges do. The last page is the recommendation."],
      [C("Take your seat.", "outcome")]))
rw(s48, "the_review", "outcome", "the_drive")

# ---- S49 (+11 -> 28)
ins(s49, "letter_full",
    N("hearing49", 3, "Thursday — shelter care",
      ["The shelter care hearing is short and mostly about custody, not addresses: the judge confirms the emergency, continues the children in care, and sets the review for March 19th. But because Odette's letter is already in the file, your counsel gets one sentence into the record that will matter in March: 'A kinship resource, the children's great-aunt, has been identified in writing; the agency is directed to proceed with her study.'",
       "Directed. On the record. Studies that are directed finish on schedules; studies that are merely 'in process' finish on sympathies."],
      [C("Leave with the order's sentence copied into your notebook. It is the study's leash.", "the_study")]))
rw(s49, "letter_full", "the_study", "hearing49")
rw(s49, "letter_short", "the_study", "hearing49")
ins(s49, "the_study",
    N("odettes_house", 6, "The third floor",
      ["The study's logistics come to Odette's kitchen table: her clearances are filed; the home visit is set; and Tomas — home for the weekend — sits for his part without being asked twice. Ms. Moreau explains what his fingerprints are for with a directness he respects: 'The study has to describe the whole house. You're part of the house. That's the whole speech.'",
       "'First honest form I've ever been on,' Tomas says, and rolls his thumb in the ink."],
      [C("His appointment is kept, his prints taken, his name spelled right on every form — the unglamorous liturgy of a household with nothing to hide.", "micah_tooth")]))
rw(s49, "the_study", "certificate", "odettes_house")
rw(s49, "the_study", "certificate_slow", "odettes_house")
ins(s49, "odettes_house",
    N("micah_tooth", 7, "A tooth, at the right address",
      ["Sunday visits at Odette's begin — the agency's practical bridge while the study runs — and on the second Sunday Micah loses a tooth at her table, in a meatball, with ceremony. Odette produces an envelope, writes 'MICAH — FIRST TOOTH — HER HOUSE' on it in pencil, and puts it in the drawer where she keeps the family's important papers, between the deed and a baptismal certificate.",
       "Children file their own evidence. By March, that drawer will hold the argument this case is really about. On the drive back, the one remaining errand from the study list surfaces — the death certificate for the background flag — and it is yours to chase or to leave to channels."],
      [C("Get the certificate yourself — county office, same week, fee paid — and hand-deliver a copy to the agency with a receipt.", "certificate", cash=-18, setFlags=["paperChased"]),
       C("Let the agency request it through channels. It is their study; the flag is their paperwork.", "certificate_slow")]))
ins(s49, "sibling_visits",
    N("kira_call", 15, "Kira's call",
      ["Kira calls from her foster home on a Tuesday, on the phone the foster mother holds and then, kindly, leaves the room for. 'Micah's tooth came out at Aunt Odette's,' she reports, with the grievance of a bureau chief whose branch offices act without her. 'I keep the chain. He keeps the teeth. Tell them at the meeting I want the Saturdays at her house. Both of us. Together.'",
       "A ten-year-old has just dictated a placement preference with more administrative clarity than most case plans contain. You write it down in her words."],
      [C("Her words go to Ms. Moreau in writing the next day — the children's stated wishes, filed by the person who heard them.", "weekend_visit", addHidden=["child-voice"])]))
rw(s49, "sibling_visits", "tomas_check", "kira_call")
ins(s49, "kira_call",
    N("weekend_visit", 17, "A whole Saturday",
      ["The first full Saturday at Odette's runs on her rules: pancakes in shifts, the blue room inspected by Kira and claimed with a hair ribbon on the doorknob, Tomas arriving at noon with hoagies and leaving the children the run of the porch. Ms. Moreau's visit note — you will read it later, in the record — is two lines long and both are gold: 'Children relaxed. Sibling interaction continuous and unforced.'",
       "The file is learning what the family already knew. The study's last open item is Tomas's history, which the county's answer on his fingerprints will frame one way or another."],
      [C("The answer comes back exactly as disclosed. Be in the room when Odette is asked about it.", "tomas_check")]))
rw(s49, "kira_call", "tomas_check", "weekend_visit")
ins(s49, "tomas_check",
    N("tomas_job", 20, "Tomas, documented",
      ["The study's final folder is Tomas-shaped: his employer's letter (six years on the same shift), his lease across town (proving the weekends are weekends, not residence), his fingerprint results, and the dismissed-charge disposition from the other county — obtained by you, at the clerk's window, for eleven dollars, because paper chased is paper arrived.",
       "Assembled, it reads the way honest households read: layered, dated, and slightly boring. Boring is what truth looks like in a kinship file."],
      [C("Ask Ms. Moreau what remains before the March review — and get the answer as a list.", "the_list2")]))
rw(s49, "tomas_check", "the_list2", "tomas_job")
ins(s49, "the_list2",
    N("foster_moms", 24, "Two foster mothers",
      ["Both foster mothers will be heard at the review if they wish — notice and the right to be heard are theirs under 42 Pa.C.S. § 6336.1 — and Ms. Moreau, doing the rounds, reports their positions honestly: Kira's foster mother supports the move ('She's packed twice already, in her head'). Micah's is torn in the open: bonded to a six-year-old who has been hers since the fire, and unwilling to pretend otherwise — but she has met Odette, and what she asks the court for is a transition, not a veto.",
       "Opposition would have been simpler. This is better: a case where every adult is telling the truth, and the court gets to decide on placements instead of on credibility."],
      [C("Thank both of them, through the agency, in writing. Truth-telling adults are this case's infrastructure.", "deshawn_plan")]))
rw(s49, "the_list2", "records49", "foster_moms")
ins(s49, "foster_moms",
    N("deshawn_plan", 25, "Your own address",
      ["Your side of the file moves too: the red-tagged apartment is settled with the landlord, your cousin's couch has an end date, and a lease on a two-bedroom — two bedrooms, chosen with a caseworker's eye — is signed for April, contingent on the review. Your counsel will present it as context, not argument: the kinship placement is the bridge; your housing is the far shore being built on schedule.",
       "Cases are never only about the question on the docket. Judges read trajectories. Yours, this month, points one way."],
      [C("File the lease copy with your review papers. Then get the record you requested weeks ago.", "records49")]))
rw(s49, "foster_moms", "records49", "deshawn_plan")
ins(s49, "records49",
    N("review_prep49", 28, "The packet",
      ["Ms. Fontaine assembles the review packet on her conference table, and it has a spine: the first letter (whole household, day one), the hearing order directing the study, the study itself, the Saturday visit notes, Kira's dictated sentence, the foster mothers' positions, your lease. 'Cases like this are won in the passive voice,' she says. 'Everything already happened. The judge just gets to agree with the record.'",
       "The agency's filing is due Thursday. Ms. Moreau has been straight with you for six weeks, and her report will say what her file says. The question is what her supervisor's recommendation line says underneath it."],
      [C("Sleep on the packet. Tomorrow the agency files; the day after, you answer if you must.", "continuance_scare")]))
rw(s49, "records49", "the_review49", "review_prep49")
ins(s49, "review_prep49",
    N("continuance_scare", 29, "The scare",
      ["The agency's filing requests a thirty-day continuance — 'to complete supervisory review of the kinship study' — and for one evening the packet feels like a sandcastle at tide. Ms. Fontaine opposes in writing the same day: the study is complete, the children are split, the statute's clock does not recognize supervisory weather. The court denies the continuance on the papers, in a two-line order that Ms. Fontaine reads to you twice.",
       "March 19th stands. Systems request delay the way water finds downhill; opposed, in writing, on a complete record, delay sometimes loses."],
      [C("March 19th. Iron something. Odette already has.", "the_review49")]))
rw(s49, "review_prep49", "the_review49", "continuance_scare")
ins(s49, "the_review49",
    N("night_before49", 31, "The night before",
      ["Odette lays out the children's rooms for nobody — they are not moving tomorrow whatever happens; tomorrow is only the order — and then lays them out again, because hands need work on the night before a judge decides where a family lives. Tomas calls from his apartment: 'Tell the part about the tooth drawer.'",
       "'They'll read the visits,' you tell him. 'The drawer is in the visits.' It is, too — two lines, gold, in the record you requested and read."],
      [C("Walk in with the record already read. It changes how a courtroom sounds.", "outcome49")]))
rw(s49, "the_review49", "outcome49", "night_before49")

# ---- S50 (+13 -> 28)
ins(s50, "exact_words",
    N("school_call", 1, "The school hadn't been told either",
      ["You call Ruben's school from the visitation center parking lot. His counselor's silence, when you explain, is the professional version of outrage: the school has heard nothing about a move — not from the agency, not from anyone — about a child whose Individualized reading plan she personally rebuilt in February.",
       "'If there's a hearing,' she says, 'the school will write. We've documented his year. Somebody should have to read it before they move him.' Somebody should. Making that somebody a judge is a filing away."],
      [C("Call Ms. Marchetti tonight anyway — now with a school that will write.", "call_lawyer50", addHidden=["school-stability"])]))
rw(s50, "exact_words", "call_lawyer50", "school_call")
ins(s50, "file_both",
    N("first_letter_back", 2, "Noted",
      ["The agency's acknowledgment of your filings arrives in three days, and it contains a sentence worth the postage: 'Mother was advised of placement planning during contact on May 1st.' You were not — May 1st was a fifteen-minute phone call about a dentist appointment, and your notebook, kept since February on counsel's advice, says so in ink dated that day.",
       "Contemporaneous notes are the poor family's subpoena. You send Ms. Marchetti the page. A file that claims you were told things you weren't is a file whose other claims now need checking — which is what record requests are for."],
      [C("Add the page to the hearing packet list. Paper answers paper.", "march30")]))
rw(s50, "file_both", "march30", "first_letter_back")
ins(s50, "march30",
    N("ruben_weekend", 4, "The weekend visit",
      ["At Saturday's visit Ruben asks the questions eleven-year-olds ask when adults' plans leak: Will the new house have a yard? Will Mrs. Renaud visit him, or is it the kind of goodbye where people say that? Can a kid finish a school year by mail? You answer the ones you can and write down the rest, because his questions are the hearing's agenda in his own syntax.",
       "'Tell the judge the fort thing,' he instructs. 'And the desk thing. Those are my two exhibits.'"],
      [C("'Exhibits A and B,' you promise. 'Filed under F, for fort.'", "kessler_speaks")]))
rw(s50, "march30", "kessler_speaks", "ruben_weekend")
ins(s50, "kessler_speaks",
    N("wexler_call", 5, "The worker, honestly",
      ["Mr. Wexler, the agency worker, calls about visit scheduling and stays on the line a moment too long — the way people do when their file and their opinion have separated. 'The new home is a good home,' he says. 'I want that in your hearing, because it's true. It's also fifty minutes away and I wrote 'parent to be notified' in a memo like that was a plan. That's in the file too, or it will be when your request lands.'",
       "Workers are not the enemy in this scenario; the calendar is. A worker who tells you the truth about his own file is giving you the map of the hearing."],
      [C("Thank him. Write it down. Then make the call to Anita — the file needs its alternative by name.", "anita_call")]))
rw(s50, "kessler_speaks", "anita_call", "wexler_call")
ins(s50, "anita_call",
    N("anita_house", 7, "Two streets from the school",
      ["Anita's house, which you have eaten in a hundred times, becomes a document the moment you walk it with study eyes: the spare room with the door that closes, the yard, the school visible — actually visible — from her porch steps, two bus stops Ruben already knows by their graffiti. She walks it with you, narrating like a woman reading her own deposition: 'His room. His school. His godmother. I don't know what else a study wants, so get me the list and I'll become it.'",
       "The list, when she files, will have a house like this behind it."],
      [C("She files Friday. You turn to the clock: her clearances, her study visit, your hearing — three races, one date.", "anita_files")]))
rw(s50, "anita_call", "anita_files", "anita_house")
ins(s50, "anita_files",
    N("clearance_wait", 9, "Clearance weather",
      ["Anita's clearances enter the particular purgatory of state databases, where everything is 'processing' until it is suddenly 'received.' You call twice; Anita calls once, with her confirmation numbers memorized like a psalm. The trick you have learned from every prior month of this case: nobody's paper is done until a person has said the word 'received' out loud and you have written down who said it.",
       "On the ninth day, a person says it. The study visit is scheduled. The race has a second lap and Anita is running it in house slippers, at speed."],
      [C("While her paper travels, yours arrives: the record you requested, with the April memo inside it.", "read_fully")]))
rw(s50, "anita_files", "read_fully", "clearance_wait")
ins(s50, "read_fully",
    N("record_second", 10, "The second installment",
      ["The record's second installment — supervisor emails, produced after Ms. Marchetti's follow-up letter — shows the move's internal life: the 'notify parent' task created April 2nd, reassigned April 14th, reassigned again April 27th, each reassignment resetting its due date like a snoozed alarm. Nobody refused to tell you. The telling was a task, and tasks without owners become weather.",
       "Your lawyer tabs the thread in yellow. 'Judges understand alarms,' she says. 'Everyone in that courtroom has snoozed one. The question is whether a child's address should ride on one.'"],
      [C("Build the packet with her — memo, alarm thread, school, clinician, kin. In that order.", "therapist_call")]))
rw(s50, "read_fully", "packet50", "record_second")
ins(s50, "record_second",
    N("therapist_call", 11, "The clinician, in writing",
      ["Ruben's therapist, reached by phone, agrees to put her March note's recommendation in a letter addressed to the court: minimize transitions; the attachment to Mrs. Renaud and to the school routine is the treatment's current foundation; a mid-year cross-county move 'would be expected to cost measurable progress.' She is careful, clinical, and devastating — the holy trinity of expert paper.",
       "'I'll write what I'd write for any child,' she says. 'He just happens to be a child whose file will actually get read.' She has understood the scenario perfectly."],
      [C("Her letter goes in the packet behind the school's. One exhibit remains to build: the map.", "bus_route_map")]))
rw(s50, "record_second", "packet50", "therapist_call")
ins(s50, "therapist_call",
    N("bus_route_map", 12, "Exhibit: geography",
      ["The packet's last exhibit is a child's geography, drawn to scale by your lawyer's paralegal and checked by you on actual buses: current home to school, eleven minutes; Anita's street to school, two stops; the proposed home to your apartment, fifty minutes on a good day, with the visit route crossing two transfer points an eleven-year-old would navigate in no one's plan but a memo's.",
       "Courts say 'best interest' and mean, in part, distance measured in a child's mornings. The map says it without adjectives."],
      [C("Eleven pages, one map, one argument. The packet is done — the agency asks to meet before the hearing.", "packet50")]))
rw(s50, "therapist_call", "packet50", "bus_route_map")
ins(s50, "packet50",
    N("agency_meeting", 14, "The offered compromise",
      ["The supervisor's offer, made across a conference table with the wary courtesy of people who have read each other's filings, is real: Ruben finishes the school year with Mrs. Renaud on an extended arrangement, then moves to the new home in July with transition visits — 'everything except the kinship piece, which isn't ours to rush.' It is the agency conceding the calendar and defending the destination.",
       "Ms. Marchetti's advice is one line: 'A compromise you accept in a hallway, you can't appeal in a courtroom. The hearing is in three days and your packet is better than their offer. Decline — in writing, gratefully, and on the record.'"],
      [C("Decline in writing, with thanks and reasons. The hearing decides.", "kessler_letter", setFlags=["compromiseDeclined"])]))
rw(s50, "packet50", "the_hearing50", "agency_meeting")
ins(s50, "agency_meeting",
    N("kessler_letter", 15, "Mrs. Renaud's letter",
      ["Mrs. Renaud's written statement arrives by email the night before the hearing, printed by you at the library because some documents deserve paper: six months of Ruben — his reading, his fort, his nightmares' slow retreat — and her professional opinion, offered as the foster parent the statute notices and hears (§ 6336.1), that 'a move now, to strangers, in another county, is the one option on the table that serves adults' logistics only.'",
       "She closes with the sentence that will be quoted back in the courtroom: 'He asked me if he could finish the school year. I am asking for him, since his asking wasn't entered anywhere.'"],
      [C("Add her letter as the packet's final exhibit. Then prepare — tomorrow, the hearing reads what the spring wrote.", "night_before50")]))
rw(s50, "agency_meeting", "the_hearing50", "kessler_letter")
ins(s50, "kessler_letter",
    N("night_before50", 16, "The night before",
      ["Ruben, at the last visit before the hearing, gives you a drawing for the judge: a house, a school, and a road between them so short the crayons overlap. 'That's the whole case,' he says, with a litigator's economy. 'You can keep the drawing after. Judges have enough papers.'",
       "Ms. Marchetti, reviewing the witness order, saves Anita for near the end: 'The agency opens with necessity. We answer with the record. And then the court hears the alternative — a person, in the room, with a house two streets from the school. Sequence is an argument too.'"],
      [C("Tomorrow the alternative gets interviewed, studied, and heard — in that order, at speed.", "anita_interview")]))
rw(s50, "kessler_letter", "the_hearing50", "night_before50")
ins(s50, "night_before50",
    N("anita_interview", 17, "Anita, interviewed",
      ["The morning of the hearing, the agency completes its expedited study interview with Anita — a scheduling accident your lawyer converts into an exhibit, by having the worker's one-page summary filed before noon: home suitable, clearances received, school proximity noted, 'applicant highly motivated; relationship to child longstanding.' The study that 'isn't ours to rush' has been rushed, by the hearing's gravity, into existence.",
       "Anita arrives at the courthouse with her folder and her godson's drawing, which she has been deputized to carry. 'Exhibit F,' she says. 'For fort.'"],
      [C("Go in. The packet, the map, the letter, the study, and Exhibit F.", "the_hearing50")]))
rw(s50, "night_before50", "the_hearing50", "anita_interview")

# ---- S51 (+14 -> 28)
ins(s51, "start",
    N("denial_anatomy", 0, "Reading it with Petra",
      ["Your daughter Petra reads the denial over your shoulder and finds the first error before you do — she points at 'additional adults residing in the home' and laughs once, without humor. 'I'm an “additional adult” in my own apartment. Mom. We have a lease. We have a meter. The mailman knows we're separate even if the county doesn't.'",
       "That is the denial's anatomy in one sentence: it describes a house assembled from fragments — a downstairs glimpsed, an attic unentered, a household merged by assumption. Your task is not to be offended by the fragments. It is to replace them, item by item, with documents."],
      [C("Start the way the correction will have to proceed: a written request for the findings behind each reason.", "request_findings")]))
rw(s51, "start", "request_findings", "denial_anatomy")
ins(s51, "request_findings",
    N("felix_visit", 3, "The visit",
      ["Benny, at Thursday's visit, has one question, asked into your shoulder so the room won't hear it: 'Is the attic room still mine?' He has never slept in it. He claimed it in June of last year, at a birthday, with the absolute property law of eight-year-olds, and the claim has survived a foster placement, two schools' worth of Tuesdays, and everything since.",
       "You answer with the discipline this case will require everywhere: 'It's still your room. The grown-ups are doing paperwork about it, and I am not going to promise you a date I don't control.' He nods like a small judge. Children can tell the difference between a promise and a forecast, and they grade adults on the difference forever."],
      [C("Carry that standard back to the paperwork: forecasts get dates, claims get documents.", "attic_history")]))
rw(s51, "request_findings", "read_summary", "felix_visit")
ins(s51, "felix_visit",
    N("attic_history", 5, "The attic's biography",
      ["The attic has a biography, and it is all paper: converted in 2019 when your brother-in-law finished it — insulation, heat run, the egress window a permit required; your nephew's room for two summers; storage for one winter when Silvia's life narrowed; Benny's claimed territory since last June. The receipts live in a coffee tin in the kitchen, because your family keeps its archives the way it keeps everything: unsorted, complete, and defended by memory.",
       "You sort the tin on the kitchen table. Egress window: receipted, 2019. Heat run: invoiced, 2019. The room's whole defense is in this tin, waiting to become a packet."],
      [C("Tin sorted, dates in order. Now the study summary arrives — read it against the tin.", "read_summary")]))
rw(s51, "felix_visit", "read_summary", "attic_history")
ins(s51, "read_summary",
    N("marta_talk", 9, "Petra's household, volunteering",
      ["Petra and her partner make the decision that turns an argument into a rout: although their household is separate — separate lease, separate meter, separate entrance — they will provide clearances anyway, and open their door to the study too. 'If the county wants to count us,' Petra says, 'let it count us with our clearances in. Then there's nothing left to be “unclear” about.'",
       "It is the household version of a principle this whole batch runs on: a disclosed complication is a task; an undisclosed one is a finding. Petra's family just volunteered to be a task, twice-documented."],
      [C("Their clearances go in with the correction packet — alongside the lease and meter bill that prove they never needed to.", "correction_packet")]))
rw(s51, "read_summary", "correction_packet", "marta_talk")
ins(s51, "correction_packet",
    N("measurements", 13, "A tape measure, dated",
      ["You measure the attic the way the study should have: length, width, ceiling height at the slope, the egress window's dimensions against the code the permit cited — photographing each measurement with that day's newspaper in frame, a trick your brother-in-law learned from insurance adjusters. The photos are ugly and unimpeachable, which is the aesthetic of evidence.",
       "The packet is complete: lease, meter bill, egress receipt, measurements, floor plan, Petra's clearances. One signature is still missing, and it belongs to the only person who can open Benny's file — his mother."],
      [C("Call Silvia. The packet needs her signature on the record request, and fifteen monitored minutes to explain why.", "call_lucia")]))
rw(s51, "correction_packet", "call_lucia", "measurements")
ins(s51, "call_lucia",
    N("the_drive51", 15, "The signature, in person",
      ["The facility allows document visits for legal paperwork, and you drive the three counties with the request in a folder on the passenger seat like a relative. Silvia reads it twice — the program has taught her to read everything twice — and signs with a hand that only shakes on the second page.",
       "'Tell Benny the attic paperwork is moving,' she says. 'Don't tell him a date. You taught me that.' She has learned the family's new liturgy in the hardest classroom there is."],
      [C("Two envelopes leave the facility with you: her signed record request, and your packet, ready to follow it.", "two_envelopes")]))
rw(s51, "call_lucia", "two_envelopes", "the_drive51")
ins(s51, "two_envelopes",
    N("supervisor_call", 19, "Handled informally",
      ["An agency supervisor calls, warm and efficient, with a proposal that sounds like mercy: 'Rather than a formal reconsideration with letters back and forth, why don't we just take a fresh look informally at the next staffing?' Families accept versions of this offer every day, because conflict is exhausting and warmth is persuasive.",
       "Your answer is the scenario's smallest hinge: 'I appreciate it — and I'd like the reconsideration in writing anyway, with the packet attached, so the fresh look has the documents in front of it.' Informal looks leave no record of what was looked at. Yours will."],
      [C("File the written reconsideration with the packet attached — the offer noted, gratefully, in the cover letter.", "reconsideration")]))
rw(s51, "two_envelopes", "reconsideration", "supervisor_call")
ins(s51, "tricky_question",
    N("neighbors", 25, "The neighbors, dated",
      ["Your neighbors — the ones who watched the 2019 renovation from their porch with professional interest — produce the corroboration you didn't know existed: dated photographs from a block party, August 2019, showing the finished attic's window open, a fan in it, and your nephew asleep on a cot beneath it at dusk. They sign a one-paragraph statement: the room was finished, heated, and slept in, seven years before the study called it storage.",
       "A study can be wrong innocently. What it cannot survive is a dated photograph. The reconsideration now has one."],
      [C("Add the statement and photo to the packet, with a one-line cover note. Then the re-study gets scheduled.", "restudy_set")]))
rw(s51, "tricky_question", "restudy_set", "neighbors")
ins(s51, "restudy_set",
    N("restudy_day", 30, "The second visit",
      ["The re-study worker arrives with the packet in her bag and reads the attic's measurements before she climbs the stairs — the system auditing itself with its own paperwork as the checklist. She measures anyway. Numbers that agree with documents are the sound of a file healing. Downstairs she photographs Petra's separate entrance, the meter, the lease on the refrigerator where Petra taped it, not as evidence but as an address label for the truth.",
       "On the porch she says the most unbureaucratic sentence of the summer: 'I don't know how the first visit missed the room. I'm not going to.'"],
      [C("Her summary follows within the week. Watch for the sentence that matters.", "ms_tomas_letter")]))
rw(s51, "restudy_set", "july_review", "restudy_day")
ins(s51, "restudy_day",
    N("ms_tomas_letter", 31, "Not sustained",
      ["The re-study summary arrives with its framed sentence — 'prior findings regarding household composition and sleeping arrangements are not sustained on re-inspection' — and Ms. Tomas adds a cover email of her own: the original summary's errors are acknowledged, the corrected study will be transmitted to the review, and the agency's position is 'under supervisory review.' Your denial has been factually dismantled. What remains is the signature that turns dismantled into approved — and signatures live in queues.",
       "You have learned the system's lesson by now: queues are climbed by paper with dates on it, and by asking, in writing, what remains."],
      [C("Ask in writing: what remains between 'not sustained' and approval, and on what date will it be decided?", "approval_clock")]))
rw(s51, "restudy_day", "july_review", "ms_tomas_letter")
ins(s51, "ms_tomas_letter",
    N("approval_clock", 33, "The queue, made visible",
      ["The answer, in writing because you asked in writing: the corrected study goes to a supervisor whose approval docket runs two weeks; the July 9th review is five days away. The arithmetic is the scenario in miniature — you will likely reach the review heard but not yet approved, with the court's order as the bridge, or approved by a margin of days. Either way, the record will be the strongest thing in the room.",
       "Silvia's part is next: her counsel will present the re-study, and Silvia herself has a statement she has been writing in the program, in a notebook, in the evenings."],
      [C("Call Silvia. The review is coming; her voice belongs in it beside yours.", "lucia_call2")]))
rw(s51, "ms_tomas_letter", "july_review", "approval_clock")
ins(s51, "approval_clock",
    N("lucia_call2", 35, "Silvia's statement",
      ["Silvia's statement, read to you over the monitored phone in a voice that gets steadier by the paragraph, does not ask the court for herself. It asks for her son to be 'held by family while I finish becoming safe' — her words — and names you, your house, and the attic room she grew up hearing her own brothers fight over. The program counselor will attest her progress; her counsel will file the statement.",
       "Kinship is sometimes described as a resource the system uses. In the courtroom it will read as what it is: a family arranging itself around a child, on paper, in advance, at cost. Courts can tell the difference between that and a claim. So can Benny."],
      [C("Prepare your own one page: your qualifications, in order — the right § 6336.1 gives you to be heard on exactly that.", "hearing_prep51")]))
rw(s51, "approval_clock", "july_review", "lucia_call2")
ins(s51, "lucia_call2",
    N("hearing_prep51", 37, "One page, qualifications",
      ["Your page is short because qualifications are: who you are to Benny; the house as corrected on the record; Petra's household documented and cleared; Silvia's support; your clearances (clean, and older than this case); the plan for school, for Silvia's visits, for the program's end. Your right to present it is narrow and real — as a potential kinship care resource, heard on your qualifications to provide kinship care, § 6336.1 — and narrow rights, precisely used, are how non-parties move outcomes.",
       "Benny's foster mother calls that evening: she has packed his overnight bag for the review weekend 'in case,' she says, 'because bags should be ready before they're needed. He taught me that this summer, waiting for you.'"],
      [C("Everyone's paperwork is ready. July 9th will assemble it — or expose what it lacks.", "july_review")]))
rw(s51, "lucia_call2", "july_review", "hearing_prep51")
ins(s51, "july_review",
    N("felix_bag", 38, "The bag, packed in case",
      ["In the courtroom's second row, Benny's foster mother sits with the overnight bag on her knees — his clothes, his toothbrush, the book with the bent cover — packed in case, in a building where 'in case' is decided by people reading files. Silvia's counsel presents the re-study. The agency rises to state its position, and the bag's presence makes its own silent argument: everyone who actually knows this child has already decided where he belongs; only the paper is undecided.",
       "The judge looks at the agency's counsel. 'Your position, as of this morning?'"],
      [C("Hear it — and know that the bag, the tin of receipts, and the dated photographs are all in the record behind the answer.", "outcome51")]))
rw(s51, "july_review", "outcome51", "felix_bag")

# ---- S52 (+15 -> 28)
ins(s52, "by_name",
    N("sanaa_visit", 2, "Sanaa's accounting",
      ["At Saturday's visit, Sanaa gives you the teenager's audit of the situation, itemized on her phone's notes app: the Kellermans — 'good people, this isn't about them'; the group placement — 'a building where the staff rotate and the girls who've been there longest run the bathroom schedule'; her school — 'mid-semester transfer means I lose French and the track season'; and then the item she has clearly been saving.",
       "'Mom. Uncle Hakim has had the same number since I was six. He texts me on Eid. Whatever the paper says about “contacted,” the paper is wrong, and I can prove it from my own phone.' She holds it up: a thread of texts, years long, ending with a photo of rice."],
      [C("Screenshot nothing yet. Ask her to write the number down in her own hand at the sign-in sheet — the record takes handwriting more seriously than phones.", "her_handwriting", addHidden=["child-voice"])]))
rw(s52, "by_name", "her_handwriting", "sanaa_visit")
ins(s52, "her_handwriting",
    N("march_entry", 2, "Side by side",
      ["You lay two documents side by side on Ms. Nowak's desk — the intake form from Sanaa's first week, with Hakim's number in your own exhausted handwriting, correct; and the March family-finding entry, with the same number and two digits transposed. The distance between your family and a group placement is visible to the naked eye: it is the distance between a 3 and an 8.",
       "Ms. Nowak looks at the pair for a long moment. 'We'll correct the entry,' she says, 'and I'll make the call today myself.' It is not an apology. It is better: it is a procedure changing course in front of a witness, on paper you will request in writing."],
      [C("Your letter follows within the day — Hakim named in full, the expedited study requested, September 2nd in the first line.", "the_letter52")]))
rw(s52, "her_handwriting", "the_letter52", "march_entry")
ins(s52, "the_letter52",
    N("agency_pushback", 4, "Are you sure",
      ["The agency's first response to your letter has a hesitation in it that you have learned to recognize as the file defending itself: 'Our notes indicate the uncle was unresponsive in March; before we invest in an expedited study, can the family confirm his current willingness?' The March fiction is being cited as a reason to doubt the March correction — a snake digesting its own tail, in triplicate.",
       "Your reply is two attachments long: the intake form and the corrected entry, with one sentence — 'Willingness confirmed by direct contact on August 4th; the March entry has been corrected by your office.' Fictions cannot survive being answered with their own file."],
      [C("Hakim gets his list the same day. The study is now a race the agency has agreed to run.", "hakim_list")]))
rw(s52, "the_letter52", "hakim_list", "agency_pushback")
ins(s52, "hakim_list",
    N("group_home_call", 6, "The default, inspected",
      ["You ask to tour the group placement — not to fight it, but because Sanaa deserves a mother who has seen the place she is threatened with. It is not a villain's address: the staff are kind, the kitchen is bright, and there are eight girls, a curfew bell, a sign-out board, and a waiting list for the phone. It is a facility doing its best for teenagers nobody's family was found for. Sanaa's family has been found. That is the entire indictment, and nobody at the facility disputes it.",
       "'If she comes to us,' the director says, 'we'll take good care of her. If she doesn't have to — better. We keep a bed for the ones with no Hakim.'"],
      [C("Thank her. Then go see the room at Hakim's, where the alternative is being assembled.", "hakim_house")]))
rw(s52, "hakim_list", "kellerman_ask", "group_home_call")
ins(s52, "group_home_call",
    N("hakim_house", 7, "The room",
      ["Hakim's spare room was his daughter's, and it still has her track medals on the wall — which he offers to take down and Sanaa, consulted by phone, forbids: 'Tell him the medals stay. I run too.' His clearances are already filed; the fingerprint card is on the counter by the rice cooker, appointment circled; his sister-in-law two doors down has signed the backup-care page without being asked twice.",
       "A kinship home assembling itself looks like this: not a courtroom argument, but a room, a calendar, and a man doing forms in the order given."],
      [C("The worker confirms the expedited track in writing tomorrow. The Kellermans, meanwhile, have a question to be asked.", "ashford_call")]))
rw(s52, "group_home_call", "kellerman_ask", "hakim_house")
ins(s52, "hakim_house",
    N("ashford_call", 8, "Expedited, confirmed",
      ["Ms. Nowak's email confirms the architecture in writing: Hakim's study designated expedited; home visit within ten days; clearance results pending; the review on August 27th identified as 'the decision point for placement,' with the Kellermans' September 2nd end date noted as 'the operative deadline.' Every one of those phrases is a handle the next month can grip.",
       "You forward it to Hakim and to your counsel. Paper that is shared is paper that survives."],
      [C("Now the hard question to the Kellermans: if the approval lands days late, will they bridge the gap?", "kellerman_ask")]))
rw(s52, "hakim_house", "kellerman_ask", "ashford_call")
ins(s52, "kellerman_ask",
    N("hakim_fingerprints", 10, "Fingerprint weather",
      ["Hakim's fingerprint appointment is canceled by the system the morning of — a database outage, rescheduled nine days out, which in this August is the difference between a signature and a cliff. He does the thing this batch keeps teaching: he calls, he documents the outage in an email to Ms. Nowak with the cancellation notice attached, and he drives to the walk-in site in the next county on his lunch break, where a human being with ink takes his prints the same day.",
       "Expedited is not a designation. It is a behavior."],
      [C("His prints are in; the home visit is done; the interview remains — the worker meets the man the wrong number hid.", "hakim_interview", cash=-10)]))
rw(s52, "kellerman_ask", "records52", "hakim_fingerprints")
ins(s52, "hakim_fingerprints",
    N("hakim_interview", 11, "The interview",
      ["The study interview is where kinship stops being paperwork: Hakim talks about discipline ('First I feed them. Rules land better after rice'), about Sanaa's father — his brother, whose absence is in both their files — about the spare room's medals, about his daughter's opinion, rendered by speakerphone from college: 'Dad's been practicing having a teenager again. He's ready. Also, tell Sanaa the top bunk is structurally hers.'",
       "The worker writes for a long time. What gets written about a home while it is being lived in, by a worker watching it work, is the strongest paper a study produces."],
      [C("While the study finishes, your record request lands — Sanaa's file, and the March entry in its original ink.", "records52")]))
rw(s52, "hakim_fingerprints", "records52", "hakim_interview")
ins(s52, "records52",
    N("sanaa_school", 13, "The counselor's letter",
      ["Sanaa's school counselor, asked in writing, answers in writing: a mid-semester transfer to the group placement's district would cost Sanaa her French sequence and her track season; her grades, 'after a hard year by any measure,' have stabilized since spring; and the counselor's professional opinion, offered without being asked twice, is that 'the proposed kinship placement preserves every structure currently supporting this student.'",
       "Schools are the continuous institution in a teenager's disrupted life. Their letters carry a weight in review courtrooms that parents' letters, through no justice, do not. Yours is in the packet now."],
      [C("One more Sunday at the Kellermans' before the review — and it is not an ordinary Sunday.", "kellerman_dinner")]))
rw(s52, "records52", "packet52", "sanaa_school")
ins(s52, "sanaa_school",
    N("kellerman_dinner", 15, "The last Sunday dinner (provisional)",
      ["Mrs. Kellerman cooks Sanaa's favorites and gives her the recipe cards, handwritten, 'for whichever kitchen' — along with their Ohio address and a standing invitation that has the force of kinship though the law calls it former foster care. Mr. Kellerman fixes the strap on Sanaa's track bag without being asked, which is his whole dialect of love.",
       "'If it goes wrong at the review,' Mrs. Kellerman says at the door, 'she comes back here until the house closes, and if the agency gives us trouble about days, the judge will hear from us. We know our rights too, dear.' They do: notice, and a voice, § 6336.1. This family is bracketed by people who know theirs."],
      [C("Carry their bridge offer to your counsel — the packet is nearly closed.", "counsel52")]))
rw(s52, "sanaa_school", "packet52", "kellerman_dinner")
ins(s52, "kellerman_dinner",
    N("counsel52", 16, "The chronology",
      ["Your counsel builds the review around a one-page chronology, because chronology is the argument: March — correct number on file, wrong number dialed, no second attempt; August 3rd — notice; August 4th — uncle reached on the first ring; the study expedited; the bridge offered; the signature pending. 'Judges forgive systems many things,' she says. 'A year of a teenager's life filed under a typo is not usually one of them. We don't ask for anger. We ask for an order that makes the file tell the truth going forward.'",
       "The packet closes: intake form, March entry, chronology, school letter, Hakim's study, the Kellermans' offer. One signature is still out there in a queue."],
      [C("Watch the signature the way sailors watch weather — daily, in writing, with dates.", "packet52")]))
rw(s52, "kellerman_dinner", "packet52", "counsel52")
ins(s52, "packet52",
    N("signature_watch", 20, "The queue",
      ["The supervisor's signature becomes your morning liturgy: a call, an email, a status line in reply — 'with supervisor,' 'in review,' 'expected Friday.' Ms. Nowak, to her credit, answers in writing each time, which means the queue now exists as a document rather than a rumor. If the signature lands late, the packet will at least be able to prove exactly where the days went — and proof of where days went is, in this system, a form of pressure all by itself.",
       "Sanaa, packing and unpacking her maybe-bag at the Kellermans', asks the only question that matters nightly: 'Did it sign?'"],
      [C("Plan the move as though it signed: Hakim's van, the Kellermans' boxes, your own calendar cleared for the 30th.", "transport_plan")]))
rw(s52, "packet52", "review52", "signature_watch")
ins(s52, "signature_watch",
    N("transport_plan", 21, "Logistics of a rescue",
      ["The move, if ordered, has a choreography now: the Kellermans drive Sanaa and her boxes on the 30th and stay for the first rice; Hakim's daughter drives down from college 'for the installation'; your sister keeps your shift. Even Mrs. Kellerman's bridge — the extra days, if the signature lags — is written into the plan with its far shore (the September 21st closing) honestly marked.",
       "Plans with named people and dated steps are what courts order when they order transitions. You have built one. The review will decide if it runs."],
      [C("The night before the review, Sanaa repacks the maybe-bag one last time. Be on the phone for it.", "night_before52")]))
rw(s52, "signature_watch", "review52", "transport_plan")
ins(s52, "transport_plan",
    N("night_before52", 23, "Uncle's / Elsewhere",
      ["Sanaa talks you through the packing on speakerphone — the two labeled compartments, the track bag Mr. Kellerman repaired, the recipe cards in the front pocket 'because those go wherever I go.' Her voice is steady in the way of teenagers performing steadiness for their mothers, and you match it, because steadiness is also a thing mothers perform for daughters, and both of you know it, and neither of you says so.",
       "'If it's Elsewhere tomorrow,' she says, 'it's Elsewhere with a date to appeal it. You taught me that. Everything's a draft until the file's closed.' She has become fluent in the family's second language. You would give a great deal for her to never have needed it."],
      [C("Tomorrow: the review, her statement, and the agency's document — signed, or not.", "review52")]))
rw(s52, "transport_plan", "review52", "night_before52")
ins(s52, "review52",
    N("in_chambers", 24, "Her words, summarized",
      ["The judge returns from chambers and does the thing good dependency judges do with a teenager's statement: she puts its substance on the record herself, so Sanaa owns it in the open courtroom without having had to perform it there. 'Sanaa asks to be placed with her uncle. She asks not to be transferred schools. She asked me to note that she provided the correct telephone number herself, in March and again in August.' A ripple — the judge's eye rests, for one level second, on the agency's table.",
       "'Counsel,' she says to the agency, 'your recommendation, and the status of the kinship approval. Exactly, please.'"],
      [C("Exactly is the word the whole month was building toward. Hear the answer.", "outcome52")]))
rw(s52, "review52", "outcome52", "in_chambers")

# ---- S53 (+19 -> 40)
ins(s53, "three_exceptions",
    N("january_visits", 3, "Two kitchens",
      ["January's visits are a geography lesson you did not enroll in: Saturdays at the Millersville home with Selah — braiding, homework, her art portfolio — and Sundays in Quarryville with Rafi and Nina, forty minutes and one transfer of a sleeping five-year-old between the two halves of your family. The children spend their sibling time in your car, which has become, by default, the family's only shared room.",
       "Rafi, buckled in the back with Nina asleep on his shoulder, delivers the review's whole question early: 'Dad. Why can't Grandma's house be the house? She has the big table.' The big table seats eight. Everyone in this case knows it. The file, so far, does not."],
      [C("Get the record — the March kinship notes first. If the file can't answer Rafi, the file is the problem to fix.", "record53")]))
rw(s53, "three_exceptions", "record53", "january_visits")
ins(s53, "record53",
    N("two_kitchens", 8, "The cost, itemized",
      ["Before the correction goes in, you do the accounting nobody at the agency is doing: the sibling set's documented contacts since placement — visits between Selah and the younger two, eleven in eleven months, most of them in your car; two missed for weather; one canceled by a schedule change nobody relayed. Eleven meetings a year is not a sibling relationship. It is a pen pal arrangement with snacks.",
       "Mr. Zielinski adds the accounting to the correction letter as an exhibit. 'Courts respond to arithmetic they can check,' he says. 'Ours checks.'"],
      [C("File the correction with the arithmetic attached — what Esther was asked in March, and what the split has cost since.", "correction53")]))
rw(s53, "record53", "correction53", "two_kitchens")
ins(s53, "correction53",
    N("esther_first_talk", 11, "Esther, precisely",
      ["Your mother, asked the narrower question at last, answers it like an engineer: her hands are good in the morning and poor by eight; the stairs are the problem, not the children; she can cook for five standing on one hip and has; what she cannot do is be the only adult in the story — and with the church program, your sister's Saturdays, and you off the truck by five, she would not be. 'I said no to drowning,' she tells you. 'Nobody asked me about swimming with a rope team.'",
       "The support plan is how a rope team gets documented."],
      [C("Build it as paper — every support a letter, every letter signed.", "support_plan")]))
rw(s53, "correction53", "support_plan", "esther_first_talk")
ins(s53, "support_plan",
    N("church_program", 14, "The director's letter",
      ["The church after-school program's director — who has known Selah since Vacation Bible School and Rafi since he was a rumor — signs her letter at the folding table where the program does its homework: capacity for all three, weekdays to six, Nina in the preschool room with the same teacher her cousin had. 'Families like yours are what the program exists for,' she says, 'though usually the forms are shorter.'",
       "The forms are never shorter. That is why the letters matter: a support that exists as a signature cannot be waved away as a hope."],
      [C("The plan is specified: program, sister, employer. The agency schedules the study — with dates this time.", "study_dates")]))
rw(s53, "support_plan", "study_dates", "church_program")
ins(s53, "study_dates",
    N("nina_preschool", 18, "Nina's mornings",
      ["The study's smallest open question is a five-year-old's morning: Nina's preschool is near the Quarryville home, not Esther's. Her teacher, consulted, provides the answer in writing — a mid-year transfer to the sister preschool two streets from Esther's, same curriculum, a seat held on the director's word — and Esther's neighbor, retired, signs on for the walk-to-school run on program days.",
       "Permanency files are lost on questions this size more often than on law. Each unanswered 'but who handles—' is a stone in the approval's shoe. You are removing stones in writing, one at a time."],
      [C("Stones out. Next: the person this case has been avoiding — Selah, and her own counsel's requested meeting.", "selah_voice")]))
rw(s53, "study_dates", "selah_voice", "nina_preschool")
ins(s53, "school_question",
    N("rafi_therapist", 24, "Rafi's therapist",
      ["Rafi's therapist — the one constant adult across his two placements — writes the letter Mr. Zielinski calls the packet's quiet bomb: the sibling separation is 'the presenting theme' of Rafi's sessions; his drawings are an atlas of two houses and a car; unification with his sisters at a stable kinship home is 'the single intervention most likely to change this child's trajectory.'",
       "It is addressed to the court, signed, and — because you requested records and read them — impossible for the agency's packet to omit without noticing its absence."],
      [C("With the district's letter in hand and Rafi's beside it, Selah's terms get put to her in full.", "selah_terms")]))
rw(s53, "school_question", "selah_terms", "rafi_therapist")
ins(s53, "selah_terms",
    N("selah_weekend", 29, "The test weekend",
      ["Selah spends a February weekend at Esther's before anyone files anything final — her own condition, conveyed through counsel: 'I want to sleep there before I say yes to living there.' The weekend runs on her treaty's terms: her corner of the room, her portfolio on the wall, pancakes at the big table with her siblings orbiting, and Sunday braiding with her foster mother by video call, so the two halves of her life can see each other being decent.",
       "Her report back, through counsel, is one sentence: 'Grandma's house is loud in the right way.' The proposal gets filed with that sentence in it, attributed, verbatim. Courts have decided harder questions on less honest evidence."],
      [C("File the proposal — Esther, all three, supports specified, Selah's terms and her sentence attached.", "proposal_filed")]))
rw(s53, "selah_terms", "proposal_filed", "selah_weekend")
ins(s53, "proposal_filed",
    N("selah_art", 33, "The art teacher's letter",
      ["Selah's art teacher — the one who wrote her recommendation — adds the school's voice to the file: Selah's portfolio is entered in the regional show; her attendance is perfect; 'her stability this year, in one school, is the platform her work is built on,' and the district's letter confirming Esther's address is in-district 'means the platform holds.' Teachers write the evidence permanency law wishes it always had: what a child's life is actually made of, in the present tense.",
       "The study packet grows; the study itself hits its one snag the same week."],
      [C("The snag: Esther's clearance renewal flags an old address mismatch. Correct it with documents, the family's new reflex.", "clearance_renewal")]))
rw(s53, "proposal_filed", "room_fix", "selah_art")
ins(s53, "selah_art",
    N("clearance_renewal", 34, "The mismatch",
      ["Esther's clearance renewal flags an address from 1998 — a house she sold before Rafi's foster parents met — because databases, like families, keep everything and date nothing. The correction is a deed, a tax record, and a letter, assembled by you in four days and transmitted with the same unglamorous ceremony as every other fix in this case: hand-delivered, copy kept, receipt obtained.",
       "It is worth pausing on the pattern, because the pattern is the pedagogy: paper problems are not character verdicts. They are errands with deadlines, and they yield to exactly one method — documents, delivered, confirmed."],
      [C("Errand run. The study visit's written findings are next — and they contain the stairs question, formalized.", "home_visit53")]))
rw(s53, "selah_art", "room_fix", "clearance_renewal")
ins(s53, "clearance_renewal",
    N("home_visit53", 37, "Interim findings",
      ["The study's interim findings arrive as a document instead of a conversation, which your winter has taught you to prefer: rooms adequate; supports verified; clearances clear as corrected; one item open — 'primary caregiver sleeping quarters on second floor; mobility plan required.' Formal questions are gifts: they can be answered formally, in a form the final report must then acknowledge.",
       "Esther reads the item and snorts. 'Required. At last, a form that talks like my doctor.' Her doctor is next."],
      [C("Get the doctor's note — arthritis managed, ground-floor living recommended — and put the conversion plan in writing.", "esther_doctor")]))
rw(s53, "clearance_renewal", "room_fix", "home_visit53")
ins(s53, "home_visit53",
    N("esther_doctor", 39, "The doctor's note",
      ["Esther's physician of twenty years writes it in the plain style of a man who has filled out forms since before they were PDFs: arthritis bilateral, managed; stairs inadvisable as a daily routine; 'patient fully capable of caregiving in a ground-floor living arrangement, which I recommend.' It is the medical third of the stairs answer. The carpentry third is your cousin's crew. The documentary third is the addendum the study will now have to write.",
       "You schedule the conversion for the following week. The dining room has hosted four dinners a decade; it is about to become the most important room in three childhoods."],
      [C("Convert the room. Document it: photos, invoice, the doctor's note stapled to the plan.", "room_fix")]))
rw(s53, "home_visit53", "room_fix", "esther_doctor")
ins(s53, "room_fix",
    N("gideon_work", 44, "Your own file",
      ["Your track advances in parallel and in writing: the parenting program's certificate, filed; the route change confirmed by your employer's second letter; your visits — all of them, both kitchens — logged by two foster homes as consistent and calm. None of it is the April question, and all of it is the April weather: a court deciding whether to build a permanency plan around a grandmother also reads the father's trajectory for what happens after.",
       "Mr. Zielinski files your progress with the packet without commentary. Trajectories speak in their own tense."],
      [C("Now the reckoning you have been postponing: Rafi and Nina's foster parents, and what they will say.", "foster_position")]))
rw(s53, "room_fix", "foster_position", "gideon_work")
ins(s53, "foster_position",
    N("sibling_saturdays", 51, "Saturdays at the big table",
      ["The agency — prodded by your written request and, in fairness, by its own worker's conscience — starts sibling Saturdays at Esther's in March: all three children, her house, the big table, agency transport both ways. The visit notes accumulate the evidence no expert can manufacture: Nina napping in the first-floor room's doorway 'because that's where everyone is'; Rafi teaching Selah the Quarryville dog's invented name; the fort, constructed in Esther's living room under Rafi's generalship, with Selah as minister of blankets.",
       "Saturdays are the placement's rehearsal, documented weekly. By April, the file no longer describes a proposal. It describes a household that already meets on weekends and is asking to stop commuting."],
      [C("Propose the bridge to the foster parents in writing — continuity after the move, not erasure.", "bridge53")]))
rw(s53, "foster_position", "bridge53", "sibling_saturdays")
ins(s53, "bridge53",
    N("agency_split", 60, "The agency, of two minds",
      ["Ms. Nilsen supports the placement and says so in her report draft; her supervisor's margin asks the question supervisors are paid to ask: 'Selah — is the yes durable?' It is a fair question, and it has a documentary answer — her terms, met item by item; her test weekend; her sentence about the loud house — which Mr. Zielinski assembles into a two-page response filed before the review, so the durability question is answered with dates instead of reassurances.",
       "Agencies are not monoliths; they are arguments between a worker's knowledge and a supervisor's caution. Filing for the supervisor's question is how families join that argument on the winning side."],
      [C("Draft the ASFA exception documentation with Mr. Zielinski — door one, built of paper.", "exception_draft")]))
rw(s53, "bridge53", "exception_draft", "agency_split")
ins(s53, "exception_draft",
    N("march20_report", 75, "March 20th",
      ["The study report issues on the date the January letter promised — a small miracle of the calendar that you note because you have learned to: promises kept by systems are data too. Esther: approved for the sibling group of three, the support plan incorporated, the mobility item closed by the conversion addendum. The agency's recommendation for April is drafted to match, with the supervisor's durability question attached as answered.",
       "What remains is the children's own words, collected cleanly — and April's ordinary weather."],
      [C("Their counsel collects the words. You do not ask what was said. Clean pages only.", "children_words")]))
rw(s53, "exception_draft", "children_words", "march20_report")
ins(s53, "children_words",
    N("continuance_scare53", 84, "The scare, again",
      ["The continuance scare arrives on schedule, as continuance scares do: a scheduling conflict, a floated May date — May, past the clock, which would convert this entire winter into a termination filing answered too late. Mr. Zielinski opposes on the papers the same day, with the ASFA date in the first paragraph and the completed study in the second. The court keeps April 22nd in a short order that does not disguise its reasoning: 'The children's fifteen-month date is May 2nd. The review will be heard April 22nd.'",
       "Even the scare did work: it made a judge write the clock into an order, which means the clock is now the court's own concern and not only yours."],
      [C("One more document surfaces before the review — the agency's own ASFA planning memo. Read it carefully.", "asfa_memo")]))
rw(s53, "children_words", "review53", "continuance_scare53")
ins(s53, "continuance_scare53",
    N("asfa_memo", 95, "The agency's memo",
      ["The agency's internal ASFA memo — produced with the updated record your January request set in motion — is the winter's most instructive document: it lists the May 2nd date, the three exceptions, and a caseworker's annotation beside 'relative care': 'Grandmother approved 3/20; placement pending court order — exception expected to be satisfied.' Expected. The agency is planning around the same door you built. Its lawyers will nonetheless argue caution at the review, because institutions argue caution the way rivers argue downhill.",
       "You do not confront anyone with the memo. You file your packet so that the court's questions meet it naturally."],
      [C("Assemble the final packet with Mr. Zielinski — every document this winter produced, in chronological order.", "packet53")]))
rw(s53, "continuance_scare53", "review53", "asfa_memo")
ins(s53, "asfa_memo",
    N("packet53", 100, "The packet",
      ["Chronology is the packet's argument: March's sentence and January's correction; the specified plan and its signed supports; the district's letter and Selah's treaty; a therapist, a teacher, a doctor, a director; a converted room; eleven Saturdays of visit notes; an approval dated March 20th; and a memo in the agency's own hand expecting the exception to be satisfied. Mr. Zielinski binds it without a summary. 'Summaries are for cases that need adjectives,' he says. 'This one has dates.'",
       "Esther has been ironing for two days. The review is Thursday."],
      [C("The night before: your mother's kitchen, the big table, three empty chairs that may not be empty long.", "night_before53")]))
rw(s53, "asfa_memo", "review53", "packet53")
ins(s53, "packet53",
    N("night_before53", 104, "The night before",
      ["Esther sets the big table for nobody — for luck, she says, the way sailors set a watch. Your sister calls from her Saturday shift to say the commitment letter is the truest thing she has ever signed. Selah, by her counsel's forwarded message, has added nothing to her terms and withdrawn nothing: 'Tell them I said yes myself. Still.'",
       "You sleep the way litigants sleep, which is to say in shifts, and dream of a car with no children asleep in the back because the children are, at last, already home. Thursday will grade the dream against the file. The file is ready to be graded."],
      [C("Go in with the file you built. It is, in the end, the argument.", "review53")]))
rw(s53, "packet53", "review53", "night_before53")

# ---- S54 (+24 -> 40)
ins(s54, "start",
    N("otto_visit", 0, "Saturday's visit",
      ["Otto, at Saturday's visit, is deep in the serious business of being six in a place that is working: he has a reading corner, a foster brother of nine who trades him dinosaur facts at par, and a drawing — produced for you with ceremony — of 'Papou's garden, with the tomatoes I planted with my hands.' Salvatore grew those tomatoes from seed in a windowsill tray, with a six-year-old's supervision, through the whole spring of the placement.",
       "The agency's summary says the current home is 'adequate.' Adequate is what documents call a life they haven't read. You take a photo of the drawing. Some exhibits are crayon."],
      [C("Ask your counsel the procedural version of your father's question: \"Can they recommend a move on a document I can't read?\"", "counsel54", addHidden=["placement-stability"])]))
rw(s54, "start", "counsel54", "otto_visit")
ins(s54, "counsel54",
    N("current_foster", 2, "Mrs. Baird",
      ["Otto's foster mother, Mrs. Baird, calls before you can — foster parents talk to parents in the cases that are working, which is how you know this one is. 'They copied me on nothing,' she says, 'but the worker mentioned Riverton at pickup, in front of Otto, so now I have a six-year-old asking if he's moving to where the dinosaurs can't visit. I am writing the judge a letter. I've had eleven foster children; I have never written a judge a letter.'",
       "Foster parents get notice of hearings and the right to be heard (42 Pa.C.S. § 6336.1). Mrs. Baird intends to use both, and what she has to say — that Otto is attached, thriving, and eleven minutes from his mother — is the current placement's defense, delivered by its only daily witness."],
      [C("Thank her — and file your own paper: the record request, naming the assessment expressly.", "request54")]))
rw(s54, "counsel54", "request54", "current_foster")
ins(s54, "request54",
    N("veronica_program", 3, "Your side of the ledger",
      ["Your own file moves in the background of the assessment fight and matters to it: parenting program completed in August with the facilitator's letter; visitation attendance eleven for eleven; the part-time job at the bakery held for three months now, with a manager who writes 'reliable' in the reference and means it as data.",
       "Courts read placement fights inside trajectory stories. Whatever the assessment says about ninety days, the trajectory says the placement question is converging on family — which is why a fifty-mile move, this autumn, reads to everyone who knows the file as a step in the wrong direction."],
      [C("The assessment arrives — mostly. Inventory the black ink before you read the numbers.", "redaction_fight")]))
rw(s54, "request54", "the_item", "veronica_program")
ins(s54, "veronica_program",
    N("redaction_fight", 4, "Inventory of black ink",
      ["You and Ms. Lindgren inventory the redactions on her conference table, itemized like a grocery list of concealments: the rater's name and signature — blacked; two narrative paragraphs — blacked; the scoring page's header — blacked with an enthusiasm that suggests habit rather than judgment. 'Some redactions protect reporters and other families,' she says. 'Those are lawful and we won't fight them. Names of the agency's own employees and the text of the instrument itself are not in that category — § 3130.44(f) says the regulation 'shall not be construed as protecting the agency's employees,' and an assessment a court is asked to rely on is not a confidence.'",
       "The fight over ink comes after the fight over arithmetic, though. The items are readable, and one of them is wrong in a way you can prove."],
      [C("Go to Item 14 — the item the whole recommendation stands on.", "the_item")]))
rw(s54, "veronica_program", "the_item", "redaction_fight")
ins(s54, "the_item",
    N("item_by_item", 5, "The other twenty-one",
      ["Before the logs arrive, you read the whole instrument — all twenty-two items — the way its author apparently didn't. The profile that emerges is not a child in crisis: school readiness strong, health strong, your visitation quality scored well by the same rater on items she could see from the file's cheerful pages. The composite is dragged across the Level II line by a cluster of three items — and Item 14, the 'supervision incidents' score, is the cluster's anchor and its only factual claim about you.",
       "Assessments fail in two ways: bad instruments, and good instruments filled in from summaries. This one has every sign of the second — which is the kind that corrections, stipulations, and primary records are built to fix."],
      [C("Do the arithmetic the grid does: what happens to the composite if Item 14 is what the logs say it is?", "scoring_page")]))
rw(s54, "the_item", "visit_logs", "item_by_item")
ins(s54, "item_by_item",
    N("scoring_page", 6, "The grid, recomputed",
      ["Ms. Lindgren recomputes it on a legal pad while you watch, because arithmetic you watch is arithmetic you can testify about: Item 14 at 3 pulls the composite to 41 — one point over the Level II threshold of 40. Item 14 at 1, which is what a single redirection scores on the instrument's own rubric, puts the composite at 37 — squarely in the 'maintain current placement with services' band. The entire recommendation — a county, a school, a childhood address — is the weight of one misread item, resting on the scale like a thumb.",
       "'We are not arguing the instrument is wicked,' she says. 'We are arguing it was fed a number its own records contradict. Judges understand thumbs on scales.'"],
      [C("See the alternative with your own eyes before you fight it: tour the Riverton home.", "level2_tour", addHidden=["assessment-items"])]))
rw(s54, "item_by_item", "visit_logs", "scoring_page")
ins(s54, "scoring_page",
    N("level2_tour", 7, "Riverton, honestly",
      ["The Riverton home, toured at the agency's invitation, is not a place you can honestly call bad: a patient couple, a quiet street, a therapy room with good light. It is also set up for teenagers — the other two residents are fifteen and sixteen — an hour's drive and two buses from your bakery shifts, and in a school district where Otto would be a mid-year kindergartner with no one who knows his name. The house parents ask, with genuine kindness, why a six-year-old is being sent to a home like theirs. You do not have an answer that survives saying out loud.",
       "You thank them and mean it. The fight was never with this house. It is with the number that addressed Otto to it."],
      [C("Home again. The visitation logs — the primary records — are the next paper in.", "visit_logs")]))
rw(s54, "scoring_page", "visit_logs", "level2_tour")
ins(s54, "visit_logs",
    N("riverton_distance", 8, "Two buses, timed",
      ["Ms. Lindgren's paralegal rides the Riverton route with a stopwatch, the way this firm builds exhibits: door to door from your apartment, one hour and fifty minutes, two transfers, the second at a shelter-less stop on a highway shoulder. From Salvatore's house: two hours and ten. Your Wednesday visits, currently a walk and a short bus, would become expeditions — and the order would still call them 'weekly,' because orders describe intentions and bus schedules describe reality.",
       "Distance is not an argument in the legal sense. It is something stronger in the human one: it is the medium in which every other provision of the order either lives or dies."],
      [C("Add the timed route to the packet. Then certify the logs — the visitation center's director is waiting to be asked.", "center_director")]))
rw(s54, "visit_logs", "correction_filing", "riverton_distance")
ins(s54, "riverton_distance",
    N("center_director", 9, "The director certifies",
      ["The visitation center's director — a woman who has supervised eleven of your visits through a one-way mirror and a sign-in book — provides the certification without being subpoenaed: the logs are contemporaneous, signed per visit by the assigned supervisor, kept in the ordinary course; and her own cover note adds, in the flat style of people who keep records for a living, 'Our center recorded one redirection involving this mother in the period, on the occasion documented. No others appear.'",
       "Contemporaneous records kept by neutrals are the aristocracy of evidence. You now hold eleven pages of it, with a crown of certification on top."],
      [C("File the correction memorandum: Item 14, the rubric, the certified logs, the grid.", "correction_filing")]))
rw(s54, "riverton_distance", "correction_filing", "center_director")
ins(s54, "correction_filing",
    N("agency_response54", 11, "The agency answers",
      ["The agency's response to the correction memorandum is a study in two registers: it does not defend Item 14 — the phrase 'the scoring reflected the information available to the rater' does that quiet work — but it defends the recommendation on 'the composite picture and clinical judgment,' and asks that the rater's identity remain confidential 'for personnel reasons.' Both defenses now have names, which means both can be answered: the composite is arithmetic, and arithmetic can be recomputed; the confidentiality claim has § 3130.44(f) standing in its doorway.",
       "'They've retreated to exactly the ground conferences exist to narrow,' Ms. Lindgren says. 'October 22nd just became the whole case, conducted early.'"],
      [C("File the memorandum's supplement: the recomputed grid and the (f) argument — and aim both at the conference.", "memo_filed")]))
rw(s54, "correction_filing", "memo_filed", "agency_response54")
ins(s54, "memo_filed",
    N("gal_position", 13, "Otto's own counsel",
      ["Otto's counsel — appointed for him, as children's counsel is — files a two-page position that changes the hearing's weather: she has visited Otto in his current home and at his grandfather's; she opposes the Riverton move as 'unsupported by the corrected record and disruptive of documented attachments'; and she supports the kinship alternative 'if the court reaches placement.' Children's positions do not decide cases. They do something subtler: they tell the judge which outcome the child's own advocate will defend on appeal, and which will be appealed.",
       "The room is filling with people whose job is Otto, all reading from the corrected record. The agency's summary is becoming the only document in the case that nobody else will sign."],
      [C("Mrs. Baird's letter is the last voice to collect — the daily witness, in her own words.", "foster_statement54")]))
rw(s54, "memo_filed", "salvatore_call", "gal_position")
ins(s54, "gal_position",
    N("foster_statement54", 14, "Mrs. Baird's letter",
      ["Mrs. Baird's letter to the court is four sentences long and took her, she tells you, eleven drafts: Otto's year-in-four-months — the reading, the nightmares' retreat, the dinosaur economy — her observation that 'his mother's visits are the week's hinge, and his grandfather is the month's,' and her conclusion: 'I am a foster parent. I am supposed to be temporary. Moving this child across the county does not make him safer; it makes him temporary somewhere else, farther away.'",
       "She will attend the hearing and say it under her § 6336.1 right to be heard. The letter goes in the packet as it was written — foster parents who write judges once in eleven children do not get edited."],
      [C("The packet has its voices. Now the alternative needs its paperwork finished: Salvatore, asked as a plan.", "salvatore_call")]))
rw(s54, "gal_position", "salvatore_call", "foster_statement54")
ins(s54, "salvatore_call",
    N("salvatore_house", 15, "The house, studied by family first",
      ["You walk Salvatore's house with study eyes before the agency does: the spare room — your brother's childhood room, then a guest room, currently a tomato-seedling nursery that can be a boy's room in a weekend; the garden's fence, sound; the school two blocks away, the same one you attended, where the crossing guard is a woman Salvatore has known for thirty years.",
       "He endures your inspection with the patience of a man being measured for something he wants. 'Ask the agency to come,' he says. 'I have been ready longer than their form has existed. Let the form catch up.'"],
      [C("His written request goes in this week, clearances started — filed early enough to be an alternative, not an aspiration.", "salvatore_files")]))
rw(s54, "salvatore_call", "salvatore_files", "salvatore_house")
ins(s54, "salvatore_files",
    N("clearance_sal", 16, "Salvatore's clearances",
      ["Salvatore's clearances return the way seventy-one years of an unremarkable life suggested they would: clean, quickly, with one phone call to confirm that the Salvatore of the garden is the Salvatore of the form, there having been a second Salvatore in the county database — a cousin, deceased in 2009, whose existence briefly confused a clerk. Identity is this batch's recurring gremlin; here it costs one phone call instead of a winter, because the identifiers were demanded up front, in writing, in the application itself.",
       "His home study visit is scheduled before the conference. The alternative is becoming a file of its own — which is what alternatives must become to be ordered."],
      [C("October 22nd: the pre-hearing conference. The narrowed fight, in a small room.", "conference_day")]))
rw(s54, "salvatore_files", "narrowed_order", "clearance_sal")
ins(s54, "clearance_sal",
    N("conference_day", 17, "October 22nd",
      ["The conference room is too small for the number of folders, which is how you know it is the right room. The agency concedes the logs' authenticity. Your counsel concedes the instrument's general validity — a concession that costs nothing and buys the only thing that matters: credibility for the sentence that follows. 'Then the conference's business,' she says, 'is one item, one rater, and one recommendation the corrected arithmetic no longer reaches.'",
       "Rule 1340(F)'s conference purposes — narrowing, settlement, order — proceed in that order and stall, honorably, at settlement: the agency will not withdraw the recommendation without a supervisor who is not in the room. Narrowing, though, is fully achieved, and narrowing gets an order."],
      [C("Get the narrowed issues into the conference order — Item 14's status, in the agency's own stipulation.", "narrowed_order")]))
rw(s54, "clearance_sal", "narrowed_order", "conference_day")
ins(s54, "narrowed_order",
    N("study_visit54", 18, "Salvatore's study visit",
      ["Salvatore's home study visit is conducted by a worker who arrives with the corrected file and leaves with a summary that contains no flagged items — a sentence so rare in this batch that Ms. Lindgren reads it twice for typos. The room (seedlings relocated to the windowsill, a boy's bed installed), the fence, the school route walked and timed by the worker herself: two blocks, seven minutes, one crossing guard known by name for thirty years.",
       "'Your father,' the worker says at the door, in the unofficial register workers use when a home has answered everything, 'has been ready since before there was a form.'"],
      [C("The study is filed. One week to the hearing. The agency's last card is its rater — prepare for her.", "rater_call")]))
rw(s54, "narrowed_order", "hearing_prep54", "study_visit54")
ins(s54, "study_visit54",
    N("rater_call", 19, "The rater, reached",
      ["Through counsel, the rater's account is finally taken, and it is the anticlimax the whole case predicted: a conscientious worker, covering three caseloads in a staffing crunch, who scored the assessment from the prior worker's running summary — a summary that had itself merged the visit notes' categories, counting every 'supervisor intervention' as a redirection of you. She has since read the logs. She will testify, her counsel-relayed position says, 'consistently with the records.'",
       "No villain, again. A summary of a summary, a threshold crossed by a point, a six-year-old nearly addressed to the wrong county by a clerical avalanche. The system produces these outcomes without a single person intending them — which is precisely why the corrections machinery, and not outrage, is the family's tool."],
      [C("Otto's school writes the last outside letter. Collect it, and the packet is complete.", "otto_school")]))
rw(s54, "study_visit54", "hearing_prep54", "rater_call")
ins(s54, "rater_call",
    N("otto_school", 20, "The kindergarten letter",
      ["Otto's kindergarten teacher writes the school's letter in the vocabulary of early childhood, which translates in courtrooms without loss: Otto 'has settled into the routines that make learning possible'; his 'secure base' in the current home and his weekly rhythm with you and Salvatore are named, by a professional who watches him five days a week, as the visible causes. A mid-year move to a distant district 'would restart a settling process that took four months, in a child for whom settling is the curriculum.'",
       "It is the third independent institution — center, school, child's counsel — to describe the same child the assessment's Item 14 could not see."],
      [C("The agency makes one more move before the hearing — a re-score offer. Hear it with your counsel.", "agency_concede")]))
rw(s54, "rater_call", "hearing_prep54", "otto_school")
ins(s54, "otto_school",
    N("agency_concede", 20, "The re-score offer",
      ["The agency offers, through counsel, to withdraw the assessment and re-score it 'administratively' — which would fix the number and quietly dissolve the hearing into a new summary, on the agency's timetable, with the move recommendation 'held in abeyance' rather than decided. It is a genuinely reasonable offer, and Ms. Lindgren's answer is the scenario's last strategic lesson: 'A correction we win by stipulation, in an order, is precedent for every future reader of this file. A correction they make in their office is a rumor by spring. We keep the hearing.'",
       "She adds the human codicil, because she is good at her job: ' — and we thank them for the offer in writing, because the next family with this worker deserves her having made it.'"],
      [C("Declined, gratefully, in writing. Final packet assembly — then the hearing reads the whole record.", "hearing_prep54")]))
rw(s54, "otto_school", "hearing_prep54", "agency_concede")
ins(s54, "hearing_prep54",
    N("packet54", 22, "The packet, indexed",
      ["The hearing packet is indexed like a book because judges read like everyone else — front to back, forming the story early: (1) the assessment, complete; (2) Item 14 and the rubric; (3) the certified logs; (4) the recomputed grid; (5) the conference order's stipulation; (6) the school, the foster mother, the child's counsel; (7) the timed bus route; (8) Salvatore — study, clearances, and the sentence from his porch. Forty-one pages, and the argument is finished by page nine; the rest is the world agreeing.",
       "Your own statement is the packet's last page, and it is the shortest thing in it."],
      [C("Recompute the grid one last time, in your own hand, so the numbers are yours in the courtroom too.", "score_recompute")]))
rw(s54, "hearing_prep54", "review54", "packet54")
ins(s54, "packet54",
    N("score_recompute", 22, "Your arithmetic",
      ["You do the subtraction at the kitchen table the way Ms. Lindgren did it on the legal pad: composite 41 as scored; Item 14 from 3 to 1, per the instrument's own rubric applied to the certified logs; composite 37; the band changes; the recommendation's engine stops. It is the whole case in four operations, and you can now do it from memory, which means in the courtroom — whatever the agency's witness says about clinical judgment — the arithmetic will be sitting beside you, calm as a metronome.",
       "Salvatore calls during the arithmetic. 'Tomorrow I wear the tie your mother gave me,' he says. 'For luck, and because she would have wanted to see this file.'"],
      [C("Sleep. Tomorrow the record gets read by the only reader who can order from it.", "night_before54")]))
rw(s54, "packet54", "review54", "score_recompute")
ins(s54, "score_recompute",
    N("night_before54", 23, "The night before",
      ["You lay out your statement — one page, rehearsed to the mirror and then deliberately un-rehearsed, because judges can hear varnish. It says: who Otto is at six; what the logs say about the visits, in numbers; what the corrected grid says, in numbers; and what is being asked — that the court decide on the whole record, including the man with the garden, rather than on a summary of a summary.",
       "It does not mention dinosaurs. Salvatore, reviewing it by phone, insists on one amendment, and you make it, because it is true and because he is right that true things belong in statements: 'Otto has a room ready in my house. It was ready before this case had a name.'"],
      [C("Morning. The courthouse. Your father's tie, your arithmetic, forty-one pages.", "morning54")]))
rw(s54, "score_recompute", "review54", "night_before54")
ins(s54, "night_before54",
    N("morning54", 24, "The courthouse steps",
      ["Salvatore arrives twenty minutes early, in the tie, with a paper bag containing two sandwiches 'because hearings run long and lawyers forget lunch' — a theory of litigation no one in the building refutes. Mrs. Baird is already inside, seated, with her letter's eleventh draft folded in her purse like a psalm. Otto's counsel nods at you across the hallway with the compact of people who have read the same forty-one pages.",
       "The agency's team arrives with the original summary, three pages, in a folder that looks — everyone in the hallway can see it — very thin."],
      [C("Go in. The whole record is about to be read by its intended reader.", "review54")]))
rw(s54, "night_before54", "review54", "morning54")

# ---- S55 (+22 -> 40)
ins(s55, "call_beatrice",
    N("zola_call", 1, "Zola, by phone",
      ["Your first call with Zola in Riverton is eleven minutes long and conducted, on her end, from a bathroom — 'it's the quiet room' — in a voice doing eight-year-old bravery at professional standard. Her inventory: the foster mother is kind and braids 'almost like Aunt Bea'; the new school has a fish tank and no one who knows her reading level; she has been put in the 'blue group,' which she has assessed, correctly, as not the group she was in.",
       "'Is Aunt Bea mad I didn't go to her house?' she asks, at the end, quietly — and there it is: a child absorbing a system's failure as a family's choice. 'Aunt Bea is not mad. Aunt Bea has a binder. The binder and I are working on it.'"],
      [C("Work means three fronts, in writing, this week. Call your counsel in the morning.", "counsel55", addHidden=["child-voice"])]))
rw(s55, "call_beatrice", "counsel55", "zola_call")
ins(s55, "counsel55",
    N("school_records", 2, "Her old school's file",
      ["Zola's old school releases her file to you as her mother, and it is the portrait of a specific child that a county-line transfer erases: reading group placement earned in October, the teacher's note ('Zola reads aloud to the kindergarten buddies on Fridays — a responsibility she guards'), attendance perfect since September. The Riverton school, through no fault of its own, received a name, a birthdate, and a 'blue group' guess.",
       "Her teacher, told where Zola went, says the sentence school people say in these cases and mean as indictment: 'Nobody called us. We would have sent her records the same day — and we would have asked why.' The asking-why, institutionalized late, is your counsel's job now."],
      [C("File all three fronts: review, record, and Beatrice from zero.", "file_three")]))
rw(s55, "counsel55", "file_three", "school_records")
ins(s55, "file_three",
    N("agency_version", 4, "The agency's answer",
      ["The agency's written response to your review filing is courteous, complete, and — read carefully — an artifact of the file it defends: the move 'necessitated by an emergency disruption'; the Riverton home 'licensed, experienced, and available'; kinship 'explored at intake, with the identified relative non-responsive to outreach.' Non-responsive. Beatrice, who keeps a binder with sub-labels, has been filed under a word she would cross out in red pencil.",
       "Your counsel tabs the sentence. 'This is the paragraph the record request exists for,' she says. 'Every factual claim in it is checkable against their own notes. We are going to check all of them, in order, and bring the receipts to December.'"],
      [C("Fight the interim first — visits and school continuity now, while the receipts accumulate.", "interim_ask")]))
rw(s55, "file_three", "interim_ask", "agency_version")
ins(s55, "interim_ask",
    N("transport_log", 7, "Fifty-five minutes, logged",
      ["You start the transport log the day the interim order issues: each visit's drive, timed, with the transport van's arrivals and one memorable non-arrival noted in the flat style the file has taught you. November 9th: 'Van 40 minutes late. Visit shortened. Zola asked if the van forgot her. Advised the van did not forget her; the schedule did.'",
       "Distance in these cases is usually argued as a feeling. Logged, it becomes a record — hours of a childhood spent on a highway because a kinship file was mishandled in February. By December the log will hold nine round trips. You intend the judge to do that arithmetic herself."],
      [C("Use the first restored weekend visit to see the Riverton home with your own eyes.", "first_riverton_visit")]))
rw(s55, "interim_ask", "record_arrives55", "transport_log")
ins(s55, "transport_log",
    N("first_riverton_visit", 8, "The Riverton home",
      ["The Riverton foster mother is as advertised — kind, experienced, unoffended by your existence — and her home runs the calm shift-work of a professional respite house: three children this month, a wall calendar in three colors, a quiet room that Zola has accurately described. She makes tea and says, without prompting, the thing that will matter in December: 'I take the emergencies. I'm good at the first month. I'm not set up to be somebody's whole school year, and I told them that when I took her.'",
       "You write it down in the car, word for word, with her permission. The system's own placement is telling you it was a bridge. The only dispute is whether the far shore was ever looked for."],
      [C("On the drive back, the agency calls: a new worker has inherited the file. Listen for what she inherits besides paper.", "halvorsen_call")]))
rw(s55, "transport_log", "record_arrives55", "first_riverton_visit")
ins(s55, "first_riverton_visit",
    N("halvorsen_call", 9, "The new worker",
      ["Ms. Halvorsen took over the case in October — the fourth worker, by your count, since February — and she has the inheritor's honesty: 'I've read the file twice. I can't defend February, and I'm not going to try in this call. What I can tell you is the December review will get my honest read of the record as it stands then — including wherever Beatrice's study has gotten to.'",
       "Worker turnover is one of the system's quiet engines: February's mistakes were made by a worker who has left; the file remains, and only the file can be cross-examined. Your record request — filed by you, answered to you — is about to become the case's memory. It arrives this week."],
      [C("Read it the day it lands. Family finding first, placement log second, dates throughout.", "record_arrives55")]))
rw(s55, "first_riverton_visit", "record_arrives55", "halvorsen_call")
ins(s55, "record_arrives55",
    N("binder_scene", 11, "The binder, reconciled",
      ["You and Beatrice reconcile the two paper systems at her kitchen table, page by page, the way auditors close a year: her binder's February 20th entry ('Called county. Spoke to a woman in intake. Said packet would be remailed.') beside the agency's own call note for the same date, with the same substance in a caseworker's hand. March 9th: binder and file agree again. The systems agree about everything except the conclusion the summary drew from them.",
       "'I was never non-responsive,' Beatrice says, closing the binder with the calm of a woman who has been proven right by the opposing archive. 'I was responsive into a drawer.' The summary's word cannot survive its own file. Your counsel will make sure December knows it."],
      [C("Read on into the placement log — you are looking for the date the Riverton bed entered the story.", "the_date55")]))
rw(s55, "record_arrives55", "the_date55", "binder_scene")
ins(s55, "the_date55",
    N("september_flag", 13, "September, in the file",
      ["The record's September pages complete the picture the two dates began: the original foster father's cardiac condition is documented in the file from September 15th — 'foster father under cardiology care; placement unit advised home may become unavailable; contingency planning recommended.' Recommended in September. Executed — nine days of it, ending at a county line with a bed already held — in late October. In the six weeks between the recommendation and the move, the file contains no kinship entry at all. Beatrice's name does not appear between March and your November filings.",
       "Six weeks of contingency planning that never once contingently planned for the child's aunt. Your counsel underlines nothing; she doesn't have to. The absence underlines itself."],
      [C("Two dates and one silence. Give all three to your counsel, in the order the file gives them.", "two_dates")]))
rw(s55, "the_date55", "two_dates", "september_flag")
ins(s55, "two_dates",
    N("supervisor_meet55", 15, "The supervisor, conceding early",
      ["The agency supervisor, at a meeting your counsel requests before the courtesy study becomes the case's second lost envelope, is more candid than her position paper: 'The kinship exploration in February and March was inadequate. I'll stipulate the call notes say what they say. What I need from December is a study I can act on — run Beatrice now, run her properly, and if she's approved, my recommendation will follow the study.'",
       "It is the sound of an institution correcting at the speed institutions do — slowly, verbally, and only after a record request has made the correction cheaper than the defense. Your counsel gets the substance into a letter the same day, because verbal concessions evaporate and letters don't."],
      [C("Convert the concession into the study's tracking: who sends the courtesy request, to whom, on what date.", "imani_program")]))
rw(s55, "two_dates", "courtesy_study", "supervisor_meet55")
ins(s55, "supervisor_meet55",
    N("imani_program", 16, "Your standing",
      ["Your own compliance gets its paragraph in the packet, and it is a good one: visits kept at a rate the transport log itself verifies (you showed up for all of them, including the shortened one); the program milestones met; your counsel's filings timely to the day. Standing in a placement fight is partly moral arithmetic — the parent who has done everything asked, on paper, gets to ask the court to hold the agency to the same standard — and your packet intends to ask exactly that.",
       "'We're not claiming perfection,' your counsel says. 'We're claiming symmetry. February asked things of Beatrice that February's mail never delivered. December should be more careful with everybody.'"],
      [C("The courtesy study request goes out. This time, your copy has a date stamp and a chaser: you.", "courtesy_study")]))
rw(s55, "supervisor_meet55", "courtesy_study", "imani_program")
ins(s55, "courtesy_study",
    N("county_capacity", 18, "The honest exhibit",
      ["Your counsel includes in the packet an exhibit that surprises the agency by helping it: the county's own placement-capacity report for October, showing zero available in-county beds for Zola's age group on the night of the move. She includes it deliberately. 'We concede the emergency and the bed map,' she tells you. 'Our case was never that a bed existed. It's that in nine days of planning — six weeks of documented warning — the kinship check that would have made the bed unnecessary was never run. Conceding what's true buys the right to be believed about what isn't.'",
       "It is the batch's recurring strategy in one paragraph: the strongest advocates are the ones whose concessions the court can rely on."],
      [C("Beatrice's clearances go in — hers, and her daughter's — while the study opens.", "beatrice_clearances")]))
rw(s55, "courtesy_study", "beatrice_study", "county_capacity")
ins(s55, "county_capacity",
    N("beatrice_clearances", 19, "Clearances, again from zero",
      ["Beatrice's clearances are filed with the grim comedy of a family doing a thing the second time as though it were the first: her prints, her daughter's prints (the daughter is the documented overnight adult on night-shift rotations), the child-abuse and state-police checks initiated with confirmation numbers Beatrice logs in the binder under a new sub-label: 'ZOLA — STUDY (SECOND ATTEMPT).'",
       "The worker assigned in Beatrice's county is new to the case and reads the summary's 'non-responsive' line in Beatrice's presence. Beatrice opens the binder to February without a word. The worker reads. 'I'll note the discrepancy in the study,' she says, in the tone of a person revising a professional opinion of her own office."],
      [C("Her interview is next — the study's heart. Be reachable; be nowhere near it. Studies interview households, not advocates.", "beatrice_interview")]))
rw(s55, "county_capacity", "beatrice_study", "beatrice_clearances")
ins(s55, "beatrice_clearances",
    N("beatrice_interview", 20, "Beatrice, interviewed",
      ["The study interview runs two hours and covers the territory studies exist to cover: discipline (hospital rules — explain, redirect, document); the night shifts (daughter documented, neighbor as backup, the binder as evidence of a household that plans); Zola's school (she has already called the old school about re-enrollment timing — the registrar knows her voice); and the question underneath all of them, asked plainly: 'Why you, why now?'",
       "'Because I was always the answer,' Beatrice says. 'February mailed it to the wrong conclusion. Ask the file — the real one, not the summary.' The worker writes it down. Workers write down the sentences that sound like the file agreeing with itself."],
      [C("The study proceeds to the home visit and the landlord letter. The report is weeks out; December is closer.", "beatrice_study")]))
ins(s55, "beatrice_study",
    N("daughter_plan", 23, "The overnight plan, documented",
      ["Beatrice's daughter — a grown woman with a toddler of her own, ten minutes away — formalizes her role in a signed care plan: the overnight adult on Beatrice's three weekly night shifts, her clearances attached, her own daughter's sleeping arrangement in the plan spelled out because plans that spell out the small people are the ones courts trust. The worker verifies it by interview and notes, in the study's margin, 'multi-adult support structure documented and interviewed.'",
       "Compare February, when the agency's whole knowledge of this family fit in the word 'non-responsive.' The distance between the file then and the file now is the scenario."],
      [C("One more document: Zola's old school, on re-enrollment. Get it in writing before the transmittal fight.", "school_letter55")]))
rw(s55, "beatrice_study", "transmittal", "daughter_plan")
ins(s55, "daughter_plan",
    N("school_letter55", 24, "Her seat in the circle",
      ["Zola's old school writes back within the week — the registrar and her teacher signing jointly, a bureaucratic duet: re-enrollment can be effected within days of a court order; her reading-group placement 'will be restored on return, the group having kept her role in the Friday reading-aloud rotation in her absence.' Someone at that school kept a chair in a circle for a child the system had mislaid across a county line. The letter goes into the packet where sentiment would go, except that it is not sentiment — it is an enrollment office's official position, and courts can order around it.",
       "You read the letter twice on the bus home. Then you turn to the study report's journey — the road where this case's paper has died before."],
      [C("Get the report's transmittal to the hearing county in writing, with a date.", "transmittal")]))
rw(s55, "daughter_plan", "transmittal", "school_letter55")
ins(s55, "transmittal",
    N("zola_weekend", 26, "The test weekend",
      ["Under the interim order, Zola spends a full weekend at Beatrice's before the review — the court testing the placement the way careful judges test all such placements: by letting it happen once, on paper, and reading the report. The report, filed by the agency's own visit supervisor, is three paragraphs of a child re-inhabiting her life: the binder toured, the bedroom claimed, the old school walked past 'to check it's still there,' and a Sunday collapse into sleep at 7 p.m., described by Beatrice as 'the tired of a kid who stopped holding her breath.'",
       "Weekend reports like this are the hearing's advance guard: they convert December's question from 'whether' toward 'why not.'"],
      [C("Zola's own counsel files her position this week. The packet completes itself around her words.", "zola_counsel")]))
rw(s55, "transmittal", "packet55", "zola_weekend")
ins(s55, "zola_weekend",
    N("zola_counsel", 27, "Zola's position",
      ["Zola's counsel files her position in the child's own priorities, translated but not improved: she likes the Riverton foster mother and wants to be able to say goodbye properly, 'not on a Thursday'; she wants her old school 'where the fish tank is not the best thing'; she wants Aunt Bea's house 'because it's ours and because Mom can walk there.' The filing also does counsel's sterner work: it opposes any further interim moves — 'this child has been transferred by adults' paperwork four times this year; the court's order should end the transfers, not schedule the next one.'",
       "Four transfers. Counted by her lawyer, in a filing, where December must read it."],
      [C("The Riverton foster mother's statement completes the voices. Then the packet closes.", "foster_statement55", addHidden=["child-voice"])]))
rw(s55, "zola_weekend", "packet55", "zola_counsel")
ins(s55, "zola_counsel",
    N("foster_statement55", 27, "The emergency home's statement",
      ["The Riverton foster mother's written statement is short, professional, and — for the agency's theory — fatal in its kindness: she confirms she accepted Zola as a thirty-to-sixty-day emergency placement; that her home is 'structured for transition, not tenure'; that Zola 'speaks of her aunt's home as her address and of mine as her visit'; and that in her experience 'this child has a placement waiting, and it isn't mine.' She will attend the review and say it under her § 6336.1 right to be heard.",
       "When the placement itself testifies that it was a bridge, a court needs a reason to make it a destination. The agency's position paper, arriving this week, will have to supply one."],
      [C("Read the agency's paper when it lands — it is the last document before December 3rd.", "packet55")]))
rw(s55, "zola_counsel", "packet55", "foster_statement55")
ins(s55, "packet55",
    N("agency_position_paper", 29, "The position paper",
      ["The agency's pre-review position holds the necessity line and concedes, in a subordinate clause you have to read twice to believe, that 'kinship exploration in the first quarter was not completed to standard.' It opposes immediate return on stability grounds — the honest core of its case: Zola has now been in Riverton six weeks; a second move is also a disruption; the court should weigh the child's present attachments.",
       "Your counsel marks the concession's page. 'They've given us February,' she says. 'Now they ask the court to forgive it for November's sake. Our answer is the weekend report and the school letter: the life she'd return to is not hypothetical. It's documented, enrolled, and has a chair kept in a circle.'"],
      [C("The night before the review: pack the binder, the log, the packet. Sleep like a litigant.", "night_before55")]))
rw(s55, "packet55", "review55", "agency_position_paper")
ins(s55, "agency_position_paper",
    N("night_before55", 30, "The night before",
      ["Beatrice lays out her binder's newest sub-label — 'ZOLA — REVIEW (DECEMBER)' — with the superstition of a nurse before a hard shift: clearances, study, care plan, the February pages copied and flagged. Your transport log is in your bag: nine round trips, four hundred ninety-five minutes each way's worth of a childhood in transit, itemized without a single adjective.",
       "Zola, by phone, gives her final instruction: 'If the judge asks about the fish tank, tell her it was a good fish tank. I don't want her thinking I lied about that part.' Eight-year-olds understand credibility better than most litigants. Nothing in your packet lies about anything, including the fish tank. That is its power."],
      [C("One call left: your counsel's final preparation, the morning of.", "pre_review_call55")]))
rw(s55, "agency_position_paper", "review55", "night_before55")
ins(s55, "night_before55",
    N("pre_review_call55", 30, "Posture",
      ["'Remember the posture,' your counsel says, on the courthouse steps call. 'We are not the prosecution of February. We are the family of December, with an approved aunt, a kept chair, a weekend report, and a file that corrects its own summary. The agency will ask the court to protect stability. We agree about stability. We simply brought evidence of where Zola's actually is.'",
       "It is the whole batch in one instruction: the record, corrected and complete, argued without adjectives. Beatrice comes up the steps with the binder under her arm like a shield that has learned to be a book."],
      [C("Go in. The binder, the two dates, the study, the child — in that order, the file walks into December.", "december_morning")]))
rw(s55, "night_before55", "review55", "pre_review_call55")
ins(s55, "pre_review_call55",
    N("december_morning", 31, "December 3rd, the hallway",
      ["The hallway outside the courtroom holds the case's entire cast in winter coats: Beatrice with the binder; Ms. Halvorsen with the file that now agrees with it; the Riverton foster mother, who drove fifty-five minutes — Zola's drive, reversed — to say four sentences in person; and you, with the transport log, whose arithmetic nobody will need to check because everybody in the hallway has lived it.",
       "The judge's clerk opens the door. The file goes in first, the way files do. Then the family."],
      [C("Hear the hearing run on documents — the February notes, the two dates, the approved aunt, the child's own words.", "review55")]))
rw(s55, "pre_review_call55", "review55", "december_morning")

# ---- S56 (+25 -> 42)
ins(s56, "start",
    N("folder_system", 0, "The folder",
      ["Your sponsor, watching you spread two envelopes across her kitchen table like a losing hand, issues the winter's first order: 'Folder. Sections. Dates on everything. Recovery runs on inventory, and so — apparently — does the county.' By evening the folder exists: APPEAL (your clock), GREGORY (his stall), LEV (visits and his file), in that order, because order is a form of hope you can manufacture.",
       "Every document this scenario produces goes into it with a date on its face. You do not yet know that the folder itself — its chronology, its completeness — will end up functioning as evidence of the thing the indicated report questions: whether you are a person who keeps track. Keep track."],
      [C("Sort the winter: the appeal clock first, in writing, while it is still cheap to stop.", "sort_winter")]))
rw(s56, "start", "sort_winter", "folder_system")
ins(s56, "sort_winter",
    N("lev_visit", 2, "Lev, at the visit",
      ["Lev, at Thursday's visit, is four years old and running a railroad across the visitation room carpet with the concentration of a tiny executive. His foster mother — kind, unhurried, the sort who sends photos through the agency without being asked — reports his current headlines: sleeping through; preschool going well; and a question he has begun asking at bath time: 'When is Uncle Greg's dog's turn?' Bruno, Gregory's ancient beagle, has been promised a supervisory role in Lev's life, and Lev intends to hold the adults to it.",
       "This is the stake under the paperwork: a four-year-old with a placement pending on a dog's turn, while two files miseducate the adults. File the appeal. Fix the name. The railroad is waiting."],
      [C("File the § 6341(a)(2) appeal this week — December, weeks inside the clock.", "appeal_filed")]))
rw(s56, "sort_winter", "appeal_filed", "lev_visit")
ins(s56, "appeal_filed",
    N("gregory_house", 4, "Gregory's half of the duplex",
      ["Gregory's home, walked in the same week, is a kinship placement in mid-assembly: the second bedroom painted a color Lev chose from a hardware-store swatch fan ('train blue'); a gate kit for the stairs still in its box because the study hasn't told him where gates go; Bruno asleep on a rug shaped like a bone, in flagrant violation of scale. Gregory's own room smells of sawdust and coffee. It is not a facility. It is an uncle's house with a four-year-old's name working its way into every room.",
       "'The hold letter's in the kitchen,' he says. 'I keep it where I can see it. It says my name and somebody else's life in the same paragraph. We're going to make them unwrite it.'"],
      [C("Unwriting starts with identifiers: his full name, his date of birth, the question of who else carries both.", "sponsor_talk")]))
rw(s56, "appeal_filed", "identifiers_ask", "gregory_house")
ins(s56, "gregory_house",
    N("sponsor_talk", 5, "The sponsor's rule",
      ["Your sponsor reviews your draft letter to the agency — the one demanding the identifiers behind Gregory's hold — and returns it with one line struck and one rule pronounced: 'No anger in ink. Anger fades; the letter stays, and someday a hearing officer reads your letters to decide who you are. Write like the person you're becoming, not the afternoon you're having.'",
       "The revised letter is four sentences: the hold's contents, the identifiers requested (full name, date of birth, report number), the correction sought, the response date asked. It is the least emotional document you have ever signed and, your counsel will later say, one of the most effective."],
      [C("Send it. The agency's answer will either be identifiers — or a silence you can also use.", "identifiers_ask")]))
rw(s56, "gregory_house", "identifiers_ask", "sponsor_talk")
ins(s56, "identifiers_ask",
    N("cousin_check", 7, "The cousin, documented",
      ["While the agency composes its answer, your family does its own records work the way families do — through your aunt, the unofficial registrar of everyone's everything. The cousin: Gregory M., two counties away, born two years earlier, a man whose 2011 you know of only as family weather ('trouble, back then'). Your aunt supplies the identifiers from a family Bible's flyleaf and an old reunion roster, and Gregory — whose stomach for this is thinner than yours — says the sentence that belongs in the file: 'I feel sorry for him too. But his report can't raise Lev. Mine has to be allowed to.'",
       "You send the identifiers to the agency as an exhibit to your request: the two men, side by side, distinguishable by every field a database keeps. Databases confuse what letters let them. Letters are how the confusion ends."],
      [C("The agency meeting follows. Get its commitments in writing — dates, names, transmittals.", "agency_meeting56")]))
rw(s56, "identifiers_ask", "correction56", "cousin_check")
ins(s56, "cousin_check",
    N("agency_meeting56", 8, "The meeting",
      ["Ms. Barlow, to her credit, runs the meeting like a person correcting her own office: the migration merge is explained (a name-only match accepted by a validation routine in 2024), the fix is itemized (source correction, re-run under full identifiers, study resumed, the erroneous summary recalled from every office that received it), and the timeline is given in dates rather than weather. Your counsel writes the dates down and reads them back, which is the ceremony by which agency timelines become commitments.",
       "'One more thing,' Ms. Barlow says, at the door, in the unofficial register. 'Tell your brother the hold letter should never have read like an accusation. The corrected one won't.'"],
      [C("Leave with the itemized fix in a follow-up letter — the correction, addressed to the file, transmitted everywhere the error went.", "correction56")]))
rw(s56, "cousin_check", "correction56", "agency_meeting56")
ins(s56, "correction56",
    N("db_holders", 10, "Everywhere the error went",
      ["The transmittal list, when the agency produces it, is the winter's quiet horror in list form: the wrong summary went to the county's placement unit, the study file, a contracted background-check vendor, and a state database extract. A name-only match, four destinations. The correction must make the same journey — each holder confirming receipt in writing — because a correction that reaches three of four holders is a rumor with good intentions.",
       "Gregory keeps the confirmations in a folder of his own now. 'My name, traveling with papers,' he says. 'Like it should have the first time.'"],
      [C("While his correction travels, build yours: your program's attendance record goes to your counsel for the appeal file.", "program_letter56")]))
rw(s56, "correction56", "records56", "db_holders")
ins(s56, "db_holders",
    N("program_letter56", 11, "Five months, one absence",
      ["Your program counselor's letter is the recovery's balance sheet: five months enrolled; attendance near-perfect with the single absence annotated (the ambulance day, which the letter handles in one clause and a hospital's corroboration); screens clean; phase advancement on schedule; and the counselor's closing assessment, written by a woman who has watched hundreds of parents from this exact chair: 'Ms. K. presents as a parent in active, documented recovery whose child is the stated center of her treatment planning.'",
       "It is not appeal evidence about the park. It is context evidence about you — and hearing officers, like all readers, judge the affidavit in front of them partly by the file around it. Your file is becoming the kind that helps."],
      [C("One more piece of your own evidence to gather before the investigation file arrives: the park itself, photographed.", "park_return")]))
rw(s56, "db_holders", "records56", "program_letter56")
ins(s56, "program_letter56",
    N("park_return", 13, "The park, photographed",
      ["Your counsel's investigator photographs the climbing structure on a gray December morning: its posted age rating (4–7 — Lev's exact bracket, in the manufacturer's plate), the sight lines from the pavilion where your neighbor fell, the distance from the structure to the path — twenty-one feet, measured, not the impressionistic geography of a narrative written afterward. Lev's stitches scar is not in the photographs. The structure that 'should have been supervised differently' stands in them looking like what it is: a playground doing its ordinary job, in a park full of parents making the same twenty-foot calculations every day.",
       "The photographs are not an argument. They are the scene, preserved, in case anyone later describes it from imagination."],
      [C("File the § 3130.44(d) request — both files, yours and the placement file, in one signature.", "records56")]))
rw(s56, "program_letter56", "records56", "park_return")
ins(s56, "records56",
    N("foster_mother56", 15, "Lev's foster mother",
      ["Lev's foster mother, at the January visit, delivers her own small report with the air of a woman filing a minority opinion in a case she supports: Lev is thriving; his questions about Bruno have achieved the status of a liturgy; and she has told the agency — in writing, she mentions, because she has learned from watching you — that 'this placement should end at his uncle's, on the uncle's readiness and not a day of database longer.'",
       "Foster parents' voices carry the § 6336.1 guarantee of notice and hearing, and hers will be in the review packet: the incumbent placement advocating for the kinship one. Files rarely contain a sentence that generous. Reviews notice when they do."],
      [C("One document in your own file needs chasing before the investigation record lands: Lev's hospital record, which you may request as his mother.", "hospital_records")]))
rw(s56, "records56", "page_eleven", "foster_mother56")
ins(s56, "foster_mother56",
    N("hospital_records", 16, "The hospital note, firsthand",
      ["Lev's emergency record, requested in your name as his mother, corroborates the investigation file's version in the hospital's own hand: 'laceration, forehead, nine sutures; no other injuries identified; child calm, consolable; mother present, appropriate, providing history.' You read 'appropriate' three times. In November, an adjective in a summary — 'distracted' — rearranged your legal life. In the primary record, another adjective has been sitting quietly, attached to the same afternoon, in the notes of people who were actually watching.",
       "This is the winter's method in miniature: summaries argue; records testify. Your appeal now has both adjectives, with provenance. The investigation file, when it arrives, will add a third voice — the attendant's."],
      [C("The investigation file lands this week. Read it whole — including page eleven.", "page_eleven")]))
rw(s56, "foster_mother56", "page_eleven", "hospital_records")
ins(s56, "page_eleven",
    N("narrative_vs_file", 19, "Summary vs. file",
      ["Your counsel builds the appeal's skeleton as a two-column document — 'What the summary says' against 'What the agency's file says' — and the columns do not behave like opponents; the second reads like the first one's correction. Summary: 'mother distracted, child unsupervised on structure.' File: mother twenty feet away rendering aid; attendant present and nearer; structure age-appropriate; hospital: mother appropriate. Summary: 'worker responded to scene.' File: the attendant's statement collected November 12th; the summary written November 20th, without it.",
       "'Act 119 exists for this document,' your counsel says. 'The burden is theirs, the evidence is theirs, and the exculpatory piece was in their drawer. We don't have to prove you're perfect. We have to make them prove the report — with their own paper, out loud, in order.'"],
      [C("Subpoena the attendant if he won't come willingly. Then prepare the hearing like the evidence exam it is.", "hearing_prep56")]))
rw(s56, "page_eleven", "hearing_prep56", "narrative_vs_file")
ins(s56, "hearing_prep56",
    N("attendant_interview", 24, "The attendant, interviewed",
      ["The parks attendant — a retired school janitor named on page eleven — agrees to testify without a subpoena, which your counsel notes is what happens when a witness is telling a story he has already signed once. His account, in the investigator's notes, matches his statement in every particular and adds the one detail memory kept for the hearing: 'She hollered over — “Eyes on him a second, love” — when she went to the lady who fell. That's not distracted. That's a handoff. I've seen a thousand of them.'",
       "A handoff. The word enters the appeal file and stays there, doing the work that adjectives do when they come from witnesses instead of summaries."],
      [C("January's visits continue while the tracks run. Attend everything. The file is watching you back, in the good way now.", "january_visit")]))
rw(s56, "hearing_prep56", "hearing56", "attendant_interview")
ins(s56, "attendant_interview",
    N("january_visit", 30, "January visits",
      ["Lev's January visits acquire a companion: Gregory now attends the second half, with the agency's blessing — the kinship study's resumption has made him a person in the case again — and Bruno attends once, ceremonially, in the parking lot, where Lev conducts a thorough inspection and files his approval by attempting to ride him. The foster mother's log of these visits, which she keeps with a diarist's care, records 'child's transition behaviors: none noted; child treats uncle's presence as furniture — the good kind.'",
       "Transition is the science the review will ask about, and it is being rehearsed weekly, on the record, by the incumbent placement herself. Some files argue. This one demonstrates."],
      [C("Gregory's study formally restarts — the home visit redone, under his own file number this time.", "study_restart")]))
rw(s56, "attendant_interview", "hearing56", "january_visit")
ins(s56, "january_visit",
    N("study_restart", 36, "The study, restarted",
      ["Gregory's re-run home visit is conducted by a worker who opens with the correction — 'For the record: this study concerns Gregory T., born [his year], of this address' — and the recitation, absurd and necessary, makes Gregory laugh in his own kitchen for the first time since November. The visit itself is thorough and brief: the train-blue room, the gate installed (he did not wait to be told where gates go), Bruno's vaccination records produced from a folder labeled with a carpenter's precision.",
       "'Your brother keeps folders now too,' the worker observes. 'It's spreading through the family,' Gregory says. 'We're calling it the winter.'"],
      [C("His references are called the following week. Answer your phone; so does everyone who loves Lev.", "gregory_references")]))
rw(s56, "january_visit", "hearing56", "study_restart")
ins(s56, "study_restart",
    N("gregory_references", 39, "References",
      ["The references speak in the order the study calls them: the pastor (Gregory tithes in carpentry — the church's ramp, the food bank's shelves); two clients (a kitchen, a nursery — 'he built the room his own kids were rocked in; he'd build Lev's right'); your mother by phone from Arizona, who provides the family's closing argument in grandmother form: 'Both my children are in your files this winter. One of them is recovering out loud. The other never did anything but share a name with trouble. Kindly sort your papers.'",
       "Reference calls are a study's oral tradition — unscripted, unrehearsed, and for that reason believed. Gregory's assemble into a man the corrected file finally describes accurately."],
      [C("Meanwhile, your indicated report collects its own winter interest: a job answer arrives that has nothing to do with the hearing.", "katya_work")]))
rw(s56, "study_restart", "hearing56", "gregory_references")
ins(s56, "gregory_references",
    N("katya_work", 42, "The report, at work",
      ["The preschool-assistant job you applied to in December — the one your recovery plan counted as a milestone — answers in January with the indicated report's practical voice: the required child-abuse clearance cannot issue while the report stands indicated; the position goes to another candidate. The letter is polite. Politeness does not pay the rent the job would have.",
       "You file the letter in the APPEAL section of the folder, because it belongs to the appeal's true accounting: an indicated report is not an abstraction awaiting a hearing. It is a fact that interviews you at every application, every program, every background check, until a hearing officer rules. The stakes of January 27th now include a sentence about your employability that no one has to explain to you twice."],
      [C("One more document arrives for the folder before the hearing: the ChildLine registry's own statement of what your status means.", "childline_letter")]))
rw(s56, "gregory_references", "hearing56", "katya_work")
ins(s56, "katya_work",
    N("childline_letter", 45, "What 'indicated' means, on paper",
      ["The registry's status letter is bureaucratically serene: your report's status, its category, the review and appeal rights recited like a weather report for a climate you're living in. You read it with your counsel at the final prep, and she does the lawyer's kindness of translating its coldest line: the report will remain as it stands unless the appeal changes it — aging out is measured in years and decades, not in the seasons of a recovery or a childhood.",
       "'Then January 27th isn't a formality,' you say. 'It was never going to be,' she says. 'It's the only room where the report has to defend itself. That's Act 119's whole point — make it come to a hearing and carry its proof.'"],
      [C("The eve of the hearing: folder closed, witness confirmed, Gregory briefed on where to sit and when to be furniture.", "hearing_eve")]))
rw(s56, "katya_work", "hearing56", "childline_letter")
ins(s56, "childline_letter",
    N("hearing_eve", 48, "The eve",
      ["The night before the hearing, Gregory cooks — badly, cheerfully, with Bruno supervising from the rug — and the family's war council consists of your sponsor's rule recited like grace: no anger in ink, and none in testimony either; the file will do the arguing. Your counsel's last text is a litigator's blessing: 'Their burden. Our paper. Sleep.'",
       "You sleep the way appellants sleep, which is in chapters, and wake to a gray morning with the folder by the door — APPEAL, GREGORY, LEV — in the order the winter taught you."],
      [C("January 27th. Bring the file. Bring Gregory. Make them carry it.", "hearing56")]))
rw(s56, "childline_letter", "hearing56", "hearing_eve")
ins(s56, "confirm56",
    N("gregory_gate", 73, "The gate, installed",
      ["February 18th arrives with the study's completion and Gregory's gate finally out of its box — installed at the top of the stairs by its purchaser in an afternoon, inspected by the study's closing visit, and noted in the approval with a bureaucrat's restraint: 'Safety gate installed; home meets standards without conditions.' Bruno has been trained, by Lev's proxy (a stuffed dog of similar vintage), to wait at the gate rather than besiege it. Two species are now ready for the placement.",
       "The approval letter goes into the GREGORY section with its confirmations: corrected summary at the front, the wrong one behind it, the file's memory of its own error preserved the way your counsel advised — visible, answered, and harmless at last."],
      [C("The approval must reach the court file before March 12th. Transmit it with confirmation — the winter's last errand of the kind.", "study_addendum")]))
rw(s56, "confirm56", "decision56", "gregory_gate")
ins(s56, "gregory_gate",
    N("study_addendum", 76, "Transmitted, confirmed",
      ["The approval's transmittal to the court file is confirmed in writing within the week — the agency's letter, the clerk's stamp, your counsel's copy, a small trinity of paper that six months ago would have seemed like overkill and now reads as hygiene. Gregory's track is complete: the right man, his own identifiers, an unconditional approval, a court file that contains all three facts.",
       "What remains is a mailbox in Harrisburg, a decision within its statutory window, and the March 12th review assembling both files at last."],
      [C("Your counsel calls once, for the record, to confirm the decision is pending issuance. Then the waiting ends the way it ends.", "decision_call")]))
rw(s56, "gregory_gate", "decision56", "study_addendum")
ins(s56, "study_addendum",
    N("decision_call", 85, "Issued",
      ["'It's issued,' your counsel says, on a Tuesday call you take standing in the bakery aisle for no reason your legs can explain. 'It's in the mail. I don't have the text yet — decisions come to the parties on paper, which this winter has taught us to respect and resent in equal measure. Do not read it alone in a parking lot. Read it at your sponsor's table, with Gregory, and then call me.'",
       "March 5th. Two envelopes from Harrisburg are in your mailbox. You drive them, unopened, to your sponsor's kitchen, where Gregory is already waiting with Bruno's leash still in his hand from the walk over."],
      [C("Open them — at the table, with your people, the way the winter taught you to do everything else.", "decision56")]))
rw(s56, "study_addendum", "decision56", "decision_call")
ins(s56, "decision56",
    N("march_packet", 90, "The review packet",
      ["Your counsel assembles the March 12th packet in the order a judge's morning prefers: the hearing officer's decision (whatever it holds); Gregory's approval, corrected file and all; the foster mother's letter advocating the placement; the visit logs showing a four-year-old already rehearsing his uncle's household; and your program record, five months becoming six, the trajectory underneath everything.",
       "'Whatever the decision says,' she tells you, 'this packet is the truest file this family has ever had in a courthouse. True files are not guarantees. They are the ground guarantees are built on, when they come.'"],
      [C("Ms. Barlow confirms the agency's recommendation by phone. Hear it before the courtroom does.", "barlow_call")]))
rw(s56, "decision56", "outcome56", "march_packet")
ins(s56, "march_packet",
    N("barlow_call", 92, "The agency's recommendation",
      ["Ms. Barlow's call is careful in the way of a worker who has corrected her own file once this winter and intends the correction to stand: the agency will recommend placement with Gregory at the review — his approval is unconditional, the transition is documented, the incumbent foster parent concurs. On your report, the agency's position follows the hearing officer's decision, 'as it should.' The institution that wrote both files' errors will walk into March carrying both corrections. It is not redemption. It is what accountability looks like at caseworker scale: specific, documented, and filed.",
       "You thank her, and write it down, and date it — the folder's last entry before the review."],
      [C("Call Gregory. Tell him the recommendation, the date, and that Bruno should expect inspection by a four-year-old with standards.", "gregory_call56")]))
rw(s56, "march_packet", "outcome56", "barlow_call")
ins(s56, "barlow_call",
    N("gregory_call56", 93, "Telling Gregory",
      ["Gregory receives the news the way carpenters receive measurements — twice, to be sure. 'Placement recommended. March 12th. And my name — spelled with the T, in the right file?' 'With the T,' you confirm, 'in the right file, in front of the wrong one, forever, as a warning to databases.' He is quiet a moment. 'Then I'll paint the gate,' he says. 'Train blue. He'll want it matching the room.'",
       "The winter ends the way it ran: in documents confirmed aloud, between two siblings, over a phone line — with a dog asleep on a rug and a gate about to change color."],
      [C("March 12th. Both files, one courtroom, one four-year-old's address.", "outcome56")]))
rw(s56, "barlow_call", "outcome56", "gregory_call56")

# ============================================================ EMIT
SCEN = [
    (47, s47_meta, s47), (48, s48_meta, s48), (49, s49_meta, s49),
    (50, s50_meta, s50), (51, s51_meta, s51), (52, s52_meta, s52),
    (53, s53_meta, s53), (54, s54_meta, s54), (55, s55_meta, s55),
    (56, s56_meta, s56),
]

def effect_str(c):
    parts = []
    if c.get("cash"):
        parts.append(f"cash {'+' if c['cash'] > 0 else '−'}{abs(c['cash'])}")
    for f in c.get("setFlags", []):
        parts.append(f"FLAG: {f}")
    for h in c.get("addHidden", []):
        parts.append(f"HIDDEN + {h}")
    for f in c.get("requiresFlags", []):
        parts.append(f"REQUIRES: {f}")
    for f in c.get("requiresNoFlags", []):
        parts.append(f"REQUIRES-NOT: {f}")
    return "; ".join(parts)

def emit(n, meta, raw, start):
    data = build(meta, raw, start)
    json_path = f"{GAME_DIR}/scenario-{n}.json"
    with open(json_path, "w") as f:
        json.dump(data, f, indent=2)
    L = []
    L.append(f"# {meta['subtitle'].split('— ', 1)[1]} — Node-for-Node Script (Scenario {n})")
    L.append("")
    L.append(f"Scenario {n} of *The First 90 Days* — script generated node-for-node from `scenario-{n}.json`; the JSON is the source of truth.")
    L.append("")
    L.append("A fictional composite built from published Pennsylvania dependency practice and documented system patterns. Not a real family's case.")
    L.append("")
    L.append("**Content note:** child removal, court hearings, family separation.")
    L.append("")
    L.append("**How to read effects:** `cash` is money spent or received at that choice; `FLAG:` marks a fact the story remembers; `HIDDEN +` is an assessment item the player never sees scored; `REQUIRES:` gates a choice on an earlier fact; `NOTE:` is authorial, not spoken in-world. Endings are marked **Ending.** with a **Debrief:**.")
    L.append("")
    L.append(f"**Start date:** {fmt(start)}. **Tier:** {meta['tier']}. **Start cash:** ${meta['startCash']}.")
    L.append("")
    L.append("---")
    for nd in data["nodes"]:
        L.append("")
        L.append(f"## [{nd['id']}] {nd['title']}")
        L.append("")
        L.append(f"*{nd['kicker']}*")
        if nd.get("ending"):
            L.append("")
            L.append("**Ending.**")
            for p in nd["debrief"]:
                L.append("")
                L.append(f"**Debrief:** {p}" if p is nd["debrief"][0] else p)
        else:
            for p in nd["body"]:
                L.append("")
                L.append(p)
            L.append("")
            L.append("**Choices:**")
            for c in nd["choices"]:
                fx = effect_str(c)
                line = f"- {c['text']} → **{c['next']}**"
                if fx:
                    line += f"  _({fx})_"
                L.append(line)
                if c.get("note"):
                    L.append(f"  - NOTE: {c['note']}")
    script_path = f"{GAME_DIR}/scenario-{n}-script.md"
    with open(script_path, "w") as f:
        f.write("\n".join(L) + "\n")
    ends = sum(1 for nd in data["nodes"] if nd.get("ending"))
    print(f"scenario {n}: {len(data['nodes'])} nodes, {ends} endings, tier {meta['tier']}")

STARTS = {47: date(2026, 3, 9), 48: date(2026, 4, 6), 49: date(2026, 2, 16),
          50: date(2026, 5, 4), 51: date(2026, 6, 1), 52: date(2026, 8, 3),
          53: date(2027, 1, 4), 54: date(2026, 10, 5), 55: date(2026, 11, 2),
          56: date(2026, 12, 7)}
for n, meta, raw in SCEN:
    emit(n, meta, raw, STARTS[n])
print("done")
