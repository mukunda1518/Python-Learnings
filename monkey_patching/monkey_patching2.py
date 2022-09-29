import monkey_patching


def handson_function(self):
    print("Handson function is called")


monkey_patching.A.func = handson_function
obj = monkey_patching.A()
obj.func()
