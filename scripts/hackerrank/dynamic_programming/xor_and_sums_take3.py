
MOD = 100_000_007

def get_modular_residues(x: int = 1, m: int = MOD) -> list[int]:

    if x >= MOD:
        raise ValueError

    residues: list[int] = []

    cond: bool = True
    i = 1

    while cond:
        if (el := x % m) not in residues:
            residues.append(el)
            x = 2*x % m

            if len(residues) == 100_000*i:
                print(f"{len(residues)=}")
                i += 1

        else:
            return residues


if __name__ == "__main__":
    res = get_modular_residues(x=1, m=MOD)
    print(res)
