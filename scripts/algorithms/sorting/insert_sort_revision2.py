from scripts.algorithms.sorting.common import sort_algo_test


def insert_sort(nums: list[int]) -> list[int]:
    for i in range(1, len(nums)):
        value = nums[i]
        j = i
        while j > 0 and nums[j-1] > value:
            nums[j] = nums[j-1]
            j -= 1
        nums[j] = value
    return nums


if __name__ == "__main__":
    sort_algo_test(
        func=insert_sort,
        inplace=False
    )
