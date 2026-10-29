# Strategy Guide — Scenario 92: "Heard, Not a Party"

*Game documentation for a fictional simulation in "The First 90 Days" (Tactic Watch). The family, the case, and every choice below are fictional. This guide is general information about how the scenario is built — it is not legal advice for any real case.*

## (1) The win

**Best ending: "Heard, and It Moved the Order."**

State it honestly: this is a **partial** win. Solana stays with her grandmother; the agency's transfer recommendation is declined on facts, with its two factual errors noted on the record; the mother's services get dates. Solana is not "home" in the law's final sense — her mother's case continues, reviews continue, and a better-prepared recommendation can return in six months. What was won is the present, documented and ordered, plus a record that makes the next recommendation harder to write carelessly. The scenario's claim is about the statute itself: § 6336.1's opportunity to be heard is a small right, and this route loads it to its full rated capacity.

## (2) The route

Verified by walking the scenario graph from the start node (see the verification note at the end). Key decision points, in order:

1. **What "Opportunity to Be Heard" Means** — the clinic defines the right's exact shape before anything is built on it: notice and an opportunity to be heard under § 6336.1; **not** party standing (which runs through custody under § 6357, which Philomena does not hold and never claims).
2. **Calling Solana's Mother** — *Ask her to sign the written request for the complete record this week.* Sets **recordsRequested** (55 Pa. Code § 3130.44(d)). The regulation's right belongs to the case's subjects; the grandmother's contribution is asking, in time, as Scenario 4's grandmother did. The file this produces contains the agency's draft recommendation — the document the whole defense is built against.
3. **The School File** — the counselor's letter with attendance figures (**schoolPacket**) — one of the two flags the winning hearing choice requires.
4. **The Neighbor With the Spare Key** (**neighborStatement**), **The Pediatrician's Summary** (cash −10, **medPacket**), **The Letter From the Parish Hall** (**thursdayLog**) — the stability packet: a child's daily life, documented by the professionals and neighbors who witness it, in formats a court can cite. You finish with $100 of the $110 start.
5. **Two Pages, In Her Own Words** — *Write the two pages, dated and specific, and practice reading them in under five minutes.* Sets **statementWritten** — the second required flag.
6. **Sunday at Philomena's Table** — the Sunday log brought current (**visitLog**): the mother's progress (§ 6351(f)(3)) documented by the only person present at every visit.
7. **The Worker's Visit** — *Ask for the recommendation in writing.* Sets **recInWriting**. The scenario's highest-leverage single move (see §3): the doorway remark becomes two checkable factual claims, both wrong.
8. **Called to the Front** — *Read the statement and hand up the packet.* Flag-gated on **statementWritten** + **schoolPacket**. The judge's questions to the agency do the rest.

## (3) Why this wins — the law as it is supposed to work

Only principles from the scenario's verified set are stated here:

- **42 Pa.C.S. § 6336.1 (Act 48 of 2023)** entitles foster parents, resource caregivers, and prospective adoptive resources — including kinship resources within § 6302's definition — to notice of permanency hearings and an opportunity to be heard. It does not make the caregiver a party: no motions, no cross-examination, no standing to request relief, which the statute reserves to parties (and which § 6357's custody route would separately supply). The scenario teaches the right at its actual size in both directions: the clinic states the limits in the same scene that states the power.
- **What the hearing does with a voice is § 6351(f)'s determinations** — made from what is presented, at hearings recurring within six months (§ 6351(e)(3)(i)). A prepared statement with exhibits gives determinations something to cite; that is the entire mechanism by which five minutes moves an order.
- **The § 3130.44(d) record request is exercised by the mother**, at the grandmother's asking — a limit the scenario respects rather than wishes away, and the reason the route's second step is a phone call, not a signature.

## (4) The traps

1. **Speaking from the heart at "Called to the Front,"** without the packet. Ends at ""For the Present": The Win That Isn't Finished" — Solana stays, provisionally, with the recommendation alive and its errors uncorrected. A judge can thank a memory; a judge can only cite paper.
2. **Staying home at "The Night Before"** because a courtroom is no place for a grandmother. Ends at "The Room She Wasn't In": the transfer ordered on the agency's uncorrected paper. § 6336.1's right exists only on the day it is used.
3. **Letting Daniela "handle her own case her own way" at the phone call.** No **recordsRequested** — the recommendation is never read in advance, its errors never identified, and the statement is written against a fear instead of a document.
4. **Accepting the doorway explanation at "The Worker's Visit."** Doorway explanations are remembered by nobody and answered by nothing; the written version is what the hearing could be won against.

## (5) What no strategy controls

The judge's receptivity to a caregiver's exhibits; the agency's choice to return in six months with a corrected recommendation; Daniela's road, which no grandmother's packet can walk for her. The route controlled preparation, paper, and presence — which is to say, the entire content of the right § 6336.1 actually grants. The scenario's respect for the statute is that it never pretends the right is bigger. Its argument is that the right, at its true size, properly loaded, carried a child.

---
*Verification: this route was walked programmatically against `scenario-92.json` — each named choice was followed from the start node in order; every intermediate node and choice exists; the flag-gated hearing choice's requirements (statementWritten, schoolPacket) were satisfied by flags set earlier on the walk; the walk terminates at the ending node titled "Heard, and It Moved the Order" after visiting 21 nodes, with $100 of the $110 starting cash remaining.*
