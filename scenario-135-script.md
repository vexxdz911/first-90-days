# THE FIRST 90 DAYS — Scenario 135: “Four Seasons”

*Human-readable script. This document and `scenario-135.json` are generated from a single source and match node-for-node: same IDs, same order, same choices, same effects.*

**The family is fictional — a composite. No real person's story appears here.**

**Content note:** This scenario depicts a long-running dependency case spanning a full year. There is no graphic content. Players may skip any scene or use the quick exit at any time.

**How to read effects:** `cash −40` changes the player's cash. `FLAG: name` sets a flag the engine tracks. `HIDDEN + item` means the case file quietly records that item at this choice — the player does not see it when it happens. `REQUIRES FLAG: name` means the choice is only available if that flag was set earlier; `REQUIRES NO FLAG: name` means it is only available if that flag was never set. `NOTE:` is text shown to the player right after choosing.

Start date: Monday, September 1, 2025. Day offsets are days since the scenario's start date (the elder children's foster-care entry date).

## [start] September, Three Times
*Day 0 — Monday, September 1, 2025 (dayOffset 0)*

Your name is Miren. Esteban, twelve, and Uxue, nine, entered care on Monday, September 1, 2025 — the housing collapse arriving, as it does, on a holiday weekend, when the landlord's deadline met the shelter's waitlist and the children's school-year start met both. Nico, five, entered four weeks later, on Monday, September 29, after his brief kinship stay with your cousin failed on her own emergency surgery.

Three children, two entry dates, one mother, and a case that will run the full wheel of the year: their fifteenth months land on Tuesday, December 1, 2026 (the elders) and Tuesday, December 29, 2026 (Nico) — dates so far away in this September that they feel theoretical. They are not theoretical. They are the case. Your lawyer, Ms. Mendieta, writes both dates on the folder before she writes anything else.

**Choices:**
- Start the compendium now: one binder, three sections, every date from day one → **compendium_start**  _(FLAG: compendiumStarted ; HIDDEN + Year compendium begun on day one, three sections)_
  - NOTE (shown after choosing): A year this long cannot be reconstructed next fall. It can only be kept.
- A binder is premature — get through the first month first → **compendium_start**
  - NOTE (shown after choosing): The first month is exactly the part nobody can reconstruct later. The binder is the memory.

## [compendium_start] Ms. Mendieta's Wheel
*Day 6 — Sunday, September 7, 2025 (dayOffset 6)*

She draws the year as a wheel — four seasons, each with its work: FALL, stabilize and document; WINTER, cure the plan's gaps in writing; SPRING, build the housing answer; SUMMER, assemble the exceptions before anyone asks for them. Counsel is your right (42 Pa.C.S. § 6337); here counsel is also a calendar with a philosophy.

'Permanency hearings are not won in the fall of the second year,' she says. 'They are won in the fall of the first, by people who knew the second fall was coming.'

**Choices:**
- Do the paper version: dated, copied, filed → **cs_a**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the case record)_
  - NOTE (shown after choosing): Another dated page joins the folder.
- Handle it with a conversation and move on → **cs_a**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [cs_a] Three Sections, Two Clocks
*Day 10 — Thursday, September 11, 2025 (dayOffset 10)*

The binder's architecture mirrors the case's: three sections (one per child), a shared front pocket for the clocks, and a rule written inside the cover — every page dated, every date cross-checked against the entry orders before it is believed.

The rule sounds like fussiness in September. By the second September it is the difference between a record and a rumor.

**Choices:**
- Carry the page to its file → **cs_b**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the record)_
  - NOTE (shown after choosing): Dated, copied, filed — the chain holds.
- Trust the conversation to carry it → **cs_b**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [cs_b] The First Pages
*Day 14 — Monday, September 15, 2025 (dayOffset 14)*

The first pages are the entry orders themselves, the plan, and Ms. Mendieta's wheel — the case's founding documents, kept at the front so the year's later paper always knows what it answers to.

Binders, like cases, are judged by whether their first pages survive their last.

**Choices:**
- Carry the page to its file → **fall_services**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the record)_
  - NOTE (shown after choosing): Dated, copied, filed — the chain holds.
- Trust the conversation to carry it → **fall_services**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [fall_services] Fall: The Services Begin
*Day 20 — Sunday, September 21, 2025 (dayOffset 20)*

The plan's services begin their slow enrollment: parenting program (October start), family therapy (November, after the provider's waitlist), housing case management (immediate, and immediately a waiting game). Each enrollment — and each wait — is a dated fact, and the compendium's first discipline is to record waits as facts rather than as blanks.

A wait recorded is a gap owned by its true owner later. A wait unrecorded becomes, in the retelling, a parent who did nothing in October.

**Choices:**
- Log every enrollment and every waitlist date in the compendium, monthly → **fs_a**  _(FLAG: waitsLogged ; HIDDEN + Service enrollment and waitlist dates logged from the first month)_
  - NOTE (shown after choosing): Waits, logged, belong to the system. Waits unlogged belong to you.
- The providers keep records — that's enough → **fs_a**
  - NOTE (shown after choosing): Providers keep records of attendance. Waits live in your file or nowhere.

## [fs_a] October's Enrollment Letters
*Day 27 — Sunday, September 28, 2025 (dayOffset 27)*

The enrollment letters arrive across October like the season's first report cards: program accepted, therapy waitlisted, housing intake scheduled — each copied into the binder the week it lands, waits and all, because October's paper is November's alibi and next October's exhibit.

The compendium's appetite is established early: everything, dated, monthly. The family settles into the rhythm the year will require.

**Choices:**
- Carry the page to its file → **fs_b**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the record)_
  - NOTE (shown after choosing): Dated, copied, filed — the chain holds.
- Trust the conversation to carry it → **fs_b**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [fs_b] The Cousin's September
*Day 34 — Sunday, October 5, 2025 (dayOffset 34)*

A page of the binder is set aside for the kinship chapter that didn't hold: your cousin's care of Nico in September, her surgery, the honest end of an arrangement nobody failed at — documented now, kindly, because next fall a hearing may ask whether kinship was ever tried, and the answer deserves better than a summary.

Tried, documented, ended by medicine: the page says it in dates. That is the whole entry, and it is enough.

**Choices:**
- Carry the page to its file → **fall_visits**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the record)_
  - NOTE (shown after choosing): Dated, copied, filed — the chain holds.
- Trust the conversation to carry it → **fall_visits**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [fall_visits] Fall: The Visits Find Their Rhythm
*Day 41 — Sunday, October 12, 2025 (dayOffset 41)*

Visits settle at the family center: Esteban's laconic twelve-year-old audits, Uxue's art output (filed copies, originals to the children), Nico's kindergarten reports relayed by his foster mother with a generosity the compendium notes by name.

Three children in two placements generate two visit structures, two sets of notes, one exhausted mother, and — if she keeps it — one binder where both structures are reconciled monthly. Reconciliation is the compendium's second discipline: contradictions found in November are cheap; found next October, they are cross-examination.

**Choices:**
- Reconcile both placements' notes into the compendium monthly → **fv_a**  _(FLAG: notesReconciled ; HIDDEN + Both placements' visit notes reconciled monthly in the compendium)_
  - NOTE (shown after choosing): One binder, two placements, no contradictions left to ripen.
- Each placement's notes are its own file's business → **fv_a**
  - NOTE (shown after choosing): Until one hearing reads both files, and asks why they disagree about you.

## [fv_a] November's Reconciliation
*Day 50 — Tuesday, October 21, 2025 (dayOffset 50)*

November's reconciliation finds its first discrepancy: a visit the center logged as supervised that ran, in fact, as a community visit — a small error with a long shadow if left to ripen into next fall's 'inconsistency.' It is corrected by a dated page, filed without accusation, in both the binder and the record.

Corrections filed kindly and early are maintenance. The same correction at a hearing is impeachment.

**Choices:**
- Carry the page to its file → **fv_b**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the record)_
  - NOTE (shown after choosing): Dated, copied, filed — the chain holds.
- Trust the conversation to carry it → **fv_b**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [fv_b] December at Two Placements
*Day 62 — Sunday, November 2, 2025 (dayOffset 62)*

The holidays run on both placements' calendars and the binder's one: gifts logged, school breaks charted, the children's December recorded as a season rather than a wound — paper doing its quietest work, keeping a family's worst year narratable.

Narratable years can be argued from. The binder is an argument under construction, disguised as a scrapbook.

**Choices:**
- Carry the page to its file → **winter_gap**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the record)_
  - NOTE (shown after choosing): Dated, copied, filed — the chain holds.
- Trust the conversation to carry it → **winter_gap**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [winter_gap] Winter: The Therapy Gap
*Day 76 — Sunday, November 16, 2025 (dayOffset 76)*

The family-therapy referral — signed in the plan in October — is actually sent in January, an eleven-week gap the record, read carefully, attributes to a staffing vacancy and a queue. The compendium has the plan's date and the referral's date on facing pages, where they have been accusing each other quietly since November.

Services identified in the plan but not provided are one of the permanency clock's own exceptions (42 U.S.C. § 675(5)(E)) — but only when they are documented as such, in the case plan, in time. A gap with dates is an exception. A gap with adjectives is an argument.

**Choices:**
- Write the gap letter: plan date, referral date, vacancy — filed, with both dates attached → **wg_a**  _(cash −5 ; FLAG: gapDocumented ; HIDDEN + Therapy referral gap documented in writing with both dates)_
  - NOTE (shown after choosing): Eleven weeks, owned by their true dates. The exception's first brick.
- Raise the gap at the winter review so the judge hears it live → **wg_a**
  - NOTE (shown after choosing): Judges hear many things live. They rely on what is filed.

## [wg_a] The Vacancy, Confirmed
*Day 82 — Saturday, November 22, 2025 (dayOffset 82)*

Before the gap letter goes, the vacancy behind it is confirmed the paper way: the provider's own letter, requested in writing, stating the referral's queue position and the staffing gap that held it — the system's explanation of its own eleven weeks, in its own hand.

Letters like this are never volunteered and always producible. Asking, in writing, is the whole technology.

**Choices:**
- Carry the page to its file → **gap_letter135**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the record)_
  - NOTE (shown after choosing): Dated, copied, filed — the chain holds.
- Trust the conversation to carry it → **gap_letter135**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [gap_letter135] Winter: The Record, Requested
*Day 90 — Sunday, November 30, 2025 (dayOffset 90)*

You request the case record in writing (55 Pa. Code § 3130.44(d)) — the mid-winter mirror check the compendium exists to survive: does the file's version of the fall match the binder's? Mostly, yes. Where it doesn't — a visit marked supervised that wasn't, a wait omitted — the corrections are filed as pages, not complaints.

Redactions under (f) black out the cousin's medical details, as the rule provides. The mirror is partial by design. The binder is not.

**Choices:**
- File the corrections as dated pages and index the mirror against the binder → **gl_a**  _(FLAG: recordsRequested ; HIDDEN + Case record requested under § 3130.44(d); corrections filed as dated pages)_
  - NOTE (shown after choosing): The mirror and the binder, reconciled. Next fall's hearing will meet one story, in two bindings.
- Note the discrepancies for counsel to raise later → **gl_a**
  - NOTE (shown after choosing): Later is where discrepancies go to become 'inconsistencies in the mother's account.' File them.

## [gl_a] The Mirror's Gaps
*Day 100 — Wednesday, December 10, 2025 (dayOffset 100)*

The mid-winter record, read against the binder, shows the expected silences: the therapy wait absent entirely (the file begins the service at its start, as if queues were weather), one visit's supervision mislabeled in the other direction.

Each silence gets its page. The binder's margins fill with the small print of a family insisting on being accurately described.

**Choices:**
- Carry the page to its file → **gl_b**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the record)_
  - NOTE (shown after choosing): Dated, copied, filed — the chain holds.
- Trust the conversation to carry it → **gl_b**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [gl_b] Corrections, Filed as Pages
*Day 110 — Saturday, December 20, 2025 (dayOffset 110)*

The corrections go in as pages with exhibits — the provider's queue letter, the center's sign-in sheet — not as complaints about the file but as additions to it, which is why they are accepted without a fight and read forever after as part of the record.

Tone is a filing strategy. Additions are read; accusations are answered. The binder prefers to be read.

**Choices:**
- Carry the page to its file → **winter_review135**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the record)_
  - NOTE (shown after choosing): Dated, copied, filed — the chain holds.
- Trust the conversation to carry it → **winter_review135**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [winter_review135] Winter: The Review
*Day 120 — Tuesday, December 30, 2025 (dayOffset 120)*

The winter review is the wheel's first checkpoint: services running, gap documented, housing the open wound — your applications are a sheaf of waitlist letters, each dated, each a small proof that the wound is the market's and not the mother's.

The judge continues the goal and says the sentence that will be quoted in the fall: 'Housing is the case. Everything else is commentary.' The compendium records the sentence, dated. Sentences judges say in winter have a way of being load-bearing in autumn.

**Choices:**
- Do the paper version: dated, copied, filed → **wr_a**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the case record)_
  - NOTE (shown after choosing): Another dated page joins the folder.
- Handle it with a conversation and move on → **wr_a**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [wr_a] February's Applications
*Day 135 — Wednesday, January 14, 2026 (dayOffset 135)*

February's housing work is a sheaf of applications, each with its date and its waitlist's arithmetic kept in the binder's housing tab — a paper trail that proves the wound's owner every time it is opened.

Applications without dates are hopes. These have dates, queue numbers, and a case manager who answers email in writing.

**Choices:**
- Carry the page to its file → **wr_b**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the record)_
  - NOTE (shown after choosing): Dated, copied, filed — the chain holds.
- Trust the conversation to carry it → **wr_b**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [wr_b] The Children's Winter Pages
*Day 150 — Thursday, January 29, 2026 (dayOffset 150)*

Winter adds its chorus pages: Esteban's mid-year report, Uxue's attendance star, Nico's foster mother's February letter about a boy who has started calling her house 'the snow house' with a permanence that worries and reassures everyone in equal measure.

The pages are filed in season. Next fall's hearing will meet children documented as they grew, not as they were remembered.

**Choices:**
- Carry the page to its file → **spring_housing**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the record)_
  - NOTE (shown after choosing): Dated, copied, filed — the chain holds.
- Trust the conversation to carry it → **spring_housing**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [spring_housing] Spring: The Housing Answer
*Day 168 — Monday, February 16, 2026 (dayOffset 168)*

The housing answer arrives the way housing answers do: not an apartment, but a letter — the housing authority's dated projection, your case manager's confirmation, and a landlord's conditional commitment for a three-bedroom in the children's school zone, contingent on the fall voucher round.

A projection is not a home. But a dated, letterheaded, contingently-committed answer is the difference between a plan and a hope — and reviews, permanency hearings especially, are machines for telling those apart.

**Choices:**
- Get every element in writing, on letterhead, dated — and file them together → **housing_letter135**  _(cash −5 ; FLAG: housingLetter ; HIDDEN + Housing answer assembled in writing: projection, confirmation, landlord commitment)_
  - NOTE (shown after choosing): Three letters, one answer. The wound now has a documented treatment plan.
- The case manager's word is solid — paper can follow → **housing_letter135**
  - NOTE (shown after choosing): Words are solid until staff rotate. Paper is the only staff that never rotates.

## [housing_letter135] Spring: The Children's Pages
*Day 196 — Monday, March 16, 2026 (dayOffset 196)*

Spring adds the children's own pages to the compendium: Esteban's school letter (attendance, the honor roll's second quarter, a counselor's line about a boy 'carrying his family like a job'), Uxue's art teacher's note, Nico's foster mother's spring letter — the chorus, collected while it is singing, not reconstructed after.

None of these pages was requested by any proceeding. All of them will be read by one.

**Choices:**
- File the children's pages in the compendium and the case record → **hl_a**  _(FLAG: chorusFiled ; HIDDEN + Children's school and caregiver pages collected and filed)_
  - NOTE (shown after choosing): The chorus, in writing, in season. Fall will not have to imagine them.
- School letters can be gathered in the fall if needed → **hl_a**
  - NOTE (shown after choosing): Fall-gathered letters describe last spring from memory. Collect in season.

## [hl_a] The Landlord's Conditions
*Day 208 — Saturday, March 28, 2026 (dayOffset 208)*

The landlord's conditional commitment gets its conditions itemized in writing — voucher round, inspection, the September lease window — because conditions that live in a phone call retire when memories do.

Itemized, the commitment becomes a checklist the fall can execute. Unitemized, it was a mood.

**Choices:**
- Carry the page to its file → **hl_b**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the record)_
  - NOTE (shown after choosing): Dated, copied, filed — the chain holds.
- Trust the conversation to carry it → **hl_b**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [hl_b] The Answer, Assembled
*Day 220 — Thursday, April 9, 2026 (dayOffset 220)*

The three letters are assembled into the binder's housing tab as a single answered question: projection, confirmation, commitment — the wound and its treatment plan, dated within the same spring.

Assembled answers are what reviews adopt. Scattered ones are what reviews ask about.

**Choices:**
- Carry the page to its file → **spring_review135**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the record)_
  - NOTE (shown after choosing): Dated, copied, filed — the chain holds.
- Trust the conversation to carry it → **spring_review135**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [spring_review135] Spring: The Review
*Day 232 — Tuesday, April 21, 2026 (dayOffset 232)*

The spring review is the first where the file and the binder fully agree, because for two seasons you have been making them agree monthly. The agency's report uses the phrase 'documented progress' four times. The goal continues; the permanency hearing is set for the fall — the wheel's last quarter, where the December dates will finally be close enough to cast shadows.

Ms. Mendieta opens the compendium to its last section, still mostly empty, labeled in her hand: EXCEPTIONS — TO BE BUILT BEFORE ASKED.

**Choices:**
- Do the paper version: dated, copied, filed → **sr_a135**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the case record)_
  - NOTE (shown after choosing): Another dated page joins the folder.
- Handle it with a conversation and move on → **sr_a135**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [sr_a135] June's First Assembly
*Day 242 — Friday, May 1, 2026 (dayOffset 242)*

June opens the EXCEPTIONS section with its inventory: what each child has (relative care assessed, gap lettered, trajectory documented), what each still needs (the plan language, requested; the packets, to be built), and the summer's work schedule — counsel's wheel entering its third season.

Inventories precede assemblies. The section will be built from a list, not from a mood.

**Choices:**
- Carry the page to its file → **sr_b135**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the record)_
  - NOTE (shown after choosing): Dated, copied, filed — the chain holds.
- Trust the conversation to carry it → **sr_b135**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [sr_b135] The Trial, Proposed on Paper
*Day 252 — Monday, May 11, 2026 (dayOffset 252)*

The trial return is proposed as a document in June — stages, school logistics, support structure — so the agency's agreement, when it comes in July, comes as a response to the family's paper rather than as the system's invention.

Proposals shape adoptions. The August trial will run on the June draft's rails, and everyone will call it the plan.

**Choices:**
- Carry the page to its file → **summer_a**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the record)_
  - NOTE (shown after choosing): Dated, copied, filed — the chain holds.
- Trust the conversation to carry it → **summer_a**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [summer_a] Summer: The Exceptions, Built
*Day 262 — Thursday, May 21, 2026 (dayOffset 262)*

Summer's work is the section's: exception one, relative care — considered and documented (the cousin's post-surgery capacity, assessed in writing and honestly insufficient for three; the assessment itself is the evidence the exception was examined, not assumed). Exception two, the case-plan compelling reason — reunification on a documented trajectory, the housing answer dated, the trial return proposed for the fall. Exception three, services not provided — the therapy gap, already lettered in the winter.

Exceptions are not arguments to be invented at the hearing. They are sections to be built in the summer, from the year's own pages.

**Choices:**
- Assemble the exception section child by child, each with its own dates → **sa_a**  _(cash −10 ; FLAG: exceptionsBuilt ; HIDDEN + Exception section assembled per child from the year's documentation)_
  - NOTE (shown after choosing): Three exceptions, three children, nine dated subsections. Built before asked.
- Build one family exception narrative — the story is unified → **sa_a**
  - NOTE (shown after choosing): Stories unify; clocks don't. The statute will count the children separately, and so must the binder.

## [sa_a] Each Child, Their Own Page
*Day 270 — Friday, May 29, 2026 (dayOffset 270)*

The exception work proceeds child by child through July: Esteban's page (his clock, his school letter, his gap arithmetic), Uxue's (hers, with the art teacher's spring note promoted to evidence of trajectory), the family's shared exhibits indexed once and cited thrice.

Shared paper, separate dates: the binder's grammar, learned over a year, now fluent.

**Choices:**
- Carry the page to its file → **sa_b**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the record)_
  - NOTE (shown after choosing): Dated, copied, filed — the chain holds.
- Trust the conversation to carry it → **sa_b**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [sa_b] The Compendium, Closed for Building
*Day 280 — Monday, June 8, 2026 (dayOffset 280)*

By August the compendium is complete enough to change tense: no longer a diary being kept but a book being cited — its building finished, its use begun. Ms. Mendieta's wheel reaches the summer's end with every section populated.

The flag the year has been earning is set here, at the assembly's completion: the compendium is built.

**Choices:**
- Rule the compendium complete and index it for the fall → **summer_b**  _(FLAG: compendiumBuilt ; HIDDEN + Year compendium completed and indexed)_
  - NOTE (shown after choosing): Built. From here to the hearing, the binder is cited, not kept.
- Keep adding pages without ruling it complete → **summer_b**
  - NOTE (shown after choosing): Unindexed completeness is a rumor. Rule it built and cite it.

## [summer_b] Summer: The Trial Begins
*Day 290 — Thursday, June 18, 2026 (dayOffset 290)*

The trial return begins in August on the compendium's own proposal: weekends becoming weeks, the placements converting to the family's documented support, school enrollment in the home zone completed in August rather than scrambled in October.

Three children come home in stages the binder has rehearsed on paper since spring. The stages are not the win — the hearing still stands between this family and permanence — but they are the hearing's best evidence, generated by living rather than by argument.

**Choices:**
- Document the trial's stages in the compendium as they happen → **nico_packet**  _(FLAG: trialDocumented ; HIDDEN + Trial return stages documented in the compendium)_
  - NOTE (shown after choosing): The trial, logged like the year was: as it happens, in ink.
- Live the trial; the file has enough paper → **nico_packet**
  - NOTE (shown after choosing): The file's appetite is the one constant of the year. Feed the trial too.

## [nico_packet] Nico's Packet
*Day 340 — Friday, August 7, 2026 (dayOffset 340)*

Nico's clock runs four weeks behind his siblings', and his packet is built to his own dates in September: his kinship chapter (the cousin's page, promoted), his foster mother's letters, his gap arithmetic — the youngest child's file assembled with the same rigor as the elders', because December 29 will ask him separately.

Youngest children in multi-child cases get summarized. This one gets a packet. The difference is the scenario.

**Choices:**
- Carry the page to its file → **fall135**  _(cash −5 ; FLAG: paperTrail ; HIDDEN + Dated documentation added to the record)_
  - NOTE (shown after choosing): Dated, copied, filed — the chain holds.
- Trust the conversation to carry it → **fall135**
  - NOTE (shown after choosing): Conversations end. The file keeps what it was given.

## [fall135] The Second Fall
*Day 365 — Tuesday, September 1, 2026 (dayOffset 365)*

A year after the first September, the wheel completes its turn: the elder children's fifteenth month is eight weeks out (Tuesday, December 1, 2026), Nico's twelve (Tuesday, December 29). The agency's permanency position lands in writing: it will ask the court to consider the goal — language that means the filing question and the goal question will be heard together, at a hearing now set for late October.

Families who built the exceptions section in the summer read that letter as a scheduling notice. Families who didn't, read it as a verdict. The difference was made in July, at a kitchen table, with a binder.

**Choices:**
- Answer the position in writing: exceptions documented per child, trial running, housing letter attached → **goal_hearing135**  _(cash −5 ; FLAG: positionAnswered ; HIDDEN + Agency permanency position answered in writing with the exception sections)_
  - NOTE (shown after choosing): Answered in writing, in advance, per child. The hearing is now a reading.
- Wait for the hearing to answer — that's what it's for → **end_december**
  - NOTE (shown after choosing): Hearings are for deciding. Families who arrive with answers already filed get decided about less.
- Ask for a continuance into December to strengthen the trial record → **end_december**
  - NOTE (shown after choosing): December is not a neutral month in this case. It is the clock's home address.

## [goal_hearing135] The Hearing Where the Goal Is the Question
*Day 415 — Wednesday, October 21, 2026 (dayOffset 415)*

The hearing is the year's harvest: the agency, to its credit and its file's, states the documented position — the exceptions stand per child, the therapy gap is the plan's own arithmetic, the trial is succeeding on the binder's pages. The goal question is asked anyway, because asking it is the hearing's job, and it is answered by a compendium the court has clearly read.

Your testimony is the year's shortest document: the dates, the waits, the housing letter, the children home. The binder testifies the rest of the way, in three sections and a winter judge's quoted sentence.

**Choices:**
- Ask for the order: goal unchanged, trial to convert, exceptions as documented per child → **end_goal_survives**  _(REQUIRES FLAG: recordsRequested ; REQUIRES FLAG: gapDocumented ; REQUIRES FLAG: compendiumBuilt ; REQUIRES FLAG: housingLetter)_
  - NOTE (shown after choosing): Asked with the whole year behind it. The wheel stops where it started: home.
- Accept the agency's compromise: the goal changes for the elders, holds for Nico → **end_split135**
  - NOTE (shown after choosing): A split goal is a split family with a court date. The binder argued for one family.
- Argue the goal should never have been questioned, at length, from the heart → **end_goal_changed**
  - NOTE (shown after choosing): Length and heart are not exhibits. The hearing punishes the speech and rewards the binder — and this branch gives it only the speech.

## [end_goal_survives] Ending — The Goal Survives
*Day 425 — Saturday, October 31, 2026 (dayOffset 425)*

The order keeps the goal — reunification — for all three children, adopts the documented exceptions, and converts the trial on schedule. The children are home for the second December in their own rooms, in the school-zone apartment the spring letters promised, the voucher and the landlord and the case manager's paper having converged, as documented things sometimes do, into an address.

State the win the house way: the children spent fifteen months in care, and the second December cannot refund the first. What the year of documentation did was ensure that when the clock finally asked its question, the answer had been assembled in advance, child by child, season by season — and the goal, which is the case's soul, survived its own hearing. Partial, the guides insist, because the year is not refundable. Survived, because everything that could be saved was.

**Ending.**

**Debrief:**
- THE CLOCKS, AUDITED PER CHILD — Elders: entered Monday, September 1, 2025 + 15 months = Tuesday, December 1, 2026. Nico: entered Monday, September 29, 2025 + 15 months = Tuesday, December 29, 2026. 42 U.S.C. § 675(5)(E) counts each child separately, which is why the exceptions were built per child: the documented therapy gap (services identified but not provided), the case-plan compelling reason, and relative care honestly assessed. The hearing preceded both dates because the exceptions were assembled in the summer, not argued in December.
- WHY PARTIAL IS THE HONEST LABEL — The goal survived, the children are home, the case converts — after fifteen months. The library's guides label outcomes, not efforts: a family that loses a year to a housing market and a staffing vacancy has won the best available outcome and lost a year doing it. Both facts belong in the debrief. The strategy's claim is the narrower one: no part of the year was lost to anything documentable-and-undocumented.
- WHAT NO STRATEGY CONTROLS — Housing markets, provider waitlists, a cousin's surgery, and the school-zone map. The route controlled the compendium: waits logged as facts, notes reconciled monthly, gaps lettered in their own season, exceptions built before asked, and a record requested in time to reconcile the mirror (55 Pa. Code § 3130.44(d)). A year-long case is a memory contest. The binder is how a family wins one. Counsel: 42 Pa.C.S. § 6337.

## [end_split135] Ending — One Family, Two Goals
*Day 425 — Saturday, October 31, 2026 (dayOffset 425)*

The court's order splits the difference the compromise offered: Nico's goal holds, the elders' converts to a longer plan with a review in the spring. The children remain, mostly, together; the file no longer describes one family with one destination.

Split goals are the permanency system's compromise genre — no one lost, no one finished, another wheel beginning for two of the three children. The binder stays open. It has a second year in it if the case insists, and by now keeping it is simply what this family does in the evenings.

**Ending.**

**Debrief:**
- THE SPLIT, NAMED HONESTLY — A partial outcome short of the partial win: the gated route required **recordsRequested**, **gapDocumented**, **compendiumBuilt**, and **housingLetter** standing together at the ask. Compromises accepted at the hearing convert documented strength into divided plans; the file that was built to answer per child was, in the end, answered per child — by the other side.
- WHAT NO STRATEGY CONTROLS — A court's instinct for compromise, which no binder abolishes. The strategy's claim is that the family never had to accept the split for lack of an alternative the record supported. Accepting it anyway is a choice the hearing offers every family; the guides merely insist it be recognized as one.

## [end_goal_changed] Ending — The Speech Instead of the Binder
*Day 415 — Wednesday, October 21, 2026 (dayOffset 415)*

The hearing that gets the speech instead of the compendium ends the way hearings end when advocacy substitutes for evidence: moved, unconvinced, and bound by a record too thin to carry the goal it was asked to save.

The goal changes. The exceptions, unbuilt, are noted as 'not documented in the case plan' — the statute's quietest and most devastating phrase — and the family's true story becomes a footnote in a plan written by someone else. The binder, where it exists in this branch, is a diary. Diaries do not testify.

**Ending.**

**Debrief:**
- NOT DOCUMENTED IN THE CASE PLAN — The exceptions under 42 U.S.C. § 675(5)(E) are not rhetorical positions; the compelling-reason exception exists, by the statute's terms, when it is documented in the case plan. The therapy gap was real, the housing answer was real, the trajectory was real — and undocumented reality is the permanency hearing's most common casualty.
- WHAT NO STRATEGY CONTROLS — Very little, here, was weather. The year's raw material was identical; only the keeping of it differed. Four seasons is the library's longest argument that documentation is not the paperwork after the work. It is the work.

## [end_december] Ending — December 1
*Day 456 — Tuesday, December 1, 2026 (dayOffset 456)*

Tuesday, December 1, 2026 arrives in this branch the way the wheel promised: as the elder children's fifteenth month, with the hearing unheld or unanswered and the filing question now the whole case. Nico's date waits four weeks behind his siblings', as it has since the Septembers.

The exceptions exist — they always existed — in the year's events. The litigation of the winter will be about whether they exist in the case plan, in writing, which is the only place the statute reads. The family that lived the exceptions will now have to prove them backward, from memory, at winter prices.

**Ending.**

**Debrief:**
- THE DATES, AS PROMISED — September 1, 2025 + 15 months = Tuesday, December 1, 2026 (elders); September 29, 2025 + 15 months = Tuesday, December 29, 2026 (Nico). 42 U.S.C. § 675(5)(E). Nothing about December was a surprise except that it arrived, which is what dates do when their answers are postponed.
- WHAT NO STRATEGY CONTROLS — Continuances in the second fall are the clock's home-field advantage. The route's defense was positional: exceptions built in the summer, the position answered in writing, the hearing reached in October with the binder already filed. Postponement is a strategy too — the other side's.
