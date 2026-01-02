from scripts.algorithms.sorting.common import sort_algo_test


def _merge(left: list[int], right: list[int], nums: list[int]):
    i, j = 0, 0
    while i + j < len(nums):
        # if j == len(right) or (i < len(left) and left[i] < right[j]):
        if j == len(right):
            nums[i+j] = left[i]
            i += 1
        elif i < len(left):
            if left[i] < right[j]:
                nums[i + j] = left[i]
                i += 1
            else:
                nums[i + j] = right[j]
                j += 1
        else:
            nums[i+j] = right[j]
            j += 1

def merge_sort_inplace(nums: list[int]) -> None:
    n = len(nums)
    if n > 1:
        mid = n // 2
        left = nums[:mid]
        right = nums[mid:]
        merge_sort_inplace(nums=left)
        merge_sort_inplace(nums=right)
        _merge(left=left, right=right, nums=nums)


if __name__ == "__main__":
    sort_algo_test(func=merge_sort_inplace, inplace=True)
