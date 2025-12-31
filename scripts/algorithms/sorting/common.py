import numpy as np


def generate_array_for_sorting(seed: int | None = None) -> list[int]:
    np.random.seed(seed=seed)
    len_ = np.random.randint(size=1, low=1_000, high=100_000)[0]
    return list(np.random.randint(size=len_, low=0, high=100_000))
