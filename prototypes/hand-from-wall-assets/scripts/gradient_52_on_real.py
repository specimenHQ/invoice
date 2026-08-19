from PIL import Image, ImageDraw, ImageFont
import os

still = Image.open("/tmp/out/wall_filled_still.png").convert("RGB")
W, H = still.size
wall_edge = 598
n_pages = 52

font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
label_font = ImageFont.truetype(font_path, 16) if os.path.exists(font_path) else ImageFont.load_default()

top_margin = 34
overlay = Image.new("RGB", (W, H + top_margin), "white")
overlay.paste(still, (0, top_margin))
draw = ImageDraw.Draw(overlay)

seg_w = wall_edge / n_pages
for i in range(n_pages + 1):
    x = round(i * seg_w)
    draw.line([(x, top_margin), (x, top_margin + H)], fill=(230, 30, 30), width=1)

for i in range(n_pages):
    cx = (i + 0.5) * seg_w
    label = str(i + 1)
    bbox = draw.textbbox((0, 0), label, font=label_font)
    tw = bbox[2] - bbox[0]
    # rotate label vertically-ish by just placing small, alternating vertical offset to avoid overlap
    y_off = 6 if i % 2 == 0 else 20
    draw.text((cx - tw/2, y_off), label, font=label_font, fill=(200, 0, 0))

# also mark the wall/hand edge itself
draw.line([(wall_edge, top_margin), (wall_edge, top_margin + H)], fill=(0, 120, 255), width=2)

overlay.save("/tmp/out/gradient_52_on_real_wall.png")
print("done", overlay.size)
