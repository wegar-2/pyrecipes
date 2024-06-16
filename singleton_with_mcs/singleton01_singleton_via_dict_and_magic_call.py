# Reference: https://refactoring.guru/design-patterns/singleton/python/example


class SingletonMeta(type):

    _INSTANCES_DICT: dict = {}

    def __call__(cls, *args, **kwargs):
        if cls not in SingletonMeta._INSTANCES_DICT:
            print(f"class {cls} instance does not yet exist")
            # 1. create instance using super: start after cls=Point2d to
            # create instance normally
            instance = super(SingletonMeta, cls).__call__(*args, **kwargs)

            # # 2. create instance normally using __new__ + __init__ calls:
            # instance = cls.__new__(cls, *args, **kwargs)
            # cls.__init__(instance, *args, **kwargs)

            # # 3. call type's __call__ directly
            # type.__call__(cls, *args, **kwargs)

            SingletonMeta._INSTANCES_DICT[cls] = instance
        return SingletonMeta._INSTANCES_DICT[cls]


class Point2d(metaclass=SingletonMeta):

    def __new__(cls, *args, **kwargs):
        print(f"class {cls.__class__.__name__} __new__ called")
        instance = super(Point2d, Point2d).__new__(cls)
        return instance

    def __init__(self, x, y):
        print(f"class {self.__class__.__name__} __init__ called")
        self.x = x
        self.y = y

    def __call__(self, *args, **kwargs):
        print(f"class {self.__class__.__name__} __call__ called")


if __name__ == "__main__":

    p1 = Point2d(123, 33)
    p2 = Point2d(1, 2)

    print(f"{(p1 is p2)=}")
    print(p1.x == 123)

    # COMMENTARY: