

def two_sum_solve(nums: list[int], target: int) -> tuple[int, int] | None:
    checked: dict = {}

    for i, x in enumerate(nums):
        rest = target - x

        if rest in checked:
            return i, checked[rest]

        if x not in checked:
            checked[x] = i

    return None




def check_solution(nums: list[int], target: int, i: int, j: int) -> bool:
    if nums[i] + nums[j] == target:
        return True
    return False


if __name__ == "__main__":
    nums = [10, 4, 11, 7, 4, 3, 1, 5, 8, 1, 1, 3]
    target = 19
    solution = two_sum_solve(nums, target)
    if solution is not None:
        print(check_solution(nums, target, *solution))
