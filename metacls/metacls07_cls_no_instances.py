import numpy as np
import pandas as pd


class NoInstancesAllowed(type):

    def __new__(mcs, name, bases, class_dict, **kwargs):
        class_ = super().__new__(mcs, name, bases, class_dict)
        return class_

    def __call__(cls, *args, **kwargs):
        raise TypeError(f"Class {cls.__name__} is not instantiable! ")


class DataProcessor(metaclass=NoInstancesAllowed):

    @staticmethod
    def add_column(data: pd.DataFrame) -> pd.DataFrame:
        return data.assign(NEW_COLUMN=12345)


if __name__ == "__main__":
    dat = pd.DataFrame(
        data=np.random.randn(30).reshape(10, 3),
        columns=["A", "B", "C"]
    )

    try:
        datp = DataProcessor()
    except TypeError as te:
        print(f"As expected, caught TypeError: {te}")

    dat = DataProcessor.add_column(data=dat)

    print("end")

