"""One-Line Laugh Sprint — make.fun entry.

Reads the entry line from entry.txt and prints it.
"""

from pathlib import Path


def load_line() -> str:
    here = Path(__file__).resolve().parent
    entry_file = here / "entry.txt"
    if not entry_file.exists():
        return "My Wi-Fi went down for five minutes, so I talked to my family."
    return entry_file.read_text(encoding="utf-8").strip()


def main() -> None:
    print(load_line())


if __name__ == "__main__":
    main()
