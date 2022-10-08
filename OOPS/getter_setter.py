class Employee:

    def __init__(self, first, last):
        self._first = first
        self._last = last

    @property
    def first(self):
        print("Getter method called")
        return "First name: {}".format(self._first)

    @property
    def last(self):
        print("Getter method called")
        return "First name: {}".format(self._last)

    @first.setter
    def first(self, name):
        self._first = name

    @last.setter
    def last(self, surname):
        self._last = surname


emp_1 = Employee("John", "Smith")


print(emp_1.first)
print(emp_1.last)

emp_1.first = "hello"
emp_1.last = "hello2"

print(emp_1.first)
print(emp_1.last)

