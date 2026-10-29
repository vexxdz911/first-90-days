# THE FIRST 90 DAYS — Scenario 132: “The Hearing That Read the Year”

*Human-readable script. This document and `scenario-132.json` are generated from a single source and match node-for-node: same IDs, same order, same choices, same effects.*

**The family is fictional — a composite. No real person's story appears here.**

**Content note:** This scenario depicts a long-running dependency case culminating in a permanency hearing. There is no graphic content. Players may skip any scene or use the quick exit at any time.

**How to read effects:** `cash −40` changes the player's cash. `FLAG: name` sets a flag the engine tracks. `HIDDEN + item` means the case file quietly records that item at this choice — the player does not see it when it happens. `REQUIRES FLAG: name` means the choice is only available if that flag was set earlier; `REQUIRES NO FLAG: name` means it is only available if that flag was never set. `NOTE:` is text shown to the player right after choosing.

Start date: Monday, August 4, 2025. Day offsets are days since the scenario's start date (the child's foster-care entry date).

## [start] Month Fourteen, Minus One
*Day 371 — Monday, August 10, 2026 (dayOffset 371)*

Your name is Eneko. Your daughter Maialen, five, entered foster care on Monday, August 4, 2025, when you were hospitalized after the accident at the warehouse and there was, for one weekend, no adult standing between her and the system's default answer. You stood up again by Friday. The case, once opened, did not close on the same schedule.

Now it is month thirteen, and the court has set the hearing that the whole case has been walking toward: the permanency hearing of Monday, October 12, 2026 — just past Maialen's fourteen-month mark, with her fifteenth month (Wednesday, November 4, 2026) visible on the horizon like weather. Your lawyer, Mr. Baptiste, puts it plainly: 'Hearings like this are not won at the hearing. They are read there. We have two months to finish the book.'

**Choices:**
- Treat the month as a production schedule: every document, dated, filed, indexed → **pro_a**  _(FLAG: productionSet ; HIDDEN + Hearing production schedule set with counsel)_
  - NOTE (shown after choosing): A hearing is a reading. You are finishing the book it will read.
- Prepare to testify well — this is finally your day in court → **pro_a**
  - NOTE (shown after choosing): It is your day. The court will spend most of it reading. Feed the reading.

## [pro_a] Fourteen Months in One Sentence
*Day 372 — Tuesday, August 11, 2026 (dayOffset 372)*

If the case had a sentence it would be this: a man was hurt at work, a child was safe with strangers within the week, and everything since has been the paperwork of proving the first fact no longer governs the second.

Mr. Baptiste does not deal in sentences. He deals in tabs. But he lets you keep yours, at the front of the folder, where the packet's first page will go.

**Choices:**
- Carry the page to its file → **pro_b**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the record)_
  - NOTE (shown after choosing): Dated, copied, filed — the chain holds.
- Trust the conversation to carry it → **pro_b**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [pro_b] The Horizon, Named
*Day 374 — Thursday, August 13, 2026 (dayOffset 374)*

November 4, 2026 is named aloud in the first meeting — the fifteenth month, said early so it can be answered early. Dates that are feared in whispers run cases. Dates on whiteboards get managed.

The whiteboard gains a second line: September 14, the hearing. Between the two dates lies the whole strategy: be read before you can be filed against.

**Choices:**
- Carry the page to its file → **production**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the record)_
  - NOTE (shown after choosing): Dated, copied, filed — the chain holds.
- Trust the conversation to carry it → **production**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [production] The Inventory of a Year
*Day 376 — Saturday, August 15, 2026 (dayOffset 376)*

The inventory of the year's paper, spread on Mr. Baptiste's table: the visit logs (fifty-one weeks, two signatures), the treatment completion letter, the employer's accommodation schedule, the pediatrician's paragraph, the housing file, the record you requested last winter under 55 Pa. Code § 3130.44(d), your written responses to the two referral gaps, the kinship study of Maialen's aunt — approved, then held as the family's reserve.

And the gaps in the inventory, listed as honestly: one missing month of visit notes (the supervisor's rotation), and the exception question nobody has yet made the agency answer in writing.

**Choices:**
- List the gaps as tasks with owners and dates, not as worries → **inv_a**  _(FLAG: gapList ; FLAG: recordsRequested ; HIDDEN + Hearing inventory built; gaps listed as dated tasks)_
  - NOTE (shown after choosing): Worries pace. Tasks get done.
- The record is strong — don't let the perfect audit the good → **inv_a**
  - NOTE (shown after choosing): The audit is the good, at capstone weight. One missing month is a door the other side will open.

## [inv_a] Tabs, Numbered
*Day 377 — Sunday, August 16, 2026 (dayOffset 377)*

The packet's tabs are numbered in the order a judge reads a life: placement, visits, treatment, work, housing, school, kin, and last — by design — the questions the agency has not answered.

Order is argument. A packet that begins with compliance and ends with an unanswered letter tells its story before a word is spoken.

**Choices:**
- Carry the page to its file → **inv_b**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the record)_
  - NOTE (shown after choosing): Dated, copied, filed — the chain holds.
- Trust the conversation to carry it → **inv_b**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [inv_b] The Copies
*Day 379 — Tuesday, August 18, 2026 (dayOffset 379)*

Three copies: the court's, counsel's, yours — plus the working set that lives in the car, because hearings have been known to lose paper and this family has stopped being surprised by physics.

Redundancy is the folder's religion. It has never yet been wrong to practice it.

**Choices:**
- Carry the page to its file → **gap_tasks**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the record)_
  - NOTE (shown after choosing): Dated, copied, filed — the chain holds.
- Trust the conversation to carry it → **gap_tasks**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [gap_tasks] The Missing Month
*Day 381 — Thursday, August 20, 2026 (dayOffset 381)*

The missing visit notes belong to October 2025, when the visit supervisor rotated and the new one's notes were 'to be uploaded.' The visits happened — Maialen's foster mother, Ms. Grey, kept her own calendar, as the careful ones do, with your arrivals in her handwriting.

A fact that happened and a fact the file can show are cousins, not twins. The cure for a gap in one file is a document from another: Ms. Grey's calendar, copied, signed, and filed with a one-page explanation.

**Choices:**
- Ask Ms. Grey for the calendar pages and file them with the explanation → **mir_a**  _(cash −5 ; FLAG: gapCured ; HIDDEN + Missing visit month cured from the foster caregiver's own calendar)_
  - NOTE (shown after choosing): Another chair's record, rescuing yours. Files are ecosystems.
- Skip October — one month in fourteen can't decide a hearing → **mir_a**
  - NOTE (shown after choosing): One month is exactly the size of the question the agency will ask: 'What happened in October?' Answer it with paper or with weather.

## [mir_a] October, Reconstructed on Paper
*Day 382 — Friday, August 21, 2026 (dayOffset 382)*

Before asking Ms. Grey, you reconstruct October from your own artifacts: the pay stubs showing the shift pattern, the text messages setting each visit, the gas receipt from the foster home's side of town. The month existed. It simply lived in the wrong drawers.

The reconstruction is filed as an appendix, so the calendar, when it comes, corroborates instead of rescues.

**Choices:**
- Carry the page to its file → **mir_b**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the record)_
  - NOTE (shown after choosing): Dated, copied, filed — the chain holds.
- Trust the conversation to carry it → **mir_b**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [mir_b] The Rotation, Explained by Its Author
*Day 384 — Sunday, August 23, 2026 (dayOffset 384)*

The rotated-out supervisor, reached by a polite letter, replies with the sentence the gap needed: the notes were kept, the upload was not, the failure was administrative and hers. It is filed without triumph. Systems that admit their gaps in writing are doing, late, the thing the file asked of you on time.

October now has three documents where it had a rumor. The gap is becoming a paragraph.

**Choices:**
- Carry the page to its file → **grey_calendar**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the record)_
  - NOTE (shown after choosing): Dated, copied, filed — the chain holds.
- Trust the conversation to carry it → **grey_calendar**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [grey_calendar] The Exception Question, In Writing
*Day 386 — Tuesday, August 25, 2026 (dayOffset 386)*

Mr. Baptiste drafts the letter the year has been pointing at: a short request that the agency state, in writing, its position on the fifteen-month question — whether it will file, and if not, which exception it will document: relative care, a case-plan compelling reason, or services identified but not provided (42 U.S.C. § 675(5)(E)).

Agencies answer letters like this slowly and sometimes not at all. Both responses are evidence. A documented silence, at a hearing, is a exhibit with a date on it.

**Choices:**
- Send it by a method that proves delivery, and calendar the silence → **cure_a**  _(cash −5 ; FLAG: exceptionAsked ; HIDDEN + Agency asked in writing to state its fifteen-month exception position)_
  - NOTE (shown after choosing): The letter asks the question the hearing will ask. Their answer, or its absence, joins the book.
- Save the question for cross-examination — surprise has value → **cure_a**
  - NOTE (shown after choosing): Surprise has value in trials. In permanency hearings, foreshadowed questions with unanswered letters have more.

## [cure_a] The Calendar, Copied at the Kitchen Table
*Day 388 — Thursday, August 27, 2026 (dayOffset 388)*

Ms. Grey spreads the calendar flat and you copy it together, her handwriting becoming the packet's most human page: arrivals, departures, one rained-out picnic rescheduled in pencil with an exclamation point she apologizes for.

You do not accept the apology. The exclamation point is the most credible mark in the file.

**Choices:**
- Carry the page to its file → **cure_b**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the record)_
  - NOTE (shown after choosing): Dated, copied, filed — the chain holds.
- Trust the conversation to carry it → **cure_b**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [cure_b] The Explanation, One Page
*Day 391 — Sunday, August 30, 2026 (dayOffset 391)*

The one-page explanation is drafted to say exactly three things: the visits happened, the notes were not uploaded, here is the corroboration. No adjectives about the agency, no adjectives about anyone. Explanations that accuse read as defenses; explanations that document read as records.

It is filed with the calendar and the supervisor's letter. October is closed.

**Choices:**
- Carry the page to its file → **exception_letter**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the record)_
  - NOTE (shown after choosing): Dated, copied, filed — the chain holds.
- Trust the conversation to carry it → **exception_letter**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [exception_letter] The Record, Refreshed
*Day 395 — Thursday, September 3, 2026 (dayOffset 395)*

The case record has grown since winter; you request the updated record in writing (55 Pa. Code § 3130.44(d)), because arguing from a nine-month-old mirror at a fourteen-month hearing is how parents get surprised by their own files.

The refresh arrives with the redactions the rule provides (55 Pa. Code § 3130.44(f)) and one new page: the agency's internal note that your exception letter was 'received and under review.' Under review is the system's favorite tense. It is also, now, a dated fact.

**Choices:**
- Index the refresh into the packet and note the exception letter's status by date → **wait_a**  _(FLAG: recordRefreshed ; HIDDEN + Updated case record requested and indexed before the hearing)_
  - NOTE (shown after choosing): The book, current edition. The hearing will read nothing older than your preparation.
- The winter record plus your folder is enough → **wait_a**
  - NOTE (shown after choosing): Enough is a number the other side gets to test. Refresh the mirror.

## [wait_a] The Silence, Calendared
*Day 397 — Saturday, September 5, 2026 (dayOffset 397)*

Week one of the silence is noted. Week two is noted. The noting is the strategy: an unanswered question with dates on it becomes, at the hearing, a short speech the other side must sit through.

Mr. Baptiste has given the speech before, in other cases, about other letters. He describes it as 'the sound of a file being read carefully.'

**Choices:**
- Carry the page to its file → **wait_b**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the record)_
  - NOTE (shown after choosing): Dated, copied, filed — the chain holds.
- Trust the conversation to carry it → **wait_b**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [wait_b] The Refresh, Requested Meanwhile
*Day 399 — Monday, September 7, 2026 (dayOffset 399)*

The record refresh is requested during the silence — timing as housekeeping, so the newest pages arrive with the hearing still a month out and surprises have time to become exhibits or corrections.

Nothing in the refresh is allowed to be new at the hearing. That is the refresh's whole job.

**Choices:**
- Carry the page to its file → **refresh_indexed**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the record)_
  - NOTE (shown after choosing): Dated, copied, filed — the chain holds.
- Trust the conversation to carry it → **refresh_indexed**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [refresh_indexed] Maialen's School Page
*Day 402 — Thursday, September 10, 2026 (dayOffset 402)*

Maialen started kindergarten in August, at the school two streets from your apartment — the placement's geography having accidentally served the reunification plan. Her teacher's letter is the file's newest voice: attendance, adjustment, 'asks for her dad at pickup-story time, in the tone of a child expecting him.'

Collect the voices with no stake. They are the chorus the hearing trusts most, because they wanted nothing from the case except a child educated.

**Choices:**
- File the teacher's letter and the attendance record → **winter_a132**  _(FLAG: schoolFiled ; HIDDEN + Kindergarten teacher's letter and attendance filed)_
  - NOTE (shown after choosing): The chorus gains its youngest-voiced member. Filed, not mentioned.
- The teacher's letter can be mentioned in testimony → **winter_a132**
  - NOTE (shown after choosing): Mentioned letters are rumors with good reputations. File it.

## [winter_a132] The Winter Choir
*Day 404 — Saturday, September 12, 2026 (dayOffset 404)*

The refreshed record's winter pages confirm the inventory: the treatment provider's mid-course letter, already filed, already dated, saying the unspectacular things mid-course letters say — attendance, engagement, prognosis guarded and good.

Choruses are built a voice at a time. This one joins the folder without ceremony, which is its credibility.

**Choices:**
- File it and note its date in the inventory → **winter_b132**  _(FLAG: paperTrail ; HIDDEN + Mid-course treatment letter confirmed in the refreshed record)_
  - NOTE (shown after choosing): A voice, dated. The choir assembles.

## [winter_b132] The Employer's Page
*Day 407 — Tuesday, September 15, 2026 (dayOffset 407)*

Your employer's accommodation schedule — the warehouse's letter, revised after the accident, moving you to the day crew permanently — is re-filed in its current form, because hearings read the version in the packet, not the version in your memory of HR's kindness.

Current versions only, from here to the hearing. The inventory now says so at the top, in Mr. Baptiste's hand.

**Choices:**
- Do the paper version: dated, copied, filed → **chorus**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the case record)_
  - NOTE (shown after choosing): Another dated page joins the folder.
- Handle it with a conversation and move on → **chorus**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [chorus] The Aunt's Standing Offer
*Day 409 — Thursday, September 17, 2026 (dayOffset 409)*

Maialen's aunt Josune — the approved kinship reserve — writes her own one-page letter: the study is current, the room is ready, and if the court wants a bridge instead of a verdict, her door is the bridge. It is an offer with a date on it, which makes it a document the court can use in either direction.

Mr. Baptiste files it under both tabs: as the relative-care answer if the clock is pressed, and as the family's own safety net if she comes home. Paper that argues two ways, honestly, is the strongest kind.

**Choices:**
- File Josune's letter in the packet under both tabs → **vis_a**  _(FLAG: kinLetter ; HIDDEN + Kinship caregiver's standing offer filed)_
  - NOTE (shown after choosing): A bridge, documented, that the court can use without building one at the hearing.
- Hold the letter — it might read as doubt about return → **vis_a**
  - NOTE (shown after choosing): Courts read standing kin as strength. Doubt is what undocumented families radiate.

## [vis_a] The Pediatrician's Paragraph
*Day 410 — Friday, September 18, 2026 (dayOffset 410)*

Maialen's pediatrician contributes the chorus's bass note: growth, attachment behaviors observed across a year of appointments, a final sentence about the father's consistency that the doctor offers unasked and you file without comment.

Unasked sentences from uninterested professionals are the file's gold standard. The packet does not gild them.

**Choices:**
- Carry the page to its file → **vis_b**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the record)_
  - NOTE (shown after choosing): Dated, copied, filed — the chain holds.
- Trust the conversation to carry it → **vis_b**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [vis_b] The Neighbor's Line
*Day 412 — Sunday, September 20, 2026 (dayOffset 412)*

The neighbor who waters the plants and watched the apartment stay ready all year signs her one line: the home was kept, the rent was paid, the child's room waited visibly. It is a small document about a large fact: readiness, maintained at cost, for fourteen months.

The line is filed in the housing tab, where readiness is the whole argument.

**Choices:**
- Carry the page to its file → **vis_c**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the record)_
  - NOTE (shown after choosing): Dated, copied, filed — the chain holds.
- Trust the conversation to carry it → **vis_c**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [vis_c] The Chorus, Indexed
*Day 414 — Tuesday, September 22, 2026 (dayOffset 414)*

The voices are indexed on the packet's second page — who, what, when, which tab — so the judge can find the teacher without hunting and the pediatrician without asking. Findability is courtesy, and courtesy, in a courtroom, is a form of credibility.

The book now has a table of contents. Books with tables of contents get finished.

**Choices:**
- Carry the page to its file → **packet132**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the record)_
  - NOTE (shown after choosing): Dated, copied, filed — the chain holds.
- Trust the conversation to carry it → **packet132**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [packet132] The Packet's First Page
*Day 416 — Thursday, September 24, 2026 (dayOffset 416)*

The packet's first page is its summary — one page, drafted by Mr. Baptiste, signed by you: the year in nine sentences, each with a date, each pointing to a tab. Hearings read first pages the way rivers read banks: everything after is steered by them.

You read it at the kitchen table at midnight. It is accurate, which grieves you a little: nine sentences for a year of Tuesdays. Then you remember the alternative — nine adjectives — and sign it.

**Choices:**
- Sign it and file the packet two weeks before the hearing → **pk_a**  _(cash −10 ; FLAG: packetBuilt ; HIDDEN + Hearing packet assembled and signed)_
  - NOTE (shown after choosing): Filed early, read early. The book is finished; the reading can begin.
- File it the Friday before — fresher → **pk_a**
  - NOTE (shown after choosing): Filings don't ripen. They just arrive late to the judge's weekend reading.

## [pk_a] The First Page, Read Aloud
*Day 418 — Saturday, September 26, 2026 (dayOffset 418)*

Mr. Baptiste reads the summary page aloud in his office, at courtroom speed, and times it: under three minutes. A year, honestly compressed, that a judge can absorb before the first witness is sworn.

You hear your own year as a stranger would. It holds. That is the test, and it passes.

**Choices:**
- Carry the page to its file → **pk_b**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the record)_
  - NOTE (shown after choosing): Dated, copied, filed — the chain holds.
- Trust the conversation to carry it → **pk_b**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [pk_b] The Filing Receipt
*Day 420 — Monday, September 28, 2026 (dayOffset 420)*

The packet is filed and the receipt is kept with the same care as the packet — because a book's existence, at a hearing, is sometimes the first thing disputed, and receipts end disputes about existence.

Two weeks of margin sit between the filing and the reading. Margin is the strategy's oldest friend.

**Choices:**
- Carry the page to its file → **filed_early**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the record)_
  - NOTE (shown after choosing): Dated, copied, filed — the chain holds.
- Trust the conversation to carry it → **filed_early**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [filed_early] The Agency Answers, Partly
*Day 423 — Thursday, October 1, 2026 (dayOffset 423)*

Three days after your packet lands, the agency files its position: it will not seek a goal change, it takes no position on return 'at this time,' and — in the paragraph your letter forced into existence — it confirms the exception letter is under review and notes your 'substantial documented progress.'

No position is a position, when the file's weight is all on one side. Mr. Baptiste smiles like a man reading weather he ordered: 'They have read the book. Now the court reads it aloud.'

**Choices:**
- Prepare your testimony to match the packet, page for page — nothing new, nothing contradicted → **ag_a**  _(FLAG: testimonyReady ; HIDDEN + Testimony prepared against the filed packet)_
  - NOTE (shown after choosing): The witness and the book, in agreement. Cross-examination hates agreement.
- Prepare to finally tell the whole story, beyond the packet → **ag_a**
  - NOTE (shown after choosing): The whole story is how witnesses contradict their own exhibits. Tell the packet's story, in your voice.

## [ag_a] Reading Their Answer Closely
*Day 424 — Friday, October 2, 2026 (dayOffset 424)*

The agency's response is read the way responses deserve: for what it concedes, what it avoids, and what it dates. It concedes progress, avoids the exception question, and dates itself three days after your packet — the sequence itself a small confession about whose paper is driving.

Mr. Baptiste annotates the margins in pencil. Penciled margins have settled more cases than speeches.

**Choices:**
- Carry the page to its file → **ag_b**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the record)_
  - NOTE (shown after choosing): Dated, copied, filed — the chain holds.
- Trust the conversation to carry it → **ag_b**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [ag_b] No Position, Positioned
*Day 426 — Sunday, October 4, 2026 (dayOffset 426)*

'No position at this time' is workshopped in the office until it confesses: the agency that intended to oppose return writes opposition. The sentence on file is the sound of a case being read and quietly re-decided.

Nothing is celebrated. Positions can change until the judge speaks. Paper just makes changing them expensive.

**Choices:**
- Carry the page to its file → **ag_c**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the record)_
  - NOTE (shown after choosing): Dated, copied, filed — the chain holds.
- Trust the conversation to carry it → **ag_c**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [ag_c] The Last Week's Quiet Jobs
*Day 428 — Tuesday, October 6, 2026 (dayOffset 428)*

The final week is quiet jobs: the suit pressed, the route timed, the folder's copies counted, Maialen's playroom logistics confirmed with Ms. Grey — the logistics of hope, handled like logistics.

You have done everything the year asked. The calendar says so, in fourteen months of handwriting.

**Choices:**
- Carry the page to its file → **testimony_prep**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the record)_
  - NOTE (shown after choosing): Dated, copied, filed — the chain holds.
- Trust the conversation to carry it → **testimony_prep**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [testimony_prep] The Night Before the Reading
*Day 430 — Thursday, October 8, 2026 (dayOffset 430)*

Maialen, told that tomorrow is 'the talking day,' has packed her own folder: drawings, in date order she insists are correct, of the apartment, the school, the park, and a house with three figures she declines to label. Ms. Grey will bring her to the courthouse playroom in the morning.

Your folder is heavier and less honest about its feelings. Both folders are ready. Sleep is the last document either of you can file.

**Choices:**
- Sleep. The book is written; tomorrow it is read. → **ni_a**
  - NOTE (shown after choosing): The library's oldest instruction, at its highest stakes.

## [ni_a] Questions at Kitchen-Table Speed
*Day 431 — Friday, October 9, 2026 (dayOffset 431)*

The likely questions are practiced at the kitchen table, at the speed of honesty: the accident, the weekend, the services, October, the plan for mornings. Each answer is shorter than the question's fear of it.

Preparation's product is not eloquence. It is the absence of surprise, which courtrooms experience as credibility.

**Choices:**
- Carry the page to its file → **ni_b**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the record)_
  - NOTE (shown after choosing): Dated, copied, filed — the chain holds.
- Trust the conversation to carry it → **ni_b**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [ni_b] The Drawings, Decided
*Day 432 — Saturday, October 10, 2026 (dayOffset 432)*

Whether Maialen's drawings come to court is decided the adult way: they stay with her, in her folder, because children are not exhibits and this family has never once used her as paper.

Your folder closes with a sound like a book's. Hers closes with a sound like a child's. Both are ready.

**Choices:**
- Carry the page to its file → **hearing132**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the record)_
  - NOTE (shown after choosing): Dated, copied, filed — the chain holds.
- Trust the conversation to carry it → **hearing132**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [hearing132] The Hearing That Read the Year
*Day 434 — Monday, October 12, 2026 (dayOffset 434)*

Monday, October 12, 2026. The courtroom does what courtrooms do with complete records: it moves without friction. The agency's counsel, facing a packet she has read and a position she has filed, does not manufacture a contest the file won't support. The judge works the tabs — visits, treatment, the cured October, the exception letter and its dated silence, the teacher's page, Josune's standing offer.

'Mr. Baptiste,' the judge says, 'your client seems to have conducted this case as if the record were the client.' It is not quite a compliment. It is better: it is a finding, forming. The question she puts to you is the question the year built: 'What does Maialen come home to, and who stands behind it?' Your testimony, prepared against the packet, answers in the packet's own dates.

**Choices:**
- Ask for the order: return home today, aftercare and Josune's respite in writing, case to close at the winter review → **end_home132**  _(REQUIRES FLAG: recordsRequested ; REQUIRES FLAG: packetBuilt ; REQUIRES FLAG: gapCured ; REQUIRES FLAG: exceptionAsked)_
  - NOTE (shown after choosing): Today. The word fourteen months of Tuesdays were for.
- Ask for return with a ninety-day trial first, to be safe → **end_trial132**
  - NOTE (shown after choosing): Safe is a slower word for the same address. The file argued for today.
- Let the judge craft the order without proposing one → **end_trial132**
  - NOTE (shown after choosing): Unproposed orders arrive wearing the court's caution. Propose the one the book supports.
- Press for return while conceding October needs explaining later → **end_contested132**  _(REQUIRES NO FLAG: gapCured)_
  - NOTE (shown after choosing): Later is the contested hearing's home address. October, unanswered, becomes the day.
- Ask for a continuance to perfect the packet — a month can only help → **end_clock132**
  - NOTE (shown after choosing): A month helps the clock, not the case. November 4 does not continue itself.

## [end_home132] Ending — Home From the Hearing
*Day 434 — Monday, October 12, 2026 (dayOffset 434)*

Maialen comes home from the hearing — not from a later visit, not after a transition plan, but in your car, that afternoon, with her folder of drawings on her lap and Ms. Grey waving from the courthouse steps with the complicated smile of a woman whose year of Tuesdays mattered and is over.

The order is four pages: return, aftercare in writing, Josune's respite named, closure set for the winter review. Behind it, doing the work orders cannot do, is the book: a year of paper that left the court nothing to guess. State the win plainly, because it is one: sometimes — when the record is complete, the gaps are cured, and the questions were asked in writing in time — the hearing reads the year, and the year says home.

**Ending.**

**Debrief:**
- THE HEARING'S LAW — The permanency framework asks, at fifteen of the most recent twenty-two months, whether the filing duty is triggered and whether an exception is documented (42 U.S.C. § 675(5)(E); the state review determination under 42 Pa.C.S. § 6351(f)(9) — entry August 4, 2025; fifteen months Wednesday, November 4, 2026). This route never lets the question ripen: the agency was asked in writing to state its exception position a month before the hearing, and its non-answer is itself part of the record the court read. Counsel (42 Pa.C.S. § 6337) built the book; the record requests (55 Pa. Code § 3130.44(d)) supplied its contents; the redactions under (f) were treated as rules, not obstacles.
- WHY THIS ENDING IS FULL — Maialen comes home from the hearing itself. The scenario is the library's proof case for its own doctrine: a complete record — visits counted, gap cured from another chair's calendar, exceptions asked about in writing, chorus filed, packet early — can convert a permanency hearing from a contest into a reading. It does not claim hearings are usually like this. It claims the difference, when they are, is paper.
- WHAT NO STRATEGY CONTROLS — The judge, the agency's litigation posture, and the accident that started it all. A different courtroom can read the same book more slowly (see the trial ending). The strategy's claim is only that nothing the court needed was missing, contradicted, or late — and that claim, this time, was enough.

## [end_trial132] Ending — Home on the Court's Schedule
*Day 434 — Monday, October 12, 2026 (dayOffset 434)*

The court orders a ninety-day trial return — Maialen home that week, the case open until winter, the file technically unfinished. It is the same address as the best ending, reached by the court's road instead of yours: the book persuaded, but the proposal it ratified was caution's.

Ninety days of documented mornings later, the case closes without ceremony. The book's last page is an order you did not draft, saying almost what you asked, three months after you asked it.

**Ending.**

**Debrief:**
- A PARTIAL WIN, NAMED HONESTLY — Home, on the court's schedule. The gated route required **recordsRequested**, **packetBuilt**, **gapCured**, and **exceptionAsked** together: the refreshed mirror, the early packet, the cured October, and the exception question put in writing in time for its silence to testify.
- WHAT NO STRATEGY CONTROLS — Judicial caution, which no packet abolishes. The trial period is the court hedging against its own reading; the book's work is to make the hedge short and the closing certain.

## [end_contested132] Ending — The Contested Reading
*Day 434 — Monday, October 12, 2026 (dayOffset 434)*

In this branch the hearing becomes what hearings become when the book has holes: October is a cross-examination, the exception question is asked for the first time aloud, and the agency — surprised into advocacy — asks for time to answer both.

Time is granted, because unanswered questions are the one exhibit courts always admit. The case continues into the fifteenth month with the filing question now open and the goal under weather. Nothing is lost forever. Everything is later, which in a five-year-old's calendar is its own kind of loss.

**Ending.**

**Debrief:**
- WHAT THE HOLES COST — An uncured month invites the inference it might have answered; an unasked exception question leaves 42 U.S.C. § 675(5)(E) to be litigated cold at the worst moment. The route's devices were all cheap: a calendar from the foster mother's drawer, a letter with proof of delivery, a refreshed record (55 Pa. Code § 3130.44(d)). Hearings do not punish parents; they punish gaps, impersonally and completely.
- WHAT NO STRATEGY CONTROLS — Even holed, this record might have persuaded a different judge. The scenario's narrower claim: holes are choices, made months earlier, at kitchen tables — and at capstone weight, the hearing is merely where they are read aloud.

## [end_clock132] Ending — November 4
*Day 457 — Wednesday, November 4, 2026 (dayOffset 457)*

Wednesday, November 4, 2026 — the fifteenth month — arrives in the branch where the hearing was continued and the packet never quite closed. The filing question is now the case. The exceptions exist, as they always did, in the statute's text (42 U.S.C. § 675(5)(E)); the question the winter will litigate is whether they exist in the case plan, in writing, in time.

Maialen asks her foster mother why the talking day keeps moving. There is no answer in the file. That is the answer, and it is the one this ending exists to prevent.

**Ending.**

**Debrief:**
- THE CLOCK, ARRIVED — Entry Monday, August 4, 2025 + 15 months = Wednesday, November 4, 2026. The filing duty and its three exceptions (42 U.S.C. § 675(5)(E)) become the whole litigation. The services-not-provided exception and the compelling-reason documentation were this family's true story all year; unwritten, they are arguments. Written, they would have been findings.
- WHAT NO STRATEGY CONTROLS — Continuances, crowded dockets, and one judge's calendar can strand even a strong case at the clock. The strategy's defense was to finish the book a month early — the one schedule in the case the parent controlled outright.
