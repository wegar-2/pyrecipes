import random

from bitarray import bitarray


__all__ = [
    "coin_flip",
    "make_random_bit_sequence"
]


def coin_flip(p: float = 0.5) -> int:
    return random.binomialvariate(p=p)


def make_random_bit_sequence(n: int) -> bitarray:
    ba: bitarray = bitarray()
    for k in range(n):
        ba.append(coin_flip())
    return ba
