#!/usr/bin/env python3
"""Generator for Scenarios 57-59 of 'The First 90 Days' (Foundation tier).
One data source emits both the .json and the -script.md for each scenario,
so they match node-for-node by construction. Every kicker and every
in-body date is computed from startDateISO + dayOffset via datestr();
no date is hand-typed in the scenario data. The script also walks each
winning route programmatically and prints the walked path, the number
of nodes visited, and the end cash, for use in the strategy guides."""
import json, os
from datetime import date, timedelta

OUT = os.path.dirname(os.path.abspath(__file__))

def datestr(start, off):
    d = start + timedelta(days=off)
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
        n_full = {"id": n["id"],
                  "kicker": f"Day {n['dayOffset']} \u2014 {datestr(start, n['dayOffset'])}",
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
             "choice \u2014 the player does not see it when it happens. `REQUIRES FLAG: name` means the choice "
             "is only available if that flag was set earlier; `REQUIRES NO FLAG: name` means it is only "
             "available if that flag was never set. `NOTE:` is text shown to the player right after choosing.")
    L.append("")
    L.append(f"Start date: {datestr(start, 0)}. Day offsets are days since the scenario's start date. Tier: Foundation.")
    for n in scen["nodes"]:
        L.append("")
        L.append(f"## [{n['id']}] {n['title']}")
        L.append(f"*{n['kicker']} \u2014 {datestr(start, n['dayOffset'])} (dayOffset {n['dayOffset']})*")
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
                    ann.extend("REQUIRES FLAG: " + r for r in c["requiresFlags"])
                if c.get("requiresNoFlags"):
                    ann.extend("REQUIRES NO FLAG: " + r for r in c["requiresNoFlags"])
                suffix = f"  _({'; '.join(ann)})_" if ann else ""
                L.append(f"- {c['text']} \u2192 **{c['next']}**{suffix}")
                if c.get("note"):
                    L.append(f"  - NOTE (shown after choosing): {c['note']}")
    path_m = os.path.join(OUT, f"scenario-{num}-script.md")
    with open(path_m, "w") as f:
        f.write("\n".join(L) + "\n")
    return path_j, path_m

def walk(scen, win_choices, win_ending):
    """Follow win_choices (node id -> exact choice text) from the start.
    Asserts every flag gate is satisfied by flags set earlier on the walk
    and that cash never goes negative. Returns (path, end_cash)."""
    by = {n["id"]: n for n in scen["nodes"]}
    flags, cash = set(), scen["meta"]["startCash"]
    path, cur = [], scen["meta"]["startNode"]
    while True:
        path.append(cur)
        node = by[cur]
        if node.get("ending"):
            assert cur == win_ending, (cur, win_ending)
            return path, cash
        text = win_choices[cur]
        choice = next(c for c in node["choices"] if c["text"] == text)
        for r in choice.get("requiresFlags", []):
            assert r in flags, (cur, "missing required flag", r, sorted(flags))
        for r in choice.get("requiresNoFlags", []):
            assert r not in flags, (cur, "forbidden flag present", r)
        cash += choice.get("cash", 0)
        assert cash >= 0, (cur, "cash negative", cash)
        flags.update(choice.get("setFlags", []))
        cur = choice["next"]

# =====================================================================
# SCENARIO 57 — The Referral That Never Came
# Start: Monday, March 16, 2026. In-home case; child home throughout.
# =====================================================================
S57_START = date(2026, 3, 16)
d57 = lambda off: datestr(S57_START, off)

s57_nodes = [
N("start", 0, "The Plan and the Promise", [
 "Your name is Colleen. Your daughter Nia is six, and she is home with you \u2014 this is an in-home case, under court supervision, and the plan is the paper version of the help everyone agreed your family would get.",
 "The plan orders a parenting program: Brightpath Parenting, twelve sessions, the one the plan names by name. At the last meeting, your worker, Ms. Voss, told you the referral had been sent. All you have to do, she said, is call Brightpath and schedule.",
 "You believe her. There is no reason not to. Believing people is not the problem in this story; what the file does with the next five weeks is.",
], [C("Call Brightpath this week to schedule, the way the plan says", "program_call",
      note="You call on your lunch break, with the plan open on the table and a pen ready for dates.")]),

N("program_call", 2, "No Referral on File", [
 f"You call Brightpath on {d57(2)}. The intake worker is pleasant. She types, she waits, she types again. Then she says the sentence this scenario is built from: there is no referral on file for you. Not pending, not misfiled \u2014 not there.",
 "She checks under your name twice, and under Nia's. Nothing. She suggests, kindly, that you ask your worker to send it, and gives you the program's email address in case it helps to have it in writing.",
 "You hang up with an email address, a pen still in your hand, and a plan that says a thing has happened which, at the program that would know, has not.",
], [C("Call Ms. Voss and tell her exactly what Brightpath said", "worker_call",
      addHidden=["Brightpath Parenting \u2014 no referral on file when mother called to schedule"],
      note="Exactly what they said, in their words: no referral on file. You write the date of this call on the plan itself.")]),

N("worker_call", 4, "It\u2019s in Process", [
 "Ms. Voss is not dismissive. She says the referral was submitted, that these things take time to land, that it is \u201cin process\u201d and she will check on it. She sounds certain. She may even be right about having submitted something, somewhere.",
 "What you have, at the end of the call, is her certainty \u2014 spoken, unrecorded, and held entirely in her memory and yours. What Brightpath has is an empty search result. The case will be measured later by whichever of those two things got written down.",
 "Tonight you can leave it in the world of phone calls, or you can move it into the world of paper. The difference will not matter this week. It will matter in five weeks, in a room you have not been in yet.",
], [C("Send a written email tonight \u2014 to Ms. Voss and to Brightpath \u2014 saying the referral is not on file and asking both to confirm when it is sent", "written_chase",
      setFlags=["referralChased"],
      addHidden=["Referral \u2014 mother emailed worker and program in writing that no referral was on file"],
      note="Short, polite, dated: the plan orders Brightpath; you called; no referral is on file; please confirm when it is sent. Sent emails keep their own dates."),
    C("Accept the assurance \u2014 she said she will check on it", "phone_only",
      note="She probably will. Checking on it is a thing she will do inside a system that does not record her doing it.")]),

N("written_chase", 7, "The Reply, in Writing", [
 "You send the email that evening. Brightpath replies within days, in writing, and their reply is worth more than its two lines suggest: as of this week, the program confirms, it has received no referral for you, and it will contact you the moment one arrives.",
 "Ms. Voss replies too: she is looking into it. No send date is given, because \u2014 though nobody writes this part \u2014 there may not be one to give.",
 "Your sent folder now holds something the case file does not: a dated account of the gap, written while the gap was still new, by you and by the program itself.",
], [C("Save both replies with the plan, and go on with everything else in the case", "wait_begins",
      addHidden=["Program reply \u2014 no referral received, confirmed by the program in writing"],
      note="Everything else \u2014 Nia's school, the home visits, the check-ins \u2014 keeps its own schedule. Only this one line is stuck.")]),

N("phone_only", 7, "Assured, and Waiting", [
 "You let the phone call carry it. The week feels ordinary: Nia's school, your shifts, the home visit that goes fine. Nothing arrives from Brightpath, but nothing was supposed to arrive quickly \u2014 referrals take time to land; you were told so, warmly, by the person whose job it is to know.",
 "What you do not have is any way, later, to show when you first learned the referral was missing, or that you raised it at all. Your memory of the call is clear. Memories are clear in exactly the rooms where they cannot be attached to anything.",
], [C("Go on with everything else in the case, and wait for the referral to land", "wait_begins",
      note="The rest of the plan does not wait. Only this one line does \u2014 silently, in a file you have not seen.")]),

N("wait_begins", 10, "Week Two, Quietly", [
 "Week two. Nia loses a tooth and gains a gap she shows everyone. Your home visits go the way they have been going: the worker looks, you talk, notes are taken in the ordinary way, on the other side of the table.",
 "A scored assessment form is part of cases like yours \u2014 filled in from visits and notes, rating what it can see. What it can see, this month, is a mother whose ordered program has not started. Why it has not started is not a box on the form. It is a fact living in a sent folder, or in a phone call, or nowhere.",
], [C("At the next visit, ask Ms. Voss again about Brightpath \u2014 and notice what is said, and what is written", "flyer_beat",
      note="She says it is still in process. The note she takes does not mention Brightpath at all.")]),

N("flyer_beat", 14, "The Flyer in the Folder", [
 "In the waiting room at the agency office there is a folder of flyers for parents, and one of them \u2014 the kind of paper most people walk past \u2014 says something you read twice: a parent may request their case record, and under 55 Pa. Code \u00a7 3130.44(d) the material \u201cshall be released upon request.\u201d",
 "Your record. The chronology, the notes, the service lines \u2014 the file's own version of these five weeks, which you have never seen. The flyer is not offering you a rescue. It is offering you a look.",
], [C("Take the flyer home and think about what your file currently says about Brightpath", "records_fork",
      note="Somewhere in that file is a service line with your name beside a program you have never attended. You would like to read it before a review does.")]),

N("records_fork", 16, "Ask for the File, or Don\u2019t", [
 "The request is simple and it is yours to make: ask, in writing, for your case record \u2014 the service chronology and the notes about the parenting program. Under 55 Pa. Code \u00a7 3130.44(d), the record is to be released on request; the asking is a right, not a favor, and it leaves a date behind.",
 "Or you can wait for the review and explain the five weeks there, out loud, to people reading a file you have never seen.",
], [C("Put the request in writing \u2014 service chronology and program notes \u2014 and keep a copy", "file_arrives",
      setFlags=["recordsRequested"], cash=-3,
      note="Three dollars of copies and postage across the errand. The request is dated, copied, and kept with the plan."),
    C("Wait for the review \u2014 you can explain it in person", "no_file",
      note="In person is how you have explained everything so far. The file, meanwhile, explains you to everyone else, daily, without you.")]),

N("file_arrives", 21, "Mother to Enroll", [
 f"The packet arrives, and you read the service chronology first, the way you would read weather about your own house. The Brightpath line, in full: \u201cmother to enroll in parenting services.\u201d No referral date. No program name beside a date. No entry recording that anyone sent anything, anywhere.",
 "\u201cMother to enroll.\u201d As if enrolling were a door standing open that you had not walked through \u2014 instead of a referral that had to be sent by someone else before you could walk through anything. The file does not accuse you. It does something quieter: it writes the gap in grammar that assigns it to the only person named in the sentence.",
 "Now you have seen the sentence the review will read. The question is what paper will be sitting next to it.",
], [C("Keep the packet with your emails \u2014 the chronology and the replies belong in the same folder", "progress_note",
      addHidden=["Case chronology \u2014 \u2018mother to enroll in parenting services,\u2019 with no referral date shown"],
      note="Your folder and their file now disagree about the same five weeks, in writing, with dates. That disagreement is the most useful thing you own.")]),

N("no_file", 21, "What You Cannot Quote", [
 "Without the file, you cannot see the service line you are being measured against \u2014 \u201cmother to enroll,\u201d or however it is worded \u2014 and you cannot quote what it leaves out. You know what happened. You know it in the way that cannot be attached to a report.",
 "Your account is true, detailed, and sincere. At the review, it will be weighed the way spoken accounts are weighed in rooms that run on attachments: personally, politely, and against a printed page that says less and therefore somehow says it louder.",
], [C("Go on toward the review with your account \u2014 and keep every email you do have", "progress_note",
      note="Whatever paper exists still exists. The review is weeks away, and weeks are where sentences harden.")]),

N("progress_note", 35, "Not Yet Engaged", [
 f"Five weeks after the plan was signed \u2014 {d57(35)} \u2014 the case gets its next progress note, and you hear its key phrase from Ms. Voss at a check-in, in a level voice: you are recorded as \u201cnot yet engaged in parenting services.\u201d",
 "Not yet engaged. You called the program the first week. You were told \u2014 by the program \u2014 that there was nothing to engage with. You check once more, and Brightpath's answer has not changed: still no referral on file.",
 "A review is coming. Reviews read notes. The note currently says the gap is a fact about you. Whether it stays that way depends on what gets assembled before the review reads it.",
], [C("Ask when the review is, and how much time is left to prepare for it", "prep",
      note="Days, not weeks. Preparation, in this system, is mostly deciding what paper will be in the room.")]),

N("prep", 38, "One Page, or a Story", [
 "Your sent folder holds the whole five weeks, if you wrote the email: your message, the program's reply, the dates. Your packet, if you requested it, holds the chronology with its missing referral date. Assembled in order, they fit on one page: plan ordered, mother called, no referral found, gap raised in writing, program confirmed, chronology silent, note written.",
 "Or the five weeks can stay where they have lived so far \u2014 in your head, in order, in a story you can tell well. Stories are true. Pages are portable. Reviews are rooms you speak in for minutes and files speak in forever.",
], [C("Build the one-page timeline from the sent emails and the chronology, in date order", "timeline_built",
      setFlags=["gapDocumented"],
      addHidden=["Timeline \u2014 one-page dated timeline built from the sent emails and the chronology"],
      note="One page. Every line dated. Nothing on it that the system's own paper does not support."),
    C("Go in with the story in your head \u2014 you lived it, in order", "story_only",
      note="You did, and you can tell it. The note in the file can also be told \u2014 by the file, to every reader, whether you are in the room or not.")]),

N("timeline_built", 40, "The Timeline, Assembled", [
 f"The page reads like a timetable, because it is one. Plan ordered, {d57(0)}. You called Brightpath, {d57(2)} \u2014 no referral on file. The gap raised in writing, {d57(7)} \u2014 the program confirmed it in writing. The chronology, received {d57(21)}, shows no referral date. The progress note, {d57(35)}, calls you not yet engaged.",
 "Five weeks, six lines, no adjectives. Your lawyer's word for a page like this is \u201cquiet.\u201d Quiet pages get read carefully, because there is nothing in them to argue with except their dates.",
], [C("Make copies \u2014 one for the review, one for your lawyer, one for the folder", "review_eve",
      note="Copies are how a page attends meetings you are not invited to. This one is about to attend the most important one.")]),

N("story_only", 40, "Clear in Her Head", [
 "Your account is clear, in order, and true: the call, the assurance, the weeks, the note. Sitting at the kitchen table you can tell it start to finish without a pause. It has only one flaw, and the flaw is not in the telling.",
 "It exists in exactly one place, and that place cannot be handed to a reviewer, attached to a report, or read after you leave the room. The file's version \u2014 \u201cnot yet engaged\u201d \u2014 exists everywhere the file goes.",
], [C("Practice telling it once more, and get Nia settled for the morning", "review_eve",
      note="The review will be short. Short rooms reward paper and punish nothing \u2014 they simply cannot hold what was never handed to them.")]),

N("review_eve", 43, "The Night Before the Review", [
 "The night before the review, your lawyer goes through your folder with you. You have one because the law provides for counsel in these cases, and for appointed counsel if a parent cannot afford one (42 Pa.C.S. \u00a7 6337) \u2014 she is the person whose job is to stand in the review room and make the paper speak in the right order.",
 "\u201cReviews measure the plan against the record,\u201d she says. \u201cTomorrow we find out which record yours is measured against \u2014 the file's one line, or the file's one line plus everything that answers it.\u201d",
 "Nia is asleep. The folder is by the door. The bus fare for the morning is in your coat.",
], [C("Take the folder and the fare, and go to the review", "review", cash=-6,
      note="Six dollars of fare. The folder weighs almost nothing. Both facts are misleading about their value tomorrow.")]),

N("review", 44, "The Review", [
 "The review is orderly and brief. The plan is read line by line. On the Brightpath line, the progress note is quoted \u2014 \u201cnot yet engaged in parenting services\u201d \u2014 and the room begins, in the ordinary way, to treat the five weeks as a fact about you.",
 "Then your lawyer asks that the record be completed before the line is weighed. What happens next depends, with a precision this scenario has been honest about from its first page, on what your choices actually put in her hands.",
], [C("Present the one-page timeline \u2014 the sent emails, the program's written reply, and the chronology attached", "end_win",
      requiresFlags=["referralChased", "recordsRequested", "gapDocumented"],
      note="Six dated lines. The room does the arithmetic itself, out loud, which is where arithmetic changes a record."),
    C("Present what paper you have \u2014 some of it, without the full set", "end_lose",
      note="Part of a timeline is an argument with missing premises. The note, whole and printed, is sitting across the table."),
    C("Tell the five weeks as a story \u2014 the call, the assurance, the waiting", "end_lose",
      note="Your voice is truthful and detailed. The file's voice is one line long and has already been read.")]),

N("end_win", 47, "Ending \u2014 Engaged, On Paper", [], ending=True, debrief=[
 f"WHAT THE FILE HELD (the hidden record, revealed): A dated account of the gap, authored largely by the system itself: your email of {d57(7)} raising the missing referral in writing, Brightpath's written reply confirming no referral had been received, and the agency chronology's own line \u2014 \u201cmother to enroll in parenting services\u201d \u2014 with no referral date beside it. At the review on {d57(44)}, the one-page timeline was put beside the progress note, and the room attributed the five weeks to the missing referral: the enrollment was ordered and the referral sent that day, and the record was corrected to say so. The assessment form rates what it can see; after this review, what it can see includes the reason.",
 "THE PROCESS UNDER THIS PATH (described, keeping to this scenario's verified law): The two instruments were the verified ones. The case record was yours on written request \u2014 it \u201cshall be released upon request\u201d (55 Pa. Code \u00a7 3130.44(d)) \u2014 and requesting it is what let you quote the chronology's silence instead of arguing against a summary of it. Counsel (42 Pa.C.S. \u00a7 6337) presented the timeline in the room where the plan is measured against the record. Nothing here invented a new right: the written chase created the dates, the request revealed the file, and the timeline assembled them. Reviews can only weigh paper that exists in time to be weighed.",
 "THE HONEST PART: Label this win honestly \u2014 it is partial. The parenting program is still ahead of you: twelve sessions, starting now, with all the ordinary difficulty of attending anything for twelve weeks. The case is still open, Nia is home as she has been throughout, and the supervision continues. A different reviewer might have noted the timeline and pressed the schedule anyway, and a worker with a lighter caseload might have caught the unsent referral in week one. Workers, reviewers, and luck all held pieces of this. Your share was narrower and durable: when the system lost five weeks, you made the system sign for them.",
]),
N("end_lose", 47, "Ending \u2014 Not Engaged, As Written", [], ending=True, debrief=[
 "WHAT THE FILE HELD (the hidden record, revealed): One line and one note. The plan's line \u2014 a program ordered \u2014 and the progress note's phrase \u2014 \u201cnot yet engaged in parenting services\u201d \u2014 with nothing in the record explaining the five weeks between them: no dated email, no program reply, no chronology quoted against itself. At the review, your account was heard and, in the way of spoken accounts, believed personally and set aside professionally. The referral was finally sent after the review. The five weeks stayed in the file as yours \u2014 a period of non-engagement, available to every future reader, in a case where you had called the program in the first week.",
 "THE PROCESS UNDER THIS PATH (described, keeping to this scenario's verified law): The tools existed at every step and are the verified ones: chase the gap in writing, so the chase itself has a date; request the record, which \u201cshall be released upon request\u201d (55 Pa. Code \u00a7 3130.44(d)), so the chronology's missing referral date can be shown rather than described; and let counsel (42 Pa.C.S. \u00a7 6337) carry the assembled page into the room. None of that requires anyone to have acted in bad faith. It only requires paper \u2014 because in a review, the burden of explaining a gap quietly falls on the person the gap is written about, whether or not she caused it.",
 "THE HONEST PART: Let this debrief be as fair as the review was not: you did the human part of this correctly and promptly. You called the program the week the plan was signed; the referral was lost on the system's side of the desk, not yours. What was lost with it was not effort \u2014 it was evidence, and the two are different currencies in a file. A different worker might have written the capacity problem into the note herself; some do. This one did not, and outcomes here turn on workers and luck as much as on parents. The sentence in the file is not a verdict on you as a mother. It is a verdict on what was documented \u2014 and a folder started tonight, with the next email, still changes what the next review reads.",
]),
]

s57_meta = {"title": "The First 90 Days",
 "subtitle": "Scenario 57 \u2014 The Referral That Never Came (a fictional composite)",
 "startDateISO": "2026-03-16", "startNode": "start", "startCash": 150,
 "tier": "Foundation",
 "summary": "A court-ordered parenting referral is never sent \u2014 five weeks vanish, and the progress note calls her \u2018not yet engaged.\u2019"}

# =====================================================================
# SCENARIO 58 — The Missed Screen
# Start: Monday, April 13, 2026. Kinship placement predates the story.
# All substance content is procedural: summonses, windows, shifts, logs.
# =====================================================================
S58_START = date(2026, 4, 13)
d58 = lambda off: datestr(S58_START, off)

s58_nodes = [
N("start", 0, "The Protocol, Said Out Loud", [
 "Your name is Desirae. You are in recovery, and your recovery, in this case, is mostly a schedule: meetings, check-ins, work, and screens. Your son Leo is five, and he is living with his grandmother Lorraine \u2014 kinship care, arranged before this story opens, in the house where his drawings are on the refrigerator.",
 "The screen protocol was explained to you out loud, once, at a meeting: summonses come by text, usually the night before; the collection site is across town and its window is 7 to 9 in the morning; your shift starts at 8:30. The plan says a missed screen is recorded as a failed appearance, and a failed appearance is counted the same as a positive result when compliance is tallied.",
 "Your first screen, on a day off, you completed at the far site without incident. The system recorded it, in its one-line way, and moved on. This story is about the second one \u2014 and about the difference between a conflict explained before it happens and a conflict explained after.",
], [C("Keep the protocol in mind, and go on with the week", "night_text",
      note="Said out loud, once. Nothing about it was handed to you in writing. That detail is doing more work than it should.")]),

N("night_text", 7, "The 9:40 Text", [
 f"The text arrives at 9:40 in the evening on {d58(7)}: screen tomorrow, {d58(8)}, 8:00, at the site across town. Your shift tomorrow starts at 8:30. The buses between the site and your workplace do not consult each other, and neither, tonight, does the arithmetic: the far site and an 8:30 shift cannot both be met \u2014 not honestly, not by you, not tomorrow.",
 "You can send a written message tonight \u2014 to the caseworker and the program number that sent the summons \u2014 documenting the conflict before it happens and asking for the nearer collection site or a later window. Or you can say nothing, set two alarms, and try to make both.",
 "Before, or after. In this system, that is not a detail. It is the whole decision.",
], [C("Text back tonight, in writing: the site, your 8:30 shift, the conflict \u2014 and ask for the nearer site or a later window", "morning_moved",
      setFlags=["screenMoved"],
      addHidden=["Screen conflict \u2014 documented in writing the night before; nearer site or later window requested"],
      note="Sent at 9:52 p.m., with a timestamp you did not have to create \u2014 the message carries its own. Asking before is a different act, on paper, than explaining after."),
    C("Say nothing and try to make both \u2014 two alarms, first bus, run", "morning_rush",
      note="Trying is a plan for the morning. It is not a record for the file. Tomorrow will produce one of those anyway \u2014 the question is whose wording it uses.")]),

N("morning_moved", 8, "The Nearer Window", [
 f"The reply comes before your first alarm on {d58(8)}: the nearer collection site, today, in its early window. You go there first, the screen is completed inside the window, and you reach your shift minutes after 8:30 to a supervisor who had already seen your message forwarded the night before \u2014 because paper, forwarded, arrives before you do.",
 "Nothing dramatic happened this morning. That is what a documented conflict looks like from inside it: a problem that was written down early enough to be solved as a scheduling problem, instead of recorded later as a character problem.",
], [C("Keep the reply and the completion slip with your other case papers", "week_after",
      addHidden=["Screen \u2014 completed at the nearer site inside the window after the written request"],
      note="A reply, a slip, a date. The morning now exists in the file the way it existed in your life: a conflict, raised and resolved.")]),

N("morning_rush", 8, "Nine O\u2019Clock, Across Town", [
 f"You run the morning honestly and the morning runs out. The first bus is late by minutes that matter; the site across town comes into view at 9:04 on {d58(8)} \u2014 four minutes after its window closed. The screen is not taken. It cannot be taken; windows are windows.",
 "The form at the desk has a line for this, and the line is filled in with the plan's own language: failed appearance. No one at the desk is unkind, and no one writes down the buses, the alarms, or the arithmetic, because the form has no line for arithmetic.",
 "You go to your shift late as well, with a morning that was entirely effort and is now, on paper, entirely something else.",
], [C("Tell your caseworker what happened today, while it is still today", "week_after",
      note="You tell her the whole morning, accurately. She listens like a person. The form, already filed, listens like a form.")]),

N("week_after", 11, "What the Week Wrote Down", [
 "At the week's check-in, the screen entry is mentioned in passing, in the file's one-line language \u2014 and you understand that the file's version of this week and your version are no longer the same document, whichever morning you lived.",
 "Your lawyer raises the question this scenario turns on. You have one because the law provides for counsel in these cases, and for appointed counsel if a parent cannot afford one (42 Pa.C.S. \u00a7 6337). Her question is short: \u201cWhat does the log itself say \u2014 the summons times, the sites, the entries? Not the summary. The log.\u201d",
], [C("Ask how a parent gets the log itself, in writing", "records_fork",
      note="\u201cThe same way you get any of your record,\u201d she says. \u201cYou ask for it, in writing, and you keep the asking.\u201d")]),

N("records_fork", 15, "Ask for the Log", [
 "The screen log \u2014 every summons, every site, every result entry \u2014 is part of your case record, and the record is to be released on request (55 Pa. Code \u00a7 3130.44(d)). A written request gets you the log itself, to sit with at your own table and check against your own texts and slips.",
 "Or you can keep working from the check-in summaries and the portal's one-line statuses, which is to say: from other people's shortening of your mornings.",
], [C("Request the screen log in writing \u2014 summonses, sites, and result entries \u2014 and keep a copy of the request", "log_arrives",
      setFlags=["recordsRequested"], cash=-3,
      note="Three dollars of copies across the errand. The request is dated; the log, when it comes, can be read line by line against your phone."),
    C("Work from the summaries \u2014 the caseworker reads them to you accurately", "no_log",
      note="She does, and she is accurate. Summaries are still selections: someone else decided which lines of your mornings were the story.")]),

N("log_arrives", 19, "The Log, on Paper", [
 f"The log arrives, and it is illuminating in the specific way of exact things. It records when each summons was sent \u2014 including 9:40 in the evening on {d58(7)} \u2014 which site each screen was assigned to, and what entry each morning received. Times, sites, entries. It is exact about all of them.",
 "What it does not record is reasons. No log does. Reasons live in messages, requests, and replies \u2014 which is why the ones you sent, if you sent them, are the other half of this document, and why keeping them matters as much as requesting this half.",
], [C("Put the log with your texts and slips, in date order", "month_two",
      addHidden=["Screen log \u2014 summons times, sites, and entries obtained and kept by parent"],
      note="Two halves of the same mornings, both on paper now: what the system recorded, and what you wrote before it recorded anything.")]),

N("no_log", 19, "Pending, in the Portal", [
 "Without the log, your mornings exist as statuses: completed, failed appearance, pending. Statuses have no times attached, no sites, no sequence. A summons sent at 9:40 the night before and a summons sent a week ahead wear, in status language, exactly the same clothes.",
 "You know the sequence. Knowing it is your half of a conversation the file is having without you, in a room \u2014 the review \u2014 where the file's half is the one printed out.",
], [C("Go on toward month two \u2014 and keep every text and slip from here", "month_two",
      note="From here is later than from the start, and earlier than the review. Paper has a way of being worth whatever week it begins in.")]),

N("month_two", 36, "The Second Text", [
 f"Month two brings a second summons cycle \u2014 and this time the screen itself goes fine: summoned with notice, completed at the assigned site on {d58(36)}, inside the window, on a day your shift allowed it. You keep the confirmation text. The site issues its dated completion slip.",
 "Then the system's paperwork does to this screen what the buses tried to do to the first one: the result posts late. Days pass. At the agency's end, your file shows the screen's result as not received \u2014 a completed screen wearing, in the file, the clothes of a missed one.",
 "A late posting is a small, ordinary system delay. So was an unsent referral, in another family's story. What decides what it becomes is whether anyone can prove, from paper, when the thing actually happened.",
], [C("Keep the confirmation text and the dated slip, and send a written note that the screen was completed on its date", "paper_kept",
      setFlags=["proofKept"],
      addHidden=["Screen completion \u2014 confirmation text and dated slip kept; late posting raised in writing"],
      cash=-8,
      note="Eight dollars of fares for that screen day, spent either way. The note costs nothing and dates everything: completed, on this date, confirmation attached."),
    C("Trust the portal to catch up \u2014 these things sort themselves out", "portal_only", cash=-8,
      note="Eight dollars of fares, spent either way. Portals do catch up, usually, eventually \u2014 on their schedule, in their wording, after the rooms that needed them.")]),

N("paper_kept", 38, "Kept: The Confirmation", [
 "Your written note goes in with the confirmation and the slip attached, and the file gains a dated claim it will eventually have to agree with: when the result does post, it posts with the completion date intact \u2014 the system's own record conceding, in its own time, that the screen happened when you said it did.",
 "It should not take a note and two attachments to establish that a completed screen was completed. In a file built from postings and statuses, it does. That is not a fact about your credibility. It is a fact about what files are made of.",
], [C("File the posted result with the note, and turn to the review ahead", "prep",
      note="The pair \u2014 your dated note, their late posting \u2014 now tells the true story without you having to say a word about it.")]),

N("portal_only", 38, "The Portal Says Pending", [
 "The portal says pending. It says it on the day of the check-in, and it is still saying it when the review packet is being assembled. Your completion \u2014 real, dated in the world, witnessed by a desk and a slip you did not keep \u2014 exists in the system as an absence with a deadline.",
 "Absences, in compliance tallies, do not stay neutral. They get read in the direction the plan's language points, and the plan's language points one way: toward the parent.",
], [C("Turn to the review ahead, with the phone that holds the summons texts", "prep",
      note="The texts are something. The slip would have been something more. The review will price the difference precisely, because pricing paper is what reviews do.")]),

N("prep", 50, "Assemble the Paper", [
 "The review is close, and preparation is an assembly job: the summons texts with their 9:40 timestamp, your written replies if you sent them, the screen log if you requested it, the confirmations and slips if you kept them. In date order, they tell a scheduling story with no adjectives in it: conflicts raised before they happened, screens completed inside their windows, postings that lagged behind completions.",
 "Or the same weeks can be carried into the review the way they were lived \u2014 as a story about buses, alarms, and effort, told by the person who set the alarms. True stories are this scenario's most common casualty.",
], [C("Assemble the packet \u2014 texts, log, confirmations, slips \u2014 in date order, with your lawyer", "packet_ready",
      setFlags=["packetBuilt"],
      addHidden=["Review packet \u2014 summons texts, screen log, and completion confirmations assembled in date order"],
      note="No adjectives. Just times: when they summoned, when you answered, when you appeared, when they posted. Times are hard to argue with."),
    C("Bring the phone and explain the mornings in person", "story_only",
      note="The phone holds some of it. The rest is in your voice, which is vivid, sincere, and \u2014 in a room running on exhibits \u2014 unaccompanied.")]),

N("packet_ready", 52, "Texts, Log, and Slips", [
 "The packet is thinner than you expected and heavier than it looks: a night-before message with its timestamp, a log with its exact times, a confirmation with its date. Three kinds of paper, each made by a different hand \u2014 yours, the system's, the site's \u2014 agreeing with each other.",
 "Your lawyer reads it once and says the sentence this scenario has been walking toward: \u201cThis doesn't argue that you tried. It shows when everything happened. Reviews believe clocks.\u201d",
], [C("Make copies, and spend the evening with Leo at Lorraine's, the way evenings should be spent", "review_eve",
      note="Copies made. The packet will do its work in a room; tonight's work is a five-year-old and a refrigerator covered in drawings.")]),

N("story_only", 52, "Everything on the Phone", [
 "Your account of these months is accurate in every particular you can name: the 9:40 text, the two alarms, the closed window, the completed screen whose result went missing into a late posting. You can tell it in order, without notes, because you lived it in order.",
 "Its flaw is structural, not personal: it can only be in one room at a time, for as long as you are speaking in it, and the file's one-line version \u2014 failed appearance; result not received \u2014 is in every room, forever, in print.",
], [C("Practice the account once, and spend the evening with Leo at Lorraine's", "review_eve",
      note="Practice helps the telling. It does not give the telling a date stamp, an attachment, or a second reader.")]),

N("review_eve", 55, "The Night Before the Review", [
 "The night before the review, Lorraine keeps Leo for the evening so you can prepare, and the house is quiet in the particular way of houses where the important paper is already done \u2014 or already not done.",
 "Tomorrow the review will tally compliance the way the plan says it is tallied: screens summoned, screens recorded. What the tally will meet, when it reaches your mornings, is either a packet of times or a story about them. You already know which one you are carrying. So, in a sense, does the file.",
], [C("Take the folder, pay the morning's fare in advance, and go to the review", "review", cash=-6,
      note="Six dollars of fare, set out tonight. Small preparations are still preparations; this whole case has run on them.")]),

N("review", 56, "The Review", [
 f"The review on {d58(56)} is orderly and brief. The plan's screen line is read the way the file holds it \u2014 summonses, entries, tallies \u2014 and the tally begins moving toward the conclusion the one-line entries point to.",
 "Then your lawyer asks that the underlying times be put beside the tally before the tally is adopted. What happens next depends, with a precision this scenario has been honest about from its first text message, on what your choices actually put in her hands.",
], [C("Present the packet \u2014 the night-before message, the screen log, and the completion confirmations", "end_win",
      requiresFlags=["screenMoved", "recordsRequested", "packetBuilt"],
      note="Times, in date order, from three different hands. The tally is re-done in the room, out loud, which is where tallies change."),
    C("Present what paper you have \u2014 part of the packet, assembled late", "end_lose",
      note="Part of a timeline answers part of a tally. The one-line entries, whole and printed, answer the rest."),
    C("Explain the mornings out loud \u2014 the alarms, the buses, the late posting", "end_lose",
      note="Every word of it is true. The tally, which runs on entries, keeps its own counsel about truth it cannot attach to anything.")]),

N("end_win", 59, "Ending \u2014 Documented, Not Positive", [], ending=True, debrief=[
 f"WHAT THE FILE HELD (the hidden record, revealed): A scheduling record with its times intact: a summons sent at 9:40 in the evening on {d58(7)}, your written answer that same night documenting the conflict with your 8:30 shift and asking for the nearer site, the nearer site's completed screen, the screen log obtained on request showing summons times, sites, and entries, and \u2014 for month two's screen \u2014 the confirmation and dated slip that proved completion on {d58(36)} when the result posted late. At the review, the tally was corrected against its own underlying times: no failed appearance stands for the conflict morning, the late posting was entered as a late posting, and both screens stand as what they were \u2014 completed.",
 "THE PROCESS UNDER THIS PATH (described, keeping to this scenario's verified law): The instruments were the verified ones. The screen log was part of your case record, released on request (55 Pa. Code \u00a7 3130.44(d)) \u2014 requesting it is what let the review compare the tally to the times instead of adopting the tally. Counsel (42 Pa.C.S. \u00a7 6337) carried the packet into the room. And the decisive move was the earliest one, and it was generic process, not a citation: a conflict documented in writing before it happened, which converted a morning that the plan's language would have tallied against you into a morning the record describes as a scheduling problem, raised and solved. The plan's default \u2014 a missed screen counted the same as a positive result \u2014 was never triggered, because on paper there was no miss.",
 "THE HONEST PART: Label this win for what it is: a corrected tally, not a finished case. Your screens continue, your recovery continues on its own schedule of meetings and work, Leo is still living at Lorraine's, and the case is still open. A different collection site might never have answered the night-before message; a different supervisor might have read the same packet ungenerously; the buses, on another morning, beat everyone. Workers, sites, and luck all held pieces of this outcome. What your choices changed was the evidence those pieces landed on. Nothing in this ending is a verdict on your recovery \u2014 it is a record of two mornings, documented as scheduling facts, which is all they ever were.",
]),
N("end_lose", 59, "Ending \u2014 Positive, By Default", [], ending=True, debrief=[
 "WHAT THE FILE HELD (the hidden record, revealed): One-line entries, doing what one-line entries do. A failed appearance for the morning the buses won \u2014 recorded without the 9:40 summons, the 8:30 shift, or the arithmetic that made the morning impossible \u2014 and a completed screen in month two whose result, posted late, sat in the file as not received when the tally was made. At the review, the plan's default did the rest, exactly as the plan says it does: a failed appearance counted the same as a positive result. No test was failed. No result was positive. The tally is positive anyway \u2014 by default, which is to say, by paperwork.",
 "THE PROCESS UNDER THIS PATH (described, keeping to this scenario's verified law): Every instrument that would have prevented this existed and is verified. A written message the night before would have dated the conflict before it happened and asked, on paper, for the nearer site \u2014 generic process that costs nothing but nerve. The screen log was available on written request (55 Pa. Code \u00a7 3130.44(d)), and would have shown the review the summons times and sites behind the tally's one lines. Counsel (42 Pa.C.S. \u00a7 6337) can assemble and present whatever paper exists. What counsel cannot do is manufacture, at the review, a timestamp from a night two months past. Defaults rule wherever documentation doesn't \u2014 that sentence, not any fact about you, is this ending.",
 "THE HONEST PART: Be clear, because the file was not: you set two alarms, ran for a bus, and completed the screen the system later lost in its own posting queue. Your recovery through these months was a schedule you kept \u2014 meetings, shifts, a son at his grandmother's who got his mother on time \u2014 and none of that is measured by this tally, in either direction. A kinder site, a caseworker who wrote the conflict into the note herself, a posting that landed on time: any of them changes this ending without you changing anything. Workers, postings, and luck signed it alongside your choices. It records a default, not a relapse, not a character \u2014 and the next summons, answered in writing the night it arrives, starts a different paper trail from its first timestamp.",
]),
]

s58_meta = {"title": "The First 90 Days",
 "subtitle": "Scenario 58 \u2014 The Missed Screen (a fictional composite)",
 "startDateISO": "2026-04-13", "startNode": "start", "startCash": 120,
 "tier": "Foundation",
 "summary": "Random screens by text, a site across town, a shift at 8:30 \u2014 a missed screen is tallied like a positive unless the conflict is on paper first."}

# =====================================================================
# SCENARIO 59 — Two Buses to the Visit
# Start: Monday, May 11, 2026. Foster placement predates the story.
# =====================================================================
S59_START = date(2026, 5, 11)
d59 = lambda off: datestr(S59_START, off)

s59_nodes = [
N("start", 0, "The Letter About the Visits", [
 "Your name is Andre. Your daughter Ruby is seven, and she is in foster care \u2014 placed before this story opens, in a home across the county from yours. Your visits with her have been the steady part of this case: Saturday afternoons at the neighborhood office, a short walk from your door, in a room Ruby knows.",
 f"The letter that arrives on {d59(0)} is one page and entirely procedural. Because of a provider consolidation, visits are moving: starting this week, they will be held at a visitation center across the county. Same day, same time. What the letter does not mention is the journey \u2014 two buses, ninety minutes each way, with a connection that works when it works.",
 "Nothing in the letter invites a reply. Letters like this rarely do. Whether one is sent anyway is the decision this scenario is built from.",
], [C("Take the two buses to the new center for the first moved visit", "first_trip", cash=-12,
      note="Twelve dollars of fares for the round trip. You leave ninety minutes before the visit \u2014 the letter's own arithmetic, done by you, at your kitchen table.")]),

N("first_trip", 5, "Two Buses, Ninety Minutes", [
 f"The first trip teaches you the route's true shape. The first bus is fine. The connection is not: it leaves as your bus arrives, and the next one costs you twenty minutes you had already spent twice in your head. You reach the center on {d59(5)} twenty minutes after the visit was to start, having left home ninety minutes early.",
 "The visit is shortened by exactly the lateness. Ruby takes it the way seven-year-olds take shortened things \u2014 completely, and then, because she is Ruby, she gets on with the visit there is. You sign the center's sign-in sheet on the way in. Its clock says what time you arrived. It does not say when you left home, or why the road took what it took.",
], [C("Sign in, take the visit there is, and keep the transfer stubs in your pocket", "note_exists",
      addHidden=["Visit note \u2014 \u2018father arrives late; visit shortened\u2019"],
      note="The stubs go in your pocket out of habit. Habits like that are about to matter more than they should have to.")]),

N("note_exists", 6, "Father Arrives Late", [
 "Days later, you hear the first visit described the way the file describes it, in the note that follows the visit: \u201cfather arrives late; visit shortened.\u201d Four words of arrival, one of consequence. No letter, no move, no buses, no ninety minutes \u2014 a note about a man who was late, written about a journey it does not mention.",
 "The note is not false. You did arrive late, and the visit was shortened. It is simply the journey with the journey removed \u2014 and a file, read over months, becomes the notes it is made of. Future readers will meet this sentence before they ever meet you.",
 "The move can still be answered \u2014 in writing, asking for a nearer site or for transportation support, on paper where answers live. Or it can be absorbed, Saturday by Saturday, one shortened visit at a time.",
], [C("Decide how to answer the move \u2014 on paper, or not at all", "split_request",
      note="Not at all is also an answer. It is the one the file is currently assuming you gave.")]),

N("split_request", 7, "Answer the Move, or Absorb It", [
 "A written answer is a small, plain thing: a dated letter or email to your caseworker and the center, saying the visits moved, what the new journey takes \u2014 two buses, ninety minutes \u2014 and asking for a nearer site or for transportation support. It does not refuse anything. It does not threaten anything. It puts the journey into the same file that currently holds only the arrival.",
 "Absorbing it is also plain: leave earlier, run the same buses, say nothing on paper, and let the notes keep their four words. The visits will happen either way. What differs is what the review, months from now, will be able to read about why they started late.",
], [C("Answer the move in writing \u2014 nearer site or transportation support, asked for on paper", "written_track",
      setFlags=["visitMoveAnswered"],
      addHidden=["Visit move \u2014 answered in writing; nearer site or transportation support requested"],
      cash=-12,
      note="Dated, copied, kept. Twelve more dollars of fares take you to the second visit \u2014 the asking and the going now travel together."),
    C("Absorb it quietly \u2014 leave earlier and say nothing on paper", "quiet_track", cash=-12,
      note="Twelve dollars of fares, an earlier alarm, and no letter. The journey gets longer and the file stays exactly as short as it was.")]),

N("written_track", 9, "Asked, on Paper", [
 "Your letter goes in this week, and the reply, when it comes, is honest about the system's shape: the consolidation is provider-wide, your request is noted, and a nearer site or support will be \u201cconsidered as capacity allows.\u201d No change is promised. No date is given.",
 "And yet the file is different tonight than it was last week. It now contains two documents about Saturdays: a note that says you arrive late, and a dated letter that says what arriving now requires and what you asked for. Reviews are where documents like those meet. They have not met yet.",
], [C("Go to the second visit \u2014 and pay attention to the sign-in sheet this time", "log_beat",
      note="The center's sheet records arrivals to the minute. Minutes, it turns out, can be evidence \u2014 if anyone keeps them.")]),

N("quiet_track", 9, "The Same Trip, Quietly", [
 "You leave earlier. The buses do not reward it reliably \u2014 connections keep their own counsel \u2014 and the second Saturday's journey takes what it takes. Nothing about the trip is written anywhere except the stubs in your pocket and the sign-in sheet at the other end.",
 "Quiet has a cost structure of its own: it costs nothing today, in nerve or postage, and it charges later, in a room where the only account of your Saturdays is a column of arrival times with no journey attached to any of them.",
], [C("Go to the second visit \u2014 and pay attention to the sign-in sheet this time", "log_beat",
      note="The sheet is by the door, with its clock and its ruled lines. It has been recording your case all along. The question is whether you start keeping a copy of its story.")]),

N("log_beat", 12, "The Sign-In Sheet", [
 f"The second visit, {d59(12)}: the journey runs long again \u2014 not by your choosing, which is rather the point \u2014 and you sign in below the other names, at the time the center's clock gives you. The sheet is a plain document: names, times, a column for the room. It will be filed. It is, whether anyone calls it this, the center's own record of what the move costs.",
 "You can start keeping your own arrival log \u2014 photograph the sign-in sheet each visit, note your departure time and the buses, keep the stubs \u2014 so that arrival times someday sit beside journey times. Or you can sign, go in, and spend the visit being a father instead of a filing system, which is also a completely understandable choice, and the one the file is quietly counting on.",
], [C("Photograph the sign-in sheet and start a dated arrival log \u2014 departures, buses, arrivals", "third_visit",
      setFlags=["arrivalLog"],
      addHidden=["Arrival log \u2014 sign-in times photographed; departures and buses logged by father"],
      note="Thirty seconds with a phone, at a door, each Saturday. The log is boring. Boring, dated, and yours \u2014 the three qualities exhibits are made of."),
    C("Sign in and go straight in \u2014 the visit is the point, not the paperwork", "third_visit",
      note="The visit is the point. It is also, in note form, the only part of the day the file will describe as shortened \u2014 and the log is the only version of the journey that would ever be attached to it.")]),

N("third_visit", 19, "The Third Saturday", [
 f"The third visit, {d59(19)}, runs the way the route runs: a connection missed or made by minutes, an arrival after the start, a visit shortened by the difference. If you are keeping the log, this Saturday's page joins the others \u2014 departure, buses, sign-in time, each dated, none of them argued about.",
 "Ruby has started managing the shortened visits the way she manages everything: completely, and then practically. She has a order she does things in now, so the important things happen first in case the end comes early. It is a sensible system. It is also a sentence no parent should have to watch a seven-year-old invent, and the file's version of its cause is still four words long: father arrives late.",
], [C("Pay the third trip's fares into the same pocket as the stubs, and go home the long way", "pattern_note", cash=-12,
      note="Twelve dollars, third time. The fares are the move's real price list, and so far you are the only one keeping it.")]),

N("pattern_note", 23, "Three Times, One Word", [
 "The pre-review summary arrives, and your Saturdays are in it as a pattern now: three visits, each described with the same word. Late. Late. Late \u2014 shortened, shortened, shortened. Patterns in summaries are how single notes grow into character, and character is how summaries get used at reviews.",
 "The summary does not mention the letter that moved the visits, because the summary was written from the notes, and the notes never mentioned it either. A pattern built from arrivals alone is now the official shape of your effort \u2014 unless the underlying documents are ever put beside it.",
 "The visit notes themselves \u2014 the center's own pages, with their recorded times \u2014 are part of your case record. You have not seen them. You could.",
], [C("Ask how to get the visit notes themselves, in writing", "records_fork",
      note="Not the summary of the notes. The notes \u2014 the center's own times, in the center's own hand, for all three Saturdays.")]),

N("records_fork", 25, "Ask for the Notes", [
 "The request is yours to make: ask, in writing, for the visit notes from your case record. Under 55 Pa. Code \u00a7 3130.44(d), the record is to be released on request \u2014 the material \u201cshall be released upon request\u201d \u2014 and visit notes are the record of the very Saturdays the summary has been describing in one word.",
 "Or you can go to the review armed with the summary and your own account of the buses, and ask the room to take the journey on your word, against the pattern on its paper.",
], [C("Request the visit notes in writing \u2014 all three visits \u2014 and keep a copy of the request", "notes_arrive",
      setFlags=["recordsRequested"], cash=-3,
      note="Three dollars of copies across the errand. The notes, when they come, will be the center's own account \u2014 which is exactly why they are worth requesting."),
    C("Work from the summary \u2014 you know what the notes will say", "no_notes",
      note="You know what you lived. What the notes say \u2014 their exact times, their exact words \u2014 is a different piece of knowledge, and reviews run on the second kind.")]),

N("notes_arrive", 30, "The Center\u2019s Own Times", [
 f"The notes arrive, and you read them with the letter open beside them. The center recorded what it records: scheduled starts, sign-in times, shortened endings \u2014 arrivals twenty, fifteen, and eighteen minutes after the start, across the three Saturdays, each one dated, each one in the center's own hand.",
 f"Read alone, they are the pattern. Read beside the move letter of {d59(0)} and your log \u2014 departures ninety minutes before each start, buses, connections \u2014 they become something else: the system's own measurements of the journey the system imposed. The center timed your lateness very carefully. It is only fair that its times be allowed to testify about the whole trip.",
], [C("Put the notes with the letter and the log, in date order", "prep",
      addHidden=["Visit notes \u2014 center\u2019s recorded arrival times obtained and kept with the move letter"],
      note="Letter, log, notes. Three documents, three different authors, one journey. Assembled, they are the first complete account of your Saturdays anyone has made.")]),

N("no_notes", 30, "Summaries of Summaries", [
 "Without the notes, the review will be a meeting about a summary of notes you have never seen \u2014 their times summarized into a word, the word repeated into a pattern, the pattern carried into a room as your record. At each step the journey fell away, because at each step the journey was in nobody's document.",
 "You still know it by heart: the departure times, the connection, the clock over the sign-in sheet. Knowledge by heart is real knowledge. It is just not the kind that gets photocopied for a review packet.",
], [C("Turn to preparing for the review, with what you have", "prep",
      note="What you have is true, warm, and unattached. The review is the kind of room that attaches things or it does not weigh them.")]),

N("prep", 36, "One Packet, in Date Order", [
 "Preparation is assembly: the move letter with its date, your written answer if you sent one, your arrival log if you kept one, the center's notes if you requested them. In date order they make a single argument without raising their voice: the visits moved on this date; the journey became this; the arrivals became that; here is every document, including the system's own.",
 "Or the Saturdays can be carried in as a story \u2014 a father, two buses, a little girl with an order she does things in. It is a story that deserves a better room than the one it is about to be told in, because that room runs on packets.",
], [C("Assemble the packet \u2014 letter, written answer, log, and notes \u2014 in date order", "packet_ready",
      setFlags=["reviewPacket"],
      addHidden=["Review packet \u2014 move letter, written answer, arrival log, and visit notes in date order"],
      cash=-4,
      note="Four dollars of copies. The packet's first page is the move letter \u2014 because chronology is the argument, and chronology starts there."),
    C("Bring the story and the stubs \u2014 the room should hear it from you", "story_only",
      note="The stubs are real, and in a pocket they are almost documents. In a packet they would have been pages. The distance between those two is this scenario's whole geography.")]),

N("packet_ready", 38, "Letter, Log, and Notes", [
 "The packet is not thick. It does not need to be. Its power is sequence: a one-page letter moves a visit; a dated reply answers the move; a log records the journeys; the center's own notes record the arrivals; and the summary's one word \u2014 late \u2014 is left sitting on top of four documents that explain it more completely than it explains itself.",
 "Your lawyer, reading it through, taps the move letter once. \u201cEverything after this page is a consequence of this page,\u201d she says. \u201cTomorrow we just ask the record to admit it.\u201d",
], [C("Make a copy for the folder, and go home the long way one more time", "review_eve",
      note="Ninety minutes home, the route the packet is about. Tomorrow, for once, the journey gets described by the people who made it \u2014 on paper, in order.")]),

N("story_only", 38, "What He Knows, Unwritten", [
 "You know your Saturdays completely: when you leave, which connection fails, the clock over the sign-in sheet, Ruby's order of important things. The knowledge is exact, lived, and entirely in one person's keeping \u2014 yours.",
 "Tomorrow it will be offered, out loud, against a printed pattern. Rooms like tomorrow's do not doubt fathers like you, particularly. They simply have a rule they cannot say out loud: what is not in the packet is, for the record, a claim; and claims are weighed against documents the way voices are weighed against clocks.",
], [C("Get the fare ready for the morning, and go to bed early", "review_eve",
      note="Early bed, early bus \u2014 the disciplines of a man whose file says the opposite of his alarms. Both facts will be in the room tomorrow. Only one of them is printed.")]),

N("review_eve", 41, "The Night Before the Review", [
 "The night before the review, your lawyer goes through the materials with you one last time. You have counsel because the law provides for it in these cases, and for appointed counsel if a parent cannot afford one (42 Pa.C.S. \u00a7 6337); her job tomorrow is to make the record describe a journey instead of a trait.",
 "\u201cLate,\u201d she says, \u201cis a conclusion. Tomorrow we find out whether the record underneath it gets read \u2014 the letter, the log, their own times \u2014 or whether the conclusion gets to keep standing in for all of it.\u201d",
], [C("Take the folder and the morning fare, and go to the review", "review",
      note="The folder, the fare, and the earliest bus there is. Some preparations are paper. Some are just mornings, made on purpose.")]),

N("review", 42, "The Review", [
 f"The review on {d59(42)} takes up your visits in their summary form: a pattern of lateness, three shortened visits, a concern noted about consistency. The words are read aloud in the level tone of people reading weather.",
 "Then your lawyer asks that the underlying documents be put beside the summary \u2014 the move, the answer, the journeys, the center's own times \u2014 before the pattern is adopted as your record. What happens next depends, with a precision this scenario has been honest about since the first bus, on what your choices actually put in her hands.",
], [C("Present the packet \u2014 the move letter, the written answer, the arrival log, and the center\u2019s own notes", "end_win",
      requiresFlags=["visitMoveAnswered", "arrivalLog", "recordsRequested", "reviewPacket"],
      note="Chronology does the arguing: first the move, then the asking, then the journeys, then their own times. The pattern is re-read in the room, in order."),
    C("Present what you have \u2014 part of the packet, without the full sequence", "end_lose",
      note="Part of a chronology is a story with its first page missing. The summary, whole and printed, has no missing pages."),
    C("Tell the Saturdays as a story \u2014 the departures, the buses, Ruby\u2019s order of things", "end_lose",
      note="It is the truest telling in the room. The pattern across the table is the printed one, and printed things are what reviews adopt.")]),

N("end_win", 45, "Ending \u2014 On Time, On Record", [], ending=True, debrief=[
 f"WHAT THE FILE HELD (the hidden record, revealed): A complete chronology, written by four different hands: the move letter of {d59(0)} relocating the visits across the county; your dated written answer asking for a nearer site or transportation support; your arrival log \u2014 departures, buses, stubs \u2014 kept from the second visit on; and the visitation center's own notes, obtained on request, recording the arrivals its move produced. At the review, the pattern was re-attributed on the record: the lateness belonged to the move, not to the father. Visits were ordered to a nearer site for the next cycle, with transportation support in the meantime, and the note language was corrected to carry the journey with the arrival.",
 "THE PROCESS UNDER THIS PATH (described, keeping to this scenario's verified law): The instruments were the verified ones. The visit notes were part of your case record, released on request (55 Pa. Code \u00a7 3130.44(d)) \u2014 requesting them is what turned the center's times into evidence for the journey instead of only against the arrival. Counsel (42 Pa.C.S. \u00a7 6337) presented the packet in sequence. The rest was generic process, done early and on paper: a move answered in writing while it was still new, and a log kept from the second visit, when the log-keeping was still a choice. Nothing here required the center or the agency to have acted in bad faith \u2014 only that consequences, to be weighed fairly, have to be documented by someone. This time, they were.",
 "THE HONEST PART: Label this win honestly \u2014 it is partial. Ruby is still in foster care tonight; this ending moves visits, not custody, and the three shortened visits already happened: that time with her is not returned by any order, and Ruby's careful order-of-things will take longer to unlearn than it took to learn. A different reviewer might have noted the journey and kept the far site anyway; a center whose sign-in times were sloppier would have given the packet less to work with. Workers, centers, reviewers, and bus connections all held pieces of this. Your share was the paper: you answered a one-page letter with a dated letter, and then you kept the receipts of every journey the letter imposed. On the record now, you were on time where it counts \u2014 in the documents, in order, from the first week.",
]),
N("end_lose", 45, "Ending \u2014 Late, As Recorded", [], ending=True, debrief=[
 "WHAT THE FILE HELD (the hidden record, revealed): Three notes and a summary: \u201cfather arrives late; visit shortened,\u201d repeated into a pattern, and read at the review as a concern about consistency. The move letter is in the file too \u2014 filed, unanswered by you, and unconnected to the notes by any document: no dated request, no arrival log, no visit notes obtained and put beside the summary. Your account at the review was detailed and, in the way of unaccompanied accounts, believed personally and adopted never. The far site stands. The shortened visits continue. The pattern now has the review's weight behind it, available to every future reader as the settled shape of your Saturdays.",
 "THE PROCESS UNDER THIS PATH (described, keeping to this scenario's verified law): The tools existed from the first week, and they are the verified ones plus one habit. Answer the move in writing \u2014 a nearer site or transportation support, asked for on paper, so the asking has a date. Keep an arrival log, so journey times exist beside arrival times. And request the visit notes, which as part of your case record are released on request (55 Pa. Code \u00a7 3130.44(d)), so the center's own times can be read beside the letter that caused them; counsel (42 Pa.C.S. \u00a7 6337) can then present a chronology instead of a claim. None of this guarantees a nearer site. It guarantees the review must describe a journey before it may describe a trait \u2014 and in this ending, no one made it.",
 "THE HONEST PART: The record's sentence is not a verdict on you as a father, and this debrief will not pretend it is a fair summary of you either: you left ninety minutes early, paid the fares three times over, and showed up \u2014 across a county, on two buses \u2014 for every visit there was. The system moved the room and then recorded the journey as a flaw in the traveler, because arrivals are timed by clocks and journeys are only recorded by the people who make them. A different center might have written the move into its own notes; some do. This one timed instead. What remains yours is portable: the next visit can be logged, the move can still be answered in writing, and a log begun next Saturday is worth more at the next review than this paragraph's fairness. Late, as recorded, is a description of a file. It was never a description of the effort.",
]),
]

s59_meta = {"title": "The First 90 Days",
 "subtitle": "Scenario 59 \u2014 Two Buses to the Visit (a fictional composite)",
 "startDateISO": "2026-05-11", "startNode": "start", "startCash": 140,
 "tier": "Foundation",
 "summary": "Visits move across the county \u2014 two buses, ninety minutes, twenty minutes late \u2014 and the note records only that he was late."}

# =====================================================================
# BUILD, EMIT, WALK
# =====================================================================
WIN57 = {
 "start": "Call Brightpath this week to schedule, the way the plan says",
 "program_call": "Call Ms. Voss and tell her exactly what Brightpath said",
 "worker_call": "Send a written email tonight \u2014 to Ms. Voss and to Brightpath \u2014 saying the referral is not on file and asking both to confirm when it is sent",
 "written_chase": "Save both replies with the plan, and go on with everything else in the case",
 "wait_begins": "At the next visit, ask Ms. Voss again about Brightpath \u2014 and notice what is said, and what is written",
 "flyer_beat": "Take the flyer home and think about what your file currently says about Brightpath",
 "records_fork": "Put the request in writing \u2014 service chronology and program notes \u2014 and keep a copy",
 "file_arrives": "Keep the packet with your emails \u2014 the chronology and the replies belong in the same folder",
 "progress_note": "Ask when the review is, and how much time is left to prepare for it",
 "prep": "Build the one-page timeline from the sent emails and the chronology, in date order",
 "timeline_built": "Make copies \u2014 one for the review, one for your lawyer, one for the folder",
 "review_eve": "Take the folder and the fare, and go to the review",
 "review": "Present the one-page timeline \u2014 the sent emails, the program's written reply, and the chronology attached",
}
WIN58 = {
 "start": "Keep the protocol in mind, and go on with the week",
 "night_text": "Text back tonight, in writing: the site, your 8:30 shift, the conflict \u2014 and ask for the nearer site or a later window",
 "morning_moved": "Keep the reply and the completion slip with your other case papers",
 "week_after": "Ask how a parent gets the log itself, in writing",
 "records_fork": "Request the screen log in writing \u2014 summonses, sites, and result entries \u2014 and keep a copy of the request",
 "log_arrives": "Put the log with your texts and slips, in date order",
 "month_two": "Keep the confirmation text and the dated slip, and send a written note that the screen was completed on its date",
 "paper_kept": "File the posted result with the note, and turn to the review ahead",
 "prep": "Assemble the packet \u2014 texts, log, confirmations, slips \u2014 in date order, with your lawyer",
 "packet_ready": "Make copies, and spend the evening with Leo at Lorraine's, the way evenings should be spent",
 "review_eve": "Take the folder, pay the morning's fare in advance, and go to the review",
 "review": "Present the packet \u2014 the night-before message, the screen log, and the completion confirmations",
}
WIN59 = {
 "start": "Take the two buses to the new center for the first moved visit",
 "first_trip": "Sign in, take the visit there is, and keep the transfer stubs in your pocket",
 "note_exists": "Decide how to answer the move \u2014 on paper, or not at all",
 "split_request": "Answer the move in writing \u2014 nearer site or transportation support, asked for on paper",
 "written_track": "Go to the second visit \u2014 and pay attention to the sign-in sheet this time",
 "log_beat": "Photograph the sign-in sheet and start a dated arrival log \u2014 departures, buses, arrivals",
 "third_visit": "Pay the third trip's fares into the same pocket as the stubs, and go home the long way",
 "pattern_note": "Ask how to get the visit notes themselves, in writing",
 "records_fork": "Request the visit notes in writing \u2014 all three visits \u2014 and keep a copy of the request",
 "notes_arrive": "Put the notes with the letter and the log, in date order",
 "prep": "Assemble the packet \u2014 letter, written answer, log, and notes \u2014 in date order",
 "packet_ready": "Make a copy for the folder, and go home the long way one more time",
 "review_eve": "Take the folder and the morning fare, and go to the review",
 "review": "Present the packet \u2014 the move letter, the written answer, the arrival log, and the center\u2019s own notes",
}

if __name__ == "__main__":
    jobs = [
        (57, s57_meta, s57_nodes, S57_START, "The Referral That Never Came",
         "This scenario depicts an in-home case under court supervision: a court-ordered parenting program, a referral that goes missing, progress notes, and a review hearing, told through calls, emails, and file pages. There is no graphic content. Players may skip any scene or use the quick exit at any time.",
         WIN57, "end_win"),
        (58, s58_meta, s58_nodes, S58_START, "The Missed Screen",
         "This scenario depicts a parent in recovery whose son is in kinship care: random screens summoned by text, work-shift conflicts, screen logs, and a review hearing, told entirely as scheduling and paperwork. There is no graphic content and no depiction of substance use. Players may skip any scene or use the quick exit at any time.",
         WIN58, "end_win"),
        (59, s59_meta, s59_nodes, S59_START, "Two Buses to the Visit",
         "This scenario depicts a father whose visits with his daughter in foster care are moved to a center across the county: bus journeys, shortened visits, visit notes, and a review hearing. There is no graphic content. Players may skip any scene or use the quick exit at any time.",
         WIN59, "end_win"),
    ]
    for num, meta, nodes, start, title_line, note, winmap, win_end in jobs:
        scen = build(meta, nodes, start)
        emit(scen, num, title_line, note, start)
        path, end_cash = walk(scen, winmap, win_end)
        print(f"scenario-{num}: emitted nodes={len(scen['nodes'])} "
              f"walk={' -> '.join(path)} visited={len(path)} "
              f"endCash={end_cash} of {meta['startCash']}")
