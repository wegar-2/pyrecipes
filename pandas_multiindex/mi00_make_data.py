from typing import TypeAlias
from data.data import load_data, DataDict
import pandas as pd
from functools import reduce

NamedData: TypeAlias = tuple[str, pd.DataFrame]


def joiner(l, r) -> pd.DataFrame:
    return pd.merge(l, r, left_index=True, right_index=True, how="outer")


def make_mi_data(add_mi: bool = False) -> pd.DataFrame:
    data: pd.DataFrame
    d: DataDict = load_data()
    data = reduce(
        joiner,
        [data for data in d.values()]
    ).fillna(method="ffill").fillna(method="bfill")
    if add_mi:
        data.columns = pd.MultiIndex.from_product([
            ["hgc", "kgh", "usdcny"],
            ["open", "high", "low", "close"]
        ], names=["asset", "ohlc_attr"])
    return data



if __name__ == "__main__":
    data = make_mi_data()

    print(f"{data=}")
