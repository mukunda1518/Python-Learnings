my_list = [1, 2, 3, 4,5]

sq_list = map(lambda x: x**2, my_list)
print(list(sq_list))


list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
sum_list = map(lambda x, y: x + y, list1, list2)
print(list(sum_list))