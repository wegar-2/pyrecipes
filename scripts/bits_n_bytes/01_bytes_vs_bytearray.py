# references:
# (1) https://stackoverflow.com/questions/62903377/python3-bytes-vs-bytearray-and-converting-to-and-from-strings

from constants.constants import GERMAN_LETTERS


if __name__ == "__main__":

    s: str = GERMAN_LETTERS
    print(f"{s=}")

    # bytes: mutable
    s_bytes: bytes = s.encode(encoding="utf-8")
    print(f"{s_bytes=}")

    # bytearray: immutable
    s_bytearray: bytearray = bytearray([x for x in s_bytes])
    print(f"{s_bytearray=}")
    s_bytearray[0] = 111
