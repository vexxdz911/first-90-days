# Strategy Guide — Scenario 26: "The Incarcerated Father"

*Game documentation for a fictional simulation ("The First 90 Days," Scenario 26). This guide describes choices inside the scenario only. It is general information about how the simulation is built — not legal advice for any real case.*

*Route verified by walking `scenario-26.json` programmatically from its start node, choice by choice: 24 edges, reaching the named ending (see the path check reported with this guide's delivery).*

## (1) The win

**Ending — Home With Mother, Paper Intact** (`end_return`)

State it honestly: this is a partial win, and for a father playing from inside a correctional facility it is the best one this scenario contains. The children go home — to their mother, Dana, on a trial return — and your rights are intact. Your contact continues, and a services-and-visitation plan for you is written into the order now, for your release. You do not go home in this ending. Your sentence clock never moved, and the guide will not pretend a folder could move it. What you won is that the return order did not erase you — because the record gave the court a father it could see, name, and preserve on paper.

The runner-up ending, **Ending — The Exception, Documented as to Father** (`end_exception`), is also a genuine win on your own track: the services-not-provided exception is documented as to you and no petition is filed as to Father at the fifteen-month point, while the case continues toward Dana. The route below beats it for the family as a whole because the children actually go home.

## (2) The route

Key decision points, in order (node titles), the winning choice at each, and what it changes:

1. **The First Letter** — *"Ask the court, in writing, for appointed counsel and for notice of every hearing"* (cash −5). Sets `counselAsked`; hidden: your dated counsel/notice request enters the file. Every later build depends on having counsel (Ms. Hart) early.
2. **Asking for the File From Inside** — *"Sign it, date it, copy it, and send the records request this week."* Sets **`recordsRequested`**. Opens the `records_packet` node: you learn the file says "no contact" for weeks that predate your notice, and that your service referrals were never sent — knowledge no other route gives you this early.
3. **What the Updated File Shows** is reached via **Asking Again, on Purpose** — *"Send the second records request — referrals, responses, and review notes named in it"* (cash −5; sets `recordsRequested` + `updatedRecord`). This is the record hinge: the updated file contains the agency's own note that your services "remain unavailable" with "no alternative arrangement made" (sets `servicesGapDocumented`). Without this node, the strategy and review scenes run on summaries and memory.
4. **The Request Is the Record** — *"Send it to the agency and Ms. Hart, dated, and file your copy"* (cash −10). Sets `fatherRequests`; hidden: dated written requests for the parenting program, the evaluations, and child contact. This converts what you asked for at a facility window into provable facts with dates.
5. **A Month of No Answer** — *"Write one short follow-up — 'following up on my letter' — with both dates in it"* (cash −5). Sets `followUpSent`. The follow-up is what turns the agency's silence into a bracketed, dated gap instead of a sad story.
6. **Dana's Hard Month** — *"Write Dana a short, decent letter — support her plan, ask about the children, keep a copy"* (cash −5). Sets `supportLetter`. In the win ending this letter sits near the front of the return packet; it is part of why the court preserves your place instead of treating the parents as opponents.
7. **Your Copy, Their Copy** — *"Pay for copies and keep the log current, every month, without exception"* (cash −15). Sets `logKept`; hidden: a continuous dated log of letters, requests, replies, and silences. Reconstructions from memory fail at the final review; this log does not.
8. **Dana's Track, Again** — *"Write the agency: you support the children's return to Dana, and you ask for your contact and release plan in writing"* (cash −5). Sets `supportReturn`. Your support becomes a filed fact before the final review, not a sentiment expressed during it.
9. **Choosing What to Build** — *"Build the return packet — Dana's progress first, your paper relationship preserved inside it."* Sets `returnPacket` and routes you through **The Return Packet** → **The Final Review — Dana's Hearing, Your Pages** → the win ending. Choosing the exception packet here instead routes to `end_exception` (the runner-up); the other two builds close the win (see Traps).

Supporting beats on the route (single-choice or low-risk nodes): keep the late-notice envelope and postmark at **What the Pages Say** (hidden item: late notice preserved); join the parenting waiting list and keep the slip at **What This Building Offers**; write to the children through the caseworker at **A Hearing, by Video**.

Total cash spent on the route: about $45 of your $140 start — stamps, cards, and copies. Cash is never the binding constraint in this scenario; dates are.

## (3) Why this wins — the law as it is supposed to work

Only principles from the scenario's verified set are used:

- **Right to counsel.** A party in these proceedings is entitled to representation, with counsel provided if the party cannot afford it (42 Pa.C.S. § 6337). The route exercises that right in writing, in week eight, rather than discovering it in month twelve — counsel is the multiplier on every later paper move.
- **The record is requestable.** A parent's case record "shall be released upon request" (55 Pa. Code § 3130.44(d)). The route uses this twice: early, to learn that the file mis-describes your silence and omits your referrals; and late, to surface the agency's own note about the services gap. The right does not shrink because the request is mailed from a facility, and it does not exercise itself.
- **The ASFA clock has documented exceptions.** At fifteen of the most recent twenty-two months in care, the agency's duty to file a termination petition arises unless an exception is documented (42 U.S.C. § 675(5)(E)) — a relative caring for the child, a documented compelling reason, or services the plan identified as necessary for safe return that the agency did not provide. The win route does not need to win the exception argument as to Father, because Dana's documented progress resolves the children's track first — but the father's documented services gap is in the packet, which is what lets the court address his track on facts instead of on a summary. (Note what the route does *not* claim: it never treats the agency's service failures as an element of any termination ground. The services point lives only inside the § 675(5)(E) filing exception, which is where the scenario — like the statute — keeps it.)
- **A filing is not a termination.** Had a petition been filed, grounds would still have to be proved by **clear and convincing evidence** at a hearing. The route's object is to keep that hearing from being scheduled on a thin record — or, as in the win, to make it unnecessary.
- **Timely process is part of the design.** The children's shelter care hearing was held within 72 hours (42 Pa.C.S. § 6332; 23 Pa.C.S. § 6315(d)) — before the father's notice even arrived. The scenario's premise is that a system which moves that fast on paper can also be answered on paper, and the route is simply that answer, kept up for fifteen months.

## (4) The traps

1. **"Wait — a caseworker will sort it out" (The First Letter).** Costs you the written counsel request and weeks of the only currency you have. The file records the wait in its own words: *no contact*. Menus of later choices narrow from here.
2. **Asking verbally at records / windows (Asking for the File From Inside; The Request Is the Record).** Each verbal ask feels cheaper and kinder, and each one routes you through the summaries version of the story: you never see the "no contact" entries, the blank referrals, or the agency's gap note, so at **Ms. Hart Draws the Clock** your lawyer is building from your memory. The exception and return packets both weaken; the thin ending becomes likely.
3. **"Keep it in your head" (Your Copy, Their Copy).** Skipping the log saves $15 and loses the case's spine. At **The Final Review — Summaries** the agency's lawyer asks, reasonably, where your requests are in the file — and honest memory without documents loses to a one-line summary.
4. **"Let the file speak as it sits" (Choosing What to Build).** The final trap is fatigue dressed as dignity. It routes directly to **Ending — Filed as to Both, a Thin File Noted** (`end_filed`): petitions filed as to both parents at the fifteen-month point, on summaries, with Dana's track weakened by the support that existed in life but never on paper.

## (5) What no strategy controls

The video connection holding. A program seat opening in your unit, or a transfer wiping out your place on its list. Whether Dana's recovery and housing hold in a given month — the largest single fact in the win ending is another person's year going well. Which judge reads the packet, how the assigned worker writes summaries, and postal luck in both directions. And above all, your sentence timeline: no letter, log, or packet in this scenario moves it by a day, and every ending is shaped by that.

As the scenario's debriefs state: outcomes in cases like this turn on workers, judges, and luck as well as on anything a parent does. The route above does not control the outcome. It controls the only thing the player was ever actually holding — what the record says when the clock arrives.
