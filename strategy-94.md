# Strategy Guide — Scenario 94: "The Custodianship Question"

*Game documentation for a fictional simulation in "The First 90 Days" (Tactic Watch). The family, the case, and every choice below are fictional. This guide is general information about how the scenario is built — it is not legal advice for any real case.*

## (1) The win

**Best ending: "Custody With His Name in the Order."**

State it honestly: this is a **partial** win, and it is the most demanding label in the batch. Permanent legal custodianship goes to Pearl's aunt — the § 6351(f.1) legal-custodian outcome — and Pearl does **not** come home; the dependency case closes with reunification ended as a court matter. What makes it the best ending is everything around that fact: the father's contact is entered in the order as enforceable terms — Wednesdays with a 5:30 pickup, a defined monthly weekend, named holidays, school and medical access, a twelve-month review, a two-year expansion provision — negotiated in writing, agreed by both parties in a joint statement, tested in real life for two weeks, and signed by a judge. On this record — twenty-two months of a four-year-old's attachment against eight documented months of a father's stability — that is the strongest outcome that protects both the child's continuity and the father's permanence. The scenario was built to be able to say, without flinching, that not every best outcome is the one where the parent gets the child back.

## (2) The route

Verified by walking the scenario graph from the start node (see the verification note at the end). Key decision points, in order:

1. **Reading Twenty-Two Months** — *Read both binders and mark every place progress is understated.* Cash −10. Sets **recordsRequested** (55 Pa. Code § 3130.44(d)). Eleven marks: the hearing will be argued from the file's own attachments against its summaries.
2. **The Letter From the Warehouse** — the signed employment letter (**workLetter**).
3. **The Audit of Eight Months** — *Assemble the fitness packet, indexed, with the tabulation.* Cash −10. Sets **fitnessRecord** — one of the two flags the winning hearing choice requires. The packet is what makes Thaddeus's terms worth entering and his consent worth having; without it, both asks are sentimental.
4. **Weekends With Pearl** — the written log specificity (**visitLog**).
5. **The Kitchen-Table Negotiation** — *Take the written terms to mediation as the opening position.* Sets **contactTermsDraft**. Terms with numbers: the negotiation exists as a document before it exists as a conversation.
6. **The Mediated Afternoon** — *Sign the mediated terms, conditioned on the court's custodianship decision.* Sets **contactTerms** — the second required flag. The walk-out branch (see traps) reaches August with the threshold question and nothing else.
7. **The Clinic Checks the Draft** — terms tightened to order-ready specificity (**termsChecked**: pickup times, defined weekends), and **The Preschool Letter** filed and shared (**schoolLetter**).
8. **Two Packets** — the fitness packet filed and served (**packetFiled**); its shadow does the quiet work in the following weeks' phone calls.
9. **The Family Meeting** — *Sign the joint statement.* Sets **auntAgreed**: the parties agree the terms will be entered in any custodianship order, removing the father's worst outcome from the table before the hearing convenes.
10. **The Test Dinner** — the terms run informally for two weeks (cash −12; **termsTested**). You finish with $108 of the $140 start.
11. **The Custodianship Hearing** — *Consent to custodianship IF the negotiated terms are entered in the order.* Flag-gated on **contactTerms** + **fitnessRecord**: the consent is powerful precisely because the fitness record made the alternative credible.

## (3) Why this wins — the law as it is supposed to work

Only principles from the scenario's verified set are stated here:

- **The hearing's frame is 42 Pa.C.S. § 6351(f) and (f.1):** the court makes its determinations and chooses an outcome from the permanency menu, on which permanent legal custodianship with a fit person is an express item. The fitness packet and the binders-read govern what the determinations can say; the menu governs what may follow from them.
- **Negotiated contact terms are taught as mechanism, not as a quoted statute** — deliberately. Parties' agreed terms, presented to the court and entered in its order, are the ordinary way contact survives a custodianship; the game's accuracy doctrine required labeling that as practice built on the (f.1) outcome rather than inventing a citation for it. The contrast device is the agency's formulation — "reasonable contact, as the parties may agree" — which is also lawful, and is worth exactly the paper it is not printed on once the case closes.
- **The record work is 55 Pa. Code § 3130.44(d)** throughout: both sides' packets are built from the file the father read in June.
- The scenario does **not** depict the court as bound to grant custodianship; the contest route is fully heard and honestly arguable. What the route claims is comparative, and the guide stands on it: given this child's age and this record's two calendars, the entered-terms outcome protects more of what matters than the contest's expected outcomes do — including the contest's *victory* conditions, which arrive with the case open, the terms unset, and a four-year-old's household reorganized around an eight-month-old stability.

## (4) The traps

1. **Walking out of the mediation** when the threshold question is raised. No **contactTerms**; the consent-with-terms choice closes, and the contest — winnable in pride, losable in fact — ends at "Contested, and the Minimums": custodianship with judicial minimum contact and the negotiated terms existing only in a drawer.
2. **Consenting on the agency's eight words at the hearing.** Ends at "Custodianship, On Eight Words": same custodian, same child, same decency — and a contact right made of agreement, expiring with the first changed circumstance of the next decade.
3. **Arguing that the case should never have happened.** Ends at "The Record, Received and Not Relied On": contact at the custodian's discretion, awarded to the record's angriest presentation. The fitness packet exists in this ending too; it is noted as *received*, the verb orders use for paper they did not rely on.
4. **Keeping terms flexible and verbal at the negotiation.** What is not written by August is not signed in August. Flexibility is a virtue in families and a solvent in orders.

## (5) What no strategy controls

Sabine's fairness — a different aunt makes this a different story, and the guide says plainly that the route depended on her; the judge's own weighing of the two calendars, which a different bench could perform differently on the identical record; Pearl's future tellings of all of it, which no order can draft. The route controlled the record, the terms, and the ask. It did not control whether the ask was wise. That was Thaddeus's decision, made at full information with the binders open — and the scenario's respect for him is located exactly there.

---
*Verification: this route was walked programmatically against `scenario-94.json` — each named choice was followed from the start node in order; every intermediate node and choice exists; the flag-gated hearing choice's requirements (contactTerms, fitnessRecord) were satisfied by flags set earlier on the walk; the walk terminates at the ending node titled "Custody With His Name in the Order" after visiting 26 nodes, with $108 of the $140 starting cash remaining.*
