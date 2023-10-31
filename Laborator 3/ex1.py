def lists_operations(a, b):
    intersection = set(set(a) & set(b))
    union = set(set(a) | set(b))
    a_diff_b = set(set(a) - set(b))
    b_diff_a = set(set(b) - set(a))

    return intersection, union, a_diff_b, b_diff_a


a = [1, 2, 3, 4]
b = [3, 4, 5, 6]

result = lists_operations(a, b)
print("Intersection:", result[0])
print("Union:", result[1])
print("a - b:", result[2])
print("b - a:", result[3])
