# Strategy Guide — Scenario 129: "The Year in a Folder"

*Game documentation for a fictional simulation in "The First 90 Days" (Tactic Watch). The family, the case, and every choice below are fictional. This guide is general information about how the scenario is built — it is not legal advice for any real case.*

## (1) The win

**Best ending: "Ending — Home at Thirteen Months."**

This is a **full** win: Unai home at the thirteen-month review, on the agency's own recommendation, a full two months before the fifteen-month horizon. It is a capstone in Hard clothing — no single dramatic beat, just the library's paper disciplines (referral dates, gap letter, record request, early packet) sequenced across a year without a miss.

## (2) The route

Verified by walking the scenario graph from the start node (see the verification note at the end). Key decision points, in order — node title, winning choice, and what it changes:

1. **Month Zero** — *Start the folder today: plan, orders, every paper, in date order* Sets **folderKept**.
2. **Nine Boxes** — *Ask the caseworker, in writing, for each referral's date — promised, sent, started* Cash −$5; Sets **referralDates**.
3. **Reading the Plan Like a Contract** — *Start the monthly written check-in on the fog-boxes* Sets **fogTracked**.
4. **The First Visit Room** — *Sign in and out precisely, and keep your own visit log with dates and one line each* Sets **visitLog**.
5. **The Referral That Wasn't** — *Write the letter: plan date, referral date, cohort date — polite, dated, copied* Cash −$5; Sets **gapDocumented**.
6. **The Visit Room in Winter** — *Ask, and add your own line to your log: what he did, what you did, what was said* Sets **notesAsked**.
7. **The Record, Requested** — *Sign the written request; keep the stamped copy in the folder* Cash −$5; Sets **recordsRequested**.
8. **Reading the Book** — *File a short written response: the two gaps, with dates, and your attendance record, with dates* Cash −$5; Sets **responseFiled**.
9. **The Winter Review** — *Leave court determined: the response gets filed this week, not 'in due course'* Sets **responsePrompted**.
10. **The Housing Box** — *File both letters and ask the agency to note the July unit in the case plan itself* Cash −$5; Sets **housingLetter**.
11. **The January Cohort** — *Attend all eight, file the certificate the week it issues* Sets **courseDone**.
12. **The Program's Word** — *File it in February, with a copy to every party* Cash −$5; Sets **treatmentFiled**.
13. **Longer Tuesdays** — *Log every expanded visit, and write Mrs. Beltran a thank-you she can keep* Sets **expansionLogged**.
14. **Month Nine Review** — *Ask Mr. Olano to build the review packet with you: every letter, log, certificate, and the gap chronology* Sets **packetBuilt**.
15. **The Unit** — *File the lease-contingent letter and the housing worker's photos* Cash −$5; Sets **leaseFiled**.
16. **Mrs. Beltran's Letter** — *Thank her, copy the letter into your packet exactly as written* Sets **fosterLetter**.
17. **The Nine-Month Review** — *Treat the sentence as a specification: list everything the record still lacks* Sets **specListed**.
18. **The Packet, Assembled** — *File the packet two weeks early, with a one-page summary Mr. Olano drafts and you sign* Cash −$10; Sets **summaryFiled**.
19. **Overnights** — *Log the overnights and the first-week pediatrician visit, and file both* Sets **overnightsLogged**.
20. **Aftercare, In Writing** — *Get the aftercare plan signed and filed before the review* Sets **aftercareWritten**.
21. **The Audit** — *Chase the discharge summary in writing and file it the day it issues* Cash −$5; Sets **auditDone**.
22. **The Thirteen-Month Review** — *Ask for the order to say it plainly: return home today, aftercare in writing* This choice is flag-gated: it is only available with **recordsRequested** + **packetBuilt** + **gapDocumented**.

Supporting choices along the same walk — every "paper version" choice (dated, copied, filed), every written request, and every dated letter — add the documentation the packet is later assembled from. The full walked path is printed in the verification note.

## (3) Why this wins — the law as it is supposed to work

- **The horizon behind everything:** fifteen of the most recent twenty-two months in foster care triggers the agency's filing duty unless an exception is documented (42 U.S.C. § 675(5)(E); state review determination at 42 Pa.C.S. § 6351(f)(9)). Entry Monday, September 8, 2025 → the fifteen-month date is Tuesday, December 8, 2026. The route's design goal is to make the court reach *return* at month thirteen so the exceptions never have to carry the case.
- **Referral dates are the services exception in embryo.** The plan's boxes depend on referrals the agency must send; asking for promised/sent/started dates in writing converts a passive-voice delay into dated facts — the same facts that, unclosed, become the § 675(5)(E) services-not-provided exception, and, closed, become the packet's proof the plan worked.
- **The mirror:** the case record on request (55 Pa. Code § 3130.44(d)); redactions under (f). The record found the second gap — a housing referral never sent — that no meeting had ever mentioned.
- **Counsel (42 Pa.C.S. § 6337)** frames the year from month zero: the court can only act on what is in the record, and the record is partly the parent's to write.

## (4) The traps

1. **Trusting the plan's thirty-day service timeline at "Nine Boxes"** — the referral gap lives in the passive voice until the review reads 'unchecked' as 'unengaged.'
2. **Raising the gap verbally at a team meeting instead of by dated letter** — minuted as 'discussed concerns'; the gated win needs **gapDocumented**, and concerns are not a flag.
3. **Skipping the record request to avoid seeming adversarial** — the never-sent housing referral stays invisible; the packet cannot answer a gap it has never seen — the win's gate (**recordsRequested**) stays shut.
4. **Handing the packet up at the hearing instead of filing it early** — paper delivered on the deadline is treated as a speech; the route settles for **The Trial Period**, home but unclosed.

## (5) What no strategy controls

Waitlists, cohort start dates, housing stock, a caseworker's relief at being documented, and the judge's appetite for a clean record. The route controls only the year's paper form — and the scenario is built so that, this once, the paper form is the case.

---
*Verification: this route was walked programmatically against `scenario-129.json` — each named choice was followed from the start node in order; every flag-gated choice's requirements were satisfied by flags set earlier on the walk; the walk terminates at the ending node titled "Ending — Home at Thirteen Months" after visiting 24 nodes, with $100 of the $150 starting cash remaining. Walked path: Month Zero → Nine Boxes → Reading the Plan Like a Contract → The First Visit Room → The Referral That Wasn't → The Visit Room in Winter → The Record, Requested → Reading the Book → The Winter Review → The Housing Box → The January Cohort → The Program's Word → Longer Tuesdays → Month Nine Review → The Unit → Mrs. Beltran's Letter → The Nine-Month Review → The Packet, Assembled → Overnights → Aftercare, In Writing → The Audit → The Night Before Month Thirteen → The Thirteen-Month Review → Ending — Home at Thirteen Months.*
