

def two_sum_on_sorted_array_solve(nums: list[int], target: int) -> None | tuple[int, int]:
    left, right = 0, len(nums) - 1
    while left < right:
        left_value = nums[left]
        right_value = nums[right]
        rest = target - left_value
        while right_value > rest:
            right_value = nums[right]
            right -= 1
        if nums[right] == rest and left < right:
            return left, right
        left += 1
        right += 1
    return None


if __name__ == "__main__":
    # rng = np.random.default_rng(seed=123_456)
    # rng.integers(0, 100_000, size=30)
    # nums_ = [11, 5, 34, 1, 90, 190, 6, 4, 5]
    # sorted_nums = sorted(nums_)
    sorted_nums = [1, 4, 5, 5, 6, 11, 11,  34, 90, 190]
    print(f"{sorted_nums=}")
    target = 22
    res = two_sum_on_sorted_array_solve(nums=sorted_nums, target=target)
    print(res)