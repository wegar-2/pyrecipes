import numpy as np
import pandas as pd


def sos(x, y):
    return x**2 + y**2


if __name__ == "__main__":

    np.random.seed(12345)

    ar: np.ndarray = np.array([1, 1, 3, 2])
    print(ar)

    npsos = np.frompyfunc(sos, 2, 1)
    print(npsos.accumulate(ar))
