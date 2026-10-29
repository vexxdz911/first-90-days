# Strategy Guide — Scenario 11: “The Interpreter” (Foundation tier)

*Game documentation for a fictional simulation in* The First 90 Days. *It describes choices and outcomes inside this scenario only — general information, not legal advice for any real case.*

## The win

**Understood, in Writing** (`end_good`) — the best ending reachable in this scenario. It is a partial, honest win: The win is understanding, made durable: a meeting held with interpretation, papers read at full speed, choices — including a declined one — recorded as choices, and a signature that means what signatures are supposed to mean. Marco's services start on the schedule that was actually agreed, because the agreement was actually made.

## The route

- **The Request, in Writing** (`records`) → choose: “Send the written request: interpreter for Friday, papers in Spanish, copies for your records” — Sets recordsRequested and interpreterRequested before the meeting — the request exists on paper, dated, copied to your lawyer, before anyone has to remember whether it happened.
- **The Meeting Room** (`split`) → choose: “Show your copy of the written request, and ask that the signing wait for the interpreter — or that the meeting be rescheduled with one” — Sets heldTheLine — the hinge of the scenario. The copy in your hand converts a "short week" apology into a reschedule with nothing signed uninformed.
- **The Packet, Read at Full Speed** (`p2`) → choose: “Mark the two pages and write your questions beside them, for Tuesday” — Sets fullyRead: the Spanish packet reveals one "mandatory" service is optional and one "requirement" is a declinable permission — the facts Tuesday is fought over.
- **Tuesday, Translated** (`p3`) → choose: “Ask, through Carmen, that the meeting summary state what was optional and what you declined” — Sets summarySpecifics. A declined permission, recorded as declined, cannot quietly become a granted one downstream.
- **For the Record** (`p5`) → choose: “Sign, having read it in a language you read at full speed” — The final gate: the signature finally means informed agreement — the only kind the win is made of.

Path check: this route was walked programmatically through the scenario's choice graph (start → start → n2 → records → prep → eve → split → p1 → p2 → p3 → p4 → p5 → end_good) and reaches `end_good`. Verified at generation time; the graph validation for this scenario reported no errors.

## Why this wins — the law as it is supposed to work

- 55 Pa. Code § 3130.44(d): your case records are released on request. The route’s first move bundles that verified right with the interpreter and translation requests in one written document — the scenario is explicit that the record right is the cited law here, and it invents no other entitlement.
- 42 Pa.C.S. § 6337's counsel right is the route's quiet second pillar: your lawyer holds copies of everything from the start (records and prep beats), which is why a drifting meeting would have been caught in days rather than never. The written request, copied to counsel, is how a parent makes both rights operational at once.

## The traps

- **The Meeting Room** (`split`) → “Stay and nod through it — don’t be difficult, Marco needs the services” — Costs the meeting’s meaning. Three forms get signed at seventy percent comprehension; the win survives only through the written repair (u2) or the filed disagreement (u4), and even then Friday’s signature stays in the file.
- **Tuesday, Translated** (`p3`) → “Let the summary be a summary” — Costs the specifics: you drop to the confident-summary track at u3, where "services accepted, permissions granted" becomes load-bearing for every later decision.
- **For the Record** (`p5`) → “Sign quickly — this one you already know is right” — Closes the win at the last line: the record’s start date is wrong by a week, your unread signature accepts it, and the error surfaces on a Monday morning, at a program door, through Marco.
- **A Second Meeting, Offered** (`u4`) → “Attend but let Ms. Ferreira do the fixing — you’re tired of rooms” — Declines the last door in your own voice: the fix happens, but the record credits your lawyer’s voice where yours will be needed in every future room.

## What no strategy controls

Carmen existed, the supervisor said yes to a reschedule, and Ms. Doyle did not get defensive — none of that was guaranteed, and in another county office, in another week, the same written request meets a shrug and a longer wait for an interpreter. No strategy controls staffing, schedules, or whether paper moves the person holding it. What the written request controls is the record: whatever happens Tuesday, the file will show you asked, in advance, in writing — and a meeting described later as one you 'attended and agreed' will have to reckon with that page.
