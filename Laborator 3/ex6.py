def count_unique_and_duplicate_elements(lst):
    element_count = {}

    for item in lst:
        if item in element_count:
            element_count[item] += 1
        else:
            element_count[item] = 1

    unique_count = sum(1 for count in element_count.values() if count == 1)
    duplicate_count = sum(1 for count in element_count.values() if count > 1)

    return unique_count, duplicate_count


# Exemplu de utilizare:
my_list = [1, 2, 2, 3, 4, 4, 5, 6]
unique_count, duplicate_count = count_unique_and_duplicate_elements(my_list)
print("Numarul de elemente unice:", unique_count)
print("Numarul de elemente duplicate:", duplicate_count)
