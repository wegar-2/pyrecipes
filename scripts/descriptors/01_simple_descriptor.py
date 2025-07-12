from typing import Final


class CustomMember:

    def __init__(self, name: str):
        self._name: Final[str] = name

    def __get__(self, instance, owner):
        print(f"Getting {self._name} from {type(instance)} instance")
        return instance.__dict__[self._name]

    def __set__(self, instance, value):
        print(f"Setting {self._name} on {type(instance)} instance")
        instance.__dict__[self._name] = value


class MyContainer:
    value = CustomMember("value")
    special_value = CustomMember("special_value")


if __name__ == "__main__":

    myc = MyContainer()
    myc.value = 123
    myc.special_value = 4321

    myc.__dict__["value"] = 909
    print(myc.value)

    myc.value = 333
    print(myc.value)
