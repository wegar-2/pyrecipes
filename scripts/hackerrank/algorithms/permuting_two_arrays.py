

def two_arrays(k, A, B):
    A = sorted(A)
    B = sorted(B)
    for i in range(len(A)):

        print(f"Iteration {i}")
        print(f"{A=}")
        print(f"{B=}")

        for j in range(i, len(A)):
            if (A[i] + B[j] >= k) and (j <= len(A) - 1):
                B[i], B[j] = B[j], B[i]
                break
            elif j == len(A) - 1:
                return False
    return True


if __name__ == "__main__":

    k = 10
    A = [5, 6, 7]
    B = [3, 4, 5]
    # B = [3, 4, 1]

    res = two_arrays(k, A, B)
    print(f"{res=}")
