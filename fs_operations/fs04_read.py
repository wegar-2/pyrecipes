from pathlib import Path

if __name__ == "__main__":
    p: Path = Path(__file__).parent / "temp.txt"

    with open(p, "rt") as f:
        print(f.read(8))

    with open(p, "rt") as f:
        print(f.read(9))

    with open(p, "rt") as f:
        print(f.read(10))

    with open(p, "rb") as f:
        print(f.read(8))

    with open(p, "rb") as f:
        print(f.read(9))

    with open(p, "rb") as f:
        print(f.read(10))
