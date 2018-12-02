from functools import wraps
import time

def timed(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        start = time.monotonic()
        result = f(*args, **kwargs)
        end = time.monotonic()
        print(f'{f.__name__} - {end-start:.5f} seconds')
        return result
    return wrapper