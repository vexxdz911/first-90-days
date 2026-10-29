# THE FIRST 90 DAYS — COMIC EDITION v2: DESIGN SPEC / INTEGRATION CONTRACT

*For the front-end developer integrating `v2-kit.html`. Companion: `visual-bible.md` Version 2. Date: 2026-10-29.*
*Design team (Agency Agents roster, `~/.claude/agents/`): Visual Storyteller (`design-visual-storyteller.md`) — plates & cast; UI Designer (`design-ui-designer.md`) — CSS/typography in §3; Brand Guardian (`design-brand-guardian.md`) — §5 check, executed and signed off below.*
*Scope: this spec + `v2-kit.html` are the whole delivery. The developer edits `play-comic.html` (and the generated `comic-*.html` builds, through whatever generator produced them); the design team did not.*

---

## 0. How to integrate the kit (mechanics)

1. Paste the **entire** contents of `v2-kit.html` inside the existing `<defs>…</defs>` block in `play-comic.html`, **after** the v1 plates and **before** `</defs>`. Do not split the fragment: its internal order (gradients/patterns → figures → plates → overlays) is load-bearing, because the v2 plates `<use>` the v2 figures.
2. Add the seven new entries to `PLATE_IDS` (§1.3). No v1 entry changes.
3. Replace the `PLATE_RULES` array with the array in §1.1 **verbatim** — order and regex spelling are the design.
4. Add variant selection + rendering per §2 (new code, ~15 lines).
5. Apply the CSS changes in §3, items C1–C8, exactly as written. Nothing else in the stylesheet changes.
6. Run the QA protocol in §4.3 before calling it done.

ID safety (verified by the design team against the shipped `play-comic.html`): `gradDawn`, `rain`, and all 17 new symbol ids collide with **zero** v1 ids. Kit size: **20,310 bytes** (target was ≤ 30 KB).

---

## 1. PLATE_RULES additions

### 1.1 The final array — replace `PLATE_RULES` with this, verbatim

```js
const PLATE_RULES = [
  ["hospital|clinic|doctor|nurse|medical|exam", "Hospital"],
  ["waiting room|lobby", "Waiting Room"],
  ["courthouse steps|courthouse|on the steps|outside court|leaving court|after court", "Courthouse Steps"],
  ["court|hearing|judge|shelter care", "Courtroom"],
  ["knock|door|house|the visit|removal|doorstep|threshold", "Doorway"],
  ["supervised|visit room|one hour", "Visit Room"],
  ["parenting|program|support group", "Program"],
  ["school office|principal|guidance office|school counselor", "School Office"],
  ["school|teacher|classroom|class", "School"],
  ["warehouse|factory|night shift|shift work|employer|paycheck", "Workplace"],
  ["bus stop|\\btransit\\b|\\bbus\\b", "Bus Stop"],
  ["laundromat|laundry|\\bwash\\b", "Laundromat"],
  ["records|file|flyer|reading|written|case against you|packet|redact", "Records Desk"],
  ["mail|letter|envelope|notice", "Mail Room"],
  ["interview|questions|supervisor|service plan|review|check-in|lawyer|attorney|counsel|decision|plan|form", "Agency Office"],
  ["apartment|building|street|porch|outside", "Apartment Exterior"],
  ["evening|morning|kitchen|table|home|gap", "Kitchen"]
];
```

(In the JS source the word-boundary escapes appear as `\\b` inside the string literals, exactly as written above; `new RegExp(...)` in `plateFor()` then compiles them to `\b`. Do not "simplify" them to single backslashes — in a JS string `"\b"` is a backspace character and the rule silently breaks.)

### 1.2 What changed, in order, and why

Relative order of all ten v1 rules is **preserved**. Seven rules are inserted:

| New # | Rule | Inserted | Constraint it satisfies |
|---|---|---|---|
| 2 | Waiting Room | After Hospital, before everything else that could claim it | Must beat Agency Office (v1 #8: `interview|questions|supervisor|…|form`) and Visit Room — a waiting-room scene *is* in the agency building / attached to a visit, so any later position loses. Hospital stays #1: a hospital waiting room is a hospital scene first. |
| 3 | Courthouse Steps | Immediately before Courtroom | Must beat generic Courtroom (`court|hearing|judge`) — but **only** for outside/after-court titles; see the keyword rationale in §1.4. Also beats Doorway and Apartment Exterior (`outside`) for the same titles. |
| 7 | Program | Immediately before School Office and School | Must beat School's bare `class`: a *Parenting Class* title contains `class`, so Program has to be tested first. The trigger words are `parenting|program|support group` — **not** `class` itself (§1.4). |
| 8 | School Office | Immediately before School | Must beat generic School (`school|teacher|classroom|class`): every School Office title also contains `school`. Only a specific-office trigger outranking the generic rule achieves that. |
| 10 | Workplace | After School, before Records Desk / Mail Room / Agency Office / Kitchen | Must beat Agency Office's `interview|questions|…|plan|form` (a *job interview*, an *employer* call, a *paycheck* problem are workplace scenes, not agency scenes) and Kitchen's `home|table` (a *night shift* title that also mentions home is still a work scene). It sits after School so a school-employer / school-work-program title keeps its school plate — the school is the place, the employer is the topic. |
| 11 | Bus Stop | After Workplace, before Laundromat / Records / Mail / Agency / Apartment Exterior / Kitchen | Must beat Apartment Exterior's `street|outside` and Kitchen's `home` — *The Bus Home* is a bus scene whose destination is home, not a kitchen scene. After School deliberately: *school bus* titles plate as School (the destination/institution is the place; see §1.4). |
| 12 | Laundromat | After Bus Stop, before Records / Mail / Agency / Kitchen | Must beat Kitchen's `home|table|gap` — laundry done at home is a kitchen/home scene, laundry done *out* is this plate, and the trigger words (`laundromat|laundry`) are what mark it as out. No other v1 rule plausibly claims these titles, so it takes the last of the new slots. |

Fallback is unchanged: **Kitchen**.

### 1.3 PLATE_IDS additions

```js
"Waiting Room": "plate-waiting", "Courthouse Steps": "plate-courtsteps",
"School Office": "plate-schooloffice", "Workplace": "plate-workplace",
"Bus Stop": "plate-busstop", "Laundromat": "plate-laundromat",
"Program": "plate-program"
```

The `aria-label` in `plateHTML()` is derived from the plate name (`"Scene: " + plateName.toLowerCase()`), so the new plates label themselves correctly with no further change — except when a variant overlay applies (§2.3).

### 1.4 Keyword-by-keyword false-positive justification

Every pattern below was run against the **actual kicker+title text of all 1,048 nodes** in `scenario-1.json` … `scenario-36.json` (the same concatenated, lowercased string `plateFor()` tests). Counts cited are from that audit.

**Waiting Room — `waiting room|lobby`.**
Deliberately **not** bare `waiting`. Five existing titles use *waiting* metaphorically and must stay where they are: *Still Waiting on a Number* (S10), *Waiting for Thursday* (S21), *The Waiting List Behind the Therapist* (S22), *What Waiting Looks Like From Milo's Chair* (S27), *The Waiting Weeks* (S32). The literal phrase `waiting room` matches exactly the two titles that are in one (S19, S29 — §4.1). `lobby` matches zero existing titles and is the other word a real lobby scene would actually use.

**Courthouse Steps — `courthouse steps|courthouse|on the steps|outside court|leaving court|after court`.**
Deliberately **not** bare `steps`, and this is the single most dangerous word in the v2 rule set: S1's *She Steps Outside to Call Her Supervisor* uses *steps* as a **verb**, and bare `steps` would steal the best-audited node in Scenario 1 from Agency Office. The other bare-`steps` titles are just as wrong for this plate: *Ending — The Existing Plan Stands; the Next Steps Are Written* (S18), *Porch, Steps, Walk* (S20 — a porch, i.e. Doorway/Exterior), *Step-Down, Dated* (S23). So the rule requires a court-context phrase: `courthouse` (the building, named), `on the steps` (the noun phrase, which the S1 verb construction *"steps outside"* does not contain — word order is the guard), `outside court`, `leaving court`, `after court`. Result on the current library: **zero** existing titles match — this plate is purely additive, for future/retitled nodes, and cannot disturb the v1 audit. Note the side effect to accept: a title containing bare `courthouse` and nothing else court-like would previously have fallen to Courtroom via `court`; now it goes to the exterior — that is the intent (naming the building = being at the building).

**Program — `parenting|program|support group`.**
Deliberately **not** `class`. Bare `class` is School's word and the only existing `class` title, *Track A, Night Class* (S33), is a class in the school sense — it must stay School, and with this pattern it does. A parenting class is caught by `parenting` before School is ever tested, which is the whole point of the ordering. `program` matches one existing title (§4.1, flagged). `support group` matches zero existing titles; both are the words a program-room scene is actually titled with.

**School Office — `school office|principal|guidance office|school counselor`.**
All four triggers name the office or its staff, not the building: `school office` (the room), `principal` (the person you sit across from in it), `guidance office` / `school counselor` (the same room under its other name). Deliberately **not** bare `counselor` (a therapist/counselor title elsewhere in these stories is a clinical scene, not a school office) and not bare `office` (that is Agency Office's whole territory). Matches **zero** existing titles — purely additive.

**Workplace — `warehouse|factory|night shift|shift work|employer|paycheck`.** Never bare `work`: the one existing `work` title, *Two Courts, One Work Schedule* (S24), is a court/scheduling node and correctly stays Courtroom — bare `work` at this position would have stolen it. Keyword by keyword:
- `warehouse`, `factory` — name the workplace itself; no non-workplace sense exists in this corpus. Zero existing matches.
- `night shift`, `shift work` — the two-word phrases only. Bare `shift` and bare `night` are both unsafe (`night` appears in 17 existing titles, §2.4). The phrases match zero existing titles.
- `employer` — the institution, not the activity; a title naming the employer is about the job relationship. Zero existing matches. (Contrast `interview`: left in Agency Office, because in this corpus interviews are overwhelmingly agency interviews; a *job interview* title that also says `employer` is caught here first, which is correct.)
- `paycheck` — names the artefact of work, like `envelope` names mail. It cannot occur in a non-work sense. Zero existing matches.

**Bus Stop — `bus stop|\btransit\b|\bbus\b`.** Both content words are boundary-guarded, for two different attested traps:
- `\bbus\b` **cannot match *business***: in *Portals, Fax Numbers, Business Days* (S25) there is no word boundary after `bus` inside `business`, so the rule does not fire and the node keeps its v1 plate. An unguarded `bus` would have stolen it. The guarded form still catches all five genuine bus titles (§4.1), including *The Bus-Fare Ledger* — see the caution in §4.2.
- `\btransit\b` **cannot match *transition***: this trap is attested, not hypothetical — *The Transition That Depends on a Tap* (S17) is a placement-transition node, and an unguarded `transit` (the spelling first proposed for this rule) **does** match it. The trailing `\b` kills the match because `transition` continues with `ion`. Only the standalone word *transit* (a transit pass, a transit office) fires the rule. Zero existing titles match the guarded form on its own; all bus re-plates come through `\bbus\b` / `bus stop`.

**Laundromat — `laundromat|laundry|\bwash\b`.**
`laundromat` is unambiguous. `laundry` names the task/place and matches zero existing titles. `wash` is included only as `\bwash\b` (the standalone verb/noun — *Wash Day*, *…to Wash*): unguarded, it would also be the most likely future false positive in this set (it is a substring risk in compounds), and the boundary costs nothing. Matches **zero** existing titles — purely additive.

### 1.5 Casting available to future authoring (no code change)

`plateFor()` selects plates only; figures inside a plate are fixed in the symbol. The v2 cast (`fig-caseworker2`, `fig-mother2`, `fig-kin`, `fig-supervisor`, `fig-toddler`, `fig-child2`) is therefore available to **future plates and future plate revisions**, not to data. Two v2 figures debut inside v2 plates: `fig-supervisor` (plate-waiting, behind the counter), `fig-mother2` (plate-workplace), `fig-kin` (plate-program). `fig-caseworker2`, `fig-toddler`, and `fig-child2` are cast-only in v2 — they ship so the next plate revision doesn't need a design round. Do not invent figure-swapping logic; that is not in this contract.

---

## 2. VARIANT rules — time / weather overlays

### 2.1 Contract

- An overlay is a `<symbol>` (`ov-dawn`, `ov-dusk`, `ov-night`, `ov-rain`, viewBox `0 0 400 225`) instanced **after** the plate `<use>`, **inside the same `<svg>`**, in the same `.plate` div. It is never a second `.plate`, never applied to the cover, never applied to text or any element outside the plate SVG.
- **At most one overlay per node.** First match in the evaluation order in §2.2 wins; do not stack (e.g. night + rain may both be true of a title — rain wins, because weather is the more specific visual fact and its wash is the lighter one).
- Overlays are decorative tint, selected from the same kicker+title string as the plate. They carry no information: nothing in the story, the HUD, THE CLOCK, or the assessment panel may depend on them.

### 2.2 VARIANT_RULES — implement exactly this

```js
const EXTERIOR_PLATES = ["Apartment Exterior", "Courthouse Steps", "Bus Stop", "School", "Doorway"];
const VARIANT_RULES = [
  /* [regex, overlayId, exteriorOnly] — first match wins, one overlay max */
  ["\\brain\\b|storm|downpour", "ov-rain", true],
  ["midnight", "ov-night", false],
  ["\\bnight\\b|tonight|overnight", "ov-night", true],
  ["dusk|sunset|twilight", "ov-dusk", false],
  ["evening", "ov-dusk", true],
  ["dawn|sunrise|first light|daybreak|early morning", "ov-dawn", false]
];
function variantFor(node, plateName) {
  const text = ((node.kicker || '') + ' ' + (node.title || '')).toLowerCase();
  for (let i = 0; i < VARIANT_RULES.length; i++) {
    if (new RegExp(VARIANT_RULES[i][0]).test(text) &&
        (!VARIANT_RULES[i][2] || EXTERIOR_PLATES.indexOf(plateName) !== -1)) {
      return VARIANT_RULES[i][1];
    }
  }
  return null;
}
```

And in `plateHTML(plateName)` — which needs the node, so change its signature to `plateHTML(plateName, node)` and update both call sites in `storyPanelHTML()`'s callers (`renderNode`, `renderEnding` pass the node through):

```js
function plateHTML(plateName, node) {
  const v = node ? variantFor(node, plateName) : null;
  return '<div class="plate" role="img" aria-label="Scene: ' + esc(plateName.toLowerCase()) +
    (v ? ', ' + v.replace('ov-', '') : '') + '">' +
    '<svg viewBox="0 0 400 225" preserveAspectRatio="xMidYMid slice" aria-hidden="true">' +
    '<use href="#' + PLATE_IDS[plateName] + '"/>' +
    (v ? '<use href="#' + v + '"/>' : '') + '</svg></div>';
}
```

The `aria-label` suffix (`, rain` / `, night` / …) is required, not cosmetic: §9/§10 of the bible hold that a plate is available to a screen reader, and a weather/time tint that changes the scene's reading should be named there. It is still never the sole carrier of plot.

### 2.3 Trigger rationale, per overlay

| Overlay | Triggers | Scope | Why |
|---|---|---|---|
| `ov-rain` | `\brain\b`, `storm`, `downpour` | **Exterior-family plates only** (§2.4) | Rain is an outdoor fact. Inside an office or kitchen plate it is a lie about the room. `\brain\b` is boundary-guarded so compounds/figurative uses don't fire it. |
| `ov-night` | `midnight` (any plate); `\bnight\b`, `tonight`, `overnight` (exterior only) | Split | `midnight` is an hour, unambiguous anywhere. *Night* in these titles is usually a **relative** word — *The Night Before…* is an evening at a lit kitchen table, not a night exterior — so the general words are gated to exteriors, where night is a property of the scene. See the audit in §2.5: this gate is what keeps 17 existing interior nodes un-darkened. |
| `ov-dusk` | `dusk`, `sunset`, `twilight` (any plate); `evening` (exterior only) | Split | The three explicit words name the light itself. `evening` names a time of day that, indoors, still looks like the warm plate — same reasoning as night. |
| `ov-dawn` | `dawn`, `sunrise`, `first light`, `daybreak`, `early morning` | Any plate | Dawn is a light event, and a warm glow low-left reads correctly through a window in an interior plate too. Deliberately **not** bare `morning`: 8 existing titles use *morning* as an ordinary daytime marker (*Visit Morning*, *Wednesday Morning, in Writing*, *The Morning They Came*…) and dawn-glow on all of them would make the overlay mean "morning," not "dawn." Only `early morning` — the phrase that actually claims the low light — fires it. |

Evaluation order (rain → night → dusk → dawn) matters in exactly one realistic case: a rainy night exterior. Rain wins (§2.1).

### 2.4 The exterior family (rain / gated night / gated dusk)

Exactly these five plate names, as listed in `EXTERIOR_PLATES` above:

**Apartment Exterior · Courthouse Steps · Bus Stop · School · Doorway**

School and Doorway are in the family on purpose: both v1 plates are *exteriors of* their buildings (facade + steps; door from outside), so weather and night are properties of what the plate shows. Kitchen, Agency Office, Waiting Room, Courtroom, Visit Room, Hospital, Records Desk, Mail Room, School Office, Workplace, Laundromat, and Program are interiors and are excluded — Workplace and Bus Stop are the instructive pair: the warehouse plate is an interior (racking, window *band*), the bus-stop plate is a street.

### 2.5 Variant impact on the existing library (audited)

Applying §2.2 to all 1,048 existing nodes changes the rendering of **exactly one** node:

- Dawn: 0 titles match. Dusk explicit: 0. Rain: 0. `midnight`: 0 titles.
- `evening` matches 5 titles (S1 *Paper Instead of Goodbye*, S5 *A Quiet Evening*, S25, S28, S29) — all plate as Kitchen (interior), so the gate blocks the overlay on all 5.
- `night`/`tonight`/`overnight` match 17 titles — 16 plate as interiors (Kitchen, Agency Office, Records Desk, Courtroom) and are blocked by the gate. The one exception is *Track A, Night Class* (S33): School **is** in the exterior family and its text contains `\bnight\b`, so it **does** acquire `ov-night`. That is the single existing-node change, and QA should expect precisely that one (§4.3). Semantically it is defensible (the plate is a school facade/exterior; a night class happens at night), and it is listed here so it is a decision, not a surprise.

If QA's count differs from {S33 night} ∪ ∅, the implementation — not this table — is wrong.

---

## 3. CSS / typography changes (UI Designer)

All values are in the v1 token system. No new colors, no new fonts, no new assets. Apply as a block; each item is independent and numbered for review.

**C1 — Scene-header grouping (kicker tab + display title).** In `storyPanelHTML()` the emitted order is already plate → kicker tab → `<h2>` → caption box; what is missing is that the tab and title read as one header unit, visually attached to the plate above and the caption box below. No DOM change:

```css
.plate{margin:0 0 10px;}              /* was 16px: header now sits closer to its plate */
.kicker.tab{margin:0 0 7px;}          /* tab hugs the title below it */
```

**C2 — Display title sizing.** Story titles are panel titles; at v1's generic `h2` size they compete with screen-level headings. Scope the larger treatment to the app (start-screen and decoy headings are unaffected — the decoy's `h2` is outside `#app`):

```css
#app h2{font-size:1.65rem;line-height:1.18;letter-spacing:-.01em;margin:0 0 10px;}
```
(This replaces the generic `h2` rule **for `#app` only**; keep the generic rule for the decoy.)

**C3 — Caption-box leading.** Narration is the longest reading on the page; it gets air, not size:

```css
.captionbox{line-height:1.62;padding:16px 18px 8px;}   /* was line-height inherit (1.55), padding 14px 16px 6px */
.captionbox p{margin:0 0 11px;}                        /* was 10px */
```

**C4 — Case-file tab upgrade (typographic only).** The `CASE FILE` tab gets letterspacing and size, nothing else — no icon, no folder clip, no new shape, no color change:

```css
.panel{margin:30px 0 16px;}                            /* was 26px: room for the taller tab */
.panel::before{font-size:.78rem;letter-spacing:.22em;padding:4px 14px 3px;top:-27px;}
/* was .72rem / .16em / 2px 12px / -25px */
```

**C5 — Scene transition (the v2 motion spec).** One transition, on scene change only, and it exists **only** under `no-preference` — under `prefers-reduced-motion: reduce` there is no transition at all, which is why this block must live in its own media query and not in the existing `reduce` block:

```css
@media (prefers-reduced-motion: no-preference){
  .plate, .captionbox{animation:sceneIn .28s ease-out;}
  @keyframes sceneIn{from{opacity:0;transform:translateY(8px);}to{opacity:1;transform:none;}}
}
```
Targeted at `.plate` + `.captionbox` only, deliberately: animating all of `#app` would make the HUD re-fade on every node and would fight THE CLOCK's "appears and stays" rule and the RATED stamp's own animation. Fade + 8px rise, ~280 ms, ease-out, once, no loop, no delay.

**C6 — Plate frame treatment.** Border and shadow are v1 law (4px ink, 8px hard offset) and do not change. The one change is the matting color behind the SVG, so any `slice`-crop edge reads as ink matting rather than as more sky:

```css
.plate{background:var(--ink);}        /* was var(--navy) */
```

**C7 — Overlay plumbing.** No CSS. Overlays are SVG-internal (§2.2); do not add classes, filters, or opacity wrappers for them. If a variant looks too strong, the fix is in the kit's opacities, not in CSS.

**C8 — Explicit non-changes.** THE CLOCK, the RATED stamp, the Quick Exit button, the Watch Mode bar, choice rows, and the HUD are **unchanged** by v2. Any diff touching them is out of scope.

**Contrast statement.** This section introduces **no new text/background pairing**. The pairings relied on are exactly the v1 measured ones (visual-bible §3): story title and body text are ink on the paper page field (**13.34:1, AAA**) and ink on cream in caption boxes (**15.40:1, AAA**); the kicker tab is ink on amber, a v1 pairing whose colors C1/C4 do not alter (type size/spacing only); HUD and watch-bar text remain cream on navy (**12.51:1, AAA**). Text never sits on a plate or an overlay, in v1 or v2 — plates are `role="img"` establishing shots above the header — so overlay opacity choices carry no contrast obligation, only a dignity one (§5).

---

## 4. v1 → v2 plate-assignment caution list (for QA)

### 4.1 The complete audited diff: exactly 8 of 1,048 nodes re-plate

Computed by running v1 rules and §1.1 rules over the kicker+title of every node in all 36 scenario JSONs. **This is the whole diff.** Anything else changing is a bug.

| # | Node | v1 plate | v2 plate | Verdict |
|---|---|---|---|---|
| 1 | S5 — *The Bus That Doesn't Come* | Kitchen (fallback) | **Bus Stop** | ✅ Intended win |
| 2 | S7 — *A Morning the Bus Fails* | Kitchen (via `morning`) | **Bus Stop** | ✅ Intended win — was the clearest v1 miss in the set |
| 3 | S8 — *The Bus Home* | Kitchen (via `home`) | **Bus Stop** | ✅ Intended win |
| 4 | S32 — *The Bus Home* | Kitchen (via `home`) | **Bus Stop** | ✅ Intended win |
| 5 | S19 — *The Other Waiting Room* | Kitchen (fallback) | **Waiting Room** | ✅ Intended win |
| 6 | S29 — *Visitation, in a Waiting Room* | Kitchen (fallback) | **Waiting Room** | ✅ Intended win — note it is *not* Visit Room in either version (`visitation` matches neither `the visit` nor `visit room`); QA should eyeball this one scene in context, as a waiting room attached to a visit is precisely the new plate's subject |
| 7 | S19 — *The Bus-Fare Ledger* | Kitchen (fallback) | **Bus Stop** | ⚠️ **Questionable — flagged, not hidden.** A *ledger* is a document; the scene is a mother doing fare arithmetic, most plausibly at home. The rule cannot tell a fare ledger from a bus ride, and no honest regex on title text can. Accepted for v2 because the other four bus titles are clear wins and the plate (a stop, a bench, no figures) does not misdepict the scene's stakes — but if a human reviewer reads the node and disagrees, the correct fix is a retitle of the node, **not** a narrower bus rule. |
| 8 | S23 — *Paper From the Program* | Kitchen (fallback) | **Program** | ⚠️ **Questionable — flagged, not hidden.** *Paper from* a program is a document beat (its neighbours in S23 are records/file nodes); the Program plate shows the room, not the paper. Accepted for the same reason as #7 — a program room is a true fact about where the paper came from, and the alternative (suppressing `program` until a purer title appears) would leave the plate unreachable. Eyeball in context during QA. |

Plus the one overlay change from §2.5: **S33 — *Track A, Night Class*** keeps its School plate and gains `ov-night`.

**Zero** existing nodes move to Courthouse Steps, School Office, Workplace, or Laundromat. Those four plates are unreachable by the current library's titles; they exist for the locations the library is growing into (the expansion path the bible already names) and for retitles. A QA run that shows them firing on current data has found an implementation bug.

### 4.2 Near-misses that must NOT change (regression traps)

Each of these was one careless regex away from re-plating. QA should assert each explicitly:

| Node | Trap | Must stay |
|---|---|---|
| S1 — *She Steps Outside to Call Her Supervisor* | bare `steps` in Courthouse Steps | **Agency Office** |
| S17 — *The Transition That Depends on a Tap* | unguarded `transit` in Bus Stop | **Kitchen** (v1 fallback — no v1 rule matches it) |
| S25 — *Portals, Fax Numbers, Business Days* | unguarded `bus` in *business* | **Kitchen** (v1 fallback — no v1 rule matches it) |
| S24 — *Two Courts, One Work Schedule* | bare `work` in Workplace | **Courtroom** |
| S33 — *Track A, Night Class* | `class` claimed by Program | **School** plate (+ `ov-night`, §2.5) |
| S10 *Still Waiting on a Number* · S21 *Waiting for Thursday* · S22 *The Waiting List Behind the Therapist* · S27 *What Waiting Looks Like From Milo's Chair* · S32 *The Waiting Weeks* | bare `waiting` in Waiting Room | Each its v1 plate |
| S18 *…the Next Steps Are Written* · S20 *Porch, Steps, Walk* · S23 *Step-Down, Dated* | bare `steps` | Each its v1 plate |
| The 17 *night/tonight* interior titles (§2.5) | ungated `ov-night` | No overlay (interior plates) |
| The 5 *evening* titles (§2.5) | ungated `ov-dusk` | No overlay (all Kitchen) |

### 4.3 QA protocol (developer)

1. Extract kicker+title for all nodes from `scenario-*.json` (1,048 nodes at spec date; the three scenario-title pseudo-entries in each file are not nodes).
2. Diff `plateFor()` before/after §1.1. Expected: **exactly the 8 rows of §4.1**, no more, no fewer.
3. Diff `variantFor()` over the same set. Expected: **exactly 1 hit** — S33 *Track A, Night Class* → `ov-night`.
4. Assert the §4.2 table.
5. Load Scenario 1 end-to-end and confirm its v1 audit still holds word for word (bible §6.1): 26 of 27 as intended, *Not Yet* still falling back to Kitchen, *She Steps Outside…* still Agency Office.
6. Confirm each new symbol renders standalone (paste each `<use>` into a test plate), and that every v2 plate's last element is the halftone rect (see §5).

---

## 5. Brand Guardian check — executed on `v2-kit.html` as delivered

Checked by the Brand Guardian role against the Red Law and the bible's hard rules (§2, §3, §5, §6.2). Method: full read of the kit + scripted greps/parses (file is well-formed XML when wrapped in a `<defs>`; parsed symbol-by-symbol).

| Check | Result |
|---|---|
| **Red Law** — the restricted color appears only in THE CLOCK box and the RATED stamp | ✅ **PASS.** The kit contains the restricted hex **zero** times and the color word zero times (grep-verified). Neither element lives in a defs kit at all — both are CSS in the build, untouched by v2. The wall clock in plate-waiting and the time-clock in plate-workplace are ink/cream, explicitly not the restricted color. |
| **At most 2 figures per plate** | ✅ **PASS.** Parsed `<use>` counts: waiting **2** (supervisor, mother), courtsteps **2** (mother, attorney), schooloffice **2** (mother, child), workplace **1** (mother2), busstop **0**, laundromat **1** (mother), program **2** (kin, mother). |
| **No faces** | ✅ **PASS.** Every v2 figure is the v1 grammar — a plain head circle with a hair distinction, no eyes/mouth/features. The one apparent exception is specified in the task itself and follows v1 precedent: `fig-kin`'s glasses are two paper-stroke circles + bridge *as a silhouette distinction*, exactly as `fig-doctor`'s stethoscope is a paper-stroke distinction in v1; they draw an object worn, not a face. |
| **No text inside art** | ✅ **PASS.** Zero `<text>` elements (grep-verified). The nameplate (schooloffice), the bus sign (busstop), the flip-chart (program), the clock dials (waiting, workplace), and the ticket window (waiting) are all deliberately **blank** blocks/circles. |
| **No child in a distress composition** | ✅ **PASS.** Children appear in exactly one v2 plate: `fig-child` in plate-schooloffice, standing plainly beside the mother at a desk — an ordinary administrative scene, no removal/argument/injury content, per bible §6.2 ("a plate never depicts… any child's distress"). `fig-toddler` and `fig-child2` are placed in **no** plate. The child option for plate-laundromat was **declined** by this team (counter + washer row is the subject; the plate stays uncrowded) — recorded here so the omission reads as a decision. |
| **One prop per figure, in paper** | ✅ **PASS**, with the v1-precise reading: exactly one *held/carried* prop per figure, in paper with ink stroke — caseworker2: shoulder bag; mother2: tote bag; kin: framed photo; supervisor: coffee cup; toddler: stuffed toy; child2: book. Paper used for *clothing* distinctions (kin's cardigan V and glasses, supervisor's lapels) follows shipped v1 precedent (attorney's paper tie, doctor's paper coat) and is not a second prop. |
| **Silhouette distinctness** (hair + posture + prop all differ) | ✅ **PASS.** caseworker2 = bob + narrow body + shoulder bag (vs caseworker's hair-back + clipboard); mother2 = long hair mass + wider line + tote (vs mother's bun + envelope); kin = glasses + cardigan V + framed photo; supervisor = flat hair + wide blazer/lapels + cup; toddler = ~102-unit internal height, larger head proportion (vs child ~147, adults ~200+); child2 = ~191 units, slim, book at chest (vs child ~147, backpack). |
| **Halftone law** — every plate ends with the `#ht` overlay rect | ✅ **PASS.** All 7 plates end with `<rect width="400" height="225" fill="url(#ht)" …/>` at the v1 opacity for their temperature (.15 cold, .13 warm). Overlays are exempt by construction (they *are* overlays); `ov-dusk` re-uses `#ht` at .18, as specified. |
| **Zero assets / no webfonts / no URLs** | ✅ **PASS.** The kit is inline SVG only; no `<image>`, no `href` to anything but `#fig-…`/`url(#…)`, no external reference of any kind. |
| **Temperature honesty** | ✅ **PASS.** Waiting/Workplace/Bus Stop/Court Steps are `gradCold`; Laundromat/Program are `gradWarm`; School Office is mixed as briefed (warm room, cold cabinets). Court Steps and Bus Stop each carry exactly **one** warm accent (lit doorway; streetlamp glow) per the threshold-space rule in bible §2. |

**Guardian verdict: the kit is cleared for integration as delivered.** Two judgement calls were made *inside* the rules rather than around them, and both are recorded above so they can be overruled knowingly: (1) the laundromat child was omitted; (2) `fig-kin`'s glasses are treated as a worn-object distinction under the doctor precedent, not as a face.

---

## 6. Inventory delivered in `v2-kit.html`

- **Gradients/patterns (2):** `gradDawn` (radial, for `ov-dawn`), `rain` (pattern, for `ov-rain`).
- **Figures (6):** `fig-caseworker2`, `fig-mother2`, `fig-kin`, `fig-supervisor`, `fig-toddler`, `fig-child2`.
- **Plates (7):** `plate-waiting`, `plate-courtsteps`, `plate-schooloffice`, `plate-workplace`, `plate-busstop`, `plate-laundromat`, `plate-program`.
- **Overlays (4):** `ov-dawn`, `ov-dusk`, `ov-night`, `ov-rain`.
- **Total:** 19 new ids, 20,310 bytes, zero collisions with v1.
