"""Make the Judge Smile — one line about a small good thing today.

Writes a single warm line to entry.txt in the output directory.
Deterministic: the same bytes on every run.
"""

import os

LINE = (
    "The rain started just as I left, and the shopkeeper I barely know "
    "ran out with her umbrella, laughing, \u201cyou\u2019ll melt!\u201d \u2014 "
    "I walked home dry and grinning."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
