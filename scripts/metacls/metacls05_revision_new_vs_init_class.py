

class A:
    """
    Using class A to review how the magic methods: __new__ and __init__ work.
    """

    def __new__(cls, x, y):
        print(f"Inside __new__; {x=}, {y=}")
        object_ = super().__new__(cls)
        object_.x = x
        return object_

    def __init__(self, x, y):
        print(f"Inside __init__; {x=}, {y=}")
        self.y = y


if __name__ == "__main__":
    a = A.__new__(A, 23, 33)
    print(f"before init: {a.__dict__=}")
    A.__init__(a, 23, 33)
    print(f"after init: {a.__dict__=}")

    # alternatively: call __init__ on instance and not on class;
    # Note, that it is not necessary to pass self in this case
    a.__init__(x=23, y=33)
