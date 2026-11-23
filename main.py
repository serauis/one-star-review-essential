#!/usr/bin/env python3
"""One-star review of something essential — sleep.

The program writes a single deadpan one-star review to ``entry.txt``
inside the output directory (``$OUTPUT_DIR`` or ``/output`` by default).
The review is exactly 129 characters, with no trailing newline, so the
file is exactly 129 bytes — inside the competition's 1–160 character gate.
"""

import os

MIN_LENGTH = 1
MAX_LENGTH = 160

# The entry: sleep returned a father who is gone, then took him back.
REVIEW_TEXT = (
    "One star. Sleep gave me eight hours with my father, alive and "
    "laughing, then woke me up and took him back. I would like a refund."
)


def check_review(text):
    """Raise if the review fails the competition's character gate."""
    if not MIN_LENGTH <= len(text) <= MAX_LENGTH:
        raise ValueError(
            f"review is {len(text)} chars, gate is {MIN_LENGTH}-{MAX_LENGTH}"
        )
    if not text.strip():
        raise ValueError("review must contain non-whitespace characters")


def output_path():
    """Resolve the entry.txt path from the environment."""
    base = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(base, exist_ok=True)
    return os.path.join(base, "entry.txt")


def write_entry():
    """Validate the review and write it with no trailing newline."""
    check_review(REVIEW_TEXT)
    target = output_path()
    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(REVIEW_TEXT)
    return target


if __name__ == "__main__":
    write_entry()
