from pathlib import Path
from typing import TypeAlias

import pandas as pd

DataDict: TypeAlias = dict[str, pd.DataFrame]


def load_data() -> DataDict:
    p: Path = Path(__file__).parent
    paths: list[Path] = list(p.glob(pattern="*.csv"))
    datas: DataDict = {}
    for path in paths:
        datas[path.name.split(".")[0][:-2]] = pd.read_csv(
            path,
            parse_dates=["Date"]
        )
    return datas


if __name__ == "__main__":

    datas = load_data()

    print("done")
