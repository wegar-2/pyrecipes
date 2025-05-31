# sources:
# (1) https://stackoverflow.com/questions/5067604/determine-function-name-from-within-that-function
# (2) https://stackoverflow.com/questions/4492559/how-to-get-current-function-into-a-variable

import inspect
from inspect import stack


def my_add(x: int, y: int) -> int:
    print(f"{stack()[0][3]=}")
    print(f"{inspect.currentframe().f_code.co_name=}")
    print(f"{get_current_function_name()=}")
    return x + y


def get_current_function_name() -> str:
    return stack()[1][3]


if __name__ == "__main__":
    my_add(12, 1)

    # Running this prints:
    # stack()[0][3]='my_add'
    # inspect.currentframe().f_code.co_name='my_add'
    # get_current_function_name()='my_add'
