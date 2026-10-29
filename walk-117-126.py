#!/usr/bin/env python3
"""Graph-walk the winning route of each scenario 117-126: verify every step is
a legal choice, every requiresFlags/requiresNoFlags gate is satisfied by flags
accumulated along the route, cash never goes negative, and the walk terminates
at the named win ending with recordsRequested set."""
import json, sys
from pathlib import Path

G = Path("/home/hatch/workspace/your_files/tacticwatch-game")

ROUTES = {
 117: (["start", "office", "lawyer_call", "plan_visit", "hearing_day", "school_call",
        "poc_letter", "bid_meeting", "records_node", "trial_run", "review_prep",
        "review_day", "end_same_bus"], "Ending — Same Bus, Same School"),
 118: (["start", "lawyer118", "consent_form", "district_reply", "visit_notes",
        "records118", "testing_day2", "khalil_talk", "waiting", "ashby_clock",
        "report_fork", "report_ready", "iep_meeting", "hearing_prep", "outcome118",
        "end_evaluated"], "Ending — Evaluated, and Heard"),
 119: (["start", "how_we_got_here", "yuen_call", "lawyer119", "dentist_call",
        "visit_teeth", "agency_reply", "franca_meeting", "dentist_office",
        "second_opinion", "navya_questions", "consult_day", "records119",
        "transport_plan119", "yuen_support", "packet119", "objection", "gal_call",
        "night_before119", "hearing119", "end_order"], "Ending — The Order Names Who Signs"),
 120: (["start", "how_siobhan", "ellery_call", "lawyer120", "request_sent",
        "respite_story", "pharmacy_bag", "siobhan_words", "visit2", "ellery_log",
        "partial_log", "prescriber_letter", "school_note", "noor_reply", "gal_view",
        "packet120", "agency_report120", "renner_whiteboard", "night_before120",
        "hearing120", "end_writing"], "Ending — Every Change in Writing"),
 121: (["start", "backstory121", "wilma_call", "bid_reveal", "gal121", "lawyer121",
        "objection_sent", "records121", "vadnais_letter", "district_poc", "bid_paper",
        "teacher_call", "wilma_statement", "alina_voice121", "bid_date",
        "transport_math", "pre_bid_prep", "bid_day", "bid_outcome_fork",
        "post_bid_origin", "first_bus_week", "math_team", "route_bill", "wilma_tired",
        "review_prep", "anselmi_findings", "review_day", "end_origin"],
       "Ending — Nineteen Miles, Funded"),
 122: (["start", "petition_read", "lucinda_count", "lawyer122", "truancy_letter",
        "school_office", "oren_voice", "clerk_honesty", "dube_visit", "clinic_visit",
        "neighbor_note", "clinic_records", "records122", "oren_school_day",
        "agency_note", "mother_calendar", "agency_conference", "correction_ask",
        "keller_second", "audit_wait", "foster_shadow", "school_board",
        "keller_evidence", "correction_letter", "expert_call", "clinic_van",
        "hearing_prep122", "night_before122", "adjudication", "disposition_day",
        "end_narrow"], "Ending — Home, on the Narrow Ground"),
 123: (["start", "backstory123", "facility_call", "facility_forms", "lawyer123", "letters_out",
        "records123", "mail_room", "phone_bill", "address_file", "intake_form",
        "candidate_list", "skye_visit", "corvath_meeting", "assignment_news",
        "yasmin_wishes", "evaluation_explainer", "consent_paper", "school_visit",
        "gal123", "thirty_days", "consent_stall_check", "yasmin_school_day",
        "address_fix", "packet123", "viteri_whiteboard", "report123", "review_motion",
        "yasmin_call", "night_before123", "review_day", "end_signature"],
       "Ending — Her Mother's Signature"),
 124: (["start", "excerpt_anatomy", "backstory124", "sayegh_office", "lawyer124",
        "nasser_whiteboard", "records124", "intake_score", "phase_two", "file_arrives",
        "visit_sep12", "visit_center_logs", "boateng_call", "sayegh_letter", "data_pull",
        "employer_letter", "assessment_fight", "redaction_fight", "school_counselor",
        "conference124", "fivemoreminutes", "agency_position", "visit_room_oct",
        "rowan_day", "gal124", "sayegh_prep", "packet124", "mother_statement",
        "rowan_question", "continuance_choice", "night_before124", "hearing_day",
        "end_whole_page"], "Ending — The Whole Page, Read Aloud"),
 125: (["start", "what_happened", "investigator", "nursery_detail", "samira_arrives",
        "lawyer125", "er_resident", "quashie", "page_nine_rumor", "kinship_paper",
        "discharge", "records125", "notice_day", "chart_arrives", "summary_vs_chart",
        "phone_notes", "appeal_choice", "registry_letter", "evidence_packet",
        "investigator_notes", "whitby_contact", "samira_visit", "dependency_track",
        "second_pediatrician", "workup_explainer", "adjudication125", "workup_complete",
        "gal125", "hearing_prep125", "ansel_whiteboard", "agency_offer", "hearing_eve",
        "hearing_day125", "waiting_decision", "reconsideration_prep", "decision_day",
        "end_whole_chart"], "Ending — The Whole Chart"),
 126: (["start", "destiny_reaction", "backstory126", "lawyer126", "caseworker_meet",
        "paraphrase", "shirley_progress", "statement_draft", "statement_filed",
        "school_front", "destiny_school_day", "records126", "transcript_gap",
        "halden_meet", "asare_goodbye", "move_day", "med_front", "pharmacy_refill",
        "med_fork", "adeyemi_reply", "march_counselor", "destiny_letter_friend",
        "ap_decision", "bid_meeting126", "transport_plan126", "fifteen_months",
        "report126", "report_quote_check", "ibe_position", "packet126",
        "yusuf_findings", "night_before126", "hearing126", "end_quoted"],
       "Ending — Quoted, Not Paraphrased"),
}

bad = 0
for n, (path, win_title) in ROUTES.items():
    data = json.loads((G / f"scenario-{n}.json").read_text())
    nodes = {nd["id"]: nd for nd in data["nodes"]}
    cash = data["meta"]["startCash"]
    flags = set()
    ok = True
    for i, nid in enumerate(path):
        if nid not in nodes:
            print(f"S{n}: route node {nid} missing"); ok = False; break
        if i == len(path) - 1:
            break
        nxt = path[i + 1]
        cur = nodes[nid]
        choice = None
        for c in cur.get("choices", []):
            if c["next"] == nxt:
                choice = c; break
        if choice is None:
            print(f"S{n}: no choice {nid} -> {nxt}"); ok = False; break
        for f in choice.get("requiresFlags", []):
            if f not in flags:
                print(f"S{n}: gate requiresFlags {f} unmet at {nid}"); ok = False
        for f in choice.get("requiresNoFlags", []):
            if f in flags:
                print(f"S{n}: gate requiresNoFlags {f} violated at {nid}"); ok = False
        cash += choice.get("cash", 0)
        if cash < 0:
            print(f"S{n}: cash negative ({cash}) at {nid}"); ok = False
        flags.update(choice.get("setFlags", []))
    end = nodes[path[-1]]
    if not end.get("ending"):
        print(f"S{n}: route does not end at an ending"); ok = False
    if end["title"] != win_title:
        print(f"S{n}: win title mismatch: {end['title']!r} != {win_title!r}"); ok = False
    if "recordsRequested" not in flags:
        print(f"S{n}: recordsRequested not set on winning route"); ok = False
    print(f"S{n}: {'OK' if ok else 'FAILED'} — walked {len(path)} nodes, "
          f"cash ${cash} of ${data['meta']['startCash']} left, flags {sorted(flags)}")
    bad += 0 if ok else 1
sys.exit(1 if bad else 0)
