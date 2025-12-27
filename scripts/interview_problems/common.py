from pathlib import Path

import pandas as pd


def load_data() -> pd.DataFrame:
    data = pd.read_csv(
        Path(__file__).parent / "data" / "mbank_2001-2020.csv",
        decimal=".",
        sep=","
    )
    data.columns = [x.lower() for x in data.columns]
    data["date"] = pd.to_datetime(data["date"])
    return data[["date", "close"]]

