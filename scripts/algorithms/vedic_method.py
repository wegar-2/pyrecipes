from bisect import bisect_left
import math
from loguru import logger


def vedic_square_root(n: int):
    # (x + y)^2 = x^2 + (2*x + y) * y
    if n <= 0:
        raise Exception(f"Only positive integers allowed; received: {n=:_} ")
    m: int = math.floor(len(str(n)) / 2)
    logger.info(f"Searching for square root of {n=:_}; "
                f"starting search at order of magnitude 10^{m=}")
    root = 0
    root_squared = 0
    candidates: list = []
    last_lower_than_pointer: int = 0
    for i, p in enumerate(range(m, -1, -1), start=1):
        logger.info(f"Iteration {i}: {root=:_}, {root_squared=:_}")
        candidates = [root_squared] + [
            root_squared + (2*root + k*10**p) * (k * 10**p)
            for k in range(1, 10, 1)
        ]
        logger.info(f"{candidates=}")
        last_lower_than_pointer = bisect_left(candidates, n)
        if p > 0:
            root = root + (last_lower_than_pointer - 1) * 10  ** p
        else:
            root = root + last_lower_than_pointer * 10 ** p
        root_squared = candidates[last_lower_than_pointer - 1]
        # last_lower_than_pointer = [c < n for c in candidates].index(False)
        # if p < m:
        #     root = root + (last_lower_than_pointer - 1) * 10 ** p
        #     root_squared = candidates[last_lower_than_pointer - 1]
        # else:
        #     root = root + (last_lower_than_pointer - 1) * 10  ** p
        #     root_squared = candidates[last_lower_than_pointer - 1]

    candidate_exact = candidates[last_lower_than_pointer]
    if candidate_exact == n:
        # logger.info(f"Found exact root: {candidate_exact=}")
        return root
    # logger.info("Not a perfect square! ")
    # logger.info(f"{root_squared=:_} < {n=:_} < {candidate_exact=:_}")
    return root_squared, candidate_exact


if __name__ == "__main__":
    # n = 1_522_757
    # print(f"{math.sqrt(n)}")
    # vedic_square_root(n=16)
    # vedic_square_root(n=144)
    # print(f"{vedic_square_root(n=16)=}")
    print(f"{vedic_square_root(n=1_522_756)=}")

    # from bisect import bisect_left
    # x = [k*10 for k in range(0, 11, 1)]
    # print(f"{x=}")
    # print(f"{bisect_left(x, 23)=}")
