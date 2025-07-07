from inspect import getgeneratorstate
from typing import Generator


def basic_example():
    x = yield 123
    print(f"Received {x=}")


if __name__ == "__main__":

    gen_: Generator = basic_example()
    print(f"Generator has just been created; {getgeneratorstate(gen_)}")

    print(f"{next(gen_)=}")
    print(f"Retrieving generator state: {getgeneratorstate(gen_)}")

    try:
        gen_.send(321)
    except StopIteration:
        print(f"Retrieving generator state: {getgeneratorstate(gen_)}")
        print(f"caught {StopIteration.__name__}")
