

class MyDescriptor:

    def __set_name__(self, owner, name):
        print(
            f"Inside {self.__set_name__.__name__};"
            f"{self=}; {owner=}; {name=}; setting name"
        )
        self._name: str = name

    def __set__(self, instance, value):
        print(
            f"Inside {self.__set__.__name__}; setting {self._name} to {value};"
            f"{instance=}"
        )
        instance.__dict__[self._name] = value

    def __get__(self, instance, owner):
        print(f"Inside {self.__set__.__name__}; getting {self._name}; "
              f"{instance=}")
        if instance is None:
            return self
        return instance.__dict__[self._name]


class MyData:

    member1 = MyDescriptor()
    member2 = MyDescriptor()

    # def __init__(self, member1, member2):
    #     print(
    #         f"Inside {self.__init__} method. "
    #     )
    #     self.member1 = member1
    #     self.member2 = member2

    def __getattribute__(self, item):
        print(
            f"Inside __getattribute__ method __getattribute__ "
            f"{item=}"
        )
        # if hasattr()
        return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        object.__setattr__(self, key, value)


if __name__ == "__main__":

    myd = MyData()
    myd.member1 = 123
