from typing import Any, Final, Type


class DataDescriptor:

    def __set_name__(self, owner, name):
        print(f"Inside set_name method")
        self._public_name: str = name
        self._private_name: str = f"_{name}"

    def __set__(self, instance, value):
        print(f"Inside class {self.__class__.__name__} dunder set; "
              f"putting {self._public_name} to {value}")
        instance.__dict__[self._private_name] = value

    def __get__(self, instance, owner):
        print(f"Inside class {self.__class__.__name__} dunder get; "
              f"retrieving {self._public_name}")
        if instance is None:
            return self
        return instance.__dict__[self._private_name]


class NonDataDescriptor:

    _instance_counter: int = 0
    _NAME: Final[str] = "_serial_number"

    def __init__(self):
        self._serial_number: int = self._instance_counter + 1
        self._instance_counter += 1

    def __get__(self, instance, owner):
        if instance is not None:
            if self._NAME not in instance.__dict__:
                instance.__dict__[self._NAME] = self._instance_counter
            return instance.__dict__[self._NAME]
        return self


class MyContainer:
    data_desc = DataDescriptor()
    non_data_desc = NonDataDescriptor()

    def __init__(self, dd_val=1):
        self.data_desc = dd_val


def access_attrib(cls_or_obj: Type | Any, attrib_name: str):
    cls_ = type(cls_or_obj)
    if cls_ is type:
        cls_ = cls_or_obj
    try:
        return getattr(cls_, attrib_name)
    except AttributeError:
        raise AttributeError(
            f"Class {cls_} has no member {attrib_name}!; "
            f"class based off of object {cls_or_obj}"
        )


def is_non_data_descriptor(
        cls_or_obj: Type | Any,
        attrib_name: str
):
    attrib = access_attrib(cls_or_obj, attrib_name)
    return hasattr(attrib, "__get__")


def is_data_descriptor(
        cls_or_obj: Type | Any,
        attrib_name: str
):
    attrib = access_attrib(cls_or_obj, attrib_name)
    return hasattr(attrib, "__set__") and hasattr(attrib, "__get__")


if __name__ == "__main__":

    myc = MyContainer()
    print(f"{myc.data_desc=}")
    myc.data_desc = 1

    print(f"{myc.non_data_desc=}")

    print(f"{is_data_descriptor(myc, 'data_desc')=}")
    print(f"{is_non_data_descriptor(myc, 'non_data_desc')=}")

    print("halt")
