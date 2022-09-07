def f1(func):

    def wrapper():
        print("Started")
        func()
        print("Ended")
    return wrapper


@f1
def f():
    print("Hello World")


# f = f1(f)
# f()
# instead of writing above 2 lines  we can simply add decorator(f1) to the f() function and f()

f()
