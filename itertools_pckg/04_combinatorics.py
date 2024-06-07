from itertools import combinations, permutations
from typing import Final


if __name__ == "__main__":

    SET: Final[set] = set(range(5))

    for i, p in enumerate(permutations(SET), start=1):
        print(f"permutation_{i:02}: {p=}")

    for i, c in enumerate(combinations(SET, 3), 1):
        print(f"combination_of_3_{i:02}: {c=}")

