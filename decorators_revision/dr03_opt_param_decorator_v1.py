from functools import wraps, partial
from typing import Callable, Union

numeric = Union[int, float]


def my_decor(func=None, *, a=3) -> Callable:
    if func is None:
        print(f"setting a to {a}")
        return partial(my_decor, a=a)

    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"inside wrapper of {func.__name__}; {args=}, {kwargs=}")
        return func(*args, **kwargs)
    return wrapper


@my_decor
def my_fun(x: numeric, y: numeric, z: numeric = 123) -> numeric:
    print("inside my_fun")
    return 3*x + 2*y + z


@my_decor(a=23)
def my_other_fun(x: numeric, y: numeric, z: numeric = 123) -> numeric:
    print("inside my_fun")
    return 3*x + 2*y + z


if __name__ == "__main__":
    my_fun(3, 2, 3)
    my_other_fun(1, 2, 1)
