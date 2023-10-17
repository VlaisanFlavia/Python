number = input("Numarul este: ")


def count_bit_1(number):
    count = 0
    number = int(number)

    while number:

        if int(number) % 2 == 1:
            count += 1

        number = number // 2

    return count


final_result = count_bit_1(number)
print("Numarul de bits egali cu 1 este: ",final_result)
