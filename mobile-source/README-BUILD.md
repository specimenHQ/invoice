# INVOICE b17.28 — Mobile Wrapper

This directory records the maintenance-relevant Capacitor/Android wrapper from the current b17.28 build.

It is intentionally **not** a replacement for the exact local project archive. The archive remains the recoverable packaged checkpoint because it contains the full Gradle/Capacitor scaffolding, current `www/index.html`, media, lockfile, resources, and generated support files.

## Identity

- appId: `com.bill.invoice`
- appName: `INVOICE`
- Android versionCode: `1728`
- Android versionName: `b17.28`
- Capacitor webDir: `www`

## Native behavior preserved here

`MainActivity.java` contains the b17.28 immersive/fullscreen behavior, keep-screen-on rule, and the deliberate-leave lifecycle rule: interruptions do not reset the book, but a deliberate Home/app-switcher exit causes the WebView to reload when the reader returns.

## Rebuild authority

Start from the local archive whose SHA-256 is recorded in `../CURRENT-STATE.md`. Do not assume the older GitHub `app/` directory is b17.28.

When a future build is promoted, update the version metadata and checkpoint docs together. Do not silently mutate b17.28.
