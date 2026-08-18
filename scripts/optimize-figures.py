# /// script
# requires-python = ">=3.9"
# dependencies = ["pymupdf"]
# ///
"""Optimize the PDFs in figures/ in place.

Applies the techniques described in
https://artifex.com/blog/optimizing-pdf-file-size-with-pymupdf-three-essential-techniques

1. subset_fonts() keeps only the glyphs each embedded font actually uses
2. scrub() strips metadata, thumbnails, attachments and other dead weight
3. rewrite_images() downsamples rasters to a medium DPI target, opt in via
   --downsample-images

The file is then written with garbage collection, deflation and object streams so
removed objects are physically purged rather than merely unreferenced.

Image downsampling is off by default because it does not pay for itself on this
figure set. Only one figure carries rasters and they are 300 DPI text labels, so
the medium pass saved 5 bytes while halving their resolution. It is also the one
pass that can corrupt a figure. rewrite_images() turns some shaded vector fills
black in Figma and matplotlib output, so when it is enabled a figure whose
rendering changes falls back to the lossless passes.

Every result is rendered and compared against the original before it is accepted,
and a figure is only replaced when the optimized version is genuinely smaller.
Rerunning the script is therefore safe and converges.

Run with:

    uv run scripts/optimize-figures.py
    uv run scripts/optimize-figures.py --downsample-images
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import pymupdf

FIGURES = Path(__file__).resolve().parent.parent / "figures"

# Medium resolution. Rasters at or below the threshold are left untouched, higher
# resolution ones come down to 150 DPI, which stays sharp in print without
# carrying full 300 DPI weight.
DPI_THRESHOLD = 225
DPI_TARGET = 150
JPEG_QUALITY = 85

# Verification. Pages are rendered at this DPI and compared pixel by pixel. The
# lossless passes are exactly identical, so anything above a rounding-level
# fraction means the optimization altered the figure.
CHECK_DPI = 150
CHANNEL_TOLERANCE = 8
MAX_CHANGED_FRACTION = 0.0005

SCRUB = dict(
    metadata=True,
    xml_metadata=True,
    attached_files=True,
    embedded_files=True,
    thumbnails=True,
    reset_fields=True,
    reset_responses=True,
)

# garbage=4 also deduplicates identical objects, which ez_save (garbage=3) skips.
SAVE = dict(garbage=4, deflate=True, use_objstms=True, clean=True)


def build(path: Path, downsample: bool) -> bytes:
    """Return an optimized copy of path as PDF bytes."""
    doc = pymupdf.open(path)
    try:
        if downsample:
            doc.rewrite_images(
                dpi_threshold=DPI_THRESHOLD,
                dpi_target=DPI_TARGET,
                quality=JPEG_QUALITY,
                lossy=True,
                lossless=True,
                bitonal=False,  # 1-bit art degrades badly under JPEG, leave it alone
                color=True,
                gray=True,
                set_to_gray=False,  # keep colour, these figures rely on it
            )
        # Both of these must run once, immediately before saving.
        doc.subset_fonts()
        doc.scrub(**SCRUB)
        return doc.tobytes(**SAVE)
    finally:
        doc.close()


def render(source) -> list:
    """Render every page to greyscale samples for comparison."""
    doc = pymupdf.open(source) if isinstance(source, Path) else pymupdf.open("pdf", source)
    try:
        return [
            page.get_pixmap(dpi=CHECK_DPI, colorspace=pymupdf.csGRAY).samples
            for page in doc
        ]
    finally:
        doc.close()


def renders_identically(reference: list, candidate: bytes) -> bool:
    pages = render(candidate)
    if len(pages) != len(reference):
        return False
    for before, after in zip(reference, pages):
        if len(before) != len(after):
            return False
        changed = sum(1 for a, b in zip(before, after) if abs(a - b) > CHANNEL_TOLERANCE)
        if changed > len(before) * MAX_CHANGED_FRACTION:
            return False
    return True


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--downsample-images",
        action="store_true",
        help=f"also downsample rasters above {DPI_THRESHOLD} DPI to {DPI_TARGET} DPI",
    )
    args = parser.parse_args()

    pdfs = sorted(FIGURES.glob("*.pdf"))
    if not pdfs:
        sys.exit(f"no PDFs found in {FIGURES}")

    # With downsampling requested, try it first and fall back to the lossless
    # passes when it alters the rendering.
    attempts = (True, False) if args.downsample_images else (False,)

    before_total = after_total = 0
    for pdf in pdfs:
        before = pdf.stat().st_size
        reference = render(pdf)

        data = None
        note = ""
        for downsample in attempts:
            candidate = build(pdf, downsample=downsample)
            if renders_identically(reference, candidate):
                data = candidate
                note = "no image pass" if args.downsample_images and not downsample else ""
                break

        if data is None:
            after, status = before, "skipped, alters rendering"
        elif len(data) >= before:
            after, status = before, "already minimal"
        else:
            pdf.write_bytes(data)
            after = len(data)
            status = f"-{(1 - after / before) * 100:.1f}%"
            if note:
                status += f" ({note})"

        before_total += before
        after_total += after
        print(f"{pdf.name:<38} {before / 1024:7.1f}K -> {after / 1024:7.1f}K  {status}")

    saved = before_total - after_total
    percent = saved / before_total * 100 if before_total else 0
    print(
        f"\ntotal {before_total / 1024:.1f}K -> {after_total / 1024:.1f}K "
        f"({saved / 1024:.1f}K saved, -{percent:.1f}%)"
    )


if __name__ == "__main__":
    main()
