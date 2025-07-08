
class MyClass:

    def __init__(self, value):
        print(f"Inside class {self.__class__.__name__} method __init__")
        self._value = value

    def __setattr__(self, key, value):
        object.__setattr__(self, key, value)

    def __getattribute__(self, item):
        if item == "__class__":
            return MyClass
        elif item == "__name__":
            return "MyClass"
        else:
            object.__getattribute__(self, item)


if __name__ == "__main__":
    obj = MyClass(value=1234)

