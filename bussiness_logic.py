import datetime


def dictionary_conversion(values):
    list_json = []

    for tup in values:
        c = {
            "emp_id": tup[0],
            "name": tup[1],
            "email": tup[2],
            "phone": tup[3],
            "address": tup[4],
            "metadata": tup[5],
            "created_on": tup[6]
        }
        list_json.append(c)
    return list_json
