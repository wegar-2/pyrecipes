from functools import wraps
from typing import Callable


def parametrized_decorator(value_of_y) -> Callable:

    def external(func: Callable) -> Callable:
        print("inside external")

        @wraps(func)
        def internal(*args, **kwargs) -> Callable:
            print(f"inside internal; {value_of_y=}")

            print("setting value of y member of kwargs")
            kwargs["y"] = value_of_y

            return func(*args, **kwargs)
        return internal
    return external


def my_function(*, x, y, z=3):
    return x + y * z


if __name__ == "__main__":
    print(parametrized_decorator(value_of_y=3)(my_function)(x=1))
