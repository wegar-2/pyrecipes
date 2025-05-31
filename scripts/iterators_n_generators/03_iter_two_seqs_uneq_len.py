from typing import Final
from string import ascii_uppercase
from itertools import zip_longest, cycle

LETTERS: Final[str] = ascii_uppercase[:7]
NUMBERS: Final[list[int]] = list(range(5))

if __name__ == "__main__":

    # 1. naively: use zip --- stops at end of the shorter iterable
    for l, n in zip(LETTERS, NUMBERS):
        print(f"{l=}, {n=}")

    # 2. using zip_longest
    for l, n in zip_longest(LETTERS, NUMBERS, fillvalue="NA"):
        print(f"{l=}, {n=}")

    # 3. iterating with index i
    cl, cn = cycle(LETTERS), cycle(NUMBERS)
    for i in range(36):
        l, n = next(cl), next(cn)
        print(f"{i:02}: {l=}, {n=}")
