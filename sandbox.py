from typing import overload, Optional

import numpy as np
import pandas as pd


def get_data() -> pd.DataFrame:
    return pd.DataFrame({
        "X": np.random.randn(100),
        "Y": np.random.randn(100)
    })


@overload
def process_data(data: pd.DataFrame) -> pd.DataFrame: ...
@overload
def process_data(data: pd.DataFrame, more_data: pd.DataFrame) -> (pd.DataFrame, pd.DataFrame): ...


def process_data(
        data: pd.DataFrame,
        more_data: Optional[pd.DataFrame] = None
) -> pd.DataFrame | (pd.DataFrame, pd.DataFrame):
    if more_data is None:
        return process_data(data=data)
    else:
        return process_data(data=data, more_data=more_data)


if __name__ == "__main__":
    process_data(data=pd.DataFrame())

