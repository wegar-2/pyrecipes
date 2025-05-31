
def xor_lists(l1: list, l2: list):
    # ensure that l1 is always at least as long as l2
    if len(l1) < len(l2):
        l1, l2 = l2, l1
    # add trailing zeros to l2
    if 0 < (len_diff := (len(l1) - len(l2))):
        l2 = l2 + [0] * len_diff
    out = []
    for i in range(max(len(l1), len(l2))):
        out.append((l1[i] + l2[i]) % 2)
    return out

def evaluate_vector_on_basis_modulo(vec: list, basis: list, m: int) -> int:
    res = 0
    for i, v in enumerate(vec):
        res = (res + v * basis[i]) % m
    return res


def xorAndSum(a, b):

    MOD = 10 ** 9 + 7
    LIMIT = 314159

    a_bin = bin(a)[2:]
    b_bin = bin(b)[2:]

    a_ar = [int(x) for x in list(a_bin)][::-1]
    b_ar = [int(x) for x in list(b_bin)][::-1]

    M = max(len(a_ar), len(b_ar))

    powers_cache = [1]
    for i in range(1, LIMIT + M):
        powers_cache.append(powers_cache[-1]*2 % MOD)

    a_ar_value = (
        evaluate_vector_on_basis_modulo(vec=a_ar, basis=powers_cache, m=MOD)
    )
    b_ar_value = (
        evaluate_vector_on_basis_modulo(vec=b_ar, basis=powers_cache, m=MOD)
    )

    result = 0
    for i in range(0, M, 1):
        if i > 0:
            b_ar = [0] + b_ar
        xor_result = xor_lists(l1=a_ar, l2=b_ar)
        result = (
            result +
            evaluate_vector_on_basis_modulo(
                vec=xor_result, basis=powers_cache, m=MOD
            )
        ) % MOD

        if i > 0:
            b_ar_value = (2*b_ar_value) % MOD

    for i in range(M, LIMIT + 1):
        b_ar_value = (2 * b_ar_value) % MOD
        result = (result + a_ar_value + b_ar_value) % MOD

    return result


if __name__ == "__main__":
    a = 0b10
    b = 0b1010
    # res = xorAndSum(a, b)
    # print(res) # 489429555

    from math import comb
    comb(10_000, 2430)
    from itertools import combinations
    list(combinations(["a", "b", "c"], 2))