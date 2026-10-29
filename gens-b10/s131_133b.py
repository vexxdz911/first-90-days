# -*- coding: utf-8 -*-
from lib import C, N
from s131_133 import S131, S132, S133

PAPER = lambda nxt: [C("Do the paper version: dated, copied, filed", nxt, cash=-5, flags=["paperTrail"], hidden="Dated documentation added to the case record", note="Another dated page joins the folder."),
                     C("Handle it with a conversation and move on", nxt, note="Conversations end. The file keeps what it was given.")]

def idx(s, nid):
    return [i for i, n in enumerate(s["nodes"]) if n["id"] == nid][0]
def ins(s, after, node):
    s["nodes"].insert(idx(s, after) + 1, node)
def sett(s, nid, off=None, text=None):
    n = s["nodes"][idx(s, nid)]
    if off is not None: n["dayOffset"] = off
    if text is not None: n["_text"] = text
def setc(s, nid, ci, **kw):
    ch = s["nodes"][idx(s, nid)]["choices"][ci]
    for k, v in kw.items():
        if k == "flags": ch["setFlags"] = sorted(set(ch.get("setFlags", [])) | set(v))
        elif k == "req": ch["requiresFlags"] = v
        elif k == "reqno": ch["requiresNoFlags"] = v
        else: ch[k] = v
def chain(s, after_id, nodes):
    tail = s["nodes"][idx(s, after_id)]["choices"][0]["next"]
    for n in nodes[:-1]:
        n["choices"] = [C("Carry the page to its file", nodes[nodes.index(n) + 1]["id"], cash=-5, flags=["paperTrail"], hidden="Dated documentation added to the record", note="The chain holds because every link is dated.")]
    nodes[-1]["choices"] = [C("Carry the page to its file", tail, cash=-5, flags=["paperTrail"], hidden="Dated documentation added to the record", note="The chain holds because every link is dated.")]
    for j, n in enumerate(nodes):
        ins(s, after_id if j == 0 else nodes[j - 1]["id"], n)

def expand131(s):
    # study_winter between study131 and packets131
    ins(s, "study131", N("study_winter", 262, "The Winter of Two Bedtimes", [
        "December splits the children's evenings between Selene's house and their placements' trial overnights, a geography of toothbrushes in three bathrooms. The log — the one document that has followed both children everywhere — records it all without commentary, which is what logs are for.",
        "Ms. Onyema reads a page and says the sentence the winter deserves: 'This is what a family looks like when it refuses to let two files raise two strangers.'"],
        PAPER("packets131")))
    # fall_reviews between gap_both (spring) and the June Bureau hearing
    ins(s, "gap_both", N("fall_reviews", 118, "The Reviews Before the Hearing", [
        "May's reviews, one per child, rehearse June: Teo's judge notes the appeal pending and says nothing more about it — its own building, its own burden — while Cosette's commends the corrected file by name, an eight-year-old's nine days entered into a court record as a lesson in proofreading with consequences.",
        "The Bureau's hearing notice is already in the folder. The spring's last job is the witness list, filed in both tracks, so no June morning begins with a missing name."],
        PAPER("appeal_hearing131")))
    # trap wiring
    s["nodes"][idx(s, "packets131")]["choices"].append(
        C("File one blended family packet covering both children and rest", "end_one_clock", note="One packet, two clocks — and one child's exception blurred past reading. The blended file is where the marathon is lost."))
    s["nodes"][idx(s, "review131")]["choices"].append(
        C("Accept the agency's split proposal: Teo home now, Cosette's goal revisited in the fall", "end_split131", note="A split offered in January is a split that lasts. The board was built to refuse it politely, with paper."))

def expand132(s):
    ins(s, "refresh_indexed", N("winter_a132", 33, "The Winter Choir", [
        "The refreshed record's winter pages confirm the inventory: the treatment provider's mid-course letter, already filed, already dated, saying the unspectacular things mid-course letters say — attendance, engagement, prognosis guarded and good.",
        "Choruses are built a voice at a time. This one joins the folder without ceremony, which is its credibility."],
        [C("File it and note its date in the inventory", "winter_b132", flags=["paperTrail"], hidden="Mid-course treatment letter confirmed in the refreshed record", note="A voice, dated. The choir assembles.")]))
    ins(s, "winter_a132", N("winter_b132", 36, "The Employer's Page", [
        "Your employer's accommodation schedule — the warehouse's letter, revised after the accident, moving you to the day crew permanently — is re-filed in its current form, because hearings read the version in the packet, not the version in your memory of HR's kindness.",
        "Current versions only, from here to the hearing. The inventory now says so at the top, in Mr. Baptiste's hand."],
        PAPER("chorus")))
    # production choice 0 also sets recordsRequested (the winter record is in the inventory)
    setc(s, "production", 0, flags=["recordsRequested"])
    # trap wiring at the hearing
    s["nodes"][idx(s, "hearing132")]["choices"].append(
        C("Press for return while conceding October needs explaining later", "end_contested132", reqno=["gapCured"], note="Later is the contested hearing's home address. October, unanswered, becomes the day."))
    s["nodes"][idx(s, "hearing132")]["choices"].append(
        C("Ask for a continuance to perfect the packet — a month can only help", "end_clock132", note="A month helps the clock, not the case. November 4 does not continue itself."))

def expand133(s):
    ins(s, "roster", N("winter_roster", 36, "The Roster's Quiet Weeks", [
        "February and March pass without a roster event, which is the roster working as designed: coverage so ordinary it generates no paper, the plan's least visible success. You log the ordinary weeks anyway, one line each, because the file cannot tell the difference between a quiet month and a missing one.",
        "Sabine, reading over your shoulder, approves the method: 'Even nothing, dated.' The family is converging on a philosophy."],
        PAPER("receipt_filed")))
    chain(s, "exhibits133", [
        N("prep_a133", 60, "The Officer's Likely Questions", [
            "Preparation turns to the hearing officer's likely questions, each answered by a document before it is answered by a voice: how long, who else was home, what the building's emergency actually was. The answers exist. They are exhibits.",
            "Ms. Whitaker's rule for the room: never say in June what a page can say from March."],
            []),
        N("prep_b133", 65, "The Neighbor's Statement, Signed", [
            "The neighbor across the hall — the one whose emergency opened your door to the police — signs her statement: the entry was for her unit, the boy was found asleep, the officer asked about the pharmacy and she heard 'twenty minutes, maybe.' Her maybe is honest. Your receipt is exact. Together they are devastating.",
            "She signs in Sabine's kitchen, over coffee, like a person returning something borrowed."],
            []),
        N("prep_c133", 68, "The Packet, Numbered", [
            "The appeal packet is numbered the way exhibits prefer: receipt first, incident report second, statement third, timeline as the cover — four pages that tell the night in the order it happened, which is the order summaries never use.",
            "Numbered, copied, filed. June is now a reading, and readings favor the prepared."],
            []),
    ])
    chain(s, "decision133", [
        N("carry_a133", 185, "The Order, Carried", [
            "The expungement order is copied for the dependency file the same week it arrives — not because the court asked, but because paper does not walk between buildings, and this family has appointed itself the corridor in three cases now.",
            "The clerk stamps it. The dependency file's next reader will meet the registry's answer before forming the registry's assumption."],
            []),
        N("carry_b133", 205, "The Endgame, Proposed on Paper", [
            "The endgame proposal goes in as a document, not a hope: trial return in the fall, respite in writing, closure at the new year — three dates with a family's whole table behind them.",
            "Proposals on paper get answered on paper. The agency's response, when it comes, concurs in a paragraph — the system's way of applauding."],
            []),
    ])

expand131(S131); expand132(S132); expand133(S133)
