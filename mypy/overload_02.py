from typing import overload, Optional

import numpy as np


@overload
def make_data(rows: int) -> np.ndarray:
    pass


@overload
def make_data(rows: int, cols: int) -> np.ndarray:
    pass


def make_data(rows: int, cols: Optional[int] = None):
    if cols is None:
        cols = 3
    return np.random.randn(rows*cols).reshape((rows, cols))


if __name__ == '__main__':
    print(f"{make_data(4, 2)=}")
    print(f"{make_data(4)=}")
