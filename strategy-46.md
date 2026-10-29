# Strategy Guide — Scenario 46: "Two Workers, One File"

*Game documentation for a fictional simulation in "The First 90 Days" (Tactic Watch). The family, the case, and every choice below are fictional. This guide is general information about how the scenario is built — it is not legal advice for any real case.*

## (1) The win

**Best ending: "Expunged — The File Couldn't Carry It"**.

This is a **full** win. A daycare provider's indicated report rests on "inconsistent statements" — but her statement never changed. The file's did, when one worker's notebook became a typed summary and the typed summary became a second worker's certainty. The route wins by making the agency produce its own file: the appeal, filed inside the window, carries the § 6341(c.2)(4) demand for the complete investigation evidence; the production, when it finally comes, contains the notebook; and at the hearing the agency's burden — substantial evidence — has to be carried by an inconsistency its own first document refutes. The report is expunged. The partial ending ("Upheld, With Fifteen Days") is the same hearing argued without the notebook; the missed ending is the window closing on an unbuilt appeal.

## (2) The route

Verified by walking the scenario graph from the start node (see the verification note at the end). Key decision points, in order — node title, winning choice, and what it changes:

1. **Three Seconds** — *Write the incident log in that first hour, verbatim — times, the sink, the catch, the bump.* Sets **incidentLog**.
2. **The File Opens** — *File the written request and mark the phrase: "possible supervision lapse" is the case.* Sets **recordsRequested**.
3. **The Typed Summary** — *Correct it in writing before signing: "turned to the sink, two steps, within arm's reach," at both interviews.* Sets **summaryCorrected**.
4. **The Leave** — *Write to the file now: a one-page continuity memo — your account, the licensing closure, the dates.* Sets **continuityMemo**. This memo is written against the day the first worker leaves — which she does.
5. **Ms. Trask's Interview** — *Submit a written statement this week — the incident, in her own words, signed and dated.* Sets **writtenStatement**.
6. **Indicated** — *Write the dates on the folder tonight — April 6, July 5 — and get counsel this week.* Sets **deadlineKept**. The determination is dated April 6, 2026; the 90-day appeal window closes July 5, 2026.
7. **Counsel's Office** — *Build the appeal properly: the request, with the evidence demand inside it.* Sets **appealBuilt** — the flag the filing is gated on.
8. **The License Clock** — *File the built appeal: written request plus the § 6341(c.2)(4) demand for the complete investigation evidence.* Flag-gated on **appealBuilt**; sets **appealFiled**, **evidenceDemanded**.
9. **The Index** — *Have counsel demand, in writing, a further search — the (c.2)(4) production is incomplete.* Sets **searchDemanded**.
10. **Not Located** — *Insist in writing: produce the notebook or stipulate it cannot be found — either document helps.* Sets **productionInsisted**.
11. **The Box** — *Build the hearing exhibit: notebook page, typed summary, second summary — the three documents side by side.* Sets **worker1Notes**, **exhibitBuilt**.
12. **The Hearing** — *Put in the three pages: the notebook, the typed summary, the second summary — and let the file disagree with itself.* Flag-gated on **worker1Notes**.

## (3) Why this wins — the law as it is supposed to work

- **The window is 90 days and it is jurisdictional in effect.** An indicated report may be appealed within 90 days of notification (23 Pa.C.S. § 6341(a)(2)). This scenario does the arithmetic on its own dates: notification April 6, 2026 + 90 days = July 5, 2026, and the missed-window ending ("The Window, Missed") is what the statute does to a meritorious case filed on day 91.
- **The appellant has a right to the investigation evidence** — all of it, including what helps her (§ 6341(c.2)(4)). The demand is not discovery rhetoric; it is the mechanism that moves a spiral notebook out of a box and into a hearing exhibit. Without it, the agency's file is tried in its summarized form.
- **The burden is the agency's, and it is real but modest**: substantial evidence (§ 6341(c.2)(5)) — enough that a reasonable mind could accept it. Two summaries and a worksheet can carry that burden, as the partial ending shows. One contemporaneous notebook page, contradicting the summaries' shared adjective, is the kind of fact that makes a reasonable mind stop.
- **The clocks after the hearing are also law**: a decision within 45 days of the hearing (§ 6341(c.3)) — this scenario's June 9 hearing produces its decision inside that window — and, if it goes wrong, reconsideration within 15 days and the Commonwealth Court within 30 (§ 6341(g)), calendared by counsel the day the envelope opens: July 24 and August 8, 2026 on this scenario's dates.
- **The underlying record right runs through the whole case**: the provider's own file is requestable on request (55 Pa. Code § 3130.44(d)), which is how she knows, before the determination, that the case against her is a single phrase.

## (4) The traps

1. **Waiting — the drawer, the bare wait, the appeal assembled late** (the wait1/app1L arm). Cost: the appeal is filed thin or the window is missed entirely; "The Window, Missed" is the one ending no argument can reopen.
2. **Filing the appeal without the (c.2)(4) demand.** Cost: the hearing is tried on the two summaries; her testimony is credited as sincere and still loses — "Upheld, With Fifteen Days" — because sincerity is not evidence and the notebook was never demanded.
3. **Accepting "not located" as an answer.** Cost: no **productionInsisted** — an incomplete production stands as the record, and the exhibit at "The Box" cannot be built.
4. **Correcting the typed summary orally, or signing it uncorrected.** Cost: the file's drift begins with her signature under it; the continuity memo and the written statement exist on the win route precisely because the first worker's departure was foreseeable and the correction had to survive her.

## (5) What no strategy controls

Whether the notebook survived the office's filing habits, the hearing officer's reading of a modest burden, the licensing track running on its own clock, and a decade's reputation being weighed by strangers. The route controls only what was ever controllable: that the log was written in the first hour, the correction was filed before the signature dried, the appeal was built before it was filed, and the demand was in it. Outcomes in this system turn on workers, judges, and luck as much as on any parent's choices — the strategy's claim is narrower: the file that convicted her was made, by her own persistence, to testify against itself.

---
*Verification: this route was walked programmatically against `scenario-46.json` — each named choice was followed from the start node in order; every flag-gated choice's requirements were satisfied by flags set earlier on the walk; the walk terminates at the ending node titled "Expunged — The File Couldn't Carry It" after visiting 30 nodes, with $150 of the $150 starting cash remaining (no choice in this scenario carries a cash cost; the starting cash never moves). Walked path: Three Seconds → Two Reports of One Fall → The File Opens → Mr. Ostrowski's Notebook → The Typed Summary → Licensing's Letter → The Leave → Isaac's Questions → Ms. Trask's Interview → Trask's Letter → The Supervisor's Review → Isaac's Own File → Indicated → Counsel's Office → The License Clock → The Request, Filed → The Long Wait → The Index → Not Located → The Box → Counsel's Exhibit → The Hearing Room → The Hearing → What the Room Decides → The Decision → The Verb → Expunged, Upheld, or Answered For → The Ruling, As Filed → Expunged — The File Couldn't Carry It.*
