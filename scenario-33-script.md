# THE FIRST 90 DAYS — Scenario 33: “The Two Petitions”

*Human-readable script. This document and `scenario-33.json` are generated from a single source and match node-for-node: same IDs, same order, same choices, same effects.*

**The family is fictional — a composite. No real person's story appears here.**

**Content note:** This scenario depicts a dependency goal-change / concurrent-planning fight — two tracks, two timelines, and a hearing — told through procedure and paperwork. There is no graphic content. Players may skip any scene or use the quick exit at any time.

**How to read effects:** `cash −40` changes the player's cash. `FLAG: name` sets a flag the engine tracks. `HIDDEN + item` means the case file quietly records that item at this choice — the player does not see it when it happens. `NOTE:` is text shown to the player right after choosing.

Start date: Monday, May 4, 2026. Day offsets are days since the scenario's start date.

## [start] Eleven Months In
*Day 0 — Monday, May 4, 2026 — Monday, May 4, 2026 (dayOffset 0)*

Eleven months ago your daughter Lark, who is seven, was placed in foster care. The reasons belong to a hard year: a lost apartment, shifts that did not line up with childcare, and a winter you managed badly and have been repairing, on paper and in person, ever since.

Here is the repair, as the file currently tells it. You are Marcus, a forklift operator on the early shift. Your apartment is stable. Your screens are clean. Visits with Lark run twice a week and have grown longer. Your parenting program stands at nine sessions of twelve. You are, in the plan's own rating word, progressing — unevenly, and really.

Lark lives with the Hartleys, who are kind, who send her school drawings home in her visit bag, and who have told the agency they would adopt her if adoption ever became the plan. Nobody has said that sentence to you yet. It is in the file anyway.

**Choices:**
- Open the mail that came while you were at work → **motion_notice**
  - NOTE (shown after choosing): One envelope is from your lawyer. One is from the agency. They are about the same hearing.

## [motion_notice] A Second Envelope
*Day 4 — Friday, May 8, 2026 — Friday, May 8, 2026 (dayOffset 4)*

The agency's letter is short and procedural. At the next permanency review it will ask the court to change Lark's goal away from reunification — toward adoption.

Nothing in the letter says your services stop. Nothing in it says your visits change. It asks for a different finish line while you are still running toward the first one, and it does not explain, in parent-sized language, how a person is supposed to run toward two finish lines at once.

Your lawyer's letter is one line: “Come in Tuesday. Bring your folder. We need to talk about tracks.”

**Choices:**
- Call her office and ask for the earliest appointment → **lawyer_map**
  - NOTE (shown after choosing): Tuesday, nine o'clock. She says the word 'tracks' again, like it is the whole appointment.

## [lawyer_map] Two Tracks on One Whiteboard
*Day 8 — Tuesday, May 12, 2026 — Tuesday, May 12, 2026 (dayOffset 8)*

Your lawyer, Ms. Osei, was appointed for you at the start of this case, as the law provides (42 Pa.C.S. § 6337). She draws two lines on her whiteboard, one above the other, and labels them in marker.

“Track A is the case you know: finish the plan the court ordered, and the court reviews whether Lark can come home. Track B is new: a goal-change track, heading toward a different future. From today, both tracks run at the same time. Evidence you build on Track A is also, whether anyone says so or not, evidence on Track B.”

“And under both lines there is a clock. Lark was placed on June 2, 2025. Fifteen of the most recent twenty-two months arrives on Wednesday, September 2, 2026. At that point the federal law presses the agency to file a petition to end parental rights — unless an exception is documented. Relative care. A documented compelling reason. Or this one, so remember it: the agency has not provided services the plan identified as necessary for Lark to come home safely (42 U.S.C. § 675(5)(E)). Our work, all summer, is to make the record on Track A so current, and the exceptions so documented, that Track B has nowhere honest to go.”

**Choices:**
- Ask what you do differently, starting this week → **class_night**  _(HIDDEN + Counsel's map — Track A (finish the plan) and Track B (goal change) run at the same time; ASFA date September 2, 2026)_
  - NOTE (shown after choosing): “You attend everything. You file your progress instead of just making it. And at every hearing, you ask which track a piece of evidence belongs to.”

## [class_night] Track A, Night Class
*Day 12 — Saturday, May 16, 2026 — Saturday, May 16, 2026 (dayOffset 12)*

Session ten of twelve. The parenting program meets in a church basement that smells of coffee and floor wax, and tonight's topic — routines a seven-year-old can count on — is one you could now teach parts of.

Your supervisor has offered overtime tonight that would cover most of a month's electric bill. The sign-in sheet is by the door. In this system, the sign-in sheet is not a formality. It is the difference between a session that happened and a session that, months from now, a summary can describe either way.

**Choices:**
- Stay for the session and sign in, as always → **written_progress**  _(HIDDEN + Parenting program — session 10 of 12 attended, signed in)_
  - NOTE (shown after choosing): The overtime goes to someone else. The signature stays in the file.
- Take the overtime — one missed session, explained later, should be fine → **written_progress**  _(cash +40; HIDDEN + Parenting program — session 10 missed for overtime; no note filed)_
  - NOTE (shown after choosing): It probably will be fine. 'Explained later' is a promise you are making to a file.

## [written_progress] Say It in Writing
*Day 16 — Wednesday, May 20, 2026 — Wednesday, May 20, 2026 (dayOffset 16)*

Ms. Osei has a rule she repeats until parents repeat it back: progress that is only spoken is weather; progress that is filed is climate.

Your class facilitator will confirm your attendance if anyone asks. Your landlord will confirm your tenancy if anyone asks. Your screen provider sends results to the agency on its own schedule. Almost everything true about your summer is currently waiting for someone to ask.

There is a one-page form for a parent's written progress statement. It goes into the court file, where summaries are later written from.

**Choices:**
- File the written progress statement this week, with certificates attached → **records_beat**  _(FLAG: writtenProgress; HIDDEN + Parent's written progress statement filed, with certificates)_
  - NOTE (shown after choosing): Dated, copied, filed. Your summer, in your words, where the judge's summer will be written from.
- Keep it verbal — your caseworker knows how you're doing → **records_beat**
  - NOTE (shown after choosing): She does. Caseworkers, as this whole series keeps showing, are not the file's only readers, or its last ones.

## [records_beat] The File, Including the Form
*Day 20 — Sunday, May 24, 2026 — Sunday, May 24, 2026 (dayOffset 20)*

Ms. Osei reminds you of the quieter right, the one that does not depend on any hearing: you may request your own case record from the county agency, and under the regulation it “shall be released upon request” (55 Pa. Code § 3130.44(d)). She is specific about asking for the whole of it, including the full assessment — the form itself, the item ratings, and the outcome — and not only the summary pages.

She adds the honest limit she always adds about the assessment: an earlier disclosure rule for the adjudication phase (Pa.R.J.C.P. 1340(B)(1)) exists, but whether it reaches every scored item of an assessment form is untested. The direct record request does not depend on that question. She intends to make it either way.

The request is one page. The stamp is one stamp.

**Choices:**
- Sign and send the request this week → **file_arrives**  _(FLAG: recordsRequested)_
  - NOTE (shown after choosing): A stamp, a date, a copy for your folder. The cheapest power in this whole system.
- Wait — one fight at a time; the goal-change hearing is the fight → **no_file**
  - NOTE (shown after choosing): Understandable. The file will still be written this summer. It will simply be written without your reading it.

## [file_arrives] The Referral That Reads 'To Be Sent'
*Day 27 — Sunday, May 31, 2026 — Sunday, May 31, 2026 (dayOffset 27)*

The packet is thick, and partly blacked out, and still: there it is. Your ratings, climbing. The visit notes, warm and specific. The assessment form itself, its items and ratings plainer than you feared and more ordinary: supervision, housing stability, follow-through.

And on the service plan's second page, a line you read three times. A referral for coached visits — the service the plan itself described as the step that would move your visits toward unsupervised time — marked, in the month Lark had been in care six months: “Referral — to be sent.” There is no send date. There is no follow-up note. The step your progress was measured against was never actually offered to you.

You sit with that a while. It is not a villain's act. It is a box, in an office, that nobody checked. Boxes like that, unchecked, have decided cases.

**Choices:**
- Take the page to Ms. Osei before you do anything else → **visits_rhythm**  _(FLAG: servicesGapFound; HIDDEN + Service plan — coached-visit referral marked 'to be sent,' month 6; never sent)_
  - NOTE (shown after choosing): “Don't be angry in September,” she says. “Be documented in September.”

## [no_file] Working from Summaries
*Day 27 — Sunday, May 31, 2026 — Sunday, May 31, 2026 (dayOffset 27)*

Without the file, you and Ms. Osei work from the court reports — which are fair, and warm about your visits, and summaries all the same.

A summary tells you what its writer thought mattered. It does not show you the plan's second page, or what any box on it says, or whether the step you were measured against was ever actually offered. You prepare for September with a good map of everything except the ground.

**Choices:**
- Prepare anyway — your attendance and your visits are real, file or no file → **visits_rhythm**
  - NOTE (shown after choosing): They are real. September will be conducted, as these hearings are, in documents.

## [visits_rhythm] Saturday with Lark
*Day 31 — Thursday, June 4, 2026 — Thursday, June 4, 2026 (dayOffset 31)*

Saturday visits have a rhythm now: the library first, then the park, then the long goodbye at the Hartleys' door that Lark has started managing by assigning you homework — a drawing to finish, a chapter to read so you can discuss it.

Mrs. Hartley mentions, kindly, that the agency has asked them about “permanency paperwork.” She does not use the word adoption. She is being careful with you, and you can feel the care and the paperwork in the same sentence.

This is Track B, arriving not in a courtroom but at a front door, in a kind voice.

**Choices:**
- Ask, just as kindly, what paperwork — and write down her answer, dated, that evening → **school_form**  _(HIDDEN + Visit note — foster family asked about 'permanency paperwork'; answer recorded, dated)_
  - NOTE (shown after choosing): Not an argument. A record. The two tracks are now visible in the same week, in your own handwriting.
- Let the sentence pass — Saturday is Lark's, not the case's → **school_form**
  - NOTE (shown after choosing): Most of Saturday is hers. That is the point of Saturday. The sentence, unwritten, goes where unwritten sentences go.

## [school_form] The School Form
*Day 34 — Sunday, June 7, 2026 — Sunday, June 7, 2026 (dayOffset 34)*

Lark's school needs a form signed about who may collect her — a small, ordinary piece of parent work that currently requires three people's signatures and a call to the agency.

Filling it in, you notice the form has two boxes for the future: the address she lives at now, and a line for “changes expected this year.” You leave the second line for the school counselor to see, and she looks at it a moment before she files it.

“Everyone's planning something for this kid,” she says, not unkindly. “It's good she has people planning.”

**Choices:**
- Ask the counselor to keep your updated contact page with the form → **two_timelines**
  - NOTE (shown after choosing): One more current page in one more file. Current is a strategy, not a personality trait.

## [two_timelines] Two Timelines, Side by Side
*Day 38 — Thursday, June 11, 2026 — Thursday, June 11, 2026 (dayOffset 38)*

Ms. Osei drafts, on one page, the document she calls the summer's spine: two timelines, side by side. On the left, Track A — your sessions, screens, visits, tenancy, each with its date and its proof. On the right, Track B — the motion, the hearing date, and at the bottom of the right-hand column, in the same size type as everything else: September 2, 2026, fifteen months.

“Judges should not have to assemble this from a pile,” she says. “We hand it up assembled. Every hearing from now on, we ask that the two timelines be stated on the record, side by side, so no one can describe your case using only one of them.”

**Choices:**
- Ask her to file the two-timeline page with the court now, not in September → **referral_call**  _(FLAG: timelineFiled; HIDDEN + Two-timeline statement filed — Track A progress and Track B clock on one page)_
  - NOTE (shown after choosing): Filed in spring light, it becomes part of the record every later summary must reckon with.
- Keep it as a hearing exhibit only — no need to show your hand early → **referral_call**
  - NOTE (shown after choosing): Ms. Osei shrugs professionally. “A record filed early corrects other records. An exhibit corrects one afternoon.”

## [referral_call] Chasing the Referral, on Paper
*Day 45 — Thursday, June 18, 2026 — Thursday, June 18, 2026 (dayOffset 45)*

There is a step available that costs nothing but nerve: ask the agency, in writing, about the coached-visit referral — the one the plan called necessary — and ask that it be made now.

If you learned of the gap from your own file, the letter can cite the plan's page and its empty box. If you did not, the letter is still worth sending in its general form: please confirm each referral the plan promised, with its send date. Either way, the answer — or the silence — becomes part of the record, dated.

A phone call would be friendlier. A phone call would also, by autumn, be a memory two people remember differently.

**Choices:**
- Send the letter — polite, dated, specific, with a copy for the court file → **shift_conflict**  _(FLAG: gapLetter; HIDDEN + Parent's letter — owed referral identified by date; agency asked to make it and confirm in writing)_
  - NOTE (shown after choosing): Short, dated, factual. Let the file correct itself out loud.
- Raise it by phone at the next check-in instead → **shift_conflict**
  - NOTE (shown after choosing): Your caseworker says she'll look into it, and means it. The file records neither the asking nor the answer.

## [shift_conflict] The Overtime Shift
*Day 52 — Thursday, June 25, 2026 — Thursday, June 25, 2026 (dayOffset 52)*

Session eleven falls on the same evening as a double shift that would pay time-and-a-half — real money, in a summer when the car has begun making a noise you are budgeting around.

A coworker offers a trade: he will take your Saturday warehouse shift if you take his Sunday. The class stays attended; the weekend gets shorter; the money gets smaller. Every option in this scene is defensible. Only one of them is a signature on a sign-in sheet.

**Choices:**
- Make the trade and attend session eleven → **progress_review**  _(cash −30; HIDDEN + Parenting program — session 11 of 12 attended, signed in)_
  - NOTE (shown after choosing): Eleven of twelve. The pattern, in ink, is starting to look like the parent you are describing.
- Take the double shift and miss session eleven → **progress_review**  _(cash +50; HIDDEN + Parenting program — session 11 missed; reason not filed)_
  - NOTE (shown after choosing): The money is real. So, in September, will be the summary's way of counting.

## [progress_review] The Interim Review
*Day 59 — Thursday, July 2, 2026 — Thursday, July 2, 2026 (dayOffset 59)*

The interim permanency review is short, and mostly Track A: your attendance, your screens, your visits, the plan's rating word — progressing — said aloud by the agency's own witness.

Then the agency's lawyer, in the tone of a person reading a train schedule, notes for the record that the goal-change request remains pending for September, and that the fifteen-month date arrives the same week.

Two cases, one child, one courtroom, described sixty seconds apart as if they were about different families.

**Choices:**
- Watch Ms. Osei, and let her do the thing you prepared → **which_track**
  - NOTE (shown after choosing): She stands. This is the beat the whole summer has been rehearsing.

## [which_track] Which Track Does That Belong To?
*Day 66 — Thursday, July 9, 2026 — Thursday, July 9, 2026 (dayOffset 66)*

Ms. Osei asks, on the record, a question so plain it sounds procedural: when the agency describes your progress as ‘progressing,’ which track is that evidence on — and when it describes the calendar as pressing, which track is that on? And may the record show the two timelines side by side, as filed?

The judge says yes. Court reporters write down what judges say yes to. From today, the official story of your case has two columns in it, and anything said about one column can be answered from the other.

Your caseworker catches your eye on the way out and says, honestly: “I do the services side. The goal side comes from above me.” You believe her. Both things she said are now, in different ways, on the record.

**Choices:**
- Thank her — and keep attending the services side as if it were the whole case → **screens_filed**  _(HIDDEN + Hearing record — two timelines stated side by side; progress evidence assigned to both tracks)_
  - NOTE (shown after choosing): Because stopping, now, would be read as surrender on both tracks at once.
- Ask her, in the hallway only, whether she personally supports the goal change → **screens_filed**
  - NOTE (shown after choosing): She looks at the floor. “I'm the services side,” she says again. Hallways are not the record. You knew that; now you know you know it.

## [screens_filed] Clean Screens, Filed
*Day 70 — Monday, July 13, 2026 — Monday, July 13, 2026 (dayOffset 70)*

Your screen results for the summer arrive at the agency on the provider's schedule, which is to say late, in a batch, covering weeks you lived one at a time.

Clean, all of them — as you knew, and as the file, until the batch landed, could not have said. Evidence that exists somewhere is not the same as evidence that exists in the record, and the distance between those two places is measured in exactly this kind of envelope.

Ms. Osei files a one-line notice attaching the batch to your progress statement, so the results join the column they belong to.

**Choices:**
- Ask her to attach them to the two-timeline page as well → **assessment_pages**  _(HIDDEN + Screens — summer batch clean, filed and attached to the timeline statement)_
  - NOTE (shown after choosing): One fact, filed in both columns. September will not have to go looking for it.

## [assessment_pages] The Assessment Pages
*Day 73 — Thursday, July 16, 2026 — Thursday, July 16, 2026 (dayOffset 73)*

The rest of your requested record arrives in a second envelope: the assessment, this time with its workings — the form, the item ratings, the outcome line — and a cover note updating two items since spring in light of your filed progress.

Read closely, the form is neither a verdict nor a villain. It rated what it was shown, when it was shown it. Where the file has grown — attendance, tenancy, visits — the ratings tied to those items have moved. Where the file is silent, the ratings have simply waited.

Ms. Osei restates the flag for your folder's cover sheet: whether the adjudication-phase disclosure rule (Pa.R.J.C.P. 1340(B)(1)) reaches every scored item of a form like this is untested; your copy came through the direct record request, which “shall be released upon request” (55 Pa. Code § 3130.44(d)). How you got it matters less, in the end, than that you are no longer the only person in the case who has not seen it.

**Choices:**
- Go through it with Ms. Osei, item by item, and note which items your last month can still move → **foster_home_meeting**  _(HIDDEN + Assessment — form, item ratings and outcome read by parent with counsel before the hearing)_
  - NOTE (shown after choosing): A form read in July can be answered in August. A form first seen in September can only be endured.

## [foster_home_meeting] Coffee at the Foster Home
*Day 80 — Thursday, July 23, 2026 — Thursday, July 23, 2026 (dayOffset 80)*

The Hartleys invite you for coffee after a visit — a first. Their kitchen has Lark's height marks on the door frame, in pencil, in a hand that is not yours. It hurts in the ordinary way true things hurt, and you stay, and you drink the coffee.

Mrs. Hartley says they did not ask for the goal to change; the agency asked them whether they would be a permanency resource “if it ever came to that,” and they said yes because saying no felt like abandoning Lark a second way. Mr. Hartley says: “Nobody in this kitchen is your enemy, Marcus.”

You believe them. That is the difficult part the movies leave out: Track B is not staffed by villains. It is staffed by kind people answering the questions they were asked, in the order they were asked them.

**Choices:**
- Thank them, and ask that Lark's visit routine stay exactly as it is while the court decides → **plan_checkpoint**  _(HIDDEN + Foster-home meeting — placement stable; visit routine to continue by agreement)_
  - NOTE (shown after choosing): Stability for Lark, continuity for you, civility for the record. Some sentences do three jobs.
- Ask them directly whether they would adopt her → **plan_checkpoint**
  - NOTE (shown after choosing): “If a judge ever decided she needed that, yes,” Mrs. Hartley says, carefully. “We answered the question we were asked.” Now you have heard Track B in its own words.

## [plan_checkpoint] Nine of Twelve, Corrected
*Day 87 — Thursday, July 30, 2026 — Thursday, July 30, 2026 (dayOffset 87)*

The agency's draft report for September arrives at Ms. Osei's office. It is mostly current — and it describes your parenting program, in one flat line, as “nine of twelve sessions completed.”

Nine was true in May. Your folder holds sign-in copies for sessions ten and eleven, and session twelve — the last — is still ahead of you, in August. Draft reports have a way of becoming final reports, and final reports have a way of becoming the past.

**Choices:**
- Have Ms. Osei send the correction this week, with the sign-in copies attached → **summer_visit**  _(FLAG: recordCorrected; HIDDEN + Draft report corrected before the hearing — attendance current, with sign-in copies)_
  - NOTE (shown after choosing): Corrected on paper, before the hearing, the error never gets to testify.
- Leave it — the real certificate will be there by September anyway → **summer_visit**
  - NOTE (shown after choosing): It will. Whether September's summary is written from the certificate or from the draft is a coin currently spinning.

## [summer_visit] The Long Visit
*Day 94 — Thursday, August 6, 2026 — Thursday, August 6, 2026 (dayOffset 94)*

August's long visit is the best one yet: a whole day, a picnic Lark planned with the seriousness of a state occasion, and a goodbye she manages by explaining, to both households, the rules of the drawing homework she has assigned.

On the bus home you understand, clearly and without drama, the arithmetic of concurrent planning from the inside: every good day like this is, at the same time, a day of Track A working and a day of Lark settling deeper into the home on Track B. The same day. The same drawing. Two columns.

The work is not to stop the day from meaning both things. The work is to make sure the record can hold both meanings at once.

**Choices:**
- Write the visit up in your folder that night, dated, while it is still warm → **birthday**
  - NOTE (shown after choosing): Contemporaneous is a cold word for a warm practice: write it while it's true in detail.

## [birthday] Seven Candles, Counted Twice
*Day 98 — Monday, August 10, 2026 — Monday, August 10, 2026 (dayOffset 98)*

Lark turns eight in August, and there are, without anyone planning it as a symbol, two small celebrations — one at the Hartleys', one at your visit — and she reports each to the other household with a diplomat's completeness.

She asks you, at yours, whether she will have “two birthdays forever.” You tell her the truth at her size: grown-ups are working out where home is, a judge helps decide, and everyone at both parties loves her in the same direction.

It is the truest available sentence. You write it down anyway when you get home, because dates and sentences are what September is made of.

**Choices:**
- Go to the last class, and finish the plan's classroom piece → **last_class**
  - NOTE (shown after choosing): One session left. Endings, even small ones, should be signed in.

## [last_class] The Twelfth Session
*Day 105 — Monday, August 17, 2026 — Monday, August 17, 2026 (dayOffset 105)*

Session twelve. The facilitator hands out certificates with the gravity of a commencement and the refreshments of a church basement, and yours says what the sign-in sheets have been saying all summer: completed.

She writes a line on the back of yours, unprompted: “Attended every session from ten onward under a goal-change motion. Did the work while the ground moved.” It is not a legal document. You file it like one.

**Choices:**
- Take the certificate straight to Ms. Osei's office → **counsel_letter**  _(HIDDEN + Parenting program — completed, certificate in the court file)_
  - NOTE (shown after choosing): Twelve of twelve. One Track A line, closed, in writing, before the hearing that decides the other track.

## [counsel_letter] A Letter Meant for the File
*Day 107 — Wednesday, August 19, 2026 — Wednesday, August 19, 2026 (dayOffset 107)*

On the last business day before the strategy meeting, Ms. Osei files a short letter that does almost nothing — and that, she explains, is its job. It confirms, with dates, the plan's current state: program completed, screens current, tenancy stable, visits running, and the two timelines as previously filed.

“September should contain no factual surprises about you,” she says. “Surprises are what the other track is for. Our track arrives pre-read.”

It is the sound of a record being closed neatly, one week early, on purpose.

**Choices:**
- Read the filed copy once more, and then go home and sleep → **strategy_choice**  _(HIDDEN + Counsel's confirmation letter filed — plan state current and dated before the hearing)_
  - NOTE (shown after choosing): Tomorrow you choose the lead argument. Everything it could lead with is already in the file.

## [strategy_choice] Choosing the Lead Argument
*Day 108 — Thursday, August 20, 2026 — Thursday, August 20, 2026 (dayOffset 108)*

In the last stretch before the hearing, Ms. Osei spreads the summer on her conference table: the filed timelines, the assessment pages, the corrected attendance, the certificate, and — if you found it and wrote about it — one service-plan page with an empty box.

September 2 is both the hearing and the fifteen-month date. The agency will argue the calendar. The Hartleys' willingness will be in the file. Your progress will be in the file too, in whatever form the summer left it.

“We lead with one argument,” she says. “Choose like a person who has to live inside the outcome — because both of you do.”

**Choices:**
- Lead with the services gap — the plan's own necessary step, never provided, documented → **path_services**
  - NOTE (shown after choosing): The exception built from the agency's own page.
- Lead with the documented compelling reason — the whole current Track A record, filed and dated → **path_compelling**
  - NOTE (shown after choosing): A reason, documented, for why filing on this date would not serve Lark.
- File a full written statement preserving every exception — and let the goal argument fall where it falls → **path_written**
  - NOTE (shown after choosing): A colder strategy: lose the label if you must, keep the argument for the stage that may come.
- Keep your head down — 'progressing' should speak for itself → **path_thin**
  - NOTE (shown after choosing): Ratings speak in summaries. September will be conducted in documents.

## [path_services] The Empty Referral Box, in a Letter
*Day 112 — Monday, August 24, 2026 — Monday, August 24, 2026 (dayOffset 112)*

The filing is short: the plan page, the empty box, the dates. The service was identified by the agency itself as necessary for Lark's safe return — the step toward unsupervised visits. It was marked “to be sent” in month six. It was never sent. Your letter asked for it, in writing; the referral was made at last in August, a year late, and the August confirmation is attached too, because fairness is also a record.

Ms. Osei's covering words are plain: the third exception in the federal rule exists for exactly this shape of fact (42 U.S.C. § 675(5)(E)) — a State that has not provided the services it identified as necessary should not be able to run the fifteen-month clock as if it had.

**Choices:**
- Go to the hearing with the exception documented, not just discovered → **hearing_services**  _(FLAG: exceptionDocumented)_
  - NOTE (shown after choosing): A fact, filed early, with its dates on it.

## [path_compelling] The Documented Reason
*Day 112 — Monday, August 24, 2026 — Monday, August 24, 2026 (dayOffset 112)*

The filing assembles the paper summer into one argument: a completed plan but for time, a certificate, clean screens, a stable tenancy, visits grown long and ordinary, the two timelines stated side by side since the interim review — a documented case that changing the goal, and filing on the fifteen-month date, would not serve Lark, who is thriving in part because her father's case is alive.

It does not ask the court to feel anything. It asks the court to write one sentence — a compelling reason, documented in the case plan — and to leave Track A's finish line where the evidence says it nearly is.

**Choices:**
- Go to the hearing with the reason documented, not just felt → **hearing_compelling**  _(FLAG: exceptionDocumented)_
  - NOTE (shown after choosing): One sentence is all you need. Sentences, in files, are load-bearing.

## [path_written] Preserving the Argument
*Day 112 — Monday, August 24, 2026 — Monday, August 24, 2026 (dayOffset 112)*

Your written statement goes in whole: progress, timelines, the assessment pages, every exception the record supports — including, if the summer found it, the owed referral, with dates. It concedes nothing. It also, deliberately, spends less of itself on the goal label than on making sure that nothing the agency may argue later, at any termination stage that may come, can be said to have gone unanswered now.

Ms. Osei is honest about the trade: “This protects the next hearing better than it wins this one. A termination case, if it is ever filed, is decided on proof the agency would have to carry clearly and convincingly — and this statement would be sitting in the record it has to carry it against. But September may still change the goal.”

**Choices:**
- File it, and go to the hearing knowing exactly what it does and doesn't do → **hearing_written**  _(FLAG: argumentPreserved)_
  - NOTE (shown after choosing): A record position, held on purpose, with open eyes.

## [path_thin] Head Down, Again
*Day 112 — Monday, August 24, 2026 — Monday, August 24, 2026 (dayOffset 112)*

The last week of August is a good week, taken singly. A visit that sings. A certificate on the refrigerator. A child who assigns drawing homework like a small, confident state.

What does not happen: paper. No lead argument is filed, no exception is documented, no statement goes in. The file the judge will open on September 2 is the file as the system wrote it — a good father, an unfinished plan, a willing resource family, and a federal date arriving exactly on schedule.

You have done the work. September's question is narrower than the work: not what you have done, but what is documented as a reason.

**Choices:**
- Go to the hearing with your folder and your summer → **hearing_thin**
  - NOTE (shown after choosing): The folder is real. Whether the court can use it depends on whether it became the court's paper too.

## [hearing_services] The Fifteen-Month Hearing — The Services Record
*Day 121 — Wednesday, September 2, 2026 — Wednesday, September 2, 2026 (dayOffset 121)*

September 2, 2026. Fifteen months, to the day the statute counts from. The agency argues the calendar first, as Ms. Osei predicted: the date has arrived, a resource family is willing, permanency should not wait.

Then the record answers, in its two columns. Track A: completed, current, filed. Track B's own foundation: a step the plan called necessary, marked to be sent in month six, sent in month fourteen — after a parent found the empty box in his own file and asked about it in writing. The agency's lawyer, to her professional credit, does not contest the dates.

The judge looks at the timeline page — the one filed in June, the one stated on the record at the interim review — for a long moment. “The clock,” she says, “is supposed to measure the case. It is not supposed to replace it.”

**Choices:**
- Listen to the order, in the order the judge gives it → **end_denied**
  - NOTE (shown after choosing): Goal first. Then the sentence about the exception. Then the services, ordered made at last, with dates.

## [hearing_compelling] The Fifteen-Month Hearing — The Paper Summer
*Day 121 — Wednesday, September 2, 2026 — Wednesday, September 2, 2026 (dayOffset 121)*

September 2, 2026. The agency argues the calendar, the settling-in, the willing resource — a real argument, made by people who also have a file.

But this summer, the file has two authors. The court works through the filed record: the certificate, the corrected attendance, the assessment items that moved when the file grew, the timelines stated side by side since the interim review. The agency's own rating word, progressing, is no longer a summary floating free of its evidence; the evidence is attached, dated, and current.

The judge asks the agency one question — “What, on this record, remains undone that time will not finish by the next review?” — and the room is quiet in a way that is itself an answer.

**Choices:**
- Listen to the order, in the order the judge gives it → **end_denied**
  - NOTE (shown after choosing): Denied and deferred are cousins. Today, either word keeps Track A's finish line where it was.

## [hearing_written] The Fifteen-Month Hearing — Granted, with a Record
*Day 121 — Wednesday, September 2, 2026 — Wednesday, September 2, 2026 (dayOffset 121)*

September 2, 2026. The court changes the goal. The words land the way Ms. Osei warned they might: Lark's settled life, the calendar, the resource family's willingness — weighed, on the day, more heavily than a father's nearly-finished plan.

And then the judge does the second thing, the one your summer built: she notes, on the record, the parent's filed statement and the exceptions it documents, unanswered in their particulars, and directs that they remain part of the record for any later stage. No termination petition has been filed. If one ever is, it will be read against a record that was being written, on purpose, since May.

You walk out with a changed goal and an unchanged file of your own making. Both facts are true. The strategy was built to hold the second one when the first one went the other way.

**Choices:**
- Ask Ms. Osei, in the hallway, exactly what was preserved and what happens next → **end_preserved**
  - NOTE (shown after choosing): “Your argument,” she says. “Intact, dated, and theirs to answer. That was the design.”

## [hearing_thin] The Fifteen-Month Hearing — Changed
*Day 121 — Wednesday, September 2, 2026 — Wednesday, September 2, 2026 (dayOffset 121)*

September 2, 2026. The hearing is shorter than the summer deserved. The agency's summary is fair and even warm — and a summary is all it is: a progressing father, an unfinished plan, a date arrived, a family willing.

Your folder is on your lap, with the visit notes you wrote warm, the sentence from the front door you did or did not write down, the progress you made and mostly did not file. The judge can only rule on the record in front of her, and the record in front of her has one column filled in by the system and the other mostly in pencil, at home.

The goal is changed. The judge, reading the room with care, adds the part that is still yours to decide: reunification services will continue for now, and reviews will continue, and what the file says by the next one is — as it has always been — partly up to the people in this room.

**Choices:**
- Keep going — attend everything, exactly as before, with the goal changed above you → **end_changed_services**  _(FLAG: keptAttending)_
  - NOTE (shown after choosing): Track A, still running, on a track the court has renamed. Attendance is now the loudest sentence in your file.
- Stop going — if the finish line moved, the running was the lie → **end_collapse**
  - NOTE (shown after choosing): It is the most understandable choice in this scenario. It is also the one September's summary, next time, will be written from.

## [end_denied] Ending — Goal Change Denied, Exception Documented
*Day 135 — Wednesday, September 16, 2026 — Wednesday, September 16, 2026 (dayOffset 135)*

**Ending.**

**Debrief:**
- WHAT THE RECORD HELD (the hidden record, revealed): Underneath this path sat a two-column file: a Track A record that was current because its author filed it — attendance corrected before it could testify wrongly, a certificate in the file before the hearing, timelines stated side by side on the record since the interim review — and, on the path that found it, an empty referral box: a service the plan called necessary, marked 'to be sent' in month six and sent in month fourteen, after the parent asked in writing. September did not turn on whether you are a good father. It turned on which facts existed in the court's paper, dated, by September 2.
- THE LAW UNDER THIS PATH: At 15 of the most recent 22 months in care, the agency is pressed to file a petition to terminate parental rights — unless an exception applies (42 U.S.C. § 675(5)(E)): the child is being cared for by a relative; a compelling reason that filing would not be in the child's best interest is documented in the case plan; or the agency has not provided the services the plan identified as necessary for the child's safe return. Your hearing documented an exception and denied or deferred the goal change on a current Track A record; counsel was your right throughout (42 Pa.C.S. § 6337), and the record that made it possible began with a request the regulation answers in five words — it 'shall be released upon request' (55 Pa. Code § 3130.44(d)). Nothing today ends the case: reviews continue, and the plan's remaining work still has to be finished, by you and — now with dates attached — by the agency.
- THE HONEST PART: This is a deferral with homework, not a rescue, and it was not produced by effort alone. A different judge could have weighed Lark's settled year more heavily on the same paper; a referral sent on time would have removed the strongest document in the file; a foster family less kind could have rewritten every visit scene. Workers, judges, an unchecked box, and luck all hold pieces of this outcome. What your choices changed was the record those pieces landed on — two columns, current, impossible to summarize honestly using only one of them.

## [end_preserved] Ending — Goal Changed, the Argument Preserved
*Day 135 — Wednesday, September 16, 2026 — Wednesday, September 16, 2026 (dayOffset 135)*

**Ending.**

**Debrief:**
- WHAT THE RECORD HELD (the hidden record, revealed): A changed goal, and underneath it a written statement that went in whole and early: your progress with its proofs, the two timelines side by side, and every exception the record supports, with dates, unanswered in their particulars and now noted by the court as part of the record for any later stage. The label moved. The argument did not. That was the strategy, and it is important to say plainly what it is: a record position, not a custody outcome.
- THE LAW UNDER THIS PATH: A goal change is not a termination. No petition has been filed in this ending, and if one ever is, the agency would have to prove its grounds by clear and convincing evidence at a hearing where your preserved record — including the documented services question under 42 U.S.C. § 675(5)(E) — would be part of what that proof must answer. Your statement sits in the file because you filed it while filing was yours to choose; your knowledge of what to preserve began with your own record, released on request (55 Pa. Code § 3130.44(d)), and your counsel's right to build it with you is the right the law gave you at the start (42 Pa.C.S. § 6337).
- THE HONEST PART: Preserved is not won, and this debrief will not pretend otherwise: Lark tonight is in the same home, under a goal that no longer names yours. What the record buys is a fairer next hearing, if there is one — and fairer next hearings are sometimes all a summer can buy. A different judge might have denied the change outright on this paper; this one didn't. Judges, workers, the Hartleys' honest kindness, and the luck of an unchecked box are all in this ending alongside your work. The work was to make sure that if the future case is ever built, it must be built over your words too — dated, filed, and already there.

## [end_changed_services] Ending — Goal Changed, Services Continue
*Day 135 — Wednesday, September 16, 2026 — Wednesday, September 16, 2026 (dayOffset 135)*

**Ending.**

**Debrief:**
- WHAT THE RECORD HELD (the hidden record, revealed): A goal changed on a thin record — and one order inside the order that matters more than it looks: reunification services continue. The court said so because a father in the room, on the worst day of his case, was still plainly a father in the middle of one: attending, visiting, unfinished rather than unwilling. What had not been filed could not be weighed. What had been lived could still be seen, just, in the man himself.
- THE LAW UNDER THIS PATH: A goal change redirects a case; it does not terminate rights, and it does not by itself end services — here the court ordered them continued while reviews continue, which is concurrent planning's dual track running in its other direction: services toward reunification maintained while an alternative future is planned (the structure the whiteboard drew in May). If you disagree with the order, there are further steps a party can take after a permanency decision; this game does not put a number on that window — ask Ms. Osei today, in person, what it is and when it runs from, because windows like that are exactly the kind that close while a parent is deciding how they feel. The fifteen-month filing question (42 U.S.C. § 675(5)(E)) also remains alive, with its exceptions, and a record can still be built toward them — beginning, as it always can, with your own file, which 'shall be released upon request' (55 Pa. Code § 3130.44(d)).
- THE HONEST PART: This ending is the system working at half its promise: the services survive because a judge chose to order them, on a day when a fuller record might have made the order unnecessary to beg for. Your continued attendance from here is not a technicality — it is the entire remaining argument, made weekly, in sign-in ink. Plenty of parents in this room of an ending rebuild the record by the next review; plenty of identical effort, in front of a different judge on a different day, does not get the services order at all. Workers, judges, and luck signed this outcome with you. Your signature, weekly, is the part still being written.

## [end_collapse] Ending — The Quiet Collapse
*Day 142 — Wednesday, September 23, 2026 — Wednesday, September 23, 2026 (dayOffset 142)*

**Ending.**

**Debrief:**
- WHAT THE RECORD HELD (the hidden record, revealed): Nothing new — and that is the ending. In the weeks after the goal changed, the sign-in sheets stop, the visit bag stops traveling, and the file, which is written from attendance and paper, begins describing an absence it did not create. By the next review, the summary can say, truthfully and completely misleadingly, that the parent disengaged after the goal change. The plan did not collapse in a hearing. It lapsed, one un-attended Tuesday at a time, in a church basement that kept meeting without you.
- THE LAW UNDER THIS PATH: Legally, almost everything that was true in September is still true: no termination has been decided, services were ordered to continue, reviews continue, and the exceptions in the federal rule (42 U.S.C. § 675(5)(E)) do not expire with a parent's hope. Practically, the case now runs on the only evidence still being generated — other people's. A record can be rebuilt from almost any week a parent chooses to restart it; counsel remains your right (42 Pa.C.S. § 6337), and your own file remains yours on request (55 Pa. Code § 3130.44(d)). What cannot be rebuilt is the appearance, in the summaries, of the weeks when nothing was filed and nothing was attended. Gaps are also a record. They testify in every later room.
- THE HONEST PART: No one who has sat in that courtroom should be surprised by this ending, and this debrief does not judge it: the goal change told a man, in legal language, that the running no longer counted, and he believed the language instead of the whiteboard. Stopping reads as surrender because the file has no column for grief. It has a column for attendance. Workers who might have called, a judge who might have kept the goal, a referral sent on time — the same luck and people run through this ending as through the good ones. The difference is that in this one, the parent's own hand leaves the page, and the page goes on being written without it.
