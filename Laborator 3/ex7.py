def set_operations(*sets):
    result = {}

    for i in range(len(sets)):
        for j in range(i + 1, len(sets)):
            set1 = sets[i]
            set2 = sets[j]
            union_key = f"{set1} | {set2}"
            intersection_key = f"{set1} & {set2}"
            diff1_key = f"{set1} - {set2}"
            diff2_key = f"{set2} - {set1}"

            result[union_key] = set1 | set2
            result[intersection_key] = set1 & set2
            result[diff1_key] = set1 - set2
            result[diff2_key] = set2 - set1

    return result


set1 = {1, 2}
set2 = {2, 3}
result = set_operations(set1, set2)
# print(result)

for key, value in result.items():
    print(f"{key}: {value}")
