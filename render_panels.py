#!/usr/bin/env python3
"""
Batch-render Book 1 panels from invoice-book-1-panel-prompt-grid.csv.

Reads each row's render_mode / jp2a_width / jp2a_chars / source_image settings
and produces a text (or marker) render for that panel using jp2a, writing
output into rendered_panels/<absolute_panel>-<panel_id>.txt

Usage:
    python3 render_panels.py                # render everything with a source_image set
    python3 render_panels.py --panel 313     # render one panel by absolute_panel number
    python3 render_panels.py --dry-run       # show what would run, don't call jp2a

Requires: jp2a installed (apt-get install jp2a / brew install jp2a)
"""
import csv
import subprocess
import argparse
import os
import sys

CSV_PATH = os.path.join(os.path.dirname(__file__), 'invoice-book-1-panel-prompt-grid.csv')
OUT_DIR = os.path.join(os.path.dirname(__file__), 'rendered_panels')


def load_rows():
    with open(CSV_PATH, encoding='utf-8-sig', newline='') as f:
        return list(csv.DictReader(f))


def render_row(row, dry_run=False):
    mode = row['render_mode']
    abs_p = row['absolute_panel']
    pid = row['panel_id']
    out_path = os.path.join(OUT_DIR, f"{abs_p}-{pid}.txt")

    if mode == 'mark':
        content = "."  # single mark, no image needed
        if not dry_run:
            with open(out_path, 'w') as f:
                f.write(content)
        return f"[mark] {pid} -> literal mark, no jp2a needed"

    if mode == 'photo':
        note = row.get('curation_notes', '')
        return f"[photo] {pid} -> HARD CUT: real photograph, no ASCII. ({note})"

    # ascii-sparse / ascii-medium / ascii-dense / single-letter / binary all go through jp2a
    src = row.get('source_image', '').strip()
    if not src:
        return f"[SKIP] {pid} -> render_mode={mode} but no source_image set yet"

    if not os.path.exists(src):
        return f"[MISSING] {pid} -> source_image not found: {src}"

    width = row.get('jp2a_width', '') or '60'
    chars = row.get('jp2a_chars', '').strip()

    cmd = ['jp2a', f'--width={width}']
    if chars:
        cmd.append(f'--chars={chars}')
    cmd.append(src)

    if dry_run:
        return f"[DRY] {pid} -> {' '.join(cmd)}"

    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        return f"[ERROR] {pid} -> {result.stderr.strip()}"

    with open(out_path, 'w') as f:
        f.write(result.stdout)
    return f"[ok] {pid} -> {out_path} ({len(result.stdout.splitlines())} lines)"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--panel', type=str, default=None, help='Render only this absolute_panel number')
    ap.add_argument('--dry-run', action='store_true')
    args = ap.parse_args()

    os.makedirs(OUT_DIR, exist_ok=True)
    rows = load_rows()

    if args.panel:
        rows = [r for r in rows if r['absolute_panel'] == args.panel]
        if not rows:
            print(f"No panel with absolute_panel={args.panel}")
            sys.exit(1)

    for row in rows:
        print(render_row(row, dry_run=args.dry_run))


if __name__ == '__main__':
    main()
