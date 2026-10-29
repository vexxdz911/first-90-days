#!/usr/bin/env python3
"""Generator for Scenarios 62 and 63 of 'The First 90 Days' (Hard tier).
One data source emits both the .json and the -script.md for each scenario,
so they match node-for-node by construction. Every kicker and every
in-body date is computed from startDateISO + dayOffset via fmt()/dstr();
no date is hand-typed. Pattern follows generate-scenarios-33-34.py."""
import json, os
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
             "choice \u2014 the player does not see it when it happens. `NOTE:` is text shown to the player right after choosing.")
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
                    ann.append(f"cash {'\u2212' + str(-c['cash']) if c['cash'] < 0 else '+' + str(c['cash'])}")
                if c.get("setFlags"):
                    ann.append("FLAG: " + ", ".join(c["setFlags"]))
                if c.get("addHidden"):
                    ann.append("; ".join("HIDDEN + " + h for h in c["addHidden"]))
                if c.get("requiresFlags"):
                    ann.append("REQUIRES FLAG: " + " ; ".join(c["requiresFlags"]))
                if c.get("requiresNoFlags"):
                    ann.append("REQUIRES NO FLAG: " + " ; ".join(c["requiresNoFlags"]))
                suffix = f"  _({'; '.join(ann)})_" if ann else ""
                L.append(f"- {c['text']} \u2192 **{c['next']}**{suffix}")
                if c.get("note"):
                    L.append(f"  - NOTE (shown after choosing): {c['note']}")
    path_m = os.path.join(OUT, f"scenario-{num}-script.md")
    with open(path_m, "w") as f:
        f.write("\n".join(L) + "\n")
    return path_j, path_m

# =====================================================================
# SCENARIO 62 \u2014 The Visit Notes
# Opens Monday, July 6, 2026. Ezra, 6, placed before the story opens;
# no removal occurs in-story (no `removed` flag, by design).
# =====================================================================
S62_START = date(2026, 7, 6)
assert S62_START.strftime("%A") == "Monday"
def D62(off):
    return fmt(S62_START + timedelta(days=off))

s62_nodes = [
N("start", 0, "The Visit Routine", [
 "Your name is Felicia. Your son Ezra is six, and he is living in foster care \u2014 placed before this story opens, in a part of the case this story does not retell. What this story covers is the part that happens twice a week, in a visit room with a clock on the wall: your supervised visits.",
 "Ms. Goss, the visit supervisor, sits to the side with a notebook. Mr. Henley, your caseworker, is rarely in the room, but he reads what the room produces. Because that is the quiet fact of supervised visits: someone is always writing. The notes Ms. Goss takes \u2014 what Ezra did, what you did, the words each of you used \u2014 go into the case file, and the file is the case's memory. Reviews you will never sit in will be written from it.",
 "You cannot write the notes. What you can do \u2014 what this scenario is about \u2014 is learn what they say, and answer them on paper, in time for the paper to matter.",
], [C("Go to this week's first visit \u2014 and pay attention to the notebook, not just to Ezra", "flat_visit",
      note="Twice a week, an hour at a time, a woman with a notebook decides what the summer will be remembered as. You cannot see the notebook. Yet.")]),

N("flat_visit", 3, "The Word \u2018Flat\u2019", [
 f"{D62(3)}'s visit comes at the end of a double shift. You came straight from work, in your work shoes, with Ezra's snack in your bag and four hours of sleep in you. You play the game he picks. You read the book. But you are running on the flat, tired edge of yourself, and some part of you knows how it must look from the chair by the wall.",
 "Ms. Goss writes, now and then, without looking up. You will not see today's note for weeks. When you finally do, one word in it will have travelled further than any other word in your file.",
], [C("Tell Ms. Goss plainly, before the visit starts: \u2018I worked a double. I'm tired \u2014 I'm not checked out.\u2019", "that_night",
      addHidden=["Visit context \u2014 mother told the supervisor she had worked a double shift and was tired"],
      note="Said out loud, in the room, where the notebook is. Whether it lands in the note is her call. That you said it is yours."),
    C("Push through and say nothing \u2014 tired is not a thing you want in writing", "that_night",
      note="Understandable. Also: the tiredness will be in writing anyway. The only question is whose sentence carries it.")]),

N("that_night", 3, "That Night, at the Kitchen Table", [
 "Home, after. The visit replays the way visits do \u2014 the good minutes first, then the notebook you couldn't see. You know what happened in the room today. You also know that knowing is a substance with a shelf life, and that the file's version is being written by someone else, in ink, tonight.",
 "There is a notebook at the store by the bus stop. There is also your memory, which feels \u2014 tonight, honestly \u2014 like enough.",
], [C("Buy the notebook and write today's visit down tonight \u2014 date, times, what was said, the double shift", "notebook_started", cash=-4,
      setFlags=["ownNotes"],
      addHidden=["Parent's same-day visit notes \u2014 begun the night of the 'flat' visit"],
      note="Three pages, in your handwriting, written while the day is still warm. Contemporaneous is a cold word for a warm practice."),
    C("Trust your memory \u2014 you will remember a day like this one", "memory_trust",
      note="You will remember most of it. The parts that fade first are dates and exact words \u2014 which are, not coincidentally, the parts reviews run on.")]),

N("notebook_started", 4, "Three Pages, Dated", [
 "The notebook's first entry is not literature. It is better than literature: it is dated. The shift, the snack, the game, the book, the sentence you said to Ms. Goss before the visit started, Ezra's joke about the clock. What you felt goes in too, in one line: \u2018Tired. Not checked out.\u2019",
 "You close it understanding something the system rarely says out loud: from tonight, this case has two memories. One of them is yours, and it is being written the same day things happen.",
], [C("Keep the habit \u2014 write every visit the same day, before sleep", "good_visit",
      note="A page a visit. It takes ten minutes. It compounds like interest.")]),

N("memory_trust", 4, "Memory, Kept Warm", [
 "You decide your memory is enough, and tonight it is: the whole visit sits in you complete \u2014 the game, the book, the tiredness, the clock. Memory is a wonderful instrument. Its one flaw is that it cannot be attached to anything. It cannot be handed across a table at a review, or filed, or quoted back by a stranger in September.",
 "The file's memory, meanwhile, is being written tonight too \u2014 by Ms. Goss, from her notebook, in the words she chose in the room.",
], [C("Go on with the visits \u2014 twice a week, the way the plan runs", "good_visit",
      note="Twice a week, the room. Twice a week, the notebook by the wall. Your version lives where it lives.")]),

N("good_visit", 7, "A Good Visit, in Full", [
 f"{D62(7)}'s visit is the other kind: rested, early, Ezra at the door of the room before you are. He has drawn the two of you at a table with an enormous clock, and he explains the drawing the way artists do, without embarrassment. The visit runs its full length. The goodbye is the ordinary hard kind \u2014 a sleeve held a moment longer than the schedule, then released.",
 "Ms. Goss writes at the good parts too. Notes are not accusations; they are simply the file's eyes. What this scenario keeps asking is narrower: when the eyes mis-see, what corrects them?",
], [C("Go home and handle the day the way you have chosen to handle days like this", "fall_visit",
      addHidden=["Visit \u2014 full-length visit; Ezra's drawing of the visit-room clock"],
      note="The good visits go in the file too. Files remember everything with the same flat voice \u2014 which is why the exceptions matter so much.")]),

N("fall_visit", 10, "The Climbing Frame", [
 "Thursday's visit, the play corner. Ezra goes up the visit-room climbing frame the way six-year-olds do \u2014 competently, until he doesn't. He slips near the bottom, lands sitting, and comes up holding his arm, more startled than hurt: a scraped arm, a red mark where his sleeve rode up.",
 "You are there before the sound finishes. You tell Ms. Goss immediately \u2014 what happened, where, how far he fell, which is not far \u2014 and you hold the sleeve up and sit with him until the startle passes and he is negotiating for a bandage with a picture on it. The visit resumes, smaller and closer. He rides the rest of it out against your side.",
], [C("Stay with him until he is ready to play again \u2014 and make sure Ms. Goss saw the whole of it", "fall_aftermath",
      addHidden=["Visit incident \u2014 fall from low on the climbing frame; mother reported it immediately and comforted the child; scraped arm"],
      note="Reported by you, at once, in the room. That is the lived version. The written version is being composed a few feet away.")]),

N("fall_aftermath", 13, "The Note, As Read to You", [
 "Sunday, a call from Mr. Henley, following up the way the plan says someone should. Ezra is fine; the mark is fading; the foster home reports nothing but a story told twice at dinner. Then Mr. Henley reads you the line from the visit note, because you ask what it says: \u2018Bruise observed on child's arm; mother offered no explanation initially.\u2019",
 "\u2018Initially,\u2019 you say. \u2018I explained it before it happened, almost. I was the one who told her.\u2019 He is quiet a moment, in the way of a man reading a sentence he did not write. \u2018That's what the note says,\u2019 he says. It is not unkind. It is worse than unkind: it is final-sounding.",
], [C("Ask him to note your objection \u2014 and write the date of this call down when you hang up", "weeks_pass",
      note="An objection, noted by the person who read you the line, on the day he read it. It is a start. It is not yet an answer in the file.")]),

N("weeks_pass", 24, "The Weeks Between", [
 "The visits go on, twice a week, and most of them are good in the unremarkable way that is the whole point of visits. Ezra grows a fraction. The clock drawing acquires a second clock. Your shifts settle into a pattern you can almost sleep inside.",
 "Somewhere offstage, in an office, the file grows too. A review summary is being drafted from the notes \u2014 summaries always are \u2014 and in it, sentences are being carried from one document into the next, the way sentences in this system travel: quoted, shortened, and ever so slightly re-pointed at each stop.",
], [C("Keep visiting \u2014 and keep whatever record you are keeping", "quote_upgrade",
      note="The summary is being written from the notes. The notes were written from the room. You were in the room. The chain has a weak link, and it isn't you.")]),

N("quote_upgrade", 31, "Quoted, Upgraded", [
 f"The draft review summary reaches your lawyer, and your lawyer reaches you. Most of it is fair. But there, in the concerns paragraph, is a sentence with a familiar skeleton: the {D62(3)} visit at which you were \u2014 the note's word was \u2018flat\u2019 \u2014 is now described as a visit raising a \u2018possible impairment concern.\u2019",
 "Flat was a word about a double shift. Somewhere between the notebook and the summary, it put on a uniform. Nobody in the chain, most likely, meant to promote it. Promotions like that do not require intent. They require only that the original word sit alone in a file, unanswered, while people who never met you quote it to each other.",
], [C("Call your lawyer and ask what can actually be done about a word", "lawyer_beat",
      addHidden=["Review summary \u2014 'flat' quoted and upgraded to 'possible impairment concern'"],
      note="\u2018Done about a word\u2019 is, it turns out, a real legal specialty. It is called the record.")]),

N("lawyer_beat", 34, "What Paper Answers a Word", [
 "Your lawyer \u2014 counsel is your right in this case, as the law provides (42 Pa.C.S. \u00a7 6337) \u2014 listens to the whole biography of the word \u2018flat,\u2019 and then she does the thing lawyers in this series always do: she asks what paper answers it.",
 "\u2018The visit notes are in the agency's case record,\u2019 she says. \u2018You may request the record, and the regulation says it \u201cshall be released upon request\u201d (55 Pa. Code \u00a7 3130.44(d)). Not the summary of the notes. The notes. Until you've read them, every argument about them is two people describing a page neither has open.\u2019",
], [C("Sign the written request for the record \u2014 visit notes, all of them, in writing", "request_sent", cash=-5,
      setFlags=["recordsRequested"],
      note="Signed, dated, copied. Whatever the notes say, you will soon be able to quote them instead of remembering them."),
    C("Wait \u2014 the word is ugly, but the review is the fight; don't open a second one", "request_deferred",
      note="Understandable, and the summary will still be quoted at the review. It will simply be quoted by people who have read the notes, to a person who hasn't.")]),

N("request_sent", 38, "The Stamp", [
 "The request goes in the way requests in this system should always go in: on paper, dated, with a copy kept. Then the ordinary wait, during which the visits continue and the summary with the promoted word in it continues to circulate to everyone except, for a little longer, you.",
], [C("Wait for the packet \u2014 and keep visiting, twice a week, in the meantime", "packet_redacted",
      note="Paper moves at the speed of offices. Visits move at the speed of a six-year-old. You keep both appointments.")]),

N("request_deferred", 38, "Working from the Summary", [
 "Without the notes, your preparation is a hall of mirrors: the summary quotes the notes, the report will quote the summary, and you can answer only the version of the words that has already been through two retellings. Your lawyer works with what exists \u2014 your account, the draft summary, the date of Mr. Henley's call.",
 "It is not nothing. It is simply not the page itself, and this case, like every case in this series, will eventually be decided by people reading pages.",
], [C("Prepare anyway \u2014 you know what happened in that room", "no_packet",
      note="You do. The review will ask a narrower question: what can be shown, and where does it live?")]),
]

s62_nodes += [
N("packet_redacted", 45, "Black Lines", [
 "The packet arrives: the visit notes, months of them, in Ms. Goss's even hand \u2014 and page after page interrupted by black marker. The observations about you and Ezra are mostly there. What is gone, again and again, is the supervisor's own observational writing around them, blacked out under a stamped reason: \u2018staff privacy.\u2019",
 "You read what is visible twice. Even blacked, the notes are a revelation \u2014 the case's memory, in the original hand. But the black bars cover some of the very sentences the summary was built from, and a correction you cannot fully read is a correction half-built.",
], [C("Read the visible parts again, slowly \u2014 then decide about the black lines", "f_beat",
      addHidden=["Records \u2014 visit notes released in part; supervisor's observations redacted as 'staff privacy'"],
      note="The packet is the first document in this case that you and its readers now hold in common. Almost.")]),

N("no_packet", 45, "The Version You Have", [
 "What you have, preparing, is the draft summary, Mr. Henley's phone reading of one line, and your own account of two visits. The summary's promoted word \u2014 \u2018possible impairment concern\u2019 \u2014 sits in the open, unanswered by any document of yours.",
 "There is still one paper move available, and it does not require the packet: a written response, filed into the record, answering the two entries as best you can describe them. Written late and from partial knowledge is weaker than written from the page. It is not the same as unwritten.",
], [C("Decide how to answer \u2014 on paper, or out loud", "correction_beat",
      note="A response built from memory and a summary is a lesser instrument. The ladder has many rungs; the mistake is standing on none of them.")]),

N("f_beat", 48, "The Answer to Black Lines", [
 "Your lawyer reads the stamped reason and shakes her head once, precisely. \u2018The release rule has a limit for other people's privacy,\u2019 she says, \u2018but the same provision says the rule is not to be read to protect agency employees' privacy (55 Pa. Code \u00a7 3130.44(f)). A supervisor's observations of a visit are the agency's work about your family \u2014 not her private life. That distinction is worth one short letter.\u2019",
 "The letter is available to be written: short, dated, addressed to the redactions specifically, asking that the supervisor's visit observations be released. Or the black lines can simply be accepted, and your energy saved for the correction itself.",
], [C("Send the short written response on the redactions, citing the provision", "read_file",
      setFlags=["redactionAnswered"],
      addHidden=["Redactions \u2014 parent responded in writing; supervisor's observations requested under 55 Pa. Code \u00a7 3130.44(f)"],
      note="One page. It does not shout. It cites. What it produces will arrive as paper, the only currency this system mints."),
    C("Accept the black lines \u2014 save your fight for the two entries themselves", "read_file",
      note="A reasonable allocation of a tired person's energy. The blacked sentences stay black, and whatever they say will reach the review unexamined.")]),

N("read_file", 52, "What the File Actually Holds", [
 "With the fuller notes in hand, you sit with the whole file at last. Two entries matter. The bruise line, exactly as Mr. Henley read it: \u2018Bruise observed on child's arm; mother offered no explanation initially.\u2019 And now you can see the note's next page too, where Ms. Goss recorded, two paragraphs later, your account of the fall in detail. The summary that travelled quoted the first sentence. It did not quote the second page.",
 f"And a plainer error, the kind paper exists to catch: the visit of {D62(17)} is marked \u2018missed \u2014 mother did not attend.\u2019 You were there. You remember the rain, the bus, Ezra's wet shoes by the door. If your notebook exists, it remembers them in ink, with the date on the page. If it doesn't, correcting that date will rest on your word against the file's \u2014 which is the whole argument of this scenario, in one line.",
], [C("Take both entries to your lawyer \u2014 it is time to answer them in the same medium they live in", "correction_beat",
      addHidden=["Visit notes as held \u2014 bruise line, with mother's account on the following page; one attended visit marked missed"],
      note="The file, read whole, is less frightening and more answerable than the summary of it. That is usually true. It is why summaries fear files.")]),

N("correction_beat", 55, "Answer in Writing, or Out Loud", [
 "Your lawyer lays out the last fork of the summer plainly. The two entries \u2014 the bruise line and, behind it, the promoted word \u2018flat\u2019 \u2014 can be answered by a short written response filed into the record: what happened, in order, with any same-day notes you kept attached, so that the file forever after holds each entry and its answer side by side.",
 "Or they can be answered out loud at the review, by you, in the room \u2014 sincerely, probably persuasively, and entirely dependent on whether the person writing the next summary chooses to carry your sentences forward the way they carried \u2018flat.\u2019",
], [C("File the written response \u2014 both entries answered, your notes (if you kept them) attached", "correction_filed_node", cash=-6,
      setFlags=["correctionFiled"],
      note="Dated, copied, filed. From today, anyone who quotes an entry from the file will find its answer in the same folder, at the same stop."),
    C("Raise it orally at the review \u2014 say it to the room, where people can hear you mean it", "correction_oral_node",
      note="They will hear you mean it. Meaning it has never been the scarce resource in this case. Paper is.")]),

N("correction_filed_node", 56, "Filed, Beside Them", [
 "The response is two pages and no adjectives worth mentioning: the fall, in sequence; the explanation, given immediately and recorded on the note's own second page; the word \u2018flat,\u2019 with its double shift attached; the missed visit that wasn't, with its date corrected. Where your notebook exists, its pages ride along as attachments, and the clerk's stamp lands on the whole packet at once.",
 "Nothing about the filing is dramatic. That is rather the point. The file now contains two versions, and \u2014 this is the part that matters \u2014 it contains them together, where every future quoter will meet them together.",
], [C("Go on visiting \u2014 the review is next, and the file going into it is no longer one-handed", "review_prep",
      note="Entries travel. From now on, yours travel with company.")]),

N("correction_oral_node", 56, "Rehearsed, Unfiled", [
 "You rehearse the answer with your lawyer until it is tight: the fall, the immediate report, the double shift behind \u2018flat.\u2019 It is true, it is ordered, and it exists in exactly one place \u2014 your voice, on a Thursday, in a room where summaries are written afterward by other people.",
 "\u2018Say it well,\u2019 your lawyer says. \u2018Then understand that what survives of it is whatever the next summary decides to carry \u2014 the same process that promoted \u201cflat\u201d will now be in charge of your answer to it.\u2019",
], [C("Go to the review ready to say it \u2014 clearly, and in order", "review_prep",
      note="A good speech, prepared. The file it will land in is written by listeners.")]),

N("review_prep", 66, "The Packet, in Date Order", [
 "The week before the review, your lawyer assembles the packet the way this series has taught you everything is assembled: in date order. The notes. The redactions, answered or accepted. Your response, filed or rehearsed. The summary that promoted a word, next to the page the word came from.",
 "Ezra, meanwhile, has opinions about the review only insofar as it touches visits. It does not, directly. It touches what every future reader of his file will believe about his mother in July. He will never read the packet. He will live downstream of it.",
], [C("Read the review notice when it comes \u2014 date, room, and the report that will be on the table", "review_notice",
      note="Date order. The summer, testified to by its own paperwork.")]),

N("review_notice", 69, "The Report on the Table", [
 "The review report arrives, and it is the draft summary grown up: fair about the visits in general, specific about the two entries in particular. \u2018Possible impairment concern\u2019 is there, in the concerns paragraph, with the bruise line beneath it as support \u2014 two quotations, holding each other up, neither of them yet met by an answer in the same document.",
 "Whether that changes on review day depends, with a precision this scenario has been honest about since its first scene, on what your summer put into the file before the hearing \u2014 and on which lead your lawyer can honestly open with.",
], [C("Go to the review", "review",
      note="Small room, enormous job: deciding what the file will say about the summer.")]),

N("review", 73, "The Review", [
 "The review is a small room doing an enormous job: deciding what the file will say about the summer, and therefore what the plan will ask of the autumn. Mr. Henley presents. The report's two entries are read aloud in the flat voice people use for other people's paper. Then it is your side's turn, and your lawyer looks at the packet \u2014 at what is actually in it \u2014 and chooses her lead.",
], [C("Open with the filed correction \u2014 your same-day notes attached, the redactions answered, both entries met on the record", "end_answered",
      requiresFlags=["ownNotes", "recordsRequested", "correctionFiled", "redactionAnswered"],
      note="This lead exists only because every piece of it was built before today: the notebook, the request, the letter, the filing. The room is just where they are spent."),
    C("Open with the filed correction alone \u2014 your version, in writing, beside theirs", "end_two_versions",
      requiresFlags=["correctionFiled"],
      note="A real answer, on paper, in the file. What it lacks is the same-day paper behind it \u2014 and the room will feel the difference."),
    C("Answer out loud \u2014 tell the room the fall, and the double shift, in order", "end_two_versions",
      requiresNoFlags=["correctionFiled"],
      note="Sincere, specific, and spoken. What survives of it will be decided by the next summary, as 'flat' was decided by the last one."),
    C("Let the report stand and talk about how the visits are going now", "end_flat",
      note="The visits are going well. The report is not about how the visits are going. It is about what the file says \u2014 and the file has just been read aloud, unanswered.")]),

N("end_answered", 80, "Ending \u2014 The Note, Answered", [], ending=True, debrief=[
 "WHAT THE FILE HELD (the hidden record, revealed): Both entries, and both answers, in the same folder. The bruise line \u2014 answered by the note's own second page, which recorded your explanation in detail, and by your filed correction, which quoted it. The word \u2018flat\u2019 \u2014 re-anchored to the double shift by your same-day notebook page, written the night it happened. The attended visit marked missed \u2014 corrected, with the notebook's dated page beside it. And the supervisor's observations \u2014 released after your written response, because the release rule is not to be read to protect agency employees' privacy (55 Pa. Code \u00a7 3130.44(f)). At the review, the concerns paragraph was rewritten: the entries stand, with their answers attached, and \u2018possible impairment concern\u2019 came out \u2014 replaced by what the record, read whole, actually shows.",
 "THE LAW UNDER THIS PATH (kept to this scenario's verified set): The notes reached you because agency records \u2018shall be released upon request\u2019 (55 Pa. Code \u00a7 3130.44(d)) \u2014 exercised in writing, so the asking itself is provable. The redactions yielded to the same regulation's own limit on its limit, \u00a7 3130.44(f), used exactly as far as it goes: a supervisor's visit observations are the agency's work about your family, not her private life. Counsel (42 Pa.C.S. \u00a7 6337) assembled, attached, and filed. Say plainly what was won: Ezra is still placed, visits are still supervised, and no order today ends this case. What changed is the record every future decision will be read from \u2014 answered, dated, and no longer quotable in halves.",
 "THE HONEST PART: A different supervisor might have written the fall note whole the first time, and none of this would have been necessary; a different reviewer could have kept the concern language even against the full packet, and some do. Ms. Goss's caseload, Mr. Henley's habits, the reviewer, and plain luck all hold pieces of this outcome alongside your work. This ending is not a verdict on you as a mother \u2014 the facts were always on your side here; what your choices changed is that the file finally knows them, in ink, beside the entries that misstated them. In this system, that is what an answer is.",
]),
N("end_two_versions", 80, "Ending \u2014 Two Versions, One File", [], ending=True, debrief=[
 "WHAT THE FILE HELD (the hidden record, revealed): Two versions, sharing one file, neither fully displacing the other. Your account of the fall and of the word \u2018flat\u2019 exists in the record \u2014 filed, or spoken at the review and partly carried into its summary \u2014 but it arrived late, or thin, or without the same-day paper behind it, and the review treated the two entries as contested rather than corrected. The concern language softened; it did not come out. The missed-visit date may or may not have moved, depending on what could be shown for it. Future readers will meet both versions and will have to choose, file in hand, which one the surrounding paper supports.",
 "THE LAW UNDER THIS PATH (kept to this scenario's verified set): Every tool that built the best ending was available on this path too, and the ones used here did real work: a response filed into the record is durable in a way a speech is not, and counsel (42 Pa.C.S. \u00a7 6337) could present it because it existed. What limited it is the same mechanism, run in reverse: the notes themselves are released on request (55 Pa. Code \u00a7 3130.44(d)), and a correction built from the actual pages \u2014 including the note's own second page, and the supervisor's observations answerable under \u00a7 3130.44(f) \u2014 answers quotations with quotations. A version built from memory answers them with sincerity. Reviews price the difference, because reviews can only price what is in front of them.",
 "THE HONEST PART: Contested is not nothing. Against a draft that began as an unanswered \u2018possible impairment concern,\u2019 a file that now argues with itself is movement \u2014 and at the next review, a fuller record can still be built, starting from the version you planted here. Judges and reviewers differ in how much weight they give a parent's late paper against a file's early sentences, and this one split the difference, as many do. Workers, supervisors, and luck are in this ending too. What your choices controlled was whether the file's memory of this summer would be the only memory in the room. It wasn't. It just wasn't the only one that arrived with dates on it.",
]),
N("end_flat", 80, "Ending \u2014 Flat, As Recorded", [], ending=True, debrief=[
 "WHAT THE FILE HELD (the hidden record, revealed): One version, unanswered. The word \u2018flat,\u2019 promoted by quotation into a \u2018possible impairment concern,\u2019 now sits in the review's findings, with the bruise line beneath it as support \u2014 its second page, the one recording your explanation, unquoted, because no one put it in front of the room. The attended visit marked missed still reads as missed. None of this was found against you after a contest. It hardened by default, the way unopposed sentences do: each document quoted the last, and the quotations agreed with each other because they were the same sentence travelling.",
 "THE LAW UNDER THIS PATH (kept to this scenario's verified set): The instruments all existed, unused or used too late: the visit notes were yours on written request \u2014 they \u2018shall be released upon request\u2019 (55 Pa. Code \u00a7 3130.44(d)); the blacked-out observations were answerable under the same provision's rule that it is not to be read to protect agency employees' privacy (\u00a7 3130.44(f)); and counsel (42 Pa.C.S. \u00a7 6337) was there to file the correction that would have travelled with the entries. None of that is gone: a record can be answered at the next review too, and a folder begun late is worth more than this paragraph's regret. But the findings written today are the findings the next summary will quote, and quotations, as this scenario has shown from its first scene, are how words get promoted.",
 "THE HONEST PART: Let this debrief be as fair as the file wasn't: you reported the fall immediately, in the room, before anyone asked; you were tired because you had worked a double shift to keep the household this case is measuring; and Ezra's visits, in the lived sense, went well. The failure in this ending is not a failure of parenting or even of effort. It is a failure of answer \u2014 nobody handed the system the exchange rate between living a fact and filing it until the findings were already written. A fuller first note, a smaller caseload, a supervisor who quoted her own second page \u2014 any of those lucks change this ending without you changing at all. Outcomes here turn on workers, reviewers, and luck. Your share, next time, is the notebook, the request, and the filing \u2014 the three unglamorous objects that decide what a word becomes.",
]),
]

s62 = build(
 {"title": "The First 90 Days",
  "subtitle": "Scenario 62 \u2014 The Visit Notes (a fictional composite)",
  "startDateISO": "2026-07-06", "startNode": "start", "startCash": 110,
  "tier": "Hard",
  "summary": "The visit notes are the case's memory \u2014 and two entries in them are quietly becoming findings."},
 s62_nodes, S62_START)
assert len(s62_nodes) == 26, len(s62_nodes)
assert sum(1 for n in s62_nodes if n.get("ending")) == 3

# =====================================================================
# SCENARIO 63 \u2014 Cancelled, Again
# Opens Monday, August 3, 2026. Felix, 8, placed before the story opens;
# no removal occurs in-story (no `removed` flag, by design).
# Report window arithmetic (stated in-game, machine-checked below):
# real schedule Aug 4 - Sep 12: 6 Tuesdays + 6 Saturdays = 12 visits;
# 3 cancelled by the center; 9 held; Simone attended all 9 held.
# The center's summary counts 15 "scheduled" (12 + 3 make-up slots it
# logged but never gave dates for): 9/15 = 60%. Corrected: 9 of 9 held.
# =====================================================================
S63_START = date(2026, 8, 3)
assert S63_START.strftime("%A") == "Monday"
def D63(off):
    return fmt(S63_START + timedelta(days=off))
# visit-day audit: offsets of Tuesdays/Saturdays in the report window
_window = [S63_START + timedelta(days=i) for i in range(1, 41)]  # Aug 4 .. Sep 12
_tue_sat = [d for d in _window if d.strftime("%A") in ("Tuesday", "Saturday")]
assert len(_tue_sat) == 12, len(_tue_sat)
assert 9 * 100 // 15 == 60

s63_nodes = [
N("start", 0, "Tuesdays and Saturdays", [
 "Your name is Simone. Your son Felix is eight, and he is living in foster care \u2014 placed before this story opens, in a part of the case this story does not retell. What this story covers is the rhythm the case now runs on: visits, Tuesdays and Saturdays, at a visitation center across town.",
 "The center's habit is a phone call. The day before a visit, someone rings to confirm \u2014 or you ring them. Ms. Kessler, who runs the desk, is brisk and not unkind, and the calls are pleasant, and at the end of each one nothing exists that a third person could read. In this system, that last part is not a detail. It is the whole mechanism of the next two months.",
 "You attend your visits. That sentence is true, simple, and \u2014 as the summer will show \u2014 surprisingly hard for a file to say, if the file is built out of phone calls.",
], [C("Go to the first Tuesday visit \u2014 and think about the phone call that confirmed it", "confirm_choice",
      note="A visit, confirmed by a voice, attended by a mother, recorded by no one. Hold that thought.")]),

N("confirm_choice", 1, "The Day Before", [
 f"It is {D63(1)}, visit day, and yesterday's confirmation was the usual call: two minutes, friendly, gone. There is another way to confirm a visit, and it costs nothing but the small awkwardness of being the person who puts things in writing: a short text or email the day before \u2014 visit, date, time, \u2018please confirm\u2019 \u2014 which the center answers, or doesn't, in writing either way.",
 "Paper (and its digital cousins) have dates on them. Phone calls have memories on them. This case will be decided, in part, by which of those your confirmations are made of.",
], [C("Start confirming in writing \u2014 a short message the day before every visit, replies saved", "written_start",
      setFlags=["confirmWritten"],
      addHidden=["Visits \u2014 confirmed in writing the day before, from the first week"],
      note="The first reply is two words: \u2018Confirmed, thanks.\u2019 Two words, with a date on them. That is what evidence looks like before it grows up."),
    C("Keep phoning \u2014 it works, it's friendly, and Ms. Kessler knows your voice", "phone_start",
      note="She does know your voice. Voices, unfortunately, cannot be attached to a review report.")]),

N("written_start", 2, "Two Words, Dated", [
 "The thread begins: your message, the center's reply, your message, the reply. It is the dullest correspondence in the world and, potentially, the most valuable paper in your case \u2014 a dated, third-party confirmation for every visit, written by the center itself, before anything about the visit could be disputed.",
 "You save the replies the way you save receipts. Somewhere, an attendance percentage is going to be computed about you this year. When it is, there will be something to compute it against.",
], [C("Go on with the visits \u2014 Tuesdays and Saturdays, confirmed the day before", "good_weeks",
      note="A rhythm with a paper shadow. The summer can now begin, in both versions.")]),

N("phone_start", 2, "The Friendly System", [
 "The calls continue, warm and weightless. Ms. Kessler confirms; you attend; the visit happens; the call evaporates. If anyone ever asks whether a given visit was confirmed, the answer will live in two people's recollections, one of whom answers phones for forty families.",
 "None of this feels like a mistake. That is what makes it one of this system's most reliable traps: the informal way works perfectly, right up until the moment it is asked to prove something.",
], [C("Go on with the visits \u2014 Tuesdays and Saturdays, as confirmed by phone", "good_weeks",
      note="The visits are real. Their confirmations are weather: true, and gone.")]),

N("good_weeks", 8, "The Good Weeks", [
 "The first full week runs the way weeks are supposed to: Tuesday's visit, Saturday's visit, Felix at the center-room door with his shoes already off and an agenda already formed. He is working on a drawing series \u2014 the center, the bus, your kitchen, the center again \u2014 and each visit adds a panel.",
 "This is what attendance actually looks like from inside it: buses, snacks, drawings, the ordinary machinery of showing up. Files do not see machinery. Files see counts. The distance between those two views is where this scenario lives.",
], [C("Keep the rhythm \u2014 and keep whatever record of it you are keeping", "second_saturday",
      note="Showing up is the job. Proving you showed up, it turns out, is a second job, running in parallel, unpaid.")]),

N("second_saturday", 12, "The Drawing, Panel Four", [
 f"{D63(12)}'s visit is the good kind that leaves nothing to write home about: a board game Felix has decided to be magnanimous about losing, a sandwich negotiated down to its crusts, the drawing's fourth panel \u2014 your kitchen, with the table set for two and a third chair drawn in pencil, \u2018for later.\u2019",
 "Ms. Kessler, passing with a clipboard, says the thing staff say: \u2018You're one of my reliables.\u2019 It is true, it is kind, and it will appear nowhere. Praise, in this building, is spoken. Counts are written. Remember which one the report will use.",
], [C("Thank her \u2014 and go home on the bus with panel four in your bag", "cancel1",
      addHidden=["Visit held \u2014 full visit; Felix's drawing, panel four"],
      note="\u2018One of my reliables.\u2019 File that under things that are true and unprovable, unless the paper says otherwise.")]),

N("cancel1", 15, "Cancelled, the First Time", [
 f"{D63(15)}, visit morning. Your phone rings while the kettle is on: Ms. Kessler, apologetic, brisk. The center is short-staffed today; today's visit is cancelled. \u2018We'll find you a make-up slot,\u2019 she says, \u2018when there's a slot.\u2019 There is no date in that sentence. There is barely a noun in it.",
 "This happens, in this system, more often than any report admits: a visit cancelled by the provider's arithmetic, not by the parent's. What happens next \u2014 in the file, I mean \u2014 depends on what you do in the next hour.",
], [C("Answer the same day in writing \u2014 sorry to miss Felix, please propose a make-up date, in reply", "cancel1_written",
      setFlags=["cancelTrail"],
      addHidden=["Cancellation 1 \u2014 center cancelled by phone, morning of; parent answered the same day in writing requesting a make-up"],
      note="Your message is short, warm, and dated, and it asks for the one thing the phone call didn't contain: a date. The asking is now a record."),
    C("Accept the verbal promise \u2014 \u2018we'll find a slot\u2019 \u2014 and hang up kindly", "cancel1_verbal", cash=-6,
      note="Kindly is how you do everything. The promise, meanwhile, has no date, no witness, and no existence outside Ms. Kessler's memory of a busy morning. (And you had already paid the bus fare before the phone rang.)")]),

N("cancel1_written", 16, "A Reply with No Date in It", [
 "The center replies the next day, in writing, which is its own small victory: \u2018Noted \u2014 we'll offer a make-up when there's a slot.\u2019 You read it three times. The sentence confirms the cancellation was theirs. It confirms you asked. It does not contain a date, a day, or a time, and you understand, holding it, that \u2018when there's a slot\u2019 is a place where make-up visits go to be forgotten politely.",
 "You save it anyway. A reply that promises nothing still proves two things: who cancelled, and that you answered in writing the same day. Percentages are computed from less.",
], [C("Save it, and go to Saturday's visit as scheduled", "held_visit2",
      note="Who cancelled: documented. Make-up: vaporous. Both halves matter, and now both halves exist.")]),

N("cancel1_verbal", 16, "When There's a Slot", [
 "No reply exists, because no message was sent. In the center's day, the cancellation was one of eleven phone calls; in yours, it was the day's whole weather. Ms. Kessler meant the promise. Meaning a promise and scheduling it are different departments, and only one of them keeps a calendar.",
 "Saturday's visit is still on, confirmed the usual way. You go, because going is what you do \u2014 and because some part of you already suspects that going, undocumented, is a tree falling in a forest of forms.",
], [C("Go to Saturday's visit \u2014 showing up is still the main thing", "held_visit2",
      note="It is the main thing. The scenario's whole argument is that \u2018main\u2019 and \u2018only\u2019 are different words.")]),

N("held_visit2", 22, "A Held Visit", [
 f"{D63(22)}: a visit that happens, which in this summer's accounting is becoming a category worth naming. Felix has opinions about the cancelled one \u2014 children keep their own attendance records, in a medium adults can't file \u2014 and then the visit does what visits do: game, sandwich, drawing, goodbye at the door with his hand up, palm out, the way he waves now.",
 "You attend. As you attend every visit that is actually held. If the summer's file could see the room, there would be no scenario. The file sees counts, and the counts are being kept by the party that cancels.",
], [C("Go home \u2014 and, whenever the make-up is mentioned, notice whether a date is attached", "makeup_chase",
      note="Held: attended. Cancelled: pending a date that does not exist. The arithmetic is already drifting, and arithmetic drifts downhill.")]),

N("makeup_chase", 26, "Chasing the Make-Up", [
 f"{D63(26)}, a held visit \u2014 and at the desk, the make-up question, raised again. \u2018Still nothing,\u2019 Ms. Kessler says, not unkindly. \u2018You're on the list.\u2019 There is a list. You have never seen the list. The list, if it says anything about dates, has not said it to you.",
 "There are two ways to leave this conversation: with a dated written record that you asked, again \u2014 or with the warm understanding of two people who both intend well, which is the raw material from which \u2018the parent never followed up\u2019 is later manufactured.",
], [C("Follow up in writing that evening \u2014 second request for a make-up date for the cancelled Tuesday", "cancel2",
      setFlags=["cancelTrail"],
      addHidden=["Make-up request \u2014 repeated in writing; center replied 'when there's a slot,' no date given"],
      note="Asked, again, in writing, again with a date on the asking. The file is learning a pattern, even if the calendar isn't."),
    C("Leave it with Ms. Kessler \u2014 you're on the list, and pushing helps no one", "cancel2",
      note="On the list. The list is the most trusted and least examined document in this entire system.")]),

N("cancel2", 29, "Cancelled, Again", [
 f"{D63(29)}. The phone rings in the morning, and you know the shape of the call before the kettle boils: staffing, apologies, cancellation \u2014 the second one. \u2018Same as before,\u2019 Ms. Kessler says, \u2018we'll find a slot.\u2019 Two make-ups are now owed to Felix's summer, in a currency of slots that has never once been observed in the wild.",
 "A pattern cancelled once is an accident. Cancelled twice, with no make-up dated, it is a system describing itself. What the review will call it depends on the paper.",
], [C("Answer in writing the same day, as before \u2014 cancellation noted, make-up requested, again", "rumor_beat",
      setFlags=["cancelTrail"],
      addHidden=["Cancellation 2 \u2014 center cancelled by phone; parent answered the same day in writing requesting a make-up"],
      note="Same day, in writing, second time. A trail is just a thing that happens twice with dates on it."),
    C("Accept it verbally, as before \u2014 they know you're reliable", "rumor_beat", cash=-6,
      note="They do know. Knowledge held by a busy desk, about forty families, across a summer, is a depreciating asset. (The bus fare, again, was already spent.)")]),

N("rumor_beat", 33, "Sixty-Something Percent", [
 f"A held visit, {D63(33)} \u2014 and at the door afterward, the foster parent mentions, in the careful voice people use for other people's paperwork, something she heard on a call with the agency: Simone's attendance described as \u2018not great \u2014 sixty-something percent, they said.\u2019",
 "Sixty-something. You do the first arithmetic standing in the doorway, and it does not work on any numbers you know: you have attended every visit that has ever actually been held. Unless \u2014 and the thought arrives whole \u2014 the cancelled ones are being counted as yours. A percentage is a fraction. Fractions have two halves. You have been watching the top half. Someone else owns the bottom.",
], [C("Go home and start counting from your own records \u2014 every scheduled visit since August", "cancel3",
      note="Scheduled. Held. Cancelled. Attended. Four different numbers wearing one another's coats. Time to separate them.")]),

N("cancel3", 40, "Halfway There", [
 f"{D63(40)} \u2014 a Saturday. You are on the bus, halfway to the center, Felix's snack in your bag and panel nine of the drawing series promised for today, when the phone rings. Staffing. Apologies. Cancelled \u2014 the third time in two months. The bus continues for one more stop out of pure momentum before you can get off.",
 "\u2018When there's a slot,\u2019 Ms. Kessler says, completing the set. Three cancellations, three promises, zero dates. You stand at a bus stop in the wrong half of town, holding a sandwich bag, being reliable at a cancelled visit.",
], [C("Text the center from the bus stop, in writing \u2014 cancellation noted, make-up requested, third time", "bus_ride_home", cash=-7,
      setFlags=["cancelTrail"],
      addHidden=["Cancellation 3 \u2014 Saturday; parent already travelling when the center cancelled; written notice sent the same day"],
      note="Sent from a bus stop, timestamped by the network itself. If a trail could have a monument, this is it."),
    C("Call back and accept it verbally \u2014 the bus home is not the place for paperwork", "bus_ride_home", cash=-7,
      note="The fare is spent either way. What differs is whether today's cancellation joins the others in writing, or in memory.")]),

N("bus_ride_home", 41, "The Long Way Back", [
 "The bus home takes the long way, as buses do when the trip has no visit at the end of it. You think about Felix being told, by someone, in some words, that today's visit is off \u2014 and about what word will be used for it in the summary of the summer, and whose name will be grammatically attached to the cancellation when it gets there.",
 "Summaries assign. That is their job and their danger. A cancellation described without an owner tends to acquire the nearest name \u2014 and the nearest name, in an attendance paragraph, is always the parent's.",
], [C("Get home, and do the full count at the kitchen table", "monday_after", cash=-6,
      note="Return fare: spent on a visit that didn't happen. Some expenses are also evidence.")]),

N("monday_after", 42, "The Count", [
 f"At the kitchen table, the count, for the report window the summer will be judged on \u2014 {D63(1)} to {D63(40)}: twelve visits scheduled, Tuesdays and Saturdays. Three cancelled by the center. Nine actually held. You attended nine. Nine of nine held visits: every single one.",
 "And yet a voice on a phone call said sixty-something. Twelve scheduled and nine attended is seventy-five percent, not sixty \u2014 so even counting the center's cancellations against you doesn't reach their number. Something else is in their denominator. You can guess at it. Guessing, as this series never tires of showing, is what you do instead of reading the file.",
], [C("Write the count down, dated, with the four numbers separated", "tally_night",
      addHidden=["Parent's tally \u2014 12 scheduled, 3 cancelled by the center, 9 held, 9 attended"],
      note="Four numbers, separated at last. Now: where did fifteen come from \u2014 because sixty percent of their count means their count isn't twelve.")]),

N("tally_night", 43, "Nine of Nine", [
 "Nine of nine. You sit with the fraction a while. It is, as a measure of a mother, perfect \u2014 and, as a document, worthless, because it is yours: your count, your table, your word. The report's number will arrive wearing the agency's letterhead, and letterhead is a kind of armour that kitchen-table arithmetic does not pierce by itself.",
 "What pierces it is the agency's own paper, read closely: their attendance summary, their cancellation log, their denominator, in their hand. There is a way to ask for that paper. There has been, all along.",
], [C("Ask your lawyer how to get the center's own numbers \u2014 before the review does its arithmetic without you", "records_beat",
      note="\u2018Their number, their paper.\u2019 Your lawyer is already nodding. This is her favourite kind of fight: one where the other side has already written everything down.")]),
]

s63_nodes += [
N("records_beat", 44, "Their Number, Their Paper", [
 "Your lawyer \u2014 counsel is your right in this case, as the law provides (42 Pa.C.S. \u00a7 6337) \u2014 lays it out in one breath: \u2018You may request the case record, and the regulation says it \u201cshall be released upon request\u201d (55 Pa. Code \u00a7 3130.44(d)). We ask for the attendance summary and the center's scheduling log. Their percentage was computed from something. We are going to read the something.\u2019",
 "The request is one page. It asks for the paper behind a number that has already been said out loud about you on a phone call \u2014 which makes it, in the quiet taxonomy of this system, not early and not late, but exactly on time.",
], [C("Sign and send the written request \u2014 attendance summary and scheduling log, in writing", "packet_arrives", cash=-4,
      setFlags=["recordsRequested"],
      note="Signed, dated, copied. The denominator is about to have an author you can quote."),
    C("Skip it \u2014 your own count is right, and the review will listen to reason", "no_packet63",
      note="Your count is right. Reviews, as a species, listen to records. Reason is admitted only when it arrives as an attachment.")]),

N("packet_arrives", 50, "Fifteen", [
 "The packet arrives, and there it is, in the center's own summary: \u2018Family attended 9 of 15 scheduled visits (60%).\u2019 Fifteen. Your count said twelve \u2014 and the scheduling log, read line by line with your lawyer, explains the extra three: make-up slots the center logged as \u2018scheduled\u2019 after each cancellation, on dates it never gave you, at times it never sent. You were marked absent from visits you were never told existed.",
 "And the three real cancellations? In the summary's arithmetic they sit in your column as visits not attended \u2014 the center's staffing folded, silently, into the family's percentage. Nine of nine held visits became sixty percent of fifteen scheduled ones. Every step of that transformation is on paper. Their paper. That is what makes it answerable.",
], [C("Ask your lawyer what the corrected table needs \u2014 line by line, from their own log", "prep_beat",
      addHidden=["Attendance summary \u2014 15 'scheduled,' 9 attended (60%); provider cancellations and unannounced make-up slots folded into the parent's percentage"],
      note="Their number, their paper, their log. The correction will not need a single fact from outside their own file.")]),

N("no_packet63", 50, "Your Count Against Their Letterhead", [
 "Without the packet, your preparation is your kitchen-table count and whatever written trail the summer left: confirmations, if you made them in writing; cancellation replies, if you answered in writing. True numbers, honestly kept \u2014 and authored by the one person the review is already inclined to treat as an interested party: you.",
 "Your lawyer is blunt about the physics. \u2018If their summary says sixty percent and your page says nine of nine, the room believes the summary until your page is made of their paper. We go in with what we have. It is less than we could have had.\u2019",
], [C("Prepare anyway \u2014 build the best table your own records allow", "prep_beat",
      note="A table built from your own trail is still a table. Whether it can move their number depends on how much of the trail is in writing.")]),

N("prep_beat", 53, "The Corrected Table", [
 "The last week before the review offers the scenario's final fork, and it is pure paperwork. The corrected table exists to be built: four columns \u2014 scheduled, cancelled by the center, actually held, attended \u2014 every row dated, the confirmations and cancellation replies attached, the center's own log lines quoted where you have them. Attached, it goes into the review packet, where percentages are read.",
 "Or you can go in with the story: three cancellations, a bus ride, a promise made three times. The story is true, and moving, and takes four minutes to tell, in a hearing that runs on attachments.",
], [C("Build the corrected table with your lawyer and attach it to the review packet", "table_built", cash=-5,
      setFlags=["mathAttached"],
      addHidden=["Corrected attendance table \u2014 12 scheduled, 3 cancelled by the center, 9 held, 9 attended; confirmations and replies attached"],
      note="Four columns, twelve rows, every number sourced. Arithmetic, dressed for court."),
    C("Go in with the story \u2014 tell it clearly, in order, and trust the room", "story_ready",
      note="The room may well believe you. Believing and correcting a written finding are, as ever, two different procedures.")]),

N("table_built", 54, "Four Columns", [
 "The table is one page and it is beautiful in the way only arithmetic can be: twelve scheduled visits, each with its date; three cancelled by the center, each with the date of your same-day written answer; nine held; nine attended. At the bottom, your lawyer adds the center's own figure, quoted from its summary, and the three logged make-up slots nobody was ever told about \u2014 the whole transformation, visible at a glance.",
 "Sixty percent, it turns out, was never a measure of you. It was a measure of a denominator. Denominators can be corrected. That is what the review is for \u2014 when someone brings the correction in writing.",
], [C("File it with the review packet \u2014 and go to the last visits before the hearing", "review_notice",
      note="Filed, copied, attached. The number going into the review now has competition.")]),

N("story_ready", 54, "The Story, Rehearsed", [
 "Your lawyer rehearses you until the story is tight: the three phone calls, the three promises, the bus. It is true in every particular and it will be believed, probably, in the way stories are believed in rooms that run on exhibits \u2014 warmly, personally, and without the percentage moving, because a percentage is a document and can only be corrected by another document.",
 "\u2018Tell it well,\u2019 she says. \u2018Then watch what the finding says. Findings quote paper. If the finding moves at all, it will move toward the make-ups \u2014 those, a room can grant on a story. The number needs the table.\u2019",
], [C("Go to the review with the story \u2014 and ask, at minimum, for the make-ups to be ordered", "review_notice",
      note="A true story, well told. In this system, that buys more than nothing and less than arithmetic.")]),

N("review_notice", 57, "Sixty Percent, in Print", [
 f"The review report arrives ahead of the hearing, and there, in the attendance paragraph, the summer has been summarized in one line: \u2018Family attended 60% of scheduled visits.\u2019 {D63(57)}'s report was written from the center's summary, the way reports are \u2014 which is to say, the number has now been quoted into a second document, and quotations, as this series keeps showing, are how numbers harden.",
 "Whether it hardens further \u2014 into the plan's findings, where it will shape what the autumn asks of you \u2014 depends on what is lying on the table next to it when the room convenes: a corrected table, a set of dated replies, a story, or nothing.",
], [C("Go to the last visits, and then to the review", "last_visits",
      note="The line is printed. Printed lines can still be corrected \u2014 by better-printed lines, attached in time.")]),

N("last_visits", 58, "Panel Ten", [
 "The visits before the review are held, both of them, and attended, both of them \u2014 the streak that the report's percentage somehow describes as sixty. Felix presents panel ten of the drawing series: the review building, as imagined by an eight-year-old, with many windows and, in the largest one, a table with four columns. He has been listening more carefully than anyone knew.",
 "\u2018That's the counting room,\u2019 he says. He is not wrong. Tomorrow, the counting happens.",
], [C("Go to the review", "review",
      note="Nine of nine, and counting. What the room does with the count is the last scene of the summer.")]),

N("review", 60, "The Review", [
 "The review convenes. The report is presented; the attendance paragraph is read aloud in the level voice reserved for numbers: \u2018Family attended 60% of scheduled visits.\u2019 Nobody in the room experiences that sentence as an accusation. It is simply what the file says \u2014 which is exactly the problem your whole summer has been about.",
 "Then it is your side's turn. Your lawyer looks at what the summer actually put on paper \u2014 the confirmations, the replies, the log, the table \u2014 and chooses her lead.",
], [C("Present the corrected table \u2014 confirmations, same-day cancellation replies, and the center's own summary and log attached", "end_corrected",
      requiresFlags=["confirmWritten", "cancelTrail", "recordsRequested", "mathAttached"],
      note="This lead exists only because every layer of it was built before today: written confirmations, written answers, the requested record, the attached arithmetic. The room is just where they are spent."),
    C("Present the cancellation replies and ask for the make-up visits to be ordered with dates", "end_makeups",
      requiresFlags=["cancelTrail"],
      note="The replies prove the cancellations were the center's and that you asked, in writing, every time. A room can grant dates on that paper \u2014 even if it leaves the number alone."),
    C("Tell the story of the three cancellations and ask for the make-ups", "end_makeups",
      note="True, in order, and believed in the way stories are believed. Make-ups live within a story's reach. Percentages don't."),
    C("Say the visits \u2018mostly happened\u2019 and move on to services", "end_poor",
      note="\u2018Mostly happened\u2019 is, not coincidentally, almost exactly what sixty percent says. The room nods, and the number keeps its coat.")]),

N("end_corrected", 66, "Ending \u2014 Sixty Percent, Corrected", [], ending=True, debrief=[
 "WHAT THE FILE HELD (the hidden record, revealed): A denominator, taken apart on the record. The center's summary counted 15 \u2018scheduled\u2019 visits: your real 12, plus 3 make-up slots it logged but never gave you dates for \u2014 and it folded its own 3 staffing cancellations into your column as visits not attended. Against that, your attached table set the four true numbers side by side, every row sourced: 12 scheduled, 3 cancelled by the center, 9 held, 9 attended \u2014 nine of nine. The confirmations were the center's own replies; the cancellation answers were dated the days the calls came in; the log lines were quoted from the record you requested. At the review, the attendance finding was corrected on the record to the table's arithmetic, and the three lost visits were ordered made up, with dates this time. The plan's language going forward describes a parent who attended every visit that was held.",
 "THE LAW UNDER THIS PATH (kept to this scenario's verified set): The paper that decided this ending was obtained the way this series always obtains it: the case record \u2014 including the attendance summary and the scheduling log behind it \u2014 \u2018shall be released upon request\u2019 (55 Pa. Code \u00a7 3130.44(d)), requested in writing by a party whose counsel (42 Pa.C.S. \u00a7 6337) then built the correction out of the agency's own lines. No new right was invented here; arithmetic is not a legal doctrine. Say plainly what was won: Felix is still placed, visits still run Tuesdays and Saturdays at the center, and no order today ends this case. What changed is the finding every future summary will quote \u2014 and the three make-up visits, ordered with dates, are real hours with your son that the old number would never have produced.",
 "THE HONEST PART: A center with fuller staffing never cancels, and none of this is necessary; a different reviewer could have noted the table and kept the percentage anyway, on the theory that summaries are entitled to their conventions \u2014 some do. Ms. Kessler's memory, the agency's report habits, the reviewer, and luck all hold pieces of this outcome. This ending is not a verdict on you as a mother: you attended every held visit on every path through this scenario, including the worst one. What your choices changed is whether the file could prove it \u2014 whether \u2018reliable,\u2019 said kindly at a desk in August, would still exist in October, in the only form October reads. It did, because you wrote it down, three different ways, all summer.",
]),
N("end_makeups", 66, "Ending \u2014 Make-Ups, Eventually", [], ending=True, debrief=[
 "WHAT THE FILE HELD (the hidden record, revealed): A partial correction. The review credited what was in front of it \u2014 your dated cancellation answers, or your account, believed \u2014 enough to order the lost visits made up, this time with dates attached to the order. What it did not do is reopen the arithmetic: the \u201860%\u2019 line stands in the findings, uncorrected, because the full correction needed the whole apparatus \u2014 written confirmations for every visit, the center's own summary and log obtained on request, and a corrected table attached to the packet \u2014 and some layer of that apparatus was missing. So the file now holds both: real make-up visits, ordered and dated, and a percentage that still describes a mother who missed visits she was never allowed to attend. Future summaries will quote the number, not the bus ride.",
 "THE LAW UNDER THIS PATH (kept to this scenario's verified set): The make-ups were won with the tools this path used \u2014 a written trail, presented by counsel (42 Pa.C.S. \u00a7 6337). The correction that didn't happen was available through the unused or unfinished ones: the record behind the percentage \u2018shall be released upon request\u2019 (55 Pa. Code \u00a7 3130.44(d)), and a percentage, being a document, can only be corrected by another document \u2014 the four-column table, built from the provider's own log, attached before the hearing. Note the asymmetry this ending teaches, because it generalizes: remedies a room can grant out of fairness (dates for make-ups) move on stories and partial paper; findings, once written, move only on complete paper. You got the remedy. The finding kept the number.",
 "THE HONEST PART: Do not let the standing percentage obscure the real hours: three visits, restored with dates, are three afternoons with Felix that September had simply deleted, and plenty of parents leave this room with neither the dates nor the correction. A different reviewer might have corrected the number on the partial trail, or refused the make-ups on the full one \u2014 reviewers differ, centers differ, and the same summer, faithfully kept, lands differently in different rooms. Your attendance was never the variable in this scenario; on every path you attended every held visit. The variable was the denominator's ownership. Next review, the table can still be built \u2014 the log still exists, and a request can still be sent. Paper keeps. That is its whole virtue.",
]),
N("end_poor", 66, "Ending \u2014 Attendance: Poor", [], ending=True, debrief=[
 "WHAT THE FILE HELD (the hidden record, revealed): One number, hardened. \u2018Family attended 60% of scheduled visits\u2019 was read at the review, met by no table, no log, and no dated trail, and was adopted into the plan's findings in the natural way of unopposed sentences: by quotation. The findings do not say the center cancelled three visits for staffing. They do not say make-up slots were logged that you were never told about. They say a percentage, and the percentage now has an owner, grammatically and permanently: the family. Which is to say, you. The next summary will quote the findings, the way this one quoted the summary, the way the summary quoted a count nobody ever showed you.",
 "THE LAW UNDER THIS PATH (kept to this scenario's verified set): Nothing in this ending was decided against you after a contest of records, because there was only one record in the room. The instruments all existed: confirmations and cancellation answers could have been made in writing, at no cost, the day each event happened; the attendance summary and scheduling log behind the percentage were yours on written request \u2014 they \u2018shall be released upon request\u2019 (55 Pa. Code \u00a7 3130.44(d)); and counsel (42 Pa.C.S. \u00a7 6337) was there to build the four-column table and attach it. All of that remains available for the next review \u2014 the log still exists, the request can still be sent, and a finding, however hardened, can still be answered by the paper it was computed from. It will simply have to be answered uphill, against a finding instead of a draft.",
 "THE HONEST PART: Let this debrief be as fair as the finding wasn't: you attended every visit that was ever held \u2014 nine of nine, all summer, including the Saturday you rode a bus halfway across town to a cancellation. The center cancelled; the summary folded; the finding hardened. At no point did anyone in the chain need to intend any of it, which is precisely the system's most dangerous property: it can misdescribe a reliable parent as a poor attendee using nothing but phone calls, a busy desk, and arithmetic nobody checked. A fuller-staffed center, a supervisor who logged cancellations in the provider's own column, a reviewer who asked for the denominator \u2014 any of those lucks changes this ending without you changing at all. Outcomes here turn on staffing, habits, and luck. Your share, next time, is the unglamorous trio: confirm in writing, answer in writing, and bring the count \u2014 because in this system, attendance you cannot prove is attendance that, on paper, did not happen.",
]),
]

s63 = build(
 {"title": "The First 90 Days",
  "subtitle": "Scenario 63 \u2014 Cancelled, Again (a fictional composite)",
  "startDateISO": "2026-08-03", "startNode": "start", "startCash": 150,
  "tier": "Hard",
  "summary": "The center cancels three visits; the report calls it her attendance \u2014 building the arithmetic that corrects the record."},
 s63_nodes, S63_START)
assert len(s63_nodes) == 29, len(s63_nodes)
assert sum(1 for n in s63_nodes if n.get("ending")) == 3

if __name__ == "__main__":
    emit(s62, 62, "The Visit Notes",
         "This scenario depicts supervised visits and the notes taken at them, including a minor fall from low on a visit-room climbing frame (a scraped arm), handled procedurally and without injury detail. There is no graphic content. Players may skip any scene or use the quick exit at any time.",
         S62_START)
    emit(s63, 63, "Cancelled, Again",
         "This scenario depicts repeated cancellation of a parent's visits by a visitation center for staffing reasons, and a review report that miscounts her attendance. There is no graphic content. Players may skip any scene or use the quick exit at any time.",
         S63_START)
    print("generated scenario-62.json/.md and scenario-63.json/.md")
