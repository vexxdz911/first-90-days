# Strategy Guide — Scenario 45: "The First Thirty Days"

*Game documentation for a fictional simulation in "The First 90 Days" (Tactic Watch). The family, the case, and every choice below are fictional. This guide is general information about how the scenario is built — it is not legal advice for any real case.*

## (1) The win

**Best ending: "Home at Adjudication"**.

This is a **full** win. Two children are removed at night over a broken latch and a hallway. What brings them home at adjudication (day 24; the ending lands day 27) is not a speech about the latch — it is the month's paper: the landlord's texts and work order, the grandmother's kinship packet, the assessment's ratings answered rating by rating in a written rebuttal, and a plan completed early and documented daily. The scenario offers three lesser landings — with grandmother on the record (a partial win, and named as one), placed on a plan she built (partial), and placed on a plan handed down (hard) — and the differences among all four are differences of record, not of devotion.

## (2) The route

Verified by walking the scenario graph from the start node (see the verification note at the end). Key decision points, in order — node title, winning choice, and what it changes:

1. **The First Night** — *Write tonight's timeline before sleeping — the texts to Beck, the evening, the times, who came, what was said.* Sets **timelineWritten**, **landlordTexts**. The landlord texts gate both the shelter care hearing and the adjudication.
2. **The Petition, Read** — *File the written record request — petition, intake, removal notes — and mark every claim the petition makes.* Sets **recordsRequested**.
3. **Friday Morning** — *Assemble both packets — landlord's paper and grandmother's — exhibits for counsel by noon.* Sets **landlordFix**, **kinshipReady**.
4. **The Shelter Care Hearing** — *Have counsel present the landlord record and the grandmother's packet — texts, work order, two beds made up since Wednesday.* Flag-gated on **landlordTexts**. The children are transferred to their grandmother, on the record, instead of remaining in stranger foster care.
5. **The Assessment Visit** — *Ask, on the record of the visit: which items were rated, who rated them, and how to obtain the results.* Sets **askedItems**.
6. **What Kind of Form Is This** — *Have counsel put the request in writing this week — results, rater notes, the record relied on.* Sets **recordSeen**.
7. **The Score Arrives** — *File the written rebuttal: rating by rating, the work order and texts attached.* Sets **rebuttalFiled** — the second flag the adjudication is gated on.
8. **Services, Hers** — *Complete the plan's items early and document each completion the day it happens.* Sets **planCompletedEarly**.
9. **Adjudication** — *Put the whole record: burden unmet — texts, work order, rebuttal, kinship, log.* Flag-gated on **landlordTexts** + **rebuttalFiled**.

## (3) Why this wins — the law as it is supposed to work

- **The first clock is 72 hours.** After a removal, a shelter care hearing must be held within 72 hours (42 Pa.C.S. § 6332; 23 Pa.C.S. § 6315(d)). This scenario starts Tuesday night, March 3, 2026, and its hearing node lands on day 3 — Friday, March 6, 2026, exactly on the clock. The hearing's narrow question is where the children must be while the case is decided, and the grandmother's packet is what gives the court a documented answer other than the foster home.
- **Counsel is machinery, not decoration** (42 Pa.C.S. § 6337; § 6332(a)): the route feeds counsel exhibits the night they are made, because a lawyer arguing from a folder she received in the hallway is the hallway version of this case.
- **The record — including the assessment — is requestable, and its redactions have a limit.** Agency records are released on request (55 Pa. Code § 3130.44(d)), and § 3130.44(f) limits what may be withheld: the rater's notes about a family are the family's record, not the staff's private papers. The foster-arm branch of this scenario is built on pressing exactly that point against a redacted file.
- **The assessment can be answered.** Court rules on family service plans and assessments (Pa.R.J.C.P. 1340(A), (B)(1), (E), (F)) contemplate assessments being shared and answered, and the route files a written, item-by-item rebuttal under that framework. The scenario flags honestly, in its own text, that Rule 1340's application to the agency's specific scored instrument is **untested** — and the route is built so the case never needs the point decided: the rebuttal is filed, attached to documents, and argued alongside the burden.
- **The burden at adjudication is the agency's**, and the win is framed as the data frames it: on this record — a documented repair, a documented home, a rebutted score — the petition's account of an unsafe hallway cannot carry it.

## (4) The traps

1. **Spending the first night calling instead of writing.** Cost: no **landlordTexts** preserved as a timeline product — the texts exist on a phone, scattered, and neither the shelter care hearing nor the adjudication can be gated open. Both courtroom wins close on night one.
2. **Taking the foster arm and treating the placement as the case.** Cost: the kinship packet is assembled late (**kinshipReady** never set in time), the children spend the month in stranger care, and the best available ending becomes the partial "Placed, With a Plan She Built."
3. **Reading the score without rebutting it in writing.** Cost: no **rebuttalFiled** — the ratings stand in the file unanswered, and at adjudication an unanswered form is treated as an agreed one.
4. **Accepting the redacted file as the file.** Cost: the ratings are argued from the agency's excerpts; the (f) point — that the notes are the family's record — is never made, and the assessment's basis stays the one thing in the case nobody has seen.

## (5) What no strategy controls

The judge at shelter care, the rater's habits, the landlord's speed with the repair itself, and whether the grandmother's home passes its own checks. The route controls only what was ever controllable: that the night was written down, the packets existed by Friday, the score was rebutted on paper, and the plan was finished early with dates. Outcomes in this system turn on workers, judges, and luck as much as on any parent's choices — the strategy's claim is narrower: at every hearing this month, the record in the room was the truest one available, because she built it.

---
*Verification: this route was walked programmatically against `scenario-45.json` — each named choice was followed from the start node in order; every flag-gated choice's requirements were satisfied by flags set earlier on the walk; the walk terminates at the ending node titled "Home at Adjudication" after visiting 22 nodes, with $145 of the $145 starting cash remaining (no choice in this scenario carries a cash cost; the starting cash never moves). Walked path: The Hallway → The First Night → The Morning After → The Petition, Read → The Caseworker's Call → Friday Morning → The Hallway at Court → The Shelter Care Hearing → The Transfer → Grandmother's Home → The First Visit There → The Assessment Visit → What Kind of Form Is This → The Score Arrives → The Work Order → Services, Hers → Diego's School → The Review Before the Hearing → Counsel's Inventory → The Night Before Day 24 → Adjudication → Home at Adjudication.*
