import io
from pathlib import Path

from constants.constants import GERMAN_LETTERS

if __name__ == "__main__":

    # example 1: using a file
    p: Path = Path(__file__).parent / "example.txt"
    f = open(p, "rt")
    for i, letter in enumerate(iter(lambda: f.read(1), "z"), 1):
        print(f"{i:03}: {letter}")

    print("\n\n\n")

    # example 2: using io.StringIO
    str_strm: io.StringIO = io.StringIO(initial_value=GERMAN_LETTERS)
    for i, letter in enumerate(iter(lambda: str_strm.read(1), "z"), 1):
        print(f"{i:03}: {letter}")

