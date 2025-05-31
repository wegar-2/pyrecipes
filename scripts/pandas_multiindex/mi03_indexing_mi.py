import pandas as pd

from scripts.pandas_multiindex.mi00_make_data import make_mi_data


if __name__ == "__main__":
    data = make_mi_data(add_mi=True)

    # get all columns with index level1 value: "kgh"
    kgh_data = data.loc[:, ("kgh", slice(None))]
    print(kgh_data)
    # get all columns with index level1 value: "kgh" or "hgc"
    hgc_kgh_data1 = data.loc[:, (["hgc", "kgh"], slice(None))]

    # get all columns with index level2 value: "close"
    close_data = data.loc[:, (slice(None), "close")]
    print(close_data)

    # get an arbitrary collection of data: all kgh and all opens
    # it is necessary to use pd.concat + remove duplicated columns
    kgh_data = data.loc[:, ("kgh", slice(None))]
    open_data = data.loc[:, (slice(None), "open")]
    custom_data = pd.concat([kgh_data, open_data], axis=1)
    custom_data = custom_data.loc[:, ~custom_data.columns.duplicated()]

    print("end")
