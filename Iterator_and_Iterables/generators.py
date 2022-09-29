def square_number(nums):
    for i in nums:
        yield i * i


my_nums = square_number([1, 2, 3, 4, 5, 6])
print(my_nums)
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))
# print(next(my_nums))  Stop iteration


my_nums2 = (x * x for x in [10, 20, 30, 40, 50, 60, 70])  # This is generator
print(my_nums2)

for num in my_nums2:
    print(num)
