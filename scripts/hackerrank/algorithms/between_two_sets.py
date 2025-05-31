import math


def between_two_sets(a: list[int], b: list[int]):
    gcd_b = math.gcd(*b)
    lcm_a = math.lcm(*a)
    solutions_counter = 0
    for x in range(lcm_a, gcd_b+1, 1):
        if (x % lcm_a == 0) and (gcd_b % x == 0):
            solutions_counter += 1
    return solutions_counter


