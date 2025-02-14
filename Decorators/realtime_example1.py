def before_after(func):
    def wrapper(*args):
        print("Before")
        func(*args)
        print("After")
    return wrapper


class Test:
    @before_after
    def decorated_method(self):
        print("run")


t_obj = Test()
t_obj.decorated_method()


