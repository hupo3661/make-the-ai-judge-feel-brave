#!/usr/bin/env python3
"""Write one short text to /output/entry.txt.

The text is written for make.fun's "Make the AI judge feel brave"
bounty: a short text that leaves the AI judge reading it braver --
steadier, unhurried, ready to move. Standard library only, no network.
"""

import os
from pathlib import Path

TEXT = (
    "At dusk, a lighthouse keeper trims the wick. "
    "The sea is wide and dark, and he does not argue with it. "
    "He lights one small lamp, then another. "
    "The dark steps back a little \u2014 not all at once, "
    "just enough to see the next stone on the path home."
)


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    text = TEXT.strip()
    assert 1 <= len(text) <= 280, f"text is {len(text)} characters"
    assert text.strip(), "text must not be only whitespace"
    (output_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
