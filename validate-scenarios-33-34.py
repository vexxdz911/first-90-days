#!/usr/bin/env python3
"""Validation for Scenarios 33 & 34: parse, link resolution, BFS reachability,
ending form, dayOffset monotonicity along every edge, kicker==computed date,
script<->JSON node-for-node match, counts, flag rules, worst-path cash."""
import json, os, re
from collections import deque
from datetime import date, timedelta

D = os.path.dirname(os.path.abspath(__file__))

def check(num, expect_removed):
    scen = json.load(open(os.path.join(D, f"scenario-{num}.json")))
    meta, nodes = scen["meta"], scen["nodes"]
    by = {n["id"]: n for n in nodes}
    assert len(by) == len(nodes), "duplicate ids"
    start = date.fromisoformat(meta["startDateISO"])
    # kicker correctness
    for n in nodes:
        d = start + timedelta(days=n["dayOffset"])
        want = f"Day {n['dayOffset']} \u2014 " + d.strftime("%A, %B ") + str(d.day) + d.strftime(", %Y")
        assert n["kicker"] == want, (n["id"], n["kicker"], want)
    # links + monotonicity
    for n in nodes:
        for c in n.get("choices", []):
            assert c["next"] in by, (n["id"], c["next"])
            assert by[c["next"]]["dayOffset"] >= n["dayOffset"], ("offset decrease", n["id"], c["next"])
    # BFS
    seen, q = set(), deque([meta["startNode"]])
    while q:
        x = q.popleft()
        if x in seen: continue
        seen.add(x)
        q.extend(c["next"] for c in by[x].get("choices", []))
    assert seen == set(by), ("unreachable", set(by) - seen)
    # endings
    ends = [n for n in nodes if n.get("ending")]
    for e in ends:
        assert e["body"] == [] and not e.get("choices") and e.get("debrief"), e["id"]
    for n in nodes:
        if not n.get("ending"):
            assert n.get("choices"), n["id"]
    assert 32 <= len(nodes) <= 45, len(nodes)
    assert 3 <= len(ends) <= 4, len(ends)
    # flags
    flags = {f for n in nodes for c in n.get("choices", []) for f in c.get("setFlags", [])}
    assert "recordsRequested" in flags
    if expect_removed: assert "removed" in flags
    else: assert "removed" not in flags
    # worst-path cash (graph is a DAG by non-decreasing offset + finite design; DP with memo, cycle guard)
    from functools import lru_cache
    import sys; sys.setrecursionlimit(10000)
    @lru_cache(maxsize=None)
    def worst(nid):
        n = by[nid]
        if n.get("ending"): return 0
        return min((c.get("cash", 0) + worst(c["next"])) for c in n["choices"])
    w = worst(meta["startNode"])
    assert meta["startCash"] + w >= 0, ("cash goes negative", w)
    # script match
    md = open(os.path.join(D, f"scenario-{num}-script.md")).read()
    ids_md = re.findall(r"^## \[([^\]]+)\] ", md, re.M)
    assert ids_md == [n["id"] for n in nodes], "script id order mismatch"
    for n in nodes:
        for c in n.get("choices", []):
            assert f"\u2192 **{c['next']}**" in md
    print(f"scenario-{num}: PASS nodes={len(nodes)} endings={len(ends)} "
          f"flags={sorted(flags)} worstPathCashDelta={w} startCash={meta['startCash']} "
          f"minBalance={meta['startCash']+w} titles={[e['title'] for e in ends]}")
    return scen

if __name__ == "__main__":
    check(33, expect_removed=False)
    check(34, expect_removed=True)
    print("ALL VALIDATION PASSED")
