# THE FIRST 90 DAYS — Scenario 107: “The Card That Stopped”

*Human-readable script. This document and `scenario-107.json` are generated from a single source and match node-for-node: same IDs, same order, same choices, same effects.*

**The family is fictional — a composite. No real person's story appears here.**

**Content note:** This scenario depicts a mother whose daughter is in kinship care with an aunt (a placement that predates the story): a benefits card that declines at a checkout, a closure notice mailed to a previous address, call centers, written corrections, a case-record request, and a meeting, told through calls, letters, and file pages. There is no graphic content. Players may skip any scene or use the quick exit at any time.

**How to read effects:** `cash −40` changes the player's cash. `FLAG: name` sets a flag the engine tracks. `HIDDEN + item` means the case file quietly records that item at this choice — the player does not see it when it happens. `REQUIRES FLAG: name` means the choice is only available if that flag was set earlier; `REQUIRES NO FLAG: name` means it is only available if that flag was never set. `NOTE:` is text shown to the player right after choosing.

Start date: Monday, April 6, 2026. Day offsets are days since the scenario's start date. Tier: Foundation.

## [start] A Full Cart, a Dead Card
*Day 0 — Monday, April 6, 2026 — Monday, April 6, 2026 (dayOffset 0)*

Your name is Camille. Your daughter Zora is seven, and three weeks ago — on Monday, March 16, 2026 — she went to stay with her aunt, in kinship care, while this case runs. The placement is not what this story is about. The grocery store is.

You moved in January, and before the move was a week old you told your caseworker the new address — on Monday, January 26, 2026 — and she wrote it down while you watched. As far as you knew, the system had it. Systems, plural, is a distinction you are about to pay tuition on.

Tonight the cart is full, the line behind you is patient in the way lines are not, and the cashier says it gently: your benefits card has been declined. Not short. Not partial. Declined — as if the household it feeds had been switched off.

**Choices:**
- Leave the cart, keep the receipt slip, and call the number on the back of the card in the morning → **call_maze**
  - NOTE (shown after choosing): The slip says only that the card was declined. Slips are terse. The reason, when you find it, will be a sentence about a letter you never saw.

## [call_maze] The Number on the Back of the Card
*Day 2 — Wednesday, April 8, 2026 — Wednesday, April 8, 2026 (dayOffset 2)*

You call on Wednesday, April 8, 2026, and the call-center maze does what mazes do: menus, music, a hold long enough to fold laundry inside — and finally a person, reading a screen you cannot see.

The screen says your case was closed for failure to respond. A closure notice was mailed, the voice says, asking for a response by the date printed on its face. No response came back, so the case closed. The voice is not unkind. The voice also cannot tell you, at first, where the notice was mailed.

You never saw a notice. You say so — and the voice, to its credit, goes looking for the address the notice was sent to.

**Choices:**
- Stay on the line until the voice reads you the exact address the notice was mailed to → **two_systems**  _(HIDDEN + Closure — recorded as failure to respond to a mailed closure notice)_
  - NOTE (shown after choosing): Exact addresses matter more than explanations. This one is about to explain everything, including why you never had a chance to respond.

## [two_systems] The Old Address, Read Aloud
*Day 4 — Friday, April 10, 2026 — Friday, April 10, 2026 (dayOffset 4)*

The address the voice reads on Friday, April 10, 2026 is your previous address — the apartment you left in January. The notice went there, waited there, and was waited on there: the response the office was expecting was being expected at a home you no longer live in.

You gave the new address to your caseworker on Monday, January 26, 2026, and she wrote it in the case file while you watched — the file entry is dated Monday, February 9, 2026. But the case file and the benefits office are two systems, and an address handed to one of them is not, automatically, an address held by the other. Nobody told you that. It is the most important sentence in this story, and it was never said to you at all.

Tonight the correction can travel the way the news has travelled so far — by phone, from voice to voice — or it can travel on paper, to both systems, with dates on it.

**Choices:**
- Correct the address in writing to BOTH offices, ask in writing for the notice to be re-sent, and attach a dated written statement of the facts → **written_moves**  _(cash −4; FLAG: addressCorrected; HIDDEN + Address — corrected in writing to both the benefits office and the agency; re-send of the notice requested in writing)_
  - NOTE (shown after choosing): Four dollars of copies and postage across two envelopes. The statement is six lines long: moved in January; new address given on the date you gave it; notice never received; card declined at the checkout. Dated, signed, copied.
- Call both offices and correct the address out loud — faster, and both of them sounded helpful → **phone_only**
  - NOTE (shown after choosing): Faster is real. Both voices were helpful. What neither voice can give you is a copy of the correction with a date on it.

## [written_moves] Two Envelopes
*Day 7 — Monday, April 13, 2026 — Monday, April 13, 2026 (dayOffset 7)*

By Monday, April 13, 2026 both envelopes are in the mail and a copy of each is in your folder: the address correction, sent to the benefits office and to the agency; the written request that the closure notice be re-sent to the address you actually live at; and your statement of the facts, with its dates in order.

Written things answer back in writing, slowly. The benefits office replies with a letter confirming the new address now stands on its file. The agency confirms the same. Two systems, one address — and, for the first time, dated paper in both places saying so.

What neither reply does, by itself, is reopen anything. The closure still stands on its own paper: failure to respond. Paper answers paper. You are going to need the rest of the file.

**Choices:**
- Keep both confirmations with the statement, and get through the weeks ahead → **waiting_weeks**  _(HIDDEN + Address confirmations — both offices confirmed the corrected address in writing)_
  - NOTE (shown after choosing): Your folder now holds the correction twice over, once from each system. The closure letter's version of you is still the only version the benefits file leads with.

## [phone_only] Corrected, Out Loud
*Day 7 — Monday, April 13, 2026 — Monday, April 13, 2026 (dayOffset 7)*

Both calls go well. The benefits worker is brisk and kind: she updates the address as you speak it, or says she does, and tells you the closure can be looked at. Your caseworker says she has had the new address all along — which is true, in her system — and that she will pass it along.

At the end of the day your address is corrected in the world of voices. In the world of paper, nothing you can hold has changed: no confirmation, no dated statement, no copy of anything. If the closure is ever argued about in a room, the argument will be your memory of two pleasant calls against a file that says failure to respond.

**Choices:**
- Get through the weeks ahead on careful shopping, and keep calling to check → **waiting_weeks**
  - NOTE (shown after choosing): Checking by phone produces more phone calls. Each one feels like progress. None of them can be attached to anything.

## [waiting_weeks] The Weeks the Card Stayed Dead
*Day 10 — Thursday, April 16, 2026 — Thursday, April 16, 2026 (dayOffset 10)*

The weeks are arithmetic now: smaller carts, careful lists, help you did not want to need. Zora's aunt covers what Zora needs at her house. What has stopped is the household support for the part of the household still at home with you — and it has stopped over a letter sent to an empty apartment.

A scored assessment form is part of cases like yours — filled in from visits and notes, rating what it can see. What it can see this month is a household under strain. Why the strain arrived — a notice, an old address, two systems that do not share one — is not a box on the form. It is a fact living in two envelopes, or in two phone calls, or nowhere.

**Choices:**
- At the next home visit, ask what the file currently says about the address and the closure → **flyer_beat**
  - NOTE (shown after choosing): Your caseworker checks and tells you, honestly: her file has had the new address since the entry you watched her make. It is the other file you have never seen.

## [flyer_beat] The Flyer in the Folder
*Day 14 — Monday, April 20, 2026 — Monday, April 20, 2026 (dayOffset 14)*

In the waiting room at the agency office there is a folder of flyers for parents, and one of them — the kind of paper most people walk past — says something you read twice: a parent may request their case record, and under 55 Pa. Code § 3130.44(d) the material “shall be released upon request.”

Your record. The address pages, the chronology, the notes — including the entry you watched your caseworker make in January, with its date on it. The flyer is not offering you a rescue. It is offering you the other system's own handwriting.

**Choices:**
- Take the flyer home and think about what the case file's address pages would show → **records_fork**
  - NOTE (shown after choosing): If the entry is dated the way you remember, the file itself — not your memory of it — can say when the system first held your new address.

## [records_fork] Ask for the File, or Don’t
*Day 16 — Wednesday, April 22, 2026 — Wednesday, April 22, 2026 (dayOffset 16)*

The request is simple and it is yours to make: ask, in writing, for your case record — the chronology, the address entries, and the notes about the placement and the household. Under 55 Pa. Code § 3130.44(d), the record is to be released on request; the asking is a right, not a favor, and it leaves a date behind.

Or you can wait for the meeting the closure will eventually get, and explain the two systems there, out loud, to people reading a file you have never seen.

**Choices:**
- Put the request in writing — chronology and address entries — and keep a copy → **packet_arrives**  _(cash −3; FLAG: recordsRequested)_
  - NOTE (shown after choosing): Three dollars of copies and postage across the errand. The request is dated, copied, and kept with the confirmations.
- Wait for the meeting — you can explain the two systems in person → **no_packet**
  - NOTE (shown after choosing): In person is how the address travelled the first time: told to a person, written in one file, lost between systems. The explanation deserves a better vehicle this time.

## [packet_arrives] The File’s Own Hand
*Day 21 — Monday, April 27, 2026 — Monday, April 27, 2026 (dayOffset 21)*

The packet arrives, and you turn to the address pages first, the way you would check a signature. There it is, in the case file's own entries: your new address, recorded on Monday, February 9, 2026 — entered from the conversation of Monday, January 26, 2026, before Zora's placement, long before the card stopped.

The system's own paper proves the sequence. The address was given, and written down, in the agency's file, in good time. The benefits office never got it, and mailed the one letter that mattered to the apartment you had left. The closure for failure to respond was built on a response being waited for at the wrong home.

Now you have seen both files' versions of you. The question is what paper will be sitting on the table when the two versions are finally in one room.

**Choices:**
- Keep the packet with the statement and the confirmations — they belong in the same folder, in date order → **closure_stands**  _(HIDDEN + Case file packet — agency file shows the new address recorded weeks before the closure)_
  - NOTE (shown after choosing): Statement, two confirmations, and the file's own dated entry. Your folder and the closure letter now disagree about the same spring, in writing, with dates.

## [no_packet] What You Cannot Quote
*Day 21 — Monday, April 27, 2026 — Monday, April 27, 2026 (dayOffset 21)*

Without the packet, you cannot quote the entry you watched being made — its exact wording, its exact date — and you cannot show the meeting a page from the system's own file. You remember the conversation clearly. Memory, unattached, is the currency this case has already devalued once.

Your account is true, detailed, and sincere. At the meeting, it will be weighed the way spoken accounts are weighed in rooms that run on attachments: personally, politely, and against a printed closure letter that says less and therefore somehow says it louder.

**Choices:**
- Go on toward the meeting with your account — and keep every confirmation you do have → **closure_stands**
  - NOTE (shown after choosing): Whatever paper exists still exists. The meeting is weeks away, and weeks are where sentences harden.

## [closure_stands] Failure to Respond
*Day 35 — Monday, May 11, 2026 — Monday, May 11, 2026 (dayOffset 35)*

On Monday, May 11, 2026 a letter reaches you — at the new address, a small irony the file does not comment on. A meeting is set to review the closure, and the letter summarises the closure the way the file holds it: notice mailed, no response received, case closed for failure to respond.

“Failure to respond.” You responded in January, to the person the system sent you, in the room where you were told to tell things. The sentence in the file does not know that, because the sentence was written inside the system that never got the address.

Meetings read letters like this one first. Whether this one stays the whole story depends on what gets assembled before it is read.

**Choices:**
- Ask your lawyer to go through your folder with you before the meeting → **prep**
  - NOTE (shown after choosing): Preparation, in this system, is mostly deciding what paper will be on the table — and in what order it will be read.

## [prep] One Page, or a Story
*Day 38 — Thursday, May 14, 2026 — Thursday, May 14, 2026 (dayOffset 38)*

Your folder holds the whole spring, if you wrote it down: the dated statement, both offices' written confirmations, and — if you requested it — the packet whose address entry is dated Monday, February 9, 2026. Assembled in order, they fit on one page: address given; address recorded in the case file; card declined; closure notice traced to the old address; correction sent to both systems in writing; file's own entry produced.

Or the spring can stay where parts of it have lived so far — in your head, in order, in a story you can tell well. Stories are true. Pages are portable. Meetings are rooms you speak in for minutes and files speak in forever.

**Choices:**
- Build the one-page chronology from the statement, the confirmations, and the file's own entry, in date order → **chronology_built**  _(FLAG: paperAssembled; HIDDEN + Chronology — one-page dated chronology built from the statement, the confirmations, and the case file entry)_
  - NOTE (shown after choosing): One page. Every line dated. Nothing on it that the system's own paper does not support.
- Go in with the story in your head — you lived it, in order → **story_only**
  - NOTE (shown after choosing): You did, and you can tell it. The closure letter can also be told — by the file, to every reader, whether you are in the room or not.

## [chronology_built] The Chronology, Assembled
*Day 40 — Saturday, May 16, 2026 — Saturday, May 16, 2026 (dayOffset 40)*

The page reads like a timetable, because it is one. New address given to the caseworker, Monday, January 26, 2026. The address recorded in the case file, Monday, February 9, 2026. Zora's kinship placement, Monday, March 16, 2026. The card declined, Monday, April 6, 2026. The correction and statement sent in writing to both systems, Monday, April 13, 2026. The case file packet received, Monday, April 27, 2026, its entry saying what it says.

Six lines, no adjectives. Your lawyer's word for a page like this is “quiet.” Quiet pages get read carefully, because there is nothing in them to argue with except their dates.

**Choices:**
- Make copies — one for the meeting, one for your lawyer, one for the folder → **meeting_eve**
  - NOTE (shown after choosing): Copies are how a page attends meetings you are not invited to. This one is about to attend the most important one.

## [story_only] The Story, Unwritten
*Day 40 — Saturday, May 16, 2026 — Saturday, May 16, 2026 (dayOffset 40)*

Your account is clear, in order, and true: the move, the conversation in January, the checkout, the maze of menus, the old address read aloud. Sitting at the kitchen table you can tell it start to finish without a pause. It has only one flaw, and the flaw is not in the telling.

It exists in exactly one place, and that place cannot be handed across a table, attached to a letter, or read after you leave the room. The file's version — “failure to respond” — exists everywhere the file goes.

**Choices:**
- Practice telling it once more, and set out the morning's things → **meeting_eve**
  - NOTE (shown after choosing): The meeting will be short. Short rooms reward paper and punish nothing — they simply cannot hold what was never handed to them.

## [meeting_eve] The Night Before the Meeting
*Day 43 — Tuesday, May 19, 2026 — Tuesday, May 19, 2026 (dayOffset 43)*

The night before the meeting, your lawyer goes through your folder with you. You have one because the law provides for counsel in these cases, and for appointed counsel if a parent cannot afford one (42 Pa.C.S. § 6337) — she is the person whose job is to stand in the meeting room and make the paper speak in the right order.

“Meetings weigh the letter that closed the case against whatever answers it,” she says. “Tomorrow we find out which record yours is weighed against — the closure's one line, or the closure's one line plus the system's own entry answering it.”

Zora is at her aunt's. The folder is by the door. The bus fare for the morning is in your coat.

**Choices:**
- Take the folder and the fare, and go to the meeting → **meeting**  _(cash −6)_
  - NOTE (shown after choosing): Six dollars of fare. The folder weighs almost nothing. Both facts are misleading about their value tomorrow.

## [meeting] The Meeting
*Day 44 — Wednesday, May 20, 2026 — Wednesday, May 20, 2026 (dayOffset 44)*

The meeting is orderly and brief. The closure letter is read the way files are read: notice mailed, no response received, closed for failure to respond. The room begins, in the ordinary way, to treat the spring as a story about a mother who did not answer.

Then your lawyer asks that the record be completed before the closure is weighed. What happens next depends, with a precision this scenario has been honest about from its first checkout, on what your choices actually put in her hands.

**Choices:**
- Put the dated paper on the table — the statement, both address confirmations, and the case file's own address entry → **end_win**  _(REQUIRES FLAG: addressCorrected; REQUIRES FLAG: recordsRequested; REQUIRES FLAG: paperAssembled)_
  - NOTE (shown after choosing): Six dated lines, one of them in the system's own hand. The room does the arithmetic itself, out loud, which is where arithmetic changes a record.
- Present what paper you have — some of it, without the full set → **end_lose**
  - NOTE (shown after choosing): Part of a chronology is an argument with missing premises. The closure letter, whole and printed, is sitting across the table.
- Tell the spring as a story — the move, the checkout, the old address read aloud → **end_lose**
  - NOTE (shown after choosing): Your voice is truthful and detailed. The file's voice is one line long and has already been read.

## [end_win] Ending — Restored, Going Forward
*Day 47 — Saturday, May 23, 2026 — Saturday, May 23, 2026 (dayOffset 47)*

**Ending.**

**Debrief:**
- WHAT THE FILE HELD (the hidden record, revealed): A dated sequence authored largely by the system itself: your new address given on Monday, January 26, 2026 and recorded in the case file on Monday, February 9, 2026; your written correction, your written request for the notice to be re-sent, and your dated statement, sent to both systems in the week of the decline; and both offices' written confirmations that the corrected address now stands on their files. At the meeting on Wednesday, May 20, 2026, the chronology was put beside the closure letter, and the room attributed the closure to the notice failure: the household's benefits for the members still at home were restored going forward, and the corrected address stands in writing in both systems. The assessment form rates what it can see; after this meeting, what it can see includes the reason.
- THE PROCESS UNDER THIS PATH (described, keeping to this scenario's verified law): The one legal instrument was the verified one. The case record was yours on written request — it “shall be released upon request” (55 Pa. Code § 3130.44(d)) — and requesting it is what let you show the file's own dated entry instead of describing a conversation. Counsel (42 Pa.C.S. § 6337) presented the chronology in the room where the closure was weighed. Everything else was generic process, deliberately without citation: correct an address in writing to every system that holds a version of you, ask in writing for the missed notice to be re-sent, and state the facts once, with dates, while they are new. No benefit rule is stated anywhere in this ending, because none was needed: the letters in this story stated their own instructions on their faces, and the paper answered the paper.
- THE HONEST PART: Label this win honestly — it is partial, and one part of it is deliberately not a win at all, because this scenario does not decide it. The card works going forward for the household members still at home; the strained weeks behind you are not repaid, Zora is still at her aunt's tonight, and the case is still open. And Zora's own portion while she is placed is a separate question, with its own papers and its own room, that this meeting did not take up and this scenario does not resolve — it is withheld here on purpose, not settled quietly in your favour. A different meeting might have noted the chronology and restored less, or later. Workers, meetings, and luck all held pieces of this. Your share was narrower and durable: when the system's letter went to the wrong home, you made the system's own file say so.

## [end_lose] Ending — Failure to Respond, As Filed
*Day 47 — Saturday, May 23, 2026 — Saturday, May 23, 2026 (dayOffset 47)*

**Ending.**

**Debrief:**
- WHAT THE FILE HELD (the hidden record, revealed): One letter and one phrase. The closure letter — notice mailed, no response received — and its phrase, “failure to respond,” with nothing in the room explaining the spring between them: no dated statement both systems received, no written confirmations to set beside the letter, no case file entry quoted against the closure. At the meeting, your account was heard and, in the way of spoken accounts, believed personally and set aside professionally. The closure stands as written. The address, corrected out loud, may or may not survive the next worker, the next office, the next letter — because out loud is where it lives now.
- THE PROCESS UNDER THIS PATH (described, keeping to this scenario's verified law): The tools existed at every step and are modest ones. Correct the address in writing to both systems, so each correction has a date and a copy; ask in writing for the notice to be re-sent; state the facts once, in writing, with dates. Request the record, which “shall be released upon request” (55 Pa. Code § 3130.44(d)), so the file's own entry — your new address, recorded in January's conversation's wake, weeks before the decline — can be shown rather than remembered. And let counsel (42 Pa.C.S. § 6337) carry the assembled page into the room. None of that requires anyone to have acted in bad faith. It only requires paper — because the burden of explaining a notice failure quietly falls on the person the failure is written about, whether or not she ever saw the notice.
- THE HONEST PART: Let this debrief be as fair as the meeting was not: you did the human part of this correctly and early. You gave your new address to the worker the system sent you, promptly, in person, and watched her write it down. The letter that closed your case was mailed to a home you had already left, by a system you had never been told was a separate system. What was lost was not effort — it was evidence, and the two are different currencies in a file. A different office might have written the address failure into the closure itself; some do. This one did not, and outcomes here turn on workers, offices, and luck as much as on parents. The phrase in the file is not a verdict on you as a mother. It is a verdict on what was documented — and a folder started tonight, with the next letter, still changes what the next meeting reads.
