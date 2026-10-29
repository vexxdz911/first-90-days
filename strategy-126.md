# Strategy Guide — Scenario 126: "In Her Own Words"

*The First 90 Days — a fictional composite. Fictional composites only; no real person or case. General information about how these hearings work, not legal advice.*

> **Route verification:** this guide's winning route was graph-walked programmatically through `scenario-126.json` (every step is a legal choice; every `requiresFlags` gate satisfied by flags accumulated earlier on the route; cash never negative). Path and totals are printed at the end.

## 1. The win

**"Ending — Quoted, Not Paraphrased"** — the full win.

At the April 8 permanency hearing, the court report the judge works from contains Destiny's statement **verbatim, attributed, in her section** — placed there because her mother demanded the correction in writing before the hearing, and the agency corrected it rather than defend the paraphrase. The court **quotes her on all three subjects**: the move was handled with honest notice and she accepts it; school continuity is ordered via the district's written transportation procedure; and the medication review she asked for is **ordered with a date**, with the prescriber's reasoning to be filed. The court finds the placement change necessary but orders it done the way Destiny specified where the record allowed, and addresses the September 12, 2027 fifteen-month date under 42 Pa.C.S. § 6351(f)(9) with the mother's progress findings attached. The win's essence: a sixteen-year-old's words entered the file as *hers* — which is what made them usable by a judge at all.

## 2. The route — graph-verified

1. **Her Words, Filed** ("The Letter") → **"Help her file it exactly as written. Her words, her signature, her date."** Sets `statementVerbatim` — a signed, dated, verbatim statement enters the custody of the file before any report summarizes it.
2. **The Record** → **"Ask for the agency record in writing... Under § 3130.44(d)..."** Sets `recordsRequested` — and the record answers the transcript mystery: two classes were restored by the sending school, and nobody told Destiny.
3. **The Medicine Question** → **"Send them. A prescriber's reasoning belongs in the file of the child swallowing the pills."** Sets `medReview` — Dr. Iyer's written reply concedes the noon drowsiness is worth a formal review; the request becomes clinical, not adversarial.
4. **The Correction** → **"Sign it. The record becomes quotes from tonight forward."** The written correction demand — replace the paraphrase with the verbatim statement, or attach the whole statement and note the dispute — is filed the same evening the draft report arrives.
5. **The Hearing** (dispatcher: `statementVerbatim` + `medReview`) → **"Ask the court to work from the verbatim statement, order the medication review with a date, and note the school-continuity finding."**

**Programmatically walked path (34 nodes):** start → destiny_reaction → backstory126 → lawyer126 → caseworker_meet → paraphrase → shirley_progress → statement_draft → statement_filed → school_front → destiny_school_day → records126 → transcript_gap → halden_meet → asare_goodbye → move_day → med_front → pharmacy_refill → med_fork → adeyemi_reply → march_counselor → destiny_letter_friend → ap_decision → bid_meeting126 → transport_plan126 → fifteen_months → report126 → report_quote_check → ibe_position → packet126 → yusuf_findings → night_before126 → hearing126 → end_quoted. **Ending cash: $122 of $130 left.** *(Names in text are the Trejo family, Dr. Iyer, and Ms. Petrides; two node ids — `adeyemi_reply`, `march_counselor` — retain pre-rename surnames from drafting.)*

## 3. Why this wins — the law

- **A child's stated wishes are findings material, not color.** Dependency courts decide placement and permanency on records that include the child's own position — carried by the guardian ad litem, the court report, and, at sixteen, by a statement the young person can sign herself. The scenario's mechanics are the verified ones: what enters the agency record (§ 3130.44(d) lets the parent obtain it — which is how the paraphrase was caught), what the court report carries into a § 6351(f) hearing, and what findings the court can write from it. A verbatim statement is *evidence*; a paraphrase is a claim about evidence, and the correction demand is the instrument that converts one into the other.
- **School continuity rides the same statute as Scenarios 117 and 121.** School of origin unless a best-interest determination says otherwise — 20 U.S.C. § 6311(g)(1)(E)(i) — with transportation under clear written procedures and shared costs — § 6312(c)(5)(B). *Newly verified during this run; see `sources-batch-N.md`.* Destiny's ask is narrower than her mother's case: fund the AP-year route *her* way, through the written procedure, and put her reasoning in the determination record.
- **Treatment changes in placement generate record duties.** As in Scenario 120, no psychotropic-medication consent statute is stated — none was verified from primary text this run. The win uses § 6351(f)'s review of services and the placement's appropriateness: a prescriber's written reasoning, solicited by the parent and answered clinically, gives the court something orderable (a review, with a date) instead of something arguable (a feeling about a dose).
- **The clock is named before it is near.** Destiny entered care June 12, 2026; the 15-month date is September 12, 2027 (§ 6351(f)(9), (f.1); 42 U.S.C. § 675(5)(E)). Findings about a mother's progress are worth most when a court writes them with the filing date in view — which is an argument for verbatim records generally: exceptions under (f.1) are proved from files, and files are made of exactly this kind of page.

## 4. The traps

- **Heard, Except About the Medicine (partial)**: the statement is quoted and the school is saved, but the medication questions were never sent — so the one subject on which Destiny asked for a *process* gets a paragraph of a caseworker's summary ("Destiny has some concerns about feeling tired") and no review. Courts can only order what the record frames.
- **The Summary of Her (partial)**: the records fight wins the transcript classes, but the statement was never filed verbatim — Destiny's positions reach the judge as report language, credited politely and weighted as color. Her transcript is whole; her voice is summarized.
- **Third Person**: no statement, no questions, no correction — the report's account of Destiny (resistant, attached, tired-sounding) is the only Destiny in the room, and the hearing proceeds on her as described.

## 5. What no strategy controls

What Destiny actually wants in six months — a sixteen-year-old's considered position can change, and a verbatim record of March is not a command to September's Destiny, only proof she was heard when she said it. Whether the medication review changes the prescription (Dr. Iyer's judgment governs); Mrs. Halden's fit over a school year; the AP results; Shirley's own treatment arc, which the findings credit but cannot complete; and the September 2027 clock, which good findings inform but do not stop. The strategy controls whose words the file holds and whether treatment questions get clinical answers in writing. It cannot control what a sixteen-year-old decides to want next, and this guide does not pretend otherwise.
