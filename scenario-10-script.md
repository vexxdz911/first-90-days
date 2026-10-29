# THE FIRST 90 DAYS — Scenario 10: “The Wrong Form” (Foundation tier)

*Human-readable script. This document and `scenario-10.json` are generated from a single source and match node-for-node: same IDs, same order, same choices, same effects.*

**The family is fictional — a composite. No real person's story appears here.**

**Content note:** This scenario depicts a housing referral stalled by a transposed digit in an ID number, and a list-review deadline. There is no graphic content. Players may skip any scene or use the quick exit at any time.

**How to read effects:** `cash −4` changes the player's cash. `FLAG: name` sets a flag the engine tracks. `HIDDEN + item` means the case file quietly records that item at this choice — the player does not see it when it happens. `NOTE:` is text shown to the player right after choosing.

Start date: Monday, June 1, 2026. Day offsets are days since the scenario's start date. Starting cash: $125.

## [start] The Referral That Stalled
*Day 0 — Monday, June 1, 2026 (dayOffset 0)*

Your daughter Alba is six, and the two of you are living in your sister's spare room while you wait for housing help — a support referral, filed months ago, that is supposed to move you toward a unit of your own. It has been 'in process' so long that 'in process' has become the family's address.

Today your caseworker, Ms. Lindqvist, calls with news that is almost good: the housing support office has your referral, but it is 'stalled in verification.' She does not know why. Stalls, in her experience, are usually a detail. Details, in yours, are usually findable — if you can see the paper.

**Choices:**
- Ask what "verification" needs, and what paper it is looking at → **n2**
  - NOTE (shown after choosing): A stall with a specific cause can be fixed. A stall with a vibe cannot.
- Ask her to check again next week → **n2**
  - NOTE (shown after choosing): Next week is when stalled things are traditionally checked again, and found still stalled.

## [n2] A Number With a Name
*Day 1 — Tuesday, June 2, 2026 (dayOffset 1)*

Verification, it turns out, means the housing office is matching your referral to your case record using the case ID number — the one number that follows your family through every system — and the match keeps failing.

A failing match has a short list of causes, and most of them are typos with consequences. Ms. Lindqvist promises to 'look when she can.' Her caseload, you happen to know, is forty-one families deep.

**Choices:**
- Ask for a copy of the referral packet, so you can check it yourself → **records**
  - NOTE (shown after choosing): Forty-one families deep means your eyes are the fastest available audit.
- Leave it to her — she knows the system → **records**
  - NOTE (shown after choosing): She does. The system also knows her caseload, and schedules accordingly.

## [records] The Packet, Requested
*Day 2 — Wednesday, June 3, 2026 (dayOffset 2)*

You put it in writing, the short dated note that has become this family's superpower: a request for a copy of the complete referral packet as sent to the housing office.

When it comes, you will be able to do the one thing nobody with forty-one cases has time to do — read your own referral like a proofreader, because your housing depends on it in a way it depends on no one else.

**Choices:**
- File the written request for the full referral packet → **prep**  _(FLAG: recordsRequested; HIDDEN + Records — parent requested a copy of the complete housing referral packet)_
  - NOTE (shown after choosing): Under 55 Pa. Code § 3130.44(d), the record is released on request. The packet arrives in three days, eleven pages, with a paperclip that has seen things.
- Wait for Ms. Lindqvist’s next check instead → **prep**
  - NOTE (shown after choosing): Her next check happens in nine days. It consists of being told the referral is still stalled.

## [prep] Eleven Pages
*Day 3 — Thursday, June 4, 2026 (dayOffset 3)*

Page one is fine. Page two is fine. Page four is where it lives: the case ID, typed by a human in a hurry — 4185 — where your number, the one on your plan, your letters, your folder, is 4815. Two digits, holding hands in the wrong order.

The housing office's computer has been looking for family 4185 for six weeks. Family 4185 does not exist. Your family does — it is simply filed under a number that isn't yours, in a queue that does not move for ghosts.

**Choices:**
- Circle the error and write the correction out: wrong number, right number, where to verify it → **eve**  _(FLAG: errorSpotted; HIDDEN + Error — transposed digits in case ID identified by parent from her own copy)_
  - NOTE (shown after choosing): Wrong: 4185. Right: 4815. Proof: your plan, page one, and every letter the agency ever sent you.
- Call Ms. Lindqvist and read her the digits over the phone → **eve**
  - NOTE (shown after choosing): Digits read aloud are digits that can be mis-heard — 4815 and 4185 sound like cousins, which is the entire problem in miniature.

## [eve] The List Review
*Day 4 — Friday, June 5, 2026 (dayOffset 4)*

There is a date that gives this small error its teeth: the housing office reviews its list on Monday, June 15, 2026. Referrals verified by then go forward for placement matching. Referrals not verified wait for the next review — six weeks later — regardless of whose typo it was.

Alba is asleep in the spare room that is not hers, in the house that is not yours, patient as only a six-year-old who has never known the system to move fast can be. The correction needs to travel before the list does.

**Choices:**
- Prepare the correction tonight, in writing, with a copy of page one attached → **split**  _(FLAG: correctionDrafted)_
  - NOTE (shown after choosing): One page: the error, the fix, and the proof, paper-clipped to the truth.
- Sleep — the call tomorrow will sort it → **split**
  - NOTE (shown after choosing): Tomorrow’s call is to a woman with forty-one families. Sorting is not scheduled.

## [split] Deliver It, or Describe It
*Day 5 — Saturday, June 6, 2026 (dayOffset 5)*

Morning. The correction is one page long. The agency office is on the bus line you already ride. Ms. Lindqvist's phone number is also right there, and phones are free, and describing one page takes ninety seconds.

But a described correction becomes a note about a correction. A delivered correction becomes the correction itself, stamped, in the file, findable by the next set of hands.

**Choices:**
- Deliver the written correction in person and get a stamped copy → **p1**  _(cash −4; FLAG: correctionFiled; HIDDEN + Correction — written correction of case ID filed; stamped copy to parent)_
  - NOTE (shown after choosing): Stamped, copied, filed. The referral now carries the right number in the agency’s own hand, with your proof clipped behind it.
- Phone it in — read the correction to Ms. Lindqvist and trust the note → **u1**  _(HIDDEN + Correction — case ID correction reported verbally; no written correction received)_
  - NOTE (shown after choosing): She writes it on the case note. The referral form itself — the thing the housing office actually reads — is a different document, in a different queue.

## [p1] Re-Filed
*Day 7 — Monday, June 8, 2026 (dayOffset 7)*

Ms. Lindqvist calls within two days, sounding like a woman who has found the pea under the mattress. The referral is corrected and re-sent; the housing office confirms the match now works — family 4815, verified, in the queue with its real name on it.

'You caught that from your copy?' she asks. 'Page four,' you say. 'Nobody reads page four,' she says. 'I do now,' you say.

**Choices:**
- Ask for written confirmation that the corrected referral was re-sent → **p2**  _(FLAG: confirmationAsked)_
  - NOTE (shown after choosing): It comes by email: corrected referral transmitted, verification match successful. Into the folder it goes, behind the stamped correction.
- Take the good news on the phone → **p2**
  - NOTE (shown after choosing): The news is genuinely good. Its proof currently lives in a phone call.

## [p2] Trust, and Verify the Other Building
*Day 8 — Tuesday, June 9, 2026 (dayOffset 8)*

One building believes the number now. The question — the same question as every story in this tier — is whether the fix has traveled to the building that acts on it: the housing office's list, compiled by hands that never saw your folder.

The list review is on Monday, June 15, 2026. Verification there is a phone call away, and the person who answers has your (correct) number.

**Choices:**
- Call the housing office and confirm the corrected ID is on the review list → **p3**  _(FLAG: verifiedDownstream; HIDDEN + Verification — parent confirmed corrected ID on the housing review list)_
  - NOTE (shown after choosing): "4815, yes — verified, on the list for the fourteenth." She reads it off her screen. Both buildings now agree on who you are.
- Assume the re-sent referral updated the list automatically → **u3**  _(HIDDEN + Verification — parent did not confirm the list carried the corrected ID)_
  - NOTE (shown after choosing): Lists are compiled by people from transmissions received. Transmissions received is a category with a history.

## [p3] On the List
*Day 10 — Thursday, June 11, 2026 (dayOffset 10)*

You are on the list — which is not a unit, not a key, not a moving date. It is the list. Families wait on it for months, and this scenario will not insult you by pretending otherwise. But the list only moves for the verified, and you are, as of this week, verifiably on it.

Ms. Lindqvist updates the case note: referral active, family awaiting matching. She reads you the note because, by now, that is the custom between you.

**Choices:**
- Ask her to include how the stall was resolved — error found and corrected from your copy → **p4**  _(FLAG: storyInFile)_
  - NOTE (shown after choosing): She does. The note now explains the six weeks instead of letting them look like silence.
- Let the note say "referral active" and leave it at that → **p4**
  - NOTE (shown after choosing): "Active" is true. It is just not the whole truth, and the whole truth was flattering this time.

## [p4] Before the Review
*Day 12 — Saturday, June 13, 2026 (dayOffset 12)*

Two days before the list review, a letter comes from the housing office: a standard pre-review confirmation — name, household, case ID, unit size sought. Four lines of fact about your family, to be confirmed by your signature and returned.

Four lines is few enough to read like a formality and exactly enough to contain one more error.

**Choices:**
- Read all four lines like a proofreader — name, household, number, unit size → **p5**  _(FLAG: confirmationRead)_
  - NOTE (shown after choosing): Name right. Household right. Number right — 4815, in friendly type. Unit size: it says one bedroom. Alba is six. It should say two.
- Sign and return it — the number is fixed, that was the point → **p5**
  - NOTE (shown after choosing): The number was the point until the unit size became the point. Errors travel in families too.

## [p5] The Second Error, Caught Cheaper
*Day 14 — Monday, June 15, 2026 (dayOffset 14)*

The unit-size line is wrong the way these things are wrong: Alba's age was entered as her household size, or something like it, somewhere upstream. It is fixable with one phone call today — because today it is a pre-review confirmation, not a placement offer for the wrong apartment.

You make the call, reference your confirmation letter, and watch the fix happen in the only way fixes are ever really watched: by asking for the corrected version.

**Choices:**
- Get the corrected confirmation in writing, then sign and return it → **end_good**  _(FLAG: readBeforeSigning)_
  - NOTE (shown after choosing): Two bedrooms, right number, right names. You sign the truest four lines in the whole file, and keep the copy that proves it.
- Let the unit size go — one bedroom beats no bedroom → **end_partial**
  - NOTE (shown after choosing): It does, until the offer arrives for a one-bedroom, your acceptance is expected in days, and declining it needs explaining to people who have your signed confirmation saying one was right.

## [end_good] One Digit, Fixed in Writing
*Day 16 — Wednesday, June 17, 2026 (dayOffset 16)*

**ENDING.** Debrief:

- The win is stated honestly: this is not a key in a door. It is a verified place on the list, a file that explains its own six-week stall, and a confirmation with four true lines — the strongest position this process offers a family still waiting, which is what 'winning' looks like at this tier.
- The law inside this story: under 55 Pa. Code § 3130.44(d), the referral packet was released on request. The transposed digits were findable by exactly one person with time to look — the person whose housing depended on them — and she could only look because she had the copy.
- Notice the repeated shape: file the correction in writing, get the stamp, then verify the fix in the other building. Systems do not share corrections telepathically. They share them when someone carries the paper across.
- Honesty requires this: the housing office might have caught the error at review, or never; lists move at speeds no parent controls; a different worker buries the stamped correction for a month. You cannot set the queue's pace. You can make sure that when your name is called, it is called under the right number.

## [u1] A Note About a Correction
*Day 7 — Monday, June 8, 2026 (dayOffset 7)*

Ms. Lindqvist is glad you called — genuinely; forty-one families and she still answers like a person. She notes the digits in the case note and promises to pass them along to whoever handles referral amendments.

Whoever handles referral amendments is, this month, covering two desks. The case note is not the referral. The referral — eleven pages, page four still wrong — sits in the housing office's queue, being matched, nightly and automatically, against a family that does not exist.

**Choices:**
- Ask for the amendment in writing — offer to bring the correction in yourself → **u2**
  - NOTE (shown after choosing): Offering to carry your own correction is not pushiness. In a system this loaded, it is logistics.
- Wait — she said she’d pass it along → **u2**
  - NOTE (shown after choosing): She will, when the desk is covered and the day allows. The list review does not have a day-allows policy.

## [u2] The Quiet Days
*Day 8 — Tuesday, June 9, 2026 (dayOffset 8)*

Days pass the way they pass in spare rooms: slowly and on someone else's schedule. The list review is on Monday, June 15, 2026, and verification still fails, nightly, automatically, in a building that has never heard your voice.

Ms. Lindqvist, reached at last, is frank: the amendment never got attached. The case note says the right number. The referral says the wrong one. Both statements are true, and only one of them is in the queue.

**Choices:**
- Bring the written correction in today, with page one of your plan attached as proof → **p3**  _(FLAG: correctionFiled; HIDDEN + Correction — written correction filed in person after verbal report failed)_
  - NOTE (shown after choosing): Stamped at the desk, re-sent the same afternoon. The housing office confirms the match within the day — the review, just barely, will see the right number.
- Ask her to please handle it this week, as a favor → **u3**  _(HIDDEN + Correction — parent relied on verbal handling; referral still uncorrected near review)_
  - NOTE (shown after choosing): Favors are real and she owes you one and neither fact attaches a document to a referral.

## [u3] The Review Passes
*Day 15 — Tuesday, June 16, 2026 (dayOffset 15)*

The list review comes and goes on Monday, June 15, 2026. Somewhere in it, referrals are verified and move forward. Yours is not among them — not rejected, not decided against, simply not matched, the bureaucratic equivalent of a letter never arriving.

At the next visit, the summary reads: 'Referral pending verification since spring.' Since spring. As if the number had been shy.

**Choices:**
- Show her your copy of page four — the digits, circled → **u4**
  - NOTE (shown after choosing): Her face does something honest. "You had this the whole time?" You did. Having it and filing it turned out to be different verbs.
- Ask when the next review is, and sit down to wait for it → **u4**
  - NOTE (shown after choosing): Six weeks. Waiting is now the plan, because waiting is what is left when a deadline passes unarmed.

## [u4] The Correction, Eventually Filed
*Day 16 — Wednesday, June 17, 2026 (dayOffset 16)*

The fix, when it comes, looks exactly like the fix in February would have — one page, in writing, stamped, with page one attached. Ms. Lindqvist files it herself this time, walks it to the right desk, and confirms the match by phone while you are still in the building.

It takes one afternoon. It would always have taken one afternoon. The cost was never the afternoon.

**Choices:**
- Keep the stamped copy and the confirmation, and ask that the file explain the stall → **u5**  _(FLAG: storyInFile; HIDDEN + Correction — written correction filed and confirmed; stall explained in the record)_
  - NOTE (shown after choosing): The note goes in: error located by parent, corrected, verified. Whatever the next review decides, it will decide about the real family, under the real number.
- File the correction but skip the explaining — being right is enough → **u5**
  - NOTE (shown after choosing): Being right is enough for you. The file, unexplained, still reads "pending since spring" to everyone who meets it cold.

## [u5] Six Weeks
*Day 18 — Friday, June 19, 2026 (dayOffset 18)*

The next review is six weeks out. Alba will start the school year from your sister's spare room — registered, finally, under the right number, which is not nothing and is not a home.

Your folder, at least, is complete now: the packet, the error, the correction, the confirmation. It arrived at completeness by the expensive road.

**Choices:**
- Put the folder where the next set of hands can find it → **end_partial**
  - NOTE (shown after choosing): Next time — and systems like this always schedule a next time — the paper starts ahead of the problem.

## [end_partial] Still Waiting on a Number
*Day 20 — Sunday, June 21, 2026 (dayOffset 20)*

**ENDING.** Debrief:

- The correction was made, verified, and filed — one review too late. The family remains on the list under the right number, which matters and is not the win: the win was the June review, and June is gone. Alba stayed with you throughout; what the wrong digit cost was six weeks of a childhood spent in a spare room, and a file that reads 'pending since spring' as if the family, not the number, had been hard to find.
- The law inside this story: under 55 Pa. Code § 3130.44(d), the packet was yours on request — and it was, from the first week. The difference between the two endings is not access. It is that a correction described on a phone becomes a note, while a correction delivered becomes an amendment.
- Digits are the smallest possible unit of this system's respect for a family: get them wrong and you are a ghost; get them fixed, in writing, and you are a household again.
- Honesty requires this: Ms. Lindqvist was overloaded, not careless in spirit, and she walked the correction through herself in the end. Another worker never returns the call; a housing office with a human review step catches its own ghost. You cannot staff the desks. You can be the person who reads page four.
