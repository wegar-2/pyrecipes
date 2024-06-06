from itertools import count


if __name__ == "__main__":
    for i in count(start=15, step=7):
        if i > 1_000:
            break
        print(i)
        