# THE FIRST 90 DAYS — Scenario 87: “The Second Letter”

*Human-readable script. This document and `scenario-87.json` are generated from a single source and match node-for-node: same IDs, same order, same choices, same effects.*

**The family is fictional — a composite. No real person's story appears here.**

**Content note:** This scenario depicts the days after an administrative appeal decision in a child-abuse registry matter — orders, deadlines, a clinic, and a mailbox. There is no graphic content. Players may skip any scene or use the quick exit at any time.

**How to read effects:** `cash −40` changes the player's cash. `FLAG: name` sets a flag the engine tracks. `HIDDEN + item` means the case file quietly records that item at this choice — the player does not see it when it happens. `REQUIRES FLAG: name` means the choice is only available if that flag was set earlier; `REQUIRES NO FLAG: name` means it is only available if that flag was never set. `NOTE:` is text shown to the player right after choosing.

Start date: Monday, March 2, 2026. Day offsets are days since the scenario's start date.

## [start] The Letter With Two Clocks
*Day 0 — Monday, March 2, 2026 (dayOffset 0)*

Your name is Sylvie Marchand. You work as an aide at the preschool two bus rides from your apartment, and your daughter Fern, five, is the light you organize every shift around. Last winter an indicated report of child abuse was filed against you after Fern's fall at the playground produced two medical readings that did not agree. You appealed it. A hearing officer heard the case, and the Bureau of Hearings and Appeals has now ruled.

The order in today's mail upholds the report. Your name stays on the registry, and the letter says plainly what that can mean for work in a childcare facility or a school. But the last page of the order is not only bad news. It describes what a person who disagrees may do next — and both of the things it describes run on clocks measured in days, not months.

The family is fictional — a composite. No real person's story appears here. What is real is the shape of the paper: an order, a mailing date, and a short window that starts whether you are ready or not.

**Choices:**
- Read the last page again, slowly, and write down the two dates it gives you → **legal_aid** _(FLAG: datesKept)_
  - NOTE (shown after choosing): Fifteen days to ask the Secretary to reconsider. Thirty days to perfect an appeal to Commonwealth Court. Both counted from the mailing date — today. You write them on the folder in ink.

## [legal_aid] The Legal Aid Line
*Day 1 — Tuesday, March 3, 2026 (dayOffset 1)*

The legal aid intake worker does not waste your minutes. "Two clocks," she says. "Asking for reconsideration and appealing to Commonwealth Court are different doors. Reconsideration goes back to the Secretary with something the Bureau got wrong or never saw. The court appeal is a judge reading the record that already exists — the court does not take new evidence."

"And one warning," she adds. "Asking for reconsideration does not stop the court clock. Families lose the second door all the time because they were politely waiting at the first one." (The two windows are stated in the order itself, from 23 Pa.C.S. § 6341(g): 15 calendar days from the mailing date to request reconsideration or appeal, and 30 calendar days from the mailing date to perfect an appeal to Commonwealth Court.)

**Choices:**
- Ask what could possibly be new — the hearing already happened → **mailbox**
  - NOTE (shown after choosing): "Anything the Bureau never saw," she says. "Start with your own mailbox. Agencies mail things. So do doctors."

## [mailbox] What Arrived Late
*Day 3 — Thursday, March 5, 2026 (dayOffset 3)*

At the bottom of the mailbox stack, under a grocery circular, is a thick envelope from the county agency, postmarked during your hearing week. Inside is the evidence packet the agency provided for your appeal — the investigation evidence, including material that could help you, which the agency must provide to a person making an appeal. (23 Pa.C.S. § 6341(c.2)(4)) One page was never mentioned at your hearing: a follow-up letter from Fern's pediatrician, written after a second examination, reading the injury as consistent with the playground fall you described.

It is not a magic page. It does not prove anything by itself. But the Bureau decided your case without ever seeing it, and a reconsideration request exists for exactly that shape of wrong.

**Choices:**
- Take the packet and the letter to the legal aid clinic this week → **clinic** _(FLAG: evidenceFound ; HIDDEN + Investigation packet — late-arriving pediatric follow-up letter identified, never considered at the hearing)_
  - NOTE (shown after choosing): You paper-clip the letter to the front of the packet. For the first time since the order arrived, the folder feels like it is pointing somewhere.
- Put the packet in the drawer — the hearing is over and you are tired → **clinic**
  - NOTE (shown after choosing): The drawer closes. The letter is still in the world, and the clocks are still running — but nobody's request will carry it anywhere from a drawer.

## [clinic] The Clinic's Two Pages
*Day 5 — Saturday, March 7, 2026 (dayOffset 5)*

Ms. Delvecchio, the clinic attorney, reads the order, then the pediatrician's letter, then the order again. "This is a reconsideration with a spine," she says. "Not 'please look again.' It is: here is evidence in the agency's own packet that the Bureau never addressed, and here is the page. We attach the letter, we cite the packet, and we file it well inside fifteen days."

"One more page," she says, sliding a short form across. "We also renew, in writing, the request for the complete investigation file — everything, not the excerpts. Records in the agency's file are to be released on request (55 Pa. Code § 3130.44(d)), and if this goes further, we will want the whole record, not the highlights." Copies cost $10 you did not budget.

**Choices:**
- Sign the reconsideration request with the letter attached, and the written request for the complete file → **daycare_office** _(cash −10 ; FLAG: reconDrafted ; FLAG: recordsRequested ; HIDDEN + Reconsideration — drafted with the unconsidered pediatric letter attached; complete investigation file requested in writing)_
  - NOTE (shown after choosing): Two signatures. The request now exists as paper, dated, with the new page riding on its back.
- Ask to come back next week and sign — you need to think it over → **clinic_late**
  - NOTE (shown after choosing): Thinking is free. This particular calendar charges for it by the day. And it spends the rest of your week — the director, the shift board, the quiet evenings — whether you spend them or not.

## [clinic_late] Seven Days Later
*Day 12 — Saturday, March 14, 2026 (dayOffset 12)*

You are back at the clinic on day twelve of fifteen. Ms. Delvecchio does not scold you; she moves faster. "We can still make it," she says, "if we sign today and file today. What we cannot do is miss anything else — not a page, not a date." The reconsideration is drafted the same way it would have been a week ago, with the pediatrician's letter attached and the written request for the complete file renewed. It is simply drafted against a wall now instead of against a calendar.

**Choices:**
- Sign both pages now and file today → **filing_day** _(cash −10 ; FLAG: reconDrafted ; FLAG: recordsRequested ; HIDDEN + Reconsideration — signed and filed on day twelve of fifteen; complete file requested in writing)_
  - NOTE (shown after choosing): The clerk's stamp lands like a small, kind hammer. Filed. Inside the window, with three days to spare and no margin left anywhere else.

## [daycare_office] The Director's Office
*Day 7 — Monday, March 9, 2026 (dayOffset 7)*

Your director calls you in with the careful voice people use around registry letters. The center runs clearances on a cycle, and your name's status is not a secret the schedule can keep. She is not unkind. She is also not able to promise anything: what she can do is tell you, honestly, that a pending reconsideration with a filed date is a different conversation than a closed file — and that the conversation will happen with or without your paperwork in it.

**Choices:**
- Tell her the truth with dates: the order, the filed reconsideration, the hearing to come → **shift_board** _(FLAG: directorTold ; HIDDEN + Employment — director informed in writing of the filed reconsideration and its dates)_
  - NOTE (shown after choosing): She writes the dates in the schedule book. "Then we wait for paper," she says, "instead of rumors."
- Say as little as possible and hope the cycle is slow → **shift_board**
  - NOTE (shown after choosing): Silence is also a schedule. It just isn't one you get to see.

## [shift_board] The Shift Board
*Day 9 — Wednesday, March 11, 2026 (dayOffset 9)*

Filing day and your hearing-prep day will both land on workdays; the board at the center is a grid of other people's emergencies. Your supervisor can swap your filing-day shift if she knows by Friday — the swap costs you a Saturday, which costs you $15 in bus fare and Fern's cousin's birthday. Keeping quiet costs nothing today.

**Choices:**
- Ask for the swap in writing and take the Saturday → **folder_night** _(cash −15 ; FLAG: shiftSwapped)_
  - NOTE (shown after choosing): The swap is initialed on the board. A small square of paper that means: you will be standing in the right room on the right day.
- Keep the shift and plan to file on your lunch break → **folder_night**
  - NOTE (shown after choosing): The courthouse is forty minutes away. Lunch is thirty. You do the arithmetic and decide not to look at it again.

## [folder_night] The Folder on the Table
*Day 11 — Friday, March 13, 2026 (dayOffset 11)*

The night before filing, the folder gets its once-over: the order with the two dates in ink on its last page, the packet, the pediatrician's letter paper-clipped to the reconsideration, the receipt for copies. Fern is asleep. The kitchen clock is loud in the way kitchen clocks are at 11 p.m.

Nothing in the folder guarantees an outcome. What it guarantees is smaller and real: if anyone, at any desk, asks what you did and when you did it, the answer will not depend on your memory.

**Choices:**
- Close the folder and sleep — filing day is tomorrow → **filing_day**
  - NOTE (shown after choosing): You set two alarms. The folder waits by the door like a dog that knows the route.

## [filing_day] Day Twelve of Fifteen
*Day 12 — Saturday, March 14, 2026 (dayOffset 12)*

The Bureau's office is quieter than you expected, and the clerk is faster. Everything now depends on what is in your hands: a reconsideration that exists as a drafted, signed document is a filing. A reconsideration that exists as an intention is a story you will tell later, to no one who can act on it.

**Choices:**
- File the reconsideration request, with the pediatrician's letter attached → **recon_filed** _(FLAG: reconFiled ; REQUIRES FLAG: reconDrafted)_
  - NOTE (shown after choosing): Stamped, copied, receipted. Day twelve of fifteen. The first clock is beaten, and the second door was never needed — yet.
- File only a notice of appeal to Commonwealth Court and skip reconsideration → **court_filed**
  - NOTE (shown after choosing): A valid door — but the court reads the record that exists, and the letter in your folder is not in it.

## [recon_filed] The Receipt
*Day 12 — Saturday, March 14, 2026 (dayOffset 12)*

The receipt has a date stamp, a docket line, and absolutely no opinion about your case, which is what makes it beautiful. Ms. Delvecchio photographs it for the file and hands you the folder. "Now the Secretary reads," she says. "Reconsideration can end three ways: denied, granted with the order changed, or granted with a new hearing ordered. If the answer is no, the court door was already counted and calendared — nothing about today spent it carelessly."

On the bus home you realize your shoulders have been somewhere up around your ears since March 2. They come down about an inch.

**Choices:**
- Go home and wait for the Secretary's answer on paper → **waiting_weeks**
  - NOTE (shown after choosing): Waiting is different when the thing being waited for has a receipt.

## [waiting_weeks] The Waiting Weeks
*Day 25 — Friday, March 27, 2026 (dayOffset 25)*

Reconsideration is read by people, on their schedule, in a queue of other people's emergencies. The weeks pass at preschool speed: Fern learns to write her name with the letters in an order of her own choosing, the clearance cycle at the center ticks one notch closer, and your director — who has the dates in her schedule book because you gave them to her — says only, "Paper's moving, then," when you pass in the hall.

You check the mailbox the way everyone in this story checks the mailbox: like it owes you money. On day forty, it pays.

**Choices:**
- Open the envelope from the Secretary's office → **answer_letter**
  - NOTE (shown after choosing): Thick envelope. Thick is good. Denials are traditionally one page.

## [answer_letter] The Answer, On Paper
*Day 40 — Saturday, April 11, 2026 (dayOffset 40)*

The Secretary's order arrives on day forty. You read it standing at the mailbox, the way all important reading in this story gets done.

The reconsideration is GRANTED. The order says, in the flat language of bureaus, that the final order did not address material evidence contained in the agency's own packet, and that the matter is returned for a new hearing at which the complete record — including the pediatrician's follow-up letter — will be considered. The indicated report is not erased today. The registry entry stands while the new hearing is pending. But the decision that kept it there has been un-decided, by the system, on paper, because of a page you carried into the right office inside the right fifteen days.

**Choices:**
- Call the clinic and start preparing for the new hearing → **hearing_prep**
  - NOTE (shown after choosing): "Now we build the hearing the first one should have been," Ms. Delvecchio says. "Starting with the whole file — which, you may recall, somebody requested in writing."

## [hearing_prep] Preparing the Hearing That Should Have Been
*Day 47 — Saturday, April 18, 2026 (dayOffset 47)*

The complete investigation file arrives because it was requested in writing weeks ago. In it, fairly read, is the whole story: the first examination, the playground aide's incident note, and the follow-up letter that reconciles them. Preparation is not dramatic. It is a timeline on one page, the letter tabbed, the incident note tabbed, your own account written in your own words while it is still yours to write.

At the preschool, your director has the new hearing date in the schedule book, because you told her the truth with dates in March.

**Choices:**
- Walk into the new hearing with the complete record → **end_recon**
  - NOTE (shown after choosing): Whatever the hearing officer decides this time, it will be decided about the whole file. That was the fight. It is already won.

## [end_recon] Ending — A New Hearing, On the Whole Record
*Day 55 — Sunday, April 26, 2026 (dayOffset 55)*

The new hearing is not shown; this story ends where its real work ended — at the moment the system agreed to decide again, this time about everything. The indicated report remains in place pending that hearing, and the hearing officer could rule either way on the complete record. Sylvie keeps her folder, her dates, and her job conversation honest and current.

What changed is the ground: the Bureau's decision no longer rests on a partial record, because one parent read the last page of an order, counted fifteen days correctly, and carried one unconsidered page into the right office in time.

**ENDING — Debrief:**

THE WIN, NAMED HONESTLY — This is a partial win, and it is the best this story offers. The reconsideration was granted and a new hearing ordered; the report was NOT expunged by this ending, and no ending in this scenario expunges it — that decision belongs to the new hearing, on the complete record.

THE LAW IN THE BEATS — The two windows come from 23 Pa.C.S. § 6341(g): within 15 calendar days of the mailing date of the Bureau's final order, a party may request reconsideration by the Secretary or appeal; and within 30 calendar days of the mailing date, an appeal to Commonwealth Court must be perfected. Asking for reconsideration does not extend the court clock — which is why the clinic calendared both from day one. The evidence packet's arrival reflects the agency's duty under § 6341(c.2)(4) to provide a person making an appeal with the investigation evidence, including potentially exculpatory evidence. The complete-file request rests on 55 Pa. Code § 3130.44(d): agency records are released upon request.

THE HIGHEST-LEVERAGE MOVE — The written record request (§ 3130.44(d)), made at the clinic table before anyone knew whether it would matter. The complete file is what the new hearing will now be fought over.

WHAT NO STRATEGY CONTROLS — The Secretary could have denied reconsideration; hearing officers weigh evidence as they find it; employers make their own decisions on their own cycles. The route controlled only what was Sylvie's: the dates, the filing, the page, the folder. Outcomes also turn on workers, officials, and luck — never on whether a parent deserved better.


## [court_filed] The Longer Road
*Day 20 — Sunday, March 22, 2026 (dayOffset 20)*

The notice of appeal to Commonwealth Court is filed inside its thirty days, and it is a real filing — the court will read the case. But a court on appeal reads the record that was made below: the transcripts, the packet as it stood, the Bureau's reasoning. It does not take new evidence, and the pediatrician's follow-up letter — sitting in your folder, unread by any deciding body — is not something the court can weigh.

Your lawyer is honest on the courthouse steps: "We can argue the Bureau misread what it had. We cannot argue about the letter. On appeal, it does not exist."

**Choices:**
- Take the appeal forward on the record that exists → **end_court**
  - NOTE (shown after choosing): The appeal proceeds. It will be decided about a smaller record than the one in your folder.

## [end_court] Ending — The Court Reads a Smaller Record
*Day 90 — Sunday, May 31, 2026 (dayOffset 90)*

The appeal runs its course on the record as it stood when the Bureau ruled: no follow-up letter, no second examination weighed, because no filing ever put them in front of a deciding body. The court reviews what the Bureau had — and reviews the Bureau's reading of it deferentially. The report stands.

The door Sylvie chose was a real door. It was simply the one that could not carry the page that mattered. The reconsideration window — fifteen days, printed on the last page of the order — closed on March 17, while a stronger argument waited in a kitchen drawer and then in a folder, unfiled.

**ENDING — Debrief:**

WHY THIS ENDING — An appeal to Commonwealth Court under 23 Pa.C.S. § 6341(g) must be perfected within 30 calendar days of the mailing date of the Bureau's final order, and the court reviews the existing record; it does not receive new evidence. The reconsideration request — the only route that could put the unconsidered letter in front of a decision-maker — had to be filed within 15 calendar days of the same mailing date. Filing the appeal did not preserve the letter, and skipping reconsideration spent the only window that could use it.

THE LAW THAT WAS AVAILABLE — Same § 6341(g) clocks; the agency's duty to provide the investigation evidence, § 6341(c.2)(4); and the record release on request, 55 Pa. Code § 3130.44(d). All three were in the story. Only the clocks were used.

WHAT NO STRATEGY CONTROLS — Nothing in this ending turns on Sylvie's worth as a parent. It turns on which of two printed windows a piece of paper was carried through, and when. The system is not described as cruel here; it is described as literal — which, on day sixteen, amounts to the same weather.

