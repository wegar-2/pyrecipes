import random
from time import sleep

from tenacity import retry, stop_after_attempt, before_log


import logging
import sys


def my_function(n):
    sleep(n)


def raise_error_randomly(error_proba: float = 0.5) -> None:
    assert error_proba > 0, f"Too low value of parameter {error_proba=}"
    assert error_proba < 1, f"Too high value of parameter {error_proba=}"
    if (x := random.uniform(0, 1)) > error_proba:
        raise ValueError(f"Error on drawing value {x}")


@retry(stop=stop_after_attempt(5))
def unreliable_invocation(p: float = 0.75):
    raise_error_randomly(error_proba=p)


logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

logger = logging.getLogger(__name__)


@retry(stop=stop_after_attempt(3), before=before_log(logger, logging.DEBUG))
def raise_my_exception():
    raise Exception("Fail")


if __name__ == "__main__":
    raise_my_exception()

    