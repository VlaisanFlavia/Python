def compare_dicts(dict1, dict2):
    if set(dict1.keys()) != set(dict2.keys()):
        return False

    for key in dict1.keys():
        value1 = dict1[key]
        value2 = dict2[key]

        if value1 != value2:
            return False

        if isinstance(value1, dict):
            if not compare_dicts(value1, value2):
                return False
        elif isinstance(value1, (list, set)):
            if len(value1) != len(value2):
                return False
            for item1, item2 in zip(value1, value2):
                if type(item1) != type(item2):
                    return False
                if isinstance(item1, dict):
                    if not compare_dicts(item1, item2):
                        return False
                elif isinstance(item1, (list, set)):
                    if not compare_lists(item1, item2):
                        return False
                elif item1 != item2:
                    return False
        elif value1 != value2:
            return False

    return True


def compare_lists(list1, list2):
    if len(list1) != len(list2):
        return False
    for item1, item2 in zip(list1, list2):
        if type(item1) != type(item2):
            return False
        if isinstance(item1, dict):
            if not compare_dicts(item1, item2):
                return False
        elif isinstance(item1, (list, set)):
            if not compare_lists(item1, item2):
                return False
        elif item1 != item2:
            return False
    return True


dict1 = {
    "name": "Flavia",
    "age": 20,
    "address": {"city": "Iasi", "zipcode": 700064},
    "hobbies": ["volunteering", "walking"],
}

dict2 = {
    "name": "Iulia",
    "age": 26,
    "address": {"city": "Iasi", "zipcode": 700064},
    "hobbies": ["reading", "walking"],
}

result = compare_dicts(dict1, dict2)
print(result)  # True
