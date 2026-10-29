# THE FIRST 90 DAYS — Scenario 63: “Cancelled, Again”

*Human-readable script. This document and `scenario-63.json` are generated from a single source and match node-for-node: same IDs, same order, same choices, same effects.*

**The family is fictional — a composite. No real person's story appears here.**

**Content note:** This scenario depicts repeated cancellation of a parent's visits by a visitation center for staffing reasons, and a review report that miscounts her attendance. There is no graphic content. Players may skip any scene or use the quick exit at any time.

**How to read effects:** `cash −40` changes the player's cash. `FLAG: name` sets a flag the engine tracks. `HIDDEN + item` means the case file quietly records that item at this choice — the player does not see it when it happens. `NOTE:` is text shown to the player right after choosing.

Start date: Monday, August 3, 2026. Day offsets are days since the scenario's start date. Tier: Hard.

## [start] Tuesdays and Saturdays
*Day 0 — Monday, August 3, 2026 — Monday, August 3, 2026 (dayOffset 0)*

Your name is Simone. Your son Felix is eight, and he is living in foster care — placed before this story opens, in a part of the case this story does not retell. What this story covers is the rhythm the case now runs on: visits, Tuesdays and Saturdays, at a visitation center across town.

The center's habit is a phone call. The day before a visit, someone rings to confirm — or you ring them. Ms. Kessler, who runs the desk, is brisk and not unkind, and the calls are pleasant, and at the end of each one nothing exists that a third person could read. In this system, that last part is not a detail. It is the whole mechanism of the next two months.

You attend your visits. That sentence is true, simple, and — as the summer will show — surprisingly hard for a file to say, if the file is built out of phone calls.

**Choices:**
- Go to the first Tuesday visit — and think about the phone call that confirmed it → **confirm_choice**
  - NOTE (shown after choosing): A visit, confirmed by a voice, attended by a mother, recorded by no one. Hold that thought.

## [confirm_choice] The Day Before
*Day 1 — Tuesday, August 4, 2026 — Tuesday, August 4, 2026 (dayOffset 1)*

It is Tuesday, August 4, 2026, visit day, and yesterday's confirmation was the usual call: two minutes, friendly, gone. There is another way to confirm a visit, and it costs nothing but the small awkwardness of being the person who puts things in writing: a short text or email the day before — visit, date, time, ‘please confirm’ — which the center answers, or doesn't, in writing either way.

Paper (and its digital cousins) have dates on them. Phone calls have memories on them. This case will be decided, in part, by which of those your confirmations are made of.

**Choices:**
- Start confirming in writing — a short message the day before every visit, replies saved → **written_start**  _(FLAG: confirmWritten; HIDDEN + Visits — confirmed in writing the day before, from the first week)_
  - NOTE (shown after choosing): The first reply is two words: ‘Confirmed, thanks.’ Two words, with a date on them. That is what evidence looks like before it grows up.
- Keep phoning — it works, it's friendly, and Ms. Kessler knows your voice → **phone_start**
  - NOTE (shown after choosing): She does know your voice. Voices, unfortunately, cannot be attached to a review report.

## [written_start] Two Words, Dated
*Day 2 — Wednesday, August 5, 2026 — Wednesday, August 5, 2026 (dayOffset 2)*

The thread begins: your message, the center's reply, your message, the reply. It is the dullest correspondence in the world and, potentially, the most valuable paper in your case — a dated, third-party confirmation for every visit, written by the center itself, before anything about the visit could be disputed.

You save the replies the way you save receipts. Somewhere, an attendance percentage is going to be computed about you this year. When it is, there will be something to compute it against.

**Choices:**
- Go on with the visits — Tuesdays and Saturdays, confirmed the day before → **good_weeks**
  - NOTE (shown after choosing): A rhythm with a paper shadow. The summer can now begin, in both versions.

## [phone_start] The Friendly System
*Day 2 — Wednesday, August 5, 2026 — Wednesday, August 5, 2026 (dayOffset 2)*

The calls continue, warm and weightless. Ms. Kessler confirms; you attend; the visit happens; the call evaporates. If anyone ever asks whether a given visit was confirmed, the answer will live in two people's recollections, one of whom answers phones for forty families.

None of this feels like a mistake. That is what makes it one of this system's most reliable traps: the informal way works perfectly, right up until the moment it is asked to prove something.

**Choices:**
- Go on with the visits — Tuesdays and Saturdays, as confirmed by phone → **good_weeks**
  - NOTE (shown after choosing): The visits are real. Their confirmations are weather: true, and gone.

## [good_weeks] The Good Weeks
*Day 8 — Tuesday, August 11, 2026 — Tuesday, August 11, 2026 (dayOffset 8)*

The first full week runs the way weeks are supposed to: Tuesday's visit, Saturday's visit, Felix at the center-room door with his shoes already off and an agenda already formed. He is working on a drawing series — the center, the bus, your kitchen, the center again — and each visit adds a panel.

This is what attendance actually looks like from inside it: buses, snacks, drawings, the ordinary machinery of showing up. Files do not see machinery. Files see counts. The distance between those two views is where this scenario lives.

**Choices:**
- Keep the rhythm — and keep whatever record of it you are keeping → **second_saturday**
  - NOTE (shown after choosing): Showing up is the job. Proving you showed up, it turns out, is a second job, running in parallel, unpaid.

## [second_saturday] The Drawing, Panel Four
*Day 12 — Saturday, August 15, 2026 — Saturday, August 15, 2026 (dayOffset 12)*

Saturday, August 15, 2026's visit is the good kind that leaves nothing to write home about: a board game Felix has decided to be magnanimous about losing, a sandwich negotiated down to its crusts, the drawing's fourth panel — your kitchen, with the table set for two and a third chair drawn in pencil, ‘for later.’

Ms. Kessler, passing with a clipboard, says the thing staff say: ‘You're one of my reliables.’ It is true, it is kind, and it will appear nowhere. Praise, in this building, is spoken. Counts are written. Remember which one the report will use.

**Choices:**
- Thank her — and go home on the bus with panel four in your bag → **cancel1**  _(HIDDEN + Visit held — full visit; Felix's drawing, panel four)_
  - NOTE (shown after choosing): ‘One of my reliables.’ File that under things that are true and unprovable, unless the paper says otherwise.

## [cancel1] Cancelled, the First Time
*Day 15 — Tuesday, August 18, 2026 — Tuesday, August 18, 2026 (dayOffset 15)*

Tuesday, August 18, 2026, visit morning. Your phone rings while the kettle is on: Ms. Kessler, apologetic, brisk. The center is short-staffed today; today's visit is cancelled. ‘We'll find you a make-up slot,’ she says, ‘when there's a slot.’ There is no date in that sentence. There is barely a noun in it.

This happens, in this system, more often than any report admits: a visit cancelled by the provider's arithmetic, not by the parent's. What happens next — in the file, I mean — depends on what you do in the next hour.

**Choices:**
- Answer the same day in writing — sorry to miss Felix, please propose a make-up date, in reply → **cancel1_written**  _(FLAG: cancelTrail; HIDDEN + Cancellation 1 — center cancelled by phone, morning of; parent answered the same day in writing requesting a make-up)_
  - NOTE (shown after choosing): Your message is short, warm, and dated, and it asks for the one thing the phone call didn't contain: a date. The asking is now a record.
- Accept the verbal promise — ‘we'll find a slot’ — and hang up kindly → **cancel1_verbal**  _(cash −6)_
  - NOTE (shown after choosing): Kindly is how you do everything. The promise, meanwhile, has no date, no witness, and no existence outside Ms. Kessler's memory of a busy morning. (And you had already paid the bus fare before the phone rang.)

## [cancel1_written] A Reply with No Date in It
*Day 16 — Wednesday, August 19, 2026 — Wednesday, August 19, 2026 (dayOffset 16)*

The center replies the next day, in writing, which is its own small victory: ‘Noted — we'll offer a make-up when there's a slot.’ You read it three times. The sentence confirms the cancellation was theirs. It confirms you asked. It does not contain a date, a day, or a time, and you understand, holding it, that ‘when there's a slot’ is a place where make-up visits go to be forgotten politely.

You save it anyway. A reply that promises nothing still proves two things: who cancelled, and that you answered in writing the same day. Percentages are computed from less.

**Choices:**
- Save it, and go to Saturday's visit as scheduled → **held_visit2**
  - NOTE (shown after choosing): Who cancelled: documented. Make-up: vaporous. Both halves matter, and now both halves exist.

## [cancel1_verbal] When There's a Slot
*Day 16 — Wednesday, August 19, 2026 — Wednesday, August 19, 2026 (dayOffset 16)*

No reply exists, because no message was sent. In the center's day, the cancellation was one of eleven phone calls; in yours, it was the day's whole weather. Ms. Kessler meant the promise. Meaning a promise and scheduling it are different departments, and only one of them keeps a calendar.

Saturday's visit is still on, confirmed the usual way. You go, because going is what you do — and because some part of you already suspects that going, undocumented, is a tree falling in a forest of forms.

**Choices:**
- Go to Saturday's visit — showing up is still the main thing → **held_visit2**
  - NOTE (shown after choosing): It is the main thing. The scenario's whole argument is that ‘main’ and ‘only’ are different words.

## [held_visit2] A Held Visit
*Day 22 — Tuesday, August 25, 2026 — Tuesday, August 25, 2026 (dayOffset 22)*

Tuesday, August 25, 2026: a visit that happens, which in this summer's accounting is becoming a category worth naming. Felix has opinions about the cancelled one — children keep their own attendance records, in a medium adults can't file — and then the visit does what visits do: game, sandwich, drawing, goodbye at the door with his hand up, palm out, the way he waves now.

You attend. As you attend every visit that is actually held. If the summer's file could see the room, there would be no scenario. The file sees counts, and the counts are being kept by the party that cancels.

**Choices:**
- Go home — and, whenever the make-up is mentioned, notice whether a date is attached → **makeup_chase**
  - NOTE (shown after choosing): Held: attended. Cancelled: pending a date that does not exist. The arithmetic is already drifting, and arithmetic drifts downhill.

## [makeup_chase] Chasing the Make-Up
*Day 26 — Saturday, August 29, 2026 — Saturday, August 29, 2026 (dayOffset 26)*

Saturday, August 29, 2026, a held visit — and at the desk, the make-up question, raised again. ‘Still nothing,’ Ms. Kessler says, not unkindly. ‘You're on the list.’ There is a list. You have never seen the list. The list, if it says anything about dates, has not said it to you.

There are two ways to leave this conversation: with a dated written record that you asked, again — or with the warm understanding of two people who both intend well, which is the raw material from which ‘the parent never followed up’ is later manufactured.

**Choices:**
- Follow up in writing that evening — second request for a make-up date for the cancelled Tuesday → **cancel2**  _(FLAG: cancelTrail; HIDDEN + Make-up request — repeated in writing; center replied 'when there's a slot,' no date given)_
  - NOTE (shown after choosing): Asked, again, in writing, again with a date on the asking. The file is learning a pattern, even if the calendar isn't.
- Leave it with Ms. Kessler — you're on the list, and pushing helps no one → **cancel2**
  - NOTE (shown after choosing): On the list. The list is the most trusted and least examined document in this entire system.

## [cancel2] Cancelled, Again
*Day 29 — Tuesday, September 1, 2026 — Tuesday, September 1, 2026 (dayOffset 29)*

Tuesday, September 1, 2026. The phone rings in the morning, and you know the shape of the call before the kettle boils: staffing, apologies, cancellation — the second one. ‘Same as before,’ Ms. Kessler says, ‘we'll find a slot.’ Two make-ups are now owed to Felix's summer, in a currency of slots that has never once been observed in the wild.

A pattern cancelled once is an accident. Cancelled twice, with no make-up dated, it is a system describing itself. What the review will call it depends on the paper.

**Choices:**
- Answer in writing the same day, as before — cancellation noted, make-up requested, again → **rumor_beat**  _(FLAG: cancelTrail; HIDDEN + Cancellation 2 — center cancelled by phone; parent answered the same day in writing requesting a make-up)_
  - NOTE (shown after choosing): Same day, in writing, second time. A trail is just a thing that happens twice with dates on it.
- Accept it verbally, as before — they know you're reliable → **rumor_beat**  _(cash −6)_
  - NOTE (shown after choosing): They do know. Knowledge held by a busy desk, about forty families, across a summer, is a depreciating asset. (The bus fare, again, was already spent.)

## [rumor_beat] Sixty-Something Percent
*Day 33 — Saturday, September 5, 2026 — Saturday, September 5, 2026 (dayOffset 33)*

A held visit, Saturday, September 5, 2026 — and at the door afterward, the foster parent mentions, in the careful voice people use for other people's paperwork, something she heard on a call with the agency: Simone's attendance described as ‘not great — sixty-something percent, they said.’

Sixty-something. You do the first arithmetic standing in the doorway, and it does not work on any numbers you know: you have attended every visit that has ever actually been held. Unless — and the thought arrives whole — the cancelled ones are being counted as yours. A percentage is a fraction. Fractions have two halves. You have been watching the top half. Someone else owns the bottom.

**Choices:**
- Go home and start counting from your own records — every scheduled visit since August → **cancel3**
  - NOTE (shown after choosing): Scheduled. Held. Cancelled. Attended. Four different numbers wearing one another's coats. Time to separate them.

## [cancel3] Halfway There
*Day 40 — Saturday, September 12, 2026 — Saturday, September 12, 2026 (dayOffset 40)*

Saturday, September 12, 2026 — a Saturday. You are on the bus, halfway to the center, Felix's snack in your bag and panel nine of the drawing series promised for today, when the phone rings. Staffing. Apologies. Cancelled — the third time in two months. The bus continues for one more stop out of pure momentum before you can get off.

‘When there's a slot,’ Ms. Kessler says, completing the set. Three cancellations, three promises, zero dates. You stand at a bus stop in the wrong half of town, holding a sandwich bag, being reliable at a cancelled visit.

**Choices:**
- Text the center from the bus stop, in writing — cancellation noted, make-up requested, third time → **bus_ride_home**  _(cash −7; FLAG: cancelTrail; HIDDEN + Cancellation 3 — Saturday; parent already travelling when the center cancelled; written notice sent the same day)_
  - NOTE (shown after choosing): Sent from a bus stop, timestamped by the network itself. If a trail could have a monument, this is it.
- Call back and accept it verbally — the bus home is not the place for paperwork → **bus_ride_home**  _(cash −7)_
  - NOTE (shown after choosing): The fare is spent either way. What differs is whether today's cancellation joins the others in writing, or in memory.

## [bus_ride_home] The Long Way Back
*Day 41 — Sunday, September 13, 2026 — Sunday, September 13, 2026 (dayOffset 41)*

The bus home takes the long way, as buses do when the trip has no visit at the end of it. You think about Felix being told, by someone, in some words, that today's visit is off — and about what word will be used for it in the summary of the summer, and whose name will be grammatically attached to the cancellation when it gets there.

Summaries assign. That is their job and their danger. A cancellation described without an owner tends to acquire the nearest name — and the nearest name, in an attendance paragraph, is always the parent's.

**Choices:**
- Get home, and do the full count at the kitchen table → **monday_after**  _(cash −6)_
  - NOTE (shown after choosing): Return fare: spent on a visit that didn't happen. Some expenses are also evidence.

## [monday_after] The Count
*Day 42 — Monday, September 14, 2026 — Monday, September 14, 2026 (dayOffset 42)*

At the kitchen table, the count, for the report window the summer will be judged on — Tuesday, August 4, 2026 to Saturday, September 12, 2026: twelve visits scheduled, Tuesdays and Saturdays. Three cancelled by the center. Nine actually held. You attended nine. Nine of nine held visits: every single one.

And yet a voice on a phone call said sixty-something. Twelve scheduled and nine attended is seventy-five percent, not sixty — so even counting the center's cancellations against you doesn't reach their number. Something else is in their denominator. You can guess at it. Guessing, as this series never tires of showing, is what you do instead of reading the file.

**Choices:**
- Write the count down, dated, with the four numbers separated → **tally_night**  _(HIDDEN + Parent's tally — 12 scheduled, 3 cancelled by the center, 9 held, 9 attended)_
  - NOTE (shown after choosing): Four numbers, separated at last. Now: where did fifteen come from — because sixty percent of their count means their count isn't twelve.

## [tally_night] Nine of Nine
*Day 43 — Tuesday, September 15, 2026 — Tuesday, September 15, 2026 (dayOffset 43)*

Nine of nine. You sit with the fraction a while. It is, as a measure of a mother, perfect — and, as a document, worthless, because it is yours: your count, your table, your word. The report's number will arrive wearing the agency's letterhead, and letterhead is a kind of armour that kitchen-table arithmetic does not pierce by itself.

What pierces it is the agency's own paper, read closely: their attendance summary, their cancellation log, their denominator, in their hand. There is a way to ask for that paper. There has been, all along.

**Choices:**
- Ask your lawyer how to get the center's own numbers — before the review does its arithmetic without you → **records_beat**
  - NOTE (shown after choosing): ‘Their number, their paper.’ Your lawyer is already nodding. This is her favourite kind of fight: one where the other side has already written everything down.

## [records_beat] Their Number, Their Paper
*Day 44 — Wednesday, September 16, 2026 — Wednesday, September 16, 2026 (dayOffset 44)*

Your lawyer — counsel is your right in this case, as the law provides (42 Pa.C.S. § 6337) — lays it out in one breath: ‘You may request the case record, and the regulation says it “shall be released upon request” (55 Pa. Code § 3130.44(d)). We ask for the attendance summary and the center's scheduling log. Their percentage was computed from something. We are going to read the something.’

The request is one page. It asks for the paper behind a number that has already been said out loud about you on a phone call — which makes it, in the quiet taxonomy of this system, not early and not late, but exactly on time.

**Choices:**
- Sign and send the written request — attendance summary and scheduling log, in writing → **packet_arrives**  _(cash −4; FLAG: recordsRequested)_
  - NOTE (shown after choosing): Signed, dated, copied. The denominator is about to have an author you can quote.
- Skip it — your own count is right, and the review will listen to reason → **no_packet63**
  - NOTE (shown after choosing): Your count is right. Reviews, as a species, listen to records. Reason is admitted only when it arrives as an attachment.

## [packet_arrives] Fifteen
*Day 50 — Tuesday, September 22, 2026 — Tuesday, September 22, 2026 (dayOffset 50)*

The packet arrives, and there it is, in the center's own summary: ‘Family attended 9 of 15 scheduled visits (60%).’ Fifteen. Your count said twelve — and the scheduling log, read line by line with your lawyer, explains the extra three: make-up slots the center logged as ‘scheduled’ after each cancellation, on dates it never gave you, at times it never sent. You were marked absent from visits you were never told existed.

And the three real cancellations? In the summary's arithmetic they sit in your column as visits not attended — the center's staffing folded, silently, into the family's percentage. Nine of nine held visits became sixty percent of fifteen scheduled ones. Every step of that transformation is on paper. Their paper. That is what makes it answerable.

**Choices:**
- Ask your lawyer what the corrected table needs — line by line, from their own log → **prep_beat**  _(HIDDEN + Attendance summary — 15 'scheduled,' 9 attended (60%); provider cancellations and unannounced make-up slots folded into the parent's percentage)_
  - NOTE (shown after choosing): Their number, their paper, their log. The correction will not need a single fact from outside their own file.

## [no_packet63] Your Count Against Their Letterhead
*Day 50 — Tuesday, September 22, 2026 — Tuesday, September 22, 2026 (dayOffset 50)*

Without the packet, your preparation is your kitchen-table count and whatever written trail the summer left: confirmations, if you made them in writing; cancellation replies, if you answered in writing. True numbers, honestly kept — and authored by the one person the review is already inclined to treat as an interested party: you.

Your lawyer is blunt about the physics. ‘If their summary says sixty percent and your page says nine of nine, the room believes the summary until your page is made of their paper. We go in with what we have. It is less than we could have had.’

**Choices:**
- Prepare anyway — build the best table your own records allow → **prep_beat**
  - NOTE (shown after choosing): A table built from your own trail is still a table. Whether it can move their number depends on how much of the trail is in writing.

## [prep_beat] The Corrected Table
*Day 53 — Friday, September 25, 2026 — Friday, September 25, 2026 (dayOffset 53)*

The last week before the review offers the scenario's final fork, and it is pure paperwork. The corrected table exists to be built: four columns — scheduled, cancelled by the center, actually held, attended — every row dated, the confirmations and cancellation replies attached, the center's own log lines quoted where you have them. Attached, it goes into the review packet, where percentages are read.

Or you can go in with the story: three cancellations, a bus ride, a promise made three times. The story is true, and moving, and takes four minutes to tell, in a hearing that runs on attachments.

**Choices:**
- Build the corrected table with your lawyer and attach it to the review packet → **table_built**  _(cash −5; FLAG: mathAttached; HIDDEN + Corrected attendance table — 12 scheduled, 3 cancelled by the center, 9 held, 9 attended; confirmations and replies attached)_
  - NOTE (shown after choosing): Four columns, twelve rows, every number sourced. Arithmetic, dressed for court.
- Go in with the story — tell it clearly, in order, and trust the room → **story_ready**
  - NOTE (shown after choosing): The room may well believe you. Believing and correcting a written finding are, as ever, two different procedures.

## [table_built] Four Columns
*Day 54 — Saturday, September 26, 2026 — Saturday, September 26, 2026 (dayOffset 54)*

The table is one page and it is beautiful in the way only arithmetic can be: twelve scheduled visits, each with its date; three cancelled by the center, each with the date of your same-day written answer; nine held; nine attended. At the bottom, your lawyer adds the center's own figure, quoted from its summary, and the three logged make-up slots nobody was ever told about — the whole transformation, visible at a glance.

Sixty percent, it turns out, was never a measure of you. It was a measure of a denominator. Denominators can be corrected. That is what the review is for — when someone brings the correction in writing.

**Choices:**
- File it with the review packet — and go to the last visits before the hearing → **review_notice**
  - NOTE (shown after choosing): Filed, copied, attached. The number going into the review now has competition.

## [story_ready] The Story, Rehearsed
*Day 54 — Saturday, September 26, 2026 — Saturday, September 26, 2026 (dayOffset 54)*

Your lawyer rehearses you until the story is tight: the three phone calls, the three promises, the bus. It is true in every particular and it will be believed, probably, in the way stories are believed in rooms that run on exhibits — warmly, personally, and without the percentage moving, because a percentage is a document and can only be corrected by another document.

‘Tell it well,’ she says. ‘Then watch what the finding says. Findings quote paper. If the finding moves at all, it will move toward the make-ups — those, a room can grant on a story. The number needs the table.’

**Choices:**
- Go to the review with the story — and ask, at minimum, for the make-ups to be ordered → **review_notice**
  - NOTE (shown after choosing): A true story, well told. In this system, that buys more than nothing and less than arithmetic.

## [review_notice] Sixty Percent, in Print
*Day 57 — Tuesday, September 29, 2026 — Tuesday, September 29, 2026 (dayOffset 57)*

The review report arrives ahead of the hearing, and there, in the attendance paragraph, the summer has been summarized in one line: ‘Family attended 60% of scheduled visits.’ Tuesday, September 29, 2026's report was written from the center's summary, the way reports are — which is to say, the number has now been quoted into a second document, and quotations, as this series keeps showing, are how numbers harden.

Whether it hardens further — into the plan's findings, where it will shape what the autumn asks of you — depends on what is lying on the table next to it when the room convenes: a corrected table, a set of dated replies, a story, or nothing.

**Choices:**
- Go to the last visits, and then to the review → **last_visits**
  - NOTE (shown after choosing): The line is printed. Printed lines can still be corrected — by better-printed lines, attached in time.

## [last_visits] Panel Ten
*Day 58 — Wednesday, September 30, 2026 — Wednesday, September 30, 2026 (dayOffset 58)*

The visits before the review are held, both of them, and attended, both of them — the streak that the report's percentage somehow describes as sixty. Felix presents panel ten of the drawing series: the review building, as imagined by an eight-year-old, with many windows and, in the largest one, a table with four columns. He has been listening more carefully than anyone knew.

‘That's the counting room,’ he says. He is not wrong. Tomorrow, the counting happens.

**Choices:**
- Go to the review → **review**
  - NOTE (shown after choosing): Nine of nine, and counting. What the room does with the count is the last scene of the summer.

## [review] The Review
*Day 60 — Friday, October 2, 2026 — Friday, October 2, 2026 (dayOffset 60)*

The review convenes. The report is presented; the attendance paragraph is read aloud in the level voice reserved for numbers: ‘Family attended 60% of scheduled visits.’ Nobody in the room experiences that sentence as an accusation. It is simply what the file says — which is exactly the problem your whole summer has been about.

Then it is your side's turn. Your lawyer looks at what the summer actually put on paper — the confirmations, the replies, the log, the table — and chooses her lead.

**Choices:**
- Present the corrected table — confirmations, same-day cancellation replies, and the center's own summary and log attached → **end_corrected**  _(REQUIRES FLAG: confirmWritten ; cancelTrail ; recordsRequested ; mathAttached)_
  - NOTE (shown after choosing): This lead exists only because every layer of it was built before today: written confirmations, written answers, the requested record, the attached arithmetic. The room is just where they are spent.
- Present the cancellation replies and ask for the make-up visits to be ordered with dates → **end_makeups**  _(REQUIRES FLAG: cancelTrail)_
  - NOTE (shown after choosing): The replies prove the cancellations were the center's and that you asked, in writing, every time. A room can grant dates on that paper — even if it leaves the number alone.
- Tell the story of the three cancellations and ask for the make-ups → **end_makeups**
  - NOTE (shown after choosing): True, in order, and believed in the way stories are believed. Make-ups live within a story's reach. Percentages don't.
- Say the visits ‘mostly happened’ and move on to services → **end_poor**
  - NOTE (shown after choosing): ‘Mostly happened’ is, not coincidentally, almost exactly what sixty percent says. The room nods, and the number keeps its coat.

## [end_corrected] Ending — Sixty Percent, Corrected
*Day 66 — Thursday, October 8, 2026 — Thursday, October 8, 2026 (dayOffset 66)*

**Ending.**

**Debrief:**
- WHAT THE FILE HELD (the hidden record, revealed): A denominator, taken apart on the record. The center's summary counted 15 ‘scheduled’ visits: your real 12, plus 3 make-up slots it logged but never gave you dates for — and it folded its own 3 staffing cancellations into your column as visits not attended. Against that, your attached table set the four true numbers side by side, every row sourced: 12 scheduled, 3 cancelled by the center, 9 held, 9 attended — nine of nine. The confirmations were the center's own replies; the cancellation answers were dated the days the calls came in; the log lines were quoted from the record you requested. At the review, the attendance finding was corrected on the record to the table's arithmetic, and the three lost visits were ordered made up, with dates this time. The plan's language going forward describes a parent who attended every visit that was held.
- THE LAW UNDER THIS PATH (kept to this scenario's verified set): The paper that decided this ending was obtained the way this series always obtains it: the case record — including the attendance summary and the scheduling log behind it — ‘shall be released upon request’ (55 Pa. Code § 3130.44(d)), requested in writing by a party whose counsel (42 Pa.C.S. § 6337) then built the correction out of the agency's own lines. No new right was invented here; arithmetic is not a legal doctrine. Say plainly what was won: Felix is still placed, visits still run Tuesdays and Saturdays at the center, and no order today ends this case. What changed is the finding every future summary will quote — and the three make-up visits, ordered with dates, are real hours with your son that the old number would never have produced.
- THE HONEST PART: A center with fuller staffing never cancels, and none of this is necessary; a different reviewer could have noted the table and kept the percentage anyway, on the theory that summaries are entitled to their conventions — some do. Ms. Kessler's memory, the agency's report habits, the reviewer, and luck all hold pieces of this outcome. This ending is not a verdict on you as a mother: you attended every held visit on every path through this scenario, including the worst one. What your choices changed is whether the file could prove it — whether ‘reliable,’ said kindly at a desk in August, would still exist in October, in the only form October reads. It did, because you wrote it down, three different ways, all summer.

## [end_makeups] Ending — Make-Ups, Eventually
*Day 66 — Thursday, October 8, 2026 — Thursday, October 8, 2026 (dayOffset 66)*

**Ending.**

**Debrief:**
- WHAT THE FILE HELD (the hidden record, revealed): A partial correction. The review credited what was in front of it — your dated cancellation answers, or your account, believed — enough to order the lost visits made up, this time with dates attached to the order. What it did not do is reopen the arithmetic: the ‘60%’ line stands in the findings, uncorrected, because the full correction needed the whole apparatus — written confirmations for every visit, the center's own summary and log obtained on request, and a corrected table attached to the packet — and some layer of that apparatus was missing. So the file now holds both: real make-up visits, ordered and dated, and a percentage that still describes a mother who missed visits she was never allowed to attend. Future summaries will quote the number, not the bus ride.
- THE LAW UNDER THIS PATH (kept to this scenario's verified set): The make-ups were won with the tools this path used — a written trail, presented by counsel (42 Pa.C.S. § 6337). The correction that didn't happen was available through the unused or unfinished ones: the record behind the percentage ‘shall be released upon request’ (55 Pa. Code § 3130.44(d)), and a percentage, being a document, can only be corrected by another document — the four-column table, built from the provider's own log, attached before the hearing. Note the asymmetry this ending teaches, because it generalizes: remedies a room can grant out of fairness (dates for make-ups) move on stories and partial paper; findings, once written, move only on complete paper. You got the remedy. The finding kept the number.
- THE HONEST PART: Do not let the standing percentage obscure the real hours: three visits, restored with dates, are three afternoons with Felix that September had simply deleted, and plenty of parents leave this room with neither the dates nor the correction. A different reviewer might have corrected the number on the partial trail, or refused the make-ups on the full one — reviewers differ, centers differ, and the same summer, faithfully kept, lands differently in different rooms. Your attendance was never the variable in this scenario; on every path you attended every held visit. The variable was the denominator's ownership. Next review, the table can still be built — the log still exists, and a request can still be sent. Paper keeps. That is its whole virtue.

## [end_poor] Ending — Attendance: Poor
*Day 66 — Thursday, October 8, 2026 — Thursday, October 8, 2026 (dayOffset 66)*

**Ending.**

**Debrief:**
- WHAT THE FILE HELD (the hidden record, revealed): One number, hardened. ‘Family attended 60% of scheduled visits’ was read at the review, met by no table, no log, and no dated trail, and was adopted into the plan's findings in the natural way of unopposed sentences: by quotation. The findings do not say the center cancelled three visits for staffing. They do not say make-up slots were logged that you were never told about. They say a percentage, and the percentage now has an owner, grammatically and permanently: the family. Which is to say, you. The next summary will quote the findings, the way this one quoted the summary, the way the summary quoted a count nobody ever showed you.
- THE LAW UNDER THIS PATH (kept to this scenario's verified set): Nothing in this ending was decided against you after a contest of records, because there was only one record in the room. The instruments all existed: confirmations and cancellation answers could have been made in writing, at no cost, the day each event happened; the attendance summary and scheduling log behind the percentage were yours on written request — they ‘shall be released upon request’ (55 Pa. Code § 3130.44(d)); and counsel (42 Pa.C.S. § 6337) was there to build the four-column table and attach it. All of that remains available for the next review — the log still exists, the request can still be sent, and a finding, however hardened, can still be answered by the paper it was computed from. It will simply have to be answered uphill, against a finding instead of a draft.
- THE HONEST PART: Let this debrief be as fair as the finding wasn't: you attended every visit that was ever held — nine of nine, all summer, including the Saturday you rode a bus halfway across town to a cancellation. The center cancelled; the summary folded; the finding hardened. At no point did anyone in the chain need to intend any of it, which is precisely the system's most dangerous property: it can misdescribe a reliable parent as a poor attendee using nothing but phone calls, a busy desk, and arithmetic nobody checked. A fuller-staffed center, a supervisor who logged cancellations in the provider's own column, a reviewer who asked for the denominator — any of those lucks changes this ending without you changing at all. Outcomes here turn on staffing, habits, and luck. Your share, next time, is the unglamorous trio: confirm in writing, answer in writing, and bring the count — because in this system, attendance you cannot prove is attendance that, on paper, did not happen.
