

class Point(object):

    def __new__(cls, *args, **kwargs):
        print(f"Inside class {cls.__name__} method {cls.__new__.__name__}")
        obj = super().__new__(cls)
        return obj

    def __init__(self, x, y):
        print(f"Inside {self.__class__.__name__} method "
              f"{self.__init__.__name__}")
        self._x = x
        self._y = y

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y


if __name__ == "__main__":

    def Point3d_init(self, x, y, z):
        print(f"Inside {self.__class__.__name__} method "
              f"{Point3d_init.__name__}")
        super(self.__class__, self).__init__(x, y)
        self._z = z

    Point3d = type(
        "Point3d", # noqa
        (Point, ),
        {
            "__init__": Point3d_init,
            "get_z": lambda self: self._z
        }
    )

    p = Point(1, 3)
    p3d = Point3d(1, 2, 3)
    print(f"{p3d.get_z()=}")
