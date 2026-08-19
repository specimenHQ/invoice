# Format & Container Spec — LOCKED

## What this project is
**Format name: Interactive Abstract Graphic Novel.**

A story told as a sequence of self-contained, single-screen interactive scenes — not static
comic panels, not a scrolling webpage, not a game with branching paths. Each scene is a small,
touchable, self-playing moment (built as one self-contained HTML file, e.g.
`hand-from-wall-demo.html`) that the reader experiences on their phone: something moves once,
resolves, and may respond to a touch (haptics, a reset). "Abstract" because the visual language is
procedural/typographic (ASCII, binary digits, gradients) built from photo references rather than
illustrated or painted art. "Graphic novel" because these scenes are read in sequence as pages of
a larger story (see `../../invoice-book-1-*.md` at the repo root for the manuscript/scene outline
this visual language serves).

## LOCKED mobile container
- **Canvas: 1168 × 2076px, 9:16 portrait** — this is the fixed frame every scene renders inside.
  Matches a standard mobile phone screen ratio. All current locked assets (`wall_filled_still.png`,
  `wall_filled_animation.gif`, `hand-from-wall-demo.html`) use this exact canvas.
- Content is full-bleed inside this frame — no letterboxing, no forced margins beyond what a
  scene's own composition calls for (e.g. the wall's left-edge black).
- Delivery wrapper (as established by `hand-from-wall-demo.html`): a single self-contained HTML
  file, dark page background (`#0b0b0b`) outside the frame, the 9:16 frame centered and scaled to
  fit the viewport via `max-width` + `aspect-ratio` (not fixed pixel size), so it scales cleanly
  across different phone screens while preserving the locked 9:16 composition untouched.
- Any interactive controls (Reset button, etc.) live BELOW the frame, never overlapping the
  canvas itself.
- Every scene obeys the standing design law (see `LOCKED-SPEC.md`): gradient always left→right,
  dark→light, ending on white, applied as a post-process pass anchored at the white baseline.

## Do not
- Don't change the 1168×2076 / 9:16 canvas ratio for this scene or future scenes without being
  asked — it's the locked mobile container for the whole graphic novel format.
- Don't turn this into a scrolling/multi-screen format — one scene = one fixed screen.
- Don't add illustrated/painted art — the visual language is procedural (ASCII/binary/gradient)
  built from real photo references, per "abstract."
