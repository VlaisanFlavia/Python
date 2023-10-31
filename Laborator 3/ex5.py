def validate_dict(rules, dictionary):
    for key, prefix, middle, suffix in rules:
        if key in dictionary:
            value = dictionary[key]
            if not value.startswith(prefix) or not value.endswith(suffix):
                return False
            middle_start = value.find(middle)
            if middle_start == -1 or middle_start == 0 or middle_start == len(value) - len(middle):
                return False
        else:
            return False
    return True


rules = {("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}
dictionary = {"key1": "come inside, it's too cold out", "key3": "this is not valid"}

result = validate_dict(rules, dictionary)
print(result)
