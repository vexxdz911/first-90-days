#!/usr/bin/env python3
"""Generator for Scenarios 112-113 of 'The First 90 Days' (Complex tier).
Wave 2, Batch 8, Part C. One data source emits both the .json and the
-script.md for each scenario, so they match node-for-node by construction.
Every kicker and every in-body date is computed from startDateISO +
dayOffset via datestr()/fmt(); no date is hand-typed in the scenario data.
ASFA arithmetic: each scenario's foster-entry date is a date object and
the 15-month date is computed by calendar-month addition and asserted.
S112: children placed with Bernice Monday, October 20, 2025;
      +15 months = Wednesday, January 20, 2027 (outside the playable
      window; no ASFA node arises in S112 and none is depicted).
S113: Umar placed Monday, March 3, 2025; +15 months =
      Wednesday, June 3, 2026 = dayOffset 61 from the story start
      (Friday, April 3, 2026); the filing-day node sits exactly there.
"""
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
             "choice \u2014 the player does not see it when it happens. `REQUIRES FLAG: name` means the choice "
             "is only available if that flag was set earlier; `REQUIRES NO FLAG: name` means it is only "
             "available if that flag was never set. `NOTE:` is text shown to the player right after choosing.")
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

def walk(scen, win_choices, win_ending):
    by = {n["id"]: n for n in scen["nodes"]}
    flags, cash = set(), scen["meta"]["startCash"]
    path, cur = [], scen["meta"]["startNode"]
    while True:
        path.append(cur)
        node = by[cur]
        if node.get("ending"):
            assert cur == win_ending, (cur, win_ending)
            assert "recordsRequested" in flags, ("win route lacks recordsRequested", sorted(flags))
            return path, cash, sorted(flags)
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
# SCENARIO 112 — The Empty Months
# Children placed with Bernice (kinship): Monday, October 20, 2025.
# Approval packet submitted: Friday, October 24, 2025 (entry + 4 days).
# ASFA 15-month date: Wednesday, January 20, 2027 — computed, asserted,
# and deliberately NOT depicted (it falls far outside this story).
# Story opens: Monday, January 12, 2026.
# =====================================================================
S112_START = date(2026, 1, 12)
S112_ENTRY = date(2025, 10, 20)
S112_PACKET = S112_ENTRY + timedelta(days=4)
S112_ASFA = add_months(S112_ENTRY, 15)
assert S112_START.strftime("%A") == "Monday"
assert S112_ENTRY.strftime("%A") == "Monday", S112_ENTRY
assert S112_PACKET == date(2025, 10, 24) and S112_PACKET.strftime("%A") == "Friday"
assert S112_ASFA == date(2027, 1, 20) and S112_ASFA.strftime("%A") == "Wednesday", S112_ASFA

def d112(off):
    return fmt(S112_START + timedelta(days=off))

s112_nodes = [
N("start", 0, "Two Children, One Kitchen Table", [
 "Your name is Bernice. You are sixty-four, retired from thirty-one years of school kitchens, and since " + fmt(S112_ENTRY) + " your house has held two more people: your grandchildren, Joaquin, who is eight, and Mireya, who is four. They came to you as a kinship placement when their mother — your daughter, Dena — entered the part of her case that could not be done with children in the house. The children are Dena's case. The beds, the lunches, the nightmares at two in the morning: those are yours.",
 "In the first week you did the caregiver paperwork the way you have done every form since 1987: completely, in ink, with copies. You submitted your approval packet on " + fmt(S112_PACKET) + " and kept the stamped copies in a folder on the kitchen table. The payments that were supposed to follow the packet have not followed. The answer, every time you ask, is the same two words: in process.",
 "Your savings were not large. They were, however, yours — and for almost three months they have been quietly doing the job the missing payments were supposed to do. This story is about those empty months, and about what a file does with a grandmother who is running out of money keeping two children fed.",
], [C("Open the folder on the kitchen table — the one with the stamped copies", "folder_copies",
      note="The folder is the first character in this story after you. It will be in more rooms than you will.")]),

N("folder_copies", 2, "The Stamped Copies", [
 "The folder holds your whole half of the paperwork: the approval packet's stamped copy, dated " + fmt(S112_PACKET) + "; the home-study notes; the children's school and clinic papers; a call log you started in November, in pencil, because a woman at the senior center told you that in this system a date you cannot show is a date that did not happen.",
 "Nothing in the folder is dramatic. That is its power. Stamps, dates, initials — the small change of a case, kept by the one person in it who was never issued a file cabinet.",
 "What the folder does not hold is any explanation of the missing payments. Explanations, so far, have all been spoken.",
], [C("Call the agency and ask, again, where the payments are", "payment_call1",
      note="You write the date of the call at the top of a fresh page before you dial. Habits are strategies that have stopped introducing themselves.")]),

N("payment_call1", 5, "In Process, Again", [
 "The call on " + d112(5) + " goes the way the December calls went. The worker who answers is polite. The packet is in process. Processing takes time. There is nothing you need to do — that sentence, again — and nothing she can tell you about when it will finish.",
 "You ask whether anything is missing from the packet. Nothing is missing, she says. You ask whether anything needs a signature. Not yours, she says — which is true, and is also, though neither of you knows it yet, the most precise sentence anyone will say about this case for weeks.",
 "You write it all in the log: the date, the words, the name of the person who said them. The log is getting long. Long logs are either a burden or an exhibit, depending on whether anyone ever has to read one.",
], [C("Thank her, hang up, and do the week's grocery math at the table", "grocery_math",
      addHidden=["Call log — payment inquiry; agency answer: packet in process, nothing missing, no signature of caregiver's needed"],
      note="The math is next. Math, in this house, is also a document.")]),

N("grocery_math", 9, "The Grocery Math", [
 "Two children eat the way weather happens: constantly, and without consulting anyone. The week's groceries, the school lunch account, Mireya's clinic co-pay, Joaquin's outgrown shoes — the list on the refrigerator is ordinary, and the total is not, and the difference between those two facts is coming out of an account that was supposed to be for your old age.",
 "You are not careless with money. You are careful with money in a house whose income stopped matching its size in October, for reasons that live in a folder marked in process.",
 "A neighbor asks how the agency lets this happen. You tell her the truth: nobody has let anything happen, visibly. That is the problem. Invisible things do not get fixed; they get described — later, by other people, in other words.",
], [C("Pay for the week's groceries and the shoes, and write the total in the log", "dena_sunday", cash=-24,
      note="Twenty-four dollars this round, and not the last round. The log gains a column it never wanted.")]),

N("dena_sunday", 13, "Dena, on Sunday", [
 "Dena visits on Sundays, at your table, in the part of the week that still belongs to the family instead of the case. She is doing the work her plan asks of her — the counselor's reports say so, in their careful language — and the children treat her arrival the way they treat weather clearing.",
 "She asks about the money. You tell her some of it: the payments are still in process; the savings are holding. She hears the part you did not say, the way daughters do. \u201cMom. If this gets bad because of paperwork\u2014\u201d",
 "\u201cThen we will fix the paperwork,\u201d you say, with more confidence than the folder currently justifies. It is the truest sentence available. It is also a promise, and promises, in this family, get logged too.",
], [C("Walk her to the bus, and come home to the week's ordinary work", "letter_in_process",
      note="Ordinary work: lunches, laundry, a form for Joaquin's school that asks for a guardian signature you can actually give.")]),

N("letter_in_process", 16, "The Letter That Says Nothing, in Writing", [
 "A letter arrives from the agency, and for one envelope's width your heart does the thing it has learned to do. Inside: a single page confirming that your caregiver approval remains in process and that payments will commence upon approval. It is dated " + d112(16) + ". It does not say what is being processed, or by whom, or what remains to happen.",
 "You file it behind the stamped packet copy, where it belongs: the agency's own words, in writing, saying that in the third month of two children living in your house, the paper that pays for their care had still not finished moving.",
 "Letters like this are not answers. They are timestamps with letterhead. Timestamps, assembled later, become chronologies — and chronologies are the one language every room in this system reads.",
], [C("File the letter, and get ready for the home visit this week", "home_visit",
      addHidden=["Agency letter — approval still in process in the third month of placement; payments to commence upon approval"],
      note="Stamped copy, meet letter. The folder is becoming a conversation the agency does not know it is having.")]),

N("home_visit", 18, "The Visit That Goes Fine", [
 "The home visit goes fine, because your home is fine. The worker — the first one, Ms. Larkin, who has carried the case since October — walks the rooms, compliments Mireya's drawing taped to the refrigerator, confirms the children are settled, in school, in routine.",
 "She asks how you are managing. You say what grandmothers say: we manage. She writes something down. What she writes, you will not see for weeks — and when you do see it, the gap between we manage and what the note made of it will be one of this story's lessons.",
 "Nothing about the visit is wrong. That is worth saying plainly, because what happens later does not require anyone to have been wrong in this room. It only requires a file that keeps summaries and loses causes.",
], [C("See her out, and help Joaquin with the homework he has been avoiding", "worker_goodbye",
      note="Fractions. He is better at them than he believes. So, it turns out, are you — the household kind.")]),

N("worker_goodbye", 21, "A Goodbye in the Hallway", [
 "Ms. Larkin is leaving the agency — a new job, a shorter commute, the ordinary weather of other people's lives. She tells you at the door, kindly, and says the case will transfer and the new worker will have the file.",
 "The file. Everything the new worker will know about Joaquin, Mireya, Dena, and you will arrive as paper: reports, notes, summaries — and somewhere in it, an approval packet that has been in process since " + fmt(S112_PACKET) + ".",
 "Worker changes are not anyone's fault. They are, however, resets: whatever the departing worker knew in her head — and she knew the payments were late, because you told her monthly — leaves with her head. What stays is what the paper says.",
], [C("Thank her, wish her well, and write the transfer in the log", "new_worker",
      note="One line in the log: worker changed. Underneath it, everything the new worker will have to learn from a file.")]),

N("new_worker", 24, "The New Worker Reads the Summary", [
 "The new worker, Mr. Osei, is courteous, prepared, and working from the summary — which is to say, from the shortest version of your family that exists. He knows the children are placed with their grandmother. He knows Dena's plan is progressing. What the summary says about your approval, in full, is the two words you could have predicted.",
 "He has a suggestion, offered helpfully, the way resets always offer themselves: the fastest way to get the approval moving, he says, is to resubmit the packet — fresh copies, current dates, a clean start for the file.",
 "A clean start. Your folder, with its stamped copy from " + fmt(S112_PACKET) + ", sits in your bag like a second opinion.",
], [C("Decide what to put in front of him: the stamped copies, or a fresh packet", "resubmit_beat",
      note="This is a small choice with a long shadow: whether the file learns that the packet already exists, with a date on it.")]),

N("resubmit_beat", 26, "Resubmit, or Show the Stamp", [
 "Resubmitting is easy, and ease is its own argument: new copies, new date, no friction with the new man in his first month. It also has a cost that does not appear on any form: a fresh packet carries a fresh date, and a fresh date quietly rewrites when this began. October becomes this week. The empty months become nobody's months — a gap with no start, attributable to no one, and therefore, in the way of files, attributable to you.",
 "Or you can do the slightly harder thing: lay the stamped copy on the table — submitted " + fmt(S112_PACKET) + ", stamp and all — and ask, politely, that the file note what already happened before anyone resubmits anything.",
], [C("Lay the stamped copy on the table and ask that the original submission date be noted in the file", "resubmit_after",
      setFlags=["submissionProven"],
      addHidden=["Approval packet — original submission date shown from caregiver's stamped copy and noted"],
      note="He photographs the stamp for the file. October is back in the record, where October belongs."),
    C("Resubmit a fresh packet — clean start, no friction", "resubmit_after",
      note="The new copies are accepted warmly. The fresh date is clean, recent, and — in every way that will matter later — wrong about when this started.")]),

N("resubmit_after", 28, "What the File Now Knows", [
 "Whichever paper you handed over, the meeting ends the same way on the surface: Mr. Osei will check on the approval, and the approval will take the time it takes. The difference is underneath, in what the file can now say about the months behind you.",
 "A file that knows a packet was submitted in October tells one story about a grandmother's empty months. A file whose earliest packet is dated this week tells another — and the second story has a hole in it exactly the shape of your savings account.",
 "You go home and write the meeting in the log, either way. Logging is what you do instead of shouting, and it has better handwriting.",
], [C("Go home — Joaquin's school form is due, and Mireya has opinions about dinner", "school_costs",
      note="The case pauses for no one's childhood. That is the case's flaw and the children's protection, in one sentence.")]),

N("school_costs", 30, "School Costs, Clinic Costs", [
 "Joaquin needs a field-trip fee and a permission slip. Mireya needs a clinic follow-up and a prescription that costs what prescriptions cost. Neither item is large. Together with the month's groceries they are the arithmetic that has been running since October, arriving in its usual installments.",
 "You pay, because the alternative — children going without, so that a grandmother's file can look comfortable — is not an alternative anyone in this house is willing to file.",
 "The log's money column is now the most honest document in the case. It is also, read cold by a stranger, the most dangerous one: it shows strain, and strain, in a summary, can be made to mean almost anything.",
], [C("Pay both, log both, and check the savings balance you have been avoiding", "savings_low", cash=-18,
      note="Eighteen dollars this round. The balance, when you look, is a number with a date attached whether you write it down or not.")]),

N("savings_low", 33, "The Balance, Looked At", [
 "The savings account that took a decade of school-kitchen overtime to build is down to its last layer. You do the arithmetic three times, the way people do when the answer is the problem: at this rate, the house has weeks of cushion left, not months.",
 "Two honest options sit on the table, and this scenario will not pretend either is painless. You can keep going — keep the house, keep the routine, and fight the paperwork with what is left. Or you can give the agency written notice that you cannot continue as the placement if the payments do not begin — a true statement, with a consequence you can see from here: a disrupted placement, and two children moved to strangers while the adults argue about a signature.",
 "Nobody should have to choose between those at a kitchen table. The choice is here anyway, because the empty months put it here.",
], [C("Keep going — and fight the paperwork with what is left", "strain_note",
      note="Not heroism. Arithmetic plus stubbornness, logged like everything else."),
    C("Give written notice that you cannot continue without the payments", "notice_beat",
      note="A true sentence, sent in writing. True sentences still have consequences, and this one's are immediate.")]),

N("notice_beat", 35, "The Notice, Sent", [
 "The notice is short, factual, and the hardest page you have ever signed: at the current rate of household spending, with no caregiver payments received since the children's arrival, you cannot continue the placement beyond the end of the month. You keep the stamped copy. Of course you keep the stamped copy.",
 "The agency answers the way systems answer ultimatums they cannot process: with urgency about the children and silence about the packet. A placement meeting is mentioned. A foster home is mentioned — as a contingency, everyone says, in the tone people use for a word they hope will frighten you back into silence.",
 "It does not frighten you. It informs you, precisely, of what the empty months were always risking — and you make the decision the notice was written to force, in the only direction left.",
], [C("Tell the children, at their sizes, that a change is coming", "end_disrupt",
      note="Joaquin asks if it is because of money. You tell him the truth at his size, which is the only size truth should ever be told to children.")]),

N("strain_note", 36, "The Word in the Summary", [
 "A copy of a case summary reaches you through Dena — a page she was given for her own plan meeting — and there it is, in the summary's flat language, next to your name: caregiver experiencing financial strain.",
 "Five words. Every one of them true, and the sentence they make is false — because the summary records the strain and not its cause, the way a photograph of a flood records water and not the broken pipe. Somewhere ahead is a review, and reviews read summaries, and a summary that says strain, standing alone, can be read as a question about whether this placement is stable.",
 "You sit with the page a long time. Then you do the thing this whole story has been teaching: you ask what paper could sit beside it.",
], [C("Ask Dena who can explain what a review will do with a line like that", "advocate_beat",
      addHidden=["Case summary — 'caregiver experiencing financial strain,' with no cause stated"],
      note="Dena has a lawyer. Lawyers, in this system, are translators between families and files.")]),

N("advocate_beat", 39, "What a Review Actually Decides", [
 "Dena's lawyer is Ms. Hart, provided for Dena as a party's counsel in this case (42 Pa.C.S. \u00a7 6337). She meets you both in a courthouse conference room and translates the review into its working parts, the way she would want it translated for her own mother.",
 "\u201cA permanency review is a hearing with a list,\u201d she says. \u201cThe court determines whether the placement is still necessary, whether the plan is being complied with, what progress has been made, and whether reasonable efforts were made to finalize the plan. (42 Pa.C.S. \u00a7 6351(f)(1), (2), (3), (5.1)) Every one of those is decided from evidence — from paper that is actually put in front of the judge.\u201d",
 "\u201cRight now,\u201d she says, \u201cthe paper in front of the judge-to-be says strain, and nothing about a packet. If we want the judge to weigh a cause, the cause has to arrive as documents. And the first document we need is the agency's own chronology — which you, Bernice, cannot request. That right belongs to the case's subjects. Dena can.\u201d",
], [C("Look at Dena — the asking is about to become hers to make", "dena_ask",
      note="The regulation's right belongs to the case's subjects, not to a placement applicant. Ms. Hart says it plainly so no one mistakes whose signature this needs.")]),

N("dena_ask", 42, "Asking Dena", [
 "The request itself is simple: Dena, as the children's mother and a party to the case, signs a written request for the case record — the chronology, the approval file, the placement notes — which under the regulation \u201cshall be released upon request\u201d (55 Pa. Code \u00a7 3130.44(d)). You cannot sign it; your name on it would make it a placement applicant's letter, and the right is not yours. Dena's name makes it what the rule contemplates.",
 "Asking her is not simple. She is mid-treatment, mid-plan, carrying her own file's worth of judgments. You can ask her to carry this one page too — at your kitchen table, with the folder open and the stamped packet copy on top — or you can spare her, and build the review answer from your folder alone.",
], [C("Ask Dena, at the kitchen table, to sign the record request this week", "dena_after",
      setFlags=["recordsRequested"], cash=-4,
      addHidden=["Case record requested in writing by the children's mother, a party, under 55 Pa. Code § 3130.44(d), at the kinship caregiver's asking"],
      note="She reads it twice, asks two exact questions, and signs. Four dollars of copies. The request is dated, copied, and kept with the plan."),
    C("Spare Dena — build the answer from your own folder alone", "dena_after",
      note="A kindness with a price: your folder knows your half cold. The agency's chronology — the half with the signature page in it — stays unread.")]),

N("dena_after", 44, "A Signature That Is Hers", [
 "Whether the request went out over Dena's signature or stayed in the folder as a road not taken, the week moves the way weeks in this house move: school runs, a clinic visit, Dena's Sunday table, Joaquin's fractions improving against his will.",
 "If Dena signed, the request is now a page in the file it asks about — which means the chronology, when it comes, will come because a party asked for it in writing, on a date, and dates are the spine of everything you are building.",
 "Ms. Hart's instruction for the waiting is one sentence: keep logging. \u201cChronologies answer chronologies,\u201d she says. \u201cYours is the only other one in this case. Keep it boring and keep it exact.\u201d",
], [C("Keep the log, keep the house, and wait for the packet to answer", "dena_progress",
      note="Boring and exact. A decade of school kitchens taught you both, in that order.")]),

N("dena_progress", 46, "Dena's Progress, in Careful Language", [
 "Dena's counselor's report arrives for her plan meeting, and Dena — who is learning, at thirty-one, to read her own file without flinching — shows it to you at the table. Progress, in the careful language: attendance complete, goals met, the plan on its rails.",
 "It matters here for a plain reason: the review ahead is about the children's placement, and the children's placement is steady partly because their mother is steady and their grandmother's house is the fixed point both of those steadinesses lean on. A review that reads strain without reading any of this will be reading a summary, not a family.",
 "\u201cTell them the house part,\u201d Dena says. \u201cNot me. The house.\u201d She means: make the paper show what the house has actually been doing. It is the best legal advice anyone gives in this story, and she gives it for free.",
], [C("Put her report copy in the folder, beside your log", "record_arrives",
      note="Two files becoming one folder, at a kitchen table, without anyone calling it a strategy.")]),

N("record_arrives", 49, "The Chronology Arrives — Or Doesn't", [
 "If Dena's request went out, the packet arrives the way records arrive: thick, partly blacked out, and heavier than its paper. If it never went out, what you have instead is the summary Dena was given, your folder, and your log — true, dated, and entirely from your side of the desk.",
 "Either way, Ms. Hart spreads what exists on her conference table and goes looking for one line: the approval packet's journey through the agency, in the agency's own chronology. Received, routed, signed, paid — the verbs a packet is supposed to collect on its way through a building.",
 "What the chronology shows — if you are holding the chronology — stops both of you mid-sentence.",
], [C("Read the approval lines together, slowly", "signature_page",
      note="Slowly is how you read a page you have been waiting three months to see.")]),

N("signature_page", 52, "The Blank Line", [
 "The chronology, in the agency's own hand, is short enough to memorize. Approval packet received: " + fmt(S112_PACKET) + " — your stamped copy's date, confirmed by the other side of the desk. Routed for signature: the following week. And then — nothing. No signature entry. No approval entry. No payment entry. Month after month of nothing, in a column where nothing is itself the entry.",
 "On the packet's own signature page, reproduced in the packet Dena requested, the line where an approver was to sign sits blank beneath a routing stamp from the week the children arrived. The packet did not fail an inspection. It was never inspected. It sat — unsigned, unacted on, unmentioned — while the file learned to call your savings account a stability question.",
 "Nobody in the room says villain. Ms. Hart says the useful word instead: \u201cDocumented.\u201d",
], [C("Ask her what a documented blank line can do at a review", "bank_book",
      addHidden=["Agency chronology — approval packet received and routed the week the children arrived; no signature, approval, or payment entry thereafter"],
      note="A blank line with a routing stamp above it. The smallest exhibit in this story, and the largest.")]),

N("bank_book", 55, "Your Side of the Ledger", [
 "Your bank book is the other half of the chronology, and it needs no lawyer to read it: a balance line descending, month by month, in amounts that match — almost to the dollar, because you logged them — the groceries, the shoes, the clinic, the lunch account. Two documents, kept by two institutions that have never spoken, telling one story in two columns.",
 "Ms. Hart puts them side by side on the table: their silence, your spending. \u201cThis,\u201d she says, \u201cis what attribution looks like when it is made of paper instead of adjectives. The gap has a start date, a routing stamp, and a blank line. The strain has the same start date. A judge does not need to be persuaded of anything. A judge needs to be shown a calendar.\u201d",
 "What remains is assembly: turning two columns into one page a review can hold.",
], [C("Ask her to lay out the assembly, step by step", "counsel_meet112",
      note="Assembly is a humble word for the most important work in this case.")]),

N("counsel_meet112", 58, "The Assembly, Step by Step", [
 "\u201cStep one,\u201d Ms. Hart says, \u201cis the chronology page — one page, dates only, every line checkable against a document: children placed, packet submitted, in-process letter, worker changed, resubmission requested, strain noted. Step two is the exhibits behind it: the stamped copy, the chronology's approval lines, the signature page, your log, your bank book. Step three is filing it — with the agency and the court, in writing, before the review — so the review reads it in advance instead of meeting it as a surprise.\u201d",
 "\u201cAnd step zero,\u201d she says, \u201cis the one you have already done, since October, without knowing its name: you kept the copies. Everything we are about to build is built out of a folder on a kitchen table. Grandmothers who throw paper away do not get this meeting.\u201d",
 "The review, she reminds you, will make its determinations from evidence (42 Pa.C.S. \u00a7 6351(f)). The plan is to make sure the evidence includes a cause.",
], [C("Build the one-page chronology with her, from the documents only", "chronology_build",
      note="Documents only. If a line cannot be checked against a page, it does not go on the page.")]),

N("chronology_build", 61, "One Page, Dates Only", [
 "The page assembles the way the log was kept: without adjectives. Placed with grandmother. Packet submitted — stamped copy attached. Agency letter: still in process. Worker changed; resubmission requested; original submission date shown and noted. Record requested by the children's mother; chronology received; approval lines end at a blank signature line. Household spending logged throughout; savings drawn down across the same months.",
 "It fits on one page because the truth of it is not complicated. It only needed to be assembled before a room that runs on summaries could summarize it wrongly.",
], [C("Build it — one page, dates only, every line checkable", "chronology_after",
      setFlags=["chronologyBuilt"], cash=-6,
      addHidden=["One-page chronology — placement, packet submission, agency lag, and household drawdown assembled from documents"],
      note="Six dollars of copies, in triplicate. One page that answers five words — caregiver experiencing financial strain — with eleven dates."),
    C("Carry the documents loose — the folder can speak for itself at the review", "chronology_after",
      note="Folders do not speak. Pages assembled from them do. The exhibits are real either way; only one version of them is readable in twenty minutes.")]),

N("chronology_after", 63, "Eleven Dates", [
 "The chronology page, finished, is the least emotional document you have ever made about the most emotional winter of your life, and Ms. Hart reads it the way judges read: once, quickly, and then again at the line where the approval column stops.",
 "\u201cThere,\u201d she says. \u201cThat is the whole case, and it took eleven dates. Everything else — the strain, the stability question, the payments — is commentary on this page. Our job now is to make the review do its commenting with this page open.\u201d",
 "Two errands remain: a written confirmation from the payments office, and the filing itself.",
], [C("Go to the payments office and ask for the confirmation in writing", "payment_office",
      note="In writing is doing all the work in that sentence, as it has since October.")]),

N("payment_office", 65, "The Payments Office", [
 "The payments office is a window, a clerk, and a screen she turns — after a moment's hesitation you will remember kindly — far enough for you to see the approval's status line. It says what the chronology said, in the system's own present tense: awaiting signature.",
 "The clerk can confirm it verbally, which helps no file anywhere. Or she can print the status page — dated today, with the packet's received date and its awaiting-signature status on it — if you ask for the printout by name.",
], [C("Ask for the printed status page, dated, with the received date on it", "review_notice",
      setFlags=["unsignedConfirmed"], cash=-4,
      addHidden=["Payments status printout — packet received in the week the children arrived; status: awaiting signature"],
      note="One printed page. The blank line, confirmed by the office that owns the line, on the day you asked."),
    C("Take the verbal confirmation — she was clear, and the bus is coming", "review_notice",
      note="Clear, kind, and unusable in a hearing room: a confirmation that exists only in your log, in your handwriting, again.")]),

N("review_notice", 67, "The Review Notice", [
 "The review notice arrives with the hearing's date and its paperwork: the agency's pre-review summary, in which the five words have grown a sentence. The summary now reports that the caregiver's financial strain raises a question about placement stability, and that the review will consider what supports the placement may need.",
 "Read cold, it is a reasonable paragraph. Read with your chronology open beside it, it is a paragraph about a flood that never mentions the pipe. Both readings will be available in the courtroom. Only one of them will be in the file unless the chronology is filed before the hearing — Ms. Hart's step three, and the last errand on her list.",
 "The hearing itself is a permanency hearing, held within six months of the children's placement (42 Pa.C.S. \u00a7 6351(e)(3)(i)). Six months is a clock too. This one, for once, is on your side: the review comes while the paper is still warm.",
], [C("Decide, with Ms. Hart, whether the chronology goes in ahead of the hearing", "paper_filed",
      note="Filed ahead, it is read in advance. Carried in, it is an ambush — and ambushes, even truthful ones, read worse than pages.")]),

N("paper_filed", 69, "Filed Ahead, or Carried In", [
 "Filing ahead costs copies, a trip, and the small social price of being the grandmother who files things. It buys the only thing that has ever mattered in this case: readers who have seen the cause before they weigh the strain.",
 "Carrying it in costs nothing today. It also means the judge meets eleven dates for the first time in a twenty-minute hearing, while the summary's sentence — the one that has been in the file for weeks — sits already read, already underlined, already halfway to being a finding.",
], [C("File the chronology and exhibits with the agency and the court, in writing, before the review", "review_prep",
      setFlags=["paperOnRecord"], cash=-6,
      addHidden=["Chronology and exhibits filed in writing with agency and court before the permanency review"],
      note="Stamped, copied, logged. The review will now be the second reading of your page, not the first."),
    C("Carry the folder to the hearing — let the judge see it fresh", "review_prep",
      note="Fresh is a quality of salads. In hearing rooms, the word for it is untested.")]),

N("review_prep", 71, "Preparing Without Rehearsing", [
 "Preparation, in Ms. Hart's office, is mostly subtraction: the chronology, the exhibits, Dena's progress report, your log. What Bernice will say, if asked, fits in three sentences, and she writes them on an index card in the handwriting that has labeled a thousand lunch trays: the children came in October. The packet went in that week. The money trouble is the packet's shadow, and the packet is in the file.",
 "\u201cDo not perform,\u201d Ms. Hart says. \u201cGrandmothers who perform get weighed as performances. Hand up paper and answer questions. The paper is better at this than any of us.\u201d",
 "Dena, on the phone that night, asks if she should come. She is a party; of course she comes. \u201cThen we both go,\u201d you say, \u201cand we let the dates talk.\u201d",
], [C("Put the index card in the folder, and go home to the children's week", "household_week",
      note="Three sentences on a card. Eleven dates on a page. A winter on both.")]),

N("household_week", 73, "The Week the Case Waits", [
 "The week before the review is, defiantly, ordinary: Joaquin loses a tooth and negotiates its price like a union man; Mireya insists on pouring her own milk and mostly succeeds; Dena's Sunday visit runs long because nobody watches the clock when the story Mireya is telling reaches its third act.",
 "This is the placement whose stability a summary is about to question: two children, in their grandmother's house, in a routine so settled it has its own weather. The routine cost money to build. It is now being read, in an office across town, as evidence that the builder is a risk.",
 "You log the week anyway — tooth, milk, story — because the log's job was never only the money. It is the house, in dates.",
], [C("Log the week, and lay out the children's clothes for the hearing morning", "bedtime_beat112",
      note="Hearing mornings start the night before, in houses that run on preparation.")]),

N("bedtime_beat112", 75, "What Mireya Asks at Bedtime", [
 "Mireya, at bedtime, asks the question underneath the whole case, in the grammar of four: \u201cAre we staying at your house a long time?\u201d",
 "You give her the truth at her size: you are staying, the grown-ups are doing their paperwork, and her job is sleep. She accepts this with the completeness children accept things, and is asleep inside the story's first page.",
 "Joaquin, eight and therefore a lawyer, asks from the doorway what happens at the review. \u201cA judge reads the papers,\u201d you say, \u201cand decides if the papers tell the truth.\u201d He considers this. \u201cDo ours?\u201d \u201cOurs are dates,\u201d you say. \u201cDates are the truest papers there are.\u201d",
], [C("Turn out the light, and check the folder one last time", "strain_deepens",
      note="Folder, card, copies. The house sleeps. The file, across town, does not — files never do.")]),

N("strain_deepens", 77, "The Form Learns a Word", [
 "Two days before the review, Dena brings word of the pre-review paperwork's other half: a scored assessment form has been updated for the review, and among the things it rates — from the visits, the notes, and the summary — is placement stability, and the rating has absorbed the summary's sentence the way forms absorb everything: without its cause attached.",
 "You cannot see the form's working. That is not this story's complaint; it is this story's weather. What you can do — the only thing anyone in your chair has ever been able to do — is make sure the room where the rating is weighed also holds the documents the rating never met.",
 "Ms. Hart, on the phone, is calm in the specific way of people holding stamped copies: \u201cForms rate what they can see. Reviews decide what counts. Ours is filed. Let it count.\u201d",
], [C("Ask whether the new worker has seen the filed chronology", "worker_ack",
      addHidden=["Scored assessment form updated for the review — placement-stability rating drawn from the summary, cause not attached"],
      note="A form's rating and a file's cause are about to be introduced, in a room with a judge in it.")]),

N("worker_ack", 79, "The New Worker's Second Reading", [
 "Mr. Osei calls the evening before the review, and his voice has the particular care of a man who has read a file twice. The chronology reached him. He checked the approval's status himself, he says — the words awaiting signature are, as of this week, no longer a secret the building was keeping from itself.",
 "He does not promise an outcome; workers who promise outcomes are writing checks the system cashes selectively. He says the smaller, truer thing: \u201cThe summary was written before the packet's history was in front of us. The review will have both.\u201d",
 "Both. For five months the case had a strain with no cause in it. Tonight, on the eve of the room that decides, it has both halves of its own story in the same file.",
], [C("Thank him, log the call, and sleep as well as hearing eves allow", "review_eve",
      note="Logged: call, date, words. Some habits outlast the cases that taught them.")]),

N("review_eve", 81, "The Night Before the Review", [
 "The folder is by the door. The index card is in the folder. Dena will meet you at the courthouse steps, a party arriving for her children's hearing with her mother beside her — which is, whatever the file calls it, the family's actual structure, arriving in person.",
 "You think about the winter in its true units: not months of process, but a stamped copy kept, a log kept, a daughter asked, a chronology assembled, a page filed. None of it was dramatic. All of it is about to be weighed in a room that weighs nothing else.",
 "Across town, the summary's sentence sits in the file too, waiting for the same room. Sentences, like grandmothers, are patient. Tomorrow they meet a calendar.",
], [C("Take the folder, take Dena's arm at the steps, and go in", "morning_review",
      note="Two generations of the same family, one folder. The courthouse has seen worse delegations.")]),

N("morning_review", 83, "Courthouse Steps", [
 "The courthouse morning runs on its rails: the metal detector, the list on the wall, the conference-room wait in which every family in the corridor is holding a version of the same folder. Dena's hands are steady. Yours are steady. Steadiness, in this building, is a form of testimony.",
 "Ms. Hart goes through the exhibits once, in order, the way she will hand them up: stamped copy, chronology page, signature page, status printout, log, bank book. \u201cDates first,\u201d she says. \u201cFeelings in the hallway, where they belong and where I will have plenty of my own afterward.\u201d",
 "The clerk calls the case. The children's case. The room, as ever, is smaller than what happens in it.",
], [C("Go in, and let the hearing be a hearing", "review_hearing",
      note="Twenty minutes, a judge, and two versions of one winter: a sentence, and a calendar.")]),

N("review_hearing", 85, "The Review", [
 "The judge opens the way the statute opens: this is a permanency hearing, and the court will determine the continuing necessity of the placement, compliance with the plan, the progress made, and whether reasonable efforts were made to finalize the plan (42 Pa.C.S. \u00a7 6351(f)(1), (2), (3), (5.1)) — and it will determine them from the evidence.",
 "The agency's summary is read first: the placement is going well; the children are settled; the caregiver is experiencing financial strain, raising a stability question. The sentence lands in the room exactly as written — true words, missing their cause, halfway to a finding.",
 "Then Ms. Hart rises, and what happens next depends — with a precision this story has been honest about since October — on what your winter actually put in her hands.",
], [C("Put the full paper on the record — the stamped copy, the eleven dates, the blank signature line", "end_win",
      requiresFlags=["recordsRequested", "chronologyBuilt", "paperOnRecord"],
      note="Exhibit by exhibit: received, routed, unsigned, unpaid — and a household ledger that matches the silence, month for month."),
    C("Accept the agency's hallway offer — payments started this week, the stability sentence left for another day", "end_middle",
      note="Money now; language later. It is a real offer, and its price is written in the part of the file that travels."),
    C("Answer the stability question out loud — the winter, told by the woman who lived it", "end_strain",
      requiresNoFlags=["paperOnRecord"],
      note="Every word of it is true. The summary is printed, filed, and already read; your voice is in the room for twenty minutes and in the transcript forever — at a summary's length, in a summary's words.")]),

N("end_win", 88, "Ending \u2014 Payments Begin, and the File Tells the Truth (PARTIAL)", [
 "The review does the thing reviews do when a cause arrives as exhibits: it re-describes the winter. The chronology is walked line by line — the packet's received date confirmed from the agency's own chronology, the routing stamp, the blank signature line, the status printout reading awaiting signature five months after the children arrived. The judge asks the agency one question — when the signature will happen — and accepts, on the record, the answer the building owed you in November: this week.",
 "The order that follows keeps the placement exactly where it is, and writes the winter correctly while it does it: the caregiver's financial strain is attributed, in the findings, to the delayed approval — an agency processing lag — and not to the caregiver. Payments are directed to begin, with the approval completed on the record's own dates. The stability question, as a question about Bernice, is withdrawn by the only mechanism that ever withdraws such questions: better paper, in the same file, read by the person who decides.",
 "You walk out with Dena's arm in yours and a folder that weighs the same as it did this morning. What it means has changed entirely.",
], ending=True, debrief=[
 "WHAT THE FILE HELD (the hidden record, revealed): Two columns that finally met. Their column: a packet received " + fmt(S112_PACKET) + ", routed the following week, and then a blank signature line and an awaiting-signature status for five months — the agency's own chronology and its own payments printout, obtained because Dena, a party, requested the record that \u201cshall be released upon request\u201d (55 Pa. Code \u00a7 3130.44(d)). Your column: the stamped copy that proved October, the call log, the bank book whose descent matched the silence month for month, and a one-page chronology of eleven checkable dates, filed with the agency and the court before the hearing. At the hearing the court made its determinations from evidence (42 Pa.C.S. \u00a7 6351(f)(1), (2), (3), (5.1)) — and the evidence had a cause in it.",
 "LABEL THIS WIN HONESTLY \u2014 IT IS PARTIAL: Payments begin, the record attributes the gap to the lag and not to the caregiver, and the placement is steadied on a truthful file. The drained savings are not restored by this ending or any ending in this scenario: the decade of overtime that the empty months spent stays spent, and no order in this story writes it back. What the win returns is the future — a placement read correctly from here, and payments that now arrive in the present tense. Anyone who calls that whole is selling something. It is enough, and it is not everything, and both halves of that sentence are the lesson.",
 "WHAT NO STRATEGY CONTROLS: A different judge could have noted the chronology and pressed the stability question anyway; a payments office that lost the printout, a worker who never re-read the file, a daughter too deep in her own crisis to sign a page — any of them thins this ending without Bernice changing a thing. Workers, judges, clerks, and luck held pieces of it. What her choices controlled was narrower and durable: when the system finally weighed her winter, it weighed a calendar she had kept since October, instead of a sentence it had written about her in her absence.",
]),
N("end_middle", 88, "Ending \u2014 Paid, With the Note Still Standing", [
 "The hallway offer is real, and you take it with open eyes: the approval is completed that week — the signature, it turns out, was always a week's work — and the first payment arrives before the month turns. Groceries stop being arithmetic. The house exhales.",
 "Inside the courtroom, the review is brief and kind. The placement continues. And the summary's sentence — caregiver experiencing financial strain, stability question noted — is adopted into the review's paperwork without its cause ever being put beside it, because the chronology that carries the cause was never the price of the hallway deal. The strain is over. Its description remains, filed, quotable, and available to every future reader of this case.",
 "You have won the money and lost the sentence. Both facts will travel with the file. Only one of them was ever going to pay for shoes.",
], ending=True, debrief=[
 "WHAT THE FILE HELD (the hidden record, revealed): The same two columns as every path — the agency's blank signature line and your descending bank book — but assembled, if at all, only as a private folder, never as the review's evidence. The payments were fixed in a hallway, administratively, the moment the building was embarrassed into a signature. The record of why they were late was nobody's exhibit. So the file keeps both truths in their unbalanced forms: payments, current; strain, unexplained — a caregiver whose file says she struggled financially in the winter her grandchildren arrived, with the reason living in her kitchen-table folder instead of in the case.",
 "THE PROCESS UNDER THIS PATH: The right that would have corrected the sentence was the verified one — the case record, released on a party's written request (55 Pa. Code \u00a7 3130.44(d)), signed by Dena because the right belongs to the case's subjects, not to a placement applicant — and the review that would have weighed the correction decides its questions from evidence put before it (42 Pa.C.S. \u00a7 6351(f)). A hallway can start payments. Only a record can re-describe a winter, and this winter's re-description was traded away, knowingly, for speed. The trade is understandable. Trades still cost what they cost.",
 "THE HONEST PART: This ending is not a failure, and this debrief will not pretend the money is a small thing — it is rent, food, and a grandmother sleeping without arithmetic. It is a partial ending with the partiality located precisely: the future is paid for and the past is misdescribed, and the misdescription is the part with a forwarding address. A later review, a different worker, a new summary quoting the old one — the note will be read again by people who were not in the hallway. Whether it is ever corrected will depend on paper that, as of tonight, still lives only in a folder on a kitchen table — where, to Bernice's credit and this system's instruction, it at least still exists.",
]),
N("end_strain", 88, "Ending \u2014 Strain, Entered as Instability", [
 "You tell the winter beautifully. You tell it in order, with the dates you know by heart, and the room listens the way rooms listen to grandmothers: with respect, and with a printed summary open in front of them.",
 "The order, when it comes, is not cruel. The placement continues — the children are settled, everyone agrees — and the court, weighing the only paper it was given about the money, does what paper invites: it notes the caregiver's financial strain as a placement-stability concern, directs supportive services aimed at the caregiver's budgeting and household management, and sets the next review to examine whether the strain has resolved.",
 "Services, arriving at last — aimed, with perfect administrative logic, at the one diagnosis the file contained. The packet, unsigned on a desk across town, is not mentioned in the order. It is not mentioned anywhere. That is what unmentioned things do: they continue.",
], ending=True, debrief=[
 "WHAT THE FILE HELD (the hidden record, revealed): A summary's sentence, adopted: strain, entered as instability, with services ordered around the wrong diagnosis — budgeting help for a woman whose budget was raided by a missing signature. Your account of the lag was spoken at the review and is preserved the way spoken accounts are: summarized, briefly, in someone else's words. The chronology that would have proven it — the agency's own approval lines ending at a blank signature line, obtainable on a party's written request under 55 Pa. Code \u00a7 3130.44(d) — was never requested, or never assembled, or never filed, and a court making its determinations from evidence (42 Pa.C.S. \u00a7 6351(f)(1), (2), (3), (5.1)) cannot weigh a cause it was never handed.",
 "THE PROCESS UNDER THIS PATH: Nothing in this ending required bad faith from anyone in the room. The summary said strain; no exhibit said lag; the order therefore treated strain. That is the mechanism this scenario exists to teach: in a permanency review, the file's description of a problem becomes the court's prescription for it, and descriptions are only ever corrected by other documents — filed, dated, and in the record before the hearing weighs them. An oral history, however true, enters the record as the note-taker's summary of it, and summaries are how this winter got misdescribed in the first place.",
 "THE HONEST PART: Be fair to the woman in this ending, because the file was not: she fed two children for five months out of her own old age, kept every copy, and told the truth in the room. The system's failure to sign a packet became, on paper, her instability — and the services now ordered will consume her afternoons teaching her to manage money she managed correctly all along. A kinder judge might have asked the agency for its approval chronology unprompted; some do. This one weighed what was filed. The folder on the kitchen table still holds the correction. Folders, unlike hearings, do not expire — but they do wait, and waiting is what the empty months were made of.",
]),
N("end_disrupt", 38, "Ending \u2014 Notice Given: The Placement Disrupts", [
 "The contingency becomes the plan, in the brisk language of placement meetings: the children will move to a foster home at the end of the month, as a temporary measure, everyone says, until the caregiver's circumstances stabilize. Temporary is a word this system uses the way families use soon — sincerely, and without a date attached.",
 "Joaquin packs his school bag and a second bag, and asks whether the new house will know that Mireya cannot sleep without the story. You write it on a card for the new caregiver, in your clearest hand: the story, the milk, the tooth money rates. It is the last document you file in this case, and like all your documents, it is exact.",
 "The approval packet, the record will eventually show, was signed some weeks after the children moved — in process, completed at last, in an empty house's file. Nobody in this ending acted from cruelty. A signature was late, a savings account was finite, and two children paid the exchange rate between those two facts.",
], ending=True, debrief=[
 "WHAT THE FILE HELD (the hidden record, revealed): A grandmother who did everything in ink — packet submitted " + fmt(S112_PACKET) + ", stamped copy kept, calls logged — and an agency chronology nobody in this path ever requested, in which the packet she submitted sat unsigned from the week the children arrived. The notice Bernice sent was true when she sent it: the money was gone because the payments had never come, and the payments had never come because of a blank line in a building she had never entered. The disruption is recorded in the file as a caregiver's inability to continue. Its cause is recorded nowhere, because the document that would record it was never asked for.",
 "THE PROCESS UNDER THIS PATH: The instrument that changes this ending is the verified one, and it was never Bernice's to sign: the case record \u201cshall be released upon request\u201d (55 Pa. Code \u00a7 3130.44(d)), and the right belongs to the case's subjects — Dena, a party, signing at her mother's asking, as the kinship scenario in this series teaches it. With the chronology in hand, the review's determinations (42 Pa.C.S. \u00a7 6351(f)) would have had a cause to weigh. Without it, the file weighed the only thing it held: a finite bank account. Notice, in this system, is also a document — and a true notice, sent without the chronology behind it, reads to every later reader as a capacity finding instead of a billing record.",
 "THE HONEST PART: This ending must not be read as a grandmother failing two children. It is a placement ended by arithmetic that an unsigned packet imposed on a fixed income — the documented administrative-lag pattern this scenario is built from, run to its end. A worker who escalated the signature, a supervisor who audited awaiting-signature packets, a daughter positioned to sign a request in November instead of February: other people's paper held pieces of this too, and any one of them changes it. What Bernice controlled — the copies, the log, the truth told at kitchen-table size — she did, from the first week, in ink. The system's blank line outlasted her savings anyway. That sentence is the indictment this scenario files, and it is filed against a line, not a woman.",
]),
]
assert len(s112_nodes) == 40, len(s112_nodes)
assert sum(1 for n in s112_nodes if n.get("ending")) == 4

s112_meta = {"title": "The First 90 Days",
 "subtitle": "Scenario 112 \u2014 The Empty Months (a fictional composite)",
 "startDateISO": "2026-01-12", "startNode": "start", "startCash": 170,
 "tier": "Complex",
 "summary": "A kinship grandmother's approval packet sits unsigned for months; her drained savings are then read as a stability risk \u2014 until the chronology is put on the record."}

s112_win = {
 "start": "Open the folder on the kitchen table \u2014 the one with the stamped copies",
 "folder_copies": "Call the agency and ask, again, where the payments are",
 "payment_call1": "Thank her, hang up, and do the week's grocery math at the table",
 "grocery_math": "Pay for the week's groceries and the shoes, and write the total in the log",
 "dena_sunday": "Walk her to the bus, and come home to the week's ordinary work",
 "letter_in_process": "File the letter, and get ready for the home visit this week",
 "home_visit": "See her out, and help Joaquin with the homework he has been avoiding",
 "worker_goodbye": "Thank her, wish her well, and write the transfer in the log",
 "new_worker": "Decide what to put in front of him: the stamped copies, or a fresh packet",
 "resubmit_beat": "Lay the stamped copy on the table and ask that the original submission date be noted in the file",
 "resubmit_after": "Go home \u2014 Joaquin's school form is due, and Mireya has opinions about dinner",
 "school_costs": "Pay both, log both, and check the savings balance you have been avoiding",
 "savings_low": "Keep going \u2014 and fight the paperwork with what is left",
 "strain_note": "Ask Dena who can explain what a review will do with a line like that",
 "advocate_beat": "Look at Dena \u2014 the asking is about to become hers to make",
 "dena_ask": "Ask Dena, at the kitchen table, to sign the record request this week",
 "dena_after": "Keep the log, keep the house, and wait for the packet to answer",
 "dena_progress": "Put her report copy in the folder, beside your log",
 "record_arrives": "Read the approval lines together, slowly",
 "signature_page": "Ask her what a documented blank line can do at a review",
 "bank_book": "Ask her to lay out the assembly, step by step",
 "counsel_meet112": "Build the one-page chronology with her, from the documents only",
 "chronology_build": "Build it \u2014 one page, dates only, every line checkable",
 "chronology_after": "Go to the payments office and ask for the confirmation in writing",
 "payment_office": "Ask for the printed status page, dated, with the received date on it",
 "review_notice": "Decide, with Ms. Hart, whether the chronology goes in ahead of the hearing",
 "paper_filed": "File the chronology and exhibits with the agency and the court, in writing, before the review",
 "review_prep": "Put the index card in the folder, and go home to the children's week",
 "household_week": "Log the week, and lay out the children's clothes for the hearing morning",
 "bedtime_beat112": "Turn out the light, and check the folder one last time",
 "strain_deepens": "Ask whether the new worker has seen the filed chronology",
 "worker_ack": "Thank him, log the call, and sleep as well as hearing eves allow",
 "review_eve": "Take the folder, take Dena's arm at the steps, and go in",
 "morning_review": "Go in, and let the hearing be a hearing",
 "review_hearing": "Put the full paper on the record \u2014 the stamped copy, the eleven dates, the blank signature line",
}

# =====================================================================
# SCENARIO 113 — The Unit That Needed a Date
# Umar placed: Monday, March 3, 2025.
# ASFA 15-month date: Wednesday, June 3, 2026 = dayOffset 61 from the
# story start (Friday, April 3, 2026, month 13) — computed + asserted.
# The filing-day node sits exactly on dayOffset 61.
# =====================================================================
S113_START = date(2026, 4, 3)
S113_ENTRY = date(2025, 3, 3)
S113_ASFA = add_months(S113_ENTRY, 15)
assert S113_START.strftime("%A") == "Friday"
assert S113_ENTRY.strftime("%A") == "Monday", S113_ENTRY
assert S113_ASFA == date(2026, 6, 3) and S113_ASFA.strftime("%A") == "Wednesday", S113_ASFA
assert (S113_ASFA - S113_START).days == 61

def d113(off):
    return fmt(S113_START + timedelta(days=off))

s113_nodes = [
N("start", 0, "Month Thirteen, One Goal Left", [
 "Your name is Farida. Your son Umar is ten, and he has been in foster care since " + fmt(S113_ENTRY) + " — thirteen months of a childhood, measured by the system in reviews and by you in school terms. This morning the case has a shape it has never had before: of every goal on your plan, exactly one is still open.",
 "Treatment: completed, certificate filed. Parenting program: completed. Employment: steady, pay stubs in the folder. Visits: kept, expanded, warm — Umar beats you at chess now and explains, each time, exactly how. The open goal is the one printed in the same bold type as all the others: HOUSING. You live in a single room whose lease does not permit a child to live in it. Everyone agrees you have done the work. Agreement has not yet produced an apartment.",
 "Somewhere in the case there is a date the calendar is walking toward, and this month — month thirteen — your lawyer has asked to meet about it. Not because anything went wrong, she said. Because of what is about to be true.",
], [C("Go to the meeting — and bring the folder, as always", "folder_audit113",
      note="The folder holds the whole case in your handwriting: certificates in front, housing at the back, where the unfinished things live.")]),

N("folder_audit113", 2, "The Folder, Audited", [
 "Before the meeting, the folder gets its audit on the kitchen table — the small table, in the single room, that has served as desk, office, and evidence locker for thirteen months. Front section: every completion the plan ever asked for, dated. Back section: housing, and housing is a different kind of thick — applications, waitlist letters, stamped receipts, a year of paper proving effort against a list.",
 "What the audit shows is the case in one image: your side is finished, and the unfinished side is not a task. It is a queue. Queues do not respond to effort. They respond, if they respond at all, to paper arriving in the right order.",
 "Your lawyer, Ms. Adler, keeps a calendar with one date circled in pencil. Today she is going to tell you whose date it is.",
], [C("Take the audited folder to Ms. Adler's office", "housing_office",
      note="First, the housing office — the letter she asked you to collect on the way, with your position on it, dated.")]),

N("housing_office", 4, "Position, Stamped", [
 "The housing office waiting room has the chairs and the ticket machine that waiting rooms for lists always have. The clerk is not the enemy; she is the list's receptionist, and she has been yelled at by people who were told a month, so she does not tell months.",
 "What she will do — what clerks of lists will reliably do for people who ask calmly, with a folder — is print the page: your name, your applications, their dates, your position, today's date stamped by the machine that stamps it. A position on a list is either a rumor or a fact, depending entirely on whether it is printed.",
 "You take the printout for the folder, and one more piece of mail that has been waiting in your box at the residence: an envelope from the housing program itself.",
], [C("Open the program's envelope at the table before you leave", "program_letter",
      cash=-4,
      note="Four dollars of bus fare for the trip. The envelope is thin, official, and — unusually for this case — about to be specific.")]),

N("program_letter", 6, "The Letter With a Condition in It", [
 "The program's letter is one page, and it says what it says on its face, in the plain language of programs: your application is complete and you are approved in principle for a family unit through the program — and the unit can be approved for occupancy once a return date for Umar exists, within sixty days of the approval, so that the unit and the child's return can be scheduled together. A return date, the letter says, is what the program needs from the court.",
 "Read it again, because the whole scenario lives in this paragraph: the housing is not waiting for your effort, your income, or your position alone. It is waiting for a date — a date that only a court, on the agency's recommendation, can set.",
 "You have been in this case thirteen months. This is the first time the barrier has been stated, in writing, as a thing the system itself is holding.",
], [C("Decide what to do with a letter like this: keep the original safe, or carry it loose", "letter_after",
      note="Letters that state systems' conditions in systems' own words are exhibits in waiting. They should be treated like glass.")]),

N("letter_after", 8, "Glass, Filed", [
 "The original goes in the folder's front pocket — the pocket for documents that would be hard to replace — and a copy goes behind it, because originals in this system travel and copies are how travel is survived.",
 "You sit with the letter's arithmetic a moment, because arithmetic is about to matter: the program needs a return date within sixty days. The agency, at your last meeting, said — in words you wrote down in the car — that no return date can be set until housing is secured. Housing is secured when the program approves the unit. The program approves the unit when a return date exists.",
 "A circle, drawn in two offices' handwriting, with your son in the middle of it. Circles in this system are not broken by effort. They are broken, if at all, by documents that make a room choose which half of the circle to act on first.",
], [C("Get a dated copy made for Ms. Adler, and go to the agency meeting first", "agency_meeting",
      setFlags=["programLetter"], cash=-3,
      addHidden=["Housing program letter — unit approvable once a return date within sixty days exists; dated copy obtained"],
      note="Three dollars of copies. The letter now exists in two places, which in this system is the beginning of existing at all."),
    C("Carry the original loose — Ms. Adler can read it at the meeting", "agency_meeting",
      note="She can, and she will. What she cannot do, later, is cite a copy that was never made, from a letter that lives in a coat pocket.")]),

N("agency_meeting", 10, "No Date Until Housing", [
 "The agency meeting is courteous and short. Your worker, Ms. Beam, reports your progress the way the file reports it: everything complete but housing. You show her the program's letter. She reads it with the attention of a person reading her own side of a correspondence she did not know was one.",
 "\u201cThe program needs a return date,\u201d she says. \u201cI understand that. But we can't recommend a return date until the housing is in place. That's the sequence. Housing first, then the date.\u201d",
 "You say, as gently as the sentence allows: the program's sequence is the other one. She does not disagree. She says she will note it in the file — and there, in miniature, is the whole case: a circle, noted, in a file, by two people who both see it and neither of whom, alone, can break it. Noting is not breaking. But a noted circle is at least a circle on paper, and paper is where breaking happens.",
], [C("Ask her to note the letter itself in the file — not just the conversation", "counsel_meet113",
      addHidden=["Agency meeting — program letter shown; agency position restated: no return date until housing is secured"],
      note="She writes the note while you watch. Whether it quotes the letter or summarizes it is a distinction this scenario has opinions about.")]),

N("counsel_meet113", 12, "Two Circles and a Date", [
 "Ms. Adler is your lawyer in this case, as the law provides for a parent (42 Pa.C.S. \u00a7 6337). She reads the program's letter twice, puts it down, and turns her desk calendar around: the circled date is " + fmt(S113_ASFA) + ".",
 "\u201cUmar was placed on " + fmt(S113_ENTRY) + ". At fifteen of the most recent twenty-two months, the agency is generally to file a petition to terminate parental rights — unless an exception is documented (42 U.S.C. \u00a7 675(5)(E)). Fifteen months from his placement is " + fmt(S113_ASFA) + " — " + d113(61) + ", sixty-one days from the morning this chapter opened. That is the first circle's deadline: the housing circle has to be answered before the calendar answers it for us.\u201d",
 "\u201cGenerally is doing real work in that sentence,\u201d she says. \u201cThere are three documented doors in it, and two of them may be standing open in your file already. Sit down. We are going to read what the file actually says — all of it, including the parts about what the agency was supposed to do about housing.\u201d",
], [C("Sit down, and ask her to say the exceptions slowly", "records_beat113",
      addHidden=["Counsel meeting — ASFA date " + fmt(S113_ASFA) + " named; housing circle and exceptions explained"],
      note="She writes three numbered lines on a legal pad before she says another word.")]),

N("records_beat113", 15, "Asking for the File", [
 "\u201cAt fifteen months, the agency is generally to file — unless an exception is documented: the child is being cared for by a relative; or there is a documented compelling reason that filing would not serve the child; or the agency has not provided the services it identified as necessary for the child's safe return (42 U.S.C. \u00a7 675(5)(E)). Now hear the discipline of it: the exceptions are record-dependent. They exist as arguments only to the extent the case file documents them. So our first job is not arguing. It is reading the file the decision will be made from.\u201d",
 "There is a right that does not depend on any hearing: a parent may request the case record from the county agency, and under the regulation the material \u201cshall be released upon request\u201d (55 Pa. Code \u00a7 3130.44(d)). Ms. Adler drafts the request while you watch — the full record, the service plan, and everything the file holds about housing assistance.",
], [C("Sign the written request for the complete record this week", "file_review113",
      setFlags=["recordsRequested"], cash=-6,
      addHidden=["Case record requested in writing under 55 Pa. Code § 3130.44(d)"],
      note="Signed, dated, copied. The request itself is now a page in the file it asks about."),
    C("Wait until after the next review — the circle is the urgent thing", "summary_only113",
      note="Understandable, and the circle is urgent. The exception, though, lives or dies in the file the circle is drawn in — unread files keep their secrets in both directions.")]),

N("file_review113", 18, "Reading for What Isn't There", [
 "The record arrives: thick, partly blacked out, and readable. You and Ms. Adler read it the way she taught you — for the housing-assistance service specifically, because the plan identified housing assistance as a service necessary for Umar's safe return, and the third exception is about exactly that: what was identified, and what was actually provided.",
 "The plan's housing page is thorough about you: applications to be made, documentation to be kept, lists to be joined — and your compliance is noted, complete, dated, month after month. The page is considerably thinner about the agency's half: a referral line with no follow-through entry; assistance described in the plan's language and then, in the chronology, largely unmentioned again.",
 "Reading for an absence is a skill this case has been teaching you for thirteen months. This is its examination.",
], [C("Mark every housing line — yours and theirs — and ask what the pattern proves", "housing_service_read",
      addHidden=["Agency record read with counsel — plan identified housing assistance; parent's housing compliance documented; agency follow-through entries sparse"],
      note="Highlighter for yours, pencil for theirs. The pencil gets less exercise, and that is the exhibit.")]),

N("summary_only113", 18, "Working from Summaries", [
 "Without the record, you work from the review reports — which are fair about your progress and summary about everything else. A summary can tell you the agency considers housing your open goal. It cannot show you the plan's own housing-assistance language, or the chronology's thin places where the agency's half of that service was supposed to be entered.",
 "Ms. Adler is blunt, kindly: \u201cWe can still build from your folder and the program's letter. What we cannot do is quote their file against itself — and in June, quoting their file against itself is the strongest version of this argument there is. Start with your stamps. They are, at least, unimpeachable.\u201d",
], [C("Start with your own paper — the stamped applications, in order", "housing_service_read",
      note="The gaps are real either way. The question June asks is whether they are documented, and by whose paper.")]),

N("housing_service_read", 21, "What the File Documents — and Doesn't", [
 "On the legal pad, under the three exception lines, Ms. Adler writes two columns. DOCUMENTED: your applications, complete and dated; your waitlist positions, printed; the program's letter, with its condition stated on its face; your completions everywhere else on the plan. NOT DOCUMENTED: any entry showing the agency providing the housing assistance its own plan identified — no referral follow-through, no assistance contacts, no entry addressing a return date or the program's condition, in thirteen months of chronology.",
 "\u201cHear me precisely,\u201d she says, \u201cbecause precision is the whole argument. I am not saying the agency did nothing out of malice. I am saying the file does not document the service the plan identified. The services exception is record-dependent: it is exactly as strong as this column is empty. And the compelling-reason door stands beside it: a parent who has completed everything but the goal the system's own circle is blocking, with a program letter proving the block — documented in the case plan, that is a reason, in writing, that filing would not serve Umar.\u201d",
 "\u201cTwo doors,\u201d she says. \u201cBoth made of paper. Both need assembling before " + fmt(S113_ASFA) + ".\u201d",
], [C("Read the chronology's silences closely, month by month, before assembling anything", "chronology_silence",
      note="Dates first, as ever \u2014 including the dates that are missing, which are also a kind of date.")]),

N("chronology_silence", 23, "The Silence, Read Closely", [
 "One more pass through the chronology, slowly, the way you would read a letter from someone whose silences you have learned to translate. Month by month, your housing entries are verbs: applied, documented, waited, re-applied. The agency's housing entries are mostly nouns: housing, noted. Housing, pending. Housing, barrier.",
 "A barrier is not a service. A note is not an assistance contact. The chronology does not accuse anyone — chronologies never do — it simply shows, in the agency's own sequence, a service that was identified in the plan and then documented mainly by its absence.",
 "Ms. Adler closes the binder. \u201cThat,\u201d she says, \u201cis tab one of the packet. Tab two is your stamps. Tab three is the program's letter. Tab four is the compelling reason, which writes itself out of tabs one through three — if we write it carefully and file it in time.\u201d",
], [C("Turn to tab two — your applications, and their stamps", "waitlist_stamps",
      note="A thin binder, labeled in pencil with a June date, opens on the table. Binders in this system are where arguments live before they are arguments.")]),

N("waitlist_stamps", 25, "Tab Two: The Stamps", [
 "Your applications, laid in a row, are a year of this case told in receiving stamps: the first application, filed in the case's early months; the renewals; the program application that produced the letter. Every one complete. Every one dated. The waiting list has moved at the speed waiting lists move, and the stamps prove the one thing the file must never be allowed to re-describe: the waiting was the list's, not yours.",
 "Assembled into one stamped set, with a cover page of dates, they stop being errands you ran and become a document a stranger can read cold — which is the only kind of document June respects.",
], [C("Assemble the dated application copies into one stamped set for the packet", "stamps_after",
      setFlags=["housingDoc"], cash=-5,
      addHidden=["Housing — dated, complete applications and waitlist stamps assembled as one set"],
      note="Five dollars of copies. A year of queues, in date order, with your name spelled right on every stamp."),
    C("Rely on the summaries — they have always called your applications complete", "stamps_after",
      note="They have. Summaries describe; stamps prove. June is a month that prefers proof, and strangers read stamps without needing to trust anyone.")]),

N("stamps_after", 27, "A Year, in Date Order", [
 "The stamped set goes behind tab two, and the binder gains the particular weight of paper that agrees with itself. Ms. Adler turns the pages slowly: applications, positions, the letter — or, where the assembling did not happen, your own clear recollection, which she does not mock and does not overvalue.",
 "\u201cTab three next,\u201d she says. \u201cThe program's letter is the packet's hinge — it is the system stating its own condition in its own words. Before we build on it, we confirm it: a call to the program, on the record of your log, so June hears the letter confirmed by the office that wrote it.\u201d",
], [C("Call the program and confirm the letter, on the log", "program_call",
      note="Confirmation is a humble errand with an exhibit's consequences: a letter, verified, by its author, in your dated log.")]),

N("program_call", 29, "The Program, Confirmed", [
 "The program's coordinator is brisk and clear, the way people are clear about things they have put in writing. Yes, the letter states the program's position. Yes, your application is complete. Yes — and she repeats it slowly, for the log you tell her you are keeping — once a return date within sixty days exists, the unit can be approved for occupancy on that schedule.",
 "She does not set return dates. She does not comment on the agency's sequence. She confirms her office's letter, on its face, and wishes you well with the specific warmth of a person who has watched this exact circle from her desk more than once.",
 "In the log, the call takes four lines. Letters confirmed by their authors are the packet's load-bearing walls.",
], [C("Log the call, file the log page behind tab three, and look at the circle whole", "circle_diagram",
      addHidden=["Housing program — letter's condition confirmed by the program by phone and logged with date"],
      note="Tab three: a letter, confirmed. The circle now exists in documents from both of its offices.")]),

N("circle_diagram", 31, "The Circle, Drawn", [
 "Ms. Adler draws it on the legal pad, because some things have to be seen to be argued: HOUSING needs DATE. DATE needs HOUSING. A two-box loop with no entrance — except, she taps the pad, the doors the law keeps in exactly this wall.",
 "\u201cThe exception packet is the entrance,\u201d she says. \u201cNot because paper is magic. Because the filing decision in June will be made on the file — and a file that documents a services gap and a compelling reason gives the decision somewhere lawful to land that is not a petition. And a documented return timeline, argued from the program's own letter, gives the court a date it can actually set — which is the thing the program is waiting for. The packet and the letter, together, are how a room breaks a circle: each unlocks the other's condition.\u201d",
 "\u201cBut hear the deadline inside the strategy,\u201d she says. \u201cA packet filed after " + fmt(S113_ASFA) + " is an argument about a decision already made. Ours goes in before. That is not a detail. It is the design.\u201d",
], [C("Ask what tab four — the compelling reason — needs from your life, not your file", "umar_visit",
      note="It needs, she says, the ordinary evidence of a finished plan and a waiting child — which is to say, next Saturday's visit, documented like everything else.")]),

N("umar_visit", 33, "Saturday, Month Fourteen", [
 "Saturday's visit is at the foster family's home, and Umar — ten, all elbows and chess openings — has set up the board before you finish taking off your coat. He wins the first game. In the second, he explains, while winning more slowly out of kindness, that his class is doing a unit on maps.",
 "He asks, in the middle of the map conversation, the question the program's letter asks in office language: when is he coming to your house — not the room, the house, the one with his room in it? You tell him the truth at his size: the grown-ups are working on the date, a judge helps decide dates, and your job is the visits and the paperwork, both of which you are doing.",
 "He accepts this with a ten-year-old's completeness and returns to the map. On the bus home you think about dates: the one in pencil on a lawyer's calendar, and the one a boy just asked for, which is the same date, wearing its real clothes.",
], [C("Write the visit up in the folder that night, dated", "umar_school",
      note="Contemporaneous, as ever: written while the chess game is still set up in your head.")]),

N("umar_school", 35, "The School Note", [
 "Umar's teacher sends a note through the visit bag, addressed to you — a courtesy teachers extend and systems rarely notice: his reading is strong, his map unit was the class's best, he tells people his mom is \u201cgetting the house ready.\u201d The foster mother passes it along promptly and without commentary, which you have learned is her form of precision: the file gets the fact, not her feelings about the fact.",
 "Into the folder it goes, behind the visit write-up. Tab four is accumulating the way compelling reasons actually accumulate — not as an argument, but as a year of finished work and a child, documented, in the middle of it.",
 "Ms. Adler's packet outline arrives by email that night: four tabs, two exceptions, one deadline. April is for assembly. The deadline is not in April.",
], [C("File the note, and turn to the packet's assembly", "packet_plan",
      note="A teacher's note is not law. It is what law's compelling reasons are made of, when they are made honestly.")]),

N("packet_plan", 37, "The Packet, Planned", [
 "The packet, planned on the legal pad, has the shape of the file itself. Tab one: the services gap — the plan's housing-assistance language, the chronology's thin follow-through, the two-column page you built from the record. Tab two: your stamped applications — the waiting proven to be the list's. Tab three: the program's letter, confirmed — the circle, in the system's own words. Tab four: the compelling reason — every other goal complete, visits kept, a unit waiting on a date, and a boy in month fourteen of a placement his mother's finished plan says he no longer needs to be in, for reasons the file itself documents.",
 "Over it all, a covering statement from Ms. Adler that says what the packet is and is not: it does not accuse anyone of bad faith. It documents a services gap and a compelling reason, and asks that both be documented in the case plan when the filing decision is made — before the date the calendar has circled.",
 "\u201cAssembled from documents, it is an exhibit,\u201d she says. \u201cAssembled from memory, it is a claim. We file the first kind.\u201d",
], [C("Assemble it from the documents only — every entry checkable", "packet_contents",
      note="Shorter than your memory of the thirteen months. Stronger, for exactly that reason.")]),

N("packet_contents", 39, "Two Doors, One Binder", [
 "Assembly is slow, unglamorous, decisive work: the chronology excerpts checked against the record, the stamps in order, the letter's copy crisp, the covering statement read aloud once for accuracy and once for tone. A packet that overclaims by one line loses the lines that were true, so the packet claims only what its tabs prove.",
 "When it is done, the binder holds the whole strategy in a form a stranger can audit: a service identified and not documented as provided; a reason, documented, that filing would not serve this child; a program waiting on a date; a mother whose own lines in the file are complete. Two doors, one binder, and a date in June that does not negotiate.",
], [C("Sign the packet's assembly page, and face the filing decision", "packet_draft",
      setFlags=["packetBuilt"], cash=-5,
      addHidden=["Written exception packet assembled from documents — services gap and compelling reason, with exhibits"],
      note="Five dollars of final copies. The packet exists. Existing, in this system, is the prerequisite for everything else.")]),

N("packet_draft", 41, "The Covering Statement", [
 "Ms. Adler's covering statement is two pages, and its discipline is the scenario's discipline in miniature. It names the date — " + fmt(S113_ASFA) + ". It names the two exceptions the packet documents, in the statute's own shape: services identified as necessary for Umar's safe return that the file does not document as provided, and a compelling reason, documented in the case plan, that filing would not serve him (42 U.S.C. \u00a7 675(5)(E)). It attaches the program's letter and asks — in the same document, because they are the same ask — that a return date be set that lets the unit be approved.",
 "Its last paragraph says what every page of this scenario has been careful to say: the packet speaks to the filing decision and to the plan. It decides nothing else, accuses no one, and predicts nothing. It is paper, filed in time, asking a file to tell the truth about itself.",
 "What remains is the decision every packet in this series eventually faces: when, and whether, it actually gets filed.",
], [C("Decide, with Ms. Adler, while deciding is still early", "packet_file_choice",
      note="June does not move. Everything in this office still can.")]),

N("packet_file_choice", 44, "File It, Hold It, or Say It", [
 "Three ways, laid out honestly. One: file the packet now — in writing, with the agency and the court, weeks before " + fmt(S113_ASFA) + " — so the exception exists in the file the filing decision will be made from, and the pre-date review can act on it. Two: hold it and file it at the pre-date review itself — later, thinner, but still paper. Three: raise it orally at the review — your voice, her voice, a transcript, and no exhibits beneath any of it.",
 "\u201cMy advice is the first,\u201d Ms. Adler says. \u201cIt is also, in the end, your case and your decision. But understand what each week of holding costs: decisions inside agencies get drafted before they get announced, and paper that arrives after a draft hardens has to move furniture. Paper that arrives before is just — furniture, already in the room.\u201d",
], [C("File the written exception packet now, with counsel, before the fifteen-month date", "packet_filed_scene",
      setFlags=["packetFiled"], cash=-8, requiresFlags=["packetBuilt", "recordsRequested"],
      addHidden=["Written exception packet filed with agency and court before the 15-month date"],
      note="Filed, stamped, copied — the exceptions now exist in the file the June decision will be made on."),
    C("Hold the packet and file it at the pre-date review", "packet_held_scene",
      setFlags=["packetHeld"],
      note="The binder stays assembled, in Ms. Adler's office, gaining nothing but age. Reviews, unlike wine, do not reward this."),
    C("Raise the exceptions orally at the review instead", "oral_scene113",
      setFlags=["oralRaised"],
      note="Two voices, clearly heard, with the binder closed on the conference table between them.")]),

N("packet_filed_scene", 46, "Filed, Stamped, Copied", [
 "The packet goes in on a weekday morning, with a stamp and a copy for your folder, and the ordinary anticlimax of important paper: a clerk, a receipt, a binder that is now a filing. Ms. Beam, at your next check-in, mentions it without edge: \u201cI saw the packet. The letter — I hadn't seen the letter stated that way.\u201d It is not agreement. It is the acknowledgment, from inside the circle, that the circle is now documented in both its halves.",
 "The case, meanwhile, is still a child's ordinary weeks, and you keep them: visits, work, the folder, the bus. Filing is an event. The weeks after it are the medium it has to survive in.",
], [C("Keep the visits, the work, and the routine exactly as they are", "month14_work",
      note="The packet is filed. June will do what June does — from paper, this time, that includes yours.")]),

N("packet_held_scene", 46, "The Binder, Waiting", [
 "The decision is made and noted: the packet will be filed at the pre-date review. The binder sits in Ms. Adler's office, its tabs in order, its letter crisp — assembled, checkable, and, for now, legally indistinguishable from a rumor, because an unfiled packet exists only where it sits.",
 "\u201cWe will file it in the room,\u201d Ms. Adler says. \u201cI want you to understand what that timing means. The agency's internal drafting will already have happened. We will not be furnishing a room. We will be asking a furnished room to make space — which rooms do, sometimes, for excellent paper, at a price in persuasion that early paper never has to pay.\u201d",
 "You keep the visits, the work, the routine. Your half of the file stays complete. The other half stays, for now, a binder on a shelf.",
], [C("Prepare, with Ms. Adler, to file it the moment the review opens", "month14_work",
      note="If the record will receive it late, it will at least receive it whole.")]),

N("oral_scene113", 46, "Saved for the Room", [
 "The decision is made and noted: the exceptions will be raised orally at the pre-date review. Ms. Adler prepares the statement with you, word by word, because if the record will hold only words, the words will at least be exact: the service, the silence, the letter, the circle, the date.",
 "\u201cUnderstand the medium,\u201d she says. \u201cA transcript preserves that we said it. Exhibits preserve what we said it about. Filing decisions are made from files. We are choosing to speak to a file in a voice it cannot keep.\u201d",
 "You keep the visits, the work, the routine. Somewhere in an office, a chronology with thin places sits in a drawer, unanswered by anything but a speech scheduled for June.",
], [C("Rehearse the statement once more, and keep the weeks clean", "month14_work",
      note="Exact words, exactly delivered, are still words. June will price the difference.")]),

N("month14_work", 48, "Month Fourteen, at Work", [
 "Month fourteen is mostly logistics, which is to say it is mostly the case: a shift change at work that threatens the Saturday visit, solved with a supervisor's signed schedule; a school form for Umar, signed and returned the same day; the residence's quiet, continued fact — a good room, for one person, that a child cannot live in.",
 "Umar's foster mother mentions, kindly, that the agency has asked about \u201cschedules in June.\u201d She does not know more than that, and says so. June is acquiring a shape in other people's calendars too. Yours has held its shape since April: a date, circled in pencil, with a binder under it — filed, held, or spoken, depending on the road you chose.",
], [C("Confirm the June dates in writing with everyone who needs them", "home_prep113",
      note="One more month where the paper and the life agree with each other.")]),

N("home_prep113", 49, "The Box Labeled UMAR'S ROOM", [
 "In the corner of the single room there is a box you have kept for a year, labeled in marker: UMAR'S ROOM. Inside: his books, the chess set's spare queen, curtains bought on sale in a month when hope was cheaper. It is not an exhibit. No tab in any binder claims it.",
 "It is included here because the packet, the letter, and the date are all, in the end, about the box: about whether a bureaucratic circle gets to decide how long a labeled box stays packed in a room a child cannot enter. The case will be decided on paper. The paper is about this.",
 "You tape the box shut again, gently, and go to sleep in the room that is waiting to stop being the barrier.",
], [C("Sleep, and face the agency's next letter in the morning", "agency_position",
      note="Envelopes from agencies have a weight you can identify before you open them. June's are arriving early.")]),

N("agency_position", 51, "The Agency's Draft Position", [
 "The letter arrives on agency letterhead, and it is almost the letter Ms. Adler predicted: as the case approaches fifteen months in care, the agency will make and document its filing decision at the fifteen-month date — " + fmt(S113_ASFA) + " — on the case record. A second paragraph notes that permanency will also be addressed at the pre-date review, including, if the evidence supports it, the goal.",
 "\u201cOn the case record,\u201d Ms. Adler says, reading it over your shoulder. \u201cThat phrase is the whole spring, in their words this time. The record currently contains your completed plan, the program's letter, and — depending on a decision made in April — a filed packet, a held binder, or a speech we have not given yet. A decision made on the record can only use what the record holds.\u201d",
 "The review is days away. What the record holds is about to stop being a planning question.",
], [C("Ask what the pre-date review can actually do, in order", "supervisor_read",
      note="Reviews do specific things in a specific order, she says. Ours has two jobs: answer the date, and break the circle. In that order.")]),

N("supervisor_read", 53, "A Cold Reader, Upstairs", [
 "Personnel is weather in this system, and this month the weather is a supervisor you have never met, who will sign the filing decision and who reads files the way supervisors read them: cold, complete, and without a single memory of any meeting you have ever attended.",
 "This is the moment the spring was quietly designed around. A cold reader cannot be told what everyone in the case happens to know about the circle. She can only read. If the packet is in the file, she reads a services gap with exhibits and a letter with a condition in it. If it is not, she reads a chronology that calls housing a barrier, a summary that calls it your open goal, and a date that says fifteen months.",
 "\u201cFiles outlive the people who remember the case,\u201d Ms. Adler says. \u201cJune's reader is the proof. Our remaining work is to make sure the paper in the room is the paper we chose.\u201d",
], [C("Go home — a call from the foster home is waiting in your log to return", "foster_call113",
      note="Cold readers are not enemies. They are the audience every filed page was always written for.")]),

N("foster_call113", 54, "A Call from the Foster Home", [
 "Umar's foster mother calls about a practical matter — a school trip form, a signature, the ordinary plumbing of a placed child's week — and handles it with the practiced kindness of a woman who has learned which parts of a case are hers to carry. The form gets signed. The week gets plumbed.",
 "\u201cHe asked the house question again,\u201d she says, at the end, not unkindly. \u201cI told him what you told him. Dates, and grown-ups working on them.\u201d Two households, one sentence, agreed across a case file: some coordination in this system happens entirely without forms, and works \u2014 and the rest of it, the part June decides, happens only with them.",
], [C("Note the call and the form in the folder, dated, and turn to the review notice", "review_notice113",
      note="Even the un-formal parts get a dated line now. The habit no longer feels like a habit; it feels like the case's other language.")]),

N("review_notice113", 55, "The Review Notice", [
 "The notice for the pre-date review arrives with its date — days before " + fmt(S113_ASFA) + " — and its paperwork: the agency's pre-review summary. Your progress is reported fairly, in the summary's careful language: all goals complete except housing; housing, barrier; visits, warm and consistent.",
 "What the summary does not contain is the circle. It describes housing as your unfinished goal and the date as the case's approaching fact, in separate paragraphs, the way summaries keep related truths in separate rooms so they never have to meet.",
 "The review is where paragraphs meet. It is also, Ms. Adler reminds you on the phone, the last room in which the packet and the letter can be put in front of the date together — before the date stops being upcoming and becomes arrived.",
], [C("Prepare the review the way Ms. Adler prepares everything: from the file outward", "review_prep113",
      note="File outward: packet, letter, stamps, record. The room will supply the rest.")]),

N("review_prep113", 57, "The Night Before the Review", [
 "Preparation is assembly, one last time: the filed packet's stamped copy — or the held binder, or the oral statement's exact words — the program's letter, the stamped applications, the school note, the visit write-ups. The folder by the door. The bus fare in your coat.",
 "Ms. Adler's last instruction is about order, because order is argument: \u201cThe packet first — what the file documents about the service and the reason. The letter second — what the system itself says it needs. The ask last, in one sentence: document the exceptions, and set the date the letter is waiting for. Rooms break circles in the order they are handed the pieces.\u201d",
 "You sleep as well as review eves allow, in the room with the labeled box.",
], [C("Take the folder, and go to the review", "review_circle",
      note="Fourteen months of paper, carried by the person it is about, into the room it was written for.")]),

N("review_circle", 59, "The Review Before the Date", [
 "The review is longer than the last one, and " + fmt(S113_ASFA) + " is named in it plainly, by the judge, on the record: fifteen months, days away. Your progress is reported, fairly again. The agency states that its filing decision will be documented at the date, on the record. Placement continues, today, as it was always going to today.",
 "Then the judge turns to the housing paragraph — the barrier, in the summary's word — and to whatever your spring has put in the file about it. What happens next depends, with a precision this scenario has been honest about since April, on what your choices actually filed, held, or saved for your voice.",
], [C("Put the filed packet and the program's letter before the court together — the exceptions, documented, and the date the letter is waiting for", "end_win113",
      requiresFlags=["packetFiled", "programLetter", "housingDoc"],
      note="Packet first, letter second, ask last, in one sentence — the order rehearsed the night before."),
    C("File the held packet now, in the room, and ask that it be received before the date", "late_filed_scene",
      requiresFlags=["packetHeld"],
      note="Whole paper, late arrival: the room is asked to make space for a binder it should have met in April."),
    C("Let the review close on the summary — the date will do what it does", "filing_eve",
      requiresNoFlags=["packetFiled", "packetHeld"],
      note="A warm, brief review, silent on the only questions June asks."),
    C("Hear the agency's goal request, unanswered by any filed paper", "end_goalchange",
      requiresNoFlags=["packetFiled", "packetHeld"],
      note="A goal, proposed in a room where the only exhibits are a summary and a date.")]),

N("late_filed_scene", 63, "Filed Late, in the Decision's Window", [
 "The review receives the packet — whole, checkable, and late. The court does not rule from the bench on the filing decision; it continues the documentation of that decision by days, into the window after " + fmt(S113_ASFA) + ", and the packet, filed " + d113(63) + ", is in the file when the agency documents its decision inside that window.",
 "Late is not early, and this scene will not pretend otherwise: the agency's draft position had already hardened, the date had already struck, and the packet had to move furniture in a furnished room. But furniture, moved by excellent paper in a window a court held open, is still moved.",
 "What the decision document does with a packet it met late is June's last lesson, and it differs from what it does with one it met in April — by exactly the width of the word partial.",
], [C("Read the documented decision when it arrives", "end_late",
      note="Stamped, filed, days after the date. In this system, days are a currency and this packet spent them.")]),

N("filing_eve", 60, "The Week the Date Arrives", [
 "The last days run on rails laid in April. A visit, kept. A chess game, lost honestly. The binder — unfiled, or never assembled into the room — sits where it sits. There is nothing left to build, which is itself the lesson this scenario has been teaching since the program's envelope: by the week of a date like this, the case is the record, and the record is finished being written by everyone.",
 "Ms. Adler calls the night before. \u201cWhatever tomorrow documents,\u201d she says, \u201cremember what it is. A filing decision. Not a verdict on you, not a hearing, not an ending of anything except a question about a petition. Umar's case goes on either way, and so do you.\u201d",
], [C("Sleep, as well as a person can, and let the date come", "filing_day",
      note=d113(61) + ". Fifteen months, to the day the count runs from.")]),

N("filing_day", 61, "The Fifteenth Month", [
 fmt(S113_ASFA) + " \u2014 computed in this story as it is computed in the law: fifteen months from the Monday Umar was placed, " + fmt(S113_ENTRY) + ". The agency's filing decision is documented today, on the record the spring built.",
 "There is no courtroom drama in this scene, because filing decisions rarely have any. There is a file, a cold reader's review of it, a decision, and a document that records the decision and its reasons. What those reasons can honestly be depends \u2014 as Ms. Adler said in April, as the agency's own letter said in its own words \u2014 on what the record holds: a completed plan, a barrier in a summary, a circle nobody filed an answer to.",
], [C("Read the documented decision when it arrives", "end_undocumented",
      note="The date arrives at a file that was never handed the documents that answer it.")]),

N("end_win113", 66, "Ending \u2014 Documented: The Goal Stays Home (PARTIAL)", [
 "The decision document, arriving days after the review, does the two things the packet was built to make possible, and it does them in writing. First: the agency documents the exceptions in the case plan — the file does not document the housing-assistance service the plan identified as necessary for Umar's safe return, and a compelling reason is documented that filing a termination petition would not serve him — and no petition is filed at the fifteen-month date. The goal stays what it has always been: reunification.",
 "Second — and this is the circle, breaking on paper — the court sets the return timeline the packet asked for: a return date, named and dated, inside the window the program's letter stated. The letter goes back to the program with the date on it. The unit's approval, the program confirms, proceeds on that schedule: the occupancy the circle was withholding, unlocked by the date the circle was demanding, each condition met by the other's document.",
 "Umar sleeps tonight where he slept last night. Read the next debrief before you call this anything. Then call it what it is.",
], ending=True, debrief=[
 "WHAT THE RECORD HELD (the hidden record, revealed): A file with both halves present. Your half: every plan goal complete but housing, visits kept, a year of stamped applications proving the waiting was the list's. The system's half, documented by your spring's asking: a plan that identified housing assistance as necessary, a chronology that does not document it as provided, and a program letter — confirmed by its author — stating on its face that a unit could be approved once a return date within sixty days existed. Assembled as a written exception packet and filed, with counsel, before " + fmt(S113_ASFA) + ", so that a cold reader, and then a court, met the services gap, the compelling reason, and the letter in one binder, in time.",
 "THE LAW UNDER THIS PATH \u2014 AND THE LABEL: At 15 of the most recent 22 months, the agency is generally to file a termination petition UNLESS an exception is documented: (i) the child is being cared for by a relative, (ii) a documented compelling reason that filing would not serve the child, or (iii) the agency has not provided services it identified as necessary for the child's safe return (42 U.S.C. \u00a7 675(5)(E)). This route built (ii) and (iii) together, exactly as the statute's discipline requires: documented, in the case plan, before the date. The route to the file began with the record released on request (55 Pa. Code \u00a7 3130.44(d)) and counsel throughout (42 Pa.C.S. \u00a7 6337). Label this win honestly \u2014 it is PARTIAL: the packet buys the documented exceptions and the goal stays reunification; a return date is set and a unit's approval proceeds on it \u2014 but Umar is still placed at this scenario's curtain, reunification itself happens, if it happens, in a later chapter this scenario does not depict, and no hearing on any petition was held or decided, because there is no petition.",
 "WHAT NO STRATEGY CONTROLS: A different cold reader could have weighed the same packet and filed anyway, turning the documented exceptions into arguments for a harder room; the program's unit could have been lost to its own list in the interval; a judge less willing to set a date on a letter's terms leaves the circle documented but unbroken. Workers, supervisors, judges, programs, and luck all hold pieces of this ending. What your choices controlled was narrower and real: whether, when the date arrived, the file documented the reasons it should not strike — and whether the letter that could break the housing circle was in the room where dates are set, before the date ran out.",
]),
N("end_late", 66, "Ending \u2014 Filed Late, and It Landed (PARTIAL)", [
 "The documented decision, arriving inside the window the court held open, engages the packet it met late — and lands, in part. The exceptions are documented in the case plan, on the packet's exhibits: the services gap is entered as documented, the compelling reason is noted, and the agency does not file a petition on the strength of a date its own file could not survive being read aloud. The goal stays reunification.",
 "What late cost is itemized in the same document's silences. No return date is set in this decision: the program's letter, answered weeks after it could first have been answered, must be taken up at the next review, with the unit's place on the program's schedule re-confirmed rather than proceeding. The circle is not broken in this ending. It is documented, conceded, and scheduled — which is more than undocumented circles get, and less than broken ones.",
 "Umar's box stays packed a while longer, in a room the file now correctly describes as a barrier the system built. Correct descriptions, filed late, still change what happens next. They just change it next.",
], ending=True, debrief=[
 "WHAT THE RECORD HELD (the hidden record, revealed): The same packet as the early path \u2014 the same tabs, the same letter, the same stamps \u2014 received after the agency's position had drafted and after " + fmt(S113_ASFA) + " had struck, inside a documentation window a court continued by days. It was enough to be engaged, documented, and acted on for the filing decision. It was not early enough to be in the room when the return date could have been set alongside it, and that difference \u2014 days, in a case of months \u2014 is the entire distance between this ending and the broken circle.",
 "THE LAW UNDER THIS PATH: The exceptions (42 U.S.C. \u00a7 675(5)(E)) are record-dependent and this record, once the packet landed, documented two of them — services identified and not documented as provided, and a compelling reason documented in the case plan. They speak to the filing decision, which is all that was decided here; a petition, had one been filed, would still have required proof by clear and convincing evidence at a hearing this scenario does not depict. The record itself came from the verified route — released on request (55 Pa. Code \u00a7 3130.44(d)), assembled with counsel (42 Pa.C.S. \u00a7 6337). Label this ending PARTIAL, twice over: the filing was answered, and the circle was not broken \u2014 the goal survives, the date does not yet exist, and the program's unit waits on a review still to come.",
 "THE HONEST PART: Late paper is this system's most common tragedy and its most survivable one: the packet was true in April and true in June, and only its timing was negotiable — which is to say, only its effect was. A reader who refused the late filing outright, a court that had not continued the window, a program slot lost in the interval: any of them demotes this ending without Farida changing a thing. What her choices bought, even late, was that the exceptions entered the file as exhibits instead of arriving as a parent's memory against a chronology's silence. Memory loses to dates. Exhibits, even late ones, have to be answered.",
]),
N("end_undocumented", 66, "Ending \u2014 The Date Strikes, Undocumented", [
 "The agency's documented decision arrives by mail, and it is brief in the way of decisions that were never really contested: the child has been in care fifteen of the most recent twenty-two months; the agency will file. Your progress is noted, fairly, in a paragraph. Housing is listed as the open goal — your open goal, in the summary's grammar — with the circle nowhere in the document, because the circle lived in a letter nobody filed and a chronology nobody quoted.",
 "Nothing in the decision is cruel, and no one in it is a villain. It is a date, doing what dates do to files that were never asked to answer them — and a housing barrier, described for fifteen months as a mother's unfinished task, completing its transformation into the reason her rights are now petitioned against.",
 "Ms. Adler puts the decision in your folder, on top. \u201cThe packet still exists,\u201d she says. \u201cEverything in it is still true, and the case it can still help is the harder one that starts now. Paper filed late still files. It just files into a different case.\u201d",
], ending=True, debrief=[
 "WHAT THE FILE HELD (the hidden record, revealed): A completed plan, fairly reported, and an unanswered file: no record request that surfaced the plan's housing-assistance language, no chronology read for its silences, no packet assembled or filed, and a program letter — the system stating its own condition in its own words — that never became an exhibit in any room. The services gap happened; the circle happened; both are in this debrief because they were in your life. Neither entered the file as a document, and a filing decision made on the file could not see them. The date did not defeat an argument. It arrived where no argument had been filed.",
 "THE LAW UNDER THIS PATH: At 15 of the most recent 22 months, the filing the federal law generally directs (42 U.S.C. \u00a7 675(5)(E)) proceeded, with none of its three documented exceptions established in the record \u2014 not relative care, not a documented compelling reason, and not the services exception, which is record-dependent and was never documented. A petition is still only a petition: the agency would have to prove it by clear and convincing evidence at a hearing this scenario does not depict, and counsel (42 Pa.C.S. \u00a7 6337) and your own record, released on request (55 Pa. Code \u00a7 3130.44(d)), remain available for the case that now follows. Nothing about grounds has been decided by anyone.",
 "THE HONEST PART: Dates do not grade effort, and this ending must not be read as one: you completed everything the plan asked that a person can complete alone, and the one goal you could not complete alone was completed against you, as a filing. Another worker who quoted the letter herself, a supervisor who asked what the file documented about assistance, a lawyer who circled the date in February instead of April \u2014 the same luck and people run through every ending of this scenario. The difference here is only that the spring's assembly never reached a file, and paper, unlike memory, cannot be filed retroactively into a decision already documented.",
]),
N("end_goalchange", 62, "Ending \u2014 The Goal Changes on a Thin Record", [
 "The agency's goal request is argued from the summary, and the summary is the only paper arguing: fifteen months approaching, one goal open, housing unresolved. Against it there is no packet, no letter in evidence, no chronology quoted \u2014 only your voice, accurate and unaccompanied, explaining a circle the file describes as a barrier.",
 "The order changes the goal. Umar's permanency goal is no longer reunification; the agency is directed to pursue the new goal, and the case's machinery — its visits, its reviews, its summaries — re-aims itself accordingly, politely, in the weeks that follow. The housing circle does not break. It becomes, in the new goal's grammar, beside the point: the unit that needed a date will simply never be asked for one.",
 "Outside, Ms. Adler does not dress it up. \u201cGoals are changed on records,\u201d she says. \u201cOurs was a summary and a date. Theirs was the same summary and the same date, read in the direction summaries point. The packet would not have guaranteed anything. It would have made them argue against documents. Arguing against documents is harder, and sometimes that is the whole margin.\u201d",
], ending=True, debrief=[
 "WHAT THE FILE HELD (the hidden record, revealed): A thin record in the precise sense: a fair summary of a strong parent, an open housing goal described as hers, an approaching date — and none of the documents that re-describe either fact. No exception packet was filed (or held, or assembled from the record), the program's letter never entered evidence, and the chronology's silence about housing assistance was never read aloud by anyone. The goal was changed on what was in the room, and what was in the room was a summary.",
 "THE LAW UNDER THIS PATH: A goal decision at a permanency review is made on the record before the court, and this record contained no documented exception under 42 U.S.C. \u00a7 675(5)(E) for the court to weigh against the approaching date \u2014 no documented compelling reason, no documented services gap \u2014 although both existed in the world and in a folder. The filing date itself, " + fmt(S113_ASFA) + ", still arrives on its schedule, and a petition, if filed under the new goal, would still require proof by clear and convincing evidence at a hearing this scenario does not depict. Counsel (42 Pa.C.S. \u00a7 6337) can still request the record (55 Pa. Code \u00a7 3130.44(d)) and build, for the harder proceedings ahead, the documentation this spring was for.",
 "THE HONEST PART: This is not an ending about a mother who failed to house her son. It is an ending about a system that described a queue as a character trait for fifteen months and then changed a child's goal on the strength of its own description — while the documents that corrected the description sat, true and unfiled, in a folder and a binder. A different judge could have asked for the letter unprompted; some do. This one weighed what was filed. The record from here is still being written, and the packet \u2014 assembled, whenever it is assembled \u2014 will be read by the next room, which is a harder room, and will need it more.",
]),
]
assert len(s113_nodes) == 40, len(s113_nodes)
assert sum(1 for n in s113_nodes if n.get("ending")) == 4

s113_meta = {"title": "The First 90 Days",
 "subtitle": "Scenario 113 \u2014 The Unit That Needed a Date (a fictional composite)",
 "startDateISO": "2026-04-03", "startNode": "start", "startCash": 170,
 "tier": "Complex",
 "summary": "Month 13: every goal complete but housing \u2014 and housing waits on a return date the agency won't set until housing exists, while the 15-month date walks toward both."}

s113_win = {
 "start": "Go to the meeting \u2014 and bring the folder, as always",
 "folder_audit113": "Take the audited folder to Ms. Adler's office",
 "housing_office": "Open the program's envelope at the table before you leave",
 "program_letter": "Decide what to do with a letter like this: keep the original safe, or carry it loose",
 "letter_after": "Get a dated copy made for Ms. Adler, and go to the agency meeting first",
 "agency_meeting": "Ask her to note the letter itself in the file \u2014 not just the conversation",
 "counsel_meet113": "Sit down, and ask her to say the exceptions slowly",
 "records_beat113": "Sign the written request for the complete record this week",
 "file_review113": "Mark every housing line \u2014 yours and theirs \u2014 and ask what the pattern proves",
 "housing_service_read": "Read the chronology's silences closely, month by month, before assembling anything",
 "chronology_silence": "Turn to tab two \u2014 your applications, and their stamps",
 "waitlist_stamps": "Assemble the dated application copies into one stamped set for the packet",
 "stamps_after": "Call the program and confirm the letter, on the log",
 "program_call": "Log the call, file the log page behind tab three, and look at the circle whole",
 "circle_diagram": "Ask what tab four \u2014 the compelling reason \u2014 needs from your life, not your file",
 "umar_visit": "Write the visit up in the folder that night, dated",
 "umar_school": "File the note, and turn to the packet's assembly",
 "packet_plan": "Assemble it from the documents only \u2014 every entry checkable",
 "packet_contents": "Sign the packet's assembly page, and face the filing decision",
 "packet_draft": "Decide, with Ms. Adler, while deciding is still early",
 "packet_file_choice": "File the written exception packet now, with counsel, before the fifteen-month date",
 "packet_filed_scene": "Keep the visits, the work, and the routine exactly as they are",
 "month14_work": "Confirm the June dates in writing with everyone who needs them",
 "home_prep113": "Sleep, and face the agency's next letter in the morning",
 "agency_position": "Ask what the pre-date review can actually do, in order",
 "supervisor_read": "Go home \u2014 a call from the foster home is waiting in your log to return",
 "foster_call113": "Note the call and the form in the folder, dated, and turn to the review notice",
 "review_notice113": "Prepare the review the way Ms. Adler prepares everything: from the file outward",
 "review_prep113": "Take the folder, and go to the review",
 "review_circle": "Put the filed packet and the program's letter before the court together \u2014 the exceptions, documented, and the date the letter is waiting for",
}

if __name__ == "__main__":
    scen112 = build(s112_meta, s112_nodes, S112_START)
    scen113 = build(s113_meta, s113_nodes, S113_START)
    print("112 emit:", emit(scen112, 112, "The Empty Months",
        "This scenario depicts a grandmother caring for her two grandchildren as a kinship caregiver while her caregiver approval and payments are delayed for months, told through stamped copies, call logs, a case chronology, and a permanency review. There is no graphic content. Players may skip any scene or use the quick exit at any time.",
        S112_START))
    print("113 emit:", emit(scen113, 113, "The Unit That Needed a Date",
        "This scenario depicts a mother in month 13 of her son's foster-care placement whose last open plan goal is housing, told through applications, a housing program's letter, a case record, and a permanency review ahead of the federal 15-of-22-months filing date. There is no graphic content. Players may skip any scene or use the quick exit at any time.",
        S113_START))
    p112, c112, f112 = walk(scen112, s112_win, "end_win")
    print(f"112 WIN WALK: nodesVisited={len(p112)} endCash={c112} flags={f112}")
    print("  path:", " -> ".join(p112))
    p113, c113, f113 = walk(scen113, s113_win, "end_win113")
    print(f"113 WIN WALK: nodesVisited={len(p113)} endCash={c113} flags={f113}")
    print("  path:", " -> ".join(p113))
    print(f"112 ASFA arithmetic: entry {fmt(S112_ENTRY)} + 15 calendar months = {fmt(S112_ASFA)} (not depicted; outside window)")
    print(f"113 ASFA arithmetic: entry {fmt(S113_ENTRY)} + 15 calendar months = {fmt(S113_ASFA)} = start {fmt(S113_START)} + {(S113_ASFA - S113_START).days} days = dayOffset 61 (filing_day node)")
