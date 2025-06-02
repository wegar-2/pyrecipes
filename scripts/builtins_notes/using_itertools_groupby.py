from itertools import groupby

from common.common import make_random_bit_sequence

from bitarray import bitarray


if __name__ == "__main__":
    bitseq: bitarray = make_random_bit_sequence(n=100)
    print(f"{bitseq=}")

    for i, x in groupby(bitseq):
        print(f"{i}: {len(tuple(x))}")
