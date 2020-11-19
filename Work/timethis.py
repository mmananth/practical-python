import time

def timethis(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print('%s.%s: %f' %(func.__module__, func.__name__, end-start))
    return wrapper

@timethis
def countdown(n):
    while n>0:
        n -= 1

countdown(10000000)