from scripts.algorithms.sorting.common import generate_array_for_sorting

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

    for k in range(1000):
        nums = generate_array_for_sorting()
        from copy import deepcopy
        backup = deepcopy(nums)
        merge_sort(nums=nums)
        builtin_sort = sorted(backup)
        # [nums[i] != builtin_sort[i] for i in range(len(nums))].index(True)
        # nums[238:243]
        # builtin_sort[238:243]
        # len(nums)
        # len(builtin_sort)
        if nums != builtin_sort:
            raise Exception("Error")
