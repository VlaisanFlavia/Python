def find_list(x, *lists):
    for input_list in lists:
        result = []
        item_counts = {}
        for item in input_list:
            if item in item_counts:
                item_counts[item] += 1
            else:
                item_counts[item] = 1
        for item, count in item_counts.items():
            if count == x and item not in result:
                result.append(item)

        if len(result)*2 == len(input_list):
            return input_list


list1 = [1, 2, 3, 2, 1, 3]
list2 = [2, 3, 5, 1, 6]
list3 = [3, 4, 5, 6, 7]
x = 2

result = find_list(x, list1, list2, list3)
print(result)
