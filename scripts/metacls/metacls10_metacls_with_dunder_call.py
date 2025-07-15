from typing import Callable

import numpy as np
import pandas as pd


class MyMetaClass(type):

    @staticmethod
    def _make_data() -> pd.DataFrame:
        return pd.DataFrame(np.random.randn(10_000).reshape(-1, 10))

    @staticmethod
    def _make_custom_init(dim) -> Callable:
        def custom_init(self):
            for k in range(1, dim + 1, 1):
                setattr(self, f"data{k}", MyMetaClass._make_data())
        return custom_init

    def __new__(mcls, name, bases, class_dict, **kwargs):
        new_class = super().__new__(mcls, name, bases, class_dict)
        if "dim" in kwargs:
            new_class.__init__ = mcls._make_custom_init(dim=kwargs["dim"])
        return new_class

    def __call__(
            mcls,
            *args,
            **kwargs
    ):
        print(f"Metaclass {mcls.__name__} method "
              f"{mcls.__call__.__name__} called; {mcls=}; {args=}; {kwargs=}")
        instance = mcls.__new__(
            mcls, # noqa
            *args,
            **kwargs
        )
        instance.__init__(*args, **kwargs)
        return instance


class MyClass(metaclass=MyMetaClass, dim=3):
    _instance_counter: int = 0


if __name__ == "__main__":
    data_pieces = MyClass()

    for k in range(1, 4, 1):
        data_piece = getattr(data_pieces, f'data{k}')
        print(f"data_piece #{k}: ", data_piece.head().to_string())

