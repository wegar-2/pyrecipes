

class MetaValueStore(type):

    def __new__(mcls, name, bases, class_dict, **kwargs):

        def set_value(self, value):
            print(f"{self.__class__.__name__} method set_value called")
            self._value = value

        def get_value(self):
            print(f"{self.__class__.__name__} method get_value called")
            return self._value

        class_dict.update({
            "_value": None,
            "set_value": set_value,
            "get_value": get_value
        })

        return type(
            name,
            bases,
            class_dict
        )


class MyVault(metaclass=MetaValueStore):
    pass


if __name__ == "__main__":
    myv = MyVault()
    myv.set_value(123)
    print(f"{myv.get_value()=}")
    print(myv)
