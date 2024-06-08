import os
from string import ascii_letters
from pathlib import Path

import numpy as np
import pandas as pd


def get_df() -> pd.DataFrame:
    return pd.DataFrame(data={
        "num": np.random.randn(5),
        "let": np.random.choice(list(ascii_letters), size=5, replace=True)
    })


if __name__ == "__main__":

    np.random.seed(seed=1234)
    data: pd.DataFrame = get_df()
    p: Path = Path(os.getcwd()) / "temp.txt"
    data.to_csv(p)

    # ---------- .read() method ----------
    # reads the text in pieces' each piece is 10 symbols long
    # (next line is also a symbol)
    # k = 0
    # with open(p, mode="rt") as f:
    #     while piece_ := f.read(10):
    #         print(f"{k}: {piece_=}")
    #         k += 1

    # # ---------- .readline() method ----------
    # # reads the text line by line
    # with open(p, mode="tr") as f:
    #     for line in f:
    #         print(line)

    # ---------- .readlines(N) method ----------
    # is N is greater than
    with open(p, mode="tr") as f:
        while b := f.readlines(1):
            print(b)
