

def generator1():
    for k in range(4):
        yield k


def generator2():
    yield "start"
    yield from generator1()
    yield "end"


if __name__ == "__main__":
    for i, x in enumerate(generator2(), start=1):
        print(f"### {i} ###: {x}")