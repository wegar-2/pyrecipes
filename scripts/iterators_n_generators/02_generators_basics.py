

def gnums(n: int = 5):
    for i in range(n):
        yield i


def yfgen(m: int = 2, n: int = 5):
    for i in range(m):
        yield from gnums(n=n)


if __name__ == "__main__":

    for i, x in enumerate(gnums()):
        print(f"{i}: {x=}")

    for i, x in enumerate(yfgen()):
        print(f"{i}: {x=}")
