import time


def cache(func):
    cache={}
    def wrapper(*args):
        print(cache)

        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args]=result
        return result
    return wrapper


@cache
def long_fun(a,b):
    time.sleep(5)
    return a+b


print(long_fun(2,4))
print(long_fun(2,4))
print(long_fun(5,5))