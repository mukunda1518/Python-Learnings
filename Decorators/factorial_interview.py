import time

# https://www.geeksforgeeks.org/memoization-using-decorators-in-python/

def memoize_factorial(func):
    memory = {}

    def wrapper(self, num):
        if num not in memory:
            memory[num] = func(self, num)
        return memory[num]
    return wrapper


def time_taken(func):
    def wrapper(*args):
        time_before = time.time()
        val = func(*args)
        time_after = time.time()
        print(time_after - time_before)
        return val

    return wrapper


class FindFactorial:

    @time_taken
    def iterative_apporach(self, num):
        fact = 1
        for i in range(1, num + 1):
            fact *= i
        return fact

    @memoize_factorial
    def recursive_apporach(self, num):
        if num == 1:
            return 1
        return num * self.recursive_apporach(num - 1)


num = 100
obj = FindFactorial()
print(obj.iterative_apporach(num))
print(obj.recursive_apporach(num))