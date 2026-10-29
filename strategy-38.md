# Strategy Guide — Scenario 38: "The Card in the Door"

*Game documentation for a fictional simulation in "The First 90 Days" (Tactic Watch). The family, the case, and every choice below are fictional. This guide is general information about how the scenario is built — it is not legal advice for any real case.*

## (1) The win

**Best ending: "The Call, On Paper"**.

This is a **full** win. The first phone call — usually the moment an investigation's first draft gets written from a parent's improvised words — is made as a document instead: planned, timeline-first, and confirmed in writing the same day. The case closes on the call the parent actually made, not the call the file reconstructed.

## (2) The route

Verified by walking the scenario graph from the start node (see the verification note at the end). Key decision points, in order — node title, winning choice, and what it changes:

1. **Nine Minutes** — *Write down Tuesday's timeline tonight — times, the broken bus, the nine minutes.* Sets **timelineWritten**.
2. **Know Your Own File First** — *File the written request for the intake summary from your record.* Sets **recordsRequested**.
3. **Schedules, Gathered** — *Assemble them: Luz's schedule, the transit alert, your roster, the timeline.* Sets **proofGathered**.
4. **The Call, Rehearsed** — *Plan the call as a document: facts first, timeline offered, everything confirmed.* Sets **callPlanned**.
5. **The First Call** — *Give the short account — and then confirm the call in writing, timeline and schedules attached.* Sets **callConfirmed**.
6. **The Backup Gets Tested** — *Log the afternoon in your own notes tonight — date, time, who met the bus.* Sets **ownNotes**.
7. **The Last Paragraph** — *Read it all, sign the acknowledgment — and attach a one-line note with the arrangement as agreed.* Sets **readBeforeSigning**.

## (3) Why this wins — the law as it is supposed to work

- **The record request precedes the first substantive conversation** — agency records are released on request (55 Pa. Code § 3130.44(d)). The parent reads the intake summary before the call, so the call answers the report that exists.
- **A phone call becomes evidence only when it is confirmed in writing.** The investigation's file is built from summaries of conversations. The written confirmation — timeline and schedules attached, sent the same day — is the one move that puts the parent's version into the file in the parent's own words.
- **One unexplained Tuesday is a documentation problem, not a character verdict.** A broken bus, a backup caregiver's schedule, and a nine-minute gap are all provable or disprovable on paper; the route assembles the paper before anyone is asked to take the parent's word for any of it.

## (4) The traps

1. **Describing the arrangement as what "routinely" happens** on the first call (the u-branch). Cost: the file records the adverb instead of the facts — "Routinely, In the File" is the partial ending, and the arrangement is then tested against a claim the parent never actually made about that Tuesday.
2. **Making the call before the record request.** Cost: no **recordsRequested** — the call is aimed at a guessed report.
3. **Accepting the plan as handed down** instead of asking for it in writing with the backup arrangement named. Cost: the plan in the file is the worker's draft, and the closing summary quotes it.

## (5) What no strategy controls

Whether the bus actually broke down on the record the transit agency keeps, whether the worker writes the confirmation into his summary fairly, and plain luck. The route controls only what was ever controllable: that the timeline was written the same night, the request was filed before the call, and the call was confirmed on paper. Outcomes in this system turn on workers, judges, and luck as much as on any parent's choices — the strategy's claim is narrower: the file's first draft of this family was written from dated facts.

---
*Verification: this route was walked programmatically against `scenario-38.json` — each named choice was followed from the start node in order; the walk terminates at the ending node titled "The Call, On Paper" after visiting 12 nodes, with $165 of the $165 starting cash remaining (no choice in this scenario carries a cash cost; the starting cash never moves). Walked path: Wedged in the Door → Nine Minutes → Know Your Own File First → Schedules, Gathered → The Call, Rehearsed → The First Call → His Summary, and Yours Beside It → The Visit, Demonstrated → The Backup Gets Tested → Closing, In Preparation → The Last Paragraph → The Call, On Paper.*
