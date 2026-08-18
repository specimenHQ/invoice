# INVOICE - BOOK 1

Prompt generation machine

## Goal

Generate image prompts for all 313 panels without letting the panels become random illustrations.

Every panel must know:

1. Where it is in the cube math.
2. What scene it belongs to.
3. What act layer it belongs to.
4. What board-geometry layer it uses.
5. What level of language is allowed.
6. What level of visibility/grey is allowed.
7. What single visual job it performs.
8. What must not appear yet.

## Master Style Prompt

Use this as the stable style base for every panel:

Black-and-white printed graphic novel panel, abstract surreal etching, heavy black ink, black-on-black visibility early, matte black field with gloss-black or near-black marks, dense linework only when the story has earned detail, no color, no clean white except rupture light, gradual black-to-grey visibility, experimental symbolic composition, claustrophobic interior pressure, wooden crate logic hidden inside the page, cube geometry born from dot to line to box to cube, no visible human body until the final page, no literal domestic room, no warehouse, no memories, no eggs, no creatures, no full prose except final page.

## Negative Prompt

Use this to keep Book 1 in scope:

color, bright white background, realistic full body, face, eyes, mouth, hands, domestic furniture, warehouse, rows of crates, children, eggs, glowing memory figures, fantasy monsters, readable narration, speech bubbles, clean modern digital art, painterly color, conventional action scene, open landscape, daylight, literal home interior.

## Panel ID Format

Use:

`B1-P##-F#`

Examples:

1. `B1-P01-F1`
2. `B1-P01-F6`
3. `B1-P52-F7`

For Pages 1-51, `F1` through `F6` echo the six faces of the cube.

For Page 52, `F7` is the breach into Book 2's formal language.

## Prompt Formula

Each panel prompt should be assembled like this:

`[MASTER STYLE] + [PANEL ID] + [ACT RULE] + [SCENE RULE] + [BOARD GEOMETRY] + [GRADIENT RULE] + [PANEL JOB] + [LANGUAGE TOKEN] + [COMPOSITION RULE] + [CONTINUITY RULE] + [NEGATIVE PROMPT]`

## Act Layer

The physical board organizes Book 1 into three act energies.

1. **Act One: Mystery / Birth** - Pages 1-18. Pre-language, pressure, body sound, growth beginning.
2. **Act Two: Terror / Death** - Pages 19-38. Planes, corners, wood, seam, sliver, break. The first container dies.
3. **Act Three: Action / Rebirth** - Pages 39-52. Outside crate, symbolic family-home dark, follow the line, humming door, silhouette, first paragraph.

These act names describe visual energy, not conventional plot exposition.

## Board Geometry Layer

Use the physical board as compositional grammar.

1. **Empty field** - large black or grey space, almost no detail.
2. **Diagonal pressure** - diagonal stress vector, growth pushing against a plane.
3. **Dense cluster** - detail accumulates, readability increases.
4. **Horizontal seam** - discovery line, crack, sliver, or threshold.
5. **Stepped threshold** - late-book approach to door, formal transition.

Do not draw the board itself. Translate its geometry into the panels.

## Panel Jobs

Every panel needs one job. Do not let a panel do everything.

Use these job types:

1. **Field** - establish blackness, pressure, or surface.
2. **Interrupt** - introduce a mark, punctuation, crack, or small disruption.
3. **Echo** - repeat a previous visual but altered.
4. **Pressure** - show growth, compression, pain, vibration.
5. **Geometry** - reveal plane, edge, corner, seam, face, grid.
6. **Material** - reveal wood grain, splinter, fiber, crate texture.
7. **Direction** - guide the eye toward seam, sliver, door, threshold.
8. **Rupture** - crack, break, tilt, breach.
9. **Stabilize** - make the panel system more readable.
10. **Threshold** - hold before transition.

## Six-Panel Page Roles

For Pages 1-51, each page has six panels. The default page rhythm:

1. **F1: Establish** - what is the page's condition?
2. **F2: Disturb** - what interrupts that condition?
3. **F3: Answer** - how does the crate/darkness respond?
4. **F4: Transform** - what changes?
5. **F5: Clarify** - what becomes more readable?
6. **F6: Hand-off** - what leads to the next page?

Early pages can hide the panel borders, but the six jobs should still exist.

## Seven-Panel Final Page

Page 52 has seven panels:

1. Recovered darkness
2. Recognizable crate aftermath
3. Direction toward door
4. Humming boundary
5. First silhouette
6. First paragraph
7. Formal breach into Book 2

The seventh panel should feel like a new law has entered the book.

## Gradient Bands

Book 1 does not become white. It becomes grey.

Use value bands:

1. **G00: total black** - Pages 1-3
2. **G05: black with marks** - Pages 4-9
3. **G10: black with pressure geometry** - Pages 10-14
4. **G15: black with stress and planes** - Pages 15-22
5. **G25: black with wood detail** - Pages 23-30
6. **G35: dark grey with rupture sliver** - Pages 31-38
7. **G45: grey-dark exterior uncertainty** - Pages 39-45
8. **G55: readable grey threshold** - Pages 46-52

White is only allowed as a narrow rupture, seam, or shock. It is not the background.

## Language Rules

The image prompt must say what text, if any, is allowed in the panel.

1. Pages 1-3: symbols/marks only
2. Pages 4-6: punctuation only
3. Pages 7-9: body sound, especially `?mmh.`
4. Pages 10-14: single letters and broken clusters
5. Pages 15-18: repeated line/grid fragments and multitude fragments
6. Pages 19-30: object/action fragments
7. Pages 31-51: fragment chains, still no prose
8. Page 52: first paragraph

Text should be part of the image system, not clean captions, until the final paragraph.

## Continuity Anchors

Book 1 continuity anchors:

1. No visible human body until Page 52 silhouette.
2. No face, mouth, hands, or eyes in Book 1.
3. The first space is a wooden crate, but it is hidden at first.
4. The dark room outside the crate represents family home, not literal furniture.
5. The actual Cube is stone, otherworldly, humming, and mostly unexplained.
6. The book goes black to grey, not black to white.
7. Six panels per page until Page 52.
8. Page 52 has seven panels.

## Scene Prompt Modules

Use one scene module per panel.

### Scene 1: Pages 1-3

Point. Empty blackness, hidden crate interior, invisible six-panel pressure, black-on-black dot/point awareness, strange marks only, no body, no wood, no room.

### Scene 2: Pages 4-6

Line. Punctuation as pressure points, period/question marks as awareness punctures, dot stretching into line, first direction/edge, unseen wall pressure.

### Scene 3: Pages 7-9

Box. First body sound as vibration and pain inside an implied flat box, no anatomy, `?mmh.` as first readable sound.

### Scene 4: Pages 10-14

Cube. Flat box begins rotating into cube logic, letters as cube geometry, curve/circle/line/closed shape, no stable full word.

### Scene 5: Pages 15-18

Growing Grid. Cube-logic becomes a slow-growing abstract grid without explicit cube drawings: one line crossed by another, incomplete cells, repeated right angles, offset corners, displaced planes, nested perspective lines, six-panel echoes. Use the feeling of a building facade receding into black, a reflective window grid, an isometric tile field, or an impossible tiled loop, but keep it black-on-black and abstract. Not literal cubes, not warehouse crates, not rows of boxes.

### Scene 6: Pages 19-22

Growth pressure / planes and corners. The repeated cube pattern compresses inward; readable planes and corners emerge, unstable orientation, resistance has shape.

### Scene 7: Pages 23-26

Wood grain emerges from blackness, material discovery, crate still not fully shown.

### Scene 8: Pages 27-30

Upper door seam appears, first line that might be an exit.

### Scene 9: Pages 31-34

Sliver of rupture light enters through seam, white only as a thin breach.

### Scene 10: Pages 35-38

Crate break, pressure becomes action, panels crack and tilt.

### Scene 11: Pages 39-42

Dark symbolic family-home space outside crate, unclear surroundings, no furniture.

### Scene 12: Pages 43-45

Follow the sliver/line through grey-dark space, directional clarity.

### Scene 13: Pages 46-48

Humming door, stone-adjacent boundary, larger Cube mystery.

### Scene 14: Pages 49-51

Threshold, escaped crate, door dominates, almost-thought but not prose.

### Scene 15: Page 52

First silhouette, first paragraph, seven panels, readable grey threshold.

## Example Prompt

Panel ID: `B1-P08-F4`

Prompt:

Black-and-white printed graphic novel panel, abstract surreal etching, heavy black ink, no color, no clean white except rupture light, gradual black-to-grey visibility. Panel B1-P08-F4, Scene 3, G05 black with marks. Show the first body sound as a small vibration disturbance in empty blackness, no mouth, no throat, no visible body. The text `?mmh.` appears as damaged pressure lettering embedded in the darkness, not a caption or speech bubble. Six-panel cube logic is hidden beneath the composition. Claustrophobic interior pressure, unseen wooden crate. Negative: color, full body, face, eyes, mouth, hands, domestic furniture, warehouse, children, eggs, creatures, speech bubble, clean white background.

## Output Schema

Each panel should produce:

1. absolute_panel
2. panel_id
3. page
4. panel_on_page
5. scene
6. act_layer
7. board_geometry
8. gradient_band
9. panel_job
10. allowed_text
11. visual_meaning
12. image_prompt
13. negative_prompt
