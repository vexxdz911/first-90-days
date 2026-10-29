# Strategy Guide — Scenario 39: "The Interview at School"

*Game documentation for a fictional simulation in "The First 90 Days" (Tactic Watch). The family, the case, and every choice below are fictional. This guide is general information about how the scenario is built — it is not legal advice for any real case.*

## (1) The win

**Best ending: "Her Words, and Yours Beside Them"**.

This is a **full** win. A ten-year-old was interviewed at school before her parent knew a report existed. The route cannot undo that interview — no route can — but it puts the child's exact words, written down the same night, and her caregiver's documented arrangement into the file beside the worker's summary of them, and the case closes on the complete record rather than the summary alone.

## (2) The route

Verified by walking the scenario graph from the start node (see the verification note at the end). Key decision points, in order — node title, winning choice, and what it changes:

1. **What Hana Said** — *Write down Hana's account tonight, in her words, dated — what she was asked, what she answered.* Sets **verbatimTonight**.
2. **The File Already Exists** — *File the written request for the record, interview summary included.* Sets **recordsRequested**.
3. **The Arrangement, Documented** — *Assemble it: roster, route, Mrs. Whitlock's written statement of the arrangement.* Sets **proofGathered**, **neighborStatement**.
4. **The Call** — *Walk her through it — Hana's own account, the two work days, Mrs. Whitlock — and send the correction in writing.* Sets **correctionSent**.
5. **Read Back to You** — *Confirm it — and ask for the amended summary in writing for your folder.* Sets **summaryInWriting**.
6. **The Last Line** — *Read it all — sign, and attach a one-line note pointing to the amended summary.* Sets **readBeforeSigning**.

## (3) Why this wins — the law as it is supposed to work

- **The file already exists, and it is requestable.** The interview produced a summary before the parent knew there was anything to summarize. Agency records are released on request — 55 Pa. Code § 3130.44(d) — and this scenario's first strategic fact is that the request explicitly includes the interview summary, the document every later conversation will quietly quote.
- **A child's words survive in the file in two forms: a worker's summary and a parent's same-night verbatim note.** Only one of those was written by someone who was trying to remember. The dated verbatim note is not a contradiction of the summary; it is the standard against which the summary can be checked — and, where it differs, corrected in writing.
- **The arrangement the report questioned is answered with its own paper**: a roster, a route, and the caregiver's written statement — documents that existed or were made once, in writing, rather than assurances repeated on calls.

## (4) The traps

1. **Letting the account become what "usually" happens** (the u-branch). Cost: the file closes around the adverb — "Usually, In the File" — and the one document that could have anchored the child's actual words was never written while they were fresh.
2. **Waiting to write the child's account down.** Cost: no **verbatimTonight** — a note written days later is a reconstruction, and the scenario treats it as one.
3. **Requesting "the record" without naming the interview summary.** Cost: the packet that arrives answers a different question, and the summary goes uncorrected into the closing.

## (5) What no strategy controls

What the child actually said in a room the parent was not in, how the worker summarized it, and whether the school cooperates promptly. The route controls only what was ever controllable: that her words were written down the night she said them, that the summary was requested by name, and that the correction was sent in writing. Outcomes in this system turn on workers, judges, and luck as much as on any parent's choices — the strategy's claim is narrower: when this file was read, it contained her words and not only a summary of them.

---
*Verification: this route was walked programmatically against `scenario-39.json` — each named choice was followed from the start node in order; the walk terminates at the ending node titled "Her Words, and Yours Beside Them" after visiting 12 nodes, with $140 of the $140 starting cash remaining (no choice in this scenario carries a cash cost; the starting cash never moves). Walked path: The Call from the School → What Hana Said → The File Already Exists → The Arrangement, Documented → The Night Before Her Call → The Call → Read Back to You → Mrs. Whitlock, In Person → A Tuesday, Observed → Closing → The Last Line → Her Words, and Yours Beside Them.*
