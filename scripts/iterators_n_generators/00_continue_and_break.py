

if __name__ == "__main__":

    for k in range(0, 100_000):
        x = None
        try:
            x = 10 / k
        except ZeroDivisionError:
            print(f"{ZeroDivisionError} caught")
            continue

        if x is None:
            print(f"failed to carry out the division")
        else:
            print(f"{x=}")

        if x == 1:
            print("breaking as x = 1")
            break
