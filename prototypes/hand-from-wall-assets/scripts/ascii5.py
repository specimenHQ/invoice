from PIL import Image

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

# restrict hand search to central columns only (avoid vignette corners)
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
pad = 1
min_col = max(0, min_col - pad)
max_col = min(cols - 1, max_col + pad)

lines = []
for y in range(rows):
    line = []
    for x in range(cols):
        p = pixels[x, y]
        if y < waterline:
            if min_col <= x <= max_col and p < HAND_THRESH:
                if p < 80:
                    ch = "1"
                elif p < 110:
                    ch = "1" if (x+y) % 2 == 0 else "0"
                else:
                    ch = "0" if (x+y) % 3 == 0 else " "
            else:
                ch = " "   # solid white above water, outside hand
        else:
            if p > 230:
                ch = " "
            elif p > 190:
                ch = "0" if (x+y) % 6 == 0 else " "
            elif p > 150:
                ch = "0" if (x+y) % 3 == 0 else " "
            elif p > 100:
                ch = "1" if (x+y) % 2 == 0 else "0"
            else:
                ch = "1"
        line.append(ch)
    lines.append("".join(line))

out = "\n".join(lines)
with open("/tmp/ascii_art5.txt", "w") as f:
    f.write(out)
print("waterline:", waterline, "hand cols:", min_col, max_col)
print(out)
