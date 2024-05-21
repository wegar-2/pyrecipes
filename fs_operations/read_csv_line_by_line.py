"""
Reading from .txt and .csv files "manually"
"""

from pathlib import Path


def read_text_file_line_by_line(p: Path) -> list:
    lines: list = []
    with open(p, mode="rb") as f:
        for line in f:
            print(line)

    with open(p, mode="rt") as f:
        for line in f:
            print(line)

    return lines


if __name__ == "__main__":
    data_path: Path = Path(__file__).parent.parent / "data" / "usdcny_d.csv"

    read_text_file_line_by_line(p=data_path)
