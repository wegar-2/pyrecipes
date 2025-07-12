import random


class MySmallClass:

    def __init__(self, value):
        self.value = value

    def another_value(self):
        return random.uniform(0, 1)

    def __getattribute__(self, item):
        print(f"Inside self.__getattribute__ with {item=}")
        return object.__getattribute__(self, item)

    def __getattr__(self, item):
        print(f"Inside self.__getattr__ with {item=}")
        return "got ya!"


if __name__ == "__main__":

    obj = MySmallClass(123)

    print(f"{obj.value=}")
    print("\n")

    print(f"{obj.another_value()=}")
    print("\n")

    print(f"{getattr(obj, 'qwerty')=}")
    print("\n")

    # here - __dict__ member is accessedR
    print(f"{obj.__dict__=}")
    print("\n")

    # note: __getattribute___ returns item=__dict__ which is subsequently accessed via key
    print(f"{obj.__dict__['value']=}")
    print("\n")