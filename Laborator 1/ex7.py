example = input("Inputul este:")


def extract_number(string_input):
    result = ""
    found_number = False

    for char in range(0, len(string_input)):
        if string_input[char].isdigit():
            found_number = True

            while string_input[char].isdigit():
                result += string_input[char]
                char += 1

            return int(result)

    if not found_number:
        return "Nu am gasit un numar"


result_number = extract_number(example)
print(result_number)
