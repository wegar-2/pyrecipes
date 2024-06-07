# source: https://mathspp.com/blog/twitter-threads/datetime-objects-and-f-strings
from typing import Final
from datetime import datetime
import pytz

ALMATY_TIME: Final = pytz.timezone("Asia/Almaty")

if __name__ == "__main__":

    now_ = datetime.now()
    print(f"{now_:%d.%m.%Y}")
    print(f"{now_:%y/%m/%d}")

    print(f"{now_=}")
    now_ = now_.replace(tzinfo=ALMATY_TIME)
    print(f"{now_=}")

    print(f"{now_:%Y/%m/%d %H:%M:%S.%f %z}")
