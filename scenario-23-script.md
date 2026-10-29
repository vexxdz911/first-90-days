# THE FIRST 90 DAYS — Scenario 23: “The Hospital Hold”

*Human-readable script. This document and `scenario-23.json` are generated from a single source and match node-for-node: same IDs, same order, same choices, same effects.*

**The family is fictional — a composite. No real person's story appears here.**

**Content note:** This scenario depicts a newborn's first weeks — a hospital discharge decision, an agency investigation touching an older sibling, and a shelter care hearing — told through procedure and paperwork. There is no graphic content. Players may skip any scene or use the quick exit at any time.

**How to read effects:** `cash −40` changes the player's cash. `FLAG: name` sets a flag the engine tracks. `HIDDEN + item` means the case file quietly records that item at this choice — the player does not see it when it happens. `NOTE:` is text shown to the player right after choosing.

Start date: Monday, January 12, 2026 (the birth day). Day offsets are days since that date. On the court track, custody is taken on Day 0 and the shelter care hearing falls on Day 3 — Thursday, January 15, 2026 — exactly 72 hours later.

## [birth] Born on a Monday
*Day 0 — Monday, January 12, 2026 — Monday, January 12, 2026 (dayOffset 0)*

Your daughter is born in the early hours of Monday, January 12, 2026, small and loud and immediately the most important paperwork-generating person you have ever met. You name her Wren.

Your older child, June, is five, safe, and asleep at your mother Rosa's house, where she has been staying while you were in the hospital — her own bed there, her school two blocks away, her grandmother's rules posted on the fridge in marker.

Two children, two addresses, one mother. By tonight, three separate groups of people — a hospital, an agency, and possibly a court — will each be keeping a file about how today went.

**Choices:**
- Hold Wren, and meet the day one form at a time → **hospital_worker**
  - NOTE (shown after choosing): The day will have forms. Some of them will matter more than they look.

## [hospital_worker] The Hospital Social Worker
*Day 0 — Monday, January 12, 2026 — Monday, January 12, 2026 (dayOffset 0)*

Wren needs a few days of monitored care after being exposed to substances before birth — that is the whole medical sentence anyone gives you today, and it is enough to work with.

A hospital social worker, Ms. Park, explains the procedure in the plain order it will happen: the hospital has made a report to the county children and youth agency, as it does in cases like this; an agency worker will come to talk with you today; and discharge — yours and Wren's — will involve the agency's view, not only the doctors'.

She is kind, and she is also a person who writes things down. Both facts are worth knowing before the next knock.

**Choices:**
- Ask her what will be written down today, and by whom → **first_paper**
  - NOTE (shown after choosing): She answers readily. People in this system are often most helpful when asked precise, paper-shaped questions.

## [first_paper] The First Paperwork
*Day 0 — Monday, January 12, 2026 — Monday, January 12, 2026 (dayOffset 0)*

The agency worker, Mr. Osei, arrives with a folder and a plan he describes out loud: June is safe at Rosa's — no one disputes that today — and for Wren, he wants either a written safety plan naming Rosa as the discharge caregiver with you, or, if there is no plan he can approve, he will ask a court for temporary custody while things are assessed.

He has forms for both roads. Rosa is twenty minutes away and already on her way. What happens in the next hour — what gets signed, what gets asked for in writing, whose name is on which page — will decide which road today takes.

**Choices:**
- Ask for copies of everything, and get Rosa's discharge plan in writing, signed, before anything else is signed → **plan_check**  _(FLAG: planWritten; HIDDEN + Hospital — written discharge/safety plan naming grandmother, signed day 0)_
  - NOTE (shown after choosing): Mr. Osei, to his credit, slows down. Paper appears. Rosa's name goes on it in ink, not just in the air.
- Sign the forms as they are handed to you — the fastest way to be seen as cooperative → **court_order**  _(FLAG: removed; HIDDEN + Hospital — forms signed as handed; no written plan requested)_
  - NOTE (shown after choosing): The signing takes four minutes. Its consequences will be measured in hearings.
- Ask questions and talk it through warmly, but leave the paperwork to the professionals → **court_order**  _(FLAG: removed; HIDDEN + Hospital — discussion held; no written plan produced)_
  - NOTE (shown after choosing): The conversation is warm. Warmth, unwritten, is hard for a court to weigh three days from now.

## [plan_check] The Plan, Checked
*Day 1 — Tuesday, January 13, 2026 — Tuesday, January 13, 2026 (dayOffset 1)*

Because the plan exists on paper, the agency's next step is to check it, not to replace it. Mr. Osei visits Rosa's house on Tuesday, January 13, 2026: June's bed, June's school records on the fridge under the rules, Wren's bassinet already assembled by a grandmother who does not wait for permission to prepare.

You are still in the hospital with Wren. Your discharge is expected tomorrow; hers depends on her monitored days finishing and on this plan holding.

**Choices:**
- Ask Mr. Osei to note, in writing, that June's placement with Rosa predates today and is stable → **grandma_home_plan**  _(HIDDEN + Agency note — older child stable with grandmother, pre-existing arrangement)_
  - NOTE (shown after choosing): He writes it while you are on speakerphone. A sentence in a file is a small, load-bearing thing.

## [grandma_home_plan] June's House, For Now
*Day 1 — Tuesday, January 13, 2026 — Tuesday, January 13, 2026 (dayOffset 1)*

Rosa's house runs on posted rules and early dinners. June shows Mr. Osei her reading folder and asks whether the baby will 'live here or at Mom's,' with the directness of a five-year-old filing a permanency question.

'Both, at first,' Rosa says, 'which is what the paper says.' It is. Because you asked for the paper, the answer to June's question is a document, not a hope.

**Choices:**
- From your hospital bed, start the records habit — for both children → **records_plan**
  - NOTE (shown after choosing): One folder at Rosa's, one with you. Two children, kept in two names from the first week.

## [records_plan] Asking for the Records, Week One
*Day 2 — Wednesday, January 14, 2026 — Wednesday, January 14, 2026 (dayOffset 2)*

A parent may request their case record — it 'shall be released upon request' (55 Pa. Code § 3130.44(d)). In week one that means two requests, really: your hospital records for Wren's birth and monitored days, and the agency's record of today's investigation, including what it says about June.

Asking in the first week feels early. It is, in fact, the only time the file is still short enough to read in one sitting.

**Choices:**
- Sign and send both requests — hospital records and agency records → **reveal_plan**  _(FLAG: recordsRequested)_
  - NOTE (shown after choosing): Two stamps, two dates, copies for both folders. The cheapest power in this system, exercised while the file is still thin.
- Wait until things settle — asking now might look adversarial → **plan_week**
  - NOTE (shown after choosing): Settling is a real thing. So is a file growing a page a day without you reading any of them.

## [reveal_plan] What the First File Says
*Day 2 — Wednesday, January 14, 2026 — Wednesday, January 14, 2026 (dayOffset 2)*

The records come quickly, because week-one files are short. Wren's hospital pages are plain: monitored days, feeding improving, discharge tied to the plan. The agency's pages record the report, Mr. Osei's visit, Rosa's house — and one line you are glad to have seen now rather than later: June is described, accurately, as 'safe in a pre-existing kin arrangement; no concerns identified at this time.'

That sentence is June's whole case, if she is lucky: one accurate sentence, written early, that later questions have to argue with.

**Choices:**
- File both copies, one per child, and prepare for discharge day → **plan_week**  _(FLAG: juneSentenceSeen; HIDDEN + Agency record — 'no concerns identified' as to older child, seen by mother week one)_
  - NOTE (shown after choosing): You now know what the file says about each child. Most parents in this system are never told they may look.

## [plan_week] Discharge Day
*Day 4 — Friday, January 16, 2026 — Friday, January 16, 2026 (dayOffset 4)*

On Friday, January 16, 2026, Wren is discharged — not to you alone, but to the plan: you and Rosa together, in Rosa's house for the first stretch, with follow-up appointments listed on a sheet the hospital hands you and the agency has already copied.

June supervises the homecoming with a clipboard she made herself. Item one: baby home. She checks it in crayon.

A plan is not the end of a case. It is a case with its promises written down — which means the next visits will be about whether the paper and the house still match.

**Choices:**
- Keep every appointment sheet and hand Rosa a copy of each, the day it happens → **agency_home_visit**
  - NOTE (shown after choosing): Two folders, kept current. June's clipboard, you notice, has the same system.

## [agency_home_visit] The Home Visit, and June's Question
*Day 8 — Tuesday, January 20, 2026 — Tuesday, January 20, 2026 (dayOffset 8)*

Mr. Osei's first home visit goes the way the paper said it would — until it widens. He asks about June: her school, her doctor, who takes her when Rosa works. The questions are routine. They are also how a baby's case asks, politely, whether it should become a sibling's case too.

June's facts are good ones. Whether they enter the file as facts — a school letter, a doctor's note, dates — or stay as a grandmother's spoken answers is, as ever, a paperwork decision.

**Choices:**
- Give him June's school and doctor letters, in writing, for her own page in the file → **plan_review**  _(FLAG: juneRecord; HIDDEN + Older child — school and medical letters filed; status documented)_
  - NOTE (shown after choosing): He copies them into the folder in front of you. June's page now argues for itself.
- Answer everything verbally — Rosa knows June's life by heart → **plan_review_thin**  _(HIDDEN + Older child — status given verbally only; no documents filed)_
  - NOTE (shown after choosing): Rosa does know it by heart. Files, unfortunately, have no hearts — only pages.

## [plan_review] The Agency Review — Plan Track
*Day 11 — Friday, January 23, 2026 — Friday, January 23, 2026 (dayOffset 11)*

The agency's internal review on Friday, January 23, 2026 reads a short file with its promises kept: the plan followed, appointments kept and sheeted, Wren gaining, June documented and unbothered by any of it.

Mr. Osei tells you the shape of the close: the plan continues a short while longer under agency oversight, then steps down. No court was ever asked to hold your daughter, so no court has to be asked to give her back. That sentence is the whole dividend of day zero's paper.

**Choices:**
- Ask for the step-down in writing, with its date → **plan_home_terms**
  - NOTE (shown after choosing): A date, in writing. Your family has learned to collect them.

## [plan_review_thin] The Agency Review — The Thin Page
*Day 11 — Friday, January 23, 2026 — Friday, January 23, 2026 (dayOffset 11)*

The review on Friday, January 23, 2026 goes well for Wren — her plan is kept, her sheets are filed — and less cleanly for June, whose page is thin: good answers, no documents.

The agency does not open a case on June. It does something quieter: it asks a court to oversee the plan for a short period rather than closing it, with Wren placed with Rosa in the meantime on paper — because oversight, unlike trust, is something this system knows how to file.

It is not a disaster. It is a longer road than the one your folder could have built, and June will now have appointments of her own to be measured by.

**Choices:**
- Accept the short oversight period, and start building June's paper now → **plan_short_terms**
  - NOTE (shown after choosing): Late paper is still paper. The next review will read whatever you file between now and then.

## [plan_home_terms] Step-Down, Dated
*Day 14 — Monday, January 26, 2026 — Monday, January 26, 2026 (dayOffset 14)*

The step-down letter arrives dated Monday, January 26, 2026: oversight ends on the date named, the plan becomes simply your family's arrangement, and Wren's file closes with June's sentence — 'no concerns identified' — still its last word about her.

June moves her clipboard to the fridge, next to Rosa's rules. Item two, in crayon: done.

**Choices:**
- Take Wren home, past Rosa's door, with June holding the discharge sheet like a flag → **end_home**  _(cash −15)_
  - NOTE (shown after choosing): Rosa keeps the bassinet, just in case. Grandmothers in this system keep everything, just in case.

## [plan_short_terms] Oversight, With an End Date
*Day 14 — Monday, January 26, 2026 — Monday, January 26, 2026 (dayOffset 14)*

The oversight order is short and dated: Wren stays with Rosa under the plan, you live there too and parent both children daily, June attends the check-ins the thin page earned her, and a review is set to close it all if the paper catches up to the life.

It will. The life was never the problem in this branch of the story. The paper was, and paper can be fixed in weeks in a way lives cannot.

**Choices:**
- Go to that review with two full folders → **end_shortterm**
  - NOTE (shown after choosing): This time, June's folder is as thick as her sister's. That is the whole lesson, arriving late and still counting.

## [court_order] The Court's Signature, Day Zero
*Day 0 — Monday, January 12, 2026 — Monday, January 12, 2026 (dayOffset 0)*

By the evening of Monday, January 12, 2026, a judge has signed an order giving the agency temporary custody of Wren. She does not move — her monitored days are in this hospital either way — but her legal address changes while she sleeps in a plastic bassinet.

Mr. Osei explains the next step with the order in his hand: there will be a hearing, soon, at which a court decides whether she stays in the agency's custody for now. He gives you the date, verbally, on his way out.

A date given verbally, about a hearing that decides where your newborn lives, is the system's way of telling you what the next three days are for.

**Choices:**
- Write the date down yourself, and ask the nurse for a copy of the order for your folder → **lawyer_court**  _(HIDDEN + Court — temporary custody order day 0; mother obtained a copy)_
  - NOTE (shown after choosing): The nurse copies it without fuss. Your folder starts the way all your folders should have: with the court's own paper in it.

## [lawyer_court] Your Lawyer, by Right
*Day 1 — Tuesday, January 13, 2026 — Tuesday, January 13, 2026 (dayOffset 1)*

You have the right to counsel in this case — and to appointed counsel if you cannot afford it (42 Pa.C.S. § 6337). Your lawyer, Ms. Ferreira, meets you at the hospital on Tuesday, January 13, 2026 with the order, a pen, and the first honest map of the week.

"The shelter care hearing is Thursday, January 15, 2026,” she says. “A child taken into custody gets that hearing within 72 hours (42 Pa.C.S. § 6332; 23 Pa.C.S. § 6315(d)). Wren was taken into custody on Monday, January 12, 2026, so the hearing falls on Thursday, January 15, 2026 — three days after, exactly. At it, the court decides where she waits while the case is sorted out. What the court can weigh is what is in front of it: Rosa, the plan that was or was not written, and whatever paper we build in the next two days."

Two days. She says it without drama, the way people state weather.

**Choices:**
- Spend the two days building — Rosa's plan, in writing, for the hearing → **grandma_sibling_court**  _(FLAG: hearingPlanBuilt)_
  - NOTE (shown after choosing): Rosa arrives with a folder of her own. Grandmothers and lawyers, properly aimed, are a formidable paperwork alliance.

## [grandma_sibling_court] Meanwhile, June
*Day 1 — Tuesday, January 13, 2026 — Tuesday, January 13, 2026 (dayOffset 1)*

While the court track runs, the agency track widens — to June. A second worker visits Rosa's house on Tuesday, January 13, 2026 to 'assess the sibling,' because a case opened on a newborn asks, by design, whether the other children in the family are safe where they are.

June is, visibly: fed, schooled, fridge-rules fluent. The worker's visit is short. What she writes about June will nonetheless be read at Wren's hearing, because files in this system travel between children more easily than children travel between houses.

**Choices:**
- Ask Rosa to give the worker June's school letter and doctor's note, in writing, that day → **records_court**  _(FLAG: juneRecord; HIDDEN + Older child — school/medical documents given to agency day 1)_
  - NOTE (shown after choosing): Rosa hands them over with the rules from the fridge still paper-clipped behind them. It is exactly the right exhibit.
- Let the visit speak for itself — June is obviously fine → **records_court**  _(HIDDEN + Older child — home visit verbal only)_
  - NOTE (shown after choosing): She is obviously fine. 'Obviously' is a word hearings are not built to weigh.

## [records_court] Asking for the Records, Before the Hearing
*Day 2 — Wednesday, January 14, 2026 — Wednesday, January 14, 2026 (dayOffset 2)*

There is one day left before the hearing on Thursday, January 15, 2026. A parent may request their case record — it 'shall be released upon request' (55 Pa. Code § 3130.44(d)) — and a two-day-old file is short enough to read tonight, hospital pages and agency pages both.

Ms. Ferreira approves with unusual warmth. 'Hearings are arguments about a file,' she says. 'I would like us to have read the file.'

**Choices:**
- Sign and send both requests today — hospital and agency records → **reveal_court**  _(FLAG: recordsRequested)_
  - NOTE (shown after choosing): Two stamps, two dates. Tomorrow's hearing will contain no sentence you have not already read.
- Spend the day on Rosa's plan instead — the file can wait until after the hearing → **hearing_prep**
  - NOTE (shown after choosing): The plan matters enormously. So does knowing whether the file agrees with it. The day holds one errand comfortably, and you have chosen.

## [reveal_court] Reading the File the Night Before
*Day 2 — Wednesday, January 14, 2026 — Wednesday, January 14, 2026 (dayOffset 2)*

The packet is thin and mostly fair: the hospital's plain pages, Mr. Osei's notes, the custody order. Two lines stand out to Ms. Ferreira's pen.

First: your request, at the hospital, to have Rosa named — recorded as 'mother states grandmother available,' with no plan attached because none was signed. Second, about June: 'sibling observed at grandmother's; school letter on file' — or, on the thinner version of this week, nothing about June at all.

'Tomorrow,' Ms. Ferreira says, 'we hand the court the plan that should have been attached to that first line. Late paper is weaker than early paper. It is much stronger than no paper.'

**Choices:**
- Go to the hearing with Rosa, the written plan, and the file you have read → **hearing_prep**  _(HIDDEN + Hearing preparation — file read in advance; no surprises)_
  - NOTE (shown after choosing): You will hear nothing tomorrow for the first time. That is a kind of strength nobody can take from you.

## [hearing_prep] The Night Before the Hearing
*Day 2 — Wednesday, January 14, 2026 — Wednesday, January 14, 2026 (dayOffset 2)*

Rosa lays out clothes for a five-year-old who is not attending and a grandmother who is. The written plan is in two folders now — Rosa's, and Ms. Ferreira's.

Tomorrow, Thursday, January 15, 2026, a judge will decide where a three-day-old baby waits while her case is sorted. The medicine will take one plain sentence. Everything else will be paper: whose house, whose name, what was written on day zero and what was written since.

**Choices:**
- Sleep what sleep is available, and go → **shelter_hearing**
  - NOTE (shown after choosing): June draws a picture for the baby 'for court.' It goes in the folder. Some exhibits are not evidence and still matter to the people carrying them.

## [shelter_hearing] The Shelter Care Hearing
*Day 3 — Thursday, January 15, 2026 — Thursday, January 15, 2026 (dayOffset 3)*

The hearing is on Thursday, January 15, 2026 — within 72 hours of Wren being taken into custody on Monday, January 12, 2026, as the law provides (42 Pa.C.S. § 6332; 23 Pa.C.S. § 6315(d)). It is shorter than you feared and more formal than you hoped: a judge, the agency's lawyer, Ms. Ferreira beside you, and Wren present only as a file and a bassinet photograph.

The hospital's part takes one plain sentence: Wren's monitored care is finishing and she is ready for discharge to an approved plan. Everything after that sentence is the question the week built: whose plan, on what paper, with what path home — and whether June's name belongs anywhere in the order.

**Choices:**
- Ask, through your lawyer, for Wren to be placed with Rosa — the written plan, the kin house, June already there → **placed_grandma**  _(FLAG: kinPlacement)_
  - NOTE (shown after choosing): Ms. Ferreira hands up the plan. The judge reads it the way judges read things that were written before they asked: slowly, and with weight.
- Ask for more time to get a plan together — you were not ready on day zero and everyone knows it → **placed_foster**
  - NOTE (shown after choosing): The judge is not unkind. Kindness, however, is not a placement. The agency's foster home, which is ready on paper, becomes the answer by default.

## [placed_grandma] Placed — With Family
*Day 3 — Thursday, January 15, 2026 — Thursday, January 15, 2026 (dayOffset 3)*

The court orders Wren to remain in the agency's custody for now, and placed with Rosa — discharged from the hospital to her grandmother's house, where June already lives, where you will stay and parent both girls daily under the plan.

It is not home. Your name is on the plan and not on the custody line, and the difference will be explained to you by every form you sign this month. But the road back is written into the order itself, with a review date on it.

June, informed by phone, adds an item to her clipboard: baby at Grandma's. Check.

**Choices:**
- Sign the order copy for your folder, and start the first placed week → **first_week_placed**
  - NOTE (shown after choosing): A dated path home is not home. It is also not nothing — it is, in this system, the main thing.

## [placed_foster] Placed — With Strangers, For Now
*Day 3 — Thursday, January 15, 2026 — Thursday, January 15, 2026 (dayOffset 3)*

The court continues Wren's custody with the agency, and she is discharged from the hospital to a foster home across the county — experienced people, a quiet house, and a forty-minute drive from Rosa's.

The order sets visits, and a review. It does not set a date for her to come home, because no plan was in front of the court from which a date could be written. Dates, you are learning, are manufactured from paper. There was not enough paper.

June asks where the baby went. Rosa answers honestly, at her size: 'To a safe house, while Mom does the paperwork.' June nods like a colleague.

**Choices:**
- Take the visit schedule in writing, and start building the paper that was missing → **first_week_placed**  _(HIDDEN + Placement — foster (non-kin) after shelter care; no plan presented)_
  - NOTE (shown after choosing): The foster mother's name and the visit days go in the folder in the darkest marker. Building starts now, later than it should have, which is still a start.

## [first_week_placed] The First Placed Week
*Day 5 — Saturday, January 17, 2026 — Saturday, January 17, 2026 (dayOffset 5)*

The first placed week runs on visits and intake appointments. You feed Wren in someone else's kitchen, or in Rosa's, depending on which road the hearing took — and in both houses, the same truth applies: the case now measures you in kept appointments and filed paper.

Your treatment intake — the assessment the plan calls for — is offered twice this week, at two times, one of which collides with a visit. Systems schedule collisions like this constantly. How a collision is handled, and whether it is documented, becomes part of the file.

**Choices:**
- Go to the intake, and ask for the attendance record and the plan in writing before you leave → **treatment_intake**  _(cash −15; FLAG: treatmentDoc; HIDDEN + Treatment — intake attended; attendance and plan documented)_
  - NOTE (shown after choosing): One page, stamped. The file's version of you gets a good week, because the week was documented being good.
- Go to the intake, do the work, and let the program report it in its own time → **treatment_intake**  _(HIDDEN + Treatment — intake attended; documentation left to the program)_
  - NOTE (shown after choosing): The work is real either way. One version of it will be in the file by the review. The other will be a phone call someone may or may not make.
- Choose the visit over the intake — Wren is days old, and the intake can surely move → **thin_week**
  - NOTE (shown after choosing): It can move. On paper, unmoved and unexcused, it will read as something else entirely — and no one will call to ask which it was.

## [treatment_intake] Paper From the Program
*Day 8 — Tuesday, January 20, 2026 — Tuesday, January 20, 2026 (dayOffset 8)*

Intake done, the program gives you its plan: sessions, screens, a parenting group that meets in a church basement with good coffee. Your part is attendance. The file's part is whether attendance becomes paper.

Meanwhile the agency's attention, having started with a newborn, does what it was designed to do: it checks the whole house the newborn belongs to. June's name comes up at your next meeting — not as an accusation, but as a question the case now intends to answer on paper.

**Choices:**
- Ask what, exactly, the agency wants to know about June — and ask for the question in writing → **sibling_question**
  - NOTE (shown after choosing): Precise questions get precise answers. Vague worry gets services, indefinitely, for a five-year-old who was never the concern.

## [sibling_question] Does the Baby's Case Reach June?
*Day 10 — Thursday, January 22, 2026 — Thursday, January 22, 2026 (dayOffset 10)*

The meeting on Thursday, January 22, 2026 is polite and pivotal. The agency proposes 'supportive services' for June — assessments, a parenting program keyed to her, regular checks — on the reasoning that the family is 'now involved.'

June's own facts have not changed since Monday, January 12, 2026: safe at Rosa's, school thriving, one accurate sentence in one file. What has changed is that a case exists next to her name, looking for somewhere to stand. Whether it stands on documents or on momentum is being decided at this table.

**Choices:**
- Hand over June's school and doctor letters and ask that her status be documented as it stands → **review_court_strong**  _(FLAG: juneRecord; HIDDEN + Older child — documented status presented; services declined on the record)_
  - NOTE (shown after choosing): Ms. Ferreira's sentence does the rest: 'Let the file show a reason, or let it show her record.' The worker looks at the letters for a long moment.
- Agree to the services — refusing help feels like the risky move → **sibling_services**  _(HIDDEN + Older child — services accepted without a documented basis)_
  - NOTE (shown after choosing): It feels cooperative. It also writes a new first sentence in June's file: 'family receiving services.' Sentences like that attract sequels.

## [sibling_services] June's Appointments
*Day 12 — Saturday, January 24, 2026 — Saturday, January 24, 2026 (dayOffset 12)*

June's services arrive as a calendar: an assessment across town, forms for Rosa, a worker who visits during school hours and must be explained to a teacher.

None of it is cruel, and June — resilient, fridge-rules fluent — takes it in stride. But her file now exists in a way it did not on Monday, January 12, 2026, with goals someone else wrote and a closing date no one has named. A case, once opened next to a child's name, closes on paper or not at all.

**Choices:**
- Go to the review and ask, with your lawyer, for June's services to be given an end date and a reason, in writing → **review_sibling**
  - NOTE (shown after choosing): You cannot un-open the file this month. You can insist it be a file with an ending — that, too, is record-building.

## [review_court_strong] The Review — A Dated Path
*Day 14 — Monday, January 26, 2026 — Monday, January 26, 2026 (dayOffset 14)*

At the review on Monday, January 26, 2026, the file is unusually legible: Wren placed with family or visited without a miss, intake attended and documented, a treatment plan with your attendance stamped into it, and June's page holding her own documents instead of the agency's momentum.

The court and the agency do what legible files make possible: they write dates. A step-down. A return, if the next weeks match these ones. June is not in the order at all, which is exactly where a child with her record belongs.

**Choices:**
- Ask for the dates in the order itself, not just in the minutes → **short_terms**
  - NOTE (shown after choosing): Dates in orders bind people. Dates in minutes merely describe them. You have learned to collect the binding kind.

## [review_sibling] The Review — Two Names in the Order
*Day 14 — Monday, January 26, 2026 — Monday, January 26, 2026 (dayOffset 14)*

The review on Monday, January 26, 2026 covers both girls, because both girls now have files. Wren's part goes well: her path home gets dates. June's part goes longer: services 'continue,' an end is discussed and not ordered, and her name stays in a system it entered through a door marked with her sister's birth date.

Ms. Ferreira gets the services review set and the basis written down at last — late, but written. What neither of you gets is June's file closed. Files opened on momentum close on somebody else's schedule.

**Choices:**
- Take Wren's dates, and June's review date, and go home to Rosa's fridge and its rules → **sibling_terms**
  - NOTE (shown after choosing): Two dates go on the fridge. One of them should never have needed to exist.

## [thin_week] The Week the File Went Quiet
*Day 9 — Wednesday, January 21, 2026 — Wednesday, January 21, 2026 (dayOffset 9)*

The missed intake is rescheduled once, then overtaken by a second collision, and the program — understaffed, not unkind — reports the file's least favorite phrase: 'did not attend; did not call.'

It is not true in spirit. You were with your newborn daughter, in a system that scheduled her against her own mother's treatment and kept both appointments in separate envelopes. But the file does not hold spirits. It holds phrases, and the next hearing will be conducted in them.

**Choices:**
- Go to the review and tell the truth out loud, with your lawyer's help → **review_thin_court**
  - NOTE (shown after choosing): Truth out loud is worth something in a courtroom. It is worth measurably less than the same truth, stamped, in a folder.

## [review_thin_court] The Review — The Paper Trail That Wasn't
*Day 14 — Monday, January 26, 2026 — Monday, January 26, 2026 (dayOffset 14)*

The review on Monday, January 26, 2026 is conducted, as Ms. Ferreira warned on Tuesday, January 13, 2026, in phrases from a file: forms signed as handed, no plan in writing, intake 'did not attend,' a sibling whose status no one documented either way.

The people in the room are not villains and several of them are visibly sorry. Sorrow is not a placement plan either. Wren's custody continues, her placement continues, no return date is set — there is, the court says, no documented basis on which to set one — and June's checks are ordered to continue 'pending the mother's engagement,' a phrase with no clock in it.

Nothing decided today is necessarily forever. Everything decided today was decided by the paper that existed today.

**Choices:**
- Hear the order, take your copy, and look at your lawyer → **hard_terms**
  - NOTE (shown after choosing): Ms. Ferreira is already writing — a plan, this time, in ink. Late is a bad address. It is not the same as nowhere.

## [short_terms] Dates, in the Order
*Day 17 — Thursday, January 29, 2026 — Thursday, January 29, 2026 (dayOffset 17)*

The order's dates are real: a step-down on the first, return on the second if the weeks match, the case's next review set and then, if all goes as written, no next review at all.

Wren's path home runs through Rosa's house, where it started — twenty minutes and one signature at a time. June's name appears nowhere in the document. Rosa reads it twice to be sure, then puts it on the fridge under the rules, where the family's binding papers live.

**Choices:**
- Live the weeks the way the order assumes you will → **end_shortterm**
  - NOTE (shown after choosing): Kept appointments, stamped paper, a baby gaining weight in her grandmother's kitchen. The order's assumptions, met, become the order's ending.

## [sibling_terms] Two Files, Two Speeds
*Day 17 — Thursday, January 29, 2026 — Thursday, January 29, 2026 (dayOffset 17)*

Wren's dates hold. June's services get their review, and at it — with the school's and doctor's letters finally filed by you, late and complete — the agency agrees her case, such as it ever was, can close after one more check.

One more check. The phrase follows your family home like a small dog: harmless, persistent, and entirely the product of a file that was opened by momentum and must now be closed by paperwork.

**Choices:**
- Do the last check, file the last letter, and take both girls to the park → **end_sibling_drawn**
  - NOTE (shown after choosing): June rides the big slide. Her file, somewhere, gets a closing stamp she will never see. Both facts are true; only one of them is the day.

## [hard_terms] What Happens Next, Honestly
*Day 17 — Thursday, January 29, 2026 — Thursday, January 29, 2026 (dayOffset 17)*

Ms. Ferreira's new folder has, at last, everything the first week should have had: a written plan with Rosa's name on it, June's documents, a re-booked intake with the collision problem solved in advance, in writing, by moving the visit with the agency's agreement noted on the page.

It is good paper. It is also, now, paper that must overcome a file instead of simply being one. The next review is months away. Wren will be held, fed, and visited in the meantime in a house that is not yours, by people who are not unkind, under an order that no one in the room that day wanted and everyone in the room that day produced.

**Choices:**
- Start — again, and for real this time — the record → **end_hard**
  - NOTE (shown after choosing): The folder is thick now. Its thickness arrived in the wrong order: after the decisions, instead of before them.

## [end_home] Ending — Home With a Safety Plan, One Case, Not Two
*Day 16 — Wednesday, January 28, 2026 — Wednesday, January 28, 2026 (dayOffset 16)*

**Ending.**

**Debrief:**
- THE BOARD, MAPPED — HOSPITAL TRACK: Wren's monitored days finished on schedule and she was discharged on Friday, January 16, 2026 to the written plan — the medicine took one plain sentence and was never the hard part. AGENCY TRACK: the investigation closed around a short, accurate file: a signed day-zero plan, Rosa's house checked on Tuesday, January 13, 2026, appointments kept and sheeted. SIBLING TRACK: June was never drawn in — her file contains one early, accurate sentence ('no concerns identified at this time') plus, on the strongest version of this path, her school and doctor letters filed before anyone proposed services for her. COURT TRACK: no court track exists. No custody order was ever signed, so no shelter care hearing was ever needed; the 72-hour hearing (42 Pa.C.S. § 6332; 23 Pa.C.S. § 6315(d)) is a protection that matters most on the paths where custody is taken, and your day-zero paper kept this family off those paths entirely.
- WHAT THE RECORD SHOWED: The plan, in writing, before it was needed — Rosa named, signed, dated Monday, January 12, 2026 — and, if you asked, the records themselves, requested under 55 Pa. Code § 3130.44(d) while the file was still short enough to read in one sitting, so you managed the case knowing what it said about each child. Counsel was available to you by right (42 Pa.C.S. § 6337), and on this path you barely needed her, which is what good early paper is for.
- WHAT WAS NEVER IN YOUR CONTROL: That a report was made at all; which worker arrived, and whether he was a person who slows down when a mother asks for copies; Rosa's proximity, health, and spare bassinet; the hospital's procedures. The same mother, with a grandmother two counties away or a worker in a hurry, signs different forms on day zero and lives a different month. Outcomes turn on workers, grandmothers, and luck as well as on parents. What your choices controlled was narrow and real: when the system reached for a form, your family's facts were already on one.

## [end_shortterm] Ending — Placed Short-Term, With a Dated Path Home
*Day 19 — Saturday, January 31, 2026 — Saturday, January 31, 2026 (dayOffset 19)*

**Ending.**

**Debrief:**
- THE BOARD, MAPPED — HOSPITAL TRACK: Wren's monitored care finished and she left the hospital to a placement — Rosa's house on the strong version of this ending, or as the subject of a short court oversight after the plan track's thin sibling page. AGENCY TRACK: the case stayed open and dated: kept, stamped appointments built a file the agency and the court could schedule a return from. SIBLING TRACK: June stayed home throughout and — decisively — out of the order: on the court version of this path her status was documented with her own school and doctor letters before the agency's momentum could make her a client; on the oversight version, her folder caught up late, and the review closed around it. COURT TRACK: where custody was taken on Monday, January 12, 2026, the shelter care hearing followed on Thursday, January 15, 2026, within 72 hours (42 Pa.C.S. § 6332; 23 Pa.C.S. § 6315(d)), with counsel beside you by right (42 Pa.C.S. § 6337); where it was not taken, the short oversight order did the same scheduling work more quietly. Either way: placed short-term, path home dated, case not closed — a beginning with paperwork.
- WHAT THE RECORD SHOWED: A plan that existed in writing by the hearing even if not on day zero; treatment attended and, on the documented version, stamped; a sibling record built from June's own documents. The dates in the final order were manufactured, visibly, from that paper — each date traces to a document the court was handed in time.
- WHAT WAS NEVER IN YOUR CONTROL: The day-zero forms put in front of a mother hours after delivery; the worker's and judge's readings of the same file; whether a treatment slot and a visit were scheduled against each other; Rosa's availability. Another mother with identical love and a thinner file — or this mother, on the same file, before a different judge — waits longer. Outcomes turn on workers, judges, and luck as well as on parents; what the record changed was the length and the datedness of the wait, which in a newborn's first months is not a small thing.

## [end_sibling_drawn] Ending — Baby Placed, and a Sibling Drawn Into Services
*Day 21 — Monday, February 2, 2026 — Monday, February 2, 2026 (dayOffset 21)*

**Ending.**

**Debrief:**
- THE BOARD, MAPPED — HOSPITAL TRACK: Wren's medicine took its one plain sentence and finished; she was placed, lived her first weeks between houses, and her path home acquired real dates at the Monday, January 26, 2026 review. AGENCY TRACK: your own case was handled — intake, plan, attendance. SIBLING TRACK: this is the track that moved. June — safe at Rosa's on Monday, January 12, 2026, school thriving, never the subject of a single new concern — acquired services, appointments, and a file of her own, because at the pivotal meeting her documented record was thinner than the agency's momentum. Her services eventually got a written basis and an end, but only after she had spent weeks as a client of a case that began with her sister's birth. COURT TRACK: custody of Wren was taken on Monday, January 12, 2026; her shelter care hearing followed on Thursday, January 15, 2026, within 72 hours (42 Pa.C.S. § 6332; 23 Pa.C.S. § 6315(d)); June was never before the court at all — everything that happened to her happened administratively, on paper nobody was required to hand a judge.
- WHAT THE RECORD SHOWED: For Wren, eventually, enough: a plan, attendance, dates. For June, for too long, a gap where her documents should have been — a school letter unfiled, a status unstated in writing — and a sentence she did nothing to earn ('family receiving services') that took a lawyer, a review, and your late, complete folder to retire. Nothing in this ending suggests June was ever unsafe. It shows how a sibling enters a system: not through a finding, but through an undocumented afternoon.
- WHAT WAS NEVER IN YOUR CONTROL: That the agency's design asks about siblings at all — that question is asked of every family, and asking it is not misconduct; that one worker documents and another proposes; the scheduling collisions; the judge. And some of it was in your control, which is the honest weight of this ending: June's letters existed, in Rosa's kitchen drawer, the whole time. Outcomes turn on workers, judges, and luck as well as on parents — and sometimes, as here, on which child's paper a tired mother is handed first.

## [end_hard] Ending — The Paper Trail That Was Never Built in Time
*Day 21 — Monday, February 2, 2026 — Monday, February 2, 2026 (dayOffset 21)*

**Ending.**

**Debrief:**
- THE BOARD, MAPPED — HOSPITAL TRACK: Wren's monitored care finished on its own schedule; everything after that sentence was decided by paper, and the paper was late. AGENCY TRACK: the investigation hardened into a case conducted in phrases — 'signed,' 'did not attend,' 'pending engagement' — several of them unfair in spirit and all of them accurate as records of what the file contained. SIBLING TRACK: June was never found unsafe and never formally opened, but her checks continue without a clock, because her status was never documented in a form that could end them. COURT TRACK: custody was taken on Monday, January 12, 2026, the shelter care hearing followed on Thursday, January 15, 2026 within 72 hours (42 Pa.C.S. § 6332; 23 Pa.C.S. § 6315(d)), and the reviews since have ruled, each time, on the record that existed that day — which is all any court can honestly do. Counsel was yours by right throughout (42 Pa.C.S. § 6337), and Ms. Ferreira's rebuilt folder is now the strongest paper in the case; it must overcome a file instead of simply being one.
- WHAT THE RECORD SHOWED: Almost nothing, in time — and that is the finding under this ending. The facts that would have changed Thursday, January 15, 2026 all existed: Rosa's house, June's school, your willingness. They existed in kitchens and conversations. The record, which is the only place hearings can look, held forms signed unread and appointments missed unexcused. Your late records request (55 Pa. Code § 3130.44(d)) and the rebuilt plan mean the next review will read a different case; the months between are the price of the order the paperwork arrived in.
- WHAT WAS NEVER IN YOUR CONTROL: Being handed binding forms hours after giving birth; a hospital's and an agency's procedures; scheduling that set your treatment against your visits; the worker and judge assigned. This ending is not a verdict on your fitness or your love, and it is not necessarily final — cases turn when records do, and yours has finally begun to turn. Outcomes in this system turn on workers, judges, hospital routines, and luck as well as on parents. The part that was yours was the pen, and the hardest fact in this scenario is how early the pen mattered most.
