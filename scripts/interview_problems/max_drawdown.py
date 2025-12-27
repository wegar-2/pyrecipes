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


def calculate_max_drawdown(data: pd.DataFrame) -> pd.DataFrame:
    data["cum_max_close"] = data["close"].expanding().apply(lambda x: max(x))
    data["current_drawdown"] = data["close"] - data["cum_max_close"]
    data["current_max_drawdown"] = data["current_drawdown"].expanding().min()
    return data


if __name__ == "__main__":
    data = load_data()
    data = calculate_max_drawdown(data=data)
