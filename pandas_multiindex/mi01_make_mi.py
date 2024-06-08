import pandas as pd

from pandas_multiindex.mi00_make_data import make_mi_data


if __name__ == "__main__":

    # note that index is named: "Date"
    data = make_mi_data()
    # multiindex from product
    mi = pd.MultiIndex.from_product([
        ["hgc", "kgh", "usdcny"],
        ["open", "high", "low", "close"]
    ], names=["asset", "ohlc_attrib"])
    data_mi = data.copy(deep=True)
    data_mi.columns = mi
    # slice dates range
    print(data_mi.loc["2022-01-01":"2022-01-10", :])
    # multiindex from tuples
    mi = list(mi)
    mi = pd.MultiIndex.from_tuples(mi, names=["asset", "ohlc_attrib"])
    data_mi.columns = mi

    print("end")
