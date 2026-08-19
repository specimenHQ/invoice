# INVOICE — Book 1 app

Browser-native, mobile-first, Android-first. Self-contained single files —
fonts embedded as base64 woff2, no external requests, works offline.

- **index.html** — the build. Title screen, start screen, pages 1–19, plus
  pages 20–52 walkable for previewing the gradient and pulse accumulation.
- **manifest.webmanifest / sw.js / icon-*.png** — PWA wrapper. Installs to the
  home screen, launches fullscreen with no browser chrome, works offline.
- **title-screen-LOCKED.html** — frozen snapshot of the locked title screen.
  Do not edit; the working build carries changes forward.
- **turn-demo.html** — standalone start-screen study (the world-level line).

## Locked

**Title screen.** Full-screen ASCII wave sweeping left to right and back on a
triangle path, riding the base gradient. The logo is a stencil over the same
character grid, not type: VOICE in 0s and 1s, IN built from the letters I and N,
on its own schedule and inverted — when VOICE is light, IN is dark. Cube is
orthographic, fitted against its rotated diagonal so it cannot clip, rotation
time-based so 60Hz and 120Hz match. 64 tone steps — fewer bands visibly.
Glyph ink coverage is measured and compensated so I, N, 0 and 1 read as one
material. Press and hold cycles the five embedded fonts.

## Opening sequence

Touch the wave (no prompt) → fade to black → black holds, a tap hurries it →
the line comes up: level with the world while the device is not, characters
staying upright and readable, a gradient falling down through it → turn the
device and the line settles level, releasing a sweep to the right → page 1.

If no tilt sensor reports within nine seconds, the line leans on its own and a
tap continues, so a sensorless device is never a dead end.

## Pages

- **1–5** black. No gradient, no texture. Auto-advance.
- **6** the one flash in the book: full white held one second, four-second fade
  back to black, leaving the period behind. The one haptic before 19.
- **6–18** marks and punctuation. Advance by touching the symbol itself —
  swipe does nothing here.
- **19** beat, flash, 0 — black — beat, flash, 1 — black — then both fade in
  together. Reveals crossfade against the flash's own fade.
- **20+** one non-repeating beat per page, lengthening 0.1s per page. Each beat
  draws a line that travels left to right, built from every symbol introduced
  so far, and deposits permanently: about half the page given to wave by 35,
  all of it by 52.
- Haptics silent until 6, then nothing until 19, then pulse trains building to
  maximum at 51–52. Pulse count and density, not one long buzz — strength is
  read as attack.

## Serving

**This must be served over HTTPS.** Android blocks orientation and motion
sensors on anything that is not a secure context, and in-app webviews do not
forward them at all — over `file://` or inside an embedded viewer the start
screen has nothing to respond to and reads as a black screen.

GitHub Pages is enough: Settings → Pages → deploy from `main`, then open
`https://<owner>.github.io/invoice/app/` in Chrome and use Add to Home Screen.

Bump `CACHE` in `sw.js` on every published build or phones will keep serving
the old one from cache. The build id also shows top-left on the title screen.
