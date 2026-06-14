# Flexo Calculator

A self-contained flexographic printing calculator for the iPhone (or any phone/computer).
**No internet, no server, no deploy** — the whole app is a single file: `index.html`.

## What it does

| Tab | Solves |
|-----|--------|
| **Repeat** | Print repeat & cylinder size from gear teeth — and the reverse |
| **Distortion** | Plate shrinkage / distortion factor & distorted artwork length |
| **Anilox** | Anilox volume (BCM), ink mileage (ft²/gal, ft²/lb) and job ink (gal, lb) |
| **Dot Gain** | Tone value increase (TVI) |
| **Screen** | Recommended anilox line count (lpi) |
| **Production** | Impressions/min & hr, run time, material length |
| **Convert** | in / count / mil / ft length converter |

All measurements are in **inches** (a **count** = 10 in). Every tab remembers
your last inputs and shows the formula used.

## Put it on your iPhone (no deploy)

1. Save `index.html` to your phone — AirDrop it, email it to yourself, or drop it
   in **iCloud Drive / Files**.
2. Open it in **Safari** (tap the file in the Files app → it opens in the browser).
3. Optional: tap **Share → Add to Home Screen** to get the app icon.

It runs entirely offline because everything (styles, logic, icon) is embedded in
the one file.

## Optional: host it later

If you ever want a real home-screen app icon and tap-to-launch behavior, you can
host `index.html` anywhere static (e.g. GitHub Pages). The `icons/` folder and
`tools/make_icons.py` (the icon generator) are included for that case but are not
needed for normal offline use.

## Disclaimer

Formulas are industry standard but defaults/assumptions (e.g. distortion measured
across full plate + tape caliper, 1 BCM/in² = 1.55 cm³/m²) should be sanity-checked
against your own shop standards.
