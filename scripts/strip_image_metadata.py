#!/usr/bin/env python3
"""Losslessly remove EXIF/XMP/text metadata (author, device, software) from images.

Usage: python scripts/strip_image_metadata.py [files...]   (default: all tracked .jpg/.jpeg/.png)
JPEG: drops APP1 (EXIF/XMP), APP13, COM segments. PNG: drops tEXt/iTXt/zTXt/eXIf chunks.
Pixels are never re-encoded.
"""
import struct
import subprocess
import sys
from pathlib import Path

JPEG_DROP = {0xE1, 0xED, 0xFE}
PNG_DROP = {b"tEXt", b"iTXt", b"zTXt", b"eXIf"}


def strip_jpeg(data):
    out, i = bytearray(b"\xff\xd8"), 2
    while i < len(data):
        if data[i] != 0xFF:
            out += data[i:]
            break
        marker = data[i + 1]
        if marker == 0xDA:
            out += data[i:]
            break
        if marker == 0xFF:
            i += 1
            continue
        if 0xD0 <= marker <= 0xD9 or marker == 0x01:
            out += data[i:i + 2]
            i += 2
            continue
        (length,) = struct.unpack(">H", data[i + 2:i + 4])
        if marker not in JPEG_DROP:
            out += data[i:i + 2 + length]
        i += 2 + length
    return bytes(out)


def strip_png(data):
    out, i = bytearray(data[:8]), 8
    while i + 8 <= len(data):
        (length,) = struct.unpack(">I", data[i:i + 4])
        end = i + 12 + length
        if data[i + 4:i + 8] not in PNG_DROP:
            out += data[i:end]
        i = end
    return bytes(out)


def strip(data):
    if data[:2] == b"\xff\xd8":
        return strip_jpeg(data)
    if data[:8] == b"\x89PNG\r\n\x1a\n":
        return strip_png(data)
    return data


def main(argv):
    files = argv or [f for f in subprocess.check_output(["git", "ls-files", "-z"], text=True).split("\0")
                     if f.lower().endswith((".jpg", ".jpeg", ".png"))]
    changed = 0
    for f in files:
        p = Path(f)
        original = p.read_bytes()
        cleaned = strip(original)
        if cleaned != original:
            p.write_bytes(cleaned)
            changed += 1
    print(f"stripped metadata from {changed} of {len(files)} images")


if __name__ == "__main__":
    main(sys.argv[1:])
