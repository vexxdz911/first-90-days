# STRATEGY — Scenario 18: “The Paternity Question”

*Game documentation for a fictional simulation. This page describes how to play “The First 90 Days,” Scenario 18, in this scenario only. It is general information about a game, not legal advice, and it is not a guide to any real case.*

*This route was verified by walking the finished `scenario-18.json` choice graph programmatically — every choice listed below is the actual edge in the data, and the path reaches the named ending.*

## (1) The win

**Ending — A Documented Role, and a Path** (`end_documented`)

Be honest about what this is: it is a **partial win, and the best this scenario offers**. At the Monday, June 15, 2026 review, the father gets a documented role — scheduled contact on a defined, expanding structure — and a stated path toward placement or expanded involvement, to be measured against the record at the next review. It is **not** placement on June 15, and it is not a promise that placement follows. In this scenario, a late-noticed father can earn the next step; he cannot skip to the last one. Any strategy page that sold this ending as “father gets his daughter back” would be overselling it.

## (2) The route

Key decision points in order. Node titles and choice texts are exactly as they appear in `scenario-18.json`.

1. **The Letter That Came Late** (`start`) — Choose: *“Write back this week — a short letter saying who you are, that you received the notice, and that you want to be involved — and keep a copy.”* Changes: cash −6; sets `fatherWritten`; adds a hidden file item (his dated written response). The win stays open only if the file stops being empty in week one.
2. **A Name She Did Not Have an Address For** (`mom_notice`) — Choose: *“Write it down for the worker: the name she gave, that she had no address, what she fears, and the boundaries she is asking for.”* Changes: sets `motherWroteEarly`; adds a hidden item. Mother's account and boundaries enter the record in her own words instead of someone else's summary.
3. **Showing Up on Paper** (`father_reply`) — Choose: *“Put your phone, address, work hours, and visit availability in writing, and file your copy in the folder.”* Changes: cash −4; sets `contactInWriting`; adds a hidden item. His availability becomes plannable-around.
4. **Asking for Counsel, in Writing** (`father_counsel`) — Choose: *“Send the written request for counsel and keep the stamped or dated copy.”* Changes: cash −4; sets `counselAsked`; adds a hidden item. Counsel arrives with weeks to work, not hallway minutes.
5. **Sunday Visit, Steady Ground** (`mom_visit`) — Choose: *“Ask the worker, in the visit note, that any new contact be structured and scheduled — and keep her copy.”* Changes: sets `motherBoundariesWritten`; adds a hidden item. The structure the final order later uses starts here, in her note.
6. **The Shift Schedule Problem** (`father_work`) — Choose: *“Send the work-and-transport page to the worker now, before any appointment is set.”* Changes: cash −4; sets `workInWriting`; adds a hidden item. His constraints read as planning instead of surfacing later as excuses.
7. **Mother Asks for the Record** (`mom_records`) — Choose: *“Sign the written record request under § 3130.44(d) and keep the copy.”* Changes: sets `recordsRequested`; adds a hidden item. This is the records hinge of the scenario.
8. **The Dates Change the Math** (`father_dates`) — Choose: *“Request the record in writing too, then rebuild your plan around the real dates.”* Changes: cash −6; sets `recordsRequested` and `sawDates`; adds two hidden items. Seeing the notice and service-plan dates replans both parents around the real clock.
9. **Boundaries, Written Kindly** (`mom_boundaries`) — Choose: *“File the boundaries statement and keep the copy in her own folder.”* Changes: sets `motherBoundariesFiled`; adds a hidden item. Her position becomes findable by a judge who has never met her.
10. **Availability, Again — Because People Change** (`father_availability`) — Choose: *“Resend updated contact and availability in writing to the new worker.”* Changes: cash −4; sets `contactUpdated`; adds a hidden item. His information survives the worker rotation.
11. **Forty Minutes, Supervised** (`first_contact`) — Choose: *“Thank the worker in writing afterward, confirm you want the next contact, and file the visit note.”* Changes: cash −4; sets `visitFollowedUp`; adds a hidden item. The first contact becomes findable evidence, not just an event.
12. **What Stability Actually Looks Like** (`mom_stability`) — Choose: *“Send her written update — progress, the contact she heard went well, and her boundaries restated once, calmly.”* Changes: sets `motherUpdateFiled`; adds a hidden item. Mother documents her own progress and acknowledges the father's first step, in writing.
13. **Follow-Through Is a Repetition** (`father_follow`) — Choose: *“Keep the rhythm: written confirmation before, written thanks after, every time.”* Changes: sets `followThrough`; adds a hidden item. Repetition, not a single good visit, is the argument.
14. **The Week the Schedule Broke** (`setback`) — Choose: *“Notify the worker in writing before the contact, attach the posted schedule, and offer two alternative days.”* Changes: cash −18; sets `conflictNotified`; adds a hidden item. The one conflict reads as reliability under pressure instead of becoming an unexplained gap.
15. **Mother Writes the Review Before It Happens** (`mom_writing`) — Choose: *“Finish her written review statement and deliver it to the worker and her counsel before the review.”* Changes: sets `motherReviewReady`; adds a hidden item. Her statement arrives early enough to be read.
16. **The Worker Reads the Folder Back** (`worker_checkin`) — Choose: *“Ask what, specifically, will be in the report to the court — and write down her answer, dated.”* Changes: sets `askedReportContents`; adds a hidden item. No surprises: he knows what the court will see.
17. **Assembling the Packet** (`packet_build`) — Choose: *“Finish the packet with counsel's help and deliver copies in advance of the review.”* Changes: cash −12; sets `packetDelivered`; adds a hidden item. Delivered early, the packet is homework the court can actually do.
18. **Mother's Last Page Before the Review** (`mom_packet`) — Choose: *“Deliver her final update in advance and go into the review with her folder complete.”* Changes: sets `motherPacketComplete`; adds a hidden item. Both folders are complete before anyone enters the room.
19. **The Folder, Weighed** (`the_folder`) — Choose: *“Present the full packet: documented involvement, structured expansion, placement path to be built on this record.”* Changes: routes to the strong track (`strong_deliver` → `mom_strong` → `review_strong`); the other two endings close. This is the fork — it only pays off because steps 1–18 built the folder this choice claims exists.

**Verified path (node IDs, in order):** `start → mom_notice → father_reply → father_counsel → mom_visit → father_work → mom_records → father_dates → mom_boundaries → father_availability → first_contact → mom_stability → father_follow → setback → mom_writing → worker_checkin → packet_build → mom_packet → the_folder → strong_deliver → mom_strong → review_strong → end_documented`

Total cash spent on this route: −62 (of the 210 start), all of it in father's-track nodes — copies, postage, and the rescheduled-conflict trip.

## (3) Why this wins — the law as it is supposed to work

Only two verified legal principles do work in this scenario, and the route uses both exactly as written:

- **Counsel — 42 Pa.C.S. § 6337.** A party is entitled to representation by legal counsel at all stages of the proceedings, and if he is without financial resources or otherwise unable to employ counsel, to have the court provide counsel for him. In this scenario the father asks **in writing, in May**, so counsel exists in time to order the packet, size the ask to the record, and present dates instead of adjectives. The scenario states no narrower eligibility rule than the statute's own words.
- **Records on request — 55 Pa. Code § 3130.44(d).** The case record “shall be released upon request.” In this scenario **both** parents request it in writing (`mom_records` sets `recordsRequested`; `father_dates` sets it again from the father's side). What the record gives them is dates — notice dates and service-plan dates that are not the same — and seeing those dates changes what each parent does with the remaining weeks. That is the regulation working as intended: a parent cannot respond to a timeline they have never been allowed to read.

Everything else on the route is not law at all. It is the discipline the law's design quietly assumes: if hearings decide on a record, then the family's share of the outcome is the quality, timing, and completeness of what they put into that record — dated, copied, in advance, in writing.

## (4) The traps

1. **“Wait until you can go in person and explain everything properly”** (`start`). Tempting because it feels more sincere. It costs the only thing the father cannot replace — the first dated page. The detour through `father_wait` is recoverable if he sends the letter on day 2, but a player who keeps choosing the verbal, in-person, later option arrives at June 15 as testimony about intentions, which is the `end_thin` record.
2. **“Call the number and give the details verbally” / “introduce yourself by phone”** (`father_reply`, `father_availability`). Tempting because it is faster and friendlier. It costs survivability: workers rotate in this scenario, and verbal contact and availability leave with the notebook. Every unwritten step is a step the file — and therefore the judge — never sees.
3. **“Miss it and explain at the next contact”** (`setback`). Tempting because the visits have gone well and goodwill feels like credit. It costs the order of the paper: an explanation dated *after* a gap reads as an excuse, while the same facts sent *before* read as reliability. This single reversal is the difference between the strong folder and a folder with a hole in it.
4. **At `the_folder`, presenting the full packet on a thin record — or bringing one copy on the day** (`packet_build` / `the_folder`). Tempting because the ask is the exciting part. It costs credibility: a full-packet presentation the folder cannot support collapses under a judge reading dates, and a packet delivered on the day is a packet nobody has read. The honest middle ask at `the_folder` — continue supervised and structured while the record grows — leads to `end_supervised`, which is a durable partial outcome, not a failure; overselling a thin folder risks worse.

## (5) What no strategy controls

This route maximises what the parents control. It does not control the rest, and in this scenario the rest is substantial: which worker holds the case and whether she rotates at the worst moment; a supervisor's posted schedule and a bus route's detour; how a particular judge weighs a short, well-documented record against a much older case clock; the child's own pace, which no order can hurry; and plain luck — the packet read in full the week before, or first opened on the bench. The published cases behind this composite include fathers who did much of this and still lost ground, and the scenario's other endings exist because a perfect May does not guarantee a particular June 15. What the strategy buys is not the ruling. It buys the strongest possible version of the only thing a family actually owns in this system: the record the ruling is made from.

---

*Draft game documentation — not legal advice. Companion files: `scenario-18.json` / `scenario-18-script.md`. The family is a fictional composite built only from published public-record opinions; no real person's case appears here.*
