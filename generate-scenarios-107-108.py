#!/usr/bin/env python3
"""Generator for Scenarios 107-108 of 'The First 90 Days' (Foundation tier).
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
# SCENARIO 107 — The Card That Stopped
# Kinship placement predates the story by three weeks. The child does
# not move in this story; what moves is paper between two systems.
# =====================================================================
S107_START = date(2026, 4, 6)
d107 = lambda off: datestr(S107_START, off)

s107_nodes = [
N("start", 0, "A Full Cart, a Dead Card", [
 "Your name is Camille. Your daughter Zora is seven, and three weeks ago \u2014 on " + d107(-21) + " \u2014 she went to stay with her aunt, in kinship care, while this case runs. The placement is not what this story is about. The grocery store is.",
 "You moved in January, and before the move was a week old you told your caseworker the new address \u2014 on " + d107(-70) + " \u2014 and she wrote it down while you watched. As far as you knew, the system had it. Systems, plural, is a distinction you are about to pay tuition on.",
 "Tonight the cart is full, the line behind you is patient in the way lines are not, and the cashier says it gently: your benefits card has been declined. Not short. Not partial. Declined \u2014 as if the household it feeds had been switched off.",
], [C("Leave the cart, keep the receipt slip, and call the number on the back of the card in the morning", "call_maze",
      note="The slip says only that the card was declined. Slips are terse. The reason, when you find it, will be a sentence about a letter you never saw.")]),

N("call_maze", 2, "The Number on the Back of the Card", [
 "You call on " + d107(2) + ", and the call-center maze does what mazes do: menus, music, a hold long enough to fold laundry inside \u2014 and finally a person, reading a screen you cannot see.",
 "The screen says your case was closed for failure to respond. A closure notice was mailed, the voice says, asking for a response by the date printed on its face. No response came back, so the case closed. The voice is not unkind. The voice also cannot tell you, at first, where the notice was mailed.",
 "You never saw a notice. You say so \u2014 and the voice, to its credit, goes looking for the address the notice was sent to.",
], [C("Stay on the line until the voice reads you the exact address the notice was mailed to", "two_systems",
      addHidden=["Closure \u2014 recorded as failure to respond to a mailed closure notice"],
      note="Exact addresses matter more than explanations. This one is about to explain everything, including why you never had a chance to respond.")]),

N("two_systems", 4, "The Old Address, Read Aloud", [
 "The address the voice reads on " + d107(4) + " is your previous address \u2014 the apartment you left in January. The notice went there, waited there, and was waited on there: the response the office was expecting was being expected at a home you no longer live in.",
 "You gave the new address to your caseworker on " + d107(-70) + ", and she wrote it in the case file while you watched \u2014 the file entry is dated " + d107(-56) + ". But the case file and the benefits office are two systems, and an address handed to one of them is not, automatically, an address held by the other. Nobody told you that. It is the most important sentence in this story, and it was never said to you at all.",
 "Tonight the correction can travel the way the news has travelled so far \u2014 by phone, from voice to voice \u2014 or it can travel on paper, to both systems, with dates on it.",
], [C("Correct the address in writing to BOTH offices, ask in writing for the notice to be re-sent, and attach a dated written statement of the facts", "written_moves",
      setFlags=["addressCorrected"], cash=-4,
      addHidden=["Address \u2014 corrected in writing to both the benefits office and the agency; re-send of the notice requested in writing"],
      note="Four dollars of copies and postage across two envelopes. The statement is six lines long: moved in January; new address given on the date you gave it; notice never received; card declined at the checkout. Dated, signed, copied."),
    C("Call both offices and correct the address out loud \u2014 faster, and both of them sounded helpful", "phone_only",
      note="Faster is real. Both voices were helpful. What neither voice can give you is a copy of the correction with a date on it.")]),

N("written_moves", 7, "Two Envelopes", [
 "By " + d107(7) + " both envelopes are in the mail and a copy of each is in your folder: the address correction, sent to the benefits office and to the agency; the written request that the closure notice be re-sent to the address you actually live at; and your statement of the facts, with its dates in order.",
 "Written things answer back in writing, slowly. The benefits office replies with a letter confirming the new address now stands on its file. The agency confirms the same. Two systems, one address \u2014 and, for the first time, dated paper in both places saying so.",
 "What neither reply does, by itself, is reopen anything. The closure still stands on its own paper: failure to respond. Paper answers paper. You are going to need the rest of the file.",
], [C("Keep both confirmations with the statement, and get through the weeks ahead", "waiting_weeks",
      addHidden=["Address confirmations \u2014 both offices confirmed the corrected address in writing"],
      note="Your folder now holds the correction twice over, once from each system. The closure letter's version of you is still the only version the benefits file leads with.")]),

N("phone_only", 7, "Corrected, Out Loud", [
 "Both calls go well. The benefits worker is brisk and kind: she updates the address as you speak it, or says she does, and tells you the closure can be looked at. Your caseworker says she has had the new address all along \u2014 which is true, in her system \u2014 and that she will pass it along.",
 "At the end of the day your address is corrected in the world of voices. In the world of paper, nothing you can hold has changed: no confirmation, no dated statement, no copy of anything. If the closure is ever argued about in a room, the argument will be your memory of two pleasant calls against a file that says failure to respond.",
], [C("Get through the weeks ahead on careful shopping, and keep calling to check", "waiting_weeks",
      note="Checking by phone produces more phone calls. Each one feels like progress. None of them can be attached to anything.")]),

N("waiting_weeks", 10, "The Weeks the Card Stayed Dead", [
 "The weeks are arithmetic now: smaller carts, careful lists, help you did not want to need. Zora's aunt covers what Zora needs at her house. What has stopped is the household support for the part of the household still at home with you \u2014 and it has stopped over a letter sent to an empty apartment.",
 "A scored assessment form is part of cases like yours \u2014 filled in from visits and notes, rating what it can see. What it can see this month is a household under strain. Why the strain arrived \u2014 a notice, an old address, two systems that do not share one \u2014 is not a box on the form. It is a fact living in two envelopes, or in two phone calls, or nowhere.",
], [C("At the next home visit, ask what the file currently says about the address and the closure", "flyer_beat",
      note="Your caseworker checks and tells you, honestly: her file has had the new address since the entry you watched her make. It is the other file you have never seen.")]),

N("flyer_beat", 14, "The Flyer in the Folder", [
 "In the waiting room at the agency office there is a folder of flyers for parents, and one of them \u2014 the kind of paper most people walk past \u2014 says something you read twice: a parent may request their case record, and under 55 Pa. Code \u00a7 3130.44(d) the material \u201cshall be released upon request.\u201d",
 "Your record. The address pages, the chronology, the notes \u2014 including the entry you watched your caseworker make in January, with its date on it. The flyer is not offering you a rescue. It is offering you the other system's own handwriting.",
], [C("Take the flyer home and think about what the case file's address pages would show", "records_fork",
      note="If the entry is dated the way you remember, the file itself \u2014 not your memory of it \u2014 can say when the system first held your new address.")]),

N("records_fork", 16, "Ask for the File, or Don\u2019t", [
 "The request is simple and it is yours to make: ask, in writing, for your case record \u2014 the chronology, the address entries, and the notes about the placement and the household. Under 55 Pa. Code \u00a7 3130.44(d), the record is to be released on request; the asking is a right, not a favor, and it leaves a date behind.",
 "Or you can wait for the meeting the closure will eventually get, and explain the two systems there, out loud, to people reading a file you have never seen.",
], [C("Put the request in writing \u2014 chronology and address entries \u2014 and keep a copy", "packet_arrives",
      setFlags=["recordsRequested"], cash=-3,
      note="Three dollars of copies and postage across the errand. The request is dated, copied, and kept with the confirmations."),
    C("Wait for the meeting \u2014 you can explain the two systems in person", "no_packet",
      note="In person is how the address travelled the first time: told to a person, written in one file, lost between systems. The explanation deserves a better vehicle this time.")]),

N("packet_arrives", 21, "The File\u2019s Own Hand", [
 "The packet arrives, and you turn to the address pages first, the way you would check a signature. There it is, in the case file's own entries: your new address, recorded on " + d107(-56) + " \u2014 entered from the conversation of " + d107(-70) + ", before Zora's placement, long before the card stopped.",
 "The system's own paper proves the sequence. The address was given, and written down, in the agency's file, in good time. The benefits office never got it, and mailed the one letter that mattered to the apartment you had left. The closure for failure to respond was built on a response being waited for at the wrong home.",
 "Now you have seen both files' versions of you. The question is what paper will be sitting on the table when the two versions are finally in one room.",
], [C("Keep the packet with the statement and the confirmations \u2014 they belong in the same folder, in date order", "closure_stands",
      addHidden=["Case file packet \u2014 agency file shows the new address recorded weeks before the closure"],
      note="Statement, two confirmations, and the file's own dated entry. Your folder and the closure letter now disagree about the same spring, in writing, with dates.")]),

N("no_packet", 21, "What You Cannot Quote", [
 "Without the packet, you cannot quote the entry you watched being made \u2014 its exact wording, its exact date \u2014 and you cannot show the meeting a page from the system's own file. You remember the conversation clearly. Memory, unattached, is the currency this case has already devalued once.",
 "Your account is true, detailed, and sincere. At the meeting, it will be weighed the way spoken accounts are weighed in rooms that run on attachments: personally, politely, and against a printed closure letter that says less and therefore somehow says it louder.",
], [C("Go on toward the meeting with your account \u2014 and keep every confirmation you do have", "closure_stands",
      note="Whatever paper exists still exists. The meeting is weeks away, and weeks are where sentences harden.")]),

N("closure_stands", 35, "Failure to Respond", [
 "On " + d107(35) + " a letter reaches you \u2014 at the new address, a small irony the file does not comment on. A meeting is set to review the closure, and the letter summarises the closure the way the file holds it: notice mailed, no response received, case closed for failure to respond.",
 "\u201cFailure to respond.\u201d You responded in January, to the person the system sent you, in the room where you were told to tell things. The sentence in the file does not know that, because the sentence was written inside the system that never got the address.",
 "Meetings read letters like this one first. Whether this one stays the whole story depends on what gets assembled before it is read.",
], [C("Ask your lawyer to go through your folder with you before the meeting", "prep",
      note="Preparation, in this system, is mostly deciding what paper will be on the table \u2014 and in what order it will be read.")]),

N("prep", 38, "One Page, or a Story", [
 "Your folder holds the whole spring, if you wrote it down: the dated statement, both offices' written confirmations, and \u2014 if you requested it \u2014 the packet whose address entry is dated " + d107(-56) + ". Assembled in order, they fit on one page: address given; address recorded in the case file; card declined; closure notice traced to the old address; correction sent to both systems in writing; file's own entry produced.",
 "Or the spring can stay where parts of it have lived so far \u2014 in your head, in order, in a story you can tell well. Stories are true. Pages are portable. Meetings are rooms you speak in for minutes and files speak in forever.",
], [C("Build the one-page chronology from the statement, the confirmations, and the file's own entry, in date order", "chronology_built",
      setFlags=["paperAssembled"],
      addHidden=["Chronology \u2014 one-page dated chronology built from the statement, the confirmations, and the case file entry"],
      note="One page. Every line dated. Nothing on it that the system's own paper does not support."),
    C("Go in with the story in your head \u2014 you lived it, in order", "story_only",
      note="You did, and you can tell it. The closure letter can also be told \u2014 by the file, to every reader, whether you are in the room or not.")]),

N("chronology_built", 40, "The Chronology, Assembled", [
 "The page reads like a timetable, because it is one. New address given to the caseworker, " + d107(-70) + ". The address recorded in the case file, " + d107(-56) + ". Zora's kinship placement, " + d107(-21) + ". The card declined, " + d107(0) + ". The correction and statement sent in writing to both systems, " + d107(7) + ". The case file packet received, " + d107(21) + ", its entry saying what it says.",
 "Six lines, no adjectives. Your lawyer's word for a page like this is \u201cquiet.\u201d Quiet pages get read carefully, because there is nothing in them to argue with except their dates.",
], [C("Make copies \u2014 one for the meeting, one for your lawyer, one for the folder", "meeting_eve",
      note="Copies are how a page attends meetings you are not invited to. This one is about to attend the most important one.")]),

N("story_only", 40, "The Story, Unwritten", [
 "Your account is clear, in order, and true: the move, the conversation in January, the checkout, the maze of menus, the old address read aloud. Sitting at the kitchen table you can tell it start to finish without a pause. It has only one flaw, and the flaw is not in the telling.",
 "It exists in exactly one place, and that place cannot be handed across a table, attached to a letter, or read after you leave the room. The file's version \u2014 \u201cfailure to respond\u201d \u2014 exists everywhere the file goes.",
], [C("Practice telling it once more, and set out the morning's things", "meeting_eve",
      note="The meeting will be short. Short rooms reward paper and punish nothing \u2014 they simply cannot hold what was never handed to them.")]),

N("meeting_eve", 43, "The Night Before the Meeting", [
 "The night before the meeting, your lawyer goes through your folder with you. You have one because the law provides for counsel in these cases, and for appointed counsel if a parent cannot afford one (42 Pa.C.S. \u00a7 6337) \u2014 she is the person whose job is to stand in the meeting room and make the paper speak in the right order.",
 "\u201cMeetings weigh the letter that closed the case against whatever answers it,\u201d she says. \u201cTomorrow we find out which record yours is weighed against \u2014 the closure's one line, or the closure's one line plus the system's own entry answering it.\u201d",
 "Zora is at her aunt's. The folder is by the door. The bus fare for the morning is in your coat.",
], [C("Take the folder and the fare, and go to the meeting", "meeting", cash=-6,
      note="Six dollars of fare. The folder weighs almost nothing. Both facts are misleading about their value tomorrow.")]),

N("meeting", 44, "The Meeting", [
 "The meeting is orderly and brief. The closure letter is read the way files are read: notice mailed, no response received, closed for failure to respond. The room begins, in the ordinary way, to treat the spring as a story about a mother who did not answer.",
 "Then your lawyer asks that the record be completed before the closure is weighed. What happens next depends, with a precision this scenario has been honest about from its first checkout, on what your choices actually put in her hands.",
], [C("Put the dated paper on the table \u2014 the statement, both address confirmations, and the case file's own address entry", "end_win",
      requiresFlags=["addressCorrected", "recordsRequested", "paperAssembled"],
      note="Six dated lines, one of them in the system's own hand. The room does the arithmetic itself, out loud, which is where arithmetic changes a record."),
    C("Present what paper you have \u2014 some of it, without the full set", "end_lose",
      note="Part of a chronology is an argument with missing premises. The closure letter, whole and printed, is sitting across the table."),
    C("Tell the spring as a story \u2014 the move, the checkout, the old address read aloud", "end_lose",
      note="Your voice is truthful and detailed. The file's voice is one line long and has already been read.")]),

N("end_win", 47, "Ending \u2014 Restored, Going Forward", [], ending=True, debrief=[
 "WHAT THE FILE HELD (the hidden record, revealed): A dated sequence authored largely by the system itself: your new address given on " + d107(-70) + " and recorded in the case file on " + d107(-56) + "; your written correction, your written request for the notice to be re-sent, and your dated statement, sent to both systems in the week of the decline; and both offices' written confirmations that the corrected address now stands on their files. At the meeting on " + d107(44) + ", the chronology was put beside the closure letter, and the room attributed the closure to the notice failure: the household's benefits for the members still at home were restored going forward, and the corrected address stands in writing in both systems. The assessment form rates what it can see; after this meeting, what it can see includes the reason.",
 "THE PROCESS UNDER THIS PATH (described, keeping to this scenario's verified law): The one legal instrument was the verified one. The case record was yours on written request \u2014 it \u201cshall be released upon request\u201d (55 Pa. Code \u00a7 3130.44(d)) \u2014 and requesting it is what let you show the file's own dated entry instead of describing a conversation. Counsel (42 Pa.C.S. \u00a7 6337) presented the chronology in the room where the closure was weighed. Everything else was generic process, deliberately without citation: correct an address in writing to every system that holds a version of you, ask in writing for the missed notice to be re-sent, and state the facts once, with dates, while they are new. No benefit rule is stated anywhere in this ending, because none was needed: the letters in this story stated their own instructions on their faces, and the paper answered the paper.",
 "THE HONEST PART: Label this win honestly \u2014 it is partial, and one part of it is deliberately not a win at all, because this scenario does not decide it. The card works going forward for the household members still at home; the strained weeks behind you are not repaid, Zora is still at her aunt's tonight, and the case is still open. And Zora's own portion while she is placed is a separate question, with its own papers and its own room, that this meeting did not take up and this scenario does not resolve \u2014 it is withheld here on purpose, not settled quietly in your favour. A different meeting might have noted the chronology and restored less, or later. Workers, meetings, and luck all held pieces of this. Your share was narrower and durable: when the system's letter went to the wrong home, you made the system's own file say so.",
]),
N("end_lose", 47, "Ending \u2014 Failure to Respond, As Filed", [], ending=True, debrief=[
 "WHAT THE FILE HELD (the hidden record, revealed): One letter and one phrase. The closure letter \u2014 notice mailed, no response received \u2014 and its phrase, \u201cfailure to respond,\u201d with nothing in the room explaining the spring between them: no dated statement both systems received, no written confirmations to set beside the letter, no case file entry quoted against the closure. At the meeting, your account was heard and, in the way of spoken accounts, believed personally and set aside professionally. The closure stands as written. The address, corrected out loud, may or may not survive the next worker, the next office, the next letter \u2014 because out loud is where it lives now.",
 "THE PROCESS UNDER THIS PATH (described, keeping to this scenario's verified law): The tools existed at every step and are modest ones. Correct the address in writing to both systems, so each correction has a date and a copy; ask in writing for the notice to be re-sent; state the facts once, in writing, with dates. Request the record, which \u201cshall be released upon request\u201d (55 Pa. Code \u00a7 3130.44(d)), so the file's own entry \u2014 your new address, recorded in January's conversation's wake, weeks before the decline \u2014 can be shown rather than remembered. And let counsel (42 Pa.C.S. \u00a7 6337) carry the assembled page into the room. None of that requires anyone to have acted in bad faith. It only requires paper \u2014 because the burden of explaining a notice failure quietly falls on the person the failure is written about, whether or not she ever saw the notice.",
 "THE HONEST PART: Let this debrief be as fair as the meeting was not: you did the human part of this correctly and early. You gave your new address to the worker the system sent you, promptly, in person, and watched her write it down. The letter that closed your case was mailed to a home you had already left, by a system you had never been told was a separate system. What was lost was not effort \u2014 it was evidence, and the two are different currencies in a file. A different office might have written the address failure into the closure itself; some do. This one did not, and outcomes here turn on workers, offices, and luck as much as on parents. The phrase in the file is not a verdict on you as a mother. It is a verdict on what was documented \u2014 and a folder started tonight, with the next letter, still changes what the next meeting reads.",
]),
]

s107_meta = {"title": "The First 90 Days",
 "subtitle": "Scenario 107 \u2014 The Card That Stopped (a fictional composite)",
 "startDateISO": "2026-04-06", "startNode": "start", "startCash": 150,
 "tier": "Foundation",
 "summary": "Three weeks after her daughter\u2019s kinship placement, a mother\u2019s benefits card declines \u2014 the closure notice went to the address she had already moved from, and only one of the two systems ever got the new one."}

# =====================================================================
# SCENARIO 108 — The Renewal That Went to the Daycare
# In-home case; the child is home throughout. The childcare arrangement
# and the parenting class are diegetic process: the form and the
# letters state their own instructions on their faces, and no program
# rule is stated as law anywhere in this scenario.
# =====================================================================
S108_START = date(2026, 6, 1)
d108 = lambda off: datestr(S108_START, off)

s108_nodes = [
N("start", 0, "The Form With Her Name On It", [
 "Your name is Kendra. Your son Cato is two, and he is home with you \u2014 this is an in-home case, under court supervision, and the plan's centrepiece, on Tuesdays, is a parenting class across town.",
 "The class does not admit toddlers \u2014 that is the class's own rule, printed on its sheet \u2014 so Tuesdays only work because Cato's childcare arrangement covers them. The same arrangement covers your work shifts. One arrangement, holding up both a job and a plan, the way one rope can hold two things and be cut once.",
 "The call comes on the morning of " + d108(0) + ", from Cato's daycare, and it is not about Cato. \u201cWe got a form with your name on it,\u201d the voice says. \u201cIt came in our mail. It looks important, and it has a date on it that already passed.\u201d",
], [C("Collect the form from the daycare tonight, and take Cato to drop-off in the morning as usual", "dropoff_lapse",
      note="Tonight you will read the form at your kitchen table. Its face is plain about itself. What it cannot tell you is what its weeks in the wrong mail tray have already done.")]),

N("dropoff_lapse", 1, "Turned Away at Drop-Off", [
 "The form's face is plain about itself, the way forms are: sign, date, and return it to the address printed at the top, by " + d108(-3) + ". It was mailed to the daycare instead of to you, it sat in the daycare's mail, and its printed date passed there. You sign it at the kitchen table on " + d108(0) + " \u2014 after the date on its face, through no door of yours.",
 "At drop-off on " + d108(1) + " \u2014 a Tuesday, class day \u2014 the lapse is discovered in the most ordinary way there is: at the desk, with Cato's bag on your shoulder. The arrangement has lapsed, the desk tells you, gently and finally; until the renewal is back in place, Cato cannot stay under it. You carry him back out into a Tuesday that has just lost its childcare and its class at the same desk, in the same minute.",
 "You miss the class. It is the first missed session in your file, and the file will record it in the file's grammar: missed. Not \u201cthe form went to the daycare.\u201d Missed.",
], [C("Call the childcare office from outside the daycare, with the signed form in your bag", "office_answers",
      addHidden=["Parenting class \u2014 session missed on the lapse day; the renewal form had been mailed to the daycare"],
      note="Calling from the pavement, with a toddler on your hip and a signed form three days past its printed date, is not how anyone plans to fix a filing. It is how filings get fixed.")]),

N("office_answers", 3, "It Went to the Daycare", [
 "Two days of menus and holds later, on " + d108(3) + ", a person at the childcare office can see the whole small disaster on her screen: the renewal form was mailed out, no return was received, and the arrangement lapsed. Where it was mailed to takes her a second screen to find. The daycare. It was mailed to the daycare.",
 "To restart it, she says, the signed form has to reach the office \u2014 the form itself says so, on its face, with the address printed at the top. She can note your call on the account. A note, in her words, in her system, is what a call becomes.",
 "Tonight the renewal can travel the way your account of it has travelled so far \u2014 spoken, noted by someone else \u2014 or it can travel filed, with a dated statement, copies kept, and its receipt confirmed in writing.",
], [C("File the renewal with a dated written statement of the facts, keep copies of everything, and ask the office to confirm receipt in writing", "written_filing",
      setFlags=["renewalFiled"], cash=-5,
      addHidden=["Renewal \u2014 filed with a dated written statement; copies kept; written confirmation of receipt requested"],
      note="Five dollars of fares and copies across the errand. The statement is short: form mailed to the daycare; found there after its printed date; lapse discovered at drop-off; class missed. Every line dated."),
    C("Post the form in the ordinary envelope and let the office's note of your call carry the explanation", "phone_only",
      note="The form will arrive either way. What will not arrive with it is any account, in your words with your dates, of why it is late.")]),

N("written_filing", 5, "Filed, With Copies", [
 "By " + d108(5) + " the packet is filed: the signed renewal, your dated statement, and your request that receipt be confirmed in writing. Copies of all of it are in your folder, because copies are the difference between filed and merely sent.",
 "The office's reply, when it comes, confirms receipt, and its letter states its own next steps on its face; you follow them the way you follow any letter \u2014 as this letter's instructions, for this case. The arrangement is not back yet. Tuesdays, meanwhile, keep arriving on schedule, indifferent to processing.",
], [C("Keep the confirmation with the statement, and face the next Tuesday", "second_tuesday",
      addHidden=["Office reply \u2014 renewal receipt confirmed in writing"],
      note="Receipt is not restoration. But for the first time in this story, a piece of the gap exists in the office's own writing, with your dates attached to it.")]),

N("phone_only", 5, "Posted, and Noted", [
 "The form goes in the ordinary post, alone: no statement with it, no copy in your folder, nothing in your handwriting anywhere in its envelope. Somewhere in the office's system there is a note of your call, in the call-taker's summary of your words, at the length call notes are kept.",
 "If the lateness of this renewal is ever argued about in a room, the argument will be that note and your memory against the file's tally of missed sessions. You have been in this case long enough to know which of those three things rooms believe.",
], [C("Face the next Tuesday, and keep the daycare's number close", "second_tuesday",
      note="The form is travelling. So is the tally. They are travelling toward the same review, and only one of them is counting.")]),

N("second_tuesday", 8, "The Second Tuesday", [
 d108(8) + " is the second Tuesday. The arrangement is still lapsed \u2014 the renewal, however it travelled, has not landed yet \u2014 and at drop-off the desk, apologetic and immovable, turns Cato away again. You miss the second class, standing in the same entryway, holding the same bag.",
 "In the file, the tally has now begun, in the file's own arithmetic: missed sessions, two. The tally counts sessions. It does not count causes, mail trays, or desks. A scored assessment form is part of cases like yours \u2014 filled in from notes like these, rating what it can see. What it can see this month is two empty Tuesdays.",
 "The daycare knows the exact shape of the gap \u2014 they watched it happen at their desk, twice, and the form that caused it arrived in their own mail. Their knowledge can become paper, or it can stay a memory at a desk that sees a hundred families.",
], [C("Ask the daycare in writing to confirm exactly which dates the lapse covered", "provider_written",
      setFlags=["lapseConfirmed"],
      addHidden=["Daycare \u2014 asked in writing to confirm the exact dates the lapse covered"],
      note="Dates, not impressions: which Tuesdays, what happened at the desk, and where the form arrived. Asked in writing, so the answer comes back in writing."),
    C("Ask at the desk and take their word for the dates \u2014 they were there, they know", "provider_verbal",
      note="They were, and they do. Knowledge at a desk is real knowledge. It is just not the kind that can be attached to a review packet.")]),

N("provider_written", 11, "The Dates, in Writing", [
 "The daycare's reply arrives by " + d108(11) + ", and it is short in the way strong documents are short. In writing, the daycare confirms that the arrangement's lapse covered exactly two class Tuesdays \u2014 " + d108(1) + " and " + d108(8) + " \u2014 that Cato was turned away at drop-off on both, and that the renewal form had arrived in the daycare's own mail.",
 "Your folder now holds a document authored by neither side of the argument the file is having with you: the desk that watched the lapse, dating it. It agrees with your statement about everything, because it is not agreeing with you \u2014 it is describing its own entryway.",
], [C("Keep the daycare's letter with the office confirmation, in date order", "flyer_beat",
      addHidden=["Daycare letter \u2014 lapse dates and the form's arrival in the daycare's mail confirmed in writing"],
      note="Two letters now, from two desks, neither of them yours, describing the same two Tuesdays. The tally in the file describes them too \u2014 in one word.")]),

N("provider_verbal", 11, "The Dates, Out Loud", [
 "The desk is happy to confirm it all out loud, and does, completely and accurately: the two Tuesdays, the turn-aways, the form in their mail tray. It is a full and truthful account, delivered in the entryway, to you, while Cato pulls at the door handle.",
 "Nothing is written down. Next month the desk will have new staff, or the same staff on a harder day, and the account will be a memory of a conversation in an entryway \u2014 true, warm, and impossible to attach to anything.",
], [C("Thank them, and go on with the month", "flyer_beat",
      note="Being believed at a desk feels like the problem being solved. Desks do not attend reviews. Paper does.")]),

N("flyer_beat", 14, "The Flyer in the Folder", [
 "In the waiting room at the agency office there is a folder of flyers for parents, and one of them \u2014 the kind of paper most people walk past \u2014 says something you read twice: a parent may request their case record, and under 55 Pa. Code \u00a7 3130.44(d) the material \u201cshall be released upon request.\u201d",
 "Your record. The class sign-in sheets, the progress notes, the tally in its original handwriting \u2014 the file's own version of your Tuesdays, which you have never seen. The flyer is not offering you a rescue. It is offering you the other side of the tally.",
], [C("Take the flyer home and think about what the sign-in sheet would show", "records_fork",
      note="You signed that sheet every Tuesday you were in the room. If it is in the record, the record knows exactly which Tuesdays you were not \u2014 and signatures have a way of raising the question of why.")]),

N("records_fork", 16, "Ask for the File, or Don\u2019t", [
 "The request is simple and it is yours to make: ask, in writing, for your case record \u2014 the parenting class sign-in sheets and the progress notes about attendance. Under 55 Pa. Code \u00a7 3130.44(d), the record is to be released on request; the asking is a right, not a favor, and it leaves a date behind.",
 "Or you can wait for the review and explain the mail tray there, out loud, to people reading a tally you have never seen.",
], [C("Put the request in writing \u2014 sign-in sheets and attendance notes \u2014 and keep a copy", "packet_arrives",
      setFlags=["recordsRequested"], cash=-3,
      note="Three dollars of copies and postage across the errand. The request is dated, copied, and kept with the letters."),
    C("Wait for the review \u2014 you can explain the daycare's mail in person", "no_packet",
      note="In person is how the desk confirmed the dates: accurately, warmly, and in a form that cannot be handed to anyone.")]),

N("packet_arrives", 21, "The Sign-In Sheet", [
 "The packet arrives, and two of its documents belong side by side, so you put them side by side. The first is the class sign-in sheet: your signature, in your hand, on every Tuesday the class met \u2014 except " + d108(1) + " and " + d108(8) + ", where your line is simply, eloquently, blank.",
 "The second is the progress note, and its whole account of the same month is a tally: \u201cmissed sessions: 2.\u201d No cause is recorded beside it \u2014 not the form, not the mail tray, not the desk. The system's own sheet proves which Tuesdays you missed and that you missed no others. The note, beside it, is what the review will quote.",
 "Now you have seen both documents the review will weigh. The question is what paper will be sitting between them.",
], [C("Keep the packet with the daycare's letter and the office confirmation, in date order", "tally_note",
      addHidden=["Class sign-in sheet \u2014 attendance on every class Tuesday except the two lapse Tuesdays, shown in the record"],
      note="Signatures, a tally, and a daycare's letter, all describing the same two blank lines \u2014 in three different grammars. Only one of the grammars mentions a cause.")]),

N("no_packet", 21, "What You Cannot Quote", [
 "Without the packet, you cannot see the tally's exact wording, and you cannot show anyone the sign-in sheet's eloquent blanks \u2014 every Tuesday signed except two. You know what the sheet would show. You know it in the way that cannot be attached to a report.",
 "Your account is true, detailed, and sincere. At the review, it will be weighed the way spoken accounts are weighed in rooms that run on attachments: personally, politely, and against a printed tally that says less and therefore somehow says it louder.",
], [C("Go on toward the review with your account \u2014 and keep every letter you do have", "tally_note",
      note="Whatever paper exists still exists. The review is weeks away, and weeks are where tallies harden.")]),

N("tally_note", 28, "Missed Sessions", [
 "By " + d108(28) + " the arrangement is back in place \u2014 the renewal landed, on its own schedule \u2014 and on " + d108(29) + " Cato stays at the daycare under it while you sit in the class and sign the sheet, in the row below the two blank lines.",
 "The tally, though, survives the fix. At the month's check-in you hear it read the way the file holds it: missed sessions, two \u2014 a compliance fact now, travelling without its cause toward a review that will read it exactly as written.",
 "Whether it arrives at that review still travelling alone depends on what gets assembled before the review sits.",
], [C("Ask when the review is, and how much time is left to prepare for it", "prep",
      note="Days, not weeks. Preparation, in this system, is mostly deciding what paper will be in the room.")]),

N("prep", 31, "One Page, or a Story", [
 "Your folder holds the whole gap, if you wrote it down: the dated statement, the office's confirmation, the daycare's letter with its two exact Tuesdays, and \u2014 if you requested it \u2014 the sign-in sheet with its two blank lines. Assembled in order, they fit on one page: the form's printed date passed in the daycare's mail; the form found; the lapse at drop-off; the renewal filed; the second Tuesday lost; the lapse confirmed in writing by the desk that watched it; the sheet signed again the week the arrangement returned.",
 "Or the gap can stay where it has partly lived so far \u2014 in your head, in order, in a story you can tell well. Stories are true. Pages are portable. Reviews are rooms you speak in for minutes and files speak in forever.",
], [C("Build the one-page timeline from the statement, the letters, and the sign-in sheet, in date order", "timeline_built",
      setFlags=["timelineBuilt"],
      addHidden=["Timeline \u2014 one-page dated timeline built from the statement, the daycare letter, and the sign-in sheet"],
      note="One page. Every line dated. Nothing on it that the system's own paper does not support."),
    C("Go in with the story in your head \u2014 you lived it, in order", "story_only",
      note="You did, and you can tell it. The tally in the file can also be told \u2014 by the file, to every reader, whether you are in the room or not.")]),

N("timeline_built", 33, "The Timeline, Assembled", [
 "The page reads like a timetable, because it is one. The renewal form's printed return date, " + d108(-3) + " \u2014 passed while the form sat in the daycare's mail. The form found, " + d108(0) + ". The lapse at drop-off and the first missed class, " + d108(1) + ". The renewal filed with its statement, " + d108(5) + ". The second missed class, " + d108(8) + ". The daycare's written confirmation, " + d108(11) + ". The sign-in sheet, obtained " + d108(21) + ", blank on exactly those two Tuesdays and signed on every other.",
 "Seven lines, no adjectives. Your lawyer's word for a page like this is \u201cquiet.\u201d Quiet pages get read carefully, because there is nothing in them to argue with except their dates.",
], [C("Make copies \u2014 one for the review, one for your lawyer, one for the folder", "review_eve",
      note="Copies are how a page attends meetings you are not invited to. This one is about to attend the most important one.")]),

N("story_only", 33, "The Story, Unwritten", [
 "Your account is clear, in order, and true: the phone call, the form in the wrong mail, the desk, the bag on your shoulder, the second Tuesday in the same entryway. Sitting at the kitchen table you can tell it start to finish without a pause. It has only one flaw, and the flaw is not in the telling.",
 "It exists in exactly one place, and that place cannot be handed to a reviewer, attached to a report, or read after you leave the room. The file's version \u2014 \u201cmissed sessions: 2\u201d \u2014 exists everywhere the file goes.",
], [C("Practice telling it once more, and get Cato settled for the morning", "review_eve",
      note="The review will be short. Short rooms reward paper and punish nothing \u2014 they simply cannot hold what was never handed to them.")]),

N("review_eve", 35, "The Night Before the Review", [
 "The night before the review, your lawyer goes through your folder with you. You have one because the law provides for counsel in these cases, and for appointed counsel if a parent cannot afford one (42 Pa.C.S. \u00a7 6337) \u2014 she is the person whose job is to stand in the review room and make the paper speak in the right order.",
 "\u201cReviews measure the plan against the record,\u201d she says. \u201cTomorrow we find out which record yours is measured against \u2014 the tally's two words, or the tally plus everything that explains it.\u201d",
 "Cato is asleep. The folder is by the door. The bus fare for the morning is in your coat.",
], [C("Take the folder and the fare, and go to the review", "review", cash=-6,
      note="Six dollars of fare. Tomorrow is a Tuesday \u2014 class day \u2014 and for once the folder, not the toddler, is what you have to get across town.")]),

N("review", 36, "The Review", [
 "The review sits on " + d108(36) + " \u2014 a Tuesday, with Cato covered at the daycare under the restored arrangement, in the class's own hours. The plan is read line by line. On the attendance line, the progress note is quoted \u2014 \u201cmissed sessions: 2\u201d \u2014 and the room begins, in the ordinary way, to treat the two Tuesdays as a fact about you.",
 "Then your lawyer asks that the record be completed before the line is weighed. What happens next depends, with a precision this scenario has been honest about from its first phone call, on what your choices actually put in her hands.",
], [C("Present the one-page timeline \u2014 the dated statement, the daycare's written confirmation, and the sign-in sheet attached", "end_win",
      requiresFlags=["renewalFiled", "lapseConfirmed", "recordsRequested", "timelineBuilt"],
      note="Seven dated lines, three of them written by the system's own desks. The room does the arithmetic itself, out loud, which is where arithmetic changes a record."),
    C("Present what paper you have \u2014 some of it, without the full set", "end_lose",
      note="Part of a timeline is an argument with missing premises. The tally, whole and printed, is sitting across the table."),
    C("Tell the two Tuesdays as a story \u2014 the call, the form, the desk", "end_lose",
      note="Your voice is truthful and detailed. The file's voice is two words long and has already been read.")]),

N("end_win", 39, "Ending \u2014 Attributed, On the Record", [], ending=True, debrief=[
 "WHAT THE FILE HELD (the hidden record, revealed): A dated account of the gap, authored largely by the system's own desks: your statement filed with the renewal, the childcare office's written confirmation of receipt, the daycare's written confirmation that the lapse covered exactly " + d108(1) + " and " + d108(8) + " and that the renewal form had arrived in the daycare's own mail, and the class sign-in sheet \u2014 signed every Tuesday except those two. At the review on " + d108(36) + ", the one-page timeline was put beside the tally, and the room attributed the two missed sessions on the record to the paperwork gap: the tally was corrected to carry its cause, the renewal stands filed, and the class was extended by two sessions so the missed ones can be made up. The assessment form rates what it can see; after this review, what it can see includes a form that went to the wrong address.",
 "THE PROCESS UNDER THIS PATH (described, keeping to this scenario's verified law): The one legal instrument was the verified one. The case record was yours on written request \u2014 it \u201cshall be released upon request\u201d (55 Pa. Code \u00a7 3130.44(d)) \u2014 and requesting it is what let you show the sign-in sheet's two blank lines instead of arguing against a summary of them. Counsel (42 Pa.C.S. \u00a7 6337) presented the timeline in the room where the plan is measured against the record. Everything else was generic process, deliberately without citation, and no program rule is stated anywhere in this ending, because none was needed: the renewal form and the office's letters stated their own instructions on their faces, and the story turned on where the form was mailed, what the desks confirmed in writing, and what the sheet showed. Reviews can only weigh paper that exists in time to be weighed.",
 "THE HONEST PART: Label this win honestly \u2014 it is partial. The two sessions are made up ahead of you, not behind you: the class continues, now two sessions longer, with all the ordinary difficulty of Tuesdays. The case is still open, Cato is home as he has been throughout, and the supervision continues. The two lost Tuesdays themselves \u2014 the entryway, the bag, the walk back out \u2014 are not returned by any correction. A different reviewer might have noted the timeline and kept the tally's wording anyway, and a daycare that had thrown the form away would have left you with nothing to confirm. Workers, desks, reviewers, and luck all held pieces of this. Your share was narrower and durable: when the system's form went to the wrong building, you made the system's own desks sign for where it went.",
]),
N("end_lose", 39, "Ending \u2014 Missed, As Tallied", [], ending=True, debrief=[
 "WHAT THE FILE HELD (the hidden record, revealed): Two words and a number. The progress note's tally \u2014 \u201cmissed sessions: 2\u201d \u2014 with nothing in the record explaining the two Tuesdays behind it: no dated statement filed with the renewal, no daycare letter fixing the lapse's dates, no sign-in sheet quoted against the note. At the review, your account was heard and, in the way of spoken accounts, believed personally and set aside professionally. The renewal is in place now and Tuesdays are covered again. The tally stays in the file as written \u2014 two unexplained misses, available to every future reader, in a case where the renewal form spent its deadline in a daycare's mail tray.",
 "THE PROCESS UNDER THIS PATH (described, keeping to this scenario's verified law): The tools existed at every step and are modest ones. File the renewal with a dated written statement, so the filing carries its own explanation; ask the provider, in writing, to confirm exactly which dates the lapse covered, so the gap's shape is fixed by the desk that watched it; request the record, which \u201cshall be released upon request\u201d (55 Pa. Code \u00a7 3130.44(d)), so the sign-in sheet's blanks can be shown rather than described; and let counsel (42 Pa.C.S. \u00a7 6337) carry the assembled page into the room. No program rule needed stating for any of that: the form and the letters carried their own instructions on their faces. What was missing was never permission. It was paper.",
 "THE HONEST PART: Let this debrief be as fair as the review was not: you did the human part of this correctly and promptly. You collected the form the day the daycare found it, signed it that night, and stood at the desk on both Tuesdays ready to comply with a plan whose paperwork had gone to another building. What was lost was not effort \u2014 it was evidence, and the two are different currencies in a file. A different provider might have written the mailing failure into the note itself; some do. This file did not, and outcomes here turn on workers, desks, and luck as much as on parents. The tally in the file is not a verdict on you as a mother. It is a verdict on what was documented \u2014 and a folder started tonight, with the next letter, still changes what the next review reads.",
]),
]

s108_meta = {"title": "The First 90 Days",
 "subtitle": "Scenario 108 \u2014 The Renewal That Went to the Daycare (a fictional composite)",
 "startDateISO": "2026-06-01", "startNode": "start", "startCash": 150,
 "tier": "Foundation",
 "summary": "A childcare renewal form is mailed to the daycare instead of to her \u2014 the arrangement lapses, two Tuesday parenting classes are missed, and the file tallies them as hers."}

# =====================================================================
# BUILD, EMIT, WALK
# =====================================================================
WIN107 = {
 "start": "Leave the cart, keep the receipt slip, and call the number on the back of the card in the morning",
 "call_maze": "Stay on the line until the voice reads you the exact address the notice was mailed to",
 "two_systems": "Correct the address in writing to BOTH offices, ask in writing for the notice to be re-sent, and attach a dated written statement of the facts",
 "written_moves": "Keep both confirmations with the statement, and get through the weeks ahead",
 "waiting_weeks": "At the next home visit, ask what the file currently says about the address and the closure",
 "flyer_beat": "Take the flyer home and think about what the case file's address pages would show",
 "records_fork": "Put the request in writing \u2014 chronology and address entries \u2014 and keep a copy",
 "packet_arrives": "Keep the packet with the statement and the confirmations \u2014 they belong in the same folder, in date order",
 "closure_stands": "Ask your lawyer to go through your folder with you before the meeting",
 "prep": "Build the one-page chronology from the statement, the confirmations, and the file's own entry, in date order",
 "chronology_built": "Make copies \u2014 one for the meeting, one for your lawyer, one for the folder",
 "meeting_eve": "Take the folder and the fare, and go to the meeting",
 "meeting": "Put the dated paper on the table \u2014 the statement, both address confirmations, and the case file's own address entry",
}
WIN108 = {
 "start": "Collect the form from the daycare tonight, and take Cato to drop-off in the morning as usual",
 "dropoff_lapse": "Call the childcare office from outside the daycare, with the signed form in your bag",
 "office_answers": "File the renewal with a dated written statement of the facts, keep copies of everything, and ask the office to confirm receipt in writing",
 "written_filing": "Keep the confirmation with the statement, and face the next Tuesday",
 "second_tuesday": "Ask the daycare in writing to confirm exactly which dates the lapse covered",
 "provider_written": "Keep the daycare's letter with the office confirmation, in date order",
 "flyer_beat": "Take the flyer home and think about what the sign-in sheet would show",
 "records_fork": "Put the request in writing \u2014 sign-in sheets and attendance notes \u2014 and keep a copy",
 "packet_arrives": "Keep the packet with the daycare's letter and the office confirmation, in date order",
 "tally_note": "Ask when the review is, and how much time is left to prepare for it",
 "prep": "Build the one-page timeline from the statement, the letters, and the sign-in sheet, in date order",
 "timeline_built": "Make copies \u2014 one for the review, one for your lawyer, one for the folder",
 "review_eve": "Take the folder and the fare, and go to the review",
 "review": "Present the one-page timeline \u2014 the dated statement, the daycare's written confirmation, and the sign-in sheet attached",
}

if __name__ == "__main__":
    jobs = [
        (107, s107_meta, s107_nodes, S107_START, "The Card That Stopped",
         "This scenario depicts a mother whose daughter is in kinship care with an aunt (a placement that predates the story): a benefits card that declines at a checkout, a closure notice mailed to a previous address, call centers, written corrections, a case-record request, and a meeting, told through calls, letters, and file pages. There is no graphic content. Players may skip any scene or use the quick exit at any time.",
         WIN107, "end_win"),
        (108, s108_meta, s108_nodes, S108_START, "The Renewal That Went to the Daycare",
         "This scenario depicts an in-home case under court supervision: a childcare renewal form mailed to the daycare instead of to the mother, a lapsed arrangement, two missed Tuesday parenting classes, progress notes, and a review hearing, told through forms, letters, and sign-in sheets. There is no graphic content. Players may skip any scene or use the quick exit at any time.",
         WIN108, "end_win"),
    ]
    for num, meta, nodes, start, title_line, note, winmap, win_end in jobs:
        scen = build(meta, nodes, start)
        emit(scen, num, title_line, note, start)
        path, end_cash = walk(scen, winmap, win_end)
        print(f"scenario-{num}: emitted nodes={len(scen['nodes'])} "
              f"walk={' -> '.join(path)} visited={len(path)} "
              f"endCash={end_cash} of {meta['startCash']}")
