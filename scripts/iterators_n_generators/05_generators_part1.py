

if __name__ == "__main__":

    gen1_ = (x**2 for x in range(10))
    while True:
        try:
            print(f"{next(gen1_)=}")
        except StopIteration:
            print(f"Exception {StopIteration.__name__} caught...")
            break
