# Strategy Guide — Scenario 2: “The Indicated Letter”

*Game documentation for a fictional simulation. “In this scenario” means in the scenario’s data and debriefs. This is general information, not legal advice for any real case.*

## 1. The win

**“Ending — The Letter Comes Out of the File.”**

The indicated report is amended/expunged on the scenario’s hearing record, the narrator’s name comes out of the statewide database, and the preschool may restore her to the toddler room. State the result honestly: this is **not** a finding that the hearing rewound February and proved exactly how Theo fell. It is a finding that the agency did not carry its burden on the evidence presented.

The recommended route is the **paper path**. A testimony-centered route also reaches this ending and was graph-checked, but it leaves more of the result riding on live composure under cross-examination.

## 2. The route

1. **The Letter with the Seal** — Choose **“Read the whole letter again, slowly, with a pen.”** You find the amendment/expungement right instead of treating the letter as only a threat.
2. **What the Letter Actually Says** — Choose **“Tell Mrs. Calloway at the center before she hears it any other way.”** The 90-day date is circled, and your employer hears the problem from you first.
3. **The Policy Binder** — Choose **“Thank her, and ask for the leave dates in writing.”** The employment consequence becomes dated paper rather than an oral warning.
4. **Twelve Cots** — Choose **“Go to the clinic on Wednesday.”** This gets counsel involved while most of the 90 days remain.
5. **The Clinic at the Library** — Choose **“Write the request this week, with her help filling in the form.”** The written appeal is filed on day 12 of 90 in the story, preserving the hearing.
6. **The Receipt in Your Wallet** — Choose **“Learn about the quieter door.”** The timely appeal is already moving; this opens the separate record-request branch.
7. **Your Own File** — Choose **“Write the request and send it this week.”** This sets `recordsRequested` and brings the investigation file into your hands before the agency’s hearing packet arrives.
8. **Sunday at Your Sister’s** — Choose **“Wait for the file you requested — it is due any day.”** You give the request time to produce the document the rest of the case will be built around.
9. **Reading What Was Written About You** — Choose **“Take the packet to Ms. Park and build the hearing around what it actually says.”** You find both the load-bearing “varied” line and Dr. Anand’s one-line note on page six.
10. **The Agency’s Evidence** — Choose **“Ask Ms. Park the only question that matters now: how do we build our side of the scale?”** You stop rehearsing innocence in the abstract and start assembling admissible, weighable evidence.
11. **Two Ways to Build** — Choose **“Build the paper case.”** Paper becomes the spine: it does not get tired, rattled, or trapped by one word.
12. **The Pediatrician’s Letter** — Choose **“Ask him to sign the full letter, and take an unpaid morning to collect it yourself.”** Cash falls by $40 and `medLetter` is set; a one-line chart note becomes a full explanation of why the injury pattern fits the playground equipment.
13. **The Climber and the Slide Are One Thing** — Choose **“Print the photographs, three angles, date-stamped, with a one-line caption each.”** This sets `photos`; the photographs show that “climber” and “slide” name parts of one structure.
14. **The Exchange** — Choose **“Send copies of everything, with a list, and keep the mailing receipt.”** This sets `disclosed`; the agency cannot plausibly keep the central photographs out as a surprise.
15. **The Hearing, Paper Path** — Choose **“Rest on the packet — let the paper say it, in order, without wobbling.”** You avoid adding a live wording variation to a case that turns on an alleged variation, and the route reaches expungement.

## 3. Why this wins — the law as it is supposed to work

- **The appeal right is real only inside its window.** Under **23 Pa.C.S. § 6341(a)(2)**, the written request to amend or expunge must be made within 90 days of notification. Filing early preserves the hearing and leaves time to build the record.
- **Your own file is not a favor.** Under **55 Pa. Code § 3130.44(d)**, the record “shall be released upon request.” The early request reveals the pediatrician’s favorable line while it can still shape the hearing.
- **The agency must disclose its evidence.** Under **23 Pa.C.S. § 6341(c.2)(4)**, the department or county agency must provide all evidence gathered during the investigation that is relevant to the determination, including potentially exculpatory evidence. The strategy uses that evidence instead of guessing at it.
- **The burden belongs to the agency.** Under **23 Pa.C.S. § 6341(c.2)(5)**, the department or county agency “shall bear the burden of proving by substantial evidence that the report should remain categorized as an indicated report.” The scenario’s debrief quotes **23 Pa.C.S. § 6303**: substantial evidence must outweigh inconsistent evidence. The full pediatrician letter and the structure photographs add weight to the inconsistent side.
- **Disclosure is part of fairness in this scenario.** Evidence the other side has never seen can be kept out. Sending the packet with a list and receipt makes the strongest proof available to be weighed.
- **The process gives the hearing officer a record, not a character contest.** The winning packet narrows the dispute to two medical readings and one playground structure. Three years of good work matter less than whether the agency’s proof about one afternoon outweighs the contrary evidence.

## 4. The traps

- **Leaving the letter in the drawer** is the quiet loss. If the drawer stays closed through the deadline, the route reaches **“Ending — The Drawer Stays Closed”**; the right was not denied on the merits—it expired untested.
- **Skipping the separate record request** does not stop the appeal, but it costs the early discovery of page six. You would be preparing around the summary’s “varied” line without knowing the file already contains a favorable pediatrician note.
- **Holding the photographs back for surprise** attacks the paper route at its strongest point. In this scenario, unseen evidence can be excluded; an unshown photograph proves nothing.
- **Testifying on the paper path and answering “the slide” before “the climber”** recreates the very wording problem the packet was built to neutralize. That choice leads to **“Ending — The Report Stays.”**

## 5. What no strategy controls

A hearing officer still weighs credibility and competing medical opinions. The urgent-care doctor’s caution, the caseworker’s lack of independent memory, and the hearing officer’s reading of the same packet are not player-controlled. Another officer could weigh the evidence differently. The strategy changes what the scale must hold; it does not guarantee how a human being balances it.

**Path check:** PASS. The JSON walk follows the 15 choices above from `start` to `end_expunged`, **“Ending — The Letter Comes Out of the File.”** Final tracked cash: $170. Key flags set: `recordsRequested`, `medLetter`, `photos`, and `disclosed`. The alternate testimony route was also walked programmatically to the same ending in 13 choices.
