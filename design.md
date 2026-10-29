# THE FIRST 90 DAYS — Game Design Document

*A branching role-playing simulation of a Pennsylvania dependency case, played from the parent's side of the table.*

**Status:** Draft design, v0.1 — for internal development and attorney review before any organizational use. Nothing in this document or its companion scenario is published or sent.
**Companion files:** `scenario-1-script.md` (human-readable script) and `scenario-1.json` (engine data — identical structure, node for node).

---

## 1. Concept

The player is a parent in the first days of a child-welfare case. A report has been called in. A worker is at the door. From there, the case runs the way cases actually run: interviews, a scored assessment form the parent cannot see, safety plans, deadlines that arrive whether the parent is ready or not, court hearings where the paperwork matters as much as the facts, and a file that follows the family long after any single visit ends.

The simulation's subject is not bad parents or bad workers. Its subject is **a system experienced from inside it**: procedure, paperwork, scarcity, and clocks. The system is depicted through its ordinary operations — forms, schedules, waiting rooms, sign-in sheets — never through villains, and never through graphic content.

The title names the design's center of gravity: the first ninety days are when the record is written, the deadlines are shortest, and the parent's own moves — a letter, a request, a folder of receipts — carry the most leverage they will ever have.

## 2. Audience and purpose

**Primary audience: organizations.** Parent-defense practices, legal-aid organizations, parent-advocate and parent-mentor programs, CASA and guardian-ad-litem training programs, social-work and law schools, and the funders, legislators, and journalists those organizations need to persuade.

**This is a training and advocacy instrument, not entertainment built on trauma.** It exists so that:

- **New parent-defense attorneys and advocates** can feel the information asymmetry their clients live inside — especially being scored on criteria they cannot see — before they meet their first client.
- **Parent mentors** can walk a case end-to-end and learn where the leverage points are (they are mostly paper, and mostly early).
- **Professionals on the other side of the table** — caseworkers, supervisors, judges, students — can sit, for ninety simulated days, in the chair that has no information and no power, and carry that into their real work.
- **Decision-makers** (funders, legislators, board members) can experience in twenty minutes what a briefing document cannot convey in twenty pages.

**How organizations use it in training:**

1. **Facilitated session (60–90 minutes).** A facilitator projects one playthrough; the group votes at each choice. The debrief — not the playthrough — is the lesson. Facilitators pause at three designed moments: the interview (What is being scored right now?), the decision (What actually decides this branch?), and the record request (Why did almost nobody in the room know this right exists?).
2. **Individual assignment with written reflection.** Trainees play two different paths and compare debriefs, then answer one prompt: *Name one thing you will do differently in your next case, visit, or hearing.*
3. **Perspective curriculum (later scenarios).** The same case replayed from other chairs (see §6), used in mixed groups — attorneys, workers, and parents in one room, comparing what each role could see.
4. **Onboarding module.** Packaged with the Tactic Watch law library entries the scenario cites, so every claim the game makes can be checked against its source in one click.

**Explicitly out of scope:** marketing to parents in crisis as a game; leaderboards or social sharing of playthroughs; any use of a real family's story as content (see §8).

## 3. Core pillars

1. **You are scored on things you cannot see.** The hidden assessment is the core mechanic and the core argument. The player experiences information asymmetry as a *feeling*, not a factoid.
2. **Paper is power, and paper is burden.** Letters, sign-in sheets, schedules, and copies decide outcomes. The same paperwork that protects a family also consumes the hours a parent does not have.
3. **The clocks do not negotiate.** Deadlines are real, computed, and displayed as dates. The system is not cruel about them; it is simply indifferent, which is worse.
4. **Outcomes are not verdicts on parents.** Every ending states plainly that real outcomes also turn on workers, judges, resources, and luck. The game never says a player "lost" because they are a bad parent — and it structurally cannot, because branches turn on logistics (who can come tonight, whose supervisor signs a schedule) rather than on virtue.
5. **Every legal beat carries its receipt.** Debriefs cite the controlling law for each beat, in the same verified wording the Tactic Watch law library uses. If a point is untested, the game says so, in the open (see §9).

## 4. Mechanics

### 4.1 Deadline clocks

Cases run on statutory clocks, and the game shows them the way the deadline engine does: **trigger → rule → citation → computed date.**

- When a removal occurs, the shelter care clock starts: a hearing within 72 hours (42 Pa.C.S. § 6332; 23 Pa.C.S. § 6315(d)). The game displays the actual calendar date, computed from the scenario's start date — in Scenario 1, removal on Monday, March 2, 2026 means a hearing by **Thursday, March 5, 2026**, and the hearing node lands exactly there.
- Later scenarios add the indicated-report appeal window (90 days from notification, 23 Pa.C.S. § 6341(a)(2)) and, in long-arc scenarios, the federal ASFA timeline (15 of the most recent 22 months in foster care, 42 U.S.C. § 675(5)(E)) — introduced in Scenario 1's third debrief as the quiet clock nobody mentions.
- Clock displays are diegetic where possible (the paper the worker hands over, the court notice) and always visible in the scene header.

**Design rule:** any date the game states must be computed from the scenario's start date and the governing offset, and verified in QA the same way the app's three proven deadline cases are verified — in both the local timezone and UTC. A wrong date is a release-blocking defect, full stop.

### 4.2 The Hidden Assessment (core mechanic)

During interviews and visits, the worker completes **a scored assessment form**. The player cannot see the items, the ratings, or the running result. Choices the player makes quietly attach ratings to items (`addHidden` in the engine data): the state of the home *as observed*, the supervision plan *as understood by the worker*, the report's context *as recorded or not recorded*, cooperation *as it appeared from the other side of the table*.

Three design commitments make this mechanic honest rather than a trick:

- **The ratings respond to what the system can actually see, not to the player's intentions.** A tidy explanation and a documented fact rate differently; a true statement the worker couldn't verify rates as "unclear." The debrief shows the item list and, choice by choice, what moved it.
- **There is one in-game way to see the form: ask for it.** The record-request beat (§4.5) reveals a partial, redacted view of the accumulated items. It is deliberately the highest-leverage move in every scenario, because in the real system it is.
- **The full reveal always comes in the debrief**, whether or not the player requested the record — the training value lives there. The difference the request makes is *timing*: seeing the form at day 8 changes what you can still fix; seeing it at the debrief changes only what you understand.

The in-game instrument is always called **"a scored assessment form."** It is never called AI, machine learning, or predictive scoring — because on the public record, Pennsylvania's Universal Assessment is a structured assessment instrument with rule-based decision support, and the game does not upgrade it into something scarier for drama.

### 4.3 Resources

Three resources, kept deliberately small — scarcity is the lesson, and complexity is not:

- **Cash** (starts at $180 in Scenario 1). Choices spend it in realistic increments: a shift swap that costs weekend hours (−40), a bus across town to a visit (−12). Cash is never the difference between a good and bad parent; it is the difference between options a parent can reach and options they cannot.
- **Time** is modeled structurally rather than as a number: scenes advance by day offsets, hearings arrive on their dates, and paperwork tasks compete with shifts. A parent cannot do everything, not because a meter ran out, but because Tuesday only happens once.
- **Support network** is tracked through flags (a sister who knows, a neighbor who confirms in writing, a supervisor who signs a schedule). Support is the resource the system's forms are worst at seeing and most affected by — which is why it is flags, not points: it matters in specific, narratable ways, or it doesn't matter at all.

### 4.4 Paperwork burden

Documentation is a verb in this game. Reading before signing, asking for schedules in writing, keeping a parallel folder, writing a one-page correction — these are moves with mechanical weight. The counterweight is modeled too: every form is read at a kitchen table after a shift, and the choice to sign quickly is written sympathetically, never as a "wrong answer." The engine tracks `readPlan`, `keptFolder`, and `broughtCorrection` not to grade the player, but so debriefs can show what each piece of paper did.

### 4.5 The record request (highest-leverage move)

In every scenario there is at least one beat where the parent learns — from a flyer, a lawyer, an advocate — that they may request their assessment record, and that under 55 Pa. Code § 3130.44(d) the material "shall be released upon request." Taking the beat sets `recordsRequested`, and a later scene delivers the packet: redacted, partial, and still transformative. Debriefs call the move out by name as the single highest-leverage action in the scenario, because it converts the hidden assessment from weather into information.

A companion beat teaches the adjudication-phase disclosure rule in plain words — you get to see the evidence before the hearing that decides the facts (Pa.R.J.C.P. 1340(B)(1)) — with its honest limit stated in-game: whether that rule reaches every scored item of an assessment form is untested.

### 4.6 Choices and branching

- Choices differ **in kind, not degree** (the branch at the decision beat is *a person can come tonight* vs. *no one can* — a difference of circumstance, not of effort or love).
- Branches converge where real cases converge (both visit paths reach the same kitchen-table interview) and diverge where real cases diverge (court).
- No choice is labeled or framed as the "good parent" choice. Some good moves are invisible to the form; some visible moves are luck. The debriefs untangle which was which.

## 5. Scenario structure

Each scenario is a self-contained composite case, 25–40 nodes, playable in 15–25 minutes:

- **Act I — The report and the door** (Day 0): report, knock, home visit, the interview and the hidden form.
- **Act II — The branch** (Day 0–3): safety plan at home, or removal and the 72-hour clock; counsel; the shelter care hearing.
- **Act III — The paperwork weeks**: visits, service plan, the record request, disclosure, first review.
- **Endings (2–3 per scenario)** with full debriefs: what the form said and how choices moved it; the controlling law for each beat; the honesty paragraph (see Pillar 4).

Scenario 1, **"The Thursday Gap,"** ships with this document: a composite evening-shift mother of two, an ex-partner's report the day after a custody argument, a child briefly with a neighbor, a messy home visit — and a four-hour childcare gap on Thursdays that the entire case turns on. Its three endings (home under a safety plan; removal, then return at the hearing; removal continuing past the first review) are designed to be reached by the same parent making reasonable choices under different luck.

## 6. Perspective-switch design (later scenarios)

The scenario engine is built so the same case can be replayed from other chairs, with **different information, not just different dialogue**:

- **The caseworker** sees the form — all of it — plus a caseload counter, a supervisor's deadline, and three other families' crises competing for the same afternoon. Her constraint is not indifference; it is arithmetic.
- **The parent's attorney** sees the record and the rules, but meets the parent the day before the hearing and cannot manufacture a supervisor's signature.
- **The judge** sees only what made it into the file — and the debrief compares the file to what the player knows happened.
- **The child** (written with extreme care, older-child perspectives only, no graphic content) sees the parts adults keep explaining badly.

Perspective scenarios unlock after the parent playthrough. In facilitated settings, mixed groups play different roles through the same case and compare debriefs — the gap between what each chair could see is the curriculum.

## 7. Trauma-informed guardrails

These are release requirements, not aspirations:

- **Content warning before play**, in plain language, naming what the scenario depicts (investigation, possible temporary removal) and what it does not (no graphic content, no abuse depictions, no violence).
- **Quick Exit on every screen** — one tap leaves to a neutral page, the same pattern as the parent app.
- **Skip any scene.** Skipping never punishes progress; the debrief still delivers the legal content of skipped beats.
- **Pause and resume.** Real life interrupts; the game waits.
- **No scoring of suffering.** There are no points, streaks, grades, or "parent scores." Resources and flags exist to make consequences legible, never to rank the player. The game does not keep a win/loss record.
- **No graphic content, ever.** Hard moments — a removal, a goodbye after a visit — are written through procedure and small true details (a sleeve held, a clock on a visit-room wall), at phone-screen paragraph length, and can be skipped mid-scene.
- **Debriefs end with steadiness, not devastation:** what the law says, what leverage exists, what happens next — plus, in organizational deployments, a facilitator guide for closing a session where some participants have lived the real version of the scenario.
- **Lived-experience review.** Before any organizational release, scenarios are reviewed by parents who have been through the system (compensated, credited as they choose) and by a trauma-informed reviewer. Their notes are release-blocking, on the same footing as legal accuracy.

## 8. Composite-case doctrine

**All families in this game are fictional composites. No real person's identifiable story appears, ever.**

- Scenarios are built from published opinions, public dockets, statutes, regulations, and the *patterns* across many cases — never from one family's file. Details are merged, moved, renamed, and re-sequenced until no character maps to a real person.
- Specific prohibition: the real cases in the developer's own orbit — every family the Tactic Watch team has ever read a docket about — are **not source material**, in disguise or otherwise. Patterns may inform (paperwork decides hearings; day-0 forms get scored before help is offered); facts may not travel.
- **Consent protocol, if a parent ever volunteers their own story:** written, informed consent covering the exact script; the parent's right to review the final scenario and withdraw before release; compensation; a standing right to be credited, pseudonymous, or uncredited; and a fresh attorney review of the release. A story taken any other way ends the project, not just the scenario.
- Every scenario file carries the line that ships in Scenario 1: *"The family is fictional — a composite. No real person's story appears here."*

## 9. Accuracy doctrine

- **Verified law only.** Every legal proposition in a scenario must trace to the verified Tactic Watch law library. Scenario 1 uses only: the 72-hour shelter care rule (42 Pa.C.S. § 6332; 23 Pa.C.S. § 6315(d)); the right to counsel and appointed counsel (42 Pa.C.S. § 6337; § 6332(a)); the 90-day indicated-report appeal window (23 Pa.C.S. § 6341(a)(2)); the ASFA 15-of-22-months timeline (42 U.S.C. § 675(5)(E)); record release on request (55 Pa. Code § 3130.44(d)); and adjudication-phase disclosure (Pa.R.J.C.P. 1340(B)(1)), flagged in-game as untested for scored assessment items specifically.
- Anything beyond the verified set is written as **generic process description with no citation** — a visit room, a sign-in sheet, a stack of forms — and invents no rule, deadline, or right.
- **Debriefs cite the law for every beat** and separate three things the culture constantly confuses: what the law requires, what the game simplified, and what is untested.
- **Attorney review before organizational release**, on the same gate as every other Tactic Watch surface. Drafts circulate internally with the prototype header until then.
- **Dates are computed, never typed from memory** (§4.1's design rule), and the three proven deadline cases are re-run against any engine change.

## 10. Production notes (engine contract)

Scenarios are data, not code: a JSON file per scenario in the agreed schema (`meta`, `nodes` with `id`, `kicker`, `dayOffset`, `title`, `body`, `choices` carrying `next` and optional `cash`, `setFlags`, `addHidden`, `note`; endings carrying `debrief`). The engine team builds to that contract; writers never touch the engine. Every scenario ships as a pair — the JSON and a human-readable script generated from the same source, matching node-for-node, so legal and lived-experience reviewers can review prose without reading code. Validation is scripted: JSON parses, every `next` resolves, every node is reachable from the start, endings have no choices, day offsets never run backwards, and every stated date is checked against the calendar.

## 11. Roadmap

1. **Scenario 1** (this package): design + "The Thursday Gap," three endings, engine-ready.
2. **Facilitator guide** for Scenario 1 (Corporate Training Designer + lived-experience reviewers).
3. **Scenario 2**: the appeal clock — an indicated report, the 90-day window, and the record request as an opening move instead of a discovery.
4. **Perspective pack**: Scenario 1 replayed as worker and judge.
5. **Long-arc scenario**: months 4–15, where the ASFA clock stops being background.

---

*Design personas consulted: Game Designer (systems documentation), Narrative Designer (branching standards), Corporate Training Designer (organizational deployment), Legal Document Review and Legal Compliance Checker (accuracy gates), Academic Psychologist (trauma-informed review). Coordinated under the Agents Orchestrator pattern. Draft — not legal advice, not a depiction of any real case.*
