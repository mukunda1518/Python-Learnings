nums = [1, 2, 3]

i_nums = iter(nums)

# print(i_nums)
# print(dir(i_nums))

# print(next(i_nums))
# print(next(i_nums))
# print(next(i_nums))

while True:
    try:
        item = next(i_nums)
        print(item)
    except StopIteration:
        break

# for num in nums:
#     print(num)

# print(dir(nums))
# print(next(nums))  TypeError: 'list' object is not an iterator
