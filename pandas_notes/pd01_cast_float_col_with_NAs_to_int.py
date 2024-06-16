import numpy as np
import pandas as pd


def make_data() -> pd.DataFrame:
    return pd.DataFrame(data={
        "int_": [1, 3, 4, np.nan], "float_": [2.2, 1.3, 4.5, np.nan]
    })


if __name__ == "__main__":
    dat = make_data()

    try:
        dat["float_"] = dat["float_"].astype(int)
    except pd.errors.IntCastingNaNError as exc:
        print(f"Caught exception {exc} when trying to cast float column with "
              f"NANs to int type using .astype(int) ")

    try:
        dat["float_"] = dat["float_"].astype(pd.Int64Dtype())
    except TypeError as exc:
        print(f"Caught exception {exc} when trying to cast float column with "
              f"NANs to int type using .astype(pd.Int64Dtype())")

    dat["float_"] = pd.Series(
        data=[pd.NA if pd.isna(x) else int(x) for x in dat["float_"]],
        dtype=pd.Int64Dtype()
    )
    print("using list comprehension works! ")
