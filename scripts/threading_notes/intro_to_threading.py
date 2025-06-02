# Reference: https://realpython.com/intro-to-python-threading/#starting-a-thread

import threading
import logging
import time

logger = logging.getLogger(__name__)


def my_configure_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s ::: %(name)s ::: %(levelname)s ::: %(message)s'
    )



def called_in_thread(name):
    logger.info(f'Starting thread {name}')
    time.sleep(5)
    logger.info(f'Ending thread {name}')


if __name__ == "__main__":

    my_configure_logging()

    logger.info("before creating thread...")
    threads = threading.Thread(
        target=called_in_thread,
        args=("qwerty", )
    )

    logger.info("before starting thread...")
    threads.start()
    threads.join(10)
    logger.info("after starting thread...")
