# References: decorators with optional parameters:
# (1) https://realpython.com/primer-on-python-decorators/
# (2) https://github.com/dabeaz/python-cookbook/blob/master/src/9/defining_a_decorator_that_takes_an_optional_argument/example.py


from functools import partial, wraps
from itertools import product
from typing import Callable, Optional, Any, TypeAlias, Union

from loguru import logger
import pandas as pd

from data.data import load_data

NewColsDict: TypeAlias = dict[str, Any]
ReturnsDF: TypeAlias = Callable[[pd.DataFrame], pd.DataFrame]


def add_lags(
        data: pd.DataFrame,
        cols: Union[str, tuple[str, ...]],
        lags: Union[int, tuple[int, ...]] = (-1, 1)
) -> pd.DataFrame:
    """
    Add all lags of columns cols
    :param data: data set
    :param cols: tuple of columns' names
    :param lags: tuple of lags to be added
    :return: dataset with added lags of cols
    """
    if len(sd := set(cols).difference(set(data.columns))) != 0:
        raise ValueError(f"Columns {sd=} not available in data! ")
    for c, l in product(cols, lags):
        data[f"{c}_lag{l}"] = data[c].shift(l)
    return data

# ----------------------- PROBLEM DESCRIPTION ---------------------------------
# write a decorator whose parameter is a dictionary whose keys are names
# of the columns to be created and its values are scalars that are
# values of the new columns


def pycookbook_style_decor(
        func: Optional[ReturnsDF] = None,
        *,
        ncs: Optional[NewColsDict] = None,
) -> Callable:

    if ncs is None:
        ncs = {"COL1": 1234, "COL2": 6789}
        logger.info(f"Setting default value of mutable optional argument to "
                    f"{ncs=}")

    if func is None:
        return partial(pycookbook_style_decor, ncs=ncs)

    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info("getting data")
        data = func(*args, **kwargs)
        logger.info("adding columns with constants")
        for k, v in ncs.items():
            data[k] = v
        return data

    return wrapper


def realpython_style_decor(
        func: Optional[ReturnsDF] = None,
        *,
        ncs: Optional[NewColsDict] = None,
):
    if ncs is None:
        ncs = {"COL1": 1234, "COL2": 6789}
        logger.info(f"Setting default value of mutable optional argument to "
                    f"{ncs=}")

    def outer(func_: ReturnsDF):
        @wraps(func)
        def inner(*args, **kwargs):
            logger.info("getting data")
            data = func_(*args, **kwargs)
            logger.info("adding columns with constants")
            for k, v in ncs.items():
                data[k] = v
            return data
        return inner

    if func is None:
        return outer
    else:
        return outer(func_=func)


# @pycookbook_style_decor
@pycookbook_style_decor(ncs={"name": "KGHM_SA"})
def add_kgh_cols(data: pd.DataFrame) -> pd.DataFrame:
    return add_lags(data=data, cols=("kgh_close", "kgh_high"), lags=(1, 2, 3))


@realpython_style_decor
# @realpython_style_decor(ncs={"name": "USDCNY_FX_RATE"})
def add_usdcny_cols(data: pd.DataFrame) -> pd.DataFrame:
    return add_lags(data=data, cols=("usdcny_close", "usdcny_high"), lags=(1, 2, 3))


if __name__ == "__main__":
    datas = load_data()
    kgh: pd.DataFrame = datas["kgh"].copy(deep=True)
    usdcny: pd.DataFrame = datas["usdcny"].copy(deep=True)

    # kgh = add_kgh_cols(data=kgh)
    usdcny = add_usdcny_cols(data=usdcny)
    print("end")
