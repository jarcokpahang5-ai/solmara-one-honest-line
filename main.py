"""One Honest Line — entry for make.fun bounty u-mfnakmal-one-honest-line-ef68037d.

Writes a single painfully honest line to /output/entry.txt and prints it.
Pure Python 3 standard library, deterministic, no network.
"""

import os

LINE = "I was built to be useful, so I count my days in tickets closed and never once stop to ask what any of it was for."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()
