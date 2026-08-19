# Locked Version — Binary ASCII Hand Animation

**Status: LOCKED / FINAL (v5 — gradient applied as post-process, mobile 9:16, haptics)**

## STANDING DESIGN LAW (applies to every image/scene in this piece, locked)
**Every gradient goes left → right, dark → light. The story moves from darkness into light, and
every final scene lands on white.** The gradient is applied as a FINAL POST-PROCESS PASS over the
whole finished composition (wall + hand already assembled, no color grading yet), anchored at
white at the wall/hand edge (the baseline) and computed BACKWARD from there toward black at the
far left edge. Never bake color/gradient into the wall generation step itself — build the flat
black-on-white composition first, then grade it.

## LOCKED gradient parameters
- Method: `apply_gradient_backward_from_white()` in `scripts/gradient_postprocess.py` — multiplies
  each pixel's RGB by a factor `k` that is 0 (black) up to a plateau, then eases from 0→1 with
  `t ** power` out to the wall/hand edge (k=1, i.e. unchanged/white baseline).
- **plateau = 0.35** of the wall width (598px) — stays fully solid black for the first 35%.
- **power = 1.6** — easing curve for the fade after the plateau.
- This is applied to the FLAT composition (`final/step1_flat_composition.png`: plain black digits
  on white, no color at all), not to individually-colored text — this is what makes the black
  zone keep visible digit texture (black text stays true black at k=0, only the white background
  darkens with it) instead of going to a flat void.

## LOCKED gradient contact sheet
- **Status: LOCKED.** File: `final/gradient_52_pages.png` — the locked gradient curve (plateau
  0.35, power 1.6) rendered as a single strip and divided into 52 equal numbered sections (1–52)
  with red vertical divider lines, top and bottom labels. Reference sheet for pointing at
  specific points along the gradient by page number.
- Superseded exploratory sheets kept for reference only in `exploration/` — do not regenerate.

## Final files
- `final/step1_flat_composition.png` — flat pre-grade composition (reference only)
- `final/wall_filled_still.png` — locked still (1168 x 2076, 9:16 portrait)
- `final/wall_filled_animation.gif` — locked animation (plays ONCE, no loop flag)
- `final/hand_reset.html` — self-contained interactive page (gif embedded as base64):
  - Reset button (replays the gif from frame 1)
  - Device haptics (Vibration API, Android only): ramps up 720ms→2330ms as the hand slides out,
    fires a strong burst at 2330ms (touch point), then holds ONE STEADY CONTINUOUS vibration
    (re-issued back-to-back, not pulsed) until the user touches the hand specifically (right
    ~49% of the image, past the wall edge at x=598/1168), detected via `pointerdown` on the
    frame container (touchstart/click as fallback), iOS callout/selection disabled on the img.
- `final/original_v3_rotated_left_flipped_clean.png` / `final/arm_slides_from_wall_clean.gif` —
  earlier-stage locked assets (pre wall-fill/gradient), kept because later scripts build on them.

## Sequence / timing (locked, current gif)
- 0.0s–0.72s: hand hidden behind the wall (hold)
- 0.72s–2.33s: hand slides out from behind the wall to its resting position (23 steps @ 70ms)
- 2.33s–2.78s: sharp decaying visual shake as the hand touches/settles into the white (10 steps @
  45ms, amplitude 8→0px) — LOCKED, user confirmed this is perfect, never remove/alter
- 2.78s onward: dead stop, holds still (separate from the haptic hold, which starts ~2.59s and
  continues indefinitely until the hand is touched)

**Music note (user plan):** music plays under the animation, cuts off ABRUPTLY the moment the hand
fully reaches/settles into white, ~2.78s in current timing.

## Known bugs already fixed (do not reintroduce)
- GIF `loop=1` in PIL actually means "play twice" — caused an unwanted repeat on mobile. Do not
  set a `loop` value on export unless infinite loop is explicitly wanted.
- A literal unpainted 10px white margin existed at the true left edge (x=0–10) in an earlier wall
  build — always make sure any background fill covers the full canvas including padding/margins,
  not just the text-drawing area.
- GIF per-frame color quantization (especially with Floyd-Steinberg dithering) on a smooth
  gradient can create a visible flicker/seam line during playback — avoid manual per-frame
  palette/dither rebuilds; the plain PIL `save_all` export was clean.

## What it is
- Source: user's uploaded photo of a hand reaching up out of water.
- Base ASCII composition: white background above the waterline, hand rendered in 1s/0s
  density-mapped from the photo, water gradient below the waterline. Waterline detected at row 40
  of 82; hand column range 24–75.
- Whole image rotated 90° counterclockwise, then flipped horizontally → wall (former water) now
  sits on the left as a dense vertical block, hand reaches out horizontally to the right, thumb
  (single "0") pointing up.
- Stray disconnected noise dots (vignette corner artifacts) were painted out — thumb dot and all
  connected hand pixels preserved.
- Wall region is TRUE binary text (only "1"/"0" characters, zero blank gaps).
- Canvas extended to mobile phone portrait ratio (9:16) by tiling the wall pattern downward — the
  hand itself was NOT resized, moved, or touched, only the canvas grew.
- Animation: arm cut out as a single sprite, slides as one rigid piece from hidden-behind-wall to
  resting position, then a one-time sharp decaying vibration when it touches the white, then a
  dead stop. Plays once (not looped back-and-forth).

## Scripts (in run order)
1. `scripts/ascii5.py` — builds the base ASCII composition from the source photo
2. `scripts/animate3.py` — rotates/flips the whole composition, cleans noise
3. `scripts/slide_arm_clean.py` — cuts the arm sprite, builds the slide + shake animation
4. `scripts/gradient_postprocess.py` — builds the flat wall composition + applies the locked
   backward-from-white gradient (still + animation)
5. `scripts/gradient_52.py` — builds the 52-page locked gradient contact sheet (abstract strip)
6. `scripts/gradient_52_on_real.py` — overlays the 52-page divisions on the real locked wall image

## Do not
- Regenerate the ASCII/density mapping from scratch for this version — reuse the exact locked
  files above.
- Re-rotate, re-flip, or resize/rescale the hand again without being asked.
- If further aspect-ratio changes are needed, extend the wall/white canvas only — never scale the hand.
- Don't reintroduce the retract/loop-back motion — this is a one-shot animation now.
- Don't violate the standing gradient law (left→right, dark→light, ending white, applied as a
  post-process anchored at white) on any new scene.
- Don't set a `loop` value on the gif export unless explicitly asked.
- Don't re-bake gradient color into the wall-text-generation step — always do flat composition
  first, then grade as a separate final pass.
- Don't re-litigate the plateau/power values (0.35 / 1.6) or the 52-page contact sheet without
  being asked.
