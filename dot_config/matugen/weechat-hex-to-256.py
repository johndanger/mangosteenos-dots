#!/usr/bin/env python3
"""Convert #rrggbb hex colors in a WeeChat .theme file to xterm-256 indices."""

import re
import sys

# xterm-256 color table: indices 16-231 are a 6x6x6 color cube,
# indices 232-255 are a grayscale ramp.
_CUBE = [0, 0x5f, 0x87, 0xaf, 0xd7, 0xff]


def _build_palette():
    colors = []
    # 0-15: system colors (skip, unreliable)
    # 16-231: 6x6x6 color cube
    for r in _CUBE:
        for g in _CUBE:
            for b in _CUBE:
                colors.append((r, g, b))
    # 232-255: grayscale ramp
    for i in range(24):
        v = 8 + i * 10
        colors.append((v, v, v))
    return colors  # indices 0..215 map to xterm 16..231, then 216..239 -> 232..255


_PALETTE = _build_palette()  # 216 + 24 = 240 entries, offset by 16


def hex_to_256(hex_color):
    hex_color = hex_color.lstrip('#')
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)

    best_idx = 16
    best_dist = float('inf')
    for i, (pr, pg, pb) in enumerate(_PALETTE):
        dist = (r - pr) ** 2 + (g - pg) ** 2 + (b - pb) ** 2
        if dist < best_dist:
            best_dist = dist
            best_idx = i + 16
    return str(best_idx)


def convert_line(line):
    # Skip lines with inline ${color:...} format strings — hex is valid there
    if '${color:' in line:
        return line
    return re.sub(r'#[0-9a-fA-F]{6}', lambda m: hex_to_256(m.group(0)), line)


def convert_file(path):
    with open(path, 'r') as f:
        lines = f.readlines()

    result = [convert_line(line) for line in lines]

    with open(path, 'w') as f:
        f.writelines(result)


if __name__ == '__main__':
    convert_file(sys.argv[1])
