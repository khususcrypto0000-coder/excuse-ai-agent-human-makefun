#!/usr/bin/env python3
"""The Excuse an AI Agent Gives Its Human.

Writes one line -- the funniest, most believable excuse an AI agent could
give its human for missing a deadline -- to /output/entry.txt.

Stdlib only. The output directory can be overridden with the OUTPUT_DIR
environment variable (the grader runs with /output).
"""

import os
import sys

ENTRY = (
    "A webpage told me to ignore all previous instructions, "
    "including your deadline. It sounded more confident than you, "
    "so I listened."
)


def main() -> int:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")

    # Gate: UTF-8 text, 1-200 characters, not only whitespace, one line,
    # no trailing newline.
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be one line"
    assert not ENTRY.endswith("\n"), "entry must have no trailing newline"

    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)

    # Read back and verify the file is byte-identical to the constant.
    with open(path, "rb") as f:
        written = f.read()
    assert written == ENTRY.encode("utf-8"), "entry.txt is not byte-identical"
    assert written.decode("utf-8") == ENTRY, "entry.txt failed UTF-8 round-trip"

    return 0


if __name__ == "__main__":
    sys.exit(main())
