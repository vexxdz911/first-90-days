# The First 90 Days — Graphics & Design v2: Enhancement Notes

*2026-10-29. Team: Visual Storyteller + UI Designer + Brand Guardian (design), Frontend Developer (build), Accessibility Auditor + Finish-Gate Reviewer (independent QA), Orchestrator (rollout + deploy). Design system: `visual-bible.md` v2. Kit: `v2-kit.html`. Contract: `v2-design-spec.md`.*

## What changed

**New location plates (7)** — the library's rooms doubled from 10 to 17, all in the v1 flat-duotone idiom (400×225 symbols, halftone overlay, ≤2 figures, no text, no faces):
`plate-waiting` (agency waiting room), `plate-courtsteps` (courthouse steps, lit doorway the sole warm accent), `plate-schooloffice`, `plate-workplace` (warehouse racking — for the shift-work stories), `plate-busstop` (place alone, streetlamp the warm element), `plate-laundromat`, `plate-program` (parenting-class circle of chairs).

**New cast figures (6)** — distinct silhouette + exactly one prop each: `fig-caseworker2` (bob, shoulder bag), `fig-mother2` (long hair, tote), `fig-kin` (glasses, framed photo), `fig-supervisor` (blazer, coffee cup), `fig-toddler` (stuffed toy), `fig-child2` (older child, book). Existing figures untouched.

**Time/weather variants** — four overlay symbols (`ov-dawn`, `ov-dusk`, `ov-night`, `ov-rain` + `gradDawn` + `rain` pattern) instanced after the plate in the same SVG, chosen by `variantFor()` from kicker/title keywords: priority rain → night → dusk → dawn, one overlay max; rain and general night/evening words gated to the exterior family (Apartment Exterior, Courthouse Steps, Bus Stop, School, Doorway). Aria-labels carry the variant ("Scene: school, night").

**Plate selection** — `PLATE_RULES` grew 10 → 17 with audited ordering (School Office beats School; Program beats the generic "class"→School rule; Waiting Room and Courthouse Steps placed by title semantics; `\b` guards keep "bus" out of "Business Days" and "transit" out of "Transition").

**Panel craft & type** — display scene titles (`#app h2` 1.65rem/1.18), caption-box leading 1.62 with roomier padding, case-file tab enlarged (typographic only), plate matting switched to ink, tighter plate→kicker spacing. **Motion:** plate + caption box fade/rise 280ms on scene change, only under `prefers-reduced-motion: no-preference`; the RATED stamp's existing reduced-motion fade is unchanged; Watch Mode pacing untouched.

**Home page** — CSS-only v2 alignment (leading, tab letterspacing, hover lift + link transitions gated to `hover: hover` + no-preference). Zero JavaScript still; content and links provably identical to v1 (below).

## QA evidence

- **Scenario data integrity:** every comic file's data block is byte-identical pre/post skin (Scenario 1 block sha256-verified; rollout transplanted each file's original block) and canonical-JSON-equal to its `scenario-N.json` source for all 36 files + template. Plain editions and scenario JSONs untouched. Per-scenario save keys and `<title>`s preserved verbatim (including play-comic.html's historical `-s1-s1` key — existing saves are not orphaned).
- **Graph walks:** 500 seeded random walks per scenario × 36 scenarios = 18,000 walks with the engine's exact gating semantics — **0 dead ends; every ending of every scenario reached** (incl. Scenario 24's flag-gated routes).
- **Syntax:** `node --check` passes on the concatenated scripts of all 37 files.
- **Red Law (programmatic, two independent audits):** literal `#b3202a` occurs **exactly once per file** (the `:root` token) in all 37 comic files; `var(--red)` appears only in `.clockbox`, `.clock-tab`, `.stamp` rules; no other red-family hex/keyword anywhere (the one `#ffd23f` is the v1 Quick Exit yellow). The v2 kit contains zero red.
- **Contrast (computed, WCAG 2.x):** ink/paper 13.34, ink/cream 15.40, cream/navy 12.51, amber/navy 7.62, cream-on-clock-red 5.59, stamp-red-on-cream 5.59, amber/navy2 5.91, paper/navy2 8.40, cream/navy2 9.70, ink/amber 9.38 — all AA or better. v2 introduced **no new text/background pairings**; SVG art contains zero `<text>` elements.
- **Plate audit (all 1,048 nodes, shipped functions):** exactly **8 re-plates** vs v1, all Kitchen→new — Bus Stop ×5 (S5, S7, S8, S19, S32), Waiting Room ×2 (S19, S29), Program ×1 (S23) — and exactly **1 variant hit** (S33 "Track A, Night Class" → `ov-night` on School). The two design-flagged re-plates were finish-gate judged against their scene text and PASS (the S19 ledger node's subject is bus fares/transfers and names no room; the S23 paper is the program's own plan handed over at intake). Regression traps verified (e.g. "She Steps Outside to Call Her Supervisor" stays Agency Office; "Business Days" stays Kitchen). Courthouse Steps / School Office / Workplace / Laundromat match zero current titles — purely additive for future scenarios. Kitchen fallback 622 nodes (v1: 630 by the same corrected measure) — the family's ground, by design.
- **Guardrails:** every new plate ≤2 figures, ends with the halftone rect, no facial elements; each new figure has exactly one prop group. One deviation on record: `fig-toddler`'s single stuffed-toy prop is drawn with 3 paper-fill shapes (v1 idiom is 1–2) — auditor-judged PASS, noted knowingly.
- **Home page identity:** visible text nodes 337 = 337 and hrefs 113 = 113, sequences identical to the git-preserved v1; `<script>` count 0.
- **Process note:** the orchestrator's first plate audit undercounted (3 changes) because the harness read the JS `\b` escapes literally; corrected and re-run — it then reproduced the predicted 8 exactly. The shipped-function audit (developer) and the corrected audit agree.

## Sizes

- Template `play-comic.html`: **85,679 → 108,044 bytes** (+22,365: kit 20,310 + rules/variants/CSS).
- Comic files (36): **99,902 – 156,784 bytes** after v2 (largest: comic-28) — all well under the ~200KB budget. `index.html`: 46,178 → 46,424 bytes.

## Deployment

- Public game repo `vexxdz911/first-90-days`: commit **a29eaf8** (41 files).
- Private repo `vexxdz911/tacticwatch` (`game/`): commit **012bfcf** (41 files).
- **Live verified** at https://vexxdz911.github.io/first-90-days/ — after the Pages rebuild, the served `comic-1.html` contains `plate-waiting`, the served `comic-24.html` contains `ov-night`, and the served library page contains the v2 hover-gating CSS.

## Not changed

Plain editions (`play-*.html`, `play/index.html`), all scenario JSONs/scripts/strategy guides, the audio library, Watch Mode logic and pacing, Quick Exit, save format/keys, and every engine feature contract from visual-bible §12.
