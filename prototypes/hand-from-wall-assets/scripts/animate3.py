from PIL import Image, ImageDraw, ImageFont
import os

src = "/root/.claude/uploads/29f6c13c-6717-5b92-976f-9b78faf4a0da/5660e667-1787099899079_image.png"
img = Image.open(src).convert("L")

cols = 100
aspect_correction = 0.55
w, h = img.size
rows = int((h / w) * cols * aspect_correction)
img_small = img.resize((cols, rows))
pixels = img_small.load()

row_avg = [sum(pixels[x, y] for x in range(cols)) / cols for y in range(rows)]
waterline = None
for y in range(1, rows):
    if row_avg[y-1] > 150 and row_avg[y] < 150 and y > rows * 0.4:
        waterline = y
        break
if waterline is None:
    waterline = rows // 2

center_lo, center_hi = int(cols*0.25), int(cols*0.75)
HAND_THRESH = 140
min_col, max_col = cols, 0
for y in range(waterline):
    for x in range(center_lo, center_hi):
        if pixels[x, y] < HAND_THRESH:
            min_col = min(min_col, x)
            max_col = max(max_col, x)
if min_col > max_col:
    min_col, max_col = center_lo, center_hi
min_col = max(0, min_col - 1)
max_col = min(cols - 1, max_col + 1)

# water gradient grid (below waterline)
water_grid = []
for y in range(rows):
    row = []
    for x in range(cols):
        p = pixels[x, y]
        if p > 230: ch = " "
        elif p > 190: ch = "0" if (x+y) % 6 == 0 else " "
        elif p > 150: ch = "0" if (x+y) % 3 == 0 else " "
        elif p > 100: ch = "1" if (x+y) % 2 == 0 else "0"
        else: ch = "1"
        row.append(ch)
    water_grid.append(row)

# hand sprite from actual photo pixels (rows 0..waterline-1, exact shape)
hand_sprite = {}
for y in range(waterline):
    for x in range(min_col, max_col+1):
        p = pixels[x, y]
        if p < HAND_THRESH:
            if p < 80: ch = "1"
            elif p < 110: ch = "1" if (x+y) % 2 == 0 else "0"
            else: ch = "0" if (x+y) % 3 == 0 else " "
            if ch != " ":
                hand_sprite[(y, x)] = ch

sprite_min_row = min(r for r, c in hand_sprite)
sprite_max_row = max(r for r, c in hand_sprite)

font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
font_size = 12
font = ImageFont.truetype(font_path, font_size) if os.path.exists(font_path) else ImageFont.load_default()
char_h = font_size + 2
img_w = int((font.getbbox("0")[2]) * cols) + 20
img_h = int(char_h * rows) + 20

total_rows_for_travel = rows  # sprite can travel all the way down through the water field

def render(row_shift):
    # row_shift: 0 = final resting position (matches liked image). Positive = pushed down INTO the water/numbers.
    grid = [[" "]*cols for _ in range(rows)]
    for y in range(waterline, rows):
        for x in range(cols):
            grid[y][x] = water_grid[y][x]
    # sprite drawn on top, can appear both above water (white bg) and submerged in water (overwriting water numbers)
    for (ry, cx), ch in hand_sprite.items():
        ny = ry + row_shift
        if 0 <= ny < rows:
            grid[ny][cx] = ch
    im = Image.new("RGB", (img_w, img_h), "white")
    draw = ImageDraw.Draw(im)
    y = 10
    for row in grid:
        draw.text((10, y), "".join(row), font=font, fill="black")
        y += char_h
    return im

frames, durations = [], []

max_shift = (rows - 1) - sprite_max_row  # sprite pushed all the way to bottom, fully submerged in water
steps = 22

# 1. blank/submerged start - only water visible, hand not yet risen (fully underwater, out of view range mostly)
start = render(max_shift)
frames += [start]*4; durations += [180]*4

# 2. hand rises up through the water numbers to its final resting pose above the waterline
for i in range(steps+1):
    shift = int(max_shift * (1 - i/steps))
    frames.append(render(shift))
    durations.append(70)

final = render(0)
frames += [final]*10; durations += [150]*10   # hold on the exact liked image

# 3. reverse: hand sinks back down through the water
for i in range(steps+1):
    shift = int(max_shift * (i/steps))
    frames.append(render(shift))
    durations.append(70)

frames += [start]*4; durations += [180]*4

frames[0].save("/tmp/out/hand_through_numbers_v2.gif", save_all=True, append_images=frames[1:],
               duration=durations, loop=0, optimize=False)
print("frames:", len(frames), "waterline:", waterline)
