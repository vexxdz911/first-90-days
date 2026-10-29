# THE FIRST 90 DAYS — Scenario 39: “The Interview at School”

*Human-readable script. This document and `scenario-39.json` are generated from a single source and match node-for-node: same IDs, same order, same choices, same effects.*

**The family is fictional — a composite. No real person's story appears here.**

**Content note:** This scenario depicts a school interview of a child and the investigation that follows it — phone calls, a home visit, and paperwork. There is no graphic content, and the interview itself is not dramatized. Players may skip any scene or use the quick exit at any time.

**How to read effects:** `cash −40` changes the player's cash. `FLAG: name` sets a flag the engine tracks. `HIDDEN + item` means the case file quietly records that item at this choice. `REQUIRES FLAG: name` means the choice is only available if that flag was set earlier.

Start date: Tuesday, September 15, 2026. Day offsets are days since the scenario's start date.

## [start] The Call from the School
*Day 0 — Tuesday, September 15, 2026 (dayOffset 0)*

It is Ms. Quimby, Hana's teacher, and her voice has the careful flatness of someone delivering news she did not make. This afternoon, Hana was interviewed at school by a county worker, Ms. Aguilar. It went fine, Ms. Quimby wants you to know. Hana answered questions about home. Someone had reported concern, and the school cooperated, the way schools do.

Hana is ten. She let herself into the house twenty minutes ago, made toast, and is currently teaching her stuffed animals long division with total confidence. She does not yet know her afternoon became a file.

**Choices:**
- Thank Ms. Quimby, hang up, and sit with Hana while the day is still fresh in her → **n2**
  - NOTE (shown after choosing): Memory decays by the hour, and children's fastest of all. Tonight, Hana remembers sentences. By Friday she'll remember feelings.
- Call the agency first — a parent should hear about an interview from the agency → **n2**
  - NOTE (shown after choosing): A parent should. A parent also should hear her daughter's account before the file's account sets in her head like plaster.

## [n2] What Hana Said
*Day 1 — Wednesday, September 16, 2026 (dayOffset 1)*

Over toast, it comes out the way ten-year-olds report things: completely, and in the wrong order. The lady was nice. She asked what happens after school. Hana told her: on regular days you pick her up; on work days she walks the two blocks, lets herself in, and Mrs. Whitlock next door — who has a key and a standing invitation to check — looks in at four.

'Work days' are Tuesdays and Thursdays, when your shift doubles. Hana said the words 'lots of days.' She is ten. Lots is doing arithmetic it cannot do.

**Choices:**
- Write down Hana's account tonight, in her words, dated — what she was asked, what she answered → **records**  _(FLAG: verbatimTonight ; HIDDEN + Record — parent wrote the child's school-interview account the same night, in the child's words)_
  - NOTE (shown after choosing): Her words, your handwriting, tonight's date. This page will be the only version of the interview not written by the interviewer.
- Decide not to write it — you don't want her dwelling on it → **records**
  - NOTE (shown after choosing): She won't dwell. The file will. It dwells professionally.

## [records] The File Already Exists
*Day 2 — Thursday, September 17, 2026 (dayOffset 2)*

Somewhere across town there is a summary of that interview, written by the person who conducted it. Summaries compress. Ten-year-olds expand. Between Hana's 'lots of days' and the summary's rendering of it, a family's afternoons are currently being decided.

You make the request in writing: a copy of the record the agency holds, including the summary of Hana's interview.

**Choices:**
- File the written request for the record, interview summary included → **prep**  _(FLAG: recordsRequested ; HIDDEN + Records — parent requested the file, including the school interview summary, in writing)_
  - NOTE (shown after choosing): Under 55 Pa. Code § 3130.44(d), the record is released on request. What arrives is one page. Hana 'states she lets herself in after school.' Full stop. No Tuesdays. No Thursdays. No Mrs. Whitlock.
- Skip it — asking for the interview summary might look adversarial → **prep**
  - NOTE (shown after choosing): It might look like reading. Parents who read their files are the natural predators of bad summaries.

## [prep] The Arrangement, Documented
*Day 3 — Friday, September 18, 2026 (dayOffset 3)*

What Hana described has a paper skeleton: your roster showing the Tuesday/Thursday doubles, the two-block route, and Mrs. Whitlock — retired, next door, keyholder since Hana was seven, checker-inner at four o'clock on work days, keeper of an emergency card on her refrigerator with your number and Hana's doctor.

None of that is in the summary. All of it exists. Assembling it is a job, and it is about to be yours.

**Choices:**
- Assemble it: roster, route, Mrs. Whitlock's written statement of the arrangement → **eve**  _(FLAG: proofGathered ; HIDDEN + Proof — work roster and neighbor's written statement of the after-school arrangement collected)_
  - NOTE (shown after choosing): Mrs. Whitlock writes like she talks: dates, times, 'I look in at four.' A neighbor's statement is the arrangement with a signature under it.
- Decide you'll describe the arrangement when the worker visits — it speaks for itself → **eve**
  - NOTE (shown after choosing): Arrangements speak fluently, in rooms they're present in. The file is a room it will never enter unless someone carries it there.

## [eve] The Night Before Her Call
*Day 4 — Saturday, September 19, 2026 (dayOffset 4)*

Ms. Aguilar calls tomorrow. Hana is asleep with a stuffed animal faculty meeting arranged around her. On your table: her words from tonight, the summary's one page, your roster, Mrs. Whitlock's statement. Four documents that mostly agree — and differ exactly where it counts.

The call can be a collision or a correction. The difference is preparation, and you have done it — if you use it.

**Choices:**
- Plan the call around the two documents: her words first, the correction second, everything in writing → **split**  _(FLAG: callPlanned)_
  - NOTE (shown after choosing): You are not disputing the interview. You are completing it — with the Tuesdays, the Thursdays, and the neighbor the summary lost.
- Plan to keep it light — Hana's fine, and sounding calm matters most → **split**
  - NOTE (shown after choosing): Calm matters. Accuracy matters more, longer. The file will forget your tone by Tuesday and keep its sentences for years.

## [split] The Call
*Day 5 — Sunday, September 20, 2026 (dayOffset 5)*

Ms. Aguilar is brisk, reading from the summary: 'Hana states she lets herself in after school.' And there it is — the decision this week has been walking toward. The summary, unamended, describes a child alone most afternoons. The truth describes a child with a two-day arrangement and a neighbor with a key.

What enters the file in the next ten minutes decides which of those children the system plans for.

**Choices:**
- Walk her through it — Hana's own account, the two work days, Mrs. Whitlock — and confirm it all in writing today → **p1**  _(FLAG: correctionSent ; HIDDEN + Response — parent supplied the child's account and the documented arrangement, confirmed in writing)_
  - NOTE (shown after choosing): Your letter lands behind her summary, dated the same week as the interview. Files are read in order. Hers will now always be read with yours attached.
- Explain it warmly on the phone and trust the summary to be updated → **u1**  _(HIDDEN + Response — arrangement explained by phone; no written account or statement provided)_
  - NOTE (shown after choosing): She listens kindly. She updates nothing on the call — updates happen at desks, from paper. Her summary sails on, unamended, into the assessment.

## [p1] Read Back to You
*Day 7 — Tuesday, September 22, 2026 (dayOffset 7)*

Two days later, Ms. Aguilar reads you the amended summary over the phone — a small courtesy, and not a universal one. 'On Tuesdays and Thursdays, the child walks two blocks home; a neighbor with a key checks in at four.' Hana's lots of days has become what it always was: two days, bounded, covered.

She asks whether the description is accurate. It is the first time in this process anyone has asked you that about a sentence concerning your child.

**Choices:**
- Confirm it — and ask for the amended summary in writing for your folder → **p2**  _(FLAG: summaryInWriting)_
  - NOTE (shown after choosing): Confirmed, requested, filed. The interview now exists in the file the way it happened in the schoolroom — plus the context the schoolroom didn't have.
- Confirm it and let the file copy be the only one → **p2**
  - NOTE (shown after choosing): The amendment is real either way. Your copy is how you'd prove it in a year, to a new worker, in one page.

## [p2] Mrs. Whitlock, In Person
*Day 8 — Wednesday, September 23, 2026 (dayOffset 8)*

The home visit includes the two-block walk, done together, and Mrs. Whitlock's doorstep, where the arrangement is performed by its participants like a fire drill everyone has actually practiced: the key, the four o'clock look-in, the emergency card on the refrigerator, produced without being asked.

Ms. Aguilar writes on her clipboard for a long time. Long writing, at a visit like this, is the sound of a summary being replaced by a description.

**Choices:**
- Ask what the file will call the arrangement when this closes → **p3**
  - NOTE (shown after choosing): 'A neighbor-supported after-school plan, in place before our involvement,' she says. Dates matter to her. They have started to matter to you, too.
- Thank her and let the visit end on the doorstep → **p3**
  - NOTE (shown after choosing): It ends well either way. What it leaves behind differs.

## [p3] A Tuesday, Observed
*Day 10 — Friday, September 25, 2026 (dayOffset 10)*

The file catches a live Tuesday: your double shift, the walk, the look-in — each element in its place, logged by the school, the roster, and Mrs. Whitlock's four-o'clock wave, which Hana has started waving back at through the window with great ceremony.

Arrangements prove themselves the way bridges do: by being crossed, on schedule, in weather.

**Choices:**
- Note the Tuesday in your own records — date, times, who did what → **p4**  _(FLAG: ownNotes)_
  - NOTE (shown after choosing): Your notes and the file's now agree about Tuesdays. Agreement between records is the quietest form of winning.
- Skip your own notes — the agency's are thorough now → **p4**
  - NOTE (shown after choosing): They are. Thorough records in one building, and none in yours, is a library you can only visit.

## [p4] Closing
*Day 12 — Sunday, September 27, 2026 (dayOffset 12)*

The investigation is concluding, Ms. Aguilar says, and not the way the one-page summary threatened: the report will be recorded as not supported, the arrangement documented as pre-existing and adequate. The closing summary is being drafted.

Your folder and hers have spent two weeks converging. That is not luck. That is what the first night's page of Hana's words made possible — everything since was citation.

**Choices:**
- Ask for the closing summary in writing, for your folder → **p5**  _(FLAG: copyFiled)_
  - NOTE (shown after choosing): It arrives in three days. Your side of this story now lives in two buildings, saying the same thing.
- Let her file be the only copy → **p5**
  - NOTE (shown after choosing): Her file is a fine home for it. Yours would have been a second one.

## [p5] The Last Line
*Day 14 — Tuesday, September 29, 2026 (dayOffset 14)*

The closing summary is accurate — the arrangement, the Tuesdays, Mrs. Whitlock, all present and correct. The interview summary, the original one-pager, is summarized in it in a single line: 'Per the school interview, the child lets herself in after school.'

True, and incomplete in exactly the original way — because summaries quote summaries, and the correction lives one page deeper. There is an acknowledgment line, and room beside it.

**Choices:**
- Read it all — sign, and attach a one-line note pointing to the amended summary's page → **end_good**  _(FLAG: readBeforeSigning)_
  - NOTE (shown after choosing): One line: 'See amended summary: Tuesdays/Thursdays, neighbor check-in, page attached.' The file's shortest sentence now points at its most accurate one.
- Sign at the door — it's closed, that's what matters → **end_partial**
  - NOTE (shown after choosing): It is closed. The file's quickest summary of your daughter still says she lets herself in — and the next reader may never dig for the amendment you know is in there.

## [end_good] Her Words, and Yours Beside Them
*Day 16 — Thursday, October 1, 2026 (dayOffset 16)*

**DEBRIEF:**

The investigation closed with the report not supported, and the file — this is the rare part — contains your daughter accurately: two work days, a two-block walk, a neighbor with a key, and a ten-year-old whose own account of her afternoons sits in the record in her own words, taken down the night she gave it. What won was sequence: her words were written before the summary's version could harden into the only version.

The record inside this story: under 55 Pa. Code § 3130.44(d), the interview summary came from your record, on request — which is how you knew the file had lost the Tuesdays and the neighbor before the assessment was written from it. A summary you haven't read is a summary you're agreeing to.

Notice what the correction required: not disputing that Hana was interviewed, or what she said — completing it, with documents. Files accept completions far more readily than arguments.

Honesty requires this: Ms. Aguilar read the correction fairly and read the amendment back, and many workers do neither. A different office keeps the one-pager as the record and your letter as an exhibit of a difficult parent. You cannot choose the reader. You can choose whether Hana's words, dated the night she said them, are in the file when the reader arrives.

## [u1] Usually
*Day 7 — Tuesday, September 22, 2026 (dayOffset 7)*

The assessment comes back with a sentence that stops your eye: 'Per the school interview, the child usually lets herself in after school, unsupervised.' Usually — Hana's 'lots of days,' grown up into an adverb. Unsupervised — Mrs. Whitlock, erased by a prefix.

Words like these are not lies. They are compressions, and compressions are how a two-day arrangement becomes a lifestyle in a file. The plan being drafted from this sentence will be sized for the lifestyle, not the arrangement.

**Choices:**
- Call Ms. Aguilar and ask what would correct the sentence — in writing → **u2**
  - NOTE (shown after choosing): There is a way. It is the way it always was. It now has to correct an assessment instead of preventing one.
- Let it go — the visit will show them the truth → **u2**
  - NOTE (shown after choosing): Visits show truths to people. Assessments show sentences to plans. The plan is already being drafted from the sentence.

## [u2] The Repair Door
*Day 8 — Wednesday, September 23, 2026 (dayOffset 8)*

She is plain on the phone: send Hana's account as you wrote it, your roster, and a statement from the neighbor — in writing — and the assessment can be amended before the plan is finalized. Desks correct assessments, she says. Visits don't.

It is the same door as before, with the draught coming through it.

**Choices:**
- Send the full written packet today — Hana's account, roster, Mrs. Whitlock's statement → **p3**  _(FLAG: packetSent ; HIDDEN + Documentation — child's account, roster, and neighbor statement submitted in writing)_
  - NOTE (shown after choosing): It lands behind the assessment, dated. Files are read in order; your packet will sit right behind the word 'usually' and correct it forever.
- Send your own written account and skip the neighbor's statement — it feels like overkill → **u3**  _(HIDDEN + Documentation — parent's account submitted; neighbor's statement not included)_
  - NOTE (shown after choosing): Your account asserts the arrangement. Her statement is the arrangement, witnessed. Assertions get weighed. Witnesses get believed, or not — but they get read.

## [u3] Weighed
*Day 10 — Friday, September 25, 2026 (dayOffset 10)*

The packet without the neighbor is weighed the way single-source packets are: noted, filed, and described in the amendment-that-isn't as 'mother reports a neighbor checks in.' Mother reports. The reports are piling up — Hana's, as summarized; yours, as reported — while the one person who could say 'I look in at four, here is my key' in her own words remains a rumor in her own arrangement.

A plan is drafted anyway: check-ins, a review, the supervision question left open for sixty days.

**Choices:**
- Ask what single document would close the supervision question → **u4**
  - NOTE (shown after choosing): Her answer is one word long, and it has a doorstep and a refrigerator card: the neighbor.
- Accept the plan — sixty days isn't forever → **u4**
  - NOTE (shown after choosing): It isn't. It is, however, sixty days sized by an adverb.

## [u4] One Document
*Day 12 — Sunday, September 27, 2026 (dayOffset 12)*

She offers it cleanly: Mrs. Whitlock's statement, signed, with the key and the four-o'clock routine in her own words, filed before the review — and the sentence gets rewritten as an arrangement, the plan shrinks to fit the actual Tuesdays, and 'usually' comes out of the file's description of your daughter.

It is one page. It was always going to be one page. It is simply later now, and it has to argue with a sentence instead of preceding one.

**Choices:**
- Get Mrs. Whitlock's signed statement and file it before the review → **p5**  _(FLAG: neighborStatement ; HIDDEN + Documentation — neighbor's signed statement of the after-school arrangement filed)_
  - NOTE (shown after choosing): The statement goes in complete, in her hand. Whatever the closing summary concludes, the file's last word about Hana's afternoons will be witnessed, signed, and specific.
- Rely on the month's clean Tuesdays to speak for themselves → **u5**
  - NOTE (shown after choosing): Clean Tuesdays speak in logs. A signed statement speaks in the file, forever, in sentences.

## [u5] Sixty Days Later
*Day 14 — Tuesday, September 29, 2026 (dayOffset 14)*

The Tuesdays pass the way they always have — walk, key, look-in, wave — because the afternoons were never the problem the adverb imagined. What remains open is only the shape of the ending: whether the file closes this chapter with the arrangement witnessed in it, or with 'usually' standing where a neighbor should be.

Hana has started calling the four-o'clock look-in 'the inspection,' with a salute. She is fine. The file is the thing still being raised.

**Choices:**
- Wait for the closing summary → **end_partial**
  - NOTE (shown after choosing): It will come. They always come. The question was only ever what would be in the file when it was written.

## [end_partial] Usually, In the File
*Day 16 — Thursday, October 1, 2026 (dayOffset 16)*

**DEBRIEF:**

The investigation closed — the arrangement was always adequate — but it closed through a plan sized for the file's version of your afternoons: check-ins, a sixty-day question mark, and a description of your daughter that says 'usually' and 'unsupervised' where Tuesdays and a neighbor belong. Hana stayed home throughout. What was lost was the description, and descriptions are what the next case, if there ever is one, will be built from.

The record inside this story: under 55 Pa. Code § 3130.44(d), the interview summary was yours for the asking, early — and your daughter's own account, written the night she gave it, was the one document that could have stood beside the summary from the start. Paper that exists and paper that is filed are different countries.

Summaries compress, and compressions compound: a child's 'lots of days' became 'usually' became a plan. The cheapest correction is always the first one. Every later one costs more and argues uphill.

Honesty requires this: Ms. Aguilar offered the repair door twice, in plain words, and many workers would not have. A different office treats the one-page summary as settled truth. You cannot choose the reader. You can choose whether the truth is in the file in writing before the reader builds a plan from its absence.
