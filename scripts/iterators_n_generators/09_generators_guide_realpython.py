# Source: https://realpython.com/introduction-to-python-generators/

from typing import Callable, Generator
import inspect
import random


def is_palindrome(x: int) -> bool:
    return str(x) == str(x)[::-1]


def infinite_sequence() -> Generator:
    num = 0
    while True:
        yield num
        num += 1


def capped_infinite_sequence() -> Generator:
    inf_seq_gen: Generator = infinite_sequence()
    for i in inf_seq_gen:
        yield i
        if i > 5:
            inf_seq_gen.close()


def infinite_sequence_expr() -> Generator:
    k = 0
    while True:
        i = yield k
        k += 1
        if i is not None:
            k += i


def capped_jumping_infinite_sequence(cap: int = 100) -> Generator:
    i = 0
    while True:
        jump = yield i
        i += jump
        if i > cap:
            break


def print_capped_infinite_sequence():
    for x in capped_infinite_sequence():
        print(x)


def print_capped_jumping_infinite_sequence():
    gen_: Generator = capped_jumping_infinite_sequence(cap=100)

    while True:
        if inspect.getgeneratorstate(gen_) == "GEN_CREATED":
            v = next(gen_)
            print(f"Value received from gen_ in GEN_CREATED state: {v=}")
        else:
            jump = random.randint(3, 5)
            print(f"Randomized jump size: {jump=}")
            try:
                v = gen_.send(jump)
            except StopIteration:
                break
            else:
                print(f"Received value: {v=}")


if __name__ == "__main__":
    # print_capped_infinite_sequence()
    print_capped_jumping_infinite_sequence()
