import pandas as pd

from scripts.interview_problems.common import load_data


def calculate_max_drawdown(data: pd.DataFrame) -> pd.DataFrame:
    data["cum_max_close"] = data["close"].expanding().apply(lambda x: max(x))
    data["current_drawdown"] = data["close"] - data["cum_max_close"]
    data["current_max_drawdown"] = data["current_drawdown"].expanding().min()
    return data


if __name__ == "__main__":
    data = load_data()
    data = calculate_max_drawdown(data=data)
