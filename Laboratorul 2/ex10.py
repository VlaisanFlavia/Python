def merge_lists(*input_lists):
    max_length = max(len(lst) for lst in input_lists)
    result = []

    for i in range(max_length):
        new_tuple = tuple(lst[i] if i < len(lst) else None for lst in input_lists)
        result.append(new_tuple)

    return result


list1 = [1, 2, 3]
list2 = [5, 6, 7]
list3 = ["a", "b", "c"]

result = merge_lists(list1, list2, list3)
print(result)