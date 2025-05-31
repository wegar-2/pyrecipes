from typing import Callable
from functools import wraps


def no_args_fun_decorator(func: Callable) -> Callable:
    @wraps(func)
    def wrapper():
        print(f"Calling function: {func.__name__}")
        return func()
    return wrapper


@no_args_fun_decorator
def my_printer():
    print("hello world! ")


def args_kwargs_decorator(func: Callable):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling parametrized function {func.__name__} with args {args}"
              f" and kwargs {kwargs}")
        return func(*args, **kwargs)
    return wrapper


@args_kwargs_decorator
def my_args_kwargs_fun(*args, **kwargs):
    """
    Some info on the function...
    """
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")


if __name__ == "__main__":

    my_printer()
    my_args_kwargs_fun(123, 22, x=123, y=90)

    print(f"doc string of {my_args_kwargs_fun.__name__}: "
          f"{my_args_kwargs_fun.__doc__}")
