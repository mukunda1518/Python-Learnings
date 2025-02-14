def f1(func):

    def wrapper(*args, **kwargs):  # As we don't know what will be the parameters. So we use args and kwargs
        print("Started")
        val = func(*args, **kwargs)
        print("Ended")
        return val
    return wrapper


@f1
def f(msg, name="Harry"):
    print(msg, name)


@f1
def add(x, y):
    return x + y


f("Hello", "Peter")
print(add(4, 5))
