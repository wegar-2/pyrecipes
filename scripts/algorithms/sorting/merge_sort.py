# reference: https://www.geeksforgeeks.org/merge-sort/

from typing import TypeAlias

__all__ = [
    "merge_sort"
]

IntList: TypeAlias = list[int]


def _split_in_half(list_: IntList) -> tuple[IntList, IntList]:
    half_len, _ = divmod(len(list_), 2)
    return list_[:half_len], list_[half_len:]


def _merge_lists(left: IntList, right: IntList) -> IntList:
    li: int = 0
    ri: int = 0
    list_out: IntList = []
    while (li < len(left)) or (ri < len(right)):
        if li == len(left):
            list_out.extend(right[ri:])
            break
        elif ri == len(right):
            list_out.extend(left[li:])
            break
        elif (lv := left[li]) < right[ri]:
            list_out.append(lv)
            li += 1
        elif left[li] > (rv := right[ri]):
            list_out.append(rv)
            ri += 1
        else:
            list_out.extend([left[li], right[ri]])
            li += 1
            ri += 1
    return list_out


def merge_sort(list_: IntList) -> IntList:
    if len(list_) == 1:
        return list_
    left, right = _split_in_half(list_=list_)
    return _merge_lists(merge_sort(list_=left), merge_sort(list_=right))


if __name__ == "__main__":
    my_list = [1, 11, 3, 19, 81, 51, 33, 901, 3, 4, 2, 8]
    print(merge_sort(list_=my_list))
