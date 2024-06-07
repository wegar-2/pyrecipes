from string import ascii_uppercase
from typing import Final

LTTRS: Final[str] = ascii_uppercase[:5]


if __name__ == "__main__":
    print(f"{LTTRS}")

    # left and right alignments
    print(f"RHS: {LTTRS:>30}[marker]")
    print(f"LHS: {LTTRS:<30}[marker]")

    # centering
    print(f"LHS: {LTTRS:^30}[marker]")

    # adding fill-in symbols
    print(f"RHS: {LTTRS:->30}[marker]")
    print(f"LHS: {LTTRS:-<30}[marker]")
    print(f"LHS: {LTTRS:-^30}[marker]")


