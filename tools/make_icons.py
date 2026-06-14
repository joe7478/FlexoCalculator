#!/usr/bin/env python3
"""Generate app icons (pure stdlib, no dependencies).

Draws a printing-themed icon: dark background with four CMYK bars and a
subtle highlight. Exports the PNG sizes referenced by the PWA manifest and
the Apple home-screen icon.
"""
import struct
import zlib
import os

OUT_DIR = os.path.join(os.path.dirname(__file__), "..", "icons")

# Palette
BG = (15, 23, 32)          # dark slate
CYAN = (0, 174, 239)
MAGENTA = (236, 0, 140)
YELLOW = (255, 222, 23)
KEY = (43, 52, 63)         # "black" channel, lightened so it reads on dark bg


def lerp(a, b, t):
    return tuple(round(a[i] + (b[i] - a[i]) * t) for i in range(3))


def make_png(size):
    bars = [CYAN, MAGENTA, YELLOW, KEY]
    # Bars occupy the central band; rounded mask is applied by iOS.
    margin = round(size * 0.16)
    band_top = round(size * 0.30)
    band_bot = round(size * 0.70)
    inner_w = size - 2 * margin
    bar_gap = round(size * 0.025)
    bar_w = (inner_w - bar_gap * 3) // 4

    raw = bytearray()
    for y in range(size):
        raw.append(0)  # filter type 0 for each scanline
        # vertical gradient background
        t = y / max(1, size - 1)
        bg = lerp(BG, (24, 34, 46), t)
        for x in range(size):
            px = bg
            if band_top <= y < band_bot and margin <= x < margin + inner_w:
                rel = x - margin
                idx = rel // (bar_w + bar_gap)
                within = rel - idx * (bar_w + bar_gap)
                if 0 <= idx < 4 and within < bar_w:
                    px = bars[idx]
            raw.extend(px)

    compressed = zlib.compress(bytes(raw), 9)

    def chunk(typ, data):
        c = struct.pack(">I", len(data)) + typ + data
        return c + struct.pack(">I", zlib.crc32(typ + data) & 0xFFFFFFFF)

    sig = b"\x89PNG\r\n\x1a\n"
    ihdr = struct.pack(">IIBBBBB", size, size, 8, 2, 0, 0, 0)  # 8-bit RGB
    return sig + chunk(b"IHDR", ihdr) + chunk(b"IDAT", compressed) + chunk(b"IEND", b"")


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    targets = {
        "icon-192.png": 192,
        "icon-512.png": 512,
        "apple-touch-icon.png": 180,
    }
    for name, size in targets.items():
        path = os.path.join(OUT_DIR, name)
        with open(path, "wb") as f:
            f.write(make_png(size))
        print("wrote", os.path.relpath(path))


if __name__ == "__main__":
    main()
