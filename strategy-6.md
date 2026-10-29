# Strategy Guide — Scenario 6: “The Folder” (Foundation tier)

*Game documentation for a fictional simulation in* The First 90 Days. *It describes choices and outcomes inside this scenario only — general information, not legal advice for any real case.*

## The win

**The Address, Corrected in Ink** (`end_good`) — the best ending reachable in this scenario. It is a partial, honest win: The referral is completed, at the right address, and the file says so — including how it was fixed: a written correction, filed by you, stamped, and verified downstream with the program itself. Anyone who reads this case later will read a story about a system error and a parent who repaired it in ink.

## The route

- **The Whole Referral, Please** (`records`) → choose: “File the written request for the referral and address page” — Sets recordsRequested (and costs $3 for the folder). Your own copy turns the wrong address from a rumor into a correctable document — § 3130.44(d) in action.
- **What the Copies Show** (`prep`) → choose: “Draft the correction tonight: old address, new address, dates, in writing” — Sets correctionDrafted. The fix exists before the method of delivering it is even chosen.
- **The Desk, or the Phone** (`split`) → choose: “Go in person: hand in the written correction and get a stamped copy for the folder” — Sets correctionFiled. The correction enters the file as a fact with a date stamp, instead of living in a phone note as "mom called re: address."
- **Watching the Right Mailbox** (`p2`) → choose: “Call the program yourself and confirm they have the new address” — Sets verifiedDownstream — the trap in this system is that the agency’s fix does not automatically reach the other building.
- **The Intake, Attended** (`p5`) → choose: “Point it out, watch her correct it, then sign — and keep your copy” — The final gate: the summary’s wrong referral date is corrected and initialed before your signature, so the file tells the whole story, including the fix.

Path check: this route was walked programmatically through the scenario's choice graph (start → start → n2 → records → prep → eve → split → p1 → p2 → p3 → p4 → p5 → end_good) and reaches `end_good`. Verified at generation time; the graph validation for this scenario reported no errors.

## Why this wins — the law as it is supposed to work

- 55 Pa. Code § 3130.44(d): agency records — including the referral and the address page it was generated from — are released on request. The route is built on that right twice: first to see the error, later to check the summary against your copies.
- The rest is how records are supposed to work: a correction filed in writing, with dates and proof (the lease), becomes part of the record that every later reader decides from. A correction spoken by phone becomes whatever the note-taker wrote, filed wherever the note went.

## The traps

- **The Desk, or the Phone** (`split`) → “Call Mr. Adeyemi and explain the address change over the phone” — Costs the stamp. You land on the unprepared track where the old address rides again and the slot is re-offered; the win survives only through the in-person filings at u2 or u4.
- **Watching the Right Mailbox** (`p2`) → “Assume the program’s copy updated itself” — Costs the verification. The agency is fixed and the program is not; you drop to the lost-slot track at u3 even though your own correction was perfect.
- **The Intake, Attended** (`p5`) → “Sign it — the date is a detail” — Closes the win at the last desk: the summary keeps the January date, and the file quietly asks why this family took three months to engage.
- **Salvage, in Writing This Time** (`u4`) → “Ask him to just handle it this time — you’re tired of paper” — Declines the salvage filing. The new referral still goes out, but the file never gets your side in writing, and the partial ending locks in.

## What no strategy controls

Mr. Adeyemi was decent, reachable, and fair — and the address still failed twice, because decency is not a filing system. A busier worker loses the stamped copy; a different clerk mis-keys the correction; the program's waitlist moves at its own speed regardless. No strategy controls the worker, the mail, or the queue. What it controls is whether the correction exists somewhere a stranger can find it later — which is most of what a file is for.
