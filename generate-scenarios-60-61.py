#!/usr/bin/env python3
"""Generator for Scenarios 60 and 61 of 'The First 90 Days' (Hard tier).
Single source: emits scenario-N.json, scenario-N-script.md and strategy-N.md
for each scenario, so all three match node-for-node / walk-for-walk by
construction. Every kicker and every in-body calendar date is computed from
startDateISO + dayOffset via datestr(); no date is hand-typed in the data.
Validation runs at the end and must pass (asserts) before the run is clean."""
import json, os, re
from datetime import date, timedelta

OUT = os.path.dirname(os.path.abspath(__file__))

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
             "choice \u2014 the player does not see it when it happens. `REQUIRES FLAG: name` means the choice "
             "is only available if that flag was set earlier; `REQUIRES NO FLAG: name` means it is only "
             "available if that flag was never set. `NOTE:` is text shown to the player right after choosing.")
    L.append("")
    L.append(f"Start date: {fmt(start)}. Day offsets are days since the scenario's start date. Tier: Hard.")
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
                    ann.append(f"cash {c['cash']:+d}")
                if c.get("setFlags"):
                    ann.append("FLAG: " + ", ".join(c["setFlags"]))
                if c.get("addHidden"):
                    ann.append("; ".join("HIDDEN + " + h for h in c["addHidden"]))
                if c.get("requiresFlags"):
                    ann.extend("REQUIRES FLAG: " + fl for fl in c["requiresFlags"])
                if c.get("requiresNoFlags"):
                    ann.extend("REQUIRES NO FLAG: " + fl for fl in c["requiresNoFlags"])
                suffix = f"  _({'; '.join(ann)})_" if ann else ""
                L.append(f"- {c['text']} \u2192 **{c['next']}**{suffix}")
                if c.get("note"):
                    L.append(f"  - NOTE (shown after choosing): {c['note']}")
    path_m = os.path.join(OUT, f"scenario-{num}-script.md")
    with open(path_m, "w") as f:
        f.write("\n".join(L) + "\n")
    return path_j, path_m

# =====================================================================
# SCENARIO 60 \u2014 The New Worker
# Start Monday, June 1, 2026. Silas placed ~8 months before the story
# (placement predates the story; no 'removed' flag).
# =====================================================================
S60_START = date(2026, 6, 1)
assert S60_START.strftime("%A") == "Monday"
def D60(off):
    return fmt(S60_START + timedelta(days=off))

s60_nodes = [
N("start", 0, "The Goodbye Letter", [
 "You are Marta. Your son Silas is nine, and he has been in foster care for eight months \u2014 long enough to have a second geography: a second bedroom, a second school route, a visit room whose clock you know by heart. Your case is in its middle: a parenting program completed, screens passed, visits kept, a plan that is mostly green ink and forward motion.",
 "Today's mail changes the cast without changing the case. Ms. Renshaw, your caseworker since the first month \u2014 the one who watched you finish the program, who knows which screen was rescheduled and why \u2014 is leaving the agency. Her letter is kind and two paragraphs long. A new worker, Mr. Wilkes, will take the case. He will receive, the letter says, a summary of your file.",
 "A summary. Eight months, compressed by a departing hand into the pages a stranger will meet you through. Everything in this scenario follows from a plain fact of this system: when the worker changes, the file becomes the case \u2014 and you are one of the few people who knows what the file leaves out.",
], [C("Read the letter twice, then look at your own papers", "handover_note",
      note="Her last day is this week. His first day is next week. The summary travels between those two days without you in the room.")]),

N("handover_note", 2, "What the Letter Says, and Doesn't", [
 "The letter says what letters like it say: a new assignment, a new phone number, appreciation for your cooperation. It does not say what the summary says. It does not say whether the summary was written from the whole file or from the last report, or whether the certificates you handed Ms. Renshaw in the spring are attached to it or filed three folders away.",
 "Ms. Renshaw knew your case the way people know things: by having been there. Mr. Wilkes will know it the way files know things: by what survived the handoff, in writing, in order. Between those two kinds of knowing there is a gap, and gaps in this system do not stay empty. They get filled by whoever writes next.",
 "The question the next eight weeks will ask, in different rooms, is who does the filling: the summary, your memory \u2014 or your paper.",
], [C("Decide what your own record of this case actually looks like tonight", "binder_beat",
      note="Eight months of paper is either an archive or a pile. Tonight it gets to be one of them on purpose.")]),

N("binder_beat", 4, "The Kitchen-Table Archive", [
 "Your paper lives the way most parents' paper lives: some of it in a binder a parent mentor gave you in the second month, some of it in a shoebox, all of it real. The binder, when you keep it up, is formidable: the program certificate, the screen results with their dates, sign-in sheets, visit notes, every letter you ever sent, in date order \u2014 a parallel file, kept by the only person who attended every event in it.",
 "Keeping it current costs an evening and a little money: fresh copies, new tabs, the spring certificates filed where a stranger could find them in thirty seconds. The shoebox costs nothing tonight. It will charge later, in a different currency, at a worse moment.",
 "This is the earliest choice in the scenario, and it is the one whose weight lasts longest \u2014 because every later room will ask the same question: can you show it, now, in order?",
], [C("Bring the binder current tonight \u2014 tabs, copies, everything in date order", "binder_kept", cash=-10,
      setFlags=["binderKept"],
      addHidden=["Parent's binder \u2014 certificates, sign-in sheets and screen results kept in date order from month one"],
      note="An evening's work. The binder now answers questions in the order a file gets asked them."),
    C("Leave the shoebox as it is \u2014 you know what's in it, and that's what matters", "binder_loose",
      addHidden=["Parent's papers \u2014 loose collection; contents known to the parent, not organized for anyone else"],
      note="You do know. Knowing, in this system, is the half of proof that cannot be handed across a table.")]),

N("binder_kept", 6, "Date Order", [
 "By midnight the binder tells your case the way you would tell it if you had an hour and a calm room: program \u2014 completed, certificate, date. Screens \u2014 submitted, passed, dates. Visits \u2014 kept, notes, dates. Nothing in it argues. It simply declines to let your spring be summarized by anyone who wasn't there.",
 "You do not know yet which two pages of it will matter. Nobody ever does. That is what a binder is for: the pages you cannot predict, kept as carefully as the ones you can.",
], [C("Go to the first meeting with Mr. Wilkes", "first_meeting",
      note="You bring the binder, not because you expect trouble, but because bringing it has become the habit the case taught you.")]),

N("binder_loose", 6, "Mostly Remembered", [
 "The shoebox holds everything, the way a drawer holds everything: truly, and unfindably. The program certificate is in there, under the visit drawings. A screen result is in there, folded into a letter. If a question is ever asked slowly, with time to dig, you could answer it. Questions in this system are rarely asked slowly.",
 "You go to the first meeting the way most parents go: on time, cooperative, carrying your memory of your own case \u2014 accurate, complete, and impossible to hand to anyone.",
], [C("Go to the first meeting with Mr. Wilkes", "first_meeting",
      note="He will be working from a summary. You will be working from eight months of having lived it. Only one of those fits in a folder.")]),

N("first_meeting", 9, "Mr. Wilkes, Week One", [
 "Mr. Wilkes is courteous, prepared in the way a person can be prepared by a document, and clearly carrying more cases than the week has hours. He has your summary open. He walks the plan with you, line by line, the way a person reads a map of a town he has just moved to.",
 "Then two lines surface, spoken the way a summary speaks them \u2014 flatly, as facts. The parenting program, he says, is listed as still open; you will want to finish that. And a screen from the spring is listed as missed; the plan may need to account for it.",
 "You completed that program. Its certificate exists. You passed that screen; its result exists. In the room, in this minute, neither document exists \u2014 because existence, in this system, means in the file, in front of the person reading it. Mr. Wilkes is not doubting you. He is reading. That is the more dangerous problem.",
], [C("Note the two lines, word for word, before you answer them", "stale_detail",
      addHidden=["New worker's summary \u2014 two stale lines: completed program listed as open; passed screen listed as missed"],
      note="You write down his exact wording. Corrections later will be built out of the sentences they correct.")]),

N("stale_detail", 12, "Two Lines, Both Wrong", [
 "After the meeting you sit with the two lines. They are not lies, exactly; they are something more ordinary and harder to fight \u2014 stale paper. The program line was true once, months ago, before the certificate. The screen line may have been copied from a week when a result was still pending, before it came back passed. A summary written in a hurry, by a departing worker doing her best, carried both of them forward into a new worker's hands.",
 "Mr. Wilkes said he would 'check when he can.' You believe he means it. You also know what his week looks like, because he told you: a full caseload, inherited whole, every family in it a summary to someone.",
 "Your lawyer, Ms. Parr, has a saying for moments like this: a file corrects at the speed of paper, not at the speed of intentions. The two lines will sit in every report drafted from that summary until something in writing displaces them.",
], [C("Decide how the correction travels \u2014 this week, or on his schedule", "letter_choice",
      note="The lines are soft right now, the way fresh print is soft. Reports harden them. Time is a material in this case.")]),

N("letter_choice", 14, "The First-Week Letter", [
 "There is a move available this week, while Mr. Wilkes is still forming his picture of the case: a one-page status letter, from you, through Ms. Parr's office \u2014 what is complete, with dates; what is in progress; what you are asking to have corrected in the summary \u2014 with copies of the program certificate and the passed screen result attached.",
 "Sent in his first weeks, it is not an argument. It is orientation: the new reader of your case receives the primary documents before the summary sets. Sent later, the same letter becomes a dispute \u2014 your word against an established file. Same page. Different physics.",
 "The other option is patience: let him learn the case, as Ms. Renshaw did, by living it alongside you. It worked with her. She had eight months. The review is closer than that.",
], [C("Send the status letter this week, with the certificates attached", "letter_sent", cash=-6,
      setFlags=["letterSent"],
      addHidden=["Status letter with certificates \u2014 sent to the new worker in his first weeks, copied to counsel"],
      note="One page, two attachments, a copy for your own papers. The summary now has company."),
    C("Wait \u2014 let him learn the case the way Ms. Renshaw did", "letter_waited",
      note="A reasonable hope, held by many parents before you. His learning curve is now part of your case plan, whether the plan says so or not.")]),

N("letter_sent", 16, f"Sent, Copied, Dated", [
 f"Your letter is dated {D60(14)} \u2014 inside Mr. Wilkes's second week. Program: completed, certificate attached. Screen: passed, result attached. Everything else: in progress, on schedule, visits kept. It asks, in one closing sentence, that the summary be corrected to match the attachments.",
 "Ms. Parr files her copy. Yours goes in your papers. Somewhere in an agency inbox, a new worker now holds primary documents that are newer than his summary \u2014 which means the summary, from today, is no longer the freshest paper in the file. In a system run on paper, freshness is a form of authority.",
 "You have not won anything. You have done something quieter: you have made the stale lines expensive to repeat, because repeating them now means repeating them against attachments.",
], [C("Go on with the plan \u2014 visits, meetings, all of it", "reorder",
      note="The case continues the way cases do: the next piece of paper is already on its way to you.")]),

N("letter_waited", 16, "His Learning Curve", [
 "The weeks arrange themselves the way they arrange themselves for a new worker with a full caseload: visits supervised, meetings held, your cooperation noted \u2014 and every note written by a man whose map of your case is a summary with two wrong lines on it. He is not careless. He is new, and the file is what newness has to steer by.",
 "Nothing goes badly, exactly. That is the texture of this path: not a crisis, but a slow setting, like plaster \u2014 the summary's version of your spring becoming, report by report, the version everyone in the next room will have read before you arrive.",
], [C("Go on with the plan \u2014 visits, meetings, all of it", "reorder",
      note="Then the mail brings a piece of paper that shows you exactly what steering by that summary costs.")]),

N("reorder", 19, "The Assessment, Again", [
 "The letter from the agency is routine in tone and remarkable in content: an updated family assessment has been scheduled for you \u2014 the full assessment you already completed in the spring, with Ms. Renshaw, over two long appointments.",
 "Mr. Wilkes, when you call, is apologetic and precise about the reason: the copy in the file is a draft \u2014 unsigned, marked as a working copy. The completed version was never filed, or was filed somewhere the handoff didn't reach. Without a completed copy in the file, his instructions are to re-order it. The system does not doubt that you did it. The system simply cannot find the paper that says so, and in this system those are the same sentence.",
 "Redoing it costs what redoing costs: two appointments, time off work, the same questions answered again, and a new date in the file that will forever look later than the first one. Answering in writing costs a stamp: your completion certificate and the dated sign-in page from the spring appointments, attached to a letter asking that the file copy be replaced.",
], [C("Answer in writing \u2014 attach the completion certificate and the dated sign-in page", "attach_cert", cash=-4,
      addHidden=["Assessment \u2014 completion certificate and dated sign-in page sent in writing; draft file copy challenged"],
      note="Your spring, in attachments. The draft now has to compete with the finished thing it was a draft of."),
    C("Redo the assessment quietly \u2014 done is done, and arguing helps no one", "redo_assessment", cash=-30,
      addHidden=["Assessment \u2014 repeated at the parent's time and expense; original completion not asserted in writing"],
      note="Two appointments, a shift traded, the questions answered again. Cooperation, certainly. Also: a second date, waiting to be mistaken for the first.")]),

N("attach_cert", 22, "The Certificate Answers", [
 "The reply takes ten days and is three lines long: the assessment re-order is withdrawn; the certificate and sign-in page are accepted; the completed report will be located or reconstructed from the provider's copy and filed. Three lines. Underneath them, a principle of this whole series, working quietly: a document answered with a document.",
 "Mr. Wilkes adds, in his own hand at the bottom, that he has flagged the file copy as a draft. You believe him, and \u2014 this is the new habit the case is teaching you \u2014 you also keep his three lines, dated, in your papers. Belief and filing are not opposites. In this system, filing is what belief looks like when it plans to survive a staff change.",
], [C("Ask Ms. Parr what else the file itself would tell you, if you asked for it", "records_beat",
      note="Because one draft has now surfaced by accident. Files rarely contain exactly one surprise.")]),

N("redo_assessment", 22, "Twice, On Paper Once", [
 "You do the assessment again. The questions are the same questions; your answers are the same answers, given to a different chair. The new report, when it is filed, will carry this season's date \u2014 and nothing in its text will explain that an earlier, identical completion exists somewhere as an unsigned draft in a transferred file.",
 "You have been cooperative, and the file will say so. It will also, unless something else corrects it, tell every future reader a quieter falsehood: that this piece of your plan was completed months later than it was. Late, on paper, is a character trait in this system. It attaches to the person, not to the filing error that produced it.",
], [C("Ask Ms. Parr what the file itself would tell you, if you asked for it", "records_beat",
      note="Because the draft problem turned out to be real. Files rarely contain exactly one surprise.")]),

N("records_beat", 25, "Ask for the File Itself", [
 "Ms. Parr listens to the whole spring \u2014 the handoff, the two stale lines, the draft \u2014 and asks the question this scenario has been walking toward: 'What does the draft review report say?' The review is written from reports, and the next report is being drafted now, somewhere, from Mr. Wilkes's summary.",
 "You do not have to guess. A party may request the case record, and the material in it 'shall be released upon request' (55 Pa. Code \u00a7 3130.44(d)). The request is one page, in writing: the file, including the draft review report and the assessment copies. What it shows you, weeks before the review, is the exact text your correction has to answer \u2014 line by line, instead of rumor by rumor.",
 "The alternative is to prepare for the review from the meetings: from tone, from assurances, from what Mr. Wilkes seems to understand. Tone is not a document. The review will be conducted entirely in documents.",
], [C("Sign the written request for the record \u2014 draft report, assessment copies, all of it", "record_arrives",
      setFlags=["recordsRequested"],
      addHidden=["Case record \u2014 requested in writing, including the draft review report and assessment copies"],
      note="Signed, dated, copied. Whatever the draft says about your spring, you are about to be able to quote it."),
    C("Rely on the meetings \u2014 Mr. Wilkes is reasonable, and the file is the agency's business", "no_record",
      note="The file is the agency's business the way weather is a sailor's business: not yours to control, and entirely yours to be rained on.")]),

N("record_arrives", 29, "The Draft, With Template Lines", [
 "The packet arrives thick, and partly blacked out \u2014 some of that is the law working as written: released material may not include material that violates another person's privacy or is protected or made confidential by law (55 Pa. Code \u00a7 3130.44(f)). The redactions are not the story. The draft review report is.",
 "There they are, in report type, with the authority of print: the program, still open. The screen, still missed. And a template sentence about the assessment \u2014 carried from the draft copy's cover sheet, the kind of line that gets pasted into reports because it was pasted into the last one \u2014 describing a completion that never quite happened, in a case where it happened in the spring.",
 "A draft is a mercy, if you get to see it: every line in it is still soft enough to correct. Ms. Parr spreads it on her desk beside your papers. 'Now,' she says, 'we stop arguing with a summary. We correct a text.'",
], [C("Decide how the correction is delivered \u2014 in writing before the review, or in person at the next meeting", "correction_choice",
      note="The draft's deadline is the review itself. Corrections filed before it arrive as paper. Corrections spoken at it arrive as weather.")]),

N("no_record", 29, "Summaries of Summaries", [
 "Without the draft, you prepare from what you have: the summary's two lines, as Mr. Wilkes spoke them; Ms. Parr's notes; your own certain knowledge of your spring. You know the lines are wrong. What you do not have is their exact wording in the report the review will read \u2014 and corrections, like keys, only work when they are cut to the lock.",
 "Ms. Parr is honest about the shape of it: 'We can still object at the review. We will be objecting to sentences we are hearing for the first time, in a room that has already read them.' She opens a blank page in her file. Whatever correction gets made from here will be made at speaking speed, against print.",
], [C("Decide how the correction is delivered \u2014 in writing before the review, or in person at the next meeting", "correction_choice",
      note="You know a correction is needed. The question left is whether it will exist as a document before the room convenes.")]),

N("correction_choice", 33, "Correct It Where It Lives", [
 "Ms. Parr drafts the correction the way this scenario has taught you everything durable is drafted: one page per line. Line one: program \u2014 completed, certificate attached. Line two: screen \u2014 passed, result attached. Line three: assessment \u2014 completed in the spring, certificate and sign-in page attached; the file copy is a draft. Each line asks for one thing: that the report be amended to match its own attachments, before the review.",
 "Filing it \u2014 with copies to the agency and into the court file, weeks ahead \u2014 costs copies and a trip. Raising the same points at the next meeting costs nothing, and Mr. Wilkes, face to face, will very likely agree with every one of them. Agreement, in this system, has a half-life measured in days. A filed correction's half-life is the life of the case.",
], [C("File the written correction before the review, certificates attached", "correction_filed", cash=-5,
      setFlags=["correctionFiled"],
      addHidden=["Written correction \u2014 filed before the review with certificates attached, line by line"],
      note="Stamped, copied, in the court file before anyone drafts another sentence from the old lines."),
    C("Raise it at the next meeting instead \u2014 he has been fair in person", "correction_oral",
      note="He has. The meeting is in three weeks. The report drafting is this week. Sequence is a kind of evidence too.")]),

N("correction_filed", 35, "Filed, Not Just Said", [
 "The correction goes in with its attachments, and the system does the thing it does with filed paper: it routes it, stamps it, and makes the next writer reckon with it. The amended draft, when Ms. Parr sees it, has the three lines struck and rewritten \u2014 program completed, screen passed, assessment completed in the spring \u2014 each with a small, beautiful footnote: 'per parent correction and attachments.'",
 "Your spring now reads the same in every copy of the file. That sameness has a name in this scenario's title sense: continuity \u2014 except that nobody handed it to you. You manufactured it, one attachment at a time, and filed it where a stranger's summary used to be the only account.",
], [C("Meet Mr. Wilkes again \u2014 the second meeting", "second_meeting",
      note="He opens a file that now contains your paper at the front. Meetings read differently from the front of a corrected file.")]),

N("correction_oral", 35, "Said, Warmly", [
 "The meeting goes exactly as hoped, which is the problem's disguise. Mr. Wilkes listens, nods, turns his screen, and agrees: the program line is wrong, the screen line is wrong, the assessment is a draft-copy mix-up. 'I'll pass it along,' he says, and means it, and writes himself a note on the pad he uses for everything.",
 "Nothing is stamped. Nothing is filed. The correction now lives in a note on a busy man's pad, competing with forty other notes \u2014 and the report, which is drafted by a process and not by his memory, is already moving through the process.",
 "You leave with his goodwill, which is real, and without a document, which is also real. The review will weigh one of those. It is not the goodwill.",
], [C("Meet Mr. Wilkes again \u2014 the second meeting", "second_meeting",
      note="He remembers the conversation kindly. What the file remembers is a separate question, and files are what reviews read.")]),

N("second_meeting", 39, "The Second Meeting", [
 "The second meeting with Mr. Wilkes is a study in what paper does to a conversation. Where the file has been corrected in writing, he works from the corrected lines as naturally as he once worked from the stale ones \u2014 the map improved, so the driving improved. Where the correction was only spoken, he apologizes that the report 'may still show the old lines' and offers to speak to them at the review itself.",
 "He is, throughout, the same man: conscientious, overloaded, reading what the file gives him to read. This scenario has never been about whether he is a good worker. It is about what a good worker can do with a bad summary, and what a parent can put in front of him that outlasts the meeting.",
 "Silas's plan, underneath the paperwork, is unchanged and progressing: visits, school, the ordinary machinery of a case in its ninth month, waiting for a review to describe it.",
], [C("Keep the rest of the plan exactly as clean as it has been", "wilkes_checkin",
      note="Because the review reads the whole file, not only the three corrected lines. The rest of it should say what it has always said: kept, submitted, attended.")]),

N("wilkes_checkin", 42, "The Check-In Call", [
 "The weekly check-in call is four minutes long, and it is the most ordinary scene in this scenario \u2014 which is why it matters. Mr. Wilkes confirms the visit schedule, the next screen window, and the review date, reading each from the file in front of him.",
 "A month ago, that file would have given him two wrong things to confirm. Today, whatever your choices have put in it is what he reads back to you, in his flat, careful voice \u2014 the correction filed, or the apology repeated, or the stale lines still sitting where the summary put them. The call is a small preview of the review: the case, as the paper currently tells it, read aloud by the person who inherited it.",
 "You hang up knowing exactly which version of your spring will walk into the review room. The only remaining question is what you will carry in with it.",
], [C("Run the last weeks before the review exactly as planned", "visits_meanwhile",
      note="Visits, screens, meetings \u2014 the plan's ordinary weeks, run ordinarily, dated as they happen.")]),

N("visits_meanwhile", 43, "Visits, and Everything Else", [
 "The weeks before the review are the plan's ordinary weeks, and you run them the way you have run them all year: visits with Silas \u2014 a school project reconstructed at a visit-room table, a chapter book moving by installments \u2014 screens submitted when called, meetings signed. None of it is dramatic. All of it is dated, and dated is what files eat.",
 "It is worth pausing on the strangeness of your position: the strongest facts in your case are the ones nobody disputes, and the weakest are the ones you completed months ago, because completion is exactly the kind of fact a handoff loses. Doing a thing and the file knowing you did it are two separate achievements in this system, and the second one is yours alone to schedule.",
], [C("Prepare for the review with Ms. Parr", "review_prep",
      addHidden=["Compliance \u2014 visits kept and screens submitted while the file was being corrected"],
      note="Your recent record is clean in the lived sense and, page by page, in the filed sense too.")]),

N("review_prep", 50, "Ms. Parr Builds the Packet", [
 "You have had a lawyer throughout this case, as the law provides (42 Pa.C.S. \u00a7 6337) \u2014 and Ms. Parr, in the week before the review, shows you what counsel is for in a paperwork case: not eloquence, but inventory. She spreads the whole matter on her conference table in two piles.",
 "Pile one is the story the summary told: program open, screen missed, assessment doubtful. Pile two is your paper: the binder in date order, the first-week status letter with its certificates, the record packet with the draft report, the filed correction with its attachments. 'The review,' she says, 'is a contest between these two piles \u2014 except that only one of them is allowed to be surprised on the day.'",
 "She is equally plain about the limit: a packet does not decide a review. Judges and report writers read the same paper differently, and Silas's placement will turn on more than three lines. What the packet decides is narrower: which version of your spring the room starts from.",
], [C("Assemble the final packet, in date order, with copies for the court", "packet_assembly",
      note="Date order. The handoff, corrected by the person it was handed to.")]),

N("packet_assembly", 52, "Date Order, Again", [
 "The packet takes an evening: the goodbye letter, the summary's two lines as you noted them word for word, the status letter and its certificates, the assessment correspondence, the draft report beside the filed correction, the clean recent weeks. Copied, paginated, plain. It weighs almost nothing. So does a summary. Reviews, in the end, are decided by which light thing a room believes.",
 "Ms. Parr puts her copy in her trial bag. Yours goes in the binder \u2014 last pages, this month, where the next worker, if there ever is one, will find the whole story of how this file learned to correct itself.",
], [C("File the packet copies and go to the review", "review", cash=-5,
      addHidden=["Review packet \u2014 status letter, certificates, correction and record excerpts filed in date order"],
      note="Every page in it existed before the review was convened. That sentence is the packet's entire argument.")]),

N("review", 56, "The Review", [
 f"The review convenes on {D60(56)}. The report is read the way reports are read: as the case, in summary, by the people who were not there for any of it. The three lines arrive in their order \u2014 program, screen, assessment \u2014 and what happens next depends, with a precision this scenario has been honest about from its first letter, on what your choices put in the room before the reading started.",
 "Ms. Parr rises. The presentation she can make is the one your paper built: the full packet, a subset of it, or \u2014 if the paper was never assembled \u2014 your voice, explaining a spring that three documents could have explained without you saying a word.",
 "Choose the presentation the record you actually built can carry.",
], [C("Present the corrected record \u2014 binder, first-week letter, record packet, and the correction filed before today", "end_win",
      requiresFlags=["binderKept", "letterSent", "recordsRequested", "correctionFiled"],
      note="This presentation exists because four pieces of paper exist, in order, filed before the room convened."),
    C("Present the filed correction and answer the rest from your own papers", "end_partial",
      requiresFlags=["correctionFiled"],
      note="The correction is real and filed. What surrounds it is thinner \u2014 and the room can feel the thinness."),
    C("Present what paper you have \u2014 some of it dated, some of it assembled this week", "end_partial",
      note="Half a packet is an argument with missing premises. It still changes the room \u2014 just later, and at a higher price."),
    C("Explain it all yourself \u2014 you were there, and the truth should be enough", "end_worst",
      note="Your account is accurate in every detail. Accuracy, unattached, is the currency this room accepts least.")]),

N("end_win", 63, "Ending \u2014 Continuity, Supplied by You", [], ending=True, debrief=[
 f"WHAT THE FILE HELD (the record, revealed): At the review on {D60(56)}, the report's three contested lines were corrected on the record before they could be argued about \u2014 program completed, screen passed, assessment completed in the spring \u2014 each traced to its attachment: the binder kept in date order, the status letter sent in Mr. Wilkes's first weeks with certificates, the record packet obtained on request, and the written correction filed before the review. Mr. Wilkes confirmed the amendments from his own file. The case the review discussed was your actual case, because you supplied the continuity the handoff had dropped. Silas remains in foster care and the plan continues; no honest debrief will call that a finished story. What is finished is the false version of your spring, and it is finished in every copy of the file at once.",
 "THE PROCESS UNDER THIS PATH (described, keeping to this scenario's verified law): Every instrument here was an ordinary one. The case record was available on written request \u2014 it 'shall be released upon request' (55 Pa. Code \u00a7 3130.44(d)) \u2014 and its limits were honored rather than fought: released material may omit what violates another person's privacy or is protected or made confidential by law (55 Pa. Code \u00a7 3130.44(f)). Counsel's role was the one the law assigns from the start of a case (42 Pa.C.S. \u00a7 6337): not to invent facts, but to put the true ones \u2014 certificate, result, sign-in page \u2014 into the file in a form the next reader cannot miss. A worker change is not an error anyone was punished for; it is a routine event whose cost is normally paid, silently, by the parent's record. This time the parent paid it in copies and stamps instead, which is cheaper and leaves receipts.",
 "THE HONEST PART: A different supervisor could have contested the correction line by line; a different review could have weighed the spring differently even on a corrected record; Mr. Wilkes could have been less conscientious about amending his own summary, and no packet compels a worker to be gracious about being corrected. Workers, judges, and luck all held pieces of this outcome. And the deepest honesty is this: nothing you did brought Silas home today, because that was never what these three lines decided. What they decided was whether the next nine months would be built on your real record or on a stale copy of it. Outcomes in this system are not verdicts on a parent's worth \u2014 this one is a verdict on a filing system, and for once the filing system was yours.",
]),
N("end_partial", 63, "Ending \u2014 Reset, Then Repaired", [], ending=True, debrief=[
 f"WHAT THE FILE HELD (the record, revealed): The correction reached the review on {D60(56)} \u2014 but it reached it there, in the room, instead of in the file beforehand. The contested lines were argued rather than read as settled: the agency accepted some amendments on the spot, questioned the dating on others, and the review treated your spring as disputed territory rather than as either version's ground. The judge directed that the file be amended to match the certificates \u2014 going forward. The review itself, however, was conducted against the old summary, and its order reads accordingly: cautious, provisional, describing a parent whose progress is 'to be confirmed.' The repair is real. So is the reset it had to repair, in front of everyone, at speaking speed.",
 "THE PROCESS UNDER THIS PATH (described, keeping to this scenario's verified law): Nothing in this ending failed for lack of a right. The record was always requestable (55 Pa. Code \u00a7 3130.44(d)); counsel was always there to file the correction (42 Pa.C.S. \u00a7 6337). What was missing was sequence: paper that arrives at the hearing contests; paper that arrives before the hearing settles. A correction filed weeks ahead becomes the report's new text, and the review starts from it. The same correction, raised orally or assembled late, becomes an argument the report's writer gets to answer \u2014 and contested paper earns contested outcomes, here as everywhere in this series. The file going forward is correct, which matters for every future reader. The review that just happened was priced on the file as it stood when the room convened.",
 "THE HONEST PART: Be fair to the version of you that lands here: you did the program, passed the screen, completed the assessment, and then did the documentation work too \u2014 some of it, in the right order, under the pressure of a case in its ninth month and a worker still learning your name. Judges differ in how much late paper they credit without a fight, and this one credited it forward instead of backward, as many do. Workers rotate again; summaries get rewritten again; the corrected file you leave behind today is the summary the next stranger will meet Silas's case through \u2014 which means the work was not wasted, only mistimed. It bought the future a true file. It could not buy the present a settled one.",
]),
N("end_worst", 63, "Ending \u2014 Starting Over at Month Nine", [], ending=True, debrief=[
 f"WHAT THE FILE HELD (the record, revealed): At the review on {D60(56)}, the only complete account in the room was the summary's. Program: open. Screen: missed. Assessment: not completed. Your explanations were heard, and believed in the way unattached explanations are believed in rooms that run on exhibits \u2014 personally, and without effect. The stale lines did the thing stale lines do when nothing in writing displaces them: they hardened into findings, and the order built a plan on top of them. You are directed to complete the parenting program you completed in the spring, to submit to screening as if the passed result did not exist, and to undergo the assessment you already underwent. Month nine of your case begins, on paper, at the start of services you finished months ago.",
 "THE PROCESS UNDER THIS PATH (described, keeping to this scenario's verified law): This ending is not produced by a rule that says summaries win. It is produced by an absence: the instruments that answer a stale file were never taken up. The case record \u2014 which would have shown the draft report's exact lines while they were still correctable \u2014 was available on written request (55 Pa. Code \u00a7 3130.44(d)). Counsel could have filed a one-page correction with the certificates attached at any point in the eight weeks (42 Pa.C.S. \u00a7 6337). The certificates themselves existed the whole time, in a kitchen, in a pile \u2014 real, accurate, and never converted into the only form a review can use. No one in this ending acted in bad faith. A departing worker summarized in haste; a new worker read what he was given; a report copied the summary. Systems do not need villains to repeat their errors. They need only silence where the correction was supposed to be filed.",
 "THE HONEST PART: Let this debrief be as fair as the review was not: you did the work. The program was completed, the screen was passed, the assessment was sat through twice over in everything but paperwork, and any measure of you as a parent that starts from those facts starts from the truth. The injustice here is narrower and more mechanical than a judgment on your parenting \u2014 it is that a handoff taxed your record for its own incompleteness, and the tax was payable only in a currency nobody handed you: dated paper, filed early. A different worker might have caught the lines himself; some do, and some parents' files are rescued by exactly that luck. Yours was not, and luck is not a filing system. The corrected record can still be built \u2014 starting at the next meeting, in writing \u2014 and it will matter at the next review. It simply cannot retroactively un-harden the findings this one just made.",
]),
]

# =====================================================================
# SCENARIO 61 \u2014 The Expired Referral
# Start Monday, June 15, 2026. Referral sent day 0; 60-day validity
# expires day 60 = Friday, August 14, 2026 (asserted). Evaluation
# week begins day 63; evaluation completed day 66 (asserted).
# Cora placed before the story; no 'removed' flag.
# =====================================================================
S61_START = date(2026, 6, 15)
assert S61_START.strftime("%A") == "Monday"
assert S61_START + timedelta(days=60) == date(2026, 8, 14)
assert (S61_START + timedelta(days=60)).strftime("%A") == "Friday"
assert S61_START + timedelta(days=66) == date(2026, 8, 20)
def D61(off):
    return fmt(S61_START + timedelta(days=off))

s61_nodes = [
N("start", 0, "Two Steps, In Order", [
 "You are Tanya. Your daughter Cora is three, and she has been in foster care since before this story opens \u2014 long enough that the visit room has a chair she claims as hers and a shelf of board books she has memorized in the wrong order, proudly.",
 "Your plan has a spine, and the spine is sequential. Step A is a trauma-therapy evaluation: a specialist evaluation that must be completed first. Step B is the parenting program \u2014 and the program will not enroll you until Step A's evaluation is complete and its report is in. A before B. No exceptions, the plan says, because B is built on what A finds.",
 f"Today, {D61(0)}, your worker, Ms. Beam, tells you the referral for Step A has been sent. Sent is a good word. It is also, as this scenario will show, a word with a date attached to it \u2014 and a second date, sixty days later, that nobody in this conversation mentions.",
], [C("Ask what happens next, and when", "copy_choice",
      note="\u201cThey'll call you for intake,\u201d Ms. Beam says. \u201cThere's a waitlist \u2014 about five weeks.\u201d Five weeks, inside a sixty-day window nobody has named yet.")]),

N("copy_choice", 2, "Sent \u2014 But On What Paper?", [
 "A referral is a small machine with three moving parts: the date it was sent, the place it was sent to, and the date it stops being valid. Referrals expire \u2014 providers hold a place only so long, agencies resend only when asked \u2014 and the expiry date is the part of the machine nobody volunteers, because to everyone in the system except you, it is routine.",
 "You can ask for the referral copy in writing: the sent date, the provider, and the validity window, printed on the agency's own letterhead. It takes a request, a few days, and a small copying cost. Or you can take today's phone call as the record of itself \u2014 Ms. Beam's summary, her assurance, her memory of having sent it.",
 "Everything in this scenario is downstream of a choice that looks, today, like a choice about paperwork fussiness. It is actually a choice about which dates you will own in August.",
], [C("Ask for the referral copy in writing \u2014 sent date and validity window included", "copy_kept", cash=-3,
      setFlags=["referralDated"],
      addHidden=[f"Referral \u2014 copy in parent's hands: sent {D61(0)}, valid through {D61(60)}"],
      note="Three dates on one page: sent, received, expires. The third one is the one this whole case will turn on."),
    C("Trust the phone call \u2014 Ms. Beam sent it, and she'll be tracking it", "trust_call",
      note="She sent it. That part is true, and will stay true. What a phone call cannot do is testify in August about what it said in June.")]),

N("copy_kept", 4, f"Sixty Days, In Print", [
 f"The copy arrives, and there it is in the provider's own print: referral sent {D61(0)}. Valid for sixty days. The window closes {D61(60)}.",
 "You do the arithmetic the way parents in this system learn to do all arithmetic \u2014 against the waitlist. Five weeks of waiting lands in late July. The evaluation itself will be scheduled after that. The window and the wait are on a collision course so slow that nobody will call it a collision; it will be called, in a report, something else. By you.",
 f"You write the date where you will see it: {D61(60)}, in the diary you keep for visits and screens, with a line under it. A date in a diary is not yet a defense. It is the raw material defenses are made of.",
], [C("Go to intake at the evaluation provider", "intake",
      note="Intake is where the waitlist stops being a rumor and becomes a number with your name under it.")]),

N("trust_call", 4, "About Two Months", [
 "What you carry out of the phone call is a shape, not a date: the referral is sent, the waitlist is about five weeks, referrals are good for 'about two months,' someone will call. Every part of that is roughly accurate. Roughly accurate is a property that survives beautifully in conversation and not at all in reports.",
 "You write 'referral \u2014 June' in your diary, because June is what you know. June is a month. The machine runs on dates, and the difference between a month and a date is the entire plot of the summer you are about to have.",
], [C("Go to intake at the evaluation provider", "intake",
      note="At intake, at least, there will be forms \u2014 and forms, whatever else they do, have dates on them.")]),

N("intake", 7, "Name on the List, Date on the Wall", [
 "Intake is thorough and kind: history, insurance, the court paperwork, an hour of questions about Cora and about you. You are an appropriate referral, the intake worker confirms. Your name goes on the waitlist for an evaluation slot.",
 "Then the scheduling reality, stated conversationally, the way weather is stated: the wait to reach the top of the list is running about five weeks \u2014 and evaluations are booked in batches, with the next batch of appointments falling in the week that begins " + D61(63) + ".",
 f"You do the arithmetic, or you don't, depending on what paper you are holding. The batch week begins three days after {D61(60)} \u2014 the day a sixty-day referral, sent {D61(0)}, stops being valid. The waitlist and the window are going to arrive at the same week from opposite directions, and which of them the file blames will depend on who wrote what down, starting now.",
], [C("Write down the intake date, the wait, and the batch week before you leave the building", "middle_weeks",
      addHidden=["Intake \u2014 completed; waitlist about five weeks; evaluation batch week begins " + D61(63)],
      note="Your name, their dates, your handwriting. A small page that will be asked, later, to do a large job.")]),

N("middle_weeks", 14, "Everything Else Runs Clean", [
 "While Step A waits, the rest of your plan does not \u2014 and you run it the way you have learned to run everything in this case: visits with Cora twice a week, on time, with the installment book and the snack she negotiates for like a tiny union. Screens, random, submitted. Meetings, signed. Work shifts arranged around all of it by a manager who has quietly become one of the people who helps.",
 "At the team meeting you do not attend, your case is summarized in the ordinary way: strong engagement across the plan \u2014 and, on the Step A line, the single word 'pending.' Pending is a neutral word in June. Left alone in a file, month after month, it ferments. By a review, 'pending' can be poured into a sentence about a parent, and the sentence will not mention waitlists, windows, or batches at all.",
], [C("Keep every other line exactly this clean \u2014 and watch the Step A clock", "visit_clean",
      note="The plan's other lines are yours to control. Step A's line is controlled by a calendar and a queue. The review will read them as if both were yours.")]),

N("visit_clean", 21, "The Installment Book, Finished", [
 "Cora finishes the installment book at today's visit \u2014 she has been rationing the last pages for two weeks, a three-year-old's instinct for suspense \u2014 and demands a new one be started next time, which it will be, because the machinery of your visits is the part of this case that has never once failed to run.",
 "Your file, for anyone who reads all of it, is acquiring a shape this series keeps returning to: page after page of dated compliance, and one line standing still. Standing-still lines get explained at reviews by whoever holds the pen. There are two candidates for that authorship: the report writer, working from a chronology that will say 'A not completed,' or your paper \u2014 if you have built any, and if it arrives first.",
], [C("Start the new book next visit \u2014 and read the letter that came from the provider", "provider_letter",
      addHidden=["Compliance during the wait \u2014 visits kept, screens submitted, meetings signed; only the waitlisted evaluation outstanding"],
      note="The letter is one paragraph. It contains, between its lines, the whole rest of your summer.")]),

N("provider_letter", 28, "A Letter With Two Dates In It", [
 "The provider's letter is routine, which is what makes it dangerous: your position on the waitlist is confirmed; you are approaching the top; evaluation appointments for your group will be scheduled in the batch week beginning " + D61(63) + ". Thank you for your patience. No action is needed from you at this time.",
 f"No action is needed. If you are holding the referral copy, you can see the sentence the letter doesn't write: the batch week begins after {D61(60)}, when the referral that put you on this list expires. If you are not holding it, the letter reads as pure good news \u2014 you are nearly there \u2014 and the cliff edge three days past the finish line is invisible.",
 "No action is needed from you at this time. It is the most expensive sentence in this scenario, and the provider does not even know it wrote it.",
], [C("Take the letter to your lawyer and ask what an expiring referral does to a sequential plan", "lawyer_check",
      note="Because Step B will not enroll you without A \u2014 and A is about to need a referral that is about to stop existing.")]),

N("lawyer_check", 35, "Your Lawyer Reads the Window", [
 "You have had a lawyer since the start of this case, as the law provides (42 Pa.C.S. \u00a7 6337). She reads the provider's letter twice, asks the question the letter was hoping nobody would ask \u2014 'When does the referral itself expire?' \u2014 and then either turns to your copy, with its printed window, or to your diary, with its month.",
 "\u201cUnderstand the machine,\u201d she says. \u201cWhen a referral lapses, the provider doesn't keep your place out of kindness or lose it out of spite. The place belongs to the referral. A re-referral is a new machine part: unless the lapse is documented as the sender's timing \u2014 the waitlist outrunning a window the agency chose \u2014 the queue treats a re-referral as a new arrival. The difference between those two sentences is entirely paper: the dated referral, and a nudge in writing before the window closes, asking the agency to re-send in time.\u201d",
 "She is clear that none of this is a promise about any court or clock beyond this plan: it is a point about whose delay the file will describe, and files describe what their paper lets them describe.",
], [C("Check the waitlist again this week \u2014 in writing, the way dates are made", "queue_check",
      note="The window closes in twenty-five days. The queue is three names from your name. Both facts need witnesses.")]),

N("queue_check", 38, "Three Names Ahead", [
 "The provider answers questions about the waitlist two ways, and the two ways produce two different cases. By email, a reply has a date, a position, and a sentence you can keep: 'You are third on the list; your group is scheduled in the batch week.' By phone, the same facts arrive warmly, personally, and evanescently, in a voice that will remember being helpful and will not remember the number.",
 "Third on the list. The batch week is fixed. The window is fixed. The only variable left in the whole machine is whether anyone with the power to re-send the referral is asked, in writing, before it lapses \u2014 and 'asked in writing' is a thing that either exists as paper or does not exist at all.",
], [C("Write the check-in \u2014 position, batch week, and your name, in an email you keep", "waiting_weeks",
      addHidden=["Waitlist check-ins \u2014 written; provider replies saved, position and batch week confirmed"],
      note="Third, confirmed, dated. The queue now has a witness besides you."),
    C("Call instead \u2014 a voice is harder to put on hold", "waiting_weeks",
      note="She is kind, she confirms third, and she keeps no record of having said so. Kindness is not a filing system.")]),

N("waiting_weeks", 44, "The Quiet Weeks", [
 "Late July is the plan's long corridor: visits kept, screens clean, work held together, and over it all the ticking nobody hears but you \u2014 a referral aging toward a date, a queue inching toward a batch week, a three-year-old finishing one board book and starting another in a visit room.",
 "Ms. Beam's check-in is brief and untroubled. Step A is 'in process,' she says. Step B is 'next.' If you ask about the referral's window, she will reassure you; if you do not, she will not raise it, because in her file the referral is filed under 'sent,' and 'sent' is a completed act in every system except the one that expires.",
 f"The diary page is coming: day fifty, {D61(50)}. Ten days after it, the window closes. What a parent does in those ten days, in writing or in trust, is the last decision this machine leaves to anyone.",
], [C("Open the diary to day fifty", "nudge_choice",
      note="Ten days of margin. In this system, ten days of margin, used in writing, is an fortune. Unused, it is a date that passes.")]),

N("nudge_choice", 50, "Day Fifty: The Nudge", [
 f"Today is {D61(50)}. The referral you may or may not be holding expires {D61(60)} \u2014 ten days from now. You are at or near the top of the waitlist. The batch week begins {D61(63)}. The collision is no longer theoretical; it has dates, and the dates are inside one diary page of each other.",
 "A written nudge is a small, unglamorous machine: a short letter or email to Ms. Beam, copied to the provider, stating the referral's sent date and expiry, the waitlist position, and the batch week \u2014 and asking, plainly, that the referral be re-sent before it lapses so your queue position is preserved as a continuation. It creates the one document the whole summer has been missing: proof that the lapse, if it comes, was seen coming, by name, by the person it would be blamed on \u2014 and reported, in time, to the people whose job the re-send was.",
 "The alternative is trust: the system sent the referral, the system knows its own windows, the system will surely handle its own machine.",
], [C("Send the written nudge today \u2014 agency and provider, dates stated, copies kept", "nudge_sent", cash=-3,
      setFlags=["diaryNudge"],
      addHidden=[f"Written nudge \u2014 sent {D61(50)}, before expiry; re-send requested as a continuation, copies kept"],
      note="Ten days early, in writing, with the dates spelled out. Whatever happens next now has to happen against this page."),
    C("Assume it is handled \u2014 the agency sent it, and agencies track their own referrals", "assume_handled",
      note="A belief held by reasonable people in every waiting room in this system. The machine is about to grade it.")]),

N("nudge_sent", 52, "A Letter Doing Its Quiet Work", [
 "The nudge does not produce drama. It produces a reply: Ms. Beam's office acknowledges the dates \u2014 a sentence you keep \u2014 and the provider's intake office notes your file. Somewhere in the machinery, a referral that was going to expire unattended is now expiring attended, which turns out to be a completely different event wearing the same date.",
 "You go back to the plan's ordinary weeks: visits, screens, the new board book's early chapters. The window is still closing. The difference is that its closing is now an item on other people's desks, in writing, with your letter underneath it \u2014 and systems, whatever their faults, route items that are on desks.",
], [C("Wait for the window to close \u2014 and watch what the machine does with a documented referral", "expiry_kept",
      note="Eight days. Your letter is older than the lapse will be. Sequence is about to become evidence.")]),

N("assume_handled", 52, "Handled, Presumably", [
 "Nothing happens, which feels like confirmation. No call comes; no letter arrives; Step A remains 'in process' at every check-in, because in process is where a referral lives in the file right up until the morning it doesn't. You keep the rest of the plan perfectly \u2014 visits, screens, meetings \u2014 and the perfection is real, and it is all happening on lines of the plan that were never in danger.",
 "The danger is on the one line you cannot touch: a date, printed on a document you never asked for, approaching at the speed of calendars. Eight days from now, the machine will make its decision about your queue position, in a room you are not in, based on paper you did not write.",
], [C("Wait for the window to close", "expiry_restart",
      note="It closes quietly, the way administrative dates do. The consequences arrive later, wearing other dates.")]),

N("expiry_kept", 60, f"The Window Closes \u2014 On Paper", [
 f"On {D61(60)}, the original referral reaches the end of its sixty days \u2014 and because the re-send was requested in writing, ten days early, with the waitlist position and batch week stated, the agency re-sends it as a continuation and the provider honors the original queue position. The lapse is documented, in the provider's own note, as the sender's timing: a five-week waitlist outrunning a sixty-day window was never a delay the parent could have prevented, and now the file says so in someone else's handwriting.",
 "Your place is not a favor. It is a record: referral, waitlist letter, nudge, re-send, continuation note \u2014 a chain with no missing links, each link dated by the person who forged it. Chains like that are what reviews cannot argue with. They can only read them.",
], [C("Go to the evaluation \u2014 in the batch week, at the top of the list, as scheduled", "evaluation_done",
      note="The appointment letter names the original referral and its continuation on the same line. Keep it. Keep everything.")]),

N("expiry_restart", 60, "The Window Closes \u2014 Silently", [
 f"On {D61(60)}, the referral expires. No alarm sounds; expiry is not an event, it is an absence that a computer notices on a schedule. The provider's list, which is a list of live referrals, quietly stops containing your name at the position you had waited five weeks to reach.",
 "The re-referral is sent days later, when the lapse surfaces \u2014 promptly, by the standards of an office that did not know it had a deadline. It is a new referral. The queue, which is a machine for ordering new referrals, places it where new referrals go: at the back. Five weeks of waiting are not stolen by anyone. They are simply not recorded anywhere the queue can read, because the paper that would have preserved them was never created.",
 "Your new position comes with a new projected batch week, in the following month. Step B's door, which opens only on Step A's completion, stays shut \u2014 and the chronology line being drafted for the review requires only four words to describe all of it: 'A not completed.'",
], [C("Ask what your place is now, and when the evaluation can happen", "evaluation_waiting",
      note="The answer is kind, apologetic, and five weeks long. Kindness does not shorten queues. Paper would have.")]),

N("evaluation_done", 66, f"The Evaluation, Completed", [
 f"On {D61(66)}, in the batch week as scheduled, you sit for the Step A evaluation: the history taken again, the questions answered, Cora's needs and your plan discussed in the specialist's unhurried hour. It is, in the lived sense, the thing itself \u2014 the step the plan ordered, completed.",
 "The paper around it matters almost as much: the appointment record names the original referral and its continuation; the provider's report will follow in days. There is one more document to secure, and it is the one the review will ask about first: the re-referral confirmation itself \u2014 the page that shows the chain, original date to re-send to honored position, without a gap for a report writer to fill with your name.",
], [C("File the re-referral confirmation with the original referral copy, in date order", "records_beat", cash=-4,
      setFlags=["rereferralProof"],
      addHidden=["Re-referral proof \u2014 continuation confirmation kept, showing the original date and the honored queue position"],
      note="Chain, complete: sent, waited, nudged, re-sent, honored, completed. Every link dated. Every link kept."),
    C("Leave the confirmation in the provider's portal \u2014 the evaluation is done, and done is what counts", "records_beat",
      note="Done is what counts in the room where it happened. In the review room, what counts is what can be shown \u2014 and portals are not packets.")]),

N("evaluation_waiting", 66, "Still Waiting, From the Back", [
 "The new queue moves at the old queue's pace: about five weeks, the provider says, to a batch week in the following month. You attend everything else. You keep the visits, the screens, the meetings \u2014 a plan running at full speed around one line that a calendar reset while nobody was watching it.",
 "There is one piece of paper in this branch worth keeping, and you may or may not think to keep it: the re-referral letter itself, with its new date. It cannot restore your position. What it can do \u2014 in a review, in a lawyer's hands \u2014 is prove when the clock restarted, which is the difference between a gap with an explanation attached and a gap with your name in it.",
], [C("Keep the re-referral letter and its date, whatever else happens", "records_beat",
      addHidden=["Re-referral letter \u2014 kept, showing the restart date after the silent expiry"],
      note="A lesser document than the chain would have been. It is not nothing. In this system, dated paper is never nothing."),
    C("Let the provider's office keep its own letters \u2014 they'll have them if anyone asks", "records_beat",
      note="They will have them, filed under a referral number you don't know, in a system your lawyer cannot attach to a report.")]),

N("records_beat", 71, "Ask for the File Itself", [
 "Your lawyer raises the other instrument, the one that answers the review before it convenes: the agency's draft chronology already contains the line 'A not completed,' and lines like that are met with attachments or they are met with nothing. A party may request the case record, and the material in it 'shall be released upon request' (55 Pa. Code \u00a7 3130.44(d)).",
 "The request is one page, in writing: the referral record, the re-referral record, the chronology, the draft report. What it would show you is the file's own account of the summer \u2014 the sent date the agency itself recorded, the absence of any expiry note, and the exact wording your packet has to answer. What it cannot show you is anything you never made: requests reveal files; they do not retroactively create the paper inside them.",
], [C("Sign the written request for the record \u2014 referral chain, chronology, draft report", "record_arrives",
      setFlags=["recordsRequested"],
      addHidden=["Case record \u2014 requested in writing, including the referral chain and the draft review report"],
      note="Signed, dated, copied. The file's version of the summer is about to be quotable \u2014 by you, for once, instead of only about you."),
    C("Rely on the provider's letters \u2014 the agency's file is its own business", "no_record",
      note="The agency's file is also the review's script. Declining to read the script does not cancel the performance.")]),

N("record_arrives", 77, "The File's Version of the Summer", [
 f"The record, when it comes, is illuminating in the specific way of unguarded documents. The agency's referral is there, dated {D61(0)} \u2014 prompt, proper, on the record. The re-referral is there too, with its date. Between them: nothing. No expiry date noted. No waitlist note. No record that the window and the queue were ever compared by anyone.",
 "And in the draft chronology, the summer's epitaph, already typed: 'A not completed.' Four words that are, depending on the chain you built, either about to be answered by their own file \u2014 the referral, the waitlist letter, the nudge, the continuation, the completion \u2014 or about to stand as the whole account, because a chronology does not know what it does not contain.",
 "Your lawyer spreads the packet beside the draft. 'We don't argue with four words,' she says. 'We outnumber them.'",
], [C("Read what Step B does next \u2014 the enrollment letter", "enroll_letter",
      note="Step B enrolls on paper too. Its letter is the last piece of the chain, or the last proof of the gap.")]),

N("no_record", 77, "The Script, Unread", [
 "Without the file, you and your lawyer prepare from your side of the paper: the provider's letters you kept, the diary, the evaluation's own documents or the re-referral's. Your account of the summer is accurate. What you cannot do is quote the other side's \u2014 and the review will be conducted from the other side's, in a chronology whose four-word line you have not seen and therefore cannot answer word for word.",
 "\u201cWe present what we have,\u201d your lawyer says, \u201cand we will be answering a sentence we haven't read, in a room that has.\u201d She says it without drama. Sequence, in this system, is not a detail. It is most of the game.",
], [C("Read what Step B does next \u2014 the enrollment letter", "enroll_letter",
      note="Step B's letter does not know about chronologies. It knows one thing: whether Step A is complete.")]),

N("enroll_letter", 83, "Step B Answers", [
 "Step B's letter arrives the way every decisive thing in this case has arrived: routinely, on letterhead, with a date. Its content is a pure function of the chain. Where the evaluation is complete and its report has landed, the letter enrolls you: a start date, a schedule, the plan's spine restored to the order it was written in \u2014 A, then B, as designed. Where the evaluation is still waiting out a restarted queue, the letter says the other thing, in the same courteous type: enrollment cannot proceed until Step A is completed.",
 "Hold the two versions side by side and the scenario's whole mechanism is visible without a single villain in it: the same mother, the same effort, the same plan \u2014 separated by whether a referral's second date was ever written down by the person it could hurt.",
], [C("Prepare for the review with your lawyer", "review_prep",
      note="The review will read the chronology and the packet. Only one of them is still yours to assemble.")]),

N("review_prep", 87, "The Packet, In Date Order", [
 "Your lawyer builds the review packet the way this scenario has built everything: in date order, so the chain tells itself. The referral copy with its window, or its absence. The intake page. The waitlist letters. The nudge, or the silence where it would be. The re-referral \u2014 as continuation or as restart. The evaluation report, or the new queue letter. Step B's answer.",
 "\u201cReviews believe sequences,\u201d she says. \u201cA sequence with a missing link gets narrated by whoever dislikes the gap least \u2014 and it is never narrated as a machine's gap. Machines don't get blamed in reports. People with names in the chronology do. Our whole job is to make the machine's part of this sequence as documented as yours.\u201d",
 "She copies the packet for the court. What it proves, and what it cannot, will be decided by which links your summer actually forged.",
], [C("Make the court copies and go to the review", "review", cash=-6,
      addHidden=["Review packet \u2014 referral chain assembled in date order, from referral copy to Step B's letter"],
      note="Date order. The summer, testified to by its own paperwork, in the order the paperwork happened.")]),

N("review", 91, "The Review", [
 f"The review convenes on {D61(91)}. The agency presents its chronology, and the Step A line gets its four words: 'A not completed' \u2014 or, where the evaluation landed, 'A completed late,' with the lateness offered without an owner. Reports are read against packets now, and the packet is in the room.",
 "What happens next depends, with a precision this scenario has been honest about since its first phone call, on the chain itself: whether the referral was dated in your hands in June, whether the nudge went out in writing before the window closed, whether the continuation was kept, and whether the file was ever requested and quoted back to its authors.",
 "Your lawyer rises. Choose the presentation the chain you actually built can carry.",
], [C("Present the whole chain \u2014 dated referral, written nudge, continuation proof, and the agency's own record", "end_win",
      requiresFlags=["referralDated", "diaryNudge", "rereferralProof", "recordsRequested"],
      note="This presentation exists because four pieces of paper exist, dated, in order, from June to September."),
    C("Present the agency's own record \u2014 the referral and re-referral dates it recorded itself", "end_partial",
      requiresFlags=["recordsRequested"],
      note="The file answers part of the charge against itself. The rest of the chain is thinner \u2014 and the room can feel where."),
    C("Present what paper you have \u2014 provider letters and the diary, assembled as a sequence", "end_partial",
      note="Half a chain is an argument with missing links. It still changes the room \u2014 just less, and later."),
    C("Explain the summer yourself \u2014 the waitlist, the window, the queue, as you lived them", "end_worst",
      note="Your account is accurate in every particular. Accuracy, unattached, is the currency this room accepts least.")]),

N("end_win", 98, "Ending \u2014 Referred, Continuously", [], ending=True, debrief=[
 f"WHAT THE FILE HELD (the chain, revealed): At the review on {D61(91)}, the chronology's line did not survive its own attachments. The chain was complete and dated at every link: the referral copy showing it sent {D61(0)} and valid through {D61(60)}; the intake and waitlist letters; the written nudge sent ten days before the window closed; the provider's continuation note honoring the original queue position because the lapse was documented as the sender's timing; the evaluation completed {D61(66)}; and Step B's enrollment letter, issued on the completed evaluation. The delay was attributed, on the record, to the referral mechanics \u2014 a five-week queue outrunning a sixty-day window \u2014 and not to you. Cora remains in foster care and Step B has weeks to run; no honest debrief will call this case won. What is won is the attribution, permanently, for every future reader of this file.",
 "THE PROCESS UNDER THIS PATH (described, keeping to this scenario's verified law): No new right was invented here. The case record was available on written request \u2014 it 'shall be released upon request' (55 Pa. Code \u00a7 3130.44(d)) \u2014 and requesting it is what let your lawyer quote the agency's own referral dates back to the chronology that omitted them. Counsel's role was the one the law assigns from the start (42 Pa.C.S. \u00a7 6337): assembling dated paper into a sequence a review cannot narrate around. The referral window itself is not a statute in this scenario; it is a piece of administrative machinery \u2014 a provider's validity period \u2014 and the scenario's claim is only the modest one the paper supports: machinery like that decides cases unless somebody documents it, and documenting it is a skill, not a virtue.",
 "THE HONEST PART: A different provider might never have honored a continuation, nudge or no nudge; a different report writer might have contested the chain link by link; Ms. Beam's office might have missed the re-send even with your letter on the desk, and no nudge compels an office to be prompt. Workers, providers, judges, and the plain luck of a batch week's timing all held pieces of this outcome. And the deepest honesty is the same as in every scenario in this series: Cora spent this summer three years old, in someone else's house, whatever the paperwork says about whose delay it was. What your choices changed was narrower and load-bearing \u2014 whether the file tells the truth about a machine's failure, or tells it as yours. Outcomes here are not verdicts on a parent. This one is a verdict on a chain of paper, and for once the chain held.",
]),
N("end_partial", 98, "Ending \u2014 A Gap, Half-Explained", [], ending=True, debrief=[
 f"WHAT THE FILE HELD (the chain, revealed): A partial chain: some links dated and kept \u2014 a provider letter here, a re-referral date there, perhaps the agency's own record quoted back to it \u2014 and gaps where the dated referral copy, the written nudge, or the continuation confirmation would have been. At the review on {D61(91)}, partial paper did partial work. The review declined to adopt 'A not completed' as a statement about you in full; the agency conceded, in general terms, that 'referral processing' had contributed to the timeline; and the gap was entered as contested rather than attributed \u2014 shared, vaguely, between a mother and a machine, in proportions nobody was required to specify. Step B's position improved or waits, depending on the chain; the plan continues; and the file's account of the summer is a draw, which against a chronology that began as four flat words is movement \u2014 and against what the whole chain would have done, is a lesson with a price.",
 "THE PROCESS UNDER THIS PATH (described, keeping to this scenario's verified law): The tools were the verified ones, used partly. The case record, on written request (55 Pa. Code \u00a7 3130.44(d)), could show the referral and re-referral dates the agency itself recorded \u2014 the strongest single answer to its own chronology \u2014 and counsel (42 Pa.C.S. \u00a7 6337) could build only from the links that existed. Nothing in this ending says you failed the summer: you waited the wait, kept every other line, and may have managed the referral diligently by phone and trust. It says the review priced your proof, not your diligence, because reviews can only price what is in front of them \u2014 and a chain, unlike an effort, cannot be half-forged in the room and expected to hold weight.",
 "THE HONEST PART: A contested gap may matter less by the next review than it does today: Step B will be running or the evaluation long completed, and nine weeks of new compliance will outweigh an argument about a summer referral. Judges differ in how much ambiguity they hold against the party who didn't create it, and this one split the difference, as many do. What remains true is the mechanism, and it is portable to every referral, waitlist, and sequential step still ahead of you in this case: the side that documents the machine's dates owns the machine's delays, and the side that merely survives them rents the explanation, review by review. Your packet, from here, is a habit looking for its next referral. It will find one.",
]),
N("end_worst", 98, "Ending \u2014 Expired, As Written", [], ending=True, debrief=[
 f"WHAT THE FILE HELD (the chain, revealed): At the review on {D61(91)}, the chronology stood as written, because it was the only written thing in the room that described the whole summer: referred, waited, 'A not completed.' The referral's expiry was never mentioned as a fact about a machine; the restarted queue was never mentioned at all; the five weeks you spent at the top of a list exist nowhere the review could read them. Your account \u2014 accurate in every detail \u2014 was received the way unattached accounts are received in rooms that run on attachments: personally, and without effect. The plan's spine stays broken at the same joint: Step B cannot enroll you, the evaluation waits out its second queue, and the next report is already drafting itself from this one's four words.",
 "THE PROCESS UNDER THIS PATH (described, keeping to this scenario's verified law): No rule says an expired referral is a parent's failure. What produced this ending was an absence of paper at the three moments paper was available: the referral copy, requestable in June with its window in print; the written nudge, sendable ten days before the window closed, which would have made the re-send a documented duty instead of a discovered lapse; and the case record itself, available on written request (55 Pa. Code \u00a7 3130.44(d)), whose own dates answer its own chronology. Counsel was there throughout (42 Pa.C.S. \u00a7 6337) to assemble any of it. The system did not defeat a strategy here. It simply ran, unattended, on its default settings \u2014 and its default setting is that an undated delay belongs to the only named person in the sentence.",
 "THE HONEST PART: Let this debrief be as fair as the review was not: the delay was never yours. You presented for intake, you waited the wait in good faith, you kept every line of the plan that a parent can touch, and the referral expired in a computer, on a date nobody told you, while a provider's letter was assuring you no action was needed. The injustice of this ending is not that the system doubted your effort; it is that effort was the wrong currency, and the exchange rate \u2014 dated referrals, written nudges, kept confirmations \u2014 was never posted in the waiting room. Workers with lighter caseloads sometimes catch an expiring referral themselves; some parents are rescued by exactly that luck. Yours was not, and luck is not a system. The chain can still be started \u2014 at the next referral, in writing, on day one \u2014 and it will matter at the next review. It simply cannot retroactively date the summer that just passed undated.",
]),
]

S60_META = {"title": "The First 90 Days",
 "subtitle": "Scenario 60 \u2014 The New Worker (a fictional composite)",
 "startDateISO": "2026-06-01", "startNode": "start", "startCash": 160,
 "tier": "Hard",
 "summary": "Eight months in, the caseworker changes \u2014 and the new worker meets a summary with two stale lines, not the mother who lived the case."}
S61_META = {"title": "The First 90 Days",
 "subtitle": "Scenario 61 \u2014 The Expired Referral (a fictional composite)",
 "startDateISO": "2026-06-15", "startNode": "start", "startCash": 130,
 "tier": "Hard",
 "summary": "Step A must finish before Step B will enroll her \u2014 but the referral for A expires while its waitlist is still running."}

scen60 = build(S60_META, s60_nodes, S60_START)
scen61 = build(S61_META, s61_nodes, S61_START)

ROUTE60 = ["start","handover_note","binder_beat","binder_kept","first_meeting",
 "stale_detail","letter_choice","letter_sent","reorder","attach_cert",
 "records_beat","record_arrives","correction_choice","correction_filed",
 "second_meeting","wilkes_checkin","visits_meanwhile","review_prep","packet_assembly",
 "review","end_win"]
ROUTE61 = ["start","copy_choice","copy_kept","intake","middle_weeks",
 "visit_clean","provider_letter","lawyer_check","queue_check","waiting_weeks",
 "nudge_choice","nudge_sent","expiry_kept","evaluation_done","records_beat",
 "record_arrives","enroll_letter","review_prep","review","end_win"]

def walk(scen, route):
    by = {n["id"]: n for n in scen["nodes"]}
    assert route[0] == scen["meta"]["startNode"]
    cash = scen["meta"]["startCash"]; flags = set(); min_cash = cash
    for a, b in zip(route, route[1:]):
        edges = [c for c in by[a].get("choices", []) if c["next"] == b]
        assert edges, f"no edge {a} -> {b}"
        e = edges[0]
        for req in e.get("requiresFlags", []):
            assert req in flags, f"gate {req} not satisfied at {a} -> {b}"
        for req in e.get("requiresNoFlags", []):
            assert req not in flags, f"no-flag gate {req} violated at {a} -> {b}"
        cash += e.get("cash", 0); min_cash = min(min_cash, cash)
        assert cash >= 0, f"cash negative at {a} -> {b}"
        flags.update(e.get("setFlags", []))
    end = by[route[-1]]
    assert end.get("ending"), f"route ends at non-ending {route[-1]}"
    assert "recordsRequested" in flags, "win route must set recordsRequested"
    return {"end_title": end["title"], "visited": len(route), "end_cash": cash,
            "min_cash": min_cash, "flags": sorted(flags)}

W60 = walk(scen60, ROUTE60)
W61 = walk(scen61, ROUTE61)

# =====================================================================
# STRATEGY GUIDES (generated after the programmatic walks above, so the
# verification footers quote the walked path, visited count and end cash)
# =====================================================================
def write_guide(num, text):
    p = os.path.join(OUT, f"strategy-{num}.md")
    with open(p, "w") as f:
        f.write(text)
    return p

GUIDE60 = f"""# Strategy Guide \u2014 Scenario 60: "The New Worker"

*Game documentation for a fictional simulation in "The First 90 Days" (Tactic Watch). The family, the case, and every choice below are fictional. This guide is general information about how the scenario is built \u2014 it is not legal advice for any real case.*

## (1) The win

**Best ending: "{W60['end_title']}."**

State it honestly: this is a **partial** win, and it is the best this scenario offers. The review report's three contested lines are corrected on the record \u2014 the completed program reads as completed, the passed screen reads as passed, the spring assessment reads as completed \u2014 because the correction was filed, with attachments, before the review convened. Silas does **not** come home at the end of this ending. His placement continues and the plan continues. The win is continuity itself: the case Mr. Wilkes inherited on paper is the case Marta actually lived, and every future reader of the file will meet that version first. There is no ending in this scenario where a worker change is painless. Anyone selling you one is selling you a different game.

## (2) The route

Verified by walking the scenario graph from the start node (see the verification note at the end). The walk passes, in order, through: The Goodbye Letter; What the Letter Says, and Doesn't; The Kitchen-Table Archive; Date Order; Mr. Wilkes, Week One; Two Lines, Both Wrong; The First-Week Letter; Sent, Copied, Dated; The Assessment, Again; The Certificate Answers; Ask for the File Itself; The Draft, With Template Lines; Correct It Where It Lives; Filed, Not Just Said; The Second Meeting; The Check-In Call; Visits, and Everything Else; Ms. Parr Builds the Packet; Date Order, Again; The Review. Key decision points:

1. **The Kitchen-Table Archive** \u2014 *Bring the binder current tonight \u2014 tabs, copies, everything in date order.* Cash \u221210. Sets **binderKept**; hidden item: the binder in date order from month one. This is the earliest choice in the scenario and the one every later room prices.
2. **The First-Week Letter** \u2014 *Send the status letter this week, with the certificates attached.* Cash \u22126. Sets **letterSent**. Sent inside Mr. Wilkes's first weeks, the letter is orientation; the same letter sent later would be a dispute. It makes the summary's stale lines expensive to repeat, because repeating them now means repeating them against attachments.
3. **The Assessment, Again** \u2014 *Answer in writing \u2014 attach the completion certificate and the dated sign-in page.* Cash \u22124. The re-order is withdrawn because the draft file copy is answered by the finished thing it was a draft of. Quietly redoing it (cash \u221230) buys a second, later date that the file will forever be tempted to mistake for the first.
4. **Ask for the File Itself** \u2014 *Sign the written request for the record \u2014 draft report, assessment copies, all of it.* Sets **recordsRequested**. This is what surfaces the draft review report \u2014 template lines and all \u2014 while every line in it is still soft enough to correct.
5. **Correct It Where It Lives** \u2014 *File the written correction before the review, certificates attached.* Cash \u22125. Sets **correctionFiled**. A correction filed weeks ahead becomes the report's new text; the same points raised orally at a meeting become a note on a busy worker's pad.
6. **Assemble the final packet (Date Order, Again)** \u2014 Cash \u22125. The packet filed for the court in date order: goodbye letter, the two lines as noted word for word, status letter, assessment correspondence, draft beside correction, the clean recent weeks.
7. **The Review** \u2014 *Present the corrected record \u2014 binder, first-week letter, record packet, and the correction filed before today.* This choice is flag-gated: it is only available with **binderKept** + **letterSent** + **recordsRequested** + **correctionFiled** all set. It leads to **{W60['end_title']}**.

Supporting route choices that cost nothing and keep the route honest: noting the two stale lines word for word at **Mr. Wilkes, Week One** (the correction is later built out of the exact sentences it corrects), and running the plan's ordinary weeks perfectly at **Visits, and Everything Else**, so the review reads a whole file that is clean, not only three repaired lines.

## (3) Why this wins \u2014 the law as it is supposed to work

Only principles from the scenario's verified set are stated here:

- **The case record is available on written request** \u2014 55 Pa. Code \u00a7 3130.44(d) ("shall be released upon request"). Step 4 is that right, exercised in writing, and it is the highest-leverage move in the scenario: it converts a rumored draft into a quotable text, weeks before the review reads it.
- **The release has a lawful limit, and the route honors it** \u2014 released material may omit what violates another person's privacy or is protected or made confidential by law (55 Pa. Code \u00a7 3130.44(f)). The packet's redactions are accepted, not fought; what is fought is the stale text that no confidentiality claim ever protected.
- **Counsel assembles and files** (42 Pa.C.S. \u00a7 6337). Ms. Parr's work in the route is inventory, not eloquence: each stale line answered by its own attachment, filed where the next report writer cannot miss it.
- **Everything else is process, stated without citation on purpose:** a summary is a derivative document. It inherits the errors of the report it was copied from and lends them its own authority. The route wins by going underneath the summary to primary paper \u2014 certificate, result, sign-in page \u2014 and filing the correction where future summaries are written from.

## (4) The traps

1. **Leaving the shoebox as it is at "The Kitchen-Table Archive"** because you know what's in it. Cost: no **binderKept**, and the best presentation at the review closes. Knowledge that cannot be handed across a table is, in a review room, a rumor about yourself.
2. **Waiting at "The First-Week Letter"** for Mr. Wilkes to learn the case the way Ms. Renshaw did. She had eight months; the review is closer than that. Cost: no **letterSent** \u2014 the summary sets, report by report, and your later letter arrives as a dispute instead of as orientation.
3. **Redoing the assessment quietly at "The Assessment, Again."** Cost: cash \u221230, two appointments, and a second completion date in the file that future summaries can mistake for the only one \u2014 cooperation that manufactures the very lateness the plan will later hold against you.
4. **Raising the correction orally at "Correct It Where It Lives."** Mr. Wilkes agrees with every word, in person, and writes himself a note. Cost: no **correctionFiled**. The best presentation closes, and the correction that reaches the review at all arrives in the room, contested, at speaking speed \u2014 **"Ending \u2014 Reset, Then Repaired."** Presenting from memory alone reaches **"Ending \u2014 Starting Over at Month Nine"**: the stale lines harden into findings and the plan restarts services that were already completed.

## (5) What no strategy controls

Whether Mr. Wilkes is conscientious or merely busy; whether his supervisor contests a correction or waves it through; whether the report writer reads attachments or copies the last report; whether the next worker change lands next month and starts the whole problem over with a new reader. Silas's own timeline \u2014 a nine-year-old spending his ninth year between two homes while adults correct his file \u2014 is not controlled by any of this either, and the route does not pretend otherwise. What the route controls is narrower: when the file was wrong, the correction existed as dated paper, filed early, in the room before the room convened. Outcomes in this system turn on workers, judges, and luck as much as on any parent's choices. The strategy's whole claim is that a handoff should not get to tax a parent's record for the handoff's own incompleteness \u2014 and that the tax, when it comes, is payable in copies and stamps instead of in months.

---
*Verification: this route was walked programmatically against `scenario-60.json` \u2014 each named choice was followed from the start node in order; every intermediate node and choice exists; every flag-gated choice's requirements were satisfied by flags set earlier on the walk (flags at the ending: {", ".join(W60['flags'])}); cash never went negative on the walk. Walked path: {" \u2192 ".join(ROUTE60)}. The walk terminates at the ending node titled "{W60['end_title']}" after visiting {W60['visited']} nodes, with ${W60['end_cash']} of the $160 starting cash remaining.*
"""

GUIDE61 = f"""# Strategy Guide \u2014 Scenario 61: "The Expired Referral"

*Game documentation for a fictional simulation in "The First 90 Days" (Tactic Watch). The family, the case, and every choice below are fictional. This guide is general information about how the scenario is built \u2014 it is not legal advice for any real case.*

## (1) The win

**Best ending: "{W61['end_title']}."**

State it honestly: this is a **partial** win, and it is the best this scenario offers. The referral chain is documented end to end \u2014 sent {D61(0)}, waited out on a five-week list, nudged in writing before its sixty-day window closed on {D61(60)}, re-sent as a continuation with the original queue position honored, the Step A evaluation completed {D61(66)}, and Step B enrolled on it. The delay is attributed on the record to the referral mechanics, not to Tanya. Cora does **not** come home at the end of this ending: her placement continues and Step B has weeks to run. The win is that the file tells the truth about a machine's failure instead of telling it as a mother's \u2014 permanently, for every future reader. There is no ending in this scenario where the referral does not expire. Anyone selling you one is selling you a different game.

## (2) The route

Verified by walking the scenario graph from the start node (see the verification note at the end). The walk passes, in order, through: Two Steps, In Order; Sent \u2014 But On What Paper?; Sixty Days, In Print; Name on the List, Date on the Wall; Everything Else Runs Clean; The Installment Book, Finished; A Letter With Two Dates In It; Your Lawyer Reads the Window; Three Names Ahead; The Quiet Weeks; Day Fifty: The Nudge; A Letter Doing Its Quiet Work; The Window Closes \u2014 On Paper; The Evaluation, Completed; Ask for the File Itself; The File's Version of the Summer; Step B Answers; The Packet, In Date Order; The Review. Key decision points:

1. **Sent \u2014 But On What Paper?** \u2014 *Ask for the referral copy in writing \u2014 sent date and validity window included.* Cash \u22123. Sets **referralDated**. The anchor exhibit of the whole scenario: the agency's own page showing the referral sent {D61(0)} and valid through {D61(60)}. Without it, the window is a rumor about a month.
2. **Name on the List, Date on the Wall** \u2014 *Write down the intake date, the wait, and the batch week before you leave the building.* The provider's own arithmetic, in your hand: a five-week wait, evaluations batched in the week beginning {D61(63)} \u2014 three days after the window closes.
3. **Day Fifty: The Nudge** \u2014 *Send the written nudge today \u2014 agency and provider, dates stated, copies kept.* Cash \u22123. Sets **diaryNudge**. Sent {D61(50)}, ten days before expiry, this is the document that converts the re-send from a discovered lapse into a documented duty \u2014 and the lapse, when it comes, into the sender's timing rather than the parent's.
4. **The Evaluation, Completed** \u2014 *File the re-referral confirmation with the original referral copy, in date order.* Cash \u22124. Sets **rereferralProof**. The provider honors the original queue position; the evaluation is completed {D61(66)}; the confirmation page is the link that proves the chain has no gap.
5. **Ask for the File Itself** \u2014 *Sign the written request for the record \u2014 referral chain, chronology, draft report.* Sets **recordsRequested**. The agency's own file records the referral promptly on {D61(0)} and the re-referral after expiry \u2014 with no expiry note anywhere between them. Quoting those dates back is what answers the chronology's "A not completed."
6. **The Packet, In Date Order (review preparation)** \u2014 Cash \u22126 for the court copies. The chain assembled as a single sequence: referral, intake, waitlist letters, nudge, continuation, evaluation, Step B's enrollment letter.
7. **The Review** \u2014 *Present the whole chain \u2014 dated referral, written nudge, continuation proof, and the agency's own record.* This choice is flag-gated: it is only available with **referralDated** + **diaryNudge** + **rereferralProof** + **recordsRequested** all set. It leads to **{W61['end_title']}**.

Supporting route choices that cost nothing and keep the chain legible: the written waitlist check-in at **Three Names Ahead** (position and batch week confirmed in a reply you can keep, instead of a phone call the file cannot), and running every other line of the plan cleanly through **Everything Else Runs Clean** and the visit weeks, so that at the review the only outstanding line is the one the machine owns.

## (3) Why this wins \u2014 the law as it is supposed to work

Only principles from the scenario's verified set are stated here. Note first what the scenario does **not** do: the sixty-day referral window is not stated as law anywhere in the game. It is administrative machinery \u2014 a provider's validity period \u2014 and the game treats it exactly that way: a fact to document, not a right to invoke.

- **The case record is available on written request** \u2014 55 Pa. Code \u00a7 3130.44(d) ("shall be released upon request"). Step 5 is that right, exercised in writing. It is what turns the agency's chronology from an assertion into a quotation \u2014 and the quotation, referral date and re-referral date with silence between them, is the packet's strongest page.
- **Counsel assembles and sequences** (42 Pa.C.S. \u00a7 6337). Reviews believe sequences; the lawyer's whole function in this route is to make the machine's part of the sequence as documented as the parent's.
- **The federal clock, in this guide only, and in the disciplined form the verified set allows:** under 42 U.S.C. \u00a7 675(5)(E), when a child has been in foster care for 15 of the most recent 22 months, the agency is generally to file for termination \u2014 except, among the statute's three exceptions, where the agency has identified services necessary for the child's safe return that it has not provided to the family. A sequential plan whose first step sat in a referral chain \u2014 sent, expired unattended, re-sent to the back of a queue \u2014 is that exception's shape. But the exception is an *argument*, and arguments need exhibits: it is record-dependent, it speaks to the *filing decision*, and any later termination case would still have to be proven by the agency by clear and convincing evidence. The chain documented on this route is what would make the argument available. The game itself makes no promise about it, asserts no filing date, and depicts no termination outcome.

## (4) The traps

1. **Trusting the phone call at "Sent \u2014 But On What Paper?"** because Ms. Beam sent the referral and will track it. She did send it. Cost: no **referralDated** \u2014 the expiry survives the summer as "about two months," a shape that cannot be nudged against, quoted, or attached to anything, and the best presentation at the review closes.
2. **Assuming it is handled at "Day Fifty: The Nudge."** The agency sent the referral; agencies track their own referrals \u2014 a reasonable belief, and the machine's favorite. Cost: no **diaryNudge**. The window closes silently on {D61(60)}, the re-referral goes out days later as a new arrival, and five weeks of queue position evaporate without a single person deciding they should.
3. **Leaving the continuation confirmation in the provider's portal at "The Evaluation, Completed."** The evaluation is done, and done feels like what counts. Cost: no **rereferralProof**. The chain reaches the review with its most important link unshowable, and a completed evaluation gets narrated as a late one.
4. **Explaining the summer yourself at "The Review."** Your account is accurate in every particular, and the room receives it the way rooms that run on attachments receive voices. Cost: **"Ending \u2014 Expired, As Written"** \u2014 the chronology's four words stand as the whole account of the summer. Presenting partial paper reaches **"Ending \u2014 A Gap, Half-Explained"**: the gap is contested rather than attributed, which is exactly what half a chain earns.

## (5) What no strategy controls

Whether the provider honors a continuation or treats every re-send as a new arrival; whether the batch week slips; whether Ms. Beam's office, nudged or not, re-sends on time; whether a report writer reads a packet or copies a chronology; and Cora's own clock \u2014 she spent this summer three years old, in someone else's house, whatever the paperwork concludes about whose delay it was. A lighter caseload, a provider with a longer window, a queue that moved faster: any of them changes this summer without Tanya changing anything. What the route controls is narrower: whether a delay everyone involved agreed was a machine's is *documented* as a machine's \u2014 because in this system, an undocumented system failure is re-filed, by default, under the parent's name.

---
*Verification: this route was walked programmatically against `scenario-61.json` \u2014 each named choice was followed from the start node in order; every intermediate node and choice exists; every flag-gated choice's requirements were satisfied by flags set earlier on the walk (flags at the ending: {", ".join(W61['flags'])}); cash never went negative on the walk. Walked path: {" \u2192 ".join(ROUTE61)}. The walk terminates at the ending node titled "{W61['end_title']}" after visiting {W61['visited']} nodes, with ${W61['end_cash']} of the $130 starting cash remaining.*
"""

# =====================================================================
# VALIDATION \u2014 all checks must pass
# =====================================================================
ALLOWED_CITES = {"6332", "6315", "6337", "6341", "675", "3130.44"}
FORBIDDEN_NAMES = ["Christine", "Annie", "Roth", "Camden", "Mara", "Eli", "Wren",
 "Marcus", "Lark", "Dana", "Noah", "Mia", "Denise", "Okafor", "Bennett", "Doyle",
 "Ito", "Osei", "Simone", "Kayla", "Diane"]

def validate(scen, num, start, exp_nodes, cast_surnames, cast_first):
    res = {}
    by = {n["id"]: n for n in scen["nodes"]}
    assert len(scen["nodes"]) == exp_nodes, (num, len(scen["nodes"]))
    res["nodes"] = len(scen["nodes"])
    ends = [n for n in scen["nodes"] if n.get("ending")]
    assert len(ends) == 3, (num, len(ends)); res["endings"] = 3
    for e in ends:
        assert e.get("debrief") and len(e["debrief"]) == 3
        assert "choices" not in e
        assert e["title"].startswith("Ending \u2014 ")
    # all next resolve + dayOffsets non-decreasing along every edge
    edges = 0
    for n in scen["nodes"]:
        for c in n.get("choices", []):
            assert c["next"] in by, (num, n["id"], c["next"])
            assert by[c["next"]]["dayOffset"] >= n["dayOffset"], (num, n["id"], c["next"])
            edges += 1
    res["edges"] = edges
    # reachability ignoring gates (BFS)
    seen = set(); stack = [scen["meta"]["startNode"]]
    while stack:
        x = stack.pop()
        if x in seen: continue
        seen.add(x)
        stack.extend(c["next"] for c in by[x].get("choices", []))
    assert seen == set(by), (num, set(by) - seen)
    res["reachable_ignoring_gates"] = len(seen)
    # kickers recomputed
    for n in scen["nodes"]:
        d = start + timedelta(days=n["dayOffset"])
        assert n["kicker"] == f"Day {n['dayOffset']} \u2014 {fmt(d)}", (num, n["id"])
    res["kickers_checked"] = len(scen["nodes"])
    # ungated subgraph: middle + worst reachable, win not reachable
    ung = set(); stack = [scen["meta"]["startNode"]]
    while stack:
        x = stack.pop()
        if x in ung: continue
        ung.add(x)
        for c in by[x].get("choices", []):
            if not c.get("requiresFlags") and not c.get("requiresNoFlags"):
                stack.append(c["next"])
    titles_ung = {by[i]["title"] for i in ung if by[i].get("ending")}
    assert "end_partial" in ung and "end_worst" in ung, (num, titles_ung)
    assert "end_win" not in ung, (num, "win reachable without gates")
    res["ungated_endings"] = sorted(titles_ung)
    # citation sweep
    text = json.dumps(scen, ensure_ascii=False)
    cites = set(re.findall(r"\u00a7\s*([0-9]+(?:\.[0-9]+)?)", text))
    assert cites <= ALLOWED_CITES, (num, cites - ALLOWED_CITES)
    res["citations"] = sorted(cites)
    for bad in ["predictive", "machine learning", "artificial intelligence"]:
        assert bad not in text.lower(), (num, bad)
    # no removed flag anywhere
    assert '"removed"' not in text
    for n in scen["nodes"]:
        for c in n.get("choices", []):
            assert "removed" not in c.get("setFlags", [])
    # cast sweep: surnames after Ms./Mr. and forbidden names
    surnames = set(re.findall(r"(?:Ms\.|Mr\.)\s+([A-Z][a-z]+)", text))
    assert surnames <= set(cast_surnames), (num, surnames)
    res["surnames"] = sorted(surnames)
    for fn in FORBIDDEN_NAMES:
        assert not re.search(rf"\b{fn}\b", text), (num, fn)
    for cf in cast_first:
        assert re.search(rf"\b{cf}\b", text), (num, cf, "cast first name missing")
    # hidden items
    hidden_total = sum(len(c.get("addHidden", [])) for n in scen["nodes"] for c in n.get("choices", []))
    res["hidden_items_total"] = hidden_total
    # script parity: ids/order/choices identical
    script = open(os.path.join(OUT, f"scenario-{num}-script.md")).read()
    sids = re.findall(r"^## \[([^\]]+)\] ", script, re.M)
    assert sids == [n["id"] for n in scen["nodes"]], (num, "script id order")
    for n in scen["nodes"]:
        if n.get("ending"): continue
        for c in n["choices"]:
            assert f"- {c['text']} \u2192 **{c['next']}**" in script, (num, n["id"], c["text"][:40])
    res["script_parity"] = "ids/order/choice-text+next identical"
    return res

if __name__ == "__main__":
    emit(scen60, 60, "The New Worker",
         "This scenario depicts a parent whose caseworker changes eight months into her son's foster-care placement, told through letters, summaries, draft reports, and a review. There is no graphic content. Players may skip any scene or use the quick exit at any time.",
         S60_START)
    emit(scen61, 61, "The Expired Referral",
         "This scenario depicts a parent working a sequential service plan \u2014 an evaluation that must be completed before a parenting program will enroll her \u2014 while the evaluation's referral runs toward its expiry date, told through referral copies, waitlist letters, and review reports. There is no graphic content. Players may skip any scene or use the quick exit at any time.",
         S61_START)
    write_guide(60, GUIDE60)
    write_guide(61, GUIDE61)
    # re-read JSON from disk for validation (parse check included)
    s60d = json.load(open(os.path.join(OUT, "scenario-60.json")))
    s61d = json.load(open(os.path.join(OUT, "scenario-61.json")))
    r60 = validate(s60d, 60, S60_START, 28, ["Renshaw", "Wilkes", "Parr"], ["Marta", "Silas"])
    r61 = validate(s61d, 61, S61_START, 27, ["Beam"], ["Tanya", "Cora"])
    print("SCENARIO 60 VALIDATION:", json.dumps(r60, ensure_ascii=False))
    print(f"  win walk: visited={W60['visited']} end_cash={W60['end_cash']} min_cash={W60['min_cash']} flags={W60['flags']}")
    print("SCENARIO 61 VALIDATION:", json.dumps(r61, ensure_ascii=False))
    print(f"  win walk: visited={W61['visited']} end_cash={W61['end_cash']} min_cash={W61['min_cash']} flags={W61['flags']}")
    print("ALL VALIDATION PASSED")
