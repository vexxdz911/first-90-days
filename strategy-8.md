# Strategy Guide — Scenario 8: “The First Visit” (Foundation tier)

*Game documentation for a fictional simulation in* The First 90 Days. *It describes choices and outcomes inside this scenario only — general information, not legal advice for any real case.*

## The win

**Notes That Match the Day** (`end_good`) — the best ending reachable in this scenario. It is a partial, honest win: Nothing in this ending is a ruling, and it does not pretend to be one: Wren is still placed, and the road home runs through hearings this scenario does not depict. What the visits built is a record — arrival times, a kept drawing, a book resumed at the right page, goodbyes on time, and a parent's notes that agree with the supervisor's in every particular.

## The route

- **The Visit Record, Requested** (`records`) → choose: “File the written request for the visit records and guidelines” — Sets recordsRequested. You read how visits are actually scored — arrival, engagement, follow-through — before the next one happens.
- **The Bag** (`prep`) → choose: “Pack the bag tonight and lay out tomorrow’s clothes — yours and the plan’s” — Costs $5 and sets up the kept-promise test Wren runs at the visit’s first minute: the drawing, kept and brought back.
- **Visit Morning** (`split`) → choose: “Go as prepared as the week allowed: bag packed, early bus, last visit’s thread picked up” — Sets visitPrepared. Arrival time and the resumed thread become the summary’s first impression instead of its apology.
- **Notes, the Same Day** (`p2`) → choose: “Write your visit notes tonight: times, the book, the tooth, the promise, how she seemed” — Sets visitNotes. Same-day notes are what let the next visit resume at the right page — and give your version a date.
- **The Monthly Summary** (`p5`) → choose: “Read the draft carefully, and sign your acknowledgment when it matches the visits” — The final gate: the draft is checked against your notes before signature, and it matches, so it stands.

Path check: this route was walked programmatically through the scenario's choice graph (start → start → n2 → records → prep → eve → split → p1 → p2 → p3 → p4 → p5 → end_good) and reaches `end_good`. Verified at generation time; the graph validation for this scenario reported no errors.

## Why this wins — the law as it is supposed to work

- 55 Pa. Code § 3130.44(d): the visit records and guidelines in your case record are released on request. The route uses that right twice — to learn the criteria before the visit, and to compare the summary against your own notes after.
- The deeper principle is how dependency records work: later decisions are made from summaries of summaries by people who were never in the room. A parent who keeps dated notes and has them attached to the record is not 'playing the system' — they are supplying the system with the firsthand account it otherwise lacks.

## The traps

- **Visit Morning** (`split`) → “Go as you are — she loves you, and that’s the visit” — Costs the theme of the month. The visit stays warm but reads as postponement; the win survives only through the same-night repair at u2 or the attached notes at u4.
- **Notes, the Same Day** (`p2`) → “Write them this weekend, when it’s quieter” — Costs the details. You drop to the memory track at u3, where the thread gets fumbled in front of the pen that records it.
- **The Monthly Summary** (`p5`) → “Sign it without reading — she’s been fair all along” — Closes the win at the draft table: a clerical swap makes your best visit the late one, and your unread signature leaves it standing.
- **A Fair Sentence, Offered a Door** (`u4`) → “Tell her thanks — you’ll keep it all in your head” — Declines the attachment door. The supervisor’s summary becomes the only version of the month in the building.

## What no strategy controls

Wren was already placed when this story opened, and no visit strategy in it decides placement — that honesty is the point of the tier. Ms. Onyema wrote fairly and offered doors out loud; a colder supervisor writes the same hour smaller, and judges read identical summaries through different lives. No strategy controls the pen, the bus, or the bench. It controls whether your half of the hour exists somewhere besides your memory.
