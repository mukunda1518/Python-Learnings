class Foo:
    def show(self):
        print("hi")


def add_attribute(self):
    self.z = 10


Test = type("Test", (Foo, ), {"x": 5, "add_attribute": add_attribute})


t = Test()
t.wy = "hello"
print(t.x)
print(t.wy)

t.show()
t.add_attribute()
print(t.z)