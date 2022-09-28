# Resource: https://www.educative.io/answers/what-are-pickling-and-unpickling-in-python
# Difference between Pickle and json : https://www.educba.com/python-pickle-vs-json/
import pickle
import json
my_list = [15, 'Python', 'Hello World']
my_list1 = [15, 20, 40, 80, 100]

# Pickling
with open("data.pickle", "wb") as file_handle:
    pickle.dump(my_list, file_handle, pickle.HIGHEST_PROTOCOL)

# Unpickling
with open("data.pickle", "rb") as file_handle:
    retrieved_date = pickle.load(file_handle)
    print(retrieved_date)

json_list = json.dumps(my_list)
print(json_list)
print(json.loads(json_list))

with open("data1.pickle", "wb") as fi:
    pickle.dump(my_list1, fi)

with open("data.pickle", "rb") as fi:
    print(pickle.load(fi))

