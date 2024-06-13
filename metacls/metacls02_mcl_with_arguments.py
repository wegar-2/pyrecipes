

class MyMeta(type):

    def __new__(mcs, name, bases, class_dict, **kwargs):
        print(f"Creating class {name} with {bases=} and {class_dict=}")
        class_ = super().__new__(mcs, name, bases, class_dict)
        if kwargs:
            print("There are class members to set on class")
            for k, v in kwargs.items():
                print(f"setting: {k} = {v}")
                setattr(class_, k, v)
        return class_


class MyClass(metaclass=MyMeta, x=123, y=234):

    def __init__(self, value):
        self.value = value


if __name__ == "__main__":

    obj = MyClass(1)
    print(f"{obj.__dict__=}")
    print({f"{MyClass.__dict__=}"})
    print(obj)
