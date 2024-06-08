from pathlib import Path
from typing import TypeAlias

import pandas as pd

DataDict: TypeAlias = dict[str, pd.DataFrame]


def load_data() -> DataDict:
    p: Path = Path(__file__).parent
    paths: list[Path] = list(p.glob(pattern="*.csv"))
    paths = sorted(paths)
    datas: DataDict = {}
    for path in paths:
        name: str = path.name.split(".")[0][:-2]
        data: pd.DataFrame = pd.read_csv(path, parse_dates=["Date"])
        data = data.set_index("Date")
        data.columns = [
            f"{name.replace('_', '')}_{c}".lower()
            for c in data.columns
        ]
        data = data.loc[:, [c for c in data.columns
                            if not c.endswith("volume")]]
        datas[name] = data
    return datas


if __name__ == "__main__":

    datas = load_data()

    print("done")
