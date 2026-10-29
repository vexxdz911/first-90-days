# THE FIRST 90 DAYS — Scenario 100: “The Prescription Is a Fact”

*Human-readable script. This document and `scenario-100.json` are generated from a single source and match node-for-node: same IDs, same order, same choices, same effects.*

**The family is fictional — a composite. No real person's story appears here.**

**Content note:** This scenario depicts a newborn case opened at a hospital: a mother in medication-assisted treatment, a shelter care hearing, releases and records, and a first review. There is no graphic content. Players may skip any scene or use the quick exit at any time.

**How to read effects:** `cash −40` changes the player's cash. `FLAG: name` sets a flag the engine tracks. `HIDDEN + item` means the case file quietly records that item at this choice — the player does not see it when it happens. `REQUIRES FLAG: name` means the choice is only available if that flag was set earlier; `REQUIRES NO FLAG: name` means it is only available if that flag was never set. `NOTE:` is text shown to the player right after choosing.

Start date: Monday, March 2, 2026. Day offsets are days since the scenario's start date.

## [start] Iris, Born Monday
*Day 0 — Monday, March 2, 2026 (dayOffset 0)*

Your name is Shondra Lachance. You have been in medication-assisted treatment for opioid use disorder for over a year — the same clinic, the same counselor, the same early-morning appointments, a record of attendance and screens that fills a binder at the clinic across town.

This morning, at the hospital, your daughter Iris was born. She is in the nursery. You are in a bed with a bracelet on your wrist and a birth certificate worksheet on the tray, deciding how to spell nothing — Iris was decided months ago, in the clinic waiting room, on a morning you were proud of yourself.

Before any discharge decision is made, a nurse tells you, kindly and without meeting the moment's eye, that a report has been made to the county agency — the hospital's social work office sent it — and that a caseworker will want to talk with you today. The case has opened before the discharge papers have.

**Choices:**
- Ask what happens next, and write the answer down on the back of the worksheet → **hospital_interview**
  - NOTE (shown after choosing): A habit from the clinic year: if it matters, it gets written. You do not yet know how much of this case will turn on which building a piece of paper lives in.

## [hospital_interview] Ms. Sloane and the Form
*Day 1 — Tuesday, March 3, 2026 (dayOffset 1)*

Ms. Sloane, the caseworker, is brisk, not unkind, and working from a scored assessment form she completes as you talk. One line of your hospital chart is doing outsized work in her questions: the medication line — the prescribed medication you take as part of treatment, listed in the chart beside everything else about the delivery.

She asks about the medication the way the chart lists it: as a substance present at delivery. Your year of treatment — the attendance, the screens, the counselor who knows your voice — enters the conversation as your say-so. The treatment record itself is in a different building, in a different file, behind releases nobody has offered you yet.

Iris, meanwhile, is not being discharged today. The agency is taking her into shelter care while things are assessed — which starts a clock the law sets in hours, not weeks: a shelter care hearing within 72 hours. (42 Pa.C.S. § 6332; 23 Pa.C.S. § 6315(d))

**Choices:**
- Tell her the treatment history in full, and ask what paper would prove it → **nursery_paper**  _(HIDDEN + Interview — mother reported a year of medication-assisted treatment; scored form worked from the hospital chart's medication line)_
  - NOTE (shown after choosing): 'What paper would prove it' turns out to be the most useful question asked in this room all day.
- Answer what is asked and no more — the chart should speak for itself → **nursery_paper**
  - NOTE (shown after choosing): The chart does speak. What it says, in the line the form is reading, is a medication — not a year of treatment. Charts speak in lines, not in years.

## [nursery_paper] Two Files, One Mother
*Day 1 — Tuesday, March 3, 2026 (dayOffset 1)*

Here is the shape of the problem, laid out by nobody and visible to everyone: the file that will score you — the agency's — currently contains a hospital report and a medication line. The file that explains you — the clinic's — contains a year of documented stability, and it cannot travel on its own. Treatment records move when a patient signs a release, and sit still when she does not.

Your counselor, Claudette, has said for a year that your record is 'the kind we wish we could show people.' It can be shown. Showing it is a signature, a fax, a filing — three unglamorous verbs between Iris's file and the truth.

Your mother, Estelle, is in the waiting room with a bag packed for a granddaughter she has not yet been allowed to hold, and opinions about paperwork she has not yet been asked for.

**Choices:**
- Call Claudette before anything else is decided → **counselor_voice**
  - NOTE (shown after choosing): Her number is in your phone under a star. A year of mornings earns a star.

## [counselor_voice] Claudette's Voice
*Day 1 — Tuesday, March 3, 2026 (dayOffset 1)*

"Shondra. Listen to me the way you listened in month two." Claudette's voice does what it has done for a year: it slows the room down. "Your record here is not a rumor. Attendance, screens, dosing, group — over a year, documented, by us. If the agency's file says anything else, it is because our file hasn't reached it. That is fixable, and it is fixable fast — with your signature."

She can write the letter: a year of treatment, stability documented, the prescribed medication named as what it is — treatment, taken as prescribed, under supervision. She can send the attendance and screening summaries with it. All of it moves on a signed release. None of it moves without one.

"And Shondra — get their file, too. You are allowed to see what they are scoring. Ask, in writing. Then we correct it in writing, before any hearing, not after."

**Choices:**
- Ask exactly which releases to sign, and where they must go → **release_decision**
  - NOTE (shown after choosing): Two destinations: the clinic, to release; the agency, to receive. A record that travels to the wrong building has not traveled.

## [release_decision] The Signature
*Day 2 — Wednesday, March 4, 2026 (dayOffset 2)*

The releases arrive as a small stack of forms on a clipboard — the least dramatic objects in the building, and the hinge the whole case will swing on. Signing lets the clinic send your treatment record to the agency: Claudette's letter, the year's attendance, the screening history, the prescription documented as treatment.

Not signing is also a real choice, and it is written sympathetically here: these are your most private medical records, the system asking for them is the system that just scored a prescription as a risk, and 'trust us with the file' has not earned itself this week. Nothing about hesitating makes you dishonest. It only makes the agency's file stay exactly as thin as it was this morning — a chart line, with no year behind it.

The shelter care hearing is tomorrow. What is in the agency's hands by then is what the hearing will be about.

**Choices:**
- Sign the releases — clinic to agency — and keep copies of every page → **estelle_offer**  _(FLAG: releaseSigned ; HIDDEN + Releases signed — treatment record authorized to travel from clinic to agency file)_
  - NOTE (shown after choosing): Copies in your bag, the originals moving. By tomorrow, two files become one story — if the receiving end files them, which is tomorrow's fight.
- Hold the releases — you want your lawyer's eyes on them first → **estelle_offer**
  - NOTE (shown after choosing): A lawyer's eyes are worth having; the hearing is tomorrow either way. The record stays in its building, and the form keeps its version.

## [estelle_offer] Estelle, in the Waiting Room
*Day 2 — Wednesday, March 4, 2026 (dayOffset 2)*

Estelle has raised three children, buried a husband, and kept every receipt since 1987. She is, by any sane assessment, Iris's safety net with a name and an address — twenty minutes away, a nursery corner already set up in the spare room 'just in case,' although the 'case' she was imagining was you needing a nap.

The agency knows she exists because you have said so. What the agency does not have — what the hearing tomorrow will wish it had — is Estelle on paper: her address, her availability, her written willingness to take Iris at any hour, and the beginnings of her own assessment as a kin placement.

She has a pen. Of course she has a pen. She has three.

**Choices:**
- Estelle writes and signs it: address, availability, 'Iris can come to me any time' → **records_beat**  _(FLAG: estelleWritten ; HIDDEN + Kin fallback — grandmother's signed written availability and willingness, on paper before the hearing)_
  - NOTE (shown after choosing): One page, three pens' worth of certainty. The fallback is no longer a description; it is a document.
- Keep it as a family understanding — the agency can call her if it needs her → **records_beat**
  - NOTE (shown after choosing): Agencies call people whose numbers are in files. Tomorrow, the file is what will be in the room; Estelle will be in the waiting room, which is a different place.

## [records_beat] Asking for Their File
*Day 2 — Wednesday, March 4, 2026 (dayOffset 2)*

Claudette's second instruction is the one Ms. Sloane's supervisor will later call, in a tone you will think about for weeks, 'assertive for a day-two case': request the agency's record — including the scored assessment form — in writing. Under the rule, those records shall be released upon request. (55 Pa. Code § 3130.44(d))

You cannot correct a characterization you have not read. If the form has already written the word 'use' where the word should be 'treatment,' you want to know it today — while it is still a line in a file, correctable with a page — not at the first review, when it has hardened into the case's official memory.

**Choices:**
- Sign and send the written record request today, before the hearing → **shelter_hearing**  _(cash −10 ; FLAG: recordsRequested)_
  - NOTE (shown after choosing): Ten dollars of copies and a stamp. The cheapest reconnaissance in the case, bought on day two instead of day twenty.
- Wait until after the hearing — one battle at a time → **shelter_hearing**
  - NOTE (shown after choosing): After the hearing, the file will include the hearing. Files grow in one direction; corrections are easiest upstream.

## [shelter_hearing] Seventy-Two Hours
*Day 3 — Thursday, March 5, 2026 (dayOffset 3)*

The shelter care hearing comes within 72 hours of Iris's placement in shelter care, as the law requires (42 Pa.C.S. § 6332; 23 Pa.C.S. § 6315(d)), in a courtroom where you are entitled to counsel, and to appointed counsel if you cannot afford one (42 Pa.C.S. § 6337). Your lawyer has had your case for a day. The agency's lawyer has had the file for three.

Everything now depends on what the file in front of the judge actually contains. If Claudette's record has traveled, the judge reads a year of documented treatment and a prescription in context. If it has not, the judge reads a hospital chart, a medication line, and a form's characterization of both — plus whatever Estelle is, on paper, in the room.

The judge looks up. 'What do we have,' she asks, 'in writing?'

**Choices:**
- The treatment record is here: 'A year of documented treatment, Your Honor — the letter and summaries are in the agency's own file.' → **home_week**  _(REQUIRES FLAG: releaseSigned)_
  - NOTE (shown after choosing): This sentence exists only because a clipboard was signed on day two. The record traveled; now it can testify when you cannot.
- Iris goes to Estelle while the record is completed: 'Her grandmother is here, assessed on paper, and ready today.' → **estelle_week**  _(REQUIRES FLAG: estelleWritten)_
  - NOTE (shown after choosing): Kin, documented, present. The hearing takes the fallback the file can actually carry — because someone put it in the file.
- The hearing proceeds on the chart alone — and the chart is all it has → **stranger_visits**  _(REQUIRES NO FLAG: releaseSigned ; REQUIRES NO FLAG: estelleWritten)_
  - NOTE (shown after choosing): No treatment record, no kin paper. The judge is not choosing between you and a stranger; she is choosing between a chart line and a stranger. The chart line loses.

## [home_week] Home, Under a Plan
*Day 7 — Monday, March 9, 2026 (dayOffset 7)*

Iris comes home with you under an interim plan: check-ins, the clinic schedule continuing as it has for a year, Estelle named as support, a review hearing on the calendar. The discharge papers and the court papers leave the hospital in the same bag, which feels exactly as mixed as it is.

Home is not the end of the case; it is the beginning of the supervised version of your actual life. Iris learns the apartment's light. You learn to keep two folders now — the clinic binder's home copy, and the agency folder, growing its own spine.

What remains undone is in the second folder: the agency file has Claudette's letter now, but its oldest pages still carry the form's original wording, uncorrected, waiting to be quoted at the review as if it were the finding instead of the first draft.

**Choices:**
- Mark the review date, and then go feed your daughter in your own kitchen → **counselor_doc**
  - NOTE (shown after choosing): First things first. The paperwork war resumes Monday, against a deadline that is now printed on a court notice.

## [counselor_doc] Getting It Into Their File
*Day 9 — Wednesday, March 11, 2026 (dayOffset 9)*

A letter sent is not a letter filed. You learn this in the friendliest possible way: Ms. Sloane, on the phone, cannot find Claudette's summary in the agency file — it arrived, someone scanned something, the something is 'in the system.' Whose system is left as an exercise.

Claudette, unbothered, prints the complete documentation again: the letter naming the medication as prescribed treatment, the attendance record, the year of screens — and this time the delivery is the strategy: hand-carried, in writing, with a written request that it be placed in the agency case file, and a copy stamped as received.

Records that travel can still get lost at the destination. Records that are filed, with a receipt, have an address.

**Choices:**
- Deliver Claudette's documentation in person, in writing, and keep the stamped receipt → **packet_arrives**  _(FLAG: counselorFiled ; HIDDEN + Treatment record — counselor's letter, attendance, and screening history filed in the agency case file with receipt)_
  - NOTE (shown after choosing): Filed, stamped, receipted. The explanation now lives in the building that does the scoring.
- Let Claudette re-send it her usual way — clinics and agencies talk all the time → **packet_arrives**
  - NOTE (shown after choosing): They do talk. Files, however, do not listen; they contain. What this one contains by Friday is anybody's guess, including Ms. Sloane's.

## [packet_arrives] The Word in the File
*Day 14 — Monday, March 16, 2026 (dayOffset 14)*

The requested record arrives — your copy of the agency's file, released on your written request (55 Pa. Code § 3130.44(d)) — and there, in the assessment narrative, is the word Claudette predicted: 'use.' One word, doing the work of a year. The narrative describes the delivery, the medication line, and the characterization the line was given by a form that had never seen the clinic binder.

Below it, now, thanks to the last week's paper, sit the attachments that contradict it: Claudette's letter, the attendance record, the screens. The file currently contains both the accusation and its answer, stapled in that order.

Files are read by their first pages in busy rooms. An uncorrected first page with a correct appendix is a coin toss. A corrected first page is a decision somebody has to sign.

**Choices:**
- Read the narrative three times, then call your lawyer about one page: the correction → **correction_writing**
  - NOTE (shown after choosing): One word to change. The changing of it, done right, is a small ceremony of copies and dates.

## [correction_writing] Correcting 'Use' in Writing
*Day 15 — Tuesday, March 17, 2026 (dayOffset 15)*

The correction is one page, drafted with your lawyer and signed by you, with Claudette's documentation cited line by line: the word 'use,' as applied to a prescribed medication taken as directed within a documented, year-long treatment program, is corrected to what the record shows — treatment. It asks that the assessment narrative in the agency file be amended, and that the correction travel with the file to the review.

It is filed before the hearing — that timing is the entire point. A correction filed after a review is an argument about the past. A correction filed before it is evidence in the present, sitting in the file when the judge opens it.

Estelle, reading it over your shoulder, says the sentence grandmothers have said in every bureaucracy since record-keeping began: 'Make sure you keep your copy.' You keep three.

**Choices:**
- File the written correction before the review, with Claudette's documentation attached → **visit_week**  _(cash −10 ; FLAG: correctionFiled ; HIDDEN + Correction filed — 'use' corrected to documented treatment in writing, before the review hearing)_
  - NOTE (shown after choosing): Into the file, before the hearing, with receipts. The first page and the appendix now tell the same story.
- Raise the correction orally at the review — the judge will have the attachments anyway → **visit_week**
  - NOTE (shown after choosing): Oral corrections are heard by the room and forgotten by the file. The file is the member of this cast who attends every future hearing.

## [visit_week] The Visit That Is Also a File
*Day 18 — Friday, March 20, 2026 (dayOffset 18)*

Ms. Sloane's home visit finds the apartment as it is on a Thursday: Iris asleep in a bassinet that was Estelle's other daughter's, clinic appointment cards on the refrigerator in a row like a tiny parade, your folder and the clinic binder side by side on the table.

She is not the villain of this scene and does not audition for it. She notes the appointment cards. She notes Iris's weight gain from the pediatrician's printout. What a visit becomes, in this system, is a note — and a note, filed, is either 'mother's treatment ongoing, documented' or 'mother states treatment ongoing,' depending on whether the documents are in the file behind it.

Yours are. The note, this time, writes itself from evidence.

**Choices:**
- Give her copies of the week's appointment cards and the pediatrician printout for the file → **home_support**  _(HIDDEN + Home as observed — treatment appointments documented; infant thriving; records in the file, not just reported)_
  - NOTE (shown after choosing): More paper, offered before it was requested. The file's picture of this home is now mostly made of documents instead of impressions.

## [home_support] Estelle's Corner of the Plan
*Day 21 — Monday, March 23, 2026 (dayOffset 21)*

Estelle comes on Mondays and Thursdays, holds Iris with the competence of a woman defusing ordnance, and — because the plan names her as support — her presence is documented too: her signed page from the hospital week, updated with the standing arrangement, filed alongside the correction.

A kin fallback that exists on paper does double work in a case like this. It answers the review's hardest question — 'and if anything falters?' — with a name, an address, and a signature, instead of a hope. And it means the fallback, if it is ever needed, is family, arranged in advance, rather than strangers, arranged in an emergency.

**Choices:**
- Confirm Estelle's support page is filed and current before the review → **review_prep**
  - NOTE (shown after choosing): One phone call, one confirmation, one copy. The net under the plan is now a document, not a metaphor.

## [review_prep] The File, Assembled
*Day 24 — Thursday, March 26, 2026 (dayOffset 24)*

Your lawyer spreads the file the way the judge will meet it: first the original narrative, then — because they were filed before this hearing — the correction, Claudette's letter, the year's attendance and screens, Estelle's page, the visit notes. In that order, the file tells one story: treatment, documented; a word, corrected; a baby, home, weighed, and thriving.

Out of that order, it would tell three different stories depending on where a reader stopped. Order, in a file, is not cosmetics. It is the argument.

'We are not asking the court to believe you,' your lawyer says. 'We are asking it to read its own file, in full. That is a much stronger ask, and today it is ours to make.'

**Choices:**
- Go to the first review with the folder, the receipts, and Iris's feeding schedule → **first_review**  _(cash −15)_
  - NOTE (shown after choosing): Bus fare, copies, a bottle packed for a courthouse wait. Fifteen dollars against the whole architecture of the month.

## [first_review] The First Review
*Day 28 — Monday, March 30, 2026 (dayOffset 28)*

The review courtroom has heard a hundred versions of this morning. The agency's report is the file, read aloud at the speed of a docket — and the file, this time, corrects itself as it goes: the narrative's original word, the filed correction of it, the counselor's documentation, the visit notes, the kin page.

The judge's question is the same one from the shelter care hearing: 'What do we have, in writing?' The answer, this time, is a year long and signed by a clinic.

**Choices:**
- Ask the court to continue Iris at home on a plan whose file now contains the treatment record → **end_best**  _(REQUIRES FLAG: recordsRequested ; REQUIRES FLAG: counselorFiled ; REQUIRES FLAG: correctionFiled)_
  - NOTE (shown after choosing): This ask exists because three unglamorous things were done in writing and in time: the record requested, the documentation filed, the word corrected.
- The correction never reached the narrative — the review works from the original word, with Estelle as the answer → **review_to_estelle**  _(REQUIRES NO FLAG: correctionFiled)_
  - NOTE (shown after choosing): The attachments exist, but the first page still says 'use,' and first pages are what busy rooms rule from. Estelle's page is what saves Iris from strangers — and costs Shondra the home she had.
- The counselor's documentation never landed in their file — the review works from the chart and the correction alone, with Estelle as the answer → **review_to_estelle**  _(REQUIRES NO FLAG: counselorFiled)_
  - NOTE (shown after choosing): A correction without the documentation behind it is an assertion. Estelle's page, again, is what the room can act on.
- Their file was never requested — its narrative was never read in time to be answered in full, with Estelle as the answer → **review_to_estelle**  _(REQUIRES NO FLAG: recordsRequested)_
  - NOTE (shown after choosing): You cannot correct a file you have not read. What could be corrected was; what could not be read governed anyway.

## [review_to_estelle] The Review Moves Iris
*Day 28 — Monday, March 30, 2026 (dayOffset 28)*

The court's reasoning is short and, on the file in front of it, not even unreasonable: the narrative characterization stands uncorrected; the treatment documentation is present but unintegrated; the documented, assessed, willing kin placement is in the room. Iris is placed with Estelle while the characterization is sorted out and the mother — in the phrase the report will use — 'continues to demonstrate stability.'

Demonstrate. A year of demonstrated stability is in the attachments. What the court is asking her to demonstrate is not stability. It is paperwork — again, from the beginning, at the speed of a docket.

**Choices:**
- Kiss Iris at Estelle's door, and start the demonstration the court described → **end_estelle**
  - NOTE (shown after choosing): Estelle's spare room has been ready since before Iris was born. Readiness, it turns out, was never the scarce resource in this family. Believed paperwork was.

## [end_best] The Prescription Is a Fact
*Day 31 — Thursday, April 2, 2026 (dayOffset 31)*

Iris stays home. The first review continues her with you under the plan — check-ins, the clinic schedule that predates the case and will outlast it, Estelle named as documented support — and the case remains open, with the next review on the calendar. Nobody should call that closure. It is not closure. It is something rarer in this system than closure: a file that says what is true.

The agency file now contains the treatment record: Claudette's letter, the year of attendance and screens, the prescription named as the treatment it is. The word 'use' survives in the file only where it belongs — inside the correction, quoted, as the error it was.

Iris, who has slept through every decisive moment of her own case, wakes for the bus ride home and studies the folder on your lap with the seriousness of a reviewing judge.

**Ending.**

**Debrief:**
- THE BOARD, MAPPED — Placement track: Iris was placed in shelter care on Tuesday, March 3, 2026, heard within 72 hours on Thursday, March 5, 2026 (42 Pa.C.S. § 6332; 23 Pa.C.S. § 6315(d)), with counsel as provided by 42 Pa.C.S. § 6337, and discharged home under an interim plan; at the first review she remains home and the case remains open. This is a PARTIAL win, labeled honestly: supervision continues, the plan continues, and the next review will read this same file — which is precisely why what the file now contains matters. Record track: the releases were signed on day two (flag: releaseSigned), so the clinic's documentation could travel; the agency record was requested in writing (flag: recordsRequested; 55 Pa. Code § 3130.44(d)); Claudette's documentation was filed with a receipt (flag: counselorFiled); and the narrative's word 'use' was corrected to documented treatment in writing, before the review (flag: correctionFiled).
- What the hidden items show: the scored assessment form began from a hospital chart line — a prescribed medication, read as the story of the case — because the exculpatory record lived in a different building. Every winning move in this scenario is a record crossing a gap: across town (the release), into the right file (the filing), and into the narrative itself (the correction). Estelle's signed page (flag: estelleWritten) meant the plan's fallback was family on paper, which changed what every hearing had to fear.
- What was never in your control: the hospital's report, the form's original wording, the docket's speed, or which worker carried the file between buildings. A corrected file is not a verdict on Shondra Lachance — any more than the uncorrected word was. Outcomes in this system also turn on workers, judges, resources, and luck; this one turned additionally on a mother's willingness to sign, file, and correct paper while she was also learning to feed a newborn. The prescription was always a fact. Now the file says so.

## [estelle_week] Iris at Estelle's
*Day 7 — Monday, March 9, 2026 (dayOffset 7)*

Iris goes to Estelle's from the shelter care hearing — not home, and not to strangers, which in the arithmetic of this week counts as two different mercies. The spare room's nursery corner stops being 'just in case.' Shondra visits daily, feeds her, and does the night's hardest work at another address: leaving.

The reason for the placement is paperwork, and everyone in the family can recite it: the treatment record did not reach the hearing in usable form. Claudette's letter exists. The year exists. What does not yet exist is the record, in the agency's file, where a judge was able to read it in time.

So the demonstration begins — the same stability, performed a second time, for an audience of forms.

**Choices:**
- Set the visiting rhythm, and start rebuilding the record toward the review → **estelle_catchup**
  - NOTE (shown after choosing): Daily visits, a calendar on Estelle's refrigerator, and a list from Claudette titled, in her handwriting: 'Round Two — Paper.'

## [estelle_catchup] Re-Proving the Year
*Day 14 — Monday, March 16, 2026 (dayOffset 14)*

Round two has a bitter curriculum. The releases get signed now, late, and the documentation travels now, late — Claudette's letter, the attendance, the screens, the whole year arriving at the agency file a fortnight after the hearing that needed it. The correction gets drafted. Each document is dated, and each date confesses the same thing: this existed in March's first week, and was believed in March's third.

Shondra attends everything, again. Screens, again. Groups, again. Nothing about her stability changed between the hospital and this kitchen table. Only its documentation did — and documentation, it turns out, was the charge all along, wearing stability's clothes.

**Choices:**
- Carry the late-built file into the first review → **estelle_review**
  - NOTE (shown after choosing): Late paper is still paper. The review will decide what its dates are worth.

## [estelle_review] The First Review — Kin
*Day 28 — Monday, March 30, 2026 (dayOffset 28)*

At the review, the file is complete at last: the treatment record filed, the correction drafted and argued, the kin placement documented and thriving — Iris gaining, sleeping, held by a family that never had to be persuaded, only papered.

The court keeps Iris with Estelle for now: the documentation arrived, but it arrived after the placement it would have prevented, and courts move children more slowly than they move paper — especially, they say, a newborn who is settled. The plan's goal remains return home. Its timeline is now measured in reviews, not days.

**Choices:**
- Hear the goal stated aloud — return home — and get the next date in writing → **end_estelle**
  - NOTE (shown after choosing): A goal in writing, a date in writing. The family's two oldest technologies, applied to its newest member.

## [end_estelle] Placed With Family, Proving It Again
*Day 31 — Thursday, April 2, 2026 (dayOffset 31)*

Iris is with Estelle — fed, adored, twenty minutes from home and an entire procedure away from it. Shondra's days have a geography now: the clinic in the morning, her daughter at her mother's kitchen table, her own apartment's quiet in the evening, folder work at night.

Name the arrangement accurately, because accuracy is this scenario's whole subject: a baby is living with her grandmother while her mother re-proves, document by document, a stability that was documented all along. The proof was never missing. It was misfiled — in the wrong building, behind an unsigned form, under a word nobody corrected in time.

The goal is return home, in writing, with a date. Claudette has started a second binder. Its first page is the year's record — the same record. This time, it is already in the right building.

**Ending.**

**Debrief:**
- THE BOARD, MAPPED — Placement track: shelter care hearing within 72 hours of placement, on Thursday, March 5, 2026 (42 Pa.C.S. § 6332; 23 Pa.C.S. § 6315(d)), counsel under 42 Pa.C.S. § 6337; Iris placed with her grandmother — the kin exception to every worse outcome in this batch of endings — and continued there at the first review, with return home as the stated goal. Record track: the treatment documentation reached the agency file after the hearing that needed it; whether because the releases were signed late or because the narrative correction was never filed in time, the file at each decisive moment lagged one step behind the truth it contained in pieces.
- What the hidden items show: Estelle's signed page (flag: estelleWritten, if built) is the whole difference between this ending and stranger care — kin on paper is the fallback that survives contact with a courtroom. The treatment record itself was never in doubt: Claudette's clinic held a year of documented stability throughout. The failure this ending maps is a handoff failure — records 'traveling' without receipts, corrections spoken instead of filed — of the same kind documented across published dependency cases, where services and proofs are lost between workers, buildings, and files.
- What was never in your control: the hospital report that opened the case, the form's first characterization, or a court's reluctance to move a settled newborn twice. Re-proving a documented year is not a verdict on Shondra Lachance's recovery — the recovery is the best-documented fact in the file. Outcomes in this system also turn on workers, judges, resources, and luck, and on whether true paper arrives before or after the hearing that needed it. In this ending, it arrived after. The difference between that and the winning route is not effort, or sobriety, or love. It is dates.

## [stranger_visits] Visits in a Room With a Clock
*Day 9 — Wednesday, March 11, 2026 (dayOffset 9)*

Iris is placed with a foster family across the county — kind people, the visit note says, and the note is probably right; kindness was never the scarce resource in this story either. What was scarce was paper: no treatment record in the file at the hearing, and no kin availability on paper for the court to act on. Estelle was in the waiting room. The file was in the courtroom. Only one of them got a vote.

Visits happen at the agency, in a room with a wall clock and a sign-in sheet. Shondra is never late. The sign-in sheet, at least, begins a record that says so — the first record in this case that has ever been entirely in her favor, and she did not have to fight a form for it.

Claudette's voice, on the phone, is steel wrapped in patience: 'Then we build the file now, all of it, and we build it so the review cannot unknow it.'

**Choices:**
- Sign every release, file every page, and make the visit log a document too → **stranger_prep**
  - NOTE (shown after choosing): Late is a date. Never is a decision. The review is three weeks out, and three weeks of perfect paper is a different file than the hearing had.

## [stranger_prep] Building the File Late
*Day 23 — Wednesday, March 25, 2026 (dayOffset 23)*

The fortnight's work is an inventory of everything that existed on day one and reached the file on day twenty-something: the signed releases, Claudette's letter, the year of attendance and screens, the written correction of the chart's characterization, Estelle's page — signed at last, assessed at last, twenty minutes away all along.

Each document tells two stories: what it proves, and when it arrived. At the review, the agency's lawyer will tell the first story generously and the second one precisely. Courts, as this scenario keeps insisting, rule from the file in front of them — and from the dates in the margins of that file.

**Choices:**
- Go to the first review with the complete, late, honest file → **stranger_review**
  - NOTE (shown after choosing): No page in it is backdated, and none pretends. If dates are the charge, dates will also have to be the defense: look what she built, and how fast, once she knew.

## [stranger_review] The First Review — Strangers
*Day 28 — Monday, March 30, 2026 (dayOffset 28)*

The review agrees the file is now complete. It agrees Estelle is assessed and willing. It agrees the treatment record documents a year of stability, and that the chart's word for it has been corrected. It then does the thing courts do with newborns and completed files that arrived late: it moves slowly. Iris remains in the foster placement for this review cycle, with transition planning toward Estelle — and, beyond her, toward home — written into the plan as steps instead of as the outcome.

Shondra hears the word 'steps' the way you hear weather through a wall. Every step is a week of a newborn's life, and newborns measure weeks in doublings.

**Choices:**
- Get every step and date in writing before leaving the courtroom → **end_stranger**
  - NOTE (shown after choosing): If the plan is steps, the steps get dates, and the dates get kept where dates can be checked. It is the only move this case has ever offered, in any of its versions.

## [end_stranger] The Unsigned Page
*Day 31 — Thursday, April 2, 2026 (dayOffset 31)*

Iris remains, for this cycle, with strangers who are kind — in a home Shondra can find on a map and cannot enter uninvited, twenty minutes and one legal universe from Estelle's spare room, which is set up, assessed, documented, and empty.

Trace the causation without flinching, because this ending exists to have it traced: nothing about Shondra's treatment failed. Nothing about Estelle's willingness failed. What failed was a signature on day two, and everything downstream of it — the record that didn't travel, the hearing that read a chart line as a life, the placement that followed the paper instead of the family.

The file is complete now. Reviews will come, and transition steps have dates, and Claudette's second binder is open. The system's next chance to read this family correctly has been built, at full price, by the family.

**Ending.**

**Debrief:**
- THE BOARD, MAPPED — Placement track: shelter care hearing within 72 hours, Thursday, March 5, 2026 (42 Pa.C.S. § 6332; 23 Pa.C.S. § 6315(d)), at which — with no treatment record in the file (no releaseSigned flag) and no kin availability on paper (no estelleWritten flag) — Iris was placed with a foster family; at the first review the now-complete file earns transition steps toward kin and home, not an immediate move. Record track: the agency record request (55 Pa. Code § 3130.44(d)) and the clinic documentation all arrived after the hearing; the original scored narrative worked from the hospital chart's medication line alone.
- What the hidden items show: this ending is the purest handoff failure in the scenario — a documented year of treatment, a ready grandmother, and a stable mother, none of which were in the room where the decision was made because none of them were in the file that was in the room. The releases were never a formality; they were the bridge, and an unsigned bridge carries nothing. Note what did accumulate in Shondra's favor from the first visit onward: a sign-in sheet record of perfect attendance, built the moment she understood that in this system, everything true also has to be written.
- What was never in your control: the hospital's report, the form's first reading of the chart, the foster family's availability that week, or the court's pacing afterward. This ending is not a verdict on Shondra Lachance — the completed file affirmatively documents the opposite of the chart's implication. Outcomes in this system also turn on workers, judges, resources, and luck; here they turned on one unsigned page, which is why the scenario makes you watch the clipboard so closely on day two.
