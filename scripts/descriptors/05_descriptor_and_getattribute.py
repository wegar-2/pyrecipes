

class DataDescriptor:

    def __set_name__(self, owner, name):
        self._name: name = name

    def __set__(self, instance, value):
        print(f"Inside {self.__class__.__name__} method __set__ with "
              f"{instance=}; {value=}")
        instance.__dict__[self._name] = value

    def __get__(self, instance, owner):
        print(f"Inside {self.__class__.__name__} method __get__ with "
              f"{instance=}; {owner=}")
        if instance is None:
            return self
        return instance.__dict__[self._name]


class ManagedClass:

    data_desc = DataDescriptor()

    def __init__(self, value=111):
        self.data_desc = value

    def __getattribute__(self, item):
        if item == "__class__":
            return ManagedClass
        print(f"Inside {self.__class__.__name__} class call to "
              f"__getattribute__ with {item=}")
        return object.__getattribute__(self, item)

    def __getattr__(self, item):
        print(f"Falling back to __getattr__ of {self.__class__.__name__}...")
        return "Fallback value! "

    def __setattr__(self, key, value):
        object.__setattr__(self, key, value)


if __name__ == "__main__":
    mc = ManagedClass()
