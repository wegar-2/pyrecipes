from constants.constants import GERMAN_LETTERS

from math import log10


def get_hex_rep(x: str) -> str:
    if len(x) != 1:
        raise ValueError(f"Only strings of length 1 are allowed! ")
    return x.encode("utf-8").hex()


def analyze_string(str_: str):
    zpad: int = int(log10(len(str_))) + 1
    for i, s in enumerate(str_):
        print(f"{str(i).zfill(zpad)}: {s} ----> {get_hex_rep(x=s)}")


if __name__ == "__main__":
    analyze_string(str_=GERMAN_LETTERS)
