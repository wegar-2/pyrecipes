import sys


p = 1_000_000_007
N = 314_159


def my_xor(a: int, b: int, i: int) -> int:
    return (a ^ (b << i)) % p


def my_sum(a: int, b: int, n: int) -> int:
    lower_sum = my_sum(a=a, b=b, n=n-1)
    elem = my_xor(a=a, b=b, i=n)
    return (lower_sum + elem) % p


def xor_and_sum(a: int, b: int) -> int:
    sum_ = 0
    for i in range(N + 1):
        sum_ = (sum_ + my_xor(a=a, b=b, i=i)) % p
        print(f"{i}: {sum_}")
    return sum_


if __name__ == "__main__":

    # a = 0b1010100011
    # b = 0b1011110001
    # a = 0b0010
    # b = 0b1010
    # res = xor_and_sum(a, b)
    # print(res)
    s = "101"
    int(s, 2)
