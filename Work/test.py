def logged(func):
    def wrapper(*args, **kwargs):
        print('calling', func.__name__)
        return func(*args, **kwargs)
    return wrapper

@logged
def add(x,y):
    return x+y

@logged
def subtract(x,y):
    return x-y

print(add(3,4))
print(subtract(5,1))