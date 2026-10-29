# Expansion Rename Log — Integration of Scenarios 37–136

*Integration pass, 2026-10-29. Companion to `sources-and-alterations.md` (which carries the expansion note) and `expansion-completion.md` (final totals and QA).*

## Method

All 136 scenario JSONs were scanned programmatically for principal first-name collisions — a principal being a parent/player character, a child, or a kin lead. Extraction combined (a) introduction patterns in the opening nodes ("Your name is X", "You are X", kinship introductions for children and kin), (b) age-appositive and caregiving patterns across the full text, and (c) frequency sweeps at two thresholds (≥5 and 2–4 mentions) over body, debrief, choice, and summary text, with honorific surnames (Ms./Mr./Judge X) and sentence-position common words filtered out. Every candidate collision was then verified by reading its contexts before any rename was decided. Replacement names were required to have **zero mentions anywhere in the 136-scenario corpus** before use.

## Renames applied (5 — all inside the expansion; the later scenario changed, per the v1 integration convention)

| Scenario | Was | Now | Role | Files changed (replacements) |
|---|---|---|---|---|
| 86 | Amara | **Nyla** | Daughter, 13, of Quiana (S64's Amara, daughter of Katrina, keeps the name) | scenario-86.json (9), scenario-86-script.md (9); strategy-86.md and sources-batch-J.md never used the name |
| 105 | Beatrix | **Maren** | Daughter, 8 (S96's player, Beatrix Lindqvist, keeps the name) | scenario-105.json (31), scenario-105-script.md (31), strategy-105.md (1), sources-batch-L.md (1) |
| 105 | Rosalind | **Vivian** | Sister and kin lead holding the placement (S89's player, Rosalind Fenn, keeps the name) | scenario-105.json (30), scenario-105-script.md (30), strategy-105.md (several); sources-batch-L.md never used the name |
| 100 | Pearl | **Iris** | Newborn daughter of Shondra Lachance (S94's Pearl, daughter of Thaddeus Cole, keeps the name) | scenario-100.json (35), scenario-100-script.md (35), strategy-100.md (8) |
| 110 | Fern | **Alma** | Cousin and kin housing lead for Charise (S87's Fern, daughter, five, keeps the name) | scenario-110.json (30), scenario-110-script.md (30), strategy-110.md (6), sources-batch-M.md (5) |

Names only were changed — no story logic, flags, choices, dates, or law text was touched. After the pass, a re-scan confirms: **zero principal first-name collisions within Scenarios 37–136, and no expansion principal shares a first name with a Version 1 principal.**

Watchlist dispositions from production: **Amara** — real collision, renamed above. **Marta** — S51 resolved in production (the name no longer appears there); Marta appears only as S60's player. No collision. **Felix** — S51 resolved in production; Felix is principal only in S63. No collision.

## Reviewed and cleared (not principals, or not names)

- **Month words caught by the patterns** — April, August, January, March, October, September: every occurrence is a calendar month, not a character. (June is a real child in S1 — Version 1, below.)
- **Tomas (S49)** — an adult grandson and household member whose undisclosed presence drives the home-study plot; a supporting character, not a parent, child, or kin lead, and the only first-name Tomas in the corpus (S51's "Ms. Tomas" is a worker's surname). No rename.
- **Riverton (S54, S55)** — a shared fictional county name across two scenarios, not a person. Kept.
- Surname-only overlaps among officials (workers, lawyers, judges — used with honorifics, never as principal first names) are accepted house practice and were logged, not renamed: Abernathy, Adeyemi, Adler, Albright, Aldan, Almeida, Alvarado, Aubert, Beam, Beaumont, Bell, Delgado, Doyle, Ferreira, Fontaine, Harkness, Hart, Hartley, Ibarra, Karp, Lindqvist, Lindt, Marsh, Mendieta, Nakamura, Ndiaye, Okafor, Osei, Park, Petrakis, Petrov, Radcliffe, Romano, Salas, Thornbury, Tran, Voss, Whitaker, Whitfield.

## Version 1 (Scenarios 1–36) — pre-existing repeats, logged, not altered

Version 1 shipped with its own integration rename pass (S33 Wren→Lark, S34 Dana→Renee/Eli→Tobias, S35 Dana→Paula/Eli→Owen) and its scenario JSONs are byte-identical to the playable editions verified in the graphics-v2 rollout. The following principal first names repeat **inside Version 1 only** and were left exactly as shipped: Dana (S17, S31 — both players), Eli (a child in S1, S7, S13, S17, S20, S24, S26, S32), Jonah (S12, S19, S36), June (S1, S18, S25, S26), Mara (S12, S24, S32), Maya (S22, S36), Milo (S22, S27), Noah (S3, S5), Renee (S34, S36), Sam (S9, S15, S21, S28), Wren (S8, S14, S25, S31, S36). No expansion scenario reuses any of these names for a principal, so the expansion adds no new collision against Version 1. Renaming inside Version 1 would break the verified byte-identity of the shipped v1 editions and is a separate editorial decision, flagged here rather than taken silently.
