example = input("Textul este: ")


def count_words(string):
    count = 1

    for char in string:
        if char == ' ':
            count += 1

    return count


final_result = count_words(example)
print("Numarul de cuvinte din text este egal cu: ",final_result)
