#!/usr/bin/env python3
"""Fail if tracked content contains data that must not be published.

Checks (text files): real GUIDs, unexpected emails, employer name, key/secret
shapes, literal passwords. Checks (images): EXIF/XMP/text metadata.

Usage: python scripts/check_sensitive.py [paths...]   (default: all tracked files)
Allow a line deliberately with the marker  sensitive-ok  on it.
"""
import re
import struct
import subprocess
import sys
from pathlib import Path

ZERO_GUID = "00000000-0000-0000-0000-000000000000"
ALLOWED_EMAILS = {"anjkeesari@gmail.com", "user@example.com", "noreply@github.com",
                  "noreply@anthropic.com"}
ALLOWED_EMAIL_DOMAINS = ("example.com", "example.org", "contoso.com")
TEXT_EXT = {".md", ".yml", ".yaml", ".html", ".css", ".js", ".json", ".txt", ".toml",
            ".py", ".ps1", ".sh", ".tf", ".cfg"}
SKIP_FILES = {"scripts/check_sensitive.py", "LICENSE"}

GUID = re.compile(r"\b[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\b")
EMAIL = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,}")
PATTERNS = {
    "employer name": re.compile(r"assetmark", re.I),
    "storage/SAS-style key": re.compile(r"(?<![A-Za-z0-9+/])[A-Za-z0-9+/]{86}==(?![A-Za-z0-9+/=])"),
    "Azure AD client secret": re.compile(r"(?<![A-Za-z0-9_.~-])[A-Za-z0-9_.~-]{3}8Q~[A-Za-z0-9_.~-]{20,}"),
    "connection-string key": re.compile(r"(SharedAccessKey|AccountKey)=(?!replaceme)[A-Za-z0-9+/=]{20,}"),
    "private key": re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
    "GitHub token": re.compile(r"\bgh[pousr]_[A-Za-z0-9]{30,}"),
}
PASSWORD = re.compile(r"""(?i)\b(password|passwd|pwd|client[_-]?secret|secret[_-]?key)\b["']?\s*[:=]\s*["']?([^\s"',;)]+)""")
PASSWORD_OK = re.compile(r"(?i)^(replaceme|<.*>|\$.*|var\..*|random_.*|azurerm_.*|data\..*|local\..*|"
                         r"example|xxx+|\*+|•+|null|true|false|\{.*|\[.*|your-.*|value|string|.*\(.*|"
                         r"mypassword|strong@passw0rd|yourstrongpassword|password|keycloak|changeme|[A-Z][A-Z_]+)$")


def tracked_files():
    out = subprocess.check_output(["git", "ls-files", "-z"], text=True)
    return [p for p in out.split("\0") if p]


def check_text(path, text):
    problems = []
    for n, line in enumerate(text.splitlines(), 1):
        if "sensitive-ok" in line:
            continue
        for g in GUID.findall(line):
            if g != ZERO_GUID:
                problems.append((n, "GUID (use all-zero GUID)", g))
        for e in EMAIL.findall(line):
            low = e.lower()
            if low in ALLOWED_EMAILS or low.endswith(tuple("@" + d for d in ALLOWED_EMAIL_DOMAINS)):
                continue
            if re.search(r"\.(png|jpg|jpeg|svg|gif|ico|css|js|webp)$", low) or "@" in low and low.split("@")[0] in ("", "types"):
                continue
            problems.append((n, "email address", e))
        for label, rx in PATTERNS.items():
            if rx.search(line):
                problems.append((n, label, "(redacted)"))
        for m in PASSWORD.finditer(line):
            if not PASSWORD_OK.match(m.group(2)):
                problems.append((n, "literal password/secret (use replaceme)", m.group(0)[:60]))
    return problems


def jpeg_metadata(data):
    found, i = [], 2
    while i + 4 <= len(data) and data[i] == 0xFF:
        marker = data[i + 1]
        if marker == 0xDA:
            break
        if marker == 0xFF:
            i += 1
            continue
        if 0xD0 <= marker <= 0xD9 or marker == 0x01:
            i += 2
            continue
        (length,) = struct.unpack(">H", data[i + 2:i + 4])
        if marker in (0xE1, 0xED, 0xFE):
            found.append({0xE1: "EXIF/XMP", 0xED: "APP13", 0xFE: "comment"}[marker])
        i += 2 + length
    return found


def png_metadata(data):
    found, i = [], 8
    while i + 8 <= len(data):
        (length,) = struct.unpack(">I", data[i:i + 4])
        ctype = data[i + 4:i + 8].decode("latin1")
        if ctype in ("tEXt", "iTXt", "zTXt", "eXIf"):
            found.append(ctype)
        if ctype == "IDAT":
            pass
        i += 12 + length
    return found


def check_image(path, data):
    if data[:2] == b"\xff\xd8":
        kinds = jpeg_metadata(data)
    elif data[:8] == b"\x89PNG\r\n\x1a\n":
        kinds = png_metadata(data)
    else:
        return []
    return [(0, "image metadata (strip it)", ", ".join(sorted(set(kinds))))] if kinds else []


def main(argv):
    files = argv or tracked_files()
    bad = 0
    for f in files:
        if f.replace("\\", "/") in SKIP_FILES:
            continue
        p = Path(f)
        if not p.is_file():
            continue
        ext = p.suffix.lower()
        if ext in TEXT_EXT:
            problems = check_text(f, p.read_text(encoding="utf-8", errors="ignore"))
        elif ext in (".jpg", ".jpeg", ".png"):
            problems = check_image(f, p.read_bytes())
        else:
            continue
        for line, kind, detail in problems:
            bad += 1
            where = f"{f}:{line}" if line else f
            print(f"{where}: {kind}: {detail}")
    if bad:
        print(f"\n{bad} problem(s). Replace secrets with 'replaceme', IDs with {ZERO_GUID}.")
        return 1
    print("check_sensitive: OK")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
