# THE FIRST 90 DAYS — Scenario 37: “The Bruise at Practice”

*Human-readable script. This document and `scenario-37.json` are generated from a single source and match node-for-node: same IDs, same order, same choices, same effects.*

**The family is fictional — a composite. No real person's story appears here.**

**Content note:** This scenario depicts an investigation into a reported bruise — a phone message, a home visit, and paperwork. There is no graphic content. Players may skip any scene or use the quick exit at any time.

**How to read effects:** `cash −40` changes the player's cash. `FLAG: name` sets a flag the engine tracks. `HIDDEN + item` means the case file quietly records that item at this choice. `REQUIRES FLAG: name` means the choice is only available if that flag was set earlier.

Start date: Monday, February 2, 2026. Day offsets are days since the scenario's start date.

## [start] The Fall, and the Phone Call
*Day 0 — Monday, February 2, 2026 (dayOffset 0)*

Your son Kwame is seven, all elbows and weather. On Saturday, at soccer, he went up for a ball with a boy twice his width, came down on the damp grass, and sat out the last ten minutes holding his shin and insisting, to anyone who would listen, that he was fine.

On Sunday you took him to the pediatrician anyway, because the bruise coming up on his left shin was the deep kind. Dr. Rao pressed it, watched him walk, wrote in the chart, and sent you home with instructions and a sticker. Today, Monday, there is a message on your phone from the county agency: a report has been made about the bruise. A worker named Ms. Bergstrom will be calling. An investigation is open.

**Choices:**
- Listen to the message again, slowly, and write down the name and number → **n2**
  - NOTE (shown after choosing): The message is forty seconds long. Fear makes it sound like forty minutes. On paper, it is a name, a number, and a word: investigation.
- Call back immediately, before you know anything, and explain the whole weekend at once → **n2**
  - NOTE (shown after choosing): Explaining is a good instinct. Explaining first, before you know what was reported, is how an explanation ends up answering a question nobody asked.

## [n2] What the Message Says
*Day 1 — Tuesday, February 3, 2026 (dayOffset 1)*

The message, written down, is smaller than the message in your head. A report was received. It concerns a bruise observed on a child. An investigation has been opened, which is the system's word for: someone will ask questions and write down the answers.

What it does not say: who called (reports' sources are not shared), what exactly was said, or what happens next. Two of those three unknowns can be shrunk — by asking for your own record before anyone visits.

**Choices:**
- Ask Ms. Bergstrom, when she calls, what the visit will be about → **records**
  - NOTE (shown after choosing): "A bruise, at soccer, reported Monday," she says. It is nearly everything she can tell you — and nearly everything you need to start.
- Decide not to ask — questions might look defensive → **records**
  - NOTE (shown after choosing): Questions are how the investigated learn anything at all. The file will not record that you were too polite to ask. It will record that you did not.

## [records] Your Own Record, First
*Day 2 — Wednesday, February 4, 2026 (dayOffset 2)*

Before you answer questions about a bruise, it helps to see what the file says the bruise is. The agency holds an intake summary. Across a desk you might glimpse it; in your own hands, you can read it at your table, twice.

You make the request in writing: a copy of the record the agency holds about this report, so your answers can meet the actual sentences.

**Choices:**
- File the written request for the intake summary from your record → **prep**  _(FLAG: recordsRequested ; HIDDEN + Records — parent requested the intake summary in writing during the investigation)_
  - NOTE (shown after choosing): Under 55 Pa. Code § 3130.44(d), the record is released on request. What arrives is one paragraph: bruise, left shin, observed at a youth sporting event, reported the following Monday. No name for the caller. One paragraph is enough to aim at.
- Work from the voicemail — a bruise is a bruise → **prep**
  - NOTE (shown after choosing): A bruise is a bruise. A file's sentence about a bruise is a machine you will be answering for weeks. It helps to have read the sentence.

## [prep] The Chart, Dated Sunday
*Day 3 — Thursday, February 5, 2026 (dayOffset 3)*

The pediatrician's office can print the visit note from Sunday: Kwame Mensah, seen for a shin contusion, mechanism — a fall at soccer — consistent with the mark, no other findings, follow up if it doesn't fade. It is dated Sunday. The report was made Monday. The order of those two facts is the whole story, and it is already written down in a chart you did not create.

What is missing is only assembly: the chart note, and your own short timeline of Saturday — the game, the fall, the ice pack from the coach's cooler.

**Choices:**
- Get the chart printout and write the Saturday timeline tonight → **eve**  _(FLAG: proofGathered ; HIDDEN + Proof — pediatrician visit note (Sunday, pre-report) and parent's written timeline collected)_
  - NOTE (shown after choosing): Two pages. The second page is yours; the first page is a doctor's, and it predates the report by a day, which is the kind of fact no interview can manufacture later.
- Decide the story is simple enough to tell without paper → **eve**
  - NOTE (shown after choosing): It is simple. Simple stories are exactly the ones that get retold wrong, one retelling at a time, until the file's version and yours are cousins.

## [eve] The Night Before the Visit
*Day 4 — Friday, February 6, 2026 (dayOffset 4)*

Ms. Bergstrom will come tomorrow after school. Kwame is doing homework at the table, shin propped on a chair, bruise going purple and yellow at the edges like weather leaving. The folder — chart note, timeline, the intake summary — is thin. Thin is fine. Thin and dated beats thick and remembered.

You could also spend tonight rehearsing Kwame. You will not. Children can tell when a sentence has been practiced on them, and so, in their way, can visitors.

**Choices:**
- Lay out the folder, and let the evening be ordinary → **split**  _(FLAG: folderReady)_
  - NOTE (shown after choosing): Ordinary is the exhibit. A boy, a table, a shin healing on schedule.
- Rehearse answers until the evening stops feeling ordinary → **split**
  - NOTE (shown after choosing): By nine, everyone in the house is performing a visit instead of having an evening. The performance is not evidence of anything — except tiredness.

## [split] The Visit
*Day 5 — Saturday, February 7, 2026 (dayOffset 5)*

Ms. Bergstrom is brisk and not unkind. She looks at the shin, asks Kwame about the game (he demonstrates the fall, enthusiastically, on the rug), and asks you how it happened. This is the decision the whole week has been walking toward — not what you say, but what you hand over while you say it.

Memory is one witness. Paper is another. Only one of them will still be in the room when the determination is made.

**Choices:**
- Tell her — and hand her the folder: the chart note and the timeline → **p1**  _(FLAG: folderGiven ; HIDDEN + Response — parent provided the pre-report medical note and a written timeline at the first visit)_
  - NOTE (shown after choosing): She reads the chart note standing in your kitchen. "Sunday," she says. "Before the report." She is not smiling. She is writing, which is better.
- Tell her, and keep the folder in reserve — in case things go badly → **u1**  _(HIDDEN + Response — parent explained the injury verbally; documentation mentioned but not provided)_
  - NOTE (shown after choosing): Reserve is a strategy for sieges. This is an interview. The folder stays on the counter, and her pen writes the version without it.

## [p1] Sunday, Before the Report
*Day 7 — Monday, February 9, 2026 (dayOffset 7)*

The visit ends with the chart note in her bag, marked for the file. "The date helps," she says, in the tone of someone telling you more than she has to. "People call us after they see a doctor, sometimes. A chart from before the call is a different animal."

She will call the pediatrician's office to confirm the note is genuine. That is not suspicion. That is her job building the same wall yours did — out of paper that can be checked.

**Choices:**
- Ask what happens next, and whether it will come in writing → **p2**
  - NOTE (shown after choosing): A determination letter, she says, either way. Letters are how this system says things it means.
- Thank her and close the door on the whole business → **p2**
  - NOTE (shown after choosing): The business is not closed until a letter says so. But the hardest room in it has been walked through.

## [p2] Confirmed
*Day 8 — Tuesday, February 10, 2026 (dayOffset 8)*

The call comes two days later, and it is short: the pediatrician's office confirmed the visit, the date, the note. Dr. Rao's chart and the coach's account of a fall agree with each other and with yours — three tellings, one shin.

Ms. Bergstrom is drafting her summary. She reads you the sentence about the injury over the phone, the way she will write it, and asks if it is accurate.

**Choices:**
- Listen closely — she says 'left shin' — and confirm it, asking for the summary in writing → **p3**  _(FLAG: summaryInWriting)_
  - NOTE (shown after choosing): Accurate, confirmed, and to be sent in writing. A file agreeing with itself is a quiet, powerful thing.
- Agree warmly and skip the written summary → **u3**  _(HIDDEN + Summary — determination summary given verbally; no written copy to parent)_
  - NOTE (shown after choosing): Warm agreement, cool record. If her summary is ever misread by the next reader, the file will contain nothing of yours beside it.

## [p3] One Detail
*Day 10 — Thursday, February 12, 2026 (dayOffset 10)*

The written summary arrives and it is right in every way but one: it says the bruise was observed at 'a school sporting event.' It was a Saturday league game, at the township fields — a small difference, and the kind that grows in files, where 'school' quietly suggests a weekday, a nurse, a different story.

A summary can be corrected the same way it was made: in writing, briefly, with the league schedule attached.

**Choices:**
- Send the one-line correction, with the league schedule, in writing → **p4**  _(FLAG: correctionSent ; HIDDEN + Correction — parent corrected the event description in writing, with documentation)_
  - NOTE (shown after choosing): One line, one attachment. The file now corrects itself, permanently, in your hand.
- Let it stand — school, league, what's the difference → **p4**
  - NOTE (shown after choosing): In a kitchen, nothing. In a file, the difference between the story that happened and a story that almost happened.

## [p4] The Determination
*Day 12 — Saturday, February 14, 2026 (dayOffset 12)*

The determination letter is being prepared. Investigations end the way they began — with paper arriving. Before it comes, Ms. Bergstrom asks whether you'd like the closing documents copied to you as they're filed.

Your folder and hers are close to twins now. Twins are harder to separate later — which is rather the point of keeping both.

**Choices:**
- Ask for copies of the closing documents for your folder → **p5**  _(FLAG: copyFiled)_
  - NOTE (shown after choosing): She agrees, and means it. Your side of this story will live in two buildings saying the same thing.
- Let her file be the only copy → **p5**
  - NOTE (shown after choosing): Her file is a fine home for it. Yours would have been a second one.

## [p5] Sign Here
*Day 14 — Monday, February 16, 2026 (dayOffset 14)*

The closing letter arrives: the investigation is closed; the report is not supported; Kwame's file note will say the injury was medically documented before the report was made. There is an acknowledgment line at the bottom — sign to confirm receipt.

Beneath your signature line, in the letter's last paragraph, the event is described one more time — and summaries, even good ones, deserve one careful read before a name goes under them.

**Choices:**
- Read the whole letter before signing, then sign and file it → **end_good**  _(FLAG: readBeforeSigning)_
  - NOTE (shown after choosing): Every sentence true. Your name goes under a letter you have actually read, into a folder that now holds the whole arc: message, summary, chart, correction, closing.
- Sign at the door — it's closed, that's what matters → **end_partial**
  - NOTE (shown after choosing): It is closed. The last paragraph, which you did not read, describes the corrected event as 'school athletics' — your correction, filed in one office, never reached this letter, and no one will ever know but you. You didn't read it.

## [end_good] Explained, With the Chart
*Day 16 — Wednesday, February 18, 2026 (dayOffset 16)*

**DEBRIEF:**

The investigation is closed and the report is recorded as unfounded — on the strength of a sequence nobody had to argue about: a fall on Saturday, a doctor on Sunday, a report on Monday. The chart existed before the question did. That is what won — not a performance at a kitchen table, but a date on a page.

The record inside this story: under 55 Pa. Code § 3130.44(d), the intake summary came from your record, on request, early — which is why your answers met the file's actual sentence instead of its shadow. The rest was assembly: a printout, a timeline, a one-line correction, all of it in writing.

Notice what the worker did with good paper: she checked it, and then she used it. Systems do that more often than their reputations suggest — when the paper is checkable.

Honesty requires this: Dr. Rao's note could have been thinner, and Ms. Bergstrom could have read generously-given documents ungenerously. Another office loses a folder page. Workers vary, offices vary, luck varies. A dated chart is the only version of Saturday that attends every meeting after you.

## [u1] From Memory
*Day 7 — Monday, February 9, 2026 (dayOffset 7)*

The visit goes the way memory goes. You tell it well — the game, the fall, the doctor 'on the weekend, Sunday, I think, or was the game Saturday — it was Sunday for the doctor, yes.' The shin is healing; your dates are not, quite, under a stranger's pen.

She writes: 'Mother reports child was seen by pediatrician; date not confirmed at visit.' She does not write it cruelly. She writes what happened in the room, and what happened in the room is that the chart was on the counter, in a folder, unopened.

**Choices:**
- Call her tomorrow and offer to send the chart note and timeline — in writing, this time → **u2**
  - NOTE (shown after choosing): Late is not never. But late is a genre, and you are now writing in it.
- Wait — she seemed satisfied; don't poke it → **u2**
  - NOTE (shown after choosing): She seemed many things, and wrote one of them down. The one she wrote down is the one that travels.

## [u2] The Repair Door
*Day 8 — Tuesday, February 10, 2026 (dayOffset 8)*

On the phone, Ms. Bergstrom is plain: the file needs the medical visit verified, and a supervisor will ask her about it this week. She cannot verify a folder she has never seen.

The door she is holding open has a shape: paper, this week, in writing — the same door it always was, now with a draught coming through it.

**Choices:**
- Get the chart printout today and send it with the timeline, in writing → **p3**  _(FLAG: chartSent ; HIDDEN + Response — medical note and timeline provided in writing after the first visit)_
  - NOTE (shown after choosing): It goes in with a date on it — later than it should have been, earlier than the determination. Files are read in order; your paper will sit behind her first note and correct it forever.
- Tell her the doctor's office can confirm it if she calls → **u3**  _(HIDDEN + Response — parent directed the agency to obtain the medical record itself)_
  - NOTE (shown after choosing): She can. Whether her week contains that call, between twenty other files, is a bet you are making with your child's record as the stake.

## [u3] Verified Late, or Not at All
*Day 10 — Thursday, February 12, 2026 (dayOffset 10)*

The week fills with other people's emergencies. The chart is confirmed eventually — or the determination is drafted first, on the file as it stood: a verbal account, an unconfirmed date, a coach who saw a fall and reported a bruise.

Her draft summary, when she reads it to you, has a sentence in it you have never heard before: 'Medical visit could not be verified at the time of the visit.' It is accurate. That is the worst part. It is accurate about the visit, and it will be read as accurate about you.

**Choices:**
- Ask what would correct the sentence before the determination is final → **u4**
  - NOTE (shown after choosing): Paper, she says. It is always paper. There is still time for some of it.
- Accept the sentence — the investigation will still close → **u4**
  - NOTE (shown after choosing): It will. Closures are not all the same shape, and sentences are what shapes are made of.

## [u4] By Friday
*Day 12 — Saturday, February 14, 2026 (dayOffset 12)*

She offers it cleanly: send the chart note, the timeline, and — if you write it — a one-paragraph correction of the 'could not verify' sentence, by Friday, and the determination will be drafted on the whole record instead of the thin one.

It is the same work the folder already was. It is simply later, and louder, and done against a deadline instead of before one.

**Choices:**
- Send the full packet by Friday — chart, timeline, correction — in writing → **p5**  _(FLAG: packetSent ; HIDDEN + Documentation — parent submitted the medical note, timeline, and correction before the determination)_
  - NOTE (shown after choosing): The packet goes in complete. Whatever the letter concludes, the file's last word about Kwame's shin will be dated, documented, and yours.
- Send the chart alone — the rest feels like overkill → **u5**
  - NOTE (shown after choosing): The chart proves a visit. The timeline and the correction were the parts that proved the story. Partial paper builds partial files.

## [u5] The Sentence Stays
*Day 14 — Monday, February 16, 2026 (dayOffset 14)*

The determination is drafted. The investigation will close — Kwame was never leaving this house over a soccer bruise, and everyone in the story has always known that, including, privately, the file. What is still undecided, down to the last letter, is what the file will say about how it closed.

The chart alone could not carry the correction. The sentence about verification stands in the draft like a chair left in a hallway.

**Choices:**
- Wait for the letter → **end_partial**
  - NOTE (shown after choosing): It will come. They always come. The question was only ever what would be in the file when it was written.

## [end_partial] Closed, With an Error In It
*Day 16 — Wednesday, February 18, 2026 (dayOffset 16)*

**DEBRIEF:**

The investigation closed and the report went down as unfounded — Kwame stayed home throughout, and the bruise faded on schedule. What was lost was not the outcome but the record: the file says the medical visit 'could not be verified,' and the event sits in it as a school game instead of a Saturday league. Closed is closed. The file's version of how is wrong in ways that will outlive the bruise.

The record inside this story: under 55 Pa. Code § 3130.44(d), the intake summary was yours for the asking, early — and the chart that decided everything existed before the report did. Paper that exists and paper that is provided are different countries. The folder spent the investigation on a counter.

Determinations are drafted from files, and files are drafted from visits. A chart handed over at the first visit writes one sentence; the same chart, sent late and alone, annotates another.

Honesty requires this: Ms. Bergstrom offered the repair door twice, in plain words, and many workers would not have. A different office closes this file slower and colder. You cannot choose the reader. You can choose whether the proof is in the file before the reader forms the sentence.
