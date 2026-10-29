# THE FIRST 90 DAYS — Scenario 102: “The Deployment Calendar”

*Human-readable script. This document and `scenario-102.json` are generated from a single source and match node-for-node: same IDs, same order, same choices, same effects.*

**The family is fictional — a composite. No real person's story appears here.**

**Content note:** This scenario depicts a deployed service member's family during a medical emergency: kinship care, paperwork mailed across an ocean, phone participation, and reviews. There is no graphic content. Players may skip any scene or use the quick exit at any time.

**How to read effects:** `cash −40` changes the player's cash. `FLAG: name` sets a flag the engine tracks. `HIDDEN + item` means the case file quietly records that item at this choice — the player does not see it when it happens. `REQUIRES FLAG: name` means the choice is only available if that flag was set earlier; `REQUIRES NO FLAG: name` means it is only available if that flag was never set. `NOTE:` is text shown to the player right after choosing.

Start date: Monday, October 6, 2025. Day offsets are days since the scenario's start date.

## [start] The Night the House Went Quiet
*Day 0 — Monday, October 6, 2025 (dayOffset 0)*

Your name is Jerome Hollis. You are deployed, thousands of miles from the house in Pennsylvania where your wife, Marlene Hollis, is raising your daughter Juniper, nine, through the school year — homework at the kitchen table you built, your photograph on the refrigerator at her eye height.

You play this case as the family team: you, acting in the windows deployment allows — scheduled calls, email, signed paper scanned and sent — and Marlene and her aunt Henrietta acting on the ground. Deployment does not pause a family's life. This week, it does not pause its paperwork either.

The call comes during a scheduled window, and it is not Marlene's voice. It is a neighbor: there was a car accident this evening. Marlene is in the hospital. Juniper is safe, asleep on the neighbor's couch, in a house with no paper that says she may stay there.

**Choices:**
- Ask the neighbor to keep Juniper tonight and get Henrietta's number to her before you lose the window → **accident_night**
  - NOTE (shown after choosing): One night, one couch, one phone number passed hand to hand across an ocean.

## [accident_night] One Night, No Paper
*Day 0 — Monday, October 6, 2025 (dayOffset 0)*

Henrietta — Marlene's aunt, retired, twenty minutes away, the adult Juniper calls when a tooth comes out — drives over in the dark and brings Juniper's school clothes and the stuffed fox whose absence would have been its own emergency. Juniper sleeps at Henrietta's that first night by family arrangement, the way families have always arranged things: by phone, by trust, by showing up.

By morning there is a second fact. A report was made at the hospital — an injured parent, a child with no local adult on paper — and the agency is opening a case. On paper, the Hollis house is empty: Marlene in a hospital bed, you on deployment, the neighbor unnamed in any document, Henrietta so far only a voice on a phone.

The gap in this case is not care. Juniper was cared for within the hour. The gap is that none of that care exists yet in the only medium the case will be conducted in.

**Choices:**
- Stay on the line for the agency's first call — Henrietta holds the phone in her kitchen → **agency_call**

## [agency_call] Ms. Thornbury's First Call
*Day 1 — Tuesday, October 7, 2025 (dayOffset 1)*

Ms. Thornbury, the caseworker, is brisk and not unkind. Marlene's injuries will keep her hospitalized and then in rehabilitation for weeks; the timeline is genuinely uncertain. Juniper cannot return to an empty house. She needs a placement the agency can document, starting now, and the agency's clock — as with any child taken into its care — runs toward an informal shelter care hearing not later than 72 hours after placement. (42 Pa.C.S. § 6332; 23 Pa.C.S. § 6315(d))

Henrietta, standing in her own kitchen, says what aunts say: 'She stays with me. She has a room here. Tell me what to sign.' Ms. Thornbury says an assessment of the kin home can begin, and that family arrangements carry more weight in the process when they are identified and documented as kinship care — the law's own definitions and notice provisions treat relatives as a distinct, named resource, not as a delay. (23 Pa.C.S. § 6302; 42 Pa.C.S. § 6336.1)

Everything now depends on how quickly 'she stays with me' becomes paper — and on whether a deployed father's participation can be made visible to a file that measures presence in visits and signatures.

**Choices:**
- Ask Ms. Thornbury to start Henrietta's kin assessment today, and ask what the family should put in writing → **kin_first_steps**
  - NOTE (shown after choosing): Today is a date a file can hold. 'Soon' is not.
- Let Henrietta and the agency work it out between them — they are both in the same town, and you are not → **kin_first_steps**
  - NOTE (shown after choosing): They are in the same town. The file, however, will record who asked for what — and a father's silence records itself.

## [kin_first_steps] What 'In Writing' Means at a Kitchen Table
*Day 1 — Tuesday, October 7, 2025 (dayOffset 1)*

Henrietta clears the kitchen table — the same gesture lawyers make with legal pads. Ms. Thornbury lists what a documented family care arrangement contains: who will care for Juniper day to day, where she will sleep and go to school, who may consent to routine medical care through the proper process, how Marlene (from her hospital bed, as she is able) and you (by phone and signed paper) remain part of decisions, and how long the arrangement is expected to last.

None of that list is a formality. It is the difference, in every later room, between a kinship placement that was arranged and a night on a couch that was remembered. Juniper, eating toast, adds the only item adults forgot: the fox stays with her, in whichever house.

The hospital, meanwhile, sends its own update: Marlene is awake, groggy, furious at the car, the hospital food, and — in that order — at being the reason a case file exists.

**Choices:**
- Draft the family care arrangement tonight, with Henrietta, by phone → **care_arrangement_choice**

## [care_arrangement_choice] The Arrangement, Signed or Spoken
*Day 2 — Wednesday, October 8, 2025 (dayOffset 2)*

The draft is one page. It names Henrietta as Juniper's kin caregiver, at Henrietta's address; keeps Juniper in her own school; names Marlene as her mother and decision-maker as she recovers; names you, with your deployment return month stated plainly; and is signed by Henrietta and, by phone-witnessed signature scanned from the hospital social worker's office, by Marlene. Your signature page travels by email, with the call log entry that witnessed it.

Signing and filing it costs copies, a notary trip for Henrietta, and your one free hour. Leaving it as a spoken understanding costs nothing tonight — everyone already agrees, and agreement feels like enough, in a kitchen, at midnight, with a child asleep upstairs.

**Choices:**
- Sign the family care arrangement and file it with the agency, in writing, naming Henrietta as kin caregiver → **arrangement_filed**  _(cash −20 ; FLAG: kinArrangementWritten ; HIDDEN + Kinship — written family care arrangement naming Henrietta filed with the agency)_
  - NOTE (shown after choosing): Filed, stamped, dated. Juniper's care is now a document, not a recollection.
- Keep the arrangement spoken for now — everyone agrees, and the signatures can follow → **arrangement_spoken**
  - NOTE (shown after choosing): Everyone does agree. The shelter care hearing, in two days, will meet only the people whose agreement made it onto paper.

## [arrangement_filed] Stamped at the Agency Window
*Day 2 — Wednesday, October 8, 2025 (dayOffset 2)*

Henrietta files the arrangement herself and keeps the stamped copy in a folder she labels, in marker, JUNIPER — PAPER. Ms. Thornbury notes the kin assessment as opened on the date the paper arrived — a small sentence with a date in it, which is the kind of sentence cases turn on.

Your signature page, arriving from deployment, is attached, with the witnessed call log. On paper, this family has a deployed father who acts, a recovering mother who signed, an aunt who stepped forward, and a child who never spent a night among strangers. That paper is now the case's first exhibit about itself.

**Choices:**
- Prepare for the shelter care hearing — you will be on the phone, and that has to count → **shelter_prep**

## [arrangement_spoken] Agreed, in a Kitchen
*Day 2 — Wednesday, October 8, 2025 (dayOffset 2)*

The arrangement is real in every way except the way the next seventy-two hours will measure. Henrietta cares for Juniper beautifully and documents nothing, because documenting care feels, to a person actually providing it, like a strange thing to do with a full sink and a frightened child.

Ms. Thornbury's file that evening records the facts as her forms receive them: child with relative; arrangement 'verbal, paperwork pending'; father 'deployed, participation to be confirmed.' None of those phrases is hostile. All of them, read cold in a courtroom, sound like a family that has not yet organized itself.

**Choices:**
- Prepare for the shelter care hearing — you will be on the phone, and that has to count → **shelter_prep**

## [shelter_prep] How a Deployed Parent Appears
*Day 2 — Wednesday, October 8, 2025 (dayOffset 2)*

Ms. Aubert, the family's attorney — retained through a payment Henrietta fronts and you repay by transfer — explains the hearing plainly. It is informal, it is fast, and it is where the court decides Juniper's placement while the case is sorted out. The family has the right to counsel, and to appointed counsel if it cannot afford one. (42 Pa.C.S. § 6337; § 6332(a))

"You will appear the way deployed parents appear," she says, "by phone, on the record, if we arrange it in advance and in writing. A father who speaks at his hearing is in the transcript. A father whose call was 'expected' is in someone's summary of the day. We will arrange it in advance, and we will put your return date and your care arrangement into the record by name."

She also flags the address problem before it happens, because she has seen it happen: the agency's mail is going to the Hollis house. The empty Hollis house.

**Choices:**
- File the advance written request for your phone participation and the corrected mailing address → **address_choice**

## [address_choice] The Address on the Envelope
*Day 3 — Thursday, October 9, 2025 (dayOffset 3)*

There are two addresses in this case now: the house, empty behind a hospital stay and a deployment, where mail will sit in a box no one checks daily; and Henrietta's, where Juniper actually lives, eats, and does homework. Agencies mail to the address in the file. Files keep the address they were opened with, unless someone corrects them — in writing, with a receipt.

Correcting it costs Henrietta one trip and you one signed page. Not correcting it costs nothing today, because mail is invisible until a deadline inside it expires. Ms. Aubert calls this, without heat, 'the cheapest disaster in family court: the letter that arrived on time, at a house with nobody in it.'

**Choices:**
- Correct the mailing address in writing to Henrietta's, with return receipt, and note both parents' contact routes → **address_corrected**  _(cash −10 ; FLAG: addressCorrected ; HIDDEN + Contact — mailing address corrected in writing to the kin home; father's call/email routes documented)_
  - NOTE (shown after choosing): One page, one receipt. Every future letter now goes where a person is.
- Mention the address to Ms. Thornbury by phone — she knows the house is empty → **address_mentioned**
  - NOTE (shown after choosing): She does know. Knowledge held by a person and knowledge held by a mailing system are different departments, and only one of them sends the letters.

## [address_corrected] Mail Where a Person Is
*Day 3 — Thursday, October 9, 2025 (dayOffset 3)*

The correction is filed and the receipt comes back signed. Ms. Thornbury updates the contact page and notes, in the file, the father's phone windows and email — the channels through which a deployed parent actually receives the world.

It is unglamorous paper and, Ms. Aubert says, possibly the most consequential page of the month: every notice, every plan draft, every 'response requested' in this case will now arrive at a house with a person in it who opens envelopes.

**Choices:**
- Go to the hearing — by phone, on the record, as arranged → **shelter_hearing**

## [address_mentioned] Mail Where Nobody Is
*Day 3 — Thursday, October 9, 2025 (dayOffset 3)*

Ms. Thornbury makes a note — a real note, in good faith. Notes, however, are not what generate envelopes. In the weeks ahead, the agency's letters will go where its system sends them: to the Hollis house, to sit in a metal box at the end of an empty driveway, behind a storm door no one opens.

You will not learn this from the letters. You will learn it later, from the record of what the letters were scored as meaning. That is a beat for a later day. Today there is a hearing.

**Choices:**
- Go to the hearing — by phone, if the arrangement holds → **shelter_hearing**

## [shelter_hearing] Shelter Care: A Voice on the Record
*Day 3 — Thursday, October 9, 2025 (dayOffset 3)*

The hearing is held within 72 hours of Juniper's placement, as the law requires. (42 Pa.C.S. § 6332; 23 Pa.C.S. § 6315(d)) Henrietta is there in person, with the folder. Marlene, by hospital phone for a few minutes, is there in the way her injuries allow. You are there by phone, arranged in advance — your name, your relationship, and your return month spoken into the record by the court itself.

The question is narrow: where does Juniper stay while Marlene recovers and the case proceeds? The agency does not oppose kinship placement with Henrietta — the assessment is underway, the home is known, the school run is short. What the court has in front of it, to ground that placement, is the arrangement: written and filed, or verbal and summarized, depending on the paper the family made in the first two days.

The court places Juniper with Henrietta as her kin caregiver, with reviews to follow under the disposition and placement-review framework. (42 Pa.C.S. § 6351) Your participation is noted — exactly as strongly as it was documented.

**Choices:**
- Ask the court to note Marlene's recovery plan and your return date in the order itself → **henrietta_assessment**  _(FLAG: returnInOrder ; HIDDEN + Shelter care order — mother's recovery plan and father's return date noted in the order)_
  - NOTE (shown after choosing): Dates in an order are case events. Dates in a conversation are weather.
- Let the placement stand on its own — kin is kin, and the details can sort themselves out → **henrietta_assessment**
  - NOTE (shown after choosing): Kin is kin. Sorting, in this system, is a paper activity, and unsorted details have a way of resurfacing as someone else's findings.

## [henrietta_assessment] The Kin Home, Assessed
*Day 4 — Friday, October 10, 2025 (dayOffset 4)*

The assessment of Henrietta's home proceeds as process, not ceremony: rooms walked, sleeping arrangements noted, school run timed, references taken, clearances filed through the proper channels. Henrietta answers it the way she answers everything, with the folder open on the table and Juniper's school calendar produced before it is asked for.

Where the written arrangement was filed on day two, the assessment reads as the confirmation of a documented plan. Where the arrangement stayed spoken, the assessment is the first paper the kinship has ever produced — and until it completes, the placement it supports rests on a summary of a conversation in a kitchen at midnight.

**Choices:**
- Begin the first full week — Juniper's routines, Marlene's calls, your windows → **after_hearing**

## [after_hearing] The First Week at Henrietta's
*Day 5 — Saturday, October 11, 2025 (dayOffset 5)*

Juniper's life reassembles at Henrietta's speed: school bus from a new stop, homework at a different kitchen table, a video call with Marlene in a hospital gown who makes faces until Juniper laughs and then, after the call, cries — both in the correct order, Henrietta says.

Your calls settle into the deployment rhythm: Tuesdays and Fridays, twenty minutes, homework questions and fox news. Ms. Thornbury visits, observes, and completes a scored assessment form from what the visit can show her — the home as observed, the supervision plan as understood by the worker, the parents' participation as it appears from the other side of the table.

Participation, as it appears. For a deployed father and a hospitalized mother, that phrase is the whole war. Henrietta starts a call-and-visit log on the refrigerator, unprompted, in pencil.

**Choices:**
- Take stock of Juniper's school week — the bus, the counselor, the homework routine at a new table → **school_continuity**

## [school_continuity] School, From a New Bus Stop
*Day 6 — Sunday, October 12, 2025 (dayOffset 6)*

Juniper's school is the fixed point both calendars agree on. Henrietta walks the new bus route with her twice before Monday. The school counselor, told — by Henrietta, in person, with the arrangement paper in hand where it exists — keeps Juniper's seat, her reading group, and her Friday library routine exactly where they were.

Continuity like this is also case paper, whether anyone calls it that: attendance uninterrupted, a counselor who can confirm the kin home's routine, a child whose school record shows a family organizing itself around her. Ms. Thornbury's form will capture some of it as observed. Henrietta's refrigerator log is where the rest of it can live.

The log question, when it comes, is not whether family life should be evidence. It is whether the family keeps its own copy.

**Choices:**
- Ask Henrietta to keep that log — and to note every one of your calls, Marlene's calls, and every agency visit → **log_kept**  _(FLAG: familyLog ; HIDDEN + Participation — family-kept log of calls, visits, and agency contacts begun)_
  - NOTE (shown after choosing): Pencil, refrigerator, dated. The humblest document in the case, and the one that will answer the most questions.
- Let the calls be calls — a log feels like it turns family life into evidence → **log_unkept**
  - NOTE (shown after choosing): It does feel that way, because it is that way. The file is turning family life into evidence either way; the log is just the family's copy.

## [log_kept] Refrigerator Paper
*Day 8 — Tuesday, October 14, 2025 (dayOffset 8)*

The log fills: your calls (Tuesdays, Fridays, one missed for a duty shift and noted as missed, which Henrietta insists on recording because 'true is true'), Marlene's calls as her strength returns, Ms. Thornbury's visit, the school counselor's name.

A log is not love and does not pretend to be. It is what love looks like after it has been translated into the only language a review hearing reads fluently.

**Choices:**
- Map your call windows against the case calendar — Tuesdays and Fridays, in writing, to the agency → **deployment_window**

## [log_unkept] Unlogged Tuesdays
*Day 8 — Tuesday, October 14, 2025 (dayOffset 8)*

The calls happen, warm and regular. The file, which was not on the calls, will later describe this period from its own instruments: visits observed, mail answered or unanswered, signatures present or absent.

Henrietta remembers everything. Memory, in a hearing, is testimony — which helps — but testimony answering a written record is always playing away from home.

**Choices:**
- Map your call windows against the case calendar — Tuesdays and Fridays, in writing, to the agency → **deployment_window**

## [deployment_window] Call Windows, in Writing
*Day 10 — Thursday, October 16, 2025 (dayOffset 10)*

Deployment gives you windows, not days: two scheduled calls a week, email answered in batches, paper signed in hours you do not choose. Ms. Aubert's advice is to make the windows themselves a document — a one-page notice to the agency of your call times, your email, and the address where your mail is actually received during deployment, filed the same way the address correction was filed.

A file that knows when a father can be reached scores silence differently from a file that never knew. The notice costs one signed page. Its absence costs nothing visible — until a hearing summary describes contact attempts made at hours no deployed parent could have answered, as if the hours had been a choice.

**Choices:**
- File the call-window notice and keep participating on that documented rhythm → **marlene_rehab**  _(FLAG: callWindowsFiled ; HIDDEN + Father's participation — deployment call windows and contact routes filed in writing)_
  - NOTE (shown after choosing): Tuesdays and Fridays, now a case fact instead of a family's private routine.
- Keep the rhythm informal — Ms. Thornbury knows your schedule from your calls → **marlene_rehab**
  - NOTE (shown after choosing): She knows it this month, on this caseload. Files outlast the people who hold their knowledge.

## [marlene_rehab] Marlene, Re-entering
*Day 12 — Saturday, October 18, 2025 (dayOffset 12)*

Marlene's recovery is not a montage. It is a walker, then a cane, then a stubborn negotiation with stairs; outpatient therapy three times a week; paperwork for her own leave; and a daughter who watches her, at visits to Henrietta's, for signs of the old strength and reports them to you by phone like a small, loyal correspondent.

The agency's plan for the family — the service plan taking shape under the review framework (42 Pa.C.S. § 6351) — needs a version of Marlene in it that matches this reality: recovering on a documented medical timeline, re-entering Juniper's daily care step by step at Henrietta's, not vanishing and then reappearing at discharge as if the middle had not happened.

Whether the plan says that depends on whether the middle gets written into it — therapy attendance, hospital discharge papers, a step-by-step care schedule Henrietta and Marlene can actually perform.

**Choices:**
- Go to the discharge-planning meeting at the hospital — Marlene, Henrietta, a social worker, and you by phone → **discharge_planning**

## [discharge_planning] Discharge Planning, on Speakerphone
*Day 14 — Monday, October 20, 2025 (dayOffset 14)*

The hospital's discharge meeting is pure process, and therefore pure gold: a printed discharge summary with dates, therapy orders three times a week, weight-bearing milestones, and a named follow-up appointment. Marlene, from the bed, adds the family's own line to it — graduated care of Juniper at Henrietta's, increasing as the milestones are met — and the social worker writes it into the discharge paperwork because Marlene asked while the paperwork was open.

Ms. Aubert, afterward, is blunt about the fork: that discharge packet can be filed straight into the agency plan, where it becomes Marlene's re-entry with medical dates attached — or it can live in a hospital chart the agency file never opens, while the plan describes her recovery in adjectives.

**Choices:**
- File the discharge packet into the written plan — therapy, dates, graduated care at Henrietta's → **reentry_written**  _(FLAG: reentryWritten ; HIDDEN + Mother's recovery — graduated re-entry steps written into the family plan with medical dates)_
  - NOTE (shown after choosing): Steps with dates. A plan that describes the mother Juniper actually has this month.
- Let the agency's draft plan stand — Marlene will simply be home soon, and the plan can catch up then → **reentry_generic**
  - NOTE (shown after choosing): 'Soon' again. Plans that will catch up later are scored, in the meantime, as plans without her in them.

## [reentry_written] Steps, With Dates
*Day 16 — Wednesday, October 22, 2025 (dayOffset 16)*

The plan now reads like the family's actual month: Marlene at therapy (attendance confirmed by the clinic's own printout), overnight time with Juniper at Henrietta's increasing as the therapist clears it, school pickup shared on cleared days. Each step has a date or a medical milestone, not an adjective.

Ms. Thornbury, to her credit, files the clinic printout without argument. A plan that matches a life is easier for everyone to score — including, quietly, the scored assessment form, whose context lines about 'caregiver capacity' now have a document to be updated from.

**Choices:**
- Face the mail problem — a letter has surfaced at the old house → **mail_surfaces**

## [reentry_generic] A Plan Waiting for 'Soon'
*Day 16 — Wednesday, October 22, 2025 (dayOffset 16)*

The agency's draft describes Marlene's status in the passive voice — 'mother recovering, return to care anticipated' — with no steps, no dates, and no mention of the graduated care happening daily at Henrietta's, because no one filed the documents that describe it.

Juniper, meanwhile, is being raised this month by a committee of love: an aunt, a recovering mother gaining strength by the week, a father on a phone twice a week. The plan sees an injured mother and an absent father. Both descriptions are made of true facts. Only one is the whole file.

**Choices:**
- Face the mail problem — a letter has surfaced at the old house → **mail_surfaces**

## [mail_surfaces] The Letter in the Empty House
*Day 20 — Sunday, October 26, 2025 (dayOffset 20)*

A neighbor, collecting a package misdelivered to the Hollis house, finds the mailbox full: agency envelopes, weeks of them — a plan draft for signature, a visit-schedule notice, a letter 'requesting a response within ten days' that was mailed a month ago. Whether this pile exists in your route depends on the address paper you filed on day three. Where it exists, its meaning has already been written somewhere: unanswered mail, in a case file, does not stay a postal fact. It becomes a participation fact.

Ms. Aubert, grim, uses the phrase 'a non-cooperation record built out of postage.' The family did not refuse anything. The family never received anything. In the file, those two sentences can look identical — until someone requests the file and reads how the conclusion was assembled.

That request, she says, is next. It was always going to be next.

**Choices:**
- Walk the mailbox's contents to Henrietta's table and sort them by the dates nobody met → **neighbor_mailbox**

## [neighbor_mailbox] Sorted by Dates Nobody Met
*Day 22 — Tuesday, October 28, 2025 (dayOffset 22)*

On Henrietta's table the pile becomes legible: each envelope a date sent, a date by which a response was wanted, an address that was technically the family's and practically a locked box at an empty house. Sorted, it stops looking like neglect and starts looking like what it is — a routing failure with a family's name on it.

Sorting it is not yet correcting it. The correction requires the one document that shows how the agency's own file assembled these envelopes into a conclusion: the file itself. Ms. Aubert is already drafting the request.

**Choices:**
- Prepare the record request — for the whole agency file, in writing → **records_beat**

## [records_beat] The Request That Reads the File
*Day 24 — Thursday, October 30, 2025 (dayOffset 24)*

Under the agency's own regulation, the agency's records are to be released on request. (55 Pa. Code § 3130.44(d)) Ms. Aubert drafts it in one paragraph: the complete agency record for Juniper's case, requested in writing, dated, filed, with a copy kept in Henrietta's folder. It is the highest-leverage move in this scenario, because everything scored about this family — participation, cooperation, response — was scored inside that file, and this is the family's one way to read the scoring while it can still be answered.

Filing it costs copies and Henrietta's trip. Not filing it leaves the family's picture of its own case at the level of phone summaries — accurate in tone, unusable in a hearing.

**Choices:**
- File the written request for the complete agency record → **records_arrive**  _(cash −15 ; FLAG: recordsRequested ; HIDDEN + Records — complete agency record requested in writing under the release-on-request rule)_
  - NOTE (shown after choosing): One paragraph, one receipt. The file is about to become readable by the people it describes.
- Ask Ms. Thornbury to summarize the file's status by phone instead → **records_summary**
  - NOTE (shown after choosing): She will, accurately, in summary. Summaries cannot be quoted, attached, corrected line by line, or handed to a judge.

## [records_arrive] What the Packet Shows
*Day 30 — Wednesday, November 5, 2025 (dayOffset 30)*

The packet arrives: redacted in places, complete in the ways that matter. And there, assembled across its pages, is the second case — the paper case, running alongside the family's real one.

The scored assessment form's context lines rate parental participation as it appeared: your calls appear where Henrietta's log or the worker's notes captured them, and thin out where they didn't. Mail to the old house is logged by date sent — and, in the narrative summary, by its silence: 'no response received' appears three times, attached to letters sent to a house with nobody in it. Marlene's recovery is 'anticipated.' Henrietta's care is thorough and well documented — the kinship paperwork, where it was filed, is the packet's strongest section.

Ms. Aubert spreads the pages on Henrietta's table. 'Now we correct it,' she says. 'In writing. Line by line. With the log, the receipts, and the return dates attached — so the correction is made of the same stuff as the record it answers.'

**Choices:**
- Read the packet the way Ms. Aubert reads it — every conclusion traced to the page that built it → **packet_reading**

## [records_summary] A Summary, Kindly Given
*Day 30 — Wednesday, November 5, 2025 (dayOffset 30)*

Ms. Thornbury's summary is fair as far as it goes: Juniper is thriving with Henrietta; Marlene is recovering; participation is 'a concern the agency is monitoring.' Monitoring what, exactly — which letters, which dates, which scored lines — the summary does not say, because summaries are not built to be answered.

Ms. Aubert writes 'no packet — concerns unspecified' on her pad. A concern you cannot read is a concern you cannot correct; it can only be carried, vaguely, into the next review, where it will be quoted from a file the family has never seen.

**Choices:**
- Prepare for the review with what paper exists outside the file — and name, honestly, what the family cannot see → **packet_reading**

## [packet_reading] Reading for Conclusions
*Day 33 — Saturday, November 8, 2025 (dayOffset 33)*

Ms. Aubert teaches the family her reading method at Henrietta's table: never argue with a conclusion until you can point at the pages that built it. 'No response' is built from mail logs. 'Participation a concern' is built from which calls were captured and which were not. 'Mother recovering' is built from whatever medical paper reached the file and whatever stayed in a hospital chart.

Each conclusion, traced, becomes a list of specific, correctable items — an address, a log, a discharge packet, a date. Untraced, it stays a fog the family would have to argue with at the review, and fog, in a hearing room, always wins on points.

**Choices:**
- Draft the written correction — mail dates, call log, return date, re-entry steps, all cited by page → **correction_choice**

## [correction_choice] Correcting the Record, in Writing
*Day 36 — Tuesday, November 11, 2025 (dayOffset 36)*

The correction Ms. Aubert drafts is deliberately unglamorous: a dated letter that identifies, by the packet's own page numbers where the family has them, (1) each letter logged as unanswered, with the mailing address it was sent to and the date the address correction was (or was not) filed; (2) your call participation, with Henrietta's log attached; (3) Marlene's documented re-entry steps; and (4) a single requested case event — your return date, five months from the accident, named as the date for a reunification step in the plan, with Henrietta's kinship care continuing as the bridge to it.

Filed, it becomes part of the record every future reader — worker, supervisor, judge — meets. Spoken at the review instead, it becomes a good five minutes that the written plan does not contain.

**Choices:**
- File the written correction with the log, receipts, and return date attached, before the review → **correction_filed**  _(cash −10 ; FLAG: correctionFiled ; HIDDEN + Correction — written correction filed before review, citing mail dates, call log, and return date)_
  - NOTE (shown after choosing): The correction joins the record it corrects. Future readers will meet the error and its answer on facing pages.
- Save the correction for the review — hearing it live will carry more weight → **correction_spoken**
  - NOTE (shown after choosing): Live carries weight in a room. Reviews, however, are decided from files after the room empties.

## [correction_filed] Filed Before the Review
*Day 41 — Sunday, November 16, 2025 (dayOffset 41)*

The stamped copy comes back to Henrietta's folder. Ms. Thornbury's next narrative — the family can see it because they now read their own file as a practice — reads differently: participation 'documented by family log and corrected contact record'; mail history 'address corrected; prior mail to vacated address noted.' The scored form's context lines do not become compliments. They become accurate, which is the only upgrade this system reliably offers.

Marlene, reading it at Henrietta's table with her cane hooked on the chair, says the sentence that is this scenario's thesis in civilian clothes: 'It's us. Finally, on paper, it's us.'

**Choices:**
- Bring Marlene home to Henrietta's — discharge day, on the plan's own documented steps → **marlene_discharge**

## [correction_spoken] Ready to Be Said Aloud
*Day 41 — Sunday, November 16, 2025 (dayOffset 41)*

The correction is rehearsed until it is tight and true. Henrietta can say every date. What it lacks is not accuracy but address: it lives in the family's mouths, not in the file the review judge will read the night before, in the plan the next worker will inherit, in the record any future 'no response' narrative would have to reckon with.

The review will hear it. Whether the review's paperwork will contain it tomorrow is a different question — the one this scenario has been asking since a mailbox began filling at an empty house.

**Choices:**
- Bring Marlene home to Henrietta's — discharge day, on the plan's own documented steps → **marlene_discharge**

## [marlene_discharge] Marlene Comes to Henrietta's
*Day 44 — Wednesday, November 19, 2025 (dayOffset 44)*

Discharge day is not a homecoming to the empty house — the plan's own steps, where they were written, say so: Marlene comes to Henrietta's, where Juniper is, where the cane and the therapy schedule and the graduated care can all happen under one roof. She sleeps in the room off the kitchen. Juniper reads to her from the reading-group book, solemnly, getting every third word gloriously wrong on purpose to make her laugh.

It is the family's best week since the accident, and — because the steps were written — it is also a plan milestone, documented by the clinic's discharge summary sitting in the file. Where the steps were never written, the same week happens identically and the file calls it, vaguely, progress.

**Choices:**
- Assemble the review packet — arrangement, log, discharge papers, correction, return date, one folder → **pre_review_packet**

## [pre_review_packet] One Folder for the Review
*Day 47 — Saturday, November 22, 2025 (dayOffset 47)*

Henrietta's folder — JUNIPER — PAPER — now holds the family's whole side of the case in the order a judge reads: the kin arrangement, the hearing order, the log, Marlene's medical steps, the record packet's key pages, the correction, and the return date. Ms. Aubert checks it page by page, the way she checks everything: if it is not in the folder, for review purposes, it did not happen.

You join by phone for the final check, in your window, and Juniper — allowed one minute — reports on the fox's morale. Then the folder closes, and the family waits for the room where folders are opened.

**Choices:**
- Go to the review — Juniper's placement, Marlene's progress, your return, one table → **review_hearing**

## [review_hearing] The Review: One Table, Two Calendars
*Day 48 — Sunday, November 23, 2025 (dayOffset 48)*

The review hearing proceeds under the placement-review framework: placement, progress, and the plan's next steps, on the record. (42 Pa.C.S. § 6351) Henrietta's kinship care is reported as what it is — stable, schooled, logged. Marlene's recovery is reported with its medical dates. You appear by phone, arranged in advance and noted, and your return date is either a case event written into the plan — with a reunification step dated to it and Henrietta named as the bridge — or a fact the family knows and the plan does not.

Ms. Thornbury's report carries the file as it now stands: corrected or uncorrected, logged or summarized, addressed or misaddressed. The court commends Henrietta, continues Juniper's kinship placement, and turns to the plan's next steps — the paragraph where this case's future will actually be written.

Ms. Aubert has told the family plainly what the honest possibilities are. None of them closes the case today. All of them are decided by which calendar the plan is finally written on: the deployment calendar, or the mail calendar.

**Choices:**
- The plan is written on both calendars — kinship throughout, your return date a dated reunification step → **end_deployment_calendar**  _(REQUIRES FLAG: kinArrangementWritten ; REQUIRES FLAG: recordsRequested ; REQUIRES FLAG: correctionFiled)_
  - NOTE (shown after choosing): Every gate here was paper filed earlier: the arrangement, the request, the correction.
- Juniper stays with Henrietta, but the plan names no return-date step — reunification floats as 'when father returns' → **end_no_step**  _(REQUIRES FLAG: kinArrangementWritten ; REQUIRES NO FLAG: correctionFiled)_
  - NOTE (shown after choosing): The care is kinship; the clock is unwritten. Both halves of that sentence will matter.
- The kin paperwork stalled unsigned, and the placement that hardened was stranger foster care → **end_stranger**  _(REQUIRES NO FLAG: kinArrangementWritten)_
  - NOTE (shown after choosing): Henrietta's care was real from the first night. The file's version of the first night is what the system placed.
- The file that governs is the mail file — 'no response,' repeated until it reads as a parent's character → **end_noncooperation**  _(REQUIRES NO FLAG: recordsRequested)_
  - NOTE (shown after choosing): No one ever refused a letter in this ending. Three letters were never received. The record needed a request to tell the difference, and the request never came.

## [end_deployment_calendar] The Deployment Calendar
*Day 60 — Friday, December 5, 2025 (dayOffset 60)*

The plan that leaves the review is written on both calendars at once. Juniper remains with Henrietta — she has never spent a night in stranger care, and the plan says so, because the kinship arrangement was paper from day two. Marlene's re-entry steps continue on their medical dates, at Henrietta's table, which has become, in the plan's own language, the family's bridge household.

And there, in the plan's next-steps paragraph, is a date from the other calendar: your return month, named, with a reunification step dated to it — transition visits at the family home, Marlene's cleared milestones, a review set to follow it. A deployment that the file once recorded as absence is now recorded as a schedule the case itself is keeping.

The case is still open. It will be open when you land, when the fox comes home in Juniper's arms, when the mailbox at the Hollis house is finally emptied by its owners. Marlene keeps the plan's stamped copy in Henrietta's folder — JUNIPER — PAPER — which by then holds the whole war: an arrangement, a log, a correction, and a date circled in two time zones.

**Ending.**

**Debrief:**
- THE LAW, BEAT BY BEAT — Shelter care was timely, inside 72 hours of placement (42 Pa.C.S. § 6332; 23 Pa.C.S. § 6315(d)), with counsel's role stated on the record (42 Pa.C.S. § 6337; § 6332(a)). Kinship: Henrietta was identified and documented as a kin caregiver from the first days, using the kinship definitions and notice framework the verified set carries (23 Pa.C.S. § 6302; 42 Pa.C.S. § 6336.1) — as written arrangement and assessment, not as a verbal understanding. Reviews proceeded on the record under 42 Pa.C.S. § 6351, and the record was the family's own work product as much as the agency's: the complete agency record was requested in writing under 55 Pa. Code § 3130.44(d), which is what exposed the mail-to-the-empty-house entries while they could still be corrected in writing. A NOTE ON SCOPE: military-specific legal protections for deployed parents exist in the wider law, but they are outside this scenario's verified set, were not cited in play, and this route does not rely on them — every winning move here is a generic, documented family-court move available to any parent.
- THE HIDDEN FORM, MAPPED — The scored assessment form rated participation as it appeared from the file: kin arrangement filed in writing (flag: kinArrangementWritten), mailing address corrected to where a person lives (flag: addressCorrected), family log of calls and visits kept (flag: familyLog), mother's re-entry written with medical dates (flag: reentryWritten), father's return date noted in the shelter care order (flag: returnInOrder), records requested (flag: recordsRequested), and the correction filed before review (flag: correctionFiled). Where those items were paper, 'participation' scored as documented; the form has no item for how much a deployed father loves his daughter, and this scenario does not pretend otherwise.
- HONEST LIMITS — This is a PARTIAL win, labeled so: Juniper was protected from stranger care and the plan is honest, but the case remains open at Jerome's return, Marlene's recovery continues on a medical timeline no filing can hurry, and reunification steps dated in a plan still have to be lived and reviewed. Real outcomes also turn on workers, judges, hospital timelines, and the luck of assignments and mail routes. This ending is not a verdict on the Hollis family. It is a map of two calendars that were finally made to describe the same family.

## [end_no_step] Kinship, Without a Date
*Day 60 — Friday, December 5, 2025 (dayOffset 60)*

Juniper stays with Henrietta — that part of the family's work held completely. She is in her school, in her aunt's house, with her fox, her homework routine, and a mother whose strength returns on schedule downstairs. No stranger care, no disruption, no lost school. By the measures a nine-year-old would choose, this is the good ending.

The plan, however, was written without the correction in it, and so it describes reunification the way weather describes rain: 'upon father's return, agency to assess.' No date. No step. No review keyed to the one event the whole family is organized around. When you return, the case will begin — then — to design a process that could have been designed now, while Henrietta's bridge was standing and Marlene's steps were documented and warm.

Henrietta keeps the folder anyway. 'Paper,' she says, 'for the next round.' She has learned the family's new language perfectly. She just learned it one review too late for this paragraph.

**Ending.**

**Debrief:**
- THE LAW, BEAT BY BEAT — Kinship placement with Henrietta held throughout, grounded in the written arrangement and the kinship framework (23 Pa.C.S. § 6302; 42 Pa.C.S. § 6336.1), with timely shelter care (42 Pa.C.S. § 6332; 23 Pa.C.S. § 6315(d)) and counsel (42 Pa.C.S. § 6337). The loss in this ending is inside the review process itself (42 Pa.C.S. § 6351): a review can only order steps that are proposed in documented form, and without the filed correction — mail history, call log, return date, all cited — the plan's next steps defaulted to the agency's passive phrasing.
- THE HIDDEN FORM, MAPPED — The kinship item scored fully (flag: kinArrangementWritten); the participation and planning items scored partially — present as testimony and summaries, absent as exhibits. The difference between this ending and the best ending is exactly one filed document (flag: correctionFiled, built on recordsRequested): the correction is what converts a father's known return date into a case event with a step attached.
- HONEST LIMITS — Reunification delayed by an unwritten step is not reunification denied; the step can be proposed at the next review, and Henrietta's stable kinship care keeps Juniper's life continuous in the meantime — no small thing, and the child's own timeline (her school year, her mother's healing) has been protected throughout. Real outcomes also turn on workers, judges, and luck. What was lost here is time and leverage, measured in a paragraph: a plan that waits for a return instead of meeting it.

## [end_stranger] The Unsigned Week
*Day 60 — Friday, December 5, 2025 (dayOffset 60)*

The kinship care was real from the first night. What the system placed, however, was the file's version of the first night: arrangement verbal, paperwork pending, assessment unopened — and when Marlene's hospital course complicated and a supervisor needed a documented placement on a deadline, the documented placement available was a licensed foster home across the district.

Juniper adapts the way nine-year-olds adapt, which is to say completely and at a cost no form itemizes: a new bus, a new table, the fox allowed, Henrietta's visits on a schedule, Marlene's recovery watched through a visit-room door. Henrietta files her paperwork then — all of it, stamped and perfect — and joins the queue of kin the case should have met in week one, now as an applicant to undo a placement rather than the author of one.

No one in this ending refused Henrietta. No one found her wanting. The assessment, when it finally completed, approved her. It simply completed into a case that had already hardened around a different address.

**Ending.**

**Debrief:**
- THE LAW, BEAT BY BEAT — Shelter care was timely (42 Pa.C.S. § 6332; 23 Pa.C.S. § 6315(d)) and counsel was available (42 Pa.C.S. § 6337); the kinship framework existed to be used (23 Pa.C.S. § 6302; 42 Pa.C.S. § 6336.1). It was not used in time, in writing — and kinship in this system is a documented status before it is a recognized one. Reviews under 42 Pa.C.S. § 6351 thereafter reviewed a stranger placement as the status quo, and status quo is the strongest argument in any review room.
- THE HIDDEN FORM, MAPPED — This ending is reached when the written arrangement was never filed (no kinArrangementWritten flag): the scored form's kinship and caregiver items were completed from a verbal understanding summarized as 'pending,' and 'pending,' under deadline pressure, loses to any placement that is already documented. Henrietta's actual care — nightly, competent, loving — appears in the form only as observed at visits after the fact.
- HONEST LIMITS — Stranger foster care, in this ending, is a placement outcome, not a finding about any member of this family, and kinship approval of Henrietta remains live inside the case; transfer to kin after placement happens in real cases and may happen in this family's next chapter. Real outcomes also turn on workers, judges, hospital complications, and luck — here, on a supervisor's deadline meeting a family's unsigned week. The scenario's narrow claim is about sequence: in a paperwork system, the order in which documents arrive is itself a fact with consequences.

## [end_noncooperation] No Response
*Day 60 — Friday, December 5, 2025 (dayOffset 60)*

The phrase follows the family into the review like a second surname: no response. No response to the plan draft (mailed to the empty house). No response to the schedule notice (same box). No response to the letter requesting a response (same box, ten days, expired in the dark behind the storm door).

At the review, Ms. Aubert says the true sentence — 'My clients never received these letters; the house was empty; the father is deployed and the mother was hospitalized' — and it is believed, in the room, by the humans. But the plan that leaves the room is written from the file, and the file's narrative, never requested, never corrected line by line, describes a pattern. Patterns, in a case file, harden into character. The next worker will inherit 'parents with a history of non-response' before she inherits anything else.

Juniper remains with Henrietta, safe and loved, while the adults discover that the most expensive letters in a deployment are the ones nobody sent wrong — only sent home, to nobody, on time. Rebuilding the record is possible. It starts, next season, with the request that would have started it this season: the family's own file, in writing, read closely.

**Ending.**

**Debrief:**
- THE LAW, BEAT BY BEAT — No rule was broken to produce this ending: shelter care was timely (42 Pa.C.S. § 6332; 23 Pa.C.S. § 6315(d)), counsel existed (42 Pa.C.S. § 6337), kinship was recognized (23 Pa.C.S. § 6302; 42 Pa.C.S. § 6336.1), and reviews were held (42 Pa.C.S. § 6351). The failure is informational, and the verified set contains its remedy, unused here: the agency record, released on request (55 Pa. Code § 3130.44(d)) — the one move that shows a family how 'no response' was assembled, address by address and date by date, while correction could still precede the review that quotes it.
- THE HIDDEN FORM, MAPPED — This ending is reached when the record was never requested (no recordsRequested flag): the scored form's cooperation and participation items were completed from mail logs and unanswered deadlines, which are real data about envelopes and no data at all about parents. A deployed father's calls and a hospitalized mother's recovery existed in the family's log and in testimony; the form's items, unanswered by any filed correction, scored the silence of a mailbox instead.
- HONEST LIMITS — 'No response' narratives can be corrected after the fact — records can still be requested, corrections still filed, and this family's actual care of Juniper (kinship, stable, schooled) is documented elsewhere in the same file and argues for them at every future review. Real outcomes also turn on workers, judges, and luck, including the pure postal luck of which house a system believes a family lives in. This ending is the scenario's warning in its purest form: a record nobody reads becomes a story nobody chose, told about people who were, the whole time, answering a different phone.
