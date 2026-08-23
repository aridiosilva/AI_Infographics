"""Insert OCR descriptions immediately before slide images in a Markdown README.

Example:
    python src/add_slide_descriptions.py README.md src/slide_ocr.json
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

IMAGE_PATTERN = re.compile(
    r"(?m)^(?P<image>!\[(?P<label>[^\]]+)\]\(<(?P<path>[^>]+)>\))$"
)
DESCRIPTION_MARKER = "<!-- OCR-DESCRIPTION: {path} -->"
DESCRIPTION_PATTERN = re.compile(
    r"(?m)^<!-- OCR-DESCRIPTION: (?P<path>[^>]+) -->\n"
    r"\*\*(?P<label>[^*]+)\*\*: (?P<text>.+)\n\n"
)
LEGACY_DESCRIPTION_PATTERN = re.compile(
    r"(?m)^\*\*Slide \d+ — .+\*\*\n\n(?=!\[Slide \d+\]\(<)"
)


def normalize_text(text: str) -> str:
    """Convert OCR line breaks and repeated whitespace into one paragraph."""
    return re.sub(r"\s+", " ", text).strip()


def remove_previous_descriptions(markdown: str) -> str:
    """Make repeated executions idempotent by replacing prior managed blocks."""
    markdown = DESCRIPTION_PATTERN.sub("", markdown)
    return LEGACY_DESCRIPTION_PATTERN.sub("", markdown)


def add_descriptions(markdown: str, ocr_text: dict[str, str]) -> str:
    """Insert a managed OCR paragraph directly before every recognized image."""

    def replacement(match: re.Match[str]) -> str:
        image_path = match.group("path")
        text = normalize_text(ocr_text.get(image_path, ""))
        if not text:
            return match.group("image")

        label = match.group("label")
        marker = DESCRIPTION_MARKER.format(path=image_path)
        return f"{marker}\n**{label} — Conteúdo do slide:** {text}\n\n{match.group('image')}"

    return IMAGE_PATTERN.sub(replacement, remove_previous_descriptions(markdown))


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Insert OCR descriptions before Markdown slide images."
    )
    parser.add_argument("readme", type=Path, help="Markdown file containing images.")
    parser.add_argument("ocr_json", type=Path, help="JSON produced by extract_slide_ocr.py.")
    args = parser.parse_args()

    markdown = args.readme.read_text(encoding="utf-8")
    ocr_text = json.loads(args.ocr_json.read_text(encoding="utf-8"))
    if not isinstance(ocr_text, dict) or not all(
        isinstance(path, str) and isinstance(text, str)
        for path, text in ocr_text.items()
    ):
        parser.error("OCR JSON must be an object mapping image paths to text.")

    updated = add_descriptions(markdown, ocr_text)
    args.readme.write_text(updated, encoding="utf-8")
    print(f"Updated {args.readme} with OCR descriptions.")


if __name__ == "__main__":
    main()
