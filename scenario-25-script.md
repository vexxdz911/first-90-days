# THE FIRST 90 DAYS — Scenario 25: “The Expert Split”

*Human-readable script. This document and `scenario-25.json` are generated from a single source and match node-for-node: same IDs, same order, same choices, same effects.*

**The family is fictional — a composite. No real person's story appears here.**

**Content note:** This scenario depicts a dependency case involving an infant's fracture and competing medical opinions — told through records, timelines, and hearings. The medicine is kept plain and general; there is no graphic content. Players may skip any scene or use the quick exit at any time.

**How to read effects:** `cash −40` changes the player's cash. `FLAG: name` sets a flag the engine tracks. `HIDDEN + item` means the case file quietly records that item at this choice — the player does not see it when it happens. `REQUIRES FLAG: name` means the choice is only available if that flag was set earlier; `REQUIRES NO FLAG: name` means it is only available if that flag was never set. `NOTE:` is text shown to the player right after choosing.

Start date: Monday, February 9, 2026. Day offsets are days since the scenario's start date.

## [start] The Quiet Arm
*Day 0 — Monday, February 9, 2026 (dayOffset 0)*

Your name is June Park. Your daughter Wren is seven months old — a champion napper, a critic of peas — and this morning at her checkup, the pediatrician went quiet in a way that reorganized your whole life.

Wren had been fussy for two days and wasn't using her left arm the way she had the week before. You thought it was a strain, or a virus, or nothing — the long list of nothings new parents learn. The imaging told a plainer story: a fracture in the arm, not brand new, already beginning to heal.

The doctor was kind and careful and used no accusing words. She also said two sentences that start the machinery: a fracture like this, in a baby who cannot yet cruise or climb, needs an explanation — and the hospital team would be looking at Wren's whole picture, and a report would be made. By tonight there will be questions, and the questions will have a form. This story is about paper: whose paper, how complete, and whether it was assembled in time.

**Choices:**
- Go to the hospital for the full evaluation, and answer everything they ask → **hospital**
  - NOTE (shown after choosing): You pack the diaper bag like evidence: bottles, blanket, the little hat. You do not know yet that you are also packing a timeline.

## [hospital] Two Versions of the Weekend
*Day 0, evening — Monday, February 9, 2026 (dayOffset 0)*

At the hospital, a doctor on the child-protection team examines Wren and asks you and Wren's father, Theo, separately, when the fussiness started.

You say Saturday morning — she cried at a diaper change and you remember because the laundry was running. Theo, exhausted and frightened, says Friday night. In the chart, two honest, tired, slightly different answers become a phrase that will follow this case everywhere: inconsistent accounts. Published cases turn on that phrase. So does this one.

A skeletal survey — a full set of images — is done to check for any other healing injury. A second hospital doctor will later read the same images and reach a different view of them. Nobody in the building tonight is a villain. Everyone in it is writing something down.

**Choices:**
- Ask for copies of everything — imaging, notes, all of it — before you leave → **night_questions**  _(cash −15 ; FLAG: recordsRequested ; HIDDEN + Records — parent requested complete hospital imaging and notes on day 0)_
  - NOTE (shown after choosing): The clerk says imaging goes on a disc, notes take a request form. You sign the form. First lesson: asking is a procedure, and procedures have forms.
- Go home and try to sleep — the hospital has everything, if anyone needs it → **night_questions**
  - NOTE (shown after choosing): The hospital does have everything. Having and holding are different verbs, and the distance between them is measured in request forms.

## [night_questions] Questions at the Kitchen Table
*Day 1, morning — Tuesday, February 10, 2026 (dayOffset 1)*

The caseworker comes to your home in the morning, with a colleague, a clipboard, and questions that are the same questions from the hospital, asked in your kitchen, where the high chair still has peas on it. When did the fussiness start? Who was with her? What did you notice, and when, exactly?

You answer everything, again, and notice your own answers shifting by hours as exhaustion does its editing — Friday, Saturday, the laundry, the nap. Theo answers from the doorway, differently. No one is lying. Everyone is tired, frightened, and being transcribed. On the clipboard, in real time, a timeline made of tired sentences is hardening into the version with a letterhead.

Ms. Ferreira will later show you this page and say the sentence that organizes this whole scenario: accounts given at midnight are weather; documents built from timestamps are climate.

**Choices:**
- Answer fully, and start writing down your own dated version as soon as they leave → **removal**  _(FLAG: ownNotes ; HIDDEN + Notes — parent began dated contemporaneous notes on day 1)_
  - NOTE (shown after choosing): Your notebook's first entries are shaky and specific: times, texts, who called whom. Specific is what survives.
- Answer fully — the professionals are keeping the record; that's their job → **removal**
  - NOTE (shown after choosing): They are keeping a record. Whose questions it answers, and whose it doesn't, is the subject of the next fifty-five days.

## [removal] The Emergency Order
*Day 1 — Tuesday, February 10, 2026 (dayOffset 1)*

The agency's position, stated plainly in a small room, is that until the fracture is explained, Wren cannot be safe at home — because no one can yet say what would need to change. Your position, stated just as plainly, is that you brought her in yourselves, the morning you noticed, and that has to count for something. Both positions are now in the file. Only one of them comes with an order.

The court signs an emergency order. Wren is placed tonight with a licensed foster family across town, with a visit set for the weekend. You hand over the diaper bag — bottles, blanket, the little hat — to a woman who receives it gently, the way people receive things that are obviously more than things.

A hearing must follow fast, because the law makes it follow fast. Your lawyer will explain the clock at the shelter care hearing. Right now there is only the drive home, in a car with an empty seat in the back.

**Choices:**
- Wren is placed tonight under the emergency order — drive home and start the notebook you will keep for this whole case → **shelter**  _(FLAG: removed ; HIDDEN + Placement — Wren removed under emergency order on day 1)_
  - NOTE (shown after choosing): On the notebook's first page you write the date, twice, the way people write things they cannot afford to get wrong.

## [shelter] Shelter Care: Seventy-Two Hours
*Day 4 — Friday, February 13, 2026 (dayOffset 4)*

The shelter care hearing is held Friday, February 13, 2026 — within 72 hours of Wren's placement, as the law requires: an informal hearing not later than 72 hours after a child is placed in shelter care. (42 Pa.C.S. § 6332; 23 Pa.C.S. § 6315(d)) The deadline date was Friday, February 13, 2026, and the court met it with a day to spare, which everyone in the room treats as normal and no one treats as guaranteed.

Before anything else, the court confirms you have counsel — you have the right to counsel, and to appointed counsel if you cannot afford one. (42 Pa.C.S. § 6337) Your lawyer, Ms. Ferreira, stands close enough that her sleeve touches your arm when the order continuing Wren's placement, for now, is read aloud.

"For now," Ms. Ferreira says in the hallway, "is the load-bearing phrase. What decides the big hearing is not tonight's fear. It's a record — medical records, complete ones, and a timeline we can prove. We start building both this week. Charm will not be an exhibit. Paper will."

**Choices:**
- Ask her what 'complete' means, medically — complete how? → **first_visit**
  - NOTE (shown after choosing): "Every image, not the summary. Every growth visit, not the highlights. A second opinion is only as good as the file it reads."

## [first_visit] The First Visit
*Day 5 — Saturday, February 14, 2026 (dayOffset 5)*

The visit is in a room with soft furniture, a camera you are told not to mind, and a worker who writes while Wren — who does not care about any of the paper — sleeps on your chest with her whole weight, which is the only fully honest document in the building.

Theo cries quietly at the door when the hour ends, because leaving is a thing you do with your hands and his hands refuse the first time. The worker writes something. You will spend weeks not knowing what, in a file you have the right to request — agency records are released on request. (55 Pa. Code § 3130.44(d)) Knowing that, and using it, are the two halves of this scenario's main skill.

**Choices:**
- On the drive home, write the visit into the notebook — date, times, who was there, what was said → **two_doctors**  _(FLAG: visitNotes ; HIDDEN + Visits — parent keeping dated visit notes from the first visit)_
  - NOTE (shown after choosing): If it is ever your word against a log, a notebook written the same day is the closest thing to a second witness you can manufacture honestly.
- Drive home in silence — some hours should not become paperwork → **two_doctors**
  - NOTE (shown after choosing): Both impulses are human. Only one of them will be readable at a hearing, and hearings are where this story is going.

## [two_doctors] Two Doctors, One Set of Images
*Day 7 — Monday, February 16, 2026 (dayOffset 7)*

The first medical opinions arrive, and they do not agree — which is less unusual, Ms. Ferreira says, than anyone outside a courtroom believes.

The hospital's child-protection doctor reads the fracture, in a baby this young, as an injury that takes more force than ordinary handling — in her words, consistent with inflicted injury, with no ordinary explanation yet offered that fits. A consulting doctor who reviewed the images for the defense reads the same bones differently: the pattern, he says, can occur accidentally or with fragile bones, and he wants Wren's bone-health labs and her full growth history before anyone says the word 'diagnosis' as if it were the word 'accusation.'

Ms. Ferreira underlines that last part twice. "A diagnosis describes an injury. An accusation names a person. The hearing will be about whether the record — all of it — lets the court travel from one to the other, clearly and convincingly. Our job is to make sure 'all of it' is actually in the room."

**Choices:**
- Start the records chase — the complete imaging set and the growth records → **peds_explainer**
  - NOTE (shown after choosing): She hands you a checklist with eleven boxes. By the end of this story you will know what each box cost.

## [peds_explainer] Your Own Doctor, Carefully Neutral
*Day 8 — Tuesday, February 17, 2026 (dayOffset 8)*

Wren's pediatrician — the doctor who sent you to the hospital — sees you alone, at your request, and does the bravest thing a professional in her position does in these weeks: she explains, precisely, what she knows and what she does not.

"I found a fracture I could not explain, and I am required to act on that, and I did. That is a finding about an injury. I have never seen either of you harm her, and my records will say she was brought in, on schedule, every time — because she was. Both of those are my job." Her records, she confirms, are yours to request like everyone else's — and hers may be the only file in the case that was written before anyone thought the word 'case.'

You leave with a strange calm. A diagnosis is a statement about a bone. An accusation is a statement about a person. Somewhere between her office and a courtroom, this case will either build the bridge between them out of records — or be carried across it by assumption.

**Choices:**
- Request her complete records today, in writing, while the conversation is fresh → **records_chase**  _(cash −10 ; FLAG: recordsRequested ; FLAG: pedsRecords ; HIDDEN + Records — complete pediatric records requested in writing on day 8)_
  - NOTE (shown after choosing): The front desk stamps your copy. Pre-case paper, requested early, before anyone's memory of it could be edited by events.
- Thank her and fold her words into your memory of who believes you → **records_chase**
  - NOTE (shown after choosing): Belief is warmth. Records are weight. The hearing, when it comes, will be a weighing.

## [records_chase] The Records Chase Begins
*Day 10 — Thursday, February 19, 2026 (dayOffset 10)*

Agency records are one request: the agency's records are to be released on request, and you make that request in writing. (55 Pa. Code § 3130.44(d)) Medical records are five requests wearing a trench coat: the hospital, the pediatrician, the urgent-care clinic from the ear infection in December, the imaging center, and the lab.

Each has its own release form, its own portal, its own cheerful estimate of business days. Ms. Ferreira's checklist sorts them by what the third opinion — a specialist your team wants to consult — will need: the complete imaging set first, growth records second, labs third.

You can work the checklist in that order, or start with whichever office answers the phone first. Order, in a records chase, is not a detail. It is the whole game, played at the speed of fax machines.

**Choices:**
- Work the checklist in order — imaging set first, signed releases everywhere → **portal_maze**  _(cash −15 ; FLAG: recordsRequested ; FLAG: imagingFirst ; HIDDEN + Records — complete imaging set requested first, releases signed at all providers)_
  - NOTE (shown after choosing): Three counters, two portals, one fax number that rings a supply closet. The imaging request is stamped and dated.
- Start wherever someone answers — the pediatrician's office picks up first → **portal_maze**
  - NOTE (shown after choosing): A friendly voice, a quick form. It feels like progress. The checklist's first box stays empty, politely, for now.

## [portal_maze] Portals, Fax Numbers, Business Days
*Day 12 — Saturday, February 21, 2026 (dayOffset 12)*

The chase, in practice: a portal that locks you out for using the password it just made you set. A fax number that rings a supply closet. A lab that will release results to the ordering doctor, the ordering doctor's office that will release them to you, and a form that must travel between the two like a treaty. Every office is staffed by someone reasonable. The system between the offices is staffed by no one at all.

Ms. Ferreira's advice is unglamorous enough to be carved over a door: log every request — date, office, name, what was promised. A log of asking is itself a record, and if a page is missing at the hearing, the log is how 'we asked, in writing, on this date' becomes a fact instead of a claim.

**Choices:**
- Keep the chase log from today — every request, date, name, and promise → **peds_partial**  _(FLAG: chaseLog ; HIDDEN + Records — dated chase log kept for every records request)_
  - NOTE (shown after choosing): Four columns in the notebook. By the hearing, this log will be the spine of an argument about diligence that no one can cross-examine away.
- Trust the offices to send what they said they would → **peds_partial**
  - NOTE (shown after choosing): Mostly, they will. Mostly, in a case that turns on completeness, is a load-bearing adverb.

## [peds_partial] What Arrived, and What Didn't
*Day 14 — Monday, February 23, 2026 (dayOffset 14)*

The first envelope is encouraging and incomplete in instructive ways. The pediatrician sends Wren's growth charts and visit notes — a reassuring paper trail of a baby brought in, weighed, measured, and worried over on schedule, by parents whose own doctor never once filed a concern. That will matter later, in exactly the dry way Ms. Ferreira predicted: as a document, not a speech.

What did not arrive: the imaging disc itself. The hospital sent its written report — one doctor's reading, in summary — but the complete set of images, including the follow-up views, is 'in process.' A report is one person's conclusion. The images are the thing conclusions are made from. A third expert cannot re-read a summary.

On the checklist, the growth-records box gets its check. The imaging box gets a star, a date, and a note in your handwriting: CHASE THIS.

**Choices:**
- Build the care timeline now, while the weekend is still arguable from texts and calendars → **timeline_beat**
  - NOTE (shown after choosing): Ms. Ferreira: "Accounts drift. Timestamps don't. We are going to build the weekend out of things that were written at the time."
- Spend the week on the imaging disc instead — the timeline can wait → **timeline_beat**
  - NOTE (shown after choosing): The disc office promises 'soon.' The weekend, meanwhile, exists only in two tired memories — the raw material of the phrase already in the chart.

## [timeline_beat] Building the Weekend
*Day 18 — Friday, February 27, 2026 (dayOffset 18)*

Ms. Ferreira clears her desk and builds the weekend the way you'd build anything load-bearing: from the bottom, out of dated pieces. Your texts to your sister ("she's fussy, won't settle — laundry day, ugh"). Theo's work schedule. The grocery receipt. The laundry you remembered, which turns out to be a load you texted about on Saturday at 9:14 a.m. — not Friday night, as Theo said at the hospital, and not Sunday, as you said once, later, misremembering under fluorescent lights.

Done carefully, with the timestamps attached, the timeline says something modest and powerful: Wren was in your care, then at her grandparents' for two hours Saturday afternoon, then home; the fussiness is first documented Saturday morning; and the 'inconsistency' in the chart is two frightened people, interviewed separately at midnight, disagreeing by one evening about a baby who cannot talk.

Done never, the chart just says: inconsistent accounts. Three words, no timestamps, carrying a whole case on their back.

**Choices:**
- Build it day by day, hour by hour, with every timestamp printed and attached → **indicated_letter**  _(cash −10 ; FLAG: timelineBuilt ; HIDDEN + Timeline — day-by-day care timeline built from contemporaneous texts, schedules, and receipts)_
  - NOTE (shown after choosing): Four pages, eleven exhibits, zero adjectives. Ms. Ferreira reads it and says the highest praise in her vocabulary: "This is a document."
- Write a one-page summary from memory instead — the gist is the same → **indicated_letter**
  - NOTE (shown after choosing): The gist is the same. Gists are what cross-examination eats. The chart's three words remain the only version with a letterhead.

## [indicated_letter] The Second Letter
*Day 20 — Sunday, March 1, 2026 (dayOffset 20)*

A second track opens with a second envelope: the report about Wren's fracture has been marked 'indicated,' and your name — yours, specifically — has been entered as a perpetrator in the statewide registry. Different track, different rules, different clock from the dependency case: a person named in an indicated report may ask, in writing, for the report to be amended or expunged, and that request must be made within 90 days of being notified. (23 Pa.C.S. § 6341(a)(2))

Ninety days from today's letter, Sunday, March 1, 2026, runs to Saturday, May 30, 2026. Ms. Ferreira circles it in the same ink as everything else that matters. "Two cases now," she says. "Same facts. Different burdens, different deciders, possibly different endings. It happens more often than anyone expects. We run both tracks, on paper, on time."

An indicated entry can also reach your work, your clearances, your future — quietly, on a form, years from now. The dependency hearing will not decide this letter. This letter will not decide the hearing. Confusing the two tracks is the most expensive mistake available to you.

**Choices:**
- Calendar the deadline in ink, and put the expunction track on its own checklist → **work_clearance**  _(FLAG: indicatedTracked ; HIDDEN + Indicated report — 90-day deadline calendared: May 30, 2026)_
  - NOTE (shown after choosing): May 30, 2026. Circled, starred, and written on the refrigerator under Wren's photo.
- Set the letter aside — the dependency hearing is the real fight → **work_clearance**
  - NOTE (shown after choosing): It is a real fight. The letter is a second one, with a clock that does not care which fight you are watching.

## [work_clearance] The Letter Reaches Your Job
*Day 22 — Tuesday, March 3, 2026 (dayOffset 22)*

You work part-time at a daycare — a fact that was in the file from the first page, and that the second letter now touches directly. Your director, Ms. Ansel, calls you in with the careful face of a person holding two duties at once: she must follow the clearance rules that govern her center, and she has watched you settle forty toddlers for naps without once raising your voice.

"While the entry stands, I can't schedule you," she says. "That is not a judgment. It is a form." She gives you the HR paperwork anyway, and a letter — at your request, in writing — confirming your employment, your record, and that the suspension is administrative, pending the outcome of a process she names correctly and dates precisely.

This is what an indicated report does while you are fighting about a fracture: it works, quietly, in other buildings, on other forms. It is why the second track has its own clock, and why the clock is not a footnote.

**Choices:**
- Get the director's letter and the HR dates in writing, for both files → **imaging_disc**  _(FLAG: workLetter ; HIDDEN + Employment — director's letter and administrative-suspension dates documented)_
  - NOTE (shown after choosing): Two tracks, two binders' worth of tabs now. The letter that can end the suspension, if it ever comes, will be a decision in the expunction case — the track with the deadline.
- Take the news verbally — she is being kind, and paperwork feels like distrust → **imaging_disc**
  - NOTE (shown after choosing): Kindness and paper are not enemies. Only one of them, though, can be shown to a hearing officer in May.

## [imaging_disc] The Disc
*Day 25 — Friday, March 6, 2026 (dayOffset 25)*

The imaging center's window has a bell, a plant, and a clerk who has clearly been yelled at by people who were promised a disc by a voice on a phone. Your complete set — the original survey, the follow-up views, every angle a specialist would need — exists. It has existed since day 0. It is sitting in a queue behind a form that needs one more signature: yours, on the right release, the one from the checklist's first box.

This is the hinge of the medical track, and it is not dramatic at all: a signature, a stamp, a disc in a paper sleeve. Without the complete images, any third opinion is a book review of someone else's reading. With them, a specialist can actually look.

**Choices:**
- Sign the correct release, pay the copy fee, and leave with the complete imaging set in hand → **growth_chase**  _(cash −20 ; FLAG: completeImaging ; HIDDEN + Records — complete imaging set obtained, including follow-up views)_
  - NOTE (shown after choosing): The disc rides home in your notebook like a heart in a cooler. Checklist box one: checked, dated, initialed.
- Take the hospital's written report as good enough — the specialist can work from the summary → **growth_chase**
  - NOTE (shown after choosing): Ms. Ferreira does not argue. She writes 'summary only' on the checklist, in the pencil she reserves for places you may fall through.

## [growth_chase] Growth Records and Grandparents
*Day 30 — Wednesday, March 11, 2026 (dayOffset 30)*

The rest of the file assembles at the speed of offices. The pediatric growth records are complete — a chart of a baby growing along her curve, visit after visit, which both sides will read their own way: the agency, as background; your team, as the paper shape of ordinary, attentive care.

Your parents, who had Wren for two hours that Saturday, write their account — and Ms. Ferreira makes them do it the timeline way: not a letter about what good grandparents they are, but a plain, dated statement of times, arrivals, departures, and what Wren did (slept, mostly, in a way they describe with unjustifiable pride).

Paper is accumulating. Whether it accumulates into a packet — complete, organized, in a specialist's hands with time to read it — is the remaining question of this track.

**Choices:**
- Assemble the full packet now: images, growth records, labs, timeline, grandparents' statement → **gp_statement**  _(cash −10 ; FLAG: packetAssembled ; HIDDEN + Packet — complete expert packet assembled: imaging, growth records, labs, timeline, statements)_
  - NOTE (shown after choosing): One binder, tabbed. It looks like nothing. It is the whole strategy, in a binder.
- Send what you have so far and supplement later — momentum matters → **gp_statement**
  - NOTE (shown after choosing): Supplements have a way of arriving after opinions do. The binder goes out with gaps where its strongest pages belong.

## [gp_statement] The Grandparents' Two Hours
*Day 32 — Friday, March 13, 2026 (dayOffset 32)*

Your parents' statement, as first drafted by your mother at her kitchen table, was four pages about what kind of family you are. Ms. Ferreira returns it with love and a red pen: "Everything in here is true, and almost none of it is usable. A court weighs times and acts. Rewrite it as the afternoon itself: when you arrived, when Wren woke, what she did, when you left."

The rewrite takes an evening and produces one page: 2:05 arrival. Wren asleep in the car seat until 2:40. A bottle at 3:00. Asleep again. Departure at 4:10, awake, ordinary, unremarkable — which, written down with dates and signed, stops being a family's reassurance and becomes a fact other facts can lean on. It closes the last gap in the timeline: the only two hours of that weekend Wren spent out of your care, accounted for by the people who held them.

**Choices:**
- File the rewritten statement with the packet — one page, dated, signed → **third_opinion**  _(FLAG: gpStatement ; HIDDEN + Timeline — grandparents' dated statement covers the Saturday-afternoon gap)_
  - NOTE (shown after choosing): One page. It will be cited more than the four-page version would ever have been, because it can be.
- Keep the original letter — the court should know what kind of family this is → **third_opinion**
  - NOTE (shown after choosing): The court will learn what kind of family this is the way courts learn everything: from what is filed, in the form filings take.

## [third_opinion] The Third Opinion
*Day 35 — Monday, March 16, 2026 (dayOffset 35)*

Your team sends the packet to a specialist in children's bone health — a doctor who has never met any of you, who does not know your names beyond the cover sheet, and who will read bones, labs, and growth curves and say what they support. This is deliberate. The point of a third opinion is not loyalty. It is a clean read of a complete file.

Her office replies with the two variables that decide this track: what she was sent, and how much time she has. A complete packet, sent now, gets a careful answer before the hearing. A partial packet gets a careful answer about a partial file — or a letter saying she cannot responsibly opine on summaries, which is its own kind of answer, and not the kind that helps.

Ms. Ferreira: "Notice what we are not doing. We are not shopping for a friendly conclusion. We are delivering a complete record to a qualified stranger and living with what she says. That is what makes it worth something if she sides with you — and survivable if she doesn't."

**Choices:**
- Send the complete packet and confirm, in writing, that she has everything and a hearing date to work toward → **specialist_call**  _(FLAG: thirdOpinionSent ; HIDDEN + Third opinion — complete packet confirmed received by specialist)_
  - NOTE (shown after choosing): Her assistant confirms receipt, item by item, against your checklist. Eleven boxes. Eleven checks.
- Let the packet stand as sent and turn to the expunction track — one fight at a time → **specialist_call**
  - NOTE (shown after choosing): Whatever was in the envelope is what she will read. Envelopes, like transcripts, do not know what you meant to include.

## [specialist_call] The Specialist's Office Calls Back
*Day 38 — Thursday, March 19, 2026 (dayOffset 38)*

Specialists' offices run on a single fuel: completeness. The call, when it comes, is a checklist read aloud — images, received; follow-ups, received; labs, received; growth chart — and here the voice pauses — 'we have a summary page. Is there a full chart?' There is: in your binder, in the tab behind the labs, in the envelope that arrived on day 14, filed under the wrong tab and nearly forgotten.

This is the last moment in the medical track when a missing page is an errand instead of an absence. After the report is written, the file it describes is fixed; after the hearing, it is history. Ms. Ferreira, listening on speaker, mouths one word at you: send.

**Choices:**
- Send the complete growth chart today, by confirmed delivery, and log it in the chase log → **indicated_filing**  _(cash −5 ; FLAG: chartSent ; HIDDEN + Third opinion — complete growth chart confirmed sent to specialist)_
  - NOTE (shown after choosing): Confirmed, logged, initialed. The report, when it comes, will describe a whole file — and will say so, which is half its power.
- Tell them the summary page covers it — the numbers are the same → **indicated_filing**
  - NOTE (shown after choosing): The numbers are the same. A specialist's confidence is not a number, and her report will carry a sentence about summaries that a judge will read twice.

## [indicated_filing] The Other Track's Paperwork
*Day 42 — Monday, March 23, 2026 (dayOffset 42)*

The expunction track needs its own filing, in writing, inside its own clock — the deadline is Saturday, May 30, 2026, and it will not be extended by the fact that the dependency case is consuming your life. At the expunction hearing, when it comes, the burden works the other way from what you might expect: the agency must prove its indicated report by substantial evidence (23 Pa.C.S. § 6341(c.2)(5)), and you, as the appellant, have the right to see the investigation evidence the agency relied on. (23 Pa.C.S. § 6341(c.2)(4))

Filing now is cheap, fast, and permanent in the only way that matters here: it exists, dated, inside the window. Filing 'after the dependency hearing, when things are clearer' is a plan the calendar is already quietly voting against.

**Choices:**
- File the written expunction request now, well inside the 90 days, and request the agency's investigation evidence → **labs_back**  _(cash −10 ; FLAG: indicatedAppealFiled ; FLAG: recordsRequested ; HIDDEN + Indicated report — written expunction request filed within 90 days; investigation evidence requested)_
  - NOTE (shown after choosing): Stamped copy in the binder. The second track is no longer a letter in a drawer; it is a case, with your name spelled right.
- Wait for the dependency outcome first — one result will surely carry the other → **labs_back**
  - NOTE (shown after choosing): Surely is doing heavy lifting in that sentence. The two tracks have different deciders, different burdens, and — soon — very different amounts of time left.

## [labs_back] Labs, Follow-Ups, and Ordinary Paper
*Day 48 — Sunday, March 29, 2026 (dayOffset 48)*

The bone-health labs come back in the plain language of ranges and flags: nothing in them, the treating doctors note, explains the fracture by itself — and nothing in them rules out the fragility the consulting doctor raised, either. Medicine, at this resolution, is honest about its edges. The follow-up images show a healing fracture and no new injuries in the weeks since — weeks Wren has spent in foster care, a fact both sides will note, for opposite reasons, and a fact the court will have to weigh without flinching in either direction.

Ms. Ferreira adds both to the binder without commentary. "Records don't argue," she says. "They accumulate. Then, on one day, a person in a robe weighs the accumulation. Our whole job was the accumulation."

**Choices:**
- Prepare for the adjudication hearing — the packet, the timeline, the witnesses, in order → **foster_update**
  - NOTE (shown after choosing): Two weeks out. The checklist comes off the wall and goes into the binder's front pocket.

## [foster_update] The Foster Family's Notebook
*Day 50 — Tuesday, March 31, 2026 (dayOffset 50)*

Mrs. Lindqvist, Wren's foster mother, keeps a notebook too — feeds, sleeps, the arm's improving use, a baby hitting her milestones on a stranger's refrigerator chart. At the visit she shows it to you without being asked, and something in you understands her perfectly: she is also building a record, of care given, in a house the system sent a baby to on a Tuesday night.

Nothing in her notebook helps or hurts your case in the way you feared and hoped. It documents an ordinary, thriving baby — which is, in the dry arithmetic of hearings, a fact both sides will cite: proof she is safe where she is, and proof of what her ordinary days look like when someone writes them down. Records do not take sides. They accumulate. Sides are taken by the people who weigh them.

**Choices:**
- Thank her, note the milestones in your own notebook, and bring the dates to Ms. Ferreira → **wren_visit**
  - NOTE (shown after choosing): Two notebooks, one baby. The hearing will eventually hold both, which feels — strangely, completely — like the system working.
- Keep the visit about Wren — the notebook talk can stay at the lawyer's office → **wren_visit**
  - NOTE (shown after choosing): Wren, for her part, has strong opinions about a hat. The paperwork of her life proceeds around her, as it has since day 0.

## [wren_visit] What Healing Looks Like on Paper
*Day 51 — Wednesday, April 1, 2026 (dayOffset 51)*

The follow-up appointment summary is one page: fracture healing as expected; arm use nearly symmetrical; no new concerns. It will be read at the hearing by both sides in opposite directions — recovery in safe care, says one reading; an injury that healed the way this kind heals, says the other — and the judge will do with it what judges do with every page in this story: weigh it, in context, against the whole accumulation.

You file it in the binder's last tab, where it sits against the first day's imaging like bookends: a beginning the doctors argue about, and an ending they don't. In between is everything you built. Tomorrow the building stops, and the weighing starts.

**Choices:**
- Go home and lay out the binder, the timeline, and the notebook in hearing order → **pre_hearing**
  - NOTE (shown after choosing): Eleven tabs. Fifty-six days. One family's paper, as complete as two determined people and a checklist could make it — or as complete as it got.

## [pre_hearing] The Week Before the Hearing
*Day 52 — Thursday, April 2, 2026 (dayOffset 52)*

The adjudication hearing is set. The agency will put on its child-protection doctor. Your team will put on the consulting doctor. And the third opinion — if the packet was complete and the time was real — will arrive as a report, and possibly a witness, that neither side hired for comfort.

One decision remains, and it is a genuine dilemma, not a trap: the third opinion has not landed yet. It may come this week. You can ask the court for more time — courts grant and deny such requests for their own reasons, and a denied request can mean the hearing proceeds on a two-expert record anyway, with the delay having bought nothing. Or you can go forward on the record as built and let the accumulation speak.

Ms. Ferreira lays it out without steering: "Decide based on what the file holds today, not what we hope the mail holds tomorrow."

**Choices:**
- Go forward on the record as built — the packet and timeline are the case → **hearing_day1**
  - NOTE (shown after choosing): You sleep badly and dress carefully. The binder rides to court in the car like a fourth passenger.
- Ask for a continuance to wait for the third opinion, whatever the court decides → **continuance_beat**
  - NOTE (shown after choosing): Ms. Ferreira drafts the request in the same plain style as everything else in the binder: dated, specific, and honest about what is missing.

## [continuance_beat] The Continuance Decision
*Day 55 — Sunday, April 5, 2026 (dayOffset 55)*

The court hears the request in the courtroom's morning voice: dockets, calendars, a baby in placement, a statute-quiet room. The judge is not unkind. The judge is also looking at a schedule, a foster placement entering another month, and a record that — even its own lawyer admits — is missing the very page the delay is meant to produce.

The ruling is short. A brief delay is granted to a date certain — measured in days, not in the weeks a careful specialist's report on a complete file actually takes — and the hearing will proceed then, on the record that exists then. Time, in this building, is rationed by people who did not create your emergency and cannot extend your specialist's calendar.

**Choices:**
- Use the short delay, chase the report daily, and prepare to be heard on the record that exists → **end_continuance**
  - NOTE (shown after choosing): You call the specialist's office every morning at nine. Every morning, the answer is kind, and the same.

## [hearing_day1] Hearing, Day One: The Agency's Expert
*Day 55 — Sunday, April 5, 2026 (dayOffset 55)*

The agency's doctor testifies first, and she is good at her job in the way that matters here: plain, careful, unhurried. The fracture, she says, in a baby Wren's age, required more force than ordinary care provides; she has reviewed the images and the history offered, and the history does not account for it. Diagnosis, in her testimony, walks right up to the edge of accusation and — professionally — stops there. What carries it across, she says, is the absence of a fitting explanation in the record.

Ms. Ferreira's cross-examination is not theatre. It is inventory. Doctor, have you seen the complete follow-up imaging? The growth records, all of them? The labs? The timeline exhibits? Each answer — yes, and considered; or no, and noted — becomes a line in a record the judge is visibly keeping. Nothing about anyone's charm is entered into evidence. The binder is.

**Choices:**
- Listen for what the record holds, and let the inventory be the argument → **hearing_lunch**
  - NOTE (shown after choosing): By lunch, the judge's own notebook has two columns. You have seen that notebook's ancestor, on a legal pad, in your lawyer's office.

## [hearing_lunch] Lunch, and the Judge's Notebook
*Day 55, midday — Sunday, April 5, 2026 (dayOffset 55)*

In the cafeteria, Ms. Ferreira eats nothing and explains the judge's notebook, which she has been watching the way sailors watch weather. "She wrote longest during the inventory. Every 'had you seen the complete follow-up?' — she wrote the answer down. Judges decide cases in notebooks before they decide them in opinions, and hers is filling up with the shape of a file: what's in it, and what isn't."

"Tomorrow is our whole accumulation, presented in order. There is nothing left to be clever about. Clever was never available. There is only: here is the record, all of it, and here is what it does and does not prove." Theo asks if that's enough. She answers like the whole scenario in one sentence: "It is exactly as much as exists. That's what a record means."

**Choices:**
- Go back upstairs for day two — your side of the accumulation → **hearing_day2**
  - NOTE (shown after choosing): The binder is heavier than the baby was, the last time you carried her out of a building. You do not say this to anyone. You write it in the notebook, later, with the date.

## [hearing_day2] Hearing, Day Two: Paper Answers Paper
*Day 56 — Monday, April 6, 2026 (dayOffset 56)*

Your side's case is the accumulation, presented in order. The consulting doctor explains his different reading of the same bones — pattern, healing, the possibilities that bone health and an unwitnessed household moment keep open. The timeline goes in as exhibits: texts, schedules, receipts, the grandparents' plain statement. Your pediatrician's records go in: visit after visit of a baby brought in on schedule by the parents now sitting at this table.

And the third opinion, if it exists, is read into the room by a doctor with no stake in any of you — and if it does not exist, the room feels its absence in the precise shape of the missing tab in the binder. The judge asks every witness the same family of questions: What did you review? All of it, or some of it? What would change your mind? The answers are the hearing. Everything else was weather.

**Choices:**
- Rest your case on the record as built → **closings**
  - NOTE (shown after choosing): Ms. Ferreira's closing is eleven minutes long and contains no adjectives you can remember. It contains page numbers. Many of them.

## [closings] Closings: Two Burdens, Described Honestly
*Day 57 — Tuesday, April 7, 2026 (dayOffset 57)*

Closing arguments are short, because the record is long. The agency's lawyer describes a serious injury without an explanation that fits, and asks the court to find the burden carried. Ms. Ferreira describes the same injury inside a complete file — timeline, growth record, labs, divided experts — and asks the court to notice the distance between a diagnosis and an accusation, and to make the agency's proof walk every step of it, clearly and convincingly.

The judge thanks counsel in the tone of a person who has already begun the weighing, and takes the case under advisement. Outside, the courthouse steps hold both families of every case in the building, all doing the same arithmetic with different numbers: what was in the room, and what was never going to be.

**Choices:**
- Wait for the decision — a week of ordinary days, lived at half volume → **decision_node**
  - NOTE (shown after choosing): Wren's foster notebook gains six pages that week. Yours gains two: the dates of the hearing, written twice, the way you write things you cannot afford to get wrong.

## [decision_node] The Court Weighs the Paper
*Day 63 — Monday, April 13, 2026 (dayOffset 63)*

A week later — courts weigh things at the speed of courts — the decision is coming. Ms. Ferreira reviews the shape of it with you one last time, honestly: dependency must be proven by clear and convincing evidence, and the judge can only weigh what the record actually holds. The judge believed one expert over another in every version of this ending. What differed — all that ever differed — was what was in front of the judge when she chose.

The envelope, when it comes, is thin. They are always thin. Everything thick happened earlier, in binders and transcripts and discs in paper sleeves.

**Choices:**
- The record was complete — timeline, imaging, growth records, and a third opinion the court could weigh — and the agency's proof did not carry its burden → **end_home**  _(REQUIRES FLAG: timelineBuilt ; REQUIRES FLAG: completeImaging ; REQUIRES FLAG: thirdOpinionSent)_
  - NOTE (shown after choosing): This ending exists because the packet was complete. Every flag in that sentence was a trip to a counter, a signature, a stamp.
- The court credits the agency's expert on the record as built — adjudication follows the credited testimony → **end_adjudicated**
  - NOTE (shown after choosing): A judge weighed two qualified readings of the same bones and chose. That choosing is the system working as designed, and it can still be wrong about a family — which is why the record, again, is what an appeal would read.
- The dependency judge rules on the hearing record — while your timely expunction case, on its own burden, is still to be decided → **end_split**  _(REQUIRES FLAG: indicatedAppealFiled ; REQUIRES FLAG: timelineBuilt)_
  - NOTE (shown after choosing): This ending exists because the second track was filed in time and the timeline was built. Two tracks, two burdens, two deciders.
- The hearing was decided on the two-expert record that existed on the day — the third opinion was never in the room → **end_continuance**  _(REQUIRES NO FLAG: thirdOpinionSent)_
  - NOTE (shown after choosing): Absence, too, is a record. The judge weighed what was there. What was not there had a reason, a date, and a paper sleeve it never arrived in.

## [end_home] Not Sustained — Home
*Day 63 — Monday, April 13, 2026 (dayOffset 63)*

The court's opinion is the binder, reflected back. The agency's expert was credited as careful — and her own testimony, on cross, had inventoried the limits of what she was given. Against a complete record — the full imaging set, the growth history of a baby reliably brought for care, the labs, and a third specialist's independent read that the fracture pattern and the documented timeline could fit an accidental or bone-fragility explanation — the judge finds the proof does not reach clear and convincing on how this injury happened, or at whose hands.

Dependency is not sustained. The petition is dismissed on the record as built. Wren comes home on a Tuesday, with the diaper bag returned — bottles, blanket, the little hat, now slightly small — and a follow-up appointment card on the refrigerator, where a log once kept a different kind of vigil.

The indicated letter is a separate track with its own clock and its own hearing still ahead, and the opinion says so in a footnote, because courts know parents confuse them. Your expunction case, filed in time, will be decided on its own burden. Today, though, the thick binder closes, and the thin envelope goes in a drawer — a good drawer, this time, the kind you open.

**Ending.**

**Debrief:**
- THE BOARD, MAPPED — Medical track: complete. The full imaging set (flag: completeImaging), growth records, labs, and a third opinion obtained on a complete packet (flags: packetAssembled, thirdOpinionSent) meant every expert — including the agency's — was cross-examined against the same whole file. Diagnosis and accusation were separated on paper: the injury was real and serious; the record did not carry the further step, clearly and convincingly, to who caused it or how.
- Dependency clock: removal on day 1, shelter care hearing within 72 hours (42 Pa.C.S. § 6332; 23 Pa.C.S. § 6315(d)) on Friday, February 13, 2026, adjudication on days 55–56, decision on Monday, April 13, 2026 — petition not sustained, Wren home. Timeline track: the day-by-day care timeline built from contemporaneous timestamps (flag: timelineBuilt) replaced the chart's bare phrase 'inconsistent accounts' with documents a judge could weigh.
- Indicated track: the expunction request was filed within the 90 days allowed (23 Pa.C.S. § 6341(a)(2); deadline Saturday, May 30, 2026, flag: indicatedAppealFiled) and remains a separate proceeding where the agency bears the burden of proving its report by substantial evidence. (23 Pa.C.S. § 6341(c.2)(5)) It was never in this hearing's gift to decide it. What was never in your control: which expert the judge would credit, the fracture itself, the first doctor's reading, and the pace of every office in the chase. This outcome does not certify anyone a perfect parent; it records that a burden was set by law, a record was built to test it, and the proof did not carry. Outcomes here also turn on workers, judges, and luck — this one also turned on eleven checked boxes.

## [end_adjudicated] Adjudicated — The Expert the Court Credited
*Day 63 — Monday, April 13, 2026 (dayOffset 63)*

The court credits the agency's expert. The opinion says why, in the language of records: her reading was direct, her review was sufficient for the weight the court gives it, and the competing reading — on the record actually assembled — left the court with possibilities where it needed proof it could hold. Where the packet had gaps, the opinion names them, one by one, like a checklist read backward.

Wren is adjudicated dependent. A plan follows: services, visits, reviews — the ordinary machinery of a case that now continues, with your compliance and the agency's obligations both to be documented, both to matter at every review. Ms. Ferreira, in the hallway, is already talking about the record of the next hearing, and about an appeal, which — as another story in this series shows — would read only what this record holds.

You drive home past the foster family's street without meaning to. Wren's hat is in your bag. You put it, deliberately, in the notebook drawer — the drawer of things that are being kept, correctly, for later.

**Ending.**

**Debrief:**
- THE BOARD, MAPPED — Medical track: the court weighed two qualified experts and credited the agency's. Where the record was incomplete — a summary instead of the full imaging set (no completeImaging flag), a timeline never built from timestamps (no timelineBuilt flag), a third opinion never obtained on a complete packet (no thirdOpinionSent flag) — the opinion's reasoning runs through those gaps. The hearing turned on the record assembled, not on anyone's manner in the room; no dialogue in this case was ever going to out-argue a missing disc.
- Dependency clock: removal day 1, shelter care within 72 hours (42 Pa.C.S. § 6332; 23 Pa.C.S. § 6315(d)), adjudication days 55–56, dependency found by clear and convincing evidence as the court weighed it, on Monday, April 13, 2026. The case continues to reviews; the plan's paper now becomes the record that future hearings — and any appeal, which reviews the record made below — will read.
- Indicated track: if the expunction request was filed within 90 days (23 Pa.C.S. § 6341(a)(2); deadline Saturday, May 30, 2026, flag: indicatedAppealFiled), that separate case still runs, under the agency's substantial-evidence burden (23 Pa.C.S. § 6341(c.2)(5)), and can end differently from this one; if it was never filed, the letter outlives the hearing by years. What was never in your control: the judge's credibility call between experts, the injury, the first reading of it. An adjudication is a finding about a record and a risk, not a measurement of your love or your worth — and outcomes here also turn on workers, judges, and luck.

## [end_split] Split — Dependent, But the Report Is Expunged
*Day 118 — Sunday, June 7, 2026 (dayOffset 118)*

Two decisions, months apart, on the same facts — and they do not match. That is not an error in this story. It is the system, running two tracks with two burdens, exactly as built.

First, the dependency court adjudicates Wren dependent: on the hearing record, crediting the agency's expert, it finds the proof clear and convincing that Wren needs the court's protection while her care is supervised and her injury's story remains, to that court, insufficiently explained. The case continues — plan, visits, reviews.

Then, on Sunday, June 7, 2026, the expunction decision arrives. There, the question was different — not what protection Wren needs, but whether the agency can prove, by substantial evidence, that its indicated report naming you is accurate. (23 Pa.C.S. § 6341(c.2)(5)) On the timeline you built and filed — timestamps, schedules, the documented weekend — the hearing officer finds the agency's proof does not carry that burden as to you. The report is expunged. Your name comes off the registry the letter put it on. One track says the court will supervise Wren's care. The other says the state may not keep calling you a perpetrator. Both papers go in the binder, in different tabs, both true in the only way court papers are true: each decided its own question, on its own record, under its own burden.

**Ending.**

**Debrief:**
- THE BOARD, MAPPED — Dependency track: adjudicated on the expert the hearing court credited; placement and plan continue under review; the adjudication record (flags: timelineBuilt, and the imaging/third-opinion flags if set) is what any further review or appeal would read. Medical track: the fracture, the split expert readings, and the completeness of the file decided the dependency hearing; the same file, tested under a different burden, decided the expunction differently.
- Indicated track: expunged. This half of the split existed only because the written request was filed inside the 90 days (23 Pa.C.S. § 6341(a)(2); deadline Saturday, May 30, 2026, flag: indicatedAppealFiled), because you could obtain the agency's investigation evidence as the appellant (23 Pa.C.S. § 6341(c.2)(4)), and because the built timeline (flag: timelineBuilt) gave the hearing officer documents, not recollections, to weigh against the agency's substantial-evidence burden. (23 Pa.C.S. § 6341(c.2)(5))
- What was never in your control: that two deciders, shown overlapping facts under different burdens, can honestly reach different answers — and did. Neither paper cancels the other; neither measures your worth as a mother. Outcomes in both tracks also turn on workers, judges, hearing officers, and luck. The split is the board, mapped honestly: protection and accusation are different questions, and this family won one and not the other.

## [end_continuance] The Continuance That Ran Out
*Day 66 — Thursday, April 16, 2026 (dayOffset 66)*

The third opinion arrives on a Thursday — thorough, careful, and eleven days after the hearing it was meant for. The specialist's office apologizes with the helpless sincerity of people whose calendars are also a system. Ms. Ferreira reads it twice, puts it in the binder, and tells you the truth in the order you need it: what it says, and when it came, are now two separate facts, and only one of them was ever going to be weighed.

The hearing, held on the date the short continuance allowed, proceeded on the record that existed: two experts, opposed, and a file whose gaps the court catalogued as it credited the agency's doctor and adjudicated Wren dependent. The late report joins the binder as its thickest, saddest tab — not evidence in a decided hearing, but the foundation of what your lawyer files next, in a system where the next record is always, already, being written.

Wren remains placed under the plan. The visits continue. The binder goes home with you, heavier than when it arrived, in every sense you have learned to measure weight.

**Ending.**

**Debrief:**
- THE BOARD, MAPPED — Medical track: decided incomplete. The third opinion existed — eventually — but a hearing can only weigh what is in the room on the day; a continuance measured in days could not hold a specialist's calendar measured in weeks. Where the underlying flags were never set (complete imaging, flag: completeImaging; packet, flag: packetAssembled), the delay was never going to cure them either: time does not assemble records. People at counters do, weeks earlier.
- Dependency clock: removal day 1; shelter care within 72 hours (42 Pa.C.S. § 6332; 23 Pa.C.S. § 6315(d)); adjudication held on the continued date, decision Thursday, April 16, 2026, dependency found on the two-expert record. The case continues to reviews, where the late-arriving report — and everything documented since — becomes part of the record those reviews will read. Indicated track: its 90-day clock (23 Pa.C.S. § 6341(a)(2); deadline Saturday, May 30, 2026) ran the whole time, indifferent to the dependency calendar; if the request was filed (flag: indicatedAppealFiled), that track still offers a separate decision under the agency's substantial-evidence burden. (23 Pa.C.S. § 6341(c.2)(5))
- What was never in your control: the judge's continuance ruling, the specialist's queue, and the arithmetic of two calendars that were never designed to mesh. This ending measures timing and paper, not devotion — outcomes here also turn on workers, judges, and luck, and sometimes on nothing more heroic than which week a disc left a shelf.
