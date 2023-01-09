from memory_profiler import memory_usage
from timeit import default_timer


def check(func):
    def wrapper(*args):
        m1 = memory_usage()
        t1 = default_timer()
        res = func(args[0])
        m2 = memory_usage()
        t2 = default_timer()
        return res, m2[0] - m1[0], t2 - t1
    return wrapper
