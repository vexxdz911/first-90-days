# STRATEGY — Scenario 21: “The Relapse Report”

*Game documentation for a fictional simulation. This page describes how the scenario's choice graph works, in this scenario. It is general information about a game, not legal advice, and it is not a guide for any real case.*

*Route verified by walking `scenario-21.json` programmatically: every choice named below exists on its node, every edge named below exists in the data, and the path reaches the ending named in §1 with no `removed` flag set anywhere on it.*

**Verified path (node IDs, in order):** `start → first_calls → kin_call → caseworker_strong → voluntary → assessment_day → lab_questions → records_request → supervision_plan → wed_visit → followup_week → december_review → end_home`
**Cash along this route:** $170 start − $14 (assessment day) − $6 (record-request copies) − $14 (follow-up week) = **$136 at the ending.**

---

## 1. The win

The best ending in the data is **“Ending — Home, Under a Documented Plan”** (node `end_home`).

Be honest about what it is: it is a **partial win, and the scenario says so in its own debrief.** The child remains home and the expanded trial-home time continues — but under a documented safety and treatment plan: a signed voluntary kin safety arrangement for the crisis nights, a stepped-up treatment plan, scheduled follow-up screens, a written supervision plan with confirmed kin cover, and the review structure still standing around the family. The reported positive screen is **not** erased, cleared, or argued away; it stays in the record. What changed is that it no longer travels alone. A player who reads this ending as “the result didn't matter” has misread it — the result is the reason every document in the folder exists.

## 2. The route

Key decision points in order, by node title, with the winning choice at each and what it changes:

1. **“The Monday Call” (`start`)** — *Call your treatment program first, then Rae.* Changes: treatment hears about the result from the parent the same morning (hidden item recorded); the Tuesday assessment exists from this choice onward; no flag, no cash.
2. **“Two Calls, Made” (`first_calls`)** — *Call Lou now, while Rae is still on the line.* Changes: kin support becomes a named, reachable person instead of a description; this is what makes a voluntary safety arrangement possible at all.
3. **“Lou Answers” (`kin_call`)** — *Tell the caseworker exactly what is arranged, with names and times.* Changes: a confirmable safety answer enters the agency's notes (hidden item: sister confirmed for overnights and school pickup); the vague alternative routes to the unprepared-visit branch instead.
4. **“A Plan She Can Repeat” (`caseworker_strong`)** — *Agree, and ask for the whole arrangement in writing tonight.* Changes: the voluntary kin safety arrangement is agreed on day one, in writing, before any court filing (hidden item) — and the removal branch is never entered, so the `removed` flag is never set and both removal endings stay closed in the player's favour.
5. **“Signed at Lou's Table” (`voluntary`)** — *Sleep at home, set two alarms, go to the assessment early.* (Only choice on this node.) Changes: converts Monday's paper into Tuesday's attendance; the 48-hour window's second day is spent inside the plan rather than renegotiating it.
6. **“Tuesday, Nine O'Clock” (`assessment_day`)** — *Ask the process questions now, and write the answers down.* Changes: cash −$14; the assessment and the accepted stepped-up plan are documented (hidden item), and the parent learns where the screen report itself lives — in the case record — which sets up the next node.
7. **“Questions About a Page” (`lab_questions`)** — *Go home and build Wednesday's folder.* (Only choice.) Changes: the process questions are noted by the provider; nothing is promised about the result, and no right is invented — the value is purely that the questions exist in the treatment record.
8. **“Wednesday Morning, in Writing” (`records_request`)** — *Send the written request today, keep the stamped copy, text the caseworker that it is sent.* Changes: cash −$6; sets **`recordsRequested`**; the screen report and related case notes are requested as case-record material (hidden item), so counsel and the court can later read from the same page as the agency.
9. **“The Plan, With Names On It” (`supervision_plan`)** — *Write it with names, nights, and a backup for the backup, and have Lou confirm it by text today.* Changes: the supervision plan becomes confirmable by a second person (hidden item); the “family support as needed” alternative reaches the same next node but leaves the plan unverifiable.
10. **“Wednesday, Both Houses” (`wed_visit`)** — *Ask what the program needs this week, and put the follow-up screen on the calendar.* (Only choice.) Changes: the 48-hour window closes with the trial-home arrangement continuing; the record, not the window, is what carries forward.
11. **“The Follow-Up Screen” (`followup_week`)** — *Keep the folder current and take it to counsel before December.* Changes: cash −$14; follow-up attendance is documented (hidden item), so December is argued from a habit of paper rather than a night-before assembly.
12. **“The December Review” (`december_review`)** — *Listen for the order with the folder in counsel's hands.* (Only choice.) Changes: reaches `end_home` — the ending in §1.

## 3. Why this wins — the law as it is supposed to work

Only principles this scenario actually uses, stated only as far as they were verified:

- **Records on request — 55 Pa. Code § 3130.44(d).** In this scenario, a party to the case may ask for the case record, and the regulation provides that it “shall be released upon request.” The winning route uses this once, in writing, inside the 48-hour window, to seek the screen report and the related case notes as case-record material. That is all the scenario claims. It does **not** claim a right to a retest, a right to have a result withdrawn or redone, or any particular lab standard — the provider/lab questions on the route are questions, documented as asked, and nothing more.
- **Counsel — 42 Pa.C.S. § 6337.** The route uses counsel on the court path: counsel is in possession of the folder at the December review because the record was requested and shared in November. The scenario does not treat counsel as a formality; counsel's function on the winning route is to argue from the whole record rather than from the result alone.
- **Shelter care timing — not used by this route, by design.** The 72-hour shelter care rule (42 Pa.C.S. § 6332; 23 Pa.C.S. § 6315(d)) governs the removal branch of this scenario — a child taken into custody on Monday, November 2 would have a shelter care hearing on Thursday, November 5, 2026 — and the second ending is built on it. The winning route never enters that branch: no removal occurs, so no shelter care hearing is triggered. Winning, here, partly means a deadline never starts.
- **No automatic consequences.** Nothing in this scenario asserts that a reported screen result automatically produces a removal, a filing, or any other legal consequence — criminal, probationary, or otherwise. In the graph, outcomes turn on the immediate safety answer and on what the record contains when a decision-maker reads it, which is the distinction the scenario exists to teach: a screen result is a reported line about one sample; follow-up documentation is the checkable account of what happened next; the court's record is what a judge can actually act on.

## 4. The traps

Tempting choices that close the win — all of them inside the first 48 hours:

1. **At “Five O'Clock, Unprepared” (`visit_unprepared`): refusing any plan and telling the caseworker to write what she wants.** This is the single choice in the scenario that sets the **`removed`** flag and enters the emergency-removal branch that same night. Programmatic check: no path carrying `removed` ever reaches `end_home`. The home ending is gone in one sentence, and the best outcome left is return at shelter care.
2. **At “A Plan She Can Repeat” (`caseworker_strong`): asking for the night to think the voluntary arrangement over.** It feels like caution; in the graph it routes straight to `visit_unprepared`, where the only remaining exits are a speakerphone rescue in front of the caseworker or removal. Signing later is not an option the day offers — the arrangement's value is that it exists *tonight*.
3. **On the removal branch, at “Counsel, and a List” (`counsel_call`) choosing to spend the day demanding the screen be done again, then at “A Day Spent on the Result” (`dispute_only`) calling the lab once more on Wednesday.** Each step routes away from the documentation list, and the second routes to `wed_thin` — no assessment, no record request — which closes the shelter-care return ending and lands in the continues-past-review ending. The graph is blunt about the mechanism: phone calls are not the mechanism by which results fall, and the hours spent on them are the same hours the list needed.
4. **At “Wednesday: The Request and the Plan” (`removal_records`): sending the record request but leaving the supervision plan verbal.** The request half is done properly (`recordsRequested` is set either way). The cost is the other half: an unconfirmed plan routes to `shelter_partial`, where the court credits the treatment record, finds the one gap it cannot fill from a description, and continues placement. The win at shelter care is lost not on the screen, but on the missing signature.

## 5. What no strategy controls

The route above controls one thing: the next 48 hours on paper. It does not control whether Lou's phone is answered on a given Monday, whether a caseworker builds with what she is handed or reaches for the shorter list of options, what a treatment provider writes in an assessment note, or how a particular judge weighs a confirmed plan against a reported result on a particular morning. The published record this scenario is composited from contains families who did much of this and lost time anyway, and families whose outcomes turned on a worker, a relative, or a calendar no one chose. In this scenario the documented route makes the best ending *reachable and supported* — it does not make it owed. Workers, judges, and luck hold the rest, and any strategy page that says otherwise is selling something the game itself refuses to claim.
