# Reference: https://mypy.readthedocs.io/en/stable/more_types.html

from typing import overload, Optional


# -----------------------------------------------------------------------------
# Use-case 1: separating implementation for methods with more parameters
# (while subset of parameters remains common - one-element set {values} in
# the case below).

@overload
def custom_sum(values: list[int]):
    pass


@overload
def custom_sum(values: list[int], multiplier: int):
    pass


def custom_sum(
        values: list[int],
        multiplier: Optional[int] = None
):
    out = sum(values)
    if multiplier is not None:
        return multiplier * out
    return out


# -----------------------------------------------------------------------------
# Use-case 2: separating declarations for method according as the
# parameter(s) types vary


@overload
def my_double(value: int) -> int:
    pass


@overload
def my_double(value: str) -> str:
    pass


def my_double(value: int | str) -> int | str:
    if isinstance(value, int):
        return 2 * value
    if isinstance(value, str):
        return f'{value}{value}'
    raise ValueError(f"Received input of invalid type: "
                     f"{value=}, {type(value)}=")
