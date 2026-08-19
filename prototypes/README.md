# Prototypes

Working demos built during design sessions. Each proves one specific
mechanism — see `../invoice-book-1-tech-spec.md` for the rules these are
testing against.

- **ascii3d-cube-demo.html** — rotating 3D ASCII cube, orthographic
  projection, procedural (no photo).
- **crate-cube-merge-demo.html** — the cube merging between pure procedural
  geometry and the real crate photo texture, plus an independent background
  gradient system. Uses `../reference-images/src-crate.jpg`.
- **gradient-full-demo.html** — full black→grey→white(rupture)→photo
  sequence built from additive/screen compositing (verified monotonic
  luminance). Uses reference-only placeholder textures.
- **live-gradient-demo.html** — scroll-driven, continuously-animated
  version of the compositing gradient (not fixed frames).
- **invoice-medium-demo.html** — the original mark→punctuation→ASCII→binary→
  photo scroll sequence, including the "I"-rendered hand test.
- **pages-6-9-hum-prototype.html** — real working prototype: the actual
  "Rckly Suffix" loop (see `../audio/`) as the literal hum from the text,
  gapless Web Audio loop, haptic pulse synced to the real loop transient.
- **hand-from-wall-demo.html** — locked hand-emerging-from-wall sequence, built
  from a real source photo: whole composition rotated 90° + flipped so the
  wall sits left/hand reaches right, wall rendered as true binary text (no
  blank gaps) with a locked left→right dark→light gradient applied as a
  final post-process pass (plateau 0.35, power 1.6, anchored at white).
  Arm slides out as one rigid sprite, one-time decaying shake on touch-down,
  plays once (no loop). Includes a Reset button and ramping device haptics
  (Vibration API, Android only) that hold steady after touch-down until the
  hand itself is tapped. Mobile 9:16 canvas (1168×2076). Self-contained
  (gif embedded as base64).

All are self-contained single HTML files (audio/images embedded as
base64) except where they explicitly reference a file in `../reference-images/`.
