def is_palindrom(number):
    ogl = 0
    aux = int(number)

    while aux:
        ogl = ogl * 10 + aux % 10
        aux = aux // 10

    if ogl == int(number):
        return True
    else:
        return False


def return_tuple(list_numbers):
    number_pali = 0
    max_pali = 0
    for i in range(len(list_numbers)):
        if is_palindrom(list_numbers[i]):
            number_pali += 1
            if max_pali < list_numbers[i]:
                max_pali = list_numbers[i]

    return number_pali, max_pali


list_numbers = [121, 11, 23, 65, 13131]

result = return_tuple(list_numbers)

print("Number of palindromes:", result[0])
print("Greatest palindrome:", result[1])
