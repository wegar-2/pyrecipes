

def solve_valid_parentheses(s: str) -> bool:
    symbols = list(s)
    checksum = 0
    for x in symbols:
        if x == "(":
            checksum += 1
        else:
            checksum -= 1

        if checksum < 0:
            return False

    if checksum == 0:
        return True
    return False


if __name__ == "__main__":
    s_valid = "()()(()())(())((()())())"
    s_invalid = "((()()())(((()"

    print(f"{solve_valid_parentheses(s_valid)=}")
    print(f"{solve_valid_parentheses(s_invalid)=}")
