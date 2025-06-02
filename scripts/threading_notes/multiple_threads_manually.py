# Reference: https://realpython.com/intro-to-python-threading/#starting-a-thread

import threading
import logging
import time
import scripts
from common.common import make_random_bit_sequence

logger = logging.getLogger(__name__)


def worker(thread_num: int, n: int = 10_000_000):
    logger.info(f"Starting thread {thread_num}")

    for j in range(5, 0, -1):
        logger.info(f"Starting processing in {thread_num}-th thread in "
                    f"{j} seconds")
        time.sleep(1)

    logger.info(f"Generating {n:_} random bits")
    x = make_random_bit_sequence(n=n)

    logger.info("Summing bits...")
    s: int = sum(x)
    logger.info(f"Sum={s:_}")

    logger.info(f"Starting thread {thread_num}")


if __name__ == "__main__":

    threads_list: list[threading.Thread] = []

    logger.info("before iteratively spawning threads...")
    for k in range(1, 4, 1):
        logger.info(f"before spawning {k}-th thread")
        thread_ = threading.Thread(
            target=worker,
            args=(k, ),
            name=f"my_thread_{str(k)}"
        )
        logger.info(f"saving {k}-th thread into list")
        threads_list.append(thread_)
        logger.info(f"spawning {k}-th thread into list")
        thread_.start()
        logger.info(f"after spawning {k}-th thread")

    for i, thread_ in enumerate(threads_list, start=1):
        logger.info(f"before joining {k}-th thread")
        thread_.join()
        logger.info(f"{k}-th thread joined! ")
