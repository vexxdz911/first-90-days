# STRATEGY GUIDE — Scenario 35: “The Hearing That Wasn't”

*Game documentation for a fictional simulation in “The First 90 Days.” The family in this scenario is a composite; nothing here describes a real case. This guide is general information about how the scenario is built — it is not legal advice for any real case. The route below was verified by walking the finished choice graph (`scenario-35.json`) node by node.*

---

## 1. The win

**“Ending — Heard, with the Delay in the Record.”**

State it honestly: this is not a reunification ending, and it does not undo a single day of delay. Owen's case slid for fifteen months, and in this ending it still slid. What the win consists of is narrower and, inside this scenario's logic, decisive: the hearing is finally held on a record that contains the case's true age — the chronology you kept and filed, the readiness you proved before every date, and the judge stating on the record that the passage of time, including the time attributable to continuances, was considered and weighed. Delay happened in the open, where a court had to reckon with it, instead of evaporating into separate, reasonable docket entries. That is the best reachable outcome in this scenario, and it is a record outcome, not a rescue.

## 2. The route

Walked and verified in the graph: `start → wall → counsel → records → records_arrive → prep1 → kitchen_table → hearing1 → cont1 → visits1 → service1 → letter_eli → prep2 → hearing2 → after2 → visits2 → payday → prep3 → hearing3 → strain → notice4 → folder_night → prep4 → hearing4_slide → asfa_shadow → final_prep → hearing_final_record → end_held_record` (cash 240 → 170).

The decision points that carry the route, in order:

1. **Your Own File, Again** (`records`) — *Choose: write the request for the full record, including the complete assessment.* Sets `recordsRequested`; hidden item records the written request. This is what lets every later page be built from the file instead of from memory, and it keeps all four endings open while strengthening the two record endings.
2. **The One-Page Readiness Statement** (`prep1`) — *Choose: file it, with certificates and the sign-in sheet attached* (cash −15). Sets `readinessFiled`. Readiness stops being a mood and becomes a dated fact the file must reckon with at every later slide.
3. **The First Slide** (`hearing1`) — *Choose: write the continuance in the chronology in the hallway, before the elevator comes.* Sets `recordAsked`; the hidden item captures continuance #1 with its reason (witness unavailable, report not filed) and your readiness attached to it. Delay enters your record at full size, the day it happens.
4. **Mail from the Foster Home** (`letter_eli`) — *Choose: file readiness statement number two, updated, with the certificate* (cash −15). One filed statement is an event; two are a pattern, and patterns are what files believe.
5. **The Second Slide** (`hearing2`) — *Choose: file a short written objection before the next date.* Sets `objectionFiled`. Note what this is in the scenario's own terms: not a rule, not a threat — a dated page saying you were ready and the case moved anyway.
6. **The Third Slide** (`hearing3`) — *Choose: submit the updated chronology to the court file before you leave the building.* Sets `chronologyFiled`. This is the route's hinge inside the courthouse: the case's true age is now in *their* file, not only in your folder.
7. **The Folder by the Door** (`folder_night`) — *Choose: file the objection and the fourth readiness statement together* (cash −15). Sets `readinessFiled` and `chronologyFiled` again, at the moment a June continuance is on the table. Skipping this filing is how the quiet-file ending gets its quiet.
8. **May 15, Decided in Advance** (`prep4`) — *Choose: the branch where the judge grants the June date* (“The judge grants the June date — and the fight moves to what the record says before June 10”). This looks like losing. In this graph it is the only road to the win, because it sets up the decision that matters more:
9. **The Conversation Changes** (`asfa_shadow`) — *Choose: file the full chronology packet — chronology, four statements, certificates — before June 10.* Sets `chronologyFiled` and puts the whole record in the room ahead of the fifteen-month date instead of behind it. From here the route runs `final_prep → hearing_final_record → end_held_record`: the hearing is held with the judge's questions starting in March 2025, not in June.

## 3. Why this wins — the law as it is supposed to work

This scenario teaches **practice and one clock**, and the guide says so plainly: there is no continuance rule in this scenario — no invented deadline, limit, or standard — because none was verified for it. The readiness statement, the spoken request that the reason and the new date be stated on the record, and the filed chronology are things a parent *can do*, not entitlements a court *must honor*.

The hard law the route operationalizes is the clock the delay ran against, plus the record rights:

- **The 15-of-22 clock.** When a child has been in foster care for 15 of the most recent 22 months, a petition to terminate parental rights is generally to be filed unless an exception fits: the child is being cared for by a relative; there is a documented compelling reason that filing would not serve the child's best interests; or the agency did not provide the services it identified as necessary for safe return (42 U.S.C. § 675(5)(E)). In this scenario the date is computed, not approximated: placement March 10, 2025 → **June 10, 2026**. The statute does not pause when hearings continue; the route works because it treats June 10 as the real deadline and files *before* it.
- **Your record, on request.** Your case record “shall be released upon request” (55 Pa. Code § 3130.44(d)) — the route's first decision, and the source of everything the later filings are built from, including the full assessment.
- **Counsel.** Parents in dependency cases have the right to counsel (42 Pa.C.S. § 6337); the route's practice is built with counsel, in plain words, at every slide.
- **The burden in dependency** is clear and convincing evidence — the standard the eventual hearing is finally held under, on a record that now includes the delay itself.
- **The assessment flag.** Where assessment material is invoked through adjudication-phase disclosure (Pa.R.J.C.P. Rule 1340(B)(1)), the scenario carries its standing caution: this assessment approach is untested, so its ratings are claims to be answered, not findings to be obeyed.

## 4. The traps

Each trap below was checked against the graph: from the trap's subtree, the win is no longer reachable.

1. **Winning the May 15 argument** (`prep4` → “The judge takes up the parent's filed position before she rules” → `hearing4_obj`). It feels like the climax — a continuance opposed and denied as requested, a hearing pulled back to May 29. It is a genuinely good ending, and it is capped: from `hearing4_obj` only **“Ending — One Objection Held”** is reachable. The partial ending is honest, but it is not the win: one objection held, three slides standing, and the fuller hearing still ahead.
2. **Bringing the folder to June 17 instead of filing it** (`asfa_shadow` → “Bring the folder to June 17 instead”). The folder stays complete, accurate — and unfiled through the one date it mattered most. That road runs through `hearing_final_plain` to **“Ending — Heard, on a Quiet File”** only: a fair hearing on a record that barely shows the waiting.
3. **Drifting past the date** (`hearing4_slide` → “Ask Ms. Okafor what June 10 changes, exactly…” → `asfa_day`). Information instead of filing, in the last weeks when filing was still possible. From `asfa_day` only **“Ending — The Date Arrived First”** is reachable: the goal conversation changes around you, and you argue uphill from then on.
4. **Skipping the record request** (`records` → “Skip it”). This one doesn't lock a door in the graph — the route can still be walked blind — but it forfeits the assessment itself, which is what the readiness pattern and the chronology are ultimately measured against. You can be visibly ready and still never see the thing the other side is ready *with*.

## 5. What no strategy controls

A different judge could read the same five filed pages and continue the case anyway; the scenario says so in its own debrief, and it is true inside the fiction and outside it. Dockets double-book, witnesses have emergencies, counsel have conflicts — the slides in this scenario are not villainy, and no filing prevents them. What the route controls is visibility and sequence: that the delay is written down where decisions are made, and that your paper arrives before the clock's date rather than after it. Outcomes in these cases turn on workers, judges, courtrooms, and luck alongside anything a parent files. The strategy's whole claim is the narrow one the debrief makes: in a system that decides from files, a true story that is filed competes better than a true story that is only lived.
