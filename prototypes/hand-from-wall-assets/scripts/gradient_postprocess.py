from PIL import Image, ImageDraw, ImageFont
import os

# STEP 1: build the full composition flat -- plain black digits on white, no color grading at all.
# STEP 2: apply the gradient as a single final pass over the whole finished image, anchored at
# white (the baseline) right at the wall/hand edge, and working BACKWARD from there into black.

still = Image.open("/tmp/out/original_v3_rotated_left_flipped_clean.png").convert("RGB")
W, H = still.size
wall_edge = 598

font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
font_size = 12
font = ImageFont.truetype(font_path, font_size) if os.path.exists(font_path) else ImageFont.load_default()
char_w = font.getbbox("0")[2]
char_h = font_size + 2

target_w = W
target_h = int(W * 16 / 9)

wall_cols = wall_edge // char_w + 1
wall_rows = target_h // char_h + 1

def wall_char(col, row):
    h = (col * 92821 + row * 68917 + col * row * 137) & 0xFFFFFFFF
    h ^= h >> 13
    h *= 0x5bd1e995
    h &= 0xFFFFFFFF
    h ^= h >> 15
    noise = (h % 1000) / 1000.0
    return "1" if noise < 0.5 else "0"

def build_flat_composition():
    # plain black-on-white wall, no gradient yet
    im = Image.new("RGB", (target_w, target_h), "white")
    draw = ImageDraw.Draw(im)
    y = 10
    row = 0
    while y < target_h:
        line = "".join(wall_char(c, row) for c in range(wall_cols))
        draw.text((10, y), line, font=font, fill="black")
        y += char_h
        row += 1
    # composite the hand, untouched, exactly where it already is
    hand_full = still.crop((wall_edge, 0, W, H))
    im.paste(hand_full, (wall_edge, 0))
    return im

flat = build_flat_composition()
flat.save("/tmp/out/step1_flat_composition.png")

def apply_gradient_backward_from_white(im):
    # baseline = white, anchored at the wall/hand edge (x = wall_edge). Working BACKWARD
    # (right-to-left) from that anchor toward black at the far left edge (x = 0).
    px = im.load()
    w, h = im.size
    plateau = 0.35 * wall_edge  # stays solid black for the leftmost stretch
    for x in range(wall_edge):
        if x <= plateau:
            k = 0.0  # fully black multiplier
        else:
            t = (x - plateau) / (wall_edge - plateau)
            k = t ** 1.6  # 0 (black) -> 1 (white/baseline) moving right, toward the anchor
        for y in range(h):
            r, g, b = px[x, y]
            # multiply the existing (black-on-white) pixel down toward black by (1-k), so white
            # text-background areas darken, and the dark text strokes stay relatively dark too,
            # everything converging smoothly to the white baseline at the anchor
            nr = int(r * k)
            ng = int(g * k)
            nb = int(b * k)
            px[x, y] = (nr, ng, nb)
    return im

graded = apply_gradient_backward_from_white(flat.copy())
graded.save("/tmp/out/wall_filled_still.png")
print("done", graded.size)

# --- animated version, same two-step process applied per frame ---
gif = Image.open("/tmp/out/arm_slides_from_wall_clean.gif")
frames, durations = [], []
try:
    while True:
        durations.append(gif.info.get("duration", 80))
        frame = gif.convert("RGB")
        base_flat = flat.copy()
        hand_area = frame.crop((wall_edge, 0, W, H))
        base_flat.paste(hand_area, (wall_edge, 0))
        graded_frame = apply_gradient_backward_from_white(base_flat)
        frames.append(graded_frame)
        gif.seek(gif.tell() + 1)
except EOFError:
    pass

frames[0].save("/tmp/out/wall_filled_animation.gif", save_all=True, append_images=frames[1:],
               duration=durations, optimize=False)
print("gif done", len(frames))
