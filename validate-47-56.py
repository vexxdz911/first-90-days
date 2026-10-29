#!/usr/bin/env python3
"""Validate scenarios 47-56: structure, dates, parity, citations, names, routes."""
import json, re, subprocess, sys
from datetime import date, timedelta
from pathlib import Path

G = Path("/home/hatch/workspace/your_files/tacticwatch-game")
BANDS = {47: ("Foundation", 16, 22, 2), 48: ("Foundation", 16, 22, 2),
         49: ("Hard", 24, 34, 3), 50: ("Hard", 24, 34, 3), 51: ("Hard", 24, 34, 3),
         52: ("Hard", 24, 34, 3), 53: ("Complex", 36, 48, None), 54: ("Complex", 36, 48, None),
         55: ("Complex", 36, 48, None), 56: ("Complex", 36, 48, None)}
fails = []

def fmt(d):
    return d.strftime("%A, %B %-d, %Y")

def load(n):
    return json.loads((G / f"scenario-{n}.json").read_text())

def check(cond, msg):
    if not cond:
        fails.append(msg)
    return cond

for n in range(47, 57):
    tier, lo, hi, nends = BANDS[n]
    data = load(n)
    meta, nodes = data["meta"], data["nodes"]
    ids = [nd["id"] for nd in nodes]
    check(len(ids) == len(set(ids)), f"S{n}: duplicate node ids")
    check(meta["tier"] == tier, f"S{n}: tier {meta['tier']} != {tier}")
    check(lo <= len(nodes) <= hi, f"S{n}: {len(nodes)} nodes outside band {lo}-{hi}")
    ends = [nd for nd in nodes if nd.get("ending")]
    if nends:
        check(len(ends) == nends, f"S{n}: {len(ends)} endings != {nends}")
    else:
        check(3 <= len(ends) <= 4, f"S{n}: {len(ends)} endings outside 3-4")
    idset = set(ids)
    start = date.fromisoformat(meta["startDateISO"])
    prev = -1
    for nd in nodes:
        check(nd["dayOffset"] >= prev, f"S{n}: dayOffset decreases at {nd['id']}")
        prev = nd["dayOffset"]
        want = f"Day {nd['dayOffset']} — {fmt(start + timedelta(days=nd['dayOffset']))}"
        check(nd["kicker"] == want, f"S{n}: kicker mismatch at {nd['id']}: {nd['kicker']!r} != {want!r}")
        if nd.get("ending"):
            check(nd["title"].startswith("Ending — "), f"S{n}: ending title style at {nd['id']}")
            check(len(nd.get("debrief", [])) >= 2, f"S{n}: debrief <2 paras at {nd['id']}")
            check(nd.get("body") == [], f"S{n}: ending body not [] at {nd['id']}")
        else:
            check(len(nd.get("body", [])) >= 1, f"S{n}: empty body at {nd['id']}")
            check(len(nd.get("choices", [])) >= 1, f"S{n}: no choices at {nd['id']}")
            for c in nd["choices"]:
                check(c["next"] in idset, f"S{n}: dangling next {c['next']} from {nd['id']}")
    # reachability
    adj = {nd["id"]: [c["next"] for c in nd.get("choices", [])] for nd in nodes}
    seen, stack = set(), [meta["startNode"]]
    while stack:
        x = stack.pop()
        if x in seen: continue
        seen.add(x); stack.extend(adj.get(x, []))
    check(seen == idset, f"S{n}: unreachable nodes {sorted(idset - seen)}")
    # script parity
    script = (G / f"scenario-{n}-script.md").read_text()
    heads = re.findall(r"^## \[([^\]]+)\] ", script, re.M)
    check(heads == ids, f"S{n}: script headers != JSON node order")
    # win ending: recordsRequested must be settable on some route (flag exists in choices)
    allflags = set()
    for nd in nodes:
        for c in nd.get("choices", []):
            allflags.update(c.get("setFlags", []))
    check("recordsRequested" in allflags, f"S{n}: recordsRequested never set")

# citation sweep (over parsed text — raw JSON escapes § as \u00a7)
def all_text(n):
    d = load(n)
    parts = [d["meta"]["summary"]]
    for nd in d["nodes"]:
        parts += nd.get("body", []) + nd.get("debrief", [])
        for c in nd.get("choices", []):
            parts.append(c["text"])
    return "\n".join(parts)

cites = {}
for n in range(47, 57):
    txt = all_text(n)
    for m in re.findall(r"§\s*[0-9][0-9.()a-zA-Z]*", txt):
        cites.setdefault(m.strip(), []).append(n)
    for m in re.findall(r"(Act 48 of 2023|Act 119|Senate Bill 1499|Pa\.R\.J\.C\.P\.? ?1340|Rule 1340)", txt):
        cites.setdefault(m, []).append(n)
print("CITATIONS FOUND:")
for k in sorted(cites):
    print(f"  {k}: scenarios {sorted(set(cites[k]))}")
ALLOWED_SECTIONS = {"6332", "6315", "6337", "6341", "3130.44", "1340", "675",
                    "6336.1", "6302", "6315(d)", "6332(a)", "6341(a)(2)", "675(5)(E)",
                    "675(5)(F)", "3130.44(d)", "3130.44(f)", "6336.1(a)", "6341(c.2)(5)",
                    "6341(c.2)(4)", "6341(c.3)", "6341(g)"}
for k, ns in cites.items():
    if k.startswith("§"):
        num = k[1:].strip()
        while num and num[-1] in ".,":
            num = num[:-1]
        while num.count(")") > num.count("("):
            num = num[:-1]
        check(num in ALLOWED_SECTIONS, f"citation outside verified set: {k} in {ns}")

# SB 1499 wording discipline
for n in range(47, 57):
    txt = all_text(n)
    if "1499" in txt:
        ok = "introduced and in committee, not law" in txt
        print(f"SB1499 in S{n}: exact-wording present = {ok}")
        check(ok, f"S{n}: SB 1499 mentioned without exact wording")

# forbidden assessment language
for n in range(47, 57):
    txt = all_text(n)
    for bad in ["artificial intelligence", "machine learning", "predictive", "algorithm"]:
        check(bad not in txt.lower(), f"S{n}: forbidden assessment term {bad!r}")

# name collisions: batch names vs all other scenario files
NAMES = ["Renata", "Ines", "Yolanda", "Reyes", "Gwen", "Hugo", "Walter", "Deshawn", "Kira",
         "Micah", "Odette", "Tomas", "Talia", "Ruben", "Anita", "Francine", "Benny",
         "Silvia", "Petra", "Noelle", "Sanaa", "Hakim", "Cyrus", "Selah", "Rafi",
         "Nina", "Esther", "Veronica", "Otto", "Salvatore", "Imani", "Zola",
         "Beatrice", "Katya", "Lev", "Gregory", "Bruno", "Krajewski", "Halloway",
         "Fontaine", "Solberg", "Delacroix", "Moreau", "Renaud", "Wexler", "Nowak",
         "Nilsen", "Zielinski", "Anselm", "Lindgren", "Baird", "Halvorsen",
         "Barlow", "Marchetti", "Rosa"]
others = [p for p in G.glob("scenario-*.json")
          if not (47 <= int(re.search(r"scenario-(\d+)\.json", p.name).group(1)) <= 56)]
print(f"\nNAME SCAN vs {len(others)} non-batch scenario files:")
batch_text = {n: (G / f"scenario-{n}.json").read_text() for n in range(47, 57)}
name_hits = []
for name in NAMES:
    in_batch = any(re.search(rf"\b{re.escape(name)}\b", t) for t in batch_text.values())
    if not in_batch:
        continue
    for p in others:
        if re.search(rf"\b{re.escape(name)}\b", p.read_text()):
            name_hits.append((name, p.name))
for h in name_hits:
    print("  HIT:", h)
check(not name_hits, f"name collisions outside batch: {name_hits}")

# within-batch: principal first names should live in exactly one scenario
PRINCIPALS = {"Renata": 47, "Ines": 47, "Yolanda": 47, "Gwen": 48, "Hugo": 48,
              "Walter": 48, "Deshawn": 49, "Kira": 49, "Micah": 49, "Odette": 49,
              "Talia": 50, "Ruben": 50, "Anita": 50, "Francine": 51, "Benny": 51,
              "Silvia": 51, "Petra": 51, "Noelle": 52, "Sanaa": 52, "Hakim": 52,
              "Cyrus": 53, "Selah": 53, "Rafi": 53, "Nina": 53, "Esther": 53,
              "Veronica": 54, "Otto": 54, "Salvatore": 54, "Imani": 55, "Zola": 55,
              "Beatrice": 55, "Katya": 56, "Lev": 56, "Gregory": 56}
for name, home in PRINCIPALS.items():
    for n in range(47, 57):
        if n == home: continue
        txt = (G / f"scenario-{n}.json").read_text()
        check(not re.search(rf"\b{name}\b", txt), f"principal {name} (S{home}) also appears in S{n}")

print("\nSTRUCTURE FAILURES:" if fails else "\nALL STRUCTURE CHECKS PASSED")
for f in fails:
    print("  FAIL:", f)
sys.exit(1 if fails else 0)
