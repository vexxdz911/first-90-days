# Strategy Guide — Scenario 119: "Two Signatures"

*The First 90 Days — a fictional composite. Fictional composites only; no real person or case. General information about how these hearings work, not legal advice.*

> **Route verification:** this guide's winning route was graph-walked programmatically through `scenario-119.json` (every step is a legal choice; every `requiresFlags` gate satisfied by flags accumulated earlier on the route; cash never negative). Path and totals are printed at the end.

## 1. The win

**"Ending — The Order Names Who Signs"** — the full win.

At the December 3 review, the court **orders, in writing**: for scheduled dental and medical care, the agency requests the mother's written consent **five business days ahead** with the provider's plan attached; the foster parent may consent to **emergency care only**, with notice to the mother the same day; the agency gives the mother every provider's name and appointment notice **before**, not after; and Navya's stated preference for the familiar dentist is entered in the record. The surgery happens December 8 with Kavita's signature on the consent and Kavita holding her daughter's hand in recovery. The win is not the surgery — it is the *order*: consent authority for the rest of the case now has names, notice periods, and an emergency definition, instead of a practice nobody wrote down.

## 2. The route — graph-verified

1. **The Consent in the Chart** ("The Signature She Never Gave") → **"Ask for the order itself. What did the court actually say about consent?"** The governing text turns out to be one line: *the agency shall arrange for appropriate medical and dental care.*
2. **The Lawyer** → **"Ask her to draft the ask: written notice before, consent from me for scheduled care, foster consent for emergencies only."** The demand is drafted before any confrontation.
3. **The Dentist** → **"Take the weekday off. You want the treatment plan from the dentist's mouth, in front of the caseworker."** Sets `noticeAsked` — Kavita hears the actual cavity count and asks, in the chart's presence, how consent will be documented.
4. **The Chart Note** → **"Note it, and ask for the note in the agency record."** "Mother requests written notice before any scheduled procedure and consents to be asked first" becomes a dated chart entry.
5. **A Second Pair of Eyes** → **"Book the consult. A second professional opinion turns a preference into evidence."** Sets `secondOpinion` — a pediatric dentist concurs on scope and flags the antibiotic course as the time-sensitive part.
6. **The Record, On Paper** → **"Ask for the agency record in writing... Under § 3130.44(d)..."** Sets `recordsRequested` — the routing is provable: the notice reached the foster home because nobody was assigned to route it to the mother.
7. **The Hearing** (dispatcher: `noticeAsked` + `secondOpinion`) → **"Ask the court to write the consent order: notice five business days ahead, mother consents to scheduled care, foster parent for emergencies only, same-day notice."**

**Programmatically walked path (21 nodes):** start → how_we_got_here → yuen_call → lawyer119 → dentist_call → visit_teeth → agency_reply → franca_meeting → dentist_office → second_opinion → navya_questions → consult_day → records119 → transport_plan119 → yuen_support → packet119 → objection → gal_call → night_before119 → hearing119 → end_order. **Ending cash: $103 of $130 left.**

## 3. Why this wins — the law

This guide states no medical-consent statute, because none was verified from primary text during this run — and the scenario is built so it does not need one. What the verified set supplies is the machinery the win actually uses:

- **Placement does not silently rewrite a court's order.** A court that assumes jurisdiction keeps the case, and changes to how a placed child's care is authorized happen the way everything else in dependency happens: on notice, at a hearing, in an order. The February blanket line ("the agency shall arrange for appropriate medical and dental care") authorized *arranging*; Kavita's ask simply makes the court say who *consents*, treatment class by treatment class.
- **The review hearing is where practice becomes findings.** A court reviewing a placement examines the child's safety, the continuing necessity and appropriateness of the placement, compliance with the permanency plan, and the services and cooperation around it — 42 Pa.C.S. § 6351(f). A documented pattern of after-the-fact notice is exactly the kind of record those findings are made from; an order allocating consent is a disposition the court can write at that hearing.
- **The record request is the spine.** Under 55 Pa. Code § 3130.44(d), the mother (or her attorney) may obtain the agency record. The chart note and the two-version appointment notice are the exhibits; without them, the hearing is her word against a practice.
- **A parallel right likely exists in medical-consent doctrine for parents of placed children** — parental rights not expressly limited by an order are generally understood to persist — but this guide does not state that body of law, because it was not verified from primary sources during this run. The win here is deliberately built to stand on the dependency court's own order-writing power, which was verified in prior batches.

## 4. The traps

- **Trusting the verbal fix** (Told Afterwards (partial)): the caseworker agrees notice "should" come first, the surgery is treated kindly — and at the next provider, the routing is the same as before, because agreement without an order binds no one. The partial is labeled partial: the child was treated; the practice stands.
- **Declining the second opinion** leaves the ask resting on a mother's preference against a provider's plan; at the hearing the scoped version of the order is what survives, notice included but consent split by default practice.
- **Skipping the chart note**: the single most portable exhibit in the case is the sentence the dentist's office wrote the day Kavita asked. Without it, her ask exists only in her own testimony.

## 5. What no strategy controls

Whether the cavities were as advanced as feared; the surgical schedule and the anesthesiologist's judgment; whether the next provider the agency chooses documents as carefully as Dr. Sorrel; Navya's fear of the mask; and whether the agency's internal routing improves for the next family — the order binds this case, not the agency's habits everywhere. The strategy controls who signs, who is told, and when, for Navya, in writing. It cannot control the dentistry, and this guide does not pretend otherwise.
