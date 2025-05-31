from itertools import groupby


if __name__ == "__main__":
    l1 = [1, 1, 0, -1, 0, 1, 0, 0, 0, 1, -1, -1, -1]

    corrected_list = []
    for k, v in groupby(l1):
        lv = list(v)
        print(f"{k}: {lv}")

        if len(lv) == 1:
            corrected_list.append(k)
        else:
            corrected_list.extend([k] + [0] * (len(lv) - 1))
    print(l1)
    print(corrected_list)
