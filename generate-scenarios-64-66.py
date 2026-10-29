#!/usr/bin/env python3
"""Generator for Scenarios 64, 65 and 66 of 'The First 90 Days'.
One data source emits both the .json and the -script.md for each scenario,
so they match node-for-node by construction. Every kicker and every
in-body date is computed with datetime from the scenario start date;
the S64 ASFA date (placement + 15 calendar months) is computed and asserted."""
import json, os
from datetime import date, timedelta

OUT = os.path.dirname(os.path.abspath(__file__))

def add_months(d, months):
    m = d.month - 1 + months
    y = d.year + m // 12
    m = m % 12 + 1
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

def emit(scen, num, title_line, content_note, start, tier="Complex"):
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
    L.append(f"Start date: {fmt(start)}. Day offsets are days since the scenario's start date. Tier: {tier}.")
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
                if c.get("requiresFlags"):
                    ann.append("REQUIRES: " + ", ".join(c["requiresFlags"]))
                if c.get("requiresNoFlags"):
                    ann.append("REQUIRES-NOT: " + ", ".join(c["requiresNoFlags"]))
                suffix = f"  _({'; '.join(ann)})_" if ann else ""
                L.append(f"- {c['text']} \u2192 **{c['next']}**{suffix}")
                if c.get("note"):
                    L.append(f"  - NOTE (shown after choosing): {c['note']}")
    path_m = os.path.join(OUT, f"scenario-{num}-script.md")
    with open(path_m, "w") as f:
        f.write("\n".join(L) + "\n")
    return path_j, path_m

# =====================================================================
# SCENARIO 64 — Fifteen Months of Paper
# Placement: Monday, November 3, 2025 (pre-story). Story opens at
# month 10: Monday, August 31, 2026. ASFA 15-month date:
# Nov 3, 2025 + 15 calendar months = Wednesday, February 3, 2027
# = dayOffset 156 from the start date (both asserted).
# =====================================================================
S64_START = date(2026, 8, 31)
S64_PLACED = date(2025, 11, 3)
S64_ASFA = add_months(S64_PLACED, 15)
assert S64_START.strftime("%A") == "Monday"
assert S64_PLACED == date(2025, 11, 3) and S64_PLACED.strftime("%A") == "Monday"
assert S64_ASFA == date(2027, 2, 3) and S64_ASFA.strftime("%A") == "Wednesday", S64_ASFA
assert (S64_ASFA - S64_START).days == 156

def d64(off):
    return fmt(S64_START + timedelta(days=off))

s64_nodes = [
N("start", 0, "Month Ten, Quietly", [
 "Your daughter Amara is five. She was placed on " + fmt(S64_PLACED) + ", and she has lived since then with a foster family whose porch she can describe better than yours. You are Katrina, her mother. Your visits are kept, your screens are clean, and the parenting and recovery program the court ordered — the one you waited to enter, then finished late but finished — is behind you, with a certificate in a folder that is getting thick.",
 "This morning there is no letter, no hearing, no crisis. There is only a calendar on the refrigerator and the quiet math you have started doing without deciding to: Amara has been placed ten months. Somewhere in the case there is a date the calendar is walking toward, whether anyone mentions it or not.",
 "Your lawyer, Mr. Sandoval, has asked you to come in this week. Not because anything happened, he said on the phone. Because of when it is.",
], [C("Go to the appointment — and bring the folder, as always", "counsel_meet",
      note="He keeps a second calendar on his desk, with one date circled in pencil. You have never asked whose date it is.")]),

N("counsel_meet", 4, "The Date in Pencil", [
 "Mr. Sandoval is your lawyer in this case, as the law provides for a parent (42 Pa.C.S. \u00a7 6337). He turns his desk calendar around so you can read the circled date yourself: " + fmt(S64_ASFA) + ".",
 "\u201cAmara was placed on " + fmt(S64_PLACED) + ". When a child has been in care for fifteen of the most recent twenty-two months, the federal law generally presses the agency to file a petition to end parental rights. Fifteen months from her placement is " + fmt(S64_ASFA) + " \u2014 " + d64(156) + " in this story's counting, one hundred fifty-six days from the morning this chapter opened.\u201d",
 "\u201cGenerally,\u201d he says, \u201cis doing real work in that sentence. There are exceptions, and one of them is about you \u2014 or rather, about what was done for you. Sit down. This is the meeting where we talk about paper.\u201d",
], [C("Sit down, and ask him to say the exception slowly", "exception_explained",
      addHidden=["Counsel meeting \u2014 ASFA date " + fmt(S64_ASFA) + " named; services exception explained"],
      note="He writes three numbered lines on a legal pad before he says another word.")]),

N("exception_explained", 7, "Three Lines on a Legal Pad", [
 "\u201cAt fifteen of the most recent twenty-two months, the agency is generally to file \u2014 unless an exception is documented (42 U.S.C. \u00a7 675(5)(E)). The child is being cared for by a relative. Or there is a documented compelling reason that filing would not serve the child. Or \u2014 line three, ours \u2014 the agency has not provided the services it identified as necessary for the child's safe return.\u201d",
 "\u201cNow hear the discipline of it,\u201d he says, \u201cbecause this is where people fool themselves. The exception is record-dependent. It is an argument that exists only to the extent the file documents services that were identified and then not provided. It speaks to the filing decision \u2014 whether a petition gets filed at all. If a petition is filed anyway, the agency would still have to prove it by clear and convincing evidence at a hearing, and no one in this room is deciding that hearing today. Our whole job between now and " + fmt(S64_ASFA) + " is the file.\u201d",
 "\u201cSo,\u201d he says. \u201cTell me about the services. Not what you remember. What the paper says.\u201d",
], [C("Start where he starts: ask what the file itself says about each service", "records_beat",
      note="He nods like you have just said the first correct sentence of the autumn.")]),

N("records_beat", 11, "Asking for the File", [
 "There is a right that does not depend on any hearing: a parent may request the case record from the county agency, and under the regulation the material \u201cshall be released upon request\u201d (55 Pa. Code \u00a7 3130.44(d)). Mr. Sandoval drafts the request on his letterhead while you watch — the full chronology, the service plan, the referral records, all of it.",
 "\u201cWe are not accusing anyone of anything,\u201d he says. \u201cWe are reading. What the chronology says about the program, the therapy, and the housing list is either our argument or our answer. Either way, we need the agency's own words, not our memories of them.\u201d",
], [C("Sign the written request for the complete record this week", "file_review",
      setFlags=["recordsRequested"], cash=-6,
      addHidden=["Case record requested in writing under 55 Pa. Code \u00a7 3130.44(d)"],
      note="Signed, dated, copied. The request itself is now a page in the file it asks about."),
    C("Wait until after the next review \u2014 one fight at a time", "summary_only",
      note="Understandable. The chronology will be written this autumn either way. It will simply be written without your reading it.")]),

N("file_review", 16, "Reading the Chronology", [
 "The record arrives: thick, partly blacked out, and readable. You and Mr. Sandoval go through it at his conference table with three highlighters, one per service, and the file's own story of your case is plainer than you feared and stranger than you remembered.",
 "The parenting and recovery program: the chronology says \u201creferred\u201d in the second month of the case, and then says nothing at all for eight weeks, and then says \u201cparent enrolled.\u201d The waitlist you lived — the eight weeks between the referral and the door opening — is present in the file only as a silence between two verbs.",
 "Therapy: \u201creferral sent,\u201d one line, one date. Six weeks later, a second line: \u201creferral re-sent.\u201d Nothing between them explains the gap. Housing: your applications are noted, complete, dated. The list, the chronology agrees with everyone, is the list.",
], [C("Mark the three gaps and ask what proof could fill each one", "chronology_gaps",
      addHidden=["Agency chronology read with counsel \u2014 program gap, therapy gap, housing status identified"],
      note="\u201cDocuments,\u201d he says. \u201cEach gap either gets a document or it stays a memory. Let's go find out which.\u201d")]),

N("summary_only", 16, "Working from Summaries", [
 "Without the record, you work from the review reports — which are fair, and warm about your visits, and summaries all the same. A summary tells you what its writer thought mattered. It does not show you the chronology's silences: the eight weeks between \u201creferred\u201d and \u201cenrolled,\u201d or the six weeks between a referral sent and a referral re-sent.",
 "Mr. Sandoval is blunt, kindly: \u201cWe can still do the archaeology. We will be doing it from other people's paper \u2014 the program's, the provider's, your own folder \u2014 instead of the agency's. It is more work, and some of it we may not be able to check. Start with what the providers kept.\u201d",
], [C("Start the archaeology with the providers' own paper", "chronology_gaps",
      note="The gaps are real either way. The question the autumn asks is whether they are documented.")]),

N("chronology_gaps", 20, "Three Gaps, Three Questions", [
 "On the legal pad, under the three exception lines, Mr. Sandoval writes three questions. One: was the program's eight-week waitlist ever put in writing by the program \u2014 a letter, a notice, anything with a date? Two: why was the therapy referral re-sent six weeks after it was sent \u2014 and does the provider have paper that says why? Three: housing \u2014 is there dated proof your applications were complete, so the file cannot quietly re-describe the list as your delay?",
 "\u201cYour completions are real,\u201d he says. \u201cClean screens, kept visits, a finished program. Nobody is building those. What we are building is the other half of the story: what the system owed, when it owed it, and what actually happened. Both halves have to be in the file. Right now only one of them is.\u201d",
], [C("Begin with the program \u2014 the waitlist letter, if it exists", "prog_beat",
      note="Eight weeks, in the second month of a fifteen-month case. In this arithmetic, eight weeks is not a detail.")]),

N("prog_beat", 25, "The Program Remembers Differently", [
 "The parenting and recovery program's office keeps a front desk, a sign-in archive, and — the intake coordinator tells you, looking at her screen — a standard waitlist notice that went out to everyone referred that season. \u201cWe sent those to the agency and to the parent,\u201d she says. \u201cYours would have said the list was running about eight weeks.\u201d",
 "You do not remember receiving it. That happens, in the second month of a case like this, to mail that arrives between a removal and everything that follows a removal. The coordinator can reprint it — with your name, your referral date, and the eight-week estimate on it — if you ask. Asking, as ever in this system, is the whole mechanism.",
], [C("Ask, in writing, for a reprint of the waitlist notice with your dates on it", "prog_letter",
      setFlags=["waitlistDoc"], cash=-4,
      addHidden=["Program waitlist \u2014 8-week wait at month 2, confirmed by the program in writing"],
      note="She prints it while you wait. Eight weeks, with your name on it, in the program's own letterhead."),
    C("Trust your memory \u2014 you know you waited; everyone knows you waited", "prog_letter",
      note="Everyone may well know it. The file, which is the only audience in February, knows what it is shown.")]),

N("prog_letter", 31, "Eight Weeks, on Letterhead", [
 "Whether it arrived as a reprint or not at all, the waitlist is now a dated fact in your folder or a dated memory in your head — and the difference between those two will matter in a room you have not entered yet.",
 "Mr. Sandoval files the copy, if there is a copy, behind tab one of a thin new binder he labels, in pencil, with the February date. \u201cOne service,\u201d he says. \u201cDocumented or not. Two to go. Therapy next — and for therapy, we ask the provider, not the agency. The answer to a re-sent referral lives at the address it was sent to.\u201d",
], [C("Go to the therapy provider and ask about the first referral", "therapy_beat",
      note="The provider's office is across town. The bus ride is the cheapest research in this case.")]),

N("therapy_beat", 37, "The Referral That Went Nowhere", [
 "The therapy provider's intake office is small and unhurried. The coordinator pulls your name, frowns at the screen, and tells you the story in the order it happened to her: the first referral arrived while their intake was closed — a staffing gap, since filled — and was returned. A second referral arrived six weeks later. That one she acted on. Your therapy began from the second referral, and you completed it, and her file says so.",
 "\u201cWe sent a letter about the closure,\u201d she says. \u201cTo the agency. It would be in our file here too, if you need it.\u201d She says it the way people say things that are simply true and simply available — which, in this system, is exactly what makes them easy to walk past.",
], [C("Ask for a copy of the closed-intake letter, with its date", "therapy_letter",
      setFlags=["therapyDoc"], cash=-4,
      addHidden=["Therapy referral \u2014 first referral sent to a provider whose intake was closed; re-sent six weeks later; closure letter obtained"],
      note="One page: the closure, the dates, the provider's own signature. The six weeks now have an author, and it is not you."),
    C("Thank her and go \u2014 her word is clear, and you were told not to make waves", "therapy_letter",
      note="Her word is clear. Words, in February, will be weighed against paper, and hers is not in the file unless someone puts it there.")]),

N("therapy_letter", 43, "Six Weeks, with an Author", [
 "Tab two of the thin binder. Mr. Sandoval reads the closure letter, if you brought it, twice. \u201cNotice what this is not,\u201d he says. \u201cIt is not anyone's fault worth naming. A provider closed an intake; an agency re-sent a referral six weeks later. Nobody in this story is a villain. It is arithmetic. But arithmetic is what the exception is made of: a service identified as necessary, and not provided, for six documented weeks.\u201d",
 "If the letter stayed at the provider's office, he writes the visit up from your account and marks the page, in pencil, with the word he has used all autumn: memory. \u201cWe proceed,\u201d he says. \u201cHousing next. Yours is the strangest of the three, because on housing, you did everything and the answer is still a list.\u201d",
], [C("Turn to housing \u2014 and your own applications", "housing_beat",
      note="Your folder holds the receipts for this one. It has held them all along.")]),

N("housing_beat", 49, "The List Is the List", [
 "Housing was ordered at disposition, as it so often is, in the form the system can order it: apply, document, wait. You applied — completely, early, and more than once — and the waiting list has moved at the speed waiting lists move, which is to say at its own speed and no one else's.",
 "Ms. Yoder, your worker, does not pretend otherwise when you meet. \u201cYour applications are complete,\u201d she says. \u201cI have said so in every report. The list is the list.\u201d It is an honest sentence, and it is already in the file in summary form. What is not in the file, yet, is the dated proof underneath it: the stamped application copies, with the dates you filed them, in a row.",
], [C("Assemble the dated application copies into one stamped set for the file", "housing_docs",
      setFlags=["housingDoc"], cash=-5,
      addHidden=["Housing \u2014 dated, complete applications assembled; delay attributable to the waiting list"],
      note="Three applications, three stamps, one page of dates. Nobody can re-describe this as a late start."),
    C("Rely on Ms. Yoder's reports \u2014 she has always described them fairly", "housing_docs",
      note="She has. Summaries describe; stamps prove. February is a month that prefers proof.")]),

N("housing_docs", 55, "Tab Three", [
 "Tab three. The binder is less thin now. Mr. Sandoval turns the pages slowly: a waitlist with a letterhead, a referral with a closure letter, a list with stamped dates — or, in the places where the autumn's asking did not happen, your own clear recollection, written in your hand, which he does not mock and does not overvalue.",
 "\u201cHousing is different from the other two,\u201d he says, \u201cand we will say so, because accuracy is our whole argument. You were provided the service the plan identified \u2014 the application process \u2014 and it is the list that is slow. That is not the exception. The exception lives in tabs one and two. Tab three is there so that no one can move the delay from tabs one and two onto you.\u201d",
], [C("Ask what the binder becomes next", "gaplog_beat",
      note="\u201cA log,\u201d he says. \u201cYours. Dated. Built from documents, so that anyone who reads it can check it.\u201d")]),

N("gaplog_beat", 62, "The Log, in Your Hand", [
 "The gap log is a single document, and it is yours: a running, dated list of every services gap in the case, each entry built from a document — the service identified at disposition, the date it was supposed to begin, what actually happened, and the paper that proves it. Program: referred, eight-week waitlist, letter attached. Therapy: referral sent to a closed intake, re-sent six weeks later, letter attached. Housing: applications complete and dated; list pending; no gap claimed.",
 "Built from documents, it is an exhibit. Built from memory, it is a claim. Mr. Sandoval will not file the second kind, and he tells you so plainly, because a log that overclaims by one entry loses the entries that were true.",
], [C("Build the log from the documents only \u2014 every entry checkable", "screens_beat",
      setFlags=["gapLog"], cash=-6,
      addHidden=["Parent's dated services-gap log assembled from documents"],
      note="Shorter than your memory of the year. Stronger, for exactly that reason."),
    C("Write the log from memory \u2014 faster, and you lived every week of it", "screens_beat",
      note="You did live it. The log will now be weighed as testimony, not as an exhibit, and February weighs those differently.")]),

N("screens_beat", 68, "The Rest of the Plan, Kept", [
 "Meanwhile — and this word does a great deal of work in a case at month eleven — the rest of the plan runs on. Screens, clean, on schedule. Visits, kept, every one, including the one in the rain and the one the week the bus route changed. Your shift supervisor signs your schedule accommodation without being asked twice, which is its own kind of document.",
 "This matters to the February argument more than it may appear to. The exception is not a claim that you were failed at everything. It is a claim about two services, made by a parent whose own lines in the file are clean enough that no one can answer the claim by pointing at her. Both halves. In the file. That was the assignment.",
], [C("File the updated screen results and visit record with Mr. Sandoval's office", "review12_notice",
      addHidden=["Parent's own compliance current \u2014 screens clean, visits kept, program completed"],
      note="Your half of the story, current to the week, in the same binder as the system's half.")]),

N("review12_notice", 75, "The Month-Twelve Review Approaches", [
 "The notice arrives for the month-twelve permanency review. Twelve months is a number the system notices: reviews take stock, reports are written fresh, and the word permanency starts appearing in letters where the word progress used to live.",
 "Ms. Yoder's report, when the draft reaches Mr. Sandoval, is fair. Your progress is reported as it happened — program completed, therapy completed, housing pending on a list, visits warm and consistent. The exception is not mentioned. It has not been raised yet, by anyone, anywhere. Mr. Sandoval reads the draft twice and says the thing he has been saying since September, in a new tense: \u201cNot yet is still a choice. After February, it stops being one.\u201d",
], [C("Go to the review with the folder, and the binder inside it", "review12",
      note="The binder comes. Whether it speaks today is a decision you and Mr. Sandoval make in the hallway.")]),

N("review12", 82, "Month Twelve, on the Record", [
 "The month-twelve review is orderly, and almost gentle. Placement continues — that was never really in question today. Your progress is reported fairly, by the agency's own witness, in words close to the ones in the draft. The court sets the next review and turns to dates, and for one sentence the February date is in the room: the court notes the case's age and the federal timeline that runs with it, the way a court notes weather it can see coming.",
 "The exception is not raised. Not by the agency, which has not reached its decision; not by you, because the packet is a filing, not a speech, and filings have their own week. You walk out with Amara still placed, your progress on the record, and a binder that has not yet been asked to do its work.",
], [C("Ask Mr. Sandoval, in the hallway, what happens between now and February", "amara_visit",
      note="\u201cA letter, most likely,\u201d he says. \u201cTheirs first. Then ours.\u201d")]),

N("amara_visit", 89, "Saturday, Month Twelve", [
 "Saturday's visit is at the foster family's home this month, and Amara shows you the reading corner she has arranged for herself, with the seriousness of a person giving a tour of a house she expects to live in for a while, because she does, because she is five and a while is the size of her planning.",
 "She asks whether your house has a reading corner yet. You tell her the truth at her size: grown-ups are still working out the timing, a judge helps decide, and your job right now is the visits and the paperwork. She accepts this with the completeness children accept things, and assigns you a book to read so you can discuss it.",
 "On the bus home you think about the binder. It is not a reading corner. It is the paperwork version of one: a place prepared, in advance, for a day whose date you know.",
], [C("Write the visit up in your folder that night, dated", "agency_letter",
      note="Contemporaneous, as ever: written while it is true in detail.")]),

N("agency_letter", 97, "The Letter", [
 "The agency's letter arrives on agency letterhead, and it is exactly the letter Mr. Sandoval predicted, which does not make it smaller. The agency writes that, as the case approaches fifteen months in care, it will weigh whether to file a petition to terminate parental rights at the fifteen-month date \u2014 " + fmt(S64_ASFA) + " \u2014 and that its decision will be made on the case record.",
 "\u201cOn the case record,\u201d Mr. Sandoval says, reading it over your shoulder in his office. \u201cThat phrase is the whole autumn, in their words this time. The record currently contains your progress, fairly reported, and our binder, unfiled. A decision made on the record can only use what the record holds.\u201d",
], [C("Ask him to lay out the packet decision, all three ways, honestly", "counsel_packet",
      note="He takes out a fresh legal pad. He has been waiting, you realize, for the letter to make this meeting necessary.")]),

N("counsel_packet", 103, "The Packet Decision", [
 "\u201cThree ways,\u201d Mr. Sandoval says. \u201cOne: we assemble the services-exception packet \u2014 the gap log, the waitlist letter, the closure letter, the housing dates, your compliance record \u2014 and we file it, in writing, with the agency and the court, before the February date. The exception then exists in the file the decision is made on. Two: we raise it orally at the next review \u2014 your voice, my voice, the court reporter's record of two voices, and no exhibits. Three: we wait, keep your record clean, and trust that the agency's own file carries the gaps.\u201d",
 "\u201cYou have seen their file,\u201d he says, or, on the autumn where the file was never requested, \u201cyou have seen their summaries. You know what their chronology does with a gap. It leaves a silence between two verbs, and silences get read as the parent's.\u201d",
 "\u201cMy advice is the packet. It is also, in the end, your case and your decision.\u201d",
], [C("Decide together, this week, while deciding is still early", "packet_decision",
      note="February does not move. Everything else in this meeting can.")]),

N("packet_decision", 109, "Three Ways, One Chosen", [
 "The packet, if it is filed, must be filed whole: the log, the letters, the dates, and a short covering statement from Mr. Sandoval that says what the packet is and is not. It is not an accusation. It does not argue anyone failed on purpose. It documents that two services the plan identified as necessary for Amara's safe return were not provided for documented weeks, and it asks that the exception be documented when the filing decision is made.",
 "Raising it orally costs nothing and exhibits nothing. Waiting costs nothing and risks everything the chronology's silences can do. The choice, like most choices in this system, is not between a good option and a bad one. It is between paper and its absence, made by a person who has learned what paper is for.",
], [C("Assemble and file the written services-exception packet with counsel", "packet_filed_scene",
      setFlags=["packetFiled"], cash=-10, requiresFlags=["gapLog", "recordsRequested"],
      addHidden=["Written services-exception packet filed with counsel before the 15-month date"],
      note="Filed, stamped, copied \u2014 the exception now exists in the file the decision will be made on."),
    C("Raise the exception orally at the next review instead", "oral_scene",
      setFlags=["oralRaised"],
      note="Your voice and Mr. Sandoval's, on the review record. The exhibits stay in the binder, in his office."),
    C("Wait \u2014 keep your record clean and trust the agency's file", "wait_scene",
      note="A clean record and an unfiled binder. February will decide what that combination is worth.")]),

N("packet_filed_scene", 115, "Filed, Stamped, Copied", [
 "The packet goes in on a weekday morning, with a stamp and a copy for your folder, and the ordinary anticlimax of important paper: a clerk, a receipt, a binder that is now a filing. Mr. Sandoval's covering statement is two pages, and its last paragraph is the discipline of the whole scenario in one sentence: the exception speaks to the filing decision, and nothing in the packet asks anyone to decide anything else.",
 "Ms. Yoder, at your next check-in, mentions it without edge: \u201cI saw the packet. The dates are the dates.\u201d It is not agreement. It is something the system values almost as much: an acknowledgment, from the other side of the table, that the paper says what it says.",
], [C("Keep the visits, the screens, and the routine exactly as they are", "month13_work",
      note="The packet is filed. The case, meanwhile, is still a child's ordinary weeks, and you keep them.")]),

N("oral_scene", 115, "Saved for the Review", [
 "The decision is made and noted in Mr. Sandoval's file: the exception will be raised orally at the month-fourteen review. The binder stays in his office, its tabs in order, its letters unfiled. \u201cWe will say it clearly,\u201d he says. \u201cI want you to understand what clearly means in a system that decides from files. It means two people said a true thing in a room, and a transcript exists. Transcripts are read. Exhibits are weighed.\u201d",
 "You keep the visits, the screens, the routine. Your half of the file stays clean. The other half stays, for now, a silence between two verbs, with a speech scheduled to answer it.",
], [C("Prepare the oral statement with Mr. Sandoval, word by word", "month13_work",
      note="If the record will hold only words, the words will at least be exact.")]),

N("wait_scene", 115, "The Clean Record Strategy", [
 "The decision is made and noted: wait. Your record is clean, your progress is fairly reported, and the agency's own people know about the waitlist and the referral \u2014 you have heard them say so, in rooms, in words. Mr. Sandoval does not argue; he has given his advice, and he writes yours down beside it, because that too is what lawyers are for.",
 "\u201cOne thing, then,\u201d he says. \u201cIf we are trusting their file, understand what their file is. It is a chronology with silences in it. In February, someone will read those silences. I hope, for Amara's sake and yours, they read them kindly.\u201d",
], [C("Keep everything clean, and let the autumn finish quietly", "month13_work",
      note="Quiet is also a strategy. February will grade it.")]),

N("month13_work", 122, "Month Thirteen, at Work", [
 "Month thirteen is mostly logistics, which is to say it is mostly the case. A shift change at work that threatens the Saturday visit, solved with a supervisor's signature. A screen rescheduled by the provider, documented by you the same day, in writing, because you document things now the way other people breathe.",
 "Amara's foster mother mentions, kindly, that the agency has asked about \u201cschedules in February.\u201d She does not know more than that, and says so. February is acquiring a shape in other people's calendars too. Yours has held its shape since September: a date, circled in pencil, with a binder underneath it.",
], [C("Confirm the February dates in writing with everyone who needs them", "review14_notice",
      note="One more week where the paper and the life agree with each other.")]),

N("review14_notice", 130, "The Month-Fourteen Review Approaches", [
 "The notice for the month-fourteen review arrives with a sentence that was not in the month-twelve notice: the court will also hear the agency's position on the approaching fifteen-month date. The review has become, in part, a preview of February.",
 "Mr. Sandoval prepares you the way he prepares for everything: from the file outward. What the file holds depends, now, on decisions already made \u2014 a packet filed, a speech prepared, or a clean record and a hope. \u201cWhatever February does,\u201d he says, \u201cit will do it from paper. Our remaining work is to make sure the paper in the room is the paper we chose.\u201d",
], [C("Go to the month-fourteen review", "review14",
      note="Fourteen months. The date in pencil is now weeks, not months, away.")]),

N("review14", 137, "Month Fourteen, on the Record", [
 "The month-fourteen review is longer than the last one, and the February date is named in it plainly, by the judge, on the record: " + fmt(S64_ASFA) + ", fifteen months. The agency states that its filing decision will be made and documented by that date. Your progress is reported, fairly again. Placement continues.",
 "If the packet was filed, it is referenced by exhibit, the way filed things are \u2014 briefly, and with its dates undisputed. If the exception is raised orally here, it is said clearly, by Mr. Sandoval, in full sentences, and the court reporter takes it down, and what the record holds afterward is a transcript of a claim and no exhibits beneath it. If nothing is raised, the review is warm, brief, and silent on the only question February asks.",
], [C("Ask, before you leave, exactly what remains between here and the date", "supervisor_change",
      addHidden=["Month-14 review \u2014 15-month date named on the record; filing decision announced for " + fmt(S64_ASFA)],
      note="\u201cWeeks of ordinary life,\u201d Mr. Sandoval says. \u201cAnd one personnel change I just heard about.\u201d")]),

N("supervisor_change", 144, "A New Supervisor Reads Cold", [
 "Personnel changes are weather in this system, and this month the weather turns: Ms. Yoder's supervisor — the person who will sign the filing decision — is new, and reviews the file cold, the way new supervisors do, knowing no one in it and remembering nothing about it that the file does not say.",
 "This is the moment the whole design of the autumn was quietly about. A cold reader cannot be told what everyone in the case happens to know. She can only read. If the packet is in the file, she reads letters with dates on them. If it is not, she reads a chronology with silences in it, and a transcript, perhaps, of two voices claiming what the silences mean.",
 "\u201cFiles outlive the people who remember the case,\u201d Mr. Sandoval says. \u201cWe have known that since September. February's reader just proved it in November's clothing.\u201d",
], [C("Ask whether anything can still be added to the file before the date", "filing_eve",
      note="\u201cVery little, and nothing new,\u201d he says. \u201cWhat is filed is filed. That was always the point.\u201d")]),

N("filing_eve", 151, "The Week Before", [
 "The last week runs on rails laid months ago. A visit, kept. A screen, clean. Amara's book, read, ready to discuss. The binder \u2014 filed or unfiled \u2014 sits where it sits. There is nothing left to build, which is itself the lesson this scenario has been teaching since the refrigerator calendar: by the week before a date like this, the case is the record, and the record is finished being written by everyone.",
 "Mr. Sandoval calls the night before. \u201cWhatever tomorrow documents,\u201d he says, \u201cremember what it is. A filing decision. Not a verdict on you, not a hearing, not an ending of anything except a question about a petition. Amara's case goes on either way, and so do you.\u201d",
], [C("Sleep, as well as a person can, and go to his office in the morning", "filing_day",
      note=d64(156) + ". Fifteen months, to the day the count runs from.")]),

N("filing_day", 156, "The Fifteenth Month", [
 "Wednesday, February 3, 2027 \u2014 computed in this story as it is computed in the law: fifteen months from the Monday Amara was placed, " + fmt(S64_PLACED) + ". The agency's filing decision is documented today, on the record the autumn built.",
 "There is no courtroom drama in this scene, because filing decisions rarely have any. There is a file, a cold reader's review of it, a decision, and a document that records the decision and its reasons. What those reasons can honestly be depends \u2014 as Mr. Sandoval said in September, as the agency's own letter said in its own words \u2014 on what the record holds.",
], [C("The decision rests on the filed packet \u2014 the exception, documented, with its letters and dates", "end_notfiled",
      requiresFlags=["packetFiled", "waitlistDoc", "therapyDoc"],
      note="The file answers February in the file's own language."),
    C("The decision rests on the packet as filed \u2014 filed in writing, on a thinner documentary base", "end_filed_complete",
      requiresFlags=["packetFiled"], requiresNoFlags=["waitlistDoc"],
      note="Paper was filed. February will weigh exactly the paper there is."),
    C("The decision rests on the packet as filed \u2014 filed, with the referral letter but not the waitlist letter", "end_filed_complete",
      requiresFlags=["packetFiled", "therapyDoc"], requiresNoFlags=["waitlistDoc"],
      note="Paper was filed. February will weigh exactly the paper there is."),
    C("The decision rests on the oral record \u2014 the exception, argued from memory and transcript", "end_thin",
      requiresFlags=["oralRaised"],
      note="Two voices, clearly heard, with no exhibits beneath them."),
    C("The decision rests on the record as it stands \u2014 progress, fairly reported, and nothing else filed", "end_date",
      requiresNoFlags=["packetFiled", "oralRaised"],
      note="The date arrives at a file that was never asked to answer it.")]),

N("end_notfiled", 163, "Ending \u2014 Not Filed: The Exception, Documented", [
 "The agency's documented decision, a week after the date: it will not file a petition at this time. The decision document names the reason in the statute's own shape \u2014 services the plan identified as necessary for Amara's safe return were not provided for documented periods \u2014 and attaches, by reference, your packet: the waitlist letter, the closure letter, the dated log. The exception is documented. That is the sentence the whole autumn was built to make possible.",
 "The same document orders the next thing, and the next thing is not a return \u2014 it is a transition plan toward home, with steps, dates, and a review. Amara is still placed at this scenario's curtain. She sleeps tonight where she slept last night. What changed is the direction of the paperwork, and in this system, direction is not nothing. Direction is most of it.",
], ending=True, debrief=[
 "WHAT THE RECORD HELD (the hidden record, revealed): A two-half file. Your half: screens clean, visits kept, the ordered program finished \u2014 late, and finished. The system's half, documented by your autumn's asking: an eight-week program waitlist at month two, on the program's own letterhead; a therapy referral sent to a provider whose intake had closed, re-sent six weeks later, with the closure letter to prove it; housing applications complete and dated, with no gap claimed where no gap existed. Assembled into a dated gap log and filed, with counsel, as a written packet before the date \u2014 while a new supervisor, reading cold, could find every word of it in the file.",
 "THE LAW UNDER THIS PATH: At 15 of the most recent 22 months, the agency is generally to file a termination petition UNLESS an exception is documented: (i) the child is being cared for by a relative, (ii) a documented compelling reason that filing would not serve the child, or (iii) the agency has not provided services it identified as necessary for the child's safe return (42 U.S.C. \u00a7 675(5)(E)). The services exception is record-dependent: it exists as an argument only to the extent the file documents identified-but-not-provided services, and it speaks to the filing decision \u2014 which is all that was decided here. No petition exists, so nothing about grounds was decided, and no hearing on grounds was held or depicted. Your route to the file began with the record released on request (55 Pa. Code \u00a7 3130.44(d)) and counsel's work throughout (42 Pa.C.S. \u00a7 6337). This ending is labeled PARTIAL plainly: Amara is still placed; a transition plan toward home is ordered; the case continues.",
 "THE HONEST PART: This outcome was not produced by effort alone, and it is not a verdict on your worth as a parent. A different supervisor could have read the same packet and filed anyway, forcing the exception to be argued in a harder room; a waitlist letter never printed, or a closure letter never kept, would have thinned the argument to memory. Workers, supervisors, judges, and the plain luck of which offices keep their letters all hold pieces of this ending. What your choices controlled was narrower and real: whether the gaps everyone agreed happened were documented in the file the decision was made on \u2014 dated, checkable, and already there when a stranger read it cold.",
]),
N("end_filed_complete", 163, "Ending \u2014 Filed, With the Record Complete", [
 "The agency's documented decision, a week after the date: a petition is filed. The decision document does not pretend your packet does not exist \u2014 it engages it, disputes the weight of the documented gaps against Amara's time in care, and files anyway. The exception is documented in the file. The filing happened despite it.",
 "Mr. Sandoval reads the decision twice and says the truest available sentence: \u201cThis is now a different kind of case, and it starts from a better record than it would have. A petition is an allegation with a burden attached. The burden is theirs, and it is clear and convincing, and the hearing that would test it has not happened and is not this scenario's to depict.\u201d",
], ending=True, debrief=[
 "WHAT THE RECORD HELD (the hidden record, revealed): A filed packet, on a thinner documentary base than the autumn offered \u2014 some of the gaps documented by letter, some carried by your log and your account. It was enough to be engaged, answered, and preserved in the agency's own decision document. It was not enough, on this reader, to stop the filing. Both of those facts are the record working exactly as records work: paper does not compel a reader; it constrains what an honest reader can say.",
 "THE LAW UNDER THIS PATH: The services exception (42 U.S.C. \u00a7 675(5)(E)) speaks to the filing decision; it does not forbid a filing, and it decided nothing here beyond being documented and answered. A petition, once filed, must still be proven by clear and convincing evidence at a hearing \u2014 a hearing this scenario does not depict and whose outcome no part of this game predicts. Nothing about grounds has been decided. Your counsel remains your right (42 Pa.C.S. \u00a7 6337), and the record you built began with its release on request (55 Pa. Code \u00a7 3130.44(d)). This ending is partial: Amara is still placed, the case continues on a new track, and your documented exception travels with it into every later room.",
 "THE HONEST PART: A filing is a serious turn, and this debrief does not soften it into a win. It is also not a verdict on you: it is one documented decision, by one cold reader, weighing a child's fifteen months against documented gaps and coming down on the side of asking a court. A different reader could have come down the other way on this same paper \u2014 that is not a flaw in the scenario; it is the scenario. What your choices bought was that the argument was made from documents, engaged on its merits, and preserved \u2014 instead of arriving, if it arrived at all, as a parent's memory against a chronology's silence.",
]),
N("end_thin", 160, "Ending \u2014 Filed, Over a Thin File", [
 "The agency's documented decision: a petition is filed. Its reasoning is short, and its shortness is the story. The exception was raised, the decision notes \u2014 orally, at review \u2014 and the file, the decision continues, does not document services identified and not provided. The waitlist you lived and the referral you waited on are present in the decision only as claims, weighed as claims are weighed: sincerely noted, and set aside for want of paper.",
 "In Mr. Sandoval's office, the binder sits on the conference table, its tabs in order, its letters \u2014 the ones that were obtained \u2014 still inside it. \u201cEverything in that binder is true,\u201d he says. \u201cTrue was never the test. Filed was the test.\u201d",
], ending=True, debrief=[
 "WHAT THE RECORD HELD (the hidden record, revealed): A warm review record, a clean compliance file, a transcript in which the exception was argued clearly and in full sentences \u2014 and, beneath the transcript, no exhibits: the waitlist carried as memory, the referral gap carried as an account, the packet never assembled or filed. The chronology's silences were answered by voices, and a filing decision made on a file cannot be carried by voices, however true.",
 "THE LAW UNDER THIS PATH: The services exception (42 U.S.C. \u00a7 675(5)(E)) is record-dependent \u2014 an argument that exists only to the extent the file documents identified-but-not-provided services \u2014 and it speaks to the filing decision, which is the decision that was just made against you. A petition is not a termination: if the agency proceeds, it must prove its case by clear and convincing evidence at a hearing this scenario does not depict, and the gaps, if they can still be documented, can still be documented \u2014 the provider's letter exists whether or not it was in February's file. Counsel remains your right (42 Pa.C.S. \u00a7 6337); your own record remains yours on request (55 Pa. Code \u00a7 3130.44(d)).",
 "THE HONEST PART: This ending is not a judgment that you failed Amara; your completions were real, your visits were kept, and everyone in the case knew about the waitlist. It is a judgment about the medium: this system decides from files, and a fact that lives only in memory enters the file as a claim about a fact. A kinder reader, a warmer supervisor, a worker who put the letters in herself \u2014 any of them could have changed this ending without your changing a thing. Workers, supervisors, and luck hold their pieces here too. Yours was the asking, in writing, in the autumn, when asking could still become paper.",
]),
N("end_date", 158, "Ending \u2014 The Date Arrives Anyway", [
 "The agency's documented decision arrives by mail, and it is brief in the way of decisions that were never really contested: the child has been in care fifteen of the most recent twenty-two months; the agency will file. Your progress is noted, fairly, in a paragraph. The services are listed as provided, in the chronology's grammar \u2014 referred, enrolled; sent, re-sent \u2014 with the silences between the verbs left exactly as silent as they were in September.",
 "Nothing in the decision is cruel, and no one in it is a villain. It is a date, doing what dates do to files that were never asked to answer them.",
], ending=True, debrief=[
 "WHAT THE RECORD HELD (the hidden record, revealed): Your progress, fairly reported, and nothing else: no record request that surfaced the chronology, no letters obtained from the program or the provider, no gap log, no packet. The eight-week waitlist and the six-week referral gap happened \u2014 they are in this debrief because they were in your life \u2014 but they never entered the file as documents, and a filing decision made on the file could not see them. The date did not defeat an argument. It arrived where no argument had been filed.",
 "THE LAW UNDER THIS PATH: At 15 of the most recent 22 months, the filing the federal law generally directs (42 U.S.C. \u00a7 675(5)(E)) proceeded, with none of its three documented exceptions established in the record \u2014 not relative care, not a documented compelling reason, and not the services exception, which is record-dependent and was never documented. A petition is still only a petition: the agency would have to prove it by clear and convincing evidence at a hearing this scenario does not depict, and counsel (42 Pa.C.S. \u00a7 6337) and your own record, released on request (55 Pa. Code \u00a7 3130.44(d)), remain available for the case that now follows. Nothing about grounds has been decided by anyone.",
 "THE HONEST PART: Dates do not grade effort, and this ending must not be read as one: your screens were clean, your visits were kept, your program was finished, and none of that was enough, because the question February asked was never \u2018did she do her part\u2019 \u2014 it was \u2018what does the file document.\u2019 A worker who filed the letters herself, a supervisor who asked about the gaps, a lawyer who pressed in September instead of advising in October \u2014 the same luck and people run through every ending of this scenario. The difference here is only that the autumn's asking never happened, and paper, unlike memory, cannot be filed retroactively.",
]),
]
assert len(s64_nodes) == 34, len(s64_nodes)
# S64 reaches 42 nodes in the assembly section below, after inserted beats.
assert sum(1 for n in s64_nodes if n.get("ending")) == 4
# S64 is built in the assembly section below, after inserted beats are merged.
# The filing-day assertion (dayOffset 156 == Wednesday, February 3, 2027)
# runs there, against the built scenario.

# =====================================================================
# SCENARIO 65 — Two Plans
# Start: Monday, September 21, 2026. Hattie, 4, placed pre-story.
# =====================================================================
S65_START = date(2026, 9, 21)
assert S65_START.strftime("%A") == "Monday"

def d65(off):
    return fmt(S65_START + timedelta(days=off))

s65_nodes = [
N("start", 0, "Two Plans, One Kitchen Table", [
 "Your daughter Hattie is four, and she is in foster care \u2014 placed before this story opens, in a season neither of you litigates anymore at the kitchen table. You are Trina, her mother. Across the table, with his own mug and his own stack of paper, is Curtis, her father. You are separated. You are also, in the eyes of the case, something more complicated than separated: two parties, two case plans, two workers, two files.",
 "Your plan runs through Ms. Whelan. His runs through Mr. Murdock. Your obligations are yours; his are his; Hattie is the same small person in both files, which is the only simple sentence in this scenario.",
 "Tonight the two plans are spread across one kitchen table, because the car, the calendar, and Hattie herself are shared even where the paperwork is not. What happens next depends less on either plan than on whether the two plans ever learn to read each other.",
], [C("Put the two plans side by side and read them as one calendar", "two_binders",
      note="Two binders, if you make them. One shoebox, if you don't. The case will be able to tell the difference.")]),

N("two_binders", 3, "Two Binders or One Shoebox", [
 "Trina's plan: a parenting program, Friday-morning screens, supervised visits with a make-up slot on Tuesday evenings \u2014 the only evening slot the visit center offers. Curtis's plan: a Tuesday-evening group across town, a class with a Friday-morning check-in \u2014 also across town, in the other direction \u2014 and his own visits, on his own days.",
 "There is one car. It is registered to neither plan. The plans were each written, carefully and in good faith, by a worker who had read one file. Nobody has yet been assigned to read both.",
 "You each have a right to counsel in this case (42 Pa.C.S. \u00a7 6337) \u2014 separate counsel, as separated parties usually have \u2014 and you each have your own folder to keep, or not to keep.",
], [C("Give each plan its own binder, its own folder, its own color of tab", "calendar_beat",
      setFlags=["ownFolder"], cash=-8,
      addHidden=["Each parent keeping their own folder \u2014 two binders, separately maintained"],
      note="Eight dollars of office supplies. The first structural repair in the case, and it fits in a shopping bag."),
    C("Keep everything together in the shoebox \u2014 you share a daughter, after all", "calendar_beat",
      note="You do share a daughter. The files, as you are about to learn, share rather more than that.")]),

N("calendar_beat", 6, "The Collision Calendar", [
 "Laid side by side, the collisions draw themselves. His Tuesday-evening group \u2014 mandatory, attendance taken \u2014 sits exactly on top of the only Tuesday-evening make-up visit slot you can use when a visit is missed. If Hattie's visit ever needs making up on a Tuesday, one of you must be in two places, and the car must be in three.",
 "Friday mornings are worse: your screens are across town to the east, his class check-in is across town to the west, both in the same ninety minutes, and there is one car between you and a bus route that serves neither appointment well.",
 "Neither collision is anyone's defiance. They are two well-made plans that have never met. The question is whether they meet on paper now \u2014 or in review reports later, translated into a language of missed appointments.",
], [C("Write it down \u2014 both collisions, with dates and times, before either one happens", "deconflict_beat",
      addHidden=["Schedule collisions identified in advance \u2014 Tuesday group vs. make-up visit; Friday screens vs. class check-in; one car"],
      note="A collision predicted in writing is a logistics problem. The same collision, unexplained, is a compliance problem.")]),

N("deconflict_beat", 9, "Letters to Two Workers", [
 "The repair available is unglamorous and entirely within your power: write to both workers \u2014 Ms. Whelan and Mr. Murdock, a copy to each, so each file holds the whole picture \u2014 identifying the two collisions in advance and asking, in writing, for the schedules to be de-conflicted: a different make-up slot, a moved check-in, anything decided before a Tuesday or a Friday decides it for you.",
 "The alternative is the way most families handle it, and it is understandable: manage week to week, swap the car, run late occasionally, and apologize after. Apologies are sincere. They are also, in a file, indistinguishable from excuses \u2014 and a file cannot tell which Tuesday an apology belongs to.",
], [C("Send the written de-confliction request to BOTH workers, a copy for each file", "car_beat",
      setFlags=["deconflictLetter"], cash=-4,
      addHidden=["Written de-confliction request sent to both workers, copies for both files"],
      note="Two envelopes, two stamps, one identical page. Each worker now holds the other plan's problem, in writing, before it happens."),
    C("Handle it week to week \u2014 you have always managed, and letters feel like escalation", "car_beat",
      note="Letters are escalation only if the alternative works. The calendar on the table says what the alternative is.")]),

N("car_beat", 13, "One Car, Honestly Described", [
 "The car is a 2014 sedan with a tire that loses air slowly and a fuel gauge nobody fully trusts. It is also, functionally, a third case plan: every appointment in both files silently assumes it. Neither worker wrote \u201ccar\u201d into a plan, because plans do not have a line for the thing everything depends on.",
 "This week it holds. Both of you make everything, by margins measured in minutes and one memorable sprint across a parking lot. A system that runs on margins like these is not being defied when a margin fails. It is being described \u2014 later, by whoever writes the description.",
], [C("Log the week's trips in each folder \u2014 who drove, who arrived, when", "screens_beat",
      note="Boring, contemporaneous, and \u2014 if a Friday ever goes wrong \u2014 the difference between a story and a record.")]),

N("screens_beat", 17, "Friday, the First Time", [
 "Friday morning, the collision's gentler rehearsal: your screen to the east, his check-in to the west, the car doing arithmetic at forty miles an hour. You are both on time \u2014 you by four minutes, Curtis by two \u2014 and both providers note attendance without comment, the way providers note weather.",
 "It works, this Friday. It works the way a rope bridge works: honestly, and with no capacity for a second traveler. Both of you understand, driving home in silence, that the question is not whether a Friday will fail. It is what the files will say on the Friday that does.",
], [C("Note both arrivals, with times, in both folders that night", "his_miss_setup",
      addHidden=["Friday collision survived \u2014 both appointments kept, arrivals logged in both folders"],
      note="Kept Fridays are evidence too. They establish what the pattern actually is, before a single miss defines it.")]),

N("his_miss_setup", 21, "The Week Everything Lands at Once", [
 "Some weeks are scheduled by an enemy, though none exists: Curtis's employer moves his shift, the car goes in for the tire and stays for the brake line, and his program schedules a make-up session on the one evening that was supposed to be free. You watch the week assemble itself at the kitchen table like weather coming over a hill.",
 "His screen \u2014 his own obligation, on his own plan \u2014 is Friday. The car will be on a lift on Friday. The bus to the screening site runs, technically, in the way that aqueducts run: impressively, and not to where he needs to be by when he needs to be there.",
 "\u201cI'll call Murdock,\u201d he says. \u201cFirst thing.\u201d Calls, in this system, are the rain of good intentions: real, sincere, and gone by the time anyone reads the ground.",
], [C("Urge him to put the car trouble in writing to Mr. Murdock before Friday", "his_miss",
      note="He nods. Whether the nod becomes a letter is next week's file entry."),
    C("Let him handle his plan his way \u2014 his worker, his call", "his_miss",
      note="His plan, his worker, his call. The files, unfortunately, do not observe the same boundaries.")]),

N("his_miss", 24, "The Missed Screen", [
 "Friday: the car is still on the lift at nine, the screen is at nine-thirty across town, and the arithmetic that worked at forty miles an hour does not work at zero. Curtis misses the screen. He calls Mr. Murdock's office from the repair shop, explains, is told to reschedule, and does \u2014 for the following week, which he keeps.",
 "A missed screen, rescheduled and kept, on a plan being worked in good faith: in the life, that is a bad Friday. In a file, it is a line. Where the line gets written \u2014 and in whose file \u2014 is the subject of the rest of this scenario.",
], [C("Ask him that night exactly what was said, and write it down, dated", "her_report",
      addHidden=["Father's missed screen \u2014 car on a lift; called worker same day; rescheduled and kept"],
      note="His miss, his facts, your handwriting, tonight. Contemporaneous notes are the poor family's subpoena.")]),

N("her_report", 28, "A Line in the Wrong Report", [
 "Your review report arrives first \u2014 Ms. Whelan's summary of your plan, your progress, your compliance. It is mostly fair, and mostly yours, until the paragraph near the end, which you read twice: \u201cThe household's compliance was complicated this month by a missed screen.\u201d",
 "The household. Your report does not say whose screen it was. It does not need to: a reader of your file \u2014 a supervisor, a judge, a stranger reading cold in some later month \u2014 will file that sentence under the name on the folder. The name on the folder is yours.",
 "Curtis stares at the page over your shoulder. \u201cThat's my miss,\u201d he says. \u201cIn your report.\u201d \u201cYes,\u201d you say. \u201cWelcome to my file.\u201d",
], [C("Read the rest of both reports side by side before reacting", "visit_makeup",
      addHidden=["File bleed identified \u2014 father's missed screen summarized inside mother's review report"],
      note="If his worst line is in your file, the next question writes itself: what of yours is in his?")]),

N("visit_makeup", 32, "The Tuesday That Tests the Calendar", [
 "As if scheduled by the scenario itself \u2014 which, between us, it was \u2014 this week's visit is cut short by a staffing closure at the visit center, and the make-up is offered for Tuesday evening. Tuesday evening: his group's night. The collision the calendar predicted in September arrives in October, on schedule, like a train in a country where trains are a rumor.",
 "If the de-confliction letters went out, there is a reply in the file \u2014 a moved slot, an alternate evening, a problem solved on paper before it became a missed anything. If they did not, there is a choice with no good side: his mandatory group, or your make-up visit, and the car keys on the table between you like a referee.",
], [C("Use whatever the paper provides \u2014 the de-conflicted slot, or the least-bad Tuesday", "records_beat65",
      note="Either way, tonight writes a line in both files. The only question is which line."),
    C("One of you skips, and you agree to explain it together afterward", "records_beat65", cash=-12,
      note="Explanations after are the currency this scenario keeps devaluing. You spend twelve dollars on fuel doing it the hard way.")]),

N("records_beat65", 36, "Asking for Both Files", [
 "There is a way to see the whole board instead of your half of it: each of you may request your own case record from the agency, and under the regulation it \u201cshall be released upon request\u201d (55 Pa. Code \u00a7 3130.44(d)). Your file is yours to request; his is his \u2014 neither of you can request the other's, which is precisely why both requests have to happen, on the same week, by design rather than by luck.",
 "Reading your own file tells you what your record says. Reading both, at one kitchen table, tells you what the case says \u2014 including every place the two have been poured into each other.",
], [C("Both of you sign and send your own records requests this week", "file_arrives65",
      setFlags=["recordsRequested"], cash=-6,
      addHidden=["Both parents requested their own complete files under 55 Pa. Code \u00a7 3130.44(d)"],
      note="Two requests, two stamps, one week. The bleed, wherever it is, is about to become visible."),
    C("Skip it \u2014 you have seen enough of your own report already", "partial_view",
      note="You have seen your report. A report is a summary of a file. The file is where summaries come from \u2014 and where they can be corrected.")]),

N("file_arrives65", 42, "Reading Each Other's Paper", [
 "The two files arrive in the same week and are read at the same table, each by its owner, aloud in the places that matter. Yours holds his missed screen, summarized as a household complication. His \u2014 Curtis reads this part twice, in the flat voice of a man reading his own weather \u2014 holds a note from your file: a visit described as \u201cended late; parent reminded about time boundaries,\u201d on a day you remember as a visit that ended when the center closed early.",
 "Neither line is a lie, exactly. Each is a true sentence filed in the wrong life, where it will do the wrong work: summaries are written from files, reviews are argued from summaries, and no later reader will know which parent a stray line belonged to unless someone separates the records \u2014 in writing, with dates.",
], [C("Mark every stray line in both files, with its rightful owner and date", "her_note_his_file",
      addHidden=["Cross-file bleed mapped \u2014 his missed screen in her file; her late visit note in his"],
      note="Two files, four hands, one highlighter each. The map of the bleed is the correction's first draft.")]),

N("partial_view", 42, "Working from One Report", [
 "Without the files, you work from what you have: your report's stray paragraph, and Curtis's recollection of a note in his. You know one line is misplaced. You suspect the other. Suspicion, at a review, is a feeling; a file, opened, is an exhibit.",
 "Curtis looks at the shoebox end of the table for a while. \u201cWe can still ask,\u201d he says. \u201cNothing says the request has an expiration date.\u201d He is right, and the lateness will be its own fact: corrections offered after a review has relied on the bleed repair less than corrections that arrive before one.",
], [C("Send both requests now \u2014 late, and anyway", "file_arrives65",
      setFlags=["recordsRequested"], cash=-6,
      note="Late paper is still paper. It simply has to introduce itself as late, and be dated honestly.")]),

N("her_note_his_file", 47, "The Late Visit Note", [
 "Your stray line deserves its own minute, because it is the smaller and more unfair of the two. The visit ended when the center closed early for staffing \u2014 a fact the center's own log holds. Somewhere between that log and Curtis's file, the early closing fell off the sentence, and what remained was a mother reminded about boundaries.",
 "\u201cIt's one line,\u201d Curtis says. \u201cIn my file it's nothing. In yours it would be a pattern.\u201d That is the whole mechanics of file bleed in one kitchen-table sentence: a line does its damage not where it is true, but where it lands \u2014 and it lands wherever the copying carried it.",
], [C("Get the visit center's own log entry for that day, in writing", "correction_beat",
      cash=-4,
      addHidden=["Visit-center log obtained \u2014 the 'late' visit ended at the center's early closing"],
      note="One page from the center: the closing time, in the center's own hand. Your line now has its other half."),
    C("Note your memory of the closing and move on to the correction", "correction_beat",
      note="Your memory is accurate. The center's log is evidence. At reviews, the difference is the whole game.")]),

N("correction_beat", 52, "Separating the Records, in Writing", [
 "The correction is a single written document, signed by both of you and filed with both workers, and its structure is the structure of the problem: item one, the missed screen belongs to Curtis's plan and Curtis's file, with its date, its reason, and its rescheduled completion; item two, the visit note belongs to Trina's file, corrected by the center's log where obtained; item three, a request that each report and summary hereafter describe each parent's compliance from that parent's own record.",
 "It accuses no one. Ms. Whelan and Mr. Murdock each wrote from what crossed their desks; the bleed happened between desks, in the copying, where no villain has ever lived. The correction simply asks the files to be two files again.",
], [C("File the written correction with BOTH workers, copies in both folders", "joint_visit",
      setFlags=["correctionFiled"], cash=-6,
      addHidden=["Written correction filed separating the two records, with dates, to both workers"],
      note="Filed before the reviews. Timing, in this system, is not a courtesy \u2014 it is the difference between a correction and an apology."),
    C("Raise it at the reviews instead \u2014 say it in the room, where people can hear it", "joint_visit",
      note="People will hear it. Reviews, however, are argued from reports already written \u2014 and the reports were written from the uncorrected files.")]),

N("joint_visit", 57, "The Joint Visit", [
 "There is a joint visit this month \u2014 both parents, Hattie, a room with a rug and a box of toys that has survived many families. It goes well in the unremarkable way that is, in a file, the most remarkable thing: snacks shared, a puzzle finished, a goodbye managed with a drawing assigned as homework.",
 "Afterward you compare notes on the bus \u2014 separately, into your own folders, a habit now \u2014 and learn the visit's paperwork fate: it is noted, warmly and completely, in one file. In the other, there is no entry at all. Not a bad entry. An absence, which a later summary may read as a visit one parent did not attend.",
], [C("Ask, in writing, that the joint visit be noted in both files", "joint_letter_beat",
      cash=-3,
      addHidden=["Joint visit \u2014 went well; noted in only one file; written request to note it in both"],
      note="One sentence, two envelopes. Absences are corrected the same way errors are: on paper, promptly."),
    C("Let it stand \u2014 the visit happened, and Hattie knows it", "joint_letter_beat",
      note="Hattie knows it. Hattie's knowledge, at four, does not get filed. That is not cynicism; it is the filing system.")]),

N("joint_letter_beat", 62, "One Letter, Two Signatures, Through Counsel", [
 "Your lawyers \u2014 each of you has your own, as the case requires (42 Pa.C.S. \u00a7 6337) \u2014 propose the capstone: one joint letter, through counsel, signed by both parents, confirming the state of the two records as corrected: schedules de-conflicted or noted as in conflict, each parent's compliance described from their own file, the joint visit noted in both.",
 "It is a short letter and a strange one, in a system built to process parents separately: two parties, acting jointly, about the accuracy of the paperwork that separates them. \u201cIt's the most cooperative document in either file,\u201d Curtis's lawyer says, \u201cand it is entirely about boundaries. Those two facts are not in tension. They are the same fact.\u201d",
], [C("Sign the joint letter through counsel and file it in both cases", "work_beat65",
      setFlags=["jointLetter"], cash=-6,
      addHidden=["Joint letter through counsel filed \u2014 corrected, separated records confirmed by both parents"],
      note="One letter, two signatures, two files. The records now agree with the family: separate, and on the same side of the table."),
    C("Skip the letter \u2014 the corrections already say what needs saying", "work_beat65",
      note="They may. The letter's job was never the words; it was the two signatures, in both files, before the reviews.")]),

N("work_beat65", 67, "Two Jobs, One Payday Problem", [
 "Parallel pressure, because this scenario believes in it: both employers adjust schedules in the same week \u2014 your unit short-staffed, his warehouse entering its season \u2014 and both new schedules are survivable only if the de-conflicted appointments stay de-conflicted. Paper that was filed in September is now load-bearing in November, or its absence is.",
 "You each do the unglamorous thing your folders have taught you: confirm the new schedules to your own worker, in writing, against your own plan, the week they change \u2014 not the week they collide.",
], [C("Send both schedule confirmations, each to your own worker, in writing", "hattie_beat",
      note="Two short letters. The files now contain the future as well as the past, which is rarer than it should be.")]),

N("hattie_beat", 72, "Hattie, at the Visit", [
 "Hattie has learned the visit room's geography the way children do, completely and without comment, and she has opinions about the puzzle with the lighthouse. During the visit she lines up the toy cars \u2014 there are two, one red, one blue \u2014 and drives each on its own road of rug-pattern, with great concentration, in opposite directions, arriving at the same lighthouse.",
 "\u201cThey both get there,\u201d she informs the room, \u201cbut on their OWN roads.\u201d Nobody writes this down. Some sentences do not need a file; they need a witness, and the room had two.",
], [C("Write the visit up in your own folder that night \u2014 your road, your words", "prep_split",
      note="Her road, her words. His folder will hold his. That is no longer a problem in this house; it is the system working.")]),

N("prep_split", 77, "Two Reviews, One Week", [
 "The reviews land in the same week \u2014 yours first, his two days later, because the system's calendar has a sense of humor it deploys sparingly. Two reviews means two reports, two summaries, two rooms in which a judge will meet each of you substantially through paper.",
 "Preparation, in this house, is now a two-desk exercise: your folder, current, on your plan; his folder, current, on his. What each room will actually see depends on the autumn's repairs: whether the schedules were de-conflicted in writing, whether the records were requested and read, whether the bleed was corrected on paper before the reports were written from the files \u2014 or whether the reports were written from the bleed, and the reviews will be argued uphill against them.",
], [C("Do a final two-folder check together, each parent auditing the other's dates", "reviews_week",
      note="Each of you checks the other's folder for one thing only: that it contains only its owner's life.")]),

N("reviews_week", 82, "The Reviews", [
 "Your review comes first. The report on the table is either the corrected one \u2014 your compliance, from your record, with the missed screen restored to its owner and the visit note restored to its context \u2014 or the report as first written, with the stray paragraph still in it, doing its quiet work in a room where you will have minutes to answer a sentence that took a month to write.",
 "His review, two days later, is the mirror: his miss, his rescheduling, his attendance \u2014 or your late visit, riding in his file, coloring a record it does not belong to. Two reviews, one family, and the question the whole autumn asked: are there two files in this case, or one file with two names on it?",
], [C("Both reviews are argued from the separated records \u2014 de-conflicted schedules, corrections filed before the reports were written", "end_two",
      requiresFlags=["deconflictLetter", "correctionFiled", "recordsRequested"],
      note="The paper arrived before the rooms did. That ordering is the entire strategy."),
    C("The corrections exist \u2014 but a review has already relied on the uncorrected file", "end_untangled",
      requiresFlags=["correctionFiled"], requiresNoFlags=["deconflictLetter"],
      note="Untangled, at last \u2014 and stamped with the date it was untangled, which is after a room already used the tangle."),
    C("The corrections exist, on a record the schedules never stopped colliding with", "end_untangled",
      requiresFlags=["correctionFiled", "recordsRequested"], requiresNoFlags=["deconflictLetter"],
      note="The records were separated; the calendar never was. One of the reviews paid for the difference."),
    C("The reviews are argued from the files as they accumulated \u2014 one household, one blended record", "end_one",
      requiresNoFlags=["correctionFiled"],
      note="No separation was ever filed. The files will now separate the family instead.")]),

N("end_two", 89, "Ending \u2014 Two Files, Two Records", [
 "Both reviews conclude the same way, which in this system counts as harmony: each plan on track, each parent's progress described in their own file, in their own name, from their own record. The Tuesday collision is de-conflicted in writing \u2014 a standing alternate slot, in both files. The Friday collision has a written arrangement of its own. The missed screen lives where it belongs, rescheduled and kept, in the file of the man who missed it.",
 "Hattie is still placed at this scenario's curtain, and this debrief will not pretend otherwise. What changed is the accuracy of the ground the case stands on: two parents, separated, each now legible to the system as the person they actually are \u2014 which is the minimum condition for either plan, or any plan, to be judged fairly.",
], ending=True, debrief=[
 "WHAT THE RECORDS HELD (the hidden record, revealed): Two files, repaired into two: the collisions named in writing before they happened, to both workers, with a copy in each file; each parent's own complete record requested and read at one table (55 Pa. Code \u00a7 3130.44(d)); the bleed mapped line by line \u2014 his missed screen in her report, her misread visit note in his file \u2014 and separated by a written correction filed with both workers before the review reports were written; a joint visit re-noted in both files; and one joint letter through counsel (42 Pa.C.S. \u00a7 6337), signed by two separated parents, confirming that the records were two records again.",
 "THE LAW UNDER THIS PATH: No statute in this scenario is exotic, and that is the point. Each parent is a party with their own right to counsel (42 Pa.C.S. \u00a7 6337) and their own record, released on their own request (55 Pa. Code \u00a7 3130.44(d)). Reviews are argued from reports, and reports are written from files \u2014 so the accuracy of each file, and the timing of its correction, is not housekeeping. It is the evidence. Nothing in this ending decides Hattie's placement, and no burden of proof was carried or tested in any hearing this scenario depicts; the reviews continued both plans, on track, which is a procedural outcome, honestly labeled PARTIAL: Hattie is still placed.",
 "THE HONEST PART: This ending is not a verdict on either parent, and the marriage was never the problem the scenario was about \u2014 the paperwork was. Two workers, each conscientious, each reading one file, produced the bleed by ordinary copying; a different pair of workers might have caught every stray line themselves, and a supervisor reading cold might have untangled this record with no correction at all. Workers, judges, and luck hold their pieces of this outcome. What the parents controlled was the asking \u2014 in writing, to both desks, before the rooms \u2014 and in a system that decides from files, asking early is most of what accuracy ever is.",
]),
N("end_untangled", 89, "Ending \u2014 Untangled, Late", [
 "The records are separated in the end \u2014 the correction is filed, the lines are restored to their owners, the files going forward will be two files. But the correction's date is later than one of the reviews, and that review was argued from the uncorrected report: the stray paragraph was read aloud, answered uphill in minutes, and noted by a judge who will remember the answering as much as the error.",
 "The judge, to her credit, says the fair thing in the room: the correction will be part of the record from today. From today is the operative phrase. Records can be repaired. The order in which a room met the facts cannot.",
], ending=True, debrief=[
 "WHAT THE RECORDS HELD (the hidden record, revealed): The same bleed as every path in this scenario \u2014 his missed screen summarized inside her report, her early-closing visit note riding in his file \u2014 discovered, mapped, and corrected in writing, but corrected after at least one review had already been written and argued from the blended version. The correction is real, permanent, and dated. Its date is its limitation.",
 "THE LAW UNDER THIS PATH: The mechanics are the scenario's verified set, arriving late: each parent's own record on their own request (55 Pa. Code \u00a7 3130.44(d)), counsel for each party (42 Pa.C.S. \u00a7 6337), and a written correction that any later reader \u2014 the next review, a cold-reading supervisor \u2014 must now reckon with. Nothing here decided placement, and no hearing in this scenario tested any burden of proof; both plans continue, one of them carrying the memory of a review argued against a sentence that was never its owner's. PARTIAL, honestly: the files are right now, and were wrong when it counted most.",
 "THE HONEST PART: Late truth is not worthless \u2014 it governs every future summary, and future summaries are most of a case \u2014 but this ending refuses to call it the same as early truth. A worker who cross-checked the files herself, a review postponed a week, a center log volunteered instead of requested: the luck and the people in this system could have landed this correction on the right side of the review without the parents lifting a pen. They could also, in a different week, have landed it later still. What the parents controlled was the discovery and the filing; the calendar controlled the rest, and the calendar, as ever, does not grade intentions.",
]),
N("end_one", 86, "Ending \u2014 One File, Shared Blame", [
 "The reviews are brief, in the way of rooms that believe the paper in front of them. Your report's stray paragraph is read as your complication. His file's borrowed visit note is read as his household's pattern. Neither of you says the sentence that would untangle it \u2014 it is my line, not hers; it is hers, not mine \u2014 in a form the record can keep, because the untangling was never done in the only medium the record keeps: writing, filed, before the reports.",
 "You leave in the same car, which is also the problem and also not the problem, and Hattie's two plans roll forward as one blended record in which each parent permanently carries the other's worst line \u2014 available, now, to every future summary written by anyone.",
], ending=True, debrief=[
 "WHAT THE RECORDS HELD (the hidden record, revealed): One blended file wearing two names: a missed screen that belonged to the father, summarized in the mother's report as a household complication; a visit note that belonged to the mother, stripped of its early-closing context and resting in the father's file; a joint visit noted in one record and absent from the other. None of it was malice. All of it was copying \u2014 and none of it was ever corrected in writing, so all of it is now simply what the case says happened, to both of you, jointly, forever, in every summary yet to be written.",
 "THE LAW UNDER THIS PATH: The tools that would have prevented this ending were ordinary and available all autumn: separate counsel for each party (42 Pa.C.S. \u00a7 6337), each parent's own record released on their own request (55 Pa. Code \u00a7 3130.44(d)), and a written correction filed before the reports were drafted. They remain available now \u2014 a correction filed after these reviews still governs the next ones \u2014 but this scenario ends where its choices ended: with the reviews argued from the bleed. No placement was decided here and no burden was tested; both plans continue, each now heavier by one borrowed line. That weight, compounded over reviews, is how blended files quietly become outcomes.",
 "THE HONEST PART: Blame, in this ending's title, is the file's word, not this debrief's. Both parents worked their plans in good faith; the collisions were built by two careful workers who never read each other's plan; the bleed was an artifact of copying, not of character. A supervisor who read both files side by side \u2014 as the parents finally did at their kitchen table \u2014 could have separated this record in an afternoon. That no one did is a fact about the system's assignments, not about this family's worth. The lesson the scenario leaves is structural, and it is deliberately unglamorous: in a two-party case, accuracy is a filing, and filings have deadlines whether or not anyone announces them.",
]),
]
assert len(s65_nodes) == 24, len(s65_nodes)
# S65 is built in the assembly section below, after inserted beats are merged.

# =====================================================================
# SCENARIO 66 — The Discharge Summary
# Start: Monday, October 5, 2026. Dario, 10, placed pre-story.
# =====================================================================
S66_START = date(2026, 10, 5)
assert S66_START.strftime("%A") == "Monday"

def d66(off):
    return fmt(S66_START + timedelta(days=off))

s66_nodes = [
N("start", 0, "Week Ten of Twelve", [
 "You are Hector, and your son Dario is ten, and he is in foster care — placed before this story opens, in the season you are now ten weeks into repairing. The repair has a rhythm, and the rhythm is an intensive outpatient program: four evenings a week, a counselor named in your folder simply as the program, screens, group, and a chair that has become, in ten weeks, recognizably yours.",
 "You are doing well. That is not your assessment; it is the program's, said in progress notes and in the counselor's plain speech. Two weeks remain of the twelve the plan describes. Your worker, Ms. Nakamura, has your attendance in her reports, and Dario's visits — kept, every one — have settled into the shape of a father and son who know where the puzzle box lives.",
 "Doing well, in this system, is a sentence that has to survive being written down by other people. This scenario is about one sentence that almost didn't.",
], [C("Go to this evening's session, the way you have gone to all of them", "intake_echo",
      note="Week ten. The chair, the circle, the coffee. Ordinary is the achievement.")]),

N("intake_echo", 3, "How Week One Felt", [
 "Ten weeks ago you sat in the same circle certain you would be found out — as what, exactly, you could not have said; the feeling did not require specifics. The counselor's intake notes from that week, which you have never seen, would describe a man who answered questions as if each one were a door closing.",
 "You think about that man on the bus sometimes, the way you think about weather you have come through. The program's own paperwork tells the distance better than your memory does: attendance, participation, screens \u2014 a record of a man arriving, four evenings a week, until arriving became the least remarkable thing about him.",
], [C("Take your seat as the session begins", "program_rhythm",
      addHidden=["IOP \u2014 week 10 of 12; attendance and progress documented by the program"],
      note="The circle fills. The work, tonight, is ordinary work, done ordinarily well.")]),

N("program_rhythm", 6, "The Rhythm", [
 "The rhythm of a good week: session Monday, session Tuesday, Dario's visit Wednesday, session Thursday, screen Friday, and the weekend held together by a part-time job, a sponsor's phone number, and a kitchen calendar with the program's logo magnet on it.",
 "Ms. Nakamura's last report used the phrase \u201cengaged and progressing,\u201d which you read three times when your lawyer forwarded it, the way a man reads a letter from a country he hopes to live in. Your counsel in this case is your right (42 Pa.C.S. \u00a7 6337); the report is the agency's side of the conversation, and at week ten the conversation is, for once, easy to be part of.",
], [C("Keep the week exactly as it is built", "screens_routine",
      note="Rhythm is not the goal. Rhythm is how the goal gets reached without being carried.")]),

N("screens_routine", 9, "Screens, Filed by Others", [
 "Friday's screen is clean, as the others have been. The results travel to the agency on the provider's schedule \u2014 batched, late, in an envelope you will never see \u2014 which is one of this system's quiet arrangements: the facts of your progress exist in several buildings at once, and assemble into a file only when someone assembles them.",
 "Your counselor mentions, in passing, that your insurer's authorization letter arrived at the program's office this week. \u201cAdministrative,\u201d she says. \u201cI'll explain Monday. It's not about your progress.\u201d She says it easily, the way people deliver news they believe is small.",
], [C("Go home, and keep the weekend's rhythm", "sponsor_beat",
      note="Administrative. You have learned to hear that word the way sailors hear weather reports about other oceans.")]),

N("sponsor_beat", 11, "The Saturday Call", [
 "Saturday is your standing call with your sponsor \u2014 a man three years ahead of you in the same arithmetic, who treats your week the way an accountant treats a ledger: what came in, what went out, what is owed. You tell him about the authorization letter, and he is quiet a moment.",
 "\u201cPaper about benefits is paper about the program, not about you,\u201d he says. \u201cPrograms run on paper. When the paper changes, get the new paper. That's the whole sermon.\u201d You write it on the calendar, under the magnet, because this house writes things down now.",
], [C("Go to Wednesday's visit with Dario", "visit_beat66a",
      note="Dario has a new puzzle strategy to demonstrate. It involves, he has warned you, sorting by color first, \u2018like a professional.\u2019")]),

N("visit_beat66a", 14, "Wednesday with Dario", [
 "The visit room has a clock, a rug, and the puzzle. Dario sorts by color first, like a professional, and narrates his school week with the completeness of a ten-year-old who has decided which adult gets the full edition. You get the full edition. That fact is not in any file, and it is not nothing, and both of those things are true at once in this system, constantly.",
 "Ms. Nakamura's observer notes the visit in the warm, flat language of visit notes. You have stopped minding the flatness. Flat, you have learned, is what good looks like in a file: attended, engaged, appropriate, concluded on time. Your whole recovery is learning to be legible in flat sentences \u2014 which is why the sentence that is coming matters.",
], [C("Go to Monday's session, and the counselor's explanation", "benefit_letter",
      note="She has the insurer's letter in a folder with your name on it. Your name, lately, is on a number of folders.")]),

N("benefit_letter", 17, "The Letter About Sessions", [
 "The letter is from your insurer, and it is exactly as administrative as promised, which is to say it changes everything by arithmetic and nothing by judgment: your benefit covers a fixed number of intensive outpatient sessions. At the end of this week \u2014 week ten of twelve \u2014 the covered number will be reached. The program is not discharging you for cause. It is not discharging you for progress, exactly, either. It is discharging you because a count, in a benefits office, has finished counting.",
 "\u201cYou have done everything we asked,\u201d the counselor says. \u201cI want that sentence in the room before the other sentence: the program cannot bill sessions the benefit will not cover, and self-pay at this rate is not a real option for \u2014 for almost anyone,\u201d she finishes, accurately.",
 "There is a step-down program \u2014 a lower-intensity program, the natural next step for someone doing well \u2014 across town. It can take you in three weeks. Three weeks, in a twelve-week plan, is a gap the plan did not draw. The agency's goal line, meanwhile, sits in a file across town, and it reads, in full: complete IOP.",
], [C("Ask exactly what the discharge will say, and what you will be given", "counselor_talk",
      note="Two questions, and the answers to both of them are paper. You can feel the scenario narrowing to the size of a document.")]),

N("counselor_talk", 20, "A Counselor Who Is Sorry and Specific", [
 "She is sorry, and \u2014 what matters more, professionally and humanly \u2014 she is specific. The discharge summary, she explains, is the program's final document: it will state your attendance, your participation, your progress, and the reason for discharge. The reason, in your case, will read: benefit limit reached. Not unsuccessful. Not non-compliant. Arithmetic.",
 "\u201cThat summary is the program's last word about you,\u201d she says. \u201cIt goes where you send it. People leave here with it in their hands, or they leave here with my handshake and my good opinion. My good opinion does not photocopy.\u201d She is not being unkind. She is being a counselor at the exact moment her profession and the filing system agree with each other.",
], [C("Decide how you will leave this program, on its last day", "call_insurer",
      note="The last day is Friday. Between here and Friday there is one phone call you owe yourself first.")]),

N("call_insurer", 23, "Calling the Number on the Letter", [
 "The insurer's phone tree takes twenty minutes to reach a person, and the person is courteous and completely immovable: the session cap is the session cap; an appeal exists, on a timeline measured in weeks, decided by the same document that set the cap. You take the appeal information down \u2014 dated, with a reference number \u2014 because this house writes things down, and you file it without illusion: the appeal may matter to the benefit. It will not un-discharge you on Friday.",
 "What the call confirms is the counselor's arithmetic: week ten is the end of the covered count, through no decision of yours or the program's. Two systems \u2014 a benefit and a case plan \u2014 have been running on different clocks, and Friday is where the clocks collide.",
], [C("Go into the last week knowing exactly where you stand", "summary_choice",
      cash=-5,
      addHidden=["Insurer session cap verified by phone \u2014 discharge at week 10 is a benefit limit, not a program decision"],
      note="Five dollars of phone-era small change and one reference number later: the reason for Friday is now a fact you can cite, not a story you tell.")]),

N("summary_choice", 26, "The Last Day: Paper or Handshake", [
 "Friday, the last session. The circle does its closing ritual for a departing member \u2014 you are the third this season, and the other two, you realize, left to step-down programs and jobs, in the ordinary traffic of recovery. There is cake. There is a card the group signed. There is the counselor, at the door, with two versions of your departure in her hands, though only one of them is literally in her hands.",
 "The discharge summary exists \u2014 printed, signed, stating your progress, your attendance, and the reason: benefit limit. Getting it is a matter of asking for it, signing the release, and carrying it out the door. Not getting it is a matter of a handshake, a warm \u2018you did great,\u2019 and a summary that stays in the program's file, available in principle, absent in practice from every file where your future will be read.",
], [C("Ask for the discharge summary in writing before you leave \u2014 sign the release, take the document", "discharge_day",
      setFlags=["dischargeSummary"], cash=-4,
      addHidden=["Discharge summary obtained in writing \u2014 progress, attendance, reason: benefit limit"],
      note="Two pages, signed, warm from the printer. The program's last word about you, in your folder, where words about you belong."),
    C("Take the handshake and the \u2018you did great\u2019 \u2014 she knows how you did, and so do you", "discharge_day",
      note="She does, and you do. The agency's file, which knows neither of you, is about to be told something else entirely.")]),

N("discharge_day", 30, "Discharged, in the Ordinary Sense", [
 "You leave the program on a Friday evening with a card from the group, a cake's worth of goodwill, and either a signed summary in your folder or a compliment in your memory. The program's door closes behind you with the sound doors make. You have completed ten weeks of a twelve-week program, attended everything, progressed by every measure the program keeps \u2014 and your formal status, in the program's own system as of tonight, is: discharged.",
 "Words travel between systems badly. \u2018Discharged\u2019 is about to travel from a program that means it arithmetically to an agency whose goal line says complete \u2014 and whose coding, as you are about to learn, has no arithmetic in it at all.",
], [C("Go home, and call your sponsor from the kitchen", "last_day_scene",
      note="He asks one question: \u2018Did you get the paper?\u2019 Your answer to it is the rest of the scenario.")]),

N("last_day_scene", 33, "The Folder That Night", [
 "That night the folder comes out on the kitchen table, as it does in weeks when the case turns. Its contents are the case as you hold it: attendance printouts, the insurer's letter, the appeal reference number, the visit notes you keep copies of \u2014 and the summary, if you have it, or the space where the summary would go, if you don't.",
 "Your lawyer calls it \u2018your half of the file.\u2019 The other half is being written tonight, somewhere, by a system processing a discharge notification in the ordinary course: a form, a status field, a goal line. Two halves of the same ten weeks, about to describe them very differently.",
], [C("Wait for the agency's side of the week to arrive", "coding_beat",
      note="It arrives the way these things arrive: as a short phone call and a shorter sentence in a system.")]),

N("coding_beat", 36, "How the System Codes a Discharge", [
 "Ms. Nakamura calls on Tuesday, and she is careful in a way you have learned to respect: she tells you exactly what she can see. The program has notified the agency of the discharge. In the agency's system, the goal \u201ccomplete IOP\u201d has a status field, and the status that a discharge generates \u2014 any discharge, for any reason, before the program's full course \u2014 is the status the field was built to hold.",
 "\u201cOn my screen,\u201d she says, \u201cyour goal currently reads: not completed.\u201d She pauses. \u201cI know what your attendance has been, Hector. The field does not have a place for what I know. It has a place for documents. If the program's summary says what you tell me it says, the summary is how the field gets corrected.\u201d",
 "Four words \u2014 goal: not completed \u2014 now sit in a file where a review will read them, in a room you will have minutes to answer in. Ten weeks of evenings are currently losing to a status field.",
], [C("Ask her exactly what would correct the coding, and in what order", "worker_call",
      addHidden=["Agency system codes IOP discharge as 'goal not completed' \u2014 reason not carried by the coding"],
      note="Her answer is a list, and every item on it is paper, and every item has a deadline shaped like a review date.")]),

N("worker_call", 40, "Ms. Nakamura's List", [
 "Her list, in her order: one, the agency needs the discharge summary itself \u2014 attached to something in writing from you, so it enters the file as your submission with a date, not as a rumor at a check-in. Two, the step-down enrollment, when it happens, needs proof in the file the same way. Three, all of it needs to arrive before the review, because the review report will be written from the file as it stands when the report is drafted \u2014 not as it stands when you explain it in the room.",
 "\u201cI am not supposed to have a strategy for you,\u201d she says. \u201cYour lawyer is for strategy. I am telling you how the paperwork moves, because the paperwork is my job.\u201d It is the most useful conversation you have had with the agency in ten weeks, and it is entirely about envelopes.",
], [C("Call your lawyer that evening with the list in front of you", "nakamura_meeting",
      note="He will have the same list, in legal order. Lawyers and workers agree about envelopes more often than either admits.")]),

N("nakamura_meeting", 44, "The Plan, in Legal Order", [
 "Your lawyer \u2014 your counsel in this case, as the law provides (42 Pa.C.S. \u00a7 6337) \u2014 rearranges Ms. Nakamura's list into a campaign: notify the agency in writing, with the summary attached, before the review; enroll in the step-down the week it opens, with the enrollment proof filed the same week; request your own record, to see exactly how the goal was coded and what the chronology says; and file a written correction, so the file's own words get fixed, not just supplemented.",
 "\u201cNote the verb in step three,\u201d he says. \u201cYou may request your case record, and under the regulation it \u2018shall be released upon request\u2019 (55 Pa. Code \u00a7 3130.44(d)). We do not guess how the goal was coded. We read it.\u201d",
 "\u201cAnd the clock,\u201d he says, \u201cis the three weeks. The step-down cannot take you for three weeks. Those weeks are the gap the review will ask about. We do not hide the gap. We paper it, in advance, as what it is: a wait for the next program the plan's own logic points to.\u201d",
], [C("Start with the step-down's intake paperwork, this week", "gap_explained",
      note="The step-down's office keeps intake hours twice a week. The first one is tomorrow.")]),

N("gap_explained", 48, "Three Weeks, Explained Slowly", [
 "The gap, stated as the file will need it stated: you were discharged at week ten for a benefit limit. The step-down program \u2014 the clinically appropriate next step, the one your counselor named \u2014 has a three-week wait for an opening. In those three weeks you will attend your sponsor meetings, keep Dario's visits, keep your screens by arrangement with Ms. Nakamura's office, and wait, in the documented way, for a door that opens on a date the step-down itself will put in writing.",
 "A gap explained in advance, with dates and a named next door, is a transition. The same gap, discovered by a review from a status field, is a disappearance. The three weeks will be identical either way. The file's version of them is entirely up to the paperwork done inside them.",
], [C("Go to the step-down's intake office tomorrow", "stepdown_beat",
      note="Intake paperwork: the least dramatic document in recovery, and this month, the most important one.")]),

N("stepdown_beat", 52, "Intake Paperwork", [
 "The step-down program's intake office is a smaller room with the same species of forms. The coordinator confirms the opening \u2014 three weeks out, dated \u2014 and offers the two versions of enrollment this system always offers: she can take your completed intake packet now, stamp it, and give you a dated enrollment confirmation for the opening; or she can take your name and phone number and call you when the opening approaches, the way programs have always done it, warmly and without a stamp.",
], [C("Complete the intake packet now and take the dated enrollment confirmation", "gap_week",
      setFlags=["stepdownEnrolled"], cash=-6,
      addHidden=["Step-down program \u2014 intake completed; dated enrollment confirmation for opening in three weeks"],
      note="Stamped, dated, copied. In three weeks you will start; as of today, the file can already prove you will."),
    C("Leave your name and number \u2014 they'll call when the opening is close", "gap_week",
      note="They will call. Programs do. The file, meanwhile, will hold a three-week silence where an enrollment should be.")]),

N("gap_week", 57, "The Gap, Week One", [
 "Week one of the gap has no program evenings in it, and the evenings are long in a way the last ten weeks had trained you not to notice. You fill them the documented way: a support meeting, signed in; the Saturday sponsor call, kept; Dario's visit, kept; a screen, by arrangement, clean.",
 "This is the week the scenario most wants you to see clearly, because it is the week a review will later compress into a phrase. \u2018A three-week gap in treatment\u2019 can be written by a report writer as a falling-off or as a bridged transition, and the difference will be made entirely of paper generated inside weeks like this one \u2014 or of its absence.",
], [C("Keep the week's paper \u2014 sign-ins, visit, screen \u2014 in the folder, dated", "transport_beat66",
      note="A bridged gap is built one ordinary kept evening at a time. So is every other kind of record.")]),

N("transport_beat66", 60, "The Bus Pass Decision", [
 "Money, because this scenario insists money is always in the room: the step-down is across town, the bus pass is a real expense against a part-time wage, and the month has already produced a phone bill for an insurer's phone tree and a folder's worth of copies. Protecting the route to the step-down \u2014 the pass, bought now, good through the review and into the program's first weeks \u2014 is unglamorous in exactly the way the whole winning strategy in these scenarios is unglamorous.",
], [C("Buy the pass now and protect the route to the step-down", "notify_beat", cash=-24,
      note="The route is now a fact, not an intention. Facts are what reviews can be told."),
    C("Pay per ride and keep the cash \u2014 the route can be managed week to week", "notify_beat",
      note="It can, most weeks. Reviews are not held in most weeks; they are held in the week the managing failed.")]),

N("notify_beat", 64, "Notifying the Agency, Before the Review", [
 "The notification is the campaign's central document, and its power is entirely in its timing and its attachment: a short written notice to the agency, from you, through your lawyer, stating that the program discharged you at week ten for a benefit limit \u2014 with the discharge summary attached, if you have it \u2014 and that you are enrolled in the step-down, with its dated confirmation attached, if you have that. Sent now, it lands in the file before the review report is drafted. Sent later, it is an argument made to a room about a report already written.",
 "Ms. Nakamura's list and your lawyer's campaign agree on this point completely, which in this system is as close to certainty as advice ever gets: the review reads the file. Notify the file.",
], [C("Send the written notification now, with the summary and enrollment attached", "letter_to_file",
      setFlags=["agencyNotified"], cash=-5,
      addHidden=["Agency notified in writing before the review, discharge summary attached"],
      note="Sent, dated, attached. The review report will now be drafted from a file that contains the program's own words."),
    C("Wait and explain it at the review in person \u2014 you'll be in the room; your voice should count", "letter_to_file",
      note="It will count, in the room, for the minutes the room gives it. The report was drafted the week before, from the file as it then stood.")]),

N("letter_to_file", 68, "What the File Holds Tonight", [
 "Tonight the file holds either a campaign or a hope. In the campaign version: the summary, with its arithmetic reason; the enrollment confirmation, with its date; a notification, stamped before the review. In the hope version: a status field reading \u2018not completed,\u2019 a counselor's good opinion in a program office across town, and a father who can explain everything, in a room, briefly, after the report is read.",
 "Your lawyer's remaining steps are the audit and the repair: read the file itself, and correct its coding in writing. \u201cWe do not yet know,\u201d he says, \u201cwhether the correction needs to fix a sentence or a status. So we read.\u201d",
], [C("Move to the audit: request the record", "records_beat66",
      note="Reading, as ever in this system, is a right with a citation attached.")]),

N("records_beat66", 72, "Reading the Coding", [
 "The request is the one your lawyer named: your case record, from the agency, which under the regulation \u201cshall be released upon request\u201d (55 Pa. Code \u00a7 3130.44(d)). You sign it with the specific ask included \u2014 the goal-status history and the chronology entries for the discharge \u2014 because you are no longer asking whether the file misdescribes you. You are asking for the page and line where it does, so the correction can cite the page and line.",
], [C("Sign and send the written records request this week", "coding_seen",
      setFlags=["recordsRequested"], cash=-4,
      addHidden=["Case record requested in writing under 55 Pa. Code \u00a7 3130.44(d)"],
      note="Signed, dated, specific. The coding is about to become a document you hold, instead of a rumor you fear."),
    C("Skip the request \u2014 Ms. Nakamura already told you how it reads", "coding_seen",
      note="She told you honestly. A correction, however, has to cite the file \u2014 and citing requires the page, not the summary of the page.")]),

N("coding_seen", 77, "Goal: Not Completed, in Print", [
 "The record, when it comes, is as described and worse in the small way that matters: the chronology entry for your discharge is one line \u2014 \u2018Parent discharged from IOP\u2019 \u2014 with no reason attached, and the goal line reads, in the file's own typographic calm: Goal: Not Completed. Nothing in the entry is false. Everything in it is incomplete, which in a file is the more durable kind of wrong, because no one ever has to defend it as a statement.",
 "Below the entry, if your notification arrived in time, sits your own submission \u2014 the summary, the enrollment, the dates \u2014 filed after the coding but before the report. The file now contains both versions of your ten weeks: the field's four words, and the program's two pages. A correction is how the first version gets amended to match the second.",
], [C("Draft the written correction with your lawyer", "correction_beat66",
      addHidden=["Goal coding read in the parent's own record \u2014 'not completed,' reason absent from the chronology"],
      note="Page, line, status: identified. Corrections, like apologies, only work when they are specific.")]),

N("correction_beat66", 82, "The Written Correction", [
 "The correction is short, because the documents do the work: it asks that the chronology be amended to state the discharge's reason \u2014 benefit limit, per the program's attached summary \u2014 and that the goal be re-coded to reflect completion to the extent the benefit allowed, with the step-down enrollment, dated and confirmed, noted as the plan's continuation. It cites the summary's page, the enrollment's date, and the chronology's line. It accuses the status field of nothing; status fields have no intentions to accuse. It simply asks the file to say the whole thing.",
], [C("File the written correction with the summary and enrollment attached", "hallway_beat66",
      setFlags=["correctionFiled"], cash=-5,
      addHidden=["Written correction filed \u2014 discharge reason and goal re-coding requested, documents attached"],
      note="Filed before the review. The report writer will now meet the correction in the file, in the ordinary course of writing."),
    C("Hold the correction for the review \u2014 hand it up in the room, where it will be seen", "hallway_beat66",
      note="It will be seen, in the room, by people reading a report that was finished without it. Seen is not the same as used.")]),

N("hallway_beat66", 86, "The Week the Step-Down Opens", [
 "The three weeks end the way dated openings do: on schedule. Before the step-down's first session, the remaining pressure arrives from the ordinary direction \u2014 Dario's school sends a note about a parent event, your employer's schedule shifts a half-day, and the visit lands midweek like a small holiday inside the logistics.",
 "None of it is the case, and all of it is the case: the review will meet a father whose ten weeks became a discharge, a gap, and a new program, and the only version of that story guaranteed a hearing is the one already in the file.",
], [C("Go to Dario's visit, the day before the step-down opens", "dario_visit",
      note="He has been saving a question. Ten-year-olds save questions the way programs save documents: carefully, and for a date.")]),

N("dario_visit", 90, "Dario's Question", [
 "The visit is a good one \u2014 the puzzle, the full edition of the school week, a drawing produced from a backpack with ceremony. Near the end, in the unhurried minute while the pieces go back in the box, Dario asks it, looking at the puzzle lid and not at you, the way people ask the questions that matter most: \u201cWhen do I come home?\u201d",
 "You give him the truth at his size, the way you have learned to: grown-ups are still working out the timing; a judge helps decide; your job is the program and the visits, and you are doing your job, all of it, including the new program that starts this week. He nods with the completeness children nod with, and holds your sleeve a moment at the door, and the visit concludes on time, as the note will say.",
], [C("Write the visit up in your folder that night, dated, as always", "dario_school",
      addHidden=["Visit kept \u2014 Dario's question answered at his size; visit concluded on time"],
      note="The note will say: attended, engaged, appropriate. The folder will hold the sleeve. Both records are true.")]),

N("dario_school", 94, "The School Note", [
 "Dario's school note is a small, ordinary piece of parent work \u2014 a form about the parent event, a signature line, a date \u2014 and it requires, as such forms now do, coordination with the agency about who signs what while a child is placed. You handle it the folder way: copy made, question asked in writing, answer kept.",
 "It is not a beat in anyone's case plan. It is a father remaining a father at the level of forms, in a week when the large machinery of the case is deciding how to describe him in a status field. The scenario includes it because real cases are made of both, in the same weeks, at the same kitchen table.",
], [C("File the school form copy and go to the step-down's first session", "stepdown_start",
      note="Ordinary parent work, done in an unordinary week. Both facts belong in the folder.")]),

N("stepdown_start", 98, "The New Chair", [
 "The step-down's room is smaller, the circle is smaller, and the chair you are given is, in the way of chairs, nobody's yet. The counselor has your intake packet \u2014 stamped weeks ago, if you filed it that way \u2014 or takes your information fresh, if the enrollment waited for a phone call. Either way, you attend, you sign in, and the program's second chapter begins with the oldest sacrament in this system: a signature on a sign-in sheet, on a date, in a file.",
 "Your participation is noted. Your status, in this program's system, is the word the agency's field never held: enrolled, attending, progressing. Whether the agency's file will say those words by the review depends on paper already sent \u2014 or on a voice, briefly, in a room.",
], [C("Send the step-down's attendance confirmation to the agency and your lawyer", "money_beat66", cash=-4,
      addHidden=["Step-down program \u2014 first session attended; attendance confirmation sent"],
      note="Proof, filed while it is fresh. The gap now has a far shore, and the far shore has a date on it.")]),

N("money_beat66", 103, "Payday, Thin and Sufficient", [
 "The part-time paycheck lands, thin and sufficient, in the week before the review. The folder's arithmetic for the autumn is its own quiet argument: bus pass, copies, stamps, intake fees where they fell \u2014 a recovery administered at retail prices by a man who kept the receipts, because receipts, in this system, are a dialect of the truth.",
 "Your lawyer asks for the folder one more time before the review. \u201cWhatever the report says,\u201d he says, \u201cwe answer from this. If the report says what the file now says, the folder rests. If it says the four words, the folder testifies.\u201d",
], [C("Bring the folder to the final preparation", "review_notice66",
      note="The notice has already arrived. It is on the refrigerator, under the program's magnet, where the calendar used to be.")]),

N("review_notice66", 108, "The Review Notice", [
 "The review notice names the date and the room. Reviews in this system are stock-takings: the report is drafted from the file, the room hears summaries and brief answers, and the stock taken is, in large part, the file's own description of you \u2014 \u2018engaged and progressing,\u2019 from month two, against \u2018goal: not completed,\u2019 from week ten, unless the file between those phrases has been repaired.",
 "Your lawyer lays the preparation out as a description, not a prediction: \u201cThe report writer is drafting this week. What she finds in the file is what the review will be. We have spent a month deciding what she finds. The rest is her pen and the judge's morning, which were never ours.\u201d",
], [C("Go to the final preparation with your lawyer", "counsel_prep66",
      note="One folder, one file, one report being drafted across town. The campaign is finished; the audit is next.")]),

N("counsel_prep66", 113, "Final Preparation", [
 "Preparation is an audit, conducted at a conference table with the folder open: the summary, if it exists \u2014 obtained on the last day, in writing, with the reason stated. The enrollment, if it exists \u2014 dated, stamped, confirmed. The notification, if it was sent \u2014 before the review, with attachments. The record request, if it was made \u2014 and the correction, if it was filed, with its page and line citations.",
 "Each document either is or is not in the agency's file tonight. There is no third state, and no preparation can create one. \u201cWhatever is in there,\u201d your lawyer says, \u201cis what we argue from. What isn't, we explain \u2014 and explaining, in a review, is the tax you pay for paper not filed.\u201d",
], [C("Check the folder's last page, and sleep", "review_prep_docs",
      note="Tomorrow the report gets read aloud. Tonight, the file is what it is, and so are you.")]),

N("review_prep_docs", 118, "What the Report Will Say", [
 "The night before the review, the honest inventory: a ten-week program, attended completely, ended by arithmetic. A three-week gap, bridged with meetings and paper or waited out on a promise. A new program, begun. A goal line in a file across town, coded in four words, corrected in writing or still standing. A son who asked a question at a puzzle table and got the truth at his size.",
 "None of that is the review's business in narrative form. The review's business is the report. The report's business is the file. The file's business \u2014 this whole scenario's business \u2014 is what was put in it, in writing, before the drafting.",
], [C("Go to the review", "review66",
      note="The room, the report, the four words or their correction. Everything now depends on which documents the file held when the report was written.")]),

N("review66", 123, "The Review", [
 "The review is orderly and brief in the way of rooms with many cases. The report is read in summary. The question the report must answer is narrow and enormous: what is the status of the plan's central goal \u2014 complete IOP \u2014 for a father who completed ten of its twelve weeks before a benefits office ended the count?",
 "The answer is in the file, in one of three forms. In the first, the file holds the program's own summary, the agency's advance notification, the dated step-down enrollment, and a filed correction \u2014 and the report, drafted from that file, describes a goal re-coded and a plan continuing. In the second, the truth exists but arrived as explanation, after the report's coding had already done its work in the room. In the third, the file holds four words, a handshake's memory, and a counselor's good opinion in a building across town \u2014 and the report reads the four words, because the four words are what a report can read.",
], [C("The report is read from the repaired file \u2014 summary, notification, enrollment, correction, all in before the drafting", "end_summary",
      requiresFlags=["dischargeSummary", "agencyNotified", "stepdownEnrolled"],
      note="The file answered the question before the room had to."),
    C("The truth is in the room, carried by voice and late paper, after the report relied on the code", "end_gap",
      requiresFlags=["dischargeSummary", "correctionFiled"], requiresNoFlags=["agencyNotified"],
      note="Everything you say is true. The report was written last week."),
    C("The truth is in the room, in the father's own account, against the file's four words", "end_notcompleted",
      requiresNoFlags=["dischargeSummary"],
      note="A counselor's good opinion does not photocopy. The review is about to demonstrate it."),
    C("The report stands on the coding \u2014 the explanation exists, but no document carries it", "end_notcompleted",
      requiresNoFlags=["agencyNotified", "correctionFiled"],
      note="Four words, unopposed by paper, in a room that runs on paper.")]),

N("end_summary", 129, "Ending \u2014 The Summary Says Progress", [
 "The report, when its turn comes, does not read the four words. It reads the goal as the correction re-coded it: IOP completed to the extent the benefit allowed \u2014 ten weeks, full attendance, progress documented by the program's own summary \u2014 with step-down treatment underway as the plan's continuation. The judge notes the enrollment's date, the notification's date, and the summary's reason, in the tone of a person reading a file that agrees with itself.",
 "\u201cThe record should say what happened,\u201d the judge says, in passing, in the direction of no one in particular. \u201cIn this file, it does.\u201d Dario is still placed at this scenario's curtain. The plan continues, the step-down continues, and the review closes on a file that describes the father Dario visited on Wednesday \u2014 which is all, and exactly, what the paperwork campaign was for.",
], ending=True, debrief=[
 "WHAT THE RECORD HELD (the hidden record, revealed): A complete paper chain, each link dated before the review: the discharge summary, obtained in writing on the program's last day, stating progress, attendance, and the reason \u2014 benefit limit; a written notification to the agency, with the summary attached, sent before the review report was drafted; a step-down enrollment completed by intake packet, with a dated confirmation for the opening three weeks out; the parent's own record, requested and read (55 Pa. Code \u00a7 3130.44(d)), so the miscoding was seen on its page and line; and a written correction, filed with documents attached, re-coding the goal on the record. The four words were amended before they could testify.",
 "THE LAW UNDER THIS PATH: No exotic law was used, and the scenario says so plainly. Counsel's role (42 Pa.C.S. \u00a7 6337) was sequencing and filing; the record request (55 Pa. Code \u00a7 3130.44(d)) was the audit; the rest was timing \u2014 reviews are argued from reports, reports are drafted from files, and a correction that arrives before the drafting is a fact, while one that arrives in the room is an argument. Nothing in this ending decided Dario's placement or tested any burden of proof; the review continued the plan on a corrected record, honestly labeled PARTIAL: Dario is still placed, and the case continues.",
 "THE HONEST PART: This ending is not a verdict on Hector's worth, and it was not produced by virtue alone. A counselor willing to print the summary without being asked twice, a worker who explained the coding honestly, a step-down with an opening in three weeks rather than three months \u2014 people and luck hold their pieces of it, as they do in every ending here. A different report writer could have clung to the status field even against the correction. What Hector controlled was the chain itself: paper obtained at the door, notice given before the drafting, enrollment proven instead of promised. In a system that reads files, the father who papers his own arithmetic is the only author his progress reliably gets.",
]),
N("end_gap", 127, "Ending \u2014 A Gap, Explained Late", [
 "The review hears the truth \u2014 all of it, from the father, with the summary produced and the correction handed up \u2014 and the truth is believed, in the personal way voices are believed in rooms that run on drafted reports. The report, however, was drafted the week before, from a file whose goal line read \u2018not completed,\u2019 and the review's own record now contains both: the coded report, and a father's correction, arriving after the coding had already framed the morning.",
 "The judge directs that the correction be filed and the record amended going forward \u2014 it will govern the next report, and every summary after it. Going forward is the operative phrase, the same one that governs every late truth in this system: repaired, permanently, and one review too late to have framed this one.",
], ending=True, debrief=[
 "WHAT THE RECORD HELD (the hidden record, revealed): The truth, in documents \u2014 eventually. The discharge summary existed and said what it said; a written correction was filed; the step-down was real. What the campaign lacked was the ordering: the agency was not notified in writing before the review report was drafted, so the report was written from the status field, and the correction, however complete, was received as an answer to a report instead of as part of the file the report was written from. The gap in treatment was three weeks. The gap in paperwork was longer, and it is the second gap this ending is named for.",
 "THE LAW UNDER THIS PATH: The verified tools were the same as in every path \u2014 counsel (42 Pa.C.S. \u00a7 6337), the parent's own record on request (55 Pa. Code \u00a7 3130.44(d)) \u2014 exercised here as repair rather than prevention. No placement was decided and no burden was tested in this review; the plan continues, the step-down continues, and the amended record will govern future reports, which in a long case is a real and material thing. PARTIAL, honestly labeled in the other direction: the file is right now, and was wrong when the report that framed this review was drafted from it.",
 "THE HONEST PART: Late truth governs the future, and the future is most of a case \u2014 this ending refuses both despair and flattery. A report writer who called the program herself, a worker who attached the summary on receipt, a review postponed a fortnight: any of them lands this correction on the right side of the drafting without Hector changing a thing, and a colder room could have received the same late paper and discounted it entirely. Workers, report writers, and calendars hold their pieces here. Hector's piece was the ordering \u2014 and ordering, in a file-driven system, is not a clerical detail. It is the difference between a fact and a rebuttal.",
]),
N("end_notcompleted", 125, "Ending \u2014 Goal: Not Completed", [
 "The report reads the goal line the way reports read goal lines, without inflection: \u201cGoal: not completed.\u201d The father's explanation follows \u2014 accurate, complete, and carried entirely by his voice and a counselor's remembered kindness \u2014 and is noted in the review's record the way explanations are noted when no document carries them: heard, summarized in a clause, and filed beneath the coding, which remains the file's operative sentence about his ten weeks.",
 "Outside, his lawyer says the sentence this scenario has been walking toward since the insurer's letter: \u201cFour words just outlived a ten-week effort, because the effort's own document never entered the file. The counselor's summary still exists, Hector. Programs keep their paper. What can still be requested, filed, and corrected is most of it \u2014 for the next report. Next reports are where cases like yours are actually decided.\u201d",
], ending=True, debrief=[
 "WHAT THE RECORD HELD (the hidden record, revealed): A status field and nothing beneath it: a discharge with no reason in the chronology, a goal coded \u2018not completed,\u2019 a step-down waited on rather than enrolled in with proof, a notification never sent in writing before the drafting, a record never requested, a correction never filed. The ten weeks happened \u2014 attendance, progress, clean screens, a counselor's genuine good opinion \u2014 and almost none of it existed in the only medium the review could read. What the file cannot say, the report cannot summarize; what the report cannot summarize, the review cannot weigh.",
 "THE LAW UNDER THIS PATH: The tools remain exactly where they were in week ten, because none of them expire at a review: counsel (42 Pa.C.S. \u00a7 6337) can still sequence the repair; the parent's record \u2018shall be released upon request\u2019 (55 Pa. Code \u00a7 3130.44(d)), so the coding can still be read on its page and corrected in writing; the program's summary can still be obtained and filed. No placement was decided at this review and no burden of proof was tested; the plan continues under a coded failure that the documents, if filed now, can still amend for every future reader. That amendability is this ending's honest floor: the four words won this report, not the case.",
 "THE HONEST PART: This debrief does not call the outcome a judgment on the father, because it is not one: it is a judgment about a medium. A worker who requested the summary herself, a counselor who mailed it unasked, a coding field with a line for \u2018reason\u2019 \u2014 any of them prevents this ending without the father changing a single evening of his ten weeks. Systems, workers, and luck are all over this outcome. The father's share was narrower and heavier: he left the program with a handshake, in a case that runs on paper, and a handshake \u2014 however warm, however earned \u2014 is the one document the file cannot hold.",
]),
]
assert len(s66_nodes) == 36, len(s66_nodes)
# S66 reaches 40 nodes in the assembly section below, after inserted beats.
assert sum(1 for n in s66_nodes if n.get("ending")) == 3

# =====================================================================
# ASSEMBLY — inserted beats, builds, emission
# =====================================================================
def insert_chain(nodes, after_id, extras, target_id):
    """Insert `extras` (a chain of nodes) between node `after_id` and the
    node its choices currently send to `target_id`. The after-node's edges
    to target_id are redirected to the first extra; the extras' own choices
    already point along the chain and finally to target_id."""
    idx = next(i for i, n in enumerate(nodes) if n["id"] == after_id)
    after = nodes[idx]
    hit = False
    for c in after["choices"]:
        if c["next"] == target_id:
            c["next"] = extras[0]["id"]
            hit = True
    assert hit, (after_id, target_id)
    for j, e in enumerate(extras):
        nodes.insert(idx + 1 + j, e)

# ---- S64 inserted beats (+8 -> 42) ----
insert_chain(s64_nodes, "start", [
N("folder_inventory", 2, "The Folder, Inventoried", [
 "Before the appointment, the folder gets its autumn inventory on the kitchen table: the disposition order with its three services underlined in a hand less steady than your current one; the program certificate; visit notes in a rising stack; screen results, filed by date, because you file everything by date now.",
 "What the inventory shows, laid out, is a record with a shape: your side of it is thick and current. The other side \u2014 what was provided, when, and what happened in between \u2014 is present mostly as references to documents you have never held. An inventory cannot fix that. It can, and does, tell you exactly what to ask a lawyer about.",
], [C("Take the inventoried folder to Mr. Sandoval's office", "counsel_meet",
      note="A folder with a known shape. The appointment is about to give the shape a date.")]),
], "counsel_meet")

insert_chain(s64_nodes, "chronology_gaps", [
N("binder_begins", 22, "A Thin Binder, Labeled in Pencil", [
 "Mr. Sandoval opens a new binder \u2014 thin, at first, as binders for unbuilt arguments are \u2014 and labels it in pencil with the February date. Three tabs go in: PROGRAM, THERAPY, HOUSING. \u201cEvery document we find goes behind its tab,\u201d he says. \u201cEvery document we don't find gets a page too \u2014 a page that says what we asked for, when, and what we were told. An honest binder shows its gaps. Dishonest ones are just scrapbooks.\u201d",
 "It is a small ceremony, and you understand it completely: from today, the autumn has a container, and containers, in this system, are what arguments are carried in.",
], [C("Begin with tab one \u2014 the program", "prog_beat",
      note="Tab one is empty. The program's office, and its printing habits, are next.")]),
], "prog_beat")

insert_chain(s64_nodes, "prog_letter", [
N("bus_home64", 34, "The Bus Home, Thinking in Dates", [
 "The bus home crosses the river in the late light, and you do the arithmetic the case has taught you: eight weeks of waitlist in a case that will be fifteen months old in February is not a footnote. It is more than a tenth of Amara's placement, spent at a door that had not opened, through no decision of yours that any document records.",
 "Arithmetic like that is either a grievance or an exhibit, depending on whether it is written down with its documents attached. You write it down on the bus, on the back of the reprint envelope or on a scrap you will copy out tonight, because that is what you do now.",
], [C("Copy the note into the folder at home, dated", "therapy_beat",
      note="Tab one's story, in your hand, with its letter behind it or its absence noted beside it.")]),
], "therapy_beat")

insert_chain(s64_nodes, "housing_docs", [
N("sandoval_call", 58, "The Call About Tab Three", [
 "Mr. Sandoval calls in the evening, between your shift and Amara's bedtime story hour at the foster home, which you know by heart and are not part of, and which you do not let yourself picture for long. His question is narrow: \u201cIf a stranger read tab three cold, could she tell the difference between a mother who applied late and a list that moves slowly?\u201d",
 "The answer, after the autumn's assembling, is yes \u2014 the stamps say it. \u201cGood,\u201d he says. \u201cThen tab three's job is done. It doesn't make the exception. It protects the exception from being answered with your name.\u201d",
], [C("Ask what the three tabs become, together", "gaplog_beat",
      note="\u201cA single document, in your voice, with dates,\u201d he says. \u201cYour log.\u201d")]),
], "gaplog_beat")

insert_chain(s64_nodes, "screens_beat", [
N("work_beat64", 71, "The Shift Supervisor's Signature", [
 "Parallel pressure, because this scenario believes a case is never the only thing happening: your employer rotates the Saturday shift, and the visit \u2014 the visit, of all things \u2014 hangs for one afternoon on a supervisor's willingness to swap two names on a schedule. She swaps them, and signs the schedule, and you keep a copy, because a signed schedule is the difference between a visit kept by luck and a visit kept by arrangement.",
 "Ms. Yoder notes the kept visit in her report without mentioning the schedule. Reports rarely do. The folder remembers what reports omit; that, increasingly, is the folder's whole job description.",
], [C("File the signed schedule with the visit note", "review12_notice",
      addHidden=["Saturday visit protected by signed work-schedule swap; copy kept"],
      note="Kept visits are your half of the February argument. This one is kept on paper twice over.")]),
], "review12_notice")

insert_chain(s64_nodes, "amara_visit", [
N("folder_night64", 93, "The Folder, the Night Before the Letter", [
 "The night before the agency's letter arrives \u2014 though you do not know it is the night before \u2014 the folder gets its monthly straightening: new pages behind their tabs, dates checked, the binder's pencil label darkened in ink, because February no longer feels hypothetical.",
 "Straightening a folder is not hope, exactly. It is the form hope takes in a case run on paper: the belief, enacted with a hole punch, that being read carefully is possible, and that it is worth being ready to be read.",
], [C("Put the folder by the door, and sleep", "agency_letter",
      note="The mail arrives in the morning. Envelopes from agencies have a weight you can identify before you open them.")]),
], "agency_letter")

insert_chain(s64_nodes, "month13_work", [
N("foster_call", 126, "A Call from the Foster Home", [
 "Amara's foster mother calls about a practical matter \u2014 a school form, a signature, the ordinary plumbing of a placed child's week \u2014 and handles it with the practiced kindness of a woman who has learned which parts of a case are hers to carry. The form gets signed. The week gets plumbed.",
 "\u201cShe asked the reading corner question again,\u201d she says, at the end, not unkindly. \u201cI told her what you told her. Timing, and grown-ups working.\u201d Two households, one sentence, agreed across a case file: some coordination in this system happens entirely without forms, and works.",
], [C("Note the call and the form in the folder, dated", "review14_notice",
      note="Even the un-formal parts get a dated line now. The habit no longer feels like a habit; it feels like the case's other language.")]),
], "review14_notice")

insert_chain(s64_nodes, "filing_eve", [
N("morning_of", 154, "Two Days Out", [
 "Two days before the date, the case performs its smallest and truest scene: a visit, kept, with a book discussed as promised \u2014 Amara's review of it is thorough and not entirely favorable to the author \u2014 and a goodbye conducted with the practiced choreography of month fifteen, which neither of you invented and both of you perform.",
 "Nothing about the visit will appear in any filing document. It is included here because it is the thing the filing documents are about, and because a scenario that forgot that would be teaching the wrong subject.",
], [C("Go home, and let the date come", "filing_day",
      note="The binder is filed or unfiled. The record is written. The date, as ever, does not negotiate.")]),
], "filing_day")

assert len(s64_nodes) == 42, len(s64_nodes)
s64 = build({"title": "The First 90 Days",
             "subtitle": "Scenario 64 \u2014 Fifteen Months of Paper (a fictional composite)",
             "startDateISO": "2026-08-31", "startNode": "start", "startCash": 170,
             "tier": "Complex",
             "summary": "Month 10 of Amara's placement: the 15-month filing date is February 3, 2027 \u2014 and the services exception exists only as far as the file documents it."},
            s64_nodes, S64_START)
_fd = [n for n in s64["nodes"] if n["id"] == "filing_day"][0]
assert _fd["dayOffset"] == 156 and _fd["kicker"] == "Day 156 \u2014 Wednesday, February 3, 2027", _fd

# ---- S65 inserted beats (+14 -> 38) ----
insert_chain(s65_nodes, "start", [
N("separate_counsel", 1, "Two Lawyers, Explained at the Table", [
 "A practical clarification, delivered by Curtis's lawyer over speakerphone that first evening: you are two parties. Each of you has the right to counsel of your own (42 Pa.C.S. \u00a7 6337), each plan is separately your own to satisfy, and neither of you can sign, waive, or explain away anything on the other's behalf. The case will treat you separately even when life doesn't.",
 "\u201cWhich means,\u201d she says, \u201cthat the most helpful thing you can do for each other is keep your own paper perfect \u2014 and compare it, often, at that table.\u201d The table, the binders, and the car: the case's real infrastructure, named at last.",
], [C("Start with the paper, tonight", "two_binders",
      note="Two parties, two plans, one table. The table is about to become a records office.")]),
], "two_binders")

insert_chain(s65_nodes, "two_binders", [
N("paper_habits", 4, "House Rules for Paper", [
 "The house rules get written on an index card and taped inside the cupboard door, in Trina's hand: each parent files their own paper the day it arrives; nothing goes in the other binder, even temporarily; anything that mentions both names gets copied, once, into both.",
 "Rules like these look like tidiness. They are, in fact, the load-bearing wall of everything that follows \u2014 because a file bleed cannot be corrected by people who cannot tell, from their own folders, what their own record ought to say.",
], [C("Lay the two plans out as one calendar", "calendar_beat",
      note="The card goes up. The calendar comes out. The collisions are about to introduce themselves.")]),
], "calendar_beat")

insert_chain(s65_nodes, "deconflict_beat", [
N("reply_week", 11, "The Workers Reply \u2014 or Don't", [
 "Replies to letters like yours arrive on the system's schedule, which is to say unevenly: one worker answers within the week, practically, with a held alternate slot and a note that she has flagged the Friday problem to the provider; the other file gets a copy placed in it, with action pending a supervisor's calendar.",
 "Or, on the autumn where no letters went out, this week is simply a week: shifts worked, appointments kept by minutes, nothing in either file about the collisions gathering above both plans like weather neither worker has been asked to forecast.",
], [C("File whatever replies exist, in both folders, and note the silences too", "car_beat",
      note="A pending answer is still a record. It proves the question was asked before the answer was needed.")]),
], "car_beat")

insert_chain(s65_nodes, "car_beat", [
N("bus_plan", 15, "The Bus Plan, Written Down", [
 "There is a bus plan now, written on the back of the calendar \u2014 routes, transfer times, the honest total in minutes \u2014 because a household with one car and two plans needs its contingencies in writing, not in optimism. The bus plan is slower than the car by forty minutes in every direction. It is also, unlike optimism, available on Fridays.",
 "Curtis reads it twice. \u201cIt's a bad plan,\u201d he says. \u201cIt's a plan,\u201d you say, \u201cfor the day the car isn't.\u201d Both assessments go on the calendar, because both are true and the day is coming.",
], [C("Keep the week, and keep the log", "screens_beat",
      note="Contingencies written down are the difference between a system and a hope.")]),
], "screens_beat")

insert_chain(s65_nodes, "screens_beat", [
N("program_night", 19, "His Tuesday Group", [
 "Curtis's Tuesday group meets in a room with a whiteboard and a sign-in sheet, and he describes it the way you describe your program: ordinary, demanding, and \u2014 on the weeks it goes well \u2014 the place where his plan's progress is actually made, one signature at a time.",
 "He is good at it, he admits at the table, in the tone of a man reporting weather in another county. His attendance is perfect. His file, at this moment, is the cleanest version of him that exists anywhere. The scenario asks you to hold that fact, because his file is about to acquire a line his conduct never wrote, from the same week yours does.",
], [C("Note his attendance in the week's log, and wait for the hard week", "his_miss_setup",
      note="Perfect attendance, logged. The hard week is already on the calendar, gathering mechanics and shift changes.")]),
], "his_miss_setup")

insert_chain(s65_nodes, "his_miss", [
N("reschedule_kept", 26, "The Reschedule, Kept", [
 "The rescheduled screen happens the following week, and Curtis keeps it, and the result is clean, and the provider's note says exactly that, in the flat dialect of providers. In the life: a miss, a reason, a remedy, a clean result \u2014 a closed loop, seven days wide.",
 "Closed loops, however, close only where they are recorded. The reschedule lives in the provider's records and in Curtis's account at the kitchen table. Whether it lives in his file \u2014 attached to the miss, completing the loop \u2014 is a question about copying, and copying is this scenario's whole weather system.",
], [C("File the reschedule result in his folder, next to the dated note of the miss", "her_report",
      note="The loop, closed in his folder. Your report, meanwhile, is already in the mail.")]),
], "her_report")

insert_chain(s65_nodes, "visit_makeup", [
N("makeup_outcome", 34, "What Tuesday Wrote", [
 "Tuesday writes its line either way. In the de-conflicted version, the make-up visit happens in the held alternate slot, both obligations survive, and the visit note is a warm paragraph about a puzzle and a parent who arrived on time. In the collision version, one plan absorbs the evening and the other absorbs the absence, and two files each acquire a sentence whose explanation exists only at a kitchen table, in a conversation nobody filed.",
 "You compare folders afterward, as has become the custom. The custom, by now, is doing quiet structural work: no line in either file will go unexamined by its owner for long.",
], [C("Turn to the files themselves \u2014 both of them, completely", "records_beat65",
      note="Reports have shown you summaries. Summaries have shown you bleed. The files are next.")]),
], "records_beat65")

insert_chain(s65_nodes, "file_arrives65", [
N("kitchen_audit", 45, "The Kitchen-Table Audit", [
 "The audit takes one evening and two highlighters, and its method is a child's method: every line in each file must answer the question whose line are you? Most answer easily. A handful hesitate \u2014 a summary phrase here, a \u2018household\u2019 there \u2014 and the hesitations, marked, become the correction's working list.",
 "\u201cIt's not even that much,\u201d Curtis says, looking at the marked pages. \u201cFour lines. Five.\u201d \u201cFour lines is a review,\u201d you say. \u201cFour lines is exactly a review.\u201d",
], [C("Take the marked lines one at a time, starting with the visit note", "her_note_his_file",
      note="The smallest line first. Small lines are where patterns hide.")]),
], "her_note_his_file")

insert_chain(s65_nodes, "her_note_his_file", [
N("two_desks", 50, "Two Desks, Visited in Person", [
 "Before the correction is drafted, you each visit your own worker's office \u2014 separately, by appointment, with your folder \u2014 and say the same sentence in two rooms: my file contains a line that belongs to the other parent's record, and I would like the correction to be a document, not a conversation. Both workers, to their credit, receive the sentence the same way: professionally, with a note taken and no defensiveness worth recording.",
 "\u201cBetween desks is where it happened,\u201d Ms. Whelan says. \u201cSo between desks is where we'll fix it. Put it in writing and I'll attach it in both.\u201d It is the system's own diagnosis, offered from inside it: the fix travels the same route the error did, or it doesn't travel at all.",
], [C("Draft the correction as one document, for both desks", "correction_beat",
      note="One document, two addressees. The error was shared; the repair will be too.")]),
], "correction_beat")

insert_chain(s65_nodes, "correction_beat", [
N("ack_beat", 55, "The Acknowledgments", [
 "Acknowledgments arrive the way corrections do, unevenly and on paper: one worker confirms the correction is filed and the report amended; the other confirms receipt and undertakes to attach it to the next summary. Filed acknowledgments, or their dated absence, go into both folders.",
 "This is the least cinematic beat in the scenario and, the lawyers will later say, one of the most important: a correction with an acknowledgment is a closed loop. A correction without one is a letter a parent believes in. Reviews run on loops, not beliefs.",
], [C("Go into the joint-visit week with the correction's status known", "joint_visit",
      note="Known, dated, filed. Whatever the reviews do, they will do it to a record whose state is not a mystery to its owners.")]),
], "joint_visit")

insert_chain(s65_nodes, "joint_visit", [
N("note_followup", 60, "One Sentence, Requested Twice", [
 "The request that the joint visit be noted in both files gets its answer in the ordinary two parts: yes, in the file that already held it, the note is confirmed; and in the other file, a short entry is added, dated to the visit and cross-referenced. Two lines, and the visit now exists everywhere it happened \u2014 which is to say, everywhere it will ever be read as having happened.",
 "\u201cWe're getting good at this,\u201d Curtis says. \u201cWe're getting documented at this,\u201d you say, \u201cwhich in this building is the same accomplishment.\u201d",
], [C("Turn to the capstone: the letter through counsel", "joint_letter_beat",
      note="The lawyers have been reading the folders. They have a proposal shaped like the autumn.")]),
], "joint_letter_beat")

insert_chain(s65_nodes, "work_beat65", [
N("money_beat65", 70, "Payday Arithmetic, Twice", [
 "Two paychecks, two plans, one car payment, and the month's ordinary arithmetic get done at the table in the manner of a treaty negotiation: fuel allocated like a budget line, the tire replaced before it can star in another Friday, copies and stamps itemized without irony in a household ledger.",
 "It is not a beat any plan ordered. It is, the folder would say, the substrate every plan silently assumes \u2014 and the reason \u2018just manage it\u2019 was never a scheduling strategy, only a hope with a fuel gauge.",
], [C("Confirm the month's arrangements in the ledger, and go to Hattie's visit", "hattie_beat",
      note="Arithmetic done is its own kind of compliance. Hattie, meanwhile, has a lighthouse puzzle reaching its decisive phase.")]),
], "hattie_beat")

insert_chain(s65_nodes, "prep_split", [
N("counsel_prep_her", 79, "Her Counsel, Her Folder", [
 "Trina's counsel preparation is a folder audit with a lawyer's questions: Is your compliance described anywhere by someone else's conduct? Is every date in this folder yours? The correction, the acknowledgments, the de-conflicted slots \u2014 each is checked against the file copy, because the review will be argued from the agency's paper, and the point of the autumn was to make the agency's paper match yours.",
 "She closes the folder. \u201cWhatever happens in the room,\u201d she says, \u201cyou will not be meeting your own record for the first time. Parents who meet their record in the room are the ones reviews happen to.\u201d",
], [C("Go home to the second preparation, across the same table", "counsel_prep_his",
      note="His folder is already open. His lawyer is already on the phone.")]),
N("counsel_prep_his", 80, "His Counsel, His Folder", [
 "Curtis's preparation mirrors hers with the symmetry this scenario has been building toward: his miss, his reschedule, his clean result \u2014 in his file, in his name, with his folder able to prove every step. The borrowed visit note is checked for its absence the way her report was checked for the stray paragraph: corrections, like errors, are verified or they are rumored.",
 "\u201cTwo folders,\u201d his lawyer says, on speaker, to the whole kitchen. \u201cTwo records. Whatever the week brings, it will at least be about the right people.\u201d",
], [C("Go into the review week", "reviews_week",
      note="Two reviews, one week, and \u2014 for the first time in the case \u2014 two files that match their owners.")]),
], "reviews_week")

assert len(s65_nodes) == 38, len(s65_nodes)
s65 = build({"title": "The First 90 Days",
             "subtitle": "Scenario 65 \u2014 Two Plans (a fictional composite)",
             "startDateISO": "2026-09-21", "startNode": "start", "startCash": 190,
             "tier": "Complex",
             "summary": "Two separated parents, two case plans, two workers, one car \u2014 and two files that keep bleeding into each other."},
            s65_nodes, S65_START)

# ---- S66 inserted beats (+4 -> 40) ----
insert_chain(s66_nodes, "visit_beat66a", [
N("employer_beat66", 15, "The Employer, Notified in Writing", [
 "A small beat with a long shadow: your part-time employer adjusts the schedule board for the coming month, and your program evenings survive the adjustment because \u2014 months ago, in a different season of this case \u2014 you put the program's hours in writing to the scheduler and kept her reply. The schedule comes out around your evenings the way water goes around a stone it has learned.",
 "You note the new schedule in the folder. Systems accommodate what they can read; the folder's copies are how your life gets read by people who were never in the room.",
], [C("Go to Monday's session, and the letter", "benefit_letter",
      note="The program's rhythm holds, this week, on the strength of an old letter. Hold that thought; the scenario will.")]),
], "benefit_letter")

insert_chain(s66_nodes, "call_insurer", [
N("appeal_info", 25, "The Appeal, Filed Without Illusion", [
 "The insurer's appeal goes in anyway \u2014 a one-page form, your counselor's supporting note, the reference number from the phone call \u2014 because a remedy unfiled is a rumor, and because its paperwork, win or lose, is one more dated document proving the cap was a cap: set by a benefit, verified by phone, appealed through channels.",
 "It will be decided in its own season, probably after the review, possibly after the step-down ends. You file it the way you now file everything: completely, dated, and without confusing the filing with the outcome.",
], [C("Go into the last week of the program", "summary_choice",
      cash=-3,
      note="Three dollars of copies. The arithmetic now has a paper trail in three buildings.")]),
], "summary_choice")

insert_chain(s66_nodes, "gap_week", [
N("gap_support", 59, "The Gap, Week Two", [
 "Week two of the gap, and the shape of it is now clear: this is not an interruption in a recovery; it is a recovery, conducted without a program's rooms for three weeks, on the strength of meetings, a sponsor, a son's Wednesdays, and paperwork. Your sponsor, reviewing the ledger on Saturday, delivers his verdict in his dialect: \u201cYou're not between programs. You're in the part of the program nobody schedules.\u201d",
 "You write that down too, on the calendar, though it will never be filed anywhere. Some records are for the file. Some are for the man the file is about.",
], [C("Finish the gap's second week, and turn to the agency", "transport_beat66",
      note="One week of gap remains. The notification decision \u2014 the campaign's center \u2014 is next.")]),
], "transport_beat66")

insert_chain(s66_nodes, "review_prep_docs", [
N("eve_beat66", 121, "The Eve of the Review", [
 "The evening before the review runs on the house's new rails: folder straightened, morning's clothes laid out, Dario's drawing from the last visit on the refrigerator under the program magnet that outlived the program. Your sponsor calls, briefly, in his ledger dialect: \u201cWhatever they read tomorrow, you know what you did. The paper either says it or the next paper will.\u201d",
 "\u201cThat's the whole sermon now,\u201d you tell him. \u201cIt got shorter.\u201d \u201cSermons do,\u201d he says, \u201cwhen they're true.\u201d",
], [C("Sleep, and go to the review in the morning", "review66",
      note="The room will read the file. The file is finished being written \u2014 by everyone, including you.")]),
], "review66")

assert len(s66_nodes) == 40, len(s66_nodes)
s66 = build({"title": "The First 90 Days",
             "subtitle": "Scenario 66 \u2014 The Discharge Summary (a fictional composite)",
             "startDateISO": "2026-10-05", "startNode": "start", "startCash": 160,
             "tier": "Complex",
             "summary": "Week 10 of 12 in IOP, Hector is discharged by arithmetic \u2014 a benefit cap \u2014 and the agency's system codes it 'goal not completed.'"},
            s66_nodes, S66_START)

if __name__ == "__main__":
    emit(s64, 64, "Fifteen Months of Paper",
         "This scenario depicts a mother in month 10 of her daughter's foster-care placement, building the written record of services that were ordered but not provided, ahead of the federal 15-of-22-months filing date. It is told through letters, chronologies, and reviews. There is no graphic content. Players may skip any scene or use the quick exit at any time.",
         S64_START)
    emit(s65, 65, "Two Plans",
         "This scenario depicts two separated parents, each working their own case plan for their daughter in foster care, whose files and schedules keep colliding. It is told through calendars, letters, and review reports. There is no graphic content. Players may skip any scene or use the quick exit at any time.",
         S65_START)
    emit(s66, 66, "The Discharge Summary",
         "This scenario depicts a father in an intensive outpatient program who is discharged at week 10 of 12 because his benefit's session cap is reached, and whose agency goal is coded 'not completed.' It is told through discharge paperwork, notifications, and a review. There is no graphic content. Players may skip any scene or use the quick exit at any time.",
         S66_START)
    for num, scen in ((64, s64), (65, s65), (66, s66)):
        ends = [n for n in scen["nodes"] if n.get("ending")]
        print(f"scenario-{num}: emitted nodes={len(scen['nodes'])} endings={len(ends)} "
              f"titles={[e['title'] for e in ends]}")
    print("GENERATION COMPLETE")
