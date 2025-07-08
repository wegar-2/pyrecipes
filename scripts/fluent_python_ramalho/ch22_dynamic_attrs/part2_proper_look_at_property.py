

class Point:
    """
    Demonstration of creating class property using property() constructor
    """

    def __init__(self, x=1, y=2):
        self._x = x
        self._y = y

    def set_x(self, x):
        print(f"Setting x to {x}")
        self._x = x

    def get_x(self):
        return self._x

    x = property(
        fget=get_x, # noqa
        fset=set_x # noqa
    )


class MyClass:

    data = "class member"

    @property
    def prop(self):
        return "value of property"


if __name__ == "__main__":

    # p = Point()
    # print(f"{p.x=}")
    # p.x = 33331 # noqa
    # print(f"{p.x=}")
    # print("\n\n")

    obj = MyClass()
    print(f"{MyClass.prop=}")
    print(f"{MyClass.data=}")
    print(f"{obj.prop=}")
    print(f"{obj.data=}")
    print("\n\n")

    try:
        obj.prop = "instance prop value"
    except AttributeError:
        print(f"Caught {AttributeError}")

    obj.__dict__["prop"] = "manually set prop in __dict__"

    # when property prop is defined on class - shadows __dict__ member
    print(f"{obj.__dict__=}")
    print(f"{obj.prop=}")
    MyClass.prop = None
    print(f"{obj.__dict__=}")
    print(f"{obj.prop=}")

    # when class variables is defined - does NOT shadow __dict__ member - cf. case of property above!
    print(f"{obj.__dict__=}")
    obj.__dict__["data"] = "instance data value"
    print(f"{obj.__dict__=}")
    print(f"{obj.data=}")



    print("halt")
