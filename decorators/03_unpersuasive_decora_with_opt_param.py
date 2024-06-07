# References: decorators with optional parameters:
# (1) https://realpython.com/primer-on-python-decorators/
# (2) https://github.com/dabeaz/python-cookbook/blob/master/src/9/defining_a_decorator_that_takes_an_optional_argument/example.py

from typing import Callable
from functools import wraps, partial
from loguru import logger


def decorator_first_version(
        func: Callable = None,
        *,
        repetitions: int = 2
) -> Callable:
    """
    This decorator is based on examples:
    (1) https://realpython.com/primer-on-python-decorators/
    """

    def wrapper(func_: Callable) -> Callable:
        @wraps(func_)
        def inner(*args, **kwargs):
            val = None
            for k in range(repetitions):
                val = func_(*args, **kwargs)
            return val
        return inner

    if func is None:
        logger.info(f"Received no function...; setting parameter")
        return wrapper
    else:
        logger.info(f"Received function {func.__name__}")
        return wrapper(func_=func)


def decorator_second_version(
        func: Callable = None,
        *,
        repetitions: int = 2
) -> Callable:
    """
    This decorator is based on:
    # (2) https://github.com/dabeaz/python-cookbook/blob/master/src/9/defining_a_decorator_that_takes_an_optional_argument/example.py
    """
    logger.info(f"{func=}")
    logger.info(f"{repetitions=}")
    if func is None:
        ret_fun = partial(decorator_second_version, repetitions=repetitions)
        logger.info(f"{ret_fun=}")
        return ret_fun

    @wraps(func)
    def wrapper(*args, **kwargs):
        for i in range(1, repetitions):
            logger.info(f"Repeated runs of function: {func.__name__}")
            func(*args, **kwargs)
        return wrapper
    return wrapper


def my_function(*args, **kwargs):
    logger.info(f"{args=}")
    logger.info(f"{kwargs=}")


if __name__ == "__main__":

    # res1 = decorator_first_version(repetitions=3)(my_function)(4, 2, a=2, b=32)
    # res2 = decorator_second_version(repetitions=4)#(my_function(4, 2, a=2, b=32))()
    # res3 = res2(func=my_function)(func_=my_function)(my_function(4, 2, a=2, b=32))
    # print(res2)
    decorator_second_version(repetitions=3)(my_function)(4, 2, a=2, b=32)

    # EXEGESIS OF APPROACH (1)
    # EXEGESIS OF APPROACH (2)
