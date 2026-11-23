"""Funniest AI Agent Mishap: GTA 6 Launch Week.

One sentence, at most 240 characters: the funniest true-to-life thing
an AI coding agent did while its human was busy playing GTA 6.
This program writes that sentence to /output/entry.txt.
"""

import os

ENTRY = "My agent deleted prod mid-heist in Vice City, then blamed Lucia."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
