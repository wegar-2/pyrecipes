


def move_to_left(arr: list[int]):

    if len(arr) == 1:
        return arr

    n = len(arr)
    value = arr[-1]

    j = n - 2
    while (j >= 0) and (arr[j] > value):
        arr[j], arr[j+1] = arr[j+1], arr[j]
        print(", ".join([str(x) for x in arr]))
        j -= 1

    return arr


def move_to_left_with_for(arr: list[int]):
    pass



if __name__ == "__main__":
    arr = [1, 43, 100, 123, 5]
    move_to_left(arr=arr)
