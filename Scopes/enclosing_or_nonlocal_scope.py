def outer_func():
    var = 100

    def inner_func():
        nonlocal var
        var += 1
        print(f"Printing var from inner_func(): {var}")
        # print(f"Printing var from inner_func(): {another_var}")  # Gets error because another_var defined after this function call
    inner_func()
    print(f"Printing var from outer_func(): {var}")
    another_var = 100


outer_func()
