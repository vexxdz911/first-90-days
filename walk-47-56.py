#!/usr/bin/env python3
"""Graph-walk the winning route of each scenario 47-56: verify every step is a
legal choice, every requiresFlags gate is satisfied by flags accumulated along
the route, print the walked path and the final cash position."""
import json
from pathlib import Path

G = Path("/home/hatch/workspace/your_files/tacticwatch-game")

ROUTES = {
 47: (["start", "the_checklist", "named_in_writing", "the_decision", "the_call", "the_bag",
       "morning", "what_judge_needs", "sister_calls", "the_plan", "records_ask",
       "hearing_day", "hearing_outcome", "end_kin"], "Ending — Home by Thursday"),
 48: (["start", "tell_in_writing", "phone_interview", "the_list", "fix_weekend", "clearances",
       "program_letter", "checklist", "home_visit", "hugo_visit", "before_review", "voss_call",
       "walter_letter", "the_review", "the_drive", "outcome", "end_move"],
      "Ending — The Spare Room, Occupied"),
 49: (["start", "the_date", "aunt_call", "letter_full", "hearing49", "the_study", "odettes_house",
       "micah_tooth", "certificate", "sibling_visits", "kira_call", "weekend_visit", "tomas_check",
       "tomas_job", "the_list2", "foster_moms", "deshawn_plan", "records49", "review_prep49",
       "continuance_scare", "the_review49", "night_before49", "outcome49", "end_oneroof"],
      "Ending — One Roof"),
 50: (["start", "exact_words", "school_call", "call_lawyer50", "file_both", "first_letter_back",
       "march30", "ruben_weekend", "kessler_speaks", "wexler_call", "anita_call", "anita_house",
       "anita_files", "clearance_wait", "read_fully", "record_second", "therapist_call",
       "bus_route_map", "packet50", "agency_meeting", "kessler_letter", "night_before50",
       "anita_interview", "the_hearing50", "outcome50", "end_sameschool"],
      "Ending — Same School, Family Address"),
 51: (["start", "denial_anatomy", "request_findings", "felix_visit", "attic_history", "read_summary",
       "marta_talk", "correction_packet", "measurements", "call_lucia", "the_drive51",
       "two_envelopes", "supervisor_call", "reconsideration", "tricky_question", "neighbors",
       "restudy_set", "restudy_day", "ms_tomas_letter", "approval_clock", "lucia_call2",
       "hearing_prep51", "july_review", "felix_bag", "outcome51", "end_secondlook"],
      "Ending — Approved on the Second Look"),
 52: (["start", "by_name", "sanaa_visit", "her_handwriting", "march_entry", "the_letter52",
       "agency_pushback", "hakim_list", "group_home_call", "hakim_house", "ashford_call",
       "kellerman_ask", "hakim_fingerprints", "hakim_interview", "records52", "sanaa_school",
       "kellerman_dinner", "counsel52", "packet52", "signature_watch", "transport_plan",
       "night_before52", "review52", "in_chambers", "outcome52", "end_familyaddress"],
      "Ending — A Family Address, Not a Facility"),
 53: (["start", "three_exceptions", "january_visits", "record53", "two_kitchens", "correction53",
       "esther_first_talk", "support_plan", "church_program", "study_dates", "nina_preschool",
       "selah_voice", "school_question", "rafi_therapist", "selah_terms", "selah_weekend",
       "proposal_filed", "selah_art", "clearance_renewal", "home_visit53", "esther_doctor",
       "room_fix", "gideon_work", "foster_position", "sibling_saturdays", "bridge53",
       "agency_split", "exception_draft", "march20_report", "children_words",
       "continuance_scare53", "asfa_memo", "packet53", "night_before53", "review53",
       "outcome53", "end_allthree"], "Ending — All Three, One Table"),
 54: (["start", "otto_visit", "counsel54", "current_foster", "request54", "veronica_program",
       "redaction_fight", "the_item", "item_by_item", "scoring_page", "level2_tour", "visit_logs",
       "riverton_distance", "center_director", "correction_filing", "agency_response54",
       "memo_filed", "gal_position", "foster_statement54", "salvatore_call", "salvatore_house",
       "salvatore_files", "clearance_sal", "conference_day", "narrowed_order", "study_visit54",
       "rater_call", "otto_school", "agency_concede", "hearing_prep54", "packet54",
       "score_recompute", "night_before54", "morning54", "review54", "outcome54",
       "end_readinfull"], "Ending — Read in Full"),
 55: (["start", "when_who_written", "call_beatrice", "zola_call", "counsel55", "school_records",
       "file_three", "agency_version", "interim_ask", "transport_log", "first_riverton_visit",
       "halvorsen_call", "record_arrives55", "binder_scene", "the_date55", "september_flag",
       "two_dates", "supervisor_meet55", "imani_program", "courtesy_study", "county_capacity",
       "beatrice_clearances", "beatrice_interview", "beatrice_study", "daughter_plan",
       "school_letter55", "transmittal", "zola_weekend", "zola_counsel", "foster_statement55",
       "packet55", "agency_position_paper", "night_before55", "pre_review_call55",
       "december_morning", "review55", "outcome55", "end_backacrosstheline"],
      "Ending — Back Across the Line"),
 56: (["start", "folder_system", "sort_winter", "lev_visit", "appeal_filed", "gregory_house",
       "sponsor_talk", "identifiers_ask", "cousin_check", "agency_meeting56", "correction56",
       "db_holders", "program_letter56", "park_return", "records56", "foster_mother56",
       "hospital_records", "page_eleven", "narrative_vs_file", "hearing_prep56",
       "attendant_interview", "january_visit", "study_restart", "gregory_references",
       "katya_work", "childline_letter", "hearing_eve", "hearing56", "the_wait56", "confirm56",
       "gregory_gate", "study_addendum", "decision_call", "decision56", "march_packet",
       "barlow_call", "gregory_call56", "outcome56", "final_gate56", "end_bothfiles"],
      "Ending — Both Files, Corrected"),
}

bad = 0
for n, (path, win_title) in ROUTES.items():
    data = json.loads((G / f"scenario-{n}.json").read_text())
    nodes = {nd["id"]: nd for nd in data["nodes"]}
    cash = data["meta"]["startCash"]
    flags = set()
    ok = True
    for i, nid in enumerate(path[:-1]):
        nd = nodes[nid]
        nxt = path[i + 1]
        cand = [c for c in nd.get("choices", []) if c["next"] == nxt]
        if not cand:
            print(f"S{n}: NO CHOICE {nid} -> {nxt}"); ok = False; break
        c = cand[0]
        for f in c.get("requiresFlags", []):
            if f not in flags:
                print(f"S{n}: GATE FAIL at {nid}: requires {f}, have {sorted(flags)}")
                ok = False
        for f in c.get("requiresNoFlags", []):
            if f in flags:
                print(f"S{n}: NEGATIVE GATE FAIL at {nid}: forbids {f}"); ok = False
        flags.update(c.get("setFlags", []))
        cash += c.get("cash", 0)
    end = nodes[path[-1]]
    title_ok = end["title"] == win_title
    rr = "recordsRequested" in flags
    print(f"S{n}: {'WALK OK' if ok and title_ok else 'PROBLEM'} — {len(path)} steps, "
          f"final cash ${cash}, recordsRequested on route: {rr}, win title match: {title_ok}")
    print(f"    path: {' → '.join(path)}")
    if not (ok and title_ok and rr):
        bad += 1
print("ROUTE FAILURES:", bad)
raise SystemExit(1 if bad else 0)
