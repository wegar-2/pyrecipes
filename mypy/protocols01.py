# Protocols MyPy doc: https://mypy.readthedocs.io/en/stable/protocols.html

from typing import Protocol

import pandas as pd


class FitPredictProtocol(Protocol):

    def fit(
            self,
            X: pd.DataFrame,  # noqa
            y: pd.DataFrame
    ) -> pd.DataFrame:
        pass

    def predict(
            self,
            X: pd.DataFrame  # noqa
    ) -> pd.DataFrame:
        pass


def backtest(
        models: list[FitPredictProtocol],
        X_train: pd.DataFrame,  # noqa
        X_test: pd.DataFrame,  # noqa
        y_train: pd.DataFrame,
):
    for model in models:
        model.fit(X=X_train, y=y_train)
        y_hat = model.predict(X=X_test)
        print(y_hat)


if __name__ == "__main__":
    pass
