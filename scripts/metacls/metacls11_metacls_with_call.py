from typing import get_type_hints
from inspect import get_annotations


class AnotherMetaclass(type):

    def __new__(mcls, name, bases, class_dict, **kwargs):
        print(f"Inside metaclass {mcls} method __new__ called")
        klass = type.__new__(mcls, name, bases, class_dict)
        return klass

    def __call__(cls, *args, **kwargs):
        print(f"Inside metaclass {cls} method __call__")
        klass = AnotherMetaclass.__new__(
            mcls=AnotherMetaclass,
            name=cls.__name__,
            bases=(),
            class_dict={}
        )
        return klass


class MyVault(metaclass=AnotherMetaclass):
    pass


if __name__ == "__main__":
    myv = MyVault()
