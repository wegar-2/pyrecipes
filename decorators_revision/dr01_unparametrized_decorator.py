from functools import wraps
from typing import Callable


def my_add(x, y):
    print("inside my_add")
    return x + y


def my_decor(func_: Callable) -> Callable:

    @wraps(func_)
    def wrapper(*args, **kwargs):
        print(f"calling function {func_.__name__} with {args=} and {kwargs=}")
        return func_(*args, **kwargs)

    return wrapper


if __name__ == "__main__":
    print(my_decor(func_=my_add)(x=1, y=3))
