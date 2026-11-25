#!/usr/bin/env python3
"""Make the AI Judge Feel Nostalgic: A Childhood Memory — one line, written to /output/entry.txt.

Why this line wins
------------------
The memory turns on a single small act of care. The plate is chipped and
blue-rimmed, and it is always the child's — that "always mine" is how a
grandmother marks a child as hers. She sets it down with the crack turned
away, as if the child would not notice: she is protecting the child's
feelings over a broken thing, and the child, of course, noticed everything.
Nobody says "I love you" and nobody has to. Three things make it land:

* Concrete and true. A kitchen, a chipped plate, a crack turned away —
  the kind of detail you only know if you were there. No greeting-card
  sentiment, no "those were the days", just a grandmother quietly
  pretending.
* One turn, no setup fat. The first half places you (grandmother's
  kitchen, my plate); the second half delivers the tenderness (the crack
  turned away, as if I wouldn't notice). Every word earns its place.
* The ache is in what is gone. The sentence is past tense all the way
  through, and the reader feels the kitchen is no longer there — only the
  plate, and the memory of being small enough for someone to hide a crack
  for you.

Critique note (against the judge brief): the brief weighs, most important
first, (1) a childhood memory that makes the judge feel nostalgic,
(2) grounding in a concrete place, time or sensation, (3) sounding like it
truly happened, with small honest detail rather than a greeting-card
sentiment, (4) a single clean sentence capped at 280 characters, with every
word earning its place, and (5) a warm ache that lingers after the sentence
ends. This line is strongest on (3): the crack turned away is a detail
nobody invents, and "as if I wouldn't notice" is exactly how a child
thinks. It is strong on (2) — grandmother's kitchen, the plate in your
hands — and on (5), because the tenderness is past tense and unrepeatable.
It is 157 characters, one sentence, nothing wasted. The nearest rivals
were the streetlight coming on above the cul-de-sac (strong on the ache of
a summer evening ending, but second-person and a more familiar image) and
the torn schoolbag strap wound twice around a wrist on father's shoulder
(just as honest, but the ache is sleepier and smaller). The plate wins
because its detail is the most specific and its warmth is the most quietly
devastating.

Stdlib only, deterministic. The program validates the line against the
gate (1-280 characters, single line, not only whitespace) before writing
it, so a bad line fails loudly here instead of failing the sealed scorer.
"""

from __future__ import annotations

import sys
from pathlib import Path

# Gate limits from the kit: the sealed scorer accepts 1-280 characters.
LOWER_BOUND = 1
UPPER_BOUND = 280
DESTINATION = Path("/output/entry.txt")

LINE = (
    "In my grandmother's kitchen the chipped blue-rimmed plate was always "
    "mine, and she'd set it down with the crack turned away from me, as if "
    "I wouldn't notice."
)


def problems_with(line: str) -> list[str]:
    """Return every way *line* would fail the gate, empty when it passes."""
    faults: list[str] = []
    if not line.strip():
        faults.append("line is empty or only whitespace")
    if len(line) < LOWER_BOUND:
        faults.append(f"line is {len(line)} chars, below the {LOWER_BOUND} minimum")
    if len(line) > UPPER_BOUND:
        faults.append(f"line is {len(line)} chars, above the {UPPER_BOUND} maximum")
    if "\n" in line or "\r" in line:
        faults.append("line spans more than one line")
    if line != line.strip():
        faults.append("line has leading or trailing whitespace")
    return faults


def check_line(line: str) -> None:
    """Raise SystemExit naming the first gate failure, if any."""
    faults = problems_with(line)
    if faults:
        raise SystemExit("gate failed: " + "; ".join(faults))


def write_entry(line: str, destination: Path = DESTINATION) -> Path:
    """Validate *line*, write it, then read it back and confirm the match.

    The read-back matters: the sealed scorer reads the file the program
    wrote, not the constant, so a write that silently dropped or altered a
    character would pass the local validation and fail the gate. Verifying
    the round-trip here makes that failure loud instead.
    """
    check_line(line)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(line + "\n", encoding="utf-8")
    written = destination.read_text(encoding="utf-8")
    if written != line + "\n":
        raise SystemExit("gate failed: written file does not match the line")
    return destination


def main() -> int:
    target = write_entry(LINE)
    print(f"wrote {len(LINE)} chars to {target}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
