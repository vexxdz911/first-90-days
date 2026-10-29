# Batch 6 validator: all programmatic checks on shipped scenario-87..96.json + scripts.
import json, glob, re, sys
from datetime import date, timedelta

ALLOWED_CITES = [
 "42 Pa.C.S. \u00a7 6332", "23 Pa.C.S. \u00a7 6315(d)", "42 Pa.C.S. \u00a7 6337", "\u00a7 6332(a)",
 "23 Pa.C.S. \u00a7 6341(a)(2)", "\u00a7 6341(c.2)(5)", "\u00a7 6341(c.2)(4)", "\u00a7 6341(c.3)", "\u00a7 6341(g)",
 "\u00a7 6341(a)", "\u00a7 6341(c)", "\u00a7 6341(d)", "\u00a7 6351(a)(1)", "\u00a7 6351(a)(2)(i)", "\u00a7 6351(a)",
 "\u00a7 6351(b)", "\u00a7 6351(e)(3)(i)", "\u00a7 6351(f)", "\u00a7 6351(f.1)", "\u00a7 6351(f)(9)",
 "\u00a7 6351(f)(2)", "\u00a7 6351(f)(3)", "\u00a7 6351(f)(5.1)", "\u00a7 6351(f)(1)",
 "42 Pa.C.S. \u00a7 6341", "42 Pa.C.S. \u00a7 6351", "\u00a7 6336.1", "\u00a7 6302", "\u00a7 6357",
 "42 U.S.C. \u00a7 675(5)(E)", "55 Pa. Code \u00a7 3130.44(d)", "\u00a7 3130.44(d)", "\u00a7 3130.44(f)",
 "Pa.R.J.C.P. 1340", "Rule 1340", "Pa.R.A.P. 903(a)", "Pa.R.A.P. 903(b)", "Pa.R.A.P. 903",
 "Act 119", "Act 48 of 2023", "\u00a7 6338",
 "23 Pa.C.S. \u00a7 6341(c.2)(4)", "23 Pa.C.S. \u00a7 6341(c.2)(5)", "23 Pa.C.S. \u00a7 6341(c.3)", "23 Pa.C.S. \u00a7 6341(g)", "42 Pa.C.S. \u00a7 6336.1",
]
CITE_RE = re.compile(r"(?:42 Pa\.C\.S\.|23 Pa\.C\.S\.|42 U\.S\.C\.|55 Pa\. Code|Pa\.R\.A\.P\.|Pa\.R\.J\.C\.P\.)\s*(?:\u00a7\s*\d[\d.]*(?:\s*\([0-9a-zA-Z.\-]+\))*|\d[\d.]*(?:\s*\([0-9a-zA-Z.\-]+\))*)?")
BARE_SECTION_OK = {"6302", "6332", "6336.1", "6337", "6338", "6341", "6351", "6357", "675", "3130.44"}
BARE_RE = re.compile(r"\u00a7\s*(\d+(?:\.\d+)?)")
BANDS = {"Foundation": (16, 22, 2), "Hard": (24, 34, 3), "Complex": (36, 48, None)}
BEST = {87: "end_recon", 88: "end_filed", 89: "end_vacated", 90: "end_home", 91: "end_goal",
        92: "end_heard", 93: "end_best", 94: "end_plc_contact", 95: "end_closed", 96: "end_vacated"}
routes = json.load(open("gens/routes-b6.json"))
errors, warnings = [], []

def kf(start, off):
    d = start + timedelta(days=off)
    return f"Day {off} \u2014 {d.strftime('%A, %B')} {d.day}, {d.year}"

walk_report = {}
for num in range(87, 97):
    d = json.load(open(f"scenario-{num}.json"))
    m, nodes = d["meta"], d["nodes"]
    ids = [n["id"] for n in nodes]
    if len(ids) != len(set(ids)): errors.append(f"S{num}: duplicate node ids")
    byid = {n["id"]: n for n in nodes}
    start = date.fromisoformat(m["startDateISO"])
    lo, hi, exp_end = BANDS[m["tier"]]
    if not (lo <= len(nodes) <= hi): errors.append(f"S{num}: {len(nodes)} nodes outside {m['tier']} band {lo}-{hi}")
    endings = [n for n in nodes if n.get("ending")]
    if exp_end and len(endings) != exp_end: errors.append(f"S{num}: {len(endings)} endings, expected {exp_end}")
    if m["tier"] == "Complex" and not (3 <= len(endings) <= 4): errors.append(f"S{num}: complex endings {len(endings)}")
    for n in nodes:
        if not re.match(r"^Day \d+ \u2014 ", n["kicker"]) and "After the date" not in n["kicker"]:
            warnings.append(f"S{num}/{n['id']}: unusual kicker {n['kicker']!r}")
        if n["kicker"].startswith("Day "):
            want = kf(start, n["dayOffset"])
            if n["kicker"] != want: errors.append(f"S{num}/{n['id']}: kicker {n['kicker']!r} != computed {want!r}")
        if n.get("ending"):
            if n.get("choices"): errors.append(f"S{num}/{n['id']}: ending has choices")
            if not n.get("debrief"): errors.append(f"S{num}/{n['id']}: ending lacks debrief")
        else:
            if not n.get("choices"): errors.append(f"S{num}/{n['id']}: non-ending lacks choices")
            for c in n["choices"]:
                if c["next"] not in byid: errors.append(f"S{num}/{n['id']}: next {c['next']} unresolved")
                elif byid[c["next"]]["dayOffset"] < n["dayOffset"]:
                    errors.append(f"S{num}: edge {n['id']}({n['dayOffset']}) -> {c['next']}({byid[c['next']]['dayOffset']}) runs backwards")
    # reachability
    seen, stack = set(), [m["startNode"]]
    while stack:
        x = stack.pop()
        if x in seen: continue
        seen.add(x)
        for c in byid[x].get("choices", []): stack.append(c["next"])
    if seen != set(ids): errors.append(f"S{num}: unreachable nodes {sorted(set(ids)-seen)}")
    # citation sweep
    blob = json.dumps(d, ensure_ascii=False)
    for cite in set(CITE_RE.findall(blob)):
        if not any(cite == a or cite.startswith(a) for a in ALLOWED_CITES):
            errors.append(f"S{num}: citation outside verified set: {cite!r}")
    for sec in set(BARE_RE.findall(blob)):
        if sec not in BARE_SECTION_OK:
            errors.append(f"S{num}: bare section cite outside verified set: \u00a7 {sec}")
    for bad in ["predictive", "machine learning", "artificial intelligence"]:
        if bad in blob.lower(): errors.append(f"S{num}: banned term {bad!r}")
    # win-route walk
    route = routes[str(num)]
    cur, flags, cash, path = m["startNode"], set(), m["startCash"], []
    guard = 0
    while True:
        guard += 1
        if guard > 300: errors.append(f"S{num}: walk loop"); break
        node = byid[cur]; path.append(cur)
        if node.get("ending"): break
        if cur not in route: errors.append(f"S{num}: no win choice recorded at {cur}"); break
        c = node["choices"][route[cur]]
        for f in c.get("requiresFlags", []):
            if f not in flags: errors.append(f"S{num}: at {cur}, requiresFlags {f} not yet set (flags={sorted(flags)})")
        for f in c.get("requiresNoFlags", []):
            if f in flags: errors.append(f"S{num}: at {cur}, requiresNoFlags {f} is set")
        cash += c.get("cash", 0)
        if cash < 0: errors.append(f"S{num}: cash negative at {cur} ({cash})")
        flags |= set(c.get("setFlags", []))
        cur = c["next"]
    if path and path[-1] != BEST[num]:
        errors.append(f"S{num}: win walk ends at {path[-1]}, expected best ending {BEST[num]}")
    if "recordsRequested" not in flags:
        errors.append(f"S{num}: recordsRequested not set on winning route")
    walk_report[num] = (len(path), cash, byid[BEST[num]]["title"] if path and path[-1] == BEST[num] else "?")
    # script parity
    script = open(f"scenario-{num}-script.md").read()
    script_ids = re.findall(r"^## \[([^\]]+)\] ", script, re.M)
    if script_ids != ids: errors.append(f"S{num}: script node order/ids differ from JSON")
    for n in nodes:
        for c in n.get("choices", []):
            if c["text"] not in script: errors.append(f"S{num}/{n['id']}: choice text missing from script: {c['text'][:60]!r}")

print("=== WIN WALKS ===")
for num, (ln, cash, title) in walk_report.items():
    print(f"S{num}: walked {ln} nodes, cash left {cash}, best ending: {title}")
print("\n=== ERRORS ===" if errors else "\nALL CHECKS PASSED")
for e in errors: print(" -", e)
for w in warnings: print(" warn:", w)
sys.exit(1 if errors else 0)
