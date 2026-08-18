# INVOICE — Book 1 — Technical Spec ("Rails")

Locked decisions from build/design sessions. This document is the reference
future work should follow — if a new idea conflicts with something here,
resolve the conflict explicitly rather than silently drifting (this is the
same failure mode that let Book 2's Sphere material leak into the Book 1
manuscript; see Scope section below).

## 1. Medium

Mobile-first, interactive, browser-native. Plain HTML/CSS/JS, deployed as a
PWA (installable, offline-capable, no app-store review). Desktop is a
secondary, letterboxed version of the same experience, not a separate design.

**Explicitly rejected:** native app wrapping (Capacitor, React Native,
Flutter), AI-generated video. The book is deliberately lo-fi — this is an
aesthetic decision, not a resource limitation, and should not be "upgraded"
away later.

## 2. Scope boundary (Book 1 vs Book 2)

Book 1 = the struggle to get out of the first crate and reach the door.
Nothing from the warehouse/memory-opening arc belongs in Book 1: no eggs, no
crate-gambling, no befriending memories, no building from crate wood.

The current manuscript file diverges into Book 2's "Sphere" material
starting around page 17 (robes, color assignment, the man in red, the
warehouse). This is out of scope for Book 1 per the rule above and still
needs to be replaced with real Book 1 content — see
`invoice-book-1-page-script.md` for the page-by-page gap.

Book 2 material may be **alluded to**, never shown — same device already
used for the Cube's hum ("felt as pressure, not explained"). Implementation:
a secondary shape or motif at ~2-3% opacity inside procedural noise, or a
matching faint haptic pulse, on panels near where the hum/sword are already
mentioned in-text (roughly pages 22-26). Never confirmed, never named.

## 3. Rendering system

313 panels, defined in `invoice-book-1-panel-prompt-grid.csv`. Each row has
a `render_mode`:

- `mark` — literal single character (e.g. `.`), no image, no jp2a. 18 panels.
- `proc-dot` / `proc-line` / `proc-plane` / `proc-seam` / `proc-cube` /
  `proc-binary` — procedurally generated (code, not photography). These
  cover the geometric/lighting stages: point, line, pressure geometry,
  planes, rupture-sliver seam, cube rotation, binary density. No source
  image required — see Section 5.
- `photo-crate` — the one photographed physical object in Book 1 (the crate
  itself, per the Material Rule: "the actual Cube is stone... the first
  prison is a wooden crate"). Source: `reference-images/src-crate.jpg`
  (locked, real, unwatermarked — already in the repo).
- `photo` — page 52, seventh panel only. The hard-cut rupture reveal. Needs
  its own dedicated photo, not yet sourced.

**Why only 2 real photos for 313 panels:** almost nothing in Book 1 is a
physical object. Point, line, box, cube, grid, pressure, and even the door
seam/sliver of light are geometry and lighting, not things a camera shoots —
they're better rendered as math. Only the crate (wood, breaking) and the
page-52 body reveal are genuinely material per the story's own rules.

Batch rendering: `python3 render_panels.py` (photo modes only — reads the
CSV, runs `jp2a` on the assigned source image with that row's width/chars).
`--dry-run` to preview without executing. `assign_source_images.py` bulk-fills
the `source_image` column from `board_geometry`.

## 4. Language Ladder (text) — extended

Marks only → punctuation → body sound → numbers/counting → single letters →
broken letter clusters → first stable shape-word → slow-growing grid →
object/action words → fragment chains → **binary density (literal 0s and 1s
form the silhouette)** → first paragraph (page 52).

The body renders in the same alphabet the language is climbing through:
sparse marks early, single-letter density mid-book (the reaching hand test
used "I" — the manuscript's only pronoun), narrowing to strictly 0/1
immediately before page 52, then hard-cutting to a real photograph. Binary
does not fade into flesh — it converts, in one panel, with a full white
rupture frame and the book's strongest haptic pulse.

## 5. Procedural rendering rules

- **Projection: orthographic, not perspective.** Rotated cube faces must stay
  true parallelograms (straight, parallel edges). Perspective projection
  (1/z divide) keystones faces into trapezoids — rejected on sight during
  testing. `ORTHO_SCALE ≈ 0.85` for a 90×45 character grid keeps the cube
  inside frame.
- **Gradient is two independent systems, not one.** (1) A page-level
  background wash, slow black→grey cycle, decoupled from panel content —
  this is the book's overall "grey created by detail accumulating in
  darkness" rule. (2) Panel-local compositing (e.g. crate/cube merge `t`),
  which can move faster and independently. Never conflate the two into a
  single parameter.
- **Compositing method: additive ("screen"), not averaging blend.** Straight
  alpha blending toward a darker layer can *reduce* mean luminance, breaking
  the monotonic black→grey requirement. Screen/additive compositing
  guarantees luminance only increases as layers accumulate — verified
  numerically (mean luminance 0.0 → 78.5 across G00→G55, strictly
  monotonic) before shipping any composite-based render.
- **White is rupture only**, never a settled state (existing Gradient Rule).
  Implemented as a hard flash frame + strongest haptic pulse, not a gradual
  fade-to-white.

## 6. Interaction rules

- **Scroll/tap-gated, one panel at a time on mobile** — vertical, portrait,
  reader cannot skip ahead (this is the mechanism that makes the "17 quiet
  dark pages" problem solvable in digital where it wasn't on paper).
- **Haptics carry the hum/pulse/breath device literally.** Rhythmic pulses
  matching heartbeat/breath timing, crescendo/fade tied to narrative
  proximity (e.g. "Something touches skin" = a haptic pulse arriving, not
  just a line of text). This is the same device later used for Book 2's
  memory-crate proximity buzz — Book 1 establishes the vocabulary, Book 2
  extends it.
- **The phone itself is a face of the box.** Per the panel-map's own Cube
  Mathematics ("the comic panel is also a face of a box"), draggable marks
  should hard-stop with haptic feedback at the four screen edges — the
  device's physical boundary functions as the crate's wall, floor, ceiling,
  door. Not yet built; scoped as the next interaction prototype.

## 7. Asset status (as of this document)

| Asset | Status |
|---|---|
| `reference-images/src-crate.jpg` | **Done.** Real, licensed-clean, unwatermarked. |
| Page 52 reveal photo | **Needed.** Real photo, not a placeholder — the one-time hard-cut payoff. |
| Procedural renderers (dot/line/plane/seam/cube/binary) | Cube prototype built and working (orthographic, texture-blending). Others not yet built as standalone generators. |
| Pages 17-52 text | **Needed.** Manuscript currently has Book 2 Sphere content here; out of scope, needs replacement Book 1 text. |

## 8. Open items explicitly not yet decided

- Tap-to-advance vs. system-paced auto-advance for the darkest early pages.
- Whether the allusion-to-Book-2 technique gets used anywhere beyond the
  hum/sword pages.
- Full interaction build for "phone as box" (drag + edge-collision haptics).
