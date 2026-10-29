# THE FIRST 90 DAYS — Scenario 90: “The Remand”

*Human-readable script. This document and `scenario-90.json` are generated from a single source and match node-for-node: same IDs, same order, same choices, same effects.*

**The family is fictional — a composite. No real person's story appears here.**

**Content note:** This scenario depicts the weeks between an appellate victory and the remand hearing it produced — paperwork, visits, and one courtroom morning. There is no graphic content. Players may skip any scene or use the quick exit at any time.

**How to read effects:** `cash −40` changes the player's cash. `FLAG: name` sets a flag the engine tracks. `HIDDEN + item` means the case file quietly records that item at this choice — the player does not see it when it happens. `REQUIRES FLAG: name` means the choice is only available if that flag was set earlier; `REQUIRES NO FLAG: name` means it is only available if that flag was never set. `NOTE:` is text shown to the player right after choosing.

Start date: Monday, November 2, 2026. Day offsets are days since the scenario's start date.

## [start] The Order With the Word 'Vacated'
*Day 0 — Monday, November 2, 2026 (dayOffset 0)*

Your name is Bogdan Lis. You drive a delivery route that starts before dawn, and your son Piotr is twelve — old enough to read a court order over your shoulder, which is what he is doing, by phone photo, from his foster home across the county.

The Superior Court's opinion arrived at your lawyer's office this morning and at your kitchen table tonight. The disposition order that placed Piotr is VACATED — undone — because the findings beneath it did not support it on the record made. The case is remanded: sent back to the same courtroom, for a new hearing, done properly.

"Does that mean I come home?" Piotr asks. The honest answer is the shape of this whole story: it means the question gets asked again, correctly. The remand hearing is set for Monday, December 7. Five weeks. What fills them will decide the answer.

The family is fictional — a composite. Remands are real, and they are won or lost in the weeks nobody writes songs about.

**Choices:**
- Ask your lawyer what a remand actually buys — and what it doesn't → **lawyer**
  - NOTE (shown after choosing): Mr. Abernathy's answer fits on an index card. It is still worth hearing in full.

## [lawyer] What 'Vacated' Buys
*Day 2 — Wednesday, November 4, 2026 (dayOffset 2)*

"It buys a hearing," Mr. Abernathy says. "Not a result. The old order is gone — the findings that held it up were not supported, so the panel struck it. On remand, the court holds the disposition hearing again and must do the thing it skipped: enter findings on the record (42 Pa.C.S. § 6351(b)) — whether keeping Piotr home is contrary to his welfare, whether reasonable efforts were made — and choose from the disposition's actual menu (42 Pa.C.S. § 6351(a)): he can be permitted to remain with you under conditions and supervision, or temporary legal custody can go to a qualified individual, including a relative."

"The agency will come ready this time. So the question of the next five weeks is simple: what will our record look like when the court starts making findings on it?"

**Choices:**
- Ask what the record needs that it didn't have before → **work_boss**
  - NOTE (shown after choosing): "Proof of the plan, not the plan," he says. "Paper for every sentence we intend the judge to say."

## [work_boss] The Route Manager
*Day 3 — Thursday, November 5, 2026 (dayOffset 3)*

Your route manager keeps the schedule that the first hearing described, in the agency's words, as 'unstable.' It is not unstable; it is early. But the only version of it the court has ever seen is an adjective. The signed version — routes, hours, the Saturday swap arrangement, the supervisor's phone number — is a page your manager will sign if asked like a person and not like a subpoena.

**Choices:**
- Ask him, in person, to sign the schedule letter → **payday** _(FLAG: scheduleLetter ; HIDDEN + Employment — signed schedule letter obtained for the remand record)_
  - NOTE (shown after choosing): Signed, dated, with the Saturday arrangement spelled out. An adjective, answered by a document.
- Let the lawyer describe the schedule at the hearing instead → **payday**
  - NOTE (shown after choosing): Lawyers describing schedules are how 'unstable' got into the record the first time.

## [payday] Payday
*Day 4 — Friday, November 6, 2026 (dayOffset 4)*

Payday, in the remand season, is an exercise in allocation: the transcript money aside, the bus pass renewed, Piotr's birthday in November funded at the level of a twelve-year-old's ambitions (a chess clock, because the eleven-move loss has been analyzed and a rematch economy is forming). What is left after the allocations is not much, which is the ordinary condition of the families in these stories, and is recorded here because the record — unlike the agency's first account of Bogdan — insists on his actual arithmetic: a man who budgets for a son's chess clock in the same week he budgets for transcripts is a data point about priorities that no adjective survives.

**Choices:**
- Bank the transcript money and move to the record work → **record_again**
  - NOTE (shown after choosing): Allocated. The remand's paper campaign is funded at the level of its actual cost: tens of dollars and five weeks of evenings.

## [record_again] The Record, Again — On Purpose
*Day 5 — Saturday, November 7, 2026 (dayOffset 5)*

There is a temptation, after winning an appeal, to treat paper as beneath you. Mr. Abernathy treats it as the whole game: order the transcripts of the first hearings (the panel's opinion quotes them; the remand judge will have read them), and request the agency's complete record in writing — released on request under 55 Pa. Code § 3130.44(d) — because the agency's recommendation on remand is being written right now, from that file, and you are entitled to read what it is being written from. The transcripts cost $20.

**Choices:**
- Order the transcripts and request the complete agency record, in writing → **uncle_call** _(cash −20 ; FLAG: recordsRequested ; HIDDEN + Record — transcripts ordered; complete agency file requested in writing for the remand)_
  - NOTE (shown after choosing): Receipt in the folder. The remand will be fought over a record both sides have actually read.
- Save the $20 — the panel already said the record was thin → **uncle_call**
  - NOTE (shown after choosing): Thin is what it was. What it becomes in five weeks is being decided by people currently reading the whole file.

## [uncle_call] The Uncle in Pittsburgh
*Day 7 — Monday, November 9, 2026 (dayOffset 7)*

Piotr's uncle — your brother, a machinist in Pittsburgh with a spare room and strong opinions about caseworkers — has said for a year that Piotr could come to him. The disposition menu includes temporary legal custody to a relative (42 Pa.C.S. § 6351(a)(2)(i)), and the remand court will want to know whether the kin option is real or rhetorical. Real requires an assessment: clearances, a home visit, paperwork with his name spelled right. Rhetorical requires nothing, and persuades accordingly.

**Choices:**
- Ask him to start the kinship assessment now, paperwork and all → **bus_pass** _(FLAG: kinAssessed ; HIDDEN + Kinship — uncle's assessment begun; the (a)(2)(i) option made real for the remand court)_
  - NOTE (shown after choosing): He grumbles about forms for exactly one minute, then asks where to sign. Family, in this system, is a verb with attachments.
- Keep him as a name to mention at the hearing → **bus_pass**
  - NOTE (shown after choosing): A name mentioned is a name weighed as a name. The court has practice at telling the difference.

## [bus_pass] The Bus Pass
*Day 8 — Tuesday, November 10, 2026 (dayOffset 8)*

Piotr's weekend visits restart under the existing order while the remand waits — the vacated disposition does not suspend the case; it reopens one question in it. The visit is across the county, the bus pass is $8, and your route ends at 2 p.m. if nothing goes wrong on Route 30, a road with opinions.

**Choices:**
- Buy the pass and protect the weekends like they're exhibits → **school_letter** _(cash −8 ; FLAG: visitsProtected)_
  - NOTE (shown after choosing): Because they are. The remand judge will read the visit record the way the panel read the transcript: as the facts.

## [school_letter] The School Counselor's Letter
*Day 10 — Thursday, November 12, 2026 (dayOffset 10)*

Piotr's school counselor has known him since fourth grade — the meltdown year, the improvement since, the honor roll in spring. Her letter exists in draft in her desk. What it needs is a reason to be finished, signed, and sent to a lawyer instead of a file: a hearing date, a name, and a parent who asks in writing and says thank you like he means it.

**Choices:**
- Ask her, in writing, for the signed letter for the December hearing → **progress_file** _(FLAG: schoolLetter ; HIDDEN + School — counselor's signed letter obtained for the remand record)_
  - NOTE (shown after choosing): Signed on school letterhead. The improvement arc of a twelve-year-old, attested by the person who watched it.
- Mention it to Mr. Abernathy and hope it materializes → **progress_file**
  - NOTE (shown after choosing): Hope is not a courier. Letters in desks tend to stay in desks.

## [progress_file] Eight Months of Paper
*Day 13 — Sunday, November 15, 2026 (dayOffset 13)*

Your progress since the first hearing is real: the parenting course finished in June, the counseling attendance unbroken since April, the schedule stabilized on paper in March. Real — and scattered across three offices, a church basement, and your kitchen drawer. A remand hearing runs on findings, and findings run on exhibits. Assembling yours costs an evening and $10 in copies, and transforms 'I've been doing everything' from a claim into a stack.

**Choices:**
- Assemble the progress exhibits into a single filed packet → **visit_weekend** _(cash −10 ; FLAG: progressRecord ; HIDDEN + Exhibits — eight months of progress assembled as a filed packet for the remand)_
  - NOTE (shown after choosing): Tabbed, dated, in order. The stack has a table of contents. The stack is the argument.
- Bring the originals loose in the folder and explain as needed → **visit_weekend**
  - NOTE (shown after choosing): Explaining as needed is the first hearing's strategy. It has a track record, and the track record has an opinion from the Superior Court.

## [visit_weekend] A Weekend Visit, Weighed
*Day 16 — Wednesday, November 18, 2026 (dayOffset 16)*

The visit goes the way the good ones go: Piotr beats you at chess in eleven moves, asks about the hearing in the tone of a boy asking about weather in a country he might move to, and eats two helpings of everything. The visit supervisor's log entry will be three lines long. In five weeks, a judge will read those three lines as data.

**Choices:**
- Ask, in writing, for the log to note the full visit and the chess result → **kitchen_table** _(FLAG: visitLog ; HIDDEN + Visit log — full weekend visit noted in writing, at the parent's request)_
  - NOTE (shown after choosing): 'Father arrived on time; visit completed in full; child relaxed throughout.' Three lines. Load-bearing.
- Leave the log to the supervisor's memory → **kitchen_table**
  - NOTE (shown after choosing): Her memory is excellent and she writes logs for eleven families. Paper remembers for everyone at once.

## [kitchen_table] The Kitchen Table, Honestly
*Day 18 — Friday, November 20, 2026 (dayOffset 18)*

The hard question of the remand sits at your kitchen table at midnight: if Piotr comes home, what does Tuesday look like? The route starts at 4 a.m. The school bus comes at 7. The honest plan — neighbor Mrs. Almeida covers 5:30 to 7 on route days, uncle on call, counselor's check-in Thursdays — is a good plan. It exists nowhere on paper. The agency's meeting is Thursday, and its recommendation is being drafted from adjectives.

**Choices:**
- Write the home plan down, hour by hour, with names → **agency_meeting** _(FLAG: homePlan ; HIDDEN + Home plan — written hour-by-hour supervision plan with named caregivers)_
  - NOTE (shown after choosing): One page. Uncomfortable to write, because it admits the gaps exist — and covers them, by name, which is the entire point.
- Keep the plan in your head — you know your own Tuesdays → **agency_meeting**
  - NOTE (shown after choosing): You do. The record does not. The record is the only one of you who will be in the room making findings.

## [agency_meeting] The Agency's New Position
*Day 20 — Sunday, November 22, 2026 (dayOffset 20)*

Thursday's meeting has the particular politeness of an organization that lost an appeal and read the opinion carefully. The recommendation for remand, the worker says, is 'open' — which means it is being written this week, from the file: the progress packet, the visit log, the school letter, the schedule letter, the home plan — or from the absence of them. 'If there's a plan,' the supervisor says, in the tone of a person leaving a door visibly ajar, 'it should be in the file before the hearing, not described at it.'

**Choices:**
- Hand over the written home plan and the exhibit packet for the file, today → **letter_from_piotr** _(FLAG: packetFiled ; HIDDEN + Agency file — home plan and progress packet filed before the remand hearing)_
  - NOTE (shown after choosing): Copies stamped, receipt kept. The recommendation will now be written about documents, not about gaps.
- Describe the plan warmly and promise the paper later → **letter_from_piotr**
  - NOTE (shown after choosing): Warm descriptions evaporate at office temperature. The recommendation is drafted Friday.

## [letter_from_piotr] The Letter From Piotr
*Day 21 — Monday, November 23, 2026 (dayOffset 21)*

It arrives through the visit bag, in a twelve-year-old's hand that has recently become legible under protest: Piotr has written the court a letter. It is half a page. It says he knows the judge will decide, that Uncle's house is 'fine and has a dog,' that his dad's Tuesdays are 'actually covered, Mrs. Almeida is real,' and that he would like to go home 'if the plan is the one with my name on the fridge.' He signs it with his full name and his school.

A child's letter is not a vote, and the court will not treat it as one. It is evidence about a child's experience of the two houses on the menu — admissible in the broad sense that remand courts hear the child's world from every document that honestly describes it — and it exists, like everything else in this story, because somebody wrote something down.

**Choices:**
- File Piotr's letter with the packet, through counsel, unedited → **piotr_asks** _(FLAG: childLetter ; HIDDEN + Child's voice — Piotr's own letter filed with the remand packet, unedited)_
  - NOTE (shown after choosing): Filed as written, misspellings and all. A record that corrects a child's spelling would correct anything, and courts can tell.

## [piotr_asks] Piotr Asks Directly
*Day 23 — Wednesday, November 25, 2026 (dayOffset 23)*

"Uncle says I can have the spare room," Piotr says on the phone, in the careful voice of a boy translating between adults. "Dad. Which one is it — home, or Uncle's?" Both doors are on the disposition menu (42 Pa.C.S. § 6351(a)(1) and (a)(2)(i)), and both, after the remand, are more real than they were in October. What he needs from you is not a promise. It is the truth in twelve-year-old units.

**Choices:**
- Tell him the truth: the judge decides December 7, both plans are real, and you'll tell him the day it happens → **hearing_prep** _(FLAG: piotrTold)_
  - NOTE (shown after choosing): 'Okay,' he says. 'December 7.' A date, held by a twelve-year-old with total recall. The system should be so reliable.

## [hearing_prep] The Night Before, Again
*Day 28 — Monday, November 30, 2026 (dayOffset 28)*

The folder, second edition: the panel's opinion with the key paragraphs underlined; the exhibit packet; the home plan; the schedule letter; the school letter; the visit log; the kinship assessment receipt; the § 3130.44(d) request and the agency file it produced — read, all of it, including the parts that sting.

Last time you entered this courtroom carrying hope and a work schedule described by somebody else. Tomorrow you carry a record. It is heavier. That is the point of it.

**Choices:**
- Sleep badly, wake early, and see what the morning brings → **snow_day**
  - NOTE (shown after choosing): The morning brings weather, because December has no respect for narrative structure.

## [snow_day] The Snow Day
*Day 33 — Saturday, December 5, 2026 (dayOffset 33)*

The weekend before the hearing, snow closes Piotr's school on Friday and turns the last weekend visit into an expedition: the uncle drives down through it because 'the boy's schedule is the boy's schedule,' the visit runs long with the school's blessing, and the visit log acquires an entry written by the supervisor in a hand slowed by admiration: 'Family maintained the visit through a weather closure; child unbothered; plan discussed calmly by all adults.'

It is not an exhibit anyone planned. It is the home plan, stress-tested by December, in writing, two days before the court makes findings about exactly that plan's reliability.

**Choices:**
- Ask for a copy of the log entry for the packet, and be at the courthouse by 8:30 on Monday → **courthouse_steps** _(FLAG: snowLog ; HIDDEN + Visit log — weather-closure visit documented; the home plan stress-tested on paper)_
  - NOTE (shown after choosing): Copied. The packet's last page is about a snowstorm. Findings about the future are built from exactly such pages.

## [courthouse_steps] The Courthouse Steps
*Day 34 — Sunday, December 6, 2026 (dayOffset 34)*

Mr. Abernathy, on the steps, gives the remand its whole theory in one breath: "The panel said the findings didn't support the order. Today the court must make findings — on the record (§ 6351(b)) — and we have spent five weeks making sure the record supports the findings we want. Whatever the court chooses from the menu, it will choose it about documents. Ours are in."

Inside, the courtroom has the same chairs. Everything else about the morning is different, because the file is.

**Choices:**
- Go in and let the record be read → **remand_hearing**
  - NOTE (shown after choosing): Piotr's uncle is in the second row, in a suit that predates the case. Family, present, assessed, on paper.

## [remand_hearing] The Remand Hearing
*Day 35 — Monday, December 7, 2026 (dayOffset 35)*

The judge opens by stating what the Superior Court held, and that findings will be entered on the record today. The agency presents its recommendation. Your lawyer rises. The hearing now runs on what five weeks put into the file — or didn't.

**Choices:**
- Present the progress packet and the written home plan, and ask for return under § 6351(a)(1) with conditions → **findings_home** _(REQUIRES FLAG: progressRecord ; REQUIRES FLAG: homePlan)_
  - NOTE (shown after choosing): Exhibit by exhibit, hour by hour. The judge asks about Tuesdays. The plan answers by name. This is what findings look like when they have something to stand on.
- Ask the court for temporary legal custody to Piotr's uncle under § 6351(a)(2)(i) → **findings_kin**
  - NOTE (shown after choosing): A real option, assessed and ready — the bridge, chosen over the homecoming.
- Ask the court to simply restore matters as they were before the appeal → **findings_placed**
  - NOTE (shown after choosing): As they were is the one disposition the panel's opinion forecloses. The judge's face says so before his ruling does.

## [findings_home] Findings, Dictated Aloud
*Day 35 — Monday, December 7, 2026 (dayOffset 35)*

The judge makes the findings the way the statute contemplates: aloud, on the record, one by one. Continuation in the father's home, under the conditions and supervision set out in the written plan, is not contrary to the child's welfare; reasonable efforts were made; the progress documented in the exhibits is credited by exhibit number. Piotr is permitted to remain — no, the judge corrects himself, with the ghost of a smile — to RETURN to his father's home, subject to the plan's conditions, agency supervision, and review in ninety days. (42 Pa.C.S. § 6351(a)(1))

In the second row, the uncle in the old suit nods like a man whose spare room just became a holiday address instead of an address. Relief can wear that face too.

**Choices:**
- Walk out and call Piotr with the date → **end_home**
  - NOTE (shown after choosing): 'December 7,' he says. 'You told me December 7.' 'I told you the judge decides December 7.' 'Same thing,' says Piotr, twelve, wrong and right at once.

## [findings_kin] Findings, Dictated Aloud
*Day 35 — Monday, December 7, 2026 (dayOffset 35)*

The judge makes findings on the record: the home plan is credited as genuine but thin at its edges — the route, the hours, the single named backup — and the kinship resource is assessed, willing, and ready. Temporary legal custody is transferred to Piotr's uncle (42 Pa.C.S. § 6351(a)(2)(i)), with the reunification goal intact, liberal visitation, and the father's conditions carried forward as the plan Piotr comes home on.

It is not the ending Bogdan argued for. It is also not the ending October threatened: Piotr goes to family, the goal stays return, and the record that will be read at the next review is the one his father built.

**Choices:**
- Walk out and call Piotr with the plan → **end_kin**
  - NOTE (shown after choosing): 'Uncle's,' he says. 'And then home.' 'And then home,' you say, 'on paper with dates.' He accepts this. He has your relationship with paper now.

## [findings_placed] Findings, Dictated Aloud
*Day 35 — Monday, December 7, 2026 (dayOffset 35)*

The judge makes findings on the record — that much, the appeal won forever. On the record before him, though: a progress story told rather than exhibited, a home plan described rather than written, a kinship option named rather than assessed. The findings, made properly this time, support the disposition he reaches: placement continues, with the goal unchanged and the deficiencies listed, specifically, as the work of the next review period.

The procedure was flawless. It is the loneliest sentence in the story.

**Choices:**
- Walk out with the list of deficiencies in your folder → **end_placed**
  - NOTE (shown after choosing): A specific list is a terrible gift and a useful one. It is, at least, a list — the first one this case has ever given him in writing.

## [end_home] Ending — Home on Remand, With Conditions and a Calendar
*Day 42 — Monday, December 14, 2026 (dayOffset 42)*

Piotr comes home on Friday, with the plan's conditions pinned inside a kitchen cabinet: Mrs. Almeida at 5:30 on route days, Thursdays with the counselor, the agency's supervision visits, review in ninety days. The case is open. The file is thick. None of that is hidden from either of them — the plan on the cabinet is the same paper the judge read.

The appeal vacated an order. The five weeks after it — the letters, the packet, the plan, the log — are what turned a vacated order into a homecoming. Remands do not return children. Records do, one exhibit at a time.

**ENDING — Debrief:**

THE WIN, NAMED HONESTLY — A partial win in form and a full one in fact: Piotr is home, but under § 6351(a)(1) conditions and supervision, with the case open and a review on the calendar. This guide calls it partial because the system's file on this family remains open — and because honesty about that is the price of the game's other claims.

THE LAW IN THE BEATS — On remand the court re-ran disposition under 42 Pa.C.S. § 6351: findings entered on the record before a removing disposition (§ 6351(b)); the outcome menu of § 6351(a)(1) (remain/return with parent under conditions and supervision) and (a)(2)(i) (temporary legal custody to a qualified individual, including a relative). The record the findings stood on was assembled through the written record request, 55 Pa. Code § 3130.44(d). The appeal that created the remand was governed by the ordinary clock (Pa.R.A.P. 903(a)) and the rule that a panel reviews the record made below.

THE HIGHEST-LEVERAGE MOVE — The written home plan. Every other document proved the past; the plan was the only exhibit that proved a Tuesday. Findings about the future need one of those.

WHAT NO STRATEGY CONTROLS — The remand judge's weighing, the agency's recommendation as first drafted, Route 30. The route controlled what the findings could stand on. It did not control the judge — it gave him something to stand on, which is the most any record ever does.


## [end_kin] Ending — Custody to Family: The Bridge Holds
*Day 42 — Monday, December 14, 2026 (dayOffset 42)*

Piotr moves to Pittsburgh on Saturday, to a spare room that has been ready, in every sense the system can measure, since November. School transfers with a counselor's letter smoothing the way. Bogdan's conditions continue as the written plan for return, with dates, and the goal on the court's order still reads reunification.

It is not home. It is family, stability, and a bridge with Bogdan's name on both ends — and it was chosen by a judge making findings on a record, not by a default. The next review will read the same file, plus six months of Piotr thriving and Bogdan completing the plan the order names.

**ENDING — Debrief:**

THE WIN, NAMED HONESTLY — A partial win: temporary legal custody to a relative under 42 Pa.C.S. § 6351(a)(2)(i), with reunification as the standing goal. It ranks below return home because that is what it is — and above continued stranger placement because kinship, assessment, and a dated plan are real goods the record bought.

THE LAW IN THE BEATS — Same § 6351 frame as the winning route: (b)'s on-the-record findings, (a)(2)(i)'s kinship custody, and the permanency machinery that keeps the goal and the reviews running (§ 6351(e)(3)(i), (f)). The kinship option persuaded because it was assessed, not invoked — the difference between a resource and a rumor, documented in the file through the § 3130.44(d) record work.

WHAT NO STRATEGY CONTROLS — The judge weighed a genuine plan against a thin margin at 5:30 a.m. and chose the bridge. Another judge, same record, might choose home. The route's claim is only that both were choosable — because for the first time in this case, the record supported more than one answer.


## [end_placed] Ending — The Order, Rewritten Properly This Time
*Day 49 — Monday, December 21, 2026 (dayOffset 49)*

Placement continues. The order that continues it is everything the first order wasn't: findings stated, evidence weighed by name, deficiencies listed with dates. It will be much harder to appeal than the first one was, and Bogdan's lawyer says so in the car, because it is true and because he is that kind of lawyer.

The appeal was won. The remand was lost in the five weeks after it, at kitchen tables and in unrequested files — the weeks when the record for the new hearing was being assembled by the agency, daily, and by Bogdan, eventually. The list in his folder is specific, dated, and achievable. The next review is in six months (§ 6351(e)(3)(i)). Paper is still the whole game; the game is simply in its next period.

**ENDING — Debrief:**

WHY THIS ENDING — A vacated order buys a hearing, not a result. On remand, disposition runs on the record then before the court (§ 6351(a), (b)). Where progress is narrated rather than exhibited and the plan described rather than written, proper findings can still support placement — the procedure the appeal won protects the process, not the parent. The scenario states this without varnish because it is the remand's central documented lesson: appellate victories expire into trial-level work immediately.

WHAT WAS AVAILABLE — Every document in the winning route existed to be made: the signed schedule, the school letter, the exhibit packet, the written plan, the kinship assessment, the complete record under 55 Pa. Code § 3130.44(d). None required money Bogdan didn't spend elsewhere in the story, or luck. They required the five weeks.

WHAT NO STRATEGY CONTROLS — Piotr's welfare was never the variable here; Bogdan's love appears nowhere in the findings, because findings run on evidence. That is not the system's cruelty. It is the system's literacy — it reads paper. The route exists to teach a parent to write in the language the court is required to read.

