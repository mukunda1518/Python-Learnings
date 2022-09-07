def f1():
    print("Called f1")


def f2(fun):  # Pass function as an argument
    fun()


print(f1)  # Here f1 is object, so we can pass it anywhere as parameter, store in variables

f2(f1)  # f1 passing as parameter


