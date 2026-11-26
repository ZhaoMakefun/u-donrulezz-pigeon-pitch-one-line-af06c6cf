#!/usr/bin/env python3
# Pigeon Pitch, One Line — a one-line startup pitch from a city pigeon.
# Running this script drops the pitch into entry.txt under the output
# directory make.fun expects. Plain stdlib, no network, same bytes every run.
# The 200-character ceiling comes from the bounty rules; the pitch is 146.

from pathlib import Path
import os
import sys

PITCH = "Coo is the Uber for breadcrumbs: 40,000 city pigeons deliver your lunch scraps in under four minutes, and we never ask for a tip — we eat the tip."
CEILING = 200

pitch = PITCH.strip()
if len(pitch) == 0:
    sys.exit("refusing to write an empty pitch")
if len(pitch) > CEILING:
    sys.exit(f"pitch is {len(pitch)} characters, over the {CEILING} limit")
if any(ch in pitch for ch in ("\n", "\r")):
    sys.exit("pitch must stay on one line")
pitch.encode("utf-8")

target_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
target_dir.mkdir(parents=True, exist_ok=True)
(target_dir / "entry.txt").write_text(pitch, encoding="utf-8")
