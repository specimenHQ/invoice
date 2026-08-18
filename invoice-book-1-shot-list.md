# INVOICE — Book 1 — Source Image Shot List

313 panels use only 6 board_geometry types. You don't need 313 photos — you need
one strong source image per type below, reused across many panels via different
jp2a crop/width/chars settings per CSV row.

## 1. Empty field — 36 panels

What to shoot: near-black texture with almost no visible structure. Dark fabric,
a shadowed wall, black card under low raking light. The goal is near-total
absence — jp2a at low width should read as almost nothing, a few marks at most.

Used for: Pages 1-3ish (Point/dot stage), G00-G05 gradient bands.

## 2. Diagonal pressure — 72 panels (largest category)

What to shoot: something under visible strain along a diagonal — a stretched
or creased dark fabric, a bent/warped board, a taut rope or strap lit from one
side so the diagonal edge is the brightest line in frame. This is your most-used
image, worth the most care.

Used for: pressure/pain-building pages, mid gradient bands (G05-G25).

## 3. Dense cluster — 48 panels

What to shoot: tangled, knotted material with no single dominant line — rope,
wire, roots, or crumpled paper photographed close so the whole frame reads as
texture rather than a recognizable object. This is what should reveal the
"letters/broken clusters" language-ladder stage, and later the single-letter
"I" body render (see the hand test — it worked because the source photo had
a clean silhouette against negative space, so lean toward strong figure-ground
contrast even in the tangle).

Used for: G15-G25 (stress/planes, wood detail).

## 4. Horizontal seam — 48 panels

What to shoot: a hard horizontal line of light — a door seam, a crack under
a doorframe, a sliver of light across an otherwise dark surface. This is
explicitly your rupture-sliver material (G35 "dark grey with rupture sliver").
Keep everything else in the frame near-black so the seam itself is the only
readable feature.

Used for: G35, the sliver-of-light material.

## 5. Stepped threshold — 43 panels

What to shoot: an edge or step with real depth — a raised sill, a stair edge,
a ledge photographed so there's a clear "before" and "after" plane. This is
the closest-to-literal image in the set: it should visually read as a
threshold even before any rendering is applied.

Used for: G45-G55, approaching the door/threshold.

## 6. Diagonal pressure to direction — 66 panels

What to shoot: similar to #2 but with a clear implied direction/vector — a
diagonal that points somewhere (a beam of light, a sightline, a leaning
form), rather than just visible strain. Where #2 reads as "under pressure,"
this one should read as "heading toward."

Used for: transition panels moving the reader's eye toward the next stage.

## Two special panels outside this system

- **Page 1 area (marks-only rows)** — no photo needed, render_mode is
  literally "mark" (a single `.`).
- **Page 52, seventh panel (absolute_panel 313)** — render_mode is "photo."
  This needs its own dedicated real photograph (or the eventual body/hand
  photo referenced earlier), not one of the 6 texture images above, since
  it's the hard-cut reveal the whole book has been building toward.

## Workflow once you have the 6 (or 7, with the page-52 photo) images

1. Save each under `reference-images/` with a clear name
   (e.g. `src-diagonal-pressure.jpg`).
2. In `invoice-book-1-panel-prompt-grid.csv`, fill the `source_image` column
   for each row with the matching file path — this can be done in bulk with
   a script since it's driven by `board_geometry`, not manually per row.
3. Run `python3 render_panels.py --dry-run` to confirm every row now resolves
   to a real command, then drop `--dry-run` to actually render.
