# Demonstration of MRO

class X:
    pass


class Y:
    pass


class Z:
    pass


class A(X, Y):
    pass


class B(Y, Z):
    pass


class M(B, A, Z):
    pass


order_list = [i.__name__ for i in M.mro()]
print(order_list)  # Order - All its siblings classes and then parents classes
