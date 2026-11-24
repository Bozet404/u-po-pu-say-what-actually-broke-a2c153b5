"""Write one brutally honest error line to /output/entry.txt.

The program uses only the Python standard library. It creates the
output directory only when it is missing and never deletes it.
"""

import os

LINE = (
    "Payment declined, so we retried it twice and your bank now thinks "
    "we're stealing your card. Call them, tell them we're clumsy, not "
    "criminals, and try a different card."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(LINE)


if __name__ == "__main__":
    main()
