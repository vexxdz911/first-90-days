# THE FIRST 90 DAYS — VISUAL BIBLE
### The comic-book / graphic-novel design system for the Tactic Watch simulation
*Version 1 — 2026-10-28. Companion build: `play-comic.html` (Scenario 1 reskin). Key art: `art/cover-art.webp`, `art/interior-sample.webp`. Everything in this system must be producible inside a zero-asset single HTML file — inline SVG and CSS only, no images, no webfonts, no network.*

---

## 1. North star: the key art

Two generated plates set the target:

- **Cover** — a mother seen from behind (hair in a bun, amber sweater, an envelope in her hand) facing her own front door. Through the door's frosted glass: the caseworker's silhouette, clipboard in hand, more shadow than person. Deep navy darkness above; warm amber lamplight below; halftone dots throughout; small true details at the edges (keys on hooks, children's photos, a pair of small shoes).
- **Interior sample** — three stacked panels on an amber halftone page: a fist knocking (close-up), two women at a kitchen table covered in paperwork, and a courtroom seen from behind the mother's seat — the judge small and far away, the mother large and near.

What the art is doing, and what every screen must do:

1. **The camera stays with the mother.** We see what she sees, from where she stands. The system is always across the table, across the room, behind glass.
2. **Duotone only.** Ink navy and paper amber. There is no full-color world in this story.
3. **Paperwork is a physical presence** — folders, envelopes, forms — drawn as carefully as faces.
4. **Dignity is the style.** Nobody is caricatured. Nobody is a villain with a curled lip. The caseworker is a silhouette with a clipboard because *that is what she is to the mother*: a role, behind glass.

## 2. Art direction

**Dignified graphic-novel realism, evoked — not reproduced.** A single HTML file cannot hold 900 painted panels (see §11), so the kit evokes the key art through flat duotone SVG scenes, halftone texture, heavy ink panel borders, and caption-box lettering. The evocation succeeds if a player who has seen the cover recognizes the same world.

**Temperature is meaning:**

| World | Rendering | How the kit expresses it |
|---|---|---|
| **Family spaces** (home, kitchen, doorway, visits) | Warm — amber-forward gradients, lamplight glow, halftone dense and soft | `gradWarm` plate gradient (cream → amber), amber figure tint for the mother, paper-colored caption boxes |
| **The system** (agency office, courtroom, records desk, hospital) | Cold — flatter, navy-forward, harder geometry, fluorescent bars, filing grids | `gradCold` plate gradient (steel navy → base navy), flat rectilinear set dressing, figures in full ink silhouette |
| **Threshold spaces** (mail room, school, apartment exterior) | Mixed — cold architecture, one warm human element | Cold gradient + one amber accent object (a lit window, an envelope, a porch light) |

**Hard rules:**

- Never cartoonish about trauma. No exaggerated expressions, no speed lines on people, no "POW!" grammar anywhere — with exactly one borrowed device (§4.4).
- No superhero framing of the mother either. She is not drawn larger than life; the *camera* is close to her, which is a different thing.
- Figures are symbolic silhouettes/duotone shapes — never portraits, never resembling any real person.
- Children are drawn small, plain, and unposed. No child figure is ever placed in a distress composition.

## 3. Palette

Base tokens, sampled from the key art:

| Token | Hex | Use |
|---|---|---|
| `--ink` | `#0d1520` | Panel borders, silhouettes, body text on paper |
| `--navy` | `#16283f` | Page field in system spaces, top bar, cold shadows |
| `--navy-2` | `#1f3a5c` | Cold mid-tone, complex-tier field |
| `--amber` | `#e8b04b` | Paper amber — warmth, the mother, primary buttons |
| `--amber-deep` | `#c98f2b` | Figure tint (sweater), hover/active states |
| `--paper` | `#f3d9a4` | Page background, warm panels |
| `--cream` | `#f7ead0` | Caption boxes, text on navy |
| `--red` | `#b3202a` | **Restricted — see the Red Law** |

**Tier accents** (set on `<body data-tier="…">` from scenario metadata; v1 scenarios carry no tier in data, so the skin defaults to amber and the hook is in place for the tiered library):

| Tier | Accent | Rationale |
|---|---|---|
| Foundation | Warmer amber (`#e8b04b` family, glow up) | Teaching scenarios — the warmest light |
| Hard | Desaturated steel (`#7e93a8`) | The warmth drains; the system gets more of the frame |
| Complex | Colder blue (`#5b83ad` on `#1f3a5c`) | Multi-track stories live mostly in system spaces |

**THE RED LAW.** Red (`--red`) appears in exactly two places in the entire game: **(1) THE CLOCK** — deadline boxes; **(2) the RATED stamp**. Nothing else may use it — not warnings, not errors, not the content-warning card (which is ink-on-paper with a heavy border), not links, not the Quick Exit. Red is the color of *time running out* and *being judged*; if it appears anywhere else, both signals die. Any future design PR that adds a red element outside these two is rejected on this page's authority.

**Measured contrast** (WCAG 2.x relative-luminance ratios, computed from the hex values):

| Pairing | Ratio | Verdict |
|---|---|---|
| Ink on paper-amber (body text) | 13.34 : 1 | AAA |
| Ink on cream (captions) | 15.40 : 1 | AAA |
| Cream on navy (panels, HUD) | 12.51 : 1 | AAA |
| Amber on navy (kickers, accents) | 7.62 : 1 | AAA (large) / AA (body) |
| Cream on clock red (THE CLOCK text) | 5.59 : 1 | AA |
| Stamp red on cream (RATED) | 5.59 : 1 | AA — and never color-alone (§9) |
| Paper-amber on cold navy (Complex) | 8.40 : 1 | AAA |

## 4. Panel grammar

### 4.1 The page
The page field is the amber halftone of the interior sample: a CSS radial-gradient dot pattern over `--paper`, dots in a slightly deeper amber. Every screen is a page; every node is a panel stack on it.

### 4.2 Hero panel (location plate)
One per node, at the top of the story panel: a 16:9 inline-SVG plate (§6) inside a 4px ink border with a hard offset shadow. The plate establishes *where she is* before a word is read. Endings get plates too — an ending is a panel, not a form.

### 4.3 Caption boxes
Narration lives in caption boxes, as in the key art's grammar: paper-cream rectangles with a 2px ink border, set in the upper area of the panel, text in ink, first paragraph of each node optionally italic (the "voice-over" line). In the build, the node's body paragraphs render inside one caption-box container. The node's kicker sits *above* the panel as a caption tab: uppercase, letterspaced, ink on amber.

### 4.4 Choices as panel-option rows
Choices are full-width rows styled as adjoining mini-panels: cream field, 2px ink border, bold text, a small numbered tab at the left edge (1, 2, 3…) set in a navy square. Hover/focus lifts the row 2px with the hard shadow growing — a page being turned, not a button being pressed. Minimum height stays 56px.

### 4.5 THE CLOCK
When a deadline is live, it renders as a black box — ink-black field, cream text, red used for the box's label strip and border only: a small red tab reading **THE CLOCK**, then the deadline sentence in cream. It is `role="alert"`, it appears the moment the removal flag is set, and it never blinks, pulses, or animates. Time in this game does not shout; it just stays on the page. (Audio: the `tick` cue fires once, when the box first appears — §8.)

### 4.6 The case file (assessment panel)
The hidden-assessment panel is styled as a case-file folder: tabbed top edge, cream card stock, dashed "sealed" border while locked, with the 🔒 line from the engine. When records are released, the border goes solid and the § 3130.44(d) caption prints like a stamp of the *good* kind — in ink, not red. Ink is what the mother makes; red is what is done to her. That asymmetry is deliberate.

### 4.7 THE STAMP — the one borrowed device
Superhero comics get one device in this game, and only one: **impact**. When a choice causes the system to rate the player (a choice carrying `addHidden`), a red **RATED** stamp slams onto the case-file card: rotated −12°, double-rule border, letterspaced capitals, entering with a fast scale-from-2.2 impact animation (~180 ms) and a `stamp` audio cue. Then it stays, faded to 85%, for that screen — a mark on the file.

- The stamp is the *only* impact effect, the *only* animation of violence-adjacent energy, and one of only two legal uses of red.
- It lands on the **file**, never on the mother, never on a child figure.
- `prefers-reduced-motion`: the stamp does not slam; it fades in at final size and rotation.
- It always says RATED in text — the signal is never color alone.

### 4.8 Epilogue pages (endings)
Endings render as an epilogue spread: the hero plate, the outcome in a caption box, then the debrief as a ruled "epilogue page" card — cream, ink, with the debrief list set like endnotes — and the revealed assessment record beneath it, fully open. The chord cue (§8) is warm for the home ending, flat otherwise; the page does not celebrate or mourn beyond that.

### 4.9 The cover (start screen)
The start screen evokes the cover composition in pure SVG: navy field deepening at the top, the door at center with frosted glass, the caseworker's silhouette inside the glass, the mother in the right foreground with her back to us. No text in the art; the game's real title and disclaimers sit below it as caption matter. The webp itself is **never** embedded — the file stays zero-asset.

## 5. Cast — reusable figures

Ten figures, one design language: flat silhouette bodies in `currentColor` (tintable per plate), heads as simple circles with one hair/hat distinction each, **exactly one prop per figure**, drawn as `<symbol>`s (`fig-*`) in a hidden SVG defs block and instanced with `<use>`. Figures are read at postcard size; they are *roles*, not people.

| Figure | Symbol | Silhouette key | Prop |
|---|---|---|---|
| Mother | `fig-mother` | Hair in a bun, sweater body | Envelope (paper) |
| Grandmother | `fig-grandmother` | Low bun, shawled shoulders | Cane |
| Caseworker | `fig-caseworker` | Plain jacket, hair back | **Clipboard** |
| Attorney | `fig-attorney` | Suit, shorter jacket line | Folder (paper) |
| Judge | `fig-judge` | Seated torso, robe V | Gavel |
| Teen | `fig-teen` | Tall, slim, hooded top | Phone (small paper rect) |
| Child | `fig-child` | Half-height, plain | Backpack (paper) |
| Father | `fig-father` | Cap, broad shoulders | Paper letter |
| Officer | `fig-officer` | Cap with brim, uniform body | Badge (paper dot) |
| Doctor | `fig-doctor` | Coat line, plain head | Stethoscope (paper stroke) |

Casting rule: a plate uses **at most two figures**. Crowds are rendered as architecture (rows of chairs, a bench, a wall of mailboxes) — the system's scale is shown by its rooms, not by multiplying people.

## 6. Plates — reusable location scenes

Ten plates (`plate-*` symbols, 400×225 viewBox), each a flat duotone composition of 10–16 shapes over the warm or cold gradient, with the halftone pattern overlaid at low opacity:

| Plate | Temp. | Composition (anchor elements) | Typical figures |
|---|---|---|---|
| Doorway | Warm | Door with frosted-glass pane, mail slot, warm hall glow | Caseworker *inside the glass*; Mother at frame edge |
| Kitchen | Warm | Table band, cabinets, papers on the table | Mother, Caseworker |
| Agency Office | Cold | Desk, filing cabinets, fluorescent bars | Caseworker |
| Courtroom | Cold | Bench block, flag, rows of seats; mother large in foreground | Judge (small, far), Mother (near) |
| Visit Room | Warm-neutral | Couch band, toy blocks, door with a small window | Mother, Child |
| Hospital | Cold | Bed band, curtain lines, chart at the foot | Doctor, Mother |
| School | Warm | Facade, steps, flag, lit windows | Child |
| Apartment Exterior | Cold dusk | Facade grid, lit windows, porch light | — (place alone) |
| Mail Room | Cold-neutral | Wall of mailbox doors, one open with an envelope | Mother |
| Records Desk | Cold | Counter, folder stacks, shelved files | Caseworker |

### 6.1 Selection convention (v1: no data changes)
The engine chooses a node's plate from its **kicker + title** text, lowercased, against an ordered keyword table — **first match wins**, so order is part of the design:

| # | Keywords (any) | Plate |
|---|---|---|
| 1 | hospital, clinic, doctor, nurse, medical, exam | Hospital |
| 2 | court, hearing, judge, shelter care | Courtroom |
| 3 | knock, door, house, the visit, removal, doorstep, threshold | Doorway |
| 4 | supervised, visit room, one hour | Visit Room |
| 5 | school, teacher, classroom, class | School |
| 6 | records, file, flyer, reading, written, case against you, packet, redact | Records Desk |
| 7 | mail, letter, envelope, notice | Mail Room |
| 8 | interview, questions, supervisor, service plan, review, check-in, lawyer, attorney, counsel, decision, plan, form | Agency Office |
| 9 | apartment, building, street, porch, outside | Apartment Exterior |
| 10 | evening, morning, kitchen, table, home, gap | Kitchen |
| — | **Fallback** | **Kitchen** (the family's ground; the warmest plate; where an unplaceable moment most plausibly happens) |

Ordering notes, so future editors don't "fix" them: Courtroom outranks Kitchen so *Home After a Hearing* still plates as the courtroom that decided it; Agency Office outranks Apartment Exterior so *She Steps Outside to Call Her Supervisor* plates as the system, not the street; Doorway's `the visit` is deliberately narrow so the *supervised* visit (rule 4) is not stolen by home-visit nodes.

**Scenario 1 audit** (all 27 nodes, machine-checked against the shipped table): 26 of 27 plate as intended — knock/removal → Doorway (and the `knock` cue), interviews/decision/check-in/service plan/review → Agency Office, hearing → Courtroom, records beats → Records Desk, supervised visit → Visit Room, evenings/home beats/endings → Kitchen. The one miss is documented, not hidden: **"Not Yet"** (the post-hearing ruling node) contains no keyword and falls back to Kitchen. The convention accepts this rather than growing a one-word rule for a single node title; if the node is ever retitled, the table will catch it.

### 6.2 What plates are not
Plates are *establishing shots*, not illustrations of the node's action. A plate never depicts the moment of removal, an injury, an argument, or any child's distress. The hardest panels in this game are a door, a table, an empty chair.

## 7. Lettering & type

System fonts only — no webfonts, ever. The comic feel comes from treatment, not typefaces:

- **Kickers / caption tabs:** uppercase, `letter-spacing: .12em`, bold, ink on amber.
- **Titles:** the system sans at 700, tight leading — treated as panel titles.
- **Narration:** body serif-adjacent feel is *not* faked; captions use the system sans at normal weight with the first paragraph italic — the typewriter-adjacent voice comes from the caption-box framing, short paragraphs, and hard borders.
- **THE CLOCK and RATED:** letterspaced capitals, the two loudest voices in the game, both restricted (red law / stamp law).
- Numbers in the HUD (dates, cash) render as a "caption strip" — small, uppercase, letterspaced — like the date boxes in a comic's first panel.

## 8. Sound hooks (visual-side contract)

The build ships a no-op stub — `window.Cue = window.Cue || { play(){}, setEnabled(){}, isEnabled(){ return false; } }` — and calls it at exactly these moments. The audio team's library replaces the stub without touching the build:

| Cue | Fires when |
|---|---|
| `page` | A new story node renders (including auto-advance in Watch Mode) |
| `knock` | A node plates as Doorway |
| `stamp` | A choice's `addHidden` lands — synchronized with the RATED stamp |
| `tick` | THE CLOCK box appears for the first time in a run |
| `unlock` | The `recordsRequested` flag is set — the file opens |
| `chord_warm` | The home ending renders |
| `chord_flat` | Any other ending renders |

## 9. Watch Mode — presentation rules

Watch Mode (the game playing itself with random choices) is a *presentation* of the same panels, and it must never be visually confusable with guided play:

- **The banner.** A slim navy strip under the top bar for the entire run: **"WATCHING — choices are random. The strategy guide shows the winning route."** It carries the Pause/Resume, Speed (1×/2×), and Take control controls. It never disappears mid-run.
- **The chose strip.** When the story picks for itself, the chosen row is highlighted in amber and a caption strip prints above the choices: *"The story chose: …"* — set like a caption box, in the past tense, so a screenshot can never be mistaken for advice.
- **Pacing.** Delays scale with the node's text (≈200 wpm, 2.5 s floor, 12 s cap; interstitial notes get a shorter beat). The ending is never auto-advanced: the debrief stays on screen. Only the start screen's **Loop for presentations** toggle may restart a run, ~20 s after an ending, for kiosk/training-room use — and the ending screen says so while it waits.
- **The save is sacred.** A watch run lives in memory only; it never writes, overwrites, or clears the player's manual save. Taking control is the single moment a watch state may become a save — because at that moment it stops being a watch.
- **Quick Exit still works** and freezes the watch timer while the decoy is up; returning resumes the current panel's pacing.
- **Reduced motion** changes nothing about pacing — only the stamp's slam becomes a fade (§4.7).

## 10. Accessibility

- Contrast: every text pairing meets WCAG AA; the main pairings meet AAA (table in §3).
- **No information by color alone:** THE CLOCK is a labeled box, not a red glow; the stamp reads RATED in letters; the deadline is a sentence, not a hue; tier accents never carry meaning.
- `prefers-reduced-motion`: stamp slam → fade; choice hover lift → none; no other animation exists to disable.
- Plates are `role="img"` with a text label ("Scene: courtroom") — decorative to the story, available to a screen reader, never the sole carrier of plot.
- Tap targets ≥ 56px (choices), ≥ 48px (controls) — inherited from the base engine and preserved in the reskin.
- Focus states: 3px amber outline on navy, 3px ink outline on paper — visible on both fields.

## 11. Production math — why a kit, and what comes after

Version 1 is **36 scenarios**. At Scenario 1's density (27 nodes), the full library is roughly **900–1,000 nodes**, each of which would need its own painted panel in a fully illustrated edition — 900+ commissions, with consistency of faces, rooms, and palette across all of them, before a single line of dialogue ships. That is the *illustrated edition*: a real and worthwhile future artifact, and the two key-art plates exist precisely to anchor its style when funding and time allow.

The kit inverts the cost: **10 plates + 10 figures + 1 grammar** cover all 36 scenarios, because the stories reuse the same *rooms* the system itself reuses — the same doorway, the same office, the same courtroom, county after county. That reuse is not only economical; it is the point. The system's sameness is part of what the game is about. New scenarios inherit the full visual identity the day their data file lands, at zero art cost, and the keyword convention means they need no visual authoring at all.

Expansion path, in order: (1) more plates for locations the library grows into (prison visiting room, treatment facility, school office); (2) figure variants (a second caseworker, a second mother — the system and the families both deserve more than one face); (3) the illustrated edition, scenario by scenario, starting with Scenario 1, reusing this bible's palette, grammar, and red law unchanged.

## 12. Build rules (non-negotiable for anyone reskinning)

1. Zero assets: no images, fonts, or URLs. The key art is a *reference*, never an embed.
2. Scenario data is byte-identical to the plain build — a reskin touches presentation and hooks only.
3. Save/resume and Quick Exit behavior are identical to the plain build; Watch Mode adds its own layer and never writes the manual save.
4. Red appears only in THE CLOCK and the RATED stamp.
5. Every cue call in §8 exists; the file must run perfectly on the no-op stub alone.
6. **Choice gating is engine law** (from Scenario 24's production requirement): a choice may carry `requiresFlags` (renders only when ALL listed flags are set) and/or `requiresNoFlags` (renders only when NONE are set). Unmet choices are **not rendered — hidden, never shown locked** (the data carries no lock text, and a greyed-out door teaches nothing). Choices without these fields behave exactly as before; all other scenarios are unaffected. The comic build is where this entered the standard engine; every future build inherits it, and its QA includes a synthetic gating scenario.
