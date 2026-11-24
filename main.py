#!/usr/bin/env python3
"""Say What Actually Broke — one brutally honest error message.

Writes a single line of error copy to /output/entry.txt. The line names
the real failure (an upload that reached the server but was lost before
it was stored) and tells the user exactly what to do next, with a joke
that survives being pasted into a real product dialog.
"""

import os

ENTRY = (
    "Your file uploaded, then vanished between the disk and the database. "
    "Nothing was saved. Upload it again. This time we'll write it down first."
)

MAX_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    line = ENTRY.strip()
    if not line:
        raise SystemExit("error: entry line is empty")
    if len(line) > MAX_CHARS:
        raise SystemExit(
            f"error: entry is {len(line)} chars, over the {MAX_CHARS} limit"
        )
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(line + "\n")
    print(f"wrote {len(line)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
