def sort_tuple(list_tuple):
    def sort_key(item):
        if len(item[1]) >= 3:
            return item[1][2]
        else:
            return ''

    return sorted(list_tuple, key=sort_key)


input_list = [('abc', 'bcd'), ('abc', 'zza')]
result = sort_tuple(input_list)
print(result)
