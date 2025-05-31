# References:
# (1) .stack(): https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.DataFrame.stack.html
# (2) .unstack(): https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.DataFrame.unstack.html#pandas.DataFrame.unstack

import numpy as np

from notebooks.pandas_multiindex.mi00_make_data import make_mi_data


if __name__ == "__main__":

    data = make_mi_data(add_mi=True)

    # melting with multiindex on columns
    stacked_data = data.stack(level=1, future_stack=True)
    unstacked_data = stacked_data.unstack(level=1, fill_value=np.nan)

    # swapping multiindex levels
    unstacked_data.columns = unstacked_data.columns.swaplevel(0, 1)
    perm, _ = unstacked_data.columns.sortlevel(level=[0, 1], ascending=[True, True])
    unstacked_data = unstacked_data.loc[:, perm]

    print("done")
