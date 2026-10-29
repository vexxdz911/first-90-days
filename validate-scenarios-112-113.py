#!/usr/bin/env python3
"""Validation for Scenarios 112-113: parse, link resolution, reachability
(ignoring gates and gate-respecting state-space), ending form, dayOffset
monotonicity along EVERY edge, kicker==computed date, in-body date
recomputation, ASFA machine audit, citation sweep vs the verified set,
term scan, name-collision grep, script parity, worst-path cash,
win-walk verification (gates satisfied earlier, cash never negative,
guide names win title + every walked node title)."""
import json, os, re, sys
from collections import deque
from datetime import date, timedelta
from functools import lru_cache

D = os.path.dirname(os.path.abspath(__file__))
sys.setrecursionlimit(10000)

# Verified law set for this part (bases + the exact forms used)
ALLOWED_BASES = {"42 Pa.C.S. § 6337", "42 Pa.C.S. § 6332",
                 "42 Pa.C.S. § 6351", "23 Pa.C.S. § 6341",
                 "55 Pa. Code § 3130.44", "42 U.S.C. § 675(5)(E)",
                 "23 Pa.C.S. § 6315", "42 Pa.C.S. § 6336.1",
                 "42 Pa.C.S. § 6302", "55 Pa. Code § 3130.44(d)",
                 "55 Pa. Code § 3130.44(f)"}
ALLOWED_FULL = {"42 Pa.C.S. § 6337", "42 Pa.C.S. § 6332(a)",
                "55 Pa. Code § 3130.44(d)", "55 Pa. Code § 3130.44(f)",
                "42 U.S.C. § 675(5)(E)",
                "42 Pa.C.S. § 6351(e)(3)(i)", "42 Pa.C.S. § 6351(f)",
                "42 Pa.C.S. § 6351(f)(1)", "42 Pa.C.S. § 6351(a)",
                "42 Pa.C.S. § 6351(b)", "42 Pa.C.S. § 6351(f)(9)",
                "42 Pa.C.S. § 6351(f.1)"}
PRINCIPALS = {112: ["Bernice", "Joaquin", "Mireya", "Dena"],
              113: ["Farida", "Umar"]}
ENTRY = {112: date(2025, 10, 20), 113: date(2025, 3, 3)}
PACKET112 = date(2025, 10, 24)
ASFA = {112: date(2027, 1, 20), 113: date(2026, 6, 3)}
EXTRA_OK = {112: {ENTRY[112], PACKET112, ASFA[112]},
            113: {ENTRY[113], ASFA[113]}}
EXPECT = {112: (40, 4, "Ending \u2014 Payments Begin, and the File Tells the Truth (PARTIAL)"),
          113: (40, 4, "Ending \u2014 Documented: The Goal Stays Home (PARTIAL)")}
WIN_END = {112: "end_win", 113: "end_win113"}

def add_months(d, months):
    m = d.month - 1 + months
    y = d.year + m // 12
    m = m % 12 + 1
    days_in = [31, 29 if (y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)) else 28,
               31, 30, 31, 30, 31, 31, 30, 31, 30, 31][m - 1]
    return date(y, m, min(d.day, days_in))

def check(num):
    scen = json.load(open(os.path.join(D, f"scenario-{num}.json")))
    meta, nodes = scen["meta"], scen["nodes"]
    by = {n["id"]: n for n in nodes}
    assert len(by) == len(nodes), "duplicate ids"
    assert meta["tier"] == "Complex" and meta["startCash"] == 170
    start = date.fromisoformat(meta["startDateISO"])
    exp_nodes, exp_ends, win_title = EXPECT[num]
    assert len(nodes) == exp_nodes, (num, len(nodes))
    assert 36 <= len(nodes) <= 48
    # ASFA machine audit
    assert add_months(ENTRY[num], 15) == ASFA[num], (num, "ASFA arithmetic")
    if num == 113:
        assert (ASFA[113] - start).days == 61
        fd = by["filing_day"]
        assert fd["dayOffset"] == 61, fd["dayOffset"]
        assert fd["kicker"] == "Day 61 \u2014 Wednesday, June 3, 2026", fd["kicker"]
    # kicker correctness
    node_dates = set()
    for n in nodes:
        d = start + timedelta(days=n["dayOffset"])
        node_dates.add(d)
        want = f"Day {n['dayOffset']} \u2014 " + d.strftime("%A, %B ") + str(d.day) + d.strftime(", %Y")
        assert n["kicker"] == want, (n["id"], n["kicker"], want)
    # links + monotonicity along EVERY edge
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
        assert not e.get("choices") and e.get("debrief") and len(e["debrief"]) >= 3, e["id"]
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
    # in-body stated dates recomputed
    ok_dates = node_dates | EXTRA_OK[num]
    text_all = []
    for n in nodes:
        text_all += n["body"] + n.get("debrief", [])
        text_all += [c.get("note", "") for c in n.get("choices", [])]
        text_all += [c["text"] for c in n.get("choices", [])]
    months = "January|February|March|April|May|June|July|August|September|October|November|December"
    found_dates = set()
    for t in text_all:
        for m in re.finditer(rf"(?:({months}) (\d{{1,2}}), (\d{{4}}))", t):
            d = date(int(m.group(3)), ["January","February","March","April","May","June","July",
                     "August","September","October","November","December"].index(m.group(1)) + 1,
                     int(m.group(2)))
            found_dates.add(d)
            assert d in ok_dates, (num, "stated date not a node/ASFA/entry/packet date", d, t[:90])
    # citation sweep vs verified set
    joined = "\n".join(text_all)
    cites = set(re.findall(r"\d+ (?:Pa\.C\.S\.|Pa\. Code|U\.S\.C\.) \u00a7 [0-9.]+(?:\([a-zA-Z0-9.]+\))*", joined))
    bad = set()
    for ctext in cites:
        if ctext in ALLOWED_FULL: continue
        base = re.match(r"(\d+ (?:Pa\.C\.S\.|Pa\. Code|U\.S\.C\.) \u00a7 [0-9.]+)", ctext).group(1)
        if base not in ALLOWED_BASES: bad.add(ctext)
    assert not bad, (num, "unverified citations", bad)
    # term scan
    assert not re.search(r"\bAI\b|machine learning|predictive", joined), (num, "assessment naming")
    # principal names present; private-orbit names absent
    for name in PRINCIPALS[num]:
        assert name in joined, (num, "principal missing", name)
    for name in ["Christine", "Annie Roth", "Camden", "Ransing"]:
        assert name not in joined, (num, "private-orbit name present", name)
    # script parity
    md = open(os.path.join(D, f"scenario-{num}-script.md")).read()
    assert "The family is fictional \u2014 a composite. No real person's story appears here." in md
    assert "**Content note:**" in md
    ids_md = re.findall(r"^## \[([^\]]+)\] ", md, re.M)
    assert ids_md == [n["id"] for n in nodes], "script id order mismatch"
    print(f"scenario-{num}: PASS nodes={len(nodes)} endings={len(ends)} "
          f"flags={sorted(flags)} worstPathDelta={w} minBalance={meta['startCash']+w} "
          f"statedDatesChecked={len(found_dates)} citations={sorted(cites)}")
    print(f"  ASFA audit: entry {ENTRY[num]} + 15 months = {ASFA[num]} "
          f"({'filing_day at offset 61' if num == 113 else 'outside window, not depicted'})")
    return scen, by

def walk(num, by, meta):
    # import the win maps from the generator by re-deriving via strategy guide check:
    # walk using the generator module's recorded routes is done in the generator;
    # here we re-walk by importing the generator file as data.
    import importlib.util
    spec = importlib.util.spec_from_file_location("gen112113", os.path.join(D, "generate-scenarios-112-113.py"))
    mod = importlib.util.module_from_spec(spec)
    import io, contextlib
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(mod)  # __main__ guard prevents re-emit
    win = mod.s112_win if num == 112 else mod.s113_win
    route, cur = [], meta["startNode"]
    cash, flags = meta["startCash"], set()
    while True:
        route.append(cur)
        node = by[cur]
        if node.get("ending"):
            break
        text = win[cur]
        c = next(cc for cc in node["choices"] if cc["text"] == text)
        assert set(c.get("requiresFlags", [])) <= flags, (num, cur, "gate unmet")
        assert not (set(c.get("requiresNoFlags", [])) & flags), (num, cur, "negative gate violated")
        cash += c.get("cash", 0)
        assert cash >= 0
        flags |= set(c.get("setFlags", []))
        cur = c["next"]
    end = by[route[-1]]
    assert end["id"] == WIN_END[num] and end["title"] == EXPECT[num][2], (num, end["title"])
    assert "recordsRequested" in flags
    guide = open(os.path.join(D, f"strategy-{num}.md")).read()
    assert end["title"] in guide, f"strategy-{num} does not name win ending exactly"
    for nid in route:
        assert by[nid]["title"] in guide, f"strategy-{num} missing node title {by[nid]['title']}"
    src = open(os.path.join(D, f"sources-part-M-c.md")).read()
    assert f"SCENARIO {num}" in src
    print(f"scenario-{num}: WIN WALK PASS nodesVisited={len(route)} endCash={cash} flagsAtEnd={sorted(flags)}")
    print(f"  path: {' -> '.join(route)}")
    return len(route), cash

def name_collision():
    import glob
    others = [f for f in glob.glob(os.path.join(D, "scenario-*.json"))
              if not f.endswith(("scenario-112.json", "scenario-113.json"))]
    others += [f for f in glob.glob(os.path.join(D, "strategy-*.md"))
               if not f.endswith(("strategy-112.md", "strategy-113.md"))]
    blob = ""
    for f in others:
        blob += open(f, encoding="utf-8", errors="ignore").read()
    for name in ["Bernice", "Joaquin", "Mireya", "Farida", "Umar"]:
        assert not re.search(rf"\b{name}\b", blob), ("name collision", name)
    print("name-collision grep: PASS (Bernice/Joaquin/Mireya/Farida/Umar absent from all other scenario-*.json/strategy-*.md)")
    # Dena checked as a standalone principal token against other scenarios too
    hits = [f for f in others if re.search(r"\bDena\b", open(f, encoding="utf-8", errors="ignore").read())]
    print(f"  Dena standalone-token files elsewhere: {[os.path.basename(h) for h in hits]}")

if __name__ == "__main__":
    scens = {}
    for num in (112, 113):
        scens[num] = check(num)
    for num in (112, 113):
        walk(num, scens[num][1], scens[num][0]["meta"])
    name_collision()
    print("ALL VALIDATION PASSED")
