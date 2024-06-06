from constants.constants import GERMAN_LETTERS


def binary_str(s: str) -> str:
    return "".join([format(x, "08b") for x in s.encode(encoding="utf-8")])


def str_from_bin(bs: str) -> str:
    return bytearray([
        int(bs[i:i+8], 2) for i in range(0, len(bs), 8)
    ]).decode("utf-8")


if __name__ == '__main__':

    bs: str = binary_str(s=GERMAN_LETTERS)
    print(f"{bs=}")
    gls: str = str_from_bin(bs=bs)
    print(f"{gls=}")
    print(f"check: {GERMAN_LETTERS == gls}")
