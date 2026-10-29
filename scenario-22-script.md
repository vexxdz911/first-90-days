# THE FIRST 90 DAYS — Scenario 22: “Fifteen Months, Twins”

*Human-readable script. This document and `scenario-22.json` are generated from a single source and match node-for-node: same IDs, same order, same choices, same effects.*

**The family is fictional — a composite. No real person's story appears here.**

**Content note:** This scenario depicts months 13–16 of a dependency case involving four-year-old twins — permanency reviews, a treatment timeline, and the federal filing timeline, assessed child by child — told through procedure and paperwork. There is no graphic content. Players may skip any scene or use the quick exit at any time.

**How to read effects:** `cash −40` changes the player's cash. `FLAG: name` sets a flag the engine tracks. `HIDDEN + item` means the case file quietly records that item at this choice — the player does not see it when it happens. `NOTE:` is text shown to the player right after choosing.

Start date: Tuesday, February 4, 2025 (placement). Day offsets are days since the scenario's start date. The ASFA fifteen-month date is Monday, May 4, 2026 (dayOffset 454).

## [start] Two Names on Every List
*Day 392 — Tuesday, March 3, 2026 — Tuesday, March 3, 2026 (dayOffset 392)*

Your twins, Maya and Milo, are four. They were placed together fourteen months ago, in the same foster home, on the same day — and for a long time the case treated them as one word: the twins.

They are not one word anymore. Maya is thriving: preschool loves her, her speech has caught up, and her worker writes 'ready' in margins she does not think you see. Milo is mid-treatment — feeding and speech therapy, twice a week, with a team that says, carefully, 'He is progressing. He is not finished.'

You have done the plan: treatment completed, job kept, an apartment with two small beds. What remains is not one question. It is two questions wearing one coat, and a federal clock that answers to each child separately.

**Choices:**
- Look at the two calendars — the twins', and the case's → **calendars**
  - NOTE (shown after choosing): Two children. Two timelines. One date circled on a file you have not seen yet.

## [calendars] Two Calendars
*Day 394 — Thursday, March 5, 2026 — Thursday, March 5, 2026 (dayOffset 394)*

Your calendar runs in therapy appointments and preschool pickup times.

The case's calendar runs toward Monday, May 4, 2026 — fifteen months after the twins' placement on Tuesday, February 4, 2025. Your lawyer says a federal filing timeline arrives that day. It does not arrive for 'the twins.' It arrives for Maya, and separately, for Milo.

**Choices:**
- Go to the month-13 review and listen for each name, separately → **review13**
  - NOTE (shown after choosing): Listen for two names. The file has started saying them separately. Your strategy should too.

## [review13] The Review Where the Names Split
*Day 400 — Wednesday, March 11, 2026 — Wednesday, March 11, 2026 (dayOffset 400)*

The worker's report is honest and split down the middle. Maya: 'substantial progress toward return.' Milo: 'continued placement recommended; treatment ongoing.'

Then the agency's lawyer names the federal date — Monday, May 4, 2026 — for the record, for both children, in one breath. Nobody explains that the exceptions to that date can be different for each twin. Your lawyer, in the hallway, promises to.

**Choices:**
- Catch your lawyer and ask what the date does to each twin → **lawyer_map**  _(HIDDEN + Court report — Maya 'substantial'; Milo 'continued placement' (month 13))_
  - NOTE (shown after choosing): Ms. Whitaker draws two lines this time, not one.

## [lawyer_map] Two Lines on the Whiteboard
*Day 407 — Wednesday, March 18, 2026 — Wednesday, March 18, 2026 (dayOffset 407)*

Ms. Whitaker draws two lines, one for each twin, both ending at the same date: Monday, May 4, 2026.

"At fifteen of the most recent twenty-two months, the law tells the agency: file a petition to terminate parental rights — for that child — unless an exception is documented for that child." (42 U.S.C. § 675(5)(E)) "The exceptions are the same three for each: the child is being cared for by a relative; the file documents a compelling reason that filing would not be in that child's best interest; or the agency did not provide services the plan said were necessary for that child to come home safely."

"Maya's best door and Milo's best door may not be the same door," she says. "So we do not build one record. We build two, in one folder, with their names on the tabs."

**Choices:**
- Start with the house both records stand on → **housing_flat**
  - NOTE (shown after choosing): Two tabs go into the folder that night: MAYA and MILO, in the darkest marker.

## [housing_flat] The Apartment Check
*Day 412 — Monday, March 23, 2026 — Monday, March 23, 2026 (dayOffset 412)*

Your apartment passed its first look in the fall. The agency wants a second visit now that return is being discussed for Maya — beds, locks, the therapy corner Milo's team described for home practice.

A passed check is a fact. Whether it is a fact in the file depends on paper.

**Choices:**
- Ask for the signed check sheet, dated, one copy for each twin's tab → **maya_preschool**  _(FLAG: housingLetter; HIDDEN + Housing — second check passed, signed and dated)_
  - NOTE (shown after choosing): She signs it at your table. Facts are easy to give to people who ask calmly, with a folder.
- Take the verbal 'looks good' and save the awkwardness → **maya_preschool**  _(HIDDEN + Housing — second check passed verbally; no sheet in file)_
  - NOTE (shown after choosing): 'Looks good,' you tell Ms. Whitaker. She underlines it once, the way you underline a word you are not sure is spelled right.

## [maya_preschool] Maya's Teacher
*Day 418 — Sunday, March 29, 2026 — Sunday, March 29, 2026 (dayOffset 418)*

Maya's preschool teacher stops you at pickup from the Saturday visit's end — Maya has been telling her class about 'going home to Mom's house,' in the present tense, the way four-year-olds file their hopes.

The teacher offers, unprompted, to write what she sees: Maya's readiness, her talk of home, her settled weeks. An offer of paper is a doorbell. Someone still has to answer it.

**Choices:**
- Answer it — ask her to write it, dated, for Maya's tab → **milo_therapy**  _(cash −10; FLAG: mayaDoc; HIDDEN + Maya — preschool letter: readiness and settled weeks, documented)_
  - NOTE (shown after choosing): Two pages, on school letterhead. Maya's tab gets its first thick week.
- Thank her warmly and let the offer ride on the feeling → **milo_therapy**  _(HIDDEN + Maya — teacher offered a letter; none requested, none in file)_
  - NOTE (shown after choosing): The feeling is real. Feelings, in June, will need exhibits.

## [milo_therapy] Milo's Team
*Day 424 — Saturday, April 4, 2026 — Saturday, April 4, 2026 (dayOffset 424)*

Milo's therapy room has a small table, a patient speech therapist named Priya, and a chart where his new sounds arrive one at a time, like shy guests.

Priya can describe his timeline precisely: what he has gained, what the next months of treatment are for, why stopping or moving his care mid-course would cost him ground. Said in the room, it is expertise. Written, dated, and filed, it is something else: a reason, documented, with a name under it.

**Choices:**
- Ask Priya for the timeline in writing — gains, next steps, why continuity matters → **provider_capacity**  _(cash −10; FLAG: miloTimeline; HIDDEN + Milo — provider timeline letter: mid-treatment, continuity documented)_
  - NOTE (shown after choosing): She says yes the way professionals do when a parent finally asks the useful question.
- Take the verbal update — she is busy, and he is progressing → **provider_capacity**  _(HIDDEN + Milo — provider timeline given verbally only)_
  - NOTE (shown after choosing): 'Progressing, not finished,' you repeat in the car. The file, which cannot hear you, records nothing.

## [provider_capacity] The Waiting List Behind the Therapist
*Day 430 — Friday, April 10, 2026 — Friday, April 10, 2026 (dayOffset 430)*

At the front desk you learn the part no one controls: Priya's clinic has a waiting list of months, and Milo's twice-weekly slots — the ones his progress is built on — took most of a year to get.

If his care moved, the slots would not move with him automatically. That is not anyone's cruelty. It is capacity, and capacity is a fact a court can only weigh if somebody writes it down.

**Choices:**
- Ask the desk for the waitlist fact in writing, for Milo's tab → **twin_time**  _(HIDDEN + Milo — clinic capacity and waitlist documented)_
  - NOTE (shown after choosing): One printed page. The least sentimental document in the folder, and one of the strongest.
- Note it yourself in your notebook and move on → **twin_time**
  - NOTE (shown after choosing): Your notebook is true. It is also, in the eyes of a file, a diary — read by no one with a stamp.

## [twin_time] Both of Them, Asleep
*Day 436 — Thursday, April 16, 2026 — Thursday, April 16, 2026 (dayOffset 436)*

Saturday's visit ends at the foster home with both twins asleep in the car seats of your imagination — in reality, on the couch, mid-cartoon, Maya's head on Milo's shoulder.

The foster mother, Mrs. Adeyemi, is kind and tired in equal measure. She tells you the truth she is allowed to tell: 'Whatever the court does, I hope it does it one child at a time. They are not a set.'

It is the wisest sentence in your case so far, and she is not even a party to it.

**Choices:**
- Write her sentence at the top of the folder, and work the last weeks like a job → **visits**
  - NOTE (shown after choosing): One child at a time. That becomes the folder's whole method.

## [visits] The Canceled Session
*Day 439 — Sunday, April 19, 2026 — Sunday, April 19, 2026 (dayOffset 439)*

Milo's Thursday therapy-observation visit — the one you attend to learn his home program — is canceled: the clinic's boiler, of all things. It is the second cancellation this spring.

A make-up has never been offered. It has also never been requested in writing, where a request, and any gap that follows it, become facts the file must carry.

**Choices:**
- Text the worker, politely and in writing, asking for a make-up date → **kinship_aunt**  _(FLAG: makeupAsked; HIDDEN + Visit log — therapy observation canceled #2; make-up requested in writing)_
  - NOTE (shown after choosing): She replies Monday: she will check. The text exists either way.
- Absorb it — boilers fail, and goodwill matters → **kinship_aunt**  _(HIDDEN + Visit log — cancellation #2; no make-up; no request on record)_
  - NOTE (shown after choosing): Goodwill does matter. So does the log. They will sit in the same file, unintroduced.

## [kinship_aunt] Aunt Rosa's Spare Room
*Day 441 — Tuesday, April 21, 2026 — Tuesday, April 21, 2026 (dayOffset 441)*

Your sister Rosa — the twins' aunt, twenty minutes away, the holiday house — has finished most of a kinship study the agency started in the winter, mostly with Milo in mind: her work-from-home schedule fits therapy runs in a way your shifts cannot, yet.

If Milo were cared for by Rosa, the first federal exception would not be an argument for him. It would be a description. But a study sitting unfinished in a drawer describes nothing.

**Choices:**
- Ask the agency to finish and file Rosa's study before the review → **aunt_weekend**  _(FLAG: miloKinship; HIDDEN + Milo — kinship study for aunt completed and filed)_
  - NOTE (shown after choosing): The worker agrees it is 'nearly done.' Nearly, filed, is done.
- Let the study wait — Rosa will always be there → **aunt_weekend**  _(HIDDEN + Milo — kinship study left unfinished)_
  - NOTE (shown after choosing): Rosa will be there. Whether her study is in the file on Monday, May 4, 2026 is a different question.

## [aunt_weekend] A Weekend at Rosa's
*Day 445 — Saturday, April 25, 2026 — Saturday, April 25, 2026 (dayOffset 445)*

The twins spend a Saturday at Rosa's under the current plan. Maya treats it as a holiday. Milo finds the quiet corner Rosa made for him and lines up her wooden spoons by size, content for an hour.

Rosa, washing dishes, says the thing relatives say in these cases and mean completely: 'However this goes, they will not lose me. Put that wherever it needs to go.'

Where it needs to go is a file. Everything in this system eventually comes down to where a true sentence is stored.

**Choices:**
- Get Rosa's sentence into a signed letter for both tabs → **work_shift**  _(cash −15; HIDDEN + Kinship — aunt's letter: ongoing presence for both twins)_
  - NOTE (shown after choosing): Signed at her kitchen table. The spoons stay lined up behind you like a small honor guard.

## [work_shift] Pay Stubs, Two Tabs
*Day 447 — Monday, April 27, 2026 — Monday, April 27, 2026 (dayOffset 447)*

Payday. The stubs go in the folder — and this time you sort the rest of the paper the way Ms. Whitaker taught you: everything that is about Maya in her tab, everything about Milo in his, and the shared things copied twice.

It feels fussy. It is, Ms. Whitaker says later, the whole ballgame: a file that answers two questions separately can be ruled on separately. A file that answers 'the twins' can only be ruled on as a set.

**Choices:**
- Do the week's paperwork twice-named, and then ask for the file itself → **records**
  - NOTE (shown after choosing): Two tabs. Two records. The request you are about to make is how you check that the agency's file looks the same.

## [records] Asking for the Whole File
*Day 448 — Tuesday, April 28, 2026 — Tuesday, April 28, 2026 (dayOffset 448)*

A parent may request their case record — it 'shall be released upon request' (55 Pa. Code § 3130.44(d)) — and at month fourteen, most of the twins' record was written by other people, in rooms you were not in.

The request is one page. What it buys is the chance to see, before Monday, May 4, 2026, what the agency's own pages say about each child — including the pages about services for each of them.

**Choices:**
- Sign and send the request this week → **reveal**  _(FLAG: recordsRequested)_
  - NOTE (shown after choosing): A stamp, a date, a copy for the folder. The cheapest power in this system, exercised in time.
- Let it ride — your lawyer has the court reports → **no_reveal**
  - NOTE (shown after choosing): Court reports are summaries. You have been taught what summaries leave out. The lesson and the choice sit together anyway.

## [reveal] The Two Unsent Referrals
*Day 451 — Friday, May 1, 2026 — Friday, May 1, 2026 (dayOffset 451)*

The packet arrives. Maya's pages are strong. Milo's are strong too — until the services page, where two boxes wait like held breaths.

Milo's second therapy referral — the added session his plan called necessary — reads 'to be sent,' dated month five, with no send date after it. And Maya's childcare support referral, the one meant to cover your shift hours after return, sits in the same handwriting: identified, necessary, unsent.

The plan promised each twin a service. For each twin, a piece of it never left the building. You read the pages twice, once per child, the way the folder taught you.

**Choices:**
- Take both pages to Ms. Whitaker, one name at a time → **folder_night**  _(FLAG: referralSeen; HIDDEN + Service plan — Milo therapy referral and Maya childcare referral marked 'to be sent,' never sent)_
  - NOTE (shown after choosing): 'Don't be angry in May,' she says. 'Be documented in May. Anger fades. These testify — separately.'

## [no_reveal] What Summaries Leave Out
*Day 451 — Friday, May 1, 2026 — Friday, May 1, 2026 (dayOffset 451)*

Without the file, you have the court reports: fair, warm, and summary-length. Maya substantial. Milo progressing. Housing passed. One barrier language for two different children.

What you do not have is the services page. Whatever is or is not on it will be in the room on Monday, May 4, 2026 whether you have read it or not — the judge will have. Surprises in this system are just facts you met late.

**Choices:**
- Build what you can from your own folder, and name the gap honestly → **folder_night**
  - NOTE (shown after choosing): Your folder is real. It is also, through no fault of yours, missing the agency's own handwriting.

## [folder_night] The Night Before Strategy
*Day 452 — Saturday, May 2, 2026 — Saturday, May 2, 2026 (dayOffset 452)*

The folder lies open on your table: two tabs, two timelines, one date — Monday, May 4, 2026, two days from now, when the agency's filing duty is tested child by child.

Ms. Whitaker's whiteboard, photographed on your phone, holds the three doors for each twin: relative care, a documented compelling reason, services identified but not provided. Tomorrow you choose which doors to build, for which child, with the paper you actually have.

**Choices:**
- Go to Ms. Whitaker's office and choose, child by child → **strategy**
  - NOTE (shown after choosing): Court clothes are laid out. So are two tabs. Neither is an accident.

## [strategy] Choosing Doors, Child by Child
*Day 452 — Saturday, May 2, 2026 — Saturday, May 2, 2026 (dayOffset 452)*

Ms. Whitaker uncaps the marker. 'We lead with what the record can carry — per child.'

For Maya: readiness documented, housing documented — a return plan, or at minimum a documented compelling reason not to file while return is this close. For Milo: Rosa's filed study, Priya's timeline, the clinic's capacity page, and an unsent referral with his name on it. Or — for either child — nothing built at all, and the date left to speak alone.

**Choices:**
- Build the full per-child packet — Maya's return record and Milo's documents, together → **build_packet**  _(FLAG: packetBuilt)_
  - NOTE (shown after choosing): Two names, two packets, one filing. Paper that answers separately.
- Build the split plan — Maya's return, Milo placed with Rosa while treatment finishes → **build_split**  _(FLAG: splitPlanBuilt)_
  - NOTE (shown after choosing): The honest shape of your family right now, written down as a plan instead of an apology.
- Put the unsent referrals on the record — a short lawyer's letter, per child → **services_letter**  _(FLAG: servicesLetter)_
  - NOTE (shown after choosing): Short, dated, factual. Let the file correct itself out loud, twice.
- Keep your head down — progress should speak for itself → **thin_path**
  - NOTE (shown after choosing): Progress speaks in summaries. Monday, May 4, 2026 will be conducted in documents.

## [build_packet] The Packet, in Two Tabs
*Day 453 — Sunday, May 3, 2026 — Sunday, May 3, 2026 (dayOffset 453)*

It assembles on the conference table in two stacks. Maya's: the teacher's letter, the signed housing sheet, therapy-corner photographs, your stubs. Milo's: Priya's timeline, the capacity page, Rosa's study and letter, the services page with its empty box.

Ms. Whitaker drafts the ask the same way for each child and differently in substance: for Maya, return — or a documented compelling reason while return is arranged; for Milo, a documented compelling reason grounded in mid-treatment continuity, with Rosa as his relative placement if the court prefers a description to an argument.

The packet goes to the agency and the court early, so the hearing is a discussion and not an ambush.

**Choices:**
- File the packet and go to the fifteen-month review → **review_packet**
  - NOTE (shown after choosing): Two stacks go into one envelope. The envelope is the last thing in this case that treats them as a set.

## [build_split] The Split Plan, Written Plainly
*Day 453 — Sunday, May 3, 2026 — Sunday, May 3, 2026 (dayOffset 453)*

The split plan says out loud what everyone in the case already knows and no one had written: Maya is ready to come home; Milo is ready to be with family, and to finish a course of treatment that has a provider, a schedule, and an end that is not yet.

It proposes: Maya returns home on a trial basis; Milo is placed with Rosa, twenty minutes away, keeping Priya, keeping his slots, with sibling time built into the week and your home program continuing at Rosa's table and yours.

It is not the ending you pictured at placement. It is, Ms. Whitaker says, the plan the record can actually carry — for each child, separately, honestly.

**Choices:**
- File the split plan and go to the fifteen-month review → **review_split**
  - NOTE (shown after choosing): A plan that fits two different children. The court has not been offered one before.

## [services_letter] A Short Letter, Twice
*Day 453 — Sunday, May 3, 2026 — Sunday, May 3, 2026 (dayOffset 453)*

The letter is two pages — one per child — and Ms. Whitaker drafts it like it is already being read aloud by someone skeptical.

Page one: the plan identified a childcare referral as necessary for Maya's safe return; it was marked 'to be sent' in month five; it was never sent. Page two: the same handwriting, the same status, for the added therapy session Milo's plan called necessary. The letter asks the agency to confirm or correct each item before the review, and to provide each service now.

'We are not accusing anyone of villainy,' she says. 'Referrals fall through cracks in every office in America. We are establishing, per child, that a necessary service was identified and not provided. The law has a door shaped exactly like that fact — one per child.'

**Choices:**
- Sign it, send it, and go to the fifteen-month review → **review_services**
  - NOTE (shown after choosing): A letter in the file is a fact. Two letters are two facts, with two names on them.

## [thin_path] Head Down
*Day 453 — Sunday, May 3, 2026 — Sunday, May 3, 2026 (dayOffset 453)*

The last days are good days, taken singly. A visit that happens. Maya reading aloud. Milo's new sound, produced for you twice, proudly.

What does not happen: paper. No packet is filed, no letter is sent, Rosa's study — finished or not — is attached to nothing. The file that will be open on Monday, May 4, 2026 is the file as the system wrote it: warm summaries, one barrier, two children answered as a set, and a federal date arriving like weather.

**Choices:**
- Go to the fifteen-month review with your folder and your year → **review_thin**  _(HIDDEN + File — no per-child exception documentation as of month 15)_
  - NOTE (shown after choosing): The folder is real. Whether the court can use it depends on whether it becomes the court's paper too.

## [review_packet] The Fifteen-Month Review — The Packet
*Day 454 — Monday, May 4, 2026 — Monday, May 4, 2026 (dayOffset 454)*

Fifteen months. Monday, May 4, 2026 arrives wearing ordinary clothes: a courtroom, a flag by the door, two names called separately — because the packet taught the room to say them that way.

The judge has read both tabs. For Maya, she asks about the teacher's letter by date. For Milo, she asks Priya's timeline and the clinic's waitlist, and the agency does not dispute either page. The filing question is now two questions, and both of them have documents attached.

What remains is the shape of the answer — and for once, the record you built lets the court choose between two good shapes instead of one hard one.

**Choices:**
- Ask for both twins home — Maya's return, and Milo's treatment transferred to a home program with Priya's plan → **both_terms**
  - NOTE (shown after choosing): The packet is why this ask is a plan and not a hope: the transfer is written, staffed, and dated.
- Ask for the split — Maya home, Milo with Rosa while he finishes treatment → **split_terms**
  - NOTE (shown after choosing): The same record, the steadier shape. Rosa is twenty minutes away, and her study is already in the file.

## [review_split] The Fifteen-Month Review — The Split Plan
*Day 454 — Monday, May 4, 2026 — Monday, May 4, 2026 (dayOffset 454)*

The split plan is in the file before anyone speaks, which changes what speaking is for.

The agency, to its credit, does not pretend the twins are one question. Its lawyer addresses Maya's readiness and Milo's treatment in separate paragraphs. The judge asks Rosa one question — 'Can you keep Priya's schedule?' — and Rosa answers with a calendar she brought, because your family has learned what rooms like this run on.

For Milo, cared for by a relative, the filing duty does not attach the same way; for Maya, the return the record documents makes a petition a solution looking for a problem. The date passes through the room like weather through a house with the windows finally shut.

**Choices:**
- Accept the split — Maya home on trial terms, Milo to Rosa's with his treatment intact → **split_terms**
  - NOTE (shown after choosing): Not the picture from placement day. A picture each twin can actually live in.
- Ask whether Milo's home program could run from your home instead, with Rosa as daily support → **both_terms**
  - NOTE (shown after choosing): You ask with Priya's transfer plan in hand — the document is what makes the question fair to ask.

## [review_services] The Fifteen-Month Review — The Empty Boxes
*Day 454 — Monday, May 4, 2026 — Monday, May 4, 2026 (dayOffset 454)*

Ms. Whitaker's letter is in the file, and files, on dates like this, get read aloud by their consequences.

The agency does not contest the letter — for either child. Its own plan called each service necessary for that child's safe return; its own pages show each referral unsent. Its lawyer says the referrals have now been sent, both of them, and the agency is not prepared to say the plan was fully provided. Because it wasn't — twice, in the same handwriting.

The law's third exception exists for this exact shape of fact, and it exists per child. The judge's pen moves twice.

**Choices:**
- Listen to the pen, and to your own breathing, in that order → **deferred_terms**
  - NOTE (shown after choosing): Not a victory speech. Two entries, in two files, where the right people will find them at the next review.

## [review_thin] The Fifteen-Month Review — The Thin Record
*Day 454 — Monday, May 4, 2026 — Monday, May 4, 2026 (dayOffset 454)*

The review is short. The worker's summary is fair and even warm — and it answers the twins as a set, because no one ever gave the file a way to answer them separately.

Maya's readiness is a paragraph. Milo's treatment is a paragraph. Rosa is a sentence without a study attached. The unsent referrals are on a page nobody in the room has been given a reason to open.

The agency's lawyer rises and says the sentence the spring was always going to produce somewhere, and says it — the court notes — for both children: the agency will file.

**Choices:**
- Look at the twins' photograph on the folder, and then at your lawyer → **filed_next**
  - NOTE (shown after choosing): Ms. Whitaker is already writing. Filing, you are about to learn, is a door too — a harder one, with its own clocks, per child.

## [both_terms] Trial Terms, Two Names
*Day 459 — Saturday, May 9, 2026 — Saturday, May 9, 2026 (dayOffset 459)*

The order that comes back is written the way your folder was: two names, two sets of terms.

Maya's return is a trial with supervision and the childcare support — referred at last — under it. Milo's is a trial built around Priya's transfer plan: his sessions continue, his home program runs at your table daily, Rosa covers the hours your shifts cannot, and the court sets a short review to read his progress in the provider's own words.

It is not a closing. It is a beginning with paperwork — the only kind this system has ever honestly offered you.

**Choices:**
- Take both children home past the foster home's door, slowly, with the car seats checked twice → **end_both_home**  _(cash −20)_
  - NOTE (shown after choosing): Mrs. Adeyemi sends their things in labeled bags, Maya's on top of Milo's, because even goodbyes in this house are organized per child.

## [split_terms] Two Addresses, One Family
*Day 459 — Saturday, May 9, 2026 — Saturday, May 9, 2026 (dayOffset 459)*

The order is split, and the split is written kindly because the record let it be: Maya returns home on trial terms. Milo is placed with Rosa — cared for by a relative, in the law's plain words — with Priya's treatment untouched, sibling time four days a week, and your home program running at both kitchen tables.

The case stays open for both children. The goals are written separately now, and so, for the first time, are the next reviews: Maya's on her school and home progress, Milo's on his treatment chart and the question of his own return, in his own time.

**Choices:**
- Drive Maya home, then drive to Rosa's for Milo's dinner, twenty minutes each way → **end_split**  _(cash −20)_
  - NOTE (shown after choosing): Twenty minutes. You will make this drive so often it becomes a road the twins know by its turns.

## [deferred_terms] Documented, Twice
*Day 459 — Saturday, May 9, 2026 — Saturday, May 9, 2026 (dayOffset 459)*

What the court enters is not a return and not a filing. It is, per child, a documented reason the petitions are not filed now — for Maya and for Milo, the agency's own record shows services the plan called necessary were not provided, and both referrals now carry dates, owners, and a next review to answer to.

The twins remain placed, together, with Mrs. Adeyemi for now. Your case continues. What changed is who owes the next documents, and that, in this system, is not a small change.

**Choices:**
- Go home and put the new dates on both calendars — yours, and the case's → **end_deferred**
  - NOTE (shown after choosing): Time, in writing, twice. What you and the agency each do with it decides the next date.

## [filed_next] After the Filing Sentence
*Day 457 — Thursday, May 7, 2026 — Thursday, May 7, 2026 (dayOffset 457)*

Ms. Whitaker's hallway voice is steady. 'Filed is not terminated. For either child.'

A petition starts a separate hearing, months away, at which the agency would have to prove its grounds for that child by clear and convincing evidence — with counsel beside you, and the whole record, including the services page nobody opened in time, available to be built on now.

The work is not over. It has changed rooms, and it is still — it will always be — two cases with two names.

**Choices:**
- Start the new folder that night: two tabs, again → **end_filed**
  - NOTE (shown after choosing): The darkest marker comes out. MAYA. MILO. The record is still being written.

## [end_both_home] Ending — Both Home, at Different Speeds
*Day 466 — Saturday, May 16, 2026 — Saturday, May 16, 2026 (dayOffset 466)*

**Ending.**

**Debrief:**
- THE BOARD, MAPPED — ASFA CLOCK: The fifteen-month date, Monday, May 4, 2026, was met with a per-child record, so no petition was filed for either twin; the filing duty was answered with documents, not undergone. MAYA'S CLOCK: her readiness ran ahead of the case — preschool documentation and a passed, signed housing record let her return on trial terms at this review. MILO'S CLOCK: his treatment ran on Priya's timeline, not the court's — what the record carried was a written transfer plan (provider, schedule, home program, Rosa's hours), so his care moved home without losing the slots that took most of a year to get. REVIEW CLOCK: a short review is set to read Milo's progress in his provider's words and Maya's progress at home; the case remains open and supervised for both.
- WHAT THE RECORD SHOWED: Two tabs. Maya's held a teacher's letter and a signed housing sheet; Milo's held a provider timeline, a clinic capacity page, and Rosa's filed study and letter; both held your pay stubs and visit history. The court could rule separately because the file finally answered separately. Your records request (55 Pa. Code § 3130.44(d)) mattered the way it matters everywhere in this system: you negotiated the date knowing what the file said.
- THE LAW UNDER THIS PATH: At 15 of the most recent 22 months in foster care, the agency must file or join a petition to terminate parental rights for a child — unless an exception applies for that child (42 U.S.C. § 675(5)(E)): the child is being cared for by a relative; the agency has documented in the case plan a compelling reason that filing would not be in the child's best interest; or the agency has not provided the services the plan identified as necessary for the child's safe return. The analysis runs child by child. Had a petition been filed for either twin, the agency would still have had to prove statutory grounds by clear and convincing evidence at a separate hearing.
- WHAT WAS NEVER IN YOUR CONTROL: Priya's clinic capacity and its waiting list; whether a boiler canceled a session; a worker's caseload and summary habits; the judge assigned and the agency's posture on the day. Another mother, identical in effort, with a provider who would not write or a relative twenty minutes farther away, reaches a different ending here. Outcomes in these cases turn on workers, judges, provider capacity, and luck as well as on parents — this ending is the system's best one for your family, and it is a trial, not a closing: supervision continues, and Milo's treatment will finish, or not, on his own body's schedule.

## [end_split] Ending — Split Outcome: One Home, One With Family
*Day 466 — Saturday, May 16, 2026 — Saturday, May 16, 2026 (dayOffset 466)*

**Ending.**

**Debrief:**
- THE BOARD, MAPPED — ASFA CLOCK: The fifteen-month date, Monday, May 4, 2026, passed without a petition for either child, but by two different doors. MAYA'S CLOCK: she came home — her readiness was documented early enough that return, on trial terms with supervision, was the record's plain answer. MILO'S CLOCK: he did not come home, and the honesty of this ending is that home was not yet the right address for his care: he is placed with Rosa, keeps Priya and his twice-weekly slots, and his return question is set for his own later review, keyed to his treatment chart — a timeline measured in sounds gained, not in court dates. REVIEW CLOCK: the twins now have separate reviews, separate goals, and a sibling-time schedule that runs four days a week between two kitchen tables twenty minutes apart.
- WHAT THE RECORD SHOWED: A split plan, filed before the review, that named each child's facts separately — Maya's teacher letter and housing sheet; Milo's provider timeline, the clinic capacity page, Rosa's completed study and her letter. For Milo, being cared for by a relative is the first exception in the statute's own words; for Maya, return made a petition unnecessary in practice. Split outcomes are a real outcome in the published record: courts assess each child individually, and siblings in the same case regularly end a review with different goals, different placements, and different clocks.
- THE LAW UNDER THIS PATH: At 15 of the most recent 22 months in foster care, the agency must file or join a petition to terminate parental rights for a child — unless an exception applies for that child (42 U.S.C. § 675(5)(E)): the child is being cared for by a relative; the agency has documented in the case plan a compelling reason that filing would not be in the child's best interest; or the agency has not provided the services the plan identified as necessary for the child's safe return. The analysis runs child by child. Had a petition been filed for either twin, the agency would still have had to prove statutory grounds by clear and convincing evidence at a separate hearing.
- WHAT WAS NEVER IN YOUR CONTROL: The pace of Milo's development and treatment — no filing, letter, or effort by you could make his therapy finish by a federal date; Priya's capacity; Rosa's availability and study timeline; the judge and the worker on the day. A split outcome is not a verdict on your worth as a mother, and it is not a final one: Milo's goal remains return, his case remains open, and the same record-keeping that produced this ending is what his return will be built from. Outcomes turn on workers, judges, treatment timelines, and luck as well as on parents.

## [end_deferred] Ending — Filing Deferred, for Both, on Paper
*Day 463 — Wednesday, May 13, 2026 — Wednesday, May 13, 2026 (dayOffset 463)*

**Ending.**

**Debrief:**
- THE BOARD, MAPPED — ASFA CLOCK: The fifteen-month date, Monday, May 4, 2026, came and went with no petition filed for either twin — deferred, not forbidden forever. MAYA'S CLOCK: her return waits behind a service that now, finally, has a send date — the childcare referral her plan called necessary in month five was sent at month fifteen, and her next review will ask whether it arrived in time to matter. MILO'S CLOCK: the same story in his tab — his added therapy session, identified as necessary and never sent, is now referred, and his treatment continues with Priya uninterrupted in the meantime. REVIEW CLOCK: both children remain placed together for now; the next review is set with the agency's own commitments attached to it, per child, with dates.
- WHAT THE RECORD SHOWED: The agency's own services pages — two referrals, two names, marked 'to be sent' and never sent — placed on the record by a short, dated lawyer's letter before the review, after your records request (55 Pa. Code § 3130.44(d)) surfaced them while there was still time to use them. Nothing about your effort changed in the last two weeks. What changed was whose gaps were documented, and when.
- THE LAW UNDER THIS PATH: At 15 of the most recent 22 months in foster care, the agency must file or join a petition to terminate parental rights for a child — unless an exception applies for that child (42 U.S.C. § 675(5)(E)): the child is being cared for by a relative; the agency has documented in the case plan a compelling reason that filing would not be in the child's best interest; or the agency has not provided the services the plan identified as necessary for the child's safe return. The analysis runs child by child. Had a petition been filed for either twin, the agency would still have had to prove statutory grounds by clear and convincing evidence at a separate hearing.
- WHAT WAS NEVER IN YOUR CONTROL: That the referrals sat unsent for ten months in the first place; the caseload that buried them; whether the programs they point to have openings when they finally arrive; the judge and the agency's candor on the day — another agency contests the same letter, and another spring ends in a filing. A deferral is a reprieve with homework, for you and for the agency alike. Outcomes turn on workers, judges, and luck as well as on parents; what your choices changed was that the homework, this time, is written down for both sides.

## [end_filed] Ending — Filing Proceeds, for Both
*Day 460 — Sunday, May 10, 2026 — Sunday, May 10, 2026 (dayOffset 460)*

**Ending.**

**Debrief:**
- THE BOARD, MAPPED — ASFA CLOCK: The fifteen-month date, Monday, May 4, 2026, arrived with no per-child exception documented, and the agency filed — or announced it will file — petitions as to both twins. MAYA'S CLOCK: her readiness was real and remains real, but it existed in the world more than in the file: a teacher's offer never turned into a letter decides less than a paragraph in a summary. MILO'S CLOCK: his mid-treatment facts — the strongest documented reason in the case — were mostly spoken in rooms, and Rosa's study was attached to nothing, so the relative door was never actually in front of the court. REVIEW CLOCK: the dependency case continues, and a separate termination track now opens, with its own hearing months away, per child.
- WHAT THE RECORD SHOWED: Warm summaries that answered the twins as a set; strong spoken facts that were never converted into filed paper; and — on a services page no one requested in time — referrals for each child marked 'to be sent' and never sent, which may yet be the strongest documents in either child's hearing. The date was not decided by your worth or even your progress. It was decided by which facts existed in the court's paper, per child, by Monday, May 4, 2026.
- THE LAW UNDER THIS PATH: At 15 of the most recent 22 months in foster care, the agency must file or join a petition to terminate parental rights for a child — unless an exception applies for that child (42 U.S.C. § 675(5)(E)): the child is being cared for by a relative; the agency has documented in the case plan a compelling reason that filing would not be in the child's best interest; or the agency has not provided the services the plan identified as necessary for the child's safe return. The analysis runs child by child. Had a petition been filed for either twin, the agency would still have had to prove statutory grounds by clear and convincing evidence at a separate hearing.
- WHAT WAS NEVER IN YOUR CONTROL: The unsent referrals; a provider's writing habits; a study that moved at an office's pace; the judge, the worker, and the agency's posture. The same mother, with a checked referral or a filed study, lands in a different ending — as the same mother reached this one. And filed is not terminated: at the hearing to come, the agency must prove its grounds for each child by clear and convincing evidence, with your counsel beside you and the whole record — including the page nobody opened in time — finally buildable. Outcomes turn on workers, judges, and luck as well as on parents. The record, per child, is still being written.
