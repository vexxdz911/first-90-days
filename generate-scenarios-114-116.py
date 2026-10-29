#!/usr/bin/env python3
"""Generator for Scenarios 114-116 of 'The First 90 Days' (Complex tier).
Wave 2, Batch 8, Part D. One data source emits both the .json and the
-script.md for each scenario, so they match node-for-node by construction.
Every kicker and every in-body date is computed from startDateISO +
dayOffset via datestr(); the S116 ASFA date (entry + 15 calendar months)
is computed with add_months() and asserted. The script also walks each
winning route programmatically and prints the walked path, the number
of nodes visited, and the end cash, for use in the strategy guides."""
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

def datestr(start, off):
    return fmt(start + timedelta(days=off))

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

def walk_by_path(scen, path_ids, win_ending):
    """Follow path_ids node-to-node from the start. At each node, select the
    choice whose next equals the following id; assert every flag gate on that
    choice is satisfied by flags set earlier on the walk and that cash never
    goes negative. Returns (path, end_cash)."""
    by = {n["id"]: n for n in scen["nodes"]}
    flags, cash = set(), scen["meta"]["startCash"]
    assert path_ids[0] == scen["meta"]["startNode"]
    assert path_ids[-1] == win_ending
    for i, cur in enumerate(path_ids):
        node = by[cur]
        if node.get("ending"):
            assert cur == win_ending and i == len(path_ids) - 1
            return path_ids, cash
        nxt = path_ids[i + 1]
        choice = next(c for c in node["choices"] if c["next"] == nxt)
        for r in choice.get("requiresFlags", []):
            assert r in flags, (cur, "missing required flag", r, sorted(flags))
        for r in choice.get("requiresNoFlags", []):
            assert r not in flags, (cur, "forbidden flag present", r)
        cash += choice.get("cash", 0)
        assert cash >= 0, (cur, "cash negative", cash)
        flags.update(choice.get("setFlags", []))
    raise AssertionError("path did not terminate at an ending")

# =====================================================================
# SCENARIO 114 — The Ledger
# Father Booker; daughter Thalia, 7 (placed pre-story).
# Start: Monday, January 5, 2026. Twelve weeks of compliance, priced.
# =====================================================================
S114_START = date(2026, 1, 5)
assert S114_START.strftime("%A") == "Monday"
d114 = lambda off: datestr(S114_START, off)

s114_nodes = [
N("start", 0, "Twelve Weeks, Priced", [
 "Your name is Booker. Your daughter Thalia is seven, and she has been placed with a foster family since before this story opens. Your plan is not mysterious: screens on summons, a weekly class run by the private provider the plan names, visits with Thalia, and work — the warehouse shifts that pay for all of it and compete with all of it.",
 "What nobody has priced for you is the plan itself. Two buses each way to the screen site. Shift hours surrendered, unpaid, every time a summons lands inside a shift. A fee the provider charges for its own class, because the plan names the class and the class charges a fee. Twelve weeks of doing everything asked has a cost, and the file records none of it.",
 f"A pre-review summary is being prepared for the review on {d114(91)}. It will describe your engagement in a word or two. This story is about what those words will be standing on.",
], [C("Begin the twelve weeks — screens, class, visits, shifts", "notebook_choice",
      note="Week one starts the way all twelve will: with a summons, a schedule, and arithmetic nobody else is doing.")]),

N("notebook_choice", 3, "A Notebook, Bought Cheap", [
 "At the dollar store by the bus stop you pass a wire-bound notebook, the kind with the date printed nowhere and room for everything. A dollar and change. Other parents in the waiting room keep their whole cases in folders; one man you have seen twice keeps his in a grocery bag that is coming apart at the seams.",
 "A notebook would be a record of the part of this case the file never sees: every trip, every fare, every surrendered hour, every fee — dated, with the receipt stapled beside it. It would also be one more thing to carry, keep, and keep up, on top of a plan that is already a second job.",
], [C("Buy the notebook and start it tonight — date, trip, cost, receipt", "week1_screen", cash=-4,
      setFlags=["ledgerStarted"],
      addHidden=["Ledger — notebook started; trips, fares, and fees to be logged with receipts"],
      note="Four dollars with a pen. The first page gets tonight's date and a heading in block letters: WHAT IT COSTS."),
    C("Skip it — your memory and your pay stubs will have to do", "week1_screen", cash=-4,
      note="The money goes to groceries instead. Memory, you tell yourself, is a record too. This scenario will test that sentence.")]),

N("week1_screen", 7, "Week One: Two Buses Each Way", [
 f"The first summons of the twelve weeks lands for {d114(7)}: screen at the site across the county, inside your shift. Two buses each way. You swap what you can, surrender what you cannot — two shift hours, unpaid — ride out, provide the screen, ride back, and make the tail of the shift smelling of bus.",
 "The screen itself takes minutes. The trip takes the morning. The file will record the screen. Nothing anywhere records the morning — unless the notebook does, tonight, in your hand, with the transfer stubs stapled to the page.",
], [C("Log it tonight — date, route, fare, hours surrendered, stubs stapled in", "class1", cash=-12,
      setFlags=["ledgerKept"],
      addHidden=["Ledger — week-one screen logged: two buses each way, fare and unpaid hours recorded, stubs kept"],
      note="Twelve dollars of fares, spent either way. The page takes four minutes. Both numbers go in the notebook."),
    C("Make the screen and get some sleep — the file has the result, and that is what counts", "class1", cash=-12,
      note="Twelve dollars of fares, spent either way. The result is in the file by morning. The morning itself is nowhere.")]),

N("class1", 10, "The Class the Plan Names", [
 "The parenting class meets weekly at the provider the plan names, and the provider charges a fee for it — payable at the door, in the ordinary way of doors. You pay it, you sign the sign-in sheet, you sit the two hours, you sign nothing else. The sheet goes into the provider's binder. The receipt goes into your pocket.",
 "At home the receipt can join the notebook — fee, date, class number, stapled flat — or it can live in the pocket until the pocket is washed. Paper has exactly two careers in this story, and this is the fork where they separate.",
], [C("Staple the fee receipt into the notebook beside the class date", "shift_cost", cash=-20,
      setFlags=["classLogged"],
      addHidden=["Ledger — provider class fee logged with receipt stapled beside the class date"],
      note="Twenty dollars, at the door, either way. Now it is also a page: fee, date, class one, receipt."),
    C("Pay the fee and keep the receipt in your coat for now", "shift_cost", cash=-20,
      note="Twenty dollars, at the door, either way. Coats get washed. Binders at the provider keep the sign-in sheet either way — theirs, not yours.")]),

N("shift_cost", 14, "Hours, Surrendered Unpaid", [
 "Your supervisor is not unkind about the swaps; she is arithmetic about them, the way supervisors are. Each summons inside a shift is hours she cannot pay and you cannot bill to anyone. By week two the pattern has a shape you can see from the kitchen table: the plan's appointments sit inside the workday, the workday pays for the plan's appointments, and the difference comes out of the same paycheck the plan will later examine for stability.",
 "A scored assessment form is part of cases like yours — filled in from visits, screens, and notes, rating what it can see. What it can see is attendance and results. The hours underneath them are not a line on it. They are a line in a notebook, or they are nothing.",
], [C("Keep the notebook current with this week's swaps and surrendered hours", "summary_rumor",
      note="The page does not complain. It accumulates. Accumulation, over twelve weeks, is the whole argument it will ever make.")]),

N("summary_rumor", 17, "Consistent, Provisionally", [
 "At a check-in, your worker describes your engagement the way the file currently supports: screens attended, class begun, visits kept — consistent, provisionally, is the shape of it, said in the level voice of a person reading a screen you cannot see.",
 "\u201cProvisionally\u201d is doing quiet work in that sentence. The summary that goes to the review is written later, from the whole twelve weeks, by whoever assembles it — and summaries count what the file counts. What the file counts, three weeks from now, depends on two mornings neither of you can see coming.",
], [C("Ask what the summary will be built from — sheets, logs, or impressions", "holiday_setup",
      note="\u201cThe sign-in sheets and the screen log, mostly,\u201d she says. \u201cThe record.\u201d You write the sentence down. It is the most useful sentence of the month.")]),

N("holiday_setup", 21, "A Summons on a Holiday", [
 f"The next summons arrives for {d114(22)} — a date your calendar at work has marked in red for months, because it is a holiday, and holidays at the warehouse are the good shifts. The summons does not know it is a holiday. Summonses are issued by a system that prints dates, not by a person who checks them.",
 "You arrange the swap anyway, because that is what the plan requires and what you have done every time: holiday shift surrendered, buses mapped, morning cleared. Nobody — not the worker, not the site, not the summons — says anything about the site's own holiday hours. There is no one whose job that sentence is.",
], [C("Take the buses out on the holiday morning, as summoned", "holiday_miss", cash=-12,
      note="Twelve dollars of fares and a premium shift, committed before you know what the morning holds. That is what compliance costs when it is punctual.")]),

N("holiday_miss", 22, "The Locked Door", [
 f"The site is closed. Not late, not short-staffed — closed, with a printed holiday schedule taped inside the glass that nobody sent you, announced to a parking lot of exactly one person. You stand at the locked door on {d114(22)} with your summons in your hand and your surrendered holiday shift already spent, and the screen that the file expects today does not happen, because there is no one inside to take it.",
 "The morning can still produce paper, if you make it: a photograph of the posted schedule with the date on it, a notebook page written on the bus home, a call log. Or it can produce only the file's version, which is already being written somewhere in the grammar files use: no screen recorded for this date.",
], [C("Photograph the posted holiday schedule and log the trip in the notebook on the bus home", "miss1_after", cash=0,
      setFlags=["holidayDoc"],
      addHidden=["Holiday screen — site closed for an unannounced holiday; posted schedule photographed, trip logged with fare and surrendered shift"],
      note="The photograph has a timestamp. The notebook page has the fare, the hours, and the locked door, in that order. The morning now exists twice."),
    C("Go home and call the worker on the next business day — she will sort it out", "miss1_after", cash=0,
      note="She may. Sorting it out will happen in her words, in her note, at her desk — if it happens in writing at all.")]),

N("miss1_after", 24, "Reporting a Locked Door", [
 "How a locked door enters the file depends on how it is reported. Said out loud on the phone, it is a conversation: sympathetic, plausible, and held by two memories. Written — a short dated message to the worker, with the photograph attached, saying the site was closed for the holiday and asking that the screen be re-issued — it is a document, and documents get filed.",
 "Your lawyer puts it plainly when you mention it at a check-in call. You have one because the law provides for counsel in these cases (42 Pa.C.S. \u00a7 6337). \u201cA locked door you reported in writing is a system event,\u201d he says. \u201cA locked door you mentioned is a story about a screen you missed.\u201d",
], [C("Send the written message with the photograph attached, and keep a copy in the notebook", "class_setup", cash=-3,
      setFlags=["holidayNoted"],
      addHidden=["Holiday closure — reported to the worker in writing with the posted schedule attached; copy kept"],
      note="Three dollars of printing and bus fare across the errand. The message carries its own date. The copy goes behind this week's page."),
    C("Report it by phone — she was sympathetic, and that should be enough", "class_setup", cash=-3,
      note="Three dollars across the week's errands either way. Sympathy is real. It is also, in a file, indistinguishable from its absence.")]),

N("class_setup", 28, "Week Five, Ordinary", [
 "The class runs on through the middle weeks the way classes do: sign-in sheet, two hours, receipt, bus. Your notebook, if you are keeping it, is becoming a second case file — thinner than the agency's, and about a subject the agency's never mentions. Week five's page writes itself in four lines.",
 "The provider's office posts the next session's date on the board at the end of class, and everyone copies it down. What the board cannot post is whether the session will actually be held. That information lives one week in the future, behind a door you have already learned to photograph.",
], [C("Go to the next class on the posted date, fee in hand", "class_cancel", cash=-20,
      note="Twenty dollars ready at the door, as always. The bus fare to get there is spent before the door tells you anything.")]),

N("class_cancel", 31, "Cancelled, by the Provider", [
 f"You arrive on {d114(31)} to a dark classroom and a note on the provider's own door: today's session is cancelled — an instructor matter, the note says, in the apologetic handwriting of an office that expected questions it will not be there to answer. The sign-in sheet for today does not exist, because there was nothing to sign in to.",
 "This is the second morning the system has cancelled on you while the file's clock kept counting you. Like the first, it can leave paper: the provider's cancellation note, a dated request at the front desk for written confirmation, a notebook page. Or it can leave the file's version — a gap in the sign-in column with your name beside the empty row.",
], [C("Photograph the cancellation note and ask the front desk, in writing, to confirm the cancellation", "cancel_after", cash=-6,
      setFlags=["cancelDoc"],
      addHidden=["Provider class — session cancelled by the provider; door note photographed, written confirmation requested at the desk"],
      note="Six dollars of fares for a class that did not meet. The desk takes your written request. A confirmation, when it comes, will have the provider's own name on it."),
    C("Head home — the provider knows it cancelled; that will be in their records", "cancel_after", cash=-6,
      note="Six dollars of fares either way. Their records are a binder you cannot open, in an office you cannot enter, summarized later by hands you will not see.")]),

N("cancel_after", 33, "The Confirmation, or the Gap", [
 "Days later the answer to the class morning arrives in one of two forms, depending on what you left at the desk. A written confirmation from the provider — session cancelled, date, their letterhead — is a document that can sit beside any summary ever written about you. Without it, the morning is a gap you will have to narrate, in rooms that price narration the way they price all unaccompanied accounts.",
 "Your notebook page for the day exists either way, if the notebook exists: fare spent, door photographed or described, class that did not happen. Notebooks testify only when someone files them. That appointment is still ahead of you.",
], [C("File the confirmation — or the notebook page — with this week's papers and keep going", "visits_beat",
      note="The twelve weeks do not pause for their own documentation. Screens, visits, and shifts continue underneath the paper, as they have all along.")]),

N("visits_beat", 35, "Thalia, on Saturday", [
 "Saturday's visit is the part of the twelve weeks that is not arithmetic. Thalia has lost a tooth and monetized it, by her telling, at an excellent rate. She shows you a drawing of the warehouse where you work, which in the drawing has a swimming pool, and asks whether the buses you take are the same buses or different buses. Different, mostly. She accepts this as a complete account of transportation.",
 "On the bus home you do the week's page, because the notebook's discipline is that every week gets one, including the weeks whose only entry is a visit and a drawing: date, visit kept, fare, hours. The file's version of this Saturday is a line that says the visit occurred. Yours says what it cost and what was said about the tooth. Both are records. Only one of them will be read at the review — unless someone puts the other one in its hands.",
], [C("Finish the week's page on the bus home, dated", "notebook_mid", cash=-8,
      note="Eight dollars of fares for the visit round trip. The page takes the length of the ride, which is exactly as long as it needs to be.")]),

N("notebook_mid", 38, "The Notebook, at Halfway", [
 "Halfway through the twelve weeks, the notebook — if you have kept it — holds a small, stubborn archive: screens with their buses and surrendered hours, class fees with receipts stapled flat, a locked door, a cancelled class, visits with their fares. Added up, in the column you keep at the back, the twelve weeks so far have cost more than a week's pay in fares, fees, and hours. The file's total for the same weeks is zero, because the file does not have a column for it.",
 "A halfway notebook can still become a whole one: every receipt you kept loose can be stapled in now, in date order, while the weeks are still recent enough to reconstruct honestly. Or the habit can lapse here, the way habits lapse — not by decision, but by tiredness, which this scenario declines to treat as a character flaw and insists on treating as a fork.",
], [C("Bring the notebook fully current — every kept receipt stapled in, in date order", "fee_again", cash=-3,
      setFlags=["ledgerComplete"],
      addHidden=["Ledger — brought fully current at the halfway point; all kept receipts stapled in date order"],
      note="Three dollars of staples, copies, and a new pen across the errand. The archive is now continuous: no week missing, no page reconstructed from air."),
    C("Let it rest a week — you are tired, and the file is keeping its own record anyway", "fee_again", cash=-3,
      note="The file is keeping a record. It is keeping the one where your name sits beside a locked door and an empty sign-in row, in grammar that assigns both to you.")]),

N("fee_again", 42, "The Rest of the Plan, Kept", [
 "The later weeks run on rails the early weeks laid: summons, buses, screen; class, fee, sign-in sheet; visit, fare, drawing. Your screens are attended, your classes accumulate, your supervisor's swaps become a standing arrangement she initials without comment — which is its own kind of document, and you keep a copy of that too, because by now keeping copies is simply what your hands do.",
 "Nothing in these weeks is dramatic, and that is their evidentiary value. A record of ordinary compliance, kept daily, is the hardest kind of paper to argue with. It is also, at this point, still sitting in your kitchen — while the summary that will describe these same weeks is being assembled somewhere else, from different paper.",
], [C("Keep the routine exactly as it is, and ask your lawyer what the review will actually read", "screens_routine",
      note="\u201cThe summary, first,\u201d he says. \u201cThen whatever is filed under it. In that order. Always in that order.\u201d")]),

N("screens_routine", 45, "Screens, Logged or Not", [
 "One more summons, one more morning of buses and surrendered hours, one more clean result filed by a site that records results and nothing else. The routine is so established now that its documentation feels redundant — which is precisely when documentation matters most, because summaries are written at the end, from the whole run, and a run is only as documented as its least-documented weeks.",
 "At the check-in your worker mentions, in passing, that the pre-review summary is being drafted. The word she uses for its method is the word from week three: it will be built from the sign-in sheets and the screen log. You think of two entries in those sources with your name beside them — a holiday with no screen, a class date with no signature — and of what sits beside neither.",
], [C("Ask your lawyer how a parent gets the sign-in sheets and the screen log themselves", "records_learn",
      note="\u201cThe same way you get the rest of your record,\u201d he says. \u201cYou ask for it. In writing. There is a regulation, and it is not a favor.\u201d")]),

N("records_learn", 47, "The Regulation, in Plain Words", [
 "Your lawyer writes the citation on the back of his card: 55 Pa. Code \u00a7 3130.44(d). The case record — the chronology, the sign-in sheets the agency holds copies of, the screen log — is to be released upon request. \u201cShall be released upon request,\u201d he says, \u201cis the whole sentence that matters. Your notebook says what the twelve weeks cost. Their sheets say what the twelve weeks were. The review should have to look at both, side by side — but it will only look at what is put in front of it.\u201d",
 "The request is yours to make, and making it leaves a date in the file the request is about. Not making it leaves the summary alone with the sheets it was built from — sheets whose two most important entries are absences.",
], [C("Decide this week, while the summary is still a draft", "records_fork",
      note="Drafts can still be answered. Filed summaries must be corrected, which is slower, colder work. The difference is this week.")]),

N("records_fork", 49, "Ask for the Sheets and the Log", [
 "The written request names what you need: the class sign-in sheets for the twelve weeks, the screen log with its dates, and the chronology entries about your attendance — the agency's own paper, to set beside yours. It goes in dated, copied, with the copy going into the notebook's back pocket, where by now all important copies live.",
 "Or the review can be met with the notebook alone — your word, your staples, your column of costs — against a summary built from sources you have never seen and cannot quote.",
], [C("Put the request in writing — sign-in sheets, screen log, attendance chronology — and keep a copy", "packet_arrives", cash=-6,
      setFlags=["recordsRequested"],
      addHidden=["Case record requested in writing under 55 Pa. Code \u00a7 3130.44(d) — sign-in sheets, screen log, attendance chronology"],
      note="Six dollars of copies and postage across the errand. The request is now itself a page in the file it asks about."),
    C("Meet the review with the notebook alone — it is complete, and it is yours", "no_packet", cash=-6,
      note="Six dollars across the week's errands either way. The notebook is yours. The summary was built from paper that is also, in a sense, yours — and you have never read it.")]),

N("packet_arrives", 53, "Their Paper, Beside Yours", [
 f"The packet arrives before {d114(53)} and you read it the way your lawyer taught you: against the notebook, line by line. The sign-in sheets show your signature on every class date except one — the cancelled session, where the sheet itself does not exist and the provider's confirmation, if you obtained it, explains why. The screen log shows every screen attended except one date — the holiday, where the log's entry is blank in a way that could mean anything a reader wants it to mean.",
 "Beside the notebook, the blanks have biographies: a locked door with a photographed schedule, a dark classroom with a photographed note. Beside nothing, they have only your name. The two records agree everywhere except the two mornings the system cancelled — and on those mornings, yours is the only one that was there.",
], [C("Take the packet and the notebook to your lawyer, together", "side_by_side",
      addHidden=["Agency sign-in sheets and screen log read against the parent's ledger — agreement except the two system-caused mornings"],
      note="Two records, one set of weeks. The lawyer's conference table is about to hold both of them at once, which no table has done yet.")]),

N("no_packet", 53, "What You Cannot Quote", [
 "Without their paper, you cannot quote the log's blank holiday entry or show that no sign-in sheet exists for the cancelled date — you can only say so, accurately, in your own words, about documents the room has not seen. Your notebook is complete and contemporaneous. It is also, to every reader who has never met you, one interested party's private book.",
 "The summary, meanwhile, was not written from your book. It was written from the sheets and the log. At the review, the question will be whether the summary's word for your twelve weeks can be examined against its own sources — or only against your staples.",
], [C("Take the notebook to your lawyer anyway, and prepare with what exists", "side_by_side",
      note="What exists is real. The review will now decide what real-but-unaccompanied paper is worth, against a printed summary.")]),

N("side_by_side", 57, "Side by Side, on Counsel's Table", [
 "On your lawyer's table the two records lie open together for the first time: the agency's sheets and log on the left, your notebook on the right, twelve weeks in two hands. He turns pages slowly. \u201cHere is what I see,\u201d he says. \u201cEleven weeks where they agree completely — which makes the twelfth kind of week impossible to wave away. Two mornings where the system cancelled on you, documented by you at the time, and by them\u201d — he taps the blank log entry, the missing sheet — \u201cby silence.\u201d",
 "\u201cSilence in their record, answered by paper in yours. That is an argument a review can actually hear. But hear the condition: it works only if both records are in the room, filed, before the summary hardens into the review's starting point. A notebook in a kitchen is a diary. A notebook in the record is evidence.\u201d",
], [C("Ask what filing it takes — and what waiting costs", "ledger_totals",
      note="\u201cCopies, a short covering page, and a deadline,\u201d he says. \u201cThe summary is coming first. Let me show you its sentence.\u201d")]),

N("ledger_totals", 59, "The Back Column, Totaled", [
 "Before the summary arrives, counsel asks for the number nobody else has ever asked for: the back column's total. You add it together on his conference table — fares across twelve weeks of screens, classes, and visits; the provider's fee, week after week; the surrendered hours priced at the rate the warehouse would have paid them. The total is more than a week's pay, and less than you feared, and entirely absent from every document the agency has produced about you.",
 "\u201cWe do not file the total to be pitied for it,\u201d counsel says. \u201cWe file it because a review that calls a man inconsistent should have to look at what his consistency cost. Numbers like this do not argue. They sit there, in a column, in date order, being true.\u201d The total goes on the notebook's last page, in your hand, with the receipts still stapled where they have always been.",
], [C("Ask to see the summary the moment it reaches counsel", "summary_arrives",
      note="It is already being drafted from the sheets and the log. In days it will have a word for you, and the word is already chosen.")]),

N("summary_arrives", 61, "Inconsistent", [
 f"The pre-review summary reaches your lawyer on {d114(61)}, and its sentence about you is one word long, with a small parade of support: your engagement is described as \u201cinconsistent.\u201d Underneath, the summary's own arithmetic: two missed screens or classes noted in the twelve weeks — the holiday date, with no screen recorded; the class date, with no sign-in. No mention of a locked door. No mention of a cancelled session. The summary counted the file, and the file counted absences, and the absences became a character word.",
 "It is, your lawyer says, a perfectly accurate summary of an incomplete record. That sentence is either the problem or the whole defense, depending on what gets filed beside it before the review reads it as settled.",
], [C("Ask exactly what can still be filed, and by when", "summary_read",
      note="Days, not weeks. Filing, in this system, is mostly deciding what paper will be in the room — and then getting it into the room.")]),

N("summary_read", 64, "Reading It Like a Stranger", [
 "You read the summary the way its future readers will: cold, quickly, as a stranger who knows nothing about buses, holidays, or dark classrooms. To that reader, \u201cinconsistent\u201d is not a claim to be checked; it is a description to be carried into the review and used. Every future report will quote it the way this one quoted the sheets.",
 "Your lawyer — counsel, as the law provides (42 Pa.C.S. \u00a7 6337) — reads it the other way, as a document with sources. \u201cEvery characterization in a summary is a footnote that lost its text,\u201d he says. \u201cOur job is to reattach the text: their log, their sheets, your ledger, the photographs, the confirmation — in one packet, in date order, filed before the review. Then the word has to survive its own evidence, in public.\u201d",
], [C("Decide how the answer will be filed", "assembly",
      note="The packet is an assembly job now: two records, two photographs, one confirmation, one covering page. Nothing in it argues. Everything in it is dated.")]),

N("assembly", 68, "Assemble the Packet, or Keep the Notebook", [
 "The packet, if it is filed, is unglamorous by design: your ledger pages copied in date order; the agency's sign-in sheets and screen log beside them; the holiday schedule photograph; the provider's cancellation confirmation if you hold it; and your lawyer's one-page covering letter that says only what the packet is — two records of the same twelve weeks, submitted so the review can characterize the engagement from both.",
 "The alternative is also a real choice, and parents make it for real reasons: keep the notebook at home, private, yours — a record of what this cost you, kept for yourself and Thalia someday — and let the review proceed on the agency's paper alone. Paper that never enters the record changes nothing in the record. That is not a criticism of the keeping. It is a fact about the filing.",
], [C("Assemble and file the packet with counsel — ledger, sheets, log, photographs, covering page", "packet_filed_scene", cash=-8,
      setFlags=["packetFiled"],
      addHidden=["Engagement packet filed with counsel before the review — ledger and agency sign-in sheets/screen log side by side"],
      note="Eight dollars of copies across the errand. Filed, stamped, copied back into the notebook's back pocket. The notebook is now in two places, one of which decides things."),
    C("Keep the notebook at home — it is yours, and Thalia's someday", "notebook_home_scene", cash=-8,
      note="Eight dollars across the week's errands either way. The notebook stays whole, private, and complete — in the one room the review will never enter.")]),

N("packet_filed_scene", 71, "Filed, Stamped, Copied Back", [
 "The filing takes eleven minutes at a counter and changes the geography of the case: the ledger is now where decisions are made from. Your worker, at the next check-in, mentions it without edge: \u201cI saw the packet. The holiday — I didn't know the site was closed.\u201d It is not an apology. It is something the system values almost as much: an acknowledgment, from inside it, that the paper says what it says.",
 "The summary still says \u201cinconsistent.\u201d Summaries are not rewritten by packets; they are answered by them, in a room, on a date. That date is now the only appointment that matters.",
], [C("Keep the routine — screens, class, visits — exactly as it is until the review", "work_beat",
      note="The packet is filed. The twelve weeks, meanwhile, are still a daughter's ordinary Saturdays, and you keep them.")]),

N("notebook_home_scene", 71, "The Notebook, by the Door", [
 "The notebook goes where it has always gone: by the door, under the summonses, in the geography of a kitchen that has run a case for twelve weeks. It is complete. It is dated. Its column of costs is accurate to the dollar, and its two most important pages — a locked door, a dark classroom — are written in the hand of the only person who was there.",
 "None of that is in dispute. What is in dispute, at the review, will be a summary neither of you wrote, built from sheets one of you has never seen — or, on the path where the record was requested, seen and never answered with the ledger that answers it.",
], [C("Keep the routine — screens, class, visits — exactly as it is until the review", "work_beat",
      note="Paper by the door decides nothing by the door. The review is where paper is weighed, and the review is close.")]),

N("work_beat", 75, "Week Eleven, at Work", [
 "Week eleven is logistics, which is to say it is the case: a shift rotation that threatens a class, solved with the supervisor's initials; a screen that lands outside the shift for once, and feels like a gift the system did not intend. Thalia's visit includes a spelling test report she presents with the ceremony of a state document, and you receive it with matching ceremony, because some documents deserve it.",
 "Your lawyer calls in the evening with the review's final shape: the summary will be read first; the packet, if filed, will be on the table; his job will be to put the two records side by side and let the room do the arithmetic. \u201cReviews believe documents that agree with each other,\u201d he says. \u201cOurs agree eleven weeks out of twelve, and the twelfth week is the system's, documented twice.\u201d",
], [C("Confirm the review date in writing with everyone who needs it", "work_letter",
      note="One more week where the paper and the life agree with each other — except for the two mornings that started all of this.")]),

N("work_letter", 77, "The Supervisor's Initials", [
 "The standing swap arrangement gets its own small ceremony in week eleven: your supervisor initials the schedule for the remaining weeks, in advance, in the box where initials go — converting a series of favors into a document. She does not make a speech about it. She says, \u201cSo you stop having to ask,\u201d which in supervisor language is a speech, and a kind one.",
 "The initialed schedule goes into the notebook, because by now everything that proves an arrangement goes into the notebook. It will never be an exhibit. It is something better and quieter: the reason the visits and classes of the last weeks happen at all, recorded by the only person whose initials could make them happen.",
], [C("File the initialed schedule and keep the week's visit", "thalia_visit2",
      note="Arrangements, initialed. The case runs on them, and now one of them, at least, runs on paper too.")]),

N("thalia_visit2", 79, "The Drawing, Filed at Home", [
 "Thalia's drawing of the warehouse — the one with the swimming pool — goes into the notebook's back pocket at her instruction, because in her filing system important papers live together, and by her taxonomy the drawing and the receipts are the same kind of thing: proof of where you were. She is not wrong enough to argue with.",
 "On the bus home you total the back column one more time. Twelve weeks: fares, fees, surrendered hours — a sum the file will never state, now sitting at the back of a record the review either will or will not hold. The sum is not the argument. The dates are the argument. The sum is what the dates cost, and it deserved one column, in one book, kept by the person who paid it.",
], [C("Put the notebook — and its filed copy — in order for the review", "thalia_school", cash=-6,
      note="Six dollars of fares for the visit, spent either way. The column is totaled. The weeks are in order. What remains is a room.")]),

N("thalia_school", 81, "A Spelling Test, Reported", [
 "Thalia's school sends its own summary home through the foster family, and it is the only summary in this story written by someone who watched its subject daily: reading, improved; arithmetic, willing; spelling test, presented to her father with state ceremony at the last visit and scored, by her account, at a level the school describes as excellent and she describes as inevitable.",
 "You file the school note in the notebook's back pocket, behind the drawing, where Thalia's filing system puts all documents of state. It will not be read at the review. Reviews read their own summaries. But a father keeping his daughter's spelling test in the same pocket as his receipts is, in this scenario's considered judgment, a data point — the kind no form has a line for, which is why the notebook exists.",
], [C("Go into the review's final week with the folder in order", "review_notice",
      note="School note filed, drawing filed, receipts stapled, column totaled. The review's paperwork is now a fair fight, if it is fought with paper at all.")]),

N("review_notice", 83, "The Review Approaches", [
 f"The notice confirms the review for {d114(91)}. Your lawyer's preparation is the same preparation he gives every document in this case: from the record outward. What the record holds now depends on decisions already made — a ledger kept or not, a record requested or not, a packet filed or kept by a door.",
 "\u201cThe judge will read the summary first,\u201d he says. \u201cEveryone does. Then the room will find out whether the summary is the only account of your twelve weeks, or merely the first one.\u201d Thalia's case will be measured against a plan. The plan will be measured against a record. The only question left is which record.",
], [C("Prepare with counsel, entry by entry", "counsel_checkin",
      note="Entry by entry is how the packet was built. It is also, not coincidentally, how corrections are made.")]),

N("counsel_checkin", 86, "Entry by Entry, with Counsel", [
 "Counsel's preparation takes the summary apart the way it was assembled: line by line, source by source. The attended screens: agreed by both records. The attended classes: agreed. The holiday: their log is blank, your ledger is a photograph and a dated page and a written report made the next business day, if you made it. The cancelled class: their sheets are silent, your packet holds the provider's own confirmation, if you obtained it.",
 "\u201cNotice what we are not doing,\u201d he says. \u201cWe are not asking the room to believe you instead of the file. We are asking it to read the whole file — theirs and yours, together — and characterize the engagement from all of it. Rooms can refuse many things. They have a harder time refusing their own log, read aloud, beside a photograph with a date on it.\u201d",
], [C("Spend the evening before with Thalia's drawing on the refrigerator, where it belongs", "review_eve",
      note="Preparation is done, or it is not done. Either way, tomorrow the summary meets whatever was filed beside it.")]),

N("review_eve", 89, "The Night Before the Review", [
 "The night before the review the kitchen is quiet in the particular way of houses where the important paper is already filed — or already kept at home. The notebook is in its place. Its copy, if you filed it, is in a folder with a stamp on it, in a building across town, waiting to be carried into a room by a lawyer.",
 "Tomorrow a word — \u201cinconsistent\u201d — will be weighed against twelve weeks of paper. You already know which paper you are bringing. So, in a sense, does the file.",
], [C("Take the folder, set out the morning's fare, and go to the review", "review", cash=-6,
      note="Six dollars of fare, set out tonight. Small preparations are still preparations; this whole case has run on them.")]),

N("review", 91, "The Review", [
 f"The review on {d114(91)} is orderly and brief. The plan is read line by line, and the pre-review summary's sentence is quoted in the room's level voice: engagement \u201cinconsistent,\u201d two missed items noted. The room begins, in the ordinary way, to treat the word as a fact about you.",
 "Then your lawyer asks that the characterization be made from the whole record before it is adopted. What happens next depends, with a precision this scenario has been honest about since the dollar-store notebook, on what your choices actually put on the table.",
], [C("Put the two records side by side — the ledger, the sign-in sheets, and the screen log, filed as one packet", "end_corrected",
      requiresFlags=["ledgerKept", "recordsRequested", "packetFiled"],
      note="Eleven weeks of agreement, read aloud, and two mornings documented by the only person who was there — and by the provider's own confirmation."),
    C("Produce the notebook today for the first time — kept faithfully, never filed", "end_unfiled",
      requiresFlags=["ledgerKept"], requiresNoFlags=["packetFiled"],
      note="The book is real, complete, and new to the room. New paper, offered at the last hour, is weighed the way last-hour paper always is."),
    C("Ask the room to take your word for the two mornings", "end_stands",
      note="Your word is accurate. The summary, printed and already read, is the room's starting point — and starting points are where characterizations live.")]),

N("end_corrected", 95, "Ending \u2014 Consistent, As Documented", [
 "The correction takes less time than the twelve weeks did, which is usually the way of corrections. Your lawyer walks the room through the packet in date order: the sign-in sheets and the ledger agreeing, week after week; the screen log and the ledger agreeing, screen after screen. Then the two mornings. The holiday: the log's blank entry, set beside the photographed posted schedule, your dated written report, and the fare and surrendered shift in the ledger's column. The cancelled class: the missing sheet, set beside the provider's own written confirmation that the provider cancelled the session.",
 "The court corrects the characterization on the record. Your engagement is documented as consistent, with the two system-caused exceptions noted as such — the holiday closure and the provider cancellation entered in the record as what they were, not as misses. The summary's word does not survive its own sources, read together, in public. The plan continues; Thalia's placement continues for now; the next review will start from a record that describes the father who actually ran these twelve weeks.",
], ending=True, debrief=[
 "WHAT THE RECORD HELD (the hidden record, revealed): Two records that agreed almost everywhere. The agency's sign-in sheets and screen log showed attendance at every screen and class of the twelve weeks except two dates. The parent's ledger — dates, trips, fares, surrendered hours, receipts stapled beside them — showed the same attendance, and, for the two excepted dates, the reasons: a screen site closed for a holiday nobody announced, photographed on its own posted schedule and reported in writing the next business day; a class cancelled by the provider, confirmed in the provider's own writing. Filed together as one packet before the review, the two records corrected the summary that had been built from only one of them.",
 "THE LAW UNDER THIS PATH: Only the verified instruments were used. The agency's sheets and log were obtained because the case record \u2018shall be released upon request\u2019 (55 Pa. Code \u00a7 3130.44(d)) — requesting them is what let counsel set the summary beside its own sources instead of arguing against its conclusion. Counsel (42 Pa.C.S. \u00a7 6337) presented the packet at the review and asked that the characterization be made from the whole record. Nothing here invented a right to a corrected adjective: the packet created the conditions under which the room, reading its own log beside a dated ledger, corrected the word itself. This ending is the scenario's win, labeled plainly: a characterization corrected on the record, with the two exceptions noted as system-caused. The case is not over, Thalia is still placed, and the plan continues.",
 "THE HONEST PART: The twelve weeks still cost what they cost — the fares, the fee, the surrendered holiday shift were never repaid by anyone, and the ledger's back column remains the only place that sum is written down. A different reviewer could have noted the packet and kept the word anyway; a site that announced its holidays, or a provider that reported its own cancellation, would have made the packet unnecessary. Workers, offices, and luck held pieces of this. What your choices controlled was narrower and durable: when the system cancelled on you twice, you were the only party who wrote it down at the time — and you filed what you wrote where it could be read. Outcomes in this system turn on workers, judges, and luck as much as on any parent's choices, and never on a parent's worth.",
]),
N("end_unfiled", 95, "Ending \u2014 Kept, But Never Filed", [
 "The notebook comes out of your bag at the review, and the room is polite about it in the way rooms are polite about paper they have never seen: it is examined, its staples and dates are noted, and its two most important pages are read with genuine attention — for the length of a review's attention, which is minutes, shared among every other line of a plan.",
 "The summary's word is softened in the discussion and survives in the document. Reports are not rewritten around a book produced at the table; the characterization is carried forward, now with a line noting that the father \u2018presented a personal log at the review.\u2019 The notebook goes home with you, complete as ever. The file goes everywhere else, with the word intact.",
], ending=True, debrief=[
 "WHAT THE RECORD HELD (the hidden record, revealed): A complete, contemporaneous, accurate ledger — in the wrong geography. Kept week by week with its receipts, photographs, and its column of costs, it answered both of the summary's counted misses. It was never requested against the agency's own sheets and log, and never filed beside them, so at the review it arrived as one party's private book, offered at the last hour, against a printed summary the room had already read. The discussion acknowledged it. The document did not absorb it.",
 "THE LAW UNDER THIS PATH: The missing moves were the verified ones, and neither is dramatic. The agency's sign-in sheets and screen log were available on written request \u2014 the record \u2018shall be released upon request\u2019 (55 Pa. Code \u00a7 3130.44(d)) \u2014 and counsel (42 Pa.C.S. \u00a7 6337) could have filed the two records together before the review, when filing changes what a summary is answered by. Paper that never enters the record changes nothing in the record: that is this ending, and it is this batch's recurring lesson, stated without blame. Keeping the notebook was the hard part, and it was done. Filing it was the decisive part, and it was not.",
 "THE HONEST PART: Nothing in this ending says the notebook was wasted. It is dated, checkable, and still exists — a later review, a later filing, can still put it where it belongs, and its column of costs is a true account no other document contradicts. What was lost was timing: characterizations harden by being quoted, and each report that repeats \u2018inconsistent\u2019 makes the next correction slower. A worker who had written the holiday closure into her own notes, or a provider who reported its cancellation to the agency, would have spared you all of it. The word in the file is a verdict on what was filed, not on the father who kept the book.",
]),
N("end_stands", 95, "Ending \u2014 The Summary Stands", [
 "The review adopts the summary's sentence the way reviews adopt most sentences: without heat, without doubt, as the starting point for the next twelve weeks. Engagement: inconsistent. Two missed items, noted. The plan continues with the word attached to it, and the word will be quoted by the next summary, and the next, the way file language reproduces — faithfully, and without ever re-meeting the mornings it describes.",
 "Your account of the locked door and the dark classroom was heard in the room, in your voice, in order. It was believed the way unaccompanied accounts are believed: personally, and set aside professionally. The buses, the holiday shift, the fee at the door — the price of the twelve weeks — remains recorded nowhere except your memory, which was always the archive this ending was going to have.",
], ending=True, debrief=[
 "WHAT THE RECORD HELD (the hidden record, revealed): One record only. The sign-in sheets and the screen log, as summarized: attendance everywhere except a holiday with no screen recorded and a class date with no signature, characterized in one word \u2014 \u2018inconsistent\u2019 \u2014 with no entry anywhere explaining either absence. The two mornings the system cancelled were present in the file only as gaps with the father's name beside them, and gaps, in summaries, are read in the direction the grammar points: toward the parent.",
 "THE LAW UNDER THIS PATH: Every instrument that would have answered the word existed and is verified. A contemporaneous ledger would have dated the costs and the cancellations as they happened. The agency's own sheets and log were available on written request (55 Pa. Code \u00a7 3130.44(d)), to be set beside their summary. Counsel (42 Pa.C.S. \u00a7 6337) can assemble and file whatever paper exists \u2014 and cannot manufacture, at the review, a photograph from a holiday morning two months past. Defaults rule wherever documentation does not. That sentence, not any fact about this father, is this ending.",
 "THE HONEST PART: Be clear, because the summary was not: you attended every screen the site was open for and every class the provider held. The two \u2018misses\u2019 were a locked door and a cancelled session, and the twelve weeks cost you fares, fees, and a premium holiday shift that no document repaid or recorded. A caseworker who wrote the closure into her own note, a provider who reported its cancellation, a reviewer who asked what the blanks meant — any of them changes this ending without you changing anything. It records the state of a file, not the engagement of a father. And the notebook can still be started tonight: paper begun late is worth less than paper begun on time, and infinitely more than the next summary's word, unanswered again.",
]),
]

s114_meta = {"title": "The First 90 Days",
 "subtitle": "Scenario 114 \u2014 The Ledger (a fictional composite)",
 "startDateISO": "2026-01-05", "startNode": "start", "startCash": 170,
 "tier": "Complex",
 "summary": "Twelve weeks of Booker's compliance have a price the file never records \u2014 until his notebook, the sign-in sheets, and the screen log are put side by side against a summary that calls him \u2018inconsistent.\u2019"}

s114 = build(s114_meta, s114_nodes, S114_START)

S114_WIN_PATH = ["start","notebook_choice","week1_screen","class1","shift_cost",
 "summary_rumor","holiday_setup","holiday_miss","miss1_after","class_setup",
 "class_cancel","cancel_after","visits_beat","notebook_mid","fee_again",
 "screens_routine","records_learn","records_fork","packet_arrives","side_by_side",
 "ledger_totals","summary_arrives","summary_read","assembly","packet_filed_scene","work_beat",
 "work_letter","thalia_visit2","thalia_school","review_notice","counsel_checkin","review_eve","review",
 "end_corrected"]

# =====================================================================
# SCENARIO 115 — Three Letters, Three Addresses
# Mother Shana; twins Ramon and Opal, 5 (placed pre-story).
# Start: Monday, February 2, 2026. Three letters, three wrong places.
# No program rule is stated as law: each letter states its own process
# on its face, and the story turns on addresses, lags, and paper.
# =====================================================================
S115_START = date(2026, 2, 2)
assert S115_START.strftime("%A") == "Monday"
d115 = lambda off: datestr(S115_START, off)

s115_nodes = [
N("start", 0, "Between Addresses", [
 "Your name is Shana. Your twins, Ramon and Opal, are five, and they have been placed with a foster family since before this story opens. When they were placed, you were between addresses — a phrase that sounds temporary in a sentence and is enormous in a life: an apartment you were leaving, a shelter you stayed in briefly, and then, finally, the rooms you live in now.",
 "Systems do not send letters to phrases. They send them to addresses — the ones in their files, in the order they were given them, at the speed their mail moves. In the weeks after the twins were placed, three letters left three different systems for you. None of them reached the rooms you live in now.",
 "You do not know that yet. What you know is that you did the one thing you were told to do on the day everything moved: you told the agency your new address, on their form, in your own handwriting. This story is about where that form went — and where the letters went instead.",
], [C("Start with the form — the one thing you know you did", "update_form",
      note="One form, correctly filled in, in a season when almost nothing else stayed still. Remember it. The file does.")]),

N("update_form", 3, "The Update Form", [
 f"On {d115(3)}, in the agency office, you filled in the address-update form the worker handed you: your new address, written carefully, number by number, in the handwriting your school reports used to call neat. The worker took it, said it would be updated, and the visit moved on to other paper.",
 "The form itself can live in two places from this day forward: in the agency's file, where it belongs — and in your folder, as a copy, if you asked for one at the desk. Copies asked for in the moment cost nothing but the asking. Copies reconstructed later cost exactly the difference between a document and a memory.",
], [C("Ask at the desk for a copy of the form you just signed, and put it in your folder", "new_address", cash=-2,
      setFlags=["updateCopy"],
      addHidden=["Address update — mother's own copy of her correctly completed update form kept"],
      note="Two dollars of copies across the day's errands. The copy shows your new address, in your hand, with the date on it. Keep it flat."),
    C("Leave it with the worker — the agency has it, and that is what forms are for", "new_address", cash=-2,
      note="Two dollars across the day's errands either way. The agency does have it. Having a thing and finding a thing, in a large file, are different events.")]),

N("new_address", 6, "The Rooms You Live in Now", [
 "The new address is two rooms and a kitchen you keep cleaner than the twins' visits require, because clean is a language you are fluent in and intend to be quoted in. Mail reaches you here — the ordinary kind, from the ordinary world. Your folder lives in a drawer. Your visits with Ramon and Opal are the fixed stars of the week, and they are kept.",
 "What you cannot see, from inside the rooms, is the view from the three systems' files: in each of them, your address is a line of text, entered by a person, at a moment, from a source — and those three lines do not agree with each other, or with the form in your drawer. Letters are about to demonstrate this, one closure at a time.",
], [C("Go on with the weeks — visits, work, the folder in the drawer", "landlord_note",
      note="The first letter has already been mailed. It is not coming here. You will learn about it the way parents learn about most mail in this system: from its consequences.")]),

N("landlord_note", 8, "The Tenancy Page", [
 "For the folder, because folders in this story are built before they are needed: the tenancy page for the rooms, with its start date and your name spelled the way your name is spelled, and the first utility letter, addressed to you at the rooms, in an envelope that arrived. Ordinary paper, unremarkable in every way except one — every line of it agrees with the update form in your drawer.",
 "You file both without knowing why, the way people in this system learn to file everything: because paper that agrees with other paper is the only kind of argument that has ever worked on anyone, and someday a room may need to be shown where you live by something other than your saying so.",
], [C("Go on with the weeks — the folder one page thicker", "childcare_news",
      note="Two pages that prove an address. In a story about addresses, that is not a small thing to own early.")]),

N("childcare_news", 9, "The First Closure", [
 "The childcare arrangement the twins used — the one the plan counted on for the hours around your shifts — is closed, you learn at a check-in, in a sentence delivered as housekeeping: the slot was released after a letter went unanswered. The letter, the worker says, was mailed weeks ago. It asked you to confirm the arrangement by a date printed on its face, and its face also stated — as these letters do — the office to contact and the steps to ask for the decision to be looked at again.",
 "It was mailed to the old apartment. The one you had already left when you filled in the update form. You never saw it, never confirmed anything, and never failed to answer anything except a letter that was delivered to an empty room and a forwarding sticker nobody can now produce.",
], [C("Ask which address the letter was sent to — and write the answer down, dated", "childcare_reply",
      addHidden=["Childcare closure — letter mailed to the prior apartment after the address update; mother never received it"],
      note="The answer is given readily, because nobody thinks it is the important part. It is the whole part. You write it down with today's date beside it.")]),

N("childcare_reply", 12, "A Trail for the First Letter", [
 "The childcare office's letter stated its own process on its face, and processes stated on letters can be followed in writing: a dated letter to that office, saying the closure letter was mailed to an address you had left before it was sent, that you never received it, and asking — in the letter's own stated terms — for the decision to be looked at again, with your current address at the top in large, careful numbers.",
 "Or the matter can be carried by phone, where it will be noted, perhaps, in someone else's words, at someone else's length. Three letters went wrong in this story. Each one will need its own trail. Trails are made of dated paper or they are made of recollection, and the two kinds are priced differently in every room that matters.",
], [C("Write to the childcare office — closure letter's own process, your current address at the top", "benefits_news", cash=-4,
      setFlags=["childcareTrail"],
      addHidden=["Childcare thread — written request to re-look at the closure, tracing the letter to the prior apartment, current address stated"],
      note="Four dollars of copies and postage. The letter keeps its own date. Trail one exists now, in writing, addressed correctly — which is more than the original managed."),
    C("Call the office and explain — they were reasonable on the phone before", "benefits_news", cash=-4,
      note="Four dollars across the week's errands either way. Reasonable people, a clear explanation, and no dated page anywhere that either happened.")]),

N("benefits_news", 15, "The Second Closure", [
 "The second system announces itself the way the first did: as a fact you are told, not a letter you are holding. Your benefits case has been closed, the check-in version says, after a notice went unanswered — a notice asking you to confirm your circumstances by a date printed on its face, with the face also stating the office to contact and how to ask for the case to be looked at again.",
 "This one was mailed to the shelter. You had already left the shelter when you filled in the update form — left it, in fact, before the notice was even printed. An empty bed in a building you no longer lived in received your deadline, kept it for the required number of days, and returned it to a file that recorded the silence as yours.",
], [C("Ask which address the notice was sent to — and add it to your dated list", "benefits_reply",
      addHidden=["Benefits closure — notice mailed to the shelter after the mother had left it; never received"],
      note="Two closures, two addresses, neither of them yours anymore. A pattern is a thing with an address list. Yours now has two entries, dated, in your hand.")]),

N("benefits_reply", 18, "A Trail for the Second Letter", [
 "The benefits notice, like the childcare letter, stated its own process on its face. Following it means the same unglamorous move in a second envelope: a dated letter to the office the notice names, saying the notice was mailed to a shelter you had left before it was sent, that it never reached you, and asking in the notice's own stated terms for the case to be looked at again — current address at the top, again, in the careful numbers.",
 "Two trails is more work than one trail, and this scenario does not pretend otherwise. It only notes that the systems are separate, their files are separate, their letters were separate — and a fix in one file has never once, in the history of files, repaired another.",
], [C("Write to the benefits office — the notice's own process, current address at the top", "housing_news", cash=-4,
      setFlags=["benefitsTrail"],
      addHidden=["Benefits thread — written request to re-look at the closure, tracing the notice to the former shelter, current address stated"],
      note="Four dollars of copies and postage. Trail two exists. Two systems have now been told, in writing, where you actually live."),
    C("Handle this one by phone — two written trails is a lot of paper for one week", "housing_news", cash=-4,
      note="It is a lot of paper. The phone call is kind and quick and leaves, at the end of it, exactly the evidence the first phone call left: none that you can hold.")]),

N("housing_news", 21, "The Briefing You Never Got", [
 "The third system does not announce a closure. It announces a character fact. At the check-in, the housing-briefing invitation is mentioned in the past tense and the passive voice: a briefing was held, invitations were mailed, and the file records that the family \u2014 you \u2014 \u2018failed to attend.\u2019 The briefing mattered: it was a step in a process whose later steps assume you took it.",
 "You were not absent from a briefing you knew about. You were absent from an invitation you never received. But absences, in files, do not come in those two kinds. They come in one line, and the line is already written.",
], [C("Ask the only question left: which address was the invitation mailed to?", "housing_reply",
      note="The worker checks. The answer takes longer this time, because this address is not your old one, and it is not the shelter's. It is a third thing, and nobody in the room has seen it before.")]),

N("housing_reply", 24, "An Address You Never Lived At", [
 "The invitation was mailed to an address you have never lived at. It resembles yours the way a reflection resembles a face: the street is right, the name is right, and the number is transposed — two digits exchanged, the oldest clerical error in the world, sitting in a file as if it were a fact about geography. You did not write that number. You have never written that number. On your update form, the number is correct.",
 "Of the three letters, this is the one that cannot be answered by persistence alone, because its error is invisible from outside the file. From outside, the invitation was mailed, the briefing was held, and the family failed to attend. From inside — from the file's own pages, the update form and the mailing record laid side by side — the error explains itself. Getting inside is a procedure, and it has a citation.",
], [C("Take the three addresses home and lay them out on the kitchen table", "three_threads",
      addHidden=["Housing briefing — invitation mailed to a transposed-number address the mother never lived at; file records \u2018failed to attend\u2019"],
      note="Three letters. Three addresses. None of them the rooms you live in. The kitchen table now holds the whole case, in one line each.")]),

N("three_threads", 27, "Three Threads, on the Table", [
 "Laid out, the three threads are almost elegant in their wrongness. A childcare letter to the apartment you had left. A benefits notice to the shelter you had left. A briefing invitation to an address that has never existed in your life at all. Three systems, three files, three lines of text — and underneath all three, one form, correctly written, dated before any of the letters were mailed.",
 "Your lawyer lays it out the way lawyers do, by separating what each thread needs. You have one because the law provides for counsel in these cases (42 Pa.C.S. \u00a7 6337). \u201cEach letter stated its own process,\u201d she says. \u201cThose trails are yours to walk, office by office. But the sentence in the dependency file \u2014 \u2018failed to attend\u2019 \u2014 will not be corrected by any of those offices. It will be corrected, if at all, by the agency's own file, read against itself. For that, we need the file.\u201d",
], [C("Ask how a parent gets the file — the update form and the mailing record, in the agency's own pages", "records_learn",
      note="\u201cIn writing,\u201d she says. \u201cThere is a regulation for exactly this, and it does not ask anyone's permission.\u201d")]),

N("records_learn", 30, "Shall Be Released", [
 "The citation goes on the back of her card: 55 Pa. Code \u00a7 3130.44(d). The case record is to be released upon request \u2014 and your case record, if it is complete, contains the two pages this whole story turns on: your address-update form, as filed, and the agency's own mailing record, showing which addresses its letters were actually sent to, and when.",
 "\u201cIf the form in their file is the form you signed,\u201d your lawyer says, \u201cit is dated before all three mailings, and it is correct. Then the file corrects itself, in its own handwriting. If we never request it, the file keeps only its conclusions: two closures for failure to respond, one briefing failed to attend. Conclusions are what reviews read.\u201d",
], [C("Decide this week — the review will read the file as it stands", "records_fork",
      note="The trails to the two offices are walks you can take any week. The file is the ground all three walks are judged on. Ground first.")]),

N("records_fork", 33, "Ask for the File", [
 "The written request names the pages: the address-update form as filed, the mailing record for the three letters, and the entries recording the closures and the briefing notation. It goes in dated and copied, with the copy filed in your drawer beside — if you kept it — your own copy of the form itself, the two copies about to become the most important pair of pages in the case.",
 "Or the three trails can be walked on your word alone, office by office, each office deciding how much of a pattern it can see from its own one letter — which is to say, none of it.",
], [C("Put the request in writing — update form, mailing record, closure and briefing entries — and keep a copy", "file_arrives", cash=-6,
      setFlags=["recordsRequested"],
      addHidden=["Case record requested in writing under 55 Pa. Code \u00a7 3130.44(d) — update form and mailing record named"],
      note="Six dollars of copies and postage. The request is dated, and it names the pages. Naming pages is how requests become evidence."),
    C("Walk the three trails on your word — the offices know you, and you can explain", "no_file", cash=-6,
      note="Six dollars across the week's errands either way. Your word is accurate in every office. Accuracy, unaccompanied, is priced in this system at a rate you are about to learn.")]),

N("file_arrives", 37, "The File, Against Itself", [
 f"The packet arrives, and your lawyer spreads its two decisive pages on the table on {d115(37)} with the care of a person laying out cards she did not deal. Page one: your address-update form — your new address, correct in every digit, in your own handwriting, dated {d115(3)}, before any of the three letters was mailed. Page two: the agency's mailing record — the childcare letter to the old apartment; the benefits notice to the shelter; the briefing invitation to the transposed number. Three mailings, all after the form, none to the address on it.",
 "Nobody in the file made any of this up, and nobody hid any of it. It was all there, in order, waiting for a reader who would put page one beside page two. Files do not read themselves. That is the entire tragedy and the entire opportunity of this scenario, in one sentence.",
], [C("Copy the two pages into your packet, in that order — form first, mailing record second", "untangle",
      setFlags=["updateFormFound"],
      addHidden=["Agency file — update form correctly written and dated before all three mailings; mailing record shows all three letters sent elsewhere"],
      note="Form first, mailing record second. Order is the argument: the correct address existed in the file before a single letter went wrong.")]),

N("no_file", 37, "Conclusions, Unaccompanied", [
 "Without the file, the three threads stand exactly as their conclusions left them: a childcare closure for failure to respond, a benefits closure for failure to respond, a briefing failed to attend. You know the update form exists and what it says. Knowing a document's contents, in this system, is the memory of a document — and memories are admitted everywhere except where decisions are made.",
 "The trails can still be walked. Each office can still be written to, in its letter's own stated process, tracing its letter to its wrong address. What cannot be built without the agency's pages is the pattern — the single dated form underneath all three errors — and patterns are what corrections are made from.",
], [C("Walk the trails with what you have — your dated list, your copies, your word", "untangle",
      note="What you have is true. The review will now price the difference between true and documented, which is the tuition this whole scenario charges.")]),

N("untangle", 41, "Which Letter Went Where", [
 "Untangling, done properly, is clerical work, and your lawyer insists on doing it clerically: a single page, three rows. Row one: childcare letter, mailed to the prior apartment, after the update; office written to, in its own stated process, on its trail. Row two: benefits notice, mailed to the former shelter, after the update; office written to. Row three: briefing invitation, mailed to the transposed number, after the update; notation in the dependency file reading \u2018failed to attend.\u2019",
 "Three rows, three addresses, one form underneath them all. The page does not accuse anyone of anything. It does something more dangerous to a file's conclusions: it makes them checkable.",
], [C("Build the three-row page with counsel, in date order, addresses exact", "mail_log_detail",
      note="Addresses exact — including the wrong one, digit for digit, because the wrong digits are the evidence in row three.")]),

N("mail_log_detail", 44, "The Transposed Digits", [
 "Row three gets its own slow minute. The mailing record's address and the update form's address, side by side: same street, same name, two digits exchanged. It is the kind of error that survives every proofread because it looks correct at reading speed, and it is visible only in exactly this posture — the file's own two pages, adjacent, read slowly, by someone looking for it.",
 "\u201cThis is why we requested the record,\u201d your lawyer says. \u201cNot to catch anyone. To make the file testify against its own conclusion. A notation that says \u2018failed to attend,\u2019 attached to an invitation the file itself mailed to a place you never lived — that notation cannot survive its own paperwork, if the paperwork is put in front of the room that owns the notation.\u201d",
], [C("Turn to the three trails — each office, each letter, each process", "trail_childcare",
      note="The pattern page is built. Now each thread still needs its own walk, because systems are repaired one file at a time.")]),

N("trail_childcare", 47, "Trail One: The Childcare Office", [
 "The childcare office's answer comes in the terms its own letter set: the closure is looked at again, on the paper. What the trail gives the office is a checkable story — the closure letter's mailing address against your update's date — and offices, like reviews, believe documents that agree with each other. The slot question is now a question about the office's own mail, and offices answer those questions differently from questions about parents.",
 "Whatever the office decides, its decision will be in writing, and the writing will either trace the letter correctly or it will not — and either way, the trail itself is now part of the record the review will read. That transformation, from a closure to a correspondence, is the trail's real product.",
], [C("File the office's reply with the three-row page, and turn to the second trail", "trail_benefits", cash=-3,
      note="Three dollars of copies. Trail one's paper joins the packet. Two threads remain, in two other buildings, in two other files.")]),

N("trail_benefits", 50, "Trail Two: The Benefits Office", [
 "The benefits office answers in its own stated process as well, and its reply turns on the same clerical pivot: the notice's mailing address — a shelter you had left — against the date you left it and the date of your update. A notice sent to a vacated bed is not a notice declined; it is a notice undelivered, and the office's own paper, once the trail puts the dates in front of it, says so in its own order.",
 "By now the packet has a rhythm: pattern page, then trails, each trail a small correspondence with dates at both ends. It is not fast, and it is not dramatic, and it is the only machinery in this story that has ever corrected anything.",
], [C("File the second reply, and turn to the hardest thread — the notation itself", "trail_housing", cash=-3,
      note="Three dollars of copies. Two trails walked. The third thread is not an office's file. It is the dependency file's own sentence about you.")]),

N("trail_housing", 53, "Trail Three: The Notation", [
 "The third thread is different in kind, and the scenario has saved it for last on purpose. The childcare and benefits closures live in other systems' files, and those systems can restore what they closed, in their own processes. The briefing notation — \u2018family failed to attend\u2019 — lives in the dependency file, the file the review reads, the file that will describe you to every future reader of this case. Correcting it requires the dependency system to correct itself, on its own pages: the update form and the mailing record, filed where the notation lives.",
 "And even a full correction has an honest limit your lawyer states now, before any review does: a corrected notation restores the record. It does not rewind the calendar. The briefing was held on its date, without you, and the steps that were to follow it have their own queue, which a correction can rejoin but cannot backdate.",
], [C("Ask counsel to lay out the filing decision — the packet, whole, or in pieces", "assembly",
      note="\u201cWhole,\u201d she says, \u201cor it is three anecdotes looking for a pattern. The pattern is the filing. Decide how it goes in.\u201d")]),

N("assembly", 57, "Assemble the Packet, Raise It Aloud, or Wait", [
 "Three ways, laid out on the kitchen table with the packet between them. One: assemble the whole packet — the three-row page, your update copy if you kept it, the agency's update form and mailing record, and the two offices' trail replies — and file it, in writing, with the agency and for the review, asking that the \u2018failed to attend\u2019 notation be corrected on the record. Two: raise the three letters orally at the review — your voice, counsel's voice, a transcript of a pattern and no exhibits beneath it. Three: wait, walk the trails as they come, and trust that each office's fix will somehow travel into the dependency file on its own. It will not, but waiting is a choice parents make for real reasons, and this scenario records it without contempt.",
 "The packet, if it is filed, must be filed whole. Filed in pieces, it is three small stories. Filed whole, it is one file correcting itself.",
], [C("Assemble and file the whole packet with counsel — pattern page, forms, mailing record, trail replies", "filed_scene", cash=-8,
      setFlags=["packetFiled"], requiresFlags=["recordsRequested", "updateFormFound"],
      addHidden=["Three-letters packet filed with counsel — update form and mailing record filed where the \u2018failed to attend\u2019 notation lives"],
      note="Filed, stamped, copied. The notation now has company in its own file: the form and the mailing record that refute it."),
    C("Raise the three letters orally at the review instead", "oral_scene",
      setFlags=["oralRaised"],
      note="Your voice and counsel's, in full sentences, on a transcript. The exhibits stay in the drawer, in date order, unfiled."),
    C("Wait — let each office's process finish on its own schedule", "wait_scene",
      note="Three processes, three schedules, no filing. The dependency file keeps its sentence, undisturbed, while the others deliberate.")]),

N("filed_scene", 60, "Filed, Where the Notation Lives", [
 "The packet goes in with a stamp and a copy for the drawer, and the ordinary anticlimax of decisive paper: a counter, a receipt, a file that is now heavier by exactly the pages that matter. Your worker, at the next check-in, mentions it in the new tone she has used since the trails began: \u201cI saw the mailing record. I had not seen the form beside it before.\u201d It is not an apology. It is the sound a file makes when it starts correcting itself — one reader at a time, in advance of the room.",
 "The two offices' processes continue on their own tracks, with their replies already in the packet. The notation awaits the review. Between here and there, the twins have visits, and a spelling curriculum Ramon intends to supervise personally.",
], [C("Keep the visits and the weeks exactly as they are until the review", "ordinary_weeks",
      note="The packet is filed. The case, meanwhile, is still two five-year-olds' ordinary weeks, and you keep them.")]),

N("oral_scene", 60, "Saved for the Review", [
 "The decision is made and noted in counsel's file: the three letters will be raised orally at the review. The packet stays assembled in your drawer, its rows in order, its forms unfiled. \u201cWe will say it clearly,\u201d your lawyer says. \u201cUnderstand what clearly buys in a system that corrects itself from paper. It buys a transcript. Transcripts are read later, if anyone asks. Filed exhibits are read now, by the room that owns the notation.\u201d",
 "You keep the visits, the weeks, the trails' replies as they arrive. Your half of every file stays accurate. The dependency file's sentence stays exactly where it was written, with a speech scheduled to answer it.",
], [C("Prepare the oral account with counsel, address by address", "ordinary_weeks",
      note="If the record will hold only words, the words will at least be exact — three letters, three addresses, one form, in that order.")]),

N("wait_scene", 60, "Three Schedules, No Filing", [
 "The decision is made and noted: wait. Each office's process is genuinely moving, in its own building, at its own speed, and it is not irrational to believe their corrections will accumulate into the truth somewhere. Your lawyer does not argue; she has given her advice, and she writes yours down beside it, because that too is what lawyers are for.",
 "\u201cOne thing, then,\u201d she says. \u201cThe dependency file does not subscribe to the other offices' mail. Whatever they restore, they restore in their files. Ours keeps its sentence until somebody files the pages that answer it. At the review, remember that we chose the sentence's company.\u201d",
], [C("Keep the weeks, and let the three processes run", "ordinary_weeks",
      note="Processes run. Files wait. The review is where the two facts will meet, and it is not far now.")]),

N("ordinary_weeks", 64, "Visits, in the Present Tense", [
 "The weeks before the review are the twins' weeks, and the scenario insists on spending one scene inside them: Ramon has appointed himself the household's spelling authority and corrects Opal's name on her drawing to a version with more letters, on principle. Opal appeals to you. You rule for the original spelling, citing the birth certificates, which is the only ruling in this story delivered with full authority and no paperwork.",
 "Underneath the ordinary weeks, the three threads sit in their three postures: two offices mid-process, one notation mid-file. The review will not ask about the spelling. It will ask, in its own way, about attendance, response, and reliability — the file's three favorite subjects, all three of which are, in your file, mailing errors wearing your name.",
], [C("Write the visit up in your folder that night, dated — as always", "twins_visit_mid",
      note="Contemporaneous, as ever. The folder's habit no longer feels like a habit. It feels like the case's other language.")]),

N("twins_visit_mid", 66, "Opal's Appeal, Heard and Decided", [
 "A second visit scene, because the weeks between a filing and a hearing are still a childhood: Opal, having reviewed Ramon's expanded spelling of her name, files a formal objection with the highest authority available, who is you, at the kitchen table, during a visit that also includes a dispute about a crayon both twins describe as legally theirs. You hear the appeal, review the evidence, and rule that names stay as they are spelled on the documents — a ruling both parties accept with the grace of litigants who have a snack pending.",
 "You write it up that night because you write everything up now. It will never be an exhibit. It is, like the spelling ruling itself, a small proof that in at least one jurisdiction in this story, decisions are made from the documents, by a reader who was actually there.",
], [C("Assemble the last folder pages counsel asked for — proof of the rooms themselves", "address_proof",
      note="One jurisdiction in this story already rules from documents. The hearing, in a few days, will show whether it is the only one.")]),

N("address_proof", 67, "Proof of the Rooms", [
 "One more page joins the folder, at counsel's suggestion, because the review may ask the plainest question in the case — where do you actually live, and since when? The answer is paper you already have or can get in one errand: the tenancy page with its start date, the utility letter in your name at the rooms, the school correspondence addressed to you where the twins' visits end. Assembled, they say what your update form said on its first day: the rooms are real, the address is the address, and it has been the address since before any letter went anywhere.",
 "It is a strange experience, proving your own address to a file that mailed your life to three other places. Counsel shrugs at the strangeness. \u201cFiles believe paper,\u201d she says. \u201cSo we bring paper. Even paper about where you sleep.\u201d",
], [C("Assemble the address pages into the folder, in date order", "summary_arrives", cash=-4,
      note="Four dollars of copies. The folder now proves the one fact every other page depends on: where you live, and since when.")]),

N("summary_arrives", 70, "Failed to Attend, in the Summary", [
 f"The pre-review summary reaches counsel on {d115(70)}, and the phrase travels exactly as file phrases travel: the briefing line appears as \u2018family failed to attend,\u2019 now promoted from a notation into a summary — the version the review will read first. The two closures appear in their own summary grammar: arrangements \u2018released after no response,\u2019 case \u2018closed after no response.\u2019 Three mailing errors, wearing the grammar of a mother's reliability.",
 "Read cold, as the review will read it, the summary describes a parent who does not answer letters and does not attend briefings. Read with the packet, it describes a mail system. Which reading happens in the room is now a question about one thing only: what is filed in front of the readers when they read.",
], [C("Ask counsel what the review can actually correct — and what it cannot give back", "counsel_second",
      note="\u201cIt can correct its own file,\u201d she says. \u201cIt can order the notation fixed and the record straight. The months are a different currency. We'll get to that honestly, in the room.\u201d")]),

N("counsel_second", 72, "What a Correction Can and Cannot Do", [
 "Counsel's second-to-last meeting is the honest one, and she schedules it on purpose before the hearing, so that no one walks into the room carrying a hope the room cannot hold. \u201cA correction can fix the notation,\u201d she says. \u201cIt can put two systems' closures back into their processes, on their trails' paper. It can restore your housing position to where you would have stood. It cannot mail a letter backwards in time. The briefing will be re-set, not un-missed. Anyone who promises you the months back is selling you a calendar that does not exist.\u201d",
 "\u201cThen the win is smaller than the loss,\u201d you say. \u201cThe win is the truth, in the file, with your position restored. In this system,\u201d she says, \u201cthat is not the small version of anything. That is the whole available version, and we are going to get all of it that paper can get.\u201d",
], [C("Prepare for the hearing with the honest version in mind", "review_notice",
      note="Truth in the file, position restored, months gone. Carrying exactly that — no more, no less — is what preparation means this week.")]),

N("review_notice", 73, "The Review Approaches", [
 f"The notice confirms the hearing for {d115(78)}. Counsel's preparation runs from the file outward, the way all her preparation runs: what the file holds depends on decisions already made — a record requested or not, a packet filed or saved for a speech, trails walked in writing or carried by phone.",
 "\u201cThe room owns the notation,\u201d she says. \u201cThat is the good news buried in this whole tangle. We are not asking strangers to fix their files — though two of them are doing it. We are asking this room to fix its own sentence, using its own pages. Rooms do that, when the pages are in front of them. When they aren't, rooms read summaries.\u201d",
], [C("Prepare with counsel, letter by letter", "review_prep",
      note="Letter by letter is how the packet was built. It is also, not coincidentally, how corrections are made.")]),

N("review_prep", 76, "Letter by Letter, with Counsel", [
 "Preparation takes the summary apart the way it was assembled: line by line, address by address. The childcare closure: the office's trail reply, tracing its letter to the apartment you had left. The benefits closure: the same, to the shelter. The briefing: the agency's own update form — your handwriting, the correct number, the date before all three mailings — beside the agency's own mailing record, with the transposed digits sitting in row three like a confession nobody had to extract.",
 "\u201cNotice what we never argue,\u201d counsel says. \u201cWe never argue you are reliable. We show the room its own mail. Reliability is the conclusion the room will draw, or not, from its own paper. Conclusions rooms draw themselves are the only ones that get written into summaries.\u201d",
], [C("Spend the evening before with the twins' drawings on the refrigerator", "eve115",
      note="Preparation is done, or it is not done. Either way, tomorrow the notation meets whatever was filed beside it.")]),

N("eve115", 77, "The Night Before", [
 "The night before the hearing the rooms are quiet in the way of rooms where the important paper is already filed — or already assembled in a drawer, waiting for a voice to carry it. Your folder is by the door. Its filed copy, if there is one, is in a building across town, in the file that contains the sentence \u2018failed to attend,\u2019 keeping it company overnight.",
 "Tomorrow three systems' mail will be weighed in one room. You already know which paper you are bringing. So, in a sense, does the file.",
], [C("Take the folder, set out the morning's fare, and go to the hearing", "review", cash=-6,
      note="Six dollars of fare, set out tonight. In this case, even the fare was always addressed correctly. It is the letters that weren't.")]),

N("review", 78, "The Hearing", [
 f"The hearing on {d115(78)} is orderly and brief. The summary is read first, in the room's level voice: two closures after no response; a briefing the family failed to attend. The room begins, in the ordinary way, to treat the three lines as facts about the mother in the chair.",
 "Then counsel asks that the file be read against itself before its conclusions are adopted. What happens next depends, with a precision this scenario has been honest about since the first unanswered letter, on what your choices actually put in the room's hands.",
], [C("Put the agency's own pages before the room — the update form dated before all three mailings, beside the mailing record", "end_restored_partial",
      requiresFlags=["recordsRequested", "packetFiled"],
      note="Form first, mailing record second. The room does the arithmetic itself, out loud, which is where arithmetic changes a record."),
    C("Raise the three letters orally — counsel states the pattern, address by address, from the transcript", "end_partial_notation",
      requiresFlags=["oralRaised"],
      note="Three letters, three addresses, one form — said clearly, in full sentences, with the exhibits in a drawer across town."),
    C("Present the file pages you obtained, without a filed packet — the form and the mailing record, produced today", "end_one_restored",
      requiresFlags=["recordsRequested"], requiresNoFlags=["packetFiled", "oralRaised"],
      note="The pages are real and they are the agency's own. Produced at the table, unfiled, they will correct what a single hearing can correct from the table."),
    C("Ask the room to take your word for where the letters went", "end_closed",
      requiresNoFlags=["packetFiled", "oralRaised", "recordsRequested"],
      note="Your word is accurate in every particular. The summary, printed and already read, is the room's starting point — and starting points are where conclusions live.")]),

N("end_restored_partial", 82, "Ending \u2014 Corrected on the Record, Restored in Part", [
 "The correction happens in the file's own language, which is the only language corrections last in. The room reads the update form — your handwriting, the correct address, the date before all three mailings — beside the mailing record, row by row. The childcare office's trail reply and the benefits office's trail reply are already in the packet. By the end of the hearing, the \u2018failed to attend\u2019 notation is corrected on the record: the invitation is entered as mailed to an address the mother never lived at, after her correct update was on file, and the briefing step is re-set for her to take.",
 "Two of the three systems stand restored in the fiction of this file: the childcare arrangement is re-looked-at and restored on the trail's paper, and the benefits case is re-opened on its trail's paper, each in its own office's process. The third thread is restored differently, and the room says so plainly: your housing position is put back to where you would have stood had the invitation reached you — your place in the process is restored, as of now. The months the process ran without you are not given back. Nobody in the room pretends otherwise, and the corrected record does not either. The twins' case proceeds from a file that finally describes its own mail.",
], ending=True, debrief=[
 "WHAT THE RECORD HELD (the hidden record, revealed): A single correct document underneath three errors. The mother's address-update form, in her own handwriting, with the correct address, dated before all three mailings — and the agency's own mailing record showing the childcare letter sent to the prior apartment, the benefits notice sent to the former shelter, and the briefing invitation sent to a transposed-number address she never lived at. Three separate written trails, one per letter, each following the process stated on that letter's own face, put the pattern in front of each office; the filed packet put the agency's own two pages in front of the room that owned the \u2018failed to attend\u2019 notation.",
 "THE LAW UNDER THIS PATH: Only the verified instruments were used, and their limits are the lesson. The agency's form and mailing record were obtained because the case record \u2018shall be released upon request\u2019 (55 Pa. Code \u00a7 3130.44(d)) \u2014 the request is what turned a mailing pattern from a mother's account into the file's own testimony. Counsel (42 Pa.C.S. \u00a7 6337) filed the packet and asked the room to correct its own notation from its own pages. No program's rules are stated anywhere in this scenario as law: each letter stated its own process on its face, the trails followed those faces, and what each office restored was restored in its own process, on its own paper. Label this ending PARTIAL, plainly: two threads restored, the notation corrected, the housing position restored to where she would have stood \u2014 and the lost months not given back, because corrections restore records and positions, not time.",
 "THE HONEST PART: The months are really lost. The briefing's season passed; steps that would have followed it start now, not then; and a different room, reading the same packet faster or colder, could have corrected less. The errors themselves were nobody's villainy \u2014 a form filed and not propagated, a number transposed at reading speed \u2014 which is precisely why they survived until somebody laid the file's pages side by side. Workers, offices, and luck held pieces of this outcome. What your choices controlled was narrower and durable: each error was answered in writing, in its own system's process, and the pattern was filed where the notation lived. Outcomes in this system turn on workers, judges, and luck as much as on any parent's choices \u2014 and never on a parent's worth.",
]),
N("end_partial_notation", 82, "Ending \u2014 Restored in Part, the Notation Standing", [
 "The oral account is given clearly, and it lands the way clear oral accounts land in rooms that run on exhibits: it is believed, personally, by several people in the room, and it moves the two offices' threads — whose written trails, where you walked them, already exist in their own files. On the strength of the hearing's discussion, the childcare and benefits processes continue toward restoration in their own buildings, on their own paper.",
 "The notation is another matter. A transcript of counsel's sentences is not the agency's form, and it is not the agency's mailing record, and the room — asked to correct its own file's sentence on the strength of a speech about pages it has not seen — does what rooms do: it notes the representation, continues the matter, and leaves \u2018failed to attend\u2019 standing in the summary, to be quoted by the next one. Partial restoration, in two systems, and the sentence intact in the third — the one that describes you.",
], ending=True, debrief=[
 "WHAT THE RECORD HELD (the hidden record, revealed): A pattern, stated accurately and completely \u2014 in a transcript. The three letters, the three addresses, and the update form underneath them were all described at the hearing in the right order with the right dates. None of the pages themselves were before the room, because none had been requested into a packet or filed beside the notation. The two offices' threads, pursued in their own processes, moved on their own paper. The dependency file gained a transcript of an argument and kept its conclusion.",
 "THE LAW UNDER THIS PATH: The instruments that distinguish this ending from the full one are the verified ones, unused at the decisive step. The agency's update form and mailing record were available on written request (55 Pa. Code \u00a7 3130.44(d)); counsel (42 Pa.C.S. \u00a7 6337) can file what a parent obtains, and cannot file what was never requested. Nothing in this scenario states any program's rules as law \u2014 the two offices acted, as before, in the processes their own letters stated on their faces. A notation is corrected by documents in its own file, not by descriptions of documents in another room's transcript. That is the whole mechanics of this ending, and it is labeled for what it is: a partial restoration with the notation standing.",
 "THE HONEST PART: Your account was true, complete, and believed by people who could not act on belief. That is not a consolation; it is an indictment of nobody in particular and a description of every file everywhere. The packet can still be assembled and filed after this hearing \u2014 the form and the mailing record still exist, and a later room can still correct the sentence \u2014 but each summary that quotes \u2018failed to attend\u2019 in the meantime makes the correction slower and the explaining longer. A worker who had laid the form beside the mailing record when the notation was written would have spared you all of it. The sentence in the file is a verdict on what was filed, not on the mother who filled in the form correctly, on time, in her best handwriting.",
]),
N("end_one_restored", 82, "Ending \u2014 One Thread, Pulled Straight", [
 "The pages you obtained do real work at the table, even unfiled: the room cannot un-see its own update form, correctly written and dated before the mailings, once counsel holds it beside the summary. The briefing notation is softened in the hearing's discussion and marked for correction \u2014 a genuine change, made from the agency's own paper, in the room that owns it.",
 "But a hearing is one morning, and a packet is a structure. Without the filed three-row page and the two offices' trail replies in front of it, the room corrects the one error its own two pages prove completely — the transposed invitation \u2014 and leaves the two closures to their offices' unfinished processes, undescribed in the dependency file except as closures. One thread is pulled straight, in the record. The other two hang where their letters left them, pending paper nobody filed.",
], ending=True, debrief=[
 "WHAT THE RECORD HELD (the hidden record, revealed): The agency's own two decisive pages \u2014 the correctly dated update form and the mailing record \u2014 produced at the hearing, but unaccompanied: no filed pattern page tying the three letters together, and the two offices' threads standing at whatever stage unfiled correspondence had reached. The room corrected what its own pages proved in a single glance \u2014 the invitation mailed to an address the mother never lived at \u2014 and had no documented basis, in its own file, to redescribe the two closures as anything but closures.",
 "THE LAW UNDER THIS PATH: The record request (55 Pa. Code \u00a7 3130.44(d)) did the heaviest lifting in this scenario, and it shows: even unfiled, the agency's pages outweighed the summary built on their absence. What was missing was the filing \u2014 counsel (42 Pa.C.S. \u00a7 6337) presenting the whole pattern as one packet before the hearing, so each thread could be corrected in the file that described it. As throughout this scenario, no program rule is stated as law: the two closures remain in their offices' own stated processes, to be restored, if at all, on their own trails' paper. Partial paper partially works; this ending is the arithmetic of that sentence.",
 "THE HONEST PART: One real correction was won here, and it was the hardest of the three to win any other way \u2014 the transposed address existed nowhere outside the agency's file. What was lost was completeness and time: the two closures will now be re-argued office by office, summary by summary, while the dependency file describes them in its shortest grammar. A different room might have chased the pattern itself from the table; most rooms wait to be handed it, filed, in order. The mother in this ending did the single hardest thing \u2014 she got the file to testify \u2014 and stopped one filing short of making it testify about everything.",
]),
N("end_closed", 82, "Ending \u2014 Failure to Respond, As Written", [
 "The hearing adopts the summary's three lines the way hearings adopt most summary lines: without heat, without doubt, as the starting point for everything next. Childcare: released after no response. Benefits: closed after no response. Briefing: family failed to attend. Three closures, entered as facts about a mother who answered every letter she ever received and filled in the only form that mattered correctly, on time, before any of them were mailed.",
 "Your account of the three addresses was heard, in order, in your own voice. It was believed the way unaccompanied accounts are believed \u2014 personally, and set aside professionally \u2014 because the pages that would have proven it were never requested, and the trails that would have documented it were never walked in writing. The three systems keep their closures. The file keeps its grammar. The twins' case proceeds on a description of their mother that its own records contradict, in a drawer nobody opened.",
], ending=True, debrief=[
 "WHAT THE RECORD HELD (the hidden record, revealed): Conclusions only. Three lines \u2014 no response, no response, failed to attend \u2014 each the residue of a letter mailed to a wrong address after the mother's correct update was already on file. The update form itself sat in the agency's file throughout: correct, dated, and unconsulted by any summary. The mailing record sat beside it, equally available, equally unread in combination. Nothing in this ending required anyone to act in bad faith. It required only that nobody lay page one beside page two.",
 "THE LAW UNDER THIS PATH: Every instrument that would have answered the summary existed and is verified. The case record \u2014 form, mailing record, and entries \u2014 was available on written request (55 Pa. Code \u00a7 3130.44(d)); the request is what makes a file testify against its own conclusions. Each letter stated its own process on its face, and a dated written trail in that process is what turns a closure into a correspondence. Counsel (42 Pa.C.S. \u00a7 6337) can assemble and file whatever paper exists \u2014 and cannot manufacture, at a hearing, a mailing record from a spring already past. Defaults rule wherever documentation does not. That sentence, not any fact about this mother, is this ending.",
 "THE HONEST PART: Be clear, because the file was not: you did the one affirmative act this tangle ever asked of you, correctly and on time \u2014 you told the system where you lived, on its form, in your own hand. The system then mailed your life to an empty apartment, a vacated shelter bed, and an address that never existed, and recorded your silence at all three. A worker who propagated the update, a clerk who read the number at proofreading speed, a supervisor who asked where the letters had gone \u2014 any of them changes this ending without you changing anything. It records the state of three files, not the reliability of a mother. And the form is still in the file, dated and correct: a request made tomorrow still starts the correction, later and slower, but from the strongest page in the case.",
]),
]

s115_meta = {"title": "The First 90 Days",
 "subtitle": "Scenario 115 \u2014 Three Letters, Three Addresses (a fictional composite)",
 "startDateISO": "2026-02-02", "startNode": "start", "startCash": 170,
 "tier": "Complex",
 "summary": "Three letters from three systems went to three wrong places after Shana's correctly filed address update \u2014 and the file recorded her silence at all three as failure to respond, and failure to attend."}

s115 = build(s115_meta, s115_nodes, S115_START)

S115_WIN_PATH = ["start","update_form","new_address","landlord_note","childcare_news","childcare_reply",
 "benefits_news","benefits_reply","housing_news","housing_reply","three_threads",
 "records_learn","records_fork","file_arrives","untangle","mail_log_detail",
 "trail_childcare","trail_benefits","trail_housing","assembly","filed_scene",
 "ordinary_weeks","twins_visit_mid","address_proof","summary_arrives","counsel_second","review_notice","review_prep",
 "eve115","review","end_restored_partial"]

# =====================================================================
# SCENARIO 116 — The Summary Line (batch capstone)
# Mother Althea; daughter Leona, 11 (placed pre-story).
# Entry into care: Monday, September 1, 2025.
# Story opens month 14: Friday, October 2, 2026.
# ASFA 15-month date: entry + 15 calendar months
#   = Tuesday, December 1, 2026 = dayOffset 60 from the start.
# All three dates and the offset are computed and asserted below.
# =====================================================================
S116_ENTRY = date(2025, 9, 1)
S116_START = date(2026, 10, 2)
S116_ASFA = add_months(S116_ENTRY, 15)
assert S116_ENTRY.strftime("%A") == "Monday", S116_ENTRY
assert S116_START.strftime("%A") == "Friday", S116_START
assert S116_ASFA == date(2026, 12, 1), S116_ASFA
assert S116_ASFA.strftime("%A") == "Tuesday", S116_ASFA
S116_ASFA_OFF = (S116_ASFA - S116_START).days
assert S116_ASFA_OFF == 60, S116_ASFA_OFF
d116 = lambda off: datestr(S116_START, off)
ASFA_STR = fmt(S116_ASFA)
ENTRY_STR = fmt(S116_ENTRY)

s116_nodes = [
N("start", 0, "Month Fourteen", [
 "Your name is Althea. Your daughter Leona is eleven, and she has been in care since before this story opens — long enough that her life has a second geography now: a foster home, a school run, a bedroom that is hers in every way except the way that is being decided. Your case is in its fourteenth month. Your compliance, in the file's own recent summaries, has been described as steady: treatment completed, visits kept, work steady, the plan's goals met or moving.",
 "A permanency review is approaching, and the talk around it — your worker's, your lawyer's — has been the talk of a case preparing to move toward home. Then the pre-review summary arrives, and in its middle, in the level grammar summaries use, sits one phrase that stops the whole direction of the case cold.",
 "\u2018Unresolved financial instability.\u2019 Four words, built \u2014 the summary's own sourcing shows, if you read it the way your lawyer reads \u2014 from three money entries in the file. This story is an audit of those three entries, one by one, on paper. It is also a race against a date the summary does not mention.",
], [C("Read the phrase the way your lawyer will: as a claim with sources", "summary_line",
      note="Claims with sources can be audited. That is either the worst news in this story or the best, and the next fifty-seven days will decide which.")]),

N("summary_line", 2, "One Phrase, Three Entries", [
 "Your lawyer spreads the summary on her table and does the thing she does with every document in this case: she finds its footnotes. \u2018Unresolved financial instability\u2019 has three. A support arrearage, accrued over two months. A missed payment, recorded on a date in the spring. And a benefits gap — a stretch where a benefit the plan counted simply was not there.",
 "Three entries. Read cold, as a judge will read them, they sketch a mother whose money is a problem she has not solved. Read by the woman who lived those months, each one has a biography the file never recorded. \u201cSummaries are conclusions,\u201d your lawyer says. \u201cEntries are claims. We audit claims. One at a time, on paper, with the file's own pages where the file has them.\u201d You have counsel because the law provides for it (42 Pa.C.S. \u00a7 6337). For the next eight weeks, her job and yours is an audit.",
], [C("Ask her to name the other clock first — the one the summary does not mention", "counsel_meet",
      note="She turns her desk calendar around. One date is already circled, in pencil, in a hand that circled it months ago.")]),

N("counsel_meet", 5, "The Date in Pencil", [
 f"Your lawyer states the arithmetic slowly, the way it must be stated to be believed. Leona entered care on {ENTRY_STR}. Fifteen calendar months from that entry is {ASFA_STR} \u2014 {ENTRY_STR} plus fifteen calendar months, computed month by month, landing on {ASFA_STR}, which is day {S116_ASFA_OFF} of this story. When a child has been in care for fifteen of the most recent twenty-two months, the federal law generally presses the agency to file a petition to end parental rights, unless an exception is documented (42 U.S.C. \u00a7 675(5)(E)).",
 "\u201cGenerally, and unless,\u201d she says, \u201care the two most important words in this case, and both of them run on paper. Our audit is the argument for the review. The exception packet is the backstop if the date arrives first. We build both, in that order, starting now \u2014 because a summary line corrected entry by entry is a case moving home, and a summary line left standing is the agency's Exhibit A for why the date should decide everything.\u201d",
], [C("Begin the audit where she begins: with the file itself, not your memory of it", "three_entries",
      addHidden=["Counsel meeting \u2014 ASFA 15-month date computed from the entry date and named; audit and exception backstop planned"],
      note="Two builds, one deadline. The audit first \u2014 because a truthful file is the argument everything else stands on.")]),

N("three_entries", 8, "Three Tabs in a Binder", [
 "The binder gets three tabs, labeled in counsel's hand: ARREARAGE. PAYMENT. GAP. Under each, the audit's question is written in the same words, because the discipline of an audit is that every entry gets the same question: what does the paper say happened, and what paper would prove it?",
 "Your side of the paper is a folder you have kept the whole case — receipts, letters, the plan itself, with its notes in the margins in three different pens. The file's side is in a building across town. An audit that reads only one side is a memoir. An audit that reads both is an exhibit. Getting the second side is, as ever in this system, a written act with a citation.",
], [C("Open your folder on the table and take the inventory honestly", "folder_beat",
      note="Receipts, letters, the plan with its margin notes. Somewhere in this folder are two of the three answers. The third is in their file, on their own page.")]),

N("folder_beat", 10, "The Folder, Inventoried", [
 "The inventory is encouraging and incomplete in the specific way that decides cases. The plan is here — all of it, including the page your whole first entry will turn on. A payment receipt is here, folded into a visit envelope, dated, legible, exactly where you put it in the spring and have not thought about since. The treatment records are here, with their admission and discharge dates in a discharge summary's brisk paragraphs.",
 "What is not here is the agency's own paperwork about your money: the arrearage ledger as they keep it, the posting record as their system kept it, the closure letter as their file received it back. Your folder proves your life. Their file is what the summary was built from. The audit needs both, in the same binder, before it argues anything.",
], [C("Ask counsel how the file's side is obtained \u2014 in writing, by right", "records_learn",
      note="\u201cThere is a regulation,\u201d she says, and is already reaching for her card. \u201cIt is the most useful sentence in this entire case, and it is eleven words long.\u201d")]),

N("records_learn", 12, "Shall Be Released", [
 "The citation goes on the back of her card: 55 Pa. Code \u00a7 3130.44(d). The case record is to be released upon request \u2014 and your audit names its pages precisely: the family service plan with its notes, the support ledger entries for the two months in question, the payment posting record for the spring date, and the benefits correspondence, including the closure letter and the address it was sent to.",
 "\u201cNotice whose paper does the proving in this audit,\u201d counsel says. \u201cThe plan's pause note is the agency's own page. The posting record is their own system. The closure letter's address is their own envelope. We are not asking the review to believe you against the file. We are asking it to read the whole file \u2014 including the pages the summary didn't.\u201d",
], [C("Decide this week \u2014 the audit's pages take time to arrive, and the calendar does not wait", "records_fork",
      note=f"The packet will take days to arrive. {ASFA_STR} will not move for it. In this story, those two facts are the whole schedule.")]),

N("records_fork", 14, "Ask for the Audit's Pages", [
 "The written request names the pages, one by one, the way the binder's tabs name them. It goes in dated and copied, with the copy going behind a fourth tab counsel labels, in pencil, REQUEST \u2014 because in this system the asking itself is evidence, dated, that the reader of the file once asked to see the file.",
 "Or the audit can run on your folder and your memory alone: strong on your life, silent on theirs, and incapable of the one move this case turns on \u2014 showing the review the agency's own page that contradicts the agency's own summary.",
], [C("Put the request in writing \u2014 plan, support ledger, posting record, benefits correspondence \u2014 and keep a copy", "packet_arrives", cash=-6,
      setFlags=["recordsRequested"],
      addHidden=["Case record requested in writing under 55 Pa. Code \u00a7 3130.44(d) \u2014 plan, support ledger, posting record, and benefits correspondence named"],
      note="Six dollars of copies and postage. The request names the pages. Named pages, in this system, arrive; unnamed files arrive as summaries."),
    C("Audit from your folder alone \u2014 it is complete about your life, and your life is the subject", "summary_only", cash=-6,
      note="Six dollars across the week's errands either way. Your folder is complete about your life. The summary was not built from your folder, and it will not be corrected by it alone.")]),

N("packet_arrives", 18, "The File's Side, on the Table", [
 "The packet arrives redacted in the ordinary places and complete in the decisive ones. The plan is here, with the note the audit came for, in the agency's own hand on the agency's own page. The support ledger is here, month by month. The posting record is here, with its two dates \u2014 the date a thing is paid and the date a system posts it, sitting in adjacent columns like strangers. And the benefits correspondence is here, closure letter and envelope data together.",
 "Counsel reads it through once, in silence, and then says the sentence the whole audit was built to earn: \u201cAll three entries are auditable from their own paper. Now we audit them. Tab one.\u201d",
], [C("Open tab one \u2014 the arrearage", "audit_plan",
      addHidden=["Agency packet received \u2014 plan note, support ledger, posting record, and benefits correspondence all present"],
      note="Three entries, three tabs, one method: the paper says what happened, or it does not, and either way the audit writes it down.")]),

N("summary_only", 18, "Auditing Blind", [
 "Without the packet, the audit works from the short side of the table. Your folder's plan copy is here \u2014 if the pause note is on your copy, it can be argued; the support ledger's own lines cannot be quoted; the posting record's second date cannot be shown; the closure letter's envelope cannot be produced. You would be telling the review, accurately and in detail, what the agency's own pages say, without the pages.",
 "Counsel is plain about the arithmetic of that: \u201cWe proceed. We document what we can from your side, in writing, while it is still true in detail. But understand the price: every entry we cannot answer from their paper, we answer from yours \u2014 and a summary is never corrected by the folder it ignored. It is corrected by the file it came from.\u201d",
], [C("Proceed with the folder's audit, documenting your side while it is still detailed", "audit_plan",
      note="The audit proceeds. Its binder will have your paper in all three tabs and their silence in all three, which the review will price precisely.")]),

N("audit_plan", 21, "The Method, Stated Once", [
 "The method is stated once, on the binder's first page, and never varied: for each entry, the summary's claim; the document that tests it; the result, in one sentence, with the document attached. No adjectives. No argument about anyone's intentions. An arrearage either accrued while the plan said paused, or it did not. A payment either posted late, or it did not. A letter either went to the old address, or it did not.",
 "\u201cReviews can argue with mothers,\u201d counsel says. \u201cThey have had practice. They cannot argue with their own ledger, their own plan page, and their own envelope, laid in a row. Tab one. The two months.\u201d",
], [C("Open the arrearage entry \u2014 the two months at the start of the year of this case", "binder_check",
      note="Two months in which the file recorded money owed and nothing else. Your memory of those months is a hospital ward. The file's memory is a column.")]),

N("binder_check", 22, "The Binder, Checked Against the Summary", [
 "Before tab one is opened, counsel performs the audit's control test: she reads the summary's three entries against the packet's table of contents, line by line, checking that each entry's testing document actually exists in the pages received. Arrearage: the plan and the ledger, both present. Payment: the posting record, present, with both its date columns. Gap: the correspondence, present, letter and mailing record together.",
 "\u201cAn audit is only an argument if its exhibits exist,\u201d she says. \u201cSummaries skip that step, which is how phrases get built from pages nobody opened. We do not skip it. Every claim we make at the review will have a page number in this binder, or it will not be made.\u201d It is a small, cold ceremony, and it is the reason the rest of this story can be warm.",
], [C("Open tab one, with the control test passed", "entry1_setup",
      note="Every testing document exists. The audit can now afford to be exact, entry by entry, in the file's own pages.")]),

N("entry1_setup", 24, "Entry One: The Paused Months", [
 "Entry one, as the summary's source shows it: a support arrearage, accrued across two months, listed in the ledger in the ordinary way \u2014 amount growing, no payments recorded, a parent's obligation silently compounding. Read cold, it is the summary's strongest entry. It looks like a debt ignored.",
 "What the ledger does not say is where you were for those two months: in inpatient treatment, admitted on one date and discharged on another, in a program the plan itself had ordered. And the plan \u2014 the agency's own plan, on the agency's own page \u2014 recorded the fact in its own words at the time: the relevant goal was noted as paused for the treatment period. A paused goal and an accruing arrearage sat in the same file, in different sections, never introduced to each other. The summary met only one of them.",
], [C("Ask what paper proves the pause \u2014 the plan page, and the treatment dates", "entry1_doc",
      note="\u201cTwo documents,\u201d counsel says. \u201cTheir plan page, with their note. And the treatment record, with its dates. Together they are the whole entry.\u201d")]),

N("entry1_doc", 26, "The Plan's Own Page", [
 "The plan page is the audit's first exhibit, and it is beautiful in the way only bureaucracy can be: the goal, the note beside it in the worker's hand recording the pause for the treatment period, the date of the note. Nobody backdated anything. Nobody wrote it for this audit. It was written at the time, for the file's own use, and then the summary was written later by someone who did not turn to this page.",
 "The treatment dates are the second document, and they can be obtained the way such records are obtained: a written request to the program, in its own process, for the admission and discharge summary you are entitled to ask them for \u2014 paper you partly hold already, in your folder's discharge summary, waiting to be copied, dated, and put behind tab one.",
], [C("Assemble entry one in writing \u2014 the plan page, the pause note, and the treatment admission and discharge dates", "treatment_dates", cash=-4,
      setFlags=["entry1Doc"],
      addHidden=["Entry one documented \u2014 arrearage accrued during inpatient treatment while the plan's own note recorded the goal as paused; treatment dates attached"],
      note="Four dollars of copies. Tab one now holds a complete sentence: the debt accrued, in the months the plan itself had paused, while its author was in the treatment the plan itself had ordered."),
    C("Carry entry one on your account \u2014 you were there, and the ward's dates are in your memory exactly", "treatment_dates", cash=-4,
      note="Four dollars across the week's errands either way. Your memory of the ward is exact. At the review, exact memory will be weighed against a printed ledger \u2014 the audit's first lesson, learned at the first tab.")]),

N("treatment_dates", 28, "Two Months, with Dates on Them", [
 "Tab one, closed or open depending on the paper in it, tells the same two months in two grammars. The ledger's grammar: an obligation, accruing. The assembled grammar: a mother in ordered treatment, a goal paused by the plan's own note, an arrearage that is the arithmetic residue of a pause nobody carried across the file from the plan section to the money section.",
 "\u201cNotice what we are not claiming,\u201d counsel says. \u201cWe are not claiming the money was not owed, or that ledgers should stop for treatment. We are claiming the summary's word \u2014 instability \u2014 cannot be built from a paused goal's residue without saying it was paused. The document says paused. The summary said nothing. Silence, in summaries, is a conclusion.\u201d Tab two is a smaller story with the same shape: a date, and another date, and a summary that read only the first.",
], [C("Open tab two \u2014 the missed payment", "ledger_page",
      note="One payment, two dates. The whole entry lives in the distance between them, which is five days wide and one summary deep.")]),

N("ledger_page", 29, "The Ledger's Own Lines", [
 "One more look at entry one before it closes, because the ledger deserves to be read as carefully as the summary read it carelessly: its lines for the two treatment months show the obligation growing in the ordinary monthly entries, each dated, each correct as arithmetic. Nothing in the ledger is false. That is the audit's most important finding about it, and counsel writes it on the binder's first page in so many words.",
 "\u201cWe are not accusing their ledger of lying,\u201d she says. \u201cA ledger that accrues during a pause is doing its job. The summary's job was to read the ledger beside the plan. It read one book of a two-book story and reviewed the wrong one — as your daughter will put it, when she is told. Tab two.\u201d",
], [C("Open tab two — the missed payment", "entry2_setup",
      note="The ledger: accurate, incomplete, and innocent. The summary: the only document in the case that read it alone.")]),

N("entry2_setup", 30, "Entry Two: The Missed Payment", [
 "Entry two, as the summary's source shows it: a payment recorded as missed, on a date in the spring \u2014 the date it was due, by the file's reckoning, with no payment beside it. In the summary's parade it is the middle entry, the one that turns one money problem into a pattern: arrearage, missed payment, gap. Patterns are what summaries are for. Patterns are also what audits are for, because a pattern built from three entries falls one audited entry at a time.",
 "You remember the spring payment the way you remember all your payments in this case: made, on time, with a receipt. Your folder holds the receipt, folded into a visit envelope since the spring. What your folder cannot show is the other half of the entry \u2014 what the receiving system did with the payment after you made it. That half lives in the posting record, in its two adjacent columns.",
], [C("Take the receipt out of the visit envelope and lay it beside the posting record", "entry2_doc",
      note="The receipt has been waiting in an envelope for months, patient as only paper can be. It is about to become the audit's smallest and cleanest exhibit.")]),

N("entry2_doc", 32, "Paid on One Date, Posted on Another", [
 "The two papers, adjacent, tell the whole entry without either of them raising its voice. Your receipt: the payment, made on its date, in the ordinary way, receipted at the time. The posting record: the same payment, entered into the system's ledger on a date five days later \u2014 a posting lag, the ordinary delay between a payment arriving and a payment being posted, recorded in the system's own two columns for anyone who reads both of them.",
 "The summary read one column. Between the due date and the posting date, the entry wore the clothes of a missed payment \u2014 and a lag, summarized, becomes a failure, and a failure, listed between an arrearage and a gap, becomes \u2018instability.\u2019 Assembled in writing, the entry corrects itself: the receipt and the posting record, copied, dated, and put behind tab two as one exhibit with two dates.",
], [C("Assemble entry two in writing \u2014 the receipt and the posting record, copied as one two-date exhibit", "posting_office", cash=-4,
      setFlags=["entry2Doc"],
      addHidden=["Entry two documented \u2014 \u2018missed payment\u2019 was a posting lag; receipt and the system's own posting record assembled as one exhibit"],
      note="Four dollars of copies. Tab two holds two dates now, and the distance between them has an author, and the author is a queue."),
    C("Keep the receipt in the folder \u2014 the review can ask the system about its own posting", "posting_office", cash=-4,
      note="Four dollars across the week's errands either way. Reviews rarely ask systems about themselves. They read summaries of systems, written from one column.")]),

N("posting_office", 34, "Five Days, Explained by Nobody", [
 "Counsel closes tab two with the audit's driest sentence so far: \u201cNobody did anything wrong in entry two. A payment was made, a queue was slow, a column was read alone. That is worth saying at the review, in exactly those words \u2014 because it teaches the room how the summary was built, and a room that understands how its summary was built reads the third entry differently.\u201d",
 "Tab three is the entry with the longest shadow, because it is the one that looks most like character: a benefits gap, weeks long, in a plan that counted on the benefit being there. It is also \u2014 the audit already suspects, from the packet's envelope data \u2014 the entry with the most familiar cause in this entire library of stories: a letter, an address, and a file that recorded a silence as a choice.",
], [C("Open tab three \u2014 the gap", "queue_explain",
      note="A closure, a prior address, and a pattern this project has met before \u2014 now read, by a summary, as a mother's character.")]),

N("queue_explain", 35, "The Queue, in Plain Words", [
 "For the binder's completeness, counsel has the posting office's ordinary explanation added to tab two in writing: payments are entered in the order they are processed, and in busy weeks the entry can follow the payment by days — a queue, described by the people who run it, in the flattest prose in the entire binder. Nobody apologizes in it. Nobody needs to. It simply establishes that the distance between tab two's two dates is a known, ordinary feature of the system that posted it.",
 "\u201cFile the flat prose first,\u201d counsel says, \u201cand the receipt second. By the time the room reaches the receipt, it will already know what a five-day gap between paying and posting is. Sequence is half of every argument ever made from paper.\u201d",
], [C("Open tab three — the gap", "entry3_setup",
      note="A queue, explained by its keepers, filed ahead of the receipt it explains. Tab three is the longest shadow in the binder, and it opens next.")]),

N("entry3_setup", 36, "Entry Three: The Gap", [
 "Entry three, as the summary's source shows it: a benefit the plan counted on was closed, and stayed closed for a stretch of weeks, before it was restored. The file records the closure and the gap. What the file's summary does not record is the closure's own first step: a letter, mailed by the system that closed it, asking the recipient to act by a date printed on its face \u2014 and mailed, the packet's correspondence shows, to your prior address. The address you had moved from. The address the agency's own file elsewhere records you leaving, with a new address given in its place.",
 "So the gap's biography is: a letter to a place you no longer lived; a deadline on its face, expiring in an empty room; a closure for non-response; weeks of absence, summarized upward into \u2018instability.\u2019 You have seen this exact shape before, in the stories this library tells \u2014 a mailing read as a mother. The audit's job is to make the review see it too, from the file's own envelope.",
], [C("Ask what paper proves the address \u2014 the letter's mailing record, and your update in their own file", "entry3_doc",
      note="\u201cTheir envelope and their file,\u201d counsel says. \u201cTab three is their handwriting from start to finish. We just have to assemble it in the order it happened.\u201d")]),

N("entry3_doc", 38, "The Envelope in the File", [
 "The assembled exhibit for tab three has three pages, all of them the system's own. The closure letter, with the action it asked for stated on its face and the date it set. The mailing record, showing the address it was sent to: the prior address. And the agency file's own record of your move \u2014 the new address, given and noted, dated before the letter was mailed. Three pages, in date order, and the gap stops being a fact about your finances and becomes a fact about a mailing, which is what it always was.",
 "Assembled in writing, copied, and put behind tab three, the entry completes the audit's pattern: three entries, three documents, three silences in a summary \u2014 a pause never carried across the file, a lag never read in its second column, a letter never traced to its address.",
], [C("Assemble entry three in writing \u2014 closure letter, mailing record, and the file's own record of the move, in date order", "address_proof", cash=-5,
      setFlags=["entry3Doc"],
      addHidden=["Entry three documented \u2014 benefits gap caused by a closure letter mailed to the prior address after the move was on file"],
      note="Five dollars of copies. Tab three is the system's own paper, in the order it happened. The audit is now three tabs deep, and every tab is checkable."),
    C("Carry entry three on your account \u2014 the move, the empty apartment, the weeks, in order", "address_proof", cash=-5,
      note="Five dollars across the week's errands either way. Your account is in perfect order. Order, unaccompanied, is the currency summaries are never paid in.")]),

N("address_proof", 40, "Three Tabs, Closed", [
 "The binder closes with a sound like a small book ending. Counsel turns its pages once, slowly, in the manner of a person checking a proof: tab one, a paused goal's residue, documented from the plan's own page; tab two, a lag, documented from two dates in the system's own record; tab three, a mailing, documented from the system's own envelope. Underneath all three, the summary's phrase, still standing in its paragraph, waiting for the review to decide whether it describes anything.",
 "\u201cNow the second build,\u201d counsel says. \u201cBecause the audit corrects the file at the review \u2014 and the review is ours to prepare for. But the date does not attend reviews. While we prepare the correction, we file the backstop: the exception packet, documented, so that if the calendar reaches fifteen months before the file is truthful, the filing decision still has to reckon with a record \u2014 relative care if it applies, a documented compelling reason, or services identified and not provided \u2014 instead of with a phrase.\u201d",
], [C("Visit Leona first \u2014 the binder can wait one Saturday", "summary_draft116",
      note="The audit is about a file. The file is about a girl who has opinions about binders, and she delivers them on Saturdays.")]),

N("summary_draft116", 41, "The Phrase, Sighted Again", [
 "Word comes through counsel, in the ordinary way of such word, that the summary's phrase is already being quoted — a draft report for the review repeats \u2018unresolved financial instability\u2019 as the case's settled description of its mother, citing the summary that coined it, which cited the entries nobody audited. Phrases reproduce exactly like this: document to document, each quotation laundering the last one's doubt, until the phrase has the one property the entries never had — it looks established.",
 "\u201cThis is why the correction has to happen on the record, in the room, entry by entry,\u201d counsel says. \u201cA phrase corrected in a filing can still be quoted out of the old summary. A phrase corrected on the record, by the court, entry by entry, gets corrected in the transcript every future report has to reckon with. We are not just fixing a line. We are fixing what the next ten documents will say.\u201d",
], [C("Take Saturday's visit first — the phrase will keep until the packet answers it", "leona_visit",
      note="The phrase is reproducing. The packet is about to be its first reader with a red pen and the authority to use it.")]),

N("leona_visit", 42, "Leona, on Saturday", [
 "Saturday's visit is the audit's only scene without paper in its hands, and the scenario insists on it for the record. Leona, at eleven, has reached the age of auditing adults: she wants to know what the phrase in the summary means, having heard it in the partial way children hear everything, completely. You tell her the truth at her size: grown-ups wrote a sentence about money that left some pages out, and you and your lawyer are putting the pages back, in order, with dates.",
 "She considers this with the seriousness of a fair judge. \u201cSo it's like a book report on the wrong book,\u201d she says. You tell her that is exactly what it is, and that the review is where the right book gets read. She assigns you, as homework, to make sure they read the whole thing. On the bus home you write the visit up in the folder, dated, because that is what your hands do now \u2014 and because the whole-thing, in this case, includes a girl who grades summaries.",
], [C("Go home and assemble the correction packet with counsel", "assembly116",
      note="Homework accepted. The packet is the whole thing, in date order, with tabs \u2014 the right book, bound.")]),

N("assembly116", 44, "Assemble the Packet, Raise It Aloud, or Wait", [
 "Three ways, laid out with the binder between them. One: assemble the entry-by-entry correction packet \u2014 the three tabs, the plan page, the receipt and posting record, the letter and its envelope, with a short covering statement from counsel that asks the review to correct the summary line entry by entry on the record before it makes its determinations \u2014 and file it, in writing, before the review. Two: raise the audit orally at the review \u2014 three true stories, told clearly, with the exhibits in a binder in counsel's office. Three: wait for the review and trust that a phrase built from one column of three records will be questioned by the room that printed it.",
 "The packet, if it is filed, goes in whole: partial paper, this scenario promises, will partially work, and the phrase needs only one surviving entry to survive.",
], [C("Assemble and file the entry-by-entry correction packet with counsel", "filed116", cash=-8,
      setFlags=["auditPacket"], requiresFlags=["recordsRequested"],
      addHidden=["Entry-by-entry correction packet filed with counsel before the permanency review"],
      note="Filed, stamped, copied. The summary line now has, in its own file, a dated answer with three tabs."),
    C("Raise the audit orally at the review instead", "oral116",
      setFlags=["oralRaised"],
      note="Three stories, clearly told, on a transcript \u2014 with the binder's documents unfiled beneath them, in counsel's office."),
    C("Wait \u2014 the review printed the phrase; the review can question it", "wait116",
      note="Rooms do sometimes question their own phrases. They do it, in this library's experience, when paper gives them a reason. Waiting declines to provide one.")]),

N("filed116", 46, "Filed, Entry by Entry", [
 "The filing takes a morning and changes the case's geography: the audit is now where decisions are made from. Your worker, at the next check-in, mentions it in the tone workers use for paper that will be read by judges: \u201cI saw the packet. The plan note \u2014 I wrote that note. I didn't connect it to the ledger.\u201d It is not an apology. It is the audit's whole thesis, confessed by the file's own author, in advance of the room: the pages were all there. They were never introduced.",
 "The summary line still stands in its paragraph. Summaries are not rewritten by packets; they are corrected by rooms, on dates, on the record. Two dates now approach at once: the review, and the fifteenth month. The backstop is next, and it is filed in the shadow of the second one.",
], [C("Turn to the backstop \u2014 the exception packet, before the date arrives", "exception_beat",
      note="The correction is filed. The calendar, unimpressed, continues. Backstops are for calendars.")]),

N("oral116", 46, "Saved for the Review", [
 "The decision is made and noted in counsel's file: the audit will be raised orally at the review. The binder stays assembled, its tabs in order, its documents unfiled. \u201cWe will say each entry clearly,\u201d counsel says. \u201cUnderstand the exchange rate. A filed exhibit is weighed. A spoken correction is heard, noted as \u2018mother's counsel stated,\u2019 and filed in a transcript nobody summarizes. The phrase, meanwhile, sits in a summary everybody reads.\u201d",
 "You keep the visits, the work, the steady weeks the file itself calls steady. The binder waits for its morning. Whether a morning is enough for three tabs of other people's paper is the question the review is about to price.",
], [C("Prepare the three accounts with counsel, entry by entry, word by word", "exception_beat",
      note="If the record will hold only words, the words will at least be exact \u2014 a pause, a lag, an envelope, in that order.")]),

N("wait116", 46, "The Phrase, Undisturbed", [
 "The decision is made and noted: wait. The audit exists \u2014 in a binder, in counsel's office, in the folder's receipts \u2014 and the summary exists in the file the review will read, and the two documents have never been introduced. Counsel does not argue; she has given her advice, and she writes yours down beside it, because that too is what lawyers are for.",
 "\u201cOne thing, then,\u201d she says. \u201cA phrase like this does not stand still while we wait. It gets quoted. Every week it stands, it becomes the file's settled description of your money, and settled descriptions are what filing decisions are made from. The date is coming either way. Waiting chooses what it will find.\u201d",
], [C("Keep the steady weeks, and let the calendar run", "exception_beat",
      note="Steady weeks, an unfiled audit, and a date that does not negotiate. The backstop decision is the last one the calendar leaves open.")]),

N("exception_beat", 49, "The Backstop: A Packet for the Date", [
 f"The exception packet is a different document from the correction packet, and counsel keeps the difference sharp. The correction packet speaks to the review: fix the line, entry by entry, on the record. The exception packet speaks to {ASFA_STR}: if the fifteenth month arrives before the file is truthful, the agency's filing duty is generally pressed \u2014 unless an exception is documented (42 U.S.C. \u00a7 675(5)(E)): Leona cared for by a relative, or a documented compelling reason that filing would not serve her, or services the agency identified as necessary for her safe return that were not provided. Exceptions are not hopes. They are documents, filed before the date they answer.",
 "The packet assembles what the record supports \u2014 the audit's documented entries, your completed services, the visit record \u2014 and asks that an exception, if the record supports one, be documented in the file before the date. Filed, it is a backstop: the correction may win first, and the packet will simply never be needed. Unfiled, it is one more true thing that exists outside the file the date will read.",
], [C("Build and file the written exception packet with counsel, before the fifteen-month date", "cold_read", cash=-6,
      setFlags=["exceptionPacket"],
      addHidden=["Documented-exception packet filed in writing before the fifteen-month date, as backstop"],
      note="Stamped, filed, dated before the date. Whatever the review does, the filing decision will now have to reckon with a document."),
    C("Rely on the correction alone \u2014 the review comes first, and it will fix the line", "cold_read", cash=-6,
      note="Six dollars across the week's errands either way. Reviews do come first \u2014 when their dates hold, and when rooms correct whole lines. Backstops exist for the other kind of month.")]),

N("cold_read", 51, "A New Reader, Reading Cold", [
 "Personnel are weather in this system, and this month the weather turns in the audit's favor or against it, depending entirely on paper: the supervisor who will sign any filing decision is new, and reads the file cold \u2014 knowing no one in it, remembering nothing about it that the file does not say. A cold reader cannot be told what everyone in the case happens to know: that the arrearage was a pause, the miss was a lag, the gap was an envelope. She can only read.",
 "If the packets are in the file, she reads the plan's own note, two dates in adjacent columns, an envelope with the wrong address, and a dated exception packet. If they are not, she reads a summary with a phrase in it. \u201cFiles outlive the people who remember the case,\u201d counsel says. \u201cWe have known it since the first tab. The fifteenth month just gives the lesson a deadline.\u201d",
], [C("Prepare for the review, entry by entry, one last time", "review_prep116",
      note="The packets are filed or they are not. What remains is a room, a line, and three tabs \u2014 in whichever posture the autumn built them.")]),

N("review_prep116", 53, "Entry by Entry, with Counsel", [
 "Preparation is the audit read aloud, in the order the review will need it. At a permanency review, counsel reminds you, the court makes its determinations on the record before it \u2014 the determinations the law lists for reviews (42 Pa.C.S. \u00a7 6351(f)), including how long Leona has been in care \u2014 and the record before it will either contain the correction packet or contain only the phrase the packet answers.",
 "\u201cWe are not asking the room to find that you are stable,\u201d counsel says. \u201cWe are asking it to correct three entries from their own documents, in order, on the record \u2014 and then make its determinations from a file that tells the truth. A truthful file is not a favor to you. It is the court's working material. Judges correct working material, when the corrections are exhibits. They adopt summaries, when they aren't.\u201d",
], [C("Face the calendar choice \u2014 the review's date, or the easier later slot", "calendar_choice",
      note="One slot sits before the fifteenth month. One sits after it. The system offers both in the same polite letter, and does not say what the difference costs.")]),

N("calendar_choice", 54, "Two Slots in One Letter", [
 f"The court's letter offers two review dates in the same courteous typeface. The first is {d116(59)} \u2014 before the fifteenth month, close, demanding, and exactly what the autumn was built for. The second is weeks later, calmer for everyone's schedule \u2014 and after {ASFA_STR}, when the filing question will already have been answered by whoever read the file on the date, in whatever state the file was in on the date.",
 "\u201cReviews can be rescheduled,\u201d counsel says. \u201cFiling dates are not reviews. Take the first slot and the correction is argued while the file can still change what the date does. Take the second and we will attend a review about a case the date has already rewritten.\u201d",
], [C("Take the first slot \u2014 the review before the fifteenth month", "morning116",
      note="Ready or not, the audit is what it is \u2014 three tabs, two packets, one phrase. That, in the end, is what audits are for."),
    C("Take the later, calmer slot \u2014 work is impossible that first week", "end_date",
      note="The confirmation letter is polite and routine. So is the other letter it will eventually cross in the mail.")]),

N("morning116", 59, "The Morning of the Review", [
 "The morning of the review has the stillness of mornings that were prepared for in the autumn-in-miniature of the last eight weeks: the binder is in counsel's bag, the packets are in the file, the fare is in your coat, and Leona's homework — make sure they read the whole thing — is in your head, where homework lives. Nothing is left to assemble. Assembly was the autumn's work; this morning's work is only presence.",
 "On the way in, counsel says the last preparatory sentence of the scenario: \u201cWhatever the room does with the line, it will do it in front of the whole file for the first time. That has never happened before in this case. It is happening today because you requested the file, audited it, and filed the audit. Remember which part was yours, whatever happens.\u201d",
], [C("Enter the review", "review116",
      note="The whole file, in one room, for the first time in fourteen months. The phrase is about to meet its sources.")]),

N("review116", 59, "The Permanency Review", [
 f"The review on {d116(59)} is longer than the last one, because this time the file is at issue, not just the family. The summary is read, and its phrase is read with it, in the room's level voice: \u2018unresolved financial instability,\u2019 built from an arrearage, a missed payment, and a gap. The room begins, in the ordinary way, to treat the phrase as a fact about the mother in the chair.",
 "Then counsel asks that the line be corrected entry by entry, from the file's own documents, before the court makes its determinations on this record. What happens next depends, with a precision this scenario has been honest about since the first tab, on what your choices actually filed.",
], [C("Correct the line entry by entry \u2014 the plan's pause note, the two posting dates, the letter's own envelope, with the exception packet already on file", "end_corrected116",
      requiresFlags=["recordsRequested", "entry1Doc", "entry2Doc", "entry3Doc", "auditPacket", "exceptionPacket"],
      note="Three entries, three exhibits, all of them the file's own paper. The room does the corrections itself, out loud, which is where corrections become the record."),
    C("Correct the line from the filed packet \u2014 the packet without the plan page behind tab one", "end_one_entry",
      requiresFlags=["auditPacket"], requiresNoFlags=["entry1Doc"],
      note="Two tabs documented, one carried by account. The room is about to price exactly that ratio."),
    C("Correct the line from the filed packet \u2014 tab one documented, the receipt never assembled behind tab two", "end_one_entry",
      requiresFlags=["auditPacket", "entry1Doc"], requiresNoFlags=["entry2Doc"],
      note="Two tabs documented, one carried by a receipt in a visit envelope, at home. The room prices paper by its presence."),
    C("Correct the line from the filed packet \u2014 two tabs documented, the envelope never assembled behind tab three", "end_one_entry",
      requiresFlags=["auditPacket", "entry1Doc", "entry2Doc"], requiresNoFlags=["entry3Doc"],
      note="The gap stands on the file's shortest grammar, because its longest document \u2014 the system's own envelope \u2014 is not in the room."),
    C("Ask the room to take your word for the three entries", "end_stands116",
      note="Your word is accurate in every particular: a pause, a lag, an envelope. The phrase, printed and already read, is the room's starting point \u2014 and starting points are where summaries live.")]),

N("end_corrected116", 66, "Ending \u2014 Corrected, Entry by Entry", [
 "The correction takes the length of the audit, entry by entry, and the room does it in the only way corrections ever become real: out loud, on the record, from documents. Entry one: the arrearage is re-entered as accrued during the two months the plan's own note recorded the goal as paused, while its author was in the treatment the plan itself ordered \u2014 a pause's residue, documented as such. Entry two: the missed payment is corrected to a payment made on its date and posted five days later, receipt and posting record read together, as they should have been read the first time. Entry three: the gap is re-entered as caused by a closure letter mailed to the prior address after the move was on file \u2014 a mailing, documented as such.",
 "With the three entries corrected, the summary line cannot stand, and the court strikes it: \u2018unresolved financial instability\u2019 is removed from the record's description of this mother, replaced by the three corrected entries in their true shapes. On the truthful file that remains \u2014 treatment completed, visits kept, work steady, every money entry explained by the system's own paper \u2014 the court does what the case had been preparing to do before the phrase stalled it: it orders Leona's return home on a short transition schedule, with the exception packet left on file, unneeded, as the backstop it was built to be.",
], ending=True, debrief=[
 f"WHAT THE RECORD HELD (the hidden record, revealed): A summary phrase built from three entries, each documented wrong or lagging in the file's own paper. The arrearage accrued during two months of inpatient treatment while the plan's own note recorded the goal as paused. The \u2018missed payment\u2019 was a posting lag \u2014 receipt in the mother's folder, posting five days later in the system's own record. The benefits gap was caused by a closure letter mailed to her prior address after her move was on file. The audit assembled all three from the file's own documents \u2014 obtained on written request (55 Pa. Code \u00a7 3130.44(d)) \u2014 filed them entry by entry before the review, and filed a documented-exception packet as backstop before the fifteen-month date of {ASFA_STR} (entry {ENTRY_STR} plus fifteen calendar months, day {S116_ASFA_OFF} of this story).",
 "THE LAW UNDER THIS PATH: At the permanency review, counsel asked the court to correct each entry from the file's own documents before making the determinations a review court makes on the record before it (42 Pa.C.S. \u00a7 6351(f), including the placement-duration determination) \u2014 and a record whose three load-bearing entries were corrected could not carry the phrase built from them. The backstop was built on the federal filing rule's own discipline: at fifteen of the most recent twenty-two months the agency is generally to file unless an exception is documented (42 U.S.C. \u00a7 675(5)(E)) \u2014 relative care, a documented compelling reason, or services identified but not provided \u2014 and the exception is record-dependent, speaking to the filing decision only. It was never needed here, because the correction came first, at a review taken before the date. Counsel's role throughout is the verified one (42 Pa.C.S. \u00a7 6337). This ending is the scenario's win, labeled plainly: the line corrected entry by entry on the record, and reunification ordered on the corrected file \u2014 the record earned it, because every other element of the case (treatment, visits, work) was already documented as complete, and the only obstacle was three entries the file itself refuted.",
 "THE HONEST PART: The win is a corrected file and a transition home, not a verdict that the system worked. The pause was never carried across the file by the people who wrote both sections; the lag was nobody's fault and everybody's summary; the letter went to an empty apartment in a pattern this library has met before. A colder room could have corrected two entries and kept the phrase on the third; a later review slot would have let the date decide first; a supervisor reading a thinner file would have signed a different paper. Workers, judges, queues, and luck held pieces of this outcome. What your choices controlled was narrower and decisive: every entry was audited from documents, the audit was filed before the room that owned the phrase, and the backstop was filed before the date that owned the calendar.",
]),
N("end_one_entry", 66, "Ending \u2014 The Phrase Survives on One Entry", [
 "The review corrects what the packet documents, and the packet \u2014 for all its tabs \u2014 documents two entries completely and carries the third on account. The corrected entries fall cleanly: their exhibits are read, the corrections entered, the room nodding at paper it cannot argue with. Then the audit reaches the un-audited entry, and the room's temperature changes by exactly the temperature of missing paper. Counsel states it clearly. The summary states it in print. Print wins the tie it always wins.",
 "So the line is narrowed, not struck: re-entered in a shorter, surviving form, resting on the one entry that still wears its summarized shape. The case proceeds \u2014 toward home, on a longer road, with a review set to revisit the surviving entry \u2014 because partial paper partially works, in exact proportion. Two-thirds of a correction is a real correction. It is also a phrase, standing, in a file, being quoted while you read this.",
], ending=True, debrief=[
 "WHAT THE RECORD HELD (the hidden record, revealed): An audit with one tab carried by memory. The two documented entries were corrected on the record from the file's own paper \u2014 the room read the exhibits and entered the corrections itself. The third entry, true in every particular the mother could state, had no assembled document behind it: no plan page, no two-date exhibit, no envelope, depending on which tab was left unbuilt. The summary's phrase, deprived of two of its three sources, re-formed itself around the survivor, the way phrases do: shorter, weaker, and still the file's description of the mother's money.",
 "THE LAW UNDER THIS PATH: The instruments are the verified ones, and their use was simply incomplete. The file's pages were available on written request (55 Pa. Code \u00a7 3130.44(d)); counsel (42 Pa.C.S. \u00a7 6337) filed what was assembled and stated the rest, and a review court making its determinations on the record before it (42 Pa.C.S. \u00a7 6351(f)) corrected the entries the record documented and retained the one it did not. The documented-exception packet, if filed, still stands as backstop toward the fifteen-month date (42 U.S.C. \u00a7 675(5)(E)) \u2014 record-dependent, filing-decision only \u2014 but a corrected line was the stronger argument, and it needed all three tabs. Partial paper partially works; this ending is that sentence with its arithmetic shown.",
 "THE HONEST PART: Nothing here was lost by effort or by truth \u2014 the un-audited entry was as true as the other two, and its author can still assemble its document and file it for the next review, where the correction can be completed. What was lost was simultaneity: a phrase struck whole, at one review, on a truthful file, moves a case; a phrase narrowed keeps a foothold in every summary until it is finally dislodged. A room less patient with exhibits, or a worker who had carried her own pause note across her own file, changes this ending without the mother changing anything. It records the state of an audit \u2014 two tabs of documents, one tab of testimony \u2014 not the stability of a mother.",
]),
N("end_stands116", 66, "Ending \u2014 The Phrase Stands Whole", [
 "The review adopts the summary line the way reviews adopt most summary lines: without heat, without inquiry, as the ground on which the next determinations stand. \u2018Unresolved financial instability\u2019 remains the file's description of the mother's money \u2014 an arrearage, a missed payment, and a gap, listed in a row, unexamined \u2014 and the case that was preparing to move toward home is re-described, in the room's orders, as a case that will continue in placement while the \u2018instability\u2019 is \u2018addressed,\u2019 a word that now has to be lived under by a woman whose three money problems were a pause, a queue, and an envelope.",
 "Your accounts of the three entries were heard in order, in detail, in your own voice and counsel's. They were believed the way unaccompanied accounts are believed \u2014 personally, and set aside professionally \u2014 because the binder that would have proven them was never filed into the record the room was reading, in whatever posture it waits tonight: assembled in an office, or still scattered between a folder, a visit envelope, and a file across town.",
], ending=True, debrief=[
 f"WHAT THE RECORD HELD (the hidden record, revealed): One phrase and its three unexamined entries. The arrearage without the plan's pause note beside it. The missed payment without the posting record's second column. The gap without the closure letter's envelope. Each refuting document existed \u2014 the pause note in the agency's own plan, the lag in its own posting record, the wrong address in its own mailing record \u2014 and none of them was in front of the room, because the audit that would have assembled them was never filed, or never built from the record it needed. The fifteen-month date, {ASFA_STR}, now approaches a file whose settled description of the mother is the phrase itself.",
 "THE LAW UNDER THIS PATH: Every instrument that would have answered the phrase existed and is verified. The record \u2014 plan, ledger, posting record, correspondence \u2014 was available on written request (55 Pa. Code \u00a7 3130.44(d)). Counsel (42 Pa.C.S. \u00a7 6337) can assemble and file whatever paper exists. A review court's determinations are made on the record before it (42 Pa.C.S. \u00a7 6351(f)); a record that contains only a summary yields determinations that rest on the summary. And the federal date rewards documented exceptions only (42 U.S.C. \u00a7 675(5)(E)): an unfiled audit is not one. Defaults rule wherever documentation does not \u2014 that sentence, not any fact about this mother's money, is this ending.",
 "THE HONEST PART: Be clear, because the summary was not: the three entries were a treatment pause the plan itself recorded, a five-day posting queue, and a letter mailed to an apartment its own file knew she had left. Her finances, in the months this case actually examined, were the finances of a woman in ordered treatment who kept working, kept visiting, and kept receipts in a visit envelope. A worker who had read her own plan note beside her own ledger, a summary writer who read both columns \u2014 any of them changes this ending without her changing anything. It records a phrase's survival, not a mother's instability. And the binder can still be built tonight: paper assembled late corrects later reviews, slower and harder, but the plan page, the posting record, and the envelope have not stopped existing, and neither has the right to request them.",
]),
N("end_date", 66, "Ending \u2014 The Date Strikes First", [
 f"The later slot was calmer for everyone's schedule. That part was true. The rest arrives by mail, in the order the calendar always intended. First, the notice from the agency: Leona has now been in care for fifteen of the most recent twenty-two months \u2014 the date was {ASFA_STR} \u2014 and the agency has filed the petition the federal timeline points it toward, on the file as the date found it: a summary whose central phrase describes unresolved financial instability, three entries deep, uncorrected. A petition is not a termination; the agency would still have to prove its grounds clearly and convincingly at a hearing. But the weather of the case has changed, permanently, while the correction was still waiting for its calmer morning.",
 "Second, the audit itself \u2014 assembled or not, filed or not \u2014 now travels into a harder proceeding as an exhibit in a case about grounds, instead of doing its quieter, stronger work: correcting a summary at a review, before the date could read the summary as settled. Two clocks ran through this whole story. Only one of them was ever waiting for a convenient week.",
], ending=True, debrief=[
 f"THE BOARD, MAPPED \u2014 Review track: no review was held before the date; the correction of the summary line (flags: auditPacket, entry1Doc, entry2Doc, entry3Doc, if built) remains available for the proceedings ahead, intact and unspent. Placement track: Leona remained placed throughout, and her case acquired, on {ASFA_STR} \u2014 computed as entry {ENTRY_STR} plus fifteen calendar months \u2014 a termination petition that will now run on its own track, whether or not the audit later corrects every entry it was built from. ASFA track: struck on schedule at fifteen of the most recent twenty-two months (42 U.S.C. \u00a7 675(5)(E)); whether a documented exception was in the file (flag: exceptionPacket) is now the first argument in the case below, instead of the backstop it was filed to be.",
 "THE LAW UNDER THIS PATH: The exception framework is record-dependent in exactly the way this ending demonstrates: at the fifteen-month point, the filing decision is made from the file as it stands on the date \u2014 documented exceptions (relative care, a documented compelling reason, services identified but not provided) can answer it; undocumented truths, however complete in a binder across town, cannot. A petition, if filed, must still be proven by clear and convincing evidence at a hearing, and the audit's three corrections \u2014 the plan's pause note (the record itself being available on request, 55 Pa. Code \u00a7 3130.44(d)), the posting record, the mailing record \u2014 remain powerful paper in that proceeding, with counsel (42 Pa.C.S. \u00a7 6337) to carry them. Nothing about grounds has been decided. What was decided, by a calendar choice, was which proceeding the audit would debut in.",
 "THE HONEST PART: The later slot was offered by the system, in the same letter, in the same typeface, with no warning attached \u2014 the choice was real, and it was made inside a trap the letter did not label. Work that week was genuinely impossible; lives do not consult court calendars, and this debrief does not pretend otherwise. Judges' schedules, agencies' filings, and the date's indifference were never the mother's to control. What was hers was only the knowledge \u2014 delivered in this story on its fifth day, in pencil, on a desk calendar \u2014 of what the date would cost. This ending is not a judgment on a mother. It is a collision between two clocks, only one of which ever claimed to be waiting for her.",
]),
]

s116_meta = {"title": "The First 90 Days",
 "subtitle": "Scenario 116 \u2014 The Summary Line (a fictional composite)",
 "startDateISO": "2026-10-02", "startNode": "start", "startCash": 170,
 "tier": "Complex",
 "summary": "Month 14 of Leona's placement: one summary phrase \u2014 \u2018unresolved financial instability\u2019 \u2014 built from three money entries, each documented wrong or lagging in the file's own paper, stalls a case that was moving toward home."}

s116 = build(s116_meta, s116_nodes, S116_START)

S116_WIN_PATH = ["start","summary_line","counsel_meet","three_entries","folder_beat",
 "records_learn","records_fork","packet_arrives","audit_plan","binder_check","entry1_setup",
 "entry1_doc","treatment_dates","ledger_page","entry2_setup","entry2_doc","posting_office",
 "queue_explain","entry3_setup","entry3_doc","address_proof","summary_draft116","leona_visit","assembly116",
 "filed116","exception_beat","cold_read","review_prep116","calendar_choice",
 "morning116","review116","end_corrected116"]

# =====================================================================
if __name__ == "__main__":
    for scen, num, title, note, start, path, win in [
        (s114, 114, "The Ledger",
         "This scenario depicts a father in the twelve weeks before a permanency review of his young daughter's placement, documenting \u2014 in a notebook of fares, fees, and surrendered shift hours \u2014 two mornings when the system itself cancelled on him: a screen site closed for an unannounced holiday and a class cancelled by its provider. It is told through sign-in sheets, screen logs, and a notebook with receipts stapled in. There is no graphic content. Players may skip any scene or use the quick exit at any time.",
         S114_START, S114_WIN_PATH, "end_corrected"),
        (s115, 115, "Three Letters, Three Addresses",
         "This scenario depicts a mother whose twins are placed, untangling three letters from three systems that were mailed to three wrong addresses after she correctly filed an address update: a childcare closure, a benefits-case closure, and a housing-briefing invitation recorded as \u2018failed to attend.\u2019 It is told through letters, mailing records, and written trails. There is no graphic content. Players may skip any scene or use the quick exit at any time.",
         S115_START, S115_WIN_PATH, "end_restored_partial"),
        (s116, 116, "The Summary Line",
         "This scenario depicts a mother in month 14 of her daughter's placement, auditing \u2014 entry by entry, on paper \u2014 the three money entries behind a summary phrase, \u2018unresolved financial instability,\u2019 as the federal fifteen-month date approaches. It is told through ledgers, plan pages, posting records, and envelopes. There is no graphic content. Players may skip any scene or use the quick exit at any time.",
         S116_START, S116_WIN_PATH, "end_corrected116"),
    ]:
        emit(scen, num, title, note, start)
        walked, end_cash = walk_by_path(scen, path, win)
        print(f"Scenario {num}: {len(scen['nodes'])} nodes, "
              f"{sum(1 for n in scen['nodes'] if n.get('ending'))} endings; "
              f"win walk {len(walked)} nodes, end cash ${end_cash}")
        print("  path: " + " -> ".join(walked))
    print(f"S116 ASFA arithmetic: entry {ENTRY_STR} + 15 calendar months = "
          f"{ASFA_STR} (dayOffset {S116_ASFA_OFF} from start {fmt(S116_START)})")
