from abc import ABC, abstractmethod


class Computer(ABC):

    @abstractmethod
    def process(self):
        pass


class Laptop(Computer):

    def process(self):
        print("It worked")


class Programmer:
    def work(self):
        print("Solving complex problems")

# Uses
#

com = Laptop()
com.process()
