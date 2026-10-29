/* ============================================================================
 * The First 90 Days — audio-cues.js
 * Comic-edition sound library for play-comic.html (Tactic Watch simulation).
 *
 * Implements the contract the game is built against:
 *   Cue.play('page' | 'stamp' | 'tick' | 'unlock' |
 *            'chord_warm' | 'chord_flat' | 'knock')   (+ 'door_close', 'phone'
 *                                                      spec'd for v1.1)
 *   Cue.setEnabled(bool)   — persists to localStorage key 'f90d-sound'
 *   Cue.isEnabled()        — sound is OFF by default
 *   Cue.unlock()           — optional: warm/resume the context from the
 *                            Start-button gesture without playing a sound
 *
 * Design: audio-bible.md. Documentary restraint — paper, stamps, doors.
 * Pure WebAudio: oscillators + filtered noise. No files, no network,
 * no dependencies. Every entry point is guarded: no path in this file may
 * throw into the game. If WebAudio is missing or sound is off, play()
 * returns immediately and silently.
 * ========================================================================== */
(function () {
  'use strict';

  var STORAGE_KEY = 'f90d-sound';
  var MASTER_GAIN = 0.6;

  var root = (typeof window !== 'undefined') ? window
           : (typeof globalThis !== 'undefined') ? globalThis : this;

  /* ---- persisted on/off state (OFF by default, failures resolve to OFF) -- */
  function readStored() {
    try {
      if (root.localStorage) return root.localStorage.getItem(STORAGE_KEY) === '1';
    } catch (e) { /* private mode / no storage — OFF */ }
    return false;
  }
  function writeStored(on) {
    try {
      if (root.localStorage) root.localStorage.setItem(STORAGE_KEY, on ? '1' : '0');
    } catch (e) { /* persistence is best-effort; in-memory state still works */ }
  }

  var enabled = readStored();
  var ctx = null;        // AudioContext, created lazily inside a gesture path
  var master = null;     // master gain -> compressor -> destination
  var noiseBuf = null;   // one shared 1s white-noise buffer per context

  function audioCtor() {
    return root.AudioContext || root.webkitAudioContext || null;
  }

  function ensureCtx() {
    if (ctx) return ctx;
    var AC = audioCtor();
    if (!AC) return null;
    try {
      ctx = new AC();
      var comp = ctx.createDynamicsCompressor();
      comp.threshold.value = -18;
      comp.knee.value = 18;
      comp.ratio.value = 12;
      comp.attack.value = 0.003;
      comp.release.value = 0.25;
      comp.connect(ctx.destination);
      master = ctx.createGain();
      master.gain.value = MASTER_GAIN;
      master.connect(comp);
      // Shared noise buffer: 1 second of white noise, generated once.
      var len = ctx.sampleRate;
      noiseBuf = ctx.createBuffer(1, len, ctx.sampleRate);
      var data = noiseBuf.getChannelData(0);
      for (var i = 0; i < len; i++) data[i] = Math.random() * 2 - 1;
    } catch (e) {
      ctx = null; master = null; noiseBuf = null;
      return null;
    }
    return ctx;
  }

  function tryResume() {
    try {
      if (ctx && ctx.state === 'suspended') {
        var p = ctx.resume();
        if (p && typeof p.catch === 'function') p.catch(function () { /* lost cue is acceptable */ });
      }
    } catch (e) { /* never throw into the game */ }
  }

  /* ---- synthesis helpers ------------------------------------------------ */

  // A single oscillator tone with a shaped envelope.
  // o: {t0, dur, peak, type, f0, f1 (optional end freq), attack (s), dest}
  function tone(o) {
    var t0 = o.t0, dur = o.dur, peak = o.peak;
    var attack = Math.min(o.attack || 0.005, dur / 2);
    var osc = ctx.createOscillator();
    osc.type = o.type || 'sine';
    osc.frequency.setValueAtTime(o.f0, t0);
    if (o.f1) osc.frequency.exponentialRampToValueAtTime(Math.max(o.f1, 1), t0 + dur);
    var g = ctx.createGain();
    g.gain.setValueAtTime(0.0001, t0);
    g.gain.exponentialRampToValueAtTime(Math.max(peak, 0.0002), t0 + attack);
    g.gain.exponentialRampToValueAtTime(0.0001, t0 + dur);
    osc.connect(g); g.connect(o.dest || master);
    osc.start(t0); osc.stop(t0 + dur + 0.05);
  }

  // A burst of filtered noise from the shared buffer.
  // o: {t0, dur, peak, type ('lowpass'|'bandpass'|'highpass'), f0, f1, q, attack, dest}
  function noise(o) {
    var t0 = o.t0, dur = o.dur, peak = o.peak;
    var attack = Math.min(o.attack || 0.008, dur / 2);
    var src = ctx.createBufferSource();
    src.buffer = noiseBuf;
    src.loop = true;
    try { src.loopStart = Math.random() * 0.5; } catch (e) { /* cosmetic */ }
    var filt = ctx.createBiquadFilter();
    filt.type = o.type || 'bandpass';
    filt.frequency.setValueAtTime(o.f0, t0);
    if (o.f1) filt.frequency.exponentialRampToValueAtTime(Math.max(o.f1, 10), t0 + dur);
    filt.Q.value = o.q || 0.9;
    var g = ctx.createGain();
    g.gain.setValueAtTime(0.0001, t0);
    g.gain.exponentialRampToValueAtTime(Math.max(peak, 0.0002), t0 + attack);
    g.gain.exponentialRampToValueAtTime(0.0001, t0 + dur);
    src.connect(filt); filt.connect(g); g.connect(o.dest || master);
    src.start(t0); src.stop(t0 + dur + 0.05);
  }

  // A soft piano-ish chord: triangle partials through one shared lowpass.
  function chord(notes, t0, opts) {
    var filt = ctx.createBiquadFilter();
    filt.type = 'lowpass';
    filt.frequency.value = opts.cutoff;
    filt.Q.value = 0.4;
    filt.connect(master);
    for (var i = 0; i < notes.length; i++) {
      tone({ t0: t0, dur: opts.dur, peak: opts.perNote, type: 'triangle',
             f0: notes[i], attack: opts.attack, dest: filt });
      // A whisper of fundamental under each note for body on small speakers.
      tone({ t0: t0, dur: opts.dur * 0.8, peak: opts.perNote * 0.5, type: 'sine',
             f0: notes[i] / 2, attack: opts.attack, dest: filt });
    }
  }

  function thump(t0, peak) { // the low body of knock / stamp / door
    tone({ t0: t0, dur: 0.11, peak: peak, type: 'sine', f0: 92, f1: 54, attack: 0.004 });
  }

  /* ---- the cues (audio-bible.md §2) -------------------------------------- */

  var CUES = {

    // Two firm thumps ~180 ms apart. A knock, not a warning.
    knock: function (t0) {
      for (var i = 0; i < 2; i++) {
        var t = t0 + i * 0.19;
        tone({ t0: t, dur: 0.10, peak: 0.34, type: 'sine', f0: 115, f1: 68, attack: 0.003 });
        noise({ t0: t, dur: 0.045, peak: 0.12, type: 'lowpass', f0: 420, attack: 0.002 });
      }
    },

    // The signature: contact, body, then the form sliding away.
    stamp: function (t0) {
      noise({ t0: t0, dur: 0.05, peak: 0.22, type: 'lowpass', f0: 700, attack: 0.002 });
      thump(t0, 0.46);
      noise({ t0: t0 + 0.07, dur: 0.22, peak: 0.10, type: 'bandpass', f0: 1250, f1: 580, q: 1.4, attack: 0.02 });
    },

    // Paper turning: lift, sweep, settle.
    page: function (t0) {
      noise({ t0: t0, dur: 0.42, peak: 0.16, type: 'bandpass', f0: 380, f1: 2400, q: 0.8, attack: 0.12 });
      noise({ t0: t0 + 0.18, dur: 0.20, peak: 0.07, type: 'bandpass', f0: 1800, f1: 760, q: 0.8, attack: 0.05 });
    },

    // One tick. Once. The game does not nag.
    tick: function (t0) {
      noise({ t0: t0, dur: 0.028, peak: 0.13, type: 'highpass', f0: 3000, attack: 0.001 });
      tone({ t0: t0, dur: 0.04, peak: 0.05, type: 'sine', f0: 1750, attack: 0.001 });
    },

    // Latch, paper unfolding, one quiet note under it.
    unlock: function (t0) {
      tone({ t0: t0, dur: 0.035, peak: 0.10, type: 'square', f0: 1150, attack: 0.001 });
      noise({ t0: t0 + 0.05, dur: 0.32, peak: 0.12, type: 'bandpass', f0: 500, f1: 1100, q: 0.7, attack: 0.09 });
      tone({ t0: t0 + 0.10, dur: 0.30, peak: 0.07, type: 'sine', f0: 659.25, attack: 0.03 });
    },

    // Home: C major triad, warm filter, room around the notes.
    chord_warm: function (t0) {
      chord([261.63, 329.63, 392.00], t0,
            { cutoff: 1250, attack: 0.045, dur: 1.1, perNote: 0.10 });
    },

    // The file stays open: diminished color, duller filter, no resolution.
    chord_flat: function (t0) {
      chord([220.00, 261.63, 311.13], t0,
            { cutoff: 820, attack: 0.07, dur: 1.05, perNote: 0.08 });
    },

    /* -- v1.1 (spec'd in the bible; not fired by the v1 visual build) ----- */

    // A door closing softly and completely. Never a slam.
    door_close: function (t0) {
      noise({ t0: t0, dur: 0.20, peak: 0.14, type: 'lowpass', f0: 780, f1: 190, attack: 0.03 });
      tone({ t0: t0 + 0.13, dur: 0.10, peak: 0.20, type: 'sine', f0: 82, f1: 58, attack: 0.004 });
      noise({ t0: t0 + 0.24, dur: 0.03, peak: 0.08, type: 'bandpass', f0: 2100, q: 2.0, attack: 0.001 });
    },

    // A phone buzzing on a table. Not a ringtone.
    phone: function (t0) {
      for (var i = 0; i < 2; i++) {
        var t = t0 + i * 0.22;
        tone({ t0: t, dur: 0.10, peak: 0.13, type: 'sawtooth', f0: 118, attack: 0.008 });
        noise({ t0: t, dur: 0.09, peak: 0.05, type: 'lowpass', f0: 500, attack: 0.005 });
      }
    }
  };

  /* ---- public contract ---------------------------------------------------- */

  var Cue = {
    // Names this build can play (contract cues first, then v1.1 extras).
    cues: Object.keys(CUES),

    play: function (name) {
      if (!enabled) return;
      var fn = CUES[name];
      if (!fn) return;                       // unknown cue: ignore, never throw
      try {
        if (!ensureCtx()) return;            // no WebAudio: silent no-op
        tryResume();                         // cues fire from click handlers
        fn(ctx.currentTime + 0.02);
      } catch (e) { /* sound must never break the game */ }
    },

    setEnabled: function (on) {
      enabled = !!on;
      writeStored(enabled);
      if (enabled) {                         // toggle click is a user gesture
        try { if (ensureCtx()) tryResume(); } catch (e) { /* guarded */ }
      }
      return enabled;
    },

    isEnabled: function () { return enabled; },

    // Call from the Start-button handler so the context is born inside the
    // gesture and the first real cue is not eaten by autoplay policy.
    unlock: function () {
      if (!enabled) return false;
      try {
        if (!ensureCtx()) return false;
        tryResume();
        return true;
      } catch (e) { return false; }
    }
  };

  root.Cue = Cue;
})();
