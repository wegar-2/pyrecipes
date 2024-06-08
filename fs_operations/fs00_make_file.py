from string import ascii_letters

import numpy as np
import pandas as pd


def get_df() -> pd.DataFrame:
    return pd.DataFrame(data={
        "num": np.random.randn(5),
        "let": np.random.choice(list(ascii_letters), size=5, replace=True)
    })
