# STRATEGY GUIDE — Scenario 31: “The Confidential File”

*Game documentation for a fictional simulation in “The First 90 Days” (Tactic Watch). Everything below describes choices inside this scenario only. It is general information about how the scenario's route works — not legal advice for any real case.*

*Route verified programmatically against `scenario-31.json`: the walk from the start node, following the choices below, reaches the named ending (path check reported with the scenario's delivery notes).*

---

## (1) The win

**“Ending — The File, Whole, in Time.”**

Stated honestly: this is a records win, not a homecoming. Wren's adjudication still sustains the petition on another ground, and she remains placed at the end of this scenario. What the winning route changes is the basis the case proceeds on: the complete assessment — form, all 17 item ratings, outcome page — is produced *before* the adjudication it was needed for; the agency withdraws its “missed visit” claim when its own full note contradicts its summary; one item is re-scored on the record; and the judge's disposition order directs that the next review be built on the corrected, complete file. The win is that the case is decided from the file instead of from a summary of it. Nothing in this scenario offers more than that, and this guide won't pretend otherwise.

## (2) The route

1. **The Morning They Came** → ask what happens next and write it down. *Sets FLAG: `removed` (the removal happens in this scene; the 72-hour shelter-care clock starts). Every later door depends on treating paper as evidence from the first hour.*
2. **Seventy-Two Hours** → either choice (the shelter care hearing is day 3 — removal + 72 hours). *You get appointed counsel; the case's second clock (adjudication) is set.*
3. **Two Doors** → “Write the first request this week.” *Opens the administrative track before the court track — the order matters, because the court track stands on the administrative paper trail.*
4. **The First Request** → “Send the specific version — certified mail, and keep the receipt” (cash −6). *Sets FLAG: `recordsRequested` and FLAG: `specificRequest`; HIDDEN + the dated, item-naming request. The general version (“my whole file”) reaches the same next node but names nothing — and unnamed pages can later be neither produced nor ruled on.*
5. **The Receipt in the Folder** → “Start the log tonight.” *Sets FLAG: `logStarted`. The log is what later converts “I asked” into a provable record — the exact element whose absence weakened a real parent's Rule 1340 complaint in a published Pennsylvania appeal used as a source for this scenario.*
6. **The Redacted Stack** → “Build an index: two lists — pages you HAVE, pages the file itself says should exist.” *Sets FLAG: `indexBuilt`; HIDDEN + the “see attached” reference. This is the scenario's hinge: the index is what turns an absence into a named, numbered set of missing pages. (The phone-call and accept-the-stack choices at this node are traps 1 and 2 below.)*
7. **Two Columns** → write the second request from the index. *No new flag; the index becomes an exhibit-grade document the motion will later attach.*
8. **The Fuller Request** → “Mail it and log it the same day” (cash −6). *Sets FLAG: `secondRequest`; HIDDEN + the dated second request naming four missing items. The request asks the agency to produce each named item or state its ground — which is what produces the stated ground the court can later review.*
9. **The Partial Second Production** → “Ask Ms. Hart to take it to court — start the Rule 1340 track.” *The optional extra administrative letter (`admin_third`) converges to the same place at a cost of days on the adjudication clock; the direct choice keeps that clock comfortable.*
10. **Door Two** → “Make the good-faith attempt first.” *Skipping this step routes to the rushed-motion branch and closes this ending (trap 3).*
11. **The Good-Faith Letter** → “File the motion to compel — with the log and both requests attached.” *Sets FLAG: `goodFaithDone` and FLAG: `rule1340Filed`; HIDDEN + the filed motion with exhibits. The motion can now truthfully say the rule's required sentence: a good-faith effort was made and proved unsuccessful.*
12. **Filed, With Receipts** → “Prepare for the motion hearing” (cash −45, an unpaid morning). *The request itself is now inside the court's own record — it cannot later be misremembered by anyone, including the system.*
13. **The Motion Hearing** → wait the seven days. *The judge orders production of the form, ratings, and outcome page before the adjudication; the genuinely private redactions stand, each with its ground stated — the win was never “no redactions,” it is “no unexplained absences.”*
14. **The Whole File** → build the item-by-item page with counsel. *Sets FLAG: `fullProduction`; HIDDEN + the full assessment. Restraint is part of the move: most ratings are left alone; the two the paper contradicts are the argument.*
15. **The Adjudication, With the File** → tell Wren the truest available sentence. *Reaches the ending.*

Cash along the route: $180 → $123 (−6 certified request, −6 certified second request, −45 unpaid morning). All four endings stay open until **The Redacted Stack**; the full-production ending specifically closes if the good-faith step is skipped at **Door Two** or the motion record is thin.

## (3) Why this wins — the law as it is supposed to work

- **The release right.** Under 55 Pa. Code § 3130.44(d), information contained in case records “shall be released upon request” to parents and legal guardians. The route operationalizes it the way the regulation rewards: in writing, by name (the form, the item ratings, the outcome), dated, and provable.
- **The limit, honored, is what makes the rest winnable.** Section 3130.44(f) permits withholding material that violates another individual's privacy or is protected or made confidential by law. The route never argues against that limit — it accepts the stated redactions and attacks only the *unexplained absence*. That is why a judge can grant this motion without ruling that confidentiality doesn't matter.
- **Rule 1340's sequence is the strategy.** Pa.R.J.C.P. 1340(A) requires a good-faith informal effort before motion practice; Rule 1340(B)(1) then provides mandatory disclosure, on a party's request, of material items; Rule 1340(E) gives the court remedies including ordering production. The route is simply that sequence executed on paper, in order, with receipts.
- **The untested flag, kept.** The scenario states in-game — and this guide repeats — that no court has yet decided whether Rule 1340 reaches a scored assessment form. The winning route does not depend on pretending otherwise: it wins production on a record (specific requests, a log, an index, a stated ground) that gives the court every reason to order it, which is how untested questions are usually answered in practice — by being asked properly, in a case that is ready.
- **Clocks are the medium.** The 72-hour shelter care hearing (42 Pa.C.S. § 6332; 23 Pa.C.S. § 6315(d)) and the adjudication date frame everything: the route works because each mechanism is started while the next clock still has room in it.

## (4) The traps

1. **The phone call (at The Redacted Stack).** Asking about the missing pages by phone feels faster and produces exactly nothing a court can rule on — no date, no letter, no log line. It doesn't end the challenge (a late index can still be built), but it demotes the best reachable ending: the full file gives way to, at best, the one-page ending, because the request trail can no longer be proved to February's standard.
2. **Accepting the thick stack as the whole file (at The Redacted Stack).** Thickness is a property of envelopes, not records. This choice skips both requests' specificity and routes to the late-motion or thin-adjudication branches: production may still be ordered, but *after* the hearing it was needed for (the paper-win-after ending), or the hearing proceeds on the summary (the withheld ending).
3. **Skipping the good-faith step (at Door Two).** Filing the motion immediately feels decisive and hands the agency the cheapest argument in the rulebook: the rule's own first paragraph wasn't followed. The motion is denied on a thin record and a protective order issues on the stated ground — the withheld ending.
4. **The unlogged, uncertified late request (on the phone-call branch).** Ordinary mail, copy kept, no tracking: a real request whose existence can be celebrated but not proved. It yields exactly one produced page instead of the file — a real win, and a permanently smaller one.

## (5) What no strategy controls

The judge could have read the confidentiality ground more broadly and upheld the withholding even on this record; judges differ, and the ground was honestly arguable. The agency's response times, the solicitor's candor, the mailroom, and the hearing calendar are all outside the player's hands — a slower seven days or a denied continuance turns this route into the paper-win-after ending through no error of yours. Workers rotate, dockets slip, and luck holds real pieces of every outcome in this scenario. What the route controls is narrower: whether the court is asked, in writing, with proof, in the rule's own order, in time. In this scenario — as the debrief puts it — outcomes turn on workers, judges, and luck; the record of asking is the only part that was ever entirely the parent's.
