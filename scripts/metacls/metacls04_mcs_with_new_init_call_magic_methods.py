# Reference:
# (1) Python Docs: https://docs.python.org/3/reference/datamodel.html
# Quote:
#
# """"3.2.8.8. Classes
# Classes are callable. These objects normally act as factories for new
# instances of themselves, but variations are possible for class types that
# override __new__(). The arguments of the call are passed to __new__() and,
# in the typical case, to __init__() to initialize the new instance.""""
#
#
# KEY TAKEAWAY: if __call__ is defined for a class, the class INSTANCES
# become callable.
# This has consequences for Python metaclasses: since any class that has
# a metaclass with __call__ method defined is considered an instance of
# that metaclass, then the call of that class using Klass(...) redirects
# the execution to the metaclass' __call__.
# Therefore, if you want your class to instantiate using the standard call,
# you need to provide the right behavior inside the metaclass' __call__
#
# Also cf. references:
# (2) https://discuss.python.org/t/init-versus-call/14065/2
# (3) https://www.datasciencecentral.com/understanding-the-complexity-of-metaclasses-and-their-practical-2/
# (4) https://eli.thegreenplace.net/2011/08/14/python-metaclasses-by-example
# (5) https://www.geeksforgeeks.org/how-to-use-__call__-method-instead-of-__new__-of-a-metaclass-in-python/

class MyMetaClass(type):

    def __new__(cls, *args, **kwargs):
        print("metaclass __new__")
        class_ = super().__new__(cls, *args, **kwargs)
        return class_

    def __init__(cls, *args, **kwargs):
        print("metaclass __init__")
        super(MyMetaClass, cls).__init__(*args, **kwargs)
        # alternative working approach:
        # super().__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        print("metaclass __call__")
        instance = cls.__new__(
            cls, *args, **kwargs # noqa
        )
        cls.__init__(instance, *args, **kwargs)
        return instance


class Point2d(metaclass=MyMetaClass):

    def __init__(self, x, y):
        print("class __init__")
        self.x = x
        self.y = y

    def __call__(self, *args, **kwargs):
        print("class __call__")


if __name__ == "__main__":
    
    print("Runnning command: p = Point2d(x=1, y=3)")
    p = Point2d(x=1, y=3)

    print("Running command: p()")
    p()
