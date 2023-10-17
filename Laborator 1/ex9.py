example = input("Inputul este: ")


def most_common_letter(string):
    string = string.lower()

    letter_count = {}
    max_count = 0
    max_letter = ""

    for char in string:
        if char.isalpha():
            if char in letter_count:
                letter_count[char] += 1
            else:
                letter_count[char] = 1

            if letter_count[char] > max_count:
                max_letter = char
                max_count = letter_count[char]

    return max_letter, max_count


final_result = most_common_letter(example)
print("Litera care apare de cele mai multe ori este: ",final_result)
