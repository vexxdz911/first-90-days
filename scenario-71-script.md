# THE FIRST 90 DAYS — Scenario 71: “Four More Weeks”

*Human-readable script. This document and `scenario-71.json` are generated from a single source and match node-for-node: same IDs, same order, same choices, same effects.*

**The family is fictional — a composite. No real person's story appears here.**

**Content note:** This scenario depicts a continuance fight and the weeks that follow it. There is no graphic content. Players may skip any scene or use the quick exit at any time.

**How to read effects:** `cash −40` changes the player's cash. `FLAG: name` sets a flag the engine tracks. `HIDDEN + item` means the case file quietly records that item at this choice — the player does not see it when it happens. `REQUIRES FLAG: name` means the choice is only available if that flag was set earlier; `REQUIRES NO FLAG: name` means it is only available if that flag was never set. `NOTE:` is text shown to the player right after choosing.

Start date: Monday, November 16, 2026. Day offsets are days since the scenario's start date.

## [start] The Four O'Clock Call
*Day 0 — Monday, November 16, 2026 (dayOffset 0)*

Your name is Teresa Garza. Your son Omar is thirteen. Since Monday, September 14, 2026, he has been living with his aunt — safe, fed, in his own school, and counting days in a way he thinks you cannot hear. Tomorrow, Tuesday, November 17, 2026, is his adjudication hearing: the day the court decides whether the agency can prove, from clear and convincing evidence, that Omar is a dependent child. (42 Pa.C.S. § 6341(c))

At four o'clock your lawyer, Ms. Ferreira, calls. The county agency is going to ask the judge to continue the hearing — put it off four weeks, to Tuesday, December 15, 2026. Its caseworker is on leave. The file, its lawyer says, "isn't ready."

"A continuance is the judge's call, not theirs and not ours," Ms. Ferreira says. "Judges grant them and deny them every day. What moves the decision is not outrage. It is the record — who has been diligent, who is ready, and who is hurt by waiting. So tonight we decide what our record is." She also reminds you of a piece of paper that costs almost nothing: the agency's record in Omar's case "shall be released upon request." (55 Pa. Code § 3130.44(d))

**Choices:**
- Ask Ms. Ferreira to file the written request for the full agency record tonight → **omar_night**  _(cash −5 ; FLAG: recordsRequested)_
  - NOTE (shown after choosing): Copies and postage: five dollars. The request is dated today — before the hearing, not after it. Whatever the record holds, your side will be reading it.
- Focus only on tomorrow — the record request can wait until after the hearing → **omar_night**
  - NOTE (shown after choosing): Understandable. Tomorrow feels big enough. But paper filed tonight exists tonight; paper filed later exists later, and hearings notice the difference.

## [omar_night] Omar's Question
*Day 0 — Monday, November 16, 2026 (dayOffset 0)*

That evening you drive Omar's school shoes over to your sister's — he outgrew the pair he left in, which is its own small sentence about how long this has been. Sixty-three days, as of today. He does his homework at her kitchen table. His backpack lives by her door, ready, the way he keeps it ready.

Before you leave he asks it plainly, the way thirteen-year-olds ask the questions adults have been circling: "If the judge says four more weeks — does that mean I did something?"

The honest answer is that a continuance is about calendars and files, not about him. The harder truth underneath it is that four weeks is not the same amount of time to a court as it is to a thirteen-year-old. To the court it is a scheduling entry. To Omar it is a month of his life, spent waiting by a door.

**Choices:**
- Tell him the truth: "It would mean the grown-ups' paperwork isn't ready. It would not mean anything about you." → **morning_prep**  _(cash −10 ; FLAG: omarTold)_
  - NOTE (shown after choosing): Gas for the trip across town. He nods like a person filing something away where he can find it later.
- Tell him not to worry about court things — that is adult business → **morning_prep**
  - NOTE (shown after choosing): He says "okay" in the voice that means he will worry about it privately instead. Children count days whether or not anyone explains the calendar.

## [morning_prep] The Counsel Room, 8:40 A.M.
*Day 1 — Tuesday, November 17, 2026 (dayOffset 1)*

The courthouse smells of radiator heat and old paper. In the small counsel room, Ms. Ferreira lays out what tomorrow — today — actually is. At adjudication, the agency must prove dependency by clear and convincing evidence; you do not have to prove innocence or fitness to win. A fact the agency does not prove is a fact the court cannot use. And you have counsel beside you, as is your right. (42 Pa.C.S. § 6337)

"If we oppose this continuance," she says, "the judge will ask one question in three forms: How long has the child been waiting? Is the other side ready? Are you? Feelings will not answer those questions. Exhibits will."

On the table between you: your completed parenting course certificate, finished in October. In the hallway: your sister, and Omar's school counselor, both here, both able to speak today. Counted on Ms. Ferreira's pad: sixty-three days of placement as of yesterday, and a mother who is ready to be heard this morning.

**Choices:**
- Put the record in her hands — certificate in the folder, witnesses confirmed in the hallway, the 63 days counted and ready to state → **hallway_hinge**  _(FLAG: evidenceReady ; HIDDEN + Exhibit — parenting course certificate, in counsel's hand at the hearing)_
  - NOTE (shown after choosing): Nothing about this is dramatic. It is a folder, two people on a bench, and a number that took ten minutes to count. It is also the entire difference between opposing and merely objecting.
- Go in with what's in your head — the certificate is at your sister's house and the witnesses can be called another day → **hallway_hinge**
  - NOTE (shown after choosing): Everything you know is true. None of it is in a form a judge can hold. In this building, that gap is where cases live.
- Spend the twenty minutes drafting the interim terms you would demand if you consented — visits, service dates, the record request, all in writing → **hallway_hinge**  _(FLAG: termsReady)_
  - NOTE (shown after choosing): Ms. Ferreira keeps the list. If the day turns toward bargaining, you will be bargaining from paper instead of from hope.

## [hallway_hinge] The Ask, in the Hallway
*Day 1 — Tuesday, November 17, 2026 (dayOffset 1)*

The agency's lawyer finds you by the courtroom door, file under one arm, tone reasonable. The request, stated plainly: continue adjudication four weeks, to Tuesday, December 15, 2026. The caseworker who knows the file is on leave. The file is not assembled. Nobody is at fault, he says. It is just four weeks.

He does not say — because hallway asks never do — what those four weeks contain on Omar's side of the ledger: four more weeks of a backpack by a door, of visits on an agency schedule, of a boy measuring his life in a unit the court treats as a rounding error.

Ms. Ferreira looks at you. Three doors stand open, and they are genuinely different strategies, not a right answer wearing two disguises. You can oppose, and make the agency carry its burden today or lose the day. You can consent — but only in exchange for written terms the court orders. Or you can let the request pass over you like weather.

**Choices:**
- OPPOSE — take the request into the courtroom and fight it → **oppose_choice**
  - NOTE (shown after choosing): Opposition is a posture. What it is worth depends entirely on what you carry into the room with it.
- NEGOTIATE — consent only in exchange for terms written into the court's order → **consent_terms**
  - NOTE (shown after choosing): Four weeks is a thing of value. The question is whether Omar's side gets anything for it, and whether what it gets is written down where judges can enforce it.
- LET IT HAPPEN — say nothing, and let the request go through unopposed → **drift_ruling**
  - NOTE (shown after choosing): The hallway empties. The agency's lawyer notes the absence of objection the way people note weather: briefly, and in writing.

## [oppose_choice] How to Oppose
*Day 1 — Tuesday, November 17, 2026 (dayOffset 1)*

The bailiff calls the case. Ms. Ferreira stands, and the shape of the next two minutes is yours to choose.

She can oppose with the record: state Omar's sixty-three days in placement, on the record, where the transcript keeps it; put your completed certificate in counsel's hand where the judge can see it exists; name the witnesses sitting in the hallway, ready today; and say the sentence that continuance fights turn on — "We are ready to proceed. If the agency is not ready to carry its burden today, that is the agency's answer, not a reason to make a thirteen-year-old wait for it."

Or she can object the other way: loudly, sincerely, and with nothing behind it but the unfairness of it all. Judges have heard that objection ten thousand times. It has a sound, and the sound is: nothing here will be different in four weeks either.

**Choices:**
- OPPOSE ON THE RECORD — the 63 days stated, the certificate in hand, the witnesses named, readiness declared → **oppose_hearing**  _(FLAG: opposedOnRecord ; HIDDEN + Transcript — parent's objection to the continuance, with the child's 63 days in placement stated on the record ; REQUIRES FLAG: evidenceReady)_
  - NOTE (shown after choosing): Every sentence of it goes into the transcript. That is the point. The judge is no longer deciding whether you feel ready; she is deciding what to do with a record that shows you are.
- OBJECT LOUDLY — argue how unfair the delay is, but offer no dates, no certificate, no witnesses → **oppose_empty**
  - NOTE (shown after choosing): Your voice carries in the courtroom. Then it stops carrying, the way voices do, at exactly the moment the judge looks down at the empty space where the record would be.
- Step back at the bar — negotiate terms for consent instead of fighting → **consent_terms**
  - NOTE (shown after choosing): Not a surrender. A different weapon. Its value will depend on whether the terms end up in an order or in the air.

## [oppose_hearing] The Judge Asks Three Questions
*Day 1 — Tuesday, November 17, 2026 (dayOffset 1)*

The judge listens to the agency's request the way judges listen to requests they have granted a hundred times — and then she starts asking the questions that a record can answer and a hallway cannot.

When did the agency learn its caseworker would be on leave? Weeks ago. When was this hearing scheduled? Before that. How long has the child been in placement? It is Ms. Ferreira who answers, from the record your side made: sixty-three days as of yesterday, with his aunt — a good home, and not his home. Is the parent ready to proceed today? "We are ready, Your Honor. Certificate completed in October. Two witnesses in the hallway." Is the agency ready? A pause that does the transcript no favors.

"A continuance is not a courtesy I hand out against a child's calendar," the judge says. "The request is denied. We proceed." The agency's lawyer asks for ten minutes. What he is really asking for is a case.

**Choices:**
- Proceed — let the agency open its case and carry its burden, today, with what it actually has → **oppose_cross**
  - NOTE (shown after choosing): This is the ground your opposition bought: the burden sits where the law puts it, on the agency, and it is due now.
- Use the ten minutes to make sure Omar, at his aunt's, hears the news from you and not from a summary later → **oppose_cross**
  - NOTE (shown after choosing): A short call, a steady voice: "The judge said today. Today is happening." Then the courtroom door closes and the case begins.

## [oppose_cross] A Supervisor, Reading
*Day 1 — Tuesday, November 17, 2026 (dayOffset 1)*

The agency calls its only witness: a supervisor, covering for the caseworker on leave, testifying from the file. She is professional and careful, and the carefulness is the problem — she did not visit your home, did not write the notes she is reading, and cannot say from her own knowledge whether the concerns in them were ever checked after September.

On cross-examination Ms. Ferreira is almost gentle. Who wrote this page? The caseworker. Who observed this? The caseworker. Is she here? She is not. The relaxed rules that let written reports come in freely belong to a different hearing — at disposition, written reports may be received and their makers examined and cross-examined (42 Pa.C.S. § 6341(d)(1), (d)(2)) — but this is adjudication, and adjudication runs on proof: the court may find a child dependent only from clear and convincing evidence. (42 Pa.C.S. § 6341(c))

You do not have to prove anything in this room. That sentence, which sounded abstract in the counsel room, turns out to be load-bearing.

**Choices:**
- Rest without testifying — the agency's evidence is the agency's problem, and it has not carried its burden → **agency_folds**
  - NOTE (shown after choosing): A principled quiet. Your certificate and your witnesses stand ready and unneeded; the case will be decided on the proof that was actually offered, which is the proof the law required.
- Let Ms. Ferreira put your certificate and one witness on anyway, so the court sees the whole picture → **agency_folds**  _(cash −5 ; FLAG: proofOffered)_
  - NOTE (shown after choosing): Five dollars of copies for the court and counsel. It changes nothing about the burden — and it leaves the judge with a picture of a parent who did not need the law's protection and used her own evidence anyway.

## [agency_folds] The Agency Rests
*Day 1 — Tuesday, November 17, 2026 (dayOffset 1)*

The agency rests the way a bridge rests when a cable goes: all at once, and audibly. There is no second witness. There is no assembled file. There is a supervisor, a stack of other people's notes, and a burden that was announced this morning and has not moved.

Ms. Ferreira's closing takes ninety seconds. Sixty-three days. A parent ready this morning, certificate in hand, witnesses in the hall. An agency that asked for four more weeks because it could not do today what the law required it to do today. "The petition asks this court to find dependency from clear and convincing evidence, Your Honor. The evidence offered is a file read aloud by someone who did not write it. If it is not proven, the petition is dismissed and the child is discharged. That is not my argument. It is the statute." (42 Pa.C.S. § 6341(a), (c))

The judge looks at the file in front of her for a long moment. Courtrooms have a particular silence for the moment before a ruling, and this one fills the room.

**Choices:**
- Hear the ruling standing beside your lawyer → **end_win**
  - NOTE (shown after choosing): Whatever it is, it was built this morning — out of a counted number, a carried folder, and a refusal to let readiness go unrecorded.
- Hear it already doing the arithmetic of the school run, the backpack, the drive to your sister's → **end_win**
  - NOTE (shown after choosing): Parents are allowed two thoughts at once. The ruling gets one of them. Omar gets the other. He always did.

## [oppose_empty] Volume Is Not a Record
*Day 1 — Tuesday, November 17, 2026 (dayOffset 1)*

The objection is heartfelt, and it is loud, and it takes four minutes, and at the end of it the judge asks the question objections like this always meet: "Counsel, what are you offering me? How long has the child been placed? Are you ready to proceed today — witnesses, exhibits, anything I can act on?"

Ms. Ferreira does her best with what the morning gave her, which is your memory and your anger, both genuine, neither admissible. The certificate is at your sister's house. The witnesses were never told to come. The days were never counted. From the bench, readiness that cannot be shown looks exactly like unreadiness — and unreadiness, the judge notes, is what the agency is asking to be excused for. If both sides are unready, the tie goes to the calendar.

You watch the objection you made turn, in the transcript, into a paragraph the next judge will read as: parent objected, offered nothing.

**Choices:**
- Stay for the ruling — you have already said everything there was to say, and that was the problem → **empty_ruling**
  - NOTE (shown after choosing): The agency's lawyer is looking at his file with the stillness of a man who has just been handed four weeks by the side that came to take them away.
- Ask for two minutes to call your sister about the certificate — knowing the answer about timing before you dial → **empty_ruling**
  - NOTE (shown after choosing): Paper at another address is a story about paper. The hearing is here. The hearing is now. That is the whole lesson, arriving at its usual price.

## [empty_ruling] Granted — and Noted
*Day 1 — Tuesday, November 17, 2026 (dayOffset 1)*

The continuance is granted, to Tuesday, December 15, 2026. The judge's order is short, and one of its sentences will outlive the hearing: the continuance issues over the parent's objection, which the court found unsupported by any showing of prejudice or readiness.

That sentence is the true cost of the morning — worse, in its way, than the four weeks themselves. Four weeks pass. A judicial impression, written into an order, stays: this parent's asks arrive without anything under them. The next time your side asks this court for something — a visit, a service, a date — it will be read by a judge who has already been taught, by you, what your asking is worth.

Outside, Ms. Ferreira does not say I told you so, because she is a professional and because you are already saying it to yourself at a volume no transcript could hold. "Four weeks is still four weeks," she says. "What they become is not decided yet. It is just — not helped."

**Choices:**
- Ask her, honestly, what the weeks can still be used for → **drift_week1**
  - NOTE (shown after choosing): Her answer is real but thin: visits, services, paper — all of it now uphill, on a slope the objection built.
- Go home and call your sister with the new date — December 15 — and hear how it sounds out loud → **drift_week1**
  - NOTE (shown after choosing): It sounds like a month. On the phone there is a pause, and in the pause you can hear a thirteen-year-old in the next room doing the arithmetic no one taught him.

## [consent_terms] The Price of Four Weeks
*Day 1 — Tuesday, November 17, 2026 (dayOffset 1)*

"We will consent," Ms. Ferreira tells the agency's lawyer, in the hallway, "and here is what consent costs." This is the other strategy, and it is a real one: judges remember a parent who was reasonable about a caseworker's leave — and a continuance you agree to can buy things a fight never would, if, and only if, the things are written where a court can enforce them.

The terms, as your side drafts them: visits double, starting this week, and longer; the family service starts on a named date, not "when the referral goes through"; the record request your side filed is acknowledged, with the record to be produced in time to prepare; and all of it goes into the court's order — not a hallway understanding, an order, with the judge's signature under it.

The agency's lawyer reads the list twice. "Half of this I can just promise you," he says. "The visits, the referral — we'll take care of it. Do we really need the court's paper for a scheduling matter?" That question, right there, is the whole game in one sentence.

**Choices:**
- CONSENT WITH TEETH — agree only if every term is written into the court's order, signed today → **consent_order**  _(FLAG: consentWithTerms ; HIDDEN + Order — interim terms: visits doubled, service start dates fixed, record request acknowledged)_
  - NOTE (shown after choosing): An order is a promise with a judge attached. Whatever these four weeks become, they will become it under a document your side can point to, line by line.
- Accept his word — "we'll take care of it" — and save everyone's morning → **drift_week1**
  - NOTE (shown after choosing): He probably means it. People in hallways usually do. The file, however, will record a continuance consented to without conditions — and hallways are not where enforcement lives.
- Walk away from the table — if terms are too much trouble, opposition is still available → **oppose_choice**
  - NOTE (shown after choosing): The courtroom door is ten feet away. Bargaining you can abandon is bargaining with a spine; the agency's lawyer watches you remember that.

## [consent_order] Signed, in Open Court
*Day 1 — Tuesday, November 17, 2026 (dayOffset 1)*

The hearing takes eleven minutes. The judge reads the proposed terms once, asks the agency's lawyer twice whether the agency agrees — on the record, both times — and signs. The continuance is granted to Tuesday, December 15, 2026, and the order granting it is not one paragraph but two pages: visits doubled beginning this week; the family service to start on its named date; the pending record request acknowledged, production to precede the new hearing date by enough time to matter.

Ms. Ferreira hands you your copy in the hallway. "Be clear about what just happened," she says. "We did not win. We sold four weeks of Omar's life — and we got a price for them, in writing, that a court will enforce. Whether it was worth it gets decided by what the weeks contain. That part starts tomorrow, and a good deal of it is ours to do."

Omar will ask tonight whether four more weeks means he did something. The answer is still no. The difference, this time, is that you can also tell him what the four weeks are for.

**Choices:**
- Take the order home and put the doubled visit dates and the service start date on the refrigerator, where Omar can see them at his aunt's and you can see them at home → **consent_week1**
  - NOTE (shown after choosing): Dates on a refrigerator are not law. Dates in a signed order are. Having both is how a family lives inside a case without disappearing into it.
- Call your sister from the courthouse steps and read her the terms, exactly as written → **consent_week1**
  - NOTE (shown after choosing): She writes them on her own calendar while you read. Paper in two houses. That is what an order is for.

## [consent_week1] Week One, With Paper Behind It
*Day 2 — Wednesday, November 18, 2026 (dayOffset 2)*

The first test of an order comes fast: the agency's scheduling office calls about the week's visit and proposes the usual one hour, Saturday, take it or leave it. This is the moment the whole strategy was built for. You do not argue. You do not plead. You read the order's second paragraph aloud, politely, the way you would read a bus schedule.

A pause. A keyboard. The visit becomes two hours, Saturday and again Wednesday, the way the judge signed it. Nobody apologizes and nobody needs to. The paper did the pushing, which is what paper is for — it lets a mother be pleasant and immovable at the same time.

The service intake is confirmed for its named date. Omar's aunt reports that he asked whether the longer visits "count." They count, she told him. She is right in more ways than the visit log will ever say.

**Choices:**
- Take both visits, take the bus both times, and keep every receipt and confirmation in the folder → **consent_visits**  _(cash −8 ; FLAG: visitsKept)_
  - NOTE (shown after choosing): Eight dollars of bus fare. The folder grows a section: ORDER, and under it, KEPT. Judges read sections like that the way accountants read ledgers.
- Take both visits and let the folder go this week — the order speaks for itself → **consent_visits**
  - NOTE (shown after choosing): The order does speak for itself — about what was promised. What was kept will need its own evidence, and evidence is a habit, not an event.

## [consent_visits] Week Two: The Visits Are Real
*Day 8 — Tuesday, November 24, 2026 (dayOffset 8)*

The doubled visits are not an abstraction anymore. Two hours is long enough for homework help, a card game, and the kind of conversation that does not happen in a one-hour room with a clock — Omar tells you about a math test, a friend, a plan for the spring that assumes, in every detail, that he will be home for it. You let the assumption stand. So, more and more, does the file.

The family service has started on the date the order named. The worker is new to the case and reads the order before she reads anything else, which tells you something about what the system's own people treat as real. Your sister reports, drily, that Omar has stopped keeping his backpack by the door. You have complicated feelings about that, and all of them are allowed.

Halfway through the sold month, Ms. Ferreira calls: the agency record, requested in writing before the first hearing, is being produced. "Clear your weekend," she says. "We are going to read what they wrote."

**Choices:**
- Clear the weekend — reading your own file with your lawyer is an appointment like any other, and you keep appointments → **consent_record**
  - NOTE (shown after choosing): The record is the one witness that never forgets and never improvises. Whatever is in it, December's hearing will be fought on it.
- Ask her to skim it and tell you the short version → **consent_record**
  - NOTE (shown after choosing): The short version of a file is somebody else's judgment about what matters in your case. Sometimes that is fine. December is not a short-version month.

## [consent_record] Week Three: What the Record Shows
*Day 15 — Tuesday, December 1, 2026 (dayOffset 15)*

The record arrives because the law says it does: agency records "shall be released upon request." (55 Pa. Code § 3130.44(d)) Some pages are blacked out. Enough are not. And on a Tuesday afternoon in your lawyer's office, the file tells a story the agency did not intend to tell about itself.

Two referrals — the parenting support referral in September and the family service referral in October, the very services your plan was faulted for not completing — are logged as created. Neither was ever sent. There is no transmission, no provider copy, no follow-up. For two months, the file has recorded your non-completion of services the agency never actually referred you to.

Ms. Ferreira puts a flag on each page, the small sticky kind, and says the thing lawyers say when a case changes shape: "This is reasonable-efforts material. When a court asks whether the agency did what it was supposed to do to keep this family together or bring Omar home, this is what the answer looks like — in the agency's own handwriting."

**Choices:**
- Read it line by line with her and build the December packet around the two referrals that were never sent → **consent_service**  _(FLAG: recordsRequested ; FLAG: recordRead ; HIDDEN + File — agency record released on written request (§ 3130.44(d)); two referrals shown as never sent)_
  - NOTE (shown after choosing): The request was filed the night before the first hearing — a five-dollar piece of paper, arriving exactly when it was needed, because it was sent before anyone knew it would be.
- Set the packet aside — it is a lot of paper, the visits are going well, and December still feels far away → **consent_service**
  - NOTE (shown after choosing): December is fourteen days away. Paper you have not read is paper the other side reads alone. The referrals sit in the folder, unflagged, unargued, waiting.

## [consent_service] Week Four: Boring and Complete
*Day 22 — Tuesday, December 8, 2026 (dayOffset 22)*

The last week of the four arrives with the strange calm of a checklist nearly finished. The family service that started on the order's named date holds its final session of the month; the provider's summary uses the words "completed" and "engaged," which are not poetry and are better than poetry.

Four weeks of doubled visits: four of them, all kept, all logged — the long Saturday ones and the Wednesday ones, homework and card games and a math test debrief, written into the agency's own visit log by the agency's own workers. Your compliance with the order is not a claim anymore. It is a log.

Ms. Ferreira spreads December's packet on the counsel table — order, visit log, service summary, and the record pages with their sticky flags — and delivers the professional's verdict: "It is not dramatic. Good. Dramatic is what people bring when boring and complete isn't available."

**Choices:**
- Finish the packet properly — service certificate and the visit log copy filed with it, every page accounted for → **consent_hearing**  _(FLAG: serviceDone ; HIDDEN + Visit log — four expanded visits in four weeks, all kept)_
  - NOTE (shown after choosing): The log is the agency's own handwriting saying the weeks were used. In December, that handwriting will be sitting on your side of the table.
- Trust the summary and skip the copies — the agency has the log; the court can ask them for it → **consent_hearing**
  - NOTE (shown after choosing): The court can. Courts ask for what is put in front of them far more reliably than they go looking. A packet is a way of putting.

## [consent_hearing] The Continued Date
*Day 29 — Tuesday, December 15, 2026 (dayOffset 29)*

Four weeks to the day, the courtroom again. The caseworker is back from leave. The agency's file is assembled this time — the continuance did its work for them too, and honesty requires saying so: their proof is better today than it would have been in November.

But the room has changed in a second way. In November, the agency's story was of a mother who had not done the services. The record — the agency's own record, released on your written request — now sits in the packet with two referrals flagged that were never sent. And the question of what the agency did, while Omar waited, is on the table next to the question of what you did.

The judge turns to your side. What the next few minutes contain was decided across the last four Tuesdays — in an order, a log, a service summary, and a packet of flagged pages — or it was not, and no eloquence this morning can retrofit it.

**Choices:**
- Let Ms. Ferreira present the packet — order, log, service record, and the flagged referrals — in that order → **consent_proof**
  - NOTE (shown after choosing): Paper first, argument second. It is the house style of every win in this courthouse.
- Ask to speak to the judge yourself first — four weeks of feelings deserve a hearing too → **consent_proof**
  - NOTE (shown after choosing): The judge will let you, briefly and kindly. Feelings deserve a hearing. What they cannot do is substitute for one. The packet waits on the table while the clock runs.

## [consent_proof] What the Weeks Were For
*Day 29 — Tuesday, December 15, 2026 (dayOffset 29)*

Ms. Ferreira's presentation is almost aggressively undramatic. The order of November 17: visits doubled — the log shows them kept, four expanded visits in four weeks, in the agency's own entries. The service ordered to start on a named date: started, attended, completed for the period, certificate attached. And then the record pages, with their small sticky flags: the two referrals the agency's plan faulted you for missing, shown — in the agency's own file — as created and never sent.

"The agency will prove what it can prove today, Your Honor," she says, "and we do not shrink from its burden being tested. But the plan this family was judged against required services the agency never referred. The four weeks this court allowed have produced a record — of the parent's compliance, in full, and of the agency's efforts, in its own hand. We ask the court to weigh both."

She sits down. What happens next depends on whether the packet on the table is the whole packet — or the version of it that leaves its sharpest pages in a folder at home.

**Choices:**
- Present the full package — order terms kept, service certificate, visit log, and the agency record showing the referrals never sent → **end_partial**  _(REQUIRES FLAG: consentWithTerms ; REQUIRES FLAG: recordsRequested)_
  - NOTE (shown after choosing): This presentation exists because the terms were written into an order and the record was requested in writing. Both sentences are literally true, and they are the whole strategy.
- Present the visits and services only, and leave the agency record out of it → **consent_shortfall**
  - NOTE (shown after choosing): A warmer, softer presentation — and one that concedes the only pages that turned the agency's own efforts into an issue. The judge can only weigh what is weighed in front of her.

## [consent_shortfall] The Pages That Stayed Home
*Day 29 — Tuesday, December 15, 2026 (dayOffset 29)*

The hearing goes the way hearings go when one side's best evidence is not in the room. Your visits are praised — genuinely. Your service completion is credited — fully. And then the agency presents its assembled file, its returned caseworker, its narrowed and tidied proof, and there is nothing in front of the judge that answers the question the flagged pages would have raised: what did the agency do, while Omar waited, besides watch the mother?

Ms. Ferreira argues from memory of the record, and you can hear the difference, because you have heard the other version in practice — argument with pages, and argument without them. "Counsel," the judge says at last, "if that is in their file, I expect I will see it at the next stage. Today I rule on today's record."

Today's record. The phrase follows you down the courthouse steps like weather.

**Choices:**
- Hear the order she is about to write, knowing exactly which pages it was written without → **end_loss**
  - NOTE (shown after choosing): The knowledge is not consolation. It is, at best, tuition — paid in the usual currency, by the usual person, for a lesson the system teaches free of charge to anyone watching someone else learn it.
- Ask Ms. Ferreira, on the steps, whether the record can still be put before the court another way → **end_loss**
  - NOTE (shown after choosing): "At reviews, yes. Later is a real tense in this system," she says. "It is just never the tense anyone would choose. Today was the day it was worth the most."

## [drift_ruling] Granted, in Ninety Seconds
*Day 1 — Tuesday, November 17, 2026 (dayOffset 1)*

The hearing, if it can be called that, takes ninety seconds. The agency's lawyer states the request. The judge looks toward your table — the moment, the only moment, when an objection or a condition could have entered the record — and your table is quiet, because quiet is what you chose in the hallway, for reasons that felt like exhaustion and peacekeeping and are about to be translated into the file's language.

The continuance is granted to Tuesday, December 15, 2026. The order is one paragraph. It sets no visits, starts no services, acknowledges no requests. And the agency's report of this hearing, filed later that week, will contain a sentence that does more work than any other in Omar's file this month: "Mother did not object to the continuance."

Silence, it turns out, is not the absence of a statement. In a case file, silence is a statement — written by whoever holds the pen.

**Choices:**
- Walk out with your copy of the one-paragraph order and read it twice in the hallway → **drift_week1**
  - NOTE (shown after choosing): There is so little of it to read. That is the information. Four weeks were just allocated, and nothing you need was written into the allocation.
- Ask Ms. Ferreira whether anything can still be attached to the four weeks — a visit schedule, a start date, anything → **drift_week1**
  - NOTE (shown after choosing): "We can ask," she says, and you hear the difference between asking from an order and asking from a favor. "Asking is what is left. We will ask."

## [drift_week1] Week One of the Four
*Day 2 — Wednesday, November 18, 2026 (dayOffset 2)*

The first week of the continuance looks, from the inside, almost like rest. No court date looms. The agency is quiet. Your sister's house settles back into its school-week rhythm, and it would be easy — it is easy — to experience the month the way the court does: as a gap in the calendar, a pause between events.

But the month is not paused. It is being written. The visit this week is the usual single hour, because nothing ordered it to be anything else. The family service has not started, because a referral — you will learn this later, in a worse week — is sitting in a queue no order pushed it out of. Omar asks his aunt how many days are in four weeks. Twenty-eight, she tells him. He already knew. He wanted to hear whether the adults did.

On your refrigerator, the space where dates could go is empty. Nothing was promised there. Nothing was ordered anywhere.

**Choices:**
- Call the agency and ask, politely, for a longer visit this Saturday anyway → **drift_week2**  _(cash −6)_
  - NOTE (shown after choosing): Six dollars of bus fare to the office and back with the answer, which is: scheduling is set for the month. Asking without an order behind it is a request. Requests are granted at the speed of other people's priorities.
- Let the week be quiet — everyone is tired, and December will come either way → **drift_week2**
  - NOTE (shown after choosing): December will. The question the file will ask in December is not whether everyone was tired. It will ask what the weeks contain, and tired, however true, is not a content.

## [drift_week2] Week Two: The Quiet Compounds
*Day 8 — Tuesday, November 24, 2026 (dayOffset 8)*

The second week, the quiet starts to have a texture. The service still has not started — the referral, the agency says when your sister calls, is "in process," a phrase with no date in it. Your one hour with Omar is spent substantially on logistics: a school form, a winter coat question, the arithmetic of whose house Christmas would be at, asked carefully by a boy who has learned to ask important questions carefully.

Ms. Ferreira, when you call her, is honest in the way that costs her something: "We are spending the month, not using it. In December they will walk in with a finished file. We will walk in with the fact that we were pleasant for four weeks. Pleasant is not an exhibit."

There are still moves — there are almost always still moves. They are just smaller now, and later, and worth less than they were worth in a hallway on November 17.

**Choices:**
- File the written record request now — late, but in writing, so the file at least has to be opened to your side before December → **drift_week3**  _(FLAG: recordsRequested)_
  - NOTE (shown after choosing): Late paper is still paper; it will matter at reviews and after. But production takes time the calendar no longer has, and December 15 is already circled in the agency's color, not yours.
- Spend the energy on Omar instead — an extra call each night, homework help by phone, presence over paper → **drift_week3**
  - NOTE (shown after choosing): He feels every minute of it. The file feels none of it. Both of those facts will be true in December, in the same room, at the same time.

## [drift_week3] Week Three: "He's Fine at His Aunt's"
*Day 15 — Tuesday, December 1, 2026 (dayOffset 15)*

Halfway through the month, someone who loves you says the sentence, meaning comfort: "At least he's fine at his aunt's. It's a good home. The time will pass." It is true — the home is good, your sister is the best part of this whole case, and Omar is loved there in a way the file itself acknowledges.

And it is the trap, stated in its gentlest form. Omar's clock is not the court's clock. A month that registers in the system as a scheduling entry registers in a thirteen-year-old as a season: a quarter of a school term, a holiday spent as a guest in the house he is grateful for, twenty-eight nights of a backpack he has started keeping by the door again. Fine is a condition. It is not a duration a child experiences as short.

Meanwhile the agency's month is not quiet at all. Its caseworker returns from leave this week. Its file begins, page by page, to be assembled — the thing it said, in November, that it needed four weeks to do.

**Choices:**
- Hear Omar's clock over the comfort — start scrambling: gather the certificate, call the counselor, list the witnesses, two weeks out → **drift_week4**  _(FLAG: scramble)_
  - NOTE (shown after choosing): Late preparation is real preparation; December will be better for it. It cannot recover the thing November offered, which was making the agency carry its burden before it was ready — that door closed the day it wasn't pushed.
- Take the comfort — he is safe, he is loved, and a frantic mother helps no one → **drift_week4**
  - NOTE (shown after choosing): He is safe. He is loved. And the file will not record either as a reason the month was well spent — the file records the agency's assembled proof, and the sentence about who did not object.

## [drift_week4] Week Four: Two Files
*Day 22 — Tuesday, December 8, 2026 (dayOffset 22)*

The last week makes the month's accounting plain. On the agency's side: a completed file. The caseworker back at her desk, the notes organized, the witnesses lined up, the concerns updated and sourced — four weeks, used exactly as the continuance asked the court to let them be used. Nobody at the agency wasted the month. That was never the allegation. The allegation, if your side had made one in time, was that Omar shouldn't have had to pay for it.

On your side: a certificate that surfaced late, a counselor who can come but was asked late, visits that stayed at an hour because nothing ever made them longer, a service that has barely begun because its referral moved at the speed of an un-ordered queue. None of it is nothing. All of it is thinner than December required.

Omar, on the phone, asks whether the judge will decide "for real this time." You tell him yes. You do not tell him — he is thirteen, and some adult knowledge is a debt you pay so he doesn't — that December's hearing was substantially decided in November, in ninety seconds, by a quiet table.

**Choices:**
- Spend the week drilling with Ms. Ferreira — testimony order, exhibits numbered, everything the scramble produced, made as ready as late can be → **drift_hearing**
  - NOTE (shown after choosing): Readiness in December is worth having. Its tragedy is arithmetic: the same readiness, in November, was worth a dismissal. Timing is not a detail in this system. It is most of the substance.
- Spend the week with Omar — the visits, the calls, the ordinary mothering that no file has ever once recorded → **drift_hearing**
  - NOTE (shown after choosing): He will remember this week when the file is forgotten. That is not nothing. It is simply not evidence, and December is an evidence event.

## [drift_hearing] December 15, on Their File
*Day 29 — Tuesday, December 15, 2026 (dayOffset 29)*

The hearing proceeds the way the agency hoped, back in November, that it would. The caseworker testifies from her own notes, in her own knowledge. The file is complete, the witnesses are present, the proof is organized to the standard the law sets — dependency, argued from clear and convincing evidence, by a side that was given four weeks and used every one of them.

Your side cross-examines well and presents what the scramble built, and it is not nothing — but the hearing keeps bending around a fact no December argument can move: for four weeks, the only party treating time as precious was the party that asked for more of it. The agency's report phrase is in the record, unrebutted by any November transcript: mother did not object to the continuance. Silence, filed in November, testifying in December.

Near the end, the judge asks whether there is anything further on the parent's efforts during the continuance period. Ms. Ferreira presents the late paper, honestly labeled with its dates. The judge accepts it, and the dates say what they say.

**Choices:**
- Stay for the ruling — all of it, in the room, the way you were not quite in the room in November → **end_loss**
  - NOTE (shown after choosing): Presence now does not rewrite presence then. You stay anyway. Omar's case will have more rooms, and you intend to be in all of them differently.
- Listen for the parts that are still movable — the disposition, the services, the dates — because the case does not end today even if the hearing does → **end_loss**
  - NOTE (shown after choosing): Correct, and it matters: adjudication is a door, not the whole house. What comes after it — placement, plan, reviews — is all still arguable, on a record that starts being written again tomorrow.

## [end_win] Heard Today — Home by Supper
*Day 1 — Tuesday, November 17, 2026 (dayOffset 1)*

The ruling takes one paragraph, read aloud. The agency has not carried its burden of proving dependency by clear and convincing evidence. The petition is dismissed. The child is discharged. Omar's placement — the placement, the court says pointedly, that was to have been extended four weeks so the agency could prepare to justify it — ends today.

There is a particular quality to courtroom joy: it arrives in whispers and signatures, because the room belongs to other people's worst days too. Ms. Ferreira shakes your hand like a person closing a well-made thing. Your sister cries in the hallway with her coat still on. The paperwork of discharge takes an hour. It is the best hour of paperwork of your life.

Omar is at school until three. You pick him up yourself — not a visit, not supervised, not scheduled against a log — and his backpack goes into your trunk instead of back to the door it had been living by. At home, over the supper he requested on the drive (the specific, ordinary supper of a boy resuming his life), he asks whether the judge knew about the sixty-three days. "She counted them out loud," you tell him. "In the room. So they're in the record." He considers this with the seriousness of a person who has learned what records are. "Good," he says.

**Ending.**

**Debrief:**
- WHAT THE FILE SAID — the record that decided this ending was built in about eighteen hours: the written request for the full agency record, filed the night before the hearing (flag: recordsRequested); the parenting course certificate, physically in counsel's hand in the courtroom (flag: evidenceReady; hidden item: the exhibit); and above all the objection stated on the record with Omar's 63 days in placement counted aloud (flag: opposedOnRecord; hidden item: the transcript). The agency's file, by contrast, showed a caseworker on leave, notes its own witness had not written, and a request for four weeks that its own timeline could not justify. The hidden assessment in this case was never a score — it was two files, and only one of them was ready.
- THE LAW THAT CONTROLLED IT — at adjudication the court may find a child dependent ONLY "from clear and convincing evidence" — 42 Pa.C.S. § 6341(c); the burden is the agency's, and the parent does not have to prove innocence or fitness to defeat it. Where dependency is not proven, the petition is dismissed and the child discharged — § 6341(a). The relaxed rule allowing written reports at DISPOSITION, whose makers may be examined and cross-examined — § 6341(d)(1), (d)(2) — did not rescue secondhand proof at adjudication. Counsel was present throughout, as of right — § 6337. And the record request that sharpened the whole defense rests on 55 Pa. Code § 3130.44(d): the record "shall be released upon request." A continuance, finally, lives in the court's discretion — what persuaded this court was not outrage but a record of diligence on one side, unreadiness on the other, and a child's 63 days stated where the transcript keeps them.
- THE HONEST PART — this ending turned on the agency genuinely being unready, on this judge, on this day. A different judge grants the continuance over the same record; a caseworker returns from leave a week early; a supervisor testifies better from someone else's notes. None of that was yours to control, and the same folder, carried into a different courtroom, can produce the middle ending instead. What was yours was narrower: being ready, on paper, on the one morning readiness was the question. Outcomes here turn on workers, judges, resources, and luck — this one also turned on a counted number and a carried certificate, and that is not a verdict on any parent who ever walked in without them. It is a description of where the leverage was.

## [end_partial] Four Weeks, With Teeth
*Day 30 — Wednesday, December 16, 2026 (dayOffset 30)*

The order is entered the morning after the hearing, and it is a document of two honest halves. On the agency's narrowed ground — one supervision period in September, proven to the standard — the court finds dependency. On disposition, with the order's terms kept in full, the service completed, the visit log unblemished, and the agency's own record showing two referrals it never sent, the court orders the disposition your side asked for: Omar returns home, remaining with his parent subject to conditions and supervision, with the agency's services to actually be delivered this time — referred, dated, and on the record. (42 Pa.C.S. § 6351(a)(1))

He comes home on Wednesday, December 16, 2026, with a court order in your folder instead of a continuance in his calendar. The backpack goes to his own room. Supper is the requested supper. Your sister cries in your kitchen this time, coat off, staying for it.

Call it what it is, because Omar will: a win with a month missing from the middle of it. The teeth were real — the order, the log, the record, the disposition — and so are the teeth marks: four weeks of a thirteen-year-old's life, spent proving, again, that he should not have had to spend them.

**Ending.**

**Debrief:**
- WHAT THE FILE SAID — this ending was bought with the only currency the four weeks accepted: the interim order itself, with visits doubled and service start dates fixed (flag: consentWithTerms; hidden item: the order); the visit log showing four expanded visits in four weeks, all kept (hidden item: the log); and the agency record, released on the written request filed November 16 (flag: recordsRequested; hidden item: the file) — which showed, in the agency's own entries, two referrals created and never sent. The file at the December hearing contained two stories: a mother who completed what was actually delivered to her, and an agency whose plan faulted her for services it never referred. The court weighed both, because both were finally in front of it.
- THE LAW THAT CONTROLLED IT — the agency still had to prove dependency from clear and convincing evidence at the December adjudication — 42 Pa.C.S. § 6341(c) — and it carried that burden only on narrowed ground. At disposition, the court chose from the statute's options and ordered the child to remain with the parent subject to conditions and supervision — § 6351(a)(1) — a choice the record supported because the agency's reasonable efforts were now examinable: the file produced under 55 Pa. Code § 3130.44(d) ("shall be released upon request") showed referrals never sent, which is what an efforts argument looks like when it is made of paper instead of adjectives. The terms that made the month survivable — doubled visits, dated services — existed because they were written into a court order on November 17, not promised in a hallway.
- THE HONEST PART — this is labeled a partial win because it is one: Omar is home, and Omar lost a month. A different judge could have denied the continuance in November and sent him home then; the same four weeks, sold without terms, end in the outcome below this one; the record packet could have sat unproduced, or unrequested, or unread, and December would have been fought on the agency's file alone. Workers, judges, and luck held pieces of this at every step — the caseworker's leave created the opening, and a different supervisor might have guarded the referrals better. What strategy controlled was only this: the weeks were sold, not given, and the price was collected in writing and spent on paper. Whether four weeks should ever have been the price is a question the outcome does not answer. Omar, home at his own table, is allowed to have an opinion about it that outranks this debrief.

## [end_loss] Four More Weeks of Nothing
*Day 30 — Wednesday, December 16, 2026 (dayOffset 30)*

The order is entered the morning after the December hearing. On the agency's now-complete proof, the court finds Omar dependent. Before ordering a disposition that keeps him placed, the court states its findings on the record, as the law requires: that continuation in the home would be contrary to his welfare at this time, and that reasonable efforts were made — findings the December record, as built, gave the court room to make. (42 Pa.C.S. § 6351(b)) Omar remains with his aunt. The next hearing — a permanency hearing, which must come within six months — is set from the bench, in the tone of a thing recited. (42 Pa.C.S. § 6351(e)(3)(i))

Your sister renews the backpack's lease by the door without a word about it. Omar takes the news the way he has learned to take news in this case: quietly, and with a count. "So how many days is it now, total?" Ninety-three. He does the look of a boy adding a column he intends to keep adding.

On the drive home, Ms. Ferreira says the truest available thing: "November 17 was the hearing. It just didn't happen in the courtroom. December was the ruling on what November did." The case is not over — dispositions are reviewed, plans are arguable, records are still requestable and still, now, requested. But the month's sentence stands in the file where November put it, in the agency's handwriting, unrebutted: mother did not object to the continuance.

**Ending.**

**Debrief:**
- WHAT THE FILE SAID — this ending's record is defined by absences that read as presences. No objection with anything under it: either silence at the November table, which the agency's report preserved as the sentence "mother did not object to the continuance," or an objection the court found unsupported by any showing of readiness or prejudice — a paragraph that discounted every later ask. No interim order: visits stayed at an hour because nothing ordered them longer; the service referral sat in a queue no order pushed. No timely record in your side's hands: whatever the agency's file contained about its own efforts, it was never put in front of the December court with pages attached. Against those absences stood the agency's December file — complete, sourced, and carried to the statutory standard by the very four weeks November handed it.
- THE LAW THAT CONTROLLED IT — the burden never moved: dependency may be found only from clear and convincing evidence — 42 Pa.C.S. § 6341(c) — and in December, on a completed record, the agency carried it. A disposition keeping a child placed requires the court first to enter findings on the record — contrary-to-welfare and reasonable efforts — § 6351(b); the record built across the four weeks allowed those findings to be made. The case continues under the permanency framework: hearings within six months of removal and of each prior permanency hearing — § 6351(e)(3)(i) — at which the court must determine placement necessity, plan compliance, progress, and reasonable efforts to finalize the plan — § 6351(f)(1), (2), (3), (5.1). The record request remains available at every stage: agency records "shall be released upon request" — 55 Pa. Code § 3130.44(d). Nothing in this ending is the last word the law allows. It is only the word the November record earned.
- THE HONEST PART — nothing about this outcome measures Teresa as a mother, and the game does not pretend otherwise. It measures a calendar, a hallway, and a pen. A caseworker's leave, a judge's ninety seconds, a mother's exhaustion on the one morning exhaustion was expensive — different workers, a different judge, a sister who lived closer to the courthouse with a certificate in her kitchen drawer, and the same woman lands in a different ending. That is not comfort and it is not an excuse the system offers; it is simply the truth about where this outcome came from. What remains true alongside it: the next record starts tomorrow, reviews are real hearings, and the sentence in the file is a sentence — not the whole book, unless nobody writes the next one.
