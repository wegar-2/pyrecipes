import random


class MetaClass(type):

    def __new__(mcls, name, bases, class_dict, **kwargs):
        print(f"Inside {mcls.__name__} method __new__; "
              f"{mcls=}; {name=}; {bases=}; {class_dict=}; {kwargs=}")
        new_class = type.__new__(mcls, name, bases, class_dict)

        def set_value(self, value):
            self.value = value

        def get_value(self):
            return self.value

        def get_instance_count(cls):
            return cls.instance_count

        def increment_instance_count(cls):
            cls.instance_count = cls.instance_count + 1

        new_class.prop = property(
            fset=set_value,
            fget=get_value
        )
        new_class.get_instance_count = classmethod(get_instance_count)
        new_class.increment_instance_count = (
            classmethod(increment_instance_count))
        return new_class

    def __init__(
            cls,
            name,
            bases,
            class_dict,
            **kwargs
    ):
        print(f"Inside {cls.__class__.__name__} method __init__; "
              f"{cls=}; {name=}; {bases=}; {class_dict=}; {kwargs=}")
        super().__init__(cls)
        print(f"Setting class {cls.__name__} counter to zero")
        cls.instance_count = 0


class Klass(metaclass=MetaClass):
    def __init__(self):
        random_value = random.uniform(0, 1)
        print(f"Inside class {self.__class__.__name__} __init__; "
              f"setting the value to {random_value}")
        self.value = random_value
        instance_num: int = getattr(self, "get_instance_count")() + 1
        getattr(self.__class__, "increment_instance_count")()
        print(f"Completed creation of instance #{instance_num:05}")


if __name__ == "__main__":

    obj = Klass()
    obj.value = 123
    print(f"{obj.value=}")

    more_instances: list[Klass] = []
    for _ in range(10):
        more_instances.append(Klass())
