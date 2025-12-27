

def find_enclosing_pair(heights: list[int], low: int, high: int):
    left = low
    right = high
    while left < right:
        if heights[left] == 0:
            left += 1
        elif heights[right] == 0:
            right -= 1
        if heights[left] > 0 and heights[right] > 0:
            break
    return left, right


def trapping_rain_water_solve(heights: list[int]):

    left, right = find_enclosing_pair(heights, 0, len(heights) - 1)
    filled_heights = [x for x in heights]
    water_units = [0] * len(heights)

    max_left_height = heights[left]
    max_right_height = heights[right]

    while left < right:
        left_height = max(heights[left], max_left_height)
        right_height = max(heights[right], max_right_height)

        if left_height <= right_height:
            if heights[left + 1] < left_height:
                filled_heights[left + 1] = left_height
                water_units[left + 1] = left_height - heights[left + 1]
                left += 1
            else:
                max_left_height = heights[left + 1]
                left += 1
        else:
            if heights[right - 1] < right_height:
                filled_heights[right - 1] = right_height
                water_units[right - 1] = right_height - heights[right - 1]
                right -= 1
            else:
                max_right_height = heights[right - 1]
                right -= 1

    return filled_heights, water_units


if __name__ == "__main__":
    heights_ = [4, 2, 0, 3, 2, 5]
    # heights_ = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    res = trapping_rain_water_solve(heights_)
    print(f"{heights_=}")
    print(f"{res[0]=}")
    print(f"{res[1]=}")
    print(f"{sum(res[1])=}")
