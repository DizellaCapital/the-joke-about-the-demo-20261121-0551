#!/usr/bin/env python3
"""The joke about the demo — make.fun bounty entry.

Writes one line (a joke about working beside an AI coding agent) to
/output/entry.txt. Deterministic, no network, no input.
"""

import os

JOKE = "The demo crashed, so my agent presented the error page as our new landing page \u2014 and three investors in the front row asked for the link."

# The gate requires 1-280 Unicode code points; fail loudly here instead of
# ever writing an invalid entry.
assert 1 <= len(JOKE) <= 280, "joke must be 1-280 characters"

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")

if __name__ == "__main__":
    main()
