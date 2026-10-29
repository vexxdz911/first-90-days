# Expansion Completion — The First 90 Days, Scenarios 37–136

*Integration completed 2026-10-29. This document is the integration record: final totals, validation evidence, repairs, deployment, and the gates that still stand. Companion files: `expansion-rename-log.md` (Step 1), the expansion note appended to `sources-and-alterations.md` (batch map and verified law), `sources-batch-F.md` … `sources-batch-O.md` (per-batch sources).*

## Final totals (computed from the scenario data, never hand-typed)

| | Scenarios | Scenes | Endings |
|---|---|---|---|
| Foundation | 27 | 493 | 55 |
| Hard | 48 | 1,290 | 145 |
| Complex | 61 | 2,321 | 230 |
| **Library total** | **136** | **4,104** | **430** |
| *of which the expansion (S37–136)* | *100 (20 / 35 / 45)* | *3,056* | *313* |

Version 1 shipped 36 scenarios / 1,048 scenes / 117 endings; the expansion adds exactly 100 scenarios, 3,056 scenes, and 313 endings on top of it. The library page (`index.html`) shows these same computed numbers.

## Step 1 — Rename pass

Programmatic principal-collision scan over all 136 scenario JSONs (introduction patterns, kinship extraction, two frequency bands, manual context review of every candidate). **5 renames**, all inside the expansion, later scenario changed per house convention, replacements verified unused corpus-wide: S86 Amara→**Nyla**; S105 Beatrix→**Maren** and Rosalind→**Vivian**; S100 Pearl→**Iris**; S110 Fern→**Alma**. Production watchlist dispositions: Marta and Felix had already been resolved inside Batch G's files during production (no collision remained). Post-pass re-scan: zero principal collisions within S37–136 and none against Version 1 principals. Surname-only overlaps among one-scene officials (39 surnames) logged, not renamed, per house practice. Pre-existing principal-name repeats *inside* Version 1 (e.g., Eli, Jonah, Sam) were logged in the rename log and deliberately not altered — Version 1's JSONs remain byte-identical to its shipped editions. Full record: `expansion-rename-log.md`.

## Step 2 — Central validation of the 100 (run on final, post-rename files)

**Result: 0 failures** across every check:

- JSON parse; node-id uniqueness; start-node presence; every choice's `next` resolves.
- Reachability: every node reachable from the start (gate-blind BFS, all 100).
- Ending debriefs: every ending node carries a non-empty debrief.
- Monotonic dayOffsets along every choice edge (all 100).
- Kicker dates: every full-date kicker recomputed from `startDateISO + dayOffset` against the real calendar — all match, weekday included.
- Citation sweep against the final verified set (Version 1 set + Batch G § 6336.1 / § 6302, Batch I § 6341(a)/(c)/(d) + § 6351, Batch K Pa.R.A.P. 903, Batch N ESSA/CFR items, plus 23 Pa.C.S. § 6302, documented in Batch L's record as part of the shared kinship set): every titled citation in the 100 is inside the set. One adjudication: S102's 23 Pa.C.S. § 6302 cites are the CPSL kinship definitions, as documented — kept.
- Forbidden-term scan (no assessment called AI / machine learning / predictive / algorithmic): clean.
- Script parity: every `scenario-N-script.md` matches its JSON node-for-node (ids, order, titles, choice texts).
- Strategy-guide win-name parity: every guide's named best ending resolves to an ending node in its scenario (all three house guide formats handled; Batch K's prefix-less quoting and trailing-period punctuation normalized).
- **Gate-aware ending reachability** (engine semantics: `requiresFlags` / `requiresNoFlags` filter choices): every ending of every scenario is reachable — by exhaustive state-space BFS for 97 scenarios; by exhaustive BFS at 50,052,185 states for S46; by targeted per-ending DFS for S129 and S130, whose state spaces overflow BFS memory.
- **Dead-state scan**: no reachable (node, flag-set) state in any scenario leaves the player without an available choice (exhaustive for 97; for S46/S129/S130, exhaustive to 600k states plus 2,000 seeded walks each).

### Defects found and repaired at the source (JSON → script → guide, then re-validated)

1. **S123 — unreachable ending.** *Ending — The Kind Stranger's Season (partial)* required `conflictRaised` without `locatedInWriting`, but the only route to the objection beat ran downstream of the location letters, so the flag combination could never occur. Fix: one objection choice added at `assignment_news` (day 18), the node whose own text stages the objection, mirroring the existing objection's flags and file entry. A gate-honoring witness path to the ending now exists and is recorded in the validation run.
2. **S64 — decision-node partition hole.** At `filing_day`, a packet filed with the waitlist letter but without the therapy record (`packetFiled ∧ waitlistDoc ∧ ¬therapyDoc ∧ ¬oralRaised`) had no available choice (4 of 200 seeded walks stranded). Fix: one summation choice in the node's voice → *Filed, With the Record Complete*, the landing the guide already names for a packet filed on a thinner base.
3. **S66 — decision-node partition hole.** At `review66`, summary + advance notification without step-down enrollment (`dischargeSummary ∧ agencyNotified ∧ ¬stepdownEnrolled`) had no available choice (28 of 200 walks stranded). Fix: one summation choice → *Goal: Not Completed*, with a clarifying sentence added to the guide's wrong-turn entry.
4. **S113 — decision-node partition hole.** At `review_circle`, a filed packet missing the program letter and/or the housing document had no available choice (33 of 200 walks stranded). Fix: two summation choices (one per missing document) → `filing_eve`, landing at *The Date Strikes, Undocumented*; a seventh wrong-turn entry added to the guide.

No other story logic was changed anywhere in the 100.

## Steps 3–4 — Editions and library

- **200 playable editions generated** (comic-N.html + play-N.html for N=37–136) by data-swap on the shipped graphics-v2 files (comic-24/play-24 as templates). Method proof: rebuilding Scenario 24 from its own JSON reproduces the shipped files **byte-for-byte**. Per-file proof for all 200: embedded scenario data is canonical-JSON-equal to its `scenario-N.json`; everything outside the data block is byte-identical to the shipped v2 engine (verified by skeleton hash on all 200), so plates, cast, Red Law, Watch Mode, and the per-scenario save keys (`first90days-save-v1-s<N>`) carry over exactly.
- **Library rebuilt at 136**: v2 home design, gate box and footer wording preserved, zero JavaScript (0 `<script>` tags), EXHIBIT A/B/C sections extended to all 136 cards in numeric order within tiers; every count on the page computed from the data; all 408 edition links resolve to files on disk. The sections-external diff against the previous page is exactly: eyebrow (EXPANDED EDITION), standfirst, the five stats, and the footer's batch-range line (now sources-batch-A…O).

## Step 5 — QA on the built set

- **Syntax:** `node --check` on every script block — 416 blocks across the 200 new files (incl. the 4 repaired scenarios' rebuilds): 0 failures.
- **Seeded walks:** final pass on the built files — 25,400 gate-honoring random walks (200 per scenario; 2,000 each for S46/S129/S130): **every walk terminated at an ending; zero stuck, zero overlong.** (The pre-repair pass is what caught the S64/S66/S113 holes above.)
- **Red Law:** the red token `#b3202a` appears exactly once in each of the 100 new comic files; `var(--red)` occurs only in the clock/stamp rules, as shipped.
- **Sizes:** largest new comic file 166,394 bytes; largest plain file 100,684 bytes — under the ~200KB budget.
- **Kicker spot-checks on built files** (independently recomputed): S53 ASFA node "Day 108 — Thursday, April 22, 2027" ✓; S56 ending "Day 95 — Friday, March 12, 2027" ✓; S64 filing decision "Day 156 — Wednesday, February 3, 2027" ✓; S123 repaired ending "Day 52 — Thursday, February 25, 2027" ✓.

## Step 6 — Deployment

Sync convention followed exactly as established at Version 1 (whole game folder, excluding `__pycache__`, `home-cards.json`, `home-redesign-spec.md`, `home-redesign.md`; the public repo's own `README.md` untouched):

- **Private repo** `vexxdz911/tacticwatch` (game corpus under `game/`): commit **fbfd275** — 549 files added, 2 modified. Pushed.
- **Public repo** `vexxdz911/first-90-days` (game-only): commit **e438fbf** — 549 files added, 2 modified. Pushed.

**Live verification** (https://vexxdz911.github.io/first-90-days/): library returns HTTP 200 at 131,228 bytes with 136 cards and the computed stats; comic-37, comic-100, comic-136, and play-87 each return HTTP 200 with the v2 markers (comic kit gradients, Watch Mode, red token exactly once in the comics) and their correct per-scenario save keys and titles. Nothing else was sent or published anywhere.

## Standing gates (unchanged)

The expansion changes none of the gates. **Attorney verification** and a **compensated lived-experience review** still stand between this library and any organizational or parent-facing program use; the library page's READ FIRST box says so, and the PROTOTYPE stamp stays on the cover. The scenarios remain fictional composites built from published opinions and documented patterns — no real family's case, and no private case in the author's orbit, appears anywhere in the 136.
