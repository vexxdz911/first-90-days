# Strategy Guide — Scenario 123: "The Empty Chair"

*The First 90 Days — a fictional composite. Fictional composites only; no real person or case. General information about how these hearings work, not legal advice.*

> **Route verification:** this guide's winning route was graph-walked programmatically through `scenario-123.json` (every step is a legal choice; every `requiresFlags` gate satisfied by flags accumulated earlier on the route; cash never negative). Path and totals are printed at the end.

## 1. The win

**"Ending — Her Mother's Signature"** — the full win.

At the February 25 review, the court **finds Dalila located** — she was never unlocatable; a stale address and unreachable facility phones were the whole of the disappearance — **vacates the surrogate appointment**, returns every educational right to her, and declines to treat the January absence as non-cooperation, addressing service adequacy under 42 Pa.C.S. § 6351(f)(9) and (f.1) instead. Her consent, obtained and filed, covers the evaluation plan; the surrogate's interim work is ratified where it served Yasmin and noted as interim. Yasmin's classes are chosen with her mother informed, her transcript is no longer routed to an empty chair, and the next school decision lands on a desk that is occupied — by the person the law keeps in it unless a court, on a record, says otherwise.

## 2. The route — graph-verified

1. **The Chair** ("Her Mother's Signature") → **"Get the paper trail of the search. 'Cannot be located' is a claim, and claims have exhibits."** The whole scenario turns on demanding the documentation behind a status.
2. **The Lawyer** → **"Both letters. And when you find my address, Ms. Viteri, correct it like it matters — because it does."** Two defects, two paper trails.
3. **The Letters Out** → **"The finding, the appointment, and the record. All three. Cheap paper beats expensive regret."** Sets `locatedInWriting` — the location finding, the surrogate appointment, and the § 3130.44(d) record request all go out in writing; `recordsRequested` is set on the same beat.
4. **The Address** → **"Update the address in writing, signed, and ask for confirmation back."** Sets `addressFixed` — the March notice arrives, proving the fix.
5. **The Conflict, Raised Properly** → **"Raise it through channels: the supervisor, the file, the review."** Sets `conflictRaised` — the casework-affiliated surrogate candidate is challenged on the conflict rule by citation, not by accusation.
6. **The Consent** → **"Consent to the evaluation plan, in writing, with the modifications noted."** Sets `consentGiven` — the mother exercises the right the appointment said she couldn't, which is the factual predicate for vacating it.
7. **The Review** (dispatcher: `locatedInWriting` + `consentGiven`) → **"Ask the court to find her located, vacate the surrogate appointment, and return every educational right to her — with the interim acts ratified."**

**Programmatically walked path (32 nodes):** start → backstory123 → facility_call → facility_forms → lawyer123 → letters_out → records123 → mail_room → phone_bill → address_file → intake_form → candidate_list → skye_visit → corvath_meeting → assignment_news → yasmin_wishes → evaluation_explainer → consent_paper → school_visit → gal123 → thirty_days → consent_stall_check → yasmin_school_day → address_fix → packet123 → viteri_whiteboard → report123 → review_motion → yasmin_call → night_before123 → review_day → end_signature. **Ending cash: $139 of $150 left.**

## 3. Why this wins — the law

- **A surrogate parent is a substitute for an absent parent, not a parallel parent.** The rights of parents must be protected by assigning a surrogate when no parent can be identified, when the public agency — after reasonable efforts — cannot locate the child's parents, when the child is a ward of the State, or when the child is an unaccompanied homeless youth; for a ward of the State, the judge overseeing the case may appoint the surrogate instead — 34 C.F.R. § 300.519(a). *Newly verified from the eCFR text during this run; see `sources-batch-N.md`.* Every trigger is a *parental-absence* trigger. A located parent with returned rights is not one of them — which is why Dalila's filing of her own consent is not a courtesy but the legal event that ends the appointment's predicate.
- **The surrogate must be disinterested, by rule.** A surrogate may not be an employee of the SEA, the LEA, or any other agency involved in the education or care of the child, must have no personal or professional interest conflicting with the child's interest, and must have the knowledge and skills to represent the child adequately — 34 C.F.R. § 300.519(d)(2)(i) and the surrounding standards. The caseworker-affiliated candidate was excludable on the rule's face; raising it through the supervisor and the file, rather than as a courtroom accusation, is what kept the challenge curative instead of theatrical.
- **The 30-day assignment duty cuts both ways.** The SEA must make reasonable efforts to ensure a surrogate is assigned not more than 30 days after determining one is needed — 34 C.F.R. § 300.519(g). The duty's speed is meant to protect the child; it is not a license to make the predicate determination ("cannot be located") carelessly. The scenario's record — no certified mail, no facility call log, one stale address — is what "reasonable efforts" failed to look like, documented by the mother's own pulled file.
- **The surrogate's authority is real while it runs.** The surrogate represents the child in all matters relating to identification, evaluation, educational placement, and FAPE — § 300.519(h) — which is why the win ratifies the interim acts instead of pretending January didn't happen: unwinding sound interim decisions would harm Yasmin to vindicate her mother.
- **The dependency frame holds the remedy.** The vacatur is granted at a § 6351(f) review, where the court reports on services, cooperation, and the 15-of-22 posture (§ 6351(f)(9), (f.1)); the education determination is made by the bodies that own it, on the record the mother built. The § 3130.44(d) request — made in the same first letter — is what produced the search file that decides the case.

## 4. The traps

- **The Consent Withheld (partial)**: located and proved, but the evaluation consent never signed before the hearing. The court returns her rights and ratifies everything — and the spring evaluation has not begun, because the one act only she could perform stayed unperformed while she proved she was the one to perform it. Rights reclaimed must also be *used*, on the school's calendar, not the court's.
- **The Kind Stranger's Season (partial)**: challenging only the conflicted assignment wins Yasmin a better surrogate — Mrs. Skye, genuinely good — while the "cannot be located" finding stands unchallenged at the root. Dalila watches a kind stranger do, well, the job that was hers.
- **The Empty Chair, Filled Wrong**: letting the appointment ride — or forcing the conflict issue as a courtroom confrontation without the file — leaves the affiliated surrogate in place, signing an evaluation plan for a child whose mother was one phone call away all along.

## 5. What no strategy controls

Why the facility's phones went unanswered in January; whether a future facility keeps better contact information; the district's surrogate roster depth in a county with few volunteers; Yasmin's course fortunes once the transcript routes correctly; and whether Dalila's treatment program — the reason any of this happened — succeeds. The strategy controls the predicate: located, in writing, with rights exercised and the appointment vacated by the court that can vacate it. It cannot control the phones in another building, and this guide does not pretend otherwise.
