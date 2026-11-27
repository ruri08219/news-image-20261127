#!/usr/bin/env python3
"""Entrypoint for the 27 November 2026 news front-page entry.

The entry is one flat-drawn front-page image holding 41 date-checked
stories from Friday 27 November 2026. This program does a single job:
it reads the bundled image, checks it against the size and SHA-256
fingerprint recorded when the page was reviewed, and writes a verified
copy to ``$MAKEFUN_OUTPUT_DIR/entry.png`` (falling back to
``out/entry.png`` when that variable is unset).

Only the Python standard library is used: hashlib, os, shutil, sys
and pathlib. Nothing is downloaded and nothing is drawn at run time;
the finished image ships in the repository next to this file.
"""

import hashlib
import os
import sys
from pathlib import Path

IMAGE_NAME = "entry.png"
EXPECTED_BYTES = 184124
EXPECTED_SHA256 = (
    "79a03f8a06a65e536256e3c565947a5e7768620f51ab60274edd17da3718da26"
)


def abort(message):
    """Print a problem to stderr and exit non-zero."""
    print(f"error: {message}", file=sys.stderr)
    raise SystemExit(1)


def read_and_check(source):
    """Read the bundled image and verify size and digest.

    Returns the verified bytes. Any mismatch means the file on disk is
    not the reviewed entry, so the run stops instead of emitting it.
    """
    if not source.is_file():
        abort(f"{IMAGE_NAME} is missing next to {source.parent}")

    data = source.read_bytes()

    if data[:8] != b"\x89PNG\r\n\x1a\n":
        abort(f"{IMAGE_NAME} is not a PNG file (bad magic bytes)")

    if len(data) != EXPECTED_BYTES:
        abort(f"{IMAGE_NAME} is {len(data)} bytes, expected {EXPECTED_BYTES}")

    digest = hashlib.sha256(data).hexdigest()
    if digest != EXPECTED_SHA256:
        abort(f"{IMAGE_NAME} sha256 mismatch: got {digest}")

    return data, digest


def copy_to_output(data, destination):
    """Write the verified bytes to the output path, creating folders."""
    destination.parent.mkdir(parents=True, exist_ok=True)
    with open(destination, "wb") as handle:
        handle.write(data)
    return destination


def output_path():
    """Resolve the destination from the environment, defaulting to out/."""
    base = os.environ.get("MAKEFUN_OUTPUT_DIR") or "out"
    return Path(base) / IMAGE_NAME


def main():
    here = Path(__file__).resolve().parent
    data, digest = read_and_check(here / IMAGE_NAME)

    if "--verify-only" in sys.argv[1:]:
        print(f"ok: {IMAGE_NAME} verified "
              f"({len(data)} bytes, sha256 {digest})")
        return 0

    target = copy_to_output(data, output_path())
    print(f"ok: wrote {target} ({len(data)} bytes, sha256 {digest})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
