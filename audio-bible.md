# The First 90 Days — Audio Bible

**Project:** *The First 90 Days* (Tactic Watch simulation), Scenario 1 comic edition (`play-comic.html`)
**Status:** Draft — design document. v1 ships synthesized cues only: **no score, no voice acting, no audio files.**
**Companion file:** `audio-cues.js` implements §2 and §5 exactly. The visual team fires only the seven contracted cues; everything beyond them is spec'd for v1.1.

---

## 1. Sound identity — documentary restraint

This is a story about a family moving through a bureaucracy. It should sound like one.

**The system sounds bureaucratic.** Paper sliding across a desk. A rubber stamp coming down. A door closing on a hallway. A phone buzzing face-down on a kitchen table. The faint, flat room tone of fluorescent light. Nothing in the agency's world is musical, and nothing in it is loud — its power is procedural, and the sound design keeps it that way.

**Warmth exists only in family spaces.** The home is the only place the sound palette allows anything resembling music: a single piano note, a kettle, a kid's shoes by the door (v1.1 ambience, §3). When the story is at home, the air is different. When the story is at the agency or the courthouse, the air is paper and HVAC. The player should be able to tell where they are with their eyes closed — and dread the change in the air.

**Comic-book sound, translated honestly.** A graphic novel does not shout POW and BAM for a story like this. Its sound lives in the quiet panels: the knock on the door that takes a whole page, the stamp that ends a scene, the gutter of silence between one day and the next. This game's cues are those panels, sounded:

- The **knock** is a panel, not an effect — the moment everything changes, drawn large and heard plainly.
- The **stamp** is the game's signature sound, the way a recurring visual motif would be: bureaucratic finality, ink on a form, a decision becoming a record.
- The **page turn** is the gutter between days — time passing in a case is the story's real antagonist, and it sounds like paper.
- **Silence** is a designed element, not an absence (§3). Hearing scenes play against nothing.

**Hard rules of the identity:**

1. **Nothing startles.** No cue is a jump scare, an alarm, or a sting. The knock is firm, never frightening. A parent who has lived this does not need the game to ambush her, and a trainee does not learn from being ambushed.
2. **Dread without harassment.** The deadline gets exactly one tick, once (§2, `tick`). There is no countdown loop, no accelerating pulse, no clock that follows the player. The law's pressure is constant; the game's sound refuses to nag.
3. **Sound never carries information alone.** Every cue is paired with a visual event already in the design — a panel change, a banner, a reveal. A player with sound off (the default) misses atmosphere, never facts.
4. **Sound is OFF by default.** The player turns it on, deliberately, with a visible toggle. Its state persists (§5).
5. **The child is never a sound effect.** No crying, no child's voice, no door slammed "for drama." The children's presence is visual and textual. This rule survives every future version, including the voiced edition (§4).

---

## 2. Cue sheet (v1 contract)

All cues are synthesized in `audio-cues.js` with the WebAudio API — oscillators and filtered noise only. No samples, no files, no network. Durations are total audible length. Loudness ceilings are peak gain at the cue's own gain stage, under a master gain of 0.6 through a soft compressor; on a phone speaker at full volume, no cue should make a player flinch or reach for the volume button.

| Cue | Story meaning | Fires when | Synthesis | Duration | Peak ceiling |
|---|---|---|---|---|---|
| `knock` | The caseworker is at the door. The case begins in person, not on paper. | The door scene — once, as the knock panel lands | Two thumps, ~180 ms apart. Each: sine dropping 115→68 Hz in 90 ms + a knuckle-contact noise burst (lowpass 420 Hz, 40 ms). Low, wooden, unhurried. | ~0.45 s | 0.34 |
| `stamp` | **The signature sound.** A decision becomes a record: final, filed, hard to undo. | A form is signed, a plan is entered, a removal is documented, an outcome is recorded — the moments paper changes the family's legal reality | Three layers: contact noise burst (lowpass 700 Hz, 50 ms) + body thump (sine 92→54 Hz, 110 ms) + the form sliding away (bandpass noise sweeping 1250→580 Hz, 220 ms, quiet). | ~0.38 s | 0.46 |
| `page` | A day passes. The gutter between panels; the case's clock moving whether anyone is ready or not. | Panel/day transitions — new dayOffset, scene changes | Paper, not a book: one noise pass through a bandpass filter sweeping 380→2400→760 Hz with a smooth in/out envelope — lift, turn, settle. | ~0.42 s | 0.16 |
| `tick` | The 72-hour deadline exists. Once you have heard it, you know the clock is real; the game will not remind you again. | Exactly once, when the shelter-care deadline banner first appears | A single clock tick: 25 ms of highpass-filtered noise (3 kHz) + a faint 1750 Hz ping decaying in 35 ms. Small, dry, over. | ~0.07 s | 0.13 |
| `unlock` | Paper the parent was not allowed to see is now in her hands. The record opens. | The records-request payoff — the hidden assessment items are revealed (§ 3130.44(d) beat) | Latch click (square blip, 1150 Hz, 30 ms) → paper unfolding (low bandpass noise swell, 300 ms) → one quiet sine at 659 Hz decaying under it, the closest thing to warmth the agency scenes allow. | ~0.52 s | 0.20 |
| `chord_warm` | Home. The ending the law is supposed to make possible. | Endings where the children are home (safety-plan and return endings) | Piano-like triad C4–E4–G4 (261.6 / 329.6 / 392.0 Hz), triangle waves through a 1250 Hz lowpass, slow 45 ms attack, ~1 s natural decay. Single notes, room around them — the home motif of §3 in miniature. | ~1.1 s | 0.30 (sum) |
| `chord_flat` | The case continues. Nothing resolved; the file stays open and so does the family's uncertainty. | Endings where placement continues past the first review | The same instrument, unresolved: A3–C4–E♭4 (220 / 261.6 / 311.1 Hz) through a duller 820 Hz lowpass, slower attack, decays without a final note. Not sinister — flat. Paper, still. | ~1.05 s | 0.24 (sum) |

### Spec'd for v1.1 (not fired by the visual team in v1)

| Cue | Story meaning | Would fire when | Synthesis | Duration | Peak ceiling |
|---|---|---|---|---|---|
| `door_close` | Leaving — a visit ends, an office door shuts behind her, the worker leaves the home. The system's doors close softly and completely. | Visit/office/home-visit scene exits | Lowpassed noise settling 780→190 Hz (180 ms) + one low thump (82 Hz) + a small latch click at the end. Never a slam. | ~0.32 s | 0.26 |
| `phone` | The case reaches into the home. A call from the worker, a missed call, a voicemail arriving during a shift. | Phone-call and missed-call panels | A phone buzzing on a table — not a ringtone: two muted pulses of lowpassed 118 Hz sawtooth with a faint body rattle, 90 ms each. Familiar, domestic, ignorable only if you're not waiting for it. | ~0.52 s | 0.13 |

**Why one tick and never a loop.** A looping countdown would make the deadline feel like a bomb, and a shelter-care deadline is not a bomb — it is a court date the system set and the parent cannot move. One tick says *the clock is running*; silence afterward says *and it does not care whether you are listening*. That is the truer sound, and the kinder one: the game models pressure without reproducing the harassment of living under it.

**Why the stamp is the signature.** Every other cue belongs to a place (door, page, phone). The stamp belongs to the system itself. It is the sound of a judgment becoming paperwork — the exact transformation this project exists to make visible. It should be satisfying to hear and slightly chilling for the same reason: it is so *final*, and so easy.

---

## 3. Music direction — design only (v1 ships no score)

**Stated plainly: version 1 has no music.** The cues above are the entire soundtrack. This section is the design for a future produced edition, so that if music is ever commissioned it is commissioned to this brief and not invented against it.

Three motifs, one instrument family, more silence than sound:

- **Home — solo piano, single notes, room tone.** Not melodies: notes, with the room audible around them — the small natural decay of a real space. Warmth in this score is *space*, not sweetness. The `chord_warm` cue is its seed. If a theme emerges, it emerges the way a house sounds familiar, not the way a film tells you to feel.
- **Agency / court — low cello, long tones.** Bowed, slow, at the edge of pitch — more air than note. Long tones under dialogue-free panels only; the moment people speak (text appears), the cello withdraws. Its job is the feeling of a building that is not hostile and not kind: refrigerated, procedural, patient.
- **Endings — the same piano, resolved or unresolved.** Endings do not get new music; they get the home piano answering the question the case asked. Home endings resolve (the `chord_warm` triad, extended). Continuing endings leave the phrase unfinished — the `chord_flat` color, a melody that stops being written. The audience should hear that the difference between the two families' futures is a few notes, and that the notes were decided by paperwork.

**Silence as a designed element.** Hearing scenes are scored with *nothing* — no motif, no room tone, not even the fluorescent hum. In a hearing, the only sounds are procedural: a page, a stamp. The design treats silence the way the comic treats a panel with no caption: it is where the weight is. Any future mix that fills hearing scenes with underscore fails this brief.

**Fatigue rule.** Any motif must be able to play a full scenario without repeating identically — variation in voicing and spacing, never a loop the player can learn to hear. If the player notices the music, it has failed (§1, rule 3 applies to score as well: music carries mood, never facts).

---

## 4. Voice direction — design only (v1 has no voice acting)

**Stated plainly: version 1 has no voices. Narration stays text.** Three reasons, in order of importance:

1. **The player's own inner voice is the narrator this story needs.** A parent reading "the worker is at the door" hears it in her own head, in her own kitchen. A performed voice replaces that with someone else's memory. Text keeps the story the player's.
2. **Consent and safety.** These scenarios are composites of real families' worst weeks. Performed voices — especially a caseworker's tone, especially anything like a child — risk turning testimony-textured material into re-enactment. Text keeps the line bright: this is a document, not a dramatization.
3. **Cost and iteration.** The law content changes as verification proceeds; text can be corrected in an afternoon. Recorded voice cannot, and unverified law should never be locked into audio.

**If an organization edition ever commissions voice** (accessibility editions are the legitimate reason — a full audio version for low-literacy or low-vision players is worth doing well):

- **One narrator, neutral.** A single adult narrator reads narration *and* all roles' lines as narration ("The worker said: …"), the way an audiobook reads a deposition. No character voices, no accents-as-characterization, no performed distress.
- **Never voice the children.** Not acted, not synthesized, not "age-appropriate casting." Children's lines are narrated about, never performed. This rule is absolute and is written into any commission.
- **Casting from lived experience, reviewed by lived experience.** Narrator selection and the final listen both go through the project's compensated lived-experience review, with release-blocking authority, as with every other parent-facing element.
- **No voice in hearing scenes that isn't procedural.** If the voiced edition reaches a hearing, the narrator reads the record flatly — the §3 silence rule translates to: no underscoring, no dramatic reading.

---

## 5. Technical rules (implemented in `audio-cues.js`)

1. **WebAudio only. Everything is synthesized.** Oscillators and filtered noise buffers. Zero audio files, zero network requests, zero dependencies. The library must work from `file://` in a single-file build.
2. **Lazy context, gesture-born.** The `AudioContext` is created (or resumed) only inside a user-gesture call path — the Start button, the sound toggle, or a cue fired by a click. Nothing touches audio at page load. `Cue.unlock()` exists so the Start button handler can warm the context silently.
3. **OFF by default, persisted.** Enabled state lives in `localStorage` under the key **`f90d-sound`** (`'1'` = on). Absent key, unreadable storage, or private-mode exceptions all resolve to OFF. `Cue.setEnabled(bool)` writes the key; `Cue.isEnabled()` reads the in-memory state.
4. **Conservative master.** Master gain 0.6 into a `DynamicsCompressor` used as a safety limiter. Per-cue peaks per §2. The mix target is "clearly audible at half phone volume, ignorable at full room distance."
5. **Total no-op safety.** If WebAudio is unavailable (`AudioContext`/`webkitAudioContext` missing), if the context cannot be created, or if sound is disabled, `Cue.play()` returns immediately and silently. Unknown cue names are ignored. No code path in the library may throw into the game — every entry point is guarded, because the game must never break because its sound did.
6. **Suspended-context discipline.** If the context is `suspended` when a cue fires, the library attempts `resume()` (cues fire from click handlers, so this stays inside the gesture rules) and still schedules the cue; if the browser refuses, the cue is simply lost. Sound is atmosphere, never facts (§1, rule 3) — a lost cue is an acceptable failure, a thrown error is not.
7. **Short and bounded.** Every cue is under 1.2 s. One-shot nodes only; nothing loops; nothing sustains. Each cue builds a handful of nodes and lets them stop — no cleanup bookkeeping, no node leaks beyond the cue's own decay.
8. **Prefixed fallback.** Safari's `webkitAudioContext` is honored. Noise is generated once per context into a reusable 1-second buffer.

### Integration (for the parent build step)

```html
<!-- inline the full contents of audio-cues.js in a <script> BEFORE the game script,
     or load it as the first script in <head>. It only defines window.Cue. -->
<script> /* …audio-cues.js contents… */ </script>
```

- The Start button handler should call `Cue.unlock()` (and may then fire `Cue.play('page')`).
- The sound toggle calls `Cue.setEnabled(!Cue.isEnabled())` and renders its label from `Cue.isEnabled()`.
- Call sites fire exactly: `Cue.play('page' | 'stamp' | 'tick' | 'unlock' | 'chord_warm' | 'chord_flat' | 'knock')`.

---

## 6. What a human must listen for (the honest limit of machine QA)

The build harness can prove the library never throws and schedules every cue; it cannot hear. Before v1 ships, a person — ideally on a mid-range Android phone speaker, then on headphones — should confirm:

- `knock` reads as a knock on a wooden door, firm and ordinary — not a heartbeat, not a gunshot, not a horror sting.
- `stamp` reads as *stamp, then paper sliding* — the slide is the detail that sells it; if only the thump is audible at low volume, the slide's gain comes up 2 dB and nothing else changes.
- `page` is paper, not a whoosh or a riser — it should almost disappear into the act of tapping.
- `tick` is barely there, and that is correct. Anyone who calls it "too quiet" should be asked whether they would want it forty more times.
- `unlock` feels like opening, not winning — no chime of triumph; the paper matters more than the note.
- `chord_warm` vs `chord_flat` are distinguishable blind, at half volume, by someone who has not read this document — and neither one sounds like a video game.
- All seven cues in sequence (the full story's sound in under five seconds) feel like one world: a house, an office, a file.

*Document ends. Drafts only — nothing in this bible authorizes recording, licensing, or publishing audio; v1 remains cues-only, text-narrated, and gated like the rest of the prototype.*
