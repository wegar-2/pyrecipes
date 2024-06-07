from loguru import logger
from typing import Callable
from functools import wraps


def conditional_sum(x, y):
    try:
        s = x + y
    except Exception as e:
        logger.warning(f"Failed to add {x=} and {y=} due to exception: {e}; "
                       f"returning zero. ")
        return x
    else:
        return s


def parametrized_decorator(multiplier: int = 2) -> Callable:
    def outer_wrapper(func: Callable):
        @wraps(func)
        def inner_wrapper(*args, **kwargs):
            logger.info(f"Running function {func.__name__} with {args=} and "
                        f"{kwargs=}")
            d: dict = func(*args, **kwargs)
            logger.info(f"Multiplying members of output dict by {multiplier=}")
            for k, v in d.items():
                d[k] = multiplier * d[k] if v is not None else d[k]
            return d
        return inner_wrapper
    return outer_wrapper


@parametrized_decorator(multiplier=2)
def custom_sum(*args, **kwargs) -> dict:
    logger.info("calculating sums of args and kwargs")
    if args is not None:
        args_sum = 0
        logger.info("args is not none; summing args")
        for x in args:
            args_sum = conditional_sum(args_sum, x)
    else:
        args_sum = None
    if kwargs is not None:
        kwargs_sum = 0
        logger.info("Summing kwargs")
        for _, v in kwargs.items():
            kwargs_sum = conditional_sum(kwargs_sum, v)
    else:
        kwargs_sum = None
    return {
        "args_sum": args_sum,
        "kwargs_sum": kwargs_sum
    }


if __name__ == "__main__":
    print(custom_sum(1, 32, "a", {123}, a=1, b=2))
