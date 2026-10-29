# STRATEGY — Scenario 17: “The Empty Apartment” (Hard)

*Game documentation for a fictional simulation in “The First 90 Days” (Tactic Watch). Everything below describes choices and mechanics **in this scenario** only. It is general information about how the simulation is built, not legal advice, and not guidance for any real case.*

*Route verified by walking `scenario-17.json` programmatically: every choice named below exists on its node, and the node sequence reaches the named ending. Verified path (node IDs, in order):*
`start → inspection_day → the_list → records_request → landlord_clock → triage → hardware_run → hot_water_letter → shift_trade → dated_photos → visit_planning → receipt_folder → reinspect_request → prep_thorough → plumber_day → worker_check → extension_talk → money_crunch → records_arrive → packet_night → reinspection_day → result_pass → movein_prep → transition_weekend → end_repaired`
*(Starting cash $260; cash on this route ends at $187 after the hardware run −$38, the extra shift +$60, folder copies −$12, and the reserved extension fee −$45 — the fee envelope is set aside even though, on this route, the extension is never needed.)*

---

## 1. The win

**Ending — Repairs Verified: Move-In and Reunification Proceed** (`end_repaired`)

Honestly stated: this is a complete win *inside the scenario's own frame* — the reinspection verifies all four items in one visit, the clearance is signed (with a dated copy in the parent's hand), the overnight and the move finish inside the lease hold, and the reunification that was “approved in principle” at the start becomes actual, on schedule. It is not oversold here because the scenario itself does not oversell it: the ending's debrief notes that it also required a plumber who came when promised, an inspector with a morning slot, and a landlord whose word held — none of which the player's choices control. What the winning route guarantees is narrower: that no delay in the month can honestly be recorded as the parent's.

## 2. The route

Key decision points, in order. Node titles are exactly as named in the data.

1. **The Inspection** (`inspection_day`) — *Ask, before she leaves, exactly how each fix will be verified.* Changes: nothing mechanical — it sets up the scenario's real question (verification, not repair) and leaves every ending open.
2. **Get It in Writing** (`the_list`) — *Tape the printed summary inside your folder and work from it.* Changes: sets flag `hasWrittenList`; hidden item: the dated four-item inspection summary enters the file.
3. **Ask for the Record** (`records_request`) — *Send the written request today, naming the inspection material and the service-plan pages, and keep your dated copy.* Changes: sets flag `recordsRequested`; hidden item: the written record request under 55 Pa. Code § 3130.44(d). This is what makes the later `records_arrive` packet possible — the parent reads the same pages the agency reads.
4. **Two Kinds of Fix** (`triage`) — *Split the list in writing: your three items to buy, the hot water to the landlord in writing.* Changes: sets flag `splitList`; routes each item to its owner, so the landlord's item can never be recorded as the parent's unfinished work.
5. **The Hardware Store** (`hardware_run`) — *Photograph each finished fix, keep the itemized receipt, and file both the same night.* Changes: cash −$38; flag `boughtSupplies`; hidden items: the dated, itemized receipt and the dated photos of the three completed fixes.
6. **The Hot Water Is Not Yours to Fix** (`hot_water_letter`) — *Send the hot-water request in writing today, quoting the inspection item and the February 4 hold date.* Changes: flag `landlordWritten`; hidden item: the dated written repair request — the document that later gives the plumber's delay (or promptness) an author who is not the parent.
7. **Photographs With Dates** (`dated_photos`) — *Build the dated photo set — yours fixed, the hot water honestly still waiting — and back it up in two places.* Changes: flag `datedPhotos`; hidden item: the dated photo set, including honest documentation of the still-unfixed landlord item.
8. **The Folder Learns to Travel** (`receipt_folder`) — *Assemble the full folder and print a copy set.* Changes: cash −$12; flag `folderComplete`; hidden item: the assembled repair folder (summary, receipts, labeled photos, both written requests, in order).
9. **Ask for the Reinspection — in Writing** (`reinspect_request`) — *Send the written reinspection request today — items, fixes, and the February 4 hold date stated — and file your copy.* Changes: flag `reinspectWritten`; hidden item: the dated written reinspection request. **This is the route's main fork:** it leads to `prep_thorough` (the inspector logs the request, notes the dated photos, and holds a morning slot). The phone-call alternative leads to `prep_thin` and makes the clean verification ending much harder to reach.
10. **The Plumber's Morning** (`plumber_day`) — *Send the dated hot-water photo and the plumber's invoice copy to the agency the same afternoon, in writing.* Changes: flag `hotWaterDone`; hidden items: the plumber's invoice copy and the dated hot-water photo — the fourth item becomes verifiable before the inspector arrives.
11. **A Visit That Is Not an Inspection** (`worker_check`) — *Walk him through the folder page by page.* Changes: hidden item: a caseworker note that cites documents and dates rather than impressions — the note later readers will quote.
12. **Insurance, in Writing** (`extension_talk`) — *Get the offered extension terms noted in a short written message today.* Changes: flag `extensionPriced`. On the winning route this insurance is never used — but it is what keeps the middle ending (`end_extended`) open if verification slips, instead of dropping straight to the lost lease.
13. **February Is Already Spoken For** (`money_crunch`) — *Set aside the extension fee in an envelope marked with its purpose.* Changes: cash −$45; flag `feeReserved` — the extension, if needed, can actually be paid for.
14. **The Reinspection** (`reinspection_day`) — *Walk her item by item with the folder open — each fix matched to its dated photo, receipt, or invoice, in her order.* Changes: flag `verifiedClean`; leads to `result_pass` (“Cleared”). This is the choice the whole route is built to make possible: verification at the speed of paper.
15. **Cleared** (`result_pass`) → **Boxes in a Cleared Apartment** (`movein_prep`) → **The Overnight** (`transition_weekend`) → the ending. Changes: hidden item: the signed, dated reinspection clearance; the transition staircase and the move complete inside the hold, and February 4 arrives as a moving date rather than a deadline.

## 3. Why this wins — the law as it is supposed to work

Only principles from the scenario's verified set are used, and this scenario needs exactly one of them as law:

- **Records on request — 55 Pa. Code § 3130.44(d).** In this scenario the parent asks, in writing, for the case record — the inspection material and the service-plan pages — and the record is released upon request, as the regulation provides (“shall be released upon request”). The principle as the scenario teaches it: the file is always being written; a written request does not change the file, it changes who gets to read it before decisions are made, so parent and agency argue from the same pages. That is the one cited legal mechanism in Scenario 17, and it appears in the `records_request` beat, the `records_arrive` beat, and every ending's debrief.
- **The lease deadline is not a statutory clock — and the scenario says so, in the story and in every debrief.** The governing date, Wednesday, February 4, 2026, is the landlord's lease-hold/move-in deadline: a practical, contractual deadline set by the lease, not by any statute, court order, or agency rule. No verified legal principle is claimed for it, deliberately. The honest framing the scenario teaches is that the *remedy follows the source of the clock*: a statutory clock is answered with a filing; a landlord's clock is answered with a signature — an extension agreed **in writing** — and confusing the two wastes time. Everything else in the scenario (inspections, reinspection requests, receipts, photographs) is kept generic and uncited on purpose: it is documentation practice inside a fiction, not a statement of law.

## 4. The traps

Tempting choices that close — or nearly close — the win:

1. **Phoning the reinspection request instead of sending it in writing** (`reinspect_request` → `prep_thin`). The call feels faster and friendlier. It costs: no logged date, no item list in the file, no advance written warning of the February 4 hold, and no held slot — the inspector never calls you back with a morning held. The clean one-visit verification in `result_pass` is built on the paper that this choice never creates.
2. **Letting the inspector re-check from memory at the reinspection** (`reinspection_day` → `result_partial` — “let her re-check the rooms while the folder waits in the other room”). Everything *is* fixed on this branch; that is the trap's cruelty. It costs the signed clearance: items observed but not documented cannot be signed off, the clearance is held, and the parent is pushed onto the landlord branch (`landlord_answer`) where the best remaining outcome is the delayed middle ending — and only if the extension was pre-negotiated.
3. **Asking the landlord for the hot-water repair face-to-face instead of in writing** (`hot_water_letter`, verbal option). A warm yes at a store counter costs the dated proof that the landlord was told early. If the plumber is then slow, the record cannot show whose delay it was — and in this scenario, unattributed delay reads as the parent's.
4. **Skipping the early extension conversation** (`extension_talk`, “trust that the reinspection will land in time”). It costs the insurance policy: if verification slips for any reason — including reasons that are not traps at all, just other people's calendars — February 4 arrives with no priced, pre-agreed extension, and `landlord_answer`'s verbal plea leads to `end_lost`, the lost lease.

## 5. What no strategy controls

This route controls the record. It does not control the people. In this scenario, the plumber might not have come on the promised morning; the inspector's slots are finite and other families are waiting in the same queue; the caseworker returned from leave when he returned; the landlord had a waitlist, a ledger, and full discretion over an unsigned hold — his courtesy extended exactly as far as his paper said it did, and no strategy obliges a landlord to be generous. Transition visits depended on a foster family's calendar and a child's ordinary, unremarkable afternoons going well. A different inspector, a reassigned worker, a back-ordered heating element, or a landlord who sold the building in January could each have moved this same folder, played perfectly, to the extension ending or the lost-lease ending — both of which the scenario writes as respectable outcomes that the documentation still improves (a signed extension; a repair record that opens the next housing attempt). The honest claim for the winning route is only this: it makes the parent's part of the record early, dated, and complete, so that whatever the month decides, it is not decided *because the paper was missing*. Workers, landlords, inspectors, and luck decide the rest — in this scenario, and by design.

---

*Draft game documentation — fictional simulation, general information only, not legal advice. Companion files: `scenario-17.json` / `scenario-17-script.md`.*
