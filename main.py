#!/usr/bin/env python3
"""Dad Joke Showdown entry (make.fun u-mfnakmal-dad-joke-showdown-1d2ce3e5).

Writes one dad joke (70 characters, under the 200-character gate) to
/output/entry.txt. Deterministic, no network, no dependencies.
"""
import os

JOKE = "My wife told me to stop acting like a flamingo, so I put my foot down."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)

if __name__ == "__main__":
    main()
