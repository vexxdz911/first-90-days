# THE FIRST 90 DAYS — Scenario 13: “The Night Shift”

*Human-readable script. This document and `scenario-13.json` are generated from a single source and match node-for-node: same IDs, same order, same choices, same effects.*

**The family is fictional — a composite. No real person's story appears here.**

**Content note:** This scenario depicts a parent whose court-ordered services are all scheduled during the hours she sleeps after a night shift, and the choice between fighting the schedule on paper and quitting the job that pays her rent. It is told through shift logs, class sign-ins, and letters. There is no graphic content. Players may skip any scene or use the quick exit at any time.

**How to read effects:** `cash −40` changes the player's cash. `FLAG: name` sets a flag the engine tracks. `HIDDEN + item` means the case file quietly records that item at this choice — the player does not see it when it happens. `NOTE:` is text shown to the player right after choosing.

Start date: Monday, April 13, 2026. Day offsets are days since the scenario's start date. Tier: Hard.

## [start] The Schedule on the Refrigerator
*Day 0 — Monday, April 13, 2026 — Monday, April 13, 2026 (dayOffset 0)*

Your son Eli, seven, is staying with a foster family twenty minutes away while you work the case plan — and the plan, you have to admit, is not crazy. Parenting classes. Random screens. Visits twice a week. You want all of it. You have wanted all of it since the first day.

The problem is printed in the plan's own handwriting, in the column nobody read against your life: parenting class Tuesdays and Thursdays at 9:30 A.M. Screens on random weekday mornings. Visits Wednesdays at 10. You work the warehouse line from 11 P.M. to 7 A.M., five nights a week, and 9:30 A.M. is — for you — the middle of the night. The plan was scheduled for a person who sleeps in the dark. You sleep in the light, with foil on the windows and a fan for the hallway noise.

**Choices:**
- Tape the plan next to your shift schedule and look at the collision honestly → **first_class**
  - NOTE (shown after choosing): Side by side, they don't overlap. They occupy the same hours the way two tenants occupy one bed: by taking turns being impossible.

## [first_class] 9:30 A.M.
*Day 2 — Wednesday, April 15, 2026 — Wednesday, April 15, 2026 (dayOffset 2)*

You go to the first class straight off shift — no sleep at all, because sleeping first means waking at 9:15 in a panic. You take the bus in your work clothes. The instructor is kind, the material is not stupid, and somewhere around the module on routines, your body files its own report and your head goes down on the table for maybe ninety seconds.

The sign-in sheet records you present. The instructor's session note — you will not see it for weeks, which is part of the point of this scenario — records something else: 'Parent appeared fatigued; head down during module; engagement unclear.' In this system, you are what the notes say you were, at 9:30 in your personal midnight.

**Choices:**
- Stay to the end and thank the instructor — then go home and think → **choice_point**  _(cash -5; HIDDEN + Class note — 'appeared fatigued; engagement unclear' (first session, straight off shift))_
  - NOTE (shown after choosing): You were there. The sheet says you were there. The note says something adjacent to there, and notes outrank sheets.

## [choice_point] Two Kinds of Tired
*Day 5 — Saturday, April 18, 2026 — Saturday, April 18, 2026 (dayOffset 5)*

At your kitchen table, in the four hours that are supposed to be your deep sleep, you lay out the actual options, because nobody at the agency has laid them out for you. Option one: ask your employer to document your shift, and ask the agency — in writing — to amend the plan's times. Paper against paper, slow, uncertain. Option two: keep going exactly like this, on coffee and alarms, and hope the notes stay kind. Option three: quit the job. Attend everything, glowing, at 9:30 A.M. — and lose the income that pays for the apartment Eli is supposed to come home to, and the employment goal the plan itself requires.

Every option costs something real. That is not a flaw in this scenario. That is the scenario.

**Choices:**
- Talk to your supervisor first — find out what the job can put in writing → **ask_boss**
  - NOTE (shown after choosing): Break room, end of shift, fluorescent light. You have had harder conversations in worse light.
- Keep going as-is — alarms, coffee, willpower → **grind**
  - NOTE (shown after choosing): Willpower is a real resource. It is also a depleting one, and the plan runs for months.
- Do the math on quitting before you decide anything → **quit_think**
  - NOTE (shown after choosing): Rent, bus pass, Eli's room, the employment goal in the same plan that schedules you into your sleep. The math has a lot of columns.

## [ask_boss] The Break Room Conversation
*Day 6 — Sunday, April 19, 2026 — Sunday, April 19, 2026 (dayOffset 6)*

Your supervisor, Dana, has loaded trucks beside you for two years and does not waste your time. 'I can't move you to days — days is seniority, you know that. But your schedule isn't a secret. If the agency needs it in writing, I'll write it: shift, hours, the overtime pattern, all of it. What I can't do is write it to nobody. Get me a name or make your request and attach it.'

It is the first useful sentence anyone has given you in this case: the job can testify, but only in writing, and only into a process that asks. Dana also says the thing you needed to hear from the one person who can't fix it: 'Don't quit over a class time, Renee. Quitting is the one thing on that list you can't undo by Friday.'

**Choices:**
- Thank her, sleep four hours, and go see what the plan actually says — in the file, not from memory → **records_fork**  _(FLAG: employerWilling)_
  - NOTE (shown after choosing): A promise of a letter is not a letter. But it is a name to put in one: Dana's, and the word 'attach.'

## [grind] Coffee and Alarms
*Day 6 — Sunday, April 19, 2026 — Sunday, April 19, 2026 (dayOffset 6)*

You set three alarms across the room, the way people do who know their own weakness at 9 A.M. It works for the Tuesday class — you are awake, upright, and so tired the instructor's voice arrives a half-second after her mouth moves. It works for the visit. It works until Thursday, when it doesn't.

The random screen call comes at 8:40 Thursday morning, ninety minutes into your sleep, on the one morning you silenced the phone because the neighbor's dog had kept you up past noon the day before. The window to report is short. By the time you wake at 3 P.M., the window is closed and the log has a new line in it.

**Choices:**
- Call the screener the moment you wake and explain — today, not tomorrow → **missed_screen**  _(cash -5)_
  - NOTE (shown after choosing): Explanations made the same day have a weight class of their own. Not enough to erase a line. Enough to stand next to it.

## [missed_screen] The Closed Window
*Day 8 — Tuesday, April 21, 2026 — Tuesday, April 21, 2026 (dayOffset 8)*

The screener is professional and immovable: the screen is recorded as missed. Your explanation is 'noted' — that word again, the smallest house in the language — and she advises you to raise scheduling concerns 'through your caseworker and the plan process.'

You stand in your kitchen at 3 P.M. in the daylight you live backwards in, and you understand the geometry of your case: every element of the plan is scheduled inside your sleep; every failure to appear inside your sleep is recorded in the language of refusal. The file is not lying about you. It is describing a night worker in a day worker's vocabulary, and the vocabulary is winning.

**Choices:**
- Go see what the plan actually says — in the file, in writing → **records_fork**  _(HIDDEN + Screen — 'missed' (call came during parent's sleep hours after night shift))_
  - NOTE (shown after choosing): 'Raise it through the plan process.' Fine. Processes run on paper. It is time to find out what the paper says.

## [quit_think] The Math of Quitting
*Day 6 — Sunday, April 19, 2026 — Sunday, April 19, 2026 (dayOffset 6)*

The math, done honestly at the kitchen table: quitting frees every 9:30 in the world and deletes $2,400 a month. Rent is $950. The apartment has Eli's room in it — the room the plan's housing goal is about. Employment is not separate from the plan; it is one of the plan's own goals, listed two lines above the class times that make the job impossible to keep.

You could attend everything and fail the plan by succeeding at it. Or keep the job and fail the plan by sleeping. The plan, read closely, contradicts itself — but contradictions in documents are not resolved by the people the documents are about. They are resolved, if at all, in writing, by name, on the record. You put the pencil down without quitting. For now, 'for now' is a decision too.

**Choices:**
- Go see what the plan actually says — in the file, in writing → **records_fork**
  - NOTE (shown after choosing): If the plan contradicts itself, the place to prove that is the plan. The real one, from the file.

## [records_fork] What the Plan Actually Says
*Day 10 — Thursday, April 23, 2026 — Thursday, April 23, 2026 (dayOffset 10)*

Your lawyer asks whether you have ever read the plan as filed — not the summary the worker walked through, the document. You have not. Most parents haven't; the plan is 'reviewed with' families the way weather is reviewed with farmers. A party may request the case record in writing, and it 'shall be released upon request' (55 Pa. Code § 3130.44(d)).

What you are looking for is specific: every service time, in the plan's own words, and anything the file already says about your work schedule — whether the plan that schedules you at 9:30 A.M. anywhere admits that you work until 7.

**Choices:**
- Sign the written request for the record — the plan and the service notes → **plan_copy**  _(FLAG: recordsRequested)_
  - NOTE (shown after choosing): The request goes in with your name spelled right and the plan named by its date. Precision is a form of respect you can afford.
- Work from the summary you were given — it's close enough → **memory**
  - NOTE (shown after choosing): Summaries are written by the summarized. The summary of your schedule, as you're about to keep learning, rounds your life in the agency's favor.

## [plan_copy] The Plan, in Writing
*Day 14 — Monday, April 27, 2026 — Monday, April 27, 2026 (dayOffset 14)*

The filed plan is eleven pages, and your work schedule appears in it exactly once, on page nine, in a sentence that does a great deal of quiet damage: 'Parent is employed full-time.' Nothing about nights. Nothing about 11 to 7. Full-time — the plan's own author knew you worked and built a 9:30 A.M. plan anyway, or built it from a template and never looked up. Either way, the filed document contradicts itself in its own pages: it requires your employment and your presence in the same hours.

The service notes hold the other half: 'fatigued; engagement unclear.' 'Missed screen.' Each note is accurate about a moment and wrong about a person, and both kinds of wrong are now exhibits — if someone assembles them.

**Choices:**
- Ask Dana for the letter this week — shift, hours, overtime, on company letterhead → **letter_draft**  _(HIDDEN + Case plan — services at 9:30 A.M.; parent's night shift recorded only as 'employed full-time')_
  - NOTE (shown after choosing): Dana writes it in two days. Employers' letters are short because employers are busy. Short is fine. Letterhead does the talking.

## [memory] From Memory
*Day 14 — Monday, April 27, 2026 — Monday, April 27, 2026 (dayOffset 14)*

From the summary, your recollection is right about the big things and fuzzy about the filings: you know the class is 9:30 because you live it. What you don't have is the plan's own page nine — 'employed full-time,' nothing about nights — the single most useful sentence in your case, sitting in a document you've never been handed.

You can still ask Dana for the letter, and you do. An employer's letter proves your shift. What it can't prove by itself is that the agency knew — and the plan, the filed one, is where knowledge lives in this system. You'll be asking the agency to amend a document you haven't read. People do it every day. It works exactly as well as that sounds.

**Choices:**
- Get Dana's letter anyway — it's the strongest paper you can hold this week → **letter_draft**
  - NOTE (shown after choosing): Half a record is not no record. It's the half the next four choices are about.

## [letter_draft] Two Letters
*Day 17 — Thursday, April 30, 2026 — Thursday, April 30, 2026 (dayOffset 17)*

Dana's letter arrives on letterhead: your name, your shift — 11 P.M. to 7 A.M., Sunday through Thursday — your overtime pattern, and one line Dana added without being asked: 'Employee is in good standing and her position depends on continued availability for her assigned shift.' The job, testifying.

Now the second letter: yours. A written request to amend the plan's service times — evening parenting cohort, screens on your days off or early evening, visits after school for Eli anyway — with Dana's letter attached and, if you requested it, the filed plan's page nine cited by number. Your lawyer reviews the draft and changes one word: 'request' stays, 'beg' goes. This is the fork the whole scenario has been walking toward, and all three roads are still open.

**Choices:**
- File the written amendment request — your letter, Dana's letter attached, copy to your lawyer → **filed**  _(cash -4; FLAG: amendmentFiled; HIDDEN + Plan amendment request — filed in writing with employer letter attached)_
  - NOTE (shown after choosing): Filed, stamped, copied. The plan now has a pending objection with a date on it, written by the person it schedules.
- Ask your caseworker verbally at Wednesday's visit — she's sympathetic, and paper feels confrontational → **verbal**
  - NOTE (shown after choosing): She is sympathetic. Sympathy, like goodwill, is a quality of a person. Amendments are qualities of documents.
- Quit the job — attend everything, and rebuild the money later → **quit_path**
  - NOTE (shown after choosing): You hand in notice at 6:50 A.M., ten minutes before your shift ends, so you won't have to come back and do it.

## [filed] Stamped and Attached
*Day 19 — Saturday, May 2, 2026 — Saturday, May 2, 2026 (dayOffset 19)*

The amendment request goes in on a Friday. By Wednesday, three things have happened, in the order paper makes things happen: your caseworker calls — actually calls — and says the request is 'with the supervisor'; the class provider's office emails your lawyer asking what evening capacity they would need; and your file acquires a new section, which is the real event. Your objection now exists where objections are adjudicated: inside the record, dated, with an employer's letterhead behind it.

Nothing is granted yet. Providers run cohorts on funding cycles; supervisors answer in their own time. But the question before the case has changed. It is no longer 'why does this parent keep failing to engage?' It is 'the parent has asked, in writing, with documentation — what is the agency's answer?'

**Choices:**
- Wait for the answer — and attend what you can, exactly as the filed request describes → **response**
  - NOTE (shown after choosing): Attending 'what you can' while a documented request pends is a different record from missing. The request explains the pattern before the pattern can be misread.

## [verbal] She Said She'd Ask
*Day 19 — Saturday, May 2, 2026 — Saturday, May 2, 2026 (dayOffset 19)*

Your caseworker is genuinely sympathetic at Wednesday's visit. She says the times are 'just when the provider runs it,' says she'll 'see what can be done,' and writes something in her notebook — her notebook, which is not the file, which is not the plan. Eli shows you a LEGO structure and the visit ends on time.

Two weeks later, nothing has moved, because nothing was ever formally asked. There is no request in the file for a supervisor to deny or grant, no employer letter attached to anything, no date from which delay could even be measured. You had a conversation. The plan had a month. Only one of those is a document.

**Choices:**
- Attend the next 9:30 class off shift and think about what paper would have done → **no_response**
  - NOTE (shown after choosing): You already know. The knowing is the tuition this scenario charges; the review is where it gets spent.

## [quit_path] Day Shift, No Shift
*Day 19 — Saturday, May 2, 2026 — Saturday, May 2, 2026 (dayOffset 19)*

Without the alarm set for a shift that no longer exists, you sleep at night like the plan's imaginary parent, and you attend the Tuesday class rested, early, with the readings done. The instructor's note for that session — you will see this one eventually — says 'engaged, prepared, a pleasure.' It is the note you always deserved. It cost $2,400 a month.

You tell Eli's caseworker you've left the job 'to focus on the plan,' and you watch her write it down, and you cannot tell from her face whether she has noticed that the plan also has an employment goal, and a housing goal, and that both of them just walked out of the warehouse with you. The landlord notices faster than the agency does. Landlords always do.

**Choices:**
- Attend everything, perfectly, and let the other goals wait their turn → **quit_strain**
  - NOTE (shown after choosing): Attendance: perfect. The plan has four goals. You are now excelling at the ones with chairs.

## [response] The Provider's Answer
*Day 26 — Saturday, May 9, 2026 — Saturday, May 9, 2026 (dayOffset 26)*

The answer takes a week and arrives as a plan, not a verdict: the provider runs a funded evening cohort that starts in three weeks — parenting classes at 6 P.M., full curriculum, same credit. Screens move to your two evenings off, by written arrangement. Visits stay Wednesdays at 10 for now, because Eli's school and the foster family's mornings are also real, but they move to late afternoon when the school term turns.

Three weeks of the old schedule remain — the gap between a granted request and a changed world, which in this system is where parents are most often lost. The request being granted does not attend those three weeks for you. But it changes what those weeks mean in the file: they are now the documented tail of a schedule the agency itself has agreed was wrong.

**Choices:**
- Bridge the three weeks exactly as your filing described — and write down every session you attend or miss, with the reason → **interim**
  - NOTE (shown after choosing): A short bridge, walked in writing. Three weeks is twelve alarms. You have set harder ones.

## [no_response] The Third Note
*Day 26 — Saturday, May 9, 2026 — Saturday, May 9, 2026 (dayOffset 26)*

By the third 9:30 session note — 'fatigued,' again, in the same hand — the file has a pattern, and patterns in files acquire names. At the team meeting you are not in, the pattern's name is 'engagement concerns.' Nobody in that room is lying. Nobody in that room works nights. The one document that could rename the pattern — a filed amendment request with an employer's letter — does not exist in this path, because it was never filed.

Your lawyer, preparing for the review, puts it plainly: 'We can still file. Late paper is worse than early paper and better than no paper, because at the review I'll have to explain the notes, and right now the only explanation is your voice.'

**Choices:**
- File the amendment request now — late, with Dana's letter, before the review → **interim_b**  _(FLAG: amendmentFiled; HIDDEN + Plan amendment request — filed late, after three 'fatigued' session notes)_
  - NOTE (shown after choosing): Late, stamped, real. The review will now contain both things: the notes, and the dated proof that you eventually answered them in the only language the system files.
- Keep grinding to the review — no paper, just attendance and hope → **interim_b**
  - NOTE (shown after choosing): Attendance you have. Hope is not a filing. The review will run on what exists.

## [quit_strain] Perfect Attendance, Empty Fridge
*Day 26 — Saturday, May 9, 2026 — Saturday, May 9, 2026 (dayOffset 26)*

The attendance record is, as promised, perfect — and the rest of the plan has begun to fail in the opposite direction. The employment goal: unmet, by resignation. The housing goal: the landlord, a decent man with a mortgage of his own, gives you until the end of next month, in writing, because even decent men put it in writing. Your lawyer gets a copy of that letter too. Everyone in this story documents things. It's only ever been a question of whose documents get read as the case.

At the team meeting, your perfect attendance is noted with approval, and then the housing slide is shown, and the room's temperature changes. The plan was a system. You optimized the part of it that met at 9:30 A.M. and broke the parts that met at the first of the month.

**Choices:**
- Go to the review and answer for the whole plan — all four goals, not one → **quit_review**
  - NOTE (shown after choosing): You will present a paradox in person: the most compliant parent in the building, and a plan further from reunification than when she quit.

## [interim] Three Weeks at 9:30
*Day 33 — Saturday, May 16, 2026 — Saturday, May 16, 2026 (dayOffset 33)*

The bridge weeks are exactly as bad as advertised, and you walk them the way your filing said you would: two classes attended off shift, notes be damned; one screen on an evening off, arranged in writing; and one class — the second Thursday — that you notify the provider about in advance, in writing, because a mandatory overtime shift lands on your sleep and the letter says, in the sentence your lawyer underlined when she drafted it, 'as documented in my pending amendment request, now granted, effective in three weeks.'

That notification is the smallest document in this scenario and maybe the most important: it converts a miss into a correspondence. When the provider's log for that Thursday is written, it says 'parent notified in advance; amendment effective [date].' Compare the vocabulary of the paths not taken. Same mother. Same sleep. Different paper.

**Choices:**
- Sleep a full day, then prepare for the review with your lawyer → **review_prep_a**  _(HIDDEN + Interim class — parent notified provider in writing in advance, citing the granted amendment)_
  - NOTE (shown after choosing): The evening cohort roster has your name on it. Rosters are promises with columns.

## [interim_b] What the Review Will See
*Day 33 — Saturday, May 16, 2026 — Saturday, May 16, 2026 (dayOffset 33)*

Review preparation is an inventory, and inventories are honest: three 'fatigued' notes, one missed screen, an employer's letter (if you got it), an amendment request (if you filed it, whenever you filed it), and a supervisor's verbal sympathy that exists in no inventory anywhere because it was never written down.

Your lawyer arranges what exists in date order and tells you the truth about reviews: the judge will not see your exhaustion, your alarms, or your intentions. She will see the inventory. The best remaining move is the one you have always had: make the inventory tell the story in the order it actually happened — a day-scheduled plan, a night-working parent, and paper that is either early, late, or absent.

**Choices:**
- Go to the review with the inventory as it is → **hearing_b**
  - NOTE (shown after choosing): Whatever is in the folder goes. Whatever isn't, doesn't. That sentence is the whole curriculum of this game.

## [review_prep_a] Paper for the Review
*Day 41 — Sunday, May 24, 2026 — Sunday, May 24, 2026 (dayOffset 41)*

Your lawyer's folder for the review is thin and devastating: the filed plan (page nine: 'employed full-time'); Dana's letter; your amendment request with its stamp; the provider's written answer; the evening roster with your name on it; and the interim notification. Six documents that tell one story in date order: the plan was scheduled against a documented life; the parent said so, in writing, with proof; the system, to its credit, moved.

'The early notes are still in the file,' your lawyer says. 'Fatigued, engagement unclear — they'll stay there. Notes don't get erased. But they stop being the story when the story gets longer.'

**Choices:**
- Go to the review → **hearing_a**
  - NOTE (shown after choosing): You sleep until 4 P.M. the day before, like a person whose life is scheduled by someone who has read her file. Because now, finally, it is.

## [quit_review] The Other Goals
*Day 41 — Sunday, May 24, 2026 — Sunday, May 24, 2026 (dayOffset 41)*

Preparing for the review on the quitting path is a different inventory: perfect class attendance; glowing session notes; an employer's letter that now describes a job you no longer have; a landlord's letter with a date in it; and two plan goals — employment, housing — moving backwards in the same weeks the service goals completed.

Your lawyer does not scold you. She does something worse: she shows you the plan's four goals printed on one page, the way the judge will see them, and lets the page make the argument. 'You didn't fail the plan,' she says. 'You obeyed it one goal at a time. The plan failed to be one plan. Our job at the review is to make the court see that — and it is a harder argument than the amendment letter would have been.'

**Choices:**
- Go to the review and make the argument in person → **hearing_quit**
  - NOTE (shown after choosing): You attend, as you now attend everything: rested, early, and unsure which of those the court will count.

## [hearing_a] The Review — The Plan Moves
*Day 49 — Monday, June 1, 2026 — Monday, June 1, 2026 (dayOffset 49)*

The review is almost anticlimactic, which is what winning in this system usually feels like from inside. The agency reports the amendment as implemented: evening cohort, adjusted screens, visits moving at the term's turn. Your lawyer places the six documents in the record without drama, because drama is what paper is for avoiding. The 'fatigued' notes are not mentioned by anyone, and they do not need to be: they have been answered by a roster.

The judge confirms the amended plan and sets the next review. Eli's foster mother, leaving, tells you the Wednesday visits will suit Eli better anyway — he'll come straight from school, full of the day, instead of being woken into them. Nobody says the sentence out loud, so you say it in the car, to the steering wheel: the plan moved. Not the mother. The plan.

**Choices:**
- Go home, set no alarm, and sleep in the daylight like it's your shift — because it is → **end_amended**
  - NOTE (shown after choosing): The evening cohort starts Monday. Your name is on the roster, in the right column, at an hour when you are a person.

## [hearing_b] The Review — Counted as Missed
*Day 49 — Monday, June 1, 2026 — Monday, June 1, 2026 (dayOffset 49)*

The review runs on the inventory, exactly as your lawyer promised it would. The agency's report uses the file's vocabulary: 'engagement concerns,' 'missed screen,' 'inconsistent participation.' Your testimony about the shift is true, and the judge does not disbelieve you — you can watch her not disbelieve you, which is its own education. Belief is not the currency. The record is, and the record's account of why a night worker kept appearing at 9:30 A.M. unready is three notes long.

If a late amendment request is in the file, she acknowledges it — 'the parent has now raised the scheduling conflict in writing' — and directs the agency to respond to it before the next review. If it isn't, she directs you, kindly, to raise concerns 'through the plan process,' the same sentence the screener gave you in your kitchen. Either way, this review closes on the notes that exist.

**Choices:**
- Leave with the judge's direction in your notebook — the process sentence, one more time → **end_counted**
  - NOTE (shown after choosing): Raised through the plan process. In writing. With a letter attached. You knew the sentence before she said it. Knowing and filing are different verbs.

## [hearing_quit] The Review — Everything Attended
*Day 49 — Monday, June 1, 2026 — Monday, June 1, 2026 (dayOffset 49)*

Your attendance is praised, on the record, by everyone — and then the housing and employment goals are read, and the praise changes key. The agency's position is not cruel; it is structural: Eli cannot be returned to an apartment that will not exist next month, and a plan goal cannot be met by a job that was resigned, however excellent the reason.

The judge looks at the four goals on one page for a long moment. 'The plan asked this parent to be in two places at once,' she says, to the agency's counsel, not to you. 'And she chose the place with the chairs.' It is the fairest sentence anyone has written about your spring — and it is a sentence about the plan, delivered at a review whose outcome still runs on the goals as they stand: two complete, two collapsing.

**Choices:**
- Hear the outcome with your folder of perfect attendance on your lap → **end_quit**
  - NOTE (shown after choosing): Every page of it true. Every page of it insufficient. The folder and the plan fail together, in opposite directions.

## [end_amended] Ending — The Plan Moves
*Day 56 — Monday, June 8, 2026 — Monday, June 8, 2026 (dayOffset 56)*

**Ending.**

**Debrief:**
- WHAT THE FILE HELD (the hidden record, revealed): The early notes never left your file — 'fatigued; engagement unclear,' a missed screen, recorded in the vocabulary of refusal. What changed is that they stopped being the file's conclusion. Your amendment request, filed in writing with your employer's letter attached, is dated and stamped; the provider's answer and the evening roster follow it in sequence. Read in order, the record now tells the true story: a plan scheduled against a documented night shift, a parent who objected on paper with proof, and a system that — slowly, on its own calendar — moved. The notes remain. They are now the first chapter instead of the whole book.
- THE PROCESS UNDER THIS PATH (described, keeping to this scenario's verified law): This win was built from the two verified tools this scenario uses: the right to the record itself (the case record 'shall be released upon request,' 55 Pa. Code § 3130.44(d)) — which is how you found page nine, the plan conceding your full-time job while scheduling you into your sleep — and counsel to aim the request (42 Pa.C.S. § 6337). No verified rule in this set entitled you to evening classes. What the written request did was convert a private hardship into a pending item the agency had to answer on the record, with the employer's letter making the hardship undeniable and the filing date making the agency's response time measurable. And note the win's honest shape: the job survived, the services survived, and three bad weeks were bridged, not erased. The plan moved. That was always the only thing that needed to.
- THE HONEST PART: A different provider might have had no evening cohort to offer; a different supervisor might have answered slower, or not at all, leaving the review to weigh a pending request instead of a granted one — which still beats weighing unexplained notes, but by less. Dana's willingness to write the letter, your lawyer's single-word edit, and the funding cycle that happened to open a 6 P.M. cohort were all partly luck. What was not luck: the request existed, in writing, with documentation, early enough for luck to act on. In the published cases this scenario is built from, parents described impossible schedules in testimony — afterward, in the past tense, to judges reading notes that had already hardened. The difference in this path is tense. You said it in the present, on paper, while it could still be fixed.

## [end_counted] Ending — Counted as Missed
*Day 49 — Monday, June 1, 2026 — Monday, June 1, 2026 (dayOffset 49)*

**Ending.**

**Debrief:**
- WHAT THE FILE HELD (the hidden record, revealed): Three session notes about fatigue, one missed screen, and a judicial direction to raise scheduling concerns 'through the plan process.' That is the whole record of a structural impossibility — a plan whose every service sat inside a night worker's sleep — as written by the system's ordinary vocabulary. Your exhaustion was real, your attendance mostly happened, and your reasons were believed by everyone who heard them aloud. None of that is in the file in a form a future reader can act on, because almost none of it was ever filed.
- THE PROCESS UNDER THIS PATH (described, keeping to this scenario's verified law): Hearings and reviews decide from records, and records are made of documents. The tools to build a different one were present the entire time: the case record on written request (55 Pa. Code § 3130.44(d)) — the filed plan's page nine, conceding your full-time employment, was the strongest single page available to you — and counsel (42 Pa.C.S. § 6337) to draft the amendment request the situation called for. A verbal ask to a sympathetic worker creates no pending item, no response deadline, and no exhibit; a written request with an employer's letter creates all three. This ending is not a punishment for being tired. It is the mechanical result of a mismatch described only in speech, inside a system that files speech nowhere.
- THE HONEST PART: It is worth saying plainly that the underlying fault was never yours: a plan that schedules a night worker's services at 9:30 A.M. is a defective plan, and on a fuller record a court might have said so in stronger terms. Judges vary; some would have pressed the agency on the schedule even from this thin file, and workers with different caseloads might have moved the times on a hallway conversation. But 'might have' is the tax this path pays at every step. And the door is not closed: the judge's direction at this review — raise it through the plan process — is the amendment request, still available, now with a court's sentence behind it. Filed next week, it changes the next review. The scenario ends here because semesters end; cases, mercifully and otherwise, continue.

## [end_quit] Ending — Everything Attended, Nothing Stable
*Day 56 — Monday, June 8, 2026 — Monday, June 8, 2026 (dayOffset 56)*

**Ending.**

**Debrief:**
- WHAT THE FILE HELD (the hidden record, revealed): A bifurcated record — attendance pages that glow and goal pages that collapse, in the same binder. The class notes praise your engagement in the vocabulary the early notes denied you; the employment and housing pages record a resignation and a landlord's deadline. Read together, which is how judges read, the file tells a story nobody intended: a parent who complied with the plan so literally that she complied herself out of the apartment and the job the plan also required. The system's own witness said it best at your review: the plan asked you to be in two places at once, and you chose the place with the chairs.
- THE PROCESS UNDER THIS PATH (described, keeping to this scenario's verified law): A case plan is adjudicated as a whole, because reunification is a whole: a child returns to a home, a job, a schedule — not to a stack of completed classes. That is why the amendment route existed, and why it mattered that it be written: a filed request (built on the record you could obtain under 55 Pa. Code § 3130.44(d), with counsel's help under 42 Pa.C.S. § 6337) asks the agency to repair the plan's internal contradiction at the agency's cost. Quitting repaired it at yours — converting the plan's defect into your deficits, which then appeared in the file under your name instead of the plan's. The attendance was real and the sacrifice was real. Neither could be spent at the review on the goals that were failing.
- THE HONEST PART: This path was not foolishness; it was a rational response to a file that kept calling your sleep 'disengagement,' and some parents who quit under this pressure do land on their feet — a new day job, a lenient landlord, a judge who credits the sacrifice. Luck and local labor markets decide much of that, and this scenario will not pretend your choice was a moral failure, because it wasn't one. It was a strategic transfer: you paid the plan's debt out of your own account. The apartment, the job, and the timeline can all be rebuilt — parents in the published record this scenario draws from rebuilt more from less — but they rebuild on the case's clock, not yours, and the clock was the one resource the warehouse job was buying you. What you keep from this ending is the knowledge, bought dearly, of what the written ask was actually worth: everything it would have cost the agency nothing but a signature to grant.
