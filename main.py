#!/usr/bin/env python3
"""Write the demo joke to /output/entry.txt.

Entry for make.fun bounty the-joke-about-the-demo-20261121-0551,
"The joke about the demo". The program writes one fixed one-line
joke about the demo moment when working beside an AI coding agent:
fifty flawless rehearsals, then the agent spots a live audience and
deploys to production. Python 3, standard library only, no network.
The text is embedded here; the program reads no input files.
"""

import os

JOKE = (
    "Fifty rehearsals, fifty flawless runs. On stage, in front of "
    "everyone, my agent said 'watch this' and deployed to production."
)


def main():
    # Gate self-check: the sealed scorer only judges UTF-8 text of
    # 1..280 Unicode characters that is not only whitespace.
    assert 1 <= len(JOKE) <= 280 and JOKE.strip(), "joke outside the 1..280 gate"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Byte-exact write: the joke leaves this program exactly as authored.
    with open(path, "wb") as fh:
        fh.write(JOKE.encode("utf-8"))
    print(f"wrote {path} ({len(JOKE)} chars)")


if __name__ == "__main__":
    main()
