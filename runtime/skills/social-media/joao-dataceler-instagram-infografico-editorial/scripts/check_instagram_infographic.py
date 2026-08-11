#!/usr/bin/env python3
"""Mechanical checks for a single-image Instagram infographic.

Visual QA is still required after this script passes.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from PIL import Image

EXPECTED_SIZE = (1080, 1350)
THUMB_SIZE = (270, 338)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("image", type=Path)
    parser.add_argument("--thumbnail", type=Path)
    parser.add_argument("--create-thumbnail", action="store_true")
    args = parser.parse_args()

    failures: list[str] = []
    if not args.image.exists():
        failures.append("image_not_found")
        print(json.dumps({"ok": False, "failures": failures}))
        return 1

    with Image.open(args.image) as image:
        size = image.size
        mode = image.mode
        extrema = image.convert("RGB").getextrema()
        if size != EXPECTED_SIZE:
            failures.append(f"wrong_size:{size[0]}x{size[1]}")
        if mode != "RGB":
            failures.append(f"wrong_mode:{mode}")
        if all(low == high for low, high in extrema):
            failures.append("uniform_image")

        thumb_path = args.thumbnail
        if args.create_thumbnail and thumb_path is None:
            thumb_path = args.image.with_name(args.image.stem + "-mobile.png")
        if args.create_thumbnail and thumb_path is not None:
            thumb = image.convert("RGB").resize(THUMB_SIZE, Image.Resampling.LANCZOS)
            thumb.save(thumb_path, optimize=True)

    if args.thumbnail is not None and not args.create_thumbnail:
        if not args.thumbnail.exists():
            failures.append("thumbnail_not_found")
        else:
            with Image.open(args.thumbnail) as thumb:
                if thumb.size != THUMB_SIZE:
                    failures.append(f"wrong_thumbnail_size:{thumb.width}x{thumb.height}")

    result = {
        "ok": not failures,
        "image": str(args.image),
        "size": list(size),
        "mode": mode,
        "thumbnail": str(thumb_path) if thumb_path else None,
        "failures": failures,
        "visual_qa_still_required": True,
    }
    print(json.dumps(result, ensure_ascii=False))
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
