from collections import Counter
import hashlib
import random
import time


def hash_generator(
        length: int = 32,
        seed: int = 12345
) -> str:
    hash_obj = hashlib.sha256(str(seed).encode())
    return hash_obj.hexdigest()[:length]

def get_elements_counts(iterable_) -> dict:
    return dict(Counter(iterable_))


if __name__ == "__main__":

    str_: str = hash_generator(length=100)
    print(f"{str_=}")

    counts_dict = get_elements_counts(iterable_=list(str_))
    for k, v in counts_dict.items():
        print(f"{k}: {v}")
