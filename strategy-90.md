# Strategy Guide — Scenario 90: "The Remand"

*Game documentation for a fictional simulation in "The First 90 Days" (Tactic Watch). The family, the case, and every choice below are fictional. This guide is general information about how the scenario is built — it is not legal advice for any real case.*

## (1) The win

**Best ending: "Home on Remand, With Conditions and a Calendar."**

State it honestly: a partial win in form and a full one in fact. Piotr comes home at the remand disposition — but under 42 Pa.C.S. § 6351(a)(1) conditions and agency supervision, with the case open and a review in ninety days. The guide labels it partial because the system's file on this family remains open. Note what the appeal alone bought: nothing but the hearing. Everything that filled the hearing — the letters, the packet, the plan, the snow-day log — was built in the five weeks after the victory, and it, not the victory, is what the findings stand on.

## (2) The route

Verified by walking the scenario graph from the start node (see the verification note at the end). Key decision points, in order:

1. **The Route Manager** — *Ask him, in person, to sign the schedule letter.* Sets **scheduleLetter**. The first hearing knew Bogdan's schedule as an adjective; the remand knows it as a document.
2. **The Record, Again — On Purpose** — *Order the transcripts and request the complete agency record, in writing.* Cash −20. Sets **recordsRequested** (55 Pa. Code § 3130.44(d)). Post-victory paper discipline is the scenario's first test, and it is graded by the agency's recommendation being written from the same file at the same time.
3. **The Uncle in Pittsburgh** — *Ask him to start the kinship assessment now.* Sets **kinAssessed**; the § 6351(a)(2)(i) option becomes real, which disciplines the whole hearing — a court with a genuine second option makes better findings about the first.
4. **The Bus Pass** — *Buy the pass and protect the weekends.* Cash −8. The vacated order reopened one question; the visits never stopped being evidence.
5. **The School Counselor's Letter** — *Ask her, in writing, for the signed letter.* Sets **schoolLetter**.
6. **Eight Months of Paper** — *Assemble the progress exhibits into a single filed packet.* Cash −10. Sets **progressRecord** — one of the two flags the winning hearing choice requires.
7. **A Weekend Visit, Weighed** — the written log note (**visitLog**).
8. **The Kitchen Table, Honestly** — *Write the home plan down, hour by hour, with names.* Sets **homePlan** — the second required flag, and the scenario's highest-leverage single document (see §3).
9. **The Agency's New Position** — *Hand over the home plan and the exhibit packet for the file, today.* Sets **packetFiled**; the agency's recommendation is written about documents.
10. **The Letter From Piotr** — *File Piotr's letter, through counsel, unedited* (**childLetter**), and the **Snow Day** log copy (**snowLog**) — the plan, stress-tested by weather, on paper. You finish with $112 of the $150 start.
11. **The Remand Hearing** — *Present the progress packet and the written home plan, and ask for return under § 6351(a)(1) with conditions.* Flag-gated on **progressRecord** + **homePlan**. It leads to findings dictated aloud, and home.

## (3) Why this wins — the law as it is supposed to work

Only principles from the scenario's verified set are stated here:

- **A remand re-runs disposition under 42 Pa.C.S. § 6351.** The court must enter findings on the record before a removing disposition (§ 6351(b)) — contrary-to-welfare and reasonable efforts — and it chooses from the disposition menu: § 6351(a)(1), remain or return with the parent under conditions and supervision; § 6351(a)(2)(i), temporary legal custody to a qualified individual, including a relative. The panel's vacatur guaranteed the *findings*; it guaranteed nothing about what they would find.
- **Findings stand on exhibits, so the route is an exhibit-building exercise.** Progress, schedule, school, visits — each is a document with a provenance. The home plan is the route's center because it is the only exhibit about the future: findings about whether a child can be home are findings about Tuesdays, and Tuesdays must be proven with names and hours.
- **The record work is 55 Pa. Code § 3130.44(d)** — released upon request — used here against the remand's version of information asymmetry: the agency's recommendation is drafted from its file, and the parent who has read that file drafts alongside it.

## (4) The traps

1. **Keeping the home plan in your head at "The Kitchen Table, Honestly."** No **homePlan** — the return choice closes at the hearing. A plan described is a plan doubted; the findings that follow send Piotr to the uncle ("Custody to Family: The Bridge Holds") at best.
2. **Bringing the progress originals loose at "Eight Months of Paper"** and explaining as needed. No **progressRecord** — same closure, from the other side. Narration was the first hearing's strategy; the Superior Court has already published its review of it.
3. **Asking the court at the hearing to "simply restore matters as they were."** The one disposition the panel's opinion forecloses. Ends at "The Order, Rewritten Properly This Time" — a flawless procedure producing continued placement, and a specific deficiency list as the consolation.
4. **Keeping the uncle as a name to mention.** Unassessed kinship persuades no one; the bridge ending requires the assessment to exist, and choosing the bridge without it collapses toward continued placement instead.

## (5) What no strategy controls

The remand judge's weighing of a genuine plan against a thin margin at 5:30 a.m.; the agency's recommendation as first drafted; Route 30; a twelve-year-old's heart, which the letter governed better than any adult in the story. The route controlled what the findings could stand on. A record does not decide a hearing — it decides what the hearing is capable of deciding, and in this story that turned out to be the difference between an order rewritten and a son at home.

---
*Verification: this route was walked programmatically against `scenario-90.json` — each named choice was followed from the start node in order; every intermediate node and choice exists; the flag-gated hearing choice's requirements (progressRecord, homePlan) were satisfied by flags set earlier on the walk; the walk terminates at the ending node titled "Home on Remand, With Conditions and a Calendar" after visiting 20 nodes, with $112 of the $150 starting cash remaining.*
