# Generate scenario-N-script.md from scenario-N.json (house format, cf. scenario-24-script.md)
import json, sys
from datetime import date, timedelta

CONTENT_NOTES = {
 87: "This scenario depicts the days after an administrative appeal decision in a child-abuse registry matter \u2014 orders, deadlines, a clinic, and a mailbox. There is no graphic content. Players may skip any scene or use the quick exit at any time.",
 88: "This scenario depicts the month after a dependency disposition order \u2014 an appeal deadline, lawyers' offices, visits, and paperwork. There is no graphic content. Players may skip any scene or use the quick exit at any time.",
 89: "This scenario depicts a Superior Court appeal from a goal-change order \u2014 transcripts, briefs, a hearing remembered in flashback. There is no graphic content. Players may skip any scene or use the quick exit at any time.",
 90: "This scenario depicts the weeks between an appellate victory and the remand hearing it produced \u2014 paperwork, visits, and one courtroom morning. There is no graphic content. Players may skip any scene or use the quick exit at any time.",
 91: "This scenario depicts a post-permanency winter: a teenager, a long-named permanency goal, and the hearing at which the goal is reconsidered. There is no graphic content. Players may skip any scene or use the quick exit at any time.",
 92: "This scenario depicts a kinship caregiver preparing to be heard at her granddaughter's permanency hearing. There is no graphic content. Players may skip any scene or use the quick exit at any time.",
 93: "This scenario depicts two appeals from one disposition order \u2014 the agency's, and the mother's cross-appeal \u2014 across one autumn. There is no graphic content. Players may skip any scene or use the quick exit at any time.",
 94: "This scenario depicts a permanent legal custodianship petition and the negotiation and hearing that decide it. There is no graphic content. Players may skip any scene or use the quick exit at any time.",
 95: "This scenario depicts a trial-home winter ending in a closure hearing \u2014 services, paperwork, one documented incident, and a final order. There is no graphic content. Players may skip any scene or use the quick exit at any time.",
 96: "This scenario depicts the thirty days and the appellate season after a termination-of-parental-rights decree. The subject is grave; the treatment is procedural \u2014 paperwork, deadlines, transcripts, and courtrooms. There are no depictions of the underlying events. Players may skip any scene or use the quick exit at any time.",
}
SHORT_TITLE = {87:"The Second Letter",88:"Thirty Days",89:"What the Panel Can See",90:"The Remand",91:"After the Order",92:"Heard, Not a Party",93:"Fourteen Days",94:"The Custodianship Question",95:"Earning the Last Order",96:"Thirty Days After the Decree"}

def fmt_effects(c):
    parts = []
    if "cash" in c: parts.append(f"cash {'+' if c['cash']>0 else '\u2212'}{abs(c['cash'])}")
    for f in c.get("setFlags", []): parts.append(f"FLAG: {f}")
    for h in c.get("addHidden", []): parts.append(f"HIDDEN + {h}")
    for f in c.get("requiresFlags", []): parts.append(f"REQUIRES FLAG: {f}")
    for f in c.get("requiresNoFlags", []): parts.append(f"REQUIRES NO FLAG: {f}")
    return " _(" + " ; ".join(parts) + ")_" if parts else ""

for num in range(87, 97):
    d = json.load(open(f"scenario-{num}.json"))
    m = d["meta"]
    start = date.fromisoformat(m["startDateISO"])
    lines = []
    lines.append(f"# THE FIRST 90 DAYS \u2014 Scenario {num}: \u201c{SHORT_TITLE[num]}\u201d")
    lines.append("")
    lines.append(f"*Human-readable script. This document and `scenario-{num}.json` are generated from a single source and match node-for-node: same IDs, same order, same choices, same effects.*")
    lines.append("")
    lines.append("**The family is fictional \u2014 a composite. No real person's story appears here.**")
    lines.append("")
    lines.append(f"**Content note:** {CONTENT_NOTES[num]}")
    lines.append("")
    lines.append("**How to read effects:** `cash \u221240` changes the player's cash. `FLAG: name` sets a flag the engine tracks. `HIDDEN + item` means the case file quietly records that item at this choice \u2014 the player does not see it when it happens. `REQUIRES FLAG: name` means the choice is only available if that flag was set earlier; `REQUIRES NO FLAG: name` means it is only available if that flag was never set. `NOTE:` is text shown to the player right after choosing.")
    lines.append("")
    sd = start.strftime("%A, %B ") + str(start.day) + start.strftime(", %Y")
    lines.append(f"Start date: {sd}. Day offsets are days since the scenario's start date.")
    for n in d["nodes"]:
        lines.append("")
        lines.append(f"## [{n['id']}] {n['title']}")
        lines.append(f"*{n['kicker']} (dayOffset {n['dayOffset']})*")
        lines.append("")
        for p in n["body"]:
            lines.append(p)
            lines.append("")
        if n.get("ending"):
            lines.append("**ENDING \u2014 Debrief:**")
            lines.append("")
            for p in n["debrief"]:
                lines.append(p)
                lines.append("")
        else:
            lines.append("**Choices:**")
            for c in n["choices"]:
                lines.append(f"- {c['text']} \u2192 **{c['next']}**{fmt_effects(c)}")
                if "note" in c:
                    lines.append(f"  - NOTE (shown after choosing): {c['note']}")
    out = "\n".join(lines) + "\n"
    open(f"scenario-{num}-script.md", "w").write(out)
    print(f"scenario-{num}-script.md written ({len(d['nodes'])} nodes)")
