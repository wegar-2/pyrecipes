

def reverse_string_with_pointers(s: str) -> str:
    lst: list[str] = list(s)
    i, j = 0, len(lst) - 1
    while i < j:
        lst[i], lst[j] = lst[j], lst[i]
        i += 1
        j -= 1
    return "".join(lst)


def check_solution(s: str, rev_s: str) -> bool:
    if s[::-1] == rev_s:
        return True
    return False


if __name__ == "__main__":
    str_ = "qwertpoiuityru"
    rev_str = reverse_string_with_pointers(s=str_)
    print(check_solution(s=str_, rev_s=rev_str))
