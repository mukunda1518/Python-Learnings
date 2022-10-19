unflat_json = {'user':
               {'Rachel':
                {'UserID': 1717171717,
                 'Email': 'rachel1999@gmail.com',
                 'friends': ['John', 'Jeremy', 'Emily']
                 }
                }
               }


def flatten_json(data):
    flatten_dict = {}

    def flatten(data, name=""):

        if type(data) is dict:

            for key in data:
                flatten(data[key], name + key + "_")

        elif type(data) is list:
            i = 0
            for item in data:
                flatten(item, name + str(i) + "_")
                i += 1
        else:
            flatten_dict[name[:-1]] = data

    flatten(data)
    return flatten_dict


print(flatten_json(unflat_json))


