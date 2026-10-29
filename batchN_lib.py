#!/usr/bin/env python3
"""Shared library for Wave 2 Batch 9 (Scenarios 117-126, Education & Medical)
of 'The First 90 Days' — follows the Wave 1 generator pattern
(see generate-scenarios-47-56.py). Fictional composites only."""
import json
from datetime import date, timedelta

GAME_DIR = "/home/hatch/workspace/your_files/tacticwatch-game"

def fmt(d):
    return d.strftime("%A, %B %-d, %Y")

def build(meta, raw_nodes, start):
    nodes = []
    for nd in raw_nodes:
        d = start + timedelta(days=nd["off"])
        item = {"id": nd["id"],
                "kicker": f"Day {nd['off']} — {fmt(d)}",
                "dayOffset": nd["off"],
                "title": nd["title"]}
        if nd.get("ending"):
            item["ending"] = True
            item["body"] = []
            item["debrief"] = nd["debrief"]
        else:
            item["body"] = nd["body"]
            item["choices"] = nd["choices"]
        nodes.append(item)
    return {"meta": meta, "nodes": nodes}

def N(id, off, title, body, choices):
    return {"id": id, "off": off, "title": title, "body": body, "choices": choices}

def C(text, next, **fx):
    c = {"text": text, "next": next}
    c.update(fx)
    return c

def E(id, off, title, debrief):
    return {"id": id, "off": off, "title": title, "ending": True, "debrief": debrief}

def effect_str(c):
    parts = []
    if c.get("cash"):
        parts.append(f"cash {'+' if c['cash'] > 0 else '−'}{abs(c['cash'])}")
    for f in c.get("setFlags", []):
        parts.append(f"FLAG: {f}")
    for h in c.get("addHidden", []):
        parts.append(f"HIDDEN + {h}")
    for f in c.get("requiresFlags", []):
        parts.append(f"REQUIRES: {f}")
    for f in c.get("requiresNoFlags", []):
        parts.append(f"REQUIRES-NOT: {f}")
    return "; ".join(parts)

def emit(n, meta, raw, start, content_note):
    raw = sorted(raw, key=lambda nd: nd["off"])   # house rule: file order is offset order
    data = build(meta, raw, start)
    json_path = f"{GAME_DIR}/scenario-{n}.json"
    with open(json_path, "w") as f:
        json.dump(data, f, indent=2)
    L = []
    L.append(f"# {meta['subtitle'].split('— ', 1)[1]} — Node-for-Node Script (Scenario {n})")
    L.append("")
    L.append(f"Scenario {n} of *The First 90 Days* — script generated node-for-node from `scenario-{n}.json`; the JSON is the source of truth.")
    L.append("")
    L.append("A fictional composite built from published Pennsylvania dependency practice and documented system patterns. Not a real family's case.")
    L.append("")
    L.append(f"**Content note:** {content_note}")
    L.append("")
    L.append("**How to read effects:** `cash` is money spent or received at that choice; `FLAG:` marks a fact the story remembers; `HIDDEN +` is an assessment item the player never sees scored; `REQUIRES:` gates a choice on an earlier fact; `NOTE:` is authorial, not spoken in-world. Endings are marked **Ending.** with a **Debrief:**.")
    L.append("")
    L.append(f"**Start date:** {fmt(start)}. **Tier:** {meta['tier']}. **Start cash:** ${meta['startCash']}.")
    L.append("")
    L.append("---")
    for nd in data["nodes"]:
        L.append("")
        L.append(f"## [{nd['id']}] {nd['title']}")
        L.append("")
        L.append(f"*{nd['kicker']}*")
        if nd.get("ending"):
            L.append("")
            L.append("**Ending.**")
            for p in nd["debrief"]:
                L.append("")
                L.append(f"**Debrief:** {p}" if p is nd["debrief"][0] else p)
        else:
            for p in nd["body"]:
                L.append("")
                L.append(p)
            L.append("")
            L.append("**Choices:**")
            for c in nd["choices"]:
                fx = effect_str(c)
                line = f"- {c['text']} → **{c['next']}**"
                if fx:
                    line += f"  _({fx})_"
                L.append(line)
                if c.get("note"):
                    L.append(f"  - NOTE: {c['note']}")
    script_path = f"{GAME_DIR}/scenario-{n}-script.md"
    with open(script_path, "w") as f:
        f.write("\n".join(L) + "\n")
    ends = sum(1 for nd in data["nodes"] if nd.get("ending"))
    print(f"scenario {n}: {len(data['nodes'])} nodes, {ends} endings, tier {meta['tier']}")
    return data
