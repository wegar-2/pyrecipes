from typing import Any, Callable, Type


def log_method_call(x: Any, method: Callable) -> None:
    print("\n")
    print(f"Method {method.__name__} called "
          f"from class {x.__class__.__name__} instance")
    print("\n")


class MySimpleMetaclass(type):

    def __new__(mcls, name, bases, class_dict, **kwargs) -> Type:
        print("\n")
        print(f"Inside {mcls.__name__} method "
              f"{mcls.__new__.__name__}")
        new_class: Type = super().__new__(mcls, name, bases, class_dict)
        print(f"{name=}")
        print(f"{bases=}")
        print(f"{class_dict=}")
        print(f"{kwargs=}")
        print("\n")
        return new_class


class MyClass(metaclass=MySimpleMetaclass):
    def __init__(self):
        log_method_call(self, self.__init__)


class MyAnotherClass(metaclass=MySimpleMetaclass, x=1, y=2):
    def __init__(self):
        log_method_call(self, self.__init__)


if __name__ == "__main__":

    obj1 = MyClass()
    print("\n")

    obj2 = MyAnotherClass()
