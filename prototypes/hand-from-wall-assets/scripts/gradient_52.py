from PIL import Image, ImageDraw, ImageFont
import os

strip_w = 1560
strip_h = 260
n_pages = 52

def make_strip(plateau_frac, power, w, h):
    im = Image.new("RGB", (w, h), "black")
    px = im.load()
    plateau = plateau_frac * w
    for x in range(w):
        if x <= plateau:
            k = 0.0
        else:
            t = (x - plateau) / (w - plateau)
            k = t ** power
        g = int(255 * k)
        for y in range(h):
            px[x, y] = (g, g, g)
    return im

# LOCKED gradient params: plateau 0.35, power 1.6
strip = make_strip(0.35, 1.6, strip_w, strip_h)

font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
label_font = ImageFont.truetype(font_path, 12) if os.path.exists(font_path) else ImageFont.load_default()

top_margin = 30
bottom_margin = 30
sheet = Image.new("RGB", (strip_w, strip_h + top_margin + bottom_margin), "white")
sheet.paste(strip, (0, top_margin))
draw = ImageDraw.Draw(sheet)

seg_w = strip_w / n_pages
for i in range(n_pages + 1):
    x = round(i * seg_w)
    draw.line([(x, top_margin), (x, top_margin + strip_h)], fill=(230, 30, 30), width=2)

for i in range(n_pages):
    cx = (i + 0.5) * seg_w
    label = str(i + 1)
    bbox = draw.textbbox((0, 0), label, font=label_font)
    tw = bbox[2] - bbox[0]
    draw.text((cx - tw/2, 8), label, font=label_font, fill="black")
    draw.text((cx - tw/2, top_margin + strip_h + 8), label, font=label_font, fill="black")

sheet.save("/tmp/out/gradient_52_pages.png")
print("done", sheet.size)
