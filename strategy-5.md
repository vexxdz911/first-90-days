# Strategy Guide — Scenario 5: “The Missed Appointment” (Foundation tier)

*Game documentation for a fictional simulation in* The First 90 Days. *It describes choices and outcomes inside this scenario only — general information, not legal advice for any real case.*

## The win

**Recorded as What It Was** (`end_good`) — the best ending reachable in this scenario. It is a partial, honest win: The miss is in the file as what it was: a bus that did not come, a parent who called at 7:34, a screen completed. The plan continues unchanged — no extra check-ins, no tightened terms.

## The route

- **Your Copy, Your Proof** (`records`) → choose: “Ask for the copies in writing, and wait while they are made” — Sets recordsRequested and puts the plan and appointment slip in your hands — every later check depends on knowing exactly what the paper says.
- **The Bus That Doesn’t Come** (`split`) → choose: “Call the testing office and Ms. Hart now, before 9:00, and say exactly what happened” — Sets calledAhead and records the hidden item as "called ahead, before the appointment time" instead of "no call received" — the single decision the whole scenario turns on.
- **Logged at 7:34** (`p1`) → choose: “Take the 10:30 slot and stay downtown” — Costs $6 and a morning, and converts the miss into a completed screen the same day.
- **Paper at the Desk** (`p2`) → choose: “Show her the transfer stub and the 7:34 call log, and ask her to note both” — Sets proofShown; the desk note becomes "Transportation failure — parent called ahead 7:34" instead of "parent states bus late."
- **Read Back to You** (`p4`) → choose: “Ask her to keep the note exactly as written — "called ahead, documented" — in the plan summary” — Sets wordingKept, so the careful sentence survives summarization.
- **Sign Here** (`p5`) → choose: “Read both pages before you sign — and keep your copy” — The final gate: catches the summary line before your signature blesses it, and reaches the win.

Path check: this route was walked programmatically through the scenario's choice graph (start → start → n2 → records → prep → eve → split → p1 → p2 → p3 → p4 → p5 → end_good) and reaches `end_good`. Verified at generation time; the graph validation for this scenario reported no errors.

## Why this wins — the law as it is supposed to work

- 55 Pa. Code § 3130.44(d): the agency's records on your family — the plan, the appointment slip, the updated note — are released on request. The route opens by exercising that right, in writing, before anything has gone wrong.
- Everything after that is the record working the way it is supposed to: facts entered near the time they happened, by the person who lived them, are what later readers — workers, supervisors, courts — actually decide from. A call placed before 9:00 is a fact in the file. A story told after is an opinion about the file.

## The traps

- **The Bus That Doesn’t Come** (`split`) → “Ride it out and explain everything at the desk when you get there” — Costs the timestamp. You land on the unprepared track with a NO-SHOW already boxed; the win survives only through the two repair doors (a written statement at u2 or u4).
- **Paper at the Desk** (`p2`) → “Tell the story again, and ask her to just put down that the bus was late” — Costs the proof. You drop from the prepared track to the review at u3 with "parent states bus late" as the whole record of the morning.
- **Sign Here** (`p5`) → “Sign quickly — it’s only a summary” — Closes the win outright, one step from the end: the summary shortens the line to "no-show," and your signature goes under it.
- **One More Chance to Put It in Writing** (`u4`) → “Let it go. It was one miss” — Declines the last repair door. The statement that could still have softened the summary is never filed, and the partial ending locks in.

## What no strategy controls

The 10:30 slot existed because one receptionist chose to hold it, and Ms. Hart chose to offer a repair door she did not have to offer. A different office closes the window; a different worker writes colder. No strategy controls who is across the desk, whether the 14 bus runs, or how a supervisor reads a file on a tired afternoon. The strategy controls only what the file can honestly say about you — which, on the days when the reader is fair, is the thing that decides.
