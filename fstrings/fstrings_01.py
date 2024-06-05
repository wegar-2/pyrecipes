from datetime import date

import numpy as np


if __name__ == "__main__":
    print(f"date: {date.today():%Y/%m/%d}")

    x = np.random.randn(1)[0]
    print(f"{x=}")
    print(f"x = {x:.4f}")


