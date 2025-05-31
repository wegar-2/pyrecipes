from pathlib import Path
from typing import Literal, TypeAlias, Final

Mode: TypeAlias = Literal["rt", "rb"]
ReadFunction: TypeAlias = Literal["read", "readline", "readlines"]
FILEPATH: Final[Path] = Path(__file__).parent / "myfile.txt"


def read_file(path: Path, mode: Mode, n: int, rf: ReadFunction):
    with open(path, mode) as f:
        if rf == "read":
            output = f.read(n)
        elif rf == "readline":
            output = f.readline(n)
        else:
            output = f.readlines(n)
    print(f"{mode=}, {n=}, {rf=}; {output=}")
