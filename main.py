#!/usr/bin/env python3
"""Entrypoint for news-image-20261120.

The front page is rendered by render-20261120.py (stdlib + Pillow only)
and bundled here as entry.png. This program copies that bundled image to
the harness output directory: $MAKEFUN_OUTPUT_DIR/entry.png, or ./entry.png
when the variable is unset.
"""
import os
import shutil
import sys


def main():
    root = os.path.dirname(os.path.abspath(__file__))
    bundled = os.path.join(root, "entry.png")
    if not os.path.exists(bundled):
        sys.stderr.write("bundled entry.png not found\n")
        sys.exit(1)
    target_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", ".")
    os.makedirs(target_dir, exist_ok=True)
    target = os.path.join(target_dir, "entry.png")
    shutil.copyfile(bundled, target)
    size = os.path.getsize(target)
    print("copied entry.png to", target, size, "bytes")


if __name__ == "__main__":
    main()
