

class MyClass:

    def __init__(self, value=12):
        self.value = value

    def __getattribute__(self, item):
        print(f"Inside __getattribute__; {item=}")
        if item == "__class__":
            print("Requested __class__ attribute")
            return MyClass
        return object.__getattribute__(self, item)


if __name__ == "__main__":

    obj = MyClass()
    print(f"{obj.value=}")
    print(f"{obj.__class__=}")

