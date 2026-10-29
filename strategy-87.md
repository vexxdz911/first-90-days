# Strategy Guide — Scenario 87: "The Second Letter"

*Game documentation for a fictional simulation in "The First 90 Days" (Tactic Watch). The family, the case, and every choice below are fictional. This guide is general information about how the scenario is built — it is not legal advice for any real case.*

## (1) The win

**Best ending: "A New Hearing, On the Whole Record."**

State it honestly: this is a **partial** win, and it is the best this scenario offers. The Secretary grants reconsideration and orders a new expunction hearing on the complete record. The indicated report is **not** expunged by this ending — it stands while the new hearing pends, and the hearing officer could rule either way on the full file. What was won is the decision being *re-decided about everything*, because the first one was made without a material page the agency itself had gathered.

## (2) The route

Verified by walking the scenario graph from the start node (see the verification note at the end). Key decision points, in order:

1. **The Letter With Two Clocks** — *Read the last page again and write down the two dates.* Sets **datesKept**. The order's own last page states the windows; everything in the scenario is downstream of reading it.
2. **What Arrived Late** — *Take the packet and the letter to the legal aid clinic this week.* Sets **evidenceFound**; the hidden file notes the late-arriving pediatric follow-up letter that the Bureau never addressed.
3. **The Clinic's Two Pages** — *Sign the reconsideration request with the letter attached, and the written request for the complete file.* Cash −10 (you finish with $115 of the $140 start). Sets **reconDrafted** and **recordsRequested** — the § 3130.44(d) request, made before anyone knew whether it would matter. (The detour through "Seven Days Later" reaches the same signatures on day twelve, at the cost of every margin in the story.)
4. **The Director's Office** — *Tell her the truth with dates.* Sets **directorTold**; the employment conversation runs on filed paper instead of rumor.
5. **The Shift Board** — *Ask for the swap in writing and take the Saturday.* Cash −15. Filing day stops depending on a lunch break.
6. **Day Twelve of Fifteen** — *File the reconsideration request, with the pediatrician's letter attached.* This choice is flag-gated on **reconDrafted**: an undrafted reconsideration cannot be filed, only intended.
7. The receipt, the waiting weeks, the Secretary's answer, and the new-hearing preparation follow from the filing. The complete file — requested in writing at step 3 — is what the new hearing is prepared from.

## (3) Why this wins — the law as it is supposed to work

Only principles from the scenario's verified set are stated here:

- **The two windows are 23 Pa.C.S. § 6341(g)'s, and they run from the mailing date.** Within 15 calendar days of the mailing date of the Bureau's final order, a party may request reconsideration by the Secretary or appeal; within 30 calendar days of the mailing date, an appeal to Commonwealth Court must be perfected. The clinic's warning is the rule's practical corollary: requesting reconsideration does not stop the court clock.
- **The page existed to be used because of § 6341(c.2)(4):** the agency must provide a person making an appeal with the investigation evidence, including potentially exculpatory evidence. The reconsideration's spine is narrow and record-shaped — material evidence, in the agency's own packet, that the final order never addressed.
- **The complete file for the new hearing rests on 55 Pa. Code § 3130.44(d):** agency records are released upon request. Step 3 is that right, exercised in writing, early.

## (4) The traps

1. **Filing only the Commonwealth Court appeal at "Day Twelve of Fifteen"** because it feels like the bigger door. Cost: the whole scenario. The court reviews the record that exists; the unconsidered letter is not in it. That route ends at "The Court Reads a Smaller Record" — the report standing, unreconsidered, while the stronger argument waits in a folder.
2. **Leaving the packet in the drawer at "What Arrived Late."** No **evidenceFound**, and the clinic builds a reconsideration with no spine — a request to "look again" instead of a demonstration that something was never looked at.
3. **Coming back next week at "The Clinic's Two Pages."** Survivable in this scenario — day twelve still files — but it spends the director conversation, the shift swap, and every spare day, and it converts a calm filing into a perfect one-or-nothing errand. The guide walks the clean route; the detour exists to show what delay actually costs: not the outcome, this time, but all of the slack.

## (5) What no strategy controls

The Secretary could have denied reconsideration outright; hearing officers weigh follow-up letters as they find them; the preschool's clearance cycle runs on its own calendar regardless of any parent's paper. The route controlled the dates, the filing, the attached page, and the complete-file request. Outcomes in this system also turn on officials, employers, and luck — the strategy's claim is only that every lever the parent actually held was pulled inside its window.

---
*Verification: this route was walked programmatically against `scenario-87.json` — each named choice was followed from the start node in order; every intermediate node and choice exists; the flag-gated filing choice's requirement (reconDrafted) was satisfied by flags set earlier on the walk; the walk terminates at the ending node titled "A New Hearing, On the Whole Record" after visiting 13 nodes, with $115 of the $140 starting cash remaining.*
