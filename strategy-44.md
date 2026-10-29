# Strategy Guide — Scenario 44: "The Morning Test"

*Game documentation for a fictional simulation in "The First 90 Days" (Tactic Watch). The family, the case, and every choice below are fictional. This guide is general information about how the scenario is built — it is not legal advice for any real case.*

## (1) The win

**Best ending: "Explained Before It Posted"**.

This is a **full** win, and it is a race won before the starting gun. A night-shift father's prescription will make a drug screen read positive. That result is a fact about chemistry; what it becomes in the file — an explained medication or an unexplained impairment — depends entirely on whether the prescriber's letter exists in the file *before* the result does. The route requests the letter on day one, chases it daily, and hands the packet to the worker before the screen is taken. When the result posts, it posts into a file that already contains its explanation.

## (2) The route

Verified by walking the scenario graph from the start node (see the verification note at the end). Key decision points, in order — node title, winning choice, and what it changes:

1. **The Kettle** — *Write Saturday down tonight — times, burner, kettle, Molly's rug — while it is still exact.* Sets **timelineWritten**.
2. **The Ask** — *Decide the letter gets requested today — before the screen is even scheduled.* Sets **letterRequestedEarly**.
3. **What the File Says So Far** — *File the written request and mark the phrase: "possible impairment" is the claim.* Sets **recordsRequested**.
4. **Saturday, Reconstructed** — *Assemble it all: schedule, timeline, Ashford's statement, the pharmacy printout.* Sets **proofGathered**.
5. **The Letter, Requested** — *Press the office, politely and daily: collect the letter in person the day it is ready.* Sets **packetReady** — the flag the screen is gated on.
6. **The Screen** — *Hand Vance the packet now — letter on top — before the result exists anywhere.* Flag-gated on **packetReady**.
7. **Positive, With a Footnote Already There** — *Ask for the closing documents in writing, for your folder — the screen note included.* Sets **copiesRequested**.
8. **The Closing, Drafted** — *Point to the phrase once, letter in hand, and ask for the medication to be named.* Sets **phraseCorrected**.

## (3) Why this wins — the law as it is supposed to work

- **Sequence is evidence.** The same letter is exculpatory before the result and an excuse after it; files are read in the order they were built. The scenario states no drug-testing rule — it teaches the evidentiary mechanics the verified set supports: the record is requestable (55 Pa. Code § 3130.44(d)), so the parent knows the file's exact claim ("possible impairment") in time to answer that claim rather than a worse one.
- **A pharmacy printout is not a prescriber's letter.** The printout proves a prescription was filled; the letter states what was prescribed, why, and what it does to a screen. The partial ending — "Ten Days Unexplained" — is the printout's biography: true, insufficient, and late.
- **Refusal is the only move that converts a chemistry question into a credibility one.** On the hard branch the screen is declined or deferred, the file records "unable to assess," and the test comes back court-ordered — "The Test, Ordered" — with the father's cooperation, rather than his medication, as the file's subject.

## (4) The traps

1. **Waiting for the screen to be scheduled before requesting the letter.** Cost: the prescriber's office moves at office pace; the result posts first; every later document is a rebuttal instead of a footnote.
2. **Submitting the pharmacy printout as the explanation** (the m-branch). Cost: ten days in which the file's only account of a positive result is the phrase "possible impairment," unanswered by anything a prescriber signed.
3. **Declining the screen** (the h-branch). Cost: the petition posture — the question stops being what the medication explains and becomes what the father is hiding, which is the one question his paper cannot answer for him.
4. **Letting the closing keep the shorthand.** Cost: "possible impairment" survives into the permanent summary although the letter in the same file names the medication; the route's last move exists because closings are quoted and letters are not.

## (5) What no strategy controls

The prescriber's office's speed, the lab's turnaround, and whether the worker reads the packet before or after the result. The route controls only what was ever controllable: that the letter was requested before the screen existed, chased daily, and filed first. Outcomes in this system turn on workers, judges, and luck as much as on any parent's choices — the strategy's claim is narrower: when the result arrived, it arrived second.

---
*Verification: this route was walked programmatically against `scenario-44.json` — each named choice was followed from the start node in order; every flag-gated choice's requirements were satisfied by flags set earlier on the walk; the walk terminates at the ending node titled "Explained Before It Posted" after visiting 13 nodes, with $155 of the $155 starting cash remaining (no choice in this scenario carries a cash cost; the starting cash never moves). Walked path: The Kettle → The Ask → What the File Says So Far → Saturday, Reconstructed → The Letter, Requested → Molly's Teacher → The Screen → Filed Before the Result Exists → Three Days → Positive, With a Footnote Already There → The Closing, Drafted → Sign Here → Explained Before It Posted.*
