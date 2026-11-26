"""One-line comeback from the office printer, in its own voice.

Writes the line to /output/entry.txt (or $OUTPUT_DIR/entry.txt).
Stdlib only, deterministic, no network.
"""

import os

LINE = "Paper jam? I have printed 12,000 pages without a single thank-you, and the one day I rest, you all gather like mourners. Error 404: gratitude not found."


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
