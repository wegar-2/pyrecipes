from itertools import chain


if __name__ == "__main__":

    l1 = ["a", "d", "q"]
    l2 = ["f", "m"]

    chain_ = [x for x in chain(l1, l2)]
    print(f"chain_ cnctnd: {', '.join(chain_)}")

    chain_itbs_ = [x for x in chain.from_iterable([l2, l1])]
    print(f"chain_itbs_ cnctnd: {', '.join(chain_itbs_)}")