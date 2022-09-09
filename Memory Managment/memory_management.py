# Resource : https://www.youtube.com/watch?v=arxWaw-E8QQ


class Car:
    def __init__(self):
        pass


x = 10
print(type(x))

y = x
if id(x) == id(y):
    print("x and y refer to the same object")

x = x + 1
if id(x) != id(y):
    print("x and y refer to Different objects!")

z = 10
if id(y) == id(z):
    print("y and z points to the same memory!!")   # Shocking for me
else:
    print("y and z points to different memory")

z = Car()
print(type(z))


# Everything is object in python
# Python is dynamically typed language
