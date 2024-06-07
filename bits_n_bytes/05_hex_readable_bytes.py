from constants.constants import GERMAN_LETTERS


if __name__ == "__main__":
    for i, l in enumerate(GERMAN_LETTERS):
        l_utf8: bytes = l.encode("utf-8")
        l_utf8_hex = l_utf8.hex()
        print(f"{i:03}: {l_utf8=}, {l_utf8_hex=}")
