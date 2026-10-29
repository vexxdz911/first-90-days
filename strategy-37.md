# Strategy Guide — Scenario 37: "The Bruise at Practice"

*Game documentation for a fictional simulation in "The First 90 Days" (Tactic Watch). The family, the case, and every choice below are fictional. This guide is general information about how the scenario is built — it is not legal advice for any real case.*

## (1) The win

**Best ending: "Explained, With the Chart"**.

This is a **full** win. The investigation closes and the report is recorded as unfounded — because the pediatrician's chart, dated the Sunday before the report existed, answers the only question the investigation ever had. Nothing in this scenario is won at a kitchen table; it is won by a sequence of dates nobody had to argue about.

## (2) The route

Verified by walking the scenario graph from the start node (see the verification note at the end). Key decision points, in order — node title, winning choice, and what it changes:

1. **Your Own Record, First** — *File the written request for the intake summary from your record.* Sets **recordsRequested**. The parent's answers now meet the file's actual sentence instead of its shadow.
2. **The Chart, Dated Sunday** — *Get the chart printout and write the Saturday timeline tonight.* Sets **proofGathered**.
3. **The Visit** — *Tell her — and hand her the folder: the chart note and the timeline.* Sets **folderGiven**.
4. **Confirmed** — *Listen closely — she says "left shin" — and confirm it, asking for the summary in writing.* Sets **summaryInWriting**.
5. **One Detail** — *Send the one-line correction, with the league schedule, in writing.* Sets **correctionSent**.
6. **Sign Here** — *Read the whole letter before signing, then sign and file it.* Sets **readBeforeSigning**.

## (3) Why this wins — the law as it is supposed to work

- **The record request comes first, and it is a right, not a favor.** Agency records are released on request — 55 Pa. Code § 3130.44(d). In this scenario the intake summary is one paragraph; reading it before answering it is the difference between answering the report that exists and answering the report you fear.
- **Contemporaneous paper outranks recollection.** The chart was written before anyone knew a report would be made. The scenario's whole argument is chronological: a fall on Saturday, a doctor on Sunday, a report on Monday. Investigations are decided by what can be checked, and dates are the most checkable things in a file.
- **Corrections are made in writing, at the level of the sentence that is wrong.** The one detail — which shin — is corrected with the league schedule attached, so the file that closes is the file that is true.

## (4) The traps

1. **Answering from memory** at "The Visit" (the u-branch). Cost: the account drifts to "usually" and "from memory," and the investigation closes — but with an error standing in the summary, which is the ending "Closed, With an Error In It." A closed file with a wrong sentence in it is a partial win, and the guide names it as one.
2. **Skipping the record request.** Cost: no **recordsRequested** — every later answer is aimed at a summary the parent never read, and the correction beat has nothing to correct against.
3. **Signing without reading** at "Sign Here." Cost: the acknowledgment adopts whatever the letter says, including the detail the route elsewhere took care to fix.

## (5) What no strategy controls

The worker's care in checking the paper, the doctor's note being as thorough as it was, and whether another office loses a page of the folder. The route controls only what was ever controllable: that the request was written, the chart was obtained, the timeline was dated, and the correction was sent. Outcomes in this system turn on workers, offices, and luck as much as on any parent's choices — the strategy's claim is narrower: the file that decided this case was the true one.

---
*Verification: this route was walked programmatically against `scenario-37.json` — each named choice was followed from the start node in order; the walk terminates at the ending node titled "Explained, With the Chart" after visiting 12 nodes, with $150 of the $150 starting cash remaining (no choice in this scenario carries a cash cost; the starting cash never moves). Walked path: The Fall, and the Phone Call → What the Message Says → Your Own Record, First → The Chart, Dated Sunday → The Night Before the Visit → The Visit → Sunday, Before the Report → Confirmed → One Detail → The Determination → Sign Here → Explained, With the Chart.*
