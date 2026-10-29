# Two Houses (a fictional composite) — Node-for-Node Script (Scenario 49)

Scenario 49 of *The First 90 Days* — script generated node-for-node from `scenario-49.json`; the JSON is the source of truth.

A fictional composite built from published Pennsylvania dependency practice and documented system patterns. Not a real family's case.

**Content note:** child removal, court hearings, family separation.

**How to read effects:** `cash` is money spent or received at that choice; `FLAG:` marks a fact the story remembers; `HIDDEN +` is an assessment item the player never sees scored; `REQUIRES:` gates a choice on an earlier fact; `NOTE:` is authorial, not spoken in-world. Endings are marked **Ending.** with a **Debrief:**.

**Start date:** Monday, February 16, 2026. **Tier:** Hard. **Start cash:** $190.

---

## [start] The night of the fire

*Day 0 — Monday, February 16, 2026*

The furnace fire did not hurt anybody, and it took everything anyway: the apartment is red-tagged, your shifts at the warehouse come with a cot at your cousin's for you, and Kira (ten) and Micah (six) are, as of tonight, in two different foster homes across the county from each other — because the emergency list had no house with two open beds, and a sibling set of two is, to a placement desk at midnight, a math problem.

The caseworker, Ms. Moreau, is apologetic in the practiced way of someone delivering weather. "It's temporary. We'll work on getting them together." Temporary is a word whose meaning depends entirely on who is keeping the calendar.

**Choices:**
- Ask — tonight, before she leaves — "Who keeps the calendar on 'together,' and when is it reviewed?" Get the hearing date and write it on the shelter's discharge paper. → **the_date**  _(HIDDEN + placement-split)_

## [the_date] The date

*Day 0 — Monday, February 16, 2026*

The shelter care hearing is Thursday — emergency placements get reviewed within 72 hours by law (42 Pa.C.S. § 6332). Cohesion is not on that hearing's short agenda; custody is. But Ms. Moreau, pinned gently to specifics, gives you two useful things: the names of both foster homes' neighborhoods, and confirmation that the children can see each other — visits between siblings are arranged, not automatic, and arranging starts with asking.

On the bus back to your cousin's couch, you make the call that this whole scenario will turn on. Your great-aunt Odette — your grandmother's sister, sixty-three, retired from the school cafeteria, in the brick house on Walnut with the porch — has two spare rooms and has been asking about the children since midnight.

**Choices:**
- Call her now, from the bus, and ask the question whole: "Aunt Odette — both of them. Your house. Would you?" → **aunt_call**

## [aunt_call] Odette

*Day 1 — Tuesday, February 17, 2026*

She answers like the phone insulted her by ringing so late with so obvious a question. "Boy, I changed your diapers in that house. Get me whatever papers they need. Both rooms. Kira gets the blue one — she'll say it's hers anyway." Then, practical as a tide table: "My grandson Tomas stays some weekends when his shift runs late. He's twenty-four. Sleeps on the third floor. That's part of the house too. Put it in whatever they ask."

A household is everyone who sleeps under the roof — on the form, in the study, and in the truth. Odette has just handed you the fact that will make or break her application, depending on what you do with it.

**Choices:**
- Put Odette's offer in writing to the agency tomorrow — full name, address, phone, both children named, and Tomas's weekend stays stated in the letter itself. → **letter_full**  _(FLAG: kinNamedWritten; FLAG: householdHonest; HIDDEN + named-kin)_
- Put Odette's offer in writing tomorrow — name, address, phone, both children. Tomas is a grown man with his own apartment; weekends hardly count as living there. Leave him out of it. → **letter_short**  _(FLAG: kinNamedWritten)_

## [letter_short] The shorter letter

*Day 2 — Wednesday, February 18, 2026*

The letter goes in clean and simple, and that is exactly its problem. Somewhere in a database the agency can search — because agencies search households, not just people — Tomas's name is attached to that address from an old matter in another county. It may be nothing. It may be a dismissed charge from when he was nineteen. But the study will find it, and when it does, the question will not be about Tomas. It will be about the letter that didn't mention him.

You hear about the match from Ms. Moreau, carefully, a week later — and spend the rest of the study climbing out of a hole labeled 'omission.'

**Choices:**
- Correct it in writing, immediately and completely: Tomas's full name, his own address, his weekend pattern, and an apology for the gap — then help Odette get his clearances started anyway. → **hearing49**  _(cash −10; FLAG: omissionCorrected)_

## [letter_full] The whole letter

*Day 2 — Wednesday, February 18, 2026*

Your letter names everybody who sleeps in that house, including the one who sleeps there eight nights a month. Ms. Moreau reads it and does something that tells you the letter worked: she starts asking you questions about Tomas as logistics, not as secrets. "He'll need clearances too, as a household member for study purposes. Can he get fingerprinted this week?"

A disclosed complication is a task. An undisclosed one is a finding.

**Choices:**
- Call Tomas yourself. "Aunt Odette's taking the kids. The county needs your prints. It's not about you — it's the shape of the house." → **hearing49**

## [hearing49] Thursday — shelter care

*Day 3 — Thursday, February 19, 2026*

The shelter care hearing is short and mostly about custody, not addresses: the judge confirms the emergency, continues the children in care, and sets the review for March 19th. But because Odette's letter is already in the file, your counsel gets one sentence into the record that will matter in March: 'A kinship resource, the children's great-aunt, has been identified in writing; the agency is directed to proceed with her study.'

Directed. On the record. Studies that are directed finish on schedules; studies that are merely 'in process' finish on sympathies.

**Choices:**
- Leave with the order's sentence copied into your notebook. It is the study's leash. → **the_study**

## [the_study] The study

*Day 4 — Friday, February 20, 2026*

Odette's study opens with her clearances, Tomas's fingerprints, and a home visit that she treats like a church inspection: the blue room gets a second bed before the worker arrives, not after. Ms. Moreau walks the third floor, notes the separate bathroom, asks Tomas his schedule directly, and writes it all down in front of him — which is what honest paper looks like.

Then the pace changes. Studies move at the speed of their slowest document, and Odette's slowest document is her late husband's death certificate, needed to clear an old joint account flag on a background report. Nobody thinks it means anything. It still has to arrive.

**Choices:**
- Get the certificate yourself — county office, same week, fee paid — and hand-deliver a copy to the agency with a receipt. → **odettes_house**  _(cash −18; FLAG: paperChased)_
- Let the agency request it through channels. It is their study; the flag is their paperwork. → **odettes_house**

## [odettes_house] The third floor

*Day 6 — Sunday, February 22, 2026*

The study's logistics come to Odette's kitchen table: her clearances are filed; the home visit is set; and Tomas — home for the weekend — sits for his part without being asked twice. Ms. Moreau explains what his fingerprints are for with a directness he respects: 'The study has to describe the whole house. You're part of the house. That's the whole speech.'

'First honest form I've ever been on,' Tomas says, and rolls his thumb in the ink.

**Choices:**
- His appointment is kept, his prints taken, his name spelled right on every form — the unglamorous liturgy of a household with nothing to hide. → **micah_tooth**

## [micah_tooth] A tooth, at the right address

*Day 7 — Monday, February 23, 2026*

Sunday visits at Odette's begin — the agency's practical bridge while the study runs — and on the second Sunday Micah loses a tooth at her table, in a meatball, with ceremony. Odette produces an envelope, writes 'MICAH — FIRST TOOTH — HER HOUSE' on it in pencil, and puts it in the drawer where she keeps the family's important papers, between the deed and a baptismal certificate.

Children file their own evidence. By March, that drawer will hold the argument this case is really about. On the drive back, the one remaining errand from the study list surfaces — the death certificate for the background flag — and it is yours to chase or to leave to channels.

**Choices:**
- Get the certificate yourself — county office, same week, fee paid — and hand-deliver a copy to the agency with a receipt. → **certificate**  _(cash −18; FLAG: paperChased)_
- Let the agency request it through channels. It is their study; the flag is their paperwork. → **certificate_slow**

## [certificate_slow] Through channels

*Day 9 — Wednesday, February 25, 2026*

Channels take nineteen days. In those nineteen days, Kira has a birthday in one foster home and Micah loses a tooth in the other, and you spend both events in a family visitation room with party hats from a dollar store, doing arithmetic about what 'temporary' costs when other people hold the calendar.

When the certificate lands, the study resumes exactly where it stopped. Nothing was denied. Nothing was decided. That is the most common way sibling placements stay split: not by ruling, but by drift.

**Choices:**
- From here in, nothing travels without you carrying a copy. Ask for the sibling visits in writing while you wait. → **sibling_visits**  _(FLAG: visitsWritten)_

## [certificate] Paper, chased

*Day 9 — Wednesday, February 25, 2026*

The certificate arrives inside the week. The flag clears. And because you are at the agency anyway, you do the second thing this scenario is about: you put the sibling visits in writing. Kira and Micah have seen each other twice in three weeks, both times because a foster parent volunteered a drive. That is kindness. Kindness is not a schedule.

"I'm asking that sibling visits be written into the plan — weekly, arranged by the agency, until they're placed together." Ms. Moreau types it where requests go to become obligations.

**Choices:**
- Weekly sibling visits, in the plan, in writing — starting this Saturday. → **sibling_visits**  _(FLAG: visitsWritten)_

## [sibling_visits] Saturdays

*Day 13 — Sunday, March 1, 2026*

The visits change the children's weather. Micah's foster mother reports he sleeps better on Saturday nights; Kira keeps a countdown on a paper chain. The file now documents something agencies are supposed to weigh and often only notice when it's written down: these two are not a caseload of two. They are a set.

Odette's study, meanwhile, has one more room in it: the interview where she is asked, as every kinship applicant is asked now, about Tomas — when he stays, where he sleeps, what the children call him. There is only one way to answer it that helps her.

**Choices:**
- "Everything in my letter is everything there is. Tomas stays two weekends a month, third floor, and here's his number — ask him." → **kira_call**  _(FLAG: householdHonest)_

## [kira_call] Kira's call

*Day 15 — Tuesday, March 3, 2026*

Kira calls from her foster home on a Tuesday, on the phone the foster mother holds and then, kindly, leaves the room for. 'Micah's tooth came out at Aunt Odette's,' she reports, with the grievance of a bureau chief whose branch offices act without her. 'I keep the chain. He keeps the teeth. Tell them at the meeting I want the Saturdays at her house. Both of us. Together.'

A ten-year-old has just dictated a placement preference with more administrative clarity than most case plans contain. You write it down in her words.

**Choices:**
- Her words go to Ms. Moreau in writing the next day — the children's stated wishes, filed by the person who heard them. → **weekend_visit**  _(HIDDEN + child-voice)_

## [weekend_visit] A whole Saturday

*Day 17 — Thursday, March 5, 2026*

The first full Saturday at Odette's runs on her rules: pancakes in shifts, the blue room inspected by Kira and claimed with a hair ribbon on the doorknob, Tomas arriving at noon with hoagies and leaving the children the run of the porch. Ms. Moreau's visit note — you will read it later, in the record — is two lines long and both are gold: 'Children relaxed. Sibling interaction continuous and unforced.'

The file is learning what the family already knew. The study's last open item is Tomas's history, which the county's answer on his fingerprints will frame one way or another.

**Choices:**
- The answer comes back exactly as disclosed. Be in the room when Odette is asked about it. → **tomas_check**

## [tomas_check] The check

*Day 18 — Friday, March 6, 2026*

Tomas's record is what Odette said it would be: a single charge at nineteen, dismissed, in a county two hours away. The dismissed charge is a fact. What the study writes about it is a judgment — and the judgment it writes, when the household was disclosed from the first letter, is 'household composition known; adult member's history reviewed; no current concern.'

Had it surfaced as a discovery, the same facts would have been written as a credibility problem for the applicant. Same Tomas. Different letter.

**Choices:**
- Ask Ms. Moreau what remains before the March review — and get the answer as a list. → **tomas_job**  _(FLAG: checklistKept)_

## [tomas_job] Tomas, documented

*Day 20 — Sunday, March 8, 2026*

The study's final folder is Tomas-shaped: his employer's letter (six years on the same shift), his lease across town (proving the weekends are weekends, not residence), his fingerprint results, and the dismissed-charge disposition from the other county — obtained by you, at the clerk's window, for eleven dollars, because paper chased is paper arrived.

Assembled, it reads the way honest households read: layered, dated, and slightly boring. Boring is what truth looks like in a kinship file.

**Choices:**
- Ask Ms. Moreau what remains before the March review — and get the answer as a list. → **the_list2**

## [the_list2] What remains

*Day 22 — Tuesday, March 10, 2026*

The list is short: the study report to be written, Odette's approval signature from a supervisor, and the hearing itself. It is also the moment to make sure the review hears the person the law added to the room. Since 2023, a potential kinship care resource — someone who meets the emergency-caregiver requirements and has said yes to being a kinship caregiver — has a statutory right to be heard at a hearing on one subject: her qualifications to provide kinship care (42 Pa.C.S. § 6336.1, as amended by Act 48 of 2023; the definition sits at 42 Pa.C.S. § 6302).

It is not standing, and Ms. Fontaine, your appointed counsel — yours by right under 42 Pa.C.S. § 6337 — is careful about the difference. "She can't argue your case. But on whether she can take them, the court must hear her, and must then decide whether she gets notice and a voice going forward. Make sure she's there."

**Choices:**
- Odette will be there, in her good coat, with her folder. Ask Ms. Fontaine to note her presence for the record at the start. → **foster_moms**  _(FLAG: auntHeard)_

## [foster_moms] Two foster mothers

*Day 24 — Thursday, March 12, 2026*

Both foster mothers will be heard at the review if they wish — notice and the right to be heard are theirs under 42 Pa.C.S. § 6336.1 — and Ms. Moreau, doing the rounds, reports their positions honestly: Kira's foster mother supports the move ('She's packed twice already, in her head'). Micah's is torn in the open: bonded to a six-year-old who has been hers since the fire, and unwilling to pretend otherwise — but she has met Odette, and what she asks the court for is a transition, not a veto.

Opposition would have been simpler. This is better: a case where every adult is telling the truth, and the court gets to decide on placements instead of on credibility.

**Choices:**
- Thank both of them, through the agency, in writing. Truth-telling adults are this case's infrastructure. → **deshawn_plan**

## [deshawn_plan] Your own address

*Day 25 — Friday, March 13, 2026*

Your side of the file moves too: the red-tagged apartment is settled with the landlord, your cousin's couch has an end date, and a lease on a two-bedroom — two bedrooms, chosen with a caseworker's eye — is signed for April, contingent on the review. Your counsel will present it as context, not argument: the kinship placement is the bridge; your housing is the far shore being built on schedule.

Cases are never only about the question on the docket. Judges read trajectories. Yours, this month, points one way.

**Choices:**
- File the lease copy with your review papers. Then get the record you requested weeks ago. → **records49**

## [records49] The record, both ways

*Day 26 — Saturday, March 14, 2026*

Before the review, Ms. Fontaine suggests the request she suggests in every case: the agency's file, in writing — a parent's right under 55 Pa. Code § 3130.44(d). The placement summaries confirm the split was a bed-count accident, not a clinical judgment: both foster homes rate the children thriving; both note the sibling countdown chains.

Paper that agrees with you is still worth having. Judges trust documents that were written before anybody knew they'd be exhibits.

**Choices:**
- File the request. Bring the summaries to the review. → **review_prep49**  _(FLAG: recordsRequested; HIDDEN + record-request)_

## [review_prep49] The packet

*Day 28 — Monday, March 16, 2026*

Ms. Fontaine assembles the review packet on her conference table, and it has a spine: the first letter (whole household, day one), the hearing order directing the study, the study itself, the Saturday visit notes, Kira's dictated sentence, the foster mothers' positions, your lease. 'Cases like this are won in the passive voice,' she says. 'Everything already happened. The judge just gets to agree with the record.'

The agency's filing is due Thursday. Ms. Moreau has been straight with you for six weeks, and her report will say what her file says. The question is what her supervisor's recommendation line says underneath it.

**Choices:**
- Sleep on the packet. Tomorrow the agency files; the day after, you answer if you must. → **continuance_scare**

## [continuance_scare] The scare

*Day 29 — Tuesday, March 17, 2026*

The agency's filing requests a thirty-day continuance — 'to complete supervisory review of the kinship study' — and for one evening the packet feels like a sandcastle at tide. Ms. Fontaine opposes in writing the same day: the study is complete, the children are split, the statute's clock does not recognize supervisory weather. The court denies the continuance on the papers, in a two-line order that Ms. Fontaine reads to you twice.

March 19th stands. Systems request delay the way water finds downhill; opposed, in writing, on a complete record, delay sometimes loses.

**Choices:**
- March 19th. Iron something. Odette already has. → **the_review49**

## [the_review49] March 19th

*Day 31 — Thursday, March 19, 2026*

The judge has the study, the sibling-visit log, and a great-aunt in the second row. Ms. Moreau presents the agency's position; Ms. Fontaine presents yours; and when the question of the kinship home arrives, Odette is heard — on her qualifications, which turn out to be a life story with a spare room attached.

"Ms. Moreau," the judge says, "the agency's recommendation on placement with the great-aunt?"

**Choices:**
- Hold still. The answer was assembled in February, one letter at a time. → **night_before49**

## [night_before49] The night before

*Day 31 — Thursday, March 19, 2026*

Odette lays out the children's rooms for nobody — they are not moving tomorrow whatever happens; tomorrow is only the order — and then lays them out again, because hands need work on the night before a judge decides where a family lives. Tomas calls from his apartment: 'Tell the part about the tooth drawer.'

'They'll read the visits,' you tell him. 'The drawer is in the visits.' It is, too — two lines, gold, in the record you requested and read.

**Choices:**
- Walk in with the record already read. It changes how a courtroom sounds. → **outcome49**

## [outcome49] One roof, or two

*Day 31 — Thursday, March 19, 2026*

The recommendation depends on what the study could honestly say about the whole household — and on how much of the month the paper spent traveling instead of arriving.

**Choices:**
- The household was disclosed from the first letter, the certificate chased, the visits documented, and Odette has been heard on her qualifications: the agency recommends both children to her home. → **end_oneroof**  _(REQUIRES: householdHonest; REQUIRES: paperChased; REQUIRES: auntHeard)_
- The study supports Kira — school-age, blue room ready — but the agency wants 'more time' on the household picture before Micah, the younger child, moves too. → **end_splitfix**
- The file is too thin to recommend a joint move today. → **end_visits**

## [end_oneroof] Ending — One Roof

*Day 31 — Thursday, March 19, 2026*

**Ending.**

**Debrief:** Kira and Micah move to Walnut Street on Saturday, into the blue room and the room beside it, with Tomas's third-floor weekends written into the safety plan like the ordinary fact they always were. The judge, granting Odette notice and participation going forward, says the quiet part into the record: the kinship resource was ready before the system was, and the file shows it.

Three things carried this outcome. The kinship offer was made in writing on day one, with the whole household in it — a disclosed complication is a task, an undisclosed one is a credibility finding. The sibling bond was made into paper: weekly visits, requested in writing, logged, and impossible to un-know by March. And Odette used the voice current law gives her: under 42 Pa.C.S. § 6336.1 (Act 48 of 2023), a potential kinship care resource (§ 6302) must be heard on her qualifications to provide kinship care, and the court must then decide her notice and participation going forward. She still has no standing in your case — the statute is explicit — but her qualifications are now a courtroom fact instead of a file hope.

What no strategy controls: the hearing judge's view of a six-year-old and a dismissed charge at nineteen, and Tomas himself. If his record had held more, this ending narrows. The strategy's job was never to guarantee Odette's house wins — it was to make sure it was judged on its actual contents, all of them, from the first letter forward.

## [end_splitfix] Ending — One Roof, One Still Away (partial)

*Day 45 — Thursday, April 2, 2026*

**Ending.**

**Debrief:** Kira moves to Walnut Street. Micah does not — not yet: the court keeps him in his foster home 'pending household stabilization' and sets the question again in six weeks, with Odette approved as his respite and weekend home in the meantime. It is half a family under one roof and half a countdown chain, and Micah's half is the heavier half to carry out of the courtroom.

Be honest about what produced the split: not Tomas, and not his record — the delay. Paper that travels by channel instead of by hand cost the study the weeks in which a supervisor's caution might have been answered twice over. Every reviewer of a young child's placement is choosing between two risks, and an unfinished file makes 'wait' the defensible choice. Finished files are how parents take 'wait' off the table.

This is a partial win with a working engine: Odette is approved, heard, and in the case with notice going forward (§ 6336.1). The six-week review is a date, not a hope. Keep the Saturday visits in writing, keep the countdown chains in the file, and let the next hearing decide about a household that has been running, visibly and without incident, for a month and a half.

## [end_visits] Ending — Sundays Together (partial)

*Day 45 — Thursday, April 2, 2026*

**Ending.**

**Debrief:** The children stay where they are, in two houses, and the court's order does the one solid thing this file could support today: sibling visits every Saturday, agency-arranged, written into the plan where they cannot quietly evaporate — and Odette's study kept open with a review date, her right to be heard on her qualifications acknowledged on the record.

It is not the ending this family aimed at, and the debrief owes you the unvarnished reason: the joint placement failed on file depth. A study slowed by undisclosed household facts and slow paper presented the judge a choice between two thriving foster placements and an unfinished kinship file — and unfinished files lose that comparison even when the home behind them is the right one. The bond evidence (the visits, the countdowns) did its work: it is why the visits are ordered and the study kept open rather than closed.

Treat this ending as a waypoint, not a verdict. The study continues; the next review inherits a complete household picture, a documented sibling bond, and a kinship resource the court has already heard once. Families reach One Roof from exactly here. The road is just measured in reviews instead of weeks.
