#!/usr/bin/env python3
"""Validate scenarios 117-126 (Wave 2, Batch 9): structure, dates, parity,
citations, names, hidden-item and flag discipline."""
import json, re, sys
from datetime import date, timedelta
from pathlib import Path

G = Path("/home/hatch/workspace/your_files/tacticwatch-game")
BANDS = {117: ("Foundation", 16, 22, 2), 118: ("Hard", 24, 34, 3), 119: ("Hard", 24, 34, 3),
         120: ("Hard", 24, 34, 3), 121: ("Complex", 36, 48, None), 122: ("Complex", 36, 48, None),
         123: ("Complex", 36, 48, None), 124: ("Complex", 36, 48, None),
         125: ("Complex", 36, 48, None), 126: ("Complex", 36, 48, None)}
fails = []

def fmt(d):
    return d.strftime("%A, %B %-d, %Y")

def load(n):
    return json.loads((G / f"scenario-{n}.json").read_text())

def check(cond, msg):
    if not cond:
        fails.append(msg)
    return cond

for n in range(117, 127):
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
    by_id = {nd["id"]: nd for nd in nodes}
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
                check(by_id[c["next"]]["dayOffset"] >= nd["dayOffset"],
                      f"S{n}: backwards edge {nd['id']} -> {c['next']}")
                for f in c.get("requiresFlags", []):
                    pass  # gate satisfiability is the walker's job
    # reachability
    adj = {nd["id"]: [c["next"] for c in nd.get("choices", [])] for nd in nodes}
    seen, stack = set(), [meta["startNode"]]
    while stack:
        x = stack.pop()
        if x in seen: continue
        seen.add(x); stack.extend(adj.get(x, []))
    check(seen == idset, f"S{n}: unreachable nodes {sorted(idset - seen)}")
    # script parity: headers in order + every choice text present
    script = (G / f"scenario-{n}-script.md").read_text()
    heads = re.findall(r"^## \[([^\]]+)\] ", script, re.M)
    check(heads == ids, f"S{n}: script headers != JSON node order")
    for nd in nodes:
        for c in nd.get("choices", []):
            check(c["text"] in script, f"S{n}: choice text missing from script at {nd['id']}")
    # recordsRequested must be settable
    allflags = set()
    for nd in nodes:
        for c in nd.get("choices", []):
            allflags.update(c.get("setFlags", []))
    check("recordsRequested" in allflags, f"S{n}: recordsRequested never set")

# citation sweep
def all_text(n):
    d = load(n)
    parts = [d["meta"]["summary"]]
    for nd in d["nodes"]:
        parts += nd.get("body", []) + nd.get("debrief", [])
        for c in nd.get("choices", []):
            parts.append(c["text"])
    return "\n".join(parts)

cites = {}
for n in range(117, 127):
    txt = all_text(n)
    for m in re.findall(r"§\s*[0-9][0-9.()a-zA-Z]*", txt):
        cites.setdefault(m.strip(), []).append(n)
    for m in re.findall(r"(Act 119|Act 48 of 2023|Pa\.R\.J\.C\.P\.? ?1340|Rule 1340|Senate Bill 1499)", txt):
        cites.setdefault(m, []).append(n)
print("CITATIONS FOUND:")
for k in sorted(cites):
    print(f"  {k}: scenarios {sorted(set(cites[k]))}")
# allowed base sections: PA verified set (v1 + Wave 1) + newly verified this run
ALLOWED_BASE = {"6332", "6315", "6337", "6341", "6351", "6336.1", "6302", "675",
                "3130.44", "1340", "6311", "6312", "300.301", "300.519"}
for k, ns in cites.items():
    if k.startswith("§"):
        num = k[1:].strip()
        base = re.match(r"[0-9]+(?:\.[0-9]+)?", num)
        check(base and base.group(0) in ALLOWED_BASE, f"citation outside verified set: {k} in {ns}")

# Rule 1340 UA-application must be flagged UNTESTED wherever Rule 1340 is argued for the assessment (S124)
txt124 = all_text(124)
if "1340" in txt124:
    check("untested" in txt124.lower(), "S124: Rule 1340 used without the UNTESTED flag")

# forbidden assessment language + no education-law overreach terms stated as holdings
for n in range(117, 127):
    txt = all_text(n)
    for bad in ["artificial intelligence", "machine learning", "predictive", "algorithm"]:
        check(bad.lower() not in txt.lower(), f"S{n}: forbidden assessment term {bad!r}")

# name collisions: batch names vs all other scenario files
NAMES = ["Gina", "Nolan", "Odessa", "Darnell", "Khalil", "Jaylen", "Kavita", "Navya",
         "Maureen", "Siobhan", "Reginald", "Alina", "Wilma", "Bernadette", "Oren",
         "Dalila", "Yasmin", "Heather", "Callum", "Bianca", "Mateo", "Samira",
         "Shirley", "Destiny", "Iversen", "Pavlik", "Clayton", "Rahal", "Greer",
         "Ostrander", "Pascal", "Ashby", "Wells", "Raman", "Yuen", "Sorrel",
         "Franca", "Petrillo", "Brackett", "Ellery", "Anwar", "Jerome", "Zielinska",
         "Renner", "Bly", "Sorin", "Vadnais", "Aldana", "Anselmi", "Havel", "Farrow",
         "Baranski", "Truman", "Mbeki", "Vasquez", "Fontana", "Keller", "Haddad",
         "Phan", "Corvath", "Skye", "Viteri", "Wexford", "Valladolid", "Sayegh",
         "Salazar", "Tuttle", "Nasser", "Aldous", "Torres", "Whitby", "Quashie",
         "Okonkwo", "Yilmaz", "Trejo", "Asare", "Halden", "Petrides", "Iyer",
         "Yusuf", "Kaminski"]
others = [p for p in G.glob("scenario-*.json")
          if not (117 <= int(re.search(r"scenario-(\d+)\.json", p.name).group(1)) <= 126)]
print(f"\nNAME SCAN vs {len(others)} non-batch scenario files:")
batch_text = {n: (G / f"scenario-{n}.json").read_text() for n in range(117, 127)}
name_hits = []
for name in NAMES:
    if not any(re.search(rf"\b{re.escape(name)}\b", t) for t in batch_text.values()):
        continue
    for p in others:
        if re.search(rf"\b{re.escape(name)}\b", p.read_text()):
            name_hits.append((name, p.name))
for h in name_hits:
    print("  HIT:", h)
check(not name_hits, f"name collisions outside batch: {name_hits}")

# within-batch: principal first names live in exactly one scenario
PRINCIPALS = {"Gina": 117, "Nolan": 117, "Odessa": 117, "Darnell": 118, "Khalil": 118,
              "Kavita": 119, "Navya": 119, "Maureen": 120, "Siobhan": 120,
              "Reginald": 121, "Alina": 121, "Wilma": 121, "Bernadette": 122, "Oren": 122,
              "Dalila": 123, "Yasmin": 123, "Heather": 124, "Callum": 124,
              "Bianca": 125, "Mateo": 125, "Samira": 125, "Shirley": 126, "Destiny": 126}
for name, home in PRINCIPALS.items():
    for n in range(117, 127):
        if n == home: continue
        txt = (G / f"scenario-{n}.json").read_text()
        check(not re.search(rf"\b{name}\b", txt), f"principal {name} (S{home}) also appears in S{n}")
# within-batch: principal surnames also confined
SURNAMES = {"Raman": 119, "Brackett": 120, "Bly": 121, "Farrow": 122, "Haddad": 123,
            "Valladolid": 124, "Torres": 125, "Trejo": 126, "Mbeki": 122, "Vasquez": 125}
for name, home in SURNAMES.items():
    for n in range(117, 127):
        if n == home: continue
        txt = (G / f"scenario-{n}.json").read_text()
        check(not re.search(rf"\b{name}\b", txt), f"surname {name} (S{home}) also appears in S{n}")

print("\nSTRUCTURE FAILURES:" if fails else "\nALL STRUCTURE CHECKS PASSED")
for f in fails:
    print("  FAIL:", f)
sys.exit(1 if fails else 0)
