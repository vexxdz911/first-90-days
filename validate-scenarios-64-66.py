#!/usr/bin/env python3
"""Validation for Scenarios 64-66: parse, link resolution, reachability
(ignoring gates and gate-respecting state-space), ending form, dayOffset
monotonicity, kicker==computed date, in-body date recomputation, citation
sweep vs the verified set, cast sweep, script parity, worst-path cash,
win-walk verification (gates satisfied, cash never negative)."""
import json, os, re, sys
from collections import deque
from datetime import date, timedelta
from functools import lru_cache

D = os.path.dirname(os.path.abspath(__file__))
sys.setrecursionlimit(10000)

ALLOWED_CITES = {"42 Pa.C.S. \u00a7 6337", "42 Pa.C.S. \u00a7 6332(a)",
                 "55 Pa. Code \u00a7 3130.44(d)", "42 U.S.C. \u00a7 675(5)(E)"}
FORBIDDEN_NAMES = ["Christine", "Annie", "Camden", "May", "Roth", "Ransing",
                   "Noah", "Wren", "Marcus", "Dana", "Mara", "Eli ", "Osei",
                   "Whitaker", "Hartley"]
EXTRA_OK_DATES = {64: {date(2025, 11, 3), date(2027, 2, 3)}, 65: set(), 66: set()}

WIN_ROUTES = {
64: ["start","folder_inventory","counsel_meet","exception_explained","records_beat",
     "file_review","chronology_gaps","binder_begins","prog_beat","prog_letter",
     "bus_home64","therapy_beat","therapy_letter","housing_beat","housing_docs",
     "sandoval_call","gaplog_beat","screens_beat","work_beat64","review12_notice",
     "review12","amara_visit","folder_night64","agency_letter","counsel_packet",
     "packet_decision","packet_filed_scene","month13_work","foster_call",
     "review14_notice","review14","supervisor_change","filing_eve","morning_of",
     "filing_day","end_notfiled"],
65: ["start","separate_counsel","two_binders","paper_habits","calendar_beat",
     "deconflict_beat","reply_week","car_beat","bus_plan","screens_beat",
     "program_night","his_miss_setup","his_miss","reschedule_kept","her_report",
     "visit_makeup","makeup_outcome","records_beat65","file_arrives65",
     "kitchen_audit","her_note_his_file","two_desks","correction_beat","ack_beat",
     "joint_visit","note_followup","joint_letter_beat","work_beat65","money_beat65",
     "hattie_beat","prep_split","counsel_prep_her","counsel_prep_his",
     "reviews_week","end_two"],
66: ["start","intake_echo","program_rhythm","screens_routine","sponsor_beat",
     "visit_beat66a","employer_beat66","benefit_letter","counselor_talk",
     "call_insurer","appeal_info","summary_choice","discharge_day",
     "last_day_scene","coding_beat","worker_call","nakamura_meeting",
     "gap_explained","stepdown_beat","gap_week","gap_support","transport_beat66",
     "notify_beat","letter_to_file","records_beat66","coding_seen",
     "correction_beat66","hallway_beat66","dario_visit","dario_school",
     "stepdown_start","money_beat66","review_notice66","counsel_prep66",
     "review_prep_docs","eve_beat66","review66","end_summary"],
}
EXPECT = {64: (42, 4, "Ending \u2014 Not Filed: The Exception, Documented"),
          65: (38, 3, "Ending \u2014 Two Files, Two Records"),
          66: (40, 3, "Ending \u2014 The Summary Says Progress")}

def check(num):
    scen = json.load(open(os.path.join(D, f"scenario-{num}.json")))
    meta, nodes = scen["meta"], scen["nodes"]
    by = {n["id"]: n for n in nodes}
    assert len(by) == len(nodes), "duplicate ids"
    start = date.fromisoformat(meta["startDateISO"])
    exp_nodes, exp_ends, win_title = EXPECT[num]
    assert len(nodes) == exp_nodes, (num, len(nodes))
    # kicker correctness
    node_dates = set()
    for n in nodes:
        d = start + timedelta(days=n["dayOffset"])
        node_dates.add(d)
        want = f"Day {n['dayOffset']} \u2014 " + d.strftime("%A, %B ") + str(d.day) + d.strftime(", %Y")
        assert n["kicker"] == want, (n["id"], n["kicker"], want)
        if num == 64 and n["id"] == "end_notfiled":
            pass  # endings may lead with fixed lead-in instead of pattern
        else:
            assert n["kicker"] == want, (n["id"], n["kicker"], want)
    # links + monotonicity
    for n in nodes:
        for c in n.get("choices", []):
            assert c["next"] in by, (n["id"], c["next"])
            assert by[c["next"]]["dayOffset"] >= n["dayOffset"], ("offset decrease", n["id"], c["next"])
    # reachability ignoring gates
    seen, q = set(), deque([meta["startNode"]])
    while q:
        x = q.popleft()
        if x in seen: continue
        seen.add(x)
        q.extend(c["next"] for c in by[x].get("choices", []))
    assert seen == set(by), ("unreachable", set(by) - seen)
    # endings form
    ends = [n for n in nodes if n.get("ending")]
    assert len(ends) == exp_ends
    for e in ends:
        assert not e.get("choices") and e.get("debrief") and 3 <= len(e["debrief"]) <= 4, e["id"]
        assert e["body"], e["id"]
    for n in nodes:
        if not n.get("ending"):
            assert n.get("choices"), n["id"]
    # flags
    flags = {f for n in nodes for c in n.get("choices", []) for f in c.get("setFlags", [])}
    assert "recordsRequested" in flags and "removed" not in flags, flags
    # gate-respecting state-space reachability of every ending
    states, q = set(), deque()
    q.append((meta["startNode"], frozenset()))
    reached_endings = set()
    while q:
        nid, fl = q.popleft()
        if (nid, fl) in states: continue
        states.add((nid, fl))
        n = by[nid]
        if n.get("ending"):
            reached_endings.add(nid); continue
        for c in n.get("choices", []):
            if set(c.get("requiresFlags", [])) <= fl and not (set(c.get("requiresNoFlags", [])) & fl):
                q.append((c["next"], fl | frozenset(c.get("setFlags", []))))
    assert reached_endings == {e["id"] for e in ends}, (num, reached_endings)
    # worst-path cash
    @lru_cache(maxsize=None)
    def worst(nid):
        n = by[nid]
        if n.get("ending"): return 0
        return min(c.get("cash", 0) + worst(c["next"]) for c in n["choices"])
    w = worst(meta["startNode"])
    assert meta["startCash"] + w >= 0, ("cash negative on some path", w)
    # hidden items
    hidden = {h for n in nodes for c in n.get("choices", []) for h in c.get("addHidden", [])}
    # in-body stated dates recomputed
    ok_dates = node_dates | EXTRA_OK_DATES[num]
    text_all = []
    for n in nodes:
        text_all += n["body"] + n.get("debrief", [])
        text_all += [c.get("note", "") for c in n.get("choices", [])]
    months = "January|February|March|April|May|June|July|August|September|October|November|December"
    found_dates = set()
    for t in text_all:
        for m in re.finditer(rf"(?:({months}) (\d{{1,2}}), (\d{{4}}))", t):
            d = date(int(m.group(3)), ["January","February","March","April","May","June","July",
                     "August","September","October","November","December"].index(m.group(1)) + 1,
                     int(m.group(2)))
            found_dates.add(d)
            assert d in ok_dates, (num, "stated date not a node/ASFA/placement date", d)
    # citation sweep
    joined = "\n".join(text_all)
    cites = set(re.findall(r"\d+ (?:Pa\.C\.S\.|Pa\. Code|U\.S\.C\.) \u00a7 [0-9.]+(?:\([a-zA-Z0-9]+\))*", joined))
    bad = {c for c in cites if c not in ALLOWED_CITES}
    assert not bad, (num, "unverified citations", bad)
    assert not re.search(r"\bAI\b|machine learning|predictive", joined), (num, "assessment naming")
    for name in FORBIDDEN_NAMES:
        assert name not in joined, (num, "forbidden/other-scenario name present", name)
    # script parity
    md = open(os.path.join(D, f"scenario-{num}-script.md")).read()
    ids_md = re.findall(r"^## \[([^\]]+)\] ", md, re.M)
    assert ids_md == [n["id"] for n in nodes], "script id order mismatch"
    print(f"scenario-{num}: PASS nodes={len(nodes)} endings={len(ends)} "
          f"flags={sorted(flags)} hiddenDistinct={len(hidden)} "
          f"worstPathDelta={w} minBalance={meta['startCash']+w} "
          f"statedDatesChecked={len(found_dates)} citations={sorted(cites)}")
    return scen, by

def walk(num, by, meta):
    route = WIN_ROUTES[num]
    assert route[0] == meta["startNode"]
    cash, flags = meta["startCash"], set()
    for a, b in zip(route, route[1:]):
        edges = [c for c in by[a].get("choices", []) if c["next"] == b]
        assert edges, f"scenario-{num}: no edge {a} -> {b}"
        c = edges[0]
        assert set(c.get("requiresFlags", [])) <= flags, (num, a, "gate unmet", c.get("requiresFlags"), flags)
        assert not (set(c.get("requiresNoFlags", [])) & flags), (num, a, "negative gate violated")
        cash += c.get("cash", 0)
        assert cash >= 0, (num, a, "cash negative", cash)
        flags |= set(c.get("setFlags", []))
    end = by[route[-1]]
    assert end.get("ending") and end["title"] == EXPECT[num][2], (num, end["title"])
    assert "recordsRequested" in flags, (num, "win route lacks recordsRequested")
    guide = open(os.path.join(D, f"strategy-{num}.md")).read()
    assert end["title"] in guide, f"strategy-{num} does not name win ending"
    for nid in route:
        assert by[nid]["title"] in guide, f"strategy-{num} missing node title {by[nid]['title']}"
    print(f"scenario-{num}: WIN WALK PASS nodesVisited={len(route)} endCash={cash} "
          f"flagsAtEnd={sorted(flags)}")
    print(f"  path: {' -> '.join(route)}")
    return len(route), cash

if __name__ == "__main__":
    scens = {}
    for num in (64, 65, 66):
        scens[num] = check(num)
    for num in (64, 65, 66):
        walk(num, scens[num][1], scens[num][0]["meta"])
    print("ALL VALIDATION PASSED")
