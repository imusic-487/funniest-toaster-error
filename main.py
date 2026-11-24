#!/usr/bin/env python3
"""Funniest Toaster Error Message — make.fun entry.

Writes one line, at most 120 characters: the error message a kitchen
toaster shows its owner. No input, no network, no environment reads;
the text is fixed in this file and written to /output/entry.txt.
"""

import os

ENTRY = "ERROR E-12: YOUR BAGEL IS TOO AMBITIOUS FOR THIS SLOT. PLEASE DOWNGRADE YOUR DREAMS."


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 120, f"entry is {len(text)} chars, must be 1-120"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Wrote {len(text)} chars to /output/entry.txt:")
    print(text)


if __name__ == "__main__":
    main()
