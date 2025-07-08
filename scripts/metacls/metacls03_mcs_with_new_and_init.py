from typing import Type


class MyMetaclass(type):

    def __new__(mcs, name, bases, class_dict, **kwargs) -> Type:
        print("metaclass __new__")
        new_class: Type = super().__new__(mcs, name, bases, class_dict)
        new_class.class_member = "set inside metaclass!"
        return new_class


class Point2d(metaclass=MyMetaclass):
    def __init__(self, x, y):
        print("class __init__")
        self.x = x
        self.y = y


if __name__ == "__main__":
    print(f"{getattr(Point2d, 'class_member')=}")
    p = Point2d(1, 3)
    print(f"{p.x=}")
