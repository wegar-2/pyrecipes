

if __name__ == "__main__":

    x = 123
    x_bin = bin(x)
    print(x_bin)

    y = 2
    y_shifted = 2 << 1
    print(f"{y=}")
    print(f"{y_shifted=}")

    a = 0b101
    b = 0b001
    print(f"{a=:04b}")
    print(f"{b=:04b}")
    print(f"{(a ^ b)=:04b}")
    print(f"{(a & b)=:04b}")
    print(f"{(a | b)=:04b}")
