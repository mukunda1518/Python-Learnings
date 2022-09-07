def f1(func):

    def wrapper(*args, **kwargs):  # As we don't know what will be the parameters. So we use args and kwargs
        print("Started")
        func(*args, **kwargs)
        print("Ended")
    return wrapper


@f1
def f(msg, name="Harry"):
    print(msg, name)


f("Hello", "Peter")
