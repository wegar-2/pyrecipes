import math


def permutations(ar: list) -> list[list]:
    if len(ar) == 1:
        return [ar]
    else:
        out = []
        for el in ar:
            for x in permutations(ar=[y for y in ar if y != el]):
                out.append([el] + x)
        return out


if __name__ == "__main__":

    ar = [1, 2, 3, 4]

    res = permutations(ar=ar)
    print(len(res) == math.factorial(len(ar)))
    print(res)
