

class MetaClass(type):

    def __new__(mcls, name, bases, class_dict, **kwargs):
        print("Inside __new__")
        new_class = type.__new__(mcls, name, bases, class_dict)
        return new_class

    def __init__(self, name, bases, class_dict, **kwargs):
        print("Inside __init__")
        super().__init__(self)


class Klass(metaclass=MetaClass):
    pass


if __name__ == "__main__":
    obj = Klass()
