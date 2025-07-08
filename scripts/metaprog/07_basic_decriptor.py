

class MyDescriptor:

    def __init__(self, name: str):
        self._name: str = name

    def __get__(self, instance, owner):
        print(f"Inside MyDescriptor method self.__get__.__name__ - "
              f"retrieving {self._name}")
        return instance.__dict__[self._name]

    def __set__(self, instance, value):
        print(f"Inside MyDescriptor method self.__set__.__name__ - setting "
              f"{self._name} to {value}")
        instance.__dict__[self._name] = value
        print(f"After setting {self._name} to {value}")


class MyContainer:
    name = MyDescriptor("name")
    value = MyDescriptor("value")

    def __init__(self, name, value):
        print(f"{self.__dict__=}")
        self.name = name
        self.value = value

    def __getattribute__(self, item):
        print(f"Inside class MyContainer method __getattribute__; {item=}")
        return object.__getattribute__(self, item)

    def __getattr__(self, item):
        print(f"Inside class MyContainer method __getattr__")
        return "Fallback value"


if __name__ == "__main__":
    my_container = MyContainer(name="salary", value=10_000)
