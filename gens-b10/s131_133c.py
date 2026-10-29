# -*- coding: utf-8 -*-
from lib import C, N
from s131_133b import S131, S132, S133

def idx(s, nid):
    return [i for i, n in enumerate(s["nodes"]) if n["id"] == nid][0]
def ins(s, after, node):
    s["nodes"].insert(idx(s, after) + 1, node)
def rewire(s, nid, newnext, cis=None):
    n = s["nodes"][idx(s, nid)]
    for i, ch in enumerate(n["choices"]):
        if cis is None or i in cis:
            ch["next"] = newnext
def P(nxt, label="Carry the page to its file"):
    return [C(label, nxt, cash=-5, flags=["paperTrail"], hidden="Dated documentation added to the record", note="Dated, copied, filed — the chain holds."),
            C("Trust the conversation to carry it", nxt, note="Conversations end. The file keeps what it was given.")]
def ichain(s, anchor, nodes):
    tail = s["nodes"][idx(s, anchor)]["choices"][0]["next"]
    for j, nd in enumerate(nodes):
        nd["choices"] = P(nodes[j + 1]["id"] if j + 1 < len(nodes) else tail)
        ins(s, anchor if j == 0 else nodes[j - 1]["id"], nd)
    rewire(s, anchor, nodes[0]["id"])

# fix b-file chain anchors (prep / carry chains in S133)
rewire(S133, "exhibits133", "prep_a133")
rewire(S133, "decision133", "carry_a133")

def c131(s):
    ichain(s, "start", [
        N("cal_a", 1, "The Envelopes, Opened in Order", ["Each envelope is opened at the kitchen table and read twice — once for what it says, once for what it starts. Three start-dates, three different kinds of clock, and a household that has just learned the difference between them.", "You write the three dates on an index card before you do anything else. The card will outlive the envelopes."], []),
        N("cal_b", 2, "What a Calendar Cannot Do", ["A calendar cannot attend a hearing, file a letter, or love two children in two placements. What it can do — all it can do, and everything — is make sure none of those things is ever attempted late.", "Counsel gets the second index card. The refrigerator gets the first. The folder gets the originals."], []),
    ])
    ichain(s, "appeal_done", [
        N("two_a", 18, "Two Sundays", ["The Sunday visit, in a park between two placements, becomes the family's fixed point: sandwiches, the log, the children's running audit of each other's weeks. Resource families who sign a log together start, slowly, to coordinate like one.", "Coordination between placements is not the agency's job to invent. It can be the family's job to document."], []),
        N("two_b", 20, "The Log's Second Signature", ["Teo's resource mother signs; Cosette's signs beneath her, in a different hand, and the log becomes the first document in either file that contains both children's names on the same page for a family reason.", "Small paper. The marathon is made of it."], []),
    ])
    ichain(s, "packets_back", [
        N("read_a", 50, "Reading Teo's File First", ["Teo's file reads like a case being run by adults: dated services, honest summaries, the crash investigation closed fairly. You index it in an evening and feel, briefly, the system's competence as a personal kindness.", "Then you open Cosette's, and the evening changes."], []),
        N("read_b", 53, "Reading Cosette's File", ["Hers is thinner — second children in widened cases often get the thinner file — and on its third page sits the entry date, November 12, nine days before the entry order you hold in your other hand says November 21.", "You read the page three times. Then you do what the library exists to teach: you reach for a pen, not a phone."], []),
    ])
    ichain(s, "correction_filed", [
        N("evid_a", 63, "The School's Letter", ["Teo's school counselor writes the letter the appeal will want in June: the crash, the nurse's note, the boy's account consistent across three tellings — the small, boring consistency that investigations are supposed to notice.", "It is requested in writing, received in writing, and filed in both tracks. Boring consistency, documented, is a theme of this family's year."], []),
        N("evid_b", 67, "The Photographs, Dated", ["The crash-weekend photographs — the bicycle, the handlebar bruise, the helmet split along its seam — are printed with their dates and filed beside the counselor's letter. Photographs without dates are allegations; with dates, they are exhibits.", "The folder gains a section. June is five months away and already losing."], []),
    ])
    ichain(s, "appeal_hearing131", [
        N("bur_a", 160, "The Transcript's Quiet Pages", ["After the hearing, before the decision, there is the transcript request — made in writing, because the words said in June will be quoted in rooms the family never enters, and quotations prefer originals.", "The agency's witness's answer about the nurse's note is on page forty-one. You will never need to quote it. Everyone will know you can."], []),
        N("bur_b", 172, "Waiting, Documented", ["The decision window — forty-five days under the statute — is waited out the documented way: services continuing, visits logged, the kinship study of Aunt Selene begun at the agency's own suggestion, paper accumulating in all three files at the pace of a family that has stopped fearing it.", "Waiting is a skill. This family has made it a record."], []),
    ])
    ichain(s, "study_winter", [
        N("ord_a", 268, "The Study's References", ["Selene's references are collected the study's way: three letters, three phone calls, each logged by the worker with dates. A retired principal writes that Selene 'kept the district's lost children found for thirty years,' a sentence no home study was ever improved by and none was ever hurt by.", "References, like everything else in this case, are paper or they are weather."], []),
        N("ord_b", 274, "The Home Visit", ["The home visit finds the spare room already plural: two beds, two hooks, a calendar on the wall with both children's school breaks marked in a grandmother-generation hand that predates the case by decades of practice.", "The worker photographs the room for the study. The room, being Selene's, photographs like an argument."], []),
        N("ord_c", 280, "Both Files Note the Study", ["Your written request — that both children's files note the study's progress by date — is granted the way such requests are granted when they are reasonable, written, and early: without discussion, in both files, by Friday.", "Two files, one study, no divergence. The marathon's arithmetic improves every time the paper agrees with itself."], []),
    ])
    ichain(s, "review131", [
        N("feb_a", 360, "The January Paper, Assembled", ["Before February's dates arrive, the packets are assembled in their final form: per child, per exception, each document dated, each date matching the master calendar — which is checked, one last time, against the entry orders themselves.", "Trust, in this family, is a thing that gets verified against originals. The calendar passes."], []),
        N("feb_b", 400, "The Trial's First Weeks", ["The trial return's first weeks are documented the way the whole case has been: visits converting to overnights, overnights to weeks, the log's signatures changing from supervision to simple acknowledgment that the children were, as expected, home.", "February approaches on the calendar like a date that has already been answered — because, in January's orders, it has."], []),
    ])

def c132(s):
    ichain(s, "start", [
        N("pro_a", 1, "Fourteen Months in One Sentence", ["If the case had a sentence it would be this: a man was hurt at work, a child was safe with strangers within the week, and everything since has been the paperwork of proving the first fact no longer governs the second.", "Mr. Baptiste does not deal in sentences. He deals in tabs. But he lets you keep yours, at the front of the folder, where the packet's first page will go."], []),
        N("pro_b", 3, "The Horizon, Named", ["November 4, 2026 is named aloud in the first meeting — the fifteenth month, said early so it can be answered early. Dates that are feared in whispers run cases. Dates on whiteboards get managed.", "The whiteboard gains a second line: September 14, the hearing. Between the two dates lies the whole strategy: be read before you can be filed against."], []),
    ])
    ichain(s, "production", [
        N("inv_a", 6, "Tabs, Numbered", ["The packet's tabs are numbered in the order a judge reads a life: placement, visits, treatment, work, housing, school, kin, and last — by design — the questions the agency has not answered.", "Order is argument. A packet that begins with compliance and ends with an unanswered letter tells its story before a word is spoken."], []),
        N("inv_b", 8, "The Copies", ["Three copies: the court's, counsel's, yours — plus the working set that lives in the car, because hearings have been known to lose paper and this family has stopped being surprised by physics.", "Redundancy is the folder's religion. It has never yet been wrong to practice it."], []),
    ])
    ichain(s, "gap_tasks", [
        N("mir_a", 11, "October, Reconstructed on Paper", ["Before asking Ms. Grey, you reconstruct October from your own artifacts: the pay stubs showing the shift pattern, the text messages setting each visit, the gas receipt from the foster home's side of town. The month existed. It simply lived in the wrong drawers.", "The reconstruction is filed as an appendix, so the calendar, when it comes, corroborates instead of rescues."], []),
        N("mir_b", 13, "The Rotation, Explained by Its Author", ["The rotated-out supervisor, reached by a polite letter, replies with the sentence the gap needed: the notes were kept, the upload was not, the failure was administrative and hers. It is filed without triumph. Systems that admit their gaps in writing are doing, late, the thing the file asked of you on time.", "October now has three documents where it had a rumor. The gap is becoming a paragraph."], []),
    ])
    ichain(s, "grey_calendar", [
        N("cure_a", 17, "The Calendar, Copied at the Kitchen Table", ["Ms. Grey spreads the calendar flat and you copy it together, her handwriting becoming the packet's most human page: arrivals, departures, one rained-out picnic rescheduled in pencil with an exclamation point she apologizes for.", "You do not accept the apology. The exclamation point is the most credible mark in the file."], []),
        N("cure_b", 20, "The Explanation, One Page", ["The one-page explanation is drafted to say exactly three things: the visits happened, the notes were not uploaded, here is the corroboration. No adjectives about the agency, no adjectives about anyone. Explanations that accuse read as defenses; explanations that document read as records.", "It is filed with the calendar and the supervisor's letter. October is closed."], []),
    ])
    ichain(s, "exception_letter", [
        N("wait_a", 26, "The Silence, Calendared", ["Week one of the silence is noted. Week two is noted. The noting is the strategy: an unanswered question with dates on it becomes, at the hearing, a short speech the other side must sit through.", "Mr. Baptiste has given the speech before, in other cases, about other letters. He describes it as 'the sound of a file being read carefully.'"], []),
        N("wait_b", 28, "The Refresh, Requested Meanwhile", ["The record refresh is requested during the silence — timing as housekeeping, so the newest pages arrive with the hearing still a month out and surprises have time to become exhibits or corrections.", "Nothing in the refresh is allowed to be new at the hearing. That is the refresh's whole job."], []),
    ])
    ichain(s, "chorus", [
        N("vis_a", 39, "The Pediatrician's Paragraph", ["Willa's pediatrician contributes the chorus's bass note: growth, attachment behaviors observed across a year of appointments, a final sentence about the father's consistency that the doctor offers unasked and you file without comment.", "Unasked sentences from uninterested professionals are the file's gold standard. The packet does not gild them."], []),
        N("vis_b", 41, "The Neighbor's Line", ["The neighbor who waters the plants and watched the apartment stay ready all year signs her one line: the home was kept, the rent was paid, the child's room waited visibly. It is a small document about a large fact: readiness, maintained at cost, for fourteen months.", "The line is filed in the housing tab, where readiness is the whole argument."], []),
        N("vis_c", 43, "The Chorus, Indexed", ["The voices are indexed on the packet's second page — who, what, when, which tab — so the judge can find the teacher without hunting and the pediatrician without asking. Findability is courtesy, and courtesy, in a courtroom, is a form of credibility.", "The book now has a table of contents. Books with tables of contents get finished."], []),
    ])
    ichain(s, "packet132", [
        N("pk_a", 47, "The First Page, Read Aloud", ["Mr. Baptiste reads the summary page aloud in his office, at courtroom speed, and times it: under three minutes. A year, honestly compressed, that a judge can absorb before the first witness is sworn.", "You hear your own year as a stranger would. It holds. That is the test, and it passes."], []),
        N("pk_b", 49, "The Filing Receipt", ["The packet is filed and the receipt is kept with the same care as the packet — because a book's existence, at a hearing, is sometimes the first thing disputed, and receipts end disputes about existence.", "Two weeks of margin sit between the filing and the reading. Margin is the strategy's oldest friend."], []),
    ])
    ichain(s, "filed_early", [
        N("ag_a", 53, "Reading Their Answer Closely", ["The agency's response is read the way responses deserve: for what it concedes, what it avoids, and what it dates. It concedes progress, avoids the exception question, and dates itself three days after your packet — the sequence itself a small confession about whose paper is driving.", "Mr. Baptiste annotates the margins in pencil. Penciled margins have settled more cases than speeches."], []),
        N("ag_b", 55, "No Position, Positioned", ["'No position at this time' is workshopped in the office until it confesses: the agency that intended to oppose return writes opposition. The sentence on file is the sound of a case being read and quietly re-decided.", "Nothing is celebrated. Positions can change until the judge speaks. Paper just makes changing them expensive."], []),
        N("ag_c", 57, "The Last Week's Quiet Jobs", ["The final week is quiet jobs: the suit pressed, the route timed, the folder's copies counted, Willa's playroom logistics confirmed with Ms. Grey — the logistics of hope, handled like logistics.", "You have done everything the year asked. The calendar says so, in fourteen months of handwriting."], []),
    ])
    ichain(s, "testimony_prep", [
        N("ni_a", 60, "Questions at Kitchen-Table Speed", ["The likely questions are practiced at the kitchen table, at the speed of honesty: the accident, the weekend, the services, October, the plan for mornings. Each answer is shorter than the question's fear of it.", "Preparation's product is not eloquence. It is the absence of surprise, which courtrooms experience as credibility."], []),
        N("ni_b", 61, "The Drawings, Decided", ["Whether Willa's drawings come to court is decided the adult way: they stay with her, in her folder, because children are not exhibits and this family has never once used her as paper.", "Your folder closes with a sound like a book's. Hers closes with a sound like a child's. Both are ready."], []),
    ])

def c133(s):
    ichain(s, "table133", [
        N("tb_a", 5, "Each Chair Gets a Date", ["The study gets its milestones, the services their sessions, the appeal its April wall — and beneath them all, the line the table exists for: what happens if two chairs need you on the same day. The answer is written down too, because it will happen.", "It happens in week three. The written answer handles it. The table begins to earn its wall space."], []),
        N("tb_b", 6, "Sabine Sees the Table", ["Sabine studies the page the way she studies recipes she intends to improve, and adds one line in her own hand: Matteo's school concert, in May, attendance non-negotiable, all chairs.", "The table accepts the amendment. Cases that forget concerts lose more than concerts."], []),
    ])
    ichain(s, "sprint_done", [
        N("st_a", 16, "The Study's First Visit", ["The kinship worker's first visit is a study in competence meeting competence: Sabine's house, Matteo's room, the forms produced from a folder labeled in marker with the boy's name and a star.", "The worker's notes, later visible in the record, use the word 'prepared' — the study's first exhibit, written by its examiner."], []),
        N("st_b", 18, "The Brother Question, Answered in Ink", ["Your brother signs his clearance form at Sabine's table and accepts the couch rule in the same sitting — family governance conducted at the speed of love and documented at the speed of paper.", "The study's only snag is retired in week three, in writing, with a signature. The table notes it and moves on."], []),
    ])
    ichain(s, "receipt_filed", [
        N("ev_a", 47, "The Timeline, One Page", ["The timeline of the pharmacy night fits one page because timestamps are mercifully short: the call, the departure, the receipt, the police entry for the neighbor's unit, the return. Five lines, five times, no adjectives.", "Adjectives are where timelines go to be argued with. This one declines."], []),
        N("ev_b", 51, "Both Tracks, Same Page", ["The timeline is filed in the dependency record and the appeal packet on the same day, with the same cover note — the corridor walked deliberately, so neither building can later claim it summarized the other.", "Identical paper in two buildings is this family's answer to the summary problem: refuse to be summarized."], []),
    ])
    ichain(s, "study_done133", [
        N("spr_a", 76, "The Course's Middle Weeks", ["The parenting course's middle weeks are unglamorous and documented: attendance perfect, the workbook's exercises done in the handwriting of a person taking the thing seriously because the file will.", "The instructor's mid-course note says 'engaged.' It is filed without embellishment. Mid-course notes are the review's appetizer."], []),
        N("spr_b", 82, "The Shift Problem, Engineered", ["Your employer's letter — the office-cleaning schedule adjusted so your late runs end by nine — joins the roster in the plan file, converting the plan's weakest paragraph into its most documented one.", "Problems that are engineered on paper stay solved longer than problems that are promised away in meetings."], []),
        N("spr_c", 87, "The Test Nobody Scheduled", ["The April night the roster executes is written up by the caseworker in the ordinary course — she does not know she is writing the review's favorite paragraph, which is exactly why it will be.", "Documents written without an audience are the only ones hearings fully trust. This family keeps producing them on schedule."], []),
    ])
    ichain(s, "appeal_hearing133", [
        N("hr_a", 163, "The Wait, Used", ["The weeks between hearing and decision are used the table's way: the trial-return proposal drafted, Sabine's respite language drafted, the endgame drawn in pencil beneath the table's ink — prepared endings being this family's final discipline.", "When the decision comes, the case will not need to improvise its response to good news."], []),
        N("hr_b", 169, "Sabine's Folder, Closed and Open", ["Sabine closes her study folder and immediately opens a respite folder — same marker, same star — because the family's paper, like the family, plans past the verdict.", "The gesture is small and total: the kinship door, once opened by documents, stays open by documents."], []),
    ])
    # endgame fall chain on the gated choice only
    fall = [
        N("fall_a133", 246, "The Trial's First Fortnight", ["Matteo's trial begins with the choreography already rehearsed at Sabine's table: school nights at home, the spare room kept as his by right rather than by order, the phone tree retired to a refrigerator magnet.", "The caseworker's first trial note is two lines long. Two-line notes are the sound of a plan working."], []),
        N("fall_b133", 254, "The Ordinary Weeks, Logged", ["The fall runs ordinary: homework, the concert's sequel, one roster revival for a late shift that executes exactly as its signatures promised — documented by habit now, the habit being the year's deepest change.", "Ordinary weeks are the trial's evidence. This family logs them like verdicts."], []),
        N("fall_c133", 261, "The Final Order, Drafted", ["The final order is drafted before the review that will adopt it: closure, the respite clause, the study's standing noted — the family's whole table converted into the court's stationery, ready for a signature.", "Drafted orders get signed. Undrafted outcomes get continued."], []),
    ]
    for j, nd in enumerate(fall):
        nd["choices"] = P(fall[j + 1]["id"] if j + 1 < len(fall) else "end_three_chairs")
        ins(s, "endgame133" if j == 0 else fall[j - 1]["id"], nd)
    rewire(s, "endgame133", "fall_a133", cis=(0,))

c131(S131); c132(S132); c133(S133)
