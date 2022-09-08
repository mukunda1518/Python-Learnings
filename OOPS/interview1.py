class Animal:

    def __init__(self, color, name):
        self.color = color
        self.__name = name

    def __str__(self):
        return f"My name is : {self.__name} and my color is {self.color}"


class Dog(Animal):

    def __init__(self, color, name, type):
        super().__init__(color, name)
        self.type = type


obj = Animal("White", "Dog")
obj1 = Dog("Black", "Dog", "Domestic")
# print(obj1.__name)
print(obj._Animal__name)


