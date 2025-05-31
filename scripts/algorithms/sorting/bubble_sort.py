

def bubble_sort(l: list[int]) -> list[int]:
    for i in range(len(l)-1):
        for j in range(len(l) - i - 1):
            if l[j] >= l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
            else:
                continue
    return l


if __name__ == "__main__":
    l = [101, 3, 5, 1, 67, 45, 1, 5, 101]
    print(f"{l=}")
    bubble_sort(l=l)
    print(f"{l=}")
