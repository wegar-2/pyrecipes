from functools import wraps, update_wrapper
from typing import Any, Callable, Final


KEY_ATTRIBUTES: Final[list[str]] = [
    "__name__",
    "__doc__",
    "__qualname__",
    "__module__"
]


def print_key_attrs(x: Callable | Any) -> None:
    print(f"Printing key attributes of {x=}")
    for attrib in KEY_ATTRIBUTES:
        try:
            print(f"{attrib=}; {getattr(x, attrib)=}")
        except AttributeError:
            continue


def mult_by_two(x):
    return 2 * x


class ClassTypeLoggingDecorator:
    """
    Note: this decorator is not using functools.wraps
    """

    def __init__(self, func: Callable):
        self._func: Callable = func

    def __call__(self, *args, **kwargs):
        print(f"Before call to {self._func.__name__} inside "
              f"{self.__class__.__name__}")
        result = self._func(*args, **kwargs)
        print(f"After call to {self._func.__name__} inside "
              f"{self.__class__.__name__}; returning")
        return result


class WrappingClassTypeLoggingDecorator:

    def __init__(self, func: Callable):
        update_wrapper(self, func)
        self._func: Callable = func

    def __call__(self, *args, **kwargs):
        print(f"Before call to {self._func.__name__} inside "
              f"{self.__class__.__name__}")
        result = self._func(*args, **kwargs)
        print(f"After call to {self._func.__name__} inside "
              f"{self.__class__.__name__}; returning")
        return result


def usual_logging_decorator(func: Callable) -> Callable:
    @wraps(func)
    def inner(*args, **kwargs):
        print(f"Before call to {func.__name__} inside "
              f"{usual_logging_decorator.__name__}")
        result = func(*args, **kwargs)
        print(f"After call to {func.__name__} inside "
              f"{usual_logging_decorator.__name__}; returning")
        return result
    return inner


if __name__ == "__main__":

    print(f"{mult_by_two(x=10)=}")
    print_key_attrs(x=mult_by_two)
    print("\n\n")

    cdec_mult_by_two: Callable = ClassTypeLoggingDecorator(mult_by_two)
    print(f"{cdec_mult_by_two(x=32)=}")
    print_key_attrs(x=cdec_mult_by_two)
    print("\n\n")

    fdec_mult_by_two: Callable = usual_logging_decorator(func=mult_by_two)
    print_key_attrs(x=fdec_mult_by_two)
    print(f"{fdec_mult_by_two(x=11)=}")
    print("\n\n")

