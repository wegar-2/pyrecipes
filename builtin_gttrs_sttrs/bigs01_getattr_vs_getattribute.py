# References:
# (1) SO's How to implement __getattribute__ without infinite recursion error?:
#     https://stackoverflow.com/questions/371753/how-do-i-implement-getattribute-without-an-infinite-recursion-error/371833#371833
# (2) Tutorial @ Medium:
# https://medium.com/@satishgoda/python-attribute-access-using-getattr-and-getattribute-6401f7425ce6

class A:

    ALLOWED_MEMBERS = ["x"]

    def __init__(self, value):
        self.value = value

    def __getattr__(self, item):
        print(f"Called: A.__getattr__()")
        return "A_default"

    def __getattribute__(self, item):
        print(f"Called: A.__getattribute__()")
        # NOTE: class members are NOT accessed via __getattr__ / __getattribute__
        if item in A.ALLOWED_MEMBERS:
            print("allowed member")
        # alternative ways of calling __getattribute__ without triggering a
        # chain of infinite recursive calls
        # return super(A, self).__getattribute__(item)
        return object.__getattribute__(self, item)


if __name__ == "__main__":

    a_obj: A = A(value=123)
    print(f"{a_obj=}")

    print("call1")
    print(f"{a_obj.value=}")

    print("call2")
    print(f"{a_obj.__dict__['value']=}")

    print("call3")
    print(f"{a_obj.x=}")

    print("call4")
    # print(f"{A.CVAR=}")