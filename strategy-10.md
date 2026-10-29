# Strategy Guide — Scenario 10: “The Wrong Form” (Foundation tier)

*Game documentation for a fictional simulation in* The First 90 Days. *It describes choices and outcomes inside this scenario only — general information, not legal advice for any real case.*

## The win

**One Digit, Fixed in Writing** (`end_good`) — the best ending reachable in this scenario. It is a partial, honest win: The win is stated honestly: this is not a key in a door. It is a verified place on the list, a file that explains its own six-week stall, and a confirmation with four true lines — the strongest position this process offers a family still waiting, which is what 'winning' looks like at this tier.

## The route

- **The Packet, Requested** (`records`) → choose: “File the written request for the full referral packet” — Sets recordsRequested. Your copy is the only audit this referral was ever going to get — the worker’s caseload is forty-one families.
- **Eleven Pages** (`prep`) → choose: “Circle the error and write the correction out: wrong number, right number, where to verify it” — Sets errorSpotted: 4185 vs. 4815, with the proof identified. A correction with its evidence attached travels further than a correction alone.
- **Deliver It, or Describe It** (`split`) → choose: “Deliver the written correction in person and get a stamped copy” — Sets correctionFiled before the day-14 list review — the one clock in the scenario. Delivered paper amends the referral; a phone call amends a case note.
- **Trust, and Verify the Other Building** (`p2`) → choose: “Call the housing office and confirm the corrected ID is on the review list” — Sets verifiedDownstream. The agency’s fix and the housing office’s list are different buildings; the route checks both.
- **The Second Error, Caught Cheaper** (`p5`) → choose: “Get the corrected confirmation in writing, then sign and return it” — The final gate: proofreading the confirmation catches the second error (unit size) while it is still a phone call, not a refused offer.

Path check: this route was walked programmatically through the scenario's choice graph (start → start → n2 → records → prep → eve → split → p1 → p2 → p3 → p4 → p5 → end_good) and reaches `end_good`. Verified at generation time; the graph validation for this scenario reported no errors.

## Why this wins — the law as it is supposed to work

- 55 Pa. Code § 3130.44(d): the referral packet — all eleven pages, including page four — is released on request. The entire route grows from that right: you cannot correct a document you have never seen, and no one else in this story had both the copy and the motive to read it closely.
- The list review itself is the housing office's process, not a statutory clock, and this guide claims nothing more for it. What the verified record right changes is which version of your family the process reviews: the ghost under 4185, or the household under 4815.

## The traps

- **Deliver It, or Describe It** (`split`) → “Phone it in — read the correction to Ms. Lindqvist and trust the note” — Costs the review. The note is right and the referral stays wrong; the win survives only through the in-person filing at u2 — by u4, the same filing only repairs the record for the next review.
- **Trust, and Verify the Other Building** (`p2`) → “Assume the re-sent referral updated the list automatically” — Costs the verification: you drop to the passed-over track at u3 with a corrected agency file and an uncorrected list.
- **The Second Error, Caught Cheaper** (`p5`) → “Let the unit size go — one bedroom beats no bedroom” — Closes the win after it was earned: your signed confirmation blesses the wrong unit size, and the eventual one-bedroom offer becomes your problem to explain.
- **The Correction, Eventually Filed** (`u4`) → “File the correction but skip the explaining — being right is enough” — Declines the record repair: the correction lands, but the file keeps reading "pending since spring," as though the family were the delay.

## What no strategy controls

The list moves at its own speed, the worker carried forty-one families, and the housing office's nightly matching is nobody's malice — it is a machine faithfully failing to find a family that was never entered correctly. A human review step might have caught the ghost; a different office loses stamped corrections. No strategy controls the queue, the caseload, or the algorithm. It controls whether the paper those things act on has your right number on it.
