


def my_insert_sort(arr: list[int]):

    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
            else:
                break
        print(", ".join([str(x) for x in arr]))


if __name__ == "__main__":
    l = [10, 11, 4, 1, 909, 23]
    my_insert_sort(arr=l)
