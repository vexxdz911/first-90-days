# Strategy Guide — Scenario 1: “The Thursday Gap”

*Game documentation for a fictional simulation. “In this scenario” means in the scenario’s data and debriefs. This is general information, not legal advice for any real case.*

## 1. The win

**“Ending — Home, With Paperwork.”**

This is the headline win: Eli and June stay home under a safety plan, the Thursday childcare gap is closed with documented coverage, and the first review narrows what remains open. It is not total closure—the plan continues, check-ins remain, and the file does not disappear—but no removal occurs.

## 2. The route

1. **The Argument, Then the Quiet** — Choose **“Text your sister Dana about the argument, so someone else knows it happened.”** This sets `sisterAware`; your support network exists on somebody else’s phone before the agency arrives.
2. **Someone at the Door** — Choose **“Ask what the report says, and whether you can have thirty minutes first.”** The visit is rated after a short delay rather than from the unprepared house.
3. **Thirty Minutes** — Choose **“Invite her to look wherever she needs to.”** The tidier rooms and the fact that you asked first both become part of the record.
4. **Questions, and a Form You Cannot See** — Choose **“Describe the patchwork honestly — including the Thursday gap.”** The hidden item names the gap in your words and beside your plan to fix it, instead of recording the plan as unclear.
5. **The Rest of the Questions** — Choose **“Tell her the argument was about custody — and that the report came the next day.”** The report’s context travels with the file.
6. **She Steps Outside to Call Her Supervisor** — Choose **“Call Dana. She can come tonight, and stay the week.”** This sets `supportEngaged` and opens the safety-plan branch instead of the removal branch.
7. **Paper Instead of Goodbye** — Choose **“Read every line before you sign.”** This sets `readPlan`; you learn about the check-in visit before it can surprise you.
8. **Closing the Thursday Gap** — Choose **“Swap Thursday shifts with a coworker — it costs you your weekend hours.”** Cash falls by $40, but the choice sets `thursdayCovered` and creates documented coverage with a name and schedule.
9. **The Flyer at the Library** — Choose **“Write the request tonight and send it in the morning.”** This sets `recordsRequested` and unlocks the assessment packet while there is still time to use it.
10. **Reading What Was Written About You** — Choose **“Bring the packet and your correction to the review.”** This sets `broughtCorrection`; the review sees the one-line neighbor entry answered with dates and a fuller account.
11. **The First Review** — Choose **“Ask what, exactly, remains open — and write it down.”** Vague continuing supervision becomes a finite written list, and the route reaches the win.

## 3. Why this wins — the law as it is supposed to work

- **The branch is supposed to turn on present safety and workable supervision, not on a parent’s worth.** Dana can be there tonight; a named schedule closes the specific Thursday gap. The strategy answers the worker’s stated problem with a person and proof.
- **Candor works when it creates a usable record.** Naming the gap yourself does not erase it. It prevents the form from saying the plan was “unclear” and pairs the problem with context and a remedy.
- **A safety plan is paper with consequences.** Reading it before signing turns an oral summary into terms you can satisfy and later prove you satisfied.
- **The record is supposed to be available to the person it describes.** Under **55 Pa. Code § 3130.44(d)**, the file material “shall be released upon request.” The request lets the parent see the scored items early enough to file a calm, dated correction.
- **The removal branch has its own safeguards if support cannot be assembled.** The scenario’s other path invokes counsel under **42 Pa.C.S. § 6337** and a shelter care hearing within 72 hours under **42 Pa.C.S. § 6332; 23 Pa.C.S. § 6315(d)**. The winning route avoids needing those safeguards; it does not make them unimportant.
- **A later indicated report would start another clock.** The scenario’s debrief identifies the written amendment/expungement request period as 90 days from notification under **23 Pa.C.S. § 6341(a)(2)**.

## 4. The traps

- **“There is no one who can come tonight”** at **She Steps Outside to Call Her Supervisor** is the hard branch trap. It closes the home-under-safety-plan ending and moves the story into removal, counsel, and a hearing. A return ending remains possible, but it is a different and harder win.
- **“Say childcare is ‘handled,’ and keep it short”** leaves the hidden item as “Supervision plan — unclear to the worker.” Short answers feel safer; on the form, uncertainty itself becomes evidence.
- **Keeping the custody argument private** removes the report-timing context from the file. The worker still has the report, but not your explanation of the dispute that preceded it.
- **Letting the record request go** leaves the same ending technically reachable, but surrenders the corrected-record version of the win: you attend the review without seeing the scored items or answering the compressed neighbor entry.

## 5. What no strategy controls

Dana has to be willing and able to drive over. A supervisor has to permit the Thursday swap. Mrs. Okafor has to confirm her part. A different worker or supervisor can weigh the same facts differently, and the scenario’s debrief says so directly: the same parent can land in a different ending in a different week. The strategy controls disclosure, documentation, and timing—not other people.

**Path check:** PASS. The JSON walk follows the 11 choices above from `start` to `end_home`, **“Ending — Home, With Paperwork.”** Final tracked cash: $140. Key flags set: `sisterAware`, `supportEngaged`, `readPlan`, `thursdayCovered`, `recordsRequested`, and `broughtCorrection`.
