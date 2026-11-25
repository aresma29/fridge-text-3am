#!/usr/bin/env python3
"""Print the 3am fridge text stored in entry.txt."""
import sys
from pathlib import Path


def main() -> int:
    entry_path = Path(__file__).resolve().parent / "entry.txt"
    text = entry_path.read_text(encoding="utf-8").rstrip("\n")
    print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
