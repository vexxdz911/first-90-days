# THE FIRST 90 DAYS — Scenario 99: “His Name in the Right Column”

*Human-readable script. This document and `scenario-99.json` are generated from a single source and match node-for-node: same IDs, same order, same choices, same effects.*

**The family is fictional — a composite. No real person's story appears here.**

**Content note:** This scenario depicts a domestic-violence case from the victim-parent's side of the paperwork: a police call, a safety plan, and reviews. The violence itself is never depicted; there is no graphic content. Players may skip any scene or use the quick exit at any time.

**How to read effects:** `cash −40` changes the player's cash. `FLAG: name` sets a flag the engine tracks. `HIDDEN + item` means the case file quietly records that item at this choice — the player does not see it when it happens. `REQUIRES FLAG: name` means the choice is only available if that flag was set earlier; `REQUIRES NO FLAG: name` means it is only available if that flag was never set. `NOTE:` is text shown to the player right after choosing.

Start date: Monday, November 3, 2025. Day offsets are days since the scenario's start date.

## [start] The Report That Names a House
*Day 0 — Monday, November 3, 2025 (dayOffset 0)*

Your name is Tamara Cordero. Your daughters are Hazel, seven, and Olive, four. Last night a neighbor heard shouting through the wall and called the police. By the time the officers arrived, the girls' father was gone. No one was hurt. The girls were asleep in the back bedroom, and they stayed asleep.

This morning there is a card in your door from the county children and youth agency, and a police report somewhere in a system you cannot see. The report, you will learn, does not open with his name. It opens with your address.

A caseworker, Mr. Albright, is coming at four. Hazel is building a tower out of soup cans. Olive is supervising. You have six hours to decide what kind of record today will be.

**Choices:**
- Spend the first hour the way this case will be spent all month: on paper → **call_log**
  - NOTE (shown after choosing): A cheap notebook from the kitchen drawer. It will turn out to be the most important object in the apartment.

## [call_log] The Notebook, Page One
*Day 1 — Tuesday, November 4, 2025 (dayOffset 1)*

You write down last night the way you would want a stranger to read it: the time the shouting started, the time you took the girls to the back bedroom and closed the door, the time you called Lucinda, your sister, the time the neighbor knocked, the time the police came, the time he was already gone.

You write down what you did. Not what he did — the police report has his part, or does not. Yours: the calls you made, the door you closed, the sister who answered on the second ring, the girls asleep through all of it.

A notebook is not a shield. But a dated page written on day one is a different thing from a memory described on day thirty, and everyone in this system knows the difference even when they do not say so.

**Choices:**
- Start the notebook: dates, times, your own actions, in ink → **albright_visit**  _(FLAG: protectiveLog ; HIDDEN + Protective log — mother's own dated record of her actions, started day one)_
  - NOTE (shown after choosing): Page one costs nothing but the hour. Every later page will cite it.
- Trust your memory — you were there; you will remember it clearly → **albright_visit**
  - NOTE (shown after choosing): You will remember it truly. The system runs on what can be shown, which is a different standard, and not always a fair one.

## [albright_visit] Mr. Albright at Four
*Day 3 — Thursday, November 6, 2025 (dayOffset 3)*

Mr. Albright is younger than you expected and carries two things: a folder, and a scored assessment form he fills in as you talk. You cannot see the items. You can see that a question about last night becomes a mark in a column, and that the column is not labeled with the name you expected.

He asks who else could be called if there were another incident. He asks about Lucinda. He asks what you did, and then — in the same tone — what you will do to make sure it does not happen again, as if the second question had only one person in it.

The girls are home. The case is open. Nothing has been decided, which in this system means everything is being decided, quietly, in a folder.

**Choices:**
- Show him the notebook and name Lucinda as your call, in front of the form → **plan_draft**  _(HIDDEN + Home as observed — daughters settled; mother's dated log and sister named as support in the interview)_
  - NOTE (shown after choosing): He writes something down. For once, you know part of what it is, because you handed it to him.
- Answer his questions and keep the notebook in the drawer — it feels private → **plan_draft**
  - NOTE (shown after choosing): It is private. Private facts have a way of staying out of files, and files are where this case will be decided.

## [plan_draft] The Plan, First Draft
*Day 7 — Monday, November 10, 2025 (dayOffset 7)*

The family service plan arrives by mail and email on the same day, which feels like emphasis. Most of it is ordinary: check-ins, a parenting support referral, the girls' school and pediatrician named correctly.

Then the conditions. You are to 'ensure no contact occurs at the residence.' You are to 'maintain a home free of exposure to conflict.' You are to 'notify the agency of any attempted contact.' Read them again: every sentence has you as its subject. The man whose conduct made the plan necessary appears in it only as weather — a thing that happens around you, that you are scored on failing to prevent.

At the bottom is a signature line and a date. Signing quickly is what the cover letter invites. Your attorney, Ms. Radcliffe, has an office two bus rides away and a standing offer to read anything before you sign it.

**Choices:**
- Take the plan to Ms. Radcliffe and read every condition with her before signing → **radcliffe_meeting**  _(cash −10 ; FLAG: counselRead)_
  - NOTE (shown after choosing): Two bus rides and a morning. What she underlines will become the map of the next month.
- Sign it and return it the same day — the conditions are what they are → **radcliffe_meeting**
  - NOTE (shown after choosing): A signed plan is a real plan, and cooperation matters in this system. So does what the plan actually says, which you have now agreed to without a witness to your reading of it.

## [radcliffe_meeting] Ms. Radcliffe Reads the Verbs
*Day 9 — Wednesday, November 12, 2025 (dayOffset 9)*

"Read the verbs," Ms. Radcliffe says, and turns the plan sideways so you can both see it. "Ensure. Maintain. Prevent. Every verb in this plan is yours. Now find his." You look. There are none. His conduct is described in the summary as 'an incident at the home.' Your home. His name is in the report. Your name is in the conditions.

"This is a known shape," she says. "It is not a judgment about you, and I am not asking you to treat Mr. Albright as an enemy. The form that scored this case has a column for risk and a column for the parent in the home, and sometimes those two columns quietly become the same column. Our work is paperwork: your protective actions, documented; the conditions, rewritten to name the actual risk and the actions that are actually yours to take."

She keeps a copy. "And you have a right you should use early," she says. "Your case record — the assessment included — shall be released upon request. (55 Pa. Code § 3130.44(d)) We will want to see your name in his column with our own eyes."

**Choices:**
- Make the list of paper to build, in order, on her legal pad → **lucinda_offer**
  - NOTE (shown after choosing): Four items. None of them is 'try harder.' All of them are documents.

## [lucinda_offer] Lucinda, in Writing
*Day 11 — Friday, November 14, 2025 (dayOffset 11)*

Lucinda lives eleven minutes away and has never once, in either of your lives, failed to answer the phone. She has a spare key, a couch the girls call the boat, and a work schedule that puts her home most evenings. Everyone in the case knows this, in the way everyone knows things that are not written anywhere.

Knowing and documenting are different countries. A worker's note that 'mother reports sister is supportive' is a rumor the file tolerates. A signed page from Lucinda — her address, her availability, her willingness to take the girls at any hour and to be called first — is a fact the file has to carry.

**Choices:**
- Ask Lucinda to put it on one signed page: availability, address, 'call me first' → **stayaway_paper**  _(FLAG: lucindaWritten ; HIDDEN + Kin support — sister's signed written availability and first-call commitment in the file)_
  - NOTE (shown after choosing): She signs it at your table and dates it without being asked. Some people understand paper instinctively.
- Keep it verbal — Lucinda's word has been good for thirty years → **stayaway_paper**
  - NOTE (shown after choosing): It has. The file, however, has never met her, and the file is who will be in the room when decisions are made.

## [stayaway_paper] The Paper She Sought
*Day 14 — Monday, November 17, 2025 (dayOffset 14)*

This morning you went, on your own, to the courthouse office Ms. Radcliffe described, and asked for the protective paperwork available to you — the filing that would put the stay-away expectation into an order with his name on it instead of a condition with yours. The clerk was brisk. The forms took an hour. You left with stamped copies.

The stamped copies are yours. The question is whose file they live in. In your kitchen drawer they prove, to anyone who opens the drawer, that you sought protection. Filed with the agency, in writing, they become part of the record the assessment should have been reading all along.

**Choices:**
- File the stamped copies with the agency, in writing, and keep your own set → **neighbor_context**  _(FLAG: stayAwayFiled ; HIDDEN + Protective action — stay-away paperwork sought by mother; stamped copies filed with the agency)_
  - NOTE (shown after choosing): One envelope, one date stamp, one copy for the folder. His name, on an order, at last — as the risk, not the weather.
- Keep the copies at home — the agency has enough of your life on paper already → **neighbor_context**
  - NOTE (shown after choosing): A fair feeling. It is also how a file comes to show a condition about contact and no record of the mother who went to court to stop it.

## [neighbor_context] The Neighbor's Sentence
*Day 15 — Tuesday, November 18, 2025 (dayOffset 15)*

The neighbor who called — Mrs. Osei, two doors down — stops you at the mailboxes with an apology you do not need and a sentence you do. "I told the police I called because of the shouting, and that I saw you at your door calling someone while it was happening. I don't know if they wrote that part."

Whether they wrote that part is, it turns out, a question with a procedure attached. She is willing to write her sentence down, sign it, and date it. One page. It does not accuse anyone. It places you, on the night in question, doing the thing the plan will later claim there is no evidence you do.

**Choices:**
- Accept her written statement and add it to the folder for the agency file → **records_beat**  _(FLAG: neighborWritten ; HIDDEN + Context — neighbor's signed statement: mother observed calling for help during the incident)_
  - NOTE (shown after choosing): Context is the first thing a summary drops and the first thing a decision needs.
- Thank her and let it go — dragging neighbors into paperwork feels heavy → **records_beat**
  - NOTE (shown after choosing): It does feel heavy. Unwritten context is heavier; it just sends its bill later, to you.

## [records_beat] The Request Itself
*Day 17 — Thursday, November 20, 2025 (dayOffset 17)*

Ms. Radcliffe drafts the request on one page, because one page is all it takes: a written request for your case record, including the scored assessment form, under the rule that those records shall be released upon request. (55 Pa. Code § 3130.44(d))

Signing it feels, absurdly, like asking permission to read your own life. Send it and the packet will come — redacted in places, slow, and the single most useful delivery of the month. Wait, and the first full look at how this case is being scored will be the look the agency's summary gives a judge.

**Choices:**
- Sign and send the written record request today → **packet_arrives**  _(FLAG: recordsRequested)_
  - NOTE (shown after choosing): Dated, copied, sent. The highest-leverage page in the case so far, and it is not even close.
- Wait until the plan meeting — there may be nothing surprising in it → **packet_arrives**
  - NOTE (shown after choosing): There will be. Surprise is what a file you have not read specializes in.

## [packet_arrives] His Column, Her Name
*Day 22 — Tuesday, November 25, 2025 (dayOffset 22)*

The packet arrives in a thick envelope: visit notes, the plan, and — stapled where it can do the most quiet damage — the scored assessment form, in a redacted copy.

There it is, in print. Item: 'Exposure to conflict — elevated.' Item: 'Failure to protect — noted.' The narrative box under both describes the night, the shouting, the police call — and names you in the risk column as the item's subject. His conduct fills the description. Your name fills the column. The form did not lie about what happened. It filed what happened under the wrong name.

Ms. Radcliffe, on the phone, is quiet for a moment. "Now we correct it," she says. "Not with a phone call. With a page that goes into the same file this came out of."

**Choices:**
- Sit with the page until you can describe it without shaking, then build the correction → **correction_letter**
  - NOTE (shown after choosing): Anger is information. The correction will be a document. Documents outlast both.

## [correction_letter] One Page, With Attachments
*Day 24 — Thursday, November 27, 2025 (dayOffset 24)*

The correction is one page long, because Ms. Radcliffe believes pages that are one page long get read. It does not argue that the night was fine. It separates two things the form merged: his conduct, which is the risk; and your actions, which are the record — the notebook's dated entries, the call to Lucinda, the stay-away paperwork you sought and filed, Lucinda's signed availability, Mrs. Osei's signed sentence.

Attached, in order, every one of them. The letter asks, in plain words, that the assessment narrative name the actual source of risk, and that the plan's conditions be rewritten to match: conditions on your actions — call, document, notify, use the kin plan — not conditions requiring you to control another adult's conduct.

A correction that is spoken evaporates. A correction that is filed has to be answered, or at least carried.

**Choices:**
- File the one-page correction with every attachment, in writing, copies kept → **copies_cost**  _(FLAG: correctionFiled ; HIDDEN + Correction filed — assessment narrative challenged in writing; protective actions documented with attachments)_
  - NOTE (shown after choosing): Into the same file the form came out of. That symmetry is the whole strategy.
- Raise it by phone with Mr. Albright — he seemed fair, and paper feels confrontational → **copies_cost**
  - NOTE (shown after choosing): He did seem fair. Fair people rotate off cases; filed pages stay. The phone call will be remembered kindly and recorded barely.

## [copies_cost] Copies, Postage, Bus Fare
*Day 27 — Sunday, November 30, 2025 (dayOffset 27)*

Paper is power and paper has a price list: copies of the full packet for Ms. Radcliffe, postage for the filings, bus fare across town twice. It is not a dramatic amount of money. It is a noticeable one, in a month that also contains rent.

Hazel asks why the folder is getting its own grocery bag. 'Because it is coming with us everywhere now,' you tell her, and she accepts this the way children accept weather: as a fact about the season she is living in.

**Choices:**
- Pay for the copies and postage — the folder goes everywhere, complete → **visit_two**  _(cash −20)_
  - NOTE (shown after choosing): Twenty dollars. The correction, the attachments, and the receipts all ride together, in order.
- Copy only the correction page and save the rest of the money → **visit_two**
  - NOTE (shown after choosing): A correction without its attachments is a claim. With them, it was an exhibit. The difference will matter in rooms you are not in.

## [visit_two] The Second Visit
*Day 29 — Tuesday, December 2, 2025 (dayOffset 29)*

Mr. Albright's second visit is a different temperature from the first. The girls are mid-tower — cans again, architecture improving. Lucinda is present, because today she was invited, with her signed page already in his folder and her knowledge of the girls' routines on open display: Olive's song, Hazel's reading level, who needs the nightlight and who pretends to.

He asks about the plan's condition — 'ensure no contact occurs' — and for the first time you hear, in his own voice, a hesitation about the verb. He does not apologize for the form. He does write, while you watch, a note whose first three words are 'Mother has documented.'

Three words. In this system, they are load-bearing.

**Choices:**
- Walk him through the folder, page by page, before he leaves → **school_note**  _(HIDDEN + Home as observed — second visit: kin support present and documented; mother walked worker through the written record)_
  - NOTE (shown after choosing): Not a performance. A guided tour of evidence that exists whether or not anyone tours it — which is exactly why the tour helps.
- Let the visit be a visit — the folder has been sent; pushing feels risky → **school_note**
  - NOTE (shown after choosing): Sent paper and seen paper are cousins, not twins. But the visit goes well either way, and that, too, goes in a note.

## [school_note] Hazel's Reading Level
*Day 31 — Thursday, December 4, 2025 (dayOffset 31)*

Hazel's teacher sends home a note in the reading folder, the ordinary miracle of an ordinary system working: Hazel has moved up a reading level, and she told the class her auntie has a couch shaped like a boat.

It has nothing to do with the case. That is the point of including it, and the point of keeping it: a case file tends to flatten a family into its worst night. Paper that records the other six nights of the week — filed, dated, ordinary — is how the flattening gets resisted, one school note at a time.

**Choices:**
- File the teacher's note with the folder and send a copy with the next update → **incident_self_report**
  - NOTE (shown after choosing): Ordinary life, documented. It will sit in the file next to the worst night, saying: there were other nights.

## [incident_self_report] The Call You Were Told to Make
*Day 34 — Sunday, December 7, 2025 (dayOffset 34)*

Sunday, mid-afternoon: his car, slowed at the corner. Not a scene — a presence, and then gone, the way a shadow crosses a yard. The girls are inside. Nothing happens, which is exactly what you were trying to make happen, and exactly what the plan orders you to report: 'notify the agency of any attempted contact.'

You call. You also — because the notebook is a habit now — write it: time, what you saw, that the girls were inside, that Lucinda came over within the hour, that you are reporting it the same day, as the plan requires and as you would have anyway.

Somewhere in the agency, this call is about to be read two ways: as a mother doing precisely what her plan says, or as fresh evidence that risk keeps visiting her address. Which reading it gets may depend on what else is in the file when it lands.

**Choices:**
- Report it the same day, in writing as well as by phone, with the notebook page attached → **supervisor_meeting**  _(HIDDEN + Self-report — attempted contact reported same day, in writing, with dated log and kin response documented)_
  - NOTE (shown after choosing): The call the plan demanded, made in the form the file respects. Whatever happens next, the reporting itself is beyond dispute.
- Report it by phone only — writing it down makes it feel bigger than it was → **supervisor_meeting**
  - NOTE (shown after choosing): By phone it is a message taken by whoever answers. Messages shrink in the retelling, except for the parts that grow.

## [supervisor_meeting] The Meeting With a Supervisor
*Day 37 — Wednesday, December 10, 2025 (dayOffset 37)*

The call has consequences, as calls in this system do: a meeting, with Mr. Albright's supervisor present, to 'review the safety picture.' The phrase could mean a rewritten plan. It could mean a petition. The folder you carry into the room is, at this point, either an argument or a scrapbook, depending on what the last month put in it.

The supervisor has the assessment summary on top of her copy. Ms. Radcliffe, beside you, has the correction, the attachments, and the stay-away filing — the record under the summary. Two stacks of paper about the same family. The meeting is, in the end, a contest between them, conducted politely, at a conference table with a box of tissues nobody touches.

**Choices:**
- Ask, on the record of the meeting, for the plan decision in writing either way → **rewrite_request**
  - NOTE (shown after choosing): Whatever is decided, a written decision can be answered, appealed to, or built on. A spoken one can only be remembered, differently, by everyone.

## [rewrite_request] Naming the Actual Risk
*Day 39 — Friday, December 12, 2025 (dayOffset 39)*

Ms. Radcliffe makes the ask plainly, the way she read the verbs: rewrite the plan so its conditions name the actual risk and the mother's actual actions. His conduct, named as the risk it is, with the stay-away order as the system's own instrument against it. Her conditions: notify, document, call Lucinda, keep the girls' routines — actions a person can actually perform, and be honestly scored on performing.

She asks that the assessment narrative be corrected to match — the version with his name in the risk column — and that the meeting's decision, whatever it is, be provided in writing. The supervisor looks at the attachments for a long moment. She does not say yes in the room. Supervisors rarely do. She says the decision will issue before the next hearing date.

**Choices:**
- Leave the written ask with her, dated, and keep the stamped copy → **safety_plan_check**  _(cash −10 ; FLAG: rewriteAsked ; HIDDEN + Plan revision — written request that conditions name the actual risk and the mother's actual actions; decision promised in writing)_
  - NOTE (shown after choosing): Ten dollars of copies and bus fare. The ask now exists in the only tense this system fully respects: filed.
- Take the verbal 'we'll look at it' and save the friction → **safety_plan_check**
  - NOTE (shown after choosing): 'We'll look at it' has no date, no author, and no appeal. It is the hallway promise of agency practice, and it ages the same way.

## [safety_plan_check] Nine Ordinary Days
*Day 42 — Monday, December 15, 2025 (dayOffset 42)*

What follows is not a montage. It is nine ordinary days: school runs, Lucinda's couch-boat on Friday, the notebook's pages filling with times and nothing dramatic, a check-in visit that finds dinner cooking and homework out.

Ordinary days are the substance a safety plan is supposed to protect, and their documentation is quietly the strongest exhibit in the case — a file that shows a pattern of life, not just a night of incident. But a second incident is not yours to schedule, and the system is about to test the file in the only way it fully believes: under pressure, again.

**Choices:**
- Keep the routine, keep the notebook, and wait for the paper decision → **second_incident**
  - NOTE (shown after choosing): The promise was a written decision before the hearing date. Paper is coming — one kind or another.

## [second_incident] Wednesday, Again
*Day 44 — Wednesday, December 17, 2025 (dayOffset 44)*

Wednesday evening: a knock that is not Lucinda's knock, a voice at the door that is his, the girls already in the back bedroom with the door closed because that is the drill you practiced without ever calling it a drill. You do not open the door. You call the police, then Lucinda, then the agency's line — in that order, in the notebook, in real time.

He is gone before the police arrive, again. Nobody is hurt, again. And now the system must decide what this night means, with the file wide open on the table: whether a mother who did every documented thing her plan and her own judgment required is a safety plan working — or a risk that keeps happening at her address.

**Choices:**
- Stand on the written record: 'Everything I was asked to do is in that file, dated — judge the file.' → **rewrite_ordered**  _(REQUIRES FLAG: protectiveLog ; REQUIRES FLAG: correctionFiled ; REQUIRES FLAG: lucindaWritten)_
  - NOTE (shown after choosing): This stand exists only because the record does: the log, the filed correction, the kin page. Paper, built in calm weeks, speaking in a hard one.
- Stand on the same record — but the file holds your voice only as summaries, and the summaries say 'exposure' → **removal_night**  _(REQUIRES NO FLAG: correctionFiled)_
  - NOTE (shown after choosing): Without the filed correction, the newest version of the story in the room is still the form's — and the form has your name in his column.
- Say nothing about files — ask the court to simply judge the plan as written, condition by condition → **adjudication_hearing**
  - NOTE (shown after choosing): The plan as written asks whether you ensured no contact occurred. On those words alone, last night answers itself.

## [rewrite_ordered] The Decision, in Writing
*Day 46 — Friday, December 19, 2025 (dayOffset 46)*

The written decision issues at the hearing, and Ms. Radcliffe reads the operative lines twice before she lets you read them, the way you handle anything load-bearing.

The plan is rewritten. The risk is named in the document's own words now — his conduct, his name, in the column where risk lives. Your conditions are the actions: notify, document, maintain the kin plan with Lucinda, keep the stay-away order current. The assessment narrative in the file is corrected to match, with your one-page correction and its attachments carried as part of the record.

The girls remain home. The case remains open — that sentence matters, and the ending will say it plainly — with a review date, a rewritten plan, and a file that finally describes this family in the right order: the danger first, by name; the protection second, by evidence.

**Choices:**
- Take the written decision home and put your copy in the folder, on top → **end_best**
  - NOTE (shown after choosing): On top, where the next reader starts. That, in the end, is what all of this was for.

## [end_best] His Name in the Right Column
*Day 53 — Friday, December 26, 2025 (dayOffset 53)*

Hazel and Olive are home, and were home for nearly all of the fifty-three days this story covers — school, the couch-boat, the soup-can architecture, the ordinary six nights of every week. The case is still open. A review is still coming. Nobody in this ending should call that a small thing, and nobody should call it closure.

What changed is the document at the center of the case. The plan's conditions now name the actual risk and the mother's actual actions. The file's narrative puts his conduct in the risk column, where it belonged on day one, and her documented protection in the protection column, where the evidence always said it belonged.

Ms. Radcliffe's copy of the notebook's first page is in her own file now. 'For the next mother,' she says, 'who thinks paper is just paperwork.'

**Ending.**

**Debrief:**
- THE BOARD, MAPPED — Placement track: Hazel and Olive remained home throughout, under a plan that was rewritten on Friday, December 19, 2025, with a review still ahead. This is a PARTIAL win, labeled honestly: the case is open, the plan is supervision, and a future incident will be read against this file — but it will be read against a corrected file. Assessment track: the scored assessment form's original narrative — 'exposure' and 'failure to protect,' with the mother's name in the risk column — was corrected in writing after the record was requested (flag: recordsRequested; 55 Pa. Code § 3130.44(d)), the one-page correction filed with its attachments (flag: correctionFiled).
- What the hidden items show: the file accumulated a dated protective log started on day one (flag: protectiveLog), stay-away paperwork the mother herself sought and filed (flag: stayAwayFiled), a sister's signed availability (flag: lucindaWritten), a neighbor's signed context statement (flag: neighborWritten), and a same-day written self-report of attempted contact. The rewritten plan's conditions are actions within the mother's power — notify, document, use the kin plan — which is also what makes them honestly enforceable. Counsel's role ran throughout, as the law contemplates parents be represented in these proceedings (42 Pa.C.S. § 6337).
- What was never in your control: his choices, the neighbor's original call, which supervisor read the file, and whether the next incident happens at all. A rewritten plan is not a verdict on Tamara Cordero, any more than the original plan was. Outcomes in this system also turn on workers, judges, resources, and luck — this one turned additionally on a discipline narrower than luck: her own actions, written down while she was doing them, filed where the scoring happens.

## [removal_night] The Knock, Answered by Paper That Isn't There
*Day 44 — Wednesday, December 17, 2025 (dayOffset 44)*

The agency's reading arrives within the hour, and it is the form's reading: another incident at the residence, exposure noted, the plan's condition — ensure no contact occurs — unmet. Your account of the night is true, detailed, and almost entirely unwritten where it counts. The notebook, where it exists, is fragmentary; the correction was a phone call; Lucinda's support is a fact everyone mentions and no document carries.

Hazel and Olive are placed tonight — Hazel holding Olive's sleeve the way she does in new places — with a foster family across the county. A hearing will follow quickly, because the law makes it follow quickly: an informal shelter care hearing not later than 72 hours after placement. (42 Pa.C.S. § 6332; 23 Pa.C.S. § 6315(d))

You go home to an apartment with a half-built soup-can tower still standing, and a folder much thinner than the month deserved.

**Choices:**
- Go to the shelter care hearing with Ms. Radcliffe and whatever paper exists → **shelter_hearing**
  - NOTE (shown after choosing): Seventy-two hours is the clock. What can be carried into that room is only what was built before tonight.

## [shelter_hearing] Seventy-Two Hours
*Day 46 — Friday, December 19, 2025 (dayOffset 46)*

The shelter care hearing is informal and fast, in a room where everyone but you does this every week. You have the right to counsel, and to appointed counsel if you cannot afford one (42 Pa.C.S. § 6337) — Ms. Radcliffe is beside you, reading from a file that keeps coming up short in the same places: the protective actions are described in summaries; the risk is described under your name.

The court continues the placement pending adjudication. It is not a finding that you failed your daughters. It is a ruling made on the paper that was in the room — and the paper in the room was the form, the summary, and the plan whose condition you could not, by its own wording, ever fully satisfy.

**Choices:**
- Leave with the adjudication date and the list of what can still be built → **end_removal**
  - NOTE (shown after choosing): Cases are lost at hearings and rebuilt between them. The record, even now, is still being written — that cuts both ways, and one of the ways is forward.

## [end_removal] Removed After the Call She Made Herself
*Day 49 — Monday, December 22, 2025 (dayOffset 49)*

Hazel and Olive remain placed at the first adjudication date, in a foster home where — the visit notes say — they are fed, schooled, and sad in the ordinary, non-emergency way of children sleeping in the wrong house.

Hold the sequence plainly, because the sequence is the scandal of this ending: the incident that triggered removal was reported by Tamara herself, as her plan ordered and her judgment agreed. The system asked her to make the call. She made the call. The file the call landed in had been written, from day one, with her name in the wrong column — and so the call was read as evidence about her, instead of as evidence about him.

The case continues. Reunification remains its stated goal, and the work of building, late, the record that should have been built early is now the work — the same pages, the same signatures, at ten times the price.

**Ending.**

**Debrief:**
- THE BOARD, MAPPED — Placement track: the girls were placed on Wednesday, December 17, 2025, after the second incident; the shelter care hearing followed within 72 hours, on Friday, December 19, 2025, as the law requires (42 Pa.C.S. § 6332; 23 Pa.C.S. § 6315(d)), with counsel as provided by 42 Pa.C.S. § 6337, and placement continued pending adjudication. Record track: the agency record was never effectively corrected in writing — the correction, if raised at all, was spoken, and spoken corrections do not travel with a file (no correctionFiled flag). The assessment narrative therefore still read 'exposure' and 'failure to protect' with the mother as the item's subject when the self-report landed. Kin support, however willing in life, reached the court as summaries rather than as a signed page the court could rely on.
- What the hidden items show: self-reporting was never the mistake. The mistake — the system's, in design, and this playthrough's, in paper — was a file in which a mother's documented protection had no standing next to a form's characterization of her. In the winning route, the identical call is read as compliance, because the file around it names the actual risk. Same mother, same call, same night: different paper, different reading.
- What was never in your control: his conduct, the timing of the incidents, the supervisor assigned, or the wording of a plan drafted before you ever saw it. This ending is not a verdict on Tamara Cordero's protection of her daughters — the record of the night shows her protecting them. Outcomes in this system also turn on workers, judges, resources, and luck, and on whether the file a decision lands in was corrected in time, in writing, by the person it misdescribed.

## [adjudication_hearing] Adjudication on the Plan as Written
*Day 46 — Friday, December 19, 2025 (dayOffset 46)*

The adjudication hearing takes the plan as it found it. That is the quiet catastrophe of this route: nobody in the room is asked to decide whose conduct created the risk, because the document being applied was drafted so that the question never arises. Its conditions have one subject. Its subject is you.

'Ensure no contact occurs at the residence' — contact occurred at the residence, twice, by the act of a man the plan does not name as its subject. The agency's evidence is the plan, the form, and the incidents. Your evidence is your testimony, truthful and uncorroborated by the attachments that were never filed. The court applies the document in front of it, because courts apply documents.

The girls are adjudicated under the plan as written, its conditions continued word for word, and the review clock starts on a case whose central document misdescribes it.

**Choices:**
- Hear the order, and ask Ms. Radcliffe what can still be filed, starting Monday → **end_unrevised**
  - NOTE (shown after choosing): An adjudication is a chapter, not the book. The correction that was not filed before it can still be filed after it — later, and uphill.

## [end_unrevised] The Plan as Written
*Day 49 — Monday, December 22, 2025 (dayOffset 49)*

Hazel and Olive come home under the original plan — which sounds like this ending's mercy and is, precisely, its trap. The conditions return with them, word for word: ensure, maintain, prevent, with the same single subject and the same unnamed weather moving around the family's address.

Every future incident — reported by Tamara, as the plan commands, or discovered any other way — will now be scored against conditions she cannot, by their own construction, guarantee. The case has not been lost. It has been loaded.

Ms. Radcliffe files, on Monday, the correction that could have come in November. It will be read. Everything in this system is eventually read; the only question the last forty-nine days ever asked was whether it would be read in time.

**Ending.**

**Debrief:**
- THE BOARD, MAPPED — Adjudication track: the case was decided on the unrevised plan, whose conditions named the mother as the subject of every obligation and the father's conduct as background. The girls are home under that plan and the case remains open to review — disposition and review practice in this system run on what the current plan and record support (42 Pa.C.S. § 6351) — and what this plan supports, incident by incident, is a reading the mother cannot control. Record track: the assessment narrative was never corrected on the record in a form the adjudication could use; the father's name never entered the risk column of any operative document.
- What the hidden items show: effort was not the gap in this playthrough. The gap was drafting — a plan accepted as written, a correction unfiled or unargued, and a hearing that therefore never had the chance to judge the right question. In the winning route, the same facts produce a rewritten plan because the question was put to the system in writing, with attachments, before an incident forced the issue.
- What was never in your control: the plan's original drafting, the form's column structure, his conduct, or the hearing's date. An order applying a miswritten plan is not a verdict on the mother who lived under it. Outcomes in this system also turn on workers, judges, resources, and luck — and on who succeeds in getting the operative document rewritten before the document gets applied.
