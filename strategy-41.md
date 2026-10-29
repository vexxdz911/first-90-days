# Strategy Guide — Scenario 41: "The Night They Came Twice"

*Game documentation for a fictional simulation in "The First 90 Days" (Tactic Watch). The family, the case, and every choice below are fictional. This guide is general information about how the scenario is built — it is not legal advice for any real case.*

## (1) The win

**Best ending: "On Her Own Paper"**.

This is a **full** win. Two workers will carry two versions of one Saturday-evening agreement out of the same living room. The route makes sure the version the file keeps is the mother's — because she wrote hers down the same night, confirmed it in a letter the second worker had to answer, and got the note amended in ink. The children never leave home on this route, and the plan that governs the family is the one that was actually agreed.

## (2) The route

Verified by walking the scenario graph from the start node (see the verification note at the end). Key decision points, in order — node title, winning choice, and what it changes:

1. **What Was Agreed** — *Write down tonight's visit verbatim — times, her sentence, your yes — dated and signed.* Sets **notesWritten**. This flag gates the win twice over.
2. **Your Own Record, First** — *File the written request for the intake summary and the visit note.* Sets **recordsRequested**.
3. **The Neighbor at the Window** — *Get Mrs. Deveraux's statement in writing, and draft the confirmation letter tonight.* Sets **neighborSeen**, **confirmReady**.
4. **The Meeting, With a Different Reader** — *Hand him the confirmation letter: the agreed terms as actually agreed Saturday.* This choice is flag-gated on **confirmReady** — a letter drafted the night before is the only version of this move that exists.
5. **Amended, In Ink** — *File your copy tonight, with the neighbor's statement and your Saturday lines beside it.* Sets **amendmentCopied**.
6. **The Draft Summary** — *Point to the line, once, with Saturday's own paper beside it — your eleven lines against his one.* Sets **lineCorrected**.
7. **Sign Here** — *Read the whole letter, then sign and file it with the rest.* Sets **readBeforeSigning**.

## (3) Why this wins — the law as it is supposed to work

- **An oral agreement has as many versions as it has hearers; a written confirmation has one.** The scenario's mechanism is not legal but evidentiary, and it is the design's core lesson: the same-night verbatim note (dated, signed) is the only first-person account of Saturday night in existence that is not a summary.
- **The record is requestable while the case is still warm** — 55 Pa. Code § 3130.44(d). Reading the visit note before the meeting with the second worker is what turns the meeting from a retelling into a correction.
- **On the branch where the parent declines the voluntary placement in writing, the law's clock is real and short**: the emergency placement that follows requires a shelter care hearing within 72 hours of a removal (42 Pa.C.S. § 6332; 23 Pa.C.S. § 6315(d)), and at that hearing the same folder — the Saturday lines, the neighbor's statement — is what counsel rises with. The paperwork discipline is identical on both branches; only the room changes.

## (4) The traps

1. **Trusting the agreement** at "What Was Agreed." Cost: no **notesWritten** — the file's only account of Saturday is the worker's summary, and the summary's version ("mother disputes") is the one every later reader plans around. The win's gates close here, on night one.
2. **Signing the voluntary placement agreement** at "'Mother Disputes.'" Cost: the children stay with Marla under a paper with no end date — "Home, On Their Paper" is a partial ending precisely because the placement was consented to, and consented placements end when the file says they end.
3. **Declining without the dated written line.** Cost: the refusal is recorded as non-cooperation rather than as a position, and the removal branch runs without the one document that distinguishes them.
4. **Correcting the draft summary from memory** at "The Draft Summary." Cost: the line stands; corrections offered without the paper beside them are noted as disputes, not made as amendments.

## (5) What no strategy controls

Which worker reads the file second, whether the neighbor was actually at her window, and the judge on the removal branch. The route controls only what was ever controllable: that Saturday night was written down on Saturday night, that the record was requested before the meeting, and that the confirmation was a letter and not a hope. Outcomes in this system turn on workers, judges, and luck as much as on any parent's choices — the strategy's claim is narrower: when two versions of one evening competed, the file kept the one that was written first.

---
*Verification: this route was walked programmatically against `scenario-41.json` — each named choice was followed from the start node in order; every flag-gated choice's requirements were satisfied by flags set earlier on the walk; the walk terminates at the ending node titled "On Her Own Paper" after visiting 15 nodes, with $170 of the $170 starting cash remaining (no choice in this scenario carries a cash cost; the starting cash never moves). Walked path: The Store at Dusk → What Was Agreed → Sunday, Quietly → Your Own Record, First → What the Note Says → The Neighbor at the Window → The Night Before Monday → The Meeting, With a Different Reader → Gable, By Phone → Amended, In Ink → The Confirmation, In Writing → A Week on the Narrow Plan → The Draft Summary → Sign Here → On Her Own Paper.*
