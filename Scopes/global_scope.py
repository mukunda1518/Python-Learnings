var = 100


def func():
    # print(var)  # only accessing works fine
    global var
    var = var + 1


def func2():
    global x
    x = 100
    x = x + 1


def func3():
    global y
    y = 100


func()
func2()
print(x)
global y
func3()
print(y)
