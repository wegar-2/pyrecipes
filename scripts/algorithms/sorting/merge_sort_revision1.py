from scripts.algorithms.sorting.common import sort_algo_test


def _merge(left: list[int], right: list[int], nums: list[int]):
    i, j = 0, 0
    while i + j < len(nums):
        if j == len(right) or (i < len(left) and left[i] < right[j]):
            nums[i+j] = left[i]
            i += 1
        else:
            nums[i+j] = right[j]
            j += 1


def merge_sort(nums: list[int]) -> None:
    if len(nums) < 2:
        pass
    else:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        merge_sort(nums=left)
        merge_sort(nums=right)
        _merge(left, right, nums)


if __name__ == "__main__":
    sort_algo_test(func=merge_sort, inplace=True)
