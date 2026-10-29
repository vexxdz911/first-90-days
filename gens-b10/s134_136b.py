# -*- coding: utf-8 -*-
from lib import C, N
from s134_136 import S134, S135, S136

def insert_chain(scen, after_id, chain):
    nodes = scen["nodes"]
    idx = next(i for i, n in enumerate(nodes) if n["id"] == after_id)
    node = nodes[idx]
    targets = {c["next"] for c in node.get("choices", [])}
    assert len(targets) == 1, (after_id, targets)
    orig = targets.pop()
    for c in node["choices"]: c["next"] = chain[0]["id"]
    for c in chain[-1].get("choices", []): c["next"] = orig
    nodes[idx + 1:idx + 1] = chain

def node(scen, nid):
    return next(n for n in scen["nodes"] if n["id"] == nid)

def P(nxt, label="Carry the page to its file"):
    return [C(label, nxt, cash=-5, flags=["paperTrail"], hidden="Dated documentation added to the record", note="Dated, copied, filed — the chain holds."),
            C("Trust the conversation to carry it", nxt, note="Conversations end. The file keeps what it was given.")]

def expand134(s):
    insert_chain(s, "two_files", [
        N("tw_a", 4, "Two Envelopes, Two Stamps", ["The two proceedings announce themselves in different paper stocks, different return addresses, different typefaces — the bureaucracy's way of saying what Ms. Adeyemi said in words: these are not the same case wearing two coats.", "You buy two folders. The colors will matter at 2 a.m. more than any filing system: blue for the Bureau, manila for the court, and never the twain at the wrong hearing."], P("tw_b")),
        N("tw_b", 5, "The Calendar Gets Two Colors", ["The board's two columns get their colors, and the dates sort themselves by peril: May 3 alone in its season on the blue side; the case's reviews spread across the manila year like ordinary weather.", "Peril, color-coded, is just planning. Uncolored, it was panic. The board is already earning its wall."], P("appeal_week")),
    ])
    insert_chain(s, "records134", [
        N("rc_a", 24, "Reading the Mirror's Margins", ["The record's margins are where its honesty lives: the investigator's initials, the supervisor's one-line concurrence, the cross-reference to the facilities log tucked into a footnote's posture — cited, but minimized, the way files minimize what they cannot omit.", "Minimized citations are still citations. The footnote is now the most important line in the mirror, and it knows it."], P("rc_b")),
        N("rc_b", 29, "Counsel Asks for the Log", ["The request for the logbook goes out on counsel's letterhead, addressed to the district, citing the investigation's own citation — a request that is, formally, unanswerable with no: the agency relied on the document; the appellant may read it.", "Five business days later, the facilities office calls. Clerks recognize clerks' paper being honored, and they cooperate with historians."], P("logbook")),
    ])
    insert_chain(s, "logbook", [
        N("lg_a", 38, "The Super's Handwriting", ["Mr. Halloran's handwriting is the handwriting of a man who has logged thirty years of furnaces: block capitals for events, cursive for people, times to the minute because boilers taught him minutes matter.", "Your two calls sit in the cursive, timed in the capitals' discipline. The page is a small masterpiece of a mind that believed records were for later. Later has arrived."], P("lg_b")),
        N("lg_b", 43, "Copies, Plural", ["The page is copied three ways at the district office copier: the appeal's, the case's, and the one for the super's own file, at his request — he has decided his logbook is a document of record and intends to keep treating it that way.", "Redundancy, practiced by everyone the paper touches, is how single pages survive to win hearings."], P("intake_note")),
    ])
    insert_chain(s, "spring_review134", [
        N("sr_a", 80, "The Addendum's Arrival", ["The correction addendum arrives without a cover letter, in an envelope whose plainness is its own confession — agencies announce victories; they slip corrections under the door. It is dated, signed by a supervisor, and filed in the investigation record as an amendment, which means the file now formally disagrees with itself.", "Files that disagree with themselves are the appellant's best friends. This one gets a tab of its own."], P("sr_b")),
        N("sr_b", 85, "Reading It Twice", ["You read the addendum twice at the kitchen table: once for what it concedes (the logbook postdates the summary; the summary should be read with it) and once for what it does not (no apology, no amended finding — the Bureau's process still required, its burden still unmet).", "Concessions without conclusions are the normal currency of spring. Conclusions are minted at hearings, from concessions."], P("exhibit_one")),
    ])
    insert_chain(s, "exhibit_one", [
        N("ex_a", 100, "The Chronology, Co-Signed", ["The one-page chronology — alarm, arrival, the two calls, the sister, the departure — is drafted from the logbook and the intake note alone, no memory admitted, so that every line can be footnoted to a document the agency or the district already holds.", "Chronologies built only from their paper are nearly unarguable. The super signs his footnote's worth with a clear conscience and a borrowed pen."], P("ex_b")),
        N("ex_b", 115, "The Packet's Weight", ["The assembled packet is thinner than the year's fear suggested: eleven pages, three exhibits, one chronology. Thin packets win paper cases because officers read all of them; thick ones get sampled.", "It is filed with the Bureau, copied to the case record, and logged on the board in both colors — the corridor's traffic, made visible."], P("bureau_prep")),
    ])
    insert_chain(s, "bureau_prep", [
        N("bp_a", 136, "The Officer's Questions, Rehearsed", ["The likely questions are rehearsed against the exhibits: When did you arrive? (The log.) Who had the child? (The calls, the sister, the intake note's first form.) Why does the summary differ? (The addendum's question to answer, not yours.)", "Each answer is a page number before it is a sentence. Witnesses who answer in page numbers are believed in proportion."], P("bp_b")),
        N("bp_b", 146, "June, in the Case's Column", ["The manila column keeps its own June: services completing, Fern's school year closing, the roster's summer version signed — the case advancing on its merits while the appeal ripens beside it, neither starved by the other's season.", "Two proceedings, fed in parallel, all spring. This is what the board was for."], P("bureau134")),
    ])
    insert_chain(s, "decision134", [
        N("dc_a", 190, "The Letter, Opened Standing Up", ["The decision is opened standing at the mailbox, read twice before the walk back — amended to unfounded, the reasoning tracking the exhibits in order, the addendum quoted in the agency's own words against its own summary.", "Eleven pages, three exhibits, one standard. The boiler room's Saturday is now, officially, what the logbook always said it was."], P("corridor_last")),
    ])
    insert_chain(s, "fall_a", [
        N("fa_a", 198, "The Safety Shelf", ["The home assessment's final visit notes the labeled Saturday shelf — the emergency supplies, the roster's laminated copy, the sister's number in three places — and the assessor's laugh becomes, in the fall packet, a documented professional judgment that this home has metabolized its worst day into a system.", "Systems are what assessments exist to find. This one was built out of a Saturday."], P("fa_b")),
        N("fa_b", 201, "Completions, Landing Monthly", ["The certificates arrive across September like the year's report cards: course, series, assessment — each filed the week it lands, each indexed in the fall packet's growing table, so October's assembly is an act of collation rather than archaeology.", "Archaeology is for cases that filed in the fall what they earned in the spring. This family filed monthly, and October is clerical."], P("fall_prep134")),
    ])
    # repair: the courtesy choice at the fall review looped backward to decision134;
    # it now lands on a dedicated late-closure ending at the same offset as the win.
    node(s, "end_dual")  # ensure exists
    s["nodes"].append(N("end_late134", 235, "Closed, Eventually", [
        "The case closes a season later than the paper earned — at a winter review nobody needed, on an order the court drafted in its own caution's image, with the respite and aftercare thinner than the family's actual arrangements.",
        "Nothing was lost that paper protects; the registry was already clear, the goal never moved. What courtesy cost was a season and some ink — the system's standard tax on endings nobody proposes in writing."],
        ending=True, debrief=[
            "THE TAX ON UNPROPOSED ENDINGS — Courts close cases on the orders in front of them. A family that arrives with a complete record and no proposed order gets the court's default craftsmanship: careful, slow, and thin where the family's paper was thick. The route's discipline — propose the ending, in writing, with the packet — exists because endings, like everything else in this library, are documents before they are events.",
            "WHAT NO STRATEGY CONTROLS — A judge's drafting pace. Everything else in this branch went right, which is its lesson: complete paper can still be taxed a season by an unwritten last page."]))
    for c in node(s, "fall_review134")["choices"]:
        if c["next"] == "decision134": c["next"] = "end_late134"

def expand135(s):
    insert_chain(s, "compendium_start", [
        N("cs_a", 10, "Three Sections, Two Clocks", ["The binder's architecture mirrors the case's: three sections (one per child), a shared front pocket for the clocks, and a rule written inside the cover — every page dated, every date cross-checked against the entry orders before it is believed.", "The rule sounds like fussiness in September. By the second September it is the difference between a record and a rumor."], P("cs_b")),
        N("cs_b", 14, "The First Pages", ["The first pages are the entry orders themselves, the plan, and Ms. Ferreira's wheel — the case's founding documents, kept at the front so the year's later paper always knows what it answers to.", "Binders, like cases, are judged by whether their first pages survive their last."], P("fall_services")),
    ])
    insert_chain(s, "fall_services", [
        N("fs_a", 27, "October's Enrollment Letters", ["The enrollment letters arrive across October like the season's first report cards: program accepted, therapy waitlisted, housing intake scheduled — each copied into the binder the week it lands, waits and all, because October's paper is November's alibi and next October's exhibit.", "The compendium's appetite is established early: everything, dated, monthly. The family settles into the rhythm the year will require."], P("fs_b")),
        N("fs_b", 34, "The Cousin's September", ["A page of the binder is set aside for the kinship chapter that didn't hold: your cousin's care of Nico in September, her surgery, the honest end of an arrangement nobody failed at — documented now, kindly, because next fall a hearing may ask whether kinship was ever tried, and the answer deserves better than a summary.", "Tried, documented, ended by medicine: the page says it in dates. That is the whole entry, and it is enough."], P("fall_visits")),
    ])
    insert_chain(s, "fall_visits", [
        N("fv_a", 50, "November's Reconciliation", ["November's reconciliation finds its first discrepancy: a visit the center logged as supervised that ran, in fact, as a community visit — a small error with a long shadow if left to ripen into next fall's 'inconsistency.' It is corrected by a dated page, filed without accusation, in both the binder and the record.", "Corrections filed kindly and early are maintenance. The same correction at a hearing is impeachment."], P("fv_b")),
        N("fv_b", 62, "December at Two Placements", ["The holidays run on both placements' calendars and the binder's one: gifts logged, school breaks charted, the children's December recorded as a season rather than a wound — paper doing its quietest work, keeping a family's worst year narratable.", "Narratable years can be argued from. The binder is an argument under construction, disguised as a scrapbook."], P("winter_gap")),
    ])
    insert_chain(s, "winter_gap", [
        N("wg_a", 82, "The Vacancy, Confirmed", ["Before the gap letter goes, the vacancy behind it is confirmed the paper way: the provider's own letter, requested in writing, stating the referral's queue position and the staffing gap that held it — the system's explanation of its own eleven weeks, in its own hand.", "Letters like this are never volunteered and always producible. Asking, in writing, is the whole technology."], P("gap_letter135")),
    ])
    insert_chain(s, "gap_letter135", [
        N("gl_a", 100, "The Mirror's Gaps", ["The mid-winter record, read against the binder, shows the expected silences: the therapy wait absent entirely (the file begins the service at its start, as if queues were weather), one visit's supervision mislabeled in the other direction.", "Each silence gets its page. The binder's margins fill with the small print of a family insisting on being accurately described."], P("gl_b")),
        N("gl_b", 110, "Corrections, Filed as Pages", ["The corrections go in as pages with exhibits — the provider's queue letter, the center's sign-in sheet — not as complaints about the file but as additions to it, which is why they are accepted without a fight and read forever after as part of the record.", "Tone is a filing strategy. Additions are read; accusations are answered. The binder prefers to be read."], P("winter_review135")),
    ])
    insert_chain(s, "winter_review135", [
        N("wr_a", 135, "February's Applications", ["February's housing work is a sheaf of applications, each with its date and its waitlist's arithmetic kept in the binder's housing tab — a paper trail that proves the wound's owner every time it is opened.", "Applications without dates are hopes. These have dates, queue numbers, and a case manager who answers email in writing."], P("wr_b")),
        N("wr_b", 150, "The Children's Winter Pages", ["Winter adds its chorus pages: Esteban's mid-year report, Paloma's attendance star, Nico's foster mother's February letter about a boy who has started calling her house 'the snow house' with a permanence that worries and reassures everyone in equal measure.", "The pages are filed in season. Next fall's hearing will meet children documented as they grew, not as they were remembered."], P("spring_housing")),
    ])
    insert_chain(s, "housing_letter135", [
        N("hl_a", 208, "The Landlord's Conditions", ["The landlord's conditional commitment gets its conditions itemized in writing — voucher round, inspection, the September lease window — because conditions that live in a phone call retire when memories do.", "Itemized, the commitment becomes a checklist the fall can execute. Unitemized, it was a mood."], P("hl_b")),
        N("hl_b", 220, "The Answer, Assembled", ["The three letters are assembled into the binder's housing tab as a single answered question: projection, confirmation, commitment — the wound and its treatment plan, dated within the same spring.", "Assembled answers are what reviews adopt. Scattered ones are what reviews ask about."], P("spring_review135")),
    ])
    insert_chain(s, "spring_review135", [
        N("sr_a135", 242, "June's First Assembly", ["June opens the EXCEPTIONS section with its inventory: what each child has (relative care assessed, gap lettered, trajectory documented), what each still needs (the plan language, requested; the packets, to be built), and the summer's work schedule — counsel's wheel entering its third season.", "Inventories precede assemblies. The section will be built from a list, not from a mood."], P("sr_b135")),
        N("sr_b135", 252, "The Trial, Proposed on Paper", ["The trial return is proposed as a document in June — stages, school logistics, support structure — so the agency's agreement, when it comes in July, comes as a response to the family's paper rather than as the system's invention.", "Proposals shape adoptions. The August trial will run on the June draft's rails, and everyone will call it the plan."], P("summer_a")),
    ])
    insert_chain(s, "summer_a", [
        N("sa_a", 270, "Each Child, Their Own Page", ["The exception work proceeds child by child through July: Esteban's page (his clock, his school letter, his gap arithmetic), Paloma's (hers, with the art teacher's spring note promoted to evidence of trajectory), the family's shared exhibits indexed once and cited thrice.", "Shared paper, separate dates: the binder's grammar, learned over a year, now fluent."], P("sa_b")),
        N("sa_b", 280, "The Compendium, Closed for Building", ["By August the compendium is complete enough to change tense: no longer a diary being kept but a book being cited — its building finished, its use begun. Ms. Ferreira's wheel reaches the summer's end with every section populated.", "The flag the year has been earning is set here, at the assembly's completion: the compendium is built."], [C("Rule the compendium complete and index it for the fall", "summer_b", flags=["compendiumBuilt"], hidden="Year compendium completed and indexed", note="Built. From here to the hearing, the binder is cited, not kept."),
         C("Keep adding pages without ruling it complete", "summer_b", note="Unindexed completeness is a rumor. Rule it built and cite it.")]),
    ])
    # Nico's own packet beat between the trial and the second fall
    insert_chain(s, "summer_b", [
        N("nico_packet", 340, "Nico's Packet", ["Nico's clock runs four weeks behind his siblings', and his packet is built to his own dates in September: his kinship chapter (the cousin's page, promoted), his foster mother's letters, his gap arithmetic — the youngest child's file assembled with the same rigor as the elders', because December 29 will ask him separately.", "Youngest children in multi-child cases get summarized. This one gets a packet. The difference is the scenario."], P("fall135")),
    ])

def expand136(s):
    # date repairs against the scenario's own prose: the notice is June 30 (offset 28),
    # the appeal filed on day 11 of the window = July 11 (offset 39); the study completes
    # in the new year (offset 230); the registry ending sits just past the Sept 28 window.
    node(s, "appeal136")["dayOffset"] = 39
    node(s, "kinship136")["dayOffset"] = 45
    node(s, "study136")["dayOffset"] = 60
    node(s, "vendor_letter")["dayOffset"] = 78
    node(s, "pace136")["dayOffset"] = 98
    node(s, "exhibits136")["dayOffset"] = 118
    node(s, "study_travels")["dayOffset"] = 230
    node(s, "end_registry136")["dayOffset"] = 118
    insert_chain(s, "order136", [
        N("or_a", 18, "The Twins' Second Envelope", ["The twins' entry order arrives in the mail of a week already full of envelopes — June 23's date entering the board as the second permanency clock, three weeks behind Silas's, a stagger that will matter in the marathon's final month and is therefore recorded now, in June, while recording is cheap.", "Staggers recorded early are strategies. Staggers discovered late are ambushes."], P("or_b")),
        N("or_b", 28, "The Notice", ["Monday, June 30: the indicated notice, read twice at the kitchen table of the house you have just come home to — the report from the hospital night, the finding written from midnight forward, the 90 days running to Sunday, September 28, 2025.", "The board takes its third column. Ms. Castellanos, by phone, is brief: 'Eleven days. We file it in eleven days, and then we never think about the window again.'"], P("appeal136")),
    ])
    insert_chain(s, "kinship136", [
        N("kn_a", 52, "Odile's First Checklist", ["Odile's checklist, drawn with her county's kinship worker, lists what a spare room must become on paper: clearances for her household, the home visit, the training, the references — each with the other county's counterpart noted beside it, because every item in this study exists twice or not at all.", "She works the list the way she has run a household for forty years: top to bottom, in pencil, with dates."], P("study136")),
    ])
    insert_chain(s, "vendor_letter", [
        N("vd_a", 84, "Everything Else, Enrolled", ["While the vendor's queue holds the plan's centerpiece, everything else enrolls and runs: the health follow-ups from your surgery, the family sessions the agency runs in-house, the visitation cadence at two placements — a Plan B executed so completely that the file's only blank wears the vendor's name.", "Completeness around a documented gap is the gap's best frame. The frame is built weekly, on time."], P("vd_b")),
        N("vd_b", 90, "The Queue, Reconfirmed", ["The waitlist letter is reconfirmed in September — position, movement, the vendor's own projection — because a July letter describing a queue is evidence; a July letter plus a September update is a record of the queue itself.", "Queues keep moving or keep stalling; either way, dated paper knows which."], P("pace136")),
    ])
    insert_chain(s, "pace136", [
        N("pc_a", 104, "Three Mirrors, Reconciled", ["The three records — Silas's, the twins', the study file's releasable pages — are reconciled against the board in October: dates agreed, two discrepancies found and filed as corrections, the pace exhibit's table verified line by line against primary pages.", "Reconciliation is the marathon's least visible discipline and its most decisive: next year's hearings will meet one chronology, in three bindings, without a seam to pull."], P("pc_b")),
        N("pc_b", 111, "The Pace Table, Drafted", ["The pace table is drafted the way indictments and love letters are: plainly. Plan date, service date, days between, per child, per service — the system's year in arithmetic, requiring no adjectives because arithmetic doesn't accept them.", "It will be filed without commentary. Tables this plain comment on themselves."], P("exhibits136")),
    ])
    insert_chain(s, "exhibits136", [
        N("wn_a", 150, "Winter: The Study's Middle", ["The kinship study's middle months are a correspondence between two counties conducted at the speed of inter-office mail: Odile's home visit in November, her county's report in December, the children's county's questions in January — each leg dated in both files, because a study traveling between counties accrues exactly the delays its paper trail must later explain.", "Delays with dates are process. Delays without them are suspicions. The study's folder prefers process."], P("wn_b")),
        N("wn_b", 185, "Winter: Visits at Odile's", ["Winter visits begin rotating through Odile's house — the placement rehearsing itself before it exists, the twins learning the spare room's geography, Silas annexing the garage workbench — documented by both counties' visit structures, reconciled monthly like everything else in this case.", "Rehearsal visits are the kinship system's best idea. Documented, they become the placement's first chapter instead of its rumor."], P("wn_c")),
        N("wn_c", 210, "Winter: The Plan's Other Half", ["Your own services' winter half completes in the in-house tracks: sessions attended, the health plan stabilized, the home-readiness assessment passed with the assessor noting the board of dates still on your kitchen wall, photographed into the report with something like respect.", "The wall has become a character in the file. Characters with dates are believed."], P("study_travels")),
    ])
    insert_chain(s, "spring136", [
        N("sp_a", 315, "The Cohort's Middle Weeks", ["The vendor program's middle weeks run through April and May with the attendance the waitlist letter promised you'd bring: perfect, documented, unremarkable in the way of all decisive things — the plan's last service converting from the file's biggest blank into its most ordinary page.", "Ordinariness, at month eleven, is the sound of a case closing in on its answer."], P("sp_b")),
        N("sp_b", 332, "Odile's Second Folder", ["Odile opens the second folder — the support folder, for the placement's conversion to standing kinship support after the trial — with the same pencil discipline as the first, in both counties' formats, because a conversion documented in advance is a hearing's shortest agenda item.", "The family's paper gene, dominant as charged, expresses itself one final time: the ending, pre-filed."], P("packets136")),
    ])
    insert_chain(s, "plan_entries136", [
        N("pe_a", 395, "The Amendments, Read Back", ["The amended plans are read back to you at the summer's first review — relative care, compelling reason, the gaps' owners' dates, all in the plans' own sentences now — and you initial each page the way litigants initial settlements: slowly, as someone who knows what sentences cost.", "Initialed plans are the exceptions' legal address. The statute reads plans. These now say it."], P("pe_b")),
        N("pe_b", 408, "Two Counties, Notified", ["The plan entries are certified into Odile's county file as well — the support clause's home county — so the conversion she has pre-filed meets plans that already describe it, in both buildings, before the hearing asks.", "Paper that agrees with itself across county lines is the marathon's final luxury, purchased with a year of couriers."], P("summer136")),
    ])
    _sm = [
        N("sm_a", 430, "August: Enrollment and Toothbrushes", ["August is logistics elevated to evidence: school enrollment in your district completed early, Odile's address filed as the documented backup, toothbrushes resident in two houses by the children's own arrangement — the trial's paperwork indistinguishable, at last, from a family's ordinary administration.", "Ordinary administration is the destination. The file's highest compliment, available only in August, is boredom."], P("sm_b")),
        N("sm_b", 440, "The Binder's Last Pages", ["The hearing binder's last pages are the summer's: trial logs, enrollment confirmations, the twins' preschool letters, Silas's workbench photograph (filed by Odile, annotated in pencil: 'his corner') — the marathon's evidence ending, as it began, with the children's lives rather than the system's forms.", "The binder closes. What opens in September is a courtroom, and it will read."], P("hearing_prep136")),
    ]
    _sn = node(s, "summer136")
    for _c in _sn["choices"]:
        if _c["next"] == "hearing_prep136": _c["next"] = "sm_a"
    _idx = next(i for i, n in enumerate(s["nodes"]) if n["id"] == "summer136")
    s["nodes"][_idx + 1:_idx + 1] = _sm

expand134(S134); expand135(S135); expand136(S136)
