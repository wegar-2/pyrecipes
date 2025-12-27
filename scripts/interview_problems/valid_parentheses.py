

def valid_parentheses(s: str):
    stack_: list = []

    for i, l in enumerate(s):
        if i == 0:
            stack_.append(l)
        else:
            if l in ["(", "{", "["]:
                stack_.append(l)
            else:
                if len(stack_) > 0:
                    if (l == ")" and stack_[-1] == "(") or (l == "}" and stack_[-1] == "{") or (l == "]" and stack_[-1] == "["):
                        stack_.pop()
                    else:
                        return False
                return False

    if len(stack_) == 0:
        return True
    return False


if __name__ == "__main__":
    # print(valid_parentheses("()[]"))
    print(valid_parentheses("([])"))
    # print(valid_parentheses("([)]"))
