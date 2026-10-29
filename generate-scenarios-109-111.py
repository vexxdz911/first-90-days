#!/usr/bin/env python3
"""Generator for Scenarios 109-111 of 'The First 90 Days' (Hard tier, Wave 2 Batch 8 Part B).
One data source emits BOTH scenario-N.json and scenario-N-script.md for each
scenario, so they match node-for-node by construction. Every kicker and every
in-body date is computed from startDateISO + dayOffset via datestr(); no date
is hand-typed in the scenario data. The script also walks each winning route
programmatically and prints the walked path, node count, and end cash."""
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
    L.append(f"Start date: {datestr(start, 0)}. Day offsets are days since the scenario's start date. Tier: Hard.")
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
    by = {n["id"]: n for n in scen["nodes"]}
    flags, cash = set(), scen["meta"]["startCash"]
    path, cur = [], scen["meta"]["startNode"]
    while True:
        path.append(cur)
        node = by[cur]
        if node.get("ending"):
            assert cur == win_ending, (cur, win_ending)
            assert "recordsRequested" in flags, ("win route missing recordsRequested", sorted(flags))
            return path, cash, flags
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
# SCENARIO 109 — The Check That Kept Coming
# Start: Monday, October 5, 2026. Emeka placed six weeks before day 0
# (placement predates the story; no 'removed' flag). No benefit-program
# rule is stated as law anywhere: the repayment letter states its own
# instructions on its face, and the story turns on dates and paper.
# =====================================================================
S109_START = date(2026, 10, 5)
assert S109_START.strftime("%A") == "Monday"
d109 = lambda off: datestr(S109_START, off)
# Placement was 42 days (six weeks) before day 0; the payee change was
# processed 42 days after placement — i.e. on day 0's week. Both facts
# are computed here, never hand-typed.
PLACEMENT_OFF = -42
PAYEE_OFF = 0

s109_nodes = [
N("start", 0, "The Letter About the Money", [
 "Your name is Keisha. Your son Emeka is nine. He has a disability, a school he loves in the stubborn way he loves anything that is his, and a foster placement that began six weeks ago \u2014 before this story opens, in a part of the case this story does not reopen.",
 f"For six weeks after the placement \u2014 from {d109(PLACEMENT_OFF)} onward \u2014 a payment connected to Emeka kept arriving to you, as his payee, the way it always had. You spent it the way you always had: on rent, in the open, with receipts. Nobody, in those six weeks, told you anything had changed.",
 f"Today, {d109(0)}, the mail holds a different kind of paper: a repayment letter. It says the payments that arrived after the placement are an overpayment. It lists an amount. It asks for the money back. And folded behind it, in the same envelope, is a form \u2014 the letter's own form, for answering it.",
], [C("Read the letter a second time, slowly, including the form behind it", "letter_close",
      note="The second reading is where letters like this keep their actual instructions.")]),

N("letter_close", 2, "What the Letter Itself Says", [
 f"The letter is dated {d109(0)}, and everything this story needs from it is printed on its own face. It says the payments after the placement date it lists \u2014 {d109(PLACEMENT_OFF)} \u2014 are claimed as an overpayment. It encloses a response form, and it says, in its own words, to return that form by {d109(30)} if you dispute the claim or want to ask that repayment be waived or reduced, and to say why, with any papers that show why.",
 "It does not say what anyone outside this envelope thinks the rules are. It does not need to. Inside this story, the letter is the process: a stated amount, a stated window, a stated form, and a place on that form for your reasons and your documents.",
 "Your caseworker, when you called yesterday, used a shorter version. You wrote her words down, the way this case has taught you to: 'mother retained child's benefits.' Five words. They are not in this letter. They are somewhere else \u2014 in a case note \u2014 and a note, unlike a letter, travels without its envelope.",
], [C("Lay the letter beside your rent receipts and look at the six weeks whole", "rent_open",
      addHidden=["Repayment letter \u2014 received; its own form and its own stated response window noted"],
      note="The letter's window runs to a date the letter itself names. Windows, in this system, are the whole game.")]),

N("rent_open", 4, "Spent the Way It Always Was", [
 "The six weeks, laid out on the kitchen table, look like what they were: rent. The payment arrived; the rent came due; the rent was paid \u2014 to the same landlord, in the same amount, by the same method as the months before the placement, when nobody questioned any of it.",
 "Your landlord's receipts are in a shoebox with everything else. They are not arguments. They are dates and amounts and a signature, which is to say they are the strongest kind of paper this system makes: paper that was created at the time, for another purpose, by somebody else.",
 "What they do not show is the one fact that would explain everything: when the change was actually processed on the other side of the desk. That date is not in your shoebox. It is in a file you have not seen.",
], [C("Decide what paper of your own you can put in order this week", "bank_choice",
      note="Your paper first. Their paper is a request away \u2014 but requests take weeks, and the letter's window does not.")]),

N("bank_choice", 6, "The Bank's Version", [
 "Your bank keeps its own chronology, and it is better than memory: statements showing each payment arriving, and the rent going out after it, month shape by month shape. Copies cost a small fee and a trip. Memory costs nothing tonight and will be worth, in a later room, approximately what it cost.",
 "There is also the question of the other chronology \u2014 the agency's. But a bank statement is the rare document nobody can call your version of events. It is the bank's.",
], [C("Order the bank statements for the six weeks and keep the bank's receipt", "bank_ordered", cash=-6,
      setFlags=["bankRecords"],
      addHidden=["Bank statements \u2014 payments in and rent out, ordered for the full six weeks"],
      note="Six dollars of fees. The statements will show arrivals and rent in the bank's own type, which argues with nobody and convinces everybody."),
    C("Work from memory \u2014 you know exactly what you spent it on", "bank_memory",
      note="You do. Knowing is the half of proof that cannot be attached to a form.")]),

N("bank_ordered", 8, "In and Out, in Type", [
 f"The statements arrive by {d109(8)}, and they are almost boring, which is their power: each payment in, the rent out days later, six weeks of an ordinary household doing an ordinary thing with money that kept arriving the ordinary way.",
 "Nothing in them says why the payments kept coming. Statements never say why. Why lives in the other file \u2014 the one with the placement date and the processing date sitting in it, forty-two days apart, waiting for somebody to ask for it.",
], [C("File the statements with the rent receipts, in date order", "receipts_beat",
      note="In date order. Chronology is not a style choice in this case; it is the argument.")]),

N("bank_memory", 8, "Clear, and Unattachable", [
 "Your account of the six weeks is exact: which payment, which rent, which receipt is in the shoebox. Told at the kitchen table, it convinces anyone who hears it. The repayment form, however, will not be heard at a kitchen table. It will be read, by a reader who was not there, next to whatever is attached to it.",
 "What is attached is the whole question. Memory attaches to nothing.",
], [C("Go on to the landlord's receipts \u2014 those, at least, are paper", "receipts_beat",
      note="Receipts are paper. The story is about to ask how much paper is enough, and whose.")]),

N("receipts_beat", 10, "The Landlord's Signature", [
 "The landlord, asked for copies, produces them without surprise \u2014 landlords keep rent paper the way this system wishes everyone kept everything. Six weeks of receipts, signed, dated, matching the bank's ins and outs to the dollar the letter lists.",
 "You now hold two-thirds of a timeline: the placement date (the letter states it), and your six weeks (the bank and the landlord state them). The missing third is the middle: what happened, on the agency's side, between the placement and this letter. Held by itself, your paper says you received money and spent it on rent. Held beside the missing third, it might say something else entirely.",
], [C("Ask your lawyer where the middle of this timeline lives", "counsel_visit",
      note="You have a lawyer in Emeka's case. Timelines are, it turns out, a legal instrument.")]),

N("counsel_visit", 11, "Two Dates in One File", [
 "You have had a lawyer throughout Emeka's case, as the law provides (42 Pa.C.S. \u00a7 6337). Ms. Harrington spreads your paper on her desk \u2014 letter, receipts, statements \u2014 and asks the question this scenario has been walking toward: 'When did the agency process the payee change?'",
 "'They knew about the placement on the day it happened \u2014 placements are their paperwork before they are anyone else's. If the change sat unprocessed for weeks while the payments kept arriving on their old instructions, then the six weeks are not a story about you retaining anything. They are a story about a lag. And a lag, unlike an intention, can be proved from dates \u2014 if the dates are in the room.'",
 "The dates are in the agency's file. Files, she reminds you, can be asked for.",
], [C("Ask how the file itself is requested, in writing", "records_fork",
      note="'The same way everything durable in this case is done,' she says. 'In writing, dated, with a copy kept.'")]),

N("records_fork", 13, "Ask for the Chronology", [
 "A party may request the case record, and the material in it 'shall be released upon request' (55 Pa. Code \u00a7 3130.44(d)). What you want is specific, and Ms. Harrington writes it specifically: the placement chronology, any entry showing when the payee change was submitted and when it was processed, and the case note that uses the phrase about retained benefits.",
 "The alternative is to answer the repayment letter from your side of the desk only \u2014 your receipts, your memory, your rent \u2014 and let the middle of the timeline stay wherever it currently lives.",
], [C("Sign the written request for the record \u2014 chronology, processing entries, and the note", "record_arrives", cash=-3,
      setFlags=["recordsRequested"],
      addHidden=["Case record \u2014 requested in writing, including placement chronology and payee-processing entries"],
      note="Signed, dated, copied. The request itself now has a date, and dates are what this whole case is made of."),
    C("Answer from your own paper alone \u2014 the receipts speak for themselves", "no_record",
      note="Receipts speak about rent. About the lag, they are silent, because the lag never happened in your kitchen.")]),

N("record_arrives", 18, "Forty-Two Days, in Their Own Hand", [
 f"The packet arrives on {d109(18)}, and the chronology is in it, in the agency's own entries. Placement: {d109(PLACEMENT_OFF)} \u2014 known to the agency that day, because the placement was the agency's own act. And then, six weeks later, the processing entry: the payee change, submitted and processed in the week of {d109(PAYEE_OFF)} \u2014 the same week the repayment letter was being prepared.",
 "Forty-two days. The payments kept arriving because the instruction that would have stopped them sat unprocessed for forty-two days, on the side of the desk that knew first. Your bank statements cover exactly those forty-two days. So do your rent receipts. Three chronologies, three different hands, one shape.",
 "The case note is in the packet too. Its phrase sits there in note type, with no chronology attached to it. Notes, like letters, can be answered \u2014 but only in writing, and only by someone holding the dates.",
], [C("Lay the packet's chronology beside your statements and receipts", "note_phrase",
      addHidden=["Agency chronology \u2014 placement known day one; payee change processed six weeks later"],
      note="The lag is no longer your theory. It is their entry, with their date on it.")]),

N("no_record", 18, "The Middle, Missing", [
 "Without the packet, the middle of the timeline stays a suspicion: you believe the change was processed late, because the payments kept coming \u2014 but payments arriving is also what the note's phrase says, in its five words, and a suspicion cannot be attached to a form.",
 "Ms. Harrington is plain about it: 'We can still answer the letter. We will be answering an amount and a date with receipts and good faith. The thing that would make it the agency's lag instead of your retention is a date we do not hold.'",
], [C("Go on toward the answer with the paper you have", "note_phrase",
      note="Good faith is real. It is also, unattached, the currency later rooms accept least.")]),

N("note_phrase", 20, "Five Words in a File", [
 "However you arrived here, the note's five words are the other half of this case: 'mother retained child's benefits.' They will be read \u2014 at the next review of Emeka's case, by people who were not in any of these rooms \u2014 by readers who will meet the phrase before they meet you, and who may never meet the chronology at all.",
 "A phrase like that is not corrected by being untrue. It is corrected by being answered, in the file, with dates \u2014 or it is carried forward, report to report, the way unchallenged sentences are.",
 "Emeka, meanwhile, is nine, and has opinions about visit snacks, and none about chronology. The visits continue while the paper argues. Both of those facts deserve their own paragraph, and only one of them will get one in the file.",
], [C("Go to the next visit, and then build the answer", "emeka_visit",
      note="The visit is the case's real life. The answer is how the case will remember it.")]),

N("emeka_visit", 22, "The Visit, Meanwhile", [
 f"The visit on {d109(22)} is ordinary and good: Emeka has a school story that takes the whole hour to tell properly, and a drawing that is mostly, he explains, a map. You keep the visit note copy the office gives you, because keeping paper has become the habit this case teaches everyone it touches.",
 "At home, the kitchen table holds two cases at once: a boy's map, and a timeline with a forty-two-day hole in its middle that is either filled by the agency's own chronology or by five words in a note. Which of those the next reader meets first is, unusually, up to you \u2014 for about a week more.",
], [C("Build the answer while the letter's window is still open", "timeline_choice",
      note="The window the letter stated runs to the date the letter stated. It has not closed yet. That is the only reason this week matters more than next week.")]),

N("timeline_choice", 24, "One Page of Dates", [
 "The answer, assembled, fits on one page, and Ms. Harrington insists it contain nothing that is not a date with a document behind it: placement, known to the agency that day; payments arriving on the old instruction; rent paid, receipted; payee change processed, six weeks later, in the agency's own entry; repayment letter, after that. No adjectives. No theory of anyone's motives. A lag, shown, is worth more than a lag argued.",
 "Or the six weeks can be carried as a story \u2014 true, detailed, and held entirely in your voice.",
], [C("Build the one-page timeline from the chronology, the statements, and the receipts", "timeline_built",
      setFlags=["timelineBuilt"],
      addHidden=["Timeline \u2014 one page of dates: placement, payments, rent, processing entry, letter"],
      note="Six lines, six documents. The page does not accuse anyone. It simply refuses to let forty-two days belong to the wrong person."),
    C("Carry the story in your own words \u2014 you lived the six weeks in order", "story_only",
      note="You did. Stories, however, cannot be attached to a form. Timelines can.")]),

N("timeline_built", 26, "Six Lines, No Adjectives", [
 f"The page reads: placement {d109(PLACEMENT_OFF)}. Payments arriving on the existing instruction through the six weeks. Rent paid and receipted in each of those weeks. Payee change processed in the agency's chronology in the week of {d109(PAYEE_OFF)}. Repayment letter dated {d109(0)}.",
 "Read in order, the page does something no paragraph of explanation could do: it makes the reader do the subtraction. Forty-two days, computed by whoever holds the page, in their own head, from the agency's own dates. Arithmetic a reader does herself is arithmetic she believes.",
], [C("Take the page to the choice the letter has been waiting for", "response_choice",
      note="Copies made: one for the form, one for Ms. Harrington, one for the shoebox that is slowly becoming a file.")]),

N("story_only", 26, "True, in One Voice", [
 "Your account is clear and complete: the payments came, the rent was due, you paid it, nobody told you anything had changed. Anyone who hears you believes you. The difficulty is structural: the form will be read by someone who will never hear you, beside a note written by someone who did not need to convince anyone \u2014 only to type five words.",
 "What can still be sent is a written answer in your own words. What cannot be sent, because it was never assembled, is the page of dates that would have answered the note instead of describing the hardship.",
], [C("Take what you have to the choice the letter has been waiting for", "response_choice",
      note="The window is still open. It will not stay open while anyone deliberates about what openness means.")]),

N("response_choice", 27, "The Form, Inside Its Own Window", [
 f"The letter stated its window on its face: return the enclosed form by {d109(30)}. Today is {d109(27)}. Three ways of using the remaining days are on the kitchen table, and they are genuinely different acts, not different tones of the same act.",
 "File the form, with the timeline and its documents attached, disputing the claim on the documented lag and asking \u2014 on the form's own line for it \u2014 that repayment be waived or reduced, and that the case note be corrected to match the chronology. Pay the amount the letter lists, silently, and let the note stand as the file's account of the six weeks. Or let the window close with no answer at all, and meet the letter again later, in whatever shape unanswered letters take.",
], [C("File the form inside the window \u2014 timeline, chronology, statements and receipts attached", "response_filed", cash=-3,
      setFlags=["responseFiled"],
      addHidden=["Response form \u2014 filed inside the letter's stated window, with the documented lag attached"],
      note="Stamped at the counter, copied, dated days before the window closes. The answer now exists in the only tense this system trusts: already filed."),
    C("Pay the amount the letter lists, and say nothing further", "response_paid",
      addHidden=["Repayment \u2014 paid without a written answer; case note left as written"],
      note="The debt, as the letter states it, is settled. The five words in the file are not. Payment answers a letter; it does not answer a note."),
    C("Let the window close \u2014 the letter can wait until the case is calmer", "response_ignored",
      addHidden=["Repayment letter \u2014 no response filed inside its stated window"],
      note="Letters like this do not wait the way people wait. They ripen.")]),

N("response_filed", 28, "Filed, With Days to Spare", [
 f"Filed on {d109(28)} \u2014 inside the window, with the page of dates on top. Ms. Harrington's covering sentence is the shortest in the file: 'The enclosed chronology is the agency's own.' Under it, the dispute, the waiver request on the form's own line, and a separate, plain request: that the case note be corrected to state the processing chronology the packet shows.",
 "Nothing is decided today. What is decided is what the decision will be made from: a documented lag, filed on time, versus five words.",
], [C("Go on with Emeka's case while the answer is read somewhere", "wait_weeks",
      note="Cases continue during paperwork the way weather continues during forecasts: entirely, and on their own schedule.")]),

N("response_paid", 28, "Paid, and Quiet", [
 "The payment is made, and the letter's account is closed in the way paying closes accounts. What does not close is the note. It sits in Emeka's file, unanswered, its five words now accompanied by a payment that a later reader may take \u2014 unfairly, and entirely predictably \u2014 as agreement with them.",
 "You bought peace from a letter. The file kept its sentence. Both transactions are complete, and only one of them was the one you meant to make.",
], [C("Go on with Emeka's case", "wait_weeks",
      note="The case continues. So does the sentence, in every summary drawn from that file from now on.")]),

N("response_ignored", 28, "The Window, Closing", [
 f"The days to {d109(30)} pass the way days pass when a letter is on a refrigerator: visibly. Then the window the letter stated is closed, and the letter changes tense \u2014 from a claim with a form attached to a balance with a history, the history being that it was not answered.",
 "Nothing dramatic happens on the day itself. That is how hardening works in this system: not as an event, but as a status, entered somewhere, in the same type as everything else.",
], [C("Go on with Emeka's case", "wait_weeks",
      note="The case continues. The letter, unanswered, continues with it \u2014 in its new tense.")]),

N("wait_weeks", 32, "Weeks of Ordinary Case", [
 "The following weeks are Emeka's case being itself: visits, school notes, a plan meeting at which the money is mentioned once, in passing, in the note's five words \u2014 because notes are what meetings read \u2014 and then not mentioned again, because meetings move on.",
 "A scored assessment form is part of cases like Emeka's, filled in from notes and visits. What it can see of these months depends, with an exactness nobody states out loud, on which sentences are in the file when it is filled in.",
], [C("Wait for the next envelope, and keep every paper that arrives", "agency_reply",
      note="You keep them all now, in date order, without being asked. The shoebox has tabs.")]),

N("agency_reply", 38, "The Next Envelope", [
 f"On {d109(38)} the next envelope arrives, and its contents depend \u2014 as this scenario has been honest about from its first letter \u2014 on what was sent into the last one. An answer filed inside a stated window gets an answer: a determination, made on the papers filed. A payment gets a receipt and silence. An unanswered letter gets a firmer letter, restating the amount, noting the closed window, and carrying the matter forward in its harder tense.",
 "Beside it, in Emeka's case, a review is approaching \u2014 the room where the note's five words, or their correction, will be read aloud as part of his mother's record.",
], [C("Take the envelope to Ms. Harrington and prepare for the review", "prep",
      note="Preparation, again, is inventory: what exists, in writing, dated, filed \u2014 and what exists only as a hope about a reader.")]),

N("prep", 44, "Ms. Harrington Builds the Packet", [
 "Ms. Harrington spreads the matter in two piles, the way lawyers in this series always eventually do. Pile one: a letter, a note of five words, and whatever status the repayment now holds. Pile two \u2014 if your choices built it \u2014 a bank's chronology, a landlord's receipts, an agency's own processing entry, a one-page timeline, and a form filed inside its window.",
 "'At the review,' she says, 'we will not be arguing about whether you are a careful mother. We will be asking the record to say what its own dates say. Rooms can do that, when the dates are in them. Rooms cannot do it from my say-so, or yours.'",
], [C("Assemble the packet in date order, with copies", "review", cash=-4,
      addHidden=["Review packet \u2014 letter, chronology, statements, receipts and filed response, in date order"],
      note="Date order, again. In this scenario date order is not filing technique. It is the entire claim.")]),

N("review", 50, "The Review", [
 f"The review convenes on {d109(50)}. The money matter is one line of it \u2014 Emeka's plan is the rest \u2014 but the line is read the way file lines are read: from the note, in its five words, unless something filed displaces it. The repayment's status is stated. Then Ms. Harrington rises, with whatever your choices actually put in her hands.",
 "Choose the presentation the paper you built can carry.",
], [C("Present the documented lag \u2014 the agency chronology, the timeline, and the response filed inside the letter's window", "end_win", cash=-6,
      requiresFlags=["bankRecords", "recordsRequested", "timelineBuilt", "responseFiled"],
      note="This presentation exists because four pieces of paper exist, in order, filed before this room convened."),
    C("Let the payment stand as the answer \u2014 the amount is settled, whatever the note says", "end_paid",
      note="Settled is a word about money. The review is about to use it, or refuse to, about a record."),
    C("Let the file speak as it stands \u2014 the unanswered letter and the five words", "end_hardened",
      note="Files speak fluently in exactly this situation. It is the situation they are built for.")]),

N("end_win", 57, "Ending \u2014 The Lag, On the Record", [], ending=True, debrief=[
 f"WHAT THE FILE HELD (the record, revealed): A complete chronology, authored in three hands. The agency knew of the placement on {d109(PLACEMENT_OFF)}, its own act. The payee change was processed six weeks later, in the agency's own entry, in the week of {d109(PAYEE_OFF)}. In between, payments arrived on the old instruction and rent was paid against them, receipted by a landlord and recorded by a bank. The response form was filed on {d109(28)}, inside the window the letter itself stated, with that chronology attached, disputing the claim on the documented lag and asking on the form's own line that repayment be waived or reduced. On that record, the repayment was addressed through the letter's own process as a documented administrative lag \u2014 and at the review, the case note was corrected on the record to state the chronology: payments continued during a processing lag, spent on rent, answered in writing inside the stated window. The five words no longer stand alone in Emeka's file.",
 "THE PROCESS UNDER THIS PATH (described, keeping to this scenario's verified law): One verified instrument did the surfacing: the case record, released on request (55 Pa. Code \u00a7 3130.44(d)) \u2014 requesting it is what put the agency's processing date beside the placement date, where any reader must subtract them. Counsel (42 Pa.C.S. \u00a7 6337) assembled the dates and filed the answer. Everything about the repayment itself \u2014 the amount, the window, the waiver request \u2014 came from the letter's own face and its enclosed form, used exactly as the letter instructed. No program rule is stated in this ending, because none was needed and none is in the verified set: the win is documentary, not doctrinal. Label it honestly: this is a partial win. Emeka remains placed, his case continues, and the determination on any remaining balance follows the letter's own process on this record \u2014 what changed is that the record now tells the truth about whose forty-two days they were.",
 "THE HONEST PART: A different reader of the same packet could have weighed the lag less generously; a different reviewer could have corrected the note's wording and still pressed the schedule of Emeka's plan exactly as hard. The landlord could have kept poor receipts; the bank could have charged more than a week's patience for statements; luck and other people's filing habits held real pieces of this. What your choices controlled was narrower: when the system took six weeks to process its own change, the proof of those six weeks existed \u2014 dated, attached, filed inside the window the letter itself set. Outcomes in this system are not verdicts on a parent's worth. This one is a verdict on a chronology, and for once the chronology was complete.",
]),
N("end_paid", 57, "Ending \u2014 Paid, and Still Written That Way", [], ending=True, debrief=[
 "WHAT THE FILE HELD (the record, revealed): A closed money account and an open sentence. The amount the letter listed was paid, without a written answer, without the chronology, without the timeline \u2014 so the file holds a payment where an explanation should be, and the case note's five words, 'mother retained child's benefits,' stand uncorrected, to be quoted into the next summary and the one after that. At the review, the payment was noted as resolving the letter. The note was not mentioned as needing resolution at all, because nothing filed had ever asked it to be.",
 "THE PROCESS UNDER THIS PATH (described, keeping to this scenario's verified law): Paying a letter settles what the letter claims. It does not correct what a file says \u2014 only paper filed into the file does that. The instruments that would have done it were the verified ones, available throughout: the case record on written request (55 Pa. Code \u00a7 3130.44(d)), which held the processing date that turns retention into lag, and counsel (42 Pa.C.S. \u00a7 6337) to attach that chronology to the letter's own form inside its own stated window. The repayment process itself, on this path, worked exactly as the letter described \u2014 which is the point: the letter was never the whole case. The note was, and the note was never answered.",
 "THE HONEST PART: Be fair to the version of you that lands here: you paid rent with money that arrived the way it always had, in the open, and then you paid the money back when a letter said to \u2014 two ordinary, peace-buying acts that many careful parents would have made in the same order. Nothing in this ending says you kept anything you meant to keep. It says the file was allowed to say you did, in five words, with a payment filed beneath them like a signature. A corrected note can still be sought \u2014 records can still be requested, chronologies still attached \u2014 and it will matter at the next review. It simply cannot retroactively give this review a different sentence to read.",
]),
N("end_hardened", 57, "Ending \u2014 The Letter, Ripened", [], ending=True, debrief=[
 f"WHAT THE FILE HELD (the record, revealed): An unanswered letter, in its harder tense. The window the letter stated closed on {d109(30)} with no form filed; the amount was restated, the file acquired the closed window as a fact about the mother's responsiveness, and the case note's five words \u2014 'mother retained child's benefits' \u2014 now sit beside a second sentence the file wrote by itself: claimed, notified, not answered. At the review, the money line was read as two facts \u2014 a retention and a silence \u2014 neither of which the underlying chronology, never requested and never attached, was present to dispute.",
 "THE PROCESS UNDER THIS PATH (described, keeping to this scenario's verified law): Nothing here required a new right to prevent. The letter carried its own process on its face \u2014 a form, a window, a line for reasons and documents \u2014 and using a process a letter offers costs a stamp, not a doctrine. The chronology that would have reframed the claim was in the case record, releasable on request (55 Pa. Code \u00a7 3130.44(d)); counsel (42 Pa.C.S. \u00a7 6337) stood ready to assemble it. What hardened was not the debt \u2014 debts can still be disputed, arranged, addressed \u2014 but the file's account of the mother, which is the asset every future room will spend. In this system, an unanswered letter does not stay a letter. It becomes a finding with an envelope.",
 "THE HONEST PART: The six weeks themselves were innocent in exactly the way the win ending's chronology shows: a placement the agency made, a change the agency processed late, rent paid openly against money that kept arriving. An unanswered letter does not change any of that \u2014 it only changes who gets to describe it, and in what rooms, and with what documents in hand. Other parents, in other files, have had a worker write the lag into the note unprompted; some notes are written by people who check chronologies first. Yours was not, and luck of that kind is not a system. The lag can still be documented now \u2014 the chronology still exists, the request can still be made \u2014 and a later review can still be given a truer sentence. It will be given it as a correction, argued at speaking speed, instead of as the record it could simply have been.",
]),
]

s109_meta = {"title": "The First 90 Days",
 "subtitle": "Scenario 109 \u2014 The Check That Kept Coming (a fictional composite)",
 "startDateISO": "2026-10-05", "startNode": "start", "startCash": 160,
 "tier": "Hard",
 "summary": "Six weeks after Emeka's placement, his benefit payment kept arriving to his mother as payee \u2014 then a repayment letter and a five-word case note reframed an administrative lag as retention."}

WIN109 = {
 "start": "Read the letter a second time, slowly, including the form behind it",
 "letter_close": "Lay the letter beside your rent receipts and look at the six weeks whole",
 "rent_open": "Decide what paper of your own you can put in order this week",
 "bank_choice": "Order the bank statements for the six weeks and keep the bank's receipt",
 "bank_ordered": "File the statements with the rent receipts, in date order",
 "receipts_beat": "Ask your lawyer where the middle of this timeline lives",
 "counsel_visit": "Ask how the file itself is requested, in writing",
 "records_fork": "Sign the written request for the record \u2014 chronology, processing entries, and the note",
 "record_arrives": "Lay the packet's chronology beside your statements and receipts",
 "note_phrase": "Go to the next visit, and then build the answer",
 "emeka_visit": "Build the answer while the letter's window is still open",
 "timeline_choice": "Build the one-page timeline from the chronology, the statements, and the receipts",
 "timeline_built": "Take the page to the choice the letter has been waiting for",
 "response_choice": "File the form inside the window \u2014 timeline, chronology, statements and receipts attached",
 "response_filed": "Go on with Emeka's case while the answer is read somewhere",
 "wait_weeks": "Wait for the next envelope, and keep every paper that arrives",
 "agency_reply": "Take the envelope to Ms. Harrington and prepare for the review",
 "prep": "Assemble the packet in date order, with copies",
 "review": "Present the documented lag \u2014 the agency chronology, the timeline, and the response filed inside the letter's window",
}

# =====================================================================
# SCENARIO 110 — Unstable, On Paper
# Start: Monday, October 19, 2026. Naledi placed before the story
# (month nine of her case); no 'removed' flag. Housing facts are the
# parent's paper; the review framework cited is only the verified
# 42 Pa.C.S. § 6351(f) determinations and, record-dependently,
# 42 U.S.C. § 675(5)(E).
# =====================================================================
S110_START = date(2026, 10, 19)
assert S110_START.strftime("%A") == "Monday"
d110 = lambda off: datestr(S110_START, off)

s110_nodes = [
N("start", 0, "The Non-Renewal", [
 "Your name is Charise. Your daughter Naledi is five, and she has been in foster care for nine months \u2014 long enough that her plan has seasons in it, and that the word 'housing' on that plan has been, until now, the quiet line: a small apartment, a lease in your name, rent paid.",
 f"The envelope on {d110(0)} ends the quiet. Your landlord will not renew the lease. The letter is short, businesslike, and final: the tenancy ends on the date it names, {d110(30)}, and the apartment is to be vacated by then. It gives no reason it is required to defend, and this story will not invent one for it.",
 "What everyone in your case will later call 'the housing situation' begins here \u2014 not with Naledi, not with the plan, but with a landlord's letter and thirty days.",
], [C("Read the letter twice, and keep it \u2014 it is now a case document", "letter_close",
      note="Kept, dated, uncreased. The first document of the housing chapter is the one that ends the old housing.")]),

N("letter_close", 2, "The Night Behind the Letter", [
 "You know, and the landlord may know, what sits behind the non-renewal in the building's memory: the night, nine months ago, when Naledi was removed \u2014 the police presence in the hallway, the neighbors' doors opening and closing. It is the texture of why this apartment stopped feeling available to you, and probably to him.",
 "It is also, your lawyer will later say, a thing this story does not litigate: nobody will prove a landlord's motive in Naledi's review, and nobody needs to. What the review will weigh is not why the lease ended. It is what your housing is, on paper, when the room convenes \u2014 and what paper says so.",
 "Thirty days. The plan's housing line currently says your address. By the review, it will say something else. The only question this scenario asks is whether that something is written by your documents or by a summary's default word.",
], [C("Start the search the way searches actually start \u2014 with who you know", "search_days",
      note="The lists are long and the month is short. Both of those are facts. Neither is the ending.")]),

N("search_days", 4, "Four Days of Doors", [
 f"Four days of the search, {d110(0)} to {d110(4)}: two buildings with waiting lists measured in seasons, one room whose rent would take the whole paycheck the plan also counts, a cousin's couch offered and refused \u2014 not from pride, but because a couch is exactly the word the file is waiting to write about you.",
 "Then your cousin Fern calls back. Fern has a house, a spare room with a door, and a proposal she makes in the plainest language anyone uses in this scenario: 'You take the room. You pay rent, like a tenant. We write it down, like adults. Naledi has a room to come home to when the court says so.'",
 "A doubled-up household, the system calls arrangements like Fern's, when it calls them anything kind at all. What it becomes in the file depends entirely on the paper it generates.",
], [C("Go and look at the room, and at the arrangement, with clear eyes", "fern_door",
      note="A room with a door. In housing paper, doors matter more than intentions.")]),

N("fern_door", 6, "A Room With a Door", [
 "The room is small, clean, and Naledi-sized in the ways that count: space for a small bed, a window, a door that closes. Fern's house has the other things a plan reads for \u2014 a kitchen, a bathroom, a school route no worse than the apartment's. Fern herself is steady, employed, and entirely willing to be looked at by anyone the case sends to look.",
 "What Fern offers can be done two ways, and the two ways are different arrangements in the file's eyes even though they are identical in the house's. It can be written: a room agreement, signed, with rent, a start date, and signatures. Or it can be familial: a handshake, a key, and everyone's good faith.",
 "Good faith fills a house. Signatures fill a file. The review will only ever see one of those rooms.",
], [C("Decide how the arrangement will exist \u2014 on paper, or on trust", "agreement_choice",
      note="Fern will sign anything true. The question is whether anyone asks her to.")]),

N("agreement_choice", 8, "Sign It Like a Lease", [
 "There is a version of this move that costs an evening: a one-page room agreement \u2014 Fern as householder, you as occupant of the named room, rent in a named amount, starting on a named date, utilities and shared spaces described in two honest sentences \u2014 signed by both of you, dated, copied.",
 "There is another version that costs nothing: you move in as family, pay what you can when you can, and trust that anyone who needs to understand the arrangement will come and see it, the way Fern sees it.",
], [C("Write and sign the room agreement with Fern, dated, before you move a single box", "agreement_signed", cash=-4,
      setFlags=["agreementSigned"],
      addHidden=["Housing \u2014 signed, dated room agreement with cousin; rent and start date stated"],
      note="Four dollars of copies. The agreement does not make the room more real. It makes the room legible \u2014 to readers who will never stand in it."),
    C("Move in as family \u2014 a handshake and a key are enough between cousins", "handshake_only",
      note="Between cousins, they are. Between a parent and a summary line, they are not the same instrument at all.")]),

N("agreement_signed", 10, "Tenant, on Paper", [
 f"The agreement is signed on {d110(8)}, effective {d110(10)}: the room, the rent, the date, two signatures. Fern files her copy in a kitchen drawer with the house's other important paper, which is exactly where tenancy paper belongs, and you keep yours with Naledi's plan.",
 "You are now, in documentary fact, a tenant in a named room at a named rent from a named date. A summary writer who wants to call that arrangement something else will have to write around a signed page to do it. Summary writers can write around pages \u2014 but it is slower, and it leaves marks.",
], [C("Move in, and set up the rent the way the agreement says", "move_day",
      note="Moving costs what moving costs. The agreement costs four dollars. Guess which one the file will remember.")]),

N("handshake_only", 10, "Family, in Person", [
 "You move in as family, and in person the arrangement is everything Fern promised: the room is yours, Naledi's small bed fits, the kitchen is shared without friction. Anyone standing in the house would call it stable without hesitating.",
 "Nobody who decides anything in Naledi's case will ever stand in the house. They will stand in rooms with files in them, and in the files, an unwritten arrangement has the documentary weight of a rumor \u2014 true, warmly believed, and exactly as provable as any other rumor.",
], [C("Move in, and set up the rent the way families do", "move_day",
      note="The house is real. The question the next eight weeks ask is whether the file will ever be told, in a form it can keep.")]),

N("move_day", 12, "Rent, With a Receipt", [
 f"The first rent is due under your arrangement in the week of {d110(12)}, and here the scenario offers its smallest, most repeated choice, because this one will recur monthly and each recurrence is a document: pay in a way that generates paper, or pay in a way that generates gratitude.",
 "A receipt book costs little. A dated receipt, signed by Fern, stating rent for the named room for a named month, is a tenancy proving itself one month at a time. Cash handed across a kitchen, between cousins who trust each other, proves itself to exactly the two people who already believe it.",
], [C("Pay by receipt from the first month \u2014 dated, signed, room and month named", "receipts_kept", cash=-5,
      setFlags=["receiptsKept"],
      addHidden=["Housing \u2014 rent paid by dated, signed receipts naming the room and month"],
      note="Five dollars for the receipt book. Each receipt is boring, dated, and cumulative \u2014 the three virtues of housing paper."),
    C("Pay across the kitchen, in cash, the way family does", "receipts_none",
      note="Fern would swear to every payment, and mean it, and be believed personally \u2014 in a room that weighs attachments, not oaths from cousins.")]),

N("receipts_kept", 14, "A Tenancy, Accumulating", [
 "Receipt one joins the agreement in your papers. It is a small page, and together the two pages already answer the only housing question a file is competent to ask: where does she live, since when, at what rent, proved how? Most housing lines in most files are written with less evidence than you now hold, because most housing is never challenged. Yours is about to be \u2014 which is why the evidence matters, and why nobody builds it after the challenge arrives.",
], [C("Turn to the second half of stability \u2014 the applications", "applications_choice",
      note="A doubled-up room answers where you live. The plan will also ask where this goes next. Lists are how that answer gets dated.")]),

N("receipts_none", 14, "Paid, and Unprovable", [
 "The rent is paid. Fern knows it, you know it, the house's whole economy knows it. The file knows nothing, because nothing told it, in any form it keeps. If the arrangement is ever described by someone else, their description will have one advantage yours lacks: it will be written down.",
 "What can still be built is the forward half of the housing story: the applications, with their dates. Paper started later is worth less than paper started first, and infinitely more than paper never started.",
], [C("Turn to the second half of stability \u2014 the applications", "applications_choice",
      note="Applications are the rare housing document whose date is stamped by somebody else's office. That is their entire value.")]),

N("applications_choice", 16, "Two Lists, Two Stamps", [
 f"There are two housing lists you can realistically join this month, and both offices do the same kind thing with paperwork: they stamp the application copy with the date it was received. An application stamped {d110(18)}, say, is a fact with an office behind it: on that date, this mother, from this address, applied, and is pending.",
 "Applying costs fares and a morning each. Not applying costs nothing, and leaves the file's housing story ending at a cousin's spare room \u2014 a story a summary can finish with one word.",
], [C("Apply to both lists and keep the date-stamped copies", "applications_done", cash=-8,
      setFlags=["applicationsDated"],
      addHidden=["Housing \u2014 applications to two housing lists, date-stamped copies kept"],
      note="Eight dollars of fares. Two stamps, two dates, two offices agreeing that your housing has a future tense as well as a present one."),
    C("Settle into Fern's first \u2014 the lists will still be there next month", "waiting_only",
      note="They will be. Their stamps will then say next month, and a review that convenes before next month will read a file with no applications in it.")]),

N("applications_done", 18, "Pending, With Dates", [
 f"Both applications are in by {d110(18)}, stamped, copied, filed behind the agreement and the receipt. Your housing paper now says a complete sentence: lease ended by a landlord's letter on a stated date; room agreement signed, rent receipted; applications pending at two offices since a stamped date. Present housing, proved. Future housing, dated. It is not a house of your own. It is also not, in any honest vocabulary, nothing.",
 "What the plan's housing line says, meanwhile, is about to be shown to you \u2014 and it was not written from this paper.",
], [C("Go to the plan meeting and hear the housing line read aloud", "plan_line",
      note="Bring the folder. Hearing a line and answering a line are different events, and folders decide which one happens.")]),

N("waiting_only", 18, "Settled, Unstamped", [
 "Fern's room is home in every way a home is home at the end of a day. In the file's way, it is an address with no applications behind it \u2014 a present with no dated future, which summary language has a word for, and the word is not 'settled.'",
 "The plan meeting is coming, and with it the first reading of the housing line since the landlord's letter. You will hear, there, what the file currently believes your housing is.",
], [C("Go to the plan meeting and hear the housing line read aloud", "plan_line",
      note="You know where you live. The meeting is where you learn where the file thinks you live.")]),

N("plan_line", 21, "Unstable, On the Line", [
 f"At the plan meeting on {d110(21)}, the updated plan is read, and the housing line reads, in full: 'Mother's housing unstable following loss of lease; currently staying with relative.' Staying. Not renting, not tenanted, not receipted, not applied-anywhere. One adjective \u2014 unstable \u2014 doing the work of your landlord's letter, your cousin's room, and your two stamped applications, and doing it wrong in a specific direction.",
 "Your worker is not hostile about it. The line was drafted from the non-renewal and a note that you had 'gone to family.' Nobody in the drafting chain had your agreement in front of them, because your agreement was in your folder, and folders do not attend drafting chains. Reviews do, though. The review is where this line will be weighed \u2014 as a finding about your housing, not as a summary of your folder.",
], [C("Note the line word for word, and ask your lawyer what the file itself says", "records_fork",
      addHidden=["Plan housing line \u2014 'unstable housing,' drafted without the agreement, receipts or applications"],
      note="Word for word. Corrections are built out of the exact sentences they correct.")]),

N("records_fork", 24, "Ask for the Housing Entries", [
 "You have had a lawyer throughout Naledi's case, as the law provides (42 Pa.C.S. \u00a7 6337). Ms. Solano asks the question this scenario has been walking toward: 'What do the file's housing entries actually say \u2014 not the plan line, the entries under it? Dates, sources, all of it.'",
 "You do not have to guess. A party may request the case record, and the material in it 'shall be released upon request' (55 Pa. Code \u00a7 3130.44(d)). A written request for the housing entries and the draft review summary shows you the exact text \u2014 and the exact dates \u2014 your paper has to answer, weeks before the review reads it.",
], [C("Sign the written request for the record \u2014 housing entries and draft summary", "record_arrives", cash=-3,
      setFlags=["recordsRequested"],
      addHidden=["Case record \u2014 requested in writing, including housing entries and draft review summary"],
      note="Signed, dated, copied. Whatever the entries say about your housing, you are about to be able to quote it instead of dreading it."),
    C("Prepare from the plan line alone \u2014 you heard it read aloud", "no_record",
      note="You heard one line. The entries under it \u2014 their dates, their sources, what they omit \u2014 are the lock your correction has to fit.")]),

N("record_arrives", 29, "What the Entries Omit", [
 f"The packet arrives on {d110(29)}. The housing entries are all true, the way omissions are true: the landlord's letter, noted. The lease's end, noted. 'Mother residing with cousin,' noted \u2014 undated, unsourced, one line. Of the agreement, the receipts, and the applications, the entries say nothing, because nothing had ever been filed where entries are written from. The draft review summary then does what summaries do with an undated line: it keeps the adjective. 'Unstable housing,' carried forward, gathering the authority of print.",
 "Beside it, Ms. Solano lays your folder: agreement, receipts, stamps. 'The file's housing story is a story with its second half missing,' she says. 'We are not going to argue that the first half is false. We are going to file the second half, before the review has to decide housing from half a story.'",
], [C("Decide how the second half is filed \u2014 in writing before the review, or aloud at it", "correction_choice",
      note="A draft is a mercy if you see it in time. This one arrived in time. Time is not the same as using it.")]),

N("no_record", 29, "One Line, Heard Once", [
 "Without the entries, you know the adjective and nothing under it: not which dates the file holds, not whether the draft summary has already hardened the line, not what your correction must quote to displace it. Ms. Solano is honest: 'We can still object at the review. We will be answering sentences we are hearing in full for the first time, in the room that has already read them.'",
 "The correction itself can still be assembled from your folder. What is missing is the target's exact wording \u2014 and corrections, like keys, are cut to locks.",
], [C("Decide how the correction is delivered \u2014 in writing before the review, or aloud at it", "correction_choice",
      note="Your folder is real either way. The question is whether the review meets it as a filing or as a surprise.")]),

N("correction_choice", 33, "Correct It Where It Lives", [
 "Ms. Solano drafts the correction the way durable things are drafted in this series: the landlord's letter first (the loss was a landlord's act, dated); the signed room agreement (a tenancy, dated, at a named rent); the receipts (the tenancy performing, monthly); the stamped applications (a future, dated, pending at two offices). One page of chronology, attachments behind it, asking that the housing entries and the summary line be corrected to describe the arrangement the documents describe \u2014 before the review.",
 "Filing it costs copies and a trip. Raising the same papers at the review costs nothing today, and prices them tomorrow as an argument instead of as the record.",
], [C("File the written correction before the review, with the agreement, receipts and applications attached", "correction_filed", cash=-5,
      setFlags=["correctionFiled"],
      addHidden=["Written correction \u2014 housing chronology filed before the review with agreement, receipts and applications"],
      note="Stamped, copied, in the file before the next summary is drafted from it. The adjective now has competition with dates on."),
    C("Raise it at the review \u2014 the papers are real, and the room will see them", "correction_oral",
      note="The room will. Rooms see late paper the way they hear late objections: politely, and at a discount they never state.")]),

N("correction_filed", 35, "Filed, Not Just Said", [
 "The correction goes in, and the file does with filed paper what it does: the draft summary is amended before the review packet is assembled. The housing paragraph now carries the chronology \u2014 lease ended by landlord's letter; doubled-up tenancy under a signed agreement at Fern's, rent receipted; applications pending, stamped \u2014 and the adjective, deprived of its empty file to live in, is gone from the draft. In its place, the system's own flattest compliment: 'Housing documented as below.'",
 "Documented. Not praised, not excused \u2014 documented, which in a review is the adjective that does the work.",
], [C("Keep the arrangement exactly as documented until the review", "visits_meanwhile",
      note="Receipts monthly, applications pending, the room Naledi-sized. A corrected file still has to be lived up to, monthly, in paper.")]),

N("correction_oral", 35, "Real, and Unfiled", [
 "The papers stay in your folder, real and complete, awaiting their room. Ms. Solano warns you once, without drama: 'At the review, the summary will be read first. It always is. We will be the second account of your housing, and second accounts are cross-examined by the first one's adjective.'",
 "Nothing is lost yet. Everything is priced differently. The review will now decide housing as a contest between a printed line and a folder produced live \u2014 a contest printed lines win more often than folders deserve.",
], [C("Keep the arrangement running until the review", "visits_meanwhile",
      note="The house, at least, does not know it is undocumented. Fern's dinners proceed as if stability were a fact. In the house, it is one.")]),

N("visits_meanwhile", 40, "Visits, From Fern's Door", [
 f"The weeks before the review run from Fern's door: visits with Naledi \u2014 a puzzle rebuilt at a visit-room table, a school song performed twice \u2014 buses caught from the new address, screens and meetings kept from the new address. On {d110(40)} the second rent receipt joins the first, and the arrangement acquires the one property no single document can give it: duration, in paper.",
 "It is worth pausing on the shape of your situation: your housing, as lived, has been stable for weeks. Your housing, as filed, is stable only if the correction was filed \u2014 because in this system stability is not a condition of a household. It is a condition of a record about a household.",
], [C("Prepare for the review with Ms. Solano", "review_prep",
      addHidden=["Compliance \u2014 visits and plan steps kept from the doubled-up address; rent receipts continuing"],
      note="Kept, from the new door, with the receipts to show the door was the same one every time.")]),

N("review_prep", 45, "The Framework, Plainly", [
 "Ms. Solano prepares you in the framework the review will actually use. At a review of this kind the court determines, among the findings the law lists, the continuing necessity of placement, compliance with the permanency plan, progress toward alleviating the circumstances that caused placement, and whether reasonable efforts were made to finalize the plan (42 Pa.C.S. \u00a7 6351(f)(1), (2), (3), (5.1)). Housing sits inside several of those at once \u2014 which is why one adjective on a summary line is not a small thing.",
 "'And one more piece,' she says, 'because it is in your file whether we raise it or not. Housing assistance was a service in Naledi's plan. The plan promised help with housing costs and referrals. What the record shows, so far, is a landlord's letter and your own paper \u2014 the assistance itself is a documented gap. If a filing question ever arises on the federal timeline \u2014 at fifteen of the most recent twenty-two months, the filing duty changes unless an exception is documented, including where services the agency was required to provide were not provided (42 U.S.C. \u00a7 675(5)(E)) \u2014 then whether that gap is documented, on this record, will matter. Exceptions are not hopes. They are documents. So we document.'",
], [C("Assemble the final packet \u2014 letter, agreement, receipts, applications, correction", "packet_assembly",
      note="Five kinds of paper, one chronology. The packet does not argue that a cousin's spare room is a palace. It argues that it is documented.")]),

N("packet_assembly", 48, "Date Order, Again", [
 "The packet takes an evening: the landlord's letter, the signed agreement, the receipts in their months, the two stamped applications, the housing entries beside the filed correction. Copied, paginated, plain. Ms. Solano adds the plan's own housing-assistance line, highlighted \u2014 the service the plan promised, beside the gap the record shows.",
 "Yours goes in the folder \u2014 this month, at the front, where the next summary writer, if summaries must be written about your housing again, will meet the whole story first.",
], [C("File the packet copies and go to the review", "review", cash=-5,
      addHidden=["Review packet \u2014 housing chronology and plan-service line filed in date order"],
      note="Every page in it existed before the review was convened, and most existed before the summary line was drafted. Sequence is the argument.")]),

N("review", 52, "The Review", [
 f"The review convenes on {d110(52)}. The report is read the way reports are read: as the case, by people who were not at Fern's kitchen table for any of it. The housing paragraph arrives, and what happens next depends, with a precision this scenario has been honest about since a landlord's letter, on what your choices put into the file before the reading started. Ms. Solano rises.",
 "Choose the presentation the record you actually built can carry.",
], [C("Present the documented housing \u2014 agreement, receipts, stamped applications, and the correction filed before today", "end_win",
      requiresFlags=["agreementSigned", "applicationsDated", "recordsRequested", "correctionFiled"],
      note="This presentation exists because the tenancy, its performance, its future, and its correction all exist as dated paper filed before the room convened."),
    C("Present the folder at the review \u2014 real papers, produced live against the printed line", "end_line_stands",
      note="The folder is real. So is the discount rooms apply to paper they meet for the first time at speaking speed."),
    C("Accept the room's suggestion \u2014 enter a shelter placement to be counted as housed", "end_shelter",
      note="A bed in a shelter would satisfy the line's vocabulary. It would also end the arrangement Fern's house actually provides.")]),

N("end_win", 59, "Ending \u2014 Stable, On the Record", [], ending=True, debrief=[
 f"WHAT THE FILE HELD (the record, revealed): A complete housing chronology, in dated paper. A landlord's non-renewal letter ending the tenancy on {d110(30)} \u2014 a landlord's act, not a mother's failure. A signed, dated room agreement at Fern's from {d110(10)}, rent receipted monthly, a room with a door kept Naledi-sized. Two housing applications, date-stamped {d110(18)}, pending at two offices. The case record, requested in writing, showing housing entries that omitted all of it \u2014 and a correction, filed before the review with every attachment, that put the second half of the story into the file. At the review, the court recorded the doubled-up arrangement as stable housing with applications pending, and the summary line was corrected on the record: the adjective 'unstable' no longer describes this mother's housing in any copy of the file.",
 "THE PROCESS UNDER THIS PATH (described, keeping to this scenario's verified law): The review weighed housing inside the determinations the law assigns it \u2014 continuing necessity of placement, compliance with the permanency plan, progress toward alleviating the circumstances that caused placement, and whether reasonable efforts were made to finalize the plan (42 Pa.C.S. \u00a7 6351(f)(1), (2), (3), (5.1)) \u2014 and on a documented record, the housing findings could be made truthfully. The record request (55 Pa. Code \u00a7 3130.44(d)) is what showed the entries' omissions while the draft was still correctable, and counsel (42 Pa.C.S. \u00a7 6337) filed the correction where summaries are written from. The plan's promised housing assistance, and its documented gap, are now also on this record \u2014 documented, exactly as the federal timeline's services exception requires any such claim to be if it is ever to matter (42 U.S.C. \u00a7 675(5)(E), where at fifteen of the most recent twenty-two months the filing duty changes unless an exception is documented, including services the agency was required to provide but did not; any filing would still have to be proven on its own grounds). Label this win honestly: it is partial. Naledi remains placed and the plan continues. What was won is the truthful record \u2014 and what it unlocks: reviews, services, and any future filing question will now start from documented stability instead of from an adjective.",
 "THE HONEST PART: A different review could have weighed a doubled-up room more skeptically even on this paper; a landlord in another story renews, and the whole chapter never happens; Fern herself \u2014 her house, her steadiness, her willingness to sign \u2014 is a piece of luck no strategy manufactures, and this debrief will not pretend the packet created her. Housing lists move at their own pace, and pending may mean pending for a long while yet. What your choices controlled was narrower: when the lease was lost through no act of yours, the arrangement that replaced it was documented as it was built \u2014 signed, receipted, applied from, and corrected into the file before a summary could finish the story with one word. Outcomes in this system turn on workers, judges, landlords, and luck as much as on any parent's choices. This one turned, in part, on a receipt book and two date stamps \u2014 which is not a small thing to have turned on.",
]),
N("end_line_stands", 59, "Ending \u2014 The Line Stands", [], ending=True, debrief=[
 "WHAT THE FILE HELD (the record, revealed): At the review, the summary's housing line was read first, as summary lines are: 'unstable housing.' The folder \u2014 to the extent your choices built one \u2014 was produced against it live: real papers, in several cases, but unfiled, or incomplete, or unattached to the entries they answered. The room heard two accounts of the same household and credited the one that had been in the file when the packet was assembled. The line stands into the next review cycle: housing will be reported as unstable, services and findings will be built on that description, and the arrangement at Fern's \u2014 stable in the house, month after month \u2014 will have to be reintroduced, as a correction, to every future reader who meets the line first.",
 "THE PROCESS UNDER THIS PATH (described, keeping to this scenario's verified law): Nothing in this ending failed for lack of a right. The housing entries were requestable in writing (55 Pa. Code \u00a7 3130.44(d)); counsel (42 Pa.C.S. \u00a7 6337) could have filed a one-page chronology with the agreement, receipts, and stamped applications attached at any point in the eight weeks; and the review's own framework (42 Pa.C.S. \u00a7 6351(f)(1), (2), (3), (5.1)) makes housing findings from evidence \u2014 which is to say, from paper in the file, not from paper in a folder produced at speaking speed. A correction filed before a review settles; the same correction produced at a review contests, and contested housing reads, to cautious rooms, as unstable housing with an argument attached. The line is now the argument's target for the next cycle instead of its casualty in this one.",
 "THE HONEST PART: Let this debrief be as fair as the line was not: your housing, as lived, was stable \u2014 a room with a door, rent paid, a child-sized corner kept ready, applications a stamp away. The gap in this ending is not between a good household and a bad one. It is between a household and its documentation, and documentation gaps are taxed, in this system, entirely to the parent \u2014 never to the summary that created the need for them. A different worker might have visited Fern's, seen the room, and written it up truthfully unprompted; some do. Yours drafted from a landlord's letter and a note, and the file inherited the difference. The correction can still be filed tomorrow, with the same attachments, and the next review will read a truer file. It cannot retroactively make this review have decided housing on the truth.",
]),
N("end_shelter", 59, "Ending \u2014 Housed, by Definition", [], ending=True, debrief=[
 "WHAT THE FILE HELD (the record, revealed): The room's suggestion was taken: a shelter placement, accepted so that the housing line could be satisfied in its own vocabulary. The line is satisfied. It now reads, in substance, housed \u2014 shelter. And the arrangement that was actually stable \u2014 Fern's room, the signed or unsigned agreement, the receipts or their absence, Naledi's corner kept ready \u2014 is ended, its paper trail stopping in the month the definition won. Future summaries will record a mother who left a relative's stable room for a shelter bed in order to be counted as housed, and none of them will record that the counting was the reason.",
 "THE PROCESS UNDER THIS PATH (described, keeping to this scenario's verified law): This ending is not produced by a rule that prefers shelters \u2014 no such rule is stated anywhere in this scenario, because none is in its verified law. It is produced by a vocabulary: a summary line that could describe a doubled-up tenancy only as 'unstable,' answered not by documenting the tenancy but by abandoning it for an arrangement the vocabulary already had a box for. The instruments that answer a line with paper existed throughout (the record on request, 55 Pa. Code \u00a7 3130.44(d); counsel to file the correction, 42 Pa.C.S. \u00a7 6337), and the review framework itself (42 Pa.C.S. \u00a7 6351(f)(1), (2), (3), (5.1)) decides from evidence \u2014 evidence a documented tenancy would have supplied. Definitions, unopposed by documents, quietly become decisions. That, and not any fact about Fern's house, is this ending.",
 "THE HONEST PART: Be clear about what was traded, because the file will not be: shelter is not nothing. For a mother with no Fern, it is safety, an address, a door that locks, and this debrief does not rank it beneath anyone's spare room as a place to sleep. The loss here is specific to this story: a stable, documented-or-documentable family arrangement was exchanged for a categorical one, at a cost \u2014 Naledi's room at her cousin's, the tenancy's accumulating months, the applications' address \u2014 that the housing line never priced, because lines do not price things. They only classify them. What classifies a household, in the end, should be the household, proved on paper. In this ending the paper was never given the chance to out-argue the adjective, and the adjective, satisfied at last, is the only winner in the file.",
]),
]

s110_meta = {"title": "The First 90 Days",
 "subtitle": "Scenario 110 \u2014 Unstable, On Paper (a fictional composite)",
 "startDateISO": "2026-10-19", "startNode": "start", "startCash": 160,
 "tier": "Hard",
 "summary": "At month nine a landlord's non-renewal moves Charise into her cousin's spare room \u2014 signed, receipted, applied from \u2014 while the plan's housing line still reads 'unstable housing.'"}

WIN110 = {
 "start": "Read the letter twice, and keep it \u2014 it is now a case document",
 "letter_close": "Start the search the way searches actually start \u2014 with who you know",
 "search_days": "Go and look at the room, and at the arrangement, with clear eyes",
 "fern_door": "Decide how the arrangement will exist \u2014 on paper, or on trust",
 "agreement_choice": "Write and sign the room agreement with Fern, dated, before you move a single box",
 "agreement_signed": "Move in, and set up the rent the way the agreement says",
 "move_day": "Pay by receipt from the first month \u2014 dated, signed, room and month named",
 "receipts_kept": "Turn to the second half of stability \u2014 the applications",
 "applications_choice": "Apply to both lists and keep the date-stamped copies",
 "applications_done": "Go to the plan meeting and hear the housing line read aloud",
 "plan_line": "Note the line word for word, and ask your lawyer what the file itself says",
 "records_fork": "Sign the written request for the record \u2014 housing entries and draft summary",
 "record_arrives": "Decide how the second half is filed \u2014 in writing before the review, or aloud at it",
 "correction_choice": "File the written correction before the review, with the agreement, receipts and applications attached",
 "correction_filed": "Keep the arrangement exactly as documented until the review",
 "visits_meanwhile": "Prepare for the review with Ms. Solano",
 "review_prep": "Assemble the final packet \u2014 letter, agreement, receipts, applications, correction",
 "packet_assembly": "File the packet copies and go to the review",
 "review": "Present the documented housing \u2014 agreement, receipts, stamped applications, and the correction filed before today",
}

# =====================================================================
# SCENARIO 111 — The Costs Column
# Start: Monday, August 17, 2026. Zane in kinship care with his aunt
# Sonya before the story; no 'removed' flag. No statute about fines,
# costs, or driving privileges is stated anywhere: every procedural
# fact comes from the clerk's letters' own faces (diegetic process).
# Saturday visits: day 5 and day 33 are Saturdays (asserted below).
# =====================================================================
S111_START = date(2026, 8, 17)
assert S111_START.strftime("%A") == "Monday"
assert (S111_START + timedelta(days=5)).strftime("%A") == "Saturday"
assert (S111_START + timedelta(days=33)).strftime("%A") == "Saturday"
d111 = lambda off: datestr(S111_START, off)

s111_nodes = [
N("start", 0, "The Clerk's Letter", [
 "Your name is Terrell. Your son Zane is six, and he is in kinship care with his aunt Sonya \u2014 placed before this story opens, in a house where his height is marked on a doorframe in pencil. Your case with Zane is one case. The letter in today's mail is from a different one.",
 f"The letter, dated {d111(0)}, is from a clerk's office, about an old matter from before Zane's case existed: fines and costs, long since assessed, that you have been paying down on a payment plan. The letter says, in its own words, that the plan has lapsed. It states its own deadline \u2014 respond and bring the plan current through the process it describes by {d111(21)} \u2014 and it states, in its own words, its own consequence if you do not: your driving privileges will be acted on under the process the letter describes.",
 "It is one page. It does not mention Zane, visits, or any court in his case. The two matters share nothing except you \u2014 and, as this story will show, a Saturday.",
], [C("Read the letter a second time, including its deadline and its stated process", "letter_close",
      note="The letter is the whole law of this scenario: what it says, by when, and what it says happens next. Read only that, and read it exactly.")]),

N("letter_close", 1, "What Lapsed, Exactly", [
 "On the second reading, the letter is precise in the way clerk's letters are precise: the plan exists; two payments are recorded as late; because of them, the plan is shown as lapsed. The letter does not say you did not pay. It says the payments posted late \u2014 recorded so, in a ledger, in a column.",
 "Posted late is a phrase with two possible authors: a man who paid late, or a process that posted late. The letter, fairly, does not choose between them. It reports a ledger. Ledgers can be answered \u2014 with the paper that ledgers are made from, if the paper was kept.",
 "Your payment receipts live the way most such paper lives: some in a drawer, some in a glove compartment, all of them real. Whether they survive as evidence depends on a decision you make this week, before any Saturday arrives to complicate it.",
], [C("Look at the old plan itself \u2014 how it ran, before it lapsed", "old_plan",
      note="A plan that ran for years and lapsed on two postings is a different object from a plan that was never honored. The drawer decides which one can be proved.")]),

N("old_plan", 2, "The Plan That Ran", [
 "The plan is old \u2014 older than Zane's case, older than Zane's school, a leftover column of numbers from a younger man's matter, paid down month by month in the unglamorous way such columns are paid: steadily, mostly on time, in amounts that were never large and never nothing.",
 "Two payments in that long run are now recorded as late. You remember those months. You remember paying \u2014 at the counter, through the processor the plan uses, with receipts that printed warm. Paying and posting are different events, separated, in the processor's world, by days. In the ledger's world, only one of them has a date.",
 "The letter's deadline stands at the date the letter stated. Before it stands a Saturday: Zane's visit, at Sonya's, across town \u2014 a drive you have made every week of his placement.",
], [C("Find the receipts for the two payments the letter calls late", "receipts_choice",
      note="Two months, two receipts. The whole first half of this scenario is whether warm-printed paper survived a glove compartment.")]),

N("receipts_choice", 4, "Warm Paper, Kept or Lost", [
 "The drawer and the glove compartment between them hold your payment history the way they hold everything: truly, and without an index. The two receipts in question exist \u2014 printed at the counter on the days you paid, showing the payment date, days before the dates the ledger recorded. Kept together, dated, they are the difference between a man who paid late and a posting that lagged. Left scattered, they are litter with numbers on it.",
 "Gathering them costs an evening. The letter's clock, and Zane's Saturday, will not wait for a more convenient evening to exist.",
], [C("Gather both receipts tonight and keep them with the letter, in date order", "receipts_found", cash=-3,
      setFlags=["receiptsKept"],
      addHidden=["Payment receipts \u2014 both payments made before the ledger's posted dates; receipts kept"],
      note="Three dollars of copies and a folder. The receipts now sit beside the letter they answer, which is where receipts do their work."),
    C("Leave the receipts where they live \u2014 you know you paid, and that's the truth of it", "receipts_scattered",
      note="It is the truth of it. Truth, unattached, is about to meet a ledger, and ledgers do not attend kitchen tables.")]),

N("receipts_found", 5, "Paid, Then Posted", [
 f"Side by side, the paper tells a small, complete story. Receipt one: paid on its date, in the month the letter questions. The ledger's entry for that payment: posted days later, across the plan's due line. Receipt two: the same shape, the same lag, the same column's verdict \u2014 late. You paid on time, twice. A processor posted late, twice. The ledger recorded the second event and called it by the first event's name.",
 "None of this, yet, is filed anywhere it matters. It is a folder on a table, on the morning of Zane's visit \u2014 and the letter, unanswered, has already stated what it says happens to your driving privileges if its process is not followed by its date.",
], [C("Face the Saturday decision with the letter open on the table", "saturday_choice",
      note="The visit is today. The letter is also today. This scenario lives in the space between those two sentences.")]),

N("receipts_scattered", 5, "True, and Somewhere in a Drawer", [
 "Your memory of the two payments is exact: the counter, the amounts, the warm receipts going into the glove compartment or the drawer or a coat. Any person who knows you believes the account instantly. The ledger, which does not know you, has already published its version: late, late, lapsed.",
 "Today is Zane's visit \u2014 a drive across town, as every week \u2014 and the clerk's letter, unanswered on the table, has stated in its own words what it says happens to your driving privileges under its process. Memory does not answer letters. But the Saturday decision arrives whether memory is ready or not.",
], [C("Face the Saturday decision with the letter open on the table", "saturday_choice",
      note="Two pieces of paper are in this room: a letter with a deadline, and a visit with a boy. Only one of them can be rescheduled by wanting to.")]),

N("saturday_choice", 5, "The Saturday Decision", [
 f"The visit with Zane is today, {d111(5)}, at Sonya's, across town. The drive is the ordinary drive of Zane's whole placement. The letter on the table says \u2014 in its own words, which are the only words this scenario treats as its process \u2014 that your driving privileges are acted on under its process if the plan is not brought current by the process and date it states, and that date has not yet come, and the plan is, on the ledger, lapsed today.",
 "You can decline to drive against the letter: miss the visit, take the bus nowhere, and be a father who was not there on a Saturday his son counts by. Or you can drive anyway \u2014 the ordinary drive, on the ordinary road \u2014 and convert a paper problem, receipts and postings, into whatever a stop on that road would make of it.",
 "There is no third option on the table. There is only the question of what gets written down afterward, and by whom.",
], [C("Do not drive against the letter \u2014 miss the visit, and stay off the road until the letter's process is answered", "visit_missed",
      setFlags=["didNotDrive"],
      addHidden=["Visit \u2014 missed rather than drive against the clerk's letter; no written explanation sent that day"],
      note="You stay home. The road stays un-driven. What the day will be recorded as is now entirely up to what the file gets told, and when."),
    C("Drive anyway \u2014 the visit matters more than a clerk's column", "visit_driven",
      setFlags=["droveAnyway"],
      addHidden=["Visit \u2014 father drove to the visit while the letter's stated consequence was outstanding"],
      note="The visit happens. The drive also happens, on a road where a paper problem can stop being paper at any set of lights.")]),

N("visit_missed", 6, "The Empty Chair", [
 "Saturday passes with an empty chair at Sonya's table. Zane asks where you are, in the direct way six-year-olds ask the only question there is, and Sonya answers kindly and truthfully, in the version available to her: something about a letter and a car. You call, that evening. Your voice is there. Your chair was not.",
 "What you do not do \u2014 today, or in the days after \u2014 is tell anyone in writing. The call is warm, human, and unrecorded in every file that will ever be read by Zane's review. A missed visit, unexplained in writing, is a blank space in a log. Blank spaces, in this system, are filled by whoever writes next \u2014 and the next writer is never the father.",
], [C("Read what the visit log writes about the Saturday you stayed home", "note_phrase",
      note="Logs are short. That is not a mercy. Short is how a sentence gets quoted forever.")]),

N("visit_driven", 6, "The Visit, and the Drive Back", [
 "The visit is good \u2014 visits with Zane are good in the uncomplicated way that makes the rest of this case bearable \u2014 and the drive there is uneventful. The drive back is the one the letter was about: a paper status, traveling at road speed, through a world where statuses get checked. Nothing, this time, checks yours. You arrive home with the visit kept and the gamble won, this time.",
 "What the file records is a kept visit. What it does not record is the drive. Both facts are now true, and only one of them is in any file \u2014 until the day, if it comes, when the other one gets written by someone whose job is writing exactly that.",
], [C("Go on into the week \u2014 the letter still on the table, its date still coming", "note_phrase",
      note="Kept visits are recorded. Kept gambles are recorded later, by other hands, if they are recorded at all.")]),

N("note_phrase", 8, "No Explanation", [
 f"On {d111(8)} you see the visit note, because Sonya, who keeps her own copies of everything in a labeled binder that shames your drawer, shows you hers. If you stayed home, the note reads, in full: 'Father missed visit, no explanation.' Three facts in six words, and one of them \u2014 the explanation \u2014 is false in the way an absence can be false: there was an explanation. It was a letter, a deadline, and a stated consequence. It simply was never sent anywhere the note's author could read it.",
 "If you drove, the note reads 'visit held,' and is true, and sits in the file beside a drive that no note mentions. Either way, the file's account of that Saturday is now a sentence other people will quote, and the only question left is whether your paper ever joins it.",
 "A second envelope from the clerk's office is already in the mail. In this system, second envelopes are how first letters grow.",
], [C("Open the second envelope when it comes", "second_letter",
      note="You already know its shape. What you do not know is its number \u2014 second letters in this column always have a bigger one.")]),

N("second_letter", 11, "The Balance, Grown", [
 f"The second letter arrives on {d111(11)}. It restates the lapsed plan. It raises the balance: added costs, listed in its own column, in its own words, bringing the total to the figure it states. And it repeats its process: the form it encloses, the office it names, and its own new deadline \u2014 {d111(32)} \u2014 for bringing the plan current or having it reinstated through the process the letter describes.",
 "Two letters now. Between them they contain every procedural fact this scenario will ever use: dates, amounts as the letters state them, a form, an office, deadlines, consequences in the letters' own words. No other law of fines or driving will be consulted, because none is needed: the letters are the process, and the process can be followed, in writing, on time.",
 "Zane's review is also coming \u2014 the room where 'no explanation' will be read, unless the explanation, in writing, gets there first.",
], [C("Lay both letters beside the receipts and the visit note, and call your lawyer in Zane's case", "ledger_beat",
      note="Four documents, two cases, one kitchen table. Lawyers in this series earn their keep at exactly this table.")]),

N("ledger_beat", 12, "Receipts Against a Ledger", [
 "Receipts against a ledger is a fair fight, if it is ever actually fought. The receipts say paid, with dates. The ledger says posted, with later dates. Two of the plan's late entries are the distance between those two columns \u2014 a processor's lag, measurable in days, provable in print, if the print is assembled and filed in both directions: to the clerk's process, to answer the letters, and into Zane's record, to answer the note.",
 "The explanation for the missed visit is, at bottom, the same document set: the first letter, dated before the Saturday it cost; the stated consequence, in the letter's own words; and the receipts showing why the letter was wrong about the lapse that triggered it. One packet, two files, every date in it older than the events it explains \u2014 because the letter itself predates the Saturday. That sequence is the explanation's whole strength: it cannot have been invented afterward, because its first page was mailed before.",
], [C("Ask your lawyer how each file gets its copy, in writing", "counsel_visit",
      note="You have a lawyer in Zane's case. What the clerk's file needs, she will tell you, is its own process, followed on its own paper.")]),

N("counsel_visit", 13, "Two Files, One Packet", [
 "You have had a lawyer throughout Zane's case, as the law provides (42 Pa.C.S. \u00a7 6337). Ms. Rutledge reads both letters, the receipts, and Sonya's note copy, in that order, and says the sentence this scenario has been walking toward: 'The letter explains the Saturday. But a letter in your drawer explains it to your drawer. Filed, it explains it to every reader the note will ever have.'",
 "'Two filings, then. The clerk's, through the process the letters themselves describe \u2014 the form, the receipts, the reinstatement request. And Zane's: a written explanation, filed before the review, attaching the first letter, so the visit note and the reason for the visit's absence travel together from now on.'",
 "Or the explanation can stay where it has lived since Saturday: in phone calls, in Sonya's kindness, in your own certainty \u2014 everywhere except a file.",
], [C("Ask for Zane's file itself \u2014 the visit note in its official copy", "records_fork",
      note="'Quote it exactly, or correct a summary of it,' she says. 'There is no third kind of correction.'")]),

N("records_fork", 15, "Ask for the Visit Record", [
 "A party may request the case record, and the material in it 'shall be released upon request' (55 Pa. Code \u00a7 3130.44(d)). The visit notes and the review summary are part of that record: the note in its official wording, and any summary already carrying the Saturday forward in its own words.",
 "The alternative is to write the explanation against Sonya's copy and your memory of the note \u2014 close, probably, and unverifiable in exactly the way that lets a room keep its original sentence.",
], [C("Sign the written request for the record \u2014 visit notes and draft summary", "record_arrives", cash=-3,
      setFlags=["recordsRequested"],
      addHidden=["Case record \u2014 requested in writing, including the visit note and draft review summary"],
      note="Signed, dated, copied. The note's exact six words are about to be in your hands, where corrections can reach them."),
    C("Write against Sonya's copy \u2014 her binder has never been wrong yet", "no_record",
      note="Her binder is excellent. It is also hers. The file's copy is the one the review will read, word for word.")]),

N("record_arrives", 21, "Six Words, Officially", [
 f"The packet arrives on {d111(21)} \u2014 the same date the first letter stated as its deadline, which has its own quiet symmetry. The visit note is there in its official copy, exactly as Sonya's binder promised: 'Father missed visit, no explanation' (or, on the road not taken, 'visit held,' with no sentence anywhere about a drive). The draft review summary carries the Saturday in the file's grammar, one line, unadorned.",
 "A draft is a mercy, if you get to see it in time: every line in it is still soft enough to be joined by another line. The joining document is the explanation \u2014 and its first attachment predates the Saturday, which is a property no document created now can fake.",
], [C("Decide how the explanation is filed \u2014 in writing before the review, or aloud at it", "explanation_choice",
      note="Before, it joins the note. At, it argues with it. The note has waited patiently; it can afford to. It is already filed.")]),

N("no_record", 21, "The Note, at One Remove", [
 "Without the packet, the explanation will be written against a copy of a copy: Sonya's binder version of a note, your memory of a Saturday, a lawyer's draft of both. It may still be filed. But the review reads the file's wording, and a correction aimed one word off its target is a correction a room can honestly call unproven.",
 "Ms. Rutledge is plain: 'We file what we can. Understand what it will be weighed as: an account, not a joining. The note stays the file's sentence; ours becomes its footnote, if we are lucky.'",
], [C("Decide how the explanation is delivered \u2014 in writing before the review, or aloud at it", "explanation_choice",
      note="Footnotes are not nothing. They are also not the text. Choose with the difference in view.")]),

N("explanation_choice", 24, "The Explanation, Filed or Spoken", [
 "The written explanation is short, because its attachments do the work: one paragraph \u2014 the visit was missed (on the road where it was missed) because a clerk's letter, dated before that Saturday, stated a consequence for driving that the father would not drive against; the letter is attached, with its date; the receipts are attached, showing the lapse behind the letter was a posting lag, not a nonpayment. It asks that the explanation be filed with the visit note and reflected in the summary.",
 "Filed before the review, it is a joining: note and reason, traveling together. Spoken at the review, it is a story told to people holding the note \u2014 believed, perhaps, and entered nowhere.",
], [C("File the written explanation before the review \u2014 first letter and receipts attached", "explanation_filed", cash=-4,
      setFlags=["explanationFiled"],
      addHidden=["Written explanation \u2014 filed before the review, with the pre-Saturday letter and payment receipts attached"],
      note="Stamped, copied, joined to the note it answers. Every future reader of that Saturday now reads it in the order it happened."),
    C("Explain it at the review \u2014 your voice, and Sonya's, will carry it", "explanation_oral",
      note="Voices carry rooms. Files carry reviews, and every room after this one. The note is a file. Your voice, that day, will not be.")]),

N("explanation_filed", 26, "Joined, Not Argued", [
 "The explanation goes in with its attachments, and the file accepts it the way files accept everything: without comment, and permanently. The visit note now has company of a kind notes rarely get \u2014 a dated, earlier letter that makes the note's last two words ('no explanation') simply inaccurate as a description of the record, whatever they described about that Saturday's phone calls.",
 "Ms. Rutledge keeps her copy. Sonya, told about it, adds her own copy to the labeled binder, with a tab. The binder, at least, was always a file. Now Zane's is one too.",
], [C("Turn to the clerk's letters themselves \u2014 the plan still stands lapsed on their paper", "reinstatement_choice",
      note="One file corrected. The other file \u2014 the one with the column \u2014 is still waiting for its own process to be followed.")]),

N("explanation_oral", 26, "True, at Speaking Speed", [
 "The explanation stays in the world of voices: yours, Sonya's, Ms. Rutledge's assurance that it will be raised. Raised is a tense that reviews are fluent in discounting. The note, meanwhile, sits in the draft summary, filed, quoted, at rest \u2014 a sentence with a head start measured in weeks.",
 "What can still be done, fully and on time, is the other filing: the clerk's own process, in the clerk's own window, with the receipts that answer its ledger.",
], [C("Turn to the clerk's letters themselves \u2014 the plan still stands lapsed on their paper", "reinstatement_choice",
      note="Ledgers, unlike reviews, can only be answered one way: in their own process, with their own paper, by their own dates.")]),

N("reinstatement_choice", 28, "The Letters' Own Process", [
 f"The second letter stated the process on its face: its enclosed form, its named office, its deadline of {d111(32)}. The reinstatement request, assembled, is the ledger's answer in the ledger's language: the form, the two receipts with their payment dates, and a one-line request that the plan be reinstated on the ground the documents state \u2014 the payments were made on time and posted late, by days, through the processor.",
 "Filing it costs copies and a fare. Not filing it costs nothing this week, and leaves two letters, a grown balance, and a stated consequence all standing in their harder tense at their stated date.",
], [C("File the reinstatement request through the letters' own process \u2014 form and receipts, inside the stated window", "reinstatement_filed", cash=-5,
      setFlags=["reinstatementFiled"],
      addHidden=["Payment plan \u2014 reinstatement requested through the letters' own process, receipts attached, inside the window"],
      note="Filed with days to spare. The ledger now has to reckon, in its own column, with the receipts' dates sitting beside its own."),
    C("Let the letters wait \u2014 Zane's review matters more than an old column", "reinstatement_ignored",
      note="Reviews do matter more. Columns, unattended, do not stay columns. That is the second letter's whole message, in its own words.")]),

N("reinstatement_filed", 30, "Filed, in Its Own Language", [
 f"Filed on {d111(30)}, inside the window the second letter stated. The office's receipt is a small, stamped thing, and you keep it the way you now keep everything: dated, copied, with the letters it answers. Whatever the office decides, it will decide it about documents \u2014 a ledger's dates against receipts' dates \u2014 which is the first fair fight this old column has ever been offered.",
 "Zane's next visit, meanwhile, is coming on its ordinary Saturday rhythm, and the road to Sonya's is, for now, a road the letters' process is actively answering.",
], [C("Take the bus-and-ride Saturday combination to Zane's next visit, carefully, while the filing is read", "zane_visit",
      note="Slower, costlier in time, and entirely off the ledger's road. Visits, unlike columns, cannot be reinstated once missed. They can only be kept, one by one.")]),

N("reinstatement_ignored", 30, "The Column, Standing", [
 "The letters wait, in the way letters with stated dates wait: briefly, and then not at all. The balance stands with its added costs. The stated consequence stands in the second letter's words. And the road to Sonya's \u2014 the ordinary Saturday road of Zane's whole placement \u2014 now carries all of it, unaddressed, at road speed.",
 "Zane's next visit arrives on schedule regardless. Schedules in this story have never once consulted the files they run beside.",
], [C("Face the next visit with the letters still unanswered", "zane_visit",
      note="A boy, a Saturday, a road, and a column. The visit will be recorded. So, in their ways, will the other three.")]),

N("zane_visit", 33, "The Next Visit, Kept", [
 f"The visit on {d111(33)} is kept \u2014 by whatever road your choices have left open, it is kept, and it is good: Zane has a doorframe measurement to report and a joke he has been saving, in the way six-year-olds save jokes, by telling it immediately. Sonya feeds everyone. The visit note, this time, will say the visit was held, because it was.",
 "One kept visit does not erase a missed one in a log. Logs are cumulative, not merciful. What decides the missed one's meaning at the review is whether its explanation is in the file beside it \u2014 and whether the letters that caused it are being answered in their own process or ripening in their drawer.",
], [C("Prepare for the review with Ms. Rutledge", "prep",
      addHidden=["Visits \u2014 subsequent visit kept; explanation and reinstatement filings pending the review"],
      note="Kept, and noted as kept. The review will now read two Saturdays, and whatever paper joins each of them.")]),

N("prep", 38, "Two Saturdays, in Two Piles", [
 "Ms. Rutledge spreads the matter in two piles. Pile one: a clerk's first letter, a ledger's two late postings, a six-word visit note, a second letter with a grown balance. Pile two \u2014 if your choices built it \u2014 two warm-printed receipts with earlier dates than the ledger's, a record packet quoting the note exactly, an explanation filed before this room convenes with the pre-Saturday letter attached, and a reinstatement request filed inside the second letter's own window.",
 "'The review will read the missed Saturday from one of these piles,' she says. 'Our whole job, for six weeks, was choosing which.'",
], [C("Assemble the packet in date order, with copies", "review", cash=-4,
      addHidden=["Review packet \u2014 letters, receipts, visit note and filed explanation, in date order"],
      note="Date order matters here more than anywhere in this series: the letter predates the Saturday. The packet's order is its proof.")]),

N("review", 44, "The Review", [
 f"The review convenes on {d111(44)}. Zane's plan is the business of it; the missed Saturday is one line \u2014 and lines, in reviews, are read from the note unless something filed displaces them. The clerk's matter is not before this room, and Ms. Rutledge does not pretend otherwise: what is before this room is a visit note, and what a father's other file did to a Saturday. She rises with whatever your choices actually put in her hands.",
 "Choose the presentation the paper you built can carry.",
], [C("Present the joined record \u2014 the explanation filed before today, the pre-Saturday letter, and the receipts, with the plan's reinstatement filed", "end_win",
      requiresFlags=["receiptsKept", "recordsRequested", "explanationFiled", "reinstatementFiled"],
      requiresNoFlags=["droveAnyway"],
      note="This presentation exists because the explanation was filed, not spoken \u2014 and because its first attachment is dated before the Saturday it explains."),
    C("Explain the Saturday aloud \u2014 the letter, the road, the choice you made", "end_note_stands",
      note="Every word true. The note, printed and already read, sits across the table with the head start this scenario measured in weeks."),
    C("Present the kept visit and let the drive stand as the answer", "end_drove",
      requiresFlags=["droveAnyway"],
      note="The visit was kept. This presentation asks the room to price the visit and ignore the road it took to get there.")]),

N("end_win", 51, "Ending \u2014 Explained, On the Record", [], ending=True, debrief=[
 f"WHAT THE FILE HELD (the record, revealed): A Saturday, fully documented at last. A clerk's letter dated {d111(0)} \u2014 before the missed visit \u2014 stating its own deadline and, in its own words, its own consequence for driving. Two payment receipts showing both questioned payments made on time and posted late by the processor, days later, across the plan's due line: the lapse was a posting lag, proved from the counter's own paper. A written explanation filed before the review, joining the letter and the receipts to the visit note, so that 'father missed visit, no explanation' no longer travels alone \u2014 at the review, the visit record was corrected on the record to state the explanation the documents carry. And in the clerk's own process, the reinstatement request \u2014 form and receipts filed on {d111(30)}, inside the second letter's stated window \u2014 reinstated the payment plan on the documented posting dates, the grown balance corrected to the plan's own terms as the letters describe them.",
 "THE PROCESS UNDER THIS PATH (described, keeping to this scenario's verified law): Two verified instruments did the joining in Zane's case: the case record, released on request (55 Pa. Code \u00a7 3130.44(d)), which put the note's exact wording in the father's hands while the draft summary was still correctable, and counsel (42 Pa.C.S. \u00a7 6337), who filed the explanation where the note lives. Everything in the clerk's matter \u2014 the lapse, the balance, the reinstatement \u2014 was handled through the letters' own stated process, on the letters' own forms, inside the letters' own windows, and this ending states no statute about fines, costs, or driving privileges because none was used and none is in the verified set: the letters were the process, followed exactly. Label this win honestly: it is partial. Zane remains in kinship care with Sonya, his case continues, the old column continues to be paid down month by month, and one Saturday with a six-year-old is gone in every ending this scenario has. What was won is that the record of that Saturday, and of the plan, now says what actually happened \u2014 in both files.",
 "THE HONEST PART: A different clerk's office could have read the same receipts ungenerously; a different reviewer could have corrected the note and still weighed the missed visit heavily; the processor's lag, in another month, might have left no receipts to find, because glove compartments are not archives. Sonya's binder, her copies, her labeled tabs \u2014 luck wearing an apron \u2014 held pieces of this outcome too. What your choices controlled was the paper: receipts gathered before a Saturday complicated them, a record requested while a draft was soft, an explanation filed instead of spoken, and a reinstatement sought through the very process the letters offered, in their own window. Outcomes in this system turn on clerks, reviewers, processors, and luck as much as on any father's choices. This one also turned on refusing, once, to let a ledger's dates be the only dates in the room.",
]),
N("end_note_stands", 51, "Ending \u2014 No Explanation, Still Standing", [], ending=True, debrief=[
 "WHAT THE FILE HELD (the record, revealed): At the review, the visit note was read as it was written on the Saturday it describes: 'Father missed visit, no explanation.' The explanation \u2014 a real letter, a real stated consequence, a real posting lag behind both \u2014 was offered aloud, in parts, at speaking speed, against a printed line the room had already read. It was believed in the way spoken explanations are believed in rooms that run on attachments: personally, and without a filing to attach the belief to. The note stands into the next review as the file's account of that Saturday, available to every future summary, and the missed visit will be weighed in Zane's case as what the note calls it: unexplained.",
 "THE PROCESS UNDER THIS PATH (described, keeping to this scenario's verified law): The instruments that join an explanation to a note are the verified ones, and they were available from the week the note was written: the case record on written request (55 Pa. Code \u00a7 3130.44(d)), to quote the note exactly and answer its exact words, and counsel (42 Pa.C.S. \u00a7 6337) to file the explanation \u2014 letter and receipts attached \u2014 where the note lives, before the review convenes. Paper filed before a hearing joins the record; the same truth spoken at a hearing annotates it, at best, in minutes nobody quotes. In the clerk's matter, the same distinction governed: the letters offered their own process, in their own words and windows, and processes, like notes, credit filings, not accounts. Nothing in this ending required anyone's bad faith \u2014 only the ordinary physics of whose paper was in which file on the day each room convened.",
 "THE HONEST PART: Let this debrief be as fair as the note was not: the Saturday was missed for a reason the file's own attachments could have proved in one page \u2014 a letter that predated it, stating a consequence no careful father drives against, issued over a lapse that was itself a processor's lag. You weighed a clerk's stated consequence against a six-year-old's Saturday and chose the road not taken, literally, and then the explanation lived where explanations go to be forgotten: in phone calls. A different worker might have asked, that week, why the chair was empty, and written the answer down herself; some do. Yours wrote six words, accurately, from an empty file. The explanation can still be filed now \u2014 the letter still predates the Saturday, the receipts still predate the ledger \u2014 and the next review can still be given a joined record. It will arrive as a correction, argued, instead of as the record it could simply have been.",
]),
N("end_drove", 51, "Ending \u2014 A Paper Problem, Driven Into a Legal One", [], ending=True, debrief=[
 "WHAT THE FILE HELD (the record, revealed): A kept visit, recorded as kept \u2014 and, outside every file until it mattered, a drive taken while a clerk's letter's stated consequence for driving was outstanding. The gamble that nothing would check the status on that ordinary road was, in the short run, won: no stop, no entry, a good visit. In the longer run the drive converted the matter's whole character. A lapsed plan is a column of numbers, answerable with receipts in the letters' own process. A drive taken against a letter's stated consequence is a different kind of fact \u2014 one that, if it is ever entered by the hands whose job is entering such facts, re-prices everything else in both files: the receipts become background, the posting lag becomes a detail, and the Saturday becomes the day the father was told, in writing, and drove anyway.",
 "THE PROCESS UNDER THIS PATH (described, keeping to this scenario's verified law): This ending states no statute about fines, costs, or driving privileges, because none is in the verified set and none is needed to see the shape of it: the letters carried their own process on their faces \u2014 a form, an office, deadlines, a stated consequence \u2014 and following that process (form and receipts filed inside the stated window) keeps a paper problem paper-sized. Counsel in Zane's case (42 Pa.C.S. \u00a7 6337) and the visit record on request (55 Pa. Code \u00a7 3130.44(d)) were the instruments for the dependency side of the Saturday, exactly as in every other ending. What changed here was not the law of anything. It was the exposure: a documented, dated warning was answered with a drive instead of a filing, and exposure, unlike a balance, cannot be paid down on a plan.",
 "THE HONEST PART: Be clear about the choice's human weight, because the file never will be: you drove to a six-year-old who counts his week in Saturdays, on the ordinary road of his whole placement, because the alternative was an empty chair \u2014 and parents in this system are handed that exact exchange, letters against Saturdays, more often than any policy admits. The visit itself was good, and Zane's memory of that day is a kept day, not a missed one; no debrief here will call that nothing. But the system you both live in prices papers, not reasons, and it had offered a paper answer \u2014 receipts, a form, a window \u2014 at the price of one Saturday. This ending is what declining that price can cost when the road, one day, decides to check. Outcomes turn on luck here more nakedly than anywhere else in this series: the same drive, on a luckier road, is a kept visit and a closed file. Luck is not a filing system, and it is not a defense. It is only, on this road, what happened not to happen \u2014 this time.",
]),
]

s111_meta = {"title": "The First 90 Days",
 "subtitle": "Scenario 111 \u2014 The Costs Column (a fictional composite)",
 "startDateISO": "2026-08-17", "startNode": "start", "startCash": 160,
 "tier": "Hard",
 "summary": "An old fines-and-costs plan lapses on two processor-late postings; a clerk's letter, a missed Saturday visit, and a six-word note turn a ledger's lag into a father's record \u2014 unless the receipts are filed in both files."}

WIN111 = {
 "start": "Read the letter a second time, including its deadline and its stated process",
 "letter_close": "Look at the old plan itself \u2014 how it ran, before it lapsed",
 "old_plan": "Find the receipts for the two payments the letter calls late",
 "receipts_choice": "Gather both receipts tonight and keep them with the letter, in date order",
 "receipts_found": "Face the Saturday decision with the letter open on the table",
 "saturday_choice": "Do not drive against the letter \u2014 miss the visit, and stay off the road until the letter's process is answered",
 "visit_missed": "Read what the visit log writes about the Saturday you stayed home",
 "note_phrase": "Open the second envelope when it comes",
 "second_letter": "Lay both letters beside the receipts and the visit note, and call your lawyer in Zane's case",
 "ledger_beat": "Ask your lawyer how each file gets its copy, in writing",
 "counsel_visit": "Ask for Zane's file itself \u2014 the visit note in its official copy",
 "records_fork": "Sign the written request for the record \u2014 visit notes and draft summary",
 "record_arrives": "Decide how the explanation is filed \u2014 in writing before the review, or aloud at it",
 "explanation_choice": "File the written explanation before the review \u2014 first letter and receipts attached",
 "explanation_filed": "Turn to the clerk's letters themselves \u2014 the plan still stands lapsed on their paper",
 "reinstatement_choice": "File the reinstatement request through the letters' own process \u2014 form and receipts, inside the stated window",
 "reinstatement_filed": "Take the bus-and-ride Saturday combination to Zane's next visit, carefully, while the filing is read",
 "zane_visit": "Prepare for the review with Ms. Rutledge",
 "prep": "Assemble the packet in date order, with copies",
 "review": "Present the joined record \u2014 the explanation filed before today, the pre-Saturday letter, and the receipts, with the plan's reinstatement filed",
}

# =====================================================================
if __name__ == "__main__":
    for scen, num, title_line, note, start, win, win_end in [
        (build(s109_meta, s109_nodes, S109_START), 109, "The Check That Kept Coming",
         "This scenario depicts a mother whose son is in foster care receiving a repayment letter about benefit payments that continued during an administrative processing lag, told through letters, bank statements, receipts, and a case note. There is no graphic content. No benefit-program rule is stated; the letter in the story states its own instructions. Players may skip any scene or use the quick exit at any time.",
         S109_START, WIN109, "end_win"),
        (build(s110_meta, s110_nodes, S110_START), 110, "Unstable, On Paper",
         "This scenario depicts a mother at month nine of her daughter's foster-care placement whose landlord declines to renew her lease, and who doubles up with a cousin under a signed room agreement, told through letters, receipts, applications, and a review. There is no graphic content. Players may skip any scene or use the quick exit at any time.",
         S110_START, WIN110, "end_win"),
        (build(s111_meta, s111_nodes, S111_START), 111, "The Costs Column",
         "This scenario depicts a father whose son is in kinship care whose old fines-and-costs payment plan lapses on two late postings, and who misses a Saturday visit rather than drive against a clerk's letter, told through letters, receipts, a visit note, and a review. There is no graphic content. No rule about fines, costs, or driving is stated; the letters in the story state their own instructions. Players may skip any scene or use the quick exit at any time.",
         S111_START, WIN111, "end_win"),
    ]:
        assert scen["meta"]["tier"] == "Hard"
        assert scen["meta"]["startCash"] == 160
        assert 24 <= len(scen["nodes"]) <= 34, (num, len(scen["nodes"]))
        ends = [n for n in scen["nodes"] if n.get("ending")]
        assert len(ends) == 3, (num, len(ends))
        for e in ends:
            assert len(e["debrief"]) >= 3 and "choices" not in e
        ids = {n["id"] for n in scen["nodes"]}
        for n in scen["nodes"]:
            for c in n.get("choices", []):
                assert c["next"] in ids, (num, n["id"], c["next"])
                assert "removed" not in c.get("setFlags", []), (num, n["id"])
        path, cash, flags = walk(scen, win, win_end)
        pj, pm = emit(scen, num, title_line, note, start)
        print(f"Scenario {num}: nodes={len(scen['nodes'])} endings={len(ends)} "
              f"walked={len(path)} endCash={cash} flags={sorted(flags)}")
        print("  path: " + " -> ".join(path))
        print(f"  wrote {pj} and {pm}")
