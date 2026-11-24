#!/usr/bin/env python3
"""u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a.

The program writes one sentence to /output/entry.txt: a single-sentence
pitch for a ridiculous invention that fixes a tiny everyday annoyance.

The annoyance: cereal goes soggy the moment milk touches it. The
invention: a bowl that keeps milk and cereal in separate compartments
until the spoon arrives, then formally introduces them with a tiny
fanfare, so nothing ever goes soggy. The laugh comes from the invention
itself -- a bowl that treats breakfast like a diplomatic summit, with
the spoon as the guest of honour and the fanfare as the handshake.

Deterministic: the same bytes on every run. Standard library only.
No network, no input, no randomness.
"""

import os

TEXT = (
    "A cereal bowl that keeps the milk and cereal in separate "
    "compartments until your spoon arrives, then introduces them "
    "with a tiny fanfare so nothing ever goes soggy."
)

# The gate allows 1-220 characters: refuse to write anything else.
LENGTH = len(TEXT)
if LENGTH < 1 or LENGTH > 220:
    raise SystemExit(f"entry text is {LENGTH} characters, outside 1-220")

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(TEXT)
