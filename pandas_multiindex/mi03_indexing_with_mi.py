import pandas as pd

from pandas_multiindex.mi00_make_data import make_mi_data


if __name__ == "__main__":
    data = make_mi_data(add_mi=True)

    # get all columns with index level1 value: "kgh"
    kgh_data = data.loc[:, ("kgh", slice(None))]
    print(kgh_data)
