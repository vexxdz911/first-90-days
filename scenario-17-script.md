# THE FIRST 90 DAYS — Scenario 17: “The Empty Apartment”

*Human-readable script. This document and `scenario-17.json` are generated from a single source and match node-for-node: same IDs, same order, same choices, same effects.*

**The family is fictional — a composite. No real person's story appears here.** Built only from published public-record opinions (see report): names, ages, county, occupations, and facts altered and merged.

**Content note:** This scenario depicts a home inspection, repairs, and a lease deadline during a reunification transition. There is no graphic content and no in-story removal — the child's placement predates the story. Players may skip any scene or use the quick exit at any time.

**How to read effects:** `cash −40` changes the player's cash. `FLAG: name` sets a flag the engine tracks. `HIDDEN + item` means the case file quietly records that item at this choice — the player does not see it when it happens. `NOTE:` is text shown to the player right after choosing.

Start date: Monday, January 5, 2026. Day offsets are days since the scenario's start date. The lease hold expires Wednesday, February 4, 2026 (day 30) — a landlord's deadline, not a statutory clock.

## [start] The Approved Plan and the Empty Rooms
*Day 0 — Monday, January 5, 2026 — Monday, January 5, 2026 (dayOffset 0)*

You are Dana Ellis, thirty-one, a home-health aide working early shifts across three clients' houses, and for eleven months your son Eli, seven, has lived with a foster family twenty minutes away. His placement predates this story — nothing in these thirty days removes him; these thirty days are about whether he comes home.

Last week the message you have been working toward finally came, in the plain language these messages use: reunification is approved in principle. One condition remains before Eli can move in — the new apartment you have just leased must pass the agency's home inspection. The rooms are empty. The lease is signed. Your folder says you have done everything else that was asked.

One clock matters this month, and it is important to be exact about what kind of clock it is: the landlord is holding the apartment and your move-in window only until Wednesday, February 4, 2026. That date comes from the lease hold — a landlord's deadline, a practical and contractual one. It is not a statute, not a court deadline, and no law sets it. If the apartment is not cleared and occupied by then, the landlord may release it to the next applicant — unless the landlord agrees, in writing, to extend the hold.

**Choices:**
- Take the inspection exactly as scheduled, folder in hand, and write down everything that is said → **inspection_day**
  - NOTE (shown after choosing): Approved in principle is real progress. It is also conditional — and conditions are cleared on paper, not on hope.

## [inspection_day] The Inspection
*Day 2 — Wednesday, January 7, 2026 — Wednesday, January 7, 2026 (dayOffset 2)*

The inspector, Ms. Okafor, is methodical and not unkind. She runs the taps, checks the windows, tests each room in turn, and writes as she goes — which you have learned, in eleven months, is what everyone in this system does.

The apartment does not pass. Four findings, read aloud at the kitchen counter: no smoke-and-carbon-monoxide detector in the hallway; the bathroom window latch is broken; two outlets in Eli's room have no covers; and the hot water runs lukewarm and never truly hot. 'All fixable,' she says. 'None of it is the structure. But I can only clear what I can verify, and I verify what I can see.'

Eli's transition visits — the longer afternoons, then an overnight — are penciled in around your work schedule for the last week of January. They depend on this apartment clearing. So does February 4.

**Choices:**
- Ask, before she leaves, exactly how each fix will be verified — and what proof she will accept → **the_list**
  - NOTE (shown after choosing): The most useful question in any inspection: not just what failed, but what 'fixed' will look like to the person checking.
- Nod, thank her, and rely on remembering the four items → **the_list**
  - NOTE (shown after choosing): Four items, remembered, feel manageable tonight. Memory, though, is the one record nobody else can read.

## [the_list] Get It in Writing
*Day 3 — Thursday, January 8, 2026 — Thursday, January 8, 2026 (dayOffset 3)*

At the agency office the next morning, the front desk prints the inspection summary: four items, dated, with the apartment's address at the top. Seeing them in type changes them. Aloud, they were a discouraging afternoon. On paper, they are a checklist — and checklists can be finished.

The summary separates the items without quite saying so: the detector, the latch, and the outlet covers are things you can buy and fit yourself. The hot water is different — the heater belongs to the building, and the building belongs to the landlord. Two kinds of fix, two different people responsible, one deadline.

Your caseworker, Mr. Bell, is out until Monday. The summary is what you have. It is, you realize, enough to start.

**Choices:**
- Tape the printed summary inside your folder and work from it, item by item → **records_request**  _(FLAG: hasWrittenList; HIDDEN + Inspection summary — four dated items: detector, latch, outlet covers, hot water)_
  - NOTE (shown after choosing): A dated list is a promise you can point to — for the inspector, the landlord, and yourself.
- Work from memory and goodwill, and save the folder for court papers → **records_request**
  - NOTE (shown after choosing): The folder stays thin a while longer. Goodwill does a lot in this story; it just cannot be attached to an email.

## [records_request] Ask for the Record
*Day 4 — Friday, January 9, 2026 — Friday, January 9, 2026 (dayOffset 4)*

Your support-group friend, a mother a year further along than you, gives you the advice she gives everyone: 'Ask for the file. Ask in writing. You are allowed.' She is right about the mechanism, in the plain terms the regulation uses: the case record shall be released upon request (55 Pa. Code § 3130.44(d)).

What you want is specific: the inspection material — today's summary and any notes behind it — and the current service-plan pages that describe the housing condition and the planned transition. If a disagreement ever comes, you want to be arguing from the same pages the agency is reading, not from your memory of a hallway conversation.

The request can be a short letter or an email. What matters is that it is written, dated, and kept — a copy in the folder, next to the inspection summary.

**Choices:**
- Send the written request today, naming the inspection material and the service-plan pages, and keep your dated copy → **landlord_clock**  _(FLAG: recordsRequested; HIDDEN + Written record request — inspection material and service-plan pages requested under 55 Pa. Code § 3130.44(d))_
  - NOTE (shown after choosing): Requested, in writing, with a copy kept. However long the packet takes, the asking is now part of the record.
- Ask Mr. Bell verbally when he is back on Monday instead → **landlord_clock**
  - NOTE (shown after choosing): A verbal ask may work — Mr. Bell is decent. But nothing about it can be shown later, dated, or attached.

## [landlord_clock] The Landlord's Clock
*Day 5 — Saturday, January 10, 2026 — Saturday, January 10, 2026 (dayOffset 5)*

The landlord, Mr. Petrocelli, manages six units and a hardware store, and answers his phone on the second ring. You tell him the truth in one sentence: the apartment is right, the inspection found four fixable things, and you need the month the lease hold already gives you.

He is blunt in return, and the bluntness is useful: 'The hold is the hold. February fourth. After that I've got a waitlist, and I can't carry an empty unit on a promise. You need more time, you get it from me in writing — same as I'd need from you.' No statute makes him say this and no statute stops him. This is the lease-hold deadline again: practical, contractual, negotiable only on paper.

You write February 4 on the folder in marker. Day 30. Everything this month is arithmetic against that square on the calendar — and against your shifts, and against Eli's transition visits, which cannot move into an apartment that has not cleared.

**Choices:**
- Thank him, and treat February 4 as fixed unless a written extension exists → **triage**
  - NOTE (shown after choosing): A deadline you respect early is a deadline you can still negotiate. A deadline you discover late negotiates you.

## [triage] Two Kinds of Fix
*Day 6 — Sunday, January 11, 2026 — Sunday, January 11, 2026 (dayOffset 6)*

Sunday, at the kitchen table in your current room — the small rented room Eli cannot live in, the reason for all of this — you sort the four items the way the summary sorted them.

Yours: a hallway detector, a window latch, outlet covers. A hardware-store trip and a free afternoon. The landlord's: the water heater, which you may not touch — it is his equipment, in his locked utility closet, and fixing it yourself could cost you the deposit and the lease. The skill this month is not handiness. It is sending each problem to the person who owns it, in a form that person cannot later say they never received.

You have $260. The detector and parts will take some of it. February's first check is spoken for twice over already.

**Choices:**
- Split the list in writing: your three items to buy, the hot water to the landlord in writing → **hardware_run**  _(FLAG: splitList)_
  - NOTE (shown after choosing): Two lists, two owners, no item floating between 'somebody should.' Floating items are where deadlines go to die.
- Try to do all four yourself to save time, including coaxing the water heater → **hardware_run**
  - NOTE (shown after choosing): Faster-feeling, riskier in fact: the heater is the landlord's equipment, and an amateur repair can become a lease problem of its own.

## [hardware_run] The Hardware Store
*Day 7 — Monday, January 12, 2026 — Monday, January 12, 2026 (dayOffset 7)*

Mr. Petrocelli's own store, as it happens — he sells you the detector, the latch, and a bag of outlet covers, and throws in the batteries. The register receipt is long and itemized. Standing at the counter, you have a choice that eleven months in this system has taught you to notice: a receipt is not clutter. A receipt is a date that proves itself.

Fitting them takes the afternoon. Detector up, tested, beeping satisfyingly. Latch replaced. Covers in, all through Eli's room and, while you are at it, the living room too. Three of the four items, done in a day — by the person who owned them.

**Choices:**
- Photograph each finished fix, keep the itemized receipt, and file both the same night → **hot_water_letter**  _(cash −38; FLAG: boughtSupplies; HIDDEN + Receipt — detector, latch, outlet covers (dated, itemized); HIDDEN + Dated photos — detector fitted and tested; latch replaced; outlet covers in place)_
  - NOTE (shown after choosing): Bought, fitted, photographed, filed — in one day. This is what 'fixed' looks like when it can travel without you.
- Fit them, enjoy the beep, and toss the receipt in the glove box → **hot_water_letter**  _(cash −38; FLAG: boughtSupplies)_
  - NOTE (shown after choosing): The fixes are real either way. The proof of when they happened is now in a glove box, keeping company with napkins.

## [hot_water_letter] The Hot Water Is Not Yours to Fix
*Day 8 — Tuesday, January 13, 2026 — Tuesday, January 13, 2026 (dayOffset 8)*

The fourth item waits on the one person who can authorize it. You need the landlord to send his plumber to the water heater — and you need the request to exist somewhere other than in his memory of a phone call.

A short written request does three jobs at once: it tells him the inspection item in the inspector's words, it gives him the deadline honestly — reinspection must happen before the February 4 hold expires — and it creates the dated proof that he was told, early, while there was still time for him to act. People respond to paper differently. Paper has a date, and dates create responsibility.

**Choices:**
- Send the hot-water request in writing today, quoting the inspection item and the February 4 hold date → **shift_trade**  _(FLAG: landlordWritten; HIDDEN + Written request to landlord — water-heater repair quoted from inspection summary, February 4 hold date stated)_
  - NOTE (shown after choosing): Written, dated, specific. If the plumber is slow now, the slowness will have an author — and it will not be you.
- Catch him at the store counter and ask him face-to-face instead → **shift_trade**
  - NOTE (shown after choosing): He will probably say yes warmly, at the counter, to your face. Warm yeses at counters have a way of evaporating by Thursday.

## [shift_trade] Shifts Against the Calendar
*Day 9 — Wednesday, January 14, 2026 — Wednesday, January 14, 2026 (dayOffset 9)*

Your supervisor posts the late-January rota, and it collides with everything: the plumber can only come on a weekday morning, the agency does reinspections on weekday mornings, and Eli's first extended transition afternoon is set for a Friday you are scheduled to work. Your clients — three elderly people who plan their weeks around you — are the third pressure in this story, and they are real too.

An extra weekend shift is on offer. It pays, and the money would refill what the hardware store took. It also takes the only free Saturday between now and the reinspection. Money and time are the same resource this month, wearing two coats.

**Choices:**
- Take the extra shift, and protect one weekday morning for the plumber and the reinspection → **dated_photos**  _(cash +60)_
  - NOTE (shown after choosing): Money restored, mornings protected. The calendar, for once, was negotiated before it collided.
- Decline the extra shift and keep every hour free for the apartment → **dated_photos**
  - NOTE (shown after choosing): Time protected, money tighter. February was already going to be close; now it is closer.

## [dated_photos] Photographs With Dates
*Day 10 — Thursday, January 15, 2026 — Thursday, January 15, 2026 (dayOffset 10)*

A photograph without a date is a claim. A photograph with a date — the phone's timestamp kept, the day's newspaper or the inspection summary in frame for one shot, the sequence showing before and after — is evidence that can be sent, printed, and believed by someone who was never in the room.

You walk the apartment slowly, the way Ms. Okafor walked it: detector, latch, every covered outlet, the tap running while the thermometer you borrowed reads the water — still lukewarm, and the photograph of that matters too. Documenting the item you have not fixed, honestly, with its date, is not an admission against yourself. It is proof of the one thing you most need believed later: that the remaining item was never yours, was requested early, and was still waiting on the day the photo was taken.

**Choices:**
- Build the dated photo set — yours fixed, the hot water honestly still waiting — and back it up in two places → **visit_planning**  _(FLAG: datedPhotos; HIDDEN + Dated photo set — three items verified complete; hot water documented as still lukewarm on this date)_
  - NOTE (shown after choosing): Before, after, and honestly-in-between. A file like this answers questions you will not be in the room to hear asked.
- Snap two quick pictures for your own memory and move on → **visit_planning**
  - NOTE (shown after choosing): Two undated pictures will remind you. Reminding you was never the problem the file has.

## [visit_planning] The Transition That Depends on a Tap
*Day 11 — Friday, January 16, 2026 — Friday, January 16, 2026 (dayOffset 11)*

Eli's transition plan is a staircase, drawn on the service-plan page you have read so often you could recite it: longer afternoon visits at the apartment, then dinner, then — once the apartment clears — an overnight, then the move. Staircases need a building. Every step after the first afternoon assumes a cleared apartment.

At today's visit, in the foster family's kitchen, Eli asks whether his room in the new place has 'the blue wall.' It does — you painted it in December, before the lease was even countersigned, because hope in this system is also a form of preparation. His foster mother, Mrs. Lindqvist, packs his drawing folder and says the thing foster parents say when they mean it as kindness and warning both: 'He's counting the afternoons, Dana. So am I.'

You do not promise Eli a date. You promise him the order of things: inspection, fixes, the inspector comes back, then the overnight. Children can hold an order. It is unexplained waiting that leaks.

**Choices:**
- Tell Mr. Bell the transition staircase in writing, asking which steps can proceed before the reinspection → **receipt_folder**  _(HIDDEN + Visit note — transition staircase explained to child in order, without a promised date)_
  - NOTE (shown after choosing): The plan, in writing, with the dependency named plainly: these steps wait on a cleared apartment. No one can later call that a surprise.
- Keep the visits warm and informal, and let the schedule sort itself out → **receipt_folder**
  - NOTE (shown after choosing): Warmth is not the risk here. Untracked dependencies are — a staircase nobody wrote down can be missed without anyone deciding to miss it.

## [receipt_folder] The Folder Learns to Travel
*Day 12 — Saturday, January 17, 2026 — Saturday, January 17, 2026 (dayOffset 12)*

Saturday is folder day, and folder day is unglamorous in the way load-bearing things are unglamorous. Inspection summary. Detector receipt. Latch receipt. Photo printouts from the library printer, each labeled underneath in pen: what, where, which day. The written hot-water request, with its date. The record request you sent, with its date.

The test you apply to every page is the test this whole scenario runs on: could this page do its job in a room you are not in? A page that needs you standing beside it explaining is a story. A page that speaks alone — dated, specific, in order — is a record. Reinspections, supervisors, and landlords who need convincing are all rooms you may not be in.

Copies cost money. So does everything. The library printer takes coins and produces the cheapest insurance in this entire case.

**Choices:**
- Assemble the full folder — summary, receipts, labeled photos, both written requests — and print a copy set → **reinspect_request**  _(cash −12; FLAG: folderComplete; HIDDEN + Repair folder assembled — inspection summary, dated receipts, labeled photos, written requests, in order)_
  - NOTE (shown after choosing): One folder, in order, that can travel without you. Whatever February decides, this already exists.
- Keep the originals safe at home and carry the details in your head to appointments → **reinspect_request**
  - NOTE (shown after choosing): Your head is an excellent witness and a terrible filing system: it cannot be copied, attached, or left with a receptionist.

## [reinspect_request] Ask for the Reinspection — in Writing
*Day 13 — Sunday, January 18, 2026 — Sunday, January 18, 2026 (dayOffset 13)*

Sunday. Three items are fixed and documented. The hot water is requested, in writing, and waiting on the landlord's plumber. The reinspection cannot pass until the heater is done — but the request for the reinspection can be made now, and how it is made decides what happens if anything slips.

A written reinspection request — dated, listing each item and its fix, naming the February 4 lease-hold date plainly as the landlord's deadline it is — does two things a phone call cannot. It puts you in the agency's queue with a timestamp, and it warns everyone, on paper and in advance, that a lease, not just a checklist, is riding on the date they choose. Systems respond to what is written in them. That is their flaw and, this month, possibly your leverage.

**Choices:**
- Send the written reinspection request today — items, fixes, and the February 4 hold date stated — and file your copy → **prep_thorough**  _(FLAG: reinspectWritten; HIDDEN + Written reinspection request — each item and fix listed; February 4 lease-hold date stated in advance)_
  - NOTE (shown after choosing): Requested in writing, with the deadline named before it could become an emergency anyone claims not to have seen.
- Phone the office Monday and ask for the soonest slot → **prep_thin**
  - NOTE (shown after choosing): A call may get a slot. It leaves nothing behind it — no list, no warning about February 4, no date anyone must answer for.

## [prep_thorough] The Paper Goes First
*Day 14 — Monday, January 19, 2026 — Monday, January 19, 2026 (dayOffset 14)*

Your written request travels the way paper travels: it is logged, it is forwarded, and on Monday it reaches Ms. Okafor herself, who calls you — not the other way around. 'You've listed the heater as outstanding, with the landlord's request dated last week,' she says. 'That's how to send these. I'll hold a morning slot the day after the plumber confirms. Send me the dated photos of the three you've done, and I'll note them as seen.'

Nothing is waived. The apartment still must pass, in person, all four items. But the queue now has your date in it, the file has your photos in it, and the last item's delay has a name on it that is not yours. Paper does not fix water heaters. It fixes something almost as important: who is waiting on whom, according to the record.

**Choices:**
- Send the dated photos the same day, and confirm the held slot in a reply that creates one more dated page → **plumber_day**  _(HIDDEN + Agency note — reinspection slot held pending plumber confirmation; dated photos received and noted)_
  - NOTE (shown after choosing): Slot held, photos filed, reply dated. The record of this week will read: parent early, parent documented, system scheduling.

## [prep_thin] The Phone Call
*Day 14 — Monday, January 19, 2026 — Monday, January 19, 2026 (dayOffset 14)*

Monday's call reaches a voicemail, then a callback, then a kind staffer who is not Ms. Okafor and who offers 'sometime next week, we'll confirm.' You describe the four items from memory. February 4 is mentioned — you think you mentioned it; the call was short, and the radiator in your room was hissing, and afterward you cannot honestly say whether the date landed.

No slot is held. No list changes hands. None of this is anyone's bad faith — it is simply what a phone call is: sound, then memory, then nothing. The plumber is now the easy part. The hard part is that if next week slides, there will be no dated page anywhere showing you asked when asking could still have changed the answer.

**Choices:**
- Call again tomorrow, and the day after — persistence will have to do the work paper would have done → **plumber_day**
  - NOTE (shown after choosing): Persistence is real effort, and it may yet land the slot. It just leaves no footprints anyone can follow later.

## [plumber_day] The Plumber's Morning
*Day 15 — Tuesday, January 20, 2026 — Tuesday, January 20, 2026 (dayOffset 15)*

The plumber — sent by Mr. Petrocelli, after your written request, on the morning you protected from the rota — spends forty minutes in the utility closet and emerges with the diagnosis and the cure in one sentence each: 'Element's burned out. Swapping it today.'

By noon the tap runs genuinely, steamingly hot. You run it three times, like a person checking a locked door, and then you do the unglamorous, decisive thing: you photograph the running tap with the borrowed thermometer in frame, note the plumber's visit on the folder's cover sheet with its date, and keep the plumber's invoice copy he leaves on the counter — his paperwork, with your address and today's date, saying in a tradesman's hand exactly what was replaced.

Four items. All four, now, are facts. What remains is getting those facts verified, in the right room, before a landlord's calendar runs out.

**Choices:**
- Send the dated hot-water photo and the plumber's invoice copy to the agency the same afternoon, in writing → **worker_check**  _(FLAG: hotWaterDone; HIDDEN + Plumber invoice copy — heating element replaced, dated, at the apartment address; HIDDEN + Dated photo — hot water running at temperature after repair)_
  - NOTE (shown after choosing): Same-day, in writing, with a tradesman's invoice doing the talking. Verification now has everything it needs except a date.
- Wait and show the inspector everything at the reinspection itself → **worker_check**  _(FLAG: hotWaterDone)_
  - NOTE (shown after choosing): All true, all provable — eventually, in the room. If the room's date slips, 'eventually' is where February 4 lives.

## [worker_check] A Visit That Is Not an Inspection
*Day 17 — Thursday, January 22, 2026 — Thursday, January 22, 2026 (dayOffset 17)*

Mr. Bell, back from leave, visits Thursday — not an inspection, he says at the door, just a check-in before the reinspection. He walks the rooms anyway, the way everyone in this system walks rooms. Detector: beeps. Latch: catches. Outlets: covered. Tap: hot, held under it long enough to nod.

'For what it's worth,' he says, making a note, 'this is what the file is supposed to look like at this stage. Everything dated. I can see what was done, when, and who did the heater.' Worth is a doing word in this building: his note goes in the record either way. What it says depends entirely on what he was able to see — and on whether what he saw was paper, or just a tidy apartment and your account of it.

**Choices:**
- Walk him through the folder page by page, so his note can name dates and documents, not impressions → **extension_talk**  _(HIDDEN + Caseworker note — apartment observed; repair folder reviewed with dated receipts, photos, and written requests)_
  - NOTE (shown after choosing): His note now cites documents. Impressions fade from files; citations get quoted.
- Let the tidy apartment speak for itself — it does look ready → **extension_talk**
  - NOTE (shown after choosing): It does look ready. His note will say so, in the soft vocabulary of impressions, which hardens into nothing quotable.

## [extension_talk] Insurance, in Writing
*Day 18 — Friday, January 23, 2026 — Friday, January 23, 2026 (dayOffset 18)*

Friday, a week and a half from the deadline, you do the thing that separates a hope from a plan: you ask Mr. Petrocelli — before you need it — whether he would extend the hold by two weeks if the reinspection slips for reasons outside your control, and you ask him to put any yes in writing.

He considers you the way landlords consider things, through the ledger. 'You're paid up, you fixed your three in a day, and my plumber says you were right about the element,' he says. 'If it comes to it — in writing, two weeks, small fee to hold it, because an empty unit costs me too. But understand: if February fourth passes with nothing signed, I have to release it. That's not me being hard. That's the waitlist.'

Nothing is signed today. What exists is a named price, a named term, and a landlord who has said the words out loud once — which makes signing them later a smaller step than asking cold on February 3.

**Choices:**
- Get the offered terms noted in a short written message today, so the extension is a signature away if needed → **money_crunch**  _(FLAG: extensionPriced)_
  - NOTE (shown after choosing): Terms named, price named, in writing. An extension you have pre-negotiated is insurance; one you beg for on deadline day is a coin toss.
- Trust that the reinspection will land in time, and leave the extension unasked until needed → **money_crunch**
  - NOTE (shown after choosing): It may land in time. If it doesn't, February 3 is a very late day to learn a landlord's price.

## [money_crunch] February Is Already Spoken For
*Day 19 — Saturday, January 24, 2026 — Saturday, January 24, 2026 (dayOffset 19)*

Saturday's arithmetic is the month's second pressure, and it does not care about your folder: February rent on the new apartment, the last month on the rented room overlapping it, Eli's winter boots giving out at the seams, and a hold-extension fee — if it comes to that — priced in a message you may or may not be holding.

Mrs. Lindqvist texts a photograph of Eli asleep under a blanket fort, one arm around the drawing of the blue wall. The transition afternoons have gone the way good afternoons go: unremarkably, which in a seven-year-old's life is the highest grade there is. The overnight is the step that waits. It waits on a verification, which waits on a date, which waits — as so much does — on other people's calendars.

**Choices:**
- Set aside the extension fee in an envelope marked with its purpose, and let the boots be the cheaper pair → **records_arrive**  _(cash −45; FLAG: feeReserved)_
  - NOTE (shown after choosing): An envelope with a purpose is a plan that survives a bad week. The boots will be outgrown before their quality is judged.
- Spend February as it comes — the reinspection will surely settle everything first → **records_arrive**
  - NOTE (shown after choosing): It may. 'Surely' has carried a lot of months in this system. It has also dropped a few.

## [records_arrive] The Record Answers
*Day 20 — Sunday, January 25, 2026 — Sunday, January 25, 2026 (dayOffset 20)*

Sunday, the packet from your written request arrives — the one you sent under 55 Pa. Code § 3130.44(d), which is to say: the file, answering because you asked it to, in writing. Inspection summary, the inspector's working notes, the service-plan pages. You read your own month in the system's handwriting.

Two things matter in it. First, the service-plan page states the housing condition exactly as you understood it: apartment to pass inspection, transition steps to follow clearance. No hidden condition ambushes you. Second, the inspector's notes are fair — 'parent responsive; items minor and remediable' — and now you hold them, which means at the reinspection, and anywhere after, everyone is arguing from the same pages. That sameness is the quiet superpower of a record request: it does not change the file. It changes who gets to read it before decisions are made.

If you never sent the written request, this Sunday looks different — you prepare from memory and hope, and the notes exist anyway, in a file you simply have not seen. The file is always being written. The only question this scenario ever asks is whether you are one of its authors.

**Choices:**
- Read the packet against your folder, page by page, and note any mismatch while there is still time to answer it → **packet_night**  _(HIDDEN + Record packet received and reviewed — inspection notes and service-plan housing condition match folder account)_
  - NOTE (shown after choosing): Same pages, both sides of the desk. Surprises at a reinspection almost always turn out to be pages one side never read.

## [packet_night] The Night Before Verification
*Day 21 — Monday, January 26, 2026 — Monday, January 26, 2026 (dayOffset 21)*

Monday night, the folder gets its final order: inspection summary first, then each item's proof in the order the inspector will check them — detector receipt and photo, latch receipt and photo, covers photo, plumber's invoice and the hot-water photograph, and behind them the written trail: your hot-water request, your reinspection request, your record request, each dated, each early.

This is the whole curriculum of The Empty Apartment, bound in one folder: in a system that decides from records, the parent who creates the record — dated photographs, kept receipts, requests made in writing with copies kept — is not being bureaucratic. She is being legible. Legibility is what lets a busy inspector verify quickly, a supervisor approve confidently, and a landlord believe a delay was not neglect.

Tomorrow Ms. Okafor returns. What she finds will be four fixed items. What she can do with what she finds depends on how fast she can verify them — and verification speed, tomorrow, is a paper quality, not a plumbing one.

**Choices:**
- Lay out the folder in the inspector's own order, and sleep → **reinspection_day**
  - NOTE (shown after choosing): In her order, not yours. Tomorrow is her checklist's day; your job is to make each check take ten seconds.

## [reinspection_day] The Reinspection
*Day 22 — Tuesday, January 27, 2026 — Tuesday, January 27, 2026 (dayOffset 22)*

Tuesday morning, Ms. Okafor walks the apartment a second time, folder under her arm — your folder, or your account of it, depending on the month you have had. Detector: tested, beeps, checked against the receipt's date. Latch: worked twice. Outlets: every one. The tap runs while she watches, and the steam does what steam does — it testifies.

She writes for a long time at the kitchen counter. How this morning ends is not decided by the fixes alone — the fixes, remember, were always fixable. It is decided by verification: how completely, quickly, and credibly each item can be confirmed from what is in front of her, in the time a working morning allows, against a landlord's deadline that is now eight days away and was never a court's deadline at all.

**Choices:**
- Walk her item by item with the folder open — each fix matched to its dated photo, receipt, or invoice, in her order → **result_pass**  _(FLAG: verifiedClean)_
  - NOTE (shown after choosing): Item, photo, receipt. Item, photo, receipt. Verification at the speed of paper.
- Let her re-check the rooms while the folder waits in the other room, answering from memory as she calls out items → **result_partial**
  - NOTE (shown after choosing): Everything she asks about is fixed. Everything she asks for, though, is in the other room, or in a glove box, or in a conversation only you remember.

## [result_pass] Cleared
*Day 23 — Wednesday, January 28, 2026 — Wednesday, January 28, 2026 (dayOffset 23)*

By the third item, Ms. Okafor's pen has changed tempo — the shorthand of a person whose checklist is agreeing with the paper in front of her. The hot water she saves for last, runs longest, and closes with a sentence you will remember longer than most sentences this year: 'Verified. All four items. The apartment passes.'

She signs the clearance at the counter, dates it, and gives you your copy — because you ask for your copy, at the counter, the way eleven months has taught you to ask. The transition staircase can now be climbed on its real schedule: the overnight this weekend, in the blue-walled room, and the move inside the lease hold, with eight days to spare.

What cleared today was an apartment. What made the clearing take twenty minutes instead of another month was a folder.

**Choices:**
- Send the signed clearance copy to Mr. Bell and to the landlord today, in writing, and confirm the overnight → **movein_prep**  _(HIDDEN + Reinspection clearance — all four items verified and signed, dated copy to parent)_
  - NOTE (shown after choosing): Cleared, copied, sent. The two people whose calendars depended on this morning now hold the same dated page.

## [result_partial] Verified — Except for the Paper
*Day 23 — Wednesday, January 28, 2026 — Wednesday, January 28, 2026 (dayOffset 23)*

The apartment, item by item, is fixed — Ms. Okafor can see that, and says so. What she cannot do, this morning, is verify all of it to the standard her form requires: a receipt she has not seen, a repair date she cannot confirm, a history of the heater fix that exists as your account rather than as an invoice in her hand. 'I believe you,' she says, and means it, and it changes nothing. 'Belief isn't a box on this form. I have to hold the clearance until the documentation reaches me and I can sign against it.'

Held is not denied. The fixes stand; the verification waits on paper catching up with plumbing. But held runs on a clock, and the clock is Mr. Petrocelli's: February 4, eight days away, with the clearance unsigned. The apartment is ready. The record is not. This month, that was always the race.

**Choices:**
- Ask her to list, in writing, exactly which documents she still needs — then go home and race the list → **landlord_answer**  _(HIDDEN + Reinspection held — items observed fixed; clearance unsigned pending documentation)_
  - NOTE (shown after choosing): A written list of what's missing, again. Even now, especially now, the list is the way through — if the lease survives the gathering.

## [movein_prep] Boxes in a Cleared Apartment
*Day 25 — Friday, January 30, 2026 — Friday, January 30, 2026 (dayOffset 25)*

Thursday is boxes — yours, and Eli's things arriving in Mrs. Lindqvist's careful installments: the drawing folder, the blanket-fort blanket, a dinosaur with one ear. Moving into an apartment that has already passed is a different species of errand from everything this month: nobody's permission is pending. There is only furniture, and a boy's room turning from blue paint into a life.

Mr. Petrocelli, given his signed clearance copy, does the landlord equivalent of applauding: he hands over the second set of keys and waives the last of the hold paperwork. 'Told you it was a good unit,' he says, as if the unit had done it.

**Choices:**
- Set up Eli's room first — bed, drawings, dinosaur — before a single kitchen box is opened → **transition_weekend**
  - NOTE (shown after choosing): His room first. In eleven months of systems, that ordering was the one rule that never needed a form.

## [transition_weekend] The Overnight
*Day 27 — Sunday, February 1, 2026 — Sunday, February 1, 2026 (dayOffset 27)*

Saturday, the staircase reaches its step: Eli sleeps in the blue-walled room, in his own bed, under the blanket from the fort, with the hallway detector's small green eye glowing its bureaucratic blessing down the hall. He tests the bathroom latch twice, solemnly, like a tiny inspector, and pronounces it 'the good kind of click.'

In the morning he demands the tap be run so he can watch the steam 'do its job.' It does. Everything in this apartment now does — verified, dated, and signed. The move completes inside the hold, the transition plan completes inside the month, and February 4 arrives as what it was always supposed to be: a moving date, not a cliff.

**Choices:**
- Let February 4 be a moving date → **end_repaired**
  - NOTE (shown after choosing): Cleared, occupied, and home — inside the landlord's window, on a record anyone can read.

## [landlord_answer] February 4, in Writing or Not at All
*Day 25 — Friday, January 30, 2026 — Friday, January 30, 2026 (dayOffset 25)*

While you gather the documents Ms. Okafor listed, the other clock reaches its square on the calendar. Mr. Petrocelli calls — not unkindly, and not flexibly. 'Dana. It's the fourth on Wednesday. I've held it as long as the paper says I have to. What have you got for me?'

Everything now depends on what exists between you and this man in writing. If the extension terms were named, priced, and noted back when asking was cheap, this call is a signature. If February 4 was trusted to take care of itself, this call is an ending — because a landlord with a waitlist cannot extend a hold on the strength of a clearance that is itself still waiting on paper.

**Choices:**
- Sign the pre-negotiated written extension — two weeks, the reserved fee, dates on paper → **end_extended**  _(cash −45; FLAG: extensionSigned)_
  - NOTE (shown after choosing): Two weeks, bought in writing, at the price named in January. The apartment survives its own deadline.
- Ask for more time on the strength of everything that is nearly finished → **end_lost**
  - NOTE (shown after choosing): 'Nearly' is the saddest word in housing. He has a waitlist, a ledger, and no signed page from you. Neither, in the end, do you.

## [end_repaired] Ending — Repairs Verified: Move-In and Reunification Proceed
*Day 30 — Wednesday, February 4, 2026 — Wednesday, February 4, 2026 (dayOffset 30)*

**Ending.**

**Debrief:**
- THE CLOCK, STATED PLAINLY: The deadline that governed this scenario — Wednesday, February 4, 2026 — was the landlord's lease-hold date. It came from a lease, not from a law. No statute set it, no court imposed it, and no agency could extend it; only the landlord could, and only in writing. Naming a deadline's true source matters, in this scenario and outside it, because the remedy depends on it: statutory clocks are answered with filings, while a landlord's clock is answered with a signature — and confusing the two wastes the one resource this family never had enough of, which was time.
- THE PAPER TRAIL IS THE SKILL: Inspectors verify what they can see and sign against what they can document. Caseworkers write notes from what they are shown. Landlords act on what was asked of them in writing, on a date. In every ending of this scenario, the four repairs themselves were identical — the detector, the latch, the covers, the heater element were fixed in all of them. What differed was the record: dated photographs, kept receipts and an invoice, and written requests — for the repair, for the reinspection, and for the case record itself, which the parent may request and which 'shall be released upon request' (55 Pa. Code § 3130.44(d)). The file does not reward effort it cannot see. It rewards evidence it can file.
- WHAT HAPPENED ON THIS PATH: The reinspection verified all four items in one visit, the clearance was signed with a dated copy in the parent's hand, the overnight and the move completed inside the lease hold, and reunification — approved in principle at the start — became actual, on schedule. The roles deserve naming kindly and accurately: the inspector verified; she did not waive. The caseworker noted what the folder let him cite. The landlord kept a hold that was satisfied in time. The parent's share was the record that let each of them do their part quickly.
- THE HONEST PART: This ending required a plumber who came when promised, an inspector with a morning slot, and a landlord whose word held — none of which a folder controls. The same folder, in a month with a broken supply chain or a reassigned caseworker, could have ended in an extension instead. What the documentation guaranteed was not this ending; it was that no delay this month could honestly be recorded as the parent's. In a system that decides from records, that is not a consolation prize. It is the ground every later decision stands on.

## [end_extended] Ending — Lease Preserved by Written Extension; Reunification Delayed
*Day 34 — Sunday, February 8, 2026 — Sunday, February 8, 2026 (dayOffset 34)*

**Ending.**

**Debrief:**
- THE CLOCK, STATED PLAINLY: The deadline that governed this scenario — Wednesday, February 4, 2026 — was the landlord's lease-hold date. It came from a lease, not from a law. No statute set it, no court imposed it, and no agency could extend it; only the landlord could, and only in writing. Naming a deadline's true source matters, in this scenario and outside it, because the remedy depends on it: statutory clocks are answered with filings, while a landlord's clock is answered with a signature — and confusing the two wastes the one resource this family never had enough of, which was time.
- THE PAPER TRAIL IS THE SKILL: Inspectors verify what they can see and sign against what they can document. Caseworkers write notes from what they are shown. Landlords act on what was asked of them in writing, on a date. In every ending of this scenario, the four repairs themselves were identical — the detector, the latch, the covers, the heater element were fixed in all of them. What differed was the record: dated photographs, kept receipts and an invoice, and written requests — for the repair, for the reinspection, and for the case record itself, which the parent may request and which 'shall be released upon request' (55 Pa. Code § 3130.44(d)). The file does not reward effort it cannot see. It rewards evidence it can file.
- WHAT HAPPENED ON THIS PATH: The apartment was fixed but the clearance could not be signed in time, so the lease survived only because the extension had been negotiated early, priced, and then signed in writing before the hold expired. Reunification is delayed — the overnight and the move wait for the documentation to reach the inspector and the clearance to be signed — and the delay is measured in a child's counted afternoons, which no one in this debrief will call small. What the written extension bought was the only thing still buyable: the same apartment, the same blue wall, two more weeks.
- THE HONEST PART: A verbal promise would not have survived February 4, and an extension asked for cold on deadline day usually doesn't either — it survived here because it was a signature completing a January conversation, not a February plea. The system roles stayed in their lanes: the inspector held a standard she could not sign around, the landlord honored exactly what was written, and the transition plan waited, as plans do, on verification. The parent's paper trail was incomplete where it mattered most — at the verification — and strong where it mattered second-most: with the landlord. Both facts are in the file, and both will be read at the next step.

## [end_lost] Ending — Lease Lost; the Documented Record Helps the Next Attempt
*Day 30 — Wednesday, February 4, 2026 — Wednesday, February 4, 2026 (dayOffset 30)*

**Ending.**

**Debrief:**
- THE CLOCK, STATED PLAINLY: The deadline that governed this scenario — Wednesday, February 4, 2026 — was the landlord's lease-hold date. It came from a lease, not from a law. No statute set it, no court imposed it, and no agency could extend it; only the landlord could, and only in writing. Naming a deadline's true source matters, in this scenario and outside it, because the remedy depends on it: statutory clocks are answered with filings, while a landlord's clock is answered with a signature — and confusing the two wastes the one resource this family never had enough of, which was time.
- THE PAPER TRAIL IS THE SKILL: Inspectors verify what they can see and sign against what they can document. Caseworkers write notes from what they are shown. Landlords act on what was asked of them in writing, on a date. In every ending of this scenario, the four repairs themselves were identical — the detector, the latch, the covers, the heater element were fixed in all of them. What differed was the record: dated photographs, kept receipts and an invoice, and written requests — for the repair, for the reinspection, and for the case record itself, which the parent may request and which 'shall be released upon request' (55 Pa. Code § 3130.44(d)). The file does not reward effort it cannot see. It rewards evidence it can file.
- WHAT HAPPENED ON THIS PATH: The hold expired unsigned, the landlord released the apartment to the waitlist — as, on his paper, he was entitled to do — and reunification is deferred while a new housing search begins. That is a real loss, of a specific blue-walled room a seven-year-old had already furnished in his imagination, and this debrief will not dress it as a lesson wearing a costume. The apartment is gone. The month is gone.
- WHAT SURVIVES, AND WHY IT IS NOT NOTHING: The repair record survives the apartment. The folder — inspection summary, dated receipts and photographs, the plumber's invoice, the written requests and their dates, the caseworker's note describing a parent whose documentation was in order — now opens the next housing attempt instead of merely closing this one: a new landlord can be shown a tenant who fixed three items in a day; a new inspection starts from a file that already reads 'responsive; items minor and remediable'; and the record request under 55 Pa. Code § 3130.44(d) means the parent searches with the agency's own pages in hand, arguing from the same record the system reads. Workers rotate, apartments turn over, and judges and hearing officers change — the file is the only participant in this story guaranteed to be present at the next attempt. It now testifies for this parent, in her absence, in rooms she has not yet entered. That is what documentation is for on the months it does not win.
