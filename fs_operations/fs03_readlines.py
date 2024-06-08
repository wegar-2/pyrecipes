from pathlib import Path

if __name__ == "__main__":
    p: Path = Path(__file__).parent / "temp.txt"

    with open(p, "rt") as f:
        print(f.readlines(8))

    with open(p, "rt") as f:
        print(f.readlines(9))

    with open(p, "rt") as f:
        print(f.readlines(1))

    with open(p, "rb") as f:
        print(f.readlines(8))

    with open(p, "rb") as f:
        print(f.readlines(9))
