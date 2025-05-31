from itertools import product


def pick_numbers(arr: list[int]):

    distinct_pairs = list(set([
        tuple(sorted(list(x)))
        for x in product(arr, arr)
        if abs(x[0] - x[1]) <= 1
    ]))

    if len(distinct_pairs) == 0:
        return 0

    lengths = []
    for pair in distinct_pairs:
        lengths.append(len([x for x in pair]))

    return max(lengths)


if __name__ == "__main__":
    a = [4, 6, 5, 3, 3, 1]
    pick_numbers(arr=a)
