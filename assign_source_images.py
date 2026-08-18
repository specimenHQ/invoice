#!/usr/bin/env python3
"""
Bulk-assign source_image in invoice-book-1-panel-prompt-grid.csv based on
board_geometry, using the 6-image shot list (see invoice-book-1-shot-list.md).

Usage:
    python3 assign_source_images.py

Edit GEOMETRY_TO_IMAGE below once you've actually shot/sourced the images and
saved them under reference-images/ with these names (or change the names to
match what you actually saved).
"""
import csv
import os

CSV_PATH = os.path.join(os.path.dirname(__file__), 'invoice-book-1-panel-prompt-grid.csv')

GEOMETRY_TO_IMAGE = {
    'empty field':                    'reference-images/src-empty-field.jpg',
    'diagonal pressure':              'reference-images/src-diagonal-pressure.jpg',
    'dense cluster':                  'reference-images/src-dense-cluster.jpg',
    'horizontal seam':                'reference-images/src-horizontal-seam.jpg',
    'stepped threshold':              'reference-images/src-stepped-threshold.jpg',
    'diagonal pressure to direction': 'reference-images/src-diagonal-pressure-direction.jpg',
}

PAGE52_PHOTO = 'reference-images/src-page52-reveal.jpg'


def main():
    with open(CSV_PATH, encoding='utf-8-sig', newline='') as f:
        rows = list(csv.DictReader(f))
    fieldnames = list(rows[0].keys())

    updated = 0
    for r in rows:
        if r['render_mode'] == 'mark':
            continue  # no image needed
        if r['render_mode'] == 'photo':
            r['source_image'] = PAGE52_PHOTO
            updated += 1
            continue
        img = GEOMETRY_TO_IMAGE.get(r['board_geometry'])
        if img:
            r['source_image'] = img
            updated += 1

    with open(CSV_PATH, 'w', newline='', encoding='utf-8-sig') as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
        w.writeheader()
        w.writerows(rows)

    print(f"Assigned source_image on {updated} rows.")
    print("Now save your actual shot-list images under reference-images/ with")
    print("the filenames above (or edit GEOMETRY_TO_IMAGE to match what you saved),")
    print("then run: python3 render_panels.py --dry-run")


if __name__ == '__main__':
    main()
