#!/usr/bin/env python3
"""Generate scenarios 125-126 (Wave 2, Batch 9: Education & Medical).
Fictional composites only."""
import sys
sys.path.insert(0, "/home/hatch/workspace/your_files/tacticwatch-game")
from batchN_lib import N, C, E, emit, fmt
from datetime import date, timedelta

# ============================================================ S125 (Complex)
S = date(2027, 4, 5)
assert fmt(S) == "Monday, April 5, 2027"
NOTICE = S + timedelta(days=7)
assert fmt(NOTICE) == "Monday, April 12, 2027"                        # indicated notice
assert fmt(NOTICE + timedelta(days=90)) == "Sunday, July 11, 2027"    # appeal deadline (90 days)
HEARING = S + timedelta(days=65)
assert fmt(HEARING) == "Wednesday, June 9, 2027"                      # appeal hearing
DECISION = S + timedelta(days=81)
assert fmt(DECISION) == "Friday, June 25, 2027"                       # decision — 16 days after hearing, inside the 45-day window
assert fmt(S + timedelta(days=45)) == "Thursday, May 20, 2027"        # dependency adjudication

s125_meta = {
    "title": "The First 90 Days",
    "subtitle": "Scenario 125 — Page Nine of the Chart (a fictional composite)",
    "startDateISO": "2027-04-05",
    "startNode": "start",
    "startCash": 140,
    "tier": "Complex",
    "summary": "You are Bianca Torres. Your son Mateo, nine months old, was admitted Friday with bruises a baby his age should not be able to earn. The hospital chart that will decide two cases is 214 pages long. The agency's case rests on a two-page summary of it — and the summary never quotes page nine.",
}

s125 = [
 N("start", 0, "The chair by the bed",
   ["You have slept three nights in the chair the hospital provides for parents who are also, in some column of a form somewhere, suspects. Mateo — nine months old, not yet crawling, a baby whose entire transportation history is other people's arms — was brought in Friday from his well-baby visit, because his pediatrician found bruises: on his ear, his cheek, the soft places where bruises on a non-mobile infant are, in the language every professional in the building shares, *concerning*.",
    "The workup has been thorough and terrifying in equal measure: a skeletal survey, blood panels, specialists. No fractures. No prior injuries on the images. A baby who eats, sleeps, and tracks faces the way thriving babies do — with a body that bruises where the car-seat buckles press, where your own fingers lift him, where nothing has happened that anyone can name. The not-knowing is the worst of it. The second-worst is watching the not-knowing get written down, in other people's words, in real time."],
   [C("Write your own account of Friday — times, symptoms, who held him — while it is still Friday in your memory.", "what_happened")]),

 N("what_happened", 0, "Friday, as lived",
   ["Friday, as you lived it: the well-baby visit at ten; Dr. Vasquez's face changing at the ear bruise — you know her face; she has examined Mateo monthly since birth and has never once looked at you the way she looked at the bruise. The drive to the emergency department she directed, with Mateo asleep in the seat whose buckles you will think about for a year. The phrase *we need to rule some things out*, spoken by a resident, kindly, as a plan.",
    "Rule some things out. Hold that phrase. It will change jobs as it travels — from a task in a doctor's sentence to a conclusion in a file — and this case lives in the distance it travels."],
   [C("The county's investigator has asked to speak with you. Go in with Friday written down.", "investigator")]),

 N("investigator", 1, "The interview",
   ["Mr. Okonkwo is courteous, thorough, and — you notice, because you are looking — writing in a form whose boxes were printed before he met you. He asks about the bruises' origins, and your answers are the truth's least useful shape: *I don't know. That's why we're here. He bruises where the buckles are. I noticed the cheek one Thursday and thought it was the swing's strap.* Honesty about uncertainty, in an interview form, has a translation problem: the boxes offer *consistent* and *inconsistent*, and *I don't know* fits in neither.",
    "You watch him write. You cannot see the words. You will spend two months trying to read what was written in rooms you were sitting in — which is, in the end, the whole curriculum of this scenario."],
   [C("Get your account out of your memory and into a document before the week metabolizes it.", "nursery_detail")]),

 N("nursery_detail", 1, "Your own notes",
   ["Your phone's notes from Friday — timestamps the phone kept for you — list the morning in the order a mother lives it: the feeding, the visit, the drive, the names of everyone who held Mateo that week (you, Samira, the sitter for two hours Wednesday). You send the notes to yourself by email, because a lawyer in a television show once said something about timestamps, and because paper you control is the only paper in this case currently guaranteed to say what you said.",
    "It is the first document of your defense, and like most first documents in this library, it cost nothing but the decision to make it while the making was cheap."],
   [C("Samira is here — your mother, Mateo's grandmother, and the county's plan for where he sleeps next.", "samira_arrives")]),

 N("samira_arrives", 1, "Samira",
   ["Samira Torres has raised four children and buried one husband and she assesses the hospital room the way she assesses everything: completely, in one pass, and aloud. Her verdicts: the baby is thriving. The chair is an instrument of torture. The county wants Mateo placed with her on discharge, and she has already told them yes — *before* they finished asking, a detail she wants entered in whatever record records such things.",
    "\"Understand me, Bianca,\" she says. \"Him coming to my house is the good door. It is still a door they are holding. We walk through it like we own it, and we find out why my grandson bruises. Both things. In writing, both things.\""],
   [C("Your lawyer arrives tomorrow. Bring her Friday, the form you couldn't see, and your mother's two sentences.", "lawyer125")]),

 N("lawyer125", 2, "Two tracks, two clocks",
   ["Ms. Yilmaz maps the case as two machines running in parallel, in different buildings, on different clocks. Machine one: the dependency case — court, hearings, Mateo's placement; the agency must prove its allegations there by clear and convincing evidence. (42 Pa.C.S. § 6341(c)) Machine two: the ChildLine track — if the report about Mateo's bruises is marked *indicated* with your name as perpetrator, a separate administrative case begins, with its own appeal, its own evidence rule, and a clock that starts the day the notice reaches you: a written request to appeal, within 90 days of notification. (23 Pa.C.S. § 6341(a)(2))",
    "\"Inside that appeal, the law hands you two tools most people never hear about. You may demand the investigation evidence — all of it, including anything that helps you. (23 Pa.C.S. § 6341(c.2)(4)) And at the hearing, the burden is the *agency's* — it must support its determination with substantial evidence. (23 Pa.C.S. § 6341(c.2)(5)) The decision comes within 45 days of the hearing. (23 Pa.C.S. § 6341(c.3)) Both machines run on the same raw material, Bianca. A 214-page hospital chart. The whole case is whether anyone in either building ever reads it whole.\""],
   [C("Ask what the chart's page nine is — the page a nurse mentioned and no summary quotes.", "er_resident")]),

 N("er_resident", 2, "Rule out",
   ["The phrase's journey, reconstructed later from the chart itself, is the case in miniature. The emergency resident wrote: *bruising in non-ambulatory infant — rule out non-accidental trauma; consult hematology re: easy bruising.* A task list, in a doctor's grammar: possibilities to exclude, in order. In the investigator's intake note, the sentence returns wearing a uniform: *ER advises injuries consistent with non-accidental trauma.* A consultation was ordered by the same hand that wrote the suspicion. Both halves are in the chart. Only one half ever travels.",
    "\"Files quote conclusions,\" Ms. Yilmaz says. \"Charts contain processes. When a process gets quoted as a conclusion, the cure is not argument. The cure is the chart, whole, in the room, with the process's pages tabbed.\""],
   [C("The hospital's social worker finds you in the corridor — Ms. Quashie, with a folder of her own.", "quashie")]),

 N("quashie", 3, "The social worker",
   ["Ms. Quashie's job is the seam between the hospital and the county, and she works it with a fairness you will remember longer than the suspicion: she explains the hospital's reporting duty without apologizing for it or inflating it; she confirms the hematology consult was placed Friday; she tells you — because you ask, and because her notes will say the same — that her own chart entries describe a mother who has not left the chair in three days.",
    "\"My notes are factual,\" she says. \"Factual is the best thing a note can be. Make sure everyone's notes get read, not just the frightening ones. There are a lot of notes in that chart, Mrs. Torres. Some of them are yours now too.\""],
   [C("A nurse, refilling the water pitcher, says the thing about page nine.", "page_nine_rumor")]),

 N("page_nine_rumor", 3, "The page everyone cites",
   ["\"You're the mom?\" The nurse keeps her voice at corridor volume. \"The hematology consult — Dr. Whitby — his note is the one the doctors keep talking about. It's early in the chart. Page nine of the consult section. If anyone ever asks you what the chart says, ask them if they've read page nine.\" She is gone before you can ask the question properly, which is how most crucial information in hospitals travels: at walking speed, between tasks.",
    "Page nine. You do not have the chart. You do not yet have the right paper to demand it. But you have the two things demands are built from: a specific page, and the knowledge that the summaries have never quoted it."],
   [C("The kinship paperwork for Samira's placement is ready. Read every line before anyone signs.", "kinship_paper")]),

 N("kinship_paper", 3, "The good door, in writing",
   ["The emergency kinship papers place Mateo with Samira on discharge: her home, her clearances expedited, your visits to be arranged through the agency. You read all of it — Samira insists, tapping each page — and sign as what you are: his mother, consenting to his grandmother, inside a system that has not yet decided what else you are.",
    "Samira signs below you. \"There,\" she says. \"Now the family is in the file in its own handwriting. Everything from here is about making the rest of the file catch up.\""],
   [C("Discharge day. Mateo goes to Samira's. You go home to an apartment with a crib in it, and two clocks running.", "discharge")]),

 N("discharge", 4, "The summary in your hand",
   ["The discharge packet includes the agency's two-page case summary, and you read it in Samira's kitchen while Mateo sleeps in the room where you grew up. The summary is competent, calm, and wrong in the specific way of documents written from other documents: *Injuries consistent with non-accidental trauma per ER. Laboratory work: pending.* The labs resulted on Saturday. The consult was written on Sunday. The summary is dated Monday — and in its two pages, the word *hematology* does not appear, page nine does not exist, and your Friday is summarized as *caregiver unable to explain injuries*.",
    "A two-page summary of a 214-page chart is not a lie. It is an editorial decision with the force of fact — and it is currently the only version of Mateo's April that any decision-maker has read."],
   [C("Ask Ms. Yilmaz for the chart and the file — all of it, in writing, this week.", "records125")]),

 N("records125", 6, "The whole chart",
   ["The requests go out in writing, in parallel, through counsel: the agency's case record, releasable on request (55 Pa. Code § 3130.44(d)) — and the hospital's complete chart, on your signed authorization as Mateo's mother, every section, consults included. Ms. Yilmaz's covering instruction is the scenario's thesis in one sentence: *Do not summarize the chart back to me. Bring me the chart.*",
    "Files answer lists; charts answer authorizations. Both are now in the mail, with receipts."],
   [C("Sign everything, date everything, keep the copies in Samira's kitchen drawer — the family archive.", "notice_day", setFlags=["recordsRequested"], cash=-13, addHidden=["Record — agency record and complete hospital chart requested in writing"]),
    C("Hold the requests until the indicated notice arrives — no sense demanding a chart for a determination that may come out unfounded.", "notice_day")]),

 N("notice_day", 7, "Indicated",
   ["The letter comes Monday, April 12, 2027, in the envelope whose design you will now recognize forever. The report concerning Mateo's bruises has been determined *indicated*. You are named as the perpetrator. The status will be recorded in the statewide database, with the consequences the letter lists — child-care and school clearances among them, which is to say, among other things, your job at the daycare center where you have worked for two years.",
    "And at the letter's end, in the paragraph most recipients never reach, the machinery of appeal: a written request may be made within 90 days of this notification. (23 Pa.C.S. § 6341(a)(2)) Notification: April 12. Ninety days: Sunday, July 11, 2027. The window is printed. It is already open. It is already closing."],
   [C("The chart arrives this week. Read it the way its authors hoped someone would: whole.", "chart_arrives")]),

 N("chart_arrives", 10, "Two hundred fourteen pages",
   ["The chart arrives as a secured file and a printed stack Samira insists on — *computers hide pages; paper shows them* — and the stack takes over the kitchen table where the kinship papers were signed. You read in the order the week happened: admission, survey (no fractures, no prior injury), the resident's note with its task list, the panels resulting one by one — and on page nine of the consult section, tabbed now in three colors, Dr. Whitby's note.",
    "It is not a vindication. It is better than a vindication, because it is a document: a platelet-function result in the abnormal pattern; a confirmatory panel ordered; and the sentence, in a hematologist's level hand: *Bruising distribution is also consistent with a bleeding diathesis under active evaluation; clinical correlation is essential before attribution of mechanism.* Also consistent with. Under active evaluation. Before attribution. The chart had been saying *not yet known* on page nine, in writing, since Sunday — while every summary downstream said *known*."],
   [C("Lay the summary and the chart side by side. The appeal is built from the distance between them.", "summary_vs_chart")]),

 N("summary_vs_chart", 12, "Side by side",
   ["The exercise takes an hour and produces the case's central exhibit: a two-column page in Ms. Yilmaz's hand. Left, the summary: *consistent with non-accidental trauma; labs pending; caregiver unable to explain.* Right, the chart: *rule out non-accidental trauma; labs resulted Saturday, abnormal pattern under evaluation; mother appropriately concerned, present throughout, explanations consistent with the documented unknowns.* Every word on the left is traceable to the chart. Every trace is a place where the chart said more.",
    "\"This is the appeal,\" Ms. Yilmaz says. \"Not your innocence — I can't file that. The distance between a chart and its summary, measured in the agency's own documents. At the hearing, *they* carry the burden, by substantial evidence. (23 Pa.C.S. § 6341(c.2)(5)) Substantial evidence is evidence a reasonable mind could accept — and we are going to ask, page by page, whether a reasonable mind could accept the summary over the chart it summarizes.\""],
   [C("Align your Friday phone notes against the chart's timestamps — your memory, corroborated by both.", "phone_notes")]),

 N("phone_notes", 12, "Aligned",
   ["Your phone notes and the chart's timestamps interlock without forcing: the feeding at seven; the visit at ten; Dr. Vasquez's examination; the drive; the resident's questions; the times you were in the cafeteria (twice, documented by receipts you did not know were evidence). The sitter's two hours on Wednesday are confirmed by her text thread. Nothing in the alignment is dramatic, which is its power: your account survives contact with the institution's own clocks.",
    "Ms. Yilmaz files the alignment as an exhibit with a one-line cover: *Respondent's account, corroborated by the record's timestamps.* Respondent. In the appeal's grammar, the agency defends its determination and you are the one asking questions. The grammar itself is half the therapy."],
   [C("File the appeal — and choose what kind of appeal it is.", "appeal_choice")]),

 N("appeal_choice", 13, "Bare or built",
   ["The appeal, Ms. Yilmaz explains, is a written request — and a choice about what kind. The bare request preserves the right and nothing more: a letter, a date, a hearing someday on the file as it stands — which is the summary's file. The built request does the thing the statute built for this exact case: it invokes your right to the investigation evidence, all of it, including anything that helps you (23 Pa.C.S. § 6341(c.2)(4)), and it puts the chart — paginated, tabbed, page nine first among equals — into the appeal record from the first filing.",
    "The window runs to Sunday, July 11, 2027. There is no version of this where waiting improves the paper."],
   [C("File the built request: the appeal, the evidence demand under (c.2)(4), and the chart — this week, in April, while the window is young.", "registry_letter", setFlags=["appealBuilt", "cpslEvidence"], addHidden=["Appeal — written request filed within the 90-day window, demanding the complete investigation evidence"]),
    C("File the bare request now to stop the clock, and build the evidence later, as it comes.", "registry_letter", setFlags=["appealFiled"]),
    C("Let the appeal wait. The dependency court will sort out the facts, and the registry can be dealt with after.", "registry_letter")]),

 N("registry_letter", 18, "What 'indicated' does meanwhile",
   ["The consequences do not wait for July. Your daycare employer, running a scheduled clearance renewal, receives the flag the notice promised; your director — who has watched you with toddlers for two years and says so, miserably — places you on unpaid leave pending the appeal, because the clearance rules leave her no discretion she can sign her name to. The appeal is now about a chart, a baby, and a paycheck, in ascending order of how often you think about them at 3 a.m.",
    "Ms. Yilmaz is blunt about the sequencing: \"This is why the appeal gets built in April. The registry does not pause while families deliberate; neither do we.\""],
   [C("The (c.2)(4) production arrives — the investigation's own file, complete, including what helps you.", "evidence_packet")]),

 N("evidence_packet", 20, "The investigation's file",
   ["The evidence production — the agency's statutory answer to the demand — arrives in a fat folder, and its contents vindicate the demand's design: the file the determination actually rested on. The investigator's intake note (the resident's task, uniformed). The interview form (your *I don't know*, boxed). And on a page the determination never cited, Dr. Vasquez's own statement to the investigator, taken the first week: *Mother appropriately sought care; no prior concerns in nine months of visits; family compliant with all follow-up.*",
    "Exculpatory evidence is a legal phrase. In a kitchen, it looks like this: the pediatrician who started the case also documented its strongest defense, and the determination proceeded as if she had only ever written the first half of her opinion. She wrote both halves on the same day."],
   [C("Read the investigator's notes the way Ms. Yilmaz taught you: as a timeline of a task becoming a conclusion.", "investigator_notes")]),

 N("investigator_notes", 24, "The timeline",
   ["The notes, dated, tell the transformation in four entries. April 2: *rule out NA trauma per ER; hematology consulted.* April 3: *injuries consistent w/ NA trauma (per ER).* April 5: *determination meeting — indicated recommended; medical workup ongoing.* April 6: *Whitby note received; to file.* The consultation the first entry ordered produced the page the fourth entry filed — and the determination, made on the third day, between them, never waited for its own order to come back.",
    "\"Substantial evidence,\" Ms. Yilmaz says, \"is supposed to be evidence that has finished happening. Their determination interrupted its own workup and called the interruption a conclusion. That is the hearing, in one timeline — and the timeline is *their* document, produced under *their* duty. This is why we demanded the file instead of arguing with the summary.\""],
   [C("One author remains: Dr. Whitby. Ask him, through counsel, to clarify page nine in writing for the hearing.", "whitby_contact")]),

 N("whitby_contact", 27, "The author of page nine",
   ["The request to Dr. Whitby is careful in the way of letters to busy specialists: not advocacy, but clarification — whether his page-nine assessment stands; what the confirmatory panel (now resulted) establishes; and whether the bruising pattern, on the completed record, is explained by the documented condition in his clinical judgment. His reply, when it comes, is a two-page letter on hospital letterhead that Ms. Yilmaz reads aloud in her office, slowly, the way people read weather they have prayed for.",
    "He stands by page nine in full. The confirmatory testing has since documented the bleeding disorder his note predicted was under evaluation. In his judgment, the bruising pattern is explained by it. The letter closes with a sentence about process, not about you: *Attribution of mechanism in such cases should await completion of the medical workup.*",
    ],
   [C("Take the letter — the author, clarifying his page, on letterhead, for the record.", "samira_visit", setFlags=["whitbyLetter"], addHidden=["Medical — consulting specialist's written clarification: completed workup documents a bleeding disorder explaining the bruising pattern"]),
    C("Leave page nine to speak for itself. Specialists dislike being exhibits; don't spend his goodwill.", "samira_visit")]),

 N("samira_visit", 29, "Samira's log",
   ["Samira, meanwhile, has been keeping the document nobody requested and everybody will read: a placement log, in her schoolteacher's hand — feedings, sleeps, and, from the second week, bruises. New ones. Small, ordinary, appearing at the rate of childhood on a baby who bumps a crib rail and bruises like a peach, under the eyes of a grandmother nobody suspects, documented by the agency's own visit supervisor, who writes *consistent with prior pattern* in the margin of the visit note and goes home.",
    "Bruising that follows the baby — to a new house, a new caregiver, under supervision — is not a caregiver's signature. It is a condition's. The log is the condition's diary, kept by the most credible witness in the case: the woman the county itself chose."],
   [C("File the log with counsel — pattern evidence, in the placement's own handwriting.", "dependency_track", setFlags=["samiraLog"], cash=-6),
    C("Keep the log in the family. Samira's kitchen table doesn't need to become an exhibit hall.", "dependency_track")]),

 N("dependency_track", 32, "The other machine",
   ["The dependency case has been running its own track all spring: Mateo thriving at Samira's under the emergency placement, your supervised visits unblemished, and adjudication set for Thursday, May 20 — where the agency must prove its petition by clear and convincing evidence (42 Pa.C.S. § 6341(c)), on allegations that lean heavily on the same bruising the chart has been busy re-describing. Ms. Yilmaz's two machines share a fuel line, and she tends it deliberately: every page the appeal builds is filed in the dependency record too, because judges in one room read what lawyers file in both.",
    "The pediatrician's nine months of notes get their own filing this week — Dr. Vasquez's longitudinal record, requested and produced, in which the words *concern about this family* do not appear until the morning she found the bruise and did exactly what she was supposed to do about it."],
   [C("Prepare for May 20 with the chart in both files — and the workup now completing.", "second_pediatrician")]),

 N("second_pediatrician", 36, "Nine months of visits",
   ["Dr. Vasquez's records letter is a model of the genre this library keeps celebrating: dates, weights, immunizations, a mother's questions recorded with their answers — nine months of ordinary, documented, appropriate care, ending with the morning she escalated a finding she did not understand. Her cover note is one sentence: *This family has never given me cause for concern; on April 2 I had a concern about a finding, and I acted on it as I am required to.*",
    "A reporter who reports carefully is the system's best citizen — and, it turns out, its best witness. The same diligence that started the case now testifies about its subject."],
   [C("The confirmatory workup completes. Read the addendum the way April taught you: whole, and for its dates.", "workup_explainer")]),

 N("workup_explainer", 40, "What 'confirmed' takes",
   ["Confirmatory testing in hematology runs on its own calendar: the repeat panel, the specialist assays, the correlation of results across draws. Through April and into May the chart grows the pages April lacked — each one narrowing the distance between *under active evaluation* and a documented conclusion. Samira's log grows in parallel: bruise, date, location, circumstance — the condition annotating itself weekly in a grandmother's handwriting.",
    "Waiting, in this phase, is not passivity. It is the evidence completing itself. The adjudication will be the first room where the chart is longer than the suspicion."],
   [C("May 20. The dependency adjudication.", "adjudication125")]),

 N("adjudication125", 45, "Thursday, May 20",
   ["The dependency adjudication runs on the burden the law assigns it (42 Pa.C.S. § 6341(c)), and the record it reads is not April's: the completed chart, the specialist's letter, the pediatrician's nine months, a grandmother's log in which bruising follows the baby rather than any pair of hands. The court continues Mateo's placement with Samira — the medical situation wants a managed transition, and the court says so without finding the petition's dark version of April proven; the agency's dependency theory is, in the judge's phrase, *in substantial part overtaken by the medical record*. Services continue; your visits expand; the case is expressly held open pending the June appeal hearing, whose record the court adopts as its own going forward.",
    "One machine has now read the chart whole. The other machine — the one with your name in a database and your job on leave — reads it on June 9."],
   [C("The confirmatory addendum lands in the chart. Then: the appeal hearing's final build.", "workup_complete")]),

 N("workup_complete", 52, "The addendum",
   ["Dr. Whitby's addendum enters the chart in late May: the repeat panel results, correlated; the diagnosis documented in the chart's own language — a mild inherited bleeding disorder, now named, with a management plan (activity guidance, a medication alert, a specialist follow-up schedule) that Mateo will carry in every future file, where it will protect him in exactly the rooms where its absence endangered his mother.",
    "Page nine has become a section. The section has become the chart's center of gravity. And the summary that started everything — two pages, *labs pending* — sits in the appeal packet where Ms. Yilmaz put it: as the first exhibit, under the tab labeled *what was decided from*."],
   [C("Ask Mateo's guardian ad litem where she stands for June.", "gal125")]),

 N("gal125", 56, "The guardian ad litem",
   ["Mateo's GAL has read the whole chart — she says so with the emphasis of a woman distinguishing herself from most of the spring. Her position for the appeal is aligned and will be stated: the determination cannot survive its own medical record; her client's interests are served by a caregiver determination that matches his diagnosis, and by a grandmother's placement that nobody in the case any longer needs to pretend is a precaution against his mother.",
    "Coalitions in this system form the way they formed here: not around a mother's innocence, which no document can hold, but around a record, which documents can."],
   [C("Final build: the packet, paginated, page nine first among equals.", "hearing_prep125")]),

 N("hearing_prep125", 58, "Paginated",
   ["The appeal packet is assembled the way appeals are won: the determination; the summary it rested on; the chart entire, with page nine and the addendum tabbed; the (c.2)(4) production, including the pediatrician's uncited half and the four-entry timeline; the specialist's letter; the grandmother's log; the dependency order adopting the medical record. Ms. Yilmaz's brief argues one proposition in four registers: the agency's determination must be supported by substantial evidence (23 Pa.C.S. § 6341(c.2)(5)), and a determination made mid-workup, from a summary that omitted the workup, is not supported by the record the workup became.",
    "\"We are not asking the hearing officer to believe you,\" she says. \"We are asking her to read. Belief follows reading, in the cases where it follows anything.\""],
   [C("The agency's counsel calls the week before the hearing. Listen.", "ansel_whiteboard")]),

 N("ansel_whiteboard", 60, "The burden, drawn",
   ["The call is professional: the agency has reviewed the packet — the whole packet, evidently, some of them for the first time — and wishes to explore resolution. Before you hear its terms, Ms. Yilmaz draws the hearing's geometry one last time. Their burden. Their determination. Your evidence — which is, almost entirely, *their own documents*: the chart the hospital wrote, the file the agency produced, the log their chosen caregiver kept. \"There is no witness in this case they can impeach,\" she says, \"because our witnesses are their files. Whatever they offer, measure it against the whole chart. They will.\"",
    "What they offer arrives by letter the next day."],
   [C("Read the offer.", "agency_offer")]),

 N("agency_offer", 61, "The offer",
   ["The agency offers to amend the report's narrative — to append a note recording that 'subsequent medical evaluation identified a bleeding disorder' — while the *indicated* status, your name's place in the database, and the clearance consequences remain exactly as determined. The appeal would be withdrawn as moot-by-amendment. It is framed as grace. It reads, to a woman on unpaid leave, as the summary's philosophy in a new costume: the status was the point; the story is negotiable.",
    "Ms. Yilmaz states the trade without decorating it: \"Accept, and the database keeps the word and your job keeps the leave, with a nicer paragraph attached. Decline, and a hearing officer reads 214 pages with the burden on them. There is a version of prudence that takes the paragraph. It is not the version that gets your clearance back.\""],
   [C("Decline. The chart goes to a hearing; the burden goes where the statute put it.", "hearing_eve"),
    C("Accept. A documented medical note in the report is real, and hearings are gambles you cannot afford on unpaid leave.", "hearing_eve", setFlags=["offerAccepted"])]),

 N("hearing_eve", 64, "The night before",
   ["Samira makes the dinner nobody eats much of and produces, as her contribution to the packet, the log's final entry in her schoolteacher's hand: *Mateo, 9½ months. Bruise, left shin — crib rail, Tuesday. Doctor's plan followed. Baby thriving. Mother present for bath, as every night she is permitted.* She closes the book with the air of a woman shelving a text whose argument is complete.",
    "Tomorrow the chart is read aloud in the only room where reading it is the agency's legal problem. Sleep the way litigants sleep: in shifts, with the folder by the door."],
   [C("June 9. The appeal hearing.", "hearing_day125")]),

 N("hearing_day125", 65, "Wednesday, June 9",
   ["The appeal hearing is a smaller room than the dependency court and a longer day than anyone scheduled. The agency presents its determination and its evidence — the summary, the interview, the intake note — and defends them as a reasonable reading of an April record. Then the record itself is presented: page nine, the addendum, the specialist's letter, the four-entry timeline, the uncited pediatrician, the log. The burden's location matters in the room's physics (23 Pa.C.S. § 6341(c.2)(5)): the questions all run one way — *what did you have, when did you have it, and what did you do with page nine* — and the answers are documents.",
    "The hearing officer takes the matter under advisement. The statute gives her a window: a decision within 45 days of the hearing. (23 Pa.C.S. § 6341(c.3)) Forty-five days of waiting, measured against an April of deciding-in-three."],
   [C("Wait — with the reconsideration clocks learned in advance, in case the reading goes wrong.", "waiting_decision")]),

 N("waiting_decision", 74, "The window",
   ["The waiting weeks have their own curriculum: Mateo, at Samira's, acquiring teeth and bruises in the documented manner; your visits expanded by the dependency court's order; the daycare's leave clock running beside the hearing officer's. Ms. Yilmaz uses the window to draft, in advance, both futures: the expungement's paperwork if the reading goes right — and if it goes wrong, the short clocks that follow an adverse decision: reconsideration requested within 15 days, and the Commonwealth Court within 30. (23 Pa.C.S. § 6341(g))",
    "\"Short windows,\" she says, \"are survived by people who drafted during the long one. Whatever June 25 says, we will not be starting from a blank page. Nothing in this case will ever again be decided from a summary of us.\""],
   [C("Have both drafts ready. Then open the decision when it comes.", "reconsideration_prep")]),

 N("reconsideration_prep", 78, "Both drafts",
   ["The two drafts sit in the folder like the two doors of every case in this library. Behind one: the administrative paperwork of a corrected status — the database entry resolved, the clearance restored, the employer's letter answered with an official document. Behind the other: the reconsideration request, pre-drafted to the record, and behind that the court in Harrisburg or Philadelphia where judges read charts for a living.",
    "You have done the thing this scenario exists to teach, in both directions: the record is whole, the burden was theirs, the clocks are known, and the next step — either next step — is already written. All that remains is which door June opens."],
   [C("Friday, June 25, 2027. The decision.", "decision_day")]),

 N("decision_day", 81, "Friday, June 25",
   ["The decision arrives sixteen days after the hearing — inside the statute's window (23 Pa.C.S. § 6341(c.3)) — as a document, the way everything in this case arrives. What it holds is the sum of what April and May put in front of it: a chart read whole, or a summary defended; a burden carried, or a burden assumed. The envelope is thin. They always are. The thickness was in the record."],
   [C("The determination cannot stand on the record it interrupted: unsupported by substantial evidence against the whole chart — page nine, the addendum, the author's own clarification — the indicated report is reversed and ordered expunged.", "end_whole_chart", requiresFlags=["cpslEvidence", "whitbyLetter"]),
    C("The determination survives on the summary's reasonableness in April — but the record for reconsideration is complete, paginated, and already drafted against.", "end_reconsidered", requiresFlags=["cpslEvidence"]),
    C("The determination stands as it was made — on two pages, in three days, from a chart no one in the chain ever read whole.", "end_summary_stands")]),

 E("end_whole_chart", 81, "Ending — The Whole Chart",
   ["The hearing officer's decision is eleven pages, and it does not call you a good mother or the agency a bad actor. It does something more useful: it weighs the determination against the record and finds the record wanting on the agency's side of the scale. A determination issued mid-workup, resting on a summary that omitted the consultation the workup existed to obtain, is not supported by substantial evidence (23 Pa.C.S. § 6341(c.2)(5)) — not when the completed chart documents a bleeding disorder that explains the findings, a pediatrician whose exculpatory statement sat uncited in the agency's own production, and a specialist whose page nine said *before attribution* in writing from the first Sunday. The indicated report is reversed; expungement is ordered; the database entry and its clearance consequences unwind on the decision's paperwork, and your employer's next letter from you has an official document in it.",
    "Name the machinery honestly. The dependency case is not over: Mateo remains with Samira tonight under a court order, your visits expanded, the transition home to be managed on the medical plan — this ending is a complete win on the indicated track and a strong position, not a conclusion, on the dependency track. What won the appeal was procedural in the deepest sense: a written request inside the 90-day window (23 Pa.C.S. § 6341(a)(2)); the investigation evidence demanded and produced, exculpatory pages included (§ 6341(c.2)(4)); the burden kept where the statute places it (§ 6341(c.2)(5)); and a chart read whole — requested in writing under the record regulation (55 Pa. Code § 3130.44(d)), its key author asked to clarify his own page. Determinations made from summaries fall to records read entire. That is the doctrine, and June 25 is its proof of concept.",
    "What no strategy controls: a hearing officer who weighed April's reasonableness over June's record; the disorder itself, which Mateo carries for life, with a plan; the dependency calendar, which continues. But the file that follows this family now contains a diagnosis where a suspicion used to be, a decision that quotes page nine, and a grandmother's log in which a baby bruises, thrives, and is believed — in that order, permanently, in writing."]),

 E("end_reconsidered", 81, "Ending — Sixteen Days, and the Next Door (partial)",
   ["The decision upholds the determination — on the ground, stated plainly in its pages, that the April record *as the agency held it* made the finding reasonable when made. It is the ending this scenario most owes its readers honesty about: burdens are carried or not on the day, and a hearing officer who reads for the determination's moment rather than the chart's completion can find substantial evidence in a summary a different reader would call an IOU. The status stands. Your leave stands. The database keeps its entry — for now, and the *for now* is load-bearing: the reconsideration request, drafted during the waiting window, goes in within its 15 days (23 Pa.C.S. § 6341(g)), with the Commonwealth Court's 30 days behind it, and the record those forums will read is the whole chart, paginated, with the specialist's clarification and the uncited pediatrician — a record built, this time, to survive being read at any altitude.",
    "Account for what the April work bought even in loss. The appeal was filed inside the window; the evidence was demanded and produced (23 Pa.C.S. § 6341(c.2)(4)), which is why the pediatrician's exculpatory page and the four-entry timeline exist as exhibits rather than as a mother's claims; the dependency court has already adopted the medical record, which is why Mateo is thriving at his grandmother's under expanding visits instead of lost in a stranger placement. A determination upheld on its April reasonableness now has to survive review against June's chart — a materially worse position for it than the one it enjoyed in the spring.",
    "Partial, then, in the strict sense: the battle's first forum is lost and its record is won. It is worth noticing — the training point of this ending — that every asset for the next door was created by the same April decisions: the written requests, the evidence demand, the specialist's letter, the grandmother's log. Appeals are ladders. This one was built while the first rung was being sawn at, which is the only way ladders in this system ever get built."]),

 E("end_summary_stands", 81, "Ending — Two Pages",
   ["The decision upholds the determination, and the reason fits in the space the case was always fought over: on the record presented — the summary, the interview form, the intake note — the finding was one a reasonable mind could accept. The chart's 214 pages were not in the record presented, or not in it as an organized whole: the request that would have produced them was never written, or the evidence demand never made, or page nine was left to speak for itself in a room where documents do not speak unless someone paginates them. Your name remains in the database. The leave becomes a resignation. Mateo remains at Samira's — the one mercy the spring arranged — while the dependency case proceeds on a theory its own medical record has quietly abandoned.",
    "The autopsy is this library's doctrine in its starkest form. The determination was never strong; it was *unopposed by its own file*. The tools were printed in the notice letter itself: a written appeal within 90 days (23 Pa.C.S. § 6341(a)(2)); a right to the investigation evidence, including the exculpatory pages (23 Pa.C.S. § 6341(c.2)(4)); a burden on the agency that a complete chart makes nearly impossible to carry (23 Pa.C.S. § 6341(c.2)(5)). Every one of them is free. Every one of them is a letter. The summary stands not because it was persuasive but because it was, in the end, the only complete document in the room.",
    "Not sealed — reconsideration's 15 days and the Commonwealth Court's 30 (23 Pa.C.S. § 6341(g)) run from the decision, and late-built records have won later forums in this system's real history; the chart still exists, page nine still says what it says, and a grandmother's log is still growing. But the doctrine has no gentler formulation: in the first ninety days, the side that reads the whole record and files it usually beats the side that summarizes it — and when both sides summarize, the first summary wins. It was two pages long. It usually is."]),
]
emit(125, s125_meta, s125, S, "an infant's hospital workup, an indicated report, and an administrative appeal. No graphic content; injuries are discussed clinically and through paperwork.")

# ============================================================ S126 (Complex)
S = date(2027, 3, 1)
assert fmt(S) == "Monday, March 1, 2027"
assert fmt(S + timedelta(days=14)) == "Monday, March 15, 2027"     # placement move
assert fmt(S + timedelta(days=38)) == "Thursday, April 8, 2027"    # permanency hearing
CARE = date(2026, 6, 12)
assert fmt(CARE + timedelta(days=457)) == "Sunday, September 12, 2027"  # 15 calendar months in care

s126_meta = {
    "title": "The First 90 Days",
    "subtitle": "Scenario 126 — In Her Own Words (a fictional composite)",
    "startDateISO": "2027-03-01",
    "startNode": "start",
    "startCash": 130,
    "tier": "Complex",
    "summary": "You are Shirley Trejo. Your daughter Destiny, sixteen, is being moved to a new foster home in two weeks. She has three demands — her school, her classes, and an answer about her medication — and one discovery: in the agency's reports, everything she says is being paraphrased. 'Some reluctance' is about to meet the girl who actually said it.",
}

s126 = [
 N("start", 0, "The move",
   ["Mrs. Asare is closing her foster home — her own mother's illness, another county, a life rearranging itself the way lives do, with two weeks' notice to everyone it touches. Destiny, sixteen, nine months into care, will move on Monday, March 15. The options on the table are a family foster home — Mrs. Halden's, across the district line — or a group placement nearer, which Destiny has already described, in the visit room, at full volume, as 'a facility with better PR.'",
    "You are Shirley Trejo. You have been housed for six months, employed for five, and compliant with a plan whose hardest requirement — stability — you have finally, expensively, achieved. April's permanency hearing is five weeks out. And your daughter has just informed you, with a barrister's calm, that she has demands."],
   [C("Hear them in order. She has clearly rehearsed this.", "destiny_reaction")]),

 N("destiny_reaction", 0, "Three demands",
   ["\"One: I keep my school. Junior year is not a draft, Mom. My AP classes are there, my counselor is there, and I am not starting over in a building where nobody knows me in March of junior year. Two: fix my classes — they dropped my AP enrollment in January and nobody can tell me why, which means nobody tried. Three: somebody asks Dr. Iyer, in writing, why the evening pill eats my evenings — I fall asleep at eight like a toddler and my grades are eating it — and the answer comes back to *me*, not to a file.\"",
    "A pause. \"And zero — before one. Whatever gets decided, it gets decided with my actual words in the room. Not the summary. I've seen the summary.\" She has. That is the next scene."],
   [C("Ask her what the summary says.", "backstory126")]),

 N("backstory126", 1, "How Destiny got here",
   ["The record, fairly and briefly: your eviction last spring, the couch-surfing summer, Destiny's attendance collapsing as the family's address did — a sixteen-year-old cannot get to school from a different couch every week, and the petition, when it came, described the result accurately. She entered care on June 12, 2026. The fifteen-month date on her case — the point where the law's termination-petition question arrives, with its exceptions — is Sunday, September 12, 2027. (42 U.S.C. § 675(5)(E)) Not this spring's fight. But the reason this spring's record matters more than it looks.",
    "Mrs. Asare's home gave Destiny a year of ordinary life: her school, her counselor, her AP track, her friends. The move threatens all of it — not through anyone's decision, but through the usual mechanism: nobody deciding, in writing, in time."],
   [C("Your lawyer, Mr. Yusuf, gets the three demands and demand zero. Ask him how each becomes paper.", "lawyer126")]),

 N("lawyer126", 2, "Three fights, four papers",
   ["Mr. Yusuf maps the demands to machinery with a advocate's economy. The school: a placement change triggers the same federal structure as any other — she remains in her school of origin unless a determination, based on all factors relating to her best interest, decides otherwise (20 U.S.C. § 6311(g)(1)(E)(i)) — and the determination must be *asked for in writing* before the move, or the default decides it by envelope. Transportation has its own written procedures and its own three funding doors: agency reimbursement, district payment, or shared. (§ 6312(c)(5)(B))",
    "The classes: a records problem — her file, requested by name, from every school that has held it. The medication: a questions problem — her questions, in writing, through counsel and her guardian ad litem, to the prescriber, whose answers then exist. And demand zero, which he calls the master key: \"A written statement, in her words, filed verbatim with the agency and the court. Paraphrase is how institutions digest people. Verbatim is how they stay people.\" The agency's whole record, he adds, is hers to request as a party's parent (55 Pa. Code § 3130.44(d)) — school correspondence included, which is where the AP decision will be hiding."],
   [C("Start with the agency meeting already scheduled — the move paperwork. Bring a notebook; take the paraphrase home in writing.", "caseworker_meet")]),

 N("caseworker_meet", 3, "Expressed reluctance",
   ["Ms. Kaminski runs the meeting kindly and efficiently: the Halden home is approved and available; the group placement is the fallback; transportation 'will be worked out'; school 'will be addressed by the districts.' Then you ask the question you came for — how Destiny's position will be recorded — and Ms. Kaminski, meaning no harm at all, shows you the draft report's sentence, which becomes this scenario's Exhibit A the moment you read it:",
    "*Youth expresses some reluctance regarding the placement change.* Sixteen years old, three demands, a barrister's calm — compressed into *some reluctance*, the way a concert becomes *some noise* in a police log. Destiny, reading it over your shoulder that evening by phone, is quiet for a moment. Then: \"Write mine down. All of it. I'll sign it.\""],
   [C("Take the sentence home as evidence of the problem — and check your own chapter of the case before you build hers.", "paraphrase")]),

 N("paraphrase", 4, "Some reluctance",
   ["You sit with the sentence longer than it deserves, because it deserves exactly that. *Some reluctance* is not a lie. It is the truth with its spine removed — a paraphrase, the file's native dialect, in which a teenager's three specific, winnable demands became a mood. Moods cannot be granted. Demands can. The distance between the report's sentence and Destiny's Tuesday-night voice is the precise distance this scenario exists to close, and it is closed the way it is always closed: her words, verbatim, signed, filed, receipted.",
    "First, though — your own standing. April's determinations will weigh your progress beside her wishes, and the packet must be honest about both."],
   [C("Inventory your own chapter quickly: housing, work, the plan — documented, all of it.", "shirley_progress")]),

 N("shirley_progress", 5, "Your chapter",
   ["Your record, as the file will tell it: housed since September — a lease, renewed once; employed since October, part-time become full; the parenting program completed in December; visits, including the hard winter ones, attended. The permanency determinations (42 Pa.C.S. § 6351(f)) will find what they find, but they will not find drift. A mother whose chapter reads *stable* can spend her credibility on her daughter's three demands instead of defending her own — a luxury nine months of work bought, and April is when it gets spent.",
    "Mr. Yusuf's phrase for the packet writes itself: *the mother's progress, documented; the daughter's wishes, verbatim; the system's defaults, contested in writing.* Three sections. Hers is the middle one, and it is the one she is about to write herself."],
   [C("Destiny writes her statement at your kitchen table on Saturday. Bring the good pens and no edits.", "statement_draft")]),

 N("statement_draft", 6, "Her draft",
   ["She writes it in one sitting, in a hand that gets steadier as it goes: who she is; where she goes to school and what she is studying; what the AP classes mean (the words *college applications* appear, underlined once); what the evening medication does to her evenings, in her own precise accounting; what she is asking — the school kept, the classes restored, the questions answered, the Halden home welcomed *if* the first three travel with her — and what she is not asking, which is to be treated as a problem of logistics. Two pages. She signs it, dates it, and writes under the signature: *These are my words. Please file them as mine.*",
    "Your instinct — every mother's instinct, and every advocate's temptation — is to wrap it in a covering letter that strengthens it. Mr. Yusuf counsels the harder discipline: file it as it stands, with a one-line cover that adds nothing but its routing: *Statement of Destiny Trejo, filed verbatim at her request.*"],
   [C("File it verbatim — agency, court, GAL, school — with receipts, exactly as written.", "statement_filed", setFlags=["statementVerbatim"], addHidden=["Child's stated wishes — written statement filed verbatim with agency and court"]),
    C("Wrap it in your own letter instead: a mother's summary, citing her points in order — warmer, more persuasive, and in your voice.", "summarized_path", setFlags=["statementSummarized"])]),

 N("statement_filed", 7, "Verbatim, receipted",
   ["The filing takes an afternoon and four stamps. The guardian ad litem, Mr. Ibe, calls that evening with the driest sentence in the case: \"In nine months, this file has contained eleven professional summaries of your daughter. It now contains one document by her. I have watched judges read both kinds. Only one kind gets quoted.\"",
    "Destiny's own review is shorter: \"Good. Now the school.\""],
   [C("The school: ask, in writing, for the best-interest determination on the Halden placement — before March 15.", "school_front"),
    C("The school: ask, in writing, for the determination — before the default does it by envelope.", "school_front")]),

 N("summarized_path", 7, "A mother's summary",
   ["Your covering letter is a good letter — clear, organized, every demand in order — and it makes the filing's central mistake with the best intentions: Destiny's two pages are enclosed, but the document the file will quote is yours. Her voice becomes an attachment to her mother's advocacy. The paraphrase machine has not been defeated; it has been given a better class of paraphrase, with a signature it can cite.",
    "Mr. Ibe, reading it, is gentle and exact: \"The court will now read that *you* say she wants these things. It would have read that *she* says so. In this system, that is not a nuance. It is the whole exhibit.\" The statement can still be re-filed verbatim — paper, unlike pride, allows second drafts."],
   [C("Re-file her pages verbatim, one-line cover, receipts — and let the file hold both versions as the lesson.", "statement_filed", setFlags=["statementVerbatim"]),
    C("Let the letter stand. April is close, and the school fight needs the hours.", "school_front")]),

 N("school_front", 8, "Before March 15",
   ["The written request goes to the agency and both districts' points of contact: a placement change is set for March 15; Destiny is to remain in her school of origin unless a determination based on all factors relating to her best interest decides otherwise (20 U.S.C. § 6311(g)(1)(E)(i)); the parent requests that determination be made, with Destiny's statement and her counselor's input in front of it, and that enrollment be held meanwhile.",
    "It is the same letter this library's parents keep writing, because the default it answers is the same default: a move processed as a change of address, with a school attached as an afterthought. The letter makes the school the subject. Subjects get meetings. Afterthoughts get envelopes."],
   [C("Attach her statement and ask for the counselor, Ms. Petrides, to be heard in it.", "destiny_school_day", setFlags=["bidAsked"]),
    C("Send the request to the agency alone — the districts will take their cue from the case file.", "destiny_school_day")]),

 N("destiny_school_day", 9, "The empty seat",
   ["Destiny's school day, which the determination will be about: AP English, where her essay is pinned — actually pinned — inside the classroom door; the counselor's office, where her junior-year plan lives in a folder with her name spelled right; and in third period, the seat she was removed from in January, when the school's schedule audit dropped her AP enrollment *for administrative reasons* and seated her, for six weeks now, in the standard track, where she is earning A's she describes as 'participation trophies with homework.'",
    "The dropped enrollment is not a decision anyone remembers making. It has the fingerprints of every default in this library: a flag, a code, a consequence. Recovering it is a records problem. She has already told you the solution's shape: *nobody tried* means *nobody requested the file by name*."],
   [C("Request the files — the agency's whole record, and the school records by name from both schools.", "records126")]),

 N("records126", 10, "By name",
   ["The requests go out in writing: the agency's case record under the regulation (55 Pa. Code § 3130.44(d)), with the school correspondence and the January enrollment decision expressly named; and to the schools, through counsel, Destiny's complete record including the transfer file from her fall move and the audit trail of the AP drop.",
    "Lists get answered. Adjectives get acknowledged. The January decision has hidden inside the second category for six weeks; the requests move it, this week, into the first."],
   [C("File them with receipts and read what comes back for the sentence that dropped her.", "transcript_gap", setFlags=["recordsRequested"], cash=-8, addHidden=["Record — agency record and school records requested in writing, enrollment decision named"]),
    C("Ask Ms. Kaminski to pull the school correspondence informally — faster, warmer, off the record.", "transcript_gap")]),

 N("transcript_gap", 12, "The missing midterm",
   ["The production explains the AP drop with bureaucratic clarity: at the January schedule audit, Destiny's file lacked her fall midterm grades from the prior school — the transfer file had been requested in the fall *as a whole*, arrived without them, and was never followed up by name. A missing document became a scheduling flag; the flag became a drop; the drop became six weeks of standard-track A's. The midterm grades themselves, requested now *by name*, arrive from the prior school in three days, with her AP teacher's fall recommendation attached — a document that has existed since November, in a drawer, endorsing exactly the enrollment January cancelled for its absence.",
    "Nobody erred, in the sense of choosing this. Everybody erred, in the sense of a system where a file's completeness is nobody's named job — until a parent makes it hers, in writing, by name."],
   [C("Take the completed file to Ms. Petrides and ask for the AP decision to be re-made on it.", "halden_meet")]),

 N("halden_meet", 13, "Mrs. Halden",
   ["Mrs. Halden's home is warm, organized, and twenty-five minutes from Destiny's school in the wrong district — the geography of this whole spring. She is candid in the way that makes placements work: \"I asked for teenagers because I remember being one. I can drive her to her school in the mornings if the plan says so — I'm up anyway, and it's one trip. What I can't do is be the plan by myself and have nobody write it down. I've seen that movie.\"",
    "She is, in the vocabulary of the file she is entering, a *factor* — and like every factor in this library, she is asking to be considered in writing rather than assumed in passing."],
   [C("Note the offer — mornings, in a plan, on paper — and say the goodbye that this move is built on.", "asare_goodbye", setFlags=["haldenOffer"])]),

 N("asare_goodbye", 13, "The goodbye",
   ["The goodbye at Mrs. Asare's is the cost side of every placement move, paid in a kitchen: the room Destiny has had for nine months, the house rules on the fridge she helped write, a foster mother packing the good snacks into the bag 'for the road, which is twenty minutes, but still.' Stability in this system is always somebody's kitchen, and moves are always, whatever the paperwork says, evictions from one.",
    "Destiny cries exactly once, in the car, briefly, and then returns to her brief: \"School. Classes. The pill questions. In that order — and my words, Mom. Zero before one.\""],
   [C("March 15. The move.", "move_day")]),

 N("move_day", 14, "Monday, March 15",
   ["The move happens the way approved moves do: bags, a caseworker, a new room, a new kitchen's rules explained kindly. Destiny is placed at Mrs. Halden's. Her schooling, as of this morning, exists in the held state your written request created: no enrollment change, pending the determination — or, in the autumns where the letter wasn't written, in the default's hands, which are also a kind of hands.",
    "One demand housed. Three to go, and April gathering at the end of them like a deadline with a gavel."],
   [C("Demand three: her questions for Dr. Iyer. Draft them with her, word for word.", "med_front")]),

 N("med_front", 16, "Her questions",
   ["Destiny's questions for the prescriber, drafted at Halden's kitchen table and edited by their author to within an inch of their lives: *What is the evening medication for, in my case specifically? Why evenings? What happens to my alertness is documented — is it expected, and is it acceptable? What are the alternatives — timing, dose, a different medication — and what would trying one involve? Who decides changes, and how am I told?* Five questions. No adjectives. Mr. Ibe reviews them and says what GALs say when a client has done his job for him: \"Send them exactly like that.\"",
    "The sending is the decision: in writing, through counsel and the GAL, so the answers exist — or aloud at the team meeting, where questions go to be *noted*."],
   [C("Send them in writing — to Dr. Iyer, copies to the agency and the file, her name on them as their author.", "pharmacy_refill", setFlags=["medReview"], addHidden=["Medical — child's written questions to prescriber sent through counsel and guardian ad litem"]),
    C("Raise them at the team meeting — faces, voices, a conversation like a family would have.", "pharmacy_refill")]),

 N("pharmacy_refill", 17, "The information sheet",
   ["A small scene with a long shadow: the refill pickup, where the pharmacy's patient information sheet — folded into the bag, as it has been folded into every bag since October — is read, for the first time, by its patient. Destiny reads it twice at Halden's counter. *May cause drowsiness. Effects on alertness are common in the first weeks and usually diminish.* \"I've had twenty-two first weeks,\" she says. The sheet goes into her folder — not as evidence against anyone, but as the document that converts her *feeling flattened* from a mood into a documented side effect with a literature.",
    "Her folder is becoming the second-most complete file in this case. She intends it to become the first."],
   [C("What the questions produce depends on how they were sent. The file knows.", "med_fork")]),

 N("med_fork", 20, "Sent, or noted",
   ["Late March. The prescriber's office responds — or the team meeting's minutes circulate — and the difference between the two paper trails is, once again, the whole story in miniature."],
   [C("The written questions draw a written answer: three pages, point by point, from Dr. Iyer's office.", "adeyemi_reply", requiresFlags=["medReview"]),
    C("The meeting's minutes record one line — *youth raised medication concerns; team to follow up* — and follow-up has no address.", "med_meeting", requiresNoFlags=["medReview"])]),

 N("adeyemi_reply", 22, "Point by point",
   ["Dr. Iyer's reply is what written questions are for: the indication, specific to Destiny; the evening timing's rationale, and its known cost; and — on the strength of the documented school-day sedation, her own statement, and the information sheet's twenty-two first weeks — an agreed change: the dose adjusted and its timing trialed earlier, with a two-week review and the results to be reported to Destiny, her mother, and counsel in writing. Her covering line goes in the packet whole: *The patient's own report was the clearest account of the problem in the chart.*",
    "A sixteen-year-old asked five questions in writing and a physician answered them in writing. Nothing about that sentence is ordinary in this system, which is why it is an exhibit."],
   [C("Demand two remains: the classes. Ms. Petrides has the completed file now.", "march_counselor")]),

 N("med_meeting", 21, "Follow up",
   ["The follow-up follows the trajectory of follow-ups: it is mentioned at the next meeting as pending, and at the one after as part of a general medication review 'the agency conducts periodically,' whose date is a rumor with a quarter attached to it. Destiny's questions, which existed in final form at a kitchen table in March, exist in the official file as a *concern* — the paraphrase machine's second course. Her evenings remain eaten. Her grades continue to pay for them in the currency of first-period alertness.",
    "Mr. Yusuf's post-mortem is one line: \"A question asked aloud joins the minutes. A question sent in writing joins the evidence. She deserved evidence.\""],
   [C("The classes, at least, are a paper fight already in motion: the completed file is with Ms. Petrides.", "march_counselor")]),

 N("march_counselor", 24, "The counselor's desk",
   ["Ms. Petrides reads the completed file the way counselors read when a student's year is at stake: the midterm grades, the fall AP recommendation, the January audit's paper trail — the flag, the drop, the six weeks. Her verdict is procedural and complete: the drop was an administrative error produced by an incomplete file; the file is now complete; the enrollment decision will be re-made on it, with Destiny's spring grades (straight A's in the standard track, a fact she reads aloud with the flatness it deserves) counted as what they are — evidence the placement was wrong, not that the student was.",
    "A friend texts Destiny during the meeting — the group chat, mid-emoji — and Destiny, watching her year being reassembled by paper, answers with the scenario's most economical sentence: *it's moving. it's all just paper that moves.*"],
   [C("The re-made decision lands within the week.", "destiny_letter_friend")]),

 N("destiny_letter_friend", 25, "The group chat",
   ["The social stakes, itemized by their owner in the chat the adults will never read: the AP classroom is not a class, it is a *cohort* — the same fourteen students, two years, one running joke per subject; the counselor's folder is where her college list lives; the school is the one address that has been constant since before the eviction. *If I switch schools in March of junior year,* she writes, *I don't lose credits. I lose the people who know what the credits mean.*",
    "It is the best statement of the appropriateness factor anyone produces in this case, and it exists only in a chat log. The determination meeting will hear its filed cousin — her statement — which is why statements get filed: so that the best sentences have somewhere official to live."],
   [C("The AP decision arrives.", "ap_decision")]),

 N("ap_decision", 27, "Reinstated",
   ["The re-made decision reinstates Destiny's AP enrollment, with a support plan for the six lost weeks and her midterm grades entered where they belonged since January. It is not a dramatic document. It cites the completed file, the counselor's review, and the fall recommendation — three pieces of paper that existed, in drawers, while a girl sat in the wrong classroom earning evidence she should never have had to produce.",
    "Demand two: granted, on paper, by the paper. One demand left at full size, and it is the first one: the school itself, whose determination meeting is now scheduled — because it was requested, in writing, before the move."],
   [C("Prepare for the determination meeting: her statement, the counselor, the Halden transport offer — in that order.", "bid_meeting126")]),

 N("bid_meeting126", 29, "The determination",
   ["The meeting has the shape these meetings have when they are done on purpose: both districts, the agency, Mr. Ibe, and — by phone, at her own request, in her own words — Destiny, whose filed statement is in the packet because she filed it. The factors are walked: the appropriateness of the current setting (a junior-year cohort, an AP track just restored, a counselor relationship of two years) against proximity (twenty-five minutes, one district line) and the transition cost of a March school change in the year colleges read.",
    "Then the last box, as always: transportation — the place principles go to be priced, and the reason Mrs. Halden's kitchen-table offer matters more than most testimony."],
   [C("Put the transport plan on the table in writing: Halden's mornings as offered, the district's afternoon route, the mileage shared under the written procedures — reimbursement, district, or shared cost.", "transport_plan126", setFlags=["transportArranged"]),
    C("Argue the factors and trust the room to solve the ride, as rooms promise to.", "transport_plan126")]),

 N("transport_plan126", 30, "Three doors",
   ["The plan, in whichever state of completeness your choices left it, is a one-page document with three names in it: a foster mother who offered mornings and meant it, a district with written procedures for exactly this ride, and an agency with a reimbursement door the statute describes (20 U.S.C. § 6312(c)(5)(B)). Determinations do not fail because factors are weak, in this library's experience. They fail because the last box stays empty while everyone admires the factors.",
    "Whatever its state, the determination now goes into the agency's report for April — where it will meet Destiny's wishes, in whichever form the file holds them."],
   [C("Mr. Yusuf marks the longer clock — September 12, 2027 — and what April's orders mean for it.", "fifteen_months")]),

 N("fifteen_months", 31, "The longer clock",
   ["Mr. Yusuf's whiteboard, one line: *September 12, 2027 — fifteen of twenty-two.* At that date the termination-petition question arrives unless an exception is documented — relative care, a documented compelling reason, or services not provided. (42 U.S.C. § 675(5)(E)) \"April is not that fight,\" he says. \"April is where the record that fight will read gets written. A daughter whose school was kept, whose classes were restored, whose questions were answered, whose words are in the file verbatim — with a mother documented stable behind her — is a September that argues itself. A file of paraphrases and defaults argues the other side's. We are not filing for September. We are filing *April*, correctly, which is the only way September ever gets filed.\"",
    "The report arrives three days later. You open it at the school chapter, the way everyone in this library has learned to open everything."],
   [C("Read the report's account of Destiny.", "report126")]),

 N("report126", 33, "The report's Destiny",
   ["The agency's report for the permanency hearing covers the case's whole spring: your progress, credited; the placement with Mrs. Halden, described; the school determination, in its made-or-defaulted state; the AP restoration, noted or not. And in its center, the passage you turn to first: the youth's wishes — in the version this file has earned. Quoted, cited, and attributed to their author — or summarized in the dialect of Exhibit A, *some reluctance*, now doing duty for a girl who filed two pages.",
    "Reports compress. That is their nature and their defense. Which is why the packet exists, and why what the packet contains — verbatim or paraphrase — is about to become the hearing's weather."],
   [C("Check the quotation, if there is one, against the filed original. Word by word.", "report_quote_check")]),

 N("report_quote_check", 34, "Word by word",
   ["The check takes four minutes and is the most quietly satisfying procedure in the case: the statement as filed, laid beside the report's use of it. In the autumn where the statement was filed verbatim, the report quotes it accurately — institutions quote what they cannot paraphrase without embarrassment, and a signed, receipted original is exactly that. In the autumn where only a mother's letter exists, the report quotes the letter, and Destiny's own two pages sit in an appendix nobody opens aloud.",
    "Either way, the check itself goes in the packet: a one-page exhibit titled, in Mr. Yusuf's flattest prose, *Comparison of filed statement and report summary*. Judges read exhibits with titles like that first."],
   [C("Mr. Ibe's position, final form.", "ibe_position")]),

 N("ibe_position", 35, "The guardian ad litem",
   ["Mr. Ibe's position for April is filed in writing, and it is built the way his client's case was built: from her documents. He supports the school arrangement the determination produced, the AP restoration, the medication change if it exists — and he closes with the sentence he has been saving since the evening the statement was filed: \"The court has before it, for once, not a summary of this young person's wishes but the wishes themselves, at pages 1–2 of the packet. The guardian ad litem joins them.\"",
    "A GAL joining a child's verbatim statement is a small thing in the law and a large thing in a hearing room: it means the paraphrase era of this file is over, and everyone in the room knows whose paperwork ended it."],
   [C("Assemble the packet: progress, verbatim, determinations — in the statute's order.", "packet126")]),

 N("packet126", 36, "In order",
   ["The packet's order mirrors the hearing's determinations: your progress, documented (necessity and the mother's chapter); her statement, verbatim (the wishes); the school determination and its transport terms; the completed school file and the AP restoration; the prescriber's answers or the meeting's one-line minute; the GAL's joinder; and the September date, noted once, as context for why paper mattered this spring.",
    "It is, Mr. Yusuf says, closing the folder, the first file in this case that describes the family it is about. Tomorrow the court makes its determinations from it — or from the summaries it was built to replace."],
   [C("Draft the findings language. Then sleep.", "yusuf_findings")]),

 N("yusuf_findings", 37, "Findings, drafted",
   ["The drafted ask is findings-shaped, because findings are what judges sign: that the youth's stated wishes, filed verbatim, be noted on the record; that the school arrangement — of origin with its transport terms, or as determined — be stated in the order where defaults cannot edit it; that the medication review's results and the prescriber's reporting be directed in terms; that the AP restoration be noted so the next file inherits the correction, not the error.",
    "\"Orders are the only summaries in this system that outrank paraphrase,\" Mr. Yusuf says. \"Tomorrow we ask the court to do the summarizing — from her words.\""],
   [C("The night before April 8.", "night_before126")]),

 N("night_before126", 37, "Zero before one",
   ["Destiny, by phone from Halden's kitchen, delivers the final instruction in the case, and it is the one she opened with in March: \"Zero before one, Mom. If they read anything of mine, make sure it's mine.\" You promise — with the packet's second page already dog-eared from the number of times you have checked that it is there, word for word, signature and all.",
    "Tomorrow the court will determine necessity, compliance, progress, and efforts. Somewhere inside those four determinations, a sixteen-year-old will either be quoted or summarized. The difference was decided in March, at a kitchen table, by whether a statement got filed as written. Sleep on that; it is the whole scenario."],
   [C("Go to court.", "hearing126")]),

 N("hearing126", 38, "Thursday, April 8",
   ["The permanency hearing makes its determinations — continuing necessity of placement, compliance, progress toward alleviating the circumstances, and reasonable efforts to finalize the plan. (42 Pa.C.S. § 6351(f)(1), (2), (3), (5.1)) Your chapter is found as documented. Then the court turns to the youth's position, and the room hears it in the form the file holds.",
    "What is ordered — about her school, her classes, her medicine, and the words themselves — is the sum of the spring's paper, read back as findings."],
   [C("The court reads her statement into the record herself — pages 1–2, verbatim — and orders the spring her words described: school kept with its transport terms, classes restored, the medication change and its reporting directed.", "end_quoted", requiresFlags=["statementVerbatim", "medReview"]),
    C("She is heard — quoted, credited, her school kept on the strength of her own pages — but the medicine question was only ever asked aloud, and its answer is a follow-up no order can quote.", "end_heard_late", requiresFlags=["statementVerbatim", "recordsRequested"], requiresNoFlags=["medReview"]),
    C("Her wishes reach the court as summaries — her mother's letter, the report's dialect — accurate in outline, weightless in the room; the classes return on the records, and everything else arrives softened.", "end_summarized", requiresFlags=["recordsRequested"], requiresNoFlags=["statementVerbatim"]),
    C("The file speaks about her all morning in the third person, and she — present, silent, done asking — lets it.", "end_silent")]),

 E("end_quoted", 38, "Ending — Quoted, Not Paraphrased",
   ["The judge reads the statement aloud — not all of it; the two sentences that carry it — and the room hears a sixteen-year-old's prose do what prose does when it has been filed correctly: it becomes the record's own voice. The order follows her text like a shadow follows a person. School of origin: kept, with the transport terms (Mrs. Halden's mornings, the district's afternoon route, the mileage shared under the written procedures) stated in the order itself, where defaults cannot edit them. (20 U.S.C. § 6311(g)(1)(E)(i); § 6312(c)(5)(B)) AP enrollment: noted as restored on the completed record. Medication: the prescriber's agreed change and its written reporting to Destiny, her mother, and counsel are directed in terms. And the findings note, as a finding, that *the youth's statement, filed verbatim at pages 1–2 of the packet, is adopted as the statement of her position* — the sentence that ends the paraphrase era of this file for good.",
    "Name the machinery without inflation. No statute in this scenario promises a teenager her school, her classes, or her evenings back. What the paper did: a best-interest determination was *requested in writing before the default ran*, with her factors and her voice in front of it; school records were requested *by name*, which is the only way files complete themselves; questions to a prescriber were *sent*, so answers exist; the agency record was requested (55 Pa. Code § 3130.44(d)), so the hearing argued from the file instead of about it. And underneath all of it, demand zero — the one she insisted on first: her words, verbatim, signed, receipted. Institutions can paraphrase a wish into a mood. They cannot paraphrase a filed document without the filing showing.",
    "What no strategy controls: September 12, 2027, when the fifteen-month question arrives (42 U.S.C. § 675(5)(E)) — April's order does not answer it; it equips it. Destiny remains in care tonight, at a kind woman's house across a district line, doing homework at a table her statement helped defend. But her file now says what she says, in her words, quoted by a judge — and every future summary of this case will have to start from that page. That is what winning looks like at sixteen: not the system's surrender, but its accurate transcription."]),

 E("end_heard_late", 38, "Ending — Heard, Except About the Medicine (partial)",
   ["She is heard — that part of the spring's work lands completely. The statement is quoted in the findings; the school is kept on the determination her words helped build; the AP restoration is noted; Mrs. Halden's transport terms are ordered. And then the medication chapter is reached, and the file's offering is a meeting minute: *youth raised medication concerns; team to follow up.* The court directs the follow-up — a written response from the prescriber within thirty days — in the tone of a judge assigning homework she can see should have been done in March. Destiny's evenings, meanwhile, remain on the old schedule for another month of first-periods.",
    "The accounting is surgical. Everything that was filed, landed: the verbatim statement (the hearing quoted it), the record requests (the classes exist because the file was completed *by name*), the determination letter (the school exists because it was asked for before the default). The one thing that was asked aloud — five precise questions, drafted to perfection at a kitchen table — joined the minutes instead of the evidence, because minutes are where spoken questions are filed by systems. A question's force is not in its phrasing. It is in its postage.",
    "Partial, with the remedy dated and ordered: the prescriber's written answer is now a court-directed document with a deadline, and when it lands it will land in a file that has learned to keep things. Destiny's spring is two-thirds the one she demanded — school, classes, her own words on the record — with the third arriving late, by order, in May. In this library's accounting that is a strong partial. It is also a precise lesson: she did everything right except put one envelope in the mail, and the envelope was the difference between an answer and a follow-up."]),

 E("end_summarized", 38, "Ending — The Summary of Her (partial)",
   ["The hearing is kind, competent, and conducted entirely in paraphrase. Her mother's letter is read and credited — *the mother reports the youth wishes to remain at her school* — the report's *some reluctance* has been upgraded, by advocacy, to a clearly stated preference, at one remove. The classes are restored for good: the records fight was fought in writing and it shows, the completed file being the one unambiguous victory in the room. The school determination, argued from summaries of her position rather than from her position, lands in the middle the way such arguments do: she will remain at her school through June, the arrangement revisited for the fall — a reprieve, not a ruling, with the transport terms left to be 'worked out' by the parties who worked out the paraphrase.",
    "Read the mechanics plainly, because Destiny already has. Her words existed — two pages, signed, specific. Their evidentiary force depended entirely on their *form*: filed verbatim, they would have been quoted; enclosed under a mother's summary, they were accurately described and permanently discounted, the way all secondhand things are discounted in rooms that weigh paper. The principle that reports may be examined and their makers questioned (42 Pa.C.S. § 6341(d)(2)) has a mirror image this ending exists to teach: a person's own statement, unfiled, is just another report about her — and she has enough of those.",
    "Partial, and unusually fixable: verbatim statements can be filed at any review, and the fall revisit is already calendared — a date by which two pages, filed as written, can convert a reprieve into an order. What the spring cost is the spring: a semester of being summarized, in a case whose subject understood the difference before any of the adults did. She told everyone, in March, exactly what she needed. Zero before one. The file now knows she was right — which is the paraphrase of a lesson she should never have had to teach it."]),

 E("end_silent", 38, "Ending — Third Person",
   ["The hearing speaks about Destiny for forty minutes, in the third person, in her presence. The report's dialect prevails because nothing was ever filed to compete with it: her wishes are *some reluctance*; her school is transferred by the default the unwritten determination left in charge; her AP file remains incomplete in whatever drawer keeps it; her medication is *managed by the team*, a body that has never been defined. By the hearing's second half she has stopped correcting the record under her breath. The system's final victory over a person is not disagreement. It is the moment she stops expecting the record to contain her.",
    "The debrief is the scenario's first scene, read backward. Every instrument in it was free and printed somewhere: a best-interest determination requestable in writing before a move (20 U.S.C. § 6311(g)(1)(E)(i)); transportation procedures with named funding doors (§ 6312(c)(5)(B)); records releasable on request, completable by name (55 Pa. Code § 3130.44(d)); a prescriber reachable by letter; a guardian ad litem whose entire function is amplification. And beneath the instruments, the girl herself — the most precise advocate in the case — whose advocacy failed for the oldest reason in this library: it was spoken, warmly received, and summarized. Systems do not run on the memory of having been told. They run on what was filed.",
    "Not sealed — she is sixteen, reviews recur, statements can be filed at any of them, and a girl who drafts demands like a barrister will not stay silent forever because one spring failed her. But the spring is spent: a school lost by default, evenings lost to an unasked question, and a file that will describe her, for years, in a dialect she never spoke. The doctrine fits in her own four words, which this ending exists to make unforgettable by their absence from the record: *zero before one.*"]),
]
emit(126, s126_meta, s126, S, "a teenager's placement move, school stability, medication questions, and her own stated wishes. No graphic content.")
print("done")
