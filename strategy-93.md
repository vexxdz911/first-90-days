# Strategy Guide — Scenario 93: "Fourteen Days"

*Game documentation for a fictional simulation in "The First 90 Days" (Tactic Watch). The family, the case, and every choice below are fictional. This guide is general information about how the scenario is built — it is not legal advice for any real case.*

## (1) The win

**Best ending: "Affirmed Where It Mattered, Reversed Where It Counted."**

State it honestly: this is a **partial** win. The agency's appeal fails — the kinship-custody order for the twins is affirmed — and the mother's cross-appeal succeeds in part: the visitation schedule is vacated and remanded with directions, and the review structure must account for her documented progress. The twins do **not** come home; reunification remains the goal, not the fact. What was won is the placement's legal security plus the afternoons — and both halves run through the same hinge: a cross-appeal that existed because a family watched a mailbox for the agency's notice like the notice was money.

## (2) The route

Verified by walking the scenario graph from the start node (see the verification note at the end). Key decision points, in order:

1. **Ms. Kaur Draws Three Lines** — learn the board: the agency's 30-day appeal clock (Pa.R.A.P. 903(a)); the cross-appeal's 14-days-from-service clock (903(b)); and the case below, which pauses for neither.
2. **The Phone Tree** — *Set the phone tree and write both clocks on the calendar.* Sets **clocksKept**. The fourteen days run from **service** of the agency's notice; the route's first asset is a family organized to know the day it lands.
3. **Fourteen Days** — *Decide the two claims and start the record work the same day.* Sets **crossDecided**: visitation and review structure — preserved, documented, winnable. Everything else is memoir.
4. **The Record, For Two Appeals** — *Order the complete transcripts and request the full agency record, in writing.* Cash −30. Sets **recordsRequested** (55 Pa. Code § 3130.44(d)).
5. **Grandmother's House, On Paper** — *Have the kinship file indexed and completed.* Sets **kinFile** — one of the two flags the winning argument choice requires. The agency's appeal attacks the placement; the defense is the assessed, documented house, in a format a panel can notice.
6. **The Mailbox, Day Eighteen** — *File the cross-appeal on day nineteen as planned.* Sets **crossFiled** (at "Filing the Cross-Appeal") — nine days after service, inside the fourteen, with the thirty-day backstop untouched.
7. **Reading the Other Side First** — build both briefs against the agency's actual placement memorandum (**memoRead**), obtained through the record request.
8. **Two Briefs, One Record** — *Check every citation in both briefs against the certified record.* Cash −10. Sets **briefChecked**.
9. Line three, fed throughout: the enrollment packet (**schoolFiled**), the specific visit notes (**visitLog**), and the written summary at the interim review (**reviewRecord**, cash −10). You finish with $120 of the $170 start.
10. **Argument, Twice** — *Defend the kinship order on its record AND press the cross-appeal on visitation.* Flag-gated on **crossFiled** + **kinFile**. Both captions argued; the cross pressed, not merely filed.

## (3) Why this wins — the law as it is supposed to work

Only principles from the scenario's verified set are stated here:

- **The clocks are Pa.R.A.P. 903's, verified from the official text for this batch.** A notice of appeal is due within 30 days after entry of the order (903(a)). If a timely notice is filed by one party, any other party may file a notice of appeal within 14 days of the date the first notice was served, or within the time otherwise prescribed, whichever period last expires (903(b)). The scenario dramatizes the rule's structure faithfully: the mother's outer limit was her own thirty days (September 2), the fourteen days ran from the agency's August 12 service (to August 26), and the route files on day twenty — early, on purpose, because margins are for weather.
- **The defended order rests on 42 Pa.C.S. § 6351(a)(2)(i)** — temporary legal custody to a qualified individual, including a relative — made with § 6351(b) findings on a documented record, while the case below kept running its § 6351(f) determinations at the § 6351(e)(3)(i) rhythm.
- **Both appeals are read from one certified record**, assembled through 55 Pa. Code § 3130.44(d) — including, decisively, the other side's own placement memorandum.

## (4) The traps

1. **Setting the cross-appeal aside at "The Mailbox, Day Eighteen"** because defending the order feels like enough. The cross-appeal never exists; the argument node offers only the single-caption morning, and the story ends at "The Door That Was Never Opened" — placement affirmed, afternoons forever unreviewed. This is the scenario's central trap and it is a *non*-act: no one errs, no one is careless in the room; a window simply closes, unsounded.
2. **Polishing past the plan at the same node.** The day-twenty-four filing survives on 903(b)'s "whichever expires last" — the scenario lets it live, and makes the family live with having risked the entire cross-appeal for four days of phrasing. Margins are a doctrine because weather is real.
3. **Resting the cross-appeal entirely on its brief at argument.** Ends at "The House Held; The Afternoons Didn't Move": the defense wins outright, the cross is treated as an afterthought with citations. Panels decide what is pressed, warmly, in the room.
4. **Spending the argument on the nine months and the first worker.** Ends at "Vacated: The Argument That Wasn't Made" — the agency's framework argument meets no record-based resistance, and the kinship order itself falls. Grievance is not merely a weak lead; here it is an expensive one, because it spends the defense too.

## (5) What no strategy controls

The panel's view of kinship versus licensure as a matter of emphasis; appellate time measured against first grade; the agency's next filings below; the remand court's visitation arithmetic. The route controlled clocks, claims, citations, and the case below's paper. That is the whole of what any appellant controls — and this scenario's evidence that it is not little: a placement kept, a schedule doubled, a family's autumn read into law by three judges who never met the twins, because a phone tree caught an envelope on day nine.

---
*Verification: this route was walked programmatically against `scenario-93.json` — each named choice was followed from the start node in order; every intermediate node and choice exists; the flag-gated choices' requirements (crossFiled at the courthouse; crossFiled and kinFile at argument) were satisfied by flags set earlier on the walk; the walk terminates at the ending node titled "Affirmed Where It Mattered, Reversed Where It Counted" after visiting 28 nodes, with $120 of the $170 starting cash remaining.*
