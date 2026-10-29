# -*- coding: utf-8 -*-
import sys, os, re, json, datetime
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from lib import build, script, validate, walk, path_choices, D, fmt, C
from s127_130 import S127, S128, S129, S130
import s127_130b; s127_130b.expand(S127, S128, S129, S130)
from s131_133c import S131, S132, S133
from s134_136b import S134, S135, S136
SCENS = [S127, S128, S129, S130, S131, S132, S133, S134, S135, S136]
GAME = os.path.expanduser("~/workspace/your_files/tacticwatch-game")

def node(s, nid): return next(n for n in s["nodes"] if n["id"] == nid)
def setoff(s, nid, off): node(s, nid)["dayOffset"] = off

# ---------------- renames (corpus collisions found by Wave 2 batches 6-9) ----------------
RENAMES = [("Halloran","Zubia"),("Ferreira","Mendieta"),("Lindqvist","Zabala"),
 ("Abernathy","Beltran"),("Adeyemi","Ndiaye"),("Whitfield","Quintela"),
 ("Onyema","Urrutia"),("Whitaker","Kortazar"),("Nadia","Tomasa"),("Noor","Leire"),
 ("Rania","Garazi"),("Dario","Ander"),("Odette","Maite"),("Imani","Edurne"),
 ("Emeka","Unai"),("Petra","Nerea"),("Bram","Iker"),("Sable","Aitana"),
 ("Cosette","Irati"),("Jerome","Eneko"),("Willa","Maialen"),("Renata","Josune"),
 ("Rosa","Lorea"),("Sabine","Itziar"),("Hollis","Koldo"),("Fern","Arantxa"),
 ("Yolanda","Miren"),("Paloma","Uxue"),("Francine","Olatz"),("Silas","Peru"),
 ("Vera","Nahia"),("Petrov","Agirre"),("Osei","Olano"),("August and Nahia","Bittor and Nahia"),("August's","Bittor's"),
 ("August (evaluation","Bittor (evaluation")]
def deep_replace(obj):
    if isinstance(obj, str):
        for a, b in RENAMES: obj = obj.replace(a, b)
        return obj
    if isinstance(obj, list): return [deep_replace(x) for x in obj]
    if isinstance(obj, dict): return {k: deep_replace(v) for k, v in obj.items()}
    return obj
for s in SCENS:
    for k in list(s.keys()):
        if isinstance(s[k], (str, list, dict)): s[k] = deep_replace(s[k])

# ---------------- offset / wiring / text repairs ----------------
# S127: the drawer branch (appeal_risk, day 40) must rejoin a path at >= day 40
for nid, off in [("appeal_sent",44),("appeal_ack",48),("records_beat",52),("packet_back",58),
                 ("mirror_detail",62),("statement_filed",66),("school_note",71),
                 ("review_prep",78),("shift_swap",81),("review_day",85),
                 ("end_home",96),("end_plan",96),("end_registry",110)]:
    setoff(S127, nid, off)
b = node(S127, "appeal_risk")["body"]
assert "The housing hunt ate April. The study ate May." in b[0]
b[0] = b[0].replace("The housing hunt ate April. The study ate May.", "The housing hunt ate the spring.")
# S128
setoff(S128, "porch_first", 2); setoff(S128, "review_prep", 95); setoff(S128, "end_quiet128", 92)
for c in node(S128, "appeal_late_risk")["choices"]:
    if c["next"] == "appeal_filed": c["next"] = "packet_index"
for c in node(S128, "appeal_hearing")["choices"]:
    if c["next"] == "end_both": c["requiresFlags"] = ["evidenceReceived"]
# S129
setoff(S129, "end_clock129", 456)
# S130: the fifteenth month lands Apr 5, 2027 (entry Jan 5, 2026 + 455 days)
setoff(S130, "spring_review", 455); setoff(S130, "end_whole", 470); setoff(S130, "end_trial130", 470)
rb = node(S130, "rhythm")["body"]
for i, p in enumerate(rb):
    if "Autumn runs on the new county's rails" in p:
        rb[i] = p.replace("Autumn runs on the new county's rails", "The seasons turn on the new county's rails")
# S131: Bureau hearing is Mon Jun 8, 2026 (offset 217); downstream re-slotted
for nid, off in [("appeal_hearing131",217),("bur_a",225),("bur_b",238),("decision131",253),
                 ("kinship131",305),("study131",322),("study_winter",334),("ord_a",340),
                 ("ord_b",346),("ord_c",352),("packets131",362),("review131",398),
                 ("feb_a",420),("feb_b",444)]:
    setoff(S131, nid, off)
# S132: endings on the hearing day / the fifteenth month; then the +371 play-open shift
setoff(S132, "end_home132", 63); setoff(S132, "end_trial132", 63)
setoff(S132, "end_contested132", 63); setoff(S132, "end_clock132", 86)
def deep_text(s, a, bb):
    def f(o):
        if isinstance(o, str): return o.replace(a, bb)
        if isinstance(o, list): return [f(x) for x in o]
        if isinstance(o, dict): return {k: f(v) for k, v in o.items()}
        return o
    for k in list(s.keys()):
        if isinstance(s[k], (str, list, dict)): s[k] = f(s[k])
deep_text(S132, "Monday, September 14, 2026", "Monday, October 12, 2026")
deep_text(S132, "just past Maialen's thirteen-month mark", "just past Maialen's fourteen-month mark")
deep_text(S132, "one month to finish the book", "two months to finish the book")
for n in S132["nodes"]: n["dayOffset"] += 371
# S133
setoff(S133, "appeal_hearing133", 158)
setoff(S133, "end_three_chairs", 365); setoff(S133, "end_trial133", 365); setoff(S133, "end_tipped", 365)
# S135: the goal hearing sits in late October
setoff(S135, "goal_hearing135", 415); setoff(S135, "end_goal_changed", 415)
setoff(S135, "end_goal_survives", 425); setoff(S135, "end_split135", 425)

# ---------------- second-pass repairs (chain anchors, clobbered traps, weekday) ----------------
def rewire(s, nid, newnext):
    for c in node(s, nid)["choices"]: c["next"] = newnext
rewire(S131, "gap_both", "fall_reviews")
rewire(S131, "study131", "study_winter")
rewire(S132, "refresh_indexed", "winter_a132")
rewire(S133, "roster", "winter_roster")
deep_text(S131, "Tuesday, February 3, 2027", "Wednesday, February 3, 2027")
setoff(S131, "end_split131", 470)
for c in node(S131, "review131")["choices"]:
    if c["text"].startswith("Ask for immediate return"): c["next"] = "end_trial131"
    elif c["text"].startswith("Let the agency's statement stand"): c["next"] = "end_trial131"
    elif c["text"].startswith("Accept the agency's split proposal"): c["next"] = "end_split131"
node(S133, "appeal133")["choices"].append(
    C("Set the appeal aside until the case settles \u2014 one proceeding is enough", "end_registry133",
      note="One proceeding is exactly the problem. The window closes April 30 whether the case has settled or not."))
node(S133, "review_prep133")["choices"].append(
    C("Consolidate everything into the appeal now and let the study and the roster coast", "end_tipped",
      note="Coasting is how chairs fall. The study's last items and the roster's signatures were the case the appeal was supposed to be beside."))

# ending titles carry the house prefix
for s in SCENS:
    for n in s["nodes"]:
        if n.get("ending") and not n["title"].startswith("Ending — "):
            n["title"] = "Ending — " + n["title"]

# ---------------- corpus name sweep against existing files ----------------
NEW_NAMES = ["Tomasa","Leire","Garazi","Mendieta","Ander","Maite","Zabala","Edurne","Unai",
 "Beltran","Nerea","Iker","Aitana","Ndiaye","Quintela","Celeste","Selene","Irati","Urrutia",
 "Eneko","Maialen","Josune","Lorea","Itziar","Kortazar","Koldo","Arantxa","Miren","Esteban",
 "Nico","Uxue","Olatz","Peru","Bittor","Nahia","Odile","Anouk","Teo","Matteo","Zayd","Zubia",
 "Agirre","Olano","Baptiste","Grey","Castellanos"]
corpus_text = ""
for fn in os.listdir(GAME):
    m = re.fullmatch(r"scenario-(\d+)\.json", fn)
    if m and int(m.group(1)) < 127:
        corpus_text += open(os.path.join(GAME, fn), encoding="utf-8").read()
name_hits = [nm for nm in NEW_NAMES if re.search(rf"\b{re.escape(nm)}\b", corpus_text)]
print("cast-name hits in existing corpus:", name_hits)

CORPUS_NAMES = ["Althea","Andre","Beatrix","Beatriz","Bernice","Bogdan","Booker","Camille",
 "Casimir","Charise","Clarence","Colette","Colleen","Corinne","Deanna","Delia","Desirae",
 "Desiree","Emmett","Farida","Farrah","Felicia","Gideon","Gloria","Hester","Imogen","Ingrid",
 "Ivo","Josephine","Karl","Keisha","Kendra","Latrice","Lucretia","Mara","Mireille","Miriam",
 "Octavia","Pavel","Philomena","Quiana","Ramona","Rosalind","Selma","Shana","Shondra","Simone",
 "Stefan","Sylvie","Tamara","Teresa","Terrell","Terrence","Thaddeus","Vernon","Rosa","Ferreira",
 "Sable","Cosette","Fern","Odette","Adeyemi","Dario","Abernathy","Emeka","Yolanda","Petra",
 "Vera","Hollis","Ibarra","Halloran","Francine","Imani","Nadia","Bram","Willa","Renata","Silas",
 "Noor","Marta","Amara","Felix"]

# ---------------- extra audits ----------------
WD = r"(Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday)"
MO = r"(January|February|March|April|May|June|July|August|September|October|November|December)"
def all_strings(o):
    if isinstance(o, str): yield o
    elif isinstance(o, list):
        for x in o: yield from all_strings(x)
    elif isinstance(o, dict):
        for v in o.values(): yield from all_strings(v)
def weekday_audit(data):
    bad, count = [], 0
    for t in all_strings(data):
        for m in re.finditer(rf"\b{WD}, {MO} (\d{{1,2}}), (\d{{4}})\b", t):
            count += 1
            d = datetime.date(int(m.group(4)), datetime.datetime.strptime(m.group(2), "%B").month, int(m.group(3)))
            if d.strftime("%A") != m.group(1): bad.append((m.group(0), d.strftime("%A")))
    return count, bad
ALLOWED_CITES = {"6332","6315","6337","6341","6351","6336.1","6302","3130.44","675","1340"}
def citation_audit(data):
    bad = set()
    for t in all_strings(data):
        for m in re.finditer(r"§\s*([0-9][0-9.]*)", t):
            if m.group(1).rstrip(".") not in ALLOWED_CITES: bad.add(m.group(1))
    return bad
def banned_audit(data):
    txt = " ".join(all_strings(data))
    hits = [w for w in ["predictive", "machine learning", "artificial intelligence"] if w in txt.lower()]
    if re.search(r"\bAI\b", txt): hits.append("AI")
    return hits
BANDS = {"Foundation": (16, 22, 2), "Hard": (24, 34, 3), "Complex": (36, 48, 3)}

report, failures = [], []
built = {}
for s in SCENS:
    data = build(s)
    built[s["num"]] = (s, data)
    errs = validate(s["num"], data, CORPUS_NAMES)
    nn = len(data["nodes"]); ne = sum(1 for n in data["nodes"] if n.get("ending"))
    lo, hi, emin = BANDS[s["tier"]]
    if not (lo <= nn <= hi): errs.append(f"node band: {nn} not in {lo}-{hi}")
    if ne < emin: errs.append(f"endings: {ne} < {emin}")
    w = walk(data, s["win_id"])
    cash_left = None; cumneg = False
    if w is None: errs.append("win not reachable under gate-respecting walk")
    else:
        path, cash_left = w
        cum = data["meta"]["startCash"]
        for nd, c in path_choices(data, path):
            cum += c.get("cash", 0)
            if cum < 0: cumneg = True
        if cumneg: errs.append("cash goes negative on the walked route")
        if cash_left is None or cash_left < 0: errs.append("negative final cash")
    wc, wbad = weekday_audit(data)
    if wbad: errs.append(f"weekday errors: {wbad}")
    cbad = citation_audit(data)
    if cbad: errs.append(f"unverified citations: {cbad}")
    bbad = banned_audit(data)
    if bbad: errs.append(f"banned terms: {bbad}")
    win_title = next(n["title"] for n in data["nodes"] if n["id"] == s["win_id"])
    report.append(dict(num=s["num"], name=s["name"], tier=s["tier"], nodes=nn, endings=ne,
                       win=win_title, walked=(len(w[0]) if w else None), cash=cash_left,
                       weekday_claims=wc, errors=errs))
    if errs: failures.append(s["num"])

print(json.dumps(report, indent=1))
print("cast-name hits:", name_hits)
if failures:
    print("FAILURES in:", failures); sys.exit(1)
print("ALL VALIDATION PASSED")

# ---------------- write deliverables ----------------
def money(v): return f"${v}" if v >= 0 else f"\u2212${-v}"
def strat_text(s, data, w):
    path, cash_left = w
    nodes = {n["id"]: n for n in data["nodes"]}
    win = nodes[s["win_id"]]
    st = s["strategy"]
    out = [f'# Strategy Guide \u2014 Scenario {s["num"]}: "{s["name"]}"', "",
     f'*Game documentation for a fictional simulation in "The First 90 Days" (Tactic Watch). The family, the case, and every choice below are fictional. This guide is general information about how the scenario is built \u2014 it is not legal advice for any real case.*', "",
     "## (1) The win", "", f'**Best ending: "{win["title"]}."**', "", st["win_honest"], "",
     "## (2) The route", "",
     "Verified by walking the scenario graph from the start node (see the verification note at the end). Key decision points, in order \u2014 node title, winning choice, and what it changes:", ""]
    i = 0
    for nd, c in path_choices(data, path):
        if not (c.get("setFlags") or c.get("requiresFlags")): continue
        i += 1
        parts = []
        if c.get("cash"): parts.append(f'Cash {money(c["cash"])}')
        if c.get("setFlags"): parts.append("Sets " + ", ".join(f'**{f}**' for f in c["setFlags"]))
        line = f'{i}. **{nd["title"]}** \u2014 *{c["text"]}*'
        if parts: line += " " + "; ".join(parts) + "."
        if c.get("requiresFlags"):
            line += " This choice is flag-gated: it is only available with " + " + ".join(f'**{f}**' for f in c["requiresFlags"]) + "."
        out.append(line)
    out += ["",
     'Supporting choices along the same walk \u2014 every "paper version" choice (dated, copied, filed), every written request, and every dated letter \u2014 add the documentation the packet is later assembled from. The full walked path is printed in the verification note.', "",
     "## (3) Why this wins \u2014 the law as it is supposed to work", ""]
    out += [f"- {b}" for b in st["law"]]
    out += ["", "## (4) The traps", ""]
    for j, (tt, why) in enumerate(st["traps"], 1):
        tt = re.sub(r"\*([^*]+)\*", r'"\1"', tt)
        out.append(f"{j}. **{tt}** \u2014 {why}")
    out += ["", "## (5) What no strategy controls", "", st["uncontrolled"], "", "---",
     f'*Verification: this route was walked programmatically against `scenario-{s["num"]}.json` \u2014 each named choice was followed from the start node in order; every flag-gated choice\'s requirements were satisfied by flags set earlier on the walk; the walk terminates at the ending node titled "{win["title"]}" after visiting {len(path)} nodes, with ${cash_left} of the ${data["meta"]["startCash"]} starting cash remaining. Walked path: ' + " \u2192 ".join(nodes[x]["title"] for x in path) + ".*"]
    return "\n".join(out) + "\n"

written = []
for s in SCENS:
    data = built[s["num"]][1]
    w = walk(data, s["win_id"])
    jp = os.path.join(GAME, f'scenario-{s["num"]}.json')
    with open(jp, "w", encoding="utf-8") as f: json.dump(data, f, indent=2, ensure_ascii=False)
    sp = os.path.join(GAME, f'scenario-{s["num"]}-script.md')
    stxt = script(s, data)
    missing = [n["id"] for n in data["nodes"] if n["id"] not in stxt]
    assert not missing, (s["num"], missing)
    with open(sp, "w", encoding="utf-8") as f: f.write(stxt)
    gp = os.path.join(GAME, f'strategy-{s["num"]}.md')
    with open(gp, "w", encoding="utf-8") as f: f.write(strat_text(s, data, w))
    written += [jp, sp, gp]
print("wrote", len(written), "scenario files")

# ---------------- sources-batch-O.md ----------------
def add_months(d, months):
    y = d.year + (d.month - 1 + months) // 12
    m = (d.month - 1 + months) % 12 + 1
    day = min(d.day, [31,29 if y%4==0 and (y%100!=0 or y%400==0) else 28,31,30,31,30,31,31,30,31,30,31][m-1])
    return datetime.date(y, m, day)
def F(d): return fmt(d)
ARITH = [
 (127, [("Appeal notice (start)", "2026-03-02", 90, "days")]),
 (128, [("Appeal notice (start)", "2026-04-06", 90, "days"), ("Bureau hearing", "2026-04-06", 130, "days"), ("Decision (45th day after the hearing)", "2026-08-14", 45, "days")]),
 (129, [("Foster-care entry (start)", "2025-09-08", 15, "months")]),
 (130, [("Foster-care entry (start)", "2026-01-05", 15, "months")]),
 (131, [("Elder child entry", "2025-11-03", 15, "months"), ("Younger child entry (corrected date)", "2025-11-21", 15, "months"), ("Appeal notice", "2025-12-16", 90, "days"), ("Bureau hearing", "2025-11-03", 217, "days")]),
 (132, [("Foster-care entry", "2025-08-04", 15, "months"), ("Permanency hearing", "2025-08-04", 434, "days")]),
 (133, [("Foster-care entry (start)", "2026-01-12", 15, "months"), ("Appeal notice", "2026-01-30", 90, "days"), ("Bureau hearing", "2026-01-12", 158, "days")]),
 (134, [("Appeal notice (start)", "2026-02-02", 90, "days"), ("Bureau hearing", "2026-02-02", 158, "days"), ("Decision (day 31 of the 45-day window)", "2026-07-10", 31, "days")]),
 (135, [("Elder children entry (start)", "2025-09-01", 15, "months"), ("Youngest child entry", "2025-09-29", 15, "months")]),
 (136, [("Elder child entry (start)", "2025-06-02", 15, "months"), ("Twins entry", "2025-06-23", 15, "months"), ("Appeal notice", "2025-06-30", 90, "days"), ("Bureau hearing", "2025-06-02", 263, "days")]),
]
lines = ["# Sources and Alterations \u2014 Batch O (Wave 2, Batch 10: Capstones, Scenarios 127\u2013136)", "",
 "**What this batch is built from \u2014 stated plainly.** This batch read **no new published opinions** and verified **no new law**. Every scenario is a composite built from (a) the verified law set below, and (b) recurring documented practice patterns already recorded in this project's earlier sources files (notably `sources-and-alterations.md` and Wave 1's batch files): multi-clock sibling cases, cross-county kinship studies, vendor waitlists outrunning service plans, indicated appeals running beside dependency cases, and permanency hearings decided by the completeness of a year-long record. No real person's case \u2014 and none of the private cases in the project owner's orbit \u2014 is depicted or drawn on. All families, workers, lawyers, judges, and documents are fictional composites.", "",
 "**Verified law set used (all verified from primary sources in earlier batches; nothing new added by this batch):** shelter care 72 hours (42 Pa.C.S. \u00a7 6332; 23 Pa.C.S. \u00a7 6315(d)); counsel (42 Pa.C.S. \u00a7 6337; \u00a7 6332(a)); indicated-report appeal within 90 days of notification (23 Pa.C.S. \u00a7 6341(a)(2)), including Act 119 \u2014 evidence to the appellant (c.2)(4), the agency's burden by substantial evidence (c.2)(5), decision timing (c.3), and post-decision reconsideration/appeal clocks (g); dependency review and permanency determinations (42 Pa.C.S. \u00a7 6351(a)/(b)/(e)(3)(i)/(f), incl. (f)(9), and (f.1)); kinship procedures and definitions (42 Pa.C.S. \u00a7 6336.1, Act 48 of 2023; \u00a7 6302); ASFA's filing duty at 15 of the most recent 22 months and its three exceptions (42 U.S.C. \u00a7 675(5)(E)); release of the case record on request (55 Pa. Code \u00a7 3130.44(d)) and its redaction rule (\u00a7 3130.44(f)); Pa.R.J.C.P. 1340(A),(B)(1),(E),(F) with the Universal Assessment application flagged UNTESTED (no scenario in this batch turns on it, and no assessment is described anywhere in this batch as AI, machine learning, or predictive).", "",
 "**Date arithmetic \u2014 machine-computed for this file** (start/notice/entry date + the statutory period, real calendar):", ""]
for num, rows in ARITH:
    lines.append(f"## Scenario {num}")
    for label, iso, n, unit in rows:
        d0 = D(iso)
        d1 = add_months(d0, n) if unit == "months" else d0 + datetime.timedelta(days=n)
        lines.append(f"- {label}: {F(d0)} + {n} {unit} = **{F(d1)}**")
    lines.append("")
lines += ["**Alterations and deviations, disclosed:**",
 "- S127 carries **3 endings** against the Foundation band's 2: the capstone's two clocks (appeal window and review) have independent failure modes, and collapsing them would have taught that a missed appeal is recoverable inside the case. It is not, so the registry has its own ending.",
 "- S128 carries **4 endings** against the Hard band's 3: the upheld-appeal ending exists to teach 23 Pa.C.S. \u00a7 6341(g)'s post-decision clocks (reconsideration within 15 days of the mailing date; Commonwealth Court appeal within 30 days), which no other ending in the batch reaches.",
 "- S129's packet node is titled \u201cThe Packet, Assembled\u201d and its month-nine beat is the node titled \u201cMonth Nine Review\u201d \u2014 titles as built; the strategy guide's route section uses the built titles verbatim.",
 "- S132's playable story opens at month thirteen-plus (offsets are counted from the entry date, so its first node carries the entry as narrated backstory and its hearing lands Monday, October 12, 2026, ahead of the Wednesday, November 4, 2026 fifteen-month date).",
 "- Two S136 node ids preserve an authoring swap (`study_travels` holds the study-completion beat; `kin_ready` holds the Bureau hearing beat). Content, order, dates, and gates are as designed; ids are internal.",
 "- Character names in this batch were re-checked against every prior scenario file in the folder at build time; colliding names found in Wave 2 batches 6\u20139's usage (and two surnames found in the earlier corpus) were renamed inside this batch before delivery. The renames are Basque surnames/given names chosen for zero corpus hits; no renamed character corresponds to any real person.",
 "- Wins labeled **partial** (S130, S131, S135, S136) are labeled in their strategy guides and ending debriefs: the children spend substantial time in care on every route, and the guides say so. Wins labeled **full** (S127\u2013129, S132\u2013134) return the child(ren) and close the track(s) completely on the walked route.", ""]
with open(os.path.join(GAME, "sources-batch-O.md"), "w", encoding="utf-8") as f: f.write("\n".join(lines) + "\n")
print("wrote sources-batch-O.md")

