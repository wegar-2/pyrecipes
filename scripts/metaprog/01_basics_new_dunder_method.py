

class Point:
    """
    This is not a metaclass. __new__ is just enriched with info printing
    """


    def __new__(cls, *args, **kwargs):
        print(f"Inside {Point.__name__} method {Point.__new__.__name__}")
        obj = super().__new__(cls)
        return obj

    def __init__(self, x=1, y=2):
        print(f"Inside {Point.__name__} method {Point.__init__.__name__}")
        self.x = x
        self.y = y

    def __str__(self):
        return f"{Point.__name__}(x={self.x}, y={self.y})"


if __name__ == "__main__":
    p = Point()
    print(p)
    exec(f"p2={str(p)}")
