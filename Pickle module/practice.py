# Resource: https://www.educative.io/answers/what-are-pickling-and-unpickling-in-python
# Difference between Pickle and json : https://www.educba.com/python-pickle-vs-json/
import pickle
import json
my_list = [15, 'Python', 'Hello World']


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

