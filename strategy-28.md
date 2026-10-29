# STRATEGY GUIDE — Scenario 28: “The Education File”

*Game documentation for “The First 90 Days,” a fictional simulation built for training and advocacy discussion. Everything here describes choices inside this scenario only. It is general information about how the simulation works — not legal advice for any real case.*

*Route verified against the data: the walk below was followed programmatically through `scenario-28.json` from the start node, choice by choice, and reaches the named ending in 31 steps. The binder gate was also checked in reverse: with the binder-building choice removed from the graph, both top endings become unreachable.*

---

## (1) The win

**Ending — Home, With the Binder** (`end_reunified`).

State it honestly: this is a **trial return home in June, under an open case** — not a closed case, not a restored-everything ending. Sam comes home for the summer with supervision and reviews continuing, and his fall return to his home school is set up with a complete handover file. What the win actually consists of is narrower and more durable than a courtroom victory: by June, **two systems that spent the fall reading two different children end the year reading one reconciled record** — and every decision made from that record (the trial return, the delivered school plan, the handover) is made about the real Sam. No petition is defeated in this scenario, because none is filed; the federal filing clock never reaches its trigger during the school year. The win is a record, a placement, and a summer — earned on paper, and still supervised.

The runner-up, **Ending — Two Files, One Child** (`end_aligned`), shares the same route until the final choice and is a genuinely good ending: placement stable, services delivered, reunification set for the fall. The win above is the only ending where Sam is home in June *and* the binder becomes his handover file.

## (2) The route

Start: $160, a backpack, two envelopes. Key decision points in order (node titles as they appear in the scenario):

1. **“In Writing, This Week”** — Choose: *“Sign it, copy it, and mail it today — the walk is the job.”*
   Sets **FLAG: recordsRequested**; **cash −6**; hidden item: the dated written records request. This is what makes the agency's file arrive as a task in a queue instead of a favor in a hallway, and it is the raw material for both the December correction and the binder.

2. **“While the Agency Copies”** — Choose: *“File both releases and keep both stamped copies together.”*
   Sets **FLAG: recordsRequested** a second time (deliberately — this flag covers the school file too); hidden items: releases signed at **both** schools, copies to the mother, and Hillside's contact page corrected to the mother's address. While the court side waits on copying, the school side starts moving paper toward you.

3. **“Every Address You Live At, On Paper”** — Choose: *“File the address change in writing with the agency, the court, and both schools — and keep every copy.”*
   Sets **FLAG: addressFixed**. Every missed meeting in this scenario began as a letter sent somewhere the mother doesn't live; this choice is why the February invitation, and every letter after it, reaches her.

4. **“One Sentence in a Draft”** — Choose: *“Write the correction: dated, factual, with the sign-in sheet and your stamped copies attached.”*
   Sets **FLAG: recordCorrected** and routes through **“The Correction Goes In.”** The draft sentence “Mother has not participated in education planning” is amended *before* the December review reads it as fact. Without this beat the sentence survives into the record the spring reviews inherit.

5. **“Promised and Delivered”** — Choose: *“Keep the log every week — promised beside delivered, with dates.”*
   Sets **FLAG: serviceLog**; hidden item: the dated services log. This is the document that, inside the binder, defeats the spring proposal to cut Sam's counselor check-ins — the school's file shows him thriving; only the log shows he is thriving *with* them.

6. **“The Weekend of the Binder”** — Choose: *“Build the whole binder — both files, reconciled, with the dated timeline in front.”*
   Sets **FLAG: binderBuilt**; **cash −18**. **This is the gate.** Only this choice leads to “Table of Contents,” “April in the Courtroom,” and “April in the School Meeting” — and only those nodes lead to either top ending. The binder is not a summary: it is both complete files, the log, and one dated timeline, filed with the court and carried into the school meeting, so both rooms decide from the same evidence in the same weeks.

7. **“May's Question”** — Choose: *“Take the June trial return — and carry the binder to Lincoln yourself, in person.”*
   Sets **FLAG: handoverReady**; **cash −40** → **Ending — Home, With the Binder**. The other choice at this node (stability through the summer) is not a mistake — it leads to Ending — Two Files, One Child — but it closes this win.

Cash on the winning route: $160 − $4 (the enrollment-page note in “‘Records to Follow’”) − $6 − $18 − $40 = **$92 remaining**. No choice on the route requires cash you don't have; the binder's $18 is the best money in the scenario.

## (3) Why this wins — the law as it is supposed to work

The route operationalizes only principles from the scenario's verified set; the school side is deliberately played as process, with no citations, because the scenario states no education law.

- **Speed at the start is the court's, not yours.** When a child is taken into protective custody, a shelter care hearing follows within **72 hours** (42 Pa.C.S. § 6332; 23 Pa.C.S. § 6315(d)). The scenario's hearing lands on day 3, inside the window — the system's first promise, kept on schedule, and the moment the two clocks start running.
- **You do not navigate either system unrepresented on the court side.** A parent in a dependency case has **counsel** (42 Pa.C.S. § 6337). In the route, counsel is the source of every strategic idea — the written request, the correction, the log, the binder — which is what the right is *for*.
- **Records move on written request, not on goodwill.** A party can request the agency's records, and the agency is to provide its records **on request** (55 Pa. Code § 3130.44(d)). The route uses this twice over: once for the agency file itself, and once as the model for the school side, where the same discipline — signed releases, correct addresses, kept copies — is applied as process rather than as a cited right.
- **The long clock rewards a documented record, and it had not run out.** At **15 of the most recent 22 months** in care, the agency must file or join a termination petition **unless an exception applies** — the child is cared for by a relative, a compelling reason not to file is documented, or services the plan required were never provided (42 U.S.C. § 675(5)(E)). The route never needs an exception, because June arrives at roughly month ten — but the binder is precisely the kind of documentation those exceptions, and every review before them, are read from.
- **Nothing in this win required anyone to prove anything the easy way.** Any future petition would still have to be proven by **clear and convincing evidence**. A complete, dated, reconciled record is what that standard looks like from the parent's side of the room: claims a stranger can check, filed before the hearing that would test them.

## (4) The traps

Three choices close the win outright; a fourth taxes it heavily. All four are tempting because each one is reasonable in the moment.

1. **The timeline-only build** at “The Weekend of the Binder” — *“Build the timeline only — one evening, from the agency file and memory.”* Feels like 80% of the work for 20% of the weekend. It routes to the partial branch and **Ending — Fixed at School, Open at Court**: the court's picture of the mother is repaired, the school's plan is fixed, and reunification still gets no date, because a timeline that *cites* documents it doesn't *contain* cannot testify in either room. Both top endings close here.
2. **Skipping the build** at the same node — *“Skip it — the folder has been enough so far, and April is busy.”* The folder *has* been enough, for a reader who already believes you. This routes to the drift branch: when the foster parent's own family emergency forces a placement move, Sam changes schools a second time and **Ending — The Third School** maps the cost — an evaluation completed once and started twice, nine months, no villain. The win, and the runner-up, both close here.
3. **The cautious final choice** at “May's Question” — *“Choose stability through the summer.”* This is the kindest trap: it is defensible, the record supports it, and it leads to a good ending. It still closes the win — Sam spends the summer in placement, and the binder waits for fall instead of becoming his handover file in June.
4. **The friendly shortcut** at “In Writing, This Week” — *“Ask Ms. Tran verbally at Thursday's visit first.”* This one does **not** close the win by itself, and the guide won't pretend otherwise: the written request can still be sent late, and the binder can still be built. What it costs is three weeks, the school-release beat, and the contact correction at Hillside — the slack the rest of the route spends. It is the only trap that charges interest instead of foreclosing.

## (5) What no strategy controls

The route controls the record. It does not control the people reading it, and the scenario is honest about the difference. The win leans on a foster parent who kept copies in a drawer *for* the mother and wrote a phone number across a consent form instead of signing it; on a caseworker who amended a draft sentence when shown attachments; on a counselor who adopted a parent's two-column log as the school's own form; on a judge who preferred a timeline to a summary. It also leans on luck with names blunter than those: a placement that lasted the whole school year, an evaluation that finished before spring, a review continued to exactly the month the binder was ready.

Play the same route with a placement that disrupts in April — as the no-binder branch shows can happen for reasons that are nobody's fault — and June arrives mid-move no matter what is in the binder. Play it with a different judge, a slower file room, a school whose staffing collapses in February, and the same choices buy a thinner spring. The scenario's debriefs say it in every ending, including the win: outcomes turn on workers, judges, timing, and luck. The strategy's claim is only this — of everything on that list, the record is the one item that was ever the parent's to build, and building it is the difference between being decided *about* and being decided *from*. That is all the binder does. In this scenario, it is enough. The scenario is fiction; real Junes vary.
