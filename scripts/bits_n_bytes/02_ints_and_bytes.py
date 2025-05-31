

def int_to_bytes(x: int) -> bytes:
    return x.to_bytes(length=(x.bit_length() + 7) // 8, byteorder="big")


def bytes_to_int(x: bytes) -> int:
    return int.from_bytes(bytes=x, byteorder="big")


if __name__ == "__main__":

    for k in range(0, 332, 1):
        print(f"{k}: {int_to_bytes(x=k)=}")

    x: int = 331
    x_bytes: bytes = int_to_bytes(x=x)
    print(f"{x=}")
    print(f"{x_bytes=}")

    x_recov = bytes_to_int(x=x_bytes)
    print(f"{x_recov=}")
