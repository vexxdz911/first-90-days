import json, datetime, re, sys
from collections import deque

def D(iso): return datetime.date.fromisoformat(iso)
def fmt(d): return d.strftime("%A, %B %-d, %Y")

def C(text, nxt, cash=None, flags=None, hidden=None, req=None, reqno=None, note=None):
    c = {"text": text, "next": nxt}
    if cash: c["cash"] = cash
    if flags: c["setFlags"] = flags
    if hidden: c["addHidden"] = hidden if isinstance(hidden, list) else [hidden]
    if req: c["requiresFlags"] = req
    if reqno: c["requiresNoFlags"] = reqno
    if note: c["note"] = note
    return c

def N(nid, off, title, body, choices=None, ending=False, debrief=None):
    n = {"id": nid, "dayOffset": off, "title": title, "body": body}
    if choices: n["choices"] = choices
    if ending:
        n["ending"] = True
        n["debrief"] = debrief
    return n

def build(scen):
    start = D(scen["startDateISO"])
    for n in scen["nodes"]:
        d = start + datetime.timedelta(days=n["dayOffset"])
        n["kicker"] = f"Day {n['dayOffset']} — {fmt(d)}"
        ordered = {"id": n["id"], "kicker": n["kicker"], "dayOffset": n["dayOffset"],
                   "title": n["title"], "body": n["body"]}
        if "choices" in n: ordered["choices"] = n["choices"]
        if n.get("ending"):
            ordered["ending"] = True; ordered["debrief"] = n["debrief"]
        n.clear(); n.update(ordered)
    meta = {"title": "The First 90 Days",
            "subtitle": f"Scenario {scen['num']} — {scen['name']} (a fictional composite)",
            "startDateISO": scen["startDateISO"], "startNode": "start",
            "startCash": scen["startCash"], "tier": scen["tier"], "summary": scen["summary"]}
    return {"meta": meta, "nodes": scen["nodes"]}

def eff_str(c):
    parts = []
    if c.get("cash"): parts.append(f"cash {'−' if c['cash']<0 else '+'}{abs(c['cash'])}")
    for f in c.get("setFlags", []): parts.append(f"FLAG: {f}")
    for h in c.get("addHidden", []): parts.append(f"HIDDEN + {h}")
    for f in c.get("requiresFlags", []): parts.append(f"REQUIRES FLAG: {f}")
    for f in c.get("requiresNoFlags", []): parts.append(f"REQUIRES NO FLAG: {f}")
    return " ; ".join(parts)

def script(scen, data):
    start = D(scen["startDateISO"])
    L = []
    L.append(f"# THE FIRST 90 DAYS — Scenario {scen['num']}: “{scen['name']}”")
    L.append("")
    L.append(f"*Human-readable script. This document and `scenario-{scen['num']}.json` are generated from a single source and match node-for-node: same IDs, same order, same choices, same effects.*")
    L.append("")
    L.append("**The family is fictional — a composite. No real person's story appears here.**")
    L.append("")
    L.append(f"**Content note:** {scen['contentNote']}")
    L.append("")
    L.append("**How to read effects:** `cash −40` changes the player's cash. `FLAG: name` sets a flag the engine tracks. `HIDDEN + item` means the case file quietly records that item at this choice — the player does not see it when it happens. `REQUIRES FLAG: name` means the choice is only available if that flag was set earlier; `REQUIRES NO FLAG: name` means it is only available if that flag was never set. `NOTE:` is text shown to the player right after choosing.")
    L.append("")
    L.append(f"Start date: {fmt(start)}. Day offsets are days since the scenario's start date{scen.get('offsetNote','')}.")
    for n in data["nodes"]:
        L.append("")
        L.append(f"## [{n['id']}] {n['title']}")
        L.append(f"*{n['kicker']} (dayOffset {n['dayOffset']})*")
        L.append("")
        for p in n["body"]:
            L.append(p); L.append("")
        if n.get("ending"):
            L.append("**Ending.**"); L.append("")
            L.append("**Debrief:**")
            for p in n["debrief"]:
                L.append(f"- {p}")
        else:
            L.append("**Choices:**")
            for c in n["choices"]:
                e = eff_str(c)
                L.append(f"- {c['text']} → **{c['next']}**" + (f"  _({e})_" if e else ""))
                if c.get("note"):
                    L.append(f"  - NOTE (shown after choosing): {c['note']}")
    return "\n".join(L) + "\n"

def _avail(c, flags):
    if c.get("requiresFlags") and not set(c["requiresFlags"]) <= flags: return False
    if c.get("requiresNoFlags") and set(c["requiresNoFlags"]) & flags: return False
    return True

def walk(data, win_id):
    nodes = {n["id"]: n for n in data["nodes"]}
    start = data["meta"]["startNode"]
    failed = set()
    def dfs(nid, flags, cash, path):
        if nid == win_id: return (path + [nid], cash)
        key = (nid, flags)
        if key in failed: return None
        chs = [c for c in nodes[nid].get("choices", []) if _avail(c, flags)]
        chs.sort(key=lambda c: (len(c.get("setFlags", [])), c.get("cash", 0)), reverse=True)
        for c in chs:
            r = dfs(c["next"], flags | set(c.get("setFlags", [])), cash + c.get("cash", 0), path + [nid])
            if r: return r
        failed.add(key)
        return None
    sys.setrecursionlimit(10000)
    return dfs(start, frozenset(), data["meta"]["startCash"], [])

def path_choices(data, path):
    nodes = {n["id"]: n for n in data["nodes"]}
    out = []
    for a, b in zip(path, path[1:]):
        for c in nodes[a].get("choices", []):
            if c["next"] == b:
                out.append((nodes[a], c)); break
    return out

def validate(num, data, corpus_names):
    errs = []
    nodes = {n["id"]: n for n in data["nodes"]}
    if len(nodes) != len(data["nodes"]): errs.append("duplicate node ids")
    for n in data["nodes"]:
        for c in n.get("choices", []):
            if c["next"] not in nodes: errs.append(f"{n['id']}: bad next {c['next']}")
        if n.get("ending") and n.get("choices"): errs.append(f"{n['id']}: ending has choices")
        if n.get("ending") and not n.get("debrief"): errs.append(f"{n['id']}: ending no debrief")
        if not n.get("ending") and not n.get("choices"): errs.append(f"{n['id']}: dead non-ending")
    reach = set(); dq = deque([data["meta"]["startNode"]])
    while dq:
        x = dq.popleft()
        if x in reach: continue
        reach.add(x)
        for c in nodes[x].get("choices", []): dq.append(c["next"])
    missing = set(nodes) - reach
    if missing: errs.append(f"unreachable: {missing}")
    start = data["meta"]["startNode"]
    def reaches(target):
        failed = set()
        def dfs(nid, fl):
            if nid == target: return True
            key = (nid, fl)
            if key in failed: return False
            for c in nodes[nid].get("choices", []):
                if not _avail(c, fl): continue
                if dfs(c["next"], fl | set(c.get("setFlags", []))): return True
            failed.add(key); return False
        return dfs(start, frozenset())
    sys.setrecursionlimit(10000)
    for n in data["nodes"]:
        if n.get("ending") and not reaches(n["id"]):
            errs.append(f"ending {n['id']} not reachable under gate-respecting search")
    for n in data["nodes"]:
        for c in n.get("choices", []):
            if nodes[c["next"]]["dayOffset"] < n["dayOffset"]:
                errs.append(f"offset decreases {n['id']}->{c['next']}")
    start_d = D(data["meta"]["startDateISO"])
    for n in data["nodes"]:
        d = start_d + datetime.timedelta(days=n["dayOffset"])
        if n["kicker"] != f"Day {n['dayOffset']} — {fmt(d)}":
            errs.append(f"{n['id']}: kicker mismatch")
    text = json.dumps(data)
    for nm in corpus_names:
        if re.search(rf"\b{re.escape(nm)}\b", text): errs.append(f"name collision with corpus: {nm}")
    return errs
