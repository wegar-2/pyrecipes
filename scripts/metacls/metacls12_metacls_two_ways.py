from typing import Callable, Final
import random


class MetaValueStore(type):

    def __new__(mcls, name, bases, class_dict, **kwargs):
        print(f"Inside {mcls.__name__} method __new__ call")

        def set_value(self, value):
            print(f"{self.__class__.__name__} method set_value called")
            self._value = value

        def get_value(self):
            print(f"{self.__class__.__name__} method get_value called")
            return self._value

        class_dict.update({
            "_value": None,
            "set_value": set_value,
            "get_value": get_value
        })

        return type(
            name,
            bases,
            class_dict
        )


class MyVault(metaclass=MetaValueStore):
    pass


class MetaCoords(type):

    _DEFAULT_DIM: Final[int] = 5

    @staticmethod
    def _getter_factory(k) -> Callable:
        def _coord_getter(self):
            print(f"Inside class {self.__class__.__name__} getter of x{k}")
            return getattr(self, f"_x{k}")
        return _coord_getter

    @staticmethod
    def _setter_factory(k) -> Callable:
        def _coord_setter(self, value):
            print(f"Inside class {self.__class__.__name__} setter of x{k}")
            setattr(self, f"_x{k}", value)
        return _coord_setter

    def __new__(mcls, name, bases, class_dict, **kwargs):
        print(f"Inside {mcls.__name__} method __new__")

        for k in range(1, mcls._DEFAULT_DIM + 1, 1):
            value = random.uniform(0, 1)
            print(f"Adding property x{k}={value} for the class {name}")

            class_dict.update({
                f"_x{k}": value,
                f"x{k}": property(
                    fget=mcls._getter_factory(k=k),
                    fset=mcls._setter_factory(k=k)
                )
            })

        return type.__new__(mcls, name, bases, class_dict)

class MyBoringClass(metaclass=MetaCoords):
    pass


if __name__ == "__main__":

    myv = MyVault()
    myv.set_value(123) # noqa
    print(f"{myv.get_value()=}") # noqa
    print(myv)
    print("=====================\n")

    mybc = MyBoringClass()
    for k in range(1, 6, 1):
        print(f"{getattr(mybc, f'x{k}')=}")