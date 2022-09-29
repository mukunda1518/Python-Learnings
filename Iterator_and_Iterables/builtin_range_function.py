class MyRange:
    def __init__(self, start, end):
        self.value = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        curr_val = self.value
        self.value += 2
        return curr_val


nums = MyRange(1, 10)
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))

for num in nums:
    print(num)


# Generator

def my_range(start, end):
    current = start
    while current < end:
        yield current
        current += 1


nums1 = my_range(100, 107)
for num in nums1:
    print(num)

