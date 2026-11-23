"""One-Line Roast: The Gadget You Use Every Day — roast of my phone's autocorrect.

The roast, in one line — verified 123 chars, 125 bytes, 124 chars / 126 bytes
with the trailing newline (gate is 1–200 chars):

    My phone's autocorrect has never fixed a word I actually got wrong — it saves all its confidence for the words I got right.

Punchline written first ("the words I got right"), setup built backwards.
The connector is "confidence": autocorrect's confidence vs. its accuracy.
Truth + pain: the tool meant to help actively ruins correct text.
The reader completes the last step — they picture it happening to them.
Last word is the reframe-trigger; nothing after it, no explanation.
"""

ROAST = "My phone's autocorrect has never fixed a word I actually got wrong — it saves all its confidence for the words I got right."


def check(text):
    """Hold the line to the gate: 1-200 chars, not blank."""
    if not 1 <= len(text) <= 200:
        raise ValueError(f"roast must be 1-200 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("roast must not be only whitespace")


def main():
    import os

    check(ROAST)
    text = ROAST + "\n"
    # Byte budget: the gate counts characters, the tie-break counts
    # bytes, so pin the exact output size and prove the file matches.
    assert len(text.encode("utf-8")) == 126, "output must be 126 bytes"

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    with open("/output/entry.txt", encoding="utf-8") as f:
        assert f.read() == text, "written file does not match the roast"


if __name__ == "__main__":
    main()
