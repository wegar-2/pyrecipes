import pandas as pd

from pandas_multiindex.mi00_make_data import make_mi_data


if __name__ == "__main__":
    data = make_mi_data(add_mi=True)
    data.loc[:, ("mynumber", "")] = 123
    print("end")
