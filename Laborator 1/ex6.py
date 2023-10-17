number = input("Numarul este:")


def palindrom(number):
    ogl = 0
    aux = int(number)

    while aux:
        ogl = ogl * 10 + aux % 10
        aux = aux // 10

    if ogl == int(number):
        return "Numarul este palindrom"
    else:
        return "Numarul nu este palindrom"


result = palindrom(number)
print(result)
