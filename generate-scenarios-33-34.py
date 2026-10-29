#!/usr/bin/env python3
"""Generator for Scenarios 33 and 34 of 'The First 90 Days'.
One data source emits both the .json and the -script.md for each scenario,
so they match node-for-node by construction. Dates/kickers are computed
with datetime; ASFA 15-month dates are computed by calendar-month addition
and asserted in-code."""
import json, os
from datetime import date, timedelta

OUT = os.path.dirname(os.path.abspath(__file__))

def add_months(d, months):
    m = d.month - 1 + months
    y = d.year + m // 12
    m = m % 12 + 1
    # day clamping (our chosen days are all <= 28-safe except June 2 / March 2)
    days_in = [31, 29 if (y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)) else 28,
               31, 30, 31, 30, 31, 31, 30, 31, 30, 31][m - 1]
    return date(y, m, min(d.day, days_in))

def fmt(d):
    return d.strftime("%A, %B ") + str(d.day) + d.strftime(", %Y")

def C(text, nxt, **kw):
    c = {"text": text, "next": nxt}
    c.update(kw)
    return c

def N(nid, off, title, body, choices=None, ending=False, debrief=None):
    n = {"id": nid, "dayOffset": off, "title": title, "body": body}
    if ending:
        n["body"] = []
        n["ending"] = True
        n["debrief"] = debrief
    else:
        n["choices"] = choices
    return n

def build(meta, nodes, start):
    for n in nodes:
        d = start + timedelta(days=n["dayOffset"])
        n_full = {"id": n["id"],
                  "kicker": f"Day {n['dayOffset']} \u2014 {fmt(d)}",
                  "dayOffset": n["dayOffset"], "title": n["title"],
                  "body": n["body"]}
        if n.get("ending"):
            n_full["ending"] = True
            n_full["debrief"] = n["debrief"]
        else:
            n_full["choices"] = n["choices"]
        n.clear(); n.update(n_full)
    return {"meta": meta, "nodes": nodes}

def emit(scen, num, title_line, content_note, start):
    path_j = os.path.join(OUT, f"scenario-{num}.json")
    with open(path_j, "w") as f:
        json.dump(scen, f, indent=1, ensure_ascii=False)
    L = []
    L.append(f"# THE FIRST 90 DAYS \u2014 Scenario {num}: \u201c{title_line}\u201d")
    L.append("")
    L.append(f"*Human-readable script. This document and `scenario-{num}.json` are generated "
             "from a single source and match node-for-node: same IDs, same order, same choices, same effects.*")
    L.append("")
    L.append("**The family is fictional \u2014 a composite. No real person's story appears here.**")
    L.append("")
    L.append(f"**Content note:** {content_note}")
    L.append("")
    L.append("**How to read effects:** `cash \u221240` changes the player's cash. `FLAG: name` sets a flag "
             "the engine tracks. `HIDDEN + item` means the case file quietly records that item at this "
             "choice \u2014 the player does not see it when it happens. `NOTE:` is text shown to the player right after choosing.")
    L.append("")
    L.append(f"Start date: {fmt(start)}. Day offsets are days since the scenario's start date.")
    for n in scen["nodes"]:
        d = start + timedelta(days=n["dayOffset"])
        L.append("")
        L.append(f"## [{n['id']}] {n['title']}")
        L.append(f"*{n['kicker']} \u2014 {fmt(d)} (dayOffset {n['dayOffset']})*")
        for p in n["body"]:
            L.append("")
            L.append(p)
        if n.get("ending"):
            L.append("")
            L.append("**Ending.**")
            L.append("")
            L.append("**Debrief:**")
            for item in n["debrief"]:
                L.append(f"- {item}")
        else:
            L.append("")
            L.append("**Choices:**")
            for c in n["choices"]:
                ann = []
                if "cash" in c:
                    ann.append(f"cash {'\u2212' + str(-c['cash']) if c['cash'] < 0 else '+' + str(c['cash'])}")
                if c.get("setFlags"):
                    ann.append("FLAG: " + ", ".join(c["setFlags"]))
                if c.get("addHidden"):
                    ann.append("; ".join("HIDDEN + " + h for h in c["addHidden"]))
                suffix = f"  _({'; '.join(ann)})_" if ann else ""
                L.append(f"- {c['text']} \u2192 **{c['next']}**{suffix}")
                if c.get("note"):
                    L.append(f"  - NOTE (shown after choosing): {c['note']}")
    path_m = os.path.join(OUT, f"scenario-{num}-script.md")
    with open(path_m, "w") as f:
        f.write("\n".join(L) + "\n")
    return path_j, path_m

# =====================================================================
# SCENARIO 33 \u2014 The Two Petitions
# Placement: Monday, June 2, 2025. Story opens Monday, May 4, 2026
# (eleven months in). ASFA 15-month date: June 2, 2025 + 15 calendar
# months = Wednesday, September 2, 2026 = dayOffset 121 (asserted).
# =====================================================================
S33_START = date(2026, 5, 4)
S33_PLACED = date(2025, 6, 2)
S33_ASFA = add_months(S33_PLACED, 15)
assert S33_ASFA == date(2026, 9, 2), S33_ASFA
assert (S33_ASFA - S33_START).days == 121

s33_nodes = [
N("start", 0, "Eleven Months In", [
 "Eleven months ago your daughter Wren, who is seven, was placed in foster care. The reasons belong to a hard year: a lost apartment, shifts that did not line up with childcare, and a winter you managed badly and have been repairing, on paper and in person, ever since.",
 "Here is the repair, as the file currently tells it. You are Marcus, a forklift operator on the early shift. Your apartment is stable. Your screens are clean. Visits with Wren run twice a week and have grown longer. Your parenting program stands at nine sessions of twelve. You are, in the plan's own rating word, progressing \u2014 unevenly, and really.",
 "Wren lives with the Hartleys, who are kind, who send her school drawings home in her visit bag, and who have told the agency they would adopt her if adoption ever became the plan. Nobody has said that sentence to you yet. It is in the file anyway.",
], [C("Open the mail that came while you were at work", "motion_notice",
      note="One envelope is from your lawyer. One is from the agency. They are about the same hearing.")]),

N("motion_notice", 4, "A Second Envelope", [
 "The agency's letter is short and procedural. At the next permanency review it will ask the court to change Wren's goal away from reunification \u2014 toward adoption.",
 "Nothing in the letter says your services stop. Nothing in it says your visits change. It asks for a different finish line while you are still running toward the first one, and it does not explain, in parent-sized language, how a person is supposed to run toward two finish lines at once.",
 "Your lawyer's letter is one line: \u201cCome in Tuesday. Bring your folder. We need to talk about tracks.\u201d",
], [C("Call her office and ask for the earliest appointment", "lawyer_map",
      note="Tuesday, nine o'clock. She says the word 'tracks' again, like it is the whole appointment.")]),

N("lawyer_map", 8, "Two Tracks on One Whiteboard", [
 "Your lawyer, Ms. Osei, was appointed for you at the start of this case, as the law provides (42 Pa.C.S. \u00a7 6337). She draws two lines on her whiteboard, one above the other, and labels them in marker.",
 "\u201cTrack A is the case you know: finish the plan the court ordered, and the court reviews whether Wren can come home. Track B is new: a goal-change track, heading toward a different future. From today, both tracks run at the same time. Evidence you build on Track A is also, whether anyone says so or not, evidence on Track B.\u201d",
 "\u201cAnd under both lines there is a clock. Wren was placed on June 2, 2025. Fifteen of the most recent twenty-two months arrives on Wednesday, September 2, 2026. At that point the federal law presses the agency to file a petition to end parental rights \u2014 unless an exception is documented. Relative care. A documented compelling reason. Or this one, so remember it: the agency has not provided services the plan identified as necessary for Wren to come home safely (42 U.S.C. \u00a7 675(5)(E)). Our work, all summer, is to make the record on Track A so current, and the exceptions so documented, that Track B has nowhere honest to go.\u201d",
], [C("Ask what you do differently, starting this week", "class_night",
      addHidden=["Counsel's map \u2014 Track A (finish the plan) and Track B (goal change) run at the same time; ASFA date September 2, 2026"],
      note="\u201cYou attend everything. You file your progress instead of just making it. And at every hearing, you ask which track a piece of evidence belongs to.\u201d")]),

N("class_night", 12, "Track A, Night Class", [
 "Session ten of twelve. The parenting program meets in a church basement that smells of coffee and floor wax, and tonight's topic \u2014 routines a seven-year-old can count on \u2014 is one you could now teach parts of.",
 "Your supervisor has offered overtime tonight that would cover most of a month's electric bill. The sign-in sheet is by the door. In this system, the sign-in sheet is not a formality. It is the difference between a session that happened and a session that, months from now, a summary can describe either way.",
], [C("Stay for the session and sign in, as always", "written_progress",
      addHidden=["Parenting program \u2014 session 10 of 12 attended, signed in"],
      note="The overtime goes to someone else. The signature stays in the file."),
    C("Take the overtime \u2014 one missed session, explained later, should be fine", "written_progress", cash=40,
      addHidden=["Parenting program \u2014 session 10 missed for overtime; no note filed"],
      note="It probably will be fine. 'Explained later' is a promise you are making to a file.")]),

N("written_progress", 16, "Say It in Writing", [
 "Ms. Osei has a rule she repeats until parents repeat it back: progress that is only spoken is weather; progress that is filed is climate.",
 "Your class facilitator will confirm your attendance if anyone asks. Your landlord will confirm your tenancy if anyone asks. Your screen provider sends results to the agency on its own schedule. Almost everything true about your summer is currently waiting for someone to ask.",
 "There is a one-page form for a parent's written progress statement. It goes into the court file, where summaries are later written from.",
], [C("File the written progress statement this week, with certificates attached", "records_beat",
      setFlags=["writtenProgress"],
      addHidden=["Parent's written progress statement filed, with certificates"],
      note="Dated, copied, filed. Your summer, in your words, where the judge's summer will be written from."),
    C("Keep it verbal \u2014 your caseworker knows how you're doing", "records_beat",
      note="She does. Caseworkers, as this whole series keeps showing, are not the file's only readers, or its last ones.")]),

N("records_beat", 20, "The File, Including the Form", [
 "Ms. Osei reminds you of the quieter right, the one that does not depend on any hearing: you may request your own case record from the county agency, and under the regulation it \u201cshall be released upon request\u201d (55 Pa. Code \u00a7 3130.44(d)). She is specific about asking for the whole of it, including the full assessment \u2014 the form itself, the item ratings, and the outcome \u2014 and not only the summary pages.",
 "She adds the honest limit she always adds about the assessment: an earlier disclosure rule for the adjudication phase (Pa.R.J.C.P. 1340(B)(1)) exists, but whether it reaches every scored item of an assessment form is untested. The direct record request does not depend on that question. She intends to make it either way.",
 "The request is one page. The stamp is one stamp.",
], [C("Sign and send the request this week", "file_arrives",
      setFlags=["recordsRequested"],
      note="A stamp, a date, a copy for your folder. The cheapest power in this whole system."),
    C("Wait \u2014 one fight at a time; the goal-change hearing is the fight", "no_file",
      note="Understandable. The file will still be written this summer. It will simply be written without your reading it.")]),

N("file_arrives", 27, "The Referral That Reads 'To Be Sent'", [
 "The packet is thick, and partly blacked out, and still: there it is. Your ratings, climbing. The visit notes, warm and specific. The assessment form itself, its items and ratings plainer than you feared and more ordinary: supervision, housing stability, follow-through.",
 "And on the service plan's second page, a line you read three times. A referral for coached visits \u2014 the service the plan itself described as the step that would move your visits toward unsupervised time \u2014 marked, in the month Wren had been in care six months: \u201cReferral \u2014 to be sent.\u201d There is no send date. There is no follow-up note. The step your progress was measured against was never actually offered to you.",
 "You sit with that a while. It is not a villain's act. It is a box, in an office, that nobody checked. Boxes like that, unchecked, have decided cases.",
], [C("Take the page to Ms. Osei before you do anything else", "visits_rhythm",
      setFlags=["servicesGapFound"],
      addHidden=["Service plan \u2014 coached-visit referral marked 'to be sent,' month 6; never sent"],
      note="\u201cDon't be angry in September,\u201d she says. \u201cBe documented in September.\u201d")]),

N("no_file", 27, "Working from Summaries", [
 "Without the file, you and Ms. Osei work from the court reports \u2014 which are fair, and warm about your visits, and summaries all the same.",
 "A summary tells you what its writer thought mattered. It does not show you the plan's second page, or what any box on it says, or whether the step you were measured against was ever actually offered. You prepare for September with a good map of everything except the ground.",
], [C("Prepare anyway \u2014 your attendance and your visits are real, file or no file", "visits_rhythm",
      note="They are real. September will be conducted, as these hearings are, in documents.")]),

N("visits_rhythm", 31, "Saturday with Wren", [
 "Saturday visits have a rhythm now: the library first, then the park, then the long goodbye at the Hartleys' door that Wren has started managing by assigning you homework \u2014 a drawing to finish, a chapter to read so you can discuss it.",
 "Mrs. Hartley mentions, kindly, that the agency has asked them about \u201cpermanency paperwork.\u201d She does not use the word adoption. She is being careful with you, and you can feel the care and the paperwork in the same sentence.",
 "This is Track B, arriving not in a courtroom but at a front door, in a kind voice.",
], [C("Ask, just as kindly, what paperwork \u2014 and write down her answer, dated, that evening", "school_form",
      addHidden=["Visit note \u2014 foster family asked about 'permanency paperwork'; answer recorded, dated"],
      note="Not an argument. A record. The two tracks are now visible in the same week, in your own handwriting."),
    C("Let the sentence pass \u2014 Saturday is Wren's, not the case's", "school_form",
      note="Most of Saturday is hers. That is the point of Saturday. The sentence, unwritten, goes where unwritten sentences go.")]),

N("school_form", 34, "The School Form", [
 "Wren's school needs a form signed about who may collect her \u2014 a small, ordinary piece of parent work that currently requires three people's signatures and a call to the agency.",
 "Filling it in, you notice the form has two boxes for the future: the address she lives at now, and a line for \u201cchanges expected this year.\u201d You leave the second line for the school counselor to see, and she looks at it a moment before she files it.",
 "\u201cEveryone's planning something for this kid,\u201d she says, not unkindly. \u201cIt's good she has people planning.\u201d",
], [C("Ask the counselor to keep your updated contact page with the form", "two_timelines",
      note="One more current page in one more file. Current is a strategy, not a personality trait.")]),

N("two_timelines", 38, "Two Timelines, Side by Side", [
 "Ms. Osei drafts, on one page, the document she calls the summer's spine: two timelines, side by side. On the left, Track A \u2014 your sessions, screens, visits, tenancy, each with its date and its proof. On the right, Track B \u2014 the motion, the hearing date, and at the bottom of the right-hand column, in the same size type as everything else: September 2, 2026, fifteen months.",
 "\u201cJudges should not have to assemble this from a pile,\u201d she says. \u201cWe hand it up assembled. Every hearing from now on, we ask that the two timelines be stated on the record, side by side, so no one can describe your case using only one of them.\u201d",
], [C("Ask her to file the two-timeline page with the court now, not in September", "referral_call",
      setFlags=["timelineFiled"],
      addHidden=["Two-timeline statement filed \u2014 Track A progress and Track B clock on one page"],
      note="Filed in spring light, it becomes part of the record every later summary must reckon with."),
    C("Keep it as a hearing exhibit only \u2014 no need to show your hand early", "referral_call",
      note="Ms. Osei shrugs professionally. \u201cA record filed early corrects other records. An exhibit corrects one afternoon.\u201d")]),

N("referral_call", 45, "Chasing the Referral, on Paper", [
 "There is a step available that costs nothing but nerve: ask the agency, in writing, about the coached-visit referral \u2014 the one the plan called necessary \u2014 and ask that it be made now.",
 "If you learned of the gap from your own file, the letter can cite the plan's page and its empty box. If you did not, the letter is still worth sending in its general form: please confirm each referral the plan promised, with its send date. Either way, the answer \u2014 or the silence \u2014 becomes part of the record, dated.",
 "A phone call would be friendlier. A phone call would also, by autumn, be a memory two people remember differently.",
], [C("Send the letter \u2014 polite, dated, specific, with a copy for the court file", "shift_conflict",
      setFlags=["gapLetter"],
      addHidden=["Parent's letter \u2014 owed referral identified by date; agency asked to make it and confirm in writing"],
      note="Short, dated, factual. Let the file correct itself out loud."),
    C("Raise it by phone at the next check-in instead", "shift_conflict",
      note="Your caseworker says she'll look into it, and means it. The file records neither the asking nor the answer.")]),

N("shift_conflict", 52, "The Overtime Shift", [
 "Session eleven falls on the same evening as a double shift that would pay time-and-a-half \u2014 real money, in a summer when the car has begun making a noise you are budgeting around.",
 "A coworker offers a trade: he will take your Saturday warehouse shift if you take his Sunday. The class stays attended; the weekend gets shorter; the money gets smaller. Every option in this scene is defensible. Only one of them is a signature on a sign-in sheet.",
], [C("Make the trade and attend session eleven", "progress_review", cash=-30,
      addHidden=["Parenting program \u2014 session 11 of 12 attended, signed in"],
      note="Eleven of twelve. The pattern, in ink, is starting to look like the parent you are describing."),
    C("Take the double shift and miss session eleven", "progress_review", cash=50,
      addHidden=["Parenting program \u2014 session 11 missed; reason not filed"],
      note="The money is real. So, in September, will be the summary's way of counting.")]),
]

s33_nodes += [
N("progress_review", 59, "The Interim Review", [
 "The interim permanency review is short, and mostly Track A: your attendance, your screens, your visits, the plan's rating word \u2014 progressing \u2014 said aloud by the agency's own witness.",
 "Then the agency's lawyer, in the tone of a person reading a train schedule, notes for the record that the goal-change request remains pending for September, and that the fifteen-month date arrives the same week.",
 "Two cases, one child, one courtroom, described sixty seconds apart as if they were about different families.",
], [C("Watch Ms. Osei, and let her do the thing you prepared", "which_track",
      note="She stands. This is the beat the whole summer has been rehearsing.")]),

N("which_track", 66, "Which Track Does That Belong To?", [
 "Ms. Osei asks, on the record, a question so plain it sounds procedural: when the agency describes your progress as \u2018progressing,\u2019 which track is that evidence on \u2014 and when it describes the calendar as pressing, which track is that on? And may the record show the two timelines side by side, as filed?",
 "The judge says yes. Court reporters write down what judges say yes to. From today, the official story of your case has two columns in it, and anything said about one column can be answered from the other.",
 "Your caseworker catches your eye on the way out and says, honestly: \u201cI do the services side. The goal side comes from above me.\u201d You believe her. Both things she said are now, in different ways, on the record.",
], [C("Thank her \u2014 and keep attending the services side as if it were the whole case", "screens_filed",
      addHidden=["Hearing record \u2014 two timelines stated side by side; progress evidence assigned to both tracks"],
      note="Because stopping, now, would be read as surrender on both tracks at once."),
    C("Ask her, in the hallway only, whether she personally supports the goal change", "screens_filed",
      note="She looks at the floor. \u201cI'm the services side,\u201d she says again. Hallways are not the record. You knew that; now you know you know it.")]),

N("screens_filed", 70, "Clean Screens, Filed", [
 "Your screen results for the summer arrive at the agency on the provider's schedule, which is to say late, in a batch, covering weeks you lived one at a time.",
 "Clean, all of them \u2014 as you knew, and as the file, until the batch landed, could not have said. Evidence that exists somewhere is not the same as evidence that exists in the record, and the distance between those two places is measured in exactly this kind of envelope.",
 "Ms. Osei files a one-line notice attaching the batch to your progress statement, so the results join the column they belong to.",
], [C("Ask her to attach them to the two-timeline page as well", "assessment_pages",
      addHidden=["Screens \u2014 summer batch clean, filed and attached to the timeline statement"],
      note="One fact, filed in both columns. September will not have to go looking for it.")]),

N("assessment_pages", 73, "The Assessment Pages", [
 "The rest of your requested record arrives in a second envelope: the assessment, this time with its workings \u2014 the form, the item ratings, the outcome line \u2014 and a cover note updating two items since spring in light of your filed progress.",
 "Read closely, the form is neither a verdict nor a villain. It rated what it was shown, when it was shown it. Where the file has grown \u2014 attendance, tenancy, visits \u2014 the ratings tied to those items have moved. Where the file is silent, the ratings have simply waited.",
 "Ms. Osei restates the flag for your folder's cover sheet: whether the adjudication-phase disclosure rule (Pa.R.J.C.P. 1340(B)(1)) reaches every scored item of a form like this is untested; your copy came through the direct record request, which \u201cshall be released upon request\u201d (55 Pa. Code \u00a7 3130.44(d)). How you got it matters less, in the end, than that you are no longer the only person in the case who has not seen it.",
], [C("Go through it with Ms. Osei, item by item, and note which items your last month can still move", "foster_home_meeting",
      addHidden=["Assessment \u2014 form, item ratings and outcome read by parent with counsel before the hearing"],
      note="A form read in July can be answered in August. A form first seen in September can only be endured.")]),

N("foster_home_meeting", 80, "Coffee at the Foster Home", [
 "The Hartleys invite you for coffee after a visit \u2014 a first. Their kitchen has Wren's height marks on the door frame, in pencil, in a hand that is not yours. It hurts in the ordinary way true things hurt, and you stay, and you drink the coffee.",
 "Mrs. Hartley says they did not ask for the goal to change; the agency asked them whether they would be a permanency resource \u201cif it ever came to that,\u201d and they said yes because saying no felt like abandoning Wren a second way. Mr. Hartley says: \u201cNobody in this kitchen is your enemy, Marcus.\u201d",
 "You believe them. That is the difficult part the movies leave out: Track B is not staffed by villains. It is staffed by kind people answering the questions they were asked, in the order they were asked them.",
], [C("Thank them, and ask that Wren's visit routine stay exactly as it is while the court decides", "plan_checkpoint",
      addHidden=["Foster-home meeting \u2014 placement stable; visit routine to continue by agreement"],
      note="Stability for Wren, continuity for you, civility for the record. Some sentences do three jobs."),
    C("Ask them directly whether they would adopt her", "plan_checkpoint",
      note="\u201cIf a judge ever decided she needed that, yes,\u201d Mrs. Hartley says, carefully. \u201cWe answered the question we were asked.\u201d Now you have heard Track B in its own words.")]),

N("plan_checkpoint", 87, "Nine of Twelve, Corrected", [
 "The agency's draft report for September arrives at Ms. Osei's office. It is mostly current \u2014 and it describes your parenting program, in one flat line, as \u201cnine of twelve sessions completed.\u201d",
 "Nine was true in May. Your folder holds sign-in copies for sessions ten and eleven, and session twelve \u2014 the last \u2014 is still ahead of you, in August. Draft reports have a way of becoming final reports, and final reports have a way of becoming the past.",
], [C("Have Ms. Osei send the correction this week, with the sign-in copies attached", "summer_visit",
      setFlags=["recordCorrected"],
      addHidden=["Draft report corrected before the hearing \u2014 attendance current, with sign-in copies"],
      note="Corrected on paper, before the hearing, the error never gets to testify."),
    C("Leave it \u2014 the real certificate will be there by September anyway", "summer_visit",
      note="It will. Whether September's summary is written from the certificate or from the draft is a coin currently spinning.")]),

N("summer_visit", 94, "The Long Visit", [
 "August's long visit is the best one yet: a whole day, a picnic Wren planned with the seriousness of a state occasion, and a goodbye she manages by explaining, to both households, the rules of the drawing homework she has assigned.",
 "On the bus home you understand, clearly and without drama, the arithmetic of concurrent planning from the inside: every good day like this is, at the same time, a day of Track A working and a day of Wren settling deeper into the home on Track B. The same day. The same drawing. Two columns.",
 "The work is not to stop the day from meaning both things. The work is to make sure the record can hold both meanings at once.",
], [C("Write the visit up in your folder that night, dated, while it is still warm", "birthday",
      note="Contemporaneous is a cold word for a warm practice: write it while it's true in detail.")]),

N("birthday", 98, "Seven Candles, Counted Twice", [
 "Wren turns eight in August, and there are, without anyone planning it as a symbol, two small celebrations \u2014 one at the Hartleys', one at your visit \u2014 and she reports each to the other household with a diplomat's completeness.",
 "She asks you, at yours, whether she will have \u201ctwo birthdays forever.\u201d You tell her the truth at her size: grown-ups are working out where home is, a judge helps decide, and everyone at both parties loves her in the same direction.",
 "It is the truest available sentence. You write it down anyway when you get home, because dates and sentences are what September is made of.",
], [C("Go to the last class, and finish the plan's classroom piece", "last_class",
      note="One session left. Endings, even small ones, should be signed in.")]),

N("last_class", 105, "The Twelfth Session", [
 "Session twelve. The facilitator hands out certificates with the gravity of a commencement and the refreshments of a church basement, and yours says what the sign-in sheets have been saying all summer: completed.",
 "She writes a line on the back of yours, unprompted: \u201cAttended every session from ten onward under a goal-change motion. Did the work while the ground moved.\u201d It is not a legal document. You file it like one.",
], [C("Take the certificate straight to Ms. Osei's office", "counsel_letter",
      addHidden=["Parenting program \u2014 completed, certificate in the court file"],
      note="Twelve of twelve. One Track A line, closed, in writing, before the hearing that decides the other track.")]),

N("counsel_letter", 107, "A Letter Meant for the File", [
 "On the last business day before the strategy meeting, Ms. Osei files a short letter that does almost nothing \u2014 and that, she explains, is its job. It confirms, with dates, the plan's current state: program completed, screens current, tenancy stable, visits running, and the two timelines as previously filed.",
 "\u201cSeptember should contain no factual surprises about you,\u201d she says. \u201cSurprises are what the other track is for. Our track arrives pre-read.\u201d",
 "It is the sound of a record being closed neatly, one week early, on purpose.",
], [C("Read the filed copy once more, and then go home and sleep", "strategy_choice",
      addHidden=["Counsel's confirmation letter filed \u2014 plan state current and dated before the hearing"],
      note="Tomorrow you choose the lead argument. Everything it could lead with is already in the file.")]),

N("strategy_choice", 108, "Choosing the Lead Argument", [
 "In the last stretch before the hearing, Ms. Osei spreads the summer on her conference table: the filed timelines, the assessment pages, the corrected attendance, the certificate, and \u2014 if you found it and wrote about it \u2014 one service-plan page with an empty box.",
 "September 2 is both the hearing and the fifteen-month date. The agency will argue the calendar. The Hartleys' willingness will be in the file. Your progress will be in the file too, in whatever form the summer left it.",
 "\u201cWe lead with one argument,\u201d she says. \u201cChoose like a person who has to live inside the outcome \u2014 because both of you do.\u201d",
], [C("Lead with the services gap \u2014 the plan's own necessary step, never provided, documented", "path_services",
      note="The exception built from the agency's own page."),
    C("Lead with the documented compelling reason \u2014 the whole current Track A record, filed and dated", "path_compelling",
      note="A reason, documented, for why filing on this date would not serve Wren."),
    C("File a full written statement preserving every exception \u2014 and let the goal argument fall where it falls", "path_written",
      note="A colder strategy: lose the label if you must, keep the argument for the stage that may come."),
    C("Keep your head down \u2014 'progressing' should speak for itself", "path_thin",
      note="Ratings speak in summaries. September will be conducted in documents.")]),

N("path_services", 112, "The Empty Referral Box, in a Letter", [
 "The filing is short: the plan page, the empty box, the dates. The service was identified by the agency itself as necessary for Wren's safe return \u2014 the step toward unsupervised visits. It was marked \u201cto be sent\u201d in month six. It was never sent. Your letter asked for it, in writing; the referral was made at last in August, a year late, and the August confirmation is attached too, because fairness is also a record.",
 "Ms. Osei's covering words are plain: the third exception in the federal rule exists for exactly this shape of fact (42 U.S.C. \u00a7 675(5)(E)) \u2014 a State that has not provided the services it identified as necessary should not be able to run the fifteen-month clock as if it had.",
], [C("Go to the hearing with the exception documented, not just discovered", "hearing_services",
      setFlags=["exceptionDocumented"],
      note="A fact, filed early, with its dates on it.")]),

N("path_compelling", 112, "The Documented Reason", [
 "The filing assembles the paper summer into one argument: a completed plan but for time, a certificate, clean screens, a stable tenancy, visits grown long and ordinary, the two timelines stated side by side since the interim review \u2014 a documented case that changing the goal, and filing on the fifteen-month date, would not serve Wren, who is thriving in part because her father's case is alive.",
 "It does not ask the court to feel anything. It asks the court to write one sentence \u2014 a compelling reason, documented in the case plan \u2014 and to leave Track A's finish line where the evidence says it nearly is.",
], [C("Go to the hearing with the reason documented, not just felt", "hearing_compelling",
      setFlags=["exceptionDocumented"],
      note="One sentence is all you need. Sentences, in files, are load-bearing.")]),

N("path_written", 112, "Preserving the Argument", [
 "Your written statement goes in whole: progress, timelines, the assessment pages, every exception the record supports \u2014 including, if the summer found it, the owed referral, with dates. It concedes nothing. It also, deliberately, spends less of itself on the goal label than on making sure that nothing the agency may argue later, at any termination stage that may come, can be said to have gone unanswered now.",
 "Ms. Osei is honest about the trade: \u201cThis protects the next hearing better than it wins this one. A termination case, if it is ever filed, is decided on proof the agency would have to carry clearly and convincingly \u2014 and this statement would be sitting in the record it has to carry it against. But September may still change the goal.\u201d",
], [C("File it, and go to the hearing knowing exactly what it does and doesn't do", "hearing_written",
      setFlags=["argumentPreserved"],
      note="A record position, held on purpose, with open eyes.")]),

N("path_thin", 112, "Head Down, Again", [
 "The last week of August is a good week, taken singly. A visit that sings. A certificate on the refrigerator. A child who assigns drawing homework like a small, confident state.",
 "What does not happen: paper. No lead argument is filed, no exception is documented, no statement goes in. The file the judge will open on September 2 is the file as the system wrote it \u2014 a good father, an unfinished plan, a willing resource family, and a federal date arriving exactly on schedule.",
 "You have done the work. September's question is narrower than the work: not what you have done, but what is documented as a reason.",
], [C("Go to the hearing with your folder and your summer", "hearing_thin",
      note="The folder is real. Whether the court can use it depends on whether it became the court's paper too.")]),

N("hearing_services", 121, "The Fifteen-Month Hearing \u2014 The Services Record", [
 "September 2, 2026. Fifteen months, to the day the statute counts from. The agency argues the calendar first, as Ms. Osei predicted: the date has arrived, a resource family is willing, permanency should not wait.",
 "Then the record answers, in its two columns. Track A: completed, current, filed. Track B's own foundation: a step the plan called necessary, marked to be sent in month six, sent in month fourteen \u2014 after a parent found the empty box in his own file and asked about it in writing. The agency's lawyer, to her professional credit, does not contest the dates.",
 "The judge looks at the timeline page \u2014 the one filed in June, the one stated on the record at the interim review \u2014 for a long moment. \u201cThe clock,\u201d she says, \u201cis supposed to measure the case. It is not supposed to replace it.\u201d",
], [C("Listen to the order, in the order the judge gives it", "end_denied",
      note="Goal first. Then the sentence about the exception. Then the services, ordered made at last, with dates.")]),

N("hearing_compelling", 121, "The Fifteen-Month Hearing \u2014 The Paper Summer", [
 "September 2, 2026. The agency argues the calendar, the settling-in, the willing resource \u2014 a real argument, made by people who also have a file.",
 "But this summer, the file has two authors. The court works through the filed record: the certificate, the corrected attendance, the assessment items that moved when the file grew, the timelines stated side by side since the interim review. The agency's own rating word, progressing, is no longer a summary floating free of its evidence; the evidence is attached, dated, and current.",
 "The judge asks the agency one question \u2014 \u201cWhat, on this record, remains undone that time will not finish by the next review?\u201d \u2014 and the room is quiet in a way that is itself an answer.",
], [C("Listen to the order, in the order the judge gives it", "end_denied",
      note="Denied and deferred are cousins. Today, either word keeps Track A's finish line where it was.")]),

N("hearing_written", 121, "The Fifteen-Month Hearing \u2014 Granted, with a Record", [
 "September 2, 2026. The court changes the goal. The words land the way Ms. Osei warned they might: Wren's settled life, the calendar, the resource family's willingness \u2014 weighed, on the day, more heavily than a father's nearly-finished plan.",
 "And then the judge does the second thing, the one your summer built: she notes, on the record, the parent's filed statement and the exceptions it documents, unanswered in their particulars, and directs that they remain part of the record for any later stage. No termination petition has been filed. If one ever is, it will be read against a record that was being written, on purpose, since May.",
 "You walk out with a changed goal and an unchanged file of your own making. Both facts are true. The strategy was built to hold the second one when the first one went the other way.",
], [C("Ask Ms. Osei, in the hallway, exactly what was preserved and what happens next", "end_preserved",
      note="\u201cYour argument,\u201d she says. \u201cIntact, dated, and theirs to answer. That was the design.\u201d")]),

N("hearing_thin", 121, "The Fifteen-Month Hearing \u2014 Changed", [
 "September 2, 2026. The hearing is shorter than the summer deserved. The agency's summary is fair and even warm \u2014 and a summary is all it is: a progressing father, an unfinished plan, a date arrived, a family willing.",
 "Your folder is on your lap, with the visit notes you wrote warm, the sentence from the front door you did or did not write down, the progress you made and mostly did not file. The judge can only rule on the record in front of her, and the record in front of her has one column filled in by the system and the other mostly in pencil, at home.",
 "The goal is changed. The judge, reading the room with care, adds the part that is still yours to decide: reunification services will continue for now, and reviews will continue, and what the file says by the next one is \u2014 as it has always been \u2014 partly up to the people in this room.",
], [C("Keep going \u2014 attend everything, exactly as before, with the goal changed above you", "end_changed_services",
      setFlags=["keptAttending"],
      note="Track A, still running, on a track the court has renamed. Attendance is now the loudest sentence in your file."),
    C("Stop going \u2014 if the finish line moved, the running was the lie", "end_collapse",
      note="It is the most understandable choice in this scenario. It is also the one September's summary, next time, will be written from.")]),

N("end_denied", 135, "Ending \u2014 Goal Change Denied, Exception Documented", [], ending=True, debrief=[
 "WHAT THE RECORD HELD (the hidden record, revealed): Underneath this path sat a two-column file: a Track A record that was current because its author filed it \u2014 attendance corrected before it could testify wrongly, a certificate in the file before the hearing, timelines stated side by side on the record since the interim review \u2014 and, on the path that found it, an empty referral box: a service the plan called necessary, marked 'to be sent' in month six and sent in month fourteen, after the parent asked in writing. September did not turn on whether you are a good father. It turned on which facts existed in the court's paper, dated, by September 2.",
 "THE LAW UNDER THIS PATH: At 15 of the most recent 22 months in care, the agency is pressed to file a petition to terminate parental rights \u2014 unless an exception applies (42 U.S.C. \u00a7 675(5)(E)): the child is being cared for by a relative; a compelling reason that filing would not be in the child's best interest is documented in the case plan; or the agency has not provided the services the plan identified as necessary for the child's safe return. Your hearing documented an exception and denied or deferred the goal change on a current Track A record; counsel was your right throughout (42 Pa.C.S. \u00a7 6337), and the record that made it possible began with a request the regulation answers in five words \u2014 it 'shall be released upon request' (55 Pa. Code \u00a7 3130.44(d)). Nothing today ends the case: reviews continue, and the plan's remaining work still has to be finished, by you and \u2014 now with dates attached \u2014 by the agency.",
 "THE HONEST PART: This is a deferral with homework, not a rescue, and it was not produced by effort alone. A different judge could have weighed Wren's settled year more heavily on the same paper; a referral sent on time would have removed the strongest document in the file; a foster family less kind could have rewritten every visit scene. Workers, judges, an unchecked box, and luck all hold pieces of this outcome. What your choices changed was the record those pieces landed on \u2014 two columns, current, impossible to summarize honestly using only one of them.",
]),
N("end_preserved", 135, "Ending \u2014 Goal Changed, the Argument Preserved", [], ending=True, debrief=[
 "WHAT THE RECORD HELD (the hidden record, revealed): A changed goal, and underneath it a written statement that went in whole and early: your progress with its proofs, the two timelines side by side, and every exception the record supports, with dates, unanswered in their particulars and now noted by the court as part of the record for any later stage. The label moved. The argument did not. That was the strategy, and it is important to say plainly what it is: a record position, not a custody outcome.",
 "THE LAW UNDER THIS PATH: A goal change is not a termination. No petition has been filed in this ending, and if one ever is, the agency would have to prove its grounds by clear and convincing evidence at a hearing where your preserved record \u2014 including the documented services question under 42 U.S.C. \u00a7 675(5)(E) \u2014 would be part of what that proof must answer. Your statement sits in the file because you filed it while filing was yours to choose; your knowledge of what to preserve began with your own record, released on request (55 Pa. Code \u00a7 3130.44(d)), and your counsel's right to build it with you is the right the law gave you at the start (42 Pa.C.S. \u00a7 6337).",
 "THE HONEST PART: Preserved is not won, and this debrief will not pretend otherwise: Wren tonight is in the same home, under a goal that no longer names yours. What the record buys is a fairer next hearing, if there is one \u2014 and fairer next hearings are sometimes all a summer can buy. A different judge might have denied the change outright on this paper; this one didn't. Judges, workers, the Hartleys' honest kindness, and the luck of an unchecked box are all in this ending alongside your work. The work was to make sure that if the future case is ever built, it must be built over your words too \u2014 dated, filed, and already there.",
]),
N("end_changed_services", 135, "Ending \u2014 Goal Changed, Services Continue", [], ending=True, debrief=[
 "WHAT THE RECORD HELD (the hidden record, revealed): A goal changed on a thin record \u2014 and one order inside the order that matters more than it looks: reunification services continue. The court said so because a father in the room, on the worst day of his case, was still plainly a father in the middle of one: attending, visiting, unfinished rather than unwilling. What had not been filed could not be weighed. What had been lived could still be seen, just, in the man himself.",
 "THE LAW UNDER THIS PATH: A goal change redirects a case; it does not terminate rights, and it does not by itself end services \u2014 here the court ordered them continued while reviews continue, which is concurrent planning's dual track running in its other direction: services toward reunification maintained while an alternative future is planned (the structure the whiteboard drew in May). If you disagree with the order, there are further steps a party can take after a permanency decision; this game does not put a number on that window \u2014 ask Ms. Osei today, in person, what it is and when it runs from, because windows like that are exactly the kind that close while a parent is deciding how they feel. The fifteen-month filing question (42 U.S.C. \u00a7 675(5)(E)) also remains alive, with its exceptions, and a record can still be built toward them \u2014 beginning, as it always can, with your own file, which 'shall be released upon request' (55 Pa. Code \u00a7 3130.44(d)).",
 "THE HONEST PART: This ending is the system working at half its promise: the services survive because a judge chose to order them, on a day when a fuller record might have made the order unnecessary to beg for. Your continued attendance from here is not a technicality \u2014 it is the entire remaining argument, made weekly, in sign-in ink. Plenty of parents in this room of an ending rebuild the record by the next review; plenty of identical effort, in front of a different judge on a different day, does not get the services order at all. Workers, judges, and luck signed this outcome with you. Your signature, weekly, is the part still being written.",
]),
N("end_collapse", 142, "Ending \u2014 The Quiet Collapse", [], ending=True, debrief=[
 "WHAT THE RECORD HELD (the hidden record, revealed): Nothing new \u2014 and that is the ending. In the weeks after the goal changed, the sign-in sheets stop, the visit bag stops traveling, and the file, which is written from attendance and paper, begins describing an absence it did not create. By the next review, the summary can say, truthfully and completely misleadingly, that the parent disengaged after the goal change. The plan did not collapse in a hearing. It lapsed, one un-attended Tuesday at a time, in a church basement that kept meeting without you.",
 "THE LAW UNDER THIS PATH: Legally, almost everything that was true in September is still true: no termination has been decided, services were ordered to continue, reviews continue, and the exceptions in the federal rule (42 U.S.C. \u00a7 675(5)(E)) do not expire with a parent's hope. Practically, the case now runs on the only evidence still being generated \u2014 other people's. A record can be rebuilt from almost any week a parent chooses to restart it; counsel remains your right (42 Pa.C.S. \u00a7 6337), and your own file remains yours on request (55 Pa. Code \u00a7 3130.44(d)). What cannot be rebuilt is the appearance, in the summaries, of the weeks when nothing was filed and nothing was attended. Gaps are also a record. They testify in every later room.",
 "THE HONEST PART: No one who has sat in that courtroom should be surprised by this ending, and this debrief does not judge it: the goal change told a man, in legal language, that the running no longer counted, and he believed the language instead of the whiteboard. Stopping reads as surrender because the file has no column for grief. It has a column for attendance. Workers who might have called, a judge who might have kept the goal, a referral sent on time \u2014 the same luck and people run through this ending as through the good ones. The difference is that in this one, the parent's own hand leaves the page, and the page goes on being written without it.",
]),
]

# =====================================================================
# SCENARIO 34 \u2014 The Missed Year
# Removal (in-story): Monday, March 2, 2026 = dayOffset 0.
# Shelter care: removal + 3 days = Thursday, March 5, 2026 (72 hours).
# ASFA 15-month date: March 2, 2026 + 15 calendar months =
# Wednesday, June 2, 2027 (asserted; stated in-game).
# =====================================================================
S34_START = date(2026, 3, 2)
S34_ASFA = add_months(S34_START, 15)
assert S34_ASFA == date(2027, 6, 2), S34_ASFA
assert (date(2026, 3, 5) - S34_START).days == 3

s34_nodes = [
N("start", 0, "The Knock and the Bag", [
 "You are Dana, a home-health aide, and Eli's mother. Eli is five. This winter your hours were cut, the landlord filed, and the arrangement that held your life together \u2014 a neighbor watching Eli between your shift and your sister's \u2014 came apart one ordinary evening at a time.",
 "Today the caseworker and a second person stand at your door with a court paper, and the paper says what the last month has been saying: the supervision arrangement is gone, the apartment is going, and no one can say, on paper, who is with Eli while you work. A small bag is packed. Eli asks whether his blue cup can go too. It can. It does.",
 "No one in the hallway is cruel. That is worth saying at the start of this scenario, because everything that follows happens among people who are mostly not cruel \u2014 and happens anyway, in files.",
], [C("Write down the names on the paper, and the time, before the door closes", "shelter_care",
      setFlags=["removed"],
      addHidden=["Removal \u2014 Monday, March 2, 2026; names and time recorded by parent"],
      note="Your first entry. You do not know yet that it is the first entry in the only continuous record this case will have.")]),

N("shelter_care", 3, "Seventy-Two Hours", [
 "The shelter care hearing comes within seventy-two hours of Eli being taken into custody, as the law requires (42 Pa.C.S. \u00a7 6332; 23 Pa.C.S. \u00a7 6315(d)) \u2014 Thursday, March 5, three days after Monday's hallway. A small courtroom. A judge. A file you have never seen, about a week you have just lived.",
 "You have a lawyer. Counsel is your right, and appointed counsel is provided if you cannot afford one (42 Pa.C.S. \u00a7 6337). Yours is Mr. Whitfield, who has forty minutes of the case in his head and uses them well: Eli stays in placement for now, with the Mensah family, and visits begin next week.",
 "On the way out he says the sentence this scenario is built from: \u201cCases like yours are decided by records, Dana. Start one of your own. Today. Boring, dated, duplicated. Start today.\u201d",
], [C("Ask him what 'one of your own' means, exactly", "folder_begins",
      note="\u201cA folder. Everything they give you, everything you sign, every visit, every receipt. Copies of the copies. Boring will save you.\u201d")]),

N("folder_begins", 7, "A Folder of Your Own", [
 "The folder costs less than lunch: a binder, dividers, a notebook with the dates already printed in the corners. You label the sections the way Mr. Whitfield said \u2014 COURT, SERVICES, VISITS, HOUSING, LETTERS \u2014 in the darkest marker the dollar store sells.",
 "Your sister watches you do it. \u201cYou really think paper is going to matter more than the actual parenting?\u201d she asks, not unkindly.",
 "\u201cI think paper is how they see the parenting,\u201d you say, surprising yourself. \u201cFrom their side of the desk, the folder is the parenting they can check.\u201d",
], [C("Make the first entry: the plan meeting, dated, with who said what", "worker_one_plan",
      note="Four lines. It takes five minutes. It will still exist in a year, which is more than will be said for some things.")]),

N("worker_one_plan", 12, "Worker One: The Plan", [
 "Your first caseworker is Ms. Adeyemi, who is organized, warm, and carrying a caseload she mentions once, the way people mention weather in another county.",
 "The family service plan has four lines that matter: complete a parenting program (ten sessions, Tuesdays); accept a referral to a housing navigator and work it; keep visits, twice a week; and rebuild a documented supervision plan for your work hours. Housing runs under all of it like a bass note: the navigator is supposed to be the bridge from your sister's couch to a lease.",
 "\u201cThe navigator referral goes out this week,\u201d Ms. Adeyemi says, and writes it in her notebook. You write it in yours. Two notebooks, one promise \u2014 remember that there were two.",
], [C("Repeat the plan back to her before you leave, and write down her corrections", "sign_in_sheet",
      addHidden=["Plan \u2014 parenting program, housing navigator referral, visits, supervision plan; referral promised 'this week'"],
      note="She corrects one date and initials your notebook without being asked. A good first page.")]),

N("sign_in_sheet", 20, "The Sign-In Sheet", [
 "The parenting program meets in a room with a sign-in sheet by the door and coffee that improves as the weeks pass. Session one: you sign, and the facilitator, Ms. Lindt, dates the sheet herself.",
 "At the break she says, to the room in general: \u201cKeep your own count. Programs close, systems change, sheets get scanned crooked. The parents who do best in these rooms are the ones who could prove they were in them.\u201d",
 "You are already keeping your own count. What you have not yet decided is whether to keep proof, or just the count.",
], [C("Ask at the end of every session for a dated copy or a stamp in your notebook", "receipts_habit",
      setFlags=["proofHabit"],
      addHidden=["Parenting program \u2014 parent collects dated proof at each session"],
      note="Ms. Lindt stamps the notebook like a passport. Small ceremony, large consequences."),
    C("Keep the count in your notebook \u2014 the program has the sheets; that should be enough", "receipts_habit",
      note="It should be. Keep the sentence. This scenario is about sentences that begin 'it should be.'")]),

N("receipts_habit", 31, "Receipts in Pencil", [
 "Spring, in folder form: bus receipts in an envelope, a money order stub for the program's workbook fee, the visit center's printed confirmations, your work schedule with the new supervision arrangement penciled in \u2014 your sister's hours, initialled by her, because Mr. Whitfield said initialled paper is a different species from remembered paper.",
 "None of it is impressive. All of it is dated. Your life, this spring, is a series of small rooms you were provably in.",
], [C("Spend one evening a month copying the month's pages at the library", "visits_first_log", cash=-10,
      note="Copies at home, originals in the folder. Duplicated is a love language in this system."),
    C("Skip the copying for now \u2014 the folder itself is the backup", "visits_first_log",
      note="One folder. One copy of everything. Remember that you chose that.")]),

N("visits_first_log", 42, "Visits, First Log", [
 "Visits run twice a week at the center, and they are the best hours of the spring: Eli's reading, out loud, mostly smooth; a card game you are losing on purpose less often than he thinks.",
 "The visit center keeps a log, and so \u2014 because nobody told you to and Mr. Whitfield told you to \u2014 do you. Dates, times, who was at the desk. The two logs agree completely. Agreement between records is easy to maintain, you will learn, exactly as long as nothing changes.",
], [C("Ask the desk for a copy of the center's log page each month", "notebook_habit",
      addHidden=["Visits \u2014 parent's log and center's log agree, spring; copies requested monthly"],
      note="The desk clerk prints it without fuss. Paper is easy to give to people who ask calmly, with a folder."),
    C("Trust the center's log \u2014 two logs for one visit is a lot of paper", "notebook_habit",
      note="Your log continues anyway, in the notebook. Dates and desk names. It will turn out to be a kind of paper too.")]),

N("notebook_habit", 55, "The Notebook Habit", [
 "By early summer the notebook has a rhythm: date in the corner, names spelled as given, promises written the way they were spoken, including the wobbly ones. \u201cNavigator referral this week\u201d has been in it since March, initialled. Under it, in smaller writing, the follow-ups: asked in April \u2014 'in process.' Asked in May \u2014 'waiting on the list.'",
 "The parenting program, meanwhile, is simply working: session follows session, stamp follows stamp, and Ms. Lindt has begun using your notebook as the room's example of the habit she preaches.",
 "A file is growing in an office across town, too. It has the same spring in it. For now.",
], [C("Finish the program", "certificate",
      note="Endings, even small ones, should be signed in.")]),

N("certificate", 85, "The Certificate", [
 "Session ten. The certificate has your name spelled right and the program's seal, and Ms. Lindt signs the completion letter that goes with it: ten of ten, with the dates listed, because she lists dates the way other people list ingredients.",
 "This letter is a door-closing document: one whole line of the plan, completed, under worker one, in a spring when the system and you were telling the same story.",
 "What a completed line is worth depends entirely on whether anyone, later, can find it.",
], [C("Put the original in the folder and copies in two other places", "supervisor_beat",
      setFlags=["certificateCopied"],
      addHidden=["Parenting program \u2014 completed 10 of 10 under worker one; certificate and completion letter copied and stored in three places"],
      note="Folder, sister's house, a photograph on your phone. Completed, three times over."),
    C("Put it in the folder \u2014 one careful place is enough", "supervisor_beat",
      addHidden=["Parenting program \u2014 completed 10 of 10 under worker one; certificate in the folder"],
      note="One careful place. The folder rides the bus with you twice a week. Folders are mortal.")]),

N("supervisor_beat", 95, "Asked in Writing", [
 "The housing navigator referral is now three months old as a promise. 'In process' was April. 'Waiting on the list' was May. June's answer, from a covering worker on a day Ms. Adeyemi is at training, is: \u201cWhich referral?\u201d",
 "You show her your notebook \u2014 the initials, the dates. She is honest, and the honesty is its own information: the referral may have gone to a program that closed its list in spring. She cannot find a send confirmation. She will, she says, flag it.",
 "Flags, you are learning, are where paper goes to be intended.",
], [C("Write it up that night \u2014 the question, her answer, her name, the date", "handoff_one",
      addHidden=["Housing navigator referral \u2014 promised March, 'in process' April, 'waiting' May, no send confirmation found in June; all recorded by parent"],
      note="Four lines in the notebook. The referral's whole biography, as it will turn out, exists only there."),
    C("Leave it to the flag \u2014 she said she'd handle it", "handoff_one",
      note="She meant it. Meaning it and it surviving the summer will turn out to be different countries.")]),

N("handoff_one", 122, "Handoff One", [
 "Ms. Adeyemi is leaving \u2014 a promotion, a going-away cake in an office kitchen, genuine good wishes. Your case transfers to a worker you will meet next week.",
 "Transfers, in offices like this one, are a summary, a stack, and a deadline. What travels is what the summary says travels. Ms. Adeyemi offers you a handoff meeting to go through your folder against her file, line by line. It will take an unpaid afternoon. Unpaid afternoons are your scarcest currency this summer, scarcer than money.",
], [C("Take the afternoon \u2014 go through the folder against the file, line by line", "worker_two", cash=-25,
      setFlags=["handoffChecked"],
      addHidden=["Handoff one \u2014 parent and worker one reconciled folder and file line by line before transfer"],
      note="Most lines match. The navigator line, in her file, reads 'referral pending.' You both look at it. She writes 'parent following up in writing' beside it, and initials it."),
    C("Send her a one-page summary of where things stand instead", "worker_two",
      note="She files it, she says later, on her last day. Last days are a busy country for filing.")]),

N("worker_two", 129, "Worker Two: Starting Over", [
 "Mr. Kowalski is brisk, new to the case, and reading from the transfer summary, which is shorter than the spring was. In the summary, your parenting program is \u201cin progress.\u201d Your visits are \u201cregular.\u201d Your housing is \u201cunstable.\u201d The navigator does not appear at all.",
 "Summaries compress. Compression loses months the way a folded map loses towns.",
 "He schedules your visits, re-explains the plan as if it were new, and asks you to re-sign two releases you signed in March. Starting over, you understand, is not his decision. It is the transfer's shape.",
], [C("Show him the certificate copy and ask him to correct 'in progress' while you watch", "referral_lost",
      addHidden=["Handoff two \u2014 transfer summary described completed program as 'in progress'; parent flagged it at first meeting"],
      note="He says he'll update it. The summary, corrected or not, has already been read by everyone who read it."),
    C("Let it ride \u2014 you'll sort the details out as you go", "referral_lost",
      note="Details, un-sorted, have a way of becoming the record. But it is a long summer and he is the second person to hold your spring.")]),

N("referral_lost", 138, "The Referral That Was Never Re-Sent", [
 "The housing question comes up in July, because housing always comes up, and Mr. Kowalski \u2014 checking, to his credit, while you sit there \u2014 finds no navigator referral in the transferred file at all. Not pending. Not closed. Absent.",
 "His theory is reasonable, which makes it worse: referrals made by a departing worker are usually re-sent by the receiving worker; his transfer summary never mentioned one; so, in the system's own logic, there was nothing to re-send. The promise lived in two notebooks. One of them was yours. The other left with Ms. Adeyemi.",
 "\u201cI'll send it today,\u201d he says, and does, in front of you. The new referral is dated July. The bridge the plan described in March begins, in the official story, in July. Four months of bridge exist only in a notebook with initials in it.",
], [C("Ask for the send confirmation, dated, for your folder", "reprove",
      addHidden=["Housing navigator referral \u2014 re-sent July under worker two; send confirmation kept by parent; March promise documented only in parent's notebook"],
      note="He prints it. August's date sits there honestly. Whether March's promise also exists, officially, is now a question about paper."),
    C("Thank him and move on \u2014 at least it's sent now", "reprove",
      note="It is sent. Forward motion is real. So is the shape a missing five months will give the story later.")]),

N("reprove", 147, "Completed, Marked Incomplete", [
 "The agency's next report reaches Mr. Whitfield's office before it reaches you, and he reads you the relevant line over the phone: parenting program \u2014 incomplete.",
 "Completed in May. Marked incomplete in a report written in summer. Somewhere between a certificate, a transfer summary that said 'in progress,' and a report written from the summary, ten Tuesdays became a gap.",
 "This is the beat the whole scenario has been walking toward: not an accusation, not a villain \u2014 a fact about you that is false, in a file, gaining the small authority that filed things gain.",
], [C("Send the completion letter, with its dates, to the agency and the court \u2014 and keep the receipts", "visit_log_restarts", cash=-10,
      setFlags=["completionReproved"],
      addHidden=["Parenting completion re-proved in writing \u2014 completion letter with dates sent to agency and court, receipts kept"],
      note="Paper answers paper. The letter goes into the file next to the line it corrects, if files are fair. Files are fair when they are made to be."),
    C("Correct it by phone \u2014 Mr. Kowalski knows the truth now, even if the report doesn't", "visit_log_restarts",
      note="He does know. The report is what will be read in February by a person who has never met either of you.")]),

N("visit_log_restarts", 160, "The Log That Restarts", [
 "The visit center has a new system, a new desk clerk, and \u2014 you discover this month, asking for your monthly copy \u2014 a new log. The new log begins in August. The clerk is apologetic and precise: the old system's records were \u201cmigrated,\u201d and what migrated, in your case, begins in August.",
 "Your visits from March to August exist, as far as the center's paper is concerned, in your notebook: dates, times, who was at the desk, Eli's reading level rising in the margins where you wrote it down because you were proud.",
 "Two logs agreed all spring. Now there is one log, restarted, and a notebook.",
], [C("Write up a one-page visit history from your notebook and file it with Mr. Whitfield now", "copy_shop",
      setFlags=["visitHistoryFiled"],
      addHidden=["Visits \u2014 center log restarts August; parent's contemporaneous notebook covers March onward; history filed with counsel in late summer"],
      note="Filed in autumn, it is a record made from a record. Filed in February, it would be a claim. Timing is a kind of evidence too."),
    C("Keep the notebook safe and say nothing yet \u2014 February is far away", "copy_shop",
      note="February is exactly as far away as February always is, right up until it isn't.")]),

N("copy_shop", 175, "Copies of the Copies", [
 "An evening at the copy shop with the whole folder is the least dramatic scene in this scenario and, Mr. Whitfield will later say, possibly the most important one you play.",
 "Page by page: certificate, completion letter, sign-in stamps, receipts, the referral pages, the notebook's summer. A second set, complete, for his office. Your set never has to travel together again. Loss, from here on, would have to happen twice to count.",
], [C("Pay for the full duplicate set for your lawyer's office", "records_request", cash=-20,
      setFlags=["folderDuplicated"],
      note="Boring, dated, duplicated. The whole strategy, in a copy-shop bag."),
    C("Copy only the certificate pages \u2014 the rest is in the folder", "records_request",
      note="The folder is good. The folder is also singular. You have been taught the difference twice already this year.")]),

N("records_request", 185, "Asking for the Whole File", [
 "Mr. Whitfield raises the move the spring's leaflets described: separate from everything else, you may request your case record from the county agency, and it \u201cshall be released upon request\u201d (55 Pa. Code \u00a7 3130.44(d)). He is specific, as good lawyers are: the whole record, including the full assessment \u2014 the form itself, the item ratings, and the outcome \u2014 not only the summaries.",
 "He adds the honest flag he always adds about the assessment: whether the adjudication-phase disclosure rule (Pa.R.J.C.P. 1340(B)(1)) reaches every scored item of an assessment form is untested. The direct record request does not depend on that question, which is why you are making it.",
 "By now the request has a second purpose, and both of you know it: you are no longer only reading the file. You are auditing it, against a folder that has never changed hands.",
], [C("Sign and send the request this week", "file_seams",
      setFlags=["recordsRequested"],
      note="A stamp, a date, a copy for the folder. The audit begins."),
    C("Wait until the new worker settles in \u2014 no need to look adversarial", "file_late",
      note="Mr. Whitfield sends it anyway two weeks later, because 'adversarial' is a mood and the record is a fact, but the weeks will show in the dates.")]),

N("file_seams", 200, "A File with Seams", [
 "The returned record is thick, bound, official \u2014 and, read against your folder on your sister's kitchen table, visibly seamed. The assessment is there, form and ratings and outcome, plainer than you feared. The court orders are there. And then the seams: the visit record, continuous from August, thin before it. The parenting line, 'in progress,' long past May. The navigator, present from July, as if housing help had been invented in July.",
 "It is not a false file. It is a restarted one \u2014 a year as remembered by a system that changed its memory twice. Your folder does not argue with it. Your folder simply continues through the months where it stops.",
 "Three people's work is in that file. The only spring in it that was written by one person, start to finish, is yours.",
], [C("Go through it with Mr. Whitfield, seam by seam, with your folder beside it", "folder_fills",
      addHidden=["Agency record returned \u2014 visit record thin before August, program long 'in progress,' navigator present only from July; seams identified against parent's folder"],
      note="By the end of the appointment there are two stacks on his desk. Only one of them has no gaps in it.")]),

N("file_late", 200, "A File with Seams, Later", [
 "The record arrives two weeks further into the winter, and it is the same file its earlier twin would have been: official, bound, and seamed. Visits thin before August. The program 'in progress' past its own completion. The navigator born in July.",
 "Late is not fatal. Late is just later \u2014 two fewer weeks to align your folder to its gaps before the review, and a lesson the notebook already taught you in March, at a kitchen table, for the price of a stamp.",
], [C("Go through it with Mr. Whitfield, seam by seam, with your folder beside it", "folder_fills",
      setFlags=["recordsRequested"],
      addHidden=["Agency record returned late \u2014 same seams identified against parent's folder"],
      note="Two stacks on his desk. Only one of them has no gaps in it.")]),

N("folder_fills", 207, "Her Folder, His Months", [
 "On the kitchen table, the two records interleave like two hands of the same deck. March: your notebook has the referral, initialled; the file has a promise. May: your folder has a certificate; the file has 'in progress.' July: both have the referral, finally sent. October: your notebook has visits; the file has a migration.",
 "Nothing here required anyone to lie. That is the finding, and it is worse than a lie would be, because a lie can be caught. A seam just sits there, looking like a parent's empty spring, until somebody produces the spring.",
 "You can produce the spring. Whether February believes paper produced by the person it is about is the whole remaining question.",
], [C("Ask Mr. Whitfield to build February's filing out of exactly this \u2014 the seams, answered", "handoff_two",
      note="\u201cThat's the filing,\u201d he says. \u201cYours is not a better story. It's a continuous one. Continuity is the argument.\u201d")]),

N("handoff_two", 235, "Handoff Two", [
 "In late October, Mr. Kowalski rotates to another unit. Worker three is coming. The year is about to change its memory again.",
 "You know the shape of this day now. The question the day asks is only whether you will pay its price a second time, knowing what the first unpaid version cost.",
], [C("Ask for a handoff meeting and reconcile the folder against the file again", "worker_three", cash=-25,
      setFlags=["handoffChecked"],
      addHidden=["Handoff two \u2014 folder reconciled against file again before transfer; corrections noted in parent's hand"],
      note="An afternoon's wages, a second time. Continuity, it turns out, has a price and you have decided it is a fair one."),
    C("Send a summary and save the afternoon \u2014 you know how this goes now", "worker_three",
      note="You do know how it goes. That is precisely what the afternoon was for.")]),

N("worker_three", 242, "Worker Three: Another First Meeting", [
 "Ms. Tran is careful, prepared, and working from a summary that has, by now, been summarized twice. In her summary, the year's shape is: a difficult spring, a program eventually completed, housing help engaged in July, visits steady since August.",
 "She is the third person to hold your case, and the first to say the quiet part in a first meeting: \u201cTell me what the file gets wrong. Every file gets something wrong. I'd rather hear it now than read it in February.\u201d",
], [C("Tell her \u2014 calmly, with the folder: the spring the summaries keep losing", "plan_retyped",
      addHidden=["Worker three \u2014 briefed by parent, from the folder, at first meeting; seams named in December"],
      note="She takes notes in a fresh notebook. You recognize the practice. You taught it to yourself in March."),
    C("Keep it general \u2014 she's new; don't start by correcting her", "plan_retyped",
      note="General is kind. February, however, is not a general kind of month.")]),

N("plan_retyped", 262, "The Plan, Re-Typed", [
 "The winter's updated plan arrives re-typed and mostly right, with one line carried faithfully forward by copy and paste through two summaries: parenting program \u2014 completed, it now says at last, but with the completion dated to the summer, when you re-proved it, instead of May, when you did it.",
 "A small error, six months wide, sitting exactly where February's judge will look for how long the spring took you.",
], [C("Ask, in writing, for the date to be corrected to May, with the completion letter attached", "visit_paper",
      setFlags=["dateCorrected"],
      addHidden=["Plan correction requested in writing \u2014 completion dated May, not summer, with letter attached"],
      note="Dates are the load-bearing walls of this entire system. You straighten one."),
    C("Leave the season wrong \u2014 completed is completed; don't fuss", "visit_paper",
      note="'Completed' is the big word. 'When' is merely the word February will ask about.")]),

N("visit_paper", 280, "Sign Your Visits", [
 "The last stretch of visits runs through the winter, and the new center log is reliable now, and stamps your arrivals without being asked.",
 "Still, the habit is yours: you keep the notebook. Dates, desk names, Eli's reading \u2014 by now he reads the card game's instructions aloud to you, in full, with expression, while you lose honestly.",
 "February will ask about visits. Both logs, this time, will have an answer. What they cannot answer is the spring \u2014 for the spring, there is only one log left in the world, and it is in your handwriting.",
], [C("Ask the desk to sign your notebook page at each visit, as well as logging it", "eli_question",
      addHidden=["Visits \u2014 winter visits doubly logged; spring visits covered only by parent's notebook"],
      note="Desk signatures in your book. Two records again, agreeing \u2014 the way spring once was, rebuilt by hand."),
    C("Rely on the center log now that it works", "eli_question",
      note="It works. The spring, which it cannot see, remains where it always was: in the notebook.")]),

N("eli_question", 292, "Is February a Holiday?", [
 "Eli asks whether February \u2014 the word the grown-ups keep using like a place \u2014 is a holiday, and whether he should make it a card.",
 "You tell him the truth at his size: February is a meeting where people who have been helping decide what happens next, and your job at it is to bring the book of the whole year, and yes, a card would be a good idea for any month that has a meeting in it.",
 "He makes the card that visit. It says FEBRUARY in letters of increasing size. You do not put it in the folder. Some things are not evidence. You write the date he made it in the notebook anyway, because by now the hand moves on its own.",
], [C("Go home and spend the evening on the folder, not the feelings", "winter_visits",
      note="Both, in truth. But the folder is the one February can hold.")]),

N("winter_visits", 298, "Winter Visits, Steady", [
 "The last visits before the review are steady in the way the plan once only hoped for: same days, same desk, a supervision plan that has held for months, a housing navigator \u2014 engaged at last, five months late in the official story \u2014 reporting real progress toward a lease you can almost touch.",
 "Eli's teacher sends a note through the visit bag, addressed to you: his reading is up; he tells the class his mom keeps 'the book of everything.'",
 "Out of the mouths of five-year-olds: the book of everything. February is next.",
], [C("Take the teacher's note for the folder, and go to the notice in the mail", "review_notice",
      note="One more dated page. The folder is as ready as a year of evenings can make it.")]),

N("review_notice", 305, "The Review Is Set", [
 "The review is set for February \u2014 the month-twelve review, the year's examination. Ms. Tran gives you the agency's draft summary to read at home, which is new, and fair, and still: there it is. In the draft, your spring is a paragraph. A completed program, eventually. Help with housing, engaged. Visits, steady since August.",
 "It is not the agency being unfair. It is the agency's record, summarized faithfully from a file with seams. Two histories of the same year now exist on paper, and February will be asked to choose between a summary and a folder.",
 "Beyond February, Mr. Whitfield reminds you, the other clock still runs: Eli was placed on March 2, 2026, and fifteen of the most recent twenty-two months arrives on June 2, 2027. February is not that hearing. But what February writes becomes what every later room reads.",
], [C("Take the draft to Mr. Whitfield and lay it beside the folder", "folder_audit",
      note="A paragraph, beside a year. The rest of the winter is for making February look at both.")]),

N("folder_audit", 318, "Auditing Your Own Folder", [
 "The audit is the least sentimental evening of the year: you and Mr. Whitfield, the folder open, a legal pad for what is missing.",
 "What it holds: a completed spring, proved; visits, logged by you without a gap; referrals, promised and re-sent, both dated in your hand. What it holds less well depends on the year you actually played \u2014 a proof habit kept or skipped, copies made or trusted to one mortal folder, corrections filed or phoned in. The folder does not grade your love. It never could. It grades, precisely, your paper.",
 "\u201cFebruary turns on whose paper survives contact with a judge,\u201d he says. \u201cNot whose year was harder. Yours was. That's not the question they'll ask.\u201d",
], [C("Decide, together, how the folder goes in", "hearing_eve",
      note="Four ways remain. They lead to four different Februaries.")]),

N("prep_choice", 330, "How the Folder Goes In", [
 "Mr. Whitfield lays out the last choice of the year the way he laid out the first one: plainly, with prices attached.",
 "File the whole folder early, indexed, every seam answered, so February is a discussion and not an ambush. File the services paper only, if that is the part your proof is strongest on, and let visits be argued. File the folder late, at the door, and trust its truth to outweigh its timing. Or take the reunification the agency's draft already half-offers, sign nothing, contest nothing \u2014 and let the official history stand as written.",
 "\u201cChoose like the person who has to live inside the file,\u201d he says. \u201cBecause after February, the file is where the year lives.\u201d",
], [C("File the complete folder early, indexed, every seam answered", "review_prevails",
      setFlags=["folderFiled"],
      note="Continuity, submitted on time, with page numbers."),
    C("File the services paper \u2014 the certificate, the letters, the referrals \u2014 and argue visits from memory", "review_services_only",
      note="Half the folder goes in like a wall. The other half goes in like a story."),
    C("Bring the folder to the hearing and file it at the door", "review_partial",
      note="True, complete, and un-read in advance. Judges read what they are given time to read."),
    C("Take the half-offer: contest nothing, and let the draft stand", "review_divided",
      note="Reunification first, history later. History, as you have learned, does not keep.")]),

N("hearing_eve", 324, "The Folder, Read Whole", [
 "The folder, a card that says FEBRUARY in letters of increasing size, a legal pad, and a pot of coffee. Mr. Whitfield's last instruction, weeks ago, was about the filing. Tonight's, by phone, is about sleep, and it is the only instruction of his you are going to half-disobey.",
 "You read the year once, start to finish, in your own handwriting. It reads the way the year felt from inside it: slow, ordinary, stubborn. Whatever February decides about its paper, the paper itself is the one part of the year no transfer ever touched.",
], [C("Close the folder, and decide how it goes in", "prep_choice",
      note="Tomorrow the folder meets February. It is ready in the ways you made it ready.")]),

N("review_prevails", 347, "The Review \u2014 The Continuous Record", [
 "February. The agency presents its summary fairly: a difficult spring, a program completed, housing help engaged, visits steady. It is the file's year, told well.",
 "Then the folder goes up \u2014 indexed, filed early, already read. The judge works through it in the order you lived it: the initialled referral promise from March beside its August re-sending; the completion letter's May dates beside summer's 'incomplete'; your notebook's unbroken visits beside a log that begins, apologetically, in autumn.",
 "Ms. Tran, to her credit, confirms what her own file cannot: the seams are transfer seams, not parenting gaps. Three workers nod from three different chairs of the same year. The judge says the sentence the year was for: \u201cThe most reliable history of this case is the one that never changed hands.\u201d",
], [C("Listen to the order", "end_folder_prevails",
      note="Substantially complete. A path home, with dates. And the record, this time, corrected to match the year.")]),

N("review_partial", 347, "The Review \u2014 Filed at the Door", [
 "February. The agency's summary goes first, and it is the only version the judge has had time to read in advance.",
 "Your folder arrives at the door \u2014 true, complete, and heavy in the wrong way: a year of paper, unindexed, encountered for the first time in a hearing's short hour. The judge takes what an hour can hold. The certificate's May date lands. The referral's five missing months land, partly. The visits, spring's visits, remain a notebook being described rather than a record being read.",
 "Nobody in the room disbelieves you. Disbelief was never the obstacle. Time, in a courtroom, is a form of evidence too, and you spent yours on truth instead of timing.",
], [C("Listen to the order", "end_partly_credited",
      note="Some of it lands. The rest is scheduled to be re-proved, a second year running.")]),

N("review_services_only", 347, "The Review \u2014 Half a Wall", [
 "February. Your services paper does its work completely: the certificate, the completion letter, the referral pages \u2014 the plan's service lines, credited, corrected, closed. The judge says so, in so many words.",
 "Then visits. And here the room runs on the only visit record the agency can produce: a log that begins in August, and your spoken account of a spring of twice-weekly visits that no filed paper corroborates. You are believed, visibly, as a person. You are not credited, on paper, as a record \u2014 because belief and credit are different currencies, and February pays in the second one.",
 "The judge's questions get shorter. The summary's version of the spring \u2014 visits beginning, for all official purposes, in autumn \u2014 survives, because nothing filed stood against it.",
], [C("Listen to the order", "end_agency_summary",
      note="Services: yours. Visits: the log's. A year, split down the middle by what was filed.")]),

N("review_divided", 347, "The Review \u2014 The Order and the Archive", [
 "February. The shortest hearing of the year. The agency's draft, uncontested, becomes the hearing's ground: a mother who completed her program eventually, engaged with housing help, steadied her visits by August \u2014 and who, on that described record, has done enough that the court orders reunification to proceed, on a plan, with dates.",
 "You won the order. Eli comes home on the order's schedule. Nobody in the room says an untrue word.",
 "And the file closes over the year like water: eventually, engaged, by August. The spring you actually lived \u2014 the initialled promises, the ten Tuesdays, the visits that started in March \u2014 remains in one place only: a folder, in your home, that the official world will never open again.",
], [C("Take the order home, and the folder with it", "end_divided",
      note="Both are yours. They do not say the same thing. That is the ending.")]),

N("end_folder_prevails", 354, "Ending \u2014 The Folder Prevails", [], ending=True, debrief=[
 "WHAT THE RECORD HELD (the hidden record, revealed): A year with no continuous author on the agency's side \u2014 three workers, two transfer summaries, a migrated visit log, a referral that existed for five months only as an initialled promise in a parent's notebook \u2014 set against one folder that never changed hands. The hearing did not hold that you were the better parent in some general sense. It held something narrower and more useful: where the two records conflicted, yours was contemporaneous, dated, duplicated, and filed in time to be read, and the agency's was a reconstruction. February credited the record that was written while the year was happening.",
 "THE LAW UNDER THIS PATH: The plan is now marked substantially complete and the reunification path reopens, on the court's order, with reviews continuing. The dates that frame the future are exact: Eli was placed on March 2, 2026, and the federal fifteen-month date \u2014 15 of the most recent 22 months \u2014 arrives June 2, 2027 (42 U.S.C. \u00a7 675(5)(E)), with its three exceptions (relative care; a documented compelling reason; services identified as necessary but not provided \u2014 a description your folder, unusually, could prove from the agency's own pages). February's corrected record is what any later room will read if that date ever matters. Your look at that record began with a request the regulation answers in five words \u2014 it 'shall be released upon request' (55 Pa. Code \u00a7 3130.44(d)) \u2014 and your counsel, who told you in March to start the folder, was your right from the first hearing (42 Pa.C.S. \u00a7 6337).",
 "THE HONEST PART: Paper prevailed this time partly because a judge read carefully, a third worker confirmed the seams aloud, and an agency lawyer presented a summary fairly instead of defending it past its evidence. Another courtroom, a busier morning, a supervisor who chose pride over accuracy, and the same folder is a parent's scrapbook against the state's bound file. Workers, judges, and luck are all in this ending. What your choices controlled was narrower and real: when the official memory failed \u2014 as, across three workers, it was always likely to \u2014 there existed a second memory, boring and dated and duplicated, that February could adopt as its own. You built the spare record in public, all year, for the price of evenings. It was enough. It is not guaranteed to be enough, and no honest debrief will promise that it is.",
]),
N("end_partly_credited", 354, "Ending \u2014 Partly Credited", [], ending=True, debrief=[
 "WHAT THE RECORD HELD (the hidden record, revealed): A complete and truthful folder that arrived too late to be read \u2014 the year's most common tragedy in miniature. The certificate's May date was credited; the referral's lost months were credited in part; the lost referrals are now re-made, properly, with confirmations. But a record credited in part, in an hour, leaves the rest of the year where summaries put it, and the clock consequences of the seams remain: reviews extend, the plan's completion is argued again from better paper, and time \u2014 Eli's time, the only currency this system spends that cannot be refunded \u2014 has been spent on re-proving a spring that was proved once already.",
 "THE LAW UNDER THIS PATH: Nothing in this ending decides the case's end. The re-made referrals and corrected lines now sit in the record where later rooms will find them, and the framing date remains exact and ahead: placement on March 2, 2026 means 15 of the most recent 22 months arrives June 2, 2027 (42 U.S.C. \u00a7 675(5)(E)), with its exceptions \u2014 including, documented now in the file itself, services the plan identified as necessary that were not provided when promised. Your counsel's right to build that record with you (42 Pa.C.S. \u00a7 6337) and your right to the agency's record on request (55 Pa. Code \u00a7 3130.44(d)) are both still yours, and both now have a year of your own paper behind them.",
 "THE HONEST PART: Partly credited is what truth usually gets when it arrives at the door instead of in the mail: believed, in principle, and rationed, in practice. The same folder, filed a month early, plausibly ends this February differently \u2014 which is this scenario's coldest lesson, and not a moral one. You were not less truthful in this ending. You were later. Judges are people with an hour; workers are people with a summary; the system is people all the way down, which is why a record that hopes to survive it must arrive early enough for people to actually read. What remains yours is that the re-proving is now done, on the record, once \u2014 no third worker can un-send a confirmation that a court has read.",
]),
N("end_agency_summary", 354, "Ending \u2014 The Summary Prevails, in Part", [], ending=True, debrief=[
 "WHAT THE RECORD HELD (the hidden record, revealed): A split year, divided exactly along the line between what was filed and what was only true. The services you could prove on paper \u2014 certificate, completion letter, the referrals with their dates \u2014 were credited in full; the plan's service lines are corrected and closed. The visits you could only describe were not: a center log that begins in August, and a judge paying, as February pays, in filed paper, left the official spring visit-less. You documented the programs and not, in the end, the visits \u2014 and the file will remember the year in precisely that shape: a mother who completed services in a spring she apparently did not visit through.",
 "THE LAW UNDER THIS PATH: The case continues from this divided record, and the division is what later rooms will inherit. The framing date does not move: placed March 2, 2026, Eli reaches 15 of the most recent 22 months on June 2, 2027 (42 U.S.C. \u00a7 675(5)(E)); if that date ever brings a filing question, its exceptions \u2014 relative care, a documented compelling reason, or necessary services not provided \u2014 will be argued from a record that now credits your services and understates your visits, which is a weaker hand than the year actually dealt you. The remedies that remain are the unglamorous ones this scenario teaches: file the notebook's visit history now, late but dated and contemporaneous in origin; keep requesting the record as it grows (55 Pa. Code \u00a7 3130.44(d)); and let counsel (42 Pa.C.S. \u00a7 6337) put every correction in writing, where corrections live.",
 "THE HONEST PART: It would be comforting to say the judge got the visits wrong. She did not, on the paper she was given \u2014 and that is the point this ending exists to make. Belief is not credit; a spoken spring, however true, weighs what spoken things weigh against a bound log with a start date in it. Workers changed, systems migrated, a clerk apologized \u2014 the luck and machinery in this outcome are real, and none of them required anyone's ill will. What was in your control was the difference between a notebook described and a notebook filed. Next time, file the notebook. That sentence, unkind as it sounds, is the most loving one this scenario owns.",
]),
N("end_divided", 354, "Ending \u2014 Reunified, Understated", [], ending=True, debrief=[
 "WHAT THE RECORD HELD (the hidden record, revealed): Two endings in one envelope. In the world: reunification, ordered, on a schedule \u2014 Eli home, the plan closing behind him, a card that says FEBRUARY filed by its maker under 'art.' In the archive: a year that reads as eventual, engaged, by August \u2014 a spring of initialled promises, ten Tuesdays, and March visits that the official record will describe, forever, as if they had barely happened. The divided ending is not a loss. It is what winning looks like when the price of the order was leaving the summary uncorrected: the child comes home, and the history stays wrong.",
 "THE LAW UNDER THIS PATH: Legally, the order is the whole ballgame this February: reunification proceeds, and the case moves toward closing on its ordinary terms, with the federal date \u2014 June 2, 2027, fifteen months from the March 2, 2026 placement (42 U.S.C. \u00a7 675(5)(E)) \u2014 expected to pass with Eli home, where it has nothing to operate on. But records outlive cases. If this family ever meets this system again, the first thing read will be this file, in this shape; the folder that contradicts it sits in a private home, aging, unaudited, one house-move away from legend. A parent's own record remains available to them on request (55 Pa. Code \u00a7 3130.44(d)) \u2014 including, should it ever matter, the corrected version February could have entered and didn't, because nobody asked it to.",
 "THE HONEST PART: Reasonable parents choose this ending every week, and this debrief will not call it a mistake: Eli's homecoming is worth more than his mother's vindication, and she knew it, and she was right. The honesty is only about the price, which is real and permanent in one direction: systems remember what they wrote, not what happened, and the next worker, the next judge, the next February will meet the summary first and the truth, if at all, second. Workers, judges, and luck ran this year alongside you; the archive is simply the part of their work that never goes home. Keep the folder anyway. Paper kept by the person it is about has a way of being needed exactly once, years later, on a day nobody circled.",
]),
]

# =====================================================================
if __name__ == "__main__":
    scen33 = build({"title": "The First 90 Days",
                    "subtitle": "Scenario 33 \u2014 The Two Petitions (a fictional composite)",
                    "startDateISO": S33_START.isoformat(), "startNode": "start",
                    "startCash": 180, "tier": "Complex",
                    "summary": "Eleven months in, the agency moves to change the goal while you are still finishing the plan \u2014 run Track A in the open while Track B is built, and make the two timelines meet on the record."},
                   s33_nodes, S33_START)
    print(emit(scen33, 33, "The Two Petitions",
               "This scenario depicts a dependency goal-change / concurrent-planning fight \u2014 two tracks, two timelines, and a hearing \u2014 told through procedure and paperwork. There is no graphic content. Players may skip any scene or use the quick exit at any time.",
               S33_START))
    scen34 = build({"title": "The First 90 Days",
                    "subtitle": "Scenario 34 \u2014 The Missed Year (a fictional composite)",
                    "startDateISO": S34_START.isoformat(), "startNode": "start",
                    "startCash": 140, "tier": "Complex",
                    "summary": "Three caseworkers in twelve months lose a referral, a completion, and a season of visits \u2014 your own folder is the only continuous record in the case."},
                   s34_nodes, S34_START)
    print(emit(scen34, 34, "The Missed Year",
               "This scenario depicts a dependency case across a year of caseworker turnover \u2014 a removal, services, visits, and a review hearing \u2014 told through procedure and paperwork. There is no graphic content. Players may skip any scene or use the quick exit at any time.",
               S34_START))
