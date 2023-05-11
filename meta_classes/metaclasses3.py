class ExampleMeta(type):

    def __new__(self, class_name, bases, attrs):
        print(class_name, bases, attrs)

        a = {}
        for name, val in attrs.items():
            if name.startswith("--"):
                a[name] = val
            else:
                a[name.upper()] = val

        print(a)
        return type(class_name, bases, a)


class Dog(metaclass=ExampleMeta):
    x = 5
    y = 10

    def hello(self):
        print("hi")


d = Dog()
print(d.X)
print(d.Y)





