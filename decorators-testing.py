import datetime as dt
import time

import functools



def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        dt_start = dt.datetime.now()
        print(f"function {func.__name__} start processing at {dt_start}")

        result = func(*args, **kwargs)

        dt_finish = dt.datetime.now()
        print(f"function {func.__name__} processing {dt_finish - dt_start}")

        return result

    return wrapper

# my_func = my_decorator(my_func)

@my_decorator
def my_func():
    print("i'm working!")
    time.sleep(2)
    print("i'm done!")

print(my_func.__name__)
print(help(my_func))
my_func()
