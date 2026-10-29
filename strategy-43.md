# Strategy Guide — Scenario 43: "Two Reports, One Week"

*Game documentation for a fictional simulation in "The First 90 Days" (Tactic Watch). The family, the case, and every choice below are fictional. This guide is general information about how the scenario is built — it is not legal advice for any real case.*

## (1) The win

**Best ending: "Two Files, Both Closed"**.

This is a **full** win. Two reports in one week — different claims, different workers, two case numbers — want to become one story about one family, and merged stories are always worse than either of their parts. The route refuses the merger on paper: two intake requests, two colors of claims, two packets, two meetings, two closing letters. Each file is answered only with its own facts, and each closes on its own record.

## (2) The route

Verified by walking the scenario graph from the start node (see the verification note at the end). Key decision points, in order — node title, winning choice, and what it changes:

1. **Monday's Card** — *Write down the call — her name, the report's words, the word "every" — before dinner.* Sets **callLogged**.
2. **Thursday's Call** — *Note the second report in its own column: different claim, different worker, different file.* Sets **filesSeparated**.
3. **Two Case Numbers** — *Request both intake summaries, in writing, one request per file.* Sets **recordsRequested**.
4. **Two Summaries** — *Mark each summary's claims in its own color — every, daily, ongoing — claim by claim.* Sets **claimsMarked**.
5. **Odell's Sentence** — *Write Odell's account tonight, in his words, with the date — for File Two.* Sets **andreAccount** (the flag name predates a completion-pass rename of the character; the flag itself is unchanged).
6. **Two Packets** — *Build two packets — one per file, each answering only its own claims.* Sets **twoPackets** — the flag the first meeting is gated on.
7. **The First Meeting** — *Deliver File One's packet: aftercare receipts, work schedule, Yvette's Wednesday letter.* Flag-gated on **twoPackets**.
8. **The Seam, Described Accurately** — *Read his draft at the table, line by line, before it is filed.* Sets **draftRead**.
9. **Two Letters** — *Read both letters fully; sign; file each in its own color, with its own packet.* Sets **readBeforeSigning**.

## (3) Why this wins — the law as it is supposed to work

- **Each report is its own case with its own record.** Nothing in the verified set lets one investigation's claims borrow another's evidence — but files merge in practice through copied summaries and shared adjectives ("every," "daily," "ongoing"). The route's discipline is administrative, and that is the point: separation is maintained by requesting, marking, and answering each file separately, in writing.
- **The record request, twice** (55 Pa. Code § 3130.44(d)): one request per file, so each summary arrives as its own document and can be marked claim by claim against its own facts.
- **A child's account belongs to the file it answers.** Odell's sentence — his own words about the afternoon File Two concerns — is written the night he says it, dated, and filed in File Two only. In the merged-file ending, that sentence is quoted in both files and believed in neither.

## (4) The traps

1. **Building one packet for both meetings** (the m-branch). Cost: the packet answers neither file's claims cleanly, the meetings produce a voluntary services plan instead of two closures — "Ninety Days of Services" — and the family's compliance is then measured against a plan neither report justified on its own paper.
2. **Letting the second worker narrate both reports as one pattern** (the h-branch). Cost: "The File They Merged" — each claim inherits the other's seriousness, the assessment is written against the composite, and there is no longer a single false sentence to correct, because the error is the frame.
3. **Answering File One with File Two's facts** at the first meeting. Cost: the correction the route needs — separation — is forfeited by the parent herself, in the room, on the record.
4. **Signing either closing letter unread.** Cost: the summary's adjectives survive into the permanent file, unmarked.

## (5) What no strategy controls

Whether the two workers ever speak to each other, whether a supervisor prefers one file, and the ordinary gravity that pulls two open cases toward each other. The route controls only what was ever controllable: that each request, packet, and letter existed separately, in writing, in its own color. Outcomes in this system turn on workers, judges, and luck as much as on any parent's choices — the strategy's claim is narrower: these two files closed as two files, because the parent never let them become one.

---
*Verification: this route was walked programmatically against `scenario-43.json` — each named choice was followed from the start node in order; every flag-gated choice's requirements were satisfied by flags set earlier on the walk; the walk terminates at the ending node titled "Two Files, Both Closed" after visiting 14 nodes, with $150 of the $150 starting cash remaining (no choice in this scenario carries a cash cost; the starting cash never moves). Walked path: Monday's Card → Thursday's Call → Two Case Numbers → Two Summaries → Odell's Sentence → Two Packets → Two Envelopes → The First Meeting → The Fence → One Color Down → The Counselor's Log → The Seam, Described Accurately → Two Letters → Two Files, Both Closed.*
