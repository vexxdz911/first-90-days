#!/usr/bin/env python3
"""Path check for strategy-33.md / strategy-34.md: walk the JSON graph from
the start node following each guide route's node sequence; assert every
step is a real edge, the final node is the guide's named ending, and every
route node's title appears in the corresponding guide."""
import json, os
D = os.path.dirname(os.path.abspath(__file__))

ROUTE33 = ["start","motion_notice","lawyer_map","class_night","written_progress",
 "records_beat","file_arrives","visits_rhythm","school_form","two_timelines",
 "referral_call","shift_conflict","progress_review","which_track","screens_filed",
 "assessment_pages","foster_home_meeting","plan_checkpoint","summer_visit","birthday",
 "last_class","counsel_letter","strategy_choice","path_services","hearing_services","end_denied"]

ROUTE34 = ["start","shelter_care","folder_begins","worker_one_plan","sign_in_sheet",
 "receipts_habit","visits_first_log","notebook_habit","certificate","supervisor_beat",
 "handoff_one","worker_two","referral_lost","reprove","visit_log_restarts","copy_shop",
 "records_request","file_seams","folder_fills","handoff_two","worker_three","plan_retyped",
 "visit_paper","eli_question","winter_visits","review_notice","folder_audit","hearing_eve",
 "prep_choice","review_prevails","end_folder_prevails"]

def walk(num, route, guide_name):
    scen = json.load(open(os.path.join(D, f"scenario-{num}.json")))
    by = {n["id"]: n for n in scen["nodes"]}
    assert route[0] == scen["meta"]["startNode"]
    cash = scen["meta"]["startCash"]
    for a, b in zip(route, route[1:]):
        edges = [c for c in by[a].get("choices", []) if c["next"] == b]
        assert edges, f"scenario-{num}: no edge {a} -> {b}"
        cash += edges[0].get("cash", 0)
    end = by[route[-1]]
    assert end.get("ending"), f"scenario-{num}: route ends at non-ending {route[-1]}"
    guide = open(os.path.join(D, guide_name)).read()
    assert end["title"] in guide, f"guide does not name ending {end['title']}"
    for nid in route:
        assert by[nid]["title"] in guide, f"guide missing node title: {by[nid]['title']}"
    print(f"scenario-{num}: PATH CHECK PASS {' -> '.join(route)}")
    print(f"  ending reached: {end['title']} | route cash delta applied at first edges only-check startCash-endCash~{cash} (guide reports route spend separately where a node offers two cash paths)")
    return end["title"]

if __name__ == "__main__":
    walk(33, ROUTE33, "strategy-33.md")
    walk(34, ROUTE34, "strategy-34.md")
    print("BOTH PATH CHECKS PASSED")
