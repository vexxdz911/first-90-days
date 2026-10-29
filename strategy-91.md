# Strategy Guide — Scenario 91: "After the Order"

*Game documentation for a fictional simulation in "The First 90 Days" (Tactic Watch). The family, the case, and every choice below are fictional. This guide is general information about how the scenario is built — it is not legal advice for any real case.*

## (1) The win

**Best ending: "The Goal Moves Back: Reunification, With Dates."**

State it honestly: this is a **partial** win. The permanency outcome changes from "another planned permanent living arrangement" back to reunification on a stepped schedule written into the order — overnights in April, expansion through the summer. Emory is not home tonight, the case is not closed, and conditions attach. What changed is the plan's direction and its dates, which in a post-permanency case is the substance courts actually control. The scenario's premise is that a changed goal is not a verdict set in stone: the outcome menu is chosen from again at every permanency hearing, on the record then before the court.

## (2) The route

Verified by walking the scenario graph from the start node (see the verification note at the end). Key decision points, in order:

1. **The New Worker's Questions** — *Hand her a written update with the certificates attached.* Sets **updateFiled**. The file's summary of Lucretia was four months old; the update makes the record correct itself, in her own words, scanned in while she watched.
2. **Reading Your Own File** — *Sign the written request for the complete record.* Cash −10. Sets **recordsRequested** (55 Pa. Code § 3130.44(d)). Post-permanency, the file is the case; the route begins by reading all of it.
3. **Emory's Letter, In His Own Hand** — *Help him send it through his lawyer and the case team, and file a copy.* Sets **childVoice** — one of the two flags the winning hearing choice requires. A fourteen-year-old's stated wishes, in the record through proper channels instead of in a purse.
4. **The Counselor Who Keeps Receipts** and **The Mentor From the Machine Shop** — the school letter (**schoolLetter**) and the mentor's signed letter (**mentorLetter**): the chord the letter plays in.
5. **The Lease, Renewed** — *Get the signed letter and a copy of the renewal into the packet.* Sets **housingProof**; the file's housing entry stops being a nod.
6. **The Last Certificate** — *Pay for the official certificate and file it the day it prints.* Cash −15. Sets **servicesDone** — the second required flag. You finish with $105 of the $130 start.
7. **Dinner Visits, Logged** — the written log specificity (**visitLog**), and the packet assembled in the statute's order (**packetBuilt**).
8. **The Six-Month Hearing** — *Ask the court to change the outcome: reunification, stepped, with overnights written into the order.* Flag-gated on **servicesDone** + **childVoice**. Note that the route requires both a completed record and the larger ask — see the traps for what each missing half costs.

## (3) Why this wins — the law as it is supposed to work

Only principles from the scenario's verified set are stated here:

- **Permanency hearings recur, and each one re-runs the analysis.** Hearings are held within six months of the previous permanency hearing (42 Pa.C.S. § 6351(e)(3)(i)); at each, the court makes the determinations listed in § 6351(f) — including (f)(2) compliance with the plan and (f)(3) progress toward alleviating the circumstances that made placement necessary — and then chooses an outcome from § 6351(f.1)'s menu. "Another planned permanent living arrangement" is one item on that menu, chosen at the last hearing on that hearing's record. It is not a terminal classification, and nothing in the verified set makes it one: a later record that better supports a different outcome supports changing it, which is what this route builds.
- **Determinations are made from the file**, which is why the route is a file-correcting exercise: the § 3130.44(d) request to see it, the written update to fix it, the letters and certificates to complete it, and the child's own letter to put the subject's voice where determinations are made from.
- **The outcome chosen is chosen from the requests presented.** The statute supplies the menu; it does not supply the ask. The winning route's final move is a sentence said out loud in the courtroom — a fact the two lesser endings exist to prove from both sides.

## (4) The traps

1. **Keeping Emory's letter in your purse at "Emory's Letter."** No **childVoice** — the winning hearing choice closes. Purses do not testify; filed letters do.
2. **Bringing the course workbook instead of the certificate at "The Last Certificate."** No **servicesDone** — the same closure from the other flank. Workbooks show effort; determinations are made about completion.
3. **Asking only for an enlarged APPLA at the hearing** — more weekends, a formal role — from a record built for more. Ends at "APPLA, With Her Name Back In It": real gains, honestly labeled, and the scenario's cleanest statement of its second doctrine — courts grant requests; they rarely upgrade them.
4. **Letting the agency's report carry the hearing.** Ends at "The Long Name, Renewed": eleven minutes, an unargued file, six more months. The record Lucretia built remains usable in September; the six months do not come back.

## (5) What no strategy controls

The judge's caution with a fourteen-year-old's remaining childhood; the agency's institutional inertia; a teenager's spring, which arrives with its own weather regardless of orders. The route controlled the record and the request. The scenario is unusually candid that in this posture, those two were most of the game — and that this is a property of post-permanency practice, where the law's machinery is a recurring hearing and the variable is what the file says when it convenes.

---
*Verification: this route was walked programmatically against `scenario-91.json` — each named choice was followed from the start node in order; every intermediate node and choice exists; the flag-gated hearing choice's requirements (servicesDone, childVoice) were satisfied by flags set earlier on the walk; the walk terminates at the ending node titled "The Goal Moves Back: Reunification, With Dates" after visiting 20 nodes, with $105 of the $130 starting cash remaining.*
