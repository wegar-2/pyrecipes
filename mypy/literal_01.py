from typing import Literal


def make_stuff(which: Literal["float", "int", "bool"]):
    if which == "float":
        return 1234.56789
    elif which == "int":
        return 1234
    elif which == "bool":
        return True


if __name__ == "__main__":
    print(f"{make_stuff(which='float')=}")
    print(f"{make_stuff(which='int')=}")
    print(f"{make_stuff(which='bool')=}")
