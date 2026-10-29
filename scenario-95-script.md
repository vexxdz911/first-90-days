# THE FIRST 90 DAYS — Scenario 95: “Earning the Last Order”

*Human-readable script. This document and `scenario-95.json` are generated from a single source and match node-for-node: same IDs, same order, same choices, same effects.*

**The family is fictional — a composite. No real person's story appears here.**

**Content note:** This scenario depicts a trial-home winter ending in a closure hearing — services, paperwork, one documented incident, and a final order. There is no graphic content. Players may skip any scene or use the quick exit at any time.

**How to read effects:** `cash −40` changes the player's cash. `FLAG: name` sets a flag the engine tracks. `HIDDEN + item` means the case file quietly records that item at this choice — the player does not see it when it happens. `REQUIRES FLAG: name` means the choice is only available if that flag was set earlier; `REQUIRES NO FLAG: name` means it is only available if that flag was never set. `NOTE:` is text shown to the player right after choosing.

Start date: Monday, February 1, 2027. Day offsets are days since the scenario's start date.

## [start] Home, On Paper, Provisionally
*Day 0 — Monday, February 1, 2027 (dayOffset 0)*

Your name is Imogen Hart. Your son Cyril is ten, all elbows and questions, and for four months he has been home — home under a disposition that permits him to remain with you subject to conditions and supervision (42 Pa.C.S. § 6351(a)(1)), in a case that remains open, with an agency worker visiting on a schedule and a permanency hearing on April 12 that will make the statute's determinations (§ 6351(f)) one more time.

At that hearing, the outcomes on the menu (§ 6351(f.1)) include the one this winter is for: the court can find the conditions satisfied and the supervision no longer necessary — Cyril home, the case closed, the file's last page an order that ends the story. It is the only ending in this family's three years that is an ending.

What stands between February and that order is not a mystery. It is a list: two course sessions unfinished, an aftercare plan unsigned, a trial-home file containing notes you have never read, and the ordinary chaos of a real household, which the file will describe — accurately or not — depending on who writes it down first.

The family is fictional — a composite. The list is the realest thing in the story.

**Choices:**
- Ask your lawyer what 'closed' actually requires → **intake_call**
  - NOTE (shown after choosing): Ms. Ibarra's answer is a checklist. Checklists, in February, are a form of hope with boxes.

## [intake_call] The Intake Call
*Day 1 — Tuesday, February 2, 2027 (dayOffset 1)*

"Closure is a determination, not a mood," Ms. Ibarra says. "April 12, the court works the list: Cyril's safety, whether placement or supervision remains necessary, your compliance, your progress (§ 6351(f)(1), (2), (3)). If the file supports it, we ask the court to discharge him from supervision and close the case. If the file has holes — an unfinished course, an unsigned aftercare plan, a bad week described only by other people — the court's caution fills them, and caution, in a closing hearing, sounds like 'six more months.'

"So the winter is simple: finish the list, sign the plan, and read the file before the file is read at you. Start with the file. It is requestable, in writing, and it always surprises."

**Choices:**
- Start with the file → **lawyer**
  - NOTE (shown after choosing): The lawyer's office sends the request form the same day. Surprises, scheduled, are just information.

## [lawyer] Ms. Ibarra and the Last Hearing
*Day 3 — Thursday, February 4, 2027 (dayOffset 3)*

Her office wall has the case's whole archaeology in frames she doesn't discuss. On the desk: the April checklist, in her hand — course certificate, aftercare signatures, school letter, the step-down record, and a line she underlines twice: 'trial-home notes: VERIFY.' "The trial home period is the evidence for closure," she says. "It's also four months of other people's note-taking. Workers write fast, in cars, about several families. Errors in those notes are not conspiracies; they're Thursdays. But uncorrected, they're findings."

**Choices:**
- Ask how the notes get verified → **records**
  - NOTE (shown after choosing): 'You read them,' she says. 'All of them. With a pencil. It's the least glamorous sentence in law and it closes more cases than any argument I own.'

## [records] Reading the Trial-Home File
*Day 6 — Sunday, February 7, 2027 (dayOffset 6)*

The complete record — requested in writing, released on request under 55 Pa. Code § 3130.44(d), $10 in copies — covers October to January: visit notes, supervision logs, service reports, the school correspondence. You read it at the kitchen table after Cyril's bedtime, with the pencil, in one sitting, the way you once read the worst of it. This time the story is mostly good. Mostly. The pencil stops twice.

**Choices:**
- Read it all and mark the two places the notes are wrong → **file_findings** _(cash −10 ; FLAG: recordsRequested ; HIDDEN + Record — complete file requested in writing and read; trial-home notes audited)_
  - NOTE (shown after choosing): Two marks. One is a date. One is a sentence about a visit that did not happen the way the sentence says. Both are small. April will be built out of small things.
- Read the summaries and trust the attachments → **file_findings**
  - NOTE (shown after choosing): The summaries are where April's judge will start reading too. Trust, unpinned by verification, is how small errors become findings with your name on them.

## [file_findings] What the File Says About the Trial Home
*Day 9 — Wednesday, February 10, 2027 (dayOffset 9)*

Error one: a supervision visit is logged on a Tuesday you worked a double — the visit happened Thursday, with your sister present, and the note's 'mother unavailable, sister vague' describes a day that never occurred. Error two: a missed-appointment note for a clinic date that the clinic's own letter, three binders later, shows you attended. Neither error is sinister. Both sit in the progress section, where April's determinations will graze.

Corrections in this system are not made by phone and indignation. They are made in writing, with the true document attached, filed, and copied.

**Choices:**
- File a written correction with the clinic letter and your sister's statement attached → **kitchen_rules** _(FLAG: fileCorrected ; HIDDEN + Record — written correction filed: misdated visit and phantom missed appointment answered with documents)_
  - NOTE (shown after choosing): Filed, with copies. The file now contains both the error and its answer, adjacent, which is the most a correction can ever achieve — and it is enough, if it happens before April instead of during it.
- Raise both errors at the hearing, from memory, when they come up → **kitchen_rules**
  - NOTE (shown after choosing): They will come up as findings, stated by counsel from the file. Memory, objecting from the gallery of the witness chair, has a known win rate.

## [kitchen_rules] The Kitchen Rules
*Day 11 — Friday, February 12, 2027 (dayOffset 11)*

Cyril has posted the household's operating rules on the refrigerator, in marker, as a joke that is not entirely a joke: SHOES BY DOOR. HOMEWORK BEFORE SCREENS. MUM'S PHONE CHARGES IN KITCHEN (his emphasis, about your scrolling, fairly). INSIDE VOICES AFTER 9 (a rule with a history). The in-home worker photographed the list for the file in January and captioned it 'structure observed in home.' It is the only file entry you would have written exactly as written.

**Choices:**
- Leave the rules up and keep the winter boring → **course_sessions**
  - NOTE (shown after choosing): Boring is the trial home's whole aesthetic program. April's judge should be able to read this winter without once raising an eyebrow.

## [course_sessions] Two Sessions Left
*Day 13 — Sunday, February 14, 2027 (dayOffset 13)*

The final course — the advanced parenting module the plan saved for last — has two sessions left, both Saturday mornings, both conflicting with shifts you have already traded once. The certificate costs $15 in fees, because completion in this system always has a small toll booth at the end of it. Finishing converts the plan's service list from 'substantially complete' — a phrase judges hear as a weather report — to 'complete,' a word with edges.

**Choices:**
- Trade the shifts, attend both, and pay for the certificate → **pharmacy_run** _(cash −15 ; FLAG: sessionsDone ; HIDDEN + Services — final course completed; plan services finished in full)_
  - NOTE (shown after choosing): Certificate in hand, March 1. The plan's list is now a list of finished things. One toll booth remains: everything costs $15 in this story, including victory's paperwork.
- Ask the provider to waive the last two sessions given your progress → **pharmacy_run**
  - NOTE (shown after choosing): Providers waive nothing in writing, and 'substantially' is the word that will describe your services in April if they try.

## [pharmacy_run] The Pharmacy Run
*Day 15 — Tuesday, February 16, 2027 (dayOffset 15)*

Cyril's prescription, the bus, the pharmacy's particular slowness, your ex's mother in the vitamin aisle performing a chance encounter at full volume about Easter plans. The trial home's daily texture: logistics and other people's opinions, handled at walking pace, unrecorded by anyone. You buy the vitamins she recommends, because they are good vitamins and because some battles are beneath documentation.

**Choices:**
- Get home by dinner and keep the receipt in the folder → **homework_table** _(cash −8)_
  - NOTE (shown after choosing): The folder grows by a receipt. The winter's documentation is mostly this: proof of the ordinary, accumulating.

## [homework_table] The Homework Table
*Day 17 — Thursday, February 18, 2027 (dayOffset 17)*

Cyril's homework era is long-division and strong opinions about it. The in-home worker's step-down schedule has her coming weekly now instead of twice — the system's own metric of a household becoming ordinary. Her notes have improved in accuracy since your correction was filed, a cause and effect nobody will ever prove and everybody in the story believes.

**Choices:**
- Keep the table, the hour, and the routine exactly this boring → **aftercare**
  - NOTE (shown after choosing): Step-down proceeds on schedule. Boring, countersigned, weekly.

## [aftercare] The Unsigned Aftercare Plan
*Day 20 — Sunday, February 21, 2027 (dayOffset 20)*

The aftercare plan is the system's one genuinely kind invention: a written plan for after the case — who Cyril's counselor remains, what the school contact does, what number you call in a crisis at month nine when no worker is assigned anymore. It exists as a draft in the agency's outbox. It has existed as a draft for five weeks. Unsigned, it is a brochure. Signed by you, the counselor, and the school contact, it is the document April's judge will hold while deciding whether closure leaves this family equipped or merely alone.

**Choices:**
- Chase the signatures: yours, the counselor's, the school's, this week → **night_shift** _(FLAG: aftercareSigned ; HIDDEN + Aftercare — plan signed by parent, counselor, and school contact before the hearing)_
  - NOTE (shown after choosing): Three signatures in four days, obtained by the ancient technology of asking in person. The plan is now an exhibit, and closure has an infrastructure.
- Leave the plan to be finalized after the hearing → **night_shift**
  - NOTE (shown after choosing): After the hearing, the plan will be finalized in the world where the hearing already decided whether it was needed. Judges notice sequences like that. They are paid to.

## [night_shift] The Night Shift Problem
*Day 22 — Tuesday, February 23, 2027 (dayOffset 22)*

Your employer's new rotation offers nights at a differential that would end the money stress permanently and reorganize Cyril's evenings around your sister's availability. It is a real opportunity and a real complication, and the file will describe it — if you raise it with the worker in writing, with the childcare plan attached, as a documented arrangement; or if you don't, as a discovery. April is close enough that discoveries are the enemy's whole remaining arsenal, and the enemy, in this scenario, is surprise.

**Choices:**
- Take the rotation and file the childcare plan with the worker, in writing → **landlord_note** _(FLAG: scheduleDocumented ; HIDDEN + Employment — night rotation and childcare plan documented in writing before the hearing)_
  - NOTE (shown after choosing): Filed: rotation, differential, sister's signed availability, Cyril's evening routine. A change, documented, is a plan. Undocumented, it's a rumor with a start date.
- Take the rotation quietly — it's your job, not the case's → **landlord_note**
  - NOTE (shown after choosing): In an open case under supervision, the distinction between your job and the case is a legal fiction maintained by people with closed files.

## [landlord_note] The Landlord's Note
*Day 24 — Thursday, February 25, 2027 (dayOffset 24)*

Eleven months of rent, on time, in a building where the landlord notices such things professionally. His note — one line, signed — completes the housing column of the file. It cost a conversation about the boiler and no money at all, and it will sit in April's packet making the word 'stable' a citation instead of an adjective.

**Choices:**
- Ask for the one signed line and file it → **school_letter** _(FLAG: landlordNote ; HIDDEN + Housing — landlord's signed note on eleven months of tenancy filed)_
  - NOTE (shown after choosing): Filed. The packet's columns are filling with documents the way the winter filled with routines: one unglamorous item at a time.

## [school_letter] The School Stability Letter
*Day 27 — Sunday, February 28, 2027 (dayOffset 27)*

Cyril's school has watched the whole arc: the foster year, the trial home, the winter. His teacher's letter reports attendance at 96 percent, reading recovered, the long-division opinions undiminished. His counselor adds the line the letter will be quoted for: 'Cyril describes his home in the present tense and his future in the first person, which has not always been so.' Schools keep the child's version of the record. April should hear it in the school's hand, not yours.

**Choices:**
- Ask for the signed letter, with the attendance figures, for the April packet → **library_card** _(FLAG: schoolLetter ; HIDDEN + School — signed stability letter with attendance record obtained for the closure hearing)_
  - NOTE (shown after choosing): Signed, with the table. The child's present tense, documented by professionals who teach it.
- Tell the judge about Cyril's progress yourself at the hearing → **library_card**
  - NOTE (shown after choosing): You will be believed exactly as much as parents are believed in that room: warmly, generally, and below the threshold of findings. Letters cross it. Speeches admire it.

## [library_card] The Library Card
*Day 29 — Tuesday, March 2, 2027 (dayOffset 29)*

Cyril gets a library card in his own name, an event he treats with the gravity of a knighthood. The librarian laminates it on the spot. It will expire in three years, by which time — this is the thought you have in the children's section, unbidden — the case will have been closed for nearly all of them, and the file will be an archive other people keep, about a winter he remembers as long division and inside voices after nine.

**Choices:**
- Put the card's receipt in the folder, among the exhibits of the ordinary → **cyril_asks**
  - NOTE (shown after choosing): The folder's last section is now 'proof of ordinary life.' It is the thickest section. That is the argument, really. The rest is procedure.

## [cyril_asks] Cyril Asks About April
*Day 31 — Thursday, March 4, 2027 (dayOffset 31)*

'In April,' Cyril says, doing the long division with theatrical suffering, 'does the worker stop coming, or does she come forever?' He has identified the hearing's entire content. The honest answer: April decides, from the file, whether supervision continues. He considers this. 'Then the file should say I do my homework,' he says, 'because that's the main thing that happens here.' It does. He checked. A ten-year-old has audited his own record, which puts him ahead of most of the adults who will ever be paid to read it.

**Choices:**
- Tell him the truth: April is a reading, and the file is ready → **stepdown**
  - NOTE (shown after choosing): 'Good,' he says, returning to the division. 'It took long enough to write.' Out of the mouths of exhibits.

## [stepdown] The Step-Down Visits
*Day 34 — Sunday, March 7, 2027 (dayOffset 34)*

The worker's visits step down to monthly in March — the last scheduled one before April falls on a rainy afternoon where nothing happens at a level that redefines the word: homework, dinner, the rules observed being ordinary. She writes her note in the car. Yours is already written, in the home log you keep by the door: date, time, who was here, what was said, in the flat prose the file respects.

**Choices:**
- Log the visit in the home log, flatly and completely → **sunday_roast** _(FLAG: homeLog ; HIDDEN + Home log — supervision visits logged contemporaneously by the parent through the trial home)_
  - NOTE (shown after choosing): Logged. Two accounts of the same Thursday now exist, and for the first time in three years, they agree.
- Let the worker's note be the only account → **sunday_roast**
  - NOTE (shown after choosing): Hers is good this time. The log is not for good times; it is insurance written in advance against Thursdays that aren't.

## [rain_week] The Rain Week
*Day 36 — Tuesday, March 9, 2027 (dayOffset 36)*

A week of rain, a school cold, a missed bus, a dinner of toast — the trial home at its most unremarkable, navigated without incident or assistance. Nothing in the file will record the rain week, because nothing in it rose to the level of a note. That is what success looks like in the present tense: an absence in the record where crises used to be filed. It feels, from inside, like being forgotten by a system you once begged to notice you. It is the best feeling the system offers, and it took three years to earn.

**Choices:**
- Keep the routine through the weather → **incident_week**
  - NOTE (shown after choosing): Toast counts as dinner in the oral history. The file, mercifully, has no opinion about toast.

## [sunday_roast] The Sunday Roast
*Day 35 — Monday, March 8, 2027 (dayOffset 35)*

Your sister's Sunday roast is the trial home's standing engagement: Cyril narrates the library card; your sister, who covered the Thursday that the file misdated, retells the correction story with the pride of a woman whose signed statement is now part of a court record. Family, in the file, is a resource. Family at the table is just Sunday. The case has never been able to tell the difference, and increasingly, neither can you, and that confusion is what closure will feel like when it comes.

**Choices:**
- Drive home in the last of the rain with April three weeks out → **rain_week**
  - NOTE (shown after choosing): Three weeks. The list is nearly done. The winter has one more thing in it. Winters do.

## [incident_week] The Loud Week
*Day 43 — Tuesday, March 16, 2027 (dayOffset 43)*

It happens on a Tuesday: your ex — Cyril's father, uninvolved for two years — appears at the door after drinking, wanting 'to see his son,' and the conversation, conducted on the doorstep with Cyril inside doing homework, gets loud enough that a neighbor calls the police. The officers are professional and brief: he leaves with a warning, no arrest, no entry, Cyril never at the door. It is over in twenty minutes. It will live in the file forever — in whose words is the only question being decided tonight.

Your account: dated, timed, flat — door answered, child kept inside, police called by a neighbor, officers attended, he left, door locked, homework resumed. Plus the officer's card. Plus, tomorrow, a written note to the worker before she hears it from the report.

**Choices:**
- Write the account tonight and send it to the worker in writing tomorrow, with the officer's card copied → **worker_call** _(FLAG: incidentDocumented ; HIDDEN + Incident — doorstep incident documented contemporaneously and reported in writing by the parent first)_
  - NOTE (shown after choosing): Sent at 9 a.m., read by 10. When the police report reaches the file, it will find your account already there, matching it in every particular that matters. That is what documentation is for: not innocence — sequence.
- Say nothing and hope the police report never reaches the file → **worker_call**
  - NOTE (shown after choosing): Police reports reach files the way weather reaches porches. Hope is not a reporting protocol.

## [worker_call] The Worker's Call
*Day 45 — Thursday, March 18, 2027 (dayOffset 45)*

The worker calls Thursday. The conversation is the audit of your documentation strategy in real time: she has your written account (two days old), the police report (concordant), and her own note to write. 'You kept him inside, you didn't engage, it ended,' she says. 'That's what your note says and it's what theirs says.' What her note will say follows from what exists. In the other version of this week — the unsent one — her note would have begun 'agency learned from police report of an incident at the home,' and April would have had a very different paragraph to work with.

**Choices:**
- Ask her to confirm her note's substance in writing for the packet → **sister_stay** _(FLAG: workerConfirmed ; HIDDEN + Agency note — worker's account of the incident confirmed in writing; concordant with parent's report)_
  - NOTE (shown after choosing): Confirmed. The loud week enters April's file as a documented disturbance handled correctly, instead of a discovery. The difference is not what happened. The difference is entirely who wrote it down first, and how.

## [sister_stay] Your Sister Stays Over
*Day 48 — Sunday, March 21, 2027 (dayOffset 48)*

Your sister stays the weekend after the loud week — not because anyone is afraid, but because family shows up in rows after a squall, and Cyril, who heard nothing through the homework headphones he now owns, nonetheless absorbs the household's weather and is reassured by the extra chair at breakfast. The trial home's support structure, visible, ordinary, and — need it be said — logged.

**Choices:**
- Log the weekend like any other → **mailbox_morning**
  - NOTE (shown after choosing): Logged, flatly. Support, like everything else in this file, counts double when it's written down before anyone asks.

## [mailbox_morning] The Mailbox, With the Notice In It
*Day 52 — Thursday, March 25, 2027 (dayOffset 52)*

April's hearing notice is in the mailbox, with the date you have known for months stated officially: April 12, 10 a.m. Nothing in it is new. Everything in it is final-form. The packet goes to Ms. Ibarra's office this week for assembly: certificate, aftercare signatures, school letter, landlord's note, the corrected file pages, the incident account with the worker's confirmation, the home log, the step-down record — the winter, indexed.

**Choices:**
- Carry the packet to the lawyer's office and build the final version → **hearing_prep**
  - NOTE (shown after choosing): The packet's weight is the winter's argument, in the only units the court accepts: pages, in order, with dates.

## [hearing_prep] Assembling the Last Packet
*Day 55 — Sunday, March 28, 2027 (dayOffset 55)*

Ms. Ibarra assembles in the statute's order — safety, necessity, compliance, progress — because hearings are read in the statute's order. The loud week gets its own tab, with your account in front and the confirmation behind it, presented as what it is: a disturbance the record shows handled by the book. 'We do not hide it,' she says. 'A file that hides its bad weeks is a file whose good weeks get discounted. Ours can survive its own contents. That's the whole pitch for closure, really: this family's file no longer needs a supervisor to be believed.'

Copies for the packet: $7. Some tolls shrink as the road ends.

**Choices:**
- Pay for the copies and confirm the packet → **folder_final** _(cash −7 ; FLAG: packetBuilt ; HIDDEN + Closure packet — assembled in § 6351(f) order, including the documented incident and its confirmation)_
  - NOTE (shown after choosing): Assembled. The winter, in statute order, with tabs. April can now be a reading instead of an investigation.

## [folder_final] The Folder, Final Form
*Day 60 — Friday, April 2, 2027 (dayOffset 60)*

The night before, the folder gets its audit at the kitchen table — Cyril asleep, the rules still on the refrigerator in marker, now joined by the library card receipt. Everything April will be decided from is in your hands in duplicate. Ms. Ibarra's last instruction was the profession's benediction: 'Tomorrow, you mostly listen. The file talks. We built it to.'

Three years of this case taught you the file talks loudest. Tomorrow it says the closing words, if the winter was written down right. It was. You checked. Twice. With a pencil.

**Choices:**
- Sleep, in a house that is quiet after nine by its own posted rules → **courthouse**
  - NOTE (shown after choosing): Inside voices after 9. The house enforces its exhibit.

## [courthouse] The Hallway Bench, Last Time
*Day 66 — Thursday, April 8, 2027 (dayOffset 66)*

The hallway bench has held this family in every posture the system offers: terrified, hopeful, furious, bored. Today it holds a woman with a packet and a ten-year-old at school, in the present tense, being ten. Cyril's worker is there with the agency's report, which recommends — Ms. Ibarra has seen the filing copy — exactly what its evidence supports. Reports follow files. This one's file is yours as much as theirs.

**Choices:**
- Go in for the last reading → **waiting_room**
  - NOTE (shown after choosing): The clerk calls the case with the same voice she used in year one. Some things the system keeps constant so families can measure how much else has changed.

## [waiting_room] The Two Minutes
*Day 68 — Saturday, April 10, 2027 (dayOffset 68)*

The judge has the packet. The judge has the report. Two minutes of paper-shuffling stand between three years of case and its disposition, and in those two minutes the entire strategy of the winter is either real or it isn't: the finished list, the signed plan, the corrected notes, the documented loud week, the school's present tense.

**Choices:**
- Stand when the case is called → **hearing**
  - NOTE (shown after choosing): Stood. The file is open on the bench at three places. All three are yours.

## [hearing] The Last Hearing
*Day 70 — Monday, April 12, 2027 (dayOffset 70)*

The court works the statute's list aloud (42 Pa.C.S. § 6351(f)): safety — established on the step-down record and the documented winter; necessity of supervision — the contested question; compliance — complete, every item, with certificates; progress — the original circumstances alleviated, documented by school, landlord, counselor, and the file's own corrections. The loud week is raised by the court itself, from the packet, and answered from the packet: account, police concordance, worker's confirmation. It takes ninety seconds. Documented things take ninety seconds. Undocumented ones take hearings.

The outcome menu is before the court (§ 6351(f.1)). What your side asks for is the winter's whole object.

**Choices:**
- Ask the court to discharge Cyril from supervision and close the case, on the aftercare plan as written → **out_closed** _(REQUIRES FLAG: sessionsDone ; REQUIRES FLAG: aftercareSigned)_
  - NOTE (shown after choosing): The ask is made in the file's language: every determination supported, the aftercare signed, the services complete, the winter documented. The judge looks at the packet for a long moment before answering.
- Ask for six more months of supervision, voluntarily — to be safe → **out_continued**
  - NOTE (shown after choosing): Safe is a real instinct and the court will honor it exactly as asked. Courts grant requests; they rarely upgrade them. The winter's work supports the larger ask. The larger ask was not made.
- Say nothing about the loud week and let the determinations run → **out_revoked** _(REQUIRES NO FLAG: incidentDocumented)_
  - NOTE (shown after choosing): The loud week is in the police report, which is in the file, which is on the bench. Silence about it is not a strategy; it is an omission the other side gets to narrate.

## [out_closed] Discharged
*Day 70 — Monday, April 12, 2027 (dayOffset 70)*

The determinations are made on the record, each one landing on a document: Cyril is safe; supervision is no longer necessary; the plan's services are complete; the circumstances that brought him into care are alleviated, on evidence spanning the whole winter and the years before it. The court discharges Cyril from supervision, adopts the aftercare plan as the family's own document going forward, and closes the case.

Ms. Ibarra shakes your hand in the hallway with the formality of a woman closing a three-year file. 'The aftercare number still works,' she says. 'Nothing else about us needs to.' The worker wishes Cyril well with genuine warmth, and means it, and will never write a note about him again.

**Choices:**
- Walk out into April with the last order in the folder → **closed_letter**
  - NOTE (shown after choosing): The last order. Four pages. It will go in the folder behind the library card receipt, which is where this family keeps its most important documents now.

## [out_continued] Continued
*Day 70 — Monday, April 12, 2027 (dayOffset 70)*

The court, honoring the ask as made, continues supervision for six months with the conditions reduced — monthly visits, the aftercare plan noted as 'in progress,' a review in October at which closure will, the judge says with a look over the glasses that is half encouragement and half bookkeeping, 'be favorably considered on a similar record.'

Nothing was lost except time — six months of a ten-year-old's life under a worker's calendar, in a household that had already become ordinary. The winter's record will still be there in October. So will the larger ask, if anyone makes it.

**Choices:**
- Walk out with October circled → **continued_letter**
  - NOTE (shown after choosing): October. The file keeps. The ask, next time, is the only variable left in the case.

## [out_revoked] The Week, Narrated by Others
*Day 70 — Monday, April 12, 2027 (dayOffset 70)*

The agency's counsel raises the police report in the register of discovery: an incident at the home, in March, unreported by the mother, involving the child's father and law enforcement. Your account — written tonight in the story's other branch — does not exist. What exists is a doorstep, a volume level, and a silence where the mother's version should be, and into that silence the court pours its caution. The determinations stall at necessity: supervision, the court finds, must not only continue — the trial home's basis is shaken — and Cyril's placement is taken back under review, with a new disposition hearing set and interim placement with his aunt directed while it pends.

It is the same Tuesday. The same twenty minutes. The same officers, the same warning, the same homework finished inside. The only difference between this April and the other one is who wrote it down first — and that difference is the whole case.

**Choices:**
- Walk out with the new hearing date and the folder, heavier than it arrived → **revoked_letter**
  - NOTE (shown after choosing): The folder contains everything except one page: the account of a Tuesday night, due last month, writable in twenty minutes, unwritten.

## [closed_letter] The Last Order, At the Kitchen Table
*Day 73 — Thursday, April 15, 2027 (dayOffset 73)*

The order goes on the refrigerator, held by the magnet Cyril got at the school fair, beside his rules and below the library card receipt. He reads his name in it, and the word 'discharged,' which he pronounces like a weather event, and asks whether the worker lady can still come for tea. 'As a guest,' you say. 'Not for notes.' He approves of this distinction professionally, as a boy who has been noted about for three years and has opinions.

**Choices:**
- Start the first unrecorded week → **end_closed**
  - NOTE (shown after choosing): Tuesday will be loud or quiet as it likes. Nobody will write it down. That is what the order bought: a childhood off the record.

## [continued_letter] The Continued Order, At the Kitchen Table
*Day 73 — Thursday, April 15, 2027 (dayOffset 73)*

The order goes in the folder: continued, reduced, October circled. Cyril's life continues in its ordinariness, with a worker's visit monthly and a mother who now knows — having built the entire record for more — that she asked for less than her own file supported. The aftercare plan gets signed in May, in the quiet, without a hearing to need it. The case will close in October, in all likelihood, on the same winter's paper. Likelihood, however, is not an order, and October is not April.

**Choices:**
- Put October on the refrigerator and keep the file warm → **end_continued**
  - NOTE (shown after choosing): The file keeps. Files in this story always keep. The question is only ever what they are asked to do.

## [revoked_letter] The Aunt's House, Again
*Day 76 — Sunday, April 18, 2027 (dayOffset 76)*

Cyril goes to his aunt's on Friday with the library card in his pocket and a dignity about the arrangement that costs you more than the hearing did. The new disposition is in five weeks. The record for it will include, at last, your written account of the Tuesday — filed now, late, accurate, and permanently second. Ms. Ibarra's debrief is one sentence long and contains the whole scenario: 'The incident didn't reopen this case, Imogen. The silence did.'

The winter's other work is all still real: the certificates, the aftercare, the school letter. They will argue from the file in May, uphill, against a narrative now set in the file's hardest format: a judge's concern, entered on the record, about candor.

**Choices:**
- Begin the May file tonight, starting with the page that should have been March's → **end_revoked**
  - NOTE (shown after choosing): Tonight. In writing. Twenty minutes. The doctrine of this game, learned at the highest available tuition.

## [end_closed] Ending — Closed: The Last Order
*Day 77 — Monday, April 19, 2027 (dayOffset 77)*

The case is closed. Cyril Hart is a ten-year-old with a library card, a homework table, inside voices after nine, and a mother whose name no longer appears in any open file. The aftercare plan lives in a drawer with the counselor's number on it, available and — the plan's whole hope — unnecessary. No worker will summarize this family again. The file goes to an archive, complete, and its last pages are the winter's: certificates, signatures, corrections, a documented bad week handled correctly, and a discharge order.

It is the only full win in this batch of stories, and it was earned the way the game's doctrine says full wins are earned: by a record so complete that the system's own caution had nothing left to stand on.

**ENDING — Debrief:**

THE WIN, NAMED HONESTLY — A full win, stated plainly because it is one: Cyril is home, supervision is discharged, the case is CLOSED. The determinations that closed it were § 6351(f)'s, made on the record at a hearing under § 6351(e)(3)(i)'s rhythm, and the outcome is the (f.1) menu's most final item as this scenario frames it — return made unconditional. Nothing about the closure is provisional except childhood itself.

THE LAW IN THE BEATS — The posture is 42 Pa.C.S. § 6351(a)(1) (child permitted to remain with the parent under conditions and supervision) ripening, on a completed record, into discharge and closure at the permanency hearing's (f) determinations and (f.1) outcome choice. The winter's engine was 55 Pa. Code § 3130.44(d): the complete record, read and corrected in writing before it could be read aloud against the family. The aftercare plan is presented as practice, not statute — a document agencies prepare so closure has an infrastructure — and the scenario labels it no more than that.

THE HIGHEST-LEVERAGE MOVE — The incident account, written the night of the loud week and sent in the morning. Every other document proved the winter was good; that one proved the file could be trusted about the winter's worst twenty minutes. Closure is, in the end, a trust determination wearing a statute's clothes.

WHAT NO STRATEGY CONTROLS — The ex's arrival itself, the neighbor's phone call, the judge's temperament. The route controlled the list, the signatures, the corrections, and the sequence of the writing. Outcomes turn on those things plus the uncontrollable ones — and honesty requires adding: this winter, the controllable ones were, for once, sufficient.


## [end_continued] Ending — Continued: Six More Months of Almost
*Day 77 — Monday, April 19, 2027 (dayOffset 77)*

Six more months of supervision in a house that no longer needs it, on a record that already proved so. Cyril's life is unchanged in every particular except the calendar over it: a worker monthly, a review in October, a mother's requests audited by a system she has fully satisfied. The case will very likely close in October. It was closable in April. The difference is a single sentence never said in a courtroom: the ask.

Imogen keeps the file, as she was always going to. In October she will bring the same winter to the same bench, plus a spring of kept conditions, and make the ask she made today in its smaller form. Nothing in the system's design punishes the delay except time, which is the one thing it charges everyone.

**ENDING — Debrief:**

NAMED HONESTLY — A partial outcome below the best: identical record, identical law, smaller request, smaller result. The scenario places it above the revocation ending because the family is intact and the trajectory unbroken — and below closure because April was winnable in full, on paper the player already held. As in Scenario 91's middle ending, the binding constraint was the size of the ask relative to the record. The game repeats the lesson because the system does.

THE LAW IN THE BEATS — Courts choose outcomes from requests presented, on records presented (42 Pa.C.S. § 6351(f), (f.1)). A court asked for six more months of supervision rarely volunteers discharge instead; the deference runs toward the parties' stated positions. All the winter's law (§ 3130.44(d); § 6351(a)(1), (e)(3)(i), (f)) was satisfied. The variable was advocacy's oldest one: what was requested, in the room, on the day.

WHAT NO STRATEGY CONTROLS — The October outcome is a likelihood, not an order, and likelihoods in this system are subject to all the usual weather: new workers, new weeks, loud or otherwise. That is the true cost of the smaller ask — not the six months themselves, but six more months of exposure to everything that can happen to a family being watched.


## [end_revoked] Ending — Revoked: The Week That Wasn't Written
*Day 84 — Monday, April 26, 2027 (dayOffset 84)*

The trial home ends not with a crisis but with a narration. Cyril is with his aunt, safe and furious in the contained way of ten-year-olds who did their homework during the incident in question. The case reopens its placement question with the mother's credibility as its contested exhibit — a far worse posture than March's, manufactured entirely from a twenty-minute event and a one-page omission.

Everything else in the winter was done right, and it will all still count in May. It will count uphill, against a finding about candor, which is the one finding a parent cannot afford and the only one in this story that was truly self-inflicted. The system's records are patient. They simply insist on being written by somebody, and they are indifferent — fatally, mechanically indifferent — as to whom.

**ENDING — Debrief:**

WHY THIS ENDING — Nothing in the verified law required this outcome; everything in the documented practice of permanency review predicts it. A supervision case runs on the agency's and the court's picture of the home (42 Pa.C.S. § 6351(f)(1), (3)), and an undisclosed police-attended incident, surfacing from the report rather than the parent, damages the one asset closure is made of: the court's confidence that the record is complete. The incident itself was survivable and was, in the winning route, survived in ninety seconds. The silence was not survivable, because in a paper system, silence about a documented event reads as concealment, and concealment reads as risk.

THE LAW THAT WAS AVAILABLE — The same instruments as the winning route, none of them exotic: the written account (a use of the record, under the discipline of 55 Pa. Code § 3130.44(d)'s world), the completed services, the signed aftercare, the corrected file. The scenario withholds no magic. It withholds one page, and shows the price.

WHAT NO STRATEGY CONTROLS — The ex's drinking, the neighbor's call, the officers' attendance: all outside anyone's control, and none of it decisive. What was decisive sat at a kitchen table for a month, unwritten. The game's doctrine holds that most outcomes turn on workers, judges, and luck. This ending is the exception that teaches the rule's boundary: sometimes the decisive variable is a single page, and it is yours.

