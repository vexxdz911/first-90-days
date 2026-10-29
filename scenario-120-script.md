# The Medicine Log (a fictional composite) — Node-for-Node Script (Scenario 120)

Scenario 120 of *The First 90 Days* — script generated node-for-node from `scenario-120.json`; the JSON is the source of truth.

A fictional composite built from published Pennsylvania dependency practice and documented system patterns. Not a real family's case.

**Content note:** a teenager in foster care and a dispute over medication records and notice. No graphic content.

**How to read effects:** `cash` is money spent or received at that choice; `FLAG:` marks a fact the story remembers; `HIDDEN +` is an assessment item the player never sees scored; `REQUIRES:` gates a choice on an earlier fact; `NOTE:` is authorial, not spoken in-world. Endings are marked **Ending.** with a **Debrief:**.

**Start date:** Monday, January 11, 2027. **Tier:** Hard. **Start cash:** $150.

---

## [start] Watching school

*Day 0 — Monday, January 11, 2027*

Siobhan has always visited at full volume — grievances, jokes, a running commentary on the foster home's television. Today she sits inside a quieter weather. Sentences arrive late and leave early. Twice she loses the thread of her own story and shrugs, unbothered, in a way that frightens you more than tears have ever managed.

"I'm fine," she says. "I just feel like I'm watching school. Like, from the hallway." A pause. "The pills changed again. In December. Didn't they tell you?" Nobody told you. You did not know there were pills whose changes could be numbered.

**Choices:**
- Ask her — gently, concretely — what she takes, and since when, and what December changed. → **how_siobhan**

## [how_siobhan] How Siobhan got here

*Day 0 — Monday, January 11, 2027*

The record, briefly and fairly: your illness last summer — the surgery, the complications, the months of recovery on a couch that was also your address — left Siobhan effectively unsupervised at the precise age supervision matters most, and the county's petition said so, in those words, accurately. She has been with Mrs. Ellery since August. Your plan is half medical recovery, half housing: you are in a medical-respite apartment now, working part-time, attending everything, missing nothing.

What your plan has never mentioned, in any of its versions, is medication — because until this visit, no one had ever mentioned medication to you.

**Choices:**
- Call Mrs. Ellery tonight. She hands Siobhan the pills every morning; start with the person who pours the water. → **ellery_call**

## [ellery_call] The bottles

*Day 1 — Tuesday, January 12, 2027*

Mrs. Ellery is a retired school secretary, and her kitchen runs on labeled shelves. Yes, there are medications — two, currently. They arrive from the pharmacy with agency paperwork; she administers what the bottles say, at the times the bottles say, and she keeps a notebook — her own, because secretaries keep notebooks — of every dose given, every refusal, every comment Siobhan makes about how she feels.

"I've wondered when you'd ask," she says, without triumph. "You're the mother. I give the pills; I don't decide them. The deciding happens somewhere above both of us, and it has never once sent me a letter either." She reads you the bottle labels over the phone, slowly, twice. You write down names and doses you cannot yet spell.

**Choices:**
- Write the names down exactly as heard — then call your lawyer and ask what a parent can actually demand here. → **lawyer120**

## [lawyer120] The paper above the pills

*Day 2 — Wednesday, January 13, 2027*

Ms. Renner maps the territory without inflating it. Medication for a child in placement is decided in prescribers' offices and agency processes, and no slogan changes that. But the decisions generate paper — prescriptions, medication administration records, visit notes, logs — and the paper is reachable. The agency's case record is released on request (55 Pa. Code § 3130.44(d)); you ask in writing, and you ask for the medication records by name. The permanency hearing on Thursday, February 18 will make the court's own determinations about this case (42 Pa.C.S. § 6351(f)) — and a court cannot determine what it cannot see.

"Two more tools," she says. "Written questions to the prescriber — real questions, about indications, changes, monitoring. Prescribers answer letters more often than they answer feelings. And your daughter's own account, in her words, with her permission. She is fourteen. A file that medicates a person should somewhere contain that person's testimony about it."

**Choices:**
- Write the request today: the full record, the medication administration records by name, the prescriber's identity and visit notes. → **request_sent**  _(FLAG: recordsRequested; FLAG: logRequested; HIDDEN + Medical — medication administration records requested by parent in writing)_
- Call the agency's nurse line first. A conversation might get you the story faster than a letter gets you the file. → **nurse_call**

## [nurse_call] The nurse line

*Day 3 — Thursday, January 14, 2027*

The agency nurse is kind, fluent, and document-free. Siobhan's medications are 'managed by her prescriber in coordination with the team.' The December change was 'a routine adjustment.' The log? 'Kept between the foster home and the pharmacy, I believe.' She cannot send you anything, but she is happy to note your concern in the call record — a record you will never see, summarizing a call whose summary is its only artifact.

You hang up knowing the shape of the answer and owning none of it. Somewhere there is a log with your daughter's name on it, and the distance between you and it is one written request long.

**Choices:**
- Send the written request. Full record, medication records by name, prescriber identified. → **request_sent**  _(FLAG: recordsRequested; FLAG: logRequested; HIDDEN + Medical — medication administration records requested in writing after verbal inquiry produced no documents)_
- Let the note in the call record stand. Professionals are coordinating; don't become the difficult file. → **waiting120**

## [request_sent] The request, out

*Day 5 — Saturday, January 16, 2027*

The request goes out in writing, dated, copied: the full case record under the regulation (55 Pa. Code § 3130.44(d)), the medication administration records expressly named, the prescriber's name and visit notes, and the pharmacy fill history if the file holds it. Ms. Renner reviews the draft and changes one word — *all* — into a list. "Lists," she says, "are what files answer. 'All' is what they hide behind."

While the file travels, life continues at visit-table scale. Siobhan has brought you a data point in a backpack.

**Choices:**
- Saturday's visit: she has something to show you. → **respite_story**

## [waiting120] Coordinated

*Day 6 — Sunday, January 17, 2027*

January coordinates itself onward. The team coordinates; the prescriber prescribes; the bottles arrive; the notebook at Mrs. Ellery's fills with doses and one-word reviews — *flat, flat, slept through breakfast*. Your knowledge of your daughter's medication remains exactly what it was in the visit room: what a fourteen-year-old could carry to you in conversation.

At the second January visit Siobhan has a new piece of data, offered with the ghost of her old delivery: "There's a bag in my backpack from the pharmacy. It has papers in it. Nobody said you can't read papers."

**Choices:**
- Read the papers — with her permission, at the visit table, in the open. → **pharmacy_bag**

## [respite_story] The October week

*Day 6 — Sunday, January 17, 2027*

On the record request's way out, Siobhan finally tells you about October — the week she has been alluding to in pieces. A respite stay while Mrs. Ellery had her own surgery; a night of panic that would not come down; an emergency department; a doctor she saw once, who started the first medication. By the time she returned to Mrs. Ellery's, the prescription had become a routine, the way weather becomes climate. Nobody designed a secret. A crisis made a decision, and then the decision made itself permanent, one refill at a time.

It is told without drama and deserves to be believed without decoration. It is also — you understand, listening — a story that exists in no document anyone has offered you.

**Choices:**
- Ask what she brought in the backpack. → **pharmacy_bag**

## [pharmacy_bag] The pharmacy bag

*Day 8 — Tuesday, January 19, 2027*

The bag holds the pharmacy's own paperwork: a fill history and an information sheet for a second medication — one whose name is not on either bottle Mrs. Ellery read to you, because it is the December addition, administered at school by the nurse, in the middle of the day you do not see. Prescriber: Dr. Anwar. Dates: December 9, and refills since.

Siobhan watches you read it. "You can take a picture," she says. "It's my bag." You photograph every page, and you understand that a fourteen-year-old has just performed, with a backpack, the document production this case's adults had not.

**Choices:**
- Ask her whether you may write down, in her exact words, what the medications feel like — for your lawyer, and only where she agrees. → **siobhan_words**  _(cash −5)_
- Take the photographs and let her words stay hers for now. The paper trail may be enough. → **visit2**

## [siobhan_words] Watching school, transcribed

*Day 10 — Thursday, January 21, 2027*

Her account takes ten minutes and one page, and she edits it like an author: *The morning one makes first period like watching it from the hallway. I fall asleep in math twice. The new one at lunch helps the panic but my hands feel far away. I am not saying stop everything. I am saying nobody asked me.* She signs it, dates it, and writes under the signature, unprompted: *You can show the judge. That's why I said it good.*

Ms. Renner, reading it later, is quiet for a moment. "Files medicate children every day," she says. "Almost none of them contain a sentence from the child about what the medicine is like. Courts notice sentences like hers. So do prescribers."

**Choices:**
- File her page with counsel, and ask what comes next: the log itself. → **visit2**  _(FLAG: siobhanHeard; HIDDEN + Medical — child's own account of medication effects recorded verbatim, with her consent)_

## [visit2] First period

*Day 13 — Sunday, January 24, 2027*

The next visit adds a corroborating witness of the accidental kind: Siobhan's school counselor mentioned — to Siobhan, in passing — that her first-period teacher has flagged sleeping in class, twice, in the grade portal the foster home can see. The picture assembling itself has three independent hands in it now: a daughter's account, a teacher's flags, a pharmacy's dates. Pictures like that are called, in courtrooms, exhibits.

What is still missing is the document at the center: the medication administration record itself — who prescribed, who changed, who administered, who was told. Your written request has been out for two weeks.

**Choices:**
- Go to Mrs. Ellery's notebook — she offered it the first night, and secretaries keep the truth. → **ellery_log**

## [ellery_log] The secretary's notebook

*Day 15 — Tuesday, January 26, 2027*

Mrs. Ellery's notebook is everything the official record will turn out not to be: dated, contemporaneous, complete. Every dose. Every change. And December 9 — the day the midday medication began — carries her careful annotation: *begun per agency phone instruction; no prescriber visit this week; S. says hands feel strange.* She makes you a copy at her kitchen table, with a retired secretary's full ceremony, and initials every page.

"I keep it because somebody should," she says. "I always assumed the agency kept the same. If theirs has a hole in it, that's their hole, not mine."

**Choices:**
- Take the copy to counsel. Two logs exist in this case now, and they are about to be compared. → **partial_log**  _(FLAG: kitchenLog)_

## [partial_log] The hole in December

*Day 17 — Thursday, January 28, 2027*

The agency's production arrives: records, reports — and a medication administration record with a six-week gap across December and early January, the exact weeks of the change. The prescriber's visit notes are 'held by the provider' and not produced. Whether the gap is sloppiness or something else, the document the court would naturally rely on cannot currently account for the most consequential month in Siobhan's medication history.

Ms. Renner tabs the gap with a yellow flag and writes one sentence on the packet memo: *The official log cannot say who decided December. The foster mother's notebook can say who was told: no one, by phone, off paper.* At a hearing, it is worth remembering, reports that are relied on can be examined and their makers questioned — the principle the law states expressly for disposition (42 Pa.C.S. § 6341(d)(2)) is the posture this packet takes toward every page.

**Choices:**
- Write to the prescriber directly — real questions, listed, dated, through counsel. → **prescriber_letter**

## [prescriber_letter] Questions for Dr. Anwar

*Day 20 — Sunday, January 31, 2027*

The letter to Dr. Anwar is a page of questions a mother is entitled to have answers exist for: What is each medication for? What prompted the December addition, and the setting in which it was decided? What monitoring is in place for a fourteen-year-old's mornings? Who, in the current arrangement, is notified before a change — and who should be? It accuses no one. It asks a prescriber to do, on paper, what prescribers do in their heads.

It can go in the mail, through counsel, with the log gap and Siobhan's page referenced. Or it can wait for a conversation that has no date, no address, and no obligation to occur.

**Choices:**
- Send it — copies to the agency and the file, the questions numbered so answers can be too. → **school_note**  _(cash −8; FLAG: prescriberAsked; HIDDEN + Medical — written questions to prescriber sent: indications, December change, monitoring, notice)_
- Raise the questions at the next team meeting instead — faces persuade better than letters. → **noor_silence**

## [school_note] The school nurse's page

*Day 24 — Thursday, February 4, 2027*

One more exhibit surfaces through the record: the school nurse's log — the midday dose, administered daily, with two notations in a nurse's flat hand: *slept through period 1 following dose timing change; teacher notified.* The system, it turns out, has been recording Siobhan's mornings faithfully, in four separate buildings, in four separate files. What it never did was let the files meet — or let her mother read any of them.

Your packet introduces the files to each other. That is most of what advocacy is, at this altitude: introductions between documents.

**Choices:**
- Wait for Dr. Anwar's answer — or its absence — with the packet nearly built. → **noor_reply**

## [noor_silence] The meeting that isn't

*Day 26 — Saturday, February 6, 2027*

The team meeting, when it finally convenes, has an agenda with eleven items and yours at the bottom in the category of *family input*, scheduled against the room's fatigue. You raise the questions. They are received warmly, noted generally, and answered in the specific way meetings answer: a follow-up will occur. No letter comes. No answers arrive with names or dates on them. The December decision remains, officially, something that happened the way weather happens.

Ms. Renner adds the meeting's minutes — one line, *mother raised medication questions; follow-up noted* — to the packet. "Sometimes the exhibit is the thinness," she says.

**Choices:**
- Build the packet around what exists: the gapped log, the notebook, the pharmacy dates, a daughter's page. → **packet120**

## [noor_reply] Dr. Anwar replies

*Day 27 — Sunday, February 7, 2027*

Dr. Anwar's reply is three pages, professional and — in the way of documents written by people who expect to be read by courts — precise. The October start: crisis, documented. The December addition: hers, by phone consultation with the agency during a reported escalation, with a visit to follow that scheduling then lost. Monitoring: described. And on the last page, the sentence the packet was built to earn: the morning dose's timing *should be reviewed against the school-day sedation reports*, and notice of non-urgent changes to the parent and counsel is, she writes, *appropriate and will be my practice in this case*.

A prescriber has now said, in writing, most of what you intend to ask the court to order. Orders are easiest to win when somebody with a title has already agreed they describe ordinary care.

**Choices:**
- Ask the guardian ad litem to read the whole packet — her position will be heard on February 18. → **gal_view**

## [gal_view] The guardian ad litem reads

*Day 30 — Wednesday, February 10, 2027*

Ms. Zielinska reads the packet the way she reads everything: completely, with a pencil. Siobhan's page gets the longest pause. "I visit her monthly," she says. "She told me she was 'fine.' She told you the truth because you asked about the pills specifically. There's a lesson in that I intend to be annoyed about later." Her position for the hearing aligns: notice of changes to mother and counsel, the log produced monthly, the dose-timing review completed and reported.

The agency's report, when it lands, will describe Siobhan as *medication compliant*. You now hold four documents that give that phrase a cross-examination.

**Choices:**
- Final assembly: the packet, in date order, gaps flagged, titles facing up. → **packet120**

## [packet120] Date order

*Day 33 — Saturday, February 13, 2027*

The packet tells December's story in the order December happened: a phone instruction; a pharmacy fill; a foster mother's notebook; a six-week hole in the official log; a nurse's two flat sentences; a daughter's signed page; a prescriber's letter, or a meeting's one-line minute where a letter should be. Ms. Renner writes the ask in findings language: that the court direct notice of non-urgent medication changes to you and counsel in advance; production of the complete medication log monthly; completion of the dose-timing review with a report to all parties.

Nothing in the ask claims you should prescribe. It claims you should be told — a distinction the packet states on its first page, before anyone can misstate it.

**Choices:**
- Read the agency's report when it comes, and mark every sentence about medication. → **agency_report120**

## [agency_report120] Medication compliant

*Day 35 — Monday, February 15, 2027*

The agency's report for the permanency hearing is competent on housing, silent where it should be specific on school, and — on medication — two sentences long. *Youth is medication compliant. Medication is managed by the prescriber in coordination with the team.* The team, as a body, has never been defined. The coordination has never been documented. December does not appear. It is, Ms. Renner says, turning the page, "a perfect report, if the file it summarizes were a different file. Ours will be in the room."

Reports at a hearing can be examined, and the people who made them questioned — the packet is built to make that examination short and factual.

**Choices:**
- One whiteboard session, then court. → **renner_whiteboard**

## [renner_whiteboard] What the court must decide

*Day 36 — Tuesday, February 16, 2027*

Ms. Renner draws the hearing the statute builds. At the permanency hearing the court determines: the continuing necessity of placement; compliance with the plan; progress toward alleviating the circumstances that caused placement; and whether reasonable efforts were made to finalize the plan. (42 Pa.C.S. § 6351(f)(1), (2), (3), (5.1))

"Medication is not a fifth determination," she says. "It is evidence inside the four — about necessity, about efforts, about what this placement is actually doing to her mornings. Our job is to make sure the court decides from the whole file, including the file's holes. Especially the holes."

**Choices:**
- Sleep. Tomorrow the file goes in front of the one person who can order it closed. → **night_before120**

## [night_before120] The folder, again

*Day 37 — Wednesday, February 17, 2027*

You think about the visit room in January: a girl inside a quieter weather, saying *didn't they tell you* — the question underneath this entire case. No conspiracy told her no. A set of defaults did: the packet routed here, the log kept there, the note filed elsewhere, the mother informed nowhere. Defaults are not villains. They are just undefeated until somebody files paper against them.

Tomorrow, somebody does.

**Choices:**
- Go to court. → **hearing120**

## [hearing120] Thursday, February 18

*Day 38 — Thursday, February 18, 2027*

The permanency hearing runs the statute's determinations (42 Pa.C.S. § 6351(f)), and the medication chapter is reached with the whole record in the room — or with as much of it as your winter assembled. The agency's two sentences are read. Then yours are. The judge's questions go where judges' questions go: to the documents.

What is ordered about Siobhan's medication — and about who is told what, in advance, in writing — is decided by what the file could prove when the room went quiet.

**Choices:**
- The file holds the mother's written requests, the foster mother's complete notebook, the daughter's own signed account, and a prescriber's letter agreeing that notice is appropriate. → **end_writing**  _(REQUIRES: recordsRequested; REQUIRES: prescriberAsked; REQUIRES: siobhanHeard)_
- The file holds the record and its December hole — but the questions to the prescriber were only ever raised aloud, and the daughter's account was never written down. → **end_eventually**  _(REQUIRES: recordsRequested)_
- The file holds a nurse-line note and a mother's memory of a visit-room conversation. → **end_counter**

## [end_writing] Ending — Every Change in Writing

*Day 38 — Thursday, February 18, 2027*

**Ending.**

**Debrief:** The order adopts the ask nearly whole, because the packet made it the path of least resistance: non-urgent medication changes require advance written notice to you and to counsel; the complete medication administration record is to be produced to all parties monthly; Dr. Anwar's dose-timing review is to be completed and reported within thirty days — and the first concrete result arrives before the ink is metaphorically dry, when the morning dose moves to evening and Siobhan's first period reopens like a window. The judge's last words on the subject are the ones your daughter wrote, quoted back into the record: *nobody asked me* — followed by the court's own sentence: "She has been asked now. It will stay that way."

Name the machinery honestly. No statute in this scenario handed a mother a veto over prescriptions, and the scenario asserts none. What the record did — the request under 55 Pa. Code § 3130.44(d), the questions a prescriber answered in writing, a foster mother's secretary-grade notebook, a child's signed page — was convert a default into a determination: at a hearing where the court must decide necessity, compliance, progress, and efforts (42 Pa.C.S. § 6351(f)), the medication chapter could no longer be two sentences long. Notice is not control. But notice is the difference between a parent and an audience.

What no strategy controls: the medicine itself, which may genuinely be helping and may change again for good reasons; a different judge's reluctance to write medication orders; the case's deeper road, which still runs through your recovery and housing. Siobhan remains in care tonight. But the log has a reader now, the changes have an addressee, and a fourteen-year-old's testimony about her own mornings is in the file that medicates her — permanently, in her own words, signed.

## [end_eventually] Ending — The Log, Eventually (partial)

*Day 38 — Thursday, February 18, 2027*

**Ending.**

**Debrief:** The court acts on what it can see, and what it can see is a hole. The order directs the agency to produce the complete medication administration record and a prescriber's summary before the next review, and notes — in the dry language courts use for weather they disapprove of — that the December gap 'should not recur.' The dose-timing question is deferred to that production. The notice arrangement you asked for is not ordered: the prescriber was never asked in writing, your daughter's account exists in your testimony rather than her handwriting, and a court asked to structure a practice prefers exhibits to recollections.

Do the honest accounting. The written record request (55 Pa. Code § 3130.44(d)) did its work — it produced the log, and the log's gap became the hearing's most durable fact. What was skipped skipped in a specific direction: the questions existed, but they were asked in a meeting, and meetings answer in minutes of one line. The daughter's account existed, but it was carried in her mother's voice, at one remove, discounted the way all secondhand things are discounted — the principle that written reports may be examined and their makers questioned (42 Pa.C.S. § 6341(d)(2)) cuts for the parent with paper and against the parent with a summary.

Partial, and pointed at a remedy: the next review now has a court-ordered production deadline in front of it, and nothing about this ending prevents the letters from being written in February instead of January. They will land differently — later, and into a file that already has a gap flagged by a judge — but paper filed late in this system is still paper. The log will be read. Eventually was this ending's title, not its epitaph.

## [end_counter] Ending — The Bag on the Counter

*Day 38 — Thursday, February 18, 2027*

**Ending.**

**Debrief:** The hearing's medication chapter is two sentences long, because two sentences is what the file held. And then, in the corridor afterward, Mrs. Ellery mentions — kindly, as one mentions weather — that the pharmacy bag on her counter this week held a new printout: the morning dose is being split, half at breakfast, half at school. You learn of the third change in your daughter's medication the way you learned of the first: by accident, from a kind person, after it had already happened. The system did not hide it from you. It simply never built a road from the decision to you, and no one had yet made it build one.

The debrief is the scenario itself, compressed: every document in this story existed. The log existed — at a foster home, in a secretary's notebook. The record existed — releasable on a written request (55 Pa. Code § 3130.44(d)) that was never sent. The daughter's knowledge existed — in her own precise sentences, never written down. The prescriber's willingness to answer existed. What did not exist was the paper connecting any of it to the one person the whole arrangement assumes is peripheral: the mother. Systems route information to the addresses they are given, in writing. Give them the address.

Nothing here is sealed. A request can be filed in February; questions can be numbered and mailed in March; permanency hearings recur on the statute's clock (42 Pa.C.S. § 6351(e)(3)(i)), and each one is a fresh chance to put the file in the room. But Siobhan's mornings between now and then will be medicated on information her mother receives by accident — and in this system, accident is what fills every space that paper doesn't.
