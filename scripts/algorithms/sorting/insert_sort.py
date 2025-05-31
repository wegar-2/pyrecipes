
__all__ = ["insert_sort"]


def insert_sort(values: list[int]):
    for i in range(1, len(values)):
        j = i
        while j >= 1:
            if values[j-1] > values[j]:
                values[j-1], values[j] = values[j], values[j-1]
                j -= 1
            else:
                break
    return values


if __name__ == "__main__":
    l_ = [10, 5, 12, 7, 17, 9, 3, 1, 3, 20, 12, 3]
    res = insert_sort(values=l_)
    print(f"{res=}")
