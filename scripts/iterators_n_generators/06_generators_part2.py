

class MyContainer:

    def __init__(self, values: list):
        self._values: list = values

    def __iter__(self):
        for x in self._values:
            yield x


if __name__ == "__main__":

    values_ = [1, 5, 2, 10, 7, 3, 112, 32]
    myc = MyContainer(values=values_)

    for i in myc:
        print(f"{i=}")

