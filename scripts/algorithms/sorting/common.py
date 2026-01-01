from typing import Callable

from loguru import logger
import numpy as np


def generate_array_for_sorting(seed: int | None = None) -> list[int]:
    np.random.seed(seed=seed)
    len_ = 1_000
    return list(np.random.randint(size=len_, low=0, high=100_000))


def sort_algo_test(
        func: Callable,
        inplace: bool = False,
):
    for k in range(1, 101, 1):
        logger.info(f"Test {k}/100...")
        nums = generate_array_for_sorting()
        builtin_sort = sorted(nums)
        if inplace:
            func(nums)
        else:
            nums = func(nums)
        if nums != builtin_sort:
            raise Exception("Testing of custom sorting algo failed! ")
