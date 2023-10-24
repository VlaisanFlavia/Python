# input_numbers = input("Introduceți numerele : ").split()


def is_prime(n):
    if n <= 1:
        return False

    if n <= 3:
        return True

    d = 2
    while d * d <= n:

        if n % d == 0:
            return False
        d += 1

    return True


def find_primes(list_numbers):
    list_primes = []
    for number in list_numbers:
        if is_prime(number):
            list_primes.append(number)
    return list_primes


numbers = [2, 3, 5, 6, 9, 11, 15, 17, 19, 20]
prime_numbers = find_primes(numbers)
print(prime_numbers)


