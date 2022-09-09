import weakref


class Car:

    def __init__(self, w):
        self.wheels = w

    def get_wheels(self):
        return self.wheels


c1 = Car(4)
c2 = c1     # No of references: 2
print("cq memory location: ", hex(id(c1)))
r = weakref.ref(c1)
print("before : ", r)
c1 = None     # No of references: 1, c1 object will become dead and it is removed by garbage collection
print("After: ", r)
print("Garbage Collected immediately")
c2 = Car(5)

