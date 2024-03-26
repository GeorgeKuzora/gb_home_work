import logging
import time
from functools import wraps

logging.basicConfig(level="DEBUG")
logger = logging.getLogger(__name__)


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        finish = time.perf_counter()
        logger.info(f"function {func} took {finish-start} seconds to complete")
        return result

    return wrapper
