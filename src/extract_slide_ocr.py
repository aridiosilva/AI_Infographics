"""Extract text from slide images with local OCR.

Example:
    python src/extract_slide_ocr.py SLIDES --output src/slide_ocr.json
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

from rapidocr_onnxruntime import RapidOCR

IMAGE_SUFFIXES = {".jpeg", ".jpg", ".png", ".webp"}


def natural_key(path: Path) -> list[int | str]:
    """Sort files by name while keeping numbered slides in numeric order."""
    return [
        int(part) if part.isdigit() else part.casefold()
        for part in re.split(r"(\d+)", path.as_posix())
    ]


def extract_text(result: list[Any] | None) -> str:
    """Join recognized OCR lines into a readable text block."""
    if not result:
        return ""

    return "\n".join(item[1].strip() for item in result if item[1].strip())


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Extract local OCR text from infographic slide images."
    )
    parser.add_argument("slides_dir", type=Path, help="Directory containing slide images.")
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("slide_ocr.json"),
        help="JSON file to create with OCR output.",
    )
    args = parser.parse_args()

    slides_dir = args.slides_dir.resolve()
    if not slides_dir.is_dir():
        parser.error(f"Slide directory does not exist: {slides_dir}")

    images = sorted(
        (
            path
            for path in slides_dir.rglob("*")
            if path.is_file() and path.suffix.casefold() in IMAGE_SUFFIXES
        ),
        key=lambda path: natural_key(path.relative_to(slides_dir)),
    )
    engine = RapidOCR()
    extracted: dict[str, str] = {}

    for image in images:
        result, _ = engine(str(image))
        extracted[image.relative_to(slides_dir.parent).as_posix()] = extract_text(result)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(extracted, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"Extracted OCR text from {len(extracted)} images to {args.output}.")


if __name__ == "__main__":
    main()
