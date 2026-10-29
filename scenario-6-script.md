# THE FIRST 90 DAYS — Scenario 6: “The Folder” (Foundation tier)

*Human-readable script. This document and `scenario-6.json` are generated from a single source and match node-for-node: same IDs, same order, same choices, same effects.*

**The family is fictional — a composite. No real person's story appears here.**

**Content note:** This scenario depicts a referral mailed to an old address, a records request, and a written correction. There is no graphic content. Players may skip any scene or use the quick exit at any time.

**How to read effects:** `cash −4` changes the player's cash. `FLAG: name` sets a flag the engine tracks. `HIDDEN + item` means the case file quietly records that item at this choice — the player does not see it when it happens. `NOTE:` is text shown to the player right after choosing.

Start date: Monday, February 2, 2026. Day offsets are days since the scenario's start date. Starting cash: $120.

## [start] The Referral You Never Got
*Day 0 — Monday, February 2, 2026 (dayOffset 0)*

Your daughter Sana is five. The two of you moved across town in November — new apartment, new mailbox, a kitchen window Sana has claimed for her drawings. The case is a prevention case: support, not separation. Sana is home, and the plan is built to keep it that way.

At today's visit, your caseworker, Mr. Adeyemi, frowns at his screen. 'The parenting program referral went out three weeks ago,' he says. 'They mailed your intake packet. Didn't you get it?' You did not. You have never heard of the program.

**Choices:**
- Ask where exactly the packet was mailed → **n2**
  - NOTE (shown after choosing): A simple question. It is about to become the whole case in miniature.
- Say the mail has been unreliable and let it go for now → **n2**
  - NOTE (shown after choosing): Mail is unreliable everywhere. That is not the same as knowing where the packet went.

## [n2] The Old Street
*Day 1 — Tuesday, February 3, 2026 (dayOffset 1)*

He turns the screen. The address on the referral is your old street — the apartment you left in November, the one with the mailbox that stuck. The agency's file has your new address on one page and the old one on the referral, and the referral is the page that travels.

'We’ll sort it,' he says, kindly, and makes a note you cannot read from your side of the desk.

**Choices:**
- Ask what the note says, and whether the program still has your slot → **records**
  - NOTE (shown after choosing): The slot is held until Monday, February 16, 2026, he says. After that, the program re-offers it. One quiet clock, now ticking.
- Thank him and head home to wait for the new packet → **records**
  - NOTE (shown after choosing): Waiting is a plan the mail has already failed once.

## [records] The Whole Referral, Please
*Day 2 — Wednesday, February 4, 2026 (dayOffset 2)*

At home, you do a thing the system did not suggest: you buy a folder. It costs three dollars and has two pockets and a fastener, and it makes you feel, obscurely, like someone whose papers are going somewhere on purpose.

Then you put in a written request — a short note, dated — for a copy of the referral and the address page of your record, so you can see with your own eyes what the program was sent.

**Choices:**
- File the written request for the referral and address page → **prep**  _(cash −3; FLAG: recordsRequested; HIDDEN + Records — parent requested copies of the referral and the address on file)_
  - NOTE (shown after choosing): Under 55 Pa. Code § 3130.44(d), the record is released on request. The copies arrive the next morning — and the wrong address is right there, in the agency’s own type.
- Skip the copies — you already saw the screen → **prep**  _(cash −3)_
  - NOTE (shown after choosing): You saw a screen, once, from across a desk. That is a memory. A copy is evidence.

## [prep] What the Copies Show
*Day 3 — Thursday, February 5, 2026 (dayOffset 3)*

The folder now holds the truth in duplicate: your lease with the new address, dated November; the agency's address page, updated in December; and the referral, mailed in January — to the old street. Three documents, and the story they tell is nobody's villainy. It is a system copying an old line into a new form.

The program's intake appointment sits on Monday, February 16, 2026, if the address is fixed in time. If it is not, the slot goes to the next family on the list, and your file gains a line about a referral 'not completed.'

**Choices:**
- Draft the correction tonight: old address, new address, dates, in writing → **eve**  _(FLAG: correctionDrafted)_
  - NOTE (shown after choosing): One page. Polite, specific, and impossible to misfile as a conversation.
- Decide a phone call tomorrow will be faster → **eve**
  - NOTE (shown after choosing): It will be faster. Faster is how the first correction — the one in December — presumably happened too.

## [eve] Two Ways to Fix an Address
*Day 4 — Friday, February 6, 2026 (dayOffset 4)*

The correction is drafted, or the phone call is planned. Either way, tomorrow you will try to move one line of type from one address to another, in a building full of lines of type.

Sana is asleep with her drawings taped above her bed in the new apartment — the one the referral has never heard of.

**Choices:**
- Sleep on it, and do it in the morning, properly → **split**
  - NOTE (shown after choosing): Morning comes either way. The question is what it finds you carrying.

## [split] The Desk, or the Phone
*Day 5 — Saturday, February 7, 2026 (dayOffset 5)*

Morning. The agency office is twenty minutes away. Your phone is in your hand, and Mr. Adeyemi's number is right there, and a call would take four minutes and no bus fare.

The correction, though, is a document — it wants to be filed, stamped, and copied, not described. What you choose in the next ten minutes decides whether 'parent corrected address' exists anywhere outside your memory.

**Choices:**
- Go in person: hand in the written correction and get a stamped copy for the folder → **p1**  _(cash −4; FLAG: correctionFiled; HIDDEN + Correction — written address correction filed; stamped copy to parent)_
  - NOTE (shown after choosing): The clerk stamps it, copies it, and hands you the copy. The correction now exists in two places, and one of them is your folder.
- Call Mr. Adeyemi and explain the address change over the phone → **u1**  _(HIDDEN + Correction — address change reported verbally by phone; no written correction received)_
  - NOTE (shown after choosing): He is glad you called. He writes a note — on his pad, in his words, between two other calls.

## [p1] Stamped
*Day 7 — Monday, February 9, 2026 (dayOffset 7)*

The stamped copy goes in the folder, in front, where the important things live. Mr. Adeyemi calls that afternoon — a real call, unhurried. The referral is being re-issued to the new address today, he says, and the program has confirmed the slot is still yours.

'Send me the confirmation when you send the referral,' you say, surprising yourself. 'So I can watch for it.'

**Choices:**
- Ask for the confirmation in writing, and note the call in the folder → **p2**  _(FLAG: confirmationAsked)_
  - NOTE (shown after choosing): He laughs, not unkindly. "You and your folder," he says, and sends it.
- Take the good news and let the paperwork be → **p2**
  - NOTE (shown after choosing): Good news travels light. It also leaves nothing behind it.

## [p2] Watching the Right Mailbox
*Day 8 — Tuesday, February 10, 2026 (dayOffset 8)*

The confirmation arrives, and with it a tracking detail you can check: the packet was re-mailed on Tuesday, February 10, 2026 to the new address. Your mailbox — the one that does not stick — is now officially part of the case plan.

There is a smaller trap left, and it is an easy one to fall into: assuming that because the agency fixed its copy, everyone the agency talks to has the fix.

**Choices:**
- Call the program yourself and confirm they have the new address → **p3**  _(FLAG: verifiedDownstream; HIDDEN + Verification — parent confirmed corrected address with the program directly)_
  - NOTE (shown after choosing): The program’s intake worker checks, and reads the new address back to you, digit by digit, like a pilot. Both systems now agree on where Sana lives.
- Assume the program’s copy updated itself → **u3**  _(HIDDEN + Verification — parent did not confirm the address downstream)_
  - NOTE (shown after choosing): Copies in other buildings update when someone updates them. No one has, yet.

## [p3] The Packet Arrives
*Day 10 — Thursday, February 12, 2026 (dayOffset 10)*

The packet comes on a Thursday, in an envelope that has your correct name on your correct street. Sana watches you open it like it is a present, which, in a sense she would not use, it is.

Intake forms, a program calendar, a letter confirming the appointment on Monday, February 16, 2026. You fill the forms out at the kitchen table and put copies — copies of your copies — in the folder.

**Choices:**
- Call the program to confirm the appointment, and file their answer → **p4**  _(FLAG: appointmentConfirmed)_
  - NOTE (shown after choosing): Confirmed, with a name attached: "Ask for Dana at the desk." The folder grows a page.
- Put the packet in the folder and wait for the day → **p4**
  - NOTE (shown after choosing): The day is on the calendar either way. Confirmation is how a plan becomes a plan twice.

## [p4] Intake Day Approaches
*Day 12 — Saturday, February 14, 2026 (dayOffset 12)*

Two days out, Mr. Adeyemi reviews the file with you by phone: referral completed, address corrected, appointment set. He reads the file the way it will be read by anyone who reviews this case after him.

There is one more ordinary moment where this can still wobble: the program will send a summary of the intake to the agency afterward, and summaries go where addresses go.

**Choices:**
- Ask that the summary come to you as well, so you can check it → **p5**  _(FLAG: summaryAsked)_
  - NOTE (shown after choosing): "Copies to the folder," he says, and you can hear the smile. It is becoming a system, and systems are what survive busy weeks.
- Let the summary travel its usual route → **p5**
  - NOTE (shown after choosing): Usual routes are how the old address got its second career.

## [p5] The Intake, Attended
*Day 14 — Monday, February 16, 2026 (dayOffset 14)*

The intake happens — you, Sana, a kind room, a program worker who has your right address and your right names and a calendar that matches yours. At the end she hands you a one-page summary to sign: attendance, referral source, address, next dates.

It is accurate in every line but one small thing: it lists the referral date as the January date — the first, failed mailing — rather than the corrected one. A tiny thing. The kind of tiny thing files are made of.

**Choices:**
- Point it out, watch her correct it, then sign — and keep your copy → **end_good**  _(FLAG: readBeforeSigning)_
  - NOTE (shown after choosing): She corrects it in pen, initials it, and copies it for you. The record now tells the whole story, including the fix.
- Sign it — the date is a detail → **end_partial**
  - NOTE (shown after choosing): Details are what files are. The January date stays, and with it, a question nobody will ask out loud: why did this family take three months to engage?

## [end_good] The Address, Corrected in Ink
*Day 16 — Wednesday, February 18, 2026 (dayOffset 16)*

**ENDING.** Debrief:

- The referral is completed, at the right address, and the file says so — including how it was fixed: a written correction, filed by you, stamped, and verified downstream with the program itself. Anyone who reads this case later will read a story about a system error and a parent who repaired it in ink.
- The law inside this story: under 55 Pa. Code § 3130.44(d), the copies of your referral and record are released on request. Without your own copy, the wrong address was a rumor you heard across a desk. With it, the wrong address was a document you could correct.
- Notice the shape of the winning moves: ask for the paper, write the correction, get the stamp, verify the fix reached the other building. Each one took minutes. Together they are the difference between 'not completed' and 'completed — corrected by parent.'
- Honesty requires this: the clerk might have misfiled a stamped correction, and Mr. Adeyemi happened to be a worker who answers his phone. Workers vary, mail varies, luck varies. What does not vary is that a correction which exists on paper can be found again — and one that was only spoken cannot.

## [u1] A Helpful Call
*Day 7 — Monday, February 9, 2026 (dayOffset 7)*

The call goes well. Mr. Adeyemi is sorry about the mix-up, promises to update the address, and wishes Sana well with the drawings. You hang up feeling handled, which is a pleasant feeling and a dangerous one.

His note from the call — 'mom called re: address' — goes into a stack. The referral system, in another part of the building, pulls addresses from a different field. Nobody is careless. Everybody is busy. The old street rides again.

**Choices:**
- Ask him to confirm the change by mail or email, so you can file it → **u2**
  - NOTE (shown after choosing): A confirmation is a small ask. It is also the whole difference between a call and a correction.
- Trust the call — he said he’d handle it → **u2**
  - NOTE (shown after choosing): He meant it when he said it. Meaning it is not the same as filing it.

## [u2] Nothing in the Mail
*Day 8 — Tuesday, February 10, 2026 (dayOffset 8)*

A week passes. The new mailbox holds bills, a flyer, a birthday card from Sana's aunt — and no packet, and no confirmation. The appointment is on Monday, February 16, 2026, and the program has now mailed two packets to a mailbox that sticks, in a building you no longer live in.

There is still time, but it has changed shape: it is the shape of a deadline now.

**Choices:**
- Go to the office in person with your written correction, today → **p3**  _(FLAG: correctionFiled; HIDDEN + Correction — written correction filed in person after phone attempt failed)_
  - NOTE (shown after choosing): The clerk stamps it. The program re-mails that afternoon, to the right street, with the slot still — just — intact.
- Call again and ask him to check on it → **u3**  _(HIDDEN + Correction — second phone call made; still no written correction on file)_
  - NOTE (shown after choosing): He checks. The referral field still shows the old street. He updates it this time — in the field the program does not pull from.

## [u3] The Slot, Re-Offered
*Day 10 — Thursday, February 12, 2026 (dayOffset 10)*

On Thursday, February 12, 2026, the program does what programs do: it offers your unclaimed slot to the next family. The packet is sitting in a stuck mailbox across town. Your file, read plainly, says a referral was made in January and not completed.

At the next visit, Mr. Adeyemi is quieter. 'I thought we’d fixed that,' he says. You did fix it — out loud, twice. Out loud is where it stayed.

**Choices:**
- Show him your lease and ask what can still be salvaged → **u4**
  - NOTE (shown after choosing): The lease is paper. It starts, late, the conversation the correction should have started in February.
- Say what’s done is done and ask about the next opening → **u4**
  - NOTE (shown after choosing): There will be a next opening. There is always a next opening, and it is always later.

## [u4] Salvage, in Writing This Time
*Day 12 — Saturday, February 14, 2026 (dayOffset 12)*

The salvage is possible, and Mr. Adeyemi — who is, in the end, a fair man working in an unfair medium — proposes it himself: a written correction, filed now, with the lease attached, and a new referral marked urgent.

The new slot, if it comes, is six weeks out. The old slot is gone. Between those two facts lies the entire lesson of this story, priced in weeks.

**Choices:**
- File the written correction with the lease, and keep the stamped copy → **p5**  _(FLAG: correctionFiled; HIDDEN + Correction — written correction and lease filed; new referral requested as urgent)_
  - NOTE (shown after choosing): It goes in stamped and copied. Whatever happens with the slot, the file now contains your side, in your words, with dates.
- Ask him to just handle it this time — you’re tired of paper → **u5**
  - NOTE (shown after choosing): Tired of paper is the most understandable sentence in this whole story. It is also how the old address wins.

## [u5] The New Referral
*Day 14 — Monday, February 16, 2026 (dayOffset 14)*

A new referral is made. It is marked urgent, because Mr. Adeyemi is kind, and 'urgent' in a busy system means it joins a shorter queue in the same long hallway.

Sana is fine. Sana has been fine the whole time, in the apartment with the drawings — the apartment the paperwork is only now learning to find.

**Choices:**
- Open the folder and put the new referral on top → **end_partial**
  - NOTE (shown after choosing): The folder exists now. It should have existed in February. It will exist for everything after.

## [end_partial] The Letter That Went to the Old Address
*Day 16 — Wednesday, February 18, 2026 (dayOffset 16)*

**ENDING.** Debrief:

- The referral was eventually fixed — in writing, with a lease attached — but the first slot was lost, and the file carries a three-month gap that reads, to a cold reader, like a family that did not engage. Sana stayed home throughout; what was lost was time, and the true story of the time.
- The law inside this story: under 55 Pa. Code § 3130.44(d), your records are released on request. The copy of the referral — with the wrong address in the agency's own type — was available in February, for the asking. Evidence you can hold beats a screen you once saw.
- A phone call is a conversation. A filed correction is a fact. This scenario is about the distance between those two things, measured in mailboxes.
- Honesty requires this: Mr. Adeyemi was decent throughout, and it was not enough, because decency is not a filing system. A worse worker loses your correction entirely; a better one catches the address in December. You cannot choose your worker. You can choose whether your fix exists on paper.
