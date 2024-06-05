# source: https://mathspp.com/blog/twitter-threads/datetime-objects-and-f-strings
from datetime import datetime

if __name__ == "__main__":

    now_ = datetime.now()
    print(f"{now_:%d.%m.%Y}")
    print(f"{now_:%y/%m/%d}")

    x = 1.2345
    print(f"{x:.2f}")
    