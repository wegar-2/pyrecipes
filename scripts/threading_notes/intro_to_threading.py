# Reference: https://realpython.com/intro-to-python-threading/#starting-a-thread

import threading
import logging
import time
import scripts

logger = logging.getLogger(__name__)


def called_in_thread(name):
    logger.info(f'Starting thread {name}')
    time.sleep(5)
    logger.info(f'Ending thread {name}')


if __name__ == "__main__":

    logger.info("before creating thread...")
    threads = threading.Thread(
        target=called_in_thread,
        args=("qwerty", ),
        name="my_thread"
    )

    logger.info("before starting thread...")
    threads.start()
    threads.join(10)
    logger.info("after starting thread...")
