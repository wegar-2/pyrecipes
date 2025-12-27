import math


def longest_consecutive_subsequence_solve(nums: list[int]):
    res = 0
    nums = set(nums)
    longest_subseq = set()

    for x in nums:
        if x - 1 not in nums:
            subseq = set()
            subseq.add(x)
            iter_len = 1
            while x + 1 in nums:
                iter_len += 1
                subseq.add(x + 1)
                x += 1
            if iter_len > res:
                longest_subseq = subseq
                res = iter_len

    return res, longest_subseq

if __name__ == "__main__":
    lst = [1, 7, 2, 5, 3, 110, 54, 33, 12, 6, 77, 4]

    res = longest_consecutive_subsequence_solve(nums=lst)
    print(f"{res=}")
