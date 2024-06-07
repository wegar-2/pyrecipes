from datetime import date

import numpy as np


if __name__ == "__main__":

    # 1. limiting decimal places displayed
    x = np.random.randn(1)[0]
    print(f"{x=}")
    print(f"x = {x:.4f}")

    # 2. displaying int with leading zeros
    x = 123
    print(f"x = {x:05}")

    # 3. displaying int as binary with leading zeros (bytes: 8 digits here)
    x = 33
    print(f"x = {x:08b}")

    # 4. displaying a number float with comma as thousands separator and dot as
    #    decimal separator
    x = 12345.678
    print(f"x = {x:0,.4f}")
