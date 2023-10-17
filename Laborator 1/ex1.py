def compute_gcd(x, y):
    while y:
        x, y = y, x % y
    return abs(x)


input_numbers = input("Introduceți numerele : ").split()

if len(input_numbers) > 1:
    gcd_result = int(input_numbers[0])

    for i in range(1, len(input_numbers)):
        current_number = int(input_numbers[i])
        gcd_result = compute_gcd(gcd_result, current_number)

    print("Cel mai mare divizor comun este:", gcd_result)
else:
    print("Introduceți cel puțin doua numere.")
