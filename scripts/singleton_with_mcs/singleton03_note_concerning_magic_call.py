
class Point2d:

    def __new__(cls, *args, **kwargs):
        print("inside __new__")
        return super().__new__(cls)

    def __init__(self, x, y):
        print("inside __init__")
        self.x = x
        self.y = y

    def __call__(self, *args, **kwargs):
        print("called __call__ of point2d")


if __name__ == "__main__":
    p = Point2d(2, 3)
    print(f"{p.__call__()=}")

    # HOW CALLING __CALL__ on a class works
    # using type class call to create instance of Point2d by:
    # (1) call to type's __call__ means that we do parenthesised call to
    #     instances of type, i.e. to classes
    # (2) class Point2d is an instance of type, since it is a class that
    #     (implicitly) inherits from object
    # (3) this call results in calling __new__ and __init__ method (in this order)
    p2 = type.__call__(Point2d, 33, 11)
    print(f"{p2.x=}")

    # Note: calling __call__ on class and passing it class instance results in
    # (as expected) normal execution of the call method in the intended manner,
    # i.e. by running it as a parenthesised call on an instance
    Point2d.__call__(p)

    print("end")
