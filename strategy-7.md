# Strategy Guide — Scenario 7: “The School Note” (Foundation tier)

*Game documentation for a fictional simulation in* The First 90 Days. *It describes choices and outcomes inside this scenario only — general information, not legal advice for any real case.*

## The win

**Answered, With Proof** (`end_good`) — the best ending reachable in this scenario. It is a partial, honest win: The warning is resolved on the strength of an answer: written, documented, and early. The absences are coded for what they were — two medical mornings and a bus route the district moved — and the plan that replaced the warning was built with you, not handed to you.

## The route

- **The Record, Requested** (`records`) → choose: “File the written request for the attendance summary and referral note” — Sets recordsRequested. You answer the school’s actual numbers — uncoded, unexplained — instead of the letter’s summary of them.
- **Proof, Gathered Slowly** (`prep`) → choose: “Spend the evening assembling it: route notice, clinic slips, pharmacy printout” — Sets proofGathered. The seven absences become two documented stories — a moved bus stop and a pair of lungs.
- **Send It, or Say It** (`split`) → choose: “Send the written response — school and Ms. Ruiz — with the proof attached, before the deadline” — Sets responseSent, before the deadline at day 12. The answer lands in every file the question lived in.
- **Codes and Plans** (`p2`) → choose: “Agree to the plan, and ask for it in writing with your name spelled right” — Sets planInWriting: the plan is built with you and measurable fairly, instead of arriving pre-written at a home visit.
- **The Follow-Up Letter** (`p5`) → choose: “Sign the acknowledgment after reading it — and file the letter” — The final gate: reading it catches the record’s wording while it can still be questioned, and reaches the win.

Path check: this route was walked programmatically through the scenario's choice graph (start → start → n2 → records → prep → eve → split → p1 → p2 → p3 → p4 → p5 → end_good) and reaches `end_good`. Verified at generation time; the graph validation for this scenario reported no errors.

## Why this wins — the law as it is supposed to work

- 55 Pa. Code § 3130.44(d): your record — the attendance summary and the school's referral note as the agency holds them — is released on request. The route starts there: answer the numbers the file actually holds, not the numbers a warning letter summarizes.
- The deadline itself is the school's, stated in its letter, and no statute in this scenario makes it move. What the verified record right changes is the quality of the answer that meets it: documented mornings, coded correctly, filed in every building that received the warning.

## The traps

- **Send It, or Say It** (`split`) → “Wait and explain it properly, in person, at the home visit” — Costs the deadline. The file gains "no response received" before it ever gains your explanation, and the plan that follows is handed down instead of built. The win survives only through the late written response (u2) or the documented month (u4).
- **Codes and Plans** (`p2`) → “Agree warmly and skip the writing part” — Costs the plan’s paper form. You drop to the handed-down-plan track at u3: agreed, unwritten, and disputed-able.
- **The Follow-Up Letter** (`p5`) → “Sign it at the door for the mail carrier’s convenience” — Closes the win at the last inch: the follow-up letter records the warning as "resolved after escalation," and your unread signature accepts the wording.
- **A Clean Month, Documented** (`u4`) → “Do the month and trust the check-ins to speak for themselves” — Declines the last repair: the month happens, but check-in checkboxes — not your documentation — become the file’s last word.

## What no strategy controls

Ms. Ruiz read the proof fairly and offered a real repair door when the deadline was missed; a different worker reads the same packet as defiance, and a different school office loses the stamped copy. The bus company answers to no one in this story. No strategy controls the reader, the route schedule, or a small boy's lungs. It controls whether the file meets your documentation before it finishes meeting you.
