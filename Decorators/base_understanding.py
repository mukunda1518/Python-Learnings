

# Use of decorators
# Functions - Used for to do certain task
# Decorators are used to add additional functionality or modify the code of functions

def div(a, b):
    print(a / b)


def smart_div(func):

    def inner(a, b):
        if a < b:
            a, b = b, a
        return func(a, b)
    return inner


div1 = smart_div(div)
div1(2, 4)