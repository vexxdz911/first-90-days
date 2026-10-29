# The Spare Room (a fictional composite) — Node-for-Node Script (Scenario 48)

Scenario 48 of *The First 90 Days* — script generated node-for-node from `scenario-48.json`; the JSON is the source of truth.

A fictional composite built from published Pennsylvania dependency practice and documented system patterns. Not a real family's case.

**Content note:** child removal, court hearings, family separation.

**How to read effects:** `cash` is money spent or received at that choice; `FLAG:` marks a fact the story remembers; `HIDDEN +` is an assessment item the player never sees scored; `REQUIRES:` gates a choice on an earlier fact; `NOTE:` is authorial, not spoken in-world. Endings are marked **Ending.** with a **Debrief:**.

**Start date:** Monday, April 6, 2026. **Tier:** Foundation. **Start cash:** $120.

---

## [start] Your father's kitchen

*Day 0 — Monday, April 6, 2026*

Your father Walter keeps a list on his refrigerator of everything his cardiologist has ever told him, in chronological order, and he follows it the way he followed a bus route for thirty-one years: exactly. He pours coffee and says the thing he has clearly rehearsed.

"The spare room is Hugo's. It was always going to be Hugo's, since before any of this. You finish your program. The boy sleeps under my roof. Tell them." You are two weeks into the program that is the center of your case, and Hugo is two weeks into a foster home across town with a kind family, the Delacroix family.

**Choices:**
- "I will, Pop. In writing — so it lands in the file, not just in a phone call." → **tell_in_writing**  _(FLAG: kinNamedWritten; HIDDEN + named-kin)_
- "I will, Pop." You will tell Hugo's worker, Mr. Solberg, when you see him Thursday. → **tell_thursday**

## [tell_thursday] Thursday, in passing

*Day 3 — Thursday, April 9, 2026*

You tell Mr. Solberg in the hallway after your visit with Hugo, while he is balancing a coffee and a laptop bag, and he says "That's great, I'll note it" the way people do in hallways. A week later, at your program review, you learn what the note became: one line — "maternal grandfather may be resource." No address. No phone. The study clock has not started, because as far as the paperwork is concerned, there is barely a person to study.

The fix is unglamorous and entirely within your power.

**Choices:**
- Write it properly this time: a letter to the agency with his full name, address, phone, and the words "I am asking for a kinship home study." → **tell_in_writing**  _(FLAG: kinNamedWritten; HIDDEN + named-kin)_

## [tell_in_writing] The letter

*Day 3 — Thursday, April 9, 2026*

However it got there, the file now holds a letter with a person's name, address, and telephone number, and a request a supervisor can route: kinship home study, maternal grandfather. Walter gets a call within days — not because the system is fast, but because a named, reachable person is the one thing every system knows how to process.

The study has three parts, Mr. Solberg explains: background clearances, a home visit, and interviews. "It's not a test he passes by being a good man," he says. "It's a list. We go down the list."

**Choices:**
- "Then get him the list. All of it, up front — not one surprise at a time." → **phone_interview**  _(FLAG: listRequested)_

## [phone_interview] The phone interview

*Day 4 — Friday, April 10, 2026*

Mr. Solberg calls Walter the next afternoon, and you listen on the extension your father insists on holding six inches from his ear. The worker asks about the house, the heart, the spare room, and Hugo — in that order, which Walter later reports with approval: 'He asked about the boy last and longest.'

At the end, Mr. Solberg says the sentence that separates a study from a rumor: 'I'm going to send you the requirements list. Everything on it. At once.'

**Choices:**
- Thank him, and tell your father to clear the kitchen table. Paper is coming. → **the_list**

## [the_list] The list

*Day 5 — Saturday, April 11, 2026*

To Mr. Solberg's credit, the list arrives as one document: clearances for Walter and any adult in the home, income verification, a medical statement from his doctor, and the home itself — sleeping arrangements, safety items, medications secured. Walter reads it twice at the kitchen table with a pencil, the way he used to read route changes.

"Medicines," he says. "Mine are in the bathroom cabinet. Boy could reach them on a chair." He says it before any worker does. That will matter more than he knows.

**Choices:**
- Help him start on the fixable things this weekend — the list is a ladder if you climb it before the visit, and a verdict if you read it after. → **fix_weekend**

## [fix_weekend] Saturday work

*Day 6 — Sunday, April 12, 2026*

The weekend becomes a project with a nine-year-old's name on it. A lockbox for the medications, screwed to the closet shelf. A handrail for the basement stairs, which Walter has been meaning to fix since 2019 and now fixes in an afternoon with his neighbor's drill. Hugo's room gets the bed from the attic, clean sheets, and the shelf of model buses moved down to eye level.

None of it is expensive. All of it is the difference between a study that reports problems and a study that reports solutions.

**Choices:**
- Spend $25 at the hardware store and keep the receipt in the study folder. → **clearances**  _(cash −25; FLAG: homeFixed)_
- Do the work with what is in the garage — lockbox from your brother, rail repaired not replaced. → **clearances**  _(cash −8; FLAG: homeFixed)_

## [clearances] Paper that travels slowly

*Day 9 — Wednesday, April 15, 2026*

Walter's clearances go in with his fingerprints on a Tuesday. His doctor's statement takes longer — the cardiologist's office faxes it to the wrong number once, because medical offices are where faxes go to be reborn as mysteries. You learn the study's least dramatic rule: nothing is submitted until somebody confirms it arrived.

You call the agency twice that week. The second call finds the fax. Persistence is not a personality trait in this system; it is a tracking method.

**Choices:**
- Ask Mr. Solberg for a checklist of what is still missing, in writing, so the study has a finish line you can see. → **program_letter**  _(FLAG: checklistKept)_

## [program_letter] Your side of the file

*Day 10 — Thursday, April 16, 2026*

A kinship study examines the caregiver. Your case examines you. Your program counselor's letter — attendance, phase progress, a drug screen history as clean as the program keeps — goes into the same review packet, because a judge deciding whether Hugo moves to his grandfather is also, always, deciding how this story is trending.

You are not the placement. You are the reason the placement is a bridge instead of a destination. The letter says so in a counselor's flat, credible prose.

**Choices:**
- Ask Mr. Solberg for the study checklist anyway — and put in your own written request for the case record under 55 Pa. Code § 3130.44(d), so the study's paper reaches you too. → **checklist**  _(FLAG: recordsRequested; HIDDEN + record-request)_

## [checklist] The finish line

*Day 12 — Saturday, April 18, 2026*

The written checklist says: clearances — received. Medical statement — received. Home visit — scheduled. One interview — Walter's, and one with you. Your program counselor will send attendance verification directly. For the first time since Hugo left your apartment, a piece of this case has an end you can point at.

The home visit is set for next week. Walter asks if he should bake. You tell him caseworkers have seen everything and pie is not on the list. He bakes anyway.

**Choices:**
- Be there for the visit if the agency allows — a daughter who shows up is data too. → **home_visit**

## [home_visit] The walk-through

*Day 16 — Wednesday, April 22, 2026*

Mr. Solberg walks the house with his list, and the house answers him: medications locked, handrail solid, Hugo's bed made, smoke detectors beeping their small green assent. He opens the bathroom cabinet out of professional habit and finds toothpaste and a man who planned ahead. "Your father fixed these before I flagged them," he says, and writes for a while.

What a home study records is not a house. It is whether the adults around a problem move toward it or wait to be told.

**Choices:**
- Walk him out. Ask the only question that matters: "What happens at the review on April 30th?" → **hugo_visit**

## [hugo_visit] Hugo, inspecting

*Day 18 — Friday, April 24, 2026*

The agency arranges Hugo's next visit at Walter's house — part visit, part quiet evidence. Hugo inspects the spare room with the seriousness of a building department: the bed, the shelf, the model bus at eye level. He tests the handrail twice, like a man who has seen a worker do it.

On the porch he asks his grandfather whether the school bus that stops at the corner is 'his bus.' It is the right route for Hugo's same school — a fact you confirm with the district that week, in writing, because school continuity is a sentence judges underline.

**Choices:**
- Confirm it in writing: same school, same route, stop at the corner. → **before_review**  _(FLAG: schoolConfirmed)_

## [before_review] Before the review

*Day 20 — Sunday, April 26, 2026*

What happens depends on the study being finished — reports written, approvals signed — and on the recommendation the agency carries into the courtroom. Yours is assembling well. One piece remains that is yours alone: a short written statement to the court supporting the placement, so the judge hears your voice asking for your father's home, not just the agency's voice reporting it.

Parents are parties in their children's cases. Parties may be heard. The smallest version of that right is a page with your name on it, filed before the hearing instead of wished for after it.

**Choices:**
- Write it: one page — the program, the plan, your father, and what Hugo asks for when he calls you (his room at Pop's). → **voss_call**  _(FLAG: motherStatement)_
- You will speak at the review instead. Writing feels like homework from a system that already took your son. → **voss_call**

## [voss_call] Mrs. Delacroix calls

*Day 21 — Monday, April 27, 2026*

Mrs. Delacroix — Hugo's foster mother — calls you the week before the review, which foster parents are not required to do and the good ones do anyway. 'He talks about the room,' she says. 'If the court moves him, we'll pack his things properly and I'll send the bus shelf photo with him. I wanted you to hear that from me.'

Foster parents receive notice of hearings and may be heard at them (42 Pa.C.S. § 6336.1). What Mrs. Delacroix will say, if asked, is that Hugo is ready and the grandfather is real. Support like that cannot be bought or faked — but it can be welcomed, in writing, so it reaches the file.

**Choices:**
- Thank her in a letter the agency gets a copy of. Bridges get built from both banks. → **walter_letter**

## [walter_letter] Walter's page

*Day 22 — Tuesday, April 28, 2026*

Walter writes his own statement for the court, one page, in handwriting like a route manifest: the house, the heart ('managed, see doctor's letter'), the room, the years he has known his grandson, and the last line, which he reads to you twice to make sure it is spelled right: 'I am not a backup plan. I am his grandfather.'

It is not a legal document. Courts are moved by legal documents that have a pulse. Your own statement is already filed; his will sit beside it, and the pair of them say what the study alone cannot: this placement has two generations asking for it.

**Choices:**
- File his page with yours. Then sleep. Tomorrow is paperwork's last mile. → **the_review**

## [the_review] The review

*Day 24 — Thursday, April 30, 2026*

The courtroom version of your father's spare room is a two-page report: clearances clear, medical managed, home safe, fixes made before they were findings. Mr. Solberg presents it. Mrs. Delacroix, Hugo's foster mother, tells the judge Hugo talks about his grandfather's model buses "like church."

The judge reads the report's last page, where the recommendation lives.

**Choices:**
- Wait for the sentence the whole spring has been walking toward. → **the_drive**

## [the_drive] The drive to court

*Day 24 — Thursday, April 30, 2026*

Walter drives, because Walter always drives, and parks with the care of a man for whom parking was once a profession. In the courthouse hallway, Hugo's file goes past on a cart — two inches thick already, for a nine-year-old who has done nothing but be loved in inconvenient circumstances.

Everything the spring built is in those two inches: your letter, his list, the lockbox receipt, the fax that was found. The judge is about to read the last page first, the way judges do. The last page is the recommendation.

**Choices:**
- Take your seat. → **outcome**

## [outcome] The recommendation

*Day 24 — Thursday, April 30, 2026*

What the judge can order depends on what the study can support — a finished study with an approval, or an unfinished one with a promise.

**Choices:**
- The study is complete and approved — clearances, medical, home, your statement — and the agency recommends the move. → **end_move**  _(REQUIRES: homeFixed; REQUIRES: checklistKept; REQUIRES: motherStatement)_
- The study is nearly there, but a piece of paper is still traveling. → **end_study**

## [end_move] Ending — The Spare Room, Occupied

*Day 24 — Thursday, April 30, 2026*

**Ending.**

**Debrief:** The court orders Hugo placed with his grandfather, effective this weekend, with your program schedule written into the order so visits and overnights build toward home. Walter, who dressed for court in his route-supervisor tie, accepts the judge's thanks with the nod of a man who has been handed a route he intends to run on time. Hugo's bed — the one from the attic, with the model buses at eye level — gets its boy.

Nothing in this scenario required money, connections, or a brilliant legal move. It required the kinship basics, in order: the relative named in writing with a way to reach him; the study treated as a list to climb before the visit instead of a verdict to fear after it; every slow-moving paper tracked until somebody confirmed it arrived; and your own voice in the file asking for it. Courts can only approve the homes that paper makes visible. Walter was ready in March. The study's job — and yours — was making the file able to see it.

What no strategy controls: the clearances and the judge. A clearance can surface something a family did not know it had to answer, and no letter fixes that overnight. This story's grandfather had a clean record and a managed heart. Another family's story has more chapters. The sequence still matters: it is how those chapters get found early, answered in writing, and weighed as facts — instead of arriving as surprises at the hearing.

## [end_study] Ending — Approved in Principle (partial)

*Day 38 — Thursday, May 14, 2026*

**Ending.**

**Debrief:** The judge praises the study's progress, approves your father as a placement resource in principle, and sets the move for the next review — fourteen days out — when the last verification is filed. Hugo spends two more weeks with the Delacroix family, who send him to Walter's for Sunday dinner in the meantime with the court's blessing. It is a good outcome wearing a waiting room's clothes.

The lesson is about paper travel time. Somewhere between the cardiologist's fax, the clearance office, and the report writer's desk, this case kept losing days it could not see — and the only instrument that finds lost days is a checklist, requested in writing, checked by a person who calls twice. Ask for the study's finish line early: what is missing, who holds it, and what date it is due. A study with a visible finish line finishes. A study without one becomes weather — everybody discusses it, nobody can schedule around it.

This ending is a partial win, and a common one: the placement is approved, the boy is loved in both houses, and the only cost was time. Name the cost anyway. In a child's calendar, two weeks is not a rounding error — and the next family over, the one that tracks its paper from day one, is the reason this scenario exists.
