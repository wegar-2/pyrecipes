

def insertionSort1(n, arr):
    # Write your code here
    if n == 1:
        return arr

    value = arr[n - 1]
    print(f"{value=}")

    j = n - 2
    while j >= 0:
        print(f"{j=}")
        if arr[j] > value:
            arr[j + 1] = arr[j]
            if j == 0:
                arr[0] = value
            print(" ".join([str(x) for x in arr]))
        else:
            arr[j + 1] = value
            print(" ".join([str(x) for x in arr]))
            break
        j -= 1


if __name__ == "__main__":
    arr = [2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
    n = len(arr)
    insertionSort1(n, arr)
