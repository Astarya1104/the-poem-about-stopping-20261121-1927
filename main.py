#!/usr/bin/env python3
"""One short poem about agency: the power to stop and to stay."""
from pathlib import Path
import os

POEM = """At the park gate I dropped the leash.
Juno looked up, ears high,
then sat down beside my shoes.

All these years I thought
the holding was the power.
It was the staying —
her choice, made twice a day,
to walk home with me."""

def main() -> None:
    if not (1 <= len(POEM) <= 280) or not POEM.strip():
        raise ValueError("poem must be 1-280 non-whitespace characters")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(POEM, encoding="utf-8")

if __name__ == "__main__":
    main()
