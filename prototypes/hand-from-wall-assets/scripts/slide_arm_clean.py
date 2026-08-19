from PIL import Image
import numpy as np

img = Image.open("/tmp/out/original_v3_rotated_left_flipped_clean.png").convert("RGB")
arr = np.array(img)
W, H = img.size

col_ink = (arr != 255).any(axis=2).sum(axis=0).astype(float)
win = 15
kernel = np.ones(win) / win
smoothed = np.convolve(col_ink, kernel, mode="same")
dense_thresh = smoothed.max() * 0.35
wall_edge = 0
for x in range(win, W):
    if smoothed[x] < dense_thresh:
        wall_edge = x
        break

nonwhite_cols = np.where(col_ink > 0)[0]
full_right = nonwhite_cols.max() + 5

# vertical extent of the arm (rows containing content past the wall edge)
row_ink = (arr[:, wall_edge:full_right] != 255).any(axis=2).sum(axis=1)
nonwhite_rows = np.where(row_ink > 0)[0]
arm_top, arm_bot = nonwhite_rows.min(), nonwhite_rows.max()

pad = 4
arm_top = max(0, arm_top - pad)
arm_bot = min(H, arm_bot + pad)

# cut the arm out as its own sprite (everything right of the wall edge)
arm_sprite = img.crop((wall_edge, arm_top, full_right, arm_bot))
sprite_w, sprite_h = arm_sprite.size

# base = wall only, with the arm's original area whited out
base = img.copy()
white_patch = Image.new("RGB", (full_right - wall_edge, arm_bot - arm_top), "white")
base.paste(white_patch, (wall_edge, arm_top))

final_x = wall_edge          # arm's natural resting x position
start_x = wall_edge - sprite_w  # fully hidden behind the wall at the start

def frame_at(x, y_jitter=0):
    canvas = base.copy()
    canvas.paste(arm_sprite, (x, arm_top + y_jitter))
    # re-draw the wall on top so the wall stays visually in front where the arm is still behind it
    wall_strip = img.crop((0, 0, wall_edge, H))
    canvas.paste(wall_strip, (0, 0))
    return canvas

frames, durations = [], []
steps = 22

start_frame = frame_at(start_x)
frames += [start_frame]*4; durations += [180]*4

for i in range(steps+1):
    x = int(start_x + (final_x - start_x) * (i/steps))
    frames.append(frame_at(x)); durations.append(70)

# strong vibration right as the hand touches/settles into the white -- happens once, only here,
# nowhere else in the sequence. Sharp, decaying shake, then it comes to a dead stop. LOCKED.
shake_pattern = [8, -7, 6, -6, 5, -4, 3, -2, 1, 0]
for amt in shake_pattern:
    frames.append(frame_at(final_x, y_jitter=amt))
    durations.append(45)

final_frame = frame_at(final_x, y_jitter=0)
frames += [final_frame] * 20
durations += [150] * 20

frames[0].save("/tmp/out/arm_slides_from_wall_clean.gif", save_all=True, append_images=frames[1:],
               duration=durations, optimize=False)
print("OK", len(frames), "wall_edge", wall_edge, "sprite", sprite_w, sprite_h, "start_x", start_x)
