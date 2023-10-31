number = input("Numarul n este: ")


def fibo(n):
    fibonacci_list = []

    if int(n) <= 0:
        return -1

    if int(n) == 1:
        fibonacci_list.append(1)
        return fibonacci_list

    if int(n) == 2:
        fibonacci_list.append(1)
        fibonacci_list.append(1)
        return fibonacci_list

    fibonacci_list = [1, 1]

    while len(fibonacci_list) <= int(n):
        fibonacci_list.append(fibonacci_list[-1] + fibonacci_list[-2])

    return fibonacci_list


final_result = fibo(number)
print(final_result)
