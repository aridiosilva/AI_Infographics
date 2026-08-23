"""Resize Markdown slide images rendered in a README.

Example:
    python src/resize_readme_images.py README.md --width-percent 75
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

MARKDOWN_IMAGE_PATTERN = re.compile(
    r"(?m)^(?P<image>!\[(?P<alt>[^\]]*)\]\(<(?P<src>[^>]+)>\))$"
)
HTML_IMAGE_PATTERN = re.compile(
    r'(?m)^<img src="(?P<src>[^"]+)" alt="(?P<alt>[^"]*)" '
    r'width="\d+%" loading="lazy">$'
)


def render_image(source: str, alt: str, width_percent: int) -> str:
    """Render a proportional HTML image accepted by GitHub Markdown."""
    return (
        f'<img src="{source}" alt="{alt}" width="{width_percent}%" '
        'loading="lazy">'
    )


def resize_images(markdown: str, width_percent: int) -> str:
    """Convert Markdown images and update previously resized HTML images."""

    def markdown_replacement(match: re.Match[str]) -> str:
        return render_image(match.group("src"), match.group("alt"), width_percent)

    def html_replacement(match: re.Match[str]) -> str:
        return render_image(match.group("src"), match.group("alt"), width_percent)

    markdown = MARKDOWN_IMAGE_PATTERN.sub(markdown_replacement, markdown)
    return HTML_IMAGE_PATTERN.sub(html_replacement, markdown)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Resize slide images rendered in a Markdown README."
    )
    parser.add_argument("readme", type=Path, help="Markdown file to update.")
    parser.add_argument(
        "--width-percent",
        type=int,
        default=75,
        help="Rendered image width as a percentage of the available width.",
    )
    args = parser.parse_args()

    if not 1 <= args.width_percent <= 100:
        parser.error("--width-percent must be between 1 and 100.")

    markdown = args.readme.read_text(encoding="utf-8")
    updated = resize_images(markdown, args.width_percent)
    args.readme.write_text(updated, encoding="utf-8")
    print(f"Updated image width to {args.width_percent}% in {args.readme}.")


if __name__ == "__main__":
    main()
