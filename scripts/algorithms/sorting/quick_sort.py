from typing import Annotated, Literal, TypeAlias
from annotated_types import Ge

QuickSortPivotType: TypeAlias = Literal["first", "last"]
NonNegInt: TypeAlias = Annotated[int, Ge(0)]


__all__ = [
    "quick_sort"
]


def _validate_values(values: list) -> None:
    if any(not isinstance(v, int) for v in values):
        print("There are non-int members in the passed values")
    if any(v < 0 for v in values):
        print("There are negative integers in the passed values")


def _partition_values_pivot_last(
        values: list[NonNegInt],
        start: NonNegInt,
        end: NonNegInt
) -> int:
    pivot = values[end]
    print(f"before partition: {values}")
    i = start-1
    for j in range(start, end, 1):
        if values[j] <= pivot:
            i += 1
            values[i], values[j] = values[j], values[i]
    values[i+1], values[end] = values[end], values[i+1]
    print(f"after partition: {values}")
    return i + 1


def _quick_sort_pivot_last(
        values: list[NonNegInt],
        start: int,
        end: int
):
    print(f"before sorting: {values}")
    if start >= end:
        return values
    pivot_position = _partition_values_pivot_last(
        values=values,
        start=start,
        end=end
    )
    _quick_sort_pivot_last(
        values=values,
        start=start,
        end=pivot_position-1
    )
    _quick_sort_pivot_last(
        values=values,
        start=pivot_position+1,
        end=end
    )
    print(f"after sorting: {values}")
    return values


def _quick_sort_pivot_first(
        values: list[NonNegInt],
        start_idx: int,
        end_idx: int
):
    if start_idx >= end_idx:
        return

    # if len(set(values[start_idx:end_idx+1])) == 1:
    #     return None

    pivot_value: NonNegInt = values[start_idx]
    pointer_latest_le_pivot = start_idx
    print(f"before swapping: {values}")
    print(f"processed slice: {values[start_idx:end_idx + 1]}")

    for j in range(start_idx + 1, end_idx + 1):
        if values[j] < pivot_value:
            pointer_latest_le_pivot += 1
            values[pointer_latest_le_pivot], values[j] = (
                values[j], values[pointer_latest_le_pivot])

    values[start_idx], values[pointer_latest_le_pivot] = (
        values[pointer_latest_le_pivot], values[start_idx])

    print(f"after swapping: {values}")
    print(f"processed slice: {values[start_idx:end_idx + 1]}")
    print(f"{pointer_latest_le_pivot=}")

    _quick_sort_pivot_first(
        values=values,
        start_idx=start_idx,
        end_idx=pointer_latest_le_pivot
    )

    _quick_sort_pivot_first(
        values=values,
        start_idx=pointer_latest_le_pivot + 1,
        end_idx=end_idx
    )

    return values


def quick_sort(
        values: list[NonNegInt],
        pivot_type: QuickSortPivotType = "last"
):
    _validate_values(values=values)
    if pivot_type == "last":
        return _quick_sort_pivot_last(
            values=values,
            start=0,
            end=len(values) - 1
        )
    else:
        return _quick_sort_pivot_first(
            values=values,
            start_idx=0,
            end_idx=len(values) - 1
        )


if __name__ == "__main__":
    l_ = [10, 5, 12, 7, 17, 9, 3, 1, 3, 20, 12, 3]
    res = quick_sort(values=l_, pivot_type="first")

    print(f"{res=}")
