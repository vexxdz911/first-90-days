# Strategy Guide — Scenario 64: "Fifteen Months of Paper"

*Game documentation for a fictional simulation in "The First 90 Days" (Tactic Watch). The family, the case, and every choice below are fictional. This guide is general information about how the scenario is built — it is not legal advice for any real case.*

## (1) The win

**Best ending: "Ending — Not Filed: The Exception, Documented."**

State it honestly: this is a **PARTIAL** win, and the scenario labels it that way in its own debrief. The agency documents the services-not-provided exception and does not file a termination petition at the fifteen-month date, and a transition plan toward home is ordered. Amara is **still placed** at the curtain. Nothing about termination grounds was decided, because there is no petition — the exception speaks only to the filing decision, and that is all this ending decides. There is no ending in this scenario where February reunifies the family.

## (2) The route

Verified by walking the scenario graph from the start node (see the verification note at the end). The full walked route, with the decision points explained:

1. **Month Ten, Quietly** → **The Folder, Inventoried** → **The Date in Pencil** — Mr. Sandoval names the date: Amara was placed Monday, November 3, 2025; fifteen of the most recent twenty-two months arrives **Wednesday, February 3, 2027**.
2. **Three Lines on a Legal Pad** — counsel states the exception and its discipline in plain words: record-dependent, filing-decision only.
3. **Asking for the File** — *Sign the written request for the complete record this week.* Cash −6. Sets **recordsRequested**. The chronology's silences become readable.
4. **Reading the Chronology** → **Three Gaps, Three Questions** → **A Thin Binder, Labeled in Pencil** — the three services are separated: program (eight-week silence), therapy (referral sent, re-sent six weeks later), housing (applications complete; the list is the list).
5. **The Program Remembers Differently** — *Ask, in writing, for a reprint of the waitlist notice with your dates on it.* Cash −4. Sets **waitlistDoc**. The month-2 eight-week waitlist now exists on the program's letterhead.
6. **Eight Weeks, on Letterhead** → **The Bus Home, Thinking in Dates** → **The Referral That Went Nowhere** — *Ask for a copy of the closed-intake letter, with its date.* Cash −4. Sets **therapyDoc**. The first referral went to a provider whose intake had closed; the letter proves it.
7. **Six Weeks, with an Author** → **The List Is the List** — *Assemble the dated application copies into one stamped set.* Cash −5. Sets **housingDoc**. Housing claims no gap; it forecloses the delay being re-described as hers.
8. **Tab Three** → **The Call About Tab Three** → **The Log, in Your Hand** — *Build the log from the documents only — every entry checkable.* Cash −6. Sets **gapLog**. The dated services-gap log exists as an exhibit, not a claim.
9. **The Rest of the Plan, Kept** → **The Shift Supervisor's Signature** → **The Month-Twelve Review Approaches** → **Month Twelve, on the Record** — her own completions stay current and fair on the record (screens clean, visits kept, program finished late-but-finished); the exception is deliberately not yet raised.
10. **Saturday, Month Twelve** → **The Folder, the Night Before the Letter** → **The Letter** — the agency writes that it will weigh filing at the fifteen-month date, on the case record.
11. **The Packet Decision** → **Three Ways, One Chosen** — *Assemble and file the written services-exception packet with counsel.* Cash −10. Sets **packetFiled**. This choice is flag-gated: it is only available with **gapLog** + **recordsRequested** both set.
12. **Filed, Stamped, Copied** → **Month Thirteen, at Work** → **A Call from the Foster Home** → **The Month-Fourteen Review Approaches** → **Month Fourteen, on the Record** — the packet is referenced by exhibit; the February date is named on the record.
13. **A New Supervisor Reads Cold** — the tremor the whole route was built for: the filing decision will be signed by a reader who knows only what the file says. The packet is in it.
14. **The Week Before** → **Two Days Out** → **The Fifteenth Month** — the filing-decision node lands exactly on dayOffset 156 = Wednesday, February 3, 2027. *The decision rests on the filed packet — the exception, documented, with its letters and dates.* This choice is flag-gated: **packetFiled** + **waitlistDoc** + **therapyDoc**. It leads to **Ending — Not Filed: The Exception, Documented**.

## (3) Why this wins — the law as it is supposed to work

Only principles from the scenario's verified set are stated here:

- **The ASFA filing point and its documented exceptions.** At 15 of the most recent 22 months, the agency is generally to file a termination petition UNLESS an exception is documented: (i) the child is being cared for by a relative, (ii) a documented compelling reason that filing would not serve the child, or (iii) the agency has not provided services it identified as necessary for the child's safe return (42 U.S.C. § 675(5)(E)). This route builds exception (iii).
- **The exception's limits, stated exactly.** The services exception is **record-dependent** — it is an argument that exists only to the extent the file documents identified-but-not-provided services. It speaks to the **filing decision** only. A petition, if filed, must still be proven by **clear and convincing evidence** at a hearing — and no scenario in this series decides such a hearing or states any termination outcome. The packet wins, at most, the decision not to file; it decides nothing else, and the guide claims nothing else for it.
- **The record is obtainable on request** — 55 Pa. Code § 3130.44(d) ("shall be released upon request"). Step 3 is that right exercised in writing; without it, the chronology's gaps stay invisible.
- **Counsel** throughout is the parent's right (42 Pa.C.S. § 6337; appointed counsel where applicable, § 6332(a)) — here used for its least dramatic function: assembling documents into a filing before a dated decision is made from the file.

## (4) The traps

1. **Trusting memory at "The Program Remembers Differently"** (no **waitlistDoc**). The eight-week wait stays true and unprovable. At "The Fifteenth Month" the best-ending choice closes; a filed packet on a thinner base leads to **Ending — Filed, With the Record Complete**. The mirror gap lands in the same place: a packet carrying the waitlist letter but not the therapy record (**waitlistDoc** without **therapyDoc**) is likewise filed on a thinner base, and February weighs exactly the paper there is.
2. **Skipping the provider's letter at "The Referral That Went Nowhere"** (no **therapyDoc**). Same mechanism, second service: the six-week referral gap loses its author, and the packet's strongest pair of documents becomes one.
3. **Building the gap log from memory at "The Log, in Your Hand"** (no **gapLog**). The packet choice at "Three Ways, One Chosen" is flag-gated on the documented log — it never appears. The remaining choices are the oral raise and waiting.
4. **Raising the exception orally** (sets **oralRaised** instead). The argument is made clearly, in full sentences, on a transcript — with no exhibits beneath it. The filing decision, made on the file, leads to **Ending — Filed, Over a Thin File**: argued from memory, and the file cannot carry it.
5. **Waiting** (no packet, no oral raise). Progress fairly reported, and nothing filed to answer the date: **Ending — The Date Arrives Anyway**. The date does what dates do.

## (5) What no strategy controls

The new supervisor's reading of the same packet — a different cold reader files anyway, and the route's paper then travels into a harder proceeding as the documented exception in **Ending — Filed, With the Record Complete**. The program's printing habits, the provider's record-keeping, the foster family's kindness, the judge's calendar, and plain luck all hold pieces of every ending here. The route controls only this: whether the gaps everyone agreed happened were documented, checkable, and already in the file when a stranger read it cold. Outcomes in this system turn on workers, supervisors, judges, and luck as much as on any parent's choices — and never on the parent's worth.

---
*Verification: this route was walked programmatically against `scenario-64.json` — each named choice was followed from the start node in order; every intermediate node and choice exists; every flag-gated choice's requirements (gapLog + recordsRequested at the packet; packetFiled + waitlistDoc + therapyDoc at the filing decision) were satisfied by flags set earlier on the walk; the filing-decision node was verified at dayOffset 156 = Wednesday, February 3, 2027 (placement Monday, November 3, 2025 + 15 calendar months, recomputed in the generator and asserted); the walk terminates at the ending node titled "Ending — Not Filed: The Exception, Documented" after visiting 36 nodes, with $135 of the $170 starting cash remaining. Walked path: start -> folder_inventory -> counsel_meet -> exception_explained -> records_beat -> file_review -> chronology_gaps -> binder_begins -> prog_beat -> prog_letter -> bus_home64 -> therapy_beat -> therapy_letter -> housing_beat -> housing_docs -> sandoval_call -> gaplog_beat -> screens_beat -> work_beat64 -> review12_notice -> review12 -> amara_visit -> folder_night64 -> agency_letter -> counsel_packet -> packet_decision -> packet_filed_scene -> month13_work -> foster_call -> review14_notice -> review14 -> supervisor_change -> filing_eve -> morning_of -> filing_day -> end_notfiled.*
