# THE FIRST 90 DAYS — Scenario 94: “The Custodianship Question”

*Human-readable script. This document and `scenario-94.json` are generated from a single source and match node-for-node: same IDs, same order, same choices, same effects.*

**The family is fictional — a composite. No real person's story appears here.**

**Content note:** This scenario depicts a permanent legal custodianship petition and the negotiation and hearing that decide it. There is no graphic content. Players may skip any scene or use the quick exit at any time.

**How to read effects:** `cash −40` changes the player's cash. `FLAG: name` sets a flag the engine tracks. `HIDDEN + item` means the case file quietly records that item at this choice — the player does not see it when it happens. `REQUIRES FLAG: name` means the choice is only available if that flag was set earlier; `REQUIRES NO FLAG: name` means it is only available if that flag was never set. `NOTE:` is text shown to the player right after choosing.

Start date: Monday, June 1, 2026. Day offsets are days since the scenario's start date.

## [start] The Petition With His Name Spelled Right
*Day 0 — Monday, June 1, 2026 (dayOffset 0)*

Your name is Thaddeus Cole. Your daughter Pearl is four. She has lived with her aunt Sabine — your late wife's sister, who took her in the week everything came apart — for twenty-two months, which is to say, for most of the life Pearl can remember and all of the life she narrates.

The envelope is a petition: Sabine, through a lawyer, asks the court to make her Pearl's permanent legal custodian — one of the outcomes on the permanency menu (42 Pa.C.S. § 6351(f.1)) — and to close the dependency case. It is not an adoption petition. It does not ask to end your rights or your name. It asks to make permanent the arrangement that already exists, with you as a father at the level of visits, holidays, and goodwill.

You have been stable for eight months: employed, housed, treated, tested, present. You have been Pearl's father, in the daily sense, for the first twenty-six months and in the visiting sense for the twenty-two since. The hearing is August 17. What you ask for in that room, and what you build between now and then, will decide which of those two fatherhoods the law makes durable.

The family is fictional — a composite. The arithmetic of a four-year-old's memory is real arithmetic.

**Choices:**
- Take the petition to your lawyer and ask for the whole truth, itemized → **intake**
  - NOTE (shown after choosing): Mr. Beaumont has represented you since the second hearing. He has never once told you what you wanted to hear in the first ten minutes. It is why you keep him.

## [intake] The Intake Call
*Day 1 — Tuesday, June 2, 2026 (dayOffset 1)*

"Before strategy, facts," Mr. Beaumont says. "I have read the petition. It is well drawn and it is not vindictive — Sabine's position is Pearl's continuity, and on the current record it is not a weak position. Ours is your eight months and your trajectory. August 17 is where those two truths meet, and the court will choose an outcome from the permanency menu: return to you, adoption with termination — not sought here — permanent legal custodianship, or the others (42 Pa.C.S. § 6351(f.1)).

"Come in Thursday. We will talk about what winning means — all three things it could mean, and what each costs Pearl and you. Bring your folder. And Thaddeus: between now and August, everything is evidence, including the asking."

**Choices:**
- Ask what to do before Thursday → **records**
  - NOTE (shown after choosing): 'Read your own case,' he says. 'The whole record, not the parts you remember. It's releasable on request. You know the rule by now. Use it like you mean it.'

## [records] Reading Twenty-Two Months
*Day 6 — Sunday, June 7, 2026 (dayOffset 6)*

The complete agency record, requested in writing under 55 Pa. Code § 3130.44(d) at $10 in copy costs, arrives in two binders. It contains your worst year in the third person and your eight good months in noticeably thinner detail — the asymmetry of files, which record trouble at length and progress in summary. It also contains Sabine's letters, the visit logs, Pearl's preschool notes, and the permanency history that produced this petition. Reading it is the worst evening of the summer and the most necessary.

**Choices:**
- Read both binders and mark every place progress is understated → **work_letter** _(cash −10 ; FLAG: recordsRequested ; HIDDEN + Record — complete agency file requested in writing and read in full by the father)_
  - NOTE (shown after choosing): Eleven marks. Eleven places where the file's summary is thinner than its own attachments. A hearing is where those eleven places get argued from.
- Read your sections and skip Sabine's letters → **work_letter**
  - NOTE (shown after choosing): Her letters are the other side's case, written in advance, in kindness. Skipping them doesn't thin them; it only thins your preparation.

## [work_letter] The Letter From the Warehouse
*Day 8 — Tuesday, June 9, 2026 (dayOffset 8)*

Your employer's letter exists in the same sense your schedule letter did: potentially. The warehouse manager runs a crew of thirty and regards paperwork as a personal insult, but he has watched you for eight months — no call-offs since January, voluntary Saturdays, the forklift certification in May. His signed account is an exhibit. His unsigned goodwill is a mood.

**Choices:**
- Ask him for the signed letter, with dates, like a man asking a favor and meaning it → **fitness_audit** _(FLAG: workLetter ; HIDDEN + Employment — signed letter documenting eight months of stability obtained)_
  - NOTE (shown after choosing): He signs it with the air of a man defusing something. 'Eight months is eight months,' he says. 'Paper should say so.'
- Let his goodwill stand in for the document → **fitness_audit**
  - NOTE (shown after choosing): Goodwill testifies only if subpoenaed by events. Letters testify on schedule.

## [fitness_audit] The Audit of Eight Months
*Day 10 — Thursday, June 11, 2026 (dayOffset 10)*

The clinic's paralegal lays your fitness record out like a pre-flight check: treatment completion certificates; eight months of clean screens, tabulated; the lease and rent receipts; the work letter; the counselor's letter; the visit log — unbroken, twenty-two months of Sundays and then Saturdays too. Assembling it into one indexed packet costs $10 and an afternoon, and produces the object this hearing will actually be about: not your past, which is conceded, but whether your present is documented well enough to build a child's future on — yours, or yours alongside Sabine's.

**Choices:**
- Assemble the fitness packet, indexed, with the tabulation → **pearl_weekend** _(cash −10 ; FLAG: fitnessRecord ; HIDDEN + Fitness record — eight months of stability assembled as an indexed exhibit packet)_
  - NOTE (shown after choosing): Indexed. The packet does not argue that the bad year didn't happen. It argues, with tabs, about what kind of fact the good months are.
- Keep the documents in their separate envelopes, as issued → **pearl_weekend**
  - NOTE (shown after choosing): Envelopes are where documents live before they become evidence. Hearings run on the second state of matter.

## [pearl_weekend] Weekends With Pearl
*Day 14 — Monday, June 15, 2026 (dayOffset 14)*

Your visits now run Saturday to Sunday morning, at your apartment, with the second bedroom that is Pearl's in every sense except the order's. She has a toothbrush there, strong opinions about pancakes, and a drawing of the household — Sabine's house, your apartment, both with suns — taped to your refrigerator by its author. The visit log records these weekends in the agency's minimalist prose: 'Visit occurred. Child returned.'

The difference between that prose and what is actually happening on these weekends is, more or less, the hearing.

**Choices:**
- Ask, in writing, for the log to note the overnights, the routines, the returns → **aunt_history** _(FLAG: visitLog ; HIDDEN + Visit log — overnight visits documented specifically, in writing)_
  - NOTE (shown after choosing): The log acquires texture: bedtime story, pancake, church with Sabine, returned fed and narrating. An ordinary childhood, countersigned.
- Let the log stay minimal — the judge knows visits matter → **aunt_history**
  - NOTE (shown after choosing): Judges know what files tell them. This file, unedited, says your weekends are two sentences long.

## [aunt_history] The Aunt, Fairly Considered
*Day 18 — Friday, June 19, 2026 (dayOffset 18)*

Sabine's case, read fairly in her letters and the preschool notes, is not about you at all. It is about a four-year-old's nervous system: Pearl's routines, her night terrors ended, her world made of two houses and one primary one. Sabine does not say you are unfit. She says Pearl is attached — to her, to the house, to the order of days — and that the court's outcome should be the one that does not reorganize a four-year-old's life around an eight-month-old stability, however real. It is a strong argument. It is strengthened, not weakened, by the fact that Sabine has been fair to you in every dealing for two years, and the record shows that too.

Mr. Beaumont's phrase for it: 'We are not fighting a villain, Thaddeus. We are fighting a calendar — hers is twenty-two months long and yours is eight. Everything we do must respect what that calendar means to a four-year-old, or the court will do it for us.'

**Choices:**
- Ask him what respecting it looks like as a strategy → **mailbox2**
  - NOTE (shown after choosing): 'It looks like this: we stop asking what you deserve, and start asking what can be built that holds Pearl's world together and your fatherhood in it — permanently, in an order, not at anyone's goodwill. Bring me your terms on Thursday. Real ones.'

## [mailbox2] The Envelope From Sabine's Lawyer
*Day 20 — Sunday, June 21, 2026 (dayOffset 20)*

The letter is courteous and complete: Sabine's counsel proposes, without prejudice, that the parties discuss terms before August — including, if custodianship is granted, 'reasonable contact as the parties may agree.' Reasonable, as the parties may agree: eight words containing, by your count, no enforceable content whatsoever. Contact that exists by agreement exists by permission; permission, unlike an order, can be withdrawn by a mood, a move, a new marriage, a bad year.

Mr. Beaumont underlines one phrase and writes in the margin the sentence that reorganizes your summer: 'Terms are only real if a judge signs them.'

**Choices:**
- Write your terms — real ones, specific enough for a judge to sign → **negotiate_open**
  - NOTE (shown after choosing): Thursday's list has numbers in it: dinners, weekends, holidays, school events, a yearly review. Numbers are what turn goodwill into an order.

## [negotiate_open] The Kitchen-Table Negotiation
*Day 24 — Thursday, June 25, 2026 (dayOffset 24)*

The first negotiation happens, at Sabine's suggestion, at her kitchen table — the room where Pearl's life is headquartered. You bring the terms, written: if custodianship is granted, then contact entered in the order itself — one dinner weekly, one weekend monthly, named holidays alternating, attendance at school and medical events, and a yearly review of the arrangement with the case's closure conditioned on a year of the terms working. Sabine reads it twice. 'You'd still be asking for her back someday,' she says. 'No,' you say, and hear how true it is as you say it. 'I'm asking that being her father not be a favor anyone grants me. The rest, her life decides.'

She does not agree. She does not refuse. She says the word that starts actual negotiations: 'Mediation.'

**Choices:**
- Take the written terms to mediation as the opening position → **letter_pearl** _(FLAG: contactTermsDraft ; HIDDEN + Negotiation — written contact terms proposed for entry in any custodianship order)_
  - NOTE (shown after choosing): Terms, in writing, with numbers. Whatever August brings, this page will exist in it: a father's ask, specified, reasonable, and refusals of it therefore also specified.
- Keep terms flexible and verbal until the hearing → **letter_pearl**
  - NOTE (shown after choosing): Flexibility is a virtue in families and a solvent in orders. What is not written by August will not be signed in August.

## [letter_pearl] The Drawing, Explained
*Day 28 — Monday, June 29, 2026 (dayOffset 28)*

Pearl explains her drawing during Sunday's visit with the seriousness of an artist at a retrospective: 'This house is Auntie's. This house is yours. The suns are because both.' She is four. She has solved, in crayon, the structure the adults are litigating in prose — two houses, both real, one child entitled to both suns. Whatever August decides will be measured by her against this drawing, though she will not have words for the measuring for twenty years.

**Choices:**
- Ask if the drawing can go in your packet — with her permission, solemnly obtained → **mediation** _(FLAG: drawingFiled)_
  - NOTE (shown after choosing): Permission is granted, with conditions about the good crayons. The drawing goes in the packet's last tab, behind the certificates. Lawyers will call it demonstrative. Pearl calls it the suns page.

## [mediation] The Mediated Afternoon
*Day 31 — Thursday, July 2, 2026 (dayOffset 31)*

The mediator is a retired judge with no patience for adjectives and a gift for calendars. By the second hour, the terms have hardened from proposal to draft order language: weekly dinner, monthly weekend, alternating named holidays, school and medical access, a twelve-month review, and — Sabine's addition, offered in good faith and accepted in the same — a provision that if the terms are kept for two years, the parties will jointly consider expanded time without a contested hearing. What remains unsigned is the threshold question itself: Sabine's consent extends to the terms if custodianship is granted. Whether it should be granted is still, formally, the court's.

The walk-out scenario exists in every mediation: the moment where the threshold question swallows the terms.

**Choices:**
- Sign the mediated terms, conditioned on the court's custodianship decision → **clinic_check** _(FLAG: contactTerms ; HIDDEN + Mediation — contact terms agreed in writing, for entry in the order if custodianship is granted)_
  - NOTE (shown after choosing): Signed, both names, terms with numbers. If August grants custodianship, the contact will be law, not goodwill. If August returns Pearl, the terms were never needed. Either way, they exist.
- Walk out when the threshold question is raised — return first, terms after → **mediation_fail**
  - NOTE (shown after choosing): The threshold question was always going to be raised; it is the hearing. Walking out raises it in the worst available room: the one with a judge and no draft terms in it.

## [mediation_fail] The Quiet After Mediation
*Day 34 — Sunday, July 5, 2026 (dayOffset 34)*

The mediation ends without terms. Sabine's counsel writes, courteously, that his client remains open to 'reasonable contact as the parties may agree' after the hearing. The eight words again. Mr. Beaumont is unsparing at the debrief: 'We now go to August with the threshold question and nothing else. If we lose the threshold, your contact will be whatever the order's boilerplate says, which is whatever Sabine's goodwill says, which is a sentence I never want to explain to Pearl at fourteen.'

The fitness packet, at least, is real. The contest will be fought on it, alone, at full length.

**Choices:**
- Prepare the contest on the fitness record alone → **school_letter**
  - NOTE (shown after choosing): Alone is a strategy too. It is simply the one with no floor under it.

## [clinic_check] The Clinic Checks the Draft
*Day 35 — Monday, July 6, 2026 (dayOffset 35)*

A second legal eye — the clinic's custody-review volunteer, a retired practitioner with annotated margins — reads the mediated terms against one question: could a judge sign this as an order and could a sheriff, a school, a hospital honor it? Two clauses get numbers they lacked (dinner pickup at 5:30; the weekend defined as Friday 6 p.m. to Sunday 6 p.m.). Terms that survive clocks are the only kind worth August.

**Choices:**
- Adopt the tightened terms as the family's position → **school_letter** _(FLAG: termsChecked ; HIDDEN + Terms — mediated contact terms tightened to order-ready specificity)_
  - NOTE (shown after choosing): 5:30 pickups and defined weekends. Affection, being unmeasurable, was left out of the draft on purpose. It has its own exhibits.

## [school_letter] The Preschool Letter
*Day 38 — Thursday, July 9, 2026 (dayOffset 38)*

Pearl's preschool teacher writes the letter both sides will cite: Pearl is securely attached in her routines; transitions between her two houses are 'unremarkable, which at four is the highest praise available'; she talks about her father in the present tense and her aunt in the permanent one, and the teacher declines, professionally, to call either fact a problem. It is the fairest document in the case, and it supports the honest version of both arguments — which is why it will be quoted twice in August, once by each side, at different paragraphs.

**Choices:**
- File the letter with the fitness packet and send Sabine a copy → **photo_book** _(FLAG: schoolLetter ; HIDDEN + School — preschool letter on attachment and transitions filed; copy shared with the aunt)_
  - NOTE (shown after choosing): Sent to Sabine too, because this negotiation runs on a family's currency: nobody ambushes anybody with a preschool teacher. The record grows; the trust, carefully, grows with it.
- Hold the letter for the hearing as a surprise → **photo_book**
  - NOTE (shown after choosing): Surprises are for birthdays. In hearings they read as tactics, and tactics read as admissions that the merits needed help.

## [photo_book] The Photo Book You Compile Anyway
*Day 41 — Sunday, July 12, 2026 (dayOffset 41)*

You compile it for Pearl, not the court: the weekends, the drawings, the pancake era, in a drugstore photo book with captions in your hand. One copy for her room at Sabine's, one for your apartment. It is not an exhibit. It is the underlying asset all the exhibits are about, and making it — calmly, in July, for a four-year-old's bookshelf — is itself a data point about the kind of father the eight months built, though no lawyer will ever cite a photo book and this one is no exception.

**Choices:**
- Deliver her copy at Sunday's visit → **packet**
  - NOTE (shown after choosing): It goes on her shelf between the suns drawing and the library books. The case file and the bookshelf are, for once, in agreement about what matters.

## [packet] Two Packets
*Day 45 — Thursday, July 16, 2026 (dayOffset 45)*

By August's approach, the case exists as two packets. Sabine's: the petition, her letters, the preschool letter's first half, twenty-two months of continuity. Yours: the fitness record, the mediated terms, the preschool letter's second half, the same twenty-two months read from the other house. Mr. Beaumont files yours with the court and serves it properly, because a packet that surprises no one is a packet that can be agreed with in advance — and much of August's outcome may be negotiated in its shadow before a judge says a word.

**Choices:**
- File the packet and let its shadow do the quiet work → **sister_call** _(FLAG: packetFiled ; HIDDEN + Fitness packet — filed and served before the hearing; negotiations conducted in its light)_
  - NOTE (shown after choosing): Filed. In the following week, Sabine's counsel calls twice. Packets with tabs have that effect on telephones.
- Hold the packet for the hearing itself → **sister_call**
  - NOTE (shown after choosing): Held packets persuade judges. Filed packets persuade everyone, earlier, cheaper. August will provide a judge either way; the question is what she'll have already read.

## [sister_call] Your Sister Asks What You Want
*Day 48 — Sunday, July 19, 2026 (dayOffset 48)*

Your sister — Pearl's other aunt, the family's referee — asks the direct question over the phone: 'If the judge offered you a choice, today: Pearl home with conditions and the case open for years, or Sabine's house with your fatherhood in the order, signed, and the case closed — which do you take?' It is the hearing's whole content, asked at kitchen-table scale, and the answer takes you a full minute. The minute is honest. It contains Pearl at two, Pearl at four, the bad year, the eight months, a drawing with two suns.

**Choices:**
- Answer her the way you'll answer in August: the order that holds both suns → **agency_position**
  - NOTE (shown after choosing): 'Then build for that,' she says, 'and stop apologizing for the shape of it. Pearl drew it first.'

## [agency_position] The Agency's Position
*Day 52 — Thursday, July 23, 2026 (dayOffset 52)*

The agency's report for August lands where agencies land: it supports custodianship with Sabine — continuity, licensure-clean, the file's inertia arranged as reasoning — and it addresses your contact in the eight words, 'as the parties may agree.' Its treatment of your eight months is two paragraphs longer than the binders' summaries were, because the filed packet had to be answered. The report cannot be called unfair. It can be called incomplete in the precise places your packet is complete, and August will feature a judge reading both.

**Choices:**
- Note the eight words and prepare to answer them with the mediated terms → **savings**
  - NOTE (shown after choosing): Your answer is a signed document with pickup times in it. The hearing will compare the two offers on specificity alone, if it comes to that. Specificity is a home game for you now.

## [savings] The Envelope Marked 'Pearl'
*Day 55 — Sunday, July 26, 2026 (dayOffset 55)*

It is not evidence and never enters the packet: your savings account, eight months of small deposits, labeled in the bank's memo field by a teller who asked no questions: PEARL. College, a car, a wedding, a deposit on an apartment near whichever school — its purpose is unspecified because its depositor is four years from every version of its use except one: it exists, monthly, like the visits, like the screens, like the rent. A father's seriousness, kept in the only ledger that never gets filed. August will not see it. Pearl, at some age, will. This story keeps both kinds of records in view because families do.

**Choices:**
- Make August's deposit early and turn back to the case → **family_meeting**
  - NOTE (shown after choosing): Deposited. The case resumes. The two ledgers of fatherhood proceed in parallel, as they will for years, under every outcome August offers.

## [family_meeting] The Family Meeting
*Day 59 — Thursday, July 30, 2026 (dayOffset 59)*

The last meeting before August happens at Sabine's table, with counsel excused by mutual agreement and the mediator's draft on the table like a treaty map. Sabine has read your packet — served papers have that effect in families — and she says the thing two years of fairness have earned her the right to say: 'If the court gives her to me permanently, I want your terms in the order. Not because a judge makes me. Because Pearl should never have to wonder if her father is allowed. Put it in the joint statement.'

It goes in the joint statement: the parties agree on contact terms, in the event of custodianship, as drafted. The threshold question — custodianship or return — remains for the court, now the only question left, which is what negotiation is for.

**Choices:**
- Sign the joint statement and prepare to argue the one remaining question → **dinner_test** _(FLAG: auntAgreed ; HIDDEN + Joint statement — parties agree contact terms will be entered in any custodianship order)_
  - NOTE (shown after choosing): Signed at the table where Pearl does her homework. The hearing is now one question wide. Everything else in this family's life has been, laboriously, agreed.
- Refuse the joint statement — agreement feels like surrender → **dinner_test**
  - NOTE (shown after choosing): It feels like it. It functions as the opposite: it removes your worst outcome from the table permanently. Feelings are data; they are not always right.

## [dinner_test] The Test Dinner
*Day 63 — Monday, August 3, 2026 (dayOffset 63)*

Under the draft terms, unexecuted, the family informally runs the schedule for two weeks in July: the Wednesday dinner at 5:30 pickup, the weekend Friday-to-Sunday. It costs $12 in gas and groceries and it works the way schedules work when they're built from a real child's life: unremarkably. Pearl narrates the arrangement to her preschool teacher as 'Daddy Wednesdays,' a phrase that will not appear in any order and will outlast most of what does.

**Choices:**
- Note the two weeks' success for the hearing packet's final page → **hearing_prep** _(cash −12 ; FLAG: termsTested ; HIDDEN + Terms — negotiated schedule informally tested for two weeks; functioned as drafted)_
  - NOTE (shown after choosing): The packet's last page: the terms, run in real life, unremarkable. At four, as the teacher said, unremarkable is the highest praise available.

## [hearing_prep] The Night Before
*Day 70 — Monday, August 10, 2026 (dayOffset 70)*

Mr. Beaumont's final prep is one page: the threshold question, your testimony's three sentences, the terms if the threshold goes Sabine's way, the conditions you'll accept if it goes yours. 'Whatever happens,' he says, 'you will not be surprised by your own positions. In my experience that puts you ahead of half the parents who've sat in that chair, including some who won.'

Pearl is asleep at Sabine's. The drawing is on your refrigerator. The packet is closed. Everything that could be written has been written by someone; the rest is a judge reading it, and a four-year-old's life being decided at the speed of law.

**Choices:**
- Sleep, and be at the courthouse early → **courthouse**
  - NOTE (shown after choosing): Early, with the folder, in the suit that has now attended every hearing of Pearl's life and is showing it.

## [courthouse] The Hallway Bench
*Day 74 — Friday, August 14, 2026 (dayOffset 74)*

Sabine is on the other bench with her counsel, and Pearl is at preschool being four, which is where the system, at its best, arranges for the subject of all this to be during the deciding of it. Sabine crosses the hallway once: 'Whatever she decides,' she says, 'the terms stand between us. I put it in writing.' 'I know,' you say. 'That's why we're both calm.' Neither of you is calm. Both of you are something better: prepared, in writing, by each other.

**Choices:**
- Go in for the one remaining question → **hearing**
  - NOTE (shown after choosing): One question wide. A summer's work made it that narrow. Narrow questions get careful answers.

## [hearing] The Custodianship Hearing
*Day 77 — Monday, August 17, 2026 (dayOffset 77)*

The judge reads the case the way it was built: the history conceded, the eight months examined, Pearl's world described by the preschool letter quoted from both ends. The threshold question is argued fully — your counsel on trajectory and the packet, Sabine's on continuity and the calendar — and the court turns, in the end, to the man in the chair. What Thaddeus asks for, now, in his own voice, is the last exhibit.

**Choices:**
- Consent to custodianship IF the negotiated terms are entered in the order, and say why: Pearl's world should not be reorganized to honor your calendar → **out_consent** _(REQUIRES FLAG: contactTerms ; REQUIRES FLAG: fitnessRecord)_
  - NOTE (shown after choosing): The room is very quiet. Sabine's counsel is already nodding at the draft. Your lawyer closes his folder. You have asked for your fatherhood to be made law at the price of the threshold — and the price, everyone in the room understands, is real.
- Contest the threshold: ask for Pearl's return under conditions, on the fitness record → **out_contest** _(REQUIRES FLAG: fitnessRecord)_
  - NOTE (shown after choosing): Eight months, tabulated and indexed, against twenty-two months of a four-year-old's memory. The argument is honest, complete, and exactly as strong as the record makes it — no stronger.
- Consent to custodianship on the agency's wording — contact as the parties may agree → **out_bare**
  - NOTE (shown after choosing): The eight words. Offered now as a settlement of everything, by the side that knows precisely what they're worth in an order: the paper they're not printed on.
- Argue that the case should never have happened and Pearl should simply come home today → **out_contested_loss**
  - NOTE (shown after choosing): The judge's pen stops. Two years of record do not stop with it. Some arguments reopen doors; this one closes the room's sympathy like a door.

## [out_consent] Custodianship, With His Name in the Order
*Day 77 — Monday, August 17, 2026 (dayOffset 77)*

The court grants permanent legal custodianship to Sabine — and enters the terms. All of them: the Wednesday dinners with the 5:30 pickup, the monthly weekend defined to the hour, the alternating holidays by name, school and medical access, the twelve-month review, the two-year expansion provision. The judge states the reasoning on the record: the child's continuity is preserved; the father's documented stability and the parties' negotiated terms make his role a matter of law rather than permission; the dependency case is closed.

'Mr. Cole,' the judge says, 'the court notes this outcome was substantially of your making.' It was. That is its cost and its dignity, in the same sentence, forever.

**Choices:**
- Sign the acknowledgment and walk out with the order → **consent_order**
  - NOTE (shown after choosing): The order has your name in it nine times. A father's name, in operative clauses, with times attached.

## [out_contest] The Threshold, Contested
*Day 77 — Monday, August 17, 2026 (dayOffset 77)*

The contest is fully heard — the packet credited, the eight months found genuine and documented, the trajectory praised in terms that will read well in the order. And then the calendar is weighed, as Mr. Beaumont promised it would be: twenty-two months of a four-year-old's remembered life, in one house, against eight months of a father's rebuilt one. The court grants custodianship to Sabine, and because the threshold was contested to the end, the contact question is decided by the court from the papers before it — the agency's report among them, with its eight words, and no joint statement to displace them, the parties having spent their agreement on the argument.

Contact is set at the court's standard formulation: reasonable, as the parties may agree, with two Sunday afternoons specified 'at minimum.'

**Choices:**
- Walk out with the order and its minimums → **contest_ruling**
  - NOTE (shown after choosing): Minimums. The word does more work in that sentence than any other, and none of it is good.

## [contest_ruling] The Minimums, Itemized
*Day 80 — Thursday, August 20, 2026 (dayOffset 80)*

In the car, Mr. Beaumont itemizes without comfort: the terms you negotiated are not in the order; the joint statement was never signed; Sabine's goodwill survives, genuinely — she has already texted about Wednesday — but goodwill is not in the order either, and orders outlast goodwill the way paper outlasts weather. 'You were entitled to contest it,' he says. 'It was your right and it was honestly arguable. This is what the arguable cost. I would rather you heard it from me than discovered it at a school gate in October.'

**Choices:**
- Go home and put the first Wednesday on the calendar anyway → **end_returned**
  - NOTE (shown after choosing): Wednesday, by text, by goodwill. The calendar holds it the way it holds everything not in an order: hopefully.

## [out_bare] Custodianship, On Eight Words
*Day 77 — Monday, August 17, 2026 (dayOffset 77)*

The court grants custodianship to Sabine and adopts, for contact, the formulation both packets carried at some point and only one side still wanted: reasonable contact, as the parties may agree. The hearing lasts forty minutes. The mediated terms — printed, signed by no one, superseded by a consent you offered to end the morning early — are not mentioned, because papers that are not presented are not ruled on, and papers that are not ruled on do not exist in orders.

**Choices:**
- Walk out with the shortest order of your life → **bare_order**
  - NOTE (shown after choosing): Two pages. Pearl's whole legal childhood, at the density of a weather report.

## [bare_order] The Order, At the Kitchen Table
*Day 81 — Friday, August 21, 2026 (dayOffset 81)*

Read at your kitchen table, the order gives Sabine permanence and you a phrase. Sabine herself is embarrassed by it — she calls that evening, decent as ever, and says the Wednesdays will happen, the weekends will happen, 'as if it were written.' For now, in her house, they will. The order will also still exist in ten years, in moves and marriages and disagreements no one can foresee, and on those days the difference between 'as if it were written' and 'written' will be the only difference in the world.

**Choices:**
- Thank her, and keep every term as if it were ordered → **end_plc_bare**
  - NOTE (shown after choosing): You will keep them. That was never the variable. The variable was whether anyone else had to.

## [out_contested_loss] The Hearing, Lost in the Arguing
*Day 77 — Monday, August 17, 2026 (dayOffset 77)*

The grievance argument takes eleven minutes and the room. By its end, the court has heard a father's account of the system's failures — several of them legitimate, none of them the question presented — and has stopped hearing the father's evidence, which was considerable. Custodianship is granted to Sabine. Contact is set at supervised-to-unsupervised progression 'as the custodian deems appropriate to the child's adjustment' — the most discretionary sentence available, awarded to the record's angriest presentation. The fitness packet is noted as received. Received is the verb orders use for paper they did not rely on.

**Choices:**
- Walk out past the bench where Sabine sits with her head in her hands → **loss_order**
  - NOTE (shown after choosing): Even she didn't want this version. Winning everything, it turns out, was not what her fairness was for.

## [loss_order] The Order, At the Kitchen Table
*Day 81 — Friday, August 21, 2026 (dayOffset 81)*

The order is read at the kitchen table where your terms were drafted in June. The terms are still there, in the drawer, unsigned by any judge: pickups, weekends, holidays, a whole fatherhood at specific hours — an order that exists in every respect except the one that makes orders orders. Pearl's Wednesdays will now occur as her custodian deems appropriate. Sabine deems generously, this year. The document in the drawer is addressed to the years after generosity is the only guarantor anyone needs it not to be.

**Choices:**
- File the draft terms behind the order, where the century can find them → **end_loss**
  - NOTE (shown after choosing): Paper keeps. That was the doctrine. It applies to the roads not taken, too, and it is not always a comfort.

## [consent_order] The Order, At the Kitchen Table
*Day 81 — Friday, August 21, 2026 (dayOffset 81)*

The order is nine pages, and page four is the one you read at the table until the words are memorized: the contact terms, verbatim from the mediated draft, with the hours and the holidays and the review. Pearl's drawing gets a successor that evening — she is told, in four-year-old units, that Daddy Wednesdays are 'in the judge's book now,' and she accepts this with the gravity of a child whose world has just been made more, not less, predictable.

'Both suns,' she says, inspecting the fridge door, where the old drawing has been joined by the new calendar. 'In the book.'

**Choices:**
- Start the first ordered Wednesday → **end_plc_contact**
  - NOTE (shown after choosing): Wednesday, 5:30 pickup, as ordered. The most ordinary sentence in this story, and the one it was all for.

## [end_plc_contact] Ending — Custody With His Name in the Order
*Day 84 — Monday, August 24, 2026 (dayOffset 84)*

Pearl lives with Sabine, permanently, lawfully — and her father is in the order: Wednesdays, weekends, holidays, school doors open to him, a review in twelve months, expansion in two years if the terms are kept, which they will be, because they were built from the child's actual life and tested in it before any judge signed them. The dependency case is closed. No agency worker will summarize Thaddeus again. His fatherhood is a legal fact with times attached, in a book a four-year-old has already been told about.

He did not get the threshold. He decided — on a record he built for the purpose of deciding honestly — that Pearl's twenty-two months outweighed his eight as the thing a court should protect first, and he spent his leverage making the consequence durable instead of deniable. That is the most adult outcome this simulation contains, and the guide names it without flinching:

**ENDING — Debrief:**

THE WIN, NAMED HONESTLY — A partial win, and this scenario's best: permanent legal custodianship to the aunt (the § 6351(f.1) legal-custodian outcome) WITH the father's contact entered as enforceable terms. It is partial because Pearl does not come home and the case's closure ends the reunification track as a court matter. It is the best because, on this record — twenty-two months of a four-year-old's attachment against eight documented months of stability — it is the strongest outcome that protects both the child's continuity and the father's permanence, and it was reached by construction, not surrender: the fitness record made his terms worth entering; the terms made the outcome bearable; the honesty made it signable.

THE LAW IN THE BEATS — The outcome menu is 42 Pa.C.S. § 6351(f.1), chosen after § 6351(f)'s determinations; the record both sides argued from was built through 55 Pa. Code § 3130.44(d). The scenario states no statute for negotiated contact terms because none was needed: parties' agreed terms, presented to the court and entered in its order, are the ordinary mechanism by which contact survives a custodianship — the game teaches the mechanism, accurately labeled as practice built on the (f.1) outcome, not as a quoted rule.

THE HIGHEST-LEVERAGE MOVE — The written terms, taken to mediation in June. Everything August became was negotiated in their shadow. A close second: reading the complete record in June (§ 3130.44(d)), which is where the eleven understated places were found.

WHAT NO STRATEGY CONTROLS — Sabine's fairness (a different aunt makes this a different story), the judge's weighing of the calendars, Pearl's own future tellings of it. The route controlled the record, the terms, and the ask. It did not control whether the ask was wise — that was Thaddeus's, and the scenario's whole respect for him is that it was a decision, made with open eyes, at full information. Not every best outcome is the one where the parent gets the child back. This simulation was built to be able to say so.


## [end_returned] Ending — Contested, and the Minimums
*Day 84 — Monday, August 24, 2026 (dayOffset 84)*

Custodianship goes to Sabine after a full and honest contest, and Thaddeus's contact rests on a judicial minimum plus a family's goodwill. The Wednesdays happen — this year. The packet he built is part of the record forever, and if the arrangement ever degrades, that record is where a future modification argument starts. He spent his leverage on the threshold and lost it fairly, to a calendar that was simply longer than his, argued by a woman who had earned her standing in Pearl's life one ordinary day at a time.

The contest was his right. The guide does not call exercising it a mistake. It calls it what it was: a choice with a price, made at full information, whose price is itemized in the order's contact paragraph — or rather, in the paragraph that isn't there.

**ENDING — Debrief:**

NAMED HONESTLY — A middle outcome: the same custodianship as the best ending, minus the enforceable terms that made the best ending the best. The delta between the two endings is entirely composed of June and July — mediation, the joint statement, the signed draft — which is the scenario's thesis: in post-permanency practice, the negotiated paper is not a preliminary to the real fight. It is frequently the whole of what is winnable.

THE LAW IN THE BEATS — § 6351(f)'s determinations and (f.1)'s menu framed the hearing; the fitness record and the § 3130.44(d) file made the contest credible; nothing in the scenario's law promised that credibility a victory. Courts weigh a young child's continuity heavily — stated here as the documented pattern of the published cases this composite draws on, not as a quoted rule.

WHAT NO STRATEGY CONTROLS — The weighing itself. A different judge, the same record, might have returned Pearl under conditions, and this guide would then have a different middle ending to write. The route's claim is narrower than a prediction: it maximized the father's position under both outcomes of the threshold. This ending is what the threshold's loss looks like when the maximization was spent contesting rather than securing.


## [end_plc_bare] Ending — Custodianship, On Eight Words
*Day 84 — Monday, August 24, 2026 (dayOffset 84)*

Pearl's life continues almost unchanged — Sabine is Sabine, and the Wednesdays happen. Legally, her father is a phrase: 'reasonable contact, as the parties may agree.' The phrase will hold exactly as long as agreement does, and no longer, and everyone who signed the mediated draft in June knows precisely which drawer the alternative is filed in. The case is closed. The closure is real. So is the exposure it leaves.

This ending is what settling for the other side's language looks like when the other side's language was drafted to be weightless. It cost nothing in August. Its invoices arrive on the schedule of other people's lives: moves, marriages, illnesses, disagreements — the ordinary weather of a decade, against which an order is the only roof the law sells, and this family declined to buy one at the one moment it was for sale.

**ENDING — Debrief:**

WHY THIS ENDING — Courts enter the terms presented to them. Agreed, specific terms existed in this story — negotiated, mediated, tightened to order-ready form — and were never presented, because the hearing was settled on the agency's formulation first. The (f.1) custodianship outcome is identical to the best ending's; the entire difference is eight words versus nine pages, which is to say: everything that will matter in year three.

THE LAW IN THE BEATS — Nothing in the verified set was misused to reach this ending, and that is its bleakness: it is fully lawful. § 6351(f.1) supplied the outcome; no rule required the court to demand better contact language than the parties jointly offered it. The scenario's law library (§ 6351(f)/(f.1); § 3130.44(d)) is a floor and a menu, not a guardian. What protects a parent in an order is what the parent puts in it.

WHAT NO STRATEGY CONTROLS — Sabine's decency may make this ending indistinguishable from the best one for years. The scenario cannot promise the invoice arrives. It can only certify that the coverage was declined, in writing, at the price of ending a hearing forty minutes early.


## [end_loss] Ending — The Record, Received and Not Relied On
*Day 84 — Monday, August 24, 2026 (dayOffset 84)*

Custodianship to Sabine; contact at the custodian's discretion; a fitness packet 'received.' Thaddeus leaves the courthouse with less than he brought into the summer — not in rights, which a court can only partly give, but in the room's willingness to hear him, which he spent in eleven minutes on a question the hearing was not asking. Sabine, who never sought this version, becomes its administrator, and her fairness will now carry weight that paper was invented to carry instead.

Pearl's Wednesdays will happen at the discretion of a good woman. The story does not call that nothing. It calls it unprotected, which at the scale of a childhood is the difference between a bridge and a favor.

**ENDING — Debrief:**

WHY THIS ENDING — Hearings decide the questions presented, on the records presented, and advocacy that spends the court's attention on the system's general failures spends it from the specific account the child and father needed. The threshold question (§ 6351(f)/(f.1)) was argued by everyone in this ending except, in the end, the father's side — which was arguing 2024. The fitness record existed; the terms existed; neither was reached. This is the post-permanency version of the oldest lesson in the game: the record only counts if it is presented, in the room, on the day, to the question actually being decided.

WHAT NO STRATEGY CONTROLS — Very little in this ending was outside the player's control, and the guide says so because the doctrine of this game is honesty in both directions: workers, judges, and luck decide much in this system — and some endings are authored at the table, in the argument, by the side that loses them. This is one. Its consolation, such as it is: records keep, children grow, and a father whose packet exists can return to court when circumstances change, with the suns page still in the last tab.

