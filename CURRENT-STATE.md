# INVOICE — Current State

## Authoritative checkpoint

- **Build:** b17.28
- **Android versionCode:** 1728
- **App ID:** `com.bill.invoice`
- **App name:** `INVOICE`
- **Checkpoint recorded:** 2026-08-31

The authoritative b17.28 project is the local archive:

`invoice-apk-project_b17.28.zip`

- Size: 6,520,349 bytes
- SHA-256: `5d8cb5b023b6d90de22e144b7a68e5750664be58cfa5095c22db6f9d42e5dad5`

The authoritative b17.28 book source (`www/index.html`) is:

- Size: 312,476 bytes
- SHA-256: `c6aff53f498c7a1bca6f6b158ee39c585009dafee4fee30f2ab22c07a3906d3d`

## Important repository rule

The existing GitHub `app/` directory predates b17.28 and is **historical**, not the current source of truth. Do not rebuild b17.28 from `app/` as currently checked in.

This checkpoint records the current native wrapper and the exact identity of the local b17.28 master without partially replacing the book with an incomplete GitHub copy.

## What b17.28 contains

The book now runs the complete 52-page progression, including the crate, babble, fever, NO, hole, collapse, hand, sound/haptics, orientation behavior, Android lifecycle behavior, and final white endpoint.

## Local runtime assets

The audio masters, current `hand.gif`, and exact packaged archive are intentionally kept with the local b17.28 master. Their filenames, byte sizes, and SHA-256 hashes are recorded in `LOCAL-ASSETS.md`.

## Repository layout added by this checkpoint

- `CURRENT-STATE.md` — source-of-truth declaration
- `LOCAL-ASSETS.md` — exact manifest for local binary media
- `mobile-source/` — maintenance-relevant Capacitor/Android wrapper from b17.28
- `scripts/verify-b17.28.mjs` — verifies the checkpoint metadata and optionally a local b17.28 archive/source

## Source-of-truth rule

Older APK ZIPs, the older `app/` implementation, and notes such as `WIRED-2026-08-23.md` remain useful project history. They do not supersede b17.28.

Do not refactor or split the book merely for conventional software organization. Preserve the working artifact first; polish should be deliberate and tested against the phone experience.
