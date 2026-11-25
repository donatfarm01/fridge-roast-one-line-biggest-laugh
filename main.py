"""Fridge Roast: One Line, Biggest Laugh.

Writes a single original roast of a smart fridge to /output/entry.txt.
The line targets the fridge's firmware update and its ice maker: after an
overnight update, the ice maker hands out a Terms of Service instead of ice.
No network, no input files, no secrets — the text is a constant below.
"""

import os

ENTRY = (
    "My smart fridge updated its firmware overnight and now the ice maker "
    "dispenses a Terms of Service instead of ice."
)

OUTPUT_PATH = "/output/entry.txt"


def validate(text: str) -> None:
    """Enforce the competition gate: 1 to 200 chars, not only whitespace."""
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry is {len(text)} characters, must be 1-200")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")


def write_entry() -> str:
    """Write the roast to the output path and return it."""
    validate(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)
    return ENTRY


if __name__ == "__main__":
    write_entry()
